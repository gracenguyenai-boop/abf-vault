# Guide — Feed Loop

> Sau mỗi lần ship script, chạy quy trình này để vault giàu dần theo thời gian.
> **Nguyên tắc:** VJ-first — insight vào VJ trước, promote lên CC/LS/TD khi đã có data thực.

---

## Luồng Hoạt Động

```
Script hoàn chỉnh (workflow done)
        ↓
Agent tạo 1 file insight (< 30 giây)
        ↓
File lưu tại: VJ/VJ-[tên]/VJ-01-Atomic/insight/insight-[YYYY-MM-DD]-[topic].md
        ↓
48h sau: Team điền "Kết quả thực tế" vào file
        ↓
Nếu insight reusable → team copy sang CC / LS / TD đúng path
Nếu chỉ relevant cho kênh đó → giữ lại trong VJ insight/
```

---

## Template File Insight (Agent Tạo Sau Mỗi Run)

```markdown
---
name: insight-[YYYY-MM-DD]-[topic-slug]
type: insight
subtype: post-run
topics: ["[vj-name]", "[topic]"]
status: raw
created: YYYY-MM-DD
source: [tên workflow run]
confidence: low
verified: false
related: ["[[VJ-MOC/MOC-VJ-[tên]]]"]
maturity: seed
review_interval: 7
next_review: YYYY-MM-DD+7
reuse_count: 0
evolution_log: []
---

# Insight — [Topic] ([YYYY-MM-DD])

**VJ:** [tên] | **Workflow:** news-viral / case-study

## Hook Đã Dùng
> [paste câu hook nguyên văn]

## Kiến Thức / Dữ Liệu Chính Trong Script
> [paste 2–3 điểm agent đã dùng để viết — số liệu, khái niệm, bối cảnh]

## Điều Chưa Chắc / Cần Verify
> [để trống nếu không có]

---

## Kết Quả Thực Tế (team điền sau 48h)
- View:
- Like rate:
- Comment đáng chú ý:
- Hook có work không? [ ] Có  [ ] Không  [ ] Không rõ

## Promote Lên Vault Chung?
- [ ] Hook → `CC/CC-01-Atomic/L3-KienThucDacThu/hook-[topic]-[date].md`
- [ ] Kiến thức ngân hàng → `LS/LS-01-Atomic/L2-KienThucNghe/[concept]-[date].md`
- [ ] Bối cảnh vĩ mô → `TD/TD-01-Atomic/L3-KienThucDacThu/[TC|BDS|CK|CS]/[topic]-[date].md`
- [ ] Không cần promote
```

---

## Routing Table — Insight → Vault Path

| Loại insight | Path ghi vào |
|---|---|
| Hook hiệu quả | `CC-ContentCreator/CC-01-Atomic/L3-KienThucDacThu/` |
| Khái niệm ngân hàng mới | `LS-LoanSpecialist/LS-01-Atomic/L2-KienThucNghe/` |
| Kỹ thuật nghiệp vụ | `LS-LoanSpecialist/LS-01-Atomic/L3-KienThucDacThu/` |
| 4F case analysis | `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/4fcases/` |
| Bối cảnh vĩ mô (TC) | `TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/TC/` |
| Bối cảnh vĩ mô (BDS) | `TD-TraDa/TD-01-Atomic/L3-KienThucDacThu/BDS/` |
| Comment / viewer sentiment | `TD-TraDa/TD-01-Atomic/L4-PDCA/` |
| Script pattern kênh | `VJ/VJ-[tên]/VJ-01-Atomic/framework/` |
| Câu chuyện KH mới | `VJ/VJ-[tên]/VJ-01-Atomic/story/` |
| Quote hay từ viewer | `VJ/VJ-[tên]/VJ-01-Atomic/quote/` |
| Performance insight | `VJ/VJ-[tên]/VJ-01-Atomic/insight/` ← default |

---

## Tên File

```
VJ/VJ-[tên]/VJ-01-Atomic/insight/insight-[YYYY-MM-DD]-[topic-ngan].md
```

Ví dụ:
```
VJ/VJ-AnBinh/VJ-01-Atomic/insight/insight-2026-05-20-laisuat-giam.md
VJ/VJ-Dat/VJ-01-Atomic/insight/insight-2026-05-20-mua-nha-lan-dau.md
```

---

## Cập Nhật Session Log (Sau Mỗi Run)

Append vào `MEMORY/sessions-log.md`:
```
[YYYY-MM-DD HH:MM] VJ:[tên] Workflow:[news-viral/case-study] Input:[tóm tắt] Output:[tên file script] Insight:[tên file insight]
```
