# V2-ref part 1 — the tools: Lemma H, Lemma L, Lemma QB, the two-ray example, Remark 4.5

Refereed: V2_notes.md 1.1-1.3, 2.1, Remark 4.5 (V2_notes.md = V2_head + V2_part1..4 + V2_tail, byte-identical, checked
with diff).  Sources re-read: Y1 Lemma T, T2, T3 (r6/Y1_notes.md 2.2), the note's lem:threshold and eq:margin.
Scripts: V2_ref_work/{qb_jac_check.py, jac_check2.py, tworay_tau.py}; V2's own V2_work/hoffman_minors_check.py re-run.

## 1. Lemma H (Hoffman bound through independent row sets and nonzero minors).  VERDICT: CORRECT (PROVED).
Re-derived line by line.  (1.1): the projection x* of x onto P satisfies x - x* in the normal cone
cone{A_i^T : A_i x* = b_i} (Farkas / KKT for a polyhedron); conic Caratheodory gives x - x* = A_J^T v, v > 0, J
linearly independent and active; ||x - x*||^2 = sum_J v_i (A_i x - b_i) <= ||v||_2 ||(A_J x - b_J)_+||_2 and
||v||_2 <= ||x - x*||_2/sigma_min(A_J).  (1.2): Cauchy-Binet, det(A_J A_J^T) = sum_K det(A_{J,K})^2 = prod s_i^2, and
s_k >= prod s_i / s_1^{k-1}.  (1.3): |J| <= n, ||A_J|| <= ||A||, every positive max_K |det A_{J,K}| is a nonzero minor.
Equalities: E x <= e, -E x <= -e; a row and its negative are dependent, so never in the same independent J.
Precision (harmless): the l_1-residual / l_1-distance version used in Theorem B(d) costs a factor sqrt(cols)
(dist_1 <= sqrt(n) dist_2, ||r||_2 <= ||r||_1); V2 accounts for it by (rows cols)(l).
Numerics: V2's script re-run: identical output (1500 tests, max ratio 1.0000 for both bounds).

## 2. Lemma L (simultaneous exactification via Lojasiewicz).  VERDICT: CORRECT (PROVED).
BCR Cor. 2.6.7 (B compact semialgebraic, f, g continuous semialgebraic, f^{-1}(0) ⊂ g^{-1}(0) => |g|^N <= C|f| on B) is
applied with B = [-2,2]^n, f = F_S = sum_{i in S} pi_i^2, g = dist(., Z_S) (semialgebraic: distance to a semialgebraic
set, BCR Prop. 2.2.8) or g = 1 if Z_S is empty.  Both alternatives re-derived; the choice of C_L, N_L is correct
(beta <= 1 gives beta^{2/N_S} <= beta^{2/N_L}).  The nearest common zero v' may lie outside [-2,2]^n; only |v' - v| is used.
Precision (wording only): Remark (c)'s example "v_1^2 + v_2 tiny with v_2 >= 0 forced" is not a polynomial system;
a correct example of exponent 1/2: S = {pi = v_1^2}, v = (beta^{1/2}, 0): pi(v) = beta, dist(v, Z) = beta^{1/2}.
Important feature (used in Theorem B and correct): the alternative (i) "beta >= 1/C_L" means that a family of tiny
polynomials ALWAYS has a common zero nearby unless the family is not tiny in the absolute sense; no transversality or
consistency hypothesis is needed.  This is what makes the determinantal exactification possible without any
structural assumption on the configuration.

## 3. Lemma QB (threshold buffer through a peak).  VERDICT: CORRECT (PROVED), one precision.
(a) = Y1 Lemma T2(b) lower bound (hypothesis E <= A s/(8(A+theta+1)) is part of QB) ✓.  (b): nu'_k <= nu_k + X <
theta + R(s) <= theta(zeta') ✓.  (c): T2(b) upper bound, then nu'_k >= nu_k - X > theta(zeta'); sign kept because
|zeta'(k) - zeta(k)| <= X Phi_k^2 < nu_k Phi_k^2 = |zeta(k)| ✓.
Precision (P1): QB asks for "a fixed non-degenerate peak k_0 != c" in C_1, h_0.  This is unnecessary and could fail
(a block whose only non-degenerate peak is the buffer c).  The upper bound of T2(b) holds with k_0 = c as well:
for h <= nu_c - theta, c in P(theta + h) for zeta, Ah(theta+h; zeta') <= A - h Phi_c^2 + s + E, and
Bh(theta+h; zeta') >= Bh(theta; zeta) - 2 theta E = A^2 - 2 theta E (the c-term of Bh is theta Phi_c at level theta,
unchanged by the push); so Psi(theta+h; zeta') < 0 for h Phi_c^2 > s + E + 2(theta+1)E/A, i.e. h > C_1(s+E) with
phi_0 = Phi_c^2.  Fix: "k_0 any non-degenerate peak (k_0 = c allowed)".
Numerics (qb_jac_check.py): 3000 random blocks (n = 14), k_0 random among non-degenerate peaks (c allowed), push
s in [1e-7, 1e-1] A, random E up to the admissible size: (a) 0/3000 violations, (b) 0/4434, upper bound 0/891,
peak preservation 0/6629.

## 4. The two-ray determinantal example (V2 2.1).  VERDICT: CORRECT (PROVED).
mu-coordinates: D(r_1) = (1,1), D(r_2) = (-1,-1+delta), mu = (1,1): D mu = (0, delta), C ∩ ker D = {0}, ratio 2/delta ✓.
I re-embedded it in tau-coordinates of an actual exact-cone system (tworay_tau.py): carriers 1,2 in block 1, 3,4 in
block 2, configuration rows tau_1 = tau_3, tau_2 = tau_4 (two TWO-BLOCK rays e_1 + e_3, e_2 + e_4), tau >= 0, (Z5)-rows
v_1 tau_1 + v_2 tau_2 = 0, v_3 tau_3 + v_4 tau_4 = 0 with v = (1,-1,1,-1+delta).  Results: the 4x4 minor containing both
(Z5)-rows equals delta = v_1 v_4 - v_2 v_3 (a multi-affine polynomial in the values, as Definition 2.1 says); the true
l_1 Hoffman ratio is exactly 4/delta (attained at tau = r_1 + r_2 = (1,1,1,1)), Lemma H's bound is ~22/delta
(ratio 0.18); at delta = 0 the true ratio is 1 (exact degeneracy harmless).  Every component of both ray d-vectors is
robust, so neither Y4-ref Cor. P5 nor V1 (C4) (linear component exactification) touches it, and (VR_w) fails.

## 5. Remark 4.5 (independent tuning of (theta_m, A_m)).  VERDICT: CORRECT (PROVED, local computation).
Re-derived from Lemma T: dPsi/dtheta = -2(A + theta) Phi_P^2; peak push: dPsi/ds = 2A, dtheta/ds = C/Phi_P^2,
dA/ds = 1 - C = M; strict non-peak push: dPsi/ds' = -2 nu_k, dtheta/ds' = -rho_k M/Phi_P^2, dA/ds' = rho_k M = |w(k)|;
det = rho_k M (M + C)/Phi_P^2 = rho_k M/Phi_P^2.  Numerics (jac_check2.py, central differences, 1169 random blocks,
steps chosen inside the peak-set-constant region): max relative entry error 4.7e-7, det ratio 1.000000.
(qb_jac_check.py's first, forward-difference version showed "errors" only for steps below double precision.)
