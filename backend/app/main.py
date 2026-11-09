import os
import sys

# Ensure backend directory is in sys.path so 'app' can be found regardless of launch folder
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.config import HOST, PORT, SUPPORTED_LANGUAGES
from app.schemas import QueryRequest, QueryResponse
from app.services.intent_parser import IntentParserService
from app.data.preloaded_flows import PRELOADED_FLOWS

app = FastAPI(
    title="Sahayak AI - Senior Digital Companion API",
    description="Backend API for elderly smartphone navigation guidance in native languages",
    version="1.0.0"
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
    return {
        "app": "Sahayak AI",
        "status": "online",
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

@app.post("/api/query", response_model=QueryResponse)
def process_user_query(request: QueryRequest):
    """
    Core Intelligence Endpoint:
    Accepts user voice transcript or text query in any language.
    Detects app, intent, recipient, platform, and returns structured step-by-step guide.
    """
    try:
        response = intent_service.parse_query(
            query=request.query,
            preferred_lang=request.language,
            platform=request.platform or "android"
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

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

    @app.get("/sw.js")
    def serve_sw():
        return FileResponse(os.path.join(frontend_dir, "sw.js"), media_type="application/javascript")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("👵👴 Starting Sahayak AI Server...")
    print(f"👉 Open your browser at: http://{HOST}:{PORT}")
    print("=" * 60 + "\n")
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True, app_dir=backend_dir)
