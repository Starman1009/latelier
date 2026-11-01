@echo off
title L'Atelier OS Launcher
cd /d "%~dp0"

echo ===================================================
echo           L'ATELIER SYSTEM INITIALIZATION
echo ===================================================
echo.

:: 1. Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.10+ from python.org.
    pause
    exit /b
)

:: 2. Check if local server is already running on port 8000
netstat -ano | findstr :8000 >nul 2>&1
if %errorlevel% equ 0 (
    echo [i] Server already active on port 8000.
) else (
    echo [+] Starting local HTTP server on port 8000...
    start /b python -m http.server 8000 >nul 2>&1
    timeout /t 2 >nul
)

:: 3. Launch default browser
echo [+] Launching L'Atelier OS in default browser...
start http://localhost:8000

echo [i] L'Atelier is live. Keep this window open while cooking.
echo.
echo Press any key to stop the server and exit.
pause >nul

:: Clean shutdown of server on port 8000
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do taskkill /f /pid %%a >nul 2>&1
echo [+] Server stopped.
exit