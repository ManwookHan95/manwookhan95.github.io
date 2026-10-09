# Z3 referee notes (Round 5): verification of Z3 ((O1): approximate swallowing, inexact free carriers), fixes, and new results

Reference: paper/martin_density_note.tex (numbering, notation). I = {1..N} finite, p = p_N (Lemma lem:martintail transfers density for
infinitely many N to Martin's p). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Report: Z3_referee.md. Scripts: Z3_ref_work/.
Parts: Z3_ref_part1.md (Z3 parts 1-2), Z3_ref_part2.md (Z3 parts 3-4), Z3_ref_part3.md (Z3 parts 5-6), Z3_ref_part4.md (new).

## Summary of results
A. Verified as correct (re-derived line by line): Lemma 1.1, Lemma 1.2, Corollary 1.3, Lemma 1.4 (with the constant 1/Re(u)),
   Remark 1.5(a),(b) (as statements about upper bounds), Lemma U, THEOREM E, Lemma 3.1 (upper bound; adversarial numerics), Lemma 5.1
   and its multi-coordinate extension (numerics), Identity 5.2, THEOREM 5.3, THEOREM 5.4, 5.5(i), Corollary 6.2 (tautological part).
B. Correct after fixes (fixes PROVED here): Lemma 3.2 (flipped set = all j with z_j eps_l < 0); Proposition T (T2: eps_l the minimizing
   sign and r*_l := ||v_l 1_{S_l\F}|| for l in A; T3: Gamma bound with an additive O(theta); T4: factor C_0^# for the vanishing rows;
   T5: (BS) is not implied by small rooms — target-induced costs; sufficient design-quantity condition given; T6: inverse margins of
   the bad peak carriers in B' and the conversion constants grow with B' and must enter K, K^#_* := K_* + sum 1/mu + C_0^#); Corollary 3.4;
   Proposition 4.1(b) and Proposition 4.2 (add r*_l > 0 for all good l); 4.3(i) (hypotheses of Proposition T made explicit).
C. FALSE: "every design has band carriers; no choice of design removes the band" (Z3 4.3(ii), 7.1). The example "r_l = 2^{-l^4}delta°_l
   for infinitely many l in one block" is not a band example (sparse sets are pinnable); it is valid for ALL l in L_N under (G1') gaps of
   L_N are O(l^{1/2}) and (G2') delta°_l >= 2^{-l^2}.
D. NEW (PROVED, part 4): for the explosive variant (D1^F) of the SLD design (window factor l 2^{l^3} replaced by a recursively chosen F(l))
   (i) all of Section 8 and of Z3 survive; (ii) the bands of different windows are pairwise disjoint, so every first row with finite base
   support has infinitely many band-free windows; (iii) at such windows the coarse carriers split into pinned and exactifiable ones with
   K_* <= C_f^{l} F^{1/4} Lambda° and exactification cost <= theta T_lo^2, theta -> 0; hence f in Rec under the companion-cone hypotheses
   ((H1)-(H3) for E u B, slaving r*_l >= r_l/2, status stability, Hoffman C_H <= F^{1/2}). So for (D1^F), (O1)(i) reduces to the
   Hoffman/companion-cone problem of growing finite sets of nearly exactly swallowed carriers (same difficulty as Remark rem:S(c), (O2)).
E. NEW (PROVED): top-sub-window form of Corollary 3.4 (exactification threshold theta 4^{-n_j}T_hi^2 with n_j ~ psi (1 + C_H)K_*).
F. SKETCH (unchanged status): Remark 1.5(c), 4.3(iii) (and: only |F| - 1 degrees of freedom for re-tuning e^# with supp a^# = F),
   5.5(ii) (genericity of the tuning shift missing), 6.1 (genericity; push range should be sum v(1 - sigma z)).
G. OPEN: (O1)(i) for the original design (band carriers / lsc along far lowerings); (O1)(i) for (D1^F) modulo the cone conditions
   (in particular d-neutral approximately resonant exactified carriers, Lemma 1.4); (O1)(ii) items of Z3 5.6; (O2)-(O4).
