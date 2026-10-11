# J1 referee, part 1: Lemmas J1.1-J1.4, Corollary J1.5; numerics N1-N3

Setting and notation as in r12/J1_notes.md 1 (design T_fin^{K2}; K2 Sections 1, 5 with K2-ref K-1..K-8; K1 2.0-2.7 with K1-ref).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Scripts and outputs: r12/J1_ref_work/.

## 1.1 Lemma J1.1 (deviation identity).  Verdict: CORRECT.
Re-derived: <U^*Dev_u, e> = kappa_u nu - kappa_u <U^*a, e> = 0; a(zhat) = ||a||_1 + nu = 1 (z = sgn a on F); u(zhat) = kappa_u a(zhat) +
Dev_u(z) + <U^*Dev_u, e>.  First-order actions: K2.4 (refereed) with D_u(s) = Dev_u(s) on F; off F, a_s = 0, so Dev_u(s) = u(s) and the bank of
mass dm at a contact s notin F acts by (mu_s^2/nu) u(s) z_s dm with NO common-mode term (the change of e is along k_s - e_s e with e_s = 0).
Rerun (J1_ref_work/rerun/check_part1.out): identity to 1.67e-14.

## 1.2 Lemma J1.2 (target-displacement form).  Verdict: identities CORRECT; the "Consequence" is IMPRECISE (precision P-1).
Ft_l = kappa_m (rc_l - rt_l) and phi_y = sum_m kappa_m sum_{l in m} y_l (rc_l - rt_l) = Psi^A_y(zhat_1) are definitions plus K2.8(a).
P-1.  "The generators depend on the targets only through the peak columns" is not literally true: in K1 2.4 every (P4)/TS mass column
contains the common mode -h gtil with gtil = g - (rt_l G_{m(l)})_l, and in K2.8(b) every generator acts on y by l_delta(Psi^A_y) where
Psi^A_y = sum_l y_l eps_l u_l - sum_m zeta_m(y; rt) K_m.  The correct statement (PROVED, K2.8(b)) is:
  for each unit y, the actions y^T g of ALL generators depend on the targets only through the N numbers zeta_m(y; rt) := sum_{l in m} y_l rt_l.
In particular the SET of near-certificates moves with the targets, so "for a fixed set of near-certificates, non-A-regularity is a statement
about the target displacement" is misleading: a displacement of the targets along a certificate y changes zeta_m(y; rt) by
sum_{l in m} y_l delta_l, and in every block with a private two-sided peak resource this destroys y as a certificate (Lemma R-PK below,
numerics N3).

LEMMA R-PK (peak-column constraint; PROVED here).  Let block m have a private two-sided peak resource: a z-move or a ZD composite move at a
design-depth coordinate s private (among coarse carriers) to a coarse peak c of m.  Under the frozen convention (FC)/K-8 its Sys-A column is
-(1 - X_m) lambda_c v_c(s) rt^{(m)} (only kappa_m moves; val_l, l in m, do not; e does not move), so every near-certificate y of size eps
satisfies
      |zeta_m(y; rt)| <= eps / ((1 - X_m) lambda_c |v_c(s)|) <= (4/3) eps Design(L)        (unnormalized columns; X_m <= 1/4).
Consequently, for such blocks, phi_y's block contribution is kappa_m [zeta_m(y; rc) - zeta_m(y; rt)] = kappa_m zeta_m(y; rc) + O(eps Design kappa_m)
= sum_{l in m} y_l val_l(R_1) + O(eps Design kappa_m): a ROW quantity; the targets enter only through the certificate condition.
Proof: the move changes only u_c(xhat) (by v_c(s) dz; e unchanged; fine carriers at s have total weight <= C c_{L+1}); kappa_m changes by
(dkappa_m/dzeta(c)) lambda_c v_c(s) dz with dkappa_m/dzeta(c) = 1 - X_m (U1 Lemma 1.4(a), frozen peak set); Ft_l = val_l - rt_l kappa_m.  QED

## 1.3 Lemma J1.3 (normal form).  Verdict: CORRECT (precision P-2).
Re-derived from K2.16 and J1.1: Dev_Psi = kappa Theta + E by definition; (b) the raise at s in S_1 acts by eff_s Dev_Psi(s) z_s >= -eps, and
Dev_Psi(s) = kappa Theta(s) with kappa < 0, giving Theta(s) z_s <= eps Design/|kappa| (the notes' eps Design^2/|kappa| is weaker); (c) J1.1(b)
with Psi(zhat_1) = phi_y.  P-2: on S_0 (design-depth coordinates off U_L) Psi(s) is the FINE part, not 0, so |E(s)| <= 2|kappa| b + C c_{L+1};
harmless.  The one-sided hole mass identity 1 + Theta(z) = (phi_y - E(z))/kappa is exact and says Phi_y(zhat_1) = phi_y/kappa ~ 0.

## 1.4 Lemma J1.4 (global rigidity).  Verdict: CORRECT as stated (an inequality with explicit error terms).
Re-derived: a(zhat') <= ||a||_1 + ||U^*a|| = 1 (|z'| <= 1, Cauchy-Schwarz); Theta(zhat') = Theta(z) + sum_{S_1} mu_s^2 Theta(s) a'_s/nu' (diagonal
base, z' = z on S_1); each summand <= mu_s^2 (eps Design/|kappa|)|a'_s| when a'_s z_s >= 0.  The rerun (20000 rows, 0 violations) tests only the
case E = 0, eps = 0 (pure Cauchy-Schwarz).  NOTE: the error terms are NOT small in general: ||E 1_{S_2}||_1 ||z' - z||_inf (two-sided
coordinates, residual action eps Design each), 2||E 1_Deep||_1 (contains |kappa| alpha(D) and, at a far coordinate j, exactly the action
Psi(j)(z'_j - z_j) of a far placement) and ||U^*E|| ||e' - e||.

## 1.5 Corollary J1.5.  Verdict: the INEQUALITY is correct; the stated CONCLUSION is FALSE as stated (finding F-1).
The inequality  phi_y <= |kappa| Bound_{J1.4}(R') + sum_m zeta_m (kappa_m(R') - kappa_m(R_1)) + 2 eta_K (1 + ||U||)  holds (re-derived; the last
term may be sharpened to eta_K ||zhat' - zhat_1||_inf).  But the conclusion "no companion that keeps the one-sided signs realizes the current
Step-A targets ... better realizations (degree arguments, larger moves, two-sided levers) cannot do it" does not follow and is contradicted
by J1's own Theorem J1.7:
 (i) The hypothesis "phi_y > |kappa| Bound(R') + ... + 2 eta_K (1 + ||U||)" is essentially never satisfiable: phi_y <= ||b|| = O(|Lambda_A|^{1/2} x),
     while 2 eta_K (1 + ||U||) = 4 eps Design (1 + ||U||) sum_m ||K_m||_1 and eps may be as large as 4 u^3 Design^{-C_A} >> x.  Even with the sharp
     form eta_K ||zhat' - zhat_1||_inf and Bound(R') evaluated for moves of size W, the error is ~ Design eps W ~ Design (rho_0 + ||b||) (K2.9(b):
     eps W < 2(rho_0 + ||b||)), i.e. not smaller than phi_y.  So J1.5 excludes realizations only within a radius ~ phi_y/(eps Design D), which is
     no more than what K2.9(b) already says.
 (ii) A far placement (J1.6(b)) keeps every S_1 coordinate's sign and data (S_1 is at design depth, the placement is beyond D(L)); its action
     coef_k v_k(j)(tau - z_j) is precisely a Deep term E(j)(z'_j - z_j) of Bound_{J1.4}; Theorem J1.7 shows that it makes Step A A-regular for the
     SAME targets.  Numerics N2 (ref_j15_placement_B.out; consistent generators): in J1's resonant toy without a private peak resource
     (variant B of N3, where the displaced-target Step A is GENUINELY obstructed: linearized minimal move 31-175), a pull at the helpful far
     coordinate of a thick-type carrier keeps every S_th sign, turns y^T Ft into -1.17e-2, and the minimal move for the SAME targets drops to
     2.8e-3 (v = 1e-2), resp. 6.6e-4 (v = 3e-3); the frozen-functional change Phi(zhat') - Phi(zhat_1) equals the Deep term E(j)dz_j/kappa exactly.
     (With J1's peak resource, ref_j15_placement.out, the displaced targets were not obstructed to begin with: N3.)
 (iii) Two-sided coordinates have residual actions up to eps Design per unit; moves of size ~ phi_y/(eps Design) along them are not excluded.
Correct replacement (PROVED): for a near-certificate y and a row R' keeping the S_1 signs and realizing the targets, the first-order
E-action of R' -- sum over S_0 ∪ S_2 of E(s)(z'_s - z_s) [resp. mass terms], over Deep of E(j)(z'_j - z_j), and <U^*E, e' - e> -- must be
>= phi_y - (second-order and eta_K terms).  So a realization must use (a) two-sided moves of size >= c phi_y/(eps Design D), or (b) far
coordinates (J1.7), or (c) a change of the direction of U^*a.  This LOCALIZES the obstruction; it does not make it "genuine".
The meta-conclusion of J1 0(1) ("no improvement of the realization ... can remove (A*)/(U*): one must move the targets, relax rows, or change
the data") must be withdrawn; J1.7 itself is a realization improvement (a far move) that removes it.

## 1.6 Numerics (sanity only)
N1 (rerun of J1's scripts, J1_ref_work/rerun/): check_part1 identical (1.67e-14; 20000 rows, 0 violations); check_resonant2 identical
  (kappa_Psi in [-2.09, -1.93], coef_k/(kappa rho_k) = 1.0000, jumps = predictions); check_band identical (29-143 vs 1.4e-4).
N2 (ref_j15_placement.py; outputs ref_j15_placement.out (J1's toy) and ref_j15_placement_B.out (no peak resource)): see 1.5(ii).
N4 (ref_noncirc.py/.out): see part 3, F-2.
N3 (ref_band_consistent.py/.out): J1's check_band.py computes the generator matrix with targets = current ratios rc but the right-hand side
  with displaced targets rt = rc +- dsz y/kappa ("stale" generators).  Recomputing CONSISTENTLY at rt:
  (A) J1's toy (the peak has a private FR coordinate): displacing the targets along y destroys the certificate (sv_min of the two-sided
      columns 1.6e-5 -> 9e-3..4e-2; zeta(y; rt) = -3.9e-3), and the minimal move WITHOUT any band is 2.0e-2..1.0e-1 (stale: 29-143).  A
      displacement orthogonal to y inside the block keeps y a near-certificate but gives phi_y ~ 1e-17 (marginal).  This is Lemma R-PK.
  (B) the same toy with the peak's FR coordinate removed (no private peak resource): the certificate persists at rt, minimal move without
      band 29-175, with a band on the thick-type row 1.6e-4.  So J1.9's mechanism is confirmed, but the configuration of J1's check_band
      is not an obstruction at all; J1's reported numbers come from the stale generator matrix.
