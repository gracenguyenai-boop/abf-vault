#!/bin/bash
# vault-reader.sh — đọc raw markdown từ GitHub private repo
# Usage: ./vault-reader.sh "MOC-MASTER.md"
#        ./vault-reader.sh "TD-TraDa/TD-MOC/TD-L3-TC-MOC.md"
# Cần: export GITHUB_TOKEN=ghp_...

REPO="gracenguyenai-boop/abf-vault"
FILE_PATH="$1"

if [ -z "$GITHUB_TOKEN" ]; then
  echo "ERROR: GITHUB_TOKEN chưa set. Chạy: export GITHUB_TOKEN=ghp_..." >&2
  exit 1
fi

if [ -z "$FILE_PATH" ]; then
  echo "Usage: $0 <file-path>" >&2
  exit 1
fi

curl -sf \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3.raw" \
  "https://api.github.com/repos/$REPO/contents/$FILE_PATH"
