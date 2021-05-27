import json

from todo import ToDoManager, ToDo, Status

def manager_to_json(obj: ToDoManager):
    copy = obj.copy()
    item_dicts = []
    for item in copy.items:
        item.id = str(item.id)
        item.status = int(item.status)
        item_dicts.append(item.__dict__)
    copy.items = item_dicts
    return json.dumps(copy.__dict__)

def json_to_manager(manager: ToDoManager, obj):
    item_dicts = []
    for item in obj['items']:
        new_item = ToDo(item['title'])
        new_item.id = item['id']
        new_item.status = item['status']
        item_dicts.append(new_item)
    manager.items = item_dicts
