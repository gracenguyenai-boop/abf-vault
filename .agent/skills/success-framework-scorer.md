---
name: success-framework-scorer
version: "1.0"
description: >
  Chấm điểm hook TikTok theo framework SUCCESS (Chip & Dan Heath).
  Gọi sau hook-writer. Chỉ hook đạt ≥ 4/6 mới được dùng.
applies_to: [tiktok-news-viral, tiktok-case-study, tiktok-ktvv]
updated: 2026-05-31
---

# SUCCESS Framework Scorer — TikTok Hook

> Chạy SAU hook-writer. Không chạy song song.
> Input: 3 hook từ hook-writer.
> Output: bảng điểm + RECOMMENDED hook + lý do.

---

## Rubric chấm — 6 tiêu chí (0 hoặc 1 điểm mỗi tiêu chí)

### S — Simple (Đơn giản)
**Câu hỏi:** Hook chỉ truyền tải **1 ý duy nhất** không?

| Điểm | Điều kiện |
|---|---|
| 1 | 1 ý, người nghe nhớ ngay sau 3 giây |
| 0 | Có 2 ý trở lên, hoặc cần đọc lại để hiểu |

✅ *"Lỗ 10 triệu một lượng — chỉ trong 4 tuần."* → 1 ý (mất tiền) → **1**
❌ *"Lãi suất giảm nhưng vàng tăng và BĐS đóng băng ảnh hưởng đến kế hoạch vay."* → 3 ý → **0**

---

### U — Unexpected (Bất ngờ)
**Câu hỏi:** Hook có **đảo ngược kỳ vọng** hoặc gây bất ngờ không?

| Điểm | Điều kiện |
|---|---|
| 1 | Người nghe dự đoán X, hook nói Y ngược lại — hoặc con số gây sốc |
| 0 | Thông tin dự đoán được, không gây bất ngờ |

✅ *"Ngân hàng giảm lãi — nhưng tiền bạn trả hàng tháng không giảm."* → ngược kỳ vọng → **1**
❌ *"Lãi suất ngân hàng đang thay đổi, hãy cập nhật."* → không bất ngờ → **0**

---

### C1 — Concrete (Cụ thể)
**Câu hỏi:** Có **số liệu hoặc ví dụ cụ thể** không? Không trừu tượng?

| Điểm | Điều kiện |
|---|---|
| 1 | Có con số, tên, địa điểm, hoặc ví dụ cụ thể có thể hình dung |
| 0 | Chung chung, mơ hồ, không hình dung được |

✅ *"87% người vay không biết điều này."* → con số cụ thể → **1**
✅ *"Khoản vay 2 tỷ — đang trả thừa 8 triệu mỗi tháng."* → số liệu rõ → **1**
❌ *"Nhiều người đang mắc sai lầm khi vay ngân hàng."* → mơ hồ → **0**

---

### C2 — Credible (Đáng tin)
**Câu hỏi:** Người nghe có lý do để **tin** hook này không?

| Điểm | Điều kiện |
|---|---|
| 1 | Có số liệu có nguồn gốc, tên ngân hàng, hoặc expert signal |
| 0 | Không có bằng chứng, nghe như quảng cáo |

✅ *"VPBank, BIDV đồng loạt hạ lãi — nhưng đây là điều bạn chưa biết."* → tên cụ thể → **1**
❌ *"Có cách vay ngân hàng tốt hơn mà ít người biết."* → không có bằng chứng → **0**

> ⚠️ Hook ngắn (≤10 từ) thường khó đạt C2 — chấp nhận 0 nếu body sẽ bổ sung credibility.

---

### E — Emotional (Cảm xúc)
**Câu hỏi:** Hook chạm vào **1 trong 4 cảm xúc** sau không?

| Cảm xúc | Dấu hiệu |
|---|---|
| FOMO | Sợ bỏ lỡ cơ hội, người khác đang làm mà mình không biết |
| Lo lắng | Đang mắc lỗi, đang mất tiền, nguy hiểm không biết |
| Tò mò | Bí mật, insider info, điều ít người biết |
| Phẫn nộ | Bị lừa, ngân hàng không nói thật, bất công |

| Điểm | Điều kiện |
|---|---|
| 1 | Chạm rõ ràng 1 trong 4 cảm xúc trên |
| 0 | Trung tính, không gây cảm xúc |

✅ *"Bạn đang trả thừa tiền mỗi tháng mà không biết."* → Lo lắng → **1**
✅ *"Điều ngân hàng không nói với bạn về lãi suất ưu đãi."* → Phẫn nộ + Tò mò → **1**
❌ *"Cập nhật lãi suất tháng 5."* → Trung tính → **0**

---

### S2 — Story (Câu chuyện)
**Câu hỏi:** Có **nhân vật hoặc tình huống** để người xem relate không?

| Điểm | Điều kiện |
|---|---|
| 1 | Có "ai đó" (khách, bạn, người vay) hoặc tình huống cụ thể người xem thấy mình trong đó |
| 0 | Câu phát biểu chung, không có nhân vật |

✅ *"Khách hàng tôi vay 3 tỷ — đây là cách họ làm trong 90 ngày."* → nhân vật → **1**
✅ *"Ai vay từ 2023–2024 đang trả thừa 8 triệu mỗi tháng."* → "ai" = người xem relate → **1**
❌ *"Lãi suất thả nổi đang ở mức cao."* → không có nhân vật → **0**

---

## Bảng chấm điểm

```
Hook 1: "[nội dung]"
S (Simple)     : [0/1] — [lý do 1 dòng]
U (Unexpected) : [0/1] — [lý do 1 dòng]
C1 (Concrete)  : [0/1] — [lý do 1 dòng]
C2 (Credible)  : [0/1] — [lý do 1 dòng]
E (Emotional)  : [0/1] — [lý do 1 dòng]
S2 (Story)     : [0/1] — [lý do 1 dòng]
TỔNG           : [X/6]
```

**Ngưỡng:**
- ≥ 5/6 → WINNER, dùng ngay
- 4/6 → ACCEPTABLE, dùng nếu không có hook nào ≥5
- ≤ 3/6 → FAIL → hook-writer viết lại hook này, không chọn

---

## Output bắt buộc

```
HOOK SCORING RESULTS

Hook 1: "..." → [X/6] — [S U C C E S điểm từng tiêu chí]
Hook 2: "..." → [X/6] — [S U C C E S điểm từng tiêu chí]
Hook 3: "..." → [X/6] — [S U C C E S điểm từng tiêu chí]

RECOMMENDED: Hook [số] — "[nội dung]"
Lý do: [2-3 câu — tiêu chí nào mạnh nhất, tại sao phù hợp với angle]

→ Nếu tất cả ≤ 3/6: GỌI LẠI hook-writer với yêu cầu cụ thể:
   "[tiêu chí yếu nhất] cần cải thiện — thêm [số liệu/bất ngờ/nhân vật]"
```

---

## Lỗi hay gặp khi chấm

| Lỗi | Cách tránh |
|---|---|
| Chấm U=1 cho hook chỉ có số liệu bình thường | U chỉ = 1 khi người nghe dự đoán ngược — số liệu không tự động = unexpected |
| Bỏ qua độ dài hook khi chấm | Kiểm tra ≤10 từ TRƯỚC khi chấm SUCCESS — hook dài tự động fail trước khi vào rubric |
| Chấm S2=1 vì có từ "bạn" | "Bạn" chung chung ≠ story — phải có tình huống cụ thể người xem thấy mình trong đó |
| Tất cả 3 hooks đều ≤3/6 nhưng vẫn chọn 1 | → Bắt buộc gọi lại hook-writer, không chọn hook kém |
