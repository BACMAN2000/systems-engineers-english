# -*- coding: utf-8 -*-
"""Build NIS English Master web app v2 — interactive (no logo, dashboard, Cmd+K, visual calendar, CLIL grid)."""
import json

with open('master_data.json', 'r', encoding='utf-8') as f:
    master_data = f.read()
with open('clil_plans.json', 'r', encoding='utf-8') as f:
    clil_plans = f.read()

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NIS English Department — Master Portal</title>
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script>
tailwind.config = {
  darkMode: 'class',
  theme: { extend: {
    colors: { nordic: { 50:'#F0F4FA', 100:'#DCE6F1', 200:'#B4BCDF', 300:'#8FA3D5', 400:'#6B91D6', 500:'#4A7BC8', 600:'#2E5B9E', 700:'#1F4E79', 800:'#143254', 900:'#0A1F38' } },
    animation: { 'fade-in':'fadeIn 200ms ease-out', 'slide-up':'slideUp 250ms cubic-bezier(0.22, 1, 0.36, 1)', 'slide-right':'slideRight 250ms ease-out' },
    keyframes: {
      fadeIn:{ '0%':{ opacity:0 }, '100%':{ opacity:1 }},
      slideUp:{ '0%':{ opacity:0, transform:'translateY(16px)' }, '100%':{ opacity:1, transform:'translateY(0)' }},
      slideRight:{ '0%':{ opacity:0, transform:'translateX(20px)' }, '100%':{ opacity:1, transform:'translateX(0)' }},
    }
  } }
}
</script>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif }
  .no-scrollbar::-webkit-scrollbar { display: none }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none }
  /* TEACHER MODE — brighter, higher contrast */
  body.teacher-mode { background: linear-gradient(180deg, #E3EDFB 0%, #F0F4FA 100%); }
  body.teacher-mode aside { background: linear-gradient(180deg, #FFFFFF 0%, #E7EFFA 100%); border-right: 2px solid #4A7BC8; box-shadow: 2px 0 12px rgba(74,123,200,0.15); }
  body.teacher-mode aside .bg-nordic-600 { background-color: #2E5B9E !important; }
  body.teacher-mode aside button:hover { background-color: #DCE6F1 !important; transform: translateX(2px); transition: all 180ms; }
  body.teacher-mode main > .p-6 { background: #FAFBFE; }
  body.teacher-mode .shadow-sm { box-shadow: 0 2px 8px rgba(74,123,200,0.12) !important; }
  body.teacher-mode.dark { background: linear-gradient(180deg, #0A1F38 0%, #143254 100%); }
  body.teacher-mode.dark aside { background: linear-gradient(180deg, #143254 0%, #1F4E79 100%); border-right: 2px solid #6B91D6; }
  .cell-fill { transition: all 150ms ease }
  .tab-row:hover { background-color: rgba(74, 123, 200, 0.08) }
  html.dark .tab-row:hover { background-color: rgba(143, 163, 213, 0.12) }
  @media print { .no-print { display: none !important } }
  .kbd { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 10px; padding: 2px 5px; border-radius: 4px; background: rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.1) }
  html.dark .kbd { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.15) }
  .gradient-text { background: linear-gradient(90deg, #4A7BC8, #8FA3D5); -webkit-background-clip: text; background-clip: text; color: transparent }
  .grade-chip { display:inline-block; padding:2px 8px; border-radius:10px; font-size:10px; font-weight:600; letter-spacing:0.5px }
  .pulse-dot { width: 8px; height: 8px; border-radius: 50%; animation: pulse 1.5s ease-in-out infinite }
  @keyframes pulse { 0%,100% { opacity: 1 } 50% { opacity: 0.5 } }
</style>
</head>
<body class="bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 antialiased">
<div id="root"></div>

<script>
const MASTER_DATA = __DATA__;
const CLIL_PLANS = __PLANS__;
</script>

<script type="text/babel">
const { useState, useEffect, useMemo, useRef, useCallback } = React;

// ============= LOGO (tries ./nordic-logo.png first, falls back to gradient text) =============
function NordicLogo({ compact = false }) {
  const [imgOk, setImgOk] = useState(true);
  const src = './nordic-logo.png';
  if (imgOk) {
    return (
      <img src={src} alt="Nordic International School"
        onError={()=>setImgOk(false)}
        className={compact ? 'h-20 w-full object-contain' : 'h-32 mx-auto object-contain'}/>
    );
  }
  return compact ? (
    <div>
      <div className="text-sm font-bold gradient-text tracking-wide">NIS ENGLISH</div>
      <div className="text-[10px] tracking-widest text-slate-500 dark:text-slate-400">IMMERSION · 2026</div>
    </div>
  ) : (
    <div className="text-center">
      <h1 className="text-3xl font-bold gradient-text mb-1">NIS ENGLISH</h1>
      <p className="text-xs tracking-[0.3em] text-slate-500 dark:text-slate-400">DEPARTMENT · 2026</p>
    </div>
  );
}

// ============= STORAGE =============
const LS = { auth:'nis_auth_v2', theme:'nis_theme', users:'nis_users_v2', overrides:'nis_overrides_v2', favorites:'nis_favs_v2', activity:'nis_activity_v2', comments:'nis_comments_v2', progress:'nis_progress_v2', rememberEmail:'nis_remember_email', resets:'nis_reset_requests' };
const DEFAULT_USERS = [
  { id:'admin', email:'paolobaca2000@gmail.com', name:'Paolo Baca Manrique', role:'admin', password:'admin2026', tabs:'all' },
];
const loadUsers = () => { try { const r = localStorage.getItem(LS.users); if (r) return JSON.parse(r); } catch(e) {} localStorage.setItem(LS.users, JSON.stringify(DEFAULT_USERS)); return DEFAULT_USERS; };
const saveUsers = (u) => localStorage.setItem(LS.users, JSON.stringify(u));
const loadOverrides = () => { try { return JSON.parse(localStorage.getItem(LS.overrides) || '{}'); } catch(e) { return {}; } };
const saveOverrides = (o) => localStorage.setItem(LS.overrides, JSON.stringify(o));
const loadFavs = () => { try { return JSON.parse(localStorage.getItem(LS.favorites) || '[]'); } catch(e) { return []; } };
const saveFavs = (f) => localStorage.setItem(LS.favorites, JSON.stringify(f));
const loadActivity = () => { try { return JSON.parse(localStorage.getItem(LS.activity) || '[]'); } catch(e) { return []; } };
const saveActivity = (a) => localStorage.setItem(LS.activity, JSON.stringify(a));
const logActivity = (entry) => { const a = loadActivity(); a.unshift(entry); saveActivity(a.slice(0, 500)); };
const loadComments = () => { try { return JSON.parse(localStorage.getItem(LS.comments) || '{}'); } catch(e) { return {}; } };
const saveComments = (c) => localStorage.setItem(LS.comments, JSON.stringify(c));
const loadProgress = () => { try { return JSON.parse(localStorage.getItem(LS.progress) || '{}'); } catch(e) { return {}; } };
const saveProgress = (p) => localStorage.setItem(LS.progress, JSON.stringify(p));

// ---- Helpers ----
const fmtDate = (ts) => { const d = new Date(ts); return d.toLocaleDateString() + ' ' + d.toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'}); };
const exportSheetCSV = (tabId) => {
  const sheet = MASTER_DATA.sheets[tabId]; if (!sheet) return;
  const rows = sheet.rows.map(row => row.map(c => { let v = String(c.v || '').replace(/"/g, '""'); return '"' + v + '"'; }).join(','));
  const csv = rows.join('\r\n');
  const blob = new Blob([csv], { type:'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = tabId + '.csv'; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 200);
};

const ALL_TABS = Object.keys(MASTER_DATA.sheets);
const isDarkColor = (hex) => {
  if (!hex) return false;
  const h = hex.replace('#','');
  if (h.length < 6) return false;
  const r = parseInt(h.substr(0,2),16), g = parseInt(h.substr(2,2),16), b = parseInt(h.substr(4,2),16);
  return (r*0.299 + g*0.587 + b*0.114) < 140;
};
const GRADE_LEVELS = {
  G1:{cefr:'Pre-A1',exam:'Pre-Starters',color:'#FCE4EC'}, G2:{cefr:'Pre-A1→A1',exam:'Starters',color:'#FCE4EC'},
  G3:{cefr:'A1',exam:'Pre-Movers',color:'#FFF3E0'}, G4:{cefr:'A1→A2',exam:'Movers',color:'#FFF3E0'},
  G5:{cefr:'A2',exam:'Flyers',color:'#FFFDE7'}, G6:{cefr:'A2→B1',exam:'KET',color:'#FFFDE7'},
  G7:{cefr:'B1',exam:'KET+ bridge',color:'#E8F5E9'}, G8:{cefr:'B1+',exam:'PET',color:'#E8F5E9'},
  G9:{cefr:'B1+→B2',exam:'FCE',color:'#E3F2FD'}, G10:{cefr:'B2+',exam:'FCE consol.',color:'#E3F2FD'},
  G11:{cefr:'C1',exam:'CAE',color:'#F3E5F5'},
};

const loadResets = () => { try { return JSON.parse(localStorage.getItem(LS.resets) || '[]'); } catch(e) { return []; } };
const saveResets = (r) => localStorage.setItem(LS.resets, JSON.stringify(r));
const getInitials = (name) => (name || '?').split(' ').map(p=>p[0]).filter(Boolean).slice(0,2).join('').toUpperCase();
const avatarColor = (name) => {
  const colors = ['#4A7BC8','#8E44AD','#16A085','#E67E22','#C0392B','#2C3E50','#D35400','#27AE60'];
  let h = 0; for (const c of (name||'X')) h = (h*31 + c.charCodeAt(0)) & 0xFFFF;
  return colors[h % colors.length];
};

// ============= AVATAR =============
function Avatar({ name, size=32 }) {
  return (
    <div className="rounded-full flex items-center justify-center text-white font-semibold shadow-sm"
         style={{ width: size, height: size, backgroundColor: avatarColor(name), fontSize: size*0.4 }}>
      {getInitials(name)}
    </div>
  );
}

// ============= TOAST =============
let toastListener = null;
const pushToast = (t) => toastListener && toastListener(t);
function ToastContainer() {
  const [toasts, setToasts] = useState([]);
  useEffect(() => {
    toastListener = (t) => {
      const id = Date.now() + Math.random();
      setToasts(s => [...s, { id, ...t }]);
      setTimeout(() => setToasts(s => s.filter(x => x.id !== id)), t.ms || 3500);
    };
    return () => { toastListener = null; };
  }, []);
  const styles = {
    success:'bg-emerald-500', error:'bg-red-500', info:'bg-nordic-600', warn:'bg-amber-500'
  };
  return (
    <div className="fixed bottom-6 right-6 z-[60] space-y-2">
      {toasts.map(t => (
        <div key={t.id} className={`${styles[t.type] || styles.info} text-white px-4 py-3 rounded-lg shadow-xl animate-slide-right min-w-[260px] max-w-sm`}>
          <div className="flex items-center gap-2">
            <span>{t.type === 'success' ? '✓' : t.type === 'error' ? '✕' : t.type === 'warn' ? '⚠' : 'ℹ'}</span>
            <span className="text-sm">{t.message}</span>
          </div>
        </div>
      ))}
    </div>
  );
}

// ============= BREADCRUMB =============
function Breadcrumb({ tabId, user }) {
  const tabToSection = {
    '_dashboard':{section:'Home', label:'Dashboard'},
    '_activity':{section:'Admin', label:'Activity Log'},
    '00_Cover':{section:'Overview', label:'Cover'},
    '01_Pathway':{section:'Overview', label:'Pathway'},
    '02_Benchmarks':{section:'Overview', label:'Benchmarks'},
    '03_SS_Master':{section:'Overview', label:'SS Master'},
    '04_Grammar':{section:'Skills', label:'Grammar'},
    '05_Vocabulary':{section:'Skills', label:'Vocabulary'},
    '06_Phonics':{section:'Skills', label:'Phonics'},
    '07_Reading':{section:'Skills', label:'Reading'},
    '08_Writing':{section:'Skills', label:'Writing'},
    '09_Speaking_Listening':{section:'Skills', label:'Speaking & Listening'},
    '10_Units_G1_G5':{section:'Units', label:'G1–G5'},
    '11_Units_G6_G11':{section:'Units', label:'G6–G11'},
    '12_CLIL_Map':{section:'CLIL', label:'CLIL Map'},
    '13_Cambridge_Calendar':{section:'Calendar', label:'Cambridge'},
    '14_Assessment_Scale':{section:'Assessment', label:'AD/A/B/C Scale'},
    '15_Teacher_QuickRef':{section:'Assessment', label:'Teacher QuickRef'},
    '16_Change_Log':{section:'Admin', label:'Change Log'},
    '17_Rubrics_Ready':{section:'Assessment', label:'Rubrics Ready'},
    '18_Detail_G1_G5':{section:'Units', label:'Detail G1–G5'},
    '19_Detail_G6_G11':{section:'Units', label:'Detail G6–G11'},
    '20_Units_Full_G1_G11':{section:'Units', label:'Full Detail'},
    '21_Immersion_Framework':{section:'Immersion', label:'Framework'},
    '22_Teaching_Strategies':{section:'Immersion', label:'Strategies'},
    '23_Parent_Guide':{section:'Immersion', label:'Parent Guide'},
  };
  let crumbs;
  if (tabId.startsWith('_grade_')) crumbs = { section:'Home', label: tabId.replace('_grade_','') + ' · deep-dive' };
  else crumbs = tabToSection[tabId] || { section:'Home', label: tabId };
  return (
    <div className="px-6 py-2 border-b border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-xs text-slate-500 dark:text-slate-400 flex items-center gap-2 no-print">
      <span>Home</span>
      <span className="text-slate-300">›</span>
      <span>{crumbs.section}</span>
      <span className="text-slate-300">›</span>
      <span className="text-nordic-600 dark:text-nordic-300 font-medium">{crumbs.label}</span>
    </div>
  );
}

// ============= LOGIN =============
function LoginPage({ onLogin }) {
  const [email, setEmail] = useState(localStorage.getItem(LS.rememberEmail) || '');
  const [password, setPassword] = useState('');
  const [remember, setRemember] = useState(!!localStorage.getItem(LS.rememberEmail));
  const [error, setError] = useState('');
  const [showForgot, setShowForgot] = useState(false);

  const submit = (e) => {
    e.preventDefault();
    const user = loadUsers().find(u => u.email.toLowerCase() === email.toLowerCase() && u.password === password);
    if (user) {
      const sessionTTL = remember ? 30*24*60*60*1000 : 12*60*60*1000; // 30d vs 12h
      if (remember) localStorage.setItem(LS.rememberEmail, email);
      else localStorage.removeItem(LS.rememberEmail);
      localStorage.setItem(LS.auth, JSON.stringify({ id: user.id, ts: Date.now(), expires: Date.now() + sessionTTL }));
      onLogin(user);
    } else setError('Invalid email or password');
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-nordic-50 via-white to-nordic-100 dark:from-slate-900 dark:via-slate-800 dark:to-nordic-900 p-4">
      <div className="max-w-md w-full bg-white dark:bg-slate-800 rounded-2xl shadow-2xl p-8 border border-nordic-100 dark:border-slate-700 animate-slide-up">
        <div className="mb-4"><NordicLogo/></div>
        <p className="text-center text-sm text-slate-600 dark:text-slate-300 mb-6">Master Scope &amp; Sequence Portal</p>
        <form onSubmit={submit} className="space-y-4">
          <div>
            <label className="block text-xs font-medium text-slate-600 dark:text-slate-300 mb-1">Email</label>
            <input type="email" required autoFocus value={email} onChange={e=>setEmail(e.target.value)}
              className="w-full px-4 py-2.5 rounded-lg border border-slate-200 dark:border-slate-600 dark:bg-slate-700 focus:ring-2 focus:ring-nordic-400 outline-none"/>
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-600 dark:text-slate-300 mb-1">Password</label>
            <input type="password" required value={password} onChange={e=>setPassword(e.target.value)}
              className="w-full px-4 py-2.5 rounded-lg border border-slate-200 dark:border-slate-600 dark:bg-slate-700 focus:ring-2 focus:ring-nordic-400 outline-none"/>
          </div>
          <div className="flex items-center justify-between">
            <label className="flex items-center gap-2 text-xs text-slate-600 dark:text-slate-300 cursor-pointer">
              <input type="checkbox" checked={remember} onChange={e=>setRemember(e.target.checked)}
                className="rounded border-slate-300 text-nordic-600 focus:ring-nordic-400"/>
              Remember me
            </label>
            <button type="button" onClick={()=>setShowForgot(true)} className="text-xs text-nordic-600 hover:underline">Forgot password?</button>
          </div>
          {error && <div className="text-sm text-red-600 bg-red-50 dark:bg-red-900/30 px-3 py-2 rounded">{error}</div>}
          <button type="submit" className="w-full py-3 bg-nordic-700 hover:bg-nordic-600 text-white font-medium rounded-lg transition shadow-lg hover:shadow-xl">Sign In</button>
        </form>
        <p className="text-[11px] text-center text-slate-400 mt-6">English Immersion Program · Lima, Perú</p>
      </div>
      {showForgot && <ForgotPasswordModal onClose={()=>setShowForgot(false)}/>}
    </div>
  );
}

function ForgotPasswordModal({ onClose }) {
  const [email, setEmail] = useState('');
  const [state, setState] = useState('idle');   // idle|sent|not_found
  const admin = loadUsers().find(u => u.role === 'admin');

  const submit = (e) => {
    e.preventDefault();
    const user = loadUsers().find(u => u.email.toLowerCase() === email.toLowerCase());
    if (!user) { setState('not_found'); return; }
    const req = { id:'r_'+Date.now(), email:user.email, userId:user.id, userName:user.name, ts:Date.now(), status:'pending' };
    const list = loadResets(); list.unshift(req); saveResets(list);
    // Open mailto to administrator
    const subj = encodeURIComponent('[NIS English Portal] Password reset request');
    const body = encodeURIComponent(`Hello ${admin?.name || 'Administrator'},%0D%0A%0D%0AI need to reset my password for the NIS English Department Portal.%0D%0A%0D%0AMy email: ${user.email}%0D%0AName: ${user.name}%0D%0ARequest date: ${new Date().toLocaleString()}%0D%0A%0D%0APlease assign me a new password and confirm via email.%0D%0A%0D%0AThank you.`);
    const mailto = `mailto:${admin?.email || ''}?subject=${subj}&body=${body}`;
    window.location.href = mailto;
    setState('sent');
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4 animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-xl shadow-2xl max-w-md w-full p-6 animate-slide-up" onClick={e=>e.stopPropagation()}>
        <div className="flex items-start justify-between mb-4">
          <h3 className="text-lg font-semibold text-nordic-700 dark:text-nordic-200">Reset password</h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 text-2xl">×</button>
        </div>
        {state === 'idle' && (<>
          <p className="text-sm text-slate-600 dark:text-slate-300 mb-4">Enter your registered email. A reset request will be sent to the administrator, and your email client will open with a pre-filled request.</p>
          <form onSubmit={submit} className="space-y-4">
            <input type="email" required autoFocus value={email} onChange={e=>setEmail(e.target.value)} placeholder="your.email@example.com"
              className="w-full px-4 py-2.5 rounded-lg border border-slate-200 dark:border-slate-600 dark:bg-slate-700 focus:ring-2 focus:ring-nordic-400 outline-none"/>
            <button type="submit" className="w-full py-2.5 bg-nordic-700 hover:bg-nordic-600 text-white font-medium rounded-lg transition">Send reset request</button>
          </form>
        </>)}
        {state === 'not_found' && (
          <div>
            <div className="p-3 bg-red-50 dark:bg-red-900/30 rounded text-sm text-red-700 dark:text-red-300">This email is not registered. Please contact the administrator directly: <b>{admin?.email}</b></div>
            <button onClick={()=>setState('idle')} className="mt-4 text-sm text-nordic-600 hover:underline">← Try again</button>
          </div>
        )}
        {state === 'sent' && (
          <div>
            <div className="p-4 bg-emerald-50 dark:bg-emerald-900/30 rounded text-sm text-emerald-700 dark:text-emerald-300">
              <div className="font-semibold mb-1">✓ Reset request sent</div>
              <div>The administrator ({admin?.email}) has been notified. Your email client should have opened with a pre-filled message — just click send.</div>
              <div className="mt-2 text-xs">You'll receive your new password from the administrator shortly.</div>
            </div>
            <button onClick={onClose} className="mt-4 w-full py-2.5 bg-nordic-700 hover:bg-nordic-600 text-white text-sm rounded-lg">Close</button>
          </div>
        )}
      </div>
    </div>
  );
}

// ============= DASHBOARD =============
function Dashboard({ onNavigate, user, progress }) {
  const today = new Date();
  const mock1 = new Date(today.getFullYear(), 4, 15);    // May 15
  const mock2 = new Date(today.getFullYear(), 9, 15);    // Oct 15
  const official = new Date(today.getFullYear(), 11, 2); // Dec 2
  const daysTo = (d) => Math.max(0, Math.ceil((d - today) / (1000*60*60*24)));

  const totalUnits = Object.keys(GRADE_LEVELS).length * 6;
  const clilRows = MASTER_DATA.sheets['12_CLIL_Map']?.rows || [];
  const totalClil = clilRows.filter(r => r[0] && /^G\d+$/.test(String(r[0].v))).length;
  const totalRubrics = (MASTER_DATA.sheets['17_Rubrics_Ready']?.rows || []).length - 3;

  const stats = [
    { label: 'Grades', value: 11, accent: 'from-nordic-400 to-nordic-600', tab: '01_Pathway' },
    { label: 'Units total', value: totalUnits, accent: 'from-emerald-400 to-emerald-600', tab: '10_Units_G1_G5' },
    { label: 'CLIL projects', value: totalClil, accent: 'from-amber-400 to-amber-600', tab: '12_CLIL_Map' },
    { label: 'Activity rubrics', value: totalRubrics, accent: 'from-rose-400 to-rose-600', tab: '17_Rubrics_Ready' },
  ];

  const examMilestones = [
    { name: 'Mock Exam 1', date: mock1, days: daysTo(mock1), label: 'May 15', color: 'bg-blue-500' },
    { name: 'Mock Exam 2', date: mock2, days: daysTo(mock2), label: 'Oct 15', color: 'bg-indigo-500' },
    { name: 'Official Cambridge', date: official, days: daysTo(official), label: 'Dec 2', color: 'bg-rose-500' },
  ];

  const quickLinks = [
    { label: 'Teacher QuickRef', tab: '15_Teacher_QuickRef', emoji: '👩‍🏫' },
    { label: 'Rubrics Ready', tab: '17_Rubrics_Ready', emoji: '📋' },
    { label: 'Parent Guide', tab: '23_Parent_Guide', emoji: '👨‍👩‍👧' },
    { label: 'Immersion Framework', tab: '21_Immersion_Framework', emoji: '🌐' },
    { label: 'Cambridge Calendar', tab: '13_Cambridge_Calendar', emoji: '📅' },
    { label: 'Grammar by Grade', tab: '04_Grammar', emoji: '📝' },
  ];

  return (
    <div className="p-6 overflow-auto h-full animate-fade-in">
      <div className="max-w-7xl mx-auto space-y-6">
        <div>
          <h1 className="text-3xl font-bold text-slate-900 dark:text-white">Welcome, {user.name.split(' ')[0]} 👋</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">English Immersion Program · Cambridge Pathway 2026</p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {stats.map(s => (
            <button key={s.label} onClick={()=>onNavigate(s.tab)}
              className={`p-5 rounded-xl bg-gradient-to-br ${s.accent} text-white shadow-lg hover:shadow-xl hover:scale-105 transition-all text-left`}>
              <div className="text-4xl font-bold">{s.value}</div>
              <div className="text-xs uppercase tracking-widest opacity-90 mt-1">{s.label}</div>
            </button>
          ))}
        </div>

        <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
          <div className="flex items-center justify-between mb-4">
            <h2 className="font-semibold text-slate-800 dark:text-slate-100">Upcoming Cambridge milestones</h2>
            <button onClick={()=>onNavigate('13_Cambridge_Calendar')} className="text-xs text-nordic-600 hover:underline">View calendar →</button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {examMilestones.map(m => (
              <div key={m.name} className="p-4 bg-slate-50 dark:bg-slate-700/50 rounded-lg">
                <div className="flex items-center gap-2 mb-1">
                  <div className={`w-2 h-2 rounded-full ${m.color}`}/>
                  <span className="text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400">{m.label}</span>
                </div>
                <div className="text-lg font-semibold text-slate-800 dark:text-slate-100">{m.name}</div>
                <div className="text-3xl font-bold text-nordic-600 dark:text-nordic-300 mt-1">
                  {m.days > 0 ? `${m.days}` : '—'}
                  <span className="text-xs text-slate-400 ml-1">days</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
          <h2 className="font-semibold text-slate-800 dark:text-slate-100 mb-4">Grade overview · click to deep-dive</h2>
          <div className="grid grid-cols-3 md:grid-cols-6 lg:grid-cols-11 gap-2">
            {Object.entries(GRADE_LEVELS).map(([g, info]) => {
              const taught = [1,2,3,4,5,6].filter(u => progress[`${g}::U${u}`]?.status === 'taught').length;
              const inProg = [1,2,3,4,5,6].filter(u => progress[`${g}::U${u}`]?.status === 'in-progress').length;
              return (
                <button key={g} onClick={()=>onNavigate('_grade_' + g)}
                  style={{ backgroundColor: info.color }}
                  className="p-3 rounded-lg hover:scale-105 transition text-slate-800 text-center shadow-sm hover:shadow-md">
                  <div className="font-bold text-lg">{g}</div>
                  <div className="text-[10px] uppercase tracking-wider opacity-80">{info.cefr}</div>
                  <div className="text-[11px] mt-1 font-medium">{info.exam}</div>
                  <div className="mt-2 bg-white/40 rounded-full h-1.5 overflow-hidden">
                    <div className="h-full bg-emerald-600" style={{width: `${(taught/6)*100}%`}}/>
                  </div>
                  <div className="text-[9px] mt-1 opacity-70">{taught}/6 taught{inProg ? ` · ${inProg} in progress`:''}</div>
                </button>
              );
            })}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-1">📚 Vocabulary (cumulative)</h3>
            <p className="text-xs text-slate-500 mb-3">Target words known by end of grade</p>
            <BarChart data={[
              {label:'G1',value:150},{label:'G2',value:450},{label:'G3',value:800},{label:'G4',value:1350},
              {label:'G5',value:2500},{label:'G6',value:3000},{label:'G7',value:3400},{label:'G8',value:3800},
              {label:'G9',value:4500},{label:'G10',value:5000},{label:'G11',value:6000}
            ]} height={180}/>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-1">📝 Grammar topics per grade</h3>
            <p className="text-xs text-slate-500 mb-3">Distinct grammar focus areas introduced</p>
            <BarChart data={[
              {label:'G1',value:6},{label:'G2',value:8},{label:'G3',value:8},{label:'G4',value:9},
              {label:'G5',value:10},{label:'G6',value:8},{label:'G7',value:9},{label:'G8',value:8},
              {label:'G9',value:10},{label:'G10',value:10},{label:'G11',value:10}
            ]} height={180} max={12}/>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-1">📖 Reading — max text length</h3>
            <p className="text-xs text-slate-500 mb-3">Words per text (end-of-grade target)</p>
            <BarChart data={[
              {label:'G1',value:50},{label:'G2',value:60},{label:'G3',value:100},{label:'G4',value:150},
              {label:'G5',value:250},{label:'G6',value:300},{label:'G7',value:450},{label:'G8',value:600},
              {label:'G9',value:1000},{label:'G10',value:1300},{label:'G11',value:1500}
            ]} height={180}/>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-1">✏ Writing — classroom word count</h3>
            <p className="text-xs text-slate-500 mb-3">Max target words per written task</p>
            <BarChart data={[
              {label:'G1',value:25},{label:'G2',value:40},{label:'G3',value:70},{label:'G4',value:100},
              {label:'G5',value:150},{label:'G6',value:180},{label:'G7',value:250},{label:'G8',value:260},
              {label:'G9',value:380},{label:'G10',value:450},{label:'G11',value:500}
            ]} height={180}/>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-1">🎧 Listening — exam duration (min)</h3>
            <p className="text-xs text-slate-500 mb-3">Cambridge exam listening paper length</p>
            <BarChart data={[
              {label:'G1',value:3},{label:'G2',value:20},{label:'G3',value:22},{label:'G4',value:25},
              {label:'G5',value:25},{label:'G6',value:25},{label:'G7',value:28},{label:'G8',value:30},
              {label:'G9',value:40},{label:'G10',value:40},{label:'G11',value:40}
            ]} height={180} max={45}/>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm p-5 border border-slate-200 dark:border-slate-700">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-1">🌟 Graduate Profile frequency</h3>
            <p className="text-xs text-slate-500 mb-3">How often each competency appears across units</p>
            <div className="flex items-center justify-center text-slate-500 dark:text-slate-300">
              <RadarChart size={220} data={[
                {label:'Critical', value:10},{label:'Communicative', value:9},
                {label:'Social-em.', value:7},{label:'Global cit.', value:9},
                {label:'Digital', value:5},{label:'Cultural', value:6},
                {label:'Ethical', value:6},{label:'Artistic', value:4},
                {label:'Healthy', value:5},{label:'Entrepren.', value:4}
              ]}/>
            </div>
          </div>
        </div>

        <div>
          <h2 className="font-semibold text-slate-800 dark:text-slate-100 mb-3">Quick access</h2>
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3">
            {quickLinks.map(q => (
              <button key={q.tab} onClick={()=>onNavigate(q.tab)}
                className="p-4 bg-white dark:bg-slate-800 rounded-lg shadow-sm hover:shadow-md border border-slate-200 dark:border-slate-700 transition text-left">
                <div className="text-2xl mb-2">{q.emoji}</div>
                <div className="text-xs font-medium text-slate-700 dark:text-slate-200">{q.label}</div>
              </button>
            ))}
          </div>
        </div>

        <div className="bg-nordic-50 dark:bg-nordic-900/30 border border-nordic-200 dark:border-nordic-700 rounded-xl p-5">
          <div className="flex items-start gap-3">
            <div className="text-2xl">💡</div>
            <div>
              <h3 className="font-semibold text-nordic-800 dark:text-nordic-200">Tip: Press <span className="kbd">Ctrl</span> + <span className="kbd">K</span> to quickly jump to any tab</h3>
              <p className="text-sm text-slate-600 dark:text-slate-400 mt-1">Or press <span className="kbd">?</span> to see all keyboard shortcuts</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// ============= COMMAND PALETTE (Ctrl+K) =============
function CommandPalette({ open, onClose, onNavigate }) {
  const [q, setQ] = useState('');
  const inputRef = useRef(null);
  useEffect(() => { if (open) { setQ(''); setTimeout(()=>inputRef.current?.focus(), 50); } }, [open]);

  const results = useMemo(() => {
    const query = q.toLowerCase().trim();
    const items = [{ id:'_dashboard', label:'🏠 Dashboard' }, ...ALL_TABS.map(t => ({ id:t, label:t.replace(/_/g,' ') }))];
    if (!query) return items.slice(0, 10);
    return items.filter(i => i.label.toLowerCase().includes(query)).slice(0, 10);
  }, [q]);

  const [sel, setSel] = useState(0);
  useEffect(() => setSel(0), [q]);

  const onKey = (e) => {
    if (e.key === 'ArrowDown') { e.preventDefault(); setSel(s => Math.min(s+1, results.length-1)); }
    if (e.key === 'ArrowUp') { e.preventDefault(); setSel(s => Math.max(s-1, 0)); }
    if (e.key === 'Enter') { e.preventDefault(); const r = results[sel]; if (r) { onNavigate(r.id); onClose(); } }
    if (e.key === 'Escape') onClose();
  };

  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 bg-black/40 animate-fade-in" onClick={onClose}>
      <div className="max-w-xl mx-auto mt-20 bg-white dark:bg-slate-800 rounded-xl shadow-2xl animate-slide-up" onClick={e=>e.stopPropagation()}>
        <input ref={inputRef} value={q} onChange={e=>setQ(e.target.value)} onKeyDown={onKey}
          placeholder="Jump to tab... (↑ ↓ Enter)"
          className="w-full px-4 py-3 bg-transparent border-b border-slate-200 dark:border-slate-700 outline-none text-sm"/>
        <div className="max-h-96 overflow-y-auto p-2">
          {results.map((r, i) => (
            <button key={r.id} onClick={() => { onNavigate(r.id); onClose(); }}
              onMouseEnter={() => setSel(i)}
              className={`w-full text-left px-3 py-2 text-sm rounded transition ${i === sel ? 'bg-nordic-600 text-white' : 'text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700'}`}>
              {r.label}
            </button>
          ))}
          {results.length === 0 && <div className="px-3 py-6 text-center text-sm text-slate-400">No matches</div>}
        </div>
        <div className="px-4 py-2 border-t border-slate-200 dark:border-slate-700 text-[10px] text-slate-400 flex gap-3">
          <span><span className="kbd">↑↓</span> Navigate</span>
          <span><span className="kbd">Enter</span> Select</span>
          <span><span className="kbd">Esc</span> Close</span>
        </div>
      </div>
    </div>
  );
}

// ============= VISUAL CAMBRIDGE CALENDAR =============
function VisualCalendar() {
  const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const phases = [
    { label:'Diagnostic CEFR', start:2, end:2, color:'bg-slate-400' },
    { label:'Pre-Mock 1 prep', start:2, end:3, color:'bg-nordic-300' },
    { label:'🎯 MOCK 1', start:4, end:4, color:'bg-blue-500', star:true },
    { label:'Analysis + re-prioritise', start:5, end:5, color:'bg-slate-400' },
    { label:'Intensive prep', start:5, end:6, color:'bg-nordic-500' },
    { label:'Consolidation + speaking', start:7, end:8, color:'bg-emerald-400' },
    { label:'🎯 MOCK 2', start:9, end:9, color:'bg-indigo-500', star:true },
    { label:'Final prep + enrol', start:9, end:10, color:'bg-amber-400' },
    { label:'🎯 OFFICIAL EXAM (Dec 2)', start:11, end:11, color:'bg-rose-500', star:true },
    { label:'Results + 2027 plan', start:11, end:11, color:'bg-violet-400' },
  ];
  const today = new Date();
  return (
    <div className="p-6 overflow-auto h-full animate-fade-in">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-2xl font-bold text-slate-900 dark:text-white mb-1">Cambridge Calendar 2026</h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mb-6">Visual Gantt — mocks + official exam schedule</p>
        <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm border border-slate-200 dark:border-slate-700 p-6">
          <div className="relative">
            <div className="grid grid-cols-12 gap-1 mb-4">
              {months.map((m, i) => (
                <div key={m} className={`text-center text-xs font-medium py-2 rounded ${i === today.getMonth() ? 'bg-nordic-600 text-white' : 'text-slate-500 dark:text-slate-400'}`}>
                  {m}
                </div>
              ))}
            </div>
            <div className="space-y-2.5">
              {phases.map((p, idx) => (
                <div key={idx} className="grid grid-cols-12 gap-1 items-center group">
                  {months.map((_, mi) => {
                    const inRange = mi >= p.start && mi <= p.end;
                    if (!inRange) return <div key={mi} className="h-8"/>;
                    const isStart = mi === p.start;
                    const isEnd = mi === p.end;
                    return (
                      <div key={mi} className={`h-8 ${p.color} ${isStart ? 'rounded-l-lg' : ''} ${isEnd ? 'rounded-r-lg' : ''} flex items-center justify-center shadow-sm group-hover:scale-y-110 transition-transform`}>
                        {isStart && (
                          <span className="text-white text-xs font-medium px-2 truncate">{p.label}</span>
                        )}
                      </div>
                    );
                  })}
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4">
          {[{label:'Mock 1',date:'May 15',color:'bg-blue-500'},{label:'Mock 2',date:'Oct 15',color:'bg-indigo-500'},{label:'Official Exam',date:'Dec 2',color:'bg-rose-500'}].map(m => (
            <div key={m.label} className="bg-white dark:bg-slate-800 p-4 rounded-xl border border-slate-200 dark:border-slate-700">
              <div className="flex items-center gap-2 mb-2"><div className={`w-3 h-3 ${m.color} rounded-full`}/><span className="text-xs uppercase tracking-wider text-slate-500">{m.label}</span></div>
              <div className="text-2xl font-bold text-slate-800 dark:text-slate-100">{m.date}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ============= VISUAL CLIL GRID =============
function VisualCLIL({ onCellClick }) {
  const clilRows = MASTER_DATA.sheets['12_CLIL_Map']?.rows || [];
  const byGradeUnit = {};
  clilRows.forEach(row => {
    if (!row[0]) return;
    const grade = String(row[0].v);
    if (!/^G\d+$/.test(grade)) return;
    const unit = String(row[1]?.v || '').match(/U(\d)/)?.[1];
    if (!unit) return;
    byGradeUnit[`${grade}_U${unit}`] = {
      theme: String(row[1]?.v || ''),
      subjects: String(row[2]?.v || ''),
      project: String(row[3]?.v || ''),
      output: String(row[4]?.v || ''),
      assessment: String(row[5]?.v || ''),
    };
  });
  const grades = Object.keys(GRADE_LEVELS);
  const units = [1,2,3,4,5,6];
  return (
    <div className="p-6 overflow-auto h-full animate-fade-in">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-2xl font-bold text-slate-900 dark:text-white mb-1">CLIL Cross-Curricular Map</h1>
        <p className="text-sm text-slate-500 dark:text-slate-400 mb-6">66 projects · 11 grades × 6 units · Click any cell for details</p>
        <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm border border-slate-200 dark:border-slate-700 p-4 overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr>
                <th className="text-xs font-medium text-slate-500 p-2">Grade</th>
                {units.map(u => <th key={u} className="text-xs font-medium text-slate-500 p-2">Unit {u}</th>)}
              </tr>
            </thead>
            <tbody>
              {grades.map(g => (
                <tr key={g}>
                  <td className="p-2">
                    <div style={{backgroundColor: GRADE_LEVELS[g].color}} className="px-3 py-2 rounded text-slate-800 text-center text-sm">
                      <div className="font-bold">{g}</div>
                      <div className="text-[10px] opacity-80">{GRADE_LEVELS[g].exam}</div>
                    </div>
                  </td>
                  {units.map(u => {
                    const cell = byGradeUnit[`${g}_U${u}`];
                    if (!cell) return <td key={u} className="p-2"><div className="h-16 bg-slate-100 dark:bg-slate-700 rounded"/></td>;
                    return (
                      <td key={u} className="p-2">
                        <button onClick={()=>onCellClick(cell, g, u)}
                          className="w-full h-20 bg-gradient-to-br from-nordic-50 to-nordic-100 dark:from-slate-700 dark:to-slate-600 hover:from-nordic-100 hover:to-nordic-200 dark:hover:from-slate-600 dark:hover:to-slate-500 rounded-lg p-2 text-left transition border border-nordic-100 dark:border-slate-600 hover:shadow-md">
                          <div className="text-[11px] font-semibold text-nordic-800 dark:text-nordic-200 line-clamp-2">{cell.project}</div>
                          <div className="text-[10px] text-slate-500 dark:text-slate-400 mt-1 line-clamp-1">{cell.subjects.split('+')[0]}</div>
                        </button>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

function CLILDetail({ data, onClose, onOpenFullUnit }) {
  if (!data) return null;
  return (
    <div className="fixed inset-0 z-50 bg-black/50 flex items-end md:items-center justify-center animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-t-2xl md:rounded-xl max-w-xl w-full p-6 shadow-2xl animate-slide-up" onClick={e=>e.stopPropagation()}>
        <div className="flex items-start justify-between mb-4">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <span className="grade-chip" style={{backgroundColor: GRADE_LEVELS[data.grade].color}}>{data.grade}</span>
              <span className="text-xs text-slate-500">Unit {data.unit} · {GRADE_LEVELS[data.grade].exam}</span>
            </div>
            <h3 className="text-xl font-bold text-slate-800 dark:text-slate-100">{data.cell.project}</h3>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 text-2xl">×</button>
        </div>
        <div className="space-y-3 text-sm">
          <div><div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Theme</div><div>{data.cell.theme}</div></div>
          <div><div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Partner subjects</div><div className="font-medium">{data.cell.subjects}</div></div>
          <div><div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Target output</div><div>{data.cell.output}</div></div>
          <div><div className="text-xs text-slate-500 uppercase tracking-wider mb-1">Assessment</div><div>{data.cell.assessment}</div></div>
        </div>
        <button onClick={()=>{ onClose(); onOpenFullUnit(data.grade, data.unit, 'clil'); }}
          className="mt-5 w-full py-3 bg-nordic-700 hover:bg-nordic-600 text-white text-sm font-bold rounded-lg transition tracking-wide">
          FULL CLIL CONTENT →
        </button>
      </div>
    </div>
  );
}

// ============= TAB CONTENT (standard) =============
function StandardTabContent({ tabId, canEdit, overrides, onEditCell, onCellDetail, favorites, onToggleFav, comments }) {
  const sheet = MASTER_DATA.sheets[tabId];
  const [search, setSearch] = useState('');
  const [searchInput, setSearchInput] = useState('');
  if (!sheet) return <div className="p-8 text-slate-500">Tab not found</div>;
  const isFav = favorites.includes(tabId);
  const filterRows = (rows) => !search.trim() ? rows : rows.filter((r, i) => i < 2 || r.some(c => String(c.v || '').toLowerCase().includes(search.toLowerCase())));
  const rows = filterRows(sheet.rows);
  const cellKey = (ri, ci) => `${tabId}::${ri}::${ci}`;
  const getVal = (ri, ci, original) => overrides[cellKey(ri, ci)] !== undefined ? overrides[cellKey(ri, ci)] : original;
  return (
    <div className="flex flex-col h-full animate-fade-in">
      <div className="px-6 py-4 bg-white dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 flex items-center justify-between gap-4 no-print">
        <div className="flex items-center gap-3">
          <h2 className="text-xl font-semibold text-nordic-700 dark:text-nordic-200">{tabId.replace(/_/g,' ')}</h2>
          <button onClick={()=>onToggleFav(tabId)} className="text-lg hover:scale-110 transition" title={isFav ? 'Remove from favorites' : 'Add to favorites'}>
            {isFav ? '⭐' : '☆'}
          </button>
          <span className="text-xs text-slate-500 dark:text-slate-400">{sheet.rows.length} rows{canEdit && ' · ✏ Edit mode ACTIVE'}</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="relative">
            <input placeholder="Search in this tab..." value={searchInput} onChange={e=>setSearchInput(e.target.value)}
              onKeyDown={e=>{ if (e.key==='Enter') setSearch(searchInput); if (e.key==='Escape') { setSearchInput(''); setSearch(''); } }}
              className="pl-9 pr-9 py-1.5 text-sm rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 focus:ring-2 focus:ring-nordic-400 outline-none w-64"/>
            <button onClick={()=>setSearch(searchInput)} title="Search (or press Enter)"
              className="absolute left-0 top-0 h-full px-2 text-slate-400 hover:text-nordic-600">
              <svg xmlns="http://www.w3.org/2000/svg" className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
                <circle cx="11" cy="11" r="7"/><path strokeLinecap="round" d="M21 21l-4.3-4.3"/>
              </svg>
            </button>
            {search && (
              <button onClick={()=>{ setSearchInput(''); setSearch(''); }} title="Clear (Esc)"
                className="absolute right-0 top-0 h-full px-2 text-slate-400 hover:text-red-500 text-lg leading-none">×</button>
            )}
          </div>
          <ExportButton tabId={tabId} sheet={sheet}/>
        </div>
      </div>
      <div className="flex-1 overflow-auto p-4 bg-slate-50 dark:bg-slate-900">
        <div className="bg-white dark:bg-slate-800 rounded-lg shadow-sm border border-slate-100 dark:border-slate-700 overflow-auto" style={{maxHeight: 'calc(100vh - 180px)'}}>
          <table className="text-xs border-collapse" style={{minWidth: '100%', width: 'max-content'}}>
            <tbody>
              {rows.map((row, ri) => {
                const darkFillCount = row.filter(c => c.f && isDarkColor(c.f)).length;
                const isHeader = ri < 6 && darkFillCount >= Math.min(3, row.length);
                // Detect grade change between rows
                const thisGrade = (String(row[0]?.v || '').match(/^(G\d+|Grade\s*\d+)/) || [])[0];
                const prevGrade = ri > 0 ? (String(rows[ri-1][0]?.v || '').match(/^(G\d+|Grade\s*\d+)/) || [])[0] : null;
                const gradeChanged = thisGrade && prevGrade && thisGrade !== prevGrade;
                return (
                  <tr key={ri} className={isHeader ? '' : 'tab-row'} style={gradeChanged ? {borderTop: '4px solid #2E5B9E'} : undefined}>
                    {row.map((cell, ci) => {
                      const val = getVal(ri, ci, cell.v);
                      const isOverride = overrides[cellKey(ri, ci)] !== undefined;
                      const darkFill = cell.f && isDarkColor(cell.f);
                      const valLen = String(val || '').length;
                      const isShort = valLen > 0 && valLen <= 30 && !val.includes('\n');
                      const style = {
                        backgroundColor: cell.f || undefined,
                        fontWeight: isShort ? 700 : (cell.b ? 600 : 400),
                        fontSize: isShort ? '13px' : '11px',
                        verticalAlign: isShort ? 'middle' : 'top',
                        textAlign: isShort ? 'center' : 'left',
                        padding: isShort ? '12px 10px' : '10px 12px',
                        lineHeight: isShort ? 1.3 : 1.5,
                        borderRight: '1px solid rgba(0,0,0,0.05)',
                        borderBottom: '1px solid rgba(0,0,0,0.05)',
                        minWidth: '120px',
                        maxWidth: '360px',
                        whiteSpace: 'pre-wrap',
                        wordBreak: 'break-word',
                        color: darkFill ? '#FFFFFF' : (cell.f ? '#1a202c' : undefined),
                        position: isHeader ? 'sticky' : undefined,
                        top: isHeader ? 0 : undefined,
                        zIndex: isHeader ? 5 : undefined,
                        boxShadow: isHeader ? '0 2px 4px rgba(0,0,0,0.08)' : undefined,
                      };
                      const hasComments = ((comments && comments[cellKey(ri, ci)]) || []).length > 0;
                      return (
                        <td key={ci} style={style}
                            className={`cell-fill ${canEdit ? 'cursor-pointer hover:ring-2 hover:ring-nordic-400' : 'cursor-pointer hover:ring-1 hover:ring-nordic-300'} ${isOverride ? 'ring-2 ring-amber-400' : ''}`}
                            onClick={() => canEdit ? onEditCell(ri, ci, val) : onCellDetail(val, tabId, ri, ci)}>
                          {val}
                          {isOverride && <span className="ml-1 text-amber-600">✎</span>}
                          {hasComments && <span className="ml-1 text-nordic-500">💬</span>}
                        </td>
                      );
                    })}
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

// ============= CELL DETAIL DRAWER =============
function CellDrawer({ data, onClose, currentUser, comments, onSaveComments }) {
  if (!data) return null;
  const cellKey = `${data.tabId}::${data.ri}::${data.ci}`;
  const count = (comments[cellKey] || []).length;
  return (
    <div className="fixed inset-y-0 right-0 w-full max-w-md bg-white dark:bg-slate-800 shadow-2xl z-40 animate-slide-right border-l border-slate-200 dark:border-slate-700 overflow-auto">
      <div className="p-6 min-h-full flex flex-col">
        <div className="flex items-start justify-between mb-4">
          <div>
            <div className="text-xs uppercase tracking-wider text-slate-500 mb-1">Cell detail {count > 0 && <span className="bg-nordic-600 text-white px-1.5 py-0.5 rounded-full text-[9px]">{count} 💬</span>}</div>
            <div className="text-sm font-medium text-slate-700 dark:text-slate-200">{data.tabId.replace(/_/g,' ')}</div>
            <div className="text-xs text-slate-400">Row {data.ri + 1} · Col {data.ci + 1}</div>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 text-2xl leading-none">×</button>
        </div>
        <div className="bg-slate-50 dark:bg-slate-900 rounded p-4 text-sm whitespace-pre-wrap">{data.value || '(empty)'}</div>
        <CommentsPanel cellKey={cellKey} currentUser={currentUser} comments={comments} onSave={onSaveComments}/>
      </div>
    </div>
  );
}

// ============= SIDEBAR =============
function Sidebar({ user, currentTab, onTabChange, onLogout, theme, onThemeToggle, onOpenUserMgmt, onOpenResets, pendingResets, editMode, onToggleEdit, allowedTabs, favorites, onOpenPalette }) {
  const [expandedSection, setExpandedSection] = useState('overview');
  const [collapsed, setCollapsed] = useState(false);
  const sections = {
    dashboard:{ label:'🏠 Dashboard', tabs:['_dashboard'] },
    overview: { label:'📘 Overview',  tabs:['00_Cover','01_Pathway','02_Benchmarks','03_SS_Master'] },
    skills:   { label:'📝 Skills',    tabs:['04_Grammar','05_Vocabulary','06_Phonics','07_Reading','08_Writing','09_Speaking_Listening'] },
    units:    { label:'📚 Units',     tabs:['10_Units_G1_G5','11_Units_G6_G11','18_Detail_G1_G5','19_Detail_G6_G11','20_Units_Full_G1_G11'] },
    clil:     { label:'🧩 CLIL',      tabs:['12_CLIL_Map'] },
    calendar: { label:'📅 Calendar',  tabs:['13_Cambridge_Calendar'] },
    assess:   { label:'🎯 Assessment',tabs:['14_Assessment_Scale','17_Rubrics_Ready','15_Teacher_QuickRef'] },
    immersion:{ label:'🌐 Immersion', tabs:['21_Immersion_Framework','22_Teaching_Strategies','23_Parent_Guide'] },
    admin:    { label:'🛠 Admin',     tabs: user.role === 'admin' ? ['16_Change_Log','_activity'] : ['16_Change_Log'] },
  };
  const canSeeTab = (t) => t === '_dashboard' || t === '_activity' || t.startsWith('_grade_') || allowedTabs === 'all' || (allowedTabs || []).includes(t);
  const niceName = (t) => t === '_dashboard' ? 'Dashboard' : t === '_activity' ? 'Activity Log' : t.startsWith('_grade_') ? t.replace('_grade_','') + ' deep-dive' : t.replace(/_/g,' ').replace(/^\d+\s+/,'');

  return (
    <aside className={`${collapsed ? 'w-14' : 'w-64'} bg-white dark:bg-slate-800 border-r border-slate-200 dark:border-slate-700 flex flex-col transition-all duration-200 no-print`}>
      <div className="py-3 px-2 border-b border-slate-100 dark:border-slate-700 flex items-center justify-center min-h-[88px]">
        {!collapsed ? <NordicLogo compact/> : <div className="text-xs font-bold gradient-text text-center">NIS</div>}
      </div>

      {!collapsed && (
        <button onClick={onOpenPalette}
          className="mx-3 mt-3 px-3 py-2 text-left text-xs bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 rounded flex items-center justify-between transition">
          <span className="text-slate-500">🔍 Quick jump...</span>
          <span className="kbd">⌘K</span>
        </button>
      )}

      {favorites.length > 0 && !collapsed && (
        <div className="px-2 mt-3">
          <div className="text-[10px] uppercase tracking-widest text-slate-400 px-2 mb-1">⭐ Favorites</div>
          {favorites.filter(canSeeTab).map(t => (
            <button key={t} onClick={()=>onTabChange(t)}
              className={`w-full text-left px-3 py-1.5 text-xs rounded transition ${currentTab===t ? 'bg-nordic-600 text-white' : 'text-slate-600 dark:text-slate-400 hover:bg-nordic-50 dark:hover:bg-slate-700'}`}>
              {niceName(t)}
            </button>
          ))}
        </div>
      )}

      <nav className="flex-1 overflow-y-auto p-2 space-y-1 mt-2">
        {Object.entries(sections).map(([key, sec]) => {
          const visibleTabs = sec.tabs.filter(canSeeTab);
          if (visibleTabs.length === 0) return null;
          const open = expandedSection === key;
          return (
            <div key={key}>
              <button onClick={()=>setExpandedSection(open ? null : key)}
                className="w-full text-left px-3 py-2 text-[13px] font-medium text-slate-700 dark:text-slate-200 rounded hover:bg-nordic-50 dark:hover:bg-slate-700 flex items-center justify-between">
                <span>{collapsed ? sec.label.split(' ')[0] : sec.label}</span>
                {!collapsed && <span className="text-xs">{open ? '−' : '+'}</span>}
              </button>
              {open && !collapsed && (
                <div className="ml-2 space-y-0.5 mt-1">
                  {visibleTabs.map(t => (
                    <button key={t} onClick={()=>onTabChange(t)}
                      className={`w-full text-left px-3 py-1.5 text-xs rounded transition ${currentTab===t ? 'bg-nordic-600 text-white' : 'text-slate-600 dark:text-slate-400 hover:bg-nordic-50 dark:hover:bg-slate-700'}`}>
                      {niceName(t)}
                    </button>
                  ))}
                </div>
              )}
            </div>
          );
        })}
      </nav>

      <div className="border-t border-slate-100 dark:border-slate-700 p-3 space-y-1">
        <button onClick={onThemeToggle}
          className="w-full flex items-center gap-2 px-3 py-2 text-xs text-slate-600 dark:text-slate-300 hover:bg-nordic-50 dark:hover:bg-slate-700 rounded">
          <span>{theme === 'dark' ? '☀' : '🌙'}</span> {!collapsed && <span>{theme === 'dark' ? 'Light mode' : 'Dark mode'}</span>}
        </button>
        {user.role === 'admin' && (
          <>
            <button onClick={onToggleEdit}
              className={`w-full flex items-center gap-2 px-3 py-2 text-xs rounded transition ${editMode ? 'bg-amber-500 text-white' : 'text-slate-600 dark:text-slate-300 hover:bg-nordic-50 dark:hover:bg-slate-700'}`}>
              <span>✏</span> {!collapsed && <span>{editMode ? 'Editing ON' : 'Edit mode'}</span>}
            </button>
            <button onClick={onOpenUserMgmt}
              className="w-full flex items-center gap-2 px-3 py-2 text-xs text-slate-600 dark:text-slate-300 hover:bg-nordic-50 dark:hover:bg-slate-700 rounded">
              <span>👥</span> {!collapsed && <span>Users</span>}
            </button>
            <button onClick={onOpenResets}
              className="w-full flex items-center gap-2 px-3 py-2 text-xs text-slate-600 dark:text-slate-300 hover:bg-nordic-50 dark:hover:bg-slate-700 rounded relative">
              <span>🔔</span> {!collapsed && <span>Reset requests</span>}
              {pendingResets > 0 && (
                <span className="absolute right-2 top-1 bg-red-500 text-white text-[9px] font-bold px-1.5 py-0.5 rounded-full min-w-[18px] text-center">{pendingResets}</span>
              )}
            </button>
          </>
        )}
        <div className="pt-2 border-t border-slate-100 dark:border-slate-700">
          {!collapsed ? (
            <div className="flex items-center gap-2 px-2 py-2">
              <Avatar name={user.name} size={32}/>
              <div className="min-w-0 flex-1">
                <div className="text-xs font-medium text-slate-700 dark:text-slate-200 truncate">{user.name}</div>
                <div className="text-[10px] text-slate-400 uppercase tracking-wider">{user.role}</div>
              </div>
            </div>
          ) : <div className="flex justify-center py-2"><Avatar name={user.name} size={28}/></div>}
          <button onClick={onLogout} className="w-full flex items-center gap-2 px-3 py-2 text-xs text-red-600 hover:bg-red-50 dark:hover:bg-red-900/30 rounded">
            <span>↪</span> {!collapsed && <span>Sign out</span>}
          </button>
        </div>
        <button onClick={()=>setCollapsed(!collapsed)} className="w-full text-xs text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 py-1">
          {collapsed ? '▶' : '◀'} {!collapsed && 'Collapse'}
        </button>
      </div>
    </aside>
  );
}

// ============= EDIT MODAL =============
function EditModal({ cell, onClose, onSave }) {
  const [value, setValue] = useState(cell.value);
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4 animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-xl shadow-2xl max-w-2xl w-full p-6 animate-slide-up" onClick={e=>e.stopPropagation()}>
        <h3 className="text-lg font-semibold text-nordic-700 dark:text-nordic-200 mb-4">Edit cell</h3>
        <p className="text-xs text-slate-500 mb-2">Sheet: {cell.tabId} · Row {cell.ri + 1} · Column {cell.ci + 1}</p>
        <textarea value={value} onChange={e=>setValue(e.target.value)} autoFocus
          className="w-full p-3 rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 min-h-[200px] text-sm focus:ring-2 focus:ring-nordic-400 outline-none"/>
        <div className="flex justify-end gap-2 mt-4">
          <button onClick={onClose} className="px-4 py-2 text-sm text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded">Cancel</button>
          <button onClick={()=>onSave(value)} className="px-4 py-2 text-sm bg-nordic-700 hover:bg-nordic-600 text-white rounded">Save (Ctrl+S)</button>
        </div>
      </div>
    </div>
  );
}

// ============= USER MANAGEMENT =============
function UserManagement({ onClose }) {
  const [users, setUsers] = useState(loadUsers());
  const [editing, setEditing] = useState(null);
  const save = (u) => { const upd = editing.isNew ? [...users, u] : users.map(x => x.id === u.id ? u : x); setUsers(upd); saveUsers(upd); setEditing(null); };
  const del = (id) => { if (id === 'admin') { alert('Cannot delete the admin'); return; } if (!confirm('Delete this user?')) return; const upd = users.filter(u => u.id !== id); setUsers(upd); saveUsers(upd); };
  const startNew = () => setEditing({ isNew:true, id:'u_'+Date.now(), email:'', name:'', password:'', role:'teacher', tabs:[] });
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4 animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-xl shadow-2xl max-w-4xl w-full max-h-[90vh] flex flex-col animate-slide-up" onClick={e=>e.stopPropagation()}>
        <div className="p-6 border-b border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <h3 className="text-lg font-semibold text-nordic-700 dark:text-nordic-200">User Management</h3>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 text-2xl">×</button>
        </div>
        <div className="flex-1 overflow-auto p-6">
          {!editing ? (<>
            <button onClick={startNew} className="mb-4 px-4 py-2 bg-nordic-700 hover:bg-nordic-600 text-white text-sm rounded">+ Add teacher</button>
            <table className="w-full text-sm">
              <thead className="bg-slate-50 dark:bg-slate-700"><tr>
                <th className="text-left p-3">Name</th><th className="text-left p-3">Email</th><th className="text-left p-3">Role</th><th className="text-left p-3">Tabs</th><th className="text-right p-3">Actions</th>
              </tr></thead>
              <tbody>{users.map(u => (<tr key={u.id} className="border-b border-slate-100 dark:border-slate-700">
                <td className="p-3">{u.name}</td>
                <td className="p-3 text-slate-500">{u.email}</td>
                <td className="p-3"><span className={`px-2 py-0.5 rounded text-xs ${u.role==='admin' ? 'bg-amber-100 text-amber-800' : 'bg-nordic-100 text-nordic-800'}`}>{u.role}</span></td>
                <td className="p-3 text-xs text-slate-500">{u.tabs === 'all' ? 'All tabs' : (u.tabs || []).length + ' tabs'}</td>
                <td className="p-3 text-right space-x-2">
                  <button onClick={()=>setEditing({...u, isNew:false})} className="text-nordic-600 hover:underline text-xs">Edit</button>
                  {u.id !== 'admin' && <button onClick={()=>del(u.id)} className="text-red-600 hover:underline text-xs">Delete</button>}
                </td>
              </tr>))}</tbody>
            </table>
          </>) : <UserEditor user={editing} onSave={save} onCancel={()=>setEditing(null)} />}
        </div>
      </div>
    </div>
  );
}

function UserEditor({ user, onSave, onCancel }) {
  const [form, setForm] = useState(user);
  const toggleTab = (tab) => { if (form.tabs === 'all') { setForm({...form, tabs:[tab]}); return; } const n = (form.tabs || []).includes(tab) ? form.tabs.filter(t=>t!==tab) : [...(form.tabs||[]), tab]; setForm({...form, tabs:n}); };
  return (
    <div className="space-y-4">
      <h4 className="font-medium text-nordic-700 dark:text-nordic-200">{user.isNew ? 'New teacher' : 'Edit user'}</h4>
      <div className="grid grid-cols-2 gap-3">
        <div><label className="text-xs text-slate-600 dark:text-slate-300">Name</label><input value={form.name} onChange={e=>setForm({...form, name:e.target.value})} className="w-full mt-1 px-3 py-2 rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 text-sm"/></div>
        <div><label className="text-xs text-slate-600 dark:text-slate-300">Email</label><input value={form.email} onChange={e=>setForm({...form, email:e.target.value})} className="w-full mt-1 px-3 py-2 rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 text-sm"/></div>
        <div><label className="text-xs text-slate-600 dark:text-slate-300">Password</label><input value={form.password} onChange={e=>setForm({...form, password:e.target.value})} className="w-full mt-1 px-3 py-2 rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 text-sm"/></div>
        <div><label className="text-xs text-slate-600 dark:text-slate-300">Role</label>
          <select value={form.role} onChange={e=>setForm({...form, role:e.target.value})} className="w-full mt-1 px-3 py-2 rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 text-sm">
            <option value="teacher">Teacher</option><option value="admin">Admin</option>
          </select>
        </div>
      </div>
      <div>
        <div className="flex items-center justify-between mb-2">
          <label className="text-xs text-slate-600 dark:text-slate-300">Allowed tabs</label>
          <div className="space-x-2">
            <button onClick={()=>setForm({...form, tabs:'all'})} className="text-xs text-nordic-600 hover:underline">Select all</button>
            <button onClick={()=>setForm({...form, tabs:[]})} className="text-xs text-slate-500 hover:underline">Clear</button>
          </div>
        </div>
        <div className="grid grid-cols-3 gap-2 max-h-[300px] overflow-y-auto border border-slate-100 dark:border-slate-700 rounded p-3">
          {ALL_TABS.map(t => {
            const checked = form.tabs === 'all' || (form.tabs || []).includes(t);
            return (<label key={t} className="flex items-center gap-2 text-xs cursor-pointer">
              <input type="checkbox" checked={checked} onChange={()=>toggleTab(t)} className="rounded"/>
              <span>{t.replace(/_/g,' ')}</span>
            </label>);
          })}
        </div>
      </div>
      <div className="flex justify-end gap-2 pt-4 border-t border-slate-100 dark:border-slate-700">
        <button onClick={onCancel} className="px-4 py-2 text-sm text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 rounded">Cancel</button>
        <button onClick={()=>onSave(form)} className="px-4 py-2 text-sm bg-nordic-700 hover:bg-nordic-600 text-white rounded">Save</button>
      </div>
    </div>
  );
}

// ============= CHART COMPONENTS =============
function RadarChart({ data, size=260 }) {
  // data: [{label, value(0-10)}]
  const n = data.length;
  const cx = size/2, cy = size/2, r = size/2 - 30;
  const pt = (angle, dist) => {
    const rad = angle - Math.PI/2;
    return [cx + Math.cos(rad) * dist, cy + Math.sin(rad) * dist];
  };
  const axisPoints = data.map((_, i) => pt(i * 2*Math.PI/n, r));
  const dataPoints = data.map((d, i) => pt(i * 2*Math.PI/n, r * (d.value/10)));
  const rings = [2, 4, 6, 8, 10];
  const poly = dataPoints.map(p => p.join(',')).join(' ');
  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      {rings.map(v => (
        <polygon key={v} fill="none" stroke="currentColor" strokeOpacity="0.15" strokeWidth="1"
          points={data.map((_, i) => pt(i*2*Math.PI/n, r*v/10).join(',')).join(' ')}/>
      ))}
      {axisPoints.map((p, i) => (
        <line key={i} x1={cx} y1={cy} x2={p[0]} y2={p[1]} stroke="currentColor" strokeOpacity="0.15"/>
      ))}
      <polygon points={poly} fill="#4A7BC8" fillOpacity="0.3" stroke="#2E5B9E" strokeWidth="2"/>
      {dataPoints.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r="3" fill="#1F4E79"/>)}
      {data.map((d, i) => {
        const [x, y] = pt(i*2*Math.PI/n, r + 14);
        return <text key={i} x={x} y={y} fontSize="9" textAnchor="middle" dominantBaseline="middle" fill="currentColor" fillOpacity="0.7">{d.label}</text>;
      })}
    </svg>
  );
}

function BarChart({ data, height=180, max=null }) {
  // data: [{label, value}]
  const maxVal = max || Math.max(...data.map(d => d.value)) * 1.1;
  return (
    <div className="flex items-end gap-2" style={{ height }}>
      {data.map((d, i) => (
        <div key={i} className="flex-1 flex flex-col items-center">
          <div className="text-[10px] font-medium text-slate-600 dark:text-slate-300 mb-1">{d.value}</div>
          <div className="w-full bg-gradient-to-t from-nordic-500 to-nordic-300 rounded-t shadow-sm transition-all hover:from-nordic-600 hover:to-nordic-400"
               style={{ height: `${(d.value/maxVal) * (height-40)}px` }}/>
          <div className="text-[10px] text-slate-500 mt-1 rotate-0">{d.label}</div>
        </div>
      ))}
    </div>
  );
}

// ============= GRADE DEEP-DIVE =============
function GradeDeepDive({ grade, onNavigate, progress, onToggleProgress, onOpenUnit, onOpenCLIL }) {
  const info = GRADE_LEVELS[grade];
  if (!info) return null;

  const pickRow = (sheetId, matchFn) => {
    const sheet = MASTER_DATA.sheets[sheetId]; if (!sheet) return null;
    return sheet.rows.find(row => row.some(c => matchFn(String(c.v || ''))));
  };

  const grammarRow = pickRow('04_Grammar', v => v.startsWith(grade + ' /'));
  const vocabRow = pickRow('05_Vocabulary', v => v.startsWith(grade + ' /'));
  const writingRow = pickRow('08_Writing', v => v.startsWith(grade + ' /'));
  const readingRows = (MASTER_DATA.sheets['07_Reading']?.rows || []).filter(r => String(r[0]?.v || '').startsWith(grade + ' /'));

  // Units for this grade
  const unitSheet = ['G1','G2','G3','G4','G5'].includes(grade) ? '10_Units_G1_G5' : '11_Units_G6_G11';
  const unitRows = (MASTER_DATA.sheets[unitSheet]?.rows || []).filter(r => String(r[0]?.v || '') === grade);

  // CLIL for this grade
  const clilRows = (MASTER_DATA.sheets['12_CLIL_Map']?.rows || []).filter(r => String(r[0]?.v || '') === grade);

  return (
    <div className="p-6 overflow-auto h-full animate-fade-in bg-slate-50 dark:bg-slate-900">
      <div className="max-w-6xl mx-auto space-y-6">
        <button onClick={()=>onNavigate('_dashboard')} className="text-sm text-nordic-600 hover:underline">← Back to dashboard</button>

        <div style={{backgroundColor: info.color}} className="rounded-2xl p-8 shadow-lg text-slate-800 relative overflow-hidden">
          <div className="relative z-10">
            <div className="text-xs uppercase tracking-[0.3em] opacity-70 mb-2">Grade deep-dive</div>
            <h1 className="text-5xl font-black">{grade}</h1>
            <div className="flex items-baseline gap-4 mt-3">
              <span className="text-xl font-semibold">{info.cefr}</span>
              <span className="text-lg opacity-75">·</span>
              <span className="text-xl">{info.exam}</span>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700 md:col-span-3">
            <h3 className="text-xs uppercase tracking-wider text-slate-500 mb-2">📝 Grammar focus — complete progression for {grade}</h3>
            <div className="text-sm whitespace-pre-wrap leading-relaxed">{grammarRow?.[2]?.v || '—'}</div>
            {grammarRow?.[3]?.v && <>
              <h4 className="text-xs uppercase tracking-wider text-slate-500 mt-4 mb-2">💬 Examples</h4>
              <div className="text-sm whitespace-pre-wrap italic text-slate-600 dark:text-slate-300">{grammarRow[3].v}</div>
            </>}
            {grammarRow?.[4]?.v && <div className="mt-3 text-xs text-nordic-600 dark:text-nordic-300">🎯 Exam link: {grammarRow[4].v}</div>}
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700">
            <h3 className="text-xs uppercase tracking-wider text-slate-500 mb-2">📝 This grade uses</h3>
            <div className="text-sm"><b>Hours (grammar):</b> {grammarRow?.[5]?.v || '—'}</div>
            <div className="text-sm mt-2"><b>Target vocab size:</b> {vocabRow?.[4]?.v || '—'}</div>
            <div className="text-sm mt-2"><b>Writing classroom:</b> {writingRow?.[2]?.v || '—'}</div>
            <div className="text-sm mt-2"><b>Writing exam:</b> {writingRow?.[4]?.v || '—'}</div>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700">
            <h3 className="text-xs uppercase tracking-wider text-slate-500 mb-2">📚 Vocabulary</h3>
            <div className="text-sm whitespace-pre-wrap"><b>Themes:</b> {vocabRow?.[1]?.v || '—'}</div>
            <div className="text-sm mt-2"><b>Target size:</b> {vocabRow?.[4]?.v || '—'}</div>
          </div>
          <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700">
            <h3 className="text-xs uppercase tracking-wider text-slate-500 mb-2">✏ Writing</h3>
            <div className="text-sm"><b>Types:</b> {writingRow?.[1]?.v || '—'}</div>
            <div className="text-sm mt-2"><b>Classroom wc:</b> {writingRow?.[2]?.v || '—'}</div>
            <div className="text-sm mt-2"><b>Exam wc:</b> {writingRow?.[4]?.v || '—'}</div>
          </div>
        </div>

        <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700">
          <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-4">📖 Reading plan</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {readingRows.slice(0, 8).map((r, i) => (
              <div key={i} className="p-3 bg-slate-50 dark:bg-slate-700/50 rounded border-l-2 border-nordic-400">
                <div className="text-sm font-medium">{r[1]?.v || '—'}</div>
                <div className="text-xs text-slate-500 mt-1">{r[2]?.v || ''} · {r[3]?.v || ''}</div>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-semibold text-slate-800 dark:text-slate-100">📅 6 Units — track progress</h3>
            <button onClick={()=>onNavigate('10_Units_G1_G5')} className="text-xs text-nordic-600 hover:underline">View full details →</button>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
            {unitRows.map((r, i) => {
              const unit = r[1]?.v || `U${i+1}`;
              const theme = r[2]?.v || '';
              const key = `${grade}::U${i+1}`;
              const status = progress[key]?.status || 'planned';
              const nextStatus = { planned:'in-progress', 'in-progress':'taught', taught:'planned' };
              const statusColor = { planned:'bg-slate-200 text-slate-600', 'in-progress':'bg-amber-200 text-amber-800', taught:'bg-emerald-200 text-emerald-800' };
              return (
                <button key={i} onClick={()=>onOpenUnit(grade, i+1)}
                  className="p-4 bg-slate-50 dark:bg-slate-700/50 rounded-lg hover:bg-nordic-50 dark:hover:bg-slate-700 hover:shadow-md hover:ring-2 hover:ring-nordic-400 transition text-left cursor-pointer">
                  <div className="flex items-center justify-between mb-2">
                    <div className="text-xs font-bold text-nordic-600">{unit}</div>
                    <button onClick={(e)=>{ e.stopPropagation(); onToggleProgress(grade, i+1, nextStatus[status]); }}
                      className={`text-[10px] px-2 py-0.5 rounded-full font-medium ${statusColor[status]}`}>
                      {status === 'taught' ? '✓ Taught' : status === 'in-progress' ? '● In progress' : 'Planned'}
                    </button>
                  </div>
                  <div className="text-sm font-medium">{theme}</div>
                  <div className="text-xs text-slate-500 mt-2 line-clamp-2">{r[3]?.v || ''}</div>
                  <div className="mt-2 text-[10px] text-nordic-600 dark:text-nordic-300 font-medium">Click for full details →</div>
                </button>
              );
            })}
          </div>
        </div>

        <div className="bg-white dark:bg-slate-800 rounded-xl p-5 shadow-sm border border-slate-200 dark:border-slate-700">
          <h3 className="font-semibold text-slate-800 dark:text-slate-100 mb-4">🧩 CLIL projects</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {clilRows.slice(0, 6).map((r, i) => {
              const unitMatch = String(r[1]?.v || '').match(/U(\d)/);
              const uIdx = unitMatch ? parseInt(unitMatch[1]) : (i + 1);
              return (
                <button key={i} onClick={()=>onOpenCLIL(grade, uIdx)}
                  className="p-3 bg-gradient-to-br from-nordic-50 to-nordic-100 dark:from-slate-700 dark:to-slate-600 rounded border border-nordic-200 dark:border-slate-600 hover:shadow-md hover:scale-[1.02] transition text-left cursor-pointer">
                  <div className="text-[10px] uppercase tracking-wider text-nordic-700 dark:text-nordic-300">{r[1]?.v || ''}</div>
                  <div className="text-sm font-semibold mt-1">{r[3]?.v || '—'}</div>
                  <div className="text-xs text-slate-500 mt-1">{r[2]?.v || ''}</div>
                  <div className="mt-2 text-[10px] text-nordic-600 font-medium">Full CLIL content →</div>
                </button>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}

// ============= RESET REQUESTS =============
function ResetRequestsPanel({ onClose, onResolved }) {
  const [list, setList] = useState(loadResets());
  const [resetting, setResetting] = useState(null);
  const [newPwd, setNewPwd] = useState('');

  const resolve = (req) => {
    if (!newPwd || newPwd.length < 6) { pushToast({type:'warn', message:'Password must be at least 6 characters'}); return; }
    const users = loadUsers();
    const upd = users.map(u => u.id === req.userId ? {...u, password:newPwd} : u);
    saveUsers(upd);
    const reqs = loadResets().map(r => r.id === req.id ? {...r, status:'resolved', resolvedTs:Date.now()} : r);
    saveResets(reqs); setList(reqs); setResetting(null); setNewPwd('');
    pushToast({type:'success', message:`Password reset for ${req.userName}. Share new password via email.`});
    onResolved && onResolved();
  };
  const dismiss = (req) => {
    const reqs = loadResets().filter(r => r.id !== req.id);
    saveResets(reqs); setList(reqs);
    onResolved && onResolved();
  };

  const pending = list.filter(r => r.status === 'pending');
  const done = list.filter(r => r.status !== 'pending');

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4 animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-xl shadow-2xl max-w-2xl w-full max-h-[90vh] flex flex-col animate-slide-up" onClick={e=>e.stopPropagation()}>
        <div className="p-6 border-b border-slate-200 dark:border-slate-700 flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold text-nordic-700 dark:text-nordic-200">Password Reset Requests</h3>
            <p className="text-xs text-slate-500 mt-1">{pending.length} pending · {done.length} resolved</p>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-slate-600 text-2xl">×</button>
        </div>
        <div className="flex-1 overflow-auto p-6 space-y-3">
          {pending.length === 0 && <div className="text-center py-8 text-slate-400 text-sm">No pending requests ✓</div>}
          {pending.map(r => (
            <div key={r.id} className="border border-amber-200 dark:border-amber-700 bg-amber-50 dark:bg-amber-900/20 rounded-lg p-4">
              <div className="flex items-start justify-between gap-3">
                <div className="flex items-start gap-3 flex-1">
                  <Avatar name={r.userName} size={36}/>
                  <div className="min-w-0">
                    <div className="font-medium text-sm">{r.userName}</div>
                    <div className="text-xs text-slate-500">{r.email}</div>
                    <div className="text-[10px] text-slate-400 mt-1">Requested {fmtDate(r.ts)}</div>
                  </div>
                </div>
                <span className="px-2 py-0.5 bg-amber-200 text-amber-800 rounded-full text-[10px] font-medium">PENDING</span>
              </div>
              {resetting === r.id ? (
                <div className="mt-3 flex gap-2">
                  <input type="text" placeholder="New password (≥6 chars)" value={newPwd} onChange={e=>setNewPwd(e.target.value)}
                    className="flex-1 px-3 py-1.5 text-xs rounded border border-slate-300 dark:border-slate-600 dark:bg-slate-700 outline-none focus:ring-2 focus:ring-nordic-400"/>
                  <button onClick={()=>resolve(r)} className="px-3 py-1.5 text-xs bg-emerald-600 hover:bg-emerald-700 text-white rounded">Save & resolve</button>
                  <button onClick={()=>{setResetting(null); setNewPwd('');}} className="px-3 py-1.5 text-xs text-slate-500 hover:underline">Cancel</button>
                </div>
              ) : (
                <div className="mt-3 flex gap-2">
                  <button onClick={()=>setResetting(r.id)} className="px-3 py-1.5 text-xs bg-nordic-700 hover:bg-nordic-600 text-white rounded">Set new password</button>
                  <button onClick={()=>dismiss(r)} className="px-3 py-1.5 text-xs text-slate-500 hover:underline">Dismiss</button>
                </div>
              )}
            </div>
          ))}
          {done.length > 0 && (
            <details className="mt-6">
              <summary className="text-xs text-slate-500 cursor-pointer">Show {done.length} resolved</summary>
              <div className="mt-3 space-y-2">
                {done.map(r => (
                  <div key={r.id} className="p-3 border border-slate-200 dark:border-slate-700 rounded text-xs text-slate-500">
                    <div className="flex items-center justify-between">
                      <span>{r.userName} · {r.email}</span>
                      <span className="px-2 py-0.5 bg-emerald-100 text-emerald-800 rounded-full text-[9px]">{r.status}</span>
                    </div>
                  </div>
                ))}
              </div>
            </details>
          )}
        </div>
      </div>
    </div>
  );
}

// ============= UNIT DETAIL (full info per unit) =============
function getUnitFullData(grade, unitIdx) {
  // Aggregates data from multiple sheets for a specific grade+unit
  const unitIdxZero = unitIdx - 1;
  const findInSheet = (sheetId, matcher) => {
    const sheet = MASTER_DATA.sheets[sheetId]; if (!sheet) return null;
    return sheet.rows.find(row => row.some(c => matcher(String(c.v || ''))));
  };
  const getCellsFromRow = (sheetId, matcher) => {
    const row = findInSheet(sheetId, matcher);
    return row ? row.map(c => String(c.v || '')) : [];
  };

  // Grammar row for this grade (sheet 04)
  const gramRow = getCellsFromRow('04_Grammar', v => v.startsWith(grade + ' /'));
  // Vocabulary row (sheet 05)
  const vocabRow = getCellsFromRow('05_Vocabulary', v => v.startsWith(grade + ' /'));
  // Reading rows for this grade (sheet 07)
  const readingRows = (MASTER_DATA.sheets['07_Reading']?.rows || []).filter(r => String(r[0]?.v || '').startsWith(grade + ' /'));
  // Writing row (sheet 08)
  const writingRow = getCellsFromRow('08_Writing', v => v.startsWith(grade + ' /'));
  // Speaking & Listening row (sheet 09)
  const slRow = getCellsFromRow('09_Speaking_Listening', v => v.startsWith(grade + ' /'));

  // Unit-specific row from sheets 10/11
  const unitSheet = ['G1','G2','G3','G4','G5'].includes(grade) ? '10_Units_G1_G5' : '11_Units_G6_G11';
  const unitRow = (MASTER_DATA.sheets[unitSheet]?.rows || []).find(r =>
    String(r[0]?.v || '') === grade && String(r[1]?.v || '') === `U${unitIdx}`);

  // Full unit-level detail from sheet 20
  const full20 = MASTER_DATA.sheets['20_Units_Full_G1_G11']?.rows || [];
  // sheet 20 has rows per sub-block with 6 unit columns (indexes 4-9)
  const fullGradeRows = full20.filter(r => String(r[0]?.v || '') === grade);
  const getSubBlock = (sbName) => {
    const r = fullGradeRows.find(row => String(row[3]?.v || '').toLowerCase().includes(sbName.toLowerCase()));
    return r ? String(r[4 + unitIdxZero]?.v || '').trim() : '';
  };

  // CLIL for grade+unit from sheet 12
  const clilRow = (MASTER_DATA.sheets['12_CLIL_Map']?.rows || []).find(r =>
    String(r[0]?.v || '') === grade && String(r[1]?.v || '').match(new RegExp(`U${unitIdx}\\b`)));

  return {
    grade, unit: unitIdx,
    theme: unitRow ? String(unitRow[2]?.v || '') : '',
    keyLanguage: unitRow ? String(unitRow[3]?.v || '') : '',
    grammar: unitRow ? String(unitRow[4]?.v || '') : '',
    vocab: unitRow ? String(unitRow[5]?.v || '') : '',
    writingOutput: unitRow ? String(unitRow[6]?.v || '') : '',

    gradeGrammarFull: gramRow[2] || '',
    gradeGrammarExamples: gramRow[3] || '',
    gradeExamLink: gramRow[4] || '',

    gradeVocabSize: vocabRow[4] || '',
    gradeWordlist: vocabRow[3] || '',

    phonics: getSubBlock('Phonics'),
    vocabulary: getSubBlock('Vocabulary'),
    listening: getSubBlock('Listening'),
    speaking: getSubBlock('Speaking'),
    textualComp: getSubBlock('Textual'),
    readingSkills: getSubBlock('Reading Skills'),
    readingPlan: getSubBlock('Reading Plan'),
    textTypes: getSubBlock('Text Types'),
    ideaDev: getSubBlock('Idea'),
    langConv: getSubBlock('Language Conventions'),
    writingReflect: getSubBlock('Writing Reflection'),
    gradProfile: getSubBlock('Graduate Profile Competencies'),
    gradAttrs: getSubBlock('Graduate Profile Attributes'),
    formAssess: getSubBlock('Formative Assessment'),
    summAssess: getSubBlock('Summative Assessment'),

    clilTheme: clilRow ? String(clilRow[1]?.v || '') : '',
    clilSubjects: clilRow ? String(clilRow[2]?.v || '') : '',
    clilProject: clilRow ? String(clilRow[3]?.v || '') : '',
    clilOutput: clilRow ? String(clilRow[4]?.v || '') : '',
    clilAssessment: clilRow ? String(clilRow[5]?.v || '') : '',
  };
}

// Specific 6-week plan if defined in CLIL_PLANS, else generic template
function buildSixWeekSchedule(data) {
  const key = `${data.grade}_U${data.unit}`;
  const specific = CLIL_PLANS[key];
  if (specific && specific.weeks) {
    return specific.weeks.map((w, i) => ({
      wk: i + 1,
      title: w.t || `Week ${i+1}`,
      focus: w.f || '',
      activities: w.a || [],
      partnerSubject: w.p || '—',
      output: w.o || '—',
    }));
  }
  // Fallback generic template
  return [
    { wk: 1, title: 'Introduction & Vocabulary Pre-teaching',
      focus: 'Build vocabulary foundation + activate prior knowledge',
      activities: [
        `Warm-up: activate schema for "${data.theme}"`,
        `Vocabulary pre-teach: ${data.vocabulary ? data.vocabulary.split('\n')[0].slice(0,80) : 'key terms from the unit'}`,
        'TPR / visuals / realia to support comprehension',
        `Phonics / pronunciation focus: ${data.phonics ? data.phonics.slice(0,60) : 'sounds relevant to new vocabulary'}`,
      ],
      partnerSubject: 'None yet (English only)',
      output: 'Vocab journal page + oral pair-share'
    },
    { wk: 2, title: 'Reading + Textual Comprehension',
      focus: 'Encounter target language in authentic context',
      activities: [
        `Shared reading: ${data.readingPlan || 'grade-appropriate texts'}`,
        `Reading skills: ${data.readingSkills ? data.readingSkills.slice(0,80) : 'main idea, details, inference'}`,
        'Guided reading groups (by level)',
        'Graphic organiser (story map / KWL)',
      ],
      partnerSubject: 'Comunicación (cross-language strategies)',
      output: 'Comprehension questions + retelling'
    },
    { wk: 3, title: 'Grammar Focus + Guided Practice',
      focus: 'Notice and practice target structures',
      activities: [
        `Grammar focus: ${data.grammar || data.langConv || 'structures for this level'}`,
        'I do / we do / you do (gradual release)',
        'Controlled practice (fill-in, transformation)',
        'Freer practice (pair dialogues)',
      ],
      partnerSubject: 'None (language-focused)',
      output: 'Grammar worksheet + speaking task'
    },
    { wk: 4, title: 'Listening + Speaking Development',
      focus: 'Oral production + comprehension',
      activities: [
        `Listening: ${data.listening ? data.listening.slice(0,80) : 'short texts at grade level'}`,
        `Speaking: ${data.speaking ? data.speaking.slice(0,80) : 'dialogues, role-plays, short talks'}`,
        'Pronunciation drills + intonation',
        'Video / podcast / authentic audio',
      ],
      partnerSubject: 'Drama / Music (performance, chants)',
      output: 'Oral presentation / role-play performance'
    },
    { wk: 5, title: `CLIL Integration: ${data.clilSubjects || 'Cross-curricular work'}`,
      focus: 'Apply English to content in another subject',
      activities: [
        `Integrated project: ${data.clilProject || data.theme}`,
        `Partner with: ${data.clilSubjects || 'other subject(s)'}`,
        'Research, data gathering (with teacher scaffolding)',
        'Draft the content product',
      ],
      partnerSubject: data.clilSubjects || 'TBD',
      output: data.clilOutput || 'Project draft'
    },
    { wk: 6, title: 'Writing, Presentation & Assessment',
      focus: 'Produce final output + formative/summative assessment',
      activities: [
        `Final writing: ${data.textTypes || data.writingOutput || 'short text for the unit'}`,
        `Writing reflection: ${data.writingReflect || 'purpose, audience, structure'}`,
        'Peer review + revision',
        'Final presentation / publication / gallery walk',
        `Summative assessment: ${data.summAssess ? data.summAssess.slice(0,100) : 'oral + written rubric'}`,
      ],
      partnerSubject: 'None — English-led assessment',
      output: data.writingOutput || 'Final written product + oral presentation'
    },
  ];
}

function deriveOutcomes(data) {
  const g = data.grade;
  const level = GRADE_LEVELS[g];
  return {
    listening: `By week 6, students can understand ${level.cefr}-level spoken texts about "${data.theme}".`,
    speaking: `By week 6, students can talk about "${data.theme}" using target grammar (${data.grammar ? data.grammar.split(';')[0] : 'grade-level structures'}).`,
    reading: `By week 6, students can read and comprehend texts about "${data.theme}" at ${level.cefr} level.`,
    writing: `By week 6, students produce: ${data.writingOutput || 'a short written piece'}.`,
    language: `By week 6, students accurately use: ${data.grammar || data.langConv || 'target grammar structures'}.`,
    clil: data.clilProject ? `By week 6, students complete the CLIL project "${data.clilProject}" integrating ${data.clilSubjects}.` : 'Cross-curricular integration through classroom-based activities.',
    graduateProfile: data.gradProfile ? `Develops: ${data.gradProfile.slice(0,100)}.` : 'Focus on communicative and socio-emotional competencies.',
  };
}

function UnitDetailModal({ grade, unitIdx, onClose, initialTab = 'overview' }) {
  const data = useMemo(() => getUnitFullData(grade, unitIdx), [grade, unitIdx]);
  const weeks = useMemo(() => buildSixWeekSchedule(data), [data]);
  const outcomes = useMemo(() => deriveOutcomes(data), [data]);
  const level = GRADE_LEVELS[grade];
  const [activeTab, setActiveTab] = useState(initialTab);

  const tabs = [
    { id:'overview', label:'📋 Overview' },
    { id:'clil', label:'🧩 CLIL' },
    { id:'language', label:'🗣 Language' },
    { id:'literacy', label:'📚 Reading/Writing' },
    { id:'weeks', label:'📅 6-Week Plan' },
    { id:'outcomes', label:'🎯 Outcomes' },
    { id:'assessment', label:'✓ Assessment' },
  ];
  const ib = (CLIL_PLANS[`${grade}_U${unitIdx}`] || {}).ib || null;

  return (
    <div className="fixed inset-0 bg-black/60 flex items-center justify-center z-50 p-4 animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-xl shadow-2xl max-w-5xl w-full max-h-[92vh] overflow-y-auto animate-slide-up" onClick={e=>e.stopPropagation()} style={{position:'relative'}}>
        <div style={{backgroundColor: level.color}} className="p-6 rounded-t-xl text-slate-800">
          <div className="flex items-start justify-between">
            <div>
              <div className="text-xs uppercase tracking-[0.2em] opacity-70 mb-1">{grade} · {level.cefr} · {level.exam}</div>
              <h2 className="text-2xl font-black">Unit {unitIdx} · {data.theme || 'Unit ' + unitIdx}</h2>
              <p className="text-sm opacity-80 mt-1">{data.keyLanguage}</p>
            </div>
            <button onClick={onClose} className="text-slate-600 hover:text-slate-900 text-3xl leading-none">×</button>
          </div>
        </div>

        <div className="bg-white dark:bg-slate-800 border-b-2 border-nordic-300 dark:border-slate-600 px-6 flex gap-1 overflow-x-auto no-scrollbar shadow-md"
             style={{position:'sticky', top:0, zIndex:40}}>
          {tabs.map(t => (
            <button key={t.id} onClick={()=>setActiveTab(t.id)}
              className={`px-4 py-3 text-xs whitespace-nowrap font-medium transition border-b-[3px] -mb-[2px] ${activeTab===t.id ? 'border-nordic-600 text-nordic-700 dark:text-nordic-200 bg-nordic-50 dark:bg-slate-700' : 'border-transparent text-slate-500 hover:text-slate-700 hover:bg-slate-50 dark:hover:text-slate-300 dark:hover:bg-slate-700/50'}`}>
              {t.label}
            </button>
          ))}
        </div>

        <div className="p-6 bg-slate-50 dark:bg-slate-900 min-h-[50vh]">
          {activeTab === 'overview' && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <InfoCard title="📝 Grammar focus" content={data.grammar || data.langConv || '—'}/>
              <InfoCard title="📚 Vocabulary" content={data.vocab || data.vocabulary || '—'}/>
              <InfoCard title="🔤 Phonics / Pronunciation" content={data.phonics || '—'}/>
              <InfoCard title="✏ Writing output" content={data.writingOutput || data.textTypes || '—'}/>
              <InfoCard title="🧩 CLIL project" content={data.clilProject ? `${data.clilProject}\n\n• Partner: ${data.clilSubjects}\n• Output: ${data.clilOutput}` : '—'}/>
              <InfoCard title="🌟 Graduate Profile" content={data.gradProfile || '—'} italic/>
            </div>
          )}
          {activeTab === 'clil' && (
            !ib ? <div className="text-slate-400 text-sm italic">No CLIL content available.</div> : (
              <div className="space-y-4">
                <div className="p-4 rounded-xl bg-gradient-to-br from-nordic-600 to-nordic-800 text-white">
                  <div className="text-[11px] uppercase tracking-[0.2em] opacity-75 mb-1">CLIL Unit · Age {ib.age_range}</div>
                  <div className="text-xl font-black">{data.theme || ('Unit ' + unitIdx)}</div>
                  <div className="text-sm opacity-90 mt-1">{data.clilProject || ''}</div>
                </div>
                {(ib.transdisciplinary_theme || ib.global_context) && (
                  <InfoCard title="🌍 Unit Theme / Context" content={ib.transdisciplinary_theme || ib.global_context}/>
                )}
                {(ib.central_idea || ib.statement_of_inquiry || ib.essential_understanding) && (
                  <InfoCard title="💡 Central Idea" content={ib.central_idea || ib.statement_of_inquiry || ib.essential_understanding} italic/>
                )}
                {ib.lines_of_inquiry && ib.lines_of_inquiry.length > 0 && (
                  <div className="bg-white dark:bg-slate-800 p-4 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                    <div className="text-xs uppercase tracking-wider text-slate-500 mb-2 font-medium">🔍 Lines of Inquiry</div>
                    <ol className="text-sm space-y-1 list-decimal list-inside">
                      {ib.lines_of_inquiry.map((l, i) => <li key={i}>{l}</li>)}
                    </ol>
                  </div>
                )}
                {ib.inquiry_questions && (
                  <div className="bg-white dark:bg-slate-800 p-4 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm space-y-3">
                    <div className="text-xs uppercase tracking-wider text-slate-500 font-medium">❓ Guiding Questions</div>
                    <div><div className="text-[11px] text-nordic-600 font-semibold mb-1">FACTUAL</div><div className="text-sm">{ib.inquiry_questions.factual}</div></div>
                    <div><div className="text-[11px] text-amber-600 font-semibold mb-1">CONCEPTUAL</div><div className="text-sm">{ib.inquiry_questions.conceptual}</div></div>
                    <div><div className="text-[11px] text-rose-600 font-semibold mb-1">DEBATABLE</div><div className="text-sm">{ib.inquiry_questions.debatable}</div></div>
                  </div>
                )}
                {ib.tok_links && (
                  <div className="bg-indigo-50 dark:bg-indigo-900/20 p-4 rounded-lg border-l-4 border-indigo-500">
                    <div className="text-xs uppercase tracking-wider text-indigo-700 dark:text-indigo-300 mb-2 font-medium">🧠 Critical Thinking Questions</div>
                    <ul className="text-sm space-y-1 list-disc list-inside">
                      {ib.tok_links.map((t, i) => <li key={i}>{t}</li>)}
                    </ul>
                  </div>
                )}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {(ib.key_concept || ib.key_concepts) && (
                    <div className="bg-amber-50 dark:bg-amber-900/20 p-4 rounded-lg border border-amber-200 dark:border-amber-700">
                      <div className="text-xs uppercase tracking-wider text-amber-700 dark:text-amber-300 mb-2 font-medium">🔑 Key Concept(s)</div>
                      <div className="text-sm font-semibold">{ib.key_concept || (ib.key_concepts || []).join(' · ')}</div>
                    </div>
                  )}
                  {ib.related_concepts && (
                    <div className="bg-emerald-50 dark:bg-emerald-900/20 p-4 rounded-lg border border-emerald-200 dark:border-emerald-700">
                      <div className="text-xs uppercase tracking-wider text-emerald-700 dark:text-emerald-300 mb-2 font-medium">🔗 Related Concepts</div>
                      <div className="text-sm">{ib.related_concepts.join(' · ')}</div>
                    </div>
                  )}
                </div>
                {ib.atl_skills && (
                  <div className="bg-white dark:bg-slate-800 p-4 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                    <div className="text-xs uppercase tracking-wider text-slate-500 mb-2 font-medium">🧰 Approaches to Learning</div>
                    <div className="flex flex-wrap gap-2">
                      {ib.atl_skills.map((s, i) => <span key={i} className="px-3 py-1 bg-nordic-100 dark:bg-slate-700 rounded-full text-xs">{s}</span>)}
                    </div>
                  </div>
                )}
                {ib.learner_profile && (
                  <div className="bg-white dark:bg-slate-800 p-4 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                    <div className="text-xs uppercase tracking-wider text-slate-500 mb-2 font-medium">🌟 Learner Attributes</div>
                    <div className="flex flex-wrap gap-2">
                      {ib.learner_profile.map((s, i) => <span key={i} className="px-3 py-1 bg-violet-100 dark:bg-violet-900/30 text-violet-800 dark:text-violet-200 rounded-full text-xs font-medium">{s}</span>)}
                    </div>
                  </div>
                )}
                {ib.assessment_criteria && (
                  <div className="bg-white dark:bg-slate-800 p-4 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
                    <div className="text-xs uppercase tracking-wider text-slate-500 mb-3 font-medium">📊 Assessment Criteria</div>
                    <div className="space-y-2">
                      {Object.entries(ib.assessment_criteria).map(([k, v]) => (
                        <div key={k} className="flex gap-3">
                          <span className="flex-shrink-0 w-8 h-8 rounded-full bg-nordic-600 text-white flex items-center justify-center text-sm font-bold">{k}</span>
                          <span className="text-sm pt-1">{v}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
                {ib.success_criteria && (
                  <div className="bg-emerald-50 dark:bg-emerald-900/20 p-4 rounded-lg border-l-4 border-emerald-500">
                    <div className="text-xs uppercase tracking-wider text-emerald-700 dark:text-emerald-300 mb-2 font-medium">✅ Success Criteria — I can…</div>
                    <ul className="text-sm space-y-1.5">
                      {ib.success_criteria.map((s, i) => <li key={i} className="flex gap-2"><span className="text-emerald-600">✓</span><span>{s}</span></li>)}
                    </ul>
                  </div>
                )}
                {ib.cambridge_link && (
                  <div className="bg-rose-50 dark:bg-rose-900/20 p-4 rounded-lg border-l-4 border-rose-500">
                    <div className="text-xs uppercase tracking-wider text-rose-700 dark:text-rose-300 mb-1 font-medium">🎯 Cambridge Exam Link</div>
                    <div className="text-sm">{ib.cambridge_link}</div>
                  </div>
                )}
              </div>
            )
          )}
          {activeTab === 'language' && (
            <div className="space-y-4">
              <InfoCard title="🗣 Language functions" content={data.keyLanguage || '—'}/>
              <InfoCard title="📝 Grammar — full progression for the grade" content={data.gradeGrammarFull || data.grammar || '—'}/>
              <InfoCard title="💬 Grammar examples" content={data.gradeGrammarExamples || '—'}/>
              <InfoCard title="🎯 Cambridge exam link" content={data.gradeExamLink || '—'}/>
              <InfoCard title="📚 Vocabulary this unit" content={data.vocabulary || data.vocab || '—'}/>
              <InfoCard title="📖 Vocabulary wordlist + size" content={`${data.gradeWordlist || ''}\n\nTarget size: ${data.gradeVocabSize || 'n/a'}`}/>
            </div>
          )}
          {activeTab === 'literacy' && (
            <div className="space-y-4">
              <InfoCard title="🎧 Listening" content={data.listening || '—'}/>
              <InfoCard title="🗣 Speaking" content={data.speaking || '—'}/>
              <InfoCard title="📖 Reading skills" content={data.readingSkills || '—'}/>
              <InfoCard title="📕 Reading plan for this unit" content={data.readingPlan || '—'}/>
              <InfoCard title="🔍 Textual comprehension" content={data.textualComp || '—'}/>
              <InfoCard title="✏ Text types" content={data.textTypes || '—'}/>
              <InfoCard title="💡 Idea development & process" content={data.ideaDev || '—'}/>
              <InfoCard title="🪞 Writing reflection" content={data.writingReflect || '—'}/>
            </div>
          )}
          {activeTab === 'weeks' && (
            <div className="space-y-3">
              {weeks.map(w => (
                <div key={w.wk} className="bg-white dark:bg-slate-800 rounded-lg border-l-4 border-nordic-500 shadow-sm p-4">
                  <div className="flex items-baseline gap-3 mb-2">
                    <span className="bg-nordic-600 text-white text-xs font-bold px-2 py-1 rounded">Week {w.wk}</span>
                    <h4 className="font-semibold text-slate-800 dark:text-slate-100">{w.title}</h4>
                  </div>
                  <p className="text-xs text-slate-500 italic mb-2">Focus: {w.focus}</p>
                  <ul className="text-sm text-slate-700 dark:text-slate-200 space-y-1 ml-2">
                    {w.activities.map((a, i) => <li key={i} className="flex gap-2"><span className="text-nordic-500">▸</span><span>{a}</span></li>)}
                  </ul>
                  <div className="grid grid-cols-2 gap-2 mt-3 pt-3 border-t border-slate-100 dark:border-slate-700 text-xs">
                    <div><span className="text-slate-500 uppercase tracking-wider">Partner subject:</span> <span className="font-medium">{w.partnerSubject}</span></div>
                    <div><span className="text-slate-500 uppercase tracking-wider">Output:</span> <span className="font-medium">{w.output}</span></div>
                  </div>
                </div>
              ))}
            </div>
          )}
          {activeTab === 'outcomes' && (
            <div className="space-y-3">
              {Object.entries(outcomes).map(([k, v]) => (
                <div key={k} className="p-4 bg-emerald-50 dark:bg-emerald-900/20 rounded-lg border-l-4 border-emerald-500">
                  <div className="text-xs uppercase tracking-wider text-emerald-700 dark:text-emerald-300 mb-1">{k}</div>
                  <div className="text-sm text-slate-800 dark:text-slate-100">{v}</div>
                </div>
              ))}
            </div>
          )}
          {activeTab === 'assessment' && (
            <div className="space-y-4">
              <InfoCard title="📋 Formative Assessment (ongoing)" content={data.formAssess || '—'}/>
              <InfoCard title="🎓 Summative Assessment (end of unit)" content={data.summAssess || '—'}/>
              <InfoCard title="🌟 Graduate Profile competencies" content={data.gradProfile || '—'}/>
              <InfoCard title="⭐ Graduate Profile attributes" content={data.gradAttrs || '—'}/>
              <div className="p-4 bg-amber-50 dark:bg-amber-900/20 rounded-lg border-l-4 border-amber-500">
                <div className="text-xs uppercase tracking-wider text-amber-700 dark:text-amber-300 mb-1">MINEDU Scale</div>
                <div className="text-sm text-slate-800 dark:text-slate-100">AD (Outstanding) · A (Expected) · B (In Progress) · C (Beginning) — see tab 14_Assessment_Scale for full descriptors per skill.</div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function InfoCard({ title, content, italic }) {
  return (
    <div className="bg-white dark:bg-slate-800 p-4 rounded-lg border border-slate-200 dark:border-slate-700 shadow-sm">
      <div className="text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2 font-medium">{title}</div>
      <div className={`text-sm text-slate-700 dark:text-slate-200 whitespace-pre-wrap leading-relaxed ${italic ? 'italic' : ''}`}>{content}</div>
    </div>
  );
}

// ============= ACTIVITY LOG =============
function ActivityLogView({ onRollback }) {
  const [activity, setActivity] = useState(loadActivity());
  const clearAll = () => { if (confirm('Clear all activity log entries?')) { saveActivity([]); setActivity([]); } };
  return (
    <div className="p-6 overflow-auto h-full animate-fade-in bg-slate-50 dark:bg-slate-900">
      <div className="max-w-5xl mx-auto">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h1 className="text-2xl font-bold">Activity Log</h1>
            <p className="text-sm text-slate-500 dark:text-slate-400">All admin edits · {activity.length} entries</p>
          </div>
          <button onClick={clearAll} className="text-xs text-red-600 hover:underline">Clear all</button>
        </div>
        {activity.length === 0 ? (
          <div className="text-center py-12 text-slate-400">No activity yet. Edits made in edit mode will appear here.</div>
        ) : (
          <div className="bg-white dark:bg-slate-800 rounded-xl shadow-sm border border-slate-200 dark:border-slate-700 divide-y divide-slate-100 dark:divide-slate-700">
            {activity.map((a, i) => (
              <div key={i} className="p-4 hover:bg-slate-50 dark:hover:bg-slate-700/30">
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center gap-2 text-xs text-slate-500 mb-1">
                      <span>{fmtDate(a.ts)}</span>
                      <span>·</span>
                      <span className="font-medium text-nordic-600">{a.user}</span>
                      <span>·</span>
                      <span>{a.tabId}</span>
                    </div>
                    <div className="grid grid-cols-2 gap-3 text-xs mt-2">
                      <div>
                        <div className="text-slate-400 uppercase tracking-wider mb-1">Before</div>
                        <div className="p-2 bg-red-50 dark:bg-red-900/30 rounded max-h-24 overflow-auto whitespace-pre-wrap">{a.before || '(empty)'}</div>
                      </div>
                      <div>
                        <div className="text-slate-400 uppercase tracking-wider mb-1">After</div>
                        <div className="p-2 bg-emerald-50 dark:bg-emerald-900/30 rounded max-h-24 overflow-auto whitespace-pre-wrap">{a.after}</div>
                      </div>
                    </div>
                  </div>
                  <button onClick={()=>onRollback(a)} className="text-xs text-amber-600 hover:underline flex-shrink-0">Rollback</button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

// ============= COMMENTS PANEL (inside cell drawer) =============
function CommentsPanel({ cellKey, currentUser, comments, onSave }) {
  const [text, setText] = useState('');
  const threadComments = comments[cellKey] || [];
  const submit = () => {
    if (!text.trim()) return;
    const c = { ...comments, [cellKey]: [...threadComments, { ts: Date.now(), user: currentUser.name, role: currentUser.role, text }] };
    onSave(c);
    setText('');
  };
  return (
    <div className="border-t border-slate-200 dark:border-slate-700 pt-4 mt-4">
      <h4 className="text-xs uppercase tracking-wider text-slate-500 mb-3">💬 Comments ({threadComments.length})</h4>
      <div className="space-y-2 mb-3 max-h-48 overflow-auto">
        {threadComments.map((c, i) => (
          <div key={i} className="p-2 bg-slate-50 dark:bg-slate-900 rounded text-xs">
            <div className="flex items-center gap-2 mb-1">
              <span className="font-medium text-nordic-600">{c.user}</span>
              <span className={`px-1.5 py-0.5 rounded text-[9px] ${c.role === 'admin' ? 'bg-amber-100 text-amber-800' : 'bg-slate-200 text-slate-700'}`}>{c.role}</span>
              <span className="text-slate-400">{fmtDate(c.ts)}</span>
            </div>
            <div className="whitespace-pre-wrap">{c.text}</div>
          </div>
        ))}
        {threadComments.length === 0 && <div className="text-xs text-slate-400 italic">No comments yet.</div>}
      </div>
      <div className="flex gap-2">
        <input value={text} onChange={e=>setText(e.target.value)} onKeyDown={e=>e.key==='Enter' && submit()}
          placeholder="Add comment..." className="flex-1 px-3 py-1.5 text-xs rounded border border-slate-200 dark:border-slate-600 dark:bg-slate-700 outline-none focus:ring-2 focus:ring-nordic-400"/>
        <button onClick={submit} className="px-3 py-1.5 text-xs bg-nordic-700 hover:bg-nordic-600 text-white rounded">Post</button>
      </div>
    </div>
  );
}

// ============= EXPORT MENU =============
function exportSheetPDF(tabId, sheet) {
  if (!sheet) return;
  // Open a clean print window with polished layout
  const w = window.open('', '_blank', 'width=1000,height=700');
  const title = tabId.replace(/_/g, ' ');
  const rowsHtml = sheet.rows.map((row, ri) => {
    const cells = row.map((c) => {
      const v = String(c.v || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
      const bg = c.f || '';
      const bold = c.b ? 'font-weight:700;' : '';
      const valLen = (c.v || '').length;
      const isShort = valLen > 0 && valLen <= 30 && !(c.v || '').includes('\n');
      const align = isShort ? 'text-align:center;' : 'text-align:left;';
      const size = isShort ? 'font-size:10pt;' : 'font-size:8.5pt;';
      const color = bg ? 'color:#1a202c;' : '';
      return `<td style="padding:6px 8px;border:1px solid #ddd;vertical-align:top;white-space:pre-wrap;${size}${align}${bold}background-color:${bg};${color}">${v}</td>`;
    }).join('');
    return `<tr>${cells}</tr>`;
  }).join('');
  const html = `<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>${title} · NIS English 2026</title>
<style>
@page { size: A4 landscape; margin: 1.5cm; }
body { font-family: -apple-system, 'Segoe UI', sans-serif; color: #1a202c; margin: 0; padding: 20px; }
.pdf-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #1F4E79; padding-bottom: 12px; margin-bottom: 16px; }
.pdf-title { font-size: 18pt; font-weight: 700; color: #1F4E79; }
.pdf-subtitle { font-size: 9pt; color: #666; letter-spacing: 2px; text-transform: uppercase; }
.pdf-meta { font-size: 8pt; color: #888; }
table { width: 100%; border-collapse: collapse; page-break-inside: auto; }
tr { page-break-inside: avoid; }
thead { display: table-header-group; }
.pdf-footer { margin-top: 20px; border-top: 1px solid #ddd; padding-top: 8px; font-size: 7.5pt; color: #888; display: flex; justify-content: space-between; }
@media print { .no-print { display: none !important; } }
.btn { background: #1F4E79; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; font-size: 11pt; margin-right: 6px; }
</style></head>
<body>
<div class="no-print" style="text-align:center; padding:20px; background:#F0F4FA; margin-bottom:20px; border-radius:8px;">
  <div style="font-size:14pt; font-weight:bold; color:#1F4E79; margin-bottom:10px;">Ready to print or save as PDF</div>
  <button class="btn" onclick="window.print()">🖨 Print / Save as PDF</button>
  <button class="btn" onclick="window.close()" style="background:#888;">Close</button>
</div>
<div class="pdf-header">
  <div>
    <div class="pdf-title">${title}</div>
    <div class="pdf-subtitle">NIS English Master · Immersion Program 2026</div>
  </div>
  <div class="pdf-meta">Exported: ${new Date().toLocaleDateString()} · Page <span class="page-num"></span></div>
</div>
<table>${rowsHtml}</table>
<div class="pdf-footer">
  <span>Nordic International School · English Department · Master Scope & Sequence 2026</span>
  <span>Exported from ${tabId}</span>
</div>
</body></html>`;
  w.document.write(html);
  w.document.close();
  setTimeout(()=> { try { w.focus(); } catch(e){} }, 300);
}

function ExportButton({ tabId, sheet }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="relative">
      <button onClick={()=>setOpen(!open)} className="px-3 py-1.5 text-xs bg-slate-100 dark:bg-slate-700 hover:bg-slate-200 dark:hover:bg-slate-600 rounded flex items-center gap-1">
        <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2"><path strokeLinecap="round" d="M4 16v4a2 2 0 002 2h12a2 2 0 002-2v-4M7 10l5-5 5 5M12 5v12"/></svg>
        Export ▾
      </button>
      {open && (
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
      )}
    </div>
  );
}

// ============= SHORTCUTS HELP =============
function ShortcutsHelp({ open, onClose }) {
  if (!open) return null;
  const list = [
    ['Ctrl/⌘ + K', 'Open command palette'],
    ['?', 'Show this help'],
    ['Esc', 'Close modal or drawer'],
    ['Ctrl/⌘ + S', 'Save cell edit (while editing)'],
    ['↑ ↓', 'Navigate in command palette'],
    ['Enter', 'Select option'],
    ['Click star ☆', 'Add tab to favorites'],
  ];
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4 animate-fade-in" onClick={onClose}>
      <div className="bg-white dark:bg-slate-800 rounded-xl shadow-2xl max-w-md w-full p-6 animate-slide-up" onClick={e=>e.stopPropagation()}>
        <h3 className="text-lg font-semibold text-nordic-700 dark:text-nordic-200 mb-4">Keyboard Shortcuts</h3>
        <div className="space-y-2">{list.map(([k,d]) => (
          <div key={k} className="flex items-center justify-between py-2 border-b border-slate-100 dark:border-slate-700">
            <span className="text-sm text-slate-700 dark:text-slate-200">{d}</span>
            <span className="kbd">{k}</span>
          </div>
        ))}</div>
      </div>
    </div>
  );
}

// ============= APP =============
function App() {
  const [user, setUser] = useState(() => {
    try { const a = JSON.parse(localStorage.getItem(LS.auth) || 'null'); if (!a) return null; return loadUsers().find(u => u.id === a.id) || null; } catch(e) { return null; }
  });
  const [theme, setTheme] = useState(localStorage.getItem(LS.theme) || 'light');
  const [currentTab, setCurrentTab] = useState('_dashboard');
  const [editMode, setEditMode] = useState(false);
  const [editingCell, setEditingCell] = useState(null);
  const [showUserMgmt, setShowUserMgmt] = useState(false);
  const [showPalette, setShowPalette] = useState(false);
  const [showShortcuts, setShowShortcuts] = useState(false);
  const [overrides, setOverrides] = useState(loadOverrides());
  const [favorites, setFavorites] = useState(loadFavs());
  const [cellDetail, setCellDetail] = useState(null);
  const [clilDetail, setClilDetail] = useState(null);
  const [comments, setComments] = useState(loadComments());
  const [progress, setProgress] = useState(loadProgress());
  const [showResets, setShowResets] = useState(false);
  const [resetCount, setResetCount] = useState(() => loadResets().filter(r => r.status === 'pending').length);
  const [unitDetail, setUnitDetail] = useState(null);  // { grade, unit, tab }

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    document.body.classList.toggle('dark', theme === 'dark');
    localStorage.setItem(LS.theme, theme);
  }, [theme]);

  useEffect(() => {
    document.body.classList.toggle('teacher-mode', user?.role === 'teacher');
  }, [user]);

  useEffect(() => {
    const handler = (e) => {
      const ctrl = e.ctrlKey || e.metaKey;
      if (ctrl && e.key === 'k') { e.preventDefault(); setShowPalette(true); }
      else if (e.key === 'Escape') { setShowPalette(false); setCellDetail(null); setClilDetail(null); setShowShortcuts(false); }
      else if (e.key === '?' && !e.target.matches('input, textarea')) { setShowShortcuts(true); }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, []);

  // Session expiry check
  useEffect(() => {
    if (!user) return;
    try {
      const auth = JSON.parse(localStorage.getItem(LS.auth) || 'null');
      if (auth && auth.expires && Date.now() > auth.expires) {
        localStorage.removeItem(LS.auth); setUser(null);
        pushToast({type:'warn', message:'Session expired. Please sign in again.'});
      }
    } catch(e) {}
  }, [user, currentTab]);

  if (!user) return (<><LoginPage onLogin={setUser}/><ToastContainer/></>);

  const logout = () => { localStorage.removeItem(LS.auth); setUser(null); };
  const saveEdit = (val) => {
    const k = `${editingCell.tabId}::${editingCell.ri}::${editingCell.ci}`;
    const before = overrides[k] !== undefined ? overrides[k] : editingCell.value;
    const n = {...overrides, [k]:val};
    setOverrides(n); saveOverrides(n);
    logActivity({ ts: Date.now(), user: user.name, tabId: editingCell.tabId, ri: editingCell.ri, ci: editingCell.ci, before, after: val });
    setEditingCell(null);
    pushToast({type:'success', message:'Cell saved'});
  };
  const rollbackActivity = (entry) => {
    const k = `${entry.tabId}::${entry.ri}::${entry.ci}`;
    const n = {...overrides}; if (entry.before) n[k] = entry.before; else delete n[k];
    setOverrides(n); saveOverrides(n);
    logActivity({ ts: Date.now(), user: user.name + ' (rollback)', tabId: entry.tabId, ri: entry.ri, ci: entry.ci, before: entry.after, after: entry.before });
    alert('Rolled back.');
  };
  const toggleFav = (t) => { const n = favorites.includes(t) ? favorites.filter(x=>x!==t) : [...favorites, t]; setFavorites(n); saveFavs(n); };
  const saveCommentsAll = (c) => { setComments(c); saveComments(c); };
  const toggleProgress = (grade, unit, status) => {
    const k = `${grade}::U${unit}`;
    const n = {...progress, [k]:{ status, by: user.name, ts: Date.now() }};
    setProgress(n); saveProgress(n);
  };

  const renderMain = () => {
    if (currentTab === '_dashboard') return <Dashboard user={user} onNavigate={setCurrentTab} progress={progress}/>;
    if (currentTab === '_activity') return <ActivityLogView onRollback={rollbackActivity}/>;
    if (currentTab.startsWith('_grade_')) return <GradeDeepDive grade={currentTab.replace('_grade_','')} onNavigate={setCurrentTab} progress={progress} onToggleProgress={toggleProgress} onOpenUnit={(g, u)=>setUnitDetail({grade:g, unit:u, tab:'overview'})} onOpenCLIL={(g, u)=>setUnitDetail({grade:g, unit:u, tab:'clil'})}/>;
    if (currentTab === '13_Cambridge_Calendar') return <VisualCalendar />;
    if (currentTab === '12_CLIL_Map') return <VisualCLIL onCellClick={(cell, grade, unit) => setClilDetail({ cell, grade, unit })} onDirectUnit={(g, u)=>setUnitDetail({grade:g, unit:u})}/>;
    return <StandardTabContent tabId={currentTab} canEdit={editMode && user.role==='admin'}
      overrides={overrides}
      onEditCell={(ri, ci, v) => setEditingCell({ tabId: currentTab, ri, ci, value: v })}
      onCellDetail={(v, tabId, ri, ci) => setCellDetail({ value: v, tabId, ri, ci })}
      favorites={favorites} onToggleFav={toggleFav} comments={comments}/>;
  };

  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar user={user} currentTab={currentTab} onTabChange={setCurrentTab} onLogout={logout}
        theme={theme} onThemeToggle={()=>setTheme(theme==='dark'?'light':'dark')}
        onOpenUserMgmt={()=>setShowUserMgmt(true)}
        onOpenResets={()=>setShowResets(true)}
        pendingResets={resetCount}
        editMode={editMode} onToggleEdit={()=>setEditMode(!editMode)}
        allowedTabs={user.tabs} favorites={favorites}
        onOpenPalette={()=>setShowPalette(true)}/>
      <main className="flex-1 overflow-hidden flex flex-col">
        <Breadcrumb tabId={currentTab} user={user}/>
        {renderMain()}
      </main>
      <CommandPalette open={showPalette} onClose={()=>setShowPalette(false)} onNavigate={setCurrentTab}/>
      {editingCell && <EditModal cell={editingCell} onClose={()=>setEditingCell(null)} onSave={saveEdit}/>}
      {showUserMgmt && <UserManagement onClose={()=>setShowUserMgmt(false)}/>}
      {cellDetail && <CellDrawer data={cellDetail} onClose={()=>setCellDetail(null)} currentUser={user} comments={comments} onSaveComments={saveCommentsAll}/>}
      {clilDetail && <CLILDetail data={clilDetail} onClose={()=>setClilDetail(null)} onOpenFullUnit={(g, u, tab)=>setUnitDetail({grade:g, unit:u, tab:tab||'overview'})}/>}
      {unitDetail && <UnitDetailModal grade={unitDetail.grade} unitIdx={unitDetail.unit} initialTab={unitDetail.tab || 'overview'} onClose={()=>setUnitDetail(null)}/>}
      <ShortcutsHelp open={showShortcuts} onClose={()=>setShowShortcuts(false)}/>
      {showResets && <ResetRequestsPanel onClose={()=>setShowResets(false)} onResolved={()=>setResetCount(loadResets().filter(r=>r.status==='pending').length)}/>}
      <ToastContainer/>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
</script>
</body>
</html>'''

OUTPUT = r'C:\Users\Paolo\OneDrive\09_Instituciones\NNORDIC\NIS_English_Master_App.html'
html = HTML.replace('__DATA__', master_data).replace('__PLANS__', clil_plans)
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)
import os
print(f'OK: {OUTPUT} ({os.path.getsize(OUTPUT)//1024} KB)')
