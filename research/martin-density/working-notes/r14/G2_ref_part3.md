# G2 referee, part 3 (working log): Lemma NP', Remark 1.8, (R0) section, Lemma NL, peak conversion, remaining precisions

## 3.1 Lemma NP' -- correct, with three precisions
Re-derived: coef_c = -zeta_m lambda_c vs_c (1 - X_m) for an untuned robust peak (Part III 5.6), and coef_c = kappa_y rho_c + O(eps Des^2)
from Theorem III-Aobs (2b) at the thick private p (TS generator two-sided); so zeta_m(y) (1 - X_m) lambda_c vs_c = -kappa_y rho_c +
O(eps Des^2): a linear approximate identity, inherited by conv(Y).  (i) via R-PK, (ii) via the one-sided balance (with P-31's theta_0 term),
(iii) via Cor. III-Asuff(d) with the data sign -sgn(Delta''_m) vs_c.  Down-scaling clause: l_d(-rt^{(m)}) = -(1 + 2 kappa' R^2) < 0.
 P-NP'1 (residual conclusion incomplete): "a residual stage with a thick-type robust peak in a shifted block m has sigma_m = sgn(Delta''_m)
  and no two-sided peak resource" omits the case that m has NO peak lever at all (no robust peak with a private data-carrying S_th near
  coordinate: possible at (R0) stages when the near coordinates of the robust peaks are thick).  Correct reading: no two-sided peak resource,
  and (sigma_m = sgn(Delta''_m) or no one-sided peak lever).  Same in Theorem 5.2(c).
 P-NP'2 (sign): with M_i = C^{(i)}_{Delta'} - sum_l r_l C^{(i)}_l, grad M_i . rt^{(m)} = -C^{(i)}_{Delta'} on Z, so pairing (2.2) with rt^{(m)}
  gives sum_i mu_i C^{(i)}_{Delta'} = -(kappa_m zeta_m(z*) - <A^T lambda, rt^{(m)}>) + O(c_MS) (opposite sign to the notes); harmless (only the
  modulus is used).
 P-NP'3: the reading needs every pinned group of m to be affine (or robust-Jacobian with the same expansion); on non-affine groups of a
  shifted block nu is unconstrained and adds an unknown term.

## 3.2 Remark 1.8 (P-KN) -- correct (mod chain) under the pre-move convention
cert0 3.2: one-shot KN pushes s_0 = C D eta' theta Phi_P^2/(rho_{d0} M) before the fixed point; J2-ref Q-KN: then active weak peaks are already
strict non-peaks at f_1 + Pi and (FC) is consistent.  Lemma-MS displacements do not raise protected statuses at first order and raise them by
<= Des^C h_max^2 << c D eta' at second order.  d_0 in N (inward only).  Accepted.

## 3.3 Lemma 5.1, Theorem 5.2 (R0-J) -- correct (mod chain), precisions
Lemma 5.1 = Lemma AL averaged (linear, y-independent error); |z_l rt_l| >= (c_*/nu_1)(u/2)|rt_l| with |rt_l| >= u Phi_l/(m K).
(a) MV(a) + (JF1)*rt_l + Lemma 5.1 (needs Des^C(eps + c_MS) << c_* u^2 Phi_l/(nu_1 m K), true since Des(L) dominates 1/Phi_l for l <= L and
eps_* = u^3 Des^{-C} with C large); pieces: pairing (2.2) with the piece vector (in V for every group type).  (b) pairing with rt^{(m)} (in V
for (U)-blocks); movable rows of robust ratio then have kappa_m z*_l rt_l >= 2 kappa' m^2 rt_l^2 Lambda_m - O(c_MS) > 0 robustly: kind (i)
impossible (|z*_l| small), kind (iv) only K^+ (z*_l >= -e_1), thick only anti-aligned.  (c) aligned movable thick rows: the inward direction
pairs with kappa z* by kappa_m |z*_l rt_l| rbar_l/|rt_l| >> c_MS, against (1.1).  (d) (JF2) holds for affine groups WITHOUT any bound on mu
(no conditioning needed in (R0)); "singular targets" must read "targets where the tiny-polynomial system of the group has no robust
full-row-rank Jacobian" (P-NL).  (e) Lemma MS(b).

## 3.4 Lemma 5.3 (NL) -- correct as stated; P-NL
Newton contraction re-derived (part 1).  Precisions: (1) "full row rank" fails at smooth points of non-complete-intersection zero sets
(several tiny minors of one matrix at a rank-r point have dependent gradients), so the complement "non-affine groups at SINGULAR targets"
is larger than the geometric singular locus: it is the set of targets where no subsystem with a robust full-row-rank Jacobian has the same
local zero set.  (2) The remark that robust Jacobians "can be made a rate object" (minors of J added to the rate scheme, tiny ones exactified)
is a DESIGN CHANGE that is not carried out (rate-object count omega(L), Lojasiewicz exponent of the enlarged system, b(w), survival): SKETCH.
(3) For AFFINE groups J is independent of the group's ratios (data and other blocks' ratios only), so a tiny-but-nonzero singular value of J
cannot be exactified by any target choice; this matters for Theorem ML (G-MU), not for Theorem 5.2.

## 3.5 Proposition 5.4 -- correct.  Lemma 5.5 -- conclusion correct, proof mechanism wrong in one detail (P-55, fixable)
Part III: kappa(zeta; Omega) = (|zeta|(|zeta| + theta) - sum_{k in Omega} v_k^2 Phi_k^2)/theta, statuses rho_k = v_k/theta are INTRINSIC
(independent of Omega), Lemma K's sigma' = Phi_{P\Omega}^2 + sum_{Omega ∩ P}(1 - rho^2)Phi^2 + s_Q is built so that kappa(.; Omega) is continuous
across a crossing when Omega is FIXED.  The notes' proof converts d by passing from (P_rob, Omega) to (P_rob ∪ {d}, Omega \ {d}): then
kappa(zeta; Omega \ {d}) - kappa(zeta; Omega) = rho_d^2 theta Phi_d^2 = theta Phi_d^2 at rho_d = 1, i.e. the block scalar and ALL ratios of
block m jump by the factor k/(k + Phi_d^2) (the equations a^2 = sigma + k^2 R^2 do coincide, but k = a + sigma does not).  Statuses are
continuous anyway (intrinsic), so the stated conclusion holds; but the targets (ratios) of a SHIFTED block -- exactly where Prop. 5.4 says
conversion is needed -- would leave Z_kappa (no scaling invariance).  FIX: keep d in Omega and freeze only the threshold pattern (theta from
the threshold equation with P_f = P_rob ∪ {d}); at rho_d = 1 both frozen thresholds coincide (d contributes theta^2 Phi_d^2 = v_d^2 Phi_d^2),
hence so do kappa, ratios and statuses.  NUMERICS R2 (G2_ref_work/r2_peak_conversion): scanning v_d through the threshold, kappa with Omega
fixed has max step 6.0e-6 (grid), kappa with Omega switched jumps by 8.018e-4 = theta Phi_d^2 (predicted 8.016e-4); theta and the other
statuses are continuous; identity |zeta|^2 = theta^2 a^2 to 6e-17.

## 3.6 Peak conversion (SKETCH) -- label honest
With Omega fixed, conversion to rho_d in [1 + beta_*, 1 + 3 beta_*] changes sigma' by -(rho_d^2 - 1)Phi_d^2 and every other status by
d log K/d s * Delta sigma' = O(D^C beta_* Phi_d^2): this is G1 (vs margins eta'/Des), unchanged by the fix.  G2 (downstream legitimacy of a
weak peak of margin ~beta_*) is not re-derived anywhere.  OPEN.

## 3.7 Further precisions found
 P-EPS: Lemma 1.1 sets eps_1 := eps_* while Theorem ML uses eps <= 4u^3 Des^{-C_A}; take eps_1 := 8u^3 Des^{-C_A} (<= eps_* when C_A >= C_* + 3);
  this still contains every transported certificate of Lemma III-cone(b) (transport error Des^C h_max << u^3 Des^{-C_A}).
 P-WMAX: whether a pre-placed TU lever counts as a two-sided generator (capacity >= W/2, H2 (U'), H2-ref P-RANGE) depends on W = W(rt);
  in Lemma MS(a) use one target-independent threshold W_max := max over rt_0 + D_{h_max} of W(rt) (<= Des^C u^{-4} W(rt_0)), so that the
  generator SET is the same at rt_0 and rt' and "y in Y" follows from the Lipschitz dependence of the columns.
 P-14: Remark 1.4(iii)/2.1 "a stage not realized by Lemma MS(a) is not realized by any of these levers either" overclaims for band levers
  and Brouwer-coupled rescalings (realized values in boxes are not fixed displacements); H2.A's conclusion is nevertheless recovered (H2.A').
 Part-1 Lemma 1.3(b) "nearly neutral statuses stay <= 2b" is false (a hold moved by h rbar_l reaches status ~ Des^C h u >> b); the notes'
  version (inside Cor. 2.4's KN-1 band, as for H1's nearly-neutral displacement) is the correct one.
 Part 2 vs notes, Lemma NL constants: the notes' constants (q^{1/2} Des^C s_max ||Delta||^2/s_J^2, hypothesis q^{1/2}Des^C h s_max <= s_J^2/8)
  are the verified ones.
