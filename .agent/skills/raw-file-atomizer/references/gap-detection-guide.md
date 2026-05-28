# Gap Detection Guide — Phát Hiện & Xử Lý Content Không Khớp

> Dùng cho Phase 6: GAP DETECT.
> Trigger khi Phase 2 không có type nào có Ownership Test = YES rõ ràng.

---

## 3 Loại Gap

### Loại 1: Type Mismatch
**Mô tả:** Content hợp nhánh nhưng không khớp với bất kỳ type nào trong nhánh đó.
**Dấu hiệu:** Ownership Test của tất cả types trong nhánh đều là PARTIAL hoặc NO.

**Output Phase 6:**
```
⚠️ GAP DETECTED — Type mismatch
Nhánh xác định : [CC/LS/TD/Shared/VJ]
Vấn đề         : Content phù hợp với nhánh [X] nhưng không khớp rõ với type nào
Type gần nhất  : [type] — thiếu [điều kiện X cụ thể]
Đề xuất:
  A: Ép vào [type gần nhất] — trade-off: [mô tả mất gì]
  B: Tạo sub-type "[tên đề xuất]" dưới [nhánh/lớp]/
  C: Tách thành [type A] + [type B]
→ Chờ user chọn A / B / C
```

---

### Loại 2: Branch Mismatch
**Mô tả:** Content không rõ thuộc nhánh nào — nhiều nhánh đều có thể.
**Dấu hiệu:** Nhiều nhánh có Ownership Test = PARTIAL nhưng không có nhánh nào = YES rõ ràng.

**Output Phase 6:**
```
⚠️ GAP DETECTED — Branch mismatch
Vấn đề         : Content có thể thuộc [nhánh A] hoặc [nhánh B]
Lý do ambiguous: [giải thích cụ thể]
Đề xuất:
  A: Lưu vào [nhánh A]-00-Inbox/ tạm với tag needs-classification
  B: HỎI USER — bạn muốn đặt content này về nhánh nào?
→ Chờ user xác nhận
```

---

### Loại 3: Novel Content
**Mô tả:** Lĩnh vực hoàn toàn mới, không có tiền lệ trong vault hiện tại.
**Dấu hiệu:** Không có nhánh nào có JD phù hợp. Content thuộc domain chưa được cover.

**Output Phase 6:**
```
⚠️ GAP DETECTED — Novel content (lĩnh vực mới)
Vấn đề    : Content này không thuộc domain nào trong vault hiện tại
Mô tả     : [mô tả lĩnh vực mới]
Đề xuất:
  A: Tạo thư mục mới [tên đề xuất]/ dưới [nhánh phù hợp nhất]
  B: Lưu vào Shared/Shared-00-Inbox/ tạm, chờ quyết định cấu trúc
→ Chờ user approve trước khi tạo cấu trúc mới
```

---

## Cách xử lý sau khi user chọn

### Nếu chọn A (ép vào type gần nhất)
- Tiến hành như bình thường từ Phase 7
- Ghi chú trong YAML: `subtype: [type gần nhất] — adapted`
- Ghi vào `MEMORY/decisions.md`: "[ngày] — Quyết định ép [content] vào [type] vì [lý do]"

### Nếu chọn B (tạo sub-type hoặc nhánh mới)
- Tạo folder mới nếu cần
- Tạo template mới (draft minimal template) — phải có user approve
- Cập nhật `VAULT-STRUCTURE-REF.md` để phản ánh cấu trúc mới
- Cập nhật `MOC-MASTER.md` nếu thêm nhánh mới

### Nếu chọn C (tách thành nhiều type)
- Chuyển sang xử lý SPLIT (xem @references/conflict-rules.md)
- Đề xuất cả 2 note trong Phase 7

---

## Ví dụ thực tế

| Tình huống | Loại gap | Xử lý thích hợp |
|---|---|---|
| Bài phân tích lãi suất + tác động BĐS (2 chủ đề) | Type Mismatch (TD/L3) hoặc SPLIT | Đề xuất C: tách TD/L3/TC + TD/L3/BDS |
| Ghi âm họp team nội bộ về chiến lược content | Branch Mismatch (CC vs VJ) | Hỏi user: đây là kiến thức chung (CC) hay gắn kênh cụ thể (VJ)? |
| Bài học về tâm lý học hành vi của người vay | Novel content | Đề xuất: Shared/concept hoặc tạo sub-type "psychology" dưới LS/L2 |
| Script workshop về cách đọc CIC cho cả team | Branch Mismatch (CC vs LS) | Ownership Test: giúp viết content hay xử lý hồ sơ? → thường là LS/L2 |
