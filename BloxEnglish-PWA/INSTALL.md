# Blox English – instalación en iPhone (PWA)

## Cómo Alejandro la instala en su iPhone

1. **Subir esta carpeta a un hosting con HTTPS.** Tres opciones gratuitas:
   - **Netlify Drop** (la más fácil): abrí <https://app.netlify.com/drop> y arrastrá la carpeta `BloxEnglish-PWA/` completa. Te da una URL del tipo `random-name.netlify.app` al instante.
   - **GitHub Pages**: subir la carpeta a un repo público, Settings → Pages → Deploy from main.
   - **Cloudflare Pages / Vercel**: similar a Netlify.

2. **Abrir la URL en Safari del iPhone** (no en Chrome — solo Safari permite "Añadir a pantalla de inicio" en iOS).

3. Tocá el botón **Compartir** (cuadrado con flecha hacia arriba).

4. Bajá y tocá **Añadir a pantalla de inicio** / *Add to Home Screen*.

5. Confirmá el nombre **Blox English** y tocá **Añadir**.

## Resultado

- Aparece un icono en la pantalla de inicio del iPhone como una app más.
- Al abrirlo se muestra **a pantalla completa** (sin barra de Safari).
- La primera vez que la abre con internet, descarga todo y queda guardado.
- Después funciona **100% offline** — Alejandro puede usarla sin Wi-Fi ni datos.

## Para actualizar

Cuando edites `alejandro-blox-english-mobile.html`:

```bash
python build/build_pwa.py
```

Re-genera la carpeta. Volvé a subirla al mismo hosting (Netlify Drop te deja arrastrar de nuevo y reemplazar). El service worker detecta la versión nueva en la siguiente visita y la baja en background.

## Diferencias vs APK

| | APK (Android) | PWA (iPhone) |
|---|---|---|
| Cómo se instala | Pasar archivo + activar fuentes desconocidas | Compartir → Añadir a pantalla |
| Necesita internet | Solo para instalar | Solo la primera vez |
| Tamaño | ~85 KB | ~250 KB cacheado |
| Actualizaciones | Pasar nuevo APK | Automático (al abrir con red) |
