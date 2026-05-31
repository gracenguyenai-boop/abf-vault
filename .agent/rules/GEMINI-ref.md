# GEMINI-ref.md — Quick Reference & Routing

> File tham chiếu nhanh. AG đọc khi cần paths, routing, hoặc skill locations.
> File chính: `.agent/rules/GEMINI.md`

---

## Routing Table — Map prompt → workflow

| Từ khoá | Workflow file | VJ / Kênh |
|---|---|---|
| news / tin tức / thời sự / breaking / tin nóng / lãi suất mới | `TikTok-news-viral-workflow.md` | ABVV (An Bình Vay Vốn) |
| case study / hồ sơ / khách hàng / câu chuyện / vay vốn / before after | `TikTok-Case-Study-Workflow.md` | Chọn 1 trong 4 kênh: Khang / Huy / Duke / Tuyết Anh |

### Natural Language Aliases

| Prompt tự nhiên | Map sang |
|---|---|
| "làm tiktok news viral" | `TikTok-news-viral-workflow.md` |
| "viết script tin tức lãi suất" | `TikTok-news-viral-workflow.md` |
| "có tin mới về NHNN" | `TikTok-news-viral-workflow.md` |
| "làm case study hồ sơ vay" | `TikTok-Case-Study-Workflow.md` |
| "có hồ sơ khách mới" | `TikTok-Case-Study-Workflow.md` |
| "viết script cho kênh Khang" | `TikTok-Case-Study-Workflow.md` (style: Khang) |

Không rõ loại → HỎI VJ trước khi tiếp tục.

---

## Workflow Files

| Workflow | GitHub Path | Load bằng |
|---|---|---|
| News Viral | `.agent/workflows/TikTok-news-viral-workflow.md` | `mcp_github_get_file_contents(path=".agent/workflows/TikTok-news-viral-workflow.md")` |
| Case Study | `.agent/workflows/TikTok-case-study-workflow.md` | `mcp_github_get_file_contents(path=".agent/workflows/TikTok-case-study-workflow.md")` |

> Tất cả paths đều thuộc repo `gracenguyenai-boop/abf-vault`, branch `main`.

---

## Kênh / Style Profiles (dùng trong Case Study workflow)

Case Study workflow hỗ trợ 4 style kênh — user chọn trong Phase 4 của workflow:
- **Khang** — `.agent/vjs/Khang Vay Hay/`
- **Huy** — `.agent/vjs/An Binh Vay Von/`
- **Duke** — `.agent/vjs/Dat Vay Don Gian/`
- **Tuyết Anh** — `.agent/vjs/Thuy Vay Von/`

Load bằng: `mcp_github_get_file_contents(path=".agent/vjs/<tên kênh>/")` để lấy toàn bộ DNA profile.

Nếu user không chọn → mặc định style Tuyết Anh (phổ quát nhất).

ABVV (An Bình Vay Vốn) — kênh chính cho News Viral, channel profile nằm trong workflow.

---

## Skill Paths

> **Cách load skill:** `mcp_github_get_file_contents(path="<GitHub Path>", owner="gracenguyenai-boop", repo="abf-vault", branch="main")`

### General Skills (dùng cho cả 2 workflows)
| Skill | GitHub Path |
|---|---|
| TikTok Script | `.agent/skills/tiktok-script-skill.md` |
| Web Enrichment | `.agent/skills/general/web-enrichment.md` |
| NotebookLM | `.agent/skills/general/notebooklm-toolkit.md` |
| Think | `.agent/skills/general/think.md` |
| Ask Clarification | `.agent/skills/general/ask-for-clarification.md` |
| Audio Transcribe | `.agent/skills/general/audio-transcribe.md` |
| Crawler | `.agent/skills/general/crawler.md` |
| Batch Web Search | `.agent/skills/general/batch-web-search.md` |
| Summarize Large Doc | `.agent/skills/general/summarize-large-document.md` |

### Skills — News Viral workflow
| Skill | Phase | Ghi chú |
|---|---|---|
| news-context-synthesizer | 1 | Tổng hợp tin từ báo chính thống |
| event-timeline-builder | 1 | Dựng timeline sự kiện |
| ethos-credibility-analyzer | 1 | Phân tích uy tín nguồn (bắt buộc) |
| root-cause-analyzer | 1 | Phân tích 3 lớp nguyên nhân |
| stakeholder-impact-mapper | 1 | Map tác động đến từng nhóm |
| historical-comparator | 1 | Tìm precedent lịch sử |
| synthesizing-viewpoints | 1 | So sánh quan điểm VJ vs chuyên gia |
| forecast-synthesizer | 1 | Dự báo + lời khuyên |
| viewer-sentiment-analysis | 2 | Phân tích tâm lý người xem |
| angle-generator | 2 | Sinh 5 angles |
| angle-scorer | 2 | Chấm điểm chọn WINNER |
| hook-writer | 3 | Viết 3 hook (shared với Case Study) |
| success-framework-scorer | 3 | Chấm SUCCESS framework (shared) |
| body-writer | 4 | Viết body (shared) |
| cta-writer | 4 | Viết CTA (shared) |
| title-writer | 4 | Viết title (shared) |
| caption-hashtag-writer | 4 | Viết caption + hashtag (shared) |
| human-voice-writer | 4 | Chuyển thành ngôn ngữ nói |
| human-authenticity-scorer | 5 | Chấm tính người (shared) |
| tiktok-policy-scanner | 5 | Quét từ cấm TikTok (shared) |
| channel-fit-validator | 5 | Kiểm tra khớp kênh (shared) |

### Skills — Case Study workflow
| Skill | Phase | Ghi chú |
|---|---|---|
| 4F-analyzer | 2 | Phân tích hồ sơ theo 4F |
| time-builder | 3 | Dựng bối cảnh thời gian vay |
| macro-context | 3 | Tra cứu vĩ mô thời điểm vay |
| story-arc | 4 | Xây dựng story arc |
| hook-writer | 6 | Viết 3 hook (shared) |
| success-framework-scorer | 6 | Chấm SUCCESS framework (shared) |
| body-writer | 7 | Viết body theo công thức content (shared) |
| cta-writer | 7 | Viết CTA theo DNA kênh (shared) |
| title-writer | 7 | Viết title (shared) |
| caption-hashtag-writer | 7 | Viết caption + hashtag (shared) |
| human-authenticity-scorer | 7, 11 | Chấm tính người (shared) |
| broll-mapper | 8 | Map b-roll vào script |
| dna-filter | 9 | Lọc văn phong theo DNA kênh |
| dynamic-injector | 10 | Inject thông tin dynamic + mask non-public |
| tiktok-policy-scanner | 11 | Quét từ cấm TikTok (shared) |
| channel-fit-validator | 11 | Kiểm tra khớp kênh (shared) |

---

## Output Paths (Local — trên máy VJ)

| Workflow | Output path |
|---|---|
| News Viral | `outputs/scripts/tiktok/` |
| Case Study | `outputs/scripts/tiktok/` |

> Output lưu local trên máy VJ, KHÔNG ghi lên GitHub repo.

---

## Temp Files
- Screenshots, logs tạm, file test → `00-Inbox/temp/` (local)
- KHÔNG lưu temp files vào output folders

---

## Vault Structure (GitHub repo)

```
gracenguyenai-boop/abf-vault @ main

00-Inbox/          ← raw news, verification logs, temp files
01-Atomic/
  Concepts/        ← kiến thức tài chính
  Stories/         ← case study thực tế (verified only)
  Insights/        ← góc nhìn đã distill
  Frameworks/
  Perspectives/
  Quotes/
  Strategies/
02-Memory/         ← decisions, blockers, sessions-log, preferences (read-only từ GitHub)
03-MOCs/           ← MOC-ABF-VayVon.md  ← ĐỌC ĐÂY TRƯỚC để hiểu cấu trúc vault
.agent/
  rules/           ← GEMINI.md, GEMINI-ref.md
  workflows/       ← workflow files
  skills/          ← skill modules
  vjs/             ← VJ / kênh DNA profiles
```
