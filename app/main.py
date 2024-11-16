from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/tasks")
async def get_tasks():
    return [{"id": "ptvWZ3", "text": "Hello!"}, {"id": "ptvWZ4", "text": "World!"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app, lifespan="off")