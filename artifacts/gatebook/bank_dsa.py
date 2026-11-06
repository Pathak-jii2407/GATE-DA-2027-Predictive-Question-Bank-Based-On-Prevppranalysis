"""GATE DA bank: Programming, Data Structures and Algorithms."""
from __future__ import annotations

from collections import defaultdict, deque
from helpers import mcq, msq, nat, uniq
import io
import contextlib
import heapq
import math


def _run(src: str) -> str:
    buf = io.StringIO()
    g: dict = {}
    with contextlib.redirect_stdout(buf):
        exec(src, g)
    return buf.getvalue().rstrip("\n")


def _bfs(edges, start, directed=False, order="alpha"):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    for k in adj:
        adj[k] = sorted(adj[k]) if order == "alpha" else adj[k]
    seen = {start}
    q = deque([start])
    out = []
    while q:
        u = q.popleft()
        out.append(u)
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                q.append(w)
    return out


def _dfs(edges, start, directed=False):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    for k in adj:
        adj[k] = sorted(adj[k])
    seen = set()
    out = []

    def rec(u):
        seen.add(u)
        out.append(u)
        for w in adj[u]:
            if w not in seen:
                rec(w)

    rec(start)
    return out


def _dijkstra(edges, start):
    adj = defaultdict(list)
    nodes = {start}
    for u, v, w in edges:
        adj[u].append((v, w))
        nodes.add(u)
        nodes.add(v)
    dist = {n: math.inf for n in nodes}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def _linprobe(keys, m, h):
    t = [None] * m
    pos = {}
    probes = {}
    for k in keys:
        i = h(k) % m
        p = 1
        while t[i] is not None:
            i = (i + 1) % m
            p += 1
        t[i] = k
        pos[k] = i
        probes[k] = p
    return t, pos, probes


def _quadprobe(keys, m, h):
    t = [None] * m
    pos = {}
    for k in keys:
        i0 = h(k) % m
        j = 0
        while True:
            i = (i0 + j * j) % m
            if t[i] is None:
                t[i] = k
                pos[k] = i
                break
            j += 1
            if j > m:
                raise RuntimeError("full")
    return t, pos


def _bin_comps(arr, y, three_way=True):
    lo, hi = 0, len(arr) - 1
    comps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1
        if arr[mid] == y:
            return comps, True
        if arr[mid] < y:
            lo = mid + 1
        else:
            hi = mid - 1
    return comps, False


def _lomuto_swaps(a):
    a = list(a)
    swaps = [0]

    def part(lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    swaps[0] += 1
                i += 1
        if i != hi:
            a[i], a[hi] = a[hi], a[i]
            swaps[0] += 1
        return i

    def qs(lo, hi):
        if lo < hi:
            p = part(lo, hi)
            qs(lo, p - 1)
            qs(p + 1, hi)

    qs(0, len(a) - 1)
    return swaps[0], a


def _bubble_swaps(a):
    a = list(a)
    n = len(a)
    sw = 0
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                sw += 1
    return sw, a


def _ins_swaps(a):
    a = list(a)
    sw = 0
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            sw += 1
            j -= 1
    return sw, a


def _sel_swaps(a):
    a = list(a)
    sw = 0
    n = len(a)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]
            sw += 1
    return sw, a


def _bubble_after_k(a, k):
    a = list(a)
    n = len(a)
    for i in range(k):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def _sel_after_k(a, k):
    a = list(a)
    n = len(a)
    for i in range(k):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
    return a


def _ins_after_k(a, k):
    a = list(a)
    for i in range(1, min(k + 1, len(a))):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def _merge_count(a):
    a = list(a)
    inv = [0]

    def merge(lo, mid, hi):
        L = a[lo:mid]
        R = a[mid:hi]
        i = j = 0
        k = lo
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
                inv[0] += len(L) - i
            k += 1
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1

    def ms(lo, hi):
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        ms(lo, mid)
        ms(mid, hi)
        merge(lo, mid, hi)

    ms(0, len(a))
    return inv[0], a


def _build_pre_in(pre, ino):
    if not pre:
        return None
    r = pre[0]
    i = ino.index(r)
    return (r, _build_pre_in(pre[1 : 1 + i], ino[:i]), _build_pre_in(pre[1 + i :], ino[i + 1 :]))


def _post(t):
    if t is None:
        return []
    r, L, R = t
    return _post(L) + _post(R) + [r]


def _pre(t):
    if t is None:
        return []
    r, L, R = t
    return [r] + _pre(L) + _pre(R)


def _ino(t):
    if t is None:
        return []
    r, L, R = t
    return _ino(L) + [r] + _ino(R)


def _height(t):
    if t is None:
        return -1
    return 1 + max(_height(t[1]), _height(t[2]))


def _leaves(t):
    if t is None:
        return 0
    if t[1] is None and t[2] is None:
        return 1
    return _leaves(t[1]) + _leaves(t[2])


def _python():
    o = []
    T = "Python"

    src = (
        "def push_tag(tag, bag=[]):\n"
        "    bag.append(tag)\n"
        "    return bag\n"
        "print(push_tag('a'))\n"
        "print(push_tag('b'))\n"
        "print(push_tag('c', []))\n"
    )
    o.append(
        mcq(
            T,
            "Consider the Python program\n" + src + "Which option is the exact printed output?",
            "['a']\\n['b']\\n['c']",
            "['a']\\n['a', 'b']\\n['c']",
            "['a']\\n['a', 'b']\\n['a', 'b', 'c']",
            "['a']\\n['b']\\n['a', 'b', 'c']",
            "B",
            "The default list is created once at def-time, so the first two calls share it. The third call passes a fresh list.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "def tally(k, box=None):\n"
        "    if box is None:\n"
        "        box = []\n"
        "    box.append(k)\n"
        "    return box\n"
        "print(tally(4))\n"
        "print(tally(5))\n"
    )
    o.append(
        mcq(
            T,
            "Consider the Python program\n" + src + "The printed output is",
            "[4]\\n[4, 5]",
            "[4]\\n[5]",
            "[4, 5]\\n[4, 5]",
            "[4]\\n[4]",
            "B",
            "box=None is immutable; a new list is allocated on every call that omits the second argument.",
            marks=1,
            diff="E",
        )
    )

    src = "shelf = [10, 20, 30]\nrack = shelf\nrack.append(40)\nprint(shelf)\n"
    o.append(
        mcq(
            T,
            "After executing\n" + src + "the value printed for shelf is",
            "[10, 20, 30]",
            "[10, 20, 30, 40]",
            "[40]",
            "[10, 20, 40]",
            "B",
            "rack and shelf alias the same list object, so append mutates both names.",
            marks=1,
            diff="E",
        )
    )

    src = "p = [1, 2, 3]\nq = p\np = p + [4]\nprint(p)\nprint(q)\n"
    o.append(
        mcq(
            T,
            "After executing\n" + src + "the pair (p, q) is",
            "([1, 2, 3, 4], [1, 2, 3, 4])",
            "([1, 2, 3, 4], [1, 2, 3])",
            "([1, 2, 3], [1, 2, 3, 4])",
            "([1, 2, 3, 4], [1, 2, 3, 4, 4])",
            "B",
            "p + [4] builds a new list and rebinds p; q still names the original list.",
            marks=1,
            diff="M",
        )
    )

    src = "p = [1, 2, 3]\nq = p\np += [4]\nprint(p is q, p, q)\n"
    o.append(
        mcq(
            T,
            "After executing\n" + src + "the printed line is",
            "False [1, 2, 3, 4] [1, 2, 3]",
            "True [1, 2, 3, 4] [1, 2, 3, 4]",
            "True [1, 2, 3, 4] [1, 2, 3]",
            "False [1, 2, 3, 4] [1, 2, 3, 4]",
            "B",
            "For lists, += is extend in-place, so p and q remain the same object.",
            marks=2,
            diff="M",
        )
    )

    src = "row = [2, 4, 6, 8, 10]\nrow[1:4] = [0]\nprint(row)\n"
    o.append(
        mcq(
            T,
            "The Python fragment\n" + src + "prints",
            "[2, 0, 10]",
            "[2, 0, 8, 10]",
            "[2, 0, 6, 8, 10]",
            "[0, 0, 0, 0, 10]",
            "A",
            "Slice assignment replaces the whole slice [4,6,8] by the single value 0, so the list shrinks.",
            marks=1,
            diff="M",
        )
    )

    src = "buf = [7, 8, 9]\nview = buf[0:2]\nview[0] = 1\nprint(buf)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "buf is",
            "[1, 8, 9]",
            "[7, 8, 9]",
            "[1, 8]",
            "[7, 1, 9]",
            "B",
            "A slice of a list copies; mutating view does not touch buf.",
            marks=1,
            diff="M",
        )
    )

    src = "grid = [[0] * 2] * 3\ngrid[0][0] = 5\nprint(grid)\n"
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "[[5, 0], [0, 0], [0, 0]]",
            "[[5, 0], [5, 0], [5, 0]]",
            "[[5, 5], [5, 5], [5, 5]]",
            "[[5, 0], [0, 0], [5, 0]]",
            "B",
            "[[0]*2]*3 reuses one inner list three times, so writing grid[0][0] is visible in every row.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "try:\n"
        "    s = { (1, 2), (3, 4), [5, 6] }\n"
        "    print('ok', len(s))\n"
        "except TypeError:\n"
        "    print('err')\n"
    )
    o.append(
        mcq(
            T,
            "Executing\n" + src + "prints",
            "ok 3",
            "ok 2",
            "err",
            "ok 1",
            "C",
            "A list is unhashable, so inserting [5,6] into a set raises TypeError.",
            marks=1,
            diff="E",
        )
    )

    src = "s = set()\ns.add((1, (2, 3)))\ns.add((1, (2, 3)))\nprint(len(s))\n"
    o.append(
        nat(
            T,
            "The fragment\n" + src + "prints which integer?",
            1,
            "Nested tuples of immutables are hashable; the second add is a duplicate.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def fib(n, c):\n"
        "    c[0] += 1\n"
        "    if n < 2:\n"
        "        return n\n"
        "    return fib(n-1, c) + fib(n-2, c)\n"
        "c = [0]\n"
        "fib(5, c)\n"
        "print(c[0])\n"
    )
    o.append(
        nat(
            T,
            "In the Python function\n" + src + "the printed call count (including the initial call) is",
            15,
            "The recursion tree of fib(5) has 15 nodes: T(n)=T(n-1)+T(n-2)+1 with T(0)=T(1)=1 gives 15.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "def count(n):\n"
        "    c = [0]\n"
        "    def b(n):\n"
        "        c[0] += 1\n"
        "        if n == 0:\n"
        "            return 1\n"
        "        return b(n-1) + b(n-1)\n"
        "    b(n)\n"
        "    return c[0]\n"
        "print(count(4))\n"
    )
    o.append(
        nat(
            T,
            "Let boom(n) return boom(n-1)+boom(n-1) with boom(0)=1. Including the first call, how many calls occur while evaluating boom(4)? Equivalent program:\n"
            + src,
            31,
            "A perfect binary recursion of depth 4 makes 2^{5}-1 = 31 activations.",
            marks=2,
            diff="H",
        )
    )

    src = "x = [1, 2, 3]\ny = x[:]\ny.append(4)\nprint(len(x), len(y), x is y)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed triple is",
            "3 4 False",
            "4 4 True",
            "3 4 True",
            "4 4 False",
            "A",
            "x[:] shallow-copies the top-level list, so append on y does not change x.",
            marks=1,
            diff="E",
        )
    )

    src = "a = [[1], [2]]\nb = a[:]\nb[0].append(9)\nprint(a)\n"
    o.append(
        mcq(
            T,
            "After the shallow copy\n" + src + "the value of a is",
            "[[1], [2]]",
            "[[1, 9], [2]]",
            "[[1, 9], [2, 9]]",
            "[[9], [2]]",
            "B",
            "The outer list is copied but inner lists are shared, so b[0].append mutates a[0].",
            marks=2,
            diff="M",
        )
    )

    src = "vals = [3, 1, 2]\nprint(sorted(vals), vals)\n"
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "[1, 2, 3] [1, 2, 3]",
            "[1, 2, 3] [3, 1, 2]",
            "[3, 1, 2] [1, 2, 3]",
            "[3, 1, 2] [3, 1, 2]",
            "B",
            "sorted returns a new list and leaves vals unchanged.",
            marks=1,
            diff="E",
        )
    )

    src = "vals = [3, 1, 2]\nr = vals.sort()\nprint(r, vals)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed pair is",
            "[1, 2, 3] [1, 2, 3]",
            "None [1, 2, 3]",
            "None [3, 1, 2]",
            "[3, 1, 2] [1, 2, 3]",
            "B",
            "list.sort sorts in place and returns None.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def wrap(xs=[]):\n"
        "    xs.append(len(xs))\n"
        "    return xs\n"
        "wrap()\n"
        "wrap()\n"
        "print(wrap())\n"
    )
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[0]",
            "[0, 1, 2]",
            "[2]",
            "[0, 1]",
            "B",
            "Three calls share one default list: append 0, then 1, then 2.",
            marks=2,
            diff="M",
        )
    )

    src = "t = (1, 2, [3])\nt[2].append(4)\nprint(t)\n"
    o.append(
        mcq(
            T,
            "Executing\n" + src + "prints",
            "(1, 2, [3])",
            "(1, 2, [3, 4])",
            "TypeError",
            "(1, 2, 3, 4)",
            "B",
            "The tuple is immutable but its third component is a mutable list, which can be mutated in place.",
            marks=1,
            diff="M",
        )
    )

    src = (
        "k = 0\n"
        "def inc(n):\n"
        "    global k\n"
        "    k += n\n"
        "    return k\n"
        "print(inc(2), inc(3), k)\n"
    )
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "2 5 5",
            "2 3 5",
            "2 5 0",
            "0 0 5",
            "A",
            "global k is updated by both calls: 0+2=2 then 2+3=5.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n):\n"
        "    if n <= 1:\n"
        "        return n\n"
        "    return f(n-1) + 2*f(n-2)\n"
        "print(f(4))\n"
    )
    o.append(
        nat(
            T,
            "For the Python function\n" + src + "the printed value is",
            5,
            "f(0)=0, f(1)=1, f(2)=1, f(3)=3, f(4)=3+2*1=5.",
            marks=1,
            diff="M",
        )
    )

    src = "a = [1, 2, 3, 4]\na[::-1] = a\nprint(a)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the list a is",
            "[4, 3, 2, 1]",
            "[1, 2, 3, 4]",
            "[1, 4, 3, 2]",
            "an error is raised",
            "B",
            "The RHS is evaluated first (the original list), then written into the reversed slice, restoring [1,2,3,4].",
            marks=2,
            diff="H",
        )
    )

    src = "a = [1, 2, 3, 4]\na[::-1] = [10, 20, 30, 40]\nprint(a)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "a equals",
            "[10, 20, 30, 40]",
            "[40, 30, 20, 10]",
            "[1, 2, 3, 4]",
            "[40, 20, 30, 10]",
            "B",
            "Assigning to the reversed slice writes 10 into a[3], 20 into a[2], 30 into a[1], 40 into a[0].",
            marks=2,
            diff="H",
        )
    )

    src = "s = 'gate'\nt = s\ns += 'da'\nprint(s, t, s is t)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed line is",
            "gateda gateda True",
            "gateda gate False",
            "gate gate True",
            "gateda gateda False",
            "B",
            "Strings are immutable; += rebinds s to a new object while t still names 'gate'.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def g(x, y=[]):\n"
        "    y.append(x)\n"
        "    return id(y)\n"
        "u = g(1)\n"
        "v = g(2)\n"
        "w = g(3, [])\n"
        "print(u == v, v == w)\n"
    )
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "True False",
            "False False",
            "True True",
            "False True",
            "A",
            "The first two calls share the default list (same id); the third uses a freshly passed list.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "xs = [1, 2, 3]\n"
        "def add(n, acc=xs):\n"
        "    acc.append(n)\n"
        "    return acc\n"
        "xs = []\n"
        "print(add(4))\n"
    )
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed list is",
            "[4]",
            "[1, 2, 3, 4]",
            "[]",
            "[1, 2, 3]",
            "B",
            "Default acc is bound to the original list object at def-time; later rebinding of the name xs is irrelevant.",
            marks=2,
            diff="H",
        )
    )

    src = (
        "d = { (1, 2): 'ok' }\n"
        "try:\n"
        "    d[[1, 2]] = 'no'\n"
        "    print('assigned')\n"
        "except TypeError:\n"
        "    print(list(d.values())[0])\n"
    )
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "assigned",
            "ok",
            "no",
            "nothing (crash without except)",
            "B",
            "A list cannot be a dict key; the except path prints the existing value 'ok'.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n, m):\n"
        "    if n == 0:\n"
        "        return m\n"
        "    return f(n-1, m+n)\n"
        "print(f(4, 0))\n"
    )
    o.append(
        nat(
            T,
            "The Python function\n" + src + "prints",
            10,
            "It accumulates 4+3+2+1 = 10.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def calls(n):\n"
        "    c = [0]\n"
        "    def g(n):\n"
        "        c[0] += 1\n"
        "        return n if n <= 1 else g(n-1) + g(n-2)\n"
        "    g(n)\n"
        "    return c[0]\n"
        "print(calls(6))\n"
    )
    o.append(
        nat(
            T,
            "How many calls (including the first) does a naive Fibonacci implementation make on input 6? Equivalent code:\n"
            + src,
            25,
            "Let C(n)=C(n-1)+C(n-2)+1, C(0)=C(1)=1. Then C(6)=25.",
            marks=2,
            diff="M",
        )
    )

    src = "a, *b, c = [9, 8, 7, 6, 5]\nprint(a, b, c)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed line is",
            "9 [8, 7, 6] 5",
            "9 8 [7, 6, 5]",
            "[9, 8, 7, 6] 5 None",
            "9 [8, 7, 6, 5] error",
            "A",
            "Starred assignment captures the middle remainder as a list.",
            marks=1,
            diff="E",
        )
    )

    src = "print(bool([]), bool([0]), bool(''), bool('0'))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "False False False True",
            "False True False True",
            "False True True True",
            "True True False True",
            "B",
            "Empty list and empty string are falsey; a non-empty list (even [0]) and '0' are truthy.",
            marks=1,
            diff="E",
        )
    )

    src = "def f(x):\n    return x or 7\nprint(f(0), f(2), f([]), f([0]))\n"
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "7 2 7 [0]",
            "0 2 [] [0]",
            "7 2 [] [0]",
            "7 2 7 7",
            "A",
            "or returns the first truthy operand, else the last: 0 and [] are falsey so 7 is returned.",
            marks=1,
            diff="M",
        )
    )

    src = (
        "n = 0\n"
        "def side():\n"
        "    global n\n"
        "    n += 1\n"
        "    return n\n"
        "print(side() and side() and side())\n"
        "print(n)\n"
    )
    o.append(
        mcq(
            T,
            "After\n" + src + "the two printed lines are",
            "1 then 1",
            "3 then 3",
            "1 then 3",
            "True then 3",
            "B",
            "Each side() returns a positive int (truthy), so all three calls run; and yields the last value 3.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "n = 0\n"
        "def side():\n"
        "    global n\n"
        "    n += 1\n"
        "    return n\n"
        "print(0 and side())\n"
        "print(n)\n"
    )
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed pair is",
            "0 then 0",
            "0 then 1",
            "1 then 1",
            "False then 0",
            "A",
            "0 is falsey so and short-circuits and side() is never called.",
            marks=1,
            diff="M",
        )
    )

    src = "print(5 / 2, 5 // 2, -5 // 2)\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "2.5 2 -2",
            "2.5 2 -3",
            "2 2 -2",
            "2.5 2.0 -2.0",
            "B",
            "True division gives 2.5; floor division rounds toward -inf, so -5//2 = -3.",
            marks=1,
            diff="M",
        )
    )

    src = "print(2 ** 3 ** 2, (2 ** 3) ** 2)\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "64 64",
            "512 64",
            "64 512",
            "256 64",
            "B",
            "** is right-associative: 2**(3**2)=2**9=512, while (2**3)**2=64.",
            marks=1,
            diff="M",
        )
    )

    src = (
        "fns = []\n"
        "for i in range(3):\n"
        "    fns.append(lambda: i)\n"
        "print([f() for f in fns])\n"
    )
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[0, 1, 2]",
            "[2, 2, 2]",
            "[3, 3, 3]",
            "[0, 0, 0]",
            "B",
            "Late binding: each lambda reads the same loop variable i, which is 2 after the loop.",
            marks=2,
            diff="H",
        )
    )

    src = (
        "fns = []\n"
        "for i in range(3):\n"
        "    fns.append(lambda i=i: i)\n"
        "print([f() for f in fns])\n"
    )
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[0, 1, 2]",
            "[2, 2, 2]",
            "[0, 0, 0]",
            "[1, 1, 1]",
            "A",
            "Default i=i captures the current integer at each iteration, so the lambdas close over 0,1,2.",
            marks=2,
            diff="H",
        )
    )

    src = "d = dict.fromkeys(['a', 'b'], [])\nd['a'].append(1)\nprint(d)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "d is",
            "{'a': [1], 'b': []}",
            "{'a': [1], 'b': [1]}",
            "{'a': [1], 'b': None}",
            "{'a': 1, 'b': []}",
            "B",
            "fromkeys reuses the same list object as the default value for every key.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "def f():\n"
        "    try:\n"
        "        return 1\n"
        "    finally:\n"
        "        return 2\n"
        "print(f())\n"
    )
    o.append(
        mcq(
            T,
            "The function\n" + src + "prints",
            "1",
            "2",
            "None",
            "an error is raised",
            "B",
            "A return in finally overrides the return in try.",
            marks=1,
            diff="M",
        )
    )

    src = (
        "def f():\n"
        "    try:\n"
        "        return 1\n"
        "    except:\n"
        "        return 3\n"
        "    else:\n"
        "        return 4\n"
        "print(f())\n"
    )
    o.append(
        mcq(
            T,
            "The function\n" + src + "prints",
            "1",
            "4",
            "3",
            "None",
            "A",
            "else runs only if try did not return/raise; here try already returned 1.",
            marks=1,
            diff="M",
        )
    )

    src = "xs = [1, 2, 3]\nys = xs\nxs[0:3] = [9, 9, 9]\nprint(ys)\n"
    o.append(
        mcq(
            T,
            "After slice assignment\n" + src + "ys is",
            "[1, 2, 3]",
            "[9, 9, 9]",
            "[9, 2, 3]",
            "[1, 2, 3, 9, 9, 9]",
            "B",
            "Slice assignment mutates the list object in place; ys aliases xs.",
            marks=1,
            diff="M",
        )
    )

    src = "print([i for i in range(5) if i % 2 == 0])\n"
    o.append(
        mcq(
            T,
            "The list comprehension\n" + src + "evaluates to",
            "[0, 2, 4]",
            "[1, 3]",
            "[0, 1, 2, 3, 4]",
            "[2, 4]",
            "A",
            "Even i in 0..4 are 0,2,4.",
            marks=1,
            diff="E",
        )
    )

    src = "acc = []\nprint([acc.append(i) or i for i in range(3)])\nprint(acc)\n"
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[0, 1, 2] then [0, 1, 2]",
            "[None, None, None] then [0, 1, 2]",
            "[0, 1, 2] then []",
            "[None, None, None] then []",
            "A",
            "append returns None (falsey) so 'or i' yields i; the side-effect fills acc.",
            marks=2,
            diff="H",
        )
    )

    src = "z = zip([1, 2, 3], [10, 20])\nprint(list(z), list(z))\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed pair is",
            "[(1, 10), (2, 20), (3, None)] []",
            "[(1, 10), (2, 20)] [(1, 10), (2, 20)]",
            "[(1, 10), (2, 20)] []",
            "[(1, 10), (2, 20), (3, 0)] []",
            "C",
            "zip stops at the shorter iterable and the iterator is exhausted after the first list().",
            marks=1,
            diff="M",
        )
    )

    src = "print((lambda x: x*x)(4))\n"
    o.append(
        nat(
            T,
            "The expression\n" + src + "prints",
            16,
            "The lambda computes 4*4.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def deco(f):\n"
        "    def g(x):\n"
        "        return f(x) + 1\n"
        "    return g\n"
        "@deco\n"
        "def h(x):\n"
        "    return x * 2\n"
        "print(h(3))\n"
    )
    o.append(
        nat(
            T,
            "The decorated function\n" + src + "prints",
            7,
            "h(3) computes 3*2 then the wrapper adds 1, giving 7.",
            marks=1,
            diff="M",
        )
    )

    src = (
        "class C:\n"
        "    n = 0\n"
        "    def __init__(self):\n"
        "        C.n += 1\n"
        "C(); C(); print(C.n)\n"
    )
    o.append(
        nat(
            T,
            "The program\n" + src + "prints",
            2,
            "Each constructor increments the class variable n.",
            marks=1,
            diff="E",
        )
    )

    src = "print(list(map(lambda p: p[0]+p[1], zip([1,2,3],[4,5,6]))))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "evaluates to",
            "[5, 7, 9]",
            "[1, 2, 3, 4, 5, 6]",
            "[(1, 4), (2, 5), (3, 6)]",
            "[14]",
            "A",
            "Pairwise sums 1+4, 2+5, 3+6.",
            marks=1,
            diff="E",
        )
    )

    src = "s = {1, 2, 3}\nt = {3, 4}\nprint(sorted(s & t), sorted(s | t), sorted(s - t))\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed line is",
            "[3] [1, 2, 3, 4] [1, 2]",
            "[3] [1, 2, 3, 4] [4]",
            "[1, 2] [1, 2, 3, 4] [3]",
            "[] [1, 2, 3, 4] [1, 2, 3]",
            "A",
            "Intersection {3}, union {1,2,3,4}, difference {1,2}.",
            marks=1,
            diff="E",
        )
    )

    src = "a = [1, 2, 3]\nb = a\na = [0]\nprint(b)\n"
    o.append(
        mcq(
            T,
            "After rebinding\n" + src + "b is",
            "[0]",
            "[1, 2, 3]",
            "[1, 2, 3, 0]",
            "None",
            "B",
            "Rebinding the name a does not mutate the list still named by b.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n):\n"
        "    if n <= 0:\n"
        "        return 0\n"
        "    return 1 + f(n-2)\n"
        "print(f(7))\n"
    )
    o.append(
        nat(
            T,
            "The function\n" + src + "prints",
            4,
            "It counts how many times 2 can be subtracted from 7 until <=0, i.e. 4.",
            marks=1,
            diff="E",
        )
    )

    src = "x = [1, 2, 3, 4, 5]\nprint(x[-1], x[-3:], x[:-2])\n"
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "5 [3, 4, 5] [1, 2, 3]",
            "5 [4, 5] [1, 2, 3]",
            "1 [1, 2, 3] [4, 5]",
            "5 [3, 4, 5] [1, 2]",
            "A",
            "x[-1] is last; x[-3:] is the last three; x[:-2] drops the last two.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def mut(t):\n"
        "    t[0].append('x')\n"
        "    t = t + ([9],)\n"
        "    return t\n"
        "u = ([1], [2])\n"
        "v = mut(u)\n"
        "print(u, v)\n"
    )
    o.append(
        mcq(
            T,
            "After\n" + src + "the pair (u, v) is",
            "(([1, 'x'], [2]), ([1, 'x'], [2], [9]))",
            "(([1], [2]), ([1, 'x'], [2], [9]))",
            "(([1, 'x'], [2], [9]), ([1, 'x'], [2], [9]))",
            "(([1], [2]), ([1], [2], [9]))",
            "A",
            "t[0].append mutates the shared inner list of u; t = t+... rebinds only the local name.",
            marks=2,
            diff="H",
        )
    )

    src = (
        "def f(a, b, c=1, *rest, d=2, **kw):\n"
        "    return (a, b, c, rest, d, kw)\n"
        "print(f(9, 8, 7, 6, d=5, z=4))\n"
    )
    o.append(
        mcq(
            T,
            "The call in\n" + src + "returns",
            "(9, 8, 7, (6,), 5, {'z': 4})",
            "(9, 8, 1, (7, 6), 5, {'z': 4})",
            "(9, 8, 7, (6,), 2, {'d': 5, 'z': 4})",
            "(9, 8, 7, (6, 5), 2, {'z': 4})",
            "A",
            "c takes 7, 6 goes to *rest, keyword d=5, leftover z in **kw.",
            marks=2,
            diff="H",
        )
    )

    src = "print(sum(i*i for i in range(1, 5) if i % 2 == 1))\n"
    o.append(
        nat(
            T,
            "The generator expression\n" + src + "prints",
            10,
            "Odd i in 1..4 are 1 and 3; 1+9=10.",
            marks=1,
            diff="E",
        )
    )

    src = "A = [1, 2, 3]\nB = [4, 5, 6]\nA.extend(B)\nprint(A)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "A is",
            "[1, 2, 3, [4, 5, 6]]",
            "[1, 2, 3, 4, 5, 6]",
            "[1, 2, 3]",
            "[4, 5, 6]",
            "B",
            "extend concatenates elements of B into A in place.",
            marks=1,
            diff="E",
        )
    )

    src = "A = [1, 2, 3]\nB = [4, 5, 6]\nA.append(B)\nprint(len(A), A[-1])\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed pair is",
            "6 [4, 5, 6]",
            "4 [4, 5, 6]",
            "4 6",
            "6 6",
            "B",
            "append adds B as a single nested element, so A has length 4.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def rec(n, acc):\n"
        "    acc.append(n)\n"
        "    if n == 0:\n"
        "        return acc\n"
        "    return rec(n-1, acc)\n"
        "print(rec(3, []))\n"
    )
    o.append(
        mcq(
            T,
            "The call in\n" + src + "prints",
            "[3, 2, 1, 0]",
            "[0, 1, 2, 3]",
            "[3]",
            "[0]",
            "A",
            "n is appended before the recursive call, so the list is 3,2,1,0.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def rec(n):\n"
        "    if n == 0:\n"
        "        return [0]\n"
        "    return rec(n-1) + [n]\n"
        "print(rec(3))\n"
    )
    o.append(
        mcq(
            T,
            "The call in\n" + src + "prints",
            "[3, 2, 1, 0]",
            "[0, 1, 2, 3]",
            "[3]",
            "[0, 3]",
            "B",
            "The recursive result is prepended: [0]+[1]+[2]+[3].",
            marks=1,
            diff="E",
        )
    )

    src = "i = 1\nwhile i < 10:\n    i *= 2\nprint(i)\n"
    o.append(
        nat(
            T,
            "The loop\n" + src + "prints",
            16,
            "i takes 1,2,4,8 then 16 which exits the while i<10 test.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "cnt = 0\n"
        "for i in range(1, 5):\n"
        "    for j in range(i):\n"
        "        cnt += 1\n"
        "print(cnt)\n"
    )
    o.append(
        nat(
            T,
            "The nested loops\n" + src + "print",
            10,
            "Inner iterations: 1+2+3+4=10.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n):\n"
        "    r = 0\n"
        "    while n:\n"
        "        r += n & 1\n"
        "        n >>= 1\n"
        "    return r\n"
        "print(f(13))\n"
    )
    o.append(
        nat(
            T,
            "The function\n" + src + "prints",
            3,
            "13 is 1101b, which has three 1-bits.",
            marks=1,
            diff="M",
        )
    )

    src = "print(int('1011', 2) + int('12', 8))\n"
    o.append(
        nat(
            T,
            "The expression\n" + src + "prints",
            21,
            "0b1011=11 and 0o12=10; sum 21.",
            marks=1,
            diff="E",
        )
    )

    src = "s = 'abca'\nprint(s.find('a'), s.rfind('a'), s.find('z'))\n"
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "0 3 -1",
            "0 0 -1",
            "1 4 0",
            "0 3 4",
            "A",
            "find leftmost index 0, rfind rightmost 3, missing char yields -1.",
            marks=1,
            diff="E",
        )
    )

    src = "print(''.join(reversed('gate')))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "etag",
            "gate",
            "e t a g",
            "['e','t','a','g']",
            "A",
            "reversed on a string yields characters in reverse, joined with empty separator.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(x, y):\n"
        "    x.append(y)\n"
        "    y = y + 1\n"
        "a = [1]\n"
        "b = 2\n"
        "f(a, b)\n"
        "print(a, b)\n"
    )
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed pair is",
            "[1, 2] 2",
            "[1, 2] 3",
            "[1] 2",
            "[1] 3",
            "A",
            "The list is mutated via the shared object; rebinding local y does not change b.",
            marks=1,
            diff="M",
        )
    )

    src = "print([n for n in range(8) if n % 3][::2])\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "evaluates to",
            "[1, 4, 7]",
            "[1, 2, 4, 5, 7]",
            "[1, 5]",
            "[0, 3, 6]",
            "A",
            "n%3 truthy keeps 1,2,4,5,7; then [::2] takes 1,4,7.",
            marks=2,
            diff="M",
        )
    )

    src = (
        "def memo_fib(n, m={}):\n"
        "    if n < 2:\n"
        "        return n\n"
        "    if n not in m:\n"
        "        m[n] = memo_fib(n-1) + memo_fib(n-2)\n"
        "    return m[n]\n"
        "memo_fib(6)\n"
        "print(sorted(memo_fib.__defaults__[0].keys()))\n"
    )
    o.append(
        mcq(
            T,
            "After calling memo_fib(6) in\n" + src + "the printed key list is",
            "[2, 3, 4, 5, 6]",
            "[0, 1, 2, 3, 4, 5, 6]",
            "[6]",
            "[]",
            "A",
            "Bases n<2 return without writing the cache; keys 2..6 are stored in the default dict.",
            marks=2,
            diff="H",
        )
    )

    src = (
        "def f(n):\n"
        "    yield n\n"
        "    yield from f(n-1) if n else ()\n"
        "print(list(f(3)))\n"
    )
    o.append(
        mcq(
            T,
            "The generator\n" + src + "yields the list",
            "[3, 2, 1, 0]",
            "[0, 1, 2, 3]",
            "[3]",
            "[3, 2, 1]",
            "A",
            "It yields n then recurses until n=0, which still yields 0 then stops.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        msq(
            T,
            "Which of the following Python objects are hashable and may be placed in a set?",
            "(1, [2])",
            "(1, (2, 3))",
            "frozenset({1, 2})",
            "{1: 2}",
            "B;C",
            "A tuple is hashable only if all components are. frozenset is hashable; list and dict are not.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        msq(
            T,
            "Let L be a list and T a tuple of the same elements. Which statements are always true in Python 3?",
            "L.append(0) mutates L in place",
            "T.append(0) mutates T in place",
            "L += [0] reuses the same list object",
            "T += (0,) reuses the same tuple object",
            "A;C",
            "Tuples have no append; T += (0,) rebinds T to a new tuple because tuples are immutable.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        msq(
            T,
            "Regarding default arguments in a Python def statement, which claims hold?",
            "A default list object is evaluated once, at function definition time",
            "A default list object is evaluated fresh on every call that omits the argument",
            "Using None as a sentinel and allocating a list inside the body avoids cross-call sharing",
            "Integer defaults such as n=0 share mutations across calls the same way lists do",
            "A;C",
            "Mutable defaults are classic sharing bugs. Integers are immutable so mutation across calls does not apply.",
            marks=2,
            diff="M",
        )
    )

    src = "def f(x):\n    x = x + [1]\n    return x\na = [0]\nprint(f(a), a)\n"
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[0, 1] [0, 1]",
            "[0, 1] [0]",
            "[0] [0]",
            "[1] [0]",
            "B",
            "x = x+[1] builds a new list; a is unchanged.",
            marks=1,
            diff="M",
        )
    )

    src = "def f(x):\n    x += [1]\n    return x\na = [0]\nprint(f(a), a)\n"
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[0, 1] [0]",
            "[0, 1] [0, 1]",
            "[0] [0]",
            "[1] [1]",
            "B",
            "For lists x += [1] is in-place extend, so a is mutated.",
            marks=1,
            diff="M",
        )
    )

    src = "print(all([]), any([]), all([1, 0]), any([0, 0, 2]))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "True False False True",
            "False False False True",
            "True True True True",
            "True False True True",
            "A",
            "all on empty is True (vacuous); any on empty is False.",
            marks=1,
            diff="M",
        )
    )

    src = "print(sorted('cba'), list('cba'))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "['a', 'b', 'c'] ['c', 'b', 'a']",
            "abc ['c', 'b', 'a']",
            "['c', 'b', 'a'] ['c', 'b', 'a']",
            "['a', 'b', 'c'] cba",
            "A",
            "sorted always returns a list of characters; list() preserves original order.",
            marks=1,
            diff="E",
        )
    )

    src = "m = {'x': 1, 'y': 2}\nprint(list(m.keys())[0], m.get('z', 9))\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "a possible printed line (insertion order is preserved) is",
            "x 9",
            "z 9",
            "x None",
            "y None",
            "A",
            "Insertion order puts 'x' first; get with default 9 is used for missing 'z'.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n):\n"
        "    if n <= 1:\n"
        "        return 1\n"
        "    return n * f(n-1)\n"
        "print(f(5))\n"
    )
    o.append(
        nat(
            T,
            "The factorial function\n" + src + "prints",
            120,
            "5!=120.",
            marks=1,
            diff="E",
        )
    )

    src = "def depth(n):\n    return 1 if n == 0 else 1 + depth(n-1)\nprint(depth(6))\n"
    o.append(
        nat(
            T,
            "The function\n" + src + "prints the number of stack frames created by the chain (including the first). The printed value is",
            7,
            "A linear chain of 6 recursive steps plus the base call is 7 activations.",
            marks=1,
            diff="E",
        )
    )

    src = "xs = [0, 1, 2, 3, 4, 5]\ndel xs[1:4]\nprint(xs)\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "xs is",
            "[0, 4, 5]",
            "[0, 1, 5]",
            "[4, 5]",
            "[0, 1, 2, 3]",
            "A",
            "del xs[1:4] removes indices 1,2,3 i.e. values 1,2,3.",
            marks=1,
            diff="E",
        )
    )

    src = "xs = [0, 1, 2, 3]\nxs[1:1] = [8, 9]\nprint(xs)\n"
    o.append(
        mcq(
            T,
            "After inserting into an empty slice\n" + src + "xs is",
            "[0, 8, 9, 1, 2, 3]",
            "[8, 9, 0, 1, 2, 3]",
            "[0, 1, 8, 9, 2, 3]",
            "[0, 8, 9, 2, 3]",
            "A",
            "xs[1:1] is the empty slice at index 1, so 8,9 are inserted there.",
            marks=1,
            diff="M",
        )
    )

    src = "print(2 < 3 < 2, 2 < 3 and 3 < 2)\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "True False",
            "False False",
            "False True",
            "True True",
            "B",
            "Chained 2<3<2 is (2<3) and (3<2), both False overall.",
            marks=1,
            diff="M",
        )
    )

    src = "a = [1, 2, 3]\nprint(a * 2, [a] * 2)\n"
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "[1, 2, 3, 1, 2, 3] [[1, 2, 3], [1, 2, 3]]",
            "[2, 4, 6] [[1, 2, 3], [1, 2, 3]]",
            "[1, 2, 3, 1, 2, 3] [1, 2, 3, 1, 2, 3]",
            "[1, 2, 3, 2] [[1, 2, 3], [1, 2, 3]]",
            "A",
            "List * k repeats elements; [a]*2 is a list of two aliases of a.",
            marks=1,
            diff="E",
        )
    )

    src = "print({1, 2, 3} == {3, 2, 1}, [1, 2, 3] == [3, 2, 1])\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "True False",
            "True True",
            "False False",
            "False True",
            "A",
            "Sets are unordered; lists compare order-sensitively.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n, s=[]):\n"
        "    s.append(n)\n"
        "    if n == 0:\n"
        "        return list(s)\n"
        "    return f(n-1)\n"
        "print(f(2))\n"
        "print(f(1))\n"
    )
    o.append(
        mcq(
            T,
            "The program\n" + src + "prints",
            "[2, 1, 0] then [1, 0]",
            "[2, 1, 0] then [2, 1, 0, 1, 0]",
            "[0] then [0]",
            "[2, 1, 0] then [2, 1, 0]",
            "B",
            "The default list survives between top-level calls, so the second call appends onto [2,1,0].",
            marks=2,
            diff="H",
        )
    )

    src = "print([i // 2 for i in range(-3, 3)])\n"
    o.append(
        mcq(
            T,
            "The comprehension\n" + src + "evaluates to",
            "[-2, -1, -1, 0, 0, 1]",
            "[-1, -1, 0, 0, 1, 1]",
            "[-2, -2, -1, -1, 0, 1]",
            "[-1, -1, -1, 0, 0, 1]",
            "A",
            "range(-3,3) is -3,-2,-1,0,1,2; floor-div by 2 gives -2,-1,-1,0,0,1.",
            marks=1,
            diff="H",
        )
    )

    src = "print(list(enumerate(['p', 'q'], start=2)))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "evaluates to",
            "[(2, 'p'), (3, 'q')]",
            "[(0, 'p'), (1, 'q')]",
            "[(1, 'p'), (2, 'q')]",
            "[(2, 'p'), (2, 'q')]",
            "A",
            "enumerate with start=2 numbers from 2.",
            marks=1,
            diff="E",
        )
    )

    src = "print(round(2.5), round(3.5), round(2.51))\n"
    o.append(
        mcq(
            T,
            "In Python 3, bankers rounding is used. The expression\n" + src + "prints",
            "2 4 3",
            "3 4 3",
            "2 3 3",
            "3 3 3",
            "A",
            "round ties-to-even: 2.5->2, 3.5->4; 2.51 is nearer 3.",
            marks=1,
            diff="M",
        )
    )

    src = "def f(n):\n    return [n] + f(n-1) if n else []\nprint(f(3))\n"
    o.append(
        mcq(
            T,
            "The function\n" + src + "prints",
            "[3, 2, 1]",
            "[1, 2, 3]",
            "[3, 2, 1, 0]",
            "[]",
            "A",
            "Prepend n until n is 0, which contributes [].",
            marks=1,
            diff="E",
        )
    )

    src = "a = {1, 2, 3}\nb = a\na |= {4}\nprint(sorted(b))\n"
    o.append(
        mcq(
            T,
            "After in-place set union\n" + src + "sorted(b) is",
            "[1, 2, 3]",
            "[1, 2, 3, 4]",
            "[4]",
            "[1, 2, 3, 4, 4]",
            "B",
            "|= mutates the set object aliased by a and b.",
            marks=1,
            diff="M",
        )
    )

    src = "a = {1, 2, 3}\nb = a\na = a | {4}\nprint(sorted(b), sorted(a))\n"
    o.append(
        mcq(
            T,
            "After\n" + src + "the printed pair is",
            "[1, 2, 3] [1, 2, 3, 4]",
            "[1, 2, 3, 4] [1, 2, 3, 4]",
            "[1, 2, 3] [4]",
            "[1, 2, 3, 4] [1, 2, 3]",
            "A",
            "a | {4} builds a new set and rebinds a; b still names {1,2,3}.",
            marks=1,
            diff="M",
        )
    )

    src = "print(min(['10','2','3'], key=int), min(['10','2','3']))\n"
    o.append(
        mcq(
            T,
            "The expression\n" + src + "prints",
            "2 10",
            "10 10",
            "2 2",
            "10 2",
            "A",
            "key=int compares numeric values so min is '2'; lexicographic min of those strings is '10'.",
            marks=1,
            diff="M",
        )
    )

    src = "xs = [1, 2, 3, 2, 1]\nprint(xs.index(2), xs.count(1))\n"
    o.append(
        mcq(
            T,
            "The fragment\n" + src + "prints",
            "1 2",
            "2 2",
            "1 1",
            "3 2",
            "A",
            "index returns the first occurrence (position 1); 1 appears twice.",
            marks=1,
            diff="E",
        )
    )

    src = (
        "def f(n):\n"
        "    k = 0\n"
        "    def g():\n"
        "        nonlocal k\n"
        "        k += 1\n"
        "        return k\n"
        "    return [g() for _ in range(n)]\n"
        "print(f(3))\n"
    )
    o.append(
        mcq(
            T,
            "The nested function\n" + src + "prints",
            "[1, 2, 3]",
            "[0, 0, 0]",
            "[1, 1, 1]",
            "[3, 3, 3]",
            "A",
            "nonlocal k is incremented on each g() call.",
            marks=1,
            diff="M",
        )
    )

    src = "print([x*y for x in range(3) for y in range(3) if x <= y])\n"
    o.append(
        mcq(
            T,
            "The double comprehension\n" + src + "evaluates to",
            "[0, 0, 0, 1, 2, 4]",
            "[0, 0, 0, 1, 2, 2, 4]",
            "[0, 1, 2, 0, 2, 4]",
            "[0, 1, 4]",
            "A",
            "Pairs (x,y) with x<=y: (0,0),(0,1),(0,2),(1,1),(1,2),(2,2) products 0,0,0,1,2,4.",
            marks=2,
            diff="M",
        )
    )

    return o


def _sim_stack(ops):
    st = []
    last = None
    for op in ops:
        if op[0] == "push":
            st.append(op[1])
        elif op[0] == "pop":
            last = st.pop() if st else None
    return st, last


def _sim_queue(ops):
    q = deque()
    last = None
    for op in ops:
        if op[0] == "enq":
            q.append(op[1])
        elif op[0] == "deq":
            last = q.popleft() if q else None
    return list(q), last


def _sim_deque(ops):
    d = deque()
    last = None
    for op in ops:
        k = op[0]
        if k == "pushl":
            d.appendleft(op[1])
        elif k == "pushr":
            d.append(op[1])
        elif k == "popl":
            last = d.popleft() if d else None
        elif k == "popr":
            last = d.pop() if d else None
    return list(d), last


def _linear_ds():
    o = []
    T = "Stacks and queues"

    ops = [("push", 3), ("push", 7), ("push", 1), ("pop",), ("push", 5), ("pop",), ("pop",)]
    st, last = _sim_stack(ops)
    o.append(
        nat(
            T,
            "An empty stack S is processed by: push 3, push 7, push 1, pop, push 5, pop, pop. The integer that remains in S is",
            st[0],
            "After the sequence the stack holds only 3.",
            marks=1,
            diff="E",
        )
    )

    ops = [("enq", 4), ("enq", 9), ("enq", 2), ("deq",), ("enq", 6), ("deq",)]
    q, last = _sim_queue(ops)
    o.append(
        mcq(
            T,
            "An empty queue (FIFO) is processed by: enqueue 4, enqueue 9, enqueue 2, dequeue, enqueue 6, dequeue. The front-to-rear contents are",
            "2, 6",
            "4, 9",
            "6, 2",
            "9, 2, 6",
            "A",
            "Dequeue removes 4 then 9, leaving 2 then 6.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "A double-ended queue D is empty. Operations: insertRear(1), insertFront(2), insertRear(3), deleteFront, insertFront(4), deleteRear. Front-to-rear contents of D are",
            "4, 1",
            "1, 3",
            "4, 1, 3",
            "2, 1",
            "A",
            "After insertRear 1: [1]; insertFront 2: [2,1]; insertRear 3: [2,1,3]; deleteFront removes 2: [1,3]; insertFront 4: [4,1,3]; deleteRear removes 3: [4,1].",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Characters of GATE are pushed on an empty stack in left-to-right order, then all are popped. If A=1, G=2, T=3, E=4, the first popped value (the code of that character) is",
            4,
            "E is pushed last and popped first; its code is 4.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "A sequence of stack operations on empty S: push(a), push(b), pop, push(c), pop, pop. The sequence of popped values is",
            "b, c, a",
            "a, b, c",
            "b, a, c",
            "c, b, a",
            "A",
            "Stack is a, then a b; pop b; push c; pop c; pop a.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            T,
            "Which data structures can implement a FIFO queue with amortized O(1) enqueue and dequeue?",
            "A singly linked list with both head and tail pointers",
            "A singly linked list with only a head pointer (insert/delete at head)",
            "Two stacks (input stack and output stack)",
            "A singly linked list with only a tail pointer (insert at tail)",
            "A;C",
            "Head+tail list gives O(1) both ends. Two stacks give amortized O(1). Head-only list makes the rear expensive; tail-only cannot delete the head in O(1).",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            T,
            "To evaluate the postfix expression 5 1 2 + 4 * + 3 - with a stack, the value remaining on the stack at the end is",
            "14",
            "10",
            "9",
            "18",
            "A",
            "5, then 1 2 + -> 3, 3 4 * -> 12, 5+12=17, 17-3=14.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "The postfix 3 4 + 2 * 7 / is evaluated with integer floor division on a stack. The final integer is",
            2,
            "(3+4)*2 = 14, then 14/7 = 2.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Which of the following sequences of push(1), push(2), push(3) and three pops cannot occur as the output of a stack (output is the pop sequence)?",
            "1 2 3",
            "3 2 1",
            "2 3 1",
            "3 1 2",
            "D",
            "3 1 2 would require 1 to be popped before 2 while 3 is already gone, which violates stack discipline: after popping 3 the top is 2, so 1 cannot come next.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "A circular queue is implemented in an array of size 6 (indices 0..5) with front=2 and rear=5, holding 3 elements in the usual convention that the rear index is the last occupied slot. Using count = (rear - front + N) mod N with front pointing at the first occupied slot, the number of stored elements is",
            3,
            "(5-2+6) mod 6 = 3.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "A queue is implemented using two stacks In and Out. Enqueue always pushes onto In. Dequeue pops from Out, but if Out is empty it first pops every element of In onto Out. Starting empty, perform: enq 1, enq 2, deq, enq 3, deq, deq. The last dequeued value is",
            "1",
            "2",
            "3",
            "the queue is empty too early",
            "C",
            "First deq yields 1 after transferring 2,1 onto Out (pop order 1 then 2). Then enq 3 onto In. Next deq pops remaining Out which is 2. Last deq transfers 3 and yields 3.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        nat(
            T,
            "Minimum number of stacks needed to implement a queue (with the two-stack method) is",
            2,
            "The standard simulation uses an input stack and an output stack.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "While converting the infix (A+B)*C - D/E to postfix with an operator stack (precedence * / over + -, left-associative, parentheses), the postfix is",
            "AB+C*DE/-",
            "AB+C*D-E/",
            "ABC*+DE/-",
            "AB+CD-E/*",
            "A",
            "(A+B)*C becomes AB+C*, then D/E becomes DE/, subtraction last: AB+C*DE/-.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Using an operator stack to convert A*(B+C) to postfix, the number of times an operator (* or +) is popped onto the output is",
            2,
            "On seeing ')' we pop '+'; at the end we pop '*'. Parentheses themselves are not output.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "A linked list holds 8 -> 3 -> 5 -> 1 (head 8). The following pointer surgery is done, where p points at the node 8 and q at the node 3: p.next = q.next; q.next = p. The sequence of keys from the new head q is",
            "3 -> 8 -> 5 -> 1",
            "8 -> 5 -> 1",
            "3 -> 5 -> 1",
            "3 -> 8 -> 3 -> ... (cycle)",
            "A",
            "p.next skips 3 and points at 5; q.next points at 8. From q: 3,8,5,1.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "A singly linked list of 9 nodes is traversed by two pointers starting at the head: slow moves one node per step, fast moves two. When fast first reaches the last node, slow is at node number (1-indexed from the head)",
            5,
            "After 4 fast steps fast is at node 9; slow moved 4 steps to node 5 (the middle).",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "To reverse a singly linked list in one pass with three pointers prev, cur, nxt, the number of next-pointer assignments per node (the rotation nxt=cur.next; cur.next=prev; prev=cur; cur=nxt) that write into a node's next field is",
            "1",
            "2",
            "3",
            "0",
            "A",
            "Only cur.next = prev writes a next field; the others only move local pointers.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "A circular singly linked list has 10 nodes. Starting at the head, the minimum number of next-pointer follows needed to return to the head is",
            10,
            "Ten steps around the cycle.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "A dummy-head singly linked list is used to delete the first key equal to 7 in 7 -> 2 -> 7. After a correct dummy-head deletion of the first 7, the list of real keys is",
            "2 -> 7",
            "7 -> 2",
            "2",
            "7 -> 2 -> 7",
            "A",
            "Dummy lets us unlink the first node without a special case; the later 7 remains.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Two sorted lists 1->4->7 and 2->3->8 are merged by the standard two-pointer merge (stable: take from the first list on ties). The number of next-pointer comparisons of keys until one list is exhausted is",
            5,
            "Compare (1,2),(4,2),(4,3),(4,8),(7,8) - five key comparisons; then the rest is appended.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            T,
            "Floyd's tortoise and hare start together at the head of 1->2->3->4->2 (the next of 4 is 2). They move (slow +1, fast +2) until they meet. The key at the meeting node is",
            "2",
            "3",
            "4",
            "1",
            "C",
            "Positions after moves: (2,3), (3,2), (4,4). They meet at 4.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        msq(
            T,
            "A dequeue (double-ended queue) supports insert/delete at both ends in O(1). Which statements are correct?",
            "A deque can simulate a stack using only one end",
            "A deque can simulate a FIFO queue using opposite ends",
            "A singly linked list with only a head pointer is already a deque",
            "BFS of a graph is naturally implemented with a deque used as a FIFO queue",
            "A;B;D",
            "A head-only singly linked list cannot delete at the tail in O(1), so it is not a deque.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "An empty stack of integers processes: push 10, push 20, pop, push 30, push 40, pop, pop. The sum of the remaining elements is",
            10,
            "Pops remove 20, then 40, then 30; 10 remains.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "An empty FIFO queue processes: enq 5, enq 8, enq 6, deq, enq 9, deq, deq. The remaining front element is",
            9,
            "Dequeues remove 5,8,6 leaving 9.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Next-greater-element to the right is computed with a stack for the array [2, 1, 4, 3]. The next-greater list (use -1 if none) is",
            "4, 4, -1, -1",
            "4, 4, 3, -1",
            "1, 4, 3, -1",
            "4, 4, -1, 4",
            "A",
            "2 and 1 both see 4; 4 and 3 have nothing larger on their right.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Using a stack to check parentheses on (()())(()), scan the given 11-character string. The maximum number of '(' sitting on the stack at any moment is",
            3,
            "Trace depths: 1,2,1,2,1,0,1,2,3,2,1. Peak is 3.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "A priority queue (min-heap) is built on keys 7, 2, 9, 4, 5 by successive insertions into an initially empty binary heap (array layout, swim on insert). The root key after all insertions is",
            "2",
            "7",
            "4",
            "9",
            "A",
            "A min-heap always stores the minimum at the root.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "Insert 7,2,9,4,5 into an empty binary min-heap (1-indexed array, swim). After all inserts, the key at index 2 (left child of the root) is",
            4,
            "Simulate: [7]; 2 swims -> [2,7]; 9 -> [2,7,9]; 4 swims with 7 -> [2,4,9,7]; 5 -> [2,4,9,7,5]. Index 2 is 4.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "A queue of size 3 (capacity 3) is used as a sliding window. Stream 4,1,7,2 is enqueued, and a dequeue happens whenever the queue is full before an enqueue. After processing the whole stream this way, the queue contents front-to-rear are",
            "1, 7, 2",
            "4, 1, 7",
            "7, 2",
            "4, 1, 7, 2",
            "A",
            "Enq 4,1,7 (full). Next 2: deq 4 then enq 2 -> 1,7,2.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        msq(
            T,
            "Which of the following problems are naturally solved with a stack?",
            "Matching HTML tags / parentheses",
            "BFS layer-order traversal of a tree",
            "Evaluating postfix arithmetic",
            "Implementing recursive DFS with an explicit data structure",
            "A;C;D",
            "BFS needs a queue. Parentheses, postfix and DFS are stack-shaped.",
            marks=2,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "A singly linked list has nodes A,B,C,D in that order. Pointer p points to A. The assignments p = p.next; p = p.next; q = p; p = p.next are executed. Node q now holds letter (A=1,B=2,C=3,D=4)",
            3,
            "Two nexts from A land on C; q aliases C.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Deleting the successor of node p in a singly linked list (p is not the tail) is done by p.next = p.next.next. If the list is 6->8->1->4 and p points at 8, the resulting sequence is",
            "6 -> 8 -> 4",
            "6 -> 1 -> 4",
            "6 -> 8 -> 1",
            "8 -> 1 -> 4",
            "A",
            "The node 1 is unlinked; 8 now points at 4.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "A doubly linked list of 5 nodes is reversed by swapping prev/next at every node and moving the head. The number of nodes whose both pointer fields are rewritten is",
            5,
            "Every node swaps its two pointers.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "An output-restricted deque allows deletions only at the front, but insertions at both ends. Which ADT can it still implement in O(1) per operation?",
            "a stack, by inserting and deleting at the front",
            "a stack, only if we insert at the rear",
            "a FIFO queue is impossible",
            "neither stack nor queue",
            "A",
            "Front insert + front delete is a stack. Front-delete plus rear-insert is also a queue, so C is false.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        nat(
            T,
            "Push the integers 1,2,3,4,5 in that order onto a stack. You may pop at any time. One possible output sequence is 2,3,1,5,4. How many pop operations occur in total to produce that full output?",
            5,
            "Every pushed item is popped once; there are 5 pops.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Which input sequence of {push, pop} on an initially empty stack leaves the stack empty and never pops an empty stack? Here + means push one new item, - means pop.",
            "+ - + - + + - -",
            "+ + - - - + + -",
            "+ - - + + - + -",
            "- + + - + - + -",
            "A",
            "The running height must stay non-negative and end at 0. A is 1,0,1,0,1,2,1,0. B goes negative. C goes negative. D starts with a pop.",
            marks=2,
            diff="M",
        )
    )

    return o


def _trees_hash():
    o = []
    T = "Trees"

    pre, ino = ["R", "A", "C", "D", "B", "E"], ["C", "A", "D", "R", "E", "B"]
    t = _build_pre_in(pre, ino)
    post = _post(t)
    o.append(
        mcq(
            T,
            "A binary tree T has preorder R A C D B E and inorder C A D R E B. The postorder of T is",
            "C D A E B R",
            "C D A R E B",
            "A C D B E R",
            "C A D E B R",
            "A",
            "R is root; left subtree inorder CAD / pre ACD so A with left C right D; right subtree inorder EB / pre BE so B with left E. Postorder C D A E B R.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        nat(
            T,
            "For the same tree with preorder R A C D B E and inorder C A D R E B, the height of T (root height 0) is",
            _height(t),
            "Longest root-to-leaf path has length 2 (R-A-C or R-A-D or R-B-E).",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "For the binary tree with preorder R A C D B E and inorder C A D R E B, the number of leaf nodes is",
            _leaves(t),
            "Leaves are C, D and E.",
            marks=1,
            diff="M",
        )
    )

    pre2, ino2 = ["P", "Q", "S", "T", "R"], ["S", "Q", "T", "P", "R"]
    t2 = _build_pre_in(pre2, ino2)
    o.append(
        mcq(
            T,
            "Binary tree U has preorder P Q S T R and inorder S Q T P R. Which statement is true?",
            "R is the right child of P and has no children",
            "R is the left child of P",
            "S is the right child of Q",
            "The postorder is S T Q R P",
            "A",
            "P is root; right inorder is just R, so R is a leaf right child. Left is Q with children S (left) and T (right). Postorder is S T Q R P, wait that's option D also true! Postorder: S,T,Q,R,P. Both A and D true - this should be MSQ or pick one. Check D: _post = "
            + " ".join(_post(t2))
            + ". Yes S T Q R P. Change to MSQ.",
            marks=2,
            diff="H",
        )
    )
    o[-1] = msq(
        T,
        "Binary tree U has preorder P Q S T R and inorder S Q T P R. Which statements are true?",
        "R is the right child of P and is a leaf",
        "Q is the left child of P",
        "S is the right child of Q",
        "The postorder is S T Q R P",
        "A;B;D",
        "Left subtree of P is Q with left S and right T; right child of P is leaf R. Postorder S T Q R P.",
        marks=2,
        diff="H",
    )

    o.append(
        nat(
            T,
            "Keys 8, 3, 10, 1, 6, 14, 4 are inserted in that order into an empty BST. The key in the left child of 6 is",
            4,
            "6 is the right child of 3; 4 is between 3 and 6 so it becomes 6's left child.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "Keys 8, 3, 10, 1, 6, 14, 4 are inserted in that order into an empty BST. The inorder traversal is",
            "1, 3, 4, 6, 8, 10, 14",
            "8, 3, 1, 6, 4, 10, 14",
            "1, 4, 6, 3, 14, 10, 8",
            "1, 3, 6, 4, 8, 10, 14",
            "A",
            "BST inorder is sorted order of the keys.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "Keys 50, 30, 70, 20, 40, 60, 80 are inserted into an empty BST. The height of the tree (root height 0) is",
            2,
            "This is a perfectly balanced tree of height 2.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "A full binary tree has 9 internal nodes (every node has 0 or 2 children). The number of leaves is",
            "10",
            "9",
            "8",
            "18",
            "A",
            "In a full binary tree L = I + 1, so 10 leaves.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "A complete binary tree with 12 nodes is stored in a 1-indexed array. The parent of the node at index 12 is at index",
            6,
            "Parent of i is floor(i/2)=6.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "A complete binary tree with 12 nodes (1-indexed heap layout) has how many leaves?",
            6,
            "Leaves start after the last internal node floor(12/2)=6, so indices 7..12: six leaves.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "Which pair of traversals uniquely determines a binary tree (no duplicate keys)?",
            "inorder and preorder",
            "preorder and postorder",
            "preorder and level-order",
            "postorder and level-order",
            "A",
            "Inorder plus one of preorder/postorder/level-order determines the tree. Preorder+postorder does not, in general.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        msq(
            T,
            "Let T be a nonempty binary tree. Which statements are always true?",
            "The inorder of a BST is a sorted sequence of its keys",
            "The preorder of a BST is always sorted",
            "A heap-ordered complete tree is always a BST",
            "The height of a complete binary tree on n nodes is floor(log2 n)",
            "A;D",
            "BST inorder is sorted; preorder is not. Heaps are not BSTs. Complete-tree height is floor(log2 n) with root height 0.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Number of distinct BSTs that can be formed with keys {W, X, Y} (three distinct keys) is",
            5,
            "The 3rd Catalan number C3=5.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "A max-heap is stored as the array [90, 40, 70, 20, 30, 10, 50]. After one extract-max (standard sink), the new root is",
            "70",
            "40",
            "50",
            "90",
            "A",
            "90 is removed, last key 50 is placed at root and sinks: 50 vs max(40,70) swaps with 70. Root becomes 70.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "In a min-heap array [2, 4, 3, 9, 7, 8], the number of heap-order violations is",
            0,
            "Every parent is <= its children.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Array [2, 8, 3, 9, 7, 4] is claimed to be a min-heap. The number of parent-child pairs that violate min-heap order is",
            "2",
            "1",
            "0",
            "3",
            "A",
            "Index pairs (1-based): 2 vs 8,9 ok; 8 vs 9,7 ok; 3 vs 4 ok. Wait 1-based [2,8,3,9,7,4]: parent 2 (idx2=8) children 9 and 7 ok; parent 3 (idx3=3) child 4 ok. 0 violations? 8>7 is ok for min-heap? min-heap requires parent <= child; 8<=7 is FALSE. Violation (8,7). And 8<=9 ok, 2<=8, 2<=3, 3<=4. Only 1 violation. Answer B.",
            marks=1,
            diff="M",
        )
    )
    o[-1] = mcq(
        T,
        "The array [2, 8, 3, 9, 7, 4] (1-indexed heap layout) is tested as a min-heap. How many parent-child pairs violate the min-heap property?",
        "0",
        "1",
        "2",
        "3",
        "B",
        "The only violation is parent 8 (index 2) versus child 7 (index 5).",
        marks=1,
        diff="M",
    )

    o.append(
        nat(
            T,
            "A binary tree has preorder F B A D C E G I H and inorder A B C D E F G H I. How many nodes are in the left subtree of F?",
            5,
            "Inorder left of F is A B C D E, five nodes.",
            marks=1,
            diff="M",
        )
    )

    t3 = _build_pre_in(list("FBADCEGIH"), list("ABCDEGFHI"))
    o.append(
        mcq(
            T,
            "Tree with preorder F B A D C E G I H and inorder A B C D E F G H I. The right child of G is",
            "I",
            "H",
            "E",
            "none (G is a leaf)",
            "A",
            "Right of F is G I H with inorder G H I, so G has right subtree H I with pre I H, hence I with left H. Right child of G is I.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        nat(
            T,
            "In a rooted binary tree every node has 0 or 2 children (full). If there are 17 leaves, the number of nodes with two children is",
            16,
            "I = L - 1 = 16.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Level-order of a binary tree is 10, 6, 15, 4, 8, 12, 20 and inorder is 4, 6, 8, 10, 12, 15, 20. This tree is",
            "a BST that is also a complete binary tree",
            "a BST that is not complete",
            "complete but not a BST",
            "neither a BST nor complete",
            "A",
            "Inorder is sorted so it is a BST; level-order fills levels left-to-right with 7 nodes, so it is complete (even perfect).",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "A perfect binary tree of height 3 (root height 0) has how many nodes?",
            15,
            "2^{4}-1 = 15.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Inserting 25 into the BST whose inorder is 10,20,30,40 and whose root is 20 (20 has right child 30, 30 has right 40, 20 has left 10) places 25 as",
            "the left child of 30",
            "the right child of 20",
            "the left child of 40",
            "the right child of 10",
            "A",
            "25 goes right of 20 then left of 30.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "The minimum possible height (root height 0) of a binary tree with 100 nodes is",
            6,
            "A complete tree has height floor(log2 100)=6.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "The maximum possible height (root height 0) of a binary tree with 100 nodes is",
            99,
            "A skew chain of 100 nodes has height 99.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            T,
            "Which of the following sequences can be the preorder of some BST on keys {1,2,3,4,5}?",
            "1, 2, 3, 4, 5",
            "5, 4, 3, 2, 1",
            "3, 1, 2, 5, 4",
            "3, 5, 1, 2, 4",
            "A;B;C",
            "A preorder of a BST cannot present a key outside the current subtree window. 3,5,1 is invalid because after going right from 3 to 5, 1 cannot appear.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            T,
            "A threaded binary tree (inorder threads) of n nodes stores two extra bits per node. Compared with a recursive inorder walk, an inorder walk on the threaded tree uses",
            "O(1) auxiliary stack space",
            "O(n) auxiliary stack space",
            "O(log n) auxiliary stack space always",
            "O(n^2) time",
            "A",
            "Threads replace the recursion/stack; time remains O(n).",
            marks=1,
            diff="M",
        )
    )

    # Hash tables
    H = "Hash tables"

    keys = [1, 4, 5, 6, 14, 15]
    t, pos, probes = _linprobe(keys, 10, lambda x: 3 * x)
    o.append(
        mcq(
            H,
            "A hash table of size 10 (indices 0..9) uses h(x)=3x mod 10 and linear probing. Keys 1,4,5,6,14,15 are inserted into an empty table. The indices of 14 and 15 are, respectively (this is a NEW table and NEW hash; do not reuse an official paper)",
            str(pos[14]) + " and " + str(pos[15]),
            str((pos[14] + 1) % 10) + " and " + str(pos[15]),
            str(pos[14]) + " and " + str((pos[15] + 1) % 10),
            str((pos[14] + 2) % 10) + " and " + str(pos[15]),
            "A",
            "h(1)=3, h(4)=2, h(5)=5, h(6)=8, h(14)=2 (collision with 4, probe 3 occupied by 1, then 4), h(15)=5 (collision, probe 6). Simulate carefully in sol: compute positions "
            + str(pos)
            + ".",
            marks=2,
            diff="H",
        )
    )

    keys2 = [12, 22, 32, 42]
    t2, pos2, pr2 = _linprobe(keys2, 11, lambda x: x)
    o.append(
        nat(
            H,
            "Hash table size 11, h(x)=x mod 11, linear probing. Insert 12,22,32,42 into an empty table. The index where 42 is stored is",
            pos2[42],
            "h=1,0,10,9? 12 mod 11=1, 22 mod 11=0, 32 mod 11=10, 42 mod 11=9. No collisions actually if those slots empty. 1,0,10,9 are distinct so 42 at 9. "
            + str(pos2),
            marks=1,
            diff="M",
        )
    )

    keys3 = [10, 22, 31, 4, 15, 28, 17]
    t3, pos3, pr3 = _linprobe(keys3, 11, lambda x: x)
    o.append(
        nat(
            H,
            "Table size 11, h(x)=x mod 11, linear probing. Insert 10,22,31,4,15,28,17. Number of probes used to insert 17 (counting the successful slot) is",
            pr3[17],
            "Positions "
            + str(pos3)
            + " and probes "
            + str(pr3)
            + ". 17 mod 11=6; collisions force extra probes.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            H,
            "Table size 7, h(x)=x mod 7, linear probing. Insert 50, 15, 36, 8 into an empty table. The slot of 8 is",
            str(_linprobe([50, 15, 36, 8], 7, lambda x: x)[1][8]),
            "0",
            "6",
            "4",
            "A",
            "50%7=1, 15%7=1 -> 2, 36%7=1 -> 3, 8%7=1 -> 4. Slot of 8 is 4. Options may duplicate A. Fix options.",
            marks=2,
            diff="M",
        )
    )
    slot8 = _linprobe([50, 15, 36, 8], 7, lambda x: x)[1][8]
    o[-1] = mcq(
        H,
        "Open-address table of size 7 with h(x)=x mod 7 and linear probing. Keys 50, 15, 36, 8 are inserted (empty start). Key 8 occupies index",
        "1",
        "2",
        "3",
        "4",
        "D" if slot8 == 4 else "A" if slot8 == 1 else "B" if slot8 == 2 else "C",
        "50 goes to 1; 15 collides and takes 2; 36 takes 3; 8 takes 4.",
        marks=2,
        diff="M",
    )

    tq, pq = _quadprobe([10, 22, 31, 4, 15], 11, lambda x: x)
    o.append(
        nat(
            H,
            "Table size 11, h(x)=x mod 11, quadratic probing i-th probe (h(x)+i^2) mod 11, i=0,1,2,... Insert 10,22,31,4,15. Index of 15 is",
            pq[15],
            "Positions " + str(pq) + ".",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            H,
            "Chaining is used in a table of size 5 with h(x)=x mod 5. Keys 12, 22, 7, 17, 27 are inserted (each chain is a list, new key at the head). The chain at index 2, from head to tail, is",
            "27 -> 17 -> 12",
            "12 -> 17 -> 27",
            "22 -> 7",
            "27 -> 22 -> 7",
            "A",
            "12,17,27 all hash to 2; inserting at head reverses insertion order: 27,17,12.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            H,
            "A hash table of 13 slots uses chaining. 10 distinct keys are stored. The minimum possible length of the longest chain is",
            1,
            "10 < 13 so the keys can occupy 10 distinct slots; longest chain can be 1.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            H,
            "A hash table of 13 slots uses chaining. 10 distinct keys are stored. The maximum possible length of the longest chain is",
            10,
            "All keys may collide in one slot.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            H,
            "Load factor alpha of an open-address table of size m holding n keys is n/m. For uniform probing, the expected probes in an unsuccessful search is about 1/(1-alpha). If m=1000 and n=800, this estimate is",
            "5",
            "1.25",
            "0.8",
            "4",
            "A",
            "1/(1-0.8)=5.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        msq(
            H,
            "Which statements about hashing are correct?",
            "Linear probing suffers from primary clustering",
            "Quadratic probing eliminates secondary clustering completely",
            "Double hashing uses a second hash to choose the step",
            "Chaining remains correct even when n exceeds m",
            "A;C;D",
            "Quadratic probing still has some clustering; it does not fully remove secondary clustering. Double hashing and chaining claims are standard.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        mcq(
            H,
            "Double hashing: h1(k)=k mod 11, h2(k)=1+(k mod 10), table size 11. Probe sequence is (h1 + i*h2) mod 11. The first three probes for k=14 are",
            "3, 8, 2",
            "3, 4, 5",
            "3, 7, 0",
            "14, 15, 16",
            "A",
            "h1=3, h2=1+4=5. Probes 3, 8, 13 mod 11=2.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        nat(
            H,
            "In a table of size 8 with h(x)=x mod 8 and linear probing, insert 16, 24, 32. The index of 32 is",
            _linprobe([16, 24, 32], 8, lambda x: x)[1][32],
            "All hash to 0; they occupy 0,1,2 so 32 is at 2.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            H,
            "Deleting a key from a linear-probing table without a tombstone can break later searches. After inserting 5, 12 into size-7 table h(x)=x mod 7 (both hash to 5: 5 at 5, 12 at 6) and physically emptying slot 5, a search for 12",
            "may stop at the empty slot 5 and miss 12",
            "always finds 12 at slot 6",
            "rehashes 12 to a new slot",
            "is guaranteed to scan the whole table",
            "A",
            "Search follows probes until an empty slot; a hole at the home address hides later clustered keys. Tombstones are required.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            H,
            "A chain-hash table of size 4 stores keys 1,5,9,13,17 (all hash to 1). The number of key comparisons to search for 17 if each chain is a list from head=most-recently-inserted is",
            1,
            "Head is 17, so the successful search compares once.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            H,
            "Same chain as above (head 17 -> 13 -> 9 -> 5 -> 1). Unsuccessful search for 3, which hashes to 1, performs how many key comparisons?",
            5,
            "The whole chain of 5 keys is scanned.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            H,
            "Universal hashing is used so that for any two distinct keys the collision probability under a random hash from the family is",
            "at most 1/m for table size m",
            "exactly 1/2",
            "0",
            "n/m",
            "A",
            "That is the definition of a universal family.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            H,
            "Simple uniform hashing, chaining, n=2m keys in m slots. Expected chain length (load factor) is",
            2,
            "alpha = n/m = 2.",
            marks=1,
            diff="E",
        )
    )

    return o


def _search_sort():
    o = []
    S = "Searching"

    arrs = [
        ("HostelWaitlist", [2, 5, 8, 11, 14, 17, 20, 23, 26, 29], 17),
        ("RollSheet", [101, 205, 308, 412, 519, 623, 730], 412),
        ("LabTimes", [9, 11, 14, 18, 22, 27, 31, 36, 40], 10),
        ("GateScores", [12, 24, 36, 48, 60, 72, 84, 96], 96),
        ("PacketIds", [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33], 21),
        ("ShelfCodes", [4, 8, 15, 16, 23, 42, 108], 42),
        ("FlightRows", [1, 2, 4, 8, 16, 32, 64, 128], 64),
        ("PrimeList", [2, 3, 5, 7, 11, 13, 17, 19, 23], 1),
        ("EvenKeys", [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 8),
        ("OddKeys", [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 21),
    ]
    for name, arr, y in arrs:
        c, found = _bin_comps(arr, y)
        o.append(
            nat(
                S,
                "Sorted array "
                + name
                + " = "
                + str(arr)
                + ". Recursive/iterative binary search uses a three-way comparison at mid = floor((lo+hi)/2) and continues while lo<=hi. Number of mid-key comparisons until the search for "
                + str(y)
                + " terminates is",
                c,
                "Standard binary search on this concrete array performs "
                + str(c)
                + " comparisons; found="
                + str(found)
                + ".",
                marks=2,
                diff="M",
            )
        )

    o.append(
        nat(
            S,
            "Let A be a sorted array of 1000 distinct integers. Recursive binary search for a missing key y uses a three-way comparison at mid and loops while lo<=hi. An upper bound on the number of comparisons is the number of times n=1000 can be halved, about ceil(log2(1001)). The exact worst-case comparison count of this implementation (floor mid, lo=mid+1 or hi=mid-1) on n=1000 is",
            _bin_comps(list(range(1000)), -1)[0],
            "Simulate unsuccessful search on 0..999 for -1 (always go left) or a value larger than all. Count="
            + str(_bin_comps(list(range(1000)), -1)[0])
            + ".",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            S,
            "Binary search runs in O(log n) worst case on which input?",
            "a linked list of n integers in increasing order",
            "an array of n integers in increasing order",
            "an array of n integers in arbitrary order",
            "a linked list of n integers in arbitrary order",
            "B",
            "Need O(1) index access and sorted order. Linked lists make mid access O(n).",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            S,
            "Linear search on an unordered array of n distinct keys. Which statements are correct?",
            "Worst-case successful search does n key comparisons",
            "Best-case successful search does 1 comparison",
            "Average successful search (uniform) does (n+1)/2 comparisons",
            "Unsuccessful search can be done in O(1) expected time without hashing",
            "A;B;C",
            "Without extra structure an unsuccessful linear scan is Theta(n).",
            marks=2,
            diff="E",
        )
    )

    o.append(
        nat(
            S,
            "Unordered array ExamMarks = [41, 17, 63, 8, 55, 29]. Linear search from the left for 55 performs how many comparisons?",
            5,
            "55 is the 5th element (1-based), so 5 comparisons.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            S,
            "Unordered array PacketLen = [20, 11, 9, 40, 7]. Linear search for 6 (absent) performs how many comparisons?",
            5,
            "Every element is compared; then the search fails.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            S,
            "Sentinel linear search puts the key at the end of an n-element array (now n+1 cells). For an unsuccessful search the number of key comparisons is",
            "n+1",
            "n",
            "1",
            "2n",
            "A",
            "The sentinel is found after n failures plus 1 match against the sentinel.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            S,
            "Binary search on a sorted array of size 1 for a present key uses how many mid comparisons?",
            1,
            "lo=hi=0, one comparison at mid, success.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            S,
            "Ternary search on a unimodal discrete array splits into three thirds. Compared with binary search on a strictly increasing array of n keys, ternary search's comparison count is",
            "still Theta(log n) but with a larger constant if each step does two comparisons",
            "O(1)",
            "Theta(n)",
            "Theta(n log n)",
            "A",
            "log3 n steps, each up to 2 comparisons, still logarithmic.",
            marks=1,
            diff="M",
        )
    )

    So = "Sorting"

    named = [
        ("QuizMarks", [4, 3, 2, 1, 5]),
        ("LabQueue", [5, 1, 4, 2, 8]),
        ("HeapTrace", [9, 7, 5, 3, 1]),
        ("InorderBuf", [1, 2, 4, 3, 5]),
        ("PivotDemo", [6, 1, 5, 2, 4, 3]),
        ("StableTry", [3, 1, 3, 2]),
        ("NearlySorted", [1, 2, 3, 5, 4]),
        ("RotatedFive", [5, 4, 3, 2, 1]),
        ("DupKeys", [2, 2, 1, 1, 3]),
        ("MidPeak", [1, 4, 3, 2, 5]),
        ("SawTooth", [1, 5, 2, 6, 3]),
        ("TinyFour", [8, 4, 6, 2]),
        ("CoachList", [10, 30, 20, 50, 40]),
        ("SeedRand", [7, 2, 9, 4, 6, 1]),
        ("TwoSwap", [2, 1, 4, 3, 6, 5]),
    ]

    for name, arr in named:
        bs, _ = _bubble_swaps(arr)
        o.append(
            nat(
                So,
                "Bubble sort (adjacent swaps, ascending, full n-1 passes, no early-stop) on "
                + name
                + " = "
                + str(arr)
                + ". The number of swaps is",
                bs,
                "Each inversion is swapped exactly once in this bubble-sort variant; the inversion count is "
                + str(bs)
                + ".",
                marks=2,
                diff="M",
            )
        )

    for name, arr in named[:8]:
        ins, _ = _ins_swaps(arr)
        o.append(
            nat(
                So,
                "Insertion sort (adjacent transpositions to place the key) on "
                + name
                + " = "
                + str(arr)
                + ". Number of swaps is",
                ins,
                "Adjacent insertion sort also swaps once per inversion, so the count equals the inversion number "
                + str(ins)
                + ".",
                marks=2,
                diff="M",
            )
        )

    for name, arr in named[:8]:
        ss, _ = _sel_swaps(arr)
        o.append(
            nat(
                So,
                "Selection sort (swap the current index with the min of the suffix, skip if already in place) on "
                + name
                + " = "
                + str(arr)
                + ". Number of swaps is",
                ss,
                "Selection sort does at most n-1 swaps; here it does "
                + str(ss)
                + ".",
                marks=1,
                diff="M",
            )
        )

    arr = [4, 3, 2, 1, 5]
    o.append(
        mcq(
            So,
            "Array CabinBags = [4, 3, 2, 1, 5] is sorted ascending. After exactly two passes of selection sort (each pass places the next minimum), the array is",
            "[1, 2, 3, 4, 5]",
            "[2, 1, 3, 4, 5]",
            "[2, 3, 4, 1, 5]",
            "[1, 3, 2, 4, 5]",
            "A",
            "Pass1 swaps 4 with 1 -> [1,3,2,4,5]; pass2 swaps 3 with 2 -> [1,2,3,4,5]. Selection after 2 passes has the two smallest in place.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        mcq(
            So,
            "Array CabinBags = [4, 3, 2, 1, 5]. After exactly two passes of bubble sort (adjacent, each pass sinks the next maximum to the right), the array is",
            "[2, 1, 3, 4, 5]",
            "[1, 2, 3, 4, 5]",
            "[3, 2, 1, 4, 5]",
            "[4, 3, 2, 1, 5]",
            "A",
            "After pass1 the largest 5 is already at the end and 4 has bubbled; after pass2 the suffix of length 2 is sorted.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        mcq(
            So,
            "Insertion sort on CabinBags = [4, 3, 2, 1, 5] after processing the first three keys (i.e. the prefix of length 3 is sorted, the rest untouched) yields",
            "[2, 3, 4, 1, 5]",
            "[1, 2, 3, 4, 5]",
            "[2, 1, 3, 4, 5]",
            "[3, 4, 2, 1, 5]",
            "A",
            "After two insertions the prefix of length 3 is [2,3,4] and the tail is [1,5].",
            marks=2,
            diff="M",
        )
    )

    qs_arr = [5, 2, 8, 1, 9, 3]
    sw, sorted_a = _lomuto_swaps(qs_arr)
    o.append(
        nat(
            So,
            "In-place Quicksort with Lomuto partition and last-element pivot on PivotTrace = [5, 2, 8, 1, 9, 3]. A swap is counted whenever two distinct indices exchange values (including the final pivot swap in a partition). The number of swaps is",
            sw,
            "Simulated Lomuto quicksort performs "
            + str(sw)
            + " distinct-index swaps and yields "
            + str(sorted_a)
            + ".",
            marks=2,
            diff="H",
        )
    )

    qs_arr2 = [10, 7, 8, 9, 1, 5]
    sw2, _ = _lomuto_swaps(qs_arr2)
    o.append(
        nat(
            So,
            "Lomuto-quicksort, last-element pivot, count swaps of distinct indices, on LastPivot = [10, 7, 8, 9, 1, 5]. Swap count is",
            sw2,
            "Simulation gives " + str(sw2) + " swaps.",
            marks=2,
            diff="H",
        )
    )

    qs_arr3 = [4, 3, 2, 1]
    sw3, _ = _lomuto_swaps(qs_arr3)
    o.append(
        nat(
            So,
            "Lomuto-quicksort, last-element pivot, distinct-index swaps, on ReverseFour = [4, 3, 2, 1]. Swap count is",
            sw3,
            "Worst-case split; simulation gives " + str(sw3) + ".",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            So,
            "Quicksort on n distinct keys with the first element of the current subarray as pivot, keys in random order, partition in linear time. Expected time T(n) satisfies",
            "T(n) = (1/n) * sum_{k=0..n-1} (T(k)+T(n-1-k)) + Theta(n)",
            "T(n) = T(n-1) + T(0) + Theta(n)",
            "T(n) = 2 T(n/2) + Theta(1)",
            "T(n) = T(n/4) + T(3n/4) + Theta(1)",
            "A",
            "A random (or random-input first) pivot is equally likely to have rank 0..n-1, giving the averaging recurrence.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            So,
            "Quicksort with a pivot that is always the smallest key of the subarray (adversarial) has recurrence",
            "T(n) = T(n-1) + Theta(n)",
            "T(n) = 2 T(n/2) + Theta(n)",
            "T(n) = T(n/2) + Theta(1)",
            "T(n) = 2 T(n-1) + Theta(n)",
            "A",
            "One side is empty, the other has n-1, plus linear partition: Theta(n^2).",
            marks=1,
            diff="M",
        )
    )

    inv, _ = _merge_count([2, 4, 1, 3, 5])
    o.append(
        nat(
            So,
            "Mergesort's merge counts split inversions. For MergeTrace = [2, 4, 1, 3, 5] the number of inversions (pairs i<j, a[i]>a[j]) is",
            inv,
            "Inversions: (2,1),(4,1),(4,3) so 3. Simulation=" + str(inv) + ".",
            marks=1,
            diff="M",
        )
    )

    inv2, _ = _merge_count([5, 4, 3, 2, 1])
    o.append(
        nat(
            So,
            "Number of inversions in ReverseFive = [5, 4, 3, 2, 1] is",
            inv2,
            "C(5,2)=10.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            So,
            "Mergesort on n keys uses the standard two-way merge. The extra array space (besides the input) is",
            "Theta(n)",
            "Theta(1)",
            "Theta(log n)",
            "Theta(n^2)",
            "A",
            "The merge buffer is linear; the recursion stack is only log n.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            So,
            "Which algorithms are stable in their usual textbook form?",
            "insertion sort",
            "mergesort (left half preferred on ties)",
            "heapsort",
            "selection sort (swap min into place)",
            "A;B",
            "Heapsort and typical selection sort swap non-adjacent equal keys and are not stable.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        msq(
            So,
            "Which algorithms sort in Theta(n^2) comparisons in the worst case on an array?",
            "insertion sort",
            "selection sort",
            "heapsort",
            "bubble sort (no early abort needed for the bound)",
            "A;B;D",
            "Heapsort is Theta(n log n) worst case.",
            marks=2,
            diff="E",
        )
    )

    o.append(
        mcq(
            So,
            "Among insertion, selection and bubble (adjacent) sorts on the array [4,3,2,1,5], which one has the prefix of length 2 equal to [1,2] after exactly two passes?",
            "selection sort only",
            "bubble sort only",
            "insertion sort only",
            "all three",
            "A",
            "Selection places the global min then the next min at the front. Bubble places maxima at the back. Insertion only sorts a growing prefix from the left, which after two insertions is [2,3,4] plus tail.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        nat(
            So,
            "Standard mergesort splits in half. For n=8 the number of merge-pass levels (times the whole array is merged from pairs, 4s, 8s) is",
            3,
            "log2 8 = 3 levels.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            So,
            "A single merge of two sorted runs of lengths 3 and 5 uses how many key comparisons in the worst case?",
            7,
            "Worst case leaves one key in a run: 3+5-1=7 comparisons.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            So,
            "Quicksort vs mergesort on arrays. Which statement is correct?",
            "mergesort's worst-case comparisons are Theta(n log n); quicksort's are Theta(n^2)",
            "both are Theta(n) worst case",
            "quicksort is stable in the usual in-place Lomuto form",
            "mergesort is in-place with Theta(1) extra memory in the usual form",
            "A",
            "Standard facts: in-place QS is not stable; usual MS needs a buffer.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            So,
            "Selection sort on n=6 keys always performs how many key comparisons (independent of the input order)?",
            15,
            "5+4+3+2+1=15.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            So,
            "Bubble sort without early abort on n=6 keys performs how many adjacent comparisons?",
            15,
            "Same triangular number 15.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            So,
            "Insertion sort on a strictly increasing array of n keys performs how many key comparisons?",
            "n-1 (each new key compared once and already in place)",
            "n(n-1)/2",
            "n log n",
            "0",
            "A",
            "Best case: each of n-1 insertions stops after one comparison.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            So,
            "A 3-way partition quicksort (Dutch-national-flag style) on keys with many duplicates is attractive because",
            "equal-to-pivot keys are excluded from both recursive calls",
            "it uses no extra memory versus Lomuto",
            "it makes the algorithm stable",
            "the worst case becomes Theta(n log n) for all inputs",
            "A",
            "The middle band of equals is finished; worst case on distinct keys is still quadratic if pivots are bad.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            So,
            "Heap-sort first build-heap on n=7 keys using Floyd's method. The number of sink operations during build-heap is equal to the number of non-leaves, which is",
            3,
            "Non-leaves in a complete 7-node tree: floor(7/2)=3.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            So,
            "After the first extract-max pass of heapsort on a max-heap [9, 6, 8, 2, 5, 7, 3] (n=7), the last array position holds",
            "9",
            "8",
            "3",
            "2",
            "A",
            "Extract-max swaps the root 9 with the last key and shrinks the heap; 9 sits at the end in its final sorted position.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        msq(
            So,
            "Let n=5 and array [2, 1, 4, 3, 5]. Which claims hold?",
            "bubble sort (adjacent) performs exactly 2 swaps",
            "insertion sort (adjacent) performs exactly 2 swaps",
            "selection sort performs exactly 2 swaps (min of suffix, skip if in place)",
            "the array has exactly 2 inversions",
            "A;B;D",
            "Inversions (2,1) and (4,3). Selection: min 1 swapped with 2 (1 swap), then min of [2,4,3,5] is 2 already in place (0), then min of [4,3,5] is 3 swapped with 4 (1), total 2 swaps actually! Wait C is also true. All four? Selection: i=0 min at 1 swap; i=1 min is 2 at index 1 no swap; i=2 min is 3 at index 3 swap with 4; i=3 min of [4,5] is 4 no swap. 2 swaps. Then A;B;C;D. Keep all.",
            marks=2,
            diff="H",
        )
    )
    o[-1] = msq(
        So,
        "Array PairSwap = [2, 1, 4, 3, 5]. Which claims hold?",
        "the array has exactly two inversions",
        "adjacent bubble sort performs exactly two swaps",
        "adjacent insertion sort performs exactly two swaps",
        "mergesort extra memory is Theta(1)",
        "A;B;C",
        "Inversions (2,1),(4,3); adjacent bubble/insertion swap once per inversion. Usual mergesort needs a linear buffer.",
        marks=2,
        diff="M",
    )

    o.append(
        nat(
            So,
            "The number of comparisons used by mergesort on n=16 in the standard recurrence T(n)=2T(n/2)+n-1, T(1)=0, is",
            16 * 4 - 16 + 0 if False else None,
            "T(n)=n ceil(log n) - n + 1 for powers of two: 16*4 - 16 + 1 = 49.",
            marks=2,
            diff="H",
        )
    )

    def merge_comps(n):
        if n <= 1:
            return 0
        a = n // 2
        b = n - a
        # worst-case? The recurrence T=2T(n/2)+n-1 is for the comparison count of the usual implementation in the worst case of each merge.
        return merge_comps(a) + merge_comps(b) + (n - 1)

    o[-1] = nat(
        So,
        "Using T(n)=T(floor n/2)+T(ceil n/2)+(n-1), T(1)=0 (each merge uses n-1 comparisons), T(16) equals",
        merge_comps(16),
        "For powers of two T(n)=n lg n - n + 1 = 64-16+1=49.",
        marks=2,
        diff="H",
    )

    o.append(
        mcq(
            So,
            "A lower bound on comparisons to sort n distinct keys in the worst case in the comparison model is",
            "ceil(log2(n!))",
            "n-1",
            "n",
            "2^n",
            "A",
            "There are n! permutations; each comparison has 2 outcomes.",
            marks=1,
            diff="M",
        )
    )

    return o


def _graphs():
    o = []
    T = "Graphs"

    graphs = [
        (
            "Campus",
            False,
            [
                ("Admin", "Lab"),
                ("Lab", "Canteen"),
                ("Canteen", "Hostel"),
                ("Admin", "Library"),
                ("Library", "Hostel"),
            ],
            "Admin",
        ),
        (
            "Harbor",
            False,
            [
                ("Pier", "Dock"),
                ("Dock", "Yard"),
                ("Yard", "Gate"),
                ("Pier", "Shed"),
                ("Shed", "Gate"),
                ("Dock", "Shed"),
            ],
            "Pier",
        ),
        (
            "Metro",
            False,
            [
                ("North", "Hub"),
                ("Hub", "East"),
                ("Hub", "West"),
                ("East", "South"),
                ("West", "South"),
            ],
            "Hub",
        ),
        (
            "Forest",
            False,
            [
                ("Oak", "Pine"),
                ("Pine", "Birch"),
                ("Birch", "Maple"),
                ("Oak", "Elm"),
                ("Elm", "Maple"),
                ("Pine", "Elm"),
            ],
            "Oak",
        ),
        (
            "Airline",
            True,
            [
                ("Delhi", "Mumbai"),
                ("Delhi", "Pune"),
                ("Mumbai", "Goa"),
                ("Pune", "Goa"),
                ("Goa", "Kochi"),
            ],
            "Delhi",
        ),
        (
            "Pipeline",
            True,
            [
                ("Src", "A"),
                ("Src", "B"),
                ("A", "C"),
                ("B", "C"),
                ("C", "Sink"),
                ("A", "Sink"),
            ],
            "Src",
        ),
        (
            "Gridlock",
            False,
            [
                ("A1", "A2"),
                ("A2", "A3"),
                ("A1", "B1"),
                ("A2", "B2"),
                ("A3", "B3"),
                ("B1", "B2"),
                ("B2", "B3"),
            ],
            "A1",
        ),
        (
            "Club",
            False,
            [("Ram", "Sam"), ("Sam", "Tom"), ("Tom", "Uma"), ("Ram", "Uma"), ("Sam", "Uma")],
            "Ram",
        ),
        (
            "LabNet",
            True,
            [("S0", "S1"), ("S0", "S2"), ("S1", "S3"), ("S2", "S3"), ("S3", "S4"), ("S1", "S4")],
            "S0",
        ),
        (
            "River",
            False,
            [("North", "Island"), ("Island", "South"), ("North", "West"), ("West", "South")],
            "North",
        ),
    ]

    for name, directed, edges, start in graphs:
        b = _bfs(edges, start, directed)
        d = _dfs(edges, start, directed)
        kind = "directed" if directed else "undirected unweighted"
        elist = ", ".join(u + "->" + v if directed else u + "-" + v for u, v in edges)
        nodes = []
        seen_n = set()
        for u, v in edges:
            if u not in seen_n:
                nodes.append(u)
                seen_n.add(u)
            if v not in seen_n:
                nodes.append(v)
                seen_n.add(v)
        b_s = " ".join(b)
        d_s = " ".join(d)
        rev_b = " ".join(reversed(b))
        rev_d = " ".join(reversed(d))
        alpha = " ".join(sorted(nodes))
        ralpha = " ".join(sorted(nodes, reverse=True))
        start_last = " ".join(nodes[1:] + nodes[:1])

        def four(correct, cands):
            opts = [correct]
            for c in cands:
                if c not in opts:
                    opts.append(c)
                if len(opts) == 4:
                    break
            pad = 0
            while len(opts) < 4:
                pad += 1
                extra = " ".join(nodes[pad:] + nodes[:pad]) + (" *" * 0)
                if extra not in opts:
                    opts.append(extra)
            return opts

        b_opts = four(b_s, [d_s, rev_b, alpha, ralpha, start_last])
        d_opts = four(d_s, [b_s, rev_d, ralpha, alpha, start_last])
        o.append(
            mcq(
                T,
                kind.capitalize()
                + " graph "
                + name
                + " has edges "
                + elist
                + ". BFS from "
                + start
                + " scans neighbours in alphabetical order. The dequeue order is",
                b_opts[0],
                b_opts[1],
                b_opts[2],
                b_opts[3],
                "A",
                "BFS with alpha neighbour order dequeues " + b_s + ".",
                marks=2,
                diff="M",
            )
        )
        o.append(
            mcq(
                T,
                kind.capitalize()
                + " graph "
                + name
                + " has edges "
                + elist
                + ". Recursive DFS from "
                + start
                + " with neighbours tried in alphabetical order. The discovery order is",
                d_opts[0],
                d_opts[1],
                d_opts[2],
                d_opts[3],
                "A",
                "DFS discovery order is " + d_s + ".",
                marks=2,
                diff="M",
            )
        )
        o.append(
            nat(
                T,
                "In graph "
                + name
                + " (edges "
                + elist
                + "), BFS from "
                + start
                + " with alphabetical neighbour order visits how many vertices?",
                len(b),
                "The reachable set has size " + str(len(b)) + ".",
                marks=1,
                diff="E",
            )
        )

    o.append(
        mcq(
            T,
            "Undirected graph Campus has edges Admin-Lab, Lab-Canteen, Canteen-Hostel, Admin-Library, Library-Hostel. How many connected components does it have?",
            "1",
            "2",
            "3",
            "5",
            "A",
            "Every vertex is reachable from Admin; the graph is connected.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "Undirected graph Forest has 6 vertices Oak,Pine,Birch,Maple,Elm,Ash and edges Oak-Pine, Pine-Birch, Birch-Maple, Oak-Elm, Elm-Maple, Pine-Elm. Ash is isolated. The number of connected components is",
            2,
            "Five trees form one connected piece; Ash is a second component.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "A tree on 12 vertices has how many edges?",
            11,
            "A tree on n vertices has n-1 edges.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            T,
            "Let G be an undirected simple graph on n>=2 vertices. Which statements are true?",
            "If G is a tree then G is connected and has n-1 edges",
            "If G is connected and has n-1 edges then G is a tree",
            "If G has n-1 edges then G is a tree",
            "Every tree is bipartite",
            "A;B;D",
            "n-1 edges alone do not imply a tree (a triangle plus an isolated vertex has n=4, e=3). Trees have no odd cycles, hence are bipartite.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "Degree sequence of undirected graph Club with edges Ram-Sam, Sam-Tom, Tom-Uma, Ram-Uma, Sam-Uma is (vertices Ram,Sam,Tom,Uma in that name order)",
            "2,3,2,3",
            "3,3,3,3",
            "1,2,2,3",
            "2,2,2,2",
            "A",
            "Ram: Sam,Uma (2); Sam: Ram,Tom,Uma (3); Tom: Sam,Uma (2); Uma: Tom,Ram,Sam (3).",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Handshaking: undirected Harbor has edges Pier-Dock, Dock-Yard, Yard-Gate, Pier-Shed, Shed-Gate, Dock-Shed. The sum of degrees is",
            12,
            "6 edges contribute 12 to the degree sum.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Which of the following degree sequences is graphic for a simple undirected graph on 4 vertices?",
            "3,1,1,1",
            "3,3,3,1",
            "4,2,2,2",
            "3,3,1,1",
            "A",
            "3,1,1,1 is a star (K1,3). 3,3,3,1 is not graphic (Havel-Hakimi fails). 4 exceeds n-1. 3,3,1,1 forces two vertices of degree 3 on 4 vertices, hence the other two have degree at least 2, contradiction with two 1s.",
            marks=2,
            diff="H",
        )
    )

    # Dijkstra instances
    dij = [
        (
            "RoadNet",
            [("S", "A", 4), ("S", "B", 1), ("B", "A", 2), ("A", "C", 1), ("B", "C", 5), ("C", "T", 3), ("B", "T", 8)],
            "S",
            "T",
        ),
        (
            "PacketNet",
            [("U", "V", 2), ("U", "W", 5), ("V", "W", 1), ("V", "X", 4), ("W", "X", 1)],
            "U",
            "X",
        ),
        (
            "HillWalk",
            [("Base", "Ridge", 6), ("Base", "Lake", 3), ("Lake", "Ridge", 2), ("Ridge", "Peak", 4), ("Lake", "Peak", 9)],
            "Base",
            "Peak",
        ),
        (
            "CityCab",
            [("Home", "X", 7), ("Home", "Y", 2), ("Y", "X", 3), ("X", "Office", 1), ("Y", "Office", 8)],
            "Home",
            "Office",
        ),
        (
            "RailLink",
            [("Pune", "Mumbai", 10), ("Pune", "Lonavala", 4), ("Lonavala", "Mumbai", 5), ("Mumbai", "Goa", 8), ("Lonavala", "Goa", 20)],
            "Pune",
            "Goa",
        ),
    ]
    for name, edges, s, t in dij:
        dist = _dijkstra(edges, s)
        el = ", ".join(u + "->" + v + "(" + str(w) + ")" for u, v, w in edges)
        o.append(
            nat(
                T,
                "Directed weighted graph "
                + name
                + " with edges "
                + el
                + ". Dijkstra from "
                + s
                + " (non-negative weights). Shortest-path distance to "
                + t
                + " is",
                int(dist[t]),
                "Dijkstra distance " + str(dist) + ".",
                marks=2,
                diff="M",
            )
        )

    o.append(
        mcq(
            T,
            "BFS on an unweighted graph computes",
            "a shortest path in number of edges from the source to every reachable vertex",
            "a minimum spanning tree",
            "shortest paths for negative weights",
            "a topological order of every directed graph",
            "A",
            "Each BFS layer is the next hop distance.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            T,
            "Dijkstra's algorithm (as taught with a min-priority queue, non-negative weights) . Which are correct?",
            "It may fail if some edge weight is negative",
            "It computes shortest paths from one source",
            "It requires the graph to be a DAG",
            "On an unweighted graph it is no better asymptotically than BFS if implemented with a binary heap on dense graphs, and BFS is the natural choice",
            "A;B;D",
            "Dijkstra is single-source and needs non-negative weights; it does not need a DAG (that's for one DP method).",
            marks=2,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "A directed graph has edges A->B, B->C, A->C, C->D. How many topological orders exist?",
            "2",
            "1",
            "3",
            "6",
            "B",
            "A must be first, then B before C, C before D, and B before C. A,B,C,D is the only order (A then B then C then D); A,C,... is illegal because B must precede C. Only ABCD.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "Directed edges P->Q, P->R, Q->S, R->S. The number of topological orders is",
            "2",
            "1",
            "3",
            "4",
            "A",
            "P first, S last; Q and R may be swapped: P Q R S and P R Q S.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Undirected cycle of 8 vertices (C8). BFS from one vertex visits how many vertices at distance exactly 2?",
            2,
            "The two vertices two hops away, one each direction, plus not the opposite which is distance 4.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Complete graph K5 has how many edges?",
            10,
            "C(5,2)=10.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "Complete bipartite K(3,4) has how many edges?",
            12,
            "Every of 3 vertices meets 4 vertices: 12 edges.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "Which graph is not bipartite?",
            "an undirected triangle C3",
            "any tree",
            "C6",
            "K(2,5)",
            "A",
            "Odd cycles are not bipartite.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "DFS on an undirected connected graph produces a DFS tree. A back edge in that classification indicates",
            "a cycle",
            "a bridge",
            "that the graph is bipartite",
            "that the graph is a tree",
            "A",
            "A back edge to an ancestor closes a cycle.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "A connected undirected graph has 10 vertices and 12 edges. The minimum number of edges that must be removed to make it a tree is",
            3,
            "A tree would have 9 edges; remove 12-9=3 (and keep connected, which is possible by dropping extra edges of cycles).",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "Bellman-Ford vs Dijkstra on a directed graph with a negative edge but no negative cycle. Which is correct?",
            "Bellman-Ford still computes correct single-source distances; Dijkstra may not",
            "Dijkstra is always correct here because there is no negative cycle",
            "Both require all weights positive",
            "BFS computes the same distances as both",
            "A",
            "Negative edges (without negative cycles) are the setting Bellman-Ford handles and Dijkstra does not.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "BFS from vertex Src in directed Pipeline with edges Src->A, Src->B, A->C, B->C, C->Sink, A->Sink, neighbours in alpha order. The hop-distance to Sink is",
            2,
            "Src-A-Sink is a 2-edge path; BFS first reaches Sink at layer 2.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "An adjacency-matrix representation of a simple undirected graph on n vertices uses Theta(n^2) space. BFS from one vertex then runs in",
            "Theta(n^2) time in the worst case",
            "Theta(n+m) time always, independent of the matrix",
            "Theta(n) time",
            "Theta(n^3) time",
            "A",
            "Scanning a row to find neighbours costs Theta(n) per vertex, total Theta(n^2).",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "Adjacency lists of a directed graph with n vertices and m edges support BFS from one vertex in",
            "Theta(n+m) time",
            "Theta(n^2) time always",
            "Theta(m log n) time",
            "Theta(n m) time",
            "A",
            "Each vertex and each edge is scanned O(1) times.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        msq(
            T,
            "Undirected simple graph G. Which are equivalent to G being a tree?",
            "G is connected and has no cycle",
            "G is connected and has n-1 edges",
            "there is a unique path between every pair of vertices",
            "G is bipartite and has n-1 edges",
            "A;B;C",
            "A bipartite graph with n-1 edges need not be connected (or can have a cycle if not connected properly); D fails. A,B,C are standard tree characterizations.",
            marks=2,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "A DAG on vertices W,X,Y,Z has edges W->X, W->Y, X->Z, Y->Z. The number of distinct topological sorts is",
            2,
            "WXYZ and WYXZ.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "In an undirected unweighted graph, if BFS from s first reaches t via parent p, then",
            "dist(s,t)=dist(s,p)+1 and this dist is minimum hop count",
            "the path s..p,t is a unique shortest path",
            "DFS would find the same parent",
            "t is a neighbour of s",
            "A",
            "BFS parents encode some shortest path, not necessarily the unique one.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Directed graph Airline: Delhi->Mumbai, Delhi->Pune, Mumbai->Goa, Pune->Goa, Goa->Kochi. Number of simple paths from Delhi to Kochi is",
            2,
            "Delhi-Mumbai-Goa-Kochi and Delhi-Pune-Goa-Kochi.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "A spanning tree of a connected undirected graph with 20 vertices has how many edges?",
            "19",
            "20",
            "21",
            "10",
            "A",
            "Any tree on 20 vertices has 19 edges.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "How many spanning trees does K3 (a triangle) have?",
            3,
            "Any two of the three edges form a spanning tree.",
            marks=1,
            diff="E",
        )
    )

    o.append(
        mcq(
            T,
            "If Dijkstra is run on RoadNet with non-negative weights from S, the set of finalized vertices grows by extracting the min tentative distance. The first vertex finalized after S, given edges S->A(4), S->B(1), B->A(2), A->C(1), B->C(5), C->T(3), B->T(8), is",
            "B",
            "A",
            "C",
            "T",
            "A",
            "Tentative: A=4, B=1. Extract B next.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "On that same RoadNet, after Dijkstra from S, the shortest-path distance of A is",
            3,
            "S-B-A = 1+2 = 3, better than the direct 4.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        msq(
            T,
            "Which claims about BFS and DFS on a finite directed graph G (no self-loops) are always true?",
            "From a vertex v, BFS and DFS visit exactly the same set of vertices (the descendants of v in the reachable sense)",
            "The order of first visits in BFS is always the reverse of DFS",
            "If G^R is G with all edges reversed, u reachable from v in G implies v reachable from u in G^R",
            "BFS requires a queue and DFS a stack (or recursion stack)",
            "A;C;D",
            "Reachable sets coincide for BFS and DFS; visit orders need not be reverses. Reachability reverses with the edges.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            T,
            "An undirected graph is Eulerian (has a closed trail using every edge) if and only if",
            "it is connected (ignoring isolated vertices) and every degree is even",
            "it is a tree",
            "it is complete",
            "it has exactly two odd-degree vertices",
            "A",
            "Euler's theorem. Exactly two odd degrees give an open Euler trail, not a circuit.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        nat(
            T,
            "Hypercube Q3 (the cube graph) has how many vertices and how many edges? Report the number of edges.",
            12,
            "Q3 has 8 vertices, each degree 3, so 12 edges.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "A cut-vertex (articulation point) of a connected graph is a vertex whose removal",
            "increases the number of connected components",
            "decreases the number of edges by 1 always",
            "always leaves the graph a tree",
            "cannot lie on a cycle",
            "A",
            "That is the definition. Cut-vertices often do lie on cycles (e.g. two cycles sharing a vertex).",
            marks=1,
            diff="E",
        )
    )

    o.append(
        nat(
            T,
            "Grid graph of a 3x3 lattice of vertices with edges between 4-neighbours. Number of vertices is 9; number of edges is",
            12,
            "Horizontal: 3 rows * 2 = 6; vertical: 3 cols * 2 = 6; total 12.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        mcq(
            T,
            "If every edge of an undirected connected graph has weight 1, Dijkstra's distances from s coincide with",
            "BFS hop distances from s",
            "DFS discovery times",
            "the number of spanning trees",
            "the maximum degree",
            "A",
            "Unit weights make Dijkstra degenerate to BFS (with a queue).",
            marks=1,
            diff="E",
        )
    )

    return o


def items():
    o = []
    o.extend(_python())
    o.extend(_linear_ds())
    o.extend(_trees_hash())
    o.extend(_search_sort())
    o.extend(_graphs())
    return uniq(o)
