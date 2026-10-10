# Referee report on K2 (Round 11): degenerate lever systems (O-c) and the new rate objects (O-d)

Refereed: r11/K2_notes.md (and K2_part0..3.md, K2_work/; scripts re-run into K2_ref_work/rerun/: psi_check, euler_check identical,
euler_share_probe's value 1.85 identical, fo_check2 1.9e-16; identity_check's double-precision first-order line shows the cancellation K2 mentions).  Checked against: r10/Q2_notes.md 2.2-2.5, 4.0-4.4 with
Q2_referee_a and Q2_refa_notes (B.1, B.2, C.1-C.7); r11/K1_notes.md 2.0-2.7, 4.1-4.3 with K1_referee and K1_ref_notes (R-1...R-14); r9/X2_notes.md 1-3
(Lemma DC, Theorem UE, Lemma UE-1); r9/X1_notes.md 2.6 and X1_ref_notes (KN^tr Steps 0-4); r8/U1_notes.md 1.1-1.5; r11/cert0_report.md 3.1-3.4.
My part files: r11/K2_ref_part1.md ... part5.md; full proofs of all verdicts and repairs: r11/K2_ref_notes.md; scripts and outputs: r11/K2_ref_work/.
Role: adversarial referee.

## 0. Bottom line
K2's two main contributions are correct.
(1) Sys-DC is settled.  The preparation (banks of mass theta_0 at every design-depth contact of the coarse supports, raises of thin coordinates, closing
of tiny rooms) puts the offsets into the BASE row, whose values are the targets of the d-consistency system.  The exact identity u(zhat) = kappa_u +
sum_F D_u sgn a + sum_{F^c} u z then turns every near-null left vector of the system into a robust two-sided first-order resource at design depth.
Theorem K2.6 (uniform singular-value bound with design constants, no rate objects, no bordering) is PROVED modulo the cited chain.  I re-derived
every step and confirmed it numerically: at rows where the square (P4) lever system is EXACTLY singular, the enlarged two-sided system of the prepared
row has s_min 0.07-0.13, independent of theta_0 in [1e-6, 1e-2], and Newton solves F = 0 for perturbations of both signs with the banked masses
staying positive.  Q2-refa C.5's exact obstruction concerns only the original lever set (S-mass and block-norm levers, which never act on
supp u_h minus F_0).
(2) Sys-A is reduced to a sign class.  Lemmas K2.8 and K2.9 and Theorem K2.16 are correct (re-derived): every Step-A obstruction has a robustly
NEGATIVE common mode and a thick design-depth support proportional to the certificate's carrier combination.  Corollary K2.17's sufficient conditions
(a)-(f) are correct.
(O-d) is settled for the objects K1 and K2 introduce.
I found one fixable GAP and several precisions; none changes a conclusion.
 GAP W-1 (Theorem K2.15, hypothesis (H1); inherited from K1-ref R-8 and enlarged by K2's extension).  The weak-peak push condition is per peak, but
   Step 0 must push ALL active weak peaks.  (P4) pushes and shared design-depth moves have first-order cross effects on other weak peaks; the common
   modes |g h| can exceed 1.  So the joint push can be singular (1 - h_W^T g_W = 0) even though every peak has its own resource; already for one
   peak a (P4) push moves the peak's own value by (1 - g_k h_k) per unit and fails when this vanishes.  Fix: replace (H1) by
   the joint condition (H1*) (Step-0 inequality system A-regular).  It holds, e.g., if every active weak peak has a PRIVATE push resource, or if the
   (P4)/shared-pushed ones have a robust bordered scalar.
 K-8 (frozen statuses; also affects K1 Lemma K1.6(A)).  Step A's realization domain contains points where near-threshold Omega carriers cross the
   threshold.  There d kappa/d zeta jumps by an amount of order 1 (numerically from 0 to -0.85...-0.96), so the remainder bound C_2 ||t||^2 fails.
   Fix: use block scalars with the coarse statuses frozen, and verify the statuses at the solution (exact ratios, Puiseux margin, uniqueness of the
   threshold solution).
 K-7 (u-scaling).  To make (H2) weaker than K1's (LR), as K2 claims, A-regularity must allow moves Design^{C_A} u^{-3} max(x, ||b||) and certificates of
   size u^3 Design^{-C}.
 Labels and wording.  Corollary K2.7 "do not arise" means "are bypassed": the square system can stay degenerate.  K2.17(g) is a reduction to (f), not a
   sufficient condition on its own.  5.5's "Moreover" (a far z-move breaks the certificate) is a SKETCH, the same mechanism as K2.11.  7.3's "iff" is
   only "only if".
 Typos.  K2.4's composite z-branch sign.  "||xhat_1 - zhat_0||_inf <= K_w Pi" in K2.6 Step 3 (the cut-off beyond N''; the bound actually needed holds).
   K_DC (number of rows).  (2a)'s missing |kappa| m_s term (m_s = mass at the pre-placed TU bank).  (2c)'s sign convention presupposes v > 0 on S_k.  (H1)'s "eps_k val_k" should be
   "vs_k val_k".
(LSC-trunc)_N for every f, and density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2), remain OPEN, as K2 states.  K2 claims no counterexample,
and nothing I found points to one.

## 1. Verdicts
| Claim (K2 label) | Verdict | Main point |
|---|---|---|
| Lemma K2.1 (PROVED) | correct | four uses of d-consistency re-derived ((u1)-(u4)); level shift cost inside X2's E; (LATE-tol) of (LATE) type |
| Lemmas K2.2-K2.4 (PROVED) | correct | identity exact; SIGNED dichotomy is what Section 5 uses; composite-move sign typo |
| Lemma K2.5 (PROVED) | correct | A^0_m = \|R_m zhat_0\|_m normed by w^0_m; no property of Omega used |
| Preparation (P) (PROVED) | correct | (R1) verified via V1 TR/E'' + contact rows; C_+ = max(5, C_f) at banked coords; costs zeroth order o(u^2T^2) |
| Theorem K2.6 (PROVED) | correct | re-derived; P-3, P-4 precisions; numerics at exactly singular square systems |
| Corollary K2.7 (PROVED) | correct after rewording | degeneracies bypassed, not absent |
| Lemma K2.8 (PROVED) | correct | Euler 4e-10; Xt_m tiny because route V tunes every coarse strict non-peak (confirms K2's (R2)) |
| Lemma K2.9 (PROVED) | correct with fixable gaps | K-8 frozen statuses in (c); K-7 u-scaling |
| Theorem K2.16 (PROVED) | correct | re-derived (1)-(6); K-1, K-2, K-3 precisions |
| Corollary K2.17 (PROVED) | correct with a fixable gap | (g) must be combined with (f)'s criterion |
| (O-c)(iii) (PROVED) | first part correct; "Moreover" SKETCH | far contacts one-sided; per-unit action below the certificate tolerance |
| Proposition K2.11 (SKETCH) | label honest | pushes are the mirror of the in-F pull |
| Lemmas K2.12-K2.14, costs (PROVED) | correct | doubled b in (D1) suffices: (P1) moves each value by <= b ||u_k||_1 <= b |
| Theorem K2.15 (PROVED mod chain) | correct after the W-1 fix | (H1) -> joint (H1*); K-7, K-8 |
| 7.3 residual (OPEN) | correct as necessary condition | "only if"; (W) -> (W*) |

## 2. Main findings
F1 (Sys-DC, the key result, holds).  Every step of K2.6 was re-derived.  Step 1: lever columns e_l - h_l gt - p q_l with signed h; every Omega carrier has
   a lever.  Step 2: gamma is robust.  Step 3: Psi_y(zhat_0) = 0.  Step 4: signed dichotomy at depth D(L).  Step 5: eff >= mu*_{D(L)}^2.
   Step 6: Poincare-Miranda; statuses fixed because the moves are K_DC r.  The interface with Theorem UE is sound: X2's (SEP) is only sufficient,
   and the new columns act at coordinates with cushion-dominated, aligned or zero data.
F2 (Sys-A structure holds).  K2.16 is a correct necessary condition for an obstruction.  Its use of the small Euler share is legitimate exactly because
   route V puts every coarse strict non-peak into Lambda_A (U1 Lemma 1.5 final form).
F3 (GAP W-1).  The weak-peak push condition must be joint.  Per-peak resources do not suffice when pushes have first-order cross effects ((P4) common
   modes, or shared coordinates under K2's extension).
F4 (K-8).  The realization of Step A (K2.9(c), and K1.6(A)'s cube) needs frozen coarse statuses.  Without them the remainder is first order near
   threshold crossings.
F5 (K-7).  The u-scaling of W is bookkeeping (monotone).  (I first suspected that (K2-e)'s doubling of b is too small for (P1); it is not: every
   value moves by <= b ||u_k||_1 <= b.  Withdrawn.)
F6 (interpretation of the residual).  The (A*) degeneracy h^T g~ ~ 1 cannot come from private proportional thick coordinates alone, since h^T g <=
   (Hilbert mass on them)/nu^2.  It needs the peak terms -(h^T rt) G_m or cross terms through shared target coordinates, consistent with K2.16(4).

## 3. Attacks attempted
I attacked the following points.
- Uniformity in t and in the window.  K2.6's constants are design numbers; (LATE-K2) hold with S2c^tr's s_1.
- Number of carriers.  eps_DC ~ 1/|Omega|; |Omega| <= |Lambda_L| is a design number.
- Companions and raises.  The clean dichotomy at depth D(L) survives the deep raise (J(w) > D(L)), Step 0, (P), Step A, the pre-row and Sys-DC.
- Levers inside the support.  Elementary columns at TS, S_th, FR, ZD coordinates have side effects on peaks and fine carriers; these are covered by
  K2.5(b) and the status margins.
- Hoffman, minor and Sherman-Morrison constants.  K2.6 is uniform, and K2.9 uses Hoffman only qualitatively.
- N-independence and well-foundedness.  Both re-checked.
- Signs and one-sidedness.  S_th coordinates are one-sided at scale x and two-sided at scale r; cushions at banked coordinates are as in F1.
- c_0 versus l_infty.  Every move acts at finitely many coordinates, and approximants have finite base support.
- Quantifier order.  Re-checked.
- Coverage of infinite-support rows.  Not every row is covered: the residual is (W*) ∪ (A*) ∪ (U*).

Results:
- Adversarial numerics: exactly singular square systems resolved after preparation.  The adversarial unprepared sign iteration oscillated.
- Found: W-1, K-7, K-8 and the labelling issues.
- Counterexample: none.

## 4. Numerics (sanity only; r11/K2_ref_work/)
- ref_identity: K2.2 to 2.7e-15; signed K2.3, 63548 tests, no violation; K2.4 (50 digits) to 1.2e-12.
- ref_blockcheck: threshold formula versus the convex program, 4e-8.
- ref_dc_degenerate: K2.5 and K2.6 at exactly singular square systems.  Prepared rows give s_min 0.07-0.13, independent of theta_0; the nonlinear
  solve succeeds for both signs; banked masses stay >= 0.76 theta_0.
- ref_sysA, ref_sysA_central: Euler identity 4e-10; generator actions 1.5e-5; Xt 3.4e-6 (route V) versus 3e-2.
- ref_kappa_jump: the derivative of kappa jumps by an amount of order 1 at threshold crossings, while A stays C^1.

## 5. Single most valuable idea
Put the offsets into the BASE row.  K1's offset obstruction says that a bank placed in the pre-row has a forced total position of uncontrolled sign.
That obstruction disappears for the d-consistency system, because its targets are the values of the prepared row.  Combined with the exact identity
u(zhat) = kappa_u + sum c_s, this yields a uniform dichotomy:
- either a near-null left vector of the system has a small common mode, and then it is not near-null;
- or it forces a robust first-order two-sided resource at design depth.
This holds with design constants and without any rate object or bordering.

## 6. What remains open (precise)
(1) (A*)/(U*) at all large main stages.  Step A carries a near-certificate with a robustly negative common mode, a thick design-depth support
    proportional to Psi with no anchor, none of K2.17(a)-(e), and one-sided mass >= c_*/2.  Step-A targets are Lojasiewicz ratios, not row values,
    so preparation cannot help.
(2) (W*): the joint Step-0 push problem (H1*) fails.  This covers missing per-peak resources and Sherman-Morrison-type degeneracy among
    (P4)/shared weak-peak pushes.
(3) Inherited: the once-refereed links of the chain (Q1/X1/X2/U1 tools, Q2's UE^inf and E^{eng,RT,inf}, K1/K1-ref).
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) are therefore OPEN.  Next steps:
- K2's "target freedom" in Z_kappa, to orient the Lojasiewicz correction against the finitely many certificates (HEURISTIC);
- a push lemma (the mirror of V1's in-F pull) with an overshoot/degree argument;
- for (W*): a private-push design or an A-regularity analysis of Step 0.
