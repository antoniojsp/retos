# main.py
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models import get_todos, add_todo, get_todo, update_todo, delete_todo
import schemas
from typing import Annotated

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_todos(request: Request):
    todos = get_todos()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})


@app.post("/todos", response_class=RedirectResponse)
async def create_todo(task: Annotated[str, Form()]):
    add_todo(task)
    return RedirectResponse(url="/", status_code=303)


@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int):
    todo = get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.post("/todos/{todo_id}/update", response_class=RedirectResponse)
async def update_existing_todo(todo_id: int, task: Annotated[str, Form()], completed: Annotated[bool, Form()] = False):
    update_todo(todo_id, task, completed)
    return RedirectResponse(url="/", status_code=303)


@app.post("/todos/{todo_id}/complete", response_class=RedirectResponse)
async def complete_todo(todo_id: int):
    todo = get_todo(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    update_todo(todo_id, todo.task, True)
    return RedirectResponse(url="/", status_code=303)


@app.post("/todos/{todo_id}/delete", response_class=RedirectResponse)
async def delete_todo_route(todo_id: int):
    delete_todo(todo_id)
    return RedirectResponse(url="/", status_code=303)
