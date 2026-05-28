# GitHub Source Config

Repo: https://github.com/gracenguyenai-boop/abf-vault (private)
Branch: main
Local path: ~/Downloads/ABF-Vault/

## Đọc raw markdown qua GitHub API

```bash
# Cần env var: GITHUB_TOKEN=ghp_...
curl -s \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3.raw" \
  "https://api.github.com/repos/gracenguyenai-boop/abf-vault/contents/{PATH}"
```

Ví dụ đọc MOC-MASTER:
```bash
curl -s \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3.raw" \
  "https://api.github.com/repos/gracenguyenai-boop/abf-vault/contents/MOC-MASTER.md"
```

## Vì sao dùng API thay vì web/HTML

- `Accept: application/vnd.github.v3.raw` → trả về markdown thuần, không có HTML wrapper
- Không tốn token parse HTML
- Không nhầm frontmatter, wikilinks `[[...]]` vẫn nguyên vẹn
- Obsidian Publish / GitHub Pages → trả HTML → phải strip tags → mất metadata

## List files trong một branch/folder

```bash
curl -s \
  -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/gracenguyenai-boop/abf-vault/contents/TD-TraDa/TD-MOC" \
  | python3 -c "import sys,json; [print(f['path']) for f in json.load(sys.stdin)]"
```

## Sync workflow

1. Edit note trong Obsidian (local)
2. `git add . && git commit -m "..." && git push` từ vault root
3. Workflow/agent đọc từ GitHub API → luôn có bản mới nhất
