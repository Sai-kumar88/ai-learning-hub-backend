@echo off
title AI Course Catalog
echo ========================================================
echo Starting AI Course Catalog (Backend + Frontend)...
echo ========================================================
cd /d "%~dp0"

REM Activate virtual environment if present
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

REM Run Flask application (serves both API & Frontend on http://127.0.0.1:5000)
python app.py
pause
