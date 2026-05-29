#!/bin/bash
# sync.sh — đồng bộ ABF-Vault lên GitHub
# Usage: ./sync.sh
#        ./sync.sh "message tùy chỉnh"

cd ~/Downloads/ABF-Vault

MSG="${1:-update vault $(date '+%Y-%m-%d %H:%M')}"

echo "📦 Staging changes..."
git add .

CHANGED=$(git diff --cached --name-only | wc -l | tr -d ' ')

if [ "$CHANGED" -eq 0 ]; then
  echo "✅ Không có gì thay đổi, vault đã up-to-date."
  exit 0
fi

echo "📝 $CHANGED file(s) thay đổi"
git diff --cached --name-only

echo ""
git commit -m "$MSG"
echo ""

echo "🚀 Pushing lên GitHub..."
git push

echo ""
echo "✅ Sync xong: $CHANGED file(s) — $MSG"
