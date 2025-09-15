"""
Package Routes

套裝旅遊行程相關的 API 路由 - 只保留 getPackage 功能
"""

from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from models.package import Package
from services.package_service import PackageService
from models.response import CustomResponse, Status, ErrorResponse

router = APIRouter(prefix="/packages", tags=["套裝旅遊行程"])

# 初始化服務
package_service = PackageService()


@router.get("/list", response_model=CustomResponse[List[Package], str])
async def get_packages(
    packageIds: str = Query(..., description="套裝旅遊行程 ID 列表，用逗號分隔"),
    activityStartDate: str = Query(..., description="活動開始日期 (YYYY-MM-DD 格式)"),
    locale: Optional[str] = Query("zh-tw", description="語言地區"),
    currency: Optional[str] = Query("TWD", description="貨幣"),
    isPreview: Optional[str] = Query("false", description="是否為預覽模式")
):
    """獲取多個套裝旅遊行程 - 根據 Request 參數表格"""
    try:
        # 驗證 packageIds 不能為空
        if not packageIds or not packageIds.strip():
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="packageIds 為必填參數，不能為空"),
                data={"field": "packageIds", "value": packageIds}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 activityStartDate 不能為空
        if not activityStartDate or not activityStartDate.strip():
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="activityStartDate 為必填參數，不能為空"),
                data={"field": "activityStartDate", "value": activityStartDate}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 驗證 activityStartDate 格式 (YYYY-MM-DD)
        try:
            datetime.strptime(activityStartDate, "%Y-%m-%d")
        except ValueError:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="activityStartDate 格式錯誤，請使用 YYYY-MM-DD 格式"),
                data={"field": "activityStartDate", "value": activityStartDate, "expectedFormat": "YYYY-MM-DD"}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 解析 packageIds 字串為整數列表
        try:
            package_id_list = [int(id.strip()) for id in packageIds.split(",") if id.strip()]
            if not package_id_list:
                error_response = ErrorResponse(
                    status=Status(code="CP01005", msg="packageIds 不能為空，請提供有效的套裝旅遊行程 ID"),
                    data={"field": "packageIds", "value": packageIds}
                )
                raise HTTPException(status_code=400, detail=error_response.dict())
        except ValueError:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="packageIds 格式錯誤，請使用逗號分隔的整數"),
                data={"field": "packageIds", "value": packageIds, "expectedFormat": "逗號分隔的整數"}
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        
        # 解析 isPreview 參數
        is_preview = isPreview.lower() == "true" if isPreview else False
        
        # 獲取多個套裝旅遊行程
        packages = []
        not_found_ids = []
        
        for package_id in package_id_list:
            package = package_service.get_package(package_id, is_preview=is_preview)
            if package:
                packages.append(package)
            else:
                not_found_ids.append(package_id)
        
        # 如果所有查詢的 package ID 都不存在，回傳 404 錯誤
        if not packages and not_found_ids:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="找不到指定的套裝旅遊行程"),
                data={"notFoundIds": not_found_ids, "requestedIds": package_id_list}
            )
            raise HTTPException(status_code=404, detail=error_response.dict())
        
        # 根據 locale 和 currency 進行處理（這裡可以添加價格轉換等邏輯）
        # 目前先返回原始數據
        
        return CustomResponse(
            status=Status(code="0", msg="success"),
            data=packages
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{package_id}", response_model=CustomResponse[Package, str])
async def get_package(
    package_id: int,
    isPreview: Optional[str] = Query("false", description="是否為預覽模式")
):
    """獲取單個套裝旅遊行程"""
    try:
        # 解析 isPreview 參數
        is_preview = isPreview.lower() == "true" if isPreview else False
        
        package = package_service.get_package(package_id, is_preview=is_preview)
        if not package:
            error_response = ErrorResponse(
                status=Status(code="CP01005", msg="套裝旅遊行程不存在"),
                data={"packageId": package_id}
            )
            raise HTTPException(status_code=404, detail=error_response.dict())
        
        return CustomResponse(
            status=Status(code="0", msg="success"),
            data=package
        )
    except HTTPException:
        raise
    except Exception as e:
        error_response = ErrorResponse(
            status=Status(code="CP01005", msg="伺服器內部錯誤"),
            data={"error": str(e)}
        )
        raise HTTPException(status_code=500, detail=error_response.dict())
