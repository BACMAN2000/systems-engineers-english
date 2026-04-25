# TOEFL Premium — Session Handoff

**Usuario:** Renatto (renattobaca@gmail.com)
**Fecha de handoff:** 2026-04-18
**Objetivo:** Continuar esta sesión en Cowork sin perder contexto.

---

## 1. Qué se construyó

Una plataforma TOEFL iBT con **dos niveles**:

- **Free** — 4 exámenes TOEFL ya existentes (16 secciones, 778 audios, 300+ preguntas). Botón rojo en la pantalla principal de Cohasset.
- **Premium** — 55 TPOs oficiales extraídos del pack XYSTPO 2.0. Botón azul, activado con código de desbloqueo (simula suscripción). Estilo auténtico ETS (navy `#034683`, Helvetica Neue).

El Premium NO requiere traducir chino — el contenido real del examen (passages, questions, options, answers) ya está 100 % en inglés oficial ETS. El chino solo aparece en una columna opcional `translation` que se **omite**, y en headers de atribución que se **limpian por regex** (`来源|QQ\d+|www\.ladynbirds|www\.kmf\.com|www\.xys`).

---

## 2. Estado actual (IMPORTANTE — leer antes de continuar)

- Todos los scripts/HTML ya están escritos en `E:\CLAUDE\PAOLO BACA MANRIQUE\`.
- **Python NO estaba instalado** cuando se intentó correr SETUP — por eso el bash fallaba (y `SETUP-TOEFL-PREMIUM.ps1` aborta con "Python not found on PATH").
- **Renatto está instalando Python ahora mismo.** Una vez instalado (Python 3.8+ con "Add to PATH" marcado), el flujo one-click funcionará.
- El sandbox Linux del chat anterior quedó inservible (disco lleno en `/tmp` durante un intento previo de extracción), por eso se pivoteó a ejecución Windows-side vía PowerShell. Eso no afecta nada en esta nueva sesión.

### Acción pendiente del usuario

1. Terminar de instalar Python 3.8+ desde python.org (marcar **Add Python to PATH**).
2. Abrir nueva terminal/explorador (para que el PATH se refresque).
3. Doble-click en `E:\CLAUDE\PAOLO BACA MANRIQUE\LAUNCH-TOEFL-PREMIUM.bat`.
4. Esperar 3-6 min (setup automático la primera vez — extrae ZIP, convierte DB → JSON).
5. Se abre el browser en `http://127.0.0.1:9124/toefl-premium-runner.html`.
6. Ingresar cualquiera de estos códigos en el modal:
   - `TOEFL-PREMIUM-2026`
   - `RENATTO-TOEFL-55`
   - `XYSTPO-UNLOCK`

---

## 3. Inventario de archivos

Todo vive en `E:\CLAUDE\PAOLO BACA MANRIQUE\`:

| Archivo | Rol |
|---|---|
| `LAUNCH-TOEFL-PREMIUM.bat` | One-click. Si `toefl-premium-assets\data\index.json` no existe, corre SETUP automáticamente. Luego arranca `serve-toefl.ps1` y abre el runner. Sin prompts. |
| `SETUP-TOEFL-PREMIUM.ps1` | Extrae `XYSTPO2.0/Resources/*` del ZIP (sin Qt5 DLLs/ejecutables), copia `Tpo.db` + carpetas `TpoN/` a `toefl-premium-assets/`, invoca Python converter. Detecta python/py/python3 vía `Get-Command -ErrorAction SilentlyContinue` (fallback chain sin `??` para compat PS 5.1). |
| `toefl-premium-assets/convert_tpo_db.py` | Convierte `Tpo.db` (SQLite) → JSONs por TPO. Query correcta: `WHERE eid=? AND chapter='read'` (chapter es string, no category int). Genera `data/index.json` + `data/tpo{1..55}/{reading,listening,speaking,writing}.json`. |
| `toefl-premium-runner.html` | Runner premium (~1300 líneas). Estilo ETS auténtico. LocalStorage gate (`toefl_premium_unlocked`). Renderers por sección. MediaRecorder para Speaking. Timers: R 54min, L 41min, S 17min, W 50min. Carga data desde `toefl-premium-assets/data/index.json`. |
| `serve-toefl.ps1` | HTTP server local en `127.0.0.1:9124` con MIME types completos (mp3/json/wav/woff2/png/etc). Sirve desde la raíz de `PAOLO BACA MANRIQUE`. |
| `LAUNCH-TOEFL.bat` | Launcher simple del runner FREE (4 exámenes). |
| `LAUNCH-COHASSET.bat` | Launcher de la plataforma integrada Cohasset. |
| `COHASSET-platform-standalone.html` | Plataforma principal — modificada para mostrar **dos botones**: Free (rojo) y Premium (azul gradient `#034683→#012a55` con badge 🔒/✓). IIFE `updateToeflPremiumBtn()` en INIT lee localStorage y actualiza el candado. |

**Fuente del pack (input, no modificar):**
`C:\Users\Paolo\OneDrive\1.2 ETS_Exams\TOEFL\TOEFL\XYSTPO2.0_2.zip`

**Output del setup (generado, ignorar en backups hasta que exista):**
`E:\CLAUDE\PAOLO BACA MANRIQUE\toefl-premium-assets\` (~2 GB tras setup)

---

## 4. Arquitectura rápida

```
Doble-click LAUNCH-TOEFL-PREMIUM.bat
        │
        ├── ¿existe toefl-premium-assets\data\index.json?
        │     NO → SETUP-TOEFL-PREMIUM.ps1
        │            ├── Extrae ZIP (solo Resources/, skip Qt5)
        │            ├── Copia Tpo.db + TpoN/ → toefl-premium-assets/
        │            └── python convert_tpo_db.py  ← REQUIERE PYTHON
        │                    └── Genera 55 × 4 JSONs + index.json
        │     SÍ → skip setup
        │
        ├── Start serve-toefl.ps1  (HTTP :9124)
        └── Open http://127.0.0.1:9124/toefl-premium-runner.html
                    │
                    └── localStorage gate → unlock code → lobby → section runner
```

**Datos esperados tras setup exitoso:**

- 55 TPOs
- ~2286 preguntas Reading
- ~1869 preguntas Listening
- 440 tasks Speaking + Writing combinados
- Audios MP3 originales ETS
- Imágenes (diagramas lectura/lecture)

---

## 5. Decisiones clave / gotchas

- **Operador `??` de PowerShell** requiere PS7+. En Windows típico hay PS 5.1 → se usó fallback chain `if (-not ...) { ... }`.
- **Extracción del ZIP** debe usarse `[System.IO.Compression.ZipFile]::OpenRead`, NO `Expand-Archive` (muy lento con archivos grandes).
- **Chapter vs category en Tpo.db**: `article.chapter` es `'read'` (string); `article.category` es int. La query correcta filtra por `chapter='read'`.
- **Limpieza de chino en listening transcripts** (`clean_lisText`): regex filtra líneas con `来源|QQ\d+|www\.ladynbirds|www\.kmf\.com|www\.xys`, preserva todo lo demás.
- **Media path resolution** (`find_file`): usa `MEDIA.parent.rglob(pattern)` para que las rutas del JSON sean relativas al root y el servidor las sirva sin tocar.
- **El sandbox Linux** (mcp__workspace__bash) tiene `--unshare-pid` → procesos background mueren entre llamadas. No hacer extracciones largas desde ahí.

---

## 6. Si algo falla tras instalar Python

Probar desde PowerShell:

```powershell
cd "E:\CLAUDE\PAOLO BACA MANRIQUE"
python --version          # debe mostrar 3.8+
python toefl-premium-assets\convert_tpo_db.py toefl-premium-assets
```

Si `python` no se encuentra pero sí hay `py`:

```powershell
py -3 toefl-premium-assets\convert_tpo_db.py toefl-premium-assets
```

Si el converter aborta con `Tpo.db not found`, rerun `SETUP-TOEFL-PREMIUM.ps1` primero (necesita copiar la DB desde el ZIP extraído).

Si el browser muestra "index.json 404" aunque setup terminó: verificar que `serve-toefl.ps1` corre (ventana PowerShell abierta con título "TOEFL Premium Server") y que el archivo `E:\CLAUDE\PAOLO BACA MANRIQUE\toefl-premium-assets\data\index.json` existe.

---

## 7. Tareas completadas (referencia)

Todas cerradas en la sesión anterior:

1. Inspeccionar `Tpo.db` (9 tablas, 27 MB, 55 exámenes).
2. Decidir mecanismo de suscripción → localStorage + unlock codes.
3. Extraer ZIP XYSTPO → delegado a Windows vía `SETUP-TOEFL-PREMIUM.ps1`.
4. "Traducir chino" → determinado que se **omite** (columna `translation`) y se **limpia** (regex en transcripts). No hay traducción real que hacer.
5. Runner premium con estilo ETS auténtico → `toefl-premium-runner.html`.
6. Separar botones Free/Premium en Cohasset → listos con badges 🔒/✓.
7. Verificación final con agente → 19/19 checks pasaron.
8. One-click launcher (sin prompts Y/N) → `LAUNCH-TOEFL-PREMIUM.bat` reescrito.

---

## 8. Próximo paso al retomar en Cowork

1. Confirmar con Renatto que Python terminó de instalar (`python --version` en una terminal NUEVA debe responder con la versión).
2. Decirle que doble-clickee `LAUNCH-TOEFL-PREMIUM.bat`.
3. Si hay error → leer el mensaje en la ventana negra del .bat y aplicar la sección 6 de este MD.
4. Una vez que el runner cargue + unlock code funcione → el proyecto está live. Todo lo demás (agregar más códigos, cambiar estilos, etc.) es enhancement.

---

*Handoff generado al terminar la sesión previa. Todos los archivos listos, solo falta Python en el PATH del usuario.*
