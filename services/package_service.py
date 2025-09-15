"""
Package Service

套裝旅遊行程管理服務模組 - 只保留 getPackage 功能
"""

from typing import Optional
from models.package import Package
from data.package_mock_data import PACKAGES_MOCK_DATA


class PackageService:
    """套裝旅遊行程管理服務類別"""
    
    def __init__(self):
        """初始化 Package Service"""
        # 使用分離的測試資料
        self._packages = [Package(**pkg_data) for pkg_data in PACKAGES_MOCK_DATA]
    
    def get_package(self, package_id: int, is_preview: bool = False) -> Optional[Package]:
        """獲取單個套裝旅遊行程"""
        for package in self._packages:
            if package.id == package_id:
                # 如果是預覽模式，將 lowestPrice 設為 0
                if is_preview:
                    # 創建一個新的 Package 實例，修改 lowestPrice
                    return Package(
                        id=package.id,
                        name=package.name,
                        bnbId=package.bnbId,
                        isSoldOut=package.isSoldOut,
                        lowestPrice=0,  # 預覽模式下所有套裝旅遊行程都顯示 0
                        pricingMethod=package.pricingMethod
                    )
                return package
        return None
