# K1 part 4 (Round 11): Theorem 5.1 (transport of Master Theorem VI to arbitrary base support) and the precise non-lever-regular class

## 4.1 THEOREM 5.1 (transport).  PROVED modulo the cited refereed results and the design bookkeeping (D-K1) below.
DESIGN (D-K1).  T_fin^* (option (a)): T_fin of Q1 over the base mu*_s = 2^{-2^{2^s}} with Design(L) >= 2^{d(L)}/(delta_min(L) mu*_{d(L)}^2),
d(L) := sigma(L) + 6 * 2^{L+1}, Q(w) := (4 Design(L)/u(w))^{omega(L) + L^2 + 20} (Q1-refa P8), and with the following objects of level L added
to the rate scheme omega(L) (each a semialgebraic function of finitely many data of f, the count a design number, N-free):
 (R-mod) |a_s| for s in [1, d(L)];  (R-pat) minors and cofactor polynomials of the class cones with the contact rows (X1^F) of part 1.3, for
 all enlarged patterns and classes of level L;  (R-lev) the spreads |1 - rho_s/rho_{s'}| of near coordinates and the bordered scalars of
 Lemma K1.5(b) (1 - h^T g~, (1 - X) lambda_c h^T rt^{(m)} + h_c, c_alpha, beta_*) for all lever assignments of level L.
[Inserting objects only enlarges omega(L), Design(L) and Q(w); by U4 Lemma GW every window condition is monotone under these changes.  The
full bookkeeping (well-foundedness, N-independence) is item (O-d) of ADDENDUM 10 (task K2).]
STATEMENT.  Let N >= 1, f in S_{p_N*} with base support F (finite or infinite), g in C(f), rho in (0,1).  Suppose f is LEVER-REGULAR for
(g, rho): for infinitely many main stages L, at the clean sub-window w(L) of L and the class a(L) selected by the class pigeonhole of part 1.3
(Lemma-P thresholds, no cube), (LR_{w(L), a(L)}) of part 2.4 holds.  Then (f, rho g) lies in the closure of NA((c_0, p_N), l_2^2), along
norm-attaining rows f'_L with FINITE base support; in particular (LSC-trunc)_N holds at (f, g, rho).  If f is lever-regular for every
(g, rho), then f is in Rec(p_N).
PROOF.  Fix N, f, g, rho and l_f = l_f(f, N, g, rho) (Q1 3.1, with Lemma M2^inf of Q2 replacing Lemma M2).  For each main stage L >= l_f of the
hypothesis, with w := w(L), T := T_lo(w):
 Step 1 (clean sub-window).  Q1 Theorem VI Step 1 with the enlarged rate scheme (D-K1): the omega(L) + 1 sub-windows have disjoint bands, so
   some w is clean for f (V1 Theorem 2', U4 Lemma GW, Q1-refb 1.1(d)).
 Step 2 (deep raise).  f -> f^r beyond J(w) (part 1.2): hypothesis (a) of Theorem E^{eng,RT,inf} at f^r with eps'_r <= theta_w T^2; the clean
   classification survives with factor 2 (U2 Lemma DR-inf); budget lemmas at f^r for g^r on the window (V3 (I1)).
 Step 3 (classes).  Two-sided decompositions of g^r at f^r at every dyadic scale of the window; class pigeonhole with thresholds A_i =
   K_*(w)^i (part 1.3): a class a = a(L) with a set S of >= n(w)/D_cl(w) scales (Lemma K1.1: no cube).  Lemma K1.2 holds on S.
 Step 4 (Step A).  Under (LR_{w,a}), Lemma K1.6(A): the companion f^# := f^(1a) with KN^tr's conclusions (exact ratios on Z_kappa, threshold
   protection with the Puiseux margin, robust statuses), p*(f^# - f^r) <= C_f Design^C eta' log(1/eta')/u + 2T^2/(L Design(L)) <= theta'_w T^2,
   theta'_w -> 0.  No Step B (Lemma K1.S).
 Step 5 (data).  Proposition K1.A: for t in S the route-V data with the deep assignment on F form a window family at f_0 := f^# with (U1), (U2),
   (U3^inf) (C_+ = 5, up to support violations of mass <= C_f Design c_{L+1} + C_f c_{L+1}^2/T), (U4), (U5') (Lemma K1.S(c)), (U6) (levers of part
   2 under (LR), Lemma K1.6(B)), (U7); p*(g - g_t) <= K_data t.
 Step 6 (engineered approximant).  Theorem UE^inf at f_0 with: (U5') in place of (U5) (Lemma K1.S(d)); support violations counted in eps (Q1-refa
   P3: at a support coordinate the base excess of a'_j + x_j is <= 2(z_j x_j)_-; the W_F raises of Q2 2.3(ii^inf) protect the theta piece on F);
   Lemma DC^inf from Lemma K1.6(B) (constant K_lev = Design^{C_0}/u in place of K_J; masses at S-mass levers keep |A(p)| >= |A_1(p)|/2 by
   (LATE), Q2-refa (p2.2)); N_w chosen after s_1 and beyond every lever coordinate (Q2 2.3(i^inf), Q2-refa B.2); s_1 := max(64 rho eps^viol/delta,
   exp(-1/(2T))) (Lemma S2c^tr: K_w <= exp(C log^2(1/T)) since every new constant -- K_lev, K_*(w) <= (Design/u)^C (log n(w))^{1/2}, C_+ = 5 --
   is at most a design power times a power of log(1/T)).  The approximant f'_L is norm attaining with finite base support (Q2 2.3), and
   p*(f'_L + tau g'_i) <= 1 + (tau^2/2)(1 - delta) for 0 < |tau| <= c_flat t_i (every piece i), p*(g'_i - rho g_i) <= K_w(K_w s_1 + c_fine + tail_W)/t_i.
   Statuses along f'_L: Lemma K1.ST (Lemma PM verbatim).
 Step 7 (averaging).  Theorem E^{eng,RT,inf} with base rows f_j := f^#(L_j), lambda_j := lambda_r(L_j), eps'_j := eps'_r + p*(f^# - f^r) <=
   (theta_w + theta'_w) T^2; (E-c) with K_j := K_data(w); (E-d), (E-e') by Corollary K1.B (|S| c_flat/K_data -> infinity, K_data T_hi/|S| -> 0,
   c_flat(w) >= c_f u(w) because C_+ = 5 is absolute, Q2-refa B.1); (E-f) by Lemma S2c^tr and (W_exp) (p-E1: K_w c_fine <= K_j T^2 4^{-n}).
   Subset averaging over S: U1 Lemma 2.4 (only the count |S| and "sum over I_r of dyadic t < 2|r|/c_flat" are used).  Conclusion: (f, rho g) in
   cl NA along the norm-attaining f'_{L_j}, which have finite base support.  QED
REMARK (what is new relative to Q2's SKETCH).  (i) Q2 Proposition 3.2 is PROVED in a corrected form (part 1): the cube normalization must be
dropped (Remark K1.1'), and is not needed (Lemma K1.1); C_+ = 5 instead of C Design/u.  (ii) Step B is dispensable (Lemma K1.S), so Q2's item
"Step B's static-ownership recursion on J_fine \ F" disappears.  (iii) The levers are audited (part 2.3); Q2-refa C.3's bank-with-offset
block-norm lever is one-sided along the degenerate direction (part 2.2, numerics) and is replaced by TU on the peak.  (iv) Lever-regularity is
defined as a modulus condition (2.4); it holds automatically when every tuned carrier is privately tunable (K1.5(a)), and otherwise reduces
to explicit bordered scalars (K1.5(b)).

## 4.2 COROLLARY K1.C (explicit lever-regular rows).  PROVED.
f is lever-regular for every (g, rho) -- hence f in Rec(p_N) -- in each of the following cases:
 (a) for infinitely many main stages L, every coarse carrier l <= L has, among the first six elements of S_l beyond s_max(L), a coordinate
     off F or with |a_s| <= b(w(L)), and (if l carries data in some class) a pullable far coordinate at the scales x_A, r of part 2;
 (b) [Q2 Corollary 5.2] F meets no S_l (l <= L) in (s_max(L), infinity) for infinitely many L -- e.g. F ∩ (union_l S_l) finite;
 (c) for infinitely many L, every coarse carrier l <= L whose first six coordinates beyond s_max(L) are all in F has two of them with spread
     |1 - rho_s/rho_{s'}| >= u(w(L)) (rho := a/v_l), and every data-carrying carrier with an off-F near coordinate has a pullable far coordinate;
 (d) any combination of (a)-(c) carrier by carrier, provided the carriers left with (P4) only satisfy the bordered condition of Lemma K1.5(b) or
     an anchor (P5) exists.
Proof.  (a), (c), (d): Lemma K1.5 (a), (b); (b) is a special case of (a) (all near and far coordinates off F; pulls at contacts of sign
eps_l closed by (C1), for support-swallowed-free carriers).  QED
Examples.  (1) If |a_s| decays polynomially on each S_l (e.g. |a_s| ~ s^{-2}), consecutive near ratios satisfy rho_{s'}/rho_s =
2^{s'-s}(s/s')^2 >= 2^{2^{l+1}-1}: robust spread, case (c) for the support-swallowed carriers.  (2) If, for every l, F ∩ S_l contains no
three consecutive elements of S_l beyond some point, then case (a) holds at every large L: the six near coordinates contain an off-F one, and
every v-window [x, x_max] (ratio >= 2^{6G(L)}) contains an off-F element of S_l, which is a contact of sign eps_l after (C1) (pullable).

## 4.3 The precise class of NON-lever-regular rows.  PROVED (as a characterization).
f is not lever-regular for (g, rho) iff for all but finitely many main stages L, at w(L) and a(L), Lemma K1.7 holds: in Sys-A or Sys-DC a
nonempty set Lambda_np(L) of tuned coarse carriers is not privately tunable, each of type
 (U) UNPULLED: carries data, no thick near coordinate, and every coordinate of S_l with x <= v_l(j) <= x_max (x = x_A or r) lies in F with
     s_j = -eps_l or |a^r_j| > x_max (deep support of the opposite sign, or super-thick at depth), or
 (S) SUPPORT-SWALLOWED: the six near coordinates are thick (|a_s| >= u) with pairwise spreads <= b (a_s ≈ c_l v_l(s) on them);
and, when Lambda_np consists of (S)-carriers only: no anchor (every thick coordinate of F ∩ [1, d(L)] lies in the support of a tuned carrier)
and all bordered scalars of Lemma K1.5(b) are <= b(w).  Exact limit (Lemma K1.7(iii)): the configuration of Q2 Lemma 4.3 / U2 Lemma ND.
This class is the infinite-F counterpart of U2's (NDN) (corrected by U2-ref G3 to a regularity modulus) and contains Q2's (NDN2) and Q2 4.4(iv)
("KN-1 holds in a degenerate raw direction").  It is item (O-c) (task K2); the sub-case (U) is new.
WHY THE CLASS IS SMALL (HEURISTIC, not used).  (S) requires a near-proportional profile a ≈ c_l v_l on six consecutive elements of S_l at
infinitely many levels together with exact cancellations of design-free scalars; (U) requires the deep part of S_l to be support of the sign
opposite to l's switching at every window.  Neither is excluded by anything proved here; no mate of such a row is shown to be non-recoverable.
