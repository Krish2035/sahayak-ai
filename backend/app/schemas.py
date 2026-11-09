from typing import Optional, List
from pydantic import BaseModel, Field

class TargetCoordinate(BaseModel):
    x_percent: float = Field(..., description="Horizontal position (0-100% from left of screen)")
    y_percent: float = Field(..., description="Vertical position (0-100% from top of screen)")
    radius_percent: float = Field(7.0, description="Radius size for the pulsing spotlight circle")
    description: str = Field("Target button", description="Visual description of the target button/area")

class StepItem(BaseModel):
    step_number: int = Field(..., description="Step index starting from 1")
    title: str = Field(..., description="Short senior-friendly title in the user's language")
    instruction: str = Field(..., description="Clear step-by-step description without technical jargon")
    target_ui_element: str = Field(..., description="Name and visual icon of button to touch (e.g. 📎 Paperclip icon)")
    target_coordinates: Optional[TargetCoordinate] = Field(None, description="Coordinates for the glowing highlight ring")
    audio_text: str = Field(..., description="Natural phonetic narration script for Text-To-Speech")
    screen_type: str = Field("generic_screen", description="Identifier for mockup UI (e.g. chat_screen, attachment_popup)")
    reassurance: Optional[str] = Field(None, description="Comforting note (e.g. 'Nothing will get deleted')")

class IntentResult(BaseModel):
    app_name: str = Field(..., description="Target application (e.g., WhatsApp, Google Pay, Phone Settings)")
    intent: str = Field(..., description="Standardized intent ID (e.g., share_contact_number)")
    confidence: float = Field(1.0, description="Confidence score between 0.0 and 1.0")
    platform: str = Field("android", description="Operating system: android or ios")
    detected_language: str = Field("en", description="ISO 639-1 language code (e.g. gu, hi, mr, ta, en)")
    language_name: str = Field("English", description="Human-readable language name (e.g. Gujarati, Hindi)")
    target_recipient: Optional[str] = Field(None, description="Identified recipient (e.g. friend, brother, person)")

class QueryRequest(BaseModel):
    query: str = Field(..., min_length=2, description="User voice transcript or typed text in any language")
    language: Optional[str] = Field("auto", description="Preferred language code or 'auto'")
    platform: Optional[str] = Field("android", description="Platform target: android or ios")
    user_age_group: Optional[str] = Field("senior", description="Target persona: senior, adult, child")

class QueryResponse(BaseModel):
    success: bool = True
    query: str
    intent_info: IntentResult
    title: str = Field(..., description="Clear task title in user's native language")
    summary: str = Field(..., description="1-sentence explanation of what will be done")
    reassurance_banner: str = Field(..., description="Calming message: e.g. 'Don't worry, you won't lose money or delete anything'")
    total_steps: int
    steps: List[StepItem]

# --- Elder Super-Tools Schemas ---

class ScamCheckRequest(BaseModel):
    text: Optional[str] = Field(None, description="SMS or WhatsApp text to analyze")
    image_base64: Optional[str] = Field(None, description="Optional screenshot of message")
    language: Optional[str] = Field("gu", description="Language code: gu, hi, en")

class ScamCheckResponse(BaseModel):
    is_scam: bool
    risk_score: int
    verdict_title: str
    verdict_audio: str
    explanation: str
    action_steps: List[str]

class DocumentReadRequest(BaseModel):
    doc_type: str = Field("medicine", description="medicine or utility_bill")
    sample_id: Optional[str] = Field(None, description="Preset sample ID")
    image_base64: Optional[str] = Field(None, description="Optional uploaded image")
    language: Optional[str] = Field("gu", description="gu, hi, en")

class DocumentReadResponse(BaseModel):
    success: bool = True
    doc_type: str
    title: str
    audio_narration: str
    key_details: List[dict]
    comfort_note: str

class VisionGuideRequest(BaseModel):
    image_base64: Optional[str] = Field(None, description="Live camera frame")
    current_task: Optional[str] = Field("whatsapp_contact", description="Task identifier")
    language: Optional[str] = Field("gu", description="gu, hi, en")

class VisionGuideResponse(BaseModel):
    detected_screen: str
    voice_instruction: str
    highlight_x_percent: float
    highlight_y_percent: float
    target_element_name: str


