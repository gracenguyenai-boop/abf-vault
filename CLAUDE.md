# CLAUDE.md — Luật Tối Cao

> Đọc file này TRƯỚC KHI làm bất cứ điều gì. Không có ngoại lệ.
> Paths và routing: fetch `VAULT-STRUCTURE-REF.md` từ vault (xem Bước 0).

---

## ⚙️ HỆ THỐNG — Vault kết nối qua GitHub Raw URL

```
Vault:    https://github.com/gracenguyenai-boop/abf-vault (public)
Base URL: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main
Tool:     WebFetch — dùng để đọc raw file từ vault
```

**Cách đọc bất kỳ file nào trong vault:**
```
WebFetch: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/<path-tới-file>
```

Ví dụ:
```
MEMORY/decisions.md
→ https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/decisions.md

.agent/workflows/TikTok-case-study-workflow.md
→ https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/TikTok-case-study-workflow.md
```

> ⛔ KHÔNG dùng `run_command`, `curl`, `mcp_obsidian_*`, hay bất kỳ MCP server nào khác.
> ✅ CHỈ dùng WebFetch để fetch raw URL. Đơn giản, không cần setup.

---

## ⚡ BOOTSTRAP — LỆNH ĐẦU TIÊN, TUYỆT ĐỐI

### ⛔ CẤM TUYỆT ĐỐI trước khi chạy Phase 0:
- CẤM đọc bất kỳ file nào ngoài CLAUDE.md
- CẤM crawl web ngoài vault
- CẤM hỏi VJ thêm thông tin

### Khi nhận BẤT KỲ prompt nào từ VJ:

⛔ DỪNG. Gọi **AskUserQuestion 2 lần liền mạch** — popup 2 hiện ngay sau popup 1, không có bước nào ở giữa. KHÔNG tự đoán.

> **Shortcut rule:** Nếu prompt đã chứa đủ thông tin (ví dụ: *"thuỷ case study đóng vai"*) → extract field đã có, bỏ qua các popup tương ứng, chạy PHASE 0 luôn.

---

**POPUP 1 — Kênh + Workflow (submit lần 1):**

```
questions: [
  {
    question: "🎬 Chọn kênh:",
    header: "Kênh",
    options: [
      { label: "An Bình Vay Vốn", description: "VJ An Bình" },
      { label: "Khang Vay Hay",   description: "VJ Khang"   },
      { label: "Thuỷ Vay Vốn",    description: "VJ Thuỷ"    },
      { label: "Đạt Vay Đơn Giản",description: "VJ Đạt"     }
    ]
  },
  {
    question: "Chọn workflow:",
    header: "Workflow",
    options: [
      { label: "News Viral",        description: "Tin tức / thời sự"     },
      { label: "Case Study",        description: "Hồ sơ vay vốn thực tế" },
      { label: "Kiến Thức Vay Vốn", description: "Chỉ dùng cho An Bình"  },
      { label: "An Bình Là Ai",     description: "Chỉ dùng cho An Bình"  }
    ]
  }
]
```

→ Nhận kết quả VJ + Workflow. **Ngay lập tức** gọi POPUP 2 — không in text, không xử lý gì ở giữa.

---

**POPUP 2 — Nội dung + Format đã lọc (submit lần 2):**

Câu hỏi nội dung theo workflow:
- News Viral        → `"Nội dung news cần phân tích — dán link hoặc mô tả:"`
- Case Study        → `"Nội dung case cần phân tích — dán file hồ sơ / ghi chú 4F:"`
- Kiến Thức Vay Vốn → `"Chủ đề cần phân tích:"`
- An Bình Là Ai     → `"Nội dung cần phân tích:"`

Format options — **chỉ đưa vào đúng format hợp lệ theo bảng:**

| VJ | News Viral | Case Study | KTVV / ABLA |
|---|---|---|---|
| An Bình | talking-head · tips-nhanh | talking-head · tips-nhanh | talking-head · tips-nhanh |
| Khang | talking-head · tips-nhanh | **→ xem POPUP 2.5** | — |
| Thuỷ | talking-head · tips-nhanh | talking-head · tips-nhanh · dong-vai | — |
| Đạt | talking-head · tips-nhanh | **→ xem POPUP 2.5** | — |

```
questions: [
  {
    question: "[câu hỏi nội dung theo workflow]",
    header: "Nội dung",
    options: [
      { label: "→ Dán nội dung vào ô bên dưới", description: "Link hoặc mô tả" },
      { label: "Chưa có — bỏ qua",              description: "Tiếp tục không có nội dung" }
    ]
  },
  {
    question: "Chọn format quay:",
    header: "Format",
    options: [chỉ format hợp lệ của VJ × Workflow vừa chọn — tối đa 4 options]
  }
]
```

> ⚠️ **Ngoại lệ — Khang × Case Study và Đạt × Case Study:** Có 5 format, vượt giới hạn 4 options/popup.
> → Trong câu hỏi Format của POPUP 2, **thay thế toàn bộ format list bằng 2 nhóm** tương ứng với VJ:
>
> **Khang × Case Study:**
> ```
> options: [
>   { label: "Nhóm cơ bản",    description: "talking-head · tips-nhanh" },
>   { label: "Nhóm thực địa",  description: "giai-quyet-thuc-dia · selfie · tu-van-hoi-thoai" }
> ]
> ```
>
> **Đạt × Case Study:**
> ```
> options: [
>   { label: "Nhóm cơ bản",      description: "talking-head · tips-nhanh" },
>   { label: "Nhóm xe & hồ sơ",  description: "trong-xe-o-to · nghe-dien-thoai · cam-giay-to" }
> ]
> ```
>
> → Sau khi user chọn nhóm → **gọi ngay POPUP 2.5** (không in text, không xử lý giữa).

---

**POPUP 2.5 — Chỉ dùng cho Khang × Case Study và Đạt × Case Study (submit lần 3):**

```
questions: [
  {
    question: "Chọn format cụ thể:",
    header: "Format",
    options: [
      // Khang — Nhóm cơ bản:
      { label: "talking-head", description: "Quay mặt trực tiếp" },
      { label: "tips-nhanh",   description: "Tips ngắn gọn" }

      // Khang — Nhóm thực địa:
      { label: "giai-quyet-thuc-dia", description: "Giải quyết tại thực địa" },
      { label: "selfie",              description: "Quay selfie" },
      { label: "tu-van-hoi-thoai",    description: "Tư vấn dạng hội thoại" }

      // Đạt — Nhóm cơ bản:
      { label: "talking-head", description: "Quay mặt trực tiếp" },
      { label: "tips-nhanh",   description: "Tips ngắn gọn" }

      // Đạt — Nhóm xe & hồ sơ:
      { label: "trong-xe-o-to",    description: "Quay trong xe ô tô" },
      { label: "nghe-dien-thoai",  description: "Nghe điện thoại" },
      { label: "cam-giay-to",      description: "Cầm giấy tờ" }
    ]
  }
]
```

⛔ Sau khi nhận đủ → lưu working memory → chạy PHASE 0 ngay.

---

> 📋 **INPUT GUIDE — Chỉ áp dụng khi Workflow = Case Study + VJ chọn dán nội dung**
>
> **Flow:**
> 1. Agent hiển thị note bên dưới TRƯỚC KHI nhận nội dung
> 2. VJ dán dữ liệu tự do (text, bảng, ghi chú đều được)
> 3. Agent extract → hiển thị bảng INPUT CHECK → hỏi bổ sung phần còn thiếu
> 4. Tất cả 🔴 ✅ → chạy PHASE 0

**Note agent hiển thị cho VJ (bước 1):**

```
📋 CASE STUDY — THÔNG TIN CẦN CÓ
Dán dữ liệu tự do bên dưới. Mình sẽ tự extract và hỏi phần còn thiếu.

🔴 BẮT BUỘC

[PHÁP LÝ]
  • Tình trạng sổ: phôi mới/cũ, loại sổ, có tranh chấp không
  • Đặc điểm pháp lý đặc thù (mộ trên đất, đất nông nghiệp, đất đang thế chấp...)

[TÀI SẢN]
  • Loại đất / tài sản (ONT, đất lúa, căn hộ, nhà ở...)
  • Diện tích + địa chỉ khu vực (tỉnh/huyện/xã)
  • Đặc điểm thực địa ảnh hưởng định giá

[CIC]
  • Kết quả CIC: sạch / có vấn đề
  • Nếu có vấn đề: nhóm mấy, bao nhiêu tháng, pattern trễ thế nào

[NHU CẦU VAY & ĐỊNH GIÁ]
  • KH muốn vay bao nhiêu
  • Định giá sơ bộ (VAAE hoặc ước tính): bao nhiêu tỷ
  • LTV dự kiến (%)

[NGUỒN THU]
  • Nghề nghiệp / ngành nghề kinh doanh
  • Thu nhập tháng (tổng)
  • Tỷ lệ tiền mặt / chuyển khoản (VD: 50/50)
  • Có đăng ký kinh doanh không

[GIẢI PHÁP & KẾT QUẢ]
  • Giải pháp đã áp dụng — phần ĐƯỢC PHÉP truyền thông
  • Tên bank giải ngân (hoặc "ngân hàng ABC" nếu cần ẩn)
  • Mục đích vay (tiêu dùng / xây sửa / kinh doanh...)
  • Số tiền giải ngân thực tế
  • Lãi suất + cố định bao nhiêu tháng
  • Kỳ hạn vay (tháng)
  • Ân hạn gốc (tháng) ← hay bị bỏ sót

🟡 NÊN CÓ

[BỐI CẢNH & CẢM XÚC]
  • Tháng/năm nộp hồ sơ · ngày giải ngân
  • Số nơi đã bị từ chối + lý do từ chối cụ thể
  • Lý do KH cần vay (mục tiêu kinh doanh, áp lực tài chính, thời điểm cần tiền)
  • Tâm lý / cảm xúc KH lúc tìm đến

[4F NHẬN ĐỊNH HỒ SƠ] (nếu đã có sẵn)
  • Facts: số liệu khách quan
  • Feelings: tâm lý KH + cảm nhận cán bộ xử lý
  • Findings: điểm mạnh / yếu / vướng mắc
  • Future: hành động & giải pháp dự kiến

[CHI PHÍ & ĐIỀU KIỆN]
  • Chi phí phát sinh (công chứng, bảo hiểm, phí dịch vụ...)
  • Điều kiện hồ sơ thành công (ngân hàng yêu cầu gì thêm)

🚫 KHÔNG ĐƯA VÀO:
  • Tên thật KH, số CCCD, số điện thoại
  • Giải pháp KHÔNG được phép truyền thông (che mộ, tác động cán bộ, phí dịch vụ...)
  • Tên cán bộ ngân hàng cụ thể
```

**Bảng INPUT CHECK agent hiển thị sau khi extract (bước 3):**

```
📊 INPUT CHECK
──────────────────────────────────────────────────
🔴 BẮT BUỘC           | Trạng thái | Ghi chú
──────────────────────────────────────────────────
Pháp lý / sổ          | ✅ / ❌    |
Tài sản thực địa      | ✅ / ❌    |
CIC                   | ✅ / ❌    |
Nhu cầu vay + định giá| ✅ / ❌    |
Nguồn thu             | ✅ / ⚠️    | VD: thiếu tỷ lệ TM/CK
Giải pháp (public)    | ✅ / ❌    |
Kết quả (5 yếu tố)    | ✅ / ⚠️    | VD: thiếu ân hạn gốc
──────────────────────────────────────────────────
🟡 NÊN CÓ            | Trạng thái
──────────────────────────────────────────────────
Thời điểm vay/g.ngân  | ✅ / ❌
Nơi bị từ chối        | ✅ / ❌
Lý do vay / áp lực    | ✅ / ❌
Tâm lý KH             | ✅ / ❌
4F (nếu có sẵn)       | ✅ / ❌
Chi phí + điều kiện   | ✅ / ❌
```

- 🔴 có ❌ → hỏi từng trường theo thứ tự từ trên xuống, không hỏi tất cả cùng lúc
- 🔴 có ⚠️ → hỏi bổ sung chi tiết còn thiếu của trường đó
- 🟡 có ❌ → hỏi gộp 1 lần: *"Còn thiếu [X, Y, Z] — bổ sung được không? Nếu chưa có thì vẫn chạy được, story arc sẽ bớt chiều sâu."*
- Tất cả 🔴 ✅ → tóm tắt input đã nhận và chạy PHASE 0

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
**⚠️ PHASE 0 LÀ CỦA CLAUDE — khi load workflow, BỎ QUA Phase 0 của workflow, bắt đầu từ Phase 1.**

**⛔ QUY TẮC CHẠY PHASE 0 — ĐỌC TRƯỚC KHI BẮT ĐẦU:**
- Chạy **LIÊN TỤC** từ Bước 0 → Bước 6. KHÔNG dừng giữa chừng để hỏi VJ, KHÔNG chờ xác nhận.
- Chỉ có **1 điểm dừng hợp lệ duy nhất**: Bước 5 — chờ VJ trả lời rồi tiếp tục ngay Bước 6.
- **KHÔNG được bỏ qua bất kỳ bước nào**, kể cả khi bước đó khó thực thi.
- Bước 2.5 là **BẮT BUỘC** — nếu bỏ qua, toàn bộ Phase 0 coi như chưa hoàn thành.
- Sau mỗi bước: in output ngắn xác nhận hoàn thành, rồi chạy bước tiếp ngay.

**⏱️ TIMEOUT: Mỗi bước tối đa 30 giây.**
Bước nào quá thời gian → ghi nhận, bỏ qua, sang bước tiếp. KHÔNG retry, KHÔNG loop.

---

### Bước 0 — Đọc VAULT-STRUCTURE-REF + Memory từ Vault

Fetch **song song cùng lúc** 5 URLs sau bằng WebFetch:

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

VJ gửi files + links + text → Agent KHÔNG chỉ ACK, phải:
1. **Nhận diện file type:** Link / Audio / Image / Text / Doc
2. **Đọc + xử lý toàn bộ nội dung:**
   - Link → WebFetch đọc toàn bài
   - Audio → yêu cầu VJ dán transcript
   - Image → đọc và mô tả nội dung (Claude hỗ trợ multimodal)
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

Từ MOC, xác định 1–2 file atomic notes liên quan nhất → fetch thêm bằng WebFetch.
⏱️ Timeout 30 giây → ghi nhận những gì tìm được, tiếp tục.
→ Output: `[Kiến thức vault liên quan]`

---

### Bước 2.5 — Load kịch bản mẫu theo VJ + format

**Cấu trúc folder thực tế:**
```
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

**Mapping VJ → folder:**

| VJ chọn | Folder |
|---|---|
| An Bình Vay Vốn | `VJ-AnBinh` |
| Khang Vay Hay | `VJ-Khang` |
| Thuỷ Vay Vốn | `VJ-Thuy` |
| Đạt Vay Đơn Giản | `VJ-Dat` |

**Path cuối cùng:** `VJ/[VJ-folder]/scripts/[format-folder]/`

→ **Fetch strategy file của VJ trước** — đọc bắt buộc, lưu nhãn `[CHANNEL STRATEGY]`:

| VJ | Path strategy file |
|---|---|
| An Bình | `VJ/VJ-AnBinh/VJ-01-Atomic/strategy/2026-05-23-dinh-huong-kenh-vay-von-an-binh.md` |
| Khang | `VJ/VJ-Khang/VJ-01-Atomic/strategy/2026-05-24-chan-dung-kenh-khang-bank.md` |
| Thuỷ | `VJ/VJ-Thuy/VJ-01-Atomic/strategy/2026-05-24-chan-dung-kenh-thuy-bank.md` |
| Đạt | `VJ/VJ-Dat/VJ-01-Atomic/strategy/2026-05-23-dinh-huong-kenh-dat-lam-tai-chinh.md` |

`[CHANNEL STRATEGY]` là nguồn định hướng kênh — đọc trước tất cả, dùng làm nền tảng cho toàn bộ quá trình viết.

→ **Lấy danh sách file bằng GitHub Contents API** (bắt buộc trước khi fetch bất kỳ script nào):
```
GET https://api.github.com/repos/gracenguyenai-boop/abf-vault/contents/VJ/[VJ-folder]/scripts/[format-folder]
```
→ API trả về JSON array chứa `name` của từng file → dùng danh sách này để fetch raw URL từng file.
⛔ KHÔNG tự đoán tên file — phải lấy từ API trước.

→ Từ danh sách trả về: fetch file `_RULE-*` trước — đọc bắt buộc, lưu nhãn `[FORMAT RULE]`.
→ Fetch các file `.md` còn lại (bỏ qua `_RULE-*`) → đọc frontmatter, lọc theo field `workflow-tags`.
→ Chỉ giữ file có `workflow-tags` chứa giá trị khớp với workflow đang chạy → lưu nhãn `[EXAMPLE SCRIPTS]`.
→ Output: `📚 Đã load [CHANNEL STRATEGY] + [n] kịch bản mẫu + 1 _RULE — VJ: [X], format: [Y], workflow: [Z].`

**Bảng mapping workflow → giá trị workflow-tags:**

| Workflow chọn | Giá trị cần có trong `workflow-tags` |
|---|---|
| News Viral | `news` |
| Case Study | `case-study` |
| Kiến Thức Vay Vốn | `ktvv` |
| An Bình Là Ai | `abla` |

**Quy tắc lọc:**
- File có `workflow-tags` chứa giá trị khớp → đưa vào `[EXAMPLE SCRIPTS]`
- File không có `workflow-tags` hoặc không khớp → bỏ qua
- Nếu sau khi lọc còn < 3 file → bỏ filter, load toàn bộ (không đủ mẫu)
- File `_RULE-*` → không lọc, load bắt buộc

⏱️ Timeout 30 giây tổng. File nào fetch thất bại → bỏ qua, tiếp tục.
⛔ Folder trống hoặc không tồn tại → báo VJ thêm scripts mẫu, tiếp tục Phase 0 không có examples.

---

### Bước 2.6 — Phân tích examples (Pattern Extraction)

Chạy ngay sau Bước 2.5. Agent tự phân tích `[EXAMPLE SCRIPTS]` đã load — không cần gọi skill.

Đọc toàn bộ `[EXAMPLE SCRIPTS]` và extract 6 pattern, output vào working memory nhãn `[EXAMPLE ANALYSIS]`:

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
→ **HÀNH ĐỘNG**: Output trực tiếp trong conversation — KHÔNG ghi file.
→ **FORMAT**:

```
📄 RAW INPUT SUMMARY
Nguồn: [link gốc hoặc tên file]
Nội dung: [tóm tắt nội dung chính, KHÔNG copy header/footer/ads]
Vấn đề cốt lõi: [1-2 câu]
```

> Dữ liệu này chỉ tồn tại trong phiên trò chuyện hiện tại. Kết thúc phiên → mất.

---

### Bước 4 — 3 Frameworks vào Working Memory

**5WHY / 4F / 5W1H**: Phân tích làm sạch input đầu vào.

> ⚠️ 4F ở đây là framework nội suy nhanh. Workflow Case Study có 4F-analyzer riêng chi tiết hơn ở Phase 1 — không dùng 4F sơ bộ này thay thế.

→ **HÀNH ĐỘNG**: Output trực tiếp trong conversation.
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

**⛔ PRE-FLIGHT CHECK — Chạy trước khi load workflow:**

Xác nhận đã hoàn thành đủ 5 bước trước:

```
✅ PHASE 0 CHECKLIST
─────────────────────────────────────────────
Bước 0 — Memory loaded        : ✅ / ⚠️ [ghi nhận nếu fail]
Bước 1 — Raw input processed  : ✅ / ⚠️
Bước 2 — Vault search done    : ✅ / ⚠️
Bước 2.5 — [CHANNEL STRATEGY] : ✅ / ❌ CHƯA CHẠY → DỪNG, chạy lại ngay
          — [FORMAT RULE]      : ✅ / ❌ CHƯA CHẠY → DỪNG, chạy lại ngay
          — [EXAMPLE SCRIPTS]  : ✅ ([n] scripts) / ❌ CHƯA CHẠY → DỪNG
Bước 2.6 — [EXAMPLE ANALYSIS] : ✅ / ❌ CHƯA CHẠY → DỪNG, chạy lại ngay
Bước 3 — RAW INPUT SUMMARY    : ✅ / ⚠️
Bước 4 — Frameworks done      : ✅ / ⚠️
Bước 5 — VJ input collected   : ✅ / ⚠️ bỏ qua
─────────────────────────────────────────────
```

> ⛔ Nếu Bước 2.5 hoặc 2.6 có ❌ → KHÔNG load workflow. Chạy lại bước đó ngay, xong mới tiếp tục.

Báo cáo Phase 0:
```
✅ PHASE 0 XONG.
📖 Memory: [Session trước: X. Hôm nay: Y.]
📄 Raw Input: [Tóm tắt vấn đề cốt lõi]
🗄️ Vault context: [n file liên quan / không có]
📚 Scripts: [n] mẫu loaded — VJ: [X], format: [Y]
📊 Frameworks: [tóm tắt 1 dòng]
→ Đang load workflow: [tên workflow]...
```

Fetch workflow file bằng WebFetch:

```
# News Viral:
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/TikTok-news-viral-workflow.md

# Case Study:
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/TikTok-case-study-workflow.md

# Kiến Thức Vay Vốn:
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/Tiktok_Kiến_Thức_Vay_Vốn_KTVV_Workflow.md

# An Bình Là Ai:
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/workflows/Tiktok_An_Binh_La_Ai_ABLA_Workflow.md
```

**⛔ SAU KHI LOAD WORKFLOW:**
1. Đọc TOÀN BỘ workflow file trước khi làm bất cứ điều gì
2. BỎ QUA Phase 0 của workflow — CLAUDE Phase 0 đã thay thế
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
| Kiến Thức Vay Vốn | `…/main/.agent/workflows/Tiktok_Kiến_Thức_Vay_Vốn_KTVV_Workflow.md` |
| An Bình Là Ai | `…/main/.agent/workflows/Tiktok_An_Binh_La_Ai_ABLA_Workflow.md` |

Routing: tin tức/news/thời sự → News Viral · case study/hồ sơ/khách hàng → Case Study · kiến thức tài chính → KTVV · giới thiệu VJ → ABLA

---

## QUY TẮC 3 — SEARCH VAULT TRƯỚC KHI TẠO MỚI
Đọc MOC → xác định file liên quan → fetch → enrich. KHÔNG BAO GIỜ bịa Story.

---

## QUY TẮC 4 — ĐỌC VAULT QUA RAW URL (BẮT BUỘC)

```
Base: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/
Tool: WebFetch
```

⏱️ Mỗi fetch: timeout 30 giây. Thất bại → ghi nhận, tiếp tục. KHÔNG retry vô hạn.
⛔ KHÔNG dùng bất kỳ MCP server nào để đọc vault.

---

## QUY TẮC 5 — HUMAN CHECKPOINT TRƯỚC KHI LƯU
Hỏi trước khi: lưu script, tạo note, ghi đè, xoá file.
Format: `✅ Hoàn thành [task]. → Lưu vào [path] không?`

---

## QUY TẮC 6 — GHI OUTPUT (Local)

Output lưu **trên máy VJ** — KHÔNG ghi ngược lên GitHub.

- **Script** → `outputs/scripts/tiktok/<filename>.md` (local)
- VJ chỉ định path khác → giữ nguyên path VJ chỉ định

---

## Thông tin hệ thống
```
Vault:     https://github.com/gracenguyenai-boop/abf-vault (public, branch: main)
Raw Base:  https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/
Access:    WebFetch — không cần token, không cần cài thêm
Workflows: News Viral · Case Study · Kiến Thức Vay Vốn · An Bình Là Ai
Sprint:    7 ngày · 34 pieces/sprint
```

## Khi không chắc → HỎI. Không tự đoán. Không tự làm rồi báo cáo sau.
