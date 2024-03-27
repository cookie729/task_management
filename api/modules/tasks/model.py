from peewee import ForeignKeyField, CharField

from api.db import BaseModel

class Task(BaseModel):
    title = CharField()
    class Meta:
        table_name = "task"

class Done(BaseModel):
    task = ForeignKeyField(Task, backref='done_tasks', column_name='task_id', on_delete='CASCADE')


# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from api.db import Base


# class Task(Base):
#     __tablename__ = "task"
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     done = relationship("Done", back_populates="task", cascade="delete")