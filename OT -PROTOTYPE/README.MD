A small prototype demonstrating passive OT asset discovery, a tiny detection engine, and a FastAPI backend. Intended as a starting point for building an OT security tool inspired by Tenable OT Security.


## What is included
- Passive Modbus/TCP sensor (pyshark) — `src/sensor_modbus.py`
- Tiny rule engine — `src/engine.py`
- FastAPI backend to list assets & alerts — `src/api.py`
- Example rule file — `rules/modbus.yml`
- Dockerfile + docker-compose for quick local runs
- Run scripts for Windows (`scripts/run_windows.bat`) and Unix (`scripts/run_unix.sh`)


## Quick start (recommended: Linux/macOS)


1. Clone the repo and create a virtual environment:


```bash
git clone <your-repo-url>
cd tenable-ot-prototype
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt