import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")

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

