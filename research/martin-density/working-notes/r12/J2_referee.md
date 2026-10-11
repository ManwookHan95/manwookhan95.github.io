# Referee report on J2 (Round 12): the joint Step-0 weak-peak push problem (W*) -- bypassed

Refereed: r12/J2_notes.md (with J2_part1..4.md and J2_work/; scripts frozen_check2, lemmaJ21e_adversarial, frozen_c11_check re-run, outputs
identical).  Checked against: Part I lem:peakshift (paper/martin_density_note.tex 4821-4856); r9/X1_notes 2.1-2.6 and X1_ref_notes 1-4, 8 (Lemma K,
K1, Lemma F, D1-D3, KN^tr); r8/U1_ref_notes 1-3 (continuity of kappa, Lemma R-kt, Prop. KN); r11/cert0_report 3.1-3.5 (incl. the "C3 alternative");
r11/K1_ref_notes R-8, R-10; r11/K2_notes 1, 4.1, 5.1-5.7, 6.1-6.6, 7.1-7.3 with K2_referee/K2_ref_notes (W-1, K-1..K-8); r12/J1_notes 1, 6, 8 (for
the combination).  My part files: r12/J2_ref_part1.md (Lemmas J2.0, J2.1), part2 ((FC), Theorem J2.1, Corollaries), part3 (signs, direct
route, J1, K-8 numerics).  Full proofs of all verdicts and repairs: r12/J2_ref_notes.md.  Scripts and outputs: r12/J2_ref_work/.
Role: adversarial referee.

## 0. Bottom line
J2's main result is correct.  Theorem J2.1 (PROVED modulo the chain of K2.15) removes Step 0's weak-peak pushes from the construction.
The block scalars of Step A are frozen with the TARGET status pattern (FC): only the robust peaks are frozen as peaks.  The frozen system
 - is smooth across every threshold crossing that Step A performs,
 - satisfies Lemma K exactly,
 - is within O(Design b) of the true system at the unpushed row,
 - and coincides with the true system at the realized point, because Step A's own targets make the pattern consistent there.
I re-derived Lemmas J2.0 and J2.1 and every step of the theorem, and confirmed both lemmas numerically with an independent implementation.
J2 also finds a genuine defect in K2-ref K-8, needed for K2.15 itself.  Literally read, K-8 freezes the active weak peaks of a (U)-block as
peaks, and these leave the peak set inside the realization.  I confirmed this numerically.  With literal K-8 the true ratios miss the targets
by 5-30 eta' Phi_k^2, so exactness on Z_kappa fails.  With (FC) the true ratios equal the targets to 1e-40.
Consequently:
 - the class (W)/(W*) of K2 7.3 / K2-ref G disappears as a separate obstruction;
 - (LSC-trunc)_N holds wherever Step A at the UNPUSHED row is A-regular, i.e. under (H2^flat);
 - the residual is (A*) ∪ (U*) at that row (Corollary J2.3, PROVED).
Fixable points: P-1..P-6, Q-KN and J4-a..c (Section 2).  None changes a conclusion.  Two statements are overclaims:
 - "Theorem J2.1 STRICTLY contains K2.15": the containment is PROVED, strictness is not;
 - the combination with J1 is PROVED only CONDITIONALLY on J1's band realization (J1.13-J1.15), which I did not referee.
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) remain OPEN, as J2 states.  J2 claims no
counterexample, and nothing I found points to one.

## 1. Verdicts
| Claim (J2 label) | Verdict | Main point |
|---|---|---|
| Lemma J2.0 (PROVED) | correct | re-derived; explicit bound in consequence (b) off by the factor 1 - a(rho - 1) >= 1 - b (positivity is all that is used) |
| Lemma J2.1 (PROVED) | correct, constant slip | (a)-(e) re-derived; fine kinks contribute C Design c_{L+1}, not C sum Phi^2 (P-1); boundary numerics 0 violations |
| (FC) precision to K-8 (PROVED) | correct, with qualifier | literal K-8 fails in (U)-blocks (numerics); for (KN)-blocks only if the lever push is not a one-shot pre-move (Q-KN) |
| Theorem J2.1 (PROVED mod chain) | correct with precisions | P-2 size b' when Pi_0 != {}; P-3 (D2) must carry R-8's enlargement ((K2-e) reading); P-5 blocks without tuned carriers; P-6 audit |
| Corollary J2.2 (PROVED) | correct after P-4 | (H2^flat) targets defined by Steps 1-3's properties (radius 2 eta'); K2.15 read with (FC); "strictly" unproved |
| Corollary J2.3 (PROVED) | correct | K2.16 holds for the frozen map (Euler share even smaller); new residual contained in the old one |
| Data sign of weak peaks (PROVED) | correct | eps_k = vs_k sgn(e_k - Delta'_m) from lem:peakshift; R-8/W-1 wrong iff Delta'_m > 0, e_k > Delta'_m; no conclusion changes |
| Proposition J2.4 (PROVED) | correct with precisions | thin raises have O(Design b) relative first-order cross terms (J4-a); constants (J4-b); Step-0 banks create S_th moduli up to Design^C b/u^2 (J4-c) |
| Lemma J2.5 (PROVED) | correct | case analysis re-done |
| Remark J2.6 (PROVED) | correct (last sentence HEURISTIC) | orientation identity and (X3) argument right; the kappa-window sentence is a caricature of J1.2 |
| Step-0 Farkas certificates (SKETCH) | label honest | identity Psi^0_y(xhat) = 0 PROVED; structure transfer SKETCH; "as hard as Step A" HEURISTIC |
| Combination with J1 (PROVED mod J1) | conditional | sound composition; (J-c)-(J-f) realize Step A with bands, so J2.1 must accept band-realized companions (J1.13) |

## 2. Main findings
F1 (the bypass is sound).  The pushed row was used in five places.
 - (L1), the Lojasiewicz start: cert0's "C3 alternative", made rigorous by Lemma J2.1(e) and the frozen Lemma F.
 - (L2), Lemma K: the frozen Lemma K holds.
 - (L3), the realization: K2.9(c) for the C^{1,1} frozen map.
 - (L4), (L5): bookkeeping.
 - One more use (P-6): the (X4^0) data violation and the shift-trick cost.  Both survive with r_0 in place of r_1.
 Step (iii) is the heart of the proof.  At the solution every block is consistent: (T)-blocks through R^2 = R_a(r'')^2 exactly and sigma_f
 approximately sigma_rob; (U)-blocks through the rescaling; pushed carriers through their margins; the robust objects are unaffected.  So
 J2.1(c) identifies the frozen solution with the true companion.
F2 (literal K-8 is defective; (FC) is the fix).  At the realized point an active weak peak of a (U)-block has nu_k < theta_f, yet literal K-8
 counts it as a peak.  Then (A_f, theta_f) != (A, theta), and the realized true ratios are off the targets.  Exactness on Z_kappa (KN-1, tiny
 minors exactly zero) is lost.  This affects K2.15 itself, independently of Step 0.
F3 (precisions).
 - P-1: fine kinks.
 - P-2: b' when Pi_0 != {}.
 - P-3: the delta_0 of (D2) must be taken at Design^C b/u, as (K2-e) states and R-8(ii) did not.
 - P-4: target definition.
 - P-5: blocks without Sys-A rows.
 - P-6: audit.
 - Q-KN: the (KN)-block qualifier.
 - J4-a..c: Proposition J2.4.
 All are proved in J2_ref_notes C.2, C.1 and D.2.  One of them, J4-c, also applies to R-8's (WP) banks inside K2.15.  The bypass with
 Pi_0 = {} avoids it.
F4 (overclaims).
 - "strictly contains K2.15" (bottom line (1)): unproved.  J2's own toy has a two-sided peak resource, and that resource also gives (H1*)
   through Proposition J2.4(ii).
 - The combination with J1 is conditional on J1.13-J1.15.

## 3. Attacks attempted
I attacked the following points.
- Puiseux margin.  F(r'') <= 1 - mu from the frozen start; this needs P-3.
- Exactness on Z_kappa.  The consistency argument holds; literal K-8 fails it, (FC) holds it (numerics).
- Cushion domination C_+.  Pi_0 = {} adds no support; banks are covered by J4-c.
- (VT) tolerances and closeness K t.  The data and the cone are unchanged, and the companion is nearer to f^r.
- Cost.  Pi_0 costs at most C_f Design^C b log(1/b)/u^2 = o(u^2 T^2).
- Uniformity along main stages, N-independence, well-foundedness.  J2 makes no design change.
- Quantifier order.  design -> N -> f, g, rho -> l_f -> L -> w -> class -> Pi_0 -> (P) -> targets -> Pi -> Step A -> data.
- Signs and one-sidedness.  Weak peaks enter Step A as tuned carriers with their own generators (D.1).
- Hypothesis boundary of J2.1(e).  20000 extreme blocks, no violation.
- Frozen root uniqueness beyond th_max.  This is irrelevant by definition.
- Whether every row falls in a covered case.  NO: the residual is (A*)/(U*) at the unpushed row.
Results:
- Counterexample: none.
- Nothing found suggests that the residual contains a non-recoverable mate.

## 4. Numerics (sanity only; r12/J2_ref_work/)
- ref_frozen_indep.py/.out (40 digits; independent true-block solver).  The true block was cross-checked against a water-filling solution of
  the dual norm program (A to 9e-16, theta to 7e-8); the frozen system was solved by Newton on (G1, G2).  On 389 admissible blocks:
  - Lemma J2.1(e): ratios 0.35 of the bound 3x and 5e-4 of the bound 4x; kappa constant 0.17;
  - frozen Lemma K to 1e-40; derivatives to 3e-22;
  - W-fix region and the Step (i) floor inequality hold in every case.
- ref_boundary_e.py/.out: 20000 blocks at the boundary of J2.1(e)'s hypotheses, 0 violations (max ratios 0.38, 4e-4).
- ref_K8_literal.py/.out: realization of (U)-block targets from the unpushed row in 60 random blocks.
  - (FC): consistent in 60/60, true ratios equal the targets to 8e-40.
  - Literal K-8: errors 1.1e-4..4.4e-3 (5-30 eta' Phi_k^2).
- rerun/: J2's frozen_check2, lemmaJ21e_adversarial and frozen_c11_check give identical outputs.

## 5. Single most valuable idea
Freeze the block scalars with the TARGET status pattern, not with the status pattern of the input row.  Pre-moves that change statuses then
become unnecessary: a weak peak is an ordinary tuned row of Step A, the C^{1,1} realization is legitimate across threshold crossings, and
consistency at the realized point, which Step A's targets supply, turns the frozen solution into the true companion.  This removes the
joint push problem (W*) as a separate obstruction and repairs K2-ref K-8 in the (U)-blocks.

## 6. What remains open (precise)
(1) (H2^flat) at every row.  This is the sign class (A*)/(U*) of Theorem K2.16 at the UNPUSHED prepared row with (FC): a near-certificate
    with robustly negative common mode, thick design-depth support proportional to Psi_y, no anchor, and one-sided mass >= c_*/2.  It is J1's
    residual (R0)/(R1), conditional on J1.
(2) Whether (H2^flat) is strictly weaker than (H1*) + (H2) (HEURISTIC; a candidate configuration is described in J2_ref_notes C.3).
(3) Inherited: the once-refereed links of the K2.15 chain, and J1's band realization J1.13-J1.15 used by the combined statement (J1.11 is a
    SKETCH).
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.
Required edits to the record:
- K2.15 (K2-ref G): replace "(H1*) and (H2)" by "(H2^flat)", read with (FC) and P-4.
- K2-ref K-8: freeze the target pattern; Q-KN for (KN)-blocks.
- (K2-e): (D2) carries R-8(ii)'s factor (P-3).
- K2-ref K-3: the range of the S_th moduli becomes [theta_0, Design^C b/u^2] when Step 0 or Pi_0 contains banks (J4-c).
- K1-ref R-8 / K2-ref W-1: eps_k = vs_k sgn(e_k - Delta'_m).
- J2's bottom line (1): "contains" instead of "strictly contains".
- J2 7.2: label "conditional on J1.13-J1.15".
