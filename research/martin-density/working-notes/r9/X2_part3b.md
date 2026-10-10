# X2 part 3b — Theorem UE (uniform engineered bound, violation tolerant, d-consistent) and its proof

## 3.4 Theorem UE.  PROVED (a line-by-line modification of the refereed proof of thm:engineered and of U3's Lemma VT, with the
## estimates of Lemma UE-1 replacing every "late stage" statement).
There are f-constants t_1 in (0,1], c^f_flat in (0, 1/8], K_sharp >= 1, eta_1 in (0, 1/4], c_late > 0 and the radius r_f := r_f(eta_1) of
Lemma M2 with the following property; put c_flat := min(c^f_flat, gamma_B/(8 rho A_2)) (an f-constant when gamma_B is fixed; >= c_f u(w) for
V1's gamma_B(w)).  Let f_0 be a base row with p*(f_0 - f) <= r_f/2 and let a window family (U1)-(U7) be given at f_0 with scales in [T, t_1].
Suppose the WINDOW CONDITIONS
   (W-a) c_fine <= c_late delta T/(n A_0),      (W-b) K_J c_tiny <= 1/4 and 2 K_J ||Y||_inf <= 1/2 (Lemma DC (3'); the s_1-dependent part of
         ||Y||_inf, <= Design-type x s_1 A_0/T, is covered by (LATE) after enlarging K_w),      (W-c) N_w is chosen with tail_W <= c_late delta T/A_0,
and let s_1 satisfy
   (VT')  64 rho eps <= delta s_1        and        (LATE)  s_1 <= s_late := c_late delta min{ T^3 gap_min/(n A_0 K_w)^2 , x_0 T/(n A_0 K_w) }.
Then the d-consistent engineered approximant f' of 3.2 (any N'' as in 3.2(iv)) is norm attaining, p*(f' - f_0) <= K_w Pi log(e/Pi) with
Pi <= K_w s_1, and for every piece i
   p*(f' + tau g'_i) <= 1 + (tau^2/2)(1 - delta)        for 0 < |tau| <= c_flat t_i,                                       (UE)
   p*(g'_i - rho g_i) <= K_w (K_w s_1 + c_fine + tail_W)/t_i.
(K_w is the window constant of Lemma UE-1; c_late is an f-constant; the conditions (W-a)-(W-c) do not involve s_1.)

## 3.5 Proof.
Step 0' (constants; order of choices f -> K_sharp -> eta_1 -> transfer data, r_f -> t_1, c_flat, c_late -> window -> N_w -> s_1 -> N'' ->
levers).  By (U1) and Lemma M2 every Gamma-quantity is <= 2: h^0(b^diamond) <= 2/q^0_0 <= 4/q_0, H_m(omega^diamond) <= 2/sigma^0_m <= 4/sigma_m.
Put K_sharp := 4 max(1/q_0, max_m 1/sigma_m) (1 + eta_0) + 2 and eta_1 := min(1/4, delta/(192 |I| K_sharp)); choose the transfer data of f in
every block with this eta_1 (lem:transferdata, gamma_m in (M_m/2, M_m)) and r_f := r_f(eta_1) (Lemma M2): at every row in B_f they have
e_y >= 1/2, iota <= 2 eta_1, ||D y|| <= K_y, |Y|/q_0 <= K_Y.  Let a_min := min_F |a_j|, gamma_0 := min_m (M_m - gamma_m), C_min := min_m C_m.
c_flat is the largest number <= 1/8 satisfying the following finitely many inequalities, in which every constant is an f-constant
(K_W := C_W (A_0 + A_2 + C_Delta), C_W an f-constant bounding the f'-block sizes per unit 1/t, see Step 3; K_A := 2(1 + ||U||) A_0 + 1):
 (c1) rho c_flat A_0 <= a_min/32          [no flip on F: |tau rho beta_j| <= rho c_flat t ||b||_inf <= a_min/32 <= |a'_j|/8];
 (c2) rho c_flat <= 1/8                    [no flip on E under (U3): |tau rho b_j| <= |a_0(j)|/8 <= |a'_j|/4];
 (c3) rho c_flat (A_2 + C_Delta + 1) <= 8  [no flip at pull coordinates, Step 3 (Base)];
 (c4) rho c_flat (A_2 + 2) <= min(M_min/2, 1/3), rho c_flat ||Phi||_2 A_2 /C_min <= 1/4, and 8 rho c_flat A_2 <= gamma_B   [block radius,
      kinds [1]-[3], Step 3 (Blocks); the last condition is the only one involving gamma_B: kind [2] needs |sigma omega(k)| <= 2 rho c_flat A_2 <=
      gap'(k)/2 with gap' >= gamma_B/2.  When gamma_B is window-dependent (V1: gamma_B(w) = min_m M_m u(w)/4) so is c_flat:
      c_flat(w) = min(c^f_flat, gamma_B(w)/(8 rho A_2)) >= c_f u(w), exactly as in V1's Theorem E'' / Lemma U'];
 (c5) K_W c_flat <= min(gamma_0/8, C_min/4), and 6 K_sharp c_flat^2 t_1^2 (2 + Lambda_max) <= gamma_min/2, 6 K_sharp c_flat^2 t_1^2 <= gamma_0/8,
      6 |I| K_sharp K_Y c_flat^2 t_1^2 <= 1;
 (c6) 6 |I| K_sharp K_Y K_A c_flat + (48 K_sharp K_W K_y c_flat + 36 K_sharp^2 K_y^2 c_flat^2)/(C_min/2) <= delta/16  [cubic and quartic
      error terms of Step 4: since |tau| <= c_flat t and K_A, K_W enter as K/t, each term is <= (const) c_flat tau^2];
 (c7) K' c_flat (1 + rho^2) <= delta/8, K' := an f-constant times (A_0 + A_2) bounding the relative errors (1 + K_H T_0), (1 + K_h T_0) per
      unit T_0/t (Lemma lem:block(d): 2|d sigma| M/C with |d(omega)| <= ||D omega||_2 <= A_2 ||Phi||_2/t + C_Delta; lem:base(b): 2|t| beta/nu with
      ||U^* beta|| <= ||U|| 2A_0/t).
t_1 := an f-constant so small that (c5)'s quadratic conditions hold (they contain c_flat^2 t_1^2) — t_1 is chosen after c_flat's
first-order conditions; c_late is an f-constant fixed in Steps 3-5 (each use is marked).  Put T_0(i) := c_flat t_i.

Step 1-2 (targets and exact decompositions).  As in thm:engineered, with g''_i, c_i, g'_i of 3.2(vi) and the three decompositions
f' + tau g'_i = (a' + tau B^diamond) + sum_m R_m^*(w'_m + tau Omega^diamond_m), B^diamond := rho(beta^diamond - c_i a').  By d-consistency (Lemma UE-1(c)),
d'_m(omega^diamond) = d_m(omega^diamond) = d^diamond_m, hence kappa^diamond_m = rho (d'_m - d_m)(omega^diamond - omega^theta) = 0 and
      Omega^diamond_m = rho(omega^diamond_m - d'_m(omega^diamond_m) w'_m) + rho(d^diamond_m - d^theta_m)(w'_m - w^0_m)   (diamond = +-),
Omega^theta_m = rho(omega^theta_m - d'_m(omega^theta_m) w'_m).  The identities of Step 2 use only the two representations at f_0 (valid for
violated pairs, U3 Lemma VT (1)).  The anchors (V^an = w^0 if Delta_m >= 0, = y_A of lem:anchor if Delta_m < 0) and the remainder Z are as
there.  ||W^natural_m - w'_m||_inf + ||D_m(W^natural_m - w'_m)||_2 <= (K_W/t_i)|tau|: |omega^diamond(k)| <= A_2/t (kinds [1]-[3]; kind [1]:
2gap/t <= 2/t), ||D omega||_2 <= A_2 ||Phi||_2/t, |d^diamond| <= ||D omega||_2/C... <= K/t, ||V^an - w'||_inf <= 3, |Delta| <= C_Delta.

Step 3 (first-order terms and excesses).
 Blocks.  lin'_m(W^natural_m) = r_m <V^an_m - w'_m, R_m x'>/sigma'_m (the kappa-term is absent), r_m := (1/2)|tau| rho |Delta_m| <= |tau| C_Delta.
 By lem:approxfacts(E5)/lem:anchor, |<V^an - w', R x'>| <= c'(Bx_m + S_m) (for V^an = w^0: = c' Bx_m; for y_A: proof of thm:engineered Step 3,
 with |(R x')(k)| <= lambda_k c').  By Lemma UE-1(d), (e) and the choice of s_1:
      Bx_m + S_m <= K_w Pi^2 log(e/Pi) + 4 Pi_X c_fine + 4 C_lev W_lev r^2 + 2 t(N'') + 4m(C_S (K_w Pi)^2 + s_1^2 T^4) <= c_late delta s_1,
 using Pi <= K_w s_1 (Lemma UE-1(a), 3.2(iii)-(iv)), (LATE) (K_w^3 s_1 log(e/s_1) <= c' delta), (W-a) (Pi_X c_fine <= (4 rho mu_1 n A_0/(T nu_0))
 s_1 c_fine <= c delta s_1), and 3.2(iv).  Hence |lin'_m| <= |tau| C_Delta (2/sigma_m) c_late delta s_1 <= (delta/(64|I|)) |tau| s_1 for c_late
 small (f-constant).
 Excess: write W_0 - r_m w' = (1 - r_m)(w' + t'(omega^diamond - d'(omega^diamond) w')), t' := tau rho/(1 - r_m) (kappa = 0).  The block radius at f'
 for sigma := t', |sigma| <= 2 rho c_flat t_i: for k of kind [1], |sigma omega(k)| <= 4 rho c_flat gap^0(k) <= gap'(k)/2 (gap' >= gap^0/2,
 Lemma UE-1(c), and (c4)); kind [2] likewise with gap' >= gamma_B/2 and |omega| <= A_2/t; kind [3]: with vs := sgn w'(k) = sgn w^0(k), the
 outward part satisfies vs sigma omega(k) <= 1.5 |sigma| gap^0(k)/t <= 3 rho c_flat gap'(k)... so vs W(k) <= (1 - d sigma)(M' - gap') + gap'/2 <=
 (1 - d sigma) M' (|d sigma| <= 1/2 by (c4)), and -vs W(k) <= |sigma omega(k)| <= 2 rho c_flat A_2 <= (1 - d sigma) M' (c4): the INWARD bound of
 Z3 Lemma 5.1.  So ||W(sigma)||_inf = (1 - d' sigma) M' (lem:block(c), whose proof uses only these coordinatewise bounds), and lem:block(d)
 at f' gives N_m(w' + sigma(omega - d' w')) <= 1 + (sigma^2/2) H'_m(omega)(1 + 2|d' sigma| M'/C').  For diamond = theta, |tau| <= s_1 and the
 radius condition |s_1 rho omega^theta(k)| <= gap'(k)/2 holds by (LATE) (s_1 <= T gap_min/(4 rho A_2)).  Therefore, as in thm:engineered,
      G'_m(W^natural_m) <= hat G_m := (rho^2 tau^2/2) H'_m(omega^diamond)(1 + K' T_0/t_i) + r_m g_m,  g_m := N(V^an) - <V^an, R x'>/sigma' <= K(Bx_m + S_m),
 and H'_m(omega) = (C^0_m/C'_m) H_m(omega) (Lemma UE-1(c)).
 Base.  By lem:bookkeeping(b) at f', G'_b(A_tau) = Exc'(tau B^diamond + Z) + nu' Psi'(U^*(tau B^diamond + Z)/nu').  Claim (*) of U3 Lemma VT holds at f'
 with the additional coordinates of f': (1) masses on W: as in VT (theta: |tau rho b^theta_j| <= s_1 rho |b^theta_j| = m_j/4 <= |a'_j|/2; +-: cost
 <= 2 rho|tau| viol(j)); (2) F: no flip by (c1) and |tau rho c_i| <= 1/2 (Lemma UE-1(g) and (LATE)); E: by (U3) and (c2) (contact-like data
 never flip on their sides, theta-masses protect the theta piece; the other alternative gives |tau rho b_j| <= |a'_j|/4); (3) lever coordinates:
 (Z-free/Z-con) coordinates carry zero data (Lemma LV(b),(c)), so their summands vanish whether they are free, contacts or banks at f';
 (TU) banks: contact-like data (sign eps_l = z = sgn a'_j); (TU) pulls: |tau rho beta^diamond_j| <= rho c_flat t_i (|gamma_{i,l}| v_l(j) + later) <=
 rho c_flat (A_2 + C_Delta + 1) lambda_l v_l(j) <= 8 lambda_l v_l(j) = mu_p/3 (c3; "later" = carriers > L meeting j through targets, whose
 coefficients are <= C_Delta lambda and whose total weight is <= 2^{-2j} c_l delta_l, negligible against lambda_l v_l(j)/t_i once r <= T/K_w), so
 a'_j + tau B_j keeps the sign of a'_j: summand 0; (S-mass) p_0: t|b| <= m_0/... as in (U3); (4) contacts in (N_w, N''], free coordinates,
 contacts beyond N'': exactly as in VT.  Hence
      Exc'(tau B^diamond) <= (1/2) rho |tau| V_{>N''} + 2 rho |tau| eps  (diamond = +-),   Exc'(tau B^theta) = 0  (0 < |tau| <= s_1),
 and with ||Z||_1 <= |tau| C_Delta sum_{A_m} lambda_k(|w' - w^0| + (C' - C)_+) <= |tau| C_Delta S_m and lem:base,
      hat G_b := (rho^2 tau^2/2) h'(beta^diamond)(1 + K' T_0/t_i) + (1/2) rho |tau| V_{>N''} + 2 rho|tau| eps + 2|tau| C_Delta sum_m S_m.
 For |tau| > s_1: (1/2) rho V_{>N''} <= delta s_1/128 (3.2(iv)), 2 rho eps <= delta s_1/32 (VT'), 2 C_Delta sum S_m <= delta s_1/128 (c_late):
 the three linear terms are <= (delta/16)|tau| s_1 <= delta tau^2/16.  So hat G_b, hat G_m <= K_sharp tau^2 for |tau| <= T_0(i)
 (H' <= 2H <= 4/sigma, h' <= 2h^0 + small by Lemma UE-1(f)).

Step 4 (rebalancing).  Proposition prop:rebalancing at f' with h := tau g'_i (h(x') = 0 since g'_i(xhat') = 0), the transfer vectors y' of
f' (Lemma M2), eps_m := (lin'_m + hat G_m - hat Gamma)/e'_{y,m}: |eps_m| <= 2(|lin'_m| + hat G_m + hat Gamma) <= 6 K_sharp tau^2 (|tau| > s_1;
|lin'| <= tau^2), <= 4 K_sharp tau^2 (theta).  (R1) via lem:TV with eta := (K_W/t_i)|tau| <= K_W c_flat: conditions (c5).  |lambda| <= 6|I|K_sharp
K_Y tau^2 <= 1 by (c5).  The error E <= 12 |I| K_sharp eta_1 tau^2 + 6|I| K_sharp K_Y |tau|^3 K_A/t_i + (48 K_sharp K_W K_y |tau|^3/t_i +
36 K_sharp^2 K_y^2 tau^4)/(C_min/2) <= (delta/16 + delta/16) tau^2 by eta_1 and (c6) (|tau| <= c_flat t_i; K_A/t_i bounds (|q*(A_tau) - 1| +
q*(A_tau - a'))/|tau|: q*(B^diamond) <= 2(1+||U||) rho A_0/t_i + |c_i|, ||Z||_1/|tau| <= C_Delta S_m <= 1).

Step 5 (levels).  hat Gamma = c' hat G_b + sum_m sigma'_m hat G_m <= (rho^2 tau^2/2)(c' h'(beta^diamond) + sum_m sigma'_m H'_m(omega^diamond))(1 + K' c_flat)
+ (linear terms).  By Lemma UE-1(c), (f): the bracket is <= Gamma^{(0)}_diamond + K_f(A_0^2 Pi/T^2 + A_0 tail_W/T + Pi) <= Gamma^{(0)}_diamond + delta/8
(LATE, W-c; c_late), and Gamma^{(0)}_theta <= max(Gamma^{(0)}_+, Gamma^{(0)}_-) <= 1 + eta_0/2 by convexity (violated pairs included: Gamma_w is
convex in the pair).  The linear terms (base: Step 3; blocks: sum sigma' r_m g_m <= |tau| C_Delta K sum (Bx + S) <= (delta/32) tau^2 for |tau| > s_1)
are absent for diamond = theta.  With (c7), for 0 < |tau| <= T_0(i):
   p*(f' + tau g'_i) <= 1 + hat Gamma + E <= 1 + (tau^2/2)(rho^2 (1 + eta_0/2) + delta/8 + delta/8 + delta/8 + delta/4 + delta/8) <= 1 + (tau^2/2)(1 - delta),
since rho^2(1 + eta_0/2) = 1 - 2 delta.  The remaining assertions are Lemma UE-1(a), (g).  QED

## 3.6 Remarks.
 (a) What changed relative to thm:engineered: (i) the first-order d-mismatch is ZERO (exact d-consistency, Lemma DC) instead of
     K(omega) s_1, so K_sharp is an f-constant (no dependence on the window or on t); (ii) every "late stage" assertion is replaced by an
     explicit bound in terms of the perturbation size Pi (Lemma UE-1), which is linear in s_1 with a WINDOW constant; (iii) the scrambling
     condition is used in the explicit form (U5); (iv) violations are tolerated as in Lemma VT, now uniformly in the piece (the cost
     2 rho|tau| eps does not depend on t); (v) the lever coordinates are protected (zero data, contact-like data, or pull masses dominating
     c_flat t |data|).
 (b) The only interplay between s_1 and the window is the interval [64 rho eps/delta, s_late]: (VT') bounds s_1 from below by the
     violation mass, (LATE) from above by window quantities.  This is exactly U3's (S2c) "threshold comparison", now with an explicit s_late.
 (c) T_0 >= c_flat t_i with c_flat an f-constant: the per-piece radius scales with the piece, as (S2a) requires.  U3's original scaling check
     was correct for every term EXCEPT the d-mismatch, which (Proposition J) is O(sqrt|Omega| ||X||) for valid data (not O(s_1/t^2)), still
     non-uniform along windows, and which d-consistency removes exactly.
