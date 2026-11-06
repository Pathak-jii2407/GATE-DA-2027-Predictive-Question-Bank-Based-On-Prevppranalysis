"""Made Easy-like styles for the GATE DA practice book."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuBd", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuIt", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"))

NAVY = HexColor("#1B365D")
TEAL = HexColor("#0F5C63")
RED = HexColor("#8B1E3F")
INK = HexColor("#1A1A1A")
MUTED = HexColor("#4A5568")
LINE = HexColor("#B7C3CE")
HEAD = HexColor("#12324D")
SOLG = HexColor("#1F4E3D")
CREAM = HexColor("#F4F1EA")
BAND = HexColor("#E8EEF3")

PAGE_W, PAGE_H = A4
LEFT, RIGHT, TOP, BOTTOM = 14 * mm, 14 * mm, 14 * mm, 12 * mm


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="Unit", fontName="DejaVuBd", fontSize=13, leading=16,
                         textColor=HEAD, spaceBefore=2, spaceAfter=4))
    s.add(ParagraphStyle(name="Chap", fontName="DejaVuBd", fontSize=10.5, leading=13,
                         textColor=TEAL, spaceBefore=6, spaceAfter=3))
    s.add(ParagraphStyle(name="QNo", fontName="DejaVuBd", fontSize=9, leading=12,
                         textColor=HEAD, spaceBefore=3, spaceAfter=1))
    s.add(ParagraphStyle(name="Stem", fontName="DejaVu", fontSize=8.7, leading=11.6,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=1.5))
    s.add(ParagraphStyle(name="Opt", fontName="DejaVu", fontSize=8.3, leading=11.2,
                         textColor=INK, leftIndent=8, spaceAfter=0.4))
    s.add(ParagraphStyle(name="Tag", fontName="DejaVuIt", fontSize=7, leading=9,
                         textColor=MUTED, spaceAfter=1))
    s.add(ParagraphStyle(name="SolH", fontName="DejaVuBd", fontSize=8.5, leading=11,
                         textColor=SOLG, spaceBefore=2, spaceAfter=0.5))
    s.add(ParagraphStyle(name="Sol", fontName="DejaVu", fontSize=8.2, leading=11,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=3))
    s.add(ParagraphStyle(name="Body", fontName="DejaVu", fontSize=8.6, leading=11.6,
                         textColor=INK, alignment=TA_JUSTIFY, spaceAfter=3))
    s.add(ParagraphStyle(name="Note", fontName="DejaVuIt", fontSize=8, leading=11,
                         textColor=MUTED, spaceAfter=3))
    s.add(ParagraphStyle(name="TOC", fontName="DejaVu", fontSize=9, leading=13,
                         textColor=INK, spaceAfter=1))
    s.add(ParagraphStyle(name="TOCH", fontName="DejaVuBd", fontSize=10, leading=14,
                         textColor=HEAD, spaceBefore=4, spaceAfter=2))
    s.add(ParagraphStyle(name="CoverT", fontName="DejaVuBd", fontSize=18, leading=22,
                         textColor=white, alignment=TA_CENTER))
    s.add(ParagraphStyle(name="CoverS", fontName="DejaVu", fontSize=10, leading=14,
                         textColor=HexColor("#D9E6EF"), alignment=TA_CENTER))
    s.add(ParagraphStyle(name="Key", fontName="DejaVu", fontSize=8, leading=11,
                         textColor=INK))
    return s
