# G2 part 4: (R0) -- minimax readings, nonlinear pinned groups, thick peaks of shifted blocks, peak conversion

Notation of Parts 1-3, H1 1, H1-ref D, E.  Thick row = thick-type row with robust or near-threshold status.

## 4.1 The (R0) residual through Lemma MS

LEMMA 4.1 (alignment of the hull element).  PROVED (mod chain).  For z* in conv(Y) and every thick row l:
 z*_l rt_l = kappa_{z*} rho_l u_l(xhat_1)/kappa_m + O(eps Des^2 + Des(eta' + b) + C b^2 D^2), kappa_{z*} := gamma(z*)/nu_1 in [-C, -c_*/nu_1];
so sgn(z*_l rt_l) = -sgn(rho_l u_l(xhat_1)) (anti-aligned: z*_l rt_l > 0) with |z*_l rt_l| >= c_* u^2 Phi_l/(2 nu_1 m K).
Proof.  Lemma AL is a linear approximate identity in y with a y-independent error (Lemma 1.1(d)); kappa_y is linear in y.  QED

THEOREM R0-J (the (R0) residual in joint form).  PROVED (mod chain).  If Step A is not realized at a stage with a thick-type carrier,
then with z*, lambda, nu, mu of Theorem JF:
 (a) [(U)-blocks with a private two-sided peak resource] Lambda_m <= Des^C (eps + c_MS) (Lemma MV(a)); no movable thick row exists
     (a movable thick row l has (JF1) kappa_m z*_l rt_l = lambda_l + 2 kappa'_m m^2 rt_l^2 Lambda_m + O(c_MS), which is small, against
     Lemma 4.1); every (U)-piece G ∩ m (with ANY rows: thick, kind (i), kind (iv)) is balanced for z*:
          |zeta^{G ∩ m}(z*)| = |kappa_{z*} Xi_{G∩m}/kappa_m + sum_{(iv) l in G ∩ m} z*_l rt_l + O(small)| <= Des^C (eps + c_MS)   (JF3, Lemma MV(a));
     here the kind-(iv) terms satisfy z*_l rt_l >= -e_1 |rt_l| on K^+ and <= e_1 |rt_l| on K^- rows.  [This is H1-ref's (H-3') extended
     to objects containing non-thick kind-(iv) rows, by a single vector z*.]
 (b) [(U)-blocks without a peak resource] sigma_m = sgn(rho_c vs_c) is common to the thick-type peaks; if sigma_m = -1 Step A is
     realized (Theorem RL, which is the displacement -delta rt^{(m)} of D_h); if sigma_m = +1: sum_{d in N ∩ m} lambda_d (1 + 2 kappa'_m
     R^2_{(d)}) = kappa_m zeta_m(z*) + O(c_MS) >= kappa_m c_* u/(4 nu_1) - O(c_MS) > 0, the block is protected, and every movable row l with
     robust ratio satisfies kappa_m z*_l rt_l = lambda_l 1[l in N] + 2 kappa'_m m^2 rt_l^2 Lambda_m + O(c_MS): it is anti-aligned thick or an
     active K^+ kind-(iv) row with that weight (H1-ref (H-4'), now with the explicit multiplier identity).
 (c) [shifted blocks] (JF1)-(JF3) hold; every movable thick row is anti-aligned (aligned ones are relieved inward, Theorem IN = the
     inward displacement in D_h) and satisfies z*_l/rt_l = (lambda_l 1[l in N]/rt_l^2 + 2 kappa'_m m^2 Lambda_m)/kappa_m + O(c_MS/(rbar_l
     |rt_l|)): for unprotected robust rows the common value 2 kappa'_m m^2 Lambda_m/kappa_m (= H1's anti-aligned proportional
     resonance, since z*_l rt_l is fixed by Lemma 4.1); every thick-type ROBUST PEAK of m forces sigma_m = sgn(Delta''_m) and the absence
     of a two-sided peak resource (Lemma NP'); if moreover rt^{(m)} is in V, sigma_m = -1 is relieved by down-scaling (Lemma NP').
 (d) [pinned groups] affine groups: (JF2); non-affine groups at targets where the tiny polynomials have a robust Jacobian: tangent
     levers (Lemma NL below), so (JF2) holds with grad P_i at rt_0; remaining: non-affine groups at SINGULAR targets (Jacobian rank
     deficient or not robust), with only (JF3).
 (e) [wrong side] phi_{z*}(rt_0) > -rho_0^max with the decomposition of Lemma OD.
Proof.  (a) Lemma MV(a); (JF1) for movable l; Lemma 4.1 gives |z*_l rt_l| robust.  Pieces: (JF3) with the piece vector, Lemma 4.1 on
thick rows, kind (i) small, kind (iv) signs from z*_l >= -e_1.  (b) Lemma NP (linear, so valid for z*); pairing (1.3) with rt^{(m)} in V
(Lemma 2.1(d)) as in Lemma MV(a), with zeta_m(z*) robust of sign sigma_m; (JF1).  (c) (JF1), Lemma 4.1, Lemma NP'.  (d) (JF2) and Lemma NL.
(e) Lemma MS(b) with the sharp threshold (Part 3).  QED

## 4.2 Nonlinear pinned groups with a robust Jacobian

LEMMA NL (tangent levers).  PROVED.  Let G be a pinned group whose tiny polynomials P_1, ..., P_q are polynomials in r^G (the other
groups' ratios fixed) with ||D^2 P_i|| <= Des^C on the W-fix region, and suppose that at the targets the Jacobian J := (grad_G P_i(rt_0))_i
has full row rank with smallest singular value s_J >= u^{C_J} Des^{-C_J} (ROBUST JACOBIAN).  Then for every Delta in ker J with ||Delta||
<= h <= s_J^2 Des^{-C-1}/(8 q) there is E(Delta) in (ker J)^perp with ||E(Delta)|| <= 2 q^{1/2} Des^C ||Delta||^2/s_J and rt_0^G + Delta +
E(Delta) in Z_G exactly; E is continuous in Delta.  Consequently ker J may be added to V (Definition 1.2) with the exactification map
Delta -> Delta + E(Delta): Lemma 1.3 holds with the extra error ||kappa y|| ||E|| <= Des^C u^{-C} h_max^2 in every pairing, and Lemmas MS,
MS^cap, JF, OD hold with this error added to rho_0^max (it is <= x/Des since h_max^2 <= Des^C u^{-8} eta'^2).
Proof.  Write r = rt_0^G + Delta + J^T xi (xi in R^q) and F(xi) := P(r).  F(0) = P(rt_0 + Delta) = J Delta + R_2 = R_2 with ||R_2|| <=
q^{1/2} Des^C ||Delta||^2/2 (Taylor; P(rt_0) = 0, J Delta = 0).  DF(xi) = J(r) J^T with ||J(r) - J|| <= q^{1/2} Des^C (||Delta|| + ||J^T xi||),
and J J^T >= s_J^2 I.  The map xi -> xi - (J J^T)^{-1} F(xi) is a contraction on {||xi|| <= 2 ||R_2||/s_J^2} when q^{1/2} Des^C (||Delta|| +
s_max ||xi||) <= s_J^2/4 (s_max := ||J|| <= Des^C), which the bound on h ensures; its fixed point solves F = 0.  E := J^T xi.  Continuity:
the fixed point depends continuously on the parameter Delta (uniform contraction).  The status and data bookkeeping of Lemma 1.3 is
unchanged (the displacement is Delta + E with ||E|| << ||Delta||).  QED
Remarks.  (1) Robustness of J can be made a rate object: the minors of J are polynomials in the ratios of the pattern (design-countable,
N-free), so they can be added to the rate scheme of level L as V2's design adds all minors; at a clean sub-window they are tiny or
robust at f, and V2 Lemma L's simultaneous exactification can make the tiny ones exactly zero at the targets.  When the full set of q
tiny polynomials has a robust q x q Jacobian minor, the lemma applies.  (2) If rank J < q at the targets (dependent gradients, e.g. a
cofactor polynomial vanishing to second order), Z_G may be singular at rt_0 and tangent levers are not available in general; only the
(U)-piece scalings remain.  This is the remaining part of (H-6'): NON-AFFINE PINNED GROUPS AT SINGULAR POINTS OF THEIR ZERO SETS.
(3) (X4^0)-minors: entries vs_l and m^2 |r_l| K(sigma_rob, R_a^2) are smooth (K Nash on the W-fix region), so Lemma NL applies to them
with "polynomial" replaced by "Nash function with Des^C second derivatives" (the proof uses only C^2 bounds).

## 4.3 Thick-type peaks of shifted blocks

See Lemma NP' (Part 1, 1.5): PROVED (mod chain).  Residual: sigma_m = sgn(Delta''_m) with only one-sided peak levers, and the block
scaling inexact (some tiny minor with nonzero shift cofactor C_{Delta'}) or (sigma_m = +1 and m protected).  In the joint form the
shift cofactors carry the robust zeta_m: sum_i mu_i C^{(i)}_{Delta'} = kappa_m zeta_m(z*) - <A^T lambda, rt^{(m)}> + O(c_MS).

## 4.4 Peak conversion of anti-aligned near-threshold rows

PROPOSITION 4.2 (where peak conversion is needed).  PROVED (mod chain).  In a (U)-block with a private two-sided peak resource no
protected movable thick row is anti-aligned at a residual stage (Theorem R0-J(a): Lambda_m ~ 0 while an anti-aligned movable row needs
lambda_l + 2 kappa' m^2 rt_l^2 Lambda_m = kappa_m z*_l rt_l robustly positive).  So peak conversion is needed only in (U)-blocks without
peak resource with sigma_m = +1 and in shifted blocks.
LEMMA 4.3 (frozen consistency of a converted peak).  PROVED (mod J2.1).  Let d be a coarse non-peak of block m frozen as a PEAK, i.e. the
block scalars of Step A computed with P_f := P_rob ∪ {d} (all other coarse carriers non-peaks, fine carriers true), and add the band row
rho_d in [1 + beta_*, 1 + 3 beta_*] to Step A.  Then the frozen system is C^{1,1} on the Brouwer domain with the constants of J2.1(b)
(|d Psi_f/d theta| >= 2 theta_f Phi_{P_rob}^2), and at any realized point satisfying the band row and the other targets it coincides with the
true system (J2.1(c): nu >= theta_f on P_f, nu <= theta_f on Q_f).  Moreover, at rho_d = 1 the frozen descriptions with d in P_f and with d
in Omega give the same a_f^2 = sigma_f + k_f^2 R^2 (the contribution Phi_d^2 = rho_d^2 Phi_d^2 moves from k^2 R^2 to sigma), so the statuses of
the other carriers are continuous across the conversion, with |Delta log rho_k| <= C D^C (rho_d - 1) Phi_d^2 for rho_d in [1, 1 + 3 beta_*].
Proof.  J2.1(a)-(c) need P_f nonempty with zeta != 0 on P_f, which holds near the realized point (|zeta_d| >= theta Phi_d^2 > 0); the
Jacobian bound uses P_rob ⊂ P_f.  Consistency: the band row and the protected statuses of the other rows.  Continuity: J2.1(d) with
(P_f, Omega) = (P_rob ∪ {d}, Omega \ {d}) versus (P_rob, Omega): sigma changes by Phi_d^2 and k^2 R^2 by -rho_d^2 Phi_d^2; at rho_d = 1 the
equations a^2 = sigma + k^2 R^2, k = a + sigma, coincide; Lipschitz in rho_d.  QED
REMAINING GAPS (OPEN, precise).  (G1) The status change of the other protected rows, O(beta_* Phi_d^2) with beta_* ~ Des^C x/u, exceeds
their margins eta'/Des unless compensated; the compensating down-scaling pairs with every certificate by -delta kappa_m zeta_m(z*) < 0 in
the sigma_m = +1 case, and its size is of the same order beta_* as the relief of the conversion: an f-dependent comparison of
|z*_d rt_d| with zeta_m(z*), not controlled.  (G2) Downstream legitimacy of a zero-data weak peak of margin ~beta_* at the companion (U1
Proposition 2.2(a)'s peak-error term and CM'(a)'s screening Scr_m for coarse peaks of non-robust margin), not re-derived here.  So peak
conversion remains a SKETCH; gap (i) of H1-ref C.6 (consistency outside (FC)) is closed by Lemma 4.3.

## 4.5 (KN)-block bookkeeping

Remark 1.8 (Part 1): with the one-shot pre-move convention (cert0 3.2, J2-ref Q-KN) every displacement of Lemma MS is legitimate in
(KN)-blocks with no lever coupling.  PROVED (mod chain).  This closes P-KN for all levers expressed through Lemma MS (which contains every
lever of H1 and H2 up to second order, Remark 1.4(iii)).
