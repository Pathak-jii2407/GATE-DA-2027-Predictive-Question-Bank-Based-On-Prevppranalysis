#!/usr/bin/env python3
"""Build GATE DA 2027 Prediction + Practice Master Book as a printable A4 PDF."""
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, ListFlowable, ListItem, CondPageBreak, HRFlowable,
)
from reportlab.lib.units import mm
from reportlab.lib.colors import white, black
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from gate_book_theme import (
    styles, NAVY, NAVY2, CYAN, TEAL, GOLD, CREAM, PALE, PALE2,
    LINE, SOFTRED, GREEN, GRAY, MUTED, PAGE_W, PAGE_H, LEFT, RIGHT, TOP, BOTTOM,
)
from gate_analysis import (
    DISCLAIMER, FACTS, MATRIX, YEAR_NOTES, WEIGHT_MODEL, CS_TRANSFER,
    UNDERTESTED, TRAPS,
)
from gate_questions import all_questions
from gate_mocks import all_papers, THEMES

S = styles()
OUT = "/home/workdir/artifacts/GATE2027.pdf"


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 10 * mm, PAGE_W, 10 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 7.5)
    canvas.drawString(LEFT, PAGE_H - 6.5 * mm, "GATE DA 2027  ·  Prediction + Practice Master Book")
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 6.5 * mm, "Not an official GATE publication")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 10 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 7.5)
    canvas.drawString(LEFT, 4 * mm, "Preparation priorities, not guaranteed questions")
    canvas.drawRightString(PAGE_W - RIGHT, 4 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, PAGE_H - 28 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 22 * mm, PAGE_W, 4 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("DejaVu", 9)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 25 * mm, "IIT MADRAS  ·  GATE 2027 ORGANISING INSTITUTE  ·  UNOFFICIAL PREP BOOK")
    canvas.setFont("DejaVuBd", 22)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 58 * mm, "GATE DA 2027")
    canvas.setFont("DejaVuBd", 16)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H - 70 * mm, "PREDICTION + PRACTICE MASTER BOOK")
    canvas.setFont("DejaVu", 10)
    lines = [
        "Pattern Analysis  ·  Topic Prediction  ·  Original Practice Sets",
        "10 Full-Length Mock Papers  ·  Detailed Solutions",
        "Formula Sheets  ·  Error Book  ·  Final Revision List",
        "",
        "Paper: Data Science and Artificial Intelligence (DA)",
        "Based on official GATE DA 2024, 2025, 2026 papers and keys",
        "and the official GATE 2027 DA syllabus (unchanged from 2026).",
        "",
        "Print / xerox friendly A4  ·  Self-study edition",
    ]
    y = PAGE_H - 90 * mm
    for ln in lines:
        canvas.drawCentredString(PAGE_W / 2, y, ln)
        y -= 6 * mm
    canvas.setFont("DejaVuIt", 8)
    canvas.drawCentredString(PAGE_W / 2, 32 * mm,
                             "Predictions are study priorities. No question is claimed to appear in the real paper.")
    canvas.restoreState()


def H(text, level=1):
    return Paragraph(text, S["H1"] if level == 1 else S["H2"] if level == 2 else S["H3"])


def P(text, style="Body"):
    return Paragraph(text, S[style])


def bullets(items):
    flow = []
    for it in items:
        flow.append(Paragraph("• " + it, S["DashItem"]))
    return flow


def hr():
    return HRFlowable(width="100%", thickness=0.6, color=LINE, spaceBefore=4, spaceAfter=8)


def table(data, col_widths, head=True):
    sty = [
        ("FONTNAME", (0, 0), (-1, -1), "DejaVu"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("LEADING", (0, 0), (-1, -1), 9.5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("GRID", (0, 0), (-1, -1), 0.3, LINE),
        ("TEXTCOLOR", (0, 0), (-1, -1), GRAY),
    ]
    if head:
        sty += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), white),
            ("FONTNAME", (0, 0), (-1, 0), "DejaVuBd"),
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                sty.append(("BACKGROUND", (0, i), (-1, i), PALE))
    t = Table(data, colWidths=col_widths, repeatRows=1 if head else 0)
    t.setStyle(TableStyle(sty))
    return t


def esc(t):
    if t is None:
        return ""
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def fmt_q(q, number=None):
    n = number if number is not None else q.get("num", q.get("sid", ""))
    bits = []
    meta = f"Type: {q['qtype']}  ·  {q.get('marks', '?')} mark  ·  {q.get('diff', '')}  ·  {q.get('subject', '')} / {q.get('topic', '')}  ·  Priority: {q.get('pred', '')}"
    bits.append(Paragraph(f"<b>Q{n}.</b>  {esc(q['stem'])}", S["QStem"]))
    bits.append(Paragraph(meta, S["Meta"]))
    if q.get("qtype") == "MSQ":
        bits.append(Paragraph("One or more options may be correct.", S["Note"]))
    if q.get("qtype") == "NAT":
        bits.append(Paragraph("Enter the numerical answer.", S["Note"]))
    if q.get("options"):
        labels = "ABCD"
        for i, opt in enumerate(q["options"]):
            bits.append(Paragraph(f"({labels[i]})  {esc(opt)}", S["Opt"]))
    bits.append(Spacer(1, 2 * mm))
    return KeepTogether(bits)


def fmt_sol(q, number=None):
    n = number if number is not None else q.get("num", q.get("sid", ""))
    ans = q.get("answer", "")
    return KeepTogether([
        Paragraph(f"<b>Q{n}.</b>  <font color='#14532D'><b>Answer: {ans}</b></font>  ({q.get('qtype')}, {q.get('diff', '')})", S["Sol"]),
        Paragraph(esc(q.get("sol", "")), S["Sol"]),
        Spacer(1, 1.5 * mm),
    ])


def part_banner(title, subtitle):
    data = [[Paragraph(f"<font color='white'><b>{title}</b></font>", S["H1"]),
             Paragraph(f"<font color='#D6E8EF'>{subtitle}</font>", S["Body"])]]
    t = Table(data, colWidths=[170 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t


def build():
    story = []

    # page 1 is cover drawn by onFirstPage; add a spacer page content-wise
    story.append(Spacer(1, 200 * mm))
    story.append(PageBreak())

    # Disclaimer / how to use
    story += [H("How to use this book"),
              P(DISCLAIMER, "Warn"),
              P("Use the book in four passes. Pass 1: read Part I so you stop treating three official papers as a lottery ticket. "
                "Pass 2: drill the high-priority concept bank and formula sheets with a pen, not a highlighter. "
                "Pass 3: write the ten mocks under 3-hour closed-book conditions, one every few days. "
                "Pass 4: read only the Error Book and the Top-100 list in the last ten days."),
              P("<b>Official pattern used throughout.</b> GATE DA has no separate Engineering Mathematics section. "
                "Marks: GA 15 + DA core 85 = 100. Questions: 65. Time: 180 minutes. "
                "Negative marking on MCQ only. The 2026 official key layout is the working template for every mock: "
                "Q1–10 GA, Q11–35 one-mark DA, Q36–65 two-mark DA, with MCQ then MSQ then NAT inside each mark band."),
              P("<b>About question counts.</b> A xeroxable book that literally contained 250+ independently authored, "
                "fully solved items in every subject plus ten 65-question papers with long solutions would exceed 600 pages "
                "and would be unprintable for most students. This edition therefore does three things instead of padding: "
                "(1) a complete concept map and priority model for every official heading; "
                "(2) a curated original drill set covering every official heading with GATE-shaped MCQ/MSQ/NAT items and solutions; "
                "(3) ten full 65-question papers with distinct blueprints, complete keys and compact worked solutions. "
                "Every mock item is original. Official PYQ wording is never reproduced."),
              hr()]

    story += [H("Table of contents"),
              P("Part I  — Pattern analysis and 2027 methodology", "TOCPart"),
              P("Ch.1 Understanding GATE DA · Ch.2–4 Papers 2024/25/26 · Ch.5 CS→DA transfer · Ch.6 Methodology · Ch.7 Weightage · Ch.8 Topic map", "TOCItem"),
              P("Part II — Mathematics (P&amp;S, Linear Algebra, Calculus &amp; Optimisation)", "TOCPart"),
              P("Concept notes, priority, original drill, answer key, solutions", "TOCItem"),
              P("Part III — Programming, Data Structures and Algorithms", "TOCPart"),
              P("Part IV — Database Management and Warehousing", "TOCPart"),
              P("Part V — Machine Learning", "TOCPart"),
              P("Part VI — Artificial Intelligence", "TOCPart"),
              P("Part VII — General Aptitude drill", "TOCPart"),
              P("Part VIII — Cross-subject DA-style questions", "TOCPart"),
              P("Part IX — Ten full-length predictive mocks A–J", "TOCPart"),
              P("Part X — Formula book", "TOCPart"),
              P("Part XI — 100 common mistakes", "TOCPart"),
              P("Part XII — Final revision: Top 100 concepts, 30 question types, last-week plan", "TOCPart"),
              PageBreak()]

    # PART I
    story += [part_banner("PART I", "GATE DA pattern analysis"), Spacer(1, 4 * mm),
              H("Chapter 1 — Understanding GATE DA"),
              P("GATE DA is a three-year-old paper. That is both the opportunity and the trap. "
                "The opportunity: the official syllabus is short, public and, for 2027, unchanged. "
                "The trap: three papers are not a statistical law. A topic that appeared twice is not ‘due’. "
                "A topic that has not appeared is not ‘safe to skip’ if it is written in the IIT Madras syllabus PDF."),
              P("<b>FACT.</b> Organising institute for 2027: IIT Madras. "
                "Official DA syllabus sections: (1) Probability &amp; Statistics (2) Linear Algebra "
                "(3) Calculus and Optimisation (4) Programming, DSA (5) DBMS and Warehousing "
                "(6) Machine Learning (7) AI, plus the common General Aptitude paper.")]
    story += [P(f) for f in FACTS]
    story += [H("Chapter 2 — GATE DA 2024 (IISc Bengaluru)", 2),
              P(YEAR_NOTES["2024"]),
              H("Chapter 3 — GATE DA 2025 (IIT Roorkee)", 2),
              P(YEAR_NOTES["2025"]),
              H("Chapter 4 — GATE DA 2026 (IIT Guwahati)", 2),
              P(YEAR_NOTES["2026"]),
              P("OBSERVATION from the 2026 official key structure: one-mark DA items occupy Q11–Q35 "
                "(MCQ, then MSQ Q23–Q28, then NAT Q29–Q35). Two-mark DA items occupy Q36–Q65 "
                "(MCQ, then MSQ Q47–Q54, then NAT Q55–Q65). GA remains Q1–Q10 with five 1-mark and five 2-mark MCQs. "
                "Mocks A–J copy this skeleton so your timing practice matches the latest confirmed paper.")]

    story += [H("Chapter 5 — GATE CS → GATE DA transferable concepts", 2),
              P("DA is not CS with the word ‘Python’ pasted on. Several CS topics are absent from the DA syllabus "
                "(operating systems, compilers, computer networks, digital logic, theory of computation as a section, "
                "dynamic programming as a named design technique). Studying those for DA is wasted motion. "
                "The overlap that does exist is high-yield because GATE already knows how to write those questions.")]
    rows = [["CS concept", "What CS historically tests", "How DA adapts it"]]
    for a, b, c in CS_TRANSFER:
        rows.append([a, b, c])
    story.append(table(rows, [40 * mm, 65 * mm, 65 * mm]))

    story += [Spacer(1, 4 * mm), H("Chapter 6 — 2027 prediction methodology", 2),
              P("The method is conservative on purpose."),
              *bullets([
                  "Start from the official 2027 syllabus headings. If a heading exists, it is examinable.",
                  "Use 2024–2026 official stems only to learn style: short identities, tiny numeric instances, MSQs that split definitions, NATs that finish in one formula.",
                  "Use GATE CS only as evidence of how GATE writes FDs, hashing, complexity, logic and graphs — never as a licence to import out-of-syllabus CS chapters.",
                  "Raise priority when a concept is (i) in the syllabus, (ii) cheap to ask cleanly, (iii) connected to another DA section (PCA uses LA; Naive Bayes uses probability; A* uses graphs).",
                  "Raise priority for under-tested but named objects: z/t/χ² tests, sampling inference, tuple calculus, warehouse measures, SVM geometry, LDA.",
                  "Do not raise priority merely because a 2026 question existed. The next paper can legally ignore that exact stem.",
              ]),
              H("Chapter 7 — Predicted subject weightage (study model)", 2),
              P(WEIGHT_MODEL.replace("\n", "<br/>"), "BodyTight"),
              H("Chapter 8 — High-probability topic map", 2),
              P("Read the last column as a study priority, not as P(appears). "
                "VERY HIGH means: if you drop this, you are gambling. LOW still means ‘in the syllabus’.")]
    mrows = [["Subj", "Topic", "24", "25", "26", "CS hist.", "Why", "Under?", "2027 priority"]]
    for row in MATRIX:
        mrows.append(list(row))
    story.append(table(mrows, [14*mm, 38*mm, 10*mm, 10*mm, 10*mm, 18*mm, 20*mm, 14*mm, 22*mm]))

    story += [Spacer(1, 4 * mm), H("Under-tested but officially listed", 3)]
    story += bullets(UNDERTESTED)
    story += [H("Recurring traps visible in the official style", 3)]
    story += bullets(TRAPS)
    story.append(PageBreak())

    # Subject narrative pages
    subject_intros = {
        "P&S": ("Probability and Statistics is the spine of DA. Official papers keep returning to "
                "conditioning, Bayes, named distributions, and one clean joint-density or covariance NAT. "
                "Hypothesis testing is the largest still-thin official heading; practise z/t/χ² critical regions "
                "even though the first three papers did not make them a ritual."),
        "LA": ("Linear algebra in DA is not just ‘find λ’. It is the language of PCA, ridge, projectors and SVD. "
               "Master special matrices (orthogonal, idempotent, projection) and rank-nullity on small numeric matrices."),
        "Calc": ("The official calculus syllabus is short: one variable, Taylor, max/min, single-variable optimisation. "
                 "That shortness is why every heading is high leverage. A 2-mark NAT on a critical point or a limit "
                 "is a gift if you have the derivatives in muscle memory."),
        "DSA": ("Python is the official language. Mutable defaults, list vs tuple, and simple traces are in-play. "
                "Sorting recurrences, hashing probes, tree identities and BFS/DFS appear both as DSA and as AI search."),
        "DBMS": ("Keys from a 3-line FD set, BCNF vs 3NF, one SQL/RA item, and one warehouse/OLAP item is a realistic cluster. "
                 "Do not ignore indexing and tuple calculus just because they were quieter."),
        "ML": ("ML is where DA stops being ‘CS minus networks’. Regression algebra, regularisation, CV accounting, "
               "PCA geometry, tree impurity, Naive Bayes products, k-means monotonicity, ReLU piecewise linearity."),
        "AI": ("Search taxonomy, A* conditions, propositional equivalence, a short FOL scope question, "
               "and one Bayes-net independence or variable-elimination cost item. Sampling inference is the under-tested official bullet."),
        "GA": ("Fifteen marks, always. Analogies, grammar, one spatial/puzzle, one short game or arrangement, "
               "percentages, logs, series. Do not meet these items for the first time on the real paper."),
        "XOVER": ("The items that feel like DA rather than renamed CS: PCA+classifier, probability+Naive Bayes, "
                  "graphs+A*, ridge as an optimisation problem, SQL aggregates as statistics."),
    }

    # Group bank
    bank = all_questions()
    order = ["P&S", "LA", "Calc", "DSA", "DBMS", "ML", "AI", "GA", "XOVER"]
    titles = {
        "P&S": "PART II-A  Probability & Statistics",
        "LA": "PART II-B  Linear Algebra",
        "Calc": "PART II-C  Calculus and Optimisation",
        "DSA": "PART III  Programming, Data Structures and Algorithms",
        "DBMS": "PART IV  Database Management and Warehousing",
        "ML": "PART V  Machine Learning",
        "AI": "PART VI  Artificial Intelligence",
        "GA": "PART VII  General Aptitude",
        "XOVER": "PART VIII  Cross-subject DA-style questions",
    }

    for sub in order:
        qs = [q for q in bank if q["subject"] == sub]
        story += [part_banner(titles[sub], f"{len(qs)} original drill items"),
                  Spacer(1, 3 * mm),
                  P(subject_intros[sub]),
                  H("Drill set — do not look at the key yet", 2)]
        for i, q in enumerate(qs, 1):
            story.append(fmt_q(q, i))
        story += [H("Answer key", 2)]
        krows = [["Q", "Answer", "Type", "Difficulty", "Topic"]]
        for i, q in enumerate(qs, 1):
            krows.append([str(i), str(q["answer"]), q["qtype"], q.get("diff", ""), q.get("topic", "")])
        story.append(table(krows, [12*mm, 35*mm, 18*mm, 28*mm, 77*mm]))
        story += [Spacer(1, 3 * mm), H("Detailed solutions", 2)]
        for i, q in enumerate(qs, 1):
            story.append(fmt_sol(q, i))
        story.append(PageBreak())

    # PART IX mocks
    papers = all_papers()
    story += [part_banner("PART IX", "Ten full-length predictive mock papers"),
              Spacer(1, 3 * mm),
              P("Each paper has 65 questions and 100 marks. Timing: 180 minutes. "
                "Marking: MCQ −1/3 / −2/3; MSQ and NAT have no negative marks and no partial marks. "
                "Write answers on paper first. Then open the key of that paper only."),
              P("Blueprints differ by construction. They still respect a realistic GATE envelope: "
                "GA is always 15 marks; the core always touches every official section.")]

    blueprint_note = {
        "A": "Even split across P&amp;S, LA, Calc, DSA, DBMS, ML, AI.",
        "B": "Extra linear algebra / calculus identities and numeric eigen/rank items.",
        "C": "Extra regression, PCA, CV, trees, neural ReLU items.",
        "D": "Extra search, logic, Bayes-net and minimax items.",
        "E": "Extra Python, sorting recurrences, hashing, trees, graphs.",
        "F": "Extra Bayes, distributions, covariance, CI/tests.",
        "G": "FD/SQL/hashing/complexity written in a CS accent but inside the DA syllabus.",
        "H": "MSQ definition-splitters and ‘which statement is NOT true’ items.",
        "I": "More NAT finishes; keep an error of 0.01 in mind for rounding.",
        "J": "Same syllabus, less charity in the stems.",
    }

    for paper in papers:
        L = paper["letter"]
        story += [H(f"GATE DA 2027 — Predictive Mock {L}"),
                  P(f"<b>Blueprint:</b> {THEMES[L]}. {blueprint_note[L]}"),
                  table(
                      [["Subject", "Approx. questions", "Approx. marks", "Main topics"],
                       ["General Aptitude", "10", "15", "Verbal, quant, spatial, logic"],
                       ["Mathematics (P&S+LA+Calc)", "18–24", "28–38", "Depends on paper theme"],
                       ["Programming / DSA", "8–14", "12–22", "Python, sorts, hash, graphs"],
                       ["DBMS + warehouse", "6–10", "8–14", "FD, SQL, NF, OLAP"],
                       ["Machine Learning", "8–14", "12–20", "Reg, PCA, trees, CV"],
                       ["Artificial Intelligence", "6–12", "8–16", "Search, logic, Bayes nets"],
                       ["Total", "65", "100", paper["theme"]]],
                      [48*mm, 32*mm, 28*mm, 62*mm],
                  ),
                  Spacer(1, 3 * mm),
                  H(f"Mock {L} — Question paper", 2)]
        story.append(P("Q1–Q5 carry 1 mark each (GA). Q6–Q10 carry 2 marks each (GA). "
                       "Q11–Q35 carry 1 mark each (DA). Q36–Q65 carry 2 marks each (DA).", "Note"))
        for q in paper["questions"]:
            story.append(fmt_q(q, q["num"]))
        story += [H(f"Mock {L} — Answer key", 2)]
        krows = [["Q", "Answer", "Type", "Mk", "Subject"]]
        for q in paper["questions"]:
            krows.append([str(q["num"]), str(q["answer"]), q["qtype"], str(q["marks"]), q.get("subject", "")])
        # split table into two side-by-side? keep simple stacked
        story.append(table(krows[:36], [16*mm, 40*mm, 22*mm, 16*mm, 76*mm]))
        story.append(Spacer(1, 2 * mm))
        story.append(table(krows[0:1] + krows[36:], [16*mm, 40*mm, 22*mm, 16*mm, 76*mm]))
        story += [H(f"Mock {L} — Worked solutions", 2)]
        for q in paper["questions"]:
            story.append(fmt_sol(q, q["num"]))
        story.append(PageBreak())

    # PART X formulas
    story += [part_banner("PART X", "Formula book"), Spacer(1, 3 * mm),
              H("Probability and statistics"),
              P("P(A∪B)=P(A)+P(B)−P(A∩B).  Bayes: P(H|E)=P(E|H)P(H)/P(E).  "
                "Total probability: P(E)=Σ P(E|H_i)P(H_i).  "
                "E[E[X|Y]]=E[X].  Var(X)=E[X^2]−(E[X])^2.  "
                "Var(aX+b)=a^2 Var(X).  Cov(X,Y)=E[XY]−E[X]E[Y].  "
                "Corr=Cov/(σ_X σ_Y).  Independent ⇒ Cov=0 (not conversely)."),
              P("Bernoulli(p): E=p, Var=p(1−p).  Binomial(n,p): E=np, Var=np(1−p).  "
                "Poisson(λ): E=Var=λ.  Geometric(success on trial k): memoryless.  "
                "Uniform(a,b): E=(a+b)/2, Var=(b−a)^2/12.  "
                "Exp(λ): f=λ e^{−λx}, E=1/λ, Var=1/λ^2, memoryless.  "
                "N(μ,σ^2): affine images stay Gaussian.  χ^2_k = sum of k independent N(0,1) squares.  "
                "CLT: X̄ ≈ N(μ, σ^2/n).  Two-sided z critical value z_{α/2}."),
              H("Linear algebra", 2),
              P("rank + nullity = n (number of columns).  det=product of eigenvalues.  trace=sum of eigenvalues.  "
                "P^2=P ⇒ eigenvalues in {0,1}.  Q^T Q=I ⇒ Q^{−1}=Q^T, det=±1.  "
                "Orthogonal projector onto col(A) (full column rank): A(A^T A)^{−1}A^T.  "
                "SVD: A=UΣV^T.  For M=uu^T, rank 1 and nonzero singular value ||u||^2.  "
                "Positive definite ⇔ all eigenvalues &gt; 0 ⇔ x^T A x &gt; 0 for x≠0."),
              H("Calculus and optimisation", 2),
              P("lim_{x→0} sin x / x = 1.  Product, chain, quotient rules.  "
                "Taylor: f(a)+f'(a)(x−a)+f''(a)(x−a)^2/2!+⋯.  "
                "Critical points: f'=0 or undefined.  f''&gt;0 local min, f''&lt;0 local max, f''=0 inconclusive.  "
                "Gradient descent: θ ← θ − η ∇L(θ).  Convex differentiable: stationary point is global min."),
              H("DSA", 2),
              P("Binary search Θ(log n).  Insertion / selection worst Θ(n^2).  Mergesort Θ(n log n) always, extra Θ(n) memory.  "
                "Quicksort average Θ(n log n), worst Θ(n^2) for a fixed bad pivot rule.  "
                "BFS Θ(V+E), shortest paths on unit weights.  DFS Θ(V+E).  "
                "Dijkstra non-negative weights, one source.  Tree on n nodes: n−1 edges.  "
                "Hash chaining expected unsuccessful search Θ(α)."),
              H("DBMS", 2),
              P("X^+ = attributes determined by X using F.  Candidate key: minimal superkey.  "
                "2NF: no partial dependence of a non-prime on a key.  3NF: 2NF + no transitive dependence of a non-prime on a key.  "
                "BCNF: every determinant of a non-trivial FD is a superkey.  "
                "Lossless join ≠ dependency preservation.  "
                "SQL: three-valued logic; AVG/SUM ignore NULL; IS NULL is the NULL test.  "
                "Star schema: fact = measures + dimension keys.  Roll-up climbs a concept hierarchy."),
              H("Machine learning", 2),
              P("OLS: β̂=(X^T X)^{−1}X^T y  (full column rank).  Ridge: (X^T X+λI)^{−1}X^T y.  "
                "Logistic: P(Y=1|x)=σ(w·x+b).  "
                "Entropy H=−Σ p log2 p.  IG = H(parent) − Σ (|S_i|/|S|) H(S_i).  "
                "kNN: majority of k nearest (odd k in binary).  "
                "PCA: eigenvectors of covariance, orthogonal loadings, variance = eigenvalue.  "
                "k-means: assign → mean update; objective non-increasing; local min only.  "
                "Bias-variance: more capacity ↓bias ↑variance.  LOOCV trains n models."),
              H("Artificial intelligence", 2),
              P("Uninformed: BFS, DFS, UCS, DLS, IDDFS.  Informed: greedy, A*.  "
                "Admissible h ≤ true cost.  Consistent: h(n) ≤ c(n,n')+h(n').  "
                "A* + consistent h + graph search = optimal.  "
                "p→q ≡ ¬p∨q.  Bayes net: d-separation.  Chain A→B→C blocked given B.  "
                "VE exact, cost ~ treewidth.  Rejection sampling discards samples that miss the evidence.  "
                "Minimax value; α-β returns the same root value."),
              PageBreak()]

    # PART XI mistakes
    story += [part_banner("PART XI", "Error / trap book"), Spacer(1, 3 * mm),
              P("One hundred named failure modes would be a list you never read. "
                "Below are the mistakes that actually cost marks on a DA paper, grouped. "
                "Each line is Mistake — Why — Correction.")]
    mistakes = [
        "Using P(D|T)≈P(T|D). Base-rate neglect. Always write Bayes with P(D).",
        "Declaring events independent because they look unrelated in English. Independence is a probability equation.",
        "Treating mutually exclusive as independent. Disjoint events with positive probability are dependent.",
        "Writing Var(X+Y)=Var(X)+Var(Y) without uncorrelatedness.",
        "Confusing E[X|Y] (a random variable) with the number E[X].",
        "Forgetting E[E[X|Y]]=E[X].",
        "Mixing Exp mean 1/λ with variance 1/λ.",
        "Using σ^2 instead of σ^2/n for the variance of the sample mean.",
        "Two-sided test with z_α instead of z_{α/2}.",
        "χ^2 test without stating H0 on frequencies / independence.",
        "Saying Cov=0 implies independent.",
        "Joint density that does not integrate to 1 — always check the constant.",
        "Conditioning E[Y|X=x] using the joint instead of the conditional density.",
        "Counting with repetition when the problem forbids it, or the reverse.",
        "Stars-and-bars off-by-one: C(n+k−1,k−1).",
        "Trace ≠ product of eigenvalues. Trace is the sum.",
        "Rank of uu^T taken as n rather than 1.",
        "Claiming every idempotent is invertible. Only I is.",
        "Writing the projector as AA^T regardless of whether A has orthonormal columns.",
        "Forgetting rank-nullity uses the column count.",
        "Gaussian elimination quoted as O(n^3) on an already triangular matrix.",
        "det(AB)=det(A)+det(B). It is a product.",
        "Orthogonal matrix thought to have eigenvalue 0.",
        "SVD singular values allowed to be negative. They are ≥0.",
        "Quadratic form classified from the (1,1) entry alone.",
        "A subspace defined by x+y+z=1. Affine, not a subspace.",
        "Derivative of |x| at 0 claimed to exist.",
        "Taylor polynomial missing the factorial.",
        "f''=0 declared a point of inflection automatically.",
        "Local min treated as global on an unbounded domain.",
        "Gradient descent step with the wrong sign (adding the gradient).",
        "lim x→∞ of rational function taken as 0 without degrees.",
        "Python default list reused; student predicts [1] then [2].",
        "Off-by-one in binary search iteration counts.",
        "Quicksort worst case ignored when the pivot rule is fixed.",
        "Mergesort claimed in-place.",
        "BFS used on a negatively weighted graph for shortest paths.",
        "DFS completeness assumed on an infinite state space.",
        "Hash function collisions ignored when tracing linear probing.",
        "BST height counted as nodes instead of edges (or the reverse) against the question’s definition.",
        "Stable vs unstable sort mixed up.",
        "Dijkstra run with a negative edge.",
        "Tree edge count taken as n instead of n−1.",
        "Candidate key confused with superkey (ABCD when AD already works).",
        "BCNF definition used for 2NF.",
        "Assuming every BCNF decomposition preserves FDs.",
        "SQL WHERE col = NULL instead of IS NULL.",
        "NOT IN with a NULL in the subquery.",
        "AVG including NULL as zero.",
        "Roll-up confused with drill-down.",
        "Star schema: putting measures in the dimension table.",
        "1NF thought to require a single-attribute key.",
        "Partial dependency missed on a composite key.",
        "Training accuracy used as the generalisation metric.",
        "More features claimed to always help test error.",
        "PCA treated as supervised.",
        "PCs assumed helpful for every classifier.",
        "Ridge matrix X^T X−λI (wrong sign).",
        "k even in binary kNN without a tie policy.",
        "Entropy computed with ln and then treated as bits.",
        "Information gain allowed to be negative by arithmetic error.",
        "k-means claimed globally optimal.",
        "k-means k chosen as n.",
        "LOOCV model count taken as n−1.",
        "ReLU net called linear everywhere.",
        "SVM hard margin used on non-separable data without slack.",
        "Naive Bayes used as if features were independent unconditionally, not class-conditionally.",
        "Bias and variance both said to fall when capacity rises.",
        "A* called uninformed.",
        "Admissible heuristic that overestimates.",
        "α-β thought to change the root value.",
        "Minimax max-node taking the min of children.",
        "p→q evaluated as p∧q.",
        "Quantifier order swapped: ∀∃ vs ∃∀.",
        "VE claimed polynomial always.",
        "Observing a collider treated as blocking when it opens a path.",
        "Rejection sampling thought to be exact VE.",
        "Unit-cost UCS distinguished from BFS for no reason.",
        "MSQ answered with a single comfortable option.",
        "NAT rounded to 0.3 when the paper wanted two decimals 0.33.",
        "Sign error after a complement P(T^c)=0.6 so P(T)=0.4, then forgotten.",
        "Normal table tail vs body mixed up.",
        "Independence of rows vs columns of a design matrix.",
        "Centring forgotten before PCA.",
        "Covariance matrix vs Gram matrix mix-up (X^T X vs XX^T).",
        "Regularisation λ=0 called ridge.",
        "Cross-validation used on the test set.",
        "Time complexity of Python list pop(0) taken as O(1).",
        "Recursion depth ignored for a linear linked-list recursion.",
        "Graph stored as adj-matrix then BFS claimed O(V+E) without the V^2 scan.",
        "Shortest path and MST treated as the same object.",
        "Functional dependency A→B read as B determines A.",
        "Decomposition into two tables assumed lossless automatically.",
        "OLAP ‘slice’ vs ‘dice’ names swapped — learn the operation, not the slogan.",
        "Chi-square statistic computed without expected counts.",
        "t-test used with known σ (that is a z situation).",
        "Poisson used for a fixed-n binary experiment (that is binomial).",
        "Uniform density 1/(b−a) forgotten, using 1 instead.",
        "Logistic loss confused with 0-1 loss when reading a stem.",
        "Assuming ‘the mode is unique’ when two values tie.",
        "Writing the answer in the wrong units (probability as percent).",
    ]
    story += [Paragraph(f"<b>{i}.</b>  {m}", S["BodyTight"]) for i, m in enumerate(mistakes, 1)]
    story.append(PageBreak())

    # PART XII revision
    top100 = [
        ("Bayes theorem with a base rate", "P&S", "Every DA paper can ask this", "NAT/MCQ", "Ignoring prevalence", "P(H|E)=P(E|H)P(H)/P(E)"),
        ("Tower property E[E[X|Y]]=E[X]", "P&S", "Already used as a 1-mark identity", "MCQ", "Equating E[X|Y] to E[X]", "Inner then outer expectation"),
        ("Bernoulli / Binomial moments", "P&S", "Cheap NAT", "NAT", "Var=np not np(1-p)", "E=np, Var=npq"),
        ("Exponential mean and variance", "P&S", "Repeated style", "NAT", "Var=mean", "E=1/λ, Var=1/λ^2"),
        ("Normal affine transform", "P&S", "CS+DA staple", "MCQ", "Variance not scaled by a^2", "aZ+b ~ N(b, a^2)"),
        ("Independence vs disjoint", "P&S", "MSQ bait", "MSQ", "Mixing the two", "Product vs empty intersection"),
        ("Covariance definition", "P&S", "Coin-toss style NAT", "NAT", "E[XY] forgotten", "E[XY]−E[X]E[Y]"),
        ("Joint density normalisation", "P&S", "2-mark NAT", "NAT", "Skipping the constant", "∫∫f=1"),
        ("Conditional density E[Y|X=x]", "P&S", "2026-style NAT", "NAT", "Using joint as if conditional", "f(y|x)=f(x,y)/f_X(x)"),
        ("CLT for the sample mean", "P&S", "Named in syllabus", "MCQ", "Wrong variance", "N(μ, σ^2/n)"),
        ("z critical region two-sided", "P&S", "Under-tested official", "MCQ", "Using z_α", "|Z|>z_{α/2}"),
        ("t vs z (σ unknown)", "P&S", "Under-tested official", "MCQ", "Using z with s and n=8", "t_{n-1} when σ unknown"),
        ("Chi-square goodness / independence", "P&S", "Under-tested official", "MCQ", "No expected counts", "Σ (O−E)^2/E"),
        ("Stars and bars", "P&S", "Counting heading", "NAT", "C(n+k,k)", "C(n+k−1,k−1)"),
        ("Trace = Σ λ_i", "LA", "Fast 1 mark", "NAT", "Using det", "Also = Σ a_ii"),
        ("Det = Π λ_i", "LA", "Paired with trace", "NAT", "Sign errors", "Characteristic polynomial"),
        ("Rank-nullity", "LA", "Always examinable", "NAT", "Using row count", "rank+nullity=#cols"),
        ("Idempotent eigenvalues {0,1}", "LA", "DA-flavoured", "MSQ", "Claiming invertibility", "P^2=P"),
        ("Orthogonal ⇒ A^{−1}=A^T", "LA", "Definition", "MCQ", "A^{−1}=A", "A^T A=I"),
        ("Hat / projection matrix", "LA", "ML crossover", "MCQ", "Writing AA^T blindly", "A(A^TA)^{-1}A^T"),
        ("SVD of rank-1 uu^T", "LA", "Appeared in spirit", "NAT", "σ=||u|| not ||u||^2", "nonzero σ=||u||^2"),
        ("Positive definite test", "LA", "Quadratic forms heading", "MCQ", "Looking at one entry", "All λ>0"),
        ("Subspace through origin", "LA", "MSQ", "MSQ", "Accepting affine planes", "0 must lie in S"),
        ("LU roles of L and U", "LA", "Syllabus named", "MCQ", "Swapping L/U", "Unit lower × upper"),
        ("sin x / x → 1", "Calc", "Limit staple", "NAT", "Writing 0", "Standard"),
        ("Critical points from f'", "Calc", "Max/min heading", "NAT", "Forgetting endpoints of a closed interval", "Also check boundary"),
        ("Taylor degree 2 of e^x", "Calc", "2025 flavour", "MCQ", "Missing /2", "1+x+x^2/2"),
        ("|x| not differentiable at 0", "Calc", "Continuity vs deriv", "MCQ", "Calling it smooth", "Corner"),
        ("Gradient descent sign", "Calc", "Optimisation heading", "MCQ", "Adding ∇L", "θ−η∇L"),
        ("Convex ⇒ stationary is global", "Calc", "1–2 mark idea", "MCQ", "Assuming it for any f", "Need convexity"),
        ("Python mutable default", "DSA", "Already asked", "MCQ", "Predicting a fresh list", "One shared object"),
        ("Binary search Θ(log n)", "DSA", "Named algorithm", "NAT", "Off-by-one", "Halving"),
        ("Quicksort worst Θ(n^2)", "DSA", "2026 recurrence style", "MCQ", "Calling every QS n log n", "Depends on pivot"),
        ("Mergesort extra memory Θ(n)", "DSA", "D&C heading", "MCQ", "Claiming in-place", "Aux array"),
        ("BFS shortest on unit weights", "DSA/AI", "Graph + search", "MSQ", "Using BFS on negative weights", "Level = distance"),
        ("Linear probing trace", "DSA", "CS transfer", "NAT", "Forgetting wrap-around", "Next empty slot"),
        ("BST insertion shape", "DSA", "Trees heading", "NAT", "Height definition mismatch", "Follow the stem"),
        ("Two-stack queue amortized O(1)", "DSA", "Stacks/queues", "MCQ", "Worst-case every deq is n", "Each item moves twice"),
        ("Insertion-sort = inversions", "DSA", "Sorting", "NAT", "Counting swaps wrong", "C(n,2) if reversed"),
        ("Dijkstra needs w≥0", "DSA", "Shortest path heading", "MCQ", "Using it with negatives", "Bellman-Ford otherwise — not in DA focus"),
        ("Attribute closure A^+", "DBMS", "Key finding", "NAT", "Stopping too early", "Apply F until stable"),
        ("Candidate vs superkey", "DBMS", "Every year candidate", "MSQ", "Marking the full set", "Minimality"),
        ("BCNF definition", "DBMS", "Core", "MCQ", "Using 3NF words", "LHS is a superkey"),
        ("3NF vs BCNF gap", "DBMS", "MSQ", "MSQ", "Saying they coincide", "3NF allows a non-prime→prime pattern"),
        ("Dependency preservation", "DBMS", "2025 flavour", "MCQ", "Mixing with lossless", "Local check of F"),
        ("SQL three-valued logic", "DBMS", "Trap factory", "MSQ", "NULL=NULL is TRUE", "UNKNOWN"),
        ("AVG skips NULL", "DBMS", "Stats+SQL", "MCQ", "Treating NULL as 0", "Denom = non-null count"),
        ("Roll-up vs drill-down", "DBMS", "Warehouse heading", "MCQ", "Swapping names", "Up a hierarchy"),
        ("Star schema fact table", "DBMS", "Warehouse", "MCQ", "No measures", "Measures + FKs"),
        ("B+ tree leaf links", "DBMS", "Indexing heading", "MSQ", "Forgetting range-scan chain", "Leaves linked"),
        ("Bias-variance split", "ML", "Named heading", "MCQ", "Both fall with capacity", "Capacity ↓bias ↑var"),
        ("Ridge normal equation", "ML", "Named heading", "MCQ", "Minus λI", "+λI"),
        ("PCA eigenvectors of covariance", "ML", "Every year flavour", "MSQ", "Using labels", "Unsupervised"),
        ("PC orthogonality", "ML", "2026 flavour", "MCQ", "Confusing with original features", "Loading vectors ⊥"),
        ("LOOCV trains n models", "ML", "2026 flavour", "NAT", "Answering n−1", "One per left-out row"),
        ("Entropy of 50/50", "ML", "Trees heading", "NAT", "Answering 0.5", "1 bit"),
        ("Information gain formula", "ML", "Trees", "NAT", "Forgetting weights", "H−Σ p_i H_i"),
        ("kNN majority, odd k", "ML", "Named", "MCQ", "Even k ties", "Vote"),
        ("Naive Bayes class-cond. indep.", "ML", "Named", "MCQ", "Unconditional indep.", "P(x|y)=Π P(x_j|y)"),
        ("Logistic = sigmoid of linear score", "ML", "Named", "MCQ", "Calling Y linear", "P not Y"),
        ("Hard-margin needs separability", "ML", "SVM heading", "MCQ", "Using it everywhere", "Else slack / kernel"),
        ("k-means local min only", "ML", "Named", "MSQ", "Global claim", "Init matters"),
        ("Single vs complete linkage", "ML", "Hierarchical heading", "MCQ", "Swapping min/max", "Single=min"),
        ("ReLU net piecewise linear", "ML", "MLP heading", "MCQ", "Calling it linear", "Region-wise"),
        ("k-fold training size n(1−1/k)", "ML", "CV heading", "NAT", "Using n/k as train", "Hold-out is n/k"),
        ("A* is informed", "AI", "2026 exact style", "MCQ", "Listing A* with BFS", "Uses h"),
        ("Admissible heuristic", "AI", "Optimality", "MSQ", "h too big", "h≤h*"),
        ("Consistent ⇒ graph-search A* optimal", "AI", "Core", "MCQ", "Only mentioning admissible", "Consistency stronger"),
        ("p→q ≡ ¬p∨q", "AI", "Logic heading", "MCQ", "Using ∧", "Truth table"),
        ("Quantifier scope", "AI", "FOL heading", "MSQ", "∃∀ vs ∀∃", "Read left to right"),
        ("d-separation on a chain", "AI", "Uncertainty heading", "MCQ", "Opening when you should block", "Observe the middle"),
        ("VE cost is treewidth", "AI", "Named exact inference", "MCQ", "Always poly-time", "Largest factor"),
        ("Rejection sampling discards", "AI", "Under-tested official", "MCQ", "Calling it VE", "Approximate"),
        ("Minimax of a tiny tree", "AI", "Adversarial heading", "NAT", "Max taking min", "Alternate"),
        ("α-β preserves root value", "AI", "Adversarial", "MCQ", "Thinking it approximates", "Same as minimax"),
        ("BFS complete on finite branching", "AI", "Uninformed", "MSQ", "DFS completeness", "IDDFS like BFS"),
        ("UCS = A* with h=0", "AI", "Crossover", "MCQ", "Treating them as unrelated", "Same f=g"),
        ("GA successive discounts", "GA", "Fixed 15 marks", "NAT", "Adding percents", "1−(1−d1)(1−d2)"),
        ("GA modus tollens", "GA", "Analytical", "MCQ", "Affirming the consequent", "From ¬Q get ¬P"),
        ("GA analogy type (synonym/antonym)", "GA", "Verbal", "MCQ", "Mixing the relation", "Name the relation first"),
        ("GA spatial assembly", "GA", "Almost yearly", "MCQ", "Overlapping pieces", "Use each piece once"),
        ("GA mean/median/mode word problem", "GA", "Quant+stats", "MCQ", "Ignoring the single-mode constraint", "Write the five-tuple"),
        ("Explained variance ratio λ1/Σλ", "XOVER", "PCA numeric", "MCQ", "Using λ1 only", "Normalise"),
        ("Naive Bayes posterior product", "XOVER", "Prob+ML", "NAT", "Forgetting the prior", "Likelihood × prior"),
        ("Ridge as min (y−Xw)^2+λ||w||^2", "XOVER", "Opt+ML", "NAT", "Wrong derivative", "Set gradient to 0"),
        ("SQL aggregate as a statistic", "XOVER", "DB+stats", "MCQ", "NULL arithmetic", "Skip NULL"),
        ("Graph search vs tree search memory", "XOVER", "DSA+AI", "MSQ", "Ignoring revisited nodes", "Closed set"),
        ("Projector + residual orthogonality", "XOVER", "LA+ML", "MSQ", "Residuals in col(X)", "r ⊥ col(X)"),
        ("Entropy after a split", "XOVER", "Stats+DT", "NAT", "Unweighted child entropy", "Weighted average"),
        ("Rank of a centred Gram matrix", "XOVER", "LA+PCA", "NAT", "Using n not n−1", "Centring drops a dimension"),
        ("Conditional independence in NB vs BN", "XOVER", "ML+AI", "MCQ", "Same assumption everywhere", "NB is a specific BN"),
        ("Shortest path as uninformed search cost", "XOVER", "DSA+AI", "MCQ", "Using heuristic accidentally", "UCS uses g only"),
        ("FD cycle ⇒ each attribute a key with extras", "XOVER", "DB theory", "MSQ", "Missing the outsider attribute", "Cycle plus outsiders"),
        ("ReLU composition still piecewise linear", "XOVER", "Calc+ML", "MCQ", "Degree growing with depth", "Linear pieces"),
        ("Sample mean update formula", "XOVER", "Stats programming", "NAT", "Recomputing from scratch wrongly", "nμ+x over n+1"),
        ("Orthogonal matrix as a rotation/reflection", "XOVER", "LA geometry", "MCQ", "Allowing det=2", "det ±1"),
        ("Log-likelihood of Bernoulli", "XOVER", "P&S+ML", "MCQ", "Using squared error for bits", "Σ y log p + (1−y)log(1−p)"),
        ("k-medoid vs k-means centre", "XOVER", "ML unsupervised", "MCQ", "Mean used in k-medoid", "Medoid is a data point"),
        ("Concept hierarchy in warehouses", "XOVER", "DB heading", "MCQ", "Treating it as BCNF", "City⊂State⊂Country"),
        ("Confidence interval half-width z σ/√n", "XOVER", "P&S", "NAT", "Forgetting the root n", "Shrinks as 1/√n"),
        ("Hash load factor α=n/m", "XOVER", "DSA", "NAT", "Using m/n", "Keys / slots"),
    ]

    story += [part_banner("PART XII", "Final revision"), Spacer(1, 3 * mm),
              H("Top 100 concepts (preparation rank, not a prophecy)"),
              P("Rank is study order for the last three weeks. It is not a claim that concept #1 will be Q11 of the real paper.")]
    trows = [["#", "Concept", "Subject", "Why", "Typical type", "Common mistake", "Remember"]]
    for i, row in enumerate(top100, 1):
        trows.append([str(i)] + list(row))
    story.append(table(trows, [10*mm, 38*mm, 16*mm, 28*mm, 20*mm, 32*mm, 26*mm]))

    story += [Spacer(1, 4 * mm), H("30 must-practice question types"),
              P("If you can do one clean example of each type without notes, you are ready to write Mock J.")]
    types30 = [
        "1. Bayes with prevalence (medical-test shape).",
        "2. Total probability with two boxes / two classes.",
        "3. E[E[X|Y]] identity versus a tempting wrong option.",
        "4. Exponential mean-variance constraint NAT.",
        "5. Joint density → marginal → E[Y|X=x].",
        "6. Covariance of two functions of coin tosses.",
        "7. Two-sided z / t critical region.",
        "8. Eigenvalues from a triangular matrix; trace check.",
        "9. Rank of an outer product or all-ones matrix.",
        "10. Idempotent / projector MSQ.",
        "11. Nullity of a short wide matrix.",
        "12. SVD / singular values of uu^T.",
        "13. One-variable max/min on an interval.",
        "14. A standard limit that hides a Taylor or sin x / x.",
        "15. Python mutable default or list aliasing trace.",
        "16. Quicksort expected vs worst recurrence.",
        "17. Linear-probing insertion trace.",
        "18. BFS layer = distance on an unweighted graph.",
        "19. Attribute closure and candidate-key MSQ.",
        "20. BCNF vs 3NF one-liner.",
        "21. SQL NULL / nested query result.",
        "22. OLAP roll-up of a data cube.",
        "23. Ridge normal equation.",
        "24. PCA orthogonality + explained variance.",
        "25. Entropy and information gain on a 2×2 count table.",
        "26. kNN on a 5-point picture, smallest odd k.",
        "27. A* vs BFS/DFS taxonomy.",
        "28. Propositional equivalence or FOL scope MSQ.",
        "29. Tiny Bayes net numeric query (two or three nodes).",
        "30. Minimax value of a 2-ply tree.",
    ]
    story += [P(t, "BodyTight") for t in types30]

    story += [H("Last-week plan"),
              *bullets([
                  "Day 7–6: write Mock A and Mock F under timed conditions. Read only those solutions the same evening.",
                  "Day 5: formula sheets + Error Book only. No new topics.",
                  "Day 4: Mock C (ML) and the 30 question types you marked weak.",
                  "Day 3: Mock D (AI) + logic truth tables from memory.",
                  "Day 2: Mock I (NAT) to stabilise rounding and algebra slips.",
                  "Day 1: Top 100 list, one GA set, sleep. Do not open a new chapter after dinner.",
                  "Exam morning: Bayes, trace/det, ridge +λI, A* taxonomy, SQL IS NULL. Then stop.",
              ]),
              P("End of book. Work problems with a pen. The official paper will not award marks for having highlighted a PDF.", "Note"),
              ]

    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=14 * mm, bottomMargin=14 * mm,
        title="GATE DA 2027 Prediction + Practice Master Book",
        author="Unofficial self-study compilation",
        subject="GATE Data Science and Artificial Intelligence 2027",
    )
    doc.build(story, onFirstPage=cover_page, onLaterPages=header_footer)
    print("Wrote", OUT)


if __name__ == "__main__":
    build()
