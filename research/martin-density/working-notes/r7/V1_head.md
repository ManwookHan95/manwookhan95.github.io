# V1 notes (Round 7): one unified design D_Omega, the ASSEMBLY theorem, the aligned corner, and MASTER THEOREM II

Setting: paper/martin_density_note.tex (Sections 1, 7, 8; numbering and notation as there), Round 5 (Z3-Z6 + referee fixes), Round 6
(Y1-Y4 + referee fixes, incl. Y4_ref_notes C.1-C.8).  Finite block sets I = {1..N}, p = p_N; F = supp a FINITE.  The base U is chosen
DIAGONAL (U^* e_j^* = 2^{-j} k_j), which is admissible (any compact dense-range U).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: V1_part1..5.md (assembled below, after this head); reading digest V1_part0.md; scripts V1_work/*.py.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN for every admissible T (including D_Omega).

## 0. Summary
(1) DESIGN D_Omega (part 1, Theorem 1'; PROVED: admissible, N-free, all listed refereed theorems survive).  SLD with bounded-gap signature
sets S_l = {2^l(2i+1)} and Y3's allowedness rule (c); one design factor Design(l) dominating every design constant of Y1 (D_X), Y2 (Xi^Y),
Y4-ref (2^{s_max}/delta_min, 2^{G_l}, H_tune) and the bank/pull constants (8^{sigma(l)}/delta_min); a rate scheme (R1)-(R7) = Y1's rooms,
target rooms, threshold distances, relative positions + RAY d-COMPONENTS of all zero-cost cones of level l + SHIFT COSTS of all shift
patterns + joint ray objects; M(l) = omega(l)+1 sub-windows with pairwise disjoint bands; Q(w) = (4 Design/u)^{omega+20}.
(2) ASSEMBLY (parts 2-4; PROVED).  At every clean sub-window w (Theorem 2') ONE companion f^#_w = row (A^#, z^#) carries all
exactifications: (C1) close class-G rooms on S^nat, (C2) close tiny target rooms, (C3) a DONOR RAISE of every block containing kept
near-threshold swallowing-type carriers, by a z-move or a BANK at a robust-margin peak (such a peak exists in EVERY block, Lemma D),
(C4) EXACT neutralization of every tiny ray d-component by one least-norm linear solve realized by pulls + private banks (Lemma TU,
explicit solution).  Proved: cost <= C_f Design T_lo^3 log(1/T_lo) = o(T_lo^2) (Lemma CO); no slaving / closure (Lemma NS); status stability
(BS) under the O(Delta) threshold drift, via the raise buffer Lam = T_lo^3 >> drift Design b (Lemma ST); robust rates stay robust (Lemma RR);
transplant to exact d-NEUTRAL two-piece data at f^#_w with design-controlled constants, via ray removal (Proposition TR); Theorem E''
(Theorem E with window-dependent constants and banked + pulled supports).
(3) MASTER THEOREM II (4.3; PROVED).  For D_Omega, F finite: f in Rec as soon as at a clean sub-window of infinitely many levels
(SH_w) [shift sources, or a robust shift cost] and (VR_w) [every extreme ray of the zero-cost cone has at most one robust d-component] hold.
No donor, compensation, one-signedness, nearly-neutral, rate or growth hypothesis.  Corollaries: N = 1 (only (SH_w) needed); maximal
contact (only (VR_w) needed; for N = 1 unconditional).
(4) ALIGNED CORNER (D): EMPTY for D_Omega (Corollary AC; PROVED): banks at the peak's own-sign far contacts push it outward (diagonal base).
Lemma IP (PROVED): "far pulls on the peak itself" — pushing near-threshold coordinates inward by >= 4b(A+theta) in nu-units raises theta and
makes them strict non-peaks (used only as an alternative tool).
(5) RESIDUAL LIST (5.3; exhaustive for Master Theorem II): f notin Rec only if, at all but finitely many levels, EVERY clean sub-window has
(B_w) a GENUINELY MULTI-BLOCK RAY (an extreme ray of C(kappa(w)) with robust d-components in two blocks) or (C_w) a COHERENT SHIFT RESONANCE
(a source-deficient block with TINY shift cost c_{pi(w)} <= b(w)).  (D) = {}.  (E) infinite F: outside.

## 0.1 Results and labels
| # | Statement | Label | Where |
|---|---|---|---|
| 1 | D_Omega: admissible, N-free, disjoint bands, (P1)-(P3) on sub-windows; survival of the listed refereed results | PROVED | part 1, Thm 1' |
| 2 | Clean sub-windows at every level for the scheme (R1)-(R7) | PROVED | part 2, Thm 2' |
| 3 | Lemma D: every block has a coarse robust-margin peak at every clean w of large level (donor candidate) | PROVED | 2.4 |
| 4 | Lemma 3.4' (sources half by half), Lemma S (shift pinning by a robust shift cost; I_up ∩ I_lo = {}) | PROVED | 2.5 |
| 5 | Patterns, zero-cost cones, ray d-components; one-signed blocks carry no robust component | PROVED | 2.6 |
| 6 | Lemma B (masses off the support, diagonal base: exact formula (3.1)) | PROVED | 3.1 |
| 7 | Lemma DR (donor raise by z-move or bank; first-order raise, second-order side effects) | PROVED | 3.3 |
| 8 | Lemma TU (exact two-sided tuning by pulls + banks, explicit solution; re-proves Y4-ref P4 with design constants) | PROVED | 3.4 |
| 9 | Lemma CO (cost o(T_lo^2); data bounds; size of the tuning eta <= Design b) | PROVED | 3.5 |
| 10 | Lemma ST (status table; (BS) under threshold drift; all kept carriers strict non-peaks of f^#) | PROVED | 3.6 |
| 11 | Lemma NS (no slaving; exactified set closed), Lemma RR (robust rates stay robust; tiny components exactly 0) | PROVED | 3.7, 3.8 |
| 12 | Proposition TR (transplant: exact d-neutral two-piece data at f^#_w; K_w <= C_f Design u^{-4}; kinds [1]-[3]; supports) | PROVED | 4.1 |
| 13 | Theorem E'' (Theorem E with window-dependent constants, banked and pulled supports) | PROVED | 4.2 |
| 14 | MASTER THEOREM II and Corollaries M-II.1 (N = 1), M-II.2 (single-block rays), M-II.3 (maximal contact) | PROVED | 4.3 |
| 15 | Corollary AC: aligned corner empty for D_Omega | PROVED | 5.1 |
| 16 | Lemma IP (inward push of near-threshold coordinates raises theta) | PROVED (+num.) | 5.2 |
| 17 | Residual list (B), (C); exhaustiveness for Master Theorem II | PROVED (logical) | 5.3 |
| 18 | Union with Y1 5.4 (with (SH_w) for (SP_w)) covers doubly-robust rays through compensated blocks | PROVED (by Lemma S + Y1) | 5.3(3) |
| 19 | (B) genuinely multi-block rays; (C) coherent shift resonance; (E) infinite F; Lemma Z; density | OPEN | 5.4 |

## 0.2 Refereed results used (dependency list)
Note (refereed): Lemmas lem:threshold, eq:margin, lem:bookkeeping, lem:algebra, prop:forced, prop:smooth(c), rem:lemmaZ(c), def:twopiece,
cor:D1, def:SLD, thm:SLD, lem:twosided, lem:smallness, lem:budget, lem:suplevel, lem:box, lem:finitebase, def:windowcert,
prop:windowcert (claim in (c)), lem:phicalc, lem:switchbudget, lem:split, lem:peakshift (eq:peakshift, eq:didentity), lem:windowtwopiece
(structure), lem:onesidedtransfer, lem:persistence, lem:martintail, thm:reductionZ.
Z3 (refereed): Theorem E, Lemma U, Lemma 3.1 (cost; also as extended in Y4 Lemma 2.2), Lemma 3.2 (referee's "flipped"), Proposition T
step (5) with fixes T2-T6 (structure of the transplant).
Y1 (refereed): Theorem 1, Theorem 2, Lemmas T, T2, T3, Lemmas 3.1-3.6 (pinning; constants per Y1-ref m2, m5), Proposition 5.2 (structure),
Theorem E', kind [1'] (Y1-ref 4), shift trick (Y1-ref (d)), donor bookkeeping (Y1-ref m3).
Y2 (refereed): Lemma T(c),(d),(e), Lemma U', Theorem E', Lemma 5.1/Proposition 5.2 (shift cost; ported as Lemma S), generalized
configurations / G**, D^Y factor Xi^Y.
Y3 (refereed): design D_sigma (Proposition 3.3).
Y4 (refereed): Lemma 1.8 (ray removal), Lemma 2.2 (cost of tuned rows), Lemma 2.3 (banked Lemma U / Theorem E), Theorem 1.6 (pigeonhole).
Y4-ref (C.1-C.7, proved by the Y4 referee, NOT independently refereed): only re-verified parts are used — P1 (pull effect: Lemma B here),
P2 (pulled support in Lemma U: re-verified in Theorem E''), P3 (data at pulls: Proposition TR(iv)), P4 (tuning: re-proved as Lemma TU).

## 0.3 How the task items are answered
(1) Part 1: D_Omega with all requested features (D_X, Xi^Y, D_sigma's bounded gaps and rule (c), Y4-ref fixes, diagonal base with private
bank and pull coordinates); Theorem 1' (admissibility, N-independence, survival list).
(2) Parts 2-4: the companion f^#_w carries (C1), (C2), (C3) [donor raise: z-move or BANK on a robust-margin peak — always available; target
donors and pulls on the peak are not needed], (C4) [all tiny single-block AND multi-block ray components neutralized EXACTLY by pulls +
private banks, which also disposes of wrong-sign nearly neutral kept carriers, residual (n) of Y1]; cost o(T_lo^2) (Lemma CO); closure under
slaving (Lemma NS); (BS) (Lemma ST); robust rates (Lemma RR); transplant with design-controlled constants (Proposition TR); Theorem E''.
(3) Master Theorem II (4.3) with the residual list (B) genuinely multi-block rays, (C) coherent shift resonance; (D) is empty (5.1);
exhaustiveness checked in 5.3.
