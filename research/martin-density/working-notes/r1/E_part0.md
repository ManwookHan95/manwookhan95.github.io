# Notes E — Strategy (E): adversarial search for a counterexample to density of NA((c_0,p), l_2^2)

Author: strategy-E agent, 2026-10-08. Setting: canonical base, Martin-type norm p = q + ||L.||_V (finite block set
unless said otherwise; Preprint B Remark martin-tail reduces Martin's norm to the p_N). Files read: BRIEFING.md,
residual_recovery.tex (Preprint A), hmr_c0_renormings.tex (Preprint B), G_notes §3.8-3.10 and §6.6, and the round-1
notes A_notes, D_notes, G_referee (I rely on A_notes §4 certificate machinery, marked as imported).
arXiv (Martin 2406.07273, KLMW 1905.08272) and Martin's homepage were UNREACHABLE (proxy 403 / DNS); I used only the
description of Martin's T in Preprint B (M1)-(M7).
Status labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN / NUMERICAL (= numerical evidence in an explicit cost model).

## Bottom line

No counterexample. Every natural mechanism I could construct either dies (with an identified recovery mechanism) or,
in one case, survives only inside an idealized cost model under a long list of unverified adversarial design conditions.
New rigorous results:
 * Averaging Criterion (Theorem 5.1, PROVED mod A_notes Prop 4.5): if a mate g of f can be approximated at EVERY small
   scale s by a finite certificate of radius >= s with error O(s) (any constant), then g is in cl Cert(f), hence
   recovered along every sequence. Corollary 5.2 (PROVED): "critical-rate" cross mates carried by off-peak (two-sided)
   coordinates are recoverable — the danger zone flagged by A_notes 7.3 / D_notes 12.6 is NOT an obstruction for
   two-sided resources; A_notes 7.4 (box tails of exact order sigma) is settled the same way (SKETCH).
 * Structural lemmas (PROVED): duality lemma and "destroyed implies convertible" (Lemma 6.1, Cor 6.2); impossibility of
   exactly collinear tails (Lemma 6.3); a single far detector can be neutralized (Lemma 6.4, first part); window moves
   must be o(1) along NA approximants (Prop 8.2, from (F1)/Prop 3.9); rigidity of two-sided certificates at NA points
   (part 2.2, from A_notes Prop 7.4).
Recovery mechanisms identified (SKETCH): T1 eta-trick at contacts of f; T2 multi-scale averaging of frozen
certificates; T3 conversion of destroyed resources through their own far tails (destruction-conversion duality);
T4 eta-trick on the frozen error's support + side switching (kills slow cross mates with one-sided near-contact
errors, candidate NC).
Residual loophole (part 7, HEURISTIC/OPEN): one-sided (peak) carriers of a core direction at all scales, error-dominated
costs, and a "rigid" T whose far tails are nearly collinear inside long detector groups. In Model N the boundary excess
is R(J) = 1.194, 1.043, 1.0093, 1.0017 for J = 1..4 converted scales (delta = 1; 1.180, 1.037, 1.006 for J = 1..3 at
delta = 2): positive for every bounded J, tending to 1 as J grows. Whether an approximant
always has unbounded conversion capacity or cheap carriers for frozen errors (part 7.5) is OPEN; I give concrete
counter-strategies (C1)-(C3) that an adversary would have to block, and I could not certify any consistent design.
Leaning: POSITIVE for Martin's own (presumably generic) T; the question might in principle depend on T.

## Status table (all claims)

| # | Claim | Status | Where |
|---|---|---|---|
| 1 | Necessary conditions for a counterexample (f non-NA, not in Omega, g not in cl Cert^sh, scale-dependent decompositions, all approximants of form (F1)) | PROVED (collection) | 1.1 |
| 2 | Critical cross mate with destroyed fine coordinates exists at suitable f (construction) | SKETCH | 1.2 |
| 3 | Single frozen coordinate recovers only up to a boundary factor ~2 | NUMERICAL (Model M) | 1.3 |
| 4 | Multi-frozen geometric averaging removes the boundary excess: R(J) = 2.0, 1.27, 1.08, 1.007, 1.0008, 1.0000 (J = 1,2,3,5,8,12) | NUMERICAL (Model M) | 1.3 |
| 5 | Two-piece mates over infinite contact sets are recovered (eta-trick + truncation) | SKETCH | 1.4(i) |
| 6 | Averaging skeleton: convexity bound p*(f'+t g') <= 1 + Q t^2/2 + kappa |t| sum_{s_j<|t|} w_j s_j | PROVED | 2.1 |
| 7 | Rigidity: one-sided resources cannot form a two-sided linear certificate at an NA point | PROVED (from A_notes 7.4) | 2.2 |
| 8 | One-sided cross mates: conversion bands via the scalar v(x') | SKETCH | 2.4 |
| 9 | Candidate NC (slow cross, near-contact errors) is a mate at f | SKETCH | 3.1 |
| 10 | NC is recovered (T4: eta on frozen error support + side switching) | SKETCH (high confidence) | 3.2 |
| 11 | Model N: one shift R = 2.82 (delta=1); two coincident shifts R = 1.031; best scanned 1.0021 (delta=1), 0.9987 (delta=2, fine scan); group transitions R ~ 1 (a0 = 0.3) | NUMERICAL | 4.2-4.4 |
| 12 | Theorem 5.1 (Averaging Criterion for cl Cert(f)) | PROVED (mod A_notes P4.5, L4.2, L4.7, C4.11) | 5 |
| 13 | Corollary 5.2 (critical two-sided cross mates in cl Cert(f)), case g_0 = 0 | PROVED (same imports) | 5 |
| 14 | A_notes §7.4 borderline box tails are in cl Cert(f) | SKETCH | 5 |
| 15 | Lemma 6.1 (duality), Cor 6.2 (destroyed => convertible, with guards) | PROVED | 6 |
| 16 | Lemma 6.3 (no exact collinearity of tails) | PROVED | 6 |
| 17 | Lemma 6.4 (single detector neutralizable; need for infinitely many groups) | PROVED (first part) / HEURISTIC (consequence) | 6 |
| 18 | Error-dominated Model N (a0 = 0.03): R(J) = 1.194, 1.043, 1.0093, 1.0017 (J = 1..4 converted scales, delta = 1); 1.180, 1.037, 1.006 (J = 1..3, delta = 2); two groups at delta = 1 can convert 3 scales (R = 1.017); excess located a few octaves above the band (frozen-error absorption) | NUMERICAL | 7.4 |
| 19 | Rigid design (A1)-(A5) gives bounded conversion capacity and a model-level obstruction | HEURISTIC / OPEN (consistency unverified; counter-strategies C1-C3 not excluded) | 7.3-7.5 |
| 20 | Gordan equivalence for the sign obstruction (A3) | PROVED (Gordan's alternative) | 7.3 |
| 21 | Prop 8.2: along NA approximants window moves are o(1); only absolute shifts act on fine resources | PROVED (statement) / SKETCH (consequence) | 8 |
| 22 | My earlier claims "deep peaks do not matter" and "individual window conversions are cheap" | FALSE (corrected) | 8.1, 7.2(iv) |
| 23 | Density of NA((c_0,p), l_2^2) | OPEN (leaning positive) | 9 |
