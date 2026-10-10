# V2 part 1 — Tools: Hoffman constants via minors, semialgebraic exactification, threshold buffer

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, F = supp a finite.
Notation of the Round-6 reports: ladder index l = j(k,m); carrier l has vector u_l, d-coefficient
q_l = eps_l Phi_l w_m(k)/(m C_m); value val_l := eps_l u_l(zhat); A_m := |R_m^** zhat|_m (so sigma_m = q_0 A_m).
At a strict non-peak k(l) of block m (Lemma lem:threshold, Z6 2.1, Y4-ref C.7, V1 Lemma ST(d)):
    q_l = val_l / A_m = (q_0/sigma_m) val_l.                                                         (1.0)
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Scripts: ctx/r7/V2_work/.

## 1.1 Lemma H (Hoffman bound through linearly independent row sets and minors).  PROVED.
Let A in R^{p x n}, b in R^p, and P := {x in R^n : Ax <= b} nonempty.  Call J subset {1..p} *independent* if J is
nonempty and the rows A_i (i in J) are linearly independent; A_J denotes the |J| x n submatrix, sigma_min(A_J) > 0 its
smallest singular value.  Then for every x in R^n
    dist_2(x, P) <= ||(Ax - b)_+||_2 * max{ 1/sigma_min(A_J) : J independent }                     (1.1)
(the maximum over the empty family is 0, which happens only if A = 0).  Moreover, for every independent J,
    sigma_min(A_J) >= max_K |det A_{J,K}| / ||A_J||_2^{|J|-1}        (K ranges over |J|-subsets of columns),   (1.2)
and the maximum in (1.2) is positive.  Consequently, with delta(A) := min{ |det A_{J,K}| : |J| = |K| >= 1, det A_{J,K} != 0 },
    dist_2(x, P) <= max(1, ||A||_2)^{n-1} delta(A)^{-1} ||(Ax - b)_+||_2 .                          (1.3)
Equality constraints Ex = e are included by writing them as Ex <= e, -Ex <= -e: an independent set never contains a
row together with its negative, the residual becomes |Ex - e|, and delta is computed for the matrix [A; E].
Proof.  Let x* be the Euclidean projection of x onto the closed convex set P.  Then x - x* lies in the normal cone of P
at x*, which for a polyhedron is cone{A_i^T : A_i x* = b_i} (Farkas' lemma).  By the conic Caratheodory theorem,
x - x* = sum_{i in J} v_i A_i^T with v_i > 0 and J independent (or x = x*, and there is nothing to prove).  Since
A_i x* = b_i for i in J,
    ||x - x*||_2^2 = sum_{i in J} v_i A_i (x - x*) = sum_{i in J} v_i (A_i x - b_i) <= ||v||_2 ||(A_J x - b_J)_+||_2 ,
using v >= 0.  As x - x* = A_J^T v and A_J^T is injective, ||v||_2 <= ||x - x*||_2 / sigma_min(A_J).  Dividing gives (1.1).
For (1.2): if s_1 >= ... >= s_k > 0 (k = |J|) are the singular values of A_J, then by the Cauchy-Binet formula
s_1^2 ... s_k^2 = det(A_J A_J^T) = sum_K det(A_{J,K})^2 >= max_K det(A_{J,K})^2 > 0 (positive since A_J has rank k), so
s_k >= (s_1 ... s_k)/s_1^{k-1} >= max_K |det A_{J,K}| / ||A_J||_2^{k-1}.  (1.3) follows since every positive max in (1.2)
is >= delta(A), ||A_J||_2 <= ||A||_2 and |J| <= n.  QED
Remarks.  (a) Only the NONZERO minors matter: a configuration in which some minors vanish exactly has a bounded
Hoffman constant; trouble comes only from minors that are small but nonzero.  (b) Hoffman constants do not depend on
the right-hand sides (b, e); (1.3) holds for every b with P nonempty.  (c) l_1/l_infty versions follow with factors
sqrt(n), sqrt(p).  Numerics (V2_work/hoffman_minors_check.py): 1500 random tests, max dist/(bound (1.1)) = 1.0000 (the
bound is attained for single active rows), per-J ratio (1/sigma_min)/(bound (1.2)) <= 1.0000.

## 1.2 Lemma L (simultaneous exactification of polynomial objects).  PROVED (Lojasiewicz inequality).
Let pi_1, ..., pi_s be real polynomials in n variables and Q := [-2, 2]^n.  There are C_L >= 1 and an integer N_L >= 1,
depending only on (pi_1, ..., pi_s), such that for every S subset {1..s} and every v in Q with max_{i in S} |pi_i(v)| <= beta,
0 <= beta <= 1, at least one of the following holds:
    (i) beta >= 1/C_L;
    (ii) there is v' in R^n with pi_i(v') = 0 for all i in S and ||v' - v||_2 <= C_L beta^{2/N_L}.
Proof.  Fix S, put F_S := sum_{i in S} pi_i^2 and Z_S := F_S^{-1}(0) subset R^n.  Let g_S(v) := dist_2(v, Z_S) if Z_S is
nonempty and g_S(v) := 1 for all v otherwise.  F_S and g_S are continuous semialgebraic functions on the compact semialgebraic set Q,
and F_S^{-1}(0) cap Q subset g_S^{-1}(0).  By the Lojasiewicz inequality (Bochnak-Coste-Roy, Real Algebraic Geometry,
Cor. 2.6.7) there are an integer N_S >= 1 and C_S > 0 with g_S(v)^{N_S} <= C_S F_S(v) on Q.  If Z_S is empty this
reads 1 <= C_S F_S(v) <= C_S |S| beta^2, i.e. (i) with any C_L >= (C_S |S|)^{1/2}.  Otherwise a nearest point v' of Z_S
satisfies ||v' - v||_2 = g_S(v) <= (C_S |S| beta^2)^{1/N_S}.  Take N_L := max_S N_S and C_L := max_S max((C_S s)^{1/2},
(C_S s)^{1/N_S}, 1) (for beta <= 1, beta^{2/N_S} <= beta^{2/N_L}).  QED
Remarks.  (a) C_L, N_L are well-defined numbers once the polynomials are fixed (e.g. take for each S the least
admissible N_S and then C_S := 1 + the infimum of admissible constants).  When the polynomials are design data of level
l (below), C_L(l), N_L(l) are design constants computable in principle at stage l of the recursion; only their
existence is used.  (b) Lemma L is the only place where a non-explicit exponent enters; the design absorbs it by
choosing b(w) as a power of T_lo(w) that depends on N_L(l) (Part 2).  (c) The exponent cannot be 1 in general: the
nearest common zero of tiny polynomials can be at distance (tiny)^{1/2} (e.g. v_1^2 + v_2 tiny with v_2 >= 0 forced).

## 1.3 Lemma QB (threshold buffer through a peak).  PROVED (from Y1 Lemma T2(b), Corollary T3; refereed).
One block; zeta in l_1 \ {0}, theta := theta(zeta) (Lemma T: root of Psi), A := |zeta|, phi := ||Phi||_2^2,
nu_k := |zeta(k)|/Phi_k^2 (k is a peak iff nu_k >= theta).  Let c be a peak, s > 0, and zeta' with
sgn zeta'(c) = sgn zeta(c), |zeta'(c)| = |zeta(c)| + s, and E := sum_{k != c} |zeta'(k) - zeta(k)| <= A s/(8(A + theta + 1)).
Let L be any set of coordinates (in applications: the coarse carriers of the block) and put
R(s) := min{1, A s/(8 phi (A + theta + 1))} and X := sup_{k in L, k != c} |zeta'(k) - zeta(k)|/Phi_k^2.  Then
 (a) theta(zeta') >= theta + R(s);
 (b) every k in L \ {c} with nu_k < theta + R(s) - X (in particular every strict non-peak in L, if R(s) > X) is a strict
     non-peak of zeta';
 (c) if C_1(s + E) < h_0 (C_1, h_0 as in Y1 Lemma T2: C_1 = (1 + 2(theta+1)/A)/Phi_{k_0}^2, h_0 = min(1, nu_{k_0} - theta) for
     a fixed non-degenerate peak k_0 != c), then theta(zeta') <= theta + C_1(s + E), and every k in L \ {c} with
     nu_k > theta + C_1(s + E) + X is a peak of zeta' with the sign of zeta(k).
(Coordinates outside L, e.g. fine carriers, may change status; only E, a weighted l_1 quantity, involves them.)
Proof.  (a) is Y1 Lemma T2(b).  (b) nu'_k <= nu_k + X < theta + R(s) <= theta(zeta').  (c) the upper bound is the second
statement of T2(b); then nu'_k >= nu_k - X > theta(zeta'), and sgn zeta'(k) = sgn zeta(k) because
|zeta'(k) - zeta(k)| <= X Phi_k^2 < nu_k Phi_k^2 = |zeta(k)|.  QED
Use.  A buffer peak c is pushed OUTWARD (|value| raised) by a tiny controlled amount; all other moves of the block (the
tuning of Part 2) are the perturbation E, X.  Choosing s with R(s) > X protects every strict non-peak (including the
near-threshold "NT" carriers of Y4-ref C.7 / V1 (K4)), and (c) protects every peak whose margin exceeds C_1(s+E) + X.
Remarks.  (a) Y2/Y1/V1 realize the push by a donor (z-move at an unused signature set); with a diagonal base the push
can be realized at ANY coarse peak whose carrier has infinitely many far contacts or far free coordinates, by banks /
pulls / z-moves (Y4-ref C.6 Prop. P4 / V1 Lemma TU and their proofs; Theorem B, Step 4), in either direction.  (b) Every block has, at
every level l >= l_f, a coarse non-degenerate peak c with |alpha_m(c)| >= 1/(2l) (Part 2, Lemma 2.3), so a buffer
peak with design-controlled constants always exists.
