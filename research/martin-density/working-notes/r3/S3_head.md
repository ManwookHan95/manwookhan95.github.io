# S3 notes — rebalancing at engineered approximants, the exact one-sided invariant, engineering without steering (O1, O2, O4)

Round 3, task S3. Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; Preprint B Remark martin-tail reduces density for p to
density for all p_N). About T only Lemma B's conclusion is used ("admissible T"). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: ctx/r3/S3_part1.md .. S3_part4.md (assembled below). Scripts: scratchpad/S3_work/ (gamma_side.py, lemma_Rplus.py).
Imports (all refereed in Rounds 1-2): A Facts A-F, A Lemmas 4.2-4.4, 4.7, 7.2, A Thm 4.10, 6.8, Cor 6.10; C Thm 7.1, 7.4 (Steps 1-6), C Lemma 5.1, 5.2, 6.1,
C Prop 8.1 parts (i), (ii), (v) (the parts the C referee re-derived; part (iii), the decoupling, is NOT used); P2A Lemmas 1.1-1.4; N_part1 Thm 1
(g in Ls(f) iff (f, rho g) in cl NA for all rho < 1; density iff Ls(f) = C(f) for all f); P1 2.1-2.2, 6.0-6.1; N2 Lemma 3.1-3.2; N2-referee Lemma R.

## 0. Summary

**O2 (second-order rebalancing at engineered approximants) — solved for two-piece data.**
 * Rebalancing add-on (Lemma 1.1, PROVED): at ANY point (NA or not), transfer peaks (C Thm 7.4) can be attached to ANY decomposition whose block pieces
   stay O(|tau|)-close to w'_m; levels are moved between base and blocks at a relative cost eps_1 fixed in advance.
 * Theorem A (PROVED): P2A Thm 2.1 / N2 Thm 1 (and, Cor A', N2 Thm 2, N2-ref Thm 3*, P2x Thm 3.5) hold with the max-form coefficient kappa_max replaced by the
   mass-weighted kappa_w := max_+- [q_0 h(b^+-) + sum_m sigma_m H_m(omega^+-_m)].
 * Theorem B (PROVED): the EXACT one-sided second-order coefficient. At every f with F finite, all Q_m finite, no degenerate peaks and (MS) — "(BT)",
   with ARBITRARY contact set K —
      lim_{t -> 0+-} 2(p*(f + t g) - 1)/t^2 = gamma^+-(g) := min over side-+- admissible decompositions of q_0 h(b) + sum_m sigma_m H_m(omega_m),
   the minimum being attained. Proof by Fenchel duality (no decoupling needed), which also repairs the C-referee gap in C Prop 8.1 and explains the
   referee's kink phenomenon (Gamma_2 < Gamma_w): numerically gamma^+ = 0.29567, gamma^- = 0.28325 reproduce the referee's exact one-sided coefficients
   (0.29567/0.29568 and 0.28325/0.28324) in his all-kinks model (2.7).
 * Corollary B2 (PROVED): at P1's example EVERY g in C(f) is recovered (f is in R). This answers the task's question and upgrades P2A 2.4 (SKETCH).

**O4 (several active blocks without (S)/(TC)) — solved, and much of the Delta d problem with it.**
 * Theorem D (PROVED): FIRST-ORDER rebalancing removes the need for steering. Engineered approximants with window masses and a far truncation ONLY
   (no far sign-flipped contacts, no tuning mass, no steering coordinates) recover every two-piece mate with rho^2 kappa_w < 1, for ANY number of active
   blocks and ANY d-coefficients, provided the blocks with Delta d_m < 0 satisfy a scrambling condition (SC_m). For Delta d_m >= 0 in all blocks there
   is no hypothesis at all beyond F finite (Corollary D1): this contains P2A Thm 2.1, N2 Thms 1-2, P2x Thm 3.5 and drops (S), (TC), (TT), (BR).
 * Lemma 3.2 ("R+", PROVED, numerically checked to 2.2e-16): the anchor of N2-referee Lemma R can be modified so that the first-order term (C'-C)_+ disappears.
 * Corollary D2 (PROVED): every (BT) point is recoverable (all mates in Ls(f)). This contains C Thm 8.4 (which needed K = empty) and Corollary B2.

**O1 (generic supports) — reduced to one explicit quantity.**
 * Infinitely many strict non-peaks are harmless for two-piece mates with Delta d_m >= 0 (D1), and for Delta d_m < 0 under (MS) + (MS-Q*) along SOME sequence of
   scales (Prop 4.2): Scr_m(s) := lambda-mass (truncated at s) of near-threshold peaks (mu <= s) and of non-peaks with Phi gap <= s or gap <= s must be o(s).
 * Without it, recovery holds for rho below an explicit threshold (4.3): the defect can only be a "rho near 1" phenomenon.
 * (MS-Q*) CAN fail for admissible T (4.4, SKETCH: prescribe a dense family of block vectors in zhat-perp at even indices), and then the simplified
   approximants do not recover Delta d < 0 mates for rho near 1; whether other approximants do is OPEN (a T-independent "compensation property" of U would suffice, HEURISTIC).
 * The deep-coefficient borderline c_k ~ sqrt(Phi_k) of C 9.2 is covered for certificate-type mates by A Cor 6.10(a) (PROVED, refereed); mixed
   deep + switching mates are OPEN.

**Density of NA((c_0,p), l_2^2):** still OPEN. Nothing found points to a counterexample; the open core shrinks to (i) Delta d < 0 switching mates at blocks
violating (MS-Q*), (ii) mates at generic supports that are not limits of two-piece data (scale-dependent, = O3), (iii) mixed deep + switching mates.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Rebalancing add-on lemma (any point, any block pieces O(tau)-close to w') | PROVED | 1.1 |
| 2 | Transfer data with prescribed inefficiency in every block; persistence along converging NA data | PROVED | 1.2, 1.3 |
| 3 | Theorem A: engineered recovery with kappa_w (weighted) instead of kappa_max | PROVED | 1.4 |
| 4 | Cor A': same upgrade for N2 Thm 2, N2-ref Thm 3*, Cor R, P2x Thm 3.5 | PROVED mod. their hypotheses (superseded by D) | 1.5 |
| 5 | Theorem B: exact one-sided coefficient = gamma^+- at (BT) points, any K; minimiser exists | PROVED (+ numerics) | 2.3, 2.7 |
| 6 | Every g in C(f) at a (BT) point has optimal two-piece data with kappa_w <= 1 | PROVED | 2.3(c), 2.4 |
| 7 | P1's example: every mate recovered (f in R) | PROVED | 2.6 |
| 8 | First-order bookkeeping identity c' l_b + sum sigma'_m l_m = g'(x') | PROVED | 3.1 |
| 9 | Lemma R+: anchor without the (C'-C)_+ term | PROVED (+ numerics) | 3.2 |
| 10 | Theorem D: engineering without steering; any blocks; Delta d >= 0 free; Delta d < 0 under (SC) | PROVED | 3.4 |
| 11 | D1: Delta d_m >= 0 two-piece mates recovered with no hypothesis on Q, K, T | PROVED | 3.5 |
| 12 | D2: every (BT) point is in R | PROVED | 3.6 |
| 13 | (MS) + (MS-Q*) along a sequence of scales => (SC) | PROVED | 4.2 |
| 14 | Quantitative recovery without (SC) (rho below explicit threshold) | PROVED | 4.3 |
| 15 | (MS-Q*) can fail for admissible T; simplified approximants then fail for Delta d < 0, rho near 1 | SKETCH | 4.4 |
| 16 | Whether some engineering always handles Delta d < 0 at (MS-Q*)-violating blocks | OPEN | 4.4 |
| 17 | Compensation property of U as a T-independent route | HEURISTIC | 4.4 |
| 18 | Deep coefficients c_k ~ sqrt(Phi_k): certificate-type mates in cl Cert(f) (A Cor 6.10(a)); weighted Gamma_w upgrade | PROVED / SKETCH | 4.5 |
| 19 | Mixed deep + switching mates; mates at generic supports beyond two-piece data | OPEN | 4.5, 4.6 |

Corrections to earlier notes (all PROVED by the results above):
 * C_notes 9.2 "the borderline c_k ~ sqrt(Phi_k) is not covered by any known technique": superseded by A Cor 6.10(a) (certificate-type mates).
 * C Prop 8.1 lower bound: its decoupling gap (C referee 1.20) is bypassed; the correct sharp coefficient at supports with infinitely many kinks is
   gamma^+- (one-sided, minimised over side-admissible decompositions), not Gamma_w of a fixed certificate (Theorem B).
 * N2-referee Lemma R / Theorem 3* / Cor R: the scalar condition (C'-C)_+ = o(t_n) and the tuning Delta d' = Delta d are unnecessary (Lemma R+, first-order rebalancing).
 * P2A Thm 2.1 / N2 Thm 1-3 / P2x Thm 3.5: hypotheses (S), (TC), (TT), (BR), far pulls and exact steering are unnecessary (Theorem D).
 * P1 6.3 Remark and P2A 2.4 ("recovery of all of C(f) at P1's example would follow ... not proved"): PROVED (Cor B2/D2), without shifted transport.
