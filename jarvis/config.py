"""
Jarvis Config
-------------
Saari settings yahan rakho — wake word, voice speed, etc.
"""

WAKE_WORD = "ashborn"          # Bolke isse activate hoga

# Edge-TTS Voice — deep/commanding tone ke liye ye options try karo:
#   "en-US-GuyNeural"          -> deep, confident (recommended)
#   "en-US-ChristopherNeural"  -> deep, calm, mature
#   "en-GB-RyanNeural"         -> British, sharp tone
# Full list dekhne ke liye terminal mein: edge-tts --list-voices
EDGE_VOICE = "en-US-GuyNeural"

# Speaking rate control (Edge-TTS format, e.g. "+0%", "-10%", "+15%")
EDGE_RATE = "+0%"
