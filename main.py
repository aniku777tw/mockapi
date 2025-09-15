from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import uvicorn
import os
from models.response import CustomResponse, Status, Message, ErrorResponse

# 創建 FastAPI 實例
app = FastAPI(
    title="Package Service API",
    description="套裝旅遊行程管理 API 服務",
    version="1.0.0"
)

# 註冊路由
from api.package_routes import router as package_router
app.include_router(package_router)

# 自定義異常處理器
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """處理 HTTP 異常，直接返回 ErrorResponse 格式"""
    if isinstance(exc.detail, dict) and "status" in exc.detail:
        # 如果 detail 已經是 ErrorResponse 格式，直接返回
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )
    else:
        # 如果是普通錯誤訊息，包裝成 ErrorResponse 格式
        error_response = ErrorResponse(
            status=Status(code=str(exc.status_code), msg=str(exc.detail)),
            data={}
        )
        return JSONResponse(
            status_code=exc.status_code,
            content=error_response.dict()
        )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """處理請求驗證錯誤，返回 ErrorResponse 格式"""
    # 提取第一個錯誤訊息
    if exc.errors():
        first_error = exc.errors()[0]
        field_name = ".".join(str(loc) for loc in first_error["loc"])
        error_msg = first_error["msg"]
        
        error_response = ErrorResponse(
            status=Status(code="422", msg=f"{field_name}: {error_msg}"),
            data={"field": field_name, "errors": exc.errors()}
        )
    else:
        error_response = ErrorResponse(
            status=Status(code="422", msg="請求參數驗證失敗"),
            data={"errors": exc.errors()}
        )
    
    return JSONResponse(
        status_code=422,
        content=error_response.dict()
    )

# 根路由
@app.get("/", response_model=CustomResponse[Message, str])
async def root():
    return CustomResponse(
        status=Status(code="0", msg="success"),
        data=Message(message="Health Check API 服務運行中")
    )

# 健康檢查
@app.get("/health", response_model=CustomResponse[Message, str])
async def health_check():
    return CustomResponse(
        status=Status(code="0", msg="success"),
        data=Message(message="服務運行正常")
    )

# 錯誤範例端點
@app.get("/error", response_model=CustomResponse[Message, str])
async def error_example():
    return CustomResponse(
        status=Status(code="500", msg="internal_server_error"),
        data=Message(message="這是一個錯誤範例")
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
