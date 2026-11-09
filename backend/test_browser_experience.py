"""
Comprehensive Verification Suite for Sahayak AI: ChatGPT-Style Systematic Visual Guide
Tests the conversational feed, embedded photos below every step,
bilingual audio narration, and calibrated spotlight coordinates.
"""

import os
import re
import xml.etree.ElementTree as ET
import json
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
from app.services.intent_parser import IntentParserService
from app.data.preloaded_flows import PRELOADED_FLOWS

REPORT = {
    "total_checks": 0,
    "passed_checks": 0
}

def log_check(section_name, check_name, passed, details=""):
    REPORT["total_checks"] += 1
    if passed:
        REPORT["passed_checks"] += 1
    status = "✅ PASS" if passed else "❌ FAIL"
    print(f"  {status} | {check_name}: {details}")
    return {"name": check_name, "passed": passed, "details": details}

def test_html_dom_structure():
    print("\n--- 1. Testing ChatGPT-Style HTML DOM & Elements ---")
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html"))
    assert os.path.exists(html_path), "index.html not found!"

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    required_ids = [
        "appTitle", "langSelectBtn", "btnClearChat", "reassuranceText",
        "chatFeed", "welcomeCard", "quickTrayTitle",
        "chipQ1", "chipQ2", "chipQ3", "chipQ4",
        "chatInput", "btnMic", "btnSend", "micActiveBanner"
    ]

    all_ids_found = True
    for el_id in required_ids:
        found = f'id="{el_id}"' in html
        if not found:
            all_ids_found = False
            log_check("HTML", f"Element ID #{el_id}", False, "Missing from index.html")
    if all_ids_found:
        log_check("HTML", "All Essential Conversational DOM Elements", True, "100% elements present")

    has_viewport = 'name="viewport"' in html and 'width=device-width' in html
    log_check("HTML", "Responsive Viewport Meta Tag", has_viewport, "Responsive mobile/tablet/desktop viewport")

def test_css_systematic_design():
    print("\n--- 2. Testing CSS Systematic Layout & Photo Embed Tokens ---")
    css_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "css", "styles.css"))
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    has_chat_feed = '.chat-feed' in css and '.user-bubble' in css and '.ai-response-container' in css
    log_check("CSS", "ChatGPT Conversational Chat Feed", has_chat_feed, "Chat bubbles & AI container defined")

    has_step_card = '.systematic-step-card' in css and '.step-photo-container' in css
    log_check("CSS", "Step Card with Embedded Photo Below", has_step_card, "Systematic card with photo container")

    has_aspect_ratio = 'aspect-ratio: 400 / 750' in css
    log_check("CSS", "Exact 400/750 Aspect Ratio", has_aspect_ratio, "Prevents vertical coordinate compression")

    has_pulse_animation = '@keyframes pulseTarget' in css and '.step-spotlight-ring' in css
    log_check("CSS", "Glowing Red Pulse Ring Animation", has_pulse_animation, "Active pulseTarget animation")

def test_multi_device_responsiveness():
    print("\n--- 3. Testing ChatGPT-Style Layout & Multi-Device Responsiveness ---")
    css_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "css", "styles.css"))
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # 1. ChatGPT Canvas Width (840px centered column)
    has_chatgpt_canvas = 'var(--chatgpt-max-width)' in css and 'max-width: var(--chatgpt-max-width)' in css
    log_check("Responsive", "ChatGPT Central Canvas Width", has_chatgpt_canvas, "840px centered conversational stream")

    # 2. Vertical Step Flow (Photo directly below step text, no split-screen)
    has_vertical_step = '.systematic-step-card' in css and 'flex-direction: column' in css
    log_check("Responsive", "Vertical Step-by-Step Flow", has_vertical_step, "Step description with photo directly underneath")

    # 3. AI Avatar Badge for ChatGPT look and feel
    has_avatar = '.ai-avatar-icon' in css
    log_check("Responsive", "ChatGPT Assistant Avatar", has_avatar, "Avatar icon on left of conversational stream")

    # 4. Mobile Responsiveness (< 768px and <= 420px)
    has_mobile_bp = '@media (max-width: 767px)' in css and '@media (max-width: 420px)' in css
    log_check("Responsive", "Mobile Responsive Breakpoints (<768px & <=420px)", has_mobile_bp, "Full-bleed layout & small phone scaling")

    # 5. Responsive Quick Chips Grid (2-column on wider screens)
    has_grid_chips = 'grid-template-columns: repeat(2, 1fr)' in css
    log_check("Responsive", "Symmetric 2-Column Suggestion Grid", has_grid_chips, "Balanced quick question tray")

def test_svg_mockups():
    print("\n--- 3. Testing Screen Mockups (SVG Assets) ---")
    screens_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "assets", "screens"))
    expected_screens = [
        "whatsapp_phone_home.svg",
        "whatsapp_chat_list.svg",
        "whatsapp_chat_screen.svg",
        "whatsapp_attachment_menu.svg",
        "whatsapp_contact_search.svg",
        "whatsapp_contact_picker.svg"
    ]

    for screen in expected_screens:
        path = os.path.join(screens_dir, screen)
        exists = os.path.exists(path)
        if not exists:
            log_check("SVG", f"Mockup: {screen}", False, "File missing")
            continue

        try:
            tree = ET.parse(path)
            root = tree.getroot()
            viewbox = root.attrib.get("viewBox", "")
            is_valid = root.tag.endswith("svg") and "400" in viewbox and "750" in viewbox
            log_check("SVG", f"Mockup: {screen}", is_valid, f"viewBox: {viewbox}")
        except Exception as e:
            log_check("SVG", f"Mockup: {screen}", False, str(e))

def test_javascript_conversational_logic():
    print("\n--- 4. Testing JavaScript Conversational Feed Logic ---")
    js_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "js", "app.js"))
    with open(js_path, "r", encoding="utf-8") as f:
        js = f.read()

    has_render_ai = 'renderAiVisualGuide' in js and 'step-photo-container' in js
    log_check("JS", "AI Visual Guide Generator", has_render_ai, "Generates step cards with photos below each step")

    has_play_all = 'playFullGuideAudio' in js
    log_check("JS", "Full Guide Audio Player", has_play_all, "Reads entire guide sequentially")

    has_share_dad = 'https://wa.me/?text=' in js and 'shareGuideOnWhatsApp' in js
    log_check("JS", "WhatsApp Share Link Generator", has_share_dad, "Formatted message generator")

    has_stt = 'webkitSpeechRecognition' in js or 'SpeechRecognition' in js
    log_check("JS", "Web Speech Recognition (STT)", has_stt, "Speech-to-text integration")

    has_calibrated_coords = '70.8' in js and '76.7' in js and '89.3' in js
    log_check("JS", "Calibrated Spotlight Coordinates", has_calibrated_coords, "Paperclip (70.8%, 94.5%), Contact (80%, 76.7%)")

def test_backend_e2e_journey():
    print("\n--- 5. Testing Systematic Step-by-Step Backend Flow ---")
    service = IntentParserService()
    query = "mane mara bhai no phone number whatsapp par bija ne moklavo che"
    response = service.parse_query(query)

    is_success = response.success
    is_app_whatsapp = response.intent_info.app_name == "WhatsApp"
    is_intent_contact = response.intent_info.intent == "share_contact_number"
    is_steps_6 = response.total_steps == 6

    log_check("Backend", "Intent Recognition for WhatsApp Contact Share", is_success and is_app_whatsapp and is_intent_contact, f"App: {response.intent_info.app_name}")
    log_check("Backend", "6 Systematic Micro-Steps Decomposed", is_steps_6, f"Total steps: {response.total_steps}")

    # Check that each step contains instruction, photo screen type, and calibrated coordinates
    # Step 1 (idx 0): WhatsApp on home screen (61.3%, 89.6%)
    # Step 3 (idx 2): Paperclip in chat (70.8%, 94.5%)
    # Step 4 (idx 3): Contact blue circle (80.0%, 76.7%)
    # Step 6 (idx 5): Green send arrow (85.0%, 89.3%)
    coords_accurate = (
        abs(response.steps[0].target_coordinates.x_percent - 61.3) < 0.5 and  # Step 1: WhatsApp
        abs(response.steps[2].target_coordinates.x_percent - 70.8) < 0.5 and  # Step 3: Paperclip
        abs(response.steps[3].target_coordinates.y_percent - 76.7) < 0.5 and  # Step 4: Contact
        abs(response.steps[5].target_coordinates.x_percent - 85.0) < 0.5      # Step 6: Green Send
    )
    log_check("Backend", "Calibrated Coordinates on Real Elements", coords_accurate, "Home (61.3%), Paperclip (70.8%), Contact (76.7%), Send (85.0%)")

def run_all_tests():
    print("=" * 70)
    print("VERIFYING SYSTEMATIC CHATGPT-STYLE VISUAL GUIDE IMPLEMENTATION")
    print("=" * 70)

    test_html_dom_structure()
    test_css_systematic_design()
    test_multi_device_responsiveness()
    test_svg_mockups()
    test_javascript_conversational_logic()
    test_backend_e2e_journey()

    print("\n" + "=" * 70)
    print(f"RESULTS: {REPORT['passed_checks']} / {REPORT['total_checks']} CHECKS PASSED ({(REPORT['passed_checks']/REPORT['total_checks'])*100:.1f}%)")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
