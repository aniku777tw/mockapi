"""
Currency Constants

貨幣常數定義
"""

from typing import Literal

# 貨幣常數
CURRENCY_JPY = "JPY"
CURRENCY_KRW = "KRW"
CURRENCY_TWD = "TWD"
CURRENCY_THB = "THB"
CURRENCY_USD = "USD"
CURRENCY_HKD = "HKD"
CURRENCY_MYR = "MYR"
CURRENCY_RMB = "RMB"
CURRENCY_SGD = "SGD"

# 默認貨幣
DEFAULT_CURRENCY = "USD"

# 貨幣列表
CURRENCIES = [
    CURRENCY_JPY,
    CURRENCY_KRW,
    CURRENCY_TWD,
    CURRENCY_THB,
    CURRENCY_USD,
    CURRENCY_HKD,
    CURRENCY_MYR,
    CURRENCY_RMB,
    CURRENCY_SGD,
]

# 貨幣型別
Currency = Literal[
    "JPY",
    "KRW", 
    "TWD",
    "THB",
    "USD",
    "HKD",
    "MYR",
    "RMB",
    "SGD"
]
