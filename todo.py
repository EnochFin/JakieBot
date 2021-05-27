import uuid
from enum import IntEnum

class Status(IntEnum):
    not_done = 0,
    in_progress = 1,
    done = 2

class ToDo():
    def __init__(self, title):
        self.id = uuid.uuid4()
        self.status = Status.not_done
        self.title = title

class ToDoManager():
    def __init__(self):
        self.items = []
        self.name = 'list'
    
    def copy(self):
        result = ToDoManager()
        result.items = self.items.copy()
        result.name = f'{self.name}'
        return result