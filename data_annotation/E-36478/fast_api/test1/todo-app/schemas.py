# schemas.py
from pydantic import BaseModel

class TodoBase(BaseModel):
    task: str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    completed: bool

class Todo(TodoBase):
    id: int
    completed: bool

    class Config:
      from_attributes = True