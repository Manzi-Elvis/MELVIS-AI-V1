import os
import webbrowser
import datetime
import subprocess
from melvis.memory import remember, load_memory

def handle_command(command):
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."

    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google."

    if "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    if "open vs code" in command or "open visual studio code" in command:
        os.system("code")
        return "Opening Visual Studio Code."

    if "time" in command:
        return datetime.datetime.now().strftime("The time is %I:%M %p.")

    if "date" in command:
        return datetime.datetime.now().strftime("Today is %A, %B %d, %Y.")

    if command.startswith("remember that"):
        return remember(command)

    if "what do you remember" in command:
        memory = load_memory()
        if not memory:
            return "I do not remember anything yet."
        return str(memory)

    opened = []

    if "chrome" in command:
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        opened.append("Chrome")

    if "github" in command:
        webbrowser.open("https://github.com")
        opened.append("GitHub")

    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        opened.append("YouTube")

    if "spotify" in command:
        os.system("start spotify:")
        opened.append("Spotify")

    if "vs code" in command or "vscode" in command or "visual studio code" in command:
        os.system("code")
        opened.append("VS Code")

    if opened:
        return "Opening " + ", ".join(opened) + "."

    return None

    return None