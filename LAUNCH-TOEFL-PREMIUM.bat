@echo off
REM ===================================================================
REM  LAUNCH-TOEFL-PREMIUM.bat
REM  One-click launcher. If assets are missing, runs SETUP automatically.
REM ===================================================================
setlocal
cd /d "%~dp0"
title TOEFL iBT Premium Launcher

if not exist "%~dp0toefl-premium-assets\data\index.json" (
    echo.
    echo =====================================================================
    echo   First-time setup: extracting XYSTPO2.0_2.zip and converting
    echo   the Tpo.db database to JSON. This takes 3-6 minutes and needs
    echo   about 2 GB of disk space on E:.
    echo =====================================================================
    echo.
    powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0SETUP-TOEFL-PREMIUM.ps1"
    if errorlevel 1 (
        echo.
        echo Setup failed. See errors above.
        pause
        exit /b 1
    )
    echo.
    echo Setup complete.
    timeout /t 2 /nobreak >nul
)

echo Starting local server and opening TOEFL Premium...
start "TOEFL Premium Server" powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0serve-toefl.ps1"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:9124/toefl-premium-runner.html"

echo.
echo =====================================================================
echo   TOEFL Premium running at http://127.0.0.1:9124/toefl-premium-runner.html
echo.
echo   Unlock codes (enter any of these in the subscription modal):
echo       TOEFL-PREMIUM-2026
echo       RENATTO-TOEFL-55
echo       XYSTPO-UNLOCK
echo.
echo   Close the PowerShell "TOEFL Premium Server" window to stop serving.
echo =====================================================================
echo.
timeout /t 8 /nobreak >nul
exit /b 0
