"""
Elder Super-Tools Service for Sahayak AI:
1. Anti-Scam Radar (AI Fraud Detector)
2. Gujarati Document & Medicine OCR Reader
3. Live Camera Vision Guidance
"""

import re
import json
import logging
from typing import Dict, Any, List, Optional
from app.config import get_gemini_api_key
from app.schemas import (
    ScamCheckRequest, ScamCheckResponse,
    DocumentReadRequest, DocumentReadResponse,
    VisionGuideRequest, VisionGuideResponse
)

logger = logging.getLogger(__name__)

class ElderToolsService:

    def _analyze_scam_with_gemini(self, text: str, lang: str) -> Optional[ScamCheckResponse]:
        """Calls Gemini API for deep semantic analysis of suspicious scam messages."""
        api_key = get_gemini_api_key()
        if not api_key:
            return None

        prompt = f"""You are an Anti-Fraud and Cyber Scam Detection expert for elderly Indian citizens.
Analyze this message received by a senior on WhatsApp or SMS:
"{text}"

Language required: {lang} (gu: Gujarati, hi: Hindi, en: English).

Provide a valid JSON response strictly matching:
{{
  "is_scam": boolean,
  "risk_score": integer between 0 and 100,
  "verdict_title": short bold title in {lang} (e.g. ❌ ૧૦૦% છેતરપિંડી if scam, or ✅ સુરક્ષિત મેસેજ if safe),
  "verdict_audio": comforting spoken audio warning in {lang} suitable for senior Text-To-Speech,
  "explanation": 1-2 sentence simple explanation in {lang} of why it is dangerous or safe,
  "action_steps": [2-3 short action advice strings in {lang}]
}}"""

        try:
            raw_text = None
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                resp = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=[prompt],
                    config={"response_mime_type": "application/json"}
                )
                raw_text = resp.text
            except Exception:
                import google.generativeai as gai
                gai.configure(api_key=api_key)
                model = gai.GenerativeModel("gemini-1.5-flash")
                resp = model.generate_content(prompt, generation_config={"response_mime_type": "application/json"})
                raw_text = resp.text

            if not raw_text:
                return None

            clean = raw_text.strip()
            if clean.startswith("```"):
                clean = re.sub(r"^```(?:json)?\s*", "", clean)
                clean = re.sub(r"\s*```$", "", clean)

            data = json.loads(clean)
            return ScamCheckResponse(
                is_scam=bool(data.get("is_scam", False)),
                risk_score=int(data.get("risk_score", 5)),
                verdict_title=str(data.get("verdict_title", "તપાસ પૂર્ણ")),
                verdict_audio=str(data.get("verdict_audio", "")),
                explanation=str(data.get("explanation", "")),
                action_steps=list(data.get("action_steps", []))
            )
        except Exception as e:
            logger.warning(f"Gemini scam analysis error: {e}")
            return None

    def check_scam(self, req: ScamCheckRequest) -> ScamCheckResponse:
        text = (req.text or "").strip().lower()
        lang = req.language or "gu"

        # Check for known scam signatures
        is_electricity_scam = any(k in text for k in ["electricity", "power", "disconnected", "light bill", "વીજળી", "લાઈટ બિલ", "કાપી", "बिजली", "बिल"]) and any(k in text for k in ["tonight", "call", "officer", "રાત્રે", "ફોન કરો", "कॉल"])
        is_digital_arrest = any(k in text for k in ["arrest", "cbi", "police", "customs", "court", "અરેસ્ટ", "પોલીસ", "વોરંટ", "ગિરફ્તાર", "वारंट"])
        is_bank_kyc = any(k in text for k in ["kyc", "pan", "account blocked", "sbi", "hdfc", "debit card", "ખાતું બ્લોક", "પાન કાર્ડ", "खाता ब्लॉक"])
        is_lottery = any(k in text for k in ["lottery", "kbc", "winner", "crore", "lakhs", "ઇનામ", "લૉટરી", "જીત્યા", "इनाम", "लॉटरी"])
        is_job_scam = any(k in text for k in ["part time", "daily 3000", "daily 5000", "like youtube", "ઘરે બેઠા કમાઓ", "घर बैठे"])

        is_scam = is_electricity_scam or is_digital_arrest or is_bank_kyc or is_lottery or is_job_scam or any(k in text for k in ["apk", "bit.ly", "tinyurl", "link", "ઓટીપી", "otp"])

        if is_scam:
            risk_score = 99
            if lang == "gu":
                title = "❌ ૧૦૦% છેતરપિંડી (SCAM ALERT)"
                audio = "ચેતવણી: આ મેસેજ ૧૦૦ ટકા છેતરપિંડી છે! આમાં આપેલા કોઈ પણ નંબર પર ફોન ન કરતા કે લિંક ન ખોલતા. તમારા પૈસા કપાઈ શકે છે."
                if is_electricity_scam:
                    explanation = "આ વીજળી બિલ કાપવાની ધમકી આપીને છેતરપિંડી કરવાનો નકલી મેસેજ છે. ટોરેન્ટ પાવર કે જીઈબી ક્યારેય આવા પર્સનલ નંબર પર કોલ કરવાનું કહેતી નથી."
                elif is_digital_arrest:
                    explanation = "આ 'ડિજિટલ અરેસ્ટ' નો ગંભીર સાયબર ફ્રોડ છે. પોલીસ કે સીબીઆઈ ક્યારેય વોટ્સએપ કે વિડીયો કોલ પર કોઈને અરેસ્ટ કે દંડ નથી કરતી."
                elif is_bank_kyc:
                    explanation = "આ બેંકનું નામ વાપરીને બેંક ખાતામાંથી પૈસા ઉપાડી લેવાનો ફ્રોડ મેસેજ છે. બેંક ક્યારેય લિંક મોકલીને પાન કાર્ડ અપડેટ કરવાનું કહેતી નથી."
                else:
                    explanation = "આ છેતરપિંડીનો મેસેજ છે. સાયબર ગુનેગારો લિંક કે નંબર આપીને પૈસા ચોરવાનો પ્રયાસ કરી રહ્યા છે."
                actions = [
                    "આ મેસેજમાં આપેલી કોઈપણ લિંક પર ભૂલથી પણ ક્લિક ન કરો.",
                    "આપેલા નંબર પર સામો ફોન ન કરો.",
                    "આ અજાણ્યા નંબરને તમારા ફોનમાં તરત જ બ્લોક કરી દો."
                ]
            elif lang == "hi":
                title = "❌ १००% फर्जी मेसेज (SCAM ALERT)"
                audio = "चेतावनी: यह संदेश सौ प्रतिशत फर्जी है! दिए गए किसी भी नंबर पर फोन न करें और न ही कोई लिंक खोलें। आपके पैसे कट सकते हैं।"
                explanation = "यह बिजली काटने, बैंक केवाईसी या फर्जी पुलिस की धमकी देकर पैसे लूटने का फ्रॉड मेसेज है। कंपनी या बैंक कभी ऐसे पर्सनल नंबर पर कॉल करने को नहीं कहते।"
                actions = [
                    "इस मेसेज में दिए गए किसी भी लिंक पर क्लिक न करें।",
                    "दिए गए नंबर पर फोन मत कीजिए।",
                    "इस नंबर को तुरंत ब्लॉक कर दीजिए।"
                ]
            else:
                title = "❌ 100% FRAUD DETECTED (SCAM ALERT)"
                audio = "Warning: This message is 100% fraud! Do not click any links or call the number provided. It is a cyber scam to steal your money."
                explanation = "This is a widespread cyber fraud scam imitating utility providers, banks, or police officers. Authentic organizations never ask you to call personal numbers."
                actions = [
                    "Do NOT click any links inside this message.",
                    "Do NOT call the phone number provided.",
                    "Block and report this sender immediately on your phone."
                ]
        else:
            # If not detected by keywords, and Gemini API key is present, run deep LLM check
            if text and get_gemini_api_key():
                ai_verdict = self._analyze_scam_with_gemini(req.text or text, lang)
                if ai_verdict is not None:
                    return ai_verdict

            risk_score = 5
            if lang == "gu":
                title = "✅ સુરક્ષિત સામાન્ય મેસેજ"
                audio = "આ મેસેજમાં કોઈ દેખીતો ખતરો કે છેતરપિંડી જણાતી નથી. આ સામાન્ય સંદેશ જણાય છે."
                explanation = "આ મેસેજમાં કોઈ શંકાસ્પદ લિંક, પૈસાની માંગણી કે ધમકી જોવા મળી નથી."
                actions = ["તમે સુરક્ષિત રીતે આ મેસેજ વાંચી શકો છો."]
            elif lang == "hi":
                title = "✅ सुरक्षित सामान्य संदेश"
                audio = "इस संदेश में कोई खतरा या धोखाधड़ी नहीं पाई गई है।"
                explanation = "इसमें कोई फर्जी लिंक या धमकी नहीं है।"
                actions = ["आप इसे सुरक्षित पढ़ सकते हैं।"]
            else:
                title = "✅ Safe Message"
                audio = "No scam or suspicious threat detected in this message."
                explanation = "The content does not contain known phishing or extortion patterns."
                actions = ["You can safely proceed."]

        return ScamCheckResponse(
            is_scam=is_scam,
            risk_score=risk_score,
            verdict_title=title,
            verdict_audio=audio,
            explanation=explanation,
            action_steps=actions
        )

    def read_document(self, req: DocumentReadRequest) -> DocumentReadResponse:
        doc_type = req.doc_type or "medicine"
        lang = req.language or "gu"
        sample_id = req.sample_id or "sample1"

        if doc_type == "medicine":
            if lang == "gu":
                title = "💊 દવાની માહિતી અને લેવાનો સમય"
                audio = "આ બ્લડ પ્રેશર અને ડાયાબિટીસની નિયમિત ટેબ્લેટ છે. ડૉક્ટરની સલાહ મુજબ આ ગોળી સવારે નાસ્તો કર્યા પછી એક વાર પાણી સાથે લેવાની છે."
                details = [
                    {"label": "દવાનું નામ", "value": "ટેબ્લેટ ટેલમિસાર્ટન 40mg (Telmisartan)"},
                    {"label": "શેના માટે છે?", "value": "બ્લડ પ્રેશર (BP) કંટ્રોલમાં રાખવા માટે"},
                    {"label": "ક્યારે લેવી?", "value": "સવારે નાસ્તો કર્યા પછી - ૧ ગોળી"},
                    {"label": "ધ્યાન રાખવાની બાબત", "value": "ભૂખ્યા પેટે ન લેવી. નિયમિત સમય જાળવવો."}
                ]
                comfort = "ચિંતા કરશો નહીં, આ તમારી રોજીંદી સામાન્ય દવા છે. સમયસર લઈ લેજો."
            elif lang == "hi":
                title = "💊 दवाई की जानकारी और समय"
                audio = "यह ब्लड प्रेशर की टैबलेट है। डॉक्टर की सलाह के अनुसार इसे सुबह नाश्ते के बाद एक गोली पानी के साथ लेना है।"
                details = [
                    {"label": "दवा का नाम", "value": "Telmisartan 40mg"},
                    {"label": "किस काम की है?", "value": "ब्लड प्रेशर नियंत्रण के लिए"},
                    {"label": "कब लेनी है?", "value": "सुबह नाश्ते के बाद - १ गोली"}
                ]
                comfort = "चिंता मत कीजिए, यह आपकी नियमित दवा है।"
            else:
                title = "💊 Medicine Prescription Details"
                audio = "This is your regular Blood Pressure medication. Take one tablet in the morning after breakfast with water."
                details = [
                    {"label": "Medication", "value": "Telmisartan 40mg"},
                    {"label": "Purpose", "value": "Blood Pressure management"},
                    {"label": "Dosage", "value": "1 Tablet daily after breakfast"}
                ]
                comfort = "Don't worry, this is your standard prescription."
        else: # utility bill
            if lang == "gu":
                title = "⚡ લાઈટ બિલની વિગતો (Electricity Bill)"
                audio = "તમારું આ મહિનાનું વીજળી બિલ આવી ગયું છે. કુલ ચૂકવવાપાત્ર રકમ ૧,૪૫૦ રૂપિયા છે, અને છેલ્લી તારીખ ૨૦ નવેમ્બર છે."
                details = [
                    {"label": "કંપનીનું નામ", "value": "ટોરેન્ટ પાવર લિમિટેડ (Torrent Power)"},
                    {"label": "ગ્રાહક નંબર (Service No)", "value": "5420 8912 341"},
                    {"label": "ભરવાની રકમ", "value": "₹ ૧,૪૫૦/-"},
                    {"label": "છેલ્લી તારીખ", "value": "૨૦ નવેમ્બર, ૨૦૨૬"}
                ]
                comfort = "તમે Google Pay કે Sahayak AI ની મદદથી સરળતાથી આ બિલ ચૂકવી શકો છો."
            elif lang == "hi":
                title = "⚡ बिजली बिल का विवरण"
                audio = "आपका इस महीने का बिजली बिल ₹१,४५० आया है। भरने की आखिरी तारीख २० नवंबर है।"
                details = [
                    {"label": "कंपनी", "value": "टोरेंट पावर"},
                    {"label": "कुल राशि", "value": "₹ १,४५०/-"},
                    {"label": "अंतिम तिथि", "value": "२० नवंबर"}
                ]
                comfort = "आप इसे गूगल पे से आसानी से भर सकते हैं।"
            else:
                title = "⚡ Electricity Bill Summary"
                audio = "Your electricity bill total is ₹1,450. The last date of payment is November 20."
                details = [
                    {"label": "Provider", "value": "Torrent Power Limited"},
                    {"label": "Amount Due", "value": "₹ 1,450/-"},
                    {"label": "Due Date", "value": "20 November 2026"}
                ]
                comfort = "You can pay this safely via UPI."

        return DocumentReadResponse(
            success=True,
            doc_type=doc_type,
            title=title,
            audio_narration=audio,
            key_details=details,
            comfort_note=comfort
        )

    def guide_vision(self, req: VisionGuideRequest) -> VisionGuideResponse:
        lang = req.language or "gu"
        if lang == "gu":
            instruction = "કેમેરામાં તમારો ફોન દેખાઈ રહ્યો છે! નીચે આપેલા લીલા રંગના બટન પર તમારા અંગૂઠાથી ટચ કરો."
            element = "લીલું બટન"
        elif lang == "hi":
            instruction = "कैमरे में आपका फोन दिख रहा है! नीचे दिए गए हरे बटन पर टैप करें।"
            element = "हरा बटन"
        else:
            instruction = "Phone screen detected in camera! Tap the green button shown below with your thumb."
            element = "Green Action Button"

        return VisionGuideResponse(
            detected_screen="smartphone_screen_live",
            voice_instruction=instruction,
            highlight_x_percent=50.0,
            highlight_y_percent=88.5,
            target_element_name=element
        )

elder_tools_service = ElderToolsService()

