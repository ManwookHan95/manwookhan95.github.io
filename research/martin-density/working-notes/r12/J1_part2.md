# J1 part 2: far jumps (Route 3 made rigorous) and the frozen-window residual

Notation of part 1.  For a coarse carrier k (tuned or a peak) a coordinate p in S_k ∩ [1, D(L)] beyond s_max(L) is PRIVATE to k among the
coarse carriers (disjoint signature sets; targets lie in T(L) ⊂ [1, s_max(L)]); fine carriers meet it with total weight <= C c_{L+1}.
k is THICK-TYPE if it has a thick private design-depth coordinate p (|a_p| >= u/2 at R_1).  The FAR WINDOW of k is
      FW_k := { j in S_k : Design(L)^{C_J} x/u <= |v_k(j)| <= x'_max },   x'_max = u^2 T^3/(Design(L)^2 |Lambda|)  (K1-ref R-6),
where C_J is an absolute constant fixed below; FW_k lies beyond D(L) (|v_k(j)| <= x'_max < v_min(L)) and beyond J(w) (2^{J(w)} <= Design(L)
+ 2 log_2(C n(w)) while |v_k(j)| <= x'_max forces j >= c log_2(1/T)), and FW_k is nonempty with >= 3 elements for every k (the window has
ratio >= 2^{6 G(L)} after the factor Design^{C_J}/u is removed from K1-ref R-6's ratio; bounded gaps G_l = 2^{l+1}).

## 2.1 Lemma J1.6(a) (orientation of thick-type coefficients).  PROVED.
Let k be thick-type with thick private p.  Every near-certificate y of size eps <= eps_* at R_1 (K2.16's hypothesis) satisfies
      | coef^y_k - kappa_y a_p / v_k(p) | <= eps Design(L)^2,   kappa_y := kappa_{Psi^A_y} <= -c_*/nu_1,
hence sgn(coef^y_k) = -sgn(a_p v_k(p)) and |coef^y_k| >= c_* u/(4 nu_1) (|v_k(p)| <= 1).  If k has two thick private coordinates p, p' with
sgn(a_p v_k(p)) != sgn(a_{p'} v_k(p')), or more generally with |a_p/v_k(p) - a_{p'}/v_k(p')| >= u |a_p/v_k(p)|, there is NO near-certificate
of size <= eps_* (K2.17(e)); so for thick-type k the sign tau_k(j) := sgn(a_p v_k(p) v_k(j)) below does not depend on the choice of p.
Proof.  K2.16(2b) at p: |coef_k v_k(p) - kappa a_p| <= eps Design, divide by |v_k(p)| >= v_min(L) >= 1/Design (K2-b).  K2.16(3): kappa <=
-c_*/nu_1 for EVERY near-certificate of size <= eps_* (both cases of its proof).  |kappa a_p| >= c_* u/(2 nu_1) >> eps Design^2.  The
two-coordinate statement is the kind-(ii) case of K2.16(3)'s proof (spread >= u).  QED
Remark.  So, at a non-A-regular stage, EVERY thick-type coarse carrier carries a robust coefficient of a FIXED sign in EVERY near-
certificate: the thick part of all near-certificates is the same vector (1/nu)-normalized, sum over thick-type k of (a_p/v_k(p)) u_k,
times the varying negative scalar kappa_y.  Only the coefficients of non-thick-type carriers vary between near-certificates.

## 2.2 Lemma J1.6(b) (helpful far placements).  PROVED (from refereed tools; cost and data bookkeeping as K1-ref R-6, V1 Lemma TU).
Let k be thick-type and put tau_k(j) := sgn(a_p v_k(p) v_k(j)).  A coordinate j in FW_k is HELPFUL for k if z_j tau_k(j) <= 0 and either
j notin F, or j in F with |a_j| <= x'_max.  The PLACEMENT at a helpful j: if j in F, lower a_j to 0 (same-sign lowering, Q2 Lemma LT);
then put support of sign tau_k(j) and mass m_j := 24 lambda_k |v_k(j)| at j.  (If k is zero-data and j notin F one may instead move z_j
to tau_k(j) without mass.)  Then:
 (i) ADMISSIBILITY.  At the companion the data at j are V_t(j) = c_k(t) v_k(j) + (fine, total <= C c_{L+1}); if c_k(t) v_k(j) has the sign
     tau_k(j) (aligned) the new support coordinate imposes no constraint; otherwise (anti-sign) |c_k(t) v_k(j)| t <= C_+ m_j for all
     scales t of the class, exactly as at V1's pulls (the pull mass 24 lambda v_l(j) dominates the data, V1 Lemma TU / K1 2.1(b)); zero-
     data carriers impose nothing.  After the deep raise every far support coordinate has |a^r_j| >= 8 lambda_k |v_k(j)| (K1 1.2), so the
     lowering step never meets a coordinate that Lemma P would pin (K1 Lemma K1.3 is a statement about the raised row and is unaffected:
     j becomes a support coordinate whose data are aligned or mass-dominated).
 (ii) COST.  p*-cost <= C(|a_j| + m_j) + C_f lambda_k |v_k(j)| log(e/|v_k(j)|) <= C Design(L) x'_max log(1/T) (Z3 Lemma 3.1, Q2 Lemma
     LT); summed over at most |Lambda_L| placements this is K1-ref R-6's budget, so theta'/c_flat^2 -> 0 is kept.
 (iii) ACTION.  For every unit y, the placement changes y^T Ft(R_1 + Pi) by
      Delta_j(y) = coef^y_k v_k(j) (tau_k(j) - z_j) + err_j,    |err_j| <= C (c_{L+1} + Design(L)^C x'^2_max + mu_j Design x'_max),
     and every column of the generator set by at most C Design(L)^C x'_max.
Proof.  (iii) J1.1(c): the z-change at j acts by Dev_Psi(j)(tau - z_j) = Psi(j)(tau - z_j) (a_j = 0 after the lowering; before it, the
lowering is a mass change at j with efficiency mu_j^2/nu <= mu*_{D(L)+1}^2, negligible); Psi(j) = coef_k v_k(j) + (fine part) since j is
private to k among coarse carriers.  The mass m_j moves e by <= mu_j m_j/nu.  Second-order terms of K2.8(b) are <= C Design^C |Delta val|^2
with |Delta val| <= 2|v_k(j)| <= 2 x'_max.  Generators are C^{1,1} functions of the row with constants Design^C (K2.4, K2.9 proof).  (i), (ii)
as stated (the references prove exactly these estimates for pulls; for an aligned placement the data impose nothing).  QED

## 2.3 Theorem J1.7 (one helpful far coordinate of one thick-type carrier makes Step A A-regular).  PROVED (modulo the cited chain).
Let C_J := C_A + 4.  If at the stage (L, w, a) some thick-type coarse carrier k has a helpful coordinate j in FW_k, then after adding the
placement at j to the pre-placements Pi, Step A is A-regular (in the sense of K2.9 with W' := Design^{C_A} u^{-3} max(x, ||b'||), b' the
new right-hand side, ||b'|| <= ||b|| + 3 x'_max) and is realized by K2.9(c) with the frozen-status convention K-8.
Proof.  Let R' := R_1 + Pi + (placement).  Suppose the stage at R' is not A-regular.  By K2.9(b) there is a near-certificate y at R' of
size eps < 4 Design^{-C_A} with phi'_y := y^T Ft(R') > -rho'_0, rho'_0 = C_2 W'^2.  By J1.6(b)(iii) the columns at R' and at R_1 + Pi differ
by <= C Design^C x'_max << Design^{-C_A}, so y is a near-certificate of size <= 2 eps <= eps_* at R_1 + Pi, and J1.6(a) applies:
coef^y_k = kappa_y a_p/v_k(p) + O(eps Design^2), kappa_y <= -c_*/nu_1.  Then, since tau_k(j) = sgn(a_p v_k(p) v_k(j)) and z_j tau_k(j) <= 0,
      coef^y_k v_k(j) (tau_k(j) - z_j) = kappa_y |a_p/v_k(p)| |v_k(j)| (1 - tau_k(j) z_j) + O(eps Design^2 x'_max)
                                       <= -(c_* u/(2 nu_1)) |v_k(j)| + O(eps Design^2 x'_max)
(1 - tau z_j >= 1).  Hence, with phi_y := y^T Ft(R_1 + Pi), |phi_y| <= |Lambda_A|^{1/2} max(x, ||b||) (each |Ft_l| <= max(x, ||b||_inf)),
      phi'_y = phi_y + Delta_j(y) <= |Lambda_A|^{1/2} max(x, ||b||) - (c_* u/(2 nu_1)) Design^{C_J} x/u + |err_j| + O(eps Design^2 x'_max) < -rho'_0,
because Design^{C_J} c_*/(2 nu_1) >> |Lambda_A|^{1/2} Design (||b|| <= |Lambda_A|^{1/2} max(x, ...) and x = C Design eta'), the errors are
<= C(c_{L+1} + Design^C x'^2_max) << x, and rho'_0 = C_2 Design^{2 C_A} u^{-6} max(x, ||b'||)^2 <= C_2 Design^{2C_A} u^{-6} (3 x'_max)^2 << x
(x'^2_max = u^4 T^6/(Design^4 |Lambda|^2) while x >= c T^4/L).  Contradiction.  The realization bounds of K2.9(c) hold with W' <= Design^{C_A}
u^{-3} 3 x'_max = 3 Design^{C_A - 2} u^{-1} T^3/|Lambda|: moves <= W' << u, cost <= C_f Design^C W' log(1/W') = o(u^2 T^2) (indeed / (u^2 T^2) <=
C Design^{C} T log(1/T)/u^3 -> 0).  QED
Remarks.  (1) Theorem J1.7 makes K2.11 and K2 5.5's "Moreover" rigorous for thick-type carriers, with the overshoot handled by the
sign-uniformity of J1.6(a): the placement lowers phi_y for ALL near-certificates simultaneously, so no new certificate can appear (the
point K2.11 left open).  (2) For data-carrying carriers without thick private coordinates the analogous placement is a pull of sign
-eps_k; a pullable far coordinate together with the carrier's bank is K1's TU lever, already a two-sided generator in K2 (kind (i));
nothing new.  (3) The window FW_k can be replaced by any window [Design^{C_J} x/u, x''] with x'' <= x'_max; only the cost bookkeeping uses
x'_max.

## 2.4 The frozen-window residual.  PROVED (as a necessary condition for non-A-regularity).
Combining J1.7 with K2.16/K2.17 and K1's TU: if Step A is not A-regular at (L, w, a) for every choice of pre-placements, then
 (FW) every thick-type coarse carrier k has a FROZEN far window: for every j in FW_k, either z_j = tau_k(j) = sgn(a_p v_k(p) v_k(j)) (j is a
      support coordinate continuing the sign of the proportional profile a ~ (a_p/v_k(p)) v_k, or a contact of that sign), or j in F,
      sgn a_j = -tau_k(j) and |a_j| > x'_max (super-thick against the profile);
 (U) every data-carrying non-thick-type carrier with a robust coefficient is unpullable on FW_k (K2's (U)-carriers);
 and a near-certificate of K2.16's structure exists (types (A*), (U*)), with the normal form of J1.3.
Discussion.  (FW) is satisfied by the "proportionally swallowed" rows a = sum_k rho_k v_k on S_k (all of S_k), the configuration of
U2 Lemma ND; for data-carrying carriers it says: anti-aligned carriers (sgn(a_p v_k(p)) = -eps_k) have their far windows already
"pulled" (anti-data-sign support), aligned carriers have far data-sign contacts or data-sign support (their natural state).  So far moves
alone cannot settle Step A; they remove every configuration in which some thick-type carrier has a far coordinate (in its window) of
the "wrong" sign or a cheaply flippable one.
