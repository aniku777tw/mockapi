#!/bin/bash

echo "🚀 FastAPI Mock API 部署腳本"
echo "================================"

# 檢查是否在正確的目錄
if [ ! -f "main.py" ]; then
    echo "❌ 錯誤：請在專案根目錄中運行此腳本"
    exit 1
fi

echo "📋 可用的部署選項："
echo "1. Railway (推薦)"
echo "2. Vercel"
echo "3. Docker 本地"
echo "4. Google Cloud Platform"
echo ""

read -p "請選擇部署方式 (1-4): " choice

case $choice in
    1)
        echo "🚀 準備部署到 Railway..."
        echo "請按照以下步驟："
        echo "1. 訪問 https://railway.app"
        echo "2. 使用 GitHub 登入"
        echo "3. 點擊 'New Project' → 'Deploy from GitHub repo'"
        echo "4. 選擇您的 mockApi 倉庫"
        echo "5. Railway 會自動部署"
        ;;
    2)
        echo "🚀 部署到 Vercel..."
        if ! command -v vercel &> /dev/null; then
            echo "安裝 Vercel CLI..."
            npm i -g vercel
        fi
        vercel --prod
        ;;
    3)
        echo "🐳 使用 Docker 本地部署..."
        echo "構建 Docker 鏡像..."
        docker build -t mockapi .
        echo "啟動容器..."
        docker run -d -p 8000:8000 --name mockapi-container mockapi
        echo "✅ 服務已啟動在 http://localhost:8000"
        echo "📖 API 文檔: http://localhost:8000/docs"
        ;;
    4)
        echo "☁️ 部署到 Google Cloud Platform..."
        if ! command -v gcloud &> /dev/null; then
            echo "❌ 請先安裝 Google Cloud CLI"
            exit 1
        fi
        gcloud app deploy
        ;;
    *)
        echo "❌ 無效的選擇"
        exit 1
        ;;
esac

echo ""
echo "🎉 部署完成！"
echo "📖 記得查看 README.md 獲取更多部署選項"
