package com.sahayak.ai

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.app.Service
import android.content.Context
import android.content.Intent
import android.graphics.PixelFormat
import android.net.Uri
import android.os.Build
import android.os.IBinder
import android.speech.tts.TextToSpeech
import android.view.Gravity
import android.view.LayoutInflater
import android.view.MotionEvent
import android.view.View
import android.view.WindowManager
import android.widget.Button
import android.widget.ImageButton
import android.widget.TextView
import androidx.core.app.NotificationCompat
import java.util.Locale

class FloatingBubbleService : Service(), TextToSpeech.OnInitListener {

    private lateinit var windowManager: WindowManager
    private var bubbleView: View? = null
    private var overlayMenuView: View? = null
    private var tts: TextToSpeech? = null

    private lateinit var bubbleParams: WindowManager.LayoutParams
    private lateinit var menuParams: WindowManager.LayoutParams

    // Drag tracking
    private var initialX = 0
    private var initialY = 0
    private var initialTouchX = 0f
    private var initialTouchY = 0f
    private var isDragging = false

    companion object {
        const val CHANNEL_ID = "sahayak_floating_bubble_channel"
        const val NOTIFICATION_ID = 1001

        var currentStepTitle: String = "👉 હાલનું પગલું: વૉટ્સએપ ખોલો"
        var currentStepDesc: String = "સ્ક્રીન પર લીલા રંગના વોટ્સએપ આઇકન પર અડો."
        var currentStepAudio: String = "તમારા ફોનની સ્ક્રીન પર લીલા રંગનું વૉટ્સએપનું ગોળ નિશાન શોધો અને તેના પર એક વાર ટચ કરો."
        var caregiverPhone: String = ""

        fun updateStep(title: String, desc: String, audio: String) {
            currentStepTitle = title
            currentStepDesc = desc
            currentStepAudio = audio
        }
    }

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onCreate() {
        super.onCreate()
        windowManager = getSystemService(Context.WINDOW_SERVICE) as WindowManager
        tts = TextToSpeech(this, this)

        createNotificationChannel()
        startForeground(NOTIFICATION_ID, buildForegroundNotification())

        initFloatingBubble()
        initOverlayMenu()
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                getString(R.string.bubble_channel_name),
                NotificationManager.IMPORTANCE_LOW
            ).apply {
                description = getString(R.string.bubble_channel_desc)
                setShowBadge(false)
            }
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(channel)
        }
    }

    private fun buildForegroundNotification(): Notification {
        val launchIntent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
        }
        val pendingIntent = PendingIntent.getActivity(
            this, 0, launchIntent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
        )

        return NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle(getString(R.string.bubble_notification_title))
            .setContentText(getString(R.string.bubble_notification_text))
            .setSmallIcon(R.drawable.ic_launcher)
            .setContentIntent(pendingIntent)
            .setOngoing(true)
            .build()
    }

    private fun initFloatingBubble() {
        val layoutFlag = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY
        } else {
            @Suppress("DEPRECATION")
            WindowManager.LayoutParams.TYPE_PHONE
        }

        bubbleParams = WindowManager.LayoutParams(
            WindowManager.LayoutParams.WRAP_CONTENT,
            WindowManager.LayoutParams.WRAP_CONTENT,
            layoutFlag,
            WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
            PixelFormat.TRANSLUCENT
        ).apply {
            gravity = Gravity.TOP or Gravity.START
            x = 30
            y = 400
        }

        bubbleView = LayoutInflater.from(this).inflate(R.layout.floating_bubble_layout, null)
        setupBubbleTouch()

        windowManager.addView(bubbleView, bubbleParams)
    }

    private fun setupBubbleTouch() {
        bubbleView?.setOnTouchListener { _, event ->
            when (event.action) {
                MotionEvent.ACTION_DOWN -> {
                    initialX = bubbleParams.x
                    initialY = bubbleParams.y
                    initialTouchX = event.rawX
                    initialTouchY = event.rawY
                    isDragging = false
                    true
                }
                MotionEvent.ACTION_MOVE -> {
                    val dx = (event.rawX - initialTouchX).toInt()
                    val dy = (event.rawY - initialTouchY).toInt()

                    if (Math.abs(dx) > 10 || Math.abs(dy) > 10) {
                        isDragging = true
                    }

                    if (isDragging) {
                        bubbleParams.x = initialX + dx
                        bubbleParams.y = initialY + dy
                        windowManager.updateViewLayout(bubbleView, bubbleParams)
                    }
                    true
                }
                MotionEvent.ACTION_UP -> {
                    if (!isDragging) {
                        // It was a click! Toggle the Quick Help Overlay Menu
                        showOverlayMenu()
                    } else {
                        // Snap bubble to nearest screen edge (left or right)
                        snapBubbleToEdge()
                    }
                    true
                }
                else -> false
            }
        }
    }

    private fun snapBubbleToEdge() {
        val screenWidth = resources.displayMetrics.widthPixels
        val bubbleWidth = bubbleView?.width ?: 160
        bubbleParams.x = if (bubbleParams.x + bubbleWidth / 2 < screenWidth / 2) {
            20 // Snap to left edge
        } else {
            screenWidth - bubbleWidth - 20 // Snap to right edge
        }
        windowManager.updateViewLayout(bubbleView, bubbleParams)
    }

    private fun initOverlayMenu() {
        val layoutFlag = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY
        } else {
            @Suppress("DEPRECATION")
            WindowManager.LayoutParams.TYPE_PHONE
        }

        menuParams = WindowManager.LayoutParams(
            WindowManager.LayoutParams.MATCH_PARENT,
            WindowManager.LayoutParams.MATCH_PARENT,
            layoutFlag,
            WindowManager.LayoutParams.FLAG_NOT_TOUCH_MODAL or WindowManager.LayoutParams.FLAG_LAYOUT_IN_SCREEN,
            PixelFormat.TRANSLUCENT
        ).apply {
            gravity = Gravity.CENTER
        }

        overlayMenuView = LayoutInflater.from(this).inflate(R.layout.floating_quick_menu, null)

        // Close Menu
        overlayMenuView?.findViewById<ImageButton>(R.id.btnCloseMenu)?.setOnClickListener {
            hideOverlayMenu()
        }

        // Click outside dialog to dismiss
        overlayMenuView?.findViewById<View>(R.id.menuRoot)?.setOnClickListener {
            hideOverlayMenu()
        }

        // Speak Current Step
        overlayMenuView?.findViewById<Button>(R.id.btnOverlaySpeakStep)?.setOnClickListener {
            speakCurrentStep()
        }

        // Open Full App
        overlayMenuView?.findViewById<Button>(R.id.btnOpenFullApp)?.setOnClickListener {
            hideOverlayMenu()
            val intent = Intent(this, MainActivity::class.java).apply {
                flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_REORDER_TO_FRONT
            }
            startActivity(intent)
        }

        // 4 Quick Actions
        overlayMenuView?.findViewById<View>(R.id.btnQuickMic)?.setOnClickListener {
            hideOverlayMenu()
            openAppWithAction("mic")
        }
        overlayMenuView?.findViewById<View>(R.id.btnQuickCam)?.setOnClickListener {
            hideOverlayMenu()
            openAppWithAction("camera")
        }
        overlayMenuView?.findViewById<View>(R.id.btnQuickScam)?.setOnClickListener {
            hideOverlayMenu()
            openAppWithAction("scam")
        }
        overlayMenuView?.findViewById<View>(R.id.btnQuickSos)?.setOnClickListener {
            hideOverlayMenu()
            if (caregiverPhone.isNotBlank()) {
                val callIntent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:$caregiverPhone")).apply {
                    flags = Intent.FLAG_ACTIVITY_NEW_TASK
                }
                startActivity(callIntent)
            } else {
                openAppWithAction("family")
            }
        }
    }

    private fun showOverlayMenu() {
        if (overlayMenuView?.windowToken != null) return

        // Update current step labels
        overlayMenuView?.findViewById<TextView>(R.id.txtCurrentStepTitle)?.text = currentStepTitle
        overlayMenuView?.findViewById<TextView>(R.id.txtCurrentStepDesc)?.text = currentStepDesc

        windowManager.addView(overlayMenuView, menuParams)
    }

    private fun hideOverlayMenu() {
        if (overlayMenuView?.windowToken != null) {
            windowManager.removeView(overlayMenuView)
        }
    }

    private fun openAppWithAction(action: String) {
        val intent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_REORDER_TO_FRONT
            putExtra("trigger_action", action)
        }
        startActivity(intent)
    }

    private fun speakCurrentStep() {
        if (tts != null && currentStepAudio.isNotBlank()) {
            tts?.speak(currentStepAudio, TextToSpeech.QUEUE_FLUSH, null, "SahayakStepAudio")
        }
    }

    override fun onInit(status: Int) {
        if (status == TextToSpeech.SUCCESS) {
            val guResult = tts?.setLanguage(Locale("gu", "IN"))
            if (guResult == TextToSpeech.LANG_MISSING_DATA || guResult == TextToSpeech.LANG_NOT_SUPPORTED) {
                val hiResult = tts?.setLanguage(Locale("hi", "IN"))
                if (hiResult == TextToSpeech.LANG_MISSING_DATA || hiResult == TextToSpeech.LANG_NOT_SUPPORTED) {
                    tts?.setLanguage(Locale.ENGLISH)
                }
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        tts?.stop()
        tts?.shutdown()

        hideOverlayMenu()
        if (bubbleView != null && bubbleView?.windowToken != null) {
            windowManager.removeView(bubbleView)
        }
    }
}
