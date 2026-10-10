# Referee report on V4 (Round 7): designing away the residual configurations; adversarial search in the residual classes

Refereed: r7/V4_notes.md (supersedes V4_part1..5 where they differ; part files read for Lemma 1.3 and the requirement analysis),
V4_work/sa_check.py and degenerate_check4.py (re-run, outputs identical), against paper/martin_density_note.tex (lem:threshold, eq:margin,
prop:forced, def:twopiece, def:BT, prop:onesidedupper, thm:onesided, def:engineered, lem:approxfacts, def:SC + remark, lem:scrambling,
thm:engineered, cor:D1, cor:BTrecovered, def:SLD, thm:SLD, lem:budget, lem:suplevel, lem:box, lem:switchbudget, lem:split, lem:peakshift,
def:swallowed, lem:modswallow, lem:badpeaks), Round 5 (Z3 Lemma U, Lemma 3.1, Theorem E, peak-ification sketch 6.1; Z4-ref (H2''), Remark 3.3),
Round 6 (Y2 Lemma 5.1, Prop. 5.2, 5.3; Y3/Y3-ref flip profiles and (O4-crit); Y4-ref Lemma P2, Prop. P4) and Round 7 (V1-ref, V2-ref).
My part files: r7/V4_ref_part1..5.md; assembled proofs of all fixes: r7/V4_ref_notes.md; scripts: r7/V4_ref_work/.

## 0. Bottom line
V4 is mathematically sound: every claim labelled PROVED is correct or correct after a fixable precision, and I found no error that changes
a conclusion.  Three statements need repair: Proposition 2.4 is literally false (trivially fixed: the dominant index must be the FIRST
non-zero one); the proof of Remark 2.3(1) (weak aligned corner) has a gap (coarse sign switches along the tuning sweep), which I close with a
hysteretic sweep and an approximate intermediate value argument (Lemma R1); and for p_N with N < infinity all owner notions and owner
recursions must be taken relative to the present carriers L_N (otherwise Theorem 2.2(e) and the (T2) check of Lemma 5.4 can fail at
coordinates owned by absent carriers) — Lemma R3, after which everything holds for every N with an N-free design.
The two substantive positive results are right: (i) Construction SA / Theorem 2.2 — explicit block-tame first rows with EXACT coherent shift
resonance, so configuration (C) (and, in weak form, (D)) occurs for every design with (SF*), (Z0) but is a residual of the window method, not an
obstruction (I re-checked it at 120 digits, since V4's double-precision run sits at one ulp); (ii) Theorem 5.6 — exact two-piece data with
Delta d_m < 0 in every block and no dead zones are recovered, via owner-aligned fine re-alignment + bank levers + (SC)-companions.  Proposition 5.3
upgrades Z3's peak-ification SKETCH to PROVED: (BT) rows are dense among F-finite rows (for designs with (SF*)).
Two scope facts are missing from V4's summary and change the reading of Section 12: Theorem 5.6's hypotheses force MAXIMAL CONTACT (Lemma R10),
and exact all-negative data exist only on a MEAGRE set of every fixed-z fibre (new Proposition R5).  So the companion route with exact data can
never reach generic rows; for F finite the decisive open problem remains V2-ref's window residual (C*), not V4's dead zones.  Lemma 2.6
(lacunary profiles exclude critical flip profiles) is correct but the remedy is costly (it destroys bounded gaps, on which Y3's D_sigma,
Y4-ref's exact pull tuning and V1's D_Omega rely, and it leaves MIXED profiles open).  No counterexample is claimed; nothing I checked
points to one.  Lemma Z and density of NA((c_0,p_N), l_2^2) remain OPEN for every admissible T.

## 1. Verdicts
| Claim (V4 label) | Verdict | Main point / fix |
|---|---|---|
| Lemma 1.1 value formula (PROVED) | correct | re-derived; in fact |val_l| <= q*(u_l) = 1 |
| Lemma 1.2 forced sharing (PROVED) | correct | convergence along a subsequence; links can also go through S_{l_1} ∩ supp y_{l_2} |
| Lemma 1.3 shift fed by negative d-weights (PROVED) | correct, fixable gap | display correct; the "free shift <= (6M/(Ct)) sum_{q<0} Phi^2 + O(t)" bound drops the q > 0 swallowed non-peaks; needs (H1) of def:swallowed (lem:modswallow(b)) or include them (R4) |
| Requirements table (PROVED) | correct as classification, overstated as inference | "no DO relation" does not mean "cannot be designed away" (FR systems can be: V4's own Lemma 3.4 under (GM)); non-excludability rests on realizability: (C) proved, (D) weak form after R1, (B) SKETCH and moot after V2 Theorem B |
| Lemma 2.1 designability (PROVED) | correct, fixable gap | the recursion order must be S_l, delta_l (GM), y_l by allowedness (a), then c_l as a minimum of upper bounds (R6); tau_l -> 0 must be added (R11) |
| Theorem 2.2 self-aligned rows (PROVED) | correct (with R3 for N < inf) | Steps 1-9 re-derived; c_*(l) = 0 for every l; for p_N the recursion must run over L_N (R3); 120-digit re-check |
| Remark 2.3(1) weak aligned corner (PROVED) | correct statement, proof gap fixed | pure owner rule may switch coarse carriers inside the sweep; hysteretic sweep + approximate IVT (R1); exact degeneracy OPEN (V4's label correct) |
| Remark 2.3(2) (B) core (SKETCH) | plausible sketch, moot | needs N >= 2, four switchable carriers, two links; superseded by V2 Theorem B |
| Proposition 2.4 single-vector principle (PROVED) | false as stated, trivially fixed | counterexample V_1 = 10, V_2 = -1 at j; take i(j) := first non-zero index (R2) |
| Proposition 5.1 Baire genericity (PROVED) | correct | any eps_l -> 0 suffices; one contact (even none) suffices; "dense" in (b) refers to {F finite}, not the fibre |
| Lemma 2.6 lacunary profiles (PROVED) | correct | proof re-derived; as a design remedy it conflicts with bounded gaps (D_sigma, Y4-ref (G), D_Omega) and leaves mixed profiles |
| Corollary 3.1 (PROVED) | correct | cor:BTrecovered; (b) for the R1 rows; "finitely-tuned variant" should be defined (owner rule above K, finitely many non-degenerate exceptions) |
| Proposition 3.2 coherent-shift mates (PROVED) | correct | identity, side admissibility, V(zhat) = 0, c g in C(f) via onesidedupper re-derived; 120-digit check |
| Lemma 5.2 threshold Lipschitz / monotone (PROVED) | correct | re-derived (one-sided derivative of Psi) |
| Theorem 3.5 + Proposition 5.3 (PROVED) | correct | hysteretic re-run, affine lever, Lemma 5.2, block-by-block gaps re-derived; upgrades Z3 6.1 (SKETCH) to PROVED; margins "beyond the first peak" read at f^(L) |
| Lemma 3.6 / Theorem 3.7 (PROVED) | correct, fixable gap | transplant re-derived; with banks rebalance by a 1_F to keep contact-likeness (R8); Lemma U applied with fixed omega (r_1 uniform) |
| Lemma 3.8 (SC) from generic threshold (PROVED) | correct, fixable gap | needs a NONINCREASING summable majorant (under (SF*): 2^{-j(k,m)-7}); single block only (def:SC needs a common sequence) (R7) |
| Lemma 4.1' / Proposition 4.2' owner alignment (PROVED) | correct (with R3) | three dominance cases re-derived; for Delta d > 0 the same proof forces anti-alignment |
| Lemma 4.4 perturb-and-realign (PROVED) | correct | flip needs delta°_l <= 2C|p|; lambda_l <= delta°_l 2^{-l-9}; not used by 5.6/5.7 |
| Theorem 5.6 (+ Lemmas 5.4, 5.5) (PROVED) | correct; scope must be stated | (SF_tau) gives perturbations << tau_o for ALL o <= L at once (checked); hypotheses force maximal contact (R10); meagre in every fixed-z fibre (R5) |
| Corollary 5.7 (PROVED) | correct for N = 1; fixable for N >= 2 | Delta d_m < 0 needed in every block; non-negligibility |Delta d_m||w| >= 2 tau C_1 (R9); existence of exactly degenerate self-aligned rows OPEN (clause is conditional) |
| Proposition 5.8 positive mismatch (PROVED) | correct | re-derived; (FD) is used only for this negative statement |
| Proposition 4.6 sequential projection (PROVED) | correct | Y4 Lemma 1.8 and sliced rays re-derived; the OPEN (B) step is superseded by V2 Theorem B |
| Structure of a counterexample (PROVED) | correct (logical) | contrapositive of cor:D1 + Thm 5.6; by R5 its first alternative (no exact data) is the generic one |

## 2. Main findings (proofs in V4_ref_notes.md)
F1 (Theorem 2.2 and Proposition 3.2 are right; high-precision check).  Every step re-derived (IVT tuning; well-definedness of the recursion
by allowedness (a); robust peaks from (SF*); dominance in three cases; c(1; l) = 0 by the W-sum; (MS) and (SC)).  V4's double-precision
script tunes n_- val_- to -4.7e-16 (one ulp).  My 120-digit re-run (sa_check_dec.py, (SF*)-type weights) gives n_- val_- = -4.18e-60 = target,
nu_-/theta = 0.25, q_- = -2.3e-59, all other nu/theta in [5, 8.4e124] with the owner signs, W and V z-signed, V(zhat) = -6.5e-121,
Delta d/Delta alpha = -5.4e-118, N(w) - 1 = 1.4e-117.
F2 (Remark 2.3(1): gap and repair R1).  With the pure owner rule, any of the l_D - 1 coarser carriers may switch inside the sweep needed to
move l_D's relative margin over (0, xi_0) (row-dependent |A_l| can be smaller than the sweep), and a coarse switch moves theta by ~lambda_l.
Hysteresis: a coarse flip needs a change >= delta_l H_l/2, while the sweep is O(theta^max Phi_{l_D}) and (SF*) gives c_{l_D} <= delta_l H_l 2^{-l-12};
no carrier below l_D flips, later carriers move zeta by <= 2 sum_{l>l_D} lambda_l, and a sup-argument gives every relative margin up to
epsilon' = 4 L_Theta sum_{l>l_D} lambda_l/theta_0 (no flip counting needed).
F3 (owners for p_N, R3).  V4's recursion and owner run over ALL carriers.  For N < infinity a coordinate owned by an absent carrier gets that
carrier's sign, while every p_N quantity (c_*-vector, d-row) is dominated there by the first PRESENT carrier; signs need not agree.  With
L_N-relative owners every dominance bound survives (they are upper bounds over all later carriers), Lemma 1.2(b) still assigns every
coordinate, and all of V4 holds for every N.
F4 (scope of Theorem 5.6, R10, and non-genericity, R5).  (H1) + (H2) force D(j) != 0 at every j notin F, hence |z_j| = 1 off F: Theorem 5.6 is about
maximal-contact (sign-mixed) rows — exactly where V2-ref says (C*) is not excluded, so it is a real complement there.  But by a Baire argument
(windows on the misaligned side of zero, plus Prop. 4.2'), in EVERY fixed-z fibre the set of a admitting exact all-negative data is meagre.
Hence the exact-data companion route acts on a meagre set; the generic F-finite row needs window data, whose residual is (C*).
F5 (smaller precisions).  Lemma 1.3 (R4), Lemma 2.1 order and tau_l -> 0 (R6, R11), Lemma 3.6 rebalancing with banks (R8), Lemma 3.8 (R7),
Corollary 5.7 for N >= 2 (R9), Proposition 2.4 (R2).  (FD) is a purely negative design condition and should not be part of a unified design.
F6 (relation to the rest of Round 7).  (B): V2 Theorem B (refereed correct) removes multi-block rays for D^{V2}; V4's Prop. 4.6 is correct but
superseded.  (D): V1's Corollary AC removes the aligned corner for D_Omega; V4's Remark 2.3(1) only shows the configuration exists.  (C): V4
proves exact coherent resonance occurs at (BT) rows; whether f_SA realizes V2-ref's rate-object form (C*) (rho^sh <= b AND c_pi <= b at clean
sub-windows) is plausible but not checked by V4 (immaterial since f_SA is (BT)).  V4's design conditions are upper bounds on weights, a
factor-2 freedom in delta_l and target additions supported in Z_0 (= the odd numbers for D_Omega), so they APPEAR compatible with D_Omega /
D^{V2} and all Round-7 results could live in one design; a line-by-line check against V1's and V2's design constants is not done here.

## 3. Attacks attempted (none broke a PROVED claim after the fixes)
weak* vs norm (transplanted G^# -> g in l_1; R^*w^# -> R^*w in l_1 by Z3 Lemma 3.1; f^(L) -> f in p*); uniformity in t (Theorem 3.7 uses FIXED
data: Lemma U with fixed omega, gaps >= gamma_0/2, t := t_1 gives one r_1 for all i); in the window (only Lemma 1.3 is window-based;
the 6t^2 fine bound needs t in W(l_*)); in the number of active carriers (K_omega, Neg, E' finite; infinitely many fine carriers handled by
dominance whose constants are design thresholds; (SF_tau) makes the coarse perturbation << tau_o uniformly in o <= L); along companions (diagonal
choice L_i -> infinity, then mu_i -> 0); simultaneous exactifications (levers and banks block by block with preserved gaps dgap_m; first-order
effects private by the diagonal base); Hoffman/Farkas constants (only in Prop. 4.6, superseded); design N-independence (conditions over the
full ladder; row constructions L_N-relative, R3) and admissibility (Lemma 2.1 with R6; (T-d) easier); non-attained infima (c_*(l) = 0 attained
by an explicit x); signs and one-sidedness (data convention Delta d = d(omega^-) - d(omega^+); anti-alignment for Delta d > 0; Lemma 1.3 one-sided
with the missing q > 0 term); near-contacts vs contacts (Theorem 5.6 forces exact contacts; levers create free coordinates, banks do not);
c_0 vs l_infty (all rows are non-attaining with z in l_infty, allowed by thm:engineered); finite vs infinite (F, F^#, Q_m at companions finite;
K infinite); hidden assumptions on T ((SF*), (SF_tau) with tau -> 0, (b'), (Z0), (GM), (FD) are explicit design choices; Prop. 5.1 for every
admissible T; U diagonal is a free choice); quantifier order (design -> N -> f -> data -> L_0 -> L -> mu -> rho; in R1: l_c, theta_0 -> l_- -> eta ->
l_D -> x).  Suspected problems examined: (i) absent-block owners (real; fixed by R3); (ii) coarse switches in tuning sweeps (real; fixed by
R1); (iii) bank rebalancing destroying contact-likeness (real but trivial; R8); (iv) tau_l not tending to 0 making negligibility vacuous (R11);
(v) a hidden circularity in Lemma 5.4 between L_0 and the perturbation bounds (none: L_0 depends on f and the data, the bounds on the
design); (vi) whether Theorem 5.6 needs (SC) at f (no: (SC) is produced at the (BT) companions).

## 4. Numerics (sanity checks only)
sa_check.py and degenerate_check4.py re-run: identical to V4's report (degenerate_check4's base point has nu_D/theta = 0.9999987, a strict
non-peak at the double-precision limit, as V4 says).  sa_check_dec.py (new; decimal arithmetic at 120 digits through the shim decimalmp.py,
since mpmath is not installed): Theorem 2.2 / Proposition 3.2 confirmed away from round-off (F1).

## 5. Single most valuable idea
Exact data with negative d-mismatch are RIGID — at every coordinate owned by a non-neutral, non-negligible carrier they force z to be
owner-aligned (Prop. 4.2') — and the owner rule under (SF*) (with hysteresis and levers or banks) produces, next to any F-finite row, block-tame
rows that agree with it on any prescribed coarse part (Prop. 5.3).  Together: the re-aligned (BT) companion keeps the d-row z-signed, so the
exact data transplant to it and (SC) is MANUFACTURED at the companion instead of being assumed at f (Theorem 5.6).  (Runner-up: Construction
SA — explicit (BT) rows with exact coherent shift resonance, which shows that (C) is a residual of the window method, not an obstruction.)

## 6. What remains open after V4 (+ this report)
Lemma Z and density of NA((c_0,p_N), l_2^2), hence of NA((c_0,p), l_2^2), remain OPEN for every admissible T, including D_Omega / D^{V2}
augmented by V4's design conditions.  Precisely:
(1) F finite, generic rows (no exact two-piece data; Prop. R5): V2-ref's (C*) — at all but finitely many levels every clean sub-window has
    rho^sh <= b(w) AND c_pi(w) <= b(w); V4 shows (C) occurs at (BT) rows but gives no general recovery of (C*)-rows.
(2) Exact data with dead zones (a meagre class): mixed data (some Delta d_m < 0, some >= 0), neutral carriers, infinitely many negligible
    carriers, D vanishing on E'; V4's "stability of nearly exact data at (BT) companions" is a correct formulation of the missing step;
    pulling the violated coordinates leads to infinite support when they are infinitely many.
(3) Existence of self-aligned rows with an EXACTLY degenerate swallowing-type peak (illustrative only; immaterial for D_Omega).
(4) Infinite F: (O4-crit) (excluded only by lacunary designs, which lose bounded gaps and create MIXED profiles, uncovered), (O4-nd), (O4-box).
(5) Design questions: (C) and weak (D) are realized for every design with (SF*), (Z0); designs violating (SF*) are not analysed (Remark 2.5,
    HEURISTIC); (GO) is negative for every admissible design (Prop. 5.1).  (B) is no longer a residual for D^{V2} (V2 Theorem B).
No counterexample; nothing points to one.
