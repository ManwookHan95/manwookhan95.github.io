# Referee report on J1 (Round 12): removing the Step-A sign-class obstruction (A*)/(U*)

Refereed: r12/J1_notes.md (with J1_part1..5.md, J1_scratch0.md, J1_work/).  Checked against: K2_notes 1-2, 4-5 and K2_ref_notes (K-1...K-8, G);
K1_notes 2.0-2.7 and K1_ref_notes (R-6, R-13, R-14); X1_notes 1-2.6 (Lemma K, Lemma EC, 2.1-2.6); cert0_report 3.1-3.5; the note's def:SLD /
thm:SLD; J2_notes 2.2, 7 (interface only; J2 is refereed separately).  Proofs of every verdict and fix: r12/J1_ref_notes.md (part files
J1_ref_part1-4.md).  Scripts and outputs: r12/J1_ref_work/.  Role: adversarial referee.

## 0. Bottom line
J1's positive core is correct after fixable repairs.  Its main structural insight survives: every near-certificate carries the same robust
coefficient of fixed sign, coef_k ~ kappa_y a_p/v_k(p), on EVERY thick-type carrier (J1.6(a), re-derived).  So relieving one thick-type carrier
removes all Step-A obstructions at once: a helpful far placement (J1.7) or a band on its row (J1.9).  J1.7 settles the point K2.11 left open:
the placement lowers phi_y for all near-certificates simultaneously, overshoot included.
Problems found:
 F-1 (Corollary J1.5; stated conclusion FALSE).  The inequality is right.  The conclusion "no companion keeping the one-sided signs realizes
     the targets; larger moves, degree arguments, two-sided levers cannot do it" does not follow, for three reasons.  The error terms
     (eta_K ~ eps Design with eps up to 4u^3 Design^{-C_A} >> |phi_y|; residual actions on two-sided coordinates) dominate phi_y.  The
     J1.4 bound contains the Deep term, which is exactly the action of a far placement.  And J1's own Theorem J1.7 realizes the same targets
     with all one-sided signs kept.  Numerically, in a genuinely obstructed toy, the minimal move drops from 31-175 to 2.8e-3 after one far
     pull.  The meta-claim in J1 0(1) must be withdrawn.  What J1.4/J1.5 do give is a localization: a realization needs E-action at least
     phi_y.
 F-2 (Lemma J1.14 / Theorem J1.15; non-circularity GAP, fixed).  The coupling rescales only the ACTIVE targets.  The private peak resource,
     however, bounds the FULL block sum zeta_m(y; rt) over all rows.  When the banded carrier is a robust hold, the active partial sum is
     about -y_k rt_k, which is robust.  The coupling term then competes with the band's gain, with ratio 2 rho_k^2 Phi_k^2/(K(a - K R^2)) by
     Lemma K; this ratio reaches 14 for admissible data (N4).  FIX: rescale ALL targets of the block uniformly.  This is legitimate: by
     Lemma K every status decreases, inactive values matter only through statuses, and the minors are homogeneous.  After the fix the
     coupling term is <= 3 kappa_m (1 - s) eps Design.
 P-TU (inherited by K2.9(c) and K1.6(A), amplified in J1.7; fixed).  A pre-placed TU lever is two-sided only within its pull's shift D_p,
     which can be ~x/2 because R-6 places pulls at the smallest pullable depth.  The Brouwer radii W, and W' >> x'_max in J1.7, exceed D_p.
     FIX: put the pulls in a window [x_TU, x'_max] and cap the far window FW_k at x'', with x_TU >= 24 Design^{C_A} u^{-3}(|Lambda|^{1/2} x + 3x'').
     This only enlarges the (U)-class, as R-6 did.
 N3 (numerics).  J1's check_band uses a STALE generator matrix: generators at the current ratios, right-hand side at displaced targets.
     With consistent generators, J1's toy is not obstructed at all, because its private peak column breaks the certificate (Lemma R-PK).  In
     a variant without a peak resource the obstruction is genuine (29-175), and the band removes it (1.6e-4).  So J1.9 is confirmed there.
 Precisions: P-1 (J1.2: every generator depends on the targets through zeta_m(y; rt), not only the peak columns; the certificate set moves
     with the targets), P-2, P-D2 (J1.10(b): inactive blocks may contain D2-pushed carriers, which are protected), P-MT (J1.12: the (X4^0)
     coefficients depend on r_k through R_a^2), P-G (gauge (d)'s "in particular" needs Q-orthogonality), P-S (7.4(c) needs (H-pure) and
     (H-pk)), "iff" -> "if" in J1.10(c), (R-np) too large (nearly neutral zero-data rows need no coupling).
New results (PROVED here):
 LEMMA R-PK: a private two-sided peak resource forces |zeta_m(y; rt)| <= (4/3) eps Design.
 LEMMA R-PB (per-block target hyperplane): if a block with a private peak resource contains only thick-type, privately tunable or
     opposite-orientation kind-(iv) carriers, and |S_m| = |sum_{K_0 ∩ m} eps_l rho_l rt_l| > tau_* (tiny), then Step A has no near-certificate.
     Conversely, at every residual stage |Phi_0^{(m)}(zhat_1)| <= kappa_m (tau_* + C Design eta''): the per-block frozen value nearly
     vanishes.  This is a stage-wise form of J1's stable exact case and a per-block, tiny-threshold form of K2.17(f).
 Remark R-W (the A-regularity radius is a window quantity).
 Observation R-G: (R1) forces a to be b(w)-thin on F ∩ (s_max(L), D(L)].
(LSC-trunc)_N for every f, and density of NA((c_0, p_N), l_2^2) and NA((c_0, p), l_2^2), remain OPEN, as J1 states.  No counterexample is
claimed, and none is suggested.

## 1. Verdicts
| Claim (J1 label) | Verdict | Main point |
|---|---|---|
| Lemma J1.1 (PROVED) | correct | re-derived; rerun 1.67e-14 |
| Lemma J1.2 (PROVED) | correct with fixable gap | identities fine; "only through peak columns" false: dependence via zeta_m(y; rt) in all columns (P-1) |
| Lemma J1.3 (PROVED) | correct | Theta z <= eps Design/|kappa| (sharper); fine part on S_0 (P-2) |
| Lemma J1.4 (PROVED) | correct | Cauchy-Schwarz; error terms not small in general |
| Corollary J1.5 (PROVED) | wrong (conclusion) | inequality correct; "no companion / larger moves cannot" false: J1.7, N2 (F-1) |
| Lemma J1.6 (PROVED) | correct | (a) holds for every near-certificate, peaks included; (b) signs/admissibility re-derived |
| Theorem J1.7 (PROVED mod chain) | correct with fixable gap | P-TU windows; argument otherwise sound |
| Lemma J1.8 (PROVED) | correct | separation + Brouwer with Box |
| Theorem J1.9 (PROVED) | correct | J1's numerics used stale generators (N3); confirmed in a consistent variant |
| Proposition J1.10 (PROVED; KN SKETCH) | correct with fixable gaps | P-D2; (c) "iff" -> "if" |
| Proposition J1.11 (SKETCH) | unclear (unproved) | exponent >= 1 by Lipschitz; uniformity lemma missing; label honest |
| Proposition J1.12 (PROVED, conditional) | correct with fixable gap | P-MT |
| Lemma J1.13 (PROVED, inspection) | correct with fixable gap | uses re-checked; add shifted-block inactive switching Delta'' w (harmless) |
| Lemma J1.14 (PROVED; KN SKETCH) | correct with fixable gap | F-2: rescale ALL targets of the block |
| Theorem J1.15 (PROVED mod chain) | correct with fixable gaps | after F-2, P-TU, P-D2; mod J1.13, J2, chain |
| Gauge 7.3 (PROVED / use SKETCH) | correct with fixable gap | P-G |
| Target freedom 7.4(a),(b) (PROVED) | correct | restatement; the cone depends on the targets |
| Stable exact case 7.4(c) (PROVED) | correct with fixable gap | P-S; stage-wise version via R-PB |

## 2. Main findings
F-1, F-2, P-TU and N3 as in 0 (proofs: J1_ref_notes C).  The positive chain J1.6(a) -> J1.7 / J1.9 -> J1.15 is sound once F-2 and P-TU are inserted.
R-PB adds a checkable sufficient condition and a new necessary condition on residual stages (J1_ref_notes D).

## 3. Attacks attempted
- Target point and bypass: (U)-block statuses are restored by s_m (with F-2), Z_kappa is preserved (homogeneity), and pinned ratios are
  realized exactly.  The Puiseux margin is untouched outside (J-e).
- Exactness on Z_kappa: tiny minors involve pinned ratios only.
- Cushion domination C_+: placements are V1 pulls or aligned support, and bands create no support.
- Closeness K t: data are projected at r^# with the same Hoffman bound.
- Cost: placement C Design x'' log(1/T); Step-A moves <= x_TU/24.
- Uniformity along main stages: every threshold is a stage quantity.
- N-independence and well-foundedness: no design change.  P-TU's windows are window quantities.
- Signs and one-sidedness: re-derived for placements (both cases) and raises.
- Quantifier order: design -> f, g, rho -> L, w, class -> (P) -> targets -> windows and pre-placements -> bands/coupling -> Brouwer ->
  data at r^#.
- Coverage of rows: not every row is covered; the residual is (R0) with the R-PB condition, or (R1).
- Joint continuity of the coupled selection, and the fixed point for beta_* (C_2 W^2 depends on beta_*): checked.
- (FC)/K-8 at the intermediate row of J1.7: harmless.
Results: F-1, F-2, P-TU, N3 and the precisions.  Counterexample: none.

## 4. Numerics (sanity only; r12/J1_ref_work/)
- rerun/: J1's scripts reproduced exactly.
- ref_band_consistent (N3): stale versus consistent generators.  Variant A has a peak resource: consistent minimal move 2e-2..1e-1 without
  any band.  Variant B has none: 29-175 without a band, 1.6e-4 with one.
- ref_j15_placement (N2): in variant B, one far pull with all S_th signs kept moves the minimal move from 31-175 to 2.8e-3.  The change of
  the frozen functional equals the Deep term to all digits shown.
- ref_noncirc (N4): F-2's ratio ranges over 0.01-14.3.

## 5. Single most valuable idea
J1's one-out-of-many principle.  Every near-certificate has the same fixed-sign robust coefficient kappa_y a_p/v_k(p) on every thick-type
carrier.  So one relieved thick-type carrier (far placement, or a band with uniform block rescaling) kills every Step-A obstruction
simultaneously.  The referee's Lemma R-PB complements it: a private peak resource pins zeta_m(y; rt) ~ 0, and therefore residual stages force
the per-block frozen values Phi_0^{(m)}(zhat_1) to nearly vanish.  This is the stable-exact structure, stage by stage.

## 6. What remains open (precise)
(1) The residual at all large main stages:
    (R0) every thick-type carrier is rigid (frozen far window on FW_k; no private two-sided resource; tiny spreads), each carrier being of
         type (R-pin), (R-T), (R-Ts), (R-KN), (R-D2), (R-np) for robust status only, or (R-pk); in addition |S_m| <= tau_* in every block
         satisfying R-PB (i)-(ii); or
    (R1) no thick-type carrier, so a is b(w)-thin beyond the coarse targets, with pure (U*) certificates.
(2) Proposition J1.11 (uniform first-order Puiseux margin); it would empty (R-T).
(3) A constrained Lojasiewicz step for pinned thick-type ratios (R-pin).
(4) The (KN)-lever coupling.
(5) The once-refereed chain links, J2 (in refereeing), and the J1.13 inspection.
(LSC-trunc)_N for every f, density for every p_N, and density for p: OPEN.
