# Referee report on H1 (Round 13): empty (R0) -- first-order Puiseux margin, target freedom as a lever, alignment and unit calculus

Refereed: r13/H1_notes.md (with H1_part1..4.md and H1_work/; scripts inspected, outputs consistent with the notes).  Checked against: r12/J1_notes,
J1_ref_notes (R-PK, R-PB, F-2, P-TU, J1.15'), J2_referee/J2 (FC); r11/K2_notes 4.1(d), 5.1-5.4 (K2.8, K2.9, K2.16, K2.17); r9/X1_notes 1.1, 2.1-2.6 and
X1_ref_notes 3.4, D1-D3, 5-8 (NLM, GEN, QC, KN^tr, KN-1); r11/cert0 3.4; Q1-refb F5 (P-HOLD).  Proofs of all verdicts and fixes, and of three
referee additions: r13/H1_ref_notes.md (part files H1_ref_part1-3.md).  Scripts and outputs: r13/H1_ref_work/.  Role: adversarial referee.

## 0. Bottom line
H1's positive results are correct.  I found no wrong conclusion among the PROVED claims; there are fixable precisions, one false (but
harmless, overly pessimistic) remark, and one overclaimed "characterization".
 - Proposition J1.11 is now PROVED.  The stratified projected flow (Lemma 2.2) needs only Whitney (a) and the frontier condition: the flow of
   P_{T_x S'} v drops through finitely many strata with velocity within eps|v| of v.  Genericity is applied to the k-definable failure set
   B^lin ⊂ B^reg (dim < |N_T|), so GEN applies.  Consequently (R-T) is EMPTY (Corollary 2.4) and X1's exact KN-1 holds can be relaxed.
 - Lemma TF' (target freedom as a lever), Lemma AL (the needed direction of a thick-type row is fixed by the f-datum rho_l u_l(zhat), the same
   for all near-certificates), Lemma NP (in an unshifted block either a peak resource kills zeta_m, or every peak is thick-type and zeta_m has the
   robust sign sgn(rho_c vs_c)), Theorem RL, Lemma KC, Theorems IN, OUT, GS, Lemma DS, Theorem UC, Lemma TG and Proposition MA are correct
   modulo the chain.  I re-derived each and confirmed Lemma NP's sign and Theorem RL's lever numerically in a new toy with a thick-type
   peak and no peak resource (26/26 runs; H1's own toys did not exercise this case).
 - Strengthenings (proved here): Lemma PC (pieces G ∩ m of ANY pinned group in an unshifted block are exactly scalable; H1's "internal"
   hypothesis and Remark 4.3's "linking groups are not scalable" are unnecessary/false); P-KC (Lemma KC needs only ONE movable compensating
   row); Proposition MA' (the per-block frozen value, thick-type PEAKS included, vanishes at every stage carrying a near-certificate in EVERY
   unshifted block); Lemma SLP (all of H1's levers are feasible points of one status-constrained LP whose dual is an explicit R^2-proportional
   anti-aligned resonance; it yields the exact form of the residual (H-3)-(H-5)).
 - (LSC-trunc)_N for every f, and density of NA((c_0, p_N), l_2^2) and NA((c_0, p), l_2^2), remain OPEN, as H1 states.  No counterexample is
   claimed, and nothing found here suggests one.

## 1. Verdicts
| Claim (H1 label) | Verdict | Main point |
|---|---|---|
| Lemma 2.2 stratified projected flow (PROVED) | correct | re-derived; Whitney (a) + frontier condition suffice; no reach bound |
| Proposition J1.11 (PROVED) | correct | regular contact points, uniform linear decrease, B^lin k-definable ⊂ B^reg; PJ-1: option (b) carrier-1 exception |
| Corollary 2.4, (R-T) empty (PROVED mod chain) | correct | (J-e) re-derived; remark (c) "no other use of KN-1 exactness" is an inspection claim (consistent with X1-ref 8, Q1-refb F5) |
| Lemma TF' (PROVED mod chain) | correct | P-TF: displacement sizes up to Design^C u^{-4}(||b|| + x); x_TU must absorb them (harmless); the first form TF's size argument is inverted -- keep TF' |
| Lemma NP (PROVED mod chain) | correct | private near coordinates of a (U)-block peak are TS or peak resources; one peak derivative 1 - X_m (route V: kappa = sum_P |zeta|); numerics N1, N2 |
| Theorem RL (PROVED mod chain) | correct | whole-block rescaling is Z-safe; (RL+) = unprotected; numerics N1 |
| Lemma KC (PROVED mod chain) | correct, strengthened | P-KC: D2 rows need not be in N_0; one movable compensator suffices |
| Lemma AL (PROVED mod chain) | correct | missing eps_l on an error term; main term dominates since u(w) decays only logarithmically |
| Theorem IN (PROVED mod chain) | correct with fixable gap | P-IN: nearly-neutral displacement must be ~2 beta_*; P-KN: (KN)-block clauses mod J1's (KN) SKETCH |
| Theorem OUT (PROVED mod chain) | correct | exchange is exactly R^2-neutral at first order; sizes u^{-2} (P-TF) |
| Theorem GS (PROVED mod chain) | correct, strengthened | P-PC (Lemma PC) |
| Proposition MA (PROVED mod chain) | correct | P-MA bookkeeping (thick-type kind-(iv) rows count as thick); generalized by MA' |
| Lemma DS, Theorem UC, Lemma TG (PROVED mod chain) | correct, strengthened | pieces of non-internal groups; TG also for minors-only pieces |
| Remark 4.3 last sentence; (H-6) "groups linking a (U)-block to a shifted block" | FALSE as stated (harmless) | their (U)-block pieces are scalable (Lemma PC) |
| Peak conversion (SKETCH) | label honest | further gaps: non-robust frozen peak outside (FC); J2.1(e) margins; peak-error bound |
| Residual (H-1)-(H-7) (PROVED as necessary condition) | correct after corrections | exact LP form (H-3')-(H-6') in H1_ref_notes E |
| 4.7 "(T)-block reading" (PROVED characterization) | overclaim | HEURISTIC: one certificate, smooth points, non-uniform delta(eps, r) |
| Persistence (PROVED, elementary) | correct | conditional on stabilization; proves nothing about persistence |
| (LSC-trunc)_N every f; density for p_N, p (OPEN) | OPEN | -- |

## 2. Main findings
F1 (J1.11 is proved).  Lemma 2.2's flow argument is sound: the projected field has norm <= |v| everywhere, so the curve stays in the ball
where Whitney (a) controls every nearby stratum; exits go to strata of strictly smaller dimension; the stratum of r_* itself cannot be exited.
The genericity step correctly avoids defining the stratification over k.  (R-T) is empty at every main stage L >= l_f.
F2 (alignment calculus is sound).  Lemma AL's sign is uniform over near-certificates because kappa_y <= -c_*/nu_1 for all of them; Lemma TF'
correctly handles the target dependence of the generator columns (affine in rt, Lipschitz constant Design^C) and the near-certificate size
budget.  Theorems IN, OUT, GS, RL, UC are correct applications.
F3 (Lemma NP checked at its weakest point).  "No peak resource => every peak is thick-type" follows from K2 4.1(d) and the vanishing of
class data on (U)-block peaks (S_th coordinates of such peaks are zero-data, hence ZD).  The peak derivative is common to all peaks because
in route V kappa_m = sum_P |zeta(c)| + S_m/theta_m and the threshold equation involves the peaks only through sum_P |zeta(c)| and Phi_P^2.
F4 (precisions).  P-TF, P-IN, P-KN, P-MA, PJ-1, wording on (R-np) (a no-peak-resource class), C.7 (4.7 downgraded to HEURISTIC).
F5 (strengthenings, proved in H1_ref_notes D).  Lemma PC; P-KC; Proposition MA' (no-peak-resource blocks: near-certificates sit on the
resonance sum_{thick-type k of m, rows and peaks} rho_k u_k(zhat) = 0 -- confirmed numerically, N3); Lemma SLP (LP primal = H1's levers,
dual = (*) Xi_E = -(lambda_E + 2 kappa'_m Lambda R_E^2) + err).  With MA/MA', (*) gives: blocks with a peak resource -- every object balanced;
blocks without -- Theorem RL and the exact (H-4') resonance with Lambda ~ sum_P rho_c u_c/(1 + 2 kappa'_m R^2) > 0; shifted blocks -- H1's
proportional resonance plus conditions on near-threshold movable rows.

## 3. Attacks attempted
- Semialgebraic uniformity: delta in Lemma 2.2 depends on (r_*, eps); J1.11 needs uniformity only on the compact Lambda (finite cover).  The
  constants c_kappa, h_kappa are design numbers of level L (computed after the level's weights, before b(w), c_{L+1}); P-CHOICE covers them.
- Puiseux margin under the levers: inward moves, down-scalings and R^2-neutral exchanges never raise a protected status at first order;
  nearly-neutral displacements change (T)-block statuses by (J-e)'s quantity (Cor 2.4); LP levers have second-order slack (h^2 << eta'/Design).
- Exactness on Z_kappa: only movable rows, (U)-block pieces (Lemma PC) and exact tangent directions of linear zero sets are moved; nothing
  in a shifted block is scaled.
- (FC) consistency: no robust non-peak reaches the threshold, no near-threshold row moves outward, frozen peaks are robust.
- Cushion domination, (VT), closeness K t: levers create no support; data are projected at the realized ratios with the same Hoffman bound;
  violations <= Design^C u^{-C} x/t << K t.
- Cost and window bookkeeping: W(rt') <= Design^C u^{-C} x, cost o(u^2 T^2); x_TU enlarged by an absolute power (P-TF).
- Lowering/pull admissibility at the companion: unchanged (no new pulls).
- N-independence, well-foundedness: no design change.
- Signs: re-derived; numerics N1 (sign of zeta), N3 (cancellation), H1's align/complement toys re-read.
- Quantifier order: design -> N -> f, g, rho -> L, w, class -> (P) -> targets -> near-certificate set -> lever -> Brouwer -> data at r^#.
- Coverage: not every stage is covered; the residual (H-1)-(H-7) is a correct necessary condition (after P-PC, P-KC; exact form via SLP).
- Counterexample: none; the residual consists of codimension >= 1 coincidences of f's stage data.

## 4. Numerics (sanity only; r13/H1_ref_work/)
- np_rl_toy2.py / np_rl_toy3.py (.out): thick-type peak without peak resource, tuned to resonance.  sgn zeta(y; rc) = sgn(rho_c vs_c) 26/26;
  whole-block rescaling in direction sigma_m: min move 1e-2..5e-1 -> 7e-4 (26/26); opposite direction: no relief (26/26).
- peakderiv.py: d kappa/d|zeta(c)| common to all peaks to 1e-7 over 397 random blocks.
- ma_peak_check.py (.out): near-certificate at the root of the extended frozen value rows + peak (<= 4e-4) while the rows-only value is
  +-0.5..0.7 (10/10).
- slp_check.py: LP duality of Lemma SLP to 9e-16; exact resonance gives V_LP = 0.

## 5. Single most valuable idea
H1's alignment calculus: by J1.6(a), every near-certificate pairs with a target displacement of a thick-type row through the f-datum
rho_l u_l(zhat), with one sign for all certificates (Lemma AL).  Together with Lemma TF' this converts target freedom into levers whose
admissibility is pure status bookkeeping.  The referee's Lemma SLP shows these levers are exactly the feasible points of one
status-constrained LP.  Its Gordan dual (*) is the precise residual: an R^2-proportional anti-aligned resonance.  With MA' it holds in
every unshifted block, peaks included.

## 6. What remains open (precise)
(1) Whether the refined residual (H-3')-(H-6') with (H-7) can hold at all large main stages for some f:
    balanced pieces; R^2-proportional anti-aligned resonances with a positive multiplier tied to sum_P rho_c u_c; vanishing extended frozen
    values; nonlinear pinned groups or thick-type peaks in shifted blocks.
(2) Objects containing non-thick kind-(iv) rows (certificate-dependent coefficients): a minimax version of Lemma SLP.
(3) Pinned groups with nonlinear tiny polynomials ((X4^0)-minors, cofactor polynomials) and thick-type peaks of shifted blocks.
(4) Peak conversion of anti-aligned near-threshold rows (SKETCH, with the gaps of C.6).
(5) The (KN)-block lever bookkeeping (inherited SKETCH, P-KN).
(6) (R1) (task H2).
(7) The once-refereed links of the chain, J1.13's inspection, J2/(FC).
(LSC-trunc)_N for every f: OPEN.  Density of NA((c_0, p_N), l_2^2) for any N: OPEN.  Density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.
Required edits to the record:
- H1 Remark 4.3 and (H-6): (U)-block pieces of linking groups are scalable (Lemma PC).
- (H-3): read "every piece".
- Lemma KC: N_0 = {d_0}, d_0 any movable row (P-KC).
- Theorem IN, nearly-neutral clause: displacement 2 beta_* + 32 nu_1 x/(c_* u) (P-IN).
- TF': size bound Design^C u^{-C'}, x_TU := Design^{C_A + C_J + C_H} u^{-C_H} x (P-TF).
- Table row 16 / 4.7: HEURISTIC.
- J1.11: state option (a) (or patterns without carrier 1 in N_T).
- (KN)-block clauses: "mod J1's (KN) SKETCH".
