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

class NormalCaseRequest(BaseModel):
    roomCount: int
    currency: str
    isActivity: bool
    activityStartDate: str
    consumerEmail: str
    consumerCountryId: int
    affiliateConversionId: Optional[str] = None
    coupon: str
    locale: str
    events: Optional[str] = None
    residentCountryCode: str
    # Normal case 欄位
    people: Optional[List[dict]] = None
    thsr: Optional[dict] = None
    roomId: Optional[int] = None
    ratePlanId: Optional[str] = None

class PackageCaseRequest(BaseModel):
    roomCount: int
    currency: str
    isActivity: bool
    activityStartDate: str
    consumerEmail: str
    consumerCountryId: int
    affiliateConversionId: Optional[str] = None
    coupon: str
    locale: str
    events: Optional[str] = None
    residentCountryCode: str
    # Package case 欄位
    singleCount: Optional[int] = None
    ticketCount: Optional[List[TicketCount]] = None
    combinationOptionId: Optional[str] = None

# 使用 Union 來支援兩種請求類型
from typing import Union
OrderPreviewRequest = Union[NormalCaseRequest, PackageCaseRequest]

router = APIRouter(prefix="/order", tags=["訂單"])

# 初始化服務
order_service = OrderService()

@router.post("/preview")
async def preview_order(request_body: dict = Body(...)):
    """預覽訂單"""
    try:
        # 檢查請求類型 (只檢查 key 是否存在，不管值是什麼)
        has_normal_case = any(key in request_body for key in ["people", "thsr", "roomId", "ratePlanId"])
        has_package_case = any(key in request_body for key in ["singleCount", "ticketCount", "combinationOptionId"])
        
        if has_normal_case and has_package_case:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="normal case 欄位與 package case 欄位不能同時存在"),
                data={
                    "normalCaseFields": {
                        "people": request_body.get("people") is not None,
                        "thsr": request_body.get("thsr") is not None,
                        "roomId": request_body.get("roomId") is not None,
                        "ratePlanId": request_body.get("ratePlanId") is not None
                    },
                    "packageCaseFields": {
                        "singleCount": request_body.get("singleCount") is not None,
                        "ticketCount": request_body.get("ticketCount") is not None,
                        "combinationOptionId": request_body.get("combinationOptionId") is not None
                    }
                }
            )
            raise HTTPException(status_code=400, detail=error_response.model_dump())
        
        # 驗證 singleCount 和 ticketCount 互斥性
        if request_body.get("singleCount") is not None and request_body.get("ticketCount") is not None:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="singleCount 和 ticketCount 其中一者為 null"),
                data={
                    "singleCount": request_body.get("singleCount"),
                    "ticketCount": request_body.get("ticketCount")
                }
            )
            raise HTTPException(status_code=400, detail=error_response.model_dump())

        if request_body.get("singleCount") is None and request_body.get("ticketCount") is None:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="singleCount 和 ticketCount 不能同時為 null"),
                data={
                    "singleCount": request_body.get("singleCount"),
                    "ticketCount": request_body.get("ticketCount")
                }
            )
            raise HTTPException(status_code=400, detail=error_response.model_dump())
        
        # 使用服務取得對應的 mock 資料
        mock_data = order_service.preview_order(request_body)
        
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