# TikTok News Viral Workflow

**Name:** TikTok-news-viral-workflow

**Description:** Đây là quy trình để có thể tự động phân tích tin tức thô và sản xuất kịch bản news viral trên TikTok với độ dài kịch bản dao động từ 200-350 từ.

**Inputs:** Link bài báo hoặc nội dung tin tức thô dưới dạng ảnh hoặc ghi âm + quan điểm, góc nhìn cá nhân về vấn đề này + insight/cmt của người xem

**Outputs:** Kịch bản hoàn chỉnh (Hook, Body, CTA, Caption) đã qua kiểm duyệt.

---

## SCOPE

- **Bài toán:** Chuyển hóa từ tin tức, báo chí khô khan thành kịch bản video ngắn viral trên TikTok nhằm cung cấp thông tin chính xác, hoặc sự thật
- **Input:** Link bài báo hoặc nội dung tin tức thô dưới dạng ảnh hoặc ghi âm + quan điểm, góc nhìn cá nhân (theo mô hình 4F) về vấn đề này + insight/cmt của người xem + quan điểm chuyên gia (nếu có)
- **Output:** Kịch bản text, dài khoảng 200-350 từ (1'-1'45s), dùng cho nền tảng TikTok (bao gồm Caption và hashtag)
- **Hoàn thành khi:** Kịch bản vượt qua hệ thống QA Gates, không chứa từ cấm, không chứa thuật ngữ chuyên ngành khó hiểu.

---

## PHASE 0: ĐÃ ĐƯỢC XỬ LÝ BỞI GEMINI PRE-PROCESSING

> ⚠️ Phase 0 (đọc memory, đọc input, upload NbLM, 3 frameworks, hỏi VJ góc nhìn, search vault) đã được GEMINI.md Phase 0 thực hiện trước khi load workflow này. Agent BỎ QUA phase này và bắt đầu từ Phase 1.
> Context từ GEMINI Phase 0 sẽ được truyền vào Phase 1.

---

## PHASE 1: PHÂN TÍCH TIN TỨC

### Mục tiêu

Đến cuối phase này, phải có 6 mục phân tích hoàn chỉnh từ tin tức thô, bao gồm: bối cảnh + diễn biến, nguyên nhân sâu xa, ảnh hưởng và tác động, so sánh với dữ liệu lịch sử/nước ngoài (nếu có), kiểm tra tính chính xác từ quan điểm của VJ, lời khuyên/dự báo. Đây là nền tảng dữ kiện để toàn bộ workflow phía sau không bị sai lệch.

### Nguồn (NotebookLM)

- Link bài báo / ảnh chụp / file ghi âm (user cung cấp)
- Quan điểm cá nhân VJ (user cung cấp)
- Insight/comment người xem (user cung cấp)
- Quan điểm chuyên gia (nếu có)

### Skills — thực hiện theo thứ tự

**Bước 1.1** → GỌI: `[news-context-synthesizer]`
Tìm và tổng hợp tất cả các đầu báo, tin tức, báo cáo, dữ liệu từ các nguồn chính thống về sự kiện/vấn đề.

**Bước 1.2** → GỌI: `[event-timeline-builder]`
Dựng bối cảnh + diễn biến theo trục thời gian ở bước 1.1.

**Bước 1.3** → GỌI: `[ethos-credibility-analyzer]`
CHẠY SONG SONG với 1.2. Phân tích uy tín của nguồn phát ngôn (ai nói, có lợi ích gì, có đáng tin không). Đây là yêu cầu bắt buộc — không được bỏ qua.

**Bước 1.4** → GỌI: `[root-cause-analyzer]`
Phân tích 3 lớp: vấn đề → nguyên nhân sâu xa → động cơ ẩn giấu.

**Bước 1.5** → GỌI: `[stakeholder-impact-mapper]`
Map tác động đến từng nhóm đối tượng cụ thể (ai hưởng lợi, ai chịu thiệt, tác động trực tiếp/gián tiếp).

**Bước 1.6** → GỌI: `[historical-comparator]`
Tìm 2-3 precedent lịch sử trong/ngoài nước nếu có. Nếu không có, ghi rõ.

**Bước 1.7** → GỌI: `[synthesizing-viewpoints]`
So sánh quan điểm của user với các chuyên gia/báo cáo phân tích xem nó đúng hay sai và phản biện, và kiểm tra ở vault ở công ty để nội suy xem nó ảnh hưởng như thế nào đến ngành tài chính, ngân hàng và tác động thế nào đến người đi vay.

**Bước 1.8** → GỌI: `[forecast-synthesizer]`
Tổng hợp dự báo ngắn hạn + dài hạn + lời khuyên thực tế cho người xem bình thường phải khớp với chân dung khách hàng của kênh ABVV.

### ✅ Pass khi

- Có đủ tối thiểu 5/6 đầu mục phân tích bao gồm: bối cảnh + diễn biến, nguyên nhân sâu xa, ảnh hưởng và tác động, kiểm tra tính chính xác từ quan điểm của VJ, lời khuyên/dự báo
- Bắt buộc phải có mục ảnh hưởng như thế nào đến khách hàng mục tiêu của kênh (đối chiếu đúng với personal brand)
- Có thể bao gồm so sánh với dữ liệu lịch sử/nước ngoài (nếu có)
- Không có mục nào để trống hoặc ghi "Không đủ thông tin" (trừ mục so sánh với dữ liệu lịch sử/nước ngoài nếu thực sự chưa từng xảy ra trước đây)

### ❌ Fail thì

- Nếu input quá sơ sài (không đủ tối thiểu 3/4 đầu mục input cần nhập): **HỎI USER** — yêu cầu bổ sung nội dung hoặc link gốc
- Nếu nguồn không xác định được: `[ETHOS ANALYSIS]` ghi "Nguồn ẩn danh — không thể xác minh uy tín" và đánh dấu
- Nếu tin tức có dấu hiệu fake news (mâu thuẫn logic, không có nguồn dẫn): **DỪNG** và báo user trước khi tiếp tục

---

## PHASE 2: TÌM VÀ CHỌN ANGLE PHÙ HỢP

### Mục tiêu

Đến cuối phase này, Agent phải tìm ra 1 WINNER Angle thông qua hệ thống suy luận logic và chấm điểm định lượng. Quá trình này không dựa trên cảm tính mà phải đối chiếu trực tiếp giữa dữ kiện từ Phase 1 với bộ khung framework STEPPS (Social Currency, Triggers, Emotion, Public, Practical Value, Stories) và 3Us (Unique, Useful, Urgent) để đảm bảo tính khách quan và khả năng viral.

### Nguồn

- 5 mục phân tích từ Phase 1
- Channel Profile (chân dung kênh: tệp khách hàng, tone giọng,..)
- VJ Perspective (góc nhìn cá nhân VJ về sự kiện này: 4F)

### Skills

**Bước 2.1** → GỌI: `[viewer-sentiment-analysis]`
Input: Comment/bình luận của người xem để hiểu người xem đang thực sự nghĩ gì, tranh luận gì, và đâu là câu hỏi/nỗi đau thực sự của họ về chủ đề này (Dựa trên 7 Psychological Triggers That Make People Say "Yes" Instantly).

**Bước 2.2** → GỌI: `[angle-generator]`
Sinh 5 angles khác nhau, tư duy dựa trên 2 framework STEPPS (Social Currency, Triggers, Emotion, Public, Practical Value, Stories) và 3Us (Unique, Useful, Urgent) đảm bảo đáp ứng đủ 9 tiêu chí.

**Bước 2.3** → GỌI: `[angle-scorer]`
Chấm điểm 5 angles theo 5 tiêu chí có trọng số. Công bố WINNER rõ ràng với lý do dựa trên ma trận chấm điểm.

### ✅ Pass khi

- Có đúng 5 Angle Cards từ angle-generator với đủ 4 trường: Tên, Góc khai thác, Emotion, Hook mẫu
- Bảng điểm đầy đủ 4 tiêu chí × 5 angles
- WINNER được tuyên bố rõ ràng với điểm cao nhất
- Không có angle nào có Risk Level > 7/10 lọt vào top 1

### ❌ Fail thì

- Nếu 5 angles quá giống nhau (cùng emotion): Gọi lại angle-generator với yêu cầu "buộc đa dạng hóa emotion"
- Nếu tất cả angles đều có Risk Level cao: **HỎI USER** — sự kiện có nhạy cảm chính trị không, có muốn tiếp tục không

---

## PHASE 2.5: GOM CONTEXT → 1 FILE MD

### Mục tiêu
Gom toàn bộ output từ Phase 1 + Phase 2 thành 1 khối MD duy nhất trong working memory. Bắt buộc trước khi viết bất kỳ phần nào của kịch bản — tránh tràn context ở các phase sau.

### Không gọi skill — GEMINI tự tổng hợp theo template:

```
# CONTEXT FILE — [topic-slug] — [dd/mm/yy]

## 1. PHÂN TÍCH TIN TỨC (Phase 1)
### Bối cảnh + diễn biến
[output event-timeline-builder]
### Nguyên nhân sâu xa
[output root-cause-analyzer]
### Tác động theo nhóm
[output stakeholder-impact-mapper]
### Uy tín nguồn
[output ethos-credibility-analyzer — tóm tắt 2-3 câu]
### So sánh lịch sử
[output historical-comparator — nếu có]
### Quan điểm + phản biện
[output synthesizing-viewpoints]
### Dự báo + lời khuyên
[output forecast-synthesizer]

## 2. ANGLE (Phase 2)
### WINNER Angle
[Tên + Góc khai thác + Emotion + Hook mẫu]
### Lý do chọn
[lý do từ angle-scorer — 2-3 câu]

## 3. EXAMPLE ANALYSIS (Phase 0)
[paste nguyên `[EXAMPLE ANALYSIS]` từ Bước 2.6]
```

### ✅ Pass khi
- File MD có đủ 3 section
- Không còn output nào nằm rải rác trong conversation — tất cả đã gom vào đây
- Tổng độ dài file < 1500 từ (nếu vượt → tóm tắt bớt phần bối cảnh, giữ nguyên Angle + Example Analysis)

---

## PHASE 3: VIẾT HOOK

### Mục tiêu

Đến cuối phase này, agent phải có 1 RECOMMENDED Hook đã được kiểm tra độc lập — trước khi viết bất kỳ phần nào của body. Hook là điểm chạm đầu tiên quyết định người xem có dừng lại xem tiếp không. Mỗi hook phải bám trực tiếp vào WINNER Angle và ít nhất 1 insight tâm lý từ Phase 2.

### Nguồn — 3 thành phần bắt buộc

1. **CONTEXT FILE** từ Phase 2.5 — toàn bộ phân tích + WINNER Angle (đọc từ đây, không đọc lại từng phase cũ)
2. **[CHANNEL STRATEGY]** từ Bước 2.5 — định hướng kênh, chân dung khách hàng, tone tổng thể
3. **[FORMAT RULE]** từ Bước 2.5 — quy tắc viết hook của format được chọn
4. **[EXAMPLE ANALYSIS]** từ Bước 2.6 — cấu trúc hook, độ dài, từ đặc trưng, điều không có trong examples

> ⚠️ Hook phải nhại đúng cấu trúc hook phổ biến nhất trong `[EXAMPLE ANALYSIS]` ② trước, sau đó mới chấm SUCCESS score.
> ⚠️ Hook phải phù hợp với định hướng kênh trong `[CHANNEL STRATEGY]` — không viết hook đúng format nhưng sai tone kênh.

### Skills

**Bước 3.1** → GỌI: `[hook-writer]`
Viết 3 phiên bản hook theo 3 patterns khác nhau từ bảng bên dưới. Mỗi hook 20–50 từ (3–7 giây đọc).

**Bước 3.2** → GỌI: `[success-framework-scorer]`
Chấm điểm 3 phiên bản hook theo framework SUCCESS (Chip & Dan Heath). Đối chiếu từng hook với 6 tiêu chí, tính tổng điểm, xác nhận hoặc thay thế RECOMMENDED từ bước 3.1 dựa trên điểm số. Chỉ chạy SAU KHI hook-writer đã trả về đủ 3 phiên bản hook.

### ✅ Pass khi

- Có đủ 3 phiên bản hook với 3 patterns KHÁC NHAU
- Mỗi hook có độ dài 20–40 từ
- Mỗi hook có lý do hiệu quả rõ ràng
- success-framework-scorer đã chạy và trả về bảng điểm SUCCESS đầy đủ cho cả 3 hooks
- FINAL RECOMMENDED được xác nhận sau khi đối chiếu SUCCESS score — có ghi rõ giữ nguyên hay thay thế và tại sao
- FINAL RECOMMENDED Hook bám vào WINNER Angle và ít nhất 1 insight tâm lý từ Phase 2

### ❌ Fail thì

- 3 hooks dùng cùng 1 pattern: Gọi lại hook-writer với yêu cầu buộc đa dạng hóa pattern
- Tất cả 3 hooks có SUCCESS score < 60%: Gọi lại hook-writer để viết lại từ đầu — không chọn hook chất lượng thấp
- Hook không bám vào WINNER Angle: Gọi lại hook-writer với context angle rõ ràng hơn

---

## PHASE 4: VIẾT KỊCH BẢN HOÀN CHỈNH

### Mục tiêu

Đến cuối phase này, agent phải có 1 kịch bản hoàn chỉnh bao gồm: Title + Hook + Body + CTA + Caption & Hashtag. Kịch bản phải đọc như người thật nói — không có dấu hiệu AI viết và nằm trong giới hạn 200-350 từ.

### Nguồn — 3 thành phần bắt buộc

1. **CONTEXT FILE** từ Phase 2.5 — nguồn dữ kiện duy nhất, không đọc lại phase cũ
2. **[CHANNEL STRATEGY]** từ Bước 2.5 — định hướng kênh, chân dung khách hàng, tone tổng thể
3. **[FORMAT RULE]** từ Bước 2.5 — quy tắc cấu trúc body, CTA, title của format
4. **[EXAMPLE SCRIPTS] + [EXAMPLE ANALYSIS]** từ Bước 2.5/2.6 — nhại cấu trúc, độ dài, từ đặc trưng; tránh pattern trong ④ "Điều KHÔNG có"

> ⚠️ Trước khi gọi bất kỳ skill nào: đọc `[EXAMPLE ANALYSIS]` ①②③④⑤⑥ — dùng làm constraint cho toàn bộ phase này.
> - ⑤ Cách câu kết nối: **mỗi câu phải là phản ứng cảm xúc tự nhiên với câu trước** — không liệt kê thông tin độc lập
> - ⑥ Hành trình cảm xúc: **viết theo cung bậc cảm xúc từ examples** — không viết theo checklist cấu trúc

### Skills — thực hiện theo thứ tự

**Bước 4.1** → GỌI: `[body-writer]`
Viết body 120-250 từ theo cung bậc cảm xúc: Context → Mechanism → Impact → Insight. Input chính: RECOMMENDED Hook + toàn bộ phân tích Phase 1 + WINNER Angle.

**Bước 4.2** → GỌI: `[cta-writer]`
Viết CTA 20-40 từ gồm: Restate insight + Discussion question + Soft CTA. Input chính: Body + WINNER Angle.

**Bước 4.3** → GỌI: `[title-writer]`
Viết 3 phiên bản tiêu đề video (8-14 từ), chọn 1 RECOMMENDED. Input chính: Hook + Body + CTA.

**Bước 4.4** → GỌI: `[caption-hashtag-writer]`
Viết caption (30-50 từ) + 3-5 hashtag phân tầng. Input chính: Toàn bộ kịch bản đã có + Channel Profile.

**Bước 4.5** → GỌI: `[human-voice-writer]`
Biến đổi toàn bộ kịch bản (Hook + Body + CTA) thành ngôn ngữ nói tự nhiên — người xem nghe lên phải cảm thấy đây là người thật đang nói chuyện với mình, không phải AI đang đọc bài.

### ✅ Pass khi

- Kịch bản có đủ 5 phần: Hook, Body, CTA, Title, Caption + Hashtag
- Tổng từ số kịch bản chính (Hook + Body + CTA): 200-350 từ
- human-tone-injector đã chạy và báo cáo "Human Score ≥ 90/100"
- Caption có 3-5 hashtag đúng format TikTok (# không có dấu cách)

### ❌ Fail thì

- Nếu từ số < 200 từ: Gọi lại body-writer với yêu cầu mở rộng phần Mechanism
- Nếu từ số > 350 từ: Gọi lại body-writer với yêu cầu tinh gọn lại kịch bản
- Nếu thiếu 1 trong 5 phần Hook, Body, CTA, Title, Caption + Hashtag: Cần bổ sung ngay phần thiếu, gọi lại kỹ năng để viết phần đó

---

## PHASE 5: VERIFY + QA GATE + SHIP

### Mục tiêu

Kiểm tra toàn bộ kịch bản trước khi ship. Đây là cổng kiểm soát chất lượng cuối cùng — agent KHÔNG được ship khi còn bất kỳ flag nào chưa được giải quyết.

### Nguồn

- Kịch bản hoàn chỉnh từ Phase 4 (Hook + Body + CTA + Title + Caption + Hashtag)
- Channel Profile
- TikTok Community Guidelines (VN) — bộ từ cấm + chính sách nội dung, quy định của nền tảng TikTok
- Human Authenticity Rubric

### Skills

→ GỌI: `[tiktok-policy-scanner]`
Quét toàn bộ kịch bản tìm từ cấm + vi phạm chính sách TikTok VN. Output: Danh sách flags (nếu có) + đề xuất thay thế.

→ GỌI: `[channel-fit-validator]`
Đánh giá kịch bản có khớp chân dung kênh không: tone, pronoun, niche, audience level. Output: Fit Score /100 + danh sách điểm lệch (nếu có).

→ GỌI: `[human-authenticity-scorer]`
Chấm điểm tính người lần cuối sau tất cả chỉnh sửa. Output: Authenticity Score /100 + danh sách câu/cụm từ cần sửa (nếu có).

→ **[SIMILARITY SCORE]** — Không cần gọi skill, GEMINI tự chấm dựa trên `[EXAMPLE ANALYSIS]`:

```
SIMILARITY SCORE
① Cấu trúc   : [X/10] — hook/body/CTA có khớp pattern phổ biến ở [EXAMPLE ANALYSIS]② không?
② Độ dài      : [X/10] — tổng từ số có nằm trong ±20% so với độ dài trung bình examples?
③ Từ đặc trưng: [X/10] — có dùng ≥3 cụm từ từ [EXAMPLE ANALYSIS]③? Liệt kê các cụm đã dùng.
④ Không có    : [X/10] — có còn pattern nào trong [EXAMPLE ANALYSIS]④ sót lại không?
⑤ Kết nối câu : [X/10] — mỗi câu trong body có phải là phản ứng cảm xúc với câu trước không, hay đang liệt kê thông tin độc lập?
⑥ Cảm xúc arc : [X/10] — hành trình cảm xúc có khớp với [EXAMPLE ANALYSIS]⑥ không?

TỔNG: [X/60] = [X%]
→ ≥ 75%: PASS  |  < 75%: ghi rõ tiêu chí nào thấp nhất → sửa đúng chỗ đó → chạy lại similarity score
```

### 4C Check

#### Correctness — Tính chính xác

- Tất cả con số, tên người, tên tổ chức trong kịch bản khớp với nguồn gốc
- Không có câu nào mang nghĩa ngược với dữ liệu phân tích Phase 1
- `[ETHOS ANALYSIS]` đã được phản ánh trong cách kịch bản dẫn nguồn (không đề cao nguồn có uy tín thấp)
- Không tuyên bố là sự thật tuyệt đối những gì chỉ là dự báo

#### Completeness — Tính đầy đủ

- Kịch bản có đủ Title + Hook + Body + CTA (không thiếu phần nào)
- Title 8-14 từ
- Caption có đủ hashtag (3-5 tags)
- CTA có câu hỏi thảo luận kích thích comment

#### Context-fit — Phù hợp ngữ cảnh

- Channel Fit Score ≥ 80/100
- Ngôn ngữ, cách viết khớp đặc thù kênh (em/anh chị hoặc theo style guide kênh)
- Không dùng từ ngữ quá học thuật/hàn lâm không phù hợp với audience của kênh
- Angle được chọn phù hợp với thời điểm đăng (không quá muộn so với news cycle)
- Đúng platform? (TikTok vs Facebook vs YouTube)
- Đúng loại content? (news vs casestudy vs QC)
- Đúng audience? (người vay / đầu tư / tài chính cá nhân)

#### Consequence — Hậu quả nếu ship ngay

- Không có flag nào từ tiktok-policy-scanner (0 flags = safe to ship)
- Không có khẳng định có thể gây hiểu lầm pháp lý (tư vấn tài chính/pháp lý trực tiếp)
- Không xúc phạm cá nhân/tổ chức cụ thể dù gián tiếp
- Human Authenticity Score ≥ 90/100

### Gate Rule

| Kiểm tra | Điều kiện Pass |
|---|---|
| tiktok-policy-scanner | 0 flags → ✅ |
| channel-fit-validator | Fit Score ≥ 80 → ✅ |
| human-authenticity-scorer | Score ≥ 90 → ✅ |
| similarity-score | Tổng ≥ 75% → ✅ |

- **ALL 4 PASS → SHIP**
- **1+ FAIL → Fix đúng điểm fail → Chạy lại CHỈ check đó → Verify lại**

### Output

- **File:** `[YYYY-MM-DD]_[topic-slug]_script.md`
- **Lưu:** `/scripts/published/` hoặc vault của kênh
- **Feed vault:** Có — sau khi ship, tách insights/angles thành công vào `01-Atomic/Insights/` để train cho các bài sau

---

## EVOLUTION NOTES

### Lỗi thường gặp khi chạy workflow này

| Lỗi | Cách tránh |
|---|---|
| Bỏ qua ethos-credibility-analyzer | Dẫn đến kịch bản vô tình khuếch đại nguồn tin kém uy tín → Bắt buộc, không optional |
| Angle-generator sinh 5 angles cùng emotion FOMO | Trong prompt angle-generator nhắc rõ "5 emotions phải khác nhau" |
| Body quá dài do analogy phức tạp | body-writer có hard limit 200 từ, analogy tối đa 3 câu |
| Human-tone-injector chạy quá sớm (trước khi có đủ Hook+Body+CTA) | Chỉ được gọi sau khi đã có đủ 3 phần |
| Caption trùng với Hook video | caption-hashtag-writer được nhắc "caption phải BỔ SUNG, không lặp lại hook" |
| Angle winner là angle an toàn nhất, không phải tốt nhất | angle-scorer không được chọn angle có Risk Score cao để trừ điểm nhiều nhất — phải cân bằng |

### Cải tiến gần nhất

- **v1.0:** Workflow cơ bản 3 phase (phân tích, viết, check)
- **v1.1:** Bổ sung ethos-credibility-analyzer theo yêu cầu sếp — phân tích uy tín nguồn phát ngôn
- **v1.2:** Bổ sung human-tone-injector và human-authenticity-scorer theo yêu cầu sếp — đảm bảo tính người
- **v1.3:** Tách angle-scorer thành skill riêng (trước kia gộp với angle-generator) — giúp có bảng điểm minh bạch hơn
