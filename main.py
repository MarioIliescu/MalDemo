from fastapi import FastAPI

from api.controllers.hello_controller import router as hello_router
from api.controllers.user_controller import router as user_router

app = FastAPI(title="MalDemo API")

app.include_router(hello_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}