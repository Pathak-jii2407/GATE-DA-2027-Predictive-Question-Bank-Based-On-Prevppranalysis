#!/usr/bin/env python3
"""Full textbook-style GATE DA 2027 book."""
import json
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, HRFlowable, CondPageBreak,
)
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import white

from gate_book_theme import (
    styles, NAVY, CYAN, GOLD, PALE, LINE, GRAY, MUTED,
    PAGE_W, PAGE_H, LEFT, RIGHT,
)
from gate_analysis import DISCLAIMER, FACTS, MATRIX, YEAR_NOTES, WEIGHT_MODEL, CS_TRANSFER, UNDERTESTED, TRAPS
from gate_mocks import all_papers, THEMES

S = styles()
OUT = "/home/workdir/artifacts/GATE2027.pdf"


def esc(t):
    return "" if t is None else str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 9 * mm, PAGE_W, 9 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 7)
    canvas.drawString(LEFT, PAGE_H - 5.8 * mm, "GATE DA 2027  ·  Prediction + Practice Master Book")
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 5.8 * mm, "Unofficial textbook edition")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 9 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.drawString(LEFT, 3.6 * mm, "Preparation priorities — not guaranteed questions")
    canvas.drawRightString(PAGE_W - RIGHT, 3.6 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, PAGE_H - 26 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 20 * mm, PAGE_W, 3.5 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 8.5)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 23.2 * mm, "GATE 2027  ·  IIT MADRAS  ·  UNOFFICIAL SELF-STUDY TEXT")
    canvas.setFont("DejaVuBd", 22)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 58 * mm, "GATE DA 2027")
    canvas.setFont("DejaVuBd", 13)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 70 * mm, "DATA SCIENCE & ARTIFICIAL INTELLIGENCE")
    canvas.setFont("DejaVuBd", 12)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 82 * mm, "PREDICTION + PRACTICE MASTER BOOK")
    canvas.setFont("DejaVu", 9.5)
    y = PAGE_H - 102 * mm
    for ln in [
        "Pattern analysis of official GATE DA 2024, 2025 and 2026",
        "Official 2027 syllabus (unchanged from 2026)",
        "2,000+ original practice items across eight subjects",
        "10 full-length GATE-style mock papers with solutions",
        "Formula book  ·  Trap book  ·  30-day revision plan",
        "",
        "Print / xerox A4  ·  Questions and solutions separated",
    ]:
        canvas.drawCentredString(PAGE_W / 2, y, ln)
        y -= 6 * mm
    canvas.setFont("DejaVuIt", 8)
    canvas.drawCentredString(PAGE_W / 2, 28 * mm, "No item is claimed to appear in the real GATE DA 2027 paper.")
    canvas.restoreState()


def H(text, lv=1):
    return Paragraph(text, S["H1"] if lv == 1 else S["H2"] if lv == 2 else S["H3"])


def P(text, st="Body"):
    return Paragraph(text, S[st])


def bullets(xs):
    return [Paragraph("• " + x, S["DashItem"]) for x in xs]


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=LINE, spaceBefore=3, spaceAfter=6)


def tbl(data, widths):
    sty = [
        ("FONTNAME", (0, 0), (-1, -1), "DejaVu"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("LEADING", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "DejaVuBd"),
        ("TEXTCOLOR", (0, 1), (-1, -1), GRAY),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            sty.append(("BACKGROUND", (0, i), (-1, i), PALE))
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle(sty))
    return t


def banner(title, sub):
    t = Table([[P(f"<font color='white'><b>{esc(title)}</b></font>"),
                P(f"<font color='#D6E8EF'>{esc(sub)}</font>")]],
              colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def qblock(q, num):
    bits = [Paragraph(f"<b>QUESTION {num:03d}</b>", S["H3"]),
            Paragraph(f"Topic: {esc(q.get('topic',''))}  ·  Type: {q.get('qtype')}  ·  "
                      f"{q.get('marks','?')} mark  ·  {esc(q.get('diff',''))}  ·  Priority: {esc(q.get('pred',''))}", S["Meta"]),
            Paragraph(esc(q["stem"]), S["QStem"])]
    if q.get("qtype") == "MSQ":
        bits.append(Paragraph("One or more options may be correct.", S["Note"]))
    if q.get("qtype") == "NAT":
        bits.append(Paragraph("Enter the numerical answer.", S["Note"]))
    if q.get("options"):
        for i, opt in enumerate(q["options"]):
            bits.append(Paragraph(f"({chr(65+i)})  {esc(opt)}", S["Opt"]))
    bits.append(Spacer(1, 2.2 * mm))
    return KeepTogether(bits)


def sblock(q, num):
    return KeepTogether([
        Paragraph(f"<b>QUESTION {num:03d} — SOLUTION</b> &nbsp;&nbsp; Answer: <font color='#14532D'><b>{esc(q.get('answer'))}</b></font>", S["H3"]),
        Paragraph(esc(q.get("sol", "")), S["Sol"]),
        Spacer(1, 1.8 * mm),
    ])


def key_table(qs, start=1):
    rows = [["No.", "Answer", "Type", "Diff", "Topic"]]
    for i, q in enumerate(qs, start):
        rows.append([f"{i:03d}", str(q.get("answer", "")), q.get("qtype", ""),
                     q.get("diff", ""), q.get("topic", "")])
    return tbl(rows, [16*mm, 32*mm, 18*mm, 24*mm, 80*mm])


INTRO = {
    "P&S": "Probability is the language of every later DA topic that reasons under uncertainty: Naive Bayes, Bayes nets, evaluation splits, noise models. Official papers keep returning to conditioning, named distributions and one clean joint or covariance NAT. Hypothesis tests are still under-tested relative to the syllabus heading — practise them anyway.",
    "LA": "Linear algebra is how DA writes PCA, ridge, projectors and SVD. Small numeric matrices, special-matrix MSQs and rank-nullity NATs are the house style.",
    "Calc": "The official calculus syllabus is short, which makes every heading high-leverage: limits, Taylor, one-variable max/min, a descent step.",
    "DSA": "Python is the official language. Mutable defaults, sorting recurrences, hashing traces, trees and BFS/DFS appear both as DSA and as AI search.",
    "DBMS": "Candidate keys from a short FD set, BCNF versus 3NF, SQL three-valued logic, and one warehouse/OLAP item form a realistic cluster.",
    "ML": "Regression algebra, regularisation, CV accounting, PCA geometry, tree impurity, Naive Bayes products, k-means monotonicity, ReLU pieces.",
    "AI": "Search taxonomy, A* conditions, propositional equivalence, FOL scope, d-separation, VE cost, sampling as approximate inference.",
    "GA": "Fifteen marks, every paper. Analogies, grammar, percentages, short logic, one spatial or arrangement item.",
}

TITLES = {
    "P&S": ("PART II", "PROBABILITY AND STATISTICS"),
    "LA": ("PART III", "LINEAR ALGEBRA"),
    "Calc": ("PART IV", "CALCULUS AND OPTIMIZATION"),
    "DSA": ("PART V", "PROGRAMMING, DATA STRUCTURES AND ALGORITHMS"),
    "DBMS": ("PART VI", "DATABASE MANAGEMENT AND DATA WAREHOUSING"),
    "ML": ("PART VII", "MACHINE LEARNING"),
    "AI": ("PART VIII", "ARTIFICIAL INTELLIGENCE"),
    "GA": ("PART IX", "GENERAL APTITUDE"),
}


def subject_part(story, code, qs):
    part, title = TITLES[code]
    story += [PageBreak(), banner(part, title), Spacer(1, 4 * mm),
              H("Subject overview"), P(INTRO[code]),
              H("How this practice set is built", 2),
              P("Each subject contains 260 original items. A conceptual core (MCQ/MSQ identities, definitions, taxonomy) "
                "is expanded by computed numeric families — different rates, different matrices, different counts. "
                "Those families are distinct questions, not copies of official PYQs. "
                "A block of 20 questions is followed by its answer key and worked solutions so you can pause."),
              hr()]
    B = 20
    for b in range(0, len(qs), B):
        chunk = qs[b:b + B]
        story += [H(f"Practice block {b//B + 1}  (Q{b+1:03d}–Q{b+len(chunk):03d})", 2)]
        for i, q in enumerate(chunk):
            story.append(qblock(q, b + i + 1))
        story += [H("Answer key", 2), key_table(chunk, b + 1), Spacer(1, 3 * mm),
                  H("Detailed solutions", 2)]
        for i, q in enumerate(chunk):
            story.append(sblock(q, b + i + 1))
        story.append(Spacer(1, 3 * mm))


def build():
    with open("/home/workdir/artifacts/da_bank.json") as f:
        bank = json.load(f)

    story = [Spacer(1, 180 * mm), PageBreak(),
             H("How to use this book"),
             P(DISCLAIMER, "Warn"),
             P("Four passes. (1) Read Part I so three official papers are not treated as a lottery. "
               "(2) Drill one subject block a day with a pen. (3) Write the ten mocks under 180 minutes, closed book. "
               "(4) Last ten days: formula book, trap book, Top-100 list."),
             P("<b>Official pattern used for every mock.</b> 65 questions, 100 marks, 3 hours. "
               "GA 10 questions / 15 marks. DA core 55 questions / 85 marks. "
               "MCQ negative marking −1/3 and −2/3. MSQ and NAT have no negative marks and no partial marks. "
               "Working skeleton (GATE DA 2026 official key): Q1–10 GA; Q11–35 one-mark DA; Q36–65 two-mark DA; "
               "inside each mark band the order is MCQ, then MSQ, then NAT."),
             P("The official GATE DA 2027 paper pattern has not been published as a separate new scheme. "
               "These mocks therefore use the latest confirmed DA pattern, not an invented 2027 format."),
             PageBreak(),
             H("Table of contents"),
             P("Part I — Pattern analysis and 2027 methodology", "TOCPart"),
             P("Part II — Probability and Statistics (260 original items)", "TOCPart"),
             P("Part III — Linear Algebra (260)", "TOCPart"),
             P("Part IV — Calculus and Optimization (260)", "TOCPart"),
             P("Part V — Programming, DSA (260)", "TOCPart"),
             P("Part VI — DBMS and Warehousing (260)", "TOCPart"),
             P("Part VII — Machine Learning (260)", "TOCPart"),
             P("Part VIII — Artificial Intelligence (260)", "TOCPart"),
             P("Part IX — General Aptitude (260)", "TOCPart"),
             P("Part X — Cross-subject notes and CS → DA transfer", "TOCPart"),
             P("Part XI — Ten full-length mocks A–J", "TOCPart"),
             P("Part XII — Formula book", "TOCPart"),
             P("Part XIII — Traps", "TOCPart"),
             P("Part XIV — Top 100 and 30-day plan", "TOCPart"),
             PageBreak(),
             banner("PART I", "GATE DA PATTERN ANALYSIS"), Spacer(1, 4 * mm),
             H("Chapter 1 — What GATE DA is"),
             P("GATE DA is three official papers old. The syllabus for 2027, published by IIT Madras, is the same seven core sections plus GA. "
               "That is a FACT. Frequency-over-three-papers is not a law. A heading that is written in the syllabus remains examinable even if it was quiet.")]
    story += [P(x) for x in FACTS]
    story += [H("Chapter 2 — 2024 / 2025 / 2026", 2),
              P("<b>2024 (IISc).</b> " + YEAR_NOTES["2024"]),
              P("<b>2025 (Roorkee).</b> " + YEAR_NOTES["2025"]),
              P("<b>2026 (Guwahati).</b> " + YEAR_NOTES["2026"]),
              H("Chapter 3 — Study-weight model", 2),
              P(WEIGHT_MODEL.replace("\n", "<br/>"), "BodyTight"),
              H("Chapter 4 — Topic priority map", 2)]
    rows = [["Subj", "Topic", "24", "25", "26", "CS", "Under?", "Priority"]]
    for r in MATRIX:
        rows.append([r[0], r[1], r[2], r[3], r[4], r[5], r[7], r[8]])
    story.append(tbl(rows, [14*mm, 52*mm, 12*mm, 12*mm, 12*mm, 22*mm, 16*mm, 30*mm]))
    story += [H("Under-tested official headings", 3)]
    story += bullets(UNDERTESTED)
    story += [H("House-style traps", 3)]
    story += bullets(TRAPS[:18])

    order = ["P&S", "LA", "Calc", "DSA", "DBMS", "ML", "AI", "GA"]
    for code in order:
        subject_part(story, code, bank[code])

    story += [PageBreak(), banner("PART X", "CS → DA TRANSFER AND DA-ONLY COMBINATIONS"),
              Spacer(1, 3 * mm),
              P("DA is not CS with Python pasted on. Operating systems, compilers, networks, digital logic and named dynamic programming are out of syllabus. "
                "The overlap that remains is high-yield because GATE already knows how to write those questions.")]
    trows = [["CS concept", "CS habit", "DA adaptation"]]
    for a, b, c in CS_TRANSFER:
        trows.append([a, b, c])
    story.append(tbl(trows, [42*mm, 64*mm, 64*mm]))
    story += [H("Combinations that feel like DA", 2)]
    story += bullets([
        "PCA + classifier: unsupervised axes can drop a labelled direction.",
        "Ridge as an optimisation problem: differentiate ||y−Xw||² + λ||w||².",
        "Naive Bayes as a Bayes-net product of class-conditional factors.",
        "BFS as A* with h=0 on unit costs.",
        "SQL AVG as a statistic that ignores NULL.",
        "Projector + residual orthogonality of least squares.",
        "Entropy of a node as a statistic that becomes a split criterion.",
    ])

    papers = all_papers()
    note = {
        "A": "Balanced envelope.", "B": "More eigen / rank / limits.",
        "C": "More regression, PCA, CV, trees.", "D": "More search, logic, Bayes nets.",
        "E": "More Python, sorts, hashing.", "F": "More Bayes and distributions.",
        "G": "FD / SQL / hashing written in a CS accent inside the DA syllabus.",
        "H": "Definition-splitting MSQs.", "I": "More NAT finishes.",
        "J": "Same syllabus, less charity.",
    }
    story += [PageBreak(), banner("PART XI", "TEN FULL-LENGTH MOCK PAPERS"),
              Spacer(1, 3 * mm),
              P("Each paper: 65 questions, 100 marks, 180 minutes. Write answers first. Open that paper’s key only afterwards.")]
    for paper in papers:
        L = paper["letter"]
        story += [PageBreak(), H(f"MOCK PAPER {L} — {THEMES[L]}"),
                  P(note[L]),
                  P("Q1–Q5: 1-mark GA. Q6–Q10: 2-mark GA. Q11–Q35: 1-mark DA. Q36–Q65: 2-mark DA.", "Note")]
        for q in paper["questions"]:
            story.append(qblock(q, q["num"]))
        story += [H(f"MOCK {L} — ANSWER KEY", 2), key_table(paper["questions"], 1),
                  H(f"MOCK {L} — DETAILED SOLUTIONS", 2)]
        for q in paper["questions"]:
            story.append(sblock(q, q["num"]))

    story += [PageBreak(), banner("PART XII", "FORMULA BOOK"), Spacer(1, 3 * mm),
              H("Probability and statistics"),
              P("P(A∪B)=P(A)+P(B)−P(A∩B).  Bayes P(H|E)=P(E|H)P(H)/P(E).  "
                "E[E[X|Y]]=E[X].  Var(X)=E[X²]−(E[X])².  Cov=E[XY]−E[X]E[Y].  "
                "Bernoulli: p, p(1−p).  Binomial: np, np(1−p).  Poisson: λ, λ.  "
                "Uniform[a,b]: (a+b)/2, (b−a)²/12.  Exp(λ): 1/λ, 1/λ².  "
                "X̄ ≈ N(μ, σ²/n).  Two-sided z: |Z|>z_{α/2}."),
              H("Linear algebra", 2),
              P("rank+nullity = #columns.  det=Πλ.  tr=Σλ.  P²=P ⇒ λ∈{0,1}.  "
                "QᵀQ=I ⇒ Q⁻¹=Qᵀ.  Projector A(AᵀA)⁻¹Aᵀ.  uuᵀ has nonzero singular value ||u||²."),
              H("Calculus", 2),
              P("sin x / x → 1.  Taylor f(a)+f'(a)h+f''(a)h²/2.  "
                "Critical: f'=0.  Descent: θ ← θ−η∇L."),
              H("DSA / DBMS / ML / AI", 2),
              P("Binary search Θ(log n).  QS worst Θ(n²) for a fixed bad pivot.  MS extra Θ(n) memory.  "
                "BFS Θ(V+E) on adj lists.  Tree: n−1 edges.  "
                "2NF: no partial dependence.  BCNF: every determinant is a superkey.  SQL: IS NULL, AVG skips NULL.  "
                "Ridge (XᵀX+λI)⁻¹Xᵀy.  H=−Σ p log2 p.  LOOCV trains n models.  "
                "A* consistent h is optimal.  p→q ≡ ¬p∨q.  VE cost ~ treewidth.")]

    story += [PageBreak(), banner("PART XIII", "TRAPS"), Spacer(1, 3 * mm)]
    for i, t in enumerate(TRAPS + [
        "Using training accuracy as generalisation.",
        "PCA treated as supervised.",
        "A* listed with BFS as uninformed.",
        "NULL = NULL taken as TRUE.",
        "Var(X+Y) without uncorrelatedness.",
        "Trace confused with determinant.",
        "MSQ answered with one comfortable option.",
    ], 1):
        story.append(Paragraph(f"<b>TRAP {i:03d}.</b>  {esc(t)}", S["BodyTight"]))

    story += [PageBreak(), banner("PART XIV", "FINAL REVISION"), Spacer(1, 3 * mm),
              H("Thirty-day skeleton"),
              *bullets([
                  "Days 1–4: Probability (Bayes, distributions, covariance, one test/CI item a day).",
                  "Days 5–7: Linear algebra (eigen, rank, projectors, SVD of uuᵀ).",
                  "Days 8–9: Calculus and one-variable optimisation.",
                  "Days 10–13: Python + sorts + hashing + trees + BFS.",
                  "Days 14–16: FDs, BCNF/3NF, SQL NULL, one OLAP item.",
                  "Days 17–21: ML (ridge, PCA, entropy, kNN, NB, k-means, CV).",
                  "Days 22–25: AI (search, logic, d-separation, VE, sampling, minimax).",
                  "Days 26–27: Mock A and Mock F timed.",
                  "Days 28–29: Mock C and Mock I; error log only.",
                  "Day 30: Top formulas + GA set + sleep.",
              ]),
              H("Final 7 days", 2),
              P("One mock every other day. Alternate evenings: trap book only. No new chapters after Day 27."),
              H("Final 24 hours", 2),
              P("Bayes with a base rate. Trace and det. Ridge +λI. A* taxonomy. SQL IS NULL. Then stop."),
              P("End of book.", "Note")]

    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=13 * mm, bottomMargin=13 * mm,
        title="GATE DA 2027 Prediction + Practice Master Book",
        author="Unofficial self-study textbook",
        subject="GATE Data Science and Artificial Intelligence 2027",
    )
    doc.build(story, onFirstPage=cover, onLaterPages=header_footer)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
