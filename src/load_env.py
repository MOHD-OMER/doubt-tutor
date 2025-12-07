import os
from dotenv import load_dotenv
from pathlib import Path

# --------------------------------------------------
# Locate Project Root (.env should be in root folder)
# --------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"

# --------------------------------------------------
# Load .env File
# --------------------------------------------------
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
    print(f"[load_env] Loaded .env from: {ENV_PATH}")
else:
    print(f"[load_env] WARNING: .env file NOT FOUND at {ENV_PATH}")

# --------------------------------------------------
# Optional: Debugging to ensure keys were loaded
# --------------------------------------------------
def debug_env():
    groq = os.getenv("GROQ_API_KEY")
    hf = os.getenv("HF_TOKEN")

    print(f"[load_env] GROQ_API_KEY: {'SET' if groq else 'NOT SET'}")
    print(f"[load_env] HF_TOKEN: {'SET' if hf else 'NOT SET'}")

# Run debug check
debug_env()
