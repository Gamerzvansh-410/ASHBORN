"""
Text-to-Speech (TTS) — Edge-TTS version
----------------------------------------
Microsoft Edge ki online neural voices use karta hai — bahut realistic
sunta hai, insaan jaisa. Internet chahiye iske liye.
"""

import asyncio
import os
import tempfile
import edge_tts
from playsound import playsound
from jarvis.config import EDGE_VOICE, EDGE_RATE

_AUDIO_FILE = os.path.join(tempfile.gettempdir(), "jarvis_voice.mp3")


async def _generate_audio(text: str):
    communicate = edge_tts.Communicate(text, voice=EDGE_VOICE, rate=EDGE_RATE)
    await communicate.save(_AUDIO_FILE)


def speak(text: str):
    """Jarvis ko bolwane ke liye ye function call karo."""
    print(f"Jarvis: {text}")
    try:
        asyncio.run(_generate_audio(text))
        playsound(_AUDIO_FILE)
    except Exception as e:
        print(f"Voice generate nahi ho payi (internet check karo): {e}")
