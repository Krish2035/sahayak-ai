# Sahayak AI - Native Android App with 24/7 Floating Overlay Bubble 👵📱

This is the native Android application project for **Sahayak AI (સહાયક AI)**. It wraps the visual guidance engine into a full-fledged native Android app equipped with a persistent **24/7 Floating Grandma Companion Overlay (`FloatingBubbleService`)** that stays on top of WhatsApp, YouTube, and the entire phone OS.

---

## 🌟 Key Native Features

1. **24/7 Draggable Floating Bubble (`FloatingBubbleService.kt`)**:
   - Uses Android's `SYSTEM_ALERT_WINDOW` permission (`TYPE_APPLICATION_OVERLAY`).
   - Floats directly over **WhatsApp, Phone Settings, Camera, YouTube**, etc.
   - **Touch & Drag**: Seniors can drag the bubble anywhere with one thumb; it smoothly snaps to the left or right edge of the phone.
   - **One-Tap Quick Help**: Tapping the bubble opens a floating quick menu without leaving WhatsApp!

2. **Quick Overlay Menu (`floating_quick_menu.xml`)**:
   - 👵 **Current Step Audio**: Reads out the active step guidance in comforting Gujarati/Hindi speech (`TextToSpeech`).
   - 🎙️ **Voice Query**: Direct voice query into Sahayak AI.
   - 👁️ **Camera Screen Vision**: Live camera help for screen detection.
   - 🛡️ **Scam Radar**: Instant check for fraud/scam messages or links.
   - 👨‍👩‍👧 **Caregiver Call (SOS)**: 1-touch dial to the senior's son/daughter.
   - 📱 **Open Full App**: Brings the full Sahayak AI guide to the foreground.

3. **High-Performance Native WebView (`MainActivity.kt`)**:
   - Hardware accelerated with auto-granted microphone and camera permissions for seniors.
   - Native-to-JavaScript two-way bridge via `SahayakBridge.kt` (`window.SahayakAndroid`).

---

## 🛠️ Project Structure

```
android/
├── app/
│   ├── build.gradle.kts          # App dependencies & SDK config (Compile SDK 35)
│   ├── proguard-rules.pro        # Proguard rules for JS Interface
│   └── src/main/
│       ├── AndroidManifest.xml   # Permissions: SYSTEM_ALERT_WINDOW, FOREGROUND_SERVICE
│       ├── java/com/sahayak/ai/
│       │   ├── MainActivity.kt           # Fullscreen WebView + Permissions + Navigation
│       │   ├── FloatingBubbleService.kt  # 24/7 Floating Overlay + Draggable Bubble
│       │   └── SahayakBridge.kt          # JavaScript Interface Bridge
│       └── res/
│           ├── layout/
│           │   ├── activity_main.xml         # Fullscreen WebView
│           │   ├── floating_bubble_layout.xml# 58dp round emerald bubble layout
│           │   └── floating_quick_menu.xml   # Floating quick help popup menu
│           ├── drawable/                     # Bubble backgrounds, shapes, ripples
│           └── values/                       # Strings, Colors, Dark/Light Themes
├── gradle/                               # Gradle wrapper and version catalog
├── build.gradle.kts                      # Project-level build script
├── settings.gradle.kts                   # Project settings
├── local.properties                      # Local Android SDK configuration
├── build_apk.bat                         # 1-Click build script to generate APK
└── README_ANDROID.md                     # This documentation
```

---

## 🚀 How to Build & Run

### Option 1: One-Click Build Script
Run the batch file in root or android folder:
```cmd
build_apk.bat
```
The compiled APK will be generated at:
`android\app\build\outputs\apk\debug\app-debug.apk`

### Option 2: Using Android Studio
1. Open **Android Studio**.
2. Select **File -> Open...** and choose the `f:\krish\AI\android` folder.
3. Wait for Gradle Sync to complete.
4. Click **Run (Shift + F10)** to install and run directly on your connected Android phone or emulator!
5. To generate a shareable APK: Select **Build -> Build Bundle(s) / APK(s) -> Build APK(s)**.

---

## 📱 How to Enable Floating Over WhatsApp on Phone
1. Install the APK on your Android phone.
2. Open **સહાયક AI**.
3. When prompted, tap **"Allow"** on **"Display over other apps"** (SYSTEM_ALERT_WINDOW).
4. Tap the **"વોટ્સએપ પર ફ્લોટિંગ બબલ શરૂ કરો (Start Overlay)"** button.
5. The green grandma bubble 👵 will now float on your screen 24/7! Open WhatsApp or any other app and tap the bubble anytime you get stuck!

