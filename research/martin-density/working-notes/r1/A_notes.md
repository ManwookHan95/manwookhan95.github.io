# Notes A — Strategy (A): lower-limit reduction and certificate recovery for Martín norms

Research notes, strategy (A). Date: 2026-10-08.
Files read: `BRIEFING.md`, Preprint A (`residual_recovery.tex`), Preprint B (`hmr_c0_renormings.tex`).
Martín's paper (arXiv:2406.07273) could NOT be fetched (no network). Every statement below that depends on the
fine structure of Martín's operator T (approximation rates of the vectors u_{k,m}) is labelled conditional/HEURISTIC.

Status labels: **PROVED** (complete proof given here, modulo the explicitly listed imported facts),
**SKETCH** (all ideas present, some routine verifications omitted), **HEURISTIC** (plausibility argument only),
**FALSE** (disproved), **OPEN**.

---------------------------------------------------------------------------------------------------

## 0. Summary of results

| # | Statement (short) | Status | Section |
|---|---|---|---|
| 1 | (R1), (R2) of the briefing: reduction to pairs (f,g), g in C(f); C(f) is the dual ball of the convex envelope of r_f = sqrt(p^2-f^2) | PROVED | §2 |
| 2 | (R3) lower-limit theorem: if f_n -> f and liminf r~_{f_n} >= rho r~_f on a dense set, then rho C(f) is inside Li C(f_n); converse; finite/diagonal versions; mate version | PROVED | §3 |
| 3 | Transitivity of the recoverable set R | PROVED | §3 |
| 4 | Exact second-order formulas for base and block certificates, explicit radii | PROVED (+ numerical check) | §4.2 |
| 5 | Quantitative multi-scale ("NA-scale") criterion: a certificate c' at f' recovers rho g if p*(f'-f) <= (1-rho^2) r_*^2/6 and p*(g_{c'}-rho g) <= (1-rho^2) r_*/6 | PROVED | §4.3 |
| 6 | Transport Theorem: every finite-certificate mate (coefficient <= 1) is recovered, up to any rho<1, along EVERY sequence f_n -> f in S_{p*}; f -> cl Cert(f) is lower semicontinuous; re-proof of the [Check] local-certificate theorem (with base parts, several blocks, ranges l_2^d) | PROVED | §4.4 |
| 7 | Shifted certificates (quadratic shifts along w_m): transported along every sequence; the coefficient condition "H <= 1" of the [Check] theorem / Preprint A Thm 3.1 is NOT sharp (explicit relaxed thresholds) | PROVED | §4.5 |
| 8 | Primal reading of the multi-scale issue (exact identity; interpretation) | PROVED identity / HEURISTIC interpretation | §5 |
| 9 | Theorem W: weighted certificates (unbounded, near-peak block coefficients; flip-weighted base parts) lie in cl Cert(f). Strictly extends Preprint A, Thm 3.1 | PROVED | §6.2 |
| 10 | Theorem L: every mate admitting a locally admissible decomposition that is LINEAR in t lies in cl Cert(f); structure lemma (base part in supp a; block part omega - d w, omega = 0 on peaks, abs(omega(k)) <= sqrt(2 gap(k)) + K gap(k); H <= 1); monotone truncation of base parts | PROVED | §6.3 |
| 11 | **Averaging ("ladder") theorem**: if at all small scales t, g is a finite certificate of radius >~ t (bounded kappa, coefficient <= 1+o(1)) up to an O(t) remainder, then g is in cl Cert(f). Decomposition form (Cor. 6.9) needs this on ONE side only. Consequences: weighted directions with O(sigma) box tails; cross mates with scale-dense rates; Theorem L again | PROVED | §6.4 |
| 12 | Budget/excess identities; Rigidity Lemma (Y cap c_00 = {0}); at points with finite contact set (all NA points) one-sided linear decompositions on both sides coincide, so such mates are in cl Cert(f) | PROVED | §1.7, §7 |
| 13 | Necessary structure of defect mates: on BOTH sides and at arbitrarily small scales they carry >> t through one-sided resources (base contacts/near-contacts/near-flips, weak peaks), switching carriers | PROVED (as the contrapositive of item 11) / HEURISTIC (list of resources) | §6.4, §7.2 |
| 14 | Engineering lemmas: far modifications of z' are norm-small; far block coordinates can be zeroed; new contacts/new small support; limits: new structure carries mass <= (size of change)/(certificate radius) | PROVED | §8.1-8.4 |
| 15 | Domination lemma (C(lambda f + (1-lambda) h) contains lambda C(f) on the sphere) and rotundity of p*, which makes it useless | PROVED | §8 |
| 16 | Three-regime engineering scheme for one-sided-contact mates (tiny mass at contacts + transfer regime) | SKETCH, not completed | §8.7 |
| 17 | Direct transfer of the decompositions of f to an NA approximant at scales below sqrt(p*(f'-f)); pointwise domination | FALSE as general methods (explained) | §9 |
| 18 | Every mate lies in cl Cert(f) (would give density and Hausdorff continuity of C everywhere) | OPEN; conjectured under a scale-separation property of T (HEURISTIC) | §7.5, §10 |
| 19 | Density of NA((c_0,p), l_2^2) | OPEN (reduced to item 18, or to recovering the defect C(f) \ cl Cert(f) along some NA sequence) | §4.4, §10 |

**Bottom line.** The lower-limit reduction (R3) is correct. All known recoverable mate classes (R6), and much larger ones
(shifted certificates; Theorems W and L; and above all the averaging Theorem 6.8: "certificate of radius >~ t up to an O(t)
remainder at every small scale, on one side"), lie in the closed convex set cl Cert^sh(f), and f -> cl Cert^sh(f) is lower
semicontinuous on the whole sphere: these mates are recovered along *every* approximating sequence (NA or not); no engineering
is needed for them and there is no multi-scale problem for them. The coefficient condition of the [Check] theorem is not sharp
(§4.5). Consequently the density problem reduces to the "defect" C(f) \ cl Cert^sh(f). A defect mate must, on BOTH sides of
t = 0 and at arbitrarily small scales, carry a part of size >> t through one-sided resources (base contacts, near-contacts or
near-flip coordinates; weak peaks of the block functionals), switching between different carriers that represent the same
component of g up to O(t): an approximate linear relation, at their own scale, among base vectors and block vectors. Whether
Martín's T permits this is the remaining question; I conjecture (HEURISTIC) that it does not under a natural scale-separation
property of T. Engineering through finite certificates alone gives only O(sqrt(eps)) of new structure (Proposition 8.4); a
three-regime scheme is described but not completed. Density remains OPEN.

---------------------------------------------------------------------------------------------------

## 1. Setting, notation, standing facts

### 1.1 Spaces and norms
All spaces real. X = c_0, X* = l_1, X** = l_infinity.

* Base: q*(a) = ||a||_1 + ||U* a||_H, B_q = B_{c_0} + U(B_H), where U: H -> c_0 is compact with dense range, so U*: l_1 -> H
  is injective and compact. B_{q**} = B_{l_infinity} + U(B_H).
* Blocks: for m in I, Phi_m(k) = 2^{-m-k} q*(T e_{k,m}) <= 2^{-m-k}, lambda_{k,m} := m Phi_m(k), u_{k,m} = T e_{k,m}/q*(T e_{k,m}) in S_{q*},
  (R_m x)(k) = lambda_{k,m} u_{k,m}(x). V_m = (l_1, |.|_m), B_{|.|_m} = B_{l_1} + D_m(B_{l_2}), dual norm
  N_m(w) = ||w||_infinity + ||D_m w||_2, with (D_m w)(k) = Phi_m(k) w(k). R_m* w = sum_k lambda_{k,m} w(k) u_{k,m}.
* V = (sum_{m in I} V_m)_{l_1}, V* = (sum_m (l_infinity, N_m))_{l_infinity}, ||W||_{V*} = sup_m N_m(W_m).
  L x = (R_m x)_m, p = q + ||L .||_V, s(t) := sqrt(1+t^2).

Imported facts (used as black boxes, all stated in Preprint B or the briefing):
* (T1) T: l_1(N x N) -> Y is injective, ||T|| = 1, Y cap c_00 = {0}, and R_m* w = T( sum_{k} w(k) m 2^{-m-k} e_{k,m} ) (Preprint B, (M2), (M6)).
  In particular L*: V* -> X* is injective.
* (T2) Every tail of (u_{k,m})_k is norm dense in S_{q*} (Preprint B).
* (T3) R_m** is injective (Preprint B, §6.1), and (R_m** xi)(k) = lambda_{k,m} xi(u_{k,m}); R_m**(X**) is contained in l_1.
* (T4) p** is strictly convex (Preprint B, Thm "finite-blocks"(b) for finite I; [Recovery] for I = N, not available).
  Consequently every f in S_{p*} has a unique normer xi_f in S_{p**}.

Elementary facts used repeatedly:
* D_m: l_infinity -> l_2 is compact (Phi_m in l_2); hence weak*-convergent bounded sequences w_n -> w satisfy
  ||D_m(w_n - w)||_2 -> 0, and also ||D_m^2 (w_n - w)||_1 -> 0 (dominated convergence, Phi_m^2 summable).
* N_m is strictly convex (sum of a norm and the strictly convex norm ||D_m .||_2, D_m injective); hence |.|_m is
  Gateaux smooth and its norming map J_m is single valued on V_m \ {0} and norm-to-weak* continuous there (Smulian).
* q* is strictly convex (||U* .|| is strictly convex since U* is injective), so q is Gateaux smooth.

### 1.2 Fact A (dual ball formula). PROVED.
B_{p*} = B_{q*} + L*(B_{V*}), and for every h in X*:
  p*(h) = min { max(q*(A), ||W||_{V*}) : A + L* W = h } (the minimum is attained).

*Proof.* If q*(A) <= 1 and ||W|| <= 1 then (A + L*W)(x) <= q(x) + ||Lx|| = p(x), so the right side is inside B_{p*}.
The set B_{q*} + L*(B_{V*}) is convex, symmetric and weak*-compact (sum of two weak*-compact sets; L* is
weak*-weak* continuous). Its support function at x in X is sup_A A(x) + sup_W W(Lx) = q(x) + ||Lx|| = p(x),
which is also the support function of B_{p*}. Two weak*-closed convex sets with the same support function on X
coincide (Hahn-Banach in (X*, weak*)). For h != 0, h/p*(h) is in B_{p*}, giving a decomposition with
max(q*(A), ||W||) <= p*(h); any decomposition gives the reverse inequality. QED.

### 1.3 Fact B (forced decomposition). PROVED (given T3, T4).
Let f in S_{p*}, xi = xi_f, q_0 := q**(xi) > 0. Then L**xi lies in V, ||L**xi||_V = 1 - q_0 > 0, every R_m** xi != 0,
and the decomposition f = a + L*w with q*(a) <= 1, ||w|| <= 1 is unique and satisfies
  q*(a) = 1, a(xi) = q_0, w_m = J_m(R_m** xi) (so N_m(w_m) = 1 for every m).
The base contact is xi/q_0 = z + U e with e := U*a/nu, nu := ||U*a||_H > 0, z in B_{l_infinity}, z_j = sign a_j on supp a.
Write zhat := xi/q_0 = z + U e; then a(zhat) = 1 and for b in l_1: b(zhat) = b(z) + <U*b, e>.

*Proof.* p**(xi) = q**(xi) + ||L**xi|| (Preprint A, §1). For any admissible decomposition,
1 = f(xi) = a(xi) + <w, L**xi> <= q_0 + sum_m |R_m** xi|_m = 1, so all inequalities are equalities:
a(xi) = q_0 (hence q*(a) >= 1, so q*(a) = 1) and <w_m, R_m**xi> = |R_m**xi|_m for each m, which forces
N_m(w_m) = 1 and w_m = J_m(R_m**xi) (smoothness, R_m**xi != 0 by T3). Then a = f - L*w is unique.
For the contact: xi/q_0 is in B_{q**} = B_{l_infinity} + U(B_H), so xi/q_0 = z + U h with ||z||_infinity <= 1, ||h|| <= 1, and
1 = a(xi/q_0) = a(z) + <U*a, h> <= ||a||_1 + ||U*a|| = 1 forces a(z) = ||a||_1 (so z_j = sign a_j on supp a) and h = e. QED.

### 1.4 Fact C (block threshold; Preprint B, Lemma block-threshold). PROVED.
Fix m, write zeta := R_m** xi, w := w_m, M := ||w||_infinity, C := ||D_m w||_2, Phi := Phi_m. Then M > 0, C > 0, M + C = 1, and
  zeta/|zeta|_m = alpha + D^2 w / C,   alpha in l_1, ||alpha||_1 = 1, alpha supported on the peak set P := {k : |w(k)| = M},
  with sign alpha(k) = sign w(k).
Hence P is nonempty; off P, w(k) = C zeta(k)/(Phi(k)^2 |zeta|_m) = C m u_{k,m}(xi)/(Phi(k) |zeta|_m); and
k is in P iff m |u_{k,m}(xi)| >= Phi(k) M |zeta|_m / C. We write gap(k) := M - |w(k)| and sigma_k := sign w(k).

*Proof.* B_{|.|} = B_{l_1} + D(B_{l_2}) is closed (closed + compact), so zeta/|zeta| = alpha + D beta with ||alpha||_1 <= 1,
||beta||_2 <= 1. Then 1 = <w, alpha> + <Dw, beta> <= M ||alpha||_1 + C ||beta|| <= M + C = 1. Equality forces
<w,alpha> = M = M ||alpha||_1 (so ||alpha||_1 = 1 since M > 0, and alpha lives on P with matching signs) and beta = Dw/C.
(M > 0 and C > 0 because w != 0 and D is injective.) QED.

Remark 1.4.1. Since Phi(k) -> 0, a far coordinate k is a peak unless |u_{k,m}(xi)| is of order Phi(k) or smaller.
So peak sets are typically infinite (often cofinite), and off-peak coordinates are those where u_{k,m}(xi) is
exceptionally small. For far peaks alpha(k) is approximately lambda_{k,m}|u_{k,m}(xi)|/|zeta|, tiny.

### 1.5 Fact D (norm-attaining functionals, R4). PROVED.
f' in NA cap S_{p*} iff f' = grad p(x') for some x' in S_p; then a' := grad q(x') lies in c_00, w' = J_V(Lx'), and
x'/q(x') = z' + U e' with z' in B_{c_0}, z' = sign a' on supp a'. Conversely, given a' in c_00 with q*(a') = 1 and any
z' in c_0 with ||z'||_infinity <= 1 and z' = sign a' on supp a', the vector x' := z' + U(U*a'/||U*a'||) satisfies q(x') = 1 = a'(x')
and grad p(x') = a' + L* J_V(L x') is norm attaining (at x'/p(x')).

*Proof.* p is Gateaux smooth (q smooth; ||L.|| smooth off 0 because each R_m x != 0 for x != 0 and each |.|_m is smooth),
so the norming functional of x' in S_p is grad p(x') = grad q(x') + L*J_V(Lx'). If a = grad q(x') then
x'/q(x') = y + U h with y in B_{c_0}, ||h|| <= 1 and a(y) = ||a||_1, h = U*a/||U*a||; as y is in c_0, |y_j| = 1 only for finitely
many j, so supp a is finite. Conversely a'(x') = a'(z') + ||U*a'|| = 1 >= q(x') >= a'(x')/q*(a') = 1. QED.

### 1.6 Fact E (convergence of the forced data). PROVED (given T3, T4).
Let f_n -> f in S_{p*} (arbitrary, NA or not), with normers xi_n, forced data (a_n, w_n, z_n, e_n, ...). Then
(i) xi_n -> xi weak*; (ii) R_m**xi_n -> R_m**xi in l_1 for each m; (iii) w_{n,m} -> w_m weak* (coordinatewise, bounded);
(iv) L*w_n -> L*w and a_n -> a in norm; e_n -> e in H; (v) C_{n,m} -> C_m, M_{n,m} -> M_m, D_m w_{n,m} -> D_m w_m in l_2;
(vi) alpha_{n,m} -> alpha_m in l_1; (vii) q**(xi_n) -> q_0 and z_n -> z weak*.

*Proof.* (i) Any weak* cluster point xi' of (xi_n) satisfies p**(xi') <= 1 and f(xi') = lim f_n(xi_n) = 1, so xi' = xi by T4.
(ii) R_m is compact, so R_m** maps bounded weak*-convergent sequences to norm-convergent ones. (iii) Any weak*
cluster point w' of (w_{n,m})_n has N_m(w') <= 1 and <w', R_m**xi> = lim |R_m**xi_n| = |R_m**xi| (norm x bounded weak*),
so w' = J_m(R_m**xi) = w_m. (iv) L* is weak*-to-norm continuous on bounded sets (adjoint of a compact operator),
and a_n = f_n - L*w_n. (v) compactness of D_m and C + M = 1. (vi) alpha = zeta/|zeta| - D^2 w/C with both terms converging in l_1.
(vii) q**(xi_n) = a_n(xi_n) -> a(xi) = q_0 (norm x weak*), and z_n = xi_n/q**(xi_n) - U e_n. QED.

### 1.7 Fact F (consequences of Y cap c_00 = {0}). PROVED (given T1).
(a) (Rigidity) If b+ + L*W+ = b- + L*W- with b+ - b- in c_00 and W+, W- in V* (bounded), then b+ = b- and W+ = W-.
(b) (Tail independence) For finitely many distinct pairs (k_i, m_i) and every N, the restrictions of u_{k_i,m_i} to the
coordinates [N, infinity) are linearly independent.

*Proof.* (a) b+ - b- = L*(W- - W+) = T(c) with absolutely summable coefficients c_{k,m} = m 2^{-m-k}(W- - W+)_m(k), so it lies in
Y cap c_00 = {0}; injectivity of T and of the coefficient map gives W- = W+. (b) If sum_i c_i u_{k_i,m_i} vanishes on [N, infinity),
then this combination lies in Y cap c_00 = {0}, so all c_i = 0 by injectivity of T. QED.

---------------------------------------------------------------------------------------------------

## 2. (R1) and (R2): verification. PROVED.

**Proposition 2.1 (R1).** Let S: X -> l_2^2 with ||S|| = 1. Then there is a rotation Q of l_2^2 such that QS = (f, g)
with f in S_{p*} and g in C(f) := {g : p*(f + t g) <= s(t) for all t}. Moreover, for f in S_{p*} and g in X*,
(f, g) is contractive iff g is in C(f) iff |g(y)| <= r_f(y) := sqrt(p(y)^2 - f(y)^2) for all y in X.
NA((X,p), l_2^2) is dense iff for all f in S_{p*}, g in C(f), rho in (0,1): (f, rho g) is in cl NA.
For rho < 1 and t != 0: p*(f + t rho g) <= s(rho t) < s(t) (slack s(t) - s(rho t)).

*Proof.* S* attains its norm on the compact sphere of l_2^2 at some unit vector; rotate it to e_1, so f := S*e_1 has
p*(f) = 1. ||(f,g)|| <= 1 iff sup_theta p*(cos theta f + sin theta g) <= 1 iff p*(f + t g) <= s(t) for all t (the case
theta = pi/2 is the limit t -> infinity). Also ||(f,g)||^2 = sup_{p(y) <= 1} f(y)^2 + g(y)^2, giving the primal form. NA is
a cone and (f,g) = lim_{rho -> 1}(f, rho g). The slack is s(rho t) < s(t). QED.

**Proposition 2.2 (R2).** For f in S_{p*}, let r~_f be the largest seminorm below r_f. Then
r~_f(x) = inf { sum_j r_f(y_j) : finite families with sum_j y_j = x }, C(f) = {g in X* : g <= r~_f on X}, C(f) is
convex, symmetric and weak*-compact, and its support function on X is r~_f: max_{g in C(f)} g(x) = r~_f(x).

*Proof.* phi(x) := inf{sum_j r_f(y_j) : sum y_j = x} is subadditive, positively homogeneous, even, nonnegative, and
phi <= r_f; every sublinear minorant s of r_f satisfies s(x) <= sum s(y_j) <= sum r_f(y_j), so s <= phi. Hence phi = r~_f.
A linear g satisfies g <= r_f iff g <= r~_f (r~_f is the largest sublinear minorant), and since r_f is even this is
|g| <= r_f, i.e. g in C(f). Given x, Hahn-Banach gives a linear g <= r~_f with g(x) = r~_f(x); |g| <= r~_f <= p makes g
continuous, so g is in C(f). QED.

Remark 2.3. Every g in C(f) satisfies p*(g) <= 1 and g(xi) = 0 ((f + t g)(xi) = 1 + t g(xi) <= s(t) for all t).

---------------------------------------------------------------------------------------------------

## 3. (R3): the lower-limit reduction, finite versions, transitivity. PROVED.

### 3.1 Global compactness (Preprint A, Thm 2.1) — re-verified
**Theorem 3.1.** If f_n -> f in S_{p*} and g_n in C(f_n), then (g_n) has a norm-convergent subsequence and every limit
lies in C(f). Hence every C(f) is norm compact, f -> C(f) is upper semicontinuous, and for every convergent sequence
f_n -> f the set Q := C(f) cup (union_n C(f_n)) is norm compact.

*Proof (verification of Preprint A's argument).* p*(g_n) <= 1; pass to a weak*-convergent subsequence g_n -> g. Weak*
lower semicontinuity of p* gives p*(f + t g) <= liminf p*(f_n + t g_n) <= s(t), so g in C(f), and g(xi) = 0. Let
D := limsup ||g_n - g||_1, realized along a further subsequence. Fix t > 0, s = s(t). By Fact A,
f_n + t g_n = A_n + L*W_n with q*(A_n) <= s, ||W_n|| <= s. Pass to a subsequence with L*W_n -> k in norm (L* compact)
and A_n -> A := f + t g - k weak*. Then k(xi) = <W, L**xi> <= s(1 - q_0) for a weak* limit W, so
A(xi) >= 1 - s(1-q_0), and q*(A) >= A(xi)/q_0. U*A_n -> U*A in norm (U* compact), and for bounded coordinatewise
convergent sequences in l_1, ||A_n||_1 - ||A_n - A||_1 -> ||A||_1. Hence
t D = limsup ||A_n - A||_1 = limsup (q*(A_n) - q*(A)) <= s - (1 - s(1-q_0))/q_0 = (s-1)/q_0.
So D <= (sqrt(1+t^2) - 1)/(t q_0) -> 0 as t -> 0. Thus g_n -> g in norm. For Q: a sequence in Q either has
infinitely many terms in one of the compact sets C(f_n), C(f), or a subsequence g_j in C(f_{n_j}) with n_j -> infinity,
to which the first part applies. QED.

(The residual-recovery Theorem 2.2 of Preprint A was also checked: x -> dist(z, C_d(x)) is lower semicontinuous by
Theorem 3.1, the continuity points of countably many lsc functions form a dense G_delta, and at such points the fibre is
Hausdorff continuous. Correct as written.)

### 3.2 The lower-limit theorem
For sets C_n in X*, Li_n C_n := {g : dist(g, C_n) -> 0}. If the C_n are convex then Li_n C_n is closed and convex.

**Theorem 3.2 (R3).** Let f_n -> f in S_{p*} (not necessarily NA) and rho in [0,1]. The following are equivalent:
 (i) rho C(f) is contained in Li_n C(f_n);
 (ii) liminf_n r~_{f_n}(x) >= rho r~_f(x) for every x in X;
 (iii) (ii) holds for all x in some dense subset of X.

*Proof.* (i) => (ii): choose g in C(f) with g(x) = r~_f(x) (Prop. 2.2) and g_n in C(f_n), g_n -> rho g; then
r~_{f_n}(x) >= g_n(x) -> rho r~_f(x).
(ii) <=> (iii): every r~_h is a seminorm with r~_h <= r_h <= p, so |r~_h(x) - r~_h(y)| <= p(x - y) uniformly in h.
(ii) => (i): suppose g in rho C(f) but dist(g, C(f_{n_j})) >= delta > 0 along a subsequence. All C(f_{n_j}) lie in the compact
set Q of Theorem 3.1. By Blaschke's selection theorem (the hyperspace of nonempty compact subsets of a compact metric
space is compact for the Hausdorff metric) we may assume C(f_{n_j}) -> A in the Hausdorff metric. A is compact, convex
(limits of midpoints) and dist(g, A) >= delta. For x in X, |h_C(x) - h_{C'}(x)| <= d_H(C, C')||x||_infinity, so
h_A(x) = lim_j r~_{f_{n_j}}(x) >= rho r~_f(x) = h_{rho C(f)}(x) >= g(x). A is norm compact, hence weak*-compact; if g were
not in A, Hahn-Banach separation in (l_1, weak*) (dual c_0) would give x in c_0 with g(x) > h_A(x). Contradiction. QED.

**Corollary 3.3 (finite/diagonal versions).** For f in S_{p*} the following are equivalent:
 (a) there is a sequence f_n in NA cap S_{p*} with f_n -> f and C(f) contained in Li_n C(f_n);
 (b) for every eps > 0, rho < 1 and x_1,...,x_k in X there is f' in NA cap S_{p*} with p*(f' - f) < eps and
     r~_{f'}(x_i) >= rho r~_f(x_i) - eps for i <= k;
 (c) for every eps > 0, rho < 1 and g_1,...,g_k in C(f) there is f' in NA cap S_{p*} with p*(f' - f) < eps and
     dist(rho g_i, C(f')) < eps for i <= k (finitely many mates recovered along a COMMON first row);
 (d) as (c) but uniformly: sup_{g in C(f)} dist(rho g, C(f')) < eps.
If they hold, then (f, g) is in cl NA((X,p), l_2^2) for every g in C(f).

*Proof.* (a) => (d): by (a), for each g in C(f), dist(g, C(f_n)) -> 0; by compactness of C(f) (finite eps/3-nets and
1-Lipschitz dependence on g) the convergence is uniform in g. Since C(f_n) is convex and contains 0, rho C(f_n) is
contained in C(f_n), so dist(rho g, C(f_n)) <= rho dist(g, C(f_n)); take f' = f_n with n large.
(d) => (c) trivial. (c) => (b): pick g_i in C(f) with g_i(x_i) = r~_f(x_i); if g'_i in C(f') with ||g'_i - rho g_i|| < eps then
r~_{f'}(x_i) >= g'_i(x_i) >= rho r~_f(x_i) - eps ||x_i||. (b) => (a): let (x_i) be dense; apply (b) with eps = 1/n,
rho = 1 - 1/n and x_1..x_n to get f_n; then liminf_n r~_{f_n}(x_i) >= r~_f(x_i) for every i, and Theorem 3.2 (iii)=>(i) with rho = 1 gives (a).
Final claim: if g_n in C(f_n) -> g and f_n attains at x_n in S_p, then g_n(x_n) = 0 (from f_n(x_n)^2 + g_n(x_n)^2 <= 1), so
(f_n, g_n) is norm attaining at x_n, and (f_n, g_n) -> (f, g). QED.

Remark 3.4. Necessity. If NA((X,p), l_2^{k+1}) is dense then (c) holds with g_i replaced by g_i/sqrt(k) only (the tuple
(g_1,...,g_k)/sqrt(k) lies in the joint fibre C_k(f)); I do not know whether density into l_2^2 alone implies (a).
Only sufficiency is needed.

### 3.3 Transitivity of the recoverable set
Let R := {f in S_{p*} : (f, g) in cl NA for every g in C(f)}. Then NA cap S_{p*} is in R (KLMW: a mate of an attaining f
vanishes at its normer) and Preprint A's residual set Omega is in R.

**Theorem 3.5 (transitivity).** Let f in S_{p*}. Suppose that for every rho < 1 there is a sequence f_n^rho in R with
f_n^rho -> f and liminf_n r~_{f_n^rho}(x) >= rho r~_f(x) for all x in a dense subset of X. Then f is in R.

*Proof.* By Theorem 3.2, rho C(f) is contained in Li_n C(f_n^rho). Given g in C(f) choose g_n in C(f_n^rho) with g_n -> rho g.
Each (f_n^rho, g_n) is in cl NA, hence so is the limit (f, rho g); let rho -> 1. QED.

The joint version (ranges l_2^{d+1}, joint fibres C_d(f), support functions on X^d) holds verbatim: C_d(f) is compact
(rows in C(f)), Blaschke selection in (l_1)^d, separation with (c_0)^d.

---------------------------------------------------------------------------------------------------

## 4. Finite certificates, the NA-scale criterion, and the Transport Theorem

Throughout this section f is in S_{p*} with forced data (xi, q_0, a, w, z, e, nu, zhat = z + U e) and, for each block m,
(zeta_m, M_m, C_m, P_m, alpha_m, gap_m(k) = M_m - |w_m(k)|). Block indices are suppressed when only one block is involved.

### 4.1 Definitions
**Definition 4.1.** A *finite certificate* at f is c = (b, omega), omega = (omega_m)_{m in I}, such that
* (C1) b is in l_1, supp b is contained in supp a, ||b/a||_infinity := sup_{j in supp a} |b_j|/|a_j| < infinity, and b(zhat) = 0
  (equivalently b(xi) = 0);
* (C2) each omega_m is in c_00 with supp omega_m disjoint from P_m, and omega_m = 0 for all but finitely many m.

Associated quantities:
* d_m := <D_m w_m, D_m omega_m>/C_m, and the *direction* g_c := b + sum_m R_m*(omega_m - d_m w_m);
* base coefficient h(b) := (||U*b||^2 - <U*b, e>^2)/nu = ||P_{e-perp} U*b||^2/nu, beta := ||U*b||;
* block coefficient H_m(omega_m) := (||D_m omega_m||^2 - d_m^2)/C_m = ||P_m-perp D_m omega_m||^2 / C_m (P_m-perp = orthogonal
  projection onto (D_m w_m)-perp);
* H(c) := max(h(b), max_m H_m(omega_m));
* gap_m(omega_m) := min_{k in supp omega_m} gap_m(k) > 0;
* radius r(c) := min{ 1/||b/a||_infinity, nu/(2 beta), min over m with omega_m != 0 of
  min( gap_m(omega_m)/(2||omega_m||_infinity), 1/(2|d_m|), C_m/(2|d_m| M_m) ) } (with 1/0 = infinity);
* kappa(c) := max{ 2 beta/nu, max_m 2|d_m| M_m / C_m }.

**Cert(f)** := { g_c : c finite certificate at f, H(c) <= 1, g_c in C(f) }.

**Lemma 4.2 (algebra). PROVED.** Finite certificates form a vector space; c -> g_c is linear; H is the maximum of
finitely many positive semidefinite quadratic forms, so H(lambda c) = lambda^2 H(c) and H is convex; r(lambda c) = r(c)/|lambda|,
kappa(lambda c) = |lambda| kappa(c). Every g_c satisfies g_c(xi) = 0. Cert(f) is convex and symmetric.

*Proof.* d_m is linear in omega_m. For the identity g_c(xi) = 0: b(xi) = q_0 b(zhat) = 0, and by Fact C
<omega_m - d_m w_m, zeta_m> = |zeta_m| ( <omega_m, alpha_m> + <omega_m, D^2 w_m>/C_m - d_m(<w_m, alpha_m> + <w_m, D^2 w_m>/C_m) )
= |zeta_m| (0 + d_m - d_m (M_m + C_m)) = 0, because alpha_m lives on P_m and supp omega_m misses P_m. Convexity of Cert(f)
follows from linearity, convexity of H and of C(f). QED.

### 4.2 Exact expansions
**Lemma 4.3 (base expansion). PROVED (numerically checked, Appendix).** Let b in l_1 with supp b contained in supp a.
For every real sigma,
  q*(a + sigma b) = 1 + sigma b(zhat) + Fl_b(sigma) + nu Psi(sigma U*b/nu),
where Fl_b(sigma) := sum_{j in supp a} 2 ( -sign(a_j) sigma b_j - |a_j| )_+ >= 0 (the "sign-flip cost", zero for
|sigma| <= 1/||b/a||_infinity), and Psi(h) := ||e + h|| - 1 - <e, h> = ||h_perp||^2 / ( ||e + h|| + 1 + <e,h> ), h_perp := h - <e,h> e.
For ||h|| <= 1/2: ||h_perp||^2/(2(1+||h||)) <= Psi(h) <= ||h_perp||^2/(2(1-||h||)). Consequently, if b(zhat) = 0 and
|sigma| <= min(1/||b/a||_infinity, nu/(2 beta)):
  (sigma^2/2) h(b)/(1 + |sigma| beta/nu) <= q*(a + sigma b) - 1 <= (sigma^2/2) h(b)/(1 - |sigma| beta/nu) <= (sigma^2/2) h(b)(1 + 2|sigma| beta/nu).
Moreover, for c, c' in l_1 with |sigma| ||U|| max(||c||_1, ||c'||_1) <= nu/2:
  | nu Psi(sigma U*c/nu) - nu Psi(sigma U*c'/nu) | <= (4 sigma^2 ||U||^2/nu) max(||c||_1, ||c'||_1) ||c - c'||_1.

*Proof.* For real x != 0 and y: |x + y| = |x| + sign(x) y + 2(-sign(x) y - |x|)_+. Summing over j in supp a (b vanishes
elsewhere): ||a + sigma b||_1 = ||a||_1 + sigma b(z) + Fl_b(sigma), since z_j = sign a_j on supp a. Next
||U*a + sigma U*b|| = nu ||e + h|| with h = sigma U*b/nu, and ||e+h|| = 1 + <e,h> + Psi(h), nu <e,h> = sigma <U*b, e>. Adding and
using ||a||_1 + nu = 1 and b(z) + <U*b, e> = b(zhat) gives the identity. The formula for Psi follows from
||e+h||^2 - (1 + <e,h>)^2 = ||h||^2 - <e,h>^2; for ||h|| <= 1/2 the denominator lies in [2(1 - ||h||), 2(1 + ||h||)].
With h = sigma U*b/nu: nu ||h_perp||^2 = sigma^2 h(b) and ||h|| = |sigma| beta/nu; 1/(1-x) <= 1 + 2x for x <= 1/2.
Lipschitz bound: grad Psi(h) = (e+h)/||e+h|| - e has norm <= 2||h||/||e+h|| <= 4||h|| on the ball of radius 1/2;
apply the mean value theorem on the segment. QED.

**Lemma 4.4 (block expansion). PROVED (numerically checked).** Fix a block; let omega: N -> R vanish on P with
D omega in l_2; d := <Dw, D omega>/C; h_perp := D omega - (d/C) Dw, so ||h_perp||^2 = ||D omega||^2 - d^2 = C H(omega).
For W(sigma) := (1 - d sigma) w + sigma omega and Y := C + d sigma M:
 (a) ||D W(sigma)||_2 = sqrt(Y^2 + sigma^2 ||h_perp||^2) for all sigma;
 (b) if 1 - d sigma >= 0 then ||W(sigma)||_infinity >= (1 - d sigma) M and hence, when Y > 0,
     N(W(sigma)) >= 1 + sigma^2 ||h_perp||^2 / ( sqrt(Y^2 + sigma^2 ||h_perp||^2) + Y );
 (c) if |d sigma| <= 1/2 and |sigma omega(k)| <= gap(k)/2 for every k with omega(k) != 0, then
     ||W(sigma)||_infinity = (1 - d sigma) M and equality holds in (b);
 (d) for omega in c_00 and |sigma| <= r_m := min( gap(omega)/(2||omega||_infinity), 1/(2|d|), C/(2|d|M) ):
     N(W(sigma)) <= 1 + (sigma^2/2) H(omega) (1 + 2|d sigma| M/C).

*Proof.* (1 - d sigma) Dw + sigma D omega = (1 - d sigma + sigma d/C) Dw + sigma h_perp = (1 + d sigma M/C) Dw + sigma h_perp,
using 1/C - 1 = M/C; orthogonality gives (a). (b): at a peak k, |W(sigma)(k)| = (1 - d sigma) M; then
N(W) >= (1 - d sigma) M + sqrt(Y^2 + sigma^2||h_perp||^2) = 1 + [sqrt(Y^2 + sigma^2 ||h_perp||^2) - Y], as (1 - d sigma) M + Y = M + C = 1.
(c): for k outside supp omega, |W(k)| = (1 - d sigma)|w(k)| <= (1 - d sigma) M; for k in supp omega,
|W(k)| <= (1 - d sigma)|w(k)| + gap(k)/2 = (1 - d sigma) M - (1 - d sigma) gap(k) + gap(k)/2 <= (1 - d sigma) M.
(d): the bracket in (b) is at most sigma^2 ||h_perp||^2/(2Y), and C/Y <= 1/(1 - |d sigma| M/C) <= 1 + 2|d sigma| M/C. QED.

**Proposition 4.5 (certificate expansion). PROVED.** For a finite certificate c at f and |sigma| <= r(c):
  p*(f + sigma g_c) <= 1 + (sigma^2/2) H(c) (1 + kappa(c) |sigma|).
*Proof.* f + sigma g_c = (a + sigma b) + sum_m R_m* W_m(sigma) with W_m(sigma) = (1 - d_m sigma) w_m + sigma omega_m
(= w_m when omega_m = 0). Apply Fact A, Lemma 4.3 (no flips for |sigma| <= 1/||b/a||) and Lemma 4.4(d). QED.

**Lemma 4.6 (validity window). PROVED.** If H(c) <= 1 - delta with 0 < delta <= 1 and
|sigma| <= r_*(c, delta) := min( r(c), delta/(2 kappa(c) + 2), sqrt(delta) ), then p*(f + sigma g_c) <= s(sigma).
*Proof.* (1 - delta)(1 + kappa|sigma|) <= (1 - delta)(1 + delta/2) <= 1 - delta/2; and
1 + (sigma^2/2)(1 - delta/2) <= 1 + sigma^2/2 - sigma^4/8 <= s(sigma) because sigma^2 <= delta gives sigma^4/8 <= sigma^2 delta/4,
and sqrt(1 + x) >= 1 + x/2 - x^2/8 for x >= 0. QED.

### 4.3 The NA-scale criterion (quantitative multi-scale lemma)
**Lemma 4.7 (slack).** For rho in (0,1) and real t: s(t) - s(rho t) >= (1 - rho^2) min(t^2, |t|)/3.
*Proof.* s(t) - s(rho t) = (1 - rho^2) t^2/(s(t) + s(rho t)) >= (1 - rho^2) t^2/(2 s(t)); and 2 s(t) <= 2 sqrt(2) < 3 for |t| <= 1,
2 s(t) <= 2 sqrt(2) |t| < 3|t| for |t| >= 1. QED.

**Proposition 4.8 (NA-scale criterion). PROVED.** Let f, f' in S_{p*}, g in C(f), rho in (0,1), and let c' be a finite
certificate AT f' with H(c') <= 1 - delta (0 < delta <= 1). Put r_* := r_*(c', delta) (<= 1), eps := p*(f' - f),
eta := p*(g_{c'} - rho g). If
  eps <= (1 - rho^2) r_*^2 / 6   and   eta <= (1 - rho^2) r_* / 6,
then g_{c'} lies in C(f'), hence in Cert(f'), and dist_{p*}(rho g, C(f')) <= eta.

*Proof.* For |t| <= r_*: Lemma 4.6 at f'. For |t| >= r_*:
p*(f' + t g_{c'}) <= p*(f + t rho g) + eps + |t| eta <= s(rho t) + eps + |t| eta, and by Lemma 4.7 it suffices that
eps + |t| eta <= (1 - rho^2) min(t^2, |t|)/3. For r_* <= |t| <= 1 we have eps <= (1-rho^2) t^2/6 and |t| eta <= (1-rho^2) t^2/6;
for |t| >= 1, eps + |t| eta <= (1 - rho^2)(1 + |t|)/6 <= (1 - rho^2)|t|/3. QED.

Remark 4.9 (the multi-scale issue, quantified). With eps = ||f' - f||: the slack alone certifies the scales
|t| >= sqrt(6 eps/(1 - rho^2)) (and |t| >= 6 eta/(1 - rho^2)); the range below must be certified by the local structure
of f'. In terms of a finite certificate the "certificate radius" is
  r(c) = min{ min_{j in supp b} |a_j|/|b_j|  [first sign flip of a base coordinate],
              nu/(2||U*b||)                  [Hilbert part of the base],
              min_m min_{k in supp omega_m} gap_m(k)/(2|omega_m(k)|)  [first box violation of a block coordinate],
              min_m C_m/(2|d_m| M_m), 1/(2|d_m|) }.
So a certificate at f' is usable iff r_* is at least of order sqrt(eps/(1-rho^2)) and its direction is within
(1 - rho^2) r_*/6 of rho g. Proposition 4.8 with f' = f gives the purely local test:
**(CA)** if for every rho < 1 and eta > 0 there is a certificate c at f with H(c) <= 1 - delta_rho and
p*(g_c - rho g) <= min(eta, (1 - rho^2) r_*(c, delta_rho)/6), then g is in cl Cert(f).

### 4.4 The Transport Theorem
**Theorem 4.10 (Transport). PROVED.** Let f_n -> f in S_{p*} (arbitrary sequence, NA or not) and let c = (b, omega) be a
finite certificate at f. Define
  G_n := { j in supp a : sign a_n(j) = sign a_j and |a_n(j)| >= |a_j|/2 },  b'_n := b 1_{G_n},  tau_n := b'_n(zhat_n),
  b_n := b'_n - tau_n a_n,  c_n := (b_n, omega)  (same block coefficients omega_m; d_{n,m} := <D w_{n,m}, D omega_m>/C_{n,m}).
Then for n large c_n is a finite certificate at f_n, ||g_{c_n} - g_c|| -> 0, H(c_n) -> H(c), kappa(c_n) -> kappa(c), and
liminf_n r(c_n) >= r(c)/2. If moreover g_c is in C(f) and H(c) <= 1, then for every rho in (0,1), rho g_{c_n} is in
Cert(f_n) for all large n.

*Proof.* Base. By Fact E, a_n -> a in l_1, nu_n -> nu, e_n -> e, z_n -> z weak*, and z_n = sign a_n on supp a_n. Each
j in supp a eventually lies in G_n, so b'_n -> b in l_1 by dominated convergence. On G_n, z_n(j) = sign a_n(j) = sign a_j = z_j,
hence tau_n = sum_{j in G_n} b_j z_j + <U*b'_n, e_n> -> b(z) + <U*b, e> = b(zhat) = 0, and b_n -> b in l_1.
supp b_n is contained in supp a_n; on G_n, |b_n(j)|/|a_n(j)| <= 2|b_j|/|a_j| + |tau_n|, and on supp a_n \ G_n the ratio is |tau_n|;
so ||b_n/a_n||_infinity <= 2||b/a||_infinity + |tau_n|. Since a_n(zhat_n) = 1 (Fact B at f_n), b_n(zhat_n) = tau_n - tau_n = 0.
Thus (C1) holds at f_n, h_n(b_n) = (||U*b_n||^2 - <U*b_n, e_n>^2)/nu_n -> h(b), and ||U*b_n|| -> beta.
Blocks. For k in supp omega_m (finite) and m in the finite set of active blocks, w_{n,m}(k) -> w_m(k) and M_{n,m} -> M_m
(Fact E), so M_{n,m} - |w_{n,m}(k)| -> gap_m(k) > 0: eventually supp omega_m misses P_{n,m}, and gap_{n,m}(omega_m) -> gap_m(omega_m).
Also d_{n,m} -> d_m, C_{n,m} -> C_m and the block coefficients converge. Hence H(c_n) -> H(c), kappa(c_n) -> kappa(c), and
liminf r(c_n) >= min(1/(2||b/a||), nu/(2 beta), block radii of c) >= r(c)/2.
Directions. g_{c_n} - g_c = (b_n - b) + sum_m (d_m R_m* w_m - d_{n,m} R_m* w_{n,m}) -> 0 since R_m* w_{n,m} -> R_m* w_m in norm.
Mates. Let delta := (1 - rho^2)/2. Then H(rho c_n) = rho^2 H(c_n) -> rho^2 H(c) <= rho^2 < 1 - delta, and
r_*(rho c_n, delta) = min(r(c_n)/rho, delta/(2 rho kappa(c_n) + 2), sqrt(delta)) is bounded below by some r_0 > 0 for n large.
Apply Proposition 4.8 with f' = f_n, c' = rho c_n and g = g_c: eps_n = p*(f_n - f) -> 0 and eta_n = rho p*(g_{c_n} - g_c) -> 0,
so the two inequalities hold for n large, and rho g_{c_n} = g_{rho c_n} lies in Cert(f_n). QED.

**Corollary 4.11 (lower semicontinuity of the certificate fibre). PROVED.** For every sequence f_n -> f in S_{p*}:
  cl Cert(f) is contained in Li_n cl Cert(f_n), which is contained in Li_n C(f_n).
Consequently:
 (a) every mate in cl Cert(f) is recovered along every NA sequence f_n -> f; any finitely many such mates are recovered
     simultaneously along any common sequence; (f, g) is in cl NA((X,p), l_2^2) for every g in cl Cert(f);
 (b) the set G := { f in S_{p*} : C(f) = cl Cert(f) } is contained in R, and C is Hausdorff continuous at every f in G;
 (c) (reduction) if for every f in S_{p*} the defect Def(f) := C(f) \ cl Cert(f) is contained in Li_n C(f_n) for SOME NA
     sequence f_n -> f, then NA((X,p), l_2^2) is dense; in particular density follows if G = S_{p*}.

*Proof.* By Theorem 4.10, rho Cert(f) is contained in Li Cert(f_n) for each rho < 1; Li is closed; so cl Cert(f) is inside
Li Cert(f_n) = Li cl Cert(f_n). (a) then follows from Corollary 3.3. (b): upper semicontinuity (Theorem 3.1) plus
C(f) = cl Cert(f) in Li C(f_n) give Kuratowski convergence of compact sets inside the compact Q, hence Hausdorff convergence.
(c): for that sequence C(f) = cl Cert(f) cup Def(f) lies in Li C(f_n); apply Corollary 3.3. QED.

**Corollary 4.12 (the known classes (R6), simultaneously; re-proof of [Check, Thm 3.1]). PROVED.**
 (i) Block directions g = R_m*(omega - d w_m), omega finitely supported strictly below the peak, with H <= 1 and (f,g)
     contractive: g is in Cert(f), hence recovered along every sequence. This is the finite local-certificate theorem of
     [Check], now proved (and extended to combinations of several blocks and a base part).
 (ii) Base directions b in c_00 (or b in l_1 with ||b/a|| < infinity), supp b in supp a, b(xi) = 0: b/C is in Cert(f) for
     every C >= C_b := max( 1, sqrt(2 h(b)), p*(b) r_0/(s(r_0) - 1) ), where r_0 := min(r(c), 1/(4 kappa(c) + 4), 1/sqrt 2) for c = (b, 0).
 (iii) Weighted directions of Preprint A, Thm 3.1, with H <= 1 and (f,g) contractive: in cl Cert(f) (Theorem 6.2 below).
 (iv) All mates of types (i)-(iii), and their closed convex hull, are recovered simultaneously along ANY NA sequence f_n -> f.
*Proof of (ii).* c/C has H = h(b)/C^2 <= 1/2, kappa(c/C) = kappa(c)/C <= kappa(c), r(c/C) = C r(c) >= r(c); so
r_*(c/C, 1/2) >= r_0 and Lemma 4.6 gives p*(f + sigma b/C) <= s(sigma) for |sigma| <= r_0. For |sigma| >= r_0,
p*(f + sigma b/C) <= 1 + |sigma| p*(b)/C <= s(sigma) because (s(sigma) - 1)/|sigma| is increasing in |sigma|. QED.

**Theorem 4.13 (ranges l_2^{d+1}). PROVED.** Let c_1, ..., c_d be finite certificates at f with
G := (g_{c_1}, ..., g_{c_d}) in the joint fibre C_d(f) (i.e. p*(f + sum_i t_i g_{c_i}) <= s(|t|) for all t in R^d) and
sup_{theta in S^{d-1}} H(sum_i theta_i c_i) <= 1. Then for every sequence f_n -> f in S_{p*} and rho < 1, the transported tuple
rho G_n := (rho g_{c_{1,n}}, ..., rho g_{c_{d,n}}) lies in C_d(f_n) for n large, and G_n -> G. Hence
cl Cert_d(f) is contained in Li_n C_d(f_n), where Cert_d(f) is the set of such tuples.
*Proof.* The transport of Theorem 4.10 is linear in c (with the same G_n and the same tau-correction applied to each b_i),
so c(t) := sum_i t_i c_i transports to c_n(t) = sum_i t_i c_{i,n}. On the unit sphere, r(c(theta)) >= r_0 > 0 (supports of the
omega_{i,m} are finitely many, ||b(theta)/a|| <= sum |theta_i| ||b_i/a||, |d_m(theta)| <= sum |theta_i||d_{i,m}|), uniformly in n large.
Run the proof of Proposition 4.8 along each ray t = |t| theta with the slack s(|t|) - s(rho|t|). QED.

Remark 4.14 (on the condition H(c) <= 1). If g_c is a mate but H(c) > 1, the decompositions that make g_c a mate are not
the linear one. The simplest cheaper decompositions are quadratic "shifts" along w (§4.5): they are transported as well, which
shows that the coefficient condition of the [Check] theorem is NOT sharp (Example 4.18). More general non-linear decompositions
are discussed in §7.

### 4.5 Shifted certificates: the coefficient condition H(c) <= 1 is not sharp

Since f = a + L*w, for any lambda we may rewrite f = lambda(a + L*w) - (lambda - 1) f. Taking lambda = 1 + theta tau^2 moves an amount of
order tau^2 of "first-order mass" between the base and the blocks. This changes the second-order coefficients.

**Definition 4.15.** A *shifted certificate* is c = (b, omega, theta) where (b, omega) is a finite certificate and theta = (theta_m) is a
finitely supported real family. Put v_theta := sum_m theta_m R_m* w_m (in l_1) and
  kappa_q(v) := sum_{j not in supp a} ( |v_j| + z_j v_j )  in [0, 2||v||_1]   (a "kink cost": zero iff v_j = -|v_j| z_j off supp a, which needs |z_j| = 1 where v_j != 0),
  H^sh(c) := max( h(b) - 2 sum_m theta_m |zeta_m|_m / q_0 + 2 kappa_q(v_theta),  max_m ( H_m(omega_m) + 2 theta_m ) ).
(Note v_theta(zhat) = sum_m theta_m <w_m, zeta_m>/q_0 = sum_m theta_m |zeta_m|/q_0.) The direction is unchanged: g_c := b + sum_m R_m*(omega_m - d_m w_m).
The associated decomposition is
  A(tau) := a + tau b - tau^2 v_theta,   W_m(tau) := (1 + theta_m tau^2) w_m + tau (omega_m - d_m w_m),   A(tau) + sum_m R_m* W_m(tau) = f + tau g_c.
Scaling: rho.c := (rho b, rho omega, rho^2 theta) has g_{rho.c} = rho g_c and H^sh(rho.c) = rho^2 H^sh(c). H^sh is convex in (b, omega, theta), and
Cert^sh(f) := { g_c in C(f) : c shifted certificate with H^sh(c) <= 1 } is convex, symmetric, and contains Cert(f) (theta = 0).

**Proposition 4.16 (shifted expansion). PROVED.** For a shifted certificate c at f there is eps_c(tau) -> 0 (tau -> 0) with
  p*(f + tau g_c) <= 1 + (tau^2/2)( H^sh(c) + eps_c(tau) ).
*Proof.* Blocks: W_m(tau) = (1 + theta_m tau^2)[w_m + tau'(omega_m - d_m w_m)] with tau' := tau/(1 + theta_m tau^2), so by Lemma 4.4(d)
N_m(W_m(tau)) <= (1 + theta_m tau^2)(1 + (tau'^2/2) H_m (1 + kappa |tau'|)) = 1 + tau^2(theta_m + H_m/2) + O(|tau|^3).
Base: apply the identity of Lemma 7.2 with t = tau, B = b - tau v_theta (B(zhat) = -tau v_theta(zhat), and tau B_j = -tau^2 v_j off supp a):
q*(A(tau)) = 1 - tau^2 v(zhat) + tau^2 kappa_q(v) + Fl_{b - tau v}(tau) + nu Psi(tau U*(b - tau v)/nu), v = v_theta.
For |tau| <= 1/(2||b/a||), each flip term is <= 2(tau^2 |v_j| - |a_j|/2)_+, so Fl <= 2 tau^2 sum_{j in supp a, |v_j| > |a_j|/(2 tau^2)} |v_j| = o(tau^2)
(dominated convergence; it vanishes for small tau if a is in c_00). The Hilbert term is (tau^2/2) h(b - tau v)(1 + O(tau)) = (tau^2/2)(h(b) + O(tau)).
Combine with Fact A. QED.

**Theorem 4.17 (shifted transport). PROVED.** Let f_n -> f in S_{p*} (arbitrary), c = (b, omega, theta) a shifted certificate at f, and
c_n := (b_n, omega, theta) with b_n as in Theorem 4.10. For every eta > 0 there are tau_eta > 0 and n_eta such that for n >= n_eta and
|tau| <= tau_eta:  p*(f_n + tau g_{c_n}) <= 1 + (tau^2/2)(H^sh(c) + eta). Moreover limsup_n H^sh_n(c_n) <= H^sh(c) (H^sh_n computed at f_n).
Consequently, if g_c is in C(f) and H^sh(c) <= 1, then for every rho < 1, rho g_{c_n} = g_{rho.c_n} lies in Cert^sh(f_n) for n large; hence
cl Cert^sh(f) is contained in Li_n cl Cert^sh(f_n), which is contained in Li_n C(f_n), for EVERY sequence f_n -> f.

*Proof.* Blocks: exactly as in Proposition 4.16, with the uniform bounds of Theorem 4.10 for (d_{n,m}, H_{n,m}, kappa, radii).
Base at f_n, with v_n := sum theta_m R_m* w_{n,m} (-> v_theta in l_1) and the identity of Lemma 7.2 at f_n:
q*(a_n + tau b_n - tau^2 v_n) = 1 - tau^2 v_n(zhat_n) + Fl^{(n)}(tau) + tau^2 kappa_{q,n}(v_n) + nu_n Psi_n(...),
where kappa_{q,n} uses supp a_n and z_n. For |tau| <= 1/(2||b_n/a_n||) we have |tau b_n(j)| <= |a_n(j)|/2, and each flip term is
 (I) for j in G_n (so |a_n(j)| >= |a_j|/2): <= 2 tau^2 |v_{n,j}| 1[ |v_{n,j}| > |a_j|/(4 tau^2) ];
 (II) for j in supp a_n \ G_n: <= 2(sign(a_n(j)) tau^2 v_{n,j})_+ = tau^2 (|v_{n,j}| + z_n(j) v_{n,j}).
Hence Fl^{(n)} + tau^2 kappa_{q,n}(v_n) <= tau^2 [ 2 sum_{j in supp a} |v_{n,j}| 1[|v_{n,j}| > |a_j|/(4tau^2)] + sum_{j not in supp a} (|v_{n,j}| + z_n(j) v_{n,j})
+ 2 sum_{j in supp a \ G_n} |v_{n,j}| ]. As n -> infinity and tau -> 0: the first sum -> 0 (split |v_{n,j}| <= |v_j| + |v_{n,j} - v_j| and use
dominated convergence, monotone in tau); the second has limsup <= kappa_q(v_theta) (z_n(j) -> z_j, v_n -> v_theta in l_1, domination by 2|v_{n,j}|);
the third -> 0 (each j in supp a eventually lies in G_n). Also v_n(zhat_n) -> v_theta(zhat) (norm x weak*), and the Hilbert term is
(tau^2/2)(h_n(b_n) + O(tau)) with h_n(b_n) -> h(b). This gives the uniform estimate. The same computation (without tau) gives
limsup kappa_{q,n}(v_n) <= kappa_q(v_theta), hence limsup H^sh_n(c_n) <= H^sh(c).
Mates: fix rho < 1, choose eta with rho^2(1 + eta) <= rho; for |tau| <= t_1 := min(tau_eta/rho, 2 sqrt(1 - rho)),
p*(f_n + tau rho g_{c_n}) <= 1 + (rho^2 tau^2/2)(1 + eta) <= 1 + rho tau^2/2 <= s(tau); for |tau| >= t_1 use the slack (Lemma 4.7) with
p*(f_n - f) -> 0 and p*(g_{c_n} - g_c) -> 0. Finally H^sh_n(rho.c_n) = rho^2 H^sh_n(c_n) <= 1 for n large. QED.

**Example 4.18 (shifts genuinely enlarge the recoverable class). PROVED (computation).** Single block, theta >= 0 (resp. <= 0).
* Pure base direction (omega = 0): H^sh = max( h(b) - 2 theta [ (1-q_0)/q_0 - kappa_q(R*w) ], 2 theta ) for theta >= 0. If
  r_1 := (1-q_0)/q_0 - kappa_q(R*w) > 0, optimizing theta = h(b)/(2(1 + r_1)) gives H^sh = h(b)/(1 + r_1) < h(b).
  So base directions with 1 < h(b) <= 1 + r_1 may be mates; they are recovered along every sequence by Theorem 4.17 although
  they are not in Cert(f) when a is in c_00 (then, by Fact F(a), the only finite certificate c' with g_{c'} = b is (b, 0), whose
  coefficient is h(b) > 1).
* Pure block direction (b = 0): for theta = -|theta|, H^sh = max( 2|theta| [ (1-q_0)/q_0 + kappa_q(-R*w) ], H - 2|theta| ); optimizing,
  H^sh = H r_2/(1 + r_2) with r_2 := (1-q_0)/q_0 + kappa_q(-R*w) > 0. So the condition "block quadratic coefficient <= 1" of the [Check]
  theorem can be relaxed to H <= 1 + 1/r_2 = 1 + q_0/((1 - q_0) + q_0 kappa_q(-R*w)).
(Whether such directions are actually mates depends on the global condition; the point is that whenever they are, they are
recovered, while the unshifted theory does not apply. Membership of such b in cl Cert(f) would require approximating c_00
vectors by block vectors at their own scale, i.e. rate conditions on T (§7.3).)

Remark 4.19. Corollary 4.11 (lower semicontinuity, reduction (b)-(c)) holds verbatim with Cert^sh in place of Cert (the defect
C(f) \ cl Cert^sh(f) is smaller). The averaging Theorem 6.8 below is proved for unshifted certificates only (shifted expansions have
non-explicit o(tau^2) remainders; a uniform version would extend it).
More general shifts tau^2 V with V_m = theta_m w_m + eta_m (eta_m finitely supported off-peak) give a further family; their exchange rate
uses kappa_q(R*eta) instead of |theta| kappa_q(R*w). I have not written out their transport (SKETCH: identical proof, since eta_m sits
strictly below the peaks). The general principle: the true local coefficient of g at f is a min-max over all decompositions that are
polynomial in tau; certificates and shifted certificates are its first two layers.

---------------------------------------------------------------------------------------------------

## 5. Primal reading of the multi-scale issue (exact identity; interpretation HEURISTIC)

Let f' be in NA cap S_{p*}, attaining at x' in S_p, and let f in S_{p*}, eps := p*(f' - f). Put
delta_1 := 1 - f(x') in [0, eps], gamma := g(x') for g in C(f) (so gamma^2 <= p(x')^2 - f(x')^2 = 2 delta_1 - delta_1^2),
and the corrected direction g^nat := g - gamma f' (so g^nat(x') = 0, p*(g^nat - g) <= sqrt(2 eps)).
Every y in X is y = s x' + h with s = f'(y) and h in ker f'. Then:
* rho g^nat is a mate of f' iff  rho^2 g(h)^2 <= p(s x' + h)^2 - s^2  for all s in R, h in ker f'.   (5.1)
* g in C(f) gives, with G := g(h), phi := f(h) (|phi| <= eps p(h)):
  p(s x' + h)^2 - s^2 >= (s gamma + G)^2 + (s(1 - delta_1) + phi)^2 - s^2
                       = -kappa s^2 + 2 s (gamma G + (1 - delta_1) phi) + G^2 + phi^2,   kappa := 1 - gamma^2 - (1 - delta_1)^2 >= 0.  (5.2)
(5.2) is an identity-based lower bound (PROVED). It implies (5.1) only on the range of s where -kappa s^2 + 2 s(...) is
small compared with (1 - rho^2) G^2, i.e. |s| <~ (1 - rho^2)^{1/2} |G| / sqrt(kappa) with kappa <= 2 delta_1 <= 2 eps. For larger |s|,
writing h = s v, (5.1) is the condition rho^2 g(v)^2 <= 2 Delta'(v) (1 + o(1)) with Delta'(v) := p(x' + v) - f'(x' + v) >= 0, i.e. a
condition on the second-order behaviour of p at x' at the scales ||v|| <~ sqrt(eps). These scales are invisible from f.
This is the primal counterpart of Remark 4.9 (dual scales |t| <~ sqrt(eps)). (Interpretation: HEURISTIC; the identity and the
inequality (5.2) are exact.)

---------------------------------------------------------------------------------------------------

## 6. Beyond finite certificates: weighted certificates (Theorem W) and linear decompositions (Theorem L)

### 6.1 Box tails
For a block m and omega: N -> R vanishing on P_m, put for sigma > 0
  E_m(sigma; omega) := { k not in P_m : sigma |omega(k)| > gap_m(k)/2 },   T_m(sigma; omega) := sum_{k in E_m(sigma; omega)} lambda_{k,m} |omega(k)|.
E_m(sigma; omega) decreases as sigma decreases and its intersection over sigma > 0 is empty (gap_m(k) > 0 off P_m).

**Lemma 6.1 (o(sigma) box tails). PROVED.** T_m(sigma; omega) = o(sigma) as sigma -> 0 in each of the cases:
 (a) sum_k lambda_k omega(k)^2 / gap(k) < infinity ("gap-weighted");
 (b) omega is bounded and |omega(k)| <= K sqrt(gap(k)) whenever gap(k) <= gamma_0 (some K, gamma_0 > 0);
 (c) Preprint A's weighted directions: gap >= M/2 on supp omega and sum_k lambda_k omega(k)^2 < infinity (a special case of (a)).
*Proof.* (a) On E(sigma), lambda_k |omega(k)| < 2 sigma lambda_k omega(k)^2/gap(k); dominated convergence on the convergent series
over the shrinking sets E(sigma). (b) If sigma ||omega||_infinity < gamma_0/2, coordinates with gap > gamma_0 are not in E(sigma); if
gap(k) <= gamma_0 and k is in E(sigma) then gap(k)/2 < sigma K sqrt(gap(k)), so gap(k) < 4K^2 sigma^2 and |omega(k)| < 2K^2 sigma; hence
T(sigma) <= 2K^2 sigma sum_{gap(k) < 4 K^2 sigma^2} lambda_k = o(sigma). (c) sum lambda omega^2/gap <= (2/M) sum lambda omega^2. QED.

### 6.2 Theorem W (weighted certificates)
**Theorem 6.2 (W). PROVED.** Let
* b in l_1 with supp b in supp a, b(zhat) = 0 and flip-weight Fw(b) := sum_{j in supp a} b_j^2/|a_j| < infinity;
* for finitely many blocks m, omega_m: N -> R vanishing on P_m with sum_k lambda_{k,m}|omega_m(k)| < infinity and
  T_m(sigma; omega_m) = o(sigma).
Then D_m omega_m is in l_2, R_m* omega_m converges absolutely; put d_m := <D_m w_m, D_m omega_m>/C_m,
g := b + sum_m R_m*(omega_m - d_m w_m), H := max(h(b), max_m H_m(omega_m)). If g is in C(f) and H <= 1, then g is in cl Cert(f);
consequently g is recovered along every sequence f_n -> f (Corollary 4.11).

This strictly extends Preprint A, Thm 3.1 (which needs b = 0, one block, gap >= M/2 on supp omega and sum lambda omega^2 < infinity):
near-peak supports are allowed as long as sum lambda omega^2/gap < infinity, and flip-weighted base parts are allowed.

*Proof.* Sum_k Phi(k)^2 omega(k)^2 <= (sum_k lambda_k |omega(k)|)^2 (as Phi(k) <= lambda_k), so D omega is in l_2.
Truncations: for J in N let kappa_J := (b 1_{[1,J]})(zhat) (-> b(zhat) = 0), b_J := b 1_{[1,J]} - kappa_J a, omega_{m,J} := omega_m 1_{[1,J]},
c_J := (b_J, (omega_{m,J})). Each c_J is a finite certificate ((C1): supp b_J in supp a, ||b_J/a|| finite since only finitely many j <= J
plus a multiple of a, b_J(zhat) = kappa_J - kappa_J = 0; (C2) clear). g_{c_J} -> g and H(c_J) -> H.

*Claim (uniform expansion).* For every eta > 0 there are sigma_eta > 0 and J_eta such that for J >= J_eta and |sigma| <= sigma_eta:
  p*(f + sigma g_{c_J}) <= 1 + (sigma^2/2)(H(c_J) + eta).
*Proof of the claim.* Fix sigma != 0. For each active block m let K := supp omega_{m,J} \ E_m(|sigma|; omega_m) (kept coordinates),
omega' := omega_m 1_K, d' := <D w_m, D omega'>/C_m, W_m := (1 - d' sigma) w_m + sigma omega', and
Delta_m := R_m*(omega_{m,J} - omega') + (d' - d_{m,J}) R_m* w_m. Put A := a + sigma b_J + sigma sum_m Delta_m. Then
A + sum_m R_m* W_m (other blocks unchanged) = f + sigma g_{c_J}.
Blocks: on K, |sigma omega'(k)| <= gap(k)/2, and |d'| <= ||D omega_m||_2 so |d' sigma| <= 1/2 for small sigma. By Lemma 4.4(c),(d)-type
estimates, N_m(W_m) <= 1 + (sigma^2/2)(||h'_perp||^2/C_m)(1 + 2|d' sigma| M_m/C_m), h' := D omega', and
||h'_perp|| <= ||P-perp D omega_{m,J}|| + ||D omega_m 1_{E_m(|sigma|)}||, where the last term tends to 0 as sigma -> 0 uniformly in J.
So N_m(W_m) <= 1 + (sigma^2/2)(H_m(omega_{m,J}) + o(1)) uniformly in J.
Base: q*(A) <= q*(a + sigma b_J) + |sigma| sum_m q*(Delta_m), and, using q*(u_{k,m}) = 1 and Phi^2 <= lambda,
q*(Delta_m) <= T_m(|sigma|) + (M_m/C_m) sum_{E_m(|sigma|)} Phi(k)^2 |omega_m(k)| q*(R_m* w_m) <= T_m(|sigma|)(1 + M_m q*(R_m* w_m)/C_m) = o(|sigma|)
uniformly in J. By Lemma 4.3 (b_J(zhat) = 0), q*(a + sigma b_J) = 1 + Fl_{b_J}(sigma) + nu Psi(sigma U* b_J/nu). For |sigma kappa_J| <= 1/2,
-sign(a_j) sigma (b_J)_j - |a_j| <= |sigma||b_j| - |a_j|/2 for j <= J and < 0 for j > J; with (x - y/2)_+ <= x^2/(2y) 1[x > y/2]
(as x^2 - 2xy + y^2 >= 0) we get Fl_{b_J}(sigma) <= sigma^2 sum_{j : |b_j|/|a_j| > 1/(2|sigma|)} b_j^2/|a_j| = o(sigma^2) uniformly in J.
And nu Psi(...) <= (sigma^2/2) h(b_J)(1 + 2|sigma| ||U* b_J||/nu). Combining via Fact A proves the claim.
*Conclusion.* Fix rho in (0,1) and eta > 0 with rho(1 + 2 eta) <= 1. For J large, H(c_J) <= 1 + eta. For |t| <= t_1 := min(sigma_eta/rho, 2 sqrt(1-rho), 1):
p*(f + t rho g_{c_J}) <= 1 + (rho^2 t^2/2)(1 + 2 eta) <= 1 + rho t^2/2 <= 1 + t^2/2 - t^4/8 <= s(t). For |t| >= t_1, by Lemma 4.7,
p*(f + t rho g_{c_J}) <= s(rho t) + rho |t| p*(g_{c_J} - g) <= s(t) as soon as p*(g_{c_J} - g) <= (1 - rho^2) t_1/3.
Hence for J large rho g_{c_J} is in C(f) with H(rho c_J) = rho^2 H(c_J) <= 1, i.e. rho g_{c_J} in Cert(f); letting J -> infinity and
rho -> 1 gives g in cl Cert(f). QED.

### 6.3 Linear decompositions (Theorem L)
**Definition.** A *locally admissible linear decomposition* of g in X* is a representation g = b + sum_{m in F} R_m* Omega_m
(F finite, b in l_1, Omega_m in l_infinity) together with tau_0 > 0 such that for all |tau| <= tau_0:
  q*(a + tau b) <= s(tau)  and  N_m(w_m + tau Omega_m) <= s(tau) for m in F.
(Equivalently, by Fact A, the linear path f + tau g = (a + tau b) + L*(w + tau Omega) is admissible at level s(tau).)

**Lemma 6.3 (structure). PROVED.** If (b, Omega) is a locally admissible linear decomposition, then
 (i) supp b is contained in supp a, b(zhat) = 0, and h(b) <= 1;
 (ii) for each m in F there are mu_m in R and a bounded omega_m vanishing on P_m with Omega_m = omega_m - d_m w_m, where
      d_m = -mu_m/M_m = <D w_m, D omega_m>/C_m, and
        |omega_m(k)| <= sqrt(2 gap_m(k)) + |mu_m| gap_m(k)/M_m   whenever gap_m(k) <= tau_0^2/2;
 (iii) H_m(omega_m) <= 1 for each m.
In particular each omega_m has o(sigma) box tails (Lemma 6.1(b)).

*Proof.* (i) phi(tau) := q*(a + tau b) is convex, phi(0) = 1, phi(tau) <= 1 + tau^2/2 on |tau| <= tau_0; hence its one-sided derivatives
satisfy phi'(0+) <= 0 <= phi'(0-) <= phi'(0+), so both vanish. By dominated convergence,
phi'(0+/-) = sum_{supp a} sign(a_j) b_j +/- sum_{j not in supp a} |b_j| + <U*b, e>. Hence sum_{j not in supp a}|b_j| = 0 and b(zhat) = 0.
By the identity of Lemma 4.3 (Fl_b >= 0) and the lower bound for Psi (valid whenever |tau| beta/nu <= 1/2, flips or not),
(tau^2/2) h(b)/(1 + |tau| beta/nu) <= phi(tau) - 1 <= tau^2/2, so h(b) <= 1.
(ii) Fix m; psi(tau) := ||w + tau Omega||_infinity and chi(tau) := ||D(w + tau Omega)||_2 are convex, chi is differentiable at 0 with
chi'(0) = <D Omega, D w>/C. As in (i), N = psi + chi is differentiable at 0 with N'(0) = 0, so psi'(0) exists and equals
mu := -chi'(0). For k in P: psi(tau) >= M + tau sigma_k Omega(k), which for tau -> 0+ and tau -> 0- gives sigma_k Omega(k) = mu.
Next psi(tau) <= s(tau) - chi(tau) <= 1 + tau^2/2 - C - tau chi'(0) = M + tau mu + tau^2/2 (convexity of chi). For k not in P with
w(k) != 0 and sigma'_k := sign w(k): tau(sigma'_k Omega(k) - mu) <= gap(k) + tau^2/2 for |tau| <= tau_0; choosing
tau = +/- min(tau_0, sqrt(2 gap(k))) gives |sigma'_k Omega(k) - mu| <= sqrt(2 gap(k)) when gap(k) <= tau_0^2/2.
Put d := -mu/M and omega := Omega + d w. On P, omega(k) = mu sigma_k - mu sigma_k = 0. Off P,
omega(k) = sigma'_k[(sigma'_k Omega(k) - mu) + mu gap(k)/M], giving the bound (and omega = Omega where w(k) = 0).
Finally mu = -<D Omega, D w>/C = -(<D omega, D w> - d C^2)/C and mu = -d M give d(M + C) = <D omega, Dw>/C, i.e. d = <Dw, D omega>/C.
(iii) w + tau Omega = (1 - d tau) w + tau omega, so Lemma 4.4(b) gives
1 + tau^2 ||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y) <= 1 + tau^2/2; letting tau -> 0 (Y -> C) gives ||h_perp||^2 <= C, i.e. H_m <= 1. QED.

**Lemma 6.4 (monotone truncation of base parts). PROVED (numerically checked).** Let b in l_1, supp b in supp a, b(zhat) = 0;
let G be any subset of supp a, b^G := b 1_G, kappa := b^G(zhat), c := b^G - kappa a (so c(zhat) = 0). If
|sigma| <= min( 1/(2|kappa|), nu/(2||U|| max(||c||_1, ||b||_1)) ) then
  q*(a + sigma c) <= q*(a + sigma b) + sigma^2 [ 4|kappa| ||b||_1 + (4||U||^2/nu) max(||c||_1, ||b||_1) ||c - b||_1 ].
*Proof.* By Lemma 4.3 the first-order terms vanish and q*(a + sigma c) - q*(a + sigma b) = [Fl_c - Fl_b](sigma) + nu[Psi(sigma U*c/nu) - Psi(sigma U*b/nu)].
For j in G, with x_j := -sign(a_j) sigma b_j - |a_j|: -sign(a_j) sigma c_j - |a_j| = x_j + sigma kappa |a_j| <= x_j + |sigma kappa||a_j|, and
(x + e)_+ <= x_+ + e 1[x > -e]; on {x_j > -|sigma kappa||a_j|} we have |sigma b_j| >= |a_j|(1 - |sigma kappa|) >= |a_j|/2.
For j in supp a \ G: -sign(a_j) sigma c_j - |a_j| = (sigma kappa - 1)|a_j| < 0. Hence Fl_c(sigma) <= Fl_b(sigma) + 4 sigma^2 |kappa| ||b||_1
(removing coordinates only removes nonnegative flip terms). The Hilbert difference is bounded by Lemma 4.3. QED.
(Key point: discarding base coordinates never increases sign-flip costs, so no flip-weight is needed.)

**Theorem 6.5 (L). PROVED.** If g is in C(f) and admits a locally admissible linear decomposition, then g is in cl Cert(f);
consequently g is recovered along every sequence f_n -> f.

*Proof.* Let (b, Omega) be the decomposition and (omega_m, d_m) as in Lemma 6.3. For t in (0, 1) choose J_t -> infinity (as t -> 0) and
  G_t := supp a cap [1, J_t] cap { j : |b_j| <= |a_j|/(2t) },  b^{(t)} := b 1_{G_t},  kappa_t := b^{(t)}(zhat),  b_t := b^{(t)} - kappa_t a,
  omega_{m,t} := omega_m 1_{[1, J_t]},  c_t := (b_t, (omega_{m,t})).
c_t is a finite certificate (||b_t/a|| <= 1/(2t) + |kappa_t|). As t -> 0: b^{(t)} -> b in l_1, kappa_t -> b(zhat) = 0, b_t -> b,
g_{c_t} -> g, and H(c_t) -> max(h(b), H_m(omega_m)) <= 1 (Lemma 6.3).
*Claim.* For every eta > 0 there are sigma_eta, t_eta > 0 such that for 0 < t <= t_eta and |sigma| <= sigma_eta:
  p*(f + sigma g_{c_t}) <= max( q*(a + sigma b) + eta sigma^2, 1 + (sigma^2/2)(max_m H_m(omega_{m,t}) + eta) ).
Proof: same decomposition as in the proof of Theorem 6.2 (discarding, at scale sigma, the block coordinates in E_m(|sigma|; omega_m) into
the base). Blocks: as there, using Lemma 6.1(b) for the box tails of omega_m. Base:
q*(a + sigma b_t + sigma sum Delta_m) <= q*(a + sigma b_t) + o(sigma^2) (uniformly in t), and by Lemma 6.4 (with G = G_t)
q*(a + sigma b_t) <= q*(a + sigma b) + sigma^2 [4|kappa_t| ||b||_1 + (4||U||^2/nu) max(||b_t||,||b||) ||b_t - b||_1] = q*(a + sigma b) + o_t(1) sigma^2.
*Conclusion.* Fix rho in (0,1); pick eta with eta <= (1 - rho^2)/(3 rho^2) and rho(1 + 2 eta) <= 1. For |tau| <= tau_1 small (also rho|tau| <= tau_0):
q*(a + rho tau b) + eta rho^2 tau^2 <= s(rho tau) + (1 - rho^2) tau^2/3 <= s(tau) (Lemma 4.7), and
1 + (rho^2 tau^2/2)(max_m H_m(omega_{m,t}) + eta) <= 1 + rho tau^2/2 <= s(tau) for t small. So p*(f + tau rho g_{c_t}) <= s(tau) for |tau| <= tau_1,
and for |tau| >= tau_1 by the slack (Lemma 4.7) once p*(g_{c_t} - g) is small. Thus rho g_{c_t} lies in Cert(f) for small t, and rho g_{c_t} -> rho g. QED.

**Corollary 6.6. PROVED.** The closed convex hull of all mates covered by Theorems 6.2 and 6.5 (and by Corollary 4.12) is contained in
cl Cert(f) and is recovered, simultaneously, along every sequence f_n -> f in S_{p*}.

Remarks 6.7.
* Theorem 6.5 covers: base directions b in l_1 with infinitely many sign flips (relevant when a is not in c_00, briefing R7(iii)), as long
  as the flip cost is paid inside the budget s(tau); bounded block parts using near-peak coordinates (the decay
  |omega(k)| <= sqrt(2 gap(k)) + K gap(k) is then automatic). Theorem 6.2 covers unbounded block parts (weighted directions) with
  near-peak support (part of R7(iv)).
* The unbounded weighted examples of Preprint A (Remark "Non-attaining examples", no bounded lift) are covered by Theorem 6.2; by
  Corollary 4.11 they are recovered along EVERY sequence, simultaneously with all certificate mates. In particular the derivative
  blow-up of Preprint A, Prop. 3.3, is no obstruction to recovery.
* What is NOT covered: mates whose admissible decompositions are not (regularized-)linear in t, i.e. whose decomposition must change
  qualitatively with the scale t. See §7.

### 6.4 The averaging ("ladder") theorem: O(t) remainders suffice

The following result is the strongest positive tool in these notes. It replaces the o(t)-type hypotheses of Theorems 6.2 and 6.5
by O(t), needs no monotonicity, and only uses convexity of p*.

**Theorem 6.8 (averaging over scales). PROVED.** Let g be in C(f). Suppose there are constants c_0 > 0, kappa_0 < infinity, K < infinity,
t_* > 0 and a function eta(t) -> 0 (t -> 0+) such that for every t in (0, t_*] there is a finite certificate c_t at f with
 (i) H(c_t) <= 1 + eta(t),   (ii) r(c_t) >= c_0 t,   (iii) kappa(c_t) <= kappa_0,   (iv) p*(g - g_{c_t}) <= K t.
Then g lies in cl Cert(f); consequently g is recovered along every sequence f_n -> f in S_{p*} (Corollary 4.11).

*Proof.* Fix rho in (0,1). Choose s_0 in (0, 1] and eta_0 > 0 with
  rho^2 (1 + eta_0)(1 + kappa_0 s_0) <= (1 + rho^2)/2   and   s_0^2 <= 1 - rho^2,
then an integer n >= 24 rho^2 K /(c_0 (1 - rho^2)), and finally t_1 in (0, t_*] so small that eta(t) <= eta_0 for t <= t_1,
t_1 <= rho s_0/(2 c_0), and 2 rho K t_1/n <= (1 - rho^2) s_0/3. Put t_i := t_1 2^{1-i} (i = 1, ..., n) and
  c := (1/n) sum_{i=1}^n c_{t_i}   (a finite certificate; g_c = (1/n) sum_i g_{c_{t_i}} by linearity, Lemma 4.2).
For each i and real s we have two bounds:
 (A) if rho|s| <= r(c_{t_i}) (in particular if rho|s| <= c_0 t_i): p*(f + s rho g_{c_{t_i}}) <= 1 + (rho^2 s^2/2)(1 + eta_0)(1 + kappa_0 rho |s|)
     (Proposition 4.5 and (i), (iii));
 (B) always: p*(f + s rho g_{c_{t_i}}) <= p*(f + s rho g) + rho|s| p*(g - g_{c_{t_i}}) <= s(rho s) + rho |s| K t_i (g in C(f) and (iv)).
By convexity of p*, p*(f + s rho g_c) <= (1/n) sum_i p*(f + s rho g_{c_{t_i}}).
*Case |s| <= s_0.* Use (A) for I_c := {i : c_0 t_i >= rho|s|} and (B) for the rest I_f. As the t_i are geometric with ratio 1/2,
sum_{i in I_f} t_i < 2 rho |s|/c_0. Hence
  p*(f + s rho g_c) <= max{ 1 + (rho^2 s^2/2)(1 + eta_0)(1 + kappa_0 s_0),  s(rho s) } + (rho |s| K/n)(2 rho |s|/c_0).
The last term is Q s^2 with Q := 2 rho^2 K/(c_0 n) <= (1 - rho^2)/12. Now
1 + (rho^2 s^2/2)(1 + eta_0)(1 + kappa_0 s_0) + Q s^2 <= 1 + (s^2/2)((1 + rho^2)/2 + (1 - rho^2)/6) <= 1 + (s^2/2)(1 - (1 - rho^2)/4) <= 1 + s^2/2 - s^4/8 <= s(s)
(using s^2 <= s_0^2 <= 1 - rho^2), and s(rho s) + Q s^2 <= s(s) by Lemma 4.7 (s(s) - s(rho s) >= (1 - rho^2) s^2/3 for |s| <= 1).
*Case |s| >= s_0.* Since c_0 t_i <= c_0 t_1 <= rho s_0/2 < rho|s|, every i uses (B):
p*(f + s rho g_c) <= s(rho s) + rho|s| K (1/n) sum_i t_i <= s(rho s) + 2 rho K t_1 |s|/n <= s(rho s) + (1 - rho^2) s_0 |s|/3 <= s(s),
because by Lemma 4.7, s(s) - s(rho s) >= (1 - rho^2) min(s^2, |s|)/3 >= (1 - rho^2) s_0 |s|/3 for |s| >= s_0.
Thus rho g_c lies in C(f). By convexity of H, H(rho c) = rho^2 H(c) <= rho^2 (1 + eta_0) <= (1 + rho^2)/2 <= 1, so rho g_c lies in Cert(f).
Finally p*(rho g_c - rho g) <= (rho/n) sum_i K t_i <= 2 rho K t_1/n, which tends to 0 as t_1 -> 0. Hence rho g is in cl Cert(f) for every
rho < 1, and so is g. QED.

The mechanism: the averaged certificate has, at each scale s, only O(1) of its n components "too fine" for s (their remainders
are O(s) each), while the coarse components are certified by their own expansions; the remainders of the fine components are
geometrically summable, so they cost O(s^2/n).

**Corollary 6.9 (decomposition form of the hypothesis). PROVED.** Let g be in C(f). Suppose that for every small t > 0 there are a
finite certificate c_t = (b_t, omega_t) with r(c_t) >= c_0 t and kappa(c_t) <= kappa_0, and e_t := g - g_{c_t} with p*(e_t) <= K t, such that for
tau = t or for tau = -t (either sign, possibly depending on t) the decomposition
  f + tau g = (a + tau b_t + tau e_t) + sum_m R_m*( (1 - d_{t,m} tau) w_m + tau omega_{t,m} )
is admissible at level s(tau) + o(tau^2). Then H(c_t) <= 1 + o(1), so Theorem 6.8 applies and g is in cl Cert(f).
*Proof.* Blocks: Lemma 4.4(b) (|d_{t,m}| <= kappa_0 C_m/(2M_m), so 1 - d tau > 0 and Y > 0 for small tau) gives
X^2/(sqrt(Y^2 + X^2) + Y) <= tau^2/2 + o(tau^2) with X := |tau| ||h_perp||; hence X -> 0 and ||h_perp||^2 <= (Y + X/2)(1 + o(1)) = C_m + o(1),
i.e. H_m(omega_{t,m}) <= 1 + o(1). Base: B := b_t + e_t satisfies B(zhat) = 0 because g(xi) = 0 and g_{c_t}(xi) = 0 (Lemma 4.2), so by Lemma 7.2
(flip and kink terms are >= 0) q*(a + tau B) - 1 >= nu Psi(tau U*B/nu) >= (tau^2/2) h(B)/(1 + |tau| ||U*B||/nu); with ||U*B|| bounded this gives
h(B) <= 1 + o(1). Since sqrt(h) is a seminorm and h(e_t) <= ||U||^2 ||e_t||_1^2/nu = O(t^2), sqrt(h(b_t)) <= sqrt(h(B)) + sqrt(h(e_t)) <= 1 + o(1). QED.

**Corollary 6.10 (applications). PROVED.**
 (a) *Theorem W with O(sigma) tails.* Theorem 6.2 remains true if T_m(sigma; omega_m) = o(sigma) is weakened to T_m(sigma; omega_m) = O(sigma), and
     the flip-weight condition on b is weakened to sum_{j : |b_j| > |a_j|/(2t)} |b_j| = O(t). In particular the "borderline" case of §7.4
     (box tails of exact order sigma) is IN cl Cert(f).
 (b) *Theorem L* follows again (with the base truncation error O(t) automatic: for a locally admissible linear decomposition,
     Fl_b(t) + Fl_b(-t) = 2 sum_j (|t||b_j| - |a_j|)_+ <= t^2 implies sum_{j : |a_j| <= |t||b_j|/2} |b_j| <= |t|).
 (c) *Cross mates with scale-dense rates are not a source of defect.* Let g = g_{c^0} + c v with c^0 a finite certificate, v in S_{q*},
     v(xi) = 0, and suppose some block m has off-peak coordinates k_1 < k_2 < ... with gap_m(k_i) >= gamma_0 > 0,
     ||u_{k_i,m} - v|| <= K' lambda_{k_i,m}, and lambda_{k_{i+1},m} >= beta lambda_{k_i,m} for some beta in (0,1). If g is in C(f) and the
     certificates c_t := c^0 + (0, (c/lambda_{k(t),m}) e_{k(t)} in block m), where k(t) is the first k_i with lambda_{k_i,m} <= t, satisfy
     H(c_t) <= 1 + o(1) (e.g. via Corollary 6.9), then g is in cl Cert(f).
*Proof.* (a) Truncate at scale t: b^{(t)} := b 1_{G_t} - kappa_t a with G_t := {|b_j| <= |a_j|/(2t)} cap [1,J_t], kappa_t := (b 1_{G_t})(zhat), and omega_{m,t} := omega_m 1_{{k <= J_t, |t omega_m(k)| <= gap_m(k)/2}}
with J_t large. Then r(c_t) >= min(t, ...) (radius at least t from the base ratio 1/(2t) + |kappa_t| and from the box condition),
kappa(c_t) is bounded, p*(g - g_{c_t}) <= C(sum_{|b_j| > |a_j|/(2t)}|b_j| + T_m(t) + tails) = O(t), and H(c_t) -> H <= 1. Apply Theorem 6.8.
(b) As in (a), with Lemma 6.3 (bounded omega with sqrt(gap) decay has o(sigma) tails) and, for the base, the bound
sum_{|a_j| <= 2t|b_j|} |b_j| <= 4t obtained from the displayed flip inequality at scale 4t. (c) r(c_t) >= min(r(c^0), gamma_0 lambda_{k(t)}/(2|c|), ...) >= c_1 t because lambda_{k(t)} >= beta t; the remainder is
c(v - u_{k(t)}) + d_{k(t)} R_m* w_m with ||v - u_{k(t)}|| <= K' t and |d_{k(t)}| = |c| Phi_m(k(t)) |w_m(k(t))|/(m C_m) = O(t); kappa(c_t) is bounded. Apply Theorem 6.8. QED.

**Consequence for the defect.** (PROVED, as the contrapositive of Theorem 6.8 and Corollary 6.9.) If g is in
Def(f) = C(f) \ cl Cert(f), then for all constants c_0, kappa_0, K and every eta(t) -> 0 there are arbitrarily small scales t at which no
finite certificate c with r(c) >= c_0 t, kappa(c) <= kappa_0 and H(c) <= 1 + eta(t) satisfies p*(g - g_c) <= K t; in decomposition terms, on BOTH
sides tau = +t and tau = -t the admissible decompositions at such scales are not "certificate + O(t) remainder in the base".
(HEURISTIC continuation.) By Corollary 7.3 the parts of size >> t must then be carried by the one-sided resources (N1), (N2) listed
in §7.2, on both sides, with different carriers representing the same component of g up to O(t): approximate linear relations,
at their own scales, between base vectors e_j* and block vectors u_{k,m}, or among block vectors.

---------------------------------------------------------------------------------------------------

## 7. Structure of general mates; where the defect C(f) \ cl Cert(f) can live

### 7.1 Excess bookkeeping
For A in X* and W = (W_m) in V* put
  E_q(A) := q*(A) - A(zhat) >= 0,   e_m(W_m) := N_m(W_m) - <W_m, zeta_m>/|zeta_m|_m >= 0,   pi_m := |zeta_m|_m/(1 - q_0)  (sum_m pi_m = 1).

**Lemma 7.1 (budget). PROVED.** If g is in C(f) and f + t g = A_t + L* W_t with q*(A_t) <= s(t), ||W_t||_{V*} <= s(t), then
  q_0 E_q(A_t) + (1 - q_0) sum_m pi_m e_m(W_{t,m}) <= s(t) - 1 <= t^2/2.
*Proof.* q_0 E_q(A_t) <= q_0 s(t) - A_t(xi) and (1 - q_0) pi_m e_m <= |zeta_m| s(t) - <W_{t,m}, zeta_m>. Summing,
the right sides add up to s(t) - (A_t(xi) + <W_t, L**xi>) = s(t) - (f + t g)(xi) = s(t) - 1, since g(xi) = 0. QED.

**Lemma 7.2 (exact excess formulas). PROVED.** For B in l_1 and real t:
  E_q(a + tB) = Fl_B(t) + sum_{j not in supp a} ( |t B_j| - z_j t B_j ) + nu Psi(t U*B/nu),
with Fl_B(t) := sum_{j in supp a} 2(-sign(a_j) t B_j - |a_j|)_+. For W_m = w_m + t Omega (one block, indices dropped):
  e_m(W) = sum_{k in P} |alpha_k| ( ||W||_infinity - sigma_k W(k) ) + t^2 ||P-perp D Omega||^2 / ( ||D W|| + <D W, D w>/C ).
*Proof.* First: expand ||a + tB||_1 coordinatewise as in Lemma 4.3 and subtract (a + tB)(zhat) = 1 + tB(zhat). Second: by Fact C,
<W, zeta>/|zeta| = <W, alpha> + <D W, D w>/C, and ||W||_infinity - <W, alpha> = sum_k |alpha_k|(||W||_infinity - sigma_k W(k)) because ||alpha||_1 = 1 and
alpha_k = |alpha_k| sigma_k; the Hilbert part is (||DW||^2 - <DW, Dw/C>^2)/(||DW|| + <DW, Dw/C>) and P-perp D W = t P-perp D Omega. QED.

**Corollary 7.3 (what an admissible decomposition can afford). PROVED.** With B_t := (A_t - a)/t, Omega_t := (W_t - w)/t:
 (a) sum_{j not in supp a} (1 - z_j sign(t B_t(j))) |t B_t(j)| <= t^2/(2 q_0): base mass outside supp a is free (at first order) only at
     contact coordinates K := {j not in supp a : |z_j| = 1}, and only with sign(t B_t(j)) = z_j; elsewhere it costs (1 - |z_j|)|t B_t(j)|.
 (b) sum_{k in P_m} |alpha_{m,k}| ( ||W_{t,m}||_infinity - sigma_k W_{t,m}(k) ) <= t^2/(2(1 - q_0) pi_m): deviations of a peak coordinate below the
     sup level cost at first order, weighted by alpha_{m,k}; for far peaks alpha_{m,k} ~ lambda_{k,m} |u_{k,m}(xi)|/|zeta_m| is tiny, so far peaks
     can deviate by O(1) at scale t when lambda_{k,m}|u_{k,m}(xi)| <~ |t|.
 (c) ||P-perp D_m Omega_{t,m}||_2^2 <= s(t)/((1 - q_0) pi_m) (bounded), while off-peak coordinates only satisfy the box
     |w_m(k) + t Omega_{t,m}(k)| <= ||W_{t,m}||_infinity, so Omega_{t,m}(k) may be of size up to ~ 2/|t| (weighted-direction phenomenon).
*Proof.* Lemma 7.1, Lemma 7.2, nonnegativity of each term, and ||D W|| + <DW, Dw>/C <= 2 s(t). QED.

### 7.2 Classification of the possible defect (statement HEURISTIC; the dichotomy results 7.4-7.5 and §6.4 are PROVED)
By Theorems 6.2, 6.5 and especially Theorem 6.8 / Corollary 6.9, a mate lies in cl Cert(f) as soon as, on ONE side (tau = +t or
tau = -t) and at all small scales t, it admits an admissible decomposition of the form "finite certificate of radius >~ t
and bounded kappa + remainder of norm O(t) placed in the base" (Corollary 6.9). Hence a mate in the defect Def(f) = C(f) \ cl Cert(f) must, on BOTH sides and at arbitrarily small
scales, carry a part of size >> t through first-order-cheap resources that are not certificates. By Corollary 7.3 these are:
 (N1) base mass at contact coordinates j in K (one-sided: allowed sign z_j sign(tau)), at near-contact coordinates (|z_j| -> 1),
      or at coordinates j in supp a with |a_j| small compared with |tau B(j)| (no first-order cost only when sign(tau B(j)) = sign a_j);
 (N2) block coordinates used beyond their two-sided capacity: deviations at weak peaks (peaks with |u_{k,m}(xi)| small; the
      first-order cost is alpha_k dev_k ~ lambda_k |u_{k,m}(xi)| dev_k/|zeta_m|, so at scale t only peaks with |u_{k,m}(xi)| <~ |t| are usable),
      and off-peak coordinates pushed toward the opposite sign by more than gap_m(k) (allowed by the box up to M + |w_m(k)|, with
      only a Hilbert cost ~ Phi_m(k)^2 (2M)^2). Both are one-sided, and both can carry mass ~ lambda_k/|t|, i.e. O(1) in total, from
      coordinates with Phi_m(k) <~ |t|. Peaks with |u_{k,m}(xi)| >= c_1 > 0 only carry O(t/c_1) at scale t (Corollary 7.3(b)).
      HEURISTIC remark ("resonance"): such carriers can represent a FIXED component c v of g at all small scales only if u_{k,m} -> v at
      rate O(Phi_m(k)) along scale-dense sequences AND the carriers stay near the peak threshold, i.e. (u_{k,m} - v)(xi)/Phi_m(k) stays close
      to +-M |zeta_m|/(C_m m); otherwise a subfamily has gaps bounded below and Corollary 6.10(c) puts the mate in cl Cert(f). So defect
      mates, if any, come from a resonance between the normer xi and the fine structure of T.
By contrast: base mass at non-contact coordinates with |z_j| <= theta < 1 only produces O(t) remainders (Corollary 7.3(a)); block
coordinates used within their two-sided capacity (|t Omega(k)| <~ gap(k)) are certificate parts; weighted-type directions whose
discarded tails are O(t), and cross mechanisms with scale-dense rates through carriers with gaps bounded below, are
certificates + O(t) at every scale (Corollary 6.10): none of these can create a defect by itself. Since (N1), (N2) are one-sided, a two-sided defect mate must use
DIFFERENT one-sided carriers on the two sides that represent the same component of g up to O(t) at each scale (N4: switching).

**Proposition 7.4 (one-sided linear decompositions). PROVED.** Let g in C(f). Suppose (b+, Omega+) and (b-, Omega-) (b+- in l_1,
Omega+- in V* supported on finitely many blocks) both represent g, and for some tau_0 > 0
  max(q*(a + tau b+), ||w + tau Omega+||) <= s(tau) for 0 <= tau <= tau_0,   max(q*(a + tau b-), ||w + tau Omega-||) <= s(tau) for -tau_0 <= tau <= 0.
Then (a) supp b+- is contained in supp a cup K, with sign b+_j = z_j and sign b-_j = -z_j for j in K cap supp b+-.
(b) If supp a cup K is finite (this holds at every NA point f, where supp a is finite and z is in c_0), then b+ = b-,
Omega+ = Omega-, supp b+ is contained in supp a, and (b+, Omega+) is a locally admissible linear decomposition; hence g is in cl Cert(f).
*Proof.* (a) For 0 < tau <= tau_0, by Lemma 7.2, q*(a + tau b+) = 1 + tau b+(zhat) + tau sum_{j not in supp a}(|b+_j| - z_j b+_j) + o(tau)
(Fl and Psi are o(tau)), and N_m(w_m + tau Omega+_m) >= 1 + tau <Omega+_m, zeta_m>/|zeta_m|. Admissibility forces both first-order
coefficients to be <= 0. Their combination q_0 [b+(zhat) + sum_{j notin supp a}(|b+_j| - z_j b+_j)] + sum_m |zeta_m| <Omega+_m, zeta_m>/|zeta_m|
equals q_0 sum_{j notin supp a}(|b+_j| - z_j b+_j) + g(xi) = q_0 sum_{j notin supp a}(|b+_j| - z_j b+_j) >= 0 and is <= 0, so
|b+_j| = z_j b+_j for every j outside supp a. The case of b- is symmetric (replace tau by -tau and b- by -b-).
(b) b+ - b- is supported in the finite set supp a cup K, so it lies in c_00; Fact F(a) gives b+ = b- and Omega+ = Omega-.
On K, sign b_j = z_j = -z_j forces b_j = 0. The common decomposition is admissible on both sides; apply Theorem 6.5. QED.

**Corollary 7.5. PROVED.** If supp a cup K is finite (e.g. f in NA) and g is in Def(f), then on at least one side of t = 0 the
mate g has NO locally admissible linear decomposition with bounded block part: its admissible decompositions are genuinely
scale dependent there. In particular, at NA points one-sided base contacts (K nonempty) can only be exploited through scale-
dependent mechanisms (N4).

Remark 7.6 (infinite contact sets). If K is infinite (possible only when f does not attain its norm: z in l_infinity \ c_0 with
|z_j| = 1 infinitely often off supp a), b+ - b- may be an infinitely supported vector in L*(V*), and Proposition 7.4(b) fails.
Whether two-piece mates of this kind exist depends on whether Y cap l_1(supp a cup K) contains suitable vectors with the sign
pattern of (a). OPEN.

### 7.3 Cross mechanisms and approximation rates (SKETCH / HEURISTIC; the positive part is Corollary 6.10(c), PROVED)
Let v in S_{q*} with v(xi) = 0, c in R, and suppose at scale t the component t c v of t g is carried by one off-peak coordinate k
of block m: put t Omega(k) := t c/lambda_{k,m} (so t R_m*(Omega(k) e_k) = t c u_{k,m}) and let the base absorb t c (v - u_{k,m}).
Costs (Lemma 7.2, Lemma 4.4): box: |t c|/lambda_{k,m} <= gap_m(k)/2; Hilbert: first order t c Phi_m(k) w_m(k)/(m C_m) (absorbed by the
d-correction, and O(t Phi_m(k)) anyway) and second order t^2 c^2/(2 m^2 C_m); base: at most |t||c| (1 + ||U||) ||v - u_{k,m}||_1.
So the cost is O(t^2) iff there is an off-peak k with lambda_{k,m} >= 2|t||c|/gap_m(k) and ||u_{k,m} - v||_1 <~ |t|.
* If such k exist at all small scales (scale-dense rates: ||u_{k_i,m} - v|| <= K' lambda_{k_i,m}, lambda_{k_{i+1}}/lambda_{k_i} >= beta > 0),
  the decomposition at scale t IS "certificate + O(t)", and Corollary 6.10(c) shows that such cross mates lie in cl Cert(f):
  they are recovered along every sequence. (Earlier in this work I expected them to be a defect source; the averaging theorem
  shows they are not.)
* If good approximations are sparse in scale (gaps in the sequence of scales), the single-carrier cross mechanism is not available
  at the intermediate scales, and a mate needing the component c v at those scales must use other resources.
Whether Martín's u_{k,m} have such rates I cannot check (paper unavailable). Status of this subsection: SKETCH (single
mechanism computation), with the positive conclusion PROVED in Corollary 6.10(c).

### 7.4 The borderline case of box tails of exact order sigma: RESOLVED
Weighted certificates whose box tails satisfy T(sigma) = O(sigma) (rather than o(sigma)) lie in cl Cert(f): Corollary 6.10(a).
(A first attempt by single-scale truncation fails for rho -> 1, because the error ~ c t is not small compared with
(1 - rho^2) times the radius ~ t; averaging over n geometric scales divides the effective error by n.)

### 7.5 Conjecture (HEURISTIC)
Call T *scale separated* if no base vector e_j* (j in N) and no block vector u_{k,m} can be approximated, within a fixed multiple of
lambda_{k',m'}, by a combination of block vectors u_{k',m'} at comparable scales lambda_{k',m'} other than itself. Conjecture: if T is
scale separated, then for every f the admissible decompositions of every mate are, on at least one side, "certificate + O(t)"
at all small scales; hence Def(f) is empty for every f, C is Hausdorff continuous on S_{p*}, and NA((c_0,p), l_2^d) is dense for all d.
Evidence: by §7.2 a defect mate needs switching between different one-sided carriers representing the same component of g up to
O(t) at scale t, which is exactly an approximation of one carrier by others at its own scale. Missing: a proof that the carried
components on the two sides must match carrier-by-carrier up to O(t) (a quantitative "linear independence at scale" argument),
and control of contacts/near-contacts and weak peaks. I have no proof. Whether Martín's T is scale separated is unknown to me.

---------------------------------------------------------------------------------------------------

## 8. Engineering NA approximants with free far coordinates

Throughout, x' = z' + U e' with a' in c_00 cap S_{q*}, e' = U*a'/||U*a'||, z' in B_{c_0}, z' = sign a' on supp a' (Fact D), f' := grad p(x').

**Lemma 8.1 (far modifications are norm-small). PROVED.** For N in N let Y_N := { y in c_0 : supp y in [N, infinity) \ supp a', ||z' + y||_infinity <= 1 }.
For y in Y_N, f'_y := grad p(x' + y) = a' + L* J_V(L(x' + y)) is norm attaining with the SAME base component a', and
sup_{y in Y_N} p*(f'_y - f') -> 0 as N -> infinity.
*Proof.* x' + y = (z' + y) + U e' with z' + y in B_{c_0} equal to sign a' on supp a', so grad q(x' + y) = a' (Fact D). Since ||y||_infinity <= 2,
||L y||_V <= sum_{m,k} lambda_{k,m} |u_{k,m}(y)| <= 2 theta_N, theta_N := sum_{m,k} lambda_{k,m} ||u_{k,m} 1_{[N,infinity)}||_1 -> 0 (dominated convergence,
sum lambda_{k,m} <= sum_m m 2^{-m}). The map v -> L*J_V(v) is norm-to-norm continuous at v = L x' (J_V is norm-to-weak* continuous at
vectors with all block components nonzero; L* is weak*-to-norm continuous on bounded sets), hence uniformly small on the balls
{ ||v - Lx'|| <= 2 theta_N }. QED.

**Lemma 8.2 (zeroing a far block coordinate). PROVED.** For every block m, every N and every delta > 0 there are j, k >= N and y = y_j e_j in Y_N
with |y_j| <= delta such that u_{k,m}(x' + y) = 0. For f'_y the coordinate k of block m is then off-peak with w''_m(k) = 0 (maximal gap).
*Proof.* Choose j >= N outside supp a' with |z'_j| <= 1/2 and |x'_j| small (x' in c_0). By (T2) choose k >= N with
||u_{k,m} - e_j*/q*(e_j*)|| <= delta_0, delta_0 small; then u_{k,m}(e_j) >= 1/(2(1 + ||U||)) and |u_{k,m}(x')| <= |x'_j| + delta_0 ||x'||_infinity.
Put y_j := -u_{k,m}(x')/u_{k,m}(e_j). Then (R_m(x' + y))(k) = 0, and by Fact C (at the NA point) k is not a peak and w''_m(k) = 0. QED.
Remark: the index k is chosen by us (u_{k,m} close to a far base vector). A prescribed k cannot in general be zeroed by far
modifications: |u_{k,m}(y)| <= 2 ||u_{k,m} 1_{[N,infinity)}||_1 for y in Y_N, which is smaller than |u_{k,m}(x')| unless u_{k,m}(x') is already tiny.

**Lemma 8.3 (new contacts and new small base support). PROVED.** (a) Setting z'_j := +-1 at finitely many far j (y in Y_N) creates new
one-sided contacts at norm cost -> 0 (Lemma 8.1). (b) For j outside supp a' with |z'_j| = 1 and eta > 0, a'' := (a' + eta z'_j e_j*)/q*(a' + eta z'_j e_j*)
is compatible with z' (sign a''_j = z'_j), and grad p(z' + U e'') -> f' as eta -> 0 (e'' -> e', continuity as in Lemma 8.1).

**Proposition 8.4 (limits of certificate engineering). PROVED.** Let f, f' in S_{p*} with forced data (a, w), (a', w'), and let c' = (b', omega')
be a finite certificate at f' with radius r' := r(c'). Then
 (a) sum_{j in supp a' : |a'_j| <= 2|a'_j - a_j|} |b'_j| <= 2 ||a' - a||_1 / r'; in particular the base mass of c' on new coordinates (j not in supp a)
     is at most ||a' - a||_1 / r';
 (b) for each block m: sum_{k in supp omega'_m : gap_m(k) < gap'_m(k)/2} lambda_{k,m} |omega'_m(k)|
       <= ( sum_k lambda_{k,m} |w'_m(k) - w_m(k)| + |M'_m - M_m| sum_k lambda_{k,m} ) / r'.
     (This includes peaks of w_m that became off-peak at f'.)
*Proof.* (a) |b'_j| <= |a'_j| ||b'/a'||_infinity <= |a'_j|/r'. (b) For k in supp omega'_m, |omega'_m(k)| <= gap'_m(k)/(2r'); if gap_m(k) < gap'_m(k)/2 then
gap'_m(k) < 2(gap'_m(k) - gap_m(k)) <= 2(|M'_m - M_m| + |w'_m(k) - w_m(k)|). QED.
*Interpretation (HEURISTIC).* Under the NA-scale criterion (eps = p*(f' - f) <= (1 - rho^2) r_*^2/6, r_* <= r'), if ||a' - a||_1 and the weighted
distances sum_k lambda_k |w'_m(k) - w_m(k)| are O(eps), then the newly created structure carries only O(eps/r') = O(sqrt(eps)) of the
recovered direction. Macroscopic new structure needs ||a' - a||_1 or sum lambda |w' - w| much larger than eps = p*(f' - f), i.e. cancellations
between a' - a and L*(w' - w) or inside L*(w' - w): a T-dependent phenomenon (near-linear dependences among the lambda_{k,m} u_{k,m},
or near-membership of Y-vectors in c_00).

**Lemma 8.5 (domination). PROVED.** If f, h in B_{p*}, lambda in (0,1) and f' := lambda f + (1 - lambda) h has p*(f') = 1, then
r_{f'} >= lambda r_f on X, hence C(f') contains lambda C(f).
*Proof.* By evenness it suffices to take y with f(y) >= 0. Then p - f' >= p - lambda f - (1 - lambda) p = lambda (p - f) and
p + f' >= p + lambda f - (1 - lambda) p = lambda (p + f), so p^2 - f'^2 >= lambda^2 (p^2 - f^2). QED.

**Lemma 8.6 (rotundity of p*). PROVED (given T1, T3, T4).** For xi in S_{p**} normed by some f in S_{p*}, the face
{h in B_{p*} : h(xi) = 1} equals {f}. Hence p* is rotund, and Lemma 8.5 applies only with h = f: it cannot produce approximants.
*Proof.* If h = A + L*W with q*(A) <= 1, ||W|| <= 1 and h(xi) = 1, then A(xi) = q_0 and <W, L**xi> = 1 - q_0, so W = J_V(L**xi) = w (smoothness)
and A(zhat) = 1 = ||A||_1 + ||U*A||; this forces U*A = ||U*A|| e = (||U*A||/nu) U*a, so A = (||U*A||/nu) a by injectivity of U*, and A(zhat) = 1 gives A = a. QED.
*Approximate version (computation, PROVED; usefulness FALSE).* If f' = lambda f + (1 - lambda) h with p*(h) = 1 + kappa, then for f(y) >= 0
p^2 - f'^2 >= [lambda(p - f) - (1-lambda) kappa p]_+ [lambda(p + f) - (1-lambda) kappa p], which degenerates exactly on the near-normer cone
{ f > (1 - (1-lambda) kappa/lambda) p } of f: the multi-scale region again.

### 8.7 A three-regime scheme for mates outside cl Cert(f) (SKETCH; not completed)
Let g be in the defect, rho < 1, and f' = grad p(x') an NA approximant with z' = z on [1, N] plus finitely many engineered far
modifications; eps := p*(f' - f). Recovery of rho g requires ONE vector g' close to rho g with p*(f' + t g') <= s(t) for all t, certified in
three regimes:
 (i) |t| >= T_0 := sqrt(6 eps/(1 - rho^2)) (and >= 6 ||g' - rho g||/(1 - rho^2)): slack (Lemma 4.7);
 (ii) t_1 <= |t| <= T_0: transfer of the admissible decompositions of f + rho t g (scale rho t) to f'. Requirements: the base resources used
      at these scales (contacts, near-contacts, flips) lie in [1, N] where z' = z, up to cost o(t^2); the block coordinates used with
      non-negligible box/peak usage lie in a finite window where |w'_m(k) - w_m(k)| and the first-order Hilbert mismatch
      |t| <D_m Omega, D_m(w'_m/C'_m - w_m/C_m)> are <= (1 - rho^2) t^2/10; and g'(x') = 0 corrections are absorbed;
 (iii) |t| <= t_1: g' = g_{c'} for a (shifted) certificate c' at f' with radius >= t_1.
For a mate of type (N1) (one-sided contact j in K used on the side t > 0, compensated on t < 0 by a scale-dependent one-sided
mechanism, so that Theorem 6.8 does not apply on either side; if the t < 0 side were "certificate + O(t)", the mate would already be
in cl Cert(f) by Corollary 6.9), the natural engineering is Lemma 8.3(b): give a' a tiny mass eta at the contact j with sign z_j. Then on t > 0 the linear decomposition stays admissible at
f' at ALL scales (|a'_j + t b_j| = |a'_j| + |t b_j|), and on t < 0 the contact is two-sided smooth for |t| <= t_1 ~ eta/|b_j|, so regime (iii)
is available with radius ~ eta; regime (ii) must transfer the cross mechanism of f on [t_1, T_0]. The difficulty: the tiny mass eta moves
e' by O(eta), hence u_{k,m}(x') by O(eta), hence the off-peak values w'_m(k) = C' m u_{k,m}(x')/(Phi_m(k)|R_m x'|) by O(eta/Phi_m(k)), which is O(1)
on the coordinates with Phi_m(k) ~ t_1 ~ eta that the t < 0 mechanism uses at the bottom of regime (ii). One must therefore re-tune
u_{k,m}(x') on the relevant window by far modifications (finitely many linear conditions, solvable by tail independence, Fact F(b)),
with precision o(t_1^2), while keeping Lemma 8.1 smallness. I could not control these precisions uniformly; this is the precise point
where strategy (A) stalls. Status: SKETCH (requirements identified), not a proof.

---------------------------------------------------------------------------------------------------

## 9. Failed attempts (with the reason they fail)

(a) **Direct transfer of decompositions** (A'_t := a' + rho t B_{rho t}, W'_t := w' + rho t Omega_{rho t}, g' := rho g). FALSE as a general method.
    Reasons: (1) w' - w is only weak*-small: ||w' - w||_{V*} need not be small; far peaks of w' may have the opposite sign to those of
    w, so |w'(k) + rho t Omega(k)| can exceed the peak level by O(1) at far coordinates where Omega_{rho t} is large. (2) Even with matching
    structure, N_m(w' + tau Omega) - N_m(w + tau Omega) contains the first-order term tau <D Omega, D(w'/C' - w/C)>, of size |tau| ||D(w' - w)||, which
    is >> tau^2 for |tau| << ||D(w' - w)||. (3) rho g does not vanish at x' (|g(x')| <~ sqrt(2 eps)); the correction g' = rho(g - g(x') f')
    introduces first-order terms of size |tau| sqrt(eps) in each component. Base parts transfer exactly only when a' = a.
(b) **Pointwise domination** r_{f'} >= rho r_f with f' NA and f not NA: FALSE (r_{f'}(x') = 0 < r_f(x')); approximate domination with
    additive errors delta p(y) is useless because the infimum defining r~ involves decompositions with unbounded sum_j p(y_j)
    (pieces +-K x' + v near the normer ray). Convex combinations: Lemmas 8.5-8.6.
(c) **Freezing an optimal decomposition at one scale t** and truncating it to a certificate: radius ~ t, error = non-certificate part at
    scale t, which is typically Theta(t) (e.g. base mass off supp a at non-contact coordinates may use the whole budget:
    ||B_t 1_{F^c}||_1 <= t/(2 q_0 (1 - theta))). The (CA) test needs error <= (1 - rho^2) t/6, which fails as rho -> 1. Rescued only by
    monotonicity (base flips: Lemma 6.4) or by o(t) tails (Theorem 6.2). SUPERSEDED: averaging the frozen certificates over n
    geometric scales (Theorem 6.8) divides the effective error by n, so O(t) remainders suffice; single-scale freezing is the
    wrong construction, not a real obstruction.
(d) **Engineering new structure through finite certificates only** (NA-scale criterion): limited by Proposition 8.4.
(e) **Local second-order analysis alone.** (1) The certificate coefficient H(c) can exceed the true local coefficient (shifts, §4.5).
    (2) The local certificate set {g_c : H(c) <= 1} without the global condition is unbounded in general: its support function at x
    is sup{ <D omega, y> : omega in c_00(S), ||P-perp D omega||^2 <= C } with y_k = m u_{k,m}(x) - (<w, R_m x>/C) Phi_m(k) w(k) on the off-peak set S,
    which is +infinity whenever (u_{k,m}(x))_{k in S} is not square summable (PROVED, elementary). So global contractivity is essential and
    membership in C(f) cannot be decided by second-order data at f alone.
(f) **Subsequential limits of optimal decompositions** (setting: a in c_00, theta := sup_{j not in supp a}|z_j| < 1, finite I). SKETCH of what one gets:
    B_t 1_{F^c} -> 0, B_t 1_F is bounded (using injectivity of U* on R^F and the Hilbert part of the budget), so along subsequences
    B_t -> B_0 in c_00(F). If moreover ||Omega_t||_{V*} stays bounded on both sides, then Omega_t -> Omega_0 weak*, g = B_0 + L* Omega_0, and by
    Fact F(a) the limit does not depend on the side or subsequence; Omega_0 is balanced on every peak set (from Corollary 7.3(b) on
    supp alpha and the one-sided constraints on P \ supp alpha), so Omega_0 = omega_0 - d_0 w with omega_0 off-peak and the consistent d_0. The first-order
    masses t B_t(zhat) and t <Omega_{t,m}, zeta_m> are O(t^2) but need not be o(t^2): their normalized limits are a shift (§4.5), so the limit
    object is a "generalized shifted certificate" (with a base shift vector lim (-t B_t 1_{F^c})/t^2 that need not be a combination of the
    R_m* w_m). Missing for a proof that g lies in cl Cert^sh(f): (i) near-peak decay of omega_0 (o(sigma) box tails) does not pass to the
    limit, because at scale t the box constraints involve Omega_t, not Omega_0; (ii) transport of general shifts with infinitely supported
    shift vectors; (iii) the bounded case itself is an assumption (weighted directions show Omega_t can be unbounded).
    If in addition the off-peak gaps are bounded below (inf_{k notin P_m} gap_m(k) > 0) then (i) disappears (box tails vanish for small sigma).
    By Theorem 6.8 the whole question reduces to showing that the non-certificate parts of (B_t, Omega_t) are O(t) on one side.

---------------------------------------------------------------------------------------------------

## 10. Conclusions, open problems, next steps

**What is now established (finite block set I; everything also holds for I = N given (T4) for p).**
1. (R3) and its finite/mate versions and transitivity are correct (§3).
2. All mates in cl Cert^sh(f) (finite certificates, shifted certificates, weighted certificates of Theorem 6.2, linear decompositions of
   Theorem 6.5, and closed convex hulls) are recovered along EVERY sequence f_n -> f in S_{p*}; the map f -> cl Cert^sh(f) is lower
   semicontinuous. In particular all (R6) classes are recovered simultaneously along one (indeed any) common sequence, and the
   [Check] local-certificate theorem is re-proved with a weaker coefficient condition (§4.5).
2'. Averaging theorem (Theorem 6.8, Corollary 6.9): a mate is in cl Cert(f) as soon as, on one side and at all small scales t, it
   is a finite certificate of radius >~ t up to an O(t) remainder. This covers weighted directions with box tails of exact order
   t (§7.4 resolved), and cross mates with scale-dense approximation rates (Corollary 6.10(c)).
3. Density of NA((c_0,p), l_2^2) (and into l_2^d) follows if, for every f, the defect Def(f) = C(f) \ cl Cert^sh(f) is recovered along some
   NA sequence; in particular if Def(f) is empty for every f, in which case C is even Hausdorff continuous everywhere.
4. Every defect mate needs genuinely scale-dependent decompositions; at points with finite contact set (all NA points) piecewise-linear
   decompositions with bounded block parts are excluded (Proposition 7.4).

**Open problems (precise).**
 (P1) Is Def(f) empty for every f? By §6.4 and §7.2 a defect mate must, on BOTH sides and at arbitrarily small scales, carry a part
      of size >> t through one-sided resources (contacts/near-contacts/near-flip coordinates of the base, weak peaks of the blocks),
      switching between different carriers. Sub-questions: (a) prove a quantitative "independence at scale" statement forcing the
      carriers on the two sides to match up to O(t) (this would prove Conjecture 7.5 under scale separation); (b) decide whether
      Martín's T is scale separated (rates of approximation of base vectors and of block vectors by block vectors at their own scale);
      (c) two-piece mates over infinite contact sets K (Remark 7.6): does Y cap l_1(supp a cup K) contain vectors with the required signs?
 (P2) Make the three-regime engineering of §8.7 rigorous for one-sided-contact mates (the transfer regime with re-tuning of u_{k,m}(x')).
 (P3) Transport of general shifts tau^2 V (Remark 4.19) with infinitely supported V; then redo §9(f) to get "bounded decompositions with
      uniform off-peak gaps => g in cl Cert^{sh,gen}(f)".
 (P4) Get Martín's construction (arXiv:2406.07273, Lemma B) to decide the rate questions; if T can be chosen "scale separated", test
      Conjecture 7.5 on that T (a positive answer for one admissible T would already give a Martín-type space with density, though not
      necessarily Martín's own).
 (P5) General finite-dimensional ranges E (not Hilbert): (R1) used the Hilbert structure; the joint-fibre/certificate machinery extends to
      l_2^d (Theorem 4.13) but not obviously to general E.

**Remarks on the sources (errors / non-sharp statements found).**
* No error found in (R1)-(R3) of the briefing, in Preprint A Thms 2.1-2.2, Props 3.2-3.3, or in the parts of Preprint B used here.
* The coefficient hypothesis "block quadratic coefficient <= 1" in the [Check] local-certificate theorem (as quoted in Preprint A,
  Section 1) and the hypothesis H <= 1 of Preprint A, Thm 3.1, are sufficient but NOT sharp: quadratic shifts along w (§4.5) give
  strictly larger recoverable classes (Example 4.18).
* Preprint A, Thm 3.1 relied on the unavailable [Check]; the dependence is now removed (Corollary 4.12, Theorem 6.2).
* Briefing (R6): "combined recoverability along a common sequence is plausible but not written down" - now proved, and along
  EVERY sequence (Corollaries 4.11-4.12, Theorems 4.17, 6.2, 6.5).
* Briefing (R7)(i) (one-sided base kinks): at points with finite contact set they cannot be used by piecewise-linear
  decompositions (Proposition 7.4); they force scale-dependent (cross) mechanisms.

**Suggested next step for the team.** Attack (P1)(a) on a single block with a in c_00 and finite contact set K: by Proposition 7.4
and Theorem 6.8, a defect mate must there use, on both sides and at all small scales, contact coordinates of K or weak peaks
carrying mass >> t; show (or refute, with explicit u_{k,m}) that two different such carriers cannot represent the same component of
g up to O(t). This is now a concrete approximation problem about (u_{k,m})_k, the weights Phi_m(k) and the values u_{k,m}(xi).

---------------------------------------------------------------------------------------------------

## Appendix. Numerical sanity checks
Script: `ctx/r1/check_expansions.py` (numpy, random instances). Results (run on 2026-10-08):
* Block certificate (Lemma 4.4): max |N(W(tau)) - (1 + tau^2 ||h_perp||^2/(sqrt(Y^2 + tau^2||h_perp||^2) + Y))| = 4.4e-16 over 2000 random
  instances x 21 values of tau in the validity window; the bound of Lemma 4.4(d) held in all cases.
* Base certificate (Lemma 4.3): the two-sided bounds (sigma^2/2) h/(1 + |sigma| beta/nu) <= q*(a + sigma b) - 1 <= (sigma^2/2) h (1 + 2|sigma| beta/nu)
  held in all 2000 x 21 cases.
* Monotone truncation (Lemma 6.4): with random a having many tiny entries (so sign flips occur), the ratio
  [q*(a + sigma c_t) - q*(a + sigma b)] / [sigma^2 (|kappa_t| ||b||_1 + ||c_t - b||_1)] never exceeded 0.098 (the lemma allows a constant
  max(4, 4||U||^2 max(||c||,||b||)/nu)), consistent with the lemma.
