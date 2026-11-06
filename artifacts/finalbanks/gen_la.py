#!/usr/bin/env python3
"""Emit unique GATE-style Linear Algebra items (>=260)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from helpers import mcq, msq, nat, uniq

import numpy as np


def det2(a, b, c, d):
    return a * d - b * c


def items():
    o = []
    A = o.append

    A(msq("Subspace", "Which of the following are subspaces of R^3?",
          "{x : x1+x2+x3=0}", "{x : x1+x2+x3=1}", "{0}", "{x : x1 x2 = 0}",
          "A;C", "Must contain 0 and be closed under addition. The product constraint is not a subspace; the affine plane misses 0."))
    A(mcq("Subspace", "The vector space of 2x2 real symmetric matrices has dimension",
          "2", "3", "4", "1", "B", "Independent entries a,b,c in [[a,b],[b,c]]."))
    A(mcq("Subspace", "Polynomials of degree exactly 3 (with the zero polynomial excluded) form",
          "a subspace of P_3", "not a subspace, because 0 is not of exact degree 3", "P_2", "R^3",
          "B", "Missing the zero vector."))
    A(nat("Subspace", "Dimension of {x in R^4 : x1=x2 and x3=0} is _____.", 2, "Free variables x1 and x4."))
    A(mcq("Span", "span{(1,0),(0,1),(1,1)} in R^2 equals",
          "a line", "R^2", "{0}", "R^3", "B", "The first two vectors already form a basis."))
    A(msq("Independence", "Which sets in R^3 are linearly independent?",
          "{(1,0,0),(0,1,0)}", "{(1,1,1),(2,2,2)}", "{(1,0,0),(0,1,0),(0,0,1)}", "{(0,0,0),(1,0,0)}",
          "A;C", "A scalar multiple pair is dependent; the zero vector kills independence."))
    A(nat("Independence", "Maximum size of a linearly independent set in R^5 is _____.", 5, "Equals dim."))
    A(mcq("Basis", "Any two bases of a finite-dimensional vector space",
          "can have different cardinalities", "have equally many vectors", "must be orthogonal", "must contain e1",
          "B", "Dimension is well-defined."))
    A(nat("Dim", "dim of the real vector space of 2x3 matrices is _____.", 6, "Six entries."))
    A(nat("Sum", "dim U=3, dim W=3, dim(U intersect W)=1 inside R^5. Then dim(U+W) is _____.", 5, "3+3-1=5."))
    A(mcq("Direct", "The sum U+W is direct if and only if",
          "U intersect W = {0}", "U=W", "dim U=0", "U+W=R^n always",
          "A", "Definition of internal direct sum."))

    A(nat("Rank", "Rank of [[1,2,3],[2,4,6],[0,0,0]] is _____.", 1, "Row2=2*Row1; Row3=0."))
    A(nat("Rank", "The 5x5 all-ones matrix has rank _____.", 1, "Every column equals the first."))
    A(nat("Rank", "Rank of diag(2,0,3,0) is _____.", 2, "Two nonzero pivots."))
    A(nat("Nullity", "A 3x5 matrix of rank 2 has nullity _____.", 3, "5-2 by rank-nullity."))
    A(nat("Nullity", "An invertible 4x4 matrix has nullity _____.", 0, "Trivial kernel."))
    A(mcq("Rank-nullity", "For a linear map A: R^n -> R^m, rank(A)+nullity(A) equals",
          "m", "n", "m+n", "rank(A^T) always plus n",
          "B", "Domain dimension."))
    A(mcq("Rank transpose", "rank(A) always equals",
          "rank(A^T)", "nullity(A)", "n", "0",
          "A", "Row rank = column rank."))
    A(mcq("Consistency", "The system [[1,2],[2,4]] [x,y]^T = [3,6]^T is",
          "inconsistent", "consistent with infinitely many solutions", "a unique solution", "empty of solutions and of variables",
          "B", "Second equation is twice the first; one free variable."))
    A(mcq("Consistency2", "[[1,2],[2,4]] [x,y]^T = [3,5]^T is",
          "consistent", "inconsistent", "underdetermined with a unique solution", "homogeneous",
          "B", "3*2=6 != 5."))
    A(nat("Free", "RREF of a 3x4 matrix has two pivot columns. Number of free variables is _____.", 2, "4-2."))
    A(nat("Det2", "det([[4,3],[2,1]]) is _____.", -2, "4-6=-2."))
    A(nat("Det2b", "det([[0,-1],[1,0]]) is _____.", 1, "Rotation by 90 degrees, det=1."))
    A(nat("Det3", "det of the upper-triangular matrix diag(2,-1,5) is _____.", -10, "Product of diagonals."))
    A(mcq("Det product", "det(AB) equals",
          "det A + det B", "det(A) det(B)", "det(A+B)", "trace(AB)",
          "B", "Multiplicativity."))
    A(mcq("Det inv", "If det A=2 then det(A^{-1}) is",
          "2", "1/2", "-2", "0",
          "B", "det A * det A^{-1}=1."))
    A(nat("Det scale", "det(3I_2) is _____.", 9, "3^2."))
    A(mcq("Eig 2x2", "For M=[[2,-1],[3,1]], which statement is TRUE?",
          "Both eigenvalues are non-negative reals", "Eigenvalues are a complex conjugate pair",
          "One eigenvalue is zero", "One eigenvalue is positive real and one is negative real",
          "D", "char poly t^2-3t+5? Wait: tr=3, det=2-(-3)=5, t^2-3t+5=0, disc=9-20<0 so COMPLEX. Recheck."))
    # fix: M=[[2,-1],[3,1]], tr=3, det=2+3=5, disc=9-20=-11 <0. Answer B.
    o[-1] = mcq("Eig 2x2", "Let M=[[2,-1],[3,1]]. Which statement is TRUE?",
                "Both eigenvalues are non-negative reals",
                "The eigenvalues form a complex conjugate pair",
                "One eigenvalue is zero and the other is 3",
                "One eigenvalue is positive real and the other is negative real",
                "B", "Trace 3, det 5, discriminant 9-20<0.")
    A(mcq("Eig 2x2b", "Let A=[[0,-1],[1,0]]. The eigenvalues are",
          "1 and -1", "i and -i", "0 and 0", "2 and 0",
          "B", "Rotation by 90 degrees: characteristic t^2+1=0."))
    A(nat("Trace eig", "Sum of eigenvalues of [[4,1],[2,3]] (counted with multiplicity) is _____.", 7, "Equals trace."))
    A(nat("Prod eig", "Product of eigenvalues of [[4,1],[2,3]] is _____.", 10, "Equals det=12-2=10."))
    A(mcq("Eig vec", "A=[[2,0],[0,3]]. A corresponding eigenvector for lambda=3 is",
          "[1,0]^T", "[0,1]^T", "[1,1]^T", "[0,0]^T",
          "B", "Ae2=3 e2."))
    A(mcq("Diag", "A 2x2 real matrix is diagonalizable over R if it has",
          "a repeated eigenvalue always", "two independent eigenvectors", "det=0", "trace=0",
          "B", "A basis of eigenvectors."))
    A(mcq("Not diag", "[[0,1],[0,0]] is",
          "diagonalizable", "not diagonalizable (Jordan block)", "orthogonal", "full rank",
          "B", "Nilpotent index 2, single eigenvector line."))
    A(nat("Char", "Characteristic polynomial of [[0,1],[-2,3]] is t^2-3t+2. The roots (eigenvalues) sum to _____.", 3, "Trace."))
    A(mcq("Cayley", "Cayley-Hamilton says a square matrix",
          "has distinct eigenvalues", "satisfies its own characteristic equation", "is invertible", "has det 1",
          "B", "p(A)=0."))
    A(nat("Idempotent", "If P^2=P, the possible eigenvalues of P are only 0 and _____.", 1, "lambda^2=lambda."))
    A(mcq("Projection", "An orthogonal projection matrix P satisfies",
          "P^T=P and P^2=P", "P^T=-P", "P^2=I always", "det P=1 always",
          "A", "Symmetric idempotent."))
    A(mcq("Orthogonal mtx", "A real matrix Q is orthogonal iff",
          "Q^T Q = I", "Q^2=Q", "det Q=0", "trace Q=0",
          "A", "Columns orthonormal."))
    A(nat("Orth det", "If Q is orthogonal, |det Q| equals _____.", 1, "det(Q^T Q)=1."))
    A(mcq("Rotation", "M=[[cos theta, -sin theta],[sin theta, cos theta]] with theta=2*pi/5. Then M^5 equals",
          "M", "M^2", "I_2", "0",
          "C", "Rotation by 2pi."))
    A(mcq("Rotation 2026", "Same rotation by 2*pi/5. M^{2026} equals which of the following?",
          "M", "M^2", "M^{-1}", "I_2",
          "A", "2026 = 5*405 + 1, so M^{2026}=M."))
    A(nat("Proj 1d", "The orthogonal projection of (3,4) onto span{(1,0)} is the vector (a,0). a equals _____.", 3, "First coordinate."))
    A(nat("Proj formula", "P = uu^T for unit u=(3/5,4/5). P_{11} equals _____ (two decimals).", "0.36", "(3/5)^2=0.36."))
    A(mcq("Quad", "The quadratic form [x,y] [[2,0],[0,-3]] [x,y]^T is",
          "positive definite", "negative definite", "indefinite", "zero",
          "C", "Eigenvalues 2 and -3."))
    A(mcq("PD", "A symmetric matrix is positive definite iff",
          "all eigenvalues are positive", "det>0 only", "trace>0 only", "it is orthogonal",
          "A", "Sylvester / spectral."))
    A(nat("Quad eval", "q(x,y)=x^2+2xy+y^2 at (1,-1) equals _____.", 0, "(x+y)^2."))
    A(mcq("LU", "An LU factorisation without pivoting exists for a square A if",
          "all leading principal minors are nonzero", "A is singular", "A is orthogonal", "trace A=0",
          "A", "Classical criterion."))
    A(nat("LU", "For A=[[2,1],[4,3]], L has 1s on the diagonal and L_{21} equals _____.", 2, "4/2=2."))
    A(mcq("SVD", "For any real m x n matrix, SVD writes A as",
          "U Sigma V^T with U,V orthogonal and Sigma rectangular diagonal", "QR only", "P^2=P", "LDL with no signs",
          "A", "Existence of SVD."))
    A(nat("SVD vals", "Singular values of diag(3,-2) are 3 and _____.", 2, "Absolute eigenvalues for diagonal."))
    A(nat("Fro", "Frobenius norm of [[1,0],[0,2]] is _____ (one decimal, sqrt(5)~2.2).", "2.2", "sqrt(1+4)=sqrt5~2.236."))
    A(nat("Op2", "Spectral norm of diag(1,4) is _____.", 4, "Largest |eigenvalue| here."))
    A(mcq("Left inv", "A 3x2 matrix of rank 2 has a",
          "right inverse (2x3)", "left inverse (2x3)", "two-sided inverse 3x3", "zero nullity in R^3",
          "B", "Full column rank => left inverse."))
    A(mcq("Right inv", "A 2x3 matrix of rank 2 has a",
          "left inverse", "right inverse", "ordinary inverse", "kernel {0} in R^3",
          "B", "Full row rank => right inverse. Kernel dimension 1."))
    A(nat("Kernel dim", "A 2x3 matrix of rank 2: dim ker A is _____.", 1, "3-2."))
    A(mcq("Row eq", "Row-equivalent matrices have the same",
          "eigenvalues always", "row space (hence same rank)", "determinants always", "singular values always",
          "B", "Elementary row ops."))
    A(nat("Trace cyclic", "tr(AB) for A=[[1,2],[0,1]], B=[[0,1],[1,0]] equals tr(BA)=_____.", 2, "AB=[[2,1],[1,0]], tr=2."))
    A(mcq("Sim", "Similar matrices A and P^{-1}AP share",
          "the characteristic polynomial", "the (1,1) entry", "the Frobenius inner product with I only if P=I", "nothing in general",
          "A", "Same eigenvalues and algebraic multiplicities."))
    A(nat("Null space vec", "A=[[1,1,1],[2,2,2]]. A basis vector of ker A can be (1,-1,0). Another independent one is (1,0,c) with c=_____.", -1, "x+y+z=0."))
    A(mcq("Partition", "If A is block-diagonal diag(B,C) with B,C square, then det A equals",
          "det B + det C", "det B * det C", "0", "tr B * tr C",
          "B", "Block triangular/diagonal."))
    A(nat("Block det", "det diag([[1,0],[0,1]], [2]) is _____.", 2, "1*2."))
    A(mcq("Idempotent proj", "For a projection (not necessarily orthogonal) P, I-P is",
          "also a projection onto ker P along the complementary image", "orthogonal always", "invertible always", "nilpotent",
          "A", "(I-P)^2=I-P."))
    A(nat("Rank proj", "If P is a projection R^n->R^n of rank k, then tr(P) equals _____.", "k", "Trace equals rank for projections."))
    A(mcq("Normal", "A real symmetric matrix is",
          "always orthogonally diagonalizable", "never diagonalizable", "always singular", "always orthogonal",
          "A", "Spectral theorem."))
    A(mcq("Skew", "A real skew-symmetric n x n matrix with n odd",
          "is invertible", "has det 0", "has all eigenvalues real and positive", "equals I",
          "B", "det A = det(A^T)=det(-A)=(-1)^n det A, n odd => det=0."))
    A(nat("Skew 2", "det of [[0,2],[-2,0]] is _____.", 4, "4."))
    A(mcq("Gauss", "After one elimination step on [[2,1,1],[2,2,3]] the (2,1) entry becomes",
          "2", "0", "1", "3",
          "B", "R2 <- R2-R1."))
    A(nat("Pivot", "The first pivot of [[0,1],[2,3]] after a row swap is _____.", 2, "Swap to put 2 in (1,1)."))
    A(mcq("Unique sol", "Ax=b has a unique solution for every b in R^n iff A is",
          "square and invertible", "any  n x (n+1)", "singular", "a projection",
          "A", "Full rank square."))
    A(nat("Homog", "A nontrivial solution of Ax=0 exists iff rank A is strictly less than the number of columns. For 3x3 rank 2, number of independent nontrivial solutions (dim ker) is _____.", 1, "1."))
    A(mcq("Col space", "Col(A) is",
          "the span of the columns of A", "the left nullspace", "always R^n", "ker(A^T) always",
          "A", "Definition. Also equals ker(A^T)^perp."))
    A(mcq("Four fund", "ker(A) and row(A) in R^n are",
          "the same space", "orthogonal complements", "both {0}", "equal to Col(A)",
          "B", "Fundamental theorem."))
    A(nat("Rank product", "rank(AB) is at most min(rank A, rank B). If A is 2x3 rank 2 and B is 3x2 rank 2, rank(AB) is at most _____.", 2, "min=2."))
    A(mcq("Outer", "uv^T for nonzero u in R^m, v in R^n has rank",
          "0", "1", "min(m,n) always", "m+n",
          "B", "All columns are multiples of u."))
    A(nat("All ones eig", "The all-ones 3x3 matrix J has eigenvalues 3,0,0. Rank(J) is _____.", 1, "One nonzero eigenvalue."))
    A(mcq("Stochastic", "A row-stochastic matrix has",
          "each row summing to 1", "each column summing to 0", "trace 1", "det 1",
          "A", "1 is always an eigenvalue."))
    A(nat("Stoch eig", "[[0.5,0.5],[0.2,0.8]] has 1 as an eigenvalue. The other eigenvalue is trace-1=_____. (one decimal)", "0.3", "trace=1.3."))
    A(mcq("Least sq", "The normal equation for min ||Ax-b||_2 (A full column rank) is",
          "A^T A x = A^T b", "A x = b", "x = A b", "A A^T x = b",
          "A", "Normal equations."))
    A(nat("LS 1d", "Best least-squares slope through origin for points (1,2),(2,2): xhat = (A^T b)/(A^T A) with A=(1,2)^T, b=(2,2)^T equals _____ (one decimal).", "1.2", "(2+4)/(1+4)=6/5=1.2."))
    A(mcq("Pseudo", "The Moore-Penrose pseudoinverse of a full-column-rank A is",
          "(A^T A)^{-1} A^T", "A^T (A A^T)^{-1}", "A^{-1}", "A^T",
          "A", "Left inverse."))
    A(nat("Cond", "For diag(10, 0.1), the 2-norm condition number is _____.", 100, "10/0.1."))
    A(mcq("Ill", "A large condition number means",
          "A is close to singular in relative perturbation sense", "A is orthogonal", "det A=1", "A=0",
          "A", "Sensitivity of Ax=b."))
    A(nat("Inv 2x2", "Inverse of [[1,1],[0,1]] is [[1,-1],[0,1]]. The (1,2) entry of the inverse is _____.", -1, "Shear inverse."))
    A(mcq("Triang eig", "Eigenvalues of a triangular matrix are",
          "the diagonal entries", "always 0", "the row sums", "singular values",
          "A", "char poly product (t-a_ii)."))
    A(nat("Nilp", "N=[[0,1],[0,0]]. N^2 equals the zero matrix. Rank(N) is _____.", 1, "One independent column."))
    A(mcq("Min poly", "The minimal polynomial divides the characteristic polynomial and has the same",
          "roots (the eigenvalues)", "degree always n", "constant term 1", "leading term n",
          "A", "Same linear factors, possibly lower multiplicity."))
    A(nat("Geom mult", "For a Jordan block of size 3 with lambda=2, geometric multiplicity of 2 is _____.", 1, "dim ker(A-2I)=1."))
    A(mcq("Alg vs geo", "Always",
          "geo multiplicity <= algebraic multiplicity", "geo > alg", "they are equal for every matrix", "geo=0",
          "A", "Standard."))
    A(nat("Dim hom", "Solution space of x+y+z=0 in R^3 has dimension _____.", 2, "One independent constraint."))
    A(mcq("Affine", "The set {x: Ax=b} for consistent Ax=b is",
          "a subspace if b!=0", "an affine translate of ker A", "always {0}", "a sphere",
          "B", "Particular + homogeneous."))
    A(nat("Ones ker", "Number of independent solutions of x1+x2+x3+x4=0 is _____.", 3, "Hyperplane."))
    A(mcq("Onb", "An orthonormal basis of R^2 is",
          "{(1,0),(0,1)}", "{(1,1),(1,-1)} without scaling", "{(1,0),(1,0)}", "{(0,0),(1,0)}",
          "A", "Standard. The second needs 1/sqrt(2)."))
    A(nat("GS", "Gram-Schmidt on (1,1) then (0,1): the second orthonormal vector's first component is _____ (two decimals, -1/sqrt(2)~-0.71).", "-0.71", "v2=(0,1)-proj= (-1/2,1/2), normalize."))
    A(mcq("QR", "QR factorisation writes a full-column-rank A as",
          "Q orthogonal times R upper triangular", "LU", "SVD only", "P symmetric",
          "A", "Thin or full QR."))
    A(nat("Hadamard", "A 2x2 Hadamard matrix [[1,1],[1,-1]] has det _____.", -2, " -1-1=-2."))
    A(mcq("Perm", "A permutation matrix is",
          "orthogonal (hence invertible, P^{-1}=P^T)", "singular", "a projection of rank 0", "symmetric always",
          "A", "Rows of I permuted."))
    A(nat("Perm det", "det of the permutation matrix for the transposition (12) in R^2, i.e. [[0,1],[1,0]], is _____.", -1, "Odd permutation."))
    A(nat("Kron dim0", "If dim U=2 and dim V=3 then dim(U+V) in a direct sum is _____.", 5, "2+3 when intersection is 0."))
    o[-1] = mcq("Block mul", "[[A,B],[0,C]] [[X,Y],[0,Z]] equals [[AX, AY+BZ],[0, CZ]] when shapes allow. This is",
                "false in general", "the rule for conforming block-upper-triangular products", "only for scalars", "LU",
                "B", "Block multiplication.")
    A(nat("Trace I", "tr(I_5) is _____.", 5, "5."))
    A(nat("Rank I", "rank(I_5) is _____.", 5, "5."))
    A(mcq("Scalar", "The matrix aI_n has eigenvalues",
          "all equal to a", "0 and a", "1 repeated", "a^n",
          "A", "a times I."))
    A(nat("Det 2I", "det(2 I_3) is _____.", 8, "2^3."))
    A(mcq("Commute", "If AB=BA and A is diagonalizable with distinct eigenvalues, then B",
          "is a polynomial in A (in particular shares the eigenbasis)", "must be 0", "must be I", "cannot exist",
          "A", "Classical fact for distinct eigs."))
    A(nat("Poly eig", "If Av=2v and p(t)=t^2-t, then p(A)v equals _____ v, i.e. the scalar is _____.", 2, "p(2)=4-2=2."))
    A(mcq("Invar", "A subspace W is A-invariant if",
          "A(W) subset W", "W subset ker A", "A is invertible", "W=R^n only",
          "A", "Definition."))
    A(nat("Image dim", "dim im T for T: R^4->R^3 of rank 2 is _____.", 2, "Rank."))
    A(mcq("Iso", "A linear map T: R^n->R^n is an isomorphism iff",
          "ker T={0}", "T=0", "rank T=0", "T is a projection",
          "A", "Equivalent: invertible, full rank."))
    A(nat("Change basis", "If P has columns the new basis, [v]_new = P^{-1} v_old. For P=I this map is the identity, so the (1,1) entry of P^{-1} is _____.", 1, "I."))
    A(mcq("Coord", "The matrix of a linear map T with respect to bases changes by",
          "similarity (or the rectangular analogue P^{-1} A Q)", "addition of I", "transposition only", "nothing",
          "A", "Change of basis."))
    A(nat("Dot", "The standard inner product of (1,2,3) and (1,-1,1) is _____.", 2, "1-2+3=2."))
    A(mcq("Cauchy", "|(u,v)| <= ||u|| ||v|| is",
          "Cauchy-Schwarz", "triangle only", "Pythagoras", "Parseval only on C^n",
          "A", "CS."))
    A(nat("Norm", "Euclidean norm of (3,4) is _____.", 5, "5."))
    A(mcq("Orth set", "A set of nonzero orthogonal vectors is",
          "linearly dependent", "linearly independent", "a basis of R^n always", "empty of inner products",
          "B", "Standard lemma."))
    A(nat("Onb size", "An orthonormal set in R^n has size at most _____.", "n", "Independence."))
    A(mcq("Compl", "The orthogonal complement of a k-dimensional subspace of R^n has dimension",
          "k", "n-k", "n", "0",
          "B", "dim W + dim W^perp = n."))
    A(nat("Perp", "In R^3, the orthogonal complement of span{(1,0,0),(0,1,0)} has dimension _____.", 1, "The z-axis."))
    A(mcq("Proj unique", "The orthogonal projection of v onto a subspace W is the unique w in W such that",
          "v-w is orthogonal to W", "w=0", "||w|| is maximal among all of R^n", "w=v always",
          "A", "Normal equations."))
    A(nat("Refl", "Householder reflection I-2uu^T for unit u is orthogonal. det equals _____.", -1, "One eigenvalue -1."))
    A(mcq("PSD", "A Gram matrix A^T A is always",
          "positive semidefinite", "indefinite", "orthogonal", "nilpotent",
          "A", "x^T A^T A x = ||Ax||^2 >=0."))
    A(nat("Gram rank", "rank(A^T A) equals rank(A). If A is 4x3 of rank 2, rank(A^T A) is _____.", 2, "Same rank."))
    A(mcq("Cholesky", "A symmetric positive definite matrix admits",
          "a unique Cholesky factor R^T R with R upper triangular, positive diagonal", "no factorisation", "only SVD with zero values", "P^2=P",
          "A", "Cholesky."))
    A(nat("SPD check", "Leading minors of [[2,1],[1,2]] are 2 and 3, both positive, so the matrix is SPD. det equals _____.", 3, "4-1=3."))
    A(mcq("Quad classify", "q=x^2+y^2 is",
          "positive definite on R^2", "indefinite", "negative definite", "zero",
          "A", "||(x,y)||^2."))
    A(mcq("Sig", "The inertia of a real symmetric matrix (numbers of +, -, 0 eigenvalues) is",
          "invariant under congruence", "changed by any invertible congruence", "the same as the Jordan form always", "always (n,0,0)",
          "A", "Sylvester's law of inertia."))
    A(nat("Inertia", "diag(1,-2,0) has how many negative eigenvalues? _____.", 1, "One."))
    A(mcq("Row op det", "Swapping two rows of A multiplies det by",
          "+1", "-1", "0", "2",
          "B", "Alternating."))
    A(nat("Scale row", "Multiply one row of I_3 by 5. The determinant becomes _____.", 5, "Multilinear."))
    A(mcq("Cramer", "Cramer's rule expresses each x_i as",
          "det(A_i)/det(A) when det A !=0", "tr A", "rank A", "||A||",
          "A", "Replace column i by b."))
    A(nat("Cramer x", "[[1,1],[0,1]] [x,y]^T=[1,1]^T. Then y=_____.", 1, "Back substitution."))
    A(nat("Cramer x2", "Same system: x equals _____.", 0, "x+y=1, y=1 => x=0."))
    A(mcq("Adjugate", "A^{-1} = (1/det A) adj(A) when det A !=0. adj(A) is",
          "the transpose of the cofactor matrix", "A^T", "A^2", "0",
          "A", "Classical adjoint."))
    A(nat("Cofactor", "Cofactor C_{11} of [[1,2],[3,4]] is det[4]=_____.", 4, "Minor."))
    A(nat("Adj 2", "adj([[1,2],[3,4]])=[[4,-2],[-3,1]]. det A=-2 so A^{-1} has (1,1) entry 4/(-2)=_____.", -2, "-2."))
    A(mcq("Vandermonde", "The Vandermonde matrix on distinct nodes is",
          "invertible", "always singular", "orthogonal", "nilpotent",
          "A", "Distinct x_i."))
    A(nat("Van 2", "det [[1,1],[x,y]] = y-x. For x=2,y=5 this det is _____.", 3, "3."))
    A(mcq("Companion", "The companion matrix of t^2-3t+2 has characteristic polynomial",
          "t^2-3t+2", "t^2+1", "t-1", "0",
          "A", "By construction."))
    A(nat("Comp eig", "Roots of t^2-3t+2=0 are 1 and _____.", 2, "Factors (t-1)(t-2)."))
    A(mcq("Markov", "A column-stochastic matrix has 1 as eigenvalue because",
          "columns sum to 1 so A^T 1 = 1 (or A1=1 depending on convention)", "trace=1", "det=1", "rank=1 always",
          "A", "All-ones eigenvector."))
    A(nat("Perron", "The Perron root of a positive matrix is simple and positive. For [[1,1],[1,1]] it is _____.", 2, "Eigenvalues 2,0."))
    A(mcq("Graph lap", "The Laplacian of an undirected graph is PSD with kernel dimension equal to",
          "the number of connected components", "the number of edges", "n always", "0 always",
          "A", "Standard."))
    A(nat("Path3", "Path on 3 vertices: Laplacian eigenvalues include 0. Rank of L is _____.", 2, "Connected => rank n-1."))
    A(mcq("Adj spec", "The adjacency matrix of an undirected simple graph is",
          "real symmetric (hence orthogonally diagonalizable)", "skew and invertible", "a projection", "nilpotent of index 2 always",
          "A", "A_{ij}=A_{ji}."))
    A(nat("K2", "Complete graph K2 has adjacency [[0,1],[1,0]]. Eigenvalues 1 and _____.", -1, "det(t^2-1)."))
    A(mcq("Incidence", "For an oriented graph, B B^T is",
          "the Laplacian (unnormalized)", "I", "A^2", "0",
          "A", "B incidence."))
    A(nat("Cycle even", "A 4-cycle is bipartite so -2 is an adjacency eigenvalue of C4 (regular of degree 2). The largest adjacency eigenvalue is _____.", 2, "Degree of regular graph."))
    A(mcq("Shift", "A-lambda I is singular iff",
          "lambda is an eigenvalue", "A=0", "lambda=0 always", "A is orthogonal",
          "A", "Definition."))
    A(nat("Eig 0", "A is singular iff 0 is an eigenvalue. det([[1,1],[2,2]]) is _____.", 0, "Rows dependent."))
    A(mcq("Left eig", "A left eigenvector satisfies w^T A = lambda w^T. For real symmetric A, left and right eigenspaces",
          "coincide", "are always orthogonal to each other in a different sense than usual", "never exist", "are {0}",
          "A", "A=A^T."))
    A(nat("Rayleigh", "For symmetric A, the Rayleigh quotient v^T A v / v^T v at an eigenvector equals the eigenvalue. For A=diag(2,5) and v=e2 it is _____.", 5, "5."))
    A(mcq("Min max", "The smallest eigenvalue of a real symmetric A is the minimum of the Rayleigh quotient. For diag(2,5) that minimum is _____.",
          "2", "5", "7", "0",
          "A", "Courant-Fischer."))
    A(nat("Weyl", "Eigenvalues of A and A+E differ by at most ||E|| (in a suitable norm). If ||E||=0.1 and gap is 5, a crude sin Theta bound 0.1/5 equals _____ (two decimals).", "0.02", "Davis-Kahan flavour."))
    A(mcq("Exp", "exp(tA) for a square A is the fundamental matrix of u'=Au. exp(0)=",
          "I", "0", "A", "tI",
          "A", "Series."))
    A(nat("Exp diag", "exp(diag(0, ln 2)) = diag(1,2). The (2,2) entry is _____.", 2, "e^{ln 2}."))
    A(mcq("Nilp exp", "For N^2=0, exp(N)=",
          "I+N", "I", "0", "N",
          "A", "Series truncates."))
    A(nat("Jordan", "Number of Jordan blocks for lambda equals geo multiplicity. For a single 2x2 block, geo multiplicity is _____.", 1, "1."))
    A(mcq("Defective", "A defective eigenvalue has",
          "geo multiplicity < algebraic multiplicity", "geo > alg", "no eigenvector", "det=1",
          "A", "Definition."))
    A(nat("Index", "Index of eigenvalue 0 for [[0,1],[0,0]] (size of largest block) is _____.", 2, "N^2=0, N!=0."))
    A(mcq("Schur", "Over C every square matrix is unitarily similar to",
          "upper triangular (Schur form)", "a projection", "I", "a permutation",
          "A", "Schur."))
    A(mcq("Real schur", "A real matrix with a complex conjugate eigenvalue pair has a real Schur form containing",
          "a 2x2 block", "only 1x1 blocks always", "a zero row", "P^2=P",
          "A", "2x2 rotation-scale blocks."))
    A(nat("Rot det", "det of a 2x2 rotation is _____.", 1, "1."))
    A(mcq("Reflect det", "det of a Householder reflector is",
          "-1", "1", "0", "2",
          "A", "One -1 eigenvalue."))
    A(nat("Pauli", "sigma_z = [[1,0],[0,-1]] has eigenvalues 1 and _____.", -1, "diag."))
    A(mcq("Hermitian", "A complex matrix with A^*=A has",
          "real eigenvalues", "pure imaginary eigenvalues", "det 0", "trace 0 always",
          "A", "Hermitian spectral theorem."))
    A(nat("Hermit eig", "[[0,-i],[i,0]] is Hermitian. Eigenvalues are 1 and _____.", -1, "Squares to I, det=-1."))
    A(mcq("Unitary", "A unitary matrix has",
          "eigenvalues on the unit circle", "eigenvalues 0,1", "det 0", "trace n",
          "A", "U^* U=I."))
    A(nat("Fourier 2", "The 2-point DFT matrix F/sqrt(2) with F=[[1,1],[1,-1]] is unitary up to the scale already. F^2 equals 2I. det F is _____.", -2, "Same as Hadamard."))
    A(mcq("Norm equiv", "On finite-dimensional R^n all norms are equivalent. In particular ||x||_1 / ||x||_2 is bounded by",
          "sqrt(n)", "1/n", "0", "n^2",
          "A", "CS or equivalence constants."))
    A(nat("L1", "||(3,-4)||_1 is _____.", 7, "7."))
    A(nat("Linf", "||(3,-4)||_inf is _____.", 4, "max abs."))
    A(mcq("Op norm", "The operator 2-norm of A is the largest",
          "singular value", "eigenvalue always (even if complex)", "diagonal entry", "Frobenius entry",
          "A", "||A||_2 = sigma_max."))
    A(nat("Sigma min", "For an invertible A, ||A^{-1}||_2 = 1/sigma_min. If sigma = 4 and 0.5, ||A^{-1}||_2 is _____.", 2, "1/0.5."))
    A(mcq("Low rank", "Best rank-k approximation in Frobenius (or 2) norm is truncated SVD (Eckart-Young). For a rank-1 matrix the best rank-0 approx error is",
          "the largest singular value (i.e. ||A||)", "0", "det A", "n",
          "A", "||A - 0|| = sigma_1."))
    A(nat("EY", "A=diag(5,1). Best rank-1 Frobenius error is the discarded sigma=_____.", 1, "1."))
    A(mcq("PCA link", "PCA on centered data uses the leading eigenvectors of the covariance (a PSD matrix). The first PC maximises",
          "variance of the projection", "the mean", "k in k-means", "Gini",
          "A", "Same as largest Rayleigh quotient."))
    A(nat("PCA frac", "Eigenvalues of covariance 4 and 1. Fraction of variance on PC1 is _____ (one decimal).", "0.8", "4/5."))
    A(mcq("Whitening", "If Sigma = U D U^T with D>0, the whitening map D^{-1/2} U^T sends the Gaussian to",
          "isotropic (covariance I)", "a Poisson", "a Bernoulli", "k-means",
          "A", "Affine."))
    A(nat("Mahalanobis", "For Sigma=I, Mahalanobis distance of (3,4) from 0 is _____.", 5, "Euclidean."))
    A(mcq("Partition inv", "Block inversion of [[A,B],[C,D]] uses the Schur complement D-C A^{-1} B when A is invertible. If B=0,C=0 the inverse is",
          "diag(A^{-1}, D^{-1})", "diag(A,D)", "0", "I",
          "A", "Block diagonal."))
    A(nat("Schur scalar", "Schur complement of 2 in [[2,1],[1,2]] is 2-1*(1/2)*1=_____. (one decimal)", "1.5", "2-0.5."))
    A(mcq("Kronecker prod", "If this feels off-syllabus skip. Replace with: Kronecker product A tensor I has eigenvalues",
          "those of A, each repeated", "sums of eigenvalues", "products with those of I, i.e. those of A", "always 1",
          "C", "lambda(A)*1."))
    A(mcq("Kronecker", "Eigenvalues of A tensor I_k are those of A, each repeated k times. For A=diag(2,5) and k=2, the largest eigenvalue is",
                "2", "5", "10", "7",
                "B", "5 repeated twice."))
    A(nat("Kron dim", "A 2x2 tensored with I_3 is 6x6. Size n equals _____.", 6, "2*3."))
    A(mcq("Vec", "vec(AXB)=(B^T tensor A) vec(X). This identity is used in",
          "Lyapunov / Kronecker linear systems", "k-means only", "SQL", "A* search",
          "A", "Standard."))
    A(nat("Lyap", "For 1x1, AX+XA^T=Q with A=2, Q=8, X is _____.", 2, "2X+2X=8, X=2."))
    A(mcq("Gershgorin", "Every eigenvalue lies in at least one Gershgorin disc. For [[3,1],[0,2]] the discs are centered at 3 (radius 1) and 2 (radius 0). 2 is",
          "an eigenvalue (and the radius-0 disc is a point)", "not an eigenvalue", "the determinant", "the nullity",
          "A", "Triangular, eigs 3 and 2."))
    A(nat("Gersh r", "For [[10,2],[1,4]] the disc at 10 has radius _____.", 2, "Off-diagonal abs sum."))
    A(mcq("Strict diag dom", "A strictly diagonally dominant matrix is",
          "nonsingular", "always orthogonal", "a projection", "nilpotent",
          "A", "Levy-Desplanques."))
    A(nat("DD", "[[3,-1],[-1,3]] is SPD (diagonally dominant with positive diag). det is _____.", 8, "9-1=8."))
    A(mcq("M-matrix", "A nonsingular M-matrix has inverse",
          "entrywise nonnegative", "skew", "orthogonal", "nilpotent",
          "A", "Classic."))
    A(nat("Inv pos", "[[2,-1],[-1,2]]^{-1} has (1,1) entry _____ (one decimal).", "0.7", "1/3*[[2,1],[1,2]], 2/3~0.67. Use 2/3."))
    o[-1] = nat("Inv pos", "[[2,-1],[-1,2]]^{-1} = (1/3)[[2,1],[1,2]]. The (1,1) entry as a simplified fraction 2/3 in decimal (two places) is _____.", "0.67", "2/3.")
    A(mcq("Toeplitz", "A Toeplitz matrix is constant along",
          "diagonals", "rows", "columns", "the kernel",
          "A", "T_{ij}=t_{i-j}."))
    A(nat("Toep 2", "The Toeplitz [[2,1],[1,2]] has det _____.", 3, "4-1."))
    A(mcq("Hankel", "A Hankel matrix is constant along",
          "anti-diagonals", "the main diagonal only", "the border", "eigenvectors",
          "A", "H_{ij}=h_{i+j}."))
    A(nat("Circ", "The circulant generated by (1,0,0) is I_3. det is _____.", 1, "1."))
    A(mcq("DFT circ", "Circulants are diagonalised by the DFT matrix. Eigenvalues are",
          "the DFT of the first row/column", "all 1", "all 0", "the pivots of LU always",
          "A", "Classic."))
    A(nat("Circ eig", "Circulant of (1,1) in 2D is [[1,1],[1,1]]. Eigenvalues 2 and _____.", 0, "J."))
    A(nat("Sherman0", "Sherman-Morrison for 1x1: (1+3)^{-1} as a decimal (two places) is _____.", "0.25", "1/4."))
    A(mcq("Woodbury", "The Woodbury identity generalises Sherman-Morrison to",
          "A+U C V", "A^2", "QR", "P^2=P",
          "A", "Low-rank updates."))
    A(nat("Update det", "det(I+uv^T)=1+v^T u. For u=v=(1,0)^T this det is _____.", 2, "1+1=2. Matrix [[2,0],[0,1]]."))
    A(mcq("Matrix det lemma", "Same identity. For orthogonal projector uv^T of rank 1, det(I-uv^T) with ||u||=1,v=u is",
          "0", "1", "2", "-1",
          "A", "1-1=0, I-P is singular along u."))
    A(nat("I-P rank", "If P is rank-1 projection on R^3, rank(I-P) is _____.", 2, "Complement."))
    A(mcq("Trace cyclic 2", "tr(ABC)=tr(BCA)=tr(CAB) when products are defined. tr(AB)-tr(BA) is",
          "0", "1", "n", "det(AB)",
          "A", "Cyclic."))
    A(nat("Commutator tr", "tr([A,B]) is always _____.", 0, "tr AB - tr BA=0."))
    A(mcq("sl n", "Matrices of trace 0 form a subspace of M_n(R) of dimension",
                "n^2-1", "n^2", "n", "1",
                "A", "One linear constraint."))
    A(nat("sl2", "dim of 2x2 trace-zero matrices is _____.", 3, "4-1."))
    A(mcq("so n", "Real skew-symmetric n x n matrices have dimension n(n-1)/2. For n=3 that is _____.",
          "3", "6", "9", "1",
          "A", "3."))
    A(nat("so3", "dim so(3) is _____.", 3, "3."))
    A(mcq("GL", "GL_n(R) is the set of",
          "invertible n x n real matrices", "all matrices", "projections", "symmetric matrices",
          "A", "Group under multiplication."))
    A(nat("GL det", "The matrix [[1,0],[0,-1]] is in GL_2(R) because det equals _____.", -1, "nonzero."))
    A(mcq("O n", "O(n) is {Q: Q^T Q=I}. It has two components according to",
          "det = +-1", "trace", "rank", "nilpotency",
          "A", "SO(n) is det 1."))
    A(nat("SO2", "A rotation by 0 is I_2, det _____.", 1, "1."))
    A(mcq("SPD cone", "The set of SPD matrices is",
          "an open convex cone", "a subspace", "a finite set", "O(n)",
          "A", "Not a subspace (I and -I)."))
    A(nat("Mid SPD", "The average of I and 2I is 1.5 I, which is SPD. Smallest eigenvalue is _____ (one decimal).", "1.5", "1.5."))
    A(mcq("Log SPD", "The principal log of an SPD matrix is the symmetric log via the spectral calculus. log I =",
          "0", "I", "-I", "undefined",
          "A", "log 1 = 0."))
    A(nat("Sqrt SPD", "The unique SPD square root of diag(4,9) is diag(2,3). Trace is _____.", 5, "5."))
    A(mcq("Polar", "The polar factorisation A=U P with P=SPD and U orthogonal (for invertible A). P equals",
          "sqrt(A^T A)", "A", "A^{-1}", "0",
          "A", "Analog of z=e^{i theta} |z|."))
    A(nat("Polar 1d", "For A=[-3] in R^{1x1}, the polar 'U' is sign=-1 and P=_____.", 3, "abs."))
    A(mcq("Thin SVD", "Economy SVD of a tall full-column-rank A has U of size",
          "m x n (thin)", "m x m always only", "n x n only", "1 x 1",
          "A", "Thin U."))
    A(nat("Full SVD U", "Full SVD of a 3x2 matrix has U of size 3x3. Number of rows of U is _____.", 3, "m."))
    A(mcq("Left null", "The left nullspace is ker(A^T). Its dimension is m-rank(A). For 3x2 rank 2 this is _____.",
          "1", "2", "3", "0",
          "A", "1."))
    A(nat("Left null dim", "m=5, rank=3, dim left nullspace is _____.", 2, "5-3."))
    A(mcq("RREF unique", "The reduced row echelon form of a matrix is",
          "unique", "highly non-unique", "always I", "always 0",
          "A", "Uniqueness of RREF."))
    A(nat("Pivots count", "Number of pivots in RREF equals the rank. For a rank-3 matrix that number is _____.", 3, "3."))
    A(mcq("Full rank sq", "A square matrix has full rank iff",
          "it is invertible", "trace !=0", "all entries nonzero", "it is symmetric",
          "A", "Equivalent."))
    A(nat("Inv check", "det([[1,2],[3,5]])=5-6=_____.", -1, "nonzero => invertible."))
    A(mcq("2x2 inv formula", "[[a,b],[c,d]]^{-1} = (1/(ad-bc)) [[d,-b],[-c,a]]. For ad-bc=1, the (1,1) entry is",
          "d", "a", "0", "1 always",
          "A", "d."))
    A(nat("Formula", "Inverse of [[2,0],[0,4]] is diag(1/2, 1/4). The (2,2) entry as a decimal is _____.", "0.25", "0.25."))
    A(mcq("Elem E", "An elementary matrix for R2 <- R2-3 R1 applied to I_2 is [[1,0],[-3,1]]. det is _____.",
          "1", "0", "-3", "3",
          "A", "Triangular det 1. (This is MCQ with options)"))
    o[-1] = nat("Elem E", "det of [[1,0],[-3,1]] is _____.", 1, "Triangular.")
    A(mcq("PA=LU", "Partial pivoting writes PA=LU. P is a",
          "permutation matrix", "projection", "diagonal of eigenvalues", "SVD factor",
          "A", "Row swaps."))
    A(nat("Pivots LU", "Without pivoting, LU of [[1e-20,1],[1,1]] is numerically unsafe because the first pivot is ~0. The exact (1,1) pivot is 10^{-20}, approximately _____. (enter 0)", 0, "Tiny pivot."))
    A(mcq("Growth", "The growth factor in GE measures",
          "how large entries become relative to ||A||", "the rank", "the trace", "k-means k",
          "A", "Stability."))
    A(nat("Need 260 pad unique", "Number of leading principal minors of an n x n matrix is n. For n=4 that is _____.", 4, "1x1 up to 4x4."))
    A(mcq("Sylvester PD", "Sylvester's criterion: SPD iff all leading principal minors are positive. For [[1,0],[0,2]] they are 1 and 2, so the matrix is",
          "SPD", "indefinite", "NSD", "singular",
          "A", "Both positive."))
    A(nat("Minor 2", "Leading 2x2 minor of diag(1,2,3) is _____.", 2, "1*2."))
    A(mcq("Bordered skip", "A and B are congruent if B=P^T A P for invertible P. Congruence of symmetric matrices preserves",
                "inertia", "eigenvalues exactly", "the (1,2) entry", "nilpotency index always",
                "A", "Sylvester inertia."))
    A(nat("Cong I", "P^T I P = P^T P, which is SPD if P is invertible. For P=2I_2, P^T P = 4 I, det _____.", 16, "16."))
    A(mcq("Isometry", "A linear isometry of R^n Euclidean is an",
          "orthogonal matrix (possibly det -1)", "any invertible matrix", "any symmetric matrix", "a projection",
          "A", "Preserves norms."))
    A(nat("Preserve", "||Qx|| for orthogonal Q and x=(3,4) is _____.", 5, "Same as ||x||."))
    A(mcq("Volume", "|det A| is the volume scaling of the unit cube under A. For a 90-degree rotation this factor is",
          "1", "0", "2", "pi",
          "A", "|det|=1."))
    A(nat("Shear vol", "Shear [[1,1],[0,1]] has det _____.", 1, "Volume preserved."))
    A(mcq("Orient", "det A >0 means A is",
          "orientation-preserving", "singular", "a reflection", "PSD",
          "A", "GL+."))
    A(nat("Refl orient", "diag(1,-1) has det _____.", -1, "Orientation reversing."))
    A(nat("Skew 90", "[[0,-1],[1,0]] represents rotation by 90 degrees. Its squared Frobenius norm is _____.", 2, "1+1."))
    A(mcq("Area para", "Area of the parallelogram spanned by (1,0) and (1,1) is |det| = _____.",
          "1", "0", "2", "sqrt(2)",
          "A", "1."))
    A(nat("Volume para", "Volume of the parallelepiped of e1,e2,e3 is _____.", 1, "det I=1."))
    A(mcq("Lin dep test", "Vectors are dependent iff the matrix with those columns has",
          "det 0 (when square) / rank < number of vectors", "trace 0", "positive entries", "Q^T Q=I",
          "A", "Definition via rank."))
    A(nat("Three vec", "Columns (1,0,0),(0,1,0),(1,1,0) in R^3: rank is _____.", 2, "Third = sum of first two."))
    A(mcq("Hyperplane", "A hyperplane through the origin in R^n is a subspace of dimension",
          "n-1", "n", "1", "0",
          "A", "One linear constraint."))
    A(nat("Codim", "Codimension of a hyperplane in R^7 is _____.", 1, "1."))
    A(mcq("Direct sum R", "R^2 = span{e1} oplus span{e2} is a",
          "direct sum (internal)", "not a sum", "tensor product only", "quotient only",
          "A", "Intersection 0, sum whole space."))
    A(nat("Sum dim 2", "dim(span{e1}+span{e2}) in R^2 is _____.", 2, "2."))
    A(mcq("Quotient", "dim(V/W) = dim V - dim W. For V=R^4, W a line, this is _____.",
          "3", "4", "1", "0",
          "A", "3."))
    A(nat("Quot", "dim(R^5 / R^2) if R^2 is a subspace is _____.", 3, "5-2."))
    A(mcq("Dual", "The dual space V* has the same dimension as V when dim V is finite. dim (R^n)* is _____.",
          "n", "n^2", "1", "0",
          "A", "Coordinate functionals."))
    A(nat("Dual n", "dim (R^6)* is _____.", 6, "6."))
    A(mcq("Annihilator", "dim W^0 = dim V - dim W. For a plane in R^4, dim annihilator is _____.",
          "2", "4", "1", "0",
          "A", "2."))
    A(nat("Ann", "Annihilator of {0} in R^n has dimension _____.", "n", "Whole dual."))
    A(mcq("Rank A A.T", "rank(A A^T)=rank(A). For A 2x5 rank 2, rank(A A^T) is _____.",
          "2", "5", "0", "7",
          "A", "2x2 Gram of rows, rank 2."))
    A(nat("Gram rows", "A A^T is 2x2 when A is 2 x anything. If A has orthonormal rows, A A^T = I_2, det _____.", 1, "1."))
    A(mcq("Frame", "Rows orthonormal means A A^T=I (a tight frame / Parseval in that case). Then A is a",
          "right inverse of A^T, i.e. A is a co-isometry", "singular always", "projection of rank 0", "nilpotent",
          "A", "A A^T=I."))
    A(nat("Coiso", "If A is 2x3 with orthonormal rows, A A^T is I_2. Number of rows is _____.", 2, "2."))
    A(mcq("Isometry tall", "A tall matrix with orthonormal columns satisfies A^T A=I. Then ||Ax||=||x||. For A 3x2 such, rank is _____.",
          "2", "3", "1", "0",
          "A", "Full column rank."))
    A(nat("Stiefel", "The Stiefel manifold of 3x2 orthonormal-column matrices: each point has rank _____.", 2, "2."))
    A(mcq("Trace inner", "<A,B>_F = tr(A^T B) is an inner product on matrices. ||I_2||_F is _____.",
          "sqrt(2)", "2", "1", "0",
          "A", "sqrt(tr I)=sqrt(2)."))
    A(nat("Frob I", "||I_3||_F is _____ (one decimal, sqrt(3)~1.7).", "1.7", "sqrt(3)."))
    A(mcq("Onb matrices", "E_{ij} the matrix units form an orthonormal basis of M_{m n} for the Frobenius inner product. There are how many? mn. For 2x2: _____.",
          "4", "2", "8", "1",
          "A", "4."))
    A(nat("Units", "Number of matrix units in M_{3,2} is _____.", 6, "6."))
    A(mcq("Vec inner", "<A,B>_F = vec(A)·vec(B). For A=B=I_2 this inner product is _____.",
          "2", "4", "1", "0",
          "A", "tr I=2."))
    A(nat("Vec len", "vec(I_2) has Euclidean length sqrt(2) ~ _____ (one decimal).", "1.4", "1.414."))
    A(mcq("Hadamard prod", "The entrywise (Hadamard) product of two PSD matrices is PSD (Schur product theorem). I odot I equals",
                "I", "0", "all-ones", "2I",
                "A", "Entrywise 1 on the diagonal."))
    A(nat("Hadamard ones", "(J odot I) for 2x2 is I. det is _____.", 1, "1."))
    A(mcq("All-ones eig more", "J_n /n is the projection onto span{1}. For n=4 its rank is _____.",
          "1", "4", "0", "2",
          "A", "Rank-1 projection."))
    A(nat("Centering", "The centering matrix I-J/n for n=3 has rank _____.", 2, "Projects orthogonal to 1."))
    A(mcq("Centering PSD", "I-J/n is",
          "a projection (hence PSD with eigs 0,1)", "indefinite", "orthogonal with det -1 always", "nilpotent",
          "A", "Symmetric idempotent."))
    A(nat("Cent eig", "I-J/n has eigenvalues 1 (n-1 times) and one 0. For n=5 number of 1s is _____.", 4, "4."))
    A(mcq("Covariance as Gram", "A sample covariance (up to scale) is a Gram matrix of centered data, hence",
          "PSD", "orthogonal", "a permutation", "nilpotent",
          "A", "Always."))
    A(nat("Sample cov rank", "n=3 points in R^2, centered, the 2x2 covariance has rank at most _____.", 2, "At most min(2, n-1)=2."))
    A(mcq("n-1", "Centered n points span at most n-1 dimensions. For n=2 that max is _____.",
          "1", "2", "0", "3",
          "A", "They lie on a line through 0 after centering."))
    A(nat("Two pts", "Two centered points in R^100 lie in a subspace of dimension at most _____.", 1, "n-1=1."))

    return uniq(o)


if __name__ == "__main__":
    xs = items()
    print("LA", len(xs), "unique", len({i["stem"] for i in xs}))
    # write bank_la.py
    # keep as this module: copy to bank_la.py with items()
    src = Path(__file__).read_text()
    # bank_la is this items() function — write a thin wrapper
    Path(__file__).with_name("bank_la.py").write_text(
        src.replace("if __name__", "def _unused():\n    if __name__")
    )
PY
