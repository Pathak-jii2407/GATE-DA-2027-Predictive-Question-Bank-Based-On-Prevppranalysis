"""Shared emit helpers for GATE bank generators."""
from __future__ import annotations

import math
import re
from pathlib import Path

HYPHEN = "-"  # ASCII hyphen-minus only


def clean(s: str) -> str:
    if s is None:
        return s
    s = (
        s.replace("\u2212", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u00d7", "x")
        .replace("\u03bb", "lambda")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u00a0", " ")
    )
    return s


def fmt_num(x, nd=8):
    if isinstance(x, bool):
        return str(x)
    if isinstance(x, int) or (isinstance(x, float) and x == int(x) and abs(x) < 1e12):
        return str(int(x))
    if isinstance(x, float):
        # compact GATE-like
        r2 = round(x, 2)
        if abs(r2 - x) < 1e-9:
            return f"{r2:.2f}".rstrip("0").rstrip(".") if False else (f"{r2:.2f}")
        r4 = round(x, 4)
        if abs(r4 - x) < 1e-9:
            s = f"{r4:.4f}".rstrip("0").rstrip(".")
            return s
        return f"{x:.10g}"
    return str(x)


def nice(x, tol=1e-9):
    """Return int if almost integer else rounded 4dp float."""
    if abs(x - round(x)) < tol:
        return int(round(x))
    for k in (1, 2, 3, 4):
        r = round(x, k)
        if abs(r - x) < 10 ** (-k - 2):
            return r
    return round(x, 4)


class Bank:
    def __init__(self, module_comment: str):
        self.comment = module_comment
        self.rows = []  # list of tuples

    def mcq(self, topic, stem, a, b, c, d, ans, sol, marks=1, diff="M"):
        self.rows.append(
            (
                "mcq",
                clean(topic),
                clean(stem),
                clean(a),
                clean(b),
                clean(c),
                clean(d),
                clean(ans),
                clean(sol),
                marks,
                diff,
            )
        )

    def msq(self, topic, stem, a, b, c, d, ans, sol, marks=2, diff="M"):
        self.rows.append(
            (
                "msq",
                clean(topic),
                clean(stem),
                clean(a),
                clean(b),
                clean(c),
                clean(d),
                clean(ans),
                clean(sol),
                marks,
                diff,
            )
        )

    def nat(self, topic, stem, ans, sol, marks=1, diff="M"):
        self.rows.append(
            (
                "nat",
                clean(topic),
                clean(stem),
                None,
                None,
                None,
                None,
                clean(str(ans) if not isinstance(ans, float) else fmt_num(ans)),
                clean(sol),
                marks,
                diff,
            )
        )

    def write(self, path: str):
        p = Path(path)
        lines = [
            '"""' + self.comment + '"""',
            "from helpers import mcq, msq, nat, uniq",
            "",
            "",
            "def items():",
            "    o = []",
        ]
        for r in self.rows:
            kind = r[0]
            topic, stem = r[1], r[2]
            if kind in ("mcq", "msq"):
                a, b, c, d, ans, sol, marks, diff = r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]
                fn = "mcq" if kind == "mcq" else "msq"
                lines.append(f"    o.append({fn}(")
                lines.append(f"        {topic!r},")
                lines.append(f"        {stem!r},")
                lines.append(f"        {a!r},")
                lines.append(f"        {b!r},")
                lines.append(f"        {c!r},")
                lines.append(f"        {d!r},")
                lines.append(f"        {ans!r},")
                lines.append(f"        {sol!r},")
                lines.append(f"        marks={marks},")
                lines.append(f"        diff={diff!r},")
                lines.append("    ))")
            else:
                ans, sol, marks, diff = r[7], r[8], r[9], r[10]
                lines.append("    o.append(nat(")
                lines.append(f"        {topic!r},")
                lines.append(f"        {stem!r},")
                lines.append(f"        {ans!r},")
                lines.append(f"        {sol!r},")
                lines.append(f"        marks={marks},")
                lines.append(f"        diff={diff!r},")
                lines.append("    ))")
        lines.append("    return uniq(o)")
        lines.append("")
        p.write_text("\n".join(lines), encoding="ascii", errors="replace")
