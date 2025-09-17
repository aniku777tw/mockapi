"""
模組測試資料
包含所有套裝旅遊行程的模組和組合數據
"""

from constants.activity_package_module import INVENTORY_STATUS, TICKET_TYPE

# 模組測試資料
MODULES_MOCK_DATA = {
    # Package 1: 台北101觀景台一日遊 (ticket pricing)
    1: {
        "modules": [
            {
                "id": 101,
                "name": "觀景台時段選擇",
                "isShowEmpty": False,
                "options": [
                    {"id": 1011, "name": "上午時段 (09:00-12:00)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 1012, "name": "下午時段 (13:00-16:00)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 1013, "name": "夜間時段 (18:00-21:00)", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 1014, "name": "凌晨時段 (02:00-05:00)", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 1015, "name": "VIP 專屬時段", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            },
            {
                "id": 102,
                "name": "導覽服務",
                "isShowEmpty": True,
                "options": [
                    {"id": 1022, "name": "中文導覽", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 1023, "name": "英文導覽", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 1024, "name": "日文導覽", "inventoryStatus": INVENTORY_STATUS["NO_COMBINATION"]},
                    {"id": 1025, "name": "韓文導覽", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            },
            {
                "id": 103,
                "name": "附加服務",
                "isShowEmpty": True,
                "options": [
                    {"id": 1032, "name": "專業攝影", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 1033, "name": "紀念品包", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 1034, "name": "豪華紀念品包", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            }
        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[1011, 1022, 1032]",
                "moduleOptionIds": [1011, 1022, 1032],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 50, "price": 600},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 30, "price": 300},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 20, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 15, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[1011, 1023, 1032]",
                "moduleOptionIds": [1011, 1023, 1032],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 25, "price": 800},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 400},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 10, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 8, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[1012, 1023, 1032]",
                "moduleOptionIds": [1012, 1023, 1032],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 20, "price": 1200},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 10, "price": 600},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 8, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 5, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[1015, 1022, 1033]",
                "moduleOptionIds": [1015, 1022, 1033],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 10, "price": 2000},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 8, "price": 1000},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 5, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 3, "price": 0},
                ]
            },
            # 新增：不加購導覽服務的組合
            {
                "combinationOptionId": "combo_[1011, null, 1032]",
                "moduleOptionIds": [1011, None, 1032],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 60, "price": 500},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 40, "price": 250},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 25, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 20, "price": 0},
                ]
            },
            # 新增：不加購附加服務的組合
            {
                "combinationOptionId": "combo_[1012, 1022, null]",
                "moduleOptionIds": [1012, 1022, None],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 30, "price": 700},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 20, "price": 350},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 15, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 10, "price": 0},
                ]
            },
            # 新增：都不加購的組合
            {
                "combinationOptionId": "combo_[1011, null, null]",
                "moduleOptionIds": [1011, None, None],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 80, "price": 400},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 50, "price": 200},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 30, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 25, "price": 0},
                ]
            }
        ]
    },

    # Package 2: 台北101美食文化體驗 (single pricing)
    2: {
        "modules": [
            {
                "id": 201,
                "name": "美食體驗選擇",
                "isShowEmpty": False,
                "options": [
                    {"id": 2011, "name": "傳統小吃體驗", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 2012, "name": "高級餐廳體驗", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 2013, "name": "夜市美食之旅", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 2014, "name": "高級日式料理", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 2015, "name": "米其林餐廳體驗", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            },
            {
                "id": 202,
                "name": "文化活動",
                "isShowEmpty": True,
                "options": [
                    {"id": 2022, "name": "茶藝體驗", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 2023, "name": "書法體驗", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 2024, "name": "太極拳體驗", "inventoryStatus": INVENTORY_STATUS["NO_COMBINATION"]},
                    {"id": 2025, "name": "書法大師班", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            },
            {
                "id": 203,
                "name": "交通方式",
                "isShowEmpty": True,
                "options": [
                    {"id": 2031, "name": "自行前往", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 2032, "name": "專車接送", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            }
        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[2011, 2022, 2031]",
                "moduleOptionIds": [2011, 2022, 2031],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 40, "price": 800},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[2011, 2023, 2031]",
                "moduleOptionIds": [2011, 2023, 2031],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 20, "price": 1200},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[2012, 2022, 2032]",
                "moduleOptionIds": [2012, 2022, 2032],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 15, "price": 2500},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[2015, 2023, 2032]",
                "moduleOptionIds": [2015, 2023, 2032],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 8, "price": 3500},
                "ticketOffering": None
            },
            # 新增：不加購文化活動的組合
            {
                "combinationOptionId": "combo_[2011, null, 2031]",
                "moduleOptionIds": [2011, None, 2031],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 50, "price": 600},
                "ticketOffering": None
            },
            # 新增：不加購交通方式的組合
            {
                "combinationOptionId": "combo_[2012, 2022, null]",
                "moduleOptionIds": [2012, 2022, None],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 25, "price": 1800},
                "ticketOffering": None
            },
            # 新增：都不加購的組合
            {
                "combinationOptionId": "combo_[2011, null, null]",
                "moduleOptionIds": [2011, None, None],
                "singleOffering": {"name": "數量", "unitCount": 1, "inventory": 60, "price": 500},
                "ticketOffering": None
            }
        ]
    },

    # Package 3: 台北101紀念品採購行程 (single pricing)
    3: {
        "modules": [
            {
                "id": 301,
                "name": "紀念品類別",
                "isShowEmpty": False,
                "options": [
                    {"id": 3011, "name": "台北101紀念品", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 3012, "name": "台灣特色商品", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 3013, "name": "文創商品", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            },
            {
                "id": 302,
                "name": "購買數量",
                "isShowEmpty": True,
                "options": [
                    {"id": 3021, "name": "單件購買", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 3022, "name": "套裝組合", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            }
        ],
        "availableCombinations": []
    },

    # Package 4: 台北101深度導覽行程 (ticket pricing)
    4: {
        "modules": [
            {
                "id": 401,
                "name": "導覽深度",
                "isShowEmpty": False,
                "options": [
                    {"id": 4011, "name": "基礎導覽 (1小時)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 4012, "name": "深度導覽 (2小時)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 4013, "name": "專業導覽 (3小時)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            },
            {
                "id": 402,
                "name": "參觀區域",
                "isShowEmpty": False,
                "options": [
                    {"id": 4021, "name": "觀景台", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 4022, "name": "觀景台+阻尼器", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 4023, "name": "全區域參觀", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            }
        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[4011, 4021]",
                "moduleOptionIds": [4011, 4021],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 30, "price": 1200},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 20, "price": 800},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 15, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 10, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[4012, 4022]",
                "moduleOptionIds": [4012, 4022],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 20, "price": 1800},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 1200},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 12, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 8, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[4013, 4023]",
                "moduleOptionIds": [4013, 4023],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 10, "price": 2500},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 8, "price": 1500},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 6, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 4, "price": 0},
                ]
            }
        ]
    },

    # Package 5: 台北101專業攝影行程 (single pricing)
    5: {
        "modules": [
            {
                "id": 501,
                "name": "攝影服務選擇",
                "isShowEmpty": False,
                "options": [
                    {"id": 5011, "name": "基礎攝影 (30分鐘)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 5012, "name": "專業攝影 (60分鐘)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 5013, "name": "豪華攝影 (90分鐘)", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            },
            {
                "id": 502,
                "name": "照片數量",
                "isShowEmpty": True,
                "options": [
                    {"id": 5021, "name": "10張精選", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 5022, "name": "20張精選", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 5023, "name": "全部照片", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            }
        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[5011, 5021]",
                "moduleOptionIds": [5011, 5021],
                "singleOffering": {"name": "人數", "unitCount": 1, "inventory": 25, "price": 1500},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[5012, 5022]",
                "moduleOptionIds": [5012, 5022],
                "singleOffering": {"name": "人數", "unitCount": 1, "inventory": 15, "price": 2500},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[5013, 5023]",
                "moduleOptionIds": [5013, 5023],
                "singleOffering": {"name": "人數", "unitCount": 1, "inventory": 8, "price": 3500},
                "ticketOffering": None
            },
            # 新增：不加購照片數量的組合
            {
                "combinationOptionId": "combo_[5011, null]",
                "moduleOptionIds": [5011, None],
                "singleOffering": {"name": "人數", "unitCount": 1, "inventory": 30, "price": 1200},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[5012, null]",
                "moduleOptionIds": [5012, None],
                "singleOffering": {"name": "人數", "unitCount": 1, "inventory": 20, "price": 2000},
                "ticketOffering": None
            },
            {
                "combinationOptionId": "combo_[5013, null]",
                "moduleOptionIds": [5013, None],
                "singleOffering": {"name": "人數", "unitCount": 1, "inventory": 12, "price": 3000},
                "ticketOffering": None
            }
        ]
    },

    # Package 6: 台北101 VIP 尊榮體驗 (ticket pricing)
    6: {
        "modules": [
            {
                "id": 601,
                "name": "VIP 服務等級",
                "isShowEmpty": False,
                "options": [
                    {"id": 6011, "name": "VIP 專屬通道", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 6012, "name": "VIP 專屬導覽", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 6013, "name": "VIP 專屬餐廳", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            },
            {
                "id": 602,
                "name": "附加服務",
                "isShowEmpty": True,
                "options": [
                    {"id": 6021, "name": "專車接送", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 6022, "name": "專屬攝影師", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                    {"id": 6023, "name": "專屬紀念品", "inventoryStatus": INVENTORY_STATUS["SOLD_OUT"]},
                ]
            }
        ],
        "availableCombinations": []
    },

    # Package 7: 台北101夜間觀景行程 (ticket pricing - 簡化票券)
    7: {
        "modules": [
            {
                "id": 701,
                "name": "觀景時段",
                "isShowEmpty": False,
                "options": [
                    {"id": 7011, "name": "18:00-20:00", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 7012, "name": "20:00-22:00", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            }
        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[7011]",
                "moduleOptionIds": [7011],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 40, "price": 500},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 20, "price": 250},
                ]
            },
            {
                "combinationOptionId": "combo_[7012]",
                "moduleOptionIds": [7012],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 30, "price": 600},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 300},
                ]
            }
        ]
    },

    # Package 8: 台北101+故宮聯票 (ticket pricing - 混合票券)
    8: {
        "modules": [
            {
                "id": 801,
                "name": "參觀順序",
                "isShowEmpty": False,
                "options": [
                    {"id": 8011, "name": "先101後故宮", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 8012, "name": "先故宮後101", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            },
            {
                "id": 802,
                "name": "交通方式",
                "isShowEmpty": True,
                "options": [
                    {"id": 8021, "name": "自行前往", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 8022, "name": "專車接送", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            }
        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[8011, 8021]",
                "moduleOptionIds": [8011, 8021],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 25, "price": 1800},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 900},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 10, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[8012, 8022]",
                "moduleOptionIds": [8012, 8022],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 20, "price": 2200},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 12, "price": 1100},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 8, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 5, "price": 0},
                ]
            },
            # 新增：不加購交通方式的組合
            {
                "combinationOptionId": "combo_[8011, null]",
                "moduleOptionIds": [8011, None],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 30, "price": 1500},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 20, "price": 750},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 15, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[8012, null]",
                "moduleOptionIds": [8012, None],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 25, "price": 1800},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 900},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 12, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 8, "price": 0},
                ]
            }
        ]
    },

    # Package 9: 台北101+故宮聯票 (ticket pricing - 混合票券)
    9: {
        "modules": [
            {
                "id": 901,
                "name": "參觀順序",
                "isShowEmpty": False,
                "options": [
                    {"id": 9011, "name": "先101後故宮", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 9012, "name": "先故宮後101", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            },
            {
                "id": 902,
                "name": "交通方式",
                "isShowEmpty": True,
                "options": [
                    {"id": 9021, "name": "自行前往", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                    {"id": 9022, "name": "專車接送", "inventoryStatus": INVENTORY_STATUS["BOOKABLE"]},
                ]
            }

        ],
        "availableCombinations": [
            {
                "combinationOptionId": "combo_[9011, null]",
                "moduleOptionIds": [9011, None],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 25, "price": 0},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 0},
                    {"id": TICKET_TYPE["TODDLER"], "age": 2, "inventory": 12, "price": 0},
                    {"id": TICKET_TYPE["INFANT"], "age": 1, "inventory": 8, "price": 0},
                ]
            },
            {
                "combinationOptionId": "combo_[9012, null]",
                "moduleOptionIds": [9012, None],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 25, "price": 0},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 0},
                ]
            } ,
            {
                "combinationOptionId": "combo_[9011, 9021]",
                "moduleOptionIds": [9011, 9021],
                "singleOffering": None,
                "ticketOffering": [
                    {"id": TICKET_TYPE["ADULT"], "inventory": 25, "price": 0},
                    {"id": TICKET_TYPE["CHILDREN"], "age": 12, "inventory": 15, "price": 0},
                ]
            }
        ]
    },
}