import json
import os

FILE_NAME = os.getenv("SAVE_FILE")

def save_json(json_data):
    with open(FILE_NAME, 'w') as f:
        json.dump(json_data, f)

def read_json():
    f = open(FILE_NAME)
    data = json.loads(json.load(f))
    return data