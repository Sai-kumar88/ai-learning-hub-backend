import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration settings."""
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")
    JSON_SORT_KEYS = False

    # Directory Paths
    BASE_DIR = Path(__file__).resolve().parent
    DATA_FOLDER = BASE_DIR / "data"
    COURSES_FILE = DATA_FOLDER / "courses.json"
    FRONTEND_DIST = BASE_DIR / "frontend" / "dist"

    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))