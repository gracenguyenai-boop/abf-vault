# Type JD — Job Descriptions Của Tất Cả Types

> Dùng cho Phase 2: TYPE MATCH.
> Sau khi xác định nhánh, so sánh INTENT với JD type trong nhánh đó.
> Vault root: `/Users/nguyenlocnhi/Downloads/ABF-Vault/`

---

## CC — Content Creator (L1 → L4)

### L1 — Framework (Tư Duy Nền)
**JD:** Lưu framework tư duy cao nhất — giải thích TẠI SAO một cách tiếp cận content hoạt động, không phải CÁCH LÀM.
**Ownership Test:** "Note này giải thích nguyên lý nền của kỹ thuật, không phải cách dùng kỹ thuật?"
**Ví dụ:** PAS framework, STEPPS model, 3U formula, viral loop theory
**Template:** `CC-ContentCreator/CC-01-Atomic/L1-Framework/_template-framework.md`
**Path ghi:** `CC-ContentCreator/CC-01-Atomic/L1-Framework/YYYY-MM-DD-[slug].md`

### L2 — Kiến Thức Nghề (Kỹ Năng Viết)
**JD:** Lưu kỹ năng thực chiến — giải thích CÁCH LÀM một kỹ thuật viết cụ thể có thể áp dụng ngay.
**Ownership Test:** "Note này chỉ tôi làm được một thứ ngay sau khi đọc xong?"
**Ví dụ:** Cách viết hook câu hỏi, cách dùng transition, cách viết CTA tránh bị report
**Template:** `CC-ContentCreator/CC-01-Atomic/L2-KienThucNghe/_template-concept-writing.md`
**Path ghi:** `CC-ContentCreator/CC-01-Atomic/L2-KienThucNghe/YYYY-MM-DD-[slug].md`

### Ranh Giới CC L1 vs L2

| Câu hỏi kiểm tra | → L1 | → L2 |
|---|---|---|
| "Sau khi đọc, tôi LÀM ĐƯỢC ngay không?" | KHÔNG — cần thêm bước | CÓ — áp dụng ngay |
| "Note giải thích CƠ CHẾ hay CÁCH DÙNG?" | Cơ chế / nguyên lý (why it works) | Cách áp dụng cụ thể (how to do) |
| "Có thể dùng như rule trong checklist ngay không?" | KHÔNG trực tiếp | CÓ — check được ngay |

**Ví dụ borderline:**
| Note | L1 hay L2? | Lý do |
|---|---|---|
| "PAS framework và tại sao nó hoạt động" | L1 | Giải thích nguyên lý — không phải bước làm cụ thể |
| "Cách áp dụng PAS vào script vay vốn — 3 bước cụ thể" | L2 | Dùng được ngay sau khi đọc |
| "Tại sao hook câu hỏi thu hút người xem (tâm lý)" | L1 | Lý thuyết tâm lý, không phải kỹ thuật thực chiến |
| "5 mẫu hook câu hỏi copy-paste cho script tài chính" | L2 | Áp dụng ngay, không cần bước trung gian |

### L3 — Kiến Thức Đặc Thù ABF (Quy Tắc Domain)
**JD:** Lưu quy tắc và ràng buộc domain — những gì PHẢI biết khi làm content tài chính/TikTok ABF.
**Ownership Test:** "Note này là rule/constraint bắt buộc phải tuân theo, không phải kỹ năng tự chọn?"
**Ví dụ:** Từ ngữ bị cấm TikTok ngành tài chính, 4 trụ cột content kênh vay vốn, hook patterns của ABF
**Template:** `CC-ContentCreator/CC-01-Atomic/L3-KienThucDacThu/_template-domain-abf.md`
**Path ghi:** `CC-ContentCreator/CC-01-Atomic/L3-KienThucDacThu/YYYY-MM-DD-[slug].md`

### L4 — PDCA (Review & Lesson)
**JD:** Lưu bài học cải tiến — những gì đã làm, kết quả thực tế, và rút ra được gì cho lần sau.
**Ownership Test:** "Note này là nhìn lại (retrospective), không phải nhìn tới (prescriptive)?"
**Ví dụ:** Review video tuần, phân tích comment pattern, sprint retrospective
**Template:** `CC-ContentCreator/CC-01-Atomic/L4-PDCA/_template-pdca-review.md`
**Path ghi:** `CC-ContentCreator/CC-01-Atomic/L4-PDCA/YYYY-MM-DD-[slug].md`

---

## LS — Loan Specialist (L1 → L4 + 4fcase)

### L1 — Framework (Khung Tư Duy Tín Dụng)
**JD:** Lưu framework phân tích tổng thể — cách TƯ DUY về một hồ sơ vay, không phải bước thực hiện.
**Ownership Test:** "Note này là khung tư duy (cách nhìn), không phải quy trình làm từng bước?"
**Ví dụ:** Framework 4F, 5C credit model, risk matrix tư duy
**Template:** `LS-LoanSpecialist/LS-01-Atomic/L1-Framework/_template-framework-ls.md`
**Path ghi:** `LS-LoanSpecialist/LS-01-Atomic/L1-Framework/YYYY-MM-DD-[slug].md`

### L2 — Kiến Thức Nghề (Nghiệp Vụ Tín Dụng)
**JD:** Lưu quy trình và kỹ năng nghiệp vụ — CÁCH LÀM từng bước cụ thể trong công việc tín dụng.
**Ownership Test:** "Note này chỉ tôi làm được một thao tác nghiệp vụ cụ thể ngay sau khi đọc?"
**Ví dụ:** Cách đọc báo cáo CIC, cách tính LTV, quy trình thẩm định tài sản
**Template:** `LS-LoanSpecialist/LS-01-Atomic/L2-KienThucNghe/_template-concept-banking.md`
**Path ghi:** `LS-LoanSpecialist/LS-01-Atomic/L2-KienThucNghe/YYYY-MM-DD-[slug].md`

### L3 — Kiến Thức Đặc Thù An Bình (Nội Bộ AB)
**JD:** Lưu kiến thức nội bộ An Bình — những gì CHỈ ĐÚNG với sản phẩm/quy trình của An Bình Bank.
**Ownership Test:** "Note này chỉ áp dụng được tại An Bình, không dùng được ngân hàng khác?"
**Ví dụ:** Điều kiện sản phẩm vay cụ thể của AB, quy trình phê duyệt nội bộ, pricing đặc thù
**Template:** `LS-LoanSpecialist/LS-01-Atomic/L3-KienThucDacThu/_template-domain-banking-ops.md`
**Path ghi:** `LS-LoanSpecialist/LS-01-Atomic/L3-KienThucDacThu/YYYY-MM-DD-[slug].md`

### L4 — PDCA (Lesson Learned từ Case)
**JD:** Lưu bài học từ case thực tế — lesson learned, không phải case data đã điền.
**Ownership Test:** "Note này là lesson learned (tổng quát), không phải dữ liệu của 1 case cụ thể?"
**Template:** `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/_template-pdca-review.md`
**Path ghi:** `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/YYYY-MM-DD-[slug].md`

### L4/4fcase — Case Đầy Đủ 4F
**JD:** Lưu hồ sơ khách đã phân tích hoàn chỉnh F1 (Facts) + F2 (Feelings) + F3 (Findings) + F4 (Future).
**Ownership Test:** "Note này có đủ cả 4F, không F nào trống?"
**Điều kiện bắt buộc:** Phải có đủ F1+F2+F3+F4.
→ Nếu thiếu bất kỳ F nào → lưu vào `LS-00-Inbox/incomplete/`, KHÔNG tạo 4fcase
**Template:** `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/_template-4fcase.md`
**Path ghi:** `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/4fcases/YYYY-MM-DD-[ma-ho-so].md`

---

## TD — Trà Đá / Market Analyst (L1 → L4, L3 có domain)

### L1 — Framework (Công Cụ Đọc Thị Trường)
**JD:** Lưu framework để ĐỌC HIỂU THỊ TRƯỜNG tổng quát — công cụ phân tích, không phải sự kiện cụ thể.
**Ownership Test:** "Note này là công cụ phân tích dùng được cho nhiều sự kiện, không phải phân tích 1 sự kiện?"
**Ví dụ:** Framework đọc tín hiệu lãi suất, cách phân tích chu kỳ BĐS
**Template:** `TD-TraDa/TD-01-Atomic/L1-Framework/_template-framework-td.md`
**Path ghi:** `TD-TraDa/TD-01-Atomic/L1-Framework/YYYY-MM-DD-[slug].md`

### L2 — Kiến Thức Nghề (Macro Concept)
**JD:** Lưu định nghĩa và cơ chế vận hành của một khái niệm vĩ mô — "X là gì và hoạt động như thế nào."
**Ownership Test:** "Note này trả lời 'X là gì và hoạt động như thế nào' ở cấp độ khái niệm tổng quát?"
**Ví dụ:** Lãi suất điều hành là gì, DTI hoạt động như thế nào, cơ chế vòng xoáy BĐS
**Template:** `TD-TraDa/TD-01-Atomic/L2-KienThucNghe/_template-concept-macro.md`
**Path ghi:** `TD-TraDa/TD-01-Atomic/L2-KienThucNghe/YYYY-MM-DD-[slug].md`

### L3 — Kiến Thức Đặc Thù Domain (Tin tức / Sự kiện / Phân tích)
**JD:** Lưu tin tức, sự kiện, phân tích gắn với một domain thị trường cụ thể và một thời điểm cụ thể.
**Ownership Test:** "Note này là sự kiện/tin tức/phân tích cụ thể (không phải khái niệm tổng quát)?"
**Domain — chọn 1:**
| Domain | Folder | Ownership Test |
|---|---|---|
| BDS | `L3-KienThucDacThu/BDS/` | "Gắn chính với thị trường nhà đất, dự án, giá BĐS?" |
| CK | `L3-KienThucDacThu/CK/` | "Gắn chính với cổ phiếu, chỉ số, IPO, ĐHĐCĐ?" |
| TC | `L3-KienThucDacThu/TC/` | "Gắn chính với lãi suất, NHNN, tín dụng, ngân hàng?" |
| CS | `L3-KienThucDacThu/CS/` | "Gắn chính với luật mới, nghị định, thuế, quy định nhà nước?" |
**Template:** `TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/_template-domain-macro.md`
**Path ghi:** `TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/[BDS|CK|TC|CS]/YYYY-MM-DD-[slug].md`

### Quy Tắc Chọn Domain Khi Sự Kiện Chồng Lấn

> **Rule:** Chọn domain của **SỰ KIỆN CHÍNH** (trigger/nguyên nhân) — không phải hiệu ứng phụ.
> Domain phụ → thêm vào YAML `topics`.

| Ví dụ sự kiện | Domain | Lý do |
|---|---|---|
| NHNN giảm lãi suất (tác động thị trường BĐS) | TC | Trigger = quyết định NHNN về tín dụng |
| Luật Kinh doanh BĐS sửa đổi (ảnh hưởng vay mua nhà) | CS | Trigger = văn bản pháp lý mới |
| Cơn sốt đất TP.HCM (ngân hàng tăng lãi suất BĐS theo) | BDS | Trigger = biến động thị trường nhà đất |
| Ngân hàng siết hạn mức tín dụng BĐS | TC | Trigger = chính sách tín dụng ngân hàng |

→ Vẫn không xác định được → HỎI USER

### L4 — PDCA (TD Insight)
**JD:** Lưu insight rút ra từ quá trình làm TD — comment scraping, viewer sentiment, meeting synthesis.
**Ownership Test:** "Note này là insight từ quá trình quan sát/phân tích, không phải tin tức hay khái niệm?"
**Ví dụ:** Viewer sentiment về chủ đề lãi suất, comment pattern từ video TD, insight meeting
**Template:** `TD-TraDa/TD-01-Atomic/L4-PDCA/_template-td-pdca.md`
**Path ghi:** `TD-TraDa/TD-01-Atomic/L4-PDCA/YYYY-MM-DD-[slug].md`

---

## Shared — Cross-branch (7 types theo nội dung)

> Mọi type phải pass Cross-Branch Test: "CC + LS + TD cùng đọc đều thấy hữu ích?"

| Type | JD | Ownership Test | Path ghi |
|---|---|---|---|
| concept | Định nghĩa + cơ chế của khái niệm cross-branch | "Note này trả lời 'X là gì' theo cách cả 3 nhánh đều cần?" | `Shared/Shared-01-Atomic/concept/` |
| framework | Công cụ phân tích có cấu trúc dùng được cross-branch | "Note này là tool phân tích, dùng được trong nhiều ngữ cảnh khác nhau?" | `Shared/Shared-01-Atomic/framework/` |
| insight | Quan sát phi hiển nhiên hữu ích cho cả 3 nhánh | "Note này khiến cả CC + LS + TD đều nói 'à ra vậy'?" | `Shared/Shared-01-Atomic/insight/` |
| perspective | Quan điểm có lập trường, liên quan đến cả 3 nhánh | "Note này có lập trường rõ, có thể không đồng ý được?" | `Shared/Shared-01-Atomic/perspective/` |
| story | Tường thuật sự kiện hữu ích cross-branch | "Note này có đủ: ai → làm gì → kết quả, hữu ích cho cả 3?" | `Shared/Shared-01-Atomic/story/` |
| strategy | Khuyến nghị hành động liên quan đến cả 3 nhánh | "Note này trả lời 'vậy phải làm gì', hữu ích cho cả 3?" | `Shared/Shared-01-Atomic/strategy/` |
| quote | Phát ngôn uy tín dùng được cross-branch | "Note này chủ yếu là lời ai đó, có thể trích dẫn trong CC + LS + TD?" | `Shared/Shared-01-Atomic/quote/` |

**Template cho Shared:** Dùng `VJ/_templates/_template-[type].md`, điền `branch: Shared` trong YAML.

---

## VJ — Virtual Journalist (7 types + special)

> VJ dùng cùng 7 types với Shared, nhưng phải gắn với kênh cụ thể.
> **`layer: null` cho tất cả VJ types** — VJ không dùng hệ L1-L4.

### Mô Tả + Ownership Test 7 Types Trong Ngữ Cảnh VJ

| Type | JD trong VJ | Ownership Test | Path ghi |
|---|---|---|---|
| concept | DNA kênh, tone & voice, định vị thương hiệu cá nhân VJ | "Note này mô tả 'kênh này là ai' và 'nói chuyện như thế nào'?" | `VJ/VJ-[kênh]/VJ-01-Atomic/concept/YYYY-MM-DD-[slug].md` |
| framework | Cấu trúc script, hook formula đặc trưng kênh — có thể dùng lại nhiều script | "Note này là template/công thức viết nhiều script cùng loại?" | `VJ/VJ-[kênh]/VJ-01-Atomic/framework/YYYY-MM-DD-[slug].md` |
| insight | Feed Loop — quan sát phi hiển nhiên rút ra SAU khi video ship (data, comment, trend) | "Note này được rút ra từ video đã publish — không phải kế hoạch trước?" | `VJ/VJ-[kênh]/VJ-01-Atomic/insight/YYYY-MM-DD-[slug].md` |
| perspective | Góc nhìn thị trường, framing vĩ mô phục vụ content kênh cụ thể | "Note này có lập trường rõ, áp dụng vào cách framing content của kênh này?" | `VJ/VJ-[kênh]/VJ-01-Atomic/perspective/YYYY-MM-DD-[slug].md` |
| story | Case KH, hành trình vay, tình huống thực từ ngữ cảnh kênh | "Note này kể chuyện ai → làm gì → kết quả, gắn với kênh cụ thể này?" | `VJ/VJ-[kênh]/VJ-01-Atomic/story/YYYY-MM-DD-[slug].md` |
| strategy | Sprint plan, content direction, quyết định chiến lược kênh | "Note này là quyết định định hướng CHỈ đúng với kênh này, không dùng kênh khác?" | `VJ/VJ-[kênh]/VJ-01-Atomic/strategy/YYYY-MM-DD-[slug].md` |
| quote | Comment viewer hay, câu nói của KH, trích dẫn dùng được trong script | "Note này chủ yếu là lời ai đó — có thể dùng ngay làm hook/closing trong script?" | `VJ/VJ-[kênh]/VJ-01-Atomic/quote/YYYY-MM-DD-[slug].md` |

**Template cho VJ:** `VJ/_templates/_template-[type].md` (điền `branch: VJ-[kênh]`, `layer: null`)

### Ranh Giới Dễ Nhầm Trong VJ Types

| Câu hỏi về content | Đi về đâu |
|---|---|
| "Kênh này xưng hô thế nào, tone gì, định vị thế nào?" | concept |
| "Dùng cấu trúc/formula nào để viết loạt script?" | framework |
| "Sau khi video ship, mình rút ra được gì từ data/comment?" | insight (Feed Loop) |
| "KH X đã vay thế nào — câu chuyện thực từ kênh?" | story |
| "Kênh nên đi theo hướng content nào? Sprint tháng này?" | strategy |
| "Thị trường đang thế nào — framing để content kênh bắt trend?" | perspective |
| "Comment hay từ viewer / câu KH nói để dùng lại?" | quote |

### Loại đặc biệt (KHÔNG phải atomic note)
| Loại | Xử lý |
|---|---|
| Script đã ship | Lưu ở `VJ/VJ-[kênh]/scripts/YYYY-MM-DD-[topic].md` — không fill atomic template |
| Sprint log | Append vào `VJ/VJ-[kênh]/VJ-01-Atomic/sprint-log.md` — không tạo file mới |
