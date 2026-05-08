#!/usr/bin/env python3
"""
Fetch Unsplash banner images for every lesson topic across all curricula.

Reads from:
- course-app/course_data.json           (Systems Engineers, 120 lessons)
- general-english-app/course_data.json  (General English, 120 lessons)
- be-curriculum-data.js + extension     (Business English, ~120 units)
- ielts-strategy-curriculum.js          (IELTS, 38 lessons)
- toefl-strategy-curriculum.js          (TOEFL, 23 lessons)
- cambridge-strategy-curriculum.js      (Cambridge, 20 lessons)

Writes incrementally to unsplash-cache.json so a partial run is never lost.
Re-running picks up where it left off (skips already-cached topics).

Rate limit: Unsplash demo tier = 50 req/hour. Sleeps RATE_LIMIT_SLEEP between
requests; a small jitter avoids exact bucket boundaries.
"""

import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ACCESS_KEY = os.environ.get("UNSPLASH_KEY", "TOeiazOrM5fgm18D2HAvAgNe0hDH1MvianBy53X9GcQ")
ROOT = Path(__file__).resolve().parent.parent
CACHE_FILE = ROOT / "unsplash-cache.json"
PROGRESS_FILE = ROOT / "unsplash-fetch.log"
RATE_LIMIT_SLEEP = 75  # seconds between requests (50/hr limit = 72s minimum)
TIMEOUT = 20

# UTM params per Unsplash API guidelines (referral attribution)
UTM = "?utm_source=cohasset_language_center&utm_medium=referral"


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    try:
        with open(PROGRESS_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def topic_key(topic):
    """Stable slug key — normalize to lowercase alphanumerics + underscore.
    JS computes the same key with: .toLowerCase().replace(/[^a-z0-9]+/g,'_')
    .replace(/^_|_$/g,'').slice(0,60). No hashing -> no async crypto in JS."""
    s = re.sub(r'[^a-z0-9]+', '_', topic.strip().lower()).strip('_')
    return s[:60] or "topic"


def load_cache():
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log("WARN: cache file corrupted, starting fresh")
    return {}


def save_cache(cache):
    tmp = CACHE_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(CACHE_FILE)


def extract_course_data_topics(path, course_label):
    if not Path(path).exists():
        return []
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    out = []
    for lvl in data.get("levels", []):
        for les in lvl.get("lessons", []):
            topic = (les.get("topic") or "").strip()
            if topic:
                out.append({
                    "topic": topic,
                    "course": course_label,
                    "level": lvl.get("code", ""),
                    "lesson_n": les.get("n"),
                })
    return out


def extract_be_unit_titles(*paths):
    """BE units have the shape {id:"be-XX-N", title:"Unit N: ..."}; we only
    capture those top-level titles, not nested exercise titles."""
    out = []
    for p in paths:
        if not Path(p).exists():
            continue
        text = Path(p).read_text(encoding="utf-8")
        for m in re.finditer(r'\bid\s*:\s*"be-[a-z0-9]+-\d+"\s*,\s*title\s*:\s*"([^"\n\\]+)"', text):
            t = m.group(1).strip()
            if t:
                out.append({"topic": t, "course": "Business English"})
    return out


def extract_strategy_lesson_titles(path, course_label):
    if not Path(path).exists():
        return []
    text = Path(path).read_text(encoding="utf-8")
    out = []
    # Top-level lesson titles in strategy curricula sit at indent of ~12 spaces inside lessons:[]
    for m in re.finditer(r'\n\s{8,16}title\s*:\s*"([^"\n\\]{8,100})"', text):
        t = m.group(1).strip()
        out.append({"topic": t, "course": course_label})
    return out


def clean_query(topic):
    """Strip 'Unit N:' / 'Class N -' prefixes that hurt photo search relevance."""
    q = re.sub(r'^\s*(Unit|Class|Lesson|Module)\s+\d+\s*[:\-–]\s*', '', topic, flags=re.I)
    # Keep only sensible characters; collapse whitespace
    q = re.sub(r'[^\w\s&\'\-]', ' ', q)
    q = re.sub(r'\s+', ' ', q).strip()
    return q or topic


def fetch_one(query):
    cleaned = clean_query(query)
    encoded = urllib.parse.quote(cleaned)
    url = (
        f"https://api.unsplash.com/search/photos?query={encoded}"
        f"&per_page=1&orientation=landscape&content_filter=high"
    )
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Client-ID {ACCESS_KEY}",
            "Accept-Version": "v1",
        },
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8")), dict(resp.headers)


def main():
    log("=" * 60)
    log("Unsplash banner fetcher starting")
    log(f"Cache file: {CACHE_FILE}")
    cache = load_cache()
    log(f"Existing cache entries: {len(cache)}")

    topics = []
    topics += extract_course_data_topics(ROOT / "course-app/course_data.json", "Systems Engineers")
    topics += extract_course_data_topics(ROOT / "general-english-app/course_data.json", "General English")
    topics += extract_be_unit_titles(
        ROOT / "be-curriculum-data.js",
        ROOT / "be-curriculum-extension.js",
        ROOT / "be-curriculum-supplement.js",
    )
    topics += extract_strategy_lesson_titles(ROOT / "ielts-strategy-curriculum.js", "IELTS Strategy")
    topics += extract_strategy_lesson_titles(ROOT / "toefl-strategy-curriculum.js", "TOEFL Strategy")
    topics += extract_strategy_lesson_titles(ROOT / "cambridge-strategy-curriculum.js", "Cambridge Strategy")

    unique = {}
    for t in topics:
        k = topic_key(t["topic"])
        if k not in unique:
            unique[k] = t

    todo = [(k, v) for k, v in unique.items() if k not in cache]
    log(f"Total unique topics: {len(unique)}")
    log(f"Already cached:     {len(unique) - len(todo)}")
    log(f"To fetch:           {len(todo)}")
    if not todo:
        log("Nothing to do. Exiting.")
        return

    estimated_hours = len(todo) * RATE_LIMIT_SLEEP / 3600
    log(f"Estimated runtime:  ~{estimated_hours:.1f}h at {RATE_LIMIT_SLEEP}s/request")
    log("=" * 60)

    consecutive_errors = 0
    for i, (k, t) in enumerate(todo, 1):
        topic = t["topic"]
        try:
            log(f"[{i:>3}/{len(todo)}] {t['course']:<20} | {topic[:55]}")
            data, headers = fetch_one(topic)
            results = data.get("results", [])
            if results:
                p = results[0]
                cache[k] = {
                    "topic": topic,
                    "course": t.get("course"),
                    "url": p["urls"]["regular"],
                    "url_small": p["urls"]["small"],
                    "url_thumb": p["urls"]["thumb"],
                    "alt": p.get("alt_description") or topic,
                    "color": p.get("color", "#888"),
                    "width": p.get("width"),
                    "height": p.get("height"),
                    "photographer_name": p["user"]["name"],
                    "photographer_url": p["user"]["links"]["html"] + UTM,
                    "photo_id": p["id"],
                    "photo_link": p["links"]["html"] + UTM,
                    "fetched_at": int(time.time()),
                }
                rl = headers.get("X-Ratelimit-Remaining", "?")
                log(f"        OK  by {p['user']['name']:<25} (rl={rl})")
            else:
                cache[k] = {"topic": topic, "course": t.get("course"), "url": None, "no_results": True, "fetched_at": int(time.time())}
                log("        NO RESULTS")
            save_cache(cache)
            consecutive_errors = 0
        except urllib.error.HTTPError as e:
            consecutive_errors += 1
            body = ""
            try:
                body = e.read().decode("utf-8")[:200]
            except Exception:
                pass
            log(f"        HTTP {e.code} {body}")
            if e.code == 403:
                log("        Got 403 — likely rate-limit hit; sleeping 5 minutes")
                time.sleep(300)
            elif consecutive_errors >= 5:
                log("        5 consecutive errors — aborting; cache preserved")
                return
            cache[k] = {"topic": topic, "course": t.get("course"), "url": None, "error": f"HTTP {e.code}", "fetched_at": int(time.time())}
            save_cache(cache)
        except Exception as e:
            consecutive_errors += 1
            log(f"        ERROR {type(e).__name__}: {e}")
            if consecutive_errors >= 5:
                log("        5 consecutive errors — aborting; cache preserved")
                return
            cache[k] = {"topic": topic, "course": t.get("course"), "url": None, "error": str(e), "fetched_at": int(time.time())}
            save_cache(cache)

        if i < len(todo):
            time.sleep(RATE_LIMIT_SLEEP + random.uniform(0, 5))

    log("=" * 60)
    log(f"DONE. Cache contains {len(cache)} entries.")


if __name__ == "__main__":
    main()
