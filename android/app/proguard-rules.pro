# Sahayak AI Proguard Rules
-keepattributes JavascriptInterface
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keep class com.sahayak.ai.SahayakBridge { *; }
