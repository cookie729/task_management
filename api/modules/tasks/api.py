from fastapi import APIRouter
import api.modules.tasks.schema as task_schema  

router = APIRouter()


@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
  return [task_schema.Task(id=1, title="1つ目の ToDo タスク")]


@router.post("/tasks")
async def create_task():
  pass


@router.put("/tasks/{task_id}")
async def update_task():
  pass


@router.delete("/tasks/{task_id}")
async def delete_task():
  pass


@router.put("/tasks/{task_id}/done")
async def mark_task_as_done():
  pass


@router.delete("tasks/{task_id}/done")
async def unmark_task_as_done():
  pass
