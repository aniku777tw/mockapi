"""
Pricing Constants

定價方法常數定義
"""

from typing import Literal

# 定價方法常數
PRICING_METHOD = {
    "TICKET": "ticket",
    "SINGLE": "single",
}

# 定價方法型別
PricingMethod = Literal["ticket", "single"]
