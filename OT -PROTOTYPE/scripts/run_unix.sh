#!/usr/bin/env bash
set -e
# Run from repo root
python -m venv .venv || true
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt &


# Start API (background)
ohbn() {
uvicorn src.api:app --host 0.0.0.0 --port 8000 &
}
ohbn


# Start sensor (foreground)
python src/sensor_modbus.py