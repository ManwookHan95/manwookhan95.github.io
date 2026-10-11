# G1 part 4: a preparation with split masses (removing H2's preparation bias)

## 4.1 Where the bias came from and why it no longer matters for soft objects
H2 Lemma 5.2: (P2)/(P3) bank every design-depth contact (mass theta_0 = b/Des^{C_P}) and raise every thin coordinate in U_L, so
every kind-(iv) value rises by >= eff v theta_0 per banked near contact, and pinned values at TARGET coordinates move by ~ eff
u_k(j) theta_0 (H2-ref F-NE, P-52(iii)); in the old scheme this pushed one-signed resonances to the wrong side by >> delta_Z.
In the scheme of parts 2-3:
 - SOFT objects: the whole preparation moves every value by <= b + C Dbar(L) theta (Lemma III-prep (b)), hence every soft minor
   by <= 2 Lip b, which is << mu_tol(w) (Lemma 2.3).  The bias is harmless for soft objects.  PROVED.
 - STRICT objects: the bias enters their start values; strict objects must be EXACT at the realized ratios, so the bias matters
   only through the one-sided realizability of A_m (Lemma LE) -- a size question addressed in 4.2.

## 4.2 The split preparation (P^nat)
Definition 4.1.  Fix the stage.  Put
   theta_T := b T_hi(w) (Des(L)/u(w))^{C_T}      (TARGET coordinates: T(L) cap U_L, design depth),
   theta_pr := max(8 rho A_0 s_1/T, 4 Des(L) K_DC r)    (PRIVATE coordinates: S_l cap [1, Dbar(L)], l coarse),
with C_T an absolute constant fixed in Lemma 4.2 (s_1, r, K_DC as in K2 6.4 / Theorem K2.6; theta_pr <= exp(-c/T)).
(P1) is unchanged (close every free s <= Dbar(L), s in U_L, with tiny room 1 - |z_s| <= b).
(P2^nat): bank mass theta_T z_s at every contact s in T(L) cap U_L, s <= Dbar(L); bank mass theta_pr z_s at every private contact.
(P3^nat): raise (same sign) every support s in T(L) cap U_L with |a_s| < theta_T to theta_T; every private thin support with |a_s|
< theta_pr to theta_pr.

LEMMA 4.2 (properties of P^nat).  PROVED (mod chain: Lemma III-prep, K2 4.1, 6.3-6.5).
 (a) Cost <= C D(L) theta_T log(1/theta_T) + C_f Dbar(L) b log(1/b) = o(u^2 T^2) (the (P1) closings dominate, as before).
 (b) Every value moves by <= b + C Dbar(L)(theta_T + theta_pr) <= 2b; the clean classification survives with factor 2.
 (c) Types (Lemma III-prep (d)) unchanged with S_th meaning |a_s| >= theta_T/2 at target coordinates and >= theta_pr/2 at
     private coordinates; (U3^inf) at banked/raised coordinates holds as before (contact-like data plus base term, cushion
     dominated by any positive mass, Prop. III-cushion (iv)); (L-K2-1) and (L-K2-2) hold at every banked coordinate (theta_pr is
     defined as the larger of the two floors, theta_T >= theta_pr for T small since b >= exp(-C log^3(1/T))).
 (d) Soft tolerance: with theta_min := theta_T in the definition of mu_tol (only target S_th rows are cushioned rows with >= 2
     variables; private rows are single-variable), mu_tol(w) = u min(theta_T, lambda_min g'_min)/(2^{L+2} K_X T_hi)
     >= b (Des/u)^{C_T - C} >= Des(L)^{10} b/u^{10} for C_T large: Lemma 2.3 and Lemma 3.2 (W^nat << D_tol) still hold.
 (e) Bias on STRICT objects from banks and raises: every strict tiny minor changes by <= Lip C Dbar(L)(theta_T + theta_pr) <=
     b T_hi(w)(Des/u)^{C_T + C} =: b_bias, a negligible multiple of b (T_hi(w) <= 2^{-L^3}/(L Q(w))).  The remaining change of
     strict objects in the preparation comes from the (P1) closings (<= Lip b, determined by f's tiny rooms).
 (f) H2 Lemma 5.2's bias on kind-(iv) values from private banks is <= eff v theta_pr <= exp(-c/T): negligible against every
     quantity of the construction except exact coincidences.
Proof.  (a)-(c) as Lemma III-prep with the two masses (each cost term is monotone in the mass; (L-K2-1), (L-K2-2) are lower
bounds on the masses).  Why private coordinates may use theta_pr: the purposes of theta_0 at a private coordinate are (i) the
S_th type for Theorem K2.6's two-sided Sys-DC lever at scale r (needs mass >= 4 Des K_DC r: (L-K2-2)), (ii) survival of the
bank under the theta piece of Theorem UE^inf (needs s_1 <= theta T/(8 rho A_0): (L-K2-1)), (iii) one-sided Step-A raises
(efficiency mu_s^2/nu, independent of the mass), (iv) cushion domination of route-V data (contact-like plus a base term
proportional to the mass: any positive mass); none needs theta ~ b.  At target coordinates the mass is used in addition for the
CUSHIONED rows of part 2 (tolerance 2 theta_T/t), which is what fixes theta_T.  (d): substitute theta_T in Lemma 2.3's
computation: u theta_T/(K_X T_hi 2^{L+2}) = u b (Des/u)^{C_T}/(K_X 2^{L+2}) and K_X 2^{L+2}/u <= (Des/u)^{C}.  (e): Lemma
III-actions (ii): a bank of mass theta at a contact s changes u(xhat) by (mu_s^2/nu) u(s) z_s theta, so values move by <=
theta per unit of |u(s)| <= 1; strict minors are Lip-Lipschitz in the ratios; ratios move by <= C_f (value moves).  (f) idem.  QED

Remark 4.3 (what is NOT removed).  (P1) closings are kept: a free coordinate with tiny room cannot carry the coarse switching
(its row would be an equality with tolerance only (VT')), so it must become a contact (and then a banked S_th coordinate whose
row is cushioned).  The closing changes values by <= b, of the size of f's own tiny objects; it is a datum of f at the clean
sub-window, not a design artefact.  Banks are one-sided (masses >= 0); if a strict one-signed resonance has every shared bank
direction on its wrong side (part 5, (R-S1) with the bank columns), no choice of masses helps; P^nat only makes the bank effect
negligible (b_bias << b).

## 4.3 Row-aligned moves (a tool, used in part 5)
LEMMA 4.4.  PROVED.  Let j be a target coordinate and let a move change the values of the coarse carriers by c u_k(j) (k coarse;
c a scalar), e.g. a bank of mass theta at the contact j (c = (mu_j^2/nu) z_j theta) or a z-move at a free j (c = dz).  Let M be a
minor of the class cone containing the row (X1)_j and exactly one (X3) row, (X3)_m, of a block whose shift is inactive, and
whose columns lie among the gamma-columns of block m and the columns on which row (X1)_j vanishes.  Then the first-order change
of M under the move is zero.
Proof.  The block scalar kappa_m changes by some dkappa, and r^(m) changes by (c u^(m)(j) - r^(m) dkappa)/kappa_m.  The term
-r^(m) dkappa/kappa_m multiplies the row (X3)_m by (1 - dkappa/kappa_m) (homogeneity, Lemma III-Uscale), changing M only by the
factor.  The term c u^(m)(j)/kappa_m changes (X3)_m by a multiple of the restriction of (X1)_j to the gamma-columns of block m,
which on the columns of M equals (X1)_j itself (by the column hypothesis); so M changes by a multiple of a determinant with two
proportional rows, i.e. by 0.  QED
Consequence.  Moves at a coordinate j are useless (two-sided or not) for exactifying the minors that contain row j (H2-ref P-41
(ii)), and harmless for them: the bank of P^nat at a resonant target contact does not move the resonance it cushions.
