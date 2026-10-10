# V2 notes (Round 7): items (B) multi-block rays (m') and (C) coherent shift resonance (h') of ADDENDUM 6, F finite

Setting: paper/martin_density_note.tex (Sections 1, 7, 8), finite block set I = {1..N}, p = p_N, F = supp a finite; the
designed admissible operator of the SLD family with the sub-window pigeonhole (Y4 D^PW with Y4-ref A.3 and (G), or V1's
unified design D_Omega), augmented below to D^{V2}; DIAGONAL base U (a free choice); far pulls and private banks
(Y4-ref C.2-C.7).  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Part files V2_part1..4.md; scripts V2_work/.
No counterexample is claimed; nothing found points to one.  Lemma Z and density remain OPEN.

## 0. Summary
**(B) multi-block rays: SETTLED for the companion route (PROVED, modulo the refereed tools cited and the assembly).**
The obstruction behind (m') is determinantal: d-vectors of extreme rays can be nearly dependent while every component is
robust (two-ray example, 2.1: Hoffman ratio 2/delta).  Three tools remove it:
 (1) Lemma H: the Hoffman constant of any finite linear system is <= (norm)^{n-1}/(least NONZERO minor); exactly vanishing
     minors are harmless.
 (2) Lemma L (Lojasiewicz inequality, semialgebraic form): finitely many tiny polynomial objects can be made EXACTLY zero
     simultaneously by a move of size C_L beta^{2/N_L}, with constants depending only on the polynomials.
 (3) The minors of the exact-cone system at a companion are multi-affine polynomials in the carrier VALUES val_l (the
     d-coefficient of a switching strict non-peak is val_l/A_m, Y4-ref C.7), up to one common factor per d-row (Y1 Cor. T3),
     and two-sided per-carrier exact tuning (Y4-ref Prop. P4) realizes any small change of the values exactly.
Making every minor a rate object of the pigeonhole design and choosing b(w) as a design power of T_lo(w) that absorbs the
Lojasiewicz exponent (design D^{V2}), Theorem B gives at every clean sub-window a companion f^# (cost o(T_lo^2)) at which
every minor of the exact system vanishes or is >= u(w)/2, hence the FULL d-row Hoffman constant (all blocks, all rays,
compensated or not, mixed or one-signed) is <= C_f^l Design(l)^2/u(w) (the factor C_f^l, like all C_f^{l^2} factors, is absorbed by the window recursion).  The threshold drift caused by tuning is controlled
by a BUFFER PEAK (Lemma 2.3: every block has, at every large level, a coarse peak with |alpha| >= 1/(2l)) pushed outward by
two-sided tuning (Lemma QB, from Y1 Lemma T2): no donor is needed.  Consequently V1's hypothesis (VR_w) (and Y1's (Cmp_w),
(NN_w), Y2's K_F^rel, Z4's Lemma R constants) are not needed: Corollary B.1, and Master Theorem III below.
**(C) coherent shift resonance: REDUCED (PROVED) to an exact/near-exact d-constrained resonance; remaining step OPEN.**
 - Theorem C1 (dichotomy): with the shift-extended system Sigma^sh (peak traces, zero-cost rows on the coarse targets, the
   d-identity coupling delta_m = -sum q tau, source rows) and its pinning rate rho^sh made a rate object, every clean
   sub-window either pins the shift with a design x u^{-3} constant, or has rho^sh <= b(w).  The case "c_* > 0 but
   decaying beyond the ladder" (Y2 5.3(c)) disappears (Cor. C1.1).
 - Theorem E^>= (Theorem E with Delta d >= 0 data) and Theorem E^SC (Delta d < 0 blocks with (SC) at the companions): PROVED.
 - Proposition C3 (rigidity of shifted data: Sum_m Delta_m R_m^* w_m must vanish at EVERY free coordinate outside the data
   support), Corollary C3.1 (with (T-d) density every coordinate is hit by targets of infinitely many carriers of every
   block: one exact cancellation identity per free coordinate), Proposition C4 (an oscillating profile of the mate on the
   signature set of a robust class-G peak forces |Delta d| >= oscillation/(lambda M) for ALL approximating data at ALL
   first rows sharing the peak: d-neutral data cannot follow non-pinned shifts), Lemma C5 (the fine tail of shifted data
   can always be completed exactly at a cheap companion, Schauder-Tychonoff): PROVED.
 - Remaining step (OPEN, 4.4): in case (II) at all large levels, shifted data are exact at a companion only if the fine
   contributions on the finitely many COARSE free coordinates are absorbed exactly (Slater-stable coarse resonance:
   Theorem C6, SKETCH) — an approximately-two-piece Corollary D1 for fine-origin, coordinate-localized errors, or a
   structural theorem, is needed.
**Master Theorem III (with V1).**  For D^{V2} (built on V1's D_Omega), F finite: f in Rec as soon as at a clean
sub-window of infinitely many levels rho^sh(kappa(w), f) >= u(w).  The only F-finite residual is (C*): rho^sh tiny at all
large levels (an exact or b-near-exact d-constrained coherent shift resonance), plus (E) infinite F.

## Results and labels
| # | Result | Label | Where |
|---|---|---|---|
| 1 | Lemma H (Hoffman via independent row sets and nonzero minors) | PROVED | 1.1 |
| 2 | Lemma L (simultaneous exactification, Lojasiewicz) | PROVED (cites BCR Cor. 2.6.7) | 1.2 |
| 3 | Lemma QB (threshold buffer at a peak) | PROVED (from Y1 T2, T3) | 1.3 |
| 4 | Two-ray determinantal example; component exactification insufficient | PROVED (+ numerics) | 2.1 |
| 5 | Design D^{V2} (determinantal objects, Lojasiewicz-adjusted b(w)); Lemma 2.1 | PROVED | 2.2 |
| 6 | Lemma 2.3 (buffer peaks with abs(alpha) >= 1/(2l) at every level) | PROVED | 2.3 |
| 7 | Theorem B (exactification of all tiny minors; d-row Hoffman constant <= C_f^l Design^2/u) | PROVED (modulo cited tools; assembly hypotheses (A1),(A2)) | 2.4 |
| 8 | Corollary B.1 ((HF) of Prop. T with design/u; (m), (m'), (NN_w), (Cmp_w) not residuals) | PROVED (given the assembly) | 2.4 |
| 9 | Lemma 3.1, Definition 3.2 (shift-extended system, pinning rate rho^sh) | PROVED | 3.1 |
| 10 | Theorem C1 (dichotomy at clean sub-windows) | PROVED | 3.2 |
| 11 | Corollary C1.1 (combinatorial shift cost is a design constant; no decay beyond the ladder) | PROVED | 3.2 |
| 12 | Theorem E^>=, Theorem E^SC | PROVED | 3.3 |
| 13 | Proposition C3 (rigidity of shifted data), Cor. C3.1 (a),(c) | PROVED | 4.1 |
| 14 | Cor. C3.1(b) reading "non-generic at partial contact" | HEURISTIC | 4.1 |
| 15 | Proposition C4 (oscillating profiles force shifted data) + example | PROVED | 4.2 |
| 16 | Lemma C5 (fine-tail completion) | PROVED | 4.3 |
| 17 | Near-coordinate conversion on good coarse signature sets | SKETCH | 4.3 |
| 18 | Theorem C6 (stable shifted resonance -> recovery) | SKETCH (block-scalar exactification unproved) | 4.4 |
| 19 | Master Theorem III (V1 Master Theorem II + Theorem B + Theorem C1) | PROVED modulo V1 (unrefereed) | 5 |
| 20 | Residual (C*) and item (E) | OPEN | 5 |

## What is used (exactly)
Design: (D0)-(D2), allowedness (a),(b), (P1)-(P3) of def:SLD; bounded gaps G_l of the S_l (Y4-ref (G)); the sub-window
recursion of D^PW / D_Omega; the two additions of Def. 2.2 (determinantal objects; b(w) adjusted to the Lojasiewicz exponent)
and of Def. 3.2 (shift-pinning objects); 1/delta_comb(l), 1/delta_sh(l), Lip(l), C_L(l) in Design(l).  All N-free.
Base: U diagonal.  Refereed tools: Z3 Theorem E, Lemma U, Lemma 3.1, Lemma 3.2, Prop. T; Y4-ref C.2-C.7 (Lemmas P1-P3,
Prop. P4, Cor. P5); Y1 Lemmas T2, T3, 3.1-3.5, Prop. 5.2, Theorem E'; Y2 Lemma T, Lemma 5.1, Prop. 5.2; Z4-ref Lemma 3.2,
Prop. 5.6'; the note's Lemmas lem:threshold, lem:switchbudget, lem:phicalc, lem:peakshift (eq:didentity), lem:suplevel,
Corollary cor:D1, Theorem thm:engineered.  Unrefereed: V1's assembly (Master Theorem II) for Master Theorem III only.
External: Lojasiewicz inequality (Bochnak-Coste-Roy, Real Algebraic Geometry, Cor. 2.6.7); Schauder-Tychonoff fixed point
theorem; Hoffman-type normal cone description of polyhedra (Farkas), Cauchy-Binet.
