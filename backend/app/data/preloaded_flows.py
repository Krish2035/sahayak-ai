"""
Curated, pre-verified task flows for senior digital assistance.
Contains pixel-perfect coordinate maps and native translations for common senior tasks.
"""

PRELOADED_FLOWS = {
    "whatsapp_share_contact": {
        "app_name": "WhatsApp",
        "intent": "share_contact_number",
        "keywords": [
            "number", "contact", "phone number", "send number", "share contact",
            "નંબર", "કોન્ટેક્ટ", "મોકલો", "મોકલવો",
            "नंबर", "कांटेक्ट", "भेजना", "भेजें"
        ],
        "flows": {
            "en": {
                "title": "Send a Contact Number on WhatsApp",
                "summary": "Easily send someone's phone number in a WhatsApp chat.",
                "reassurance_banner": "Don't worry, this will only share the phone number. Nothing will be deleted.",
                "steps": [
                    {
                        "step_number": 1,
                        "title": "Open WhatsApp",
                        "instruction": "Find the green WhatsApp icon on your phone's home screen and tap it once to open the app.",
                        "target_ui_element": "WhatsApp Green App Icon",
                        "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5, "description": "Green WhatsApp icon on home screen"},
                        "audio_text": "First, find the green WhatsApp icon on your phone screen and tap it once.",
                        "screen_type": "whatsapp_phone_home",
                        "reassurance": "This will safely open WhatsApp on your phone."
                    },
                    {
                        "step_number": 2,
                        "title": "Go to the Contact You Want to Send to",
                        "instruction": "Find and tap the name of the person you want to send the phone number to (for example, your brother or friend).",
                        "target_ui_element": "Contact's Chat Name",
                        "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5, "description": "Tap on the contact's chat"},
                        "audio_text": "Tap the name of the person you want to send the number to to open their chat.",
                        "screen_type": "whatsapp_chat_list",
                        "reassurance": "Tapping their name opens the message conversation."
                    },
                    {
                        "step_number": 3,
                        "title": "Tap the Paperclip Icon",
                        "instruction": "At the bottom right where you type messages, tap the small Paperclip symbol 📎.",
                        "target_ui_element": "📎 Paperclip Attachment Icon",
                        "target_coordinates": {"x_percent": 70.8, "y_percent": 94.5, "radius_percent": 5.5, "description": "Paperclip icon at bottom right"},
                        "audio_text": "At the bottom right where you write messages, tap the small paperclip symbol.",
                        "screen_type": "whatsapp_chat_screen",
                        "reassurance": "This safely opens attachment options like photos and contacts."
                    },
                    {
                        "step_number": 4,
                        "title": "Select 'Contact' Option in That Window",
                        "instruction": "A colorful popup menu will appear. Tap the blue circular button with the white person symbol labeled 'Contact' 👤.",
                        "target_ui_element": "👤 Blue Contact Option",
                        "target_coordinates": {"x_percent": 80.0, "y_percent": 76.7, "radius_percent": 7.0, "description": "Blue Contact circle in popup menu"},
                        "audio_text": "Now tap the blue circle with the person symbol that says Contact.",
                        "screen_type": "whatsapp_attachment_menu",
                        "reassurance": "This opens your phone's address book."
                    },
                    {
                        "step_number": 5,
                        "title": "Search & Select the Contact You Want to Send",
                        "instruction": "Search or scroll down to find the contact whose number you want to share, and tap their name to select it.",
                        "target_ui_element": "Target Contact Name to Send",
                        "target_coordinates": {"x_percent": 50.0, "y_percent": 23.6, "radius_percent": 8.0, "description": "Tap the contact whose number to share"},
                        "audio_text": "Find and tap the name of the person whose number you want to share.",
                        "screen_type": "whatsapp_contact_search",
                        "reassurance": "A green checkmark will appear next to their name."
                    },
                    {
                        "step_number": 6,
                        "title": "Click on the Green Icon to Send",
                        "instruction": "At the very bottom right, tap the round green button with the white arrow ➡️. The phone number is now sent!",
                        "target_ui_element": "Green Circular Send Arrow Button",
                        "target_coordinates": {"x_percent": 85.0, "y_percent": 89.3, "radius_percent": 7.5, "description": "Green Send arrow button at bottom right"},
                        "audio_text": "Finally, tap the round green arrow button at the bottom right. The number has been sent!",
                        "screen_type": "whatsapp_contact_picker",
                        "reassurance": "The phone number has been sent safely."
                    }
                ]
            },
            "gu": {
                "title": "વોટ્સએપ પર ફોન નંબર મોકલો",
                "summary": "વોટ્સએપ ચેટમાં સરળતાથી કોઈનો ફોન નંબર બીજાને મોકલો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, આનાથી ફક્ત ફોન નંબર જશે. ફોનમાંથી કશું જ ડિલીટ નહીં થાય.",
                "steps": [
                    {
                        "step_number": 1,
                        "title": "1. વૉટ્સએપ ખોલો (Open WhatsApp)",
                        "instruction": "તમારા ફોનની સ્ક્રીન પર લીલા રંગનું વૉટ્સએપનું ગોળ નિશાન શોધો અને તેના પર એક વાર ટચ કરો.",
                        "target_ui_element": "વૉટ્સએપ એપનું લીલું નિશાન",
                        "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5, "description": "ફોનની સ્ક્રીન પર વૉટ્સએપ આઇકન"},
                        "audio_text": "સૌપ્રથમ તમારા ફોનમાં લીલા રંગના વૉટ્સએપ નિશાન પર એક વાર અડો.",
                        "screen_type": "whatsapp_phone_home",
                        "reassurance": "આનાથી તમારા ફોનમાં વૉટ્સએપ ખુલશે."
                    },
                    {
                        "step_number": 2,
                        "title": "2. જેમને નંબર મોકલવો છે તેમની ચેટ ખોલો",
                        "instruction": "જે વ્યક્તિને તમારે ફોન નંબર મોકલવો છે (દા.ત. તમારા ભાઈ કે મિત્ર), તેમના નામ પર ટચ કરીને ચેટ ખોલો.",
                        "target_ui_element": "વ્યક્તિની ચેટનું નામ",
                        "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5, "description": "જેમને નંબર મોકલવો છે તેમના નામ પર ટચ કરો"},
                        "audio_text": "હવે જેમને નંબર મોકલવો છે તેમના નામ પર ટચ કરીને વાતચીત ખોલો.",
                        "screen_type": "whatsapp_chat_list",
                        "reassurance": "એમના નામ પર ટચ કરવાથી મેસેજની સ્ક્રીન ખુલશે."
                    },
                    {
                        "step_number": 3,
                        "title": "3. પેપરક્લિપ (ક્લિપ) ના નિશાન પર ટચ કરો",
                        "instruction": "નીચે જ્યાં મેસેજ લખો છો તેની જમણી બાજુ નાની ક્લિપ જેવું નિશાન 📎 દેખાશે. તેના પર ટચ કરો.",
                        "target_ui_element": "📎 પેપરક્લિપ આઇકન",
                        "target_coordinates": {"x_percent": 70.8, "y_percent": 94.5, "radius_percent": 5.5, "description": "નીચે જમણી બાજુ ક્લિપનું નિશાન"},
                        "audio_text": "નીચે મેસેજ લખવાની જગ્યા પાસે નાની પેપરક્લિપ પર અડો.",
                        "screen_type": "whatsapp_chat_screen",
                        "reassurance": "આનાથી ફોટો કે નંબર મોકલવાના વિકલ્પો દેખાશે."
                    },
                    {
                        "step_number": 4,
                        "title": "4. મેનૂમાંથી 'Contact' (વાદળી ગોળ) પસંદ કરો",
                        "instruction": "એક નાનું રંગીન મેનૂ ખુલશે. તેમાં વાદળી રંગના ગોળ 'Contact' (માણસના ચહેરાવાળા) બટન પર ટચ કરો.",
                        "target_ui_element": "👤 વાદળી કોન્ટેક્ટ બટન",
                        "target_coordinates": {"x_percent": 80.0, "y_percent": 76.7, "radius_percent": 7.0, "description": "મેનૂમાં વાદળી કોન્ટેક્ટનું ગોળ નિશાન"},
                        "audio_text": "હવે વાદળી રંગના કોન્ટેક્ટ વાળા બટન પર ટચ કરો.",
                        "screen_type": "whatsapp_attachment_menu",
                        "reassurance": "આનાથી તમારા ફોનની કોન્ટેક્ટ લિસ્ટ ખુલશે."
                    },
                    {
                        "step_number": 5,
                        "title": "5. જે વ્યક્તિનો નંબર મોકલવો છે તેમને શોધીને પસંદ કરો",
                        "instruction": "ઉપર સર્ચમાં જે વ્યક્તિનો નંબર મોકલવો હોય તેમનું નામ લખો અથવા લિસ્ટમાંથી શોધીને તેમના નામ પર ટચ કરો.",
                        "target_ui_element": "મોકલવા માટે કોન્ટેક્ટનું નામ",
                        "target_coordinates": {"x_percent": 50.0, "y_percent": 23.6, "radius_percent": 8.0, "description": "જેમનો નંબર મોકલવો છે તેમના નામ પર ટચ કરો"},
                        "audio_text": "જેમનો નંબર મોકલવો હોય તેમના નામ પર ટચ કરો.",
                        "screen_type": "whatsapp_contact_search",
                        "reassurance": "તેમના નામ પાસે લીલું નિશાન આવી જશે."
                    },
                    {
                        "step_number": 6,
                        "title": "6. નીચે આપેલા લીલા બટન પર ટચ કરો",
                        "instruction": "સૌથી નીચે જમણી બાજુ આપેલા લીલા રંગના તીર ➡️ વાળા સેન્ડ બટન પર ટચ કરો. નંબર સફળતાપૂર્વક પહોંચી જશે!",
                        "target_ui_element": "લીલું સેન્ડ (મોકલો) બટન",
                        "target_coordinates": {"x_percent": 85.0, "y_percent": 89.3, "radius_percent": 7.5, "description": "જમણી બાજુ નીચે લીલું તીરનું બટન"},
                        "audio_text": "નામ પસંદ કર્યા પછી નીચે લીલા તીર પર અડો. નંબર પહોંચી ગયો છે!",
                        "screen_type": "whatsapp_contact_picker",
                        "reassurance": "નંબર સફળતાપૂર્વક મોકલાઈ ગયો છે."
                    }
                ]
            },
            "hi": {
                "title": "व्हाट्सएप पर फोन नंबर भेजें",
                "summary": "व्हाट्सएप चैट में किसी का भी फोन नंबर आसानी से भेजें।",
                "reassurance_banner": "चिंता मत कीजिए, इससे सिर्फ फोन नंबर जाएगा। फोन से कुछ भी डिलीट नहीं होगा।",
                "steps": [
                    {
                        "step_number": 1,
                        "title": "1. व्हाट्सएप खोलें (Open WhatsApp)",
                        "instruction": "अपने फोन की स्क्रीन पर हरे रंग का व्हाट्सएप का निशान देखें और उस पर एक बार छुएं।",
                        "target_ui_element": "व्हाट्सएप का हरा निशान",
                        "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5, "description": "फोन स्क्रीन पर व्हाट्सएप आइकॉन"},
                        "audio_text": "सबसे पहले अपने फोन में हरे रंग के व्हाट्सएप निशान पर एक बार छुएं।",
                        "screen_type": "whatsapp_phone_home",
                        "reassurance": "इससे आपके फोन में व्हाट्सएप खुल जाएगा।"
                    },
                    {
                        "step_number": 2,
                        "title": "2. जिन्हें नंबर भेजना है उनकी चैट खोलें",
                        "instruction": "जिस व्यक्ति को आप फोन नंबर भेजना चाहते हैं (जैसे आपके भाई या दोस्त), उनके नाम पर टैप करें।",
                        "target_ui_element": "व्यक्ति का चैट नाम",
                        "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5, "description": "जिन्हें नंबर भेजना है उनकी चैट खोलें"},
                        "audio_text": "जिन्हें नंबर भेजना है उनके नाम पर टैप करके चैट खोलें।",
                        "screen_type": "whatsapp_chat_list",
                        "reassurance": "उनके नाम पर टैप करने से बातचीत खुल जाएगी।"
                    },
                    {
                        "step_number": 3,
                        "title": "3. पिन (पेपरक्लिप) के निशान को छुएं",
                        "instruction": "नीचे जहां मैसेज लिखते हैं, उसके पास छोटी पिन जैसी क्लिप 📎 दिखेगी। उस पर टैप करें।",
                        "target_ui_element": "📎 पिन या पेपरक्लिप का निशान",
                        "target_coordinates": {"x_percent": 70.8, "y_percent": 94.5, "radius_percent": 5.5, "description": "नीचे दाईं तरफ क्लिप का निशान"},
                        "audio_text": "नीचे जहां टाइप करते हैं, वहां छोटी पिन के निशान पर छुएं।",
                        "screen_type": "whatsapp_chat_screen",
                        "reassurance": "इससे नंबर और फोटो भेजने के विकल्प खुलेंगे।"
                    },
                    {
                        "step_number": 4,
                        "title": "4. मेनू से 'Contact' (नीला गोल) चुनें",
                        "instruction": "रंगीन गोल बटन खुलेंगे। इनमें नीले रंग के 'Contact' (आदमी का निशान) वाले बटन को छुएं।",
                        "target_ui_element": "👤 नीला कांटेक्ट बटन",
                        "target_coordinates": {"x_percent": 80.0, "y_percent": 76.7, "radius_percent": 7.0, "description": "मेनू में नीले कांटेक्ट का निशान"},
                        "audio_text": "अब नीले रंग वाले कांटेक्ट बटन को छुएं।",
                        "screen_type": "whatsapp_attachment_menu",
                        "reassurance": "इससे आपके फोन के सभी नंबर दिखेंगे।"
                    },
                    {
                        "step_number": 5,
                        "title": "5. जिसका नंबर भेजना है उसे चुन लें",
                        "instruction": "ऊपर सर्च में नाम लिखें या लिस्ट से देखकर जिसका नंबर भेजना है उनके नाम पर टैप करें।",
                        "target_ui_element": "कांटेक्ट का नाम",
                        "target_coordinates": {"x_percent": 50.0, "y_percent": 23.6, "radius_percent": 8.0, "description": "कांटेक्ट के नाम पर टैप करें"},
                        "audio_text": "जिसका नंबर भेजना है उनके नाम पर टैप करें।",
                        "screen_type": "whatsapp_contact_search",
                        "reassurance": "उनके नाम के आगे हरा निशान लग जाएगा।"
                    },
                    {
                        "step_number": 6,
                        "title": "6. नीचे दिए गए हरे तीर वाले बटन को दबाएं",
                        "instruction": "सबसे नीचे दाईं तरफ हरे तीर ➡️ वाले बटन को दबा दें। नंबर चला गया!",
                        "target_ui_element": "हरा सेंड तीर बटन",
                        "target_coordinates": {"x_percent": 85.0, "y_percent": 89.3, "radius_percent": 7.5, "description": "हरे रंग का सेंड बटन"},
                        "audio_text": "नीचे हरे तीर वाले बटन को दबाएं। नंबर सफलतापूर्वक चला गया!",
                        "screen_type": "whatsapp_contact_picker",
                        "reassurance": "नंबर सफलतापूर्वक भेजा जा चुका है।"
                    }
                ]
            }
        }
    },
    "whatsapp_send_photo": {
        "app_name": "WhatsApp",
        "intent": "send_photo",
        "keywords": ["photo", "picture", "image", "ફોટો", "તસવીર", "फोटो", "तस्वीर"],
        "flows": {
            "en": {
                "title": "Send a Photo on WhatsApp",
                "summary": "Send any picture from your gallery to your family or friend.",
                "reassurance_banner": "Don't worry, the photo stays safely saved on your phone too.",
                "steps": [
                    {"step_number": 1, "title": "Open Chat", "instruction": "Open the conversation with the person you want to send the photo to.", "target_ui_element": "Chat conversation", "target_coordinates": {"x_percent": 50.0, "y_percent": 30.0, "radius_percent": 8.0, "description": "Tap contact chat"}, "audio_text": "Open the chat of the person.", "screen_type": "whatsapp_chat_list"},
                    {"step_number": 2, "title": "Tap Camera or Paperclip", "instruction": "Tap the small Camera 📷 or Paperclip 📎 icon next to the typing area at the bottom.", "target_ui_element": "📷 Camera icon", "target_coordinates": {"x_percent": 90.0, "y_percent": 94.0, "radius_percent": 6.5, "description": "Camera icon at bottom right"}, "audio_text": "Tap the camera icon at the bottom.", "screen_type": "whatsapp_chat_screen"},
                    {"step_number": 3, "title": "Select Photo and Tap Send", "instruction": "Tap the photo you want to send, then tap the green round Send button with the white arrow ➡️.", "target_ui_element": "Green Send arrow", "target_coordinates": {"x_percent": 90.0, "y_percent": 93.0, "radius_percent": 7.0, "description": "Green send button"}, "audio_text": "Select your photo and tap the green send button.", "screen_type": "whatsapp_photo_preview"}
                ]
            },
            "gu": {
                "title": "વોટ્સએપ પર ફોટો મોકલો",
                "summary": "તમારા ફોનમાંથી કોઈપણ ફોટો બીજાને મોકલો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, ફોટો તમારા ફોનમાં પણ સુરક્ષિત રહેશે.",
                "steps": [
                    {"step_number": 1, "title": "ચેટ ખોલો", "instruction": "જેમને ફોટો મોકલવો હોય તેમની ચેટ ખોલો.", "target_ui_element": "ચેટનું નામ", "target_coordinates": {"x_percent": 50.0, "y_percent": 30.0, "radius_percent": 8.0, "description": "ચેટ ખોલો"}, "audio_text": "જેમને ફોટો મોકલવો હોય તેમની વાતચીત ખોલો.", "screen_type": "whatsapp_chat_list"},
                    {"step_number": 2, "title": "કેમેરા પર ટચ કરો", "instruction": "નીચે જમણી બાજુ આપેલા કેમેરા 📷 ના નિશાન પર ટચ કરો.", "target_ui_element": "📷 કેમેરાનું નિશાન", "target_coordinates": {"x_percent": 90.0, "y_percent": 94.0, "radius_percent": 6.5, "description": "કેમેરા બટન"}, "audio_text": "નીચે આપેલા કેમેરાના નિશાન પર અડો.", "screen_type": "whatsapp_chat_screen"},
                    {"step_number": 3, "title": "ફોટો પસંદ કરી મોકલો", "instruction": "તમારો ફોટો પસંદ કરો અને નીચે લીલા રંગના સેન્ડ બટન ➡️ પર ટચ કરો.", "target_ui_element": "લીલું સેન્ડ બટન", "target_coordinates": {"x_percent": 90.0, "y_percent": 93.0, "radius_percent": 7.0, "description": "લીલું સેન્ડ બટન"}, "audio_text": "ફોટો પસંદ કરીને લીલા બટન પર અડો. ફોટો મોકલાઈ ગયો!", "screen_type": "whatsapp_photo_preview"}
                ]
            },
            "hi": {
                "title": "व्हाट्सएप पर फोटो भेजें",
                "summary": "अपनी गैलरी से कोई भी फोटो आसानी से भेजें।",
                "reassurance_banner": "चिंता मत कीजिए, फोटो आपके फोन में भी सुरक्षित रहेगी।",
                "steps": [
                    {"step_number": 1, "title": "चैट खोलें", "instruction": "जिन्हें फोटो भेजना है, उनका चैट खोलें।", "target_ui_element": "चैट नाम", "target_coordinates": {"x_percent": 50.0, "y_percent": 30.0, "radius_percent": 8.0, "description": "चैट खोलें"}, "audio_text": "जिन्हें फोटो भेजना है उनकी चैट खोलें।", "screen_type": "whatsapp_chat_list"},
                    {"step_number": 2, "title": "कैमरा छुएं", "instruction": "नीचे दिए गए कैमरा 📷 के निशान को छुएं।", "target_ui_element": "📷 कैमरा निशान", "target_coordinates": {"x_percent": 90.0, "y_percent": 94.0, "radius_percent": 6.5, "description": "कैमरा बटन"}, "audio_text": "नीचे कैमरे के निशान पर टैप करें।", "screen_type": "whatsapp_chat_screen"},
                    {"step_number": 3, "title": "फोटो चुनकर भेजें", "instruction": "अपनी फोटो चुनें और नीचे हरे तीर ➡️ वाले बटन को दबा दें।", "target_ui_element": "हरा सेंड बटन", "target_coordinates": {"x_percent": 90.0, "y_percent": 93.0, "radius_percent": 7.0, "description": "हरा सेंड बटन"}, "audio_text": "फोटो चुनकर हरे तीर पर टैप करें। फोटो चली गई!", "screen_type": "whatsapp_photo_preview"}
                ]
            }
        }
    },
    "gpay_scan_qr": {
        "app_name": "Google Pay",
        "intent": "scan_qr_code",
        "keywords": ["scan", "qr", "pay", "google pay", "gpay", "સ્કેન", "રૂપિયા", "पेमेंट", "स्कैन", "क्यूआर"],
        "flows": {
            "en": {
                "title": "Scan a QR Code to Pay on Google Pay",
                "summary": "Pay at a shop by scanning the shop's QR code stand.",
                "reassurance_banner": "You will always see the amount and verify before entering your UPI PIN.",
                "steps": [
                    {"step_number": 1, "title": "Open Google Pay", "instruction": "Unlock Google Pay on your phone.", "target_ui_element": "App icon", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 10.0, "description": "Open GPay"}, "audio_text": "Open Google Pay on your screen.", "screen_type": "gpay_home"},
                    {"step_number": 2, "title": "Tap 'Scan any QR code'", "instruction": "At the top of the screen, tap the big square button that says 'Scan any QR code'.", "target_ui_element": "Scan QR Code button", "target_coordinates": {"x_percent": 25.0, "y_percent": 22.0, "radius_percent": 9.0, "description": "Scan QR box at top left"}, "audio_text": "Tap the button that says Scan any QR code.", "screen_type": "gpay_home"},
                    {"step_number": 3, "title": "Point Camera at Shop's Code", "instruction": "Hold your phone steady in front of the shop's QR code until it beeps.", "target_ui_element": "Camera viewfinder box", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 15.0, "description": "Square scanner frame"}, "audio_text": "Hold your camera in front of the shop's QR code.", "screen_type": "scanner_camera"},
                    {"step_number": 4, "title": "Enter Amount & PIN", "instruction": "Type the exact amount to pay, check the shopkeeper's name, and enter your secret UPI PIN.", "target_ui_element": "Amount text box & Pay button", "target_coordinates": {"x_percent": 50.0, "y_percent": 90.0, "radius_percent": 8.0, "description": "Pay button"}, "audio_text": "Enter the amount and enter your UPI PIN. Payment is complete!", "screen_type": "gpay_amount_screen"}
                ]
            },
            "gu": {
                "title": "ગૂગલ પે પર દુકાને ક્યૂઆર કોડ સ્કેન કરો",
                "summary": "દુકાનદારના ક્યૂઆર કોડ પર સ્કેન કરીને પેમેન્ટ કરો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, તમારો ગુપ્ત પિન નાખ્યા વગર પૈસા નહીં કપાય.",
                "steps": [
                    {"step_number": 1, "title": "ગૂગલ પે ખોલો", "instruction": "તમારા ફોનમાં ગૂગલ પે (Google Pay) એપ ખોલો.", "target_ui_element": "એપ ખોલો", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 10.0, "description": "ગૂગલ પે ખોલો"}, "audio_text": "સૌપ્રથમ ગૂગલ પે એપ ખોલો.", "screen_type": "gpay_home"},
                    {"step_number": 2, "title": "'Scan QR code' પર ટચ કરો", "instruction": "ઉપર ડાબી બાજુ મોટા ચોરસ 'Scan any QR code' ના બટન પર ટચ કરો.", "target_ui_element": "સ્કેન ક્યૂઆર કોડ બટન", "target_coordinates": {"x_percent": 25.0, "y_percent": 22.0, "radius_percent": 9.0, "description": "સ્કેન બટન પર અડો"}, "audio_text": "ઉપર આપેલા સ્કેન ક્યૂઆર કોડ ના બટન પર અડો.", "screen_type": "gpay_home"},
                    {"step_number": 3, "title": "કેમેરા કોડ સામે રાખો", "instruction": "દુકાનદારના ક્યૂઆર કોડ સામે તમારો ફોન સ્થિર પકડી રાખો.", "target_ui_element": "સ્કેનર ચોરસ ફ્રેમ", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 15.0, "description": "કેમેરા ચોરસ ફ્રેમ"}, "audio_text": "દુકાનદારના કોડ સામે કેમેરો રાખો જ્યાં સુધી બીપ અવાજ ન આવે.", "screen_type": "scanner_camera"},
                    {"step_number": 4, "title": "રકમ અને પિન નાખો", "instruction": "રૂપિયાની રકમ લખો, દુકાનદારનું નામ ચકાસો અને તમારો ગુપ્ત UPI પિન નાખો.", "target_ui_element": "પે બટન", "target_coordinates": {"x_percent": 50.0, "y_percent": 90.0, "radius_percent": 8.0, "description": "પે બટન"}, "audio_text": "રૂપિયા નાખી તમારો પિન દાખલ કરો. પેમેન્ટ થઈ ગયું!", "screen_type": "gpay_amount_screen"}
                ]
            },
            "hi": {
                "title": "गूगल पे पर क्यूआर कोड स्कैन करके भुगतान करें",
                "summary": "दुकानदार का क्यूआर कोड स्कैन करके आसानी से पैसे भेजें।",
                "reassurance_banner": "चिंता मत कीजिए, बिना यूपीआई पिन डाले एक भी रुपया नहीं कटेगा।",
                "steps": [
                    {"step_number": 1, "title": "गूगल पे खोलें", "instruction": "अपने फोन में गूगल पे खोलें।", "target_ui_element": "गूगल पे खोलें", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 10.0, "description": "गूगल पे खोलें"}, "audio_text": "गूगल पे ऐप खोलें।", "screen_type": "gpay_home"},
                    {"step_number": 2, "title": "'Scan any QR code' पर टैप करें", "instruction": "स्क्रीन पर ऊपर दिए गए 'Scan any QR code' बटन को छुएं।", "target_ui_element": "स्कैन बटन", "target_coordinates": {"x_percent": 25.0, "y_percent": 22.0, "radius_percent": 9.0, "description": "स्कैन बटन"}, "audio_text": "ऊपर दिए गए स्कैन क्यूआर कोड बटन को छुएं।", "screen_type": "gpay_home"},
                    {"step_number": 3, "title": "कैमरा दुकान के कोड पर रखें", "instruction": "दुकान के क्यूआर कोड के सामने अपने फोन का कैमरा सीधा रखें।", "target_ui_element": "स्कैनर फ्रेम", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 15.0, "description": "कैमरा फ्रेम"}, "audio_text": "दुकानदार के कोड के सामने कैमरा सीधा रखें।", "screen_type": "scanner_camera"},
                    {"step_number": 4, "title": "रुपये डालें और यूपीआई पिन दर्ज करें", "instruction": "दुकानदार का नाम देखकर रुपये डालें और अपना गुप्त यूपीआई पिन डालें।", "target_ui_element": "पे बटन", "target_coordinates": {"x_percent": 50.0, "y_percent": 90.0, "radius_percent": 8.0, "description": "पे बटन"}, "audio_text": "रुपये लिखकर अपना गुप्त पिन डालें। पेमेंट पूरा हो गया!", "screen_type": "gpay_amount_screen"}
                ]
            }
        }
    },
    "settings_font_size": {
        "app_name": "Settings",
        "intent": "increase_font_size",
        "keywords": ["font", "size", "bigger text", "akshar", "mota", "font size", "મોટા અક્ષર", "अक्षर बड़े", "फॉन्ट"],
        "flows": {
            "en": {
                "title": "Make Text & Letters Bigger on Phone",
                "summary": "Increase the screen font size so letters are comfortable and clear to read.",
                "reassurance_banner": "This makes reading much easier. You can change it back anytime.",
                "steps": [
                    {"step_number": 1, "title": "Open Phone Settings", "instruction": "Open the gray Gear icon ⚙️ labeled 'Settings' on your home screen.", "target_ui_element": "⚙️ Settings Gear icon", "target_coordinates": {"x_percent": 50.0, "y_percent": 40.0, "radius_percent": 9.0, "description": "Settings app"}, "audio_text": "Open Settings on your phone.", "screen_type": "android_home"},
                    {"step_number": 2, "title": "Tap 'Display'", "instruction": "Scroll down slightly and tap on 'Display' (the Sun or Screen icon).", "target_ui_element": "Display menu item", "target_coordinates": {"x_percent": 50.0, "y_percent": 45.0, "radius_percent": 8.0, "description": "Display option"}, "audio_text": "Tap on Display.", "screen_type": "settings_list"},
                    {"step_number": 3, "title": "Tap 'Font Size'", "instruction": "Tap on 'Font size and style'. Drag the round slider to the right to make the letters large and readable.", "target_ui_element": "Font size slider", "target_coordinates": {"x_percent": 75.0, "y_percent": 70.0, "radius_percent": 8.0, "description": "Drag slider right"}, "audio_text": "Move the slider to the right to make text bigger.", "screen_type": "font_settings"}
                ]
            },
            "gu": {
                "title": "ફોનમાં અક્ષરો મોટા કરો",
                "summary": "સ્ક્રીન પર અક્ષરો મોટા કરો જેથી સરળતાથી વાંચી શકાય.",
                "reassurance_banner": "ચિંતા કરશો નહીં, આનાથી વાંચવામાં ઘણી સરળતા રહેશે.",
                "steps": [
                    {"step_number": 1, "title": "સેટિંગ્સ (Settings) ખોલો", "instruction": "ફોનમાં ચક્ર જેવા નિશાન ⚙️ વાળા 'Settings' પર ટચ કરો.", "target_ui_element": "⚙️ સેટિંગ્સ આઇકન", "target_coordinates": {"x_percent": 50.0, "y_percent": 40.0, "radius_percent": 9.0, "description": "સેટિંગ્સ ખોલો"}, "audio_text": "ફોનમાં સેટિંગ્સ એપ ખોલો.", "screen_type": "android_home"},
                    {"step_number": 2, "title": "'Display' (ડિસ્પ્લે) પર ટચ કરો", "instruction": "નીચે જોઈને સૂર્ય જેવા નિશાનવાળા 'Display' પર ટચ કરો.", "target_ui_element": "Display વિકલ્પ", "target_coordinates": {"x_percent": 50.0, "y_percent": 45.0, "radius_percent": 8.0, "description": "ડિસ્પ્લે પર અડો"}, "audio_text": "ડિસ્પ્લે પર ટચ કરો.", "screen_type": "settings_list"},
                    {"step_number": 3, "title": "અક્ષર મોટા કરવા ગોળ બટન જમણી બાજુ ખસેડો", "instruction": "'Font Size' માં ગોળ બટનને જમણી બાજુ ખેંચો. અક્ષરો તરત જ મોટા થઈ જશે.", "target_ui_element": "સ્લાઇડર બટન", "target_coordinates": {"x_percent": 75.0, "y_percent": 70.0, "radius_percent": 8.0, "description": "સ્લાઇડર જમણી બાજુ ખસેડો"}, "audio_text": "ગોળ બટનને જમણી તરફ ખસેડો જેથી અક્ષર મોટા થઈ જશે.", "screen_type": "font_settings"}
                ]
            },
            "hi": {
                "title": "फोन में लिखावट (अक्षर) बड़े करें",
                "summary": "फोन के अक्षरों को बड़ा करें ताकि आसानी से पढ़ा जा सके।",
                "reassurance_banner": "चिंता मत कीजिए, इससे पढ़ने में बहुत आसानी होगी।",
                "steps": [
                    {"step_number": 1, "title": "सेटिंग्स (Settings) खोलें", "instruction": "फोन की स्क्रीन पर पहिए जैसे निशान ⚙️ वाले 'Settings' पर छुएं।", "target_ui_element": "⚙️ सेटिंग्स", "target_coordinates": {"x_percent": 50.0, "y_percent": 40.0, "radius_percent": 9.0, "description": "सेटिंग्स खोलें"}, "audio_text": "फोन में सेटिंग्स ऐप खोलें।", "screen_type": "android_home"},
                    {"step_number": 2, "title": "'Display' (डिस्प्ले) छुएं", "instruction": "नीचे स्क्रॉल करके 'Display' वाले विकल्प पर टैप करें।", "target_ui_element": "Display विकल्प", "target_coordinates": {"x_percent": 50.0, "y_percent": 45.0, "radius_percent": 8.0, "description": "डिस्प्ले विकल्प"}, "audio_text": "डिस्प्ले पर टैप करें।", "screen_type": "settings_list"},
                    {"step_number": 3, "title": "अक्षर बड़े करने के लिए स्लाइडर दाईं ओर खिसकाएं", "instruction": "'Font size' में गोल बिंदी को दाईं तरफ खींचें। सारे अक्षर बड़े हो जाएंगे।", "target_ui_element": "फॉन्ट स्लाइडर", "target_coordinates": {"x_percent": 75.0, "y_percent": 70.0, "radius_percent": 8.0, "description": "स्लाइडर दाईं तरफ खिसकाएं"}, "audio_text": "स्लाइडर को दाईं ओर खींचें, अक्षर बड़े हो जाएंगे।", "screen_type": "font_settings"}
                ]
            }
        }
    }
}

