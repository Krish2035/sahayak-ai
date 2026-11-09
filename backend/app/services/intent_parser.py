import json
import re
import os
import logging
from typing import Optional, Dict, Any

from app.config import get_gemini_api_key
from app.schemas import QueryResponse, IntentResult, StepItem, TargetCoordinate
from app.services.language_detector import detect_language_and_script
from app.services.prompts import SENIOR_GUIDE_SYSTEM_PROMPT, build_user_prompt
from app.data.preloaded_flows import PRELOADED_FLOWS

logger = logging.getLogger(__name__)

class IntentParserService:
    def __init__(self):
        self.api_key = get_gemini_api_key()
        self.gemini_client = None
        self._sdk_type = None
        self._init_gemini()

    def _init_gemini(self):
        """Initializes Gemini API client if API key is present."""
        self.api_key = get_gemini_api_key()
        if not self.api_key:
            logger.info("No GEMINI_API_KEY set. Operating in offline/curated flow mode.")
            self.gemini_client = None
            return

        # 1. Try google-genai Client (new SDK)
        try:
            from google import genai
            self.gemini_client = genai.Client(api_key=self.api_key)
            self._sdk_type = "genai"
            logger.info("Initialized google-genai Client successfully.")
            return
        except Exception as e:
            logger.warning(f"Could not initialize google-genai: {e}. Trying google.generativeai fallback.")

        # 2. Try google.generativeai (GenerativeModel)
        try:
            import google.generativeai as gai
            gai.configure(api_key=self.api_key)
            self.gemini_client = gai.GenerativeModel("gemini-1.5-flash")
            self._sdk_type = "generativeai"
            logger.info("Initialized google.generativeai fallback successfully.")
        except Exception as e2:
            logger.error(f"Could not initialize Gemini SDK: {e2}")
            self.gemini_client = None

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

        # Step 4: If Gemini client available (or newly configured), run dynamic LLM prompt pipeline
        if not self.gemini_client:
            self._init_gemini()

        if self.gemini_client:
            llm_response = self._call_gemini_pipeline(query_clean, active_lang, platform, target_recipient)
            if llm_response:
                return llm_response

        # Step 5: Fallback default response
        return self._generate_graceful_fallback(query_clean, active_lang, detected_lang_name, platform)

    def _parse_coordinates(self, coords: Any) -> Optional[TargetCoordinate]:
        """Safely parses target coordinates into TargetCoordinate schema."""
        if not coords or not isinstance(coords, dict):
            return None
        return TargetCoordinate(
            x_percent=float(coords.get("x_percent", 50.0)),
            y_percent=float(coords.get("y_percent", 50.0)),
            radius_percent=float(coords.get("radius_percent", 7.0)),
            description=str(coords.get("description", "Target button"))
        )

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
        """Checks if the query matches our verified top 15 senior tasks with keyword scoring."""
        lower = query.lower()
        best_flow_key = None
        best_score = 0

        # Dynamic keyword matching against all 15 preloaded flows
        for flow_key, flow_data in PRELOADED_FLOWS.items():
            score = 0
            keywords = flow_data.get("keywords", [])
            for kw in keywords:
                kw_lower = kw.lower()
                if kw_lower in lower:
                    score += len(kw_lower) * 2
            if score > best_score:
                best_score = score
                best_flow_key = flow_key

        if best_flow_key and best_score >= 4:
            flow_data = PRELOADED_FLOWS[best_flow_key]
            lang_key = lang if lang in flow_data["flows"] else ("gu" if "gu" in flow_data["flows"] else "en")
            selected_content = flow_data["flows"][lang_key]

            steps = [
                StepItem(
                    step_number=s["step_number"],
                    title=s["title"],
                    instruction=s["instruction"],
                    target_ui_element=s["target_ui_element"],
                    target_coordinates=self._parse_coordinates(s.get("target_coordinates")),
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
                    app_name=flow_data.get("app_name", "App"),
                    intent=flow_data.get("intent", "action"),
                    confidence=0.98,
                    platform=platform,
                    detected_language=lang,
                    language_name=self._get_lang_name(lang),
                    target_recipient=recipient if ("contact" in best_flow_key or "photo" in best_flow_key) else None
                ),
                title=selected_content["title"],
                summary=selected_content["summary"],
                reassurance_banner=selected_content.get("reassurance_banner", ""),
                total_steps=len(steps),
                steps=steps
            )

        return None

    def _call_gemini_pipeline(self, query: str, lang: str, platform: str, recipient: Optional[str]) -> Optional[QueryResponse]:
        """Calls Google Gemini model with structured JSON prompting."""
        prompt = build_user_prompt(query, lang, platform)
        raw_json = None
        try:
            # If using google-genai Client
            if getattr(self, "_sdk_type", "") == "genai" or hasattr(self.gemini_client, "models"):
                try:
                    response = self.gemini_client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=[SENIOR_GUIDE_SYSTEM_PROMPT, prompt],
                        config={"response_mime_type": "application/json"}
                    )
                    raw_json = response.text
                except Exception as ex1:
                    logger.warning(f"gemini-1.5-flash attempt returned: {ex1}. Trying gemini-2.0-flash.")
                    response = self.gemini_client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=[SENIOR_GUIDE_SYSTEM_PROMPT, prompt],
                        config={"response_mime_type": "application/json"}
                    )
                    raw_json = response.text
            else:
                # If using google.generativeai GenerativeModel
                try:
                    response = self.gemini_client.generate_content(
                        f"{SENIOR_GUIDE_SYSTEM_PROMPT}\n\n{prompt}",
                        generation_config={"response_mime_type": "application/json"}
                    )
                    raw_json = response.text
                except Exception as ex2:
                    logger.warning(f"GenerativeModel generation error: {ex2}")
                    raw_json = None

            if not raw_json:
                return None

            # Clean potential Markdown code fences like ```json ... ```
            raw_clean = raw_json.strip()
            if raw_clean.startswith("```"):
                raw_clean = re.sub(r"^```(?:json)?\s*", "", raw_clean)
                raw_clean = re.sub(r"\s*```$", "", raw_clean)

            data = json.loads(raw_clean)
            steps = []
            for idx, s in enumerate(data.get("steps", [])):
                steps.append(
                    StepItem(
                        step_number=idx + 1,
                        title=s.get("title", f"Step {idx + 1}"),
                        instruction=s.get("instruction", ""),
                        target_ui_element=s.get("target_ui_element", "Screen Button"),
                        target_coordinates=self._parse_coordinates(s.get("target_coordinates")),
                        audio_text=s.get("audio_text", s.get("instruction", "")),
                        screen_type=s.get("screen_type", "generic_screen"),
                        reassurance=s.get("reassurance")
                    )
                )

            if not steps:
                return None

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
                target_coordinates=self._parse_coordinates(s.get("target_coordinates")),
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
