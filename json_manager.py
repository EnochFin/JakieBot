import json

FILE_NAME = 'save.json'

def save_json(json_data):
    with open(FILE_NAME, 'w') as f:
        json.dump(json_data, f)

def read_json():
    f = open(FILE_NAME)
    data = json.loads(json.load(f))
    return data