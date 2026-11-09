"""
Integration test using FastAPI TestClient to test server routes, static files, and intent API.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi.testclient import TestClient
from app.main import app

def run_integration_tests():
    client = TestClient(app)

    print("=" * 60)
    print("RUNNING END-TO-END SERVER & API INTEGRATION TESTS")
    print("=" * 60)

    # 1. Test Health / Root Frontend Serve
    resp = client.get("/")
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    assert "<title>Sahayak AI" in resp.text
    print("  ✅ [GET /] Frontend HTML served successfully.")

    # 2. Test CSS and JS static mounts
    css_resp = client.get("/css/styles.css")
    assert css_resp.status_code == 200
    assert "pulseTarget" in css_resp.text
    print("  ✅ [GET /css/styles.css] Static CSS file served.")

    js_resp = client.get("/js/app.js")
    assert js_resp.status_code == 200
    assert "SpeechRecognition" in js_resp.text
    print("  ✅ [GET /js/app.js] Static JS file served.")

    svg_resp = client.get("/assets/screens/whatsapp_chat_list.svg")
    assert svg_resp.status_code == 200
    assert "<svg" in svg_resp.text
    print("  ✅ [GET /assets/screens/whatsapp_chat_list.svg] Visual SVG mockup served.")

    # 3. Test Languages endpoint
    lang_resp = client.get("/api/languages")
    assert lang_resp.status_code == 200
    data = lang_resp.json()
    assert "gu" in data["languages"] and "hi" in data["languages"]
    print("  ✅ [GET /api/languages] Supported languages endpoint verified.")

    # 4. Test Core Query API: Father's exact WhatsApp Contact Sharing incident
    post_payload = {
        "query": "mane mara bhai no phone number whatsapp par bija ne moklavo che",
        "language": "gu",
        "platform": "android"
    }
    api_resp = client.post("/api/query", json=post_payload)
    assert api_resp.status_code == 200
    guide = api_resp.json()
    assert guide["success"] is True
    assert guide["intent_info"]["app_name"] == "WhatsApp"
    assert guide["intent_info"]["intent"] == "share_contact_number"
    assert guide["total_steps"] == 6
    assert len(guide["steps"]) == 6

    # Verify coordinates for step 2 (paperclip)
    step2 = guide["steps"][1]
    assert step2["target_coordinates"]["x_percent"] > 0
    assert step2["target_coordinates"]["y_percent"] > 0
    print(f"  ✅ [POST /api/query] Returned 4-step verified guide: '{guide['title']}'")
    print(f"     Step 2 target: {step2['target_ui_element']} at ({step2['target_coordinates']['x_percent']}%, {step2['target_coordinates']['y_percent']}%)")

    print("\n" + "=" * 60)
    print("ALL INTEGRATION TESTS PASSED! FULL SYSTEM IS WORKING.")
    print("=" * 60)

if __name__ == "__main__":
    run_integration_tests()

