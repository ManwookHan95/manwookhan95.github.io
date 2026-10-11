# Referee report on H2 (Round 13): the residual (R1) of Step A -- thin rows, pure (U*) certificates

Refereed: r13/H2_notes.md (with H2_part1..5.md and H2_work/).  Checked against: J1/J1-ref (R-PK, R-PB, F-2, P-TU, J1.13, J1.15'), J2/J2-ref ((FC),
weak-peak data signs), K2 notes 1-2, 4.1, 5.1-5.4, 6.1-6.4 (kinds, K2.16, K2.17, (K2-c), (K2-d), (L-K2-1/2)), K1 notes 1.0-1.5, 2.0-2.2, 3.1 and
K1-ref R-6, Q1 notes 1.1-1.4 (T_fin rounds, absorbers, (W_exp)), X1 1.1 (Lemma K), H1 Lemma TF'/NP.  Proofs of every verdict and fix:
r13/H2_ref_notes.md (part files H2_ref_part1-3.md).  Scripts and outputs: r13/H2_ref_work/.  Role: adversarial referee.

## 0. Bottom line
H2 does not exclude (R1) and does not claim to; it reduces it.  The reduction is sound in its main lines:
 - At an (R1) stage every tuned row is privately tunable (kind (i)) or one-sided upward (kind (iv)); h = 0, so every near-certificate is of
   pure type (U*); every unshifted block has a private two-sided peak resource; every shifted block has a one-sided kappa lever of direction
   -sgn Delta''_m (Facts 1.1/1.2).  Re-derived.
 - Theorem H2.A: one-sided overshoot bands on all free K^- rows and all bandable free K^+ rows realize Step A unless some block is residual
   (two/up/down with pinned or locked rows).  The proof combines the all-at-once positivity sum_{(iv)} y_l >= c_1/4 with the per-block lever
   balance; re-derived, numerics reproduced, plus an independent model.
 - Cross-stage memory (Lemmas 2.3, 2.6, 2.7): a kind-(iv) carrier of an (R1) stage is inactive at the next (R1) stage, switching signs never
   flip, (up)/(down) blocks become unshifted.  Re-derived, including the design arithmetic of the cluster sweep.
Problems found:
 F-NE (5.4 and bottom line (6); the argument FAILS).  The claim that, under near-exactness and a bias-free preparation, the pinned residual
   disappears in unshifted blocks and in shifted blocks without near-threshold actives rests on a design clause (start row within delta_Z of
   Z_kappa, "b only an upper threshold").  The clause contradicts (K2-d) theta_0 = b/Design^{C_P} together with (L-K2-1) s_1 <= theta_0 T/(8 rho
   A_0): these force b >= 8 rho A_0 Design^{C_P} s_1/T, while delta_Z <= delta s_1/(64 rho C_f Design^C), and a tiny minor with value in
   (Lip delta_Z, b] is admissible.  Wrong-sided resonances of size in (delta_Z, C b] therefore remain in every block type -- as H2's own 5.3
   says.  The "inward-locked near-threshold core" is not established.
 F-COR (Corollary 4.2; FALSE as stated).  With several tiny minors a Farkas certificate can combine them.  Explicit counterexamples:
   M_1 = x_1 + y, M_2 = x_1 + 2x_2 + 3x_3 + y (every minor has a two-sided cofactor), and M_1 = x_1 - x_2, M_2 = x_2 - x_1 + x_3 + x_4 (mixed
   signs in every minor); both residual iff a positive combination is positive at the start.  LP-verified.  Repair: full row rank of the
   two-sided cofactor matrix.
 G-CPL (Theorem H2.A; fixable gap).  The K^+ bands of (U)-blocks need J1-ref F-2's coupled rescaling of all block targets.  The band inequality
   must be read at the coupled targets and closed with R-PK, phi_y(s) = phi_y(1) + kappa_m(1 - s) zeta_m(y; rt(1)), not with ||b(s)||; done in the
   ref notes.
 Precisions: P-41 (Proposition 4.1 is exact only in a restricted single-block model: other blocks fixed, private generators only, no margin;
   "EXACTLY" overclaims), P-25 (Lemma 2.5's sort (4) "unaffordable" is relative to cost upper bounds only; a cushion bound misstated), P-31
   (theta_0 term in the one-sided lever bound), P-RANGE/P-AGG (pull range up to x''_max needs R-6's redefinition; pre-place a subset of
   pulls), P-OWN (memory proof cites Step-B ownership; the correct reason is tiny signature room), P-52 (bias also at target coordinates; a
   robust cofactor is needed), Q-1/Q-2 (quantifiers of Theorems H2.B and H).
Neither (LSC-trunc)_N for every f nor density of NA((c_0, p_N), l_2^2) or NA((c_0, p), l_2^2) is claimed or implied.  No counterexample is claimed,
and nothing found points to one.

## 1. Verdicts
| Claim (H2 label) | Verdict | Main point |
|---|---|---|
| Fact 1.1 / 1.2 (PROVED) | correct | (R1) excludes thick near coordinates directly; h = 0; weak-peak orientation consistent (J2 1.3) |
| Lemma 2.1 (PROVED) | correct | anchor or thick private coordinate of a coarse carrier; K2.16(4) at every s <= D(L) |
| Lemma 2.2 (PROVED) | correct | induction over main/PRE/cluster targets; (D-enum) not needed |
| Lemma 2.3 (PROVED, (D-enum)) | correct with precision | s_max(p+1) >= 4/T_lo(p, M(p)) re-derived; (D-enum) used for p', p''; P-RANGE |
| Lemma 2.4 (PROVED) | correct with precisions | P-RANGE, P-AGG |
| Lemma 2.5 (PROVED) | correct for the certified toolbox | P-25; not load-bearing |
| Idea (1) literal (FALSE) | correct | zero pull capacity at anti-sign support |
| Lemmas 2.6, 2.7 (PROVED) | correct | K1.3(S) at the next stage; flip budget at (near-)contacts; P-OWN |
| Proposition 3.1 (PROVED) | correct with constant precision | P-31 |
| Lemmas 3.2-3.4 (PROVED; 3.4(c) SKETCH) | correct; 3.4(a) needs G-CPL; (c) SKETCH honest | sigma in Lemma K depends on the peak pattern only |
| Theorem H2.A (PROVED) | correct with a fixable gap | G-CPL; numerics 4000/4000 and 699/699 |
| Proposition 3.5 ((d) HEURISTIC) | correct | (a) vacuous in (R1); (d) honest |
| Proposition 4.1 / Cor 4.2 / Ex 4.3 (PROVED) | 4.1 correct in a restricted model; 4.2 FALSE as stated (repaired); 4.3 correct algebra | P-41, F-COR |
| Lemma 5.2 (PROVED) | correct with precisions | P-52 |
| Prop NE + bias-free preparation (SKETCH) | conclusion WRONG | F-NE |
| (D-abs) long memory (SKETCH) | consequences re-derived; compatibility pending | label honest |
| Theorems H2.B / H (necessary conditions) | correct with quantifier precisions | Q-1, Q-2 |

## 2. Attacks attempted
- Semialgebraic uniformity and constants: cofactors are rate objects (tiny or robust), so "charging" rows need robust cofactors (P-52).  The
  Lojasiewicz/near-exactness clause fails against the preparation's lower bound on b (F-NE).
- Puiseux margin: K^- shrinking bands lower every status (Lemma K: sigma = Phi_P^2 + s_f is pattern-only), so the margin only improves.  K^+
  bands are allowed only in (U)-blocks (coupling) or unprotected shifted blocks.
- Exactness on Z_kappa: pinned rows are never banded; Corollary 4.2's shortcut is false (F-COR).
- (FC) consistency: realized statuses are <= target statuses (K^-), or rescaled (K^+ in (U)-blocks).
- Cushion domination: bands create no support.  Aggregated pulls carry cushions 24 lambda_l v >= t|c_l| v.  Banks sit at aligned S_th coordinates.
- (VT) tolerances: used only in Proposition NE (SKETCH); delta_Z << s_1 << theta_0 << b is exactly what defeats 5.4.
- Closeness K t and cost o(c_flat^2 T^2): pull range up to x''_max costs O(u^2 T^2/(Design^{C-2} log(1/T))) in total.
- Lowering/pull admissibility at the companion: pullability must be re-defined with x''_max (P-RANGE).
- N-independence and well-foundedness: (D-enum) only orders a countable pool and is N- and f-free.  (D-abs) is N-free; the (W4'') list is
  still to be re-checked.
- Signs: weak-peak switching sign = data sign on private coordinates; the peak-bank direction -sgn Delta''_m is the same for all robust peaks;
  the one-sided column carries an extra +|kappa| theta_0 (P-31).
- Quantifier order: Q-1 (every clean sub-window/class), Q-2 (memory needs consecutive (R1) stages).
- Coverage: not every (R1) stage is covered.  The residual is the H2.A residual, contained in the restricted Farkas class only for single blocks
  (P-41).
Counterexample: none.

## 3. Numerics (sanity only; r13/H2_ref_work/)
- rerun/: H2's toy_onesided (4000/4000) and toy_resonance (3000/3000; Example 4.3) reproduced; outputs identical.
- ref_cor42.py/.out: both counterexamples to Corollary 4.2 (feasible at -1e-4, infeasible at +1e-4).  Full-row-rank repair: 0 infeasible
  instances in 2000 random tests.
- ref_h2a_shared.py/.out: independent H2.A model with common-mode perturbations of the private columns.  Non-residual: 699/699 feasible.
  Residual: 801 configurations; 654 had a privately infeasible right-hand side, and 478 of those became feasible with two random shared
  two-sided columns.  So the residual is a necessary condition, not a sufficient one.

## 4. Single most valuable idea
Cross-stage memory through the cluster sweep.  After a main stage p, the cluster absorbers push s_max beyond 4/T_lo(p, M(p)).  So every
coordinate a kind-(iv) carrier relied on at p becomes, at the next main stage, a private, unraised, design-depth coordinate on which (R1)
forces |a| <= b.  This covers its data-sign near coordinates and its anti-sign far pull range.  K1.3(S) and the flip budget then forbid the
carrier from being active again with either sign.  Consequences:
 - one-sided obstructions cannot be reused;
 - (up)/(down) blocks become unshifted;
 - with (D-abs), each (carrier, sign) is used at most once per round range.
Combined with Theorem H2.A (one-sided bands on all movable kind-(iv) rows at once), persistent (R1) needs a FRESH, pinned, wrong-signed
resonance at every main stage.

## 5. What remains open (precise)
(1) (R1) at all large main stages.  At every clean sub-window and class some block is residual: (two) pinned K^- rows and pinned-or-locked K^+
    rows; (up) pinned K^- rows; (down) pinned-or-locked K^+ rows.  The resonance must be fresh at consecutive (R1) stages.
    - Single unshifted blocks (restricted model): a wrong-signed one-signed linear resonance of tiny minors.
    - Not yet written: the joint multi-block Farkas form, the effect of shared target-coordinate generators, and the shifted-block form.
(2) Lemma 3.4(c): exchange/compensation for K^+ rows in protected shifted blocks.
(3) Exactness versus one-sidedness.  Near-exactness cannot remove wrong-sided resonances of size in (delta_Z, C b] (F-NE).  A new tool is
    needed, for example:
    - a face-wise Hoffman bound insensitive to tiny minors not met by the data;
    - a preparation that does not move values at target coordinates.
(4) Exclusion of persistence: (D-abs) (pending the (W4'') check) plus the base-part thinness of 4.3(a).
(5) H1's (R0) residual and the once-refereed links of the chain.
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.

## 6. Required edits to H2
- Bottom line (6) and 5.4: withdraw "the pinned residual would disappear in unshifted blocks and shifted blocks without near-threshold actives"
  and the "inward-locked core".  Replace with F-NE's corrected statement.
- Corollary 4.2: replace with the full-row-rank criterion.  The original holds for a single tiny minor.
- Proposition 4.1 and bottom line (1): "EXACTLY" should become "in the restricted single-block model (P-41)".
- Theorem H2.A: insert G-CPL (coupled rescaling, R-PK bound on phi_y(s)).
- Lemma 2.4: define pullability with x''_max and pre-place a subset of pulls.
- Lemma 2.5: restrict sort (4) to the certified toolbox and correct the cushion bound.
- Lemma 2.6: replace the Step-B ownership citation by tiny signature room.
- Proposition 3.1(b): add the theta_0 term (Design^2 constants).
- Theorems H2.B / H: "every clean sub-window and class", and the memory items only along consecutive (R1) stages.
