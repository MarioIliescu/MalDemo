from fastapi import APIRouter, HTTPException
from grpc import RpcError, StatusCode

from grpc_clients.user_grpc_client import UserGrpcClient

router = APIRouter(prefix="/user", tags=["User"])

client = UserGrpcClient()


@router.get("/{username}")
async def get_by_username(username: str):
    try:
        return await client.get_by_username(username)
    except RpcError as ex:
        if ex.code() == StatusCode.NOT_FOUND:
            raise HTTPException(
                status_code=404,
                detail=f"User with username {username} not found.",
            )

        raise HTTPException(
            status_code=500,
            detail={
                "grpc_code": ex.code().name,
                "grpc_details": ex.details(),
            },
        )


@router.get("/email/{email}")
async def get_by_email(email: str):
    try:
        return await client.get_by_email(email)
    except RpcError as ex:
        if ex.code() == StatusCode.NOT_FOUND:
            raise HTTPException(
                status_code=404,
                detail=f"User with email {email} not found.",
            )

        raise HTTPException(
            status_code=500,
            detail={
                "grpc_code": ex.code().name,
                "grpc_details": ex.details(),
            },
        )