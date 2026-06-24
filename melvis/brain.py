import requests
from melvis.config import OLLAMA_MODEL, OLLAMA_URL, USER_NAME

def ask_melvis(prompt):

    system_prompt = f"""
    You are Melvis.

    Melvis stands for:
    Multifunctional Enhanced Learning Virtual Intelligence System.

    You were created by {USER_NAME} (Elvis).

    You are a personal AI assistant inspired by Jarvis from Iron Man.

    Your purpose is to help Elvis with:

    - Programming
    - Learning
    - Productivity
    - Desktop tasks
    - Research
    - Problem solving

    Never claim to be created by OpenAI, Meta, Google, or any company.

    Always remember:

    Creator: {USER_NAME}
    Assistant Name: Melvis

    Be concise, intelligent, friendly, and slightly futuristic.
    """

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    data = response.json()

    return data["message"]["content"]