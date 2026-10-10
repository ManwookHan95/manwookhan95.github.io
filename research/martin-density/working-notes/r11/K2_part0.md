# K2 part 0 — reading notes and first reductions (working file)

## Where kappa enters (X2 Theorem UE / thm:engineered)
- kappa^{+-}_m = rho (d'_m - d_m)(omega^{+-} - omega^theta) = -+(rho/2) X_m,  X_m := (d'_m - d_m)(Domega_m) (per piece).
- With the d-mismatch, Omega^{+-}_m = rho(omega^{+-} - d'(omega^{+-})w') - (rho/2)(Delta_m (w' - w) + X_m w')  [both sides],
  so lin'_m acquires -(rho/2)|tau| X_m (SAME sign on both sides).  kappa^theta = 0 identically.
- Only lin'_m sees kappa; X2 Step 4 needs only |lin'_m| <= tau^2 for |tau| > s_1 (K_sharp >= 1, eta_1 = delta/(192|I|K_sharp)).
  => TOLERANCE VARIANT: |X_m| <= c s_1 with c an f-constant suffices (all other uses of d-consistency are (LATE)-absorbed).
- (d'-d)(Domega) = sum_k Domega(k) lambda_k eps_k F_k / A'_m, and by Cauchy-Schwarz (Prop J) |X_m| <= (m/A'_m)||D_m Domega_m||_2 ||F|_{Omega_m}||_2
  with ||D_m Domega_m||_2 <= C_f (Gamma <= 2, U1 Lemma 2.1): uniform in t.  So |F|_inf <= c s_1 / |Omega|^{1/2} (design-weighted) suffices.

## U1 Prop 2.2: data of a class have a COMMON SHIFT Delta'^* but gamma(t) varies in the cone -> the switching span Sigma can be large.
  (So the referee's "one ray per class" picture for (R3-a) is too optimistic; the exceptional case y in Sigma must be handled.)

## Exceptional exact degenerate case: structure
 y = h (X = 0 route, all h^T p_m = 0), Phi(P) := y^T F(P) = u_h(xhat(P)) exactly; support moves: Phi = -(kappa nu/2)||e - e_0||^2 (+ off-F terms).
 Phi has a strict local MAX along support moves at f_0 (kappa > 0).  Forced residual = tau_W (theta-masses on supp u_h \ F_0) + tau_z.
 Single-carrier model: sigma := sign of theta-mass contributions = -sgn(kappa) (computed from u_l(zhat_0) = 0); F_0-moves, flips, lowerings,
 second order all push sigma as well; only pulls / inward z-moves / banks at contacts of opposite type push -sigma.

## Key idea under test: DISPLACEMENT.  The target row (companion) must not sit at the max of Phi; a companion-level displacement
 raise at a design coordinate p in F cap supp u_h makes grad Phi != 0 (efficiency ~ kappa mu_p^2 |Delta|), so forced residuals of either
 sign are absorbable at the approximant.  Must be done at the COMPANION (target) level; interacts with Step A exactness (KN-1).
