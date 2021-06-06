import json
from todo import ToDo, ToDoManager

import json_manager
import util

def add(manager: ToDoManager, commands):
    task_name = ' '.join(commands[1:])
    manager.items.append(ToDo(task_name))
    return f'added: {task_name}'

def list(manager: ToDoManager, commands):
    result = '```\n'
    for item in manager.items:
        line = f'{item.status}| {item.title}\n'
        result += line
    return result + '```'

def save(manager: ToDoManager, commands):
    json_manager.save_json(util.manager_to_json(manager))
    return 'saved the list!'

def load(manager: ToDoManager, commands):
    json_obj = json_manager.read_json()

    util.json_to_manager(manager, json_obj)

    return list(manager, commands)

def progress(manager: ToDoManager, commands):
    if len(commands) == 1:
        return list(manager, commands)

    try:
        index = int(commands[1])
    except:
        return f'Cannot find an item at index: {commands[1]}'

    print(index)

    if index > 0:
        selected = manager.items[index - 1]
        if int(selected.status) == 2:
            return f'Cannot progress status of item at index: {index}'
        selected.status = int(selected.status) + 1
        return f'Updated status of item at index: {index} to: {selected.status}'
    return f'Please select an index of [1-{len(manager.items)}'

MANAGER_COMMANDS = {
    'add': add,
    'list': list,
    'save': save,
    'load': load,
    'progress': progress,
}