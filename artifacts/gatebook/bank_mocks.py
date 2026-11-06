"""10 full-length GATE DA mocks. 2026 skeleton, PYQ-like mix, disjoint stems."""
from __future__ import annotations

from collections import defaultdict
import random


# Official GATE DA 2026 (IIT Guwahati) skeleton:
# Q.1-5 GA 1m, Q.6-10 GA 2m, Q.11-35 DA 1m, Q.36-65 DA 2m.
# Mix modelled on DA 2024 / 2025 / 2026: MCQ + MSQ + NAT, no negative on MSQ/NAT.

DA_SUBJECTS = ["ps", "la", "calc", "dsa", "db", "ml", "ai"]

# 55 DA questions: typical DA paper weights (2024-2026).
DA_SHARE = {
    "ps": 10,
    "la": 9,
    "calc": 6,
    "dsa": 8,
    "db": 7,
    "ml": 9,
    "ai": 6,
}

TITLES = [
    "Mock Paper 01  ·  Guwahati skeleton (full mix)",
    "Mock Paper 02  ·  Bayes, 2x2 eigs, Python defaults",
    "Mock Paper 03  ·  SQL NULL, PCA axes, A* vs UCS",
    "Mock Paper 04  ·  BCNF, ridge, FOL implication",
    "Mock Paper 05  ·  CLT, SVD, trees / hash",
    "Mock Paper 06  ·  Exponential, B+ fanout, minimax",
    "Mock Paper 07  ·  Joint tables, HAC, d-separation",
    "Mock Paper 08  ·  3VL SQL, LOOCV, variable elimination",
    "Mock Paper 09  ·  Rotation matrices, logistic, sampling",
    "Mock Paper 10  ·  Full syllabus mix",
]


def _by_type(items):
    b = defaultdict(list)
    for it in items:
        b[it.get("qtype") or "MCQ"].append(it)
    return b


def _take_one(bucket, used):
    rest = []
    picked = None
    for it in bucket:
        if picked is None and it["stem"] not in used:
            picked = it
        else:
            rest.append(it)
    return picked, rest


def _fill(need, pools, used, rng):
    """Take `need` items, cycling preferred types then any leftover."""
    out = []
    order = list(pools.keys())
    rng.shuffle(order)
    # First pass: round-robin types so a paper is never all-MCQ.
    while len(out) < need:
        progressed = False
        for t in order:
            if len(out) >= need:
                break
            got, pools[t] = _take_one(pools[t], used)
            if got is None:
                continue
            used.add(got["stem"])
            out.append(got)
            progressed = True
        if not progressed:
            break
    return out


def _split_marks_pools(items):
    """Prefer native 2-mark items for 2-mark slots, else longer stems / MSQ."""
    m1, m2 = [], []
    for it in items:
        it = dict(it)
        if int(it.get("marks") or 1) == 2 or it.get("qtype") == "MSQ" or len(it.get("stem") or "") > 140:
            m2.append(it)
        else:
            m1.append(it)
    return m1, m2


def papers():
    import bank_ga, bank_ps, bank_la, bank_calc, bank_dsa, bank_db, bank_ml, bank_ai
    from helpers import uniq, thin_families

    def _interleave(items):
        buckets = defaultdict(list)
        for it in items:
            buckets[str(it.get("topic") or "X")].append(it)
        out = []
        while any(buckets.values()):
            for k in list(buckets):
                if buckets[k]:
                    out.append(buckets[k].pop(0))
        return out

    mods = {
        "ga": bank_ga,
        "ps": bank_ps,
        "la": bank_la,
        "calc": bank_calc,
        "dsa": bank_dsa,
        "db": bank_db,
        "ml": bank_ml,
        "ai": bank_ai,
    }
    pools = {}
    for name, mod in mods.items():
        raw, _ = thin_families(uniq(mod.items()), cap=2)
        pools[name] = _interleave(raw)

    used: set[str] = set()
    out = []
    for i, title in enumerate(TITLES):
        rng = random.Random(2027 + i * 17)
        # --- GA 5 x 1m, 5 x 2m ---
        ga_items = [it for it in pools["ga"] if it["stem"] not in used]
        ga1_src, ga2_src = _split_marks_pools(ga_items)
        rng.shuffle(ga1_src)
        rng.shuffle(ga2_src)
        g1 = _fill(5, _by_type(ga1_src), used, rng)
        g2 = _fill(5, _by_type(ga2_src + [x for x in ga1_src if x["stem"] not in used]), used, rng)

        # --- DA by subject share, then 25 of 1m and 30 of 2m ---
        da_picked = []
        for subj, share in DA_SHARE.items():
            cand = [it for it in pools[subj] if it["stem"] not in used]
            rng.shuffle(cand)
            take = _fill(share, _by_type(cand), used, rng)
            for it in take:
                it = dict(it)
                it["section"] = subj
                da_picked.append(it)

        # If a subject ran dry, top up from any remaining DA.
        if len(da_picked) < 55:
            leftover = []
            for subj in DA_SUBJECTS:
                leftover.extend(it for it in pools[subj] if it["stem"] not in used)
            rng.shuffle(leftover)
            extra = _fill(55 - len(da_picked), _by_type(leftover), used, rng)
            da_picked.extend(extra)

        rng.shuffle(da_picked)
        d1_src, d2_src = _split_marks_pools(da_picked)
        # Re-bucket; ignore previous used-stems because these are already unique to this paper.
        local = set()
        d1 = _fill(25, _by_type(d1_src), local, rng)
        # remaining go to 2-mark
        remain = [it for it in da_picked if it["stem"] not in {x["stem"] for x in d1}]
        d2 = remain[:30]
        if len(d2) < 30:
            more = [it for it in d1_src if it["stem"] not in {x["stem"] for x in d1 + d2}]
            d2 = d2 + more[: 30 - len(d2)]

        qs = []
        for it in g1[:5]:
            qs.append(dict(it, marks=1, section="GA"))
        for it in g2[:5]:
            qs.append(dict(it, marks=2, section="GA"))
        for it in d1[:25]:
            qs.append(dict(it, marks=1))
        for it in d2[:30]:
            qs.append(dict(it, marks=2))
        qs = qs[:65]
        out.append({"code": chr(65 + i), "title": title, "questions": qs})

        # consume from master pools
        taken = {it["stem"] for it in qs}
        used |= taken
        for name in pools:
            pools[name] = [it for it in pools[name] if it["stem"] not in taken]
    return out
