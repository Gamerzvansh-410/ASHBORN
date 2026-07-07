"""
Skills
------
Yahan har command ka logic hai. Naya skill add karna ho to
niche ek naya function likho aur handle_command() mein map kar do.
"""

import datetime
import webbrowser
import subprocess
import platform


def tell_time() -> str:
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"Abhi time hai {now}"


def tell_date() -> str:
    today = datetime.datetime.now().strftime("%d %B, %Y")
    return f"Aaj ki date hai {today}"


def open_website(site: str) -> str:
    urls = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "gmail": "https://mail.google.com",
        "whatsapp": "https://web.whatsapp.com",
    }
    url = urls.get(site)
    if url:
        webbrowser.open(url)
        return f"{site} khol raha hoon"
    return f"Mujhe {site} ka pata nahi hai"


def open_app(app_name: str) -> str:
    """Basic app opener — OS ke hisaab se command run karta hai."""
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.Popen(f"start {app_name}", shell=True)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", app_name])
        else:  # Linux
            subprocess.Popen([app_name])
        return f"{app_name} khol raha hoon"
    except Exception:
        return f"{app_name} nahi khul paya, check karo naam sahi hai kya"


def handle_command(command: str) -> str:
    """
    Command text lekar sahi skill call karta hai.
    Ye tumhara 'brain' hai — jitna chaaho utna badha sakte ho.
    """
    command = command.lower()

    if "time" in command:
        return tell_time()
    if "date" in command:
        return tell_date()
    if "open" in command:
        for site in ["youtube", "google", "gmail", "whatsapp"]:
            if site in command:
                return open_website(site)
        # agar website list mein nahi hai, app khol ke try karo
        app_name = command.replace("open", "").strip()
        if app_name:
            return open_app(app_name)
    if "stop" in command or "bye" in command or "exit" in command:
        return "__EXIT__"

    return "Sorry, ye command mujhe samajh nahi aayi. Thoda alag tarike se bolo."
