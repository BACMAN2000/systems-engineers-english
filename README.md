# Systems Engineers English Course

> A complete English course (A1 → C2) built for systems engineers, cybersecurity professionals and IT students. Aligned to the Common European Framework of Reference (CEFR) and calibrated against Cambridge, IELTS and TOEFL exam standards.

[![CEFR](https://img.shields.io/badge/CEFR-A1%20→%20C2-2563EB?style=for-the-badge)](https://www.coe.int/en/web/common-european-framework-reference-languages)
[![Lessons](https://img.shields.io/badge/Lessons-120%2F120-10B981?style=for-the-badge)](https://bacman2000.github.io/systems-engineers-english/course-app/)
[![Exercises](https://img.shields.io/badge/Exercises-2425-7C3AED?style=for-the-badge)](#contenido)
[![License](https://img.shields.io/badge/License-Educational-D97706?style=for-the-badge)](#licencia)
[![Live App](https://img.shields.io/badge/Live%20App-bacman2000.github.io-DC2626?style=for-the-badge&logo=github)](https://bacman2000.github.io/systems-engineers-english/course-app/)

---

## 🚀 Open the apps

This repository hosts **two sister apps** that share the same UI and pedagogy. Pick the variant that matches your audience:

| | App | Audience | Live URL |
|---|---|---|---|
| 🛡️ | **Systems Engineers English** | IT / cybersecurity professionals | **[bacman2000.github.io/systems-engineers-english/course-app/](https://bacman2000.github.io/systems-engineers-english/course-app/)** |
| 🌍 | **General English** | Adult learners, everyday topics | **[bacman2000.github.io/systems-engineers-english/general-english-app/](https://bacman2000.github.io/systems-engineers-english/general-english-app/)** |

Both apps work on any modern browser, on **desktop, tablet or mobile**. No installation, no account, no fees. Progress is saved locally in each browser. Mobile users get a hamburger menu, large touch targets and a layout fully optimised for small screens.

---

## 📚 What is this?

This repository contains a full ESP (English for Specific Purposes) curriculum for **systems engineers and cybersecurity professionals**, plus a **standalone web application** that delivers the course interactively.

The programme spans the **six CEFR levels** with **20 lessons per level** (120 total lessons / 180 contact hours) and is calibrated against the descriptors of the major international English exams.

| | A1 | A2 | B1 | B2 | C1 | C2 |
|---|---|---|---|---|---|---|
| **Cambridge** | KET (low) | KET | PET | FCE | CAE | CPE |
| **IELTS** | < 4.0 | 4.0 | 4.5–5.0 | 5.5–6.5 | 7.0–8.0 | 8.5–9.0 |
| **TOEFL iBT** | 0–31 | 32–41 | 42–71 | 72–94 | 95–120 | 118–120 |
| **Vocabulary** | 500 | 1 000 | 2 000 | 4 000 | 8 000 | 16 000+ |
| **Writing words/task** | 25–35 | 35–50 | 100–140 | 140–190 | 220–260 | 280–350 |
| **Reading words/text** | 100–180 | 180–300 | 300–500 | 550–800 | 800–1 100 | 1 100–1 500 |

---

## ✨ Features

### Pedagogical content
- **120 original lessons**, each with: warm-up, grammar focus with table and examples, key phrases, common mistakes, professional tip
- **120 original passages** (one per lesson) on cybersecurity and emerging tech topics — total ~50 000 words of CEFR-calibrated text
- **600 reading comprehension exercises** in Cambridge / IELTS style (MCQ, T/F/NG, gap-fill, matching, short answer)
- **2 425 Use of English exercises** with answer keys (mc-cloze, open cloze, word formation, key-word transformation — 5 of each type per lesson at FCE+ level)
- **3 532 vocabulary items** across the six levels
- All exercises are **auto-corrected** with explanations

### Interactive app features
- 🎧 **Pronunciation modal** with IPA, native TTS via Web Speech API, accent selector (US / GB / AU / IN / CA), recording with comparison
- 🔤 **Vocabulary practice quiz** generated from each lesson's words
- 🌐 **Spanish translation** with curated IT/cyber dictionary (300+ terms) + MyMemory API fallback
- ✍️ **Writing tasks** with live word counter and submit-for-feedback export (`.json` with rubric)
- 📊 **Progress tracking** per level and overall, persisted in `localStorage`
- 🔄 **EN / ES toggle** for the entire UI
- 🎯 **Cambridge-style mock exam** at lesson 20 of each level

### Themes covered
- Foundations of systems engineering
- Cybersecurity (CIA triad, threat landscape, malware, phishing, MFA, encryption)
- Network and application security (OWASP, PKI, VPNs, ZTNA, SIEM)
- Cloud and DevSecOps (IaaS/PaaS/SaaS, K8s, supply chain, SLSA)
- Advanced cyber (CTI, APTs, Zero Trust, threat hunting, RE, forensics)
- Emerging tech (AI/ML, adversarial AI, quantum, post-quantum cryptography, FHE, ZKPs, blockchain)
- Policy and governance (GDPR, NIS2, Schrems II, AI Act, CFAA)

---

## 🗂️ Repository structure

```
systems-engineers-english/
├── README.md                                   ← this file
├── .gitignore                                  ← excludes secrets and build artefacts
│
├── 📱 course-app/                              ← THE STANDALONE APP
│   ├── index.html                              ← main app (single file, ~1.1 MB)
│   ├── course_data.json                        ← course content (lessons, exercises, etc.)
│   └── README.md                               ← deployment notes for LMSs
│
├── 📄 Systems_Engineers_English_Course_A1_C2.docx   ← curriculum document (Word)
│
├── 🐍 Generators (Python scripts)
│   ├── build_course.py                         ← generates the .docx
│   ├── extract_course_data.py                  ← Python → JSON
│   ├── build_app.py                            ← generates index.html from JSON
│   ├── fill_pilot_content.py                   ← initial 30 pilot lessons
│   ├── fill_lesson_notes.py                    ← teaching notes
│   ├── fill_uoe_content.py                     ← Use of English exercises
│   ├── fill_uoe_max.py                         ← UoE expansion to 20 per lesson
│   ├── fill_expansion_a1_a2.py                 ← A1/A2 expansion
│   ├── fill_expansion_b1.py                    ← B1 expansion
│   ├── fill_expansion_b2.py                    ← B2 expansion
│   ├── fill_expansion_c1.py                    ← C1 expansion
│   └── fill_expansion_c2.py                    ← C2 expansion
│
└── 🚀 LAUNCH-SYSTEMS-ENGLISH.bat               ← Windows launcher for local use
```

---

## 🌐 How to use the app

### Option 1 — Hosted version (recommended)
Just open the link:
**[https://bacman2000.github.io/systems-engineers-english/course-app/](https://bacman2000.github.io/systems-engineers-english/course-app/)**

### Option 2 — Local download
1. Download `course-app/index.html` from this repository
2. Double-click the file
3. Opens in your default browser — works fully offline (except dictionary lookup, which requires internet)

### Option 3 — Embed in an LMS (Moodle / Canvas / Cohasset)
Embed the app via iframe:

```html
<iframe src="https://bacman2000.github.io/systems-engineers-english/course-app/"
        style="width:100%; height:calc(100vh - 108px); border:0"
        title="Systems Engineers English"></iframe>
```

For SCORM 1.2 packaging, see `course-app/README.md`.

---

## 🛠️ How to regenerate / extend

If you want to add lessons, modify exercises, or rebuild the app:

```bash
# 1. Edit course_data.json directly, OR run a fill_*.py script
python fill_pilot_content.py        # example

# 2. Rebuild the app
python build_app.py

# 3. Commit and push
git add course-app/
git commit -m "Update: added new lessons"
git push
```

The hosted version updates within 1–2 minutes after pushing.

### Requirements
- Python 3.8+
- `python-docx` (only for regenerating the `.docx` curriculum)
- No other dependencies — no build step, no Node.js

---

## 🎓 CEFR / Cambridge alignment

Each level closes with a Cambridge-style mock exam (lesson 20). Skill targets:

| Skill | A1 | A2 | B1 | B2 | C1 | C2 |
|---|---|---|---|---|---|---|
| **Reading** | Signs, menus | Emails, blog posts | Tech articles | News features | White papers | Research papers |
| **Listening** | Slow dialogues | Voicemails | Podcasts L2 | TED-Ed | Conference keynotes | Academic panels |
| **Writing** | Forms, notes | Informal emails | Reports, emails | Essays, reviews | Proposals, articles | Research articles |
| **Speaking** | Greetings | Describe a job | Project pitch | Structured debate | Q&A keynote | Defend thesis |

---

## 🎙️ Audio sources used

All free for educational use. Each verified:

| Source | License | Levels |
|---|---|---|
| [VOA Learning English](https://learningenglish.voanews.com) | US gov / Public Domain | A1–B2 |
| [NIST](https://www.nist.gov), [CISA](https://www.cisa.gov), [NASA](https://www.nasa.gov) | US gov / Public Domain | B1–C2 |
| [LibriVox](https://librivox.org) | Public Domain | A2–C2 |
| [MIT OpenCourseWare](https://ocw.mit.edu) | CC BY-NC-SA | B2–C2 |
| [OpenLearn](https://www.open.edu/openlearn) | CC BY-NC-SA | B1–C1 |
| [EFF Podcasts](https://www.eff.org) | CC BY | B2–C2 |

---

## 👤 Author

**Paolo Baca Manrique**
English Department Coordinator
Nordic International School (NIS), Perú
Year: 2026

Built collaboratively with the assistance of an AI coding agent (Claude Code).

---

## 📜 License

This material is provided for **educational use** within Nordic International School and similar non-commercial educational settings. The curriculum, app code and original passages are the author's work.

When using third-party resources (audio, images, references), check and respect each source's specific licence. The audio sources listed above are compatible with educational use; for redistribution, verify the licence of the specific resource.

---

## 🤝 Contributions

This is primarily a personal teaching project, but if you find errors or want to suggest improvements:

1. Open an issue describing the change
2. For fixes, fork the repo and open a pull request

---

## 📬 Contact

For questions about the curriculum, deployment to your institution, or collaboration:

- GitHub: [@BACMAN2000](https://github.com/BACMAN2000)
- Institution: Nordic International School, Perú

---

<sub>Built with ❤️ for IT students learning English. If this helps, leave a ⭐ on the repo.</sub>
