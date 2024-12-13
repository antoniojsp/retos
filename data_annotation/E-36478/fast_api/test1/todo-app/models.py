# models.py
from typing import List


class Todo:
    def __init__(self, id: int, task: str, completed: bool = False):
        self.id = id
        self.task = task
        self.completed = completed


# In-memory storage (replace with database interaction in a real app)
todos: List[Todo] = []
next_todo_id = 1


def get_todos():
    return todos


def add_todo(task: str):
    global next_todo_id
    todo = Todo(id=next_todo_id, task=task)
    todos.append(todo)
    next_todo_id += 1
    return todo


def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


def update_todo(todo_id: int, task: str, completed: bool):
    todo = get_todo(todo_id)
    if todo:
        todo.task = task
        todo.completed = completed
        return todo
    return None


def delete_todo(todo_id: int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id]
