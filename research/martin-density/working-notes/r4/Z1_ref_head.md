# Z1 referee notes (assembled): verification of Z1 (Lemma Z via far lowering and scale decoupling) and the referee's additions

Setting: canonical base q, finite block set I_N (p := p_N, every N; Remark martin-tail, G3_referee sec. 4, transfers to Martin's p);
the SLD operator T of G3 1.2. Notation of G3/Z1. Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Parts: Z1_ref_part1.md (Z1 1.1-1.5), Z1_ref_part2.md (Z1 part 2), Z1_ref_part3.md (Z1 part 3), Z1_ref_part4.md (Z1 part 4),
Z1_ref_part5.md (Z1 part 5 + Theorem M). Scripts: Z1ref_work/scalar_checks.py, Z1ref_work/hm2.py (and hoffman_matching.py, the variant
without an exact resonance). Report: Z1_referee.md.

## Summary of verdicts
| Z1 claim | Verdict | Where |
|---|---|---|
| R_0-approximants exist; Lemma Z is a lower-semicontinuity statement | correct with a fixable overstatement: Lemma Z is PER MATE; the uniform "rho C(f) subset Li C(f'_n) along one sequence" is only sufficient. Far lowerings must also truncate a when F is infinite | 1.1 |
| Exposed face {phi : phi(xi) = 1} = {f} | correct (PROVED) | 1.2 |
| "Hence rho C(f) subset C(f') forces f' = f" | WRONG (non sequitur; only the sufficient condition (*) fails). Exact criterion: f'^2 + rho^2 r~_f^2 <= p^2; it forces only C(f) subset ker xi'. The pattern is false in ell_4^3. New: C_base(a) subset C(f') for every f' with base part a | 1.3 |
| Local reduction (P2A 1.4 for non-NA f') | correct | 1.4 |
| Theorem B* (window-pinned mates, F finite) | correct (traced every use of (SR) and gamma in G3) | 1.5 |
| Ray lemma; budget form; consequences | correct; 2.4(b) "not below" and 2.4(c) "only if" are HEURISTIC, not PROVED | 2.1-2.4 |
| Far lowering of one swallowed set | (a), (b) correct as necessary conditions; (d) is HEURISTIC since it rests on (c) | 3.1 |
| Approximants f^L and reduction (A)+(B) => density | correct for F finite; for F infinite (B) must be stated for all f; the design adjustment is harmless but unnecessary | 3.0, 3.2, 3.3 |
| (O-c): naive window averaging + S3 Thm D fails | arithmetic correct; it is a statement about one estimate chain; it disappears if the mismatch is exactly 0 | 3.4 |
| Flip lemma (infinite F) | correct | 4.1 |
| Theorem B^inf | SKETCH as labelled; plausible; the import is the C referee's two-line remark | 4.2 |
| Bounded free switching | correct | 4.3 |
| Common-functional obstruction (5.2) | WRONG as a conclusion: an artefact of fixing the + component as g - Rem_+. Under Z1's own (E1), (E2) the obstruction is removed by trimming the + contact base by O(K t) and Hoffman-projecting the free switching onto the polyhedral cone of exact d-neutral resonances | 5.2-5.3 |
| (referee) Theorem M: finitely swallowed points with exact free resources are in R | SKETCH (steps 1-4 of the matching PROVED) | 5.4-5.5 |

