# Example: Link Báo → TD / L3 / TC

> Minh hoạ toàn bộ 10 phases khi xử lý một link bài báo về chính sách tiền tệ.

---

## Input

**Loại:** Link bài báo
**Nguồn:** vnexpress.net/nhnn-giam-lai-suat-dieu-hanh-lan-thu-3-2026-05-15.html
**User nói:** "atomize cái này"

---

## Phase 0: EXTRACT

```
SOURCE_TYPE : link
SUMMARY     : NHNN giảm lãi suất tái cấp vốn từ 4.5% xuống 4% và lãi suất chiết
              khấu từ 2.5% xuống 2%, hiệu lực từ 16/5/2026. Đây là lần giảm thứ
              3 trong năm 2026, nhằm kích thích tăng trưởng tín dụng và hỗ trợ
              doanh nghiệp phục hồi sau giai đoạn lãi suất cao.
INTENT      : Tường thuật quyết định điều chỉnh lãi suất điều hành của NHNN
              tháng 5/2026. Hữu ích cho TD vì cung cấp bối cảnh vĩ mô về môi
              trường lãi suất ảnh hưởng trực tiếp đến quyết định vay của khách.
MULTI_NOTE  : NO
```

---

## Phase 1: BRANCH MATCH

| Nhánh | Ownership Test | Kết quả |
|---|---|---|
| CC | "Giúp viết content tốt hơn?" | NO — đây là thông tin thị trường |
| LS | "Giúp xử lý hồ sơ vay cụ thể?" | PARTIAL — liên quan nhưng không phải hồ sơ |
| TD | "Mô tả thế giới bên ngoài ảnh hưởng đến quyết định vay?" | **YES** |
| Shared | "Cả CC + LS + TD đều thiếu nếu xóa?" | NO — chủ yếu cho TD |
| VJ | "Chỉ có ý nghĩa khi gắn kênh cụ thể?" | NO |

**→ Nhánh: TD**
**Lý do:** TD Ownership Test = YES rõ ràng. LS = PARTIAL nhưng TD Exclusion Rule không loại trừ content này.

---

## Phase 2: TYPE MATCH

| Type | Ownership Test | Kết quả |
|---|---|---|
| L1-Framework | "Là công cụ phân tích tổng quát?" | NO — là sự kiện cụ thể |
| L2-KienThucNghe | "Trả lời 'X là gì' ở cấp khái niệm?" | NO — là tin tức, không phải định nghĩa |
| L3-KienThucDacThu | "Là sự kiện/tin tức/phân tích cụ thể?" | **YES** |
| L4-PDCA | "Là insight rút ra từ quá trình làm TD?" | NO |

**→ Type: L3-KienThucDacThu**

---

## Phase 3: DOMAIN

| Domain | Ownership Test | Kết quả |
|---|---|---|
| BDS | "Gắn chính với nhà đất?" | NO |
| CK | "Gắn chính với cổ phiếu?" | NO |
| TC | "Gắn chính với lãi suất, NHNN, tín dụng?" | **YES** |
| CS | "Gắn chính với luật, nghị định?" | NO — đây là quyết định tiền tệ, không phải văn bản pháp lý |

**→ Domain: TC**

---

## Phase 5: CONFLICT CHECK

Search: "lãi suất điều hành NHNN 2026" → 0 kết quả trùng INTENT.
**→ Tình huống: NEW**

---

## Phase 7: PROPOSE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 ĐỀ XUẤT ATOMIZE — vnexpress-nhnn-giam-lai-suat-may-2026.link
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTENT     : Tường thuật quyết định giảm lãi suất điều hành của NHNN tháng
             5/2026 (lần 3 trong năm). Hữu ích cho TD vì bối cảnh vĩ mô về
             môi trường lãi suất ảnh hưởng trực tiếp đến quyết định vay.
Source type: link

PHÂN LOẠI:
  Nhánh    : TD
  Lý do    : "Mô tả THẾ GIỚI BÊN NGOÀI ảnh hưởng đến quyết định vay" → YES
  Type     : L3-KienThucDacThu
  Lý do    : "Sự kiện cụ thể (không phải khái niệm tổng quát)" → YES
  Domain   : TC — lãi suất + NHNN + tín dụng

ĐẦU RA:
  Path     : TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/TC/
  Tên file : 2026-05-15-nhnn-giam-lai-suat-dieu-hanh-lan-3.md
  Template : TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/_template-domain-macro.md

CONFLICT:
  Tình huống : NEW
  Note liên quan: —

GAP: Không có

MOC CẦN CẬP NHẬT:
  1. TD-TraDa/TD-MOC/TD-L3-TC-MOC.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Xác nhận? (yes / chỉnh sửa [field] / skip)
```

---

## Phase 9: OUTPUT FILE

**File tạo ra:** `TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/TC/2026-05-15-nhnn-giam-lai-suat-dieu-hanh-lan-3.md`

```yaml
---
name: nhnn-giam-lai-suat-dieu-hanh-lan-3-2026-05
type: insight
subtype: TC
topics: ["lãi suất", "NHNN", "tín dụng", "vĩ mô"]
status: raw
created: 2026-05-15
source: "vnexpress.net/nhnn-giam-lai-suat-dieu-hanh-lan-thu-3"
confidence: high
verified: false
related: ["[[TD-L3-TC-MOC]]"]
maturity: seed
review_interval: 14
next_review: 2026-05-29
reuse_count: 0
evolution_log: []
---
```
