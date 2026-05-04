#!/usr/bin/env bash
set -Eeuo pipefail

NETWORK="plantify-network"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Checking Docker..."
docker info >/dev/null 2>&1

if ! docker network inspect "$NETWORK" >/dev/null 2>&1; then
  echo "Creating Docker network: $NETWORK"
  docker network create --driver bridge "$NETWORK"
else
  echo "Docker network already exists: $NETWORK"
fi

echo "Base Docker setup complete."

cd "$PROJECT_ROOT"

echo "Checking uv..."
uv --version

echo "Syncing Python environment..."
uv sync

echo "Preparing generated folder..."
mkdir -p generated
touch generated/__init__.py

echo "Generating gRPC Python files..."
uv run python -m grpc_tools.protoc \
  -I./protos \
  --python_out=./.generated \
  --grpc_python_out=./.generated \
  --pyi_out=./.generated \
  ./protos/*.proto

echo "Dev setup complete."
echo "Run app with:"
echo "uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload"