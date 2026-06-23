import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MELVIS_NAME = os.getenv("MELVIS_NAME", "Melvis")
USER_NAME = os.getenv("USER_NAME", "Elvis")