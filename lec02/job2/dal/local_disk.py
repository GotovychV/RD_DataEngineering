import os
import json
from fastavro import writer, parse_schema

def create_and_clear_directory(stg_dir: str) -> None:

    # create a directory path if it doesn't already exist    
    os.makedirs(os.path.join(os.getcwd(), stg_dir), exist_ok=True)

    # delete all existing files in the directory
    for filename in os.listdir(stg_dir):
        file_path = os.path.join(stg_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")


def rewrite_files(raw_dir: str, stg_dir: str) -> None:
    """
    "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    "stg_dir": "/path/to/my_dir/stg/sales/2022-08-09"
    """

    # Schema for Avro
    schema = {
        "type": "record",
        "name": "SalesRecord",
        "fields": [
            {"name": "client", "type": "string"},
            {"name": "purchase_date", "type": "string"},
            {"name": "product", "type": "string"},
            {"name": "price", "type": "int"}
        ]
    }

    # Parse the schema
    parsed_schema = parse_schema(schema)

    # Read JSON files from raw directory
    for filename in os.listdir(raw_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(raw_dir, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

                # Write to Avro file in staging directory
                avro_file_path = os.path.join(stg_dir, filename.replace(".json", ".avro"))
                with open(avro_file_path, 'wb') as avro_file:
                    writer(avro_file, parsed_schema, data)