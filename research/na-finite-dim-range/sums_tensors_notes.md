# sums_tensors -- density of NA(X,Y), Y finite-dimensional, X a direct sum or a tensor product

Key: sums_tensors. Real scalars throughout. Written 2026-10-30 by a workflow subagent.
Labels: PROVED (complete proof written here), KNOWN (reference given; "confirmed" = a web-search hit,
URL in Section 10; "FROM MEMORY" = not confirmed by search), SKETCH, HEURISTIC, OPEN, FALSE.

## 0. Summary

Verdict: EQUIVALENT_TO_JOHNSON_WOLFE.
For each class C below and each finite-dimensional Y:
    [NA(W,Y) dense in L(W,Y) for every W in C]   <=>   [Y has Lindenstrauss property B].
Classes: {X (+)_a Z} for a fixed absolute norm a (even {X (+)_a X}); {E(X)} for a fixed Banach sequence
lattice E (l_p(X), 1<=p<=oo, c_0(X), ...); {X (x)_pi l_1^n} (n>=1 fixed), {X (x)_pi l_1},
{X (x)_pi L_1(mu)} for any fixed sigma-finite mu != 0 (atomless mu included); {X (x)_eps l_oo^n},
{X (x)_eps c_0}, {C(K) (x)_eps X} with K fixed having an isolated point.
So "NA always dense for these classes and all finite-dimensional Y" is exactly the (open) Johnson-Wolfe
question. A counterexample inside such a class exists iff a counterexample exists among the building
blocks; sums and tensor products cannot create counterexamples. (Theorem 4.)

Main results of these notes:
- T1 (PROVED) l_1-sums, both directions, any Y, any index set.
- T2 (PROVED) summand inheritance for EVERY absolute sum and every Banach-lattice sum, any Y
  (abstract condition (AD)); the suggested route of the task works verbatim.
- T3 (PROVED, modulo the von Neumann-Maharam lifting theorem) NA(L_1(mu,X),Y) dense => NA(X,Y) dense,
  Y finite-dimensional, mu any nonzero sigma-finite measure (atomless allowed).
- P11 (PROVED, modulo L_1(mu,X)^* = L_oo(mu,X^*) for X^* RNP) converse of T3 when X^* has RNP.
- P5 (PROVED) for Y finite-dimensional, c_0-sums and l_p-sums (1<p<oo) reduce to finite subsums.
- P6 (PROVED) converse for a finite absolute sum when all summands but one are "AA-dense"
  (e.g. reflexive, finite-dimensional, or with a dense linear subspace inside NA(X_i,R)) and the
  remaining one has property P (NA(X_1,F) dense for all finite-dimensional F).
- P7/P15 (PROVED) the lineability criterion passes to finite absolute/lattice sums, c_0-sums,
  l_p-sums (1<p<oo), C(K,X) for scattered K, and to X (x)_pi Z whenever every operator X -> Z^* is a
  norm limit of finite-rank operators (then the dense subspace even consists of norm-attaining
  BILINEAR forms). K(H) = H (x)_eps H is lineable (P14).
- P13 (PROVED) Schachermayer's property alpha is stable under projective tensor products.
- OPEN: the converse for X_1 (+)_oo X_2 (or (+)_p) with BOTH summands merely having P. It follows from a
  positive JW answer; a failure would refute JW (Proposition 8). No literature found.

Notation. NA(X,Y) = {T in L(X,Y): ||Tx|| = ||T|| for some x in S_X}. NA is a cone containing 0, so
NA(X,Y) is dense iff every norm-one T is a limit of elements of NA(X,Y).
Property P of X: NA(X,F) is dense in L(X,F) for every finite-dimensional F.
Property B of Y: NA(Z,Y) dense for every Banach space Z. JW question: does every finite-dimensional Y
have B? (Equivalently: does every X have P?) KNOWN (given background): polyhedral finite-dimensional Y
have B (Lindenstrauss 1963), so only non-polyhedral Y matter; for Y = R density is Bishop-Phelps.

## 1. Preliminaries

### Lemma 1.1 (adjoint criterion) -- PROVED
T in NA(X,Y) iff there is y* in S_{Y*} with ||T* y*|| = ||T|| and T* y* in NA(X,R).
Proof. (=>) Let x in S_X with ||Tx|| = ||T||. Hahn-Banach gives y* in S_{Y*} with y*(Tx) = ||Tx||.
Then (T*y*)(x) = ||T|| >= ||T*y*|| (because ||T*y*|| <= ||T||), so ||T*y*|| = ||T|| and T*y* attains
its norm at x. (<=) If T*y* attains its norm at x in S_X, then ||Tx|| >= y*(Tx) = ||T*y*|| = ||T||. QED
For finite-dimensional Y the function y* -> ||T*y*|| is continuous on the compact S_{Y*} and
||T|| = max of it, so maximizers exist.

### 1.2 Absolute norms -- PROVED (standard facts, proofs included)
a is a norm on R^2 with a(s,t) = a(|s|,|t|) and a(1,0) = a(0,1) = 1.
(i) Monotonicity: |s| <= |s'| and |t| <= |t'| imply a(s,t) <= a(s',t').
Proof: fix t; g(s) = a(s,t) is even and convex. For 0 <= s <= s' with s' > 0 write
s = lam*s' + (1-lam)(-s') with lam = (1 + s/s')/2 in [1/2,1]; then
g(s) <= lam g(s') + (1-lam) g(-s') = g(s'). Same in the second variable.
(ii) max(|s|,|t|) <= a(s,t) <= |s| + |t|: the upper bound is the triangle inequality,
a(s,t) <= a(s,0) + a(0,t); the lower bound is (i): a(s,t) >= a(s,0) = |s|, and similarly >= |t|.
(iii) The dual norm a*(alpha,beta) = max{ |alpha| s + |beta| t : a(s,t) <= 1 } is again absolute
and normalized (the unit ball of a is compact and invariant under coordinate sign changes; a*(1,0) =
max{s : a(s,t) <= 1} = 1 by (ii)). For alpha, beta >= 0 the max is attained at some (s,t) >= 0 with
a(s,t) = 1 (compactness; replacing (s,t) by (|s|,|t|) does not decrease the value).
(iv) a* is monotone (by (i) applied to a*) and convex.
X_1 (+)_a X_2 := X_1 x X_2 with ||(x_1,x_2)|| = a(||x_1||, ||x_2||). It is a Banach space: the triangle
inequality follows from (i): a(||x_1+y_1||, ||x_2+y_2||) <= a(||x_1||+||y_1||, ||x_2||+||y_2||) <=
a(||x_1||,||x_2||) + a(||y_1||,||y_2||); completeness from the equivalence with the l_1-norm (ii).

### Lemma 1.2 (dual of an absolute sum; NA functionals) -- PROVED
Every f in (X_1 (+)_a X_2)* is f(x_1,x_2) = f_1(x_1) + f_2(x_2) with f_i = f o J_i, and
||f|| = a*(||f_1||, ||f_2||). If f_1 in NA(X_1,R) and f_2 in NA(X_2,R), then f in NA(X_1 (+)_a X_2, R).
Proof. |f(x)| <= ||f_1|| ||x_1|| + ||f_2|| ||x_2|| <= a*(||f_1||,||f_2||) a(||x_1||,||x_2||) by the
definition of a* (apply it to (||x_1||,||x_2||)/a(||x_1||,||x_2||)). Choose (s,t) >= 0, a(s,t) = 1,
with s||f_1|| + t||f_2|| = a*(||f_1||,||f_2||) (1.2(iii)). Given delta > 0 choose z_i in S_{X_i} with
f_i(z_i) >= ||f_i|| - delta; x = (s z_1, t z_2) has norm a(s,t) = 1 and f(x) >= a*(...) - 2 delta.
Hence ||f|| = a*(||f_1||,||f_2||). If both f_i attain their norms, take z_i with f_i(z_i) = ||f_i||
(any unit vector if f_i = 0); then f(x) = ||f|| exactly. QED

### 1.3 Banach sequence lattices and E-sums
E is a Banach space of real functions on a set I != {} with (L1) ideal property: b in E and |a_i| <= |b_i|
for all i imply a in E and ||a||_E <= ||b||_E; (L2) every unit vector e_i lies in E with ||e_i||_E = 1.
(L1)+(L2) give |b_i| = || |b_i| e_i ||_E <= ||b||_E for every b in E and i in I.
E(X_i) = (+)_E X_i := {x = (x_i): x_i in X_i, (||x_i||)_i in E}, ||x|| = ||(||x_i||)_i||_E.
Completeness (PROVED): if (x^n) is Cauchy, then ||x^n_i - x^m_i|| <= ||x^n - x^m||, so x^n_i -> x_i.
For fixed n, the functions d^{n,m} = (||x^n_i - x^m_i||)_i are Cauchy in E as m -> oo (because
| ||x^n_i - x^m_i|| - ||x^n_i - x^k_i|| | <= ||x^m_i - x^k_i||), with limit d^n in E; norm convergence
in E implies coordinatewise convergence, so d^n_i = ||x^n_i - x_i||. Thus x^n - x lies in E(X_i), and
||x^n - x|| = ||d^n||_E = lim_m ||x^n - x^m|| -> 0 as n -> oo. Examples: l_p (1<=p<=oo), c_0, Orlicz and
Lorentz sequence spaces. Finite I and E absolute normalized on R^I: finite lattice sums.
For an absolute norm a on R^2, X_1 (+)_a X_2 is the E-sum with E = (R^2, a).

### 1.4 AA operators
AA(X,Y) := {S in L(X,Y): S* y* in NA(X,R) for every y* in Y*} ("all-attaining").
(a) For Y finite-dimensional, AA(X,Y) is contained in NA(X,Y) (Lemma 1.1 plus compactness of S_{Y*}).
(b) If X is reflexive, AA(X,Y) = L(X,Y) (every functional attains its norm on the weakly compact ball).
(c) (KLMW criterion; Preprint B Lemma densesubspace; PROVED) If V is a linear subspace of X* contained
in NA(X,R) and dense in X*, then AA(X,Y) is dense in L(X,Y) for every finite-dimensional Y.
Proof: write T = sum_{k<=d} phi_k (x) y_k with (y_k) a basis of Y, approximate phi_k by psi_k in V and
put S = sum psi_k (x) y_k; then S* y* = sum_k y*(y_k) psi_k lies in V, which is inside NA(X,R). QED
(d) If S_i in AA(X_i,Y) (i = 1,2), then (S_1,S_2) in AA(X_1 (+)_a X_2, Y) (Lemma 1.2, applied to
(S_1* y*, S_2* y*)). Same for finite lattice sums (same proof with E* in place of a*).

## 2. l_1-sums: Theorem 1 -- PROVED (task item (1)(a))

Theorem 1. Let (X_i)_{i in I} be any nonempty family of Banach spaces, X = (+)_{l_1} X_i, Y ANY Banach
space. Then NA(X,Y) is dense in L(X,Y) iff NA(X_i,Y) is dense in L(X_i,Y) for every i in I.
Literature: KNOWN in the property-A form ("Lindenstrauss property A is stable under arbitrary
l_1-sums", attributed in Aron-Choi-Kim-Lee-Martin 2015 to Choi-Song 2008; confirmed by search snippet).
The fixed-Y form is presumably folklore (FROM MEMORY: an l_1-sum lemma of this type appears in
Paya-Saleh 2000; not confirmed). The proof below is self-contained.

Notation: J_i : X_i -> X canonical isometric embedding; P_i : X -> X_i coordinate map (norm 1);
for A in L(X,Y) put A_i := A J_i.

Lemma 2.1. (a) ||A|| = sup_i ||A_i|| for A in L(X,Y). (b) If (B_i)_i is a family with B_i in L(X_i,Y)
and sup_i ||B_i|| < oo, then B x := sum_i B_i x_i defines B in L(X,Y) with B J_i = B_i and
||B|| = sup_i ||B_i||.
Proof. For x in X only countably many x_i are nonzero and sum_i ||x_i|| = ||x||. (b): the series
sum_i B_i x_i converges absolutely, since sum ||B_i x_i|| <= (sup_i ||B_i||) ||x||; B is linear,
||Bx|| <= sup_i ||B_i|| ||x||, and ||B|| >= ||B J_i|| = ||B_i||. (a): x = sum_i J_i x_i converges in X,
so Ax = sum_i A_i x_i, and the same estimate gives ||A|| <= sup_i ||A_i||; the reverse is clear. QED

Proof of "<=". Let T in L(X,Y), ||T|| = 1, 0 < eps < 1/4. By Lemma 2.1(a) choose i0 with
||T_{i0}|| > 1 - eps. By hypothesis choose S_0 in NA(X_{i0},Y) with ||S_0 - T_{i0}|| < eps. Then
||S_0|| > 1 - 2 eps > 0 and ||S_0|| < 1 + eps. Put S_0' := S_0/||S_0||; it is in NA(X_{i0},Y), has norm
1, and ||S_0' - T_{i0}|| <= | 1 - ||S_0|| | + ||S_0 - T_{i0}|| < 2 eps + eps = 3 eps. Define B_{i0} := S_0'
and B_i := T_i for i != i0; by Lemma 2.1(b) this defines S in L(X,Y) with ||S|| = max(1, sup_{i!=i0}
||T_i||) = 1 (note ||T_i|| <= ||T|| = 1). Let z in S_{X_{i0}} with ||S_0' z|| = 1. Then J_{i0} z is in
S_X and ||S J_{i0} z|| = 1 = ||S||, so S is in NA(X,Y). Finally ||S - T|| = sup_i ||(S - T) J_i|| =
||S_0' - T_{i0}|| < 3 eps (Lemma 2.1(a)). Since eps is arbitrary, NA(X,Y) is dense.

Proof of "=>". Fix i0 and T_0 in L(X_{i0},Y) with ||T_0|| = 1; let T := T_0 P_{i0} (norm 1). Let
0 < eps < 1/2 and S in NA(X,Y) with ||S - T|| < eps; S attains its norm at x in S_X. Then
||S|| = ||Sx|| = || sum_i S_i x_i || <= sum_i ||S_i|| ||x_i|| <= ||S|| sum_i ||x_i|| = ||S||,
so every inequality is an equality. Since ||S_i|| <= ||S|| for every i, the equality
sum ||S_i|| ||x_i|| = ||S|| sum ||x_i|| forces ||S_i|| = ||S|| whenever x_i != 0. For i != i0 we have
T J_i = 0, hence ||S_i|| = ||(S - T) J_i|| < eps < 1 - eps < ||S||; therefore x_i = 0 for every
i != i0, so x = J_{i0} x_{i0} with ||x_{i0}|| = 1, and ||S_{i0} x_{i0}|| = ||Sx|| = ||S|| >= ||S_{i0}||.
Thus S_{i0} is in NA(X_{i0},Y) and ||S_{i0} - T_0|| = ||(S - T) J_{i0}|| < eps. QED

Remark 2.2. In the "<=" construction the approximant attains its norm at a vector supported on ONE
coordinate. This is used in Proposition 11 below.

## 3. Every absolute sum and every lattice sum: Theorem 2 -- PROVED (task item (1)(b))

Definition (AD). Let X be a Banach space, X = X_1 (+) W an algebraic direct sum of closed subspaces
(write x = x_1 + w). We say (AD) holds if: for all x_1, u in X_1, w in W and lambda in [-1,1],
    ||u|| <= ||x_1||   implies   ||u + lambda w|| <= ||x_1 + w||.
Taking u = x_1, lambda = 0 gives ||x_1|| <= ||x_1 + w||, so the projection P onto X_1 along W has
||P|| <= 1; taking u = 0, lambda = 1 gives ||w|| <= ||x_1 + w||, so ||I - P|| <= 1.

Lemma 3.1 (examples) -- PROVED. (AD) holds in the following cases.
(a) X = X_1 (+)_a X_2 for any absolute normalized a, X_1 = X_1 x {0}, W = {0} x X_2:
||(u, lambda w)|| = a(||u||, |lambda| ||w||) <= a(||x_1||, ||w||) by monotonicity 1.2(i).
(b) X = E(X_i) for a Banach sequence lattice E on I, X_1 = J_{i0}(X_{i0}), W = {x: x_{i0} = 0}: the norm
sequence of u + lambda w is (||u|| at i0, |lambda| ||w_i|| at i != i0), coordinatewise dominated by the
norm sequence of x_1 + w; apply (L1).
(c) Consequently: l_p(X_i) (1 <= p <= oo), c_0(X_i), L_1(mu,X) when mu has an atom (it is an l_1-sum),
C(K,X) when K has an isolated point k0 (C(K,X) = X (+)_oo C(K \ {k0}, X) isometrically via
f -> (f(k0), f restricted to K \ {k0}); K \ {k0} is compact because {k0} is open).

Theorem 2. Assume (AD) and let Y be ANY Banach space. If NA(X,Y) is dense in L(X,Y), then NA(X_1,Y) is
dense in L(X_1,Y). Quantitatively: if T_1 in L(X_1,Y), ||T_1|| = 1, 0 < eps < 1/4, and S in NA(X,Y)
satisfies ||S - T_1 P|| < eps, then there is R in NA(X_1,Y) with ||R - T_1|| < 3 eps.

Proof (this is exactly the route suggested in the task; it works for every absolute norm).
T := T_1 P has ||T|| = 1: ||Tx|| <= ||T_1|| ||Px|| <= ||x||, and T = T_1 on X_1.
Let S be as in the statement; S attains its norm at x = x_1 + w in S_X. Put S_1 := S restricted to X_1,
S_W := S restricted to W. Since T vanishes on W, ||S_W|| = ||(S - T) restricted to W|| < eps; since
T = T_1 on X_1, ||S_1 - T_1|| < eps. Also 1 - eps < ||S|| < 1 + eps and ||w|| <= ||x|| = 1 by (AD).
Step 1 (x_1 is not small): ||S|| = ||S x_1 + S w|| <= ||S_1|| ||x_1|| + ||S_W|| ||w||
<= ||S|| ||x_1|| + eps, so c := ||x_1|| >= 1 - eps/||S|| > 1 - eps/(1-eps) = (1-2eps)/(1-eps) > 0.
Step 2 (the operator R): choose phi in X_1* with ||phi|| = 1 and phi(x_1) = c (Hahn-Banach), and
define E : X_1 -> X, E u := u + (phi(u)/c) w, and R := S E, i.e. R u = S_1 u + (phi(u)/c) S w.
Step 3 (||E|| <= 1/c): for u in B_{X_1} write E u = c^{-1} (c u + phi(u) w). Here cu is in X_1 with
||cu|| <= c = ||x_1||, and lambda := phi(u) lies in [-1,1]. By (AD), ||c u + lambda w|| <= ||x_1 + w|| =
1. Hence ||E u|| <= 1/c.
Step 4 (R attains its norm): E(x_1/c) = x_1/c + (phi(x_1)/c^2) w = (x_1 + w)/c = x/c. So
R(x_1/c) = Sx/c has norm ||S||/c, while ||R|| <= ||S|| ||E|| <= ||S||/c and ||x_1/c|| = 1. Hence
R is in NA(X_1,Y) (with ||R|| = ||S||/c).
Step 5 (R is close to T_1): ||R - S_1|| <= ||S w||/c <= eps/c, so ||R - T_1|| < eps/c + eps
< eps (1-eps)/(1-2eps) + eps < 3 eps for eps < 1/4. As eps -> 0 and NA is a cone, NA(X_1,Y) is dense. QED

Corollary 3.2. For every absolute norm a: NA(X_1 (+)_a X_2, Y) dense => NA(X_1,Y) and NA(X_2,Y) dense.
For every Banach sequence lattice E: NA(E(X_i),Y) dense => NA(X_i,Y) dense for each i. Any Y.
(Infinite families included; types 1, 2 and oo of absolute norms included.)

Remark 3.3 (literature). Choi-Dantas-Jung-Martin (Mediterr. J. Math. 16 (2019), arXiv 1806.09366) study
inheritance of the BPBp and of density of NA by absolute summands. Search snippets (we could not read
the full text) state the domain-side BPBp result for absolute summands of type 1 or oo, and one snippet
says the density analogue on the domain side is stated for type 1. Theorem 2 covers all absolute norms
and all lattice sums for plain density; it is elementary and possibly known to experts, but we found no
statement of it. The BPBp version for general absolute norms is a different (harder) question and is
NOT claimed here.

## 4. Universality: Theorem 4 -- PROVED (task items (1)(c), (2)(a))

Theorem 4. Fix a finite-dimensional Y. Let C be any one of the classes
 (C1) {X (+)_a Z : X, Z Banach} for a fixed absolute normalized a; also the diagonal class {X (+)_a X};
 (C2) {E(X_i)} or the constant-family class {E(X)} for a fixed Banach sequence lattice E
      (e.g. {l_p(X)}, 1 <= p <= oo, {c_0(X)});
 (C3) {X (x)_pi l_1^n} (n >= 1 fixed), {X (x)_pi l_1}, {X (x)_pi L_1(mu)} (mu fixed, sigma-finite, nonzero);
 (C4) {X (x)_eps l_oo^n}, {X (x)_eps c_0}, {C(K) (x)_eps X} (K fixed with an isolated point);
 (C5) all projective (resp. all injective) tensor products X (x) Z with dim X, dim Z >= 2.
Then: NA(W,Y) is dense for every W in C  <=>  Y has property B.
Proof. "<=" is trivial. "=>": let X be any Banach space. (C1): NA(X (+)_a X, Y) dense gives NA(X,Y)
dense by Theorem 2. (C2): Theorem 2 with Lemma 3.1(b). (C3): X (x)_pi l_1^n = l_1^n(X) and
X (x)_pi l_1 = l_1(X) isometrically (Proposition 9), then Theorem 1; X (x)_pi L_1(mu) = L_1(mu,X)
(Proposition 9), then Theorem 10 (works also for atomless mu). (C4): X (x)_eps l_oo^n = l_oo^n(X),
X (x)_eps c_0 = c_0(X), C(K) (x)_eps X = C(K,X) = X (+)_oo C(K\{k0},X) (Proposition 9, Lemma 3.1(c)),
then Theorem 2. (C5) contains X (x)_pi l_1^2 resp. X (x)_eps l_oo^2. QED

Corollary 4.1. "NA(W,F) dense for every W in C and every finite-dimensional F" is equivalent to a
positive answer to the Johnson-Wolfe question. A counterexample W in C (for some Y) forces a
counterexample X (a summand / tensor factor) for the same Y; conversely any counterexample Z gives
counterexamples Z (+)_a Z, l_p(Z), c_0(Z), Z (x)_pi l_1^2, L_1([0,1],Z), ... for the same Y.
Corollary 4.2 (transfer for Martin's space; uses Proposition 11 and Proposition 6). Let 𝔛 be Martin's
renorming of c_0 (𝔛* is isomorphic to l_1, so has RNP). Then P(𝔛) <=> P(l_1(𝔛)) <=> P(L_1([0,1],𝔛))
<=> P(𝔛 (+)_a G) for any reflexive G and any absolute a. Each of P(c_0(𝔛)), P(l_oo^n(𝔛)) implies P(𝔛);
the converse implications are instances of the OPEN question of Section 5.5.

## 5. The converse direction for c_0, l_oo, l_p sums (task item (1)(d))

### 5.1 l_1-sums: the converse holds (Theorem 1), for every Y.

### Proposition 5 (reduction to finite subsums; Y finite-dimensional) -- PROVED
Let X = c_0(X_i) (any infinite I) or X = l_p(X_i) with 1 < p < oo, and Y finite-dimensional. For a
finite F in I let X_F be the corresponding finite subsum ((+)_{i in F} X_i with the l_oo, resp. l_p
norm), pi_F : X -> X_F the coordinate map and P_F = (inclusion) o pi_F. Then NA(X,Y) is dense iff
NA(X_F,Y) is dense for every finite F.
Proof. "=>": X = X_F (+)_oo X_{I\F} (resp. (+)_p), an absolute sum; apply Theorem 2.
"<=": X* = l_1(X_i*) for c_0-sums and X* = l_q(X_i*) (1/p + 1/q = 1) for l_p-sums (standard). Write
T in L(X,Y) as T = sum_{k<=d} phi_k (x) y_k. For phi in X*, ||phi - phi P_F|| = sum_{i not in F}
||phi_i|| (resp. (sum_{i not in F} ||phi_i||^q)^{1/q}), which tends to 0 along the net of finite F.
Hence ||T - T P_F|| -> 0. Now T P_F = T_F o pi_F with T_F = T restricted to X_F. If S_F in NA(X_F,Y) is
close to T_F and attains at z in S_{X_F}, then S := S_F o pi_F has ||S|| = ||S_F|| (pi_F has norm 1
and is the identity on X_F), attains at z, and ||S - T P_F|| <= ||S_F - T_F||. QED
(For p = 1 the tail estimate fails, e.g. phi = (1,1,1,...) on l_1, but Theorem 1 handles l_1.)
(For infinite l_oo-sums no such reduction exists: X* contains functionals vanishing on c_0(X_i).)

### Proposition 6 (one arbitrary summand, the others all-attaining) -- PROVED
Let a be an absolute normalized norm, Y finite-dimensional, X = X_1 (+)_a X_2. Assume
 (H1) NA(X_1, F) is dense in L(X_1,F) for every norm F on the vector space Y (in particular if P(X_1));
 (H2) AA(X_2, Y) is dense in L(X_2, Y) (e.g. X_2 reflexive, or finite-dimensional, or NA(X_2,R)
      contains a dense linear subspace -- 1.4(b),(c)).
Then NA(X,Y) is dense in L(X,Y).
Proof. Write T = (T_1,T_2), T(x_1,x_2) = T_1 x_1 + T_2 x_2, ||T|| = 1, and let eps > 0.
Step 0. Choose S_2 in AA(X_2,Y) with ||S_2 - T_2|| < eps; T'' := (T_1,S_2) has | ||T''|| - 1 | < eps;
T' := T''/||T''|| = (T_1', S_2') with S_2' in AA (AA is a cone), ||T' - T|| < 2 eps, ||T'|| = 1.
Step 1 (norm formula). By Lemma 1.2, ||T'^* y*|| = a*(h_1(y*), h_2(y*)) where h_1(y*) = ||T_1'^* y*||,
h_2(y*) = ||S_2'^* y*||. So for any R_1 in L(X_1,Y): ||(R_1, S_2')|| <= 1 iff for all y* in S_{Y*},
||R_1^* y*|| <= psi(y*) := phi(h_2(y*)), where phi(beta) := max{alpha >= 0 : a*(alpha,beta) <= 1}
for 0 <= beta <= 1. [a*(.,beta) is continuous, nondecreasing in alpha >= 0, tends to oo, and
a*(0,beta) = beta <= 1; so {alpha >= 0: a*(alpha,beta) <= 1} = [0, phi(beta)] and a*(phi(beta),beta) = 1.]
Step 2 (degenerate case). If ||S_2'|| = 1, then S_2' is in NA (1.4(a)), say ||S_2' z|| = 1 with z in S_{X_2},
and T'(0,z) = S_2' z has norm 1 = ||T'|| with ||(0,z)|| = a(0,1) = 1; so T' is already in NA.
Step 3 (the body D). Assume r_2 := ||S_2'|| < 1. phi is nonincreasing (a* monotone), concave on [0,1]
(the set {(alpha,beta) >= 0 : a*(alpha,beta) <= 1} is convex), phi(0) = 1, phi > 0 on [0,1), hence phi is
continuous on [0, r_2] (a concave function is continuous on the interior of its domain; at 0 use
phi(beta) >= (1 - beta/r)phi(0) + (beta/r)phi(r) for 0 <= beta <= r). Thus psi is continuous on S_{Y*}
with values in [phi(r_2), 1], phi(r_2) > 0. Let D := {v in Y : y*(v) <= psi(y*) for all y* in S_{Y*}}.
D is closed, convex, symmetric (psi(-y*) = psi(y*)), phi(r_2) B_Y is contained in D and D is contained
in B_Y. Let p_D be its gauge, a norm on Y with ||y|| <= p_D(y). By Step 1, ||(R_1,S_2')|| <= 1 iff
R_1(B_{X_1}) is contained in D iff ||R_1||_{X_1 -> (Y,p_D)} <= 1.
Step 4 (||T_1'||_D = 1). It is <= 1 since ||T'|| = 1. If it were r < 1, then h_1 <= r psi, and by
monotonicity and convexity of a*, a*(r phi(beta), beta) <= r a*(phi(beta),beta) + (1-r) a*(0,beta)
<= r + (1-r) r_2 < 1 for every beta = h_2(y*) <= r_2; so ||T'|| < 1, a contradiction.
Step 5 (approximate in the new norm). By (H1) pick S_1 in NA(X_1,(Y,p_D)) with ||S_1 - T_1'||_D < eta.
Normalize S_1' := S_1/||S_1||_D: still norm attaining in (Y,p_D), ||S_1' - T_1'||_D < 2 eta, and
S_1'(B_{X_1}) is contained in D. Let x_1 in S_{X_1} with p_D(S_1' x_1) = 1 and v := S_1' x_1.
Step 6 (contact functional). There is y* in S_{Y*} with y*(v) = psi(y*). Otherwise the continuous
function y* -> psi(y*) - y*(v) is positive on the compact S_{Y*}, hence >= delta > 0, so v + delta B_Y is
contained in D, (1 + delta')v is in D for small delta' > 0, and p_D(v) < 1 -- contradiction.
Step 7 (S attains). Let S := (S_1', S_2'); ||S|| <= 1 by Step 3. For the y* of Step 6: ||S_1'^* y*|| <=
psi(y*) (as S_1'(B) is contained in D) and (S_1'^* y*)(x_1) = psi(y*), so S_1'^* y* attains its norm
psi(y*) = phi(beta), beta := h_2(y*). S_2'^* y* attains its norm beta (S_2' in AA). By Lemma 1.2,
S^* y* = (S_1'^* y*, S_2'^* y*) attains its norm, which equals a*(phi(beta),beta) = 1 >= ||S||. By
Lemma 1.1, S is in NA(X,Y).
Step 8 (distance). ||S - T'|| = sup over a(s,t) <= 1 ... = ||S_1' - T_1'||_{X_1 -> Y} <= ||S_1' -
T_1'||_D < 2 eta (since ||y|| <= p_D(y)); hence ||S - T|| < 2 eps + 2 eta. QED
[Detail for Step 8: (S - T')(x_1,x_2) = (S_1' - T_1')x_1 and ||x_1|| <= ||(x_1,x_2)|| by 1.2(ii).]

Corollary 6.1 -- PROVED. (a) P(X_1) and X_2 reflexive (or lineable, or finite-dimensional) imply
P(X_1 (+)_a X_2) for every absolute a. (b) By induction with 1.4(d) and associativity of l_p and l_oo
sums: if P(X_{i0}) and every X_i (i != i0) is AA-dense for every finite-dimensional range (e.g.
reflexive or lineable), then P holds for every finite l_p/l_oo sum and, by Proposition 5, for c_0(X_i)
and l_p(X_i) (1<p<oo). (c) In particular P(X) implies P(X (+)_oo l_2), P(X (+)_p F) for finite-dim F.
Remark 6.2 (Preprint B). (X,p) with B_p = B_q + U(B_G) is the quotient of (X,q) (+)_oo G by the kernel of
(x,g) -> x + Ug; Corollary 6.1 gives P((X,q) (+)_oo G) from P(X,q), but the Transfer Theorem of Preprint
B needs approximants of the special form (S, SU); that extra step is what Preprint B supplies. No conflict.
For finite lattice sums (general E on R^n) the proof of Proposition 6 goes through verbatim with
phi(beta_2..beta_n) := max{alpha: ||(alpha,beta_2,..,beta_n)||_{E*} <= 1} (SKETCH: not rewritten).

### Proposition 7 (the lineability criterion passes to sums) -- PROVED (task item (2)(d), sums part)
Let V_i be a linear subspace of X_i*, dense in X_i*, contained in NA(X_i,R).
(a) Finite absolute sums X_1 (+)_a X_2: V_1 x V_2 is a dense linear subspace of (X_1 (+)_a X_2)* =
X_1* (+)_{a*} X_2* contained in NA (Lemma 1.2). Same for finite lattice sums and finite l_1-sums.
(b) c_0(X_i): V := {(f_i) : f_i in V_i, f_i = 0 for all but finitely many i}. Dense in l_1(X_i*): given g
and eps choose finite F with sum_{i not in F} ||g_i|| < eps and f_i in V_i with ||f_i - g_i|| < eps/|F|
(i in F). NA: if f has support F, pick z_i in S_{X_i} with f_i(z_i) = ||f_i|| (i in F); x := sum_{i in F}
J_i z_i is in S_X and f(x) = sum ||f_i|| = ||f||.
(c) l_p(X_i), 1<p<oo, X* = l_q(X_i*): same V. If f has support F and z_i norms f_i, put
x := c sum_{i in F} ||f_i||^{q-1} J_i z_i with c = (sum_{i in F} ||f_i||^q)^{-1/p}; then ||x||_p = 1 and
f(x) = c sum ||f_i||^q = (sum ||f_i||^q)^{1/q} = ||f||.
(d) C(K,X) with K scattered compact, X lineable via V: C(K,X)* = rcabv(K,X*) (Singer; KNOWN, FROM MEMORY);
every regular measure on a scattered compactum is purely atomic (KNOWN, FROM MEMORY), so for m in
C(K,X)*, |m| is carried by a countable set D and m = sum_{t in D} delta_t (x) m({t}) with
||m|| = sum ||m({t})||. Finitely supported atomic measures with atoms in V form a dense linear subspace;
each attains: for m = sum_{j<=n} delta_{t_j} (x) v_j choose disjoint open U_j containing t_j, Urysohn
functions u_j (u_j(t_j) = 1, 0 <= u_j <= 1, support in U_j) and z_j in S_X norming v_j; f := sum u_j z_j
has ||f|| <= 1 and m(f) = sum ||v_j|| = ||m||. (Proof complete modulo the two KNOWN facts.)
Consequence: if every X_i is lineable (e.g. reflexive: V_i = X_i*), then P holds for all sums in (a)-(d).
This contains the KNOWN result of Kadets-Lopez-Martin-Werner that finite-rank operators from a c_0-sum
of reflexive spaces are approximable by NA operators (confirmed by search snippet).
(e) FALSE (naive transfer to infinite l_1-sums): the set {(f_i) in l_oo(X_i*): f_i in V_i} is NOT inside
NA(l_1(X_i),R): take X_i = R, f = (1 - 1/i)_i, whose sup is not attained. For l_1 itself lineability
does hold (finitely-valued sequences: a dense linear subspace of l_oo whose elements attain their sup).
For l_1(X_i) with infinite-dimensional X_i we do not know (OPEN here; not needed, Theorem 1 suffices).

### Proposition 8 (logical status of the general converse) -- PROVED (i)-(iii); (iv),(v) HEURISTIC
Let (C_a) be the statement: for all Banach X_1, X_2, P(X_1) and P(X_2) imply P(X_1 (+)_a X_2).
(i) A positive answer to JW implies (C_a) (trivial).
(ii) If (C_a) fails for some pair, X_1 (+)_a X_2 fails P, i.e. some finite-dimensional Y fails property
B: a negative answer to JW. So (C_a) cannot be refuted without refuting JW.
(iii) (C_oo) implies, by induction and Proposition 5, that P is stable under arbitrary c_0-sums and under
l_p-sums (1<p<oo) via (C_p); conversely stability under c_0-sums contains (C_oo).
(iv) HEURISTIC: no reduction of JW to (C_a) is visible, because by Theorem 2 every absolute summand of a
P-space has P; so (C_a) may well be provable without solving JW. We did not find it in the literature
(searches for stability of property A or of density under l_oo/c_0 sums returned only l_1-results,
range-side results and BPBp results).
(v) HEURISTIC (where the difficulty is): by Lemmas 1.1-1.2, T = (T_1,T_2) attains its norm iff some
maximizer y* of a*(||T_1* y*||, ||T_2* y*||) has T_1* y* and T_2* y* both norm-attaining (for a = l_p,
1<p<oo, and a = l_oo, every norming pair (s,t) of a vector with both coordinates positive has s,t > 0,
so both components must attain; for a = l_1 only the dominant one must attain, which is why Theorem 1
is easy). Property P of each X_i controls one attaining direction at a time; in Proposition 6 the contact
direction y* is produced by the approximation in the norm p_D and is not controlled exactly. For
strictly convex Y (e.g. l_2^2) the body D = B_Y minus-Minkowski cl S_2(B) is an intersection of
translates of B_Y and has no facets, so the contact direction cannot be pinned by a polyhedral cut; one
needs S_2* to attain on a whole neighbourhood of directions, which AA provides.

### 5.5 Infinite-dimensional ranges (context only; outside the question)
KNOWN (confirmed by search snippets): c_0, C[0,1] and L_1[0,1] fail property A; C_0(L) fails A for
infinite L (Martin's lecture notes); L_1(mu) has A iff mu is purely atomic. Hence for infinite-dimensional
ranges the converse FAILS for infinite c_0-sums (c_0 = c_0(R)), for infinite l_oo-sums (l_oo = C(beta N)
= l_oo(R)), and for L_1(mu) (x)_pi (.) with atomless mu (L_1[0,1] = L_1([0,1],R)), although R has A.
For a finite l_oo- or l_p-sum of two spaces with property A we found nothing either way (OPEN as far as
we know). Range side, KNOWN (confirmed snippet): property B is stable under arbitrary c_0-sums.

### 5.6 Status table for (1)(d), Y finite-dimensional
- l_1-sums, any family: converse TRUE (Theorem 1, any Y).
- c_0-sums, l_p-sums (1<p<oo): equivalent to the finite-subsum statements (Proposition 5).
- Finite absolute/l_oo/l_p sums: TRUE if all summands but one are AA-dense and the remaining one has P
  (Proposition 6, Corollary 6.1); TRUE if all summands are lineable (Proposition 7). In general OPEN,
  and a counterexample would refute JW (Proposition 8).
- Infinite l_oo-sums l_oo(X_i): no reduction; even P(l_oo(l_2)) is not settled here (OPEN here).
  Known special case: P(l_oo) (Johnson-Wolfe: l_oo^* is an L_1-space); P(l_oo(E)) for finite-dim E
  (Proposition 12(b), since l_oo(E) = C(beta N, E)).
- Inheritance (sum => summand): TRUE for all absolute and lattice sums (Theorem 2), any Y.

## 6. Tensor products: identifications, L_1(mu,X), C(K,X) (task item (2)(a))

### Proposition 9 (isometric identifications) -- PROVED (KNOWN: R. Ryan, Introduction to Tensor
Products of Banach Spaces, 2002, Ch. 2-3; FROM MEMORY for exact numbering)
(i) X (x)_pi l_1^n = l_1^n(X). J(sum_k x_k (x) a_k) := (sum_k a_k(i) x_k)_{i<=n} is a linear bijection
from the algebraic tensor product. ||J u|| = sum_i ||sum_k a_k(i) x_k|| <= sum_k ||x_k|| ||a_k||_1 for
every representation, so ||Ju|| <= pi(u); and u = sum_i z_i (x) e_i with z = Ju gives pi(u) <= sum_i
||z_i|| = ||Ju||.
(ii) X (x)_pi l_1 = l_1(X). Same J on the algebraic tensor product X (x) l_1 gives ||Ju|| <= pi(u).
For u = sum_k x_k (x) a_k, u - sum_{i<=N} z_i (x) e_i = sum_k x_k (x) (a_k - P_N a_k) has pi-norm
<= sum_k ||x_k|| ||a_k - P_N a_k||_1 -> 0, hence pi(u) <= sum_i ||z_i|| = ||Ju||. J is an isometry with
dense range (it contains the finitely supported sequences), so it extends to an onto isometry.
(iii) X (x)_eps l_oo^n = l_oo^n(X): for u = sum_i z_i (x) e_i, eps(u) = sup over x* in B_{X*}, b in B_{l_1^n}
of |sum_i b_i x*(z_i)| = sup_{x*} max_i |x*(z_i)| = max_i ||z_i||.
(iv) X (x)_eps c_0 = c_0(X): for u = sum_k x_k (x) a_k (a_k in c_0) put z_i = sum_k a_k(i) x_k, so
z in c_0(X); (x* (x) b)(u) = sum_i b_i x*(z_i) for b in l_1, hence eps(u) = sup_i ||z_i||; dense range.
(v) C(K) (x)_eps X = C(K,X): u = sum_k f_k (x) x_k -> (t -> sum_k f_k(t) x_k);
eps(u) = sup_{x*, mu in B_{M(K)}} |sum_k mu(f_k) x*(x_k)| = sup_{x*} ||sum_k x*(x_k) f_k||_oo =
sup_t ||sum_k f_k(t) x_k||. Dense range: for f in C(K,X) and delta > 0 cover the compact f(K) by finitely
many delta-balls B(x_k,delta), take a partition of unity (phi_k) subordinate to the open cover
{f^{-1}(B(x_k,delta))}; then ||f - sum_k phi_k x_k||_oo <= delta.
(vi) L_1(mu) (x)_pi X = L_1(mu,X) (mu sigma-finite): the L_1(mu,X)-norm is a cross norm <= pi by the
triangle inequality. For a simple u = sum_j 1_{B_j} (x) z_j with disjoint B_j of finite measure,
pi(u) <= sum_j mu(B_j) ||z_j|| = ||u||_{L_1(mu,X)}. A general u = sum_k g_k (x) x_k in L_1(mu) (x) X is
the pi-limit of u_n = sum_k s_{k,n} (x) x_k with simple s_{k,n} -> g_k in L_1(mu); each u_n is simple
(rewrite over the common refinement), so pi(u_n) = ||u_n||_{L_1(mu,X)}, and passing to the limit (both
norms continuous w.r.t. pi) gives pi(u) = ||u||_{L_1(mu,X)}. Simple functions are dense in L_1(mu,X).

### Theorem 10 (L_1(mu,X) => X) -- PROVED modulo the lifting theorem (KNOWN: von Neumann-Maharam; see
A. and C. Ionescu Tulcea, Topics in the Theory of Lifting, 1969; FROM MEMORY)
Let mu be sigma-finite with L_1(mu) != {0}, X a Banach space, Y finite-dimensional. If NA(L_1(mu,X),Y) is
dense in L(L_1(mu,X),Y), then NA(X,Y) is dense in L(X,Y). (No atom is needed.)
Proof. Step 0 (reduction). Pick A with 0 < mu(A) < oo. L_1(mu,X) = L_1(mu|A,X) (+)_1 L_1(mu|A^c,X)
isometrically, so by Theorem 1 NA(L_1(mu|A,X),Y) is dense. With nu := mu|A / mu(A), f -> mu(A) f is an
onto isometry L_1(mu|A,X) -> L_1(nu,X). Completing nu does not change L_1(nu,X). So assume nu is a
complete probability measure on (Omega, Sigma). Let rho : L_oo(nu) -> bounded measurable functions be a
lifting: rho(h) is a representative of h, rho is linear and multiplicative, rho(1) = 1; hence h >= 0
a.e. implies rho(h) = rho(sqrt h)^2 >= 0 everywhere. Fix a basis b_1..b_d of Y and put, for an
essentially bounded Y-valued H = sum_j h_j b_j, rho(H) := sum_j rho(h_j) b_j; then
y*(rho(H)(t)) = rho(y* o H)(t) for all y* in Y*, t in Omega (linearity).
Step 1 (densities). Let S in L(L_1(nu,X),Y). For x in X, m_x(A) := S(1_A (x) x) is a countably additive
(||1_{union A_k} (x) x - sum_{k<=n} 1_{A_k} (x) x||_1 -> 0), nu-continuous Y-valued measure with
||m_x(A)|| <= ||S|| ||x|| nu(A). Radon-Nikodym (coordinatewise, Y finite-dimensional) gives H_x with
m_x(A) = int_A H_x dnu. Claim: ||H_x(t)|| <= ||S|| ||x|| for a.e. t. Indeed, let (y_k*) be dense in
S_{Y*} and A_k := {t : y_k*(H_x(t)) > ||S|| ||x||}; if nu(A_k) > 0, then y_k*(m_x(A_k)) =
int_{A_k} y_k* o H_x dnu > ||S|| ||x|| nu(A_k) >= ||m_x(A_k)||, impossible; off the null set union A_k,
||H_x(t)|| = sup_k y_k*(H_x(t)) <= ||S|| ||x||. Also H_{alpha x + beta x'} = alpha H_x + beta H_{x'} a.e.
Step 2 (the operators S_t). Define S_t x := rho(H_x)(t). Since rho acts on a.e.-classes and is linear,
x -> S_t x is linear for EVERY t. Since y_k* o H_x <= ||S|| ||x|| a.e. for each k, positivity gives
y_k*(S_t x) = rho(y_k* o H_x)(t) <= ||S|| ||x|| for every t and k, so ||S_t|| <= ||S|| for every t.
Step 3 (representation). For f in L_1(nu,X), t -> S_t f(t) is measurable and Sf = int S_t f(t) dnu(t).
For simple f = sum_k 1_{A_k} (x) x_k (disjoint A_k): int S_t f(t) dnu = sum_k int_{A_k} rho(H_{x_k}) dnu
= sum_k int_{A_k} H_{x_k} dnu = sum_k S(1_{A_k} (x) x_k) = Sf. For general f choose simple f_n with
f_n -> f a.e. and ||f_n(t)|| <= 2||f(t)|| (take simple g_n -> f a.e. and f_n := g_n 1_{||g_n|| <= 2||f||});
then f_n -> f in L_1 (dominated convergence), S_t f_n(t) -> S_t f(t) a.e. with domination
2||S|| ||f(t)||, so t -> S_t f(t) is measurable (nu complete) and Sf = lim S f_n = int S_t f(t) dnu.
Step 4 (compatibility with T). Let T_0 in L(X,Y), ||T_0|| = 1, Phi(f) := int f dnu (||Phi|| <= 1,
Phi(1 (x) x) = x) and T := T_0 Phi, so ||T|| = 1. For the operator S - T the measures are
m_x - nu(.) T_0 x, with densities H_x - T_0 x, and rho(H_x - T_0 x) = rho(H_x) - T_0 x (rho(1) = 1).
So (S - T)_t = S_t - T_0 for every t, and Step 2 applied to S - T gives ||S_t - T_0|| <= ||S - T|| for
EVERY t.
Step 5. Let 0 < eps < 1 and S in NA(L_1(nu,X),Y) with ||S - T|| < eps, attaining at f, ||f||_1 = 1. Take
y* in S_{Y*} with y*(Sf) = ||S||. By Step 3, ||S|| = int y*(S_t f(t)) dnu <= int ||S_t|| ||f(t)|| dnu <=
||S|| int ||f(t)|| dnu = ||S||. The integrand ||S|| ||f(t)|| - y*(S_t f(t)) is >= 0 with integral 0, so
y*(S_t f(t)) = ||S|| ||f(t)|| for a.e. t. As {f != 0} has positive measure, pick t0 with f(t0) != 0 and
this equality; with u := f(t0)/||f(t0)||: ||S_{t0} u|| >= ||S|| >= ||S_{t0}||. So S_{t0} is in NA(X,Y)
and ||S_{t0} - T_0|| < eps (Step 4). Hence NA(X,Y) is dense. QED
Remarks. (1) For separable X the lifting can be avoided (define S_t on a countable Q-linear dense set off
one null set and extend). (2) The proof shows more: for a.e. t in supp f, S_t attains its norm and
||S_t|| = ||S||. (3) Novelty unknown; we found no statement of it (a BPBp-for-compact-operators relative
is in Dantas-Garcia-Maestre-Martin, arXiv 1604.00618, under the assumption X* has RNP).

### Proposition 11 (converse of Theorem 10 when X* has RNP) -- PROVED modulo KNOWN L_1(nu,X)* =
L_oo(nu,X*) (Bochner) for X* with RNP (Diestel-Uhl, Vector Measures, IV.1; FROM MEMORY)
If X* has RNP, Y is finite-dimensional and NA(X,Y) is dense, then NA(L_1(mu,X),Y) is dense
(mu sigma-finite; for general mu use that L_1(mu,X) is an l_1-sum of L_1's of finite measures + Thm 1).
Proof. By sigma-finiteness pick w > 0 with int w dmu = 1 and put dnu = w dmu; f -> f/w is an onto isometry L_1(mu,X) -> L_1(nu,X), so assume mu = nu is a probability measure. For S in L(L_1(nu,X),Y), b_j* o S is given by
g_j in L_oo(nu,X*) (strongly measurable). G(t) := sum_j g_j(t) (x) b_j is a strongly measurable bounded
L(X,Y)-valued function with Sf = int G(t) f(t) dnu. Off a null set G has separable range; for eps > 0
take a countable dense set (R_k) of that range and disjoint measurable A_k := {||G - R_k|| < eps} minus
earlier ones; G' := sum_k 1_{A_k} R_k satisfies ||G - G'|| < eps a.e., so S'f := int G'(t) f(t) dnu =
sum_k R_k(int_{A_k} f dnu) has ||S - S'|| <= eps. Now S' = R o Psi with Psi f := (int_{A_k} f dnu)_k,
Psi : L_1(nu,X) -> l_1(X) of norm <= 1, and R(z) := sum_k R_k z_k (sup ||R_k|| < oo). By Theorem 1 and
Remark 2.2, there is R' in NA(l_1(X),Y) with ||R' - R|| < eps attaining at J_{k0} z, ||z|| = 1, and
||R'|| = ||R'_{k0}||. Then S'' := R' o Psi attains its norm at f_0 := 1_{A_{k0}} (x) z / nu(A_{k0})
(Psi f_0 = J_{k0} z, ||S''|| <= ||R'||) and ||S'' - S|| < 2 eps. QED
Consequence: for X with X* RNP (e.g. every renorming of c_0, Martin's 𝔛, Read-type spaces):
P(L_1(mu,X)) <=> P(X).
(Detail for Prop. 11: index the l_1-sum only by k with nu(A_k) > 0; null A_k do not affect S'.)

### Proposition 12 (C(K,X) = C(K) (x)_eps X)
(a) PROVED. If K has an isolated point k0, C(K,X) = X (+)_oo C(K\{k0},X), so NA(C(K,X),Y) dense implies
NA(X,Y) dense (Theorem 2, any Y). This gives universality for (x)_eps (Theorem 4, class C4).
(b) SKETCH (standard measure theory not written out). If X* has RNP and P(l_oo^m(X)) holds for all m
(e.g. X reflexive: l_oo^m(X) is reflexive; or X finite-dimensional), then P(C(K,X)) for every compact K.
Outline: a finite-rank T on C(K,X) is given by finitely many m_k in rcabv(K,X*) (Singer); with the
control measure lambda = sum |m_k|, RNP gives Bochner densities g_k in L_1(lambda,X*); approximate g_k in
L_1(lambda,X*) by simple functions sum_j 1_{C_j} x*_{kj} with pairwise disjoint COMPACT C_j (regularity),
which changes T by little in operator norm. The new operator factors as R o Q with
Q f := (lambda(C_j)^{-1} int_{C_j} f dlambda)_{j<=m} : C(K,X) -> l_oo^m(X), ||Q|| <= 1, and Q maps the
closed ball ONTO the closed ball (for (x_j) in B take f = sum u_j x_j with Urysohn functions u_j = 1 on
C_j with disjoint supports). Approximate R by R' in NA(l_oo^m(X),Y) attaining at (x_j); then R' o Q
attains at f = sum u_j x_j. In particular P(l_oo(E)) for finite-dimensional E (l_oo(E) = C(beta N, E)).
(c) OPEN here: for perfect K (e.g. K = [0,1]) neither "NA(C(K,X),Y) dense => NA(X,Y) dense" nor its
converse for non-reflexive X. (The trick of Theorem 2 needs a contraction-valued continuous family A_t
with A_t x0 = f(t), A_{k0} = I; this fails in general, e.g. in l_4^2 at x0 = (1,0) there is no
contraction close to I mapping x0 to a nearby unit vector other than x0, because B_{l_4^2} is flatter
at (1,0) than at nearby points.)

## 7. Positive results for tensor products (task item (2)(b))

### Proposition 13 (property alpha is stable under (x)_pi) -- PROVED
Schachermayer's property alpha: there are (x_i, x_i*) in S_X x S_{X*}, i in I, with x_i*(x_i) = 1,
|x_i*(x_k)| <= lambda < 1 for i != k, and B_X = closed absolutely convex hull of {x_i}. If X has alpha
with (x_i,x_i*,lambda_X) and Z with (z_j,z_j*,lambda_Z), then X (x)_pi Z has alpha with
u_{ij} = x_i (x) z_j, phi_{ij} = x_i* (x) z_j* and lambda = max(lambda_X, lambda_Z).
Proof. pi(x_i (x) z_j) = 1, ||phi_{ij}|| = 1 (as a bilinear form), phi_{ij}(u_{ij}) = 1. For
(k,l) != (i,j): |phi_{ij}(u_{kl})| = |x_i*(x_k)| |z_j*(z_l)|, which is <= lambda_X if k != i and
<= lambda_Z if k = i, l != j. B_{X (x)_pi Z} is the closed absolutely convex hull of {x (x) z : x in B_X,
z in B_Z} (KNOWN, standard). If x = lim sum_k a_k x_{i_k} and z = lim sum_l b_l z_{j_l} with sum|a_k|,
sum|b_l| <= 1, then x (x) z = lim sum_{k,l} a_k b_l x_{i_k} (x) z_{j_l} (pi(x (x) z - x' (x) z') <=
||x - x'|| ||z|| + ||x'|| ||z - z'||) with sum |a_k b_l| <= 1; so the closed absolutely convex hull of
{u_{ij}} is the whole ball. QED  With Schachermayer's theorem (alpha => property A; KNOWN) X (x)_pi Z has
property A. (Example: l_1 (x)_pi Z for Z with alpha.)
KNOWN (confirmed snippet): Choi-Song (Math. Nachr. 2008): if X_1..X_{n-1} have property quasi-alpha and
X_n has property A, then X_1 (x)_pi ... (x)_pi X_n has property A. (Contains Prop. 13's consequence when
one factor has alpha.)
KNOWN (confirmed snippets): (X (x)_eps Z)* = X* (x)_pi Z* when X* or Z* has RNP and X* or Z* has the AP
(Ryan, Thm 5.33). Hence l_p (x)_pi l_q = (l_{p'} (x)_eps l_{q'})* (1<p,q<oo) is a separable dual, so it
has RNP and property A (Bourgain); moreover l_p (x)_pi l_q is reflexive iff 1/p + 1/q < 1 (Pitt's
theorem; e.g. Rueda Zoca arXiv 2409.20220 citing Ryan). Duals of injective tensor products of Asplund
spaces (with AP) have RNP (the injective tensor product of Asplund spaces is Asplund, attributed to
Ruess-Stegall 1982 -- partially confirmed snippet), hence property A. l_1 (x)_pi Z = l_1(Z): property A
iff Z has A (Theorem 1). For finite-dimensional Y only: Proposition 15 below gives P(c_0 (x)_pi c_0)
and P(c_0 (x)_pi l_p) (non-RNP examples).

### Proposition 14 (K(H) is lineable) -- PROVED
H a real Hilbert space, K(H) = H (x)_eps H, K(H)* = S_1(H) via <S,K> = tr(SK) (KNOWN). A trace-class S
attains its norm on K(H) iff S has finite rank. Proof: S = sum_n s_n <., e_n> f_n (Schmidt; s_n > 0,
orthonormal (e_n),(f_n)), ||S||_1 = sum s_n, tr(SK) = tr(KS) = sum_n s_n <K f_n, e_n> <= ||K|| sum s_n.
Equality with ||K|| <= 1 forces <K f_n, e_n> = 1, hence K f_n = e_n for all n. If S has infinite rank,
K maps the weakly null orthonormal sequence (f_n) to the orthonormal (e_n), so K is not compact. If S
has rank N, K := sum_{n<=N} <., f_n> e_n works. Finite-rank operators are dense in S_1(H), so NA(K(H),R)
is a dense linear subspace and P(K(H)) holds (1.4(c)). (Listed in the KLMW paper, confirmed snippet.)

## 8. Notions that DO fail -- different from plain NA on the tensor product (task item (2)(c))
Plain notion: T in L(X (x)_pi Z, Y) attains its norm at SOME u in the unit ball. For Y = R this is always
dense (Bishop-Phelps applied to the Banach space X (x)_pi Z). The following are DIFFERENT notions:
(F1) Norm-attaining bilinear forms = functionals on X (x)_pi Z attaining at an ELEMENTARY tensor:
NOT dense in general: Acosta-Aguirre-Paya, Israel J. Math. 93 (1996) (a Gowers-type space G, bilinear
forms on G x G; confirmed); Choi, J. Math. Anal. Appl. 211 (1997) (L_1[0,1] x L_1[0,1]; confirmed).
(F2) Operator vs bilinear: NA(L_1[0,1], L_oo[0,1]) is dense (Finet-Paya 1998; Paya-Saleh 2000 for
general measures; confirmed snippets) although bilinear forms on L_1 x L_1 = (L_1 (x)_pi L_1)* do not
attain densely (F1). Positive bilinear results: RNP => dense NA multilinear forms (Choi-Kim 1996;
FROM MEMORY), and Proposition 15 below.
(F3) Norm-attaining TENSORS (elements u of X (x)_pi Z whose projective norm is attained by a
representation): Dantas-Jung-Roldan-Rueda Zoca, Mediterr. J. Math. 19 (2022); Rueda Zoca, Mediterr.
J. Math. 2023 (examples where both NA tensors and their complement are dense); Garcia-Lirola,
Guerrero-Viu, Rueda Zoca (Banach J. Math. Anal. 2025); arXiv 2607.28054 (2026). A property of elements,
unrelated to density of operators. (Confirmed snippets.)
(F4) BPBp-type strengthenings under sums (ACKLM 2015, CDJM 2019): quantitative, not needed here.
None of (F1)-(F4) bears on density of plain NA(X (x)_pi Z, Y) for finite-dimensional Y, which by
Theorem 4 is exactly as hard as JW. FALSE statement to avoid: "NA(X (x)_pi Z, R) dense iff
norm-attaining bilinear forms on X x Z are dense" (the left side always holds; the right side fails
for G x G and L_1 x L_1).
(Check of the l_4^2 claim in 12(c), PROVED: if ||A|| <= 1, A e_1 = z = (z_1,z_2) in S_{l_4^2}, z_1 != 0,
then A* phi_z = e_1* (unique norming functionals), which forces A e_2 = (b,d) with b z_1^3 + d z_2^3 = 0,
and ||A(1,s)||_4^4 = 1 + 6 s^2 (z_1^2 b^2 + z_2^2 d^2) + O(s^3) <= 1 + s^4 forces b = 0 and, if z_2 != 0,
d = 0; so A = e_1* (x) z has rank one and ||A - I|| >= 1.)

## 9. Lineability through tensor products (task item (2)(d), tensor part)

### Proposition 15 -- PROVED
Let V (in X*) and W (in Z*) be linear subspaces with V in NA(X,R) and W in NA(Z,R). Identify
(X (x)_pi Z)* = L(X,Z*) = bilinear forms. Then:
(a) every u = sum_{k<=n} v_k (x) w_k in V (x) W (the operator A x = sum_k v_k(x) w_k) attains its norm at
an ELEMENTARY tensor x0 (x) z0 with x0 in S_X, z0 in S_Z; i.e. V (x) W consists of norm-attaining
bilinear forms, in particular of elements of NA(X (x)_pi Z, R);
(b) if V, W are dense, the norm closure of V (x) W is A(X,Z*) (norm closure of the finite-rank
operators). Hence: if V, W are dense and L(X,Z*) = A(X,Z*), then X (x)_pi Z satisfies the lineability
criterion, P(X (x)_pi Z) holds, and norm-attaining bilinear forms on X x Z are dense.
Proof. (a) A factors as X --Q--> R^n --M--> Z*, Qx = (v_k(x))_k, M(s) = sum s_k w_k. Let F := R^n/ker M
with the norm N([s]) := ||Ms|| and iota : F -> Z*, [s] -> Ms (isometric); S := q o Q : X -> F with q the
quotient map; A = iota o S, ||A|| = ||S||. For phi in F*, S* phi = sum_k c_k v_k (where phi o q (s) =
sum c_k s_k) lies in V. As F is finite-dimensional, pick phi0 in S_{F*} with ||S* phi0|| = ||S||;
S* phi0 is in V, so it attains its norm at some x0 in S_X, and ||S x0|| >= phi0(S x0) = ||S||. Then
||A x0|| = N(S x0) = ||A||, and A x0 = sum_k v_k(x0) w_k is in W, so it attains its norm at some z0 in
S_Z: (A x0)(z0) = ||A||. (b) x* (x) z* is the limit of v (x) w with v -> x*, w -> z*
(||x* (x) z* - v (x) w|| <= ||x* - v|| ||z*|| + ||v|| ||z* - w||), so the closure of V (x) W contains all
finite-rank operators; conversely V (x) W consists of finite-rank operators. QED
Examples (PROVED, using Pitt's theorem, KNOWN: every operator c_0 -> l_r (1 <= r < oo) and every operator
l_p -> l_r with r < p is compact; c_0, l_p have AP so compact = approximable): X = Z = c_0 (V = W = c_00
in l_1; L(c_0,l_1) = K = A): c_0 (x)_pi c_0 is lineable, so P(c_0 (x)_pi c_0) and NA bilinear forms on
c_0 x c_0 are dense; c_0 (x)_pi l_p (1<p<oo), l_p (x)_pi l_q with 1/p + 1/q < 1 (reflexive anyway).
Lineability also passes (Proposition 7) to X (x)_eps l_oo^n = l_oo^n(X), X (x)_eps c_0 = c_0(X) and to
C(K) (x)_eps X for scattered K. For general X (x)_eps Z, infinite l_1-sums, l_oo(X_i): OPEN here.

## 10. Literature log (searches of 2026-10-30; full texts not accessible; one WebFetch attempt to
mathdept.okstate.edu failed with DNS error, so no further hosts were tried)
Confirmed by search hit (abstract/snippet level):
- Choi, Dantas, Jung, Martin, The BPBp and absolute sums, Mediterr. J. Math. 16 (2019) 73, arXiv
  1806.09366 -- https://arxiv.org/pdf/1806.09366 ; https://oasis.postech.ac.kr/handle/2014.oak/100835
  (domain inheritance: type 1 or oo for BPBp; density analogues "also given"; one snippet: type 1).
- Aron, Choi, Kim, Lee, Martin, Trans. AMS 367 (2015) 6085-6101, arXiv 1305.6420 --
  https://arxiv.org/pdf/1305.6420 (c_0, l_1, l_oo sums; snippet: "Lindenstrauss property A is stable
  under arbitrary l_1-sums [12]" (Choi-Song) and "property B is stable under arbitrary c_0-sums [4]").
- Choi, Song, Property (quasi-alpha) and the denseness of norm attaining mappings, Math. Nachr. 2008 --
  https://oasis.postech.ac.kr/handle/2014.oak/22500 (projective tensor product theorem).
- Paya, Saleh, Arch. Math. 75 (2000) 380-388 -- https://link.springer.com/article/10.1007/s000130050519
- Acosta, Aguirre, Paya, Israel J. Math. 93 (1996) 221-227 -- https://www.doi.org/10.1007/BF02761104
- Choi, J. Math. Anal. Appl. 211 (1997) 295-300 -- https://remotecenter.postech.ac.kr/handle/2014.oak/20923
- Kadets, Lopez-Perez, Martin, Werner, Norm attaining operators of finite rank (2020), arXiv 1905.08272
  -- https://arxiv.org/pdf/1905.08272 ;
  https://www.ugr.es/~mmartins/Curriculum/Papers/pre2019_KadetsLopezMartinWerner-finiterank.pdf
  (c_0-sums of reflexive spaces; proximinal subspaces of c_0 and K(l_2)).
- Martin, The version for compact operators of Lindenstrauss properties A and B, RACSAM 2016 --
  https://arxiv.org/pdf/1502.07084 ; Martin's notes (c_0, C[0,1], L_1[0,1], C_0(L) fail A):
  https://www.ugr.es/local/mmartins/Curriculum/Papers/pre2014_Martin-norm-attaining_survey.pdf
- Johnson, Wolfe, Studia Math. 65 (1979) 7-19 -- https://eudml.org/doc/218261
- Dantas, Garcia, Maestre, Martin (BPBp for compact operators; L_1(mu,X) with X* RNP) --
  https://dcmpx.remotevs.com/org/arxiv/PL/pdf/1604.00618
- Dantas, Jung, Roldan, Rueda Zoca, Mediterr. J. Math. 19 (2022) -- https://arxiv.org/abs/2006.09871v3
- Rueda Zoca, Several remarks on norm attainment in tensor product spaces (2023) --
  https://arxiv.org/pdf/2209.02947 ; Garcia-Lirola, Guerrero-Viu, Rueda Zoca --
  https://arxiv.org/pdf/2407.10710 ; arXiv 2607.28054 -- https://arxiv.org/pdf/2607.28054
- (X (x)_eps Y)* = X* (x)_pi Y* under RNP+AP [Ryan Thm 5.33] -- snippet in https://arxiv.org/pdf/2407.10710
- Reflexivity of l_p (x)_pi l_q iff 1/p + 1/q < 1 -- https://arxiv.org/pdf/2409.20220
- Rmoutil (Read's space, no 2-dim subspaces in NA) -- https://arxiv.org/abs/1503.06112v1
FROM MEMORY (not confirmed): lifting theorem (Ionescu Tulcea book); L_1(mu,X)* = L_oo(mu,X*) iff X* has
RNP (Diestel-Uhl IV.1); Singer's representation of C(K,X)*; Schachermayer (alpha => A); Choi-Kim 1996
(RNP => NA multilinear dense); Ryan's identifications and their numbering; Pitt's theorem statement;
Ruess-Stegall (Asplund stability of (x)_eps).

## 11. Open questions isolated here
(Q1) (C_a): P(X_1), P(X_2) => P(X_1 (+)_oo X_2) (or (+)_p)? Implied by JW-positive; failure refutes JW.
(Q2) P(X) => P(L_1([0,1],X)) when X* lacks RNP (weak*-densities cannot be approximated by countably
valued ones).
(Q3) C(K,X) with K perfect: does NA(C(K,X),Y) dense imply NA(X,Y) dense? Does P(X) imply P(C(K,X)) for
non-reflexive X with X* RNP (this reduces to P(l_oo^m(X)), i.e. to (Q1))?
(Q4) P(l_oo(X_i)) for infinite families (e.g. l_oo(l_2)); lineability of l_1(X_i), l_oo(X_i) and of
general injective tensor products.
(Q5) (infinite-dimensional ranges) is property A stable under finite l_oo- or l_p-sums?

## 12. Referee addendum (2026-10-30; full report in sums_tensors_referee.md)
All items labelled PROVED above were re-derived by the referee and found correct; verdict
EQUIVALENT_TO_JOHNSON_WOLFE confirmed. Required literature corrections: (C1) "C_0(L) fails A" is known for
infinite METRIZABLE L; "l_oo = C(beta N) fails A" is unsupported, so the Sec 5.5 claim about infinite
l_oo-sums must be withdrawn or marked OPEN. (C2) KLMW: finite-codimensional proximinal subspaces.
(C3) RNP => dense NA multilinear forms: Aron-Finet-Werner 1995 (Choi-Kim 1996: polynomials). (C4) AAP 1996:
the space "G x G" is unconfirmed. Referee additions (proved in the report): C(K) is in
AAD = {X : AA(X,Y) dense for all finite-dim Y} for every compact K; AAD is stable under finite absolute
sums, c_0/l_p sums and C(K,.) for X* RNP (this upgrades Prop 12(b) to PROVED for reflexive X); P(X) <=>
P(X (+)_a Z) for Z in AAD; Read's space has P but is not in AAD, so Q1 stays open even for R (+)_oo R;
fixed-factor universality for Z with a one-dimensional L-summand (pi) or M-summand (eps), any Y; wedge
sums: F(M_1 v M_2) = F(M_1) (+)_1 F(M_2).
