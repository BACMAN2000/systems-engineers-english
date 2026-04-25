"""
Flyers Practice Tests — Web App Builder
========================================

Reads the 10 practice tests from flyers_content.py + flyers_content_2.py and
produces a single, self-contained HTML file: Flyers_Practice_App.html

The HTML has:
  - Test selector (Test 1..10)
  - Three tabs per test: Reading & Writing (7 parts), Listening (5 parts), Speaking (4 parts)
  - Inputs for every answer + a "Check answers" button that auto-grades
  - Inline SVG illustrations for each part (theme-aware)
  - <audio> tags pointing to ./audios/test_XX_partY.mp3 (generate with generate_audios.py)

USAGE:
  python build_webapp.py
  # produces Flyers_Practice_App.html in the same folder

Deploy: drop Flyers_Practice_App.html next to the audios/ folder and open in any browser.
"""
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flyers_content import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5
from flyers_content_2 import TEST_6, TEST_7, TEST_8, TEST_9, TEST_10

ALL_TESTS = [TEST_1, TEST_2, TEST_3, TEST_4, TEST_5,
             TEST_6, TEST_7, TEST_8, TEST_9, TEST_10]

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(OUT_DIR, 'Flyers_Practice_App.html')


# ---------------------------------------------------------------------
# SVG illustration library — one generic illustration per theme.
# Simple, clean, child-friendly. Rendered inline for zero extra files.
# ---------------------------------------------------------------------
SVG_LIB = {
    'Animals & Pets': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#e0f2fe" rx="12"/>
  <circle cx="80" cy="110" r="35" fill="#fbbf24"/>
  <circle cx="70" cy="100" r="4" fill="#0f172a"/><circle cx="90" cy="100" r="4" fill="#0f172a"/>
  <path d="M70 118 Q80 126 90 118" stroke="#0f172a" stroke-width="2" fill="none"/>
  <polygon points="50,85 60,70 70,85" fill="#fbbf24"/><polygon points="90,85 100,70 110,85" fill="#fbbf24"/>
  <ellipse cx="220" cy="120" rx="50" ry="30" fill="#a3e635"/>
  <circle cx="220" cy="90" r="25" fill="#a3e635"/>
  <circle cx="212" cy="88" r="3" fill="#0f172a"/><circle cx="228" cy="88" r="3" fill="#0f172a"/>
  <path d="M215 98 Q220 102 225 98" stroke="#0f172a" stroke-width="2" fill="none"/>
</svg>''',
    'School & Learning': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#fef3c7" rx="12"/>
  <rect x="40" y="60" width="240" height="90" fill="#1e40af" rx="6"/>
  <rect x="50" y="70" width="220" height="70" fill="#1e3a8a"/>
  <text x="160" y="110" text-anchor="middle" fill="#fff" font-size="24" font-family="sans-serif">A B C</text>
  <rect x="100" y="155" width="40" height="8" fill="#92400e"/>
  <rect x="180" y="155" width="40" height="8" fill="#92400e"/>
</svg>''',
    'Food & Drink': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#fee2e2" rx="12"/>
  <ellipse cx="100" cy="120" rx="50" ry="45" fill="#f87171"/>
  <path d="M100 75 Q108 65 115 75" stroke="#16a34a" stroke-width="4" fill="none"/>
  <rect x="180" y="80" width="100" height="60" fill="#fde68a" rx="8"/>
  <rect x="180" y="95" width="100" height="8" fill="#78350f"/>
  <rect x="180" y="115" width="100" height="8" fill="#dc2626"/>
</svg>''',
    'Family & Home': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#ede9fe" rx="12"/>
  <rect x="70" y="80" width="180" height="80" fill="#fbbf24"/>
  <polygon points="60,80 160,30 260,80" fill="#dc2626"/>
  <rect x="145" y="110" width="30" height="50" fill="#78350f"/>
  <rect x="90" y="95" width="30" height="30" fill="#38bdf8"/>
  <rect x="200" y="95" width="30" height="30" fill="#38bdf8"/>
</svg>''',
    'Sports & Hobbies': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#dcfce7" rx="12"/>
  <circle cx="100" cy="100" r="40" fill="#fff" stroke="#0f172a" stroke-width="2"/>
  <polygon points="100,75 110,95 100,110 90,95" fill="#0f172a"/>
  <polygon points="125,100 110,95 100,110" fill="#0f172a"/>
  <rect x="190" y="60" width="80" height="8" fill="#92400e"/>
  <circle cx="230" cy="120" r="18" fill="#f59e0b"/>
</svg>''',
    'Weather & Seasons': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#cffafe" rx="12"/>
  <circle cx="100" cy="70" r="30" fill="#fcd34d"/>
  <g stroke="#fcd34d" stroke-width="3">
    <line x1="100" y1="25" x2="100" y2="40"/><line x1="100" y1="100" x2="100" y2="115"/>
    <line x1="55" y1="70" x2="70" y2="70"/><line x1="130" y1="70" x2="145" y2="70"/>
  </g>
  <ellipse cx="220" cy="110" rx="50" ry="22" fill="#fff"/>
  <ellipse cx="200" cy="100" rx="30" ry="18" fill="#fff"/>
  <line x1="210" y1="140" x2="205" y2="160" stroke="#3b82f6" stroke-width="3"/>
  <line x1="230" y1="140" x2="225" y2="160" stroke="#3b82f6" stroke-width="3"/>
</svg>''',
    'Travel & Transport': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#e0e7ff" rx="12"/>
  <rect x="60" y="90" width="200" height="50" fill="#ef4444" rx="8"/>
  <rect x="70" y="100" width="40" height="25" fill="#fef3c7"/>
  <rect x="120" y="100" width="40" height="25" fill="#fef3c7"/>
  <rect x="170" y="100" width="40" height="25" fill="#fef3c7"/>
  <circle cx="100" cy="145" r="14" fill="#0f172a"/><circle cx="220" cy="145" r="14" fill="#0f172a"/>
</svg>''',
    'Jobs & Daily Routines': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#fef3c7" rx="12"/>
  <circle cx="160" cy="90" r="50" fill="#fff" stroke="#0f172a" stroke-width="4"/>
  <line x1="160" y1="90" x2="160" y2="55" stroke="#0f172a" stroke-width="4"/>
  <line x1="160" y1="90" x2="185" y2="90" stroke="#0f172a" stroke-width="3"/>
  <circle cx="160" cy="90" r="4" fill="#0f172a"/>
  <text x="160" y="165" text-anchor="middle" font-size="14" font-family="sans-serif" fill="#374151">My day</text>
</svg>''',
    'Clothes & Body': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#fce7f3" rx="12"/>
  <polygon points="160,40 120,80 140,80 140,140 180,140 180,80 200,80" fill="#60a5fa"/>
  <rect x="140" y="140" width="15" height="25" fill="#1e40af"/>
  <rect x="165" y="140" width="15" height="25" fill="#1e40af"/>
  <circle cx="160" cy="30" r="15" fill="#fbbf24"/>
</svg>''',
    'Holidays & Celebrations': '''<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg">
  <rect width="320" height="180" fill="#fef9c3" rx="12"/>
  <rect x="120" y="80" width="80" height="70" fill="#dc2626"/>
  <rect x="140" y="60" width="40" height="20" fill="#fbbf24"/>
  <circle cx="80" cy="50" r="12" fill="#f472b6"/>
  <circle cx="240" cy="50" r="12" fill="#a78bfa"/>
  <circle cx="60" cy="90" r="10" fill="#60a5fa"/>
  <circle cx="260" cy="90" r="10" fill="#34d399"/>
  <line x1="80" y1="62" x2="80" y2="150" stroke="#374151" stroke-width="1"/>
  <line x1="240" y1="62" x2="240" y2="150" stroke="#374151" stroke-width="1"/>
</svg>''',
}


def svg_for(theme):
    return SVG_LIB.get(theme, SVG_LIB['Animals & Pets'])



# ---------------------------------------------------------------------
# Per-word emoji icons. Rendered via Twemoji (consistent cartoon style)
# with native-emoji fallback if offline. Covers the vocabulary across all
# 10 tests so each Part 1 question gets a real cartoon image.
# ---------------------------------------------------------------------
P1_EMOJI = {
    # Test 1 — Animals & Pets
    'rabbit':'\U0001f407', 'shark':'\U0001f988', 'spider':'\U0001f577',
    'parrot':'\U0001f99c', 'squirrel':'\U0001f43f', 'kangaroo':'\U0001f998',
    'panda':'\U0001f43c', 'giraffe':'\U0001f992', 'butterfly':'\U0001f98b',
    'frog':'\U0001f438', 'dolphin':'\U0001f42c', 'peacock':'\U0001f99a',
    'crocodile':'\U0001f40a', 'bat':'\U0001f987', 'camel':'\U0001f42a',
    'cat':'\U0001f431', 'dog':'\U0001f436', 'horse':'\U0001f434',
    'cow':'\U0001f42e', 'sheep':'\U0001f411', 'pig':'\U0001f437',
    'mouse':'\U0001f42d', 'fish':'\U0001f41f', 'chicken':'\U0001f414',
    'elephant':'\U0001f418', 'lion':'\U0001f981', 'tiger':'\U0001f42f',
    'monkey':'\U0001f435', 'bear':'\U0001f43b', 'snake':'\U0001f40d',
    'whale':'\U0001f433', 'turtle':'\U0001f422', 'duck':'\U0001f986',
    'owl':'\U0001f989', 'penguin':'\U0001f427', 'koala':'\U0001f428',
    # Test 2 — School & Learning
    'ruler':'\U0001f4cf', 'chair':'\U0001fa91', 'playground':'\U0001f6dd',
    'teacher':'\U0001f9d1\u200d\U0001f3eb', 'dictionary':'\U0001f4d6',
    'uniform':'\U0001f454', 'timetable':'\U0001f4c5', 'library':'\U0001f4da',
    'calculator':'\U0001f9ee', 'rubber':'\U0001f9fd', 'eraser':'\U0001f9fd',
    'book':'\U0001f4d8', 'pencil':'\u270f\ufe0f', 'pen':'\U0001f58a\ufe0f',
    'school':'\U0001f3eb', 'student':'\U0001f9d1\u200d\U0001f393',
    'classroom':'\U0001f3eb', 'whiteboard':'\U0001f4cb',
    # Test 3 — Food & Drink
    'apple':'\U0001f34e', 'banana':'\U0001f34c', 'pizza':'\U0001f355',
    'sandwich':'\U0001f96a', 'milk':'\U0001f95b', 'water':'\U0001f4a7',
    'bread':'\U0001f35e', 'cheese':'\U0001f9c0', 'cake':'\U0001f370',
    'icecream':'\U0001f368', 'ice cream':'\U0001f368', 'rice':'\U0001f35a',
    'chocolate':'\U0001f36b', 'soup':'\U0001f35c', 'salad':'\U0001f957',
    'pasta':'\U0001f35d', 'burger':'\U0001f354', 'biscuit':'\U0001f36a',
    'orange':'\U0001f34a', 'strawberry':'\U0001f353', 'lemon':'\U0001f34b',
    'carrot':'\U0001f955', 'potato':'\U0001f954', 'tomato':'\U0001f345',
    'egg':'\U0001f95a', 'tea':'\U0001f375', 'coffee':'\u2615',
    'juice':'\U0001f964', 'lemonade':'\U0001f9c3',
    # Test 4 — Family & Home
    'kitchen':'\U0001f37d\ufe0f', 'bedroom':'\U0001f6cf\ufe0f',
    'bathroom':'\U0001f6c1', 'sofa':'\U0001f6cb\ufe0f', 'bed':'\U0001f6cf\ufe0f',
    'lamp':'\U0001f4a1', 'fridge':'\U0001f9ca', 'door':'\U0001f6aa',
    'window':'\U0001fa9f', 'mirror':'\U0001fa9e', 'mother':'\U0001f469',
    'father':'\U0001f468', 'sister':'\U0001f467', 'brother':'\U0001f466',
    'baby':'\U0001f476', 'grandmother':'\U0001f475', 'grandfather':'\U0001f474',
    'family':'\U0001f46a', 'house':'\U0001f3e0', 'garden':'\U0001f3e1',
    'roof':'\U0001f3da\ufe0f', 'garage':'\U0001f697',
    # Test 5 — Sports & Hobbies
    'football':'\u26bd', 'basketball':'\U0001f3c0', 'tennis':'\U0001f3be',
    'swimming':'\U0001f3ca', 'running':'\U0001f3c3', 'cycling':'\U0001f6b4',
    'dancing':'\U0001f483', 'drawing':'\U0001f58c\ufe0f', 'painting':'\U0001f3a8',
    'reading':'\U0001f4d6', 'guitar':'\U0001f3b8', 'piano':'\U0001f3b9',
    'chess':'\u265f\ufe0f', 'puzzle':'\U0001f9e9', 'singing':'\U0001f3a4',
    'kite':'\U0001fa81', 'bicycle':'\U0001f6b2', 'skateboard':'\U0001f6f9',
    # Test 6 — Weather & Seasons
    'sun':'\u2600\ufe0f', 'sunny':'\u2600\ufe0f', 'rain':'\U0001f327\ufe0f',
    'rainy':'\U0001f327\ufe0f', 'snow':'\u2744\ufe0f', 'snowy':'\U0001f328\ufe0f',
    'wind':'\U0001f4a8', 'windy':'\U0001f4a8', 'cloud':'\u2601\ufe0f',
    'cloudy':'\u2601\ufe0f', 'storm':'\u26c8\ufe0f', 'rainbow':'\U0001f308',
    'umbrella':'\u2602\ufe0f', 'spring':'\U0001f338', 'summer':'\u2600\ufe0f',
    'autumn':'\U0001f342', 'winter':'\u2744\ufe0f', 'snowman':'\u26c4',
    'thunder':'\u26a1', 'lightning':'\u26a1',
    # Test 7 — Travel & Transport
    'bus':'\U0001f68c', 'car':'\U0001f697', 'taxi':'\U0001f695',
    'train':'\U0001f686', 'plane':'\u2708\ufe0f', 'aeroplane':'\u2708\ufe0f',
    'helicopter':'\U0001f681', 'ship':'\U0001f6a2', 'boat':'\u26f5',
    'bike':'\U0001f6b2', 'motorbike':'\U0001f3cd\ufe0f', 'tractor':'\U0001f69c',
    'lorry':'\U0001f69a', 'truck':'\U0001f69a', 'rocket':'\U0001f680',
    'submarine':'\U0001f6a2', 'station':'\U0001f689', 'airport':'\U0001f6eb',
    'map':'\U0001f5fa\ufe0f', 'passport':'\U0001f6c2', 'suitcase':'\U0001f9f3',
    # Test 8 — Jobs & Daily Routines
    'doctor':'\U0001f9d1\u200d\u2695\ufe0f', 'nurse':'\U0001f9d1\u200d\u2695\ufe0f',
    'farmer':'\U0001f9d1\u200d\U0001f33e', 'cook':'\U0001f9d1\u200d\U0001f373',
    'chef':'\U0001f9d1\u200d\U0001f373', 'police':'\U0001f46e',
    'firefighter':'\U0001f9d1\u200d\U0001f692', 'pilot':'\U0001f9d1\u200d\u2708\ufe0f',
    'driver':'\U0001f9d1\u200d\U0001f3eb', 'singer':'\U0001f9d1\u200d\U0001f3a4',
    'artist':'\U0001f9d1\u200d\U0001f3a8', 'breakfast':'\U0001f95e',
    'lunch':'\U0001f96a', 'dinner':'\U0001f37d\ufe0f', 'sleep':'\U0001f634',
    'wakeup':'\u23f0', 'shower':'\U0001f6bf', 'brushteeth':'\U0001faa5',
    # Test 9 — Clothes & Body
    'tshirt':'\U0001f455', 't-shirt':'\U0001f455', 'shirt':'\U0001f455',
    'trousers':'\U0001f456', 'jeans':'\U0001f456', 'dress':'\U0001f457',
    'skirt':'\U0001f458', 'shoe':'\U0001f45f', 'shoes':'\U0001f45f',
    'socks':'\U0001f9e6', 'jacket':'\U0001f9e5', 'coat':'\U0001f9e5',
    'hat':'\U0001f9e2', 'cap':'\U0001f9e2', 'scarf':'\U0001f9e3',
    'gloves':'\U0001f9e4', 'glasses':'\U0001f453', 'watch':'\u231a',
    'bag':'\U0001f45c', 'eye':'\U0001f441\ufe0f', 'ear':'\U0001f442',
    'nose':'\U0001f443', 'mouth':'\U0001f444', 'hair':'\U0001f9b1',
    'tooth':'\U0001f9b7', 'hand':'\u270b', 'foot':'\U0001f9b6',
    'leg':'\U0001f9b5', 'arm':'\U0001f4aa',
    # Test 10 — Holidays & Celebrations
    'birthday':'\U0001f382', 'cake':'\U0001f382', 'present':'\U0001f381',
    'gift':'\U0001f381', 'balloon':'\U0001f388', 'party':'\U0001f389',
    'fireworks':'\U0001f386', 'candle':'\U0001f56f\ufe0f', 'christmas':'\U0001f384',
    'tree':'\U0001f384', 'halloween':'\U0001f383', 'pumpkin':'\U0001f383',
    'easter':'\U0001f430', 'wedding':'\U0001f492', 'flag':'\U0001f3f3\ufe0f',
    'crown':'\U0001f451', 'star':'\u2b50',
    # === Filled-in vocabulary for Tests 3-10 (missing entries) ===
    # Test 3 — Food
    'onion':'\U0001f9c5', 'cucumber':'\U0001f952', 'grape':'\U0001f347', 'grapes':'\U0001f347',
    'melon':'\U0001f348', 'watermelon':'\U0001f349', 'coconut':'\U0001f965', 'pineapple':'\U0001f34d',
    'avocado':'\U0001f951', 'mango':'\U0001f96d', 'pear':'\U0001f350', 'peach':'\U0001f351',
    'cherry':'\U0001f352', 'cherries':'\U0001f352', 'corn':'\U0001f33d', 'pepper':'\U0001fad1',
    'mushroom':'\U0001f344', 'broccoli':'\U0001f966', 'donut':'\U0001f369', 'doughnut':'\U0001f369',
    'honey':'\U0001f36f', 'popcorn':'\U0001f37f', 'pancake':'\U0001f95e', 'pancakes':'\U0001f95e',
    'butter':'\U0001f9c8', 'salt':'\U0001f9c2',
    # Test 4 — Family & Home
    'wardrobe':'\U0001f6aa', 'cushion':'\U0001fa91', 'carpet':'\U0001f9f6', 'curtain':'\U0001fa9f',
    'bath':'\U0001f6c1', 'cooker':'\U0001f373', 'oven':'\U0001f373', 'sink':'\U0001f6c0',
    'dishes':'\U0001f37d\ufe0f', 'plate':'\U0001f37d\ufe0f', 'cup':'\U0001f964', 'glass':'\U0001f95b',
    'bowl':'\U0001f963', 'spoon':'\U0001f944', 'fork':'\U0001f374', 'knife':'\U0001f52a',
    'aunt':'\U0001f469', 'uncle':'\U0001f468', 'cousin':'\U0001f9d1',
    # Test 5 — Sports & Hobbies
    'helmet':'\u26d1\ufe0f', 'racket':'\U0001f3f8', 'racquet':'\U0001f3f8', 'medal':'\U0001f3c5',
    'gym':'\U0001f3cb\ufe0f', 'whistle':'\U0001f3a3', 'swimmingpool':'\U0001f3ca',
    'pool':'\U0001f3ca', 'trainers':'\U0001f45f', 'sneakers':'\U0001f45f',
    'rope':'\U0001faa2', 'tenniscourt':'\U0001f3be', 'court':'\U0001f3c6',
    'goal':'\U0001f3af', 'ball':'\U0001f3c0', 'bat':'\U0001f3cf',
    'stadium':'\U0001f3df\ufe0f', 'badminton':'\U0001f3f8',
    # Test 6 — Weather
    'snowflakes':'\u2744\ufe0f', 'snowflake':'\u2744\ufe0f', 'raincoat':'\U0001f9e5',
    'wellies':'\U0001f97e', 'wellingtons':'\U0001f97e', 'sunglasses':'\U0001f576\ufe0f',
    'ice':'\U0001f9ca', 'sandals':'\U0001fa74', 'fog':'\U0001f32b\ufe0f', 'foggy':'\U0001f32b\ufe0f',
    'hot':'\U0001f525', 'cold':'\U0001f976', 'leaves':'\U0001f342', 'leaf':'\U0001f342',
    'flower':'\U0001f33c', 'flowers':'\U0001f33c',
    # Test 7 — Travel
    'ferry':'\U0001f6f3\ufe0f', 'ticket':'\U0001f3ab', 'tunnel':'\U0001f6e4\ufe0f',
    'tram':'\U0001f68b', 'underground':'\U0001f687', 'metro':'\U0001f687',
    'roundabout':'\U0001f504', 'trafficlight':'\U0001f6a6', 'traffic':'\U0001f6a6',
    'bridge':'\U0001f309', 'beach':'\U0001f3d6\ufe0f', 'mountain':'\u26f0\ufe0f',
    'forest':'\U0001f332', 'island':'\U0001f3dd\ufe0f', 'camera':'\U0001f4f7',
    'compass':'\U0001f9ed', 'tent':'\u26fa',
    # Test 8 — Jobs
    'dentist':'\U0001f9b7', 'waiter':'\U0001f9d1\u200d\U0001f37d\ufe0f', 'waitress':'\U0001f469\u200d\U0001f37d\ufe0f',
    'mechanic':'\U0001f9d1\u200d\U0001f527', 'journalist':'\U0001f4f0', 'librarian':'\U0001f9d1\u200d\U0001f4da',
    'scientist':'\U0001f9d1\u200d\U0001f52c', 'astronaut':'\U0001f9d1\u200d\U0001f680',
    'painter':'\U0001f9d1\u200d\U0001f3a8', 'photographer':'\U0001f4f7',
    'plumber':'\U0001f527', 'engineer':'\U0001f527', 'office':'\U0001f3e2',
    'shop':'\U0001f3ec', 'computer':'\U0001f4bb', 'phone':'\U0001f4f1',
    # Test 9 — Clothes & Body
    'pyjamas':'\U0001f6cc', 'pajamas':'\U0001f6cc', 'earrings':'\U0001f48d',
    'jumper':'\U0001f9f6', 'sweater':'\U0001f9f6', 'tie':'\U0001f454',
    'belt':'\U0001f9f5', 'shorts':'\U0001fa73', 'boots':'\U0001f97e',
    'pocket':'\U0001f455', 'zip':'\U0001f455', 'button':'\U0001f535',
    'finger':'\u261d\ufe0f', 'knee':'\U0001f9b5', 'shoulder':'\U0001f9be',
    'face':'\U0001f600', 'tongue':'\U0001f445', 'lips':'\U0001f444',
    # Test 10 — Holidays
    'card':'\U0001f48c', 'card':'\U0001f48c', 'costume':'\U0001f3ad',
    'guest':'\U0001f9d1', 'invitation':'\U0001f4e9', 'ribbon':'\U0001f380',
    'decorations':'\U0001f38a', 'decoration':'\U0001f38a', 'confetti':'\U0001f38a',
    'lantern':'\U0001f3ee', 'mask':'\U0001f637', 'witch':'\U0001f9d9\u200d\u2640\ufe0f',
    'ghost':'\U0001f47b', 'gift':'\U0001f381', 'present':'\U0001f381',
    'sparkler':'\U0001f387', 'parade':'\U0001f3c1', 'medalfair':'\U0001f3aa',
}

# ---------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------
HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Flyers Practice Tests — Cohasset</title>
<style>
  :root {
    --primary:#0a3a66; --accent:#f59e0b; --ok:#16a34a; --bad:#dc2626;
    --bg:#f8fafc; --card:#fff; --border:#e2e8f0; --text:#0f172a; --muted:#64748b;
  }
  * { box-sizing:border-box; }
  body { margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
         background:var(--bg); color:var(--text); }
  header { background:var(--primary); color:#fff; padding:16px 24px;
           display:flex; justify-content:space-between; align-items:center; }
  header h1 { margin:0; font-size:20px; font-weight:700; }
  header .sub { font-size:13px; opacity:.85; }
  .container { max-width:1300px; margin:0 auto; padding:20px;
                display:grid; grid-template-columns:280px 1fr; gap:24px;
                transition:grid-template-columns .25s ease; }
  .container.collapsed { grid-template-columns:0 1fr; gap:0; }
  .container.collapsed .sidebar { opacity:0; pointer-events:none;
                                  transform:translateX(-20px); transition:.2s; }
  .container.collapsed .main { max-width:1100px; margin:0 auto; }
  @media (max-width:860px) { .container { grid-template-columns:1fr; } }

  .menu-toggle { position:fixed; top:80px; left:14px; z-index:50;
                 background:var(--primary); color:#fff; border:0;
                 width:42px; height:42px; border-radius:10px; cursor:pointer;
                 box-shadow:0 4px 12px rgba(0,0,0,.15); font-size:18px;
                 display:none; align-items:center; justify-content:center; }
  .container.collapsed ~ .menu-toggle { display:flex; }
  .menu-toggle:hover { background:#0d4880; }
  .sidebar-close { position:absolute; top:0; right:6px; background:transparent;
                   border:0; cursor:pointer; color:var(--muted); font-size:20px;
                   padding:6px 10px; border-radius:6px; }
  .sidebar-close:hover { background:var(--bg); color:var(--primary); }

  /* Sidebar with test list */
  .sidebar { position:sticky; top:20px; align-self:start; transition:.2s; }
  .sidebar-title { font-size:12px; text-transform:uppercase; letter-spacing:.8px;
                   color:var(--muted); font-weight:700; margin:4px 8px 10px; }
  .test-list { display:flex; flex-direction:column; gap:6px; }
  .test-btn { display:flex; align-items:flex-start; gap:10px; padding:12px 14px;
              border:2px solid var(--border); border-radius:10px; background:#fff;
              cursor:pointer; font-size:14px; font-weight:600; color:var(--text);
              transition:.15s; text-align:left; width:100%; }
  .test-btn:hover { border-color:var(--primary); transform:translateX(2px); }
  .test-btn.active { background:var(--primary); color:#fff; border-color:var(--primary); }
  .test-btn .num { display:inline-flex; align-items:center; justify-content:center;
                   min-width:30px; height:30px; border-radius:50%; background:var(--bg);
                   color:var(--primary); font-weight:700; font-size:13px; flex-shrink:0; }
  .test-btn.active .num { background:rgba(255,255,255,.25); color:#fff; }
  .test-btn .meta { display:flex; flex-direction:column; gap:2px; line-height:1.3; }
  .test-btn .meta small { font-size:11px; font-weight:500; opacity:.7; }

  /* Tabs */
  .main { min-width:0; }
  .tabs { display:flex; border-bottom:2px solid var(--border); margin-bottom:20px; gap:4px; }
  .tab { padding:12px 18px; cursor:pointer; font-weight:600; color:var(--muted);
         border-bottom:3px solid transparent; margin-bottom:-2px; font-size:14px; }
  .tab:hover { color:var(--primary); }
  .tab.active { color:var(--primary); border-bottom-color:var(--accent); }

  /* Overview card */
  .overview { background:linear-gradient(135deg,#0a3a66,#1e5a9e); color:#fff;
              border-radius:16px; padding:28px; margin-bottom:20px; }
  .overview h2 { margin:0 0 4px; font-size:26px; }
  .overview .theme-tag { display:inline-block; background:rgba(255,255,255,.2);
                        padding:4px 12px; border-radius:999px; font-size:12px;
                        font-weight:600; margin-bottom:14px; letter-spacing:.3px; }
  .overview p { margin:8px 0; opacity:.92; line-height:1.5; }
  .overview .ov-svg { width:240px; float:right; margin:-10px 0 10px 20px; }
  .overview .ov-svg svg { border-radius:12px; }
  .ov-stats { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:18px; }
  .ov-stat { background:rgba(255,255,255,.12); padding:14px; border-radius:10px; }
  .ov-stat .big { font-size:24px; font-weight:700; }
  .ov-stat .lbl { font-size:12px; opacity:.85; }
  .ov-actions { display:flex; flex-wrap:wrap; gap:10px; margin-top:18px; }
  .ov-btn { padding:12px 20px; background:var(--accent); color:#fff; border:0;
            border-radius:8px; font-weight:700; cursor:pointer; font-size:14px; }
  .ov-btn:hover { background:#d97706; }
  .ov-btn.secondary { background:rgba(255,255,255,.2); }
  .ov-btn.secondary:hover { background:rgba(255,255,255,.3); }
  .ov-parts { display:grid; grid-template-columns:repeat(auto-fill,minmax(180px,1fr));
              gap:10px; margin-top:14px; }
  .ov-part { background:#fff; border:1px solid var(--border); border-radius:10px;
             padding:12px 14px; }
  .ov-part .p { font-size:11px; color:var(--muted); text-transform:uppercase; font-weight:700; }
  .ov-part .t { color:var(--text); font-weight:600; font-size:14px; margin-top:2px; }
  .hidden { display:none !important; }
  .card { background:var(--card); border:1px solid var(--border); border-radius:12px;
          padding:20px; margin-bottom:16px; box-shadow:0 1px 3px rgba(0,0,0,.04); }
  .part-title { color:var(--primary); font-size:16px; font-weight:700; margin:0 0 4px; }
  .part-instr { color:var(--muted); font-size:13px; margin:0 0 12px; font-style:italic; }
  .svg-wrap { width:100%; max-width:320px; margin:8px 0 16px; }
  .svg-wrap svg { width:100%; height:auto; display:block; border:1px solid var(--border); border-radius:12px; }
  .item { margin:10px 0; display:flex; flex-wrap:wrap; gap:8px; align-items:center; }
  .item label { flex:1; min-width:260px; }
  .item input[type=text] { padding:8px 12px; border:2px solid var(--border); border-radius:6px;
                           font-size:14px; min-width:120px; }
  .item input[type=text]:focus { outline:none; border-color:var(--primary); }
  .item input.ok { border-color:var(--ok); background:#f0fdf4; }
  .item input.bad { border-color:var(--bad); background:#fef2f2; }
  .correct-answer { color:var(--ok); font-size:12px; font-weight:600; margin-left:8px; }
  .word-bank { background:#f1f5f9; padding:10px 14px; border-radius:8px; margin:10px 0;
               font-size:14px; }
  .word-bank b { color:var(--primary); }
  .passage { background:#fffbeb; padding:14px; border-radius:8px; line-height:1.7;
             border-left:4px solid var(--accent); margin:10px 0; }
  .mc-options label { display:block; padding:6px 0; cursor:pointer; }
  .mc-options input[type=radio] { margin-right:8px; }
  audio { width:100%; margin:10px 0; }
  textarea { width:100%; min-height:120px; padding:12px; border:2px solid var(--border);
             border-radius:6px; font-family:inherit; font-size:14px; }
  .check-btn { background:var(--accent); color:#fff; border:0; padding:12px 28px;
               font-size:15px; font-weight:700; border-radius:8px; cursor:pointer;
               margin-top:10px; }
  .check-btn:hover { background:#d97706; }
  .score { font-size:18px; font-weight:700; margin:16px 0; padding:12px;
           border-radius:8px; background:#f0fdf4; color:var(--ok); }
  .score.low { background:#fef2f2; color:var(--bad); }
  /* Stacked question block: label on top, input below */
  .qblock { margin:14px 0; padding:12px; background:#fafbfc; border:1px solid var(--border); border-radius:8px; }
  .qblock label { display:block; margin-bottom:8px; font-weight:500; line-height:1.5; }
  .qblock input[type=text] { width:100%; max-width:420px; padding:10px 14px; border:2px solid var(--border); border-radius:6px; font-size:15px; }
  .qblock input[type=text]:focus { outline:none; border-color:var(--primary); }
  .qblock input.ok { border-color:var(--ok); background:#f0fdf4; }
  .qblock input.bad { border-color:var(--bad); background:#fef2f2; }
  .qblock select { width:100%; max-width:560px; padding:10px 14px; border:2px solid var(--border); border-radius:6px; font-size:15px; background:#fff; }
  .qblock select:focus { outline:none; border-color:var(--primary); }
  .qblock select.ok { border-color:var(--ok); background:#f0fdf4; }
  .qblock select.bad { border-color:var(--bad); background:#fef2f2; }

  /* Big word box */
  .word-box { background:#fff8e1; border:2px dashed var(--accent); border-radius:10px;
              padding:14px 18px; margin:12px 0; }
  .word-box .title { font-weight:700; color:var(--primary); margin-bottom:8px; font-size:14px;
                     text-transform:uppercase; letter-spacing:.5px; }
  .word-box .words { display:flex; flex-wrap:wrap; gap:10px; }
  .word-box .word { display:inline-block; padding:6px 12px; background:#fff; border:1px solid #fcd34d;
                    border-radius:999px; font-size:14px; color:#374151; }

  /* Per-question icon for Part 1 — Twemoji cartoon images */
  .qblock.with-icon { display:grid; grid-template-columns:90px 1fr; gap:14px; align-items:start; }
  .qblock .q-icon { width:90px; height:90px; background:linear-gradient(135deg,#f8fafc,#e2e8f0);
                    border:1px solid var(--border); border-radius:14px;
                    display:flex; align-items:center; justify-content:center;
                    box-shadow:0 2px 6px rgba(0,0,0,.05); overflow:hidden; }
  .qblock .q-icon img { width:72px; height:72px; display:block; object-fit:contain; }
  .qblock .q-icon .emoji { font-size:60px; line-height:1; user-select:none;
                           width:72px; height:72px; display:flex; align-items:center; justify-content:center;
                           font-family:"Apple Color Emoji","Segoe UI Emoji","Noto Color Emoji",sans-serif; }

  /* Sticky reference inside a part (word bank / passage) */
  .sticky-ref { position:sticky; top:10px; z-index:5;
                background:#fff; border:1px solid var(--border);
                border-radius:12px; padding:12px;
                box-shadow:0 4px 14px rgba(0,0,0,.06); margin-bottom:14px; }
  .sticky-ref .sticky-label { font-size:11px; text-transform:uppercase;
                              letter-spacing:.5px; color:var(--muted);
                              font-weight:700; margin-bottom:6px; }

  /* Bigger word bank for Part 3 */
  .word-box.big .words { gap:14px; justify-content:center; }
  .word-box.big .word { padding:10px 18px; font-size:18px; font-weight:600;
                        color:var(--primary); border-width:2px; }
  .word-box.centered { max-width:560px; margin-left:auto; margin-right:auto; text-align:center; }

  /* Part 4 stacked: number + options in one tight block */
  .mc-stacked { margin:12px 0; padding:12px; background:#fafbfc; border:1px solid var(--border); border-radius:8px; }
  .mc-stacked .mc-q { font-weight:700; color:var(--primary); margin-bottom:8px; }
  .mc-stacked label { display:block; padding:6px 10px; margin:4px 0; border-radius:6px; cursor:pointer; }
  .mc-stacked label:hover { background:#f1f5f9; }
  .mc-stacked input[type=radio] { margin-right:8px; }
  .speaking-prompt { background:#e0f2fe; border-left:4px solid #0284c7; padding:12px 16px;
                     border-radius:6px; margin:10px 0; }
</style>
</head>
<body>
<header>
  <div>
    <h1>Cambridge A2 Flyers — Practice Tests</h1>
    <div class="sub">10 complete tests · auto-graded · British English audio</div>
  </div>
  <div class="sub">Cohasset Platform</div>
</header>
<div class="container" id="container">
  <aside class="sidebar">
    <button class="sidebar-close" onclick="toggleSidebar(true)" title="Hide menu">&times;</button>
    <div class="sidebar-title">Practice Tests</div>
    <div class="test-list" id="testPicker"></div>
  </aside>
  <main class="main">
    <div class="tabs hidden" id="tabs">
      <div class="tab" data-tab="overview">Overview</div>
      <div class="tab" data-tab="rw">Reading &amp; Writing</div>
      <div class="tab" data-tab="listening">Listening</div>
      <div class="tab" data-tab="speaking">Speaking</div>
    </div>
    <div id="content"></div>
    <button class="check-btn hidden" id="checkBtn" onclick="checkAnswers()">Check my answers</button>
    <div id="scoreBox"></div>
  </main>
</div>
<button class="menu-toggle" onclick="toggleSidebar(false)" title="Show test menu">&#9776;</button>

<script>
const TESTS = __TESTS_JSON__;
const SVGS = __SVGS_JSON__;
const ICONS = __ICONS_JSON__;
let currentTest = -1;   // -1 = nothing selected (welcome screen)
let currentTab = 'overview';

// ---- helpers ----
function norm(s){ return (s||'').toString().trim().toLowerCase().replace(/[.,;:!?'"]/g,'').replace(/\s+/g,' '); }
function esc(s){ return (s||'').toString().replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

// Expand an answer key like "(some) water" into all acceptable variants.
// Rules:
//   "(some) water"        -> ["some water", "water"]                  (optional prefix)
//   "water (cold)"        -> ["water cold", "water"]                  (optional suffix)
//   "my (or our)"         -> ["my", "our"]                            (alternative)
//   "(maybe) yes (please)"-> ["maybe yes please", "yes please", "maybe yes", "yes"] (combinations)
function expandVariants(s) {
  if (!s) return [''];
  s = s.toString();
  // Find all parenthetical groups
  const re = /\(([^)]+)\)/g;
  const groups = []; let m;
  while ((m = re.exec(s)) !== null) {
    groups.push({start:m.index, end:m.index + m[0].length, text:m[1].trim()});
  }
  if (groups.length === 0) return [s.trim()];
  // Generate combinations: for each group, either include its content or skip it.
  // For "(or X)" -> alternative: include or replace base.
  const variants = new Set();
  const total = 1 << groups.length; // 2^n combinations
  for (let mask = 0; mask < total; mask++) {
    let out = '';
    let cursor = 0;
    for (let i = 0; i < groups.length; i++) {
      out += s.slice(cursor, groups[i].start);
      const include = (mask >> i) & 1;
      if (include) {
        const t = groups[i].text;
        // strip leading "or " for alternatives
        out += t.replace(/^or\s+/i, '');
      }
      cursor = groups[i].end;
    }
    out += s.slice(cursor);
    out = out.replace(/\s+/g, ' ').trim();
    if (out) variants.add(out);
  }
  // Also: special "X (or Y)" pattern -> add Y alone
  const orMatch = s.match(/^([^()]+)\s*\(or\s+([^)]+)\)\s*$/i);
  if (orMatch) {
    variants.add(orMatch[1].trim());
    variants.add(orMatch[2].trim());
  }
  return Array.from(variants);
}

function expandAll(arr) {
  const out = new Set();
  arr.forEach(a => expandVariants(a).forEach(v => out.add(v)));
  return Array.from(out);
}

function input(name, placeholder='') {
  return `<input type="text" data-name="${name}" placeholder="${placeholder}">`;
}
function radio(name, options) {
  return options.map(([k,v])=>
    `<label><input type="radio" name="${name}" value="${k}"> <b>${k}</b> — ${esc(v)}</label>`
  ).join('');
}

function renderRW(t) {
  const rw = t.rw; const ans = t.answers.rw;
  let html = '';
  // Part 1 — definitions → word
  html += `<div class="card"><h3 class="part-title">Part 1 — Match the definitions (7 questions)</h3>
    <p class="part-instr">Look at the pictures. Read the sentences. Write the correct word.</p>
    <div class="svg-wrap">${SVGS[t.theme]||''}</div>
    <div class="sticky-ref"><div class="sticky-label">Word Bank — stays visible while you scroll</div>
      <div class="word-box" style="margin:0;border:0;background:transparent;padding:0">
        <div class="words">${rw.p1.words.map(w=>`<span class="word">${esc(w)}</span>`).join('')}</div>
      </div></div>
    <div style="margin:12px 0"><b>Example:</b> It lives in the sea and is very clever. → <i>${rw.p1.example}</i></div>`;
  rw.p1.defs.forEach((d,i)=> {
    const expected = (ans && ans['rw_p1_'+i]) || '';
    const word = (Array.isArray(expected) ? expected[0] : expected).toString().toLowerCase()
                 .replace(/^a |^an |^the /, '').replace(/[.,;]/g,'').trim();
    const emoji = ICONS[word] || ICONS[word.replace(/\s+/g,'')] || '❓';
    // Build Twemoji CDN URL: codepoints joined with '-' (no fe0f for the basic set)
    const cps = Array.from(emoji).map(c=>c.codePointAt(0).toString(16))
                  .filter(c=>c!=='fe0f').join('-');
    const tw = `https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/${cps}.svg`;
    const icon = `<img src="${tw}" alt="${emoji}" loading="lazy" onerror="this.outerHTML='<span class=\'emoji\'>${emoji}</span>';">`;
    html += `<div class="qblock with-icon">
      <div class="q-icon">${icon}</div>
      <div><label><b>${i+1}.</b> ${esc(d)}</label>${input('rw_p1_'+i,'Write the word here')}</div>
    </div>`;
  });
  html += `</div>`;

  // Part 2 — dialogue matching
  html += `<div class="card"><h3 class="part-title">Part 2 — Complete the conversation (6 questions)</h3>
    <p class="part-instr">Read each line. Choose the best response from the dropdown below.</p>
    <div style="padding:10px;background:#f8fafc;border-radius:8px;margin-bottom:14px">
      <b>${esc(rw.p2.speakerA)}:</b> ${esc(rw.p2.line0_a)}<br>
      <b>${esc(rw.p2.speakerB)}:</b> (example) <i>${esc(rw.p2.line0_b_text)}</i> <span style="color:var(--muted)">[${rw.p2.line0_b_letter}]</span>
    </div>`;
  const p2opts = rw.p2.options.map(([k,v])=>`<option value="${k}">${k} — ${esc(v)}</option>`).join('');
  rw.p2.pairs.forEach((p,i)=> {
    html += `<div class="qblock">
      <label><b>${esc(rw.p2.speakerA)}:</b> ${esc(p.a)}</label>
      <label style="font-weight:400;color:var(--muted);margin-bottom:6px">${esc(rw.p2.speakerB)} answers:</label>
      <select data-name="rw_p2_${i}"><option value="">— choose a response —</option>${p2opts}</select>
    </div>`;
  });
  html += `</div>`;

  // Part 3 — fill gaps from word list + title
  html += `<div class="card"><h3 class="part-title">Part 3 — Read and complete (7 questions)</h3>
    <p class="part-instr">Read the story. Write the correct word from the box in each gap.</p>
    <div class="word-box big centered"><div class="title">Choose words from this list</div>
      <div class="words">${rw.p3.words.map(w=>`<span class="word">${esc(w)}</span>`).join('')}</div></div>
    <div class="passage">${esc(rw.p3.text).replace(/__\((\d+)\)__/g,(_,n)=>` ${input('rw_p3_'+(n-1))} `)}</div>
    <div class="mc-stacked" style="max-width:560px;margin:14px auto;text-align:left"><div class="mc-q">Choose the best title</div>${radio('rw_p3_title',rw.p3.title_choices)}</div></div>`;

  // Part 4 — multiple choice cloze
  html += `<div class="card"><h3 class="part-title">Part 4 — Choose the best word (6 questions)</h3>
    <p class="part-instr">${esc(rw.p4.title)}</p>
    <div class="sticky-ref"><div class="sticky-label">Reading Passage — stays visible while you answer</div>
      <div class="passage" style="margin:0;border-radius:8px">${esc(rw.p4.text).replace(/__\((\d+)\)__/g,(_,n)=>` <b style="color:var(--accent)">[${n}]</b> `)}</div></div>`;
  rw.p4.items.forEach((it,i)=> {
    const opts = Object.entries(it.options).map(([k,v])=>`<label><input type="radio" name="rw_p4_${i}" value="${k}"> <b>${k}</b> — ${esc(v)}</label>`).join('');
    html += `<div class="mc-stacked"><div class="mc-q">Question ${it.q}</div>${opts}</div>`;
  });
  html += `</div>`;

  // Part 5 — reading comprehension
  html += `<div class="card"><h3 class="part-title">Part 5 — Read and answer (7 questions)</h3>
    <p class="part-instr">${esc(rw.p5.title)} — write 1–4 words.</p>
    <div class="sticky-ref"><div class="sticky-label">Reading Passage — stays visible while you answer</div>
      <div class="passage" style="margin:0;border-radius:8px">${esc(rw.p5.text)}</div></div>
    <div style="margin:6px 0 14px"><b>Example:</b> ${esc(rw.p5.example_q)} → <i>${esc(rw.p5.example_a)}</i></div>`;
  rw.p5.questions.forEach((q,i)=>{
    html += `<div class="qblock"><label><b>${i+1}.</b> ${esc(q)}</label>${input('rw_p5_'+i,'Your answer (1-4 words)')}</div>`;
  });
  html += `</div>`;

  // Part 6 — short sentences / responses (often cloze)
  if (rw.p6) {
    html += `<div class="card"><h3 class="part-title">Part 6 — Complete the sentences (5 questions)</h3>
      <p class="part-instr">Read the story and write 1, 2 or 3 words in each gap.</p>
      <div class="passage">${esc(rw.p6.text||'').replace(/__\((\d+)\)__/g,(_,n)=>` ${input('rw_p6_'+(n-1))} `)}</div></div>`;
  }

  // Part 7 — writing
  if (rw.p7) {
    html += `<div class="card"><h3 class="part-title">Part 7 — Write a story (20+ words)</h3>
      <p class="part-instr">${esc(rw.p7.prompt||'Look at the pictures and write the story.')}</p>
      <textarea data-name="rw_p7" placeholder="Write your story here..."></textarea></div>`;
  }
  return html;
}

function renderListening(t) {
  const n = t.number.toString().padStart(2,'0');
  const L = t.listening;
  let html = '';
  for (let p=1; p<=5; p++) {
    const part = L['p'+p]; if(!part) continue;
    html += `<div class="card"><h3 class="part-title">Listening — Part ${p}</h3>
      <p class="part-instr">${esc(part.instr || 'Listen and answer. You will hear each part twice.')}</p>
      <audio controls src="audios/test_${n}_part${p}.mp3"></audio>`;
    if (Array.isArray(part.items)) {
      part.items.forEach((it,i)=>{
        html += `<div class="item"><label>${i+1}. ${esc(it.q||it.text||'')}</label>${input('lis_p'+p+'_'+i)}</div>`;
      });
    }
    html += `</div>`;
  }
  return html;
}

function renderSpeaking(t) {
  const S = t.speaking || {};
  let html = `<div class="card"><h3 class="part-title">Speaking — practice prompts</h3>
    <p class="part-instr">Record yourself on your phone and compare to the model answers in the PDF key.</p>`;
  for (let p=1; p<=4; p++) {
    const part = S['p'+p]; if(!part) continue;
    html += `<div class="speaking-prompt"><b>Part ${p}:</b> ${esc(part.prompt || JSON.stringify(part))}</div>`;
  }
  html += `</div>`;
  return html;
}

function renderWelcome() {
  return `<div class="overview">
    <h2>Cambridge A2 Flyers — Practice Tests</h2>
    <div class="theme-tag">10 complete tests · auto-graded</div>
    <p>Welcome. Pick a test from the list on the left to begin. Each test includes:</p>
    <div class="ov-parts">
      <div class="ov-part" style="background:rgba(255,255,255,.1);border-color:transparent;color:#fff"><div class="p" style="color:rgba(255,255,255,.7)">Reading &amp; Writing</div><div class="t" style="color:#fff">7 parts · ~40 min</div></div>
      <div class="ov-part" style="background:rgba(255,255,255,.1);border-color:transparent;color:#fff"><div class="p" style="color:rgba(255,255,255,.7)">Listening</div><div class="t" style="color:#fff">5 parts · ~25 min</div></div>
      <div class="ov-part" style="background:rgba(255,255,255,.1);border-color:transparent;color:#fff"><div class="p" style="color:rgba(255,255,255,.7)">Speaking</div><div class="t" style="color:#fff">4 parts · ~7 min</div></div>
    </div>
  </div>`;
}

function renderOverview(t) {
  const partsRW = [
    ['1','Match the definitions'],['2','Complete the conversation'],
    ['3','Read and complete'],['4','Choose the best word'],
    ['5','Read and answer'],['6','Complete the sentences'],['7','Write a story']
  ];
  const partsL = [['1','Listen & match people'],['2','Form filling'],['3','Match pictures'],['4','Multiple choice'],['5','Listen, colour & draw']];
  const partsS = [['1','Find the differences'],['2','Ask/answer info'],['3','Picture story'],['4','Personal questions']];
  return `<div class="overview">
    <div class="ov-svg">${SVGS[t.theme]||''}</div>
    <h2>Test ${t.number}</h2>
    <div class="theme-tag">${esc(t.theme)}</div>
    <p>A complete A2 Flyers practice test. Work through each section at your own pace, then press <b>Check my answers</b> to see your score.</p>
    <div class="ov-stats">
      <div class="ov-stat"><div class="big">16</div><div class="lbl">Reading &amp; Writing parts + items</div></div>
      <div class="ov-stat"><div class="big">25</div><div class="lbl">Listening questions</div></div>
      <div class="ov-stat"><div class="big">~70</div><div class="lbl">Total auto-graded items</div></div>
    </div>
    <div class="ov-actions">
      <button class="ov-btn" onclick="goTab('rw')">Start Reading &amp; Writing</button>
      <button class="ov-btn secondary" onclick="goTab('listening')">Start Listening</button>
      <button class="ov-btn secondary" onclick="goTab('speaking')">Speaking practice</button>
    </div>
    <div style="clear:both"></div>
  </div>
  <div class="card"><h3 class="part-title">Reading &amp; Writing parts</h3>
    <div class="ov-parts">${partsRW.map(([n,t])=>`<div class="ov-part"><div class="p">Part ${n}</div><div class="t">${t}</div></div>`).join('')}</div>
  </div>
  <div class="card"><h3 class="part-title">Listening parts</h3>
    <div class="ov-parts">${partsL.map(([n,t])=>`<div class="ov-part"><div class="p">Part ${n}</div><div class="t">${t}</div></div>`).join('')}</div>
  </div>
  <div class="card"><h3 class="part-title">Speaking parts</h3>
    <div class="ov-parts">${partsS.map(([n,t])=>`<div class="ov-part"><div class="p">Part ${n}</div><div class="t">${t}</div></div>`).join('')}</div>
  </div>`;
}

function goTab(tab) {
  currentTab = tab;
  document.querySelectorAll('.tab').forEach(x=>{
    x.classList.toggle('active', x.dataset.tab===tab);
  });
  render();
}

function render() {
  const tabs = document.getElementById('tabs');
  const checkBtn = document.getElementById('checkBtn');
  if (currentTest < 0) {
    tabs.classList.add('hidden');
    checkBtn.classList.add('hidden');
    document.getElementById('content').innerHTML = renderWelcome();
    document.getElementById('scoreBox').innerHTML = '';
    return;
  }
  tabs.classList.remove('hidden');
  const t = TESTS[currentTest];
  let html;
  if (currentTab==='overview')       { html = renderOverview(t);  checkBtn.classList.add('hidden'); }
  else if (currentTab==='rw')        { html = renderRW(t);         checkBtn.classList.remove('hidden'); }
  else if (currentTab==='listening') { html = renderListening(t);  checkBtn.classList.remove('hidden'); }
  else                               { html = renderSpeaking(t);   checkBtn.classList.remove('hidden'); }
  document.getElementById('content').innerHTML = html;
  document.getElementById('scoreBox').innerHTML = '';
  window.scrollTo({top:0,behavior:'smooth'});
}

function checkAnswers() {
  const t = TESTS[currentTest];
  if (currentTab==='speaking') {
    document.getElementById('scoreBox').innerHTML =
      '<div class="score">Speaking is self-graded. See the Answer Key PDF for model answers.</div>';
    return;
  }
  const key = currentTab==='rw' ? t.answers.rw : t.answers.listening;
  let correct = 0, total = 0;
  document.querySelectorAll('#content [data-name], #content input[type=radio]').forEach(el=>{
    const name = el.dataset.name || el.name;
    if (!name || !key || !(name in key)) return;
    let val;
    if (el.type==='radio') {
      if (!el.checked) return;
      val = el.value;
    } else {
      val = el.value;
    }
    if (el.tagName==='SELECT' && !val) return;
    total++;
    const expected = key[name];
    const arr = Array.isArray(expected) ? expected : [expected];
    const variants = expandAll(arr);
    const ok = variants.some(a => norm(a)===norm(val));
    if (el.type==='text' || el.tagName==='SELECT') {
      el.classList.remove('ok','bad');
      el.classList.add(ok?'ok':'bad');
      if (!ok) {
        let after = el.nextElementSibling;
        if (!after || !after.classList.contains('correct-answer')) {
          const s = document.createElement('span');
          s.className = 'correct-answer';
          // Show cleanest variant (drop parens) but keep alternatives readable
        const display = arr.map(a => (a||'').toString().replace(/\(or\s+([^)]+)\)/i,'/ $1').replace(/\(([^)]+)\)/g,'').replace(/\s+/g,' ').trim()).filter(Boolean).join(' / ');
        s.textContent = '→ ' + display;
          el.after(s);
        }
      }
    }
    if (ok) correct++;
  });
  // De-duplicate radio totals
  const box = document.getElementById('scoreBox');
  const pct = total? Math.round(100*correct/total) : 0;
  box.innerHTML = `<div class="score ${pct<60?'low':''}">Score: ${correct} / ${total} (${pct}%)</div>`;
}

// ---- init ----
function toggleSidebar(collapse) {
  const c = document.getElementById('container');
  if (collapse===undefined) collapse = !c.classList.contains('collapsed');
  c.classList.toggle('collapsed', collapse);
}

function init() {
  const picker = document.getElementById('testPicker');
  TESTS.forEach((t,i)=>{
    const b = document.createElement('button');
    b.className = 'test-btn';
    b.innerHTML = `<span class="num">${t.number}</span><span class="meta"><span>${esc(t.theme)}</span><small>Reading · Listening · Speaking</small></span>`;
    b.onclick = ()=>{
      currentTest = i;
      currentTab = 'overview';
      document.querySelectorAll('.test-btn').forEach(x=>x.classList.remove('active'));
      b.classList.add('active');
      document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('active', x.dataset.tab==='overview'));
      toggleSidebar(true);   // auto-collapse on selection
      render();
    };
    picker.appendChild(b);
  });
  document.querySelectorAll('.tab').forEach(tab=>{
    tab.onclick = ()=>{
      if (currentTest<0) return;
      document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
      tab.classList.add('active');
      currentTab = tab.dataset.tab;
      render();
    };
  });
  render();
}
init();
</script>
</body>
</html>
'''

# ---------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------
from parse_answers import try_get_answers


def build():
    serialized = []
    for t in ALL_TESTS:
        item = {
            'number': t['number'],
            'theme': t['theme'],
            'rw': t.get('rw', {}),
            'listening': t.get('listening', {}),
            'speaking': t.get('speaking', {}),
            'answers': try_get_answers(t),
        }
        serialized.append(item)

    html = HTML.replace('__TESTS_JSON__', json.dumps(serialized, ensure_ascii=False))
    html = html.replace('__SVGS_JSON__', json.dumps(SVG_LIB, ensure_ascii=False))
    html = html.replace('__ICONS_JSON__', json.dumps(P1_EMOJI, ensure_ascii=False))
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    size_kb = os.path.getsize(OUT_FILE) / 1024
    print('[OK] Built %s  (%.1f KB)' % (OUT_FILE, size_kb))
    print('     Open it in a browser. Place ./audios/ next to it for Listening playback.')


if __name__ == '__main__':
    build()
