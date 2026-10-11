# G2 referee, part 1 (working log): Lemma MS, Lemma 1.1, Theorem JF -- first pass

Sources read: BRIEFING, BRIEFING_R2 (all addenda), martin summary, r13 H1_referee/H1_ref_notes, H2_referee/H2_ref_notes, H2_notes 1-3,
Part III 5.6 (Definition III-SysA, Lemma III-Euler, Definition III-Areg, Lemma III-cone, Theorem III-Aobs, Corollary III-Asuff), G2_notes (all).

## 1.1 Lemma MS (minimax over the certificate hull): re-derivation
- Phi(Delta, y) = <kappa y, Delta> - phi_y(rt_0) is linear in Delta and affine in y (phi_y = y^T Ft(rt_0) linear in y).  D_{h_max} compact
  convex polytope; conv(Y) compact convex (Y closed and bounded).  Von Neumann/Sion applies; min over conv(Y) of an affine function is
  attained on Y.  (a) and (b) follow exactly as written.  CORRECT.
- Inclusion of certificates at rt' in Y: generator columns are g = eps_l l_delta(u_l) - rt_l l_delta(K_{m(l)}) (Lemma III-Euler(b)), affine in
  rt with slope bounded by Des^C, so a near-certificate at rt' of size < 4 u^3 Des^{-C_A} is one at rt_0 of size < 4 u^3 Des^{-C_A} +
  Des^C h_max <= eps_* (h_max = Des^{C_h} u^{-4}(||b|| + x), ||b|| + x <= Des^C eta').  CORRECT.
- Theorem III-Aobs (3) (gamma <= -c_*) holds for EVERY near-certificate of size <= eps_*, with no hypothesis on phi_y: checked in the proof
  in Part III (uses (1), whose bound involves |phi_y| <= |Lambda_A|^{1/2} max(x, ||b||) only).  So Lemma 1.1(b),(c) are correct and conv(Y)
  avoids 0.  Only item (6) needs phi_y > -rho_0; G2 correctly excludes it.
- Lemma 1.1(d): items (2a), (2c) contain |kappa_Psi| on the right; averaging is legitimate because kappa_y < 0 for every y in Y (common
  sign), so sum theta_i |kappa_{y_i}| = |kappa_z|.  PRECISION (P-LIN): say so.
- LP dual (c): max{c^T Delta : Delta in V, A Delta <= 0, |Delta_l| <= rbar_l} = min_{lambda >= 0, nu in V^perp} sum_l rbar_l |c - A^T lambda - nu|_l
  (Lagrangian with nu for the subspace constraint; box conjugate).  CORRECT; dual attained.

## 1.2 Theorem JF
- (JF1): (a_d)_l = 1[l = d]/rt_{0,d} + 2 kappa'_{(d)} m^2 rt_{0,l} 1[l in Omega_(d)], so the multiplier term is
  2 m^2 rt_{0,l} sum_{d: l in Omega_(d)} kappa'_{(d)} lambda_d, not 2 kappa'_m m^2 rt_{0,l} Lambda^{(l)}_m, when Puiseux statuses (T-blocks)
  carry a different kappa'.  PRECISION (P-JF1): define Lambda^{(l)}_m with the weights kappa'_{(d)}/kappa'_m (all >= 0; nothing changes).
- (JF2), (JF3): splitting of V^perp correct (V_G tangent space => V_G^perp|_G = row space of the Jacobian; piece-scaling V_G => pairing with
  the piece vectors, |rt_{0,l}| <= rbar_l).
- Every row is movable or pinned (holds and pushed rows are movable), so rt^{(m)} in V for (U)-blocks: piece vectors are tangent to Z_G by
  Euler's identity for P homogeneous in r^{(m)} (Lemma PC).  CORRECT.

## 1.3 Lemma 3.2 statement
"every hull element z ... satisfies kappa_m(z_l - c_lp sgn(rt_p) z_p) <= ..." is FALSE for general hull elements: the bound
<kappa z, Delta> < c_MS on D_1 holds only for the minimax element z* of Lemma MS(b).  PRECISION (P-32).  The use (for z*) is correct.

## 1.4 Lemma NL (first look)
Newton contraction re-derived: ||D Phi|| <= (9/8)(1/8) < 1/2 on the ball of radius 2||R_2||/s_J^2; self-map; ||E|| <= q^{1/2} Des^C s_max
||Delta||^2/s_J^2.  CORRECT as stated.  But the hypothesis "J has FULL ROW RANK" fails for determinantal systems at smooth points
(the (r+1)-minors of a rank-r matrix have dependent gradients), so "the remaining (H-6') is non-affine groups at SINGULAR targets" must read
"at targets where the tiny-polynomial system of the group has no robust full-row-rank subsystem with the same local zero set".
PRECISION (P-NL), to be expanded in part 3.
