import json

from todo import ToDoManager, ToDo, Status

def manager_to_json(obj: ToDoManager):
    item_dicts = []
    for item in obj.items:
        item.id = str(item.id)
        item.status = int(item.status)
        item_dicts.append(item.__dict__)
    obj.items = item_dicts
    return json.dumps(obj.__dict__)