"""
訂單服務類別
"""

from typing import Dict, Any
from data.order_mock_data import get_normal_case_mock_data, get_package_case_mock_data

class OrderService:
    """訂單服務類別"""
    
    def __init__(self):
        """初始化 Order Service"""
        pass
    
    def preview_order(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """預覽訂單"""
        # 檢查是否為 package case
        package_case_fields = [
            request_data.get("singleCount"),
            request_data.get("ticketCount"),
            request_data.get("combinationOptionId")
        ]
        has_package_case = any(field is not None for field in package_case_fields)
        
        if has_package_case:
            # Package case
            return get_package_case_mock_data(
                currency=request_data.get("currency", "TWD"),
                locale=request_data.get("locale", "zh-tw"),
                activity_start_date=request_data.get("activityStartDate"),
                combination_option_id=request_data.get("combinationOptionId"),
                single_count=request_data.get("singleCount"),
                ticket_count=request_data.get("ticketCount")
            )
        else:
            # Normal case
            return get_normal_case_mock_data(
                currency=request_data.get("currency", "TWD"),
                activity_start_date=request_data.get("activityStartDate")
            )
