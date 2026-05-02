from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Hello"])


@router.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}