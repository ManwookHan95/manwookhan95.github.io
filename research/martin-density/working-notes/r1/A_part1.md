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

