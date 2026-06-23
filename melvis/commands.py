import os
import webbrowser
import datetime
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

    return None