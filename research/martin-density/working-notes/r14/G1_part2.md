# G1 part 2: the transplant needs exactness only on STRICT minors (soft/strict split of the class cone)

Setting: Part III Section 5 (infinite base support; design T^inf_fin with K2/J1/J2/H1/H2 conventions: (FC), P-TU, F-2,
(D-enum)), main stage L >= l_f, clean sub-window w, class a, b = b(w), u = u(w), T = T_lo(w), T_hi = T_hi(w), theta_0 =
b/Des^{C_P}.  f^r the deep-raised row, f^P the prepared row (Def. III-prep), f^# the route-V companion after Step A.
K_X := C_f Des(L)^C bounds the coarse data (part 1, Section 0); K t bounds their row violations; n <= 2L active variables.

## 2.1 The rows of the enlarged class cone and their tolerances at the companion
Rows of Gamma^#(kappa, a; r) (Part II Def. 5.52 / Part III Def. III-cone, enlarged by (X1^F) at tiny-support target
coordinates, Part III before Lemma III-track), in the active variables (Delta', gamma):
 (X3)_m        Delta'_m - sum_{l in Omega_a(m)} r_l gamma_l = 0 (active shift) or sum r_l gamma_l = 0 (inactive): EQUALITY.
 (X1-FR)       L_j(Delta', gamma) = 0 at target coordinates j in E_c(w) that are free with robust room (type FR): EQUALITY.
 (X1-ag)       aggregated signature rows on S_l cap (L, s_far]: ONE variable each (gamma_l, or Delta'_m for a robust peak).
 (X1-c), (X1^F) s_j L_j >= 0 at target coordinates that are contacts (X1) or tiny support (X1^F) of f^r.
 (X4^0), (X4), (X4^U)  inward rows at near-threshold carriers ((X4^U) has one variable).
Here L_j(Delta', gamma) = sum_l gamma_l u_l(j) - sum_m Delta'_m tau_m(j).  Coordinates beyond Dbar(L) that are not aggregated
carry no coarse carrier with two variables (signature sets of distinct coarse carriers are disjoint, targets lie in T(L)
subset [1, Dbar(L)]), so every row with >= 2 variables is (X3), (X1-FR), (X1-c)/(X1^F) at a target coordinate, or (X4)-type.

After the preparation (P1)-(P3) every target coordinate j in U_L cap [1, Dbar(L)] with a row of type (X1-c)/(X1^F) is a
SUPPORT coordinate of f^P and of f^# of type S_th, |a^#_j| >= theta_0/2 (contacts are banked by (P2), tiny rooms are closed by
(P1) and then banked, tiny support is raised by (P3)); Lemma III-prep (d).  Robust target support has no row.

LEMMA 2.1 (tolerances).  PROVED (mod chain: Prop. III-cushion, Lemma III-CMtr's kind-[3] verification).
At the companion f^#, for every scale t of the class set:
 (a) [S_th rows]  a violation of the row (X1-c)/(X1^F) at j by delta >= 0 at the projected data point (i.e. s_j V_proj(j) >=
     -delta) is admissible for (U3^inf) with cushion constant C_+ := 9 provided delta <= 4|a^#_j|/t.  In particular every
     such row tolerates beta_j(t) := 2 theta_0/t.
 (b) [(X4^0)/(X4) rows]  a violation of the inward row at a near-threshold carrier d by v >= 0 (in the units of the row,
     i.e. of lambda_d vs_d Delta omega(d)) keeps d of kind [3] relative to gap^#(d) provided v <= lambda_d gap^#(d)/t.
 (c) [strict rows]  (X3) and (X1-FR) rows must hold exactly at the projected point (single-variable rows too).
Proof.  (a) Two places use the row.  At a banked contact s (P2) the pieces are built as in Prop. III-cushion (iv): contact-like
z-signed part of V(s) plus the base term beta_s, |beta_s| <= 4Kt|a^#_s| <= |a^#_s|/t.  If s_j V(s) = -delta < 0 is anti-signed,
replace the contact-like split of the anti-signed part by the symmetric split b^+ ∋ -delta s_j/2, b^- ∋ +delta s_j/2 (so b^+ -
b^- = V is kept and b^theta receives nothing).  Then (s_j b^+)_- <= delta/2 + |beta_s| and (s_j b^-)_+ <= delta/2 + |beta_s|, which
is <= 9|a^#_s|/t... more precisely <= (2 + 1)|a^#_s|/t when delta <= 4|a^#_s|/t; (U3^inf) holds with C_+ = 9 and r(j) unchanged.
At a tiny-support target coordinate (raised by (P3)) the deep assignment of Prop. III-cushion is applied with A_j :=
2|a^#_j|/t in place of 2|a^r_j|/t: the interval [y_j - A_j - tr_j, x_j + A_j] is nonempty iff s_j V_c(j) >= -2A_j - tr_j,
which holds when delta <= 4|a^#_j|/t, and the conclusions (s_j b^+_1)_- <= A_j, (s_j b^-_1)_+ <= A_j + tr_j and the bound
||B_+1_F - b^+_1||_1 <= (1 + eta')t/q_0 + Kt + 7C c_{L+1}/t are unchanged (a larger A_j only shortens sigma_j).  Since |a^#_j|
>= theta_0/2, beta_j(t) = 2 theta_0/t is admissible.
(b) In the proof of Lemma III-CMtr (kind [3] in (T)-blocks) the cone point is used only through lambda_l vs_l Delta omega^#(l) >=
-C_f lambda_l (c_{L+1} + D^C c_{L+1}^2), which is then compared with -3 lambda_l gap^#(l)/t; an additional violation v of the
row lowers the left side by v (Lemma III-floorrow (a)), and -C_f lambda(c_{L+1} + ...) - v >= -3 lambda gap^#/t holds for v <=
lambda gap^#/t because C_f(c_{L+1} + D^C c_{L+1}^2) <= gap^#/t (c_{L+1} <= b^2, gap^# >= M mu/4).  (KN)-blocks: the same with the
row (X4) in the units of vs Delta omega (Lemma III-CMtr, (KN) clause: -|Delta'*|gap^#/M - C_f c_{L+1} >= -3gap^#/t).
(c) (X3) defines the true shift (U1 Lemma 4.6 / II Lemma 5.58) and a mismatch enters the peak traces at FR coordinates, where
only the violation tolerance (VT') of mass <= delta s_1/(64 rho) is available, and the far aggregated rows of the robust peaks
of inactive blocks (H2 Prop NE's list); (X1-FR) violations are violations at free coordinates (tolerance (VT') only).  QED

Remark 2.2 (finer split, SKETCH).  (X3)_m of a block with an ACTIVE shift can also be cushioned when no FR coordinate lies in
supp tau_m (a mismatch then only enters cushioned rows and the sign of the far aggregated peak rows is kept by the robust
|Delta'_m| >= A Kt).  This is J1's mismatch tolerance (Prop. J1.12, (MT1)); not used below.

## 2.2 Definition (strict and soft rate objects; strictly pinned ratios)
For a pattern kappa let S(kappa) be the set of STRICT rows: (X3) rows, (X1-FR) rows and the single-variable rows; all other
rows are CUSHIONED.  A minor of the matrix of Gamma^#(kappa, a; r) is STRICT if all its rows are strict, SOFT otherwise.
Since strict rows other than (X3) have design coefficients, every strict minor not containing an (X3) row is a design number
(0 or >= delta_comb(L)); a strict tiny object contains at least one (X3) row ("equality resonance").
An active ratio is STRICTLY PINNED if some tiny strict minor depends on it, SOFTLY PINNED if it is pinned (J1.13) but not
strictly pinned, FREE otherwise.  Z^str_kappa := {r in K_kappa : every tiny strict minor vanishes}  (contains Z_kappa).

## 2.3 The soft tolerance
Put, for the sub-window w,
   mu_tol(w) := u min( theta_0, lambda_min(L) g'_min(w) ) / (2^{L+2} K_X T_hi(w)),
where g'_min(w) is the least gap^# of a near-threshold carrier at the companion (>= M mu/8 in (T)-blocks, >= c_flat eta'M in
(KN)/(U)-blocks).  Lemma CH with eta = 2^{n/2} mu/u <= 2^L mu/u and |X^#| <= 2 K_X shows: if every soft tiny minor has modulus
<= mu_tol at the realized ratios, the cushioned rows are violated by at most eta |X^#| <= min(2theta_0, lambda_min g'_min)/T_hi
<= the tolerances of Lemma 2.1 at every scale t <= T_hi.

LEMMA 2.3 (size of the tolerance).  PROVED.  For L >= l_f: mu_tol(w) >= b (Q(w)/Des(L)^{C_P + C}) >= Des(L)^{10} b, provided
g'_min(w) >= b Des(L)^{-C}.  In particular every soft tiny object at the prepared row f^P (modulus <= (1 + 2 Lip) b, Lemma
III-prep (b)) is within the soft tolerance with a factor >= Des(L)^5 to spare.
Proof.  T_hi(w) <= 2^{-L^3}/(L Q(w)) (window recursion, Lemma III-count) and Q(w) = (4 Des(L)/u)^{omega(L) + L^2 + 20}, while
K_X, 2^{L+2}, 1/u, Des^{C_P} are all <= (Des/u)^C << Q(w); lambda_min(L) >= 1/D(L) >= 1/Des(L).  QED
So the near-exactness gap of H2-ref F-NE (b >> s_1/T >> delta_Z) concerns the (VT') tolerance only; for SOFT objects the
relevant tolerance is the cushion, mu_tol >> b, and F-NE does not apply to them.

## 2.4 Theorem (soft transplant)
THEOREM G1.A.  PROVED (mod the chain cited by J1.15', J2.1, and Prop. III-cushion; once-refereed links as listed there).
Let (L, w, a) be a stage as above and let f^# be a companion built by Step 0, the preparation and a realization of Step A whose
realized active ratios r^# satisfy
 (E1) every tiny STRICT minor of Gamma^#(kappa, a) vanishes at r^#;
 (E2) every tiny soft minor has modulus <= mu_tol(w) at r^#, every robust minor has modulus >= u/2;
 (E3) the statuses required by J1.13 (ii) (with the gap bound g'_min(w) >= b Des^{-C}), and |r^# - r(f)| <= u/(4 Lip).
Then the conclusions of Lemma III-CMtr (c), (d) and of Prop. III-cushion hold at f^# with C_+ = 9 and with K_data replaced by
H_CH K_data, H_CH := p^{p/2} Lambda^p/(u/2), Lambda := 2p^{p/2}/u + 1 (p = number of rows); the class thresholds K_*(w) of
Lemma III-track are taken >= 6(H_CH(C_Gamma J + 1) + 1).  Hence the stage feeds Theorem E^{eng,RT,inf} exactly as a stage
with r^# on Z_kappa does.  Exactness on Z_kappa is needed ONLY for the strictly pinned ratios.
Proof.  At r^#, (SE) holds for the strict rows: a strict minor without (X3) row is a design number, one with an (X3) row is a
rate object, robust (>= u/2) or tiny and then 0 by (E1).  (MD) holds with mu := mu_tol(w) and u/2 by (E2).  The data of a scale t
(inactive components zeroed) violate every row at r^# by V <= (1 + C_Gamma J A_{i(t)}) K t + Lip |r^# - r(f)| K_X <= 2(1 +
C_Gamma J A_{i(t)}) K t (the second term is <= Des^C eta' K_X << K T_lo).  Lemma CH (rows of the whole cone; the face-wise
restriction is not needed here) gives X^# with strict rows exact, cushioned rows violated by <= eta |X^#| <= the tolerances of
Lemma 2.1 (Section 2.3), and |X^# - X| <= H_CH V.  Lemma III-track (active components move by <= 1/6 of their modulus) holds with
the enlarged K_*(w).  The construction of the pieces (Prop. III-cushion and Lemma III-CMtr (c),(d)) uses the cone point only
through: exact (X3) (true shift = cone shift), exact (X1-FR) (V_proj = 0 at free coordinates), the sign of the projected
switching on contacts and tiny-support target coordinates (replaced by Lemma 2.1(a)), the inward rows (replaced by Lemma
2.1(b)), and the bound on |X^# - X| (multiplied by H_CH).  The window count (Lemma III-count) absorbs H_CH: log_B H_CH <= C p
log p, and p <= C Des(L) <= omega(L)/4 (the rate scheme contains all minors of all patterns, omega(L) >= 2^p).  QED

## 2.5 What changes in J1.13 (minimal exactness set)
COROLLARY G1.B.  PROVED (inspection of J1.13's list, with Theorem G1.A).  Downstream of Step A the following suffices:
 (i) strictly pinned active ratios realized EXACTLY on Z^str_kappa (not Z_kappa);
 (ii) softly pinned active ratios: realized anywhere such that (E2) holds, in particular within D_tol(w) := mu_tol(w)/(2 Lip)
      of their values at f^P (soft objects at f^P are <= (1 + 2Lip)b <= mu_tol/2);
 (iii) free ratios and inactive values: as in J1.13 (statuses only);
 (iv) cofactor polynomials need not be exact: route V uses no cube normalization (Lemma III-nocube), so A_max and the
      g_J-minors are not used [inspection of Lemma III-nocube's proof, which lists every use of the normalization].
Comparison with J1.13: there, every pinned ratio (strict or soft) and every cofactor polynomial had to be exact.

Remark 2.4 (necessity).  Exactness of strict tiny minors cannot be dropped in general (part 1, Remark (c): two equality rows
with a tiny nonzero minor collapse the face).  For soft minors the tolerance mu_tol is the right scale: the cushioned violation
is exactly d_i x' (Lemma CH (v)), proportional to the minor.
