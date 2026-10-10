# K2 referee, part 4: bookkeeping (O-d) (Lemmas K2.12-K2.14, costs) and Theorem K2.15

## 1. Lemmas K2.12-K2.14 and 6.5 (costs).  VERDICT: correct, one precision on (K2-e).
K2.12 (a) Order inside stage L: carriers of stages <= L, d(L), delta_min(L) -> H(L), D(L), U_L, v_min(L) -> Design(L) (K2-b) -> omega(L) with the
2D(L) objects (K2-c) -> sub-windows, b(w) -> theta_0(w) (K2-d).  No circularity: D(L) does not involve Design(L).  D(L) < infinity because the
finitely many u_k (k in Lambda_L) are in l_1; H(L) bounds 1/v_l on near coordinates under the SLD signature form (v_l(s) >= delta_l 2^{-s}, (D-lev)).
(b) positivity, (c) N-freeness (no rule mentions N or f), (d) monotonicity (U4 Lemma GW; the sub-window bands stay disjoint): correct.
K2.13 (clean dichotomy at depth D(L)): correct; |a_s| and 1 - |z_s| (s <= D(L)) are bona fide rate objects (functions of f with values in [0, 1],
finitely many per level, design count 2D(L)).
CHECK of (K2-e) (objection WITHDRAWN): (P1) closes up to D(L) tiny rooms, but each value moves by |sum_s u_k(s) dz_s| <= b ||u_k||_1 <= b;
(P2), (P3) move values by <= C D(L) theta_0/nu << b.  K2's doubled b in (D1), (D2) (on top of R-8's factor) is sufficient.
K2.14: re-derived.  log(1/b) <= C log^3(1/T) (b is a design power of eta' = T^4/(L Design), exponents <= Design(L) <= n(w) <= log_2(1/T), R-8's factor),
so theta_0 >= exp(-C log^3(1/T)); K_DC <= C_{f,N} Design^{C_0} <= C_{f,N} log^{C_0}(1/T); K_w, C_lev <= exp(C log^2(1/T)); s_1 <= (1 + 32 rho/delta)
exp(-1/(2T)) once 64 rho eps^viol/delta <= exp(-1/(2T)) (eps^viol <= C Design c_{L+1}, c_{L+1} <= exp(-1/T) by (W_exp)).  Hence (L-K2-1)-(L-K2-4)
and eps_E <= eps_DC/8 hold for T small.  Correct.
6.5 costs: preparation <= C_f D(L) theta_0 log(1/theta_0); Step A <= C_f Design^C W log(1/W), W <= Design^C x (compensated pre-placements;
<= Design^C x'_max in general); pre-placements as K1-ref R-6.  Divided by (c_f u T)^2 all tend to 0 (u^2 >= 16 log_2(1/T)^{-1/10}).  Correct.
(O-d) as K2 defines it (the objects introduced by K1/K2) is therefore settled.  K1's (R-lev) objects become unnecessary (K2 uses none of them);
K2.17(e)'s "robust spread" can be weakened to "spread >= Design^{-C}" (part 3), so no spread rate object is needed either.

## 2. Theorem K2.15.  VERDICT: correct as a conditional theorem AFTER strengthening (H1) to a joint condition (gap W-1, fixable).
GAP W-1 (Step 0 with several weak peaks; inherited from K1-ref R-8 and enlarged by K2's extension of (H1)).  (H1) is a PER-PEAK condition ("every
active weak peak has a push resource").  Step 0 must push ALL active weak peaks of (T)-blocks to rho <= 1 - b (X1 KN^tr Step 0; this makes them strict
non-peaks, so that U1 Lemma 1.4(c)'s small Euler share and Lemma R-kt apply).  A (P4) push of k moves every value at FIRST order by the common mode
-g_{k'} h_k (per unit private change), with |h_k| up to H(L)/nu (thick near coordinate, tiny v_k), so |g_{k'} h_k| can exceed 1; K2's extension to
"any design-depth move of K2.4" adds first-order PRIVATE effects u_{k'}(s) on other weak peaks at shared coordinates.  With two or more such pushes
the push system for the weak-peak rows is (I - g_W h_W^T) (two-sided (P4) pushes), singular when 1 - h_W^T g_W = 0 -- the Step-0 analogue of the
Sherman-Morrison degeneracy; then the per-peak resources exist but the joint push is not realizable (or needs moves >> Design^C b/u, outside the
enlarged (D1)).  R-8's fix bounds the side effects on rate objects but not this feedback between weak peaks.
Already for one weak peak, a (P4) push changes its own value by (1 - g_k h_k) per unit: it is a push resource only if |1 - g_k h_k| is robust.
FIX (PROVED as stated).  Replace (H1) by
  (H1*) the Step-0 push problem is solvable within the enlarged (D1) radius: there are admissible moves (far pulls at depth in [2b theta Phi/m,
        x'_max], near banks when Delta''_m > 0, (P1), (P3), (P4), design-depth moves of K2.4 admissible for their data) of total size <= Design(L)^C b/u
        after which every active weak peak of a (T)-block has rho <= 1 - b, i.e. the Step-0 inequality system is A-regular in the sense of K2.9 with
        right-hand side the needed decreases.
  Sufficient: (i) every active weak peak has a PRIVATE push resource (far pull, near bank with Delta''_m > 0, (P3); active weak peaks carry data,
  so (P1) does not occur): cross
  effects between weak peaks are then second order (V1 Lemma B: <= C Design^2 size^2 << b), and pushing each to rho <= 1 - 2b realizes Step 0;
  (ii) the weak peaks pushed by (P4) or shared moves form a system with a robust bordered scalar, |1 - h_W^T g_W| >= u(w) (private ones then absorb the
  first-order cross effects one-sidedly: block-triangular).  Proof of sufficiency: (i) as said; (ii) exact two-sided solve of the (P4) rows with
  ||(I - g_W h_W^T)^{-1}|| <= 1 + ||g|| ||h||/u, moves <= Design^C b/u, then the private pushes of the remaining peaks with their targets shifted by the
  first-order effects (one-sided, scalable: inward pushes may overshoot).  The cone version follows from K2.9(c) applied to the inequality system.
Also a sign slip: (H1)'s "lowering eps_k val_k" must read "lowering vs_k val_k" (the push is inward: rho_k decreases), which is "raising eps_k val_k"
when Delta''_m > 0 (eps_k = -sgn(Delta''_m) vs_k, K1-ref R-8).
With (H1*) in place of (H1), the proof of K2.15 goes through: Step 0 under (H1*); (P) (costs 6.5; data 4.1(c)); Step A by K2.9(c) under (H2); data by
K1 Proposition K1.A (the banked coordinates are E-coordinates of V1 TR with contact-like data, part 2 1(c)); engineered approximant by Theorem UE^inf with
Lemma DC^inf from Theorem K2.6 (K_DC in place of K_J; the protection of the new column coordinates as in part 2); averaging by E^{eng,RT,inf} with
K1-ref B's (E-d) check.  Quantifier order re-checked: design (incl. D(L), H(L), v_min(L), Design(L), omega(L)) -> N -> f, g, rho -> l_f -> main stage L ->
clean w -> J(w) > D(L), f^r -> Step 0 -> classes -> (P) with theta_0(w) -> Lojasiewicz targets -> pre-placements Pi -> Step A -> data -> s_1 -> N_w ->
N'' -> Sys-DC columns -> approximant.  N-independence: the design is N-free; K_DC, l_f depend on N only through f-constants.  c_0 versus l_infty: all
moves are at finitely many coordinates, approximants have z' in c_00 and finite base support (Q2 2.3).
7.2: correct with K2.17 read as in part 3 (with (g) only together with (f)'s criterion).
7.3: the remaining class must be stated with "only if" (part 3, K-6) and with (W) replaced by (W*) := "the Step-0 push problem (H1*) is not solvable"
(contains: some active weak peak has no push resource, and Sherman-Morrison-type degeneracy among (P4)/shared weak-peak pushes).

## 3. Overall status of K2's main claims after this referee pass
Sys-DC ((O-c)(i), (ii)): SETTLED by Theorem K2.6 (PROVED modulo the cited chain; precisions P-1...P-5).  The exact obstruction of Q2-refa C.5 concerns
the square lever system only; the enlarged two-sided system of the PREPARED row is uniformly regular (numerically: s_min 0.07-0.13 at exactly singular
square systems, independent of theta_0).
Sys-A: reduced to the sign class (A*)/(U*) (Theorem K2.16 PROVED; precisions K-1...K-6).  Step 0: reduced to (W*) (gap W-1, fixed by (H1*)).
(O-d): settled.
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2): OPEN.  Nothing found points to a counterexample:
every obstruction identified is a sign/cone degeneracy at the companion construction, not a property of a mate.
