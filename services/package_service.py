"""
Package Service

套裝旅遊行程管理服務模組 - 只保留 getPackage 功能
"""

from typing import Optional
from models.package import Package


class PackageService:
    """套裝旅遊行程管理服務類別"""
    
    def __init__(self):
        """初始化 Package Service"""
        # 模擬數據庫 - 只創建一個 BNB，有 8 個套裝旅遊行程
        self._packages = []
        package_id = 1
        
        # BNB 1: 台北101 (8個套裝旅遊行程)
        bnb1_packages = [
            {"name": "台北101觀景台一日遊", "isSoldOut": False, "lowestPrice": 600, "pricingMethod": "ticket"},
            {"name": "台北101美食文化體驗", "isSoldOut": False, "lowestPrice": 800, "pricingMethod": "single"},
            {"name": "台北101紀念品採購行程", "isSoldOut": True, "lowestPrice": None, "pricingMethod": "single"},
            {"name": "台北101深度導覽行程", "isSoldOut": False, "lowestPrice": 1200, "pricingMethod": "ticket"},
            {"name": "台北101專業攝影行程", "isSoldOut": False, "lowestPrice": 1500, "pricingMethod": "single"},
            {"name": "台北101 VIP 尊榮體驗", "isSoldOut": False, "lowestPrice": 3000, "pricingMethod": "ticket"},
            {"name": "台北101夜間觀景行程", "isSoldOut": False, "lowestPrice": 500, "pricingMethod": "ticket"},
            {"name": "台北101+故宮聯票", "isSoldOut": False, "lowestPrice": 1800, "pricingMethod": "ticket"}
        ]
        
        for pkg in bnb1_packages:
            self._packages.append(Package(
                id=package_id,
                name=pkg["name"],
                bnbId=66632,
                isSoldOut=pkg["isSoldOut"],
                lowestPrice=pkg["lowestPrice"],
                pricingMethod=pkg["pricingMethod"]
            ))
            package_id += 1
    
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
