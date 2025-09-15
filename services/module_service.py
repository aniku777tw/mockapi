"""
Module Service

套裝旅遊行程模組管理服務
"""

from typing import Optional
from models.module import Module, ModuleOption, AvailableCombination, SingleOffering, TicketOffering, GetPackageModulesData
from constants.activity_package_module import INVENTORY_STATUS, TICKET_TYPE
from data.module_mock_data import MODULES_MOCK_DATA


class ModuleService:
    """套裝旅遊行程模組管理服務類別"""
    
    def __init__(self):
        """初始化 Module Service"""
        # 使用分離的測試資料
        self._modules_data = MODULES_MOCK_DATA
    
    def get_package_modules(self, activity_id: int, package_id: int, is_preview: bool = False) -> Optional[GetPackageModulesData]:
        """獲取套裝旅遊行程模組數據"""
        if package_id not in self._modules_data:
            return None
        
        data = self._modules_data[package_id]
        
        # 轉換可用組合數據
        available_combinations = []
        for combo_data in data["availableCombinations"]:
            single_offering = None
            if combo_data["singleOffering"]:
                single_offering = SingleOffering(**combo_data["singleOffering"])
            
            ticket_offering = None
            if combo_data["ticketOffering"]:
                # 處理票券數據，成人票不包含 age 欄位
                processed_tickets = []
                for ticket in combo_data["ticketOffering"]:
                    # 如果是成人票 (id=4)，移除 age 欄位
                    if ticket["id"] == TICKET_TYPE["ADULT"]:
                        ticket_data = {k: v for k, v in ticket.items() if k != "age"}
                    else:
                        ticket_data = ticket
                    processed_tickets.append(TicketOffering(**ticket_data))
                ticket_offering = processed_tickets
            
            # 如果是預覽模式，將價格設為 0
            if is_preview:
                if single_offering:
                    single_offering.price = 0
                if ticket_offering:
                    for ticket in ticket_offering:
                        ticket.price = 0
            
            available_combinations.append(AvailableCombination(
                combinationOptionId=combo_data["combinationOptionId"],
                moduleOptionIds=combo_data["moduleOptionIds"],
                singleOffering=single_offering,
                ticketOffering=ticket_offering
            ))
        
        # 轉換模組數據，並根據可用組合動態計算 inventoryStatus
        modules = []
        for module_data in data["modules"]:
            options = []
            for option_data in module_data["options"]:
                # 檢查該選項是否有可用的組合
                has_available_combination = self._check_option_availability(
                    option_data["id"], available_combinations
                )
                
                # 動態計算庫存狀態
                if not has_available_combination:
                    # 如果沒有可用組合，檢查原始狀態
                    if option_data["inventoryStatus"] == INVENTORY_STATUS["SOLD_OUT"]:
                        # 如果原始狀態是 SOLD_OUT，保持 SOLD_OUT
                        inventory_status = INVENTORY_STATUS["SOLD_OUT"]
                    else:
                        # 否則設為 NO_COMBINATION
                        inventory_status = INVENTORY_STATUS["NO_COMBINATION"]
                else:
                    # 如果有可用組合，使用原始資料中的狀態（可能是 BOOKABLE 或 SOLD_OUT）
                    inventory_status = option_data["inventoryStatus"]
                
                options.append(ModuleOption(
                    id=option_data["id"],
                    name=option_data["name"],
                    inventoryStatus=inventory_status
                ))
            
            modules.append(Module(
                id=module_data["id"],
                name=module_data["name"],
                isShowEmpty=module_data["isShowEmpty"],
                options=options
            ))
        
        return GetPackageModulesData(
            modules=modules,
            availableCombinations=available_combinations
        )
    
    def _check_option_availability(self, option_id: int, available_combinations: list) -> bool:
        """檢查選項是否有可用的組合"""
        for combo in available_combinations:
            if option_id in combo.moduleOptionIds:
                return True
        return False
