@echo off
title Vaps Artificial Intelligence Learning Center
echo ========================================================
echo Starting Vaps Artificial Intelligence Learning Center...
echo ========================================================
cd /d "%~dp0"

REM Activate virtual environment if present
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

REM Run Flask application (serves both API & Frontend on http://127.0.0.1:5000)
python app.py
pause
