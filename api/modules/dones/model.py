from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from api.db import Base


class Done(Base):
    __tablename__ = "done"
    id = Column(Integer, ForeignKey("task.id"), primary_key=True)
    task = relationship("Task", back_populates="done")