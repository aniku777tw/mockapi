"""
價格計算服務
"""

from typing import Optional
from models.price import PostPackagePriceData, Package, Combination, TicketCount
from services.package_service import PackageService
from services.module_service import ModuleService
from constants.activity_package_module import TICKET_TYPE

class PriceService:
    """價格計算服務類別"""
    
    def __init__(self):
        """初始化 Price Service"""
        self.package_service = PackageService()
        self.module_service = ModuleService()
    
    def calculate_package_price(
        self, 
        activity_id: int, 
        package_id: int, 
        combination_option_id: str,
        single_count: Optional[int] = None,
        ticket_count: Optional[list] = None
    ) -> Optional[PostPackagePriceData]:
        """計算套裝旅遊行程價格"""
        
        # 獲取套裝旅遊行程資訊
        package = self.package_service.get_package(package_id, is_preview=False)
        if not package:
            return None
        
        # 獲取模組資料
        modules_data = self.module_service.get_package_modules(activity_id, package_id, is_preview=False)
        if not modules_data:
            return None
        
        # 找到對應的組合
        target_combination = None
        for combo in modules_data.availableCombinations:
            if combo.combinationOptionId == combination_option_id:
                target_combination = combo
                break
        
        if not target_combination:
            return None
        
        # 計算價格
        total_price = 0
        
        if single_count and target_combination.singleOffering:
            # Single pricing
            total_price = target_combination.singleOffering.price * single_count
        elif ticket_count and target_combination.ticketOffering:
            # Ticket pricing
            for ticket_req in ticket_count:
                for ticket_offering in target_combination.ticketOffering:
                    if ticket_offering.id == ticket_req["id"]:
                        total_price += ticket_offering.price * ticket_req["count"]
                        break
        
        # 構建 optionsMap (從 moduleOptionIds 轉換為選項名稱)
        options_map = []
        for option_id in target_combination.moduleOptionIds:
            if option_id:
                # 從模組資料中找到對應的選項名稱
                option_name = self._find_option_name(modules_data.modules, option_id)
                options_map.append(option_name if option_name else str(option_id))
            else:
                options_map.append(None)
        
        return PostPackagePriceData(
            package=Package(
                id=package.id,
                name=package.name
            ),
            combination=Combination(
                combinationOptionId=target_combination.combinationOptionId,
                optionsMap=options_map
            ),
            defaultPrice=total_price,
            useDiscount=False,  # 測試資料固定為 false
            discountPrice=0  # 測試資料固定為 0
        )
    
    def _find_option_name(self, modules, option_id):
        """從模組資料中找到選項名稱"""
        for module in modules:
            for option in module.options:
                if option.id == option_id:
                    return option.name
        return None
