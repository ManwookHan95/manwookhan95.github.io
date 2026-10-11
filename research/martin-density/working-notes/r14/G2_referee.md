# Referee report on G2 (Round 14): minimax SLP over the certificate hull, joint Farkas form, coupled directions, margin levers,
# and the remaining (R0)/(R1) resonance classes

Refereed: r14/G2_notes.md (with G2_part0..4.md and G2_work/; scripts re-read, outputs consistent).  Checked against: Part III 5.6
(Definition III-SysA, Lemma III-Euler, Definition III-Areg, Lemma III-cone, Theorem III-Aobs, Corollary III-Asuff, Definition III-resources,
Lemma III-K, block-scalar formula of 2.1); r13 H1_ref_notes (Lemma SLP, PC, MA', C.6, E), H2_notes 1-4, H2_ref_notes (P-RANGE, P-31, P-41,
F-NE, B.10); r12 J2_ref_notes C.1 (Q-KN); r11 cert0 3.2; r10 Q1_refb 1.2.  Proofs of every verdict and fix: r14/G2_ref_notes.md (part files
G2_ref_part1-3.md).  Scripts and outputs: r14/G2_ref_work/.  Role: adversarial referee.

## 0. Bottom line
G2's main new tool, LEMMA MS, is correct.  It is a minimax over the convex hull of near-certificates and all first-order status-safe, exactly
admissible target displacements.  It yields either one displacement that realizes Step A, or one hull element z* that keeps every LINEAR
certificate property.  Its LP dual (Theorem JF) is the joint Farkas form.  Theorem H2.A' (H2.A by one fixed displacement), Lemma 3.4(c) via
coupled directions, Theorem R1-J, the (W4'') re-check for (D-abs), Proposition 4.7/Corollary 4.8, Theorem 5.2 and Remark 1.8 are correct up
to precisions.
Problems found:
 - G-MU / G-LAM / G-NAFF (Theorem ML, the new positive result).  The proof bounds the resonance term by |mu| beta(b) with "|mu| <= Des^C/u by
   V2 Lemma H".  This is FALSE in general.  The size of mu is governed by the smallest nonzero singular value s_J of the Jacobian of the
   group's tiny polynomials, and the design does not control it: J's minors are not rate objects, and for affine groups J does not even
   depend on the group's ratios.  Numerics R1 give a restricted-model counterexample in which all hypotheses (S), (G), (B) hold but the needed
   capacity is 3.3 beta/s_J.  The bound also needs bounded status multipliers (G-LAM) and small multipliers on blocks with non-affine kind-(i)
   groups (G-NAFF).  Theorem ML as stated is therefore NOT proved.  The repaired statement adds (S+) and (G+) (robust Jacobian, affine groups
   included).
 - REFEREE ADDITION, Theorem ML' (PROVED mod chain).  The crude bound |phi_{z*}| <= ||b(rt_0)|| makes the decomposition unnecessary.  A pinned
   or locked kind-(iv) row is controlled as soon as S_l has a pullable coordinate at depth v in [Des^{C_m} max(x, ||b||), x''_max].  This range
   lies inside the CERTIFIED pre-placement range [x, x''_max] (Definition III-resources, R-6, P-RANGE); J1-ref P-TU restricted only the
   CAPACITY of two-sided TU levers.  So ML' needs no (S), no (G) and no (K1-depth).  Consequently the persistent (R1)
   residual (Theorem 4.9') is a pure deep-swallowing condition (P-res').  G2's Theorem 4.9 lists (P-prot) and (P-naff), but as stated they
   miss affine groups with non-robust Jacobian and blocks with large multipliers; corrected in C.8.
 - G-CAP (Lemma 4.2).  Box capacities W/2 on every uncapped generator break the Brouwer remainder bound ||Rem|| <= rho_0.  Fix: simplex budget.
 - P-55 (Lemma 5.5).  Removing d from Omega makes the block scalar jump by theta Phi_d^2 (numerics R2).  This rescales every ratio of the
   block, which is fatal for exactness in shifted blocks, exactly where conversion is needed.  Fix: keep d in Omega.  The stated conclusion
   (continuity of statuses) holds.
 - Precisions: P-LIN, P-EPS, P-WMAX, P-JF1, P-41i, P-14, P-32 ("every hull element" false), P-NP'1 (no-peak-lever case missing), P-NP'2 (sign),
   P-NP'3, P-NL (full row rank fails at non-complete-intersection points; the J-minor rate-object design change is not carried out), part-1
   Lemma 1.3(b).
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p remain OPEN, as
G2 states.  No counterexample is claimed, and nothing found here suggests one.

## 1. Verdicts
| Claim (G2 label) | Verdict | Main point |
|---|---|---|
| Lemma MS with Lemmas 1.1, 1.3 (PROVED mod chain) | correct | Sion on compact convex sets; Aobs(3) holds without phi-hypothesis; P-LIN, P-EPS, P-WMAX |
| Theorem JF, Corollary JF' (PROVED mod chain) | correct | split of V^perp re-derived; P-JF1 (kappa'_(d)), P-41i (multi-block groups are bilinear) |
| Lemma NP' (PROVED mod chain) | correct with fixable gaps | P-NP'1: residual must allow "no peak lever"; P-NP'2 sign; P-NP'3 |
| Remark 1.8, P-KN (PROVED mod chain) | correct | pre-move convention (cert0 3.2, Q-KN) |
| Lemma 3.1', Lemma 3.2 (PROVED) | correct with fixable gap | P-32: bound holds for z* only, not "every hull element" |
| Theorem H2.A', Theorem R1-J (PROVED mod chain) | correct | case analysis uses only linear certificate properties + D_1 bounds |
| Lemma 4.1 ((W4'') re-check) (PROVED, inspection) | correct | constraint set shrinks; legitimacy beyond weights via R-abs/K1.S |
| Lemma 4.2 CAP (PROVED) | correct with fixable gap | G-CAP: box capacities break ||Rem|| <= rho_0; simplex fix |
| Lemma 4.3 MS^cap, 4.4 OD, 4.5 MV (PROVED mod chain) | correct (4.3 after G-CAP) | re-derived |
| Theorem ML (PROVED mod chain + (K1-depth)) | wrong as stated | |mu| bound false without robust Jacobian (R1); G-LAM, G-NAFF; repaired; ML' replaces it |
| Proposition 4.7, Corollary 4.8 | correct | obstruction of A-regularity in the restricted model; statement about the method |
| Theorem 4.9 (PROVED as necessary condition) | correct with fixable gaps | residual list too narrow; Theorem 4.9' (P-res') + repaired disjunction |
| Lemma 5.1, Theorem 5.2 (PROVED mod chain) | correct with fixable gaps | P-NP'1 in (c); "singular targets" terminology (P-NL) |
| Lemma 5.3 NL (PROVED) | correct | Newton contraction re-derived; scope remark overclaims (P-NL) |
| Proposition 5.4 (PROVED mod chain) | correct | -- |
| Lemma 5.5 (PROVED mod J2.1) | correct with fixable gap | P-55: keep d in Omega (block scalar jump theta Phi_d^2 otherwise; R2) |
| Peak conversion (SKETCH) | label honest | G1, G2 open |
| (R0), (R1) at all large stages; (LSC-trunc)_N; density (OPEN) | OPEN | -- |

## 2. Main findings
F1 (Lemma MS is sound and is the right object).  Every hypothesis of the minimax is met: Phi is linear in Delta and affine in y, and both sets
are compact convex.  Certificates at the displaced targets are transported into Y by the Lipschitz dependence of the generator columns; the
generator SET must be fixed with a target-independent capacity threshold (P-WMAX).  Theorem III-Aobs(3) needs no hypothesis on phi_y, so the
hull avoids 0.  The linear properties (J1.6(a), AL, R-PK, NP(b), H2 (1.2), Prop. 3.1) average.  The two items carrying |kappa| average
because kappa_y < 0 on Y (P-LIN).
F2 (Theorem ML: false step, repair, and a stronger replacement).  See G-MU above.  In the model J = [[1,1,1],[1,1+s,1-s]] with P(rc) = (0, beta)
and full target freedom, the needed capacity is 3.33 beta/s (LP, s = 1e-1..1e-4).  Repaired form: hypotheses (S+), (G+), with
Des^C beta(b)/(u s_J) in cap_min.  ML' needs only (B) and a pull in [Des^{C_m} max(x, ||b||), x''_max].  Such a pull may be too small to be
a two-sided generator of the cone realization (capacity below the Brouwer radius, J1-ref P-TU), but it is large enough at the scale of the
right-hand side.
F3 (G-CAP).  With box capacities, ||t||_2 reaches (W/2)|G|^{1/2}, so C_2||t||^2 can exceed rho_0 by |G|/4 >> 1.  Lemma III-cone(c) needs the
simplex budget; MS^cap is unaffected once (b) is restated with a max over G_u.
F4 (P-55).  Part III's kappa(zeta; Omega) depends on Omega; statuses do not.  Converting d by removing it from Omega rescales all ratios of the
block by k/(k + Phi_d^2).  Keeping d in Omega and freezing only the threshold pattern makes the conversion continuous in kappa, ratios and
statuses (Lemma K's sigma' has the (1 - rho^2) term for exactly this).
F5 (precisions).  P-32, P-NP'1-3, P-NL, P-41i, P-14, P-EPS, P-JF1, part-1 Lemma 1.3(b) (see ref notes C).

## 3. Attacks attempted
- Hoffman constants and which rows they involve: targets stay exactly on Z_kappa (Lemma 1.3(a); piece scalings exact; Newton exactification
  for robust Jacobians).  Minors move by Des^C h << u, so V2's design-controlled Hoffman bound persists.  The NEW conditioning quantity is s_J
  of the tiny-polynomial Jacobian: it is not a Hoffman constant of the class cone and the design does not control it (G-MU).
- Scale constraints: h_max = Des^{C_h} u^{-4}(||b|| + x) with Des^C h_max^2 << eta'/Des; the displacement is inside P-TF's x_TU window and
  J1.13's allowance.  Margin-lever depths: [cap'_min/2, x''_max] lies in the certified range [x, x''_max]; G2's deeper range [cap_min/2, x)
  needs (K1-depth).  J1-ref P-TU (TU levers need capacity >= radius) is respected: capped generators are used only up to their capacity.
  Preparation banks (theta_0 = b/Des^{C_P}, b <= (eta'/3C_L)^{N_L/2} by (QC4)) are too small to serve as margin levers.
- Puiseux margin and (FC): first-order status-safe displacements; second order Des^C h^2 << eta'/(12 Des); robust peaks stay robust; frozen weak
  peaks stay below 1 - eta' + Des^C h^2; (KN)-blocks under the pre-move convention; peak conversion handled with Omega fixed (P-55).
- Counting: Corollary 4.8 checked (a tiny resonance obstructs every coarser sub-window in the model).  Memory gives fresh CARRIERS only;
  at most N (up)/(down) events per round range (H2-ref B.10 + Lemma 4.1).
- Design changes: (D-abs) is N-free and well-founded, and only removes upper bounds on weights.  The J-minor rate objects of Lemma NL's
  remark are not carried out.  ML' needs no design change.
- Signs: JF1 multiplier signs, MV signs, NP' (sign slip in the (beta) reading), orientation of K^+/K^- helpful directions all re-derived.
- Quantifiers: design -> N -> (f, g, rho) -> L -> w -> class -> preparation -> targets rt_0 -> margin-lever pre-placement (threshold W_max)
  -> Y(rt_0) -> minimax -> Delta* -> Brouwer -> data at the realized ratios.
- Coverage: not every stage is covered; Theorems 4.9' and 5.2 are necessary conditions.  Counterexample: none.
- Missed recovering mechanisms: ML' itself (any pull in [Des^C x, x''_max], even of sub-threshold aggregated capacity).  The capped-generator
  idea could also use shared pulls or other carriers' TU levers (suggestion).

## 4. Numerics (sanity only; r14/G2_ref_work/)
- r1_mu_gap.py (.out): minimal margin-lever capacity for an exact-target-freedom (U)-block model with two tiny minors of Jacobian singular value
  s: c_need/beta = 3.33/s (3.3, 33, 333, 3333); certificate lower bound 1.67/s; robust J: 0.5.
- r2_peak_conversion.py (.out): exact block threshold (KKT of the block norm), identity |zeta|^2 = theta^2 a^2 to 6e-17; kappa with Omega fixed
  continuous (max step = grid 6e-6), kappa with Omega switched jumps by 8.018e-4 = theta Phi_d^2 (predicted 8.016e-4).
- G2's N1-N3 re-read and consistent.  N2's margin levers have capacity ~ ||b||, so N2 tests ML', not the refined cap_min.

## 5. Single most valuable idea
The capped minimax over the certificate hull (Lemma MS^cap; G2's idea, sharpened here).  One fixed target displacement plus capped one-sided
resources either realizes Step A or yields one vector z* with all linear certificate properties.  Combined with |phi_{z*}| <= ||b||
(Theorem ML'), a pinned or locked one-sided row is harmless once it has a downward resource of capacity Des^{C_m} max(x, ||b||).  This holds
whatever the resonance, its exactness, the Jacobian or the status multipliers.  The obstruction "exactness versus one-sidedness" thus becomes
a pure DEPTH-SWALLOWING condition on fresh carriers.

## 6. What remains open (precise)
(1) (R1) at all large main stages: (P-res') at every clean sub-window/class.  This means pinned or locked kind-(iv) rows anti-sign swallowed
    over [cap'_min/2, x''_max]: on both sides in blocks with a two-sided peak resource, and on the lever-opposed side in one-sided blocks.  The
    carriers are fresh within each round range outside at most N events, and the certificate must also satisfy the normal form of Theorem
    III-Aobs(4).  Refined alternative: (P-prot+), (P-naff+) (affine groups included), or swallowing down to cap_min/2 (needs (K1-depth)).
(2) (R0) at all large main stages: Theorem 5.2's coincidence classes (with P-NP'1); non-affine groups without a robust Jacobian (including
    non-complete-intersection points); (H-7); peak conversion gaps G1 (O(beta_* Phi_d^2) status change against eta'/Des) and G2 (downstream
    legitimacy of a weak peak of margin ~ beta_*).
(3) Inherited: once-refereed links of the chain; (K1-depth) (only for the refined range); the J-minor rate-object design change (Lemma NL).
(LSC-trunc)_N for every f: OPEN.  Density of NA((c_0, p_N), l_2^2) for any N: OPEN.  Density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.

## 7. Required edits to G2
- Theorem ML: either add (S+), (G+) and the s_J term to cap_min (C.6), or replace it by Theorem ML' (C.7).  Remove "|mu| <= Des^C/u by V2
  Lemma H".
- Theorem 4.9: replace by Theorem 4.9' (C.8).  (P-naff) must include affine groups with non-robust Jacobian; (P-prot) must include blocks with
  large multipliers that contain pinned groups.
- Lemma 4.2: simplex budget for G_u and sum of capped capacities <= W/2; restate (b) with max over G_u (C.5).
- Lemma 5.5: keep d in Omega; freeze only the threshold pattern (C.11).
- Lemma NP' and Theorem 5.2(c): residual "sigma_m = sgn(Delta''_m) or no one-sided peak lever"; sign of the (beta) reading (C.9).
- Lemma 3.2: "z* of Lemma MS(b)" instead of "every hull element" (C.4).
- Lemma 5.3 "Use" and Theorem 5.2(d): "targets without a robust full-row-rank subsystem", and label the J-minor rate-object remark SKETCH (C.10).
- Lemma 1.1/MS(a): eps_1 := 8u^3 Des^{-C_A}; target-independent two-sidedness threshold W_max (C.2).
- (JF1): kappa'_(d) weights; summary: P-41 (i) removed only for affine groups (multi-block groups are bilinear) (C.3).
- Part 1 Lemma 1.3(b): drop "nearly neutral statuses stay <= 2b" (C.12).
