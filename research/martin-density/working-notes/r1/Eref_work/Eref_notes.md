# E referee — assembled notes (concise; full report in ctx/r1/E_referee.md)

Parts: Eref_part1 (reading log), part2 (N1, Thm 5.1, Cor 5.2, box tails), part3 (skeleton, rigidity, critical cross,
T1 first pass), part4 (bands, NC, T4, Lemmas 6.1-6.4, Prop 8.2, Gordan), part5 (one-sided structure, T1 d-mismatch,
T4 head shift, multi-block remark), part6 (numerics, verdict list), part7 (referee repair of T1 for Delta d >= 0;
T4 cost CORRECTED: both switched regimes pay).

Verdicts:
* N1 correct.
* Thm 5.1 correct; it duplicates A Thm 6.8 and needs H <= 1 exactly.
* Cor 5.2 correct; it duplicates A Cor 6.10(c). For g_0 != 0 the hypothesis should be
  H_m(omega_0) + c^2 q*(v)^2/(m^2 C_m) < 1.
* Box tails: correct with fixable gaps.
  * The index truncation as worded fails.
  * Needs the coordinatewise radius and A Thm 6.8.
* Skeleton correct.
* Rigidity correct; it covers linear decompositions only.
* Critical cross candidate: correct with fixable gaps.
  * The vectors are in c_00, contradicting Y ∩ c_00 = {0}.
  * It lies in cl Cert(f).
* T1 unclear.
  * The d-mismatch Delta d L*(w''-w) ~ |Delta d| eta is not addressed.
  * Covered for Delta d = 0 (A-ref 5.4) and Delta d >= 0 (referee block-absorption).
  * Delta d < 0 is OPEN.
* Conversion bands correct; the cost carries a log factor.
* NC: correct with fixable gaps.
  * Y-tails are needed.
  * The design constraint contradicts density.
* T4: correct with fixable gaps.
  * a-multiple missing.
  * The head-contact shift gives a first-order kink cost of relative size c_gamma eps_0 in both regimes.
  * Repair by averaging heads.
* L6.1/C6.2 correct; room factor in (b).
* L6.3, L6.4, P8.2 correct.
* Gordan: correct for finite families only; use the closed-hull / uniform-margin version.

Most valuable idea: the destruction-conversion duality (free tail mass) combined with Prop 8.2 and averaging. Together
they reduce the one-sided-block part of the problem to quantitative tail independence of T, which also governs the
open Delta d < 0 case of T1.
Density: OPEN.
