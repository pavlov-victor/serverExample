import fastapi
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todo_data = []

@app.get('/')
# void functionName - java
def posts():
    return {'todos': todo_data}

@app.get('/{todo}/change')
def change_post(todo: str):
    for index, todo_item in enumerate(todo_data):
        print(todo_item, todo)
        if todo_item['todo'] == todo:
            todo_data[index]['status'] = not todo_data[index]['status']
            print(todo_data[index]['status'])


@app.post('/')
def create_post(todo: str, status: bool):
    data = {"todo": todo, "status": status}
    todo_data.append(data)
    return data
