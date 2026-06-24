import os
from dotenv import load_dotenv

load_dotenv()

MELVIS_NAME = os.getenv("MELVIS_NAME")
USER_NAME = os.getenv("USER_NAME")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_URL = os.getenv("OLLAMA_URL")