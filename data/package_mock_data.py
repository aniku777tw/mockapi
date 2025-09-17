"""
Package 測試資料
包含所有套裝旅遊行程的測試數據
"""

# Package 測試資料
PACKAGES_MOCK_DATA = [
    # BNB 1: 台北101 (8個套裝旅遊行程)
    {
        "id": 1,
        "name": "台北101觀景台一日遊",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 600,
        "pricingMethod": "ticket"
    },
    {
        "id": 2,
        "name": "台北101美食文化體驗",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 800,
        "pricingMethod": "single"
    },
    {
        "id": 3,
        "name": "台北101紀念品採購行程",
        "bnbId": 66632,
        "isSoldOut": True,
        "lowestPrice": None,
        "pricingMethod": "single"
    },
    {
        "id": 4,
        "name": "台北101深度導覽行程",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 1200,
        "pricingMethod": "ticket"
    },
    {
        "id": 5,
        "name": "台北101專業攝影行程",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 1500,
        "pricingMethod": "single"
    },
    {
        "id": 6,
        "name": "台北101 VIP 尊榮體驗",
        "bnbId": 66632,
        "isSoldOut": True,
        "lowestPrice": None,
        "pricingMethod": "ticket"
    },
    {
        "id": 7,
        "name": "台北101夜間觀景行程",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 500,
        "pricingMethod": "ticket"
    },
    {
        "id": 8,
        "name": "台北101+故宮聯票",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 1800,
        "pricingMethod": "ticket"
    },
    {
        "id": 9,
        "name": "台北101+故宮聯票",
        "bnbId": 66632,
        "isSoldOut": False,
        "lowestPrice": 0,
        "pricingMethod": "ticket"
    },
]
