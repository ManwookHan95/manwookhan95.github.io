# Z5 referee notes: assembled proofs of the fixes and of the extension (Theorem R1)

Numbering/notation: paper/martin_density_note.tex ("the note") and r5/Z5_notes.md ("Z5"). Part files: r5/Z5_ref_part0..4.md.
Script: r5/Z5_ref_work/check_deep_assignment.py. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Throughout: I finite; for the SLD statements T is the operator of Definition def:SLD, N >= 1, p = p_N. For f in S_{p*} with forced
data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a may be infinite, s_j := sgn a_j (j in F), v_l := delta_l h_l / n_l, and
f^+_j := (-s_j B_+(j) - |a_j|/t)_+, f^-_j := (s_j B_-(j) - |a_j|/t)_+ for a two-sided decomposition (B_+-, Theta_+-) at scale t
(Lemma lem:flip: sum_F f^+_j <= t/(4q_0), sum_F f^-_j <= t/(4q_0)).

## 1. Verdict summary (details in Z5_referee.md)
T1-T5, T6, T8-T11, T13a: correct (PROVED). T7: correct; the gloss of (W^c) needs a correction (1.1). T12: correct; Example 6.2 is
covered more simply by T5 (Section 3), and the (B_res) extension needs the note's Lambda*_f (Section 4). T14, T15: arithmetic correct,
conclusions overclaimed (Section 5). T16: correct (trivial). New: Theorem R1 (Section 2) replaces cushion domination (H4-inf) by
cushion sparsity (CS_B) in Theorem S-inf, covering part of the "fast support swallowing" case that Z5 lists as open.

1.1 (W^c) (Z5 Theorem 3.6). If sgn a is constant on S_l cap F and r_l = 0, then r_l^{[M]} = 0 for EVERY M (the sign sigma = -sgn a
annihilates all far support terms, and S_l \ F contributes 0), so (W^c) fails. (W^c) can only help when a is sign-mixed on the
swallowed signature set (and then it needs super-fast decay). Theorem 3.6 itself is correct.

1.2 Lemma lem:rigidity(a) as stated (b_+ - b_- in c_00) holds for every F; what fails at infinite F is uniqueness of data whose base
parts lie in l_1(F cup K) (e.g. u_l with supp u_l contained in F). Z5's correction of Lemma lem:boundedfree (T10) is right and corrects
the Round-4 referee (Z1_ref_notes.md, "F finite is essential (Y may contain a)").

## 2. Theorem R1: cushion sparsity suffices. PROVED.

Definitions (Z5 Section 6): r_l := min_{sigma = +-1} sum_{s in S_l \ F} v_l(s)(1 + sigma z_s); B := {l in L_N : r_l = 0};
B_K := {l in B : S_l \ F infinite}, B_F := B \ B_K; eps_l (z == eps_l on S_l \ F; eps_l := 1 if S_l \ F is empty);
tau_l := -eps_l Delta theta_l; q_l := eps_l Phi_{m(l)}(k(l)) w_{m(l)}(k(l))/(m(l) C_{m(l)}); for good l, S*_l := S_l \ (F cup
U_{l' in B, l' > l} supp y_{l'}), r*_l := min_sigma sum_{S*_l} v_l(s)(1 + sigma z_s), Lambda*_f(l) := prod_{l'' <= l, l'' good}(1 + 3/r*_{l''}).
(W*): r*_l > 0 for good l and liminf_l Lambda*_f(l)/(l 2^{l^3} Lambda°(l)) = 0. (H2): every block has a non-degenerate peak k with
j(k,m) notin B. (H3-inf): no l in B_K at a degenerate peak with sgn w_{m(l)}(k(l)) = eps_l; no l in B_F at a degenerate peak.
(B_fin): B finite. New: U_B(j) := sum_{l in B}|u_l(j)|, m_B(y) := sum{U_B(j) : j in F, |a_j| < y U_B(j)},
  (CS_B)  m_B(y) = o(y) as y -> 0+.

Lemma R0. Under (B_fin): (a) (H4-inf) [sup_{l in B} sup_{j in F}|u_l(j)|/|a_j| = c_B < infinity] implies (CS_B); (b) (CS_B) holds iff
m_l(y) := sum{v_l(j) : j in S_l cap F, |a_j| < y v_l(j)} = o(y) for every l in B with S_l cap F infinite.
Proof. (a) U_B <= |B| c_B |a| on F, so the defining set is empty for y < 1/(|B| c_B). (b) T_y := U_{l in B} supp y_l is finite. By (P1),
on S_l \ T_y (l in B) U_B = v_l, and off U_{l in B} S_l, U_B vanishes outside T_y. Each of the finitely many j in F cap T_y has a_j != 0
and leaves the defining set for small y. QED

Lemma R2 (one-sided transfer expansion with sparse flips; any admissible T, any f). Let U_* in l_1, U_* >= 0, with
m_*(y) := sum{U_*(j) : j in F, |a_j| < y U_*(j)} = o(y). For eps_tr > 0, A_0, A_2, C_* >= 1 and gamma_B in (0,1] there are
c_flat in (0, 1/12] and t_1 > 0 such that for every t in (0, t_1] and every side-+ (resp. side--) admissible pair (b, omega)
(Definition def:twopiece read at arbitrary F) with b(zhat) = 0, t||b||_1 <= A_0, Gamma_w(b, omega) <= 2, every k in supp omega_m
satisfying [gap_m(k) >= t^2 and |omega_m(k)| <= 2 gap_m(k)/t] or [gap_m(k) >= gamma_B and |omega_m(k)| <= A_2/t], and
  (s_j b_j)_- <= 3|a_j|/t + C_* U_*(j)   [resp. (s_j b_j)_+ <= 3|a_j|/t + C_* U_*(j)]   for all j in F,
the functional g := b + sum_m R_m*(omega_m - d_m(omega_m) w_m) satisfies p*(f + r g) <= 1 + (r^2/2)(Gamma_w(b, omega) + eps_tr) for
0 < r <= c_flat t [resp. -c_flat t <= r < 0].
Proof (side +; side - is the same with -b). By Lemma lem:bookkeeping(b) and (eq:baseidentity), G_b(a + rb) = Exc(rb) +
nu Psi(r U*b/nu), and Exc(rb) = sum_{j in F} 2(r beta_j - |a_j|)_+ with beta_j := (s_j b_j)_- (off F the side condition makes every
summand 0; on F use |x + y| - |x| - sgn(x) y = 2(-sgn(x) y - |x|)_+ and -s_j r b_j <= r beta_j). Since 3r|a_j|/t <= |a_j|/4, a positive
summand forces r C_* U_*(j) > 3|a_j|/4, and then 2(r beta_j - |a_j|)_+ <= 2(|a_j|/4 + r C_* U_*(j)) <= 3 r C_* U_*(j). Hence
Exc(rb) <= Fl_*(r) := 3C_* r m_*(2C_* r), and Fl_*(r)/r^2 -> 0 as r -> 0, independently of t and of (b, omega). Fix r_0 with
Fl_*(r) <= r^2 for 0 < r <= r_0. Now run the proof of Lemma lem:onesidedtransfer with Ghat_b := (r^2/2)h(b)(1 + K'_A c_flat) + Fl_*(r)
(||r U*b||/nu <= c_flat ||U|| A_0/nu <= 1/2, K'_A := 2||U||A_0/nu): the bound |eps_m| <= K_3 r^2 for the rebalancing amounts holds with
K_3 depending on f only (now also using Fl_* <= r^2); the error term |lambda|(|q*(A) - 1| + q*(A - a)) <= 2|lambda|(1 + ||U||)c_flat A_0;
the blocks and transfer data are unchanged. The only new contribution to Gammahat is q_0 Fl_*(r). Choose eta_1, c_flat as there, then
t_1 <= r_0/c_flat so small that q_0 Fl_*(r) <= (eps_tr/4)(r^2/2) and the r^4-terms are <= (eps_tr/4)(r^2/2) for 0 < r <= c_flat t_1. QED

Theorem R1. For the SLD operator and every N, every f in S_{p_N*} (F arbitrary) satisfying (W*), (H2), (H3-inf), (B_fin) and
(CS_B) belongs to Rec. By Lemma R0(a) this contains Theorem S-inf of Z5 (T12).

Proof. Fix g in C(f) and rho in (0,1); choose eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2, kappa_0 := (sqrt(1 + eta_0/2) - 1)/2,
eps_tr := eta_0/2, eta <= eta_* with eta_Gamma(eta) <= 1 and sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0. Let l_* >= l_f := max(max B,
max_m l°_m) (l°_m: a good non-degenerate peak of block m, (H2)), t in W(l_*), t <= min(t_eta, 1), (B_+-, Theta_+-) a two-sided
decomposition at scale t, K* := (1/q_0 + 22) Lambda*_f(l_*). Constants C_f, C_U, C_tau, K_kappa, A^R_0, A_2 depend only on f, N and
the design; K^R_2, K^R_4 are such constants times Lambda*_f(l_*).

Step 1 (pinning of good carriers; Z5 Step 1). sum_{l notin B}|Delta theta_l| <= K* t and sum_{l > l_*}|Delta theta_l| <= 6t^2
(Lemma lem:modswallow(a): for good l and s in S*_l, -Delta B(s) = Delta theta_l v_l(s) + sum_{l' > l good} Delta theta_{l'} y_{l'}(s)/n_{l'};
sum of phi_{z_s} over S*_l; E_l := sum_{S_l \ F} phi_{z_s}(Delta B(s)) has sum_l E_l <= t/q_0 by Lemma lem:switchbudget; unroll over good
indices). Lemma lem:badpeaks (a)-(c) hold (they use only Lemma lem:peakshift, (eq:didentity), Step 1 and (H2)).

Step 2 (exact switching; Z5 Step 2 = note's Lemma lem:exactswitch, (B_fin) case, with no sign condition for l in B_F). There is
tau' in R^B with tau'_l = 0 for l in B_pk (bad peaks), sum_{m(l)=m} q_l tau'_l = 0 for every m, V' := sum_{l in B} eps_l tau'_l u_l 1_{F^c}
z-signed and supported in K, sum_B |tau_l - tau'_l| <= C_f K* t and ||Delta B 1_{F^c} - V'||_1 <= C_f K* t.

Step 2' (bounded switching). By Lemma 5.2 of Z5 (T10; valid at every F: the map c -> (P^perp U* sum_U c u, (sum_U c u)(zhat)) is
injective, |Delta B(zhat)| <= t/q_0, ||P^perp U* Delta B|| <= 2(2nu/q_0)^{1/2}) with U := {(k(l), m(l)) : l in B},
|Delta theta_l| <= C_U(1 + ||sum_{l notin B} Delta theta_l u_l||_1) <= C_U(1 + K* t) (l in B). Assume K* t <= 1 and C_f K* t <= 1; then
|tau'_l| <= 2C_U + 1 =: C_tau. Put X := sum_{l in B} eps_l tau'_l u_l. Then X 1_{F^c} = V', |X_j| <= C_tau U_B(j) for every j, and
Delta B - X = sum_{l in B} eps_l(tau_l - tau'_l) u_l - sum_{l notin B} Delta theta_l u_l, so ||Delta B - X||_1 <= (C_f + 1) K* t.

Step 3 (exact two-piece data with deep coordinates). Let chi, e_+- be given by Lemma lem:split for e := Delta B 1_{F^c} - V':
B_+ 1_{F^c} = chi V' + e_+, B_- 1_{F^c} = -(1 - chi)V' + e_-, ||e_+-||_1 <= C_f K* t + t/q_0. For j in F put A_j := 2|a_j|/t and
D_t := {j in F : s_j X_j < -2A_j}. Define b^+_1 := 0 off F and, for j in F:
  j notin D_t: x_j := s_j B_+(j), y_j := s_j(B_+(j) - X_j); the interval [y_j - A_j, x_j + A_j] is nonempty (x_j - y_j = s_j X_j >= -2A_j);
               sigma_j := its point closest to 0; b^+_1(j) := B_+(j) - s_j sigma_j;
  j in D_t:    b^+_1(j) := -s_j A_j.
Claim 3.1. For j in F: (i) |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B - X)_j|; (ii) s_j b^+_1(j) >= -A_j; (iii) s_j(b^+_1 - X)(j) <= A_j
if j notin D_t, and = |X_j| - A_j <= |X_j| if j in D_t; (iv) |b^+_1(j)| <= A_j + |X_j|.
Proof. We use s_j B_+(j) >= -|a_j|/t - f^+_j, s_j B_-(j) <= |a_j|/t + f^-_j (definitions), A_j >= |a_j|/t, and B_+ - X = B_- + (Delta B - X).
If j notin D_t: (ii), (iii) are x_j - sigma_j >= -A_j and y_j - sigma_j <= A_j. The point of [y - A, x + A] closest to 0 has modulus
(-x - A)_+ + (y - A)_+ (if x + A < 0 it is x + A; if y - A > 0 it is y - A; otherwise 0). Here (-x_j - A_j)_+ <= f^+_j and
(y_j - A_j)_+ <= (s_j B_-(j) - |a_j|/t)_+ + |(Delta B - X)_j| = f^-_j + |(Delta B - X)_j|: (i). For (iv), -A_j <= s_j b^+_1(j) = x_j - sigma_j
<= x_j - y_j + A_j = s_j X_j + A_j. If j in D_t (so s_j X_j = -|X_j| and |X_j| > 2A_j): (ii), (iv) are clear and (iii) is an identity.
For (i): s_j B_+(j) + A_j >= A_j - |a_j|/t - f^+_j >= -f^+_j, and s_j B_+(j) = s_j B_-(j) + s_j X_j + s_j(Delta B - X)_j <= |a_j|/t + f^-_j
- |X_j| + |(Delta B - X)_j| <= -A_j + f^-_j + |(Delta B - X)_j| (because |X_j| > 2A_j >= A_j + |a_j|/t). Hence |s_j B_+(j) + A_j| <=
f^+_j + f^-_j + |(Delta B - X)_j|, and |B_+(j) - b^+_1(j)| = |s_j B_+(j) + A_j|. QED
Consequently ||B_+ 1_F - b^+_1||_1 <= t/(2q_0) + (C_f + 1)K* t. [Checked on 4e5 random instances, check_deep_assignment.py.]
Put kappa := (b^+_1 + chi V')(zhat), b^+ := b^+_1 + chi V' - kappa a, b^- := b^+ - X (no truncation of b^+_1). In block m let
omega^+_m := omega^c_m (Definition def:windowcert) off {k(l) : l in B_np} (B_np := bad strict non-peaks), omega^+_m(k(l)) :=
omega_{+,m}(k(l)) for l in B_np, omega^-_m := omega^+_m + sum_{l in B_np, m(l)=m} (eps_l tau'_l/lambda_l) e_{k(l)}, and
g_t := b^+ + sum_m R_m*(omega^+_m - d_m(omega^+_m) w_m). Since B_+ = B_+ 1_F + chi V' + e_+, (b^+_1 + chi V')(zhat) = B_+(zhat) - e_+(zhat)
- (B_+ 1_F - b^+_1)(zhat), so by Lemma lem:budget(a) and ||zhat||_inf <= 1 + ||U||, |kappa| <= K_kappa t with K_kappa = O(K*).
Claim 3.2 (assume K* t, C_f K* t, K_kappa t^2 <= 1, t <= 1). (a) (b^+, omega^+) is side-+ admissible and (b^-, omega^-) side--
admissible (off F they are chi V' and -(1-chi)V'); both represent g_t: b^+ - b^- = X = sum_{l in B_np} eps_l tau'_l u_l =
sum_m R_m*(omega^-_m - omega^+_m) (tau'_l = 0 on B_pk) and d_m(omega^-_m) - d_m(omega^+_m) = sum_{m(l)=m} q_l tau'_l = 0 (d-neutral);
b^+(zhat) = 0, hence b^+(xi) = 0 = b^-(xi) (Lemma lem:algebra). (b) On F, with |kappa||a_j| <= |a_j|/t:
(s_j b^+_j)_- <= 3|a_j|/t; (s_j b^-_j)_+ <= 3|a_j|/t for j notin D_t and <= |X_j| <= C_tau U_B(j) for j in D_t (there s_j b^-_j =
|X_j| - A_j - kappa|a_j|); |b^+_j| <= 3|a_j|/t + C_tau U_B(j); |b^-_j| <= 3|a_j|/t + 2C_tau U_B(j). Hence every
beta in {(s b^+)_-, (s b^-)_+, |b^theta|} (b^theta := (b^+ + b^-)/2) satisfies beta_j <= 3|a_j|/t + 2C_tau U_B(j) on F.
(c) t||b^+-||_1 <= A^R_0 := 3 + 3C_tau |B| (sum_F A_j <= 2/t, ||U_B||_1 <= |B|, ||X||_1 <= C_tau |B|).
(d) B_+ - b^+ = e_+ + (B_+ 1_F - b^+_1) + kappa a; off F, B_- - b^- = e_-; on F, B_- - b^- = (B_+ - b^+) - (Delta B - X); all are O(K* t) in
l_1. The block parts are compared with Theta_+- exactly as in the proof of Lemma lem:windowtwopiece (b), (c) (which uses Lemma lem:suplevel,
Lemma lem:box, (P2), Steps 1-2 and |omega^+-_m(k)| <= A_2/t). Hence ||g - g_t||_1 <= K^R_2 t and
Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + K^R_4 t)^2 (sqrt(Gamma_w) is a seminorm on data, Lemma lem:budget(d)).
(e) supp omega^+-_m satisfies (d) of Lemma lem:windowtwopiece with gamma_B > 0 ((B_fin)) and A_2 := 4 + C_tau/lambda_B,
lambda_B := min_B lambda_l (|tau'_l| <= C_tau).

Step 4. For t also satisfying K^R_4 t <= kappa_0 and t <= t_1, Lemma R2 (U_* := U_B, C_* := 2C_tau, A_0 := A^R_0, A_2, gamma_B) applies
to the + data for 0 < r <= c_flat t and to the - data for -c_flat t <= r < 0; both represent g_t and have Gamma_w <= (1 + 2kappa_0)^2 =
1 + eta_0/2 <= 2. So p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t, and p*(g - g_t) <= (1 + ||U||)K^R_2 t.

Step 5. By (W*) choose window indices l_1 < l_2 < ... with Lambda*_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0; by (P3),
Lambda*_f(l_j) T_hi(l_j) -> 0 and n^w_{l_j}/Lambda*_f(l_j) -> infinity, so for large j all dyadic scales t_i := T_hi(l_j) 2^{1-i}
(1 <= i <= n_j := n^w_{l_j}) satisfy the smallness conditions of Steps 2-4, and K_j := (1 + ||U||)K^R_2 satisfies
n_j >= 24 rho^2 K_j/(c_flat(1 - rho^2)), K_j T_hi(l_j)/n_j -> 0. Lemma lem:avgfunctionals gives rho gbar_j in C(f) and rho gbar_j -> rho g,
gbar_j := (1/n_j) sum_i g_{t_i}. The averaged data Dbar_j := (1/n_j) sum_i D_i (D_i the data of Step 3 at t_i) are two-piece data of gbar_j
(side conditions and representations are linear), d-neutral, with kappa_w(Dbar_j) <= 1 + eta_0/2 (convexity of Gamma_w), so
kappa_w(rho Dbar_j) <= rho^2(1 + eta_0/2) <= 1. (CS-data) for rho Dbar_j: by Claim 3.2(b) and convexity of x -> x_+, x_-, |x|, each
beta in {|bbar^theta|, (s bbar^+)_-, (s bbar^-)_+} satisfies beta_j <= 3|a_j|/T_lo(l_j) + 2C_tau U_B(j) on F. For 0 < x <= T_lo(l_j)/6,
|a_j| < x beta_j gives |a_j| < |a_j|/2 + 2x C_tau U_B(j), i.e. |a_j| < 4x C_tau U_B(j), and then beta_j <= 4C_tau U_B(j); so
m_beta(x) <= 4C_tau m_B(4C_tau x) = o(x). Z5 Theorem 4.3 under (CS-data) (Proposition 4.8 of Z5_part4b; T8), with I_- empty, gives
(f, rho' rho gbar_j) in cl NA for every rho' < 1, hence (f, rho gbar_j) in cl NA. Let j -> infinity, then rho -> 1. QED

Remark R1.1 (scope). Model: v_l(j) ~ 2^{-j} on S_l (bounded gaps), |a_j| ~ 2^{-(1+beta)j} on S_l cap F: m_l(y) ~ y^{1/beta}, so (CS_l)
iff beta < 1. Ratios varrho_l(j) = |a_j|/v_l(j) = 1/j or 2^{-sqrt j} are covered. T12 needed inf varrho_l > 0. Script: Fl(r)/r^2 at
r = 0.05t -> 0 for beta = 0.5, 0.9; ~1.4 (constant) at beta = 1; grows at beta = 1.5.
Remark R1.2 (non-sparse case; OPEN). If limsup_{y->0} m_l(y)/y > 0 for some l in B, fixed data whose anti-sign part on S_l cap F is
|c| v_l (c != 0) pay flip cost >= r|c| m_l(r|c|/2) at scale r (each j with |a_j| < r|c|v_l(j)/2 contributes >= r|c|v_l(j)), not o(r^2)
along a sequence r -> 0; so averaged window data fail (CS-data) unless the constrained-direction switching vanishes. By Lemma 7.1 of Z5
the constrained amplitude is <= D*_l(t) (-> 0 if beta > 1, but not O(t)); the free direction creates no deep coordinates.
Remark R1.3 (cushions are better than near-contacts). A support coordinate is a contact whose anti-sign use is free up to 2|a_j|/t:
the allowance grows as t -> 0, and sparse violations cost o(r^2) (Theorem R1). A near-contact (room eps_j > 0 fixed) penalizes use in
both directions at first order (phi_z(x) >= eps_j|x|); fixed two-piece data cannot use it, and an engineered approximant can make it a
contact only while eps_j <= s_1 (cost <= s_1||u||_1 in (E2)), which fails at late stages for each fixed j. So Theorem R1 has no
analogue for near-contact tails: Z5's identification of (O4)(b) with (O1)(i) ("allowance 2|a_j|/t <-> room 1 - |z_j|") is HEURISTIC
and imperfect; the support version is strictly better behaved.

## 3. First-order pinning; Example 6.2 is window-pinned. PROVED.
Lemma R3 (any admissible T, any f). For a two-sided decomposition at scale t <= min(t_eta, 1):
|sum_{(k,m)} Delta theta_{k,m} u_{k,m}(zhat)| = |Delta B(zhat)| <= t/q_0.
Proof. (eq:DeltaB) and Lemma lem:budget(a) (|q_0 B_+-(zhat)| <= t/2). QED
Hence, if sum_{l != l_0}|Delta theta_l| <= K t and u_{l_0}(zhat) != 0, then |Delta theta_{l_0}| <= (1/q_0 + K)t/|u_{l_0}(zhat)|
(|u_l(zhat)| <= q*(u_l) q**(zhat) = 1). For the SLD, u_l(zhat) = 0 iff l is d-neutral ((R_m** xi)(k) = lambda_{k,m} q_0 u_{k,m}(zhat) and
Lemma lem:threshold).
Example 6.2 of Z5 (a = u_{l_0}, z = sgn a on F, 0 off F): u_{l_0}(zhat) = a(zhat) = 1, and the good carriers are window-pinned by Step 1
under (W*) (which holds, as Z5 shows). So sum_l |Delta theta_l| <= (1/q_0 + 2K*)t on every window scale; every mate is window-pinned
and f in Rec by T5, without (H2) or (H3-inf). (Also k(l_0) is a non-degenerate peak.) The example is correct but does not exercise the
exact-switching part of T12; genuine examples need a bad d-neutral carrier (w_{m(l)}(k(l)) = 0) whose signature lies in F.

## 4. (B_res) extension (Z5 Remark 6.3(b)). PROVED with the note's Lambda*_f.
Lemma lem:modswallow(b) unrolls the bad inequalities r*_l (tau_l)_- <= E_l + 2 sum_{good l' > l} pi_{l',l}|Delta theta_{l'}|, r*_l :=
2||v_l 1_{S_l \ F}||_1 > 0 (B_F empty), together with the good ones; the product therefore contains the bad factors. (W*) must be read
with the note's Lambda*_f(l) := prod_{l'' <= l, l'' in L_N}(1 + 3/r*_{l''}). With this reading Z5's argument (tau'_l := (tau_l)_+,
sum_B |tau'_l| <= 2/t, |X_j| <= 2c_B|a_j|/t on F with the uniform c_B, then Z5 Steps 3-5) is correct.

## 5. T14 and T15: correct statements. PROVED.
(a) For every support-swallowed carrier l (S_l \ F finite, S_l cap F infinite) and every K > 0: Phi_l(Kt, t) := sum_{S_l cap F}
(K t v_l(j) - 2|a_j|/t)_+ <= K t m_l(K t^2/2) and m_l(y) -> 0 as y -> 0 (dominated convergence; each varrho_l(j) > 0), so
D*_l(t) >= K t for small t: D*_l(t)/t -> infinity for every support-swallowed carrier (also cushion-dominated ones, where D*_l(t) >=
2 inf varrho_l/t). The model exponent (beta-1)/(beta+1) of Z5 Lemma 7.1(b) is correct for S_l with bounded gaps (Z5_part4b line 30 has
the sign typo (1-beta)/(1+beta)). The conclusion "windowed averaging cannot apply" is FALSE as stated: windowed averaging applies via
exact data under (H4-inf) (T12) and under (CS_B) (Theorem R1); what fails is the derivation of window PINNING from the base budget.
(b) Necessity in T15 holds for ANY two-piece data with b^+ - b^- = X on F: s_j(b^+_j - b^-_j) = s_j X_j < -2A_j forces
(s_j b^+_j)_- > A_j or (s_j b^-_j)_+ > A_j. "Fixed data reproducing deep flips pay a first-order cost" is true per coordinate, but the
total cost 2|r| sum{beta_j : |a_j| < |r| beta_j} is o(r^2) under cushion sparsity when the deep usage is bounded (Theorem R1); the
obstruction is the non-sparse regime (Remark R1.2).

## 6. What remains open for (O4) after Z5 and these notes (SLD, finite I)
Infinite F, f not window-pinned for the mate in question, and one of: (a) room off F decaying too fast ((W^pm)/(W*) fail; the
support-free part of (O1)(i)); (b') finitely many bad carriers, (H2), (H3-inf), (W*) hold, but some bad carrier has non-sparse support
swallowing, limsup_{y->0} m_l(y)/y > 0 (model beta >= 1); (c) infinitely many bad carriers, except (B_res) with uniform cushion domination
(support versions of (O2)/(O3), e.g. F = N with a > 0); (d) (H2) or (H3-inf) fails ((O1)(ii)). Also OPEN: (LSC-trunc) in general
(equivalent, given Lemma Z at finite F, to Lemma Z at infinite F), Theorem thm:onesided at infinite F. No counterexample mechanism.
