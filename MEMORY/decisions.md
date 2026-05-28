# Memory — Decisions

> Các quyết định quan trọng đã đưa ra trong hệ thống.
> Agent đọc file này đầu mỗi session để hiểu context hiện tại.
> **Path:** `MEMORY/decisions.md`

## Format
```
[YYYY-MM-DD] [CATEGORY] [QUYẾT ĐỊNH]: [nội dung] — [lý do]
Category: SYSTEM / WORKFLOW / VAULT / VJ / CONTENT
```

## Log

[2026-05-20] [SYSTEM] Thiết kế vault theo 3 nhánh CC/LS/TD — Áp dụng ConanSchool framework cho ABF
[2026-05-20] [VAULT] Vault mới tạo tại ABF-Vault/ tách biệt khỏi ABF01-main 3/ — Tránh nhầm lẫn với vault cũ
[2026-05-20] [VAULT] MEMORY/ là folder session memory chính — Đọc đầu mỗi session
[2026-05-20] [VAULT] VJ profiles lưu tại VJ/VJ-[tên]/profile.md — Dễ search và update
[2026-05-20] [VAULT] Feed Loop ghi tại FEED-LOOP/ sau mỗi workflow run — Vòng lặp compound knowledge
