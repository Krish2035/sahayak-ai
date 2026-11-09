# Sahayak AI (Digital Companion for Seniors) 👵👴
> A voice-first, visual step-by-step smartphone assistant designed for elderly parents (60+ years old) in their native language (Gujarati, Hindi, English).

---

## 🌟 The Real-World Incident Solved
Inspired by the real experience of needing to guide a father on how to send someone's phone number on WhatsApp while at a salon:
- **No typing required**: Tap a giant mic button and speak naturally (*"Mane WhatsApp ma bhai no number bija ne moklavo che"*).
- **Show, Don't Just Tell**: Displays real app screens with a **glowing, pulsing red ring** pointing directly at the button to press.
- **Paced Native Voice**: The app speaks each step out loud calmly in Gujarati, Hindi, or English.
- **Reassurance**: *"Don't worry, nothing will get deleted."*
- **Share Guide with Dad**: Generates a 1-tap WhatsApp message to send the full step-by-step guide directly to your parent.

---

## 📁 Project Structure

```
AI/
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI server & static file host
│   │   ├── config.py                # Configuration & supported languages
│   │   ├── schemas.py               # Pydantic data schemas
│   │   ├── services/
│   │   │   ├── intent_parser.py     # Gemini pipeline & verified flow matcher
│   │   │   ├── language_detector.py # Gujarati, Hindi, Marathi, Tamil detector
│   │   │   └── prompts.py           # Senior-friendly system prompts
│   │   └── data/
│   │       └── preloaded_flows.py   # Verified 6-step flows (WhatsApp, GPay, Settings)
│   ├── requirements.txt
│   ├── .env.example
│   ├── test_backend.py              # Test suite for intent and language detection
│   └── test_browser_experience.py   # Comprehensive 20-point UI & flow verification
│
└── frontend/
    ├── index.html                   # ChatGPT-Style Systematic Visual Guide UI
    ├── css/
    │   └── styles.css               # Conversational feed, systematic cards, pulse engine
    ├── js/
    │   └── app.js                   # Web Speech STT, TTS, Feed Renderer & WhatsApp Share
    └── assets/
        └── screens/
            ├── whatsapp_phone_home.svg       # Step 1: Phone Home Screen with WhatsApp
            ├── whatsapp_chat_list.svg        # Step 2: Chat List Screen
            ├── whatsapp_chat_screen.svg      # Step 3: Chat Screen with Paperclip 📎
            ├── whatsapp_attachment_menu.svg  # Step 4: Popup Menu with Contact 👤
            ├── whatsapp_contact_search.svg   # Step 5: Search & Select Contact
            ├── whatsapp_contact_picker.svg   # Step 6: Send Arrow ➡️ Screen
            ├── whatsapp_photo_preview.svg
            ├── gpay_home.svg
            ├── gpay_scanner.svg
            ├── gpay_amount.svg
            └── settings_home.svg
```

---

## 🚀 How to Run the App

### Option A: The 1-Step Root Launcher (Recommended)
From the project root (`f:\krish\AI`), simply run:
```bash
python run.py
```

### Option B: Direct Backend Entrypoint
```bash
python backend/app/main.py
```

---

### Step 2: Open in Your Browser or Phone
Open your browser and navigate to:
👉 **`http://127.0.0.1:8000`**
*(On your phone on the same Wi-Fi, open `http://<YOUR_COMPUTER_IP>:8000`)*

---

## 🎙️ Testing Queries

Try speaking or clicking any of these test scenarios:
1. **The Father's Incident (Gujarati)**:
   - *"વોટ્સએપ પર કોઈનો નંબર કેવી રીતે મોકલવો?"* (or *"mane mara bhai no number whatsapp par bija ne moklavo che"*)
2. **Hindi WhatsApp Contact**:
   - *"व्हाट्सएप पर किसी का कांटेक्ट नंबर कैसे भेजें?"*
3. **Google Pay QR Scan**:
   - *"દુકાને ક્યૂઆર કોડ સ્કેન કરીને પેમેન્ટ કેમ કરવું?"*
4. **Phone Settings (Font Size)**:
   - *"ફોનમાં અક્ષરો મોટા કેવી રીતે કરવા?"*

---

## 🔑 Adding Your Free Gemini API Key (Optional)
The system works out of the box with the verified curated flows. To enable dynamic AI generation for any arbitrary question:
1. Copy `.env.example` to `backend/.env`.
2. Add your free key from [Google AI Studio](https://aistudio.google.com/):
   ```env
   GEMINI_API_KEY=your_key_here
   ```

