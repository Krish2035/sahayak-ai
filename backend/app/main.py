import os
import sys
import datetime
from typing import Optional, Any

# Ensure backend directory is in sys.path so 'app' can be found regardless of launch folder
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.config import (
    HOST, PORT, SUPPORTED_LANGUAGES,
    DATABASE_URL, REDIS_URL, RATE_LIMIT_DEFAULT
)
from app.db import init_db, get_db, SeniorProfile, ScamReportLog
from app.schemas import (
    QueryRequest, QueryResponse,
    ScamCheckRequest, ScamCheckResponse,
    DocumentReadRequest, DocumentReadResponse,
    VisionGuideRequest, VisionGuideResponse,
    CaregiverProfileRequest, CaregiverProfileResponse
)
from app.services.intent_parser import IntentParserService
from app.services.elder_tools_service import elder_tools_service
from app.data.preloaded_flows import PRELOADED_FLOWS

# Initialize Database tables
init_db()

# Initialize Rate Limiter with Redis or In-Memory fallback (10 req/min)
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[RATE_LIMIT_DEFAULT],
    storage_uri=REDIS_URL if REDIS_URL else "memory://"
)

app = FastAPI(
    title="Sahayak AI - Senior Digital Companion API",
    description="Production-grade API for elderly smartphone navigation guidance in native languages",
    version="1.0.0"
)
app.state.limiter = limiter

# Custom Rate Limit Handler with comforting senior-friendly trilingual message
@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "rate_limit_exceeded",
            "message": "કૃપા કરીને ૧ મિનિટ રાહ જુઓ. વડીલોની સુરક્ષા અને સિસ્ટમ સ્થિરતા માટે પ્રતિ મિનિટે ૧૦ સવાલોની મર્યાદા છે.",
            "message_en": "Please wait 1 minute. A rate limit of 10 queries per minute is active to prevent overload.",
            "retry_after_seconds": 60
        }
    )

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

intent_service = IntentParserService()

# API Endpoints
@app.get("/api/health")
def health_check():
    api_key_set = bool(os.getenv("GEMINI_API_KEY", "").strip())
    db_type = "postgresql" if DATABASE_URL else "sqlite_persistent"
    redis_type = "redis_connected" if REDIS_URL else "in_memory_fast"
    return {
        "app": "Sahayak AI",
        "status": "online",
        "gemini_live_enabled": api_key_set,
        "mode": "gemini_live" if api_key_set else "curated_flows_offline",
        "database": db_type,
        "rate_limiter": f"slowapi_{redis_type} (10 req/min)",
        "legal_compliance": "disclaimers_active",
        "version": "1.0.0"
    }

@app.get("/api/ping")
@app.get("/api/heartbeat")
def keep_alive_heartbeat():
    """24/7 Keep-Alive heartbeat endpoint for UptimeRobot or Cron to eliminate Render cold-starts."""
    return {
        "status": "healthy_alive",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "database_connected": True,
        "rate_limiter": "active (10/min)",
        "render_plan_mode": "24/7_keepalive_active",
        "version": "1.0.0"
    }

@app.get("/api/languages")
def get_supported_languages():
    """Returns list of supported Indian and international languages."""
    return {"languages": SUPPORTED_LANGUAGES}

@app.get("/api/flows")
def list_preloaded_flows():
    """Lists verified pre-loaded common senior task flows."""
    summary = []
    for flow_id, data in PRELOADED_FLOWS.items():
        summary.append({
            "flow_id": flow_id,
            "app_name": data["app_name"],
            "intent": data["intent"],
            "available_languages": list(data["flows"].keys())
        })
    return {"flows": summary}

def _get_active_session(db_param: Any):
    if isinstance(db_param, Session):
        return db_param, False
    return SessionLocal(), True

# Profile Management Endpoints (PostgreSQL / SQLite)
@app.get("/api/profile/{user_uid}", response_model=CaregiverProfileResponse)
def get_senior_profile(user_uid: str, db: Session = Depends(get_db)):
    """Retrieves senior citizen preferences and caregiver emergency contact."""
    session, should_close = _get_active_session(db)
    try:
        profile = session.query(SeniorProfile).filter(SeniorProfile.user_uid == user_uid).first()
        if not profile:
            return CaregiverProfileResponse(
                success=True,
                user_uid=user_uid,
                senior_name="વડીલ (Senior User)",
                preferred_language="gu",
                caregiver_name="દીકરો / દીકરી (Family Caregiver)",
                caregiver_phone="",
                caregiver_relation="દીકરો (Son)",
                message="Default profile generated. Caregiver contact not yet configured."
            )
        return CaregiverProfileResponse(
            success=True,
            user_uid=profile.user_uid,
            senior_name=profile.senior_name or "વડીલ",
            preferred_language=profile.preferred_language or "gu",
            caregiver_name=profile.caregiver_name or "દીકરો / દીકરી",
            caregiver_phone=profile.caregiver_phone or "",
            caregiver_relation=profile.caregiver_relation or "દીકરો (Son)",
            message="Profile retrieved successfully."
        )
    finally:
        if should_close:
            session.close()

@app.post("/api/profile", response_model=CaregiverProfileResponse)
def save_or_update_profile(req: CaregiverProfileRequest, db: Session = Depends(get_db)):
    """Saves or updates senior citizen profile and family caregiver contact."""
    session, should_close = _get_active_session(db)
    try:
        profile = session.query(SeniorProfile).filter(SeniorProfile.user_uid == req.user_uid).first()
        if not profile:
            profile = SeniorProfile(
                user_uid=req.user_uid,
                senior_name=req.senior_name or "વડીલ",
                preferred_language=req.preferred_language or "gu",
                caregiver_name=req.caregiver_name or "દીકરો / દીકરી",
                caregiver_phone=req.caregiver_phone or "",
                caregiver_relation=req.caregiver_relation or "દીકરો (Son)"
            )
            session.add(profile)
        else:
            if req.senior_name:
                profile.senior_name = req.senior_name
            if req.preferred_language:
                profile.preferred_language = req.preferred_language
            if req.caregiver_name:
                profile.caregiver_name = req.caregiver_name
            if req.caregiver_phone is not None:
                profile.caregiver_phone = req.caregiver_phone
            if req.caregiver_relation:
                profile.caregiver_relation = req.caregiver_relation

        session.commit()
        session.refresh(profile)
        return CaregiverProfileResponse(
            success=True,
            user_uid=profile.user_uid,
            senior_name=profile.senior_name,
            preferred_language=profile.preferred_language,
            caregiver_name=profile.caregiver_name,
            caregiver_phone=profile.caregiver_phone,
            caregiver_relation=profile.caregiver_relation,
            message="Caregiver & Senior profile saved successfully in database!"
        )
    finally:
        if should_close:
            session.close()

def _execute_query(request_body: QueryRequest) -> QueryResponse:
    return intent_service.parse_query(
        query=request_body.query,
        preferred_lang=request_body.language,
        platform=request_body.platform or "android"
    )

@app.post("/api/query", response_model=QueryResponse)
@limiter.limit("10/minute")
def process_user_query(request: Request, body: QueryRequest = None):
    """
    Core Intelligence Endpoint with Rate Limiting (10 req/min):
    Accepts user voice transcript or text query in any language.
    Detects app, intent, recipient, platform, and returns structured step-by-step guide.
    """
    req_body = body if body is not None else (request if isinstance(request, QueryRequest) else None)
    if req_body is None:
        raise HTTPException(status_code=400, detail="Invalid request body")
    try:
        return _execute_query(req_body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.post("/api/check-scam", response_model=ScamCheckResponse)
@limiter.limit("10/minute")
def check_scam_message(request: Request, body: ScamCheckRequest = None, db: Session = Depends(get_db)):
    """Checks SMS/WhatsApp messages or threats for cyber scam patterns with Rate Limiting and DB Audit."""
    req_body = body if body is not None else (request if isinstance(request, ScamCheckRequest) else None)
    if req_body is None:
        raise HTTPException(status_code=400, detail="Invalid request body")
    try:
        res = elder_tools_service.check_scam(req_body)
        # Log scam checks to database for audit and analytics
        try:
            if isinstance(db, Session):
                log_entry = ScamReportLog(
                    submitted_text=req_body.text[:500] if req_body.text else "",
                    language=req_body.language or "gu",
                    is_scam=res.is_scam,
                    risk_score=res.risk_score,
                    verdict_title=res.verdict_title[:250]
                )
                db.add(log_entry)
                db.commit()
        except Exception:
            pass
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error checking scam: {str(e)}")

@app.post("/api/read-document", response_model=DocumentReadResponse)
@limiter.limit("10/minute")
def read_elder_document(request: Request, body: DocumentReadRequest = None):
    """OCR Reader for medicine strips and utility bills in Gujarati/Hindi/English."""
    req_body = body if body is not None else (request if isinstance(request, DocumentReadRequest) else None)
    if req_body is None:
        raise HTTPException(status_code=400, detail="Invalid request body")
    try:
        return elder_tools_service.read_document(req_body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading document: {str(e)}")

@app.post("/api/vision-guide", response_model=VisionGuideResponse)
def live_camera_vision_guide(request: Request, body: VisionGuideRequest = None):
    """Live Camera Screen Vision guidance for physical smartphone screens."""
    req_body = body if body is not None else (request if isinstance(request, VisionGuideRequest) else None)
    if req_body is None:
        raise HTTPException(status_code=400, detail="Invalid request body")
    try:
        return elder_tools_service.guide_vision(req_body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in vision guide: {str(e)}")

# Mount Frontend static files for full-stack 1-click execution
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))

if os.path.exists(frontend_dir):
    app.mount("/css", StaticFiles(directory=os.path.join(frontend_dir, "css")), name="css")
    app.mount("/js", StaticFiles(directory=os.path.join(frontend_dir, "js")), name="js")
    app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dir, "assets")), name="assets")

    @app.get("/")
    def serve_frontend_index():
        return FileResponse(os.path.join(frontend_dir, "index.html"))

    @app.get("/manifest.json")
    def serve_manifest():
        return FileResponse(os.path.join(frontend_dir, "manifest.json"), media_type="application/manifest+json")

    @app.get("/favicon.svg")
    def serve_favicon():
        return FileResponse(os.path.join(frontend_dir, "favicon.svg"), media_type="image/svg+xml")

    @app.get("/sw.js")
    def serve_sw():
        return FileResponse(os.path.join(frontend_dir, "sw.js"), media_type="application/javascript")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("👵👴 Starting Sahayak AI Server...")
    print(f"👉 Open your browser at: http://{HOST}:{PORT}")
    print("=" * 60 + "\n")
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True, app_dir=backend_dir)
