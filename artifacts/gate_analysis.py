"""Official-pattern analysis text for GATE DA 2024–2026 and 2027 prediction framing."""

DISCLAIMER = (
    "This book is a preparation instrument, not an official GATE publication and not a leak. "
    "FACT means something shown by an official syllabus, paper, or answer key. "
    "OBSERVATION means a pattern visible across official papers. "
    "INFERENCE is a reasoned conclusion from those patterns plus GATE CS history. "
    "PREDICTION means a study-priority judgement. No question here is claimed to appear verbatim in GATE DA 2027."
)

FACTS = [
    "FACT: GATE 2027 is organised by IIT Madras. Official exam dates announced: 6, 7, 13, 14, 20 and 21 February 2027.",
    "FACT: Official DA 2027 syllabus (gate2027.iitm.ac.in) has the same seven core sections as 2024–2026: Probability & Statistics; Linear Algebra; Calculus & Optimization; Programming, DSA; DBMS & Warehousing; Machine Learning; AI.",
    "FACT: Multiple independent reports of the 2027 syllabus release state that DA is unchanged from 2026. Treat the 2024–2026 papers as the primary official evidence base.",
    "FACT: GATE DA is a 3-hour CBT, 65 questions, 100 marks. General Aptitude is 10 questions / 15 marks. The DA core is 55 questions / 85 marks. There is no separate Engineering Mathematics bucket; mathematics is inside the DA core.",
    "FACT: Question types are MCQ, MSQ and NAT. Negative marking applies only to MCQ (−1/3 for 1-mark, −2/3 for 2-mark). MSQ has no partial credit and no negative marking. NAT has no negative marking.",
    "FACT: Latest confirmed internal layout (GATE DA 2026 official key): Q1–Q10 GA; Q11–Q35 one-mark DA; Q36–Q65 two-mark DA. Within DA, 1-mark items run MCQ then MSQ then NAT; 2-mark items run MCQ then MSQ then NAT.",
    "FACT: DA was introduced in GATE 2024 (IISc Bengaluru), continued in 2025 (IIT Roorkee) and 2026 (IIT Guwahati). Three official papers exist. That sample is small; do not treat frequency counts as statistically tight probabilities.",
]

# Compact topic tags used in the matrix
MATRIX = [
    # subject, topic, y24, y25, y26, cs, importance, under, p2027
    ("P&S", "Conditional / Bayes / total probability", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("P&S", "Expectation, variance, conditioning E[X|Y]", "Y", "Y", "Y", "High", "Core", "No", "VERY HIGH"),
    ("P&S", "Discrete: Bernoulli / Binomial / counting", "Y", "Y", "Y", "High", "Core", "No", "VERY HIGH"),
    ("P&S", "Continuous: Uniform / Exponential / Normal", "Y", "Y", "Y", "High", "Core", "No", "VERY HIGH"),
    ("P&S", "Joint PDF, marginal, conditional PDF", "Y", "Y", "Y", "Med", "Core", "Partial", "HIGH"),
    ("P&S", "Covariance / correlation / independence", "Y", "Y", "Y", "High", "Core", "No", "VERY HIGH"),
    ("P&S", "CLT, CI, z/t/chi-square tests", "Low", "Low", "Low", "Med", "Syllabus", "YES", "HIGH"),
    ("P&S", "t and chi-square distributions as objects", "N", "N", "N", "Low", "Syllabus", "YES", "MEDIUM"),
    ("LA", "Eigenvalues / eigenvectors / characteristic poly", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("LA", "Rank, nullity, linear dependence", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("LA", "Special matrices: orthogonal, projection, idempotent", "Y", "Y", "Y", "Med-High", "DA-specific", "Partial", "VERY HIGH"),
    ("LA", "SVD / outer products / singular values", "Y", "Low", "Y", "Med", "ML-link", "Partial", "HIGH"),
    ("LA", "LU / Gaussian elimination complexity", "Y", "Y", "Low", "High", "Core", "No", "HIGH"),
    ("LA", "Quadratic forms / positive definite", "Y", "Low", "Low", "Med", "Syllabus", "YES", "HIGH"),
    ("LA", "Vector spaces / subspaces / projection onto subspace", "Y", "Y", "Y", "High", "Core", "No", "VERY HIGH"),
    ("Calc", "Limits, continuity, differentiability", "Y", "Y", "Y", "High", "Core", "No", "HIGH"),
    ("Calc", "Taylor series / higher derivatives", "Y", "Y", "Low", "Med", "Core", "Partial", "HIGH"),
    ("Calc", "Maxima-minima of one variable", "Y", "Y", "Y", "High", "Core", "No", "VERY HIGH"),
    ("Calc", "Single-variable optimisation / critical points", "Y", "Y", "Y", "Med", "ML-link", "No", "VERY HIGH"),
    ("DSA", "Python semantics (defaults, lists, scope)", "Y", "Y", "Y", "CS uses C", "DA-specific", "No", "VERY HIGH"),
    ("DSA", "Sorting + recurrences (QS, MS, insertion)", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("DSA", "Trees: traversals, BST, height relations", "Y", "Y", "Y", "Very high", "Core", "No", "HIGH"),
    ("DSA", "Hashing / collisions / load", "Y", "Y", "Low", "Very high", "Core", "Partial", "HIGH"),
    ("DSA", "Stacks, queues, deques, linked lists", "Y", "Y", "Y", "High", "Core", "No", "HIGH"),
    ("DSA", "Graphs: BFS/DFS, DAG, shortest path", "Y", "Y", "Y", "Very high", "AI-link", "Partial", "VERY HIGH"),
    ("DSA", "Search: linear / binary complexity", "Y", "Y", "Y", "High", "Core", "No", "HIGH"),
    ("DB", "Functional dependencies / candidate keys", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("DB", "Normal forms / decomposition / preservation", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("DB", "Relational algebra / tuple calculus", "Y", "Y", "Y", "High", "Core", "Partial", "HIGH"),
    ("DB", "SQL (joins, nested, aggregation, NULL)", "Y", "Y", "Y", "Very high", "Core", "No", "VERY HIGH"),
    ("DB", "Indexing / file organisation", "Low", "Low", "Y", "High", "Syllabus", "YES", "HIGH"),
    ("DB", "OLAP / data cube / roll-up / warehouse schemas", "Y", "Low", "Y", "Low in CS", "DA-specific", "Partial", "HIGH"),
    ("DB", "Discretisation / sampling / compression", "N", "N", "Low", "Low", "Syllabus", "YES", "MEDIUM"),
    ("ML", "Linear / ridge / logistic regression", "Y", "Y", "Y", "Low-Med", "Core", "No", "VERY HIGH"),
    ("ML", "Bias-variance / regularisation / CV / LOO", "Y", "Y", "Y", "Low", "Core", "No", "VERY HIGH"),
    ("ML", "PCA / dimensionality reduction", "Y", "Y", "Y", "Low", "Core", "No", "VERY HIGH"),
    ("ML", "kNN / decision trees / entropy-gain", "Y", "Y", "Y", "Med", "Core", "No", "VERY HIGH"),
    ("ML", "Naive Bayes / LDA / generative classifiers", "Y", "Y", "Low", "Med", "Core", "Partial", "HIGH"),
    ("ML", "SVM / margins / kernels (level of syllabus)", "Y", "Low", "Low", "Med", "Core", "YES", "HIGH"),
    ("ML", "k-means / hierarchical linkage", "Y", "Y", "Y", "Low", "Core", "No", "HIGH"),
    ("ML", "MLP / feed-forward / ReLU composition", "Y", "Y", "Y", "Low", "Core", "Partial", "HIGH"),
    ("AI", "Uninformed vs informed search / A*", "Y", "Y", "Y", "High (AI elec)", "Core", "No", "VERY HIGH"),
    ("AI", "Adversarial / game trees / minimax", "Y", "Y", "Low", "Med", "Core", "Partial", "HIGH"),
    ("AI", "Propositional + predicate logic / entailment", "Y", "Y", "Y", "High (TOC/DM)", "Core", "No", "VERY HIGH"),
    ("AI", "Bayesian networks / variable elimination", "Y", "Y", "Y", "Low", "Core", "Partial", "VERY HIGH"),
    ("AI", "Sampling / approximate inference", "Low", "Low", "Low", "Low", "Syllabus", "YES", "HIGH"),
    ("GA", "Verbal analogy / grammar / RC inference", "Y", "Y", "Y", "Always", "Fixed 15", "No", "VERY HIGH"),
    ("GA", "Quant: combinatorics, series, logs", "Y", "Y", "Y", "Always", "Fixed 15", "No", "VERY HIGH"),
    ("GA", "Spatial / puzzle assembly", "Y", "Y", "Y", "Always", "Fixed 15", "No", "HIGH"),
    ("GA", "Analytical games / arrangements", "Y", "Y", "Y", "Always", "Fixed 15", "No", "HIGH"),
]

YEAR_NOTES = {
    "2024": (
        "First official DA paper (IISc). The setters established the genre: short conceptual MCQs, "
        "MSQs that punish incomplete definitions, and NATs that need a clean numerical finish. "
        "Mathematics and programming were already mixed with ML/AI rather than isolated. "
        "Logic, keys/FDs, PCA-adjacent linear algebra, and elementary probability all appeared. "
        "Several 2-mark NATs were short calculations (probability, linear algebra scalars, simple ML counts)."
    ),
    "2025": (
        "IIT Roorkee paper. Strong presence of conditional expectation identities, structured matrices "
        "(row-sum / polynomial of a matrix), hashing with linear probing, propositional equivalence, "
        "dependency-preserving decompositions, CDFs and transformations of Gaussians, and linear classifiers. "
        "Gaussian-elimination complexity on a structured matrix is a typical GATE move: they test whether "
        "you notice structure instead of quoting the generic O(n^3) blindly."
    ),
    "2026": (
        "IIT Guwahati paper. Very DA-shaped: PCA orthogonality of principal axes, LOOCV sample accounting, "
        "Python mutable default argument, candidate keys from a small FD set, OLAP projection of a data cube, "
        "quicksort expected recurrence, FOL entailment, ReLU networks, kNN on a tiny point set, a four-node "
        "Bayes net NAT, coin-toss covariance, joint-density conditional expectation, SVD of a rank-1 outer product, "
        "and a decision-tree style table. Hypothesis testing and t/chi-square objects remained thin."
    ),
}

WEIGHT_MODEL = """
Observed (not official) core-mark ranges across 2024–2026, reconstructed from question stems
and typical topic tagging. These are OBSERVATIONS, rounded, and year-to-year movement is real.

  Probability & Statistics ........ about 12–18 marks
  Linear Algebra .................. about 8–14 marks
  Calculus & Optimisation ......... about 4–8 marks
  Programming + DSA ............... about 12–20 marks
  DBMS + Warehousing .............. about 8–14 marks
  Machine Learning ................ about 10–16 marks
  Artificial Intelligence ......... about 8–14 marks
  General Aptitude ................ exactly 15 marks

PREDICTION for preparation time, not a promised 2027 split:
  Spend roughly 30–35% of study hours on Mathematics (P&S + LA + Calculus).
  Spend 25–30% on ML + AI together, always with the maths that sits underneath them.
  Spend 20–25% on Programming/DSA + DBMS.
  Keep GA alive with short daily sets; 15 marks are cheap only if you practise them.

Why not copy one year's counts? 2026 looked ML/DB/probability heavy; 2025 looked more
linear-algebra + probability-identity heavy. A 2027 paper can legally sit anywhere inside
the same syllabus. Train the whole syllabus; overweight the high-leverage concepts.
"""

CS_TRANSFER = [
    ("Asymptotic complexity of sorts/search",
     "CS asks worst-case of QS, MS, heap, binary search invariants.",
     "DA asks the same plus Python-level cost and expected-time recurrences (seen in 2026 QS)."),
    ("Hashing with probing",
     "CS staple: hash function, clustering, unsuccessful search probes.",
     "DA 2025 already used linear probing. Easy 1–2 mark item."),
    ("Functional dependencies, keys, 3NF/BCNF",
     "CS workhorse for 2 decades.",
     "DA asks the same, often as MSQ on which attributes form a key."),
    ("SQL nested queries and NULL",
     "CS loves NOT IN / NOT EXISTS / 3-valued logic.",
     "DA 2026 used a multi-table movie schema. Same traps."),
    ("BFS/DFS, shortest path, DAG properties",
     "CS algorithms paper.",
     "DA uses them both as DSA and as uninformed/informed search in AI."),
    ("Propositional / first-order logic",
     "CS Discrete Maths + some AI electives.",
     "DA tests entailment, prenex readings, and 'which sentence is valid'."),
    ("Eigenvalues, rank, projections",
     "CS engineering maths, thinner than DA.",
     "DA goes further: projection/idempotent/orthogonal matrices and SVD because of PCA."),
    ("Conditional probability and Bayes",
     "CS maths + AI uncertainty.",
     "DA connects it to Naive Bayes and Bayesian networks."),
    ("Recursion and trees",
     "CS C-recursion traces.",
     "DA prefers Python traces and tree-shape identities (H, I, L, N)."),
    ("Dynamic programming / greedy",
     "Central in CS Algorithms.",
     "Not named in the DA syllabus. Do not study DP as a DA topic. Use only if a search/optimisation question needs it."),
]

UNDERTESTED = [
    "Hypothesis testing: z-test, t-test, chi-square test, and confidence intervals — listed explicitly, rarely a clean standalone NAT so far.",
    "t-distribution and chi-square as named sampling distributions.",
    "Partition matrices and their block algebra.",
    "Tuple relational calculus (SQL/RA appear more often).",
    "Data-warehouse concept hierarchies and measure categorisation beyond one OLAP stem.",
    "Discretisation, sampling designs, and compression as data-transformation items.",
    "LDA as a named classifier (Naive Bayes and logistic appear more).",
    "SVM dual / margin geometry beyond a definition-level MCQ.",
    "Approximate inference by sampling (likelihood weighting, Gibbs) — syllabus-listed, thin so far.",
    "Adversarial search with alpha-beta numerical traces.",
    "Hierarchical clustering with complete vs single linkage on a 4-point distance matrix.",
    "Ridge regression as a matrix formula (X^T X + λI) rather than a verbal regularisation item.",
]

TRAPS = [
    "Quoting O(n^3) Gaussian elimination on a triangular or otherwise structured matrix.",
    "Treating MSQ like MCQ and marking only the 'most familiar' option.",
    "Confusing orthogonality of principal components with uncorrelated features in the original basis.",
    "Python mutable default argument: the same list object is reused across calls.",
    "Candidate key vs superkey vs prime attribute.",
    "P(A|B) vs P(B|A); forgetting the complement path in total probability.",
    "E[X|Y] is a random variable; E[E[X|Y]] = E[X] is an identity, not 'equals Y'.",
    "Independence implies Cov = 0; converse is false without extra assumptions.",
    "ReLU networks are not linear overall, but they are linear in each activation pattern region.",
    "A* is informed; BFS/DFS/DLS are uninformed. Greedy best-first is informed but not optimal.",
    "kNN with even k and ties; GATE often asks the smallest odd k that changes a label.",
    "SQL NULL: 'col = NULL' is unknown; NOT IN with a NULL in the list collapses.",
    "Normalisation: 3NF allows a non-prime to depend on a proper subset of a key in a restricted way; BCNF does not.",
    "Variance of Exponential(λ) is 1/λ^2, mean is 1/λ — mixing the two is a classic NAT miss.",
    "Rank-1 matrix uu^T has one nonzero singular value ||u||^2 (for the positive orientation of σ).",
]
