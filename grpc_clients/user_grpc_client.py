import sys
from pathlib import Path

generated_path = Path(__file__).resolve().parents[1] / "generated"
sys.path.insert(0, str(generated_path))

import grpc
import user_pb2
import user_pb2_grpc

from config.settings import settings


class UserGrpcClient:
    async def get_by_username(self, username: str) -> dict:
        async with grpc.aio.insecure_channel(settings.grpc_address) as channel:
            stub = user_pb2_grpc.UserServiceProtoStub(channel)

            request = user_pb2.GetUserRequest(
                username=username,
            )

            response = await stub.Get(request)

            return self._parse_user_response(response)

    async def get_by_email(self, email: str) -> dict:
        async with grpc.aio.insecure_channel(settings.grpc_address) as channel:
            stub = user_pb2_grpc.UserServiceProtoStub(channel)

            request = user_pb2.GetUserRequest(
                email=email,
            )

            response = await stub.Get(request)

            return self._parse_user_response(response)

    def _parse_user_response(self, response) -> dict:
        return {
            "name": response.name,
            "username": response.username,
            "password": response.password,
            "email": response.email,
        }