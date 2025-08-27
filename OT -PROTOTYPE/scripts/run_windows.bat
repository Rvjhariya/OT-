@echo off
REM Run this from repository root in an elevated command prompt


REM Create venv if not present
if not exist .venv (python -m venv .venv)
call .venv\Scripts\activate.bat


pip install --upgrade pip
pip install -r requirements.txt


REM Start API in new window
start "OT API" cmd /k "call .venv\Scripts\activate.bat && python src\api.py"


REM Start sensor in new window (change interface in sensor_modbus.py before running)
start "OT Sensor" cmd /k "call .venv\Scripts\activate.bat && python src\sensor_modbus.py"


echo All services started. Close this window if you want to keep them running.
pause