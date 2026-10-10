# Q2 referee (a), part 4 -- Section 5 (assembly), overall assessment, open items

## 1. Theorem 5.1 (transport to infinite F at lever-regular rows).  VERDICT: SKETCH is the right label; architecture coherent.
Route checked for consistency of the quantifier order and of the error accounting:
 f, g, rho -> main stage L, clean sub-window w (rate objects at f, including c_alpha, beta_* for EVERY possible lever configuration of level L: a design
 count, see (p4.1)) -> deep raise f^r beyond J (raise mass sum_{j >= J}(8 Bx_* + |g_j|) is small but NOT o(T_lo^2); it enters only through lambda - 1 -> 0,
 and the transfer error is the Hilbert footprint 2||U* Delta a|| + normer change <= C mu*_J (...) log, which the design makes o(T_lo(w)^2)) -> companion
 f^# of f^r (cost o(T_lo^2), Z3 Lemma 3.1) -> window data (Lemma 3.1, Proposition 3.2) -> s_1 -> N_w -> levers (Lemma DC^inf) -> N'' -> Theorem UE^inf
 -> averaging by Theorem E^{eng,RT,inf} with lambda_j -> 1, eps'_j = footprint + companion cost.
 Hypothesis (a) of E^{eng,RT,inf} at f_j = f^#: V3 Lemma 2.3 at f^r plus p*(f^# - f^r) (triangle inequality): correct.
 (p4.1) The non-degeneracy "max(|c_alpha|, |beta_*|) >= u(w)" is evaluated at the PRE-ROW f_1, which is built after w.  For the pigeonhole it must be a rate
        object fixed before w: define c_alpha, beta_* at f for each of the finitely many lever configurations of level L (a design count) and put them into
        omega(L).  Robust at f implies >= u(w)/2 at f_1, because f -> f_1 moves e and the values by O(mu*_J) + O(Design T_lo^3) + O(K_w s_1) << u(w) = b(w^-).
        (Tiny at f does not imply tiny at f_1, but that is the (NDN2) case, which is excluded by lever-regularity anyway.)  Q2's (R4) should say this.
 Why SKETCH (agree with Q2): Proposition 3.2 for Q1's data; replacement of every lever of Q1's construction; Step B's ownership recursion on J_fine \ F;
 status stability under the side effects of (L2), (L3), S-mass and bank-with-offset levers; bookkeeping.  I add: the block-norm levers must be the repaired
 ones of (p3.4) when the window carries a shift in block m*, and the "tolerated residue" of 4.4(ii) needs the UE variant with |kappa^+-| <= c delta s_1 (SKETCH).

## 2. Corollary 5.2.  VERDICT: SKETCH is the right label.
For F cap (union S_l) finite: for every L with s_max(L) > max(F cap union S_l), every lever coordinate of Q1's construction (z-moves, banks, pulls -- by
X2-ref (p-LV2) the pulls lie in S_l cap (s_max, s_far], donors, block-norm levers) is off F: type (L1), verbatim.  The "more generally" clause (F meets no S_l
of level <= L inside (s_max(L), s_far(w(L))] for infinitely many L) is consistent with that placement of the pulls.  Remaining: Proposition 3.2 (support data on
F are still there and must be cushion-dominated at the deep-raised companion) and the Step B audit.  Correctly stated "modulo".

## 3. Overall assessment of Q2
 * Every PROVED claim I checked is correct: Lemma 1.1, Lemma LT (sharp), Corollary 1.2, Lemma M2^inf, Theorem UE^inf, Theorem E^{eng,RT,inf}, Lemma 3.1,
   Lemma 3.4, Proposition 4.1, Corollary 4.2 (conditional), Lemma 4.3 (a)-(c), the second-order statement of 4.4(ii).  Precisions (p1.1)-(p1.3),
   (p2.1)-(p2.5), (p3.1)-(p3.5), (p4.1); two overstatements in the Consequence of Lemma 4.3 (repaired: private-set version for kappa = 0; bank-with-offset
   block-norm levers when the block carries a shift).
 * SKETCH labels (Proposition 3.2, Theorem 5.1, Corollary 5.2) and OPEN labels ((LSC-trunc) in general, 4.4(iii), (iv)) are honest.  The VERDICT ((LSC-trunc)
   NOT proved for every f) is correct.
 * No counterexample is claimed.  The only negative statements (Lemma 3.4(c); heuristic 1.4) are correct and limited: Lemma 3.4(c) says that, in the exact
   (ND)-failure configuration, support moves cannot raise the degenerate RAW combination (kappa > 0); it does not obstruct (LSC-trunc), because d-consistency
   needs only normalized values, and the d-mismatch needs only the components seen by the switching vectors (my (R3-a)).
 * Scepticism check on "nothing points to a counterexample": I looked for an infinite-F mechanism that the violation-tolerant route cannot absorb.
   (1) Far support used two-sidedly at all scales: absorbed (tail_W after s_1).  (2) Shallow thin support coordinates used beyond the cushion at the window
   scales: Lemma P pins the switching (U2, refereed); the residual is Proposition 3.2's projection (SKETCH).  (3) Infinitely many thick coordinates in the
   lever ranges at all stages with exact (ND)-failure and (NDN2): an exact degeneracy at every level, compatible with Lemma B and the design as far as I can
   see; it blocks EXACT d-consistency (my analysis in part 3, item 8), but the data-side bordering (R3-a) reduces it to a still more degenerate configuration.
   None of these produces a mate that is provably not recovered; each is a construction gap.

## 4. What remains open (precise list, referee's version)
 (O-a) Proposition 3.2 for Q1's data: the zero-switching projection at shallow thin coordinates (Lemma P) and the clamping, inside Q1's (class, cube)
       pigeonhole; window-dependent C_+ <= C Design(L)/u(w) (accepted by E^{eng,RT,inf} after (p2.5)).
 (O-b) Lever audit: every lever of Q1's construction (KN^tr TU levers, KN-1 holds, peak pushes, Lemma DC levers, V1 donors and pulls, the block-norm levers)
       at coordinates of S_l cap F replaced by (L1)-(L3), Lemma DC^inf, or the bank-with-offset block-norm lever (p3.4); Step B's static-ownership recursion on
       J_fine \ F (support coordinates cannot be assigned a z-sign); status stability (V1 Lemma ST) under the new side effects.
 (O-c) Degenerate lever systems at infinitely many levels: (NDN2) for d-consistency.  Exact case: exact d-consistency is impossible when tau_W != 0; needs either
       (R3-a) [residual along yhat blockwise orthogonal to the switching vectors; fails only if y lies blockwise in their span] plus the UE variant with a residual
       kappa^+- <= c delta s_1 (SKETCH), or an argument excluding the configuration.  Quantitative case: c_alpha, beta_* tiny but nonzero and not separated by the
       pigeonhole (they are rate objects only after (p4.1)).  KN-1 raw holds in a degenerate raw direction (Lemma 3.4(c) caps raw targets).
 (O-d) Bookkeeping: moduli |a_s| at design depth, spreads, Sherman-Morrison denominators, c_alpha and beta_* for all lever configurations (p4.1), lever ranges of
       thick S-mass and bank-with-offset levers (p2.2), (p3.3), (p3.4) in omega(L), Design(L) and (LATE).
 (O-e) Everything Q2 inherits: Q1's Master Theorem VI with its once-refereed links (U1-ref MT IV' assembly, Proposition KN, X1-ref KN-1/S-0/K1/W fixes,
       X2-ref (R-abs), CM', C_mix'), and Q1-referee precisions P1-P8.
 Density of NA((c_0, p_N), l_2^2) (any N) and of NA((c_0, p), l_2^2): OPEN.
