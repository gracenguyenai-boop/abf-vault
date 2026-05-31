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

⛔ DỪNG. Gọi **AskUserQuestion tool 1 LẦN DUY NHẤT** với 4 câu hỏi cùng lúc — user điền hết rồi submit 1 lần.

> **Shortcut rule:** Nếu prompt đã chứa đủ thông tin → extract field đã có, bỏ qua AskUserQuestion, chạy PHASE 0 luôn.

---

**GỌI AskUserQuestion với 4 câu hỏi:**

```
questions: [
  {
    question: "🎬 Chọn kênh:",
    header: "Kênh",
    options: [
      { label: "An Bình Vay Vốn", description: "VJ An Bình" },
      { label: "Khang Vay Hay",   description: "VJ Khang"   },
      { label: "Thuỷ Vay Vốn",    description: "VJ Thuỷ"    },
      { label: "Đặt Vay Đơn Giản",description: "VJ Đặt"     }
    ]
  },
  {
    question: "Chọn workflow:",
    header: "Workflow",
    options: [
      { label: "News Viral",         description: "Tin tức / thời sự"        },
      { label: "Case Study",         description: "Hồ sơ vay vốn thực tế"    },
      { label: "Kiến Thức Vay Vốn",  description: "Chỉ dùng cho An Bình"     },
      { label: "An Bình Là Ai",      description: "Chỉ dùng cho An Bình"     }
    ]
  },
  {
    question: "[Câu hỏi nội dung theo workflow — xem bảng dưới]",
    header: "Nội dung",
    options: [
      { label: "→ Nhập vào ô bên dưới", description: "Dán link hoặc mô tả nội dung" },
      { label: "Chưa có nội dung",      description: "Bỏ qua bước này"              }
    ]
  },
  {
    question: "Chọn format quay:",
    header: "Format",
    options: [
      { label: "talking-head",          description: "Monologue — mọi kênh"         },
      { label: "tips-nhanh",            description: "Tips ngắn — mọi kênh"         },
      { label: "dong-vai / giai-quyet / trong-xe", description: "Format đặc biệt theo kênh" },
      { label: "selfie / tu-van / nghe-dt / cam-giay", description: "Format đặc biệt theo kênh" }
    ]
  }
]
```

Câu hỏi nội dung theo workflow:
- News Viral        → `"Nội dung news cần phân tích:"`
- Case Study        → `"Nội dung case cần phân tích:"`
- Kiến Thức Vay Vốn → `"Chủ đề cần phân tích:"`
- An Bình Là Ai     → `"Nội dung cần phân tích:"`

Format hợp lệ theo VJ × Workflow — **sau khi nhận kết quả, kiểm tra và báo lỗi nếu chọn sai combo:**

| VJ | News Viral | Case Study |
|---|---|---|
| An Bình | talking-head, tips-nhanh | talking-head, tips-nhanh |
| Khang | talking-head, tips-nhanh | talking-head, tips-nhanh, giai-quyet-thuc-dia, selfie, tu-van-hoi-thoai |
| Thuỷ | talking-head, tips-nhanh | talking-head, tips-nhanh, dong-vai |
| Đặt | talking-head, tips-nhanh | talking-head, tips-nhanh, trong-xe-o-to, nghe-dien-thoai, cam-giay-to |

⛔ Sau khi nhận đủ 4 kết quả → validate combo VJ × Workflow × Format → lưu working memory → chạy PHASE 0.

---

→ Sau khi có đủ 4 bước → lưu working memory:
`VJ = [X]` | `WORKFLOW = [Y]` | `FORMAT = [Z]` | `INPUT = [W]`

Hiển thị confirm:
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
