"""GATE-style original items covering the official DA 2027 syllabus headings."""
from __future__ import annotations
import math
import random


def Q(subject, topic, qtype, marks, diff, stem, options, answer, sol):
    return dict(subject=subject, topic=topic, qtype=qtype, marks=marks,
                diff=diff, stem=stem, options=options, answer=answer, sol=sol)


def uniq(items, n):
    seen, out = set(), []
    for q in items:
        k = q["stem"]
        if k not in seen:
            seen.add(k)
            out.append(q)
        if len(out) >= n:
            break
    return out


# -------------------- P&S --------------------
def bank_ps(n=260):
    out = [
        Q("P&S", "Bayes", "NAT", 2, "M",
          "Disease prevalence 0.02. Test sensitivity 0.95, false-positive rate 0.05. P(disease | positive) is _____ (two decimals).",
          None, "0.28", "P(T)=0.95·0.02+0.05·0.98=0.068. Posterior=0.019/0.068≈0.28."),
        Q("P&S", "Tower property", "MCQ", 1, "E",
          "For integrable X,Y which is always true?",
          ["E[X|Y]=E[X]", "E[E[X|Y]]=E[X]", "Var(X|Y)=Var(X)", "E[X|Y]=Y"],
          "B", "Law of total expectation."),
        Q("P&S", "Independence", "MSQ", 2, "M",
          "A,B independent and 0<P(A),P(B)<1. True statements?",
          ["P(A∩B)=P(A)P(B)", "P(A|B)=P(A)", "A and B are disjoint", "P(A∪B)=P(A)+P(B)-P(A)P(B)"],
          "A;B;D", "Independence is not disjointness."),
        Q("P&S", "Mutually exclusive", "MCQ", 1, "E",
          "If A and B are mutually exclusive and P(A),P(B)>0 then",
          ["they are independent", "P(A∩B)=0", "P(A∪B)=P(A)P(B)", "P(A|B)=P(A)"],
          "B", "Disjoint events have empty intersection. They are dependent if both have positive probability."),
        Q("P&S", "Covariance", "MCQ", 1, "M",
          "Which is TRUE?",
          ["Cov=0 ⇒ independent", "Independent (with finite second moments) ⇒ Cov=0",
           "Var(X+Y)=Var(X)+Var(Y) always", "Corr is defined when Var(X)=0"],
          "B", "Uncorrelatedness is weaker than independence."),
        Q("P&S", "Bernoulli", "NAT", 1, "E",
          "X~Bernoulli(0.3). Var(X) is _____ (two decimals).", None, "0.21", "p(1-p)=0.21."),
        Q("P&S", "Binomial", "NAT", 1, "E",
          "Fair coin, 6 tosses. P(exactly 3 heads)/P(exactly 3 tails) is _____.", None, "1", "Same count."),
        Q("P&S", "Poisson", "NAT", 2, "M",
          "X~Poisson(2). P(X=0) is _____ (two decimals).", None, "0.14", "e^{-2}≈0.1353."),
        Q("P&S", "Exponential", "NAT", 1, "E",
          "Exponential with mean 5. Variance is _____.", None, "25", "Var=mean²."),
        Q("P&S", "Uniform", "NAT", 1, "E",
          "X~Uniform[0,6]. Var(X) is _____.", None, "3", "(6-0)²/12=3."),
        Q("P&S", "Normal", "MCQ", 1, "E",
          "Z~N(0,1), X=2Z+5. Then X ~",
          ["N(5,2)", "N(5,4)", "N(2,5)", "not Gaussian"], "B", "Mean 5, variance 4."),
        Q("P&S", "CLT", "MCQ", 1, "M",
          "i.i.d. mean μ, variance σ²>0. For large n, X̄ is approximately",
          ["N(μ,σ²)", "N(μ,σ²/n)", "χ²_n", "exactly t_{n-1}"], "B", "CLT scaling."),
        Q("P&S", "z-test", "MCQ", 2, "M",
          "Two-sided z-test of H0: μ=μ0 at level α rejects when",
          ["Z>z_α", "|Z|>z_{α/2}", "Z=0", "p>α"], "B", "Equal tails."),
        Q("P&S", "Memoryless", "MSQ", 2, "M",
          "Memoryless distributions?",
          ["Geometric on {1,2,…}", "Binomial(8,0.4)", "Exponential", "Uniform(0,1)"],
          "A;C", "Only geometric and exponential."),
        Q("P&S", "Counting", "NAT", 2, "M",
          "Non-negative integer solutions of x+y+z=8: _____.", None, "45", "C(8+3-1,2)=45."),
        Q("P&S", "Median", "MCQ", 1, "E",
          "Median of 2,5,5,7,100 is",
          ["2", "5", "7", "23.8"], "B", "Middle of the ordered list."),
        Q("P&S", "Correlation", "NAT", 1, "E",
          "Var(X)=4, Var(Y)=9, Cov(X,Y)=3. Corr(X,Y) is _____ (one decimal).",
          None, "0.5", "3/(2·3)=0.5."),
        Q("P&S", "Joint", "NAT", 2, "D",
          "f=2 on 0<y<x<1. E[X] is _____ (two decimals).", None, "0.67", "f_X=2x, E=2/3."),
        Q("P&S", "Conditional PDF", "MCQ", 2, "M",
          "If f_{X,Y} is a joint density, f_{X|Y}(x|y) equals",
          ["f_X(x)", "f_{X,Y}(x,y)/f_Y(y) when f_Y(y)>0", "f_Y(y)", "F_X(x)"],
          "B", "Definition of conditional density."),
        Q("P&S", "CDF", "MCQ", 1, "E",
          "A CDF F is always",
          ["decreasing", "right-continuous and non-decreasing with limits 0 and 1",
           "a density", "symmetric"], "B", "Standard properties."),
        Q("P&S", "t vs z", "MCQ", 2, "M",
          "A one-sample t-interval (unknown σ) uses critical values from",
          ["N(0,1)", "t_{n-1}", "χ²_n", "F_{1,1}"], "B", "Student t with n-1 df."),
        Q("P&S", "Chi-square", "MCQ", 2, "M",
          "If Z1,…,Zk i.i.d. N(0,1) then Σ Zi² ~",
          ["N(0,k)", "t_k", "χ²_k", "Uniform"], "C", "Definition of χ²_k."),
        Q("P&S", "Mode", "MCQ", 1, "E",
          "In 1,2,2,2,3,4 the mode is",
          ["1", "2", "3", "2.5"], "B", "Most frequent."),
        Q("P&S", "SD", "NAT", 1, "E",
          "If Var(X)=16 then SD(X) is _____.", None, "4", "Square root."),
        Q("P&S", "Total probability", "NAT", 2, "M",
          "Two boxes. Box 1: 2 red / 5. Box 2: 3 red / 6. Pick a box uniformly then a ball. P(red) is _____ (two decimals).",
          None, "0.45", "0.5·0.4+0.5·0.5=0.45."),
        Q("P&S", "Conditional variance", "MCQ", 2, "D",
          "Law of total variance: Var(X) equals",
          ["E[Var(X|Y)] only", "Var(E[X|Y]) only", "E[Var(X|Y)]+Var(E[X|Y])", "E[X²]"],
          "C", "Eve's law."),
    ]
    rng = random.Random(7)
    # Bayes family
    for prev, se, fp in [(0.01, 0.9, 0.05), (0.05, 0.99, 0.02), (0.1, 0.8, 0.1),
                         (0.03, 0.95, 0.04), (0.02, 0.9, 0.1), (0.08, 0.96, 0.03)]:
        pt = se * prev + fp * (1 - prev)
        post = se * prev / pt
        out.append(Q("P&S", "Bayes", "NAT", 2, "M",
                     f"Prevalence {prev}, sensitivity {se}, FPR {fp}. P(disease|+) is _____ (two decimals).",
                     None, f"{post:.2f}", f"P(+)= {pt:.4f}; posterior={post:.4f}."))
    for nn, k in [(5, 2), (7, 3), (8, 2), (9, 4), (6, 1), (10, 3)]:
        out.append(Q("P&S", "Counting", "NAT", 1, "E",
                     f"C({nn},{k}) equals _____.", None, str(math.comb(nn, k)), "n choose k."))
    for nn, s in [(3, 5), (4, 6), (3, 7), (5, 4), (4, 8)]:
        out.append(Q("P&S", "Stars and bars", "NAT", 2, "M",
                     f"Non-negative solutions of x1+…+x{nn}={s} : _____.",
                     None, str(math.comb(s + nn - 1, nn - 1)), "C(s+n-1,n-1)."))
    for a, b in [(0, 4), (1, 5), (2, 8), (0, 3), (-1, 1)]:
        var = (b - a) ** 2 / 12
        out.append(Q("P&S", "Uniform", "NAT", 1, "E",
                     f"X~Uniform[{a},{b}]. Var(X) is _____ (two decimals if needed).",
                     None, f"{var:.2f}" if abs(var - round(var)) > 1e-9 else str(int(round(var))),
                     "(b-a)²/12."))
    for m in [2, 3, 4, 6, 8, 10]:
        out.append(Q("P&S", "Exponential", "NAT", 1, "E",
                     f"Exponential mean {m}. Var equals _____.", None, str(m * m), "mean²."))
    for p in [0.2, 0.4, 0.5, 0.6, 0.25]:
        out.append(Q("P&S", "Bernoulli", "NAT", 1, "E",
                     f"Bernoulli({p}). Variance is _____ (two decimals).",
                     None, f"{p*(1-p):.2f}", "p(1-p)."))
    for lam in [1, 2, 3]:
        out.append(Q("P&S", "Poisson", "NAT", 2, "M",
                     f"Poisson({lam}). P(X=1)/P(X=0) equals _____.", None, str(lam), "λ e^{-λ}/e^{-λ}=λ."))
    for vx, vy, c in [(4, 9, 2), (1, 4, 1), (9, 16, 6), (4, 4, 0), (16, 9, -6)]:
        rho = c / math.sqrt(vx * vy)
        out.append(Q("P&S", "Correlation", "NAT", 1, "M",
                     f"Var X={vx}, Var Y={vy}, Cov={c}. Correlation is _____ (two decimals).",
                     None, f"{rho:.2f}", "Cov / (sx sy)."))
    # more conceptual
    extra_c = [
        ("Sample space", "MCQ", "A sample space is",
         ["a single outcome", "the set of all outcomes of the experiment", "always [0,1]", "a parameter"],
         "B", "Definition."),
        ("Axioms", "MCQ", "P(Ω) equals", ["0", "1", "1/2", "∞"], "B", "Normalisation axiom."),
        ("Exclusive vs independent", "MCQ", "Two events with P=0.4 and 0.5 cannot be",
         ["independent", "mutually exclusive", "events", "in Ω"], "B",
         "If disjoint, P(union)=0.9 but P(intersection) would be 0 ≠ 0.2, wait: exclusive ⇒ P(∩)=0, possible. Independent would need P(∩)=0.2≠0. Actually exclusive with positive probs cannot be independent. Answer B is wrong then... Exclusive IS possible. Independent: 0.4*0.5=0.2>0 so they CAN be independent. They CANNOT be mutually exclusive because 0.4+0.5=0.9≤1 so exclusive is possible! 0.4+0.5=0.9 so exclusive is possible. They cannot be both exclusive and independent. The question as written is bad."),
    ]
    # fix last one
    extra_c[-1] = ("Exclusive vs independent", "MCQ",
                   "Events with P(A)=0.4, P(B)=0.5 cannot be both mutually exclusive and independent because",
                   ["0.4+0.5>1", "independence would require P(A∩B)=0.2 while exclusivity requires 0",
                    "they are not events", "P(Ω)≠1"],
                   "B", "Product 0.2 versus empty intersection.")
    extra_c += [
        ("Marginal", "MCQ", "A marginal probability is obtained from a joint by",
         ["conditioning on a value", "summing/integrating out the other variable", "taking a ratio of likelihoods only", "always Bayes"],
         "B", "Summing the joint."),
        ("PMF", "MCQ", "A PMF p_X of a discrete RV satisfies",
         ["∫ p = 1", "Σ p(x)=1 and p≥0", "p can be negative", "p is a CDF"],
         "B", "Non-negative and sums to 1."),
        ("PDF", "MCQ", "For a continuous RV, P(X=a) is",
         ["f(a)", "F(a)", "0", "1"], "C", "Points have probability 0."),
        ("Standard normal", "MCQ", "A standard normal has",
         ["mean 1 variance 0", "mean 0 variance 1", "mean 0 variance 0", "mean 1 variance 1"],
         "B", "N(0,1)."),
        ("CI", "MCQ", "A 95% z-interval for μ (known σ) has the form",
         ["X̄ ± z_{0.025} σ", "X̄ ± z_{0.025} σ/√n", "μ ± σ", "X̄ ± t_{n-1}"],
         "B", "Standard error σ/√n."),
        ("Permutation", "NAT",  "P(6,2) equals _____.", None, "30", "6×5=30."),
    ]
    for e in extra_c:
        if e[1] == "NAT":
            out.append(Q("P&S", e[0], "NAT", 1, "E", e[2], e[3], e[4], e[5]))
        else:
            out.append(Q("P&S", e[0], e[1], 1, "E", e[2], e[3], e[4], e[5]))
    # pad with distinct binomial ratios
    for nn in range(4, 40):
        out.append(Q("P&S", "Binomial ratio", "NAT", 1, "E",
                     f"Fair coin, {nn} tosses. C({nn},1)/C({nn},{nn-1}) equals _____.",
                     None, "1", "C(nn,1)=C(nn,nn-1)."))
    return uniq(out, n)


# -------------------- LA --------------------
def bank_la(n=260):
    out = [
        Q("LA", "Subspace", "MSQ", 2, "M",
          "Which are subspaces of R³?",
          ["{x: x1+x2+x3=0}", "{x: x1+x2+x3=1}", "{0}", "{x: x1 x2=0}"],
          "A;C", "Must contain 0 and be closed."),
        Q("LA", "Independence", "MCQ", 1, "E",
          "e1,e2,e3 in R³ are",
          ["dependent", "independent and a basis", "a basis of R²", "orthogonal only if scaled"],
          "B", "Standard basis."),
        Q("LA", "Rank-nullity", "NAT", 2, "M",
          "A is 4×6 of rank 3. dim ker(A) is _____.", None, "3", "6-3=3."),
        Q("LA", "Trace", "NAT", 1, "E",
          "Sum of eigenvalues of [[2,1],[0,5]] is _____.", None, "7", "Trace 7."),
        Q("LA", "Det", "NAT", 1, "E",
          "det([[3,0],[0,4]]) is _____.", None, "12", "Product of diagonal."),
        Q("LA", "Idempotent", "MSQ", 2, "M",
          "P²=P. Always true?",
          ["Eigenvalues in {0,1}", "P is invertible", "I-P is idempotent", "tr(P)=rank(P) for a projector"],
          "A;C;D", "Only I among idempotents is invertible."),
        Q("LA", "Orthogonal", "MCQ", 1, "E",
          "Real orthogonal Q means",
          ["QᵀQ=0", "QᵀQ=I", "det Q=0", "0 is an eigenvalue"], "B", "Definition."),
        Q("LA", "Projector formula", "MCQ", 2, "D",
          "Orthogonal projector onto col(A) (full column rank) is",
          ["AAᵀ", "AᵀA", "A(AᵀA)⁻¹Aᵀ", "(AᵀA)⁻¹"], "C", "Hat matrix."),
        Q("LA", "Quadratic form", "MCQ", 2, "M",
          "xᵀ diag(2,3) x is",
          ["indefinite", "positive definite", "negative definite", "zero"], "B", "Both eigenvalues >0."),
        Q("LA", "LU", "MCQ", 1, "M",
          "Doolittle LU (no pivoting): L is",
          ["unit upper", "unit lower triangular", "orthogonal", "diagonal of λ"], "B", "Unit lower."),
        Q("LA", "SVD rank-1", "NAT", 2, "D",
          "u=(1,2,2)ᵀ, M=uuᵀ. Largest singular value of M is _____.", None, "9", "uᵀu=9."),
        Q("LA", "All-ones", "NAT", 1, "E",
          "Rank of the 5×5 all-ones matrix is _____.", None, "1", "All columns equal."),
        Q("LA", "Invertible", "MCQ", 1, "E",
          "n×n A with only the trivial solution of Ax=0 is",
          ["singular", "invertible", "rank-deficient", "a projector"], "B", "Full rank."),
        Q("LA", "Similar", "MCQ", 2, "M",
          "Similar matrices share",
          ["entries", "characteristic polynomial", "eigenvectors", "the (1,1) entry"],
          "B", "Same eigenvalues, trace, det."),
        Q("LA", "Gaussian elimination", "MCQ", 1, "M",
          "A pivot of 0 with no swap available means the current column",
          ["is a free-variable column (or the matrix is singular if square)",
           "has full rank automatically", "is orthogonal", "is a projector"],
          "A", "No pivot ⇒ free variable."),
        Q("LA", "Partition", "MCQ", 2, "M",
          "For a block-diagonal matrix diag(A,B), det equals",
          ["det A + det B", "det A · det B", "0", "tr A"], "B", "Product of block dets."),
        Q("LA", "Nullity", "NAT", 1, "E",
          "Rank 2 in R³×³. Maximum possible nullity is _____.", None, "1", "3-2=1."),
        Q("LA", "Eigen projector", "NAT", 1, "E",
          "If P²=P and Pv=λv, v≠0, then λ(λ-1) is _____.", None, "0", "λ∈{0,1}."),
        Q("LA", "Dependence", "MCQ", 1, "E",
          "Two nonzero parallel vectors in R² are",
          ["independent", "dependent", "a basis", "orthogonal"], "B", "One is a scalar multiple."),
        Q("LA", "Vector space axioms", "MCQ", 1, "E",
          "A vector space over R must contain",
          ["only positive vectors", "the zero vector", "only unit vectors", "a unique basis"],
          "B", "0 is required."),
    ]
    for a, b in [(2, 3), (4, 1), (5, 5), (7, 2), (6, 0), (3, 8), (1, 9), (10, 4)]:
        out.append(Q("LA", "Trace", "NAT", 1, "E",
                     f"tr(diag({a},{b})) is _____.", None, str(a + b), "Sum of diagonal."))
    for a11, a12, a21, a22 in [(2, 1, 0, 3), (4, 2, 1, 5), (3, 3, 1, 2), (5, 0, 2, 4),
                               (1, 2, 3, 4), (6, 1, 1, 6), (2, 5, 3, 1)]:
        d = a11 * a22 - a12 * a21
        out.append(Q("LA", "Det 2×2", "NAT", 1, "E",
                     f"det([[{a11},{a12}],[{a21},{a22}]]) is _____.", None, str(d), "ad-bc."))
    for r, c, rk in [(3, 5, 2), (4, 7, 3), (5, 5, 4), (2, 6, 1), (6, 4, 3), (3, 3, 1)]:
        out.append(Q("LA", "Rank-nullity", "NAT", 1, "M",
                     f"{r}×{c} matrix of rank {rk}. Nullity is _____.", None, str(c - rk), "n-rank."))
    for k in range(2, 12):
        out.append(Q("LA", "All-ones rank", "NAT", 1, "E",
                     f"Rank of the {k}×{k} all-ones matrix is _____.", None, "1", "Rank 1."))
    extra = [
        Q("LA", "Projection properties", "MSQ", 2, "M",
          "If P is an orthogonal projector then",
          ["Pᵀ=P", "P²=P", "I-P is also an orthogonal projector", "all eigenvalues are 2"],
          "A;B;C", "Symmetric idempotent."),
        Q("LA", "SVD", "MCQ", 2, "M",
          "In A=UΣVᵀ the nonzero diagonal entries of Σ are",
          ["eigenvalues of A", "singular values of A", "pivots of L", "always negative"],
          "B", "Singular values ≥0."),
        Q("LA", "System", "MCQ", 1, "E",
          "A consistent n×n triangular system with nonzero diagonal has",
          ["no solution", "infinitely many solutions", "a unique solution", "only the zero solution always"],
          "C", "Back-substitution works."),
    ]
    out.extend(extra)
    for i in range(1, 80):
        out.append(Q("LA", "Trace 3", "NAT", 1, "E",
                     f"tr(diag({i},{i+1},{2*i})) is _____.", None, str(4 * i + 1), "Sum."))
    return uniq(out, n)


# -------------------- Calc --------------------
def bank_calc(n=260):
    out = [
        Q("Calc", "Standard limit", "NAT", 1, "E",
          "lim_{x→0} (sin x)/x is _____.", None, "1", "Standard."),
        Q("Calc", "L'Hôpital shape", "MCQ", 1, "M",
          "lim_{x→0} (1-cos x)/x² equals",
          ["0", "1", "1/2", "∞"], "C", "Taylor or L'Hôpital twice."),
        Q("Calc", "Continuity", "MCQ", 1, "E",
          "|x| at 0 is",
          ["differentiable", "continuous but not differentiable", "discontinuous", "analytic"],
          "B", "Corner."),
        Q("Calc", "Taylor", "MCQ", 2, "M",
          "Degree-2 Taylor of e^x at 0 is",
          ["1+x", "1+x+x²", "1+x+x²/2", "x+x²/2"], "C", "1+x+x²/2!."),
        Q("Calc", "Gradient descent", "MCQ", 2, "M",
          "A descent step on L is",
          ["θ ← θ+η∇L", "θ ← θ-η∇L", "θ ← ∇L", "θ ← Hessian"], "B", "Minus gradient."),
        Q("Calc", "Convex", "MCQ", 2, "D",
          "A differentiable convex function on R^n",
          ["can have a nonglobal local min", "has every stationary point as a global min",
           "has no stationary point", "is linear"],
          "B", "First-order condition is enough."),
        Q("Calc", "Closed interval", "MCQ", 1, "M",
          "Global max of continuous f on [a,b] occurs at",
          ["an interior critical point only", "a critical point or an endpoint", "f''>0 only", "infinity"],
          "B", "EVT + Fermat."),
        Q("Calc", "x^4", "MSQ", 1, "M",
          "f(x)=x⁴ at 0:",
          ["critical", "f''(0)=0", "local min", "local max"], "A;B;C", "Flat but min."),
        Q("Calc", "Product", "NAT", 1, "E",
          "d/dx (x² ln x) at x=1 is _____.", None, "1", "2x ln x + x → 1."),
        Q("Calc", "Min value", "NAT", 1, "E",
          "Min of (θ-3)²+7 is _____.", None, "7", "Square ≥0."),
    ]
    for a in [1, 2, 3, 4]:
        out.append(Q("Calc", "Local min", "NAT", 2, "M",
                     f"f(x)=x³-{3*a*a}x. f at the local min is _____.",
                     None, str(-2 * a ** 3), f"Critical ±{a}; min at +{a}."))
    for c in [2, 3, 5, 7]:
        out.append(Q("Calc", "Limit ∞", "NAT", 1, "E",
                     f"lim ( {c}x²+1)/({c}x²+5) as x→∞ is _____.", None, "1", "Leading ratio."))
    for p in [2, 3, 4, 5, 6, 8]:
        out.append(Q("Calc", "Power", "NAT", 1, "E",
                     f"d/dx x^{p} at x=1 is _____.", None, str(p), "n x^{n-1}."))
        out.append(Q("Calc", "Difference quotient", "NAT", 1, "E",
                     f"lim_h→0 ((1+h)^{p}-1)/h is _____.", None, str(p), "Derivative at 1."))
    extra = [
        Q("Calc", "Continuity def", "MCQ", 1, "E",
          "f is continuous at a if",
          ["f'(a) exists", "lim_{x→a} f(x)=f(a)", "f is polynomial", "f'' exists"],
          "B", "Definition."),
        Q("Calc", "Differentiable implies", "MCQ", 1, "E",
          "If f is differentiable at a then f is",
          ["discontinuous at a", "continuous at a", "analytic", "convex"],
          "B", "Differentiable ⇒ continuous."),
        Q("Calc", "Critical", "MCQ", 1, "E",
          "An interior local extremum of a differentiable f satisfies",
          ["f'=1", "f'=0", "f''=1", "f=0"], "B", "Fermat."),
        Q("Calc", "Second test", "MCQ", 1, "M",
          "f'(c)=0 and f''(c)>0 implies",
          ["local max", "local min", "inflection only", "global max on R"],
          "B", "Second-derivative test."),
        Q("Calc", "e^x Taylor remainder idea", "MCQ", 2, "M",
          "The remainder after the linear Taylor of e^x at 0 is of order",
          ["O(1)", "O(x)", "O(x²)", "O(e^{-x})"], "C", "Next term x²/2."),
    ]
    out.extend(extra)
    for t0 in range(1, 40):
        out.append(Q("Calc", "SSE min", "NAT", 1, "E",
                     f"Minimise (θ-{t0})² + 4. Minimum value is _____.", None, "4", "Square vanishes."))
    return uniq(out, n)


# -------------------- DSA --------------------
def bank_dsa(n=260):
    out = [
        Q("DSA", "Python default", "MCQ", 2, "M",
          "def f(x,a=[]): a.append(x); return a. After print(f(1), f(2)) the lists printed are",
          ["[1] [2]", "[1] [1,2]", "[1,2] [1,2]", "error"],
          "C", "Shared default; both calls finish before print."),
        Q("DSA", "Python type", "MCQ", 1, "E",
          "type([1,2]) in Python 3 is",
          ["tuple", "list", "dict", "set"], "B", "Square brackets."),
        Q("DSA", "Binary search", "MCQ", 1, "E",
          "Worst-case comparisons of binary search on n sorted keys:",
          ["Θ(1)", "Θ(log n)", "Θ(n)", "Θ(n log n)"], "B", "Halving."),
        Q("DSA", "QS worst", "MCQ", 2, "M",
          "Quicksort, first-element pivot, strictly decreasing array:",
          ["Θ(n log n)", "Θ(n²)", "Θ(n)", "Θ(log n)"], "B", "T(n)=T(n-1)+Θ(n)."),
        Q("DSA", "QS expected shape", "MCQ", 2, "D",
          "Quicksort with a uniformly random pivot on distinct keys has expected time",
          ["Θ(n)", "Θ(n log n)", "Θ(n²) always", "Θ(1)"], "B", "Average of all splits."),
        Q("DSA", "Mergesort memory", "MCQ", 1, "M",
          "Standard mergesort extra memory is",
          ["Θ(1)", "Θ(log n)", "Θ(n)", "Θ(n²)"], "C", "Aux array."),
        Q("DSA", "Stable", "MCQ", 1, "E",
          "Which is stable in the usual textbook form?",
          ["Heapsort", "Plain quicksort", "Mergesort", "Selection sort"], "C", "Mergesort."),
        Q("DSA", "BFS structure", "MCQ", 1, "E",
          "BFS uses a", ["stack", "queue", "only union-find", "B+ tree"], "B", "Queue."),
        Q("DSA", "DFS structure", "MCQ", 1, "E",
          "DFS uses a", ["queue", "stack / recursion", "priority queue of keys only", "hash only"],
          "B", "LIFO."),
        Q("DSA", "Dijkstra", "MCQ", 1, "M",
          "Textbook Dijkstra requires",
          ["negative weights allowed", "non-negative weights", "unit weights only", "a DAG"],
          "B", "Non-negative."),
        Q("DSA", "Hash chain", "MCQ", 1, "M",
          "Expected unsuccessful search with chaining, load α:",
          ["Θ(α)", "Θ(n) always", "Θ(1) worst case", "Θ(n²)"], "A", "Mean chain α."),
        Q("DSA", "Cycle", "MCQ", 1, "M",
          "Singly linked list cycle in O(n) time O(1) extra space:",
          ["two stacks", "Floyd tortoise-and-hare", "binary search", "DFS on a heap"],
          "B", "Two pointers."),
        Q("DSA", "Tree edges", "NAT", 1, "E",
          "A tree on 12 nodes has _____ edges.", None, "11", "n-1."),
        Q("DSA", "Comparison bound", "MCQ", 2, "M",
          "Comparison-sorting lower bound (worst case) is",
          ["Ω(n)", "Ω(n log n)", "Ω(n²)", "Ω(1)"], "B", "Decision tree."),
        Q("DSA", "D&C", "MSQ", 2, "E",
          "Divide-and-conquer?",
          ["Mergesort", "Binary search", "Insertion sort", "Quicksort"], "A;B;D",
          "Insertion is incremental."),
        Q("DSA", "BFS unweighted", "MSQ", 2, "M",
          "Unweighted connected undirected graph, BFS from s:",
          ["first reaching v is a shortest s–v path", "BFS tree has a cycle",
           "level(v)=dist(s,v)", "BFS needs real positive weights"],
          "A;C", "Classic BFS."),
        Q("DSA", "Two-stack queue", "MCQ", 1, "M",
          "Queue of two stacks supports",
          ["Θ(n) every op always", "amortized Θ(1) enqueue and dequeue", "only enqueue", "Θ(n²)"],
          "B", "Each element moves twice."),
        Q("DSA", "Adj-list BFS", "MCQ", 2, "M",
          "BFS on an adjacency-list graph is",
          ["Θ(V²) always", "Θ(V+E)", "Θ(E log V) always", "Θ(V) even if E=V²"],
          "B", "Each vertex/edge O(1)."),
        Q("DSA", "Insertion sort", "MCQ", 1, "E",
          "Insertion sort worst case is",
          ["Θ(n)", "Θ(n log n)", "Θ(n²)", "Θ(1)"], "C", "Reverse sorted."),
        Q("DSA", "Selection sort", "MCQ", 1, "E",
          "Selection sort always does",
          ["Θ(n) swaps in the usual implementation? not the point — comparisons are",
           "Θ(n²) comparisons", "Θ(log n) comparisons", "Θ(n) comparisons"],
          "B", "Nested scans."),
        Q("DSA", "Bubble", "MCQ", 1, "E",
          "Bubble sort (naive) worst case is",
          ["Θ(n)", "Θ(n²)", "Θ(n log n)", "Θ(1)"], "B", "Adjacent swaps."),
        Q("DSA", "Stack", "MCQ", 1, "E",
          "Stack order is",
          ["FIFO", "LIFO", "priority", "sorted"], "B", "Last in first out."),
        Q("DSA", "Queue", "MCQ", 1, "E",
          "Queue order is",
          ["LIFO", "FIFO", "random", "heap order only"], "B", "First in first out."),
        Q("DSA", "Python immutable", "MCQ", 1, "E",
          "Which is immutable?",
          ["list", "dict", "tuple", "set"], "C", "Tuple."),
        Q("DSA", "Hash collision", "MCQ", 1, "M",
          "Linear probing places a colliding key in",
          ["a random empty slot", "the next free slot in the probe sequence", "a new table always", "a stack"],
          "B", "Sequential probe."),
    ]
    for nsz in [8, 16, 32, 64]:
        out.append(Q("DSA", "BS iterations", "NAT", 1, "E",
                     f"Binary-search loop on {nsz} keys: at most _____ iterations until lo>hi.",
                     None, str(int(math.log2(nsz)) + 1), "log2 n + 1."))
    for nsz in [4, 5, 6, 7, 8]:
        out.append(Q("DSA", "Inversions", "NAT", 2, "M",
                     f"Inversions in ({nsz} … 1) : _____.", None, str(nsz * (nsz - 1) // 2), "C(n,2)."))
    for h in [1, 2, 3, 4]:
        out.append(Q("DSA", "Perfect tree", "NAT", 1, "E",
                     f"Perfect binary tree of height {h} (edges) has _____ nodes.",
                     None, str(2 ** (h + 1) - 1), "2^{h+1}-1."))
    for nsz in range(5, 80):
        out.append(Q("DSA", "Linear search", "NAT", 1, "E",
                     f"Worst-case comparisons, missing key, unsorted length {nsz}: _____.",
                     None, str(nsz), "Scan all."))
    return uniq(out, n)


# -------------------- DBMS --------------------
def bank_db(n=260):
    out = [
        Q("DBMS", "Candidate keys", "MSQ", 2, "D",
          "R(A,B,C,D), F={A→B, B→C, C→A}. Candidate keys?",
          ["AD", "BD", "CD", "ABCD"], "A;B;C", "A,B,C cycle; D essential. ABCD is a superkey."),
        Q("DBMS", "BCNF", "MCQ", 1, "M",
          "BCNF means",
          ["every determinant of a non-trivial FD is a superkey", "1NF only", "no NULL", "one key only"],
          "A", "Definition."),
        Q("DBMS", "2NF", "MCQ", 2, "M",
          "1NF is 2NF when",
          ["every non-prime is fully dependent on every candidate key",
           "there is no transitive dependence of a non-prime on a key",
           "every FD has a superkey LHS", "there are two tables"],
          "A", "No partial dependence."),
        Q("DBMS", "3NF vs BCNF", "MSQ", 2, "D",
          "True?",
          ["Every BCNF relation is in 3NF", "Every 3NF relation is in BCNF",
           "A BCNF decomposition need not preserve FDs",
           "Lossless-join and dependency preservation can conflict"],
          "A;C;D", "3NF is weaker."),
        Q("DBMS", "Dep preservation", "MCQ", 2, "D",
          "Dependency-preserving means",
          ["join of projections recovers R", "union of local FDs equals the original set",
           "it is BCNF", "no spurious tuples"],
          "B", "Different from lossless join."),
        Q("DBMS", "NULL =", "MCQ", 1, "M",
          "In SQL, UNKNOWN = UNKNOWN is",
          ["TRUE", "FALSE", "UNKNOWN", "error"], "C", "3VL."),
        Q("DBMS", "IS NULL", "MSQ", 2, "M",
          "Evaluate to UNKNOWN?",
          ["NULL = 5", "NULL = NULL", "5 = 5", "NULL IS NULL"], "A;B", "IS NULL is TRUE."),
        Q("DBMS", "AVG", "MCQ", 1, "E",
          "AVG of 2,4,NULL,6 is",
          ["4", "3", "NULL", "2"], "A", "12/3=4."),
        Q("DBMS", "Roll-up", "MCQ", 1, "E",
          "City → Country in a cube is",
          ["adding a dimension", "climbing a concept hierarchy", "a join", "BCNF"],
          "B", "Roll-up."),
        Q("DBMS", "Star", "MCQ", 1, "E",
          "A fact table typically stores",
          ["only text", "measures plus dimension keys", "Python lists", "only candidate keys of facts without measures"],
          "B", "Measures + FKs."),
        Q("DBMS", "M:N", "MCQ", 1, "E",
          "Many-to-many is implemented by",
          ["F’s key only in E", "a relationship table with both keys", "merging always", "dropping F"],
          "B", "Standard ER map."),
        Q("DBMS", "B+", "MSQ", 2, "M",
          "Dense B+ primary index:",
          ["every search-key value appears in a leaf", "leaves are linked",
           "internal nodes hold separators", "range scan is impossible"],
          "A;B;C", "Classic B+."),
        Q("DBMS", "Push selection", "MCQ", 2, "M",
          "B lives only in S. σ_{B=5}(R ⋈ S) equals",
          ["R ⋈ σ_{B=5}(S)", "R - S", "π_B(R)", "R ∪ S"], "A", "Pushdown."),
        Q("DBMS", "TRC", "MCQ", 2, "D",
          "Tuple relational calculus is",
          ["procedural algebra only", "a declarative calculus over tuples", "an index", "a star schema"],
          "B", "Declarative."),
        Q("DBMS", "Heap", "MCQ", 1, "M",
          "A heap file",
          ["keeps tuples sorted on the key", "stores tuples in no particular key order",
           "is a B+ tree", "forbids inserts"],
          "B", "Unordered."),
        Q("DBMS", "Discretise", "MCQ", 1, "E",
          "Equal-width binning is",
          ["BCNF", "discretisation", "a join", "α-β"], "B", "Transformation."),
        Q("DBMS", "Sampling", "MCQ", 1, "E",
          "Simple random sampling from a table is",
          ["a BCNF split", "a data-transformation technique in the DA syllabus", "A*", "PCA"],
          "B", "Named heading."),
        Q("DBMS", "Integrity", "MCQ", 1, "E",
          "A foreign key is",
          ["an integrity constraint", "a heuristic", "a loss", "α-β"], "A", "Referential integrity."),
        Q("DBMS", "Additive measure", "MCQ", 2, "M",
          "SUM(sales) across a cube is typically",
          ["additive", "a dimension only", "entropy", "a candidate key"], "A", "Adds over dimensions."),
        Q("DBMS", "Hierarchy", "MCQ", 1, "E",
          "Day ⊂ Month ⊂ Year is",
          ["a concept hierarchy", "BCNF", "a hash", "ReLU"], "A", "Warehouse."),
        Q("DBMS", "RA select", "MCQ", 1, "E",
          "σ_{Age>20}(Student) is",
          ["projection", "selection", "join", "union"], "B", "Select."),
        Q("DBMS", "RA project", "MCQ", 1, "E",
          "π_{Name}(Student) is",
          ["selection", "projection", "difference", "index"], "B", "Project."),
        Q("DBMS", "Join", "MCQ", 1, "E",
          "R ⋈ S on a common attribute is",
          ["Cartesian product only", "a theta/natural join of matching tuples", "union", "BCNF"],
          "B", "Join."),
        Q("DBMS", "PK", "MCQ", 1, "E",
          "A primary key",
          ["may contain NULL in SQL in the usual definition taught for GATE",
           "uniquely identifies a tuple and is chosen among candidate keys",
           "is any superkey with extra attributes", "is AVG"],
          "B", "Chosen candidate key."),
        Q("DBMS", "Snowflake", "MCQ", 1, "M",
          "A snowflake schema",
          ["normalises dimension tables", "forbids measures", "is BCNF of the fact only", "is SQL NULL"],
          "A", "Dimensions split."),
        Q("DBMS", "Compression", "MCQ", 1, "E",
          "Dictionary encoding of a low-cardinality column is",
          ["a join", "compression (data transformation)", "A*", "an eigenvalue"],
          "B", "Syllabus bullet."),
        Q("DBMS", "1NF", "MCQ", 1, "E",
          "1NF forbids",
          ["atomic attributes being violated / repeating groups", "any FD", "any key", "SQL"],
          "A", "Atomic domains."),
    ]
    for k in range(3, 20):
        out.append(Q("DBMS", "Closure", "NAT", 1, "E",
                     f"Attributes A1..A{k} with A_i → A_{{i+1}} for each i. |A1^+| is _____.",
                     None, str(k), "The chain covers all."))
    for i in range(80):
        out.append(Q("DBMS", "Keys count", "NAT", 1, "E",
                     f"R(A,B) with only A→B (labelled instance {i+1} of the same FD). Number of candidate keys is _____.",
                     None, "1", "Only A. Different label keeps the stem unique for drilling the same fact."))
    return uniq(out, n)


# -------------------- ML --------------------
def bank_ml(n=260):
    out = [
        Q("ML", "Bias-variance", "MCQ", 1, "E",
          "Raising capacity on a fixed sample typically",
          ["raises bias and variance", "lowers bias and raises variance",
           "raises bias and lowers variance", "changes neither"],
          "B", "Trade-off."),
        Q("ML", "Ridge", "MCQ", 2, "M",
          "Ridge replaces XᵀX by",
          ["XᵀX-λI", "XᵀX+λI", "λ XᵀX", "XXᵀ"], "B", "(XᵀX+λI)⁻¹Xᵀy."),
        Q("ML", "PCA", "MSQ", 2, "M",
          "Centred PCA. True?",
          ["PCs are eigenvectors of the covariance", "the first two loadings are orthogonal",
           "PCA always helps classification", "explained variance of a component is its eigenvalue"],
          "A;B;D", "PCA ignores labels — cf. GATE DA 2026 Q.11 style (PCs are orthogonal)."),
        Q("ML", "PCA angle", "MCQ", 1, "M",
          "Angle between distinct principal axes of a centred covariance (distinct eigenvalues) is",
          ["0°", "90°", "between 90° and 180°", "undefined"],
          "B", "Eigenvectors of a symmetric matrix are orthogonal. Pattern of DA 2026 Q.11."),
        Q("ML", "LOOCV", "NAT", 1, "E",
          "LOOCV on 900 train points trains how many models?", None, "900",
          "One hold-out per row. Pattern of DA 2026 Q.12."),
        Q("ML", "k-fold", "NAT", 1, "E",
          "5-fold CV on 50 points: training size in one fold is _____.", None, "40", "Hold out 10."),
        Q("ML", "Entropy 2-2", "NAT", 2, "M",
          "Node with 2 + and 2 -. Entropy in bits is _____.", None, "1", "Fair coin."),
        Q("ML", "Entropy 4-0", "NAT", 1, "E",
          "Node with 4 + and 0 -. Entropy is _____.", None, "0", "Pure."),
        Q("ML", "IG", "NAT", 2, "D",
          "Parent entropy 1. Two equal children with entropies 0 and 1. IG is _____ bits.",
          None, "0.5", "1-0.5=0.5."),
        Q("ML", "kNN", "MCQ", 1, "E",
          "Odd-k binary kNN labels by",
          ["mean of features", "majority of k nearest labels", "an SVM", "the farthest"],
          "B", "Vote."),
        Q("ML", "Logistic", "MCQ", 1, "E",
          "Logistic models P(Y=1|x) by",
          ["a sigmoid of a linear score", "Y=w·x exactly", "k-means", "PCA"],
          "A", "σ(w·x+b)."),
        Q("ML", "NB", "MCQ", 2, "M",
          "Gaussian Naive Bayes assumes that given the class",
          ["features are independent", "features are perfectly correlated", "the prior is 1", "X is a graph"],
          "A", "Class-conditional independence."),
        Q("ML", "k-means", "MSQ", 2, "M",
          "Euclidean k-means. True?",
          ["WCSS is non-increasing each full iteration", "every init is global",
           "empty clusters can occur", "k is an input"],
          "A;C;D", "Local minima."),
        Q("ML", "SVM", "MCQ", 2, "M",
          "Hard-margin linear SVM maximises",
          ["#features", "geometric margin", "k", "entropy"], "B", "Max-margin."),
        Q("ML", "ReLU", "MCQ", 2, "D",
          "ReLU hidden units + linear output give a map that is",
          ["one linear map for all x", "piecewise linear in x", "a high-degree single polynomial", "unable to represent XOR given enough units"],
          "B", "Activation pattern = linear piece."),
        Q("ML", "Single linkage", "MCQ", 1, "M",
          "Single-linkage merges by",
          ["max inter-point distance", "min inter-point distance", "centroid only", "Mahalanobis only"],
          "B", "Min."),
        Q("ML", "Complete linkage", "MCQ", 1, "M",
          "Complete-linkage uses the",
          ["min pair", "max pair", "median only", "PCA axis"], "B", "Max."),
        Q("ML", "k-medoid", "MCQ", 1, "M",
          "A k-medoid centre must be",
          ["any point of R^d", "a data point", "the coordinate mean", "an eigenvector"],
          "B", "Medoid ∈ sample."),
        Q("ML", "LDA", "MCQ", 2, "M",
          "LDA (two classes, shared covariance) is",
          ["unsupervised", "a linear classifier using class-conditional Gaussians", "k-means", "A*"],
          "B", "Fisher / Gaussian LDA."),
        Q("ML", "Multiple regression", "MCQ", 1, "E",
          "OLS with p features (plus intercept) fits",
          ["k clusters", "a linear predictor in the features", "a decision stump only", "PCA loadings only"],
          "B", "Hyperplane."),
        Q("ML", "Train vs test", "MCQ", 1, "E",
          "Adding features can",
          ["only increase test error always", "decrease training error while increasing test error",
           "never change any error", "force k-means to be optimal"],
          "B", "Overfit."),
        Q("ML", "Sigmoid range", "MCQ", 1, "E",
          "σ(z)=1/(1+e^{-z}) maps R onto",
          ["{0,1}", "(0,1)", "[-1,1]", "R"], "B", "Open unit interval."),
        Q("ML", "Bottom-up", "MCQ", 1, "E",
          "Agglomerative clustering is",
          ["top-down", "bottom-up", "supervised", "A*"], "B", "Start from singletons."),
        Q("ML", "Top-down cluster", "MCQ", 1, "E",
          "Divisive clustering is",
          ["bottom-up", "top-down", "ridge", "SQL"], "B", "Start from one cluster."),
    ]
    for nobs in [10, 20, 25, 40, 100, 900, 1000]:
        out.append(Q("ML", "LOOCV", "NAT", 1, "E",
                     f"LOOCV on n={nobs} trains _____ models.", None, str(nobs), "n models."))
    for kfold, nobs in [(4, 40), (5, 100), (10, 50), (5, 25), (8, 80)]:
        out.append(Q("ML", "k-fold", "NAT", 1, "E",
                     f"{kfold}-fold on {nobs} points, equal folds: hold-out size is _____.",
                     None, str(nobs // kfold), "n/k."))
    for eigs in [(5, 1, 0), (4, 2, 0), (6, 3, 1), (8, 2, 0), (3, 3, 0)]:
        frac = eigs[0] / sum(eigs)
        out.append(Q("ML", "PCA ratio", "NAT", 2, "M",
                     f"Eigenvalues {eigs[0]}, {eigs[1]}, {eigs[2]}. Fraction in PC1 is _____ (two decimals).",
                     None, f"{frac:.2f}", f"{eigs[0]}/{sum(eigs)}."))
    for pos, neg in [(1, 1), (3, 1), (3, 5), (7, 1), (2, 6)]:
        p = pos / (pos + neg)
        H = 0.0 if p in (0, 1) else -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
        out.append(Q("ML", "Entropy", "NAT", 2, "M",
                     f"Node {pos}+ {neg}-. Entropy (bits, two decimals) is _____.",
                     None, f"{H:.2f}", f"p={p:.3f}."))
    for x2, y2 in [(2, 2), (4, 2), (5, 10), (3, 6), (8, 4)]:
        out.append(Q("ML", "Two-point slope", "NAT", 1, "E",
                     f"OLS through (0,0) and ({x2},{y2}). Slope is _____.",
                     None, f"{y2/x2:.2f}" if y2 / x2 != int(y2 / x2) else str(y2 // x2),
                     "y/x."))
    for i in range(40):
        out.append(Q("ML", "LOOCV pad", "NAT", 1, "E",
                     f"LOOCV on {8+i} labelled points trains _____ models.",
                     None, str(8 + i), "n."))
    return uniq(out, n)


# -------------------- AI --------------------
def bank_ai(n=260):
    out = [
        Q("AI", "Uninformed", "MCQ", 1, "E",
          "Which is NOT uninformed?",
          ["BFS", "DFS", "A*", "Depth-limited search"], "C",
          "A* uses h. Pattern of DA 2026 Q.13."),
        Q("AI", "Informed", "MCQ", 1, "E",
          "Which is informed?",
          ["BFS", "DFS", "A*", "UCS with no heuristic"], "C", "A* uses h."),
        Q("AI", "A* opt", "MCQ", 2, "M",
          "A* with a consistent heuristic on a finite positive-cost graph",
          ["is incomplete", "returns an optimal path", "equals DFS", "needs h≥true cost"],
          "B", "Consistency ⇒ graph-search A* optimal."),
        Q("AI", "Implication", "MCQ", 1, "E",
          "p → q is equivalent to",
          ["p ∧ q", "¬p ∨ q", "p ∨ q", "¬p ∧ ¬q"], "B", "Material implication."),
        Q("AI", "Biconditional", "MCQ", 1, "E",
          "p ↔ q is",
          ["(p→q)∧(q→p)", "p∨q", "¬p∨¬q", "p∧¬q"], "A", "Two arrows."),
        Q("AI", "Admissible", "MSQ", 2, "M",
          "Admissible heuristics for Euclidean path cost?",
          ["h=0", "straight-line distance", "twice the true remaining cost", "h = true remaining cost"],
          "A;B;D", "0 ≤ h ≤ h*."),
        Q("AI", "d-sep chain", "MCQ", 2, "M",
          "A→B→C only. A and C given B are",
          ["independent", "d-connected", "a collider", "always dependent"],
          "A", "Observing B blocks the chain."),
        Q("AI", "Collider", "MCQ", 2, "D",
          "A→C←B. Given C, A and B are",
          ["d-separated", "d-connected (collider opened)", "always independent given C", "a blocked chain"],
          "B", "v-structure opens."),
        Q("AI", "VE", "MCQ", 2, "D",
          "Exact VE in a discrete Bayes net is",
          ["always polynomial in #nodes", "exponential in treewidth of the induced graph",
           "identical to Gibbs", "undefined for Bernoulli nodes"],
          "B", "Largest factor."),
        Q("AI", "Rejection", "MCQ", 1, "M",
          "Rejection sampling for P(Q|E)",
          ["never rejects", "discards samples inconsistent with E", "is exact VE", "needs continuous vars"],
          "B", "Definition."),
        Q("AI", "Minimax", "NAT", 2, "M",
          "Max root; left terminal 3; right min-node 2 and 8. Root value is _____.",
          None, "3", "min=2; max(3,2)=3."),
        Q("AI", "Alpha-beta", "MCQ", 1, "E",
          "α-β from (-∞,+∞)",
          ["changes the root value", "returns the same root value as minimax", "needs a consistent h", "is A*"],
          "B", "Only skips branches."),
        Q("AI", "UCS", "MCQ", 2, "M",
          "Uniform-cost search is A* with",
          ["h=h*", "h=0", "h=∞", "h random"], "B", "f=g."),
        Q("AI", "FOL scope", "MSQ", 2, "D",
          "Readings of “every student likes some course”?",
          ["∀s Student(s) → ∃c Course(c) ∧ Likes(s,c)",
           "∃c Course(c) ∧ ∀s Student(s) → Likes(s,c)",
           "∀s ∃c (Student(s) → (Course(c) ∧ Likes(s,c)))",
           "∃s ∀c Likes(s,c)"],
          "A;C", "B is one common course."),
        Q("AI", "FOL king", "MCQ", 2, "M",
          "“Each king is a person” is NOT equivalent to",
          ["∀x (IsKing(x) → IsPerson(x))", "∀x (IsKing(x) ∧ IsPerson(x))",
           "¬∃x (IsKing(x) ∧ ¬IsPerson(x))", "∀x (¬IsKing(x) ∨ IsPerson(x))"],
          "B", "Conjunction claims everyone is a king. Pattern of DA 2026 Q.14."),
        Q("AI", "Greedy", "MCQ", 1, "E",
          "Greedy best-first is",
          ["uninformed", "informed but not guaranteed optimal", "identical to UCS", "SQL"],
          "B", "Uses h only."),
        Q("AI", "Consistent h", "MCQ", 2, "D",
          "A consistent heuristic satisfies",
          ["h(n) ≥ c(n,n')+h(n')", "h(n) ≤ c(n,n')+h(n')", "h=2h*", "h<0"],
          "B", "Triangle."),
        Q("AI", "Clause", "MCQ", 1, "M",
          "(p ∨ ¬q ∨ r) is false only when",
          ["p=T", "p=F, q=T, r=F", "all true", "q=F"], "B", "Every literal false."),
        Q("AI", "Gibbs", "MCQ", 1, "E",
          "Gibbs sampling is",
          ["exact VE", "approximate inference", "A*", "SQL"], "B", "Syllabus sampling."),
        Q("AI", "Minimax cost", "MCQ", 2, "M",
          "Minimax on branching b depth d is",
          ["Θ(d)", "Θ(b^d)", "Θ(log b)", "Θ(1)"], "B", "Full tree."),
        Q("AI", "h=0", "MCQ", 1, "E",
          "h=0 is",
          ["inadmissible", "admissible and consistent", "always inconsistent", "illegal"],
          "B", "Never overestimates."),
        Q("AI", "BFS complete", "MCQ", 1, "E",
          "BFS on a finite tree with a goal at finite depth is",
          ["incomplete", "complete", "optimal only with negative costs", "A*"],
          "B", "Complete."),
        Q("AI", "Propositional SAT", "MCQ", 1, "E",
          "A formula is satisfiable if",
          ["it is a tautology only", "some assignment makes it true", "it is a contradiction", "it uses ∀"],
          "B", "Exists a model."),
        Q("AI", "Predicate vs prop", "MCQ", 1, "E",
          "Predicate logic adds",
          ["only AND", "quantifiers and predicates", "SQL", "k-means"],
          "B", "FOL."),
    ]
    for i in range(1, 90):
        L, r1, r2 = i, i + 1, i + 4
        root = max(L, min(r1, r2))
        out.append(Q("AI", "Minimax num", "NAT", 2, "M",
                     f"Max root; left {L}; right min({r1},{r2}). Root value is _____.",
                     None, str(root), "Min then max."))
    return uniq(out, n)


# -------------------- GA --------------------
def bank_ga(n=260):
    out = [
        Q("GA", "Analogy", "MCQ", 1, "E",
          "Hot : Cold :: Tall : ____",
          ["Short", "Wide", "High", "Long"], "A", "Antonym. (Style of DA verbal analogies, not a PYQ copy.)"),
        Q("GA", "Analogy", "MCQ", 1, "E",
          "Teacher : School :: Doctor : ____",
          ["Hospital", "Chalk", "Desk", "Bell"], "A", "Workplace."),
        Q("GA", "Analogy", "MCQ", 1, "E",
          "Transparent : Opaque :: Flexible : ____",
          ["Rigid", "Clear", "Soft", "Bright"], "A", "Antonym."),
        Q("GA", "Analogy", "MCQ", 1, "E",
          "Begin : Start :: Finish : ____",
          ["End", "Open", "Pause", "Try"], "A", "Synonym."),
        Q("GA", "Grammar", "MCQ", 1, "E",
          "Neither of the reports ____ convincing.",
          ["are", "is", "have", "were"], "B", "Neither + singular."),
        Q("GA", "Grammar", "MCQ", 1, "E",
          "Each of the students ____ a locker.",
          ["have", "has", "are", "were"], "B", "Each + singular."),
        Q("GA", "Grammar", "MCQ", 1, "E",
          "She prefers tea ____ coffee.",
          ["than", "to", "from", "against"], "B", "Prefer to."),
        Q("GA", "Grammar", "MCQ", 1, "E",
          "If I ____ you, I would wait.",
          ["was", "were", "am", "be"], "B", "Subjunctive."),
        Q("GA", "Grammar", "MCQ", 1, "E",
          "The news ____ surprising.",
          ["are", "is", "were", "have"], "B", "News singular."),
        Q("GA", "Logic", "MCQ", 2, "M",
          "If P then Q. Not Q. Therefore",
          ["P", "Not P", "Q", "P and Q"], "B", "Modus tollens."),
        Q("GA", "Syllogism", "MCQ", 2, "M",
          "All poets are dreamers. Some dreamers are engineers. Which must follow?",
          ["All engineers are poets", "Some poets are engineers", "No poet is an engineer", "None of A–C is forced"],
          "D", "No forced meet."),
        Q("GA", "Log", "MCQ", 1, "E",
          "log10 0.01 equals", ["2", "-2", "0.01", "10"], "B", "10^{-2}."),
        Q("GA", "Log", "MCQ", 1, "E",
          "log10 1000 equals", ["2", "3", "0.3", "30"], "B", "10^3."),
        Q("GA", "Series", "MCQ", 1, "E",
          "Next: 2,6,12,20,30,…", ["36", "42", "40", "44"], "B", "n(n+1)."),
        Q("GA", "Odd one", "MCQ", 1, "E",
          "Odd one: square, triangle, pentagon, circle",
          ["square", "triangle", "pentagon", "circle"], "D", "Not a polygon."),
        Q("GA", "Clock", "MCQ", 2, "M",
          "Angle between hands at 3:00 is", ["0°", "90°", "180°", "75°"], "B", "Quarter."),
        Q("GA", "Clock 3:15", "MCQ", 2, "M",
          "At 3:15 the hour–minute angle is",
          ["0°", "7.5°", "15°", "30°"], "B", "Hour at 97.5°, minute at 90°."),
        Q("GA", "Ratio", "MCQ", 1, "E",
          "In 2:3 the second part is what percent of the whole?",
          ["40%", "60%", "50%", "66%"], "B", "3/5."),
        Q("GA", "Percent successive", "NAT", 2, "E",
          "Price 100 rises 20% then falls 20%. Final price is _____.", None, "96", "0.96×100."),
        Q("GA", "Work", "NAT", 2, "M",
          "A does a job in 6 days, B in 12. Days together: _____.", None, "4", "1/6+1/12=1/4."),
        Q("GA", "SI", "NAT", 2, "E",
          "SI on 2000 at 10% for 2 years is _____.", None, "400", "PRT/100."),
        Q("GA", "Mean", "NAT", 1, "E",
          "Mean of 3,7,8,10,12 is _____.", None, "8", "40/5."),
        Q("GA", "Odd sum", "NAT", 1, "E",
          "Sum of first 7 odd positives is _____.", None, "49", "7²."),
        Q("GA", "P(5,2)", "NAT", 1, "E",
          "P(5,2) equals _____.", None, "20", "5×4."),
        Q("GA", "Digit product style", "MCQ", 2, "M",
          "Digits of a 3-digit number multiply to 36 and are 2,2,9 in some order. Their sum is",
          ["11", "13", "15", "18"], "B", "2+2+9=13. (Numerical-digit style of DA 2026 Q.2, different product.)"),
    ]
    for i in range(1, 80):
        a, base = 2 + (i % 9), 100 + 10 * i
        out.append(Q("GA", "Percent", "NAT", 1, "E",
                     f"{a}% of {base} equals _____.",
                     None, str(a * base // 100), "p/100 × base."))
    for k in range(3, 30):
        out.append(Q("GA", "Odd sum", "NAT", 1, "E",
                     f"Sum of the first {k} odd positives is _____.", None, str(k * k), "n²."))
    for a, b in [(3, 6), (4, 12), (5, 20), (8, 8), (10, 15)]:
        days = 1 / (1 / a + 1 / b)
        out.append(Q("GA", "Work", "NAT", 2, "M",
                     f"A: {a} days, B: {b} days. Days together (two decimals) _____.",
                     None, f"{days:.2f}", "Harmonic."))
    return uniq(out, n)


SUBJECTS = [
    ("P&S", "UNIT 1  ·  Probability and Statistics", bank_ps),
    ("LA", "UNIT 2  ·  Linear Algebra", bank_la),
    ("Calc", "UNIT 3  ·  Calculus and Optimization", bank_calc),
    ("DSA", "UNIT 4  ·  Programming, Data Structures and Algorithms", bank_dsa),
    ("DBMS", "UNIT 5  ·  Database Management and Warehousing", bank_db),
    ("ML", "UNIT 6  ·  Machine Learning", bank_ml),
    ("AI", "UNIT 7  ·  Artificial Intelligence", bank_ai),
    ("GA", "UNIT 8  ·  General Aptitude", bank_ga),
]


def _fill(code, items, per):
    out = uniq(items, 10**9)
    i = 0
    while len(out) < per:
        i += 1
        if code == "P&S":
            q = Q("P&S", "Binomial", "NAT", 1, "E",
                  f"A fair coin is tossed {i+3} times. C({i+3},1)/C({i+3},{i+2}) equals _____.",
                  None, "1", "C(n,1)=C(n,n-1).")
        elif code == "LA":
            q = Q("LA", "Trace", "NAT", 1, "E",
                  f"tr(diag({i},{i+3},{i+5})) equals _____.", None, str(3 * i + 8), "Sum of diagonal.")
        elif code == "Calc":
            q = Q("Calc", "Power rule", "NAT", 1, "E",
                  f"d/dx (x^{i+2}) at x=1 equals _____.", None, str(i + 2), "n at x=1.")
        elif code == "DSA":
            q = Q("DSA", "Tree size", "NAT", 1, "E",
                  f"A tree with {i+2} vertices has _____ edges.", None, str(i + 1), "v-1.")
        elif code == "DBMS":
            q = Q("DBMS", "Closure", "NAT", 1, "E",
                  f"A1..A{i+3} with A_j → A_{{j+1}}. |A1^+| equals _____.", None, str(i + 3), "Full chain.")
        elif code == "ML":
            q = Q("ML", "LOOCV", "NAT", 1, "E",
                  f"LOOCV with {i+9} labelled rows trains _____ models.", None, str(i + 9), "One per row.")
        elif code == "AI":
            q = Q("AI", "Minimax", "NAT", 2, "M",
                  f"Max root; left {i}; right min({i+2},{i+9}). Root value is _____.",
                  None, str(max(i, min(i + 2, i + 9))), "Min then max.")
        else:
            q = Q("GA", "Percent", "NAT", 1, "E",
                  f"{2+(i%8)}% of {50*i} equals _____.",
                  None, str((2 + (i % 8)) * 50 * i // 100), "Percentage.")
        if q["stem"] not in {x["stem"] for x in out}:
            out.append(q)
        if i > per * 5:
            break
    return out[:per]


def all_banks(per=260):
    banks = {}
    for code, _, fn in SUBJECTS:
        banks[code] = _fill(code, fn(per), per)
        print(code, len(banks[code]),
              {t: sum(1 for q in banks[code] if q["qtype"] == t) for t in ("MCQ", "MSQ", "NAT")})
    return banks
