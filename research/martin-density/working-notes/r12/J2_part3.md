# J2 part 3 (Round 12): direct solvability of the joint push problem (H1*) -- threshold raisers; sign structure; what a direct proof meets

Setting of J2_part1.md.  This part is NOT needed for Theorem J2.1 (which removes (WP) altogether); it describes when the pre-pushes Pi_0 of
(H2^flat) are available, and why a direct proof of (H1*) at every row would meet the same sign obstruction as Step A.

## 3.1 PROPOSITION J2.4 (joint pushes with private resources and threshold raisers).  PROVED (mod the refereed lever lemmas cited).
At a main stage L >= l_f (clean w, class a), (H1*) holds -- with sizes <= 3 b theta Phi_k/m for own pushes and <= Design(L)^C b/u^2 in VALUE
units (ratio displacement <= Design(L)^C b/u, J2_part1 1.2(a)) for threshold raisers -- if for every (T)-block m with W(m) != {} one of:
 (i)  [own pushes] every k in W(m) has a PRIVATE push resource: (P1) if k is zero-data (e_k = Delta'_m, J2_part1 1.3); a near coordinate of k
      off F or thin when eps_k = -vs_k (a bank/raise there raises eps_k val_k, i.e. lowers |u_k(xhat)|, K1 2.1(b), Lemma K1.3(S)); a pullable far
      coordinate j of k with v_k(j) in [3 b theta Phi_k/m, x'_max] when eps_k = vs_k (the pull lowers eps_k val_k by >= v_k(j)/2, K1 2.1(b)); or (P3)
      on k (two-sided, K1 2.1(c));
 (ii) [threshold raiser] some robust peak p of m (rho_p >= 1 + u) has a private resource RAISING |u_p(xhat)|: a near coordinate off F or thin
      when eps_p = vs_p, i.e. Delta'_m < 0 (bank/raise), a pullable far coordinate when eps_p = -vs_p, i.e. Delta'_m > 0 (pull), or (P3); or some
      active strict non-peak l of m with rho_l >= u has a private resource LOWERING |u_l(xhat)| (bank if eps_l = -vs_l, pull if eps_l = vs_l, (P3));
or a mixture: some k in W(m) by (i), all others by one move of type (ii).
Proof.  First-order actions.  A private move acts at first order only on its own carrier's value (K1 2.1(a)-(c): banks/raises at a near
coordinate s of S_k beyond s_max(L) change u_j(xhat) for coarse j != k only through e, at second order (diagonal base, V1 Lemma B: <= C
Design(L)^2 (size)^2); pulls likewise; (P3) is private).  By Lemma J2.0, an own push lowers rho_k (consequence (b)), and a threshold raiser
raises theta_m, which multiplies every relative position of block m by the same factor theta_m/theta'_m < 1 (consequence (a)), and does not
act on other blocks at first order.  Hence the first-order action on the vector (log rho_k)_{k in W} is DIAGONAL for own pushes and a NONNEGATIVE
common decrease on all of W(m) for a threshold raiser: the Step-0 inequality system is solved by moves of the stated sizes with overshoot
(target rho_k <= 1 - 2b, resp. theta_m raised by the relative amount 4b): the second-order cross effects are <= C Design^2 (Design^C b/u^2)^2 << b
(b <= T^4 << u^C/Design^C).  No Sherman-Morrison denominator 1 - h_W^T g_W arises (K2-ref W-1): no common-mode ((P4)/(P5)) column is used.
Admissibility and side effects: banks at near contacts of the data sign and raises of thin coordinates of the data sign are the (P2)/(K2 4.1)
moves (data aligned); pulls are K1's (P2) pulls (anti-sign data dominated by the pull mass, K1-ref R-6 depth window); robust objects move by
<= Design^C b/u^2 << u (b << u^3); every rate object moves by <= Design^C b/u (peak VALUES do not enter the rate objects, Q1-refb E7; the ratios
move by the common factor of kappa_m, J2_part1 1.2(a)), inside R-8(ii)'s enlarged (D1).  Costs <= C_f Design^C b log(1/b)/u^2 = o(u^2 T^2).  QED
Remark.  The size bound "Design^C b/u" in K2-ref E's formulation of (H1*) must be read in rate-object (ratio) units for threshold raisers; in
value units they need Design^C b/u^2 (because a >= u Phi_p^2 is only robust, J2_part1 1.2(a)).

## 3.2 LEMMA J2.5 (which blocks have a bank-type threshold raiser).  PROVED.
(a) If Delta'_m < 0, every coarse peak p of block m has eps_p = vs_p (J2_part1 1.3; robust peaks: eps_p = -sgn(Delta'_m) vs_p).  Hence (ii)
    holds as soon as ONE robust peak of m has a near coordinate off F or thin (off-F near coordinates of a nonzero-data carrier are contacts of
    its data sign, K1 2.1(b); thin ones carry its data sign, Lemma K1.3(S)), or a robust-spread thick pair ((P3)).  So in a (T)-block with
    Delta'_m < 0, the direct push fails only if EVERY robust peak of m is support-swallowed of type (S) (six thick near coordinates with tiny
    spreads) AND some weak peak of m has neither a pullable far coordinate nor (P3) AND no active strict non-peak gives (ii).
(b) If Delta'_m > 0, robust peaks have eps_p = -vs_p: their banks LOWER theta, their pulls raise it.  A weak peak k has eps_k = -vs_k iff
    e_k < Delta'_m; then its own bank pushes it.  So in a (T)-block with Delta'_m > 0 the direct push fails only if some weak peak lacks its own
    push (no off-F/thin near coordinate when e_k < Delta'_m, no pullable far coordinate when e_k > Delta'_m, no (P3)), every robust peak lacks a
    pullable far coordinate and (P3), and no active strict non-peak gives (ii).
(c) Consequently every failure of Proposition J2.4 involves only carriers of K1's types (S), (U), (M) (K1-ref R-10): the residual of the direct
    route is a sub-configuration of the non-lever-regular class, i.e. of the same kind as the Step-A residual (A*)/(U*).
Proof.  (a), (b): the sign formulas of J2_part1 1.3 and the case analysis of Proposition J2.4; (c): a carrier without (P1)-(P3) and without
the relevant bank/pull is (S), (U) or (M) by K1-ref R-10.  QED

## 3.3 What a direct proof of (H1*) at every row meets (SKETCH)
If the Step-0 inequality system is not A-regular, quantitative Farkas (K2.9(b)) gives weights y >= 0 on W, not all 0, such that no admissible
move decreases sum_k y_k log rho_k at first order (up to eps).  By Lemma J2.0 this functional is l_delta(Psi^0_y) for the carrier combination
      Psi^0_y := sum_m sum_{j in block m} c_j u_j,    c_j := vs_j [ y_j/|u_j(xhat)| 1_{j in W} - Y_m (d theta_m/d|zeta_j|) lambda_j/theta_m ],   Y_m := sum_{W(m)} y_k,
and Psi^0_y(xhat) = 0 by the 1-homogeneity of theta (Lemma J2.0: sum_j (d theta/d|zeta_j|)|zeta_j| = theta).  This is the exact analogue of K2's
left combinations (Psi_y(zhat_0) = 0, K2 Lemma K2.5(a)) and of K2.8(a); the identity (2.1) and the resource dichotomy K2.3 then give: two-sided
design-depth coordinates force c_s(Psi^0_y) ~ 0, one-sided ones c_s >= -eps, hence a nonpositive common mode, and a robustly negative common
mode with thick design-depth support proportional to Psi^0_y -- the structure of Theorem K2.16, now for Step 0.  (Not written line by line:
SKETCH.)  So a direct proof of (H1*) at every row is AS HARD as Step A's (A*)/(U*) problem; Theorem J2.1 avoids it by merging the two cone
conditions into one (Step A's), at no loss (Corollary J2.2).

## 3.4 REMARK J2.6 (orientation of weak peaks inside Step A; information for the Step-A analysis).  PROVED.
Call vs_l eps_l the ORIENTATION of a tuned carrier (it is the sign "rt_l eps_l sigma_l" of K2.17(g) for SLD signatures, where the S_th near
coordinates of a data-carrying carrier have the data sign sigma_l = eps_l).  By 1.3, an active weak peak has orientation sgn(e_k - Delta'_m):
it is +1 whenever Delta'_m < 0.  By the coupling row (X3)/kappa of the class cone, sum_{l in Omega_a(m)} r_l gamma_l = Delta'_m, i.e.
sum_l |r_l| |gamma_l| (vs_l eps_l) = Delta'_m; hence a block with Delta'_m < 0 always contains an active carrier of orientation -1, and a block with
Delta'_m > 0 one of orientation +1.  Consequently, in a (T)-block with Delta'_m < 0 an active weak peak whose only resource is one-sided (kind (iv)
of K2.16) has orientation +1 while some other active carrier has orientation -1: if that carrier is ALSO of kind (iv), the block violates
K2.17(g)'s one-sign condition and the kappa/threshold lever cannot serve both (a weak peak needs kappa_m to rise by the factor |r_k|/|r''_k|,
the other carrier needs it not to rise above |r_l|/|r''_l|).  This is the precise way in which weak peaks can take part in a (U*)-certificate
of the merged Step A; it is a target-placement condition (J1 Lemma J1.2), not a push condition.
