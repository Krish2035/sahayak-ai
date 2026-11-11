package com.sahayak.ai

import android.content.Context
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.provider.Settings
import android.webkit.JavascriptInterface
import android.widget.Toast

class SahayakBridge(private val activity: MainActivity) {

    @JavascriptInterface
    fun isNativeApp(): Boolean {
        return true
    }

    @JavascriptInterface
    fun hasOverlayPermission(): Boolean {
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            Settings.canDrawOverlays(activity)
        } else {
            true
        }
    }

    @JavascriptInterface
    fun requestOverlayPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && !Settings.canDrawOverlays(activity)) {
            val intent = Intent(
                Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                Uri.parse("package:${activity.packageName}")
            )
            activity.startActivityForResult(intent, MainActivity.OVERLAY_PERMISSION_REQ_CODE)
            activity.runOnUiThread {
                Toast.makeText(
                    activity,
                    "વોટ્સએપ પર ફ્લોટિંગ બબલ માટે 'Display over other apps' પરમિશન ચાલુ કરો",
                    Toast.LENGTH_LONG
                ).show()
            }
        }
    }

    @JavascriptInterface
    fun startFloatingBubble() {
        if (!hasOverlayPermission()) {
            requestOverlayPermission()
            return
        }

        val serviceIntent = Intent(activity, FloatingBubbleService::class.java)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            activity.startForegroundService(serviceIntent)
        } else {
            activity.startService(serviceIntent)
        }

        activity.runOnUiThread {
            Toast.makeText(
                activity,
                "👵 સહાયક AI ફ્લોટિંગ બબલ સક્રિય થયો! તમે વોટ્સએપ ખોલી શકો છો.",
                Toast.LENGTH_LONG
            ).show()
        }
    }

    @JavascriptInterface
    fun stopFloatingBubble() {
        val serviceIntent = Intent(activity, FloatingBubbleService::class.java)
        activity.stopService(serviceIntent)
    }

    @JavascriptInterface
    fun updateActiveStep(title: String, desc: String, audio: String) {
        FloatingBubbleService.updateStep(title, desc, audio)
    }

    @JavascriptInterface
    fun setCaregiverPhone(phone: String) {
        FloatingBubbleService.caregiverPhone = phone
    }
}

