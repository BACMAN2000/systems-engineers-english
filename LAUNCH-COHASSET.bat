@echo off
REM Launches Cohasset Platform: starts local server and opens browser
REM Double-click this file to open the full platform (with TOEFL button)
cd /d "%~dp0"
start "Cohasset + TOEFL Server" powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0serve-toefl.ps1"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:9124/COHASSET-platform-standalone.html"
echo.
echo Cohasset Platform launched at http://127.0.0.1:9124/COHASSET-platform-standalone.html
echo Click the "TOEFL iBT Tests" button in the header to launch TOEFL Runner.
echo Close the PowerShell window to stop the server.
echo.
pause
