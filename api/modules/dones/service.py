from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.modules.dones.model as done_model

def get_done(db: Session, task_id: int) -> done_model.Done | None:
  result: Result = db.execute(
    select(done_model.Done).filter(done_model.Done.id == task_id)
  )
  return result.scalars().first()

def create_done(db: Session, task_id: int) -> done_model.Done:
  done = done_model.Done(id=task_id)
  print("1", done)
  print("2", task_id)
  db.add(done)
  db.commit()
  db.refresh(done)
  return done

def delete_done(db: Session, original: done_model.Done) -> None:
  db.delete(original)
  db.commit()