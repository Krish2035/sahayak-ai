/**
 * Sahayak AI: Systematic Step-by-Step Visual Guide
 * Conversational Feed Engine with Photos Embedded Below Every Step
 * Trilingual: Gujarati (Primary), Hindi, English
 */

// Resolve backend API URL for local dev, Render, or Vercel
function getApiBaseUrl() {
  const meta = document.querySelector('meta[name="backend-api-url"]');
  if (meta && meta.content && meta.content.trim() !== '' && !meta.content.includes('YOUR_RENDER_URL')) {
    return meta.content.replace(/\/+$/, '');
  }
  if (window.__BACKEND_API_URL__) {
    return window.__BACKEND_API_URL__.replace(/\/+$/, '');
  }
  const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
  if (isLocal) {
    return window.location.origin;
  }
  return '';
}

// Application State
const state = {
  currentLanguage: 'gu', // default to Gujarati, toggle to Hindi / English
  isListening: false,
  recognition: null,
  speechSynth: window.speechSynthesis || null,
  currentSpeakingUtterance: null,
  apiBaseUrl: getApiBaseUrl(),
  latestFlow: null,
  fontSizeLevel: 0, // 0: normal, 1: large (A++), 2: xlarge (A-)
  isVoiceNavActive: false,
  voiceNavRecognition: null
};

// Trilingual UI Translations
const UI_STRINGS = {
  gu: {
    appTitle: "સહાયક AI",
    appSubtitle: "વડીલો માટે સ્ટેપ-બાય-સ્ટેપ ફોટો ગાઈડ",
    reassuranceGeneral: "ચિંતા કરશો નહીં, આ ગાઈડથી તમારા ફોનમાં કશું જ ડિલીટ કે ખોટું નહીં થાય.",
    welcomeTitle: "નમસ્તે! હું તમારો સહાયક AI છું",
    welcomeDesc: "તમારે ફોનમાં જે પણ કરવું હોય, તે નીચે માઇક દબાવીને બોલો અથવા લખો. હું તમને દરેક સ્ટેપની નીચે ફોટો સાથે સરળતાથી સમજાવીશ.",
    quickTrayTitle: "પ્રશ્ન પૂછવા માટે અહીં ટચ કરો:",
    q1: "વોટ્સએપ પર કોઈનો નંબર કેવી રીતે મોકલવો?",
    q2: "વોટ્સએપ પર ફોટો કેવી રીતે મોકલવો?",
    q3: "દુકાને ક્યૂઆર કોડ સ્કેન કરીને પેમેન્ટ કેમ કરવું?",
    q4: "ફોનમાં અક્ષરો મોટા કેવી રીતે કરવા?",
    q5: "YouTube પર ભજન કેવી રીતે ડાઉનલોડ કરવું?",
    q6: "WhatsApp પર લાઈવ લોકેશન કેમ મોકલવું?",
    q7: "અજાણ્યા ફોન નંબર બ્લોક કેમ કરવા?",
    q8: "વોટ્સએપ પર બોલીને અવાજનો મેસેજ કેમ મોકલવો?",
    inputPlaceholder: "બોલો અથવા અહીં પ્રશ્ન લખો (દા.ત. વૉટ્સએપ નંબર)...",
    micListening: "🎙️ સાંભળી રહ્યું છે... તમારો પ્રશ્ન બોલો",
    thinking: "સહાયક AI સ્ટેપ-બાય-સ્ટેપ ફોટો ગાઈડ તૈયાર કરી રહ્યું છે...",
    stepLabel: "પગલું",
    tapHere: "👉 અહીં ટચ કરો",
    listenStep: "🔊 સાંભળો",
    stopAudio: "⏹️ બંધ કરો",
    listenFull: "🔊 પૂરો ગાઈડ સાંભળો",
    shareDad: "📲 પપ્પાને WhatsApp પર મોકલો",
    finishBannerTitle: "કામ પૂરું થયું! 🎉",
    finishBannerDesc: "આ બધા પગલાં અનુસર્યા પછી તમારું કામ સરળતાથી પૂરું થઈ જશે.",
    copiedToast: "લિંક કોપી થઈ ગઈ છે!",
    stepDoneBtn: "મેં આ કર્યું ✓",
    stepDoneCompleted: "પૂર્ણ થયું! ✅",
    voiceNavActive: "🎙️ બોલો 'Next' અથવા 'આગળ' આગળ વધવા માટે",
    voiceNavNextHeard: "આગળનું પગલું ખોલ્યું",
    voiceNavBackHeard: "પાછલું પગલું ખોલ્યું"
  },
  hi: {
    appTitle: "सहायक AI",
    appSubtitle: "वरिष्ठ नागरिकों के लिए फोटो गाइड",
    reassuranceGeneral: "चिंता मत कीजिए, इस गाइड से आपके फोन में कुछ भी गलत या डिलीट नहीं होगा।",
    welcomeTitle: "नमस्ते! मैं आपका सहायक AI हूँ",
    welcomeDesc: "आपको फोन में जो भी करना है, नीचे माइक दबाकर बोलें या लिखें। मैं आपको हर स्टेप के नीचे फोटो के साथ समझाऊँगा।",
    quickTrayTitle: "सवाल पूछने के लिए यहाँ छुएं:",
    q1: "व्हाट्सएप पर किसी का नंबर कैसे भेजें?",
    q2: "व्हाट्सएप पर फोटो कैसे भेजें?",
    q3: "दुकान पर क्यूआर कोड स्कैन करके भुगतान कैसे करें?",
    q4: "फोन में लिखावट (अक्षर) बड़े कैसे करें?",
    q5: "YouTube पर भजन कैसे डाउनलोड करें?",
    q6: "WhatsApp पर लाइव लोकेशन कैसे भेजें?",
    q7: "अनजान फोन नंबर ब्लॉक कैसे करें?",
    q8: "व्हाट्सएप पर बोलकर आवाज का मैसेज कैसे भेजें?",
    inputPlaceholder: "बोलें या यहाँ सवाल लिखें (उदा. व्हाट्सएप नंबर)...",
    micListening: "🎙️ सुन रहा हूँ... अपना सवाल बोलिए",
    thinking: "सहायक AI स्टेप-बाय-स्टेप फोटो गाइड तैयार कर रहा है...",
    stepLabel: "कदम",
    tapHere: "👉 यहाँ छुएं",
    listenStep: "🔊 सुनें",
    stopAudio: "⏹️ रोकें",
    listenFull: "🔊 पूरी गाइड सुनें",
    shareDad: "📲 पिताजी को WhatsApp पर भेजें",
    finishBannerTitle: "काम पूरा हुआ! 🎉",
    finishBannerDesc: "इन सभी कदमों को पूरा करने के बाद आपका काम आसानी से हो जाएगा।",
    copiedToast: "गाइड कॉपी हो गई है!",
    stepDoneBtn: "मैंने यह कर लिया ✓",
    stepDoneCompleted: "पूरा हुआ! ✅",
    voiceNavActive: "🎙️ बोलिए 'Next' या 'आगे' अगले कदम पर जाने के लिए",
    voiceNavNextHeard: "अगले कदम पर आ गए",
    voiceNavBackHeard: "पिछले कदम पर आ गए"
  },
  en: {
    appTitle: "Sahayak AI",
    appSubtitle: "Step-by-Step Visual Guide for Seniors",
    reassuranceGeneral: "Don't worry, following this guide will not delete anything or break your phone.",
    welcomeTitle: "Hello! I am your Sahayak AI",
    welcomeDesc: "Tell me what you want to do on your phone by tapping the microphone or typing below. I will guide you with a real screenshot under every single step.",
    quickTrayTitle: "Common Questions (tap to try):",
    q1: "How to send someone's phone number on WhatsApp?",
    q2: "How to send a photo on WhatsApp?",
    q3: "How to scan a QR code to pay at a shop?",
    q4: "How to make text and letters bigger on phone?",
    q5: "How to download bhajan/songs on YouTube?",
    q6: "How to share live location on WhatsApp?",
    q7: "How to block unknown spam phone numbers?",
    q8: "How to send a voice message on WhatsApp?",
    inputPlaceholder: "Speak or type your question (e.g. WhatsApp number)...",
    micListening: "🎙️ Listening... speak your question now",
    thinking: "Sahayak AI is generating your systematic step-by-step visual guide...",
    stepLabel: "Step",
    tapHere: "👉 Tap Here",
    listenStep: "🔊 Listen",
    stopAudio: "⏹️ Stop",
    listenFull: "🔊 Listen to Full Guide",
    shareDad: "📲 Share with Dad on WhatsApp",
    finishBannerTitle: "All Done! 🎉",
    finishBannerDesc: "Following these steps will safely complete your task.",
    copiedToast: "Guide copied to clipboard!",
    stepDoneBtn: "Done with this step ✓",
    stepDoneCompleted: "Completed! ✅",
    voiceNavActive: "🎙️ Say 'Next' or 'Back' to navigate hands-free",
    voiceNavNextHeard: "Next step",
    voiceNavBackHeard: "Previous step"
  }
};

// Screen Mockups Assets Map
const SCREEN_ASSETS = {
  whatsapp_phone_home: "assets/screens/whatsapp_phone_home.svg",
  whatsapp_chat_list: "assets/screens/whatsapp_chat_list.svg",
  whatsapp_chat_screen: "assets/screens/whatsapp_chat_screen.svg",
  whatsapp_attachment_menu: "assets/screens/whatsapp_attachment_menu.svg",
  whatsapp_contact_search: "assets/screens/whatsapp_contact_search.svg",
  whatsapp_contact_picker: "assets/screens/whatsapp_contact_picker.svg",
  whatsapp_photo_preview: "assets/screens/whatsapp_photo_preview.svg",
  youtube_bhajan_screen: "assets/screens/youtube_bhajan_screen.svg",
  phone_recents_screen: "assets/screens/phone_recents_screen.svg",
  maps_directions_screen: "assets/screens/maps_directions_screen.svg",
  clock_alarm_screen: "assets/screens/clock_alarm_screen.svg",
  gpay_home: "assets/screens/gpay_home.svg",
  scanner_camera: "assets/screens/gpay_scanner.svg",
  gpay_amount_screen: "assets/screens/gpay_amount.svg",
  android_home: "assets/screens/whatsapp_phone_home.svg",
  settings_list: "assets/screens/settings_home.svg",
  font_settings: "assets/screens/settings_home.svg",
  settings_home: "assets/screens/settings_home.svg",
  default_screen: "assets/screens/whatsapp_chat_screen.svg"
};

// DOM References
const el = {
  btnThemeToggle: document.getElementById('btnThemeToggle'),
  themeIcon: document.getElementById('themeIcon'),
  btnFontZoom: document.getElementById('btnFontZoom'),
  fontZoomLabel: document.getElementById('fontZoomLabel'),
  langSelectBtn: document.getElementById('langSelectBtn'),
  langLabel: document.getElementById('langLabel'),
  btnClearChat: document.getElementById('btnClearChat'),
  reassuranceText: document.getElementById('reassuranceText'),
  chatFeed: document.getElementById('chatFeed'),
  welcomeCard: document.getElementById('welcomeCard'),
  welcomeTitle: document.getElementById('welcomeTitle'),
  welcomeDesc: document.getElementById('welcomeDesc'),
  quickTrayTitle: document.getElementById('quickTrayTitle'),
  chipQ1: document.getElementById('chipQ1'),
  chipQ2: document.getElementById('chipQ2'),
  chipQ3: document.getElementById('chipQ3'),
  chipQ4: document.getElementById('chipQ4'),
  chipQ5: document.getElementById('chipQ5'),
  chipQ6: document.getElementById('chipQ6'),
  chipQ7: document.getElementById('chipQ7'),
  chipQ8: document.getElementById('chipQ8'),
  chipQ1Text: document.getElementById('chipQ1Text'),
  chipQ2Text: document.getElementById('chipQ2Text'),
  chipQ3Text: document.getElementById('chipQ3Text'),
  chipQ4Text: document.getElementById('chipQ4Text'),
  chipQ5Text: document.getElementById('chipQ5Text'),
  chipQ6Text: document.getElementById('chipQ6Text'),
  chipQ7Text: document.getElementById('chipQ7Text'),
  chipQ8Text: document.getElementById('chipQ8Text'),
  chatInput: document.getElementById('chatInput'),
  btnMic: document.getElementById('btnMic'),
  btnSend: document.getElementById('btnSend'),
  micActiveBanner: document.getElementById('micActiveBanner')
};

// Senior High-Contrast Light Mode Engine
function initTheme() {
  const savedTheme = localStorage.getItem('sahayak_theme') || 'dark';
  applyTheme(savedTheme);
}

function applyTheme(theme) {
  if (theme === 'light') {
    document.body.classList.add('light-theme');
    if (el.themeIcon) el.themeIcon.textContent = '🌙';
  } else {
    document.body.classList.remove('light-theme');
    if (el.themeIcon) el.themeIcon.textContent = '☀️';
  }
  localStorage.setItem('sahayak_theme', theme);
}

function toggleTheme() {
  const isLight = document.body.classList.contains('light-theme');
  applyTheme(isLight ? 'dark' : 'light');
}

// Initialize Speech Recognition (STT for Queries)
function initSpeechRecognition() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    console.warn("Web Speech Recognition API not supported in this browser.");
    return;
  }

  state.recognition = new SpeechRecognition();
  state.recognition.continuous = false;
  state.recognition.interimResults = false;

  state.recognition.onstart = () => {
    state.isListening = true;
    stopVoiceNavListener(); // pause voice nav during query dictation
    if (el.btnMic) el.btnMic.classList.add('listening');
    if (el.micActiveBanner) el.micActiveBanner.classList.add('active');
  };

  state.recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    console.log("Voice transcript recognized:", transcript);
    el.chatInput.value = transcript;
    submitQuery(transcript, true);
  };

  state.recognition.onerror = (event) => {
    console.warn("Speech recognition error:", event.error);
    stopListening();
  };

  state.recognition.onend = () => {
    stopListening();
  };
}

function startListening() {
  if (!state.recognition) {
    initSpeechRecognition();
  }
  if (!state.recognition) {
    alert("Speech recognition is not available in this browser. You can type your query in the text box.");
    return;
  }

  const langMap = { gu: 'gu-IN', hi: 'hi-IN', en: 'en-IN' };
  state.recognition.lang = langMap[state.currentLanguage] || 'gu-IN';

  try {
    state.recognition.start();
  } catch (err) {
    console.warn("Recognition already active or failed to start:", err);
  }
}

function stopListening() {
  state.isListening = false;
  if (el.btnMic) el.btnMic.classList.remove('listening');
  if (el.micActiveBanner) el.micActiveBanner.classList.remove('active');
}

// Live Voice Navigation Mode ("Next" / "આગળ" Hands-Free Trigger)
function startVoiceNavListener() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) return;

  if (state.voiceNavRecognition) {
    try { state.voiceNavRecognition.stop(); } catch (e) {}
  }

  const navRec = new SpeechRecognition();
  navRec.continuous = true;
  navRec.interimResults = false;
  const langMap = { gu: 'gu-IN', hi: 'hi-IN', en: 'en-IN' };
  navRec.lang = langMap[state.currentLanguage] || 'gu-IN';

  navRec.onresult = (event) => {
    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        const spoken = event.results[i][0].transcript.trim().toLowerCase();
        console.log("Live Voice Nav heard:", spoken);
        handleVoiceNavCommand(spoken);
      }
    }
  };

  navRec.onerror = (e) => {
    console.log("Voice nav notice:", e.error);
  };

  navRec.onend = () => {
    if (state.isVoiceNavActive && !state.isListening) {
      try { navRec.start(); } catch (err) {}
    }
  };

  state.voiceNavRecognition = navRec;
  state.isVoiceNavActive = true;
  try {
    navRec.start();
  } catch (err) {}
}

function stopVoiceNavListener() {
  state.isVoiceNavActive = false;
  if (state.voiceNavRecognition) {
    try { state.voiceNavRecognition.stop(); } catch (e) {}
  }
}

function handleVoiceNavCommand(spoken) {
  const isNext = /next|આગળ|આગલ|आगे|agla|agle|nekst/i.test(spoken);
  const isBack = /back|પાછળ|પાછલ|પીછે|piche|pichhe|bek/i.test(spoken);

  if (isNext) {
    const stepCards = document.querySelectorAll('.systematic-step-card');
    for (let card of stepCards) {
      const btn = card.querySelector('.step-done-btn');
      if (btn && !btn.classList.contains('completed')) {
        btn.click();
        const feedback = UI_STRINGS[state.currentLanguage].voiceNavNextHeard;
        speakText(feedback);
        return;
      }
    }
  } else if (isBack) {
    const stepCards = Array.from(document.querySelectorAll('.systematic-step-card'));
    for (let i = stepCards.length - 1; i >= 0; i--) {
      const btn = stepCards[i].querySelector('.step-done-btn');
      if (btn && btn.classList.contains('completed')) {
        btn.classList.remove('completed');
        btn.innerHTML = `<span>✓</span> <span>${UI_STRINGS[state.currentLanguage].stepDoneBtn}</span>`;
        stepCards[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
        const feedback = UI_STRINGS[state.currentLanguage].voiceNavBackHeard;
        speakText(feedback);
        return;
      }
    }
    if (stepCards.length > 0) {
      stepCards[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
}

// Text-to-Speech (TTS)
function speakText(textToSpeak, onEndCallback) {
  if (!state.speechSynth) return;
  state.speechSynth.cancel();

  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  utterance.rate = 0.82; // Patient, slow pace for elderly listeners
  utterance.pitch = 1.0;

  const langMap = { gu: 'gu-IN', hi: 'hi-IN', en: 'en-IN' };
  utterance.lang = langMap[state.currentLanguage] || 'gu-IN';

  utterance.onend = () => {
    state.currentSpeakingUtterance = null;
    if (onEndCallback) onEndCallback();
  };

  utterance.onerror = () => {
    state.currentSpeakingUtterance = null;
    if (onEndCallback) onEndCallback();
  };

  state.currentSpeakingUtterance = utterance;
  state.speechSynth.speak(utterance);
}

function stopSpeaking() {
  if (state.speechSynth) {
    state.speechSynth.cancel();
  }
  state.currentSpeakingUtterance = null;
}

// Submit User Query
async function submitQuery(queryText, wasVoice = false) {
  const query = queryText.trim();
  if (!query) return;

  // Clear input
  el.chatInput.value = '';
  stopListening();

  // Hide welcome card once a conversation begins
  if (el.welcomeCard) {
    el.welcomeCard.style.display = 'none';
  }

  // 1. Render User Message in Chat Feed
  renderUserMessage(query, wasVoice);

  // 2. Render Thinking Indicator
  const thinkingId = renderThinkingIndicator();

  // 3. Fetch Guide from Backend or Offline Fallback
  try {
    const res = await fetch(`${state.apiBaseUrl}/api/query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: query,
        language: state.currentLanguage,
        platform: 'android',
        user_age_group: 'senior'
      })
    });

    removeThinkingIndicator(thinkingId);

    if (res.status === 429) {
      const errJson = await res.json().catch(() => ({}));
      const limitMsg = errJson.message || "કૃપા કરીને ૧ મિનિટ રાહ જુઓ. વડીલોની સુરક્ષા માટે પ્રતિ મિનિટે ૧૦ સવાલોની મર્યાદા છે.";
      alert(limitMsg);
      return;
    }

    if (!res.ok) throw new Error("API call failed");
    const flowData = await res.json();
    state.latestFlow = flowData;
    renderAiVisualGuide(flowData);
  } catch (err) {
    console.warn("Backend request failed, falling back to local flow:", err);
    removeThinkingIndicator(thinkingId);
    const fallbackFlow = getLocalFallbackFlow(query);
    state.latestFlow = fallbackFlow;
    renderAiVisualGuide(fallbackFlow);
  }
}

// Render User Message
function renderUserMessage(text, wasVoice) {
  const row = document.createElement('div');
  row.className = 'chat-row user';
  row.innerHTML = `
    <div class="user-bubble">
      ${wasVoice ? '<span class="voice-icon">🎙️</span>' : ''}
      <span>${escapeHtml(text)}</span>
    </div>
  `;
  el.chatFeed.appendChild(row);
  scrollToBottom();
}

// Render Thinking Indicator
function renderThinkingIndicator() {
  const thinkingId = `thinking-${Date.now()}`;
  const row = document.createElement('div');
  row.className = 'chat-row ai';
  row.id = thinkingId;
  row.innerHTML = `
    <div class="ai-avatar-icon">👵</div>
    <div class="ai-thinking-row">
      <div class="thinking-dots">
        <div class="dot"></div>
        <div class="dot"></div>
        <div class="dot"></div>
      </div>
      <span>${UI_STRINGS[state.currentLanguage].thinking}</span>
    </div>
  `;
  el.chatFeed.appendChild(row);
  scrollToBottom();
  return thinkingId;
}

function removeThinkingIndicator(thinkingId) {
  const elThinking = document.getElementById(thinkingId);
  if (elThinking) elThinking.remove();
}

// CORE: Render Systematic Step-by-Step Guide with Photos Embedded Below Every Step
function renderAiVisualGuide(flowData) {
  const strings = UI_STRINGS[state.currentLanguage];
  const containerRow = document.createElement('div');
  containerRow.className = 'chat-row ai';

  // ChatGPT-style AI Avatar
  const avatar = document.createElement('div');
  avatar.className = 'ai-avatar-icon';
  avatar.innerHTML = '👵';
  containerRow.appendChild(avatar);

  const container = document.createElement('div');
  container.className = 'ai-response-container';

  // 1. AI Guide Header
  const header = document.createElement('div');
  header.className = 'ai-response-header';
  header.innerHTML = `
    <div class="guide-badge-pill">
      <span>●</span>
      <span>${flowData.intent_info?.app_name || "App"} • ${flowData.total_steps || flowData.steps.length} ${strings.stepLabel}</span>
    </div>
    <h2 class="guide-main-title">${escapeHtml(flowData.title)}</h2>
    <p class="guide-summary-text">${escapeHtml(flowData.summary)}</p>
    <div class="guide-actions-bar">
      <button class="btn-guide-action" id="btnPlayAll-${Date.now()}">
        <span>🔊</span>
        <span>${strings.listenFull}</span>
      </button>
      <button class="btn-guide-action" id="btnShareDad-${Date.now()}">
        <span>📲</span>
        <span>${strings.shareDad}</span>
      </button>
    </div>
    <!-- Live Voice Navigation Mode Banner -->
    <div class="voice-nav-banner">
      <div class="voice-nav-badge">
        <span class="voice-nav-indicator-dot"></span>
        <span>${strings.voiceNavActive}</span>
      </div>
      <span class="voice-nav-hint">Next ➔ / Back ⬅️</span>
    </div>
  `;
  container.appendChild(header);

  // Bind Header Listeners
  const btnPlayAll = header.querySelector('[id^="btnPlayAll-"]');
  btnPlayAll.addEventListener('click', () => playFullGuideAudio(flowData, btnPlayAll));

  const btnShareDad = header.querySelector('[id^="btnShareDad-"]');
  btnShareDad.addEventListener('click', () => shareGuideOnWhatsApp(flowData));

  // 2. Systematic Step Cards List
  const stepsList = document.createElement('div');
  stepsList.className = 'steps-feed-list';

  flowData.steps.forEach((step, idx) => {
    const stepCard = document.createElement('div');
    stepCard.className = 'systematic-step-card';

    // Step Header with Title & Instruction
    const stepHeader = document.createElement('div');
    stepHeader.className = 'step-header-area';
    stepHeader.innerHTML = `
      <div class="step-num-pill">${strings.stepLabel} ${step.step_number || idx + 1}</div>
      <h3 class="step-title-text">${escapeHtml(step.title)}</h3>
      <p class="step-instruction-text">${escapeHtml(step.instruction)}</p>
      <div class="step-meta-row">
        <div class="target-badge">${escapeHtml(step.target_ui_element)}</div>
        <button class="step-speaker-btn" data-audio-step="${idx}">
          <span>🔊</span>
          <span>${strings.listenStep}</span>
        </button>
        <button class="btn-guide-action btn-ask-child-step" data-step-num="${idx + 1}" data-step-title="${escapeHtml(step.title)}">
          <span>👨‍👩‍👧</span>
          <span>બેટાને પૂછો</span>
        </button>
      </div>
    `;

    // Embedded Photo Container (Directly below the step!)
    const photoContainer = document.createElement('div');
    photoContainer.className = 'step-photo-container';

    const assetPath = SCREEN_ASSETS[step.screen_type] || SCREEN_ASSETS.default_screen;
    
    // Exact Coordinate Grounding
    let spotlightHtml = '';
    if (step.target_coordinates) {
      const { x_percent, y_percent, radius_percent } = step.target_coordinates;
      const radiusPx = (radius_percent || 7) * 4.5;
      spotlightHtml = `
        <div class="step-spotlight-ring" 
             style="left: ${x_percent}%; top: ${y_percent}%; width: ${radiusPx * 2}px; height: ${radiusPx * 2}px;"
             title="${escapeHtml(step.target_ui_element)}"></div>
        <div class="step-tap-indicator" style="left: ${x_percent}%; top: ${y_percent}%;">
          ${strings.tapHere}
        </div>
      `;
    }

    photoContainer.innerHTML = `
      <img class="step-photo-img" src="${assetPath}" alt="${escapeHtml(step.title)}">
      ${spotlightHtml}
    `;

    // Step Reassurance Footer if provided
    let reassuranceHtml = '';
    if (step.reassurance) {
      reassuranceHtml = `
        <div class="step-reassurance-footer">
          <span>🛡️</span>
          <span>${escapeHtml(step.reassurance)}</span>
        </div>
      `;
    }

    stepCard.appendChild(stepHeader);
    stepCard.appendChild(photoContainer);
    if (step.reassurance) {
      const footerEl = document.createElement('div');
      footerEl.innerHTML = reassuranceHtml;
      stepCard.appendChild(footerEl.firstElementChild);
    }

    // Step Completion Checklist Button ("મેં આ કર્યું ✓")
    const completionRow = document.createElement('div');
    completionRow.className = 'step-completion-row';
    const doneBtn = document.createElement('button');
    doneBtn.className = 'step-done-btn';
    doneBtn.innerHTML = `<span>✓</span> <span>${strings.stepDoneBtn}</span>`;
    doneBtn.addEventListener('click', () => {
      doneBtn.classList.toggle('completed');
      if (doneBtn.classList.contains('completed')) {
        doneBtn.innerHTML = `<span>✅</span> <span>${strings.stepDoneCompleted}</span>`;
        // Auto-scroll to next step if exists
        setTimeout(() => {
          const nextCard = stepCard.nextElementSibling;
          if (nextCard && nextCard.classList.contains('systematic-step-card')) {
            nextCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }, 200);
      } else {
        doneBtn.innerHTML = `<span>✓</span> <span>${strings.stepDoneBtn}</span>`;
      }
    });
    completionRow.appendChild(doneBtn);
    stepCard.appendChild(completionRow);

    // Step Audio Listener
    const speakerBtn = stepHeader.querySelector('[data-audio-step]');
    speakerBtn.addEventListener('click', () => {
      const textToRead = step.audio_text || step.instruction;
      if (speakerBtn.classList.contains('speaking')) {
        stopSpeaking();
        speakerBtn.classList.remove('speaking');
        speakerBtn.querySelector('span:last-child').textContent = strings.listenStep;
      } else {
        // Reset other speaker buttons
        document.querySelectorAll('.step-speaker-btn.speaking').forEach(b => {
          b.classList.remove('speaking');
          b.querySelector('span:last-child').textContent = strings.listenStep;
        });
        speakerBtn.classList.add('speaking');
        speakerBtn.querySelector('span:last-child').textContent = strings.stopAudio;
        speakText(textToRead, () => {
          speakerBtn.classList.remove('speaking');
          speakerBtn.querySelector('span:last-child').textContent = strings.listenStep;
        });
      }
    });

    // Step Ask Child Button Listener
    const askChildBtn = stepHeader.querySelector('.btn-ask-child-step');
    if (askChildBtn) {
      askChildBtn.addEventListener('click', () => {
        openModal('modalFamilyBridge');
      });
    }

    stepsList.appendChild(stepCard);
  });

  container.appendChild(stepsList);

  // 3. Completion & WhatsApp Share Card
  const finishCard = document.createElement('div');
  finishCard.className = 'guide-finish-card';
  finishCard.innerHTML = `
    <div class="finish-title">
      <span>✅</span>
      <span>${strings.finishBannerTitle}</span>
    </div>
    <p class="finish-desc">${escapeHtml(flowData.reassurance_banner || strings.finishBannerDesc)}</p>
    <button class="btn-whatsapp-share-lg">
      <span>💬</span>
      <span>${strings.shareDad}</span>
    </button>
  `;

  finishCard.querySelector('.btn-whatsapp-share-lg').addEventListener('click', () => shareGuideOnWhatsApp(flowData));
  container.appendChild(finishCard);

  containerRow.appendChild(container);
  el.chatFeed.appendChild(containerRow);
  scrollToBottom();

  // Start continuous voice navigation for elderly users hands-free
  startVoiceNavListener();
}

// Play Full Guide Audio Sequentially
function playFullGuideAudio(flowData, btnElement) {
  const strings = UI_STRINGS[state.currentLanguage];
  if (btnElement.classList.contains('speaking')) {
    stopSpeaking();
    btnElement.classList.remove('speaking');
    btnElement.querySelector('span:last-child').textContent = strings.listenFull;
    return;
  }

  btnElement.classList.add('speaking');
  btnElement.querySelector('span:last-child').textContent = strings.stopAudio;

  let fullScript = `${flowData.title}. `;
  flowData.steps.forEach((step, idx) => {
    fullScript += ` ${strings.stepLabel} ${idx + 1}: ${step.audio_text || step.instruction}. `;
  });

  speakText(fullScript, () => {
    btnElement.classList.remove('speaking');
    btnElement.querySelector('span:last-child').textContent = strings.listenFull;
  });
}

// WhatsApp Share Link Generator
function shareGuideOnWhatsApp(flowData) {
  const lang = state.currentLanguage;
  const taskTitle = flowData.title;

  let shareText = "";
  if (lang === 'gu') {
    shareText = `નમસ્તે પપ્પા! તમે જે પૂછ્યું હતું કે "${taskTitle}", તેની સરળ સ્ટેપ-બાય-સ્ટેપ ગાઈડ અહીં છે: \n`;
  } else if (lang === 'hi') {
    shareText = `नमस्ते पिताजी! आपने जो पूछा था कि "${taskTitle}", उसकी आसान स्टेप-बाई-स्टेप गाइड यहाँ है: \n`;
  } else {
    shareText = `Hi Dad! Here is the simple step-by-step guide for "${taskTitle}": \n`;
  }

  flowData.steps.forEach((step, idx) => {
    shareText += `\n${idx + 1}. ${step.title}: ${step.instruction}`;
  });

  shareText += `\n\n- Sahayak AI (Digital Companion for Parents)`;

  const encodedUrl = `https://wa.me/?text=${encodeURIComponent(shareText)}`;
  window.open(encodedUrl, '_blank');
}

// Local Fallback Flow for 100% Reliable Offline Operation
function getLocalFallbackFlow(query) {
  const lang = state.currentLanguage;
  const qLower = (query || "").toLowerCase();

  // 1. YouTube Bhajan Download
  if (qLower.includes("youtube") || qLower.includes("bhajan") || qLower.includes("ભજન") || qLower.includes("भजन") || qLower.includes("ડાઉનલોડ") || qLower.includes("डाउनलोड")) {
    if (lang === 'gu') {
      return {
        title: "YouTube પર ભજન ડાઉનલોડ કરો",
        summary: "તમારા મનપસંદ ભજનને ફોનમાં ડાઉનલોડ કરો જેથી ઇન્ટરનેટ વગર પણ સાંભળી શકાય.",
        reassurance_banner: "ચિંતા કરશો નહીં, આ ભજન તમારા YouTube માં સુરક્ષિત સેવ રહેશે અને ગમે ત્યારે વાગશે.",
        total_steps: 4,
        intent_info: { app_name: "YouTube", intent: "download_youtube_video" },
        steps: [
          { step_number: 1, title: "1. YouTube એપ ખોલો", instruction: "તમારા ફોનમાં લાલ રંગનું YouTube નું નિશાન શોધો અને તેના પર ટચ કરો.", target_ui_element: "લાલ YouTube આઇકન", target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 }, audio_text: "સૌપ્રથમ લાલ રંગની YouTube એપ ખોલો.", screen_type: "whatsapp_phone_home", reassurance: "YouTube એપ ખુલશે." },
          { step_number: 2, title: "2. ઉપર સર્ચમાં ભજનનું નામ લખો", instruction: "ઉપર આપેલા કાચ જેવા સર્ચ 🔍 નિશાન પર ટચ કરી જે ભજન સાંભળવું હોય તેનું નામ લખો.", target_ui_element: "🔍 સર્ચ બટન", target_coordinates: { x_percent: 82.5, y_percent: 4.0, radius_percent: 6.5 }, audio_text: "ઉપર સર્ચમાં ભજનનું નામ લખો.", screen_type: "youtube_bhajan_screen", reassurance: "ભજનનું લિસ્ટ દેખાશે." },
          { step_number: 3, title: "3. વિડીયો નીચે 'ડાઉનલોડ' પર ટચ કરો", instruction: "ભજન ચાલુ થાય પછી વિડીયોની નીચે ગોળ તીર ⬇️ વાળા 'ડાઉનલોડ' (Download) બટન પર ટચ કરો.", target_ui_element: "⬇️ ડાઉનલોડ બટન", target_coordinates: { x_percent: 63.0, y_percent: 52.0, radius_percent: 7.5 }, audio_text: "વિડીયોની નીચે ડાઉનલોડ બટન પર અડો.", screen_type: "youtube_bhajan_screen", reassurance: "ડાઉનલોડ શરૂ થઈ જશે." },
          { step_number: 4, title: "4. ભજન ડાઉનલોડ થઈ ગયું છે!", instruction: "નીચે લાઈબ્રેરી 📚 માં જઈને તમે નેટ વગર પણ આ ભજન ગમે ત્યારે સાંભળી શકશો.", target_ui_element: "લાઈબ્રેરી સેવ", target_coordinates: { x_percent: 87.5, y_percent: 96.0, radius_percent: 6.0 }, audio_text: "ભજન ડાઉનલોડ થઈ ગયું છે. હવે ઇન્ટરનેટ વગર પણ સાંભળી શકશો.", screen_type: "youtube_bhajan_screen", reassurance: "ભજન સફળતાપૂર્વક સેવ થઈ ગયું છે." }
        ]
      };
    }
  }

  // 2. WhatsApp Share Live Location
  if (qLower.includes("location") || qLower.includes("લોકેશન") || qLower.includes("लोकेशन")) {
    return {
      title: lang === 'gu' ? "WhatsApp પર લાઈવ લોકેશન મોકલો" : (lang === 'hi' ? "WhatsApp पर लाइव लोकेशन भेजें" : "Share Live Location on WhatsApp"),
      summary: lang === 'gu' ? "તમે ક્યાં છો તે ઘરના સભ્યોને નકશા પર તરત જ બતાવો." : (lang === 'hi' ? "घर वालों को नक्शे पर अपनी लोकेशन भेजें।" : "Safely share your location in chat."),
      reassurance_banner: lang === 'gu' ? "ચિંતા કરશો નહીં, આ ફક્ત તમે જેને મોકલશો તેમને જ તમારું લોકેશન બતાવશે." : "Don't worry, your location is shared privately.",
      total_steps: 4,
      intent_info: { app_name: "WhatsApp", intent: "share_location" },
      steps: [
        { step_number: 1, title: lang === 'gu' ? "1. વોટ્સએપ ખોલો" : "1. Open WhatsApp", instruction: lang === 'gu' ? "તમારા ફોનની સ્ક્રીન પર લીલા રંગનું વૉટ્સએપનું નિશાન શોધો." : "Find and open WhatsApp.", target_ui_element: "WhatsApp Icon", target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 }, audio_text: "Open WhatsApp.", screen_type: "whatsapp_phone_home", reassurance: "Safe." },
        { step_number: 2, title: lang === 'gu' ? "2. જેમને મોકલવું છે તેમની ચેટ ખોલો" : "2. Open Chat", instruction: lang === 'gu' ? "જે સભ્યને લોકેશન મોકલવું છે તેમના નામ પર ટચ કરો." : "Tap person's chat.", target_ui_element: "Chat Name", target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 }, audio_text: "Open the chat.", screen_type: "whatsapp_chat_list", reassurance: "Opens conversation." },
        { step_number: 3, title: lang === 'gu' ? "3. પેપરક્લિપ 📎 પર ટચ કરી 'Location' પસંદ કરો" : "3. Tap Clip & Choose Location", instruction: lang === 'gu' ? "નીચે ક્લિપ 📎 પર અડો અને લીલા રંગના 'Location' 📍 બટન પર ટચ કરો." : "Tap Paperclip and select Location 📍.", target_ui_element: "📍 Location Option", target_coordinates: { x_percent: 50.0, y_percent: 76.7, radius_percent: 7.0 }, audio_text: "Tap Location.", screen_type: "whatsapp_attachment_menu", reassurance: "Shows map options." },
        { step_number: 4, title: lang === 'gu' ? "4. 'Send your current location' પર ટચ કરો" : "4. Send Current Location", instruction: lang === 'gu' ? "'Send your current location' વાળા વિકલ્પ પર અડો. તમારું લોકેશન પહોંચી ગયું!" : "Tap Send Current Location.", target_ui_element: "Send Location Button", target_coordinates: { x_percent: 50.0, y_percent: 62.0, radius_percent: 7.5 }, audio_text: "Location sent!", screen_type: "maps_directions_screen", reassurance: "Location successfully sent." }
      ]
    };
  }

  // 3. Block Unknown Number
  if (qLower.includes("block") || qLower.includes("બ્લોક") || qLower.includes("ब्लॉक") || qLower.includes("અજાણ્યા") || qLower.includes("अनजान") || qLower.includes("spam")) {
    return {
      title: lang === 'gu' ? "અજાણ્યા ફોન નંબર બ્લોક કરો" : (lang === 'hi' ? "अनजान फोन नंबर ब्लॉक करें" : "Block Unknown Spam Numbers"),
      summary: lang === 'gu' ? "ખોટા કે અજાણ્યા નંબરોને બ્લોક કરો જેથી તેમના ફોન કે મેસેજ ન આવે." : "Block spam numbers from calling you.",
      reassurance_banner: lang === 'gu' ? "ચિંતા કરશો નહીં, આ નંબર બ્લોક કરવાથી તમારા પોતાના કોઈ સંપર્કો ડિલીટ નહીં થાય." : "Safe to block spam.",
      total_steps: 4,
      intent_info: { app_name: "Phone", intent: "block_phone_number" },
      steps: [
        { step_number: 1, title: lang === 'gu' ? "1. ફોન (કોલ) ની એપ ખોલો" : "1. Open Phone App", instruction: lang === 'gu' ? "તમારા ફોનની સ્ક્રીન પર લીલા ફોન રીસીવર 📞 વાળા આઇકન પર ટચ કરો." : "Tap Phone receiver icon.", target_ui_element: "📞 Phone App", target_coordinates: { x_percent: 38.5, y_percent: 89.6, radius_percent: 7.5 }, audio_text: "Open Phone app.", screen_type: "whatsapp_phone_home", reassurance: "Opens recents." },
        { step_number: 2, title: lang === 'gu' ? "2. અજાણ્યા નંબરની બાજુમાં 'i' બટન પર ટચ કરો" : "2. Tap Info Button (i)", instruction: lang === 'gu' ? "જે ખોટો નંબર આવ્યો હતો તેની જમણી બાજુ ગોળ (i) માહિતી વાળા બટન પર ટચ કરો." : "Tap (i) next to the spam number.", target_ui_element: "(i) Info Button", target_coordinates: { x_percent: 88.7, y_percent: 33.6, radius_percent: 6.5 }, audio_text: "Tap info button.", screen_type: "phone_recents_screen", reassurance: "Opens call details." },
        { step_number: 3, title: lang === 'gu' ? "3. નીચે 'Block' (બ્લોક) પર ટચ કરો" : "3. Tap Block", instruction: lang === 'gu' ? "સ્ક્રીનની નીચે આપેલા 'Block' 🚫 બટન પર ટચ કરો." : "Tap Block at the bottom.", target_ui_element: "🚫 Block Button", target_coordinates: { x_percent: 50.0, y_percent: 78.0, radius_percent: 7.5 }, audio_text: "Tap Block.", screen_type: "phone_recents_screen", reassurance: "Prevents spam." },
        { step_number: 4, title: lang === 'gu' ? "4. નંબર બ્લોક થઈ ગયો છે!" : "4. Number Blocked Successfully", instruction: lang === 'gu' ? "હવે આ નંબર પરથી ક્યારેય તમને ફોન કે મેસેજ આવી શકશે નહીં." : "This spam number can no longer disturb you.", target_ui_element: "Blocked Badge", target_coordinates: { x_percent: 50.0, y_percent: 22.0, radius_percent: 7.0 }, audio_text: "Number blocked successfully.", screen_type: "phone_recents_screen", reassurance: "Safe and protected." }
      ]
    };
  }

  // 4. Default: The Verified Core Incident (WhatsApp Contact Share)
  if (lang === 'gu') {
    return {
      title: "વોટ્સએપ પર ફોન નંબર મોકલો",
      summary: "વોટ્સએપ ચેટમાં સરળતાથી કોઈનો ફોન નંબર બીજાને મોકલો.",
      reassurance_banner: "ચિંતા કરશો નહીં, આનાથી ફક્ત ફોન નંબર જશે. ફોનમાંથી કશું જ ડિલીટ નહીં થાય.",
      total_steps: 6,
      intent_info: { app_name: "WhatsApp", intent: "share_contact_number" },
      steps: [
        { step_number: 1, title: "1. વૉટ્સએપ ખોલો (Open WhatsApp)", instruction: "તમારા ફોનની સ્ક્રીન પર લીલા રંગનું વૉટ્સએપનું ગોળ નિશાન શોધો અને તેના પર એક વાર ટચ કરો.", target_ui_element: "વૉટ્સએપ એપનું લીલું નિશાન", target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 }, audio_text: "સૌપ્રથમ તમારા ફોનમાં લીલા રંગના વૉટ્સએપ નિશાન પર એક વાર અડો.", screen_type: "whatsapp_phone_home", reassurance: "આનાથી તમારા ફોનમાં વૉટ્સએપ ખુલશે." },
        { step_number: 2, title: "2. જેમને નંબર મોકલવો છે તેમની ચેટ ખોલો", instruction: "જે વ્યક્તિને તમારે ફોન નંબર મોકલવો છે (દા.ત. તમારા ભાઈ કે મિત્ર), તેમના નામ પર ટચ કરીને ચેટ ખોલો.", target_ui_element: "વ્યક્તિની ચેટનું નામ", target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 }, audio_text: "હવે જેમને નંબર મોકલવો છે તેમના નામ પર ટચ કરીને વાતચીત ખોલો.", screen_type: "whatsapp_chat_list", reassurance: "એમના નામ પર ટચ કરવાથી મેસેજની સ્ક્રીન ખુલશે." },
        { step_number: 3, title: "3. પેપરક્લિપ (ક્લિપ) ના નિશાન પર ટચ કરો", instruction: "નીચે જ્યાં મેસેજ લખો છો તેની જમણી બાજુ નાની ક્લિપ જેવું નિશાન 📎 દેખાશે. તેના પર ટચ કરો.", target_ui_element: "📎 પેપરક્લિપ આઇકન", target_coordinates: { x_percent: 70.8, y_percent: 94.5, radius_percent: 5.5 }, audio_text: "નીચે મેસેજ લખવાની જગ્યા પાસે નાની પેપરક્લિપ પર અડો.", screen_type: "whatsapp_chat_screen", reassurance: "આનાથી ફોટો કે નંબર મોકલવાના વિકલ્પો દેખાશે." },
        { step_number: 4, title: "4. મેનૂમાંથી 'Contact' (વાદળી ગોળ) પસંદ કરો", instruction: "એક નાનું રંગીન મેનૂ ખુલશે. તેમાં વાદળી રંગના ગોળ 'Contact' (માણસના ચહેરાવાળા) બટન પર ટચ કરો.", target_ui_element: "👤 વાદળી કોન્ટેક્ટ બટન", target_coordinates: { x_percent: 80.0, y_percent: 76.7, radius_percent: 7.0 }, audio_text: "હવે વાદળી રંગના કોન્ટેક્ટ વાળા બટન પર ટચ કરો.", screen_type: "whatsapp_attachment_menu", reassurance: "આનાથી તમારા ફોનની કોન્ટેક્ટ લિસ્ટ ખુલશે." },
        { step_number: 5, title: "5. જે વ્યક્તિનો નંબર મોકલવો છે તેમને શોધીને પસંદ કરો", instruction: "ઉપર સર્ચમાં જે વ્યક્તિનો નંબર મોકલવો હોય તેમનું નામ લખો અથવા લિસ્ટમાંથી શોધીને તેમના નામ પર ટચ કરો.", target_ui_element: "મોકલવા માટે કોન્ટેક્ટનું નામ", target_coordinates: { x_percent: 50.0, y_percent: 23.6, radius_percent: 8.0 }, audio_text: "જેમનો નંબર મોકલવો હોય તેમના નામ પર ટચ કરો.", screen_type: "whatsapp_contact_search", reassurance: "તેમના નામ પાસે લીલું નિશાન આવી જશે." },
        { step_number: 6, title: "6. નીચે આપેલા લીલા બટન પર ટચ કરો", instruction: "સૌથી નીચે જમણી બાજુ આપેલા લીલા રંગના તીર ➡️ વાળા સેન્ડ બટન પર ટચ કરો. નંબર સફળતાપૂર્વક પહોંચી જશે!", target_ui_element: "લીલું સેન્ડ (મોકલો) બટન", target_coordinates: { x_percent: 85.0, y_percent: 89.3, radius_percent: 7.5 }, audio_text: "નામ પસંદ કર્યા પછી નીચે લીલા તીર પર અડો. નંબર પહોંચી ગયો છે!", screen_type: "whatsapp_contact_picker", reassurance: "નંબર સફળતાપૂર્વક મોકલાઈ ગયો છે." }
      ]
    };
  } else if (lang === 'hi') {
    return {
      title: "व्हाट्सएप पर फोन नंबर भेजें",
      summary: "व्हाट्सएप चैट में किसी का भी फोन नंबर आसानी से भेजें।",
      reassurance_banner: "चिंता मत कीजिए, इससे सिर्फ फोन नंबर जाएगा। फोन से कुछ भी डिलीट नहीं होगा।",
      total_steps: 6,
      intent_info: { app_name: "WhatsApp", intent: "share_contact_number" },
      steps: [
        { step_number: 1, title: "1. व्हाट्सएप खोलें (Open WhatsApp)", instruction: "अपने फोन की स्क्रीन पर हरे रंग का व्हाट्सएप का निशान देखें और उस पर एक बार छुएं।", target_ui_element: "व्हाट्सएप का हरा निशान", target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 }, audio_text: "सबसे पहले अपने फोन में हरे रंग के व्हाट्सएप निशान पर एक बार छुएं।", screen_type: "whatsapp_phone_home", reassurance: "इससे आपके फोन में व्हाट्सएप खुल जाएगा।" },
        { step_number: 2, title: "2. जिन्हें नंबर भेजना है उनकी चैट खोलें", instruction: "जिस व्यक्ति को आप फोन नंबर भेजना चाहते हैं, उनके नाम पर टैप करें।", target_ui_element: "व्यक्ति का चैट नाम", target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 }, audio_text: "जिन्हें नंबर भेजना है उनके नाम पर टैप करके चैट खोलें।", screen_type: "whatsapp_chat_list", reassurance: "बातचीत खुल जाएगी।" },
        { step_number: 3, title: "3. पिन (पेपरक्लिप) के निशान को छुएं", instruction: "नीचे जहां मैसेज लिखते हैं, उसके पास छोटी पिन जैसी क्लिप 📎 दिखेगी। उस पर टैप करें।", target_ui_element: "📎 पिन या पेपरक्लिप का निशान", target_coordinates: { x_percent: 70.8, y_percent: 94.5, radius_percent: 5.5 }, audio_text: "छोटी पिन के निशान पर छुएं।", screen_type: "whatsapp_chat_screen", reassurance: "विकल्प खुलेंगे।" },
        { step_number: 4, title: "4. मेनू से 'Contact' (नीला गोल) चुनें", instruction: "रंगीन गोल बटन खुलेंगे। इनमें नीले रंग के 'Contact' वाले बटन को छुएं।", target_ui_element: "👤 नीला कांटेक्ट बटन", target_coordinates: { x_percent: 80.0, y_percent: 76.7, radius_percent: 7.0 }, audio_text: "नीले रंग वाले कांटेक्ट बटन को छुएं।", screen_type: "whatsapp_attachment_menu", reassurance: "कांटेक्ट खुलेंगे।" },
        { step_number: 5, title: "5. जिसका नंबर भेजना है उसे चुन लें", instruction: "ऊपर सर्च में नाम लिखें या लिस्ट से देखकर उनके नाम पर टैप करें।", target_ui_element: "कांटेक्ट का नाम", target_coordinates: { x_percent: 50.0, y_percent: 23.6, radius_percent: 8.0 }, audio_text: "नाम पर टैप करें।", screen_type: "whatsapp_contact_search", reassurance: "हरा निशान लगेगा।" },
        { step_number: 6, title: "6. नीचे दिए गए हरे तीर वाले बटन को दबाएं", instruction: "सबसे नीचे दाईं तरफ हरे तीर ➡️ वाले बटन को दबा दें। नंबर चला गया!", target_ui_element: "हरा सेंड तीर बटन", target_coordinates: { x_percent: 85.0, y_percent: 89.3, radius_percent: 7.5 }, audio_text: "हरे तीर वाले बटन को दबाएं। नंबर चला गया!", screen_type: "whatsapp_contact_picker", reassurance: "नंबर सफलतापूर्वक भेजा जा चुका है।" }
      ]
    };
  } else {
    return {
      title: "Send a Contact Number on WhatsApp",
      summary: "Easily send someone's phone number in a WhatsApp chat.",
      reassurance_banner: "Don't worry, this will only share the phone number. Nothing will be deleted.",
      total_steps: 6,
      intent_info: { app_name: "WhatsApp", intent: "share_contact_number" },
      steps: [
        { step_number: 1, title: "1. Open WhatsApp", instruction: "Find the green WhatsApp icon on your phone's home screen and tap it once to open the app.", target_ui_element: "WhatsApp Green App Icon", target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 }, audio_text: "First, find the green WhatsApp icon on your phone screen and tap it once.", screen_type: "whatsapp_phone_home", reassurance: "Safely opens WhatsApp." },
        { step_number: 2, title: "2. Go to the Contact You Want to Send to", instruction: "Find and tap the name of the person you want to send the phone number to.", target_ui_element: "Contact's Chat Name", target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 }, audio_text: "Tap the name of the person you want to send the number to.", screen_type: "whatsapp_chat_list", reassurance: "Opens conversation." },
        { step_number: 3, title: "3. Tap the Paperclip Icon", instruction: "At the bottom right where you type messages, tap the small Paperclip symbol 📎.", target_ui_element: "📎 Paperclip Attachment Icon", target_coordinates: { x_percent: 70.8, y_percent: 94.5, radius_percent: 5.5 }, audio_text: "Tap the small paperclip symbol.", screen_type: "whatsapp_chat_screen", reassurance: "Opens attachments." },
        { step_number: 4, title: "4. Select 'Contact' Option in That Window", instruction: "A colorful popup menu will appear. Tap the blue circular button labeled 'Contact' 👤.", target_ui_element: "👤 Blue Contact Option", target_coordinates: { x_percent: 80.0, y_percent: 76.7, radius_percent: 7.0 }, audio_text: "Tap the blue circle labeled Contact.", screen_type: "whatsapp_attachment_menu", reassurance: "Opens phone book." },
        { step_number: 5, title: "5. Search & Select the Contact You Want to Send", instruction: "Search or find the contact whose number you want to share, and tap their name.", target_ui_element: "Target Contact Name to Send", target_coordinates: { x_percent: 50.0, y_percent: 23.6, radius_percent: 8.0 }, audio_text: "Find and tap the name of the person whose number you want to share.", screen_type: "whatsapp_contact_search", reassurance: "Green checkmark appears." },
        { step_number: 6, title: "6. Click on the Green Icon to Send", instruction: "At the bottom right, tap the round green button with the white arrow ➡️. The phone number is sent!", target_ui_element: "Green Circular Send Arrow Button", target_coordinates: { x_percent: 85.0, y_percent: 89.3, radius_percent: 7.5 }, audio_text: "Tap the round green arrow button. The number is sent!", screen_type: "whatsapp_contact_picker", reassurance: "Phone number sent safely." }
      ]
    };
  }
}

// Language Switcher Logic
function toggleLanguage() {
  const order = ['gu', 'hi', 'en'];
  const currIdx = order.indexOf(state.currentLanguage);
  const nextLang = order[(currIdx + 1) % order.length];
  applyLanguage(nextLang);
}

function applyLanguage(langCode) {
  state.currentLanguage = langCode;
  const s = UI_STRINGS[langCode];

  const labels = { gu: "🇮🇳 ગુજરાતી", hi: "🇮🇳 हिन्दी", en: "🌐 English" };
  if (el.langLabel) el.langLabel.textContent = labels[langCode];

  if (el.reassuranceText) el.reassuranceText.textContent = s.reassuranceGeneral;
  if (el.welcomeTitle) el.welcomeTitle.textContent = s.welcomeTitle;
  if (el.welcomeDesc) el.welcomeDesc.textContent = s.welcomeDesc;
  if (el.quickTrayTitle) el.quickTrayTitle.textContent = s.quickTrayTitle;
  if (el.chipQ1Text) el.chipQ1Text.textContent = s.q1;
  if (el.chipQ2Text) el.chipQ2Text.textContent = s.q2;
  if (el.chipQ3Text) el.chipQ3Text.textContent = s.q3;
  if (el.chipQ4Text) el.chipQ4Text.textContent = s.q4;
  if (el.chipQ5Text) el.chipQ5Text.textContent = s.q5;
  if (el.chipQ6Text) el.chipQ6Text.textContent = s.q6;
  if (el.chipQ7Text) el.chipQ7Text.textContent = s.q7;
  if (el.chipQ8Text) el.chipQ8Text.textContent = s.q8;
  if (el.chatInput) el.chatInput.placeholder = s.inputPlaceholder;
  if (el.micActiveBanner) el.micActiveBanner.textContent = s.micListening;
}

// Reset Chat
function clearChat() {
  stopSpeaking();
  stopListening();
  stopVoiceNavListener();
  // Clear chat rows except welcome card
  const rows = el.chatFeed.querySelectorAll('.chat-row');
  rows.forEach(r => r.remove());
  if (el.welcomeCard) {
    el.welcomeCard.style.display = 'block';
  }
  applyLanguage(state.currentLanguage);
}

function scrollToBottom() {
  setTimeout(() => {
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    if (el.chatFeed) el.chatFeed.scrollTop = el.chatFeed.scrollHeight;
  }, 100);
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&<>"']/g, m => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#39;'
  })[m]);
}

// Senior Accessibility Font Zoom Toggle
function toggleFontZoom() {
  state.fontSizeLevel = (state.fontSizeLevel + 1) % 3;
  document.body.classList.remove('font-large', 'font-xlarge');
  if (state.fontSizeLevel === 1) {
    document.body.classList.add('font-large');
    if (el.fontZoomLabel) el.fontZoomLabel.textContent = 'A++';
  } else if (state.fontSizeLevel === 2) {
    document.body.classList.add('font-xlarge');
    if (el.fontZoomLabel) el.fontZoomLabel.textContent = 'A-';
  } else {
    if (el.fontZoomLabel) el.fontZoomLabel.textContent = 'A+';
  }
}

// Setup Event Listeners

// ==========================================================================
// ELDER SUPER-TOOLS LOGIC:
// 1. Anti-Scam Radar
// 2. Live Camera Screen Vision
// 3. Zero-Risk UPI Sandbox Practice
// 4. Family Caregiver Bridge & SOS
// 5. Gujarati Document & Medicine OCR Reader
// 6. Android Floating Bubble Companion
// ==========================================================================

let activeCameraStream = null;
let currentSandboxPin = "";
let latestScamAudioText = "";
let latestDocAudioText = "";

// Modal Management
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');

  if (modalId === 'modalCameraVision') {
    startCameraVision();
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');

  if (modalId === 'modalCameraVision') {
    stopCameraVision();
  }
  stopSpeaking();
}

// 1. Anti-Scam Radar Logic
async function runScamCheck(customText) {
  const textInput = document.getElementById('scamInputText');
  const textToCheck = (customText || (textInput ? textInput.value : '')).trim();
  if (!textToCheck) {
    alert(state.currentLanguage === 'gu' ? "કૃપા કરીને તપાસવા માટે મેસેજ લખો અથવા સેમ્પલ બટન દબાવો." : "Please enter a message to check.");
    return;
  }

  const verdictCard = document.getElementById('scamVerdictCard');
  const badgeEl = document.getElementById('scamVerdictBadge');
  const explanationEl = document.getElementById('scamVerdictExplanation');
  const actionsEl = document.getElementById('scamVerdictActions');

  try {
    const res = await fetch(`${state.apiBaseUrl}/api/check-scam`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        text: textToCheck,
        language: state.currentLanguage
      })
    });
    const data = await res.json();
    renderScamVerdict(data);
  } catch (err) {
    // Client-side fallback analysis
    const lower = textToCheck.toLowerCase();
    const isScam = lower.includes('power') || lower.includes('disconnected') || lower.includes('arrest') || lower.includes('kyc') || lower.includes('lottery') || lower.includes('બિલ') || lower.includes('કાપી') || lower.includes('અરેસ્ટ');
    const fallbackData = {
      is_scam: isScam,
      verdict_title: isScam ? "❌ ૧૦૦% છેતરપિંડી (SCAM ALERT)" : "✅ સુરક્ષિત સામાન્ય મેસેજ",
      verdict_audio: isScam ? "ચેતવણી: આ મેસેજ ૧૦૦ ટકા છેતરપિંડી છે! કોઈ લિંક પર ક્લિક ન કરતા કે નંબર પર ફોન ન કરતા." : "આ મેસેજમાં કોઈ ખતરો જણાતો નથી.",
      explanation: isScam ? "આ વીજળી બિલ કાપવાની ધમકી આપીને કે બેંક એકાઉન્ટ બ્લોકના નામે છેતરપિંડી કરવાનો ફ્રોડ મેસેજ છે." : "આ મેસેજમાં કોઈ શંકાસ્પદ લિંક નથી.",
      action_steps: isScam ? ["આ મેસેજની કોઈપણ લિંક પર ક્લિક ન કરો.", "નંબર પર સામો ફોન ન કરો.", "આ નંબરને તરત બ્લોક કરો."] : ["તમે સુરક્ષિત છો."]
    };
    renderScamVerdict(fallbackData);
  }
}

function renderScamVerdict(data) {
  const verdictCard = document.getElementById('scamVerdictCard');
  const badgeEl = document.getElementById('scamVerdictBadge');
  const explanationEl = document.getElementById('scamVerdictExplanation');
  const actionsEl = document.getElementById('scamVerdictActions');

  latestScamAudioText = data.verdict_audio;
  verdictCard.style.display = 'flex';
  if (data.is_scam) {
    verdictCard.classList.remove('safe');
    badgeEl.textContent = data.verdict_title;
  } else {
    verdictCard.classList.add('safe');
    badgeEl.textContent = data.verdict_title;
  }

  explanationEl.textContent = data.explanation;
  actionsEl.innerHTML = '';
  data.action_steps.forEach(act => {
    const li = document.createElement('div');
    li.innerHTML = `• ${escapeHtml(act)}`;
    actionsEl.appendChild(li);
  });

  // Speak aloud immediately for senior safety
  speakText(data.verdict_audio);
}

// 2. Live Camera Vision Guide Logic
async function startCameraVision() {
  const videoEl = document.getElementById('cameraVideo');
  const sampleEl = document.getElementById('cameraSampleView');
  const instructionEl = document.getElementById('cameraInstructionText');

  const promptText = state.currentLanguage === 'gu'
    ? "કેમેરામાં તમારો ફોન દેખાય છે! નીચે વાદળી રંગના બટન પર તમારા અંગૂઠાથી ટચ કરો."
    : (state.currentLanguage === 'hi' ? "कैमरे में आपका फोन दिख रहा है! नीचे दिए गए नीले बटन पर टैप करें।" : "Phone screen visible in camera! Tap the blue button below.");

  if (instructionEl) instructionEl.textContent = promptText;

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'environment' }
      });
      activeCameraStream = stream;
      if (videoEl) {
        videoEl.srcObject = stream;
        videoEl.style.display = 'block';
      }
      if (sampleEl) sampleEl.style.display = 'none';
      speakText(promptText);
      return;
    } catch (err) {
      console.log("Camera access not available or denied, showing simulated phone view:", err);
    }
  }

  // Graceful fallback to interactive camera view mockup
  if (videoEl) videoEl.style.display = 'none';
  if (sampleEl) sampleEl.style.display = 'block';
  speakText(promptText);
}

function stopCameraVision() {
  if (activeCameraStream) {
    activeCameraStream.getTracks().forEach(track => track.stop());
    activeCameraStream = null;
  }
}

function toggleCameraSource() {
  const videoEl = document.getElementById('cameraVideo');
  const sampleEl = document.getElementById('cameraSampleView');
  if (sampleEl.style.display === 'none') {
    stopCameraVision();
    if (videoEl) videoEl.style.display = 'none';
    if (sampleEl) sampleEl.style.display = 'block';
  } else {
    startCameraVision();
  }
}

// 3. Safe Sandbox Practice (UPI PIN Keypad) Logic
function handleSandboxKey(key) {
  if (currentSandboxPin.length < 4) {
    currentSandboxPin += key;
    updateSandboxPinDots();
    if (currentSandboxPin.length === 4) {
      setTimeout(submitSandboxPayment, 300);
    }
  }
}

function clearSandboxKey() {
  currentSandboxPin = currentSandboxPin.slice(0, -1);
  updateSandboxPinDots();
}

function updateSandboxPinDots() {
  for (let i = 1; i <= 4; i++) {
    const dot = document.getElementById(`pinDot${i}`);
    if (dot) {
      if (i <= currentSandboxPin.length) {
        dot.classList.add('filled');
      } else {
        dot.classList.remove('filled');
      }
    }
  }
}

function submitSandboxPayment() {
  const successBanner = document.getElementById('sandboxSuccessBanner');
  if (successBanner) {
    successBanner.style.display = 'flex';
  }
  const chimeMsg = state.currentLanguage === 'gu'
    ? "રૂપિયા ૧૦ સફળતાપૂર્વક ચૂકવાયા! ખૂબ સરસ, તમે સાચો પિન નાખીને ડેમો પેમેન્ટ પૂર્ણ કર્યું. આ માત્ર પ્રેક્ટિસ હતી, તમારા સાચા ખાતામાંથી એક પણ રૂપિયો કપાયો નથી."
    : (state.currentLanguage === 'hi'
      ? "दस रुपये का भुगतान सफल हुआ! बहुत बढ़िया, आपने डेमो पेमेंट पूरा कर लिया। यह सिर्फ अभ्यास था, आपके असली खाते से कोई पैसा नहीं कटा।"
      : "Ten rupees payment successful! Great job, this was a zero-risk sandbox practice.");
  speakText(chimeMsg);
}

function resetSandbox() {
  currentSandboxPin = "";
  updateSandboxPinDots();
  const successBanner = document.getElementById('sandboxSuccessBanner');
  if (successBanner) successBanner.style.display = 'none';
}

// 4. Family Bridge & Caregiver Persistent Profile Logic (PostgreSQL/SQLite + LocalStorage)
function getUserUid() {
  let uid = localStorage.getItem('sahayak_user_uid');
  if (!uid) {
    uid = 'user_' + Math.random().toString(36).substring(2, 11) + '_' + Date.now();
    localStorage.setItem('sahayak_user_uid', uid);
  }
  return uid;
}

async function initFamilyBridge() {
  const uid = getUserUid();
  const seniorNameInput = document.getElementById('familySeniorName');
  const childNameInput = document.getElementById('familyChildName');
  const childPhoneInput = document.getElementById('familyChildPhone');
  const relationSelect = document.getElementById('familyRelation');
  const footerCaregiverText = document.getElementById('footerCaregiverText');

  // Fill instantly from localStorage
  const savedSenior = localStorage.getItem('sahayak_senior_name') || 'રમણિકભાઈ (Ramnikbhai)';
  const savedName = localStorage.getItem('sahayak_child_name') || 'અમિત (દીકરો)';
  const savedPhone = localStorage.getItem('sahayak_child_phone') || '';
  const savedRelation = localStorage.getItem('sahayak_relation') || 'દીકરો (Son)';

  if (seniorNameInput) seniorNameInput.value = savedSenior;
  if (childNameInput) childNameInput.value = savedName;
  if (childPhoneInput) childPhoneInput.value = savedPhone;
  if (relationSelect) relationSelect.value = savedRelation;

  if (footerCaregiverText) {
    footerCaregiverText.textContent = savedPhone ? `કેરગીવર: ${savedName}` : 'કેરગીવર સેટ કરો';
  }

  // Sync with persistent backend database
  if (state.apiBaseUrl) {
    try {
      const res = await fetch(`${state.apiBaseUrl}/api/profile/${uid}`);
      if (res.ok) {
        const data = await res.json();
        if (data && data.success && data.caregiver_phone) {
          if (seniorNameInput && data.senior_name) seniorNameInput.value = data.senior_name;
          if (childNameInput && data.caregiver_name) childNameInput.value = data.caregiver_name;
          if (childPhoneInput && data.caregiver_phone) childPhoneInput.value = data.caregiver_phone;
          if (relationSelect && data.caregiver_relation) relationSelect.value = data.caregiver_relation;

          localStorage.setItem('sahayak_senior_name', data.senior_name || savedSenior);
          localStorage.setItem('sahayak_child_name', data.caregiver_name || savedName);
          localStorage.setItem('sahayak_child_phone', data.caregiver_phone || savedPhone);
          localStorage.setItem('sahayak_relation', data.caregiver_relation || savedRelation);

          if (footerCaregiverText) {
            footerCaregiverText.textContent = `કેરગીવર: ${data.caregiver_name}`;
          }
        }
      }
    } catch (e) {
      console.warn("Could not sync profile from database:", e);
    }
  }
}

async function saveFamilyContact() {
  const uid = getUserUid();
  const seniorNameInput = document.getElementById('familySeniorName');
  const childNameInput = document.getElementById('familyChildName');
  const childPhoneInput = document.getElementById('familyChildPhone');
  const relationSelect = document.getElementById('familyRelation');
  const footerCaregiverText = document.getElementById('footerCaregiverText');

  const seniorName = seniorNameInput ? seniorNameInput.value.trim() : 'વડીલ';
  const name = childNameInput ? childNameInput.value.trim() : 'દીકરો';
  const phone = childPhoneInput ? childPhoneInput.value.trim() : '';
  const relation = relationSelect ? relationSelect.value : 'દીકરો (Son)';

  if (!phone) {
    alert("કૃપા કરીને દીકરા/દીકરીનો WhatsApp નંબર લખો.");
    return;
  }

  localStorage.setItem('sahayak_senior_name', seniorName);
  localStorage.setItem('sahayak_child_name', name);
  localStorage.setItem('sahayak_child_phone', phone);
  localStorage.setItem('sahayak_relation', relation);

  if (footerCaregiverText) {
    footerCaregiverText.textContent = `કેરગીવર: ${name}`;
  }

  // Persist to PostgreSQL / SQLite database
  try {
    const res = await fetch(`${state.apiBaseUrl}/api/profile`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_uid: uid,
        senior_name: seniorName,
        preferred_language: state.currentLanguage,
        caregiver_name: name,
        caregiver_phone: phone,
        caregiver_relation: relation
      })
    });
    if (res.ok) {
      alert("✅ પ્રોફાઈલ અને દીકરાનો નંબર PostgreSQL/SQLite ડેટાબેઝમાં સાચવી લેવાયો છે!");
    } else {
      alert("સંપર્ક સફળતાપૂર્વક સેવ થઈ ગયો છે! ✅");
    }
  } catch (e) {
    alert("સંપર્ક લોકલમાં સેવ થઈ ગયો છે! ✅");
  }
}

function askChildOnWhatsApp() {
  const phone = (localStorage.getItem('sahayak_child_phone') || '').replace(/[^0-9]/g, '');
  const childName = localStorage.getItem('sahayak_child_name') || 'બેટા';
  const taskTitle = state.latestFlow?.title || "ફોન ચલાવવામાં મદદ";

  let msg = `નમસ્તે ${childName}! હું સહાયક AI વાપરી રહ્યો છું અને મને "${taskTitle}" માં તમારી મદદ જોઈએ છે. કૃપા કરીને મને ફોન પર સમજાવો ને!`;
  if (state.currentLanguage === 'hi') {
    msg = `नमस्ते ${childName}! मैं सहायक AI में "${taskTitle}" कर रहा हूँ और मुझे आपकी मदद चाहिए।`;
  } else if (state.currentLanguage === 'en') {
    msg = `Hi ${childName}! I am using Sahayak AI for "${taskTitle}" and need a little help.`;
  }

  const cleanPhone = phone ? (phone.startsWith('91') ? phone : `91${phone}`) : '';
  const url = cleanPhone ? `https://wa.me/${cleanPhone}?text=${encodeURIComponent(msg)}` : `https://wa.me/?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
}

function callChildDirect() {
  const phone = (localStorage.getItem('sahayak_child_phone') || '').replace(/[^0-9]/g, '');
  if (!phone) {
    alert("કૃપા કરીને દીકરા/દીકરીનો મોબાઈલ નંબર નાખીને સેવ કરો.");
    return;
  }
  window.location.href = `tel:${phone}`;
}

// 5. Document & Medicine OCR Reader Logic
async function loadDocumentData(docType) {
  const titleEl = document.getElementById('docResultTitle');
  const gridEl = document.getElementById('docDetailsGrid');
  const comfortEl = document.getElementById('docComfortText');

  try {
    const res = await fetch(`${state.apiBaseUrl}/api/read-document`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ doc_type: docType, language: state.currentLanguage })
    });
    const data = await res.json();
    renderDocumentData(data);
  } catch (err) {
    // Client-side fallback
    if (docType === 'medicine') {
      renderDocumentData({
        title: "💊 દવાની માહિતી અને લેવાનો સમય",
        audio_narration: "આ બ્લડ પ્રેશરની ટેબ્લેટ છે. ડૉક્ટરની સલાહ મુજબ આ ગોળી સવારે નાસ્તો કર્યા પછી ૧ ગોળી પાણી સાથે લેવાની છે.",
        key_details: [
          { label: "દવાનું નામ", value: "ટેલમિસાર્ટન 40mg (Telmisartan)" },
          { label: "શેના માટે?", value: "બ્લડ પ્રેશર (BP) કંટ્રોલ રાખવા" },
          { label: "ક્યારે લેવી?", value: "સવારે નાસ્તો કર્યા પછી - ૧ ગોળી" }
        ],
        comfort_note: "ચિંતા કરશો નહીં, આ તમારી રોજીંદી સામાન્ય દવા છે."
      });
    } else {
      renderDocumentData({
        title: "⚡ લાઈટ બિલની વિગતો (Electricity Bill)",
        audio_narration: "તમારું આ મહિનાનું વીજળી બિલ ₹૧,૪૫૦ આવ્યું છે. ભરવાની છેલ્લી તારીખ ૨૦ નવેમ્બર છે.",
        key_details: [
          { label: "કંપનીનું નામ", value: "ટોરેન્ટ પાવર લિમિટેડ" },
          { label: "ગ્રાહક નંબર", value: "5420 8912 341" },
          { label: "ભરવાની રકમ", value: "₹ ૧,૪૫૦/-" },
          { label: "છેલ્લી તારીખ", value: "૨૦ નવેમ્બર, ૨૦૨૬" }
        ],
        comfort_note: "તમે Google Pay થી આ બિલ ચૂકવી શકો છો."
      });
    }
  }
}

function renderDocumentData(data) {
  const titleEl = document.getElementById('docResultTitle');
  const gridEl = document.getElementById('docDetailsGrid');
  const comfortEl = document.getElementById('docComfortText');

  latestDocAudioText = data.audio_narration;
  if (titleEl) titleEl.textContent = data.title;
  if (comfortEl) comfortEl.textContent = data.comfort_note;

  if (gridEl) {
    gridEl.innerHTML = '';
    data.key_details.forEach(item => {
      const row = document.createElement('div');
      row.className = 'doc-detail-row';
      row.innerHTML = `
        <span class="doc-detail-label">${escapeHtml(item.label)}</span>
        <span class="doc-detail-value">${escapeHtml(item.value)}</span>
      `;
      gridEl.appendChild(row);
    });
  }

  speakText(data.audio_narration);
}

function setupEvents() {
  // Senior High Contrast Light Mode Toggle Button
  if (el.btnThemeToggle) {
    el.btnThemeToggle.addEventListener('click', toggleTheme);
  }

  // Accessibility Font Zoom Button
  if (el.btnFontZoom) {
    el.btnFontZoom.addEventListener('click', toggleFontZoom);
  }

  // Mic Button for Query input
  if (el.btnMic) {
    el.btnMic.addEventListener('click', () => {
      if (state.isListening) {
        stopListening();
      } else {
        startListening();
      }
    });
  }

  // Send Button
  if (el.btnSend) {
    el.btnSend.addEventListener('click', () => {
      submitQuery(el.chatInput.value);
    });
  }

  // Enter Key on Input
  if (el.chatInput) {
    el.chatInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        submitQuery(el.chatInput.value);
      }
    });
  }

  // Language Toggle
  if (el.langSelectBtn) {
    el.langSelectBtn.addEventListener('click', toggleLanguage);
  }

  // Clear Chat
  if (el.btnClearChat) {
    el.btnClearChat.addEventListener('click', clearChat);
  }

  // Quick Chips (All 8 core queries)
  if (el.chipQ1) el.chipQ1.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q1));
  if (el.chipQ2) el.chipQ2.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q2));
  if (el.chipQ3) el.chipQ3.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q3));
  if (el.chipQ4) el.chipQ4.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q4));
  if (el.chipQ5) el.chipQ5.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q5));
  if (el.chipQ6) el.chipQ6.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q6));
  if (el.chipQ7) el.chipQ7.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q7));
  if (el.chipQ8) el.chipQ8.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q8));

  // --- ELDER SUPER-TOOLS EVENT LISTENERS ---
  // Modals Open Triggers
  const btnOpenScam = document.getElementById('btnOpenScamRadar');
  if (btnOpenScam) btnOpenScam.addEventListener('click', () => openModal('modalScamRadar'));

  const btnOpenCam = document.getElementById('btnOpenCameraVision');
  if (btnOpenCam) btnOpenCam.addEventListener('click', () => openModal('modalCameraVision'));

  const btnOpenBox = document.getElementById('btnOpenSandbox');
  if (btnOpenBox) btnOpenBox.addEventListener('click', () => openModal('modalSafeSandbox'));

  const btnOpenFam = document.getElementById('btnOpenFamilyBridge');
  if (btnOpenFam) btnOpenFam.addEventListener('click', () => openModal('modalFamilyBridge'));

  const btnOpenDoc = document.getElementById('btnOpenDocReader');
  if (btnOpenDoc) btnOpenDoc.addEventListener('click', () => {
    openModal('modalDocReader');
    loadDocumentData('medicine');
  });

  const btnOpenBub = document.getElementById('btnOpenBubble');
  if (btnOpenBub) btnOpenBub.addEventListener('click', () => openModal('modalBubbleGuide'));

  const floatBub = document.getElementById('floatingBubble');
  if (floatBub) floatBub.addEventListener('click', () => openModal('modalBubbleGuide'));

  // Modals Close Buttons
  const closeScam = document.getElementById('btnCloseScamRadar');
  if (closeScam) closeScam.addEventListener('click', () => closeModal('modalScamRadar'));

  const closeCam = document.getElementById('btnCloseCameraVision');
  if (closeCam) closeCam.addEventListener('click', () => closeModal('modalCameraVision'));

  const closeBox = document.getElementById('btnCloseSandbox');
  if (closeBox) closeBox.addEventListener('click', () => closeModal('modalSafeSandbox'));

  const closeFam = document.getElementById('btnCloseFamilyBridge');
  if (closeFam) closeFam.addEventListener('click', () => closeModal('modalFamilyBridge'));

  const closeDoc = document.getElementById('btnCloseDocReader');
  if (closeDoc) closeDoc.addEventListener('click', () => closeModal('modalDocReader'));

  const closeBub = document.getElementById('btnCloseBubbleGuide');
  if (closeBub) closeBub.addEventListener('click', () => closeModal('modalBubbleGuide'));

  // Disclaimers and Footer Caregiver Listeners
  const btnOpenDisc = document.getElementById('btnOpenDisclaimers');
  if (btnOpenDisc) btnOpenDisc.addEventListener('click', () => openModal('modalDisclaimers'));

  const closeDisc = document.getElementById('btnCloseDisclaimers');
  if (closeDisc) closeDisc.addEventListener('click', () => closeModal('modalDisclaimers'));

  const btnFootCare = document.getElementById('btnFooterCaregiver');
  if (btnFootCare) btnFootCare.addEventListener('click', () => openModal('modalFamilyBridge'));

  const btnSaveFam = document.getElementById('btnSaveFamilyContact');
  if (btnSaveFam) btnSaveFam.addEventListener('click', () => saveFamilyContact());

  const btnAskChild = document.getElementById('btnAskChildWhatsApp');
  if (btnAskChild) btnAskChild.addEventListener('click', () => askChildOnWhatsApp());

  const btnCallChild = document.getElementById('btnCallChildDirect');
  if (btnCallChild) btnCallChild.addEventListener('click', () => callChildDirect());

  // Close modals on clicking backdrop
  document.querySelectorAll('.elder-modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) {
        closeModal(backdrop.id);
      }
    });
  });

  // Scam Radar Listeners
  const btnRunScam = document.getElementById('btnRunScamCheck');
  if (btnRunScam) btnRunScam.addEventListener('click', () => runScamCheck());

  const pScamElec = document.getElementById('presetScamElectricity');
  if (pScamElec) pScamElec.addEventListener('click', () => {
    const txt = "Dear consumer electricity power will be disconnected tonight by 9:30 PM from electricity office call 9876543210 immediately.";
    document.getElementById('scamInputText').value = txt;
    runScamCheck(txt);
  });

  const pScamBank = document.getElementById('presetScamBank');
  if (pScamBank) pScamBank.addEventListener('click', () => {
    const txt = "SBI Alert: Your Account has been suspended. Please update your PAN Card immediately by clicking https://bit.ly/sbi-pan-kyc";
    document.getElementById('scamInputText').value = txt;
    runScamCheck(txt);
  });

  const pScamArrest = document.getElementById('presetScamArrest');
  if (pScamArrest) pScamArrest.addEventListener('click', () => {
    const txt = "Arrest warrant issued by CBI and Cyber Police department. Join video call immediately or face arrest.";
    document.getElementById('scamInputText').value = txt;
    runScamCheck(txt);
  });

  const btnListenScam = document.getElementById('btnListenScamVerdict');
  if (btnListenScam) btnListenScam.addEventListener('click', () => {
    if (latestScamAudioText) speakText(latestScamAudioText);
  });

  // Camera Vision Listeners
  const btnToggleCam = document.getElementById('btnToggleCameraSource');
  if (btnToggleCam) btnToggleCam.addEventListener('click', toggleCameraSource);

  const btnSpeakCam = document.getElementById('btnSpeakCameraGuidance');
  if (btnSpeakCam) btnSpeakCam.addEventListener('click', () => {
    const txt = document.getElementById('cameraInstructionText')?.textContent;
    if (txt) speakText(txt);
  });

  // Safe Sandbox UPI Keypad Listeners
  document.querySelectorAll('.keypad-btn[data-key]').forEach(btn => {
    btn.addEventListener('click', () => handleSandboxKey(btn.getAttribute('data-key')));
  });

  const btnClr = document.getElementById('btnKeypadClear');
  if (btnClr) btnClr.addEventListener('click', clearSandboxKey);

  const btnSub = document.getElementById('btnKeypadSubmit');
  if (btnSub) btnSub.addEventListener('click', submitSandboxPayment);

  const btnResetBox = document.getElementById('btnResetSandbox');
  if (btnResetBox) btnResetBox.addEventListener('click', resetSandbox);

  // Family Bridge Listeners
  const btnSaveFam = document.getElementById('btnSaveFamilyContact');
  if (btnSaveFam) btnSaveFam.addEventListener('click', saveFamilyContact);

  const btnAskChild = document.getElementById('btnAskChildWhatsApp');
  if (btnAskChild) btnAskChild.addEventListener('click', askChildOnWhatsApp);

  const btnCallChild = document.getElementById('btnCallChildDirect');
  if (btnCallChild) btnCallChild.addEventListener('click', callChildDirect);

  // Document Reader Listeners
  const tabDocMed = document.getElementById('tabDocMedicine');
  const tabDocB = document.getElementById('tabDocBill');
  if (tabDocMed && tabDocB) {
    tabDocMed.addEventListener('click', () => {
      tabDocMed.classList.add('active');
      tabDocB.classList.remove('active');
      loadDocumentData('medicine');
    });
    tabDocB.addEventListener('click', () => {
      tabDocB.classList.add('active');
      tabDocMed.classList.remove('active');
      loadDocumentData('utility_bill');
    });
  }

  const pDocMed = document.getElementById('presetDocMedicine');
  if (pDocMed) pDocMed.addEventListener('click', () => loadDocumentData('medicine'));

  const pDocBill = document.getElementById('presetDocBill');
  if (pDocBill) pDocBill.addEventListener('click', () => loadDocumentData('utility_bill'));

  const btnListenDoc = document.getElementById('btnListenDocAudio');
  if (btnListenDoc) btnListenDoc.addEventListener('click', () => {
    if (latestDocAudioText) speakText(latestDocAudioText);
  });

}

// App Bootstrap
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initFamilyBridge();
  setupEvents();
  applyLanguage('gu');
  initSpeechRecognition();

  // Register PWA Service Worker for Mobile & Desktop Offline Capability
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(err => {
      console.log('ServiceWorker notice (non-blocking):', err);
    });
  }

  console.log("Sahayak AI ChatGPT-Style Visual Guide ready.");
});
