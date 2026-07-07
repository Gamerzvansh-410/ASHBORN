"""
Speech-to-Text (STT)
--------------------
Microphone se sunke text mein convert karta hai.
"""

import speech_recognition as sr

_recognizer = sr.Recognizer()


def listen(timeout: int = 5, phrase_time_limit: int = 8) -> str:
    """
    Microphone se sunta hai aur text return karta hai.
    Kuch samajh na aaye to empty string return karega.
    """
    with sr.Microphone() as source:
        _recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Sun raha hoon...")
        try:
            audio = _recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""

    try:
        text = _recognizer.recognize_google(audio, language="en-IN")
        print(f"Tumne bola: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        print("Internet check karo — speech recognition service tak nahi pahunch paya.")
        return ""
