# Ashborn (Python Voice Assistant)

Voice-controlled assistant. Wake word "Ashborn" bolke activate karo.

## Install (sab platforms ke liye pehla step)

pip install -r requirements.txt

**Windows** pe agar pyaudio install nahi ho: pip install pipwin phir pipwin install pyaudio
**Mac** pe pehle: brew install portaudio phir pip install pyaudio
**Linux** pe pehle: sudo apt install portaudio19-dev python3-pyaudio

---

## 1️⃣ Windows / macOS / Linux (direct, mic ke saath)
python main.py

Bas itna hi — mic se sunega, wake word "jarvis" bolo, phir command bolo
(e.g. "time batao", "youtube kholo").

---

## 3️⃣ iPhone (Siri Shortcuts se)
... (Server + Shortcuts steps) ...

---

## Voice Badalni Hai?
jarvis/config.py mein EDGE_VOICE line change karo. ⚠️ Ye asli Solo Leveling
character ki awaaz clone nahi hai, ek similar vibe wali AI voice hai.

## Naya Skill Add Karna Hai?
jarvis/skills.py kholo, function likho, handle_command() mein map karo.

## Note
- Basic keyword-matching hai, natural NLU nahi.
- Google Speech Recognition use ho raha hai (internet chahiye).
