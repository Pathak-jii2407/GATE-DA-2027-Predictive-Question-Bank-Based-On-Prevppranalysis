#!/usr/bin/env python3
"""Made Easy-style GATE DA practice book (questions + compact solutions + 10 mocks)."""
import json
import random
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable,
)
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import white, black

from practice_style import (
    styles, NAVY, TEAL, INK, MUTED, LINE, HEAD, BAND, PAGE_W, PAGE_H,
    LEFT, RIGHT, TOP, BOTTOM,
)
from refined_bank import SUBJECTS

S = styles()
OUT = "/home/workdir/artifacts/GATE2027.pdf"


def esc(t):
    return "" if t is None else str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 7.5)
    canvas.drawString(LEFT, PAGE_H - 5.2 * mm, "GATE DA Practice Book  ·  2027 edition")
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 5.2 * mm, "Questions in official style")
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.3)
    canvas.line(LEFT, 9 * mm, PAGE_W - RIGHT, 9 * mm)
    canvas.setFillColor(MUTED)
    canvas.setFont("DejaVu", 7)
    canvas.drawString(LEFT, 4.2 * mm, "Unofficial  ·  originals inspired by DA 2024–2026 patterns")
    canvas.drawRightString(PAGE_W - RIGHT, 4.2 * mm, str(doc.page))
    canvas.restoreState()


def cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, PAGE_H - 22 * mm, PAGE_W, 6 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 8)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 20 * mm, "GATE 2027  ·  DATA SCIENCE & ARTIFICIAL INTELLIGENCE")
    canvas.setFont("DejaVuBd", 20)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 55 * mm, "PRACTICE BOOK")
    canvas.setFont("DejaVu", 11)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 70 * mm, "250 questions × 8 units   ·   10 full-length mocks")
    canvas.setFont("DejaVu", 9)
    y = PAGE_H - 95 * mm
    for line in [
        "Layout modelled on standard GATE / Made Easy practice books:",
        "unit questions, then compact solutions — not a theory text.",
        "",
        "Stems follow official DA 2024 / 2025 / 2026 habits:",
        "Bayes and named distributions  ·  small matrices  ·  Python defaults",
        "quicksort recurrences  ·  BCNF / SQL NULL  ·  PCA orthogonality",
        "LOOCV counts  ·  uninformed vs A*  ·  FOL implication vs conjunction",
        "",
        "Official 2027 DA syllabus (IIT Madras) is unchanged from 2026.",
        "Mocks use the latest confirmed paper: 65 Q, 100 marks, 3 hours.",
        "",
        "No official PYQ is copied. Similar patterns only.",
    ]:
        canvas.drawCentredString(PAGE_W / 2, y, line)
        y -= 6 * mm
    canvas.setFont("DejaVu", 8)
    canvas.drawCentredString(PAGE_W / 2, 24 * mm, "Print A4  ·  Work the unit, then open that unit’s solutions")
    canvas.restoreState()


def qflow(q, num):
    bits = [Paragraph(f"<b>Q.{num}</b>  &nbsp;[{q['qtype']}, {q['marks']} mark]", S["QNo"]),
            Paragraph(esc(q["stem"]), S["Stem"])]
    if q["qtype"] == "MSQ":
        bits.append(Paragraph("One or more options may be correct.", S["Tag"]))
    if q["qtype"] == "NAT":
        bits.append(Paragraph("Numerical answer type.", S["Tag"]))
    if q.get("options"):
        # two-column options when short
        opts = q["options"]
        if all(len(str(o)) <= 42 for o in opts) and len(opts) == 4:
            row = " &nbsp;&nbsp; ".join(f"<b>({chr(65+i)})</b> {esc(o)}" for i, o in enumerate(opts))
            bits.append(Paragraph(row, S["Opt"]))
        else:
            for i, o in enumerate(opts):
                bits.append(Paragraph(f"({chr(65+i)})  {esc(o)}", S["Opt"]))
    bits.append(Spacer(1, 1.6 * mm))
    return KeepTogether(bits)


def sflow(q, num):
    return KeepTogether([
        Paragraph(f"<b>Q.{num}</b>  &nbsp;[{q['answer']}]", S["SolH"]),
        Paragraph(esc(q.get("sol", "")), S["Sol"]),
    ])


def sort_unit(qs):
    rank = {"MSQ": 0, "MCQ": 1, "NAT": 2}
    return sorted(qs, key=lambda q: (rank.get(q["qtype"], 9), q["topic"]))


def pick_mock(bank, letter, rng):
    """65 Q following 2026 skeleton. Prefer conceptual items."""
    def pool(code, types=None):
        xs = [q for q in bank[code] if types is None or q["qtype"] in types]
        # prefer shorter conceptual (non pad-like) by topic diversity
        rng.shuffle(xs)
        return xs

    used = set()

    def take(code, k, types=None):
        got = []
        for q in pool(code, types):
            if q["stem"] in used:
                continue
            used.add(q["stem"])
            got.append(q)
            if len(got) == k:
                break
        return got

    # GA 1-5 one mark, 6-10 two mark
    ga_mcq = take("GA", 10, {"MCQ", "NAT"})
    while len(ga_mcq) < 10:
        ga_mcq += take("GA", 10 - len(ga_mcq))
    # DA 1-mark 25: mix subjects
    one = (take("ML", 4) + take("AI", 4) + take("P&S", 4) + take("LA", 3)
           + take("DSA", 4) + take("DBMS", 3) + take("Calc", 3))
    two = (take("ML", 6) + take("AI", 5) + take("P&S", 5) + take("LA", 4)
           + take("DSA", 4) + take("DBMS", 4) + take("Calc", 2))
    rng.shuffle(one)
    rng.shuffle(two)
    one, two = one[:25], two[:30]
    qs = []
    n = 1
    for q in ga_mcq[:5]:
        q = dict(q); q["num"] = n; q["marks"] = 1; n += 1; qs.append(q)
    for q in ga_mcq[5:10]:
        q = dict(q); q["num"] = n; q["marks"] = 2; n += 1; qs.append(q)
    for q in one:
        q = dict(q); q["num"] = n; q["marks"] = 1; n += 1; qs.append(q)
    for q in two:
        q = dict(q); q["num"] = n; q["marks"] = 2; n += 1; qs.append(q)
    return qs


def build():
    bank = json.load(open("/home/workdir/artifacts/practice_bank.json"))
    for k in bank:
        bank[k] = sort_unit(bank[k])

    story = [Spacer(1, 160 * mm), PageBreak(),
             Paragraph("CONTENTS", S["Unit"]),
             Paragraph("This is a question book. There is no chapter theory. "
                       "Each unit lists 250 GATE-style items, then that unit’s answer line and a short solution. "
                       "Ten mocks at the end follow the official DA skeleton (GA Q.1–10, DA Q.11–65).", S["Body"]),
             Spacer(1, 2 * mm)]
    toc = [
        "UNIT 1  Probability and Statistics ………… 250 Q",
        "UNIT 2  Linear Algebra ……………………………… 250 Q",
        "UNIT 3  Calculus and Optimization ………… 250 Q",
        "UNIT 4  Programming / DSA …………………… 250 Q",
        "UNIT 5  DBMS and Warehousing …………… 250 Q",
        "UNIT 6  Machine Learning ……………………… 250 Q",
        "UNIT 7  Artificial Intelligence ……………… 250 Q",
        "UNIT 8  General Aptitude ………………………… 250 Q",
        "MOCKS A–J  (each 65 Q, 100 marks) ",
    ]
    for line in toc:
        story.append(Paragraph(line, S["TOC"]))
    story += [Spacer(1, 3 * mm),
              Paragraph("Paper rules used in every mock", S["Chap"]),
              Paragraph("65 questions, 100 marks, 180 minutes. GA 10 Q / 15 marks. DA 55 Q / 85 marks. "
                        "MCQ negative marking −1/3 (1-mark) and −2/3 (2-mark). MSQ and NAT: no negative, no partial credit. "
                        "Official GATE DA 2027 pattern has not been published as a new scheme; mocks use the 2026 confirmed pattern.", S["Body"]),
              Paragraph("Pattern notes from official DA papers (not copied questions)", S["Chap"]),
              Paragraph("2024 IISc — first DA paper; counting, series, dice/spatial GA; core DA already mixes probability, algebra, a little ML/AI. "
                        "2025 Roorkee — conditional expectation identity, Gaussian elimination operation count, SQL tables, Python snippets, graphs. "
                        "2026 Guwahati — PCA axes orthogonal, LOOCV split count (900 not 1000), A* is not uninformed, "
                        "FOL ‘each king is a person’ is implication not conjunction, quicksort expected recurrence with random-looking first-element pivot, "
                        "Python mutable default list, ER, Uniform, Bernoulli matrix. "
                        "Practice items below replay those habits with new numbers and new wording.", S["Body"])]

    for code, title, _ in SUBJECTS:
        qs = bank[code]
        story += [PageBreak(), Paragraph(title, S["Unit"]),
                  Paragraph(f"{len(qs)} questions  ·  work this unit before the solutions page that follows the last question.", S["Note"]),
                  HRFlowable(width="100%", thickness=0.4, color=LINE, spaceAfter=4)]
        for i, q in enumerate(qs, 1):
            story.append(qflow(q, i))
        story += [PageBreak(), Paragraph(title + "  —  SOLUTIONS", S["Unit"])]
        # compact key first
        keys = []
        row = []
        for i, q in enumerate(qs, 1):
            row.append(f"{i}. {q['answer']}")
            if len(row) == 5:
                keys.append(" &nbsp;&nbsp; ".join(row))
                row = []
        if row:
            keys.append(" &nbsp;&nbsp; ".join(row))
        story.append(Paragraph("KEY", S["Chap"]))
        for line in keys:
            story.append(Paragraph(line, S["Key"]))
        story.append(Paragraph("SOLUTIONS", S["Chap"]))
        for i, q in enumerate(qs, 1):
            story.append(sflow(q, i))

    # 10 mocks
    themes = {
        "A": "Balanced", "B": "More algebra / calculus", "C": "More ML",
        "D": "More AI", "E": "More DSA / Python", "F": "More probability",
        "G": "More DBMS", "H": "Trickier MSQ mix", "I": "NAT-heavy finish",
        "J": "Full mixed rank-separator",
    }
    rng = random.Random(2027)
    story += [PageBreak(), Paragraph("FULL-LENGTH MOCK PAPERS A–J", S["Unit"]),
              Paragraph("Each paper is 65 questions / 100 marks / 3 hours. Write answers first. Open the key of that paper only afterwards.", S["Body"])]
    for L, theme in themes.items():
        qs = pick_mock(bank, L, rng)
        story += [PageBreak(),
                  Paragraph(f"MOCK {L}  ·  {theme}", S["Unit"]),
                  Paragraph("Q.1–Q.5 GA 1 mark · Q.6–Q.10 GA 2 mark · Q.11–Q.35 DA 1 mark · Q.36–Q.65 DA 2 mark.", S["Note"])]
        for q in qs:
            story.append(qflow(q, q["num"]))
        story += [PageBreak(), Paragraph(f"MOCK {L} — KEY AND SOLUTIONS", S["Unit"])]
        row, keys = [], []
        for q in qs:
            row.append(f"{q['num']}. {q['answer']}")
            if len(row) == 5:
                keys.append(" &nbsp;&nbsp; ".join(row)); row = []
        if row:
            keys.append(" &nbsp;&nbsp; ".join(row))
        for line in keys:
            story.append(Paragraph(line, S["Key"]))
        story.append(Spacer(1, 2 * mm))
        for q in qs:
            story.append(sflow(q, q["num"]))

    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=12 * mm, bottomMargin=12 * mm,
        title="GATE DA 2027 Practice Book",
        author="Unofficial practice book",
    )
    doc.build(story, onFirstPage=cover, onLaterPages=header_footer)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
