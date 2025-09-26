"""
訂單預覽測試資料
"""

from constants.activity_package_module import TICKET_TYPE

def _generate_ticket_offering(ticket_count: list):
    """根據 ticketCount 動態產生 ticketOffering"""
    if not ticket_count:
        return None
    
    ticket_offering = []
    for ticket in ticket_count:
        ticket_id = ticket.get("id")
        count = ticket.get("count", 0)
        
        # 根據票種 ID 設定對應的價格和年齡
        if ticket_id == TICKET_TYPE["TODDLER"]:
            price = 0
            age = 2
        elif ticket_id == TICKET_TYPE["INFANT"]:
            price = 0
            age = 1
        elif ticket_id == TICKET_TYPE["CHILDREN"]:
            price = 500
            age = 12
        elif ticket_id == TICKET_TYPE["ADULT"]:
            price = 1000
            age = None  # 成人沒有年齡限制
        else:
            price = 0
            age = None
        
        ticket_item = {
            "id": ticket_id,
            "count": count,
            "totalWithoutDiscount": {
                "price": price * count,
                "payment": price * count,
                "show": price * count
            }
        }
        
        # 只有非成人票種才需要 age 欄位
        if age is not None:
            ticket_item["age"] = age
            
        ticket_offering.append(ticket_item)
    
    return ticket_offering

def get_normal_case_mock_data(currency: str, activity_start_date: str):
    """取得 Normal case 的 mock 資料"""
    return {
        "token": "e08574f3396ca276040d6e03d8fd953252168a97bddb7ccdbc405e72922657cc",
        "currency": {
            "show": currency,
            "price": currency,
            "payment": currency
        },
        "coupon": {
            "status": 0,
            "message": "ok",
            "payment": 0,
            "show": 0,
            "expireDate": None,
            "maxDiscount": None,
            "type": None,
            "promotionType": None,
            "cost": 0,
            "rate": 0,
            "isLodgingVoucher": False
        },
        "amount": {
            "payable": {
                "price": 1000,
                "payment": 1000,
                "show": 1000
            },
            "final": {
                "price": 1000,
                "payment": 1000,
                "show": 1000
            },
            "room": {
                "total": {
                    "price": 1000,
                    "payment": 1000,
                    "show": 1000
                },
                "detail": [
                    {
                        "date": activity_start_date.replace("-", "/"),
                        "unit": {
                            "price": 1000,
                            "payment": 1000,
                            "show": 1000
                        },
                        "total": {
                            "price": 1000,
                            "payment": 1000,
                            "show": 1000
                        }
                    }
                ]
            },
            "extraPeople": {
                "count": 0,
                "adultCount": None,
                "childCount": None,
                "staffing": [
                    {
                        "seq": 0,
                        "count": 0,
                        "adult": {
                            "count": 0
                        },
                        "child": []
                    }
                ],
                "unit": {
                    "price": 500,
                    "payment": 500,
                    "show": 500
                },
                "childUnit": [],
                "total": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                },
                "adultTotal": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                },
                "childTotal": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                }
            },
            "cleaningFee": {
                "count": 0,
                "unit": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                },
                "total": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                }
            },
            "discount": {
                "type": 0,
                "items": [],
                "rebate": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                }
            },
            "memberPriceDiscount": [],
            "exchange": {
                "currency": {
                    "price": currency,
                    "show": currency,
                    "payment": currency,
                    "supportedPayments": [currency]
                }
            },
            "events": [],
            "affiliate": [],
            "ratePlan": {
                "id": 62837,
                "capacity": None,
                "refundPolicyId": 18,
                "minStayUnits": 1,
                "discount": {
                    "type": "none",
                    "amount": 0,
                    "sumRatePlanDiscount": {
                        "price": 0,
                        "payment": 0,
                        "show": 0
                    }
                },
                "isHostDiscountsAvailable": {
                    "earlyBird": True,
                    "lastMinute": True,
                    "longStay": True,
                    "period": True
                },
                "foods": {
                    "breakfast": {
                        "isIncluded": False,
                        "count": 0,
                        "unitPrice": 0,
                        "unitPayment": 0
                    },
                    "lunch": {
                        "isIncluded": False,
                        "count": 0,
                        "unitPrice": 0,
                        "unitPayment": 0
                    },
                    "dinner": {
                        "isIncluded": False,
                        "count": 0,
                        "unitPrice": 0,
                        "unitPayment": 0
                    },
                    "afternoonTea": {
                        "isIncluded": False,
                        "count": 0,
                        "unitPrice": 0,
                        "unitPayment": 0
                    }
                },
                "foodsTotalPrice": 0,
                "foodsTotalPayment": 0,
                "paidItems": [],
                "paidItemsTotalPrice": 0,
                "paidItemsTotalPayment": 0,
                "isDefault": True,
                "foodsTotalShow": 0,
                "paidItemsTotalShow": 0,
                "totalWithoutDiscount": {
                    "price": 1000,
                    "payment": 1000,
                    "show": 1000
                },
                "name": "基本方案",
                "partnerVendorNameHash": None
            },
            "amountAdjustment": [],
            "hasMultiBedTypes": False,
            "tax": {
                "price": 0,
                "payment": 0,
                "show": 0
            },
            "inCash": {
                "currency": "",
                "price": 0,
                "payment": 0,
                "show": 0
            }
        },
        "refundPolicyRules": [
            {
                "rate": 0.99,
                "startTimestamp": 1750780800,
                "nights": 0,
                "cancelCurrency": "",
                "cancelAmount": 0
            },
            {
                "rate": 0.8,
                "startTimestamp": 1753372800,
                "nights": 0,
                "cancelCurrency": "",
                "cancelAmount": 0
            },
            {
                "rate": 0.5,
                "startTimestamp": 1756051200,
                "nights": 0,
                "cancelCurrency": "",
                "cancelAmount": 0
            },
            {
                "rate": 0.25,
                "startTimestamp": 1757260800,
                "nights": 0,
                "cancelCurrency": "",
                "cancelAmount": 0
            },
            {
                "rate": 0,
                "startTimestamp": 1759161600,
                "nights": 0,
                "cancelCurrency": "",
                "cancelAmount": 0
            }
        ],
        "host": {
            "businessName": None,
            "ubn": None
        },
        "checkInDate": activity_start_date,
        "checkOutDate": "2025-10-01",
        "nonrefundableDateRanges": []
    }

def get_package_case_mock_data(currency: str, locale: str, activity_start_date: str, combination_option_id: str = None, single_count: int = None, ticket_count: list = None):
    """取得 Package case 的 mock 資料"""
    return {
        "token": "e08574f3396ca276040d6e03d8fd953252168a97bddb7ccdbc405e72922657cc",
        "currency": {
            "show": currency,
            "price": currency,
            "payment": currency
        },
        "coupon": {
            "status": 0,
            "message": "ok",
            "payment": 0,
            "show": 0,
            "expireDate": None,
            "maxDiscount": None,
            "type": None,
            "promotionType": None,
            "cost": 0,
            "rate": 0,
            "isLodgingVoucher": False
        },
        "package": {        
            "id": 12345,
            "name": "測試的方案名稱"
        },
        "amount": {
            "payable": {
                "price": 1000,
                "payment": 1000,
                "show": 1000
            },
            "final": {
                "price": 1000,
                "payment": 1000,
                "show": 1000
            },
            "extraPeople": {
                "count": 0,
                "adultCount": None,
                "childCount": None,
                "staffing": [
                    {
                        "seq": 0,
                        "count": 0,
                        "adult": {
                            "count": 0
                        },
                        "child": []
                    }
                ],
                "unit": {
                    "price": 500,
                    "payment": 500,
                    "show": 500
                },
                "childUnit": [],
                "total": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                },
                "adultTotal": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                },
                "childTotal": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                }
            },
            "cleaningFee": {
                "count": 0,
                "unit": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                },
                "total": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                }
            },
            "discount": {
                "type": 0,
                "items": [],
                "rebate": {
                    "price": 0,
                    "payment": 0,
                    "show": 0
                }
            },
            "memberPriceDiscount": [],
            "exchange": {
                "currency": {
                    "price": currency,
                    "show": currency,
                    "payment": currency,
                    "supportedPayments": [currency]
                }
            },
            "events": [],
            "affiliate": [],
            "amountAdjustment": [],
            "hasMultiBedTypes": False,
            "tax": {
                "price": 0,
                "payment": 0,
                "show": 0
            },
            "inCash": {
                "currency": "",
                "price": 0,
                "payment": 0,
                "show": 0
            },
            "combinationOption": {
                "combinationOptionId": combination_option_id,
                "moduleResult": [
                    {
                        "name": "接駁車站",
                        "optionName": "車站A"
                    },
                    {
                        "name": "景點",
                        "optionName": "熊本"
                    },
                    {
                        "name": "門票",
                        "optionName": None
                    }
                ],
                "singleOffering": {
                    "name": "人數",
                    "unitCount": 1,
                    "count": single_count,
                    "totalWithoutDiscount": {
                        "price": 5000,
                        "payment": 5000,
                        "show": 5000
                    }
                } if single_count else None,
                "ticketOffering": _generate_ticket_offering(ticket_count) if ticket_count else None
            }
        },
        "host": {
            "businessName": None,
            "ubn": None
        },
        "checkInDate": activity_start_date,
        "checkOutDate": "2025-10-01",
        "nonrefundableDateRanges": []
    }
