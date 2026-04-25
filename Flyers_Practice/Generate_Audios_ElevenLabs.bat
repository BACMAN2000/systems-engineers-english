@echo off
REM --- Generate Flyers Practice Audios using ElevenLabs (premium British) ---
cd /d "%~dp0"
if "%ELEVENLABS_API_KEY%"=="" (
  set /p ELEVENLABS_API_KEY="Pega tu ELEVENLABS_API_KEY y presiona ENTER: "
)
pip install --quiet elevenlabs
python generate_audios.py --provider elevenlabs --skip-existing
pause
