#!/usr/bin/env python3
"""GATE DA 2027 Practice Book — two-column Made Easy layout, A4."""
from __future__ import annotations

import json
import os
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

NAVY = HexColor("#13293d")
HARBOR = HexColor("#1d6a7a")
INK = HexColor("#1c1917")
FAINT = HexColor("#5c534a")
RULE = HexColor("#c9bba6")
BAND = HexColor("#efe6d6")
SOL = HexColor("#1f4e3d")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DejaVu", f"{FONT_DIR}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", f"{FONT_DIR}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans", f"{FONT_DIR}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", f"{FONT_DIR}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuMono", f"{FONT_DIR}/DejaVuSansMono.ttf"))

PAGE_W, PAGE_H = A4
MARGIN_L = 12 * mm
MARGIN_R = 12 * mm
MARGIN_T = 16 * mm
MARGIN_B = 12 * mm
GUTTER = 7 * mm
COL_W = (PAGE_W - MARGIN_L - MARGIN_R - GUTTER) / 2.0
COL_H = PAGE_H - MARGIN_T - MARGIN_B
HEADER_H = 9 * mm

_CTX = {"running": "", "part": ""}


def esc(s: str) -> str:
    if s is None:
        return ""
    s = (
        str(s)
        .replace("\u2212", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2264", " <= ")
        .replace("\u2265", " >= ")
    )
    s = s.replace("&", "&")
    # reportlab treats "<x" as a tag named x — spaces around entities are required
    s = s.replace("<", " < ")
    s = s.replace(">", " > ")
    s = s.replace("\n", "<br/>")
    return s


def styles():
    return {
        "coverKicker": ParagraphStyle(
            "coverKicker", fontName="DejaVuSans-Bold", fontSize=8.5,
            textColor=HexColor("#7ec8c8"), alignment=TA_CENTER, leading=12,
        ),
        "coverTitle": ParagraphStyle(
            "coverTitle", fontName="DejaVu-Bold", fontSize=32,
            textColor=white, alignment=TA_CENTER, leading=38, spaceAfter=8,
        ),
        "coverSub": ParagraphStyle(
            "coverSub", fontName="DejaVu", fontSize=11.5,
            textColor=HexColor("#d9cbb6"), alignment=TA_CENTER, leading=16,
        ),
        "coverBody": ParagraphStyle(
            "coverBody", fontName="DejaVu", fontSize=9.2,
            textColor=HexColor("#c9d6dc"), alignment=TA_CENTER, leading=13.5,
        ),
        "h1": ParagraphStyle(
            "h1", fontName="DejaVu-Bold", fontSize=16, textColor=NAVY,
            leading=20, spaceAfter=6, spaceBefore=2,
        ),
        "h2": ParagraphStyle(
            "h2", fontName="DejaVu-Bold", fontSize=11.5, textColor=NAVY,
            leading=15, spaceBefore=6, spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body", fontName="DejaVu", fontSize=8.6, textColor=INK,
            leading=11.6, alignment=TA_JUSTIFY, spaceAfter=3,
        ),
        "toc": ParagraphStyle(
            "toc", fontName="DejaVu", fontSize=9.2, textColor=INK, leading=14,
        ),
        "band": ParagraphStyle(
            "band", fontName="DejaVuSans-Bold", fontSize=8.2, textColor=white,
            leading=11, alignment=TA_LEFT,
        ),
        "qhead": ParagraphStyle(
            "qhead", fontName="DejaVuSans-Bold", fontSize=8.0, textColor=NAVY,
            leading=11, spaceBefore=2, spaceAfter=1,
        ),
        "stem": ParagraphStyle(
            "stem", fontName="DejaVu", fontSize=8.15, textColor=INK,
            leading=11.1, alignment=TA_JUSTIFY, spaceAfter=1.5,
        ),
        "code": ParagraphStyle(
            "code", fontName="DejaVuMono", fontSize=7.1, textColor=INK,
            leading=9.6, spaceAfter=1.5, backColor=BAND,
        ),
        "opt": ParagraphStyle(
            "opt", fontName="DejaVu", fontSize=7.9, textColor=INK,
            leading=10.6, leftIndent=6, spaceAfter=0.4,
        ),
        "sol": ParagraphStyle(
            "sol", fontName="DejaVu", fontSize=7.6, textColor=INK,
            leading=10.2, spaceAfter=2,
        ),
        "inst": ParagraphStyle(
            "inst", fontName="DejaVu-Bold", fontSize=8.4, textColor=NAVY,
            leading=11.5, spaceBefore=4, spaceAfter=3, alignment=TA_CENTER,
        ),
        "foot": ParagraphStyle(
            "foot", fontName="DejaVuSans", fontSize=7.2, textColor=FAINT,
            alignment=TA_CENTER,
        ),
    }


S = styles()


def looks_code(stem: str) -> bool:
    return bool(
        stem
        and any(
            tok in stem
            for tok in ("def ", "print(", "SELECT ", "FROM ", "INSERT ", "class ", "lambda ", "yield ")
        )
    )


def type_hex(qtype: str) -> str:
    return {"MCQ": "8b3a2a", "MSQ": "1d6a7a", "NAT": "3d4a1f"}.get(qtype, "13293d")


def draw_header(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - HEADER_H, PAGE_W, HEADER_H, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVuSans-Bold", 7.4)
    canvas.drawString(MARGIN_L, PAGE_H - 6.2 * mm, "GATE 2027  ·  DATA SCIENCE & AI")
    canvas.setFont("DejaVuSans", 7.2)
    canvas.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 6.2 * mm, "Practice Book")
    canvas.setFillColor(HARBOR)
    canvas.rect(0, 0, PAGE_W, 6 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVuSans", 7)
    canvas.drawString(MARGIN_L, 2 * mm, "Unofficial  ·  unit questions, then compact solutions")
    canvas.drawRightString(PAGE_W - MARGIN_R, 2 * mm, str(doc.page))
    canvas.restoreState()


def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(HARBOR)
    canvas.rect(0, PAGE_H - 18 * mm, PAGE_W, 18 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVuSans-Bold", 8.5)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 11 * mm, "GATE 2027  ·  DATA SCIENCE & ARTIFICIAL INTELLIGENCE")
    canvas.setFillColor(HARBOR)
    canvas.rect(0, 0, PAGE_W, 14 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 8)
    canvas.drawCentredString(PAGE_W / 2, 6 * mm, "Print A4  ·  Work the unit, then open that unit's solutions")
    canvas.restoreState()


def q_block(q: dict, n: int):
    qtype = q.get("qtype") or "MCQ"
    marks = int(q.get("marks") or 1)
    topic = esc(q.get("topic") or "")
    head = Paragraph(
        f"Q.{n}  <font color='#{type_hex(qtype)}'>{qtype}</font>"
        f"  ·  {marks} mark{'s' if marks != 1 else ''}  ·  {topic}",
        S["qhead"],
    )
    stem_txt = esc(q.get("stem") or "")
    sty = S["code"] if looks_code(q.get("stem") or "") else S["stem"]
    try:
        stem = Paragraph(stem_txt, sty)
    except Exception:
        stem = Paragraph(esc((q.get("stem") or "").replace("<", " < ").replace(">", " > ")), sty)
    bits = [head, stem]
    opts = q.get("options") or []
    for i, opt in enumerate(opts):
        try:
            bits.append(Paragraph(f"({chr(65 + i)})&nbsp;&nbsp;{esc(opt)}", S["opt"]))
        except Exception:
            bits.append(Paragraph(f"({chr(65 + i)})  {esc(str(opt))}", S["opt"]))
    if not opts:
        bits.append(Paragraph("<font color='#5c534a'>NAT  ·  enter the numerical value</font>", S["opt"]))
    bits.append(Spacer(1, 3.2 * mm))
    if len(q.get("stem") or "") < 520:
        return KeepTogether(bits)
    return bits


def sol_block(q: dict, n: int):
    ans = esc(q.get("answer") or "")
    sol = esc(q.get("sol") or "")
    qtype = q.get("qtype") or "MCQ"
    body = f"<b>Q.{n}</b>  [{qtype}]  <font color='#1f4e3d'><b>{ans}</b></font>"
    if sol:
        body += f"  —  {sol}"
    try:
        return Paragraph(body, S["sol"])
    except Exception:
        return Paragraph(f"Q.{n}  [{qtype}]  {ans}", S["sol"])


def section_banner(text: str):
    data = [[Paragraph(esc(text), S["band"])]]
    t = Table(data, colWidths=[COL_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


class BookDoc(BaseDocTemplate):
    def __init__(self, path: str):
        super().__init__(
            path,
            pagesize=A4,
            leftMargin=MARGIN_L,
            rightMargin=MARGIN_R,
            topMargin=MARGIN_T,
            bottomMargin=MARGIN_B,
            title="GATE DA 2027 Practice Book",
            author="Unofficial practice compilation",
        )
        cover_frame = Frame(MARGIN_L, 30 * mm, PAGE_W - MARGIN_L - MARGIN_R, PAGE_H - 55 * mm, id="cover")
        full = Frame(MARGIN_L, MARGIN_B, PAGE_W - MARGIN_L - MARGIN_R, COL_H, id="full")
        c1 = Frame(MARGIN_L, MARGIN_B, COL_W, COL_H, id="c1")
        c2 = Frame(MARGIN_L + COL_W + GUTTER, MARGIN_B, COL_W, COL_H, id="c2")
        self.addPageTemplates(
            [
                PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
                PageTemplate(id="one", frames=[full], onPage=draw_header),
                PageTemplate(id="two", frames=[c1, c2], onPage=draw_header),
            ]
        )


def build(book: dict, out_path: str):
    doc = BookDoc(out_path)
    story = []
    units = book.get("units") or []
    mocks = book.get("mocks") or []
    total = sum(len(u.get("questions") or []) for u in units)
    mock_q = sum(len(m.get("questions") or []) for m in mocks)

    story.append(Spacer(1, 38 * mm))
    story.append(Paragraph("PRACTICE BOOK", S["coverTitle"]))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            f"{total} unit questions  ·  {len(units)} subjects  ·  {len(mocks)} full-length mocks",
            S["coverSub"],
        )
    )
    story.append(Spacer(1, 14 * mm))
    story.append(
        Paragraph(
            "Layout modelled on standard GATE / Made Easy practice books:<br/>"
            "unit questions, then compact solutions — not a theory text.",
            S["coverBody"],
        )
    )
    story.append(Spacer(1, 8 * mm))
    story.append(
        Paragraph(
            "Stems follow official DA 2024 / 2025 / 2026 habits:<br/>"
            "Bayes and named distributions  ·  small matrices  ·  Python defaults<br/>"
            "quicksort recurrences  ·  BCNF / SQL NULL  ·  PCA orthogonality<br/>"
            "LOOCV  ·  uninformed vs A*  ·  FOL implication vs conjunction",
            S["coverBody"],
        )
    )
    story.append(Spacer(1, 10 * mm))
    story.append(
        Paragraph(
            "Official 2027 DA syllabus (IIT Madras) is unchanged from 2026.<br/>"
            "Mocks use the latest confirmed paper: 65 Q, 100 marks, 3 hours.<br/><br/>"
            "No official PYQ is copied. Similar patterns only.",
            S["coverBody"],
        )
    )
    story.append(NextPageTemplate("one"))
    story.append(PageBreak())

    _CTX["running"] = "How to use this book"
    _CTX["part"] = "Front matter"
    story.append(Paragraph("How to use this book", S["h1"]))
    story.append(
        Paragraph(
            "This is a question book, not a textbook. Each unit is a dense drill in the style of "
            "standard GATE practice volumes: numbered stems, four options for MCQ/MSQ, a blank for NAT, "
            "then a compact answer key. Work a column with a timer. Open solutions only after you finish.",
            S["body"],
        )
    )
    story.append(Paragraph("Official GATE DA paper (confirmed 2026, unchanged for 2027)", S["h2"]))
    story.append(
        Paragraph(
            "65 questions, 100 marks, 3 hours. General Aptitude 10 questions / 15 marks "
            "(Q.1-5 one mark, Q.6-10 two marks). DA 55 questions / 85 marks "
            "(Q.11-35 one mark, Q.36-65 two marks). MCQ negative marking is -1/3 (1-mark) and "
            "-2/3 (2-mark). MSQ and NAT have no negative marking. The ten mock papers in this book "
            "use that exact skeleton.",
            S["body"],
        )
    )
    story.append(Paragraph("What was analysed", S["h2"]))
    story.append(
        Paragraph(
            "Official DA 2024 (IISc Bengaluru), DA 2025 (IIT Roorkee) and DA 2026 (IIT Guwahati) "
            "were read for habit, not copied: 2x2 eigenproblems, a named distribution with a number, "
            "a 6-8 line Python snippet with a mutable default, SQL three-valued logic, BCNF vs 3NF on "
            "a tiny FD set, PCA axes at 90 degrees, LOOCV counting, A* vs uninformed search, and FOL "
            "implication versus conjunction. New numbers and wording throughout. Predictions in older "
            "drafts were preparation priorities, not guarantees — this edition does not claim to forecast 2027.",
            S["body"],
        )
    )
    story.append(Paragraph("Marking while you practise", S["h2"]))
    story.append(
        Paragraph(
            "MCQ: choose one option. A wrong MCQ should be scored with the official negative. "
            "MSQ: one or more options; no partial credit in this key (all-correct or zero). "
            "NAT: a number; GATE accepts a range, so treat a clearly equivalent form as correct.",
            S["body"],
        )
    )

    story.append(Paragraph("Contents", S["h1"]))
    toc_rows = []
    for u in units:
        nq = len(u.get("questions") or [])
        toc_rows.append(
            [
                Paragraph(f"Unit {u.get('code')}", S["toc"]),
                Paragraph(esc(u.get("title") or ""), S["toc"]),
                Paragraph(str(nq), S["toc"]),
            ]
        )
    toc_rows.append(["", Paragraph("<b>Mock papers (65 Q, 100 marks, 3 h)</b>", S["toc"]), ""])
    for m in mocks:
        toc_rows.append(
            [
                Paragraph(f"Paper {m.get('code')}", S["toc"]),
                Paragraph(esc(m.get("title") or ""), S["toc"]),
                Paragraph(str(len(m.get("questions") or [])), S["toc"]),
            ]
        )
    tw = PAGE_W - MARGIN_L - MARGIN_R
    toc = Table(toc_rows, colWidths=[22 * mm, tw - 38 * mm, 16 * mm])
    toc.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LINEBELOW", (0, 0), (-1, -2), 0.2, RULE),
                ("ALIGN", (2, 0), (2, -1), "RIGHT"),
            ]
        )
    )
    story.append(toc)
    story.append(Spacer(1, 6 * mm))
    story.append(
        Paragraph(
            f"Unit questions {total}  ·  mock questions {mock_q}  ·  unofficial  ·  not affiliated with GATE / IIT / IISc.",
            S["foot"],
        )
    )

    story.append(NextPageTemplate("two"))
    story.append(PageBreak())
    for u in units:
        title = u.get("title") or ""
        code = u.get("code") or ""
        qs = u.get("questions") or []
        _CTX["running"] = f"Unit {code}  ·  {title}"
        _CTX["part"] = f"Unit {code} questions"
        story.append(section_banner(f"UNIT {code}   {title}   ·   {len(qs)} questions"))
        story.append(Spacer(1, 2 * mm))
        story.append(
            Paragraph(
                "MCQ negative -1/3 or -2/3.  MSQ / NAT no negative.  Work first, then the solutions section.",
                S["inst"],
            )
        )
        for i, q in enumerate(qs, 1):
            blk = q_block(q, i)
            if isinstance(blk, list):
                story.extend(blk)
            else:
                story.append(blk)
        story.append(PageBreak())
        _CTX["part"] = f"Unit {code} solutions"
        story.append(section_banner(f"UNIT {code}   SOLUTIONS"))
        story.append(Spacer(1, 2 * mm))
        for i, q in enumerate(qs, 1):
            story.append(sol_block(q, i))
        story.append(PageBreak())

    for m in mocks:
        code = m.get("code") or ""
        title = m.get("title") or ""
        qs = m.get("questions") or []
        _CTX["running"] = f"Mock {code}"
        _CTX["part"] = f"Mock {code}  ·  65 Q  ·  100 marks  ·  3 hours"
        story.append(section_banner(f"MOCK PAPER {code}   {title}"))
        story.append(Spacer(1, 1.5 * mm))
        story.append(
            Paragraph(
                "Duration: 3 hours.  Maximum marks: 100.  "
                "Q.1-5 GA one mark · Q.6-10 GA two marks · Q.11-35 DA one mark · Q.36-65 DA two marks.  "
                "MCQ: -1/3 / -2/3.  MSQ and NAT: no negative.",
                S["inst"],
            )
        )

        def band(i0, i1, label):
            story.append(Paragraph(label, S["inst"]))
            for i in range(i0, min(i1, len(qs))):
                blk = q_block(qs[i], i + 1)
                if isinstance(blk, list):
                    story.extend(blk)
                else:
                    story.append(blk)

        band(0, 5, "Q.1 - Q.5  Carry ONE mark each  (General Aptitude)")
        band(5, 10, "Q.6 - Q.10  Carry TWO marks each  (General Aptitude)")
        band(10, 35, "Q.11 - Q.35  Carry ONE mark each  (DA)")
        band(35, 65, "Q.36 - Q.65  Carry TWO marks each  (DA)")

        story.append(PageBreak())
        _CTX["part"] = f"Mock {code} answer key"
        story.append(section_banner(f"MOCK {code}  ANSWER KEY AND SHORT SOLUTIONS"))
        story.append(Spacer(1, 2 * mm))
        for i, q in enumerate(qs, 1):
            story.append(sol_block(q, i))
        story.append(PageBreak())

    if story and isinstance(story[-1], PageBreak):
        story.pop()

    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    doc.build(story)
    return out_path


def main():
    src = Path("/workspace/public/book.json")
    if not src.exists():
        src = Path("/workspace/artifacts/book.json")
    book = json.loads(src.read_text())
    out1 = "/workspace/public/GATE2027.pdf"
    out2 = "/workspace/artifacts/GATE2027.pdf"
    build(book, out1)
    Path(out2).write_bytes(Path(out1).read_bytes())
    size = Path(out1).stat().st_size
    print("wrote", out1, "bytes", size)
    print("wrote", out2, "bytes", size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
