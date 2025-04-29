from dal import local_disk

def rewrite_files(raw_dir: str, stg_dir: str) -> None:
    """    
    "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    "stg_dir": "/path/to/my_dir/stg/sales/2022-08-09"
    """
    local_disk.create_and_clear_directory(stg_dir=stg_dir)

    local_disk.rewrite_files(raw_dir=raw_dir, stg_dir=stg_dir)