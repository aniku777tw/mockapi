"""
Module Models

套裝旅遊行程模組相關的數據模型
"""

from pydantic import BaseModel
from typing import List, Optional, Union
from constants.activity_package_module import INVENTORY_STATUS, TICKET_TYPE


class ModuleOption(BaseModel):
    """模組選項"""
    id: int
    name: str
    inventoryStatus: int  # ValueOf<typeof INVENTORY_STATUS>


class Module(BaseModel):
    """模組"""
    id: int
    name: str
    isShowEmpty: bool
    options: List[ModuleOption]


class SingleOffering(BaseModel):
    """單一商品"""
    name: str
    unitCount: int
    inventory: int
    price: int


class TicketOffering(BaseModel):
    """票券商品"""
    id: int  # ValueOf<typeof TICKET_TYPE>
    age: Optional[int] = None
    inventory: int
    price: int
    
    class Config:
        exclude_none = True  # 排除 None 值


class AvailableCombination(BaseModel):
    """可用組合"""
    combinationOptionId: str
    moduleOptionIds: List[Optional[int]]
    singleOffering: Optional[SingleOffering] = None
    ticketOffering: Optional[List[TicketOffering]] = None


class GetPackageModulesData(BaseModel):
    """獲取套裝旅遊行程模組數據"""
    modules: List[Module]
    availableCombinations: List[AvailableCombination]
