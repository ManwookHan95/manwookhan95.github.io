# X1-ref part 1 — Lemma K, Lemma F, Remark 1.3, Lemma EC

Notation of U1 / U1-ref / X1.  For a block (index m) of a first row: zeta = R_m^** zhat, A = |zeta|_m, M + C = 1, theta = AM/C,
nu_k = |zeta(k)|/Phi_k^2 = m |u_k(zhat)|/Phi_k (since zeta(k) = lambda_k u_k(zhat), lambda_k = m Phi_k), rho_k = nu_k/theta,
P = {rho >= 1}, Q = complement.  For a finite set Omega of carriers of the block, U1 Lemma 1.3 DEFINES
     kappa(Omega) := [ A(A + theta) - sum_{k in Omega} nu_k^2 Phi_k^2 ] / theta                                  (formula 1)
and proves kappa(Omega) = A + theta Phi_P^2 + S_f/theta, S_f = sum_{Q \ Omega} nu^2 Phi^2, WHEN Omega ⊂ Q            (formula 2).
r_l := u_l(zhat)/kappa(Omega), R^2 := m^2 sum_{Omega} r_l^2, a := A/theta, k := kappa/theta.

## 1. Lemma K.  Verdict: CORRECT (re-derived; independent numerics).
Re-derivation.  (E2) of U1 Lemma 1.2 divided by theta^2: a^2 = Phi_P^2 + sum_Q rho^2 Phi^2 = sum_{all k} Phi_k^2 min(rho_k, 1)^2 (the uniform
form).  With Omega ⊂ Q: sum_Omega rho^2 Phi^2 = sum_Omega (m |u|/theta)^2 = k^2 R^2, so a^2 = sigma + k^2 R^2 with sigma := Phi_P^2 + s_f,
and formula 2 divided by theta gives k = a + sigma.  Eliminating a: (1 - R^2) k^2 - 2 sigma k + sigma^2 - sigma = 0; discriminant /4 equals
sigma^2 R^2 + sigma (1 - R^2) > 0.  The smaller root k_- satisfies k_- <= sigma iff sigma R^2 <= sqrt(sigma^2 R^2 + sigma(1 - R^2)), i.e.
0 <= sigma (1 - R^2)(1 + sigma R^2): true; it would give a = k_- - sigma <= 0, excluded by a = A/theta > 0.  (R < 1 is Lemma R-kt.)  Hence
k = K(sigma, R^2).  Monotonicity in sigma: numerator increasing, denominator fixed.  In x = R^2 at fixed sigma: differentiate a^2 = sigma + k^2 x,
a = k - sigma: 2a k' = 2 k x k' + k^2, k' = k^2/(2(a - k x)) > 0 because a > k R >= k R^2 (a^2 = sigma + k^2 R^2 > k^2 R^2, R < 1).
The relative position rho_l = nu_l/theta = m |r_l| kappa/(Phi_l theta) = m |r_l| k/Phi_l is the definition (valid for EVERY carrier l, whatever
Omega is).
Numerics (r9/X1_ref_work/indep_block.py, NEW independent solver: bisection on the threshold equation derived from (E1), (E2), 60 digits,
not the fixed-point solver of status_rigidity.py used by U1-ref and X1): 99 random blocks, k = K(sigma, R^2) and rho = m|r|k/Phi to 3.0e-61,
a^2 = E to 5.5e-61; the minus root is always <= sigma; K increasing in sigma and R^2 on grids.  The solver itself was cross-checked against a
direct convex computation of the dual norm (cvxpy/CLARABEL: maximize <w, zeta> s.t. ||w||_inf + ||D w||_2 <= 1): A to 1e-11 relative,
M and C to 1e-8, the off-peak duality-map entries w(k) = C zeta(k)/(Phi_k^2 A) to 1e-5 (cvx_check2.out; the last entries are weakly
determined by the convex program, solver tolerance).

PRECISION K1 (convention; needed later).  Formula 2, hence Lemma K in the form k = K(Phi_P^2 + s_f, R^2), requires Omega ⊂ Q.  If Omega
contains carriers that are (weak) peaks of the row — as happens for the active weak peaks of f, which belong to the pattern's Omega because they
are pushed inward at the companion — then with formula 1 one gets, by the same computation,
     a^2 = sigma' + k^2 R^2,   k = a + sigma',   sigma' := Phi_{P \ Omega}^2 + sum_{l in Omega ∩ P} (1 - rho_l^2) Phi_l^2 + s_f,
so Lemma K holds with sigma' in place of sigma; for weak peaks (rho_l in [1, 1 + b]) the correction is in [-3b Phi_l^2, 0].  The ratios must
therefore be computed with formula 1 and the PATTERN's Omega (U1's definition).  In the "peak convention" (kappa computed with the weak
peak in P) the ratios of the whole block differ by a relative amount of order Phi_l^2/k, which is NOT small: weakpeak_ref.py finds relative
kappa differences 0.7% ... 7% between the conventions, while in formula 1 the active statuses differ from the floor by 0.54 b (b = 1e-2,
1e-3, 1e-4).  X1's sentence "active weak peaks contribute Phi^2 as peaks and rho^2 Phi^2 = (1 + O(b)) Phi^2 as Omega members" is correct
only in the formula-1 convention; with that reading 2.1(T) and 2.2(ii) hold as stated.

## 2. Lemma F (floor lemma).  Verdict: CORRECT (elementary consequence of Lemma K; numerics).
Statement as proved: let P_rob ⊂ P (peaks of the row), Omega_a ⊂ Omega ⊂ Q, ratios computed with kappa(Omega).  Then for l in Omega_a
     rho_l = m |r_l| K(sigma, R^2)/Phi_l >= m |r_l| K(sigma_rob, R_a^2)/Phi_l = rho^0_l,
because sigma = Phi_P^2 + s_f >= Phi_{P_rob}^2 = sigma_rob and R^2 >= R_a^2, and K is increasing in both arguments.  Equality iff
P = P_rob, s_f = 0 and r = 0 on Omega \ Omega_a.  The words "(up to the fine terms ...)" in X1's statement are superfluous: fine terms only
increase sigma.  (With a weak peak in Omega the inequality holds up to the O(b) correction of K1; irrelevant below.)
Consequence (i) (a lever created or tuned at a companion cannot bring an active status below the floor at fixed active ratios): PROVED, it is
the inequality.  (ii) "(KN_{w,a}) iff an inactive coarse carrier with rho in [u, 1 + b]": definitional (U1-ref 3.2 plus the remark that an
inactive near-threshold peak can be pushed inward first) — correct.  (iii) correct reformulation.
Numerics (floor_ref.py, independent solver): 400 random blocks with random inactive masses (nearly neutral, robust and near-threshold) at
fixed active ratios: every active rho >= floor; equality case exact to 8.5e-41.  New quantitative facts: (b) nearly neutral inactive
carriers at relative position b raise the active statuses only by O(b^2) (ratio to b^2 constant 0.01 for b = 1e-2, 1e-3, 1e-4): they enter
R^2 through rho^2 Phi^2/k^2; (d) the (U)-block rescaling r -> s r lowers every active rho by a factor <= s (checked, s = 0.99).

## 3. Remark 1.3 (designed levers).  Verdict: facts plausible, conclusion HEURISTIC as labelled; NOT needed for anything below.
(a) is correct (capacity of a fine lever <= theta c_{L+1}^2).  (b) is a counting heuristic.  (c) (siblings) I did not re-derive the constants
[rho_d/5, 4 rho_d/5]; it plays no role in the proofs.  The positive content of Section 1 is Lemma F; the negative answer "private levers cannot
make (KN) automatic" is PROVED only in the precise sense of Lemma F (no move at fixed active ratios beats the floor), as X1 says.

## 4. Lemma EC (effective columns).  Verdict: CORRECT, with two precisions.
L(Delta', gamma) = sum_{Omega} gamma_l u_l|_{E_c} - sum_m Delta'_m tau_m (U1 2.1, peaks enter with coefficient gamma_p = lambda_p(0 - Delta_m vs_p M) =
-Delta'_m lambda_p vs_p, U1 Lemma 1.1(a)); inserting (X3)_m / kappa_m, Delta'_m = sum_{Omega_a(m)} r_l gamma_l (inactive gamma = 0 by (X5)) gives
L = sum_{Omega_a} gamma_l (u_l - r_l tau_{m(l)}).  Precisions: (EC1) in blocks with Delta'_m := 0 by (X5) the row (X3)_m becomes the
CONSTRAINT sum r_l gamma_l = 0 (no elimination); (EC2) "the weights of the Omega carriers do not occur" refers to (X1)-(X3), (X5): U1-ref's
inward row (X4) contains 1/lambda_l (this is exactly what X1's (X4^0) removes, Section 2).
