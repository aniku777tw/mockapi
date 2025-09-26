"""
訂單相關的 API 路由
"""

from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from typing import List, Optional
from models.response import CustomResponse, Status, ErrorResponse
from services.order_service import OrderService

class TicketCount(BaseModel):
    id: int
    count: int

class OrderPreviewRequest(BaseModel):
    roomCount: int
    singleCount: Optional[int] = None
    ticketCount: Optional[List[TicketCount]] = None
    currency: str
    combinationOptionId: Optional[str] = None
    isActivity: bool
    activityStartDate: str
    consumerEmail: str
    consumerCountryId: int
    affiliateConversionId: Optional[str] = None
    coupon: str
    locale: str
    events: Optional[str] = None
    residentCountryCode: str
    # Normal case 欄位 (optional)
    people: Optional[List[dict]] = None
    thsr: Optional[dict] = None
    roomId: Optional[int] = None
    ratePlanId: Optional[str] = None

router = APIRouter(prefix="/order", tags=["訂單"])

# 初始化服務
order_service = OrderService()

@router.post("/preview")
async def preview_order(request_body: OrderPreviewRequest = Body(...)):
    """預覽訂單"""
    try:
        # 驗證欄位互斥性
        normal_case_fields = [request_body.people, request_body.thsr, request_body.roomId, request_body.ratePlanId]
        package_case_fields = [request_body.singleCount, request_body.ticketCount, request_body.combinationOptionId]
        
        # 檢查是否有 normal case 欄位
        has_normal_case = any(field is not None for field in normal_case_fields)
        # 檢查是否有 package case 欄位
        has_package_case = any(field is not None for field in package_case_fields)
        
        if has_normal_case and has_package_case:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="normal case 欄位與 package case 欄位不能同時存在"),
                data={
                    "normalCaseFields": {
                        "people": request_body.people is not None,
                        "thsr": request_body.thsr is not None,
                        "roomId": request_body.roomId is not None,
                        "ratePlanId": request_body.ratePlanId is not None
                    },
                    "packageCaseFields": {
                        "singleCount": request_body.singleCount is not None,
                        "ticketCount": request_body.ticketCount is not None,
                        "combinationOptionId": request_body.combinationOptionId is not None
                    }
                }
            )
            raise HTTPException(status_code=400, detail=error_response.model_dump())
        
        # 驗證 singleCount 和 ticketCount 互斥性
        if request_body.singleCount is not None and request_body.ticketCount is not None:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="singleCount 和 ticketCount 其中一者為 null"),
                data={
                    "singleCount": request_body.singleCount,
                    "ticketCount": request_body.ticketCount
                }
            )
            raise HTTPException(status_code=400, detail=error_response.model_dump())
        
        # 使用服務取得對應的 mock 資料
        mock_data = order_service.preview_order(request_body.model_dump())
        
        return CustomResponse(
            status=Status(code="0", msg="success"),
            data=mock_data
        )
    except HTTPException:
        raise
    except Exception as e:
        error_response = ErrorResponse(
            status=Status(code="CP50001", msg="伺服器內部錯誤"),
            data={"error": str(e)}
        )
        raise HTTPException(status_code=500, detail=error_response.dict())