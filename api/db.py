from peewee import PostgresqlDatabase, Model

DB_URL = "postgres://posrtgres@db:5432/postgres"

db = PostgresqlDatabase(
    'postgres', 
    host='db', 
    port = 5432, 
    user='postgres', 
    password='postgres'
)

class BaseModel(Model):
    class Meta:
        database = db

db.connect()

def get_db():
    with db.atomic() as txn:
        yield txn


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DB_URL = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"

# db_engine = create_engine(DB_URL, echo=True)
# db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# Base = declarative_base()
# def get_db():
#   with db_session() as session:
#     yield session