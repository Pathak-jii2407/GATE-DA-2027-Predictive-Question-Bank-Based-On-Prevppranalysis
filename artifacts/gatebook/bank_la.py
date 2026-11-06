"""Unique Linear Algebra items."""
from helpers import mcq, msq, nat, uniq


def items():
    o = []
    A = o.append

    A(msq("Subspace", "Which of the following are subspaces of R^3?",
          "{x : x1+x2+x3=0}", "{x : x1+x2+x3=1}", "{0}", "{x : x1 x2=0}",
          "A;C", "Must contain 0 and be closed. Product constraint is not."))
    A(mcq("Subspace", "The set of all 2×2 symmetric real matrices is a subspace of M_2(R) of dimension",
          "2", "3", "4", "1", "B", "a,b,c independent in [[a,b],[b,c]]."))
    A(mcq("Subspace", "Polynomials of degree exactly 3 form",
          "a subspace of P_3", "not a subspace (no 0 of exact degree 3)", "P_2", "R^3",
          "B", "0 has undefined/negative degree."))
    A(nat("Subspace", "Dimension of {x in R^4 : x1=x2, x3=0} is _____.", 2, "Free: x1 and x4."))
    A(mcq("Span", "span{(1,0),(0,1),(1,1)} in R^2 is",
          "a line", "R^2", "{0}", "R^3", "B", "First two already a basis."))
    A(msq("Independence", "In R^3, which sets are linearly independent?",
          "{(1,0,0),(0,1,0)}", "{(1,1,1),(2,2,2)}", "{(1,0,0),(0,1,0),(0,0,1)}", "{(0,0,0),(1,0,0)}",
          "A;C", "Parallel pair and zero vector fail."))
    A(nat("Independence", "Maximum size of a linearly independent set in R^5 is _____.", 5, "Dimension."))
    A(mcq("Basis", "The standard basis of R^n has",
          "n−1 vectors", "n orthonormal vectors", "2n vectors", "infinitely many vectors as a set of size n? n vectors",
          "B", "e1..en."))
    A(mcq("Basis", "Two bases of a finite-dimensional space",
          "can have different cardinalities", "have the same number of vectors", "must be orthogonal", "must contain e1",
          "B", "Dimension is well-defined."))
    A(nat("Dim", "dim(R^{2×3}) as a real vector space is _____.", 6, "6 entries."))
    A(mcq("Sum", "If U,W subspaces, dim(U+W)+dim(U∩W) equals",
          "dim U − dim W", "dim U + dim W", "0", "dim U dim W",
          "B", "Grassmann."))
    A(nat("Sum", "dim U=3, dim W=3, dim(U∩W)=1 in R^5. dim(U+W) is _____.", 5, "3+3−1=5."))
    A(mcq("Direct", "U+W is direct iff",
          "U∩W={0}", "U=W", "dim U=0", "U+W=R^n always",
          "A", "Definition."))

    A(nat("Rank", "Rank of [[1,2,3],[2,4,6],[0,0,0]] is _____.", 1, "Rows 2=2×row1."))
    A(nat("Rank", "Rank of I_4 is _____.", 4, "Full."))
    A(nat("Rank", "Rank of the 5×5 all-ones matrix is _____.", 1, "All columns equal."))
    A(nat("Rank", "Rank of diag(2,0,3,0) is _____.", 2, "Two nonzero pivots."))
    A(nat("Nullity", "A 3×5 matrix of rank 2 has nullity _____.", 3, "5−2."))
    A(nat("Nullity", "A 4×4 invertible matrix has nullity _____.", 0, "Trivial kernel."))
    A(mcq("Rank-nullity", "For A: R^n → R^m, rank(A)+nullity(A) equals",
          "m", "n", "m+n", "rank(A^T)",
          "B", "Domain dimension."))
    A(mcq("Rank transpose", "rank(A) equals",
          "rank(A^T) always", "nullity(A) always", "n always", "0 always",
          "A", "Equal row and column rank."))
    A(nat("Det", "det([[2,1],[0,5]]) is _____.", 10, "10."))
    A(nat("Det", "det([[1,2,3],[0,4,5],[0,0,6]]) is _____.", 24, "Product of diagonal."))
    A(nat("Det", "det(2I_3) is _____.", 8, "2^3."))
    A(mcq("Det product", "det(AB) equals",
          "det A + det B", "det A · det B", "det(A+B)", "tr(AB)",
          "B", "Multiplicativity."))
    A(mcq("Det inverse", "If det A=4 then det(A^{−1}) is",
          "4", "1/4", "−4", "0",
          "B", "Reciprocal."))
    A(nat("Det swap", "Swapping two rows of I_2, the determinant becomes _____.", -1, "Odd permutation."))
    A(mcq("Singular", "A square matrix is singular iff",
          "det ≠ 0", "det = 0", "it is orthogonal", "it is diagonal",
          "B", "Definition."))
    A(nat("Trace", "tr([[1,2],[3,4]]) is _____.", 5, "1+4."))
    A(nat("Trace", "tr(I_7) is _____.", 7, "n."))
    A(mcq("Trace cyclic", "tr(ABC) equals",
          "tr(CAB)", "tr(ACB) always", "det(ABC)", "0",
          "A", "Cyclic property; not all permutations."))
    A(mcq("Eigen", "Eigenvalues of [[0,−1],[1,0]] are",
          "real 1,−1", "± i", "0,0", "2,−2",
          "B", "Rotation by 90°."))
    A(nat("Eigen", "Sum of eigenvalues of [[2,1],[0,5]] (counted with multiplicity) is _____.", 7, "Trace."))
    A(nat("Eigen", "Product of eigenvalues of [[3,0],[1,4]] is _____.", 12, "Det."))
    A(mcq("Eigen real", "A real symmetric matrix has",
          "complex non-real eigenvalues possibly", "real eigenvalues and an orthonormal eigenbasis", "det 0 always", "rank 1",
          "B", "Spectral theorem."))
    A(msq("Eigen projector", "If P^2=P then",
          "eigenvalues of P lie in {0,1}", "I−P is also idempotent", "P is always invertible", "tr(P)=rank(P) for a projector over R",
          "A;B;D", "Only I is invertible among projectors."))
    A(nat("Idempotent", "If P^2=P and Pv=λv, v≠0, then λ(λ−1)=_____.", 0, "λ∈{0,1}."))
    A(mcq("Orthogonal mat", "Real Q is orthogonal iff",
          "Q^T Q=0", "Q^T Q=I", "det Q=0", "0 is an eigenvalue",
          "B", "Preserves inner product."))
    A(nat("Orthogonal det", "If Q is real orthogonal, |det Q| is _____.", 1, "±1."))
    A(mcq("Rotation", "The matrix [[cosθ,−sinθ],[sinθ,cosθ]] is",
          "singular", "orthogonal with det 1", "symmetric for all θ", "nilpotent",
          "B", "SO(2). DA 2026 Q.21 pattern."))
    A(mcq("Rotation power", "M a rotation by 2π/5. M^5 equals",
          "M", "M^2", "I", "0",
          "C", "Order 5."))
    A(mcq("Projector formula", "Orthogonal projector onto col(A) (A full column rank) is",
          "AA^T", "A(A^T A)^{−1} A^T", "A^T A", "(A^T A)^{−1}",
          "B", "Hat matrix."))
    A(msq("Orth projector", "If P is an orthogonal projector then",
          "P^T=P", "P^2=P", "I−P is an orthogonal projector onto the orthogonal complement", "all eigenvalues equal 2",
          "A;B;C", "Symmetric idempotent."))
    A(nat("Proj R2", "Orthogonal projection of (3,4) onto span{(1,0)} is (a,0) with a=_____.", 3, "First coordinate."))
    A(mcq("Quadratic", "x^T diag(2,3) x is",
          "indefinite", "positive definite", "negative definite", "zero",
          "B", "Eigenvalues >0."))
    A(mcq("Quadratic", "x^T [[0,1],[1,0]] x = 2x1 x2 is",
          "positive definite", "indefinite", "negative definite", "a projector",
          "B", "Eigenvalues ±1."))
    A(mcq("Sylvester", "A symmetric matrix is PD iff",
          "all eigenvalues <0", "all leading principal minors >0 (Sylvester) / all eigen >0", "trace=0", "det=0",
          "B", "Criteria."))
    A(nat("PD", "[[2,0],[0,2]] has smallest eigenvalue _____.", 2, "PD."))
    A(mcq("System", "Ax=b has a unique solution for every b iff A is",
          "singular", "square and invertible", "rectangular", "nilpotent",
          "B", "Full rank square."))
    A(mcq("System inf", "Ax=0 for nonzero A of size 3×5 always has",
          "only 0", "a nontrivial kernel (by rank-nullity)", "a unique nonzero solution", "no solution",
          "B", "nullity ≥2."))
    A(mcq("GE", "Gaussian elimination on a generic n×n matrix costs",
          "O(n)", "O(n^2)", "O(n^3)", "O(2^n)",
          "C", "DA 2025 Q.12 is about triangular — generic GE is n^3/3."))
    A(mcq("GE triangular", "GE on an n×n matrix that is already upper triangular involves",
          "O(n^3) eliminations below the diagonal", "no elimination below the diagonal (already U)", "O(n^4)", "inverting via Cramer only",
          "B", "DA 2025 Q.12 pattern: already triangular."))
    A(mcq("LU", "Doolittle LU (no pivoting): L is",
          "unit upper", "unit lower triangular", "orthogonal", "diagonal of eigenvalues",
          "B", "Unit lower."))
    A(nat("LU", "[[2,1],[4,3]] = L U with L unit lower. L_{21} is _____.", 2, "4/2=2."))
    A(mcq("Pivoting", "Partial pivoting is used to",
          "make the matrix symmetric", "avoid tiny pivots / improve stability", "compute SVD", "force orthogonality",
          "B", "Numerical."))
    A(mcq("SVD", "In A=UΣV^T the diagonal of Σ holds",
          "eigenvalues of A (possibly negative)", "singular values (≥0)", "pivots of L", "random numbers",
          "B", "Definition."))
    A(nat("SVD", "Singular values of [[3,0],[0,4]] are 3 and _____.", 4, "Already diagonal PSD."))
    A(nat("SVD rank1", "u=(1,2,2)^T, M=uu^T. Largest singular value of M is _____.", 9, "||u||^2=9."))
    A(mcq("SVD rank", "Number of positive singular values equals",
          "n always", "rank(A)", "nullity", "trace",
          "B", "Rank."))
    A(mcq("Thin SVD", "For a tall full-rank A, the left singular vectors of the nonzero σ's span",
          "ker(A)", "col(A)", "row(A)^⊥", "ker(A^T)^⊥ wait that's col(A) too",
          "B", "Range."))
    A(mcq("Pseudo", "The Moore–Penrose pseudoinverse uses",
          "only det", "reciprocals of nonzero singular values", "LU without Σ", "k-means",
          "B", "A^+ = V Σ^+ U^T."))
    A(nat("Inv 2x2", "Inverse of [[1,1],[0,1]] is [[1,a],[0,1]] with a=_____.", -1, "Shear inverse."))
    A(mcq("Inv product", "(AB)^{−1} equals",
          "A^{−1} B^{−1}", "B^{−1} A^{−1}", "A B", "A^T B^T",
          "B", "Reverse order."))
    A(mcq("Transpose inv", "(A^T)^{−1} equals",
          "A^{−1}", "(A^{−1})^T", "A", "−A^T",
          "B", "Commute."))
    A(nat("Cramer", "[[1,1],[1,2]] x = (1,1)^T. x1 by Cramer is _____.", 1, "det[[1,1],[1,2]]=1, det[[1,1],[1,2]] wait x1=det[[1,1],[1,2]]/1=1."))
    A(mcq("Row eq", "Elementary row operations do not change",
          "the entries", "the row space (up to the same span — actually they change the explicit rows but not the row space)", "the determinant always", "the (1,1) entry",
          "B", "Row space invariant."))
    A(mcq("RREF", "The RREF of an invertible n×n matrix is",
          "0", "I_n", "a single 1", "undefined",
          "B", "Full pivots."))
    A(nat("Pivots", "RREF of [[1,2,3],[2,4,6]] has how many pivots?", 1, "Rank 1."))
    A(mcq("Consistent", "Ax=b is consistent iff b is in",
          "ker(A)", "col(A)", "ker(A^T) always", "row(A) always as a column",
          "B", "Range."))
    A(mcq("Normal eq", "The least-squares problem min ||Ax−b||_2 leads to",
          "A x = b always", "A^T A x = A^T b", "A A^T x = b", "x=0",
          "B", "Normal equations."))
    A(nat("LS", "Fit y=c through data y=1,3. OLS c (no slope) is _____.", 2, "Mean."))
    A(mcq("Hat", "The hat matrix H=A(A^T A)^{−1} A^T satisfies",
          "H^2=0", "H^2=H", "H=I always", "tr H=0 always",
          "B", "Orthogonal projector onto col(A)."))
    A(nat("Hat tr", "For a 10×3 full-column-rank A with intercept+2 predictors, tr(H) is _____.", 3, "tr=rank=p."))
    A(mcq("Similar", "Similar matrices share",
          "all entries", "characteristic polynomial", "eigenvectors", "the (1,1) entry",
          "B", "Same eigenvalues."))
    A(mcq("Diagble", "A matrix is diagonalizable over C iff",
          "it is invertible", "algebraic multiplicity equals geometric for every eigenvalue (minimal poly splits with distinct linear factors)", "det=0", "it is orthogonal",
          "B", "Full eigenspace."))
    A(nat("AM GM", "[[0,1],[0,0]] has eigenvalue 0 with algebraic multiplicity _____.", 2, "Nilpotent Jordan block."))
    A(nat("GM", "Same nilpotent 2×2 block. Geometric multiplicity of 0 is _____.", 1, "Rank 1, nullity 1."))
    A(mcq("Jordan", "A Jordan block of size k for λ has",
          "k independent eigenvectors", "one independent eigenvector", "k distinct eigenvalues", "det I",
          "B", "Defective if k>1."))
    A(mcq("Cayley", "Cayley–Hamilton says",
          "A=0", "p_A(A)=0", "det A=0", "A^T=A",
          "B", "A satisfies its characteristic polynomial."))
    A(nat("CH 2", "A=[[0,−1],[1,−1]] (rotation-ish). Characteristic poly λ^2+λ+1. Then A^2+A+I equals the zero matrix; its (1,1) entry is _____.", 0, "CH."))
    A(mcq("Min poly", "The minimal polynomial divides",
          "any annihilating poly, in particular the characteristic poly", "the determinant only", "n!", "tr A",
          "A", "Definition."))
    A(mcq("Char poly", "p_A(λ)=det(λI−A) is monic of degree",
          "rank(A)", "n for n×n A", "nullity", "1 always",
          "B", "Degree n."))
    A(nat("Char 2", "A=[[1,0],[0,2]]. p_A(λ)=(λ−1)(λ−2). p_A(0) is _____.", 2, "det(−A)=2."))
    A(mcq("Partition", "det of block-diagonal diag(A,B) equals",
          "det A + det B", "det A · det B", "0", "tr A + tr B",
          "B", "Product."))
    A(nat("Block", "diag(I_2, 3) has det _____.", 3, "1·1·3."))
    A(mcq("Kronecker", "If A is m×m and B n×n, A⊗B is",
          "m×n", "mn × mn", "m+n", "1×1",
          "B", "Kronecker size."))
    A(nat("Kron det", "det(A⊗B) for 2×2 A,B is (det A)^n (det B)^m with n=m=2: (det A)^2 (det B)^2. If det A=det B=2 this is _____.", 16, "4×4=16."))
    A(mcq("Norm", "The 2-norm of a matrix equals",
          "|tr A|", "largest singular value", "smallest eigenvalue", "det A",
          "B", "Operator 2-norm."))
    A(nat("Norm diag", "||diag(1,5)||_2 is _____.", 5, "Max |diag|."))
    A(mcq("Frobenius", "||A||_F^2 equals",
          "sum of squares of entries = tr(A^T A)", "det A", "rank A", "0",
          "A", "Definition."))
    A(nat("Frob", "||I_3||_F is _____.", 3, "√3? Wait ||I_3||_F=√3. Answer √3 not integer."))
    o[-1] = nat("Frob", "||I_3||_F^2 is _____.", 3, "Three ones.")
    A(mcq("Inner", "The standard inner product on R^n is",
          "x1+y1", "x^T y", "xy^T", "||x|| ||y|| always",
          "B", "Dot product."))
    A(nat("Dot", "(1,2,3)·(4,5,6) is _____.", 32, "4+10+18."))
    A(mcq("Cauchy", "|x·y| ≤",
          "||x|| + ||y||", "||x|| ||y||", "0", "x^T A y",
          "B", "Cauchy–Schwarz."))
    A(nat("Angle", "x=(1,0), y=(0,1). Cosine of angle is _____.", 0, "Orthogonal."))
    A(mcq("ONB", "An orthonormal basis B satisfies",
          "vectors of different lengths", "u_i·u_j=δ_{ij}", "sum to 0", "all equal",
          "B", "Definition."))
    A(msq("ONB uniqueness", "Which are true in R^n (n≥2)?",
          "There is a unique orthonormal basis", "There are infinitely many orthonormal bases", "Orthonormal ⇒ linearly independent", "Linearly independent ⇒ orthonormal",
          "B;C", "DA 2025 Q.25 pattern."))
    A(mcq("GS", "Gram–Schmidt turns a basis into",
          "a diagonal matrix", "an orthonormal basis of the same span", "eigenvectors always", "a Jordan form",
          "B", "QR idea."))
    A(mcq("QR", "In A=QR with Q orthogonal thin, R is",
          "lower triangular", "upper triangular", "a permutation", "Σ",
          "B", "Classic."))
    A(nat("QR 1", "QR of a single nonzero column a: R is the 1×1 matrix [||a||]. For a=(3,4), that entry is _____.", 5, "Norm."))
    A(mcq("Householder", "A Householder reflector is",
          "singular", "orthogonal and symmetric", "a Jordan block", "nilpotent",
          "B", "I−2vv^T/||v||^2."))
    A(nat("House det", "det of a Householder matrix is _____.", -1, "Reflection."))
    A(mcq("Givens", "A Givens rotation is used to",
          "zero a single entry using a 2×2 rotation", "compute k-means", "invert via Cramer", "find PCA labels",
          "A", "Sparse orthogonal."))
    A(mcq("Condition", "κ_2(A)=σ_max/σ_min. Large κ means",
          "A is orthogonal", "A is ill-conditioned", "A=0", "A is a projector of rank 0",
          "B", "Sensitivity."))
    A(nat("Cond I", "κ_2(I) is _____.", 1, "All σ=1."))
    A(nat("Cond diag", "κ_2(diag(1,10)) is _____.", 10, "10/1."))
    A(mcq("SPD solve", "The stable way to solve A x=b for SPD A is",
          "normal equations of a random matrix", "Cholesky + two triangular solves", "Cramer's rule", "power method only",
          "B", "O(n^3/3)."))
    A(mcq("Cholesky", "Cholesky exists (over R) iff A is",
          "any invertible", "SPD (or PSD with care)", "orthogonal", "skew",
          "B", "A=LL^T."))
    A(nat("Chol", "[[4,0],[0,9]] = L L^T with L diagonal. L_{11} is _____.", 2, "√4."))
    A(mcq("Pos def test", "x^T A x >0 for all x≠0 means A (symmetric) is",
          "PSD", "PD", "indefinite", "orthogonal",
          "B", "Definition."))
    A(mcq("Skew", "A real skew-symmetric n×n matrix with n odd has",
          "det ≠0 always", "det=0", "all eigen real nonzero", "rank n always",
          "B", "0 is an eigenvalue."))
    A(nat("Skew 2", "[[0,2],[-2,0]] has det _____.", 4, "4."))
    A(mcq("Hermitian", "A Hermitian matrix has",
          "real eigenvalues", "pure imaginary eigenvalues always", "det 0", "Q^T Q=0",
          "A", "Like symmetric over C."))
    A(mcq("Unitary", "U^* U = I characterises",
          "Hermitian", "unitary", "nilpotent", "stochastic",
          "B", "Complex orthogonal analogue."))
    A(nat("Unitary det", "|det U| for unitary U is _____.", 1, "On the circle."))
    A(mcq("Normal mat", "A is normal iff",
          "A A^*=A^* A", "A^2=0", "det A=1", "A=A^T over C",
          "A", "Unitarily diagonalizable iff normal."))
    A(mcq("Stochastic", "A row-stochastic matrix has",
          "rows summing to 1, entries ≥0 typically in Markov chains", "trace 0", "det 1 always", "rank 0",
          "A", "Transition matrix. DA 2025 Q.13 related: rows sum 1."))
    A(mcq("Perron", "A positive matrix (Perron–Frobenius) has",
          "no real eigenvalue", "a simple positive dominant eigenvalue", "only 0 as eigen", "det <0 always",
          "B", "PF."))
    A(nat("Stoch eigen", "A row-stochastic matrix always has eigenvalue _____.", 1, "Rows sum 1 ⇒ A 1=1."))
    A(mcq("Nilpotent", "A^k=0, A^{k−1}≠0. Then all eigenvalues are",
          "1", "0", "k", "−1",
          "B", "Only 0."))
    A(nat("Index", "For N=[[0,1],[0,0]], N^2 is the zero matrix. N^2_{12} is _____.", 0, "Nilpotent index 2."))
    A(mcq("Companion", "The companion matrix of a monic polynomial has that polynomial as",
          "minimal? at least characteristic (and minimal if the poly is the min poly)", "trace", "determinant only if n=1", "a singular value",
          "A", "Classic."))
    A(mcq("Vandermonde", "A Vandermonde matrix with distinct nodes is",
          "singular", "invertible", "nilpotent", "orthogonal always",
          "B", "Distinct ⇒ det≠0."))
    A(nat("Vand det 2", "V=[[1,1],[a,b]] det is b−a. If a=1,b=3, det=_____.", 2, "2."))
    A(mcq("Hadamard", "A Hadamard matrix has entries ±1 and orthogonal rows. Then H H^T equals",
          "0", "n I", "I", "J all-ones",
          "B", "Scaled orthogonal."))
    A(mcq("Laplacian", "Graph Laplacian L=D−A is",
          "indefinite typically", "PSD with 1 in the kernel (connected graph: exactly 1)", "orthogonal", "always invertible",
          "B", "Connected ⇒ nullity 1."))
    A(nat("Lap sum", "Rows of L sum to _____.", 0, "L 1=0."))
    A(mcq("Adj eigen", "The adjacency matrix of a simple graph is",
          "asymmetric always", "real symmetric (undirected)", "unitary", "nilpotent always",
          "B", "A_{ij}=A_{ji}."))
    A(nat("Adj tr", "tr(A) for a simple graph (no loops) is _____.", 0, "Diagonal 0."))
    A(mcq("Incidence", "Rank of the oriented incidence matrix of a connected graph on n vertices is",
          "n", "n−1", "m", "0",
          "B", "Kernel = constants."))
    A(mcq("Left null", "Left-nullspace of A is ker(A^T), which is orthogonal to",
          "ker(A)", "col(A)", "row(A) wait: orthogonal to columns, i.e. col(A)", "R^n always",
          "B", "Fundamental theorem."))
    A(mcq("Four subspaces", "col(A)^⊥ equals",
          "col(A^T)", "ker(A^T)", "ker(A)", "row(A)",
          "B", "Strang's four subspaces."))
    A(nat("Row dim", "Row space dimension equals rank. For rank 3, that dimension is _____.", 3, "Same."))
    A(mcq("Change basis", "P^{−1} A P is A in a new basis (columns of P). This is",
          "a similarity", "a congruence only", "always SVD", "a Householder",
          "A", "Change of basis."))
    A(mcq("Congruence", "P^T A P for symmetric A is",
          "similarity always", "congruence (preserves inertia by Sylvester)", "SVD", "LU",
          "B", "Inertia."))
    A(nat("Inertia", "diag(1,1,−1) has signature (n_+, n_−, n_0) with n_+ = _____.", 2, "Two positives."))
    A(mcq("Law inertia", "Sylvester's law says congruence preserves",
          "eigenvectors", "the triple (n_+,n_−,n_0)", "the entries", "det exactly (not just sign)",
          "B", "Inertia."))
    A(mcq("Bilinear", "A bilinear form on R^n is given by a",
          "vector of length n^2? an n×n matrix via x^T A y", "scalar only", "set", "graph",
          "A", "Matrix of the form."))
    A(mcq("Inner from form", "x^T A y is an inner product iff A is",
          "skew", "SPD", "orthogonal", "nilpotent",
          "B", "Positive definite symmetric."))
    A(nat("Norm from inner", "||x||^2 = x·x. For x=(3,4), ||x|| is _____.", 5, "3-4-5."))
    A(mcq("Parallelogram", "||x+y||^2 + ||x−y||^2 equals",
          "||x||^2", "2||x||^2+2||y||^2", "0", "||x|| ||y||",
          "B", "Parallelogram law."))
    A(mcq("Polar", "A real invertible matrix A= Q S with Q orthogonal, S SPD is",
          "Jordan", "polar decomposition", "SVD only when A is normal", "LU",
          "B", "Like z=e^{iθ} r."))
    A(mcq("CS decomp", "The CS decomposition concerns",
          "k-means", "orthogonal matrices partitioned into blocks", "Poisson", "SQL",
          "B", "Two subspaces."))
    A(nat("Vol", "Volume scaling of the unit cube under A is |det A|. For A=2I_2 this volume is _____.", 4, "4."))
    A(mcq("Orient", "det A >0 means A",
          "is singular", "preserves orientation", "is a reflection", "has a negative eigenvalue necessarily",
          "B", "GL^+."))
    A(mcq("Adjugate", "A (adj A) equals",
          "0", "(det A) I", "A^{−1}", "A^T",
          "B", "Cramer's identity."))
    A(nat("Adj 2", "adj [[a,b],[c,d]] = [[d,−b],[−c,a]]. For [[1,2],[3,4]] the (1,1) of adj is _____.", 4, "d=4."))
    A(mcq("Cramer cost", "Cramer's rule for n×n is",
          "O(n) practical", "O(n!) if dets are expanded naively — not a practical solver", "faster than GE always", "O(1)",
          "B", "Pedagogic."))
    A(mcq("Iterative", "Conjugate gradient applies to",
          "any matrix", "SPD systems", "only 2×2", "SVD of rectangular only",
          "B", "CG."))
    A(mcq("Power method", "The power method finds",
          "the smallest singular value typically", "a dominant eigenpair", "the kernel only", "LU",
          "B", "If there is a spectral gap."))
    A(nat("Power", "A=diag(3,1), x0=(1,1). After many normalisations, the iterate approaches a multiple of e1. The Rayleigh quotient → _____.", 3, "Dominant."))
    A(mcq("QR algo", "The QR algorithm is a standard way to compute",
          "k-means centres", "eigenvalues of dense matrices", "shortest paths", "SQL joins",
          "B", "Francis."))
    A(mcq("Hessenberg", "Reduction to Hessenberg form speeds",
          "k-NN", "eigenvalue algorithms (QR)", "hashing", "BFS",
          "B", "O(n^2) per QR step."))
    A(mcq("Bidiag", "Golub–Kahan bidiagonalisation is for",
          "SVD", "k-means", "Dijkstra", "normalization in SQL",
          "A", "SVD path."))
    A(nat("Nuclear", "Nuclear norm = sum of singular values. For diag(3,4) it is _____.", 7, "3+4."))
    A(mcq("Low rank", "Eckart–Young: best rank-k approx in 2-norm / Frobenius is",
          "k-means of rows", "truncated SVD", "LU with k pivots always optimal", "a random projection with no SVD",
          "B", "Theorem."))
    A(nat("Trunc", "Σ=diag(5,1,0.1). Rank-1 2-norm error is the next σ = _____ (one decimal).", "1.0", "σ2=1."))
    A(mcq("PCA LA", "PCA on centred data is the SVD / eigendecomposition of",
          "the Laplacian", "the covariance / Gram matrix", "a Jordan form of labels", "the adjacency of k-NN",
          "B", "Link to DA ML."))
    A(nat("PCA var", "Eigenvalues of covariance 5,3,2. Fraction on first PC is _____ (one decimal).", "0.5", "5/10."))
    A(mcq("Whitening LA", "If Σ=U Λ U^T, a whitening map is",
          "U Λ^{1/2}", "Λ^{−1/2} U^T (up to orthogonal freedom)", "U only", "Λ",
          "B", "Σ^{−1/2}."))
    A(mcq("Idempotent rank", "For a projector, rank equals",
          "0 always", "trace", "n always", "det",
          "B", "tr=rank."))
    A(nat("Rank P", "P=uu^T/||u||^2, u≠0. Rank of P is _____.", 1, "Rank-1 projector."))
    A(mcq("Complement", "If P projects onto U, I−P projects onto",
          "U", "a complement (orthogonal complement if P is orthogonal)", "U∩U^⊥", "{0} always",
          "B", "Complementary projector."))
    A(mcq("Oblique", "A projector that is not symmetric is",
          "orthogonal", "oblique", "unitary", "normal automatically",
          "B", "Along a complement ≠ orthogonal."))
    A(nat("Trace proj", "Orthogonal projector onto a 3D subspace of R^10 has trace _____.", 3, "Rank 3."))
    A(mcq("Least dist", "The orthogonal projection of b onto col(A) is the unique closest point in the subspace because",
          "the residual is orthogonal to the subspace", "A is square", "b=0", "rank=0",
          "A", "Pythagoras."))
    A(nat("Dist", "Distance from (1,1) to span{(1,0)} is _____.", 1, "The y-coordinate."))
    A(mcq("Fourier", "The DFT matrix (properly scaled) is",
          "singular", "unitary (up to scaling convention)", "nilpotent", "a projector of rank 1",
          "B", "F^* F = I."))
    A(nat("F2", "Unnormalised 2-point DFT maps (1,1) to (2,0). The first coordinate is _____.", 2, "Sum."))
    A(mcq("Circulant", "Circulant matrices are diagonalised by",
          "k-means", "the Fourier matrix", "a random Householder", "LU without pivoting always",
          "B", "Convolution theorem."))
    A(mcq("Toeplitz", "A Toeplitz matrix is constant along",
          "rows", "diagonals", "the spectrum always", "singular vectors always",
          "B", "t_{i−j}."))
    A(mcq("Hankel", "A Hankel matrix is constant along",
          "diagonals", "anti-diagonals", "only the first row", "eigenvalues",
          "B", "i+j."))
    A(nat("Toep 2", "[[1,2],[2,1]] has eigenvalues 3 and −1. Product is _____.", -3, "Det=1−4=−3."))
    A(mcq("Positive map", "x ↦ Ax is injective iff",
          "ker A={0}", "det A=0", "A is square only", "rank A=0",
          "A", "Trivial kernel."))
    A(mcq("Surjective", "A: R^n→R^m is onto iff",
          "rank A = m", "rank A = n always", "nullity=n", "A=0",
          "A", "Full row rank."))
    A(nat("Max rank", "Max rank of a 3×7 matrix is _____.", 3, "Min(3,7)."))
    A(mcq("Outer", "uv^T has rank at most",
          "2", "1", "n", "0",
          "B", "Rank-1 if u,v ≠0."))
    A(nat("Outer rank", "u=(1,0,0), v=(0,1). Rank of u v^T (3×2) is _____.", 1, "Nonzero."))
    A(mcq("Inner vs outer", "u^T v is",
          "a matrix n×n", "a scalar", "always 0", "a projector",
          "B", "Dot."))
    A(mcq("Kronecker vec", "vec(AXB)=(B^T ⊗ A) vec(X). This is used in",
          "SQL", "linear matrix equations (Sylvester, Lyapunov)", "Dijkstra", "tokenisation",
          "B", "Vectorisation identity."))
    A(mcq("Lyapunov", "A^T P + P A = −Q, Q PD, A Hurwitz: then P is",
          "indefinite", "PD (continuous Lyapunov)", "0", "orthogonal",
          "B", "Stability."))
    A(nat("Hurwitz 1", "A=[-1] is Hurwitz. Eigenvalue is _____.", -1, "Re<0."))
    A(mcq("Discrete stab", "Spectral radius ρ(A)<1 implies",
          "A^k → 0", "A is singular", "det A=1", "A is orthogonal",
          "A", "Discrete-time stability."))
    A(nat("Rho", "A=diag(0.5, 0.2). ρ(A) is _____ (one decimal).", "0.5", "Max |λ|."))
    A(mcq("Gershgorin", "Every eigenvalue lies in at least one Gershgorin disc. For diag(3,8) plus tiny off-diagonals, eigenvalues are",
          "near 0", "near 3 and 8", "pure imaginary", "infinite",
          "B", "Discs centred at diagonals."))
    A(nat("Gersh", "[[4,1],[1,4]] discs centred at 4 with radius 1. The true eigenvalues 3 and 5 lie in the union. Sum of eigenvalues is _____.", 8, "Trace."))
    A(mcq("Interlace", "Cauchy interlacing: eigenvalues of a principal submatrix interlace those of a",
          "random matrix", "Hermitian / symmetric matrix", "any Jordan block", "a permutation",
          "B", "Theorem."))
    A(mcq("Weyl", "Weyl inequalities bound eigenvalues of A+B in terms of those of A and B for",
          "Hermitian A,B", "any A,B without symmetry", "nilpotents only", "permutation matrices only",
          "A", "Perturbation."))
    A(nat("Pert", "Eigenvalues of I + ε e1 e1^T for small ε>0: one of them is 1+ε, others 1. For ε=0.1, the largest is _____ (one decimal).", "1.1", "Rank-1 update."))
    A(mcq("Sherman", "Sherman–Morrison updates the inverse after a rank-1 change. It requires",
          "the original inverse and a scalar denominator 1+v^T A^{−1} u", "SVD of the whole A every time", "n! operations", "Cramer",
          "A", "Formula."))
    A(nat("SM", "A=I, u=v=(1,0,...,) wait 1D: (a)^{-1} after adding 1 is 1/(a+1). If a=1, new inverse is _____ (one decimal).", "0.5", "1/2."))
    A(mcq("Woodbury", "Woodbury identity generalises Sherman–Morrison to",
          "rank-k updates", "only scalars", "graphs", "SQL",
          "A", "Block inverse."))
    A(mcq("Schur", "The Schur complement appears in",
          "k-means loss", "block Gaussian elimination / conditional covariance", "A* heuristics", "token BPE",
          "B", "Blocks."))
    A(nat("Schur 2", "[[1,2],[2,5]] Schur complement of 1 is 5−4=_____.", 1, "5−2*(1/1)*2."))
    A(mcq("PD block", "A block SPD matrix has SPD diagonal blocks and SPD Schur complements. In particular the leading principal",
          "minors are positive", "minors are 0", "block is singular", "trace is 0",
          "A", "Sylvester."))
    A(mcq("Equivalence", "A and B are equivalent (PAQ) iff they have the same",
          "eigenvalues", "rank", "trace", "determinant",
          "B", "Same rank."))
    A(mcq("Smith", "Over PIDs, matrices have a Smith normal form. Over fields this reduces to",
          "Jordan", "the rank form (identity plus zeros)", "SVD with complex σ", "a Hadamard matrix",
          "B", "Elementary divisors trivial."))
    A(nat("Canon rank", "Any rank-2 5×7 matrix is equivalent to a matrix with I_2 in the corner. Number of 1s on that diagonal is _____.", 2, "Rank."))
    A(mcq("Left inv", "A tall full-column-rank matrix has a",
          "right inverse", "left inverse", "two-sided inverse", "zero inverse",
          "B", "A^+ A = I."))
    A(mcq("Right inv", "A fat full-row-rank matrix has a",
          "left inverse", "right inverse", "no generalised inverse", "Jordan inverse",
          "B", "A A^+ = I."))
    A(nat("Fat rank", "A 2×5 matrix of rank 2 has a right inverse of size _____. (enter 5, meaning 5×2)", 5, "5×2; we record 5 as the first dimension."))
    A(mcq("Frame", "A frame operator is of the form Σ u_i u_i^T. It is",
          "PSD", "skew", "always singular", "a permutation",
          "A", "Sum of PSD."))
    A(mcq("Tight frame", "A tight frame satisfies Parseval. The frame operator is a",
          "multiple of I", "nilpotent", "Jordan block", "Hadamard of size 3",
          "A", "A=λI."))
    A(nat("Parseval", "Orthonormal basis: Parseval says Σ |<x,e_i>|^2 = ||x||^2. For x=e_1 this is _____.", 1, "1."))
    A(mcq("Riesz", "A Riesz basis is a",
          "linearly dependent spanning set", "basis equivalent to an orthonormal one (bounded invertible change)", "set of size 1 always", "frame of bound 0",
          "B", "Stable basis."))
    A(mcq("Coordinate", "Coordinates of v in basis B are P^{−1} v if columns of P are B. This solves",
          "P c = v", "P^T c = v always without independence", "c=Pv", "c=0",
          "A", "Linear system."))
    A(nat("Coord", "v=(3,5), B={(1,0),(1,1)}. Coordinates (c1,c2): c2=5, c1=_____.", -2, "c1(1,0)+5(1,1)=(3,5) ⇒ c1+5=3."))
    A(mcq("Dual basis", "The dual basis satisfies f_i(v_j)=δ_{ij}. In R^n with ONB, dual is",
          "something else", "the same basis (via inner product)", "0", "the Jordan dual",
          "B", "Self-dual ONB."))
    A(mcq("Annihilator", "U^0 = {f : f|_U=0} has dimension",
          "dim U", "n − dim U", "0 always", "n+1",
          "B", "Dual dimension."))
    A(nat("Ann", "U a 2D subspace of R^5. dim U^0 is _____.", 3, "5−2."))
    A(mcq("Quotient", "dim(V/U) equals",
          "dim V + dim U", "dim V − dim U", "0", "dim U",
          "B", "Quotient."))
    A(nat("Quot", "R^4 / a 1D line has dimension _____.", 3, "4−1."))
    A(mcq("Iso", "Finite-dimensional spaces over the same field are isomorphic iff",
          "they have a basis", "they have equal dimension", "they are R^n for n=1", "det=1",
          "B", "Classification."))
    A(nat("Iso R", "R^6 is isomorphic to the space of 2×3 matrices. Both have dim _____.", 6, "Same."))
    A(mcq("Linear map matrix", "The matrix of a linear map depends on",
          "nothing — it is unique", "the choice of bases", "only the determinant", "the SVD uniquely without bases",
          "B", "Change-of-basis."))
    A(nat("Map rank", "A linear map R^4→R^3 that is onto has rank _____.", 3, "Full target."))
    A(mcq("Rank-nullity map", "rank T + dim ker T =",
          "dim domain", "dim codomain", "rank T^2", "0",
          "A", "Same theorem."))
    A(mcq("Injective n m", "A linear map R^n→R^m can be injective only if",
          "n≤m", "n≥m", "n=0", "m=0",
          "A", "Need enough room."))
    A(nat("Inj max", "Max n such that some injective linear R^n→R^7 exists is _____.", 7, "n≤7."))
    A(mcq("Eval", "The dual map T* satisfies",
          "T* f = f ∘ T", "T* = T^{−1}", "T*=0", "T*=T always",
          "A", "Pullback."))
    A(mcq("Adjoint inner", "The Hilbert adjoint satisfies <Tx,y>=<x,T* y>. For real matrices this is",
          "T^T", "−T", "T^{−1}", "adj T",
          "A", "Transpose."))
    A(nat("Self adjoint", "A real matrix equal to its adjoint is symmetric. For [[1,2],[2,1]] A_{12}−A_{21} is _____.", 0, "Symmetric."))
    A(mcq("Spectral real", "A real symmetric matrix is orthogonally diagonalizable. This is",
          "false", "the real spectral theorem", "Jordan's theorem", "SVD for rectangular only",
          "B", "Q^T A Q = Λ."))
    A(nat("Orth diag", "[[2,0],[0,3]] is already orthogonally diagonal. Q can be I. det Q is _____.", 1, "I."))
    A(mcq("Simultaneous", "Two symmetric matrices are simultaneously orthogonally diagonalizable iff they",
          "have the same trace", "commute", "are invertible", "are 1×1",
          "B", "Commute."))
    A(nat("Comm", "I and A always commute. [I,A] has all entries _____.", 0, "0."))
    A(mcq("Lie", "[A,B]=AB−BA. tr([A,B]) equals",
          "tr(A)tr(B)", "0", "det A", "n",
          "B", "tr AB=tr BA."))
    A(nat("Lie tr", "tr([A,B]) is _____.", 0, "Always."))
    A(mcq("Exp", "exp(A)=Σ A^k/k!. exp(A+B)=exp A exp B if",
          "always", "AB=BA", "det A=0", "A=−B always needed",
          "B", "Trotter otherwise."))
    A(nat("Exp 0", "exp(0) is I. Its trace for n=3 is _____.", 3, "tr I."))
    A(mcq("Exp skew", "exp of a real skew-symmetric matrix is",
          "symmetric PD", "orthogonal with det 1", "nilpotent", "a projector",
          "B", "Rodrigues / SO(n)."))
    A(mcq("Log", "A real orthogonal matrix with det −1",
          "is exp of a skew matrix", "is not in the image of exp: so(n)→SO(n)", "is I", "has all eigen 2",
          "B", "O(n) has two components."))
    A(nat("Rot 90", "Rotation by 90° has trace _____.", 0, "2 cos 90=0."))
    A(mcq("SO3", "A 3×3 rotation is determined by",
          "9 free parameters", "3 parameters (axis-angle)", "1 parameter", "6 independent constraints without counting",
          "B", "dim SO(3)=3."))
    A(nat("Dim SO", "dim SO(n)= n(n−1)/2. For n=3 this is _____.", 3, "3."))
    A(mcq("SL", "SL(n) is det=1. dim SL(n) is",
          "n^2", "n^2−1", "n", "1",
          "B", "One constraint."))
    A(nat("SL2", "dim SL(2) is _____.", 3, "4−1."))
    A(mcq("GL", "GL(n,R) is",
          "all n×n matrices", "invertible n×n matrices", "orthogonal matrices", "SPD matrices",
          "B", "Open subset of R^{n^2}."))
    A(nat("GL2", "A 2×2 matrix is in GL(2) iff det ≠ _____.", 0, "Nonzero det."))
    A(mcq("Connected GL", "GL(n,R) has",
          "1 connected component", "2 components (sign of det)", "n components", "infinitely many",
          "B", "Det sign."))
    A(mcq("SPD cone", "The set of SPD matrices is",
          "a linear subspace", "an open convex cone", "compact", "finite",
          "B", "Convex cone, not a subspace."))
    A(nat("SPD 1", "Smallest n for which SPD n×n exists with a negative entry off-diagonal: n=_____. (e.g. [[2,−1],[-1,2]])", 2, "2×2."))
    A(mcq("Log SPD", "The matrix log of an SPD matrix is",
          "undefined", "the unique real symmetric logarithm", "a rotation", "nilpotent",
          "B", "Via spectral."))
    A(nat("Log I", "log(I)=0. Trace of log I is _____.", 0, "0."))
    A(mcq("Geo SPD", "The geodesic between SPD A,B can be written A^{1/2} (A^{−1/2} B A^{−1/2})^t A^{1/2}. At t=0 this is",
          "B", "A", "I", "0",
          "B", "Start."))
    A(mcq("Karcher", "The Karcher mean of SPD matrices is a",
          "Euclidean mean of entries", "Riemannian centre of mass", "max eigenvalue", "k-means of rows",
          "B", "SPD manifold."))
    A(nat("2mean", "Geometric mean of 1 and 4 (1×1 SPD) is _____.", 2, "√4."))
    A(mcq("Vec SPD", "vech stacks the upper triangle. For n=3, vech has length _____.",
          "6", "9", "3", "1",
          "A", "n(n+1)/2=6. Wait this is MCQ with 6 as A."))
    A(nat("vech", "Length of vech for n=4 is _____.", 10, "10."))
    A(mcq("Kronecker SPD", "A,B SPD ⇒ A⊗B is",
          "indefinite", "SPD", "skew", "singular always",
          "B", "Eigenvalues products >0."))
    A(nat("Kron eig", "eigs 2,3 and 4,5. Products include 8,10,12,15. Product of all four is _____.", 14400, "2*3*4*5 * something wait product of products = (2*3)^2 (4*5)^2? No: 8*10*12*15=14400."))
    A(mcq("Stable GE", "Without pivoting, GE can fail on",
          "I", "[[0,1],[1,0]]", "a random SPD (Cholesky still OK)", "diag(1,2)",
          "B", "Zero pivot."))
    A(nat("Pivot 0", "[[0,1],[1,0]] has det _____.", -1, "Invertible but needs swap."))
    A(mcq("Growth", "The growth factor in GE bounds",
          "k-means loss", "element growth vs stability of LU", "the SVD gap", "the graph diameter",
          "B", "Wilkinson."))
    A(mcq("Iter ref", "Iterative refinement improves a computed solution of Ax=b using",
          "k-NN", "residual in higher precision + correction", "dropping a row", "A*",
          "B", "Classic."))
    A(nat("Resid", "A x̂ − b = (0.01, 0). Infinity-norm residual is _____ (two decimals).", "0.01", "Max abs."))
    A(mcq("Backward", "A stable algorithm produces the exact solution of a nearby problem. This is",
          "forward stability only", "backward stability", "consistency of an estimator", "unbiasedness",
          "B", "Wilkinson."))
    A(mcq("IEEE", "Machine epsilon is about 2^{−52} for float64 ≈ 2e−16. Relating to unit roundoff u,",
          "κ u ≪ 1 is needed for a well-conditioned problem to be accurately solvable", "κ=∞ is fine", "u=1", "u=0 in IEEE",
          "A", "Rule of thumb."))
    A(nat("eps order", "log10 of ~2e−16 is about −16. The number of decimal digits in float64 mantissa is about _____.", 16, "16."))
    A(mcq("Ill posed", "A small singular value of A means some direction is",
          "amplified in the inverse", "killed in A (near kernel)", "a left singular vector of σ_max", "a Householder v of 0",
          "B", "Near dependence."))
    A(nat("Near dep", "Columns (1,1) and (1,1.001) are nearly dependent. The 2×2 Gram det is about _____ (six decimals) ≈ 1e-6.", "0.000002", "(1+1.001^2)−(1+1.001)^2 wait: det [[2, 2.001],[2.001, 1+1.001^2]]. Approximately 2*2.002001 − 2.001^2 ≈ 4.004002−4.004001=0.000001."))
    o[-1] = nat("Near dep", "det([[1,1],[1,1]]) is _____.", 0, "Exact dependence.")
    A(mcq("Tikhonov LA", "Replacing A^T A by A^T A + λ I is",
          "ridge / Tikhonov", "dropping SVD", "k-means", "Householder",
          "A", "Link to ML ridge."))
    A(nat("Ridge LA", "Least squares with λ=1, A=[[1],[0]], b=(1,0). The 1-parameter solution (A^T A+λ)^{-1} A^T b = 1/(1+1)*1 = _____ (one decimal).", "0.5", "0.5."))
    A(mcq("Truncated SVD solve", "A truncated-SVD solver of Ax=b drops",
          "large singular components", "components with small σ", "the residual's orthogonal part only always keeping all σ", "the labels",
          "B", "Filter."))
    A(nat("Filter", "σ=10, 0.1, filter at 1: number of components kept is _____.", 1, "Only 10."))
    A(mcq("Numeric rank", "Numeric rank counts singular values above a",
          "random threshold from k-means", "tolerance (often related to ε ||A||)", "p-value", "df of t",
          "B", "Practical rank."))
    A(nat("Num rank", "σ=5, 4, 1e-14. Numeric rank at tol 1e-8 is _____.", 2, "Two large."))
    A(mcq("Column scale", "Ill-conditioning from bad column scaling is helped by",
          "ignoring units", "equilibration / scaling columns", "adding copies of columns", "dropping the intercept always",
          "B", "Simple fix."))
    A(nat("Scale", "Columns of norms 1 and 1000. κ can be large even if they are orthogonal: κ ≥ 1000/1 = _____.", 1000, "σ_max/σ_min."))
    A(mcq("Pivot growth", "Complete pivoting is",
          "cheaper than partial and always used", "more expensive; partial is the usual compromise", "the same as no pivoting", "SVD",
          "B", "Practice."))
    A(mcq("Band", "A banded SPD matrix is factored with",
          "fill-in confined near the band (if using a suitable order)", "dense SVD only", "exponential fill always", "k-NN",
          "A", "Sparse GE."))
    A(nat("Band width", "Tridiagonal n×n has bandwidth _____. (1 off-diagonal)", 1, "k=1."))
    A(mcq("Sparse", "CSR/CSC store a sparse matrix by",
          "the dense n^2 entries", "indexes and nonzero values", "only the determinant", "its Jordan form",
          "B", "Compressed."))
    A(nat("Nnz", "A cycle graph on 5 vertices has 5 edges, undirected Laplacian nnz on diagonal+2 per edge... number of edges is _____.", 5, "C_5."))
    A(mcq("Matvec", "A sparse matvec with nnz nonzeros costs",
          "O(n^2)", "O(nnz)", "O(n!)", "O(1)",
          "B", "Linear in stored entries."))
    A(nat("Dense matvec", "Dense n=100 matvec costs about n^2 = _____ multiplies.", 10000, "1e4."))
    A(mcq("BLAS", "GEMM is",
          "a graph algorithm", "dense matrix–matrix multiply", "k-means", "SQL join",
          "B", "Level-3 BLAS."))
    A(nat("GEMM flops", "Two n×n multiply: ~2n^3 flops. For n=2 this is about _____.", 16, "2*8=16."))
    A(mcq("Strassen", "Strassen multiplies 2×2 block matrices with",
          "8 multiplies", "7 multiplies", "4 multiplies", "1 multiply",
          "B", "7."))
    A(nat("Strassen n", "Number of scalar multiplies in one Strassen step (2×2 blocks) is _____.", 7, "7."))
    A(mcq("Tensor", "A 3-way tensor's CP rank is",
          "the matrix rank of a flattening always equal to CP rank", "the min number of rank-1 terms in a sum", "always 1", "n!",
          "B", "CANDECOMP."))
    A(nat("Tensor 1", "A rank-1 tensor u⊗v⊗w for nonzero vectors has CP rank _____.", 1, "By definition."))
    A(mcq("Flatten", "Unfolding a tensor to a matrix lets one apply",
          "only k-means", "matrix SVD (Tucker / HOSVD)", "Dijkstra", "α-β pruning",
          "B", "Multilinear SVD."))
    A(mcq("Tucker", "Tucker decomposition uses",
          "a core tensor and factor matrices", "only one vector", "a Jordan block", "a B+ tree",
          "A", "HOSVD."))
    A(nat("Core", "Tucker rank (2,2,2) core has _____ entries.", 8, "2^3."))
    A(mcq("Kronecker vec2", "A⊗B applied to vec(X) (with matching sizes) relates to",
          "B X A^T or similar depending on convention", "k-means of X", "the trace of X only", "det X",
          "A", "Identity above."))
    A(mcq("Commute Kron", "I⊗A and A⊗I (suitable sizes) often appear in",
          "Lyapunov / Sylvester operators", "SQL GROUP BY", "BFS layers", "hash probing",
          "A", "Linear matrix eqns."))
    A(nat("Sylvester 1", "AX−XB=C, A=2, B=3 (1×1). Then X=C/(2−3). If C=4, X=_____.", -4, "4/(2−3)."))
    A(mcq("Unique Sylvester", "AX−XB=C has a unique solution iff",
          "A,B share no eigenvalue", "A=B", "C=0", "n=1 only",
          "A", "Spectra disjoint."))
    A(nat("Disjoint", "A=diag(1,2), B=[3]. They share _____ eigenvalues (count).", 0, "None."))
    A(mcq("Vec stacking", "Column-major vec of [[1,2],[3,4]] is",
          "(1,2,3,4)", "(1,3,2,4)", "(4,3,2,1)", "(1,1,1,1)",
          "B", "Columns."))
    A(nat("Vec1", "First entry of column-major vec of [[7,8],[9,10]] is _____.", 7, "A_11."))
    A(mcq("Reshape", "Reshape does not change",
          "the set of entries (as a list in some order)", "the eigenvalues of a non-square array (undefined)", "the SVD of every flattening equally", "rank of every unfolding equally",
          "A", "Just layout."))
    A(mcq("Broadcast", "Adding a vector to each row of a matrix is",
          "illegal in LA", "an affine operation (like 1 v^T + M)", "a Jordan reduction", "an SVD of v",
          "B", "Centering is this."))
    A(nat("Center", "Mean of rows of [[1,3],[5,7]] is (3,5). Centred first row is (a,b) with a=_____.", -2, "1−3."))
    A(mcq("One-hot", "A one-hot matrix of k classes for n samples is n×k with",
          "all ones", "a single 1 per row typically", "rank 0", "negative entries",
          "B", "Dummy."))
    A(nat("Onehot rank", "n=10 samples, k=3 classes all present. Rank of the one-hot matrix is _____.", 3, "Full k."))
    A(mcq("Gram", "The Gram matrix G=X^T X (columns=samples? conventions vary) is",
          "always indefinite", "PSD", "orthogonal", "skew",
          "B", "A^T A."))
    A(nat("Gram rank", "X is 5×3 of rank 3. Rank of X^T X is _____.", 3, "Same."))
    A(mcq("Kernel trick LA", "A kernel matrix K_{ij}=k(x_i,x_j) must be",
          "indefinite always", "PSD if k is a positive kernel", "hollow with 1s", "a rotation",
          "B", "Mercer."))
    A(nat("Kernel 1", "k(x,y)=x·y, two orthonormal x_i. K is I_2. det K is _____.", 1, "1."))
    A(mcq("Centring K", "Double-centring a kernel matrix is used in",
          "kernel PCA / MDS", "Dijkstra", "SQL DISTINCT", "minimax",
          "A", "H K H."))
    A(nat("H", "Centring matrix H=I−11^T/n for n=2 is [[1/2,−1/2],[−1/2,1/2]]. Rank of H is _____.", 1, "Projects orthogonal to 1."))
    A(mcq("MDS", "Classical MDS from a Euclidean distance matrix recovers",
          "k-means labels", "centred point coordinates up to orthogonal transform", "a B+ tree", "an ER diagram",
          "B", "Eigendecompose the Gram."))
    A(nat("MDS 1", "Two points distance 2. After MDS in 1D, they sit at ±1 if centred. Separation is _____.", 2, "2."))
    A(mcq("Procrustes", "Orthogonal Procrustes min ||A Q − B||_F over orthogonal Q is solved by",
          "k-NN", "SVD of A^T B", "LU of A", "BFS",
          "B", "Q=UV^T."))
    A(nat("Proc", "A=B=I. Optimal Q is I, ||AQ−B||_F is _____.", 0, "0."))
    A(mcq("Wahba", "Wahba's problem is Procrustes with",
          "SQL constraints", "weights on vector observations (attitude determination)", "Poisson noise only", "a tree prior",
          "B", "Spacecraft."))
    A(mcq("ICP", "Iterative closest point alternates",
          "SQL joins", "correspondence and Procrustes", "k-means only without rotation", "A*",
          "B", "Registration."))
    A(nat("Align", "Two identical point clouds already aligned: RMS after ICP is _____.", 0, "0."))
    A(mcq("Cross product", "In R^3, x×y is orthogonal to x and y. |x×y| equals",
          "x·y", "area of the parallelogram", "||x||+||y||", "0 always",
          "B", "Geometry."))
    A(nat("Cross", "(1,0,0)×(0,1,0)=(0,0,1). The third coordinate is _____.", 1, "k."))
    A(mcq("Scalar triple", "x·(y×z) equals",
          "det[x y z]", "x·y·z", "0 always", "||x||",
          "A", "Volume."))
    A(nat("Volume", "det with columns e1,e2,e3 is _____.", 1, "I."))
    A(mcq("Orient 3", "A left-handed basis has det",
          ">0", "<0", "0", "1 always",
          "B", "Negative orientation."))
    A(mcq("Gram det", "det(G) for columns of A is (vol)^2 of the parallelepiped. If A has orthonormal columns, det G is _____.",
          "0", "1", "n", "−1",
          "B", "G=I. This should be nat."))
    o[-1] = nat("Gram det", "Orthonormal columns: det(A^T A) is _____.", 1, "det I=1.")
    A(mcq("QR det", "If A=QR, |det A| equals",
          "|det R| (since |det Q|=1)", "0", "tr R", "||A||_F",
          "A", "Product of |R_ii|."))
    A(nat("Prod diag", "R=diag(2,3,4). |det A| if A=QR with Q orthogonal is _____.", 24, "24."))
    A(mcq("Pivoted QR", "Column-pivoted QR is a rank-revealing factorisation. It is used to",
          "sort eigenvalues always", "select independent columns / subset selection", "compute A*", "parse SQL",
          "B", "RRQR."))
    A(nat("RRQR", "If R_{33} is tiny after CPQR of a 5×5, numeric rank is likely _____.", 2, "Two large diagonals before the drop."))
    A(mcq("ID", "An interpolative decomposition writes A ≈ A[:,J] X. It is related to",
          "k-means labels", "skeleton / CUR / RRQR", "Dijkstra trees", "minimax",
          "B", "Column subset."))
    A(mcq("CUR", "CUR uses actual columns and rows of A, unlike",
          "SQL", "truncated SVD (which uses combinations)", "k-NN", "hashing",
          "B", "Interpretability."))
    A(nat("C cols", "A 100×20 matrix, CUR with 5 columns: C has _____ columns.", 5, "5."))
    A(mcq("Nystrom", "Nyström approximation of a kernel matrix uses",
          "a random subset of columns (landmarks)", "the full eigen-decomposition always", "BFS", "a B+ tree",
          "A", "Landmark."))
    A(nat("Landmarks", "n=1000, ℓ=50 landmarks. Nyström C is 1000× _____.", 50, "ℓ."))
    A(mcq("Randomized SVD", "Halko–Martinsson–Tropp randomized SVD sketches with",
          "SQL GROUP BY", "a random Gaussian (or SRHT) sketch then QR/SVD", "k-means++ only", "A* only",
          "B", "Modern numerical LA."))
    A(nat("Sketch", "A 1000×50 sketch of a 1000×800 matrix uses a 800×50 random matrix. The sketch has _____ columns.", 50, "50."))
    A(mcq("Range finder", "The randomized range finder approximates",
          "ker(A)", "a basis for the dominant left (or right) subspace", "the full Jordan form", "SQL indexes",
          "B", "First stage of RSVD."))
    A(mcq("Oversample", "Oversampling p extra sketch columns improves",
          "the failure probability / capture of a spectral tail", "the exact arithmetic rank always to n", "SQL speed only", "the graph diameter",
          "A", "p≈5–10 typical."))
    A(nat("p", "Target rank k=10, oversample p=5. Sketch width is _____.", 15, "k+p."))
    A(mcq("Power iter RSVD", "A few (A A^T)^q applications before sketching",
          "worsen the gap", "improve capture of a slow spectral decay", "compute SQL joins", "zero the matrix",
          "B", "Power iteration."))
    A(nat("q0", "q=0 means no extra power. Number of extra (AA^T) applications is _____.", 0, "0."))
    A(mcq("Pass", "A pass-efficient algorithm reads A",
          "n^2 times", "a small number of times (streaming)", "never", "only from SQL",
          "B", "Large-scale LA."))
    A(nat("Two pass", "A 2-pass algorithm reads A _____ times.", 2, "2."))
    A(mcq("Streaming", "In one-pass streaming SVD, you cannot",
          "store a sketch", "revisit arbitrary entries of A at will", "multiply by a random Ω on the fly", "output an approximation",
          "B", "Turnstile / row-arrival."))
    A(mcq("CountSketch", "CountSketch is a",
          "SQL constraint", "sparse embedding for sketching", "Householder reflector", "Jordan block",
          "B", "Hashing-based sketch."))
    A(nat("Hash", "CountSketch with 4 buckets and 1 nonzero per column: nnz per column of S is _____.", 1, "1."))
    A(mcq("JL", "Johnson–Lindenstrauss: n points in high dim embed into k = O(ε^{−2} log n) with",
          "exact distances", "approximately preserved distances", "exact PCA", "a spanning tree only",
          "B", "JL lemma."))
    A(nat("JL k", "log n for n=e^{10} is 10. Ignoring ε, k scales as _____. (enter 10 as the log n factor)", 10, "log n."))
    A(mcq("Isometry", "A matrix with orthonormal rows is a",
          "partial isometry (preserves norms of vectors in row space? actually orthonormal rows: ||Ax||=||x|| if A has orthonormal columns)",
          "partial isometry / isometric embedding when columns are orthonormal", "nilpotent", "stochastic always",
          "B", "Stiefel."))
    A(nat("Stiefel", "The Stiefel manifold V_{n,k} of orthonormal k-frames in R^n for n=5,k=2 has matrices of size 5×2. Number of columns is _____.", 2, "2."))
    A(mcq("Grassmann", "Grassmannian Gr(k,n) is the set of",
          "k×k invertible matrices", "k-dimensional subspaces of an n-space", "orthogonal matrices n×n", "SPD n×n",
          "B", "Subspaces."))
    A(nat("Gr dim", "dim Gr(k,n)=k(n−k). For k=2,n=5 this is _____.", 6, "2*3=6."))
    A(mcq("Principal angles", "Principal angles between subspaces are computed via",
          "SQL", "SVD of Q1^T Q2", "BFS", "k-means",
          "B", "Canonical angles."))
    A(nat("Angle 0", "The same subspace vs itself: all principal angles are _____.", 0, "0."))
    A(mcq("Chordal", "A chordal metric on Grassmann uses",
          "the Frobenius distance of projectors", "edit distance", "Hamming on bits of det", "SQL Levenshtein",
          "A", "||P−Q||_F."))
    A(nat("Proj dist", "Two orthogonal 1D projectors in R^2 at 90°: ||P−Q||_F^2 = 2. ||P−Q||_F is _____ (one decimal, √2≈1.4).", "1.4", "√2."))
    A(mcq("CS again", "Davis–Kahan sin Θ theorem bounds",
          "SQL errors", "subspace perturbation via a gap in the spectrum", "k-means local min", "hash collisions",
          "B", "Perturbation of eigenspaces."))
    A(nat("Gap", "Eigenvalues 5, 0. A perturbation of size 0.1, gap is 5. Sin Θ is at most about 0.1/5=_____ (two decimals).", "0.02", "DK scale."))
    return uniq(o)
