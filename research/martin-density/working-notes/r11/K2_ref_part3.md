# K2 referee, part 3: Sys-A (Lemma K2.8, Lemma K2.9, Theorem K2.16, Corollary K2.17, 5.5, Proposition K2.11)

## 1. Lemma K2.8 (Euler combination).  VERDICT: correct.
kappa_m = A + theta Phi_P^2 + S/theta (U1 Lemma 1.3, S over Q_m minus Omega_m).  (E1), (E2) of U1 Lemma 1.2 are invariant under nu -> c nu, A -> cA,
theta -> c theta, so A, theta are positively 1-homogeneous in the block vector zeta_m while the peak set (a scale-invariant condition nu_k > theta)
is fixed; S is 2-homogeneous; so kappa_m is 1-homogeneous and C^1 there.  Euler: kappa_m = sum_k zeta(k) d kappa/d zeta(k) = K_m(xhat).  Then
Psi^A_y(xhat) = sum_l y_l val_l - sum_m (sum_{l in m} y_l rt_l) kappa_m = y^T Ft; (b) is the chain rule with dkappa_m = l_delta(K_m); (c) follows.
The notation zeta_m is used both for the block vector and for the scalar sum_{l in m} y_l rt_l; harmless but should be separated.
Numerics (K2_ref_work/ref_sysA.py, ref_sysA_central.py): Euler 4e-10; Psi^A(xhat) = y^T Ft to 2e-11; generator actions = l_delta(Psi^A) to 1.5e-5
(central differences, 1802 moves).
Point (R2) of K2 (non-peak Euler share Xt_m <= 1/4): CONFIRMED in route V.  Lambda_A contains every coarse strict non-peak, so Q_m minus Omega_m
consists of fine carriers and U1 Lemma 1.5 (final form) gives X_m <= C b^2 D^2; d kappa/d|zeta(d)| = rho_d M X/C for d in Omega_m (U1 Lemma 1.4(c)),
hence |Xt_m| <= ||rt||_inf X_m (tiny).  Numerics: |Xt| <= 3.4e-6 in this regime, 3e-2 when one coarse strict non-peak is left out of Omega (and up
to 1.85 in K2's general-block probe).  So K2.16's use is legitimate exactly because route V tunes every coarse strict non-peak.

## 2. Lemma K2.9 (cone realization).  VERDICT: correct.
(a) B(0, eps_PS) is inside Q = conv(G u {0}) by separation; ||b||/eps_PS <= W/4 needs C_A >= C_1 + 2; rho_0/eps_PS <= W/4 needs W <= 1/(4 C_2
Design^{C_1}), true since W <= Design^C x'_max.  (b) Separation of a point of B(b, rho_0) from the compact convex (W/2)Q gives a unit y with
y^T b < rho_0 - (W/2) max(0, max_g(-y^T g)); hence max_g(-y^T g) < 2(rho_0 + ||b||)/W <= 4 Design^{-C_A} and phi_y = -y^T b > -rho_0.  Only the
implication "not A-regular => such a certificate" is proved (see 5 below for the consequence).  (c) Two-sided generators enter as +-g; the
minimal-norm nonnegative selection never uses both (they are antiparallel), so the realized move is well defined and its first-order effect is
exactly G t.  S(b') = argmin{||s||_2 : G s = b', s >= 0} is continuous on cone(G) (Hoffman: the feasible polyhedra move Hausdorff-Lipschitz; the
metric projection of 0 onto a Hausdorff-continuous family of closed convex sets is continuous -- one may intersect with a large ball since the
minimal-norm point stays bounded).  T(t) = S(b - Rem(t)) maps K = {t >= 0, ||t||_2 <= W} into itself because b - Rem(t) is in B(b, rho_0) inside
(W/2)Q, so a feasible s with ||s||_2 <= ||s||_1 <= W/2 exists.  Brouwer gives t* with Ft + G t* + Rem(t*) = 0.  The composite moves are C^{1,1}
(part 1, 3), so ||Rem(t)|| <= C_2 ||t||^2.  Correct.  The size of the realized moves is <= W; with K1's compensated pre-placements ||b|| ~ x and W
is of the order of K1 Lemma K1.6(A)'s moves, so K1.6(A)'s status, Puiseux and cost conclusions transfer (they use only exactness and move sizes).

## 3. Theorem K2.16 (structure of Step-A obstructions).  VERDICT: correct (each step re-derived), with three precisions.
(2) generator actions: re-derived from K2.8(b) + K2.4.  (2a) a pre-placed TU bank sits at a near coordinate that is now support of mass >= theta_0,
    so its action is eff (coef_k v_k(s) - kappa a_s): the bound reads |coef_k| <= (eps Design + |kappa| theta_0) Design -- K2 omits the kappa theta_0
    term in (2a) (it keeps it in (2c)); harmless (PRECISION K-1).
(2c) PRECISION K-2 (signs): the action of a raise at a data-carrying S_th coordinate is (coef_k v_k(s') - kappa a_{s'}) sgn(a_{s'}); the stated form
    "coef_k z_{s'} >= -(...)" presupposes v_k > 0 on S_k (true for the positive signatures delta_l h_l of the SLD family); in general replace z_{s'}
    by z_{s'} sgn v_k(s') here, in kind (iv) and in K2.17(d) ("same sign" means sgn(a_p v_k(p)) = sgn(z_{s'} v_k(s'))).
(1) If gamma > 0 then kappa(1 - alpha(D)) >= kappa nu_1 = gamma, and by (2) and 4.1(d) every design-depth c_s >= -eps Design except thin
    off-U_L coordinates (c_s = -kappa |a_s| >= -2 kappa b); the deep sum >= -tail_D; so gamma <= phi_y + D eps Design + 2 D kappa b + tail_D and,
    as 2 D b <= nu_1/2, gamma <= 2(|phi_y| + D eps Design + tail_D).  Correct (this is the signed form of K2.3).
(3) Re-derived: zeta_m(1 - Xt_m) = sum_{l in m} rt_l eps_l coef_l (from eps_l y_l = coef_l + zeta_m lambda_l d kappa/d zeta(l)), so ||coef_tuned||_2
    >= c_1 (with Xt_m tiny, c_1 can even be taken ~1/2).  Kinds (i)-(iv) are exhaustive (a data-carrying carrier's off-F near coordinates are
    contacts of the data sign, its thin ones carry the data sign; a free near coordinate forces c_l = 0).  Kind (ii) may be defined with ANY
    non-tiny spread: two thick private coordinates force |kappa||rho_s - rho_{s'}| <= C eps Design^2, so an intermediate spread (between C eps
    Design^3/|kappa| and u) also excludes certificates; the classification "robust spread / otherwise" is therefore harmless.  Case gamma > -gamma_0:
    ||coef_(iii)|| <= |gamma| ||h|| + small <= c_1/4, kinds (i), (ii) small, so ||coef_(iv)|| >= c_1/2; each kind-(iv) carrier with coef_l sigma_l > 0
    contributes >= coef_l sigma_l v_l(s) - |kappa| |a_s| at each of its S_th near coordinates; identity (2.1) then forces kappa(1 - alpha(D)) <=
    |phi_y| - c_U + tail_D < 0 and gamma = kappa nu_1 <= -c_1 nu_1/(8 H(L)).  Correct.
(4)-(6) Correct.  (6) is derived under phi_y > -rho_0; the thin off-U_L coordinates contribute +|kappa||a_s| >= 0 (K2 bounds them in absolute value).
PRECISION K-3: in (3)'s kind (iv), |a_s| at f_1 + Pi is in [theta_0, 2b] (banked contacts: theta_0; raised thin coordinates: max(theta_0, |a_s|));
K2 writes theta_0; the estimate needs only |kappa||a_s| <= 2|kappa| b << c_1/H(L).
Interpretation.  K2.16 is a necessary condition for an obstruction; it does not assert that obstructions exist.  The degeneracy behind (A*) is the
Sherman-Morrison type condition h^T g~ ~ 1 (Sys-A: g~ = g - (rt_l G_{m(l)})_l).  Observation (PROVED, elementary): if a (P4)-carrier l has all its
thick coordinates proportional, a_s = r_l v_l(s), and u_l meets the support only there, then h_l g_l = sum_{s in S_l cap F} mu_s^2 a_s^2/nu^2; for
such carriers h^T g <= (Hilbert mass of a on their private sets)/nu^2 <= 1.  So h^T g~ ~ 1 needs either the peak terms -(h^T rt^{(m)}) G_m or cross
terms through shared (target) coordinates of T(L) -- consistent with (4), which forces a = Psi/kappa on the whole thick design-depth support,
targets included.  (Toys ref_sysA2/3.py, without target cross terms: no degenerate point and no certificate was found; evidence only.)

## 4. Corollary K2.17.  VERDICT: (a)-(f) correct; (g) correct as a reduction, but it is NOT by itself a sufficient condition.
(a)-(e) re-derived from K2.16 (with K-2's sign convention in (d)).  (f) re-derived: in K1.5(b)'s setting y ~ +-h/||h||, gamma = +-h^T gt/||h||, so the
only candidate certificate is -y_+, and phi_{y_+} >= 2 rho_0 + (deviation) excludes it by the contrapositive of K2.9(b).  (g): the argument shows
that every near-certificate has coef_(iv) small, hence gamma <= -gamma_0 and y ~ -h/||h|| (type (A*)); A-REGULARITY then still requires (f)'s
criterion.  7.2 of K2 lists "(a)-(g)" as sufficient conditions: (g) must be read as "(g) together with (f)'s criterion" (PRECISION K-4).
Toy check (ref_sysA.py): 15 configurations satisfying (c) or (d): no certificate.

## 5. 5.5 ((O-c)(iii)) and 5.7 (residual).  VERDICT: first part correct; the "Moreover" sentence is a SKETCH; 7.3's "iff" is only "only if".
KN-1 holds are rows of Sys-A with zero targets and zero data; kind (i)/(ii)/(iii) classification as K2 says; so they are covered by K2.16: correct.
"Moreover ... a z-move there (two-sided ...) breaks the certificate": a far CONTACT gives only a one-sided z-move; it becomes two-sided only after
pre-placing z_j inside (-1, 1) (cost as R-6, admissible since the data vanish); and the generator's per-unit action |coef_l| v_l(j) <= x'_max is far
below the certificate tolerance Design^{-C}, so it "breaks" the certificate only through the range/overshoot argument of Proposition K2.11 --
SKETCH (PRECISION K-5).  The conclusion "(A*) then requires S_l cap {x <= v_l <= x'_max} in F with |a_j| > x'_max" inherits this status.
7.3: "(f, g, rho) is NOT covered by Theorem K2.15 iff ..." -- only "=>" is proved (K2.9(b) gives a certificate from non-A-regularity; the converse
is not shown and not needed).  PRECISION K-6: replace "iff" by "only if".
Proposition K2.11 (SKETCH): label honest.  Remark: for a data-carrying carrier, support of the DATA sign placed at a contact of the data sign
does nothing (sigma - z_j = 0); a push has an effect only at far coordinates of F of the anti-data sign (flip through zero, cost ~ |a_j|) or at
zero-data carriers -- the push lemma is genuinely the mirror of V1's in-F pull, not of the off-F pull.
