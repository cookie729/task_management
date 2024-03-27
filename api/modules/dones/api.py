from fastapi import APIRouter, HTTPException, Depends
from api.db import get_db
from api.modules.dones.model import Done
import api.modules.dones.schema as done_schema
import api.modules.dones.service as done_service

router = APIRouter()

@router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db = Depends(get_db)):
  done = done_service.get_done(db, task_id=task_id)
  if done is not None:
    raise HTTPException(status_code=400, detail="Done already exists")
  done = done_service.create_done(db, task_id)
  return done


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int, db = Depends(get_db)):
  try:
    done = Done.get(Done.task_id == task_id)
  except Done.DoesNotExist:
    raise HTTPException(status_code=404, detail="Done not found")
  done.delete_instance()



# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session

# import api.modules.dones.schema as done_schema
# import api.modules.dones.service as done_service
# from api.db import get_db

# router = APIRouter()


# @router.put("/tasks/{task_id}/done", response_model=done_schema.DoneResponse)
# async def mark_task_as_done(task_id: int, db: Session = Depends(get_db)):
#   done = done_service.get_done(db, task_id=task_id)
#   if done is not None:
#     raise HTTPException(status_code=400, detail="Done already exists")
#   return done_service.create_done(db, task_id)


# @router.delete("/tasks/{task_id}/done", response_model=None)
# async def unmark_task_as_done(task_id: int, db: Session = Depends(get_db)):
#   done = done_service.get_done(db, task_id=task_id)
#   if done is None:
#     raise HTTPException(status_code=404, detail="Done not found")
#   return done_service.delete_done(db, original=done)
