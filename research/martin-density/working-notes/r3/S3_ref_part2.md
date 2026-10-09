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
