"""Helper: parse free-form answer strings from flyers_content into structured keys."""
import re

# Matches "<num> <value>" items; value starts with a non-digit char.
_NUM_ITEM_RE = re.compile(
    r'(?<![\w])(\d{1,2})\s+([^0-9][^,;\u2014]*?)(?=\s*(?:[,;]|\s\u2014|$))'
)


def parse_numbered(s):
    """Parse '1 a rabbit, 2 a shark, 3 a spider' into a contiguous list."""
    if not isinstance(s, str):
        return []
    main = s.split('\u2014')[0]
    out = {}
    for m in _NUM_ITEM_RE.finditer(main):
        n = int(m.group(1))
        if n < 1 or n > 20:
            continue
        val = m.group(2).strip().rstrip('.').strip()
        if not val:
            continue
        if val.startswith('(') and val.endswith(')'):
            continue
        alts = [v.strip() for v in val.split('/') if v.strip()]
        out[n] = alts if len(alts) > 1 else alts[0]
    if not out:
        return []
    result = []
    i = 1
    while i in out:
        result.append(out[i])
        i += 1
    return result


def parse_letters(s):
    """Parse '1 D, 2 F' or '1 A (live), 2 C (for)' -> ['D','F'] / ['A','C']"""
    if not isinstance(s, str):
        return []
    out = {}
    for m in re.finditer(r'(\d{1,2})\s+([A-H])\b', s):
        n = int(m.group(1))
        if 1 <= n <= 20:
            out[n] = m.group(2)
    if not out:
        return []
    result = []
    i = 1
    while i in out:
        result.append(out[i])
        i += 1
    return result


def extract_title(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'[Bb]est title[^A-Z]*([A-C])\b', s)
    return m.group(1) if m else None


def try_get_answers(t):
    out = {'rw': {}, 'listening': {}}
    ans = t.get('answers', {}) or {}
    rw_ans = ans.get('rw', {}) if isinstance(ans, dict) else {}

    for i, v in enumerate(parse_numbered(rw_ans.get('p1', ''))):
        out['rw']['rw_p1_' + str(i)] = v
    for i, v in enumerate(parse_letters(rw_ans.get('p2', ''))):
        out['rw']['rw_p2_' + str(i)] = v
    for i, v in enumerate(parse_numbered(rw_ans.get('p3', ''))):
        out['rw']['rw_p3_' + str(i)] = v
    title = extract_title(rw_ans.get('p3', ''))
    if title:
        out['rw']['rw_p3_title'] = title
    for i, v in enumerate(parse_letters(rw_ans.get('p4', ''))):
        out['rw']['rw_p4_' + str(i)] = v
    for i, v in enumerate(parse_numbered(rw_ans.get('p5', ''))):
        out['rw']['rw_p5_' + str(i)] = v

    p6_str = rw_ans.get('p6', '')
    if isinstance(p6_str, str):
        mm = re.search(r'\b1\s+\w', p6_str)
        if mm:
            p6_str = p6_str[mm.start():]
    for i, v in enumerate(parse_numbered(p6_str)):
        out['rw']['rw_p6_' + str(i)] = v

    lis = ans.get('listening', {}) if isinstance(ans, dict) else {}
    for p in range(1, 6):
        s = lis.get('p' + str(p), '')
        letters = parse_letters(s)
        nums = parse_numbered(s)
        items = letters if (len(letters) >= len(nums) and len(letters) >= 4) else nums
        for i, v in enumerate(items):
            out['listening']['lis_p' + str(p) + '_' + str(i)] = v
    return out
