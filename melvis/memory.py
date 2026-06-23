import json
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")

def load_memory():
    if not MEMORY_FILE.exists():
        return {}

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def save_memory(key, value):
    memory = load_memory()
    memory[key] = value

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def remember(command):
    text = command.replace("remember that", "").strip()

    if " is " in text:
        key, value = text.split(" is ", 1)
        save_memory(key.strip(), value.strip())
        return f"I will remember that {key.strip()} is {value.strip()}."

    return "Tell me what to remember using: remember that your name is Elvis."