# Referee report on K1 (Round 11): cushion-dominated window data at deep-raised infinite-support rows (O-a) and the lever audit (O-b)

Refereed: r11/K1_notes.md (= K1_head + K1_part1..4 + K1_tail, checked identical) and r11/K1_work/ (offset_check.py, deep_assign_check.py; re-run,
outputs identical).  Checked against: r10/Q1_notes.md 2.2-2.6 with Q1_referee_a/b and Q1_refa_notes (P2, P3, P6, P8); r10/Q2_notes.md 2.2-2.5, 3.2-3.3,
4.0-4.4 with Q2_referee_a and Q2_refa_notes (B.1, B.2, C.1-C.7); r9/X2_notes.md 3.1-3.5, 4.1 (Theorem UE, Lemma UE-1, Theorem E^eng) with X2_ref_notes
3-4; r9/X1_notes.md 2.1-2.2 ((T)-blocks, Step 0); r8/U1_notes.md 1.1-1.5, 2.1-2.6, 4.1-4.3 with U1_ref_notes 4; r8/U2_notes.md 1.2 (Lemma P);
r5/Z5_ref_notes.md 2 (Claim 3.1); cross-checked with r11/cert2_report.md and cert3_report.md (E^eng with window-dependent c_flat).
My part files: r11/K1_ref_part1.md (Section 1 of K1), K1_ref_part2.md (Section 2), K1_ref_part3.md (Sections 3-4).  Proofs of all corrections:
r11/K1_ref_notes.md.  Scripts and outputs: r11/K1_ref_work/.  Role: adversarial referee.

## 0. Bottom line
K1's two main contributions are correct and valuable.  (1) Item (O-a) is settled: at the deep-raised row, class thresholds that dominate the
Lemma-P pinning constant (window dependent only through 2^{J(w)} = O(Design(L) + log n(w))) make every pinned carrier inactive, so the route-V data have
no deep anti-sign set (Lemma K1.3), and Z5-ref's deep assignment on F gives side cushion domination (U3^inf) with the ABSOLUTE constant C_+ = 5
(Proposition K1.A).  The cube normalization is not needed in route V (Lemma K1.1).  (2) Step B (static ownership, self-aligned fine carriers, G1
release) is dispensable in route V at finite and infinite F (Lemma K1.S): with (W_exp) the fine carriers enter the scrambling and violation budgets
only through their total weight c_{L+1} << s_1.  The correction (C2) of Q2-refa C.3 (a bank with offset is one-sided along the degenerate direction)
is right; I confirmed it with a nonlinear test.
There are three fixable gaps in the transport theorem and its supporting lemmas, and the characterization of the non-lever-regular class is misstated:
 R-6 (cost accounting): Corollary K1.B and Theorem 5.1 do not check the third condition of (E-d), theta'/c_flat(w)^2 -> 0, which E^eng needs when c_flat
     depends on the window (c_flat ~ u(w)).  With K1's x_max = T^2/(L Design |Lambda|) the far pulls and in-F lowerings cost up to ~ T^2 log(1/T)/L.  That is
     not even o(T^2), and theta'/c_flat^2 -> infinity.  FIXED by x'_max := u(w)^2 T^3/(Design(L)^2 |Lambda|) with pulls at the smallest pullable depth.
 R-7 ((P6) through an S-mass lever on the peak): the claim that Q2-refa C.3(iv)'s rank-one argument applies "verbatim" is false, because the common mode
     h0 = O(Design/u) is not small.  The correct bordered scalars are c'_alpha = c_alpha + (h0/pi) q*^T D^{-1} g and beta'_* = beta_* + (h0/pi)(1 - q*^T p*).
     PROVED, numerically confirmed.  They must be added to (R-lev).
 R-8 (Step 0): KN^tr's Step 0 pushes the active weak peaks of (T)-blocks before the Lojasiewicz step, and (LR) does not cover it.  For Delta''_m < 0 such a
     push needs a pull, (P3) or (P4).  A (P4) push moves every rate object by Design^C b/u, which exceeds (D1)'s radius.  FIXED by adding a push condition
     to (LR) and enlarging (D1) by the factor Design^C/u(w).
 R-10, R-11, R-13 (characterization): Lemma K1.7(i) misses a third type of carrier (M): a data-carrying carrier with mixed near coordinates and no pull.
     The exact-limit statement holds only on F_thick ∩ [1, d(L)].  The "iff" of 4.3 is false for configurations with (U)-carriers: peak resources can
     border them, so such rows can still be lever-regular.  It is correct as a necessary condition, and as an iff for (S) ∪ (M)-only configurations.
With these fixes, Theorem 5.1 is PROVED modulo the cited chain (several links once-refereed) and the design bookkeeping (D-K1) = (O-d).  Theorem 5.1 then
says that (LSC-trunc)_N holds at every lever-regular (f, g, rho).  (LSC-trunc) for every f, density of NA((c_0, p_N), l_2^2) and of NA((c_0, p),
l_2^2) remain OPEN, as K1 states.  No counterexample is claimed, and nothing I found points to one.

## 1. Verdicts
| Claim (K1 label) | Verdict | Main point |
|---|---|---|
| Lemma K1.1 (PROVED) | correct | no step of route V uses a common shift; U1 Lemma 4.2's dominance is uniform over the class, so even Step B does not need the cube; the Gamma error is K_data t |
| Deep raise and J(w) (PROVED) | correct | moduli change by the factor 1/lambda_r, not by O(mu*_J) (harmless, R-1); b enters J(w) only through log (R-2) |
| Lemma K1.2 (PROVED) | correct, constant slip | K_* >= 5(HJ+2) gives a 1/5 error relative to |c^act|, not to |c| (R-3); K1.3 unaffected |
| Lemma K1.3 (PROVED) | correct | four cases exhaustive; Lemma P hypotheses checked at f^r; arithmetic re-done |
| Proposition K1.A (PROVED) | correct | deep assignment with trace slack re-derived (exact rational test, 0 violations); C_+ = 5; support excess tolerated as in Q1-refa P3 |
| Corollary K1.B (PROVED) | incomplete | theta'/c_flat^2 -> 0 not checked; fails with x_max; fixed by x'_max (R-6) |
| Lemma K1.4 (PROVED) | correct for (P1)-(P5) | (P3) orientation, TU net range [-d_p, infinity) checked |
| (C2): Q2-refa C.3 bank with offset | K1 correct | forced total position y^T F_orig(0)/(pi y^T p); nonlinear test confirms |
| Lever audit (PROVED) | correct inventory, two omissions | (P6) via (P4) (R-7); Step 0 weak-peak pushes (R-8) |
| Sys-A, Sys-DC, (LR) | Sys-A correct; Sys-DC needs R-7; (LR) needs R-8 | ratio form and floating kappa verified; (LR) is a hypothesis, not a rate object |
| Lemma K1.5 (PROVED) | (a), (b1), (c) correct; (b2) incomplete | bordered inverse independent of 1 - h^T g~ (numerics 1.8e-12) |
| Lemma K1.6 (PROVED) | correct up to R-6, R-8 | Poincare-Miranda needs C_2 ||R||^2 rho_A <= 1/4 (holds) |
| Lemma K1.7 (PROVED) | (i) false as stated; (iii) overstated | missing type (M) (R-10); exact limit only on F_thick ∩ [1, d(L)] (R-11) |
| Lemma K1.S (PROVED) | correct | fine part of S_m <= 6m c_{L+1} << s_1 under (W_exp) |
| Lemma K1.ST (PROVED) | correct | with R-8's enlarged (D1) for Step-0 common modes |
| Theorem 5.1 (PROVED mod (D-K1), chain) | correct with fixable gaps | R-6, R-7, R-8; corrected statement in K1_ref_notes E |
| Corollary K1.C (PROVED) | correct with precisions | (c) wording; Example (2) needs uniform starting points (R-12) |
| Characterization (PROVED) | necessary condition correct; "iff" false | (U)-carriers can be bordered by peak resources (R-13) |
| Ratio trick (SKETCH) | SKETCH honest | needs |rt_l| >= u (R-14) |

## 2. Main findings
F1 (O-a is settled).  Lemma K1.2 + Lemma P + the deep raise: a carrier that is deep at an unraised shallow anti-sign coordinate has actual amplitude
   <= (5/4) C_q 2^J t/delta_min.  The class thresholds K_*^2 K >= 8 C_q 2^J D/delta_min put it in the zero face, and the active carriers track the
   decomposition.  The deep assignment then needs no |g_j| term and gives C_+ = 5, which improves Q2's C Design/u.  The window dependence through 2^{J(w)}
   costs only (log n(w))^{(L+N+2)/2} in K_data, which the window length absorbs.
F2 (K1.S is right and simplifies the whole chain).  (U5) enters Theorem UE only via Lemma UE-1(e).  Coarse carriers are never scrambled below x_0(w), and
   fine carriers contribute <= 6m c_{L+1} <= exp(-1/T) << s_1 >= exp(-1/(2T)).  The J_fine violations are O(Design c_{L+1}), with b^theta = 0 at free
   coordinates.  This removes Step B and with it Q2's "ownership recursion on J_fine \ F", whose coordinates of F could not be assigned.
F3 (R-6, a real gap).  Q1 verified theta/c_flat^2 -> 0 explicitly (Theorem C^tr).  K1's new far moves (lowering of in-F pull coordinates, pull z-flips
   at depth up to x_max, TU bank compensation) add a cost ~ C Design |Lambda| x_max log(1/T) = C T^2 log(1/T)/L.  Because log(1/T) >= n(w) >> L Design(L),
   this is not o(T^2).  For i >= 2, u = b(w^-) <= T_lo(w^-)^4/(L Design), so theta'/c_flat^2 -> infinity.  Fix: x'_max = u^2 T^3/(Design^2 |Lambda|) and pulls at
   the smallest pullable depth.  The window [x_A, x'_max] keeps ratio >= 2^{6G(L)}.
F4 (R-7).  For a (P4) block-norm lever the degenerate set is {c'_alpha = beta'_* = 0}, not Q2's {c_alpha = beta_* = 0}.  In degenerate one-block systems
   with robust beta_*, a (P4) column with h0 = -pi beta_*/(1 - q^T p) is not onto (2797/2797 instances).  Conversely, in Q2's doubly degenerate case a
   (P4) peak lever borders N (1577/1577).  This does not help in the exact full degeneracy, where peaks have no thick near coordinates.
F5 (R-8).  Step 0 of KN^tr is not covered by (LR).  Add a push condition to (LR) and enlarge (D1).
F6 (R-10, R-11, R-13).  The non-lever-regular class is "some tuned carrier is (U) or (S') = (S) ∪ (M), plus tiny bordered scalars and no anchor if all are
   (S')", as a NECESSARY condition.  (U)-carriers can be lever-regular through peak bordering (efficiency (1 - X) lambda_c |rt_l|).

## 3. Attacks attempted
uniformity in t (Lemma P per scale; one class on S; thresholds fixed per window): OK.  Window dependence of K_*(w), K_data, J(w) (log n(w) powers;
(E-d) first two parts): OK.  Number of carriers (J_Om <= L + N): OK.  Along companions and raises (rate objects under the deep raise, R-1; Step-A moves
<= Design^C eta'/u): OK.  Levers inside the support and their side effects (common modes on statuses: OK by K1.ST; on Step 0: R-8; on block-norm
bordering: R-7).  Offsets (C2): confirmed.  Hoffman/minor constants (enlarged patterns are contact patterns on T(L) of G**-type, weight-free rows):
OK.  Signs at support coordinates (thin near coordinates of data-carrying carriers carry the data sign; deep anti-sign support only within cushions;
pulled coordinates dominated by the pull mass): OK.  c_0 versus l_infty (all data in l_1, approximants with finite base support): OK.  Quantifier
order: OK.  Cost accounting against the window-dependent c_flat: FOUND R-6.  Characterization: FOUND R-10, R-11, R-13.  Counterexample: none.

## 4. Numerics (sanity only; r11/K1_ref_work/)
K1's scripts re-run: identical.  ref_offset_nonlinear: the one-sided bank with quadratic remainder leaves min ||F||^2 >= 0.52 (y^T F_0)^2 in 23/23 instances
with a negative forced position; the two-sided control reaches <= 4.5e-13.  ref_deep_assign (exact rationals, 60000 instances, boundary cases): 0
violations of the deep-assignment claims and of the F_low split bound.  ref_bordered: Sys-A bordering identity to 4e-14 and explicit inverse to
1.8e-12; (P4)-type block-norm failure 2797/2797.  ref_p4_peak_scalars: Proposition R-7 inverse residual 3e-15; Q2 doubly degenerate case bordered
1577/1577.  ref_cost_ratio: R-6 exponents (log2 theta'/c_flat^2 ~ +8e3, +8e5, +8e7 with x_max; -2.9e5, -1.3e8, -1.2e11 with x'_max).

## 5. Single most valuable idea
Lemma K1.S: in the violation-tolerant route the fine structure needs no construction at all.  Under (W_exp), fine carriers enter the scrambling term of
Theorem UE and the violation budget only through their total weight c_{L+1} << s_1.  So the static-ownership recursion (Step B), which could not be
carried out where fine signature sets meet the base support, can simply be dropped.  A runner-up is the observation behind Lemmas K1.2-K1.3: class
thresholds that dominate the Lemma-P pinning constant make the class pigeonhole itself perform the "projection of pinned switching to zero".

## 6. What remains open (precise)
(1) The non-lever-regular rows (with the corrected definition): at all large main stages L, at w(L) and a(L), the bordered systems Sys-A/Sys-DC have no
    right inverse of norm <= Design^{C_0}/u, or some active weak peak of a (T)-block has no push resource.  Necessarily some tuned carrier is (U) (data-
    carrying, no thick near coordinate, no pullable far coordinate in [x, x'_max]) or (S') = (S) ∪ (M) (only (P4) two-sided).  If all are (S'), there is
    no anchor and every bordered scalar (1 - h^T g~, (1 - X) lambda_c h^T rt + h_c, c_alpha, beta_*, and R-7's c'_alpha, beta'_*) is tiny; this contains
    Q2's (NDN2) and Q2 4.4(iv), item (O-c), and the exact degenerate case is obstructed by Q2-refa C.5.  The (U)-case: the ratio trick or peak bordering
    (R-13, R-14) is a SKETCH.
(2) Item (O-d): bookkeeping of (D-K1) with the additions (R-lev) += {c'_alpha, beta'_*} (R-7) and the enlarged (D1) (R-8): well-foundedness, N-independence
    and monotonicity (U4 Lemma GW).  x'_max (R-6) is a window quantity and needs no design change.
(3) Inherited: the once-refereed links of Q1's chain (U1-ref MT IV' tools, X1-ref KN^tr, X2-ref CM'/C_mix') and of Q2 (UE^inf, E^{eng,RT,inf}).
(LSC-trunc)_N for every f, hence density of NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2): OPEN.
