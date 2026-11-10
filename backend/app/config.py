import os
from pathlib import Path
from dotenv import load_dotenv

# Robustly find and load .env from backend folder, project root, or cwd
current_file = Path(__file__).resolve()
backend_dir = current_file.parent.parent
root_dir = backend_dir.parent

env_paths = [
    backend_dir / ".env",
    root_dir / ".env",
    Path(".env")
]

for p in env_paths:
    if p.is_file():
        load_dotenv(dotenv_path=p, override=False)

# Catch-all for environment or cwd
load_dotenv()

def get_gemini_api_key() -> str:
    """Returns the currently configured GEMINI_API_KEY from environment."""
    return os.getenv("GEMINI_API_KEY", "").strip()

GEMINI_API_KEY = get_gemini_api_key()
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

# Database & Redis Settings
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

REDIS_URL = os.getenv("REDIS_URL", "").strip()
RATE_LIMIT_DEFAULT = os.getenv("RATE_LIMIT_DEFAULT", "10/minute")

# Supported Languages Mapping
SUPPORTED_LANGUAGES = {
    "gu": {"name": "Gujarati", "native": "ગુજરાતી", "stt_code": "gu-IN", "tts_lang": "gu-IN"},
    "hi": {"name": "Hindi", "native": "हिन्दी", "stt_code": "hi-IN", "tts_lang": "hi-IN"},
    "mr": {"name": "Marathi", "native": "मराठी", "stt_code": "mr-IN", "tts_lang": "mr-IN"},
    "ta": {"name": "Tamil", "native": "தமிழ்", "stt_code": "ta-IN", "tts_lang": "ta-IN"},
    "te": {"name": "Telugu", "native": "తెలుగు", "stt_code": "te-IN", "tts_lang": "te-IN"},
    "bn": {"name": "Bengali", "native": "বাংলা", "stt_code": "bn-IN", "tts_lang": "bn-IN"},
    "en": {"name": "English", "native": "English", "stt_code": "en-IN", "tts_lang": "en-IN"}
}


