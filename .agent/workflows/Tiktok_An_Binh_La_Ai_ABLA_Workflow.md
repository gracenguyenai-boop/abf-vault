---
title: "Workflow An Bình Là Ai - TikTok Script"
source_file: "Workflow_An_binh_la_ai.docx"
source_type: "docx"
converted_at: "2026-04-18"
uid: "wf-abla-script-v14"
vj: "VJ-AnBinh"
vj_label: "An Bình Vay Vốn"
tags:
  - source
  - type/docx
  - workflow
  - tiktok
  - script
  - vj/vj-anbinh
---

# Workflow: An Bình Là Ai — TikTok Script

> **Path:** `/abla-script-workflow`
> **Version:** v1.4

**Description:** Workflow viết kịch bản TikTok "An Bình là ai" cho An Bình Finance. Input: chủ đề hoặc yêu cầu từ user. Output: 1 script 120-200 từ, sẵn sàng quay, đúng giọng nói TikTok tài chính, target 20k+ views.

---

## SCOPE

- **Bài toán:** Viết kịch bản TikTok giới thiệu An Bình Finance theo hướng storytelling — không phải quảng cáo liệt kê tính năng
- **Input:** Yêu cầu từ user — có thể chỉ là "viết kịch bản mới" hoặc chủ đề cụ thể (vd: "về ân hạn gốc", "dùng case anh Hải")
- **Output:** 1 script hoàn chỉnh, 120-200 từ, định dạng văn nói tự nhiên 100% tính người, kèm ghi chú `[Công thức: X] [Từ: Y] [Nguyên liệu: Z]`
- **Hoàn thành khi:** Script pass toàn bộ 4C Check ở Phase 3, đọc to lên nghe như người thật đang nói chuyện — không có dấu hiệu AI viết
- **Skills gọi:** `[15-content-formulas, viral-pattern-analysis, human-voice-filter]`

---

## PHASE 1: XÁC ĐỊNH IDEA + CHỌN NGUYÊN LIỆU

### Mục tiêu
Đến cuối phase này, agent và user đã thống nhất được **1 idea cụ thể** sẽ viết. Không gọi skill ở phase này — chỉ hỏi user và đề xuất dựa trên 3 kho nguyên liệu bên dưới.

### Nguồn
- Profile An Bình Finance (AnBinhFinance_Profile.docx)
- 3 kho nguyên liệu bên dưới (Kho A, B, C)
- User input

### Skill
→ Không gọi skill ở phase này. Agent tự xử lý dựa trên kho nguyên liệu.

### Quy trình hỏi + đề xuất

**Bước 1.1 — Hỏi user:**

> "Anh/chị đã có idea hoặc chủ đề muốn viết chưa?"

**Bước 1.2 — Nếu user đã có idea:**
→ Xác nhận idea đó thuộc Kho nào (A/B/C), xác định nhóm khách hàng nhắm tới, chuyển sang Phase 2.

**Bước 1.3 — Nếu user chưa có idea:**
→ Đọc profile + 3 kho nguyên liệu, tự chọn ra 3 idea chưa từng làm (hoặc ít được khai thác), trình bày theo format:

```
Mình đề xuất 3 idea anh/chị có thể chọn:

① [Tên idea ngắn gọn]
   Góc: [điểm mù / case study / tip]
   Hook mẫu: "[câu mở đầu dự kiến]"
   Nhắm tới: [nhóm khách hàng cụ thể]

② [Tên idea ngắn gọn]
   Góc: ...
   Hook mẫu: "..."
   Nhắm tới: ...

③ [Tên idea ngắn gọn]
   Góc: ...
   Hook mẫu: "..."
   Nhắm tới: ...

Anh/chị chọn idea nào, hoặc muốn điều chỉnh gì không?
```

---

### Kho nguyên liệu để đề xuất idea

### KHO A — CASE STUDY

**Nguồn:** Vault/Tri thức từ sale

*Social proof — "người khác tệ hơn mình còn được, mình sao không?"*

*(Tham khảo bảng Case Study trong Vault)*

---

### KHO B — ĐIỂM MÙ NHẬN THỨC

*Educate, build trust — người xem có "à há moment", học được gì đó dù không liên hệ ngay*

**Nguồn:** Vault/Kiến thức vay vốn

- **B1 — Lãi suất & chi phí ẩn:** Lãi trên hợp đồng ≠ tổng chi phí thực. Nghe lãi thấp hơn 1-2% vội chuyển bank → có thể lỗ hơn sau phí tất toán trước hạn (5-8% tổng dư nợ). 45 triệu/tháng lãng phí = 540 triệu/năm
- **B2 — Định giá tài sản:** Ngân hàng định giá thấp hơn thị trường. Gộp thửa đất trước khi định giá → tăng hạn mức đáng kể. Cùng 1 tài sản: bank này 8 tỷ, bank kia 11 tỷ — bình thường
- **B3 — Ân hạn nợ gốc:** 90% người vay không biết hỏi câu này. Mặc định 6-12 tháng, đàm phán được lên 24-36 tháng = giải phóng hàng tỷ thanh khoản giai đoạn đầu
- **B4 — Bị từ chối:** Việt Nam có 31 ngân hàng. Bị từ chối 3 nơi = mới thử 10%. Mỗi bank có "khẩu vị" riêng — bị từ chối ≠ không vay được
- **B5 — Vay lớn >20 tỷ:** Vay nhỏ cán bộ tranh nhau nhận, vay lớn không ai dám nhận → vì vượt thẩm quyền chi nhánh. Khoản >30-50 tỷ phải trình đúng cấp hội sở
- **B6 — Hồ sơ & quy trình:** Ngân hàng không thiếu tiền — thiếu hồ sơ được trình đúng cách. Cùng 1 định giá: bank này duyệt 7 tỷ, bank kia 10 tỷ
- **B7 — Chuyển bank & cơ cấu nợ:** Chuyển bank phải tính tổng chi phí, không chỉ so lãi. Cơ cấu đúng lúc có thể tăng vốn thêm 20-30%

---

### KHO C — TIPS & QUY TRÌNH

*Hữu ích ngay — người xem lưu lại để dùng sau*

**Nguồn:** Vault/Kiến thức vay vốn

- **C1 — Checklist trước khi đi vay:** Kiểm tra CIC trước / gộp thửa nếu có thể / chuẩn bị 2-3 nguồn thu chứng minh được / hỏi ân hạn gốc TRƯỚC khi ký / so sánh ≥3 ngân hàng
- **C2 — Câu hỏi bắt buộc hỏi ngân hàng trước khi ký:** "Ân hạn nợ gốc bao nhiêu tháng?" / "Phí tất toán trước hạn bao nhiêu %?" / "Lãi suất sau ưu đãi năm 2, 3 là bao nhiêu?" / "Tôi đàm phán được điều khoản nào?"
- **C3 — Dấu hiệu hồ sơ yếu cần làm sạch:** Nợ quá hạn dù 1-2 tháng → bị coi là nợ xấu / Dòng tiền tài khoản không đều → khó chứng minh thu nhập / Tài sản chưa kiểm tra pháp lý / Mục đích vay và dòng tiền thực tế không khớp
- **C4 — Quy trình ngân hàng xử lý hồ sơ:** (1) Tiếp nhận & thẩm định sơ bộ → (2) Định giá tài sản → (3) Thẩm định thu nhập/dòng tiền → (4) Trình duyệt → (5) Ký & giải ngân. *Điểm nghẽn hay gặp nhất: bước 2 và bước 3*
- **C5 — An Bình làm được gì cán bộ ngân hàng không làm:** Đại diện cho khách chứ không cho bank / Biết khẩu vị 20+ ngân hàng / Đưa hồ sơ vào 5-7 bank cùng lúc / Quan hệ trực tiếp giám đốc chi nhánh lớn

### Pass khi
- User đã chọn hoặc xác nhận 1 idea cụ thể
- Đã xác định được nhóm khách hàng nhắm tới
- Idea chưa được dùng trong video gần nhất (không lặp lại)

### Fail thì
- User chọn idea quá chung chung → hỏi thêm: "Anh/chị muốn nhắm vào khách đang bị từ chối, đang trả lãi cao, hay chuẩn bị vay lần đầu?"
- User muốn thay đổi 1 trong 3 idea đề xuất → đề xuất lại idea mới, không cần đề xuất lại cả 3

---

## PHASE 2: VIẾT SCRIPT + LỌC GIỌNG NGƯỜI

### Mục tiêu
Đến cuối phase này, agent phải có 1 script hoàn chỉnh đã qua **2 lớp xử lý**: (1) viết đúng công thức content, (2) lọc bỏ hoàn toàn ngôn ngữ AI — script nghe phải như người thật đang nói, không phải AI đang trình bày.

### Nguồn
- Idea đã chọn từ Phase 1
- `references/15-content-formulas.md`
- `references/viral-pattern-analysis.md`
- Bảng số liệu được phép dùng (xem bên dưới)

### Skill
→ GỌI: `[15-content-formulas, viral-pattern-analysis]` — chọn combo công thức phù hợp với idea
→ GỌI: `[human-voice-filter]` — lọc ngôn ngữ AI, đảm bảo 100% tính người

### Lớp 1 — Viết theo công thức

Có thể kết hợp 1-3 công thức. Thường phân vai: 1 công thức cho hook / 1 cho thân bài / 1 cho kết-CTA. Tối đa 3 — quá 3 là đang nhồi quá nhiều.

*(Tham khảo bảng chọn công thức nhanh, 5 quy tắc cứng, và bảng số liệu được phép dùng trong file gốc trên Lark Docs)*

> **Tuyệt đối không nói:** cam kết "chắc chắn duyệt" / "100%" / bất kỳ con số nào không có trong profile

### Lớp 2 — Lọc giọng người (Human Voice Filter)

Sau khi có bản draft script, chạy toàn bộ script qua bộ lọc sau trước khi output ra cho user.

*(Tham khảo danh sách dấu hiệu AI cần loại bỏ trong file gốc trên Lark Docs)*

**Chuẩn giọng đúng của An Bình Finance:**
- Nói chuyện như đang tư vấn 1-1 — không phải đứng trên sân khấu phát biểu
- Dùng "anh/chị" để gọi người xem — tạo cảm giác nói trực tiếp với họ
- Được phép dùng từ lóng nhẹ: "cái này", "thật ra", "nói thật", "chứ", "mà", "thôi"
- Câu ngắn được, câu không đủ chủ vị được — miễn là nghe tự nhiên khi đọc to
- Cảm xúc được phép lộ ra: ngạc nhiên, thẳng thắn, đồng cảm — không phải robot trung lập

**Ví dụ trước/sau:**

**TRƯỚC (giọng AI):**
> "Thực tế cho thấy rằng nhiều khách hàng thường không nắm rõ các điều khoản trong hợp đồng vay vốn, dẫn đến việc phát sinh các chi phí ngoài dự kiến, gây ảnh hưởng tiêu cực đến dòng tiền kinh doanh."

**SAU (giọng người):**
> "Nhiều anh chị ký hợp đồng vay mà không đọc kỹ. Rồi mấy tháng sau mới phát hiện ra có khoản phí mà mình không lường trước. Lúc đó thì đã muộn."

### Pass khi
- Script đã qua cả 2 lớp xử lý
- Đọc to lên toàn bộ script — không có câu nào nghe giống AI viết
- Không còn dấu hiệu AI nào trong danh sách bộ lọc bên trên
- Giữ nguyên đủ 5 quy tắc cứng từ Lớp 1

### Fail thì
- Script vẫn còn dấu hiệu AI sau Lớp 2 → chạy lại Lớp 2, không cần chạy lại Lớp 1
- Script bị mất con số cụ thể sau khi lọc → khôi phục lại số liệu, giữ giọng người
- Script <120 từ sau khi lọc → mở rộng phần Pain hoặc Bằng chứng, không thêm vào phần giới thiệu An Bình

---

## PHASE 3: VERIFY + SHIP

### Mục tiêu
Kiểm tra toàn bộ script lần cuối trước khi ship. **Đọc to lên 1 lần** — nếu có đoạn nào đọc lên thấy vấp hoặc cứng, đó là đoạn cần sửa.

### Nguồn
→ GỌI: `[ablaai-script]` — chạy 4C Check

### 4C Check cho workflow này

**Correctness — Đúng không?**
- [ ] Hook câu đầu KHÔNG bắt đầu bằng tên công ty hoặc lời chào
- [ ] Tất cả con số và case đều có trong profile hoặc kịch bản gốc (không hư cấu)
- [ ] Không có cam kết vô lý ("chắc chắn duyệt", "lãi 0%"...)

**Completeness — Đủ không?**
- [ ] Có đủ: Hook → Pain → Insight/Bằng chứng → Định vị An Bình → CTA
- [ ] Có ít nhất 1 con số cụ thể
- [ ] Độ dài 120-200 từ

**Context-fit — Đúng ngữ cảnh không?**
- [ ] Giọng văn 100% tự nhiên — đọc to lên không có câu nào nghe như AI viết
- [ ] Nhắm đúng 1 nhóm khách hàng cụ thể
- [ ] CTA gắn với nội dung vừa xem, không generic

**Consequence — Dùng thật có ổn không?**
- [ ] Không tạo kỳ vọng sai lệch về kết quả dịch vụ
- [ ] Nếu khách hàng inbox sau khi xem video này — team có thể tiếp nối tự nhiên không?

### Gate rule
- **ALL pass → SHIP** kèm ghi chú: `[Công thức: X] [Từ: Y] [Nguyên liệu: Z]`
- **1+ fail → fix → verify lại TẤT CẢ** — không skip bước nào dù chỉ fix nhỏ

---

## OUTPUT

- **File:** Script hoàn chỉnh kèm dòng ghi chú `[Công thức: X] [Từ: Y] [Nguyên liệu: Z]`
- **Lưu:** Trả về trực tiếp trong conversation; lưu vào `examples/` nếu đây là script mẫu mới cần giữ lại
- **Feed vault:** Nếu script dùng góc tiếp cận chưa từng thử → ghi chú để cập nhật `references/viral-pattern-analysis.md`

---

## EVOLUTION NOTES

**Lỗi thường gặp khi chạy workflow này:**
- **Hook vẫn bắt đầu bằng tên công ty:** Check câu đầu tiên ngay sau Lớp 1 — trước khi chạy Lớp 2
- **Script dài hơn 200 từ:** Cắt phần giới thiệu An Bình trước — phần đó thường là phần thừa nhất
- **Lớp 2 lọc quá tay làm mất số liệu:** Giữ nguyên tất cả con số, chỉ thay đổi cấu trúc câu và từ ngữ
- **CTA generic sau khi lọc giọng người:** Viết lại CTA bằng ngôn ngữ gần với nội dung vừa kể
- **Script liệt kê nhiều vấn đề:** Nếu thấy script đang "liệt kê" — chọn 1 và cắt phần còn lại

**Changelog:**
- v1.0: Khởi tạo workflow — cấu trúc 3 bước đơn giản
- v1.1: Cập nhật Phase 2 — cho phép kết hợp 1-3 công thức
- v1.2: Gộp "Chọn công thức" và "Viết script" vào 1 phase
- v1.3: Rebuild theo template chuẩn — đúng heading, đủ Gate rule, có Feed vault
- v1.4: Phase 1 bỏ skill call, thêm quy trình hỏi user + đề xuất 3 idea; Phase 2 thêm Lớp 2 Human Voice Filter
