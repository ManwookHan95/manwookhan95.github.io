# Z5 referee, part 3: Theorem R1 (cushion sparsity replaces cushion domination in Theorem S-inf). PROVED.

Setting: SLD operator, N >= 1, I = {1..N}, p = p_N; f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F arbitrary;
s_j := sgn a_j (j in F); v_l := delta_l h_l/n_l. Notation of Z5 Section 6: r_l (room on S_l \ F), bad set B, B_K, B_F, eps_l,
tau_l := -eps_l Delta theta_l, q_l, S*_l, r*_l, Lambda*_f (product over good l'' only), conditions (W*), (H2), (H3-inf), (B_fin).
New: U_B(j) := sum_{l in B} |u_l(j)|,  m_B(y) := sum{ U_B(j) : j in F, |a_j| < y U_B(j) },
  (CS_B)  m_B(y) = o(y) as y -> 0+   (cushion sparsity of the bad carriers).

Lemma R0. Assume (B_fin). (a) (H4-inf) implies (CS_B). (b) (CS_B) holds iff, for every l in B with S_l cap F infinite,
m_l(y) := sum{ v_l(j) : j in S_l cap F, |a_j| < y v_l(j) } = o(y).
Proof. (a) U_B <= |B| c_B |a| on F, so the defining set is empty for y < 1/(|B| c_B). (b) Let T_y := U_{l in B} supp y_l (finite).
By (P1), for j in S_l \ T_y (l in B): u_l(j) = v_l(j), u_{l'}(j) = 0 for l' != l in B; off U_B S_l, U_B vanishes outside T_y.
On the finite set F cap T_y, a_j != 0, so these j leave the defining sets for small y. QED

Theorem R1. Every f with (W*), (H2), (H3-inf), (B_fin) and (CS_B) is in Rec. (Contains Theorem S-inf of Z5 by Lemma R0(a).)

Proof. Fix g in C(f), rho in (0,1); eta_0, kappa_0, eps_tr, eta as in the proof of thm:S. Window index l_* >= l_f :=
max(max B, max_m l°_m), t in W(l_*), t <= min(t_eta, 1), (B_+-, Theta_+-) a two-sided decomposition of g at scale t,
K* := (1/q_0 + 22) Lambda*_f(l_*). All constants called C_f, C_tau, K_kappa, K^R_2, K^R_4, A^R_0, A_2 depend only on f, N, the design
(and K^R_2, K^R_4 are such constants times Lambda*_f(l_*)).

Step 1 (= Z5 Step 1): sum_{l notin B}|Delta theta_l| <= K* t, sum_{l > l_*}|Delta theta_l| <= 6t^2; lem:badpeaks (a)-(c).
Step 2 (= Z5 Step 2): Hoffman projection tau' in Z_f: tau'_l = 0 on bad peaks, sum_{m(l)=m} q_l tau'_l = 0, V' := sum_B eps_l tau'_l u_l 1_{F^c}
z-signed and supported in K, sum_B |tau_l - tau'_l| <= C_f K* t, ||Delta B 1_{F^c} - V'||_1 <= C_f K* t.
Step 2' (bounded switching; NEW). Lemma 5.2 of Z5 (T10, valid at every F) with U := {(k(l),m(l)) : l in B} gives
|Delta theta_l| <= C_U (1 + ||sum_{l notin B} Delta theta_l u_l||_1) <= C_U(1 + K* t) for l in B. For K* t <= 1 and C_f K* t <= 1:
|tau'_l| <= 2C_U + 1 =: C_tau. Put X := sum_{l in B} eps_l tau'_l u_l. Then X 1_{F^c} = V', |X_j| <= C_tau U_B(j) for all j, and
Delta B - X = sum_B eps_l(tau_l - tau'_l)u_l - sum_{l notin B} Delta theta_l u_l, so ||Delta B - X||_1 <= (C_f + 1) K* t.
Step 3 (exact data with deep coordinates; NEW). chi, e_+- from lem:split for e := Delta B 1_{F^c} - V':
B_+ 1_{F^c} = chi V' + e_+, B_- 1_{F^c} = -(1-chi)V' + e_-, ||e_+-||_1 <= C_f K* t + t/q_0.
For j in F put A_j := 2|a_j|/t and D_t := {j in F : s_j X_j < -2A_j} ("deep" coordinates). Define b^+_1 on F by
  j in F \ D_t:  x_j := s_j B_+(j), y_j := s_j(B_+(j) - X_j); sigma_j := point of [y_j - A_j, x_j + A_j] closest to 0 (nonempty since
                 x_j - y_j = s_j X_j >= -2A_j); b^+_1(j) := B_+(j) - s_j sigma_j;
  j in D_t:      b^+_1(j) := -s_j A_j;
and b^+_1 := 0 off F.
Claim 3.1. For every j in F:
 (i) |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B - X)_j|;   (ii) s_j b^+_1(j) >= -A_j;
 (iii) s_j(b^+_1 - X)(j) <= A_j if j notin D_t, and = |X_j| - A_j <= |X_j| if j in D_t;   (iv) |b^+_1(j)| <= A_j + |X_j|.
Proof. By definition of f^+-_j (lem:flip): s_j B_+(j) >= -|a_j|/t - f^+_j and s_j B_-(j) <= |a_j|/t + f^-_j; also A_j >= |a_j|/t and
B_+ - X = B_- + (Delta B - X). Case j notin D_t: (ii), (iii) are the defining inequalities x_j - sigma_j >= -A_j, y_j - sigma_j <= A_j;
by Lemma 7.4 of Z5, |sigma_j| <= (-x_j - A_j)_+ + (y_j - A_j)_+ <= f^+_j + (s_j B_-(j) - |a_j|/t)_+ + |(Delta B - X)_j|, which is (i);
(iv): -A_j <= s_j b^+_1(j) = x_j - sigma_j <= x_j - y_j + A_j = s_j X_j + A_j. Case j in D_t (s_j X_j = -|X_j|, |X_j| > 2A_j):
(ii), (iv) are clear and (iii) is the identity -A_j + |X_j|. For (i): s_j B_+(j) + A_j >= A_j - |a_j|/t - f^+_j >= -f^+_j, and
s_j B_+(j) = s_j B_-(j) + s_j X_j + s_j(Delta B - X)_j <= |a_j|/t + f^-_j - |X_j| + |(Delta B - X)_j| < -A_j + f^-_j + |(Delta B - X)_j|
(as |X_j| > 2A_j >= A_j + |a_j|/t); so |s_j B_+(j) + A_j| <= f^+_j + f^-_j + |(Delta B - X)_j|. QED
Hence ||B_+ 1_F - b^+_1||_1 <= sum_F (f^+_j + f^-_j) + ||Delta B - X||_1 <= t/(2q_0) + (C_f + 1)K* t.
(No truncation of b^+_1: the tail of X beyond M_t need not be O(t) here.) Balance: kappa := (b^+_1 + chi V')(zhat) (a(zhat) = 1),
  b^+ := b^+_1 + chi V' - kappa a,   b^- := b^+ - X,
and omega^+-_m, g_t := b^+ + sum_m R_m*(omega^+_m - d_m(omega^+_m) w_m) exactly as in Lemma lem:windowtwopiece (B_np := bad strict
non-peaks; omega^- := omega^+ + sum_{l in B_np, m(l)=m} (eps_l tau'_l/lambda_l) e_{k(l)}).
Since B_+ = B_+ 1_F + chi V' + e_+, (b^+_1 + chi V')(zhat) = B_+(zhat) - e_+(zhat) - (B_+ 1_F - b^+_1)(zhat), so by lem:budget(a) and
||zhat||_inf <= 1 + ||U||: |kappa| <= t/(2q_0) + (1+||U||)(||e_+||_1 + ||B_+1_F - b^+_1||_1) =: K_kappa t, K_kappa = O(K*).
Claim 3.2 (assume K* t <= 1, C_f K* t <= 1, K_kappa t^2 <= 1, t <= 1).
 (a) (b^+, omega^+) is side-+ admissible, (b^-, omega^-) side-- admissible (off F: chi V' and -(1-chi)V'); both represent g_t
     (b^+ - b^- = X = sum_m R_m*(omega^-_m - omega^+_m), tau'_l = 0 on bad peaks); d_m(omega^-_m) = d_m(omega^+_m) (sum q_l tau'_l = 0);
     b^+(zhat) = 0, hence b^+-(xi) = 0 (Lemma lem:algebra).
 (b) On F (using |kappa| |a_j| <= |a_j|/t):  (s_j b^+_j)_- <= 3|a_j|/t;  (s_j b^-_j)_+ <= 3|a_j|/t for j notin D_t and <= |X_j| <= C_tau U_B(j)
     for j in D_t (s_j b^-_j = |X_j| - A_j - kappa|a_j| there);  |b^+_j| <= 3|a_j|/t + C_tau U_B(j),  |b^-_j| <= 3|a_j|/t + 2C_tau U_B(j).
     So each of beta in {(s b^+)_-, (s b^-)_+, |b^theta|} satisfies beta_j <= 3|a_j|/t + 2C_tau U_B(j) on F.
 (c) t||b^+-||_1 <= A^R_0 := 3 + 3C_tau|B| (||u_l||_1 <= 1, sum_F A_j <= 2/t, ||X||_1 <= C_tau|B|).
 (d) B_+ - b^+ = e_+ + (B_+1_F - b^+_1) + kappa a; off F, B_- - b^- = e_-; on F, B_- - b^- = (B_+ - b^+) - (Delta B - X); all O(K* t)
     in l_1. The block parts are compared as in Lemma lem:windowtwopiece (b),(c) (Lemma lem:suplevel, Lemma lem:box, (P2), Steps 1-2).
     Hence ||g - g_t||_1 <= K^R_2 t and Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + K^R_4 t)^2.
 (e) Block supports satisfy (d) of lem:windowtwopiece with gamma_B > 0 (B_fin) and A_2 := 4 + C_tau/lambda_B (|tau'_l| <= C_tau).
Step 4 (one-sided transfer expansion with sparse flips; NEW).
Lemma R2. T admissible, I finite, f arbitrary, U_* in l_1, U_* >= 0, with m_*(y) := sum{U_*(j) : j in F, |a_j| < y U_*(j)} = o(y).
For eps_tr > 0, A_0, A_2, C_* >= 1, gamma_B in (0,1] there are c_flat in (0,1/12] and t_1 > 0 such that for t in (0,t_1] and every
side-+ (side--) admissible (b, omega) with b(zhat) = 0, t||b||_1 <= A_0, Gamma_w(b,omega) <= 2, the block conditions of
lem:onesidedtransfer (with A_2, gamma_B), and on F the anti-sign bound (s_j b_j)_- <= 3|a_j|/t + C_* U_*(j)
[(s_j b_j)_+ <= 3|a_j|/t + C_* U_*(j)], the functional g := b + sum_m R_m*(omega_m - d_m(omega_m) w_m) satisfies
p*(f + r g) <= 1 + (r^2/2)(Gamma_w(b,omega) + eps_tr) for 0 < r <= c_flat t [for -c_flat t <= r < 0].
Proof (side +). By (eq:baseidentity)/Lemma lem:bookkeeping(b), G_b(a + rb) = Exc(rb) + nu Psi(rU*b/nu), Exc(rb) = sum_F 2(r beta_j - |a_j|)_+
(beta_j := (s_j b_j)_-; off F the side condition gives 0). As 3r|a_j|/t <= |a_j|/4, a positive summand forces r C_* U_*(j) > 3|a_j|/4 and
is then <= 2r beta_j <= 2(|a_j|/4 + r C_* U_*(j)) <= 3 r C_* U_*(j). So Exc(rb) <= Fl_*(r) := 3C_* r m_*(2C_* r), and Fl_*(r)/r^2 -> 0
INDEPENDENTLY of t and b. Put Ghat_b := (r^2/2)h(b)(1 + K'_A c_flat) + Fl_*(r) and run the proof of lem:onesidedtransfer with this Ghat_b
(rebalancing: |eps_m| <= K_3 r^2 still holds once Fl_*(r) <= r^2; error term |lambda|(|q*(A)-1| + q*(A-a)) <= 2|lambda|(1+||U||)c_flat A_0).
The new contribution to Gammahat is q_0 Fl_*(r); choose t_1 so small that q_0 Fl_*(r) <= (eps_tr/4)(r^2/2) for 0 < r <= c_flat t_1. QED
Apply Lemma R2 with U_* := U_B, C_* := 2C_tau, A_0 := A^R_0, A_2, gamma_B: the + data of Step 3 for 0 < r <= c_flat t, the - data for
-c_flat t <= r < 0 (Claim 3.2(b)); both represent g_t, so p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t, whenever
K^R_4 t <= kappa_0 (then Gamma_w <= (1 + 2kappa_0)^2 = 1 + eta_0/2 <= 2).
Step 5 (averaging and engineering). As in the proof of thm:S / Z5 Step 5: windows l_j from (W*), dyadic scales t_i of W(l_j),
g_i := g_{t_i}, gbar_j := (1/n_j) sum_i g_i; Lemma lem:avgfunctionals: rho gbar_j in C(f) and rho gbar_j -> rho g. The averaged data
Dbar_j are d-neutral two-piece data of gbar_j with kappa_w(rho Dbar_j) <= rho^2(1 + eta_0/2) <= 1. (CS-data) for rho Dbar_j: by
convexity and Claim 3.2(b), every beta in {|bbar^theta|, (s bbar^+)_-, (s bbar^-)_+} has beta_j <= 3|a_j|/T_lo(l_j) + 2C_tau U_B(j); for
0 < x <= T_lo(l_j)/6, |a_j| < x beta_j forces |a_j| < 4x C_tau U_B(j) and then beta_j <= 4C_tau U_B(j); so m_beta(x) <= 4C_tau m_B(4C_tau x)
= o(x). Theorem 4.3/Proposition 4.8 of Z5 (T8 under (CS-data), I_- empty) gives (f, rho' rho gbar_j) in cl NA for all rho' < 1, hence
(f, rho gbar_j) in cl NA; let j -> infinity, then rho -> 1. QED

Remark R1.1 (scope). In the model v_l(j) ~ 2^{-j} on S_l (bounded gaps), |a_j| ~ 2^{-(1+beta)j} on S_l cap F: m_l(y) ~ y^{1/beta}, so
(CS_l) holds iff beta < 1; varrho_l(j) = |a_j|/v_l(j) = 1/j (or 2^{-sqrt j}) is covered. Z5's T12 required inf varrho_l > 0.
Numerical check: Z5_ref_work/check_deep_assignment.py (Claim 3.1 on 4e5 random instances: no violation beyond round-off; flip cost
Fl(r)/r^2 at r = 0.05t: -> 0 for beta = 0.5, 0.9 (slowly), ~1.4 constant at beta = 1, growing at beta = 1.5).
Remark R1.2 (what is still open in (O4)(b)). Non-sparse support swallowing: limsup_{y->0} m_l(y)/y > 0 for a bad carrier. Then fixed
data whose anti-sign part on S_l cap F is |c| v_l (c != 0, any bounded amplitude) have flip cost at scale r of at least
r|c| m_l(r|c|/2) (each j with |a_j| < r|c|v_l(j)/2 contributes 2(r|c|v_l(j) - |a_j|)_+ >= r|c|v_l(j)); if m_l(y_n) >= c'y_n with y_n -> 0,
then at r_n := 2y_n/|c| the cost is >= c'c^2 r_n^2/2, not o(r^2). So averaged data fail (CS-data) unless the constrained-direction
switching vanishes. By (4.1)/Lemma 7.1, the constrained amplitude is <= D*_l(t) -> 0 when beta > 1, but not O(t). The free direction is
harmless (no deep coordinates). Open: exactification for beta >= 1.
Remark R1.3 (the cushion/near-contact analogy is imperfect). A support coordinate is a contact whose ANTI-sign use is free up to
2|a_j|/t: the allowance GROWS as t -> 0, so a fixed coordinate becomes two-sided at small scales, and sparse violations cost o(r^2)
(Theorem R1). A near-contact (|z_j| = 1 - eps_j, eps_j > 0 fixed) penalizes use in BOTH directions at first order (phi_z(x) >= eps_j|x|):
fixed two-piece data cannot use it at all (Definition def:twopiece); an engineered approximant may turn it into a contact only while
eps_j <= s_1 (cost <= s_1||u||_1 in (E2)), which fails at late stages for every fixed j (z'_j -> z_j forces |z'_j| < 1 - eps_j/2), and
then any fixed data using j pay the first-order cost (eps_j/2)|tau||beta_j|. So Theorem R1 has no analogue for near-contact tails, and
(O1)(i)(a) is not "the same" as (O4)(b): the support version is strictly better behaved.
