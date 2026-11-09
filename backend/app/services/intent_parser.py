import json
import logging
from typing import Optional, Dict, Any

from app.config import GEMINI_API_KEY
from app.schemas import QueryResponse, IntentResult, StepItem, TargetCoordinate
from app.services.language_detector import detect_language_and_script
from app.services.prompts import SENIOR_GUIDE_SYSTEM_PROMPT, build_user_prompt
from app.data.preloaded_flows import PRELOADED_FLOWS

logger = logging.getLogger(__name__)

class IntentParserService:
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.gemini_client = None
        self._init_gemini()

    def _init_gemini(self):
        """Initializes Gemini API client if API key is present."""
        if not self.api_key:
            logger.info("No GEMINI_API_KEY set. Operating in offline/curated flow mode.")
            return

        try:
            from google import genai
            self.gemini_client = genai.Client(api_key=self.api_key)
            logger.info("Initialized google-genai Client successfully.")
        except Exception as e:
            logger.warning(f"Failed to initialize google-genai: {e}. Trying google.generativeai fallback.")
            try:
                import google.generativeai as gai
                gai.configure(api_key=self.api_key)
                self.gemini_client = gai.GenerativeModel("gemini-1.5-flash")
                logger.info("Initialized google.generativeai fallback successfully.")
            except Exception as e2:
                logger.error(f"Could not initialize Gemini: {e2}")

    def parse_query(self, query: str, preferred_lang: Optional[str] = "auto", platform: str = "android") -> QueryResponse:
        """
        Main entry point for analyzing user voice transcript or text query.
        1. Detects language (Gujarati, Hindi, English, etc.)
        2. Checks Curated Preloaded Flow matching (high-speed & 100% verified)
        3. If no preloaded match or custom request, calls Gemini LLM
        4. Returns validated QueryResponse
        """
        query_clean = query.strip()
        
        # Step 1: Detect Language
        detected_lang_code, detected_lang_name = detect_language_and_script(query_clean)
        active_lang = detected_lang_code if preferred_lang in (None, "", "auto") else preferred_lang

        # Step 2: Extract Recipient if present
        target_recipient = self._extract_recipient(query_clean, active_lang)

        # Step 3: Match with Preloaded Flows (Instant, Pixel-Perfect)
        matched_flow = self._match_preloaded_flow(query_clean, active_lang, platform, target_recipient)
        if matched_flow:
            return matched_flow

        # Step 4: If Gemini client available, run dynamic LLM prompt pipeline
        if self.gemini_client:
            llm_response = self._call_gemini_pipeline(query_clean, active_lang, platform, target_recipient)
            if llm_response:
                return llm_response

        # Step 5: Fallback default response
        return self._generate_graceful_fallback(query_clean, active_lang, detected_lang_name, platform)

    def _extract_recipient(self, query: str, lang: str) -> Optional[str]:
        """Extracts person/relationship if mentioned in the query."""
        lower = query.lower()
        relationships = {
            "bhai": "Brother", "brother": "Brother", "daddy": "Father", "papa": "Father",
            "mummy": "Mother", "baa": "Mother/Grandmother", "friend": "Friend",
            "dost": "Friend", "sister": "Sister", "ben": "Sister", "doctor": "Doctor"
        }
        for word, label in relationships.items():
            if word in lower:
                return label
        return None

    def _match_preloaded_flow(self, query: str, lang: str, platform: str, recipient: Optional[str]) -> Optional[QueryResponse]:
        """Checks if the query matches our verified top senior tasks."""
        lower = query.lower()
        
        # Check Font Size first if query mentions font or akshar
        if any(k in lower for k in ["font", "size", "bigger text", "akshar", "mota", "મોટા", "अक्षर बड़े", "अक्षर", "लिखावट"]):
            flow_data = PRELOADED_FLOWS["settings_font_size"]
            lang_key = lang if lang in flow_data["flows"] else "en"
            selected_content = flow_data["flows"][lang_key]
            steps = [
                StepItem(
                    step_number=s["step_number"],
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s["target_ui_element"],
                    target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                    audio_text=s["audio_text"],
                    screen_type=s["screen_type"],
                    reassurance=s.get("reassurance")
                )
                for s in selected_content["steps"]
            ]
            return QueryResponse(
                success=True,
                query=query,
                intent_info=IntentResult(
                    app_name="Settings",
                    intent="increase_font_size",
                    confidence=0.98,
                    platform=platform,
                    detected_language=lang,
                    language_name=self._get_lang_name(lang),
                    target_recipient=None
                ),
                title=selected_content["title"],
                summary=selected_content["summary"],
                reassurance_banner=selected_content["reassurance_banner"],
                total_steps=len(steps),
                steps=steps
            )

        # Check WhatsApp Send Photo first if photo/image mentioned
        if any(k in lower for k in ["photo", "picture", "image", "ફોટો", "તસવીર", "फोटो", "तस्वीर"]):
            flow_data = PRELOADED_FLOWS["whatsapp_send_photo"]
            lang_key = lang if lang in flow_data["flows"] else "en"
            selected_content = flow_data["flows"][lang_key]
            steps = [
                StepItem(
                    step_number=s["step_number"],
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s["target_ui_element"],
                    target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                    audio_text=s["audio_text"],
                    screen_type=s["screen_type"],
                    reassurance=s.get("reassurance")
                )
                for s in selected_content["steps"]
            ]
            return QueryResponse(
                success=True,
                query=query,
                intent_info=IntentResult(
                    app_name="WhatsApp",
                    intent="send_photo",
                    confidence=0.98,
                    platform=platform,
                    detected_language=lang,
                    language_name=self._get_lang_name(lang),
                    target_recipient=recipient
                ),
                title=selected_content["title"],
                summary=selected_content["summary"],
                reassurance_banner=selected_content["reassurance_banner"],
                total_steps=len(steps),
                steps=steps
            )

        # Check WhatsApp Contact Sharing (the user's core incident!)
        is_contact_query = any(k in lower for k in [
            "number", "contact", "phone number", "cellphone number", "mobile number",
            "નંબર", "કોન્ટેક્ટ", "नंबर", "कांटेक्ट"
        ])
        is_whatsapp = any(k in lower for k in ["whatsapp", "વોટ્સએપ", "व्हाट्सएप", "વોટ્સપ"]) or "number" in lower

        if is_contact_query and (is_whatsapp or len(lower.split()) < 10):
            flow_data = PRELOADED_FLOWS["whatsapp_share_contact"]
            lang_key = lang if lang in flow_data["flows"] else "en"
            selected_content = flow_data["flows"][lang_key]

            steps = [
                StepItem(
                    step_number=s["step_number"],
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s["target_ui_element"],
                    target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                    audio_text=s["audio_text"],
                    screen_type=s["screen_type"],
                    reassurance=s.get("reassurance")
                )
                for s in selected_content["steps"]
            ]

            return QueryResponse(
                success=True,
                query=query,
                intent_info=IntentResult(
                    app_name="WhatsApp",
                    intent="share_contact_number",
                    confidence=0.99,
                    platform=platform,
                    detected_language=lang,
                    language_name=self._get_lang_name(lang),
                    target_recipient=recipient
                ),
                title=selected_content["title"],
                summary=selected_content["summary"],
                reassurance_banner=selected_content["reassurance_banner"],
                total_steps=len(steps),
                steps=steps
            )

        # Check Google Pay QR code scan
        if any(k in lower for k in ["qr", "scan", "gpay", "google pay", "સ્કેન", "स्कैन", "पेमेंट"]):
            flow_data = PRELOADED_FLOWS["gpay_scan_qr"]
            lang_key = lang if lang in flow_data["flows"] else "en"
            selected_content = flow_data["flows"][lang_key]
            steps = [
                StepItem(
                    step_number=s["step_number"],
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s["target_ui_element"],
                    target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                    audio_text=s["audio_text"],
                    screen_type=s["screen_type"],
                    reassurance=s.get("reassurance")
                )
                for s in selected_content["steps"]
            ]
            return QueryResponse(
                success=True,
                query=query,
                intent_info=IntentResult(
                    app_name="Google Pay",
                    intent="scan_qr_code",
                    confidence=0.97,
                    platform=platform,
                    detected_language=lang,
                    language_name=self._get_lang_name(lang),
                    target_recipient=None
                ),
                title=selected_content["title"],
                summary=selected_content["summary"],
                reassurance_banner=selected_content["reassurance_banner"],
                total_steps=len(steps),
                steps=steps
            )

        # Check Font Size
        if any(k in lower for k in ["font", "size", "bigger text", "akshar", "mota", "મોટા", "अक्षर बड़े"]):
            flow_data = PRELOADED_FLOWS["settings_font_size"]
            lang_key = lang if lang in flow_data["flows"] else "en"
            selected_content = flow_data["flows"][lang_key]
            steps = [
                StepItem(
                    step_number=s["step_number"],
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s["target_ui_element"],
                    target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                    audio_text=s["audio_text"],
                    screen_type=s["screen_type"],
                    reassurance=s.get("reassurance")
                )
                for s in selected_content["steps"]
            ]
            return QueryResponse(
                success=True,
                query=query,
                intent_info=IntentResult(
                    app_name="Settings",
                    intent="increase_font_size",
                    confidence=0.98,
                    platform=platform,
                    detected_language=lang,
                    language_name=self._get_lang_name(lang),
                    target_recipient=None
                ),
                title=selected_content["title"],
                summary=selected_content["summary"],
                reassurance_banner=selected_content["reassurance_banner"],
                total_steps=len(steps),
                steps=steps
            )

        return None

    def _call_gemini_pipeline(self, query: str, lang: str, platform: str, recipient: Optional[str]) -> Optional[QueryResponse]:
        """Calls Google Gemini model with structured JSON prompting."""
        prompt = build_user_prompt(query, lang, platform)
        try:
            # If using google-genai Client
            if hasattr(self.gemini_client, "models"):
                response = self.gemini_client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[SENIOR_GUIDE_SYSTEM_PROMPT, prompt],
                    config={"response_mime_type": "application/json"}
                )
                raw_json = response.text
            else:
                # If using google.generativeai GenerativeModel
                response = self.gemini_client.generate_content(
                    f"{SENIOR_GUIDE_SYSTEM_PROMPT}\n\n{prompt}",
                    generation_config={"response_mime_type": "application/json"}
                )
                raw_json = response.text

            data = json.loads(raw_json)
            steps = [
                StepItem(
                    step_number=idx + 1,
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s.get("target_ui_element", "Screen Button"),
                    target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                    audio_text=s.get("audio_text", s["instruction"]),
                    screen_type=s.get("screen_type", "app_screen"),
                    reassurance=s.get("reassurance")
                )
                for idx, s in enumerate(data.get("steps", []))
            ]

            return QueryResponse(
                success=True,
                query=query,
                intent_info=IntentResult(
                    app_name=data.get("app_name", "App"),
                    intent=data.get("intent", "task"),
                    confidence=0.92,
                    platform=platform,
                    detected_language=data.get("detected_language", lang),
                    language_name=data.get("language_name", self._get_lang_name(lang)),
                    target_recipient=recipient
                ),
                title=data.get("title", "Help Guide"),
                summary=data.get("summary", "Here are the simple steps to follow."),
                reassurance_banner=data.get("reassurance_banner", "Don't worry, you can follow these steps at your own pace."),
                total_steps=len(steps),
                steps=steps
            )
        except Exception as e:
            logger.error(f"Error calling Gemini API: {e}")
            return None

    def _generate_graceful_fallback(self, query: str, lang: str, lang_name: str, platform: str) -> QueryResponse:
        """Fallback when Gemini is offline - returns the verified full 6-step WhatsApp guide."""
        flow_data = PRELOADED_FLOWS["whatsapp_share_contact"]
        lang_key = lang if lang in flow_data["flows"] else "gu"
        selected_content = flow_data["flows"][lang_key]

        steps = [
            StepItem(
                step_number=s["step_number"],
                title=s["title"],
                instruction=s["instruction"],
                target_ui_element=s["target_ui_element"],
                target_coordinates=TargetCoordinate(**s["target_coordinates"]) if s.get("target_coordinates") else None,
                audio_text=s["audio_text"],
                screen_type=s["screen_type"],
                reassurance=s.get("reassurance")
            )
            for s in selected_content["steps"]
        ]

        return QueryResponse(
            success=True,
            query=query,
            intent_info=IntentResult(
                app_name="WhatsApp",
                intent="share_contact_number",
                confidence=0.95,
                platform=platform,
                detected_language=lang,
                language_name=self._get_lang_name(lang),
                target_recipient=None
            ),
            title=selected_content["title"],
            summary=selected_content["summary"],
            reassurance_banner=selected_content["reassurance_banner"],
            total_steps=len(steps),
            steps=steps
        )

    def _get_lang_name(self, code: str) -> str:
        names = {"gu": "Gujarati", "hi": "Hindi", "mr": "Marathi", "ta": "Tamil", "en": "English"}
        return names.get(code, "English")
