from fastapi import FastAPI

app = FastAPI()

todos = []


@app.get("/")
def read_root():
    return {"message": "Todo API running"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def add_todo(todo: str):
    todos.append(todo)
    return {"todos": todos}