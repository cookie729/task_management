from fastapi import FastAPI
from api.modules.tasks import api

app = FastAPI()

app.include_router(api.router)

# @app.get("/hello")
# async def hello():
#   return {"message": "hello world!"}