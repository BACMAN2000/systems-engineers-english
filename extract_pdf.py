"""Extract text from Cambridge handbook PDFs."""
import pdfplumber
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

path = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

with pdfplumber.open(path) as pdf:
    print(f"# PDF: {path} — {len(pdf.pages)} pages\n")
    for i, page in enumerate(pdf.pages, start=1):
        if i < start or i > end:
            continue
        print(f"\n===== PAGE {i} =====")
        try:
            txt = page.extract_text() or ""
        except Exception as e:
            txt = f"[extract failed: {e}]"
        print(txt)
