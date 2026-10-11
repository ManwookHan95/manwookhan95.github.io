# J1 part 1: Step A in target form; the deviation identity; normal form and global rigidity of the obstruction

Setting and notation: r11/K2_notes.md Sections 1, 5 (with K2-ref precisions K-1..K-8) and r11/K1_notes.md 2.0-2.7 (with K1-ref
R-6..R-14).  Design T_fin^{K2}, N >= 1, f in S_{p_N*} with base support F arbitrary, g in C(f), rho in (0,1), a main stage L >= l_f,
a clean sub-window w, a class a.  b = b(w), u = u(w), T = T_lo(w), D = D(L), x = Step-A scale, W = Design^{C_A} u^{-3} max(x, ||b||)
(K-7), rho_0 = C_2 W^2.  The input row of Step A is R_1 := f_1 + Pi (after the deep raise, Step 0, the preparation (P) and the
pre-placements Pi), with forced data (a, z, zhat, e, nu), q*(a) = ||a||_1 + nu = 1, diagonal base U k_s = mu_s e_s.
Rows: l in Lambda_A, Ft_l := val_l - rt_l kappa_{m(l)}, val_l := eps_l u_l(zhat).  Generators: two-sided G_2, one-sided G_1
(raises at S_th coordinates carrying data).  A near-certificate of size eps: unit y with y^T g >= -eps for all g in G (for g in G_2
both g and -g are generators).  phi_y := y^T Ft(R_1).  zeta_m := sum_{l in m} y_l rt_l,  Psi := Psi^A_y := sum_l y_l eps_l u_l -
sum_m zeta_m K_m (K2.8).  Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Lemma J1.1 (deviation identity).  PROVED.
For u in l_1 put kappa_u := <U^*u, e>/nu and Dev_u := u - kappa_u a (an element of l_1).  Then
  (a) <U^* Dev_u, e> = 0;
  (b) u(zhat) = kappa_u + Dev_u(z);
  (c) the first-order actions of K2.4 are, for every u: mass change dm at s in F: (mu_s^2/nu) Dev_u(s) dm; bank of mass dm z_s at a
      contact s notin F: (mu_s^2/nu) Dev_u(s) z_s dm; change dz of z_s (s notin F): Dev_u(s) dz.
Proof.  (a) <U^*Dev_u, e> = kappa_u nu - kappa_u <U^*a, e> = kappa_u nu - kappa_u nu = 0.  (b) a(zhat) = a(z) + <U^*a, e> = ||a||_1 + nu = 1
(z_s = sgn a_s on F), so u(zhat) = kappa_u a(zhat) + Dev_u(zhat) = kappa_u + Dev_u(z) + <U^*Dev_u, e> = kappa_u + Dev_u(z) by (a).
(c) K2.4 with D_u(s) = u(s) - kappa_u a_s = Dev_u(s) for s in F and Dev_u(s) = u(s) for s notin F (a_s = 0).  QED
[This is K2.2 written without the depth split; it shows that ALL generator actions on y^T Ft see Psi only through Dev_Psi.]

## 1.2 Lemma J1.2 (target-displacement form).  PROVED.
Let rc_l := val_l(R_1)/kappa_{m(l)}(R_1) (current eps-oriented ratio; kappa_m > 0).  Then Ft_l(R_1) = kappa_m (rc_l - rt_l) and
      phi_y = sum_m kappa_m sum_{l in m} y_l (rc_l - rt_l) = Psi(zhat_1)  (Euler, K2.8(a)).
In particular phi_y = 0 whenever every target equals the current ratio, and for any two target vectors rt, rt' (same row R_1, same
generators) phi_y(rt') - phi_y(rt) = - sum_m kappa_m sum_{l in m} y_l (rt'_l - rt_l).
Proof.  Definitions and K2.8(a).  QED
Consequence (PROVED).  The generators at design-depth coordinates, the levers (P1)-(P4) and the pre-placements depend only on R_1; the
targets enter the generator set ONLY through the peak columns col_c = -(1 - X_m) lambda_c rt^{(m)} - h_c gtil (K1 2.4), whose action on
a vector y is -(1 - X_m) lambda_c zeta_m - h_c y^T gtil.  Apart from this, the targets enter K2.9 only through the right-hand side
b = -Ft(R_1).  So, for a fixed set of near-certificates, "Step A is not A-regular" is a statement about the position of the target
displacement rt - rc relative to the dual cone: by K2.9(b) a failure produces a near-certificate y of size < 4 Design^{-C_A} with
sum_m kappa_m sum_{l in m} y_l (rt_l - rc_l) < rho_0.  Every obstruction is a TARGET-PLACEMENT obstruction (with the peak columns as the
only target-dependent generators).

## 1.3 Lemma J1.3 (normal form of a residual certificate).  PROVED (from K2.16).
Let y be a near-certificate of size eps <= eps_* with phi_y > -rho_0 (the situation of K2.9(b)); by K2.16(3) kappa := kappa_Psi <= -c_*/nu_1.
Let S_1 be the set of design-depth coordinates carrying a one-sided generator (data-carrying S_th coordinates), S_2 the design-depth
coordinates carrying a two-sided generator (TS, FR, ZD, levers), S_0 the remaining design-depth coordinates (off U_L, off F or thin), and
Deep := (D, infinity).  Define
      Theta := (1/kappa) Dev_Psi 1_{S_1},    E := Dev_Psi 1_{S_0 ∪ S_2 ∪ Deep}.
Then Psi = kappa (a + Theta) + E, and:
 (a) |E(s)| <= eps Design(L) for s in S_2; |E(s)| <= 2|kappa| b for s in S_0; ||E 1_Deep||_1 <= tail_D + |kappa| alpha(D) (alpha(D) :=
     sum_{s in F, s > D} |a_s|);
 (b) ANTI-SIGN: Theta(s) z_s <= eps Design(L)/(|kappa| eff_s) <= eps Design(L)^2/|kappa| for s in S_1 (z_s = the sign of the S_th
     coordinate = the data sign);
 (c) ONE-SIDED MASS: 1 + Theta(z) = (phi_y - E(z))/kappa, hence
      sum_{s in S_1} (-Theta(s) z_s)  >=  1 - (rho_0 + |E(z)|)/|kappa|,    |E(z)| <= D(L)(eps Design + 2|kappa| b) + tail_D + |kappa| alpha(D).
Proof.  Psi = kappa a + Dev_Psi and Dev_Psi = kappa Theta + E by definition.  (a): S_2: K2.16(2) (two-sided generator at s: |eff_s
Dev_Psi(s)| <= eps, eff_s >= 1/Design) and K2.16(4)-(5); S_0: Psi(s) = 0 (s off U_L) so Dev_Psi(s) = -kappa a_s with |a_s| <= 2b;
Deep: Dev_Psi = Psi - kappa a, ||Psi 1_Deep||_1 <= tail_D (K2.16 proof of (1)).  (b): the raise at s in S_1 acts on y^T Ft by
eff_s Dev_Psi(s) z_s >= -eps (J1.1(c), raise of |a_s| in the direction z_s), and Dev_Psi(s) z_s = kappa Theta(s) z_s with kappa < 0.
(c): J1.1(b): Psi(zhat) = kappa + Dev_Psi(z) = kappa + kappa Theta(z) + E(z), and Psi(zhat_1) = phi_y (J1.2); divide by kappa < 0 and use
phi_y > -rho_0; Theta(z) = sum_{S_1} Theta(s) z_s.  The bound on |E(z)| is (a) with |z| <= 1.  QED
Reading.  A residual certificate is "a + (anti-signed one-sided part of mass ~ 1) + small": the combination Phi_y := Psi/kappa is, up to
small errors, the base vector a plus a vector Theta supported on the data-carrying one-sided coordinates, anti-signed there, of total
mass >= 1 - small.  This holds for BOTH types (A*) and (U*); the type only describes which carriers own S_1 and which carry the robust
coefficients.  [For (A*) with K_0 := supp(coef) ∩ (P4)-carriers: Phi_y = (1/nu_1) sum_{K_0} (a_p/v_l(p)) u_l + ..., i.e. the support is
swallowed proportionally (U2 Lemma ND / Q2 Lemma 4.3 form) and Theta lives on the data-sign contacts/banks of these carriers.]

## 1.4 Lemma J1.4 (global rigidity: the frozen functional cannot be increased).  PROVED.
Keep the notation of 1.3 and put Phi := Psi/kappa = a + Theta + E/kappa (a fixed vector of l_1).  Let R' = (a', z') be ANY row (forced
data of some first row; a' normalized, q*(a') = 1) such that
 (i) for s in S_1: z'_s = z_s and a'_s z_s >= 0 (the one-sided coordinates stay contacts/supports of their data sign);
 (ii) supp(a') ∩ supp(Theta) ⊂ S_1 (automatic: supp Theta ⊂ S_1).
Then
      Phi(zhat') <= 1 + Theta(z) + delta_Theta + (E(zhat') )/kappa,      delta_Theta := sum_{s in S_1} mu_s^2 Theta(s) a'_s / nu'  ( <= eps Design^2 sum_{S_1} mu_s^2 |a'_s| /(|kappa| nu') ),
and Phi(zhat_1) = 1 + Theta(z) + delta_Theta(R_1) + E(zhat_1)/kappa.  Consequently
      Phi(zhat') - Phi(zhat_1) <= [delta_Theta(R') - delta_Theta(R_1)] + [E(zhat') - E(zhat_1)]/kappa,
and the right side is bounded by eps Design^2 (sum_{S_1} mu_s^2 (|a'_s|/nu' + |a_s|/nu))/|kappa| + (||E 1_{S_0∪S_2}||_1 ||z' - z||_inf +
2 ||E 1_Deep||_1 + ||U^*E|| ||e' - e||)/|kappa|.
Proof.  a(zhat') = sum_s a_s z'_s + <U^*a, e'> <= ||a||_1 + ||U^*a|| = 1 (|z'| <= 1; Cauchy-Schwarz, ||e'|| = 1).  Theta(zhat') = Theta(z') +
<U^*Theta, e'> = Theta(z) + sum_{s in S_1} mu_s Theta(s) mu_s a'_s/nu' by (i) and the diagonal base (e'_s = mu_s a'_s/nu').  Add E(zhat')/kappa.
At R_1 itself a(zhat_1) = 1 exactly (J1.1(b) proof).  Subtract; E(zhat') - E(zhat_1) = E(z' - z) + <U^*E, e' - e>.  Each summand of
delta_Theta has mu_s^2 Theta(s) a'_s = mu_s^2 (Theta(s) z_s)(a'_s z_s) <= mu_s^2 (eps Design^2/|kappa|) |a'_s| by 1.3(b) and (i).  QED
Remarks.  (1) Equality in a(zhat') <= 1 holds iff z' = sgn a on F and e' = e (strict convexity of the Hilbert norm): every move that
changes the direction of U^*a strictly DECREASES Phi at second order (U2's -kappa nu ||e' - e||^2/2 with kappa < 0).  (2) Lemma J1.4 is
NONLINEAR and GLOBAL: it does not use the size W of the moves, only (i).  It is the exact counterpart of the first-order statement of
K2.16 (all generators increase y^T Ft = Psi(zhat) = kappa Phi(zhat), kappa < 0).

## 1.5 Corollary J1.5 (the obstruction is a genuine infeasibility of the targets; target freedom or a change of data is necessary).  PROVED.
Assume in addition that every block m meeting supp(y) has a PRIVATE two-sided peak resource (then |zeta_m| <= 2 eps Design, K2.17(f)
proof / K1 2.4: y^T col_c = -(1 - X_m) lambda_c zeta_m) — the generic situation, since at a clean sub-window every block has a coarse peak
with robust margin (V1 Lemma D).  Let R' be any row satisfying (i) of J1.4 at which the Step-A equations Ft = 0 hold (targets rt).  Then
      kappa Phi(zhat') = sum_l y_l val_l(R') = sum_m zeta_m kappa_m(R') + y^T Ft(R') = sum_m zeta_m kappa_m(R'),
so |Phi(zhat')| <= 2 eps Design sum_m kappa_m(R')/|kappa|, while Phi(zhat_1) = phi_y/kappa + sum_m zeta_m kappa_m(R_1)/kappa.  Hence, if
      phi_y > |kappa| (bound of J1.4 at R') + 4 eps Design sum_m (kappa_m(R') + kappa_m(R_1)),
no row R' with (i) realizes the targets at all — whatever the size of the moves leading to it.
Proof.  Euler: y^T Ft(R') = sum_l y_l val_l(R') - sum_m zeta_m kappa_m(R') (definition of Ft, zeta).  Since sum_l y_l val_l = sum_l y_l eps_l
u_l(zhat') = Psi(zhat') + sum_m zeta_m K_m(zhat') and Psi = kappa Phi ... we use instead the direct form: sum_l y_l val_l(R') = (sum_l y_l eps_l
u_l)(zhat') =: Psi_0(zhat') with Psi_0 = Psi + sum_m zeta_m K_m, ||sum_m zeta_m K_m||_1 <= 2 eps Design sum_m ||K_m||_1; so Psi_0 = kappa Phi + (a
vector of l_1-norm <= C eps Design).  At R': Psi_0(zhat') = sum_m zeta_m kappa_m(R') (Ft = 0), at R_1: Psi_0(zhat_1) = phi_y + sum_m zeta_m
kappa_m(R_1).  Lemma J1.4 bounds kappa Phi(zhat') - kappa Phi(zhat_1) from BELOW (kappa < 0) by -|kappa| (bound); combine.  QED
Meaning.  When phi_y is of the size of the target displacement (O(x)), no companion that keeps the data-carrying one-sided coordinates
as contacts/supports of their data sign can realize the targets: the one-sided coordinates PIN the frozen functional Phi(zhat) from
above, and the targets demand a larger value.  So no improvement of the realization step (Brouwer, degree, larger moves, different
lever menus on two-sided coordinates) can remove (A*)/(U*); one must change (I) the targets (target freedom), (II) the treatment of
the one-sided coordinates (their data), or (III) the data equations themselves (relaxation / gauge).  These are routes (1), (2)/(3),
and the mismatch-tolerance route below.
