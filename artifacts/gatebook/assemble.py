#!/usr/bin/env python3
"""Assemble unique GATE DA banks into public/book.json."""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from helpers import uniq, stem_key, thin_families  # noqa: E402

UNITS = [
    ("ps", "1", "Probability and Statistics", "P&S", "bank_ps"),
    ("la", "2", "Linear Algebra", "LA", "bank_la"),
    ("calc", "3", "Calculus and Optimization", "Calculus", "bank_calc"),
    ("dsa", "4", "Programming, Data Structures and Algorithms", "DSA", "bank_dsa"),
    ("db", "5", "Database Management and Warehousing", "DBMS", "bank_db"),
    ("ml", "6", "Machine Learning", "ML", "bank_ml"),
    ("ai", "7", "Artificial Intelligence", "AI", "bank_ai"),
    ("ga", "8", "General Aptitude", "GA", "bank_ga"),
]

_OFFSYL = re.compile(r"kronecker|stiefel|grassmann|if this feels off-syllabus", re.I)


def interleave(items):
    buckets: dict[str, list] = defaultdict(list)
    for it in items:
        buckets[str(it.get("topic") or "X")].append(it)
    out = []
    while any(buckets.values()):
        for k in list(buckets):
            if buckets[k]:
                out.append(buckets[k].pop(0))
    return out


def normalize_item(it: dict, unit_id: str, n: int) -> dict:
    opts = it.get("options")
    if opts is not None:
        opts = [str(x) for x in opts]
    return {
        "id": f"{unit_id}-{n:03d}",
        "unitId": unit_id,
        "topic": str(it.get("topic") or ""),
        "qtype": str(it.get("qtype") or "MCQ"),
        "marks": int(it.get("marks") or 1),
        "stem": str(it["stem"]).strip(),
        "options": opts,
        "answer": str(it.get("answer") or "").strip(),
        "sol": str(it.get("sol") or "").strip(),
        "diff": str(it.get("diff") or "M"),
        "section": str(it.get("section") or ""),
    }


def quality_report(items, label):
    stems = [i["stem"] for i in items]
    sk = [stem_key(s) for s in stems]
    types: dict[str, int] = {}
    for i in items:
        types[i["qtype"]] = types.get(i["qtype"], 0) + 1
    print(
        f"  {label:8s} n={len(items):4d}  stem_dups={len(stems)-len(set(stems))}  "
        f"skeleton_dups={len(sk)-len(set(sk))}  {types}"
    )


def assemble():
    units = []
    for uid, code, title, short, modname in UNITS:
        try:
            mod = __import__(modname)
            raw = uniq(mod.items())
            raw = [it for it in raw if not _OFFSYL.search(it.get("stem") or "")]
            raw, dropped = thin_families(raw, cap=2)
            if dropped:
                print(f"  {short}: dropped {dropped} template-family clones")
            raw = interleave(raw)
        except Exception as e:
            print(f"FAIL {modname}: {e}", file=sys.stderr)
            raw = []
        qs = [normalize_item(it, uid, i + 1) for i, it in enumerate(raw)]
        quality_report(qs, short)
        units.append({"id": uid, "code": code, "title": title, "short": short, "questions": qs})

    mocks = []
    try:
        import bank_mocks

        papers = bank_mocks.papers()
        for i, p in enumerate(papers):
            code = str(p.get("code") or chr(65 + i))
            qs = []
            for j, it in enumerate(p.get("questions") or []):
                q = normalize_item(it, f"mock-{code}", j + 1)
                q["id"] = f"mock-{code}-{j+1:02d}"
                qs.append(q)
            mocks.append(
                {
                    "code": code,
                    "title": p.get("title") or f"Mock Paper {i+1:02d}",
                    "questions": qs,
                }
            )
            quality_report(qs, f"Mock {code}")
    except Exception as e:
        print(f"mocks: {e}", file=sys.stderr)

    total = sum(len(u["questions"]) for u in units)
    book = {
        "meta": {
            "title": "GATE DA 2027 Practice Book",
            "edition": "2027",
            "totalQuestions": total,
            "unitCount": len(units),
            "mockCount": len(mocks),
            "note": (
                "Unofficial practice book. Layout follows standard GATE / Made Easy unit-then-solutions books. "
                "Stems follow official DA 2024-2026 habits with new numbers and wording. "
                "Official PYQs are not copied. Mocks use the latest confirmed paper: 65 Q, 100 marks, 3 hours."
            ),
        },
        "units": units,
        "mocks": mocks,
    }
    print("TOTAL UNIT Q", total, "MOCK PAPERS", len(mocks))
    return book


def main():
    book = assemble()
    text = json.dumps(book, ensure_ascii=True)
    Path("/workspace/public/book.json").write_text(text)
    Path("/workspace/artifacts/book.json").write_text(text)
    print("wrote book.json bytes", Path("/workspace/public/book.json").stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
