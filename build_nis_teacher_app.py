# -*- coding: utf-8 -*-
"""Build TEACHER-only version of NIS English Master App.
- No login (direct to dashboard)
- Limited tabs (Dashboard, Pathway, Benchmarks, SS Master, Skills, Units, CLIL, Assessment, Immersion)
- No edit mode, no user management, no admin features
- Only PDF export (no CSV)
- Vibrant teacher-mode colors always on
- "Welcome, Teacher"
- Runs in any browser (standalone HTML)
"""
import json

# Load the main build script to extract HTML template
with open('build_nis_app.py', 'r', encoding='utf-8') as f:
    src = f.read()

# Extract the HTML template block
s = src.find("HTML = r'''")
e = src.find("'''", s + 11)
html = src[s+11:e]

# Load data
with open('master_data.json', 'r', encoding='utf-8') as f:
    master_data = f.read()
with open('clil_plans.json', 'r', encoding='utf-8') as f:
    clil_plans = f.read()

# =================================================================
# TEACHER-SPECIFIC PATCHES to the HTML template
# =================================================================

# 1) Change title
html = html.replace(
    "<title>NIS English Department — Master Portal</title>",
    "<title>NIS English — Teacher Portal</title>"
)

# 2) Inject TEACHER_MODE flag at top of React script + auto-apply teacher CSS
html = html.replace(
    "const { useState, useEffect, useMemo, useRef, useCallback } = React;",
    """const { useState, useEffect, useMemo, useRef, useCallback } = React;
// ============= TEACHER MODE (hardcoded) =============
const TEACHER_MODE = true;
const TEACHER_USER = { id:'teacher', email:'teacher@nis.edu.pe', name:'Teacher', role:'teacher', password:'', tabs: [
  '01_Pathway','02_Benchmarks','03_SS_Master',
  '04_Grammar','05_Vocabulary','06_Phonics','07_Reading','08_Writing','09_Speaking_Listening',
  '10_Units_G1_G5','11_Units_G6_G11','18_Detail_G1_G5','19_Detail_G6_G11','20_Units_Full_G1_G11',
  '12_CLIL_Map',
  '14_Assessment_Scale','17_Rubrics_Ready','15_Teacher_QuickRef',
  '21_Immersion_Framework','22_Teaching_Strategies','23_Parent_Guide'
] };
document.body.classList.add('teacher-mode');"""
)

# 3) Replace App initial user: if TEACHER_MODE, use TEACHER_USER always
html = html.replace(
    """  const [user, setUser] = useState(() => {
    try { const a = JSON.parse(localStorage.getItem(LS.auth) || 'null'); if (!a) return null; return loadUsers().find(u => u.id === a.id) || null; } catch(e) { return null; }
  });""",
    """  const [user, setUser] = useState(() => {
    if (TEACHER_MODE) return TEACHER_USER;
    try { const a = JSON.parse(localStorage.getItem(LS.auth) || 'null'); if (!a) return null; return loadUsers().find(u => u.id === a.id) || null; } catch(e) { return null; }
  });"""
)

# 4) Sidebar: hide admin section entirely for teacher
html = html.replace(
    "    admin:    { label:'🛠 Admin',     tabs: user.role === 'admin' ? ['16_Change_Log','_activity'] : ['16_Change_Log'] },",
    "    admin:    { label:'🛠 Admin',     tabs: (TEACHER_MODE ? [] : (user.role === 'admin' ? ['16_Change_Log','_activity'] : ['16_Change_Log'])) },"
)

# 5) Sidebar: hide Cover tab in Overview when teacher mode
html = html.replace(
    "    overview: { label:'📘 Overview',  tabs:['00_Cover','01_Pathway','02_Benchmarks','03_SS_Master'] },",
    "    overview: { label:'📘 Overview',  tabs: (TEACHER_MODE ? ['01_Pathway','02_Benchmarks','03_SS_Master'] : ['00_Cover','01_Pathway','02_Benchmarks','03_SS_Master']) },"
)

# 6) Sidebar: hide Calendar for teachers (not in their list)
html = html.replace(
    "    calendar: { label:'📅 Calendar',  tabs:['13_Cambridge_Calendar'] },",
    "    calendar: { label:'📅 Calendar',  tabs: (TEACHER_MODE ? [] : ['13_Cambridge_Calendar']) },"
)

# 7) Hide admin buttons in sidebar (edit mode, users, reset requests)
html = html.replace(
    "        {user.role === 'admin' && (",
    "        {user.role === 'admin' && !TEACHER_MODE && ("
)

# 8) Welcome message: "Teacher"
html = html.replace(
    "<h1 className=\"text-3xl font-bold text-slate-900 dark:text-white\">Welcome, {user.name.split(' ')[0]} 👋</h1>",
    "<h1 className=\"text-3xl font-bold text-slate-900 dark:text-white\">Welcome, Teacher 👋</h1>"
)

# 9) Export button: only PDF option (hide CSV + Print)
html = html.replace(
    """      {open && (
        <div className="absolute right-0 mt-1 bg-white dark:bg-slate-800 shadow-lg border border-slate-200 dark:border-slate-600 rounded w-52 z-20 animate-fade-in">
          <button onClick={()=>{ exportSheetCSV(tabId); setOpen(false); }} className="w-full text-left px-3 py-2 text-xs hover:bg-slate-100 dark:hover:bg-slate-700 flex items-center gap-2">
            <span>📄</span> <span>CSV (spreadsheet)</span>
          </button>
          <button onClick={()=>{ exportSheetPDF(tabId, sheet); setOpen(false); }} className="w-full text-left px-3 py-2 text-xs hover:bg-slate-100 dark:hover:bg-slate-700 flex items-center gap-2">
            <span>📑</span> <span>Clean PDF (polished)</span>
          </button>
          <button onClick={()=>{ window.print(); setOpen(false); }} className="w-full text-left px-3 py-2 text-xs hover:bg-slate-100 dark:hover:bg-slate-700 flex items-center gap-2">
            <span>🖨</span> <span>Print current view</span>
          </button>
        </div>
      )}""",
    """      {open && (
        <div className="absolute right-0 mt-1 bg-white dark:bg-slate-800 shadow-lg border border-slate-200 dark:border-slate-600 rounded w-52 z-20 animate-fade-in">
          <button onClick={()=>{ exportSheetPDF(tabId, sheet); setOpen(false); }} className="w-full text-left px-3 py-2 text-sm hover:bg-slate-100 dark:hover:bg-slate-700 flex items-center gap-2">
            <span>📑</span> <span>Download PDF</span>
          </button>
          {!TEACHER_MODE && (<>
          <button onClick={()=>{ exportSheetCSV(tabId); setOpen(false); }} className="w-full text-left px-3 py-2 text-xs hover:bg-slate-100 dark:hover:bg-slate-700 flex items-center gap-2">
            <span>📄</span> <span>CSV</span>
          </button>
          <button onClick={()=>{ window.print(); setOpen(false); }} className="w-full text-left px-3 py-2 text-xs hover:bg-slate-100 dark:hover:bg-slate-700 flex items-center gap-2">
            <span>🖨</span> <span>Print</span>
          </button>
          </>)}
        </div>
      )}"""
)

# 10) Stronger visual colors for teacher mode — amp them up further in body class
html = html.replace(
    "body.teacher-mode { background: linear-gradient(180deg, #E3EDFB 0%, #F0F4FA 100%); }",
    """body.teacher-mode { background: linear-gradient(135deg, #DCE6F1 0%, #F0F4FA 50%, #E3EDFB 100%); }
  body.teacher-mode main { background: linear-gradient(135deg, #F5F7FC 0%, #FFFFFF 100%); }
  body.teacher-mode .animate-fade-in { animation-duration: 300ms; }
  body.teacher-mode .grade-chip, body.teacher-mode button[style*="backgroundColor"] { box-shadow: 0 2px 8px rgba(74,123,200,0.25); }
  body.teacher-mode h1, body.teacher-mode h2 { color: #1F4E79; font-weight: 800; }
  body.teacher-mode .tab-row:hover { background-color: rgba(74, 123, 200, 0.15) !important; transform: translateX(2px); transition: all 200ms; }"""
)

# 11) Remove login-related session expiry nagging for teacher
html = html.replace(
    """  if (!user) return (<><LoginPage onLogin={setUser}/><ToastContainer/></>);""",
    """  if (!user) { if (TEACHER_MODE) { setTimeout(()=>setUser(TEACHER_USER), 0); return null; } return (<><LoginPage onLogin={setUser}/><ToastContainer/></>); }"""
)

# 12) Hide Users tabs list in user management (not visible for teacher anyway, but belt+braces)
# (already hidden via admin check)

# =================================================================
# Inject data
# =================================================================
html = html.replace('__DATA__', master_data).replace('__PLANS__', clil_plans)

# =================================================================
# Save
# =================================================================
OUTPUT = r'C:\Users\Paolo\OneDrive\09_Instituciones\NNORDIC\NIS_English_Teacher_App.html'
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)
import os
print(f'OK: {OUTPUT} ({os.path.getsize(OUTPUT)//1024} KB)')
print('Teacher version created successfully.')
