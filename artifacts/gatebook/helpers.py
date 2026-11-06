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
_camel = re.compile(r"\b[A-Z][a-zA-Z0-9]+(?:[A-Z][a-zA-Z0-9]+)+\b")
_list = re.compile(r"\[[^\[\]]{0,80}\]")


def stem_key(stem: str) -> str:
    s = _num_re.sub("#", stem)
    s = _space_re.sub(" ", s).strip().lower()
    return s


def family_key(stem: str) -> str:
    s = _list.sub("[ ]", stem)
    s = _camel.sub("Name", s)
    s = _num_re.sub("#", s)
    s = _space_re.sub(" ", s).strip().lower()
    if "fit simple ols with intercept" in s and "slope" in s:
        return "slr-slope-template"
    if "ols line fitted" in s and "prediction" in s:
        return "slr-pred-template"
    if "the ols intercept is" in s:
        return "slr-int-template"
    if "ols residual sum of squares" in s:
        return "slr-sse-template"
    if "selection sort (swap the current index" in s:
        return "sel-sort-swaps-template"
    return s


def thin_families(items, cap: int = 2):
    seen, out, dropped = {}, [], 0
    for it in items:
        k = family_key(it["stem"])
        n = seen.get(k, 0)
        if n >= cap:
            dropped += 1
            continue
        seen[k] = n + 1
        out.append(it)
    return out, dropped


def uniq(items):
    seen, out = set(), []
    for it in items:
        k = stem_key(it["stem"])
        if k in seen:
            continue
        seen.add(k)
        out.append(it)
    return out
