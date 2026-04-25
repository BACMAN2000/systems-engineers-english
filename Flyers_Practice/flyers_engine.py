"""
Flyers Practice Test PDF Generator
Generates professional A2 Flyers practice tests following the official Cambridge format.
All content is original; only the format/structure follows public Cambridge specifications.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable, ListFlowable, ListItem
)
from reportlab.pdfgen import canvas as rl_canvas

# ------------------- STYLES -------------------

def build_styles():
    s = getSampleStyleSheet()
    styles = {}
    styles['title'] = ParagraphStyle(
        'TitleX', parent=s['Title'], fontName='Helvetica-Bold',
        fontSize=22, alignment=TA_CENTER, textColor=colors.HexColor('#0a3a66'),
        spaceAfter=6
    )
    styles['subtitle'] = ParagraphStyle(
        'SubX', parent=s['Normal'], fontName='Helvetica',
        fontSize=13, alignment=TA_CENTER, textColor=colors.HexColor('#444444'),
        spaceAfter=14
    )
    styles['part'] = ParagraphStyle(
        'PartX', parent=s['Heading2'], fontName='Helvetica-Bold',
        fontSize=14, textColor=colors.white,
        backColor=colors.HexColor('#0a3a66'),
        borderPadding=6, leftIndent=0, spaceBefore=10, spaceAfter=6,
    )
    styles['instr'] = ParagraphStyle(
        'InstrX', parent=s['Italic'], fontName='Helvetica-Oblique',
        fontSize=10.5, textColor=colors.HexColor('#222222'),
        spaceAfter=8, leading=14
    )
    styles['body'] = ParagraphStyle(
        'BodyX', parent=s['Normal'], fontName='Helvetica',
        fontSize=11, leading=16, spaceAfter=4
    )
    styles['bodyJ'] = ParagraphStyle(
        'BodyJ', parent=s['Normal'], fontName='Helvetica',
        fontSize=11, leading=16, alignment=TA_JUSTIFY, spaceAfter=4
    )
    styles['q'] = ParagraphStyle(
        'QX', parent=s['Normal'], fontName='Helvetica',
        fontSize=11, leading=16, leftIndent=16, spaceAfter=4
    )
    styles['example'] = ParagraphStyle(
        'ExX', parent=s['Normal'], fontName='Helvetica-Oblique',
        fontSize=10.5, leading=14, textColor=colors.HexColor('#555555'),
        spaceAfter=6
    )
    styles['box'] = ParagraphStyle(
        'BoxX', parent=s['Normal'], fontName='Helvetica',
        fontSize=11, leading=18, alignment=TA_CENTER,
        backColor=colors.HexColor('#f2f2f2'),
        borderColor=colors.HexColor('#999999'), borderWidth=0.6,
        borderPadding=8, spaceAfter=10
    )
    styles['small'] = ParagraphStyle(
        'SmallX', parent=s['Normal'], fontName='Helvetica',
        fontSize=9.5, leading=12, textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER, spaceBefore=4
    )
    styles['story'] = ParagraphStyle(
        'StoryX', parent=s['Normal'], fontName='Helvetica',
        fontSize=11, leading=17, alignment=TA_JUSTIFY, spaceAfter=6,
        leftIndent=6, rightIndent=6
    )
    styles['sectionH'] = ParagraphStyle(
        'SectH', parent=s['Heading1'], fontName='Helvetica-Bold',
        fontSize=16, alignment=TA_CENTER,
        textColor=colors.HexColor('#0a3a66'),
        spaceBefore=6, spaceAfter=10
    )
    styles['keyH'] = ParagraphStyle(
        'KeyH', parent=s['Heading2'], fontName='Helvetica-Bold',
        fontSize=13, textColor=colors.HexColor('#0a3a66'),
        spaceBefore=8, spaceAfter=4
    )
    return styles


# ------------------- PAGE FURNITURE -------------------

def make_header_footer(test_number, test_title):
    def _draw(canvas_obj, doc):
        canvas_obj.saveState()
        # Top bar
        canvas_obj.setFillColor(colors.HexColor('#0a3a66'))
        canvas_obj.rect(0, A4[1] - 1.2*cm, A4[0], 1.2*cm, fill=1, stroke=0)
        canvas_obj.setFillColor(colors.white)
        canvas_obj.setFont('Helvetica-Bold', 11)
        canvas_obj.drawString(1.5*cm, A4[1] - 0.8*cm, 'A2 FLYERS – Practice Test')
        canvas_obj.drawRightString(A4[0] - 1.5*cm, A4[1] - 0.8*cm, test_title)

        # Footer
        canvas_obj.setFillColor(colors.HexColor('#666666'))
        canvas_obj.setFont('Helvetica', 9)
        canvas_obj.drawString(1.5*cm, 1*cm, f'Flyers Practice – Test {test_number}')
        canvas_obj.drawRightString(A4[0] - 1.5*cm, 1*cm, f'Page {doc.page}')
        canvas_obj.setStrokeColor(colors.HexColor('#cccccc'))
        canvas_obj.line(1.5*cm, 1.3*cm, A4[0] - 1.5*cm, 1.3*cm)
        canvas_obj.restoreState()
    return _draw


def key_header_footer(canvas_obj, doc):
    canvas_obj.saveState()
    canvas_obj.setFillColor(colors.HexColor('#6a1b9a'))
    canvas_obj.rect(0, A4[1] - 1.2*cm, A4[0], 1.2*cm, fill=1, stroke=0)
    canvas_obj.setFillColor(colors.white)
    canvas_obj.setFont('Helvetica-Bold', 11)
    canvas_obj.drawString(1.5*cm, A4[1] - 0.8*cm, 'A2 FLYERS – Answer Keys')
    canvas_obj.drawRightString(A4[0] - 1.5*cm, A4[1] - 0.8*cm, 'Teacher\u2019s copy')
    canvas_obj.setFillColor(colors.HexColor('#666666'))
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.drawRightString(A4[0] - 1.5*cm, 1*cm, f'Page {doc.page}')
    canvas_obj.setStrokeColor(colors.HexColor('#cccccc'))
    canvas_obj.line(1.5*cm, 1.3*cm, A4[0] - 1.5*cm, 1.3*cm)
    canvas_obj.restoreState()


# ------------------- BUILDING BLOCKS -------------------

def part_header(styles, label, title):
    return Paragraph(f'{label} &nbsp; &nbsp; {title}', styles['part'])


def instructions(styles, text):
    return Paragraph(text, styles['instr'])


def example_line(styles, text):
    return Paragraph(f'<b>Example:</b> {text}', styles['example'])


def word_box(styles, words):
    # Render a shaded word bank
    text = ' &nbsp; &nbsp; '.join(words)
    return Paragraph(text, styles['box'])


def numbered_qs(styles, items, start=1, answer_line=True):
    """items: list of strings (the question text)."""
    flows = []
    for i, q in enumerate(items, start=start):
        suffix = ' ' + ('_' * 30) if answer_line else ''
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {q}{suffix}', styles['q']))
    return flows


def mcq_block(styles, items, start=1):
    """items: list of dicts {'q': str, 'options': {'A':..,'B':..,'C':..}}."""
    flows = []
    for i, it in enumerate(items, start=start):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {it["q"]}', styles['q']))
        for letter in ['A', 'B', 'C']:
            flows.append(Paragraph(
                f'&nbsp;&nbsp;&nbsp;&nbsp; ( &nbsp; ) &nbsp; <b>{letter}</b> &nbsp; {it["options"][letter]}',
                styles['q']))
        flows.append(Spacer(1, 2))
    return flows


def picture_placeholder(styles, caption, w_cm=14, h_cm=5):
    """Create a bordered box representing a picture with a caption inside."""
    data = [[Paragraph(f'<i>[ PICTURE: {caption} ]</i>', styles['body'])]]
    t = Table(data, colWidths=[w_cm * cm], rowHeights=[h_cm * cm])
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.8, colors.HexColor('#888888')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fafafa')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    return t


def picture_row(styles, captions, total_w_cm=17):
    """Row of picture placeholders."""
    n = len(captions)
    col = total_w_cm / n
    data = [[Paragraph(f'<i>[ {c} ]</i>', styles['body']) for c in captions]]
    t = Table(data, colWidths=[col * cm]*n, rowHeights=[3.8*cm])
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.6, colors.HexColor('#888888')),
        ('INNERGRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#aaaaaa')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#fafafa')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def two_col_list(styles, left, right, header_left='', header_right=''):
    """left and right are lists of equal length - rendered as two-column table."""
    rows = []
    if header_left or header_right:
        rows.append([Paragraph(f'<b>{header_left}</b>', styles['body']),
                     Paragraph(f'<b>{header_right}</b>', styles['body'])])
    for l, r in zip(left, right):
        rows.append([Paragraph(l, styles['body']), Paragraph(r, styles['body'])])
    t = Table(rows, colWidths=[6*cm, 11*cm])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('LINEBELOW', (0, 0), (-1, 0), 0.4, colors.grey),
    ]))
    return t


# ------------------- PART BUILDERS -------------------

def build_rw_part1(styles, data):
    """Part 1: 10 words -> match with definitions (15 definitions including extras)."""
    flows = [part_header(styles, 'Part 1', 'Read the definitions and write the correct words.')]
    flows.append(instructions(styles,
        'Look at the words. Read the definitions. Which word matches each definition? '
        'There is one example and 5 extra definitions you will not need.'))
    flows.append(word_box(styles, data['words']))
    flows.append(example_line(styles, f'an animal that lives in water and has fins &nbsp;&nbsp;→&nbsp; <b>{data["example"]}</b>'))
    items = []
    for i, d in enumerate(data['defs'], start=1):
        items.append(f'{d} &nbsp; ................................................')
    flows.extend(numbered_qs(styles, items, start=1, answer_line=False))
    return flows


def build_rw_part2(styles, data):
    """Part 2: Dialogue completion - 6 gaps, choose from 8 options (with example)."""
    flows = [part_header(styles, 'Part 2', 'Complete the dialogue.')]
    flows.append(instructions(styles,
        'Read the conversation. What does the second person say? Choose the correct letter (A\u2013H). '
        'There is one example.'))
    # Dialogue as formatted text
    flows.append(Paragraph(f'<b>{data["speakerA"]}:</b> {data["line0_a"]}', styles['body']))
    flows.append(Paragraph(f'<b>{data["speakerB"]}:</b> (example) &nbsp; <b>{data["line0_b_letter"]}</b> – {data["line0_b_text"]}', styles['example']))
    for i, pair in enumerate(data['pairs'], start=1):
        flows.append(Paragraph(f'<b>{data["speakerA"]}:</b> {pair["a"]}', styles['body']))
        flows.append(Paragraph(f'<b>{data["speakerB"]}:</b> &nbsp; <b>{i}</b> ___________________', styles['body']))
    flows.append(Spacer(1, 6))
    flows.append(Paragraph('<b>Options:</b>', styles['body']))
    for letter, text in data['options']:
        flows.append(Paragraph(f'&nbsp; <b>{letter}</b> &nbsp; {text}', styles['q']))
    return flows


def build_rw_part3(styles, data):
    """Part 3: Text with 6 gaps (word bank of 8) + choose best title from 3 options."""
    flows = [part_header(styles, 'Part 3', 'Read the story and write the missing words.')]
    flows.append(instructions(styles,
        'Read the text. Choose one word from the box and write it next to numbers 1\u20136. '
        'There is one example. At the end, tick (✓) the best name for the story.'))
    flows.append(word_box(styles, data['words']))
    flows.append(Paragraph(f'<b>{data["title"]}</b>', styles['body']))
    flows.append(Paragraph(data['text'], styles['story']))
    flows.append(Spacer(1, 6))
    flows.append(Paragraph('<b>Now choose the best name for this story.</b>', styles['body']))
    for letter, opt in data['title_choices']:
        flows.append(Paragraph(f'&nbsp; ( &nbsp; ) &nbsp; <b>{letter}</b> &nbsp; {opt}', styles['q']))
    return flows


def build_rw_part4(styles, data):
    """Part 4: Gap-fill factual text, 6 gaps, A/B/C options for each."""
    flows = [part_header(styles, 'Part 4', 'Read the text. Choose the right word for each space.')]
    flows.append(instructions(styles,
        'Read the text. For each number, choose A, B or C.'))
    flows.append(Paragraph(f'<b>{data["title"]}</b>', styles['body']))
    flows.append(Paragraph(data['text'], styles['story']))
    flows.append(Spacer(1, 4))
    flows.extend(mcq_block(styles, data['items'], start=1))
    return flows


def build_rw_part5(styles, data):
    """Part 5: Story + 7 comprehension questions (short answers)."""
    flows = [part_header(styles, 'Part 5', 'Read the story and write 1, 2, 3 or 4 words to complete the sentences.')]
    flows.append(instructions(styles,
        'Read the story and then answer the questions below. You only need to write short answers (1\u20134 words).'))
    flows.append(Paragraph(f'<b>{data["title"]}</b>', styles['body']))
    flows.append(Paragraph(data['text'], styles['story']))
    flows.append(Spacer(1, 4))
    flows.append(example_line(styles, f'{data["example_q"]} &nbsp;→&nbsp; <b>{data["example_a"]}</b>'))
    items = [q + ' &nbsp; ' + ('_' * 30) for q in data['questions']]
    flows.extend(numbered_qs(styles, items, start=1, answer_line=False))
    return flows


def build_rw_part6(styles, data):
    """Part 6: Text with 6 one-word gaps (no options given)."""
    flows = [part_header(styles, 'Part 6', 'Write one word for each space.')]
    flows.append(instructions(styles,
        'Read the text and write the missing words. Write ONE word on each line. '
        'There is one example.'))
    flows.append(Paragraph(f'<b>{data["title"]}</b>', styles['body']))
    flows.append(Paragraph(data['text'], styles['story']))
    flows.append(Spacer(1, 4))
    flows.append(example_line(styles, f'(example) &nbsp; <b>{data["example"]}</b>'))
    items = ['________________________' for _ in data['answers']]
    for i, _ in enumerate(data['answers'], start=1):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; ________________________', styles['q']))
    return flows


def build_rw_part7(styles, data):
    """Part 7: Write a short story (20+ words) based on 3 pictures."""
    flows = [part_header(styles, 'Part 7', 'Look at the pictures and write a short story.')]
    flows.append(instructions(styles,
        'Look at the three pictures. Write the story shown in the pictures. '
        'Write 20 or more words.'))
    flows.append(picture_row(styles, [
        f'Picture 1: {data["p1"]}',
        f'Picture 2: {data["p2"]}',
        f'Picture 3: {data["p3"]}',
    ]))
    flows.append(Spacer(1, 6))
    flows.append(Paragraph(f'<b>Title:</b> {data["title"]}', styles['body']))
    for _ in range(8):
        flows.append(Paragraph(
            '_____________________________________________________________________________________',
            styles['body']))
    return flows


# ----- Listening builders -----

def build_list_part1(styles, data):
    """Part 1: Match 5 names with people in a picture. Example + 5 tasks."""
    flows = [part_header(styles, 'Part 1', 'Listen and draw lines.')]
    flows.append(instructions(styles,
        'There are people in the picture. Listen carefully and draw a line from each name to the correct person. '
        'There is one example.'))
    flows.append(picture_placeholder(styles,
        data['scene'], w_cm=17, h_cm=6.5))
    flows.append(Paragraph('<b>Names:</b>', styles['body']))
    names_text = ' &nbsp; • &nbsp; '.join([data['example_name']] + data['names'])
    flows.append(Paragraph(names_text, styles['body']))
    flows.append(Paragraph(f'<i>(Example name: {data["example_name"]})</i>', styles['example']))
    return flows


def build_list_part2(styles, data):
    """Part 2: Gap-fill 5 notes from conversation. Example included."""
    flows = [part_header(styles, 'Part 2', 'Listen and write.')]
    flows.append(instructions(styles, 'Listen to the conversation. Write one word or a number or a date or a time.'))
    flows.append(Paragraph(f'<b>{data["heading"]}</b>', styles['body']))
    flows.append(example_line(styles, f'{data["example_label"]}: &nbsp;&nbsp; <b>{data["example"]}</b>'))
    for i, label in enumerate(data['labels'], start=1):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {label}: &nbsp; ________________________',
                               styles['q']))
    return flows


def build_list_part3(styles, data):
    """Part 3: Match 5 items (e.g. days / people) to 5 pictures/options (from 8)."""
    flows = [part_header(styles, 'Part 3', 'Listen and match.')]
    flows.append(instructions(styles,
        f'{data["instruction"]} Choose a letter (A\u2013H) for each one. There is one example.'))
    flows.append(example_line(styles,
        f'{data["example_item"]} &nbsp;→&nbsp; <b>{data["example_letter"]}</b>'))
    # Items
    flows.append(Paragraph('<b>Items:</b>', styles['body']))
    for i, item in enumerate(data['items'], start=1):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {item} &nbsp;&nbsp; _____', styles['q']))
    flows.append(Spacer(1, 4))
    flows.append(Paragraph('<b>Options:</b>', styles['body']))
    for letter, opt in data['options']:
        flows.append(Paragraph(f'&nbsp; <b>{letter}</b> &nbsp; {opt}', styles['q']))
    return flows


def build_list_part4(styles, data):
    """Part 4: 5 multiple-choice questions. Each has 3 picture options (A/B/C)."""
    flows = [part_header(styles, 'Part 4', 'Listen and tick (✓) the box.')]
    flows.append(instructions(styles,
        'Listen to the five short conversations. There is one question for each conversation. '
        'Put a tick in the correct box.'))
    for i, it in enumerate(data['items'], start=1):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {it["q"]}', styles['q']))
        flows.append(picture_row(styles, [
            f"A: {it['A']}", f"B: {it['B']}", f"C: {it['C']}",
        ], total_w_cm=16))
        flows.append(Spacer(1, 4))
    return flows


def build_list_part5(styles, data):
    """Part 5: Listen and colour/write (5 instructions + example)."""
    flows = [part_header(styles, 'Part 5', 'Listen, colour and write.')]
    flows.append(instructions(styles,
        'There is one picture. Listen and colour and write. There is one example.'))
    flows.append(picture_placeholder(styles, data['scene'], w_cm=17, h_cm=7))
    flows.append(example_line(styles, f'The first instruction is an example: {data["example"]}'))
    flows.append(Paragraph('<b>Student instructions summary (teacher reads script):</b>', styles['body']))
    for i, it in enumerate(data['items'], start=1):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {it}', styles['q']))
    return flows


# ----- Speaking builders -----

def build_speaking(styles, data):
    flows = [Paragraph('Speaking Paper', styles['sectionH'])]
    flows.append(Paragraph(
        'The Speaking test lasts about 7\u20139 minutes. The examiner has two sets of cards. '
        'This practice material includes the prompts for both examiner and student.',
        styles['instr']))

    # Part 1 - Find the Differences
    flows.append(part_header(styles, 'Part 1', 'Find the Differences'))
    flows.append(instructions(styles,
        'The examiner shows the candidate two pictures that look similar but have 4 differences. '
        'The candidate describes the differences.'))
    flows.append(Paragraph('<b>Examiner\u2019s picture:</b>', styles['body']))
    flows.append(picture_placeholder(styles, data['p1_ex']))
    flows.append(Paragraph('<b>Candidate\u2019s picture:</b>', styles['body']))
    flows.append(picture_placeholder(styles, data['p1_cand']))
    flows.append(Paragraph('<b>Four differences to find:</b>', styles['body']))
    for i, d in enumerate(data['p1_diffs'], start=1):
        flows.append(Paragraph(f'&nbsp;{i}. {d}', styles['q']))

    # Part 2 - Information Exchange
    flows.append(PageBreak())
    flows.append(part_header(styles, 'Part 2', 'Information Exchange'))
    flows.append(instructions(styles,
        'Two cards with information about similar topics. The candidate and examiner ask each other questions '
        'to complete the missing information.'))
    flows.append(Paragraph(f'<b>Candidate\u2019s card – {data["p2_topic"]}</b>', styles['body']))
    flows.append(Paragraph(data['p2_cand_card'], styles['story']))
    flows.append(Paragraph('<b>Questions the candidate must ask:</b>', styles['body']))
    for q in data['p2_cand_qs']:
        flows.append(Paragraph(f'• {q}', styles['q']))
    flows.append(Spacer(1, 6))
    flows.append(Paragraph(f'<b>Examiner\u2019s card – {data["p2_topic"]}</b>', styles['body']))
    flows.append(Paragraph(data['p2_ex_card'], styles['story']))
    flows.append(Paragraph('<b>Questions the examiner asks:</b>', styles['body']))
    for q in data['p2_ex_qs']:
        flows.append(Paragraph(f'• {q}', styles['q']))

    # Part 3 - Picture Story
    flows.append(PageBreak())
    flows.append(part_header(styles, 'Part 3', 'Picture Story'))
    flows.append(instructions(styles,
        'The examiner shows the candidate four pictures that tell a short story. '
        'The examiner describes the first picture. The candidate describes the other three.'))
    flows.append(Paragraph(f'<b>Story title:</b> {data["p3_title"]}', styles['body']))
    flows.append(picture_row(styles, [
        f'1 (examiner): {data["p3_p1"]}',
        f'2: {data["p3_p2"]}',
        f'3: {data["p3_p3"]}',
        f'4: {data["p3_p4"]}',
    ], total_w_cm=17))
    flows.append(Paragraph(f'<b>Examiner begins:</b> "{data["p3_examiner_open"]}"', styles['body']))

    # Part 4 - Personal Questions
    flows.append(part_header(styles, 'Part 4', 'Personal Questions'))
    flows.append(instructions(styles,
        'The examiner asks the candidate some simple questions about their life, family, school, friends and hobbies.'))
    for i, q in enumerate(data['p4_questions'], start=1):
        flows.append(Paragraph(f'<b>{i}.</b> &nbsp; {q}', styles['q']))
    return flows


# ------------------- WHOLE EXAM BUILDER -------------------

def build_exam_pdf(test_data, out_path):
    styles = build_styles()
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        title=f'Flyers Practice Test {test_data["number"]}'
    )
    story = []

    # Cover / title
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(f'Cambridge A2 Flyers', styles['title']))
    story.append(Paragraph(
        f'Practice Test {test_data["number"]} – {test_data["theme"]}', styles['subtitle']))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#0a3a66')))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        '<b>Candidate name:</b> _______________________________ &nbsp; &nbsp; '
        '<b>Date:</b> ______________', styles['body']))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        '<b>Reading & Writing</b> – 40 minutes &nbsp;|&nbsp; <b>Listening</b> – about 25 minutes &nbsp;|&nbsp; '
        '<b>Speaking</b> – about 7\u20139 minutes', styles['small']))
    story.append(Spacer(1, 10))

    # ---- Reading & Writing ----
    story.append(Paragraph('Reading & Writing Paper', styles['sectionH']))
    story.append(Paragraph(
        'There are 7 parts. You have 40 minutes. Write your answers on this paper.',
        styles['instr']))
    rw = test_data['rw']
    story.extend(build_rw_part1(styles, rw['p1']))
    story.append(PageBreak())
    story.extend(build_rw_part2(styles, rw['p2']))
    story.append(PageBreak())
    story.extend(build_rw_part3(styles, rw['p3']))
    story.append(PageBreak())
    story.extend(build_rw_part4(styles, rw['p4']))
    story.append(PageBreak())
    story.extend(build_rw_part5(styles, rw['p5']))
    story.append(PageBreak())
    story.extend(build_rw_part6(styles, rw['p6']))
    story.append(Spacer(1, 10))
    story.extend(build_rw_part7(styles, rw['p7']))

    # ---- Listening ----
    story.append(PageBreak())
    story.append(Paragraph('Listening Paper', styles['sectionH']))
    story.append(Paragraph(
        'There are 5 parts. You will hear each recording twice. '
        'For this practice material, the teacher reads the audio script (in the Answer Key booklet) aloud.',
        styles['instr']))
    lst = test_data['listening']
    story.extend(build_list_part1(styles, lst['p1']))
    story.append(PageBreak())
    story.extend(build_list_part2(styles, lst['p2']))
    story.append(Spacer(1, 10))
    story.extend(build_list_part3(styles, lst['p3']))
    story.append(PageBreak())
    story.extend(build_list_part4(styles, lst['p4']))
    story.append(PageBreak())
    story.extend(build_list_part5(styles, lst['p5']))

    # ---- Speaking ----
    story.append(PageBreak())
    story.extend(build_speaking(styles, test_data['speaking']))

    doc.build(story,
              onFirstPage=make_header_footer(test_data['number'], test_data['theme']),
              onLaterPages=make_header_footer(test_data['number'], test_data['theme']))


# ------------------- ANSWER KEY BUILDER -------------------

def build_key_pdf(all_tests, out_path):
    styles = build_styles()
    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=1.8*cm, bottomMargin=1.8*cm,
        title='Flyers Practice Tests – Answer Keys'
    )
    story = []
    story.append(Paragraph('Cambridge A2 Flyers', styles['title']))
    story.append(Paragraph('Answer Keys & Listening Scripts – 10 Practice Tests',
                           styles['subtitle']))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#6a1b9a')))
    story.append(Spacer(1, 10))

    for t in all_tests:
        story.append(Paragraph(
            f'Test {t["number"]} – {t["theme"]}', styles['sectionH']))

        # R&W
        story.append(Paragraph('Reading & Writing', styles['keyH']))
        for i in range(1, 8):
            ans = t['answers']['rw'].get(f'p{i}')
            if ans:
                story.append(Paragraph(f'<b>Part {i}:</b> {ans}', styles['body']))

        # Listening
        story.append(Paragraph('Listening – answer keys', styles['keyH']))
        for i in range(1, 6):
            ans = t['answers']['listening'].get(f'p{i}')
            if ans:
                story.append(Paragraph(f'<b>Part {i}:</b> {ans}', styles['body']))

        # Scripts
        story.append(Paragraph('Listening – audio script (teacher reads aloud, twice)',
                               styles['keyH']))
        for i in range(1, 6):
            script = t['scripts'].get(f'p{i}')
            if script:
                story.append(Paragraph(f'<b>Part {i}:</b>', styles['body']))
                story.append(Paragraph(script, styles['story']))

        # Speaking
        story.append(Paragraph('Speaking – sample answers & notes', styles['keyH']))
        for k, v in t['answers']['speaking'].items():
            story.append(Paragraph(f'<b>{k}:</b> {v}', styles['body']))

        story.append(PageBreak())

    doc.build(story, onFirstPage=key_header_footer, onLaterPages=key_header_footer)
