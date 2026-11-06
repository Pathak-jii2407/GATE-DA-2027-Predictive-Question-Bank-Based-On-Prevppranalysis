"""Shared constructors for GATE DA item banks."""
import re


def q(topic, qtype, marks, stem, options, answer, sol, diff="M", section=None):
    item = {
        "topic": topic,
        "qtype": qtype,
        "marks": marks,
        "stem": stem,
        "options": options,
        "answer": str(answer),
        "sol": sol,
        "diff": diff,
    }
    if section:
        item["section"] = section
    return item


def mcq(topic, stem, a, b, c, d, ans, sol, marks=1, diff="M", section=None):
    return q(topic, "MCQ", marks, stem, [a, b, c, d], ans, sol, diff, section)


def msq(topic, stem, a, b, c, d, ans, sol, marks=2, diff="M", section=None):
    return q(topic, "MSQ", marks, stem, [a, b, c, d], ans, sol, diff, section)


def nat(topic, stem, ans, sol, marks=1, diff="M", section=None):
    return q(topic, "NAT", marks, stem, None, ans, sol, diff, section)


_num_re = re.compile(r"\d+(?:\.\d+)?")
_space_re = re.compile(r"\s+")


def stem_key(stem: str) -> str:
    s = _num_re.sub("#", stem)
    s = _space_re.sub(" ", s).strip().lower()
    return s


def uniq(items):
    seen, out = set(), []
    for it in items:
        k = stem_key(it["stem"])
        if k in seen:
            continue
        seen.add(k)
        out.append(it)
    return out
