# lipzero -- NA(Lip_0(M), Y) for finite-dimensional Y (domain Lip_0(M) = F(M)^*)

Key: lipzero. Real scalars throughout. Written 2026-10-30 by a workflow subagent.
Labels: PROVED (complete proof written here), KNOWN (reference; "confirmed" = a web-search hit,
URL in Section 8; "FROM MEMORY" = not confirmed by search), SKETCH, HEURISTIC, OPEN, FALSE.
Network: arxiv/ar5iv/ugr were not used (unreachable). The single allowed WebFetch try
(www.math.fu-berlin.de, Werner's preprint of KLMW) failed with ENOTFOUND: that host would have to be
allowed in the session's network settings. Everything "confirmed" below is from WebSearch snippets.

## 0. Summary

VERDICT: OPEN. "NA(Lip_0(M),Y) is dense for every pointed metric space M and every finite-dimensional
Y" is not known, is not proved here, and is not known to be equivalent to the Johnson-Wolfe (JW)
question (only "JW positive => statement" is trivial). A counterexample would refute JW (none expected).

PROVED here (full proofs below, modulo standard KNOWN facts that are named):
 (1) Thm 3.5: C(K) has LOCAL lineability (LL) (definition below): every finite family in C(K)^* is a
     small perturbation of a family spanning a subspace of NA(C(K),R). Hence P(C(K)). This is the
     finite-rank content of Johnson-Wolfe for C(K) (Riesz + inner regularity + Tietze).
 (2) Prop 3.7/3.8: P(Lip_0(M)) whenever F(M) is isometric to SOME L_1(mu) (no sigma-finiteness
     needed: Lip_0(M) = L_1(mu)^* is a C(K) by Kakutani). Godard's hypothesis "closure of M contains
     the branching points of its convex hull" is NEEDED: the claim "closed subset of an R-tree =>
     F(M) = L_1(mu)" is FALSE (equilateral triangle, Example 3.6). Self-contained proof for M in R.
     Conversely the JW hypothesis (Lip_0(M)^* an L-space) forces M to be tree-like (Godard).
 (3) Thm 3.9 (new as far as we know): every weak*-closed finite-codimensional subspace
     X = {h in L_oo(mu) : int h g_l dmu = 0, l <= b} (mu sigma-finite, g_l in L_1(mu)) has (LL),
     hence P(X). Mechanism: L_1 best-approximation duality + "cushions" (small L_1 densities that
     blow up on the supports of the singular parts).
 (4) Cor 3.10/Prop 3.11: P(Lip_0(G)) for every connected metric graph G (geodesic metric, countably
     many edges) with FINITE first Betti number: circle, theta graph, every finite graph, R with
     finitely many loops. If G has a cycle, JW does NOT apply (Lip_0(G)^* is not an L-space). These
     are the first INFINITE non-tree-like M we know of with P(Lip_0(M)) (finite M are trivial).
 (5) Reductions: weak*-continuous finite-rank operators on dual spaces attain their norm (dense iff
     the predual is reflexive; for Lip_0(M) iff M finite); T** = T o pi iff T is weak*-continuous
     (so Lindenstrauss' biadjoint theorem does not decide the question); wedge sums give l_oo-sums;
     P passes from Lip_0(M_1 v M_2) to Lip_0(M_i); (LL) is stable under finite wedges; the converse
     for two arbitrary pieces is OPEN (a failure would refute JW).
 (6) Lineability: F(M) (inside NA) is dense only for finite M. C(K): scattered K => dense lineable;
     non-scattered K: dense lineability OPEN (KLMW state it is unknown for C_0(L); confirmed). We
     prove a structure lemma for 2-dim subspaces of NA(C(K)) and obstructions (e.g. no linear subspace
     of NA(L_oo(mu),R) contains g.mu with g != 0 a.e. together with a nonzero singular functional).
     JW-type density needs only (LL), not global lineability.
 (7) Transfer: X^* is 1-complemented in Lip_0(X) (invariant means; Prop 5.1). The summand argument
     (AD) fails for X^* in Lip_0(X) (Example 5.2). "P(Lip_0(X)) => P(X^*)": OPEN. Universality of
     dual spaces: OPEN. c_0, hence every renorming of c_0 (Read, Martin), is not complemented in any
     dual space (Prop 5.3), so summand arguments cannot move Martin-type candidates into duals; and
     "P passes to closed subspaces" and "P passes to exact quotients" are each EQUIVALENT to a
     positive JW answer (Prop 5.4).
 (8) Lip_0(R^n), n >= 2 (Euclidean): isometric to the curl-free fields in L_oo(R^n; l_2^n); none of
     the known tools applies; OPEN. Simplest open cases: R^2, the 2-torus, the planar grid graph,
     the Hawaiian earring (infinitely many cycles).

Notation. NA(X,Y) = {T in L(X,Y) : ||Tx|| = ||T|| for some x in S_X}.
P(X): NA(X,F) is dense in L(X,F) for every finite-dimensional F.
AA(X,F) := {S in L(X,F) : S^* y^* in NA(X,R) for every y^* in F^*}.
(LL) local lineability: for all phi_1..phi_d in X^* and eps > 0 there are psi_1..psi_d in X^* with
     ||psi_i - phi_i|| < eps and span{psi_1..psi_d} contained in NA(X,R).
(DL) dense lineability: NA(X,R) contains a norm-dense linear subspace of X^* (the KLMW criterion,
     Preprint B Lemma densesubspace).
M = (M,d,0) pointed metric space; Lip_0(M) with norm L(f) (best Lipschitz constant); F(M) = closed
span of {delta_x} in Lip_0(M)^*; F(M)^* = Lip_0(M) isometrically; on bounded sets the weak* topology
is pointwise convergence. M~ := {(x,y) in M^2 : x != y}.

## 1. Basic lemmas

Lemma 1.1 (adjoint criterion) -- PROVED. Y finite-dimensional, T in L(X,Y). Then T in NA(X,Y) iff
there is y^* in S_{Y^*} with ||T^* y^*|| = ||T|| and T^* y^* in NA(X,R).
Proof. (=>) Let x in S_X with ||Tx|| = ||T||; Hahn-Banach gives y^* in S_{Y^*} with
y^*(Tx) = ||Tx||. Then (T^*y^*)(x) = ||T|| >= ||T^*y^*||, so ||T^*y^*|| = ||T|| and T^*y^* attains
its norm at x. (<=) If T^*y^* attains its norm at x in S_X, then ||Tx|| >= y^*(Tx) = ||T^*y^*|| =
||T|| >= ||Tx||. QED. (y^* -> ||T^*y^*|| is continuous on the compact S_{Y^*}; maximizers exist.)

Lemma 1.2 -- PROVED. (a) (DL) => (LL). (b) (LL) <=> AA(X,F) is dense in L(X,F) for every
finite-dimensional F. (c) (LL) => P(X).
Proof. (a) Approximate each phi_i by psi_i in the dense subspace V; span{psi_i} lies in V, inside NA.
(b) "=>": let F have basis y_1..y_d and T = sum_i phi_i (x) y_i. Take psi_i from (LL) and
S = sum_i psi_i (x) y_i; ||S - T|| <= sum_i ||psi_i - phi_i|| ||y_i||, and S^* y^* =
sum_i y^*(y_i) psi_i lies in span{psi_i}, inside NA(X,R). "<=": given phi_1..phi_d put F = l_oo^d,
T = (phi_1,..,phi_d), choose S in AA(X,F) with ||S - T|| < eps and psi_i := S^* e_i^*. Then
||psi_i - phi_i|| = ||(S - T)^* e_i^*|| <= ||S - T|| < eps and span{psi_i} = S^*(F^*) lies in NA.
(c) If S in AA(X,F), pick y_0^* in S_{F^*} maximizing ||S^* y^*||; S^* y_0^* attains, so S is in
NA(X,F) by Lemma 1.1. Combine with (b). QED

Remark 1.3 -- PROVED modulo KNOWN results. P does not imply (LL). Read's renorming R of c_0 has no
2-dimensional subspace inside NA(R,R) (Rmoutil, J. Funct. Anal. 272 (2017) 918-928; confirmed), so
(LL) fails already for d = 2; but NA(R,F) is dense for every reflexive F (Preprint B, abstract and
Theorem read-finite-density), so P(R) holds. Thus (LL) is a sufficient mechanism, not a necessary one.

Remark 1.4 -- PROVED. P, (LL), (DL) are isometric properties; isomorphic information such as
"Lip_0(M) is isomorphic to l_oo" says nothing about them: e.g. c_0 has (DL) (finitely supported
vectors of l_1), while Read's renorming of c_0 fails (LL) (Remark 1.3).

## 2. Literature (task item (a))

L1 Lindenstrauss, Israel J. Math. 1 (1963) 139-148. Properties A and B; reflexive X has A; property
   beta of Y implies B (finite-dim polyhedral Y have B); for ALL X, Y the set {T : T^** attains its
   norm} is dense in L(X,Y). KNOWN, confirmed (Martin's notes / arXiv 1306.1155 snippets).
L2 Johnson-Wolfe, Studia Math. 65 (1979) 7-19 (paper confirmed: eudml.org/doc/218261). Density of NA
   operators for C(K) domains (and for ranges L_1 or preduals of L_1, real case): confirmed only via
   a secondary-source snippet (survey quoting the paper). The formulation "if X^* is isometric to an
   L_1(mu) (X a real L_1-predual), then every compact operator from X into any Y is a limit of
   norm-attaining finite-rank operators" is FROM MEMORY; KLMW (confirmed snippet) state the same
   conclusion for C_0(L) and for isometric preduals of l_1. Our Theorem 3.5 is self-contained for
   C(K) and finite-dimensional ranges, so nothing below depends on the exact JW wording.
L3 Schachermayer, Pacific J. Math. 105 (1983): weakly compact operators from C(K) are limits of NA
   operators; NA(C(K),L_1[0,1]) and NA(C(K),l_2) dense; NA(L_1[0,1],C[0,1]) not dense. KNOWN,
   confirmed snippet. Property alpha => property A (Israel J. Math. 44 (1983)): FROM MEMORY.
L4 Bourgain 1977 (RNP => property A): confirmed (Werner's 2019 slides snippet). Uhl 1976 (finite-rank
   NA operators dense in K(L_1(mu),Y)): confirmed (Martin survey snippet).
L5 BPBp with C(K)/L_oo domains: Kim-Lee, J. Math. Anal. Appl. 2015 (arXiv 1407.7872): (C(K),Y) has the
   Bishop-Phelps-Bollobas property for every uniformly convex Y; Kim-Lee-Lin, J. Nonlinear Convex
   Anal. 2016: (L_oo(mu),Y) has the BPBp for EVERY measure space and uniformly convex Y; Acosta,
   Banach J. Math. Anal. 2016: complex C_0(L). KNOWN, confirmed snippets. Consequence: NA(C(K),l_2^n),
   NA(L_oo(mu),l_2^n) dense -- an independent route for strictly convex finite-dim Y, with no
   sigma-finiteness. (Not for finite-dim Y that are neither polyhedral nor strictly convex; Thm 3.5
   covers every finite-dim Y.)
L6 KLMW = Kadets-Lopez-Martin-Werner, "Norm attaining operators of finite rank", in: The Mathematical
   Legacy of Victor Lomonosov, De Gruyter 2020, 157-188 (arXiv 1905.08272). Confirmed snippets: a
   dense linear subspace of NA(X,R) gives density of finite-rank NA operators among finite-rank ones
   (with AP of X^*: among compact ones); isometric preduals of l_1 and L_1(mu) have such a subspace;
   NA functionals form a linear space for c_0, K(l_2) and their finite-codimensional proximinal
   subspaces; "For C_0(L), we do not know whether it is actually true that NA(C_0(L)) contains a
   dense linear subspace."
L7 Rmoutil, J. Funct. Anal. 272 (2017) 918-928 (arXiv 1503.06112): NA of Read's space contains no
   2-dimensional subspace. Confirmed.
L8 Godard, Proc. Amer. Math. Soc. 138 (2010) 4311-4320 (arXiv 0904.3178): F(M) is isometric to a
   subspace of L_1 iff M embeds isometrically into an R-tree; if T is an R-tree and A is a subset of T
   with Br(T) contained in the closure of A, then F(A) is isometric to L_1(mu_{cl A}) (cited as
   Godard Cor. 3.4 by DKP). Confirmed snippets.
L9 Dalet-Kaufmann-Prochazka, Bull. Belg. Math. Soc. 23 (2016) (arXiv 1502.02719): for negligible M in
   an R-tree, F(M) = l_1 isometrically iff M contains all branching points of its convex hull; the
   free space of an ultrametric space with >= 3 points is never isometric to l_1. Aliaga-Petitjean-
   Prochazka, J. Funct. Anal. 2021 (arXiv 1909.05285): (almost) isometric embeddings into l_1.
   Confirmed.
L10 Godefroy-Kalton, Studia Math. 159 (2003) 121-141: Lipschitz-free spaces; for separable X the
   barycentre map F(X) -> X has a linear isometric right inverse (confirmed: abstract snippet), whose
   adjoint is a weak*-continuous norm-one projection Lip_0(X) -> X^*. Lindenstrauss, Michigan Math.
   J. 11 (1964), "On nonlinear projections in Banach spaces": X^* is 1-complemented in Lip_0(X) via
   invariant means: FROM MEMORY (proof reproduced in Prop 5.1).
L11 Cuth-Kalenda-Kaplicky, Mathematika 63 (2017) 538-552 (arXiv 1610.03966): for a convex open Omega
   in a finite-dimensional normed space, F(Omega) = L_1(Omega;R^d)/{fields with zero distributional
   divergence}. Confirmed.
L12 Kalton, Collect. Math. 55 (2004) 171-217 (existence confirmed); Cuth-Doucha-Wojtaszczyk, Proc. AMS
   144 (2016) (arXiv 1505.07209): F(M) contains a complemented copy of l_1 for every infinite M
   (confirmed). "Lip_0(M) isomorphic to l_oo": only the 1-dimensional cases Lip_0(R) = L_oo,
   Lip_0(Z) = l_oo were confirmed (Aliaga-Medina, arXiv 2601.03131, snippet; they record that it is
   asked whether Lip_0(X) and Lip_0(N_X) are isomorphic for nets N_X). The general statements
   attributed to Kalton/CDW in the task were NOT confirmed (FROM MEMORY at best). Irrelevant anyway:
   Remark 1.4.
L13 Naor-Schechtman, SIAM J. Comput. 37 (2007) (arXiv cs/0509074): the transportation-cost metric on
   probability measures on {0..n}^2 needs distortion Omega(sqrt(log n)) into L_1 (confirmed); hence
   F(R^2) is not isomorphic to a subspace of L_1 (free-space formulation FROM MEMORY).
L14 Notions that FAIL but are DIFFERENT (Section 6): Kadets-Martin-Soloviova, Banach J. Math. Anal. 10
   (2016) 621-637: strongly norm-attaining Lipschitz functionals SNA(M,R) are not dense for geodesic
   M (e.g. [0,1]); Chiclana-Garcia-Lirola-Martin-Rueda Zoca (SNA density theory). Confirmed snippets.
L15 Norm-attaining operators FROM Lip_0(M) (the question here): no paper found (searches return only
   SNA, F(M)-domain and BPBp-for-Lipschitz-maps papers). Negative search result, not a proof of
   absence.

## 3. Reductions (task item (b))

### 3.1 Weak*-continuous operators; Lindenstrauss' biadjoint theorem

Prop 3.1 -- PROVED. Let X = Z^* be a dual space and Y finite-dimensional.
(a) Every weak*-to-norm continuous S in L(X,Y) attains its norm.
(b) S is weak*-continuous iff S = sum_i J_Z(z_i) (x) y_i with z_i in Z, i.e. iff S^*(Y^*) is
    contained in J_Z(Z) (J_Z : Z -> Z^** canonical).
(c) The weak*-continuous operators are norm dense in L(X,Y) (Y != 0) iff Z is reflexive.
(d) For X = Lip_0(M), Z = F(M): they are dense iff M is finite.
Proof. (a) B_X is weak*-compact (Alaoglu) and x -> ||Sx|| is weak*-continuous on it, so the supremum
is a maximum, attained at some x of norm 1 if S != 0 (if ||x|| < 1, x/||x|| gives a larger value).
(b) Write S = sum_i phi_i (x) y_i (basis y_i, phi_i in X^* = Z^**). S is weak*-to-norm continuous iff
each phi_i is weak*-continuous on Z^*, iff phi_i in J_Z(Z) (the weak*-continuous functionals on a
dual space are exactly the elements of the predual). (c) The set W := {S : S^*(Y^*) in J_Z Z} is
norm closed (J_Z Z is closed in Z^**). If W is dense it is everything; then phi (x) y in W for every
phi in Z^** and y != 0, so Z^** = J_Z Z. Conversely reflexive Z gives W = L(X,Y). (d) If M is finite,
F(M) is finite-dimensional. If M is infinite, F(M) contains a complemented copy of l_1 (CDW 2016,
KNOWN, confirmed), so it is not reflexive. QED

Prop 3.2 -- PROVED. X = Z^*, pi := (J_Z)^* : Z^*** -> Z^* (pi(Xi) = Xi o J_Z), a norm-one
projection onto Z^* (identified with J_{Z^*}(Z^*)). For Y finite-dimensional and T in L(X,Y):
T^** = T o pi  iff  T is weak*-continuous.
Proof. T = sum_i phi_i (x) y_i, phi_i in Z^**. For Xi in X^** = Z^***: T^**(Xi) = sum_i Xi(phi_i) y_i
and T(pi Xi) = sum_i phi_i(pi Xi) y_i. If phi_i = J_Z z_i then phi_i(pi Xi) = (pi Xi)(z_i) =
Xi(J_Z z_i) = Xi(phi_i). Conversely, if T^** = T o pi, take Xi in the annihilator (J_Z Z)^perp inside
Z^***: then pi Xi = 0, hence Xi(phi_i) = 0 for all such Xi, so phi_i lies in the weak-closure of
J_Z Z, i.e. in J_Z Z (Hahn-Banach; J_Z Z is norm closed). QED
Consequence (PROVED). Lindenstrauss' theorem (L1) gives a dense set of T in L(Lip_0(M),Y) whose
biadjoints attain their norms on B_{Lip_0(M)^**}; via pi the attainment point can be pushed back to
B_{Lip_0(M)} only when T^** = T o pi, i.e. only for weak*-continuous T, which are dense only for finite
M (Prop 3.1(d)). So Lindenstrauss' theorem does not decide P for dual spaces, in particular not for
Lip_0(M).

### 3.2 Wedge sums

Prop 3.3 -- PROVED. Let (M_i, d_i, 0_i), i in I (I nonempty), be pointed metric spaces. The wedge
M = v_i M_i is the disjoint union with all base points identified to one point 0, with
d(x,y) = d_i(x,y) if x, y in M_i, and d(x,y) = d_i(x,0) + d_j(0,y) if x in M_i, y in M_j, i != j.
Then R(f) := (f|M_i)_i is an onto linear isometry Lip_0(M) -> (+)_{l_oo} Lip_0(M_i), and a
homeomorphism for the pointwise (= weak*) topologies on bounded sets. Consequently
F(M) = (+)_{l_1} F(M_i) isometrically.
Proof. d is a metric: symmetry and positivity are clear; the triangle inequality d(x,z) <= d(x,y) +
d(y,z) reduces in each placement of x, y, z among the pieces to the triangle inequality of one d_i
together with d(x,y) = d(x,0) + d(0,y) across pieces (e.g. x, z in M_i, y in M_j: d_i(x,z) <=
d_i(x,0) + d_i(0,z) <= d(x,y) + d(y,z); x in M_i, y, z in M_j: d(x,z) = d_i(x,0) + d_j(0,z) <=
d_i(x,0) + d_j(0,y) + d_j(y,z)). Each restriction has norm <= 1, so L(f) >= sup_i L(f|M_i). For
x in M_i, y in M_j, i != j: |f(x) - f(y)| <= |f(x) - f(0)| + |f(0) - f(y)| <= L(f|M_i) d_i(x,0) +
L(f|M_j) d_j(0,y) <= (sup_k L(f|M_k)) d(x,y); pairs in one piece are trivial. So R is isometric.
Onto: a bounded family (f_i) with f_i(0) = 0 glues to a well-defined f. Pointwise convergence of a
bounded net in Lip_0(M) is pointwise convergence in every piece. The l_1-sum of the F(M_i) is a
predual of the l_oo-sum whose induced weak* topology agrees with the pointwise one on bounded sets,
and it contains the deltas of M (delta_x = the element supported in the piece of x); so F(M) is
isometric to it. QED

Cor 3.4. (i) PROVED (any Y): if NA(Lip_0(M_1 v M_2),Y) is dense then NA(Lip_0(M_k),Y) is dense,
k = 1, 2. More generally every summand of an l_oo-sum inherits density.
Proof (the (AD) argument of sums_tensors Theorem 2, written for X = X_1 (+)_oo W). Let T_1 in
L(X_1,Y), ||T_1|| = 1, 0 < eps < 1/4, T := T_1 P_1 (P_1(x_1,w) = x_1, ||T|| = 1). Let S in NA(X,Y)
with ||S - T|| < eps, attaining at x = (x_1,w) in S_X. Put S_1 := S(.,0), S_W := S(0,.); then
||S_W|| < eps, ||S_1 - T_1|| < eps, 1 - eps < ||S||. With c := ||x_1|| (note ||w|| <= 1):
||S|| = ||S_1 x_1 + S_W w|| <= ||S|| c + eps, so c >= 1 - eps/||S|| > (1-2eps)/(1-eps) > 0.
Pick phi in S_{X_1^*} with phi(x_1) = c and define E u := (u, (phi(u)/c) w) in X. Then
||Eu|| = max(||u||, |phi(u)| ||w||/c) <= ||u||/c (as c <= 1 and ||w|| <= 1). R := S o E. Since
E(x_1/c) = (x_1/c, w/c) = x/c, ||R(x_1/c)|| = ||S||/c >= ||S|| ||E|| >= ||R|| and ||x_1/c|| = 1,
so R in NA(X_1,Y). Finally ||R - S_1|| <= ||S_W||/c, hence ||R - T_1|| < eps/c + eps < 3 eps. QED
(ii) PROVED: finite l_oo-sums (finite wedges) of (LL)-spaces have (LL). Proof. (X_1 (+)_oo X_2)^* =
X_1^* (+)_1 X_2^*. Given phi_i = (phi_i^1, phi_i^2), apply (LL) in X_k to (phi_i^k)_i, getting psi_i^k
with span{psi_i^k}_i inside NA(X_k). For eta in R^d, the functional (sum eta_i psi_i^1, sum eta_i
psi_i^2) has both components attaining, at z_1, z_2 (any unit vector for a zero component); (z_1,z_2)
has norm 1 and the value is ||.||_1 + ||.||_2, the norm of the functional. QED
(iii) KNOWN from the sums_tensors notes (Prop 6 there, PROVED there): if P(Lip_0(M_1)) and AA is dense
for Lip_0(M_2) (e.g. M_2 finite, or Lip_0(M_2) with (LL)), then P(Lip_0(M_1 v M_2)).
(iv) OPEN: P(Lip_0(M_1)) and P(Lip_0(M_2)) => P(Lip_0(M_1 v M_2)) in general (instance of the open
l_oo-sum question (C_oo) of the sums_tensors notes; true if JW is positive, a failure refutes JW).

### 3.3 C(K): the Johnson-Wolfe mechanism for finite-dimensional ranges

Lemma 3.5a -- PROVED. mu in M(K) = C(K)^* attains its norm iff supp mu^+ and supp mu^- are disjoint.
Proof. (<=) Disjoint closed sets in the normal space K: Urysohn gives f in C(K), -1 <= f <= 1,
f = 1 on supp mu^+, f = -1 on supp mu^-; mu(f) = ||mu^+|| + ||mu^-|| = ||mu||. (=>) If |f| <= 1 and
mu(f) = ||mu||, then int (1 - f) dmu^+ + int (1 + f) dmu^- = 0, so f = 1 mu^+-a.e. and f = -1
mu^--a.e.; {f = 1} is closed of full mu^+-measure, hence contains supp mu^+; likewise
{f = -1} contains supp mu^-; these are disjoint. QED

Theorem 3.5 -- PROVED. For every compact Hausdorff K, C(K) has (LL). Hence P(C(K)), and AA(C(K),F) is
dense for every finite-dimensional F. (This is the finite-rank content of Johnson-Wolfe.)
Proof. Let mu_1..mu_d in M(K) (regular Borel signed measures; Riesz) and eps > 0.
Step 1. rho := sum_i |mu_i| is a finite positive regular Borel measure and |mu_i| <= rho; by
Radon-Nikodym mu_i = h_i rho with |h_i| <= 1 rho-a.e.
Step 2. Simple functions are dense in L_1(rho); taking a common refinement there are a finite Borel
partition {A_1..A_n} of K and reals c_ij with sum_i int |h_i - sum_j c_ij 1_{A_j}| drho < eps.
Step 3. Inner regularity: compact K_j contained in A_j with sum_{i,j} |c_ij| rho(A_j \ K_j) < eps.
Step 4. nu_j := rho restricted to K_j (positive, concentrated on K_j), psi_i := sum_j c_ij nu_j. Then
sum_i ||psi_i - mu_i|| = sum_i int |h_i - sum_j c_ij 1_{K_j}| drho < eps + eps.
Step 5. Every nu = sum_j a_j nu_j attains its norm: ||nu|| = sum_j |a_j| rho(K_j) (the nu_j live on
disjoint sets). The K_j are finitely many pairwise disjoint closed sets, so g := sign(a_j) on K_j
is continuous on the closed set union_j K_j; Tietze gives f in C(K) with ||f|| <= 1 extending g, and
nu(f) = sum_j a_j sign(a_j) rho(K_j) = ||nu||. So span{psi_i} is inside span{nu_j}, inside NA. QED
Remark 3.5b (exact quotient form). Q f := (nu_j(f)/nu_j(K))_j maps B_{C(K)} ONTO B_{l_oo^n}
(Tietze, as in Step 5), and psi_i = Q^*(w_i); every R o Q with R : l_oo^n -> F attains its norm.
This is the "averaging over disjoint compacta" form of the Johnson-Wolfe argument.

### 3.4 Tree-like M: exact hypotheses

Example 3.6 -- PROVED. "M closed in an R-tree => F(M) isometric to L_1(mu)" is FALSE without
Godard's branching-point hypothesis. Let M = {0, a, b} with d(0,a) = d(0,b) = d(a,b) = 2 (it embeds
in the tripod with legs of length 1 whose centre o is not in M; M is closed). Lip_0(M) = R^2 via
f -> (f(a), f(b)) with L(f) = max(|f(a)|, |f(b)|, |f(a) - f(b)|)/2. Its unit ball
{|x| <= 2, |y| <= 2, |x - y| <= 2} is the hexagon with vertices (2,2), (2,0), (0,-2), (-2,-2),
(-2,0), (0,2); it is not a parallelogram, so Lip_0(M) is not isometric to l_oo^2 and F(M) is not
isometric to l_1^2, the only 2-dimensional L_1(mu). QED. (Consistent with Godard Cor. 3.4, which needs
Br(T) in cl(M), and with DKP: ultrametric spaces with >= 3 points never have F(M) = l_1.)
Consequences: (a) for finite M, P is trivial anyway; (b) for an infinite wedge of copies of this
triangle, Lip_0(M) = l_oo(H) with H the hexagonal plane (Prop 3.3); its dual contains H as a
1-complemented subspace (the biadjoint of the coordinate projection), so it is not an L-space and JW
does not apply; P(l_oo(H)) = P(C(beta N, H)) follows from the C(K,E)-argument for a FIXED finite-dim E
(sums_tensors Prop 12(b), SKETCH there); for wedges of varying finite tree-like pieces: OPEN here.

Prop 3.7 -- PROVED modulo KNOWN (Godard; Kakutani). (a) If F(M) is isometric to L_1(mu) for some
measure mu (no sigma-finiteness assumed), then Lip_0(M) is isometric to C(K) for some compact
Hausdorff K; Lip_0(M)^* = M(K) is an abstract L-space (so the JW hypothesis holds); and P(Lip_0(M))
holds (Theorem 3.5). This applies whenever M is a subset of an R-tree T with Br(T) contained in the
closure of M (Godard). (b) Conversely, if Lip_0(M)^* is isometric to some L_1(nu), then M embeds
isometrically into an R-tree.
Proof. (a) Lip_0(M) = F(M)^* = L_1(mu)^*. L_1(mu) is an AL-space for every measure mu; the dual of an
AL-space is an AM-space with strong order unit (the unit is e(x) = ||x^+|| - ||x^-||) [KNOWN]; by
Kakutani's representation theorem an AM-space with unit is lattice-isometric to some C(K) [KNOWN].
(For sigma-finite mu simply L_1(mu)^* = L_oo(mu), which is a C(K).) Then Theorem 3.5. (b) F(M) is
isometric to a subspace of F(M)^** = Lip_0(M)^* = L_1(nu); apply Godard's theorem (KNOWN; it is a
statement about finite subsets: F(A) is isometrically contained in F(M) for every finite A containing
0, by McShane extension). QED
So the answer to "check sigma-finiteness": not needed (Kakutani); "precise JW statement": not needed
either, since Theorem 3.5 proves what is used. The real hypothesis to check is Godard's.
Remark 3.7c. On "Lip_0(M) is not an L_1-predual unless F(M) is an L_1-space": PROVED here are the
implications F(M) = L_1(mu) => Lip_0(M) L_1-predual (3.7(a)) and Lip_0(M) L_1-predual => M tree-like
(3.7(b)). Whether "Lip_0(M) L_1-predual => F(M) isometric to an L_1(mu)" holds in general (i.e.
whether tree-like M missing a branching point can have an L-space as F(M)^**) is NOT settled here;
in the examples of 3.6 it fails as expected (a hexagonal F(A) is 1-complemented in F(M)^**).

Prop 3.8 -- PROVED (self-contained apart from L_oo = C(K)). Let M be a closed subset of R with 0 in M,
and let G be the (countable) set of bounded components g = (a_g, b_g) of R \ M. Put
nu := lambda|_M + sum_{g in G} delta_{p_g} (p_g a fixed point of g), a sigma-finite measure. Then
Lip_0(M) is isometric to L_oo(nu). Hence P(Lip_0(M)) (L_oo(nu) is a C(K), KNOWN; Theorem 3.5).
Proof. For f in Lip_0(M) let F be its interpolation: F = f on M, F affine on each bounded gap, F
constant on each unbounded gap (equal to f at its finite end). L(F) = L(f): if x < y lie in the
closure of one gap, |F(x) - F(y)| <= (slope) |x - y| <= L(f)|x - y|; otherwise let x' be the right end
of the gap of x (x' = x if x in M) and y' the left end of the gap of y (y' = y if y in M); then
x <= x' <= y' <= y, x', y' in M and |F(x) - F(y)| <= |F(x) - F(x')| + |f(x') - f(y')| +
|F(y') - F(y)| <= L(f)((x' - x) + (y' - x') + (y - y')) = L(f)(y - x) (on unbounded gaps F is
constant). F is Lipschitz, so F(x) = int_0^x F' and ess sup |F'| = L(F). Define Phi(f) := h with
h = F' lambda-a.e. on M and h(p_g) := (f(b_g) - f(a_g))/(b_g - a_g). Then ||h||_{L_oo(nu)} =
ess sup_R |F'| (F' equals the slope on each bounded gap and 0 on unbounded gaps) = L(f). Onto: for h in
L_oo(nu) let H := h on M, H := h(p_g) on g, H := 0 on unbounded gaps, F(x) := int_0^x H and f := F|_M;
f is in Lip_0(M), F is its interpolation (H is constant on gaps), so Phi(f) = h. Phi is linear. QED
(This is the special case "subsets of R" of Godard; R has no branching points.)

### 3.5 Beyond Johnson-Wolfe: finite-codimensional weak*-closed subspaces of L_oo; metric graphs

KNOWN facts used (standard; FROM MEMORY):
(K1) Stone/Kakutani representation. For a probability space (Omega, Sigma, mu) there are a compact
     Hausdorff extremally disconnected (hence zero-dimensional) space K and an onto linear isometry
     J : L_oo(mu) -> C(K) which is multiplicative with J(1) = 1, J(1_A) = 1_{A~} with A~ clopen, and
     A -> A~ is a Boolean isomorphism from the measure algebra onto the algebra of clopen subsets
     (A~ is empty iff mu(A) = 0).
(K2) Riesz representation, Radon-Nikodym, Lebesgue decomposition, regularity of finite Radon
     measures, Hahn-Banach, Banach-Alaoglu, L_1(mu)^* = L_oo(mu).
Consequences -- PROVED from (K1),(K2):
(C1) For h in L_oo(mu), A in Sigma, c in R: h = c mu-a.e. on A iff Jh = c on A~. [(h - c)1_A = 0 iff
     (Jh - c)1_{A~} = 0, by multiplicativity and injectivity of J.]
(C2) lambda(f) := int J^{-1}(f) dmu is a Radon probability on K with lambda(A~) = mu(A); every
     nonempty clopen set has positive measure.
(C3) For g in L_1(mu), m_g(f) := int J^{-1}(f) g dmu is a Radon measure with ||m_g|| = ||g||_1,
     m_g << lambda, m_g(A~) = int_A g dmu; and every Radon measure << lambda equals m_g for a unique
     g in L_1(mu). [||m_g|| = sup{int h g dmu : ||h||_oo <= 1} = ||g||_1. For bounded g >= 0,
     0 <= m_g <= ||g||_oo lambda, so m_g << lambda; general g by L_1-approximation, the
     lambda-continuous measures forming a norm-closed set. Onto: g -> m_g is an isometry into
     L_1(lambda) (identified with the lambda-continuous measures), so its range is closed; the range
     contains m_{1_A} = 1_{A~} lambda for all A; and indicators of clopen sets are dense in
     L_1(lambda): for Borel B and delta > 0 choose compact C in B in open U with lambda(U \ C) <
     delta and, K being zero-dimensional, a clopen D with C in D in U; then lambda(B Delta D) < delta.]

Theorem 3.9 -- PROVED (modulo K1, K2). Let mu be sigma-finite, g_1..g_b in L_1(mu) (b >= 0) and
X := {h in L_oo(mu) : int h g_l dmu = 0, l = 1..b} (weak*-closed, codimension <= b). Then X has (LL);
hence P(X) and AA(X,F) is dense for every finite-dimensional F.
Proof. Step 0 (normalization). Take w_0 in L_1(mu), w_0 > 0 a.e., int w_0 = 1; mu' := w_0 mu has the
same null sets, L_oo(mu') = L_oo(mu), and int h g_l dmu = int h (g_l/w_0) dmu'. So let mu be a
probability. Discarding dependent g_l does not change X: let g_1..g_b be independent. Fix K, J, lambda
as in (K1),(C2); identify L_oo(mu)^* with M(K) by Phi(h) = int Jh dPhi. X^perp = span{m_{g_l}}
(annihilator of the pre-annihilator of a finite-dimensional, hence weak*-closed, subspace), so by
Hahn-Banach, for Psi in M(K): ||Psi|_X||_{X^*} = dist(Psi, X^perp) = min_t ||Psi - sum_l t_l m_{g_l}||.
Step 1 (data). Let phi_1..phi_d in X^*, eps > 0; Hahn-Banach extensions Phi_i in M(K). Lebesgue
decomposition with respect to lambda and (C3): Phi_i = m_{a_i} + sigma_i, a_i in L_1(mu), sigma_i
singular to lambda.
Step 2 (singular parts). rho := sum_i |sigma_i| is singular to lambda: there is a Borel N with
lambda(N) = 0 and rho(K \ N) = 0. Radon-Nikodym: sigma_i = h_i rho, |h_i| <= 1. As in Thm 3.5,
Steps 2-4 (intersect the partition sets with N before taking compacts): pairwise disjoint compact
K_1..K_m inside N and reals d_ik with sum_i ||sigma_i - sum_k d_ik nu_k|| < eps, nu_k := rho|_{K_k}
(positive; discard nu_k = 0). Then lambda(K_k) = 0 and nu_k is singular to lambda.
Step 3 (weight, clopen neighbourhoods). w := 1 + sum_i |a_i| + sum_l |g_l| in L_1(mu), w >= 1. As
m_w << lambda, m_w(K_k) = 0. K is zero-dimensional and the K_k are disjoint compact sets, so there are
pairwise disjoint clopen O_k containing K_k. For each k choose clopen O_k = D_k^(0) ⊇ D_k^(1) ⊇ ...
⊇ K_k with m_w(D_k^(n)) <= 8^{-n}: outer regularity of the positive Radon measure m_w gives an open
U ⊇ K_k with m_w(U) <= 8^{-n}, and compactness plus zero-dimensionality a clopen D with
K_k ⊆ D ⊆ U ∩ D_k^(n-1). Let E_k^(n) in Sigma with (E_k^(n))~ = D_k^(n) (K1). Then
int_{E_k^(n)} w dmu = m_w(D_k^(n)) <= 8^{-n} (C3); after changes on null sets the E_k^(n) decrease in
n and are disjoint for different k (Boolean isomorphism).
Step 4 (cushions). For theta > 0 let chi_k := theta sum_{n>=1} 2^n w 1_{E_k^(n)}. Then chi_k >= 0,
||chi_k||_1 <= theta sum_n 2^n 8^{-n} = theta/3, chi_k = 0 off E_k^(1), and chi_k >= theta 2^n w on
E_k^(n) (all E_k^(j), j <= n, contain E_k^(n)).
Step 5 (approximants). Psi_i := m_{a_i + sum_k d_ik chi_k} + sum_k d_ik nu_k and psi_i := Psi_i|_X.
Then ||psi_i - phi_i||_{X^*} <= ||Psi_i - Phi_i|| <= sum_k |d_ik| theta/3 + ||sigma_i - sum_k d_ik
nu_k||, so sum_i ||psi_i - phi_i|| < 2 eps for theta small enough.
Step 6 (every combination attains). Fix eta in R^d \ {0}, psi_eta := sum_i eta_i psi_i,
a_eta := sum_i eta_i a_i, c_k := sum_i eta_i d_ik, u := a_eta + sum_k c_k chi_k in L_1(mu). Then
sum_i eta_i Psi_i = m_u + sum_k c_k nu_k.
(6a) Norm. For t in R^b, m_{u - sum t_l g_l} << lambda while sum_k c_k nu_k is singular to lambda and
the nu_k live on disjoint sets, so ||m_u + sum c_k nu_k - sum t_l m_{g_l}|| = ||u - sum t_l g_l||_1 +
sum_k |c_k| ||nu_k||. The function t -> ||u - sum t_l g_l||_1 is continuous, convex and coercive
(>= c|t| - ||u||_1 by independence), so it has a minimizer t*; put r := u - sum_l t*_l g_l. Then
||psi_eta|| = ||r||_1 + sum_k |c_k| ||nu_k||.
(6b) A norming element. G := span{g_l} in L_1(mu). Hahn-Banach (L_1^* = L_oo): dist(u,G) =
sup{int u h dmu : ||h||_oo <= 1, int h g_l = 0 for all l}; the sup is attained at some h_0 (weak*-
compact set, weak*-continuous objective). So h_0 is in B_X and int r h_0 = int u h_0 = dist(u,G) =
||r||_1; since |h_0| <= 1 this forces h_0 = sign(r) mu-a.e. on {r != 0}.
(6c) Cushion domination. Let c_k != 0. On E_k^(n) (n >= 1), mu-a.e.: the other cushions vanish, so
r = a_eta + c_k chi_k - sum_l t*_l g_l with |a_eta| <= |eta|_oo w, |sum t*_l g_l| <= |t*|_oo w and
|c_k chi_k| >= |c_k| theta 2^n w. Choose n_k with |c_k| theta 2^{n_k} > |eta|_oo + |t*|_oo; then
r != 0 and sign r = sign c_k a.e. on E_k^(n_k) (w >= 1). By (6b) h_0 = sign c_k a.e. on E_k^(n_k),
so by (C1) Jh_0 = sign c_k on D_k^(n_k), which contains K_k; hence int Jh_0 dnu_k = |c_k|/c_k ||nu_k||.
(6d) psi_eta(h_0) = int u h_0 dmu + sum_k c_k int Jh_0 dnu_k = ||r||_1 + sum_k |c_k| ||nu_k|| =
||psi_eta||. So psi_eta is in NA(X,R). Thus span{psi_i} lies in NA(X,R): (LL). QED

Remark 3.9a -- PROVED. (i) b = 0 gives (LL) for every L_oo(mu) (second proof of the C(K)-case for
hyperstonean K). (ii) Why the C(K)-proof (free zones + Tietze) is not enough when b >= 1: in
X = {h in L_oo[0,1] : int h = 0} take A = [0,3/5] and nu a positive norm-one functional singular to
Lebesgue measure and concentrated in (3/5,1]~. Then psi := (lambda|_A/lambda(A) + nu)|_X has norm
min_t (lambda(A)|1/lambda(A) - t| + lambda(A^c)|t|) + 1 = 2/3 + 1, attained by the median t = 5/3;
for h in B_X, int_A h = -int_{A^c} h <= 2/5, so the first part is <= 2/3 with equality only if h = -1
a.e. on A^c, which forces nu(h) = -1 (C1); hence psi does NOT attain its norm. The median of the
normal density decides the forced signs; the cushions make those signs agree with the singular signs.
(iii) What is used about the g_l: finite dimension of span{g_l} (proximinality in L_1 and the bound
|sum t_l g_l| <= |t|_oo w). Infinitely many constraints (Lip_0(R^n), graphs with infinitely many
cycles) are NOT covered. (iv) X is a weak*-closed (hence proximinal) finite-codimensional subspace of
L_oo; KLMW (confirmed) treat finite-codimensional proximinal subspaces of c_0 and K(l_2). We found no
reference for the L_oo statement; novelty not certified.

Cor 3.10 -- PROVED (from Thm 3.9). Let G be a connected metric graph: countable edge set E, each edge
e oriented and identified with [0, l_e], l_e > 0, glued at vertices; d = path-length metric (assumed
to be a metric, e.g. G locally finite); base point a vertex. Assume the cycle space is finite-
dimensional, and let Z_1..Z_b be the fundamental cycles of a spanning tree (a Z-basis of the integral
cycle space). With lambda_E = Lebesgue measure on the disjoint union of the edges (sigma-finite) and
g_c := +1 / -1 on the edges that Z_c traverses along / against their orientation, 0 elsewhere,
  Lip_0(G) is isometric to X_G := {h in L_oo(lambda_E) : int h g_c = 0, c = 1..b}.
Hence P(Lip_0(G)) and (LL). Examples: circle, theta graph, every finite connected graph, R or [0,oo)
with finitely many loops attached, trees (b = 0) -- the last ones are also in Prop 3.7.
Proof. For f in Lip_0(G) and an edge e, s -> f(e(s)) is L(f)-Lipschitz (d(e(s),e(s')) <= |s - s'|);
let h_e be its a.e. derivative, |h_e| <= L(f); Phi(f) := (h_e)_e. For every edge path gamma from x to
y, f(y) - f(x) = int_gamma h (signed sum of integrals over traversed pieces; absolute continuity), so
int h g_c = (integral of h around Z_c) = 0, Phi(f) is in X_G and ||Phi(f)|| <= L(f). Conversely let h
in X_G. The chain of every closed edge path is an integer combination of the Z_c, so int_gamma h = 0
for every closed path; hence f(x) := int_gamma h (gamma any edge path from 0 to x) is well defined,
f(0) = 0, and for every path gamma from x to y, |f(y) - f(x)| = |int_gamma h| <= ||h||_oo
length(gamma); taking the infimum over gamma, L(f) <= ||h||_oo. Differentiating along edges,
Phi(f) = h. So Phi is an onto linear isometry. Theorem 3.9 applies. QED

Prop 3.11 -- PROVED (modulo the four-point characterization of R-tree subsets and Godard). If the
metric graph G of Cor 3.10 contains a cycle, then Lip_0(G)^* is not isometric to any L_1(nu) (so JW
does not apply to Lip_0(G)), and Lip_0(G) is not isometric to any C(K).
Proof. Simple cycles correspond to nonzero elements of the finite Z_2-cycle space, so there are finitely
many; let Z be one of minimal length L_0. Claim: d = d_Z on Z (d_Z = shorter-arc distance). Let x, y in
Z (subdivide edges so that they are vertices), alpha, beta the two arcs of Z from x to y, length(alpha)
= d_Z(x,y) <= length(beta), and gamma any path from x to y. Let c := [gamma] + [beta] in the Z_2-cycle
space. If c != 0, its support contains a simple cycle (even subgraphs decompose into edge-disjoint
cycles), so L_0 <= length(gamma) + length(beta), i.e. length(gamma) >= length(alpha). If c = 0, gamma
traverses every edge of beta an odd number of times, so length(gamma) >= length(beta) >= length(alpha).
Hence d(x,y) = d_Z(x,y). Four points of Z at consecutive arc distance L_0/4 have pair sums L_0/2,
L_0/2 and L_0; the largest is attained once, so the four-point condition fails and G does not embed
isometrically into an R-tree. Prop 3.7(b) gives the first claim; if Lip_0(G) = C(K) isometrically,
then Lip_0(G)^* = M(K) would be an L_1(nu) (Kakutani), a contradiction. QED

### 3.6 Lip_0(R^n), Euclidean

Prop 3.12. (a) KNOWN/PROVED: f -> grad f is an onto linear isometry from Lip_0(R^n, |.|_2) onto
  G_n := {G in L_oo(R^n; l_2^n) : d_i G_j = d_j G_i in D'(R^n)}, ||G|| = ess sup |G(x)|_2,
weak*-weak* continuous; G_n is the annihilator of the divergence-free fields in L_1(R^n; l_2^n), i.e.
the dual of F(R^n) = L_1/{div v = 0} (CKK 2017, confirmed). Isometry: |grad f| <= L(f) at points of
differentiability (Rademacher); conversely for x, y and a.e. small translate of the segment [x,y] the
segment meets the non-differentiability set in a null set (Fubini), so |f(y') - f(x')| <= ||grad f||_oo
|y' - x'| for a dense set of pairs, hence everywhere by continuity. Onto: a curl-free L_oo field is a
distributional gradient of a W^{1,oo}_loc function (Poincare lemma for distributions, KNOWN), which is
Lipschitz with constant ||G||_oo by the previous sentence.
(b) PROVED: L_oo(R) is isometric to a 1-complemented subspace: Pf(x) := f(x_1 e_1) is a norm-one
projection onto {f : f(x) = phi(x_1)} = isometric copy of Lip_0(R) = L_oo(R) (Prop 3.8).
(c) Which tools apply (n >= 2)? Reflexivity: no. RNP: no (contains L_oo). Johnson-Wolfe: no -- the
four vertices of a unit square have pair sums 2, 2, 2 sqrt 2, so the four-point condition fails, R^n is
not tree-like and Lip_0(R^n)^* is not an L-space (Prop 3.7(b)); isomorphically F(R^2) is not even a
subspace of L_1 (Naor-Schechtman). Uhl: no (domain not L_1). Theorem 3.9: no (the curl-free constraint
is infinite-dimensional and local, and the norm is vector valued). Wedge decompositions: no (cross
distances in R^n are not additive). (DL)/(LL): unknown. STATUS: P(Lip_0(R^n)), n >= 2: OPEN. The same
holds for polyhedral norms on R^n (e.g. Lip_0(l_1^n) = curl-free part of L_oo(R^n; l_oo^n), a
weak*-closed subspace of a scalar L_oo of infinite codimension): OPEN.
(d) HEURISTIC contrast with the circle: Lip_0(S^1) = {h in L_oo : int h = 0} has ONE cycle constraint
and Theorem 3.9 applies; Lip_0(R^2) has one constraint per loop (all of them local), and the cushion
proof breaks at step (6b) (no proximinality in L_1 of the infinite-dimensional space of divergence-free
fields: the Beckmann problem min{||v||_1 : div v = div v_0} need not have an L_1 minimizer) and at
step (6c) (the dominating bound |sum t_l g_l| <= |t| w has no analogue).

## 4. Lineability (task item (c))

Prop 4.1 -- PROVED. F(M) is a closed linear subspace of Lip_0(M)^* contained in NA(Lip_0(M),R)
(Prop 3.1(a) with d = 1); it is dense iff F(M) is reflexive iff M is finite (Prop 3.1(d)).

Lemma 4.2 -- PROVED (structure of 2-dim subspaces of NA(C(K))). Let mu, nu in M(K) with s mu + t nu in
NA(C(K),R) for all (s,t). Put rho := |mu| + |nu|, S := supp rho. Then there are continuous a, b : S -> R
with |a| + |b| = 1 on S, mu = a rho and nu = b rho, and for every (s,t) != 0 the closed sets
cl{y in S : s a + t b > 0} and cl{y in S : s a + t b < 0} are disjoint.
Proof. Radon-Nikodym: mu = a_0 rho, nu = b_0 rho, |a_0| + |b_0| = 1 rho-a.e. (as |mu| + |nu| = rho);
write D := {p in R^2 : |p|_1 = 1}. For x in S let R(x) be the set of p in R^2 such that
rho(U ∩ {|(a_0,b_0) - p| < delta}) > 0 for every open U containing x and every delta > 0.
R(x) is closed, contained in D, and nonempty: otherwise finitely many (U_i, delta_i) cover D, and
U := ∩ U_i has rho(U) = 0, contradicting x in supp rho.
(A) R(x) is a singleton. If p != p' are in R(x), there is (s,t) with s p_1 + t p_2 > 0 > s p'_1 +
t p'_2 (two distinct points of D are never positive multiples of each other: if they are linearly
independent solve a 2x2 system, if p' = -c p with c > 0 take (s,t) = p). For m := s mu + t nu =
(s a_0 + t b_0) rho, every neighbourhood U of x meets {|(a_0,b_0) - p| < delta} (delta small, so that
s a_0 + t b_0 > 0 there) in positive rho-measure, so x in supp m^+; likewise x in supp m^-;
contradicting Lemma 3.5a. Let r(x) be the element of R(x).
(B) r is continuous on S: given x and an open W containing r(x), every p in D \ W has (U_p, delta_p)
with rho(U_p ∩ {|(a_0,b_0) - p| < delta_p}) = 0; finitely many balls cover the compact D \ W; on
U := ∩ U_{p_i}, (a_0,b_0) lies in W rho-a.e., so R(y) is in cl W for all y in U ∩ S.
(C) (a_0,b_0) = r rho-a.e.: for each ball B of a countable base let E_B := {(a_0,b_0) in B} and O_B the
union of all open U with rho(U ∩ E_B) = 0; inner regularity gives rho(O_B ∩ E_B) = 0. Off the null set
union_B (O_B ∩ E_B) union (K \ S) union {(a_0,b_0) not in D}, the value (a_0,b_0)(y) lies in R(y).
(D) For m = s mu + t nu = (s a + t b) rho, supp m^+ = cl P with P := {y in S : s a + t b > 0}: "inside"
since m^+ is concentrated on P; "contains" since every nonempty relatively open subset of S = supp rho
has positive measure. Likewise supp m^- = cl N. Lemma 3.5a gives cl P ∩ cl N = empty. QED

Cor 4.3 -- PROVED. In the situation of Lemma 4.2: (i) if |mu| and |nu| are mutually singular then
supp mu ∩ supp nu = empty. (ii) If C is a connected relatively open subset of S, then r is constant on
C. (iii) If K is connected and supp(|mu| + |nu|) = K, then mu and nu are proportional.
Proof. (i) a b = 0 rho-a.e., hence everywhere on S by continuity (a nonempty open set where both are
nonzero would have positive measure); {a != 0} and {b != 0} are disjoint, open in S and cover S
(|a| + |b| = 1), hence clopen; supp mu = {a != 0}, supp nu = {b != 0}. (ii) If r(C) contains p != p',
r(C) (connected, in the circle D) contains an arc A from p to a point p'' != p of angular length
< pi. For each q in the open arc (uncountably many, pairwise non-antipodal) pick (s,t) != 0 vanishing
at q, positive at p, negative at p''. P_q, N_q (as in Lemma 4.2, intersected with C) are nonempty,
relatively open, with disjoint closures; C connected forces W_q := C \ (cl P_q ∪ cl N_q) != empty; W_q
is open in S and r takes values in {q,-q} on it. The W_q are pairwise disjoint nonempty open subsets of
supp rho, uncountably many sets of positive measure: impossible. (iii) is (ii) with C = K. QED

Prop 4.4 -- PROVED modulo KNOWN. If K is scattered then NA(C(K),R) contains a dense linear subspace:
every regular measure on a scattered compactum is purely atomic (Rudin / Pelczynski-Semadeni, KNOWN,
FROM MEMORY), so finitely supported measures are dense in M(K) = l_1(K), and each of them attains its
norm (Urysohn on finitely many points).

Prop 4.5 -- PROVED (an obstruction in L_oo). Let mu be any measure with L_1(mu)^* = L_oo(mu), g in
L_1(mu) with g != 0 a.e., and sigma != 0 a functional on L_oo(mu) singular to L_1(mu) (so
||g.mu + s sigma|| = ||g||_1 + |s| ||sigma|| for s in R, by the L-decomposition of L_oo^* (Yosida-
Hewitt / Lebesgue decomposition in the C(K)-model, KNOWN)). Then span{g.mu, sigma} is NOT contained in
NA(L_oo(mu),R). Proof. If g.mu + s sigma attains at h, ||h|| <= 1, then int g h = ||g||_1 forces
h = sign g (uniquely, as g != 0 a.e.) and s sigma(sign g) = |s| ||sigma||. Taking s = 1 and s = -1
gives sigma(sign g) = ||sigma|| = -sigma(sign g), so sigma = 0. QED
So a dense linear subspace of NA(L_oo) cannot contain e.g. the Lebesgue integral together with any
singular functional; elements near normal functionals must have densities vanishing somewhere near the
supports of the singular elements, and the cushions of Theorem 3.9 point the other way (they are
private to a finite family).

4.6 Status of (DL). PROVED: (DL) for C(K), K scattered (Prop 4.4). KNOWN OPEN: (DL) for C_0(L) in
general (KLMW, confirmed). For infinite M in the Godard class, Lip_0(M) = C(K) contains a complemented
l_oo (dual of the complemented l_1 in F(M), CDW), so K is not scattered (C(K) with K scattered is
Asplund) and (DL) for Lip_0(M) is an instance of the open KLMW question; the same for L_oo[0,1] and
l_oo = C(beta N). Lemma 4.2, Cor 4.3, Prop 4.5 are obstructions to naive constructions, not a
disproof. We found neither a dense linear subspace nor a proof that none exists (OPEN here).

4.7 How Johnson-Wolfe gets density without (DL), and adaptation to Lip_0(M).
(a) PROVED: what JW-type arguments use is (LL) (Thm 3.5): for each FINITE family, positive measures on
disjoint compacta (Riesz, regularity) and one Tietze function realizing all sign patterns. The
attaining subspaces span{nu_j} depend on the family; by Lemma 4.2/Cor 4.3 they cannot in general be
merged (e.g. two families producing mutually singular but not support-disjoint measures).
(b) PROVED: the argument adapts when Lip_0(M) is a C(K) (Prop 3.7) and, with cushions, when Lip_0(M)
is a weak*-closed finite-codimensional subspace of an L_oo (Thm 3.9, Cor 3.10), and passes to finite
wedges (Cor 3.4(ii)).
(c) HEURISTIC (why not in general). The de Leeuw map Df(x,y) = (f(x) - f(y))/d(x,y) identifies
Lip_0(M) isometrically and weak*-continuously with Gamma^perp in l_oo(M~), where Gamma in l_1(M~) is the
closed span of e_(x,y) + e_(y,x) and d(x,y) e_(x,y) + d(y,z) e_(y,z) - d(x,z) e_(x,z) (a bounded u
satisfying these relations is Df for f(x) := d(x,0) u(x,0), with L(f) = ||u||_oo); l_1(M~)/Gamma =
F(M). Gamma is infinite-dimensional as soon as |M| >= 3 and M is infinite. The Tietze step would need
ONE 1-Lipschitz f whose slope extension to beta M~ equals prescribed signs on prescribed disjoint
compacta -- a Lipschitz extension problem with prescribed asymptotic slopes that has no general
solution. The cushion step needs (i) proximinality of Gamma in l_1(M~), i.e. optimal molecular
representations of elements of F(M); this FAILS already for M = [0,1] (PROVED: in F([0,1]) = L_1[0,1],
an optimal representation of g as sum a_k (normalized interval indicators) with sum |a_k| = ||g||_1
forces |g| = sum |a_k| 1_{I_k}/|I_k| a.e., so each I_k is a.e. inside {g != 0}; for g = 1_C, C a fat
Cantor set, no interval is a.e. inside C); and (ii) freedom to take h_0 = sign(r), which fails since
sign functions are not cocycles. So new ideas are needed beyond finitely many cycle constraints.

## 5. Transfer (task item (d))

Prop 5.1 -- PROVED modulo the existence of invariant means on abelian groups (KNOWN). For every real
Banach space X there is a norm-one linear projection P from Lip_0(X) onto X^* (embedded as the linear
functionals). (Lindenstrauss 1964, FROM MEMORY; for separable X the adjoint of the Godefroy-Kalton
linear isometric lifting X -> F(X) is a weak*-continuous such projection, KNOWN, confirmed.)
Proof. Let m be a translation-invariant mean on l_oo(X) (X as an additive group): m positive, linear,
m(1) = 1, m(phi(. + a)) = m(phi). For f in Lip_0(X), x in X, phi_x(y) := f(x + y) - f(y) is bounded by
L(f)||x||. Put Pf(x) := m(phi_x). Since phi_{x+x'}(y) = phi_x(y + x') + phi_{x'}(y), invariance gives
Pf(x + x') = Pf(x) + Pf(x'); and |Pf(x)| <= L(f)||x||. An additive function bounded by a multiple of the
norm is Q-linear and continuous, hence R-linear: Pf in X^*, ||Pf|| <= L(f). If f is linear, phi_x is the
constant f(x), so Pf = f. P is linear in f. QED

Example 5.2 -- PROVED. The summand-inheritance mechanism ((AD) of sums_tensors Thm 2) does not apply to
X^* inside Lip_0(X), already for X = R. Lip_0(R) = L_oo(R) (f -> f'), X^* = constants. Any norm-one
projection onto the constants is Q(h) = phi(h) 1 with phi a state (norm one, phi(1) = 1, hence
positive). (AD) for R1 (+) ker(phi) would give ||w + 1||_oo = ||w - 1||_oo for all w in ker(phi)
(take u = -x_1 with x_1 = 1 and x_1 = -1). Pick a measurable A with A and A^c non-null and
alpha := phi(1_A) != 1/2 (exists: if phi(1_A) = 1/2 whenever A, A^c are non-null, split such an A into
non-null A_1, A_2 with non-null complements; then 1/2 = phi(1_A) = phi(1_{A_1}) + phi(1_{A_2}) = 1).
w := 1_A - alpha 1 is in ker(phi), ||w + 1|| = 2 - alpha (attained on A; on A^c |1 - alpha| <= 2 -
alpha), ||w - 1|| = 1 + alpha (attained on A^c); these differ. QED
Status of "P(Lip_0(X)) => P(X^*)": OPEN. It would follow if P passed to 1-complemented subspaces, which
is not known (OPEN here; see Prop 5.4 for the closely related subspace/quotient versions). At present no
X with dim X >= 2 is known to satisfy P(Lip_0(X)) (Lip_0(R^n) is open), so the implication cannot even
be tested.

Prop 5.3 -- PROVED modulo Phillips' lemma (c_0 is not complemented in l_oo; KNOWN). c_0 is not
isomorphic to a complemented subspace of any dual space. In particular no renorming of c_0 (Read's
space, Martin's space, the p_N of Preprint B) is complemented in any dual space, e.g. in any Lip_0(M).
Proof. Suppose T : c_0 -> E is an isomorphism onto E in Z^* and P : Z^* -> E is a bounded projection.
For z in Z, a -> <Ta, z> is in c_0^* = l_1, so sum_n |<T e_n, z>| <= ||T|| ||z||. Define J : l_oo -> Z^*
by <J a, z> := sum_n a_n <T e_n, z>; |<Ja,z>| <= ||a||_oo ||T|| ||z||, so J is bounded, and J = T on c_0
(the series sum a_n T e_n converges in norm for a in c_0). Then T^{-1} P J : l_oo -> c_0 is bounded and
equals the identity on c_0: a bounded projection of l_oo onto c_0, contradicting Phillips. QED

Prop 5.4 -- PROVED. Fix nothing; quantify over all finite-dimensional Y.
(a) "P passes to closed subspaces" is equivalent to a positive answer to JW.
(b) "P passes to exact quotients (Q : W -> Z with Q(B_W) = B_Z)" is equivalent to a positive answer.
Proof. "<=" in both: a positive answer gives P for every space. (a) "=>": every Z is isometric to a
subspace of l_oo(Gamma) = C(beta Gamma) (Gamma = B_{Z^*}), which has P by Thm 3.5. (b) "=>": every Z is
an exact quotient of l_1(B_Z) via e_z -> z (the image of the unit ball is the absolutely convex hull of
B_Z, i.e. B_Z), and l_1(Gamma) has property A (Lindenstrauss 1963; also sums_tensors Thm 1), hence P.
So P(Z) for all Z, i.e. every finite-dimensional Y has property B. QED
(The sums_tensors (AD)-inheritance is the special 1-complemented case that IS available.)

5.5 Universality of dual spaces -- OPEN. (i) Trivially a positive JW answer gives P for all duals.
(ii) All known transfer mechanisms (sums_tensors Thm 4: X -> X (+)_a X, l_p(X), L_1(mu,X), tensor
products) produce non-dual spaces from a non-dual X, and by Prop 5.3 no dual space contains a
c_0-renorming complementably; so the Martin-type candidates cannot be moved into the class of duals
by summand arguments. (iii) Whether P(Z^**) implies P(Z) (which would make duals universal) or
P(Z) implies P(Z^**) is unknown; for Z = c_0 both hold. For the finite-block truncations
Z = (c_0, p_J) of Martin's norm, Z^** = (l_oo, p_J^**) is a strictly convex dual renorming of l_oo
(Preprint B, Thm finite-blocks(b)), and P(Z^**) is as open as P(Z). (iv) X^* is 1-complemented in Lip_0(X) (Prop 5.1), so the class
{Lip_0(M)} would be universal for duals if P passed to 1-complemented subspaces (OPEN).
Verdict for (d): PROVED: Prop 5.1, Example 5.2, Prop 5.3, Prop 5.4. OPEN: P(Lip_0(X)) => P(X^*);
universality of dual spaces; inheritance of P by 1-complemented subspaces. KNOWN: Lindenstrauss 1964,
Godefroy-Kalton 2003 complementation.

## 6. Overall answer (task item (e)) and notions that fail

6.1 Status table for P(Lip_0(M)) (Y finite-dimensional, all of them):
- M finite: trivial (finite dimension).                                         KNOWN/PROVED
- F(M) isometric to an L_1(mu) (Godard: M in an R-tree T, Br(T) in cl M), incl.
  every subset of R, every R-tree, F(M) = l_1(Gamma) (DKP): Lip_0(M) = C(K).     PROVED (Prop 3.7/3.8)
- connected metric graphs with finite first Betti number (circle, theta, finite
  graphs, R with finitely many loops): JW does NOT apply.                         PROVED (Cor 3.10)
- finite wedges of the above (finite l_oo-sums of (LL)-spaces).                  PROVED (Cor 3.4(ii))
- tree-like M without branching points: finite -- trivial; infinite wedge of one
  fixed finite piece -- via C(beta N, E) (sums_tensors Prop 12(b), SKETCH there);
  varying pieces -- OPEN.
- R^n (n >= 2, Euclidean or polyhedral norm), the 2-torus, the planar grid graph,
  graphs with infinitely many cycles (Hawaiian earring), non-tree countable
  compacta in R^2, infinite wedges of arbitrary pieces.                           OPEN
- arbitrary M.                                                                    OPEN
Equivalence with JW: only "JW positive => P(Lip_0(M)) for all M" is known (trivial). No reduction of
JW to the class {Lip_0(M)} is known: the class contains every X^* as a 1-complemented subspace
(Prop 5.1) but P is not known to pass to 1-complemented subspaces, and passing to subspaces or exact
quotients is itself equivalent to JW (Prop 5.4). A counterexample in this class would refute JW;
none is expected.
VERDICT: OPEN (positive for the classes above; undecided for Lip_0(R^2)).

6.2 Notions that DO fail -- DIFFERENT from NA operators FROM Lip_0(M):
(N1) Strongly norm-attaining Lipschitz functionals SNA(M,R) (f in Lip_0(M) with |f(x) - f(y)| =
     L(f) d(x,y) for some x != y, i.e. f attains its norm as a functional on F(M) AT A MOLECULE): not
     dense for M = [0,1] and for every geodesic M (Kadets-Martin-Soloviova 2016; confirmed). These are
     elements of Lip_0(M), viewed on the domain F(M), not operators on Lip_0(M).
(N2) NA(F(M),R) (functionals on F(M) attaining somewhere on B_{F(M)}) is dense by Bishop-Phelps; the
     operator question NA(F(M),Y) is the free-space-DOMAIN problem, another class.
(N3) Infinite-dimensional ranges: C(K) fails property A for infinite compact metric K (Lindenstrauss,
     quoted in arXiv 2110.02066, confirmed snippet), C[0,1] fails A (Schachermayer); so for
     Lip_0([0,1]) = L_oo[0,1] = C(K) density can fail for some infinite-dimensional ranges (FROM MEMORY
     for the L_oo case), while P holds (Thm 3.5). P is strictly weaker than property A.
(N4) For the domain Lip_0(M) with finite-dimensional ranges no failing notion is known to us;
     weak*-continuous ("molecular") operators always attain (Prop 3.1).

## 7. Open questions isolated here
Q1 P(Lip_0(R^2))? Also (LL) for Lip_0(R^2). (Simplest case beyond Thm 3.9: infinitely many local
   cycle constraints.)
Q2 P(Lip_0(G)) for metric graphs with infinitely many independent cycles (Z^2 grid with unit edges;
   Hawaiian earring).
Q3 (DL) for C(K), K not scattered (KLMW); in particular L_oo[0,1], l_oo, and so Lip_0(M) for every
   infinite M in the Godard class.
Q4 Does P pass to 1-complemented subspaces? (Would give P(Lip_0(X)) => P(X^*).)
Q5 Does P(Z^**) imply P(Z)? (Would make dual spaces universal for JW.)
Q6 P(l_oo(E_n)) for arbitrary finite-dimensional E_n (infinite wedges of finite metric spaces).
Q7 P(X_1) and P(X_2) => P(X_1 (+)_oo X_2)? (Converse of Cor 3.4(i); sums_tensors question C_oo.)

## 8. Sources (search hits; full texts not read)
- Johnson-Wolfe 1979: https://eudml.org/doc/218261 ; https://impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/65/1/102407/norm-attaining-operators
- Schachermayer 1983 (C(K) results): https://msp.org/pjm/1983/105-2/pjm-v105-n2-p13-s.pdf ; https://projecteuclid.org/download/pdfview_1/euclid.pjm/1102723338
- JW C(K)-domain statement via survey: https://www.ugr.es/local/mmartins/Curriculum/Papers/pre2014_Martin-norm-attaining_survey.pdf
- Lindenstrauss 1963 (biadjoints, A/B): https://arxiv.org/pdf/1306.1155 ; https://www.ugr.es/local/mmartins/material/2016-Korea-ILJU-school-NOTES.pdf
- KLMW: https://arxiv.org/pdf/1905.08272 ; https://ar5iv.arxiv.org/html/1905.08272
- Rmoutil: https://arxiv.org/pdf/1503.06112
- Kim-Lee (C(K), uniformly convex): https://arxiv.org/pdf/1407.7872 ; Kim-Lee-Lin (L_oo): https://digitalcommons.memphis.edu/facpubs/5836
- Godard: https://arxiv.org/pdf/0904.3178 ; https://www.ams.org/proc/2010-138-12/S0002-9939-2010-10421-5/
- Dalet-Kaufmann-Prochazka: https://arxiv.org/pdf/1502.02719 ; Aliaga-Petitjean-Prochazka: https://arxiv.org/pdf/1909.05285
- Godefroy-Kalton: https://geodesic.mathdoc.fr/articles/10.4064/sm159-1-6
- Cuth-Kalenda-Kaplicky: https://arxiv.org/pdf/1610.03966
- Cuth-Doucha-Wojtaszczyk: https://arxiv.org/pdf/1505.07209 ; Kalton 2004: https://www.raco.cat/index.php/CollectaneaMathematica/article/view/56573
- Aliaga-Medina (nets, Lip_0(R) = L_oo, Lip_0(Z) = l_oo): https://arxiv.org/html/2601.03131v1
- Naor-Schechtman: https://arxiv.org/pdf/cs/0509074
- Kadets-Martin-Soloviova: https://arxiv.org/pdf/1601.07821 ; SNA (Chiclana et al.): https://www.ugr.es/local/mmartins/Curriculum/Papers/pre2019_SNA_2.pdf
- C(K) fails A for infinite metric K (quoted): https://arxiv.org/pdf/2110.02066
- Uhl/Martin compact version: https://ar5iv.arxiv.org/html/1502.07084
