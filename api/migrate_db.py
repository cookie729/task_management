# from sqlalchemy import create_engine

# from api.modules.tasks.model import Base

# DB_URL = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"
# engine = create_engine(DB_URL, echo=True)


# def reset_database():
#   Base.metadata.drop_all(bind=engine)
#   Base.metadata.create_all(bind=engine)


# if __name__ == "__main__":
#   reset_database()



from peewee import PostgresqlDatabase
from api.modules.tasks.model import Task
from api.modules.dones.model import Done

DB_URL = "postgres://postgres:postgres@db:5432/postgres"

db = PostgresqlDatabase("postgres", user="postgres", password="postgres", host="db", port=5432)
db.connect()
Task.bind(db)
Done.bind(db)
def reset_database():
    db.drop_tables([Task], safe=True)
    db.create_tables([Task])
    db.drop_tables([Done], safe=True)
    db.create_tables([Done])

if __name__ == "__main__":
    reset_database()