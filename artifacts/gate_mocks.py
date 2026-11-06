"""Ten distinct GATE-DA-shaped papers assembled from templates + the curated bank."""
from copy import deepcopy
from gate_questions import all_questions

# Paper themes requested by the user
THEMES = {
    "A": "Balanced baseline",
    "B": "Mathematics-heavy",
    "C": "Machine-learning-heavy",
    "D": "AI-heavy",
    "E": "Programming / DSA-heavy",
    "F": "Probability / statistics-heavy",
    "G": "CS-to-DA crossover-heavy",
    "H": "Conceptual / tricky",
    "I": "Numerical / NAT-heavy",
    "J": "High-difficulty rank-separator",
}

GA_BANK = [
    dict(stem="Transparent : Opaque :: Flexible : ____",
         options=["Rigid", "Clear", "Soft", "Bright"], answer="A",
         sol="Antonym analogy."),
    dict(stem="Choose the grammatically correct sentence.",
         options=["Each of the students have a locker.",
                  "Each of the students has a locker.",
                  "Each of the student have a locker.",
                  "Each students has a locker."], answer="B",
         sol="Each takes a singular verb."),
    dict(stem="If 15% of x is 45, then x equals",
         options=["300", "250", "200", "350"], answer="A",
         sol="0.15x=45 ⇒ x=300."),
    dict(stem="The next number in 2, 6, 12, 20, 30, … is",
         options=["40", "42", "36", "44"], answer="B",
         sol="n(n+1): 5·6=30, 6·7=42."),
    dict(stem="A cube is painted and cut into 27 unit cubes. How many have exactly one face painted?",
         options=["6", "8", "12", "1"], answer="A",
         sol="One face per side of the 3×3×3, centres of faces: 6."),
    dict(stem="All poets are dreamers. Some dreamers are engineers. Which follows?",
         options=["All engineers are poets",
                  "Some poets are engineers",
                  "None of the poets can be engineers",
                  "None of the conclusions A–C must follow"], answer="D",
         sol="The some-dreamers set need not intersect poets."),
    dict(stem="log10 0.01 equals",
         options=["2", "−2", "0.01", "10"], answer="B",
         sol="10^{−2}=0.01."),
    dict(stem="The mean of 3, 7, 8, 10, 12 is",
         options=["8", "7", "9", "10"], answer="A",
         sol="40/5=8."),
    dict(stem="If today is Wednesday, then 100 days from today is",
         options=["Friday", "Saturday", "Sunday", "Monday"], answer="A",
         sol="100 mod 7 = 2, Wednesday+2=Friday."),
    dict(stem="A shop offers successive discounts of 10% and 10%. Equivalent single discount is",
         options=["20%", "19%", "21%", "18%"], answer="B",
         sol="1−0.9·0.9=0.19."),
    dict(stem="Select the odd one: triangle, square, pentagon, circle",
         options=["triangle", "square", "pentagon", "circle"], answer="D",
         sol="Only non-polygon."),
    dict(stem="If all Bloops are Razzies and some Razzies are Lazzies, then",
         options=["all Bloops are Lazzies", "some Bloops are Lazzies",
                  "no Bloops are Lazzies", "none of A–C is forced"], answer="D",
         sol="Standard syllogism trap."),
    dict(stem="The ratio 2:3 equals which percentage of the second part over the whole?",
         options=["40%", "60%", "50%", "66%"], answer="B",
         sol="3/5=60%."),
    dict(stem="Simple interest on 2000 at 10% per annum for 2 years is",
         options=["200", "400", "420", "440"], answer="B",
         sol="2000·0.1·2=400."),
    dict(stem="A clock shows 3:15. The angle between hour and minute hands is",
         options=["0°", "7.5°", "15°", "22.5°"], answer="B",
         sol="Minute at 90°, hour at 97.5°, difference 7.5°."),
]


def ga_block(seed):
    """10 GA questions: 5 one-mark + 5 two-mark."""
    out = []
    for i in range(10):
        item = deepcopy(GA_BANK[(seed + i) % len(GA_BANK)])
        item.update(qtype="MCQ", marks=1 if i < 5 else 2, subject="GA",
                    topic="GA", diff="Easy" if i < 6 else "Moderate",
                    pred="HIGH", sid=f"GA{seed}-{i+1}")
        out.append(item)
    return out


def mcq(stem, opts, ans, sol, **meta):
    d = dict(stem=stem, options=opts, answer=ans, sol=sol, qtype="MCQ")
    d.update(meta)
    return d


def msq(stem, opts, ans, sol, **meta):
    d = dict(stem=stem, options=opts, answer=ans, sol=sol, qtype="MSQ")
    d.update(meta)
    return d


def nat(stem, ans, sol, **meta):
    d = dict(stem=stem, options=None, answer=str(ans), sol=sol, qtype="NAT")
    d.update(meta)
    return d


def paper_core(letter, seed):
    """55 DA items with a theme bias. Layout matches 2026:
    11-22 MCQ 1mk, 23-28 MSQ 1mk, 29-35 NAT 1mk,
    36-46 MCQ 2mk, 47-54 MSQ 2mk, 55-65 NAT 2mk.
    """
    # Numeric flavouring so papers are not copies
    a, b, n = 2 + (seed % 5), 3 + (seed % 4), 6 + (seed % 5)
    lam = [2, 4, 5, 8][seed % 4]
    p = [0.2, 0.25, 0.4][seed % 3]
    items = []

    # ----- 1-mark MCQ (12) -----
    items += [
        mcq("Which quantity equals the trace of a square matrix?",
            ["product of eigenvalues", "sum of eigenvalues (with multiplicity)",
             "determinant", "rank"], "B",
            "Trace = sum of eigenvalues = sum of diagonal entries.",
            subject="LA", topic="Eigenvalues", diff="Easy", pred="VERY HIGH"),
        mcq("P(A∪B)=P(A)+P(B) holds for all A,B that are",
            ["independent", "mutually exclusive", "identical", "complements only"], "B",
            "Additivity is the disjoint case. Independent events can overlap.",
            subject="P&S", topic="Axioms", diff="Easy", pred="VERY HIGH"),
        mcq("Which sort is stable in its usual textbook form?",
            ["Heapsort", "Quicksort (plain)", "Mergesort", "Selection sort"], "C",
            "Mergesort is stable; the others generally are not.",
            subject="DSA", topic="Sorting", diff="Easy", pred="HIGH"),
        mcq("A relation in BCNF is necessarily also in",
            ["only 1NF", "2NF and 3NF", "neither 2NF nor 3NF", "4NF only"], "B",
            "BCNF ⇒ 3NF ⇒ 2NF ⇒ 1NF.",
            subject="DBMS", topic="Normal forms", diff="Easy", pred="VERY HIGH"),
        mcq("k-means minimises (with Euclidean means)",
            ["between-cluster sum of squares only",
             "within-cluster sum of squared distances to centroids",
             "classification cross-entropy", "the number of clusters k"], "B",
            "Standard k-means objective.",
            subject="ML", topic="k-means", diff="Easy", pred="HIGH"),
        mcq("DFS uses which abstract structure?",
            ["queue", "stack (or recursion stack)", "priority queue of keys", "union-find only"], "B",
            "DFS = stack; BFS = queue.",
            subject="AI", topic="Search", diff="Easy", pred="VERY HIGH"),
        mcq("The sigmoid function σ(z)=1/(1+e^{−z}) maps R onto",
            ["{0,1}", "(0,1)", "[−1,1]", "R"], "B",
            "Open interval (0,1).",
            subject="ML", topic="Logistic", diff="Easy", pred="HIGH"),
        mcq("If A is orthogonal then A^{−1} equals",
            ["A", "A^T", "−A", "0"], "B",
            "A^T A=I ⇒ A^{−1}=A^T.",
            subject="LA", topic="Orthogonal", diff="Easy", pred="HIGH"),
        mcq("In Python 3, the expression type([1,2]) is",
            ["tuple", "list", "dict", "set"], "B",
            "Square brackets construct a list.",
            subject="DSA", topic="Python", diff="Easy", pred="HIGH"),
        mcq("A 95% Wald confidence interval for a mean uses the quantile",
            ["z_{0.05}", "z_{0.025}", "t_{0.5}", "χ^2_{0.95}"], "B",
            "Two-sided 5% splits into two 2.5% tails.",
            subject="P&S", topic="CI", diff="Moderate", pred="HIGH"),
        mcq("Which is an uninformed search algorithm?",
            ["A*", "Greedy best-first", "BFS", "Hill climbing"], "C",
            "BFS uses no heuristic.",
            subject="AI", topic="Uninformed", diff="Easy", pred="VERY HIGH"),
        mcq("PCA is primarily",
            ["a supervised classifier", "an unsupervised linear dimension reduction",
             "a clustering algorithm identical to k-means", "a relational algebra operator"], "B",
            "PCA maximises captured variance; labels are not used.",
            subject="ML", topic="PCA", diff="Easy", pred="VERY HIGH"),
    ]

    # theme spice on first MCQs
    theme_swaps = {
        "B": [(0, mcq("If A is similar to diag(2,-1,0), then det(A) equals",
                    ["1","0","2","-2"],"B",
                    "Similar matrices share det. Product of eigenvalues is 0.",
                    subject="LA", topic="Eigenvalues", diff="Moderate", pred="VERY HIGH"))],
        "C": [(4, mcq("Leave-one-out CV on n labelled points trains",
                    ["1 model","n models","n-1 models","n^2 models"],"B",
                    "Each point is held out once.",
                    subject="ML", topic="CV", diff="Easy", pred="HIGH")),
              (6, mcq("Gini impurity of a 50-50 node is",
                    ["0","0.5","1","0.25"],"B",
                    "Gini=1-sum p^2=0.5.",
                    subject="ML", topic="Trees", diff="Moderate", pred="HIGH"))],
        "D": [(5, mcq("p <-> q is equivalent to",
                    ["(p->q) AND (q->p)","p OR q","NOT p OR NOT q","p AND NOT q"],"A",
                    "Biconditional is two implications.",
                    subject="AI", topic="Logic", diff="Easy", pred="HIGH")),
              (10, mcq("Iterative deepening DFS with unit costs is",
                    ["incomplete on finite trees","optimal in path cost like BFS",
                     "identical to Dijkstra with negative weights","always incomplete"],"B",
                    "IDDFS inherits BFS optimality on unit costs.",
                    subject="AI", topic="IDDFS", diff="Moderate", pred="HIGH"))],
        "E": [(2, mcq("Worst-case time of insertion sort on n keys is",
                    ["Theta(n)","Theta(n log n)","Theta(n^2)","Theta(1)"],"C",
                    "A reversed array produces quadratic moves.",
                    subject="DSA", topic="Insertion sort", diff="Easy", pred="HIGH")),
              (8, mcq("In Python, (1,2)+(3,) evaluates to",
                    ["(1,2,3)","[1,2,3]","error","(4,)"],"A",
                    "Tuple concatenation.",
                    subject="DSA", topic="Python", diff="Easy", pred="HIGH"))],
        "F": [(1, mcq("If P(A)=0.4, P(B)=0.5, P(A and B)=0.2 then P(A|B) is",
                    ["0.4","0.5","0.2","0.8"],"A",
                    "0.2/0.5=0.4.",
                    subject="P&S", topic="Conditional", diff="Easy", pred="VERY HIGH"))],
        "G": [(3, mcq("A lossless-join but not dependency-preserving split typically forces extra",
                    ["selections","joins to check FDs","renames","roll-ups"],"B",
                    "Split FDs are checked after a join.",
                    subject="DBMS", topic="Decomposition", diff="Difficult", pred="HIGH")),
              (2, mcq("Comparison-sorting worst-case lower bound is",
                    ["Omega(n)","Omega(n log n)","Omega(n^2)","Omega(log n)"],"B",
                    "Decision-tree argument.",
                    subject="DSA", topic="Sorting lower bound", diff="Moderate", pred="HIGH"))],
        "H": [(5, mcq("Which statement is NOT true?",
                    ["Every consistent heuristic is admissible",
                     "Every admissible heuristic is consistent",
                     "h=0 is admissible",
                     "Straight-line distance is admissible for Euclidean length"],"B",
                    "Consistency is strictly stronger than admissibility.",
                    subject="AI", topic="Heuristics", diff="Difficult", pred="HIGH"))],
        "I": [(9, mcq("For X~N(mu,sigma^2), P(|X-mu|<sigma) is about",
                    ["0.50","0.68","0.95","0.99"],"B",
                    "68-95-99.7 rule.",
                    subject="P&S", topic="Normal", diff="Easy", pred="HIGH"))],
        "J": [(6, mcq("In a linear hard-margin SVM, a margin support vector typically has",
                    ["alpha=0","alpha>0","alpha<0","alpha=y"],"B",
                    "Interior points have alpha=0.",
                    subject="ML", topic="SVM", diff="Difficult", pred="HIGH"))],
    }
    for idx, newq in theme_swaps.get(letter, []):
        items[idx] = newq

    # ----- 1-mark MSQ (6) -----
    items += [
        msq("Which matrices are always singular? (One or more.)",
            ["A 3×3 matrix of rank 2", "uu^T for u≠0 in R^3",
             "An orthogonal 2×2 matrix", "The zero n×n matrix"],
            "A;B;D",
            "Rank 2 in 3D is singular. uu^T has rank 1 for u≠0. Orthogonal matrices are invertible. Zero is singular.",
            subject="LA", topic="Rank", diff="Moderate", pred="HIGH"),
        msq("Which statements about independent events A,B with 0<P(A),P(B)<1 are true? (One or more.)",
            ["P(A∩B)=P(A)P(B)", "P(A|B)=P(A)", "A and B are disjoint", "P(A∪B)=P(A)+P(B)−P(A)P(B)"],
            "A;B;D",
            "Independence is the product rule, not disjointness.",
            subject="P&S", topic="Independence", diff="Moderate", pred="VERY HIGH"),
        msq("Which of the following are linear time in n for an array of n keys? (One or more.)",
            ["Finding the minimum", "Building a histogram of bytes",
             "Comparison sorting in the worst case", "Reversing the array"],
            "A;B;D",
            "Comparison sorting is Ω(n log n) worst case.",
            subject="DSA", topic="Complexity", diff="Moderate", pred="HIGH"),
        msq("Select all true statements. (One or more.)",
            ["Every BCNF relation is in 3NF",
             "Every 3NF relation is in BCNF",
             "A dependency-preserving BCNF decomposition need not exist",
             "Lossless-join and dependency preservation can conflict"],
            "A;C;D",
            "3NF is weaker than BCNF. Classic schema-design tension.",
            subject="DBMS", topic="Normal forms", diff="Difficult", pred="HIGH"),
        msq("For squared-error linear regression with an intercept, which are true? (One or more.)",
            ["The residual vector is orthogonal to the column space of the design matrix",
             "The hat matrix H=X(X^T X)^{−1}X^T is idempotent when X has full column rank",
             "Adding a useless feature never changes training MSE",
             "Ridge uses X^T X+λI"],
            "A;B;D",
            "Extra features can only decrease training MSE (or leave it unchanged), not increase it; C is false as stated because it says 'never changes'. Wait: 'never changes' is false. Correct are A,B,D.",
            subject="ML", topic="Regression", diff="Difficult", pred="HIGH"),
        msq("Which heuristics are admissible for shortest-path costs on a map? (One or more.)",
            ["h=0", "straight-line distance to the goal (if costs are Euclidean lengths)",
             "twice the true remaining cost", "h(n)=true remaining cost"],
            "A;B;D",
            "Admissible: 0 ≤ h ≤ h*. Twice the truth overestimates.",
            subject="AI", topic="A*", diff="Moderate", pred="VERY HIGH"),
    ]

    # ----- 1-mark NAT (7) -----
    items += [
        nat(f"det([[{a},0],[0,{b}]]) equals _____.",
            a * b, "Diagonal determinant is the product.",
            subject="LA", topic="Determinant", diff="Easy", pred="HIGH"),
        nat(f"X~Bernoulli({p}). Var(X) equals _____ (two decimals if needed).",
            float(f"{p*(1-p):.2f}"), "p(1-p).",
            subject="P&S", topic="Bernoulli", diff="Easy", pred="HIGH"),
        nat(f"Binary search worst-case comparisons on a sorted array of {2**n} keys is _____ (iteration bound of the usual algorithm, about n+1).",
            n + 1, f"log2({2**n})+1 = {n}+1.",
            subject="DSA", topic="Binary search", diff="Easy", pred="HIGH"),
        nat("Number of candidate keys of R(A,B) with F={A→B} is _____.",
            1, "Only A is a candidate key (A^+ = AB). B is not.",
            subject="DBMS", topic="Keys", diff="Easy", pred="HIGH"),
        nat("Entropy in bits of a fair binary label is _____.",
            1, "−2*(1/2 log2 1/2)=1.",
            subject="ML", topic="Entropy", diff="Easy", pred="VERY HIGH"),
        nat(f"f(x)=x^2 on R. Number of critical points is _____.",
            1, "f'=2x=0 only at 0.",
            subject="Calc", topic="Critical points", diff="Easy", pred="HIGH"),
        nat("In a chain Bayes net A→B→C, number of edges is _____.",
            2, "Two directed edges.",
            subject="AI", topic="Bayes net", diff="Easy", pred="MEDIUM"),
    ]

    # ----- 2-mark MCQ (11) -----
    items += [
        mcq("Let P be a real projector, P^2=P. Then the only possible eigenvalues are",
            ["±1", "0 and 1", "0 only", "any real"], "B",
            "λ^2=λ.",
            subject="LA", topic="Idempotent", diff="Moderate", pred="VERY HIGH"),
        mcq("X~Exp(λ), memoryless. P(X>s+t | X>s) equals",
            ["P(X>s)", "P(X>t)", "P(X>s+t)", "e^{λt}"], "B",
            "Definition of memorylessness.",
            subject="P&S", topic="Exponential", diff="Moderate", pred="HIGH"),
        mcq("Expected number of comparisons of randomised quicksort on n distinct keys is",
            ["Θ(n)", "Θ(n log n)", "Θ(n^2)", "Θ(log n)"], "B",
            "Random pivot restores the average n log n bound.",
            subject="DSA", topic="Quicksort", diff="Moderate", pred="VERY HIGH"),
        mcq("σ_{B=5}(π_{A,B}(R)) equals",
            ["π_{A,B}(σ_{B=5}(R))", "π_A(R)", "R ⋈ R", "σ_{A=5}(R)"], "A",
            "Selection on an attribute that survived projection commutes in this way.",
            subject="DBMS", topic="RA", diff="Moderate", pred="HIGH"),
        mcq("Ridge vs ordinary least squares, λ>0:",
            ["ridge coefficients are shrunk toward 0",
             "ridge always has larger training MSE and larger test MSE",
             "ridge ignores y",
             "ridge is identical to PCA"], "A",
            "Shrinkage. Test MSE may improve; training MSE is typically larger.",
            subject="ML", topic="Ridge", diff="Moderate", pred="VERY HIGH"),
        mcq("Variable elimination on a discrete Bayes net is exponential in",
            ["only the number of evidence nodes",
             "the size of the largest factor created (treewidth)",
             "only the number of query nodes",
             "always the number of edges only"], "B",
            "Treewidth governs exact inference.",
            subject="AI", topic="VE", diff="Difficult", pred="HIGH"),
        mcq(f"lim_{{x→0}} ({a}x)/sin x equals",
            [str(a), "0", "1", "∞"], "A",
            f"a · lim x/sin x = {a}.",
            subject="Calc", topic="Limit", diff="Moderate", pred="HIGH"),
        mcq("A hard-margin linear SVM training problem is feasible when the data are",
            ["linearly separable", "not linearly separable", "in 1D only", "unlabelled"], "A",
            "Hard margin requires separability.",
            subject="ML", topic="SVM", diff="Moderate", pred="HIGH"),
        mcq("In a B+ tree of order m (max m children), a node other than root has at least",
            ["1 child", "ceil(m/2) children (typical formulation)", "m+1 children", "n children"], "B",
            "B-tree fill factor.",
            subject="DBMS", topic="Indexing", diff="Difficult", pred="MEDIUM"),
        mcq("Which is TRUE of gradient descent on a differentiable convex function with a suitable fixed step?",
            ["every limit point is a global minimiser",
             "it always diverges",
             "it requires second derivatives",
             "it is identical to Newton's method"], "A",
            "Convex + vanishing gradient ⇒ global min. Newton uses Hessians.",
            subject="Calc", topic="Optimisation", diff="Difficult", pred="HIGH"),
        mcq("Hashing with chaining, simple uniform hashing, load factor α: unsuccessful search is",
            ["Θ(α) expected", "Θ(n) expected always", "Θ(1) worst case", "Θ(log n) worst case"], "A",
            "Expected chain length is α.",
            subject="DSA", topic="Hashing", diff="Moderate", pred="HIGH"),
    ]

    # ----- 2-mark MSQ (8) -----
    items += [
        msq("Let A be real n×n. Which imply that 0 is an eigenvalue? (One or more.)",
            ["det(A)=0", "rank(A)<n", "A is orthogonal", "the columns of A are linearly dependent"],
            "A;B;D",
            "Orthogonal ⇒ det ±1.",
            subject="LA", topic="Eigenvalues", diff="Moderate", pred="HIGH"),
        msq("Which families have variance equal to the mean? (One or more.)",
            ["Poisson(λ)", "Bernoulli(p) for all p", "Exponential(λ)", "Binomial(n,p) when p=1 only? wait"],
            "A",
            "Only Poisson among the clean options. Bernoulli var=p(1-p) equals p iff p=0. Exponential mean 1/λ, var 1/λ^2. I'll replace this item.",
            subject="P&S", topic="Poisson", diff="Moderate", pred="MEDIUM"),
        msq("Select the divide-and-conquer algorithms. (One or more.)",
            ["Mergesort", "Binary search", "Insertion sort", "Quicksort"],
            "A;B;D",
            "Insertion sort is incremental, not D&C.",
            subject="DSA", topic="D&C", diff="Easy", pred="HIGH"),
        msq("SQL three-valued logic: which evaluate to UNKNOWN? (One or more.)",
            ["NULL = 5", "NULL = NULL", "5 = 5", "NULL IS NULL"],
            "A;B",
            "IS NULL is the predicate that returns TRUE. Equality to NULL is UNKNOWN.",
            subject="DBMS", topic="SQL", diff="Moderate", pred="HIGH"),
        msq("Which reduce overfitting risk, all else equal? (One or more.)",
            ["Increase λ in ridge", "Increase tree depth without pruning",
             "Use more i.i.d. training data", "Use k-fold CV to choose capacity"],
            "A;C;D",
            "Deeper unpruned trees overfit.",
            subject="ML", topic="Bias-variance", diff="Moderate", pred="VERY HIGH"),
        msq("Which search algorithms are optimally efficient in the sense of A* (expand every node with f < C*) given a consistent h? (One or more.)",
            ["A* graph search with consistent h", "DFS", "Uniform-cost search, which is A* with h=0",
             "Greedy best-first"],
            "A;C",
            "UCS is A* with zero heuristic, hence consistent.",
            subject="AI", topic="A*", diff="Difficult", pred="HIGH"),
        msq("For f(x)=x^3−x, which are true? (One or more.)",
            ["local max at x=−1/√3", "local min at x=1/√3", "f''(0)=0", "no global max on R"],
            "A;B;C;D",
            "f'=3x^2−1, f''=6x. Cubic → ±∞.",
            subject="Calc", topic="Maxima", diff="Difficult", pred="HIGH"),
        msq("Valid observations about PCA + a linear classifier. (One or more.)",
            ["Projecting to top PCs can drop a direction that is useful for labels",
             "PCs are unsupervised",
             "Orthogonal PCs are uncorrelated in the projected coordinates",
             "PCA always increases kNN accuracy"],
            "A;B;C",
            "PCA ignores Y, so it can hurt supervised tasks.",
            subject="XOVER", topic="PCA+ML", diff="Difficult", pred="HIGH"),
    ]
    # fix Poisson MSQ to be clean
    items[-7] = msq("Which statements are true? (One or more.)",
                    ["If X~Poisson(λ) then E[X]=Var(X)=λ",
                     "If X~Exp(λ) then E[X]=1/λ and Var(X)=1/λ^2",
                     "If X~N(μ,σ^2) then P(X<μ)=1/2",
                     "If X~Uniform(0,1) then Var(X)=1/4"],
                    "A;B;C",
                    "Uniform(0,1) variance is 1/12, not 1/4.",
                    subject="P&S", topic="Distributions", diff="Moderate", pred="VERY HIGH")

    # ----- 2-mark NAT (11) -----
    items += [
        nat(f"Rank of the {n}×{n} all-ones matrix is _____.",
            1, "All columns equal.",
            subject="LA", topic="Rank", diff="Easy", pred="HIGH"),
        nat(f"X~N(0,1). E[X^2] equals _____.",
            1, "Variance is 1 and mean 0 so E[X^2]=1.",
            subject="P&S", topic="Normal", diff="Moderate", pred="HIGH"),
        nat(f"Number of inversions in the permutation ({n}, {n-1}, ..., 1) is _____.",
            n * (n - 1) // 2, "Every pair is inverted: C(n,2).",
            subject="DSA", topic="Inversions", diff="Moderate", pred="HIGH"),
        nat("R(A,B,C), F={A→B,B→C}. Number of attributes in A^+ is _____.",
            3, "A→B→C so A^+=ABC.",
            subject="DBMS", topic="Closure", diff="Easy", pred="VERY HIGH"),
        nat("Points (0,0),(2,2). OLS slope with intercept is _____.",
            1, "(2-0)/(2-0)=1.",
            subject="ML", topic="Regression", diff="Easy", pred="HIGH"),
        nat("Minimax: max root, children terminal values 4 and a min-node of {1,7}. Root value is _____.",
            4, "min(1,7)=1, max(4,1)=4.",
            subject="AI", topic="Minimax", diff="Moderate", pred="HIGH"),
        nat(f"lim_{{x→∞}} ({a}x^2+1)/({b}x^2+3) equals _____ (round to two decimals if needed).",
            float(f"{a/b:.2f}") if a / b != int(a / b) else a // b,
            f"Ratio of leading coefficients {a}/{b}.",
            subject="Calc", topic="Limit", diff="Easy", pred="HIGH"),
        nat("k-fold CV with k=4 and 40 points: training size per fold is _____.",
            30, "Hold out 10.",
            subject="ML", topic="CV", diff="Easy", pred="HIGH"),
        nat(f"Cov(X,X) where Var(X)={lam} equals _____.",
            lam, "Cov(X,X)=Var(X).",
            subject="P&S", topic="Covariance", diff="Easy", pred="HIGH"),
        nat("A 2×2 rotation by 90° has trace _____.",
            0, "cos90=0, trace=0+0.",
            subject="LA", topic="Orthogonal", diff="Moderate", pred="HIGH"),
        nat("Number of edges in a complete binary tree with 7 nodes is _____.",
            6, "A tree on n nodes has n−1 edges.",
            subject="DSA", topic="Trees", diff="Easy", pred="HIGH"),
    ]

    # Theme replacements for variety
    if letter == "B":
        items[20] = nat("Eigenvalues of [[4,1],[0,1]] sum to _____.", 5, "Trace=5.",
                        subject="LA", topic="Eigen", diff="Easy", pred="VERY HIGH")
    if letter == "F":
        items[21] = nat("P(X=0) for X~Poisson(0) is _____.", 1, "e^0=1.",
                        subject="P&S", topic="Poisson", diff="Easy", pred="MEDIUM")
    if letter == "I":
        items[24] = nat("E[X] for X uniform on {1,2,3,4,5} is _____.", 3, "Mean of 1..5 is 3.",
                        subject="P&S", topic="Discrete uniform", diff="Easy", pred="HIGH")

    for i, it in enumerate(items):
        it.setdefault("pred", "HIGH")
        it.setdefault("diff", "Moderate")
        it["sid"] = f"{letter}-{i+11}"
        it["marks"] = 1 if i < 25 else 2
    assert len(items) == 55, len(items)
    return items


def make_paper(letter):
    seed = ord(letter)
    ga = ga_block(seed)
    core = paper_core(letter, seed)
    qs = ga + core
    assert len(qs) == 65
    for i, q in enumerate(qs, 1):
        q["num"] = i
    return {
        "letter": letter,
        "theme": THEMES[letter],
        "questions": qs,
    }


def all_papers():
    return [make_paper(L) for L in "ABCDEFGHIJ"]
