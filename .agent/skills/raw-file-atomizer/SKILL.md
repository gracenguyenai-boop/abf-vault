---
name: raw-file-atomizer
version: "2.2"
description: >
  Nhận bất kỳ file raw nào (PDF, audio, link, image, text) và tự động phân loại
  đúng nhánh + type, chuyển đổi sang Markdown sạch, tạo atomic note theo template,
  cập nhật T2 Sub-MOC.
---

# Raw File Atomizer
> Bất kỳ file nào cũng có một ngôi nhà trong vault — công việc của skill này là tìm đúng ngôi nhà đó mà không cần người dùng phải phán đoán.

---

## L1 — INTENT

### Mục đích
Tự động hoá vòng lặp "raw file vào → atomic note ra" cho vault ABF. Khi user thả bất kỳ file nào vào chat, skill này: (1) đọc và làm sạch nội dung, (2) phân loại đúng nhánh + type dựa trên semantic intent — không phải keyword, (3) chuyển sang Markdown chuẩn, (4) tạo file .md theo template đúng nhánh, (5) cập nhật T2 Sub-MOC.

### Khi nào dùng
- User thả file raw bất kỳ (PDF, audio, link, image, text, video) và muốn lưu vào vault
- User paste text thô và nói "atomize", "lưu vào vault", "phân loại cái này"
- Sau workflow run có insight/PDCA cần lưu lại vào Feed Loop

### KHÔNG dùng khi
- File đã ở dạng atomic note chuẩn (có YAML đầy đủ 17 fields)
- User chỉ muốn đọc/tóm tắt, không cần lưu vào vault
- User muốn tìm kiếm trong vault (dùng skill khác)

### Đầu ra được xem là hoàn thành khi
- File .md đã được tạo tại đúng path trong vault
- YAML hợp lệ (17 fields, không có tab, list đúng format)
- T2 Sub-MOC đã cập nhật entry mới
- MEMORY/sessions-log.md đã append log

### Phạm vi
- **Được phép**: Đọc, phân loại, chuyển đổi, ghi file .md, cập nhật MOC
- **Không được phép**: Ghi bất kỳ file nào trước khi Phase 7 được user xác nhận
- **Không được phép**: Tự quyết khi confidence < 70% — phải HỎI USER
- **Không được phép**: Bịa thêm thông tin không có trong source file

---

## L2 — KNOWLEDGE

### Tri thức nền cần có
1. **INTENT STATEMENT** — Câu tổng hợp 3 câu hỏi: Q-WHAT (nội dung nói gì?) + Q-FOR-WHOM (hữu ích cho ai?) + Q-ENABLES (người đọc làm được gì sau khi đọc?)
2. **JD của 5 nhánh** — Định nghĩa phạm vi trách nhiệm của CC / LS / TD / Shared / VJ, mỗi nhánh có Ownership Test và Exclusion Rule
3. **JD của tất cả types** — CC (L1-L4) / LS (L1-L4 + 4fcase) / TD (L1-L4, L3 có domain BDS/CK/TC/CS) / Shared (7 types) / VJ (7 types + scripts + sprint-log)
4. **Conflict logic** — Phân biệt NEW / ENRICH / DUPLICATE / SPLIT và cách xử lý từng tình huống
5. **Gap detection** — Nhận diện khi content không khớp type nào, đề xuất 3 hướng xử lý
6. **MD conversion** — Pipeline 4 bước để chuyển bất kỳ format nào sang Obsidian-compatible Markdown

### Tham chiếu bắt buộc
- @references/branch-jd.md — JD đầy đủ 5 nhánh + Ownership Tests + Exclusion Rules
- @references/type-jd.md — JD đầy đủ tất cả types + template path + path ghi
- @references/conflict-rules.md — Quy tắc NEW/ENRICH/DUPLICATE/SPLIT + spec chi tiết
- @references/gap-detection-guide.md — Phát hiện gap + đề xuất type/sub-type mới
- @references/md-conversion-guide.md — Hướng dẫn convert sang Markdown sạch

### Nguyên tắc phân loại (quan trọng)
- **KHÔNG** đếm keyword, tính điểm theo từ xuất hiện, dùng bộ tín hiệu cố định
- **PHẢI** đọc INTENT → so sánh với JD từng nhánh/type → chọn nhánh có Ownership Test = YES
- Khi nhiều nhánh YES → chọn nhánh JD mô tả INTENT gần nhất (phải giải thích lý do)
- Confidence < 70% → HỎI USER, không tự quyết

---

## L3 — EXECUTION

### Tổng quan 10 phases

```
PHASE 0: EXTRACT          → đọc file, làm sạch, tổng hợp INTENT
PHASE 1: BRANCH MATCH     → so sánh INTENT với JD 5 nhánh → chọn nhánh
PHASE 2: TYPE MATCH       → so sánh INTENT với JD type trong nhánh
PHASE 3: DOMAIN (TD/L3)   → xác định BDS / CK / TC / CS nếu TD + L3
PHASE 4: VJ ROUTE         → xác định kênh cụ thể nếu nhánh = VJ
PHASE 5: CONFLICT CHECK   → so sánh với vault → NEW / ENRICH / DUPLICATE / SPLIT
PHASE 6: GAP DETECT       → phát hiện content không khớp type nào → đề xuất
PHASE 7: PROPOSE          → trình bày đề xuất đầy đủ → DỪNG chờ user confirm
PHASE 8: CONVERT TO MD    → chuyển CLEAN_TEXT sang STRUCTURED_MD
PHASE 9: EXECUTE          → fill template + lưu file .md vào vault
PHASE 10: MOC UPDATE      → cập nhật T2 Sub-MOC + sessions-log
```

**Nguyên tắc cứng:**
- KHÔNG ghi bất kỳ file nào trước Phase 7 approve
- Confidence < 70% ở bất kỳ phase → HỎI USER
- 1 file raw = 1 lần propose (SPLIT → đề xuất tất cả cùng lúc, execute từng cái)
- Nhiều file input → xử lý serial (từng file một, không parallel)

---

### PHASE 0: EXTRACT

**Mục tiêu:** Từ bất kỳ file nào, sản xuất INTENT STATEMENT.

**0A. Đọc theo format:**

| Loại file | Xử lý | Lưu ý |
|---|---|---|
| PDF (có text layer) | Đọc trực tiếp, tóm tắt nếu >5000 chữ | Xử lý encoding artifact ở 0B |
| PDF (scan) | OCR → đánh dấu `ocr: true` | Chất lượng thấp hơn |
| Audio (.mp3/.m4a/.wav) | Transcribe | `[INAUDIBLE: ~X giây]` nếu không rõ |
| Image / screenshot | OCR + mô tả context hình ảnh | |
| Link bài báo | Crawl full article | Dừng nếu paywall, không hallucinate |
| Text / .md / .txt | Đọc trực tiếp | |
| Video | Extract key points từ transcript | |

**0B. Làm sạch text (bắt buộc mọi loại):**
1. Encoding artifacts (PDF): chữ dính nhau `CHÂNDUNGKÊNH` → `CHÂN DUNG KÊNH`
2. HTML artifacts: strip tags, `<table>` → MD table, `<ul>` → `- list`
3. Audio noise: filler words (`ừm`, `à à`), timestamps không cần thiết
4. Diacritical marks tiếng Việt: đảm bảo UTF-8, không bị mất dấu
5. Duplicates: tiêu đề lặp, header/footer báo, quảng cáo xen giữa

**0C. Tổng hợp INTENT (3 câu hỏi bắt buộc):**
```
Q-WHAT    : Nội dung này nói về điều gì? (1-2 câu)
Q-FOR-WHOM: Hữu ích cho ai trong hệ thống ABF? (CC / LS / TD / VJ / tất cả)
Q-ENABLES : Sau khi đọc, người đọc làm được / hiểu được điều gì cụ thể?
```

Tổng hợp thành:
```
INTENT: "[Q-WHAT]. Hữu ích cho [Q-FOR-WHOM] vì [Q-ENABLES]."
```

**Output bắt buộc Phase 0:**
```
SOURCE_TYPE : [pdf/audio/image/link/text/video]
SUMMARY     : [3-5 câu tóm tắt]
INTENT      : [câu INTENT đầy đủ]
MULTI_NOTE  : [YES/NO] — có nhiều chủ đề cần tách thành nhiều note không?
```

---

### PHASE 1: BRANCH MATCH

So sánh INTENT với JD của 5 nhánh. Với mỗi nhánh, trả lời Ownership Test (YES/NO/PARTIAL).

| Nhánh | Ownership Test tóm tắt |
|---|---|
| CC | "Nội dung này giúp VIẾT NỘI DUNG TỐT HƠN không?" |
| LS | "Nội dung này giúp XỬ LÝ HỒ SƠ VAY CỤ THỂ không?" |
| TD | "Nội dung này mô tả THẾ GIỚI BÊN NGOÀI ảnh hưởng đến quyết định vay không?" |
| Shared | "Nếu xóa note này, cả CC lẫn LS lẫn TD đều thiếu không?" |
| VJ | "Nội dung này CHỈ có ý nghĩa khi gắn với kênh TikTok cụ thể không?" |

→ Xem JD đầy đủ + Exclusion Rules: @references/branch-jd.md

**Cơ chế quyết định:**
```
BƯỚC 1: Đọc INTENT từ Phase 0
BƯỚC 2: Trả lời Ownership Test từng nhánh (YES / NO / PARTIAL)
BƯỚC 3:
  - Đúng 1 YES → nhánh đó thắng
  - Nhiều YES → chọn nhánh JD mô tả INTENT gần nhất (giải thích lý do)
  - Không YES nào rõ → Confidence < 70% → HỎI USER
BƯỚC 4: Kiểm tra Exclusion Rule → nếu content bị loại trừ → reconsider
```

---

### PHASE 2: TYPE MATCH

So sánh INTENT với JD type trong nhánh đã chọn.

| Nhánh | Types |
|---|---|
| CC | L1-Framework / L2-KienThucNghe / L3-KienThucDacThu / L4-PDCA |
| LS | L1-Framework / L2-KienThucNghe / L3-KienThucDacThu / L4-PDCA / L4/4fcase |
| TD | L1-Framework / L2-KienThucNghe / L3-KienThucDacThu (→ Phase 3 domain) / L4-PDCA |
| Shared | concept / framework / insight / perspective / story / strategy / quote |
| VJ | concept / framework / insight / perspective / story / strategy / quote |

→ Xem JD đầy đủ từng type + template path: @references/type-jd.md

---

### PHASE 3: DOMAIN (chỉ khi TD + L3)

Áp dụng khi nhánh = TD **và** type = L3-KienThucDacThu.

| Domain | Path | Ownership Test |
|---|---|---|
| BDS | `TD-01-Atomic/L3-KienThucDacThu/BDS/` | "Gắn chính với thị trường nhà đất, dự án, giá BĐS?" |
| CK | `TD-01-Atomic/L3-KienThucDacThu/CK/` | "Gắn chính với cổ phiếu, chỉ số, IPO, ĐHĐCĐ?" |
| TC | `TD-01-Atomic/L3-KienThucDacThu/TC/` | "Gắn chính với lãi suất, NHNN, tín dụng, ngân hàng?" |
| CS | `TD-01-Atomic/L3-KienThucDacThu/CS/` | "Gắn chính với luật mới, nghị định, thuế, quy định?" |

**Rule cross-domain:** Đặt vào domain có tác động trực tiếp nhất đến quyết định vay/đầu tư của KH. Thêm tag domain phụ vào YAML topics nếu chồng lấn. Không xác định được → HỎI USER.

---

### PHASE 4: VJ ROUTE (chỉ khi VJ)

| Cách nhận biết | Kênh |
|---|---|
| File đề cập tên VJ / kênh rõ ràng | Match kênh tương ứng |
| Script có DNA giọng rõ (xưng hô, tone) | Phân tích DNA → match kênh |
| Không xác định được | HỎI USER — KHÔNG tự gán |

- Script đã ship → `VJ/VJ-[kênh]/scripts/YYYY-MM-DD-[topic].md` (không phải atomic note)
- Sprint log → append vào `VJ/VJ-[kênh]/VJ-01-Atomic/sprint-log.md` (không tạo file mới)

**VJ Insight "Promote Lên Vault" — khi nào SPLIT sang nhánh khác:**

Template `_template-insight.md` có checklist "Promote Lên Vault?" — dùng rule sau:

| Điều kiện | Hành động |
|---|---|
| Insight CHỈ có ý nghĩa với kênh này (viewer sentiment, data video cụ thể) | Giữ trong VJ branch, KHÔNG promote |
| Insight chứa pattern content chung (không gắn kênh cụ thể) | SPLIT: VJ/insight + CC/L3 note |
| Insight chứa thông tin thị trường phổ biến | SPLIT: VJ/insight + TD/L3 note |
| Insight chứa nghiệp vụ tín dụng chung | SPLIT: VJ/insight + LS/L2 note |

→ Nếu cần SPLIT: đề xuất trong Phase 7, KHÔNG tự execute. Chờ user xác nhận.
→ Không chắc → HỎI USER.

---

### PHASE 5: CONFLICT CHECK

1. Lấy 3-5 từ khoá cốt lõi từ INTENT
2. Search vault → top 5 kết quả gần nhất

**Phạm vi search (bao gồm):**
- ✅ Atomic notes: `CC-ContentCreator/CC-01-Atomic/`, `LS-LoanSpecialist/LS-01-Atomic/`, `TD-TraDa/TD-01-Atomic/`, `Shared/Shared-01-Atomic/`, `VJ/VJ-[kênh]/VJ-01-Atomic/`

**Phạm vi search (loại trừ):**
- ❌ `VJ/VJ-[kênh]/scripts/` — scripts là output đã ship, không phải knowledge base
- ❌ `*-MOC.md` — navigation file, không phải atomic note
- ❌ `MEMORY/` — session log, không phải vault knowledge

3. Đọc YAML + summary của từng kết quả, so sánh INTENT

| Tình huống | Điều kiện | Hành động mặc định |
|---|---|---|
| NEW | Không có note nào INTENT gần giống | Tạo mới |
| ENRICH | Cùng chủ đề nhưng có dữ liệu/góc nhìn mới | Thêm section vào note cũ, update YAML |
| DUPLICATE | Gần như giống hệt (INTENT + type) | Đề xuất SKIP; REPLACE cần explicit "replace" |
| SPLIT | File chứa ≥2 INTENT khác nhau cần tách | Tạo nhiều note, đề xuất tất cả cùng lúc |
| UNCLEAR | Không đủ cơ sở đánh giá | HỎI USER |

→ Spec chi tiết ENRICH + SPLIT: @references/conflict-rules.md

---

### PHASE 6: GAP DETECT

**Trigger:** Sau Phase 2, không có type nào có Ownership Test = YES rõ ràng.

```
⚠️ GAP DETECTED — [Type/Branch] mismatch
Nhánh xác định : [CC/LS/TD/Shared/VJ]
Vấn đề         : [mô tả vấn đề cụ thể]
Type gần nhất  : [type] — thiếu [điều kiện X]
Đề xuất:
  A: Ép vào [type gần nhất] (có thể mất một số đặc trưng)
  B: Tạo sub-type "[tên đề xuất]" dưới [nhánh/lớp]/
  C: Tách thành [type A] + [type B]
→ Chờ user chọn
```

→ Chi tiết 3 loại gap + cách xử lý: @references/gap-detection-guide.md

---

### PHASE 7: PROPOSE (BLOCKING CHECKPOINT)

Hiển thị đầy đủ rồi DỪNG — không tự động execute:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 ĐỀ XUẤT ATOMIZE — [tên file gốc]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTENT     : [câu INTENT từ Phase 0]
Source type: [pdf/audio/image/link/text]

PHÂN LOẠI:
  Nhánh    : [CC/LS/TD/Shared/VJ-X]
  Lý do    : "[Ownership Test] → YES vì [lý do cụ thể]"
  Type     : [type/layer]
  Lý do    : "[Ownership Test] → YES vì [lý do cụ thể]"
  Branch   : [giá trị sẽ điền vào YAML field branch]
  Layer    : [giá trị sẽ điền vào YAML field layer — ghi null nếu VJ/Shared]
  Domain   : [BDS/CK/TC/CS — chỉ khi TD/L3]
  Kênh VJ  : [chỉ khi VJ]

ĐẦU RA:
  Path     : [đường dẫn đầy đủ từ vault root]
  Tên file : [YYYY-MM-DD-slug-title.md]
  Template : [tên template sẽ dùng]

CONFLICT:
  Tình huống    : [NEW/ENRICH/DUPLICATE/SPLIT]
  Note liên quan: [[path]] — [mô tả nếu có]

GAP: [Không có / Có: mô tả + options A/B/C]

[Nếu SPLIT — liệt kê TẤT CẢ N note cần tạo]

MOC CẦN CẬP NHẬT:
  1. [T2 Sub-MOC path] — vd: CC-L2-MOC.md / TD-L3-TC-MOC.md / MOC-VJ-Khang.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Xác nhận? (yes / chỉnh sửa [field] / skip)
```

**RULE tuyệt đối:** Phase 8, 9, 10 không chạy nếu chưa có "yes" từ user.

---

### PHASE 8: CONVERT TO MD

Từ `CLEAN_TEXT` (Phase 0B) → `STRUCTURED_MD` sẵn sàng điền vào template.

**8A. Phát hiện cấu trúc nguồn** (tiêu đề, danh sách, bảng, quote, đoạn văn thường)

**8B. Map sang Markdown:**

| Cấu trúc nguồn | Output Markdown |
|---|---|
| Tiêu đề lớn | `## Tiêu đề` |
| Tiêu đề nhỏ | `### Tiêu đề con` |
| Danh sách unordered | `- item` |
| Danh sách ordered | `1. item` |
| Bảng dữ liệu | `\| col \| col \|` (MD table) |
| Trích dẫn / quote | `> "câu"` |
| Nhấn mạnh quan trọng | `**từ**` |
| Số liệu quan trọng | Giữ nguyên, không in đậm |

**8C. Chuẩn hoá Obsidian:**
- Tên file: `YYYY-MM-DD-slug-title.md` — không dấu tiếng Việt trong tên file, giữ dấu trong content
- Internal links: `[[note-name]]`
- KHÔNG dùng HTML trong .md file
- KHÔNG trailing spaces

**8D. Validate YAML trước khi lưu:**
- String có ký tự đặc biệt (`:`, `#`, `"`) → phải trong `""`
- topics phải là list: `["topic1", "topic2"]` — không phải string
- Indent 2 spaces, KHÔNG dùng tab
- Mở và đóng bằng `---`

→ Chi tiết từng loại file: @references/md-conversion-guide.md

---

### PHASE 9: EXECUTE

**9A. Template path theo nhánh + type:**

| Nhánh | Type/Layer | Template |
|---|---|---|
| CC | L1-Framework | `CC-ContentCreator/CC-01-Atomic/L1-Framework/_template-framework.md` |
| CC | L2-KienThucNghe | `CC-ContentCreator/CC-01-Atomic/L2-KienThucNghe/_template-concept-writing.md` |
| CC | L3-KienThucDacThu | `CC-ContentCreator/CC-01-Atomic/L3-KienThucDacThu/_template-domain-abf.md` |
| CC | L4-PDCA | `CC-ContentCreator/CC-01-Atomic/L4-PDCA/_template-pdca-review.md` |
| LS | L1-Framework | `LS-LoanSpecialist/LS-01-Atomic/L1-Framework/_template-framework-ls.md` |
| LS | L2-KienThucNghe | `LS-LoanSpecialist/LS-01-Atomic/L2-KienThucNghe/_template-concept-banking.md` |
| LS | L3-KienThucDacThu | `LS-LoanSpecialist/LS-01-Atomic/L3-KienThucDacThu/_template-domain-banking-ops.md` |
| LS | L4/4fcase | `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/_template-4fcase.md` |
| TD | L1-Framework | `TD-TraDa/TD-01-Atomic/L1-Framework/_template-framework-td.md` |
| TD | L2-KienThucNghe | `TD-TraDa/TD-01-Atomic/L2-KienThucNghe/_template-concept-macro.md` |
| TD | L3-KienThucDacThu | `TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/_template-domain-macro.md` |
| TD | L4-PDCA | `TD-TraDa/TD-01-Atomic/L4-PDCA/_template-td-pdca.md` |
| Shared | 7 types | `VJ/_templates/_template-[type].md` (YAML branch: Shared) |
| VJ | 7 types | `VJ/_templates/_template-[type].md` (YAML branch: VJ-[kênh]) |

**9B. Fill YAML (17 fields bắt buộc):**
```yaml
---
name: [slug-title]
type: [concept/insight/framework/story/perspective/strategy/quote/4fcase/pdca]
branch: [CC/LS/TD/Shared/VJ-AnBinh/VJ-Dat/VJ-Khang/VJ-Thuy]
layer: [L1-Framework/L2-KienThucNghe/L3-KienThucDacThu/L4-PDCA/null]
subtype: [chi tiết hơn về loại]
topics: ["topic1", "topic2"]
status: raw
created: YYYY-MM-DD
source: "[tên file gốc hoặc link]"
confidence: [high/medium/low]
verified: false
related: ["[[{Branch}-{Layer}-MOC]]"]
maturity: seed
review_interval: 30
next_review: YYYY-MM-DD
reuse_count: 0
evolution_log: []
---
```

**Quy tắc `related` — luôn trỏ T2 Sub-MOC, KHÔNG phải T1 Branch MOC:**

| Branch | Layer / Domain | Giá trị `related` |
|---|---|---|
| CC | L1-Framework | `[[CC-L1-MOC]]` |
| CC | L2-KienThucNghe | `[[CC-L2-MOC]]` |
| CC | L3-KienThucDacThu | `[[CC-L3-MOC]]` |
| CC | L4-PDCA | `[[CC-L4-MOC]]` |
| LS | L1-Framework | `[[LS-L1-MOC]]` |
| LS | L2-KienThucNghe | `[[LS-L2-MOC]]` |
| LS | L3-KienThucDacThu | `[[LS-L3-MOC]]` |
| LS | L4-PDCA / 4fcase | `[[LS-L4-MOC]]` |
| TD | L1-Framework | `[[TD-L1-MOC]]` |
| TD | L2-KienThucNghe | `[[TD-L2-MOC]]` |
| TD | L3 / TC | `[[TD-L3-TC-MOC]]` |
| TD | L3 / BDS | `[[TD-L3-BDS-MOC]]` |
| TD | L3 / CS | `[[TD-L3-CS-MOC]]` |
| TD | L3 / CK | `[[TD-L3-CK-MOC]]` |
| TD | L4-PDCA | `[[TD-L4-MOC]]` |
| Shared | type: `framework` | `[[Shared-L1-MOC]]` |
| Shared | type: `concept` / `insight` / `perspective` | `[[Shared-L2-MOC]]` |
| Shared | type: `story` / `quote` | `[[Shared-L3-MOC]]` |
| Shared | type: `strategy` | `[[Shared-L4-MOC]]` |
| VJ-Khang | News hoặc Case Study | `[[MOC-VJ-Khang]]` |
| VJ-AnBinh | any | `[[MOC-VJ-AnBinh]]` |
| VJ-Dat | any | `[[MOC-VJ-Dat]]` |
| VJ-Thuy | any | `[[MOC-VJ-Thuy]]` |

> ⚠️ **Shared `layer: null`** — Shared dùng 7 semantic types (concept/framework/insight/perspective/story/quote/strategy), không phải hệ L1-L4. Chọn T2 Sub-MOC theo cột `type` ở bảng trên. Điền `layer: null` trong YAML — không bao giờ điền L1/L2/L3/L4 cho Shared.

**Rule fill `branch` và `layer`:**

| Nhánh | branch | layer |
|---|---|---|
| CC | `CC` | `L1-Framework` / `L2-KienThucNghe` / `L3-KienThucDacThu` / `L4-PDCA` |
| LS | `LS` | `L1-Framework` / `L2-KienThucNghe` / `L3-KienThucDacThu` / `L4-PDCA` |
| TD | `TD` | `L1-Framework` / `L2-KienThucNghe` / `L3-KienThucDacThu` / `L4-PDCA` |
| Shared | `Shared` | `null` |
| VJ | `VJ-AnBinh` / `VJ-Dat` / `VJ-Khang` / `VJ-Thuy` | `null` |

> `layer` lấy giá trị từ kết quả Phase 2 (TYPE MATCH). VJ và Shared không dùng L-level → ghi `null`.

**9C. Fill nội dung:**
- Điền STRUCTURED_MD từ Phase 8 vào sections của template
- Không bịa thêm thông tin không có trong source
- Section bắt buộc bị thiếu data → ghi `[CẦN BỔ SUNG]`
- Không copy nguyên văn >200 chữ liên tục (phải paraphrase)

**9D. Rollback nếu Phase 10 thất bại:**
- File note đã tạo → KHÔNG xóa
- Cập nhật YAML: `status: raw-moc-pending`
- Ghi vào `MEMORY/blockers.md`: path note cần update MOC thủ công

---

### PHASE 10: MOC UPDATE

**10A. Sub-MOC (T2)** — path từ kết quả Phase 2 + 3, xem bảng mapping trong Phase 9B

Tìm section đúng với type/domain vừa tạo, append vào cuối (không chèn giữa):
```markdown
| [[relative-path/YYYY-MM-DD-slug]] | [mô tả ≤80 ký tự] |
```
Nếu section chưa tồn tại → tạo section mới ở cuối file.

> ⚠️ KHÔNG cập nhật T1 Branch MOC hay T0 MOC-MASTER với link đến atomic note riêng lẻ.
> T0 và T1 chỉ link đến tier liền kề — không link thẳng xuống T3.

**10B. MEMORY/sessions-log.md** — Append:
```
## [YYYY-MM-DD] Atomize: [tên file gốc]
- Branch: [CC/LS/TD/Shared/VJ-X] | Type: [type] | Conflict: [NEW/ENRICH/DUPLICATE]
- Created: [[path/to/note]]
- MOC updated: [T2 Sub-MOC — vd: CC-L2-MOC / TD-L3-TC-MOC]
```

**Quy tắc format MOC:**
- Dùng em dash `—` (không phải `-`)
- Mô tả: tóm tắt INTENT trong ≤80 ký tự, không có dấu chấm cuối

---

## L4 — VERIFICATION

### Checklist từng phase

**Phase 0:**
- [ ] INTENT có đủ 3 yếu tố (WHAT / FOR-WHOM / ENABLES)?
- [ ] CLEAN_TEXT đã xử lý encoding / HTML / transcript noise?
- [ ] MULTI_NOTE đã xác định (YES/NO)?

**Phase 1-2:**
- [ ] Branch được chọn dựa trên Ownership Test (không phải keyword count)?
- [ ] Khi nhiều nhánh YES → có giải thích lý do chọn?
- [ ] Confidence ≥ 70%?

**Phase 7:**
- [ ] Đã hiển thị đầy đủ propose block và DỪNG chờ user?
- [ ] SPLIT → đã liệt kê TẤT CẢ note trong 1 lần propose?

**Phase 8-9:**
- [ ] YAML valid (không tab, topics là list, string có dấu ngoặc kép khi cần)?
- [ ] `branch` và `layer` đã fill đúng theo bảng rule trong Phase 9B?
- [ ] Không có section bắt buộc nào bỏ trống không báo?
- [ ] Không copy nguyên văn >200 chữ liên tục?

**Phase 10:**
- [ ] T2 Sub-MOC đã update entry mới (KHÔNG update T1 Branch MOC hay T0 MOC-MASTER)?
- [ ] sessions-log.md đã append?
- [ ] Nếu MOC fail → blockers.md đã ghi + status: raw-moc-pending?

### Edge cases

| Tình huống | Xử lý |
|---|---|
| File >5000 chữ | Summarize trước, tạo note từ summary (không toàn văn) |
| PDF scan | OCR + đánh dấu `ocr: true` trong YAML |
| Paywall | Dừng, báo user, KHÔNG hallucinate |
| Audio kém | `[INAUDIBLE: ~X giây]`, hỏi user bù thông tin |
| File tiếng Anh | Xử lý bình thường, thêm `"language": "en"` vào topics |
| SPLIT ≥3 notes | Propose tất cả cùng 1 lần, execute từng cái sau approve |
| DUPLICATE | SKIP mặc định; REPLACE cần "replace" explicit từ user |
| 4fcase thiếu F | Lưu vào `LS-00-Inbox/incomplete/`, không tạo 4fcase chưa đủ |
| YAML validation fail | DỪNG, báo lỗi cụ thể, không lưu file lỗi |
| MOC file không tồn tại | Tạo skeleton MOC mới trước khi add entry |
| Kênh VJ không xác định | HỎI USER, KHÔNG tự gán |
| Nhiều file cùng lúc | Xử lý serial (từng file một) |
| ENRICH note cũ | Thêm section mới `## [Nguồn bổ sung] — [ngày]`, update YAML reuse_count |

### Câu hỏi cuối
> Nếu atomic note này được dùng ngay trong workflow hôm nay, người đọc có hiểu ngay đây là gì và tìm thêm ở đâu không?

---

## L5 — EVOLUTION

### Version hiện tại: v2.2

### Changelog
- **v2.2** (2026-05-24): Fix L1 section bugs (15 fields → 17 fields, "Branch MOC" → "T2 Sub-MOC", xóa MOC-MASTER khỏi completion criteria, "2 lớp MOC" → "T2 Sub-MOC"). Fix Shared `related` table (dùng type names thay L-level labels, thêm cảnh báo `layer: null`). Thêm Phase 5 search scope (loại trừ scripts/, MOC files, MEMORY/). Thêm Phase 4 VJ promote flow rule. Thêm edge cases: LS/TD lãi suất, CC/Shared kỹ năng viết, LS L3/TD CS regulatory. Thêm CC L1 vs L2 boundary table. Thêm TD L3 domain combo rule. Fix 7 VJ templates (branch/layer YAML fields, related placeholder). Mở rộng VJ type-jd với JD + Ownership Tests + boundary table cho 7 types.
- **v2.1** (2026-05-23): Thêm field `branch` và `layer` vào YAML (15 fields → 17 fields). Fix bug type vocabulary collision — TD/L3 và VJ/insight đều ra `type: insight`, workflow không phân biệt được nguồn gốc. Nay dùng `branch` + `layer` để route chính xác khi query. Cập nhật Phase 7 PROPOSE block + L4 checklist.
- **v2.0** (2026-05-22): Thay keyword matching bằng JD-based semantic matching. Thêm Phase 8 (MD conversion pipeline). Thêm Phase 6 (gap detection). Thêm L4 verification checklist. Thêm VJ templates.
- **v1.0**: Khởi tạo.

### Gotchas đã gặp
- Chưa có — cập nhật khi gặp lỗi lặp lại > 2 lần.

### Cách cập nhật skill này
- Lỗi classification → cập nhật L3 Phase 1-2 + @references/branch-jd.md hoặc type-jd.md
- Lỗi MD format → cập nhật L3 Phase 8 + @references/md-conversion-guide.md
- Type mới được approve → cập nhật L3 Phase 2 type table + @references/type-jd.md
- Edge case mới gặp → cập nhật L4 edge cases table
- Conflict rule thay đổi → cập nhật @references/conflict-rules.md
