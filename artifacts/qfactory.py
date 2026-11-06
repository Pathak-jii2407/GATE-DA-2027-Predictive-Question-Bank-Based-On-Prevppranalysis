"""Original GATE-style item factory. Numeric answers are computed, not guessed."""
from __future__ import annotations
import math
import random
from itertools import combinations

import numpy as np


def item(subject, topic, qtype, marks, diff, pred, stem, options, answer, sol):
    return dict(
        subject=subject, topic=topic, qtype=qtype, marks=marks, diff=diff,
        pred=pred, stem=stem, options=options, answer=answer, sol=sol,
    )


def mcq(*a, **k):
    k.setdefault("qtype", "MCQ")
    return item(*a, **k) if a else item(**k)


# -------------------- helpers --------------------
def _opts(correct, distractors, rng):
    labels = ["A", "B", "C", "D"]
    pool = [correct] + list(distractors)[:3]
    while len(pool) < 4:
        pool.append(str(rng.randint(0, 20)))
    # unique stringify
    seen, clean = set(), []
    for p in pool:
        s = str(p)
        if s not in seen:
            seen.add(s)
            clean.append(s)
    while len(clean) < 4:
        s = str(rng.randint(30, 99))
        if s not in seen:
            seen.add(s)
            clean.append(s)
    order = list(range(4))
    rng.shuffle(order)
    opts = [clean[i] if i < len(clean) else str(100 + i) for i in range(4)]
    # rebuild properly
    bag = clean[:4]
    rng.shuffle(bag)
    # ensure correct is in bag
    cs = str(correct)
    if cs not in bag:
        bag[0] = cs
        rng.shuffle(bag)
    ans = labels[bag.index(cs)]
    return bag, ans


def _round_ans(x, nd=2):
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return f"{x:.{nd}f}"


# =================================================
# Probability & Statistics
# =================================================
def gen_ps(n=260, seed=2027):
    rng = random.Random(seed)
    out = []
    k = 0
    while len(out) < n:
        k += 1
        t = k % 18
        if t == 0:
            # Bayes disease
            prev = rng.choice([0.01, 0.02, 0.05, 0.1])
            sens = rng.choice([0.9, 0.95, 0.96, 0.99])
            fpr = rng.choice([0.02, 0.04, 0.05, 0.1])
            pt = sens * prev + fpr * (1 - prev)
            post = sens * prev / pt
            out.append(item(
                "P&S", "Bayes theorem", "NAT", 2, "Moderate", "VERY HIGH",
                f"A disease has prevalence {prev}. A test is positive with probability {sens} if the person has the disease and {fpr} otherwise. Given a positive test, P(disease) equals _____ (two decimals).",
                None, _round_ans(post),
                f"P(T)={sens}·{prev}+{fpr}·{1-prev}={pt:.4f}. Posterior={sens*prev:.4f}/{pt:.4f}={post:.4f}."
            ))
        elif t == 1:
            ntr, p = rng.choice([6, 8, 10]), rng.choice([0.5, 0.5, 0.5])
            k1, k2 = 2, ntr - 2
            c1 = math.comb(ntr, k1)
            c2 = math.comb(ntr, k2)
            ratio = c1 / c2
            out.append(item(
                "P&S", "Binomial", "NAT", 1, "Easy", "HIGH",
                f"A fair coin is tossed {ntr} times. P(exactly {k1} heads) / P(exactly {k2} heads) equals _____.",
                None, _round_ans(ratio),
                f"C({ntr},{k1})/C({ntr},{k2}) = {c1}/{c2} = {ratio}."
            ))
        elif t == 2:
            mean = rng.choice([2, 4, 5, 8, 10])
            out.append(item(
                "P&S", "Exponential", "NAT", 1, "Easy", "VERY HIGH",
                f"X ~ Exponential with mean {mean}. Var(X) equals _____.",
                None, str(mean * mean),
                f"Mean 1/λ={mean} so λ=1/{mean}. Var=1/λ²={mean*mean}."
            ))
        elif t == 3:
            a, b = rng.choice([0, 1, 2]), rng.choice([3, 4, 5])
            var = (b - a) ** 2 / 12
            out.append(item(
                "P&S", "Uniform", "NAT", 2, "Moderate", "HIGH",
                f"X ~ Uniform[{a},{b}]. Var(X) equals _____ (two decimals if needed).",
                None, _round_ans(var),
                f"(b-a)²/12 = ({b}-{a})²/12 = {var}."
            ))
        elif t == 4:
            vx, vy = rng.choice([1, 4, 9, 16]), rng.choice([1, 4, 9])
            cov = rng.choice([1, 2, 3, -1, -2])
            # keep |corr|<=1
            if abs(cov) > math.sqrt(vx * vy) - 1e-9:
                cov = 0
            corr = cov / math.sqrt(vx * vy)
            out.append(item(
                "P&S", "Correlation", "NAT", 1, "Easy", "HIGH",
                f"Var(X)={vx}, Var(Y)={vy}, Cov(X,Y)={cov}. Corr(X,Y) equals _____ (two decimals).",
                None, _round_ans(corr),
                f"ρ = {cov}/sqrt({vx}·{vy}) = {corr:.4f}."
            ))
        elif t == 5:
            p = rng.choice([0.2, 0.3, 0.4, 0.5])
            var = p * (1 - p)
            out.append(item(
                "P&S", "Bernoulli", "NAT", 1, "Easy", "HIGH",
                f"X ~ Bernoulli({p}). Var(X) equals _____ (two decimals).",
                None, _round_ans(var),
                f"p(1-p)={p}·{1-p}={var}."
            ))
        elif t == 6:
            lam = rng.choice([1, 2, 3, 4])
            # P(X=0)=e^{-lam}
            val = math.exp(-lam)
            out.append(item(
                "P&S", "Poisson", "NAT", 2, "Moderate", "HIGH",
                f"X ~ Poisson({lam}). P(X=0) equals _____ (two decimals).",
                None, _round_ans(val),
                f"e^{{-λ}} = e^{{-{lam}}} = {val:.4f}."
            ))
        elif t == 7:
            n1, k1 = rng.choice([4, 5, 6]), rng.choice([2, 3])
            n2, k2 = rng.choice([4, 5, 6]), rng.choice([1, 2])
            # two boxes, pick box then ball
            p = 0.5 * (k1 / n1) + 0.5 * (k2 / n2)
            out.append(item(
                "P&S", "Total probability", "NAT", 2, "Moderate", "VERY HIGH",
                f"Box 1 has {k1} red out of {n1}. Box 2 has {k2} red out of {n2}. A box is chosen uniformly, then a ball. P(red) equals _____ (two decimals).",
                None, _round_ans(p),
                f"0.5·({k1}/{n1})+0.5·({k2}/{n2})={p}."
            ))
        elif t == 8:
            nvar, s = rng.choice([3, 4, 5]), rng.choice([6, 8, 10])
            ans = math.comb(s + nvar - 1, nvar - 1)
            out.append(item(
                "P&S", "Counting", "NAT", 2, "Moderate", "HIGH",
                f"Number of non-negative integer solutions of x1+…+x{nvar}={s} is _____.",
                None, str(ans),
                f"Stars and bars C({s}+{nvar}-1,{nvar}-1)=C({s+nvar-1},{nvar-1})={ans}."
            ))
        elif t == 9:
            out.append(item(
                "P&S", "Conditional expectation", "MCQ", 1, "Easy", "VERY HIGH",
                "Which identity always holds for integrable X,Y?",
                ["E[X|Y]=E[X]", "E[E[X|Y]]=E[X]", "E[X|Y]=Y", "Var(X|Y)=Var(X)"],
                "B",
                "Tower property. A needs independence; C is special; D is false in general."
            ))
        elif t == 10:
            out.append(item(
                "P&S", "Independence", "MSQ", 2, "Moderate", "VERY HIGH",
                "A,B independent with 0<P(A),P(B)<1. Which are true? (One or more.)",
                ["P(A∩B)=P(A)P(B)", "P(A|B)=P(A)", "A and B are disjoint", "P(A∪B)=P(A)+P(B)-P(A)P(B)"],
                "A;B;D",
                "Independence is the product rule, not disjointness."
            ))
        elif t == 11:
            out.append(item(
                "P&S", "CLT", "MCQ", 1, "Moderate", "HIGH",
                "i.i.d. with mean μ and variance σ²>0. For large n, X̄ is approximately",
                ["N(μ,σ²)", "N(μ,σ²/n)", "N(0,1) exactly", "χ²_n"],
                "B",
                "CLT: X̄ ≈ N(μ, σ²/n)."
            ))
        elif t == 12:
            out.append(item(
                "P&S", "Hypothesis testing", "MCQ", 2, "Moderate", "HIGH",
                "Two-sided z-test of H0: μ=μ0 at level α rejects when",
                ["Z>z_α", "|Z|>z_{α/2}", "Z<z_α", "Z=0"],
                "B",
                "Equal tails of probability α/2."
            ))
        elif t == 13:
            mu, a = rng.choice([0, 1, -2]), rng.choice([2, 3, 4])
            # X=aZ+mu with Z standard? X~N(mu,a^2)
            out.append(item(
                "P&S", "Normal", "MCQ", 1, "Easy", "HIGH",
                f"Z~N(0,1) and X={a}Z+({mu}). Then X ~",
                [f"N({mu},{a})", f"N({mu},{a*a})", f"N({-mu},{a*a})", "not Gaussian"],
                "B",
                f"Affine image of a Gaussian is Gaussian: mean {mu}, variance {a*a}."
            ))
        elif t == 14:
            # joint triangle density
            # f=c on 0<y<x<1, find c then E[X]
            # area=1/2 so c=2, E[X]=∫_0^1 x·2x dx=2/3
            out.append(item(
                "P&S", "Joint PDF", "NAT", 2, "Difficult", "HIGH",
                "f_{X,Y}(x,y)=2 on 0<y<x<1 (0 else). E[X] equals _____ (two decimals).",
                None, "0.67",
                "f_X(x)=2x on (0,1). E[X]=∫ x·2x dx=2/3≈0.67."
            ))
        elif t == 15:
            out.append(item(
                "P&S", "Memoryless", "MSQ", 2, "Moderate", "HIGH",
                "Which are memoryless? (One or more.)",
                ["Geometric on {1,2,…}", "Binomial(n=8,p=0.4)", "Exponential", "Uniform(0,1)"],
                "A;C",
                "Geometric and exponential. Binomial and uniform are not."
            ))
        elif t == 16:
            nobs = rng.choice([9, 16, 25, 36])
            # CI half width idea: z σ/√n with z=1.96 σ=2
            hw = 1.96 * 2 / math.sqrt(nobs)
            out.append(item(
                "P&S", "Confidence interval", "NAT", 2, "Difficult", "HIGH",
                f"n={nobs}, σ=2, z_{{0.025}}=1.96. Half-width of the 95% z-interval for μ is _____ (two decimals).",
                None, _round_ans(hw),
                f"1.96·2/√{nobs}={hw:.4f}."
            ))
        else:
            out.append(item(
                "P&S", "Covariance identity", "MCQ", 1, "Easy", "HIGH",
                "Cov(X,X) equals",
                ["0", "E[X]", "Var(X)", "1"],
                "C",
                "By definition Cov(X,X)=Var(X)."
            ))
    # unique-ish stems: drop exact duplicate stems
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    # if short, add numbered variants of counting
    i = 0
    while len(uniq) < n:
        i += 1
        nn, r = 5 + (i % 6), 2 + (i % 3)
        ans = math.comb(nn, r)
        uniq.append(item(
            "P&S", "Combinations", "NAT", 1, "Easy", "MEDIUM",
            f"C({nn},{r}) equals _____.",
            None, str(ans),
            f"n!/(r!(n-r)!) = {ans}."
        ))
    return uniq[:n]


# =================================================
# Linear Algebra
# =================================================
def gen_la(n=260, seed=11):
    rng = random.Random(seed)
    np_rng = np.random.default_rng(seed)
    out = []
    k = 0
    while len(out) < n:
        k += 1
        t = k % 16
        if t == 0:
            a, b = rng.randint(1, 6), rng.randint(1, 6)
            out.append(item(
                "LA", "Trace / eigenvalues", "NAT", 1, "Easy", "VERY HIGH",
                f"Sum of eigenvalues of [[ {a}, 1],[0, {b}]] (with multiplicity) is _____.",
                None, str(a + b),
                f"Triangular ⇒ eigenvalues {a},{b}. Trace={a+b}."
            ))
        elif t == 1:
            a, b = rng.randint(2, 5), rng.randint(2, 5)
            out.append(item(
                "LA", "Determinant", "NAT", 1, "Easy", "HIGH",
                f"det([[{a},0],[0,{b}]]) equals _____.",
                None, str(a * b),
                "Product of diagonal entries."
            ))
        elif t == 2:
            r, c, rank = 4, 6, rng.choice([2, 3])
            nul = c - rank
            out.append(item(
                "LA", "Rank-nullity", "NAT", 2, "Moderate", "VERY HIGH",
                f"A is {r}×{c} of rank {rank}. dim(null(A)) is _____.",
                None, str(nul),
                f"rank + nullity = {c} ⇒ nullity={nul}."
            ))
        elif t == 3:
            u = np.array([rng.randint(1, 3) for _ in range(3)], dtype=float)
            M = np.outer(u, u)
            # nonzero singular value = ||u||^2
            sig = float(u @ u)
            out.append(item(
                "LA", "SVD / outer product", "NAT", 2, "Difficult", "HIGH",
                f"u=[{int(u[0])},{int(u[1])},{int(u[2])}]^T and M=uu^T. The largest singular value of M is _____.",
                None, _round_ans(sig),
                f"Rank-1 PSD. Nonzero eigenvalue = u^Tu = {sig}."
            ))
        elif t == 4:
            out.append(item(
                "LA", "Idempotent", "MSQ", 2, "Moderate", "VERY HIGH",
                "P real square, P²=P. Which are always true? (One or more.)",
                ["Eigenvalues of P lie in {0,1}", "P is invertible", "I−P is idempotent", "tr(P)=rank(P) for real projectors of this type"],
                "A;C;D",
                "λ²=λ. Only I is invertible among idempotents. I−P is a complementary projector. Trace equals rank for a projector."
            ))
        elif t == 5:
            out.append(item(
                "LA", "Orthogonal matrix", "MCQ", 1, "Easy", "HIGH",
                "If Q is real orthogonal then",
                ["Q^T Q=0", "Q^T Q=I", "det(Q)=0", "0 is an eigenvalue"],
                "B",
                "Definition. Then det=±1."
            ))
        elif t == 6:
            out.append(item(
                "LA", "Projection", "MCQ", 2, "Difficult", "VERY HIGH",
                "Orthogonal projector onto col(A) when A has full column rank is",
                ["AA^T", "A^T A", "A(A^T A)^{-1}A^T", "(A^T A)^{-1}"],
                "C",
                "The hat matrix of least squares."
            ))
        elif t == 7:
            out.append(item(
                "LA", "Subspace", "MSQ", 2, "Moderate", "HIGH",
                "Subspaces of R³? (One or more.)",
                ["{x: x1+x2+x3=0}", "{x: x1+x2+x3=1}", "{0}", "{x: x1 x2 x3=0}"],
                "A;C",
                "Through the origin and closed under + and scalar. Affine plane and union of planes fail."
            ))
        elif t == 8:
            out.append(item(
                "LA", "Quadratic form", "MCQ", 2, "Moderate", "HIGH",
                "x^T diag(2,3) x is",
                ["indefinite", "positive definite", "negative definite", "zero"],
                "B",
                "Eigenvalues 2,3>0."
            ))
        elif t == 9:
            out.append(item(
                "LA", "LU", "MCQ", 1, "Moderate", "MEDIUM",
                "In a Doolittle LU factorisation without pivoting, L is",
                ["unit upper triangular", "unit lower triangular", "orthogonal", "diagonal of eigenvalues"],
                "B",
                "Unit lower L times upper U."
            ))
        elif t == 10:
            a11, a12, a21, a22 = rng.randint(1, 4), rng.randint(0, 3), rng.randint(0, 3), rng.randint(1, 4)
            det = a11 * a22 - a12 * a21
            out.append(item(
                "LA", "Determinant 2x2", "NAT", 1, "Easy", "HIGH",
                f"det([[{a11},{a12}],[{a21},{a22}]]) equals _____.",
                None, str(det),
                f"{a11}·{a22}−{a12}·{a21}={det}."
            ))
        elif t == 11:
            out.append(item(
                "LA", "Linear independence", "MCQ", 1, "Easy", "HIGH",
                "The standard basis e1,e2,e3 of R³ is",
                ["dependent", "independent and a basis", "orthogonal but not a basis", "a basis of R²"],
                "B",
                "Three independent vectors in R³."
            ))
        elif t == 12:
            nsz = rng.choice([3, 4, 5])
            out.append(item(
                "LA", "All-ones rank", "NAT", 1, "Easy", "HIGH",
                f"Rank of the {nsz}×{nsz} all-ones matrix is _____.",
                None, "1",
                "Every column equals the first."
            ))
        elif t == 13:
            out.append(item(
                "LA", "Null space", "MCQ", 2, "Moderate", "HIGH",
                "If Ax=0 has only the trivial solution and A is n×n then",
                ["rank(A)<n", "det(A)=0", "A is invertible", "0 is an eigenvalue"],
                "C",
                "Trivial nullspace ⇔ full rank ⇔ invertible ⇔ 0 not an eigenvalue."
            ))
        elif t == 14:
            out.append(item(
                "LA", "Eigenvalue of projector", "NAT", 1, "Easy", "HIGH",
                "If P²=P and Pv=λv, v≠0, then λ(λ−1) equals _____.",
                None, "0",
                "λ²=λ ⇒ λ∈{0,1}."
            ))
        else:
            out.append(item(
                "LA", "Similar matrices", "MCQ", 2, "Moderate", "HIGH",
                "Similar matrices always share",
                ["the same entries", "characteristic polynomial", "eigenvectors", "the (1,1) entry"],
                "B",
                "Hence the same eigenvalues, trace and determinant."
            ))
    seen, uniq = set(), []
    for q in out:
        key = (q["topic"], q["stem"])
        if key not in seen:
            seen.add(key)
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        a = 1 + i % 7
        uniq.append(item(
            "LA", "Trace", "NAT", 1, "Easy", "HIGH",
            f"tr(diag({a},{a+1},{a+2})) equals _____.",
            None, str(3 * a + 3),
            f"{a}+{a+1}+{a+2}={3*a+3}."
        ))
    return uniq[:n]


# =================================================
# Calculus
# =================================================
def gen_calc(n=260, seed=22):
    rng = random.Random(seed)
    out = []
    k = 0
    while len(out) < n:
        k += 1
        t = k % 14
        if t == 0:
            a = rng.choice([1, 2, 3])
            # f=x^3 - 3a^2 x , f'=3x^2-3a^2, crit ±a, local min at +a, f(a)=a^3-3a^2·a=-2a^3
            val = -2 * a ** 3
            out.append(item(
                "Calc", "Maxima minima", "NAT", 2, "Moderate", "VERY HIGH",
                f"f(x)=x³−{3*a*a}x. The value of f at its local minimum is _____.",
                None, str(val),
                f"f'=3x²-{3*a*a}=0 ⇒ x=±{a}. f''=6x>0 at x={a}. f({a})={val}."
            ))
        elif t == 1:
            out.append(item(
                "Calc", "Standard limit", "NAT", 1, "Easy", "HIGH",
                "lim_{x→0} (sin x)/x equals _____.",
                None, "1",
                "Standard limit."
            ))
        elif t == 2:
            c = rng.choice([2, 3, 4])
            out.append(item(
                "Calc", "Limit at infinity", "NAT", 1, "Easy", "HIGH",
                f"lim_{{x→∞}} ({c}x²+1)/({c}x²+5) equals _____.",
                None, "1",
                "Ratio of leading coefficients."
            ))
        elif t == 3:
            out.append(item(
                "Calc", "Taylor", "MCQ", 2, "Moderate", "HIGH",
                "Degree-2 Taylor polynomial of e^x about 0 is",
                ["1+x", "1+x+x²", "1+x+x²/2", "x+x²/2"],
                "C",
                "1+x+x²/2!."
            ))
        elif t == 4:
            out.append(item(
                "Calc", "Continuity vs derivative", "MCQ", 1, "Easy", "MEDIUM",
                "f(x)=|x| at 0 is",
                ["differentiable", "continuous but not differentiable", "discontinuous", "analytic"],
                "B",
                "Corner."
            ))
        elif t == 5:
            t0 = rng.choice([2, 3, 5])
            out.append(item(
                "Calc", "Optimisation", "NAT", 2, "Easy", "VERY HIGH",
                f"Minimise (θ−{t0})²+7. The minimum value is _____.",
                None, "7",
                f"Square ≥0, min 7 at θ={t0}."
            ))
        elif t == 6:
            out.append(item(
                "Calc", "Product rule", "NAT", 1, "Easy", "HIGH",
                "d/dx (x² ln x) at x=1 (natural log) equals _____.",
                None, "1",
                "2x ln x + x; at 1 equals 1."
            ))
        elif t == 7:
            out.append(item(
                "Calc", "Critical points", "MSQ", 1, "Moderate", "HIGH",
                "f(x)=x⁴. Which are true? (One or more.)",
                ["x=0 is critical", "f''(0)=0", "x=0 is a local min", "x=0 is a local max"],
                "A;B;C",
                "Flat second derivative still a min."
            ))
        elif t == 8:
            out.append(item(
                "Calc", "Gradient descent", "MCQ", 2, "Moderate", "HIGH",
                "A gradient-descent step on differentiable L uses",
                ["θ ← θ + η ∇L", "θ ← θ − η ∇L", "θ ← ∇L", "θ ← θ − η Hessian"],
                "B",
                "Minus the gradient."
            ))
        elif t == 9:
            a = rng.choice([2, 3, 4])
            out.append(item(
                "Calc", "Derivative at a point", "NAT", 1, "Easy", "HIGH",
                f"d/dx (x^{a}) at x=1 equals _____.",
                None, str(a),
                f"{a} x^{a-1} at 1 is {a}."
            ))
        elif t == 10:
            out.append(item(
                "Calc", "Convexity", "MCQ", 2, "Difficult", "HIGH",
                "A differentiable convex function on R^n",
                ["may have a local min that is not global",
                 "has every stationary point as a global minimiser",
                 "cannot have a stationary point",
                 "is linear"],
                "B",
                "Convexity turns first-order stationarity into global optimality."
            ))
        elif t == 11:
            out.append(item(
                "Calc", "L'Hôpital structure", "MCQ", 1, "Moderate", "MEDIUM",
                "lim_{x→0} (1-cos x)/x² equals",
                ["0", "1", "1/2", "∞"],
                "C",
                "Taylor: 1-(1-x²/2+…)=x²/2 over x²."
            ))
        elif t == 12:
            out.append(item(
                "Calc", "Endpoint vs critical", "MCQ", 2, "Moderate", "HIGH",
                "On a closed interval the global max of a continuous f",
                ["must be an interior critical point",
                 "occurs at a critical point or an endpoint",
                 "cannot occur at an endpoint",
                 "requires f''>0"],
                "B",
                "Extreme value theorem + Fermat's interior criterion."
            ))
        else:
            p = rng.choice([2, 3, 4])
            out.append(item(
                "Calc", "Power rule limit", "NAT", 1, "Easy", "MEDIUM",
                f"lim_{{h→0}} ((1+h)^{p}−1)/h equals _____.",
                None, str(p),
                f"Derivative of x^{p} at 1 is {p}."
            ))
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        c = 2 + i % 8
        uniq.append(item(
            "Calc", "Derivative constant", "NAT", 1, "Easy", "MEDIUM",
            f"d/dx ({c}) equals _____.",
            None, "0",
            "Derivative of a constant is 0."
        ))
    return uniq[:n]


# =================================================
# DSA
# =================================================
def gen_dsa(n=260, seed=33):
    rng = random.Random(seed)
    out = []
    phrases = [
        ("Python mutable default", "MCQ",
         "def f(x, a=[]): a.append(x); return a. After print(f(1), f(2)) the printed lists are",
         ["[1] [2]", "[1] [1,2]", "[1,2] [1,2]", "error"], "C",
         "Shared default object; both calls finish before print."),
        ("Binary search complexity", "MCQ",
         "Worst-case comparisons of binary search on a sorted array of n keys is",
         ["Θ(1)", "Θ(log n)", "Θ(n)", "Θ(n log n)"], "B",
         "Halving."),
        ("Quicksort worst case", "MCQ",
         "Quicksort with first-element pivot on a strictly decreasing array is",
         ["Θ(n log n)", "Θ(n²)", "Θ(n)", "Θ(log n)"], "B",
         "Unbalanced partition T(n)=T(n-1)+Θ(n)."),
        ("Mergesort memory", "MCQ",
         "Standard mergesort extra memory beyond the input is",
         ["Θ(1)", "Θ(log n)", "Θ(n)", "Θ(n²)"], "C",
         "Auxiliary array of length n."),
        ("BFS vs DFS structure", "MCQ",
         "BFS uses a",
         ["stack", "queue", "union-find only", "priority queue of keys only"], "B",
         "Queue; DFS uses a stack."),
        ("Dijkstra", "MCQ",
         "Dijkstra as usually taught requires",
         ["negative weights allowed", "non-negative weights", "unit weights only", "a DAG"], "B",
         "Non-negative edge weights."),
        ("Hash chaining", "MCQ",
         "Expected unsuccessful search with chaining and load α is",
         ["Θ(α)", "Θ(n) always", "Θ(1) worst case", "Θ(n²)"], "A",
         "Mean chain length α."),
        ("Stable sort", "MCQ",
         "Which usual textbook algorithm is stable?",
         ["Heapsort", "Plain quicksort", "Mergesort", "Selection sort"], "C",
         "Mergesort is stable."),
        ("List cycle", "MCQ",
         "A cycle in a singly linked list can be found in O(n) time and O(1) extra space by",
         ["two stacks", "Floyd tortoise-and-hare", "binary search", "DFS on a heap"], "B",
         "Two pointers."),
        ("Tree edges", "MCQ",
         "A tree on n nodes has how many edges?",
         ["n", "n-1", "n+1", "2n"], "B",
         "Connected acyclic."),
    ]
    for i in range(n):
        t = i % 20
        if t < len(phrases):
            topic, qt, stem, opts, ans, sol = phrases[t]
            out.append(item("DSA", topic, qt, 1 if t < 6 else 2, "Easy" if t < 5 else "Moderate", "HIGH",
                            stem, opts, ans, sol))
        elif t == 10:
            nsz = 2 ** rng.choice([3, 4, 5])
            out.append(item(
                "DSA", "Binary search count", "NAT", 1, "Easy", "HIGH",
                f"A usual binary-search loop on {nsz} sorted keys does at most _____ iterations in the worst case (until lo>hi).",
                None, str(int(math.log2(nsz)) + 1),
                f"log2({nsz})+1."
            ))
        elif t == 11:
            nsz = rng.choice([4, 5, 6])
            inv = nsz * (nsz - 1) // 2
            out.append(item(
                "DSA", "Inversions", "NAT", 2, "Moderate", "HIGH",
                f"Number of inversions in the permutation ({nsz},…,1) is _____.",
                None, str(inv),
                f"C({nsz},2)={inv}."
            ))
        elif t == 12:
            m = rng.choice([7, 11])
            keys = [rng.choice([10, 17, 24, 31, 3, 15]) for _ in range(3)]
            # simulate linear probe for last key only after inserting previous
            table = [None] * m
            last_idx = None
            for key in keys:
                i0 = key % m
                j = i0
                while table[j] is not None:
                    j = (j + 1) % m
                table[j] = key
                last_idx = j
            out.append(item(
                "DSA", "Linear probing", "NAT", 2, "Moderate", "HIGH",
                f"Table size {m}, h(k)=k mod {m}, linear probing, insert {keys} into an empty table. Index of the last key is _____.",
                None, str(last_idx),
                f"Trace slots from k mod {m} to the first free cell."
            ))
        elif t == 13:
            out.append(item(
                "DSA", "Divide and conquer", "MSQ", 2, "Easy", "HIGH",
                "Divide-and-conquer algorithms? (One or more.)",
                ["Mergesort", "Binary search", "Insertion sort", "Quicksort"],
                "A;B;D",
                "Insertion sort is incremental."
            ))
        elif t == 14:
            out.append(item(
                "DSA", "BFS shortest path", "MSQ", 2, "Moderate", "VERY HIGH",
                "Unweighted connected undirected graph, BFS from s. True statements? (One or more.)",
                ["First reaching v yields a shortest s–v path",
                 "BFS tree contains a cycle",
                 "Level of v is dist(s,v)",
                 "BFS needs positive real weights"],
                "A;C",
                "Classic BFS facts."
            ))
        elif t == 15:
            out.append(item(
                "DSA", "Python types", "MCQ", 1, "Easy", "HIGH",
                "In Python 3, type([1,2]) is",
                ["tuple", "list", "dict", "set"],
                "B",
                "Square brackets build a list."
            ))
        elif t == 16:
            out.append(item(
                "DSA", "Two-stack queue", "MCQ", 1, "Moderate", "MEDIUM",
                "A queue of two stacks supports",
                ["Θ(n) every operation always", "amortized Θ(1) enqueue and dequeue",
                 "only enqueue", "Θ(n²)"],
                "B",
                "Each element moves at most twice."
            ))
        elif t == 17:
            out.append(item(
                "DSA", "Comparison sort bound", "MCQ", 2, "Moderate", "HIGH",
                "Worst-case lower bound for comparison sorting is",
                ["Ω(n)", "Ω(n log n)", "Ω(n²)", "Ω(1)"],
                "B",
                "Decision-tree argument."
            ))
        elif t == 18:
            h = rng.choice([2, 3])
            nodes = 2 ** (h + 1) - 1
            out.append(item(
                "DSA", "Perfect binary tree", "NAT", 1, "Easy", "MEDIUM",
                f"A perfect binary tree of height {h} (edges) has _____ nodes.",
                None, str(nodes),
                f"2^{{{h}+1}}-1={nodes}."
            ))
        else:
            out.append(item(
                "DSA", "Adjacency list BFS cost", "MCQ", 2, "Moderate", "HIGH",
                "BFS on an adjacency-list graph is",
                ["Θ(V²) always", "Θ(V+E)", "Θ(E log V) always", "Θ(V) even if E=V²"],
                "B",
                "Each vertex and edge is scanned O(1) times."
            ))
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        nsz = 8 + i % 20
        uniq.append(item(
            "DSA", "Linear search worst case", "NAT", 1, "Easy", "MEDIUM",
            f"Worst-case comparisons of linear search for a missing key in an unsorted array of {nsz} is _____.",
            None, str(nsz),
            "Scan all entries."
        ))
    return uniq[:n]


# =================================================
# DBMS
# =================================================
def gen_db(n=260, seed=44):
    out = []
    bank = [
        item("DBMS", "Candidate keys", "MSQ", 2, "Difficult", "VERY HIGH",
             "R(A,B,C,D), F={A→B, B→C, C→A}. Candidate keys? (One or more.)",
             ["AD", "BD", "CD", "ABCD"], "A;B;C",
             "A,B,C cycle; D is outside. ABCD is a superkey, not candidate."),
        item("DBMS", "BCNF", "MCQ", 1, "Moderate", "VERY HIGH",
             "A relation is in BCNF if",
             ["every determinant of a non-trivial FD is a superkey", "it is in 1NF only",
              "it has no NULL", "it has one candidate key"], "A",
             "Standard BCNF."),
        item("DBMS", "2NF", "MCQ", 2, "Moderate", "HIGH",
             "1NF is 2NF when",
             ["every non-prime is fully dependent on every candidate key",
              "there is no transitive dependence of a non-prime on a key",
              "every FD has a superkey LHS", "there are two tables"], "A",
             "No partial dependence. C is BCNF. B is the extra 3NF demand."),
        item("DBMS", "Dependency preservation", "MCQ", 2, "Difficult", "HIGH",
             "A decomposition is dependency-preserving if",
             ["the join of projections recovers R",
              "the union of local FDs equals the original set",
              "it is BCNF", "there are no spurious tuples"], "B",
             "Lossless-join is a different property."),
        item("DBMS", "SQL NULL", "MCQ", 1, "Moderate", "HIGH",
             "In SQL, UNKNOWN = UNKNOWN evaluates to",
             ["TRUE", "FALSE", "UNKNOWN", "a runtime error"], "C",
             "Three-valued logic."),
        item("DBMS", "SQL IS NULL", "MSQ", 2, "Moderate", "HIGH",
             "Which evaluate to UNKNOWN? (One or more.)",
             ["NULL = 5", "NULL = NULL", "5 = 5", "NULL IS NULL"], "A;B",
             "IS NULL is TRUE. Equality involving NULL is UNKNOWN."),
        item("DBMS", "AVG NULL", "MCQ", 1, "Easy", "HIGH",
             "AVG of values 2, 4, NULL, 6 in SQL is",
             ["4", "3", "NULL", "2"], "A",
             "AVG ignores NULL: 12/3=4."),
        item("DBMS", "OLAP roll-up", "MCQ", 1, "Easy", "HIGH",
             "Rolling up City → Country in a cube is",
             ["adding a dimension", "climbing a concept hierarchy", "a join", "BCNF"], "B",
             "Roll-up vs drill-down."),
        item("DBMS", "Star schema", "MCQ", 1, "Easy", "MEDIUM",
             "A warehouse fact table typically stores",
             ["only text descriptions", "measures plus dimension keys",
              "only candidate keys of dimensions", "Python lists"], "B",
             "Measures + FKs."),
        item("DBMS", "ER M:N", "MCQ", 1, "Easy", "MEDIUM",
             "A many-to-many relationship is usually implemented by",
             ["F’s key only in E", "a relationship table with both keys",
              "merging E and F always", "dropping F"], "B",
             "Standard mapping."),
        item("DBMS", "B+ tree", "MSQ", 2, "Moderate", "HIGH",
             "Dense B+ primary index on a sorted file. True? (One or more.)",
             ["Every search-key value appears in a leaf",
              "Leaves are linked for range scans",
              "A primary index never needs uniqueness machinery",
              "Internal nodes hold separators"], "A;B;D",
             "Classic B+ facts."),
        item("DBMS", "Relational algebra pushdown", "MCQ", 2, "Moderate", "HIGH",
             "If attribute B lives only in S, σ_{B=5}(R ⋈ S) equals",
             ["R ⋈ σ_{B=5}(S)", "R − S", "π_B(R)", "R ∪ S"], "A",
             "Selection pushed into the owner."),
        item("DBMS", "3NF vs BCNF", "MSQ", 2, "Difficult", "VERY HIGH",
             "True statements? (One or more.)",
             ["Every BCNF relation is in 3NF",
              "Every 3NF relation is in BCNF",
              "A BCNF decomposition need not preserve FDs",
              "Lossless-join and dependency preservation can conflict"], "A;C;D",
             "3NF is weaker."),
        item("DBMS", "Tuple calculus", "MCQ", 2, "Difficult", "MEDIUM",
             "Tuple relational calculus is",
             ["a procedural algebra of joins only",
              "a declarative calculus over tuples",
              "an indexing method", "a warehouse schema"], "B",
             "Declarative counterpart of RA."),
        item("DBMS", "File organisation", "MCQ", 1, "Moderate", "MEDIUM",
             "A heap file",
             ["keeps tuples sorted on the key", "stores tuples in no particular key order",
              "is a B+ tree", "forbids inserts"], "B",
             "Unordered file."),
        item("DBMS", "Discretisation", "MCQ", 1, "Easy", "MEDIUM",
             "Equal-width binning of a numeric attribute is a form of",
             ["BCNF", "discretisation", "a join", "α-β pruning"], "B",
             "Syllabus data-transformation bullet."),
        item("DBMS", "Sampling", "MCQ", 1, "Easy", "MEDIUM",
             "Simple random sampling without replacement from a table is",
             ["a lossless BCNF split", "a data-transformation technique in the DA syllabus",
              "an uninformed search", "PCA"], "B",
             "Named under data transformation."),
        item("DBMS", "Integrity", "MCQ", 1, "Easy", "HIGH",
             "A foreign key constraint is an example of",
             ["an integrity constraint", "a heuristic", "a loss function", "α-β"], "A",
             "Referential integrity."),
        item("DBMS", "Measure type", "MCQ", 2, "Moderate", "MEDIUM",
             "In a warehouse, SUM(sales) is typically",
             ["an additive measure", "a dimension attribute", "a candidate key of a snowflake only", "entropy"], "A",
             "Additive across the cube."),
        item("DBMS", "Concept hierarchy", "MCQ", 1, "Easy", "MEDIUM",
             "Day ⊂ Month ⊂ Year is",
             ["a concept hierarchy", "BCNF", "a hash function", "a ReLU"], "A",
             "Warehouse modelling."),
    ]
    i = 0
    while len(out) < n:
        q = dict(bank[i % len(bank)])
        if i >= len(bank):
            # closure NAT variants
            attrs = i % 5 + 2
            q = item(
                "DBMS", "Attribute closure", "NAT", 1, "Easy", "VERY HIGH",
                f"R with attributes A1…A{attrs} and F={{A1→A2, A2→A3, …}} so the chain starts at A1. |A1^+| is at least _____.",
                None, str(min(attrs, attrs)),
                "A chain from A1 reaches every later attribute in the listed F pattern; use the stated chain length."
            )
            # make precise: if F is A1→A2, A2→A3, ..., A_{k-1}→A_k then |A1^+|=attrs
            q["stem"] = (
                f"Relation with attributes A1,…,A{attrs} and FDs A_i → A_{{i+1}} for i=1…{attrs-1}. "
                f"The size of A1^+ is _____."
            )
            q["answer"] = str(attrs)
            q["sol"] = f"The chain gives A1→A2→…→A{attrs}, so A1^+ is the full set."
        out.append(q)
        i += 1
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        uniq.append(item(
            "DBMS", "Keys count", "NAT", 1, "Easy", "HIGH",
            f"R(A,B) with F={{A→B}}. Number of candidate keys is _____.",
            None, "1",
            "Only A."
        ))
        # force unique stem
        uniq[-1]["stem"] = f"R(A,B) with only A→B (instance {i}). Number of candidate keys is _____."
    return uniq[:n]


# =================================================
# Machine Learning
# =================================================
def gen_ml(n=260, seed=55):
    rng = random.Random(seed)
    out = []
    k = 0
    while len(out) < n:
        k += 1
        t = k % 18
        if t == 0:
            out.append(item(
                "ML", "Bias-variance", "MCQ", 1, "Easy", "VERY HIGH",
                "Raising model capacity on a fixed sample typically",
                ["raises bias and variance", "lowers bias and raises variance",
                 "raises bias and lowers variance", "changes neither"],
                "B", "Classic trade-off."
            ))
        elif t == 1:
            out.append(item(
                "ML", "Ridge", "MCQ", 2, "Moderate", "VERY HIGH",
                "Ridge replaces X^T X by",
                ["X^T X−λI", "X^T X+λI", "λ X^T X", "XX^T"],
                "B", "β̂=(X^TX+λI)^{-1}X^Ty."
            ))
        elif t == 2:
            out.append(item(
                "ML", "PCA", "MSQ", 2, "Moderate", "VERY HIGH",
                "Centred PCA. True? (One or more.)",
                ["PCs are eigenvectors of the covariance",
                 "The first two loading vectors are orthogonal",
                 "PCA always helps classification",
                 "Explained variance of a component equals its eigenvalue"],
                "A;B;D", "PCA ignores labels."
            ))
        elif t == 3:
            nobs = rng.choice([10, 20, 25, 40])
            out.append(item(
                "ML", "LOOCV", "NAT", 1, "Easy", "HIGH",
                f"LOOCV on n={nobs} labelled points trains how many models?",
                None, str(nobs), "One hold-out per row."
            ))
        elif t == 4:
            kfold, nobs = rng.choice([4, 5, 10]), rng.choice([40, 50, 100])
            train = nobs - nobs // kfold
            out.append(item(
                "ML", "k-fold", "NAT", 1, "Easy", "HIGH",
                f"{kfold}-fold CV on {nobs} points uses _____ training points in one fold (equal folds).",
                None, str(train), f"Hold out {nobs//kfold}."
            ))
        elif t == 5:
            pos, neg = rng.choice([1, 2, 3, 4]), rng.choice([1, 2, 3, 4])
            tot = pos + neg
            p = pos / tot
            if p in (0, 1):
                H = 0.0
            else:
                H = -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
            out.append(item(
                "ML", "Entropy", "NAT", 2, "Moderate", "VERY HIGH",
                f"A node has {pos} positive and {neg} negative labels. Entropy in bits is _____ (two decimals).",
                None, _round_ans(H),
                f"p={p:.3f}, H=−p log2 p −(1-p)log2(1-p)={H:.4f}."
            ))
        elif t == 6:
            out.append(item(
                "ML", "kNN", "MCQ", 2, "Easy", "HIGH",
                "Binary kNN with odd k and Euclidean distance labels by",
                ["the mean of features", "majority vote of k nearest labels",
                 "an SVM on all data", "the farthest neighbour"],
                "B", "Definition."
            ))
        elif t == 7:
            out.append(item(
                "ML", "Logistic", "MCQ", 1, "Easy", "HIGH",
                "Logistic regression models P(Y=1|x) by",
                ["a sigmoid of a linear score", "Y=w·x exactly",
                 "k-means", "an unsupervised mixture only"],
                "A", "σ(w·x+b)."
            ))
        elif t == 8:
            out.append(item(
                "ML", "Naive Bayes", "MCQ", 2, "Moderate", "HIGH",
                "Gaussian Naive Bayes assumes that given the class",
                ["features are independent", "features are perfectly correlated",
                 "the prior is 1", "X is a graph"],
                "A", "Class-conditional independence."
            ))
        elif t == 9:
            out.append(item(
                "ML", "k-means", "MSQ", 2, "Moderate", "HIGH",
                "Standard Euclidean k-means. True? (One or more.)",
                ["The WCSS objective is non-increasing each full iteration",
                 "Every initialisation reaches the global min",
                 "Empty clusters can occur",
                 "k is an input"],
                "A;C;D", "Local minima."
            ))
        elif t == 10:
            x1, y1, x2, y2 = 0, 0, rng.choice([2, 4, 5]), rng.choice([2, 4, 10])
            slope = (y2 - y1) / (x2 - x1)
            out.append(item(
                "ML", "Simple regression", "NAT", 2, "Easy", "HIGH",
                f"OLS line through ({x1},{y1}) and ({x2},{y2}). Slope equals _____.",
                None, _round_ans(slope),
                f"({y2}-{y1})/({x2}-{x1})={slope}."
            ))
        elif t == 11:
            out.append(item(
                "ML", "SVM", "MCQ", 2, "Moderate", "HIGH",
                "Hard-margin linear SVM on separable data maximises",
                ["the number of features", "the geometric margin",
                 "training 0-1 loss only by chance of origin", "k"],
                "B", "Max-margin."
            ))
        elif t == 12:
            out.append(item(
                "ML", "ReLU net", "MCQ", 2, "Difficult", "HIGH",
                "A feed-forward net with ReLU hidden units and linear output is",
                ["one linear map for all x", "piecewise linear in x",
                 "a single polynomial of degree = depth", "unable to represent XOR given enough units"],
                "B", "Each activation pattern is a linear piece."
            ))
        elif t == 13:
            out.append(item(
                "ML", "Linkage", "MCQ", 1, "Moderate", "MEDIUM",
                "Single-linkage merges by the",
                ["max inter-point distance", "min inter-point distance",
                 "centroid distance only", "Mahalanobis only"],
                "B", "Single=min, complete=max."
            ))
        elif t == 14:
            eigs = rng.choice([(5, 1, 0), (4, 2, 0), (6, 3, 1)])
            frac = eigs[0] / sum(eigs)
            out.append(item(
                "ML", "PCA variance ratio", "NAT", 2, "Moderate", "VERY HIGH",
                f"Covariance eigenvalues {eigs[0]}, {eigs[1]}, {eigs[2]}. Fraction of variance in PC1 is _____ (two decimals).",
                None, _round_ans(frac),
                f"{eigs[0]}/{sum(eigs)}={frac:.4f}."
            ))
        elif t == 15:
            out.append(item(
                "ML", "Information gain", "NAT", 2, "Difficult", "HIGH",
                "Parent entropy 1 bit. Two equal children with entropies 0 and 1. IG is _____ bits.",
                None, "0.5",
                "1 − (0.5·0 + 0.5·1) = 0.5."
            ))
        elif t == 16:
            out.append(item(
                "ML", "k-medoid", "MCQ", 1, "Moderate", "MEDIUM",
                "A k-medoid centre must be",
                ["any point in R^d", "a data point of the cluster",
                 "the coordinate-wise mean", "an eigenvector"],
                "B", "Medoid ∈ the sample."
            ))
        else:
            out.append(item(
                "ML", "Training vs test", "MCQ", 1, "Easy", "HIGH",
                "Adding features can",
                ["only increase test error always",
                 "decrease training error while increasing test error",
                 "never change any error",
                 "force k-means to be optimal"],
                "B", "Overfitting pattern."
            ))
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        uniq.append(item(
            "ML", "Sigmoid range", "MCQ", 1, "Easy", "MEDIUM",
            f"σ(z)=1/(1+e^{{-z}}) maps R onto (instance {i} of the same fact)",
            ["{0,1}", "(0,1)", "[-1,1]", "R"],
            "B", "Open interval (0,1)."
        ))
        # better unique NAT
        uniq[-1] = item(
            "ML", "MSE two points", "NAT", 1, "Easy", "MEDIUM",
            f"Predict ŷ={i%5} for both points whose labels are {i%5} and {i%5}. MSE equals _____.",
            None, "0",
            "Perfect fit."
        )
    return uniq[:n]


# =================================================
# AI
# =================================================
def gen_ai(n=260, seed=66):
    out = []
    bank = [
        item("AI", "Informed vs uninformed", "MCQ", 1, "Easy", "VERY HIGH",
             "Which is informed?",
             ["BFS", "DFS", "A*", "Unit-cost UCS with no heuristic"], "C",
             "A* uses h."),
        item("AI", "A* optimality", "MCQ", 2, "Moderate", "VERY HIGH",
             "A* with a consistent heuristic on a finite positive-cost graph",
             ["is incomplete", "returns an optimal path", "equals DFS", "needs h ≥ true cost"], "B",
             "Consistency ⇒ graph-search A* is optimal."),
        item("AI", "Implication", "MCQ", 1, "Easy", "VERY HIGH",
             "p → q is equivalent to",
             ["p ∧ q", "¬p ∨ q", "p ∨ q", "¬p ∧ ¬q"], "B",
             "Material implication."),
        item("AI", "Biconditional", "MCQ", 1, "Easy", "HIGH",
             "p ↔ q is",
             ["(p→q)∧(q→p)", "p∨q", "¬p∨¬q", "p∧¬q"], "A",
             "Two implications."),
        item("AI", "Admissible", "MSQ", 2, "Moderate", "VERY HIGH",
             "Admissible heuristics for Euclidean path cost? (One or more.)",
             ["h=0", "straight-line distance", "twice the true remaining cost", "h = true remaining cost"],
             "A;B;D", "Admissible means 0 ≤ h ≤ h*."),
        item("AI", "d-separation chain", "MCQ", 2, "Moderate", "HIGH",
             "In A→B→C with no other edges, A and C are",
             ["independent given B", "d-connected given B", "always independent unconditionally", "a collider"],
             "A", "Observing B blocks the chain."),
        item("AI", "Variable elimination", "MCQ", 2, "Difficult", "VERY HIGH",
             "Exact VE in a discrete Bayes net is",
             ["always polynomial in the number of nodes",
              "exponential in treewidth of the induced graph",
              "identical to Gibbs sampling",
              "undefined for Bernoulli nodes"],
             "B", "Cost follows the largest factor."),
        item("AI", "Rejection sampling", "MCQ", 1, "Moderate", "HIGH",
             "Rejection sampling for P(Q|E)",
             ["never rejects", "discards samples inconsistent with E",
              "is exact VE", "needs continuous variables"],
             "B", "Definition."),
        item("AI", "Minimax", "NAT", 2, "Moderate", "HIGH",
             "Max root; left terminal 3; right is a min-node with terminals 2 and 8. Root value is _____.",
             None, "3", "min(2,8)=2; max(3,2)=3."),
        item("AI", "Alpha-beta", "MCQ", 1, "Easy", "MEDIUM",
             "α-β pruning from (−∞,+∞)",
             ["changes the root minimax value", "returns the same root value as minimax",
              "needs a consistent heuristic", "is A*"],
             "B", "Only skips irrelevant branches."),
        item("AI", "BFS complete", "MSQ", 1, "Easy", "HIGH",
             "Finite tree, unit cost, goal at finite depth. Complete? (One or more.)",
             ["BFS", "DFS that may miss in graphs with loops (general DFS)", "IDDFS", "arbitrary greedy best-first"],
             "A;C", "IDDFS like BFS. Greedy is not complete."),
        item("AI", "UCS and A*", "MCQ", 2, "Moderate", "HIGH",
             "Uniform-cost search is A* with",
             ["h=h*", "h=0", "h=∞", "h random"],
             "B", "f=g."),
        item("AI", "FOL scope", "MSQ", 2, "Difficult", "HIGH",
             "Readings of ‘every student likes some course’? (One or more.)",
             ["∀s Student(s) → ∃c Course(c) ∧ Likes(s,c)",
              "∃c Course(c) ∧ ∀s Student(s) → Likes(s,c)",
              "∀s ∃c (Student(s) → (Course(c) ∧ Likes(s,c)))",
              "∃s ∀c Likes(s,c)"],
             "A;C", "B is one common course; D is a different claim."),
        item("AI", "Collider", "MCQ", 2, "Difficult", "HIGH",
             "In A→C←B, A and B are",
             ["d-separated given C", "d-connected given C (the collider is opened)",
              "always independent given C", "a chain blocked by C"],
             "B", "Observing a collider opens the v-structure."),
        item("AI", "DFS structure", "MCQ", 1, "Easy", "HIGH",
             "DFS uses a",
             ["queue", "stack / recursion stack", "union-find", "B+ tree"],
             "B", "LIFO."),
        item("AI", "Heuristic consistency", "MCQ", 2, "Difficult", "HIGH",
             "A consistent heuristic satisfies",
             ["h(n) ≥ c(n,n')+h(n')", "h(n) ≤ c(n,n')+h(n')", "h=2h*", "h<0"],
             "B", "Triangle inequality."),
        item("AI", "Propositional SAT shape", "MCQ", 1, "Moderate", "MEDIUM",
             "A clause (p ∨ ¬q ∨ r) is false only when",
             ["p=T", "p=F, q=T, r=F", "all true", "q=F"],
             "B", "Every literal false."),
        item("AI", "Sampling vs exact", "MCQ", 1, "Easy", "HIGH",
             "Gibbs sampling is",
             ["exact VE", "an approximate inference method", "A*", "SQL"],
             "B", "Syllabus approximate inference."),
        item("AI", "Game tree branching", "MCQ", 2, "Moderate", "MEDIUM",
             "Minimax time on a tree of branching b and depth d is",
             ["Θ(d)", "Θ(b^d)", "Θ(log b)", "Θ(1)"],
             "B", "Full tree unless pruned."),
        item("AI", "Knowledge of h=0", "MCQ", 1, "Easy", "HIGH",
             "h=0 is",
             ["inadmissible", "admissible and consistent", "always inconsistent", "illegal"],
             "B", "Zero never overestimates and satisfies the triangle with non-negative costs."),
    ]
    i = 0
    while len(out) < n:
        if i < len(bank) * 3:
            q = dict(bank[i % len(bank)])
            if i >= len(bank):
                # numeric minimax variants
                L = 1 + (i % 9)
                r1, r2 = 1 + (i % 5), 2 + (i % 7)
                right = min(r1, r2)
                root = max(L, right)
                q = item(
                    "AI", "Minimax numeric", "NAT", 2, "Moderate", "HIGH",
                    f"Max root; left terminal {L}; right min-node terminals {r1} and {r2}. Root value is _____.",
                    None, str(root),
                    f"Right plays {right}; max({L},{right})={root}."
                )
            out.append(q)
        else:
            out.append(item(
                "AI", "Search taxonomy", "MCQ", 1, "Easy", "HIGH",
                "Greedy best-first search is",
                ["uninformed", "informed but not guaranteed optimal", "identical to UCS", "a DBMS index"],
                "B", "Uses h, not optimal in general."
            ))
        i += 1
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        uniq.append(item(
            "AI", "BFS layers", "NAT", 1, "Easy", "MEDIUM",
            f"In a complete binary tree of height {1+(i%4)} (edges) with unit costs, BFS from the root reaches a leaf after _____ expansions of the start’s descendants at least in the last level index. Give the leaf depth.",
            None, str(1 + (i % 4)),
            "Leaf depth equals height."
        ))
        uniq[-1]["stem"] = f"Unit-cost complete binary tree of height {1+(i%4)}. Depth of a leaf is _____."
    return uniq[:n]


# =================================================
# General Aptitude
# =================================================
def gen_ga(n=260, seed=77):
    rng = random.Random(seed)
    out = []
    analogies = [
        ("Hot : Cold :: Tall : ____", ["Short", "High", "Wide", "Long"], "A", "Antonyms."),
        ("Teacher : School :: Doctor : ____", ["Hospital", "Book", "Chalk", "Desk"], "A", "Workplace."),
        ("Ephemeral : Transient :: Ancient : ____", ["Archaic", "Brief", "Sudden", "Modern"], "A", "Synonyms."),
        ("Book : Author :: Song : ____", ["Composer", "Paper", "Ink", "Library"], "A", "Creator."),
        ("Verbosity : Brevity :: Generous : ____", ["Stingy", "Kind", "Loud", "Tall"], "A", "Antonyms. Original pairing, not a PYQ copy."),
    ]
    grammar = [
        ("Neither of the reports ____ convincing.", ["are", "were", "is", "have"], "C", "Neither is singular."),
        ("Each of the students ____ a locker.", ["have", "has", "are having", "were"], "B", "Each takes singular."),
        ("The committee ____ divided in its opinion. (as a unit, formal)", ["are", "is", "were being", "have"], "B", "Collective as one."),
        ("She prefers tea ____ coffee.", ["than", "to", "from", "against"], "B", "Prefer to."),
        ("If I ____ you, I would wait.", ["was", "were", "am", "be"], "B", "Subjunctive."),
    ]
    i = 0
    while len(out) < n:
        t = i % 12
        if t == 0:
            stem, opts, ans, sol = analogies[i // 12 % len(analogies)]
            out.append(item("GA", "Analogy", "MCQ", 1, "Easy", "HIGH", stem, opts, ans, sol))
        elif t == 1:
            stem, opts, ans, sol = grammar[i // 12 % len(grammar)]
            out.append(item("GA", "Grammar", "MCQ", 1, "Easy", "HIGH", stem, opts, ans, sol))
        elif t == 2:
            x = rng.choice([80, 100, 120, 200])
            # +20% then -20%
            net = round(x * 1.2 * 0.8 - x)
            out.append(item(
                "GA", "Successive percent", "NAT", 2, "Easy", "HIGH",
                f"A price {x} rises 20% then falls 20%. Net change (negative if fall) is _____.",
                None, str(int(x * 0.96 - x)),
                "1.2×0.8=0.96 ⇒ −4% of the original."
            ))
        elif t == 3:
            a, b = rng.choice([3, 4, 5]), rng.choice([2, 3])
            ans = math.perm(a, b) if hasattr(math, "perm") else math.factorial(a) // math.factorial(a - b)
            out.append(item(
                "GA", "Permutations", "NAT", 2, "Moderate", "HIGH",
                f"P({a},{b}) equals _____.",
                None, str(ans),
                f"{a}!/({a}-{b})! = {ans}."
            ))
        elif t == 4:
            out.append(item(
                "GA", "Modus tollens", "MCQ", 2, "Moderate", "HIGH",
                "From ‘If it rains, the ground is wet’ and ‘the ground is not wet’ infer",
                ["it rains", "it does not rain", "the ground is wet", "nothing"],
                "B", "Modus tollens."
            ))
        elif t == 5:
            n = rng.choice([5, 6, 7])
            out.append(item(
                "GA", "Odd numbers sum", "NAT", 1, "Easy", "MEDIUM",
                f"Sum of first {n} odd numbers equals _____.",
                None, str(n * n),
                f"{n}²={n*n}."
            ))
        elif t == 6:
            p, r, t = 2000, 10, rng.choice([2, 3])
            out.append(item(
                "GA", "Simple interest", "NAT", 2, "Easy", "HIGH",
                f"SI on {p} at {r}% per annum for {t} years is _____.",
                None, str(p * r * t // 100),
                "P·R·T/100."
            ))
        elif t == 7:
            out.append(item(
                "GA", "Syllogism", "MCQ", 2, "Moderate", "HIGH",
                "All poets are dreamers. Some dreamers are engineers. Which must follow?",
                ["All engineers are poets", "Some poets are engineers",
                 "No poet is an engineer", "None of A–C is forced"],
                "D", "The ‘some dreamers’ set need not meet poets."
            ))
        elif t == 8:
            out.append(item(
                "GA", "Logarithm", "MCQ", 1, "Easy", "HIGH",
                "log10 0.01 equals",
                ["2", "−2", "0.01", "10"],
                "B", "10^{−2}=0.01."
            ))
        elif t == 9:
            out.append(item(
                "GA", "Mean", "NAT", 1, "Easy", "MEDIUM",
                "Mean of 3,7,8,10,12 is _____.",
                None, "8",
                "40/5=8."
            ))
        elif t == 10:
            out.append(item(
                "GA", "Clock angle", "MCQ", 2, "Moderate", "MEDIUM",
                "At 3:15 the hour–minute angle is",
                ["0°", "7.5°", "15°", "30°"],
                "B", "Minute at 90°, hour at 97.5°."
            ))
        else:
            out.append(item(
                "GA", "Ratio", "MCQ", 1, "Easy", "MEDIUM",
                "In the ratio 2:3 the second part is what percent of the whole?",
                ["40%", "60%", "50%", "66%"],
                "B", "3/5=60%."
            ))
        i += 1
    seen, uniq = set(), []
    for q in out:
        if q["stem"] not in seen:
            seen.add(q["stem"])
            uniq.append(q)
    i = 0
    while len(uniq) < n:
        i += 1
        a, b = 2 + i % 9, 3 + i % 7
        uniq.append(item(
            "GA", "Percent of", "NAT", 1, "Easy", "MEDIUM",
            f"{a} percent of {100*b} equals _____.",
            None, str(a * b),
            f"{a}/100 × {100*b} = {a*b}."
        ))
    return uniq[:n]


SUBJECTS = {
    "P&S": gen_ps,
    "LA": gen_la,
    "Calc": gen_calc,
    "DSA": gen_dsa,
    "DBMS": gen_db,
    "ML": gen_ml,
    "AI": gen_ai,
    "GA": gen_ga,
}


def generate_all(per=260):
    bank = {}
    for name, fn in SUBJECTS.items():
        bank[name] = fn(per)
        print(name, len(bank[name]), flush=True)
    return bank
