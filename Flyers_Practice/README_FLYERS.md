# Flyers Practice Tests — Paquete completo

## Archivos entregados

| Archivo | Qué es |
|---------|--------|
| `Flyers_Practice_Test_01..10_*.pdf` | Los 10 exámenes impresos (14 páginas c/u) |
| `Flyers_Practice_Tests_Answer_Keys.pdf` | Clave de respuestas combinada (20 págs) |
| `Flyers_Practice_App.html` | **Web app auto-corregida** con los 10 tests |
| `generate_audios.py` | Script que genera los 50 audios MP3 (5 partes × 10 tests) |
| `build_webapp.py` | Reconstructor del HTML (si editas el contenido) |
| `parse_answers.py`, `flyers_content*.py`, `flyers_engine.py` | Código fuente |

## Paso 1 — Generar los audios (British English)

Desde una terminal, en esta carpeta:

```bash
# Opción A — OpenAI (barato, ~$0.50)
pip install openai
set OPENAI_API_KEY=sk-...
python generate_audios.py --provider openai --voice fable

# Opción B — ElevenLabs (premium británico, recomendado, ~$12)
pip install elevenlabs
set ELEVENLABS_API_KEY=...
python generate_audios.py --provider elevenlabs
```

Esto crea `./audios/test_01_part1.mp3` … `test_10_part5.mp3` (50 archivos).

## Paso 2 — Abrir la web app

Doble click en `Flyers_Practice_App.html`. Funciona en cualquier navegador.
La carpeta `audios/` debe estar al lado.

Características:
- Selector de Test 1–10 con su tema
- 3 pestañas por test: Reading & Writing / Listening / Speaking
- Todos los inputs se auto-corrigen con el botón **"Check my answers"**
- Muestra puntaje y la respuesta correcta donde falló
- Ilustraciones SVG por tema

## Paso 3 — Integración con COHASSET platform

Hay dos formas de enchufarlo al botón "Flyers" del `COHASSET-platform-standalone.html`:

### Opción A (más simple) — abrir en ventana nueva
En COHASSET-platform-standalone.html, donde está el botón de Flyers, añade:

```html
<a href="Flyers_Practice_App.html" target="_blank" class="btn-practice">
  10 Practice Tests
</a>
```

Coloca `Flyers_Practice_App.html` y la carpeta `audios/` junto al COHASSET HTML.

### Opción B — embebido con iframe
Dentro del panel del módulo Flyers, agrega:

```html
<iframe src="Flyers_Practice_App.html"
        style="width:100%;height:900px;border:0;border-radius:12px;"
        title="Flyers Practice Tests"></iframe>
```

Ambos funcionan offline si COHASSET está sirviendo los archivos localmente.

## Actualizar contenido

Si cambias algo en `flyers_content.py` o `flyers_content_2.py`, regenera:
```bash
python run_generate.py      # actualiza los PDFs
python build_webapp.py      # actualiza la web app
python generate_audios.py   # regenera audios (sólo los cambiados con --skip-existing)
```
