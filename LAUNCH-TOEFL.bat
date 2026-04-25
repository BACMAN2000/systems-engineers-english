@echo off
REM Launches TOEFL Runner: starts local server and opens browser
REM Double-click this file to run the TOEFL iBT Practice Tests
cd /d "%~dp0"
start "TOEFL Runner Server" powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0serve-toefl.ps1"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:9124/toefl-runner.html"
echo.
echo TOEFL Runner launched at http://127.0.0.1:9124/toefl-runner.html
echo A PowerShell window is running the local server.
echo Close that window to stop the server.
echo.
pause
