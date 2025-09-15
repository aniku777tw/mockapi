"""
Response Models

回應相關的數據模型
"""

from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Dict, Any

# 型別變量
CodeType = TypeVar('CodeType', bound=str)
DataType = TypeVar('DataType')

# 基礎狀態模型
class Status(BaseModel, Generic[CodeType]):
    code: str
    msg: str

# 自定義回應模型
class CustomResponse(BaseModel, Generic[DataType, CodeType]):
    status: Status[CodeType]
    data: DataType

# 錯誤回應模型
class ErrorResponse(BaseModel, Generic[CodeType]):
    status: Status[CodeType]
    data: Dict[str, Any] = {}

# 簡單的訊息模型
class Message(BaseModel):
    message: str
