"""
Integration test to test server routes, static files, and intent API.
"""

import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.main import (
    app, health_check, keep_alive_heartbeat, get_supported_languages, list_preloaded_flows,
    process_user_query, check_scam_message, read_elder_document, live_camera_vision_guide,
    get_senior_profile, save_or_update_profile
)
from app.db import SessionLocal
from app.schemas import (
    QueryRequest, ScamCheckRequest, DocumentReadRequest, VisionGuideRequest,
    CaregiverProfileRequest
)

def run_integration_tests():
    print("=" * 60)
    print("RUNNING END-TO-END SERVER & API INTEGRATION TESTS")
    print("=" * 60)

    # 1. Test Health Check & Heartbeat Keep-Alive endpoints
    health = health_check()
    assert health["app"] == "Sahayak AI"
    assert health["status"] == "online"
    assert "rate_limiter" in health
    print(f"  ✅ [GET /api/health] Health check verified. Mode: {health.get('mode')} (DB: {health.get('database')}, Limiter: {health.get('rate_limiter')})")

    ping = keep_alive_heartbeat()
    assert ping["status"] == "healthy_alive"
    assert ping["database_connected"] is True
    print(f"  ✅ [GET /api/ping] 24/7 Heartbeat keep-alive verified: {ping['status']}")

    # 2. Test Caregiver & Senior Profile Persistent Storage (PostgreSQL/SQLite)
    db = SessionLocal()
    try:
        save_req = CaregiverProfileRequest(
            user_uid="test_user_senior_1",
            senior_name="રમણિકભાઈ (Ramnikbhai)",
            preferred_language="gu",
            caregiver_name="અમિત (દીકરો)",
            caregiver_phone="9876543210",
            caregiver_relation="દીકરો (Son)"
        )
        saved_prof = save_or_update_profile(save_req, db=db)
        assert saved_prof.success is True
        assert saved_prof.caregiver_phone == "9876543210"

        fetched_prof = get_senior_profile("test_user_senior_1", db=db)
        assert fetched_prof.senior_name == "રમણિકભાઈ (Ramnikbhai)"
        assert fetched_prof.caregiver_name == "અમિત (દીકરો)"
        print(f"  ✅ [DB Persistent Storage] Senior & Caregiver profile verified: {fetched_prof.senior_name} -> {fetched_prof.caregiver_name} ({fetched_prof.caregiver_phone})")
    finally:
        db.close()

    # 3. Test Languages endpoint
    langs = get_supported_languages()
    assert "gu" in langs["languages"] and "hi" in langs["languages"] and "en" in langs["languages"]
    print(f"  ✅ [GET /api/languages] Supported languages endpoint verified ({len(langs['languages'])} languages).")

    # 3. Test Preloaded Flows endpoint
    flows = list_preloaded_flows()
    assert len(flows["flows"]) >= 15
    print(f"  ✅ [GET /api/flows] Preloaded flows catalog verified ({len(flows['flows'])} core senior flows).")

    # 4. Test Core Query API with Rate-Limited Endpoint & Mock Request
    from starlette.requests import Request
    scope = {"type": "http", "path": "/api/query", "client": ("127.0.0.1", 50000), "headers": []}
    mock_req = Request(scope)

    post_payload = QueryRequest(
        query="mane mara bhai no phone number whatsapp par bija ne moklavo che",
        language="gu",
        platform="android"
    )
    guide = process_user_query(mock_req, post_payload)
    assert guide.success is True
    assert guide.intent_info.app_name == "WhatsApp"
    assert guide.intent_info.intent == "share_contact_number"
    assert guide.total_steps == 6
    assert len(guide.steps) == 6

    step2 = guide.steps[1]
    assert step2.target_coordinates.x_percent > 0
    assert step2.target_coordinates.y_percent > 0
    print(f"  ✅ [POST /api/query] Returned 6-step verified guide: '{guide.title}'")
    print(f"     Step 2 target: {step2.target_ui_element} at ({step2.target_coordinates.x_percent}%, {step2.target_coordinates.y_percent}%)")

    # 5. Test Elder Super-Tools: Anti-Scam Radar
    scam_req = ScamCheckRequest(text="Electricity bill overdue tonight power cut call 9876543210", language="gu")
    scam_resp = check_scam_message(mock_req, scam_req)
    assert scam_resp.is_scam is True
    assert scam_resp.risk_score >= 90
    print(f"  ✅ [POST /api/check-scam] Scam radar verified: '{scam_resp.verdict_title}' (Risk: {scam_resp.risk_score}%)")

    # 6. Test Elder Super-Tools: Document Reader
    doc_req = DocumentReadRequest(doc_type="medicine", language="gu")
    doc_resp = read_elder_document(mock_req, doc_req)
    assert "ટેલમિસાર્ટન" in str(doc_resp.key_details) or "દવા" in doc_resp.title
    print(f"  ✅ [POST /api/read-document] Document OCR reader verified: '{doc_resp.title}'")

    # 7. Test Elder Super-Tools: Live Vision Guide
    vision_req = VisionGuideRequest(frame_base64="", language="gu")
    vision_resp = live_camera_vision_guide(mock_req, vision_req)
    assert vision_resp.highlight_x_percent > 0
    print(f"  ✅ [POST /api/vision-guide] Camera vision guide verified: target '{vision_resp.target_element_name}'")

    # 8. Test Static Files Integrity
    frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
    assert (frontend_dir / "index.html").is_file()
    assert (frontend_dir / "css" / "styles.css").is_file()
    assert (frontend_dir / "js" / "app.js").is_file()
    assert (frontend_dir / "manifest.json").is_file()
    assert (frontend_dir / "favicon.svg").is_file()
    print("  ✅ [Static Files] Verified index.html, styles.css, app.js, manifest.json, favicon.svg exist.")

    print("\n" + "=" * 60)
    print("ALL INTEGRATION TESTS PASSED! FULL SYSTEM IS WORKING.")
    print("=" * 60)

if __name__ == "__main__":
    run_integration_tests()


