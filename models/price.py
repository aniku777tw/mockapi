"""
價格計算相關的 Pydantic 模型
"""

from pydantic import BaseModel
from typing import List, Optional
from constants.activity_package_module import TICKET_TYPE
from constants.locales import Locale
from constants.currency import Currency

class TicketCount(BaseModel):
    """票券數量"""
    id: int  # ValueOf<typeof TICKET_TYPE>
    count: int

class PostPackagePriceRequest(BaseModel):
    """套裝旅遊行程價格計算請求"""
    activityStartDate: str
    combinationOptionId: str
    locale: Optional[Locale] = None
    currency: Optional[Currency] = None
    singleCount: Optional[int] = None  # 如果 single 則會有這個 key，反之則沒有
    ticketCount: Optional[List[TicketCount]] = None  # 如果 ticket 則會有這個 key，反之則沒有

class Package(BaseModel):
    """套裝旅遊行程基本資訊"""
    id: int
    name: str

class Combination(BaseModel):
    """組合選項"""
    combinationOptionId: str
    optionsMap: List[Optional[str]]

class PostPackagePriceData(BaseModel):
    """套裝旅遊行程價格計算回應資料"""
    package: Package
    combination: Combination
    defaultPrice: int
    useDiscount: Optional[bool] = False  # 測試資料先固定為 false
    discountPrice: Optional[int] = 0  # 測試資料先固定為 0
