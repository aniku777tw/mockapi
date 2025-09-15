# Mock API Service

一個基於 FastAPI 的模擬 API 服務，支援多種雲端平台部署。

## 功能特色

- 🚀 基於 FastAPI 的高性能 API 服務
- 📝 完整的 CRUD 操作（用戶管理）
- 🔍 自動生成的 API 文檔（Swagger UI）
- 🐳 Docker 容器化支援
- ☁️ 多雲端平台部署配置
- 🔄 健康檢查和錯誤處理
- 🌐 CORS 支援

## API 端點

### 基本端點
- `GET /` - 歡迎訊息
- `GET /health` - 健康檢查
- `GET /docs` - Swagger UI 文檔
- `GET /redoc` - ReDoc 文檔

### 用戶管理
- `GET /users` - 獲取所有用戶
- `GET /users/{user_id}` - 根據 ID 獲取用戶
- `POST /users` - 創建新用戶
- `PUT /users/{user_id}` - 更新用戶
- `DELETE /users/{user_id}` - 刪除用戶

### 測試端點
- `GET /slow-api` - 模擬慢速 API（2秒延遲）
- `GET /error-api` - 模擬錯誤 API

## 本地開發

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 運行服務

```bash
# 開發模式
uvicorn main:app --reload

# 生產模式
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 使用 Docker

```bash
# 構建鏡像
docker build -t mockapi .

# 運行容器
docker run -p 8000:8000 mockapi

# 使用 docker-compose
docker-compose up --build
```

## 雲端部署

### 1. Railway 部署

1. 將代碼推送到 GitHub
2. 在 [Railway](https://railway.app) 連接 GitHub 倉庫
3. 選擇自動部署
4. 服務將自動構建並部署

### 2. Vercel 部署

1. 安裝 Vercel CLI：
   ```bash
   npm i -g vercel
   ```

2. 部署：
   ```bash
   vercel --prod
   ```

### 3. Google Cloud Platform 部署

1. 安裝 Google Cloud CLI
2. 初始化項目：
   ```bash
   gcloud init
   ```

3. 部署：
   ```bash
   gcloud app deploy
   ```

### 4. Heroku 部署

1. 安裝 Heroku CLI
2. 創建應用：
   ```bash
   heroku create your-app-name
   ```

3. 部署：
   ```bash
   git push heroku main
   ```

### 5. AWS Elastic Beanstalk 部署

1. 安裝 EB CLI
2. 初始化：
   ```bash
   eb init
   ```

3. 創建環境：
   ```bash
   eb create production
   ```

4. 部署：
   ```bash
   eb deploy
   ```

## 環境變量

- `PORT`: 服務端口（默認：8000）

## 項目結構

```
mockApi/
├── main.py                 # 主應用文件
├── requirements.txt        # Python 依賴
├── Dockerfile             # Docker 配置
├── docker-compose.yml     # Docker Compose 配置
├── railway.json          # Railway 部署配置
├── vercel.json           # Vercel 部署配置
├── app.yaml              # Google Cloud 部署配置
├── .github/workflows/    # GitHub Actions 配置
└── README.md             # 項目說明
```

## 開發建議

1. 在生產環境中，請修改 CORS 設置以限制允許的域名
2. 添加適當的日誌記錄
3. 實施身份驗證和授權
4. 添加數據庫持久化存儲
5. 設置監控和警報

## 授權

MIT License
