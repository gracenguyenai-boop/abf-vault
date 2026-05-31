---
vj: Khang Vay Hay
format: Tips Ngắn (Enumerated List)
scripts_analyzed: 5
generated: 2026-05-30
usage: Đọc file này TRƯỚC KHI viết bất kỳ dòng nào. Bước đầu tiên: chọn Sub-type L, R, hay O. Đọc kèm các RULE file khác của Khang để tránh nhầm format.
---

# RULE FILE — VJ Khang Vay Hay × Tips Ngắn

> Đọc file này **TRƯỚC KHI** viết bất kỳ dòng nào.
> **Bước đầu tiên bắt buộc: Xác định Sub-type L, R, hay O.**

---

## ⚠️ QUAN TRỌNG — Đặc điểm phân biệt tuyệt đối

**Con số được công bố trong hook, và toàn bộ script là để deliver đúng con số đó.** Đây là điểm nhận dạng số 1 — không có trong bất kỳ format nào khác của Khang.

| Sub-type | Scripts | Hook | Cảm xúc chủ |
|---|---|---|---|
| **L — Loss warning** | 9 nguyên tắc mua đất, Mua nhà thế chấp | Câu chuyện mất tiền → danh sách bảo vệ | Sợ → Được trang bị |
| **R — Regulation** | Thuế khoán 3 mốc, NĐ68 5 nhóm | Alert bị phạt → phân loại nhóm | Bất ngờ → Tự kiểm tra |
| **O — Opportunity** | Đất lên thổ/hợp thửa | *"Tin cực vui"* → lợi thế mới | Hứng khởi → Hành động ngay |

**Không trộn lẫn sub-type trong cùng 1 script.**

---

## A. BLUEPRINT FORMAT

### A1. Skeleton bất biến (5/5 scripts)

```
HOOK [số lượng điểm + stakes]
    ↓
[TÙY CHỌN: Câu chuyện mất mát — chỉ Sub-type L]
    ↓
ENUMERATED LIST
Thứ nhất... Thứ hai... Thứ N...
    ↓
[TÙY CHỌN: "Tóm lại nha..." — khi ≥3 điểm phức tạp]
    ↓
CTA [mời hành động cụ thể]
```

---

### A2. Cấu trúc theo sub-type

**Sub-type L — Loss warning:**
```
[Câu chuyện mất tiền thật — 1-2 câu, không kéo dài]
→ "Để tránh rơi vào tình huống này, đây là [N] nguyên tắc/bước..."
→ ENUMERATED LIST (điểm bảo vệ)
→ CTA: mời comment tình huống riêng
```

**Sub-type R — Regulation:**
```
[Alert rủi ro + đối tượng bị ảnh hưởng]
→ "Hãy xem mình có thuộc nhóm này không..."
→ ENUMERATED LIST (nhóm/mốc phân loại)
→ [Worked example nếu cần thiết]
→ RECAP ("Tóm lại nha, anh chị chỉ cần nhớ...")
→ CTA: mời tự xếp nhóm hoặc nhờ tính toán
```

**Sub-type O — Opportunity:**
```
["Tin cực vui cho anh chị nào có [đối tượng cụ thể]"]
→ "Luật/Quy định mới vừa thay đổi [N] điều..."
→ ENUMERATED LIST (thay đổi tạo cơ hội)
→ CTA: mời kiểm tra hồ sơ / inbox ngay
```

---

### A3. Hook — cách công bố số điểm (4/5 scripts nêu tường minh)

> *"chín nguyên tắc sống còn"* (Script 1)
> *"ba trường hợp cực kỳ rõ ràng"* (Script 2)
> *"năm nhóm người kinh doanh bị ảnh hưởng ngay lập tức"* (Script 3)
> *"ba điều sau đây"* (Script 4)

Script 5 không nêu số — dùng *"Thứ nhất... Thứ hai... Cuối cùng"* thay thế. Đây là ngoại lệ — nên nêu số tường minh khi có thể.

---

### A4. Bộ 4 yếu tố của mỗi list item

| Yếu tố | Bắt buộc | Mô tả |
|---|---|---|
| **Label** | ✅ | *"Thứ nhất / Nhóm hai / Mốc ba"* |
| **Rule** | ✅ | Điều cần làm hoặc tránh |
| **Reason** | ⬜ | Tại sao — có thể bỏ ở item ngắn |
| **Specificity** | ✅ (≥1/item) | Số tiền, %, ngày, ví dụ cụ thể |

**Ví dụ item đủ 4 yếu tố (Script 2 — thuế khoán):**
> **Label:** *"Mốc cuối cùng, doanh thu trên 3 tỷ"*
> **Rule:** *"Bắt buộc phải hạch toán, tính thuế 17% lợi nhuận thực tế"*
> **Reason:** *"Mọi giao dịch từ 5 triệu trở lên phải chuyển khoản"*
> **Specificity:** *"Số tiền phạt có thể lên tới hàng trăm triệu, thậm chí hàng tỷ"*

---

### A5. 3 mức độ dài của list item

| Mức | Độ dài | Khi dùng | Ví dụ |
|---|---|---|---|
| **Ngắn** | 1 câu | Điểm đơn giản, dễ nhớ | *"Thứ năm: Cẩn thận bẫy giá rẻ bất ngờ. Đất rẻ thường hay có biến."* |
| **Trung bình** | 2–3 câu | Cần giải thích nguyên nhân + hành động | Đa số items |
| **Dài** | 4–6 câu | Có điều kiện phân nhánh hoặc worked example | Script 2 (thuế), Script 1 (nguyên tắc 2, 6) |

> **Quy tắc variation:** Xen kẽ item ngắn và dài — không để tất cả items dài bằng nhau.
> **Quy tắc năng lượng:** Điểm quan trọng nhất ở vị trí 1 hoặc 2 — năng lượng giảm dần về cuối list.

---

### A6. Worked example — kỹ thuật mạnh nhất (1/5 scripts, Sub-type R)

Dùng nhân vật giả định để tính toán thực tế thay cho giải thích trừu tượng:

> *"Ví dụ như anh Minh, chủ quán bún bò, doanh thu 1 tỷ 2... VAT 3% = 36 triệu... TNCN 1,5% trên 720 triệu = 10,5 triệu... Tổng 46,5 triệu."*

> **Khi dùng:** Sub-type R khi cần cement khái niệm thuế/tính toán. Không dùng trong L hoặc O.

---

### A7. Recap section — chỉ khi ≥3 điểm phức tạp (2/5 scripts)

> *"Tóm lại nha, anh chị chỉ cần nhớ ba mốc: dưới 500 triệu... từ 500 triệu đến 3 tỷ... Trên 3 tỷ..."*

Liệt kê lại cực ngắn (mỗi mốc ½ câu) — **không giải thích lại**.
Bù đắp cho việc năng lượng giảm dần ở cuối list.

---

### A8. Audience self-identification — cơ chế kéo xem (4/5 scripts)

Người xem buộc phải tự hỏi *"Mình có thuộc nhóm này không?"* → xem tiếp để tự phân loại:

> *"anh chị xem mình có làm trong danh sách này không"* (Script 3)
> *"anh chị nào đang kinh doanh chưa biết..."* (Script 2)
> *"anh chị nào đang cần vốn"* (Script 5)

---

### A9. CTA phân loại theo sub-type

| Sub-type | CTA | Ví dụ |
|---|---|---|
| **L** | Comment tình huống riêng | *"Anh chị nào khi mua nhà có yếu tố khác cần lưu ý thì comment cho em Khang"* |
| **R** | Tự xếp nhóm HOẶC nhờ tính | *"Comment ngành nghề và doanh thu để em Khang tính thử miễn phí"* |
| **O** | Kiểm tra hồ sơ / inbox ngay | *"Em cam kết... hãy kiểm tra lại hồ sơ của mình sớm nhất"* / inbox |

> **Lưu ý:** TIPS CTA phải mời **hành động cụ thể** (comment/inbox/tính toán) — không chỉ *"Follow em Khang"* đơn thuần.

---

### A10. ❌ Không được có

1. **Hook không công bố số điểm** — người xem không biết sắp nghe bao nhiêu điểm
2. **List item chỉ có label, không có rule + specificity** — không phải bullet point rỗng
3. **Tất cả items dài bằng nhau** — cần variation để tránh monotony
4. **Điểm quan trọng nhất đặt ở cuối** — năng lượng giảm dần về cuối
5. **Template kết quả vay** (số tiền + lãi + thời hạn) — đó là Thực địa
6. **Customer voice opener** — đó là Tư vấn hội thoại
7. **"Em Thảo"** hoặc tên khác trong CTA — luôn là *"em Khang"*
8. **CTA chỉ là "Follow em Khang"** — phải mời hành động cụ thể
9. **Recap khi list ≤3 điểm đơn giản** — không cần thiết

---

## B. VOICE DNA

### B1. Xưng hô

| Vai | Cách gọi | Ghi chú |
|---|---|---|
| VJ tự xưng (ngôi 1) | **em** | Trong câu thông thường |
| VJ tự xưng trong CTA | **em Khang** | *"Comment cho em Khang"* — branding |
| Gọi khán giả | **anh chị** | Không dùng "bạn" |
| Nhân vật worked example | **anh Minh / chị X** | Nhân vật giả định có tên — tăng credibility |

---

### B2. VoiceMarker theo vị trí

**Hook — 3 pattern:**

`Sub-type L — câu mất tiền:`
> *"Có những gia đình đã mất trắng cả tỉ đồng chỉ sau một đêm."*

`Sub-type R — alert + đối tượng:`
> *"Anh chị nào đang kinh doanh chưa biết về luật thuế khoán mới — rủi ro bị phạt rất cao"*

`Sub-type O — tin vui:`
> *"Tin cực vui cho anh chị nào đang có đất nông nghiệp muốn lên thổ cư"*

**Label mỗi item — 3 pattern:**
- *"Thứ nhất / Thứ hai / Thứ ba..."*
- *"Nhóm một / Nhóm hai..."*
- *"Mốc một / Mốc hai..."*

**Câu nhấn trong item:**
- *"Lưu ý nhỏ nhé..."* — chèn điều kiện quan trọng sau item chính
- *"Điều quan trọng nhất nhé..."* / *"Đây là cái quan trọng nhất nha"* — nhấn item trọng tâm

**Câu chốt ngắn kết item:**
- *"Đừng tiếc vài triệu để check địa chính"*
- *"Đất rẻ thường hay có biến"*
- *"Không check là mất tiền oan"*

**Recap opener:**
- *"Tóm lại nha, anh chị chỉ cần nhớ [N] [mốc/điều/bước]..."*

---

### B3. Mẫu câu đặc trưng (trích nguyên văn)

**Hook Sub-type L — 2 mẫu:**
> *"Có những gia đình đã mất trắng cả tỉ đồng chỉ sau một đêm. Có những người khóc ròng vì ký vào một tờ giấy mà không đọc kỹ."*

> *"Mất trắng 2 tỷ vì mua nhà thế chấp mà không biết 3 điều này."*

**Hook Sub-type R — 2 mẫu:**
> *"Từ mùng 1 tháng 1 năm 2026, thuế khoán bị bãi bỏ. Anh chị nào đang kinh doanh chưa biết điều này — rủi ro bị phạt hàng trăm triệu."*

> *"NĐ68 vừa có hiệu lực — đây là 5 nhóm người kinh doanh bị ảnh hưởng ngay lập tức."*

**Hook Sub-type O — 1 mẫu:**
> *"Tin cực vui cho anh chị nào đang có đất nông nghiệp muốn lên thổ cư hoặc muốn hợp thửa — luật đất đai 01/01/2026 vừa thay đổi 3 điều quan trọng."*

**Worked example — 1 mẫu:**
> *"Ví dụ như anh Minh, chủ quán bún bò, doanh thu 1 tỷ 2. VAT 3% trên toàn bộ doanh thu = 36 triệu. TNCN 1,5% trên phần trên 100 triệu = 10,5 triệu. Tổng cộng anh Minh phải nộp 46,5 triệu một năm."*

**Recap — 1 mẫu:**
> *"Tóm lại nha, anh chị chỉ cần nhớ ba mốc: dưới 500 triệu thì không cần lo; từ 500 triệu đến 3 tỷ thì áp thuế khoán mới; trên 3 tỷ thì bắt buộc hạch toán đầy đủ."*

**Câu cam kết (Sub-type O — dùng sparingly):**
> *"Em cam kết với anh chị: nếu hồ sơ đủ điều kiện theo luật mới, em sẽ hỗ trợ đến khi xong."*

---

### B4. AnalogyBridge

> **Tips Ngắn hiếm dùng analogy** — ưu tiên số liệu cụ thể và worked example. Khi cần làm rõ khái niệm, dùng worked example (tính toán thực tế) thay vì metaphor.

---

### B5. Vocabulary

**ĐƯỢC DÙNG — Signature words riêng của Tips Ngắn:**

| Từ / cụm | Sub-type | Cách dùng |
|---|---|---|
| Thứ nhất / Nhóm một / Mốc một | Tất cả | Label item, không bao giờ bỏ |
| Lưu ý nhỏ nhé... | Tất cả | Chèn điều kiện sau item chính |
| Đây là cái quan trọng nhất nha | Tất cả | Nhấn item trọng tâm |
| Tóm lại nha... | Tất cả | Mở recap section |
| Đất rẻ thường hay có biến | L | Câu chốt cảnh báo |
| Đừng tiếc vài triệu để check | L | Call to action nhẹ trong item |
| Anh chị xem mình thuộc nhóm nào | R | Audience self-identification |
| Comment ngành nghề + doanh thu | R | CTA tính toán miễn phí |
| Tin cực vui cho... | O | Hook opener |
| Em cam kết với anh chị | O | Sparingly — không dùng cho mọi script |
| Ví dụ như [tên] [nghề] doanh thu [X] | R | Mở worked example |
| điểm mấu chốt mà nhiều người chưa biết | R/O | Nhấn insight chưa phổ biến |

**KHÔNG ĐƯỢC DÙNG trong Tips Ngắn:**

| Từ / pattern | Lý do |
|---|---|
| *"Em Khang vừa đi [địa điểm]..."* | Đó là Thực địa |
| *"Khang ơi / Khang em..."* | Đó là Tư vấn hội thoại |
| *"Em Khang thương quá"* | Đó là Thực địa |
| *"Em Khang bó tay"* | Đó là Selfie Type W |
| Template kết quả vay 5 yếu tố | Đó là Thực địa |
| *"Follow em Khang"* đơn thuần | CTA quá yếu — phải mời hành động cụ thể |
| *"Em Thảo"* trong CTA | Sai tên — luôn kiểm tra |
| List item không có số/ví dụ | Bullet point rỗng = không dùng được |

---

### B6. Nhịp câu

- **Hook:** câu ngắn, ngắt mạnh, cảm xúc cao — *"Có những gia đình đã mất trắng cả tỉ đồng chỉ sau một đêm."* (1 câu, không đệm)
- **Enumerate methodically:** đều đặn, mỗi item tự hoàn chỉnh — người nghe biết *"còn X điểm nữa"*
- **Variation:** xen kẽ item ngắn (1 câu) và item dài (3-4 câu) để tránh monotony
- **Worked example:** câu dài nhất trong script — tính toán thực tế, chậm rãi
- **Recap:** nhanh, mỗi mốc ½ câu — không giải thích lại
- **CTA:** 1-2 câu, mời hành động cụ thể

---

## C. KNOWLEDGE PAYLOAD

### C1. TechConcept chuẩn (Tips Ngắn)

| Thuật ngữ | Misconception | Cách Khang giải thích trong list |
|---|---|---|
| Sổ đỏ vs sổ hồng | Cứ có giấy tờ là an toàn | Phải là sổ đỏ chính chủ — không nhận hợp đồng tay, giấy tờ lá cải |
| Quy hoạch đất | Không cần check vì đất đang dùng bình thường | Check quy hoạch tổng thể trước khi mua — đất trong quy hoạch bị siết sẽ mất giá trị thế chấp |
| Thuế khoán mới 2026 | Cách tính thuế giống như trước | 3 mốc doanh thu hoàn toàn khác nhau — dưới 500M / 500M-3 tỷ / trên 3 tỷ |
| Mua nhà thế chấp | Ngân hàng đang giữ sổ = đủ uy tín | Phải check trực tiếp ngân hàng A chi nhánh B — không tin qua trung gian |
| Đất nông nghiệp lên thổ | Phức tạp, mất nhiều thời gian như cũ | Luật đất đai 01/01/2026 thay đổi điều kiện — nhiều trường hợp dễ hơn trước |
| NĐ68 | Chỉ ảnh hưởng doanh nghiệp lớn | 5 nhóm hộ kinh doanh nhỏ đều bị ảnh hưởng — cơ quan thuế đã nhìn thấy mọi giao dịch |

---

### C2. Cấu trúc conflict formula

```
[Rủi ro/Cơ hội lớn] + [Người xem chưa biết N điều] = Lý do phải xem đến hết
```

| Script | Rủi ro/Cơ hội | N điều chưa biết |
|---|---|---|
| 9 nguyên tắc | Mất trắng tỷ khi mua đất | 9 nguyên tắc bảo vệ |
| Thuế khoán | Bị phạt hàng trăm triệu | 3 mốc doanh thu và cách tính |
| NĐ68 | Cơ quan thuế thấy mọi giao dịch | 5 nhóm bị ảnh hưởng |
| Mua nhà thế chấp | Tiền mất, nhà vẫn của ngân hàng | 3 bước check trước khi xuống tiền |
| Đất lên thổ | Đất đang bị định giá thấp hơn thực tế | 3 thay đổi quy định mới |

---

### C3. Vị trí Khang trong format này

**TIPS Khang = Giáo viên trung lập** — quyền lực đến từ kiến thức, không từ câu chuyện cá nhân.

| Format | Vai Khang | Nguồn quyền lực |
|---|---|---|
| Thực địa | Người thương cảm, đi tận nơi | Hành động vật lý + kết quả số |
| Selfie | Insider / Tinh hoa | Thông tin không đối xứng |
| Tư vấn HT | Chuyên gia tư vấn | Reframe + root cause analysis |
| Tips Ngắn | **Giáo viên trung lập** | **Kiến thức có cấu trúc + worked example** |

---

## D. SO SÁNH 5 FORMAT CỦA KHANG

| Tiêu chí | Thực địa | Talking Head | Selfie | Tư vấn HT | Tips Ngắn |
|---|---|---|---|---|---|
| Cấu trúc cốt lõi | Case study | Case hoặc phân tích | Monologue thông tin | Customer Q + Khang A | **Enumerated list** |
| Số điểm trong script | 1 case | 2–3 điểm | 2–3 điểm | 1 vấn đề | **3–9 điểm** |
| Số announce ở hook | Không | Không | Không | Không | **Có — bắt buộc** |
| Recap *"Tóm lại nha"* | Không | Đôi khi | Không | Không | **Có — khi ≥3 điểm** |
| Worked example | Không | Không | Không | Không | **Có (Sub-type R)** |
| Opening story mất tiền | Không | Không | Không | Không | **Có (Sub-type L)** |
| Mật độ thông tin | Thấp | Trung bình | Trung bình | Thấp | **Cao nhất** |
| Cảm xúc Khang | *"Thương quá"* | Nhà phân tích | Insider/Tinh hoa | Kiên nhẫn | **Giáo viên trung lập** |
| CTA | Ẩn / inbox | Inbox / Comment | Follow/Comment/Inbox | Inbox | **Comment cụ thể / inbox tính toán** |

---

## E. 5 CÂU TỰ KIỂM TRA

> ① Hook có **công bố số điểm cụ thể** không? Người xem có biết mình sắp nghe bao nhiêu điểm? — Không → thêm số vào hook.

> ② Mỗi item trong list có **ít nhất 1 con số, ngày, %, hoặc ví dụ cụ thể** không? — Item không có số = bullet point rỗng, viết lại.

> ③ **Điểm quan trọng nhất** có nằm ở vị trí đầu tiên hoặc thứ hai không? — Ở cuối = đặt lại thứ tự.

> ④ Nếu có **≥3 điểm phức tạp**, có phần *"Tóm lại nha"* để recap không? — Thiếu = thêm recap.

> ⑤ CTA có **mời hành động cụ thể** (comment ngành/số nhóm/inbox tính toán) chứ không chỉ *"follow"*? — Chỉ follow = viết lại CTA.
