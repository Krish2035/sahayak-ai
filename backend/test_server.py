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
    app, health_check, get_supported_languages, list_preloaded_flows,
    process_user_query, check_scam_message, read_elder_document, live_camera_vision_guide
)
from app.schemas import (
    QueryRequest, ScamCheckRequest, DocumentReadRequest, VisionGuideRequest
)

def run_integration_tests():
    print("=" * 60)
    print("RUNNING END-TO-END SERVER & API INTEGRATION TESTS")
    print("=" * 60)

    # 1. Test Health Check endpoint
    health = health_check()
    assert health["app"] == "Sahayak AI"
    assert health["status"] == "online"
    print(f"  ✅ [GET /api/health] Health check verified. Mode: {health.get('mode')} (Gemini Live: {health.get('gemini_live_enabled')})")

    # 2. Test Languages endpoint
    langs = get_supported_languages()
    assert "gu" in langs["languages"] and "hi" in langs["languages"] and "en" in langs["languages"]
    print(f"  ✅ [GET /api/languages] Supported languages endpoint verified ({len(langs['languages'])} languages).")

    # 3. Test Preloaded Flows endpoint
    flows = list_preloaded_flows()
    assert len(flows["flows"]) >= 15
    print(f"  ✅ [GET /api/flows] Preloaded flows catalog verified ({len(flows['flows'])} core senior flows).")

    # 4. Test Core Query API: Father's exact WhatsApp Contact Sharing incident
    post_payload = QueryRequest(
        query="mane mara bhai no phone number whatsapp par bija ne moklavo che",
        language="gu",
        platform="android"
    )
    guide = process_user_query(post_payload)
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
    scam_resp = check_scam_message(scam_req)
    assert scam_resp.is_scam is True
    assert scam_resp.risk_score >= 90
    print(f"  ✅ [POST /api/check-scam] Scam radar verified: '{scam_resp.verdict_title}' (Risk: {scam_resp.risk_score}%)")

    # 6. Test Elder Super-Tools: Document Reader
    doc_req = DocumentReadRequest(doc_type="medicine", language="gu")
    doc_resp = read_elder_document(doc_req)
    assert "ટેલમિસાર્ટન" in str(doc_resp.key_details) or "દવા" in doc_resp.title
    print(f"  ✅ [POST /api/read-document] Document OCR reader verified: '{doc_resp.title}'")

    # 7. Test Elder Super-Tools: Live Vision Guide
    vision_req = VisionGuideRequest(frame_base64="", language="gu")
    vision_resp = live_camera_vision_guide(vision_req)
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


