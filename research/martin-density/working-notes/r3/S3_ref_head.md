# S3 referee notes (assembled): verification of S3 with full proofs of all fixes

Setting: canonical base q, Martin's norm with FINITE block set I (p_N; Preprint B Remark martin-tail), admissible T (Lemma B's conclusion only).
Object refereed: ctx/r3/S3_notes.md (identical to S3_head + S3_part1..4 + S3_tail). Report with verdict table: ctx/r3/S3_referee.md.
Referee scripts: ctx/r3/S3ref_work/ (thmB_check.py, thmB_small.py: independent SOCP test of Theorem B; rplus_indep.py: Lemma R+).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## Summary of results
 * CORRECT (re-derived): Lemma 1.1 and Lemmas 1.2-1.3; Theorem A; Theorem B (Fenchel duality, any contact set K); Corollary B2 (f in R at P1's
   example); Lemma R+; Theorem D (first-order rebalancing, no steering); Corollary D1 (Delta d >= 0 two-piece mates, F finite, no further hypothesis).
 * CORRECT WITH FIXABLE GAPS: Corollary D2 and Prop 4.2 (circular |C' - C| = O(s_1) estimate, repaired by Lemma F1; common sequence of scales F2);
   4.5 (needs a regularity hypothesis on Phi, Proposition F3 shows Lemma B does not give it; result already in A_notes 7.4).
 * OVERSTATED: 4.3's "rho-defect only" (needs K^scr < infinity; Remark F4); 4.4's "simplified approximants do not recover" (only a sufficient
   condition fails: HEURISTIC/OPEN); open-core list omits F infinite (a not in c_00).
 * NUMERICS: finite analogue of Theorem B confirmed by an independent solver for certificate and NON-certificate directions on both sides;
   onset-scale phenomenon documented (gamma^+- is reached only below min gap/|omega| of the optimal decomposition).
 * Most valuable idea: first-order rebalancing (linear first-order mismatches are pure level shifts, removable at cost mismatch x inefficiency,
   inefficiency fixed before the mismatch scale) — with Theorem B's duality it reduces F-finite recovery to existence of two-piece data and the
   Delta d < 0 scrambling quantity.
 * Density of NA((c_0,p), l_2^2): still OPEN; nothing points to a counterexample.

