#!/usr/bin/env python3
"""
Format raw transcript scripts thành văn bản có dấu câu và đoạn văn.
Giữ nguyên nội dung — chỉ thêm formatting.

Áp dụng cho: VJ/VJ-Thuy/scripts/talking-head/ (và các folder khác nếu cần)
"""

import os
import re

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Sentence boundary markers ──────────────────────────────────────────────
# Các từ/cụm thường kết thúc 1 câu trong văn nói tiếng Việt
SENTENCE_ENDS = [
    r'nhá(?=\s)',
    r'nhé(?=\s)',
    r'nha(?=\s)',
    r'ạ(?=\s)',
    r'nhé(?=$)',
    r'nhá(?=$)',
    r'nha(?=$)',
    r'ạ(?=$)',
    r'thôi(?=\s+[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ])',
]

# Conjunctions thường BẮT ĐẦU câu mới
NEW_SENTENCE_STARTERS = [
    'nhưng mà', 'nhưng', 'tuy nhiên', 'vì vậy', 'do đó', 'bởi vì',
    'chính vì', 'vì là', 'vì thế', 'còn nếu', 'nếu như', 'nếu anh chị',
    'ví dụ như', 'ví dụ', 'cụ thể là', 'đặc biệt là',
    'em có', 'em sẽ', 'em đã', 'em vừa', 'em thấy',
    'anh chị', 'và nếu', 'còn về', 'còn với',
    'thực tế là', 'thực ra', 'thật ra', 'thật sự',
    'kết quả là', 'kết quả', 'điều này',
]

# Paragraph break triggers — chủ đề chuyển sang đoạn mới
PARA_BREAKS = [
    'em có khách hàng', 'đây là một ca', 'trường hợp thực tế',
    'kết quả là', 'và kết quả', 'cuối cùng',
    'nếu anh chị', 'nếu như anh chị', 'vì vậy anh chị',
    'thứ nhất', 'thứ hai', 'thứ ba', 'đầu tiên là',
    'vì là mỗi', 'ví dụ như các',
    'em sẽ hỗ trợ', 'em thủy sẽ',
]


def fix_capitalization(text: str) -> str:
    """Lowercase random ALL-CAPS words, giữ proper nouns."""
    # Fix những từ bị viết hoa giữa câu kiểu: Sai, Ra, Cho, Cao, Chu, Minh
    # Chỉ lowercase nếu: chữ hoa đứng giữa câu (không đầu câu)
    def fix_word(m):
        word = m.group(0)
        # Giữ nguyên các từ viết tắt thật sự: BHXH, CIC, BA (số), VPBank...
        if word.isupper() and len(word) <= 3:
            return word  # giữ nguyên: BA, CIC, OK...
        if word[0].isupper() and word[1:].islower():
            # Có thể là proper noun hoặc lỗi capitalize
            # Lowercase nếu không phải tên riêng (đơn giản hóa: lowercase tất cả giữa câu)
            return word.lower()
        return word

    # Lowercase từ viết hoa bất thường giữa câu (không đầu dòng)
    text = re.sub(r'(?<=[a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ\s])[A-ZÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ][a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]+', fix_word, text)
    return text


def add_sentence_breaks(text: str) -> str:
    """Thêm dấu chấm và xuống dòng tại sentence boundaries."""

    # 1. Thêm dấu chấm sau sentence-ending particles
    for pattern in SENTENCE_ENDS:
        text = re.sub(pattern, lambda m: m.group(0) + '.', text, flags=re.IGNORECASE)

    # 2. Thêm dấu chấm + capitalize trước new sentence starters
    for starter in NEW_SENTENCE_STARTERS:
        # Nếu starter xuất hiện giữa câu (không sau dấu câu)
        pattern = r'(?<![.!?,\n])\s+(' + re.escape(starter) + r')'
        text = re.sub(pattern, r'. \1', text, flags=re.IGNORECASE)

    return text


def add_paragraph_breaks(text: str) -> str:
    """Thêm paragraph breaks tại topic transitions."""
    for trigger in PARA_BREAKS:
        pattern = r'(?<=[.!?])\s+(' + re.escape(trigger) + r')'
        text = re.sub(pattern, r'\n\n\1', text, flags=re.IGNORECASE)

    return text


def capitalize_sentences(text: str) -> str:
    """Capitalize đầu mỗi câu sau dấu chấm/xuống dòng."""
    lines = text.split('\n')
    result = []
    for line in lines:
        if not line.strip():
            result.append(line)
            continue
        # Capitalize đầu dòng
        line = line[0].upper() + line[1:] if line else line
        # Capitalize sau ". " hoặc "! " hoặc "? "
        line = re.sub(r'([.!?])\s+([a-záàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ])',
                      lambda m: m.group(1) + ' ' + m.group(2).upper(),
                      line)
        result.append(line)
    return '\n'.join(result)


def add_final_period(text: str) -> str:
    """Đảm bảo câu cuối có dấu chấm."""
    text = text.strip()
    if text and text[-1] not in '.!?':
        text += '.'
    return text


def format_script_body(raw_body: str) -> str:
    """Pipeline format toàn bộ."""
    text = raw_body.strip()
    text = fix_capitalization(text)
    text = add_sentence_breaks(text)
    text = add_paragraph_breaks(text)
    text = capitalize_sentences(text)
    text = add_final_period(text)
    # Clean up multiple spaces/newlines
    text = re.sub(r' {2,}', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def process_file(filepath: str) -> str:
    """Format 1 script file. Return 'formatted', 'skip', hoặc 'error'."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tìm body giữa 2 dấu --- (thứ 3 và thứ 4, vì frontmatter đã dùng 1-2)
    # Structure: ---\nfrontmatter\n---\n\n# Title\n\n**Topic:**...\n\n---\n\nbody\n\n---\n\n← link
    parts = content.split('\n---\n')
    if len(parts) < 3:
        return 'skip'

    # Body nằm ở parts[-2] (trước phần link cuối)
    body_raw = parts[-2].strip()

    # Kiểm tra xem body đã được format chưa (có dấu chấm không)
    period_count = body_raw.count('.')
    word_count = len(body_raw.split())
    if word_count > 0 and period_count / word_count > 0.05:
        return 'already_formatted'

    # Format body
    body_formatted = format_script_body(body_raw)

    # Ghép lại
    parts[-2] = '\n' + body_formatted + '\n'
    new_content = '\n---\n'.join(parts)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return 'formatted'


def process_folder(folder_path: str):
    """Format tất cả scripts trong 1 folder."""
    stats = {'formatted': 0, 'skip': 0, 'already': 0, 'error': 0}

    for fname in sorted(os.listdir(folder_path)):
        if not fname.endswith('.md') or fname.startswith('_'):
            continue
        fpath = os.path.join(folder_path, fname)
        try:
            result = process_file(fpath)
            if result == 'formatted':
                stats['formatted'] += 1
                print(f'  ✅ {fname[:55]}')
            elif result == 'already_formatted':
                stats['already'] += 1
            else:
                stats['skip'] += 1
        except Exception as e:
            stats['error'] += 1
            print(f'  ❌ {fname}: {e}')

    return stats


def main():
    # Bắt đầu với Thuỷ TH
    targets = [
        'VJ/VJ-Thuy/scripts/talking-head',
    ]

    total = {'formatted': 0, 'skip': 0, 'already': 0, 'error': 0}

    for rel_path in targets:
        folder = os.path.join(VAULT_ROOT, rel_path)
        print(f'\n📁 {rel_path}')
        stats = process_folder(folder)
        for k, v in stats.items():
            total[k] += v

    print(f'\n── TỔNG KẾT ──')
    print(f'Đã format:     {total["formatted"]}')
    print(f'Đã có format:  {total["already"]}')
    print(f'Bỏ qua:        {total["skip"]}')
    print(f'Lỗi:           {total["error"]}')


if __name__ == '__main__':
    main()
