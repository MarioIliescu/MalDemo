```shell
uv add fastapi uvicorn grpcio grpcio-tools protobuf

uv add --dev ruff

uv add pydantic-settings python-dotenv
```

Create proto
```shell
uv run python -m grpc_tools.protoc \
  -I protos \
  --python_out=generated \
  --grpc_python_out=generated \
  --pyi_out=generated \
  protos/*.proto
```