#!/usr/bin/env python3
"""Generate bank_ml.py with unique GATE-DA Machine Learning items."""
from __future__ import annotations

import math
from _gen_common import Bank, nice, fmt_num

B = Bank("GATE DA Machine Learning item bank (supervised + unsupervised syllabus).")


def ols(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    b1 = num / den
    b0 = my - b1 * mx
    yhat = [b0 + b1 * x for x in xs]
    sse = sum((y - yh) ** 2 for y, yh in zip(ys, yhat))
    sst = sum((y - my) ** 2 for y in ys)
    ssr = sst - sse
    r2 = (ssr / sst) if sst else 0.0
    return dict(n=n, mx=mx, my=my, b0=b0, b1=b1, sse=sse, sst=sst, ssr=ssr, r2=r2, yhat=yhat)


def mean(a):
    return sum(a) / len(a)


def var_pop(a):
    m = mean(a)
    return sum((x - m) ** 2 for x in a) / len(a)


def var_sample(a):
    m = mean(a)
    return sum((x - m) ** 2 for x in a) / (len(a) - 1)


def euclid(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q)))


def manh(p, q):
    return sum(abs(a - b) for a, b in zip(p, q))


def gini_bin(n0, n1):
    n = n0 + n1
    if n == 0:
        return 0.0
    p0, p1 = n0 / n, n1 / n
    return 1.0 - p0 * p0 - p1 * p1


def entropy_bin(n0, n1):
    n = n0 + n1
    if n == 0:
        return 0.0
    h = 0.0
    for c in (n0, n1):
        if c:
            p = c / n
            h -= p * math.log(p, 2)
    return h


def sigmoid(z):
    if z >= 0:
        ez = math.exp(-z)
        return 1.0 / (1.0 + ez)
    ez = math.exp(z)
    return ez / (1.0 + ez)


# ---------------------------------------------------------------------------
# SLR
# ---------------------------------------------------------------------------
SLR = "SLR"

# unique named OLS datasets: (title, xname, yname, xs, ys, extra_qtype)
slr_sets = [
    ("Chai stall on FC Road", "cups", "revenue in 10 Rs", [1, 2, 3, 4], [2, 3, 5, 6]),
    ("Wheat plots in Nanded", "kg urea", "quintals", [0, 1, 2, 3], [2, 3, 5, 6]),
    ("Pune-Mumbai express", "speed 10 km/h", "stopping m", [4, 5, 6, 7], [8, 11, 13, 16]),
    ("Click ads for DiyaMart", "1000 impressions", "clicks", [1, 3, 5, 7], [2, 4, 7, 9]),
    ("Clinic BP desk", "BMI units over 20", "systolic excess", [1, 2, 3, 4], [4, 6, 7, 9]),
    ("Ice factory", "C above 0", "tonnes sold", [2, 4, 6, 8], [1, 2, 2, 3]),
    ("Tutoring hours", "weeks enrolled", "mock score", [1, 2, 3, 5], [40, 48, 52, 64]),
    ("Printer toner", "100 pages", "density drop", [2, 3, 4, 5], [1, 2, 2, 3]),
    ("Solar panel tilt", "degrees over 10", "kWh", [0, 2, 4, 6], [5, 8, 10, 13]),
    ("Bakery oven", "minutes extra", "loaf height mm", [1, 2, 3, 4], [10, 14, 16, 20]),
    ("Cricket nets", "overs faced", "runs", [2, 4, 6, 8], [6, 10, 16, 20]),
    ("Library footfall", "hours open extra", "entries 10s", [1, 2, 3, 4], [3, 5, 6, 8]),
]

for i, (title, xn, yn, xs, ys) in enumerate(slr_sets):
    f = ols(xs, ys)
    pts = ", ".join(f"({x},{y})" for x, y in zip(xs, ys))
    # slope NAT
    B.nat(
        SLR,
        f"{title} records {xn} x vs {yn} y as {pts}. Fit simple OLS with intercept. The fitted slope equals ____ (round to 2 decimals if needed).",
        nice(f["b1"]),
        f"b1 = Sxy/Sxx = {nice(f['b1'])}.",
        marks=2,
        diff="M",
    )
    # intercept or prediction or SSE depending on i to vary asked quantity
    if i % 3 == 0:
        xq = xs[-1] + 1
        yh = f["b0"] + f["b1"] * xq
        B.nat(
            SLR,
            f"Using the OLS line for {title} on pairs {pts} ({xn} vs {yn}), the prediction at x={xq} is ____.",
            nice(yh),
            f"yhat = {nice(f['b0'])} + {nice(f['b1'])}*{xq} = {nice(yh)}.",
            marks=2,
            diff="M",
        )
    elif i % 3 == 1:
        B.nat(
            SLR,
            f"For {title} data {pts} of {xn} against {yn}, the OLS intercept is ____.",
            nice(f["b0"]),
            f"b0 = ybar - b1 xbar = {nice(f['b0'])}.",
            marks=1,
            diff="M",
        )
    else:
        B.nat(
            SLR,
            f"On {title} the OLS residual sum of squares for {pts} ({xn}, {yn}) equals ____.",
            nice(f["sse"]),
            f"SSE = sum (y - yhat)^2 = {nice(f['sse'])}.",
            marks=2,
            diff="H",
        )

# more SLR conceptual unique
B.mcq(
    SLR,
    "Four GATE mock pairs (hours, score) are (1,10), (2,20), (3,30), (4,40). After fitting OLS, the residual at hours=3 is",
    "0",
    "10",
    "-10",
    "5",
    "A",
    "The points are collinear on y=10x, so every residual is 0.",
    marks=1,
    diff="E",
)
B.mcq(
    SLR,
    "OLS for y on x is y = 4 + 2x. The same sample is used to regress x on y. Which statement is TRUE?",
    "The slope of x on y must be 1/2",
    "The slope of x on y is 2 r^2, hence at most 1/2",
    "The slope of x on y equals r^2 / 2 times (sx/sy)^2 wait no: it is r^2 / 2",
    "The product of the two OLS slopes equals r^2",
    "D",
    "b_yx * b_xy = r^2, which lies in [0,1]. It equals 1/2 only if r^2=1 and the first slope is 2, which forces the reverse slope to 1/2, but D is the identity that always holds.",
    marks=2,
    diff="H",
)
B.msq(
    SLR,
    "Let e_i be OLS residuals from simple linear regression with intercept. Which identities ALWAYS hold?",
    "sum e_i = 0",
    "sum e_i x_i = 0",
    "sum e_i y_i = 0",
    "sum e_i yhat_i = 0",
    "A;B;D",
    "Normal equations give 1^T e = 0 and x^T e = 0. Also yhat is in the column space, so yhat^T e = 0. sum e y is not generally 0.",
    marks=2,
    diff="M",
)
B.mcq(
    SLR,
    "For a sample, corr(x,y)=0.6, s_x=2, s_y=5. The OLS slope of y on x equals",
    "0.60",
    "1.50",
    "2.40",
    "0.24",
    "B",
    "b1 = r * s_y / s_x = 0.6 * 5 / 2 = 1.5.",
    marks=1,
    diff="E",
)
B.nat(
    SLR,
    "A lab reports SST=80 and SSE=20 for an OLS fit of absorbance on concentration (with intercept). The coefficient of determination R^2 is ____.",
    0.75,
    "R^2 = 1 - SSE/SST = 1 - 20/80 = 0.75.",
    marks=1,
    diff="E",
)
B.mcq(
    SLR,
    "Simple OLS is fitted through the origin (no intercept) to (x,y) in {(1,1),(2,2),(3,1)}. The slope minimising sum of squared residuals is",
    "1",
    "6/7",
    "4/7",
    "5/7",
    "C",
    "Through-origin OLS: b = (sum x y)/(sum x^2) = (1+4+3)/(1+4+9) = 8/14 = 4/7.",
    marks=2,
    diff="M",
)

B.mcq(
    SLR,
    "In OLS y = b0 + b1 x + e, adding 5 to every x-value and leaving y unchanged will",
    "increase b1 by 5",
    "leave b1 unchanged and decrease b0 by 5 b1",
    "leave both b0 and b1 unchanged",
    "multiply b1 by 5",
    "B",
    "Slope is invariant to a shift of x; intercept adjusts by -b1 * 5.",
    marks=1,
    diff="M",
)
B.nat(
    SLR,
    "Pairs (2,3), (4,7), (6,11) lie on a straight line. OLS slope of y on x is ____.",
    2,
    "The unique line through the three points has slope (7-3)/(4-2)=2.",
    marks=1,
    diff="E",
)
B.mcq(
    SLR,
    "A residual plot of OLS on 'hours vs marks' fans out as hours grow. This most directly suggests",
    "the intercept is biased toward 0",
    "heteroscedasticity, so the Gauss-Markov equal-variance assumption fails",
    "the slope must be negative",
    "R^2 is necessarily 0",
    "B",
    "A fan shape is the textbook residual signature of non-constant variance.",
    marks=1,
    diff="M",
)
B.nat(
    SLR,
    "For n=5 observations, OLS with intercept uses how many degrees of freedom for SSE?",
    3,
    "Two parameters (intercept, slope) are estimated, so df = 5-2 = 3.",
    marks=1,
    diff="E",
)

# ---------------------------------------------------------------------------
# MLR
# ---------------------------------------------------------------------------
MLR = "MLR"

B.mcq(
    MLR,
    "Design matrix X is n x (p+1) including a column of ones. OLS beta_hat exists uniquely iff",
    "n > p+1 only",
    "X has full column rank p+1",
    "y is orthogonal to the column space",
    "the features are standard-normal",
    "B",
    "Uniqueness needs X^T X invertible, i.e. rank(X)=p+1.",
    marks=1,
    diff="E",
)
B.msq(
    MLR,
    "In multiple linear regression y = X beta + e with OLS, which are ALWAYS true when X has full column rank?",
    "The residual vector is orthogonal to every column of X",
    "H = X (X^T X)^{-1} X^T is the orthogonal projector onto col(X)",
    "R^2 cannot decrease when a new linearly independent column is added",
    "Every coefficient is unbiased even if a relevant variable is omitted",
    "A;B;C",
    "A,B are the normal-equation geometry. Unadjusted R^2 is non-decreasing in nested OLS. Omitted-variable bias can wreck unbiasedness.",
    marks=2,
    diff="M",
)
B.nat(
    MLR,
    "A house-price model uses intercept, area, and a binary 'near-metro'. n=40, OLS. How many columns does X have?",
    3,
    "Intercept + area + dummy = 3 columns.",
    marks=1,
    diff="E",
)
B.mcq(
    MLR,
    "Features x1 and x2 satisfy x2 = 2 x1 on every training row. For OLS of y on (1, x1, x2),",
    "X^T X is singular so the usual unique OLS solution does not exist",
    "the slope of x2 is forced to 2",
    "VIF of x1 is 0",
    "predictions are undefined for every y",
    "A",
    "Perfect collinearity makes rank(X)<3, so X^T X is not invertible.",
    marks=2,
    diff="M",
)
B.nat(
    MLR,
    "OLS on y ~ 1 + x1 + x2 is fitted. The fitted values are yhat = 3 + 2 x1 - x2. At (x1,x2)=(4,5) the prediction is ____.",
    6,
    "3 + 8 - 5 = 6.",
    marks=1,
    diff="E",
)
B.mcq(
    MLR,
    "Two features are orthogonal (after centering) in the sample. Then the MLR slope of each feature",
    "equals the SLR slope of y on that feature (with intercept)",
    "must be zero",
    "equals the inverse of the SLR slope",
    "cannot be estimated",
    "A",
    "For centered orthogonal columns, X^T X is diagonal, so each coefficient decouples to the simple-regression formula.",
    marks=2,
    diff="M",
)
B.nat(
    MLR,
    "A dummy-coded MLR uses 4 city levels (Pune, Nashik, Nagpur, Surat) plus intercept, no other features. The dummy block has how many columns (excluding intercept)?",
    3,
    "k-level categorical needs k-1 dummies with an intercept.",
    marks=1,
    diff="E",
)
B.mcq(
    MLR,
    "Adjusted R^2 differs from R^2 because it",
    "uses a kernel smoother",
    "penalises extra parameters via df, so it can fall when a useless feature is added",
    "is always larger than R^2",
    "equals 1 - SSE/SST without any n,p",
    "B",
    "R_adj^2 = 1 - (SSE/(n-p-1))/(SST/(n-1)); adding a useless variable can decrease it.",
    marks=1,
    diff="M",
)
B.msq(
    MLR,
    "Which modelling choices keep the problem inside multiple linear regression as used in GATE DA?",
    "y = b0 + b1 x + b2 x^2 + e  (polynomial in a scalar x)",
    "y = b0 + b1 log x + e with x>0",
    "y = b0 + b1 x1 + b2 x2 + b3 x1 x2 + e",
    "y = sigmoid(b0 + b1 x) with Bernoulli likelihood",
    "A;B;C",
    "A-C are linear in parameters. D is logistic regression, not MLR.",
    marks=2,
    diff="M",
)
B.nat(
    MLR,
    "n=12, p=3 predictors plus intercept. Residual df for OLS SSE is ____.",
    8,
    "df = n - (p+1) = 12-4 = 8.",
    marks=1,
    diff="E",
)
B.mcq(
    MLR,
    "If the true map is y = 1 + 2 x1 + 0 x2 + noise and we still include x2 in OLS, then as n grows",
    "the x2 coefficient converges to 0 in probability (no omitted bias here)",
    "R^2 converges to 0",
    "X^T X stays singular",
    "the intercept cannot be estimated",
    "A",
    "The model is correctly specified (true coeff of x2 is 0), so OLS is consistent and that entry goes to 0.",
    marks=2,
    diff="M",
)
B.mcq(
    MLR,
    "A fitted MLR is yhat = 10 + 3 x1 - 2 x2. Holding x1 fixed, a unit increase in x2 changes the mean response by",
    "3",
    "-2",
    "1",
    "10",
    "B",
    "Partial slope of x2 is -2.",
    marks=1,
    diff="E",
)
B.nat(
    MLR,
    "Centered features satisfy sum x1=0, sum x2=0, sum x1 x2=0, sum x1^2=10, sum x2^2=5, sum x1 y=20, sum x2 y=-10. The OLS slope of x1 is ____.",
    2,
    "Orthogonality: b1 = (x1^T y)/(x1^T x1) = 20/10 = 2.",
    marks=2,
    diff="M",
)
B.mcq(
    MLR,
    "Including an interaction x1 x2 in MLR means",
    "the partial effect of x1 is allowed to depend on the value of x2",
    "x1 and x2 must be independent in the population",
    "OLS becomes nonlinear in beta",
    "the intercept must be dropped",
    "A",
    "dyhat/dx1 = b1 + b3 x2 when the product term has coefficient b3.",
    marks=1,
    diff="M",
)
B.nat(
    MLR,
    "yhat = 5 + 0*x1 + 4*x2. At (x1,x2)=(10, 0.5) predicted y is ____.",
    7,
    "5 + 0 + 4*0.5 = 7. x1 drops out.",
    marks=1,
    diff="E",
)

# ---------------------------------------------------------------------------
# Ridge
# ---------------------------------------------------------------------------
RDG = "Ridge"

B.mcq(
    RDG,
    "Ridge regression (with intercept unpenalised, features centered) solves",
    "min ||y - Xb||_2^2 + lambda ||b||_2^2  for lambda > 0",
    "min ||y - Xb||_1 + lambda ||b||_2",
    "min ||y - Xb||_2^2 + lambda ||b||_1",
    "min ||b||_2 subject to ||y-Xb||_2 = 0",
    "A",
    "Ridge is squared loss plus L2 penalty on slopes.",
    marks=1,
    diff="E",
)
B.msq(
    RDG,
    "Relative to OLS, increasing the ridge penalty lambda typically",
    "raises bias of the coefficient vector",
    "lowers variance of the coefficient vector",
    "drives coefficients toward 0",
    "makes X^T X + lambda I more ill-conditioned",
    "A;B;C",
    "Ridge shrinks, trading bias for variance; adding lambda I improves conditioning, it does not worsen it.",
    marks=2,
    diff="M",
)
B.nat(
    RDG,
    "In 1-D with no intercept, X^T X = 4, X^T y = 8, lambda=4. The ridge coefficient is ____.",
    1,
    "b = (X^T X + lambda)^{-1} X^T y = 8/(4+4) = 1.",
    marks=2,
    diff="M",
)
B.nat(
    RDG,
    "Same 1-D setup X^T X=4, X^T y=8, but now lambda=0. The ridge (hence OLS) coefficient is ____.",
    2,
    "8/4 = 2. Ridge with lambda=0 recovers OLS.",
    marks=1,
    diff="E",
)
B.mcq(
    RDG,
    "As lambda -> infinity with fixed centered design, ridge slopes",
    "diverge",
    "approach the OLS vector",
    "approach the zero vector",
    "approach the principal-component loadings",
    "C",
    "The penalty dominates, so b_ridge -> 0.",
    marks=1,
    diff="E",
)
B.mcq(
    RDG,
    "Why add lambda I to X^T X in ridge?",
    "To enforce integer coefficients",
    "To guarantee a unique finite solution even when X is rank-deficient, and to shrink",
    "To turn the loss into hinge loss",
    "To make residuals heteroscedastic on purpose",
    "B",
    "X^T X + lambda I is SPD for lambda>0, hence invertible, and it shrinks.",
    marks=2,
    diff="M",
)
B.nat(
    RDG,
    "Two orthogonal centered columns have norms squared 9 and 4. X^T y = (18, 8). Ridge with lambda=3 gives the first coefficient equal to ____.",
    1.5,
    "b1 = 18/(9+3)=18/12=1.5 because the Gram matrix is diagonal.",
    marks=2,
    diff="M",
)
B.mcq(
    RDG,
    "Ridge vs OLS on a wide matrix (p > n, columns linearly dependent):",
    "OLS has a unique minimiser, ridge does not",
    "ridge has a unique minimiser, OLS does not",
    "both fail to have any minimiser",
    "both yield identical coefficients",
    "B",
    "OLS loss is minimised on an affine space when X is rank-deficient; ridge is strictly convex.",
    marks=2,
    diff="M",
)
B.nat(
    RDG,
    "If every ridge coefficient is multiplied by 0 after taking lambda to infinity, the training MSE approaches the MSE of the intercept-only model. For centered y with variance (1/n) SST = 16, that limiting MSE is ____.",
    16,
    "The intercept-only fit is ybar; for centered y, MSE = (1/n) SST = 16.",
    marks=2,
    diff="H",
)
B.mcq(
    RDG,
    "Standardising features before ridge is recommended because",
    "lambda then penalises coefficients on a comparable scale",
    "OLS already requires standardising to exist",
    "standardising removes the need for a penalty",
    "it converts ridge into LDA",
    "A",
    "L2 penalty is not scale-invariant; standardising makes lambda meaningful across features.",
    marks=1,
    diff="E",
)
B.msq(
    RDG,
    "Which statements about ridge are TRUE?",
    "The effective degrees of freedom fall as lambda grows",
    "Ridge paths are piecewise linear in lambda like lasso",
    "For a fixed design, b_ridge(lambda) = (X^T X + lambda I)^{-1} X^T y",
    "Ridge performs exact zeroing of coefficients for large finite lambda",
    "A;C",
    "Ridge shrinks but does not zero (unlike lasso). Paths are smooth, not piecewise linear.",
    marks=2,
    diff="H",
)
B.nat(
    RDG,
    "Scalar ridge: observations x=1,1,1 and y=3,5,7 (no intercept). X^T X=3, X^T y=15. With lambda=2 the coefficient is ____.",
    3,
    "15/(3+2)=3.",
    marks=1,
    diff="M",
)
B.mcq(
    RDG,
    "A researcher reports that raising lambda increased training R^2. This is",
    "expected, because ridge always fits training data better than OLS",
    "impossible for the usual nested ridge vs OLS on the same design: OLS maximises training R^2 among linear predictors, and ridge is a shrinkage of it",
    "required by Gauss-Markov",
    "proof that lambda was negative",
    "B",
    "OLS minimises training SSE in the linear class; ridge cannot beat it on train SSE unless lambda=0.",
    marks=2,
    diff="H",
)
B.nat(
    RDG,
    "Let X^T X = [[2,0],[0,2]] and X^T y = [4, 2], lambda=2. The ridge vector (b1,b2). The value of b2 is ____.",
    0.5,
    "b2 = 2/(2+2)=0.5.",
    marks=2,
    diff="M",
)
B.mcq(
    RDG,
    "Bias-variance reading of ridge: compared with OLS, a moderate lambda usually",
    "cuts variance more than it adds bias, lowering expected prediction error in ill-posed problems",
    "cuts bias and raises variance",
    "is identical to dropping intercept",
    "is the same as k-means",
    "A",
    "Classic shrinkage trade-off, helpful under multicollinearity or p comparable to n.",
    marks=1,
    diff="M",
)
B.nat(
    RDG,
    "OLS slope in 1-D (no intercept) is 5. Ridge uses lambda such that (X^T X + lambda) = 2 (X^T X). Then the ridge slope is ____.",
    2.5,
    "b_r = (X^T y)/(2 X^T X) = (1/2) b_ols = 2.5.",
    marks=2,
    diff="M",
)

# ---------------------------------------------------------------------------
# Logistic
# ---------------------------------------------------------------------------
LOG = "Logistic"

B.mcq(
    LOG,
    "Logistic regression models P(Y=1|x) as",
    "w^T x  (unbounded)",
    "sigmoid(w^T x + b) = 1/(1+exp(-(w^T x+b)))",
    "the density of N(w^T x, 1)",
    "a hard 0-1 threshold of w^T x",
    "B",
    "The logistic (sigmoid) maps a linear score to (0,1).",
    marks=1,
    diff="E",
)
B.nat(
    LOG,
    "If the fitted sigmoid outputs f(x)=0.8, the derivative f(x)(1-f(x)) equals ____.",
    0.16,
    "0.8*0.2=0.16.",
    marks=1,
    diff="E",
)
B.nat(
    LOG,
    "Sigmoid output 0.2. Then f(1-f) equals ____.",
    0.16,
    "0.2*0.8=0.16. Same value as at 0.8 by symmetry.",
    marks=1,
    diff="E",
)
B.nat(
    LOG,
    "A logistic model has score z = 2 x - 2. At x=1 the predicted probability is ____.",
    0.5,
    "z=0, sigmoid(0)=1/2.",
    marks=1,
    diff="E",
)
B.mcq(
    LOG,
    "Log-odds form: log P/(1-P) = 3 - 6 x. The decision boundary P=0.5 occurs at x equal to",
    "0",
    "0.5",
    "2",
    "3",
    "B",
    "P=0.5 iff log-odds=0 iff 3-6x=0 iff x=1/2.",
    marks=1,
    diff="M",
)
B.msq(
    LOG,
    "Which are TRUE of binary logistic regression trained by MLE?",
    "The negative log-likelihood is convex in (w,b), so a global optimum exists",
    "With linearly separable data and no regularisation, ||w|| may diverge",
    "Predicted probabilities are guaranteed to be exactly 0 or 1 on train points",
    "A feature-scale change can be absorbed into w",
    "A;B;D",
    "NLL is convex; separability sends MLE to infinity; probabilities stay in (0,1). Affine rescaling of a feature is compensated by w.",
    marks=2,
    diff="H",
)
B.nat(
    LOG,
    "One training pair x=2, y=1. Model p = sigmoid(w x) with current w=0. Gradient of log-loss L= -log p w.r.t. w is (p-y) x. One SGD step with eta=0.5 updates w to ____.",
    0.5,
    "p=sigmoid(0)=0.5, grad=(0.5-1)*2=-1, w := 0 - 0.5*(-1)=0.5.",
    marks=2,
    diff="H",
)
B.nat(
    LOG,
    "Current w=1, x=0 (so p=0.5), y=0, eta=1, grad=(p-y)x=0. After one SGD step w equals ____.",
    1,
    "Gradient is 0 because x=0, so w stays 1.",
    marks=1,
    diff="M",
)
B.mcq(
    LOG,
    "Binary cross-entropy on a single point with y=1 and p=0.5 equals (natural log)",
    "0",
    "log 2",
    "1",
    "0.5",
    "B",
    "-log(0.5)=log 2.",
    marks=1,
    diff="M",
)
B.mcq(
    LOG,
    "Unlike LDA, logistic regression",
    "requires class-conditional Gaussians",
    "models P(Y|x) directly and does not need a Gaussian class-conditional assumption",
    "cannot use a linear decision boundary",
    "cannot output probabilities",
    "B",
    "Logistic is a discriminative linear model for the log-odds.",
    marks=1,
    diff="M",
)
B.nat(
    LOG,
    "Odds P/(1-P)=3. Then P equals ____.",
    0.75,
    "P=3(1-P) => 4P=3 => P=0.75.",
    marks=1,
    diff="E",
)
B.mcq(
    LOG,
    "A 1-D logistic classifier predicts class 1 iff 4x - 2 >= 0. The threshold on x is",
    "0",
    "0.5",
    "2",
    "4",
    "B",
    "4x>=2 => x>=1/2.",
    marks=1,
    diff="E",
)
B.nat(
    LOG,
    "Sigmoid derivative at f(x)=0.5 equals ____.",
    0.25,
    "0.5*0.5=0.25, the maximum of p(1-p).",
    marks=1,
    diff="E",
)
B.mcq(
    LOG,
    "L2-regularised logistic regression adds (lambda/2)||w||^2. As lambda grows the decision boundary",
    "must become quadratic",
    "shrinks toward the origin in parameter space, typically moving toward a prior-only classifier",
    "interpolates every label",
    "becomes k-means",
    "B",
    "Shrinkage drives w to 0, so predictions approach the intercept-only (class prior) model.",
    marks=2,
    diff="M",
)
B.nat(
    LOG,
    "Score z=-2. sigmoid(z) = 1/(1+e^{2}). Using e^2 ~ 7.39, the probability rounded to 2 decimals is ____.",
    0.12,
    "1/(1+7.39)=1/8.39~0.119 ~ 0.12.",
    marks=2,
    diff="M",
)
B.msq(
    LOG,
    "For a linear logistic model in 2-D, the set {x : P(Y=1|x)=0.5} is",
    "a hyperplane (a line in 2-D)",
    "always a circle",
    "unchanged if w and b are multiplied by the same positive constant",
    "empty if w=0 and b=0, because then P=0.5 everywhere so the =0.5 set is the whole plane, not a line",
    "A;C;D",
    "P=0.5 iff w^T x+b=0, a hyperplane if w != 0. Positive scaling of (w,b) keeps the zero set. If w=b=0, P=0.5 everywhere.",
    marks=2,
    diff="H",
)
B.nat(
    LOG,
    "Three points with labels 1,1,0 have predicted p=0.8, 0.8, 0.2. Mean Bernoulli log-likelihood (base e) is (2 log 0.8 + log 0.8? wait: 2*log(0.8)+log(0.8) no: last is y=0 so log(1-p)=log(0.8). All three contribute log 0.8. Average is log 0.8. Using log 0.8 ~ -0.22314, report the average NLL = - mean ll, rounded to 2 decimals.",
    0.22,
    "Each term -log 0.8 ~ 0.223, average ~ 0.22.",
    marks=2,
    diff="H",
)
B.mcq(
    LOG,
    "A logistic weight on 'hours_studied' is +1.2. Holding others fixed, one extra hour",
    "adds 1.2 to the probability",
    "adds 1.2 to the log-odds",
    "multiplies the probability by 1.2",
    "is illegal in logistic models",
    "B",
    "Coefficients are log-odds slopes, not probability slopes.",
    marks=1,
    diff="M",
)

# ---------------------------------------------------------------------------
# kNN
# ---------------------------------------------------------------------------
KNN = "kNN"

B.mcq(
    KNN,
    "Training points: A(0,0) class 0, B(0,2) class 0, C(2,0) class 1, D(2,2) class 1. Query q=(0,1). 1-NN (Euclidean) predicts",
    "class 0, because A and B are both at distance 1 and C,D are farther",
    "class 1",
    "class 0 only if Manhattan distance is used",
    "tie among all four",
    "A",
    "d(q,A)=d(q,B)=1, d(q,C)=sqrt(4+1)=sqrt5, d(q,D)=sqrt(4+1)=sqrt5. Nearest are class 0.",
    marks=2,
    diff="M",
)
B.nat(
    KNN,
    "Points: P(0,0) y=1, Q(4,0) y=2, R(0,3) y=2. Query (1,1). Euclidean 1-NN label is ____.",
    1,
    "d(P)=sqrt(2)~1.41, d(Q)=sqrt(9+1)~3.16, d(R)=sqrt(1+4)~2.24. Nearest is P with label 1.",
    marks=2,
    diff="M",
)
B.mcq(
    KNN,
    "In the previous geometry, 3-NN majority label at (1,1) is",
    "1, because P wins",
    "2, because Q and R out-vote P",
    "undefined because k exceeds n",
    "always equal to 1-NN",
    "B",
    "All three points are used; labels 1,2,2 so majority 2.",
    marks=1,
    diff="E",
)
B.msq(
    KNN,
    "Which statements about k-NN classification are TRUE?",
    "Training error of 1-NN is 0 if no two equal-x points have different labels",
    "As k -> n, the prediction at every point approaches the global majority class",
    "1-NN has lower bias and higher variance than a large k, typically",
    "k-NN needs an explicit parametric density for each class",
    "A;B;C",
    "k-NN is a nonparametric local vote. Large k smooths toward the prior. No class-density model is fitted.",
    marks=2,
    diff="M",
)
B.nat(
    KNN,
    "1-D train: x=0,1,2,3 with labels 0,0,1,1. Query x=1.6 with k=1 (Euclidean). Predicted label is ____.",
    1,
    "Nearest is x=2 (dist 0.4) vs x=1 (dist 0.6), label 1.",
    marks=1,
    diff="E",
)
B.nat(
    KNN,
    "Same 1-D train 0,1,2,3 labels 0,0,1,1. Query 1.6 with k=3. Predicted majority label is ____.",
    1,
    "Neighbours of 1.6: x=2 (dist 0.4, label 1), x=1 (0.6, label 0), x=3 (1.4, label 1). Majority 1.",
    marks=2,
    diff="H",
)

B.mcq(
    KNN,
    "Manhattan 1-NN on A(0,0):0, B(3,0):1, query (1,1). Predicted class is",
    "0, since |1|+|1|=2 < |2|+|1|=3",
    "1",
    "tie",
    "2",
    "A",
    "d1(A)=2, d1(B)=3, so A wins with class 0.",
    marks=1,
    diff="M",
)
B.mcq(
    KNN,
    "A large k in k-NN, relative to k=1, typically",
    "fits more wiggly decision boundaries",
    "smooths the decision boundary and raises bias",
    "is undefined for classification",
    "always overfits more than 1-NN",
    "B",
    "Larger neighbourhoods average more, higher bias, lower variance.",
    marks=1,
    diff="E",
)
B.nat(
    KNN,
    "Five training labels in a neighbourhood are 1,1,1,0,0. 5-NN majority class is ____.",
    1,
    "Votes 3 to 2 for class 1.",
    marks=1,
    diff="E",
)
B.mcq(
    KNN,
    "k-NN regression with k=2 on pairs (0,0), (2,4), (10,0). Query x=1. The prediction is",
    "0",
    "2",
    "4",
    "1",
    "B",
    "Nearest are (0,0) and (2,4); mean response (0+4)/2=2.",
    marks=2,
    diff="M",
)
B.mcq(
    KNN,
    "Feature A is in millimetres, feature B in kilometres. Euclidean k-NN without scaling will",
    "treat both axes as equally important automatically",
    "be dominated by the large-magnitude axis unless features are scaled",
    "become logistic regression",
    "ignore the training labels",
    "B",
    "Distance k-NN is not scale-invariant.",
    marks=1,
    diff="E",
)
B.nat(
    KNN,
    "Train points on the line: -2,-1,0,8 with labels 1,1,1,0. 3-NN at query 7. The predicted label is ____.",
    1,
    "Dists from 7: to 8 is 1 (label 0), to 0 is 7 (label 1), to -1 is 8 (label 1). Votes 0,1,1 so majority 1.",
    marks=2,
    diff="M",
)

B.msq(
    KNN,
    "Leave-one-out error of 1-NN on a 1-D two-class set that is perfectly clustered (all 0s then all 1s, no overlap) is driven by",
    "only the two points at the class boundary, which may be closer to the other class when left out",
    "every interior point, which is still nearer a same-class neighbour",
    "the fact that 1-NN LOOCV error must be 50 percent",
    "distance ties only",
    "A;B",
    "Interior points stay correctly classified by a same-class neighbour; only the two boundary points can flip. C is false.",
    marks=2,
    diff="H",
)
B.nat(
    KNN,
    "3-NN classifier, 2-class, odd k so no vote ties. Training set size n=10. A query's 3 neighbours have labels 1,1,0. Predicted class is ____.",
    1,
    "Majority of {1,1,0} is 1.",
    marks=1,
    diff="E",
)
B.mcq(
    KNN,
    "k-NN is a lazy learner meaning",
    "it updates a global w by SGD at train time",
    "it stores the training set and defers computation to query time",
    "it discards the training set after building a tree of depths k",
    "it requires linearly separable data",
    "B",
    "No parametric model is fitted; neighbours are retrieved at prediction.",
    marks=1,
    diff="E",
)
B.nat(
    KNN,
    "Points (0,0), (0,2), (6,0). Query (1,0). Euclidean 1-NN is the first point. Its distance is ____.",
    1,
    "sqrt((1-0)^2+(0-0)^2)=1.",
    marks=1,
    diff="E",
)
B.mcq(
    KNN,
    "If k equals the training size n, k-NN classification (majority vote, no distance weights) ignores the query location and returns",
    "the 1-NN label",
    "the training majority class",
    "a random class with equal probability always",
    "the mean of the features",
    "B",
    "Every training point is a neighbour, so the vote is the global mode.",
    marks=1,
    diff="E",
)

print("partial ml count", len(B.rows))
