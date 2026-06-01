# Workflow Case Study

**name:** TikTok-casestudy-workflow

**description:** Quy trình tự động hóa phân tích hồ sơ vay vốn thực tế và sản xuất kịch bản case study viral trên TikTok với độ dài dao động từ 150–300 từ, đúng DNA từng kênh, đã nạp bối cảnh vĩ mô thời điểm vay và che đi thông tin không public.

- **Input:** file hồ sơ PDF/audio/image + 4F phân tích + broll (nếu có) + style viết để thực hiện ở bước 5
- **Output:** script TikTok hoàn chỉnh theo style kênh, công thức content, DNA văn phong.
- **Platform:** TikTok

---

## /tiktok-casestudy-workflow

### SCOPE

- **Bài toán:** Biến hồ sơ vay vốn thô (PDF, ghi âm, ảnh) thành kịch bản TikTok case study viral, đúng style từng kênh, chuẩn DNA văn phong, inject thông tin dynamic theo tháng/quý.
- **Input:** File sổ đỏ/CIC (PDF/scan), file ghi âm buổi họp case study (audio), ảnh thực tế, broll (nếu có), ghi chú 4F phân tích của user, chọn style kênh, chọn công thức content + tổng hợp các nguồn thông tin liên quan đến case study trong obsidian vault + style viết để thực hiện ở bước 5
- **Output:** 1 file kịch bản TikTok hoàn chỉnh, gồm hook + body + CTA, tích hợp b-roll note, độ dài 60–180 giây đọc thoại trên Platform: TikTok.
- **Hoàn thành khi:** Script đã qua qa-scan 4C pass toàn bộ, thông tin dynamic đã inject, không chứa thông tin không được phép public, không chứa từ cấm và những từ vi phạm chính sách TikTok.
- **Skills gọi:** [ ....]

> ⚠️ **QUY TẮC CHẠY TOÀN BỘ WORKFLOW**
> - Agent phải chạy **lần lượt 10 phase**, step by step, không được nhảy cóc.
> - **Lưu ý anh Thế Anh:** Phải lưu file ban đầu (input) vào NotebookLM, các key decision, output sau từng phase.

---

## PHASE 0: XÁC NHẬN B-ROLL TRƯỚC KHI CHẠY

### Mục tiêu

Xác định ngay từ đầu user có B-roll sẵn hay không để agent chọn đúng nhánh viết kịch bản từ Phase 7 trở đi. **Không chạy bất kỳ phase nào trước khi có câu trả lời.**

### Nguồn

- User input trực tiếp

### Skill

→ Không cần gọi skill - agent hỏi trực tiếp user 1 câu duy nhất:

> *"Bạn có sẵn b-roll (video cảnh quay thực tế, tài liệu, hành động) cho case này không, hay sẽ tự quay sau khi có kịch bản?"*

- **Có B-roll** → ghi nhận danh sách/mô tả b-roll, đánh dấu `broll_mode: A`
- **Chưa có / tự quay sau** → đánh dấu `broll_mode: B`

### Pass khi

- User đã xác nhận rõ ràng 1 trong 2 lựa chọn
- Nếu có B-roll: user đã mô tả sơ bộ nội dung từng file b-roll

### Fail khi và hành động

- User chưa trả lời → hỏi lại, không chạy tiếp cho đến khi có câu trả lời rõ ràng

> ⛔ **BLOCKING RULE - Phase 0**
> Agent KHÔNG được chạy Phase 1 khi chưa có xác nhận `broll_mode` từ user.

---

## PHASE 1: THU THẬP & CHUẨN HÓA HỒ SƠ

### Mục tiêu

Đến cuối phase này, agent phải có một bản hồ sơ chuẩn hóa duy nhất tương tự như bảng bên dưới, tổng hợp từ tất cả file đầu vào, kèm phân tích 4F, sẵn sàng cho các phase sau khai thác.

### Nguồn

- User upload: PDF (sổ đỏ, CIC, ...), audio (ghi âm họp), image (ảnh thực tế)
- User input: ghi chú 4F phân tích thủ công (nếu có)

→ GỌI: `[global skill]` của anh Thế Anh để xử lý, chuẩn hóa file dữ liệu đầu vào (đọc file raw)

→ GỌI: `[4F - analyzer]` - Phân tích hồ sơ theo khung 4F:

- **Facts:** Số liệu vay, Các vấn đề ảnh hưởng đến khoản vay (độ tuổi, tài sản, nguồn thu, dòng tiền, CIC, định giá,...)
- **Feelings:** Tâm lý khách hàng, áp lực, kỳ vọng, lo ngại, và cảm nhận từ cán bộ xử lý hồ sơ về hồ sơ khách hàng này
- **Findings:** Những điểm nào ổn, điểm nào vô lý, những vấn đề và vướng mắc nào cần xử lý và cần phải giải quyết (ví dụ như tuổi quá cao thì không sử dụng được gói vay nào?)
- **Future:** Hành động cụ thể trong tương lai, Đưa ra những giải pháp nào để xử lý và dự kiến xử lý như nào?

### Pass khi

- Các thông tin được phân tích phải được fill vào trong Form chuẩn hóa có đầy đủ các trường: Tên cơ hội, ngày tạo cơ hội, nhóm vấn đề, thông tin, 4F nhận định hồ sơ, list, giải pháp của An bình, Lý do hồ sơ không thành công, Sản phẩm bank áp dụng
- Đủ 4 nhóm 4F có dữ liệu (không được để trống yếu tố nào)

### Fail khi và hành động

- Nếu audio không transcribe được → hỏi user cung cấp transcript thủ công hoặc tóm tắt buổi họp
- Nếu PDF bị mã hóa/scan mờ → hỏi user upload lại bản rõ hơn hoặc nhập tay số liệu chính
- Nếu thiếu Facts cốt lõi (giá trị tài sản, số tiền vay) → hỏi lại user; nếu user không confirm thì không chạy tiếp
- Nếu thiếu 1 trong số các trường (Tên cơ hội, ngày tạo cơ hội, nhóm vấn đề, thông tin, 4F nhận định hồ sơ, list, giải pháp của An bình, Lý do hồ sơ không thành công, Sản phẩm bank áp dụng) thì cần hỏi lại user để bổ sung thông tin, nếu user không bổ sung thì dừng không chạy nữa

---

## PHASE 2: DỰNG BỐI CẢNH THỜI GIAN (TIME BUILDER)

### Mục tiêu

Đến cuối phase này, agent phải có bối cảnh thời điểm vay cụ thể: chính sách lãi suất, tình hình vĩ mô, sự kiện kinh tế nổi bật ảnh hưởng đến quyết định vay vốn của khách hàng tại thời điểm đó - thật chi tiết và cụ thể, rõ ràng để tạo dramatic tension thực tế trong story arc, không phải mô tả chung chung.

### Nguồn

- Hồ sơ chuẩn hóa từ Phase 1 (thời điểm vay)
- Lấy thêm nguồn tin tức về kinh tế, tài chính, lãi suất cho vay, lãi suất tiết kiệm, chính sách ngân hàng, các tin tức vi mô, vĩ mô,... tại thời điểm vay bằng cách Gọi MCP của perplexity

### Skill

→ GỌI: `[time-builder]` - Dựng timeline vay: thời điểm nộp hồ sơ, thời điểm giải ngân, chính sách lãi suất áp dụng, gói vay phù hợp từ danh sách SP An Bình, thời gian xử lý thực tế vs kỳ vọng.

→ GỌI: `[macro-context]` - Tra cứu và tóm tắt bối cảnh vĩ mô tại thời điểm vay: chính sách tiền tệ NHNN, lãi suất thị trường, biến động bất động sản, chính sách liên quan (ví dụ như thuế hộ kinh doanh), sự kiện kinh tế đáng chú ý gây ảnh hưởng đến quyết định và khả năng vay vốn.

### Pass khi

- Có ít nhất 1 điểm bối cảnh vĩ mô liên quan trực tiếp đến quyết định vay của KH, kèm thông tin số liệu cụ thể, rõ ràng, chi tiết
- Chính sách lãi suất và gói vay An Bình áp dụng tại thời điểm đó được xác định rõ ràng
- Timeline vay có đủ: ngày nộp hồ sơ → thời gian xử lý → ngày giải ngân

### Fail khi và hành động

- Nếu không xác định được thời điểm vay (nộp hồ sơ) và giải ngân → hỏi đến khi nào user cung cấp thông tin thì thôi
- Nếu macro-context không có dữ liệu cho thời điểm đó → dùng bối cảnh gần nhất và gắn disclaimer `[BỐI CẢNH GẦN NHẤT - CẦN XÁC NHẬN]`

---

## PHASE 3: DỰNG STORY ARC

### Mục tiêu

Đến cuối phase này, agent phải có một story arc hoàn chỉnh và đủ chiều sâu, gồm đầy đủ 7 yếu tố bên dưới - mỗi yếu tố phải thật chi tiết, cụ thể, rõ ràng cho case này, không được viết chung chung, sáo rỗng. Story arc này là nền tảng để viết kịch bản ở các phase sau.

### Nguồn

- 4F từ Phase 1 (đặc biệt Feelings và Future)
- Time Builder từ Phase 2 (bối cảnh tạo dramatic tension)

### Skills

→ GỌI: `[story-arc]` - Xây dựng story arc phải có đầy đủ 8 yếu tố theo khung sau:

1. **Thời điểm vay** (Tháng/năm + lý do vay cụ thể)
2. **Bối cảnh vĩ mô tại thời điểm vay** (Chính sách NHNN, lãi suất, BĐS, tình hình kinh tế,...)
3. **Chân dung khách hàng** (Tuổi, nghề, thu nhập, tài sản, dòng tiền, tâm lý,...)
4. **Chính sách của ngân hàng tại thời điểm vay** (Các gói vay của các ngân hàng áp dụng kèm điều kiện)
5. **Tình hình vĩ mô, Sự kiện kinh tế** (Sự kiện hay thông tin nào ảnh hưởng đến quyết định và khả năng vay vốn của KH tại thời điểm đó, ví dụ như dịch covid 19 làm nguồn vốn ngưng đọng, kinh doanh sụt giảm, dẫn đến không có khả năng trả nợ ngân hàng chẳng hạn)
6. **Những vướng mắc, khó khăn của khách khi đi vay**
7. **Giải pháp của An Bình nếu có thể xử lý được**
8. **Cơ hội kinh doanh nếu khách hàng vay được** (nó giải quyết được vấn đề gì cho khách hàng như mở rộng cơ hội kinh doanh đúng mùa vụ hay có thêm tiền để đầu tư sinh lời như mua 1 khu đất đang rất có tiềm năng tăng giá,...)

### Pass khi

- Story arc có đủ 8/8 yếu tố được nêu ở trên, thông tin đầy đủ, rõ ràng, chi tiết (story arc >800 từ)
- Resolution có kết quả đo lường được (số tiền, thời gian, tỷ lệ)
- Không có yếu tố nào có thể copy sang case khác mà không cần chỉnh sửa

### Fail khi và hành động

- Có ít hơn 7 yếu tố được nêu ra trong story-arc → hỏi lại user về trường thông tin còn thiếu để user cung cấp thêm thông tin để bổ sung cho đủ 7 yếu tố, nếu user không cung cấp thì dừng không chạy nữa
- Nếu story arc < 800 từ → agent tự bổ sung thông tin cho đủ, không được để mơ hồ, sáo rỗng, lưu ý không được tự bịa thông tin mà phải lấy tin chính xác từ nguồn đã có và dữ liệu nhập vào.

---

## PHASE 3.5: GOM CONTEXT → 1 FILE MD

### Mục tiêu
Gom toàn bộ output từ Phase 1 + Phase 2 + Phase 3 thành 1 khối MD duy nhất trong working memory. Bắt buộc trước khi chọn style và viết kịch bản — tránh tràn context ở các phase sau.

### Không gọi skill — GEMINI tự tổng hợp theo template:

```
# CONTEXT FILE — [ma-ho-so-an-danh] — [dd/mm/yy]

## 1. HỒ SƠ CHUẨN HÓA (Phase 1)
### Form 4F
[paste form 4F đã điền đủ từ 4F-analyzer]
### Sản phẩm bank áp dụng
[từ Phase 1]

## 2. BỐI CẢNH THỜI GIAN (Phase 2)
### Timeline vay
[ngày nộp → xử lý → giải ngân]
### Vĩ mô tại thời điểm vay
[output macro-context — tóm tắt 3-5 câu, giữ số liệu cụ thể]

## 3. STORY ARC (Phase 3)
[paste đủ 8 yếu tố story arc]

## 4. EXAMPLE ANALYSIS (Phase 0)
[paste nguyên `[EXAMPLE ANALYSIS]` từ Bước 2.6]
```

### ✅ Pass khi
- File MD có đủ 4 section
- Không còn output nào nằm rải rác trong conversation — tất cả đã gom vào đây
- Tổng độ dài file < 2000 từ (nếu vượt → tóm tắt bớt phần vĩ mô, giữ nguyên 4F + Story Arc + Example Analysis)

---

## PHASE 4: CHỌN STYLE VIẾT

### Mục tiêu

Đến cuối phase này, agent phải xác định được style kênh phù hợp và profile BTL tương ứng để khai thác, hoặc xác nhận style đã được user chỉ định.

### Nguồn

- 4F từ Phase 1
- Story arc từ Phase 3
- Bảng DNA Content Ratio bên dưới

### DNA Content Ratio - Bảng chuẩn 4 style

Mỗi style kênh có tỷ lệ phân bổ cố định giữa **nhóm trọng tâm** và **nhóm bổ sung**. Agent phải áp đúng ratio này khi phân tích - không được tự điều chỉnh tỷ lệ.

| Style | Nhóm trọng tâm (tỷ lệ cố định) | Nhóm bổ sung (phần còn lại) |
|---|---|---|
| **Tuyết Anh** | 50% - Bệnh của KH + Giải pháp An Bình + Tệp KH có thể làm được | 50% - suy luận từ story arc |
| **Khang** | 55% - Điều kiện hồ sơ thành công + Điểm nghẽn xử lý hồ sơ + Network & quan điểm + 4F hồ sơ | 45% - suy luận từ story arc |
| **Huy** | 50% - Kinh tế vĩ mô + 4F hồ sơ + Điều kiện ghi nhận (checklist) + Sản phẩm của An bình | 50% - suy luận từ story arc |
| **Duke** | 60% - Tệp KH có thể làm được + 4F hồ sơ + Cơ hội kinh doanh + Điều kiện hồ sơ thành công | 40% - suy luận từ story arc |

Nhóm bổ sung = agent tự chọn từ 10 mục còn lại dựa trên dữ liệu thực tế của case. Mục nào không có dữ liệu từ case → bỏ qua, không ép khai thác.

**Danh sách 10 mục có thể khai thác:**

1. Danh sách sản phẩm An Bình
2. Điều kiện hồ sơ thành công
3. Kinh tế vĩ mô
4. Bệnh của khách hàng
5. Điểm nghẽn xử lý hồ sơ
6. Điều kiện ghi nhận (checklist)
7. Network và quan điểm
8. Tệp KH có thể làm được
9. 4F hồ sơ
10. Cơ hội kinh doanh

### Skill

→ Không cần gọi skill - agent thực hiện 2 bước:

**Bước 4.1 - Đề xuất style kênh:**

Hỏi user xem muốn chọn style nào để khai thác và viết kịch bản, hay muốn để AI tự chọn.
- User chọn style nào thì áp DNA của style đó
- Nếu user nói tự chọn thì auto chọn style Tuyết Anh

**Bước 4.2 - Áp DNA ratio, lập bản đồ khai thác:**

Sau khi có style, agent áp DNA ratio tương ứng vào case và hiển thị theo format:

```
🎙 STYLE: [Tên kênh]
→ Lý do gợi ý: [2 câu cụ thể từ đặc điểm case]

📊 BẢN ĐỒ KHAI THÁC NỘI DUNG:

▌NHÓM TRỌNG TÂM ([X]% script)
• [Mục 1]: [Dữ liệu cụ thể từ case này sẽ khai thác - 1 câu]
• [Mục 2]: [Tương tự]
• [Mục 3]: [Tương tự]

▌NHÓM BỔ SUNG ([Y]% script)
• [Mục A]: [Lý do chọn mục này cho case này - 1 câu]
• [Mục B nếu có]: [Tương tự]

🚫 Không khai thác: [liệt kê các mục không có dữ liệu từ case]

Bạn đồng ý với bản đồ này không? Muốn thay đổi style hoặc điều chỉnh mục nào không?
```

### Pass khi

- Agent đã áp đúng DNA ratio của style được chọn - không tự điều chỉnh tỷ lệ
- Mỗi mục trong nhóm trọng tâm đều có dữ liệu cụ thể từ case được map vào
- Nhóm bổ sung chỉ chứa mục có dữ liệu thực - không có mục "ép" vào cho đủ
- User đã xác nhận cả style lẫn đầu mục khai thác

### Fail thì

- Nếu case không có dữ liệu cho 1 mục trong nhóm trọng tâm → ghi rõ `[Thiếu dữ liệu]`, giữ nguyên tỷ lệ nhưng phân bổ phần đó sang mục bổ sung có data, hỏi user xác nhận
- Nếu case không khớp rõ với style nào → hỏi user chọn trực tiếp, không tự suy luận
- Không fallback về Tuyết Anh nếu user chưa nói "tự chọn đi"

> ⛔ **BLOCKING RULE - Phase 4**
> Hiển thị bản đồ khai thác đầy đủ theo format trên. DỪNG và hỏi: *"Bạn đồng ý với style và bản đồ khai thác này không? Muốn điều chỉnh gì không? Nếu ổn thì mình tiếp tục sang Phase 5."*
> Chỉ chạy Phase 5 sau khi user xác nhận cả style lẫn bản đồ khai thác.

---

## PHASE 5: VIẾT HOOK

### Mục tiêu

Đến cuối phase này, agent phải có 1 Hook đã được kiểm tra độc lập - trước khi viết bất kỳ phần nào của body. Hook là điểm chạm đầu tiên quyết định người xem có dừng lại xem tiếp không.

### Nguồn — 3 thành phần bắt buộc

1. **CONTEXT FILE** từ Phase 3.5 — toàn bộ 4F + Story Arc + bối cảnh (đọc từ đây, không đọc lại phase cũ)
2. **[FORMAT RULE]** từ Bước 2.5 — quy tắc viết hook của format được chọn
3. **[EXAMPLE ANALYSIS]** từ Bước 2.6 — cấu trúc hook, độ dài, từ đặc trưng, điều không có trong examples

> ⚠️ Hook phải nhại đúng cấu trúc hook phổ biến nhất trong `[EXAMPLE ANALYSIS]` ② trước, sau đó mới chấm SUCCESS score.

### Skills

**Bước 5.1** → GỌI: `[hook-writer]` - Viết 3 phiên bản hook khác nhau (số liệu gây sốc / câu hỏi kích thích / tuyên bố đảo ngược kỳ vọng) dựa trên nguồn ở trên, agent chọn 1 phiên bản phù hợp nhất với style kênh đã xác định ở Phase 4.

Mỗi hook: 20–40 từ, đúng xưng hô của kênh, dùng chi tiết thực từ hồ sơ.

**Bước 5.2** → GỌI: `[success-framework-scorer]`

Chấm điểm 3 phiên bản hook theo framework SUCCESS (Chip & Dan Heath). Đối chiếu từng hook với 6 tiêu chí, tính tổng điểm, xác nhận hoặc thay thế RECOMMENDED từ bước 3.1 dựa trên điểm số. Chỉ chạy SAU KHI hook-writer đã trả về đủ 3 phiên bản hook.

### Pass khi

- Có đủ 3 phiên bản hook với 3 patterns KHÁC NHAU
- Mỗi hook có độ dài 20-40 từ
- Mỗi hook có lý do hiệu quả rõ ràng
- success-framework-scorer đã chạy và trả về bảng điểm SUCCESS đầy đủ cho cả 3 hooks
- 1 recommendation Hook bám vào style kênh và được điểm cao nhất
- Hỏi lại user 1 lần nữa xem có lấy recommendation Hook này không? Nếu không chọn thì user sẽ phải chọn 1 hook, nếu user không chọn hook, dừng bước này lại cho đến khi user chọn

### Fail khi và hành động

- 3 hooks dùng cùng 1 pattern → gọi lại hook-writer với yêu cầu buộc đa dạng pattern
- Tất cả 3 hooks có SUCCESS score < 60% → gọi lại hook-writer viết lại từ đầu, không chọn hook chất lượng thấp

> ⛔ **BLOCKING RULE - Phase 5 (BẮT BUỘC)**
> Hook phải pass qua các yêu cầu của phase 5 thì mới được tiến hành tiếp phase 6, trường hợp không pass thì phải thực hiện lại đến khi nào pass thì thôi

---

## PHASE 6: ÁP DỤNG CÔNG THỨC CONTENT

### Mục tiêu

Đến cuối phase này, story arc từ Phase 3 được restructure theo công thức content được chọn, tạo ra skeleton kịch bản với các section được đánh dấu rõ ràng.

### Nguồn — 3 thành phần bắt buộc

1. **CONTEXT FILE** từ Phase 3.5 — nguồn dữ kiện duy nhất, không đọc lại phase cũ
2. **[FORMAT RULE]** từ Bước 2.5 — quy tắc cấu trúc body, CTA, title của format
3. **[EXAMPLE SCRIPTS] + [EXAMPLE ANALYSIS]** từ Bước 2.5/2.6 — nhại cấu trúc, độ dài, từ đặc trưng; tránh pattern trong ④ "Điều KHÔNG có"

> ⚠️ Trước khi gọi bất kỳ skill nào: đọc `[EXAMPLE ANALYSIS]` ①②③④⑤⑥ — dùng làm constraint cho toàn bộ phase này.
> - ⑤ Cách câu kết nối: **mỗi câu phải là phản ứng cảm xúc tự nhiên với câu trước** — không liệt kê thông tin độc lập
> - ⑥ Hành trình cảm xúc: **viết theo cung bậc cảm xúc từ examples** — không viết theo checklist cấu trúc

### Skills

**Bước 6.1** → GỌI: `[body-writer]` - Viết phần body dựa trên công thức content được chọn, kết nối liền mạch từ Hook. Map story arc vào cấu trúc công thức:

- **PAS:** Phù hợp case có "bệnh" rõ, conflict mạnh
- **AIDA:** Phù hợp case có kết quả ấn tượng làm điểm bán
- **BAB:** Phù hợp case transformation story rõ nét
- **4U:** Phù hợp case có số liệu cụ thể, thời gian rõ
- *(11 công thức còn lại tương tự - agent tự map dựa trên đặc điểm case)*

**15 công thức content có thể áp dụng:** AIDA, A FOREST, FAS, FAB, BAB, APP, PAS, 4A, 5A, 4C, 4P, 4U, 3S, 5 sự cản trở, 3 lý do vì sao.

Output: Body text đầy đủ, section headers theo công thức, 120–260 từ.

**Bước 6.2** → GỌI: `[cta-writer]` - Viết CTA phù hợp với DNA kênh:

Output: 1–3 câu CTA, gắn liền với Resolution của story arc.

**Bước 6.3** → GỌI: `[title-writer]` - Viết title video TikTok (8-14 từ), bám vào nội dung kịch bản ở trên (hook+body+CTA).

Output: 3 phiên bản title, agent recommend 1.

**Bước 6.4** → GỌI: `[caption-hashtag-writer]` - Viết caption post (≤ 30 từ) + bộ hashtag (5–10 hashtag: mix broad + niche + branded).

Output: caption + hashtag list.

**Bước 6.5** → GỌI: `[human-authenticity-scorer]` - Quét toàn bộ Body + CTA + Caption: loại bỏ cụm từ robot ("Hãy cùng khám phá...", ...), kiểm tra nhịp câu có tự nhiên không khi đọc to, kiểm tra transition giữa các section có mượt không.

Output: Authenticity Score /100 + danh sách câu/cụm từ cần rewrite.

### Pass khi

- Skeleton có đủ tất cả section của công thức được chọn
- Mỗi section có nội dung cụ thể, không chung chung
- Thời lượng ước tính (WPM × word count) nằm trong 60–150 giây
- CTA đúng soft/hard theo DNA kênh
- Có 3 phiên bản title + 1 recommendation
- Caption ≤ 50 từ, hashtag 5–10 cái
- human-authenticity-scorer: Authenticity Score ≥ 80/100, không còn flag chưa xử lý

### Fail khi và hành động

- Nếu skeleton vượt 180 giây → cắt bớt phần Agitate/Interest, giữ Hook và Resolution nguyên vẹn
- Nếu Authenticity Score < 85 → rewrite câu bị flag, chạy lại scorer trước khi tiếp tục

---

## PHASE 7: B-ROLL MAPPING

### Mục tiêu

Đến cuối phase này, agent phải có danh sách b-roll được gắn vào từng segment của script, kèm note cho editor. Nếu b-roll đã có sẵn, script được viết theo b-roll. Nếu chưa có, agent gợi ý danh sách b-roll cần quay để user thực hiện sau.

### Nguồn

- Kịch bản hoàn chỉnh từ phase 5 + phase 6 (hook + body + cta)
- User input: danh sách b-roll đã có (nếu có), mô tả file b-roll (từ phase 0)

### Skills

→ GỌI: `[broll-mapper]` - Phân tích script và chạy theo đúng nhánh:

- **Nhánh A** (`broll_mode: A` - có b-roll sẵn): Map từng cảnh b-roll vào segment tương ứng trong script, viết lại lời thoại bám sát hành động b-roll đã có. VD: "Đi thẩm định cùng cán bộ ngân hàng tại địa phương" → viết lời thoại dẫn dắt hành động đó.
- **Nhánh B** (`broll_mode: B` - chưa có b-roll): Viết kịch bản talking-head thuần, kèm danh sách b-roll suggestion cho từng segment (mô tả cảnh quay gợi ý, khả thi quay thực tế, ≥ 5 cảnh cụ thể).

### Pass khi

- Mọi segment trong script đều có b-roll note (hoặc talking head nếu không có b-roll sẵn)
- Nhánh A: lời thoại không mâu thuẫn với hành động trong b-roll
- Nhánh B: danh sách b-roll suggestion có ít nhất 5 cảnh cụ thể, khả thi quay thực tế

### Fail khi và hành động

- Nếu user cung cấp b-roll nhưng không mô tả nội dung → hỏi user mô tả ngắn từng file b-roll
- Nếu b-roll không liên quan đến story arc → chuyển sang Nhánh B

> ⛔ **BLOCKING RULE - Phase 7**
> Nếu user bảo có broll nhưng không cung cấp nội dung mô tả thì cần hỏi lại user để xác nhận, nếu user không trả lời thì dừng không chạy nữa, còn nếu user bảo tùy chọn thì coi như không có broll, quay lại viết theo nhánh B

---

## PHASE 8: LỌC QUA DNA KÊNH

### Mục tiêu

Đến cuối phase này, skeleton script được viết thành full script, đã mang đúng văn phong, cách xưng hô, cách thể hiện đặc trưng của kênh được chọn.

### Nguồn

- Skeleton script từ Phase 7

### Skills

→ GỌI: `[dna-filter]` - Viết full script từ skeleton, áp dụng DNA kênh:

- Cách xưng hô (mình/anh/chị/tôi/em...)
- Nhịp điệu câu (ngắn-dài-ngắn / chuỗi liệt kê / câu hỏi tu từ...)
- Từ ngữ đặc trưng và từ ngữ bị cấm của kênh
- Cách kết thúc CTA (soft/hard, câu hỏi/mệnh lệnh)
- Tone tổng thể (chuyên gia tư vấn / người kể chuyện / người bạn đồng hành)

→ GỌI: `[oral-communication-filter]` - Chạy bắt buộc sau [dna-filter], trước khi pass Phase 8. Đây là skill chuyên biệt chuyển toàn bộ script sang văn nói tự nhiên, đơn giản, gần gũi - loại bỏ mọi yếu tố hoa mỹ và dramatize sai mức.

### Pass khi

- Không có câu nào dùng sai xưng hô ("em" / "An Bình" - không phải tên creator)
- Script đọc tự nhiên, không có cảm giác AI viết hoặc dùng từ quá sách vở
- CTA phù hợp soft/hard theo DNA kênh
- Độ dài: 150–300 từ, tùy brief
- Oral-communication Score ≥ 95/100 - không còn flag chưa xử lý
- Không còn từ nào trong blacklist van-noi-filter sót lại
- Mọi vấn đề trong script phản ánh đúng severity label từ Phase 1 - không có đoạn nào bị nâng mức

### Fail khi và hành động

- Nếu DNA profile kênh chưa có trong vault → hỏi user mô tả 3 đặc điểm văn phong chính của kênh rồi mới viết
- Nếu xưng hô sai → sửa toàn bộ trước khi tiếp tục, không patch từng chỗ

---

## PHASE 9: FILTER PUBLIC

### Mục tiêu

Đến cuối phase này, script được cập nhật để tất cả thông tin không thể public được mask hoặc thay thế bằng placeholder.

### Nguồn

- Full script từ Phase 8
- Vault: BTL/Story - 4F - Giải pháp ABF - Điều kiện thành công - Sản phẩm Bank áp dụng (danh sách thông tin không public: tên KH, địa chỉ cụ thể, số hợp đồng, thông tin nội bộ...)

### Skills

→ GỌI: `[non-public-filter]` - Thực hiện rà soát toàn script, thay thế thông tin không được public bằng dạng tổng quát hóa (tên KH → "một khách hàng tại [tỉnh/thành]", số tiền cụ thể → làm tròn hoặc dùng dải, địa chỉ → khu vực)

### Pass khi

- Không có thông tin định danh cá nhân (tên, CCCD, số hợp đồng, địa chỉ nhà cụ thể) trong script
- Không có thông tin giải pháp hoặc vấn đề nào không được phép truyền thông xuất hiện trong script

### Fail khi và hành động

- Nếu không rõ thông tin nào là non-public → hỏi user review danh sách trước khi mask, không tự quyết định

---

## PHASE 10 (FINAL): VERIFY + SHIP

### Mục tiêu

Kiểm tra toàn bộ script trước khi bàn giao. Script chỉ được ship khi pass toàn bộ 4C.

### Skills

→ GỌI: `[tiktok-policy-scanner]`

Quét toàn bộ kịch bản tìm từ cấm + vi phạm chính sách TikTok VN. Output: Danh sách flags (nếu có) + đề xuất thay thế

→ GỌI: `[channel-fit-validator]`

Đánh giá kịch bản có khớp chân dung kênh không: tone, pronoun, niche, audience level. Output: Fit Score /100 + danh sách điểm lệch (nếu có)

→ GỌI: `[human-authenticity-scorer]`

Chấm điểm tính người lần cuối sau tất cả chỉnh sửa. Output: Authenticity Score /100 + danh sách câu/cụm từ cần sửa (nếu có)

→ **[SIMILARITY SCORE]** — Không cần gọi skill, GEMINI tự chấm dựa trên `[EXAMPLE ANALYSIS]`:

```
SIMILARITY SCORE
① Cấu trúc   : [X/10] — hook/body/CTA có khớp pattern phổ biến ở [EXAMPLE ANALYSIS]② không?
② Độ dài      : [X/10] — tổng từ số có nằm trong ±20% so với độ dài trung bình examples?
③ Từ đặc trưng: [X/10] — có dùng ≥3 cụm từ từ [EXAMPLE ANALYSIS]③? Liệt kê các cụm đã dùng.
④ Không có    : [X/10] — có còn pattern nào trong [EXAMPLE ANALYSIS]④ sót lại không?
⑤ Kết nối câu : [X/10] — mỗi câu trong body có phải là phản ứng cảm xúc với câu trước không, hay đang liệt kê thông tin độc lập?
⑥ Cảm xúc arc : [X/10] — hành trình cảm xúc có khớp với [EXAMPLE ANALYSIS]⑥ không? (tò mò → nhận ra → muốn làm gì đó)

TỔNG: [X/60] = [X%]
→ ≥ 75%: PASS  |  < 75%: ghi rõ tiêu chí nào thấp nhất → sửa đúng chỗ đó → chạy lại similarity score
```

### 4C Check cho workflow này

**Correctness**

- [ ] Số liệu trong script (giá trị tài sản, số vay, lãi suất) khớp với hồ sơ gốc Phase 1
- [ ] Bối cảnh thời gian Phase 2 không bị áp sai vào case (không nhầm chính sách năm này vào case năm khác)
- [ ] Thông tin dynamic đã inject là phiên bản mới nhất trong vault
- [ ] Severity của mọi vấn đề trong script khớp với bảng severity Phase 1 - không có vấn đề nào bị nâng mức

**Completeness**

- [ ] Script có đủ 5 điểm story arc: Hook → Conflict → Turning Point → Resolution → CTA
- [ ] B-roll note có mặt ở tất cả segment cần minh họa
- [ ] Không còn placeholder chưa điền
- [ ] Van Noi Score ≥ 85/100 (từ Phase 8)

**Context-fit**

- [ ] Xưng hô đúng: "em" hoặc "An Bình" - không có tên creator nào trong script
- [ ] Văn phong, nhịp điệu đúng DNA kênh được chọn
- [ ] Công thức content áp dụng nhất quán từ đầu đến cuối
- [ ] Hook phù hợp với audience của kênh (không dùng jargon ngân hàng cho kênh đại chúng)

**Consequence**

- [ ] Không có thông tin non-public nào sót lại sau dynamic-injector
- [ ] Không có cam kết lãi suất tuyệt đối không có cơ sở pháp lý
- [ ] Nếu script đề cập chính sách nhà nước → có disclaimer "theo chính sách tại thời điểm..."
- [ ] Không có từ nào trong blacklist ngôn ngữ sót lại

### Gate rule

| Kiểm tra | Điều kiện Pass |
|---|---|
| tiktok-policy-scanner | 0 flags → ✅ |
| channel-fit-validator | Fit Score ≥ 80 → ✅ |
| human-authenticity-scorer | Score ≥ 90 → ✅ |
| similarity-score | Tổng ≥ 75% → ✅ |

- **ALL 4 PASS → SHIP**
- **1+ fail → fix đúng điểm fail → chạy lại CHỈ check đó → verify lại**

---

## OUTPUT

- **File:** `casestudy_[style-kênh]_[tháng-năm]_[mã-hồ-sơ-ẩn-danh].md`
- **Lưu:** `/outputs/scripts/tiktok/`
- **Feed vault:** Có - sau khi ship, tách 4F phân tích + bảng severity vào `01-Atomic/4fcases/` để train cho các case sau
