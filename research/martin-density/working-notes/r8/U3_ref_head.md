# U3 referee notes (Round 8): verification of U3 and proofs of the fixes

Refereed: r8/U3_notes.md (= U3_head + U3_part1..5, byte-identical, checked with diff) and r8/U3_work/*.py, against
paper/martin_density_note.tex (Sections 1, 7, 8) and the refereed Round-5/6/7 results (V1, V2, V3, V4 and their referee notes).
This file = U3_ref_head + U3_ref_part1..5 (part 1: U3 Part 1; part 2: U3 Part 2; part 3: U3 Part 3; part 4: U3 Part 4 and numerics;
part 5: proofs of the fixes F1-F7).  Scripts: r8/U3_ref_work/ (nl_check2.py and vt_check.py re-run; vt_ref_check.py and
junction_check.py new).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting: p = p_N, N finite (mostly N = 1), F finite.

## Summary of the verification
 * CORRECT as PROVED: Lemma S, Corollaries S1, S2, Proposition S3, Theorem NL (lsc of the fibre map fails at f_SA along (BT) rows),
   Lemma D', Proposition FZ (any admissible T), Corollary FZ (for the stated aligned class), Lemma A (statement precision P2.2),
   Theorem NT properties (b)-(e) incl. rho^sh = 0 and c_pi = 0, Proposition NT-M (i), (iii), (iv), Lemma 3.5 (after the sign precision
   F3), Lemma QB2 as an inequality (accounting precisions F4), Lemma VT (single stage; confirmed numerically), Proposition RT*(a),(b),(d),
   (f) (bookkeeping F7), (S1) for one shifted block with a free-ray q < 0 carrier, Lemma R-pin.
 * SKETCH, correctly labelled but with defects: Theorem NT existence — the written induction is INCONSISTENT (the stage region is empty),
   repaired in F1; Section 3.4 (all mates of f^infty) — plausible, but what remains is not (S2) (P3.4); RT*(c), (e); (S2b).
 * Wrong or overstated: Proposition NT-M(ii) for general Omega/Dom (fails when a special omega-carrier has a wrongly signed off-F target
   coordinate and eps Dom is large; correct for Omega = {k_-} and under the design addition (Z0+), F2); Corollary NT-R's genericity
   sentence for (H2) (F2); Corollary FZ Consequence (a) for general (C*) rows (P2.1); the "(PROVED arithmetic)" scaling check of (S2a):
   K_sharp is NOT O(1) — the window masses create a first-order theta/+- junction mismatch of order s_1/t^2 (F6; numerically exact
   scaling, junction_check.py), which for super-fast ladders cannot be rebalanced with the available transfer peaks (HEURISTIC); repair by
   d-consistent engineered approximants (SKETCH).
 * Not an obstruction after all: U3's "OPEN sub-case" of (S2d) (free in-window violations with b^+ b^- > 0): the symmetric split gives (H3)
   at an l_1 cost <= the violation mass (F5).
 * No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN for every admissible T.
