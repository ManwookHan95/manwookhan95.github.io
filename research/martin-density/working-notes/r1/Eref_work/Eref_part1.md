# E referee — part 1: reading log and first observations

Read in full: BRIEFING.md, BRIEFING_R2.md, Preprint A, Preprint B, G_notes 3.8-3.10 and 6.6, E_notes (all 771 lines),
A_notes §1, §2, §3, §4 (Defs 4.1, Lemmas 4.2-4.7, Prop 4.8, Thm 4.10, Cor 4.11-4.12, Thm 4.13, §4.5), §6 (Thm 6.2,
Lemma 6.3/6.4, Thm 6.5, Thm 6.8, Cor 6.9, Cor 6.10), A_referee §0-§3.

## Observations so far
O1. E's Theorem 5.1 (Averaging Criterion) is a re-derivation of A_notes Theorem 6.8 (averaging/ladder), which the A-referee
    verified (correct). Differences: E uses radius >= s (c_0 = 1), H <= 1 exactly (A allows 1 + eta(t)), J dyadic scales,
    and a slightly different constant bookkeeping. Need to check E's constants independently.
O2. E's Cor 5.2 is A_notes Cor 6.10(c) with the hypothesis H(c_t) <= 1 + o(1) made explicit as c^2 q*(v)^2/(m^2 C_m) <= 1.
    Need to check: (i) H formula for a single coordinate (P-perp projection: H = (Phi^2 omega^2 - d^2)/C <= Phi^2 omega^2 / C);
    (ii) the claim lambda_i < 2 c q*(v) s/(gamma theta_0); (iii) the radius bound uses 1/(2|d_s|) and C/(2|d_s|M) — fine;
    (iv) whether "g in C(f)" is a real hypothesis (it is assumed). Also whether H(c_s) <= 1 is EXACT (Thm 5.1 requires
    H <= 1, not 1 + o(1)).
O3. E's "A_notes 7.4 box tails" = A_notes Cor 6.10(a), which has the G1 gap (radius). E's SKETCH must use coordinatewise radius.
O4. Need A_notes §7 (Lemma 7.1, 7.2, Cor 7.3, Prop 7.4) for E's part 2.2 rigidity claim and N-c.
O5. Need G_referee 4.7 for (F1).
