# Referee report (a) on Q2 (Round 10): (LSC-trunc), infinite base support through finite-support approximants

Refereed: r10/Q2_notes.md (with Q2_part1..4.md) and r10/Q2_work/*.py (onesided_check, prop41_check, border_check re-run: outputs identical; lt_check.out inspected, superseded by my own adversarial LT test).  Checked against: paper/martin_density_note.tex
(lem:dualball, prop:forced, prop:smooth, prop:continuity, prop:approximants, lem:threshold, lem:bookkeeping, lem:transferdata, lem:persistence,
lem:smallness, lem:budget, lem:finitebase, lem:windowtwopiece, lem:slack); r9/X2_notes.md 1-4 with X2_ref_notes.md (precisions and (R-abs));
r7/V3_notes.md 2.1-2.5 (raise transfer, normer change, E_RT); r7/V1_notes.md 4.1 (Proposition TR); r10/Q1 referee report (a) for the inherited chain.
My part files: r10/Q2_refa_part1..4.md; proofs of all precisions and repairs: r10/Q2_refa_notes.md; scripts: r10/Q2_refa_work/ (lt_adversarial.py,
smass_jacobian.py, border_inverse.py, drift_check.py, with outputs).  Role: independent adversarial referee (a).

## 0. Bottom line
Q2's main contribution is correct: infinite base support is NOT an obstruction for the violation-tolerant route.  Truncating the base support after s_1
turns the far support into contacts of the norm-attaining approximant whose two-sided use is a tolerated violation (mass tail_W <= delta s_1/(64 rho)), and
the truncation mass cancels exactly (Lemma LT, the lowering counterpart of V3's raise transfer).  So (LSC-trunc) at (f, g, rho) -- indeed (f, rho g) in
cl NA -- follows from window families with side cushion domination (U3^inf) at base rows of arbitrary support (Theorems UE^inf, E^{eng,RT,inf}).  Every
PROVED claim I checked is correct; the precisions are bookkeeping, plus two overstatements in the Consequence of Lemma 4.3 which I repair.  The SKETCH
labels (Proposition 3.2, Theorem 5.1, Corollary 5.2) and OPEN labels are honest.  New: in the exact degenerate lever configuration, EXACT d-consistency is
impossible as soon as the window theta-masses touch the support of the degenerate combination (an exact scalar identity, notes C.5); I propose a data-side
bordering (R3-a) that avoids exactness along that direction (SKETCH).  (LSC-trunc) for every f, hence density for p_N and for p: OPEN.  No counterexample is
claimed or suggested.

## 1. Verdicts
| Claim (Q2 label) | Verdict | Main point / fix |
|---|---|---|
| Lemma 1.1 (PROVED) | correct | (d) needs mu non-increasing; (c) via prop:approximants (ii) => (i), valid for non-NA rows |
| Lemma LT (PROVED) | correct, SHARP | factor 2 attained (notes A.1; numerics: (LT) attained to 2.7e-7 by adversarial h); partial form re-derived (4 cases) |
| Corollary 1.2 (PROVED) | correct | finitely many scales fixed before M; NOT uniform down to r = 0 (notes A.2: an explicit h with Lambda_M linear in r) -- consistent with Q2 1.3 |
| Lemma M2^inf (PROVED) | correct | the removed clause was used only in (c1) |
| Theorem UE^inf (PROVED) | correct (conditional) | new coordinate classes re-derived; precisions: lever radius contains Pi_tr; S-mass range at thick coordinates must enter (LATE); N_w >= S-mass lever coordinates |
| Theorem E^{eng,RT,inf} (PROVED) | correct | must be stated with window-dependent C_+(j), c_flat(j) (Prop. 3.2 gives C_+ <= C Design/u): needs n c_flat/K -> inf, theta/c_flat^2 -> 0; both hold for the design (notes B.1) |
| Lemma 3.1 (PROVED) | correct | lem:smallness is F-free and uniform over g in C(f); A_0 = 10 |
| Proposition 3.2 (SKETCH) | SKETCH correct | constants rechecked coordinatewise (deep: C_+ = 2; shallow robust: C/u); compatibility with the class/cube pigeonhole unverified, as Q2 says |
| Lemma 3.4 (PROVED) | correct | exact identity re-derived; numerics 2.5e-15; supp u is infinite (u in Y), hypotheses are strong but exactly as stated |
| 4.0 Jacobian (PROVED) | correct | confirmed by finite differences in an exact one-block model with thick S-mass levers: 9.9e-10; block-norm column -pi p: 2.8e-9 |
| Proposition 4.1 (PROVED) | correct | every inequality of K checked; independent implementation: residual 1e-13; doubly degenerate left null vector y = D^{-T}(h + sum theta_m q_m) |
| Corollary 4.2 (PROVED) | correct (conditional) | Poincare-Miranda constants (K^2 C_2 r <= 1/4 on |y| <= r, or cube r/K); thick S-mass range/remainder are design quantities; "zero data at the peak coordinate" NOT automatic when the block carries a shift -- repaired by a bank-with-offset lever (notes C.3) |
| Lemma 4.3 (PROVED) | (a)-(c) correct; Consequence overstated | kappa = 0 does not keep individual carriers off F (only their private sets beyond s_max); off-support != zero-data (repaired, C.3/C.4) |
| Second-order residue 4.4(ii) (PROVED) | correct with precision | needs h^T D^{-1} p_m = 0 for EVERY block (else the null vector has q_m-terms); "tolerated by UE^inf" is a SKETCH (UE^inf assumes kappa = 0) |
| Theorem 5.1 (SKETCH) | SKETCH correct | architecture and error accounting coherent; c_alpha, beta_* must be rate objects defined at f (C.7) |
| Corollary 5.2 (SKETCH) | SKETCH correct | pulls lie in (s_max, s_far] (X2-ref p-LV2), so the hypothesis covers all lever coordinates |

## 2. Main findings
F1 (the reduction is right).  The base claim of X2's Theorem UE survives at infinite F with exactly three new coordinate classes: kept support (no flip by
   (U3^inf) and (c1^inf); theta piece protected by the W_F raises), truncated support in (N_w, N''] (contacts, cost 0 or rho|tau||v_j|, total <= rho|tau| tail_W
   <= delta tau^2/64 above s_1, zero in the theta regime), support beyond N'' (inside the cut-off term).  Step 5's budget 1 - 5 delta/4 + delta/32 <= 1 - delta.
   The truncation's l_1 mass costs only 2(1 + ||U||) alpha_0(N_w) <= 2 theta T^2, used only for pieces with c_flat t_i < |r|.  No transition-band problem.
F2 (Lemma LT is sharp and genuinely scale-limited).  The factor 2 on the cushion loss is attained; and for a continuum of scales truncation is not free
   (A.2).  Both facts support Q2's architecture (truncation inside the engineered approximant, after s_1).
F3 (block-norm levers need repair when the block is shifted).  v = sum_m R_m*(Domega_m - Delta_m w_m) gives every peak a coefficient -lambda w Delta_m, so a
   peak's private coordinates carry data unless Delta_{m*} = 0.  Validity of the window family then forces them to be contacts of the data's sign, and a
   bank-with-offset lever (base mass 2 K r beta_j, varied by beta_j P_0) is two-sided, cushion-dominated, with a small common mode h_0 <= 2 K r Design^2
   (notes C.3).  With this, "every block has a two-sided block-norm lever" (Lemma 4.3 + V1 Lemma D) holds.
F4 (exact degenerate configuration: an exact scalar obstruction).  If h^T p_m = 0 in every block and u_h := sum h_l eps_l u_l is proportional to a on the
   support, then for EVERY lever setting h^T F = -(kappa nu/2)||e - e_0||^2 + tau_W + tau_z exactly (notes C.5).  Levers act on it only at second order, so
   exact d-consistency is impossible when tau_W (theta-masses on W cap supp u_h) is of first order; it is even impossible at all when kappa(tau_W + tau_z) < 0.
   This sharpens Q2 4.4(iii) from "OPEN whether compatible" to "exactness must be given up along this direction".
F5 (data-side bordering (R3-a), SKETCH).  Only the components of nv' - nv seen by the switching vectors enter kappa^+-.  Solving F = lambda yhat with yhat
   blockwise orthogonal to the (weighted) switching vectors and y^T yhat != 0 keeps kappa^+- = 0 exactly; the residual O(C_W s_1) moves gaps and H' only by
   (LATE)-controlled amounts.  It fails only if y lies blockwise in the span of the switching vectors (for one ray per class: h parallel to the class ray in
   every switching block) -- a further degeneracy.  Not written line by line.
F6 (rate objects).  c_alpha, beta_* live at the pre-row, built after the sub-window; they must be defined at f for all lever configurations of level L
   (design count) to enter the pigeonhole; robust at f implies robust at the pre-row (C.7).

## 3. Attacks attempted (all negative)
uniformity in the scale (per-piece split I_r; theta regime; truncation after s_1; zeroth-order costs only above c_flat T); the transition between transferred
and exact regimes (bound (B') vs (UE) per piece, average by convexity: re-derived with the extra lambda-term); raise/truncation accounting (raise mass only in
lambda; truncation mass cancels; Hilbert footprints in Pi); order of choices (s_1 before N_w is legitimate: s_late, (VT'), K_w are N_w-free); per-mate quantifier
order (f, g, rho -> rows/windows -> s_1 -> N_w -> levers -> N''; density needs only single mates); hidden finite-F uses in X2's proof (only (c1), the mass set on
E, N_w >= max F_0); lever availability inside the support (thick S-mass common mode: Jacobian confirmed; bordering confirmed; zero-data hypothesis broken by shifts
-> repaired); degenerate systems (exact obstruction found, F4); counterexample search: none -- every defect is a construction gap with a repair or a precisely
isolated degenerate configuration.

## 4. Numerics (sanity only; Q2_refa_work/)
lt_adversarial.py: (LT) max(LHS - RHS) = -2.7e-7 over 150 adversarial tests; partial form -6.7e-4; sharpness exact.  smass_jacobian.py: Q2 4.0 confirmed to
9.9e-10 (194 instances, h up to 4.9), block-norm column to 2.8e-9.  border_inverse.py: Proposition 4.1 residual 1.2e-13, bound ratio 3.7e-5, Woodbury 4e-13,
doubly degenerate null vector 5e-16.  drift_check.py: Lemma 3.4 to 2.5e-15, one-sidedness, first-order action of masses on supp u \ F.

## 5. Single most valuable idea
Truncate the base support AFTER s_1 inside the engineered approximant: the far support becomes contacts whose two-sided use is a tolerated violation of mass
tail_W, while the truncation's l_1 mass cancels exactly (lowering transfer, dual to raise transfer).  Infinite base support is then free in the
violation-tolerant route, and the infinite-F half of Lemma Z reduces to producing cushion-dominated window families at infinite-support base rows.

## 6. What remains open
(O-a) Proposition 3.2 for Q1's data (Lemma P projections and clamping inside the class/cube pigeonhole).  (O-b) Lever audit of Q1's construction at coordinates
of S_l cap F ((L1)-(L3), Lemma DC^inf, bank-with-offset block-norm levers), Step B's ownership recursion on J_fine \ F, status stability under the new side
effects.  (O-c) Degenerate lever systems at all large levels: exact (NDN2) with exact full degeneracy (exact d-consistency impossible when tau_W != 0, F4; needs
(R3-a) or a tolerance variant of UE^inf, both SKETCH), the quantitative near-degenerate case, KN-1 raw holds in a degenerate raw direction.  (O-d) Bookkeeping of
the new rate objects and lever ranges.  (O-e) Inherited: Q1's Master Theorem VI chain (several once-refereed links).  (LSC-trunc) for every f, density of
NA((c_0, p_N), l_2^2) for any N, and of NA((c_0, p), l_2^2): OPEN for every admissible T.
