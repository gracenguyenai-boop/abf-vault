#!/usr/bin/env python3
"""
Batch thêm workflow-tags vào frontmatter của tất cả script files trong vault.

Logic phân loại:
- Format cố định → case-study: giai-quyet-thuc-dia, dong-vai, tu-van-hoi-thoai, cam-giay-to, nghe-dien-thoai
- Format cố định → news: selfie
- Format cố định → trong-xe-o-to: case-study hoặc news dựa theo topics
- talking-head / tips-nhanh: phân tích topics + filename để phán đoán
"""

import os
import re
import sys

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VJ_FOLDER = os.path.join(VAULT_ROOT, "VJ")

# Từ khóa trong topics/filename → case-study
CASE_STUDY_KEYWORDS = [
    "case study", "case-study", "hồ sơ", "khách hàng", "4f",
    "giải quyết", "cơ cấu", "chuyển bank", "chuyển ngân hàng",
    "tái cơ cấu", "mua nợ", "đáo hạn", "ngoại lệ", "thực địa",
    "vay được", "bị từ chối", "tài sản", "sổ đỏ", "định giá",
    "cic", "nợ xấu", "trình phê duyệt", "giải ngân"
]

# Từ khóa trong topics/filename → news
NEWS_KEYWORDS = [
    "tin tức", "thời sự", "nhnn", "ngân hàng nhà nước", "chính sách",
    "lãi suất", "thị trường", "bất động sản", "vàng", "chứng khoán",
    "kinh tế", "tăng trưởng", "gdp", "lạm phát", "tỷ giá",
    "thông tư", "nghị định", "quyết định", "room tín dụng",
    "bơm tiền", "hút tiền", "dự báo", "phân tích thị trường",
    "canh bao", "cảnh báo tin tức"
]

FORMAT_FIXED_CASE_STUDY = [
    "giai-quyet-thuc-dia", "dong-vai", "tu-van-hoi-thoai",
    "cam-giay-to", "nghe-dien-thoai"
]
FORMAT_FIXED_NEWS = ["selfie"]


def detect_workflow_tags(filepath, format_name, topics_text, filename):
    """Phán đoán workflow-tags từ format + topics + filename."""
    combined = (topics_text + " " + filename).lower()

    if format_name in FORMAT_FIXED_CASE_STUDY:
        return ["case-study"]
    if format_name in FORMAT_FIXED_NEWS:
        return ["news"]

    # trong-xe-o-to: check topics
    if format_name == "trong-xe-o-to":
        for kw in CASE_STUDY_KEYWORDS:
            if kw in combined:
                return ["case-study"]
        return ["news"]

    # talking-head / tips-nhanh: score keywords
    case_score = sum(1 for kw in CASE_STUDY_KEYWORDS if kw in combined)
    news_score = sum(1 for kw in NEWS_KEYWORDS if kw in combined)

    if case_score > news_score:
        return ["case-study"]
    elif news_score > case_score:
        return ["news"]
    else:
        # Tie → dùng cả 2
        return ["news", "case-study"]


def add_workflow_tags(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Bỏ qua nếu đã có workflow-tags
    if "workflow-tags" in content:
        return "skip"

    # Parse frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return "no-frontmatter"

    fm = fm_match.group(1)

    # Lấy format từ frontmatter
    format_match = re.search(r"^format:\s*(.+)$", fm, re.MULTILINE)
    format_name = format_match.group(1).strip() if format_match else ""

    # Lấy topics
    topics_match = re.search(r"topics:(.*?)(?=\n\w|\Z)", fm, re.DOTALL)
    topics_text = topics_match.group(1) if topics_match else ""

    filename = os.path.basename(filepath).lower()

    tags = detect_workflow_tags(filepath, format_name, topics_text, filename)
    tags_yaml = "\n".join([f"  - {t}" for t in tags])
    new_field = f"workflow-tags:\n{tags_yaml}"

    # Chèn workflow-tags sau dòng "format:"
    new_fm = re.sub(
        r"(^format:.*$)",
        r"\1\n" + new_field,
        fm,
        flags=re.MULTILINE
    )

    new_content = content.replace(fm_match.group(1), new_fm, 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return f"added: {tags}"


def main():
    stats = {"added": 0, "skipped": 0, "no_frontmatter": 0, "errors": 0}

    for vj_dir in os.listdir(VJ_FOLDER):
        vj_path = os.path.join(VJ_FOLDER, vj_dir)
        if not os.path.isdir(vj_path) or vj_dir.startswith("_"):
            continue

        scripts_path = os.path.join(vj_path, "scripts")
        if not os.path.exists(scripts_path):
            continue

        for root, dirs, files in os.walk(scripts_path):
            for fname in files:
                if not fname.endswith(".md") or fname.startswith("_"):
                    continue
                fpath = os.path.join(root, fname)
                try:
                    result = add_workflow_tags(fpath)
                    if result == "skip":
                        stats["skipped"] += 1
                    elif result == "no-frontmatter":
                        stats["no_frontmatter"] += 1
                    else:
                        stats["added"] += 1
                        print(f"  ✅ {fname[:50]} → {result}")
                except Exception as e:
                    stats["errors"] += 1
                    print(f"  ❌ {fname}: {e}")

    print(f"\n--- DONE ---")
    print(f"Added:          {stats['added']}")
    print(f"Already tagged: {stats['skipped']}")
    print(f"No frontmatter: {stats['no_frontmatter']}")
    print(f"Errors:         {stats['errors']}")


if __name__ == "__main__":
    main()
