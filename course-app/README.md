# Systems Engineers English Course — Standalone App

Un único archivo HTML (`index.html`) que implementa el curso A1→C2 de inglés técnico para ingenieros de sistemas descrito en `Systems_Engineers_English_Course_A1_C2.docx`.

- **120 clases** organizadas en 6 niveles CEFR (A1, A2, B1, B2, C1, C2) × 20 clases.
- **3 500+ ítems de vocabulario** con modo lista + flashcards.
- **Writing** con contador en vivo calibrado a rangos Cambridge por nivel.
- **Reading** con textarea para pegar la fuente (VOA, NIST, CISA…) + 5 preguntas de comprensión estilo Cambridge/IELTS.
- **Listening** con directorio curado de audios sin copyright por nivel.
- **Progreso** persistido en `localStorage` (sin servidor, sin cuentas).
- **Exportable**: writing a `.txt`, progreso completo a `.json`.

## Archivos

```
course-app/
├── index.html         ← la app (único archivo necesario, ~170 KB)
├── course_data.json   ← datos del currículo (fuente)
└── README.md          ← este archivo
```

Y en la raíz del proyecto:

```
build_course.py         ← genera el .docx de la malla curricular
extract_course_data.py  ← extrae los datos del .py al JSON
build_app.py            ← genera index.html a partir del JSON
```

## Uso local (sin LMS)

Doble clic sobre `index.html` y se abre en tu navegador. Funciona 100 % offline salvo por:

- DM Sans (Google Fonts) — opcional, cae a fuente del sistema si no hay internet.
- Font Awesome (CDN) — íconos; la app sigue siendo usable sin ellos.

Progreso: se guarda en el `localStorage` del navegador. No sale de tu máquina.

## Deploy en plataformas LMS

### Cohasset (plataforma existente del usuario)

La app comparte el design system (paleta `--p:#2563EB`, DM Sans, `.hd` / `.pbar` / `.sb` / `.mn`) con `COHASSET-platform-standalone.html`. Para integrar:

1. **Como recurso independiente**: sube `index.html` al mismo directorio y enlázalo desde el menú de Cohasset.
2. **Como iframe embebido**:

```html
<iframe src="course-app/index.html"
        style="width:100%;height:calc(100vh - 108px);border:0"
        title="Systems Engineers English"></iframe>
```

3. **Como módulo**: copia el bloque `<script>const COURSE=…</script>` y los paneles de renderizado al archivo principal de Cohasset siguiendo sus convenciones de tabs.

### Moodle

Sube `index.html` como recurso tipo **Archivo** o dentro de un **Libro SCORM** simple:

1. Course › Add an activity or resource › **File**.
2. Display: *Embed* o *In pop-up*.
3. Alternativa SCORM: empaqueta `index.html` + un `imsmanifest.xml` mínimo (ver plantilla `scorm-shell.xml` abajo) y sube como paquete SCORM.

### Canvas LMS

1. Files › Upload `index.html`.
2. En una página, inserta: `[link]{Systems Engineers English}` apuntando al archivo, o usa un iframe.

### Google Classroom / Blackboard / otros

Cualquier LMS que acepte subir archivos HTML o iframes de terceros es compatible. No requiere backend.

## Personalización

Todo el contenido vive en `course_data.json`. Editas el JSON y regeneras:

```powershell
python build_app.py
```

Campos por lección:

| Campo        | Descripción                                          |
|--------------|------------------------------------------------------|
| `n`          | Número de clase (1–20)                                |
| `topic`      | Tema de la sesión                                    |
| `grammar`    | Objetivo gramatical / Use of English                 |
| `vocab_raw`  | Vocabulario completo (string)                        |
| `vocab_list` | Array de palabras (se usa en flashcards y chips)     |
| `reading`    | Descripción de la tarea de lectura (Cambridge/IELTS) |
| `listening`  | Fuente sugerida + formato                            |
| `writing`    | Tipo de tarea + rango de palabras                    |
| `cyber`      | Enfoque de ciberseguridad / tech emergente           |

## Plantilla SCORM mínima

Para empaquetar como SCORM 1.2 (válido para Moodle, Canvas, Blackboard):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="sec-english-a1-c2" version="1.0"
 xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
 xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <metadata>
  <schema>ADL SCORM</schema><schemaversion>1.2</schemaversion>
 </metadata>
 <organizations default="org1">
  <organization identifier="org1">
   <title>Systems Engineers English A1-C2</title>
   <item identifier="item1" identifierref="res1">
    <title>Course</title>
   </item>
  </organization>
 </organizations>
 <resources>
  <resource identifier="res1" type="webcontent"
   adlcp:scormtype="sco" href="index.html">
   <file href="index.html"/>
  </resource>
 </resources>
</manifest>
```

Guárdalo como `imsmanifest.xml` en la misma carpeta que `index.html`, comprime ambos en un `.zip` y súbelo como SCORM.

## Credits

- **Autor**: Paolo Baca Manrique — Nordic International School, Perú.
- **Año**: 2026.
- **Frameworks**: Vanilla JS. Sin dependencias de build.
- **Fuentes de audio**: VOA Learning English, NIST, CISA, NASA, FBI (US gov — PD), LibriVox (PD), MIT OCW, OpenLearn, EFF, Berkman Klein (CC).
- **Licencia del curso**: uso educativo interno. Revisa la licencia de cada recurso audio/texto enlazado antes de redistribuir.
