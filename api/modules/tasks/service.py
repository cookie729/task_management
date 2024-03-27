from typing import List, Tuple, Union
from peewee import fn, JOIN
from api.modules.tasks.model import Task
from api.modules.dones.model import Done
from api.modules.tasks.schema import TaskCreate

def create_task(task_create: TaskCreate) -> Task:
  task = Task.create(**task_create.model_dump())
  return task


def get_tasks_with_done() -> List[Task]:
  tasks = (Task
            .select(Task.id, Task.title, fn.COALESCE(fn.Count(Done.task_id), 0).alias('done_count'))
            .join(Done, JOIN.LEFT_OUTER, on=(Task.id == Done.task_id))
            .group_by(Task.id))
  return [(task.id, task.title, task.done_count > 0) for task in tasks]


def get_task(task_id: int) -> Union[Task, None]:
  task = Task.get_or_none(Task.id == task_id)
  return task

def update_task(task_create: TaskCreate, original: Task) -> Task:
  original.title = task_create.title
  original.save()
  return original

def delete_task(original: Task) -> None:
  original.delete_instance()





# from sqlalchemy.orm import Session
# from sqlalchemy import select
# from sqlalchemy.engine import Result

# import api.modules.tasks.model as task_model
# import api.modules.tasks.schema as task_schema
# import api.modules.dones.model as done_model


# def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
#   task = task_model.Task(**task_create.model_dump())
#   db.add(task)
#   db.commit()
#   db.refresh(task)
#   return task

# def get_tasks_with_done(db: Session) -> list[tuple[int, str, bool]]:
#   result: Result = db.execute(
#     select(
#       task_model.Task.id,
#       task_model.Task.title,
#       done_model.Done.id.isnot(None).label("done"),
#     ).outerjoin(done_model.Done)
#   )

#   return result.all()

# def get_task(db: Session, task_id: int) -> task_model.Task | None:
#   result: Result = db.execute(
#     select(task_model.Task).filter(task_model.Task.id == task_id)
#   )
#   return result.scalars().first()

# def update_task(
#     db: Session, task_create: task_schema.TaskCreate, original: task_model.Task
# ) -> task_model.Task:
#   original.title = task_create.title
#   db.add(original)
#   db.commit()
#   db.refresh(original)
#   return original

# def delete_task(db: Session, original: task_model.Task) -> None:
#   db.delete(original)
#   db.commit()