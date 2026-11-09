"""
Test script for Phase 1: Core Intelligence & Intent Parser
Verifies multilingual query processing, intent detection, and step generation.
"""

import sys
import os

# Add backend directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.intent_parser import IntentParserService

def run_tests():
    service = IntentParserService()
    test_cases = [
        {
            "name": "Father's Incident - Gujarati WhatsApp Contact Share",
            "query": "mane mara bhai no phone number whatsapp par bija ne moklavo che",
            "expected_app": "WhatsApp",
            "expected_intent": "share_contact_number",
            "expected_lang": "gu",
            "expected_recipient": "Brother"
        },
        {
            "name": "Father's Incident - Hindi WhatsApp Contact Share",
            "query": "mujhe whatsapp par kisi ko contact number bhejna hai",
            "expected_app": "WhatsApp",
            "expected_intent": "share_contact_number",
            "expected_lang": "hi",
            "expected_recipient": None
        },
        {
            "name": "Father's Incident - English WhatsApp Contact Share",
            "query": "How do I send my friend's phone number on WhatsApp?",
            "expected_app": "WhatsApp",
            "expected_intent": "share_contact_number",
            "expected_lang": "en",
            "expected_recipient": "Friend"
        },
        {
            "name": "GPay Scan QR Payment - Hindi",
            "query": "dukaan par QR code scan karke payment kaise karein?",
            "expected_app": "Google Pay",
            "expected_intent": "scan_qr_code",
            "expected_lang": "hi",
            "expected_recipient": None
        },
        {
            "name": "Phone Settings Font Size - Gujarati",
            "query": "phone ma akshar mota karva che",
            "expected_app": "Settings",
            "expected_intent": "increase_font_size",
            "expected_lang": "gu",
            "expected_recipient": None
        }
    ]

    print("=" * 70)
    print("RUNNING PHASE 1 CORE INTELLIGENCE & INTENT PARSER TESTS")
    print("=" * 70)

    all_passed = True

    for idx, tc in enumerate(test_cases, 1):
        print(f"\n[Test {idx}] {tc['name']}")
        print(f"  Input Query: \"{tc['query']}\"")
        
        response = service.parse_query(tc["query"])
        
        app_match = response.intent_info.app_name == tc["expected_app"]
        intent_match = response.intent_info.intent == tc["expected_intent"]
        lang_match = response.intent_info.detected_language == tc["expected_lang"]
        
        print(f"  - Detected App: {response.intent_info.app_name} (Expected: {tc['expected_app']}) -> {'PASS' if app_match else 'FAIL'}")
        print(f"  - Detected Intent: {response.intent_info.intent} (Expected: {tc['expected_intent']}) -> {'PASS' if intent_match else 'FAIL'}")
        print(f"  - Detected Language: {response.intent_info.detected_language} ({response.intent_info.language_name}) -> {'PASS' if lang_match else 'FAIL'}")
        print(f"  - Target Recipient: {response.intent_info.target_recipient}")
        print(f"  - Title: {response.title}")
        print(f"  - Reassurance Banner: {response.reassurance_banner}")
        print(f"  - Total Steps Generated: {response.total_steps}")
        
        # Verify first step structure
        first_step = response.steps[0]
        print(f"    * Step 1: '{first_step.title}'")
        print(f"    * Instruction: {first_step.instruction}")
        print(f"    * Target UI Element: {first_step.target_ui_element}")
        if first_step.target_coordinates:
            print(f"    * Coordinates: (x={first_step.target_coordinates.x_percent}%, y={first_step.target_coordinates.y_percent}%)")

        test_passed = app_match and intent_match and lang_match and response.total_steps > 0
        if not test_passed:
            all_passed = False
            print("  ❌ TEST FAILED")
        else:
            print("  ✅ TEST PASSED")

    print("\n" + "=" * 70)
    if all_passed:
        print("ALL TESTS PASSED! Phase 1 Core Intelligence & Intent Parser is 100% verified.")
    else:
        print("SOME TESTS FAILED! Please check logs above.")
    print("=" * 70)
    return all_passed

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)

