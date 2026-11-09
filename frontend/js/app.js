/**
 * Sahayak AI: Systematic Step-by-Step Visual Guide
 * Conversational Feed Engine with Photos Embedded Below Every Step
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
  fontSizeLevel: 0 // 0: normal, 1: large (A++), 2: xlarge (A-)
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
    finishBannerDesc: "આ બધા પગલાં અનુસર્યા પછી તમારો ફોન નંબર સરળતાથી મોકલાઈ જશે.",
    copiedToast: "લિંક કોપી થઈ ગઈ છે!",
    stepDoneBtn: "મેં આ કર્યું ✓",
    stepDoneCompleted: "પૂર્ણ થયું! ✅"
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
    stepDoneCompleted: "पूरा हुआ! ✅"
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
    finishBannerDesc: "Following these steps will safely complete your task on WhatsApp.",
    copiedToast: "Guide copied to clipboard!",
    stepDoneBtn: "Done with this step ✓",
    stepDoneCompleted: "Completed! ✅"
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
  gpay_home: "assets/screens/gpay_home.svg",
  scanner_camera: "assets/screens/gpay_scanner.svg",
  gpay_amount_screen: "assets/screens/gpay_amount.svg",
  android_home: "assets/screens/whatsapp_phone_home.svg",
  settings_list: "assets/screens/settings_home.svg",
  font_settings: "assets/screens/settings_home.svg",
  default_screen: "assets/screens/whatsapp_chat_screen.svg"
};

// DOM References
const el = {
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
  chipQ1Text: document.getElementById('chipQ1Text'),
  chipQ2Text: document.getElementById('chipQ2Text'),
  chipQ3Text: document.getElementById('chipQ3Text'),
  chipQ4Text: document.getElementById('chipQ4Text'),
  chatInput: document.getElementById('chatInput'),
  btnMic: document.getElementById('btnMic'),
  btnSend: document.getElementById('btnSend'),
  micActiveBanner: document.getElementById('micActiveBanner')
};

// Initialize Speech Recognition (STT)
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
    el.btnMic.classList.add('listening');
    el.micActiveBanner.classList.add('active');
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
  el.btnMic.classList.remove('listening');
  el.micActiveBanner.classList.remove('active');
}

// Text-to-Speech (TTS)
function speakText(textToSpeak, onEndCallback) {
  if (!state.speechSynth) return;
  state.speechSynth.cancel();

  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  utterance.rate = 0.82; // Patient, slow speed for elderly listeners
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

    if (!res.ok) throw new Error("API call failed");
    const flowData = await res.json();
    state.latestFlow = flowData;
    renderAiVisualGuide(flowData);
  } catch (err) {
    console.warn("Backend request failed, falling back to local preloaded flow:", err);
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

// Local Fallback Flow for 100% Reliable Offline Demonstration
function getLocalFallbackFlow(query) {
  const lang = state.currentLanguage;
  if (lang === 'gu') {
    return {
      title: "વોટ્સએપ પર ફોન નંબર મોકલો",
      summary: "વોટ્સએપ ચેટમાં સરળતાથી કોઈનો ફોન નંબર બીજાને મોકલો.",
      reassurance_banner: "ચિંતા કરશો નહીં, આનાથી ફક્ત ફોન નંબર જશે. ફોનમાંથી કશું જ ડિલીટ નહીં થાય.",
      total_steps: 6,
      intent_info: { app_name: "WhatsApp", intent: "share_contact_number" },
      steps: [
        {
          step_number: 1,
          title: "1. વૉટ્સએપ ખોલો (Open WhatsApp)",
          instruction: "તમારા ફોનની સ્ક્રીન પર લીલા રંગનું વૉટ્સએપનું ગોળ નિશાન શોધો અને તેના પર એક વાર ટચ કરો.",
          target_ui_element: "વૉટ્સએપ એપનું લીલું નિશાન",
          target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 },
          audio_text: "સૌપ્રથમ તમારા ફોનમાં લીલા રંગના વૉટ્સએપ નિશાન પર એક વાર અડો.",
          screen_type: "whatsapp_phone_home",
          reassurance: "આનાથી તમારા ફોનમાં વૉટ્સએપ ખુલશે."
        },
        {
          step_number: 2,
          title: "2. જેમને નંબર મોકલવો છે તેમની ચેટ ખોલો",
          instruction: "જે વ્યક્તિને તમારે ફોન નંબર મોકલવો છે (દા.ત. તમારા ભાઈ કે મિત્ર), તેમના નામ પર ટચ કરીને ચેટ ખોલો.",
          target_ui_element: "વ્યક્તિની ચેટનું નામ",
          target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 },
          audio_text: "હવે જેમને નંબર મોકલવો છે તેમના નામ પર ટચ કરીને વાતચીત ખોલો.",
          screen_type: "whatsapp_chat_list",
          reassurance: "એમના નામ પર ટચ કરવાથી મેસેજની સ્ક્રીન ખુલશે."
        },
        {
          step_number: 3,
          title: "3. પેપરક્લિપ (ક્લિપ) ના નિશાન પર ટચ કરો",
          instruction: "નીચે જ્યાં મેસેજ લખો છો તેની જમણી બાજુ નાની ક્લિપ જેવું નિશાન 📎 દેખાશે. તેના પર ટચ કરો.",
          target_ui_element: "📎 પેપરક્લિપ આઇકન",
          target_coordinates: { x_percent: 70.8, y_percent: 94.5, radius_percent: 5.5 },
          audio_text: "નીચે મેસેજ લખવાની જગ્યા પાસે નાની પેપરક્લિપ પર અડો.",
          screen_type: "whatsapp_chat_screen",
          reassurance: "આનાથી ફોટો કે નંબર મોકલવાના વિકલ્પો દેખાશે."
        },
        {
          step_number: 4,
          title: "4. મેનૂમાંથી 'Contact' (વાદળી ગોળ) પસંદ કરો",
          instruction: "એક નાનું રંગીન મેનૂ ખુલશે. તેમાં વાદળી રંગના ગોળ 'Contact' (માણસના ચહેરાવાળા) બટન પર ટચ કરો.",
          target_ui_element: "👤 વાદળી કોન્ટેક્ટ બટન",
          target_coordinates: { x_percent: 80.0, y_percent: 76.7, radius_percent: 7.0 },
          audio_text: "હવે વાદળી રંગના કોન્ટેક્ટ વાળા બટન પર ટચ કરો.",
          screen_type: "whatsapp_attachment_menu",
          reassurance: "આનાથી તમારા ફોનની કોન્ટેક્ટ લિસ્ટ ખુલશે."
        },
        {
          step_number: 5,
          title: "5. જે વ્યક્તિનો નંબર મોકલવો છે તેમને શોધીને પસંદ કરો",
          instruction: "ઉપર સર્ચમાં જે વ્યક્તિનો નંબર મોકલવો હોય તેમનું નામ લખો અથવા લિસ્ટમાંથી શોધીને તેમના નામ પર ટચ કરો.",
          target_ui_element: "મોકલવા માટે કોન્ટેક્ટનું નામ",
          target_coordinates: { x_percent: 50.0, y_percent: 23.6, radius_percent: 8.0 },
          audio_text: "જેમનો નંબર મોકલવો હોય તેમના નામ પર ટચ કરો.",
          screen_type: "whatsapp_contact_search",
          reassurance: "તેમના નામ પાસે લીલું નિશાન આવી જશે."
        },
        {
          step_number: 6,
          title: "6. નીચે આપેલા લીલા બટન પર ટચ કરો",
          instruction: "સૌથી નીચે જમણી બાજુ આપેલા લીલા રંગના તીર ➡️ વાળા સેન્ડ બટન પર ટચ કરો. નંબર સફળતાપૂર્વક પહોંચી જશે!",
          target_ui_element: "લીલું સેન્ડ (મોકલો) બટન",
          target_coordinates: { x_percent: 85.0, y_percent: 89.3, radius_percent: 7.5 },
          audio_text: "નામ પસંદ કર્યા પછી નીચે લીલા તીર પર અડો. નંબર પહોંચી ગયો છે!",
          screen_type: "whatsapp_contact_picker",
          reassurance: "નંબર સફળતાપૂર્વક મોકલાઈ ગયો છે."
        }
      ]
    };
  } else if (lang === 'hi') {
    return {
      title: "व्हाट्सएप पर फोन नंबर भेजें",
      summary: "व्हाट्सएप चैट में किसी का भी फोन नंबर आसानी से भेजें।",
      reassurance_banner: "चिंता मत कीजिए, इससे सिर्फ फोन नंबर जाएगा। फोन से कुछ भी डिलीટ नहीं होगा।",
      total_steps: 6,
      intent_info: { app_name: "WhatsApp", intent: "share_contact_number" },
      steps: [
        {
          step_number: 1,
          title: "1. व्हाट्सएप खोलें (Open WhatsApp)",
          instruction: "अपने फोन की स्क्रीन पर हरे रंग का व्हाट्सएप का निशान देखें और उस पर एक बार छुएं।",
          target_ui_element: "व्हाट्सएप का हरा निशान",
          target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 },
          audio_text: "सबसे पहले अपने फोन में हरे रंग के व्हाट्सएप निशान पर एक बार छुएं।",
          screen_type: "whatsapp_phone_home",
          reassurance: "इससे आपके फोन में व्हाट्सएप खुल जाएगा।"
        },
        {
          step_number: 2,
          title: "2. जिन्हें नंबर भेजना है उनकी चैट खोलें",
          instruction: "जिस व्यक्ति को आप फोन नंबर भेजना चाहते हैं (जैसे आपके भाई या दोस्त), उनके नाम पर टैप करें।",
          target_ui_element: "व्यक्ति का चैट नाम",
          target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 },
          audio_text: "जिन्हें नंबर भेजना है उनके नाम पर टैप करके चैट खोलें।",
          screen_type: "whatsapp_chat_list",
          reassurance: "उनके नाम पर टैप करने से बातचीत खुल जाएगी।"
        },
        {
          step_number: 3,
          title: "3. पिन (पेपरक्लिप) के निशान को छुएं",
          instruction: "नीचे जहां मैसेज लिखते हैं, उसके पास छोटी पिन जैसी क्लिप 📎 दिखेगी। उस पर टैप करें।",
          target_ui_element: "📎 पिन या पेपरक्लिप का निशान",
          target_coordinates: { x_percent: 70.8, y_percent: 94.5, radius_percent: 5.5 },
          audio_text: "नीचे जहां टाइप करते हैं, वहां छोटी पिन के निशान पर छुएं।",
          screen_type: "whatsapp_chat_screen",
          reassurance: "इससे नंबर और फोटो भेजने के विकल्प खुलेंगे।"
        },
        {
          step_number: 4,
          title: "4. मेनू से 'Contact' (नीला गोल) चुनें",
          instruction: "रंगीन गोल बटन खुलेंगे। इनमें नीले रंग के 'Contact' (आदमी का निशान) वाले बटन को छुएं।",
          target_ui_element: "👤 नीला कांटेक्ट बटन",
          target_coordinates: { x_percent: 80.0, y_percent: 76.7, radius_percent: 7.0 },
          audio_text: "अब नीले रंग वाले कांटेक्ट बटन को छुएं।",
          screen_type: "whatsapp_attachment_menu",
          reassurance: "इससे आपके फोन के सभी नंबर दिखेंगे।"
        },
        {
          step_number: 5,
          title: "5. जिसका नंबर भेजना है उसे चुन लें",
          instruction: "ऊपर सर्च में नाम लिखें या लिस्ट से देखकर जिसका नंबर भेजना है उनके नाम पर टैप करें।",
          target_ui_element: "कांटेक्ट का नाम",
          target_coordinates: { x_percent: 50.0, y_percent: 23.6, radius_percent: 8.0 },
          audio_text: "जिसका नंबर भेजना है उनके नाम पर टैप करें।",
          screen_type: "whatsapp_contact_search",
          reassurance: "उनके नाम के आगे हरा निशान लग जाएगा।"
        },
        {
          step_number: 6,
          title: "6. नीचे दिए गए हरे तीर वाले बटन को दबाएं",
          instruction: "सबसे नीचे दाईं तरफ हरे तीर ➡️ वाले बटन को दबा दें। नंबर चला गया!",
          target_ui_element: "हरा सेंड तीर बटन",
          target_coordinates: { x_percent: 85.0, y_percent: 89.3, radius_percent: 7.5 },
          audio_text: "नीचे हरे तीर वाले बटन को दबाएं। नंबर सफलतापूर्वक चला गया!",
          screen_type: "whatsapp_contact_picker",
          reassurance: "नंबर सफलतापूर्वक भेजा जा चुका है।"
        }
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
        {
          step_number: 1,
          title: "1. Open WhatsApp",
          instruction: "Find the green WhatsApp icon on your phone's home screen and tap it once to open the app.",
          target_ui_element: "WhatsApp Green App Icon",
          target_coordinates: { x_percent: 61.3, y_percent: 89.6, radius_percent: 7.5 },
          audio_text: "First, find the green WhatsApp icon on your phone screen and tap it once.",
          screen_type: "whatsapp_phone_home",
          reassurance: "This safely opens WhatsApp."
        },
        {
          step_number: 2,
          title: "2. Go to the Contact You Want to Send to",
          instruction: "Find and tap the name of the person you want to send the phone number to.",
          target_ui_element: "Contact's Chat Name",
          target_coordinates: { x_percent: 50.0, y_percent: 18.2, radius_percent: 7.5 },
          audio_text: "Tap the name of the person you want to send the number to.",
          screen_type: "whatsapp_chat_list",
          reassurance: "This opens your conversation."
        },
        {
          step_number: 3,
          title: "3. Tap the Paperclip Icon",
          instruction: "At the bottom right where you type messages, tap the small Paperclip symbol 📎.",
          target_ui_element: "📎 Paperclip Attachment Icon",
          target_coordinates: { x_percent: 70.8, y_percent: 94.5, radius_percent: 5.5 },
          audio_text: "At the bottom right, tap the small paperclip symbol.",
          screen_type: "whatsapp_chat_screen",
          reassurance: "This opens attachment options."
        },
        {
          step_number: 4,
          title: "4. Select 'Contact' Option in That Window",
          instruction: "A colorful popup menu will appear. Tap the blue circular button labeled 'Contact' 👤.",
          target_ui_element: "👤 Blue Contact Option",
          target_coordinates: { x_percent: 80.0, y_percent: 76.7, radius_percent: 7.0 },
          audio_text: "Tap the blue circle with the person symbol that says Contact.",
          screen_type: "whatsapp_attachment_menu",
          reassurance: "This opens your phone book."
        },
        {
          step_number: 5,
          title: "5. Search & Select the Contact You Want to Send",
          instruction: "Search or find the contact whose number you want to share, and tap their name.",
          target_ui_element: "Target Contact Name to Send",
          target_coordinates: { x_percent: 50.0, y_percent: 23.6, radius_percent: 8.0 },
          audio_text: "Find and tap the name of the person whose number you want to share.",
          screen_type: "whatsapp_contact_search",
          reassurance: "A green checkmark will appear next to their name."
        },
        {
          step_number: 6,
          title: "6. Click on the Green Icon to Send",
          instruction: "At the bottom right, tap the round green button with the white arrow ➡️. The phone number is sent!",
          target_ui_element: "Green Circular Send Arrow Button",
          target_coordinates: { x_percent: 85.0, y_percent: 89.3, radius_percent: 7.5 },
          audio_text: "Tap the round green arrow button at the bottom right. The number has been sent!",
          screen_type: "whatsapp_contact_picker",
          reassurance: "The phone number has been sent safely."
        }
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
  el.langLabel.textContent = labels[langCode];

  el.reassuranceText.textContent = s.reassuranceGeneral;
  el.welcomeTitle.textContent = s.welcomeTitle;
  el.welcomeDesc.textContent = s.welcomeDesc;
  el.quickTrayTitle.textContent = s.quickTrayTitle;
  el.chipQ1Text.textContent = s.q1;
  el.chipQ2Text.textContent = s.q2;
  el.chipQ3Text.textContent = s.q3;
  el.chipQ4Text.textContent = s.q4;
  el.chatInput.placeholder = s.inputPlaceholder;
  el.micActiveBanner.textContent = s.micListening;
}

// Reset Chat
function clearChat() {
  stopSpeaking();
  stopListening();
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
    el.chatFeed.scrollTop = el.chatFeed.scrollHeight;
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
function setupEvents() {
  // Accessibility Font Zoom Button
  if (el.btnFontZoom) {
    el.btnFontZoom.addEventListener('click', toggleFontZoom);
  }

  // Mic Button
  el.btnMic.addEventListener('click', () => {
    if (state.isListening) {
      stopListening();
    } else {
      startListening();
    }
  });

  // Send Button
  el.btnSend.addEventListener('click', () => {
    submitQuery(el.chatInput.value);
  });

  // Enter Key on Input
  el.chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      submitQuery(el.chatInput.value);
    }
  });

  // Language Toggle
  el.langSelectBtn.addEventListener('click', toggleLanguage);

  // Clear Chat
  el.btnClearChat.addEventListener('click', clearChat);

  // Quick Chips
  el.chipQ1.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q1));
  el.chipQ2.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q2));
  el.chipQ3.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q3));
  el.chipQ4.addEventListener('click', () => submitQuery(UI_STRINGS[state.currentLanguage].q4));
}

// App Bootstrap
document.addEventListener('DOMContentLoaded', () => {
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
