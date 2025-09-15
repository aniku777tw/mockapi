#!/bin/bash

# 獲取 Railway 提供的 PORT 環境變量，如果沒有則使用默認值 8000
PORT=${PORT:-8000}

echo "Starting FastAPI server on port $PORT"

# 使用 uvicorn 啟動服務
uvicorn main:app --host 0.0.0.0 --port $PORT
