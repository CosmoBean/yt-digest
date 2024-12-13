import os

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("API_KEY", "default_api_key")
    DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "downloads")
    MODEL_TYPE = os.getenv("MODEL_TYPE", "base")
