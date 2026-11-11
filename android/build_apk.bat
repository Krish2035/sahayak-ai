@echo off
echo ============================================================
echo   Building Sahayak AI Native Android APK with Floating Bubble
echo ============================================================

set JAVA_HOME=C:\Program Files\Java\jdk-23
set ANDROID_HOME=C:\Users\DELL\AppData\Local\Android\Sdk
set GRADLE_USER_HOME=F:\gradle_cache

cd /d "%~dp0"

echo [1/3] Using Android SDK at %ANDROID_HOME%
echo [2/3] Using Gradle cache on Drive F: (F:\gradle_cache)
echo [3/3] Compiling Native Android APK...

call gradlew.bat assembleDebug --no-daemon

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================================
    echo   BUILD SUCCESSFUL! APK generated at:
    echo   F:\krish\AI\android\app\build\outputs\apk\debug\app-debug.apk
    echo ============================================================
) else (
    echo.
    echo [ERROR] Build failed. You can also open the 'android' folder
    echo directly in Android Studio and click 'Build -> Build APK'.
)
pause

