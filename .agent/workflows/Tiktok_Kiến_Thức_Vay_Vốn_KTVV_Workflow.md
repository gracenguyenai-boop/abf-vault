---
title: "Workflow Kiến Thức Vay Vốn - TikTok Script"
source_file: "Workflow_kien_thuc_vay_von.docx"
source_type: "docx"
converted_at: "2026-04-18"
uid: "wf-ktvv-script-v13"
vj: "Shared"
vj_label: "Kiến thức chung"
tags:
  - source
  - type/docx
  - workflow
  - tiktok
  - script
  - shared
  - kien-thuc-vay-von
---

# Workflow: Kiến Thức Vay Vốn — TikTok Script

> **Path:** `/tiktok-vayvon-script`
> **Version:** v1.3

**Description:** Input: chủ đề vay vốn/ngân hàng. Output: kịch bản TikTok 60-90 giây dạng kiến thức (điểm mù, tip, quy trình, cảnh báo). Dùng cho kênh TikTok tài chính tiếng Việt.

---

## SCOPE

- **Bài toán:** Tự động research, phân tích và viết kịch bản TikTok kiến thức vay vốn — thay thế việc người viết tự đi tìm idea thủ công từ mạng xã hội.
- **Input:** Chủ đề hoặc từ khóa do user cung cấp (ví dụ: "làm sạch hồ sơ trước khi vay", "lãi suất thả nổi", "CIC và điểm tín dụng").
- **Output:** 1 kịch bản TikTok hoàn chỉnh gồm Hook / Bridge / Thân bài / CTA + gợi ý visual + hashtag. Độ dài thân bài 150-300 từ, tổng thời lượng video 60-90 giây.
- **Hoàn thành khi:** Kịch bản có đủ 4 phần, hook kích hoạt ít nhất 1 trigger tâm lý, thân bài có ít nhất 1 con số hoặc ví dụ cụ thể, pass toàn bộ 4C Check.
- **Skills gọi:** `[tiktok-viral-hook, tiktok-body-writer, tiktok-cta-writer, human-voice]`
- **MCP:** Perplexity (Phase 1 — search & research)

---

## DANH SÁCH NỘI DUNG KHÔNG ĐƯỢC PUBLIC

> ⚠️ **Bộ lọc bắt buộc** — áp dụng xuyên suốt tất cả phases. Agent phải kiểm tra danh sách này trước khi viết bất kỳ nội dung nào vào kịch bản. Nếu phát hiện vi phạm ở bất kỳ phase nào → xóa/thay thế ngay, không chờ đến Phase 4.

- **Không đề cập đến chi phí xử lý đáo hạn** — đây là chi phí cho vay lãi không được pháp luật cho phép.
- **Ngoài chi phí tất toán, không được nhắc đến bất kỳ chi phí nào khi xử lý hồ sơ** trên kịch bản.
- **Không được đề cập đến vay hộ hoặc vay ké** — đây là hành vi vi phạm pháp luật.
- **Không đề cập đến nợ xấu nhóm 3 trở lên** — không có giải pháp xử lý, không đưa vào nội dung.
- **Không nói xấu ngân hàng** dưới bất kỳ hình thức nào.
- **Không dùng cụm "mua định giá" hay "nâng định giá"** — chỉ được dùng: *"hỗ trợ khách hàng chọn đơn vị định giá ngoài để sát giá thị trường"*.
- **Không dùng cụm "vẽ nguồn thu"** — chỉ được dùng: *"tối ưu hóa sổ sách cho phù hợp với ngân hàng"*.

---

## PHASE 1: RESEARCH — THU THẬP KIẾN THỨC & INSIGHT

### Mục tiêu
Đến cuối phase này, agent phải có ít nhất 1 insight cốt lõi có thể khai thác thành video, kèm 1 con số hoặc ví dụ thực tế minh họa, và xác định rõ nhóm người xem bị ảnh hưởng trực tiếp.

### Nguồn
- **Perplexity MCP** — search và tổng hợp thông tin từ web theo chủ đề (báo tài chính: CaféF, VnEconomy, Tạp chí Tài chính, website ngân hàng chính thức)
- User input (chủ đề, từ khóa, hoặc angle cụ thể user muốn khai thác)

### 5 loại nội dung cần tìm, theo thứ tự ưu tiên

*(Tham khảo bảng chi tiết trong file gốc trên Lark Docs)*

### Cụm từ search theo loại nội dung
- **Điểm mù:** "[chủ đề] điều ngân hàng không nói" / "sai lầm khi vay [chủ đề]" / "[chủ đề] ít người biết"
- **Tips & Quy trình:** "cách tăng khả năng vay ngân hàng" / "quy trình xét duyệt hồ sơ vay" / "làm sạch hồ sơ tín dụng"
- **Số liệu & Cảnh báo:** "lãi suất vay [loại vay] [tháng/năm]" / "rủi ro vay [chủ đề]"

### Pass khi
- Có ít nhất 1 insight cốt lõi thuộc 1 trong 5 loại trên
- Có ít nhất 1 con số cụ thể, tên ngân hàng cụ thể, hoặc ví dụ thực tế có thể kiểm chứng
- Xác định được nhóm người xem bị ảnh hưởng trực tiếp
- Xác định được hệ quả nếu người xem không biết thông tin này

### Fail thì
- Search không ra insight đủ cụ thể → thử lại với từ khóa hẹp hơn (thêm tên ngân hàng / loại vay / năm hiện tại)
- Sau 3 lần search vẫn không đủ → hỏi user: "Em cần thêm thông tin về [khía cạnh cụ thể], anh/chị có tài liệu hoặc case thực tế nào không?"
- Không được chuyển sang Phase 2 nếu chưa pass

---

## PHASE 2: PHÂN TÍCH — XÁC ĐỊNH ANGLE & ĐỐI TƯỢNG

### Mục tiêu
Đến cuối phase này, agent phải quyết định được: (1) đây là loại nội dung gì, (2) angle khai thác cụ thể, (3) đối tượng người xem được gọi tên rõ ràng — để Phase 3 viết đúng tone và công thức.

### Nguồn
- Output từ Phase 1

### Xử lý
Agent tự phân tích output từ Phase 1 và điền vào idea card — không cần gọi skill.

### Cấu trúc idea card (output của phase này)

```
Loại nội dung : [Điểm mù / Tip / Quy trình / Cảnh báo / So sánh]
Insight cốt lõi: [1 câu mô tả thứ người xem chưa biết]
Con số / ví dụ : [dữ liệu cụ thể hỗ trợ insight]
Angle         : [câu mô tả góc tiếp cận - xem bảng dưới]
Đối tượng     : [nhóm người xem cụ thể]
Hệ quả nếu bỏ qua: [điều xảy ra nếu người xem không biết thông tin này]
```

*(Tham khảo bảng chọn angle theo loại nội dung trong file gốc trên Lark Docs)*

### Pass khi
- Idea card đã điền đủ 6 trường
- Angle được chọn khớp với loại nội dung
- Đối tượng được gọi tên cụ thể (không phải "mọi người" hay "người đi vay" chung chung)

### Fail thì
- Insight quá rộng để chọn 1 angle → thu hẹp lại: chọn 1 khía cạnh cụ thể nhất, lưu phần còn lại vào vault làm idea cho video sau
- Không xác định được đối tượng rõ ràng → quay lại Phase 1, search thêm context

---

## PHASE 3: VIẾT KỊCH BẢN — ÁP DỤNG CÔNG THỨC CONTENT

### Mục tiêu
Đến cuối phase này, agent phải có kịch bản hoàn chỉnh đủ 4 phần: Hook / Bridge / Thân bài / CTA — đúng tone giọng kênh, đúng độ dài video 60-90 giây.

### Nguồn
- Idea card từ Phase 2

### Skill
→ GỌI lần lượt: `[tiktok-viral-hook]` → `[tiktok-body-writer]` → `[tiktok-cta-writer]` → `[human-voice]`

Mỗi skill chạy độc lập, output của skill trước là input của skill sau.

### PHẦN 1 — HOOK (0-5 giây)

→ GỌI: `[tiktok-viral-hook]`

Truyền vào: loại nội dung + angle + đối tượng + insight cốt lõi + con số/ví dụ từ idea card.

Skill xuất 3 biến thể hook. Agent chọn 1 biến thể tốt nhất để chuyển sang phần tiếp theo.

*(Tham khảo bảng định hướng công thức hook theo loại nội dung trong file gốc)*

### PHẦN 2 — BRIDGE (5-10 giây)

Viết trực tiếp, không cần gọi skill. Câu xác nhận rằng video sẽ giải quyết đúng vấn đề người xem vừa thấy ở hook. Ví dụ:

- "Trong video này em sẽ chỉ rõ [vấn đề cụ thể] và [thứ người xem sẽ học được]."
- "Đây là [số] điều mà nhân viên ngân hàng không bao giờ chủ động nói với anh/chị."
- "Em sẽ giải thích đúng [số bước] mà anh/chị cần nắm để [kết quả cụ thể]."

### PHẦN 3 — THÂN BÀI (10-75 giây)

→ GỌI: `[tiktok-body-writer]`

Truyền vào: hook đã chọn + bridge + idea card đầy đủ.

Skill chọn 1 trong 4 cấu trúc phù hợp và viết thân bài:

**Cấu trúc A — Danh sách có số thứ tự (List)**
Dùng khi: Tip thực chiến, quy trình, checklist các bước.

```
"Đây là [số] điều anh/chị cần biết:"
Điểm [N]: [Tiêu đề ngắn]
→ Giải thích cụ thể, 2-4 câu
→ Ví dụ thực tế hoặc con số minh họa
```

**Cấu trúc B — Vấn đề → Nguyên nhân → Giải pháp (PAS)**
Dùng khi: Điểm mù nhận thức, giải thích tại sao, cảnh báo.

```
[Vấn đề] → Tình huống người xem đang gặp hoặc có thể gặp
[Nguyên nhân] → Insight ít người biết - phần này là cốt lõi
[Giải pháp] → Hành động cụ thể, làm được ngay
```

**Cấu trúc C — Trước / Sau (Before / After)**
Dùng khi: So sánh, cách đúng vs cách sai.

```
[Trước] → Cách hầu hết mọi người đang làm (sai hoặc thiếu)
[Sau] → Cách người hiểu rõ làm - cụ thể, áp dụng được ngay
[Kết quả khác biệt] → Con số hoặc hệ quả rõ ràng
```

**Cấu trúc D — Câu chuyện → Bài học (Storytelling)**
Dùng khi: Case study, tình huống thực tế.

```
[Tình huống] → Có anh/chị khách hàng [mô tả hoàn cảnh ngắn]...
[Diễn biến] → Điều đã xảy ra - thường là sai lầm hoặc điều bất ngờ
[Hệ quả] → Kết quả - tốt hoặc xấu tùy angle
[Bài học] → "Từ câu chuyện này, điều anh/chị cần ghi nhớ là..."
```

### PHẦN 4 — CTA (75-90 giây)

→ GỌI: `[tiktok-cta-writer]`

Truyền vào: loại nội dung + insight cốt lõi + thân bài đã viết.

Skill chọn kiểu CTA phù hợp nhất với nội dung — không copy-paste công thức CTA cũ vào video mới:

- **Hành động ngay** (dùng khi tip/quy trình có thể làm được ngay): "Anh/chị làm ngay điều này trước khi quá muộn: [hành động cụ thể]."
- **Kéo tương tác** (dùng khi nội dung chạm vào tình huống cá nhân): "Anh/chị đang ở bước nào rồi? Comment bên dưới để em tư vấn thêm."
- **Tiếp tục xem** (dùng khi mở ra chủ đề liên quan): "Video tiếp theo em sẽ nói về [chủ đề liên quan] — follow để không bỏ lỡ."

### PHẦN 5 — LOẠI BỎ TÍNH AI, TRẢ LẠI GIỌNG NGƯỜI

→ GỌI: `[human-voice]` — Quét toàn bộ script: loại bỏ cụm từ robot ("Hãy cùng khám phá...", ...), kiểm tra nhịp câu có tự nhiên không khi đọc to, kiểm tra transition giữa các section có mượt không.

### Pass khi
- Hook pass checklist `[tiktok-viral-hook]`: ≥1 trigger tâm lý, ≥1 chi tiết cụ thể, có khoảng trống, không giải thích sớm
- Thân bài có ít nhất 1 con số hoặc ví dụ cụ thể có thể kiểm chứng, 150-250 từ
- CTA khớp với nội dung — không phải CTA generic copy-paste
- Sau khi `[human-voice]` chạy xong: đọc to kịch bản nghe tự nhiên, không nghe như văn viết

### Fail thì
- Hook không đủ mạnh → gọi lại `[tiktok-viral-hook]` với biến thể khác, không tự sửa tay
- Thân bài không có con số cụ thể → quay lại Phase 1, search thêm bằng Perplexity
- Vượt quá 300 từ → cắt bớt trước khi đưa vào `[human-voice]`, phần dư làm idea card video tiếp theo
- Sau `[human-voice]` vẫn còn câu nghe gượng → chạy lại `[human-voice]` với đoạn cụ thể đó, không chạy lại toàn bộ

---

## PHASE 4: VERIFY + SHIP

### Mục tiêu
Kiểm tra toàn bộ kịch bản trước khi ship — đảm bảo đúng sự thật, đủ thành phần, phù hợp người xem, và không gây rủi ro khi đăng.

### 4C Check cho workflow này

**Correctness:**
- [ ] Thông tin trong thân bài có thể kiểm chứng (có nguồn rõ ràng hoặc là thông lệ phổ biến trong ngành)
- [ ] Không có con số, tên ngân hàng, hoặc mốc thời gian bịa đặt
- [ ] Nếu không chắc chắn về 1 thông tin → đã dùng ngôn ngữ phỏng chừng có trách nhiệm: "thường dao động", "theo thông lệ", "anh/chị kiểm tra lại với ngân hàng cụ thể"

**Completeness:**
- [ ] Kịch bản có đủ 4 phần: Hook / Bridge / Thân bài / CTA
- [ ] Hook đã pass checklist của skill `[tiktok-viral-hook]` (≥1 trigger, ≥1 chi tiết cụ thể, có khoảng trống, không giải thích sớm)
- [ ] File output có đủ: kịch bản + gợi ý visual + hashtag

**Context-fit:**
- [ ] Giọng văn đúng chuẩn: xưng em, gọi anh/chị, câu ≤20 từ, viết như nói
- [ ] Độ phức tạp phù hợp người không chuyên ngành — không có thuật ngữ chưa được giải thích
- [ ] Chỉ có 1 ý chính trong toàn bộ video

**Consequence:**
- [ ] Nếu thông tin sai, hậu quả với người xem là gì? (nếu nghiêm trọng → phải kiểm tra lại nguồn trước khi ship)
- [ ] Nội dung có đang tư vấn tài chính cá nhân không? (nếu có → thêm disclaimer: "đây là thông tin tham khảo, anh/chị cần xác nhận thêm với ngân hàng")
- [ ] Nội dung có đang so sánh trực tiếp 2 ngân hàng theo hướng bất lợi cho 1 bên không? (nếu có → cân nhắc lại angle)

### Gate rule
- **ALL pass → SHIP**
- **1+ fail → fix → verify lại TẤT CẢ** (không chỉ phần bị fail)

---

## OUTPUT

- **File:** `script_[chủ-đề-ngắn]_[YYYYMMDD].md` — Ví dụ: `script_lam-sach-ho-so_20260420.md`
- **Lưu:** `/vault/04-Scripts/tiktok/`
- **Feed vault:** Có — sau khi ship, tách insight cốt lõi (1-3 câu) vào `01-Atomic/` dưới tag `#insight/vayvon` để dùng lại cho video sau

---

## EVOLUTION NOTES

**Lỗi thường gặp khi chạy workflow này:**

- **Hook quá chung chung:** Không có tên ngân hàng / con số / mốc thời gian cụ thể → hook đọc xong không gây được phản xạ dừng lại. *Cách tránh: luôn ép thêm ít nhất 1 chi tiết cụ thể vào hook trước khi pass Phase 3.*
- **Thân bài nhồi quá nhiều ý:** Cố đưa 3-4 tip vào 1 video → người xem không nhớ được gì. *Cách tránh: chọn 1 nhánh sâu nhất, lưu phần còn lại thành idea card riêng.*
- **Thông tin không kiểm chứng được:** Dùng con số hoặc quy trình ngân hàng nghe có vẻ đúng nhưng không có nguồn → rủi ro khi đăng. *Cách tránh: nếu không có nguồn rõ ràng, thay bằng ngôn ngữ phỏng chừng hoặc quay lại Phase 1 search thêm.*
- **Giọng văn lẫn lộn formal/informal:** Câu đầu viết như nói, câu sau lại như báo cáo. *Cách tránh: đọc to toàn bộ kịch bản sau khi viết xong — chỗ nào đọc lên nghe gượng là chỗ cần sửa.*
- **CTA không liên quan đến nội dung:** CTA copy-paste từ video khác. *Cách tránh: CTA phải là bước tiếp theo tự nhiên sau thứ người xem vừa học được.*
- **Kịch bản đọc lên nghe như AI viết:** Câu cân đối quá, chuyển ý quá mượt, không có chỗ bỏ lửng tự nhiên. *Cách tránh: `[human-voice]` là bước bắt buộc — không skip dù thân bài đọc có vẻ ổn.*

**Changelog:**
- v1.0: Khởi tạo workflow, tích hợp skill `[tiktok-viral-hook]` vào Phase 3
- v1.1: Bổ sung 5 loại nội dung ưu tiên vào Phase 1, thêm cụm từ search cụ thể theo từng loại
- v1.2: Tách Phase 2 thành phase riêng với idea card chuẩn hóa — trước đó Phase 1 và 2 gộp chung, gây ra angle không rõ trước khi viết
- v1.3: Phase 1 bỏ skill trung gian, dùng trực tiếp Perplexity MCP. Phase 3 tách thành 5 bước với 4 skill độc lập: `[tiktok-viral-hook]` → `[tiktok-body-writer]` → `[tiktok-cta-writer]` → `[human-voice]`. Thêm skill `[human-voice]` để loại bỏ tính AI và trả lại giọng nói tự nhiên
