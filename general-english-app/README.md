# General English Course — Standalone App

Twin of `course-app/` (Systems Engineers English) with the **same UI, same
features, same single-file packaging** — but the topics and vocabulary are
everyday General English instead of IT/cybersecurity.

- **120 classes** organised in 6 CEFR levels (A1, A2, B1, B2, C1, C2) × 20.
- **Same design system** as `course-app/index.html` (DM Sans, blue palette,
  the Cohasset look).
- **Vocabulary mode** with list view + flashcards.
- **Writing** with live word counter calibrated to Cambridge ranges per level.
- **Reading** passages with comprehension exercises.
- **Listening** directory of curated, copyright-clean audio sources.
- **Use of English** practice (mc-cloze, cloze, word-form, key-word).
- **Lesson notes** with grammar tables, common mistakes, useful phrases, tips.
- **Progress** persisted in `localStorage` (key prefix `ge_`, kept separate
  from the systems-engineers app's `sec_` prefix).
- **Exportable**: writing → `.txt`, full progress → `.json`.

## Files

```
general-english-app/
├── index.html         ← the app (single file, ~440 KB)
├── course_data.json   ← curriculum data
└── README.md          ← this file
```

In the project root:

```
generate_general_english.py  ← turns curated seeds into course_data.json
build_general_app.py         ← turns course_data.json into index.html
```

## Status — full release (2026-04-26)

| Level | Lessons fully written | Notes                                |
|-------|----------------------|--------------------------------------|
| A1    | **20 / 20** ✔        | Beginner everyday topics, 90-w passages |
| A2    | **20 / 20** ✔        | Elementary, 110-w passages           |
| B1    | **20 / 20** ✔        | Intermediate, 130-w passages         |
| B2    | **20 / 20** ✔        | Upper-int, 170-w passages, abstract topics |
| C1    | **20 / 20** ✔        | Advanced, 230-w passages, intellectual topics |
| C2    | **20 / 20** ✔        | Mastery, 280-w passages, philosophy/stylistics |
| **Total** | **120 / 120** ✔ | All levels complete                  |

Every lesson includes:
- A topic-tailored vocabulary list (25–35 words at higher levels)
- An original reading passage (CEFR-calibrated word count)
- 5 comprehension exercises (mcq, true/false, gap-fill, match, short-answer)
- 12 use-of-English drills (mc-cloze, cloze, word-form, key-word transformations)
- Lesson notes (warmup, grammar table, useful phrases, common mistakes, tip)
- Culture / real-life note
- Curated listening source recommendation

## Local use

Double-click `index.html` and it opens in your browser. Fully offline except
for two CDN assets:

- **DM Sans** (Google Fonts) — falls back to system fonts offline.
- **Font Awesome** — icons; the app stays usable without them.

Progress lives in your browser's `localStorage` only. It does **not** leave
your machine.

## Branding differences vs the systems-engineers app

| Element             | systems-engineers              | general-english                          |
|---------------------|--------------------------------|------------------------------------------|
| Title               | Systems Engineers English      | General English Course                   |
| Logo icon           | `fa-microchip`                 | `fa-language`                            |
| Tagline             | Cybersecurity & Emerging Tech  | Everyday topics, culture & travel        |
| 6th tab             | Cyber angle (`fa-shield-halved`) | Culture & real-life note (`fa-globe`)    |
| `cyber` JSON field  | cybersecurity angle            | Culture / real-life note                 |
| Search hints        | cisa.gov, nist.gov, mitre.org  | bbc.co.uk/learningenglish, britishcouncil.org, en.wikipedia.org |
| Audio sources       | VOA / NIST / CISA / MIT OCW    | BBC LE / VOA LE / British Council / ELLLO / TED-Ed / LibriVox / NPR |
| localStorage prefix | `sec_`                         | `ge_`                                    |

## Customisation

Edit the seed lists in `generate_general_english.py` (`SEEDS_A1`, `SEEDS_A2`,
`B1_TOPICS`, etc.), then re-run:

```powershell
python generate_general_english.py
python build_general_app.py
```

Each A1/A2 seed is a `L(...)` call defining: topic, vocabulary list, passage
title + text, key facts (used to auto-build comprehension exercises),
culture/real-life note, optional writing task / listening source / reading
description.

The grammar focus for each lesson (CEFR ladder) is defined separately in
`GRAMMAR_BY_LEVEL`. Use of English drills and lesson notes are templated
from `make_uoe()` and `make_lesson_notes()` so adding a new lesson is just
defining its seed.

## Roadmap

All 120 lessons now ship with full content, reaching parity with the
systems-engineers app. Possible next iterations:

- Optional **audio narration** of each passage (TTS-generated `.mp3`s).
- Built-in **vocabulary bilingual gloss** in Spanish (already partially
  supported — the Translate to Spanish button will fetch on demand).
- **Pilot test** with NIS students; track which exercises feel too easy or
  too hard and rebalance.
- **SCORM packaging** for direct upload to Moodle / Canvas / Blackboard.

## Credits

- **Author**: Paolo Baca Manrique — Nordic International School, Perú.
- **Year**: 2026.
- **Frameworks**: Vanilla JS. No build dependencies.
- **Audio sources**: BBC Learning English, VOA Learning English, British
  Council LearnEnglish, ELLLO, TED-Ed, LibriVox, Project Gutenberg,
  StoryNory, OpenLearn, BBC Sounds, NPR, The Guardian Audio, Wikimedia
  Commons, ESL Pod. Check each source's licence before redistributing.
- **Licence**: internal educational use.
