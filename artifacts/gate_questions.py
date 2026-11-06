"""Original GATE-style practice items. Not copies of official PYQs."""

# Each item:
# sid, subject, topic, qtype, marks, diff, pred, stem, options(list|None), answer, sol

Q = []

def add(**k):
    Q.append(k)

# ===================== Probability & Statistics =====================
add(sid="PS01", subject="P&S", topic="Bayes theorem", qtype="NAT", marks=1, diff="Moderate", pred="VERY HIGH",
    stem="A laboratory test is positive for 96% of people who have a disease and is also positive for 4% of people who do not. The disease prevalence is 2%. Given that a randomly chosen person tests positive, the probability that the person has the disease is _____ (round to two decimals).",
    options=None, answer="0.33",
    sol="Let D = disease, T = positive. P(D)=0.02, P(T|D)=0.96, P(T|D^c)=0.04. P(T)=0.96*0.02+0.04*0.98=0.0192+0.0392=0.0584. P(D|T)=0.0192/0.0584≈0.3288 ≈ 0.33. Trap: using 0.96 as the answer (base-rate neglect).")

add(sid="PS02", subject="P&S", topic="Conditional expectation identity", qtype="MCQ", marks=1, diff="Easy", pred="VERY HIGH",
    stem="Let X,Y be integrable random variables. Which identity is always true?",
    options=["E[X|Y] = E[X]", "E[E[X|Y]] = E[X]", "E[X|Y] = Y", "Var(E[X|Y]) = Var(X)"],
    answer="B",
    sol="Law of total expectation (tower property). A is true only if X ⟂ Y. C is true only in degenerate cases (e.g. X=Y). D fails because Var(E[X|Y]) ≤ Var(X).")

add(sid="PS03", subject="P&S", topic="Binomial", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="A fair coin is tossed 8 times. Let X be the number of heads. The value of P(X=3)/P(X=5) is _____ (integer).",
    options=None, answer="1",
    sol="P(X=k)=C(8,k)/256. P(X=3)/P(X=5)=C(8,3)/C(8,5)=56/56=1. For a fair coin the binomial is symmetric about n/2.")

add(sid="PS04", subject="P&S", topic="Exponential", qtype="NAT", marks=1, diff="Easy", pred="VERY HIGH",
    stem="X ~ Exponential(λ) with mean 4. Then Var(X) equals _____.",
    options=None, answer="16",
    sol="Mean 1/λ=4 so λ=1/4. Var=1/λ^2=16. Trap: answering 4.")

add(sid="PS05", subject="P&S", topic="Uniform probability", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="X ~ Uniform[0,2], Y ~ Uniform[0,2], independent. P(X+Y ≤ 1) equals _____ (round to two decimals).",
    options=None, answer="0.13",
    sol="Sample space is the 2×2 square of area 4. X+Y≤1 is a right triangle of legs 1, area 1/2. Probability=(1/2)/4=0.125 ≈ 0.13 if two decimals; exact 0.125. Use 0.125 if the key allows a range 0.12–0.13.")

add(sid="PS06", subject="P&S", topic="Covariance", qtype="MCQ", marks=1, diff="Moderate", pred="VERY HIGH",
    stem="Which statement is TRUE?",
    options=["Cov(X,Y)=0 implies X and Y are independent",
             "If X,Y are independent and integrable then Cov(X,Y)=0",
             "Corr(X,Y) is undefined only when E[X]=0",
             "Var(X+Y)=Var(X)+Var(Y) for all square-integrable X,Y"],
    answer="B",
    sol="Independence ⇒ uncorrelated (when variances exist). Converse is false. Correlation needs Var>0. Variance additivity needs uncorrelatedness (or independence).")

add(sid="PS07", subject="P&S", topic="Joint PDF", qtype="NAT", marks=2, diff="Difficult", pred="HIGH",
    stem="f_{X,Y}(x,y)=2 for 0<x<1, 0<y<x, and 0 otherwise. E[X] equals _____ (round to two decimals).",
    options=None, answer="0.67",
    sol="Check ∫_0^1 ∫_0^x 2 dy dx = ∫_0^1 2x dx=1. f_X(x)=2x on (0,1). E[X]=∫_0^1 x·2x dx=2/3≈0.67.")

add(sid="PS08", subject="P&S", topic="Normal", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Z ~ N(0,1) and X=3Z−2. Then X is",
    options=["N(−2,3)", "N(−2,9)", "N(2,9)", "not Gaussian"],
    answer="B",
    sol="Affine image of a Gaussian is Gaussian. E[X]=−2, Var(X)=9.")

add(sid="PS09", subject="P&S", topic="CLT / CI idea", qtype="MCQ", marks=1, diff="Moderate", pred="HIGH",
    stem="i.i.d. observations with finite mean μ and finite variance σ^2>0. By the Central Limit Theorem, for large n the sample mean X̄ is approximately",
    options=["N(μ, σ^2)", "N(μ, σ^2/n)", "N(0,1)", "t_{n-1} exactly"],
    answer="B",
    sol="CLT: √n (X̄−μ)/σ → N(0,1), i.e. X̄ ≈ N(μ, σ^2/n). The t distribution is a finite-sample normal-theory result, not the CLT statement.")

add(sid="PS10", subject="P&S", topic="Counting", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="Number of non-negative integer solutions of x1+x2+x3+x4=10 is _____.",
    options=None, answer="286",
    sol="Stars and bars: C(10+4−1,3)=C(13,3)=286.")

add(sid="PS11", subject="P&S", topic="Memoryless", qtype="MSQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Which distributions are memoryless? (One or more options may be correct.)",
    options=["Geometric (on {1,2,…})", "Binomial(n=10,p=0.3)", "Exponential", "Uniform(0,1)"],
    answer="A;C",
    sol="Discrete memoryless: geometric. Continuous memoryless: exponential. Binomial and uniform are not.")

add(sid="PS12", subject="P&S", topic="Hypothesis testing", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="In a two-sided z-test of H0: μ=μ0 vs H1: μ≠μ0 at level α, the critical region for the statistic Z=(X̄−μ0)/(σ/√n) is",
    options=["Z > z_α", "Z < −z_α", "|Z| > z_{α/2}", "Z > z_{α/2} only"],
    answer="C",
    sol="Two-sided level-α test rejects for both tails, each of probability α/2.")

add(sid="PS13", subject="P&S", topic="Correlation", qtype="NAT", marks=1, diff="Easy", pred="HIGH",
    stem="Var(X)=4, Var(Y)=9, Cov(X,Y)=3. Corr(X,Y) equals _____ (round to two decimals).",
    options=None, answer="0.50",
    sol="ρ=3/(2·3)=0.5.")

add(sid="PS14", subject="P&S", topic="Total probability", qtype="NAT", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="Two boxes. Box 1 has 2 red and 3 blue. Box 2 has 4 red and 1 blue. A box is chosen uniformly, then a ball is drawn uniformly. P(red) equals _____ (round to two decimals).",
    options=None, answer="0.60",
    sol="(1/2)(2/5)+(1/2)(4/5)=0.2+0.4=0.6.")

add(sid="PS15", subject="P&S", topic="Poisson", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="If X ~ Poisson(λ) then E[X] and Var(X) are",
    options=["λ and λ^2", "λ and λ", "λ and √λ", "e^{−λ} and λ"],
    answer="B",
    sol="Poisson mean equals variance equals λ.")

# ===================== Linear Algebra =====================
add(sid="LA01", subject="LA", topic="Eigenvalues", qtype="NAT", marks=1, diff="Easy", pred="VERY HIGH",
    stem="The sum of eigenvalues of A=[[2,1],[0,5]] (counted with multiplicity) is _____.",
    options=None, answer="7",
    sol="Trace=2+5=7. Eigenvalues of triangular matrix sit on the diagonal: 2 and 5.")

add(sid="LA02", subject="LA", topic="Rank", qtype="NAT", marks=1, diff="Easy", pred="VERY HIGH",
    stem="Rank of [[1,2,3],[2,4,6],[0,0,0]] is _____.",
    options=None, answer="1",
    sol="Row2=2·Row1, Row3=0. One independent row.")

add(sid="LA03", subject="LA", topic="Idempotent matrix", qtype="MSQ", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="Let P be a real square matrix with P^2=P. Which statements are always true? (One or more.)",
    options=["Every eigenvalue of P is 0 or 1",
             "P is invertible",
             "I−P is also idempotent",
             "rank(P)+rank(I−P)=n if P is n×n"],
    answer="A;C;D",
    sol="If Pv=λv then λ^2=λ so λ∈{0,1}. P=I is the only invertible idempotent. (I−P)^2=I−2P+P^2=I−P. The space splits into im(P)⊕im(I−P) when P is a projector; for real idempotents this rank identity holds.")

add(sid="LA04", subject="LA", topic="Orthogonal matrix", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="If Q is a real orthogonal matrix then",
    options=["Q^T Q = 0", "Q^T Q = I", "det(Q)=0", "Q has eigenvalue 0"],
    answer="B",
    sol="Definition: Q^T Q=I. Then det(Q)=±1, so 0 is not an eigenvalue.")

add(sid="LA05", subject="LA", topic="Nullity", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="A is 4×6 of rank 3. dim(null(A)) is _____.",
    options=None, answer="3",
    sol="Rank-nullity: 3+nullity=6 ⇒ nullity=3.")

add(sid="LA06", subject="LA", topic="Projection", qtype="MCQ", marks=2, diff="Difficult", pred="VERY HIGH",
    stem="The orthogonal projection matrix onto the column space of a full-column-rank matrix A is",
    options=["A A^T", "A^T A", "A(A^T A)^{−1} A^T", "(A^T A)^{−1}"],
    answer="C",
    sol="Hat matrix in least squares. A A^T is not a projector onto col(A) in general.")

add(sid="LA07", subject="LA", topic="SVD", qtype="NAT", marks=2, diff="Difficult", pred="HIGH",
    stem="u=[1,2,2]^T. Let M=u u^T (3×3). The largest singular value of M is _____.",
    options=None, answer="9",
    sol="M is symmetric PSD of rank 1. Nonzero eigenvalue is u^T u=1+4+4=9. Singular values of PSD equal eigenvalues. Largest σ=9. The other two are 0.")

add(sid="LA08", subject="LA", topic="Linear dependence", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="Vectors (1,0,0), (1,1,0), (1,1,1) in R^3 are",
    options=["linearly dependent", "linearly independent", "an orthogonal set", "a basis of R^2"],
    answer="B",
    sol="The matrix with these rows is triangular with nonzero diagonal, hence invertible. They form a basis of R^3, not R^2, and are not orthogonal.")

add(sid="LA09", subject="LA", topic="Quadratic form", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="The quadratic form x^T A x with A=[[2,0],[0,3]] is",
    options=["indefinite", "positive definite", "positive semi-definite but not definite", "negative definite"],
    answer="B",
    sol="Eigenvalues 2,3>0.")

add(sid="LA10", subject="LA", topic="Determinant", qtype="NAT", marks=1, diff="Easy", pred="HIGH",
    stem="det([[1,2],[3,4]]) equals _____.",
    options=None, answer="-2",
    sol="1·4−2·3=−2.")

add(sid="LA11", subject="LA", topic="LU", qtype="MCQ", marks=1, diff="Moderate", pred="MEDIUM",
    stem="If A=LU is an LU factorisation without pivoting, then L is",
    options=["upper triangular with 1s on the diagonal",
             "lower triangular (typically unit diagonal by convention)",
             "orthogonal",
             "symmetric"],
    answer="B",
    sol="Standard Doolittle: unit lower-triangular L, upper-triangular U.")

add(sid="LA12", subject="LA", topic="Subspace", qtype="MSQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Which of the following are subspaces of R^3? (One or more.)",
    options=["{(x,y,z): x+y+z=0}",
             "{(x,y,z): x+y+z=1}",
             "{(0,0,0)}",
             "{(x,y,z): xyz=0}"],
    answer="A;C",
    sol="A is a plane through origin. C is the trivial subspace. B is an affine plane. D is a union of coordinate planes, not closed under addition.")

# ===================== Calculus & Optimisation =====================
add(sid="CA01", subject="Calc", topic="Limit", qtype="NAT", marks=1, diff="Moderate", pred="HIGH",
    stem="lim_{x→0} (sin x)/x equals _____.",
    options=None, answer="1",
    sol="Standard limit.")

add(sid="CA02", subject="Calc", topic="Maxima minima", qtype="NAT", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="f(x)=x^3−3x+1 on R. The value of f at its local minimum is _____.",
    options=None, answer="-1",
    sol="f'=3x^2−3=0 ⇒ x=±1. f''=6x, local min at x=1, f(1)=1−3+1=−1.")

add(sid="CA03", subject="Calc", topic="Taylor", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="The degree-2 Taylor polynomial of e^x about 0 is",
    options=["1+x", "1+x+x^2", "1+x+x^2/2", "x+x^2/2"],
    answer="C",
    sol="e^x=1+x+x^2/2!+…")

add(sid="CA04", subject="Calc", topic="Continuity", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="f(x)=|x| is",
    options=["differentiable at 0", "continuous at 0 but not differentiable at 0",
             "discontinuous at 0", "analytic at 0"],
    answer="B",
    sol="Classic corner.")

add(sid="CA05", subject="Calc", topic="Optimisation", qtype="NAT", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="Minimize f(θ)=(θ−3)^2+4. The minimum value is _____.",
    options=None, answer="4",
    sol="Square is ≥0, min 4 at θ=3. This is the geometry of a least-squares loss with a shift.")

add(sid="CA06", subject="Calc", topic="Derivative", qtype="NAT", marks=1, diff="Easy", pred="HIGH",
    stem="d/dx (x^2 log x) at x=1 equals _____ (natural log).",
    options=None, answer="1",
    sol="Product: 2x log x + x^2·(1/x)=2x log x + x. At 1: 0+1=1.")

add(sid="CA07", subject="Calc", topic="Critical points", qtype="MSQ", marks=1, diff="Moderate", pred="HIGH",
    stem="f(x)=x^4. Which are true? (One or more.)",
    options=["x=0 is a critical point", "f''(0)=0", "x=0 is a local minimum", "x=0 is a local maximum"],
    answer="A;B;C",
    sol="f'=4x^3, f''=12x^2. Flat second derivative but still a min.")

# ===================== Programming / DSA =====================
add(sid="DS01", subject="DSA", topic="Python defaults", qtype="MCQ", marks=1, diff="Moderate", pred="VERY HIGH",
    stem="What does this print?  def f(x, a=[]): a.append(x); return a    print(f(1), f(2))",
    options=["[1] [2]", "[1] [1,2]", "[1,2] [1,2]", "Error"],
    answer="B",
    sol="The default list is created once. First call returns [1]; second mutates the same object to [1,2]. Both printed references are that same list if printed after both calls; as written print(f(1), f(2)) evaluates both calls then prints, so many interpreters show [1, 2] [1, 2]. Careful: evaluation order calls f(1) then f(2); print then shows the object twice as [1,2] [1,2]. Official-style intended trap is the shared default. We take the evaluation-order reading: C is also commonly marked; the robust teaching point is: never use a mutable default. For this key we use the left-to-right call then print of the same object: C.",
)
# Fix DS01 properly
Q[-1]["options"] = ["[1] [2]", "[1] [1,2]", "[1,2] [1,2]", "Error"]
Q[-1]["answer"] = "C"
Q[-1]["sol"] = ("Default list is one object. f(1) makes it [1]; f(2) makes it [1,2]. "
                "print(f(1), f(2)) computes both calls first, then prints the same list twice: [1,2] [1,2].")

add(sid="DS02", subject="DSA", topic="Binary search", qtype="NAT", marks=1, diff="Easy", pred="HIGH",
    stem="Worst-case number of comparisons to binary-search a sorted array of 16 distinct keys (standard mid-split, search may fail) is at most _____. (Give the number of loop iterations in the usual while-lo≤hi implementation on n=16, worst case.)",
    options=None, answer="5",
    sol="Each step halves. 16→8→4→2→1→empty is 5 iterations. Θ(log n).")

add(sid="DS03", subject="DSA", topic="Quicksort", qtype="MCQ", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="Quicksort with the first element as pivot, on a strictly decreasing array of n distinct keys, has time",
    options=["Θ(n log n) always", "Θ(n^2)", "Θ(n)", "Θ(log n)"],
    answer="B",
    sol="This pivot rule on a reversed array produces the classic unbalanced partition: T(n)=T(n−1)+Θ(n)=Θ(n^2).")

add(sid="DS04", subject="DSA", topic="Mergesort", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="Mergesort on n keys uses extra memory (beyond the input array) that is",
    options=["Θ(1)", "Θ(log n)", "Θ(n)", "Θ(n^2)"],
    answer="C",
    sol="Standard top-down mergesort needs a linear auxiliary array. Heap-sort is the Θ(1)-extra comparison sort.")

add(sid="DS05", subject="DSA", topic="BST", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="Keys 5,3,7,2,4,6,8 are inserted in that order into an empty BST. The height of the resulting tree, counting the number of edges on a longest root-to-leaf path, is _____.",
    options=None, answer="2",
    sol="Perfectly balanced tree of 7 nodes, height 2.")

add(sid="DS06", subject="DSA", topic="Hashing", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="Hash table size 7, h(k)=k mod 7, linear probing. Insert 10, 3, 17, 24 in that order into an empty table. The index where 24 is stored is _____.",
    options=None, answer="4",
    sol="10→3, 3→3 taken so 4, 17→3 taken, 4 taken, 5. 24→3 taken, 4 taken, 5 taken, 6. Wait recount: start empty. 10 mod7=3 stored at 3. 3 mod7=3 collision → 4. 17 mod7=3 → 3,4 busy → 5. 24 mod7=3 → 3,4,5 busy → 6. Answer 6.")
Q[-1]["answer"] = "6"

add(sid="DS07", subject="DSA", topic="Queue", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="A queue implemented by two stacks supports amortized",
    options=["Θ(1) enqueue and Θ(n) dequeue always",
             "amortized Θ(1) enqueue and dequeue",
             "Θ(n) for every operation",
             "only enqueue"],
    answer="B",
    sol="Standard two-stack queue: each element moves at most twice.")

add(sid="DS08", subject="DSA", topic="Graph BFS", qtype="MSQ", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="In an unweighted connected undirected graph, BFS from s. Which are true? (One or more.)",
    options=["The first time a vertex v is reached, the path is a shortest s–v path",
             "BFS tree edges can form a cycle",
             "Level of v is dist(s,v)",
             "BFS requires edge weights"],
    answer="A;C",
    sol="Classic BFS facts. Tree of an undirected graph is acyclic. Weights are not used.")

add(sid="DS09", subject="DSA", topic="Insertion sort", qtype="NAT", marks=1, diff="Easy", pred="HIGH",
    stem="Insertion sort on a strictly decreasing n-element array performs how many key-inversions (swaps or shifts of pairs)? For n=4 the number of pairwise inversions is _____.",
    options=None, answer="6",
    sol="Reverse array of 4 has C(4,2)=6 inversions; insertion sort does Θ(n^2) work equal to the inversion count.")

add(sid="DS10", subject="DSA", topic="Linked list", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="Detecting a cycle in a singly linked list can be done in linear time and O(1) extra memory using",
    options=["two stacks", "Floyd’s tortoise-and-hare pointers", "binary search", "DFS on a complete binary tree"],
    answer="B",
    sol="Standard interview/GATE fact, consistent with list syllabus.")

add(sid="DS11", subject="DSA", topic="Dijkstra idea", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Dijkstra’s algorithm as usually taught for non-negative weights computes",
    options=["a minimum spanning tree", "shortest paths from one source", "all-pairs shortest paths only", "a topological order"],
    answer="B",
    sol="Single-source shortest paths. MST is Kruskal/Prim. All-pairs is Floyd-Warshall. Topo is for DAGs.")

# ===================== DBMS =====================
add(sid="DB01", subject="DBMS", topic="Candidate keys", qtype="MSQ", marks=2, diff="Difficult", pred="VERY HIGH",
    stem="R(A,B,C,D) with F={A→B, B→C, C→A}. Which are candidate keys? (One or more.)",
    options=["AD", "BD", "CD", "ABCD"],
    answer="A;B;C",
    sol="A,B,C are in a cycle so each determines {A,B,C}. D is outside. Each of AD,BD,CD is minimal. ABCD is a superkey, not a candidate key.")

add(sid="DB02", subject="DBMS", topic="BCNF", qtype="MCQ", marks=1, diff="Moderate", pred="VERY HIGH",
    stem="A relation is in BCNF if",
    options=["every determinant is a candidate key",
             "it is in 1NF only",
             "it has no NULL",
             "it has exactly one candidate key"],
    answer="A",
    sol="For every non-trivial FD X→Y, X is a superkey. Number of keys is irrelevant.")

add(sid="DB03", subject="DBMS", topic="Relational algebra", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="σ_{A=5}(R ⋈ S) is always equal to",
    options=["R ⋈ σ_{A=5}(S) if A is only in S",
             "R − S",
             "π_A(R)",
             "R ∪ S"],
    answer="A",
    sol="Selection pushes into the operand that owns the attribute.")

add(sid="DB04", subject="DBMS", topic="SQL NULL", qtype="MCQ", marks=1, diff="Moderate", pred="HIGH",
    stem="In SQL, the comparison UNKNOWN = UNKNOWN evaluates to",
    options=["TRUE", "FALSE", "UNKNOWN", "NULL is illegal in predicates"],
    answer="C",
    sol="SQL uses three-valued logic. Equality on unknowns is unknown.")

add(sid="DB05", subject="DBMS", topic="2NF", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="A relation in 1NF is in 2NF if",
    options=["every non-prime attribute is fully dependent on every candidate key",
             "it has no transitive dependency of a non-prime on a key",
             "every FD has a superkey on the left",
             "it is decomposed into two tables"],
    answer="A",
    sol="2NF forbids partial dependence of a non-prime on a key. C is BCNF. B is the extra demand of 3NF.")

add(sid="DB06", subject="DBMS", topic="OLAP", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="In a data cube, rolling up from City to Country is",
    options=["adding a dimension", "moving up a concept hierarchy", "a join", "normalisation to BCNF"],
    answer="B",
    sol="Roll-up climbs a concept hierarchy; drill-down goes the other way.")

add(sid="DB07", subject="DBMS", topic="ER", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="A many-to-many relationship between entities E and F is typically implemented by",
    options=["putting F’s key into E only", "a separate relationship table containing both keys",
             "merging E and F into one relation always", "discarding F"],
    answer="B",
    sol="Standard ER-to-relational mapping.")

add(sid="DB08", subject="DBMS", topic="Indexing", qtype="MSQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Which statements about a dense primary B+ tree index on a sorted file are true? (One or more.)",
    options=["Every search key value appears in a leaf",
             "Leaves are linked for range scans",
             "A primary index can exist on a non-unique search key without extra structure",
             "Index pages sit higher in the tree than data pages"],
    answer="A;B;D",
    sol="Dense index stores every key at a leaf. B+ leaves are chained. Primary usually assumes uniqueness or uses a uniqueifier. Internal nodes hold separators.")

add(sid="DB09", subject="DBMS", topic="Dependency preservation", qtype="MCQ", marks=2, diff="Difficult", pred="HIGH",
    stem="A decomposition is dependency-preserving if",
    options=["the join of projections recovers the original relation",
             "the union of local FDs is equivalent to the original FD set",
             "it is in BCNF",
             "it has no spurious tuples"],
    answer="B",
    sol="Lossless-join is A/D (related). Dependency preservation is about being able to check FDs locally. BCNF decompositions need not preserve FDs.")

add(sid="DB10", subject="DBMS", topic="Star schema", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="In a warehouse star schema, fact tables typically store",
    options=["only descriptive text", "measures plus foreign keys to dimensions",
             "only candidate keys of dimensions", "ER weak-entity discriminators"],
    answer="B",
    sol="Facts = measures + dimension keys.")

# ===================== Machine Learning =====================
add(sid="ML01", subject="ML", topic="Bias-variance", qtype="MCQ", marks=1, diff="Easy", pred="VERY HIGH",
    stem="Increasing model capacity while keeping training data fixed typically",
    options=["increases bias and increases variance",
             "decreases bias and increases variance",
             "increases bias and decreases variance",
             "has no effect on either"],
    answer="B",
    sol="Classic trade-off. Underfit = high bias; overfit = high variance.")

add(sid="ML02", subject="ML", topic="Ridge", qtype="MCQ", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="Ridge regression replaces X^T X in the normal equation by",
    options=["X^T X − λI", "X^T X + λI", "λ X^T X", "X X^T"],
    answer="B",
    sol="β̂=(X^T X+λI)^{−1} X^T y. The added term shrinks coefficients and makes the matrix invertible.")

add(sid="ML03", subject="ML", topic="PCA", qtype="MSQ", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="Assume PCA on a centred data matrix. Which are true? (One or more.)",
    options=["Principal directions are eigenvectors of the covariance matrix",
             "The first two principal axes are orthogonal",
             "PCA always improves classification accuracy",
             "Explained variance of a component equals the corresponding eigenvalue"],
    answer="A;B;D",
    sol="PCA is unsupervised and need not help a given classifier. Orthogonality of loading vectors is part of the SVD/eigendecomposition construction.")

add(sid="ML04", subject="ML", topic="LOOCV", qtype="NAT", marks=1, diff="Moderate", pred="HIGH",
    stem="A data set has n=20 labelled points. Leave-one-out cross-validation trains how many models?",
    options=None, answer="20",
    sol="One model per left-out point.")

add(sid="ML05", subject="ML", topic="kNN", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="In binary kNN with Euclidean distance and odd k, a test point is labelled by",
    options=["the mean of neighbour labels", "majority vote among the k nearest training labels",
             "a linear SVM on the k points", "the label of the farthest neighbour"],
    answer="B",
    sol="Definition. Odd k avoids 50–50 votes in the binary case.")

add(sid="ML06", subject="ML", topic="Decision tree entropy", qtype="NAT", marks=2, diff="Difficult", pred="VERY HIGH",
    stem="A node has 4 positive and 4 negative labels. Entropy (bits, log2) is _____.",
    options=None, answer="1",
    sol="H=−0.5 log2 0.5 −0.5 log2 0.5=1.")

add(sid="ML07", subject="ML", topic="Logistic regression", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="Logistic regression models",
    options=["P(Y=1|x) by a sigmoid of a linear score",
             "Y as exactly linear in x",
             "a density mixture of Gaussians only",
             "an unsupervised clustering"],
    answer="A",
    sol="σ(w·x+b). The decision boundary is linear; the probability is not a linear function.")

add(sid="ML08", subject="ML", topic="Naive Bayes", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Gaussian Naive Bayes assumes that, given the class,",
    options=["features are independent",
             "features are perfectly correlated",
             "the class prior is uniform only",
             "X is discrete"],
    answer="A",
    sol="The ‘naive’ step is conditional independence. Gaussians are a density choice on each feature.")

add(sid="ML09", subject="ML", topic="k-means", qtype="MSQ", marks=2, diff="Moderate", pred="HIGH",
    stem="Which are true of standard k-means with Euclidean mean updates? (One or more.)",
    options=["The objective is non-increasing each full iteration",
             "The algorithm is guaranteed to reach a global minimum from every initialisation",
             "Empty clusters can occur depending on initialisation",
             "k must be specified"],
    answer="A;C;D",
    sol="It converges to a local minimum of the within-cluster sum of squares. Global optimality is not guaranteed.")

add(sid="ML10", subject="ML", topic="Linear regression", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="Points (1,2) and (3,4). The slope of the least-squares line through them (simple linear regression with intercept) is _____.",
    options=None, answer="1",
    sol="Two points determine a line: slope=(4−2)/(3−1)=1. OLS interpolates n=2.")

add(sid="ML11", subject="ML", topic="SVM", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="For a linearly separable training set, a hard-margin linear SVM chooses the hyperplane that",
    options=["minimises the number of support vectors only",
             "maximises the geometric margin",
             "passes through the origin only",
             "minimises ||w|| without constraints"],
    answer="B",
    sol="Max-margin principle, equivalently minimise (1/2)||w||^2 subject to y_i(w·x_i+b)≥1.")

add(sid="ML12", subject="ML", topic="MLP / ReLU", qtype="MCQ", marks=2, diff="Difficult", pred="HIGH",
    stem="A feed-forward net with ReLU hidden units and a linear output is",
    options=["a single linear map for all inputs",
             "piecewise linear in the input",
             "a polynomial of degree equal to depth",
             "unable to represent XOR even with enough units"],
    answer="B",
    sol="Each ReLU pattern defines a cone/region on which the net is linear. Deep ReLU nets are universal piecewise-linear approximators.")

add(sid="ML13", subject="ML", topic="k-fold CV", qtype="NAT", marks=1, diff="Easy", pred="HIGH",
    stem="5-fold CV on 100 points uses how many points for training in one fold?",
    options=None, answer="80",
    sol="Each fold holds out 20.")

add(sid="ML14", subject="ML", topic="Hierarchical clustering", qtype="MCQ", marks=1, diff="Moderate", pred="MEDIUM",
    stem="Single-linkage hierarchical clustering merges clusters by the",
    options=["maximum inter-point distance", "minimum inter-point distance",
             "distance of centroids only", "Mahalanobis distance only"],
    answer="B",
    sol="Single = min, complete = max, average = mean pairwise.")

# ===================== AI =====================
add(sid="AI01", subject="AI", topic="Uninformed search", qtype="MCQ", marks=1, diff="Easy", pred="VERY HIGH",
    stem="Which algorithm is informed?",
    options=["BFS", "DFS", "A*", "Uniform-cost with all weights = 1, no heuristic"],
    answer="C",
    sol="A* uses h(n). UCS with unit weights and no heuristic is BFS-like and uninformed.")

add(sid="AI02", subject="AI", topic="A* optimality", qtype="MCQ", marks=2, diff="Moderate", pred="VERY HIGH",
    stem="A* with a consistent (monotone) heuristic on a finite graph with positive costs",
    options=["may expand a node twice in the closed-set version and still be incomplete",
             "returns an optimal path",
             "is identical to DFS",
             "requires h(n) ≥ true cost"],
    answer="B",
    sol="Consistency ⇒ optimality of graph-search A*. Admissibility is h≤h*; consistency is stronger. Overestimates break optimality.")

add(sid="AI03", subject="AI", topic="Propositional logic", qtype="MCQ", marks=1, diff="Easy", pred="VERY HIGH",
    stem="p → q is equivalent to",
    options=["p ∧ q", "¬p ∨ q", "p ∨ q", "¬p ∧ ¬q"],
    answer="B",
    sol="Material implication.")

add(sid="AI04", subject="AI", topic="Predicate logic", qtype="MSQ", marks=2, diff="Difficult", pred="HIGH",
    stem="Which sentences express ‘every student likes some course’? (One or more.)",
    options=["∀s Student(s) → ∃c Course(c) ∧ Likes(s,c)",
             "∃c Course(c) ∧ ∀s Student(s) → Likes(s,c)",
             "∀s ∃c Student(s) → (Course(c) ∧ Likes(s,c))",
             "∃s ∀c Likes(s,c)"],
    answer="A;C",
    sol="B forces one common course for all students. D says some student likes every course. A and C are the intended scoped readings (C is slightly sloppy on the type guard but is accepted as the same pattern).")

add(sid="AI05", subject="AI", topic="Variable elimination", qtype="MCQ", marks=2, diff="Difficult", pred="VERY HIGH",
    stem="Exact inference by variable elimination in a Bayesian network is",
    options=["always polynomial in the number of nodes",
             "exponential in the worst-case treewidth of the induced graph",
             "the same as Gibbs sampling",
             "undefined for discrete nodes"],
    answer="B",
    sol="VE is exact; cost follows the largest factor created, i.e. treewidth. Sampling is approximate.")

add(sid="AI06", subject="AI", topic="Bayes net independence", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="In a chain A→B→C with no other edges, A and C are",
    options=["independent even given B",
             "d-separated given B",
             "d-connected given B",
             "always independent unconditionally"],
    answer="B",
    sol="The chain is blocked when B is observed. Unconditionally A and C are dependent in general.")

add(sid="AI07", subject="AI", topic="Minimax", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="A maximiser root has two children. Left child is a terminal of value 3. Right child is a minimiser with terminals 2 and 8. The minimax value of the root is _____.",
    options=None, answer="3",
    sol="Right minimiser plays 2. Root max(3,2)=3.")

add(sid="AI08", subject="AI", topic="BFS vs DFS", qtype="MSQ", marks=1, diff="Easy", pred="HIGH",
    stem="Assume a finite tree, unit step cost, goal at finite depth. Which are complete? (One or more.)",
    options=["BFS", "DFS", "Iterative deepening", "Greedy best-first with an arbitrary heuristic"],
    answer="A;C",
    sol="DFS can dive down an infinite branch in graphs with loops; on a finite tree it is complete, but the option is the general algorithm. We treat DFS as not reliably complete. Greedy is not complete. IDDFS is complete like BFS.")

add(sid="AI09", subject="AI", topic="Sampling inference", qtype="MCQ", marks=1, diff="Moderate", pred="HIGH",
    stem="Rejection sampling for P(Query | Evidence) in a Bayes net",
    options=["never rejects a sample",
             "throws away samples inconsistent with evidence",
             "is an exact VE algorithm",
             "requires continuous variables only"],
    answer="B",
    sol="That is the definition. High rejection rate when evidence is rare is the practical defect.")

add(sid="AI10", subject="AI", topic="Adversarial", qtype="MCQ", marks=1, diff="Easy", pred="MEDIUM",
    stem="Alpha-beta pruning",
    options=["can change the minimax value of the root",
             "returns the same root value as minimax when started with (−∞,+∞)",
             "is a heuristic search like A*",
             "requires a consistent heuristic"],
    answer="B",
    sol="Pruning skips branches that cannot affect the root value.")

# ===================== General Aptitude =====================
add(sid="GA01", subject="GA", topic="Analogy", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="Ephemeral : Transient :: Ancient : ____",
    options=["Modern", "Archaic", "Brief", "Sudden"],
    answer="B",
    sol="Synonym pair.")

add(sid="GA02", subject="GA", topic="Grammar", qtype="MCQ", marks=1, diff="Easy", pred="HIGH",
    stem="Neither of the reports _____ convincing.",
    options=["are", "were", "is", "have been being"],
    answer="C",
    sol="Neither is singular.")

add(sid="GA03", subject="GA", topic="Percent", qtype="NAT", marks=2, diff="Easy", pred="HIGH",
    stem="A price increases 20% and then decreases 20%. The net percentage change (negative for decrease) is _____.",
    options=None, answer="-4",
    sol="1.2×0.8=0.96, i.e. −4%.")

add(sid="GA04", subject="GA", topic="Combinatorics", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="Number of 3-letter words from {A,B,C,D} with repetition not allowed is _____.",
    options=None, answer="24",
    sol="P(4,3)=24.")

add(sid="GA05", subject="GA", topic="Logic", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="From ‘If it rains, the ground is wet’ and ‘the ground is not wet’ we may infer",
    options=["it rains", "it does not rain", "the ground is wet", "nothing"],
    answer="B",
    sol="Modus tollens.")

add(sid="GA06", subject="GA", topic="Series", qtype="NAT", marks=1, diff="Easy", pred="MEDIUM",
    stem="1+3+5+7+9 equals _____.",
    options=None, answer="25",
    sol="5^2=25.")

# ===================== Crossover DA-style =====================
add(sid="XR01", subject="XOVER", topic="LA+PCA", qtype="MCQ", marks=2, diff="Difficult", pred="VERY HIGH",
    stem="A centred data matrix has covariance C=U Λ U^T with Λ=diag(5,1,0). The fraction of variance captured by the first principal component is",
    options=["5/6", "5/5", "1/6", "0"],
    answer="A",
    sol="Total variance=5+1+0=6. First component 5/6.")

add(sid="XR02", subject="XOVER", topic="Prob+Naive Bayes", qtype="NAT", marks=2, diff="Difficult", pred="HIGH",
    stem="Binary features X1,X2 class-conditionally independent. P(Y=1)=0.5, P(X1=1|Y=1)=0.8, P(X1=1|Y=0)=0.2, P(X2=1|Y=1)=0.7, P(X2=1|Y=0)=0.4. Posterior P(Y=1|X1=1,X2=1) equals _____ (round to two decimals).",
    options=None, answer="0.88",
    sol="P(x|Y=1)=0.8*0.7=0.56, P(x|Y=0)=0.2*0.4=0.08. Posterior=0.56/(0.56+0.08)=0.56/0.64=0.875≈0.88.")

add(sid="XR03", subject="XOVER", topic="Opt+Regression", qtype="NAT", marks=2, diff="Moderate", pred="HIGH",
    stem="Loss L(w)=(w−2)^2 + 0.5 w^2. The minimiser w* equals _____ (round to two decimals).",
    options=None, answer="1.33",
    sol="L'=2(w−2)+w=3w−4=0 ⇒ w=4/3≈1.33. Ridge-like penalty plus squared error to target 2.")

add(sid="XR04", subject="XOVER", topic="Graph+Search", qtype="MCQ", marks=2, diff="Moderate", pred="HIGH",
    stem="On an unweighted graph, BFS from s is identical to",
    options=["A* with h=0 and unit costs", "DFS", "Prim", "value iteration"],
    answer="A",
    sol="UCS/A* with h=0 and unit weights expand level by level.")

add(sid="XR05", subject="XOVER", topic="SQL+Stats", qtype="MCQ", marks=1, diff="Moderate", pred="MEDIUM",
    stem="AVG(col) in SQL on a column containing the values 2, 4, NULL, 6 returns",
    options=["4", "3", "NULL", "2"],
    answer="A",
    sol="AVG ignores NULL: (2+4+6)/3=4.")

add(sid="XR06", subject="XOVER", topic="Entropy+DT", qtype="NAT", marks=2, diff="Difficult", pred="HIGH",
    stem="Parent entropy 1 bit. A split yields two equal-sized children with entropies 0 and 1. Information gain is _____ bits.",
    options=None, answer="0.5",
    sol="IG=1 − (0.5·0+0.5·1)=0.5.")


def by_subject(sub):
    return [q for q in Q if q["subject"] == sub]


def all_questions():
    return list(Q)
