# -*- coding: utf-8 -*-
"""
Build standalone single-file HTML app for the Systems Engineers English Course.
Design system inspired by COHASSET-platform-standalone.html.
"""
import json
from pathlib import Path

DATA = json.loads(Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\course_data.json")
                  .read_text(encoding="utf-8"))

OUT = Path(r"E:\CLAUDE\PAOLO BACA MANRIQUE\course-app\index.html")

# ---- Colores por nivel
LVL_COLORS = {
    "A1": "#10B981", "A2": "#14B8A6",
    "B1": "#2563EB", "B2": "#7C3AED",
    "C1": "#D97706", "C2": "#DC2626",
}
LVL_ICON = {"A1":"seedling","A2":"tree","B1":"route","B2":"mountain","C1":"crown","C2":"rocket"}

HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Systems Engineers English Course \u2013 A1 \u2192 C2</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
 --p:#2563EB;--pd:#1E40AF;--pl:#93C5FD;--pvl:#EFF6FF;--a:#3B82F6;
 --d:#1E293B;--m:#475569;--l:#94A3B8;--w:#FFF;--bg:#F8FAFC;
 --ok:#10B981;--okl:#D1FAE5;--er:#EF4444;--erl:#FEE2E2;--wa:#F59E0B;--wal:#FEF3C7;
 --b:#E2E8F0;--sh:0 4px 20px rgba(0,0,0,.06);--t:all .25s ease;
 --cyber:#0B3C5D;--cyber2:#328CC1;
}
html{scroll-behavior:smooth}
body{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--d);line-height:1.55;font-size:15px}
code,.mono{font-family:'JetBrains Mono',Consolas,monospace}

/* ===== HEADER ===== */
.hd{background:linear-gradient(135deg,#0F172A,#1E293B);color:#fff;padding:12px 24px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(0,0,0,.25)}
.logo{display:flex;align-items:center;gap:14px;cursor:pointer}
.logo-box{width:46px;height:46px;background:linear-gradient(135deg,#2563EB,#3B82F6);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;color:#fff;box-shadow:0 4px 12px rgba(37,99,235,.4)}
.logo-tx .t1{font-size:1.05rem;font-weight:700;letter-spacing:-.3px;line-height:1.1}
.logo-tx .t2{font-size:.72rem;color:#93C5FD;text-transform:uppercase;letter-spacing:1.2px;margin-top:2px;font-weight:500}
.hdr-r{display:flex;align-items:center;gap:14px}
.pmini{display:flex;flex-direction:column;gap:4px}
.pmini-bar{width:140px;height:6px;background:rgba(255,255,255,.15);border-radius:6px;overflow:hidden}
.pmini-fill{height:100%;background:linear-gradient(90deg,#60A5FA,#3B82F6);border-radius:6px;transition:width .5s}
.pmini-tx{font-size:.72rem;color:rgba(255,255,255,.7)}
.pmini-tx b{color:#fff}
.hd-btn{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);color:#fff;padding:8px 14px;border-radius:8px;font-family:inherit;font-weight:600;font-size:.82rem;cursor:pointer;display:flex;gap:6px;align-items:center;transition:var(--t)}
.hd-btn:hover{background:rgba(255,255,255,.18)}
.hd-btn.pr{background:linear-gradient(135deg,#DC2626,#991B1B);border:none}
.hd-btn.pr:hover{background:linear-gradient(135deg,#991B1B,#7F1D1D)}

/* ===== PROGRAM BAR ===== */
.pbar{background:#0F172A;padding:0 24px;display:flex;overflow-x:auto;gap:0;scrollbar-width:none}
.pbar::-webkit-scrollbar{display:none}
.ptab{padding:13px 20px;color:#94A3B8;font-size:.82rem;font-weight:600;cursor:pointer;border-bottom:3px solid transparent;white-space:nowrap;transition:var(--t);display:flex;align-items:center;gap:7px}
.ptab:hover{color:#fff;background:rgba(255,255,255,.04)}
.ptab.act{color:#fff;border-bottom-color:var(--a);background:rgba(59,130,246,.1)}
.ptab .lvl-dot{width:9px;height:9px;border-radius:50%;display:inline-block}

/* ===== LAYOUT ===== */
.lay{display:grid;grid-template-columns:280px 1fr;min-height:calc(100vh - 108px)}
.sb{background:var(--w);border-right:1px solid var(--b);padding:16px 0;overflow-y:auto;max-height:calc(100vh - 108px);position:sticky;top:108px}
.sb-section{padding:0 16px;margin-bottom:6px;font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:1.2px;color:var(--l)}
.sb-lvl-info{margin:0 12px 12px;padding:12px;background:var(--pvl);border-radius:10px;border-left:4px solid var(--p)}
.sb-lvl-code{font-size:1.4rem;font-weight:800;color:var(--p);line-height:1}
.sb-lvl-desc{font-size:.72rem;color:var(--m);margin-top:4px}
.sb-lvl-prog{margin-top:10px;font-size:.72rem;color:var(--m)}
.sb-lvl-prog b{color:var(--p)}

.lsn-item{display:flex;align-items:center;gap:10px;padding:9px 16px;cursor:pointer;transition:var(--t);border-left:3px solid transparent;font-size:.83rem}
.lsn-item:hover{background:var(--pvl)}
.lsn-item.act{background:var(--pvl);border-left-color:var(--p)}
.lsn-item.done .lsn-n{background:var(--ok);color:#fff}
.lsn-n{width:28px;height:28px;border-radius:7px;background:var(--bg);display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:700;color:var(--m);flex-shrink:0;border:1px solid var(--b)}
.lsn-item.act .lsn-n{background:var(--p);color:#fff;border-color:var(--p)}
.lsn-body{flex:1;min-width:0}
.lsn-ttl{font-size:.82rem;font-weight:600;color:var(--d);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lsn-sub{font-size:.68rem;color:var(--l);margin-top:1px}
.lsn-mark{color:var(--ok);font-size:.75rem}

/* ===== MAIN ===== */
.mn{padding:28px 36px;max-width:1100px}
.crumb{font-size:.78rem;color:var(--l);margin-bottom:10px;display:flex;align-items:center;gap:6px}
.crumb a{color:var(--p);text-decoration:none;font-weight:500}
.crumb a:hover{text-decoration:underline}

/* welcome */
.wel{text-align:center;padding:10px 0 30px}
.wel h1{font-size:2rem;margin-bottom:6px;color:var(--d);letter-spacing:-.5px}
.wel h1 span{background:linear-gradient(90deg,var(--p),#3B82F6);-webkit-background-clip:text;background-clip:text;color:transparent}
.wel p.lead{color:var(--m);font-size:1.02rem;max-width:700px;margin:0 auto 24px}
.wel-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:800px;margin:0 auto 30px}
.wel-stat{background:var(--w);padding:18px;border-radius:12px;border:1px solid var(--b);text-align:center}
.wel-stat-v{font-size:1.8rem;font-weight:800;color:var(--p);letter-spacing:-.5px}
.wel-stat-l{font-size:.75rem;color:var(--m);text-transform:uppercase;letter-spacing:.8px;margin-top:2px}

/* level cards on home */
.lvl-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:28px}
.lvl-card{padding:20px;border-radius:14px;cursor:pointer;transition:var(--t);background:var(--w);border:1px solid var(--b);display:flex;flex-direction:column;position:relative;overflow:hidden}
.lvl-card:hover{transform:translateY(-3px);box-shadow:0 10px 28px rgba(0,0,0,.1)}
.lvl-card .lvl-head{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.lvl-card .lvl-badge{width:42px;height:42px;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:1.1rem}
.lvl-card .lvl-title{font-size:1.25rem;font-weight:800;color:var(--d);letter-spacing:-.3px}
.lvl-card .lvl-sub{font-size:.78rem;color:var(--m);margin-top:1px}
.lvl-card .lvl-chips{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.lvl-card .chip{font-size:.68rem;background:var(--pvl);color:var(--p);padding:3px 9px;border-radius:10px;font-weight:600}
.lvl-card .chip.g{background:#DCFCE7;color:#166534}
.lvl-card .chip.o{background:#FFEDD5;color:#9A3412}
.lvl-card .lvl-desc{font-size:.82rem;color:var(--m);flex:1;margin-bottom:10px}
.lvl-card .lvl-prog{display:flex;align-items:center;gap:8px}
.lvl-card .lvl-prog-bar{flex:1;height:5px;background:var(--bg);border-radius:3px;overflow:hidden}
.lvl-card .lvl-prog-fill{height:100%;border-radius:3px;transition:width .5s}
.lvl-card .lvl-prog-tx{font-size:.72rem;color:var(--m);font-weight:600}
.lvl-card .lvl-topline{position:absolute;top:0;left:0;right:0;height:4px}

/* equiv table */
.section{margin-bottom:32px}
.section h2{font-size:1.2rem;font-weight:700;color:var(--d);margin-bottom:4px;letter-spacing:-.2px}
.section .s-sub{font-size:.85rem;color:var(--m);margin-bottom:14px}
.tbl{width:100%;border-collapse:collapse;background:var(--w);border-radius:12px;overflow:hidden;box-shadow:var(--sh);font-size:.85rem}
.tbl th,.tbl td{padding:10px 14px;text-align:left;border-bottom:1px solid var(--b)}
.tbl th{background:#0F172A;color:#fff;font-weight:600;font-size:.78rem;text-transform:uppercase;letter-spacing:.8px}
.tbl tr:last-child td{border-bottom:none}
.tbl tr:hover td{background:var(--bg)}
.tbl .lvl-pill{display:inline-block;padding:3px 10px;border-radius:6px;color:#fff;font-weight:700;font-size:.75rem}

/* lesson list view */
.lesson-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px;margin-top:14px}
.lesson-card{background:var(--w);border:1px solid var(--b);border-radius:12px;padding:16px;cursor:pointer;transition:var(--t);position:relative;overflow:hidden}
.lesson-card:hover{transform:translateY(-2px);box-shadow:0 8px 22px rgba(0,0,0,.08);border-color:var(--pl)}
.lesson-card.done{border-color:var(--ok)}
.lesson-card.done::after{content:"\f00c";font-family:"Font Awesome 6 Free";font-weight:900;position:absolute;top:12px;right:12px;color:var(--ok);font-size:1rem}
.lesson-card .lc-n{font-size:.72rem;color:var(--p);font-weight:700;letter-spacing:.8px;text-transform:uppercase}
.lesson-card .lc-t{font-size:1rem;font-weight:700;color:var(--d);margin-top:3px;line-height:1.25}
.lesson-card .lc-tags{display:flex;gap:4px;flex-wrap:wrap;margin-top:10px}
.lesson-card .lc-tag{font-size:.66rem;background:var(--bg);color:var(--m);padding:2px 7px;border-radius:10px;border:1px solid var(--b)}

/* lesson detail */
.lhd{margin-bottom:20px;padding-bottom:16px;border-bottom:2px solid var(--b)}
.lhd .lh-chip{display:inline-flex;align-items:center;gap:6px;padding:4px 12px;border-radius:20px;font-size:.72rem;font-weight:700;color:#fff;margin-bottom:10px}
.lhd h1{font-size:1.8rem;line-height:1.2;color:var(--d);margin-bottom:4px;letter-spacing:-.3px}
.lhd .lh-sub{font-size:.92rem;color:var(--m)}

/* tabs */
.tabs{display:flex;gap:0;border-bottom:2px solid var(--b);margin-bottom:22px;overflow-x:auto;scrollbar-width:none}
.tabs::-webkit-scrollbar{display:none}
.tab{padding:11px 18px;font-size:.85rem;font-weight:600;color:var(--m);cursor:pointer;border-bottom:3px solid transparent;white-space:nowrap;transition:var(--t);display:flex;align-items:center;gap:6px;margin-bottom:-2px}
.tab:hover{color:var(--p)}
.tab.act{color:var(--p);border-bottom-color:var(--p)}
.tab i{font-size:.85rem}

/* panel */
.panel{display:none;animation:fade .25s ease}
.panel.act{display:block}
@keyframes fade{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}

/* info grid */
.info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-bottom:18px}
.info-card{background:var(--w);border:1px solid var(--b);border-radius:12px;padding:16px}
.info-card h4{font-size:.72rem;text-transform:uppercase;letter-spacing:1px;color:var(--l);margin-bottom:8px;display:flex;align-items:center;gap:6px}
.info-card h4 i{color:var(--p);font-size:.9rem}
.info-card p{font-size:.92rem;color:var(--d);line-height:1.55}

.callout{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);border-left:4px solid var(--p);padding:14px 18px;border-radius:0 10px 10px 0;margin-bottom:18px;font-size:.9rem;color:var(--d)}
.callout.cyber{background:linear-gradient(135deg,#0B3C5D,#1E40AF);color:#fff;border-left-color:#60A5FA}
.callout.cyber h4{color:#93C5FD}
.callout h4{font-size:.78rem;text-transform:uppercase;letter-spacing:.8px;color:var(--p);margin-bottom:6px;font-weight:700}

/* vocab */
.vocab-meta{background:var(--w);border:1px solid var(--b);border-radius:10px;padding:14px 16px;display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;font-size:.85rem;flex-wrap:wrap;gap:10px}
.vocab-meta .vm-stat b{color:var(--p);font-size:1.05rem}
.vocab-ctrls{display:flex;gap:8px}
.v-mode-btn{background:var(--bg);border:1px solid var(--b);padding:6px 12px;border-radius:8px;font-family:inherit;font-size:.78rem;font-weight:600;color:var(--m);cursor:pointer;display:flex;align-items:center;gap:6px}
.v-mode-btn.act{background:var(--p);color:#fff;border-color:var(--p)}

.vocab-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px;margin-bottom:14px}
.v-chip{background:var(--w);border:1px solid var(--b);padding:9px 12px;border-radius:8px;font-size:.85rem;color:var(--d);transition:var(--t);cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:6px}
.v-chip:hover{border-color:var(--p);background:var(--pvl)}
.v-chip.known{background:var(--okl);color:#065F46;border-color:var(--ok);text-decoration:line-through;opacity:.65}
.v-chip i{font-size:.7rem;color:var(--l)}
.v-chip.known i{color:var(--ok)}

.flashcard-zone{background:#0F172A;border-radius:14px;padding:34px 24px;min-height:260px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;position:relative;margin-bottom:14px}
.flashcard{background:#fff;color:var(--d);min-height:160px;width:100%;max-width:460px;border-radius:14px;padding:30px 24px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 10px 30px rgba(0,0,0,.25);cursor:pointer;position:relative}
.flashcard .fc-w{font-size:1.9rem;font-weight:700;color:var(--d);text-align:center;letter-spacing:-.3px}
.flashcard .fc-flip{font-size:.7rem;color:var(--l);position:absolute;bottom:10px}
.flashcard.flip{background:#1E293B;color:#fff}
.flashcard .fc-prompt{font-size:.92rem;color:var(--m);text-align:center;margin-top:10px}
.flashcard.flip .fc-prompt{color:#94A3B8}
.fc-counter{color:rgba(255,255,255,.7);font-size:.78rem;margin-bottom:14px}
.fc-actions{display:flex;gap:8px;margin-top:14px}
.fc-btn{background:rgba(255,255,255,.12);color:#fff;border:1px solid rgba(255,255,255,.18);padding:8px 16px;border-radius:8px;font-family:inherit;font-size:.82rem;font-weight:600;cursor:pointer;display:flex;align-items:center;gap:6px}
.fc-btn:hover{background:rgba(255,255,255,.2)}
.fc-btn.ok{background:var(--ok);border-color:var(--ok)}
.fc-btn.sk{background:var(--wa);border-color:var(--wa)}

/* reading */
.read-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px;margin-bottom:14px}
.read-stat{background:var(--w);border:1px solid var(--b);border-radius:10px;padding:12px}
.read-stat-l{font-size:.68rem;color:var(--l);text-transform:uppercase;letter-spacing:.8px}
.read-stat-v{font-size:1.1rem;font-weight:700;color:var(--d);margin-top:3px}
.rp-area{background:var(--bg);border-left:4px solid var(--p);padding:18px 22px;border-radius:0 10px 10px 0;margin-bottom:14px;min-height:120px;font-size:.93rem;line-height:1.8}
.rp-area[contenteditable]{outline:none}
.rp-area.empty::before{content:attr(data-ph);color:var(--l);font-style:italic}
.q-block{background:var(--w);border:1px solid var(--b);border-radius:10px;padding:14px 16px;margin-bottom:10px}
.q-block .q-n{font-size:.72rem;color:var(--p);font-weight:700;letter-spacing:.8px;margin-bottom:4px}
.q-block .q-t{font-size:.95rem;color:var(--d);font-weight:600;margin-bottom:8px}
.q-block textarea{width:100%;min-height:50px;padding:9px 12px;border:1px solid var(--b);border-radius:8px;font-family:inherit;font-size:.9rem;resize:vertical;background:var(--bg)}
.q-block textarea:focus{outline:none;border-color:var(--p);background:#fff}

/* listening */
.audio-src-card{background:linear-gradient(135deg,#1E293B,#334155);color:#fff;border-radius:14px;padding:18px 22px;margin-bottom:14px}
.audio-src-card .as-t{font-size:1rem;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px}
.audio-src-card .as-d{font-size:.88rem;color:#CBD5E1}
.audio-src-card .as-meta{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.as-chip{background:rgba(255,255,255,.15);padding:4px 10px;border-radius:10px;font-size:.72rem;font-weight:600}
.as-chip.pd{background:rgba(16,185,129,.3);color:#A7F3D0}
.as-chip.cc{background:rgba(245,158,11,.3);color:#FDE68A}
.audio-src-card a{color:#93C5FD;text-decoration:underline}

.audio-pool{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:10px}
.ap-card{background:var(--w);border:1px solid var(--b);border-radius:10px;padding:12px}
.ap-card .ap-name{font-size:.9rem;font-weight:700;color:var(--d)}
.ap-card .ap-dom{font-size:.74rem;color:var(--p);margin-top:2px;word-break:break-all}
.ap-card .ap-lic{font-size:.7rem;color:var(--m);margin-top:6px;display:inline-block;background:var(--bg);padding:2px 8px;border-radius:8px}

/* writing */
.write-meta{background:var(--w);border:1px solid var(--b);border-radius:12px;padding:14px 18px;margin-bottom:12px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px}
.write-target{font-size:.88rem;color:var(--d)}
.write-target b{color:var(--p)}
.write-counter{font-size:1.15rem;font-weight:800;color:var(--l);font-variant-numeric:tabular-nums}
.write-counter.ok{color:var(--ok)}
.write-counter.low{color:var(--wa)}
.write-counter.over{color:var(--er)}
.warea{width:100%;min-height:260px;padding:18px;border:2px solid var(--b);border-radius:12px;font-family:'DM Sans',sans-serif;font-size:1rem;line-height:1.7;resize:vertical;background:var(--bg);color:var(--d)}
.warea:focus{outline:none;border-color:var(--p);background:#fff;box-shadow:0 0 0 4px rgba(37,99,235,.1)}
.cefr-check{background:var(--wal);border-radius:10px;padding:12px 16px;margin-top:12px;font-size:.85rem;color:#78350F}
.cefr-check h4{font-size:.78rem;font-weight:700;margin-bottom:6px}
.cefr-check ul{list-style:none;padding:0}
.cefr-check li{padding:3px 0;display:flex;align-items:center;gap:8px}
.cefr-check input{accent-color:var(--p);cursor:pointer}

/* buttons */
.btn{padding:10px 20px;border-radius:10px;font-family:inherit;font-size:.85rem;font-weight:600;cursor:pointer;transition:var(--t);border:none;display:inline-flex;align-items:center;gap:7px}
.btn.pri{background:var(--p);color:#fff}
.btn.pri:hover{background:var(--pd);transform:translateY(-1px);box-shadow:0 6px 16px rgba(37,99,235,.3)}
.btn.sec{background:var(--bg);color:var(--d);border:1px solid var(--b)}
.btn.sec:hover{background:#fff;border-color:var(--p);color:var(--p)}
.btn.ok{background:var(--ok);color:#fff}
.btn.ok:hover{background:#059669}
.btn.wide{width:100%;justify-content:center}

.lesson-nav{display:flex;justify-content:space-between;align-items:center;margin-top:28px;padding-top:20px;border-top:1px solid var(--b);gap:10px}

/* overview cards (level home) */
.lvl-overview{background:linear-gradient(135deg,var(--cyber),#1E40AF);color:#fff;border-radius:14px;padding:22px 26px;margin-bottom:20px;position:relative;overflow:hidden}
.lvl-overview::after{content:"";position:absolute;top:-50%;right:-10%;width:40%;height:200%;background:rgba(255,255,255,.04);border-radius:50%;transform:rotate(-18deg)}
.lvl-overview h2{font-size:1.6rem;margin-bottom:2px;position:relative;z-index:1;letter-spacing:-.3px}
.lvl-overview .lo-sub{color:#93C5FD;font-size:.92rem;margin-bottom:14px;position:relative;z-index:1}
.lvl-overview .lo-stats{display:flex;gap:18px;flex-wrap:wrap;position:relative;z-index:1}
.lvl-overview .lo-stat b{color:#FDE68A;font-size:1.15rem;display:block}
.lvl-overview .lo-stat span{color:#CBD5E1;font-size:.72rem;text-transform:uppercase;letter-spacing:.6px}

/* footer */
.footer{text-align:center;padding:30px 24px;color:var(--l);font-size:.78rem;border-top:1px solid var(--b);margin-top:40px}

/* language toggle + pronunciation modal */
.lang-pill{display:inline-flex;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:18px;overflow:hidden;padding:2px}
.lang-opt{padding:5px 12px;font-size:.75rem;font-weight:700;color:rgba(255,255,255,.65);cursor:pointer;border-radius:14px;transition:var(--t);user-select:none}
.lang-opt.act{background:linear-gradient(135deg,#2563EB,#3B82F6);color:#fff;box-shadow:0 2px 8px rgba(37,99,235,.4)}

.pron-overlay{display:none;position:fixed;inset:0;background:rgba(15,23,42,.6);backdrop-filter:blur(4px);z-index:500;align-items:center;justify-content:center;padding:20px}
.pron-overlay.sh{display:flex;animation:fade .2s ease}
.pron-modal{background:#fff;border-radius:16px;max-width:520px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,.4);overflow:hidden;position:relative}
.pron-head{background:linear-gradient(135deg,#0F172A,#1E293B);color:#fff;padding:26px 28px 20px;position:relative}
.pron-word{font-size:2.2rem;font-weight:800;letter-spacing:-.8px;line-height:1}
.pron-ipa{font-family:'JetBrains Mono',monospace;font-size:1.1rem;color:#93C5FD;margin-top:8px;letter-spacing:.5px}
.pron-ipa.empty{color:#64748B;font-style:italic;font-size:.85rem;font-family:inherit}
.pron-respell{font-size:.82rem;color:#CBD5E1;margin-top:3px;font-style:italic}
.pron-close{position:absolute;top:14px;right:14px;background:rgba(255,255,255,.12);border:none;color:#fff;width:34px;height:34px;border-radius:50%;cursor:pointer;font-size:.95rem;display:flex;align-items:center;justify-content:center;transition:var(--t)}
.pron-close:hover{background:rgba(255,255,255,.22)}
.pron-listen{background:linear-gradient(135deg,#2563EB,#3B82F6);color:#fff;border:none;padding:10px 20px;border-radius:10px;font-family:inherit;font-size:.9rem;font-weight:700;cursor:pointer;display:inline-flex;gap:8px;align-items:center;margin-top:14px;box-shadow:0 4px 12px rgba(37,99,235,.4);transition:var(--t)}
.pron-listen:hover{transform:translateY(-1px);box-shadow:0 6px 16px rgba(37,99,235,.55)}
.pron-listen.playing{background:linear-gradient(135deg,#DC2626,#991B1B)}
.pron-voices{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap}
.pron-voice-btn{background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.15);padding:5px 10px;border-radius:7px;font-size:.7rem;font-weight:600;cursor:pointer;font-family:inherit}
.pron-voice-btn:hover{background:rgba(255,255,255,.2)}
.pron-voice-btn.act{background:#3B82F6;border-color:#3B82F6}
.pron-body{padding:20px 28px 24px;max-height:50vh;overflow-y:auto}
.pron-sec{margin-bottom:14px}
.pron-sec h4{font-size:.7rem;text-transform:uppercase;letter-spacing:1.2px;color:var(--l);margin-bottom:5px;font-weight:700}
.pron-pos{display:inline-block;background:var(--pvl);color:var(--p);padding:2px 10px;border-radius:10px;font-size:.72rem;font-weight:700;font-style:italic;margin-right:6px}
.pron-def{font-size:.92rem;color:var(--d);line-height:1.55;margin-bottom:6px}
.pron-ex{font-size:.82rem;color:var(--m);font-style:italic;padding-left:12px;border-left:2px solid var(--pl);margin-top:4px}
.pron-loading{text-align:center;padding:20px;color:var(--l)}
.pron-error{background:var(--wal);color:#78350F;padding:10px 14px;border-radius:8px;font-size:.82rem;display:flex;gap:8px;align-items:center}
.pron-mark-row{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
.pron-mark-btn{padding:8px 14px;border-radius:8px;font-size:.8rem;font-weight:600;border:none;cursor:pointer;display:inline-flex;gap:6px;align-items:center;font-family:inherit}
.pron-mark-btn.known{background:var(--ok);color:#fff}
.pron-mark-btn.review{background:var(--wa);color:#fff}

/* Voice recording */
.pron-rec-zone{margin-top:14px;padding:14px;background:linear-gradient(135deg,#FEF2F2,#FEE2E2);border-radius:10px;border:1px solid #FECACA}
.pron-rec-zone h4{font-size:.72rem;text-transform:uppercase;letter-spacing:1px;color:#991B1B;margin-bottom:8px;font-weight:700;display:flex;align-items:center;gap:6px}
.pron-rec-row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.pron-rec-btn{background:linear-gradient(135deg,#DC2626,#991B1B);color:#fff;border:none;padding:9px 16px;border-radius:9px;font-family:inherit;font-size:.82rem;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:var(--t);box-shadow:0 3px 10px rgba(220,38,38,.3)}
.pron-rec-btn:hover{transform:translateY(-1px);box-shadow:0 5px 14px rgba(220,38,38,.4)}
.pron-rec-btn.recording{background:linear-gradient(135deg,#7F1D1D,#450A0A);animation:pulse 1.2s infinite}
@keyframes pulse{0%,100%{box-shadow:0 3px 10px rgba(220,38,38,.3)}50%{box-shadow:0 3px 18px rgba(220,38,38,.6),0 0 0 6px rgba(220,38,38,.15)}}
.pron-rec-play{background:var(--p);color:#fff;border:none;padding:9px 14px;border-radius:9px;font-family:inherit;font-size:.82rem;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.pron-rec-play:hover{background:var(--pd)}
.pron-rec-play:disabled{background:var(--l);cursor:not-allowed;opacity:.6}
.pron-rec-status{font-size:.76rem;color:#991B1B;font-weight:600;display:flex;align-items:center;gap:6px}
.pron-rec-status.ready{color:#065F46}
.pron-rec-meter{height:6px;background:#FECACA;border-radius:3px;overflow:hidden;margin-top:8px}
.pron-rec-meter-fill{height:100%;background:linear-gradient(90deg,#DC2626,#F59E0B,#10B981);width:0%;transition:width .1s}
.pron-compare{background:rgba(255,255,255,.8);border-radius:8px;padding:8px 12px;margin-top:8px;font-size:.78rem;color:#7F1D1D}
.pron-compare b{color:var(--p)}

/* Lesson / teaching notes */
.ln-section{background:var(--w);border:1px solid var(--b);border-radius:12px;padding:18px 22px;margin-bottom:14px;box-shadow:var(--sh)}
.ln-section h3{font-size:.75rem;text-transform:uppercase;letter-spacing:1.2px;color:var(--p);font-weight:800;margin-bottom:10px;display:flex;align-items:center;gap:8px}
.ln-section h3 i{color:var(--p)}
.ln-warmup{background:linear-gradient(135deg,#EFF6FF,#DBEAFE);border-left:5px solid var(--p);padding:16px 20px;border-radius:0 12px 12px 0;margin-bottom:14px}
.ln-warmup .lnw-label{font-size:.7rem;text-transform:uppercase;letter-spacing:1.2px;color:var(--p);font-weight:800;margin-bottom:6px;display:flex;align-items:center;gap:6px}
.ln-warmup p{font-size:.95rem;line-height:1.65;color:var(--d)}
.ln-grammar{background:linear-gradient(135deg,#FEFCE8,#FEF9C3);border-left:5px solid #EAB308;border-radius:0 12px 12px 0;padding:18px 22px;margin-bottom:14px}
.ln-grammar .lng-title{font-size:1.05rem;font-weight:800;color:#713F12;margin-bottom:6px;display:flex;align-items:center;gap:8px}
.ln-grammar .lng-rule{font-size:.92rem;color:#422006;line-height:1.6;margin-bottom:12px}
.ln-table{width:100%;border-collapse:collapse;margin-bottom:12px;background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.06)}
.ln-table th{background:#713F12;color:#fff;font-size:.75rem;padding:8px 12px;text-align:left;text-transform:uppercase;letter-spacing:.8px;font-weight:700}
.ln-table td{padding:9px 12px;border-bottom:1px solid #FEF3C7;font-size:.88rem;color:#422006;vertical-align:top}
.ln-table tr:last-child td{border-bottom:none}
.ln-table td:first-child{font-weight:700;color:#713F12;font-family:'JetBrains Mono',monospace;font-size:.82rem}
.ln-examples{display:flex;flex-direction:column;gap:6px}
.ln-ex{background:rgba(255,255,255,.7);padding:9px 14px;border-radius:8px;display:flex;justify-content:space-between;align-items:center;gap:14px;font-size:.88rem}
.ln-ex-en{color:#422006;font-weight:500;flex:1}
.ln-ex-note{color:#713F12;font-style:italic;font-size:.78rem;text-align:right;padding:3px 10px;background:#FEF3C7;border-radius:10px;white-space:nowrap}
.ln-phrases{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px}
.ln-phrase{background:var(--bg);padding:10px 14px;border-radius:8px;border-left:3px solid var(--p)}
.ln-phrase .lnp-ph{font-size:.9rem;color:var(--d);font-weight:700;margin-bottom:3px}
.ln-phrase .lnp-use{font-size:.76rem;color:var(--m);font-style:italic}
.ln-mistakes{display:flex;flex-direction:column;gap:10px}
.ln-mist{background:#FEF2F2;border:1px solid #FECACA;border-radius:8px;padding:10px 14px}
.ln-mist-wr{color:#991B1B;text-decoration:line-through;font-size:.88rem;font-weight:600}
.ln-mist-wr::before{content:"\2716 ";color:#DC2626;font-weight:700;text-decoration:none}
.ln-mist-ri{color:#065F46;font-size:.88rem;font-weight:600;margin-top:4px}
.ln-mist-ri::before{content:"\2713 ";color:#10B981;font-weight:700}
.ln-mist-why{color:var(--m);font-size:.78rem;margin-top:4px;padding-top:4px;border-top:1px dashed #FCA5A5}
.ln-tip{background:linear-gradient(135deg,#0F172A,#1E293B);color:#fff;padding:16px 20px;border-radius:12px;margin-bottom:14px;display:flex;gap:14px;align-items:flex-start}
.ln-tip i{font-size:1.4rem;color:#FDE68A;flex-shrink:0}
.ln-tip-content .lnt-label{font-size:.7rem;text-transform:uppercase;letter-spacing:1.2px;color:#FDE68A;font-weight:800;margin-bottom:3px}
.ln-tip-content p{font-size:.92rem;color:#E0E7FF;line-height:1.55}
.ln-pending{background:linear-gradient(135deg,#FEF3C7,#FDE68A);border:1px dashed #F59E0B;border-radius:12px;padding:18px 22px;color:#78350F;font-size:.92rem;display:flex;gap:14px;align-items:center}
.ln-pending i{font-size:1.6rem;color:#D97706}
.ln-next{background:linear-gradient(135deg,#065F46,#047857);color:#fff;padding:14px 18px;border-radius:12px;margin-top:14px;display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap}
.ln-next .lnn-label{font-size:.82rem;color:#D1FAE5}
.ln-next .lnn-label b{color:#fff}
.ln-next button{background:#fff;color:#065F46;border:none;padding:9px 18px;border-radius:8px;font-family:inherit;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:7px;transition:var(--t)}
.ln-next button:hover{transform:translateY(-1px);box-shadow:0 4px 12px rgba(0,0,0,.2)}

/* Use of English exercise variants */
.uoe-sent{background:var(--pvl);padding:10px 14px;border-radius:8px;margin-bottom:10px;font-size:.95rem;line-height:1.7;color:var(--d)}
.uoe-sent .uoe-gap{display:inline-block;min-width:90px;padding:2px 6px;border-bottom:2px solid var(--p);background:#fff;color:var(--p);font-weight:700;text-align:center}
.uoe-base{display:inline-block;background:#0F172A;color:#fff;padding:3px 12px;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:.8rem;font-weight:700;letter-spacing:1px;margin-right:8px;text-transform:uppercase}
.uoe-keyword{display:inline-block;background:linear-gradient(135deg,#D97706,#F59E0B);color:#fff;padding:3px 12px;border-radius:6px;font-weight:700;font-size:.82rem;margin:0 4px;text-transform:uppercase;letter-spacing:.5px;box-shadow:0 2px 6px rgba(217,119,6,.3)}
.uoe-from{font-size:.72rem;color:var(--m);margin-bottom:4px;text-transform:uppercase;letter-spacing:.8px;font-weight:600}
.uoe-original{background:var(--bg);padding:9px 14px;border-radius:7px;margin-bottom:8px;font-size:.9rem;color:var(--d);border-left:3px solid var(--l)}
.uoe-to{font-size:.72rem;color:var(--p);margin:6px 0 4px;text-transform:uppercase;letter-spacing:.8px;font-weight:700}
.uoe-word-count{font-size:.72rem;color:var(--m);margin-top:4px;text-align:right}
.uoe-word-count b{color:var(--p)}

/* Use of English progress header */
.uoe-intro{background:linear-gradient(135deg,#1E1B4B,#312E81);color:#fff;padding:18px 22px;border-radius:12px;margin-bottom:16px}
.uoe-intro h3{font-size:1.05rem;font-weight:700;margin-bottom:4px;display:flex;align-items:center;gap:8px}
.uoe-intro p{font-size:.85rem;color:#C7D2FE;line-height:1.5}
.uoe-intro .uoe-parts{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.uoe-intro .uoe-part{background:rgba(255,255,255,.12);padding:4px 10px;border-radius:10px;font-size:.72rem;color:#E0E7FF;font-weight:600}

/* passages + interactive exercises */
.passage-card{background:#fff;border-radius:14px;box-shadow:var(--sh);padding:22px 26px;margin-bottom:16px;border-left:5px solid var(--p)}
.passage-title{font-size:1.15rem;font-weight:700;color:var(--d);margin-bottom:4px;letter-spacing:-.2px}
.passage-meta{font-size:.74rem;color:var(--l);margin-bottom:14px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.passage-meta .pm-badge{background:var(--pvl);color:var(--p);padding:2px 9px;border-radius:10px;font-weight:600}
.passage-body{font-size:.98rem;line-height:1.85;color:var(--d);white-space:pre-wrap}
.passage-body p{margin-bottom:10px}
.passage-source{margin-top:14px;padding-top:10px;border-top:1px dashed var(--b);font-size:.72rem;color:var(--m);font-style:italic}
.reading-timer{background:var(--wal);color:#78350F;border-radius:8px;padding:6px 12px;font-size:.78rem;font-weight:600;display:inline-flex;align-items:center;gap:6px;cursor:pointer}
.reading-timer.on{background:var(--ok);color:#fff}

.ex-block{background:#fff;border:1px solid var(--b);border-radius:12px;padding:16px 18px;margin-bottom:12px}
.ex-head{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.ex-num{background:var(--p);color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.8rem;flex-shrink:0}
.ex-type{font-size:.65rem;text-transform:uppercase;letter-spacing:1px;color:var(--l);font-weight:700}
.ex-q{font-size:.95rem;color:var(--d);font-weight:600;margin-bottom:12px;line-height:1.45}
.ex-opts{display:flex;flex-direction:column;gap:6px}
.ex-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;border:2px solid var(--b);border-radius:8px;cursor:pointer;transition:var(--t);font-size:.9rem}
.ex-opt:hover{border-color:var(--pl);background:var(--pvl)}
.ex-opt.selected{border-color:var(--p);background:var(--pvl)}
.ex-opt.correct{border-color:var(--ok);background:var(--okl);color:#065F46}
.ex-opt.wrong{border-color:var(--er);background:var(--erl);color:#991B1B}
.ex-opt .ex-letter{width:26px;height:26px;border-radius:6px;background:var(--bg);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.78rem;color:var(--m);flex-shrink:0;border:1px solid var(--b)}
.ex-opt.selected .ex-letter{background:var(--p);color:#fff;border-color:var(--p)}
.ex-opt.correct .ex-letter{background:var(--ok);color:#fff;border-color:var(--ok)}
.ex-opt.wrong .ex-letter{background:var(--er);color:#fff;border-color:var(--er)}

.ex-gap-input{border:2px solid var(--b);background:var(--bg);padding:7px 11px;border-radius:7px;font-family:inherit;font-size:.9rem;width:180px;color:var(--p);font-weight:600}
.ex-gap-input:focus{outline:none;border-color:var(--p);background:#fff}
.ex-gap-input.correct{border-color:var(--ok);background:var(--okl);color:#065F46}
.ex-gap-input.wrong{border-color:var(--er);background:var(--erl);color:#991B1B}

.ex-match{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ex-match-col h5{font-size:.68rem;text-transform:uppercase;letter-spacing:.8px;color:var(--l);margin-bottom:6px;font-weight:700}
.ex-match-item{padding:9px 12px;border:2px solid var(--b);border-radius:7px;margin-bottom:6px;cursor:pointer;transition:var(--t);font-size:.85rem;position:relative}
.ex-match-item:hover{border-color:var(--pl);background:var(--pvl)}
.ex-match-item.selected{border-color:var(--p);background:var(--pvl);box-shadow:0 0 0 3px rgba(37,99,235,.1)}
.ex-match-item.matched{background:var(--okl);border-color:var(--ok);cursor:default}
.ex-match-item.wrong{animation:shk .4s;border-color:var(--er);background:var(--erl)}
.ex-match-item .match-num{position:absolute;top:-7px;right:-7px;width:20px;height:20px;background:var(--ok);color:#fff;border-radius:50%;display:none;align-items:center;justify-content:center;font-size:.65rem;font-weight:700}
.ex-match-item.matched .match-num{display:flex}
@keyframes shk{0%,100%{transform:translateX(0)}25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}

.ex-short-text{width:100%;min-height:70px;padding:10px 13px;border:1px solid var(--b);border-radius:8px;font-family:inherit;font-size:.9rem;resize:vertical;background:var(--bg)}
.ex-short-text:focus{outline:none;border-color:var(--p);background:#fff}

.ex-actions{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
.ex-btn{padding:7px 14px;border-radius:7px;font-size:.78rem;font-weight:600;font-family:inherit;cursor:pointer;border:none;display:inline-flex;align-items:center;gap:5px;transition:var(--t)}
.ex-btn.check{background:var(--p);color:#fff}.ex-btn.check:hover{background:var(--pd)}
.ex-btn.reset{background:var(--bg);color:var(--m);border:1px solid var(--b)}
.ex-btn.reset:hover{background:#fff;color:var(--d)}
.ex-btn.reveal{background:var(--wa);color:#fff}

.ex-feedback{margin-top:10px;padding:10px 14px;border-radius:8px;font-size:.85rem;display:none}
.ex-feedback.ok{background:var(--okl);color:#065F46;border-left:3px solid var(--ok);display:block}
.ex-feedback.no{background:var(--erl);color:#991B1B;border-left:3px solid var(--er);display:block}
.ex-feedback .ex-fb-head{font-weight:700;margin-bottom:3px;display:flex;align-items:center;gap:6px}
.ex-feedback.model{background:var(--wal);color:#78350F;border-left:3px solid var(--wa);display:block}

.ex-progress{background:var(--w);border:1px solid var(--b);border-radius:10px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;font-size:.82rem}
.ex-progress b{color:var(--p)}
.ex-score-pill{padding:4px 12px;border-radius:12px;font-size:.78rem;font-weight:700}
.ex-score-pill.g{background:var(--okl);color:#065F46}
.ex-score-pill.y{background:var(--wal);color:#78350F}
.ex-score-pill.r{background:var(--erl);color:#991B1B}

.content-pending{background:linear-gradient(135deg,#FEF3C7,#FDE68A);border:1px dashed #F59E0B;border-radius:12px;padding:16px 20px;color:#78350F;font-size:.9rem;margin-bottom:14px;display:flex;gap:12px;align-items:center}
.content-pending i{font-size:1.4rem;color:#D97706}

/* ===== RESPONSIVE: tablet ===== */
@media(max-width:900px){
 .lay{grid-template-columns:1fr}
 .sb{display:none;position:fixed;left:0;top:108px;bottom:0;width:280px;z-index:99;box-shadow:6px 0 20px rgba(0,0,0,.2);overflow-y:auto}
 .sb.op{display:block}
 .mn{padding:18px;max-width:100%}
 .wel-stats{grid-template-columns:repeat(2,1fr)}
 .lvl-grid{grid-template-columns:1fr}
 .hd{padding:10px 14px}
 .pbar{padding:0 10px}
 .pmini{display:none}
 .hdr-r .hd-btn-label{display:none}
 .info-grid{grid-template-columns:1fr}
 .lesson-grid{grid-template-columns:1fr}
 .ex-match{grid-template-columns:1fr}
 .read-stats{grid-template-columns:repeat(2,1fr)}
 .audio-pool{grid-template-columns:1fr}
 .ln-phrases{grid-template-columns:1fr}
 .vocab-list{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
 .ln-table{font-size:.78rem}
 .ln-table th,.ln-table td{padding:6px 8px}
 .mobile-menu-btn{display:flex !important}
 .sb-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:98}
 .sb-overlay.op{display:block}
}
/* ===== RESPONSIVE: phone ===== */
@media(max-width:600px){
 body{font-size:14px}
 .hd{padding:8px 10px;flex-wrap:wrap;gap:8px}
 .logo{gap:8px;flex:1;min-width:0}
 .logo-box{width:38px;height:38px;font-size:1.05rem}
 .logo-tx .t1{font-size:.92rem}
 .logo-tx .t2{font-size:.62rem;letter-spacing:.8px}
 .hdr-r{gap:6px}
 .hd-btn{padding:6px 8px;font-size:.74rem}
 .lang-pill{padding:1px}
 .lang-opt{padding:4px 8px;font-size:.7rem}
 .pbar{padding:0 4px}
 .ptab{padding:11px 12px;font-size:.74rem;gap:5px}
 .lay{min-height:calc(100vh - 96px)}
 .sb{top:96px;width:85vw;max-width:300px}
 .mn{padding:14px 12px}
 .wel{padding:6px 0 18px}
 .wel h1{font-size:1.45rem;line-height:1.2}
 .wel p.lead{font-size:.92rem}
 .wel-stats{grid-template-columns:repeat(2,1fr);gap:8px}
 .wel-stat{padding:12px 8px}
 .wel-stat-v{font-size:1.4rem}
 .wel-stat-l{font-size:.65rem}
 .lvl-card{padding:14px}
 .section h2{font-size:1.05rem}
 .tbl{font-size:.74rem}
 .tbl th,.tbl td{padding:7px 8px}
 .lhd h1{font-size:1.35rem;line-height:1.2}
 .lhd .lh-sub{font-size:.82rem}
 .tabs{gap:0}
 .tab{padding:9px 11px;font-size:.78rem}
 .tab i{font-size:.78rem}
 .info-card{padding:14px}
 .info-card p{font-size:.86rem}
 .callout{padding:11px 14px;font-size:.85rem}
 .ln-section{padding:14px 16px}
 .ln-warmup,.ln-grammar,.ln-tip{padding:13px 16px}
 .ln-grammar .lng-title{font-size:.95rem}
 .ln-grammar .lng-rule{font-size:.85rem}
 .lesson-nav{flex-direction:column;align-items:stretch;gap:8px}
 .lesson-nav .btn{width:100%;justify-content:center}
 .vocab-list{grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:7px}
 .v-chip{padding:7px 10px;font-size:.82rem;gap:7px}
 .flashcard{padding:24px 18px;min-height:130px}
 .flashcard .fc-w{font-size:1.55rem}
 .fc-actions{flex-wrap:wrap;justify-content:center}
 .fc-btn{padding:7px 12px;font-size:.78rem}
 .passage-card{padding:16px 16px}
 .passage-title{font-size:1.05rem}
 .passage-body{font-size:.94rem;line-height:1.7}
 .ex-block{padding:13px 14px}
 .ex-q{font-size:.9rem}
 .ex-opt{padding:9px 11px;font-size:.86rem}
 .uoe-intro{padding:14px 16px}
 .uoe-intro h3{font-size:.95rem}
 .uoe-intro p{font-size:.8rem}
 .uoe-sent{font-size:.88rem;padding:8px 11px}
 .uoe-keyword{padding:2px 9px;font-size:.74rem}
 .write-meta{padding:11px 13px;font-size:.8rem}
 .warea{min-height:200px;padding:13px;font-size:.92rem}
 .audio-src-card{padding:14px 16px}
 .pron-modal{margin:0 8px;border-radius:14px}
 .pron-head{padding:18px 18px 14px}
 .pron-word{font-size:1.7rem}
 .pron-body{padding:14px 18px 18px;max-height:55vh}
 .pron-mark-row,.pron-voices{flex-direction:column}
 .pron-mark-btn,.pron-voice-btn{width:100%;justify-content:center}
 .footer{padding:18px 12px;font-size:.7rem}
 .ln-table{font-size:.72rem;display:block;overflow-x:auto;white-space:nowrap}
 .ln-mist-wr,.ln-mist-ri{font-size:.84rem}
 .ln-ex{flex-direction:column;align-items:stretch;gap:6px}
 .ln-ex-note{text-align:left;align-self:flex-start}
}
@media(max-width:380px){
 .ptab{padding:9px 8px;font-size:.7rem}
 .logo-tx .t1{font-size:.84rem}
 .wel h1{font-size:1.25rem}
 .vocab-list{grid-template-columns:1fr 1fr}
}
@media(hover:none) and (pointer:coarse){
 .v-chip:hover{transform:none;box-shadow:none}
 .lvl-card:hover{transform:none;box-shadow:none}
 .ex-opt:hover{background:initial}
 button,.btn,.tab,.ptab,.v-chip,.ex-opt,.lsn-item{min-height:40px;-webkit-tap-highlight-color:rgba(37,99,235,.15)}
}
*{-webkit-text-size-adjust:100%;text-size-adjust:100%}
input,textarea,button,select{font:inherit}
img{max-width:100%;height:auto}
@supports not (backdrop-filter:blur(4px)){
 .pron-overlay{background:rgba(15,23,42,.85)}
}

/* ===== Anti-overflow hardening (prevents horizontal scrolling on mobile) ===== */
html,body{overflow-x:hidden;max-width:100vw}
.mn,.callout,.info-card,.ln-section,.ln-warmup,.ln-grammar,.ln-tip,.ln-pending,.ln-next,.passage-card,.write-meta,.uoe-intro,.audio-src-card,.lhd,.section,.lvl-overview,.ex-block,.q-block,.cefr-check,.lvl-card,.lesson-card,.wel,.wel-stat{max-width:100%;min-width:0;overflow-wrap:break-word;word-wrap:break-word;word-break:break-word}
.callout,.callout *,.info-card,.info-card *,.ln-section,.ln-section *,.passage-body,.passage-body *,.uoe-intro,.uoe-intro *{overflow-wrap:break-word;word-wrap:break-word}
.tbl,.ln-table{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}
.tbl thead,.tbl tbody,.tbl tr,.ln-table thead,.ln-table tbody,.ln-table tr{display:table;width:100%;table-layout:fixed}
@media(max-width:600px){
 .tbl,.ln-table{display:block;white-space:normal}
 .tbl thead,.tbl tbody,.tbl tr,.ln-table thead,.ln-table tbody,.ln-table tr{display:revert;width:auto;table-layout:auto}
 .tbl,.ln-table{display:table;table-layout:auto}
 .lhd,.callout,.info-card,.ln-section{padding-left:14px;padding-right:14px}
}
.tabs{overflow-x:auto;-webkit-overflow-scrolling:touch;flex-wrap:nowrap}
.lay,.hd,.hdr-r,.logo,.lhd,.write-meta,.vocab-meta,.ex-progress,.lesson-nav,.lvl-overview .lo-stats{min-width:0}
.logo,.logo-tx{min-width:0;overflow:hidden}
.logo-tx .t1,.logo-tx .t2{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
</style>
</head>
<body>
<!-- HEADER -->
<header class="hd">
 <button class="mobile-menu-btn" onclick="toggleSidebar()" aria-label="Open menu" title="Menu" style="display:none;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;width:38px;height:38px;border-radius:8px;align-items:center;justify-content:center;cursor:pointer;font-size:1rem;flex-shrink:0">
  <i class="fas fa-bars"></i>
 </button>
 <div class="logo" onclick="route('home')">
  <div class="logo-box"><i class="fas fa-microchip"></i></div>
  <div class="logo-tx">
   <div class="t1">Systems Engineers English</div>
   <div class="t2">A1 \u2192 C2 \u2022 CEFR aligned</div>
  </div>
 </div>
 <div class="hdr-r">
  <div class="pmini">
   <div class="pmini-bar"><div class="pmini-fill" id="pm-fill" style="width:0%"></div></div>
   <div class="pmini-tx"><b id="pm-pct">0%</b> <span data-i18n="course_done">of course</span> \u2022 <span id="pm-done">0</span>/120 <span data-i18n="lessons">lessons</span></div>
  </div>
  <div class="lang-pill" title="Translate / Traducir">
   <span class="lang-opt" data-lang="en" onclick="setLang('en')">EN</span>
   <span class="lang-opt" data-lang="es" onclick="setLang('es')">ES</span>
  </div>
  <button class="hd-btn" onclick="resetProgress()" title="Reset progress">
   <i class="fas fa-arrow-rotate-left"></i><span class="hd-btn-label" data-i18n="reset">Reset</span>
  </button>
  <button class="hd-btn pr" onclick="exportProgress()">
   <i class="fas fa-download"></i><span class="hd-btn-label" data-i18n="export">Export</span>
  </button>
 </div>
</header>

<!-- PROGRAM BAR -->
<div class="pbar" id="pbar"></div>

<!-- LAYOUT -->
<div class="lay">
 <div class="sb-overlay" id="sb-overlay" onclick="toggleSidebar()"></div>
 <aside class="sb" id="sb"></aside>
 <main class="mn" id="mn"></main>
</div>

<footer class="footer">
 <div>Systems Engineers English Course \u2013 CEFR syllabus A1 to C2 \u2022 120 lessons \u2022 Cybersecurity & Emerging Tech</div>
 <div style="margin-top:4px">Paolo Baca Manrique \u2013 Nordic International School, Peru \u2013 2026</div>
</footer>

<!-- Pronunciation modal -->
<div class="pron-overlay" id="pron-overlay" onclick="if(event.target===this) closePron()">
 <div class="pron-modal">
  <div class="pron-head">
   <button class="pron-close" onclick="closePron()" aria-label="Close"><i class="fas fa-xmark"></i></button>
   <div class="pron-word" id="pron-word">\u2014</div>
   <div class="pron-ipa empty" id="pron-ipa">IPA loading\u2026</div>
   <div class="pron-respell" id="pron-respell"></div>
   <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px">
   <button class="pron-listen" id="pron-listen" onclick="speakCurrent()">
    <i class="fas fa-volume-high"></i> <span data-i18n="listen">Listen</span>
   </button>
   <button class="pron-listen" id="pron-translate" onclick="translateCurrent()" style="background:linear-gradient(135deg,#D97706,#F59E0B)">
    <i class="fas fa-language"></i> <span>Translate to Spanish</span>
   </button>
  </div>
  <div id="pron-translation" style="margin-top:12px;font-size:1.05rem;color:#FDE68A;font-weight:700;display:none;padding:10px 14px;background:rgba(217,119,6,.18);border-radius:8px;border-left:3px solid #F59E0B">
   <span style="font-size:.7rem;text-transform:uppercase;letter-spacing:1.2px;color:#FCD34D;display:block;margin-bottom:3px">ES</span>
   <span id="pron-es-text">—</span>
  </div>
   <div class="pron-voices" id="pron-voices"></div>
  </div>
  <div class="pron-body" id="pron-body">
   <div class="pron-loading"><i class="fas fa-spinner fa-spin"></i> Loading dictionary\u2026</div>
  </div>
 </div>
</div>

<script>
// =============================================================
// DATA
// =============================================================
const COURSE = __COURSE_DATA__;
const LVL_COLORS = __LVL_COLORS__;
const LVL_ICONS = __LVL_ICONS__;

// =============================================================
// I18N \u2013 default language is English; Spanish overlay optional
// =============================================================
const I18N_ES = {
 "of course": "del curso",
 "lessons": "clases",
 "reset": "Reiniciar",
 "export": "Exportar",
 "listen": "Escuchar",
 "Home": "Inicio",
 "Overview": "Resumen",
 "Vocabulary": "Vocabulario",
 "Reading": "Lectura",
 "Listening": "Audio",
 "Writing": "Escritura",
 "Cyber angle": "Enfoque cyber",
 "Choose your level": "Elige tu nivel",
 "Start with A1 or jump to your current level.": "Empieza por A1 o salta a tu nivel actual.",
 "The course": "El curso",
 "Levels": "Niveles",
 "Vocabulary (total)": "Vocabulario (total)",
 "Completed": "Completadas",
 "CEFR \u2013 Cambridge \u2013 IELTS \u2013 TOEFL equivalences": "Equivalencias CEFR \u2013 Cambridge \u2013 IELTS \u2013 TOEFL",
 "Ranges are indicative. Cambridge and TOEFL are multilevel exams.": "Los rangos son indicativos. Cambridge y TOEFL son ex\u00e1menes multinivel.",
 "Quantitative quotas per level": "Cuotas cuantitativas por nivel",
 "Accumulated vocabulary, reading length, writing words and listening hours.": "Vocabulario acumulado, longitud de lectura, palabras de escritura y horas de listening.",
 "Free-use audio sources": "Fuentes de audio libres",
 "Educational-use licensed domains. Verify each specific resource.": "Dominios con licencias de uso educativo. Verifica cada recurso espec\u00edfico.",
 "Professional IT profile": "Perfil profesional IT",
 "Level": "Nivel",
 "Cambridge": "Cambridge",
 "IELTS": "IELTS",
 "TOEFL iBT": "TOEFL iBT",
 "Lessons in level": "Clases del nivel",
 "20 lessons of 90 minutes each, in 4 modules: Foundations (1\u20135) \u2022 Core IT/ESP (6\u201310) \u2022 Cybersecurity (11\u201315) \u2022 Emerging Tech + Exam Prep (16\u201320).":
  "20 clases de 90 minutos, en 4 m\u00f3dulos: Foundations (1\u20135) \u2022 Core IT/ESP (6\u201310) \u2022 Cybersecurity (11\u201315) \u2022 Emerging Tech + Exam Prep (16\u201320).",
 "Pilot content": "Contenido piloto",
 "Class": "Clase",
 "Progress": "Progreso",
 "Previous": "Anterior",
 "Next": "Siguiente",
 "Next level": "Siguiente nivel",
 "Finish course": "Terminar curso",
 "View lessons": "Ver clases",
 "Mark as completed": "Marcar como completada",
 "Lesson objective": "Objetivo de la clase",
 "By the end of this session (90 min), the learner will use": "Al finalizar esta sesi\u00f3n (90 min), el estudiante podr\u00e1 usar",
 "applied to the topic": "aplicado al tema",
 "recognise and use the": "reconocer y usar las",
 "target words, and produce a written task of": "palabras objetivo, y producir una tarea escrita de",
 "Use of English": "Use of English",
 "Reading task": "Tarea de reading",
 "Listening task": "Tarea de listening",
 "Writing target": "Objetivo de writing",
 "Cybersecurity / emerging tech angle": "Enfoque de ciberseguridad / tecnolog\u00eda emergente",
 "Target vocabulary": "Vocabulario objetivo",
 "Mastered": "Dominado",
 "List": "Lista",
 "Flashcards": "Flashcards",
 "Mark all as known": "Marcar todo como dominado",
 "Review": "Revisar",
 "I know it": "La s\u00e9",
 "Click a word to hear its pronunciation and see the IPA symbols.": "Haz clic en una palabra para escuchar la pronunciaci\u00f3n y ver los s\u00edmbolos IPA.",
 "Click the card to flip": "Haz clic en la tarjeta para voltear",
 "Write a sentence using this word in an IT context.": "Escribe una oraci\u00f3n usando esta palabra en contexto IT.",
 "Reading task (Cambridge / IELTS / TOEFL style)": "Tarea de reading (estilo Cambridge / IELTS / TOEFL)",
 "Words": "Palabras",
 "CEFR range": "Rango CEFR",
 "Speed": "Velocidad",
 "Approx. time": "Tiempo aprox.",
 "Start timer": "Iniciar cron\u00f3metro",
 "Comprehension exercises": "Ejercicios de comprensi\u00f3n",
 "Not attempted yet": "Sin intentar",
 "Check all": "Revisar todo",
 "Restart": "Reiniciar",
 "Multiple Choice": "Multiple Choice",
 "True / False / Not Given": "True / False / Not Given",
 "Gap-fill": "Gap-fill",
 "Matching": "Matching",
 "Short answer": "Short answer",
 "Check": "Verificar",
 "your answer": "tu respuesta",
 "Write your answer...": "Escribe tu respuesta...",
 "Show model answer": "Ver respuesta modelo",
 "Column A": "Columna A",
 "Column B": "Columna B",
 "Correct!": "\u00a1Correcto!",
 "Incorrect": "Incorrecto",
 "Correct": "Correcto",
 "Select an option first.": "Selecciona una opci\u00f3n primero.",
 "Select True, False or Not Given.": "Selecciona True, False o Not Given.",
 "Write an answer.": "Escribe una respuesta.",
 "Expected answer:": "Respuesta esperada:",
 "Valid alternatives:": "Alternativas v\u00e1lidas:",
 "Correct answer:": "Respuesta correcta:",
 "All pairs matched correctly!": "\u00a1Todos los emparejamientos correctos!",
 "pairs matched. Keep trying.": "emparejados. Sigue intentando.",
 "Model answer": "Respuesta modelo",
 "(no model)": "(sin modelo)",
 "Reading text not yet included in the pilot.": "Texto de lectura a\u00fan no incluido en el piloto.",
 "Use the textarea to paste an article from a free source (see Listening tab for the directory).":
  "Usa el textarea para pegar un art\u00edculo de una fuente libre (ver pesta\u00f1a Listening para el directorio).",
 "Recommended range": "Rango recomendado",
 "Pasted words": "Palabras pegadas",
 "Paste the reading text here\u2026": "Pega aqu\u00ed el texto de lectura\u2026",
 "Open questions": "Preguntas abiertas",
 "Main idea": "Idea principal",
 "In 1\u20132 sentences, what is the main idea?": "En 1\u20132 oraciones, \u00bfcu\u00e1l es la idea principal?",
 "Detail": "Detalle",
 "List 3 specific facts or figures from the text.": "Enumera 3 hechos o cifras concretos del texto.",
 "Vocabulary in context": "Vocabulario en contexto",
 "Pick 3 words from today's vocabulary that appear in the text and explain them.": "Elige 3 palabras del vocabulario de hoy que aparezcan en el texto y expl\u00edcalas.",
 "Inference": "Inferencia",
 "What can be inferred that is NOT explicitly stated?": "\u00bfQu\u00e9 se puede deducir que NO est\u00e1 dicho expl\u00edcitamente?",
 "Cyber transfer": "Transferencia cyber",
 "How does this reading relate to:": "\u00bfC\u00f3mo se relaciona esta lectura con:",
 "How to work the audio": "C\u00f3mo trabajar el audio",
 "1st global listening (no text) \u2022 2nd listening with transcript \u2022 3rd shadowing of key fragments. Record new words.":
  "1\u00b0 escucha global (sin texto) \u2022 2\u00b0 escucha con transcripci\u00f3n \u2022 3\u00b0 shadowing de los fragmentos clave. Registra palabras nuevas.",
 "Recommended free sources (Level": "Fuentes libres recomendadas (Nivel",
 "Listening comprehension questions": "Preguntas de comprensi\u00f3n auditiva",
 "Write 3 key words you heard.": "Escribe 3 palabras clave que escuchaste.",
 "What is the general topic of the audio?": "\u00bfCu\u00e1l es el tema general del audio?",
 "Identify one figure, date or proper name mentioned.": "Identifica una cifra, fecha o nombre propio mencionado.",
 "Summarise the audio in 2\u20133 sentences.": "Resume el audio en 2\u20133 oraciones.",
 "Target:": "Objetivo:",
 "Suggested time:": "Tiempo sugerido:",
 "words": "palabras",
 "min": "min",
 "Write your answer here. Try to use at least 5 words from today's vocabulary. Do not use a translator for the first draft.":
  "Escribe tu respuesta aqu\u00ed. Intenta usar al menos 5 palabras del vocabulario de la clase. No uses traductor en el primer borrador.",
 "Cambridge criteria (self-review)": "Criterios Cambridge (auto-revisi\u00f3n)",
 "I answered all parts of the prompt (Content)": "Respond\u00ed a todas las partes de la consigna (Content)",
 "I used appropriate register: formal / semi-formal / informal (Communicative Achievement)":
  "Us\u00e9 el registro apropiado: formal / semi-formal / informal (Communicative Achievement)",
 "I organised the text with paragraphs and linkers (Organisation)": "Organic\u00e9 el texto con p\u00e1rrafos y conectores (Organisation)",
 "I applied the target grammar:": "Apliqu\u00e9 la gram\u00e1tica objetivo:",
 "I included \u2265 5 target vocabulary words (Range)": "Inclu\u00ed \u2265 5 palabras del vocabulario de hoy (Range)",
 "I reviewed spelling and punctuation": "Revis\u00e9 ortograf\u00eda y puntuaci\u00f3n",
 "Save draft": "Guardar borrador",
 "Export .txt": "Exportar .txt",
 "Clear": "Limpiar",
 "Clear the text?": "\u00bfLimpiar el texto?",
 "Draft saved": "Borrador guardado",
 "Reset ALL progress (lessons, vocabulary, drafts)?": "\u00bfReiniciar TODO el progreso (lecciones, vocabulario, borradores)?",
 "Progress reset": "Progreso reiniciado",
 "To dig deeper": "Para profundizar",
 "Search": "Busca en",
 "and": "y",
 "for related terms to": "t\u00e9rminos relacionados con",
 "Also": "Tambi\u00e9n",
 "for technical papers.": "para papers t\u00e9cnicos.",
 "Suggested speaking activity": "Actividad oral sugerida",
 "In pairs, explain the topic in 90 seconds using at least 6 words from the vocabulary. Your partner asks 2 follow-up questions.":
  "En pares, explica el tema en 90 segundos usando al menos 6 palabras del vocabulario. El compa\u00f1ero hace 2 preguntas de seguimiento.",
 "Exam connection": "Enlace con ex\u00e1menes",
 "CAE/CPE Reading Part 7 and Writing Part 2 (report/proposal) typically cover tech policy topics.":
  "CAE/CPE Reading Part 7 y Writing Part 2 (report/proposal) t\u00edpicamente incluyen temas de tech policy.",
 "PET/FCE Reading uses informational tech texts; IELTS Academic Reading does as well.":
  "PET/FCE Reading usa textos divulgativos sobre tecnolog\u00eda; IELTS Academic Reading tambi\u00e9n.",
 "A course for systems engineers, aligned to CEFR and calibrated against Cambridge, IELTS and TOEFL. 120 lessons. Focus on cybersecurity and emerging technology.":
  "Un programa de ingl\u00e9s t\u00e9cnico para ingenieros de sistemas, alineado al Marco Com\u00fan Europeo de Referencia y calibrado contra Cambridge, IELTS y TOEFL. 120 clases. Foco en ciberseguridad y tecnolog\u00eda emergente.",
 "per writing task": "por tarea de escritura",
 "Readings": "Lecturas",
 "Part of speech": "Categor\u00eda gramatical",
 "Definition": "Definici\u00f3n",
 "Example": "Ejemplo",
 "No definition found for this word.": "No se encontr\u00f3 definici\u00f3n para esta palabra.",
 "Mark as known": "Marcar como dominada",
 "Mark for review": "Marcar para revisar",
 "Loading dictionary\u2026": "Cargando diccionario\u2026",
 "Pronunciation not available offline for this word. TTS still works.": "Pronunciaci\u00f3n no disponible offline para esta palabra. TTS s\u00ed funciona.",
 "module": "m\u00f3dulo",
 "Foundations": "Foundations",
 "Core IT": "Core IT",
 "Cybersecurity": "Cybersecurity",
 "Emerging + Exam": "Emerging + Exam",
 "Record your pronunciation": "Graba tu pronunciaci\u00f3n",
 "Start recording": "Iniciar grabaci\u00f3n",
 "Stop": "Detener",
 "Play mine": "Mi voz",
 "Play model": "Modelo",
 "Idle": "En espera",
 "Recording...": "Grabando...",
 "Ready to play": "Lista para reproducir",
 "Microphone access denied or unavailable.": "Acceso al micr\u00f3fono denegado o no disponible.",
 "Tip": "Consejo",
 "Listen to the model first, then record yourself and compare. Self-assessment: does your recording stress the same syllable?":
  "Escucha el modelo primero, luego gr\u00e1bate y compara. Autoevaluaci\u00f3n: \u00bftu grabaci\u00f3n acent\u00faa la misma s\u00edlaba?",
 "Original:": "Original:",
 "Rewrite:": "Reescribe:",
 "Rewrite using the key word (do not change it):": "Reescribe usando la palabra clave (sin modificarla):",
 "Back to home": "Volver a inicio",
 "Back to": "Volver a",
 "progress": "progreso",
 "Your progress": "Tu progreso",
 "Per-level progress and overall course completion.": "Progreso por nivel y avance global del curso.",
 "Overall": "Total",
 "Vocabulary preview": "Vista previa del vocabulario",
 "more": "m\u00e1s",
 "Recommended path": "Ruta recomendada",
 "Start with Lesson": "Empezar con la lecci\u00f3n",
 "Translate to Spanish": "Traducir al espa\u00f1ol",
 "Translating\u2026": "Traduciendo\u2026",
 "Translation not available offline.": "Traducci\u00f3n no disponible offline.",
 "Translation not reliable. Consult a dictionary.": "Traducci\u00f3n no confiable. Consulta un diccionario.",
 "Submit for teacher feedback": "Enviar para feedback del profesor",
 "How feedback works": "C\u00f3mo funciona el feedback",
 "Click \"Submit for teacher feedback\" to download a JSON file. Send that file to your teacher (or paste it in chat) and you will receive marked corrections, errors highlighted, and 3 specific improvements.":
  "Haz clic en \"Enviar para feedback\" para descargar un archivo JSON. Env\u00edalo al profesor (o p\u00e9galo en el chat) y recibir\u00e1s correcciones marcadas, errores resaltados y 3 mejoras espec\u00edficas.",
 "Saved! Send this file to your teacher for feedback.": "\u00a1Guardado! Env\u00eda este archivo al profesor para feedback.",
 "Write something first.": "Escribe algo primero.",
 "Practise vocabulary": "Practicar vocabulario",
 "New quiz": "Nuevo quiz",
 "Match the word with its meaning": "Empareja la palabra con su significado",
 "Choose the correct word": "Elige la palabra correcta",
 "Type the missing word": "Escribe la palabra que falta",
 "Lesson": "Lecci\u00f3n",
 "Warm-up": "Introducci\u00f3n",
 "Grammar focus": "Foco gramatical",
 "Key phrases": "Frases clave",
 "Common mistakes": "Errores frecuentes",
 "Pro tip": "Consejo profesional",
 "Ready to practise?": "\u00bfListo para practicar?",
 "Go to": "Ve a",
 "for the exercises.": "para los ejercicios.",
 "Teaching notes not yet included for this lesson.": "Notas did\u00e1cticas a\u00fan no incluidas para esta lecci\u00f3n.",
 "The Overview tab summarises the grammar target and Use of English contains the practice items.":
  "La pesta\u00f1a Overview resume el objetivo gramatical y Use of English contiene los ejercicios.",
};

function setLang(l){
 state.lang = l;
 localStorage.setItem('sec_lang', l);
 document.querySelectorAll('.lang-opt').forEach(o=>o.classList.toggle('act', o.dataset.lang===l));
 render();
}
function t(en){ return (state && state.lang==='es' && I18N_ES[en]) ? I18N_ES[en] : en; }

// One-time cache invalidation for low-quality translations from previous version
const TR_CACHE_VERSION = 'v2';
if(localStorage.getItem('sec_tr_cache_ver') !== TR_CACHE_VERSION){
 Object.keys(localStorage).filter(k=>k.startsWith('sec_es_')).forEach(k=>localStorage.removeItem(k));
 localStorage.setItem('sec_tr_cache_ver', TR_CACHE_VERSION);
}

// state
const state = {
 view: 'home',  // 'home' | 'level' | 'lesson'
 levelCode: null,
 lessonN: null,
 activeTab: 'overview',
 progress: loadProgress(),
 vocab: {},   // { [lessonKey]: { [word]: 'known'|'review' } }
 flashIdx: 0,
 flashFlipped: false,
 lang: localStorage.getItem('sec_lang') || 'en',
};
state.vocab = JSON.parse(localStorage.getItem('sec_vocab')||'{}');
// mark active language pill
document.addEventListener('DOMContentLoaded', ()=>{
 document.querySelectorAll('.lang-opt').forEach(o=>o.classList.toggle('act', o.dataset.lang===state.lang));
});

function loadProgress(){
 try{return JSON.parse(localStorage.getItem('sec_progress')||'{}')}catch(e){return {}}
}
function saveProgress(){localStorage.setItem('sec_progress', JSON.stringify(state.progress))}
function saveVocab(){localStorage.setItem('sec_vocab', JSON.stringify(state.vocab))}

function lessonKey(lv,n){return lv+'-'+n}
function isDone(lv,n){return !!state.progress[lessonKey(lv,n)]}
function setDone(lv,n,v){
 const k=lessonKey(lv,n);
 if(v){state.progress[k]=Date.now()} else {delete state.progress[k]}
 saveProgress();
}

function totalDone(){return Object.keys(state.progress).length}
function levelDone(lv){return COURSE.levels.find(l=>l.code===lv).lessons.filter(le=>isDone(lv,le.n)).length}

// =============================================================
// ROUTING
// =============================================================
function toggleSidebar(){
 const sb = document.getElementById('sb');
 const ov = document.getElementById('sb-overlay');
 if(!sb) return;
 const opening = !sb.classList.contains('op');
 sb.classList.toggle('op', opening);
 if(ov) ov.classList.toggle('op', opening);
 document.body.style.overflow = opening ? 'hidden' : '';
}
function closeSidebar(){
 const sb = document.getElementById('sb');
 const ov = document.getElementById('sb-overlay');
 if(sb) sb.classList.remove('op');
 if(ov) ov.classList.remove('op');
 document.body.style.overflow = '';
}
function route(view,lv,n){
 state.view = view;
 state.levelCode = lv || null;
 state.lessonN = n || null;
 state.activeTab = 'overview';
 state.flashIdx = 0;
 state.flashFlipped = false;
 closeSidebar();
 // reset exercise runtime state
 window.__exDone = new Set();
 window.__uoeDone = new Set();
 exState = {}; matchState = {};
 if(_rtInt){clearInterval(_rtInt); _rtInt=null; _rtStart=null;}
 render();
 window.scrollTo(0,0);
}

// =============================================================
// RENDER
// =============================================================
function render(){
 renderProgramBar();
 renderSidebar();
 renderMain();
 renderHeaderProgress();
}

function renderHeaderProgress(){
 const d = totalDone();
 const pct = Math.round(d/120*100);
 document.getElementById('pm-fill').style.width = pct+'%';
 document.getElementById('pm-pct').textContent = pct+'%';
 document.getElementById('pm-done').textContent = d;
}

function renderProgramBar(){
 const bar = document.getElementById('pbar');
 const home = '<div class="ptab '+(state.view==='home'?'act':'')+'" onclick="route(\'home\')"><i class="fas fa-house"></i>Inicio</div>';
 const tabs = COURSE.levels.map(l => {
  const act = (state.view!=='home' && state.levelCode===l.code) ? 'act' : '';
  const color = LVL_COLORS[l.code];
  return '<div class="ptab '+act+'" onclick="route(\'level\',\''+l.code+'\')">'
       + '<span class="lvl-dot" style="background:'+color+'"></span>'+l.code+'</div>';
 }).join('');
 bar.innerHTML = home + tabs;
}

function renderSidebar(){
 const sb = document.getElementById('sb');
 if(state.view==='home'){
  sb.innerHTML = '<div class="sb-section">'+t('The course')+'</div>'
   + COURSE.levels.map(l=>{
     const d=levelDone(l.code);
     return '<div class="lsn-item" onclick="route(\'level\',\''+l.code+'\')">'
      + '<div class="lsn-n" style="background:'+LVL_COLORS[l.code]+';color:#fff;border-color:'+LVL_COLORS[l.code]+'">'+l.code+'</div>'
      + '<div class="lsn-body"><div class="lsn-ttl">'+l.desc.split(' \u2013 ')[0]+'</div>'
      + '<div class="lsn-sub">'+d+'/20 '+t('lessons')+'</div></div>'
      + (d===20 ? '<i class="fas fa-check-circle lsn-mark"></i>' : '')
      + '</div>';
   }).join('');
  return;
 }
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const d = levelDone(lv.code);
 sb.innerHTML = '<div class="sb-lvl-info" style="border-left-color:'+LVL_COLORS[lv.code]+'">'
  +'<div class="sb-lvl-code" style="color:'+LVL_COLORS[lv.code]+'">'+lv.code+'</div>'
  +'<div class="sb-lvl-desc">'+lv.desc+'</div>'
  +'<div class="sb-lvl-prog">'+t('Progress')+': <b>'+d+'/20</b> \u2022 '+Math.round(d/20*100)+'%</div>'
  +'</div>'
  +'<div class="sb-section">'+t('lessons').replace(/^./,c=>c.toUpperCase())+'</div>'
  + lv.lessons.map(le=>{
    const done = isDone(lv.code,le.n);
    const act = (state.view==='lesson' && state.lessonN===le.n) ? 'act' : '';
    return '<div class="lsn-item '+(done?'done':'')+' '+act+'" onclick="route(\'lesson\',\''+lv.code+'\','+le.n+')">'
     +'<div class="lsn-n">'+le.n+'</div>'
     +'<div class="lsn-body"><div class="lsn-ttl">'+escapeHtml(le.topic)+'</div>'
     +'<div class="lsn-sub">'+escapeHtml(le.grammar.slice(0,50))+(le.grammar.length>50?'\u2026':'')+'</div></div>'
     +(done?'<i class="fas fa-check-circle lsn-mark"></i>':'')
     +'</div>';
   }).join('');
}

function renderMain(){
 const mn = document.getElementById('mn');
 if(state.view==='home') mn.innerHTML = renderHome();
 else if(state.view==='level') mn.innerHTML = renderLevel();
 else if(state.view==='lesson') { mn.innerHTML = renderLesson(); bindLessonHandlers(); }
}

// =============================================================
// HOME VIEW
// =============================================================
function renderHome(){
 const done = totalDone();
 const overallPct = Math.round(done/120*100);
 return `
 <div class="wel">
  <h1>Systems Engineers <span>English Course</span></h1>
  <p class="lead">${t("A course for systems engineers, aligned to CEFR and calibrated against Cambridge, IELTS and TOEFL. 120 lessons. Focus on cybersecurity and emerging technology.")}</p>
  <div class="wel-stats">
   <div class="wel-stat"><div class="wel-stat-v">120</div><div class="wel-stat-l">${t('lessons')}</div></div>
   <div class="wel-stat"><div class="wel-stat-v">6</div><div class="wel-stat-l">CEFR ${t('Levels')}</div></div>
   <div class="wel-stat"><div class="wel-stat-v">16k+</div><div class="wel-stat-l">${t('Vocabulary (total)')}</div></div>
   <div class="wel-stat"><div class="wel-stat-v">${done}</div><div class="wel-stat-l">${t('Completed')}</div></div>
  </div>
 </div>

 <div class="section" style="background:#fff;border-radius:14px;padding:22px 26px;box-shadow:var(--sh);border:1px solid var(--b);margin-bottom:24px">
  <h2 style="display:flex;align-items:center;gap:10px"><i class="fas fa-chart-line" style="color:var(--p)"></i> ${t('Your progress')}</h2>
  <div class="s-sub" style="margin-bottom:14px">${t('Per-level progress and overall course completion.')}</div>
  <div style="margin-bottom:14px">
   <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;font-size:.82rem"><b>${t('Overall')}:</b> <span style="font-weight:700;color:var(--p)">${done}/120 • ${overallPct}%</span></div>
   <div style="height:10px;background:var(--bg);border-radius:5px;overflow:hidden"><div style="height:100%;width:${overallPct}%;background:linear-gradient(90deg,${LVL_COLORS.A1},${LVL_COLORS.B1},${LVL_COLORS.C2});border-radius:5px;transition:width .5s"></div></div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">
   ${COURSE.levels.map(l=>{
    const d = levelDone(l.code); const pct = Math.round(d/20*100); const col = LVL_COLORS[l.code];
    return `<div style="background:var(--bg);border-radius:10px;padding:10px 14px;cursor:pointer" onclick="route('level','${l.code}')">
     <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;font-size:.78rem">
      <b style="color:${col}">${l.code}</b>
      <span style="color:var(--m);font-weight:600">${d}/20 • ${pct}%</span>
     </div>
     <div style="height:6px;background:#fff;border-radius:3px;overflow:hidden">
      <div style="height:100%;width:${pct}%;background:${col};border-radius:3px;transition:width .5s"></div>
     </div>
    </div>`;
   }).join('')}
  </div>
 </div>

 <div class="section">
  <h2>${t('Choose your level')}</h2>
  <div class="s-sub">${t('Start with A1 or jump to your current level.')}</div>
  <div class="lvl-grid">
  ${COURSE.levels.map(l=>{
   const d = levelDone(l.code);
   const pct = Math.round(d/20*100);
   const eq = COURSE.cefr_equiv.find(e=>e.cefr===l.code);
   const qt = COURSE.quotas.find(q=>q.cefr===l.code);
   const col = LVL_COLORS[l.code];
   return `<div class="lvl-card" onclick="route('level','${l.code}')">
    <div class="lvl-topline" style="background:${col}"></div>
    <div class="lvl-head">
     <div class="lvl-badge" style="background:${col}"><i class="fas fa-${LVL_ICONS[l.code]}"></i></div>
     <div><div class="lvl-title">${l.code}</div><div class="lvl-sub">${eq.cambridge.split(' (')[0]}</div></div>
    </div>
    <div class="lvl-chips">
     <span class="chip">IELTS ${eq.ielts}</span>
     <span class="chip g">TOEFL ${eq.toefl}</span>
     <span class="chip o">${qt.vocab_total} w</span>
    </div>
    <div class="lvl-desc">${eq.profile} \u2022 ${qt.writing} w ${t('per writing task')} \u2022 ${t('Readings')} ${qt.reading} w.</div>
    <div class="lvl-prog">
     <div class="lvl-prog-bar"><div class="lvl-prog-fill" style="width:${pct}%;background:${col}"></div></div>
     <div class="lvl-prog-tx">${d}/20</div>
    </div>
   </div>`;
  }).join('')}
  </div>
 </div>

 <div class="section">
  <h2>${t('CEFR \u2013 Cambridge \u2013 IELTS \u2013 TOEFL equivalences')}</h2>
  <div class="s-sub">${t('Ranges are indicative. Cambridge and TOEFL are multilevel exams.')}</div>
  <table class="tbl">
   <thead><tr><th>CEFR</th><th>${t('Cambridge')}</th><th>${t('IELTS')}</th><th>${t('TOEFL iBT')}</th><th>${t('Professional IT profile')}</th></tr></thead>
   <tbody>
   ${COURSE.cefr_equiv.map(e=>`<tr>
     <td><span class="lvl-pill" style="background:${LVL_COLORS[e.cefr]}">${e.cefr}</span></td>
     <td>${e.cambridge}</td><td>${e.ielts}</td><td>${e.toefl}</td><td>${e.profile}</td>
    </tr>`).join('')}
   </tbody>
  </table>
 </div>

 <div class="section">
  <h2>${t('Quantitative quotas per level')}</h2>
  <div class="s-sub">${t('Accumulated vocabulary, reading length, writing words and listening hours.')}</div>
  <table class="tbl">
   <thead><tr><th>${t('Level')}</th><th>Vocab total</th><th>+New</th><th>Writing (words)</th><th>Reading (words)</th><th>${t('Speed')} (wpm)</th><th>Listening (h)</th></tr></thead>
   <tbody>
   ${COURSE.quotas.map(q=>`<tr>
     <td><span class="lvl-pill" style="background:${LVL_COLORS[q.cefr]}">${q.cefr}</span></td>
     <td>${q.vocab_total}</td><td>+${q.vocab_new}</td><td>${q.writing}</td>
     <td>${q.reading}</td><td>${q.wpm}</td><td>${q.listen_h} h</td>
    </tr>`).join('')}
   </tbody>
  </table>
 </div>

 <div class="section">
  <h2>${t('Free-use audio sources')}</h2>
  <div class="s-sub">${t('Educational-use licensed domains. Verify each specific resource.')}</div>
  <div class="audio-pool">
  ${COURSE.audio_sources.map(a=>{
   return `<div class="ap-card">
    <div class="ap-name">${a.name}</div>
    <div class="ap-dom">${a.domain}</div>
    <div style="margin-top:6px;font-size:.78rem;color:var(--m)">${a.content}</div>
    <span class="ap-lic">${a.license}</span>
    <span class="ap-lic" style="margin-left:4px">${a.levels}</span>
   </div>`;
  }).join('')}
  </div>
 </div>`;
}

// =============================================================
// LEVEL VIEW
// =============================================================
function renderLevel(){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const eq = COURSE.cefr_equiv.find(e=>e.cefr===lv.code);
 const qt = COURSE.quotas.find(q=>q.cefr===lv.code);
 const d = levelDone(lv.code);
 const col = LVL_COLORS[lv.code];
 return `
 <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;flex-wrap:wrap">
  <button class="btn sec" onclick="route('home')" style="padding:7px 14px"><i class="fas fa-arrow-left"></i> ${t('Back to home')}</button>
  <div class="crumb" style="margin:0"><a onclick="route('home')">${t('Home')}</a> <i class="fas fa-chevron-right" style="font-size:.65rem"></i> ${t('Level')} ${lv.code}</div>
 </div>
 <div class="lvl-overview" style="background:linear-gradient(135deg,${col},#1E40AF)">
  <h2>${t('Level')} ${lv.code}</h2>
  <div class="lo-sub">${lv.desc}</div>
  <div class="lo-stats">
   <div class="lo-stat"><b>${qt.vocab_total}</b><span>${t('Vocabulary')}</span></div>
   <div class="lo-stat"><b>${qt.writing}</b><span>Writing (w/task)</span></div>
   <div class="lo-stat"><b>${qt.reading}</b><span>Reading (w/text)</span></div>
   <div class="lo-stat"><b>${qt.listen_h} h</b><span>Listening</span></div>
   <div class="lo-stat"><b>${eq.cambridge.split(' (')[0]}</b><span>Cambridge</span></div>
   <div class="lo-stat"><b>${d}/20</b><span>${t('Progress')}</span></div>
  </div>
 </div>

 <div class="section">
  <h2>${t('Lessons in level')} ${lv.code}</h2>
  <div class="s-sub">${t('20 lessons of 90 minutes each, in 4 modules: Foundations (1\u20135) \u2022 Core IT/ESP (6\u201310) \u2022 Cybersecurity (11\u201315) \u2022 Emerging Tech + Exam Prep (16\u201320).')}</div>
  <div class="lesson-grid">
  ${lv.lessons.map(le=>{
    const done = isDone(lv.code,le.n);
    const mod = le.n<=5?t('Foundations'):le.n<=10?t('Core IT'):le.n<=15?t('Cybersecurity'):t('Emerging + Exam');
    const pilot = le.has_content ? '<span class="lc-tag" style="background:#DCFCE7;color:#166534;border-color:#86EFAC"><i class="fas fa-circle-check"></i> '+t('Pilot content')+'</span>' : '';
    return `<div class="lesson-card ${done?'done':''}" onclick="route('lesson','${lv.code}',${le.n})">
     <div class="lc-n">${t('Class')} ${le.n} \u2022 ${mod}</div>
     <div class="lc-t">${escapeHtml(le.topic)}</div>
     <div class="lc-tags">
      ${pilot}
      <span class="lc-tag"><i class="fas fa-book"></i> ${escapeHtml(le.grammar.slice(0,30))}${le.grammar.length>30?'\u2026':''}</span>
      <span class="lc-tag"><i class="fas fa-pen"></i> ${escapeHtml(le.writing)}</span>
     </div>
    </div>`;
   }).join('')}
  </div>
 </div>`;
}

// =============================================================
// LESSON VIEW
// =============================================================
function renderLesson(){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 const done = isDone(lv.code,le.n);
 const col = LVL_COLORS[lv.code];
 const vocabCount = le.vocab_list.length;

 const lvDone = levelDone(lv.code);
 const lvPct = Math.round(lvDone/20*100);
 return `
 <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;flex-wrap:wrap">
  <button class="btn sec" onclick="route('level','${lv.code}')" style="padding:7px 14px"><i class="fas fa-arrow-left"></i> ${t('Back to')} ${lv.code}</button>
  <button class="btn sec" onclick="route('home')" style="padding:7px 14px"><i class="fas fa-house"></i> ${t('Home')}</button>
  <div class="crumb" style="margin:0;flex:1">
   <a onclick="route('home')">${t('Home')}</a>
   <i class="fas fa-chevron-right" style="font-size:.65rem"></i>
   <a onclick="route('level','${lv.code}')">${t('Level')} ${lv.code}</a>
   <i class="fas fa-chevron-right" style="font-size:.65rem"></i>
   ${t('Class')} ${le.n}
  </div>
 </div>

 <div style="background:var(--w);border:1px solid var(--b);border-radius:10px;padding:8px 14px;margin-bottom:14px;display:flex;align-items:center;gap:12px;font-size:.78rem">
  <span style="font-weight:600;color:var(--m)">${t('Level')} ${lv.code} ${t('progress')}:</span>
  <div style="flex:1;height:6px;background:var(--bg);border-radius:3px;overflow:hidden">
   <div style="height:100%;width:${lvPct}%;background:${col};border-radius:3px;transition:width .5s"></div>
  </div>
  <span style="font-weight:700;color:${col};font-variant-numeric:tabular-nums">${lvDone}/20 • ${lvPct}%</span>
 </div>

 <div class="lhd">
  <div class="lh-chip" style="background:${col}"><i class="fas fa-${LVL_ICONS[lv.code]}"></i> ${lv.code} \u2022 ${t('Class')} ${le.n}/20</div>
  <h1>${escapeHtml(le.topic)}</h1>
  <div class="lh-sub">${escapeHtml(le.grammar)}</div>
 </div>

 <div class="tabs">
  <div class="tab ${state.activeTab==='overview'?'act':''}" onclick="setTab('overview')"><i class="fas fa-circle-info"></i> ${t('Overview')}</div>
  <div class="tab ${state.activeTab==='lesson'?'act':''}" onclick="setTab('lesson')"><i class="fas fa-chalkboard-user"></i> ${t('Lesson')}</div>
  <div class="tab ${state.activeTab==='uoe'?'act':''}" onclick="setTab('uoe')"><i class="fas fa-spell-check"></i> ${t('Use of English')}${le.use_of_english?' ('+le.use_of_english.length+')':''}</div>
  <div class="tab ${state.activeTab==='vocab'?'act':''}" onclick="setTab('vocab')"><i class="fas fa-book-bookmark"></i> ${t('Vocabulary')} (${vocabCount})</div>
  <div class="tab ${state.activeTab==='read'?'act':''}" onclick="setTab('read')"><i class="fas fa-eye"></i> ${t('Reading')}</div>
  <div class="tab ${state.activeTab==='listen'?'act':''}" onclick="setTab('listen')"><i class="fas fa-headphones"></i> ${t('Listening')}</div>
  <div class="tab ${state.activeTab==='write'?'act':''}" onclick="setTab('write')"><i class="fas fa-pen-fancy"></i> ${t('Writing')}</div>
  <div class="tab ${state.activeTab==='cyber'?'act':''}" onclick="setTab('cyber')"><i class="fas fa-shield-halved"></i> ${t('Cyber angle')}</div>
 </div>

 <!-- PANELS -->
 <div id="panel-overview" class="panel ${state.activeTab==='overview'?'act':''}">
  ${renderOverview(lv,le)}
 </div>
 <div id="panel-lesson" class="panel ${state.activeTab==='lesson'?'act':''}">
  ${renderLessonNotes(lv,le)}
 </div>
 <div id="panel-uoe" class="panel ${state.activeTab==='uoe'?'act':''}">
  ${renderUoE(lv,le)}
 </div>
 <div id="panel-vocab" class="panel ${state.activeTab==='vocab'?'act':''}">
  ${renderVocab(lv,le)}
 </div>
 <div id="panel-read" class="panel ${state.activeTab==='read'?'act':''}">
  ${renderReading(lv,le)}
 </div>
 <div id="panel-listen" class="panel ${state.activeTab==='listen'?'act':''}">
  ${renderListening(lv,le)}
 </div>
 <div id="panel-write" class="panel ${state.activeTab==='write'?'act':''}">
  ${renderWriting(lv,le)}
 </div>
 <div id="panel-cyber" class="panel ${state.activeTab==='cyber'?'act':''}">
  ${renderCyber(lv,le)}
 </div>

 <div class="lesson-nav">
  ${le.n>1 ? `<button class="btn sec" onclick="route('lesson','${lv.code}',${le.n-1})"><i class="fas fa-chevron-left"></i> ${t('Previous')}</button>` : `<button class="btn sec" onclick="route('level','${lv.code}')"><i class="fas fa-list"></i> ${t('View lessons')}</button>`}
  <button class="btn ${done?'ok':'pri'}" onclick="toggleDone()">
   <i class="fas fa-${done?'check-double':'check'}"></i> ${done?t('Completed'):t('Mark as completed')}
  </button>
  ${le.n<20 ? `<button class="btn pri" onclick="route('lesson','${lv.code}',${le.n+1})">${t('Next')} <i class="fas fa-chevron-right"></i></button>` : (findNextLevel(lv.code) ? `<button class="btn ok" onclick="route('level','${findNextLevel(lv.code)}')">${t('Next level')} <i class="fas fa-chevron-right"></i></button>` : `<button class="btn ok" onclick="route('home')"><i class="fas fa-trophy"></i> ${t('Finish course')}</button>`)}
 </div>`;
}

function findNextLevel(code){
 const i = COURSE.levels.findIndex(l=>l.code===code);
 return i>=0 && i<COURSE.levels.length-1 ? COURSE.levels[i+1].code : null;
}

// ---------- LESSON NOTES (teaching content) ----------
function renderLessonNotes(lv,le){
 const n = le.lesson_notes;
 if(!n){
  return `<div class="ln-pending">
   <i class="fas fa-triangle-exclamation"></i>
   <div><b>${t('Teaching notes not yet included for this lesson.')}</b><br>
   ${t('The Overview tab summarises the grammar target and Use of English contains the practice items.')}</div>
  </div>`;
 }
 const warmup = `
 <div class="ln-warmup">
  <div class="lnw-label"><i class="fas fa-lightbulb"></i> ${t('Warm-up')}</div>
  <p>${escapeHtml(n.warmup)}</p>
 </div>`;

 let grammar = '';
 if(n.grammar){
  const g = n.grammar;
  const tableHtml = g.table ? `
   <table class="ln-table">
    <thead><tr>${g.table.head.map(h=>'<th>'+escapeHtml(h)+'</th>').join('')}</tr></thead>
    <tbody>${g.table.rows.map(r=>'<tr>'+r.map(c=>'<td>'+escapeHtml(c)+'</td>').join('')+'</tr>').join('')}</tbody>
   </table>` : '';
  const exHtml = g.examples ? `
   <div class="ln-examples">
   ${g.examples.map(e=>`<div class="ln-ex"><div class="ln-ex-en">${escapeHtml(e.en)}</div>${e.note?'<div class="ln-ex-note">'+escapeHtml(e.note)+'</div>':''}</div>`).join('')}
   </div>` : '';
  grammar = `
  <div class="ln-grammar">
   <div class="lng-title"><i class="fas fa-book-open"></i> ${escapeHtml(g.title||t('Grammar focus'))}</div>
   <div class="lng-rule">${escapeHtml(g.rule||'')}</div>
   ${tableHtml}
   ${exHtml}
  </div>`;
 }

 const phrases = n.phrases && n.phrases.length ? `
 <div class="ln-section">
  <h3><i class="fas fa-quote-right"></i> ${t('Key phrases')}</h3>
  <div class="ln-phrases">
  ${n.phrases.map(p=>`<div class="ln-phrase"><div class="lnp-ph">${escapeHtml(p.phrase)}</div><div class="lnp-use">${escapeHtml(p.use||'')}</div></div>`).join('')}
  </div>
 </div>` : '';

 const mistakes = n.mistakes && n.mistakes.length ? `
 <div class="ln-section">
  <h3><i class="fas fa-circle-exclamation"></i> ${t('Common mistakes')}</h3>
  <div class="ln-mistakes">
  ${n.mistakes.map(m=>`<div class="ln-mist">
   <div class="ln-mist-wr">${escapeHtml(m.wrong)}</div>
   <div class="ln-mist-ri">${escapeHtml(m.right)}</div>
   <div class="ln-mist-why">${escapeHtml(m.why||'')}</div>
  </div>`).join('')}
  </div>
 </div>` : '';

 const tip = n.tip ? `
 <div class="ln-tip">
  <i class="fas fa-lightbulb"></i>
  <div class="ln-tip-content">
   <div class="lnt-label">${t('Pro tip')}</div>
   <p>${escapeHtml(n.tip)}</p>
  </div>
 </div>` : '';

 const nextCta = `
 <div class="ln-next">
  <div class="lnn-label">${t('Ready to practise?')} <b>${t('Go to')} \u201C${t('Use of English')}\u201D ${t('for the exercises.')}</b></div>
  <button onclick="setTab('uoe')"><i class="fas fa-arrow-right"></i> ${t('Use of English')}</button>
 </div>`;

 return warmup + grammar + phrases + mistakes + tip + nextCta;
}

// ---------- USE OF ENGLISH ----------
function renderUoE(lv,le){
 // Cambridge UoE guide by level
 const guide = {
  A1: {title: t('Use of English') + " \u2013 A1 / Pre-KET", parts: ["Basic grammar in context","Short sentence completion","Word recognition"]},
  A2: {title: t('Use of English') + " \u2013 A2 / KET", parts: ["Sentence completion","Simple transformations","Basic word formation"]},
  B1: {title: t('Use of English') + " \u2013 B1 / PET", parts: ["Multiple-choice cloze","Open cloze","Word formation"]},
  B2: {title: t('Use of English') + " \u2013 B2 / FCE", parts: ["Part 1 \u2013 MCQ cloze (8Q)","Part 2 \u2013 Open cloze (8Q)","Part 3 \u2013 Word formation (8Q)","Part 4 \u2013 Key word transformation (6Q)"]},
  C1: {title: t('Use of English') + " \u2013 C1 / CAE", parts: ["Part 1 \u2013 MCQ cloze","Part 2 \u2013 Open cloze","Part 3 \u2013 Word formation","Part 4 \u2013 Key word transformation (3\u20135 words)"]},
  C2: {title: t('Use of English') + " \u2013 C2 / CPE", parts: ["Part 1 \u2013 MCQ cloze","Part 2 \u2013 Open cloze","Part 3 \u2013 Word formation","Part 4 \u2013 Key word transformation (3\u20138 words)"]},
 };
 const g = guide[lv.code] || guide.B2;

 const header = `
 <div class="uoe-intro">
  <h3><i class="fas fa-spell-check"></i> ${g.title}</h3>
  <p>${escapeHtml(le.grammar)}</p>
  <div class="uoe-parts">${g.parts.map(p=>'<span class="uoe-part">'+escapeHtml(p)+'</span>').join('')}</div>
 </div>`;

 if(!le.use_of_english || !le.use_of_english.length){
  return header + `
  <div class="content-pending">
   <i class="fas fa-triangle-exclamation"></i>
   <div><b>Use of English exercises not yet included in the pilot for this lesson.</b><br>
   Coming soon. Use the Overview tab for the target grammar summary: <i>${escapeHtml(le.grammar)}</i>.</div>
  </div>`;
 }

 return header + `
  <div class="ex-progress">
   <div>${t('Comprehension exercises').replace('Comprehension','Use of English').replace('Ejercicios de comprensi\u00f3n','Ejercicios Use of English')}: <b id="uoe-done-count">0</b> / ${le.use_of_english.length}</div>
   <div class="ex-score-pill g" id="uoe-score-pill">${t('Not attempted yet')}</div>
  </div>
  ${le.use_of_english.map((ex,i)=>renderExercise(ex,i,'uoe')).join('')}
  <div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap">
   <button class="btn pri" onclick="checkAllUoE()"><i class="fas fa-check-double"></i> ${t('Check all')}</button>
   <button class="btn sec" onclick="resetAllUoE()"><i class="fas fa-rotate-left"></i> ${t('Restart')}</button>
  </div>`;
}

function checkAllUoE(){
 const le = getLesson();
 if(!le.use_of_english) return;
 le.use_of_english.forEach((ex,i)=>dispatchCheck(ex,i,'uoe'));
}
function resetAllUoE(){
 const le = getLesson();
 if(!le.use_of_english) return;
 le.use_of_english.forEach((_,i)=>resetEx(i,'uoe'));
 window.__uoeDone = new Set();
 updateUoEProgress();
}
function getLesson(){
 return COURSE.levels.find(l=>l.code===state.levelCode).lessons.find(x=>x.n===state.lessonN);
}
function updateUoEProgress(){
 const le = getLesson();
 if(!le.use_of_english) return;
 const done = (window.__uoeDone||new Set()).size;
 const cntEl = document.getElementById('uoe-done-count'); if(cntEl) cntEl.textContent = done;
 const pill = document.getElementById('uoe-score-pill');
 if(pill){
  const pct = done/le.use_of_english.length;
  pill.className='ex-score-pill '+(pct>=0.8?'g':pct>=0.4?'y':'r');
  pill.textContent = done+'/'+le.use_of_english.length;
 }
}
function dispatchCheck(ex,i,scope){
 if(ex.type==='mcq' || ex.type==='mc_cloze') checkMCQ(i,scope);
 else if(ex.type==='tfng') checkTFNG(i,scope);
 else if(ex.type==='gap' || ex.type==='cloze' || ex.type==='word_form') checkGap(i,scope);
 else if(ex.type==='key_word') checkKeyWord(i,scope);
 else if(ex.type==='match') checkMatch(i,scope);
 else if(ex.type==='short') revealModel(i,scope);
}

// ---------- OVERVIEW ----------
function renderOverview(lv,le){
 const previewWords = (le.vocab_list||[]).slice(0,12);
 const moreCount = Math.max(0, (le.vocab_list||[]).length - 12);
 return `
 <div class="callout">
  <h4>${t('Lesson objective')}</h4>
  ${t('By the end of this session (90 min), the learner will use')} <b>${escapeHtml(le.grammar)}</b> ${t('applied to the topic')} "<b>${escapeHtml(le.topic)}</b>", ${t('recognise and use the')} ${le.vocab_list.length} ${t('target words, and produce a written task of')} <b>${escapeHtml(le.writing)}</b>.
 </div>
 <div class="info-grid">
  <div class="info-card">
   <h4><i class="fas fa-gear"></i> ${t('Use of English')}</h4><p>${escapeHtml(le.grammar)}</p>
  </div>
  <div class="info-card">
   <h4><i class="fas fa-book-open"></i> ${t('Reading task')}</h4><p>${escapeHtml(le.reading)}</p>
  </div>
  <div class="info-card">
   <h4><i class="fas fa-headphones"></i> ${t('Listening task')}</h4><p>${escapeHtml(le.listening)}</p>
  </div>
  <div class="info-card">
   <h4><i class="fas fa-pen"></i> ${t('Writing target')}</h4><p>${escapeHtml(le.writing)}</p>
  </div>
 </div>
 <div class="info-card" style="margin-bottom:14px">
  <h4><i class="fas fa-book-bookmark"></i> ${t('Vocabulary preview')} (${le.vocab_list.length} ${t('words')})</h4>
  <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:8px">
   ${previewWords.map(w=>`<span class="v-chip" onclick="setTab('vocab');setTimeout(()=>openPron('${escapeJs(w)}'),200)" style="cursor:pointer">${escapeHtml(w)} <i class="fas fa-volume-high"></i></span>`).join('')}
   ${moreCount?`<span class="v-chip" onclick="setTab('vocab')" style="background:var(--p);color:#fff;border-color:var(--p);cursor:pointer">+${moreCount} ${t('more')} →</span>`:''}
  </div>
 </div>
 <div class="callout cyber">
  <h4><i class="fas fa-shield-halved"></i> ${t('Cybersecurity / emerging tech angle')}</h4>
  <div style="font-size:.95rem;line-height:1.65">${escapeHtml(le.cyber)}</div>
 </div>
 <div style="background:linear-gradient(135deg,#065F46,#047857);color:#fff;padding:14px 18px;border-radius:12px;margin-top:14px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
  <div style="font-size:.88rem">${t('Recommended path')}: <b>${t('Lesson')} → ${t('Use of English')} → ${t('Vocabulary')} → ${t('Reading')} → ${t('Writing')}</b></div>
  <button onclick="setTab('lesson')" style="background:#fff;color:#065F46;border:none;padding:8px 16px;border-radius:8px;font-weight:700;cursor:pointer;font-family:inherit;display:inline-flex;align-items:center;gap:6px"><i class="fas fa-chalkboard-user"></i> ${t('Start with Lesson')}</button>
 </div>`;
}

// ---------- VOCABULARY ----------
function renderVocab(lv,le){
 const key = lessonKey(lv.code,le.n);
 const known = (state.vocab[key]||{});
 const knownCount = Object.values(known).filter(v=>v==='known').length;
 return `
 <div class="vocab-meta">
  <div class="vm-stat">${t('Target vocabulary')}: <b>${le.vocab_list.length}</b> \u2022 ${t('Mastered')}: <b style="color:var(--ok)">${knownCount}</b></div>
  <div class="vocab-ctrls">
   <button class="v-mode-btn act" onclick="setVocabMode('list')" id="vm-list"><i class="fas fa-list"></i> ${t('List')}</button>
   <button class="v-mode-btn" onclick="setVocabMode('flash')" id="vm-flash"><i class="fas fa-bolt"></i> ${t('Flashcards')}</button>
  </div>
 </div>

 <div class="callout" style="font-size:.82rem;padding:10px 14px">
  <i class="fas fa-volume-high" style="color:var(--p)"></i> <b>${t('Click a word to hear its pronunciation and see the IPA symbols.')}</b>
 </div>

 <div id="vocab-list-view">
  <div class="vocab-list">
   ${le.vocab_list.map((w,i)=>{
    const k = known[w]==='known';
    return `<div class="v-chip ${k?'known':''}" onclick="openPron('${escapeJs(w)}')" data-w="${escapeAttr(w)}" title="${t('listen').toUpperCase()}">
     <span>${escapeHtml(w)}</span>
     <i class="fas fa-volume-high"></i>
    </div>`;
   }).join('')}
  </div>
  <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:10px">
   <button class="btn pri" onclick="startVocabQuiz()"><i class="fas fa-graduation-cap"></i> ${t('Practise vocabulary')}</button>
   <button class="btn sec" onclick="markAllKnown()"><i class="fas fa-check-double"></i> ${t('Mark all as known')}</button>
   <button class="btn sec" onclick="resetVocab()"><i class="fas fa-rotate-left"></i> ${t('Restart')}</button>
  </div>
  <div id="vocab-quiz-zone" style="margin-top:18px"></div>
 </div>

 <div id="vocab-flash-view" style="display:none">
  <div class="flashcard-zone">
   <div class="fc-counter" id="fc-counter">1 / ${le.vocab_list.length}</div>
   <div class="flashcard" id="fc-card" onclick="flipCard()">
    <div class="fc-w" id="fc-word">\u2014</div>
    <div class="fc-prompt" id="fc-prompt"></div>
    <div class="fc-flip">${t('Click the card to flip')}</div>
   </div>
   <div class="fc-actions">
    <button class="fc-btn" onclick="prevCard()"><i class="fas fa-chevron-left"></i></button>
    <button class="fc-btn" onclick="speakFlash()" title="${t('listen')}"><i class="fas fa-volume-high"></i></button>
    <button class="fc-btn sk" onclick="markCard('review')"><i class="fas fa-rotate"></i> ${t('Review')}</button>
    <button class="fc-btn ok" onclick="markCard('known')"><i class="fas fa-check"></i> ${t('I know it')}</button>
    <button class="fc-btn" onclick="nextCard()"><i class="fas fa-chevron-right"></i></button>
   </div>
  </div>
 </div>`;
}

// ---------- PRONUNCIATION MODAL ----------
let _currentPronWord = null;
let _currentPronVoice = null;
function openPron(word){
 _currentPronWord = word;
 const modal = document.getElementById('pron-overlay');
 modal.classList.add('sh');
 document.getElementById('pron-word').textContent = word;
 document.getElementById('pron-ipa').textContent = t('Loading dictionary\u2026');
 document.getElementById('pron-ipa').classList.add('empty');
 document.getElementById('pron-respell').textContent = '';
 document.getElementById('pron-body').innerHTML = '<div class="pron-loading"><i class="fas fa-spinner fa-spin"></i> '+t('Loading dictionary\u2026')+'</div>';
 // reset translation panel
 const trEl = document.getElementById('pron-translation');
 if(trEl){trEl.style.display='none'; document.getElementById('pron-es-text').textContent='\u2014';}
 renderVoiceButtons();
 loadDictEntry(word);
}

// ---------- CURATED IT/CYBER ES DICTIONARY (highest priority) ----------
const VOCAB_ES = {
 // Hardware
 "computer":"computadora / ordenador","laptop":"laptop / port\u00e1til","desktop":"computadora de escritorio",
 "server":"servidor","servers":"servidores","monitor":"monitor","screen":"pantalla","keyboard":"teclado",
 "mouse":"rat\u00f3n / mouse","webcam":"c\u00e1mara web","speaker":"parlante / altavoz","microphone":"micr\u00f3fono",
 "headset":"aud\u00edfonos / cascos","cable":"cable","cables":"cables","port":"puerto","ports":"puertos",
 "USB":"USB","HDMI":"HDMI","CPU":"CPU / procesador","RAM":"RAM / memoria","SSD":"SSD",
 "hard disk":"disco duro","disk":"disco","drive":"unidad","fan":"ventilador","battery":"bater\u00eda",
 "charger":"cargador","plug":"enchufe","tower":"torre","case":"caja / chasis","motherboard":"placa madre",
 "chip":"chip","slot":"ranura","rack":"rack / bastidor","data center":"centro de datos","router":"router / enrutador",
 "modem":"m\u00f3dem","switch":"switch","printer":"impresora","scanner":"esc\u00e1ner",
 // Software / OS
 "software":"software / programa","program":"programa","programs":"programas","app":"app / aplicaci\u00f3n","apps":"apps / aplicaciones",
 "application":"aplicaci\u00f3n","operating system":"sistema operativo","Windows":"Windows","Linux":"Linux","macOS":"macOS",
 "Android":"Android","iOS":"iOS","kernel":"kernel / n\u00facleo","driver":"controlador / driver","update":"actualizaci\u00f3n",
 "updates":"actualizaciones","upgrade":"mejora / actualizaci\u00f3n mayor","patch":"parche","patches":"parches",
 "install":"instalar","installer":"instalador","uninstall":"desinstalar","reboot":"reiniciar","restart":"reiniciar",
 "shutdown":"apagar","launch":"iniciar / lanzar","run":"ejecutar","close":"cerrar","open":"abrir",
 "save":"guardar","delete":"eliminar","edit":"editar","copy":"copiar","paste":"pegar","cut":"cortar",
 "select":"seleccionar","menu":"men\u00fa","icon":"\u00edcono / icono","window":"ventana","tab":"pesta\u00f1a",
 "settings":"configuraci\u00f3n","preferences":"preferencias","extension":"extensi\u00f3n","plugin":"complemento",
 // Files
 "file":"archivo","files":"archivos","folder":"carpeta","folders":"carpetas","document":"documento",
 "image":"imagen","photo":"foto","video":"video","audio":"audio","backup":"copia de seguridad / respaldo",
 "backups":"copias de seguridad","restore":"restaurar","recovery":"recuperaci\u00f3n","archive":"archivo / archivar",
 // Network
 "network":"red","networks":"redes","internet":"internet","Wi-Fi":"Wi-Fi","wireless":"inal\u00e1mbrico",
 "wired":"cableado","ethernet":"ethernet","LAN":"LAN / red local","WAN":"WAN","VPN":"VPN",
 "IP address":"direcci\u00f3n IP","domain":"dominio","DNS":"DNS","HTTP":"HTTP","HTTPS":"HTTPS",
 "TCP":"TCP","UDP":"UDP","TLS":"TLS","SSL":"SSL","port":"puerto",
 "protocol":"protocolo","handshake":"negociaci\u00f3n / handshake","packet":"paquete","traffic":"tr\u00e1fico",
 "bandwidth":"ancho de banda","latency":"latencia","throughput":"rendimiento","connection":"conexi\u00f3n",
 "connect":"conectar","disconnect":"desconectar","sign in":"iniciar sesi\u00f3n","sign out":"cerrar sesi\u00f3n",
 "log in":"iniciar sesi\u00f3n","log out":"cerrar sesi\u00f3n","login":"inicio de sesi\u00f3n","upload":"subir",
 "download":"descargar","stream":"transmitir","streaming":"transmisi\u00f3n",
 // Security
 "security":"seguridad","cybersecurity":"ciberseguridad","threat":"amenaza","threats":"amenazas",
 "risk":"riesgo","risks":"riesgos","vulnerability":"vulnerabilidad","vulnerabilities":"vulnerabilidades",
 "exploit":"explotar / exploit","attack":"ataque","attacks":"ataques","attacker":"atacante",
 "hacker":"hacker","defender":"defensor","defence":"defensa","defense":"defensa",
 "protect":"proteger","prevent":"prevenir","detect":"detectar","detection":"detecci\u00f3n","respond":"responder",
 "response":"respuesta","recover":"recuperar","recovery":"recuperaci\u00f3n","mitigate":"mitigar","mitigation":"mitigaci\u00f3n",
 "encrypt":"cifrar","encryption":"cifrado / encriptaci\u00f3n","decrypt":"descifrar","decryption":"descifrado",
 "hash":"hash","key":"clave","keys":"claves","public key":"clave p\u00fablica","private key":"clave privada",
 "certificate":"certificado","certificates":"certificados","signature":"firma","sign":"firmar",
 "password":"contrase\u00f1a","passwords":"contrase\u00f1as","passphrase":"frase contrase\u00f1a",
 "credential":"credencial","credentials":"credenciales","authentication":"autenticaci\u00f3n","authenticate":"autenticar",
 "authorisation":"autorizaci\u00f3n","authorization":"autorizaci\u00f3n","authorise":"autorizar","access":"acceso",
 "permission":"permiso","permissions":"permisos","privilege":"privilegio","privileges":"privilegios",
 "role":"rol","user":"usuario","users":"usuarios","admin":"administrador","administrator":"administrador",
 "account":"cuenta","accounts":"cuentas","identity":"identidad","biometric":"biom\u00e9trico",
 "fingerprint":"huella dactilar","face":"rostro / cara","2FA":"2FA / doble factor","MFA":"MFA / m\u00faltiple factor",
 "OTP":"OTP / contrase\u00f1a de un solo uso","TOTP":"TOTP","passkey":"passkey / clave de acceso",
 // Threats
 "malware":"malware / programa malicioso","virus":"virus","worm":"gusano","trojan":"troyano","rootkit":"rootkit",
 "spyware":"spyware / software esp\u00eda","keylogger":"keylogger","ransomware":"ransomware","wiper":"wiper",
 "phishing":"phishing","spear phishing":"phishing dirigido","smishing":"smishing","vishing":"vishing",
 "spam":"spam","botnet":"botnet","backdoor":"puerta trasera","payload":"carga \u00fatil","dropper":"dropper",
 "exfiltrate":"exfiltrar","exfiltration":"exfiltraci\u00f3n","reconnaissance":"reconocimiento","persistence":"persistencia",
 "lateral movement":"movimiento lateral","privilege escalation":"escalaci\u00f3n de privilegios",
 "kill chain":"kill chain","TTP":"TTPs / t\u00e1cticas t\u00e9cnicas y procedimientos","IOC":"IOC / indicador de compromiso",
 // Defence
 "firewall":"firewall / cortafuegos","antivirus":"antivirus","EDR":"EDR / detecci\u00f3n y respuesta de endpoints",
 "SIEM":"SIEM","SOC":"SOC / centro de operaciones de seguridad","SOAR":"SOAR","WAF":"WAF",
 "IDS":"IDS / sistema de detecci\u00f3n","IPS":"IPS / sistema de prevenci\u00f3n","DLP":"DLP / prevenci\u00f3n de fuga",
 "VPN":"VPN","ZTNA":"ZTNA / acceso de confianza cero","CASB":"CASB","CSPM":"CSPM",
 "audit":"auditor\u00eda","audits":"auditor\u00edas","log":"registro / log","logs":"registros / logs","alert":"alerta",
 "alerts":"alertas","alarm":"alarma","monitor":"monitorear","monitoring":"monitoreo","incident":"incidente",
 "breach":"brecha / vulneraci\u00f3n","compromise":"compromiso","containment":"contenci\u00f3n","eradication":"erradicaci\u00f3n",
 "playbook":"playbook / manual de respuesta","runbook":"runbook / manual operativo","CSIRT":"CSIRT",
 "MTTD":"MTTD","MTTR":"MTTR","SLA":"SLA","SLI":"SLI","SLO":"SLO","KPI":"KPI",
 // Software dev
 "code":"c\u00f3digo","coding":"programaci\u00f3n / codificaci\u00f3n","programming":"programaci\u00f3n","developer":"desarrollador",
 "developers":"desarrolladores","engineer":"ingeniero","engineers":"ingenieros","analyst":"analista",
 "tester":"tester / probador","architect":"arquitecto","manager":"gerente / director",
 "team":"equipo","sprint":"sprint","backlog":"backlog","epic":"\u00e9pica","story":"historia",
 "task":"tarea","ticket":"ticket","bug":"error / bug","fix":"corregir / arreglar","debug":"depurar",
 "deploy":"desplegar","deployment":"despliegue","release":"versi\u00f3n / lanzamiento","build":"compilar / build",
 "test":"prueba","tests":"pruebas","testing":"pruebas / testing","unit test":"prueba unitaria",
 "integration":"integraci\u00f3n","CI":"CI / integraci\u00f3n continua","CD":"CD / entrega continua","pipeline":"pipeline / canalizaci\u00f3n",
 "version":"versi\u00f3n","versions":"versiones","commit":"commit","branch":"rama","merge":"fusionar / merge",
 "pull request":"pull request","review":"revisi\u00f3n","retrospective":"retrospectiva","standup":"standup / reuni\u00f3n diaria",
 // Cloud / data
 "cloud":"nube","public cloud":"nube p\u00fablica","private cloud":"nube privada","hybrid cloud":"nube h\u00edbrida",
 "AWS":"AWS","Azure":"Azure","GCP":"GCP / Google Cloud","IaaS":"IaaS","PaaS":"PaaS","SaaS":"SaaS",
 "container":"contenedor","containers":"contenedores","Docker":"Docker","Kubernetes":"Kubernetes",
 "serverless":"serverless / sin servidor","function":"funci\u00f3n","API":"API","SDK":"SDK","REST":"REST",
 "database":"base de datos","databases":"bases de datos","SQL":"SQL","NoSQL":"NoSQL",
 "table":"tabla","row":"fila","column":"columna","record":"registro","query":"consulta",
 "data":"datos","information":"informaci\u00f3n","knowledge":"conocimiento","analytics":"anal\u00edtica",
 "encryption at rest":"cifrado en reposo","encryption in transit":"cifrado en tr\u00e1nsito",
 // Verbs IT
 "configure":"configurar","manage":"gestionar / administrar","administer":"administrar","maintain":"mantener",
 "design":"dise\u00f1ar","build":"construir","develop":"desarrollar","test":"probar","verify":"verificar",
 "validate":"validar","report":"reportar / informar","write":"escribir","read":"leer","check":"revisar",
 "fix":"arreglar","solve":"resolver","help":"ayudar","train":"entrenar / capacitar","support":"apoyar / dar soporte",
 "lead":"liderar","supervise":"supervisar","oversee":"supervisar","approve":"aprobar","reject":"rechazar",
 "assign":"asignar","prioritise":"priorizar","prioritize":"priorizar","schedule":"programar","plan":"planear",
 "implement":"implementar","propose":"proponer","recommend":"recomendar","suggest":"sugerir",
 "discuss":"discutir","present":"presentar","summarise":"resumir","summarize":"resumir",
 "investigate":"investigar","analyse":"analizar","analyze":"analizar","decide":"decidir",
 "comply":"cumplir","compliance":"cumplimiento","governance":"gobernanza","policy":"pol\u00edtica","policies":"pol\u00edticas",
 "regulation":"regulaci\u00f3n","standard":"est\u00e1ndar","framework":"marco / framework","audit":"auditar / auditor\u00eda",
 // Common
 "yes":"s\u00ed","no":"no","please":"por favor","thanks":"gracias","thank you":"gracias","sorry":"disculpe / lo siento",
 "hi":"hola","hello":"hola","goodbye":"adi\u00f3s","good morning":"buenos d\u00edas","good afternoon":"buenas tardes",
 "name":"nombre","job":"trabajo / empleo","work":"trabajo / trabajar","company":"empresa","office":"oficina",
 "team":"equipo","colleague":"colega / compa\u00f1ero","manager":"jefe / gerente","client":"cliente","customer":"cliente",
 "today":"hoy","tomorrow":"ma\u00f1ana","yesterday":"ayer","now":"ahora","later":"m\u00e1s tarde","soon":"pronto",
 "always":"siempre","usually":"normalmente","often":"frecuentemente","sometimes":"a veces","rarely":"raramente","never":"nunca",
 "morning":"ma\u00f1ana","afternoon":"tarde","evening":"noche / tarde","night":"noche","day":"d\u00eda","days":"d\u00edas",
 "week":"semana","month":"mes","year":"a\u00f1o","hour":"hora","minute":"minuto","second":"segundo",
 "first":"primero","second":"segundo","third":"tercero","next":"siguiente","last":"\u00faltimo","previous":"anterior"
};

async function translateCurrent(){
 const word = _currentPronWord; if(!word) return;
 const trEl = document.getElementById('pron-translation');
 const txt = document.getElementById('pron-es-text');
 trEl.style.display='block';
 txt.textContent = t('Translating\u2026');
 const lower = word.toLowerCase().trim();
 // 1. Curated dictionary first (most reliable)
 if(VOCAB_ES[lower]){
  txt.textContent = VOCAB_ES[lower];
  return;
 }
 // 2. Cache (validated previous queries only)
 const cacheKey = 'sec_es_'+lower;
 let es = localStorage.getItem(cacheKey);
 if(es && es.toLowerCase() !== lower){
  txt.textContent = es;
  return;
 }
 // 3. MyMemory with quality validation
 try{
  const resp = await fetch('https://api.mymemory.translated.net/get?q='+encodeURIComponent(word)+'&langpair=en|es&de=paolobaca2000@gmail.com');
  const data = await resp.json();
  if(data && data.responseData){
   const candidate = (data.responseData.translatedText||'').trim();
   const match = parseFloat(data.responseData.match) || 0;
   // Reject low-quality, identical, or empty results
   if(candidate && match >= 0.7 && candidate.toLowerCase() !== lower && candidate.length < 80){
    es = candidate;
    localStorage.setItem(cacheKey, es);
   }
  }
 } catch(e){ es=null; }
 if(es){
  txt.textContent = es;
 } else {
  txt.textContent = t('Translation not reliable. Consult a dictionary.');
 }
}
function closePron(){
 document.getElementById('pron-overlay').classList.remove('sh');
 if(window.speechSynthesis) window.speechSynthesis.cancel();
 document.getElementById('pron-listen').classList.remove('playing');
 // stop any ongoing recording
 if(_recorder && _recorder.state==='recording'){ try{_recorder.stop();}catch(e){} }
 if(_recStream){ try{_recStream.getTracks().forEach(t=>t.stop());}catch(e){} _recStream=null; }
 if(_recAudio){ try{_recAudio.pause();}catch(e){} }
 if(_recMeterTimer){clearInterval(_recMeterTimer); _recMeterTimer=null;}
}
function renderVoiceButtons(){
 if(!window.speechSynthesis) return;
 const voices = window.speechSynthesis.getVoices().filter(v=>v.lang.toLowerCase().startsWith('en'));
 const tgt = document.getElementById('pron-voices');
 if(!voices.length){ tgt.innerHTML = '<span style="color:#94A3B8;font-size:.72rem">'+t('Pronunciation not available offline for this word. TTS still works.')+'</span>'; return; }
 const preferOrder = ['en-US','en-GB','en-AU','en-IN','en-CA'];
 voices.sort((a,b)=>preferOrder.indexOf(a.lang)-preferOrder.indexOf(b.lang));
 if(!_currentPronVoice) _currentPronVoice = voices[0].name;
 tgt.innerHTML = voices.slice(0,5).map(v=>{
  const label = v.lang.replace('en-','').toUpperCase();
  return `<button class="pron-voice-btn ${_currentPronVoice===v.name?'act':''}" onclick="pickVoice('${escapeJs(v.name)}')">${label}</button>`;
 }).join('');
}
function pickVoice(name){
 _currentPronVoice = name;
 renderVoiceButtons();
 speakCurrent();
}
function speakCurrent(){
 if(!_currentPronWord || !window.speechSynthesis) return;
 window.speechSynthesis.cancel();
 const u = new SpeechSynthesisUtterance(_currentPronWord);
 const voices = window.speechSynthesis.getVoices();
 const v = voices.find(x=>x.name===_currentPronVoice) || voices.find(x=>x.lang && x.lang.toLowerCase().startsWith('en'));
 if(v){ u.voice = v; u.lang = v.lang; } else { u.lang='en-US'; }
 u.rate = 0.9;
 const btn = document.getElementById('pron-listen');
 btn.classList.add('playing');
 u.onend = ()=>btn.classList.remove('playing');
 u.onerror = ()=>btn.classList.remove('playing');
 window.speechSynthesis.speak(u);
}
function speakFlash(){
 const w = document.getElementById('fc-word').textContent;
 if(!w) return;
 _currentPronWord = w;
 speakCurrent();
}
async function loadDictEntry(word){
 const cacheKey = 'sec_dict_'+word.toLowerCase();
 let data = null;
 const cached = localStorage.getItem(cacheKey);
 if(cached){
  try{ data = JSON.parse(cached); } catch(e){}
 }
 if(!data){
  try{
   const resp = await fetch('https://api.dictionaryapi.dev/api/v2/entries/en/'+encodeURIComponent(word.toLowerCase().split(' ')[0]));
   if(resp.ok){
    data = await resp.json();
    localStorage.setItem(cacheKey, JSON.stringify(data));
   } else {
    data = null;
   }
  } catch(e){ data = null; }
 }
 if(_currentPronWord !== word) return; // user may have closed modal
 const body = document.getElementById('pron-body');
 const ipaEl = document.getElementById('pron-ipa');
 if(!data || !data.length || data.title){
  ipaEl.textContent = '/ '+simpleRespell(word)+' /';
  ipaEl.classList.remove('empty');
  body.innerHTML = `<div class="pron-error"><i class="fas fa-triangle-exclamation"></i> ${t('No definition found for this word.')}</div>
   <div class="pron-mark-row">${markButtons(word)}</div>
   ${recordZone(word)}`;
  _recBlob = null;
  const playBtn = document.getElementById('pron-rec-play');
  if(playBtn) playBtn.disabled = true;
  return;
 }
 const entry = data[0];
 // IPA
 let ipa = '';
 if(entry.phonetic) ipa = entry.phonetic;
 if(!ipa && entry.phonetics && entry.phonetics.length){
  ipa = (entry.phonetics.find(p=>p.text)||{}).text || '';
 }
 if(ipa){ ipaEl.textContent = ipa; ipaEl.classList.remove('empty'); }
 else { ipaEl.textContent = '/ '+simpleRespell(word)+' /'; ipaEl.classList.remove('empty'); }
 // meanings
 let html = '';
 (entry.meanings||[]).slice(0,3).forEach(m=>{
  html += `<div class="pron-sec"><h4><span class="pron-pos">${escapeHtml(m.partOfSpeech||'')}</span></h4>`;
  (m.definitions||[]).slice(0,2).forEach(d=>{
   html += `<div class="pron-def">\u2022 ${escapeHtml(d.definition||'')}</div>`;
   if(d.example) html += `<div class="pron-ex">"${escapeHtml(d.example)}"</div>`;
  });
  html += '</div>';
 });
 html += '<div class="pron-mark-row">'+markButtons(word)+'</div>';
 html += recordZone(word);
 body.innerHTML = html;
 // reset any previous recording handle
 _recBlob = null;
 const playBtn = document.getElementById('pron-rec-play');
 if(playBtn) playBtn.disabled = true;
}

// ---------- VOICE RECORDING ----------
let _recChunks = [], _recorder = null, _recStream = null, _recBlob = null, _recAudio = null, _recMeterTimer = null;
async function toggleRecord(word){
 const btn = document.getElementById('pron-rec-btn');
 const lbl = document.getElementById('pron-rec-label');
 const status = document.getElementById('pron-rec-status');
 const meter = document.getElementById('pron-rec-meter');
 if(_recorder && _recorder.state==='recording'){
  stopRecord(); return;
 }
 if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia){
  status.innerHTML = '<i class="fas fa-triangle-exclamation"></i> '+t('Microphone access denied or unavailable.');
  return;
 }
 try{
  _recStream = await navigator.mediaDevices.getUserMedia({audio:true});
  _recChunks = [];
  const mime = MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : 'audio/webm';
  _recorder = new MediaRecorder(_recStream, {mimeType: mime});
  _recorder.ondataavailable = e => { if(e.data.size>0) _recChunks.push(e.data); };
  _recorder.onstop = ()=>{
   _recBlob = new Blob(_recChunks, {type: mime});
   const playBtn = document.getElementById('pron-rec-play'); if(playBtn) playBtn.disabled = false;
   status.innerHTML = '<i class="fas fa-check-circle"></i> '+t('Ready to play');
   status.classList.add('ready');
   btn.classList.remove('recording');
   lbl.textContent = t('Start recording');
   if(meter) meter.style.width = '0%';
   if(_recMeterTimer){clearInterval(_recMeterTimer); _recMeterTimer=null;}
   if(_recStream){_recStream.getTracks().forEach(t=>t.stop()); _recStream=null;}
  };
  _recorder.start();
  btn.classList.add('recording');
  lbl.textContent = t('Stop');
  status.innerHTML = '<i class="fas fa-circle" style="color:#DC2626"></i> '+t('Recording...');
  status.classList.remove('ready');
  // simple level meter via setInterval (time-based, decorative)
  let elapsed = 0;
  _recMeterTimer = setInterval(()=>{
   elapsed += 0.1;
   const pct = Math.min(100, (elapsed/5)*100);
   if(meter) meter.style.width = pct+'%';
   if(elapsed >= 5) stopRecord();
  }, 100);
 } catch(e){
  status.innerHTML = '<i class="fas fa-triangle-exclamation"></i> '+t('Microphone access denied or unavailable.');
 }
}
function stopRecord(){
 if(_recorder && _recorder.state==='recording') _recorder.stop();
}
function playRecording(){
 if(!_recBlob) return;
 if(_recAudio){ try{_recAudio.pause();}catch(e){} }
 _recAudio = new Audio(URL.createObjectURL(_recBlob));
 _recAudio.play();
}
function markButtons(word){
 return `<button class="pron-mark-btn known" onclick="markWordFromPron('${escapeJs(word)}','known')"><i class="fas fa-check"></i> ${t('Mark as known')}</button>
  <button class="pron-mark-btn review" onclick="markWordFromPron('${escapeJs(word)}','review')"><i class="fas fa-rotate"></i> ${t('Mark for review')}</button>`;
}

function recordZone(word){
 return `
 <div class="pron-rec-zone">
  <h4><i class="fas fa-microphone"></i> ${t('Record your pronunciation')}</h4>
  <div class="pron-rec-row">
   <button id="pron-rec-btn" class="pron-rec-btn" onclick="toggleRecord('${escapeJs(word)}')">
    <i class="fas fa-microphone"></i> <span id="pron-rec-label">${t('Start recording')}</span>
   </button>
   <button id="pron-rec-play" class="pron-rec-play" onclick="playRecording()" disabled>
    <i class="fas fa-play"></i> ${t('Play mine')}
   </button>
   <button class="pron-rec-play" onclick="speakCurrent()" style="background:#475569">
    <i class="fas fa-volume-high"></i> ${t('Play model')}
   </button>
   <span class="pron-rec-status" id="pron-rec-status"><i class="fas fa-circle"></i> ${t('Idle')}</span>
  </div>
  <div class="pron-rec-meter"><div class="pron-rec-meter-fill" id="pron-rec-meter"></div></div>
  <div class="pron-compare" id="pron-compare"><b>${t('Tip')}:</b> ${t("Listen to the model first, then record yourself and compare. Self-assessment: does your recording stress the same syllable?")}</div>
 </div>`;
}
function markWordFromPron(word, status){
 const k = lessonKey(state.levelCode, state.lessonN);
 state.vocab[k] = state.vocab[k]||{};
 state.vocab[k][word] = status;
 saveVocab();
 closePron();
 // refresh vocab tab if visible
 if(state.activeTab==='vocab') renderMain();
}
function simpleRespell(w){
 return w.toLowerCase();
}

// ---------- VOCABULARY PRACTICE QUIZ ----------
async function startVocabQuiz(){
 const le = getLesson();
 const words = (le.vocab_list||[]).slice();
 if(words.length<4){
  document.getElementById('vocab-quiz-zone').innerHTML = '<div class="content-pending"><i class="fas fa-info-circle"></i> Need at least 4 vocabulary items.</div>';
  return;
 }
 // Pick 6 random words for the quiz
 const pick = words.sort(()=>Math.random()-0.5).slice(0, Math.min(6, words.length));
 const zone = document.getElementById('vocab-quiz-zone');
 zone.innerHTML = '<div class="pron-loading"><i class="fas fa-spinner fa-spin"></i> '+t('Loading dictionary…')+'</div>';
 // Translate each word (Spanish) and pull a definition from cache
 const items = [];
 for(const w of pick){
  let es = localStorage.getItem('sec_es_'+w.toLowerCase());
  if(!es){
   try{
    const r = await fetch('https://api.mymemory.translated.net/get?q='+encodeURIComponent(w)+'&langpair=en|es');
    const d = await r.json();
    if(d && d.responseData) es = d.responseData.translatedText;
    if(es) localStorage.setItem('sec_es_'+w.toLowerCase(), es);
   } catch(e){ es = w; }
  }
  let def = '';
  const cached = localStorage.getItem('sec_dict_'+w.toLowerCase());
  if(cached){
   try{
    const data = JSON.parse(cached);
    if(data && data[0] && data[0].meanings && data[0].meanings[0] && data[0].meanings[0].definitions){
     def = data[0].meanings[0].definitions[0].definition || '';
    }
   } catch(e){}
  }
  items.push({en: w, es: es||w, def: def});
 }
 renderVocabQuiz(items);
}

let _vqState = {};
function renderVocabQuiz(items){
 _vqState = {items, answers:{}};
 const zone = document.getElementById('vocab-quiz-zone');
 // Build a matching exercise: word ↔ Spanish translation
 const left = items.map((it,i)=>({k:i, label:it.en}));
 const right = items.map((it,i)=>({k:i, label:it.es})).slice().sort(()=>Math.random()-0.5);
 const html = `
 <div class="ex-block" style="border:2px solid var(--p)">
  <div class="ex-head">
   <div class="ex-num"><i class="fas fa-graduation-cap"></i></div>
   <div><div class="ex-type">${t('Match the word with its meaning')}</div></div>
  </div>
  <div class="ex-q">${t('Drag and drop or click to match each English word with its Spanish meaning.')}</div>
  <div class="ex-match">
   <div class="ex-match-col"><h5>EN</h5>
    ${left.map(it=>`<div class="ex-match-item" data-side="L" data-k="${it.k}" onclick="vqClick('L',${it.k})">${escapeHtml(it.label)}<span class="match-num"></span></div>`).join('')}
   </div>
   <div class="ex-match-col"><h5>ES</h5>
    ${right.map(it=>`<div class="ex-match-item" data-side="R" data-k="${it.k}" onclick="vqClick('R',${it.k})">${escapeHtml(it.label)}<span class="match-num"></span></div>`).join('')}
   </div>
  </div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="startVocabQuiz()"><i class="fas fa-rotate"></i> ${t('New quiz')}</button>
  </div>
  <div class="ex-feedback" id="vq-fb"></div>
 </div>`;
 zone.innerHTML = html;
 _vqMatch = {L:null,R:null,pairs:{}};
}

let _vqMatch = {L:null,R:null,pairs:{}};
function vqClick(side, k){
 const block = document.getElementById('vocab-quiz-zone');
 const item = block.querySelector('.ex-match-item[data-side="'+side+'"][data-k="'+k+'"]');
 if(item.classList.contains('matched')) return;
 block.querySelectorAll('.ex-match-item[data-side="'+side+'"].selected').forEach(x=>x.classList.remove('selected'));
 item.classList.add('selected');
 _vqMatch[side]=k;
 if(_vqMatch.L!=null && _vqMatch.R!=null){
  if(_vqMatch.L===_vqMatch.R){
   const nums = Object.keys(_vqMatch.pairs).length+1;
   block.querySelectorAll('.ex-match-item[data-k="'+_vqMatch.L+'"]').forEach(x=>{
    x.classList.remove('selected');x.classList.add('matched');
    x.querySelector('.match-num').textContent = nums;
   });
   _vqMatch.pairs[_vqMatch.L]=true;_vqMatch.L=null;_vqMatch.R=null;
   if(Object.keys(_vqMatch.pairs).length===_vqState.items.length){
    const fb = document.getElementById('vq-fb');
    fb.className='ex-feedback ok';
    fb.innerHTML='<div class="ex-fb-head"><i class="fas fa-circle-check"></i> '+t('Correct!')+'</div>'+t('All pairs matched correctly!');
   }
  } else {
   block.querySelectorAll('.ex-match-item.selected').forEach(x=>{
    x.classList.remove('selected');x.classList.add('wrong');
    setTimeout(()=>x.classList.remove('wrong'),400);
   });
   _vqMatch.L=null;_vqMatch.R=null;
  }
 }
}

// ensure voices load (Chrome fires event after load)
if(typeof window!=='undefined' && window.speechSynthesis){
 window.speechSynthesis.onvoiceschanged = ()=>{
  if(document.getElementById('pron-overlay') && document.getElementById('pron-overlay').classList.contains('sh')) renderVoiceButtons();
 };
}

// ---------- READING ----------
function renderReading(lv,le){
 const tgt = parseRangeAny(le.reading) || [200,400];
 const wpm = COURSE.quotas.find(q=>q.cefr===lv.code).wpm;
 // if the lesson has a pilot passage + exercises, render the full interactive mode
 if(le.has_content && le.passage){
  const p = le.passage;
  const est = Math.ceil(p.word_count / parseInt(String(wpm).split('\u2013')[0]));
  return `
  <div class="callout">
   <h4>${t('Reading task (Cambridge / IELTS / TOEFL style)')}</h4>${escapeHtml(le.reading)}
  </div>

  <div class="read-stats">
   <div class="read-stat"><div class="read-stat-l">${t('Words')}</div><div class="read-stat-v">${p.word_count}</div></div>
   <div class="read-stat"><div class="read-stat-l">${t('CEFR range')}</div><div class="read-stat-v">${tgt[0]}\u2013${tgt[1]} w</div></div>
   <div class="read-stat"><div class="read-stat-l">${t('Speed')}</div><div class="read-stat-v">${wpm} wpm</div></div>
   <div class="read-stat"><div class="read-stat-l">${t('Approx. time')}</div><div class="read-stat-v">${est} ${t('min')}</div></div>
  </div>

  <div class="passage-card">
   <div class="passage-title">${escapeHtml(p.title)}</div>
   <div class="passage-meta">
    <span class="pm-badge"><i class="fas fa-layer-group"></i> ${lv.code}</span>
    <span><i class="fas fa-file-lines"></i> ${p.word_count} ${t('words')}</span>
    <span class="reading-timer" id="rt-btn" onclick="toggleTimer()"><i class="fas fa-stopwatch"></i> <span id="rt-text">${t('Start timer')}</span></span>
   </div>
   <div class="passage-body">${escapeHtml(p.text).split('\n\n').map(par=>'<p>'+par.replace(/\n/g,'<br>')+'</p>').join('')}</div>
   <div class="passage-source"><i class="fas fa-bookmark"></i> ${escapeHtml(p.source)}</div>
  </div>

  <div class="ex-progress">
   <div>${t('Comprehension exercises')}: <b id="ex-done-count">0</b> / ${le.exercises.length}</div>
   <div class="ex-score-pill g" id="ex-score-pill">${t('Not attempted yet')}</div>
  </div>

  ${le.exercises.map((ex,i)=>renderExercise(ex,i)).join('')}

  <div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap">
   <button class="btn pri" onclick="checkAllExercises()"><i class="fas fa-check-double"></i> ${t('Check all')}</button>
   <button class="btn sec" onclick="resetAllExercises()"><i class="fas fa-rotate-left"></i> ${t('Restart')}</button>
  </div>
  `;
 }

 // fallback: lesson without pilot content yet
 const key = lessonKey(lv.code,le.n);
 return `
 <div class="content-pending">
  <i class="fas fa-triangle-exclamation"></i>
  <div>
   <b>${t('Reading text not yet included in the pilot.')}</b><br>
   ${t('Use the textarea to paste an article from a free source (see Listening tab for the directory).')}
  </div>
 </div>
 <div class="callout">
  <h4>${t('Reading task')}</h4>${escapeHtml(le.reading)}
 </div>

 <div class="read-stats">
  <div class="read-stat"><div class="read-stat-l">${t('Recommended range')}</div><div class="read-stat-v">${tgt[0]}\u2013${tgt[1]} w</div></div>
  <div class="read-stat"><div class="read-stat-l">${t('Speed')}</div><div class="read-stat-v">${wpm} wpm</div></div>
  <div class="read-stat"><div class="read-stat-l">${t('Pasted words')}</div><div class="read-stat-v" id="rp-count">0</div></div>
 </div>

 <div class="rp-area empty" id="rp-area" contenteditable="true" data-ph="${t('Paste the reading text here\u2026')}"></div>

 <h3 style="font-size:1rem;font-weight:700;margin:18px 0 10px">${t('Open questions')}</h3>
 ${[
  {n:'Q1',tt:t('Main idea'),p:t('In 1\u20132 sentences, what is the main idea?')},
  {n:'Q2',tt:t('Detail'),p:t('List 3 specific facts or figures from the text.')},
  {n:'Q3',tt:t('Vocabulary in context'),p:t("Pick 3 words from today's vocabulary that appear in the text and explain them.")},
  {n:'Q4',tt:t('Inference'),p:t('What can be inferred that is NOT explicitly stated?')},
  {n:'Q5',tt:t('Cyber transfer'),p:t('How does this reading relate to:')+' '+le.cyber+'?'}
 ].map(q=>`
  <div class="q-block">
   <div class="q-n">${q.n} \u2022 ${q.tt}</div>
   <div class="q-t">${escapeHtml(q.p)}</div>
   <textarea placeholder="${t('your answer')}..." data-q="${q.n}"></textarea>
  </div>`).join('')}
 `;
}

// ---------- EXERCISES ENGINE ----------
function renderExercise(ex,i,scope){
 scope = scope || 'rd'; // 'rd' (reading) or 'uoe'
 const prefix = scope; // for unique DOM IDs
 const base = `<div class="ex-block" data-ex-i="${i}" data-ex-scope="${scope}" data-ex-type="${ex.type}">
  <div class="ex-head"><div class="ex-num">${i+1}</div>
   <div><div class="ex-type">${exerciseTypeLabel(ex.type)}</div></div>
  </div>`;
 const q = ex.q ? `<div class="ex-q">${escapeHtml(ex.q)}</div>` : '';
 let body='';
 if(ex.type==='mcq'){
  body = q + `<div class="ex-opts">
   ${ex.options.map((o,j)=>`<div class="ex-opt" data-j="${j}" onclick="selectMCQ(${i},${j},'${scope}')">
    <div class="ex-letter">${String.fromCharCode(65+j)}</div>
    <div>${escapeHtml(o)}</div></div>`).join('')}
  </div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkMCQ(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='mc_cloze'){
  // sentence with gap + 4 options (FCE Part 1 style)
  const sentHtml = escapeHtml(ex.sentence||'').replace(/_{2,}|\\u2500{2,}|___/g, '<span class="uoe-gap">_____</span>');
  body = q + `<div class="uoe-sent">${sentHtml}</div>
  <div class="ex-opts">
   ${ex.options.map((o,j)=>`<div class="ex-opt" data-j="${j}" onclick="selectMCQ(${i},${j},'${scope}')">
    <div class="ex-letter">${String.fromCharCode(65+j)}</div>
    <div>${escapeHtml(o)}</div></div>`).join('')}
  </div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkMCQ(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='tfng'){
  body = q + `<div class="ex-opts">
   ${[['T','True'],['F','False'],['NG','Not Given']].map(([k,lbl])=>`<div class="ex-opt" data-j="${k}" onclick="selectTFNG(${i},'${k}','${scope}')">
    <div class="ex-letter">${k}</div><div>${lbl}</div></div>`).join('')}
  </div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkTFNG(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='gap'){
  body = q + `<div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">
   <input class="ex-gap-input" type="text" data-gap="${i}" data-scope="${scope}" placeholder="${t('your answer')}" autocomplete="off">
   <button class="ex-btn check" onclick="checkGap(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='cloze'){
  // open cloze: sentence with ___ and inline input (FCE Part 2)
  const parts = (ex.sentence||'').split(/_{2,}|___/);
  const sentHtml = parts.map(escapeHtml).join('<input class="ex-gap-input" type="text" data-gap="'+i+'" data-scope="'+scope+'" placeholder="?" autocomplete="off" style="width:140px;display:inline-block;margin:0 4px">');
  body = q + `<div class="uoe-sent">${sentHtml}</div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkGap(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='word_form'){
  // word formation (FCE Part 3)
  const parts = (ex.sentence||'').split(/_{2,}|___/);
  const sentHtml = parts.map(escapeHtml).join('<input class="ex-gap-input" type="text" data-gap="'+i+'" data-scope="'+scope+'" placeholder="?" autocomplete="off" style="width:160px;display:inline-block;margin:0 4px">');
  body = q + `<div><span class="uoe-base">${escapeHtml(ex.base||'')}</span></div>
  <div class="uoe-sent" style="margin-top:8px">${sentHtml}</div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkGap(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='key_word'){
  // key word transformation (FCE Part 4)
  const parts = (ex.gap_template||'').split(/_{2,}|___/);
  const tplHtml = parts.map(escapeHtml).join('<input class="ex-gap-input" type="text" data-gap="'+i+'" data-scope="'+scope+'" placeholder="3\u20135 words" autocomplete="off" style="width:220px;display:inline-block;margin:0 4px">');
  body = q + `<div class="uoe-from">${t('Original:')||'Original:'}</div>
  <div class="uoe-original">${escapeHtml(ex.original||'')}</div>
  <div style="margin:10px 0"><span class="uoe-keyword">${escapeHtml(ex.key||'')}</span></div>
  <div class="uoe-to">${t('Rewrite:')||'Rewrite using the key word (do not change it):'}</div>
  <div class="uoe-sent">${tplHtml}</div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkKeyWord(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reveal" onclick="revealModel(${i},'${scope}')"><i class="fas fa-eye"></i> ${t('Show model answer')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='match'){
  const left = ex.pairs.map(p=>p[0]);
  const right = ex.pairs.map(p=>p[1]);
  const shuffled = shuffleStable(right, i+lessonKey(state.levelCode,state.lessonN));
  body = q + `<div class="ex-match">
   <div class="ex-match-col"><h5>${t('Column A')}</h5>
    ${left.map((x,k)=>`<div class="ex-match-item" data-side="L" data-k="${k}" onclick="matchClick(${i},'L',${k},'${scope}')">${escapeHtml(x)}<span class="match-num"></span></div>`).join('')}
   </div>
   <div class="ex-match-col"><h5>${t('Column B')}</h5>
    ${shuffled.map((x,k)=>{
     const origIdx = right.indexOf(x);
     return `<div class="ex-match-item" data-side="R" data-k="${origIdx}" onclick="matchClick(${i},'R',${origIdx},'${scope}')">${escapeHtml(x)}<span class="match-num"></span></div>`;
    }).join('')}
   </div>
  </div>
  <div class="ex-actions">
   <button class="ex-btn check" onclick="checkMatch(${i},'${scope}')"><i class="fas fa-check"></i> ${t('Check')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 } else if(ex.type==='short'){
  body = q + `<textarea class="ex-short-text" placeholder="${t('Write your answer...')}" data-short="${i}" data-scope="${scope}"></textarea>
  <div class="ex-actions">
   <button class="ex-btn reveal" onclick="revealModel(${i},'${scope}')"><i class="fas fa-eye"></i> ${t('Show model answer')}</button>
   <button class="ex-btn reset" onclick="resetEx(${i},'${scope}')"><i class="fas fa-rotate-left"></i></button>
  </div>`;
 }
 return base + body + `<div class="ex-feedback" data-fb="${i}" data-fb-scope="${scope}"></div></div>`;
}

function exerciseTypeLabel(tp){
 const labels = {
  mcq:t('Multiple Choice'),
  mc_cloze:'Multiple-choice cloze',
  tfng:t('True / False / Not Given'),
  gap:t('Gap-fill'),
  cloze:'Open cloze',
  word_form:'Word formation',
  key_word:'Key word transformation',
  match:t('Matching'),
  short:t('Short answer')
 };
 return labels[tp]||tp;
}

function shuffleStable(arr, seedStr){
 let h=0; for(let i=0;i<seedStr.length;i++) h=(h*31+seedStr.charCodeAt(i))|0;
 const a = arr.slice();
 for(let i=a.length-1;i>0;i--){ h = (h*9301+49297)%233280; const j = Math.floor((h/233280)*(i+1)); [a[i],a[j]]=[a[j],a[i]]; }
 return a;
}

// state for exercises (per lesson, reset on route) \u2013 keyed by scope+index
let exState = {};
let matchState = {};
function sk(i,scope){return (scope||'rd')+'_'+i}
function getEx(i,scope){
 const le = getLesson();
 return (scope==='uoe' ? le.use_of_english : le.exercises)[i];
}
function blockSel(i,scope){
 return document.querySelector('[data-ex-scope="'+(scope||'rd')+'"][data-ex-i="'+i+'"]');
}
function selectMCQ(i,j,scope){
 const block = blockSel(i,scope); if(!block) return;
 block.querySelectorAll('.ex-opt').forEach(o=>o.classList.remove('selected'));
 block.querySelector('.ex-opt[data-j="'+j+'"]').classList.add('selected');
 exState[sk(i,scope)] = j;
}
function selectTFNG(i,k,scope){
 const block = blockSel(i,scope); if(!block) return;
 block.querySelectorAll('.ex-opt').forEach(o=>o.classList.remove('selected'));
 block.querySelector('.ex-opt[data-j="'+k+'"]').classList.add('selected');
 exState[sk(i,scope)] = k;
}
function checkMCQ(i,scope){
 scope = scope||'rd';
 const ex = getEx(i,scope); const sel = exState[sk(i,scope)];
 const block = blockSel(i,scope);
 if(sel===undefined){ flash(i,t('Select an option first.'),false,scope); return; }
 block.querySelectorAll('.ex-opt').forEach((o,j)=>{
  o.classList.remove('selected');
  if(j===ex.a) o.classList.add('correct');
  else if(j===sel) o.classList.add('wrong');
 });
 const ok = sel===ex.a;
 flash(i, ok ? (t('Correct!')+' '+(ex.explain||'')) : (t('Correct answer:')+' '+String.fromCharCode(65+ex.a)+' \u2013 '+escapeHtml(ex.options[ex.a])+'. '+(ex.explain||'')), ok, scope);
 markDone(i,scope);
}
function checkTFNG(i,scope){
 scope = scope||'rd';
 const ex = getEx(i,scope); const sel = exState[sk(i,scope)];
 const block = blockSel(i,scope);
 if(sel===undefined){ flash(i,t('Select True, False or Not Given.'),false,scope); return; }
 block.querySelectorAll('.ex-opt').forEach(o=>{
  const k = o.dataset.j;
  o.classList.remove('selected');
  if(k===ex.a) o.classList.add('correct');
  else if(k===sel) o.classList.add('wrong');
 });
 const ok = sel===ex.a;
 flash(i, ok ? (t('Correct!')+' '+(ex.explain||'')) : (t('Correct answer:')+' '+ex.a+'. '+(ex.explain||'')), ok, scope);
 markDone(i,scope);
}
function checkGap(i,scope){
 scope = scope||'rd';
 const ex = getEx(i,scope);
 const block = blockSel(i,scope);
 const inp = block.querySelector('[data-gap="'+i+'"]');
 const v = (inp.value||'').trim();
 if(!v){ flash(i,t('Write an answer.'),false,scope); return; }
 const alts = (ex.alts||[ex.a]).map(s=>String(s).toLowerCase().trim());
 const ok = alts.includes(v.toLowerCase());
 inp.classList.remove('correct','wrong');
 inp.classList.add(ok?'correct':'wrong');
 flash(i, ok ? (t('Correct!')+' '+(ex.explain||'')) : (t('Expected answer:')+' "'+ex.a+'". '+(ex.explain||'')), ok, scope);
 markDone(i,scope);
}
function checkKeyWord(i,scope){
 scope = scope||'rd';
 const ex = getEx(i,scope);
 const block = blockSel(i,scope);
 const inp = block.querySelector('[data-gap="'+i+'"]');
 const v = (inp.value||'').trim();
 if(!v){ flash(i,t('Write an answer.'),false,scope); return; }
 const alts = (ex.alts||[ex.a]).map(s=>String(s).toLowerCase().replace(/\s+/g,' ').trim());
 const userLower = v.toLowerCase().replace(/\s+/g,' ').trim();
 // must include key word
 const keyOk = userLower.split(/\s+/).includes((ex.key||'').toLowerCase());
 const matchOk = alts.includes(userLower);
 const ok = keyOk && matchOk;
 inp.classList.remove('correct','wrong');
 inp.classList.add(ok?'correct':'wrong');
 let msg;
 if(ok) msg = t('Correct!')+' '+(ex.explain||'');
 else if(!keyOk) msg = 'You must use the key word: '+ex.key+' (unchanged). '+(ex.explain||'');
 else msg = t('Expected answer:')+' "'+ex.a+'". '+(ex.explain||'');
 flash(i, msg, ok, scope);
 markDone(i,scope);
}

function matchClick(i,side,k,scope){
 scope = scope||'rd';
 const key = sk(i,scope);
 matchState[key] = matchState[key]||{L:null,R:null,pairs:{}};
 const ms = matchState[key];
 const block = blockSel(i,scope);
 const item = block.querySelector('.ex-match-item[data-side="'+side+'"][data-k="'+k+'"]');
 if(item.classList.contains('matched')) return;
 block.querySelectorAll('.ex-match-item[data-side="'+side+'"].selected').forEach(x=>x.classList.remove('selected'));
 item.classList.add('selected'); ms[side]=k;
 if(ms.L!=null && ms.R!=null){
  if(ms.L===ms.R){
   const nums = Object.keys(ms.pairs).length+1;
   block.querySelectorAll('.ex-match-item[data-k="'+ms.L+'"]').forEach(x=>{
    x.classList.remove('selected'); x.classList.add('matched');
    x.querySelector('.match-num').textContent = nums;
   });
   ms.pairs[ms.L]=true; ms.L=null; ms.R=null;
   const ex = getEx(i,scope);
   if(Object.keys(ms.pairs).length===ex.pairs.length){
    flash(i,t('All pairs matched correctly!'),true,scope); markDone(i,scope);
   }
  } else {
   block.querySelectorAll('.ex-match-item.selected').forEach(x=>{
    x.classList.remove('selected'); x.classList.add('wrong');
    setTimeout(()=>x.classList.remove('wrong'),400);
   });
   ms.L=null; ms.R=null;
  }
 }
}
function checkMatch(i,scope){
 scope = scope||'rd';
 const ex = getEx(i,scope);
 const ms = matchState[sk(i,scope)]||{pairs:{}};
 const found = Object.keys(ms.pairs).length;
 const ok = found===ex.pairs.length;
 flash(i, ok ? (found+'/'+ex.pairs.length+' '+t('Correct')+'!') : (found+'/'+ex.pairs.length+' '+t('pairs matched. Keep trying.')), ok, scope);
 if(ok) markDone(i,scope);
}

function revealModel(i,scope){
 scope = scope||'rd';
 const ex = getEx(i,scope);
 const block = blockSel(i,scope);
 const fb = block.querySelector('[data-fb="'+i+'"]');
 fb.className='ex-feedback model';
 fb.innerHTML = '<div class="ex-fb-head"><i class="fas fa-lightbulb"></i> '+t('Model answer')+'</div>'+escapeHtml(ex.model||ex.a||t('(no model)'));
 markDone(i,scope);
}

function resetEx(i,scope){
 scope = scope||'rd';
 const block = blockSel(i,scope); if(!block) return;
 block.querySelectorAll('.ex-opt').forEach(o=>o.classList.remove('selected','correct','wrong'));
 block.querySelectorAll('.ex-match-item').forEach(o=>{o.classList.remove('selected','matched','wrong');const mn=o.querySelector('.match-num');if(mn) mn.textContent='';});
 block.querySelectorAll('.ex-gap-input').forEach(o=>{o.classList.remove('correct','wrong');o.value='';});
 block.querySelectorAll('.ex-short-text').forEach(o=>o.value='');
 const fb = block.querySelector('[data-fb="'+i+'"]'); if(fb){fb.className='ex-feedback'; fb.innerHTML='';}
 delete exState[sk(i,scope)]; delete matchState[sk(i,scope)];
 const doneSet = (scope==='uoe'?(window.__uoeDone||new Set()):(window.__exDone||new Set()));
 doneSet.delete(i);
 if(scope==='uoe') window.__uoeDone = doneSet; else window.__exDone = doneSet;
 if(scope==='uoe') updateUoEProgress(); else updateExProgress();
}
function resetAllExercises(){
 const le = getLesson();
 if(!le.exercises) return;
 le.exercises.forEach((_,i)=>resetEx(i,'rd'));
 window.__exDone = new Set();
 updateExProgress();
}
function checkAllExercises(){
 const le = getLesson();
 if(!le.exercises) return;
 le.exercises.forEach((ex,i)=>dispatchCheck(ex,i,'rd'));
}

function flash(i,msg,ok,scope){
 scope = scope||'rd';
 const block = blockSel(i,scope);
 const fb = block ? block.querySelector('[data-fb="'+i+'"]') : document.querySelector('[data-fb="'+i+'"]');
 if(!fb) return;
 fb.className = 'ex-feedback '+(ok?'ok':'no');
 fb.innerHTML = '<div class="ex-fb-head"><i class="fas fa-'+(ok?'circle-check':'circle-xmark')+'"></i> '+(ok?t('Correct'):t('Incorrect'))+'</div>'+msg;
}
function markDone(i,scope){
 scope = scope||'rd';
 if(scope==='uoe'){
  const s = window.__uoeDone || new Set(); s.add(i); window.__uoeDone = s;
  updateUoEProgress();
 } else {
  const s = window.__exDone || new Set(); s.add(i); window.__exDone = s;
  updateExProgress();
 }
}
function updateExProgress(){
 const le = getLesson();
 if(!le.exercises) return;
 const done = (window.__exDone||new Set()).size;
 const cntEl = document.getElementById('ex-done-count'); if(cntEl) cntEl.textContent = done;
 const pill = document.getElementById('ex-score-pill');
 if(pill){
  const pct = done/le.exercises.length;
  pill.className = 'ex-score-pill '+(pct>=0.8?'g':pct>=0.4?'y':'r');
  pill.textContent = done+'/'+le.exercises.length+(done===le.exercises.length?' \u2014 '+t('Completed').toLowerCase()+'!':'');
 }
}

// ---------- READING TIMER ----------
let _rtStart=null, _rtInt=null;
function toggleTimer(){
 const btn = document.getElementById('rt-btn'); const tx = document.getElementById('rt-text');
 if(!btn) return;
 if(_rtStart){ clearInterval(_rtInt); _rtStart=null; btn.classList.remove('on'); tx.textContent=t('Start timer'); return; }
 _rtStart = Date.now(); btn.classList.add('on');
 _rtInt = setInterval(()=>{
  const s = Math.floor((Date.now()-_rtStart)/1000);
  const mm = String(Math.floor(s/60)).padStart(2,'0'); const ss = String(s%60).padStart(2,'0');
  tx.textContent = mm+':'+ss;
 },500);
}

// ---------- LISTENING ----------
function renderListening(lv,le){
 // pick 3 audio sources most relevant to the level
 const lvIdx = {A1:0,A2:1,B1:2,B2:3,C1:4,C2:5}[lv.code];
 const relevant = COURSE.audio_sources.filter(a=>{
  const [lo,hi] = a.levels==='Todos'?[0,5]:a.levels.split('\u2013').map(c=>({A1:0,A2:1,B1:2,B2:3,C1:4,C2:5}[c]));
  return lvIdx>=lo && lvIdx<=hi;
 }).slice(0,6);
 return `
 <div class="callout">
  <h4>${t('Listening task')}</h4>${escapeHtml(le.listening)}
 </div>

 <div class="audio-src-card">
  <div class="as-t"><i class="fas fa-circle-play"></i> ${t('How to work the audio')}</div>
  <div class="as-d">${t("1st global listening (no text) \u2022 2nd listening with transcript \u2022 3rd shadowing of key fragments. Record new words.")}</div>
  <div class="as-meta">
   <span class="as-chip">90 min</span>
   <span class="as-chip pd">${t('Level')} ${lv.code}</span>
  </div>
 </div>

 <h3 style="font-size:1rem;font-weight:700;margin:18px 0 10px">${t('Recommended free sources (Level')} ${lv.code})</h3>
 <div class="audio-pool">
 ${relevant.map(a=>{
  return `<div class="ap-card">
   <div class="ap-name">${escapeHtml(a.name)}</div>
   <a class="ap-dom" href="https://${a.domain}" target="_blank" rel="noopener">${a.domain} <i class="fas fa-up-right-from-square" style="font-size:.7rem"></i></a>
   <div style="margin-top:6px;font-size:.78rem;color:var(--m)">${escapeHtml(a.content)}</div>
   <span class="ap-lic">${escapeHtml(a.license)}</span>
  </div>`;
 }).join('')}
 </div>

 <h3 style="font-size:1rem;font-weight:700;margin:20px 0 10px">${t('Listening comprehension questions')}</h3>
 ${[
  t('Write 3 key words you heard.'),
  t('What is the general topic of the audio?'),
  t('Identify one figure, date or proper name mentioned.'),
  t('Summarise the audio in 2\u20133 sentences.')
 ].map((q,i)=>`<div class="q-block">
  <div class="q-n">L${i+1}</div>
  <div class="q-t">${escapeHtml(q)}</div>
  <textarea placeholder="${t('your answer')}..."></textarea>
 </div>`).join('')}
 `;
}

// ---------- WRITING ----------
function renderWriting(lv,le){
 const tgt = parseRangeAny(le.writing) || [100,140];
 const qt = COURSE.quotas.find(q=>q.cefr===lv.code);
 return `
 <div class="callout">
  <h4>Writing task</h4>${escapeHtml(le.writing)}
 </div>

 <div class="write-meta">
  <div class="write-target">${t('Target:')} <b>${tgt[0]}\u2013${tgt[1]} ${t('words')}</b> \u2022 ${t('Suggested time:')} ${Math.round((tgt[0]+tgt[1])/2/8)} ${t('min')}</div>
  <div class="write-counter" id="w-count">0 ${t('words')}</div>
 </div>

 <textarea class="warea" id="warea" placeholder="${t("Write your answer here. Try to use at least 5 words from today's vocabulary. Do not use a translator for the first draft.")}"></textarea>

 <div class="cefr-check">
  <h4><i class="fas fa-list-check"></i> ${t('Cambridge criteria (self-review)')}</h4>
  <ul>
   <li><label><input type="checkbox"> ${t('I answered all parts of the prompt (Content)')}</label></li>
   <li><label><input type="checkbox"> ${t('I used appropriate register: formal / semi-formal / informal (Communicative Achievement)')}</label></li>
   <li><label><input type="checkbox"> ${t('I organised the text with paragraphs and linkers (Organisation)')}</label></li>
   <li><label><input type="checkbox"> ${t('I applied the target grammar:')} ${escapeHtml(le.grammar)} (Language)</label></li>
   <li><label><input type="checkbox"> ${t('I included \u2265 5 target vocabulary words (Range)')}</label></li>
   <li><label><input type="checkbox"> ${t('I reviewed spelling and punctuation')}</label></li>
  </ul>
 </div>

 <div style="display:flex;gap:10px;margin-top:14px;flex-wrap:wrap">
  <button class="btn pri" onclick="exportForFeedback()"><i class="fas fa-paper-plane"></i> ${t('Submit for teacher feedback')}</button>
  <button class="btn sec" onclick="saveWriting()"><i class="fas fa-floppy-disk"></i> ${t('Save draft')}</button>
  <button class="btn sec" onclick="exportWriting()"><i class="fas fa-file-export"></i> ${t('Export .txt')}</button>
  <button class="btn sec" onclick="clearWriting()"><i class="fas fa-eraser"></i> ${t('Clear')}</button>
 </div>
 <div style="background:#EFF6FF;border-left:4px solid var(--p);padding:12px 16px;border-radius:0 10px 10px 0;margin-top:14px;font-size:.82rem;color:#1E40AF">
  <b><i class="fas fa-circle-info"></i> ${t('How feedback works')}:</b> ${t('Click "Submit for teacher feedback" to download a JSON file. Send that file to your teacher (or paste it in chat) and you will receive marked corrections, errors highlighted, and 3 specific improvements.')}
 </div>
 `;
}

// ---------- CYBER ----------
function renderCyber(lv,le){
 return `
 <div class="callout cyber">
  <h4>${t('Cybersecurity / emerging tech angle')}</h4>
  ${escapeHtml(le.cyber)}
 </div>
 <div class="info-grid">
  <div class="info-card">
   <h4><i class="fas fa-link"></i> ${t('To dig deeper')}</h4>
   <p>${t('Search')} <b>cisa.gov</b>, <b>nist.gov</b> ${t('and')} <b>mitre.org</b> ${t('for related terms to')} <i>"${escapeHtml(le.cyber.split(' ').slice(0,4).join(' '))}..."</i>. ${t('Also')} <b>arXiv cs.CR</b> ${t('for technical papers.')}</p>
  </div>
  <div class="info-card">
   <h4><i class="fas fa-microphone"></i> ${t('Suggested speaking activity')}</h4>
   <p>${t('In pairs, explain the topic in 90 seconds using at least 6 words from the vocabulary. Your partner asks 2 follow-up questions.')}</p>
  </div>
  <div class="info-card">
   <h4><i class="fas fa-graduation-cap"></i> ${t('Exam connection')}</h4>
   <p>${lv.code==='C1'||lv.code==='C2'?t('CAE/CPE Reading Part 7 and Writing Part 2 (report/proposal) typically cover tech policy topics.'):t('PET/FCE Reading uses informational tech texts; IELTS Academic Reading does as well.')}</p>
  </div>
 </div>`;
}

// =============================================================
// HELPERS
// =============================================================
function escapeHtml(s){return (s||'').replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]))}
function escapeAttr(s){return (s||'').replace(/"/g,'&quot;')}
function escapeJs(s){return (s||'').replace(/\\/g,'\\\\').replace(/'/g,"\\'")}
function parseRangeAny(s){const m = String(s).match(/(\d+)[\u2013\-](\d+)/); return m?[+m[1],+m[2]]:null}

function setTab(t){
 state.activeTab = t;
 document.querySelectorAll('.tab').forEach(e=>e.classList.remove('act'));
 document.querySelectorAll('.panel').forEach(e=>e.classList.remove('act'));
 document.querySelector(`.tab[onclick*="'${t}'"]`).classList.add('act');
 document.getElementById('panel-'+t).classList.add('act');
 if(t==='vocab') setVocabMode('list');
 if(t==='write') wireWriting();
 if(t==='read') wireReading();
}

function toggleDone(){
 const lv = state.levelCode, n = state.lessonN;
 setDone(lv,n,!isDone(lv,n));
 render();
}

function bindLessonHandlers(){
 if(state.activeTab==='write') wireWriting();
 if(state.activeTab==='read') wireReading();
}

// ---------- VOCAB ----------
function setVocabMode(mode){
 document.getElementById('vm-list').classList.toggle('act', mode==='list');
 document.getElementById('vm-flash').classList.toggle('act', mode==='flash');
 document.getElementById('vocab-list-view').style.display = mode==='list'?'':'none';
 document.getElementById('vocab-flash-view').style.display = mode==='flash'?'':'none';
 if(mode==='flash') updateFlash();
}
function toggleWord(w){
 const k = lessonKey(state.levelCode,state.lessonN);
 state.vocab[k] = state.vocab[k]||{};
 state.vocab[k][w] = state.vocab[k][w]==='known' ? null : 'known';
 saveVocab();
 const mn = document.getElementById('mn');
 mn.querySelectorAll('.v-chip').forEach(c=>{
  if(c.dataset.w===w){
   const known = state.vocab[k][w]==='known';
   c.classList.toggle('known', known);
   c.querySelector('i').className = 'fas fa-'+(known?'check':'circle');
  }
 });
 renderVocabMeta();
}
function markAllKnown(){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 const k = lessonKey(lv.code,le.n);
 state.vocab[k] = {};
 le.vocab_list.forEach(w => state.vocab[k][w]='known');
 saveVocab();
 render();
}
function resetVocab(){
 const k = lessonKey(state.levelCode,state.lessonN);
 delete state.vocab[k]; saveVocab(); render();
}
function renderVocabMeta(){
 const lv = state.levelCode, n = state.lessonN;
 const le = COURSE.levels.find(l=>l.code===lv).lessons.find(x=>x.n===n);
 const k = lessonKey(lv,n);
 const kc = Object.values(state.vocab[k]||{}).filter(v=>v==='known').length;
 const el = document.querySelector('.vm-stat');
 if(el) el.innerHTML = `Vocabulario objetivo: <b>${le.vocab_list.length}</b> \u2022 Dominado: <b style="color:var(--ok)">${kc}</b>`;
}
function updateFlash(){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 const w = le.vocab_list[state.flashIdx];
 document.getElementById('fc-word').textContent = w;
 document.getElementById('fc-prompt').textContent = state.flashFlipped
   ? t('Write a sentence using this word in an IT context.') : '';
 document.getElementById('fc-counter').textContent = (state.flashIdx+1)+' / '+le.vocab_list.length;
 const card = document.getElementById('fc-card');
 card.classList.toggle('flip', state.flashFlipped);
}
function flipCard(){state.flashFlipped=!state.flashFlipped;updateFlash();}
function nextCard(){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 state.flashIdx = (state.flashIdx+1) % le.vocab_list.length;
 state.flashFlipped=false; updateFlash();
}
function prevCard(){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 state.flashIdx = (state.flashIdx-1+le.vocab_list.length) % le.vocab_list.length;
 state.flashFlipped=false; updateFlash();
}
function markCard(status){
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 const w = le.vocab_list[state.flashIdx];
 const k = lessonKey(lv.code,le.n);
 state.vocab[k] = state.vocab[k]||{};
 state.vocab[k][w] = status;
 saveVocab();
 nextCard();
}

// ---------- READING ----------
function wireReading(){
 const rp = document.getElementById('rp-area');
 if(!rp) return;
 const key = 'sec_read_'+lessonKey(state.levelCode,state.lessonN);
 const saved = localStorage.getItem(key);
 if(saved){rp.textContent=saved;rp.classList.remove('empty')}
 const update = ()=>{
  const txt = rp.textContent.trim();
  rp.classList.toggle('empty', !txt);
  const wc = txt.split(/\s+/).filter(Boolean).length;
  document.getElementById('rp-count').textContent = wc;
  localStorage.setItem(key, rp.textContent);
 };
 rp.addEventListener('input', update);
 update();
 // restore question answers
 document.querySelectorAll('[data-q]').forEach(t=>{
  const qk = key+'_'+t.dataset.q;
  t.value = localStorage.getItem(qk)||'';
  t.addEventListener('input', ()=>localStorage.setItem(qk, t.value));
 });
}

// ---------- WRITING ----------
function wireWriting(){
 const w = document.getElementById('warea');
 if(!w) return;
 const key = 'sec_write_'+lessonKey(state.levelCode,state.lessonN);
 w.value = localStorage.getItem(key)||'';
 const lv = COURSE.levels.find(l=>l.code===state.levelCode);
 const le = lv.lessons.find(x=>x.n===state.lessonN);
 const tgt = parseRangeAny(le.writing)||[100,140];
 const update = ()=>{
  const wc = w.value.trim().split(/\s+/).filter(Boolean).length;
  const c = document.getElementById('w-count');
  c.textContent = wc+' '+t('words');
  c.classList.remove('ok','low','over');
  if(wc===0){}
  else if(wc < tgt[0]) c.classList.add('low');
  else if(wc <= tgt[1]) c.classList.add('ok');
  else c.classList.add('over');
  localStorage.setItem(key, w.value);
 };
 w.addEventListener('input', update);
 update();
}
function saveWriting(){
 const w = document.getElementById('warea');
 const key = 'sec_write_'+lessonKey(state.levelCode,state.lessonN);
 localStorage.setItem(key, w.value);
 notify(t('Draft saved'));
}
function exportWriting(){
 const w = document.getElementById('warea');
 const lv = state.levelCode, n = state.lessonN;
 const le = COURSE.levels.find(l=>l.code===lv).lessons.find(x=>x.n===n);
 const txt = `Systems Engineers English \u2013 ${lv} Class ${n}\n${le.topic}\n\n${w.value}`;
 const blob = new Blob([txt],{type:'text/plain'});
 const url = URL.createObjectURL(blob);
 const a = document.createElement('a'); a.href=url; a.download=`writing-${lv}-${n}.txt`; a.click();
 URL.revokeObjectURL(url);
}

function exportForFeedback(){
 const w = document.getElementById('warea');
 if(!w || !w.value.trim()){ notify(t('Write something first.')); return; }
 const lv = state.levelCode, n = state.lessonN;
 const le = COURSE.levels.find(l=>l.code===lv).lessons.find(x=>x.n===n);
 const wc = w.value.trim().split(/\s+/).filter(Boolean).length;
 const out = {
  course: 'Systems Engineers English Course',
  level_cefr: lv,
  lesson_number: n,
  lesson_topic: le.topic,
  grammar_focus: le.grammar,
  writing_target: le.writing,
  target_word_range: parseRangeAny(le.writing) || null,
  cyber_angle: le.cyber,
  vocabulary_target: le.vocab_list,
  student_writing: w.value,
  word_count: wc,
  submitted_at: new Date().toISOString(),
  feedback_request: [
   '1) Mark grammar errors and corrections (especially target grammar: '+le.grammar+').',
   '2) Comment on register and tone for the audience.',
   '3) Identify which target vocabulary words were used (and which were missed).',
   '4) Comment on cohesion (linkers, paragraphing, flow).',
   '5) Give 3 specific improvements with rewritten examples.',
   '6) Provide a Cambridge-style band score (1-5) for: Content, Communicative Achievement, Organisation, Language.'
  ]
 };
 const blob = new Blob([JSON.stringify(out,null,2)],{type:'application/json'});
 const url = URL.createObjectURL(blob);
 const a = document.createElement('a'); a.href=url; a.download=`feedback-${lv}-${n}-${Date.now()}.json`; a.click();
 URL.revokeObjectURL(url);
 notify(t('Saved! Send this file to your teacher for feedback.'));
}
function clearWriting(){
 if(!confirm(t('Clear the text?'))) return;
 const w = document.getElementById('warea'); w.value=''; w.dispatchEvent(new Event('input'));
}

// ---------- GLOBAL ----------
function resetProgress(){
 if(!confirm(t('Reset ALL progress (lessons, vocabulary, drafts)?'))) return;
 Object.keys(localStorage).filter(k=>k.startsWith('sec_')).forEach(k=>localStorage.removeItem(k));
 state.progress={}; state.vocab={};
 render(); notify(t('Progress reset'));
}
function exportProgress(){
 const out = {progress:state.progress, vocab:state.vocab, date:new Date().toISOString()};
 const blob = new Blob([JSON.stringify(out,null,2)],{type:'application/json'});
 const url = URL.createObjectURL(blob);
 const a = document.createElement('a'); a.href=url; a.download='systems-english-progress.json'; a.click();
 URL.revokeObjectURL(url);
}
function notify(msg){
 const d = document.createElement('div');
 d.style.cssText='position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#0F172A;color:#fff;padding:10px 20px;border-radius:10px;font-size:.85rem;z-index:9999;box-shadow:0 6px 20px rgba(0,0,0,.2)';
 d.textContent = msg;
 document.body.appendChild(d);
 setTimeout(()=>d.remove(), 2000);
}

// ---------- INIT ----------
render();
</script>
</body>
</html>
"""

html = HTML.replace("__COURSE_DATA__", json.dumps(DATA, ensure_ascii=False))
html = html.replace("__LVL_COLORS__", json.dumps(LVL_COLORS))
html = html.replace("__LVL_ICONS__", json.dumps(LVL_ICON))

# Raw string quedo con secuencias \uXXXX literales: las convierto a caracteres reales.
import re as _re
html = _re.sub(r'\\u([0-9A-Fa-f]{4})', lambda m: chr(int(m.group(1), 16)), html)

OUT.write_text(html, encoding="utf-8")
size_kb = OUT.stat().st_size/1024
print(f"OK: {OUT}  ({size_kb:.1f} KB)")
