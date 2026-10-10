# K2 referee, part 1: Lemma K2.1 (tolerance variant), Lemmas K2.2-K2.5

Setting and notation of r11/K2_notes.md.  Sources re-read for this part: r9/X2_notes.md 1.0-1.4, 2.1-2.2, 3.1-3.6 (Theorem UE, Lemma UE-1,
Lemma DC); r10/Q2_notes.md 2.2-2.4, 4.0-4.4; r10/Q2_refa_notes.md B.2, C.1-C.6; r8/U1_notes.md 1.1-1.5.  Labels PROVED / SKETCH / HEURISTIC /
FALSE / OPEN.

## 1. Lemma K2.2 (exact identity).  VERDICT: correct.
Re-derivation.  zhat = z + Ue, so u(zhat) = sum_s u(s) z_s + <U^*u, e> and <U^*u, e> = kappa_u nu by definition of kappa_u.  On F, z_s = sgn a_s
and u(s) = D_u(s) + kappa_u a_s, so sum_F u(s) sgn a_s = sum_F D_u(s) sgn a_s + kappa_u ||a||_1.  Since q*(a) = ||a||_1 + nu = 1 (forced
decomposition), u(zhat) = kappa_u + sum_F D_u sgn a + sum_{F^c} u z.  For (2.1): for s in F, s > D, D_u(s) sgn a_s = u(s) z_s - kappa_u |a_s|;
summing gives -kappa_u alpha(D).  1 - alpha(D) = ||a 1_{[1,D]}||_1 + nu >= nu.  Valid for every bounded U (only <U^*u, e> = kappa_u nu is used)
and for every row (normalized, q*(a) = 1); u in l_1 is needed for absolute convergence.  No gap.

## 2. Lemma K2.3 (resource dichotomy).  VERDICT: correct; a sharper (signed) form holds and is what Section 5 really uses.
If kappa_u >= 0 then kappa_u (1 - alpha(D)) >= kappa_u nu = <U^*u, e>, and the deep sum is >= -||u 1_{(D,inf)}||_1 (|z| <= 1).  Hence
      sum_{s <= D} (c_s(u))_-  >=  - sum_{s <= D} c_s(u)  >=  <U^*u, e> - u(zhat) - ||u 1_{(D,inf)}||_1 ,
i.e. the NEGATIVE parts of the c_s carry the bound (signed form; K2 states it for |c_s|).  Mirror statement: if kappa_u <= 0 then
kappa_u (1 - alpha(D)) <= kappa_u nu, so sum_{s <= D} (c_s(u))_+ >= sum_{s<=D} c_s(u) >= |<U^*u, e>| + u(zhat) - ||u 1_{(D,inf)}||_1.
This signed pair is exactly the mechanism of Theorem K2.16 (1), (3), (6).  (Numerics: K2_ref_work/ref_identity.py.)

## 3. Lemma K2.4 (first-order actions, diagonal base).  VERDICT: correct; one sign typo.
(i) U^*A changes by mu_s dm k_s; d(x/||x||) = (I - e e^T) dx/||x||, and <U^*u, k_s - e_s e> = mu_s u(s) - (mu_s a_s/nu) kappa_u nu = mu_s D_u(s): the
first-order change of u(xhat) is (mu_s^2/nu) D_u(s) dm.  Renormalization by q* does not change e (scale invariant) nor z; the second derivative of
x -> x/||x|| is bounded by 3||dx||^2/||x||^2, whence the remainder.  (ii) is (i) with a_s = 0; admissibility requires dm of the sign z_s (a bank is
one-sided).  (iii) is exact.
Typo: in the composite move at a zero-data contact the z-branch must be "z-move P z_s for P <= 0" (inward, z_s -> z_s(1 + P)), not "-P z_s";
with this reading the slope is u(s) z_s on both sides (bank branch: mass (nu/mu_s^2) P z_s gives (mu_s^2/nu) u(s) z_s (nu/mu_s^2) P).
Precision (used later): at a ZD coordinate that Step A left with a small positive mass m, the composite (mass change, then z-move after the mass
reaches 0) has slopes (mu_s^2/nu)(u(s) - kappa_u a_s) per unit mass and u(s) z_s per unit z; after normalization the two first derivatives differ by
kappa_u m/|u(s)|, a first-order discrepancy of size <= Design m.  It enters the Poincare-Miranda remainder like c_tiny and is harmless when
m <= Design K_DC r (otherwise use the mass branch only, which is two-sided).  (Numerics: ref_identity.py, mpmath 50 digits.)

## 4. Lemma K2.5 (left combinations of Sys-DC).  VERDICT: correct.
(a) sum_{l in Omega_m} y_l eps_l u_l(zhat_0) = A^0_m y^T p_m (p_l = eps_l u_l(zhat_0)/A^0_m) and (R_m^* w^0_m)(zhat_0) = <w^0_m, R_m^** zhat_0> = A^0_m,
because X2 Lemma DC defines A^0_m := |R_m^** zhat_0|_m and w^0_m (|w^0_m|^*_m = 1) norms R_m^** zhat_0 (forced decomposition, Observation C).
No property of Omega is used (Omega need not contain all carriers of a block).
(b) dF_l = eps_l du_l - p_l dA_m (eps_l^2 = 1), dA_m = <w^1_m, R_m dxhat> + O(|delta|^2) (block norm smooth away from 0; second-order constant
from the clamp formula, X2 DC (2)), and ||R_m^*(w^0_m - w^1_m)||_1 <= sum_k lambda_k |w^0_m(k) - w^1_m(k)| <= K_w Pi + 2 c_{L+1} (X2 UE-1(d) for
coarse carriers whose status is kept; |w| <= 1 for fine ones).  The constant C in |err| <= C |delta| ||y|| (...) contains ||y||_1 <= |Omega|^{1/2}
||y||_2 and the efficiency of the move; harmless.
(c) <U^* R_m^* w^0_m, e_1> = sum_k lambda_k w^0_m(k) <U^*u_k, e_1> = G_m (with w^0; Q2 4.0 writes G_m with w at the linearization point; the
difference is the same error).  So <U^*Psi_y, e_1> = y^T g - sum_m beta_m G_m = y^T gt up to the stated error.
(Numerics: ref_dc_degenerate.py part (a): Psi_y(zhat_0) = O(1e-16) for random y; finite-difference columns satisfy y^T c = l_delta(Psi_y).)

## 5. Lemma K2.1 (tolerance variant of Theorem UE^inf).  VERDICT: correct.
I re-derived the four places where X2's proof (r9/X2_notes 3.5) and Q2's modification (M1)-(M5) use d-consistency.
(u1) Step 2.  With diamond = +, b^theta - b^+ = -(1/2) sum_m R_m^*(Domega_m - Delta_m w^0_m), omega^theta - omega^+ = Domega/2, so the block part of
     tau g'_i is tau [rho(omega^+ - d'(omega^+) w') - (rho/2)(d' - d)(Domega) w' + (rho/2) Delta (w^0 - w')], i.e.
       Omega^+_m = rho(omega^+_m - d'_m(omega^+_m) w'_m) + kappa^+_m w'_m + rho(d^+_m - d^theta_m)(w'_m - w^0_m),  kappa^+_m = -(rho/2) mis_m,
     and symmetrically kappa^-_m = +(rho/2) mis_m; the theta pair has Omega^theta = rho(omega^theta - d'(omega^theta) w') by construction of g''_i
     (kappa^theta = 0 with or without d-consistency).  Exactly K2's (u1).
(u2) W_0 = (1 + tau kappa)(w' + t''(omega - d'(omega) w')), t'' = tau rho/(1 + tau kappa); N_m is positively homogeneous, so the level term is
     tau kappa^diamond, a first-order term added to lin'_m.  X2's Step 4 uses lin'_m only through |lin'_m| <= tau^2 (|eps_m| <= 6 K_sharp tau^2), and the
     cost of a level shift is |tau kappa| iota with iota <= 2 eta_1 (Proposition J's discussion) -- already inside E <= 12|I| K_sharp eta_1 tau^2.  With
     |mis| <= s_1: |tau kappa| <= (rho/2)|tau| s_1 <= tau^2 for |tau| > s_1; the theta piece (|tau| <= s_1) has kappa = 0.  Radius conditions: t'' differs
     from tau rho by a factor 1 + O(c_flat t s_1).  Correct.
(u3) |d'(omega) - d(omega)| = |sum_k omega(k)(nv'_k - nv^0_k)| <= |Omega| (A_2/t) K_w Pi; H' - (C/C')H = (d^2 - d'^2)/C', so |H' - (C/C')H| <=
     C_f |Omega| A_2^2 K_w Pi/t^2; relative error in Step 5's bracket <= C_f |Omega| A_2^2 K_w^2 s_1/T^2 (Pi <= K_w s_1) <= delta/32 under (LATE-tol).
     Statuses of Omega: gap' >= gap^0 - C K_w Pi (Lipschitz) instead of (1.1); (LATE) suffices.  Correct.
(u4) g''_i - g_i = sum_m d^theta_m R_m^*(w^0_m - w'_m) + sum_m (d_m - d'_m)(omega^theta_m) R_m^* w'_m - b^theta 1_{(N_w,inf)}; the new middle term has
     l_1 norm <= N |Omega| A_2 K_w Pi/t_i.  Correct.
Nothing else in X2 3.5 or Q2 (M1)-(M5) uses d-consistency: Step 3 (Base) does not involve d; Lemma UE-1(d), (e) use statuses and Lipschitz value
bounds only; (f) is d-free.  (LATE-tol) has the form of X2's (LATE) (a window constant times T^2) and is implied by it after enlarging K_w.
Remark 2 of K2.1 (|mis| <= (m/A'_m)||D_m Domega||_2 ||F||_2, ||D Domega||_2 <= C'_Delta by X2 Proposition J(a)) is correct, so an approximate zero
|F|_inf <= c_f s_1/|Omega|^{1/2} suffices.  The lemma is not used by the main line (Theorem K2.6 gives exact zeros), only as robustness.
