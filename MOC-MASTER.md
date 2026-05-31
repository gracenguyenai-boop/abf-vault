# MOC-MASTER — Entry Point Toàn Vault

> Cửa vào duy nhất. Agent và người dùng đều bắt đầu từ đây.
> Vault root: `Downloads/ABF-Vault/`

---

## Sơ Đồ Phân Tầng MOC (3 Tầng)

```
TIER 0 ─── MOC-MASTER (file này)
              │
    ┌─────────┼──────────┬──────────┬──────────┐
    │         │          │          │          │
TIER 1    CC-MOC     LS-MOC     TD-MOC   Shared-MOC   VJ-Master
    │         │          │          │          │
    │    ┌────┴────┐  ┌──┴───┐  ┌──┴────┐  ┌──┴──┐
    │    │  L1·L2  │  │L1·L2 │  │L1·L2  │  │L1·L2│
TIER 2  │  L3·L4  │  │L3·L4 │  │L3(TC  │  │L3·L4│   4 kênh VJ
(sub)   └─────────┘  └──────┘  │ BDS   │  └─────┘  ├ AnBinh
                                │ CS·CK)│           ├ Đạt
                                │ L4    │           ├ Khang──→ KienThuc-MOC
                                └───────┘           └ Thuỷ     CaseStudy-MOC
    │         │          │          │
TIER 3   (shells)    7 notes    94 notes    1 note     47 scripts Khang
```

**Legend:** ✅ = có notes thực | Shell = cấu trúc sẵn, chờ điền notes

---

## 4 Nhánh Tri Thức Chính

| Nhánh | Mục đích | MOC Tầng 1 |
|---|---|---|
| [[MOC-ContentCreator]] | Kỹ thuật viết, hook, cấu trúc kịch bản | `CC-ContentCreator/CC-MOC/` |
| [[MOC-LoanSpecialist]] | Nghiệp vụ ngân hàng, xử lý hồ sơ vay | `LS-LoanSpecialist/LS-MOC/` |
| [[MOC-TraDa]] | Bối cảnh vĩ mô, tin tức thị trường | `TD-TraDa/TD-MOC/` |
| [[MOC-Shared]] | Kiến thức cross-nhánh, kỹ năng mềm | `Shared/Shared-MOC/` |

---

## Toàn Bộ Sub-MOC Tầng 2

### CC — Content Creator
| Sub-MOC | Nội dung | Trạng thái |
|---|---|---|
| CC-L1-MOC | Framework tư duy: 4P, 5W1H, 5Why, bullet-group | Shell |
| CC-L2-MOC | Copywriting: PAS, AIDA, muc-tieu-dau-ra | Shell |
| CC-L3-MOC | Hook ABF, 4 trụ cột, hook library | Shell |
| CC-L4-MOC | PDCA review: KTP, comment-analysis, sprint | Shell |

### LS — Loan Specialist
| Sub-MOC | Nội dung | Trạng thái |
|---|---|---|
| LS-L1-MOC | Framework: quy trình 7 bước, logic tiếp nhận | ✅ 1 note |
| LS-L2-MOC | 23 NH thị trường · thẩm định · nguồn KH · 5 sản phẩm | ✅ 4 notes |
| LS-L3-MOC | VPBank ops: sản phẩm · lãi suất · checklist · luồng · ngoại lệ · nguồn thu | ✅ 6 notes |
| LS-L4-MOC | Template 4F + 36 cases (14 giải ngân · 22 không thành công) | ✅ 36 cases |

### TD — Trà Đá (Vĩ Mô)
| Sub-MOC | Nội dung | Trạng thái |
|---|---|---|
| TD-L1-MOC | Framework đọc tin: signal/noise, ethos | Shell |
| TD-L2-MOC | Kỹ năng đọc chỉ số kinh tế | Shell |
| TD-L3-TC-MOC | 58 notes — Tài Chính / Ngân Hàng | ✅ |
| TD-L3-BDS-MOC | 16 notes — Bất Động Sản | ✅ |
| TD-L3-CS-MOC | 19 notes — Chính Sách | ✅ |
| TD-L3-CK-MOC | 1 note — Chứng Khoán | ✅ |
| TD-L4-MOC | Viewer sentiment, comment scraping | Shell |

### Shared
| Sub-MOC | Nội dung | Trạng thái |
|---|---|---|
| Shared-L1-MOC | Chân dung KH Venn (A/B/C/KEY) | ✅ 1 note |
| Shared-L2-MOC | Kỹ năng mềm: storytelling, simplicity, trust | Shell |
| Shared-L3-MOC | Tài nguyên: số liệu, glossary, nguồn tin | Shell |
| Shared-L4-MOC | PDCA hệ thống: sprint review, vault health | Shell |

### VJ
| Sub-MOC | Nội dung | Trạng thái |
|---|---|---|
| MOC-VJ-Templates | Index 7 templates dùng chung | ✅ |
| MOC-VJ-AnBinh | DNA kênh + **2 Rule Files** (Talking Head · Tips Ngắn) | ✅ |
| MOC-VJ-Dat | DNA kênh + **5 Rule Files** (TH · Tips · Xe ô tô · Điện thoại · Giấy tờ) | ✅ |
| MOC-VJ-Khang | DNA kênh + **5 Rule Files** (TH · Tips · Thực địa · Selfie · Hội thoại) | ✅ |
| MOC-VJ-Thuy | DNA kênh + **3 Rule Files** (TH · Tips · Đóng vai) | ✅ |

> **Rule Files** (`_RULE-[vj]-[format].md`) là blueprint viết script theo từng format — đọc TRƯỚC KHI viết. Inventory đầy đủ tại [[MOC VJ-Master]].

---

## VJ Profiles

→ [[MOC VJ-Master]] — Routing, DNA, so sánh 4 kênh

---

## Workflow → Vault (Quick Map)

### News Viral — VJ An Bình
```
Phase 0   → MEMORY/decisions.md + preferences.md
Phase 1b  → [[LS-L3-MOC]] (VPBank ops) + [[LS-L2-MOC]] (thị trường)
Phase 1.3 → [[TD-L1-MOC]] (ethos credibility nguồn)
Phase 1.7 → [[TD-L3-TC-MOC]] (lãi suất / tín dụng)
Phase 2   → [[TD-L4-MOC]] (viewer sentiment)
Phase 3   → [[CC-L3-MOC]] (hook ABF)
Phase 4a  → VJ/MOC VJ-Master.md (VJ routing gateway)
Phase 4   → VJ/VJ-AnBinh/VJ-MOC/MOC-VJ-AnBinh.md (DNA)
Output    → VJ/VJ-AnBinh/scripts/[date]-[topic].md
Feed Loop → VJ/VJ-AnBinh/VJ-01-Atomic/insight/insight-[date]-[topic].md
```

### Case Study — VJ Đạt / Khang / Thuỷ
```
Phase 0   → MEMORY/decisions.md + preferences.md
Phase 1   → [[LS-L4-MOC]] → _template-4fcase.md
Phase 2   → [[TD-L3-TC-MOC]] + [[TD-L3-BDS-MOC]]
Phase 4a  → VJ/MOC VJ-Master.md (VJ routing gateway)
Phase 4   → VJ/VJ-[tên]/VJ-MOC/MOC-VJ-[tên].md (DNA)
Phase 5   → [[CC-L3-MOC]] (hook)
Phase 6   → [[CC-L2-MOC]] (body formula)
Output    → VJ/VJ-[tên]/scripts/[date]-[case].md
Feed Loop → VJ/VJ-[tên]/VJ-01-Atomic/insight/insight-[date]-[case].md
```

---

## Sau Mỗi Workflow Run
```
1. Agent tạo insight file → VJ/VJ-[tên]/VJ-01-Atomic/insight/
2. Append session log    → MEMORY/sessions-log.md
3. Sau 48h: team điền kết quả thực tế vào insight file
4. Nếu reusable → promote lên CC / LS / TD
```
→ [[_GUIDE-FeedLoop]]

---

## Graph View — Tag Theo Nhánh

| Tag | Nhánh | Màu đề xuất |
|---|---|---|
| `#CC` | Content Creator | Vàng |
| `#LS` | Loan Specialist | Xanh dương |
| `#TD` + `#TC` `#BDS` `#CS` `#CK` | Trà Đá | Xanh lá |
| `#Shared` | Shared | Tím |
| `#VJ` + `#Khang` `#AnBinh` v.v. | VJ kênh | Cam |
| `#MOC` | Tất cả MOC files | Trắng / đậm |

---

## Skills & Automation

→ Skill: [[.agent/skills/raw-file-atomizer/SKILL]]
→ Cấu trúc vault đầy đủ: [[.agent/rules/VAULT-STRUCTURE-REF]]
