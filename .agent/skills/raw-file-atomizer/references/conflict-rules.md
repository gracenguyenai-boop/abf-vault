# Conflict Rules — Xử Lý Trùng Lặp

> Dùng cho Phase 5: CONFLICT CHECK.
> Sau khi phân loại xong, tìm xem vault đã có note nào gần giống chưa.

---

## Quy trình tìm kiếm

1. Lấy 3-5 từ khoá cốt lõi từ INTENT (Phase 0)
2. Search vault theo từ khoá → lấy top 5 kết quả gần nhất
3. Đọc YAML (name, type, topics) + phần mở đầu của từng kết quả
4. So sánh INTENT của file mới với INTENT của note hiện có
5. Phân loại theo bảng bên dưới

---

## 5 Tình huống

### NEW — Tạo mới
**Điều kiện:** Không có note nào trong vault có INTENT gần giống.
**Hành động:** Tạo file .md mới theo template đúng.
**Trong Phase 7:** Ghi `CONFLICT: NEW`

---

### ENRICH — Bổ sung vào note cũ
**Điều kiện:** Có note cùng chủ đề nhưng file mới bổ sung:
- Dữ liệu/số liệu mới hơn (cùng topic, khác thời điểm)
- Góc nhìn mới không có trong note gốc
- Case thực tế mới minh hoạ cho concept đã có

**Hành động:**
1. Không tạo file mới
2. Thêm section mới vào cuối note hiện có:
```markdown
## [Nguồn bổ sung] — [YYYY-MM-DD]
> Nguồn: [tên file gốc]

[nội dung bổ sung]
```
3. Cập nhật YAML:
   - `reuse_count: +1`
   - Append vào `evolution_log`:
     ```yaml
     evolution_log:
       - date: YYYY-MM-DD
         change: "Bổ sung từ [tên file nguồn]: [mô tả ngắn]"
     ```
4. **KHÔNG** thay đổi hoặc overwrite phần nội dung gốc
5. **KHÔNG** thêm entry mới vào T2 Sub-MOC — không tạo file mới thì không có MOC entry mới

**Trong Phase 7:** Ghi `CONFLICT: ENRICH | Note hiện có: [[path]]`
**Trong Phase 10:** CHỈ cập nhật YAML note hiện có (reuse_count + evolution_log). KHÔNG thêm MOC entry.

---

### DUPLICATE — Trùng lặp
**Điều kiện:** Có note gần như giống hệt:
- Cùng INTENT (cùng chủ đề + cùng góc nhìn)
- Cùng type

**Hành động mặc định:** Đề xuất SKIP (không tạo gì thêm).
**Nếu muốn REPLACE:** User phải nói rõ "replace" hoặc "ghi đè" → mới được overwrite.

**Trong Phase 7:** Ghi `CONFLICT: DUPLICATE | Note hiện có: [[path]] — Đề xuất SKIP`

---

### SPLIT — Tách thành nhiều note
**Điều kiện:** File raw chứa ≥2 INTENT khác nhau cần tách:
- Chủ đề A và chủ đề B không liên quan đủ chặt để làm 1 atomic note
- Mỗi chủ đề có thể thuộc nhánh/type khác nhau

**Hành động:**
1. Tách thành N note riêng biệt
2. Đề xuất TẤT CẢ N note trong Phase 7 cùng 1 lần (không execute từng cái)
3. Mỗi note có YAML `related` link đến các note còn lại trong bộ:
   ```yaml
   related: ["[[path/note-A]]", "[[path/note-B]]"]
   ```
4. Execute từng note SAU KHI user approve toàn bộ proposal

**Trong Phase 7:**
```
CONFLICT: SPLIT — file này chứa [N] INTENT khác nhau
Note 1: [path/tên] — [INTENT 1]
Note 2: [path/tên] — [INTENT 2]
...
```

---

### UNCLEAR — Không đủ cơ sở
**Điều kiện:** Không đủ thông tin để phán đoán mức độ tương đồng.
**Hành động:** HỎI USER, không tự quyết.

---

## Bảng quyết định nhanh

| Câu hỏi | YES | NO |
|---|---|---|
| Vault có note cùng INTENT + cùng type? | DUPLICATE | → tiếp |
| Vault có note cùng chủ đề, file mới có dữ liệu/góc nhìn MỚI? | ENRICH | → tiếp |
| File raw chứa nhiều INTENT khác nhau? | SPLIT | NEW |

---

## Lưu ý quan trọng

- ENRICH: Phải đọc note gốc trước để đảm bảo nội dung bổ sung thực sự mới, không lặp lại
- DUPLICATE: Không xóa file raw gốc; chỉ báo user và SKIP
- SPLIT: Proposal phải liệt kê đầy đủ tất cả note trước khi execute bất kỳ cái nào
- REPLACE chỉ được thực hiện khi user explicit approve — không suy diễn
