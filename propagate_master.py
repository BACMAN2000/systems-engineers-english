# -*- coding: utf-8 -*-
"""
PLAN A — Master as single source of truth.
Archives ALL outdated planners (renames with _ARCHIVE_pre2026_ prefix).
Only active files: Master Excel + Web App + MASTER_INDEX.md
"""
import os, shutil, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from datetime import datetime

NNORDIC = r'C:\Users\Paolo\OneDrive\09_Instituciones\NNORDIC'
INFORMATION = r'C:\Users\Paolo\OneDrive\Documentos\Claude\Projects_I\Information'
TODAY = datetime.now().strftime('%Y-%m-%d')

def archive_file(src):
    if not os.path.exists(src): return None
    dirn, base = os.path.split(src)
    new_name = f'_ARCHIVE_pre2026_{base}'
    dst = os.path.join(dirn, new_name)
    if os.path.exists(dst):
        try: os.remove(src); return 'deleted-duplicate'
        except: return None
    try:
        shutil.move(src, dst)
        return new_name
    except PermissionError:
        return 'LOCKED'
    except Exception as e:
        return f'ERR:{e}'

# === FILES TO ARCHIVE (everything except master + app) ===
to_archive_nnordic = [
    'S&S English.xlsx',
    'NIS_English_Units_G1-G11_2026_SOURCE.xlsx',
    'Units by Grade  - Secondary.xlsx',
    'NIS_Grammar_Curriculum_Complete.xlsx',
    'NIS_ELA_CURRICULUM_COMPLETE.xlsx',
    'NIS_Scope_Sequence_Cambridge_MINEDU.xlsx',
    'NIS_English_Curriculum_Alignment_Analysis.xlsx',
    'ok units_by_grade_G1-G11_Nordic.xlsx',
]

to_archive_information = [
    'S&S English.xlsx',
    'OK_Units_by_Grade_G1-G11_Nordic.V2.xlsx',
    'NIS_Grammar_Curriculum_Complete.xlsx',
    'NIS_ELA_CURRICULUM_COMPLETE.xlsx',
    'NIS_Scope_Sequence_Cambridge_MINEDU.xlsx',
    'NIS_Scope_Sequence.xlsx',
    'NIS_English_Curriculum_Alignment_Analysis.xlsx',
    'ok units_by_grade_G1-G11_Nordic.xlsx',
    'NIS_Plan_de_Trabajo_2026.xlsx',
    'NIS_Work_Plan_2026_EN.xlsx',
    'NIS_Work_Plan_2026_EN_new.xlsx',
]

print('=== PLAN A — Archiving all non-canonical planners ===\n')

archived = []
locked = []
missing = []

for fname in to_archive_nnordic:
    full = os.path.join(NNORDIC, fname)
    result = archive_file(full)
    if result is None: missing.append(fname)
    elif result == 'LOCKED': locked.append(fname)
    elif result and result.startswith('ERR'): print(f'  ERROR: {fname}: {result}')
    else: archived.append(f'NNORDIC/{fname}')
    print(f'  [NNORDIC] {fname} → {result or "missing"}')

print()

for fname in to_archive_information:
    full = os.path.join(INFORMATION, fname)
    result = archive_file(full)
    if result is None: missing.append(fname)
    elif result == 'LOCKED': locked.append(fname)
    elif result and result.startswith('ERR'): print(f'  ERROR: {fname}: {result}')
    else: archived.append(f'Information/{fname}')
    print(f'  [Information] {fname} → {result or "missing"}')

# === MASTER_INDEX.md ===
INDEX_MD = f'''# NIS English Department — Master Index 2026

**Last updated:** {TODAY}
**Owner:** Paolo Baca Manrique (English Coordination)
**Policy:** PLAN A — Single Source of Truth

---

## ✅ ACTIVE FILES (use these)

| # | File | Purpose |
|---|------|---------|
| 1 | `NIS_English_Master_SS_2026.xlsx` | **MASTER Excel** — Scope & Sequence, Grammar, Vocabulary, Reading, Writing, Rubrics, Immersion, Parent Guide (24 sheets) |
| 2 | `NIS_English_Master_App.html` | **Web portal** — auth + admin editing + teacher view + charts (open in any browser) |
| 3 | `MASTER_INDEX.md` | This file |

**Teachers:** use file #2 (open the HTML in any browser, sign in).
**Admin:** editing is done via the web app (changes persist in browser localStorage) or by editing `generate_nis_master.py` and re-running.

---

## 📦 ARCHIVED FILES

All other planners have been archived with prefix `_ARCHIVE_pre2026_`. They contain HISTORICAL data only — do not use for current planning.

**To restore an archived file:** remove the `_ARCHIVE_pre2026_` prefix. But first check with the coordinator — the content likely needs correction before using.

Archived files can be permanently deleted after **2026-12-31** if no longer needed.

---

## 📌 KEY CORRECTIONS (applied in master, 2026-04-19)

1. G1 grammar: removed past simple / going to / would (Pre-A1 compliance)
2. G2 Starters: past simple, future will, comparatives deferred to G4
3. G5 Flyers: replaced *Into the Wild* with age-appropriate titles
4. G6 KET: reconciled grammar vs ELA contradiction; themes align to KET level
5. G7: added conditional 2, reported speech, causative
6. G8 PET: capped narrative writing at 260w
7. G9 FCE: added review genre writing practice
8. G11 CAE: removed "article" from writing (proposal only); word count 220–260
9. G1–G3: writing word counts halved to age-appropriate levels
10. Vocabulary: cumulative counts corrected (G5→2500, G6→3000, G7→3400 etc)
11. Reading plan: aligned to Plan Lector 2026 oficial (in Downloads)
12. Assessment descriptors: translated to English (AD Outstanding / A Expected / B In Progress / C Beginning)

See `16_Change_Log` tab in master for full audit trail.

---

## 🔄 HOW TO UPDATE THE MASTER

1. Open `E:\\CLAUDE\\PAOLO BACA MANRIQUE\\generate_nis_master.py`
2. Edit the relevant Python data
3. Run: `python generate_nis_master.py`
4. Regenerate the web app: `python build_nis_app.py`
5. Verify changes in the HTML app
6. Share with teachers

**DO NOT hand-edit the master Excel directly** — changes will be lost when the script re-runs.

---

## 🏫 PER-GRADE ADMINISTRATIVE FILES

These remain in the `C:\\Users\\Paolo\\OneDrive\\Documentos\\NORDIC\\` folder (separate from this one) for MINEDU compliance:
- `Grado N Primaria.xlsx` (MINEDU rubrics per subject per grade)
- `EY_Assessment Criteria_G1.xlsx`, Kinder equivalents
- `S&S per subject` inside ZIPs (Kinder, G1)
- Weekly planning `.docx` per grade (P1, P2)

**These are independent** of this folder. When updating unit plans or rubrics there, consult the master first for English content.

---

*Generated {TODAY} by propagate_master.py (Plan A — archive all)*
'''

with open(os.path.join(NNORDIC, 'MASTER_INDEX.md'), 'w', encoding='utf-8') as f:
    f.write(INDEX_MD)

print(f'\n=== DONE ===')
print(f'Archived: {len(archived)}')
print(f'Missing (already archived/removed): {len(missing)}')
print(f'Locked (file open in Excel): {len(locked)}')
if locked:
    print(f'\n⚠ LOCKED files (close in Excel and re-run):')
    for f in locked: print(f'   - {f}')
print(f'\nMASTER_INDEX.md: {os.path.join(NNORDIC, "MASTER_INDEX.md")}')
