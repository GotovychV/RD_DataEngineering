"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
from flask import Flask, request
from flask import typing as flask_typing
from bll.rewriter_api import rewrite_files

AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer

    Proposed POST body in JSON:
    {      
      "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09",
      "stg_dir": "/path/to/my_dir/stg/sales/2022-08-09"
    }
    """
    input_data: dict = request.json
    if not input_data:
        return {
            "message": "Request body is empty",
        }, 400    

    raw_dir = input_data.get('raw_dir')    
    stg_dir = input_data.get('stg_dir') 

    if not raw_dir:
        return {
            "message": "raw_dir parameter missed",
        }, 400
    
    if not stg_dir:
        return {
            "message": "stg_dir parameter missed",
        }, 400

    rewrite_files(raw_dir=raw_dir, stg_dir=stg_dir)

    return {
               "message": "Data files from raw-directory into avro-directory rewrited",
           }, 201

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)