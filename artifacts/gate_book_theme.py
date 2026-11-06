"""Shared theme, fonts, and flow helpers for GATE DA 2027 book."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import Color, HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuBd", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuIt", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerifBd", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerifIt", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuMono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))

NAVY = HexColor("#0B1F3A")
NAVY2 = HexColor("#122A4A")
CYAN = HexColor("#0E7490")
TEAL = HexColor("#115E59")
GOLD = HexColor("#B45309")
CREAM = HexColor("#F7F3EA")
PALE = HexColor("#EEF4F7")
PALE2 = HexColor("#F3F6F8")
LINE = HexColor("#C5D0D8")
SOFTRED = HexColor("#9F1239")
GREEN = HexColor("#14532D")
GRAY = HexColor("#334155")
MUTED = HexColor("#64748B")

PAGE_W, PAGE_H = A4
LEFT = 16 * mm
RIGHT = 16 * mm
TOP = 16 * mm
BOTTOM = 16 * mm


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(
        name="CoverTitle", fontName="DejaVuBd", fontSize=26, leading=32,
        textColor=white, alignment=TA_CENTER, spaceAfter=6
    ))
    s.add(ParagraphStyle(
        name="CoverSub", fontName="DejaVu", fontSize=11, leading=16,
        textColor=HexColor("#D6E8EF"), alignment=TA_CENTER, spaceAfter=4
    ))
    s.add(ParagraphStyle(
        name="H1", fontName="DejaVuBd", fontSize=16, leading=20,
        textColor=NAVY, spaceBefore=10, spaceAfter=8
    ))
    s.add(ParagraphStyle(
        name="H2", fontName="DejaVuBd", fontSize=13, leading=17,
        textColor=CYAN, spaceBefore=9, spaceAfter=5
    ))
    s.add(ParagraphStyle(
        name="H3", fontName="DejaVuBd", fontSize=11, leading=15,
        textColor=NAVY2, spaceBefore=7, spaceAfter=3
    ))
    s.add(ParagraphStyle(
        name="Body", fontName="DejaVu", fontSize=9, leading=13,
        textColor=GRAY, alignment=TA_JUSTIFY, spaceAfter=5
    ))
    s.add(ParagraphStyle(
        name="BodyTight", fontName="DejaVu", fontSize=8.5, leading=12,
        textColor=GRAY, alignment=TA_JUSTIFY, spaceAfter=3
    ))
    s.add(ParagraphStyle(
        name="Note", fontName="DejaVuIt", fontSize=8.5, leading=12,
        textColor=TEAL, alignment=TA_LEFT, spaceBefore=3, spaceAfter=6,
        leftIndent=4, rightIndent=4
    ))
    s.add(ParagraphStyle(
        name="DashItem", fontName="DejaVu", fontSize=9, leading=12.5,
        textColor=GRAY, leftIndent=12, bulletIndent=0, spaceAfter=2
    ))
    s.add(ParagraphStyle(
        name="QStem", fontName="DejaVu", fontSize=9, leading=12.5,
        textColor=NAVY, spaceAfter=3, spaceBefore=4
    ))
    s.add(ParagraphStyle(
        name="Opt", fontName="DejaVu", fontSize=8.5, leading=12,
        textColor=GRAY, leftIndent=14, spaceAfter=1
    ))
    s.add(ParagraphStyle(
        name="Meta", fontName="DejaVuIt", fontSize=7.5, leading=10,
        textColor=MUTED, spaceAfter=2
    ))
    s.add(ParagraphStyle(
        name="Sol", fontName="DejaVu", fontSize=8.5, leading=12,
        textColor=GRAY, alignment=TA_JUSTIFY, spaceAfter=4
    ))
    s.add(ParagraphStyle(
        name="Caption", fontName="DejaVuBd", fontSize=8, leading=11,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=4
    ))
    s.add(ParagraphStyle(
        name="TOCPart", fontName="DejaVuBd", fontSize=11, leading=15,
        textColor=NAVY, spaceBefore=8, spaceAfter=3
    ))
    s.add(ParagraphStyle(
        name="TOCItem", fontName="DejaVu", fontSize=9, leading=13,
        textColor=GRAY, leftIndent=8
    ))
    s.add(ParagraphStyle(
        name="Footer", fontName="DejaVu", fontSize=7.5, leading=10,
        textColor=MUTED, alignment=TA_CENTER
    ))
    s.add(ParagraphStyle(
        name="SmallCenter", fontName="DejaVu", fontSize=8, leading=11,
        textColor=MUTED, alignment=TA_CENTER
    ))
    s.add(ParagraphStyle(
        name="MonoBlock", fontName="DejaVuMono", fontSize=8, leading=11,
        textColor=NAVY, backColor=PALE, leftIndent=6, spaceBefore=2, spaceAfter=3
    ))
    s.add(ParagraphStyle(
        name="Warn", fontName="DejaVu", fontSize=8.5, leading=12,
        textColor=SOFTRED, alignment=TA_JUSTIFY, spaceAfter=6
    ))
    s.add(ParagraphStyle(
        name="TableCell", fontName="DejaVu", fontSize=7.5, leading=10,
        textColor=GRAY
    ))
    s.add(ParagraphStyle(
        name="TableHead", fontName="DejaVuBd", fontSize=7.5, leading=10,
        textColor=white
    ))
    return s
