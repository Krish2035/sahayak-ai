import re
from typing import Tuple

# Common stopwords and transliteration markers
GUJARATI_ROMAN_MARKERS = [
    "mane", "tame", "kevi", "rite", "moklu", "moklavo", "che", "chhe", "bhai",
    "bija", "karvanu", "karo", "aapo", "su", "shu", "kya", "kyathi", "maro",
    "mari", "maru", "joie", "kem", "aavi", "nathi"
]

HINDI_ROMAN_MARKERS = [
    "kaise", "kare", "karein", "karna", "hai", "mujhe", "apne", "kisi", "bhejna",
    "bheju", "bheje", "kholo", "dekhna", "batao", "chahiye", "nahi", "ho",
    "raha", "rahi", "karo", "pe", "par", "se", "ko", "kya"
]

MARATHI_ROMAN_MARKERS = [
    "kasa", "kashi", "karaycha", "karaychi", "ahe", "mala", "pathvaycha",
    "pathva", "dakhva", "sang", "sanga"
]

def detect_language_and_script(text: str) -> Tuple[str, str]:
    """
    Detects language code and language name.
    Returns: (lang_code, lang_name) e.g. ('gu', 'Gujarati')
    """
    if not text or not text.strip():
        return "en", "English"

    # 1. Check Unicode Character Ranges
    gujarati_chars = len(re.findall(r'[\u0A80-\u0AFF]', text))
    devanagari_chars = len(re.findall(r'[\u0900-\u097F]', text))
    tamil_chars = len(re.findall(r'[\u0B80-\u0BFF]', text))
    telugu_chars = len(re.findall(r'[\u0C00-\u0C7F]', text))
    bengali_chars = len(re.findall(r'[\u0980-\u09FF]', text))

    max_script_chars = max(gujarati_chars, devanagari_chars, tamil_chars, telugu_chars, bengali_chars)

    if max_script_chars > 2:
        if max_script_chars == gujarati_chars:
            return "gu", "Gujarati"
        if max_script_chars == devanagari_chars:
            # Check for Marathi-specific words in Devanagari if needed, else Hindi
            if any(w in text for w in ["कसे", "करावे", "पाठवा", "आहे", "मला"]):
                return "mr", "Marathi"
            return "hi", "Hindi"
        if max_script_chars == tamil_chars:
            return "ta", "Tamil"
        if max_script_chars == telugu_chars:
            return "te", "Telugu"
        if max_script_chars == bengali_chars:
            return "bn", "Bengali"

    # 2. Check Romanized / Latin script transliteration
    lower_words = set(re.findall(r'\b[a-z]+\b', text.lower()))
    
    gu_matches = sum(1 for w in lower_words if w in GUJARATI_ROMAN_MARKERS)
    hi_matches = sum(1 for w in lower_words if w in HINDI_ROMAN_MARKERS)
    mr_matches = sum(1 for w in lower_words if w in MARATHI_ROMAN_MARKERS)

    if gu_matches > 0 and gu_matches >= hi_matches:
        return "gu", "Gujarati"
    if mr_matches > 0 and mr_matches >= hi_matches:
        return "mr", "Marathi"
    if hi_matches > 0:
        return "hi", "Hindi"

    return "en", "English"

