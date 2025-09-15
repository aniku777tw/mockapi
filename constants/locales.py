"""
Locale Constants

語言地區常數定義
"""

from typing import Literal

# 語言地區常數
LOCALE_JA_JP = "ja-jp"
LOCALE_KO_KR = "ko-kr"
LOCALE_EN_US = "en-us"
LOCALE_ZH_TW = "zh-tw"
LOCALE_ZH_HK = "zh-hk"
LOCALE_ZH_CN = "zh-cn"
LOCALE_ZH_MY = "zh-my"
LOCALE_TH_TH = "th-th"

# 默認語言地區
DEFAULT_LOCALE = LOCALE_ZH_TW

# 可用的語言地區列表
AVAILABLE_LOCALES = [
    LOCALE_ZH_HK,
    LOCALE_ZH_MY,
    LOCALE_ZH_TW,
    LOCALE_EN_US,
    LOCALE_KO_KR,
    LOCALE_JA_JP,
]

# 語言地區型別
Locale = Literal[
    "ja-jp",
    "ko-kr", 
    "en-us",
    "zh-tw",
    "zh-hk",
    "zh-cn",
    "zh-my",
    "th-th"
]
