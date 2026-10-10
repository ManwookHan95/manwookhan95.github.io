# K1 referee, part 3: Sections 3-4 of K1: Lemma K1.S, Lemma K1.ST, Theorem 5.1, Corollary K1.C, the characterization, the ratio trick

## 3.1 Lemma K1.S (Step B dispensable in route V).  Verdict: CORRECT.  (This is the most useful new observation of K1.)
Where (U5) enters Theorem UE: only Lemma UE-1(e) (X2 3.3), through the Phi-mass of A_m ∩ {t_k <= Pi} (scrambled carriers of lem:anchor), which X2 bounds
by Scr^{(0)}_m(2K_*Pi) <= C_S(2K_*Pi)^2.  X2-ref (p-UE2) already notes that d-consistent Omega carriers are in S_2 whatever their gap, so (U5) is needed
only for peaks and fine carriers.  Re-derivation of K1's replacement: by K1.S(c) (coarse peaks margin >= u/2, coarse non-peaks gap >= g_min(w) at f^#;
values and thresholds move by <= K_w Pi, UE-1(b), (c)) no coarse carrier is scrambled once 2K_* Pi <= x_0(w); every fine carrier k contributes
Phi_k^2 + lambda_k(|w' - w^0| + (C' - C)_+) <= Phi_k + 3 m Phi_k, so the fine part of S_m is <= 4m sum_{k > L} Phi_k <= 6m c_{L+1}.  With (W_exp)
(c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T)) and s_1 >= exp(-1/(2T)) (Lemma S2c^tr / X2-ref (S2c)), 6m c_{L+1} <= c_late delta s_1/4 for T small.
Violations on J_fine: ||V 1_{J_fine}||_1 <= C_f D(L) 2^{-s_far} + C_Delta sum_{k>L} lambda_k <= C_f Design c_{L+1} (coarse carriers meet J_fine only on
S_l ∩ (s_far, inf), 2^{-s_far} <= c_{L+1}^2); chi = 1/2 at free coordinates gives b^theta = 0 ((H3)); at contacts (z b^+)_- + (z b^-)_+ = (zV)_-.
X2-ref's own CM'(c) already tolerated the positive-owned coordinates of J_fine with the same bound, so the extension to all of J_fine is consistent.
Nothing else used Step B: Lemma PM bounds fine clamp terms by sum_fine Phi^2 whatever the statuses; UE-1(d) bounds fine Bregman terms by c_fine.
Consequences (correct): Q1 CM^tr Step B, X2 Lemma CM(a) and the G1 release are redundant in route V once (W_exp) holds; Q2's item "ownership
recursion on J_fine \ F" disappears.  Precision: K1.S(d) uses that every rate requirement on s_1 is at most exp(-C log^2(1/T)) (Lemma S2c^tr) -- the
new window constants K_*(w) (<= (Design/u)^C (log n(w))^{1/2}), K_lev, C_+ = 5 keep K_w <= exp(C log^2(1/T)): checked.

## 3.2 Lemma K1.ST (statuses under the new side effects).  Verdict: CORRECT (with R-8's enlarged (D1) for Step-0 common modes).
(a) Ratio-form exactness fixes every coarse non-peak status through X1 Lemma K (rho_d = m|r_d| K(sigma, R^2)/Phi_d): verified that sigma depends only on
the peak set (robust peaks stay peaks; fine peaks contribute O(c_{L+1}^2)).  At f': Lemma PM's three inputs (nv' = nv^# on Omega exactly; coarse
peaks clamped; fine terms <= C sum_fine Phi^2) do not involve privacy: common modes of (P4)/(P5)/(P6) move only peaks (margin u/2 >> K_lev r h) and fine
carriers.  (b) Deep raise: values move by O(mu*_J) <= b^2 Phi_min/Design; moduli by the common factor 1/lambda_r (R-1); lowering a far in-F coordinate
keeps z and moves e by <= 2 mu*_j x'_max/nu.  Remark on V1 Lemmas ST/NS: right ((C3) unused; (C1), (C2) off F).

## 3.3 Theorem 5.1 (transport of Master Theorem VI to arbitrary base support).  Verdict: CORRECT WITH FIXABLE GAPS (R-6, R-7, R-8); with the fixes
## below it is PROVED modulo the cited (partly once-refereed) chain and the design bookkeeping (D-K1) = item (O-d).
Step-by-step check:
 Step 1 (clean sub-window with the enlarged rate scheme): monotone enlargement of omega(L), Design(L), Q(w) (U4 Lemma GW).  OK.
 Step 2 (deep raise): OK (1.2; R-1, R-2 notational).
 Step 3 (classes, Lemma-P thresholds, no cube): OK (Lemma K1.1; R-3 constant).
 Step 4 (Step A under (LR)): needs R-8 (Step 0's weak-peak pushes must be realizable; enlarged (D1) for (P4) pushes).  Cost: with K1's x_max the far
   moves cost up to ~ T^2 log(1/T)/(L Design) (pull z-flips C_f v log(e/v), in-F lowerings, TU bank compensation), which is NOT o(T^2) (log(1/T) >= n(w)
   >> L Design(L)) and NOT o(c_flat^2 T^2); R-6's x'_max = u^2 T^3/(Design^2 |Lambda|) fixes it.
 Step 5 (data): Proposition K1.A: OK.
 Step 6 (UE^inf at f^#): (U5') by K1.S: OK; support excesses tolerated (Q1-refa P3): OK; Lemma DC^inf from K1.6(B) with R-7's scalars for (P4)-type
   block-norm levers; in-F DC pull coordinates lowered at the pre-row with cost <= 4 x'_max each (inside theta').  OK after fixes.
 Step 7 (averaging, E^{eng,RT,inf} with window-dependent c_flat): (E-d)'s third condition theta'_j/c_flat(j)^2 -> 0 (X2 4.1, Q2-refa B.1) was not
   checked by K1 and FAILS with x_max (R-6); with x'_max: theta' <= theta_w + C Design^C T^2 log(1/T)/u + C u^2 T log(1/T), and theta'/c_flat^2 <=
   C Design^C T^2 log(1/T)/u^3 + C T log(1/T) -> 0.  (E-d) first two parts and (E-f), (p-E1): OK (Corollary K1.B).
 Quantifier order: design (with (D-K1) objects) -> N -> f -> (g, rho) -> l_f -> L -> clean w -> J(w), f^r -> Step 0 -> classes (thresholds K_*(w), f-dependent
   through C_q, legitimate) -> Step A -> data -> N_w -> s_1 -> N'' -> DC levers -> f'_L.  Verified; x'_max is a window quantity (no design change).
 Statement: "lever-regular" must be read with the corrected (LR) (R-8 added; (P4)-type (P6) with R-7's scalars) and the class a(L) = some class with
   >= n(w)/D_cl(w) scales.  The conclusion (f, rho g) in cl NA along NA rows with finite base support, hence (LSC-trunc)_N at (f, g, rho), follows.

## 3.4 Corollary K1.C (explicit lever-regular rows).  Verdict: CORRECT with precisions.
 (a) OK; "every coarse carrier l <= L" includes the active weak peaks, so R-8 is covered; "pullable" now refers to the window [x, x'_max].
 (b) OK (all near and far coordinates of S_l off F; data-carrying carriers are class G, S^nat_l consists of contacts of sign eps_l after (C1), so every
     depth is pullable; zero-data carriers have (P1)).  Note union_{l >= 1} S_l = even numbers, so "F ∩ (union S_l) finite" = "F almost odd".
 (c) Read "two THICK coordinates with spread >= u" and "an off-F OR THIN near coordinate".  [R-12]
 Example (1) (|a_s| = s^{-2} on S_l ⊂ F): rho_{s'}/rho_s = 2^{G_l}(s/s')^2 >= 2^{2^{l+1}-2} for s >= 2^{l+1}, spread >= 3/4: robust; near moduli >> u: thick.  OK.
 Example (2) needs UNIFORMITY: "for every l, no three consecutive elements of F ∩ S_l beyond some point p_l" does not give the condition at level L for
     the carriers l close to L unless p_l <= s_max(L); state it as "beyond s_max(l)" (or p_l <= s_max(L) for all l <= L at infinitely many L).  [R-12]

## 3.5 Characterization of the non-lever-regular class (K1 4.3).  Verdict: NECESSARY CONDITION CORRECT after adding type (M); the "iff" is FALSE as
## stated for configurations containing (U)-carriers.  [R-10, R-13]
 * Necessity ("not (LR) at all large L => some tuned carrier (now including Step-0 weak peaks) is (U) or (S') = (S) ∪ (M); if all are (S'), no anchor and all
   bordered scalars (with R-7's for (P4)-type (P6)) are tiny"): PROVED from K1.5 with R-7, R-10.
 * Sufficiency fails for (U): a (U)-carrier contributes a row without a two-sided private column, but bordering columns (one peak resource per block,
   anchors) can supply the missing rank: in Sys-A a buffer-peak push of block m has entries -(1 - X) lambda_c rt_l on the ratio rows of block m, so with one
   (U)-carrier per block and a two-sided peak resource the square system can be regular (it is, whenever the corresponding bordered minors are robust).
   So rows with (U)-carriers may be lever-regular.  The correct statement: (LR) fails iff the bordered systems (all admissible assignments, (U)-carriers
   contributing rows only) have no right inverse of norm <= Design^{C_0}/u -- which is the definition -- and the structural description is a necessary
   condition.  For (S')-only configurations K1.5(b) gives the iff (tiny scalars => s_min of the bordered matrix <= C b ||h||, so rho_lev << u/Design^{C_0}).
 * The exact-limit sentence (Q2 Lemma 4.3/U2 Lemma ND structure on all of F) is overstated: only on F_thick ∩ [1, d(L)] (R-11).
 * Containment of Q2's (NDN2) and Q2 4.4(iv): correct (both are (S')-configurations with tiny bordered scalars).

## 3.6 Ratio trick for (U)-carriers.  Verdict: SKETCH (label honest); precision R-14.
Linear algebra re-derived: in ratio form d(val_l/kappa) = (d val_l - rt_l d kappa)/kappa; with rt_l > 0 for all (U)-carriers of block m and a two-sided
buffer-peak resource, d kappa := kappa max(0, max_U(-delta_l/rt_l)) and d val_l := kappa delta_l + rt_l d kappa >= 0 realize any small ratio correction
with banks only.  Needs in addition |rt_l| >= u for the (U)-carriers (else d kappa ~ kappa |delta|/|rt_l| is not small), the other carriers of the block
two-sided, the nonlinear (cone-domain degree) argument and the Sys-DC analogue (A_m in place of kappa through a block-norm lever).  Mixed signs of rt
inside a block are not covered.  SKETCH.

## 3.7 Attacks attempted (all on K1's PROVED claims)
uniformity in t (Lemma P per scale; class fixed on S; thresholds per window) -- OK; window dependence of K_*(w), K_data (log n(w) powers) -- OK;
number of carriers (J_Om <= L + N) -- OK; companions and raises (rate objects under the raise: R-1) -- OK; levers inside the support and side effects:
(P4) common modes on statuses (K1.ST) OK, on Step 0 (R-8), on block-norm bordering (R-7); offsets (C2) confirmed nonlinearly; Hoffman/minor constants
(enlarged patterns are G**-type contact patterns) -- OK; N-independence -- inherited (O-d); signs at support coordinates (thin near coordinates of
data-carrying carriers have the data sign; deep anti-sign support only through cushions) -- OK; c_0 vs l_infty (all data in l_1; approximants finite
support) -- OK; quantifier order -- OK; COST ACCOUNTING against the window-dependent c_flat -- FOUND R-6; characterization -- FOUND R-10, R-11, R-13.
Counterexample: none suggested by anything found; every defect is a bookkeeping/route defect with a repair, or a precisely described open class.
