---
name: ops-luong-trinh-phe-duyet-vpbank
type: framework
subtype: process
topics: ["luong-trinh", "phe-duyet", "cpc-uw", "vpbank", "digital"]
status: raw
created: 2026-05-23
source: "Học nghiệp vụ — PDF VPBank"
inbox_ref: "[[LS-LoanSpecialist/LS-00-Inbox/2026-05-23-raw-hoc-nghiep-vu-vpbank]]"
confidence: high
verified: true
related: ["[[LS-L3-MOC]]"]
maturity: seed
review_interval: 30
next_review: 2026-06-22
reuse_count: 0
evolution_log: []
---

# Luồng Trình Phê Duyệt Hồ Sơ VPBank

## Mục Đích
> Xác định đúng luồng trình cho từng hồ sơ (Digital / Luồng A / Luồng B) và chính sách theo Good/Normal/Bad Branch để tránh trình sai, mất thời gian.

---

## 3 Luồng Chính

| Luồng | Tên | Điều kiện |
|---|---|---|
| **Digital Thế chấp** | Phê duyệt tự động | Khoản vay thỏa SP từng thời kỳ (theo bảng Digital) |
| **Luồng A — CPC UW** | Qua thẩm định tập trung | Chuẩn lệ: ≤20 tỷ/khoản vay hoặc tổng dư nợ KH ≤20 tỷ. Ngoại lệ: ≤8 tỷ và tổng dư nợ ≤20 tỷ |
| **Luồng B — Tái thẩm định** | Thẩm định lại | Chuẩn lệ >20 tỷ. Ngoại lệ: khoản vay >8 tỷ hoặc ≤8 tỷ có NL nhưng CPC UW Luồng A từ chối |

---

## Bảng Chính Sách Theo Branch

| Chính sách / Luồng | Good Branch | Normal Branch | Bad Branch |
|---|---|---|---|
| 1 — Phê duyệt nhanh (XN trưởng ĐV) | ✅ | ✅ | ✅ |
| 2 — Trưởng ĐV tốt xác nhận nguồn thu | ✅ | | |
| 3 — Thẩm định điện thoại/thực địa (≤4 tỷ) | ✅ | ✅ | |
| 4 — Chứng minh tài chính | ✅ | ✅ | ✅ |
| 5 — Luận thu nhập / Tài sản tích lũy | ✅ | ✅ | ✅ |

**Lưu ý:**
- Khoản vay HKD **không** được trình Luồng 5
- Bad Branch + ĐVKD trình KH vay >600 triệu theo Luồng 4 & 5 → yêu cầu thực địa

---

## Thẩm Quyền Xác Nhận ĐCBG (Đối Chiếu Bản Gốc)

| Giá trị khoản vay | Thẩm quyền |
|---|---|
| ≤ 3 tỷ | CBBH đối chiếu bản gốc trên giấy tờ xác minh TSTL |
| ≤ 5 tỷ | Trưởng phòng KD đối chiếu |
| ≤ 10 tỷ | GĐ trung tâm thế chấp / GĐ ĐVKD / GĐMAF / GĐKV |
| > 10 tỷ | GĐ Vùng ký đối chiếu hoặc sao y chứng thực từ cơ quan có thẩm quyền |
| Tại giải ngân | CSR đối chiếu bản gốc tại bước giải ngân |

---

## Điểm Hay Bị Bỏ Qua
> - TSTL đang thế chấp/cầm cố tại TCTD: chấp nhận sao y đối chiếu/văn bản xác nhận TCTD trong vòng 30 ngày
> - KH đã sang tên số đỏ nhưng vẫn dùng số đỏ cũ → cần cập nhật số đỏ mới
> - Khoản vay HKD: không trình Luồng 5 (luận thu nhập)

## Áp Dụng Cho Loại Vay
- [x] Mua nhà
- [x] Kinh doanh
- [x] Tái cấp vốn
- [x] Khác: Tất cả hồ sơ thế chấp VPBank

## Nguồn / Người Dạy
> Tài liệu đào tạo nội bộ VPBank — Các phân luồng trình phê duyệt KHCN tại VPBank

## Liên Kết
- [[2026-05-23-danh-muc-ngoai-le-vpbank]]
- [[2026-05-23-checklist-ho-so-vpbank]]


← [[LS-L3-MOC]]