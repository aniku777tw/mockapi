"""
Module Routes

套裝旅遊行程模組相關的 API 路由
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models.module import GetPackageModulesData
from models.response import CustomResponse, Status, ErrorResponse
from services.module_service import ModuleService

router = APIRouter(prefix="/activity", tags=["套裝旅遊行程模組"])

# 初始化服務
module_service = ModuleService()


@router.get("/{activity_id}/package/{package_id}/modules", response_model=CustomResponse[GetPackageModulesData, str])
async def get_package_modules(
    activity_id: int,
    package_id: int,
    activityStartDate: str = Query(..., description="活動開始日期 (YYYY-MM-DD 格式)"),
    locale: Optional[str] = Query("zh-tw", description="語言地區"),
    currency: Optional[str] = Query("TWD", description="貨幣"),
    isPreview: Optional[str] = Query("false", description="是否為預覽模式")
):
    """獲取套裝旅遊行程模組數據"""
    try:
        # 驗證 activityStartDate 不能為空
        if not activityStartDate or not activityStartDate.strip():
            error_response = ErrorResponse(
                status=Status(code="400", msg="activityStartDate 為必填參數，不能為空"),
                data={"field": "activityStartDate", "value": activityStartDate}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 activityStartDate 格式 (YYYY-MM-DD)
        from datetime import datetime
        try:
            datetime.strptime(activityStartDate, "%Y-%m-%d")
        except ValueError:
            error_response = ErrorResponse(
                status=Status(code="400", msg="activityStartDate 格式錯誤，請使用 YYYY-MM-DD 格式"),
                data={"field": "activityStartDate", "value": activityStartDate, "expectedFormat": "YYYY-MM-DD"}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 解析 isPreview 參數
        is_preview = isPreview.lower() == "true" if isPreview else False
        
        # 獲取套裝旅遊行程模組數據
        modules_data = module_service.get_package_modules(activity_id, package_id, is_preview=is_preview)
        
        if not modules_data:
            error_response = ErrorResponse(
                status=Status(code="404", msg="套裝旅遊行程模組不存在"),
                data={"activityId": activity_id, "packageId": package_id}
            )
            raise HTTPException(status_code=404, detail=error_response.dict())
        
        return CustomResponse(
            status=Status(code="0", msg="success"),
            data=modules_data
        )
    except HTTPException:
        raise
    except Exception as e:
        error_response = ErrorResponse(
            status=Status(code="500", msg="伺服器內部錯誤"),
            data={"error": str(e)}
        )
        raise HTTPException(status_code=500, detail=error_response.dict())
