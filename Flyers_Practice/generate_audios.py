"""
Flyers Practice Tests — Audio Generator (British English)
=========================================================

Generates MP3 audio files for the Listening section of all 10 Flyers practice tests.
Supports two TTS providers:

  1) OpenAI TTS   — cheap (~$0.50 total), good quality
  2) ElevenLabs   — ~$12 total, premium British voices (recommended for exam)

USAGE
-----
  # Install one of these:
  pip install openai
  # or
  pip install elevenlabs

  # Set your API key as environment variable:
  set OPENAI_API_KEY=sk-...                (Windows CMD)
  $env:OPENAI_API_KEY="sk-..."             (PowerShell)
  export OPENAI_API_KEY=sk-...             (macOS/Linux)

  # Or for ElevenLabs:
  set ELEVENLABS_API_KEY=...

  # Run:
  python generate_audios.py --provider openai
  python generate_audios.py --provider elevenlabs

OUTPUT
------
Creates folder ./audios/ with files named:
  test_01_part1.mp3, test_01_part2.mp3, ..., test_10_part5.mp3
(50 files total — 5 parts x 10 tests)

These names match what the web app (Flyers_Practice_App.html) expects.
"""
import os
import sys
import argparse
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flyers_content import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5
from flyers_content_2 import TEST_6, TEST_7, TEST_8, TEST_9, TEST_10

ALL_TESTS = [TEST_1, TEST_2, TEST_3, TEST_4, TEST_5,
             TEST_6, TEST_7, TEST_8, TEST_9, TEST_10]

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audios')
os.makedirs(OUT_DIR, exist_ok=True)


# ----------------------------------------------------------------------
# Build the listening script text for each part from the content dict.
# We include the standard Cambridge-style intro + instructions + item
# pauses. This yields a single continuous audio per part.
# ----------------------------------------------------------------------
INTRO = ("Cambridge English, A2 Flyers, Listening Test {n}. "
         "You will hear five conversations. For each question, there are "
         "three pictures and a short conversation. You will hear each "
         "conversation twice. There is one example. [pause]  ")


def _pause(seconds=1.5):
    """Insert a pause marker. Different TTS handle this differently;
    we use natural punctuation to trigger it."""
    return ". ... " + ("... " * int(seconds))


def _build_part_script(test_num, part_num, part_data):
    """Convert a 'scripts' dict entry into a narratable paragraph."""
    n = test_num
    p = part_num
    if isinstance(part_data, str):
        body = part_data
    elif isinstance(part_data, dict):
        # Common shapes: {'intro': ..., 'items': [...]}, or {'text': ...}
        body_parts = []
        if 'intro' in part_data:
            body_parts.append(part_data['intro'])
        if 'text' in part_data:
            body_parts.append(part_data['text'])
        if 'items' in part_data:
            for i, item in enumerate(part_data['items']):
                if isinstance(item, str):
                    body_parts.append(f"Number {i+1}. {item} {_pause(2)}")
                elif isinstance(item, dict) and 'text' in item:
                    body_parts.append(f"Number {i+1}. {item['text']} {_pause(2)}")
        body = " ".join(body_parts)
    elif isinstance(part_data, list):
        body = " ".join(
            f"Number {i+1}. {x} {_pause(2)}" if isinstance(x, str) else ""
            for i, x in enumerate(part_data)
        )
    else:
        body = str(part_data)

    header = f"Flyers Listening. Test {n}. Part {p}. {_pause(1)}"
    return header + body + _pause(2) + f"That is the end of Part {p}."


def collect_scripts():
    """Return list of (filename, text) tuples ready for TTS."""
    out = []
    for t in ALL_TESTS:
        n = t['number']
        scripts = t.get('scripts', {})
        for p in range(1, 6):
            key = f'p{p}'
            part_data = scripts.get(key)
            if part_data is None:
                # Fallback: use the listening questions themselves as prompt
                listening = t.get('listening', {}).get(key, {})
                part_data = str(listening)
            text = _build_part_script(n, p, part_data)
            fname = f'test_{n:02d}_part{p}.mp3'
            out.append((fname, text))
    return out


# ----------------------------------------------------------------------
# OpenAI TTS
# ----------------------------------------------------------------------
def tts_openai(text, out_path, voice='alloy'):
    """
    OpenAI TTS. Voices: alloy, echo, fable (British!), onyx, nova, shimmer.
    We use 'fable' for a British-sounding narrator.
    Model: 'tts-1' (cheaper) or 'tts-1-hd' (higher quality).
    """
    from openai import OpenAI
    client = OpenAI()  # reads OPENAI_API_KEY from env
    resp = client.audio.speech.create(
        model='tts-1-hd',
        voice=voice,
        input=text[:4000],   # hard limit ~4096 chars
    )
    resp.stream_to_file(out_path)


# ----------------------------------------------------------------------
# ElevenLabs TTS
# ----------------------------------------------------------------------
ELEVEN_VOICES = {
    # Curated British voices (as of 2025).
    # You can change these IDs after browsing https://elevenlabs.io/voice-library
    'narrator':   'ThT5KcBeYPX3keUQqHPh',   # "Dorothy" - British female, warm
    'teacher_f':  'XB0fDUnXU5powFXDhCwa',   # "Charlotte" - British female, clear
    'teacher_m':  'pNInz6obpgDQGcFmaJgB',   # "Adam" - neutral; swap for British male
    'child_a':    'jBpfuIE2acCO8z3wKNLl',   # "Gigi" - younger female
    'child_b':    'AZnzlk1XvdvUeBnXmlld',   # "Domi" - young female
}


def tts_elevenlabs(text, out_path, voice_id=None):
    """ElevenLabs TTS. Uses 'eleven_multilingual_v2' model."""
    from elevenlabs.client import ElevenLabs
    client = ElevenLabs()   # reads ELEVENLABS_API_KEY
    if voice_id is None:
        voice_id = ELEVEN_VOICES['narrator']
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        text=text,
        model_id='eleven_multilingual_v2',
        output_format='mp3_44100_128',
    )
    with open(out_path, 'wb') as f:
        for chunk in audio:
            if chunk:
                f.write(chunk)


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--provider', choices=['openai', 'elevenlabs'],
                    default='openai')
    ap.add_argument('--voice', default=None,
                    help='OpenAI voice (alloy|echo|fable|onyx|nova|shimmer) '
                         'or ElevenLabs voice_id')
    ap.add_argument('--only', type=int, default=None,
                    help='Generate only this test number (1-10)')
    ap.add_argument('--skip-existing', action='store_true',
                    help='Skip files that already exist')
    args = ap.parse_args()

    jobs = collect_scripts()
    if args.only:
        jobs = [j for j in jobs if j[0].startswith(f'test_{args.only:02d}_')]

    print(f'Provider: {args.provider}   Files to generate: {len(jobs)}')
    print(f'Output folder: {OUT_DIR}\n')

    for i, (fname, text) in enumerate(jobs, 1):
        out_path = os.path.join(OUT_DIR, fname)
        if args.skip_existing and os.path.exists(out_path):
            print(f'[{i}/{len(jobs)}] skip (exists): {fname}')
            continue
        print(f'[{i}/{len(jobs)}] {fname}  ({len(text)} chars)')
        try:
            if args.provider == 'openai':
                voice = args.voice or 'fable'
                tts_openai(text, out_path, voice=voice)
            else:
                tts_elevenlabs(text, out_path, voice_id=args.voice)
            time.sleep(0.3)   # be gentle on rate limits
        except Exception as e:
            print(f'   ERROR: {e}')

    print('\nDone. Audios saved to:', OUT_DIR)


if __name__ == '__main__':
    main()
