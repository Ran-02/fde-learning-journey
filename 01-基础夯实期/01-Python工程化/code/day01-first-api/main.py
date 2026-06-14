from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="我的第一个FDE项目", version="1.0")

class Task(BaseModel):
    title: str
    description: str | None = None
    priority: int = 1

@app.get("/", summary="问候窗口")
def hello():
    return {"code": 0, "message": "欢迎来到fde学习之旅"}

@app.post("/tasks", summary="创建任务")
# 参数名还是 task，类型用大写的 Task
def create_task(task: Task):
    return {
        "code": 0,
        "data": {
            "task_id": 1,
            "title": task.title,
            "description": task.description,
            "priority": task.priority
        }
    }