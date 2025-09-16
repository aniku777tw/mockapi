"""
價格計算相關的 API 路由
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from datetime import datetime
from models.price import PostPackagePriceRequest, PostPackagePriceData
from models.response import CustomResponse, Status, ErrorResponse
from services.price_service import PriceService

router = APIRouter(prefix="/activity", tags=["價格計算"])

# 初始化服務
price_service = PriceService()

@router.post("/{activity_id}/packages/{package_id}/price", response_model=CustomResponse[PostPackagePriceData, str])
async def calculate_package_price(
    activity_id: int,
    package_id: int,
    request: PostPackagePriceRequest
):
    """計算套裝旅遊行程價格"""
    try:
        # 驗證 activity_id 必須為正整數
        if activity_id <= 0:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="activityId 必須為正整數"),
                data={"field": "activityId", "value": activity_id}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 package_id 必須為正整數
        if package_id <= 0:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="packageId 必須為正整數"),
                data={"field": "packageId", "value": package_id}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 activityStartDate 不能為空
        if not request.activityStartDate or not request.activityStartDate.strip():
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="activityStartDate 為必填參數，不能為空"),
                data={"field": "activityStartDate", "value": request.activityStartDate}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 activityStartDate 格式 (YYYY-MM-DD)
        try:
            datetime.strptime(request.activityStartDate, "%Y-%m-%d")
        except ValueError:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="activityStartDate 格式錯誤，請使用 YYYY-MM-DD 格式"),
                data={"field": "activityStartDate", "value": request.activityStartDate, "expectedFormat": "YYYY-MM-DD"}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 combinationOptionId 不能為空
        if not request.combinationOptionId or not request.combinationOptionId.strip():
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="combinationOptionId 為必填參數，不能為空"),
                data={"field": "combinationOptionId", "value": request.combinationOptionId}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 singleCount 和 ticketCount 不能同時為空
        if not request.singleCount and not request.ticketCount:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="singleCount 和 ticketCount 至少需要提供一個"),
                data={"singleCount": request.singleCount, "ticketCount": request.ticketCount}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 singleCount 和 ticketCount 不能同時提供
        if request.singleCount and request.ticketCount:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="singleCount 和 ticketCount 不能同時提供"),
                data={"singleCount": request.singleCount, "ticketCount": request.ticketCount}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 singleCount 必須為正整數
        if request.singleCount is not None and request.singleCount <= 0:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="singleCount 必須為正整數"),
                data={"field": "singleCount", "value": request.singleCount}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 ticketCount 格式
        if request.ticketCount:
            for i, ticket in enumerate(request.ticketCount):
                if ticket.count < 0:
                    error_response = ErrorResponse(
                        status=Status(code="CP01005", msg=f"ticketCount[{i}].count 不能為負數"),
                        data={"field": f"ticketCount[{i}].count", "value": ticket.count}
                    )
                    raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 計算價格
        price_data = price_service.calculate_package_price(
            activity_id=activity_id,
            package_id=package_id,
            combination_option_id=request.combinationOptionId,
            single_count=request.singleCount,
            ticket_count=[ticket.dict() for ticket in request.ticketCount] if request.ticketCount else None
        )
        
        if not price_data:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="找不到指定的套裝旅遊行程或組合選項"),
                data={"activityId": activity_id, "packageId": package_id, "combinationOptionId": request.combinationOptionId}
            )
            raise HTTPException(status_code=404, detail=error_response.dict())
        
        return CustomResponse(
            status=Status(code="0", msg="success"),
            data=price_data
        )
        
    except HTTPException:
        raise
    except Exception as e:
        error_response = ErrorResponse(
            status=Status(code="CP50001", msg="伺服器內部錯誤"),
            data={"error": str(e)}
        )
        raise HTTPException(status_code=500, detail=error_response.dict())
