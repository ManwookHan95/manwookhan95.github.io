# G1 part 3: Step A at the linear scale; linear exactification of single-row strict resonances; scale rebalancing

Setting as in part 2.  Throughout, "design numbers of level L" are the finitely many numbers obtained from the non-weight
design data of level L (target values u_l(j), coefficients alpha_l, signs, combinatorial data) by polynomial expressions of
degree <= 4L^2 with integer coefficients bounded by 2^{L^2}; delta'_comb(L) > 0 denotes the least NONZERO modulus of such a
number.  Design insertion (D-G1a): Des(L) >= 1/delta'_comb(L) and Des(L) >= p(L)^{p(L)^2} (p(L) = maximal number of rows of an
enlarged class cone of level L).  Both are level-L quantities, N-free and f-free; insertion is monotone (U4 Lemma GW).

## 3.1 Linear exactification of single-row strict resonances
LEMMA LE.  PROVED.  Let kappa be a pattern such that every tiny strict minor contains exactly ONE (X3) row.  For a block m let
M_m be the set of tiny strict minors containing (X3)_m.  Then:
 (a) every M in M_m is an affine function of the block-m ratio vector alone, M(r) = <C_M, r^(m)> + c_M, where C_M in
     R^{Omega_a(m)} and c_M in R are design numbers (c_M = 0 if the shift of m is inactive);
 (b) if |M(r_1)| <= beta for all M in M_m and beta Des(L)^{3} < 1, the affine set A_m := {rho : <C_M, rho> + c_M = 0, M in M_m}
     is nonempty and dist_2(r_1^(m), A_m) <= Des(L)^{3} |M_m|^{1/2} beta;
 (c) moving r^(m) inside A_m changes no tiny strict minor of another block (they do not contain r^(m)); the blocks decouple.
Proof.  (a) Expand the minor along its unique (X3) row.  The entries of (X3)_m are 1 (column Delta'_m, if active and selected)
and -r_l (columns gamma_l, l in Omega_a(m)); the complementary minors are minors of rows with design coefficients (FR rows,
single-variable rows, (X3) rows of other blocks restricted to columns where they have the constant entry 1 or no entry -- a
minor containing another (X3) row would contain a second (X3) row, excluded).  So the cofactors are design numbers (minors of
design rows), and no other block's ratio occurs.  (b) Write the system as C rho = -c (rows C_M).  If it were inconsistent there
would be lambda with lambda^T C = 0 and lambda^T c = 1; choose lambda as a basic solution of the consistent system [C^T; c^T]
lambda = (0, 1): by Cramer's rule its entries are ratios of minors of the matrix [C | c], i.e. design numbers divided by a nonzero
design number, so ||lambda||_1 <= Des(L)^2 (by (D-G1a), each nonzero design number is >= delta'_comb and each design number is
<= 2^{L^2}(2L)! <= Des^{1/2}).  Then 1 = lambda^T c = lambda^T (C r_1 + c) <= ||lambda||_1 beta < 1, a contradiction.  So A_m is a
nonempty affine set.  By the Hoffman bound for linear EQUALITY systems (the polyhedron is an affine set; V2 Lemma H with E only,
or directly: dist(r_1, A_m) = ||C^+ (C r_1 + c)|| <= ||C r_1 + c||_2/sigma_min^+(C)), and sigma_min^+(C) >= (least nonzero
maximal-rank minor of C)/||C||^{rank - 1} >= delta'_comb/Des^{1/2}, we get dist <= Des^{3} |M_m|^{1/2} beta.  (c) is (a).  QED
Remark.  Minors containing >= 2 (X3) rows are multi-affine (one degree per block); their exactification can require a
non-linear displacement (Lojasiewicz exponent > 1; e.g. a 2-block minor factoring as (x_1 - x_2)(y_1 + y_2) with both factors
NOT rate objects).  They form the class (R-S2) below.

## 3.2 Step A at the linear scale (Step A^nat)
Definition 3.1.  At a stage (L, w, a) with pattern kappa, let f_1 be the row after the deep raise, Step 0 and the preparation
(part 4 for the split masses).  The Step-A^nat system is the Step-A system of Def. III-SysA with the following TARGETS:
 (T1) strictly pinned active ratios: a point of A_m (Lemma LE) -- chosen as the realizable point (see 3.3), within Des^3 L
      beta of r_1, beta := (1 + 2 Lip) b;
 (T2) softly pinned and free active ratios: their ratios at f_1 (zero displacement), with bands (overshoot bands for kind (iv),
      symmetric for two-sided rows) of half-width beta_band <= min(beta_*, kappa_min D_tol(w)), D_tol(w) := mu_tol(w)/(2 Lip);
 (T3) near-threshold active carriers of (T)-blocks that are not strictly pinned: |r_d| lowered by h_d := Des^{C_x} b (inward);
      if one is strictly pinned: a point of A_m cap {F_Phi <= 1 - 3mu/4} (descent inside A_m, see 3.4);
 (T4) KN-1 holds (nearly neutral inactive carriers of (T)-blocks): value 0 (displacement <= C b), or bands (H1 Cor. 2.4);
 (T5) inactive near-threshold carriers of (U)/(KN)-blocks: pushed to relative position <= 1 - Des^{C_x} b; (KN)-lever push of
      size Des^{C_x} b; (U)-block rescaling s_m := 1 - 4 Des^{C_x} b realized by the kappa-lever (no value moves).
The Step-A^nat scale is x^nat := Des(L)^{C_x + 4} b (C_x absolute); W^nat := Des^{C_A} u^{-3} max(x^nat, ||b||), rho_0^nat :=
C_2 (W^nat)^2, as in Def. III-Areg with x replaced by x^nat.

LEMMA 3.2 (the right-hand side is at the linear scale).  PROVED (mod chain).  At f_1 + P (P the TU pre-placements, P-TU), |Ft|_inf
<= x^nat.  Hence ||b|| <= |Lambda_A|^{1/2} x^nat, W^nat <= Des^{C} b/u^3, and all Step-A^nat moves are <= W^nat << D_tol(w).
Proof.  Rows with targets (T2) have Ft = 0 at f_1; (T1) by Lemma LE(b); (T3)-(T5) by definition (kappa_m, Phi bounded below by
1/C_f and 1/D(L)); the TU pre-placements contribute their second-order residue <= C Des^C (W')^2 (P-TU, compensating base banks).
W^nat << D_tol: D_tol >= mu_tol/(2Lip) >= b Q(w)/Des^C (Lemma 2.3) while W^nat <= Des^C b/u^3.  QED

## 3.3 Realization criterion
THEOREM G1.C.  PROVED (mod chain: Lemma III-cone (c), J1.8, H2 Lemma 3.2/3.3, J1-ref F-2, J2 (FC), and Theorem G1.A).
Let (L, w, a) be a stage at which every tiny strict minor of kappa contains exactly one (X3) row and no strictly pinned
near-threshold active carrier of a (T)-block exists.  If the band-relaxed Step-A^nat system is A-regular (Lemma 3.2 of H2:
B(b, rho_0^nat) subset (W^nat/2) conv(G u {0}) - Box), then there is a companion f^# satisfying (E1)-(E3) of Theorem G1.A, with
cost <= C_f Des^C W^nat log(1/W^nat) = o(u^2 T^2); hence (LSC-trunc)_N holds at (f, g, rho) if this happens at infinitely
many main stages (with J2.1's (FC) and Theorem E^{eng,RT,inf} as in J1.15').
Proof.  Brouwer realization as in Lemma III-cone (c) / J1.8 (a) with the frozen (FC) block scalars.  At the realized point:
(E1) strictly pinned ratios are exactly on A_m (equality rows of Step A^nat), so every tiny strict minor vanishes (Lemma LE(a));
(E2) every soft tiny minor M: |M(r^#)| <= |M(r_1)| + Lip |r^# - r_1|_{ratios of M} <= (1 + 2Lip) b + Lip (W^nat/kappa_min +
beta_band/kappa_min) <= mu_tol (Lemma 2.3, Lemma 3.2), and robust minors stay >= u/2 (moves << u); the (U)-block rescaling
multiplies every minor of the block by s_m^e with e <= n (Lemma III-Uscale), preserving vanishing and smallness;
(E3) statuses: (T)-blocks -- the lowered floor statuses are <= 1 - c Des^{C_x} b/D(L) while all other moves change statuses by
<= Des^C W^nat ... more precisely the frozen statuses at the targets are as prescribed (Lemma III-K is monotone in |r_d| and R^2),
and the protected margin mu := c Des^{C_x - 1} b exceeds the later drifts C_f Des c_{L+1} <= C_f Des b^2 (Lemma III-drift);
(U)/(KN)-blocks -- margins Des^{C_x} b M as in Prop. III-KNtr (b) with eta' replaced by Des^{C_x} b; robust statuses move by
<= Des^C W^nat << u.  Theorem G1.A then applies.  QED

## 3.4 Scale bookkeeping (constraints (K2-d), (L-K2-1), (L-K2-2), (W_exp), (LATE), S2c^tr, Lemma III-drift)
LEMMA 3.3.  PROVED (bookkeeping).  With x^nat, the companion of Theorem G1.C, and the split preparation of part 4:
 (a) (K2-d) theta_0 = b/Des^{C_P} is used only at TARGET coordinates (cushions, part 2); at private near coordinates the
     preparation uses theta_pr := max(8 rho A_0 s_1/T, 4 Des K_DC r) (part 4); (L-K2-1) s_1 <= theta T/(8 rho A_0) and (L-K2-2)
     Des K_DC r <= theta/4 hold for theta in {theta_0, theta_pr} by definition (s_1 := max(64 rho eps/delta, exp(-1/(2T))),
     K2 6.4);
 (b) (W_exp) c_{L+1} <= exp(-1/T_lo) is unchanged and still gives eps <= C_f Des c_{L+1} << s_1 (fine carriers through their
     weight only, K1.S);
 (c) (LATE): s_late = c_late (T gap_min x_0/(n A_0 K_w))^7 with gap_min >= c b/Des^C (T3)-(T5) and x_0 = c_f g_min Phi_min >=
     b/Des^C, K_w <= exp(C log^3(1/T)) (K2 6.4 with 1/gap_min <= Des^C/b, b >= exp(-C log^3(1/T))); hence s_late >=
     exp(-C' log^3(1/T)) >> exp(-1/(2T)) >= s_1 for T small: (LATE) holds;
 (d) Lemma S2c^tr: the Puiseux exponent no longer enters at stages covered by Theorem G1.C ((T3) is a linear lowering); where
     the old Puiseux step is kept its cost exp(O(log^2(1/T))) is absorbed by (W_exp) exactly as before;
 (e) Lemma III-drift: later moves change statuses by <= C_f Des c_{L+1} <= C_f Des b^2 << mu = c Des^{C_x - 1} b;
 (f) costs: preparation <= C D(L)(theta_0 log(1/theta_0)), Step A^nat <= C_f Des^C W^nat log(1/W^nat) <= C_f Des^C b log(1/b)
     u^{-3}; both o(u^2 T^2) since b <= T^4.
Proof.  Direct substitution in the cited inequalities; the only changed inputs are gap_min, x_0 (now >= b/Des^C instead of
>= eta'/Des^C) and the Step-A scale; K2 6.4's estimates are monotone in these inputs.  QED

Remark 3.4 (why the scale must be linear).  If Step A ran at the old scale x = C Des eta' (Lojasiewicz/Puiseux displacements
~ eta'), soft minors containing displaced ratios could move by Lip eta' >> mu_tol whenever b << eta' T_hi (which happens as soon
as the Lojasiewicz exponent of the pattern is > 1: b <= (eta'/C_L)^{N_L/2}).  The linear Step A avoids every non-linear
Lojasiewicz/Puiseux step EXCEPT for strict multi-row resonances (R-S2) and strictly pinned (T)-block near-threshold actives
(R-S3), which are therefore listed as residual classes (part 5).
