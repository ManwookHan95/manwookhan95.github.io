# E notes, part 9: conclusions, refined necessary conditions, recommendations

## 9.1 Refined necessary conditions for a counterexample (combining parts 1-8)

A counterexample (f, g, rho) must satisfy, in addition to 1.1:
 (R-a) g is not in cl Cert(f). By Theorem 5.1 this means: there is NO family of finite certificates c_s (H <= 1,
       radius >= s, bounded kappa) with p*(g_{c_s} - g) = O(s). Equivalently (HEURISTIC reading): at a cofinal set of
       small scales the decompositions of f + t g must use ONE-SIDED resources carrying an O(1) share of g:
       block peaks / near-peak coordinates used in their long direction, or one-sided base contacts/near-contacts.
 (R-b) One-sided BASE resources are not enough: T1 (eta-trick) and T4 (eta on frozen error support + side switching)
       recover them (SKETCH). So the one-sided resources must be BLOCK peaks carrying a CORE direction (window
       coordinates with |z| bounded away from 1, where (F1) forbids eta-tricks).
 (R-c) Destroyed peaks are convertible through the far tails that destroy them (Cor 6.2); window moves are o(1)
       (Prop 8.2). So the far tails of the carriers near every possible boundary must be quantitatively RIGID (nearly
       collinear in long groups), otherwise the approximant converts unboundedly many adjacent scales and the averaging
       (T2) closes the boundary (Model M/N: R -> 1).
 (R-d) Costs must be ERROR-dominated (first-order peak cost small compared with the critical core error cost): when
       the peak cost is comparable, conversion removes it and two converted scales already give R <= 1 (Model N, a0=0.3).
 (R-e) Frozen core errors must not be carriable by blocks at the boundary, neither by converted generic coordinates of
       fine groups (C1), nor by one-sided coarse carriers of core directions (C2), nor by combinations (C3).
I could not decide whether (R-a)-(R-e) can hold simultaneously for an admissible T. Each additional requirement made the
adversarial design more delicate; none led to a contradiction I could prove.

## 9.2 What the adversarial search contributes to a positive proof

 * Reduce to one-sided resources: Theorem 5.1 removes all mates that are O(s)-approximable by certificates at f.
 * For one-sided base resources use T1/T4 (eta-tricks with budget = finest matched scale x error mass).
 * For one-sided block resources the needed lemma is QUANTITATIVE TAIL INDEPENDENCE: near any boundary scale an NA
   approximant can convert (make two-sided) the carriers at an unbounded number of adjacent scales at cost o(1);
   or alternatively a FROZEN-ERROR CARRYING lemma: the core errors of finitely many boundary carriers can be carried
   by block coordinates that are two-sided at f' (C1) or one-sided above the boundary on both sides (C2).
   Lemma 6.1/Cor 6.2 (free tail mass) and Lemma 6.3 (no exact collinearity) are the qualitative versions.
 * Use group transitions (two independent scalars) and conversion of BOTH carrier types at the same scales; Model N
   shows these choices matter (one-type bands give R ~ 2.8, coincident two-type bands R ~ 1.03, two groups R ~ 1).

## 9.3 Toy models (as requested)

Model M (two-sided critical cross resources only) and Model N (one-sided resources of both types + conversion bands)
are explicit convex cost models (definitions in 1.3 and 4.1) in which the question "can the truncated structure at an
NA approximant recover rho g for every rho < 1?" is SETTLED NUMERICALLY:
 * Model M: yes, by multi-scale averaging (R(J) -> 1); Theorem 5.1 is the rigorous counterpart at f.
 * Model N with >= 2 adjacent converted scales and comparable peak cost: yes (R <= 1 within 1e-3).
 * Model N error-dominated with a bounded number J of converted scales: no for rho^2 > 1/R(J) (delta = 1: R(2) = 1.043,
   R(3) = 1.0093, R(4) = 1.0017; delta = 2: R(2) = 1.037, R(3) = 1.006); yes if J is unbounded.
The models are proxies; they do not include every approximant strategy of the real norm (part 7.5), and no lower
bound for the real norm is proved. Single-block and "simple u_k" versions of Martin's norm reduce to the same
mechanisms (the analysis above is single-block throughout).

## 9.4 Suggested next steps

 1. Prove the quantitative tail independence / frozen-error carrying lemma for Martin's ACTUAL T (needs the details of
    Martin's Lemma B; arXiv was not reachable from this sandbox).
 2. Try to build an explicit "rigid" T satisfying (M1)-(M7) and (A1)-(A5); if this is impossible (e.g. because density
    of tails forces counter-strategy C1 or C3), the remaining loophole closes and Theorem 5.1 + T1-T4 + conversion give a
    complete heuristic picture of density; the proof would then be a matter of bookkeeping.
 3. Extend Theorem 5.1 to shifted certificates (needs a quantitative radius in A_notes Prop 4.16) and to joint fibres
    C_d(f) (ranges l_2^{d+1}); the averaging argument is convexity-based and should extend verbatim along rays.

## Appendix: numerical scripts (all in ctx/r1/E_work/, numpy only)

 * modelM.py, modelM_opt.py, modelM_opt2.py — Model M (part 1.3).
 * modelN.py (solver; unit-tested against hand computations and brute force, see part 9 log), modelN_run.py,
   modelN_run2.py, modelN_scan.py, modelN_fine.py, modelN_groups.py, modelN_groups_dense.py, modelN_groups_a0.py,
   modelN_phase.py, modelN_diag.py — Model N (parts 4 and 7). Outputs: *.out files in the same directory
   (error-dominated runs: modelN_groups_a0.out (delta = 1), modelN_groups_a0_d2_g{1,2,3}.out (delta = 2),
   modelN_phase.out). Typical run time 5-20 minutes per configuration (Nelder-Mead over the frozen weights, sup over
   ~80 scales).
 * Solver unit tests (run 2026-10-08): off-peak single resource cost 0.48 (expected 0.48); peak inward cost 0.72
   (0.72); wrong side infeasible (inf); exact frozen cancellation 0.08 (0.08); two-resource box case 0.626875
   (brute force 0.626875).
