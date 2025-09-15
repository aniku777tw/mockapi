"""
Activity Package Module Constants

活動套裝旅遊行程模組相關常數
"""

# 庫存狀態
INVENTORY_STATUS = {
    "BOOKABLE": 0,
    "SOLD_OUT": 1,
    "NO_COMBINATION": 2,  # 沒有可售組合
}

# 票券類型
TICKET_TYPE = {
    "TODDLER": 1,    # 嬰兒
    "INFANT": 2,     # 幼兒
    "CHILDREN": 3,   # 兒童
    "ADULT": 4,      # 成人
}
