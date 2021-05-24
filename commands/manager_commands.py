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

MANAGER_COMMANDS = {
    'add': add,
    'list': list,
    'save': save,
}