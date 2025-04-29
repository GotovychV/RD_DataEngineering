import os
import json
from typing import List, Dict, Any

def create_and_clear_directory(raw_dir: str) -> None:

    # create a directory path if it doesn't already exist    
    os.makedirs(os.path.join(os.getcwd(), raw_dir), exist_ok=True)

    # delete all existing files in the directory
    for filename in os.listdir(raw_dir):
        file_path = os.path.join(raw_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    
    with open(path, 'w') as json_file:
        json.dump(json_content, json_file, indent=4)