"""
Run the PDF generator for all 10 Flyers practice tests + a combined answer key.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flyers_engine import build_exam_pdf, build_key_pdf
from flyers_content import TEST_1, TEST_2, TEST_3, TEST_4, TEST_5
from flyers_content_2 import TEST_6, TEST_7, TEST_8, TEST_9, TEST_10

ALL_TESTS = [TEST_1, TEST_2, TEST_3, TEST_4, TEST_5,
             TEST_6, TEST_7, TEST_8, TEST_9, TEST_10]

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

for t in ALL_TESTS:
    n = t['number']
    fn = os.path.join(OUT_DIR, f'Flyers_Practice_Test_{n:02d}_{t["theme"].replace(" & ", "_and_").replace(" ", "_")}.pdf')
    build_exam_pdf(t, fn)
    print(f'[OK] {fn}')

key_fn = os.path.join(OUT_DIR, 'Flyers_Practice_Tests_Answer_Keys.pdf')
build_key_pdf(ALL_TESTS, key_fn)
print(f'[OK] {key_fn}')
print('Done.')
