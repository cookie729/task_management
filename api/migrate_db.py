from sqlalchemy import create_engine

from api.modules.tasks.model import Base as task_base
from api.modules.dones.model import Base as done_base

DB_URL = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"
engine = create_engine(DB_URL, echo=True)


def reset_database():
  task_base.metadata.drop_all(bind=engine)
  task_base.metadata.create_all(bind=engine)
  done_base.metadata.drop_all(bind=engine)
  done_base.metadata.create_all(bind=engine)


if __name__ == "__main__":
  reset_database()
