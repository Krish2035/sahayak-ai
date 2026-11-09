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
        "keywords": ["font", "size", "bigger text", "akshar", "mota", "font size", "મોટા અક્ષર", "અક્ષરો", "અક્ષર", "મોટા", "अक्षर बड़े", "अक्षर", "लिखावट", "फॉन्ट"],
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
    },
    "youtube_download_bhajan": {
        "app_name": "YouTube",
        "intent": "download_youtube_video",
        "keywords": ["youtube", "bhajan", "download", "ભજન", "ડાઉનલોડ", "ગીત", "યુટ્યુબ", "भजन", "डाउनलोड", "गाने"],
        "flows": {
            "gu": {
                "title": "YouTube પર ભજન ડાઉનલોડ કરો",
                "summary": "તમારા મનપસંદ ભજનને ફોનમાં ડાઉનલોડ કરો જેથી ઇન્ટરનેટ વગર પણ સાંભળી શકાય.",
                "reassurance_banner": "ચિંતા કરશો નહીં, આ ભજન તમારા YouTube માં સુરક્ષિત સેવ રહેશે અને ગમે ત્યારે વાગશે.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. YouTube એપ ખોલો", "instruction": "તમારા ફોનમાં લાલ રંગનું YouTube નું નિશાન શોધો અને તેના પર ટચ કરો.", "target_ui_element": "લાલ YouTube આઇકન", "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "સૌપ્રથમ લાલ રંગની YouTube એપ ખોલો.", "screen_type": "whatsapp_phone_home", "reassurance": "YouTube એપ ખુલશે."},
                    {"step_number": 2, "title": "2. ઉપર સર્ચમાં ભજનનું નામ લખો", "instruction": "ઉપર આપેલા કાચ જેવા સર્ચ 🔍 નિશાન પર ટચ કરી જે ભજન સાંભળવું હોય તેનું નામ લખો.", "target_ui_element": "🔍 સર્ચ બટન", "target_coordinates": {"x_percent": 82.5, "y_percent": 4.0, "radius_percent": 6.5}, "audio_text": "ઉપર સર્ચમાં ભજનનું નામ લખો.", "screen_type": "youtube_bhajan_screen", "reassurance": "ભજનનું લિસ્ટ દેખાશે."},
                    {"step_number": 3, "title": "3. વિડીયો નીચે 'ડાઉનલોડ' પર ટચ કરો", "instruction": "ભજન ચાલુ થાય પછી વિડીયોની નીચે ગોળ તીર ⬇️ વાળા 'ડાઉનલોડ' (Download) બટન પર ટચ કરો.", "target_ui_element": "⬇️ ડાઉનલોડ બટન", "target_coordinates": {"x_percent": 63.0, "y_percent": 52.0, "radius_percent": 7.5}, "audio_text": "વિડીયોની નીચે ડાઉનલોડ બટન પર અડો.", "screen_type": "youtube_bhajan_screen", "reassurance": "ડાઉનલોડ શરૂ થઈ જશે."},
                    {"step_number": 4, "title": "4. ભજન ડાઉનલોડ થઈ ગયું છે!", "instruction": "નીચે લાઈબ્રેરી 📚 માં જઈને તમે નેટ વગર પણ આ ભજન ગમે ત્યારે સાંભળી શકશો.", "target_ui_element": "લાઈબ્રેરી સેવ", "target_coordinates": {"x_percent": 87.5, "y_percent": 96.0, "radius_percent": 6.0}, "audio_text": "ભજન ડાઉનલોડ થઈ ગયું છે. હવે ઇન્ટરનેટ વગર પણ સાંભળી શકશો.", "screen_type": "youtube_bhajan_screen", "reassurance": "ભજન સફળતાપૂર્વક સેવ થઈ ગયું છે."}
                ]
            },
            "hi": {
                "title": "YouTube पर भजन डाउनलोड करें",
                "summary": "अपने पसंदीदा भजन को फोन में डाउनलोड करें ताकि बिना इंटरनेट भी सुन सकें।",
                "reassurance_banner": "चिंता मत कीजिए, यह भजन आपके यूट्यूब में हमेशा के लिए सुरक्षित रहेगा।",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. YouTube ऐप खोलें", "instruction": "फोन में लाल रंग का YouTube का निशान देखकर उस पर टैप करें।", "target_ui_element": "लाल YouTube निशान", "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "सबसे पहले यूट्यूब ऐप खोलें।", "screen_type": "whatsapp_phone_home", "reassurance": "यूट्यूब खुल जाएगा।"},
                    {"step_number": 2, "title": "2. ऊपर सर्च में भजन का नाम लिखें", "instruction": "ऊपर दिए गए सर्च 🔍 निशान पर टैप करके जो भजन सुनना हो उसका नाम लिखें।", "target_ui_element": "🔍 सर्च बटन", "target_coordinates": {"x_percent": 82.5, "y_percent": 4.0, "radius_percent": 6.5}, "audio_text": "ऊपर सर्च में भजन का नाम खोजें।", "screen_type": "youtube_bhajan_screen", "reassurance": "भजन की लिस्ट दिखेगी।"},
                    {"step_number": 3, "title": "3. वीडियो के नीचे 'डाउनलोड' छुएं", "instruction": "वीडियो के नीचे तीर ⬇️ वाले 'डाउनलोड' (Download) बटन को छुएं।", "target_ui_element": "⬇️ डाउनलोड बटन", "target_coordinates": {"x_percent": 63.0, "y_percent": 52.0, "radius_percent": 7.5}, "audio_text": "वीडियो के नीचे डाउनलोड बटन पर टैप करें।", "screen_type": "youtube_bhajan_screen", "reassurance": "डाउनलोड होना शुरू हो जाएगा।"},
                    {"step_number": 4, "title": "4. भजन डाउनलोड हो गया!", "instruction": "नीचे लाइब्रेरी 📚 में जाकर आप बिना इंटरनेट के भी यह भजन सुन सकते हैं।", "target_ui_element": "लाइब्रेरी सेव", "target_coordinates": {"x_percent": 87.5, "y_percent": 96.0, "radius_percent": 6.0}, "audio_text": "भजन डाउनलोड हो गया है। अब बिना इंटरनेट भी सुन सकते हैं।", "screen_type": "youtube_bhajan_screen", "reassurance": "सफलतापूर्वक सेव हो गया।"}
                ]
            },
            "en": {
                "title": "Download Bhajans or Videos on YouTube",
                "summary": "Save your favorite devotional songs to watch or listen offline without internet.",
                "reassurance_banner": "Don't worry, the downloaded video will stay safely in your YouTube library.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. Open YouTube App", "instruction": "Find the red YouTube icon on your phone screen and tap it.", "target_ui_element": "YouTube Red App Icon", "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "First, open the YouTube app.", "screen_type": "whatsapp_phone_home", "reassurance": "Opens YouTube safely."},
                    {"step_number": 2, "title": "2. Search for the Bhajan", "instruction": "Tap the search icon 🔍 at the top and type the Bhajan or song title.", "target_ui_element": "🔍 Search Icon", "target_coordinates": {"x_percent": 82.5, "y_percent": 4.0, "radius_percent": 6.5}, "audio_text": "Search for your favorite Bhajan.", "screen_type": "youtube_bhajan_screen", "reassurance": "Finds the song."},
                    {"step_number": 3, "title": "3. Tap 'Download' Below Video", "instruction": "Below the playing video, tap the round 'Download' ⬇️ button.", "target_ui_element": "⬇️ Download Button", "target_coordinates": {"x_percent": 63.0, "y_percent": 52.0, "radius_percent": 7.5}, "audio_text": "Tap the download button below the video.", "screen_type": "youtube_bhajan_screen", "reassurance": "Downloading starts."},
                    {"step_number": 4, "title": "4. Ready to Listen Offline", "instruction": "Your bhajan is saved in your Library 📚. You can play it anytime without data.", "target_ui_element": "Library Saved", "target_coordinates": {"x_percent": 87.5, "y_percent": 96.0, "radius_percent": 6.0}, "audio_text": "Downloaded! You can now listen anytime without internet.", "screen_type": "youtube_bhajan_screen", "reassurance": "Saved safely."}
                ]
            }
        }
    },
    "whatsapp_share_location": {
        "app_name": "WhatsApp",
        "intent": "share_location",
        "keywords": ["location", "live location", "map", "લોકેશન", "ક્યાં છું", "જગ્યા", "लोकेशन", "कहाँ हूँ"],
        "flows": {
            "gu": {
                "title": "વોટ્સએપ પર લાઈવ લોકેશન મોકલો",
                "summary": "પરિવારના સભ્યને તમે ક્યાં છો તે નકશા પર સરળતાથી બતાવો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, ફક્ત તમે પસંદ કરેલા સભ્ય જ તમારું લોકેશન જોઈ શકશે.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. જેમને લોકેશન મોકલવું હોય તેમની ચેટ ખોલો", "instruction": "તમારા દીકરા કે પરિવારજનના નામ પર ટચ કરીને તેમની ચેટ ખોલો.", "target_ui_element": "ચેટનું નામ", "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5}, "audio_text": "જેમને લોકેશન મોકલવું હોય તેમની ચેટ ખોલો.", "screen_type": "whatsapp_chat_list", "reassurance": "ચેટ ખુલશે."},
                    {"step_number": 2, "title": "2. નીચે ક્લિપ (પેપરક્લિપ) પર ટચ કરો", "instruction": "મેસેજ લખવાની જગ્યા પાસે નાની ક્લિપ 📎 ના નિશાન પર ટચ કરો.", "target_ui_element": "📎 પેપરક્લિપ આઇકન", "target_coordinates": {"x_percent": 70.8, "y_percent": 94.5, "radius_percent": 5.5}, "audio_text": "નીચે નાની પેપરક્લિપ પર અડો.", "screen_type": "whatsapp_chat_screen", "reassurance": "વિકલ્પો ખુલશે."},
                    {"step_number": 3, "title": "3. લીલા રંગના 'Location' બટન પર ટચ કરો", "instruction": "મેનૂમાંથી લીલા રંગના ગોળ 'Location' (નકશાના પિન) વાળા બટન પર ટચ કરો.", "target_ui_element": "📍 લીલું લોકેશન બટન", "target_coordinates": {"x_percent": 50.0, "y_percent": 64.0, "radius_percent": 7.0}, "audio_text": "લીલા રંગના લોકેશન વાળા બટન પર ટચ કરો.", "screen_type": "whatsapp_attachment_menu", "reassurance": "નકશો ખુલશે."},
                    {"step_number": 4, "title": "4. 'Send your current location' પર ટચ કરો", "instruction": "'તમારું વર્તમાન લોકેશન મોકલો' પર ટચ કરો. તમારું સરનામું પહોંચી જશે!", "target_ui_element": "કરન્ટ લોકેશન મોકલો", "target_coordinates": {"x_percent": 50.0, "y_percent": 48.0, "radius_percent": 8.0}, "audio_text": "કરન્ટ લોકેશન મોકલો પર અડો. સરનામું પહોંચી ગયું!", "screen_type": "maps_directions_screen", "reassurance": "લોકેશન પહોંચી ગયું છે."}
                ]
            },
            "hi": {
                "title": "WhatsApp पर लाइव लोकेशन भेजें",
                "summary": "परिवार को नक्शे पर बताएं कि आप इस समय कहाँ हैं।",
                "reassurance_banner": "चिंता मत कीजिए, केवल वही व्यक्ति आपका स्थान देख पाएगा जिन्हें आप भेजेंगे।",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. जिन्हें लोकेशन भेजना है उनकी चैट खोलें", "instruction": "परिवार के सदस्य के नाम पर टैप करके उनकी चैट खोलें।", "target_ui_element": "चैट नाम", "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5}, "audio_text": "उनकी चैट खोलें।", "screen_type": "whatsapp_chat_list", "reassurance": "चैट खुलेगी।"},
                    {"step_number": 2, "title": "2. नीचे पिन (पेपरक्लिप) को छुएं", "instruction": "नीचे जहां टाइप करते हैं, वहां पिन 📎 के निशान पर टैप करें।", "target_ui_element": "📎 पिन निशान", "target_coordinates": {"x_percent": 70.8, "y_percent": 94.5, "radius_percent": 5.5}, "audio_text": "पिन के निशान पर टैप करें।", "screen_type": "whatsapp_chat_screen", "reassurance": "विकल्प खुलेंगे।"},
                    {"step_number": 3, "title": "3. हरे 'Location' बटन पर टैप करें", "instruction": "मेनू में हरे रंग के 'Location' वाले बटन को छुएं।", "target_ui_element": "📍 हरा लोकेशन बटन", "target_coordinates": {"x_percent": 50.0, "y_percent": 64.0, "radius_percent": 7.0}, "audio_text": "हरे लोकेशन बटन को छुएं।", "screen_type": "whatsapp_attachment_menu", "reassurance": "नक्शा खुलेगा।"},
                    {"step_number": 4, "title": "4. 'Send your current location' दबाएं", "instruction": "'अपना वर्तमान स्थान भेजें' पर टैप करें। लोकेशन सुरक्षित पहुंच गया!", "target_ui_element": "लोकेशन भेजें", "target_coordinates": {"x_percent": 50.0, "y_percent": 48.0, "radius_percent": 8.0}, "audio_text": "लोकेशन भेजें पर टैप करें। पता पहुंच गया!", "screen_type": "maps_directions_screen", "reassurance": "स्थान सफलतापूर्वक चला गया।"}
                ]
            },
            "en": {
                "title": "Share Live Location on WhatsApp",
                "summary": "Show your family exactly where you are on the map safely.",
                "reassurance_banner": "Don't worry, only the family member you choose can see your location.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. Open Family Member's Chat", "instruction": "Tap the name of the person you want to send your location to.", "target_ui_element": "Contact Chat Name", "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5}, "audio_text": "Open the chat of the person.", "screen_type": "whatsapp_chat_list", "reassurance": "Opens chat."},
                    {"step_number": 2, "title": "2. Tap Paperclip Icon", "instruction": "Tap the small paperclip 📎 icon next to the typing area at the bottom.", "target_ui_element": "📎 Paperclip Icon", "target_coordinates": {"x_percent": 70.8, "y_percent": 94.5, "radius_percent": 5.5}, "audio_text": "Tap the paperclip icon.", "screen_type": "whatsapp_chat_screen", "reassurance": "Opens attachment options."},
                    {"step_number": 3, "title": "3. Tap 'Location' Button", "instruction": "From the popup menu, tap the green circular 'Location' 📍 button.", "target_ui_element": "📍 Green Location Button", "target_coordinates": {"x_percent": 50.0, "y_percent": 64.0, "radius_percent": 7.0}, "audio_text": "Tap the green location button.", "screen_type": "whatsapp_attachment_menu", "reassurance": "Opens GPS map."},
                    {"step_number": 4, "title": "4. Tap 'Send Your Current Location'", "instruction": "Tap 'Send your current location'. Your family can now see where you are!", "target_ui_element": "Send Current Location", "target_coordinates": {"x_percent": 50.0, "y_percent": 48.0, "radius_percent": 8.0}, "audio_text": "Tap send location. Delivered safely!", "screen_type": "maps_directions_screen", "reassurance": "Location shared safely."}
                ]
            }
        }
    },
    "block_unknown_number": {
        "app_name": "Phone",
        "intent": "block_phone_number",
        "keywords": ["block", "spam", "unknown", "બ્લોક", "અજાણ્યા", "ફ્રોડ", "ખોટા કોલ", "ब्लॉक", "अनजान", "फ्रॉड"],
        "flows": {
            "gu": {
                "title": "અજાણ્યા કે ફ્રોડ નંબર બ્લોક કરો",
                "summary": "અજાણ્યા કે હેરાન કરતા ફોન નંબરને હંમેશ માટે બંધ (બ્લોક) કરો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, આ નંબર પરથી તમને ફરી ક્યારેય ફોન કે મેસેજ નહીં આવે.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. ફોનની કોલિંગ એપ 📞 ખોલો", "instruction": "જ્યાંથી તમે ફોન કરો છો તે ફોન ડાયલર એપ ખોલો.", "target_ui_element": "📞 ફોન એપ", "target_coordinates": {"x_percent": 20.0, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "સૌપ્રથમ ફોન ડાયલર ખોલો.", "screen_type": "whatsapp_phone_home", "reassurance": "કોલિંગ સ્ક્રીન ખુલશે."},
                    {"step_number": 2, "title": "2. 'Recents' (છેલ્લા કોલ) પર ટચ કરો", "instruction": "વચ્ચે આપેલા 'Recents' (કોલ હિસ્ટ્રી) ના લિસ્ટ પર ટચ કરો.", "target_ui_element": "છેલ્લા કોલ ટેબ", "target_coordinates": {"x_percent": 50.0, "y_percent": 13.0, "radius_percent": 7.0}, "audio_text": "છેલ્લા આવેલા કોલના લિસ્ટ પર ટચ કરો.", "screen_type": "phone_recents_screen", "reassurance": "કોલ લિસ્ટ દેખાશે."},
                    {"step_number": 3, "title": "3. અજાણ્યા નંબર પાસે (i) નિશાન પર ટચ કરો", "instruction": "જે અજાણ્યા નંબરને બ્લોક કરવો હોય તેની જમણી બાજુ માહિતી ℹ️ ના નિશાન પર ટચ કરો.", "target_ui_element": "ℹ️ માહિતી આઇકન", "target_coordinates": {"x_percent": 88.7, "y_percent": 33.6, "radius_percent": 6.5}, "audio_text": "અજાણ્યા નંબર પાસે માહિતીના નિશાન પર અડો.", "screen_type": "phone_recents_screen", "reassurance": "નંબરની વિગત ખુલશે."},
                    {"step_number": 4, "title": "4. નીચે લાલ 'Block' (બ્લોક) બટન પર ટચ કરો", "instruction": "નીચે આપેલા લાલ રંગના '🚫 નંબર બ્લોક કરો' પર ટચ કરો. નંબર કાયમ માટે બંધ થઈ ગયો!", "target_ui_element": "🚫 બ્લોક નંબર બટન", "target_coordinates": {"x_percent": 50.0, "y_percent": 78.0, "radius_percent": 8.0}, "audio_text": "નીચે લાલ બ્લોક બટન પર અડો. હવે ક્યારેય ફોન નહીં આવે!", "screen_type": "phone_recents_screen", "reassurance": "નંબર સફળતાપૂર્વક બ્લોક થઈ ગયો છે."}
                ]
            },
            "hi": {
                "title": "अनजान या फ्रॉड नंबर ब्लॉक करें",
                "summary": "परेशान करने वाले किसी भी नंबर को हमेशा के लिए ब्लॉक करें।",
                "reassurance_banner": "चिंता मत कीजिए, इस नंबर से आपको दोबारा कभी कॉल या मैसेज नहीं आएगा।",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. फोन कॉलिंग ऐप 📞 खोलें", "instruction": "फोन स्क्रीन पर कॉलिंग वाली फोन ऐप खोलें।", "target_ui_element": "📞 फोन ऐप", "target_coordinates": {"x_percent": 20.0, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "फोन कॉलिंग ऐप खोलें।", "screen_type": "whatsapp_phone_home", "reassurance": "कॉल स्क्रीन खुलेगी।"},
                    {"step_number": 2, "title": "2. 'Recents' (हाल के कॉल) छुएं", "instruction": "स्क्रीन पर 'Recents' या हाल में आई कॉल की लिस्ट पर टैप करें।", "target_ui_element": "हाल के कॉल", "target_coordinates": {"x_percent": 50.0, "y_percent": 13.0, "radius_percent": 7.0}, "audio_text": "हाल की कॉल लिस्ट पर टैप करें।", "screen_type": "phone_recents_screen", "reassurance": "कॉल लिस्ट दिखेगी।"},
                    {"step_number": 3, "title": "3. अनजान नंबर के पास (i) निशान छुएं", "instruction": "जिस अनजान नंबर को ब्लॉक करना है उसके पास जानकारी ℹ️ के निशान को छुएं।", "target_ui_element": "ℹ️ जानकारी निशान", "target_coordinates": {"x_percent": 88.7, "y_percent": 33.6, "radius_percent": 6.5}, "audio_text": "अनजान नंबर के पास जानकारी निशान को छुएं।", "screen_type": "phone_recents_screen", "reassurance": "नंबर की डिटेल खुलेगी।"},
                    {"step_number": 4, "title": "4. नीचे लाल 'Block' बटन दबाएं", "instruction": "नीचे दिए गए लाल रंग के '🚫 ब्लॉक करें' बटन को दबाएं। नंबर हमेशा के लिए बंद हो गया!", "target_ui_element": "🚫 ब्लॉक बटन", "target_coordinates": {"x_percent": 50.0, "y_percent": 78.0, "radius_percent": 8.0}, "audio_text": "नीचे लाल ब्लॉक बटन दबाएं। अब कभी कॉल नहीं आएगी!", "screen_type": "phone_recents_screen", "reassurance": "नंबर सफलतापूर्वक ब्लॉक हो गया।"}
                ]
            },
            "en": {
                "title": "Block Spam or Unknown Phone Numbers",
                "summary": "Permanently block unknown or scam callers from calling your phone.",
                "reassurance_banner": "Don't worry, this caller will never be able to ring your phone again.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. Open Phone App 📞", "instruction": "Open the Phone / Dialer app on your home screen.", "target_ui_element": "Phone Call App", "target_coordinates": {"x_percent": 20.0, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "Open the Phone dialer app.", "screen_type": "whatsapp_phone_home", "reassurance": "Opens dialer safely."},
                    {"step_number": 2, "title": "2. Tap 'Recents' Tab", "instruction": "Tap 'Recents' to see your incoming call history.", "target_ui_element": "Recents Call Log", "target_coordinates": {"x_percent": 50.0, "y_percent": 13.0, "radius_percent": 7.0}, "audio_text": "Tap on your recent calls.", "screen_type": "phone_recents_screen", "reassurance": "Shows caller list."},
                    {"step_number": 3, "title": "3. Tap (i) Info Icon Next to Number", "instruction": "Tap the circular info ℹ️ icon next to the unknown or spam caller.", "target_ui_element": "ℹ️ Info Icon", "target_coordinates": {"x_percent": 88.7, "y_percent": 33.6, "radius_percent": 6.5}, "audio_text": "Tap the info icon next to the number.", "screen_type": "phone_recents_screen", "reassurance": "Opens caller options."},
                    {"step_number": 4, "title": "4. Tap 'Block' Button 🚫", "instruction": "Tap the red 'Block Number' button. They can never call you again!", "target_ui_element": "🚫 Block Button", "target_coordinates": {"x_percent": 50.0, "y_percent": 78.0, "radius_percent": 8.0}, "audio_text": "Tap the red block button. Blocked permanently!", "screen_type": "phone_recents_screen", "reassurance": "Caller blocked safely."}
                ]
            }
        }
    },
    "whatsapp_voice_message": {
        "app_name": "WhatsApp",
        "intent": "send_voice_message",
        "keywords": ["voice message", "audio message", "bolvu", "boline", "અવાજ", "વોઇસ", "બોલીને", "बोलकर", "आवाज", "ऑडियो"],
        "flows": {
            "gu": {
                "title": "વોટ્સએપ પર બોલીને અવાજનો મેસેજ મોકલો",
                "summary": "લખ્યા વગર ફક્ત બોલીને તમારો અવાજ સામેવાળાને મોકલો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, તમે જે બોલશો તે જ અવાજ સામે જશે. લખવાની જરૂર નથી.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. જેમને મેસેજ કરવો હોય તેમની ચેટ ખોલો", "instruction": "તમારા પરિવારજન કે મિત્રના નામ પર ટચ કરીને ચેટ ખોલો.", "target_ui_element": "ચેટનું નામ", "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5}, "audio_text": "જેમને બોલીને મેસેજ મોકલવો હોય તેમની ચેટ ખોલો.", "screen_type": "whatsapp_chat_list", "reassurance": "ચેટ ખુલશે."},
                    {"step_number": 2, "title": "2. નીચે લીલા માઇક 🎙️ ના નિશાનને દબાવી રાખો", "instruction": "નીચે જમણી બાજુ આપેલા લીલા રંગના માઇક્રોફોન 🎙️ બટન પર આંગળી દબાવી રાખો.", "target_ui_element": "🎙️ લીલું માઇક બટન", "target_coordinates": {"x_percent": 91.0, "y_percent": 94.5, "radius_percent": 6.5}, "audio_text": "નીચે લીલા માઇક પર આંગળી દબાવી રાખો.", "screen_type": "whatsapp_chat_screen", "reassurance": "અવાજ રેકોર્ડ શરૂ થશે."},
                    {"step_number": 3, "title": "3. આંગળી દબાવી રાખીને તમારો સંદેશો બોલો", "instruction": "જેમ કે: 'કેમ છો? હું સાંજે ઘરે આવીશ.' સ્પષ્ટ અવાજમાં બોલો.", "target_ui_element": "બોલવાનું શરૂ કરો", "target_coordinates": {"x_percent": 50.0, "y_percent": 94.5, "radius_percent": 7.0}, "audio_text": "આંગળી દબાવી રાખીને તમારો મેસેજ બોલો.", "screen_type": "whatsapp_chat_screen", "reassurance": "અવાજ રેકોર્ડ થઈ રહ્યો છે."},
                    {"step_number": 4, "title": "4. બોલી રહ્યા પછી આંગળી છોડી દો", "instruction": "જેવી તમે આંગળી હટાવશો, તમારો અવાજ સામેવાળાને તરત જ પહોંચી જશે!", "target_ui_element": "આંગળી છોડો - સેન્ડ", "target_coordinates": {"x_percent": 91.0, "y_percent": 94.5, "radius_percent": 6.5}, "audio_text": "બોલ્યા પછી આંગળી હટાવો. અવાજનો મેસેજ પહોંચી ગયો!", "screen_type": "whatsapp_chat_screen", "reassurance": "વોઇસ મેસેજ પહોંચી ગયો છે."}
                ]
            },
            "hi": {
                "title": "WhatsApp पर बोलकर वॉयस मैसेज भेजें",
                "summary": "टाइप किए बिना केवल बोलकर अपनी आवाज में मैसेज भेजें।",
                "reassurance_banner": "चिंता मत कीजिए, जो आप बोलेंगे वही आवाज सामने पहुंचेगी।",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. जिन्हें मैसेज भेजना है उनकी चैट खोलें", "instruction": "परिवार के सदस्य के नाम पर टैप करके चैट खोलें।", "target_ui_element": "चैट नाम", "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5}, "audio_text": "चैट खोलें।", "screen_type": "whatsapp_chat_list", "reassurance": "चैट खुलेगी।"},
                    {"step_number": 2, "title": "2. नीचे हरे माइक 🎙️ को दबाए रखें", "instruction": "नीचे दाईं तरफ दिए गए हरे माइक 🎙️ के निशान पर उंगली दबाकर रखें।", "target_ui_element": "🎙️ हरा माइक", "target_coordinates": {"x_percent": 91.0, "y_percent": 94.5, "radius_percent": 6.5}, "audio_text": "माइक पर उंगली दबाकर रखें।", "screen_type": "whatsapp_chat_screen", "reassurance": "रिकॉर्डिंग शुरू होगी।"},
                    {"step_number": 3, "title": "3. उंगली दबाए रखकर अपना संदेश बोलें", "instruction": "साफ आवाज में बोलें जो भी आप कहना चाहते हैं।", "target_ui_element": "बोलना शुरू करें", "target_coordinates": {"x_percent": 50.0, "y_percent": 94.5, "radius_percent": 7.0}, "audio_text": "उंगली दबाए रखकर अपना मैसेज बोलिए।", "screen_type": "whatsapp_chat_screen", "reassurance": "आवाज रिकॉर्ड हो रही है।"},
                    {"step_number": 4, "title": "4. बोलने के बाद उंगली हटा लें", "instruction": "उंगली हटाते ही आपका वॉयस मैसेज तुरंत चला जाएगा!", "target_ui_element": "उंगली हटाएं", "target_coordinates": {"x_percent": 91.0, "y_percent": 94.5, "radius_percent": 6.5}, "audio_text": "बोलने के बाद उंगली हटाएं। मैसेज पहुंच गया!", "screen_type": "whatsapp_chat_screen", "reassurance": "सफलतापूर्वक भेज दिया गया।"}
                ]
            },
            "en": {
                "title": "Send a Voice Message on WhatsApp",
                "summary": "Speak naturally to send your voice without typing any words.",
                "reassurance_banner": "Don't worry, your exact spoken voice will safely reach your family.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. Open Contact Chat", "instruction": "Tap the name of the person you want to send your voice message to.", "target_ui_element": "Contact Chat", "target_coordinates": {"x_percent": 50.0, "y_percent": 18.2, "radius_percent": 7.5}, "audio_text": "Open the chat of the person.", "screen_type": "whatsapp_chat_list", "reassurance": "Opens conversation."},
                    {"step_number": 2, "title": "2. Press & Hold Green Mic 🎙️", "instruction": "At bottom right, press and hold the green microphone button with your finger.", "target_ui_element": "🎙️ Green Mic Button", "target_coordinates": {"x_percent": 91.0, "y_percent": 94.5, "radius_percent": 6.5}, "audio_text": "Hold the green mic button down.", "screen_type": "whatsapp_chat_screen", "reassurance": "Recording audio."},
                    {"step_number": 3, "title": "3. Speak Your Message Clearly", "instruction": "Speak your message while keeping your finger on the green button.", "target_ui_element": "Speak into phone", "target_coordinates": {"x_percent": 50.0, "y_percent": 94.5, "radius_percent": 7.0}, "audio_text": "Speak your message clearly.", "screen_type": "whatsapp_chat_screen", "reassurance": "Capturing voice."},
                    {"step_number": 4, "title": "4. Release Finger to Send", "instruction": "Release your finger from the screen. Your voice message is sent immediately!", "target_ui_element": "Release to Send", "target_coordinates": {"x_percent": 91.0, "y_percent": 94.5, "radius_percent": 6.5}, "audio_text": "Release your finger. Voice message sent!", "screen_type": "whatsapp_chat_screen", "reassurance": "Delivered safely."}
                ]
            }
        }
    },
    "google_maps_navigate_home": {
        "app_name": "Google Maps",
        "intent": "navigate_home",
        "keywords": ["maps", "home", "rasto", "directions", "ઘર", "મેપ્સ", "રસ્તો", "નકશો", "घर", "रास्ता", "नक्शा"],
        "flows": {
            "gu": {
                "title": "ગૂગલ મેપ્સ પર ઘરનો રસ્તો જુઓ",
                "summary": "તમે જ્યાં પણ હોવ ત્યાંથી તમારા ઘર સુધીનો સરળ રસ્તો જુઓ.",
                "reassurance_banner": "ગૂગલ મેપ્સ તમને બોલીને જણાવશે કે ક્યાંથી ડાબે કે જમણે વળવું.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. ગૂગલ મેપ્સ (Google Maps) 🗺️ ખોલો", "instruction": "તમારા ફોનમાં નકશાવાળી Google Maps એપ પર ટચ કરો.", "target_ui_element": "Google Maps એપ", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 9.0}, "audio_text": "ગૂગલ મેપ્સ એપ ખોલો.", "screen_type": "whatsapp_phone_home", "reassurance": "નકશો ખુલશે."},
                    {"step_number": 2, "title": "2. ઉપર સર્ચમાં 'ઘર' (Home) લખો", "instruction": "ઉપર સર્ચમાં 'Home' લખો અથવા ઘર 🏠 ના નિશાન પર ટચ કરો.", "target_ui_element": "🏠 ઘર શૉર્ટકટ", "target_coordinates": {"x_percent": 65.0, "y_percent": 28.0, "radius_percent": 8.0}, "audio_text": "ઘરના નિશાન પર ટચ કરો.", "screen_type": "maps_directions_screen", "reassurance": "રસ્તો દેખાશે."},
                    {"step_number": 3, "title": "3. વાદળી 'Start' (શરૂ કરો) પર ટચ કરો", "instruction": "નીચે જમણી બાજુ વાદળી રંગના 'Start' ↗️ બટન પર ટચ કરો. ફોન બોલીને રસ્તો બતાવશે!", "target_ui_element": "Start ↗️ બટન", "target_coordinates": {"x_percent": 68.0, "y_percent": 92.5, "radius_percent": 8.0}, "audio_text": "વાદળી સ્ટાર્ટ બટન પર અડો. ફોન બોલીને રસ્તો બતાવશે!", "screen_type": "maps_directions_screen", "reassurance": "નેવિગેશન શરૂ થઈ ગયું છે."}
                ]
            },
            "hi": {
                "title": "Google Maps पर घर का रास्ता देखें",
                "summary": "आप कहीं भी हों, वहां से घर तक का सीधा रास्ता देखें।",
                "reassurance_banner": "गूगल मैप्स बोलकर बताएगा कि कहां से मुड़ना है।",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Google Maps 🗺️ ऐप खोलें", "instruction": "फोन में गूगल मैप्स ऐप पर टैप करें।", "target_ui_element": "Maps ऐप", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 9.0}, "audio_text": "गूगल मैप्स खोलें।", "screen_type": "whatsapp_phone_home", "reassurance": "नक्शा खुलेगा।"},
                    {"step_number": 2, "title": "2. ऊपर 'Home' (घर) चुनें", "instruction": "ऊपर सर्च में घर 🏠 के निशान को छुएं।", "target_ui_element": "🏠 घर का निशान", "target_coordinates": {"x_percent": 65.0, "y_percent": 28.0, "radius_percent": 8.0}, "audio_text": "घर के निशान को छुएं।", "screen_type": "maps_directions_screen", "reassurance": "रास्ता दिखेगा।"},
                    {"step_number": 3, "title": "3. नीले 'Start' बटन को दबाएं", "instruction": "नीचे दिए गए नीले 'Start' ↗️ बटन को दबाएं। फोन बोलकर रास्ता दिखाएगा!", "target_ui_element": "नीला Start बटन", "target_coordinates": {"x_percent": 68.0, "y_percent": 92.5, "radius_percent": 8.0}, "audio_text": "नीले स्टार्ट बटन को दबाएं। रास्ता शुरू हो गया!", "screen_type": "maps_directions_screen", "reassurance": "नेविगेशन शुरू हो गया।"}
                ]
            },
            "en": {
                "title": "Navigate Home on Google Maps",
                "summary": "Find the fastest route home with voice directions from wherever you are.",
                "reassurance_banner": "Google Maps will speak aloud when to turn left or right.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Open Google Maps 🗺️", "instruction": "Tap the Google Maps app icon on your home screen.", "target_ui_element": "Google Maps Icon", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 9.0}, "audio_text": "Open Google Maps on your phone.", "screen_type": "whatsapp_phone_home", "reassurance": "Opens map safely."},
                    {"step_number": 2, "title": "2. Select 'Home' 🏠 Shortcut", "instruction": "Tap the Home 🏠 shortcut pin at the top.", "target_ui_element": "🏠 Home Shortcut", "target_coordinates": {"x_percent": 65.0, "y_percent": 28.0, "radius_percent": 8.0}, "audio_text": "Tap the Home pin.", "screen_type": "maps_directions_screen", "reassurance": "Finds route."},
                    {"step_number": 3, "title": "3. Tap Blue 'Start' ↗️ Button", "instruction": "Tap the blue 'Start' button at bottom right. Spoken driving/walking directions will guide you!", "target_ui_element": "Start Button", "target_coordinates": {"x_percent": 68.0, "y_percent": 92.5, "radius_percent": 8.0}, "audio_text": "Tap the blue start button. Spoken navigation started!", "screen_type": "maps_directions_screen", "reassurance": "Navigation active."}
                ]
            }
        }
    },
    "set_phone_alarm": {
        "app_name": "Clock",
        "intent": "set_alarm",
        "keywords": ["alarm", "clock", "wake up", "savare", "એલાર્મ", "ઘડિયાળ", "જાગવું", "अलार्म", "घड़ी", "सुबह"],
        "flows": {
            "gu": {
                "title": "ફોનમાં સવારનો એલાર્મ સેટ કરો",
                "summary": "સવારે સમયસર જાગવા માટે ઘડિયાળમાં એલાર્મ મૂકો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, એલાર્મ વાગશે એટલે સુંદર ભક્તિ ધૂન વાગશે.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. ઘડિયાળ (Clock) ⏰ એપ ખોલો", "instruction": "તમારા ફોનમાં ગોળ ઘડિયાળ જેવી 'Clock' એપ શોધીને ટચ કરો.", "target_ui_element": "⏰ Clock એપ", "target_coordinates": {"x_percent": 35.0, "y_percent": 50.0, "radius_percent": 8.0}, "audio_text": "ફોનમાં ઘડિયાળ એપ ખોલો.", "screen_type": "whatsapp_phone_home", "reassurance": "ઘડિયાળ ખુલશે."},
                    {"step_number": 2, "title": "2. સવારનો સમય (દા.ત. 06:00 AM) પસંદ કરો", "instruction": "જે સમયે જાગવું હોય તે સમય સેટ કરો અને 'AM' પસંદ કરો.", "target_ui_element": "સમય પસંદગી", "target_coordinates": {"x_percent": 50.0, "y_percent": 24.0, "radius_percent": 9.0}, "audio_text": "જે સમયે જાગવું હોય તે સમય સેટ કરો.", "screen_type": "clock_alarm_screen", "reassurance": "સમય પસંદ થઈ ગયો."},
                    {"step_number": 3, "title": "3. નીચે લીલા 'Save' (સેવ કરો) પર ટચ કરો", "instruction": "નીચે આપેલા 'એલાર્મ સેવ કરો' બટન પર ટચ કરો. એલાર્મ સફળતાપૂર્વક મુકાઈ ગયું!", "target_ui_element": "💾 એલાર્મ સેવ કરો", "target_coordinates": {"x_percent": 50.0, "y_percent": 88.5, "radius_percent": 8.0}, "audio_text": "સેવ બટન પર અડો. એલાર્મ મુકાઈ ગયું છે!", "screen_type": "clock_alarm_screen", "reassurance": "એલાર્મ સેટ થઈ ગયું છે."}
                ]
            },
            "hi": {
                "title": "फोन में सुबह का अलार्म लगाएं",
                "summary": "सुबह समय पर जागने के लिए घड़ी में अलार्म सेट करें।",
                "reassurance_banner": "चिंता मत कीजिए, सही समय पर मीठी धुन बजेगी।",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. घड़ी (Clock) ⏰ ऐप खोलें", "instruction": "फोन स्क्रीन पर Clock ऐप पर टैप करें।", "target_ui_element": "⏰ Clock ऐप", "target_coordinates": {"x_percent": 35.0, "y_percent": 50.0, "radius_percent": 8.0}, "audio_text": "घड़ी ऐप खोलें।", "screen_type": "whatsapp_phone_home", "reassurance": "घड़ी खुलेगी।"},
                    {"step_number": 2, "title": "2. सुबह का समय (उदा. 06:00 AM) चुनें", "instruction": "जितने बजे जागना हो वह समय चुनें और AM दबाएं।", "target_ui_element": "समय चुनें", "target_coordinates": {"x_percent": 50.0, "y_percent": 24.0, "radius_percent": 9.0}, "audio_text": "जागने का समय सेट करें।", "screen_type": "clock_alarm_screen", "reassurance": "समय चुना गया।"},
                    {"step_number": 3, "title": "3. नीचे 'Save Alarm' दबाएं", "instruction": "नीचे दिए गए हरे 'Save' बटन को दबाएं। अलार्म लग गया!", "target_ui_element": "💾 सेव अलार्म", "target_coordinates": {"x_percent": 50.0, "y_percent": 88.5, "radius_percent": 8.0}, "audio_text": "सेव बटन दबाएं। अलार्म लग चुका है!", "screen_type": "clock_alarm_screen", "reassurance": "अलार्म सफलता से सेट हुआ।"}
                ]
            },
            "en": {
                "title": "Set a Morning Alarm on Phone",
                "summary": "Set an alarm on your phone to wake up on time with peaceful morning chimes.",
                "reassurance_banner": "Don't worry, your phone will ring clearly at the exact time you set.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Open Clock ⏰ App", "instruction": "Find the Clock app on your home screen and tap it.", "target_ui_element": "Clock App Icon", "target_coordinates": {"x_percent": 35.0, "y_percent": 50.0, "radius_percent": 8.0}, "audio_text": "Open the Clock app.", "screen_type": "whatsapp_phone_home", "reassurance": "Opens clock safely."},
                    {"step_number": 2, "title": "2. Pick Wake-up Time", "instruction": "Set the hour and minute (e.g. 06:00) and tap AM for morning.", "target_ui_element": "Time Picker", "target_coordinates": {"x_percent": 50.0, "y_percent": 24.0, "radius_percent": 9.0}, "audio_text": "Set your wake-up time.", "screen_type": "clock_alarm_screen", "reassurance": "Time selected."},
                    {"step_number": 3, "title": "3. Tap 'Save Alarm' 💾", "instruction": "Tap the green 'Save Alarm' button at the bottom. Your alarm is now active!", "target_ui_element": "Save Alarm Button", "target_coordinates": {"x_percent": 50.0, "y_percent": 88.5, "radius_percent": 8.0}, "audio_text": "Tap save alarm. Alarm is set!", "screen_type": "clock_alarm_screen", "reassurance": "Alarm saved safely."}
                ]
            }
        }
    },
    "whatsapp_exit_group": {
        "app_name": "WhatsApp",
        "intent": "exit_whatsapp_group",
        "keywords": ["exit group", "leave group", "group", "ગ્રુપ", "બહાર", "લીવ", "ग्रुप", "बाहर निकलें", "छोड़ें"],
        "flows": {
            "gu": {
                "title": "વોટ્સએપ ગ્રુપમાંથી બહાર નીકળો",
                "summary": "જે ગ્રુપમાંથી વધુ પડતા મેસેજ આવતા હોય તેમાંથી શાંતિથી બહાર નીકળો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, તમારા વ્યક્તિગત મેસેજ કે ફોટા સુરક્ષિત રહેશે.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. જે ગ્રુપ છોડવું હોય તે ખોલો", "instruction": "જે WhatsApp ગ્રુપમાંથી બહાર નીકળવું હોય તેના પર ટચ કરો.", "target_ui_element": "ગ્રુપ ચેટ", "target_coordinates": {"x_percent": 50.0, "y_percent": 25.0, "radius_percent": 7.5}, "audio_text": "જે ગ્રુપ છોડવું હોય તે ખોલો.", "screen_type": "whatsapp_chat_list", "reassurance": "ગ્રુપ ખુલશે."},
                    {"step_number": 2, "title": "2. ઉપર જમણી બાજુ ત્રણ ટપકાં ⋮ પર ટચ કરો", "instruction": "સૌથી ઉપર જમણી બાજુ આપેલા ત્રણ નાના ટપકાં ⋮ પર ટચ કરો.", "target_ui_element": "⋮ મેનૂ બટન", "target_coordinates": {"x_percent": 93.0, "y_percent": 4.5, "radius_percent": 5.5}, "audio_text": "ઉપર ત્રણ ટપકાં પર અડો.", "screen_type": "whatsapp_chat_screen", "reassurance": "મેનૂ ખુલશે."},
                    {"step_number": 3, "title": "3. 'More' $\rightarrow$ 'Exit group' પર ટચ કરો", "instruction": "મેનૂમાં નીચે 'More' પર અડી 'Exit group' (ગ્રુપમાંથી બહાર નીકળો) પર ટચ કરો.", "target_ui_element": "Exit group વિકલ્પ", "target_coordinates": {"x_percent": 75.0, "y_percent": 55.0, "radius_percent": 7.0}, "audio_text": "એક્ઝિટ ગ્રુપ પર ટચ કરો.", "screen_type": "whatsapp_attachment_menu", "reassurance": "ખાતરી પૂછશે."},
                    {"step_number": 4, "title": "4. લાલ 'Exit' બટન પર ટચ કરો", "instruction": "તમે સફળતાપૂર્વક ગ્રુપમાંથી બહાર નીકળી ગયા છો. હવે તેના મેસેજ નહીં આવે!", "target_ui_element": "Exit કન્ફર્મ", "target_coordinates": {"x_percent": 75.0, "y_percent": 65.0, "radius_percent": 7.0}, "audio_text": "એક્ઝિટ પર અડો. તમે ગ્રુપમાંથી બહાર નીકળી ગયા છો!", "screen_type": "whatsapp_attachment_menu", "reassurance": "ગ્રુપ સફળતાપૂર્વક છોડી દીધું."}
                ]
            },
            "hi": {
                "title": "WhatsApp ग्रुप से बाहर निकलें",
                "summary": "जिस ग्रुप से बहुत मैसेज आते हों, उसे आसानी से छोड़ें।",
                "reassurance_banner": "चिंता मत कीजिए, आपके बाकी मैसेज सुरक्षित रहेंगे।",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. जो ग्रुप छोड़ना है उसे खोलें", "instruction": "उस व्हाट्सएप ग्रुप पर टैप करें जिससे बाहर निकलना है।", "target_ui_element": "ग्रुप चैट", "target_coordinates": {"x_percent": 50.0, "y_percent": 25.0, "radius_percent": 7.5}, "audio_text": "ग्रुप चैट खोलें।", "screen_type": "whatsapp_chat_list", "reassurance": "ग्रुप खुलेगा।"},
                    {"step_number": 2, "title": "2. ऊपर तीन बिंदियों ⋮ पर टैप करें", "instruction": "ऊपर दाईं तरफ दी गई तीन बिंदियों ⋮ को छुएं।", "target_ui_element": "⋮ मेनू", "target_coordinates": {"x_percent": 93.0, "y_percent": 4.5, "radius_percent": 5.5}, "audio_text": "तीन बिंदियों पर टैप करें।", "screen_type": "whatsapp_chat_screen", "reassurance": "मेनू खुलेगा।"},
                    {"step_number": 3, "title": "3. 'More' $\rightarrow$ 'Exit group' चुनें", "instruction": "मेनू में 'More' दबाकर 'Exit group' (ग्रुप छोड़ें) पर टैप करें।", "target_ui_element": "Exit group", "target_coordinates": {"x_percent": 75.0, "y_percent": 55.0, "radius_percent": 7.0}, "audio_text": "एग्जिट ग्रुप चुनें।", "screen_type": "whatsapp_attachment_menu", "reassurance": "पुष्टि पूछेगा।"},
                    {"step_number": 4, "title": "4. लाल 'Exit' बटन दबाएं", "instruction": "अब आप ग्रुप से बाहर आ चुके हैं। इसके मैसेज अब आपको परेशान नहीं करेंगे!", "target_ui_element": "Exit पुष्टि", "target_coordinates": {"x_percent": 75.0, "y_percent": 65.0, "radius_percent": 7.0}, "audio_text": "एग्जिट दबाएं। आप ग्रुप से बाहर निकल चुके हैं!", "screen_type": "whatsapp_attachment_menu", "reassurance": "ग्रुप से हट गए।"}
                ]
            },
            "en": {
                "title": "Exit a WhatsApp Group Safely",
                "summary": "Leave noisy groups that send too many messages without deleting your other chats.",
                "reassurance_banner": "Don't worry, your other conversations and pictures remain safe.",
                "total_steps": 4,
                "steps": [
                    {"step_number": 1, "title": "1. Open the WhatsApp Group", "instruction": "Tap the name of the group you want to leave.", "target_ui_element": "Group Chat", "target_coordinates": {"x_percent": 50.0, "y_percent": 25.0, "radius_percent": 7.5}, "audio_text": "Open the WhatsApp group.", "screen_type": "whatsapp_chat_list", "reassurance": "Opens group."},
                    {"step_number": 2, "title": "2. Tap 3 Dots ⋮ Top Right", "instruction": "At top right, tap the three vertical dots ⋮ menu.", "target_ui_element": "⋮ Three Dots Menu", "target_coordinates": {"x_percent": 93.0, "y_percent": 4.5, "radius_percent": 5.5}, "audio_text": "Tap the 3 dots menu at top right.", "screen_type": "whatsapp_chat_screen", "reassurance": "Opens options."},
                    {"step_number": 3, "title": "3. Tap 'More' $\rightarrow$ 'Exit group'", "instruction": "Tap 'More' and then tap 'Exit group'.", "target_ui_element": "Exit Group Option", "target_coordinates": {"x_percent": 75.0, "y_percent": 55.0, "radius_percent": 7.0}, "audio_text": "Tap Exit group.", "screen_type": "whatsapp_attachment_menu", "reassurance": "Asks confirmation."},
                    {"step_number": 4, "title": "4. Confirm by Tapping 'Exit'", "instruction": "Tap 'Exit' to confirm. You have safely left the group!", "target_ui_element": "Confirm Exit", "target_coordinates": {"x_percent": 75.0, "y_percent": 65.0, "radius_percent": 7.0}, "audio_text": "Tap exit. You have safely left the group!", "screen_type": "whatsapp_attachment_menu", "reassurance": "Group left safely."}
                ]
            }
        }
    },
    "increase_call_volume": {
        "app_name": "Settings",
        "intent": "increase_volume",
        "keywords": ["volume", "sound", "ringtone", "avaj", "અવાજ", "વોલ્યુમ", "રીંગટોન", "સાંભળવું", "आवाज", "वॉल्यूम", "रिंगटोन"],
        "flows": {
            "gu": {
                "title": "ફોનમાં રીંગટોન અને અવાજ મોટો કરો",
                "summary": "ફોન આવે ત્યારે રીંગટોન જોરથી સંભળાય તે માટે અવાજ ફૂલ (100%) કરો.",
                "reassurance_banner": "આનાથી ફોન આવશે ત્યારે સ્પષ્ટ અને જોરથી અવાજ આવશે.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. ફોનની બાજુનું ઉપરનું બટન દબાવો", "instruction": "તમારા ફોનની જમણી કે ડાબી બાજુ આપેલું અવાજ વધારવાનું ઉપરનું બટન એક વાર દબાવો.", "target_ui_element": "વોલ્યુમ બટન", "target_coordinates": {"x_percent": 98.0, "y_percent": 30.0, "radius_percent": 7.0}, "audio_text": "ફોનની બાજુમાં આપેલું અવાજ વધારવાનું બટન દબાવો.", "screen_type": "settings_home", "reassurance": "અવાજની પટ્ટી દેખાશે."},
                    {"step_number": 2, "title": "2. સ્ક્રીન પર આવેલા ત્રણ ટપકાં ... પર ટચ કરો", "instruction": "વોલ્યુમ પટ્ટી પાસે ત્રણ નાના ટપકાં પર ટચ કરો જેથી બધા અવાજના વિકલ્પો ખુલે.", "target_ui_element": "વોલ્યુમ ત્રણ ટપકાં", "target_coordinates": {"x_percent": 50.0, "y_percent": 20.0, "radius_percent": 6.5}, "audio_text": "વોલ્યુમ પટ્ટી પાસે ત્રણ ટપકાં પર અડો.", "screen_type": "settings_home", "reassurance": "રીંગટોન વિકલ્પ ખુલશે."},
                    {"step_number": 3, "title": "3. રીંગટોન 🔔 ની પટ્ટીને છેક ઉપર સુધી ખેંચો", "instruction": "રીંગટોન વાળી પટ્ટીને છેક ઉપર (100%) સુધી ખેંચો. અવાજ પૂરેપૂરો મોટો થઈ ગયો!", "target_ui_element": "રીંગટોન સ્લાઇડર", "target_coordinates": {"x_percent": 75.0, "y_percent": 40.0, "radius_percent": 8.0}, "audio_text": "રીંગટોનની પટ્ટીને છેક ઉપર સુધી ખેંચો. અવાજ મોટો થઈ ગયો!", "screen_type": "settings_home", "reassurance": "અવાજ સંપૂર્ણ મોટો થઈ ગયો છે."}
                ]
            },
            "hi": {
                "title": "फोन में रिंगटोन और आवाज तेज करें",
                "summary": "फोन आने पर रिंगटोन जोर से सुनाई दे, इसके लिए वॉल्यूम फुल करें।",
                "reassurance_banner": "अब फोन आने पर आपको साफ और तेज आवाज सुनाई देगी।",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. फोन के साइड वाला ऊपर का बटन दबाएं", "instruction": "फोन के किनारे पर आवाज बढ़ाने वाले ऊपर के बटन को दबाएं।", "target_ui_element": "वॉल्यूम बटन", "target_coordinates": {"x_percent": 98.0, "y_percent": 30.0, "radius_percent": 7.0}, "audio_text": "फोन की साइड वाला वॉल्यूम बटन दबाएं।", "screen_type": "settings_home", "reassurance": "वॉल्यूम स्लाइडर दिखेगा।"},
                    {"step_number": 2, "title": "2. स्क्रीन पर तीन बिंदियों ... को छुएं", "instruction": "वॉल्यूम पट्टी के पास तीन बिंदियों को छुएं ताकि सभी आवाज खुल जाएं।", "target_ui_element": "तीन बिंदियां", "target_coordinates": {"x_percent": 50.0, "y_percent": 20.0, "radius_percent": 6.5}, "audio_text": "तीन बिंदियों पर टैप करें।", "screen_type": "settings_home", "reassurance": "रिंगटोन विकल्प खुलेगा।"},
                    {"step_number": 3, "title": "3. रिंगटोन 🔔 की पट्टी को पूरा ऊपर खींचें", "instruction": "रिंगटोन वाली पट्टी को 100% ऊपर खींचें। आवाज पूरी तेज हो गई!", "target_ui_element": "रिंगटोन स्लाइडर", "target_coordinates": {"x_percent": 75.0, "y_percent": 40.0, "radius_percent": 8.0}, "audio_text": "रिंगटोन की पट्टी को पूरा ऊपर करें। आवाज तेज हो गई!", "screen_type": "settings_home", "reassurance": "आवाज फुल हो गई।"}
                ]
            },
            "en": {
                "title": "Increase Ringtone and Call Volume",
                "summary": "Make your incoming ringtones loud and clear so you never miss a family call.",
                "reassurance_banner": "Your phone will now ring loudly and clearly for all calls.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Press Volume Up on Phone Side", "instruction": "Press the top physical volume button on the side of your phone.", "target_ui_element": "Volume Button", "target_coordinates": {"x_percent": 98.0, "y_percent": 30.0, "radius_percent": 7.0}, "audio_text": "Press the volume up button on the side of your phone.", "screen_type": "settings_home", "reassurance": "Shows volume slider."},
                    {"step_number": 2, "title": "2. Tap 3 Dots on Slider", "instruction": "Tap the three dots on the on-screen volume bar to expand all volume sliders.", "target_ui_element": "Three Dots Option", "target_coordinates": {"x_percent": 50.0, "y_percent": 20.0, "radius_percent": 6.5}, "audio_text": "Tap the 3 dots on the slider.", "screen_type": "settings_home", "reassurance": "Opens sound channels."},
                    {"step_number": 3, "title": "3. Slide Ringtone 🔔 to 100%", "instruction": "Drag the Ringtone slider all the way up to maximum volume.", "target_ui_element": "Ringtone Slider", "target_coordinates": {"x_percent": 75.0, "y_percent": 40.0, "radius_percent": 8.0}, "audio_text": "Drag the ringtone slider to maximum volume. Done!", "screen_type": "settings_home", "reassurance": "Volume maximized safely."}
                ]
            }
        }
    },
    "toggle_mobile_data": {
        "app_name": "Quick Settings",
        "intent": "toggle_mobile_data",
        "keywords": ["data", "internet", "wifi", "net", "ઇન્ટરનેટ", "ડેટા", "વાઇફાઇ", "નેટ", "इंटरनेट", "डाटा", "वाईफाई"],
        "flows": {
            "gu": {
                "title": "મોબાઈલ ડેટા (ઇન્ટરનેટ) ચાલુ અથવા બંધ કરો",
                "summary": "ફોનમાં નેટ ચાલુ કરો અથવા ડેટા બચાવવા માટે બંધ કરો.",
                "reassurance_banner": "ઇન્ટરનેટ ચાલુ કરવાથી વોટ્સએપ મેસેજ અને ફોટો આવવાના શરૂ થશે.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. સ્ક્રીનની સૌથી ઉપરથી નીચે તરફ આંગળી ખેંચો", "instruction": "તમારા ફોનની સ્ક્રીન પર સૌથી ઉપરથી નીચે તરફ આંગળી સરકાવો (સ્વાઇપ ડાઉન કરો).", "target_ui_element": "ઉપરથી નીચે સ્વાઇપ", "target_coordinates": {"x_percent": 50.0, "y_percent": 2.0, "radius_percent": 8.0}, "audio_text": "સ્ક્રીનની ઉપરથી નીચે આંગળી ખેંચો.", "screen_type": "whatsapp_phone_home", "reassurance": "કંટ્રોલ પેનલ ખુલશે."},
                    {"step_number": 2, "title": "2. 'Mobile Data' 📶 ના નિશાન પર ટચ કરો", "instruction": "ગોળ તીર અથવા ટાવર જેવા 'Mobile Data' ના નિશાન પર એક વાર ટચ કરો.", "target_ui_element": "📶 મોબાઇલ ડેટા બટન", "target_coordinates": {"x_percent": 35.0, "y_percent": 18.0, "radius_percent": 8.0}, "audio_text": "મોબાઇલ ડેટાના નિશાન પર એક વાર અડો.", "screen_type": "whatsapp_phone_home", "reassurance": "ડેટા સ્વિચ થશે."},
                    {"step_number": 3, "title": "3. નિશાન લીલું/વાદળી થઈ જાય એટલે નેટ ચાલુ!", "instruction": "નિશાનમાં રંગ આવી જશે એટલે તમારું ઇન્ટરનેટ સફળતાપૂર્વક ચાલુ થઈ ગયું છે.", "target_ui_element": "ઇન્ટરનેટ ચાલુ", "target_coordinates": {"x_percent": 35.0, "y_percent": 18.0, "radius_percent": 8.0}, "audio_text": "નિશાનમાં રંગ આવી ગયો છે. ઇન્ટરનેટ ચાલુ થઈ ગયું!", "screen_type": "whatsapp_phone_home", "reassurance": "ઇન્ટરનેટ સક્રિય થઈ ગયું છે."}
                ]
            },
            "hi": {
                "title": "मोबाइल इंटरनेट (डाटा) चालू या बंद करें",
                "summary": "फोन में इंटरनेट चालू करें या डाटा बचाने के लिए बंद करें।",
                "reassurance_banner": "इंटरनेट चालू होने पर व्हाट्सएप मैसेज और वीडियो आने लगेंगे।",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. स्क्रीन के ऊपर से नीचे उंगली खींचें", "instruction": "फोन स्क्रीन के सबसे ऊपर से नीचे की तरफ स्वाइप करें।", "target_ui_element": "ऊपर से स्वाइप", "target_coordinates": {"x_percent": 50.0, "y_percent": 2.0, "radius_percent": 8.0}, "audio_text": "ऊपर से नीचे उंगली खींचें।", "screen_type": "whatsapp_phone_home", "reassurance": "कंट्रोल पैनल खुलेगा।"},
                    {"step_number": 2, "title": "2. 'Mobile Data' 📶 के निशान को छुएं", "instruction": "टावर जैसे 'Mobile Data' के निशान पर एक बार टैप करें।", "target_ui_element": "📶 मोबाइल डाटा", "target_coordinates": {"x_percent": 35.0, "y_percent": 18.0, "radius_percent": 8.0}, "audio_text": "मोबाइल डाटा पर टैप करें।", "screen_type": "whatsapp_phone_home", "reassurance": "डाटा स्विच होगा।"},
                    {"step_number": 3, "title": "3. निशान नीला/हरा होने पर नेट चालू!", "instruction": "निशान में रंग आते ही आपका इंटरनेट चालू हो चुका है।", "target_ui_element": "इंटरनेट चालू", "target_coordinates": {"x_percent": 35.0, "y_percent": 18.0, "radius_percent": 8.0}, "audio_text": "इंटरनेट सफलतापूर्वक चालू हो गया है!", "screen_type": "whatsapp_phone_home", "reassurance": "इंटरनेट सक्रिय हो गया।"}
                ]
            },
            "en": {
                "title": "Turn Mobile Internet (Data) On or Off",
                "summary": "Turn on internet connection to receive WhatsApp messages or turn off to save battery.",
                "reassurance_banner": "Turning mobile data on connects your phone to internet safely.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Swipe Down from Top of Screen", "instruction": "Swipe your finger down from the very top edge of your phone screen.", "target_ui_element": "Top Screen Swipe", "target_coordinates": {"x_percent": 50.0, "y_percent": 2.0, "radius_percent": 8.0}, "audio_text": "Swipe down from the top edge.", "screen_type": "whatsapp_phone_home", "reassurance": "Opens quick settings."},
                    {"step_number": 2, "title": "2. Tap 'Mobile Data' 📶 Icon", "instruction": "Tap the Mobile Data or Cellular Data icon once.", "target_ui_element": "📶 Mobile Data Icon", "target_coordinates": {"x_percent": 35.0, "y_percent": 18.0, "radius_percent": 8.0}, "audio_text": "Tap the Mobile Data icon.", "screen_type": "whatsapp_phone_home", "reassurance": "Toggles connection."},
                    {"step_number": 3, "title": "3. Icon Lights Up - Internet is Active!", "instruction": "When the icon turns blue/green, your phone is connected to the internet.", "target_ui_element": "Internet Connected", "target_coordinates": {"x_percent": 35.0, "y_percent": 18.0, "radius_percent": 8.0}, "audio_text": "Icon is lit up. Your internet is connected!", "screen_type": "whatsapp_phone_home", "reassurance": "Connected safely."}
                ]
            }
        }
    },
    "whatsapp_view_status": {
        "app_name": "WhatsApp",
        "intent": "view_whatsapp_status",
        "keywords": ["status", "story", "updates", "સ્ટેટસ", "વાર્તા", "અપડેટ્સ", "ફોટા", "स्टेटस", "अपडेट्स"],
        "flows": {
            "gu": {
                "title": "વોટ્સએપ સ્ટેટસ (ફોટા-વિડીયો) જુઓ",
                "summary": "તમારા મિત્રો અને સગા-સંબંધીઓએ મૂકેલા આજના ફોટા અને વિડીયો જુઓ.",
                "reassurance_banner": "ચિંતા કરશો નહીં, ફક્ત ફોટા પર ટચ કરવાથી સ્ટેટસ શરૂ થઈ જશે.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. વૉટ્સએપ ખોલો", "instruction": "તમારા ફોનમાં લીલા રંગના વૉટ્સએપ પર ટચ કરીને એપ ખોલો.", "target_ui_element": "વૉટ્સએપ આઇકન", "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "વૉટ્સએપ એપ ખોલો.", "screen_type": "whatsapp_phone_home", "reassurance": "વૉટ્સએપ ખુલશે."},
                    {"step_number": 2, "title": "2. 'Updates' અથવા 'Status' ટેબ પર ટચ કરો", "instruction": "ચેટની બાજુમાં આપેલા 'Updates' (સ્ટેટસ) વાળા ગોળ ચિહ્ન પર ટચ કરો.", "target_ui_element": "Updates / Status ટેબ", "target_coordinates": {"x_percent": 50.0, "y_percent": 7.0, "radius_percent": 7.5}, "audio_text": "સ્ટેટસ ટેબ પર ટચ કરો.", "screen_type": "whatsapp_chat_list", "reassurance": "સ્ટેટસ લિસ્ટ ખુલશે."},
                    {"step_number": 3, "title": "3. કોઈપણ સગાના ગોળ ફોટા પર ટચ કરો", "instruction": "જેમનો ફોટો કે વિડીયો જોવો હોય તેમના ગોળ ફોટા પર ટચ કરો. સ્ટેટસ શરૂ થઈ જશે!", "target_ui_element": "કોન્ટેક્ટનો ગોળ ફોટો", "target_coordinates": {"x_percent": 50.0, "y_percent": 22.0, "radius_percent": 8.0}, "audio_text": "જેમનો સ્ટેટસ જોવો હોય તેમના ફોટા પર ટચ કરો.", "screen_type": "whatsapp_chat_list", "reassurance": "સ્ટેટસ દેખાઈ રહ્યું છે."}
                ]
            },
            "hi": {
                "title": "WhatsApp स्टेटस (फोटो-वीडियो) देखें",
                "summary": "रिश्तेदारों और दोस्तों द्वारा डाले गए आज के स्टेटस आसानी से देखें।",
                "reassurance_banner": "चिंता मत कीजिए, फोटो पर टैप करते ही स्टेटस चलने लगेगा।",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. व्हाट्सएप खोलें", "instruction": "अपने फोन में हरे रंग का व्हाट्सएप ऐप खोलें।", "target_ui_element": "व्हाट्सएप ऐप", "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "व्हाट्सएप ऐप खोलें।", "screen_type": "whatsapp_phone_home", "reassurance": "व्हाट्सएप खुलेगा।"},
                    {"step_number": 2, "title": "2. 'Updates' या 'Status' टैब छुएं", "instruction": "चैट के पास दिए गए 'Updates' (स्टेटस) वाले टैब पर टैप करें।", "target_ui_element": "Updates टैब", "target_coordinates": {"x_percent": 50.0, "y_percent": 7.0, "radius_percent": 7.5}, "audio_text": "स्टेटस टैब को छुएं।", "screen_type": "whatsapp_chat_list", "reassurance": "स्टेटस लिस्ट दिखेगी।"},
                    {"step_number": 3, "title": "3. किसी के भी गोल फोटो पर टैप करें", "instruction": "जिनका स्टेटस देखना है उनके गोल फोटो पर टैप करें। स्टेटस शुरू हो जाएगा!", "target_ui_element": "गोल फोटो", "target_coordinates": {"x_percent": 50.0, "y_percent": 22.0, "radius_percent": 8.0}, "audio_text": "गोल फोटो पर टैप करें। स्टेटस चालू हो गया!", "screen_type": "whatsapp_chat_list", "reassurance": "स्टेटस दिखने लगा।"}
                ]
            },
            "en": {
                "title": "View WhatsApp Status & Photo Updates",
                "summary": "Watch daily photo and video status updates posted by your friends and family.",
                "reassurance_banner": "Don't worry, tapping simply plays the photo or video update safely.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Open WhatsApp", "instruction": "Tap the green WhatsApp icon on your phone screen.", "target_ui_element": "WhatsApp Icon", "target_coordinates": {"x_percent": 61.3, "y_percent": 89.6, "radius_percent": 7.5}, "audio_text": "Open WhatsApp.", "screen_type": "whatsapp_phone_home", "reassurance": "Opens WhatsApp."},
                    {"step_number": 2, "title": "2. Tap 'Updates' or 'Status' Tab", "instruction": "Tap the 'Updates' or 'Status' tab next to Chats.", "target_ui_element": "Updates / Status Tab", "target_coordinates": {"x_percent": 50.0, "y_percent": 7.0, "radius_percent": 7.5}, "audio_text": "Tap the Status or Updates tab.", "screen_type": "whatsapp_chat_list", "reassurance": "Shows contact updates."},
                    {"step_number": 3, "title": "3. Tap Any Contact's Circle Photo", "instruction": "Tap on any contact's circular photo. Their photo or video update will play!", "target_ui_element": "Contact Story Circle", "target_coordinates": {"x_percent": 50.0, "y_percent": 22.0, "radius_percent": 8.0}, "audio_text": "Tap the circle photo to watch the update.", "screen_type": "whatsapp_chat_list", "reassurance": "Playing status update."}
                ]
            }
        }
    },
    "slow_charging_clear_apps": {
        "app_name": "Device Care",
        "intent": "optimize_battery_charging",
        "keywords": ["battery", "charge", "slow", "charging", "close apps", "ચાર્જિંગ", "ચાર્જ", "બેટરી", "ધીમું", "ધીમો", "ગરમ", "चार्जिंग", "चार्ज", "बैटरी", "धीमा", "धीमी"],
        "flows": {
            "gu": {
                "title": "ફોન ચાર્જિંગમાં સ્પીડ વધારો અને એપ બંધ કરો",
                "summary": "ફોન ઝડપથી ચાર્જ થાય તે માટે બેકગ્રાઉન્ડમાં ચાલતી બધી એપ્સ બંધ કરો.",
                "reassurance_banner": "ચિંતા કરશો નહીં, આનાથી કશું જ ડિલીટ નહીં થાય. ફક્ત ખુલ્લી એપ્સ બંધ થશે.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. સ્ક્રીનની નીચે ત્રણ લીટી III વાળા બટન પર ટચ કરો", "instruction": "તમારા ફોનની નીચે આપેલા ત્રણ ઉભી લીટીઓ III અથવા ચોરસ બટન પર ટચ કરો.", "target_ui_element": "III રીસન્ટ એપ્સ બટન", "target_coordinates": {"x_percent": 25.0, "y_percent": 98.0, "radius_percent": 7.0}, "audio_text": "નીચે ત્રણ લીટી વાળા બટન પર ટચ કરો.", "screen_type": "whatsapp_phone_home", "reassurance": "ખુલ્લી એપ્સ દેખાશે."},
                    {"step_number": 2, "title": "2. 'Close all' (બધું બંધ કરો) પર ટચ કરો", "instruction": "સ્ક્રીન પર દેખાતા 'Close all' અથવા ચોકડી ❌ બટન પર ટચ કરો.", "target_ui_element": "Close All બટન", "target_coordinates": {"x_percent": 50.0, "y_percent": 85.0, "radius_percent": 8.0}, "audio_text": "ક્લોઝ ઓલ બટન પર અડો.", "screen_type": "settings_home", "reassurance": "બધી એપ્સ બંધ થઈ જશે."},
                    {"step_number": 3, "title": "3. ફોનને અસલ ચાર્જર લગાવી મૂકી રાખો", "instruction": "ફોનને ઓરિજિનલ ચાર્જર લગાવો. ચાર્જિંગ ચાલુ હોય ત્યારે ફોન ન વાપરવો જેથી ઝડપથી ચાર્જ થાય.", "target_ui_element": "ચાર્જર પિન", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 9.0}, "audio_text": "ઓરિજિનલ ચાર્જર લગાવો. ફોન ઝડપથી ચાર્જ થશે!", "screen_type": "settings_home", "reassurance": "ઝડપી ચાર્જિંગ શરૂ થઈ ગયું છે."}
                ]
            },
            "hi": {
                "title": "फोन चार्जिंग तेज करें और खुली ऐप्स बंद करें",
                "summary": "फोन तेजी से चार्ज हो इसके लिए बैकग्राउंड में चल रही सारी ऐप्स बंद करें।",
                "reassurance_banner": "चिंता मत कीजिए, इससे कुछ डिलीट नहीं होगा। केवल खुली हुई ऐप्स बंद होंगी।",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. नीचे तीन लाइनों III वाले बटन को दबाएं", "instruction": "फोन स्क्रीन के नीचे दिए गए तीन खड़ी लाइनों वाले बटन को दबाएं।", "target_ui_element": "III रीसेंट ऐप्स", "target_coordinates": {"x_percent": 25.0, "y_percent": 98.0, "radius_percent": 7.0}, "audio_text": "नीचे तीन लाइनों वाले बटन को दबाएं।", "screen_type": "whatsapp_phone_home", "reassurance": "खुली ऐप्स दिखेंगी।"},
                    {"step_number": 2, "title": "2. 'Close all' (सभी बंद करें) दबाएं", "instruction": "स्क्रीन पर 'Close all' बटन को दबाएं ताकि बैटरी खर्च होना बंद हो।", "target_ui_element": "Close all बटन", "target_coordinates": {"x_percent": 50.0, "y_percent": 85.0, "radius_percent": 8.0}, "audio_text": "क्लोज ऑल बटन दबाएं।", "screen_type": "settings_home", "reassurance": "सभी ऐप्स बंद हो जाएंगी।"},
                    {"step_number": 3, "title": "3. असली चार्जर लगाकर फोन रख दें", "instruction": "ओरिजिनल चार्जर लगाएं और चार्ज होते समय फोन न चलाएं।", "target_ui_element": "चार्जिंग", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 9.0}, "audio_text": "चार्जर लगाएं। फोन तेजी से चार्ज होगा!", "screen_type": "settings_home", "reassurance": "फास्ट चार्जिंग शुरू।"}
                ]
            },
            "en": {
                "title": "Speed Up Charging & Close Background Apps",
                "summary": "Clear memory and close all open applications to speed up phone charging and stop battery drain.",
                "reassurance_banner": "Don't worry, this will not delete anything. It simply pauses open background apps.",
                "total_steps": 3,
                "steps": [
                    {"step_number": 1, "title": "1. Tap III Recent Apps Button", "instruction": "Tap the three vertical lines III button at the bottom of your phone.", "target_ui_element": "III Recents Button", "target_coordinates": {"x_percent": 25.0, "y_percent": 98.0, "radius_percent": 7.0}, "audio_text": "Tap the 3 lines button at the bottom.", "screen_type": "whatsapp_phone_home", "reassurance": "Shows open apps."},
                    {"step_number": 2, "title": "2. Tap 'Close All' Button", "instruction": "Tap the 'Close all' button to instantly pause all battery-draining apps.", "target_ui_element": "Close All Button", "target_coordinates": {"x_percent": 50.0, "y_percent": 85.0, "radius_percent": 8.0}, "audio_text": "Tap Close All.", "screen_type": "settings_home", "reassurance": "Frees memory."},
                    {"step_number": 3, "title": "3. Plug in Original Charger", "instruction": "Plug in your original charger and let the phone charge without using it.", "target_ui_element": "Charging", "target_coordinates": {"x_percent": 50.0, "y_percent": 50.0, "radius_percent": 9.0}, "audio_text": "Plug in your charger. Your phone will charge much faster!", "screen_type": "settings_home", "reassurance": "Fast charging active."}
                ]
            }
        }
    }
}

