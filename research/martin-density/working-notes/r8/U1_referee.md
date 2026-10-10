# Referee report on U1 (Round 8): the near-exact coherent shift resonance (C*) — exact shifted data at companions

Refereed: r8/U1_notes.md (= U1_head + U1_part1..5, identical up to blank lines between parts, checked with diff), U1_work/*.py (kappa_check,
shift_bound_check, recursion_check2, mixed_fixedpoint_check re-run: outputs identical to U1's report), against paper/martin_density_note.tex
(lem:threshold, eq:margin, def:twopiece, eq:Lstar, lem:twosided, lem:budget, lem:suplevel, lem:switchbudget, lem:peakshift (eq:peakshift,
eq:didentity), def:SC, lem:scrambling, thm:engineered, cor:D1, def:SLD, thm:SLD, lem:martintail) and the refereed Rounds 5-7 (Z3 Theorem E,
Lemma U, Lemma 3.1; Y1 Lemma T; V1 design D_Omega, Lemmas D, S, 3.4', B, DR, TU, CO, ST, NS, RR, Prop. TR, Theorem E'', MT II; V2 Lemmas H, L,
QB, Def. 2.1/2.2, Theorem B (with Step 4), Theorem C1, Theorems E^>=, E^SC, Prop. C3, C4, Lemma C5, Remark 4.5, V2-ref (P1)-(P7), (g3)-(g5);
U4 T_final with U4-ref; U3-ref F6).  Part files r8/U1_ref_part1..5.md; assembled proofs of all fixes r8/U1_ref_notes.md; scripts
r8/U1_ref_work/ (kappa_indep.py, lemma_Rkt_check.py, status_rigidity2.py with outputs; re-runs of U1's mixed-class toys).

## 0. Bottom line
U1 contains several correct and useful new ingredients: the exactness certificate (Lemma 1.1), the data identity with ONE block scalar kappa
(Lemma 1.3, verified to 50 digits by an independent method), the shift bound (Lemma 2.1), the normalization of all scales of a class onto
ONE shift ray by fixed-size increments on the minus side (Proposition 2.2(c)), ZERO-VALUE ABSORBER PAIRS that cancel fine residues on the
coarse coordinates exactly without any d- or kappa-effect (Lemma 3.3, Proposition 3.4), the robust self-aligned recursion that makes (SC) hold
at the companion in configuration (i) (Lemmas 4.1-4.3), the Schauder completion on one ray in configuration (ii) (Lemma 4.4) and a clean
analysis of mixed classes (Lemmas 5.2-5.4).  These close V2-ref's gaps (C*-1), (C*-2), (C*-4), (C*-5) — after repairs.
But the central claim does NOT hold as proved: Theorem 2.3 (exactification with one scalar per block) has a genuine gap.  Its proof asserts that
V1's moves (C1)-(C3) move kappa by <= Design b; the donor raise (C3) moves kappa by (1 - X)[Lam, 3 Lam], Lam = T_lo^3.  Since all peaks act
identically on (theta, A, kappa), U1's kappa-push back to the Lojasiewicz value restores theta and UNDOES the raise, so the strict-non-peak status
of the near-threshold switching carriers (V1 Lemma ST(c), quoted in U1's Lemma 4.5) is lost; computing the Lojasiewicz point after the raise
instead puts it at distance ~ Lam^{2/N_L} >> T_lo^4.  I prove that this is structural (Lemma R-kt): the shifted exact system depends on a block
only through the ratios u_l/kappa (l in Omega), and so do all relative positions of the Omega carriers; with Omega = all coarse strict
non-peaks and only peak pushes as levers, exactness and threshold protection cannot be achieved independently.  V2's "two-scalar" problem
(C*-3) therefore survives in a sharper form (status coherence).  I give a complete fix under an explicit hypothesis (KN): a kappa-neutral
lever (an inactive Omega carrier with robust relative position) in every active block that has an active near-threshold switching carrier.
In addition I found one coverage gap (G1: far parts of the signature sets of coarse NON-owner carriers are neither in E_c nor in J_fine; fixed by
releasing them into J_fine), a mis-stated cone row ((X4); fixed), an inconsistency of the design with T_final's (W6) and an undefined notion of
"main stage" (design D^{U1'} given), and a false step in the proof of Lemma 4.2(ii) (repaired).
Consequently MASTER THEOREM IV and Corollaries IV.1 (finite-F Lemma Z for p_1), IV.2, IV.4 are NOT proved as stated; Master Theorem IV' (with
(KN)) is PROVED after the repairs.  No counterexample is claimed or suggested.  Lemma Z and density of NA((c_0,p_N), l_2^2) (every N, including
N = 1) and of NA((c_0,p), l_2^2) remain OPEN for every admissible T, including D^{V2} / D^{U1}.

## 1. Verdicts
| Claim (U1 label) | Verdict | Main point / fix |
|---|---|---|
| Lemma 1.1 exactness certificate (PROVED) | correct | re-derived; gamma_dec = -Delta theta is the exact analogue of gamma (no extra term) |
| Lemmas 1.2-1.3 identities, data identity, kappa-reduction (PROVED) | correct (identities); the "only one scalar" CONSEQUENCE is overstated | 50-digit independent check (rel. err <= 1.6e-49); kappa is continuous across status changes outside Omega (no "jumps" in U1's IVT); but theta re-enters through the statuses (Lemma R-kt) |
| Lemmas 1.4-1.5 derivatives, tuning (PROVED) | correct as tuning statements | derivatives re-derived and checked by central differences on full recomputations (rel. err <= 3e-27); kappa strictly increasing in the buffer push; Lemma 1.5's parenthetical "margins and gaps >= c_f Lam (V1 Lemma ST)" presupposes V1's raise, which the push itself undoes (see Theorem 2.3) |
| Lemma 2.1 shift bound (PROVED) | correct | re-derived; numerics re-run |
| Activity classes (PROVED) | correct, precision (p-a) | thresholds separated by the full Hoffman constant (incl. 1/lambda); classes may be read off the decomposition data |
| Proposition 2.2 normalization, C*-4 (PROVED) | correct after precisions (p-b) (X4) row mis-stated, (p-c) cofactor minors of the Delta'-projections and aggregation of scaled rows, (p-d) sign preservation of increments; part (b) inherits the gap of Theorem 2.3 | the minus-side normalization is right and neat |
| Theorem 2.3 exactification, C*-3 (PROVED) | GAP (not proved) | false claim "(C3) moves kappa by <= Design b"; kappa-push undoes V1's raise; Lemma R-kt: statuses are functions of the ratios u/kappa; FIX under (KN_{w,a}) (kappa-neutral lever, ratio-space Lojasiewicz); general case OPEN (status coherence) |
| Lemma 2.4 subset averaging (PROVED) | correct | re-derived against Z3 Thm E / V3 Thm 2.5 |
| Theorem 3.1 design D^{U1} (PROVED) | idea sound, definition incomplete and partly inconsistent | (D1) "main stage", ladder and deep-pair deadlines undefined; (D2) absorber targets incompatible with T_final's (W6) (no R exists); (D3) (W2), (W5), (W7) fail at cluster stages (V4's features lost); (D4) sub-window data needed at all stages; corrected design D^{U1'} (pre-pairs + clusters) PROVED admissible, N-free |
| Lemmas 3.2-3.3, Prop. 3.4 exact absorption, C*-1 (PROVED) | correct (Lemma 3.2 under D^{U1'}); trivial precisions | IVT tuning to value zero, biased pair cancels any residue, capacity and no-flip checked |
| Lemmas 4.1-4.3 config (i), (SC), C*-2 (PROVED) | correct for the coordinates covered; gap G1 (coverage) fixed; Lemma 4.2(ii) proof repaired; 4.3 needs the coarse statuses (gap of 2.3) | G1: far parts of closed coarse non-owner signature sets get uncontrolled-sign fine contributions; release them into J_fine |
| Lemmas 4.4-4.6 config (ii), costs, true shift, C*-5 (PROVED) | 4.4, 4.6 correct (with G1); 4.5 cost correct, status claim NOT proved (gap of 2.3) | no jumps (kappa continuous); extra C Design c_{L+1}^2 term from G1 is absorbed |
| Lemmas 5.1-5.4 mixed classes (PROVED) | 5.2-5.4 correct (5.3: constant precision 2^{m+k}); 5.1 inherits the gap of 2.3 | toy (5.5) reproduced (148/115/114/134/1) |
| MASTER THEOREM IV (PROVED) | NOT PROVED as stated | PROVED as IV' with (KN_{w,a}) after all repairs |
| Corollary IV.1, N = 1 (PROVED) | NOT PROVED | (K4) carriers of an active negative block are forced active, so (KN) is a real restriction even for N = 1 |
| Corollaries IV.2-IV.4 (PROVED) | IV.4's reduction "I_up or I_lo empty => one-signed" correct; conclusions need (KN); IV.2 must add "or (KN) fails" | — |
| (C_mix) follows from U3's (S2) (SKETCH) | plausible SKETCH only; inherits the gap of 2.3 and (S2)'s junction mismatch (U3-ref F6) | a fixed violation at a fixed companion is tolerated by Lemma VT only above s_1 ~ eps_j |
| Corrections 5.8 | near-coordinate conversion FALSE as stated: agree; "two-scalar exactification unnecessary": DISAGREE | see F1 |

## 2. Main findings (proofs in U1_ref_notes.md)
F1 (status coherence; Theorem 2.3).  Lemma R-kt (PROVED): for a block with peak set P and switching set Omega ⊂ Q, a := A/theta and
k := kappa/theta satisfy a^2 = Phi_P^2 + k^2 R^2 + S_f/theta^2, k = a + Phi_P^2 + S_f/theta^2 (R^2 = m^2 sum_Omega (u_l/kappa)^2, S_f = fine terms),
and rho_l = m (u_l/kappa) k/Phi_l.  Hence the relative positions of all Omega carriers are functions of the ratios r = u/kappa (up to O(c_{L+1}^2)),
and the exact shifted system depends on the block only through r.  V1's raise = uniform rescaling of r; restoring r restores every status
(numerics: rho changes 1e-22 after restoring the ratios; theta returns exactly when kappa is restored by a second peak push).  Fix (PROVED)
under (KN_{w,a}): an inward push of an INACTIVE Omega carrier with rho >= u changes theta at first order and kappa only by
rho M X/C = O(c_{L+1}^2 D^2) per unit (Lemma 1.4(c)), so it lowers k = kappa/theta and every active rho at FIXED active ratios (numerics:
active rho drop 1.2e-4 ... 2.1e-4 with kappa and the active ratios exact to 1e-41).  Without a lever the residual is: the exact zero set of
the tiny minors near r(f) lies in {rho_d >= 1} for an active near-threshold switching carrier d (OPEN).
F2 (G1, coverage).  U1's J_fine excludes the far parts of the class-G coarse signature sets (closed by (C1)); E_c contains only the near parts.
U1 covers the far parts of OWNER coarse carriers by dominance, but not those of inactive Omega carriers and of coarse peaks of inactive
blocks, where V receives later fine contributions of uncontrolled sign.  Release them into J_fine (cost and value changes <= 4 c_{L+1}^2).
F3 (design).  (D1)-(D4) above.  Most serious: absorber targets need 2^{3-R} <= mu_{p_0}^2 c_p^2/4 while (W6) forces c_p <= K 3^{-R}; no R exists.
D^{U1'}: rounds PRE (absorber pairs for the signature coordinates of the next main target) - MAIN - CLUSTER; no (W6) at absorber stages (R
chosen from a lower bound of c_p independent of R); sub-window data at every stage; windows used at main stages.  Lemma 3.2 then holds without
deadlines.
F4 (the cone).  (X4) must read vs gamma_l/lambda_l + Delta'_m >= 0 (design coefficients), on every near-threshold strict non-peak of f^# in Omega;
"vs gamma >= 0" is violated by the decomposition by lambda Delta' in configuration (ii) and does not give kind [3] in configuration (i).
Class-R near-threshold strict non-peaks and (P-ii) carriers pin Delta'_dec >= -C_f D K_g t, so they never sit in an active negative block.
F5 (Lemma 4.2(ii)).  "c_{k+1} <= b(k, M(k))^2" is false inside clusters; the conclusion holds because no later cluster carrier meets k's
coordinates except its partner, and the next non-absorber stage has weight <= b(previous)^2.
F6 (what is right and new).  Zero-value absorbers (value exactly 0 => no d-effect, no kappa-effect, any residue cancelled by a biased pair,
capacity c_{L+1}/(Design t)); the minus-side normalization to one ray; the self-aligned recursion producing (SC) for ANY sequence; the
Schauder completion on one ray; the three-state analysis and frustration in mixed classes; the Cantor-set refutation of V2's conversion.

## 3. Attacks attempted
weak* vs norm (Schauder continuity in the product topology, costs in p* via Z3 Lemma 3.1; no weak* limit is taken in the data); uniformity in t
(one companion per (class, cube); configuration (i) admissible for every shift of the class; increments of fixed size, not O(t)); in the window
(D_cls(w) = (Design/u)^{C}, C_f factors absorbed for large L; |S| >= n/D_cls^2); in the number of active carriers (patterns over subsets of
[1,L]; ~2|E_c| tuned absorbers, finite, joint scalar fixed point); along companions (one per main stage; absorbers' masses <= C_f c_{L+1} T_hi);
simultaneous exactifications (FOUND: kappa-push vs donor raise, F1); Hoffman/Farkas/minor constants (aggregation of scaled signature rows;
cofactor minors; Lemma H only needs nonzero minors); design N-independence (absorbers in block 1); admissibility ((W4) at every stage; FOUND (W6)
inconsistency, F3); well-foundedness (R defined from c_p^low); non-attained infima (Lojasiewicz points exist; IVT exact since kappa continuous);
signs and one-sidedness ((X4) mis-stated, F4; increments keep signs via (X2) at the robust peak of every block); near-contacts vs contacts (far
coarse parts: G1); c_0 vs l_infty (companions with z in l_infty allowed by Theorem E''); finite vs infinite (E_c finite, F^# finite, infinitely many
fine carriers handled by dominance / Schauder); hidden assumptions on T ((W3) at cluster stages automatic; (W4'') needed and present);
quantifier order (design -> f -> main stage, clean w -> class, cube -> companion -> g, rho -> data at each t; classes must be fixed before the
exactification in the (KN) fix — legitimate).  Suspected problems examined and REFUTED: kappa jumps (none); minus-side increments changing the
represented functional (no); absorbers changing kappa (no: nu = 0); the robust recursion failing (no, with (W4'')); (SC) along a common
sequence (any sequence works).

## 4. Numerics (sanity checks; r8/U1_ref_work/)
kappa_indep.py: independent norming routine (clamp parametrization, 50 digits): (E1), (E2), both kappa forms, identity (1.3) exact to <= 1.6e-49;
Lemma 1.4 (a), (b), (c) by central differences on full recomputations: rel. err 1.7e-27, 3.3e-27, 1.9e-21.
lemma_Rkt_check.py: Lemma R-kt on 56 random blocks: a^2 = Phi_P^2 + k^2 R^2 + s_f, k = a + Phi_P^2 + s_f, rho_l = m r_l k/Phi_l exact to 2.3e-41;
R < 1 (min 1 - R = 0.143) and a > kR (min 0.016) on all tests.
status_rigidity2.py: (1) donor raise: dkappa/Lam = 1.0, dtheta/Lam = C/Phi_P^2 (3.6328596 vs 3.63286); (2) kappa restored by a second peak push:
theta - theta_0 = 0 (raise undone); (3) active ratios restored: rho changes 1e-22 (no inactive lever) — status protection impossible;
(4) with an inactive robust Omega carrier: active rho decrease 1.2e-4 ... 2.1e-4 at fixed kappa and fixed active ratios (the lever works).
U1's scripts re-run: kappa_check (identical), shift_bound_check (5220 tests, sharp), recursion_check2 ((W4'') necessary: 27% failures without),
mixed_fixedpoint_check (148 mixed, 115 with exact completions, 114 good, 134 frustrated, 1 without good completion: identical),
mixed_forcedW_check (3 instances with forced wrong branches; instances without a good completion for band widths 0.004 / 0.0004 / 0.00004:
1 / 0 / 0: identical).  These toys are lexicographic and say nothing about the status-coherence gap (they fix all coarse data).

## 5. Single most valuable idea
ZERO-VALUE ABSORBERS: a biased pair of block-1 carriers whose targets carry fresh binary tuning coordinates, tuned at the companion to value
EXACTLY zero, carries any switching coefficient without d-effect and without kappa-effect; placed as the first touchers of every coarse
coordinate after a main stage, they cancel the fine residues on the coarse coordinates exactly.  This turns "absorb the fine part on the
coarse coordinates" (V2's C*-1) into bookkeeping.  (Runner-up: normalization of all scales of a class onto ONE shift ray by fixed-size
increments on the minus side only, which is what makes one Schauder completion serve all scales.)  The referee's complementary insight
(Lemma R-kt): statuses of switching carriers are functions of the ratios u/kappa, so a kappa-neutral lever is the exact missing ingredient.

## 6. What remains open after U1 (+ this report), design D^{U1'} (on T_final), diagonal mu-base, finite I
(1) STATUS COHERENCE (refined (C*-3)): an active block with an active near-threshold switching carrier and no inactive Omega carrier of robust
    relative position, at which the exact zero set of the tiny minors (ratio space) near r(f) forces that carrier onto or above its threshold.
    Routes: (KN) lever (done); taking near-threshold carriers with INACTIVE excess out of Omega with the continuous coefficient
    -Delta' lambda min(rho, 1) vs (SKETCH); a GENERIC design making (rho_d)_{d in N} transversal to (1, ..., 1) on every exact zero set
    (HEURISTIC; needs a construction and quantitative stratification, ref notes 3.4).
(2) (C_mix): (SC) for the negative blocks at an exact completion of a mixed class (frustrated positive carriers; bad wrong-branch carriers in
    bands of width ~ Phi^{1/2}).
(3) Infinite F: (E1)-(E5) of ADDENDUM 7 (U2's items).
(4) Transfer to Martin's p: hypotheses of IV' are not N-independent (lem:martintail transfers density, not rows).
Lemma Z and density of NA((c_0,p_N), l_2^2) for every N (including N = 1) and of NA((c_0,p), l_2^2): OPEN for every admissible T.
