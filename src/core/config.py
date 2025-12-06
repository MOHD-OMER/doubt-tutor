"""
Configuration management for Doubt Tutor
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration"""

    # Base directory (project root)
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

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

    # Tesseract OCR
    TESSERACT_PATH = os.getenv(
        "TESSERACT_PATH",
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    # File upload limits
    MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", "10"))
    MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

    # Allowed file extensions
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

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def ensure_directories(cls):
        """Ensure required directories exist"""
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.DATABASE_DIR.mkdir(parents=True, exist_ok=True)
        cls.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


# Initialize directories on import
Config.ensure_directories()
