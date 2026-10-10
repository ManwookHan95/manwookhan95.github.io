# X2 part 2 — Exact d-consistency by levers (Lemma DC) and the availability of levers at U1's companions (Lemma LV)

Setting of part 1.  f_0 is a row (F_0 finite), Omega = union_m Omega_m a finite set of strict non-peaks of f_0, split into
Omega^abs (zero-value absorbers of D^{U1'}: u_a(zhat_0) = 0, block 1) and Omega^0 := Omega \ Omega^abs.  A PRE-ROW f_1 = (A_1, z_1) is
obtained from f_0 by adding finitely many masses of sign z_0 at coordinates off F_0 (or same-sign masses on F_0) and by changing
z_0 only on a set Z_1 (e.g. the cut-off z_1 := 0 beyond N''); all carriers' values move by at most delta_1 := max_k |u_k(xhat_1) -
u_k(zhat_0)| (Lemma M1: delta_1 <= ||X_1||/nu + max_k sum_{s in Z_1} |u_k(s)| |z_1(s) - z_0(s)|).

## 2.1 Levers.  (Definitions.)
For l in Omega with block m = m(l) fix a sign eps_l in {+-1} and one of the following lever types; v_l(s) := u_l(s) for s in S_l.
 (Z-free) a coordinate j in S_l \ F_0 that is FREE at f_1 with room 1 - |z_1(j)| >= rr > 0; for P in R put z(j) := z_1(j) + eps_l P/v_l(j).
 (Z-con)  a coordinate j in S_l \ F_0 that is a contact of f_1 with z_1(j) = eps_l; for P <= 0 put z(j) := eps_l (1 - |P|/v_l(j))
          (inward move), for P > 0 a BANK: mass beta_j P with sign eps_l at j, beta_j := nu_1/(mu_j^2 v_l(j)) (nu_1 := ||U^*A_1||).
 (TU)     a PULL coordinate j_p in S_l, a contact of f_1 with z_1 = eps_l, and a BANK coordinate j' in S_l, j' != j_p, a contact of f_1 with
          z_1 = eps_l (or a support coordinate with sgn A_1(j') = eps_l); the pull is fixed: z(j_p) := -eps_l, mass -eps_l mu_p at j_p with
          mu_p := 24 lambda_l v_l(j_p); for P >= -2 v_l(j_p) a bank of mass beta_{j'} (P + 2 v_l(j_p)) with sign eps_l at j'.
 (S-mass) a support coordinate p in F_0 with u_l(p) != 0; for P in R change A(p) by sgn(A_1(p)) beta_p P, beta_p := nu_1/(mu_p^2 |u_l(p)|),
          and put eps_l := sgn(A_1(p) u_l(p)).
Write P = (P_l)_{l in Omega}, f(P) for the resulting row and Lev_l for the lever coordinates of l.  SEPARATION (SEP):
 (i) the sets Lev_l are pairwise disjoint and disjoint from F_0 except for (S-mass); (ii) Lev_l ∩ supp u_k = {} for all k in Omega^0 \ {l};
 (iii) for a in Omega^abs, Lev_a ∩ supp u_k = {} for all k in Omega \ {a}.  (Absorbers may meet lever coordinates of Omega^0.)

## 2.2 Lemma DC (exact d-consistency).  PROVED.
Put, for l in Omega, F_l(P) := eps_l [ u_l(xhat(P)) - (A_m(P)/A_m^0) u_l(zhat_0) ], where A_m(P) := |R_m xhat(P)|_m, A_m^0 := |R_m^** zhat_0|_m.
Zeros of F are exactly the lever parameters at which f(P) is d-consistent with f_0 on Omega (Definition 1.4; statuses below).
Constants: A_min := min_m A_m^0, K_X := max_{a in Omega^abs} sum_{k in Omega^0} sum_{s in Lev_k} |u_a(s)|/v_k(s), K_J := (1 + K_X)(1 + 4/A_min).
There are r_0 > 0 and C_2 < infinity, depending only on f_0, Omega, the lever data (v_l on Lev_l, mu on Lev_l, rooms, pull ratios
v_l(j_p)/r <= 2^{G}) and the status margins of the carriers of Omega and of the peaks of f_0 (all positive), such that: if
      K_J |F(0)|_inf <= r/2,   K_J C_2 r <= 1/4,   K_J c_tiny <= 1/4,   r <= r_0,   and (TU levers) v_l(j_p) >= r,
where c_tiny := max_{m, k in Omega} sum_{l' notin Omega, l' > L} lambda_{l'} sum_{s in Lev_k} |u_{l'}(s)|/v_k(s) (first-order effect of the
levers on the block norms through carriers outside Omega that meet lever coordinates), then F has a zero P* with |P*|_inf <= r.  At f(P*):
every l in Omega is a strict non-peak with nv_l(P*) = nv_l^0 (exact d-consistency), the peaks of f_0 of every block remain peaks with the
same signs, every carrier value moves by at most delta_1 + C_lev r (C_lev := max over carriers k of sum_{s in Lev} |u_k(s)| (|dz_s| + mass
effect) per unit r, a constant of the lever data), the total off-F_0 mass vector satisfies ||X_lev|| <= C_2 r, and the data moved are
only: z on the Z-type and pull coordinates, masses on banks/pulls/S-mass coordinates.
Proof.  (1) Continuity.  For |P|_inf <= r_0 the row f(P) has admissible forced data (bank masses >= 0 have the sign of z; inward z-moves
keep |z| <= 1; (TU) needs P >= -2 v_l(j_p), true for |P| <= r <= v_l(j_p); (S-mass) keeps the sign of A_1(p) for r_0 small; (Z-free) keeps
|z(j)| < 1 for r_0 <= rr min v_l(j)).  Its forced data depend continuously on P (finitely many coordinates move; prop:forced, prop:continuity
applied to the explicit formulas: e(P) = U^*A(P)/||U^*A(P)||, xhat(P) = z(P) + U e(P), A_m(P) = |R_m xhat(P)|_m).
(2) First-order structure.  By construction of the levers and Lemma M1(i) with base A_1: eps_l (u_l(xhat(P)) - u_l(xhat_1)) = P_l + E_l(P), where
E_l collects (a) Hilbert terms: changing masses changes e by Lemma M1(i)-(ii); the first-order part of a mass at its own coordinate s in
Lev_l is exactly the normalized slope (beta_s mu_s^2 v_l(s)/nu_1 = 1) up to the factor nu_1/nu(P) - 1 = O(||X_lev||^2), and the
cross part (nu/nu_A - 1)<U^*u, e> is O(||X_lev||^2); for other masses <U^*u_l, X> vanishes at first order unless the mass coordinate lies in
supp u_l, excluded by (SEP)(ii) for l in Omega^0; (b) for a in Omega^abs, the first-order effects of the Z/TU levers of Omega^0 at
coordinates of supp u_a: sum_k X_{ak} P_k with |X_{ak}| <= sum_{s in Lev_k} |u_a(s)|/v_k(s).  Hence |E_l(P) - sum_k X_{lk} P_k| <= C_2' |P|^2
(X_{lk} := 0 unless l is an absorber).  Next, A_m is a norm with norming functional w_m(P) at R_m xhat(P), so with dxhat := xhat(P) - xhat_1,
0 <= A_m(P) - A_m(1) - <w_m(1), R_m dxhat> <= <w_m(P) - w_m(1), R_m dxhat>; the clamp formula (proof of lem:F1) gives |w_m(P)(k) - w_m(1)(k)|
<= K_cl |dxhat-value at k| for every carrier k of block m whose status does not change, with K_cl depending on 1/Phi_k^2 and the threshold
constants; carriers outside Omega ∪ peaks contribute only through c_tiny and second order.  And <w_m(1), R_m dxhat> = sum_{k in Omega_m}
lambda_k w_m(1)(k) eps_k (P_k + E_k) + (contributions of carriers outside Omega meeting lever coordinates, <= c_tiny |P|_inf A_m^0) +
O(|P|^2).  Finally w_m(1)(k) = w_m^0(k) + O(delta_1/Phi_k^2) and u_l(xhat_1) - u_l(zhat_0) = O(delta_1).
(3) The linearization.  Order the variables (Omega^0, Omega^abs).  With p_l := eps_l u_l(zhat_0)/A_m^0 and q_k := eps_k lambda_k w_m^0(k)
(k, l in Omega_m ∩ Omega^0; p, q := 0 on absorbers, whose values and w vanish), F(P) = F(0) + J P + R(P) with
      J = [[ I - p q^T , 0 ], [ X , I ]]     (p q^T blockwise, i.e. only within each block),
and |R(P)|_inf <= C_2 |P|_inf^2 + c_tiny |P|_inf + C delta_1 |P|_inf on |P|_inf <= r_0 (the last term from replacing data at f_1 by data at f_0;
absorbed into C_2 r once delta_1 <= r).  Now q^T p = sum_{k in Omega_m} w_m^0(k) nv_k^0 = sum_{Omega_m} Phi_k^2 w(k)^2/C_m <= C_m <= 1/2 by
(1.0) and ||D_m w_m||_2 = C_m < 1/2, so by Sherman-Morrison (I - p q^T)^{-1} = I + p q^T/(1 - q^T p) has inf-norm <= 1 + 2||p||_inf ||q||_1
<= 1 + 4/A_min (|u_l(zhat_0)| <= ||zhat_0||_inf <= 2, ||q||_1 <= sum_k lambda_k <= 1).  The block-triangular J has
J^{-1} = [[ (I - pq^T)^{-1}, 0 ], [ -X (I - pq^T)^{-1}, I ]], ||J^{-1}||_inf <= K_J.
(3') Lever masses placed at coordinates s that are ALREADY in supp A_1 ((S-mass) levers; (TU) banks at window contacts that carry a
theta-mass; (Z-con) banks at such contacts) act, by Lemma M1(iv), at first order on every value through the nu-change, with coefficients
Y_{k,l} = -sgn(A_1(s)) beta_s mu_s^2 A_1(s) eps_k <U^*u_k, e_1>/nu_1^2, i.e. |Y_{k,l}| <= |A_1(s)|/(nu_1 v_l(s)) (resp. |A_1(p)|/(nu_1 |u_l(p)|)).
Hence the true linearization is J + Y; if K_J ||Y||_inf <= 1/2 (hypothesis added to the lemma), then ||(J + Y)^{-1}||_inf <= 2 K_J and the
argument below runs with 2K_J in place of K_J.  (At U1's companions: for absorbers |A_1(p_0)| = m_0(a) <= theta_a + c_p^2, theta_a = C_f lambda_a T_hi,
|u_a(p_0)| >= 1/(8 n_a), so their contribution is <= C sum_a m_0(a)/nu <= C_f c_{L+1}; for banks at window contacts |A_1(s)| is a theta-mass
4 rho s_1 max_i |b^theta_i(s)| <= 4 rho s_1 A_0/T, so ||Y||_inf <= C_f c_{L+1} + Design(L) s_1 A_0/T: negligible under (LATE).)
(4) Poincare-Miranda.  G(P) := J^{-1} F(P) = J^{-1} F(0) + P + J^{-1} R(P) is continuous on the cube Q_r := [-r, r]^Omega.  On the face P_l = r,
G_l(P) >= r - K_J |F(0)|_inf - K_J (C_2 r^2 + c_tiny r) >= r - r/2 - r/4 - r/4 >= 0, and symmetrically G_l <= 0 on P_l = -r.  By the
Poincare-Miranda theorem G has a zero P* in Q_r; J^{-1} is invertible, so F(P*) = 0.
(5) Statuses and sizes.  r_0 is chosen below the relative margins/gaps of the peaks and Omega carriers of f_0 (divided by the Lipschitz
constant of the values, which is C_lev), so no status changes; at a zero of F, eps_l u_l(xhat) = eps_l (A_m/A_m^0) u_l(zhat_0) means
nv_l(P*) = nv_l^0, and (1.1) gives gap(P*) >= gap^0/2 once |C(P*) - C^0| <= gap^0_min/4.  Masses of the levers are <= beta (r + 2 v(j_p)) <=
beta 2^{G+2} r and z-moves <= r/v: ||X_lev|| <= C_2 r after enlarging C_2.  QED
Remark.  The rank-one structure is exact: a lever acting on one value changes the block norm, hence ALL normalized values of that block;
the factor 1/(1 - q^T p) >= 1 - C_m >= 1/2 is the reason no second, kappa-neutral lever is needed here (compare U1-ref's Lemma R-kt, which
concerns the different problem of holding ratios while moving statuses).

## 2.3 Lemma LV (levers exist at U1's companions).  PROVED (from U1's refereed structure: Lemma 3.2, Lemma 3.3, Proposition 3.4, Lemma 4.1,
## Lemma 4.2, Section 5 of U1-ref (release G1), and V1 Lemma ST / Proposition TR).
Let f^# be the companion of a clean sub-window w of a main stage L of D^{U1'} (U1 part 4 with U1-ref's fixes) carrying, for every scale t of
a (class, cube) set S, data Domega(t) supported in Omega = (coarse strict non-peaks of f^#) ∪ (tuned absorbers), and let s_max := s_max(L),
s_far := s_far(w).  Then every l in Omega has a lever satisfying (SEP), with lever data that are design quantities of level L:
 Lever coordinate j(l) := the least element of S_l ∩ (s_max, infinity) \ F^# (the first or the second element: inside (s_max, sigma_2(L)]
 the companion's support meets S_l at most in the first element, a donor/tuning bank of V1 (C3)/(C4) or of U1 Prop. KN; V1's and U1's pulls
 sit where v_l <= 2^{G} Design b, far beyond).  DESIGN ADDITION (D-lev), a ladder condition computable at stage L and N-free:
 Design(L) >= max_{l <= L} 2^{sigma_2(L)}/(mu_{sigma_2(L)}^2 delta_l), sigma_2(L) := max_{l <= L} (second element of S_l beyond s_max(L));
 then mu_{j(l)}^2 v_l(j(l)) >= Design(L)^{-1} for all l <= L (efficiency of every lever below).
 (a) ACTIVE class-G carriers (gamma_l != 0 in the class): type (TU) with eps_l := sgn of the switching coefficient, bank coordinate j' := j(l)
     (a contact with z^# = eps_l and contact-like data V_t(j') = gamma_l(t) v_l(j') of sign eps_l; it is met by its first absorber pair,
     a first-order cross effect recorded in X), pull coordinates among the far coordinates of S_l (contacts of f^# with z = eps_l: they
     are owned by l, U1 Lemmas 4.1-4.2 / owners of type (a) in mixed classes, Lemma 5.1); bounded gaps of S_l give, for every r <= r_0, a pull
     coordinate with v_l(j_p) in [r, 2^{G(L)} r];
 (b) INACTIVE class-G carriers (gamma_l = 0) and class-G carriers that are strict non-peaks of value tuned to 0 ((K3)): type (Z-con) at
     j := j(l) in S_l ∩ (s_max, s_far] \ F^#; there z^# = eps_l (closed by V1's (C1)) and the exact data vanish for every scale:
     V_t(j) = L(Delta'', gamma(t))(j) = gamma_l v_l(j) = 0 (Proposition 3.4(b) of U1: exact equality on E_c; only l lives on S_l ∩ (s_max,
     infinity) among coarse carriers, allowedness (a), (c)), hence b^+-_t(j) = chi V_t(j) = 0;
 (c) class-R carriers (robust aggregate room on S^nat): at j := j(l) in S_l ∩ (s_max, s_far] \ F^# the data vanish, V_t(j) = gamma_l v_l(j) = 0
     (gamma_l = 0 for class R, U1 (X2)), whatever z^#(j) is (free or contact).  Use the ZERO-DATA lever (Z-gen): for P in R move
     z(j) := clamp_{[-1,1]}(z^#(j) + eps_l P/v_l(j)) and put the overflow into a bank at j with the sign of the contact reached
     (mass beta_j x overflow in value units).  This is continuous, has first-order slope 1 on both sides, and every state of j is admissible
     because the data at j vanish ((Z-free) and (Z-con) are the special cases of a free coordinate with large room and of a contact);
 (d) tuned absorbers a: type (S-mass) at their continuous tuning coordinate p_0 (support coordinate of f^#, mass m_0 in
     [theta_a, theta_a + c_p^2], U1 Lemma 3.3), with eps_a := sgn(m_0 u_a(p_0)); the data satisfy t|b_t(p_0)| <= m_0 (U1 Prop. 3.4(d)).
(SEP) holds: (i) the coordinates of (a)-(c) lie in the private signature sets S_l, those of (d) are fresh odd coordinates; (ii) beyond s_max no
coarse target meets S_l (allowedness (c): supp y_k ∩ S_l ⊂ [1, k] ⊂ [1, s_max] for coarse k), so a lever coordinate of l lies in no supp u_k,
k in Omega^0 \ {l}; (iii) p_0 lies in no earlier target and in no signature set; later carriers meeting p_0 are fine (not in Omega).  The
only first-order cross effects are those of (b), (c) on the first absorber pair P(j) of each lever coordinate j in (s_max, s_far] (U1
Lemma 3.2), i.e. exactly the matrix X of Lemma DC; an absorber's vector meets at most one lever coordinate (its own target coordinate s;
the other coordinates of its target are fresh), so K_X <= max_l 1/v_l(j(l)) <= Design(L) by (D-lev).
Proof.  Read off from the cited statements; the only new observation is the zero-data property in (b), (c), which is the exactness of the
coarse system on E_c (Proposition 3.4(b) of U1: V(s) = L(Delta'', gamma)(s) for s in E_c \ F^#) combined with gamma_l = 0, and the
representation b^+ = beta + chi V 1_{K} (U1 Proposition 2.2(e) / Lemma 1.1(c): beta is supported in F^#).  For (a): in configuration (i) the
far part of S_l is owned by l (owner-candidate of type (a), Lemma 4.1) with z = sgn(gamma_l v_l) = eps_l; in configuration (ii) and in mixed
classes the fixed owners of types (a)-(c) keep their owned sets (Lemma 4.4 / 5.1 with Lemma 4.2's dominance, whose estimates do not use signs);
the G1 release (U1-ref Section 5) concerns only NON-owner carriers.  QED
Consequence.  At U1's companions Lemma DC applies with lever data of level L: r_0, C_2, C_lev, K_J are (f-constant) x Design(L)^{C}, and
c_tiny <= Design(L)^C c_{L+1} (fine carriers meeting lever coordinates have total weight <= 2 c_{L+1}).
Numerics (X2_work/dcons_check.py, dcons_check2.py; N = 1 model with exact forced data via the threshold equation): for VALID exact data
(Gamma^+ = 0.0066, Gamma^- = 0.031) the untuned mismatch kappa is proportional to ||X|| (kappa/||X|| = 0.0230 constant over s_1 in
[1e-5, 1e-2]); one (TU) lever (pull with v(j_p) in [2 du, 2^G 2 du] plus a bank, brentq on the bank mass) restores nv exactly
(residual <= 2e-17) and kappa_tuned <= 3e-17; the bank mass is 15-26 times ||X|| (the factor varies with the discrete pull coordinate).
