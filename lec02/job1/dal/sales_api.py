import os
import requests
from typing import Any, Dict, List

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
ENDPOINT = 'sales'

def get_sales(date: str, page_num: int) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :page_num: page number to retrieve
    :return: list of records
    """
    
    AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")
    headers = {'Authorization': AUTH_TOKEN}
    params = {'date': date, 'page': page_num}

    response = requests.get(url=API_URL + ENDPOINT, params=params, headers=headers)    

    return response.json()