# main.py

from fastapi import FastAPI
from api.controllers.hello_controller import router as hello_router

app = FastAPI()

app.include_router(hello_router)


@app.get("/")
async def root():
    return {"message": "Hello MAL"}