# K1 notes (Round 11): items (O-a) and (O-b) of ADDENDUM 10 -- cushion domination at deep-raised companions (Q2 Proposition 3.2) and
# the lever audit at infinite base support; Theorem 5.1 (transport of Master Theorem VI) for lever-regular rows

Setting: paper/martin_density_note.tex (Sections 1, 2, 7, 8), finite block set I = {1..N}, p = p_N, design T_fin^* (Q1's T_fin, option (a),
over the doubly exponential base mu*_s = 2^{-2^{2^s}}, Q2), first rows f with base support F = supp a ARBITRARY.  Sources: r10/Q1_notes.md
(+ Q1_referee_a/b, Q1_refa/refb_notes), r10/Q2_notes.md (+ Q2_referee_a, Q2_refa_notes), r8/U2 (Lemma P, Lemma W, DR-inf, TR-inf, Lemma ND)
with U2-ref, r7/V3 (raise transfer), r7/V1 (TU, TR, ST), r9/X1, X2 with X1-ref, X2-ref, r8/U1 with U1-ref, r5/Z5_ref_notes (Theorem R1).
Part files r11/K1_part1..4.md (reproduced below as Sections 1-4); scripts r11/K1_work/.  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
"PROVED" = complete proof here, citing refereed results precisely (several of them once-refereed, as listed in Q1 3.5 and Q2).

## 0. Summary
(O-a) Q2's Proposition 3.2 is PROVED in a CORRECTED form (Proposition K1.A):
  * the CLASS pigeonhole is compatible with Lemma P once its thresholds dominate the Lemma-P pinning constant 8 C_q 2^{J(w)} D(L)/delta_min(L)
    (window-dependent only through 2^{J(w)} = O(Design(L) + log n(w)), absorbed by the window): active carriers then track the
    decomposition (Lemma K1.2) and are never deep at unraised shallow anti-sign coordinates (Lemma K1.3), while pinned carriers fall into the
    inactive (zero) face automatically -- this IS Q2's "projection of the switching to zero";
  * the CUBE pigeonhole (normalization to one shift ray) is NOT compatible in general (its increment has fixed size ~ eps, not ~ t; Remark
    K1.1', HEURISTIC), but it is NOT NEEDED in route V (Lemma K1.1, PROVED: no step of route V uses a common shift);
  * the "clamping" is Z5-ref's deep assignment (Claim 3.1) applied on F with the data's own switching; it costs <= (1 + eta')t/q_0 + K t in l_1
    (closeness O(K t)); the result is (U3^inf) with the ABSOLUTE constant C_+ = 5 (better than Q2's C Design/u), up to support violations of
    mass O(Design c_{L+1}) (tolerated, Q1-refa P3);
  * the deep box-level raise needs no |g_j| term (Q2's raise level 8 Bx_* + |g_j| was for copied base data).
(O-b) Line-by-line lever audit (part 2.3).  Every lever of Q1's route-V construction acts on one carrier's private near coordinates (first six
  elements of S_l beyond s_max(L)) or far (pull) coordinates; at infinite F each is replaced by one of (P1)-(P6) (Lemma K1.4).  Findings:
  * Q2-refa C.3's "bank with offset" block-norm lever is FALSE as a two-sided lever: along the degenerate direction the TOTAL lever position is
    forced to y^T F(0)/(pi y^T p_{m*}) independently of the offset (numerics: negative, i.e. infeasible for a bank, in 48.7% of random cases);
    repaired by TU on the peak (pull + bank) or (P3)/(P4) on the peak (2.2);
  * offsets never create two-sidedness; far coordinates give only one-sided private moves; two-sided private levers are: Z-con/Z-gen at a near
    off-F or thin coordinate (zero-data carriers), TU = near bank + far pull (data-carrying carriers), Hilbert pairs of thick near coordinates
    with robust spread; otherwise single thick S-mass levers with common mode (rank-one perturbation of the identity);
  * V1's donor raise (C3) is not on the tree of route V; V1's (C1), (C2) act off F as at finite F;
  * with common modes, Step A must tune the RATIOS of ALL coarse strict non-peaks (kappa may float: only ratios enter the cone, Lemma K and the
    true shift), and the linearizations become I - g~ h^T bordered by peak resources (Sys-A) resp. Q2's bordered N (Sys-DC).
  LEVER-REGULARITY is defined as a modulus condition (LR_{w,a}) on these two bordered systems (2.4); it holds automatically when every tuned
  carrier is privately tunable (K1.5(a)), and otherwise reduces to explicit bordered scalars (K1.5(b)).
Step B (static ownership) is DISPENSABLE in route V, at finite and infinite F (Lemma K1.S): with (W_exp), every fine-origin misfit is a
  tolerated violation of mass O(Design c_{L+1}) << s_1, and the scrambling hypothesis (U5) of Theorem UE is needed for COARSE carriers only
  (fine carriers contribute <= 4m C c_{L+1} to S_m).  So "Step B's ownership recursion on J_fine \ F" does not arise.  Status stability under the
  new side effects: Lemma K1.ST.
THEOREM 5.1 (transport) is PROVED for lever-regular rows (4.1), modulo the cited refereed chain and the monotone design enlargement (D-K1)
  (rate objects: near moduli, enlarged patterns, spreads and bordered scalars).  Corollary K1.C gives explicit lever-regular classes, including
  Q2 Corollary 5.2 and all rows whose support profile on each S_l is not nearly proportional to the signature profile at design depth.
THE NON-LEVER-REGULAR CLASS (4.3) is characterized exactly: at all large main stages some tuned carrier is (U) UNPULLED (data-carrying, near
  coordinates off F/thin, deep part of S_l support of the opposite sign or super-thick) or (S) SUPPORT-SWALLOWED (six near coordinates thick with
  tiny spreads, a ≈ c_l v_l there), with no anchor and all bordered scalars tiny; exact limit = Q2 Lemma 4.3 / U2 Lemma ND.  It contains Q2's
  (NDN2) and "KN-1 holds in a degenerate raw direction" and is item (O-c) (K2); the (U) case is new.
(LSC-trunc) for every f, hence density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): still OPEN (reduced to the non-lever-regular class).
No counterexample is claimed; nothing found points to one.

## Results table
| # | Result | Status | Where |
|---|---|---|---|
| 1 | Lemma K1.1 (route V needs no cube normalization) | PROVED | 1.1 |
| 2 | Remark K1.1' (cube increment breaks cushion domination at infinite F) | HEURISTIC | 1.1 |
| 3 | Deep raise without the |g_j| term; choice of J(w), 2^{J(w)} <= Design(L) + 2 log_2(C n(w)) | PROVED | 1.2 |
| 4 | Lemma K1.2 (active coefficients track the decomposition; Lemma-P thresholds) | PROVED | 1.3 |
| 5 | Lemma K1.3 (no deep set at the raised row: deep / robust target / tiny target / shallow non-target cases) | PROVED | 1.4 |
| 6 | Proposition K1.A (= Q2 Prop. 3.2, corrected: (U3^inf) with C_+ = 5, closeness O(K t)) | PROVED | 1.5 |
| 7 | Corollary K1.B (window bookkeeping, (E-d), (E-e')) | PROVED | 1.5 |
| 8 | Lemma K1.4 (first-order action of the resources (P1)-(P6)) | PROVED (from refereed lemmas) | 2.1 |
| 9 | Q2-refa C.3 bank-with-offset is two-sided | FALSE (repaired: TU on the peak) | 2.2 |
| 10 | Line-by-line audit of Q1's levers at infinite F | PROVED | 2.3 |
| 11 | Sys-A in ratio form, Sys-DC bordered; definition of lever-regularity | definition / PROVED structure | 2.4 |
| 12 | Lemma K1.5 (sufficient conditions for (LR)) | PROVED | 2.5 |
| 13 | Lemma K1.6 (realization of Step A and Lemma DC^inf under (LR)) | PROVED | 2.6 |
| 14 | Lemma K1.7 (structure of non-(LR) configurations; exact limit) | PROVED | 2.7 |
| 15 | Lemma K1.S (Step B dispensable in route V; (U5') suffices) | PROVED | 3.1 |
| 16 | Lemma K1.ST (statuses under the new side effects; Lemma PM verbatim) | PROVED | 3.2 |
| 17 | THEOREM 5.1 (transport; (LSC-trunc) at every lever-regular (f, g, rho)) | PROVED mod (D-K1) bookkeeping and the cited chain | 4.1 |
| 18 | Corollary K1.C (explicit lever-regular rows; contains Q2 Cor. 5.2) | PROVED | 4.2 |
| 19 | Characterization of the non-lever-regular class ((U), (S)) | PROVED (as characterization) | 4.3 |
| 20 | (U)-carriers via the ratio trick under a sign condition | SKETCH | 2.7 Remark (1) |
| 21 | (LSC-trunc) at non-lever-regular rows; density for p_N and p | OPEN | 4.3, 7 |
