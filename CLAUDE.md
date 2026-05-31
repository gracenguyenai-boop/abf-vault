# ABF Workflow — Claude Code Instructions

> File này được đọc tự động bởi Claude Code trước mỗi session.
> Đây là bản thích nghi của GEMINI.md cho môi trường Claude Code.

---

## ⚙️ HỆ THỐNG

```
Vault:    https://github.com/gracenguyenai-boop/abf-vault (public)
Base URL: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main
Tool:     WebFetch — dùng để đọc raw file từ vault
```

**Cách đọc file từ vault:**
```
WebFetch: https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/<path>
```

---

## ⚡ BOOTSTRAP — Khi nhận BẤT KỲ prompt nào

⛔ DỪNG. Chạy 4 bước tuần tự — mỗi bước chờ input trước khi hiện bước tiếp. KHÔNG tự đoán.

> **Shortcut rule:** Nếu prompt đã chứa đủ thông tin (ví dụ: *"thuỷ case study đóng vai"*) → extract các field đã có, chỉ hỏi bước còn thiếu (thường là Bước 3 — nội dung).

---

**BƯỚC 1 — Chọn kênh:**

```
🎬 ABF Workflow

Chọn kênh:

  [ A ] An Bình Vay Vốn     [ B ] Khang Vay Hay
  [ C ] Thuỷ Vay Vốn        [ D ] Đặt Vay Đơn Giản
```

⛔ DỪNG — chờ chọn. Không hiện bước 2 trước khi có kết quả.

---

**BƯỚC 2 — Chọn workflow** *(hiện sau khi có VJ)*

| VJ | Workflow hiển thị |
|---|---|
| A — An Bình | `[1] News Viral` `[2] Case Study` `[3] Kiến Thức Vay Vốn` `[4] An Bình Là Ai` |
| B, C, D | `[1] News Viral` `[2] Case Study` |

```
✅ Kênh: [tên VJ]

Chọn workflow:

  [danh sách theo VJ]
```

⛔ DỪNG — chờ chọn.

---

**BƯỚC 3 — Nhập nội dung** *(hiện sau khi có VJ + Workflow)*

| Workflow | Câu hỏi |
|---|---|
| News Viral | `Dán link bài báo hoặc mô tả tin tức:` |
| Case Study | `Dán file hồ sơ / mô tả case / ghi chú 4F:` |
| Kiến Thức Vay Vốn | `Nhập chủ đề kiến thức vay vốn:` |
| An Bình Là Ai | `Nhập nội dung / góc nhìn muốn khai thác:` |

```
✅ Kênh: [X]   Workflow: [Y]

[Câu hỏi theo workflow]

  _______________________________________________
```

⛔ DỪNG — chờ nhập.

---

**BƯỚC 4 — Chọn format** *(hiện sau khi có VJ + Workflow + Nội dung)*

Ma trận format hợp lệ theo VJ × Workflow:

| VJ | News Viral | Case Study |
|---|---|---|
| A — An Bình | talking-head · tips-nhanh | talking-head · tips-nhanh |
| B — Khang | talking-head · tips-nhanh | talking-head · tips-nhanh · giai-quyet-thuc-dia · selfie · tu-van-hoi-thoai |
| C — Thuỷ | talking-head · tips-nhanh | talking-head · tips-nhanh · dong-vai |
| D — Đặt | talking-head · tips-nhanh | talking-head · tips-nhanh · trong-xe-o-to · nghe-dien-thoai · cam-giay-to |

```
✅ Kênh: [X]   Workflow: [Y]   Nội dung: nhận ✓

Chọn format quay:

  [chỉ hiện format hợp lệ theo bảng trên]
```

⛔ DỪNG — chờ chọn. KHÔNG tự đoán format.

---

→ Sau khi có đủ 4 bước → lưu working memory:
`VJ = [X]` | `WORKFLOW = [Y]` | `FORMAT = [Z]` | `INPUT = [W]`

```
✅ Kênh: [X]   Workflow: [Y]   Format: [Z]   Nội dung: nhận ✓
→ Đang khởi động PHASE 0...
```

---

## 🔄 PHASE 0 — PRE-PROCESSING (BẮT BUỘC)

Fetch **song song** 5 URLs bằng WebFetch:

```
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/.agent/rules/VAULT-STRUCTURE-REF.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/decisions.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/blockers.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/sessions-log.md
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MEMORY/preferences.md
```

→ Tóm tắt: `"Session trước: [X]. Hôm nay: [Y]."`

Fetch MOC:
```
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/MOC-MASTER.md
```

Load scripts mẫu theo VJ + format (fetch `_RULE-*` trước, rồi các script `.md` lọc theo `workflow-tags`):
```
https://raw.githubusercontent.com/gracenguyenai-boop/abf-vault/main/VJ/VJ-[tên]/scripts/[format]/
```

Fetch workflow file:

| Workflow | URL |
|---|---|
| News Viral | `.../main/.agent/workflows/TikTok-news-viral-workflow.md` |
| Case Study | `.../main/.agent/workflows/TikTok-case-study-workflow.md` |
| KTVV | `.../main/.agent/workflows/Tiktok_Kiến_Thức_Vay_Vốn_KTVV_Workflow.md` |
| ABLA | `.../main/.agent/workflows/Tiktok_An_Binh_La_Ai_ABLA_Workflow.md` |

→ Đọc toàn bộ workflow → chạy từ Phase 1.

---

## QUY TẮC

1. **Ngôn ngữ:** Luôn tiếng Việt. Tên file/path giữ tiếng Anh.
2. **Vault first:** Search vault trước khi tạo nội dung mới.
3. **Không bịa Story** — chỉ dùng thông tin có trong hồ sơ thực tế.
4. **Hỏi trước khi lưu:** `✅ Hoàn thành [task]. → Lưu vào [path] không?`
5. **Output lưu local:** `outputs/scripts/tiktok/<filename>.md`
