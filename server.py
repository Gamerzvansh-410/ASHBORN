"""
Jarvis - Remote Server
----------------------
Ye Windows/Mac/Linux PC pe chalao. Isse tumhara iPhone, Android,
ya koi bhi device Jarvis ko command bhej sakta hai — wifi ke through.

Chalane ka tareeka: python server.py
Phir dusre device se: http://<tumhare-PC-ka-IP>:8000/command?text=time%20batao

iPhone pe "Shortcuts" app mein ek "Get Contents of URL" action banao
jo is URL ko hit kare, aur response ko Siri bulwaye. README mein steps hain.
"""

from fastapi import FastAPI
from jarvis.skills import handle_command
import uvicorn

app = FastAPI(title="Jarvis Remote API")


@app.get("/command")
def run_command(text: str):
    """
    Example: /command?text=time batao
    Response: {"reply": "Abhi time hai 03:45 PM"}
    """
    reply = handle_command(text)
    if reply == "__EXIT__":
        reply = "Theek hai, bye!"
    return {"reply": reply}


@app.get("/")
def health_check():
    return {"status": "Jarvis online hai"}


if __name__ == "__main__":
    # host="0.0.0.0" zaroori hai taaki dusre devices bhi connect ho sakein
    uvicorn.run(app, host="0.0.0.0", port=8000)
