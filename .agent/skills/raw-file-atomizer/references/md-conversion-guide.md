# MD Conversion Guide — Chuyển Đổi File Nguồn Sang Markdown

> Dùng cho Phase 8: CONVERT TO MD.
> Từ CLEAN_TEXT (Phase 0B) → STRUCTURED_MD sẵn sàng điền vào template.

---

## Pipeline Tổng Quát (4 bước)

```
8A: Phát hiện cấu trúc nguồn
8B: Map sang Markdown syntax
8C: Chuẩn hoá cho Obsidian
8D: Validate YAML
```

---

## 8A. Phát Hiện Cấu Trúc Nguồn

Xác định các loại cấu trúc có trong text:

| Cấu trúc | Dấu hiệu nhận biết |
|---|---|
| Tiêu đề lớn | In hoa, in đậm, font lớn hơn, dòng đứng một mình |
| Tiêu đề nhỏ | Dòng in đậm/gạch dưới trước đoạn văn |
| Danh sách bullet | `•`, `-`, `*`, số thứ tự ở đầu dòng |
| Bảng | Hàng/cột với dữ liệu tương ứng |
| Trích dẫn | Trong ngoặc kép `""`, hoặc có attribution `— Tên người` |
| Đoạn văn thường | Text liền mạch, không phải list hay tiêu đề |
| Số liệu quan trọng | Con số + đơn vị, %, tỷ đồng, ngày tháng |

---

## 8B. Map Sang Markdown

| Cấu trúc nguồn | Markdown output |
|---|---|
| Tiêu đề lớn (section) | `## Tiêu đề` |
| Tiêu đề nhỏ (sub-section) | `### Tiêu đề con` |
| Danh sách không thứ tự | `- item` |
| Danh sách có thứ tự | `1. item` |
| Bảng dữ liệu | `\| Col1 \| Col2 \|` (MD table đầy đủ header) |
| Trích dẫn / quote | `> "câu trích dẫn" — Nguồn` |
| Nhấn mạnh quan trọng | `**từ hoặc cụm từ**` |
| Số liệu quan trọng | Giữ nguyên — KHÔNG in đậm (vault style) |
| Ghi chú / caveat | `> ⚠️ [ghi chú]` |

---

## 8C. Chuẩn Hoá Cho Obsidian

### Tên file
- Format: `YYYY-MM-DD-slug-title.md`
- Slug: chữ thường, thay dấu tiếng Việt bằng ký tự Latin không dấu, dùng `-` thay space
- Ví dụ: `2026-05-22-lai-suat-nhan-hang-giam.md`
- **GIỮ nguyên dấu tiếng Việt TRONG nội dung file** — chỉ bỏ dấu trong TÊN FILE

### Internal links
- Dùng `[[note-name]]` cho Obsidian wikilinks
- Dùng `[[note-name|display text]]` nếu cần text khác tên file
- KHÔNG dùng Markdown standard links `[text](path)` cho internal links

### Formatting rules
- KHÔNG dùng HTML tags (`<br>`, `<b>`, `<table>`) trong .md file
- KHÔNG có trailing spaces ở cuối dòng
- Blank line giữa các sections (không dính vào nhau)
- Headers không có dấu chấm cuối

### Vietnamese encoding
- Đảm bảo UTF-8 đầy đủ
- Các ký tự hay bị mất: ắ ặ ẳ ẵ ặ ề ệ ổ ộ ồ ờ ướ — kiểm tra sau khi convert
- Nếu có ký tự lạ (`??`, `□`, `â`) → tìm nguồn gốc và fix

---

## 8D. Validate YAML Trước Khi Lưu

### Checklist YAML
- [ ] Mở bằng `---` (dòng đầu tiên của file)
- [ ] Đóng bằng `---` (sau trường cuối cùng)
- [ ] Dùng 2 spaces indent cho nested — KHÔNG dùng tab
- [ ] String có ký tự đặc biệt (`:`, `#`, `"`, `[`) → phải trong `""`
- [ ] `topics` là list YAML: `["topic1", "topic2"]` — KHÔNG phải string
- [ ] `evolution_log` là list rỗng: `[]` nếu chưa có entry
- [ ] `related` là list: `["[[MOC-name]]"]` — phải có `[]` dù chỉ 1 phần tử

### Các lỗi YAML hay gặp

| Lỗi | Sai | Đúng |
|---|---|---|
| String có dấu `:` | `source: NHNN: Thông báo 2026` | `source: "NHNN: Thông báo 2026"` |
| topics là string | `topics: "macro, finance"` | `topics: ["macro", "finance"]` |
| related là string | `related: "[[MOC-TraDa]]"` | `related: ["[[MOC-TraDa]]"]` |
| Dùng tab | `··name: abc` (tab) | `  name: abc` (2 spaces) |
| Thiếu dấu ngoặc list | `evolution_log:` (trống) | `evolution_log: []` |

---

## Hướng Dẫn Theo Loại File Nguồn

### PDF (có text layer)
1. Extract text
2. Fix encoding: chữ dính nhau (xem Phase 0B)
3. Nhận diện heading từ font size / bold (thường không có Markdown syntax)
4. Convert đoạn văn thường → đoạn văn Markdown thông thường
5. Convert bảng từ PDF → Markdown table (có thể cần thủ công)

### PDF scan (OCR)
- Thêm `ocr: true` vào YAML
- OCR output thường có lỗi spacing → fix trước khi convert
- Chất lượng thấp → đánh dấu `[OCR - có thể có lỗi]` ở đầu note
- Section không rõ ràng → dùng `### [OCR - tiêu đề không rõ]`

### Audio transcript
- Loại bỏ: filler words (ừm, à, ờ), speaker labels không cần thiết
- Giữ lại: timestamps nếu cần reference, tên speaker nếu nhiều người
- Convert spoken language → written language (rút gọn câu, bỏ lặp)
- Đánh dấu: `[INAUDIBLE: ~X giây]` cho đoạn không nghe được

### Web article / link
- Strip HTML navigation, ads, related articles, sidebar
- Giữ: headline, byline (tác giả + ngày), body text, key quotes
- Convert inline HTML (`<strong>`, `<em>`) → Markdown equivalent
- External links → giữ nguyên URL hoặc footnote nếu quan trọng

### Plain text / paste
- Thường ít cần convert nhất
- Chủ yếu cần: nhận diện và format heading, list, quote nếu có
- Fix line breaks không cần thiết (wrap ở 80 char → ghép lại thành đoạn văn)

---

## Ví Dụ Convert

**Input (PDF extract):**
```
NHNNVN điều chỉnh lãi suất điều hành
Ngày 15/5/2026, Ngân hàng Nhà nước Việt Nam đã quyết định:
- Hạ lãi suất tái cấp vốn từ 4,5% xuống 4%
- Hạ lãi suất chiết khấu từ 2,5% xuống 2%
Đây là lần giảm thứ 3 trong năm 2026.
```

**Output (Structured MD):**
```markdown
## NHNN Điều Chỉnh Lãi Suất Điều Hành

**Ngày:** 15/5/2026

| Loại lãi suất | Trước | Sau |
|---|---|---|
| Tái cấp vốn | 4.5% | 4.0% |
| Chiết khấu | 2.5% | 2.0% |

> Đây là lần giảm thứ 3 trong năm 2026.
```
