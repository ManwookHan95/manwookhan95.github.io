# S3 referee notes (assembled): verification of S3 with full proofs of all fixes

Setting: canonical base q, Martin's norm with FINITE block set I (p_N; Preprint B Remark martin-tail), admissible T (Lemma B's conclusion only).
Object refereed: ctx/r3/S3_notes.md (identical to S3_head + S3_part1..4 + S3_tail). Report with verdict table: ctx/r3/S3_referee.md.
Referee scripts: ctx/r3/S3ref_work/ (thmB_check.py, thmB_small.py: independent SOCP test of Theorem B; rplus_indep.py: Lemma R+).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## Summary of results
 * CORRECT (re-derived): Lemma 1.1 and Lemmas 1.2-1.3; Theorem A; Theorem B (Fenchel duality, any contact set K); Corollary B2 (f in R at P1's
   example); Lemma R+; Theorem D (first-order rebalancing, no steering); Corollary D1 (Delta d >= 0 two-piece mates, F finite, no further hypothesis).
 * CORRECT WITH FIXABLE GAPS: Corollary D2 and Prop 4.2 (circular |C' - C| = O(s_1) estimate, repaired by Lemma F1; common sequence of scales F2);
   4.5 (needs a regularity hypothesis on Phi, Proposition F3 shows Lemma B does not give it; result already in A_notes 7.4).
 * OVERSTATED: 4.3's "rho-defect only" (needs K^scr < infinity; Remark F4); 4.4's "simplified approximants do not recover" (only a sufficient
   condition fails: HEURISTIC/OPEN); open-core list omits F infinite (a not in c_00).
 * NUMERICS: finite analogue of Theorem B confirmed by an independent solver for certificate and NON-certificate directions on both sides;
   onset-scale phenomenon documented (gamma^+- is reached only below min gap/|omega| of the optimal decomposition).
 * Most valuable idea: first-order rebalancing (linear first-order mismatches are pure level shifts, removable at cost mismatch x inefficiency,
   inefficiency fixed before the mismatch scale) — with Theorem B's duality it reduces F-finite recovery to existence of two-piece data and the
   Delta d < 0 scrambling quantity.
 * Density of NA((c_0,p), l_2^2): still OPEN; nothing points to a counterexample.

# S3 referee, part 1: Lemma 1.1 (rebalancing add-on), Lemma 3.2 (R+), first pass on Theorem B and Theorem D

Setting checked: finite block set I (p_N), canonical base, admissible T (Lemma B conclusion only). Notation of S3_notes.

## 1.1 Lemma 1.1 (rebalancing add-on). Verdict: CORRECT (line-by-line re-derivation).
(i) lowering, y = s'1_{L'} + Lambda e_{k*}, eps >= 0.
 - k in L' \ {k*}: |w'(k)| >= gamma, |V(k) - w'(k)| <= eta < gamma (eps(2+Lambda) <= gamma - eta forces gamma > eta when eps > 0),
   so sign V(k) = s'(k) and |V(k)| >= gamma - eta >= eps; hence |V(k) - eps s'(k)| = |V(k)| - eps <= ||V|| - eps.
 - k*: upper bound trivial (Lambda >= 0); lower bound V(k*) + ||V|| >= 2(gamma - eta) >= eps(2 + Lambda). OK.
 - k notin L': |V(k)| < gamma + eta, and ||V|| >= V(k*) >= M' - eta, so need gamma + 2eta + eps <= M': true from
   eta, eps <= (M' - gamma)/4. OK.
(ii) raising: same, with V(k*) + ||V|| + e(2 - Lambda) >= 2(gamma - eta) - e(Lambda + 1) >= 0. OK.
(iii) elementary (sqrt(A^2 + x) <= A + x/(2A); the 4|a-b||y|/|b| bound uses |a| >= |b|/2). OK.
(iv) bookkeeping. Needs ||alpha'||_1 = 1 exactly: true (if R x'/sigma' = x_0 + D b with ||x_0||_1, ||b|| <= 1, then
   1 = w'(x_0) + <Dw', b> <= M' ||x_0||_1 + C' ||b|| <= 1 forces ||x_0||_1 = 1 when M' > 0, b = Dw'/C'). Then
   y(R x') = sigma'(1 +- Lambda |alpha'_{k*}|) + sigma'<Dw', Dy>/C' and sigma'|alpha'_{k*}| = m Phi_*(u_*(x') - theta' Phi_*). OK.
(v) algebra: R_m* y = (Y'/c') a' + e' with e'(x') = 0; q*(lambda_A a' + tau B + sum eps e') <= lambda_A q*(a' + (tau/lambda_A)B) + sum|eps| q*(e'). OK.
Remark: the inefficiency is always a COST in both directions (lowering: +eps Lambda m Phi mu'/c' added to the base; raising:
eps < 0 and Y' = sigma' e'_y - Lambda m Phi mu', so the base again gets +|eps| Lambda m Phi mu'/c'). Checked.
Valid at a non-NA f with xi in place of x' (A Fact C at the normer is all that is used). OK.

## 1.2 Lemma 1.2 / 1.3 (transfer data, persistence). Verdict: CORRECT.
Key points checked: tau_* := -(R*(s 1_L) - (R*(s 1_L)(xi)/q_0) a) has tau_*(xi) = 0, so the target T = tau_* + delta_0 q*(tau_*) a has
T(xi) = delta_0 q_0 q*(tau_*) > 0 and a deep u_{k*} ~ T/q*(T) is a positive peak with margin ~ delta_0 q_0 (density of every tail);
Lambda m Phi_* = q*(T) is BOUNDED independently of the inefficiency target (q*(tau_*) <= 2 sum_k m Phi_m(k) q*(u_k)), so the
"exchange-rate" terms Y'/c' are bounded independently of eta_1 — this matters for Theorem D (K_l, K_tr independent of eta_1).
Lambda Phi_*^2 = q*(T) Phi_*/m -> 0, so e_y -> e^0_y. Persistence: coordinatewise convergence of w' plus |w(k)| != gamma for all k
and dominated convergence (majorant m Phi_m(k) q*(u_{k,m})). OK.

## 1.3 Lemma 3.2 (R+). Verdict: CORRECT (constant in the displayed intermediate bound is loose but the final bound holds).
Re-derived: ||y||_inf <= M' - gamma (S_1: |y| = 2M' - M = M' - gamma; S_2: <= M' - |gamma|; A: <= M' - gamma_+).
||Dy||^2 = 2C'^2 - C^2 + ||D(w'-w)||^2 + ||DY||^2 - 2R_A and 2(C+gamma)^2 - C^2 = (C+2gamma)^2 - 2gamma^2. OK.
X-bound: the note writes ||DY||^2 <= 2||D(w'-w)||^2 + 2(...)||Dw'1_A||^2, which with the stated |R_A| bound gives only
X <= 4||D(w'-w)||^2 + 5||Dw' 1_A||^2 (M' close to 1 in Martin's blocks, so 5M'^2 > 4). But Y has DISJOINT pieces on S and A, so
||DY||^2 = ||D(w'-w)1_S||^2 + (gamma_+/M')^2 ||Dw'1_A||^2 and then X <= 3||D(w'-w)||^2 + 4||Dw'1_A||^2 <= 4||D(w'-w)||^2 + 4 sum_A Phi^2.
So the stated final bound is TRUE (cosmetic fix: use disjointness). gamma_+/M' <= 1 needs C <= 2/3: fine (C_m <= 2^{-m}).
Consequence (E_y bound): <y - w', R x'> >= -sum_A |Rx'(k)|(|w'-w| + gamma_+) uses Bx = <w'-w, Rx'> >= 0 (w' norms Rx'). OK.
Numerical re-check: see part 2 (independent script).

## 1.4 First pass on Theorem B upper bound. Verdict: CORRECT.
Base: ||a + tb||_1 = ||a||_1 + t b(z) for 0 < t < min_F|a_j|/||b||_inf uses b vanishing off F cup K and z_j b_j = |b_j| on K. OK.
b(zhat) = 0 uses A Lemma 4.2 (<omega - d w, zeta_m> = 0 for omega supported off peaks). Re-derived: zeta_m = sigma_m(alpha + D^2 w/C),
<omega, zeta> = sigma d, <w, zeta> = sigma (M + C) = sigma. OK.
Block: N(w + t(omega - d w)) first-order term -dM + (d - dC) = d(1 - M - C) = 0. OK.
Rebalancing at f (no engineering): all blocks, including omega_m = 0 blocks (which ABSORB level via raising), equalised at
Lev = Gamma_w/2. Elimination verified: q_0 h/2 + sum sigma_m H_m/2 = Lev (q_0 + sum sigma_m) = Lev.
# S3 referee, part 2: Theorem B (lower bound / duality), Corollary B2, numerics

## 2.1 Theorem B lower bound — line-by-line. Verdict: CORRECT (given the refereed C Prop 8.1 (ii), (v)).
Step 1 re-derived: k_2 = kappa'_2 e + k_{2,perp}, Gram system on E_F (U* injective => Gram invertible), <k_{2,perp}, e> = 0 uses
||a||_1 + nu = 1; <e,k_2> = kappa_2 - ||k||^2/(2q_0) checked; Z_{t,j} = (q_0 + t^2 kappa_2) sign a_j on F; off F, Z_{t,j} = q_0 z_j + t nu_{c,j}
(the U k movement is absorbed in the Hilbert part H_t, so contacts in K are NOT moved by U k — this is why infinite K is harmless
for the test points). q**(eta_t) <= max(||Z_t||, ||H_t||) is the Minkowski-sum gauge. a(eta_t - xi) = t<U*a,k> = 0. OK.
Step 3: (f+tg)(eta_t)/p**(eta_t) = 1 + t^2 g(nu) - Delta(eta_t) + O(t^3) (numerator O(t^2), p**(eta_t) = 1 + O(t)). OK.
Step 2 (block expansion along t delta_1 + t^2 delta_2): with Q_m finite, C Lemma 5.1 makes |.|_m locally the function
Lambda(S_P(y), ||D^{-1} y_Q||) of |Q_m| + 1 variables; peaks crossing their threshold are controlled by the overshoot bound
(C Lemma 5.2), which costs <= 2 sum_{P: mu_k <= O(t)} O(t) Phi_k = o(t^2) under (MS); the first-order terms (including the t^2 delta_2 term)
cancel because grad Lambda = w in the reduced variables (dLambda/dS = M, dLambda/dY = CY/|z|). I re-derived this; it is what C_referee
1.20 lists as correct. OK.
Step 4 (Fenchel): Rockafellar Thm 31.1 condition (a) (ri dom Qf = R^n meets ri dom Psi, Psi proper concave since Psi(0) >= 0 and the
+infinity case is treated separately); closedness is NOT needed under (a); the dual minimum is attained. Conjugates re-derived:
 - -Psi_*(lambda) = sup_k [2<P_perp U*beta,k> - (nu/q_0)||k||^2] + sup_{nu_c in C_+} 2 beta(nu_c), separable; = q_0 h(beta) on side-+ admissible
   beta, +infinity otherwise (dual cone of C_+ inside l_1). OK.
 - Qf_m^*: <lambda_m, ell_m(nu)> = 2 v(R_m nu) with v = omega~ + c w_m, omega~ supported on Q_m (on P_m, v = (lambda_P/2) s_k = c w_m(k)). The
   kernel of the PSD form Qf_m is exactly the radial line R ell_m(zeta_m) (Lemma 5.1 Hessian: (C/|z|)||P_{h0-perp}D^{-1}delta_Q||^2 +
   (Lambda_SS/Y^2)(Y sigma_1 - S sigma_2)^2, kernel = {delta ~ zeta}; degenerate case z_Q = 0: E = C||D^{-1}delta_Q||^2/(2|z|), kernel = S-axis = radial).
   Hence Qf_m^* finite iff v balanced (c = -d(omega~)), and then = sigma_m H_m(omega~). I re-checked the degenerate case by hand:
   M = 1/(1+sqrt F2), C = sqrt F2/(1+sqrt F2), S = sigma/M, Hb = C delta_2^2/(sigma Phi_2^2), sup_delta [2 omega_2 delta_2 - Hb] = sigma Phi_2^2 omega_2^2/C = sigma H.
 - Weak duality (elementary direction) also re-derived: b(nu_c) <= 0 on C_+ for side-+ admissible b. OK.
Every step is either elementary or one of the refereed items (C Lemma 5.1, 5.2, Prop 8.1 (i),(ii),(v)). Decoupling (C Prop 8.1 (iii)) is
indeed not used: the dual variable ranges over ALL lambda in R^n and the primal test set need not reach every value of ell — Fenchel
duality handles a non-surjective ell automatically (Psi = -infinity off its range). This is the genuine improvement over C.
Statement (c): g in C(f) => p*(f+tg) <= s(t) = 1 + t^2/2 + O(t^4) => gamma^+- <= 1; minimisers exist by (b), finitely supported on Q_m. OK.
Small remark: the theorem is stated for g in l_1 with g(xi) = 0; for g(xi) != 0 the one-sided limits are +-infinity on one side — irrelevant.

## 2.2 Corollary B2 (P1's example). Verdict: CORRECT.
(BT) at P1's f: F = {1}; Q_1 = {2}, Q_m = empty (P1 2.2(b), refereed); P1 6.0 margins mu >= q_0 min(1/4, 2 sqrt Phi) (re-read: non-exceptional
k >= 2: mu >= 1.5 q_0 rho_l >= 2 q_0 sqrt(Phi); exceptional and k = 1: mu >= q_0/4), so no degenerate peaks; (MS): mu < s < q_0/4 forces
Phi < s^2/(4q_0^2) and Phi_m(k+1) <= Phi_m(k)/2 (c_l decreasing along k because l(n,m) increasing in n), sum <= s^2/(2q_0^2) = o(s); finite I.
Side decompositions: omega_1 = (mu/lambda_0) e_2, d = 0 (w_1(2) = 0), H_1 = mu^2/C_1 (m = 1, Phi_1(2) = lambda_0); g in C(f) is supported in
{1} cup K' (P1 6.1) and u > 0 on K', so side-+ admissibility is exactly mu <= inf theta(g) (side -: mu >= sup theta(g)). Phi_g strictly
convex in mu => minimisers mu+- exist; gamma+- <= 1 by Thm B(c); Delta d = 0, one active block => Theorem A (or D) applies. Since the
weighted value q_0 h + sigma_1 mu^2/C_1 <= 1 is what Thm B gives, and P1 6.3 needed the max-form <= 1/rho^2, B2 genuinely closes P1's
remark "recovery of all of C(f) ... not proved". (If mu+- = 0, omega = 0 and the side is a pure base side; Theorem A covers v = 0 too.)

## 2.3 Numerical check of Theorem B. Verdict: CORRECT as reported (re-run reproduces the table), with one unreported line.
Re-ran S3_work/gamma_side.py (cvxpy): free coordinates gamma+- = 0.29824 = Gamma_w(cert); all kinks gamma+ = 0.29567, gamma- = 0.28325
vs the C referee's exact one-sided coefficients 0.29567/0.29568 (t = 3e-4, 1e-4) and 0.28325/0.28324 — 5-digit agreement on both sides.
Nature of the check: the C referee's numbers come from a direct ellipsoid-method computation of p*(f + t g) (Cref_work/kinks_*.py), so this
is a genuinely independent confirmation of the finite-dimensional ANALOGUE of the duality formula (in the finite model the transfer is
provided by a non-peak coordinate with u proportional to pi(xt) a - pi, which makes base/block exchange exactly efficient at second order).
It does not test the infinite-dimensional parts (transfer peaks, (MS), overshoots), which are handled analytically.
Unreported: the script's third case ("kinks opposite signs") prints gamma+ = 0.626 > Gamma_w(cert) = 0.520. This is NOT a contradiction:
there Q = [5] and k_0 = 1 has become a peak, so the "certificate" is not a valid decomposition and g need not even satisfy g(xi) = 0.
The notes do not quote this case; fine, but the script output should carry a warning.
Independent re-check of the exact coefficient with a different solver: see part 3.
# S3 referee, part 3: independent numerical test of Theorem B (finite analogue), beyond certificates

Script: ctx/r3/S3ref_work/thmB_check.py and thmB_small.py. Same finite model as the C referee / S3 (seed 21, n = 6, d = 3, one block
with 5 coordinates + transfer coordinate), but p* computed INDEPENDENTLY as the SOCP p*(h) = min_W max(q*(h - R^T W), N(W)) (exact
formula, since B_{p*} = B_{q*} + L*(B_{V*}) is a Minkowski sum), solved with Clarabel at tolerance 1e-14 (p*(f) - 1 = 5e-15 in the
kink model). gamma^+- computed by the QP of 2.2 (side-admissible omega in R^Q).

Results (kink model, every off-support coordinate a contact):
| g | side | gamma (QP) | exact 2(p*(f+tg)-1)/t^2 at |t| = 2e-3, 5e-4, 1e-4 |
|---|---|---|---|
| C-referee certificate | + | 0.29567 | 0.35981, 0.29567, 0.29588 (precision drift at 1e-4) |
| C-referee certificate | - | 0.28325 | 0.28323, 0.28325, 0.28325 |
| random g, g(xi) = 0 (rand0) | + | 1.10419 | 1.97333, 1.25569, 1.10425 |
| random g, g(xi) = 0 (rand0) | - | 1.75850 | 84.315, 28.829, 1.75872 (and 1.75852 at 2.5e-5) |
Free-coordinate model: certificate 0.29824 both sides (Richardson 0.29825); random g are side-infeasible (gamma = +infinity) and the
exact coefficients blow up like 1/|t| (8.6, 15.1, 27.6 at t = .02, .01, .005), as Theorem B predicts.

Conclusions.
 (1) The finite analogue of Theorem B holds for NON-certificate directions too (random g with g(xi) = 0, both sides, asymmetric values,
     infeasible sides): strong independent evidence that the duality formula is right.
 (2) ONSET SCALE: the exact coefficient reaches gamma only for |t| below the radius min_k gap_k/|omega_k| of the OPTIMAL side
     decomposition (here the transfer coordinate k = 5 with Phi = 0.45^10 carries omega_5 ~ 800-2400, radius ~3e-4). Above that the
     coefficient can be 50 times larger (rand0, side -). This is harmless for Theorem B (a limit) and for Theorem D (T_0 is chosen after
     the data are fixed), but it means "gamma^+- <= 1" says nothing about any FIXED scale; any argument needing uniformity of the
     second-order behaviour across a family of points/data (O3, averaging over scales, generic supports) must not use gamma as if it
     were attained at a data-independent scale.
# S3 referee, part 4: Theorem A, Theorem D (first-order rebalancing), D1, D2, Prop 4.2, Lemma R+ numerics

## 4.1 Theorem A / Cor A'. Verdict: Theorem A CORRECT; Cor A' correct in outline (superseded by D, not re-checked line by line).
Theorem A = P2A Thm 2.1 (refereed) + second-order equalisation through Lemma 1.1. Checked: block pieces V_m = w'_m + tau rho(omega - d'w')
satisfy ||V - w'|| <= K_1|tau|; the T_0-constraints make Lemma 1.1(i)/(ii) applicable with the (huge but FIXED) Lambda; the base no-flip
estimates of P2A Step 5 survive the rescaling s = tau/lambda_A (factor-2 margins, lambda_A in [0.99, 1.01]); the theta piece gets
Lev_theta = Gamma_w(b^theta, omega^theta)/2 <= kappa_w/2 by convexity of Gamma_w. Order of choices: delta -> eta_1 -> transfer data -> T_0
-> (N, s_1, ...). OK.

## 4.2 Theorem D. Verdict: CORRECT for Delta d_m >= 0 (no extra hypothesis) and, under (SC_m), for Delta d_m < 0.
Re-derived:
 * Bookkeeping 3.1: g'(x') = B(x') + sum Omega_m(R_m x') = c' l_b + sum sigma'_m l_m; G_b, G_m >= 0 (A Lemma 7.2; subgradient R_m x'/sigma' of N_m at w').
 * Theta piece: c = g''(xhat') = (b^theta 1_[1,N])(xhat') (the block terms vanish since d'^theta is the f'-coefficient), so l^theta_b = 0 and
   l^theta_m = 0 EXACTLY; window masses cover |tau| <= s_1 (no flips, no kinks). So no first-order term at scales below s_1. OK.
 * Side pieces: B^+ = B^theta + rho theta v, B^- = B^theta - rho(1-theta)v, beta^+- as in P2A; Omega^sigma decomposition
   rho(omega^sigma - d'(omega^sigma)w') + kappa^sigma w' + rho c^sigma(w' - w), with c^+ = -theta Delta d, c^- = (1-theta)Delta d. Algebra checked.
 * Linear terms: l^sigma_b = rho theta v(xhat') resp. -rho(1-theta)v(xhat'), v(xhat') = -V_{>N''} + <U*v, e' - e> = O(s_1); l^sigma_m =
   kappa^sigma + rho c^sigma c' Bx_m/sigma', kappa^sigma = rho (d' - d)(omega^sigma - omega^theta) = O(s_1 + tail). The constant K_l does NOT
   depend on eta_1 (I checked: Lambda m Phi_* = q*(T) is bounded independently of eta_1, cf. part 1), so choosing eta_1 BEFORE s_1 is legitimate.
 * Convexity case (s = tau rho c^sigma <= 0, i.e. both sides when Delta d_m >= 0): W = (1-|s|)V_1 + |s| w, N(w) = 1, genuine cost
   rho^2 tau^2 H'/2 + |s| c' Bx/sigma'. Bx_m = <w' - w, R xhat'> in [0, sum_k lambda_k |w'-w|(k)(K_e s_1 + t_k)] = o(s_1) by dominated convergence
   (w' -> w coordinatewise along the sequence, P2A Lemma 1.2). OK.
 * Anchor case (s > 0): W = (1-s)V_1 + s y, s Z_A moved to the base; G(W) <= rho^2tau^2H'/2 + s E_y with E_y = N(y) - <y, Rx'>/sigma' >= 0. OK.
 * First-order rebalancing (Step 6): eps_m = tau l_m/e'_y + t_m rho^2 tau^2; the bracket tau(l_b + sum sigma'_m l_m/c') vanishes by 3.1; what is left
   is |tau| |l_m| x (transfer inefficiency) = O(|tau| s_1 eta_1) <= eps_0 tau^2 for |tau| > s_1. Lemma 1.1's radius condition
   |eps|(2 + Lambda) <= gamma - eta holds because |eps^(1)| <= T_0 K_l s_1 -> 0 with Lambda fixed. Error terms of Lemma 1.1(iii):
   O(|eps||tau| ||Dy||/C') with ||Dy|| bounded independently of eta_1 (Lambda Phi_* = q*(T)/m). OK.
 * The essential new point is sound: a LINEAR first-order mismatch between pieces of an exact decomposition is a pure level shift and can be
   moved through transfer peaks at a cost proportional to (mismatch) x (inefficiency), the inefficiency being fixed before the mismatch scale s_1;
   only the theta piece (exactly balanced) is used below s_1. This is why steering (far pulls, IVT tuning, (S), (TC), (TT), (BR)) is unnecessary.
Minor presentation issues (no effect): K_tr as written mixes the bounded exchange rate with the inefficiency; what is needed (and true) is
"rebalancing cost <= |eps| (Lambda m Phi mu'/c' + q*(e'_m))" with the bracket <= 2 eta_1 at late stages.

## 4.3 Corollary D1. Verdict: CORRECT.
Nothing about Q_m, K, degenerate peaks or rates of T is used: the deep structure enters only via (E4)-(E5), which hold for every f with F finite.
(The two-piece data themselves are finitely supported in the blocks — that is where the restriction lies; D1 does not say that mates at
generic supports HAVE such data.)

## 4.4 Corollary D2. Verdict: CORRECT, with one fixable circularity in the auxiliary rate |C' - C| = O(s_1).
D2 = Theorem B (optimal two-piece data, kappa_w <= 1) + Theorem D + (SC) under (BT). Checked (SC): ||D(w'-w)||^2 <= sum_k min(K^2(s_1+t_k)^2, 4Phi_k^2)
= O(s_1^2 log(1/s_1)) + (tail made <= s_1^2; note sum_k t_k^2 itself may diverge — the min with 4Phi_k^2 is essential, as written);
A_m within {peaks with mu_k <= K'(s_1 + t_k)} under (BT) (finite Q with gaps >= gamma_0); (MS) and dominated convergence give o(s_1).
GAP (fixable): D2(i) and Prop 4.2(a) use a Lipschitz bound Phi_k|w'(k) - w(k)| <= K_0(s_1 + t_k) whose constant needs |C' - C| = O(s_1), while
Prop 4.2(b) derives |C' - C| = O(s_1) FROM that bound (circular as written). Fix: C is the unique root of the strictly decreasing
F(C; v) := sum_k min(Phi_k(1-C)/C, v_k)^2 = 1, v_k := m|u_k(.)|/|R .|; |F(C; v') - F(C; v)| <= (2(1-C)/C) sum_k Phi_k |v'_k - v_k| = O(s_1) + o(s_1^2-tail)
by (E2)/(E4), and |dF/dC| >= 2 Phi_*^2 (1-C)/C^3 > 0 near the root as long as one fixed peak with positive margin (e.g. a transfer peak) stays
active; hence |C' - C| = O(s_1) with no hypothesis. After this, (a) and the rest go through. C Thm 8.4 is contained ((T4) = (MS) is part of
C-tameness, checked in C_notes Def 6.0).

## 4.5 Prop 4.2 ((MS-Q*) => (SC)). Verdict: CORRECT with two small fixes.
 (1) The circularity above (same fix).
 (2) "Consequently (Theorem D): if every block with Delta d_m < 0 satisfies these conditions ..." needs ONE common sequence of scales s_1
     for all such blocks: with a liminf-type hypothesis per block the good scales of different blocks can be disjoint (Scr_m is monotone,
     so goodness transfers only within bounded scale ratios). State the hypothesis along a common sequence, or with lim instead of liminf.
 (d) of the proof bounds Phi_k^2 by 3m min(Phi_k, K_0(s_1 + t_k)): this needs Phi_k <~ s_1 on A_m, which follows from the hypothesis
     (a scrambled coordinate with Phi_k >= K s_1 contributes K s_1 to Scr_m(K s_1) = o(s_1), so there are none at late stages). Cosmetic.

## 4.6 Lemma R+ numerics. Independent test (S3ref_work/rplus_indep.py): 17076 random/adversarial blocks (5-40 coordinates, flipped peaks,
created peaks, perturbations 1e-4..0.5, 3615 cases with C' > C): max N(y) - bound = 0.0, max X - (4||D(w'-w)||^2 + 4 sum_A Phi^2) = -1.4e-13.
# S3 referee, part 5: 4.3 (quantitative), 4.4 (failure of (MS-Q*)), 4.5 (deep coefficients), global checks

## 5.1 Section 4.3 (quantitative recovery without (SC)). Verdict: the implication is CORRECT; its interpretation is OVERSTATED.
Implication re-derived: on the wrong side the genuine cost is s E_y + 2 s ||R*Z_A||_1 with s = tau rho c^sigma, |c^sigma| <= |Delta d|/2, hence
<= rho (|Delta d|/2) K^scr tau^2 (1 + o(1)) for |tau| >= s_1; each genuine cost sits in one piece, so the max of the levels gets at most
the SUM of them (on a fixed side they are upper-bounded by linear functions of tau and could even be AVERAGED with the weights c', sigma'_m
by first-order rebalancing, which only improves the threshold). With K^scr := limsup (E_y + 2||R*Z_A||_1)/s_1 the condition
rho^2 kappa_w + rho sum |Delta d_m| K_m^scr < 1 suffices; the stated factor 8 is conservative. OK.
Overstatement: "the non-recovered part ... is confined to rho close to 1: rho-defect only" needs K_m^scr < infinity. The note's sufficient
condition ("non-peak gaps bounded below off a finite set") controls only the NON-PEAK part of Scr_m. The PEAK part
sum{min(Phi_k, s) : k in P_m, mu_k <= s} is only O(s log(1/s)) in general (Phi_m(k) <= 2^{-m-k}), and it is ~ (s/2) log2(1/s) if, e.g.,
mu_k ~ 4^{-k} along a density-one (log-counting) subsequence of peaks — compatible with Lemma B, since density of (u_{k,m})_k only
needs a sparse dense subsequence and T can be built after zhat (P1 2.1 technique). Then K^scr = +infinity and 4.3 gives nothing.
Fix: add "(MS) in the block" (then the peak part is o(s)) or state K^scr < infinity as a hypothesis.

## 5.2 Section 4.4 (MS-Q*) can fail. Verdict: the construction is a fair SKETCH; the conclusion about the approximants is OVERSTATED.
 * Failure of (MS-Q*): prescribing u_{2k,1} in zhat-perp (with P1-type signature tails and an e_1*-correction keeping u(zhat) = 0 exactly)
   makes every (2k,1) a strict non-peak with w = 0 and gap M_1, so Scr_1(s) >= c s at every scale. Fine as SKETCH (T-c / P3-type margins
   for the remaining coordinates must be re-checked, as in P1 2.1).
 * Scrambling: u_{2k,1}(xhat') = <U*u_{2k,1}, e' - e> + o(s_1); new peaks wherever s_1 |<U*u, h_N>| >~ theta Phi_{2k}. "A positive proportion"
   needs an equidistribution property of the enumeration of the dense family (arrangeable by construction, not automatic). SKETCH.
 * OVERCLAIM: the head/summary/table say "the simplified approximants then do not recover Delta d < 0 two-piece mates for rho near 1".
   What is shown is only that (SC_1) — a SUFFICIENT condition in an UPPER bound — fails, i.e. Theorem D's estimate does not apply (which is
   what 4.4's body says). Non-recovery along these f'_n would require a LOWER bound dist(rho g, C(f'_n)) >= c > 0 over all targets g'_n, which
   is not attempted. Correct label for that sentence: HEURISTIC (or OPEN).
 * Remark: the unrefereed sibling notes R3 (Theorem EC) convert FINITELY many generic block coordinates into strict non-peaks with w'' = 0 by
   o(1) window moves; 4.4 would need infinitely many (all deep (2k,1) below s_1) at precision ~ theta Phi_{2k} — not covered; the OPEN label stands.

## 5.3 Section 4.5 (deep coefficients c_k ~ sqrt(Phi_k)). Verdict: CORRECT WITH FIXABLE GAPS (missing hypothesis on Phi); not new.
Box tail: k in E(sigma) iff sigma |c_k| > m Phi_k gap_k/2 (the note drops the factor m — harmless); with |c_k| <= K sqrt(Phi_k), gap >= g_0:
E(sigma) within {Phi_k < 4K^2 sigma^2/(m g_0)^2} and T(sigma) <= K sum_{Phi_k < c sigma^2} sqrt(Phi_k).
 * This is O(sigma) only if Phi is regular, e.g. Phi_m(k+1) <= beta Phi_m(k) (the note's parenthetical "geometric Phi"). Lemma B does NOT
   give this: rescaling the columns of T by any 0 < c_{k,m} <= 1 preserves admissibility, so Phi_m(k) = 2^{-m-k} q*(T e_{k,m}) can cluster
   (e.g. ~2j coordinates at level 2^{-j^2}), and then T(sigma) ~ sigma sqrt(log(1/sigma)) and A Cor 6.10(a) does not apply. Martin's own
   Phi_m(k) = 2^{-m-k}|||v*_{k,m}||| is likewise uncontrolled. The hypothesis must be stated (P1's T satisfies it).
 * Further hypotheses that must be kept explicit (they are in the note, not in the claim list): b supported in F (no contact components),
   gaps bounded below on supp omega, and the MAX-form H = max(h(b), H_m) <= 1 (a mate in C(f) need only satisfy weighted-type bounds).
 * "Supersedes C 9.2": correct as a statement about coverage, but A_notes §7.4 ("The borderline case of box tails of exact order sigma:
   RESOLVED", Round 1, refereed) already says exactly this; S3 re-states it.
 * Gamma_w upgrade (SKETCH): plausible. Caveat for whoever writes it: the rebalanced expansion has a radius ~ sqrt(gamma/(t_max(2 + Lambda)))
   that SHRINKS as the inefficiency eta_1 -> 0 (Lambda ~ q*(T)/(m Phi_*) -> infinity); the averaging must therefore be run at fixed eta_1
   (fixed transfer data, radius bounded below) and eta_1 -> 0 taken last. This order works but should be written.

## 5.4 Global adversarial checks (all passed)
 * Hidden assumptions on T: only per-block density of tails (transfer peaks), U* injective (Gram system), Phi_m(k) <= 2^{-m-k}
   (D2(i) log-bound). Exception: 4.5 (Phi regularity), see 5.3. P1's example uses P1's admissible T.
 * c_0 vs l_inf: normers in l_inf only at f (test points, Theorem B); approximants x' = z' + Ue' with z' in c_00. OK.
 * weak* vs norm: f' -> f in norm (P2A Lemma 1.2), g' -> rho g in l_1 (R* w' -> R* w in l_1, beta^sigma -> b^sigma). OK.
 * Uniformity in tau: all estimates hold for 0 < |tau| <= T_0 at late stages with T_0 fixed before (N, s_1, N''); the theta piece covers
   |tau| <= s_1 with NO first-order terms, the side pieces |tau| > s_1 where |tau| o(s_1) <= o(1) tau^2. OK.
 * Attainment: Theorem B attains its minima (Fenchel (a)); D2 uses minimisers. OK.
 * Signs/one-sidedness: s <= 0 on both sides iff Delta d >= 0 (checked); side-- test points need z_j nu_{c,j} >= 0 with t < 0 (checked);
   raising transfers cost the same inefficiency as lowering (checked).
 * Finite vs infinite K: contacts are never moved by the Hilbert part of the test points (Z_t/H_t split), and beyond N'' the side pieces pay
   rho |tau| V_{>N''} <= eps_0 s_1 |tau|. OK.
 * I finite throughout (p_N); Remark martin-tail invoked for p. OK.
 * Consistency with earlier verdicts: C-referee kink phenomenon explained (and reproduced numerically, part 3); P1-referee R3 (canonical
   truncations fail) not contradicted (window masses); N2-referee Lemma R improved (R+), consistent numerically.
# S3 referee, part 6: complete proofs of the fixes

## 6.1 Lemma F1 (|C' - C| = O(s_1) with no hypothesis; removes the circularity in Prop 4.2(a)-(b) and D2(i)). PROVED.
Setting: one block, y in l_1 \ {0}, w = J(y) (N(w) = 1, w(y) = |y|), M = ||w||_inf, C = ||Dw||, M + C = 1, P = peak set.
Clamp formula (P2A Lemma 1.1): Phi_k w(k) = sgn(y_k) min(Phi_k M, C v_k), v_k := |y_k|/(Phi_k |y|). For y = R_m x: v_k = m|u_k(x)|/|R_m x|
(scale invariant in x). Squaring and summing, C^2 = sum_k min(Phi_k M, C v_k)^2, i.e. (divide by C^2, M = 1 - C)
   F(C; v) := sum_k min(Phi_k (1-C)/C, v_k)^2 = 1.                                                    (F)
(i) F(.; v) is continuous and nonincreasing on (0,1). (ii) Since ||alpha||_1 = 1 (part 1, 1.1(iv)), some peak k_* has alpha_{k_*} != 0, i.e.
v_{k_*} > Phi_{k_*}(1-C)/C strictly (positive margin). (iii) Let v' be another datum with |v'_{k_*} - v_{k_*}| small and C' the root of F(.; v') = 1
(the C-datum of y' = R x'). There is a neighbourhood N_0 of C, independent of v' (for |v'_{k_*} - v_{k_*}| <= r_0), on which the k_*-term of
F(.; v') equals Phi_{k_*}^2((1-c)/c)^2, whose derivative is <= -c_* := -2 Phi_{k_*}^2 (1 - sup N_0)/(sup N_0)^3 < 0; the other terms are
nonincreasing. Hence F(c_1; v') - F(c_2; v') >= c_*(c_2 - c_1) for c_1 < c_2 in N_0.
(iv) |min(a, s)^2 - min(a, s')^2| <= 2a|s - s'| for a, s, s' >= 0. So |F(C; v') - F(C; v)| <= (2(1-C)/C) sum_k Phi_k |v'_k - v_k|.
(v) If C' in N_0 (true at late stages, C' -> C by P2A Lemma 1.2): F(C'; v') = 1 = F(C; v), so by (iii)-(iv)
   |C' - C| <= (2(1-C)/(C c_*)) sum_k Phi_k |v'_k - v_k|.
(vi) Along the approximants of S3 3.3: |v'_k - v_k| <= (m/|R xhat'|)|u_k(xhat' - zhat)| + m |u_k(zhat)| | 1/|R xhat'| - 1/|R** zhat| |
<= K(s_1 + t_k) by (E2) and the convexity sandwich of (E4) (which does not use C'). Hence
   |C' - C| <= K'(s_1 sum_k Phi_k + sum_k Phi_k t_k) = O(s_1) + (a quantity -> 0 as N'' -> infinity, made <= s_1^2). QED.
Consequence (Lipschitz bound, Prop 4.2(a), D2(i)): if sgn u_k(xhat') = sgn u_k(zhat),
|Phi_k w'(k) - Phi_k w(k)| <= Phi_k|M' - M| + |C' - C| v_k + C'|v'_k - v_k| <= K(s_1 + t_k); if the signs differ, both |u_k| are <= |u_k(xhat') - u_k(zhat)|
and |Phi_k w'(k) - Phi_k w(k)| <= C' v'_k + C v_k <= K(s_1 + t_k). The constant is uniform in k. This is the input that Prop 4.2(a),(c),(d) and
D2(i),(ii) need; no circularity remains.

## 6.2 Remark F2 (common scales; a logical gap, not a counterexample).
Scr_m(s) is nondecreasing in s. If Scr_m(K s_i) <= eps_i s_i with eps_i -> 0, then Scr_m(K s) <= 2 eps_i s on [s_i/2, s_i]; nothing more follows
from monotonicity. So two nondecreasing functions can each be o(s) along some sequence while their "good" scale sets are disjoint
(e.g. one is small near s = 2^{-j^2}, the other near 2^{-j^2-j}, each increasing steeply in between). Theorem D with several Delta d < 0
blocks needs (SC_m) along ONE sequence of s_1; hence Prop 4.2's "Consequently" is a non sequitur as stated, and must assume a common sequence
(or Scr_m(Ks) = o(s) as s -> 0 in all but one such block). Whether actual blocks of an admissible T can realise disjoint good scales is
irrelevant for the correction.

## 6.3 Proposition F3 (Phi need not be regular for admissible T). PROVED.
If T is admissible and 0 < c_{n,m} <= 1 with c_{n,m} = 1 for some (n,m) with q*(T e_{n,m}) = 1 (or sup c_{n,m} q*(T e_{n,m}) = 1), then
T' := T Diag(c) is admissible: ||T'|| = sup c q*(Te) = 1; T' injective (c > 0); Ran T' is contained in Ran T, so Ran T' cap c_00 = {0} and Ran T' is in Y;
T'e/q*(T'e) = Te/q*(Te), so every tail is still dense. Given any admissible T and any increasing k_0 < k_1 < ..., choosing
c_{k,m} := Phi_m(k_j)/Phi_m(k) for k_{j-1} < k <= k_j gives Phi'_m(k) = Phi_m(k_j) on the j-th cluster (c <= 1 since Phi_m decreases along
k... if not monotone, use min over the cluster). With cluster lengths L_j -> infinity: sum_{Phi'_k < x} sqrt(Phi'_k) >= L_j sqrt(Phi_m(k_j)) at
x slightly above Phi_m(k_j), so sup_x (sum_{Phi' < x} sqrt(Phi'))/sqrt(x) = infinity, and the box tail of A Cor 6.10(a) for |c_k| = K sqrt(Phi'_k)
is not O(sigma) along those scales. So S3 4.5's "O(sigma) box tails when |c_k| <= K sqrt(Phi_k)" needs a regularity hypothesis on Phi
(e.g. Phi_m(k+1) <= beta Phi_m(k), beta < 1), which Lemma B does not supply.
(Remark: the l_1-mass bound used in D2(i), ||D(w'-w)||^2 = O(s_1^2 log(1/s_1)), only uses Phi_m(k) <= 2^{-m-k} and is unaffected.)

## 6.4 Remark F4 (K^scr can be infinite; scope of S3 4.3). SKETCH.
The peak part of Scr_m(s) is sum{min(Phi_k, s) : k in P_m, mu_k <= s} <= s #{k : Phi_k >= s} + sum_{Phi_k < s} Phi_k = O(s log(1/s)) and no better
in general: if mu_k <= 4^{-k} for a set of peaks of positive log-density (e.g. all k outside a sparse subsequence carrying the density of the
u_{k,m}; T built after zhat as in P1 2.1, with |u_{k,m}(zhat)| - theta Phi_m(k) prescribed), then for small s about (1/2)log_2(1/s) peaks with
Phi_k >= s have mu_k <= s and Scr_m(s) >~ (s/2) log_2(1/s). Then K^scr = +infinity is possible and 4.3 gives no threshold. (MS) in the block
excludes this. So 4.3's "rho-defect only" holds under (MS) (+ non-peak gaps bounded below off a finite set), not in general.

## 6.5 Numerical evidence produced by the referee (scripts in ctx/r3/S3ref_work/)
 * thmB_check.py / thmB_small.py: finite analogue of Theorem B confirmed for the C-referee certificate AND for random g with g(xi) = 0
   (both sides, values 1.10419 / 1.75850 matched to 4-5 digits below the onset radius; infeasible sides blow up like 1/|t|). Independent
   SOCP evaluation of p* (Clarabel, tol 1e-14), not the ellipsoid method used by the C referee.
 * rplus_indep.py: Lemma R+ on 17076 random/adversarial blocks, max violation 0.0.
