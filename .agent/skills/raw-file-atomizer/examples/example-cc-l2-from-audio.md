# Example: Audio Workshop → CC / L2-KienThucNghe

> Minh hoạ xử lý file audio ghi âm workshop về kỹ thuật viết content.

---

## Input

**Loại:** Audio (.m4a)
**Nội dung:** Ghi âm buổi workshop nội bộ, trainer chia sẻ kỹ thuật viết hook "câu hỏi đảo ngược" — bắt đầu bằng kết luận gây bất ngờ, rồi kéo người xem muốn biết tại sao.

---

## Phase 0: EXTRACT

**0A — Transcribe:** Transcript đầy đủ từ audio (có đoạn [INAUDIBLE: ~3 giây] do tiếng ồn)

**0B — Làm sạch:**
- Loại bỏ: "ừm", "à", "thì là", lặp từ
- Giữ lại: các ví dụ cụ thể, con số A/B test nếu có
- Fix: transcript ghi `"câu hỏi đảo ngược"` → đảm bảo dấu tiếng Việt đúng

```
SOURCE_TYPE : audio
SUMMARY     : Workshop về kỹ thuật hook "câu hỏi đảo ngược" — bắt đầu bằng kết
              luận bất ngờ (e.g. "Ngân hàng KHÔNG muốn bạn biết điều này") sau đó
              giải thích từng bước để kéo viewer tò mò. Trainer demo 3 ví dụ và
              phân tích tại sao kỹ thuật này hoạt động về mặt tâm lý.
INTENT      : Hướng dẫn kỹ thuật viết hook câu hỏi đảo ngược với 3 ví dụ cụ thể
              và lý giải tâm lý. Hữu ích cho CC vì là kỹ năng viết thực chiến
              có thể áp dụng ngay vào script TikTok.
MULTI_NOTE  : NO
```

---

## Phase 1: BRANCH MATCH

| Nhánh | Ownership Test | Kết quả |
|---|---|---|
| CC | "Giúp VIẾT NỘI DUNG TỐT HƠN?" | **YES** — dạy kỹ thuật viết hook cụ thể |
| LS | "Giúp xử lý hồ sơ vay?" | NO |
| TD | "Mô tả thế giới bên ngoài?" | NO |

**→ Nhánh: CC**

---

## Phase 2: TYPE MATCH

| Type | Ownership Test | Kết quả |
|---|---|---|
| L1-Framework | "Giải thích nguyên lý nền?" | PARTIAL — có phần lý giải tâm lý |
| L2-KienThucNghe | "Chỉ tôi làm được một thứ ngay sau khi đọc?" | **YES** — có 3 ví dụ áp dụng ngay |
| L3 | "Là rule/constraint bắt buộc?" | NO |
| L4 | "Là retrospective?" | NO |

**→ Type: L2-KienThucNghe**
**Lý do:** L1 chủ yếu là "tại sao"; L2 là "cách làm có thể áp dụng ngay" — audio này có cả 2 nhưng phần "cách làm" chiếm ưu thế với 3 ví dụ cụ thể.

---

## Phase 7: PROPOSE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 ĐỀ XUẤT ATOMIZE — workshop-hook-dao-nguoc-2026-05-18.m4a
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTENT     : Kỹ thuật hook câu hỏi đảo ngược — bắt đầu bằng kết luận bất ngờ,
             kéo viewer tò mò. Có 3 ví dụ + lý giải tâm lý. Áp dụng ngay.
Source type: audio

PHÂN LOẠI:
  Nhánh    : CC
  Lý do    : "Giúp viết nội dung tốt hơn" → YES
  Type     : L2-KienThucNghe
  Lý do    : "Chỉ tôi làm được một thứ ngay" → YES (3 ví dụ áp dụng được ngay)

ĐẦU RA:
  Path     : CC-ContentCreator/CC-01-Atomic/L2-KienThucNghe/
  Tên file : 2026-05-18-hook-cau-hoi-dao-nguoc.md
  Template : _template-concept-writing.md

CONFLICT:
  Tình huống : NEW

MOC CẦN CẬP NHẬT:
  1. CC-ContentCreator/CC-MOC/CC-L2-MOC.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Xác nhận? (yes / chỉnh sửa [field] / skip)
```

---

## Phase 8: MD Conversion từ Transcript

**Input (transcript):**
```
...ừm, kỹ thuật này gọi là câu hỏi đảo ngược, tức là thay vì hỏi
"bạn có biết lãi suất đang giảm không?" thì mình bắt đầu bằng câu
"ngân hàng không muốn bạn biết điều này"...
```

**Output STRUCTURED_MD:**
```markdown
## Kỹ Thuật Hook "Câu Hỏi Đảo Ngược"

### Định Nghĩa
Thay vì đặt câu hỏi thông thường → bắt đầu bằng kết luận gây bất ngờ,
khiến viewer tò mò muốn biết tại sao.

### Cấu Trúc
1. **Câu mở:** Kết luận bất ngờ / gây tranh cãi
2. **Câu bridge:** "Và đây là lý do..."
3. **Câu kéo:** Hint về nội dung sắp giải thích

### 3 Ví Dụ Áp Dụng Ngay
...
```

**YAML:**
```yaml
---
name: hook-cau-hoi-dao-nguoc
type: concept
subtype: writing-technique
topics: ["hook", "content", "TikTok", "writing"]
status: raw
created: 2026-05-18
source: "workshop-hook-dao-nguoc-2026-05-18.m4a"
confidence: medium
verified: false
related: ["[[CC-L2-MOC]]"]
maturity: seed
review_interval: 30
next_review: 2026-06-17
reuse_count: 0
evolution_log: []
---
```
