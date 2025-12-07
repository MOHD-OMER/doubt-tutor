"""
Configuration management for Doubt Tutor
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# -----------------------------------------------------------
# 🔍 1. Compute absolute path to project root .env
# -----------------------------------------------------------
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"

print("\n===== DEBUG PATH CHECK =====")
print("Calculated ENV_PATH:", ENV_PATH)
print("Exists?:", ENV_PATH.exists())
print("============================\n")

# -----------------------------------------------------------
# 🔐 2. Load .env from this exact path
# -----------------------------------------------------------
load_dotenv(dotenv_path=ENV_PATH)

print("DEBUG GROQ KEY:", os.getenv("GROQ_API_KEY"))
print("DEBUG GEMINI KEY:", os.getenv("GEMINI_API_KEY"))
print("--------------------------------------------------\n")


class Config:
    """Application configuration"""

    BASE_DIR = Path(__file__).resolve().parents[2]

    # Paths
    DATA_DIR = BASE_DIR / "data"
    DATABASE_DIR = BASE_DIR / "database"
    LOGS_DIR = BASE_DIR / "logs"
    UPLOAD_DIR = BASE_DIR / "uploads"

    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{(DATABASE_DIR / 'doubt_tutor.db').as_posix()}"
    )

    # OCR
    TESSERACT_PATH = os.getenv(
        "TESSERACT_PATH",
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    # File limits
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

    # File extensions
    ALLOWED_EXTENSIONS = {
        "pdf": "application/pdf",
        "txt": "text/plain",
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
    }

    # AI Models
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "llama3.2")
    DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
    DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "2000"))

    # API KEYS
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def ensure_directories(cls):
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


Config.ensure_directories()
