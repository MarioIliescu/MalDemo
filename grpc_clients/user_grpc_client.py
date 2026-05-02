import grpc

from config.settings import settings
from generated import user_pb2
from generated import user_pb2_grpc


class UserGrpcClient:
    async def get_user(self, username: str, email: str = "") -> dict:
        async with grpc.aio.insecure_channel(settings.grpc_address) as channel:
            stub = user_pb2_grpc.UserServiceProtoStub(channel)

            request = user_pb2.GetUserRequest(
                username=username,
                email=email,
            )

            response = await stub.Get(request)

            return {
                "name": response.name,
                "username": response.username,
                "password": response.password,
                "email": response.email,
            }