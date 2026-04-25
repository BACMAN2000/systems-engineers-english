@echo off
REM --- Generate Flyers Practice Audios using OpenAI TTS (British "fable" voice) ---
cd /d "%~dp0"
if "%OPENAI_API_KEY%"=="" (
  set /p OPENAI_API_KEY="Pega tu OPENAI_API_KEY y presiona ENTER: "
)
pip install --quiet openai
python generate_audios.py --provider openai --voice fable --skip-existing
pause
