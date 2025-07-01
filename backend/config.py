import os
from dotenv import load_dotenv
load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL","llama2")
