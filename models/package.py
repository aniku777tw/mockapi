"""
Package Models

套裝旅遊行程相關的數據模型 - 只保留 getPackage 需要的模型
"""

from pydantic import BaseModel
from typing import List, Optional
from constants.pricing import PricingMethod


class Package(BaseModel):
    """套裝旅遊行程模型 - 對應 TypeScript Package 型別"""
    id: int
    name: str
    bnbId: int
    isSoldOut: bool
    lowestPrice: Optional[int] = None
    pricingMethod: PricingMethod


class GetPackagesData(BaseModel):
    """獲取多個套裝旅遊行程的回應資料"""
    packages: List[Package]
