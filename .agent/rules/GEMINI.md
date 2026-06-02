# GEMINI.md — Luật Tối Cao

> Đọc file này TRƯỚC KHI làm bất cứ điều gì. Không có ngoại lệ.
> Paths và routing: fetch `VAULT-STRUCTURE-REF.md` từ vault (xem Bước 0).

---

## ⚙️ HỆ THỐNG — Vault kết nối qua GitHub Raw URL

```
Base URL: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main
Tool:     [crawler] — có sẵn trong Antigravity, không cần cài thêm gì
```

**Cách đọc bất kỳ file nào trong vault:**
```
fetch: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/<path-tới-file>
```

Ví dụ:
```
MEMORY/decisions.md
→ https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/decisions.md

.agent/workflows/TikTok-case-study-workflow.md
→ https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/TikTok-case-study-workflow.md
```

> ⛔ KHÔNG dùng `run_command`, `curl`, `mcp_obsidian_*`, hay bất kỳ MCP server nào khác.
> ✅ CHỈ dùng [crawler] để fetch raw URL. Đơn giản, không cần setup.

---

## ⚡ BOOTSTRAP — LỆNH ĐẦU TIÊN, TUYỆT ĐỐI

### ⛔ CẤM TUYỆT ĐỐI trước khi chạy Phase 0:
- CẤM đọc bất kỳ file nào ngoài GEMINI.md
- CẤM crawl web ngoài vault
- CẤM hỏi VJ thêm thông tin

### Khi nhận BẤT KỲ prompt nào từ VJ:

⛔ DỪNG. Hiển thị **2 vòng chip liền mạch** — vòng 2 hiện ngay sau vòng 1, không có bước nào ở giữa. KHÔNG tự đoán.

> **Shortcut rule:** Nếu prompt đã chứa đủ thông tin (ví dụ: *"thuỷ case study đóng vai"*) → extract field đã có, bỏ qua các vòng tương ứng, chạy PHASE 0 luôn.

---

**VÒNG 1 — Kênh + Workflow (2 chip cùng lúc):**

```
🎬 ABF Workflow

Chọn kênh:
  ╔══════════════════╗  ╔══════════════════╗
  ║ An Bình Vay Vốn  ║  ║ Khang Vay Hay    ║
  ╚══════════════════╝  ╚══════════════════╝
  ╔══════════════════╗  ╔══════════════════╗
  ║ Thuỷ Vay Vốn     ║  ║ Đạt Vay Đơn Giản ║
  ╚══════════════════╝  ╚══════════════════╝

Chọn workflow:
  ╔══════════════╗  ╔══════════════╗
  ║ News Viral   ║  ║ Case Study   ║
  ╚══════════════╝  ╚══════════════╝
  [+ Kiến Thức Vay Vốn · An Bình Là Ai — chỉ hiện nếu VJ = An Bình]
```

⛔ DỪNG — chờ VJ chọn xong cả 2. **Ngay lập tức** hiện VÒNG 2 — không in text, không xử lý gì ở giữa.

---

**VÒNG 2 — Nội dung + Format đã lọc (2 chip cùng lúc):**

Dòng hỏi nội dung theo workflow:
- News Viral        → `Nội dung news cần phân tích — dán link hoặc mô tả:`
- Case Study        → `Nội dung case cần phân tích — dán file hồ sơ / ghi chú 4F:`
- Kiến Thức Vay Vốn → `Chủ đề cần phân tích:`
- An Bình Là Ai     → `Nội dung cần phân tích:`

Format chip — **chỉ hiện format hợp lệ theo bảng VJ × Workflow:**

| VJ | News Viral | Case Study | KTVV / ABLA |
|---|---|---|---|
| An Bình | talking-head · tips-nhanh | talking-head · tips-nhanh | talking-head · tips-nhanh |
| Khang | talking-head · tips-nhanh | talking-head · tips-nhanh · giai-quyet-thuc-dia · selfie · tu-van-hoi-thoai | — |
| Thuỷ | talking-head · tips-nhanh | talking-head · tips-nhanh · dong-vai | — |
| Đạt | talking-head · tips-nhanh | talking-head · tips-nhanh · trong-xe-o-to · nghe-dien-thoai · cam-giay-to | — |

```
[Dòng hỏi nội dung theo workflow] ↓
→ _______________________________________________

Chọn format quay:
  [chỉ chip format hợp lệ của VJ × Workflow đã chọn]
```

⛔ DỪNG — chờ VJ nhập nội dung và chọn format. Sau khi có đủ → lưu working memory → chạy PHASE 0 ngay.

---

→ Sau khi có đủ 4 bước → lưu working memory:
   `VJ = [X]` | `WORKFLOW = [Y]` | `FORMAT = [Z]` | `INPUT = [W]`

```
✅ Kênh: [X]   Workflow: [Y]   Format: [Z]   Nội dung: nhận ✓
→ Đang khởi động PHASE 0...
```

→ Chạy PHASE 0.
→ Sau Phase 0 → fetch workflow file từ vault → chạy từ Phase 1.
⛔ KHÔNG làm gì khác giữa Phase 0 và workflow.

---

## 🔄 PHASE 0 — PRE-PROCESSING (BẮT BUỘC)

**⚠️ PHASE 0 CÓ 6 BƯỚC. SAU BƯỚC 6 → LOAD WORKFLOW.**
**⚠️ PHASE 0 LÀ CỦA GEMINI — khi load workflow, BỎ QUA Phase 0 của workflow, bắt đầu từ Phase 1.**

**⏱️ TIMEOUT: Mỗi bước tối đa 30 giây.**
Bước nào quá thời gian → ghi nhận, bỏ qua, sang bước tiếp. KHÔNG retry, KHÔNG loop.

---

### Bước 0 — Đọc VAULT-STRUCTURE-REF + Memory từ Vault

Fetch **song song cùng lúc** 5 URLs sau bằng [crawler]:

```
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/rules/VAULT-STRUCTURE-REF.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/decisions.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/blockers.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/sessions-log.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/preferences.md
```

File nào fetch thất bại → bỏ qua, tiếp tục. ⏱️ Timeout 20 giây tổng.
→ Tóm tắt 1 dòng: `"Session trước: [X]. Hôm nay: [Y]."`

---

### Bước 1 — Nhận + Đọc Hiểu Raw Input (BẮT BUỘC)

VJ gửi files + links + text → AG KHÔNG chỉ ACK, phải:
1. **Nhận diện file type:** Link / Audio / Image / Text / Doc
2. **Đọc + xử lý toàn bộ nội dung:**
   - Link → [crawler] đọc toàn bài
   - Audio → [audio-transcribe]
   - Image → [understand-images]
   - Text/Doc → đọc và tóm tắt
3. **Nội suy và hiểu sâu:** Vấn đề cốt lõi? Số liệu quan trọng? Bối cảnh? Ai liên quan?

→ Output bắt buộc: `[Tóm tắt nội dung]` + `[Vấn đề cốt lõi]` + `[Bối cảnh]`
⏱️ Timeout 1 phút → tóm tắt từng phần đã đọc được, tiếp tục.

---

### Bước 2 — Tìm Kiến Thức Liên Quan Từ Vault

Dựa trên hiểu biết từ Bước 1, fetch MOC trước để biết vault có gì:

```
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MOC-MASTER.md
```

Từ MOC, xác định 1–2 file atomic notes liên quan nhất → fetch thêm bằng [crawler].
⏱️ Timeout 30 giây → ghi nhận những gì tìm được, tiếp tục.
→ Output: `[Kiến thức vault liên quan]`

---

### Bước 2.5 — Load kịch bản mẫu theo VJ + format

**Cấu trúc folder thực tế:**
```
scripts/
  VJ-AnBinh/scripts/
    talking-head/       ← 16 scripts + _RULE
    tips-nhanh/         ← 13 scripts + _RULE
  VJ-Dat/scripts/
    talking-head/       ← 9 scripts + _RULE
    tips-nhanh/         ← 16 scripts + _RULE
    trong-xe-o-to/      ← 10 scripts + _RULE
    nghe-dien-thoai/    ← 2 scripts + _RULE
    cam-giay-to/        ← 1 script + _RULE
  VJ-Khang/scripts/
    talking-head/       ← 13 scripts + _RULE
    tips-nhanh/         ← 7 scripts + _RULE
    giai-quyet-thuc-dia/ ← 12 scripts + _RULE
    selfie/             ← 10 scripts + _RULE
    tu-van-hoi-thoai/   ← 3 scripts + _RULE
  VJ-Thuy/scripts/
    talking-head/       ← 33 scripts + _RULE
    tips-nhanh/         ← 4 scripts + _RULE
    dong-vai/           ← 9 scripts + _RULE
```

**Logic load — 2 bước lọc:**

**Bước 1 — Lọc theo VJ:**

| VJ chọn | Folder |
|---|---|
| A — An Bình Vay Vốn | `VJ-AnBinh` |
| B — Khang Vay Hay | `VJ-Khang` |
| C — Thuỷ Vay Vốn | `VJ-Thuy` |
| D — Đạt Vay Đơn Giản | `VJ-Dat` |

**Bước 2 — Lọc theo format trong VJ đó:**

User chọn format từ danh sách format thực tế của VJ đó (xem bảng trên). GEMINI hiển thị đúng danh sách format có sẵn theo VJ — không hiển thị format không tồn tại.

Ví dụ: VJ = Khang → hiển thị: `talking-head / tips-nhanh / giai-quyet-thuc-dia / selfie / tu-van-hoi-thoai`

**Path cuối cùng:**
```
VJ/[VJ-folder]/scripts/[format-folder]/
```
Ví dụ: VJ = Khang + format = talking-head → `VJ/VJ-Khang/scripts/talking-head/`

→ **Fetch strategy file của VJ trước** — đọc bắt buộc, lưu nhãn `[CHANNEL STRATEGY]`:

| VJ | Path strategy file |
|---|---|
| A — An Bình | `VJ/VJ-AnBinh/VJ-01-Atomic/strategy/2026-05-23-dinh-huong-kenh-vay-von-an-binh.md` |
| B — Khang | `VJ/VJ-Khang/VJ-01-Atomic/strategy/2026-05-24-chan-dung-kenh-khang-bank.md` |
| C — Thuỷ | `VJ/VJ-Thuy/VJ-01-Atomic/strategy/2026-05-24-chan-dung-kenh-thuy-bank.md` |
| D — Đạt | `VJ/VJ-Dat/VJ-01-Atomic/strategy/2026-05-23-dinh-huong-kenh-dat-lam-tai-chinh.md` |

`[CHANNEL STRATEGY]` là nguồn định hướng kênh — đọc trước tất cả, dùng làm nền tảng cho toàn bộ quá trình viết.

→ Fetch file `_RULE-*` — đọc bắt buộc, lưu nhãn `[FORMAT RULE]`.
→ Fetch toàn bộ file `.md` còn lại trong folder → đọc frontmatter, lọc theo field `workflow-tags`.
→ Chỉ giữ file có `workflow-tags` chứa giá trị khớp với workflow đang chạy → lưu nhãn `[EXAMPLE SCRIPTS]`.
→ Output: `📚 Đã load [CHANNEL STRATEGY] + [n] kịch bản mẫu + 1 _RULE — VJ: [X], format: [Y], workflow: [Z].`

**Bảng mapping workflow → giá trị workflow-tags:**

| Workflow chọn | Giá trị cần có trong `workflow-tags` |
|---|---|
| 1 — News Viral | `news` |
| 2 — Case Study | `case-study` |
| 3 — Kiến Thức Vay Vốn | `ktvv` |
| 4 — An Bình Là Ai | `abla` |

**Quy tắc lọc:**
- File có `workflow-tags` chứa giá trị khớp → đưa vào `[EXAMPLE SCRIPTS]`
- File không có `workflow-tags` hoặc không khớp → bỏ qua
- Nếu sau khi lọc còn < 3 file → bỏ filter, load toàn bộ (không đủ mẫu)
- File `_RULE-*` → không lọc, load bắt buộc

⏱️ Timeout 30 giây tổng. File nào fetch thất bại → bỏ qua, tiếp tục.
⛔ Folder trống hoặc không tồn tại → báo VJ thêm scripts mẫu vào `scripts/[VJ-folder]/scripts/[format]/`, tiếp tục Phase 0 không có examples.

---

### Bước 2.6 — Phân tích examples (Pattern Extraction)

Chạy ngay sau Bước 2.5. Không cần gọi skill — GEMINI tự phân tích `[EXAMPLE SCRIPTS]` đã load.

Đọc toàn bộ `[EXAMPLE SCRIPTS]` và extract 6 pattern sau, output trực tiếp vào working memory nhãn `[EXAMPLE ANALYSIS]`:

```
[EXAMPLE ANALYSIS]
① Độ dài trung bình : [X] từ (Hook: ~Xw / Body: ~Xw / CTA: ~Xw)
② Cấu trúc phổ biến: [mô tả 1-2 câu — ví dụ: "Hook = số liệu sốc + câu hỏi, Body = 3 điểm đánh số, CTA = câu hỏi thảo luận"]
③ Từ/cụm đặc trưng : [liệt kê 5-8 cụm hay xuất hiện — ví dụ: "nói thật nhé / anh chị ơi / mình vừa / thật ra / đừng chờ"]
④ Điều KHÔNG có     : [liệt kê pattern AI thường dùng nhưng không thấy trong examples — ví dụ: "không có 'hãy cùng khám phá', không có câu kết tổng kết dài"]
⑤ Cách câu kết nối  : [mô tả cơ chế dẫn dắt giữa các câu — KHÔNG phải liệt kê cấu trúc mà mô tả logic cảm xúc:
   ví dụ: "Câu 1 throw người xem vào tình huống → Câu 2 là cảm xúc/phản ứng tự nhiên của người xem trước tình huống đó → Câu 3 lật ngược hoặc đào sâu hơn → không có câu nào giải thích lại câu trước"]
⑥ Hành trình cảm xúc: [mô tả cung bậc cảm xúc từ đầu đến cuối script — ví dụ:
   "Mở = bất ngờ/tò mò → Giữa = nhận ra mình đang/đã mắc lỗi này → Đỉnh = khoảnh khắc 'ồ ra là vậy' → Cuối = muốn làm gì đó ngay"]
```

> ⚠️ ⑤ và ⑥ là 2 pattern quan trọng nhất — dùng để viết câu tiếp theo dựa trên cảm xúc câu trước, không phải dựa trên checklist cấu trúc.
> Khi viết body: mỗi câu phải là **phản ứng cảm xúc tự nhiên** với câu trước — không liệt kê thông tin độc lập.

⏱️ Tối đa 60 giây. Nếu < 3 examples → ghi `[Không đủ mẫu để phân tích]`, tiếp tục.
→ `[EXAMPLE ANALYSIS]` là input bắt buộc cho bước viết kịch bản — truyền nguyên vào phase script writing.

---

### Bước 3 — Tóm tắt Raw Input vào Working Memory

→ Xử lý input theo loại file (audio/image/link/doc như Bước 1)
→ **HÀNH ĐỘNG**: Output trực tiếp trong conversation — KHÔNG ghi file, KHÔNG gọi NbLM.
→ **FORMAT**:

```
📄 RAW INPUT SUMMARY
Nguồn: [link gốc hoặc tên file]
Nội dung: [tóm tắt nội dung chính, KHÔNG copy header/footer/ads]
Vấn đề cốt lõi: [1-2 câu]
```

> Dữ liệu này chỉ tồn tại trong phiên trò chuyện hiện tại. Kết thúc phiên → mất. Không tích lũy dung lượng.

---

### Bước 4 — 3 Frameworks vào Working Memory

**5WHY / 4F / 5W1H**: Phân tích nội suy từ input.

> ⚠️ 4F ở đây là framework nội suy nhanh của GEMINI. Workflow Case Study có 4F-analyzer riêng chi tiết hơn ở Phase 1 — không dùng 4F sơ bộ này thay thế.

→ **HÀNH ĐỘNG**: Output trực tiếp trong conversation — KHÔNG gọi NbLM.
→ **FORMAT**:

```
📊 FRAMEWORKS
5WHY: [chuỗi 5 câu hỏi tại sao → nguyên nhân gốc rễ]
4F:   Facts / Feelings / Findings / Future — mỗi mục 1-2 câu
5W1H: Who / What / When / Where / Why / How — mỗi mục 1 câu
```

> Dữ liệu này chỉ tồn tại trong phiên trò chuyện hiện tại. Kết thúc phiên → mất.

---

### Bước 5 — Hỏi VJ góc nhìn (1 lần duy nhất)

> "Bạn có muốn thêm ① quan điểm cá nhân ② trải nghiệm thực tế không? (bỏ qua để tiếp tục)"

⛔ DỪNG, chờ VJ trả lời. KHÔNG tự tiếp tục trước khi VJ phản hồi.
→ VJ trả lời → tích hợp vào context.
→ VJ nói bỏ qua → tiếp tục. KHÔNG hỏi lại.

---

### Bước 6 — Load Workflow (BẮT BUỘC)

Báo cáo Phase 0:
```
✅ PHASE 0 XONG.
📖 Memory: [Session trước: X. Hôm nay: Y.]
📄 Raw Input: [Tóm tắt vấn đề cốt lõi]
🗄️ Vault context: [n file liên quan / không có]
📊 Frameworks: [tóm tắt 1 dòng]
→ Đang load workflow: [tên workflow]...
```

Fetch workflow file bằng [crawler]:

```
# News Viral:
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/TikTok-news-viral-workflow.md

# Case Study:
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/TikTok-case-study-workflow.md
```

**⛔ SAU KHI LOAD WORKFLOW:**
1. Đọc TOÀN BỘ workflow file trước khi làm bất cứ điều gì
2. BỎ QUA Phase 0 của workflow — GEMINI Phase 0 đã thay thế
3. Chạy TỪNG PHASE theo thứ tự (Phase 1 → 2 → ... → N)
4. Khi workflow gọi `[skill-name]` → fetch skill từ vault theo path trong VAULT-STRUCTURE-REF.md
5. Báo cáo kết quả mỗi Phase trước khi chuyển tiếp
6. **CẤM**: Viết script/output trực tiếp bỏ qua phases

---

## QUY TẮC 1 — NGÔN NGỮ
Luôn tiếng Việt. Tên file/folder giữ tiếng Anh. Script output theo DNA kênh trong workflow.

---

## QUY TẮC 2 — WORKFLOW FIRST

| Workflow | Fetch URL |
|---|---|
| News Viral | `…/main/.agent/workflows/TikTok-news-viral-workflow.md` |
| Case Study | `…/main/.agent/workflows/TikTok-case-study-workflow.md` |

Routing: tin tức/news/thời sự → News Viral · case study/hồ sơ/khách hàng → Case Study

---

## QUY TẮC 3 — SEARCH VAULT TRƯỚC KHI TẠO MỚI
Đọc MOC → xác định file liên quan → fetch → enrich. KHÔNG BAO GIỜ bịa Story.

---

## QUY TẮC 4 — ĐỌC VAULT QUA RAW URL (BẮT BUỘC)

```
Base: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/
Tool: [crawler]
```

⏱️ Mỗi fetch: timeout 30 giây. Thất bại → ghi nhận, tiếp tục. KHÔNG retry vô hạn.
⛔ KHÔNG dùng bất kỳ MCP server nào để đọc vault.

---

## QUY TẮC 5 — HUMAN CHECKPOINT TRƯỚC KHI LƯU
Hỏi trước khi: lưu script, tạo note, ghi đè, xoá file.
Format: `✅ Hoàn thành [task]. → Lưu vào [path] không?`
Tự động lưu: session log vào NbLM.

---

## QUY TẮC 6 — GHI OUTPUT (Local)

Output lưu **trên máy VJ** — KHÔNG ghi ngược lên GitHub.

- **Script** → `outputs/scripts/tiktok/<filename>.md` (local)
- **Session log** → NbLM ABF-Working-Memory (tự động)
- VJ chỉ định path khác → giữ nguyên path VJ chỉ định

---

## Thông tin hệ thống
```
Vault:     https://github.com/gracenguyenai-boop/abf-vault (public, branch: main)
Raw Base:  https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/
Access:    [crawler] — không cần token, không cần cài thêm
Workflows: News Viral (ABVV) · Case Study (Khang/Huy/Duke/Tuyết Anh)
NbLM:      ABF-Working-Memory
URL:       https://notebooklm.google.com/notebook/c18e32d5-ff8e-4b2a-9dc1-c6ffb868e591
Sprint:    7 ngày · 34 pieces/sprint
```

## Khi không chắc → HỎI. Không tự đoán. Không tự làm rồi báo cáo sau.
