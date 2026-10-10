# K2 part 2 (Round 11): Step A (Sys-A) at arbitrary base support -- (O-c)(iii) and K1's (S)/(U) configurations

Setting of part 1.  SYS-A = K1 2.4: Step 4 of X1's Proposition KN^tr (inside Q1 Lemma CM^tr) in RATIO form with floating block scalars:
      F~_l := val_l - rt_l kappa_{m(l)}  (l in Lambda_A),   val_l := eps_l u_l(xhat),
rt_l the target ratio (r''_l eps_l for active l; 0 for KN-1 holds H_T; the current ratio for Hold; the pushed ratio for D), kappa_m = U1's block
scalar kappa_m = A_m + theta_m Phi_{P_m}^2 + S_m/theta_m (U1 Lemma 1.3).  The input row is f_1 := the deep-raised row after Step 0 AND the
preparation (P) of 1.6 (P before the Lojasiewicz step; its perturbation <= b is absorbed by the doubled b in (D1), part 3).  x := x_A = C Design(L)
eta' is the correction scale: |F~(f_1)|_inf <= x (Lojasiewicz displacement eta', KN-1 values <= 4 c_{L+1}^2, D-pushes eta').
Resources of Sys-A: K1 2.0 (P1)-(P5) for the carriers of Lambda_A, peak resources s_c, and (new) one elementary resource at each design-depth
coordinate s <= D(L) with s in U_L or s a thick coordinate of F_1 (types of 1.6(d) at f_1: TS thick support (anchors included), S_theta
(banked/raised, modulus theta_0), FR, ZD, and DC := the designated near TU-bank coordinates of data-carrying carriers, which are contacts at f_1;
thin s <= D(L) in F_1 \ U_L carry no resource and contribute at most kappa b each to the identity).  At the scale x >> theta_0 Design: TS, FR, ZD and
TU levers WITH a pull are TWO-SIDED; S_theta (raise only, beyond theta_0) and DC (bank only) and TU banks WITHOUT a pull are ONE-SIDED, with
a fixed allowed direction.

## 2.1 Lemma K2.8 (the combination of Sys-A).  PROVED.
For y in R^{Lambda_A} put zeta_m := sum_{l in m} y_l rt_l and
      Psi^A_y := sum_l y_l eps_l u_l - sum_m zeta_m K_m,     K_m := sum_k (d kappa_m/d zeta_m(k)) lambda_k u_k     (derivatives at f_1).
Then (a) Psi^A_y(xhat_1) = y^T F~(f_1) =: phi_y, |phi_y| <= x ||y||_1;  (b) for every elementary move delta, y^T c_A(delta) = l_delta(Psi^A_y) +
O(|delta|^2); (c) <U^*Psi^A_y, e_1> = y^T g~ with K1's g~ := g - (rt_l G_{m(l)})_l.
Proof.  kappa_m is a function of the block vector zeta_m = (lambda_k u_k(xhat))_k, positively homogeneous of degree 1 and C^1 while the peak set is
fixed (A_m, theta_m are 1-homogeneous -- the clamp/threshold equations (E1), (E2) of U1 Lemma 1.2 are invariant under zeta -> c zeta, A -> cA,
theta -> c theta -- and S_m = sum nu_k^2 Phi_k^2 is 2-homogeneous; U1 Lemma 1.4 gives the derivatives); Euler's identity gives kappa_m(f_1) =
K_m(xhat_1), whence (a); (b) is the chain rule with dkappa_m(delta) = l_delta(K_m); (c) is (b) for the common mode (K1 2.4: G_m = <U^*K_m, e_1>
up to O(X)).  QED

## 2.2 Lemma K2.9 (positive spanning; realization of Step A).  PROVED.
Let G be the set of normalized columns of Sys-A: +-c for two-sided resources, c (allowed direction) for one-sided ones, and put
      eps_PS := min_{||y||_2 = 1} max_{g in G} (- y^T g)            (positive-spanning modulus).
(a) If eps_PS >= eps > 0, every b in R^{Lambda_A} is a nonnegative combination of G with total weight <= ||b||_2/eps.
(b) If eps_PS >= eps with eps >= Design(L)^{-C_1}, Step A is realized: there is a companion f^(1a) with all conclusions of KN^tr / K1 Lemma
    K1.6(A) (exact ratios r'' on Z_kappa, exact KN-1 zeros, Puiseux protection, robust statuses), cost <= C_f Design^C eta' log(1/eta')/eps.
Proof.  (a) If some b with ||b|| < eps were outside conv(G), a separating y (unit) would give y^T b < min_g y^T g <= -eps, impossible since
|y^T b| < eps.  So B(0, eps) is inside conv(G) and b = (||b||/eps) sum t_g g with sum t_g = 1.  (b) Let G also denote the matrix of generators and
S(b) := argmin{ ||s||_2 : G s = b, s >= 0 } (unique; by (a) feasible for every b, with ||S(b)||_1 <= ||b||_2/eps).  S is continuous: the feasible
polyhedra P(b) depend Lipschitz-continuously on b in the Hausdorff metric on bounded sets (Hoffman's bound), and the nearest point to 0 of a
Hausdorff-continuous family of closed convex sets is continuous.  The nonlinear system is F~(f_1) + G t + Rem(t) = 0, t >= 0 (one parameter per
generator, two-sided resources split into +- generators), |Rem(t)| <= C_2 ||t||^2 with C_2 a design constant (K2.4, K1 2.1).  The map
T(t) := S(-F~(f_1) - Rem(t)) is continuous and maps K := {t >= 0 : ||t||_1 <= R}, R := 2x/eps, into itself as soon as C_2 R^2 <= x, i.e.
4 C_2 x <= eps^2 -- true since x = C Design eta' and eps >= Design^{-C_1}.  By Brouwer, T has a fixed point t*, which solves the system with
t* >= 0.  Statuses, Puiseux margin and costs as in K1 Lemma K1.6(A) (they use only exactness of the realized ratios and the size R of the moves).
(This also makes K1's "ratio trick" (K1 2.7 Remark (1), SKETCH there) rigorous whenever the generators positively span.)  QED

## 2.3 Proposition K2.10 (structure of positive-spanning failures).  PROVED.
Suppose a unit y has max_{g in G}(-y^T g) <= eps (a near-certificate), with eps <= eps_* := c_f Design(L)^{-C}.  Put gamma := <U^*Psi^A_y, e_1>.
 (a) [identity bound]  gamma <= phi_y + D(L) eps/eff + ||Psi^A_y 1_{(D(L),inf)}||_1 <= C x + C D(L) Design eps + gamma_tail, where eff >=
     Design^{-1} is the least normalized efficiency of a design-depth resource and gamma_tail <= |gamma| /16 + C c_{L+1} by the choice of D(L).
     Hence gamma <= (16/15)(C x + C Design^2 eps + C c_{L+1}): a near-certificate never has a robust POSITIVE common-mode coefficient.
 (b) [shape]  y_l = gamma h_l + O(eps') on carriers with a two-sided S-mass lever (P4), y_l = O(eps') on carriers with a private two-sided lever
     ((P1), (P3), TU with pull), and y_l >= -O(eps') (in the orientation of the allowed direction) on carriers whose only lever is one-sided
     (K1's (U)); zeta_m = O(eps') in every block with a two-sided peak resource (y^T(peak column) = -(1 - X_m) lambda_c zeta_m - h_c gamma).
 (c) [dichotomy]  Either  (A*) gamma <= -gamma_0 with gamma_0 := 1/(4 ||h||_2) (a robustly NEGATIVE common mode: y is, up to O(eps') and a
     nonnegative part on (U)-carriers, a negative multiple of h), or  (U*) |gamma| <= gamma_0 and y is concentrated on (U)-carriers:
     ||y 1_{(U)}||_2 >= 1/2, y >= -O(eps') there, and zeta_m = O(eps') in every block with a two-sided peak resource.
Proof.  (a) In Lemma K2.2 at f_1 with u := Psi^A_y (coarse part; fine part <= C c_{L+1}) and depth D(L): at every design-depth coordinate the
contribution c_s := D_u(s) sgn(a_s) (s in F_1) or u(s) z_s (s notin F_1) equals, by K2.4 and K2.8(b), the y-component of the resource at s divided
by its efficiency (for one-sided resources in their allowed direction: a bank adds mass of sign z_s, so its y-component is (mu_s^2/nu) u(s) z_s;
a raise of |a_s|: (mu_s^2/nu) D_u(s) sgn(a_s)).  Two-sided: |c_s| <= eps/eff; one-sided: c_s >= -eps/eff.  Hence sum_{s <= D} c_s >= -D eps/eff and
     phi_y = u(xhat_1) = kappa_u (1 - alpha(D)) + sum_{s <= D} c_s + (deep terms)   >=   kappa_u (1 - alpha(D)) - D eps/eff - tail_u(D).
If gamma = kappa_u nu_1 > 0, kappa_u(1 - alpha(D)) >= gamma (1 - alpha(D) >= nu_1), and (a) follows with K2.8(a).  (b) As Step 1 of Theorem K2.6
(the S-mass column is e_l - g~ h_l in Sys-A, K1 2.5(b); private columns e_l + O(X + Design^2 x), K1 2.1).  (c) If gamma >= -gamma_0 then by (a)
|gamma| <= gamma_0, so by (b) the components of y on two-sided carriers are <= gamma_0 ||h|| + O(eps') <= 1/4 + O(eps') in l_2, and the rest of the unit
vector sits on (U)-carriers.  QED
Consequences (PROVED).
 (i) Degenerate (S)-directions whose needed correction points DOWN are realizable: if y ~ gamma h with gamma > 0 is the degenerate direction of
     the square part (K1 2.5(b1)) and phi_y >= 0, then -F~ lies in the cone (the near-certificates are (A*)-type, i.e. -y, and -y^T(-F~) = phi_y >= 0
     is not an obstruction); by (a), robust POSITIVE-gamma obstructions do not exist at all.
 (i') Quantitative form of (i): in that case the identity gives sum_{s <= D} c_s <= phi_y - gamma + tail <= -gamma/2, so some design-depth
     resource s has c_s <= -gamma/(2 D(L)): a one-sided resource pushing Psi DOWN with efficiency >= eff gamma/(2D(L)); together with the two-sided
     columns (which span the complement of y robustly, K1 2.5(b)) it represents -F~(f_1) with weight <= Design^C x, so Lemma K2.9(b) applies.
 (ii) KN-1 holds (Q2 4.4(iv)): a KN-1-held carrier is zero-data, so every off-support coordinate of its signature set is ZD (two-sided); if all
     its design-depth coordinates are thick it is an S-mass carrier and enters only through gamma h; its own correction is <= 4 c_{L+1}^2 <<
     theta_0 eff, a scale at which S_theta coordinates are two-sided as well.  Hence a degenerate direction in which KN-1 holds take part is
     realizable unless it is of type (A*) below; "KN-1 holds in a degenerate raw direction" is not a separate residual.
 (iii) Ratio trick (K1 2.7 Remark (1), made rigorous): let m be a block with a two-sided peak resource, on whose two-sided carriers y = O(eps')
     (e.g. no S-mass carrier with nonzero target in m), and in which every (U)-carrier has |rt_l| >= u(w) with the same sign of rt_l in the
     orientation of its allowed direction.  Then y = O(eps'/u) on the (U)-carriers of m: zeta_m = sum_{(U) in m} y_l rt_l + O(eps') = O(eps') with
     y_l >= -O(eps') and all rt_l of one sign.  So blocks of this kind never carry a (U*)-certificate.

## 2.4 The residual of Step A (precise).  OPEN.
A main stage L (clean w, class a) is A-REGULAR if eps_PS(Sys-A) >= Design(L)^{-C_1}, or, more generally, if -F~(f_1) lies in the cone of G with
weight <= Design^{C} x (Lemma K2.9 applies verbatim).  If L is not A-regular, Proposition K2.10 gives a near-certificate of one of the types:
 (A*) [wrong-sign degenerate direction]  a degenerate support-swallowed direction (K1's (S): near coordinates thick, tiny spreads, Sherman-Morrison
      degenerate 1 - h^T g~ ~ 0, zeta_m ~ 0 in blocks with two-sided peak resources) whose needed correction points UP (phi_y < 0 for y ~ +h), while
      every design-depth resource of Psi^A_y is one-sided pushing DOWN (banks at anti-aligned data-carrying contacts, raises at S_theta
      coordinates) or has zero effect; equivalently (by the identity) the support-swallowed carriers l with nonzero data have switching sign
      OPPOSITE to their support sign on the near set, and their signature sets carry less than x of anti-aligned off-support mass beyond D(L)
      (deep pulls at anti-aligned contacts are UP-moves: if sum_{j in S_l \ F_1, j > D(L), z_j = eps_l} v_l(j) >= C Design x for one such l, the many-pull
      version of V1 Lemma TU realizes the UP correction and the stage is A-regular);
 (U*) [one-sided carriers outside the ratio trick]  data-carrying carriers without thick near coordinate and without pullable far coordinate
      (K1's (U)), in a block that is NOT of the kind of Consequence (iii) (target ratios of both orientations, or a tiny target ratio, or S-mass
      carriers with nonzero targets in the block, or no two-sided peak resource), and a needed correction outside the cone (some such carrier
      needs a DOWN correction that no combination of UP-moves and kappa-rescalings produces).
Both are sign (cone) conditions, not rank conditions; (A*) additionally requires the exact-limit structure of U2 Lemma ND / Q2 Lemma 4.3 on the
near coordinates.  NOT shown: that (A*) or (U*) at ALL large stages is impossible, or that rows with this property have a non-recoverable mate.
Remark (why the remedy of part 1 does not apply here).  Sys-A's targets are the ratios r'' (fixed by the Lojasiewicz/Puiseux step), not the
values of the row; in a square system the final lever positions are FORCED by the targets, independently of any offset placed in the input row
(the same mechanism as K1 2.2).  Preparation offsets therefore make S_theta coordinates two-sided only at scales <= theta_0 eff (enough for KN-1
holds, not for Lojasiewicz displacements of size eta').  For Sys-DC the targets are the values of the prepared row itself, so offsets work.
