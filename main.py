from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os

# 創建 FastAPI 實例
app = FastAPI(
    title="Mock API Service",
    description="一個用於模擬 API 的 FastAPI 服務",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 添加 CORS 中間件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生產環境中應該設置具體的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 數據模型
class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    age: Optional[int] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None

class Message(BaseModel):
    message: str

# 模擬數據庫
users_db = []
user_id_counter = 1

# 根路由
@app.get("/", response_model=Message)
async def root():
    return {"message": "歡迎使用 Mock API 服務！"}

# 健康檢查
@app.get("/health", response_model=Message)
async def health_check():
    return {"message": "服務運行正常"}

# 獲取所有用戶
@app.get("/users", response_model=List[UserResponse])
async def get_users():
    return users_db

# 根據 ID 獲取用戶
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = next((user for user in users_db if user["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="用戶不存在")
    return user

# 創建新用戶
@app.post("/users", response_model=UserResponse)
async def create_user(user: User):
    global user_id_counter
    new_user = {
        "id": user_id_counter,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
    users_db.append(new_user)
    user_id_counter += 1
    return new_user

# 更新用戶
@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: User):
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="用戶不存在")
    
    users_db[user_index] = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }
    return users_db[user_index]

# 刪除用戶
@app.delete("/users/{user_id}", response_model=Message)
async def delete_user(user_id: int):
    user_index = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    if user_index is None:
        raise HTTPException(status_code=404, detail="用戶不存在")
    
    users_db.pop(user_index)
    return {"message": f"用戶 {user_id} 已刪除"}

# 模擬延遲的 API
@app.get("/slow-api", response_model=Message)
async def slow_api():
    import asyncio
    await asyncio.sleep(2)  # 模擬 2 秒延遲
    return {"message": "這是一個慢速 API 響應"}

# 模擬錯誤的 API
@app.get("/error-api", response_model=Message)
async def error_api():
    raise HTTPException(status_code=500, detail="模擬服務器錯誤")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
