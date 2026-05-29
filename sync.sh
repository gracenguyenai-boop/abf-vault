#!/bin/bash
# sync.sh — đồng bộ ABF-Vault lên GitHub (chắc chắn, không sai sót)
# Usage: ./sync.sh
#        ./sync.sh "mô tả thay đổi"

set -e  # dừng ngay nếu bất kỳ lệnh nào lỗi
cd ~/Downloads/ABF-Vault

echo "🔄 Bước 1/4: Pull từ GitHub (tránh conflict)..."
git pull origin main
echo ""

echo "📦 Bước 2/4: Stage tất cả thay đổi..."
git add .

CHANGED=$(git diff --cached --name-only | wc -l | tr -d ' ')

if [ "$CHANGED" -eq 0 ]; then
  echo "✅ Không có gì thay đổi, vault đã up-to-date."
  exit 0
fi

echo "📝 $CHANGED file(s) thay đổi:"
git diff --cached --name-only
echo ""

MSG="${1:-update vault $(date '+%Y-%m-%d %H:%M')}"
echo "💬 Bước 3/4: Commit — \"$MSG\""
git commit -m "$MSG"
echo ""

echo "🚀 Bước 4/4: Push lên GitHub..."
git push origin main
echo ""

echo "🔍 Verify — trạng thái cuối:"
git status
echo ""
git log --oneline -3
echo ""
echo "✅ Sync hoàn tất: $CHANGED file(s)"
