# Y1 notes (Round 6): one N-free design D_X and a master theorem that removes the rate obstruction (r)

Setting: paper/martin_density_note.tex (Sections 1, 7, 8: notation and numbering), Round-5 reports Z3-Z6 with their referee fixes.
Finite block sets I = {1..N}, p = p_N; D_X is ONE admissible operator for all N (so Lemma lem:martintail applies: Lemma Z for
infinitely many N gives density for Martin's norm built with D_X).  F = supp a finite unless said otherwise.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files: Y1_part0 (reading digest), Y1_part1..4, Y1_part5a, 5b, 5c
(assembled below in the order 1, 2, 3, 4, 5a, 5c, 5b; 5c contains the definition (Rep) used in 5a and the corrected design factor
Q(w) = Design(l)^4 u(w)^{-omega(l)-8}, already inserted in part 1).  Script: Y1_work/threshold_check.py.
Parallel Round-6 work read after the plan was fixed (unrefereed): Y4 (design D^PW and pigeonhole sub-windows: same idea as
Theorem 2 below), Y2 (Lemma T, donors, Theorem E', Theorem P for degenerate peaks: same threshold mechanism as part 4).  Every
statement used here is proved here; overlaps are marked.  No counterexample is claimed; nothing found points to one.

## 0. Summary
(1) DESIGN D_X (part 1, PROVED admissible, N-free, Section 8 and all refereed Round-5 window theorems survive): SLD with an explosive
ladder of SUB-WINDOWS: each level l has M(l) = omega(l) + 1 consecutive sub-windows with pairwise disjoint bands (b(w), u(w)),
omega(l) = 3l + |T(l)| = number of rate objects of level l; the design factor contains Z4's G*(l), Z6's H_comb(l) and D(l) (D''' fixes:
1/Phi, m^nat), a GENERALIZED configuration Hoffman constant G**(l) (arbitrary contact patterns on all coarse targets), 2^{sigma(l)}
(donor coordinates) and |T(l)|; fine weights c_{l+1} <= b(l, M(l))^2.
(2) RATE DICHOTOMY (part 2, PROVED): at EVERY level l some sub-window w is clean: every rate of level l — room of a signature set
outside all coarse targets (R1), target room (R2), threshold distance |rho - 1| (R3, margins and gaps), relative d-coefficient rho (R4) —
is TINY (<= b(w)) or ROBUST (>= u(w)).  Lemma T (threshold equation, independent of Y2) and Lemma T2 (quantitative raising).
(3) PINNING AT f (part 3, PROVED): robust rooms pin DIAGONALLY (no products, no slaving: coarse targets are excluded from the pinning
sets); tiny-room carriers are "generalized bad" with one-sided budget pinning; robust margins pin swallowing-type peaks; NEW: a
near-threshold strict non-peak of ANTI type is pinned like an anti-type peak (its tiny gap is not a rate); one-signed blocks are
d-row-pinned with constants design x u^{-1} (robust q) — only nearly neutral carriers stay free.
(4) EXACTIFYING COMPANION (part 4, PROVED): f^#_w closes all tiny rooms (C1) and tiny target rooms (C2) and RAISES THE THRESHOLD
(C3) of every block containing near-threshold swallowing-type carriers through a DONOR (a peak whose signature tail has the anti sign;
always available at maximal contact), at cost p*(f^# - f) <= C_f T_lo(w)^3 log(1/T_lo(w)) = o(T_lo(w)^2).  After the raise every
near-threshold coordinate (weak peak, DEGENERATE peak, tiny-gap non-peak) is a strict non-peak of f^# (tiny positive gap), all robust
statuses are preserved, d-neutrality is preserved except through closed rooms/targets (Lemma 4.3 = Z3 Lemma 1.4: forced sign).
(5) MASTER THEOREM (5.4, PROVED): for D_X, f in Rec if at infinitely many levels a clean sub-window satisfies (SP_w) [shift sources],
(Do_w) [donors where a raise is needed], (Cmp_w) [each block compensated at w or one-signed] and (NN_w) [no uncompensable
nearly neutral kept carriers].  No growth/rate condition at all.  Corollaries: maximal contact (M1): weak and degenerate swallowing
peaks, near-threshold carriers, rooms: all harmless; (M2): Z4 Theorem A'' without (H3) and without (W_inf), donors instead of (H3).
(6) RESIDUAL (5.6, OPEN): (n) directional nearly-neutral resources in one-signed blocks (incl. Z3 Lemma 1.4 carriers), (m) blocks
neither compensated nor one-signed, (d) "aligned corner" (no donor), (h) failure of (SP_w), (O4) infinite F.  None is a rate.

| # | Statement | Label | Where |
|---|---|---|---|
| 1 | D_X admissible, N-free; (P1), (P2), (P3_X); disjoint bands; survival of Section 8 and Round-5 theorems | PROVED | part 1 |
| 2 | Clean sub-window at every level (pigeonhole) | PROVED | part 2, Thm 2 |
| 3 | Threshold equation Psi(theta) = 0; P = {nu >= theta}; monotonicity | PROVED (+num.) | Lemma T |
| 4 | Quantitative Lipschitz/raising bounds for the threshold; uniform rescaling of relative positions | PROVED | T2, T3 |
| 5 | Diagonal pinning by rooms outside all coarse targets | PROVED | Lemma 3.1 |
| 6 | One-sided pinning of generalized-bad carriers | PROVED | Lemma 3.2 |
| 7 | Shift pinning from window-level sources | PROVED | Lemma 3.4 |
| 8 | Near-threshold anti-type strict non-peaks are pinned | PROVED | Lemma 3.5(b) |
| 9 | d-row pinning of one-signed blocks (robust q) | PROVED | Lemma 3.6 |
| 10 | Exactifying companion: cost o(T_lo^2), status table, d-coefficients | PROVED | Lemmas 4.1, 4.2 |
| 11 | Lemma 1.4 revisited: closing a room of a d-neutral carrier forces q^# = r^nat/A^# > 0 | PROVED | Lemma 4.3 |
| 12 | Repair directions untouched by the companion; (DR) => (Rep) | PROVED | Lemmas 5.1, 5.1' |
| 13 | Transplant: exact d-neutral two-piece data at f^#_w with design x u^{-k} constants | PROVED | Prop 5.2 |
| 14 | Theorem E' (window-dependent c_flat, inward coordinates) | PROVED | 5.3 |
| 15 | MASTER THEOREM | PROVED | 5.4 |
| 16 | Corollaries M1 (maximal contact), M2 (Thm A'' without (H3), (W_inf)) | PROVED | 5.5 |
| 17 | Tiny imbalances can be repaired by converted near-threshold anti-type peaks | SKETCH | 5.6 Remark (3) |
| 18 | Residual (n), (m), (d), (h), (O4) | OPEN | 5.6 |
