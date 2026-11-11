// Sahayak AI Offline Service Worker
const CACHE_NAME = 'sahayak-ai-v3';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/css/styles.css',
  '/js/app.js',
  '/manifest.json',
  '/favicon.svg',
  '/assets/logo.svg',
  '/assets/icons/pwa-icon.svg',
  '/assets/icons/icon-192.png',
  '/assets/icons/icon-512.png',
  '/assets/screens/whatsapp_phone_home.svg',
  '/assets/screens/whatsapp_chat_list.svg',
  '/assets/screens/whatsapp_chat_screen.svg',
  '/assets/screens/whatsapp_attachment_menu.svg',
  '/assets/screens/whatsapp_contact_search.svg',
  '/assets/screens/whatsapp_contact_picker.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).catch(err => console.log('Cache install non-blocking notice:', err))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Let /api/ calls bypass cache for live queries
  if (event.request.url.includes('/api/')) {
    return;
  }
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    }).catch(() => {
      return caches.match('/');
    })
  );
});

