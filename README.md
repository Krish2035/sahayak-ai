# Sahayak AI (Digital Companion for Seniors) 👵📱👴
> A voice-first, systematic visual smartphone assistant designed for elderly parents (60+ years old) in their native languages (Gujarati, Hindi, English).

---

## 🌟 The Real-World Incident Solved
Inspired by the real experience of needing to guide a father on how to send someone's phone number on WhatsApp while at a salon:
- **No typing required**: Tap a giant mic button and speak naturally (*"Mane WhatsApp ma bhai no number bija ne moklavo che"*).
- **Show, Don't Just Tell**: Displays real app screens with a **glowing, pulsing red ring** pointing directly at the button to press.
- **Paced Native Voice**: The app speaks each step out loud calmly in Gujarati, Hindi, or English.
- **Hands-Free Voice Navigation**: Speak *"Next"* or *"આગળ"* to mark steps done and scroll down automatically.
- **Reassurance**: *"Don't worry, nothing will get deleted."*
- **1-Tap Daylight High Contrast Mode**: Instant switch between Dark Teal and pure black-on-white high contrast for cataract-friendly reading under sunlight.
- **Share Guide with Dad**: Generates a 1-tap WhatsApp message to send the full step-by-step guide directly to your parent.

---

## 🛡️ 6 Elder Innovation Super-Tools
1. 🛡️ **Anti-Scam Radar (રક્ષા કવચ)**: Detects electricity disconnection SMS, digital arrest threats, fake bank KYC, and lottery scams with audio alarms.
2. 👁️ **Live Camera Screen Vision (લાઈવ કેમેરા ગાઈડ)**: Point camera at any physical smartphone screen for interactive highlighted voice guidance.
3. 🧪 **Zero-Risk Safe Sandbox (સેફ પ્રેક્ટિસ મોડ)**: Realistic dummy Google Pay UPI PIN keypad to practice payments with zero real money risk.
4. 👨‍👩‍👧 **Family Bridge (ફેમિલી બ્રિજ)**: 1-tap WhatsApp alert and direct SOS call to son/daughter when stuck on any step.
5. 💊 **Gujarati Document & Medicine OCR Reader (દવા & બિલ રીડર)**: Photo voice reader for medicine dosage and electricity bills.
6. 🎈 **Android Floating Bubble (ફ્લોટિંગ બબલ)**: Interactive overlay avatar preview and 1-tap PWA install guide.

---

## 📚 15 Core Senior Task Flows
1. **WhatsApp Contact Sharing** (*વોટ્સએપ પર કોઈનો નંબર મોકલવો*)
2. **WhatsApp Photo Sharing** (*વોટ્સએપ પર ફોટો મોકલવો*)
3. **Google Pay QR Scan & Pay** (*દુકાને QR કોડ સ્કેન કરીને પેમેન્ટ કરવું*)
4. **Phone Settings: Font Size** (*ફોનમાં અક્ષરો મોટા કરવા*)
5. **YouTube Bhajan Download** (*YouTube પર ભજન કેવી રીતે ડાઉનલોડ કરવું?*)
6. **WhatsApp Live Location** (*WhatsApp પર લાઈવ લોકેશન કેમ મોકલવું?*)
7. **Block Unknown Spam Calls** (*અજાણ્યા ફોન નંબર બ્લોક કેમ કરવા?*)
8. **WhatsApp Voice Audio Message** (*વોટ્સએપ પર બોલીને અવાજનો મેસેજ કેમ મોકલવો?*)
9. **Google Maps Navigate Home** (*ઘરે જવાનો રસ્તો ગૂગલ મેપ્સમાં કેમ જોવો?*)
10. **Set Morning Alarm** (*સવારે ૬ વાગ્યાનું એલાર્મ કેમ સેટ કરવું?*)
11. **Exit WhatsApp Group** (*વોટ્સએપ ગ્રુપમાંથી બહાર કેમ નીકળવું?*)
12. **Increase Ringtone Volume** (*ફોનની રીંગટોનનો અવાજ મોટો કેમ કરવો?*)
13. **Toggle Mobile Data / Wi-Fi** (*મોબાઈલ ઇન્ટરનેટ ડેટા કેમ ચાલુ બંધ કરવો?*)
14. **View WhatsApp Status & Stories** (*વોટ્સએપમાં લોકોના સ્ટેટસ ફોટા કેમ જોવા?*)
15. **Speed Up Charging & Clear Apps** (*ફોન ધીમો ચાર્જ થાય છે શું કરવું?*)

---

## 📁 Project Structure

```
AI/
├── backend/
│   ├── app/
│   │   ├── main.py                  # FastAPI server & API endpoints
│   │   ├── config.py                # Configuration & supported languages
│   │   ├── schemas.py               # Pydantic data schemas
│   │   ├── services/
│   │   │   ├── intent_parser.py     # Multi-flow matching engine
│   │   │   ├── elder_tools_service.py # Scam radar, doc reader & vision logic
│   │   │   ├── language_detector.py # Gujarati, Hindi, Marathi, Tamil detector
│   │   │   └── prompts.py           # Senior-friendly system prompts
│   │   └── data/
│   │       └── preloaded_flows.py   # Verified 15 preloaded task flows
│   ├── requirements.txt
│   ├── test_backend.py              # Backend test suite
│   └── test_browser_experience.py   # 25-point visual and conversational tests
│
└── frontend/
    ├── index.html                   # High-contrast UI with 6 Elder Modals
    ├── css/
    │   └── styles.css               # Dark & Daylight themes, responsive 840px grid
    ├── js/
    │   └── app.js                   # Speech Recognition, TTS, Live Voice Nav & Modals
    └── assets/
        └── screens/                 # SVG screen mockups (400x750 aspect ratio)
```

---

## 🚀 How to Run Locally

```bash
# Start backend server
python backend/app/main.py
```
Open **`http://127.0.0.1:8000`** in your browser.

---

## 🌐 Deployments
- **GitHub Repository**: [https://github.com/Krish2035/sahayak-ai](https://github.com/Krish2035/sahayak-ai)
- **Live Render Backend**: [https://sahayak-ai-m58x.onrender.com](https://sahayak-ai-m58x.onrender.com)
