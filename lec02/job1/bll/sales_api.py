import os
from dal import local_disk, sales_api

def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    """
    "date: "2022-08-09"
    "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    """

    page_num = 1

    while True:
        # 1. get data from the API
        sales = sales_api.get_sales(date=date, page_num=page_num)            

        if not sales or len(sales) <= 1:
            break

        # 3. create directory only if there is at least some data
        if page_num == 1 and len(sales) > 1:
            local_disk.create_and_clear_directory(raw_dir=raw_dir)
        
        # 2. save data to disk
        local_disk.save_to_disk(json_content=sales, path=os.path.join(raw_dir, f"sales_{date}_{page_num}.json"))

        page_num += 1