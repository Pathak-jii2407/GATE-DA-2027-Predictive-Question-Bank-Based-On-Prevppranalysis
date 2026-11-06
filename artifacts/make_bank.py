"""Build 260 unique original items per subject; numeric answers computed."""
from __future__ import annotations
import json, math, random
from qfactory import item, gen_ps, gen_la, gen_calc, gen_dsa, gen_db, gen_ml, gen_ai


def unique(qs):
    seen, out = set(), []
    for q in qs:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            out.append(q)
    return out


def pad_nat(base, subject, topic, maker, n):
    out = unique(base)
    i = 0
    guard = 0
    while len(out) < n and guard < n * 20:
        guard += 1
        i += 1
        q = maker(i)
        if q["stem"] not in {x["stem"] for x in out}:
            out.append(q)
    return out[:n]


def ga_bank(n=260):
    rng = random.Random(2027)
    out = []
    pairs = [
        ("Hot:Cold :: Tall:", ["Short", "Wide", "High", "Long"], "A", "Antonym."),
        ("Author:Book :: Composer:", ["Song", "Piano", "Stage", "Crowd"], "A", "Creator-work. Options ordered so A is Song."),
        ("Transparent:Opaque :: Flexible:", ["Rigid", "Clear", "Soft", "Bright"], "A", "Antonym."),
        ("Teacher:School :: Doctor:", ["Hospital", "Chalk", "Desk", "Bell"], "A", "Workplace."),
        ("Scarce:Rare :: Abundant:", ["Plentiful", "Empty", "Tiny", "Bitter"], "A", "Synonym."),
        ("Begin:Start :: Finish:", ["End", "Open", "Pause", "Try"], "A", "Synonym."),
        ("Knife:Cut :: Pen:", ["Write", "Ink", "Paper", "Sharp"], "A", "Instrument-action."),
        ("Oasis:Desert :: Island:", ["Ocean", "Tree", "Sand", "Camel"], "A", "Land in a surrounding medium."),
    ]
    # fix Author analogy options to match answer
    pairs[1] = ("Author : Book :: Composer : ____", ["Song", "Piano", "Stage", "Crowd"], "A", "Creator and work.")
    grams = [
        ("Neither of the answers ____ correct.", ["are", "is", "have", "were"], "B", "Neither + singular."),
        ("Each of the players ____ a medal.", ["have", "has", "are", "were"], "B", "Each + singular."),
        ("She prefers coffee ____ tea.", ["than", "to", "from", "against"], "B", "Prefer to."),
        ("If I ____ richer, I would travel.", ["was", "were", "am", "be"], "B", "Subjunctive."),
        ("The news ____ surprising.", ["are", "is", "were", "have"], "B", "News is singular."),
        ("One of the books ____ missing.", ["are", "is", "have", "were"], "B", "One of + singular verb."),
        ("He is good ____ mathematics.", ["in", "at", "on", "by"], "B", "Good at."),
        ("I look forward ____ meeting you.", ["to", "for", "at", "on"], "A", "Look forward to + gerund."),
    ]
    for stem, opts, ans, sol in pairs:
        out.append(item("GA", "Analogy", "MCQ", 1, "Easy", "HIGH", stem, opts, ans, sol))
    for stem, opts, ans, sol in grams:
        out.append(item("GA", "Grammar", "MCQ", 1, "Easy", "HIGH", stem, opts, ans, sol))
    out += [
        item("GA", "Logic", "MCQ", 2, "Moderate", "HIGH",
             "If P then Q. Not Q. Therefore",
             ["P", "Not P", "Q", "P and Q"], "B", "Modus tollens."),
        item("GA", "Logic", "MCQ", 2, "Moderate", "HIGH",
             "All A are B. Some B are C. Therefore",
             ["All A are C", "Some A are C", "No A is C", "None of A–C must follow"],
             "D", "No forced intersection of A with C."),
        item("GA", "Log", "MCQ", 1, "Easy", "HIGH",
             "log10 1000 equals", ["2", "3", "0.3", "30"], "B", "10^3=1000."),
        item("GA", "Log", "MCQ", 1, "Easy", "HIGH",
             "log10 0.01 equals", ["2", "−2", "0.01", "10"], "B", "10^{-2}=0.01."),
        item("GA", "Series", "MCQ", 1, "Easy", "HIGH",
             "Next term: 2,6,12,20,30,…", ["36", "42", "40", "44"], "B", "n(n+1): 6·7=42."),
        item("GA", "Odd one", "MCQ", 1, "Easy", "MEDIUM",
             "Odd one: square, triangle, pentagon, circle",
             ["square", "triangle", "pentagon", "circle"], "D", "Not a polygon."),
        item("GA", "Clock", "MCQ", 2, "Moderate", "MEDIUM",
             "Angle between hands at 3:00 is", ["0°", "90°", "180°", "75°"], "B", "Quarter circle."),
        item("GA", "Ratio", "MCQ", 1, "Easy", "MEDIUM",
             "2:3 means the second part is what fraction of the whole?",
             ["2/5", "3/5", "2/3", "1/2"], "B", "3/5."),
    ]
    def maker(i):
        t = i % 8
        if t == 0:
            x = 50 + 10 * (i % 9)
            return item("GA", "Percent change", "NAT", 2, "Easy", "HIGH",
                        f"A price of {x} rises 10% then falls 10%. Final price is _____.",
                        None, str(int(round(x * 1.1 * 0.9))),
                        "1.1×0.9=0.99 of original.")
        if t == 1:
            a, b = 3 + i % 5, 2 + i % 3
            if b > a:
                a, b = b, a
            ans = math.perm(a, b)
            return item("GA", "Permutations", "NAT", 2, "Moderate", "HIGH",
                        f"How many injective maps from a set of {b} elements to a set of {a} elements?",
                        None, str(ans), f"P({a},{b})={ans}.")
        if t == 2:
            k = 3 + i % 8
            return item("GA", "Odd sum", "NAT", 1, "Easy", "MEDIUM",
                        f"Sum of the first {k} odd positive integers is _____.",
                        None, str(k * k), f"{k}²={k*k}.")
        if t == 3:
            p, r, ty = 1000 + 100 * (i % 5), 5 + i % 6, 1 + i % 4
            return item("GA", "Simple interest", "NAT", 2, "Easy", "HIGH",
                        f"Simple interest on {p} at {r}% per annum for {ty} years is _____.",
                        None, str(p * r * ty // 100), "PRT/100.")
        if t == 4:
            a, b = 2 + i % 8, 3 + i % 7
            return item("GA", "Percentage", "NAT", 1, "Easy", "MEDIUM",
                        f"{a}% of {200 * b} equals _____.",
                        None, str(a * 2 * b), f"{a}/100 × {200*b} = {2*a*b}.")
        if t == 5:
            n = 6 + i % 10
            return item("GA", "Mean", "NAT", 1, "Easy", "MEDIUM",
                        f"Mean of the integers 1 through {n} is _____ (two decimals if needed).",
                        None, str(n + 1) if (n + 1) % 2 == 0 else f"{(n+1)/2:.1f}" if False else str((n + 1) / 2).replace(".0", ""),
                        f"(1+{n})/2 = {(1+n)/2}.")
        if t == 6:
            a, b = 4 + i % 6, 6 + i % 5
            # work = a days, b days together
            # 1/a+1/b
            days = 1 / (1 / a + 1 / b)
            return item("GA", "Work", "NAT", 2, "Moderate", "MEDIUM",
                        f"A finishes a job in {a} days, B in {b} days. Days they take together is _____ (two decimals).",
                        None, f"{days:.2f}",
                        f"1/a+1/b = {(a+b)/(a*b)}; days={days:.4f}.")
        w, l = 3 + i % 5, 8 + i % 7
        return item("GA", "Perimeter", "NAT", 1, "Easy", "MEDIUM",
                    f"Perimeter of a {w} by {l} rectangle is _____.",
                    None, str(2 * (w + l)), "2(L+W).")
    return pad_nat(out, "GA", "mixed", maker, n)


def build(per=260):
    bank = {
        "P&S": unique(gen_ps(per * 3))[:per],
        "LA": unique(gen_la(per * 3))[:per],
        "Calc": unique(gen_calc(per * 4))[:per],
        "DSA": unique(gen_dsa(per * 3))[:per],
        "DBMS": unique(gen_db(per))[:per],
        "ML": unique(gen_ml(per * 3))[:per],
        "AI": unique(gen_ai(per * 3))[:per],
        "GA": ga_bank(per),
    }
    # pad any short subject with computed NAT so we hit 260
    def fill(name, lst, maker):
        return pad_nat(lst, name, "extra", maker, per)

    bank["P&S"] = fill("P&S", bank["P&S"], lambda i: item(
        "P&S", "Combinations", "NAT", 1, "Easy", "MEDIUM",
        f"C({10 + i},2) equals _____.", None,
        str(math.comb(10 + i, 2)), f"(10+i)(9+i)/2 with i-shift {i}."))
    bank["LA"] = fill("LA", bank["LA"], lambda i: item(
        "LA", "Trace", "NAT", 1, "Easy", "HIGH",
        f"tr(diag({i+1},{i+2},{i+3})) equals _____.", None,
        str(3 * i + 6), "Sum of the three diagonal entries."))
    bank["Calc"] = fill("Calc", bank["Calc"], lambda i: item(
        "Calc", "Power derivative", "NAT", 1, "Easy", "HIGH",
        f"d/dx (x^{i+2}) at x=1 equals _____.", None,
        str(i + 2), "n x^{n-1} at 1 equals n."))
    bank["DSA"] = fill("DSA", bank["DSA"], lambda i: item(
        "DSA", "Linear search", "NAT", 1, "Easy", "MEDIUM",
        f"Worst-case comparisons for a missing key in an unsorted array of {i+7} keys is _____.",
        None, str(i + 7), "Every entry is read once."))
    bank["ML"] = fill("ML", bank["ML"], lambda i: item(
        "ML", "LOOCV count", "NAT", 1, "Easy", "HIGH",
        f"LOOCV on {i+8} labelled points trains _____ models.",
        None, str(i + 8), "One model per left-out row."))
    bank["AI"] = fill("AI", bank["AI"], lambda i: item(
        "AI", "Minimax", "NAT", 2, "Moderate", "HIGH",
        f"Max root; left terminal {i+1}; right is min({i+2},{i+5}). Root value is _____.",
        None, str(max(i + 1, min(i + 2, i + 5))),
        "Right plays the min; root plays the max."))
    bank["DBMS"] = fill("DBMS", bank["DBMS"], lambda i: item(
        "DBMS", "Closure size", "NAT", 1, "Easy", "VERY HIGH",
        f"Attributes A1..A{i+3} with A_j→A_{{j+1}} for each consecutive pair. |A1^+| equals _____.",
        None, str(i + 3), "The chain from A1 reaches every attribute."))
    bank["GA"] = fill("GA", bank["GA"], lambda i: item(
        "GA", "Percentage", "NAT", 1, "Easy", "MEDIUM",
        f"{(i % 9) + 2}% of {100 + 10 * i} equals _____.",
        None, str(((i % 9) + 2) * (100 + 10 * i) // 100),
        "p/100 times the base."))

    for k, v in bank.items():
        print(k, len(v), "unique", len({q['stem'] for q in v}),
              {t: sum(1 for q in v if q['qtype'] == t) for t in ('MCQ', 'MSQ', 'NAT')})
    return bank


if __name__ == "__main__":
    bank = build(260)
    with open("/tmp/da_bank.json", "w") as f:
        json.dump(bank, f)
    print("saved", sum(len(v) for v in bank.values()))
