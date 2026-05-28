# Example: File Nhiều Chủ Đề → SPLIT → 2 Notes

> Minh hoạ khi 1 file raw chứa 2 INTENT khác nhau cần tách.

---

## Input

**Loại:** Text (ghi chú buổi họp team)
**Nội dung:** File ghi chú buổi họp hàng tuần — nửa đầu bàn về hook pattern mới cho TikTok, nửa sau tổng hợp diễn biến lãi suất ngân hàng thương mại tháng 5.

---

## Phase 0: EXTRACT

```
SOURCE_TYPE : text
SUMMARY     : Ghi chú 2 chủ đề: (1) Kỹ thuật viết hook câu hỏi cho TikTok tài
              chính — 3 pattern hiệu quả nhất dựa trên test A/B. (2) Tổng hợp
              diễn biến lãi suất cho vay các ngân hàng thương mại tháng 5/2026,
              xu hướng giảm theo sau quyết định của NHNN.
INTENT      : [2 INTENT khác nhau]
  INTENT-A: Chia sẻ 3 pattern viết hook câu hỏi đã được test A/B, có kết quả.
            Hữu ích cho CC vì là kỹ năng viết thực chiến có thể áp dụng ngay.
  INTENT-B: Tổng hợp lãi suất cho vay ngân hàng thương mại tháng 5/2026.
            Hữu ích cho TD vì là dữ liệu thị trường bối cảnh vĩ mô.
MULTI_NOTE  : YES — 2 INTENT khác nhau, thuộc 2 nhánh khác nhau
```

---

## Phase 5: CONFLICT CHECK → SPLIT

Cả 2 INTENT đều là NEW trong vault.
→ Tình huống: SPLIT — tạo 2 note riêng

---

## Phase 7: PROPOSE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 ĐỀ XUẤT ATOMIZE — hop-team-2026-05-20.txt
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFLICT: SPLIT — file này chứa 2 INTENT khác nhau

NOTE 1:
  INTENT  : 3 pattern viết hook câu hỏi đã test A/B, có kết quả.
            Hữu ích cho CC vì kỹ năng viết thực chiến áp dụng ngay.
  Nhánh   : CC | Type: L2-KienThucNghe
  Lý do   : "Chỉ tôi làm được một thứ ngay sau khi đọc" → YES
  Path    : CC-ContentCreator/CC-01-Atomic/L2-KienThucNghe/
  Tên file: 2026-05-20-hook-cau-hoi-3-pattern-ab-test.md
  Template: _template-concept-writing.md

NOTE 2:
  INTENT  : Lãi suất cho vay NH thương mại tháng 5/2026 giảm theo NHNN.
            Hữu ích cho TD vì dữ liệu thị trường bối cảnh vĩ mô.
  Nhánh   : TD | Type: L3-KienThucDacThu | Domain: TC
  Lý do   : "Sự kiện/dữ liệu thị trường cụ thể" → YES
  Path    : TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/TC/
  Tên file: 2026-05-20-lai-suat-ngan-hang-thuong-mai-t5-2026.md
  Template: _template-domain-macro.md

MOC CẦN CẬP NHẬT:
  1. CC-ContentCreator/CC-MOC/CC-L2-MOC.md
  2. TD-TraDa/TD-MOC/TD-L3-TC-MOC.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Xác nhận? (yes / chỉnh sửa [field] / skip)
```

---

## Lưu ý sau khi execute

- Mỗi note có `related` link đến note kia trong YAML:
  - Note CC: `related: ["[[CC-L2-MOC]]", "[[TD-01-Atomic/L3/TC/2026-05-20-lai-suat...]]"]`
  - Note TD: `related: ["[[TD-L3-TC-MOC]]", "[[CC-01-Atomic/L2/2026-05-20-hook-cau-hoi...]]"]`
- MOC update sau khi cả 2 note đã tạo xong — batch 1 lần
