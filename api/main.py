from fastapi import FastAPI
from api.modules.tasks import api as task_api
from api.modules.dones import api as done_api

app = FastAPI()

app.include_router(task_api.router)
app.include_router(done_api.router)
