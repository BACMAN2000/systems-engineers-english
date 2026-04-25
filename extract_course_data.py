# -*- coding: utf-8 -*-
"""Extract LEVELS data from build_course.py into JSON for reuse."""
import json
import re
from pathlib import Path

src = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\build_course.py").read_text(encoding="utf-8")

# Localiza el bloque LEVELS = [ ... ] y eval\u00faalo dentro de un namespace limpio
m = re.search(r"LEVELS\s*=\s*\[", src)
assert m, "LEVELS no encontrado"
start = m.end() - 1  # posici\u00f3n del '['

# Contador de corchetes
depth = 0
end = None
in_str = False
str_ch = None
i = start
while i < len(src):
    ch = src[i]
    if in_str:
        if ch == "\\":
            i += 2; continue
        if ch == str_ch:
            in_str = False
    else:
        if ch in ('"', "'"):
            in_str = True; str_ch = ch
        elif ch == '[':
            depth += 1
        elif ch == ']':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    i += 1

assert end, "No cerr\u00f3 LEVELS"
levels_literal = src[start:end]

LEVELS = eval(levels_literal, {"__builtins__": {}}, {})

# Convertir a estructura JSON rica
course = {
    "title": "Systems Engineers English Course",
    "subtitle": "A1 \u2192 C2 \u2013 CEFR aligned \u2013 120 clases",
    "author": "Paolo Baca Manrique",
    "org": "Nordic International School, Per\u00fa",
    "year": 2026,
    "cefr_equiv": [
        {"cefr":"A1","cambridge":"KET (parte baja)","ielts":"< 4.0","toefl":"0\u201331","profile":"Usuario b\u00e1sico"},
        {"cefr":"A2","cambridge":"A2 Key (KET)","ielts":"4.0","toefl":"32\u201341","profile":"T\u00e9cnico junior"},
        {"cefr":"B1","cambridge":"B1 Preliminary (PET)","ielts":"4.5\u20135.0","toefl":"42\u201371","profile":"T\u00e9cnico"},
        {"cefr":"B2","cambridge":"B2 First (FCE)","ielts":"5.5\u20136.5","toefl":"72\u201394","profile":"Ingeniero"},
        {"cefr":"C1","cambridge":"C1 Advanced (CAE)","ielts":"7.0\u20138.0","toefl":"95\u2013120","profile":"Senior / Arquitecto"},
        {"cefr":"C2","cambridge":"C2 Proficiency (CPE)","ielts":"8.5\u20139.0","toefl":"118\u2013120","profile":"Investigador / CISO"},
    ],
    "quotas": [
        {"cefr":"A1","vocab_total":500,"vocab_new":500,"writing":"25\u201335","reading":"100\u2013180","wpm":"80\u2013110","listen_h":15},
        {"cefr":"A2","vocab_total":1000,"vocab_new":500,"writing":"35\u201350","reading":"180\u2013300","wpm":"110\u2013140","listen_h":20},
        {"cefr":"B1","vocab_total":2000,"vocab_new":1000,"writing":"100\u2013140","reading":"300\u2013500","wpm":"140\u2013170","listen_h":25},
        {"cefr":"B2","vocab_total":4000,"vocab_new":2000,"writing":"140\u2013190","reading":"550\u2013800","wpm":"170\u2013220","listen_h":30},
        {"cefr":"C1","vocab_total":8000,"vocab_new":4000,"writing":"220\u2013260","reading":"800\u20131100","wpm":"220\u2013260","listen_h":35},
        {"cefr":"C2","vocab_total":16000,"vocab_new":8000,"writing":"280\u2013350","reading":"1100\u20131500","wpm":"260\u2013300","listen_h":40},
    ],
    "audio_sources": [
        {"name":"VOA Learning English","domain":"learningenglish.voanews.com","license":"US gov \u2013 Dominio p\u00fablico","content":"Tech/science a 3 velocidades","levels":"A1\u2013B2"},
        {"name":"NASA Audio","domain":"nasa.gov/audio","license":"US gov \u2013 PD","content":"Ciencia e ingenier\u00eda","levels":"B1\u2013C2"},
        {"name":"CISA Cyber","domain":"cisa.gov","license":"US gov \u2013 PD","content":"Alertas ciberseguridad","levels":"B2\u2013C2"},
        {"name":"NIST","domain":"nist.gov","license":"US gov \u2013 PD","content":"Est\u00e1ndares, webinars","levels":"B2\u2013C2"},
        {"name":"FBI Cyber","domain":"fbi.gov","license":"US gov \u2013 PD","content":"Casos cibercrimen","levels":"B2\u2013C1"},
        {"name":"LibriVox","domain":"librivox.org","license":"Dominio p\u00fablico","content":"Audiolibros PD","levels":"A2\u2013C2"},
        {"name":"Project Gutenberg","domain":"gutenberg.org","license":"PD","content":"Textos cl\u00e1sicos","levels":"B1\u2013C2"},
        {"name":"Internet Archive","domain":"archive.org","license":"Mixto (filtrar CC/PD)","content":"Confs t\u00e9cnicas","levels":"Todos"},
        {"name":"MIT OCW","domain":"ocw.mit.edu","license":"CC BY-NC-SA","content":"Clases ing/CS","levels":"B2\u2013C2"},
        {"name":"OpenLearn","domain":"open.edu/openlearn","license":"CC BY-NC-SA","content":"Cursos y podcasts","levels":"B1\u2013C1"},
        {"name":"TED / TED-Ed","domain":"ted.com","license":"CC BY-NC-ND","content":"Charlas + transcripci\u00f3n","levels":"B1\u2013C2"},
        {"name":"Wikimedia Commons","domain":"commons.wikimedia.org","license":"CC BY-SA / PD","content":"Art\u00edculos hablados","levels":"A2\u2013C2"},
        {"name":"Freesound","domain":"freesound.org","license":"CC0 / CC BY","content":"SFX (server hum, keyboard)","levels":"Todos"},
        {"name":"Pixabay Audio","domain":"pixabay.com/music","license":"Pixabay License","content":"M\u00fasica y SFX","levels":"Todos"},
        {"name":"Berkman Klein Center","domain":"cyber.harvard.edu","license":"CC BY","content":"Internet y sociedad","levels":"C1\u2013C2"},
        {"name":"EFF","domain":"eff.org","license":"CC BY","content":"Privacidad/pol\u00edtica","levels":"B2\u2013C2"},
    ],
    "levels": []
}

for code, desc, quota, classes in LEVELS:
    level = {
        "code": code,
        "desc": desc,
        "quota": quota,
        "lessons": []
    }
    for i, (tema, gram, vocab, reading, listening, writing, angle) in enumerate(classes, 1):
        # parse vocab string: "+60: word1, word2, ..." or "25 palabras: w1, w2, ..."
        vocab_list = []
        m = re.search(r":\s*(.+)$", vocab, flags=re.S)
        if m:
            raw = m.group(1)
            # split by comma, take first 50
            for w in re.split(r",\s*", raw):
                w = w.strip()
                if w and len(w) < 60:
                    vocab_list.append(w)
        level["lessons"].append({
            "n": i,
            "topic": tema,
            "grammar": gram,
            "vocab_raw": vocab,
            "vocab_list": vocab_list[:80],
            "reading": reading,
            "listening": listening,
            "writing": writing,
            "cyber": angle
        })
    course["levels"].append(level)

out = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\course_data.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(course, ensure_ascii=False, indent=1), encoding="utf-8")

total = sum(len(l["lessons"]) for l in course["levels"])
total_vocab = sum(len(le["vocab_list"]) for l in course["levels"] for le in l["lessons"])
print(f"OK: {total} lecciones, {total_vocab} items de vocabulario extra\u00eddos")
print(f"-> {out}")
