# Listening Quiz — Deployment a GitHub Pages

Esta guía te lleva de cero a "los alumnos abren un link y sus respuestas llegan a mi Google Sheet" en ~20 minutos.

App: `listening-quiz.html` · 4 niveles (A2 · B1 · B2 · C1) · 40 preguntas por nivel · 160 ítems totales.

---

## Calibración CEFR

| Nivel | Fuente | Calibración | Audio |
|---|---|---|---|
| **A2** | Cambridge KET Tests 1-2 Listening Part 1 | A2 oficial Cambridge | TTS Edge Neural (Aria/Guy) |
| **B1** | Cambridge PET Tests 3 + 5 Listening Part 2 | B1 oficial Cambridge | TTS Edge Neural |
| **B2** | TOEFL Test 1 — listening section | B2/C1 (TOEFL ETS) | mp3 real |
| **C1** | TOEFL Test 2 — listening section | C1 (TOEFL ETS) | mp3 real |

🌟 **Importante**: para A2/B1 los alumnos deben abrir la app **en Microsoft Edge con internet** para que se carguen las voces neuronales (Aria, Guy, Jenny, Christopher). En otros navegadores funciona pero con voz robótica estándar.

---

## Paso 1 — Apps Script + Google Sheet (10 min)

### 1.1 Crear la Sheet
1. Drive → **Nuevo → Hoja de cálculo** → renombra a `Listening Responses 2026`.
2. Renombra la pestaña por defecto a `Responses`.
3. Pega esta fila como encabezados (fila 1):
   ```
   Timestamp	Name	Class	Level	Score	Total	Percent	Elapsed_min	Answers_JSON	Breakdown_JSON
   ```
   (separados por TAB; pégalos en A1 y se distribuyen solos)

### 1.2 Crear el Apps Script
En la misma Sheet → **Extensiones → Apps Script**.

Borra el código que está y pega:

```js
const SHEET_ID = "PEGA_AQUI_EL_ID_DE_TU_SHEET";  // ej: 1AbCd...XyZ (lo sacas de la URL de tu Sheet)
const SHEET_NAME = "Responses";

function doPost(e){
  try{
    const data = JSON.parse(e.parameter.data);
    const sheet = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
    const pct = data.total ? Math.round(100*data.score/data.total) : 0;
    sheet.appendRow([
      new Date(),
      data.name || "",
      data.klass || "",
      data.level || "",
      data.score || 0,
      data.total || 0,
      pct,
      data.elapsed_min || 0,
      JSON.stringify(data.answers || {}),
      JSON.stringify(data.breakdown || [])
    ]);
    return ContentService.createTextOutput("OK");
  } catch(err){
    return ContentService.createTextOutput("ERROR: " + err.message);
  }
}

function doGet(){
  return ContentService.createTextOutput("Listening Quiz endpoint OK");
}
```

**Cómo sacar el SHEET_ID**: en la URL de tu Sheet, está entre `/d/` y `/edit`:
`https://docs.google.com/spreadsheets/d/`**`AQUI_VA_EL_ID`**`/edit#gid=0`

### 1.3 Publicar como Web App
1. **Implementar → Nueva implementación**.
2. Icono engranaje → **Aplicación web**.
3. Descripción: `Listening Quiz endpoint`
4. **Ejecutar como:** Tú (tu Gmail).
5. **Quién tiene acceso:** **Cualquiera** ← clave (los alumnos no autenticarán con Google).
6. **Implementar** → autoriza permisos cuando lo pida.
7. **Copia la URL** del Web App (termina en `/exec`). Guárdala — la pegas en el Paso 2.

### 1.4 Prueba el endpoint
Abre la URL en una pestaña nueva. Debe decir: `Listening Quiz endpoint OK`. Si dice eso, está listo.

---

## Paso 2 — Pegar la URL del Apps Script en el HTML (1 min)

Abre `listening-quiz.html` y busca esta línea (cerca del inicio del `<script>`):

```js
APPS_SCRIPT_URL: "PEGA_AQUI_TU_URL_DEL_APPS_SCRIPT",
```

Reemplaza por tu URL:

```js
APPS_SCRIPT_URL: "https://script.google.com/macros/s/AKfy.../exec",
```

Guarda el archivo.

---

## Paso 3 — Subir a GitHub Pages (5 min)

Tu repo: `github.com/BACMAN2000/systems-engineers-english`

### 3.1 Verifica que el repo sea público

Abre `https://github.com/BACMAN2000/systems-engineers-english/settings` (ya logueado).
- En la sección **Danger Zone** abajo del todo, dice "Change visibility".
- Si dice "Make private" → ya es público ✅
- Si dice "Make public" → es privado. Cambia a público (necesitas hacer click en "Change visibility" y confirmar — solo si no hay nada sensible).

(GitHub Pages gratis solo funciona con repos públicos.)

### 3.2 Push de los archivos

Yo ya dejé el commit listo en la rama `claude/relaxed-ellis-46b797` con:
- `listening-quiz.html`
- `mp3/` (los 4 audios TOEFL necesarios)
- `SETUP-LISTENING.md` (este archivo)

Para subirlo:

```powershell
# (En PowerShell, en tu carpeta principal del repo)
cd "E:\CLAUDE\PAOLO BACA MANRIQUE"

# Trae la rama del worktree y mézclala a main
git checkout main
git merge claude/relaxed-ellis-46b797
git push origin main
```

### 3.3 Activar GitHub Pages

1. Ve a `https://github.com/BACMAN2000/systems-engineers-english/settings/pages`
2. Source: **Deploy from a branch**
3. Branch: **main** → folder: **/ (root)**
4. **Save**.
5. Espera ~1 minuto. GitHub te mostrará la URL.

Tu link final:

```
https://bacman2000.github.io/systems-engineers-english/listening-quiz.html
```

### 3.4 Verifica
Abre la URL desde otro navegador (modo incógnito). Si carga la pantalla "Listening Quiz 🎧" y los audios funcionan → ✅

---

## Paso 4 — Comparte con tus alumnos

Dales este link. Para mejor calidad sonora, recomiéndales **abrirlo en Microsoft Edge**:

```
https://bacman2000.github.io/systems-engineers-english/listening-quiz.html
```

Flujo del alumno:
1. Abre el link en Edge.
2. Escribe su nombre + grado.
3. Elige nivel (tú asignas cuál según el grupo).
4. Escucha los 2 audios y responde las 40 preguntas.
5. Click **📤 Enviar respuestas**.
6. La app:
   - Descarga automáticamente un JSON local como backup
   - Envía las respuestas a tu Google Sheet
   - Muestra el score y el detalle

---

## Tú revisas las respuestas

Abre tu Google Sheet → pestaña `Responses`. Verás una fila por cada alumno que envió:
- Nombre, clase, nivel, score, %, tiempo
- JSON completo con sus respuestas
- JSON con desglose pregunta-por-pregunta (qué eligió vs qué era correcto)

Puedes filtrar por nivel/clase, exportar a Excel, o usar fórmulas para calcular promedios.

---

## Troubleshooting

**Los alumnos no escuchan nada (A2/B1)**
- ¿Están en Microsoft Edge? Otros navegadores no cargan las voces neuronales.
- ¿Tienen internet? Las voces Edge Neural se descargan de la nube la primera vez.
- En el reproductor TTS, debajo del Play debería decir "🌟 Edge Neural" (verde). Si dice "Standard voice" (amarillo) → no son neurales pero igual funciona.

**Los audios mp3 (B2/C1) no cargan**
- Verifica que la carpeta `mp3/` se subió a GitHub (debe verse en el repo).
- En GitHub Pages, la URL debe ser `https://bacman2000.github.io/systems-engineers-english/listening-quiz.html` exactamente.

**Las respuestas no llegan a la Sheet**
- ¿La URL del Apps Script termina en `/exec`? (no `/dev`).
- ¿Está pegada entre comillas en el HTML?
- ¿El Web App está publicado como "Cualquiera" puede acceder?
- Plan B: las respuestas siempre se descargan como JSON en la PC del alumno. Pídeles que te lo envíen por correo.

**Quiero actualizar el quiz después de publicarlo**
- Edita el HTML, commit + push → GitHub Pages actualiza solo en 30-60 seg.

---

## Modo profesor — verificar voces (secreto)

El indicador de voces (♀/♂, Neural/Standard) está **oculto para los alumnos**.

Para verlo tú, agrega `?debug` al final de la URL:

```
https://bacman2000.github.io/systems-engineers-english/listening-quiz.html?debug
```

Solo con ese parámetro aparece el indicador debajo del Play. Sin él, los alumnos ven la app limpia. No compartas la URL con `?debug` — dales la URL normal.

---

## Quitar el quiz cuando termine la clase

Para apagar la URL pública sin borrar nada:
1. Ve a Settings → Pages → cambia Branch a "None" → Save.
2. Listo, la URL deja de funcionar (puedes reactivarla cuando quieras).
