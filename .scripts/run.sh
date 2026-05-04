#!/usr/bin/env bash
set -Eeuo pipefail

cd /workspace

export PYTHONPATH="/workspace/.generated:/workspace:${PYTHONPATH:-}"

uv run uvicorn main:app --host 0.0.0.0 --port 12080 --reload