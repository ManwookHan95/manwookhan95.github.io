# Z5 part 5: Theorem S-inf: exactly swallowed and support-swallowed signature sets at arbitrary F (finitely many bad carriers)

Setting: SLD operator, N >= 1, I = {1..N}, p = p_N; f in S_{p*} with F arbitrary; s_j = sgn a_j on F; alpha(M) as before.

## 5.1 Definitions (Definition def:swallowed read at arbitrary F, plus support swallowing).
r_l := min_{sigma = +-1} sum_{s in S_l \ F} v_l(s)(1 + sigma z_s) (room OFF the support). Bad set B := {l in L_N : r_l = 0}. For l in B
with S_l \ F nonempty, z == epsilon_l on S_l \ F for a sign epsilon_l (|z| = 1 there); if S_l \ F is empty put epsilon_l := +1.
B_K := {l in B : S_l \ F infinite} (contact-swallowed), B_F := B \ B_K (support-swallowed: S_l \ F finite). Switching amplitudes
tau_l := -epsilon_l Delta theta_l, q_l := epsilon_l Phi_{m(l)}(k(l)) w_{m(l)}(k(l))/(m(l) C_{m(l)}) as in the note.
For good l: S*_l := S_l \ (F cup U_{l' in B, l' > l} supp y_{l'}), r*_l := min_sigma sum_{s in S*_l} v_l(s)(1 + sigma z_s);
Lambda*_f(l) := prod_{l'' <= l, l'' in L_N \ B} (1 + 3/r*_{l''}).
Conditions:
 (W*)   r*_l > 0 for every good l, and liminf_l Lambda*_f(l)/(l 2^{l^3} Lambda°(l)) = 0;
 (H2)   every block m has a peak k with alpha_m(k) != 0 and j(k,m) notin B;
 (H3-inf) no l in B_K has k(l) a degenerate peak with sgn w_{m(l)}(k(l)) = epsilon_l, and no l in B_F has k(l) a degenerate peak;
 (B_fin) B is finite;
 (H4-inf) every bad carrier is cushion-dominated on the support: c_B := max_{l in B} sup_{j in F} |u_l(j)|/|a_j| < infinity.
R_S^inf := {f in S_{p*} : (W*), (H2), (H3-inf), (B_fin), (H4-inf)}. For F finite, (H4-inf) is automatic, B_F is empty, and R_S^inf is
the (B_fin) part of R_S. (H4-inf) only concerns the signature parts on S_l cap F (targets y_l are finitely supported).

Theorem 5.1 (S-inf). For the SLD operator and every N, R_S^inf is contained in Rec. PROVED (proof below, as a list of modifications of
the proof of Theorem thm:S; all lemmas of the note quoted below were checked to hold at arbitrary F, see 2.0).

Example 5.2. Let l_0 be a carrier and a := u_{l_0} (q*(a) = 1), so F = supp y_{l_0} cup S_{l_0} is infinite and a is in Y; let z := sgn a on F
and z := 0 off F. Then S_{l_0} \ F is empty, so l_0 is bad and support-swallowed, (H4-inf) holds with c_B = 1, every other S_l (l != l_0,
meeting F at most in the finite set supp y_{l_0}) has full room off F, and (W*) holds as in Theorem thm:R0 (only finitely many factors
are affected). If (H2), (H3-inf) hold at this f (they concern the block data of f), then f in Rec. Such f are NOT in R_0^inf, R_0^{pm,inf}
or the (W^c)-class (the signature of l_0 lies inside the support), so Theorem 5.1 genuinely covers "infinite F without room".

## 5.2 Proof of Theorem 5.1.
Fix g in C(f), rho in (0,1), and eta_0, kappa_0, eps_tr, eta as in the proof of Theorem thm:S. All statements below are for a window
index l_* >= l_f := max(max B, max_m l°_m) (l°_m from (H2)) and t in W(l_*) with t <= min(t_eta, 1); (B_+-, Theta_+-) is a two-sided
decomposition at scale t; K* := (1/q_0 + 22) Lambda*_f(l_*).

Step 1 (pinning modulo bad carriers). Lemma lem:modswallow(a) holds verbatim: sum_{l notin B}|Delta theta_l| <= K* t and
sum_{l > l_*}|Delta theta_l| <= 6t^2 (its good inequalities only use S*_l, which is disjoint from F, Lemma lem:switchbudget and (P1)).
Lemma lem:badpeaks (a)-(c) hold verbatim (they use Lemma lem:peakshift, (eq:didentity), Lemma lem:modswallow(a) and (H2)); under (B_fin)
and l_* >= max B the hypothesis of (b) holds.

Step 2 (exact switching; Lemma lem:exactswitch in the (B_fin) case). Let T_0 := U_{l in B} supp y_l cup U_{l in B_F}(S_l \ F) (finite),
L_j(tau) := sum_{l in B} epsilon_l tau_l u_l(j), c(tau) := sum_{j notin F} phi_{z_j}(L_j(tau)). For j notin F cup T_0 the only bad vector that
can be nonzero at j is the signature of the l in B_K with j in S_l (by (P1): other signatures vanish, bad targets vanish off T_0, and
signatures of l in B_F vanish off F cup T_0), where z_j = epsilon_l; so
  c(tau) = sum_{l in B_K} 2(tau_l)_- m_l + sum_{j in T_0 \ F} phi_{z_j}(L_j(tau)),   m_l := ||v_l 1_{S_l \ (F cup T_0)}||_1 > 0.
Let Z_f be the polyhedral cone in R^B given by: tau_l >= 0 (l in B_K); z_j L_j(tau) >= 0 (j in T_0 cap K); L_j(tau) = 0
(j in T_0 \ (F cup K)); tau_l = 0 (l in B_pk := {l in B : k(l) in P_{m(l)}}); sum_{m(l) = m} q_l tau_l = 0 (m in I). [For l in B_F no sign
condition is imposed: the switching of a support-swallowed carrier has no contact part off T_0.] Every tau in Z_f has c(tau) = 0, and
c(tau) >= 2 sum_{B_K} m_l (tau_l)_- + 2 sum_{T_0 cap K}(z_j L_j(tau))_- + sum_{T_0 \ (F cup K)}(1-|z_j|)|L_j(tau)|, so Hoffman's bound gives
dist_1(tau, Z_f) <= C_H(C_0 c(tau) + sum_{B_pk}|tau_l| + sum_m|sum_{m(l)=m} q_l tau_l|) with C_H, C_0 depending only on f.
For the actual amplitudes: Delta B 1_{F^c} = L(tau) 1_{F^c} + e_0, e_0 := -sum_{l notin B} Delta theta_l u_l 1_{F^c}, ||e_0||_1 <= K* t,
so c(tau) <= t/q_0 + 2K* t (Lemmas lem:switchbudget, lem:phicalc(c)). Bad peaks: for l in B_pk, by (H3-inf) either alpha(k(l)) != 0
and |tau_l| <= lambda_l(t/(sigma|alpha(k(l))|) + K_d t), or l in B_K, k(l) is degenerate with sgn w(k(l)) = -epsilon_l, and then
tau_l <= lambda_l K_d t and (tau_l)_- <= c(tau)/(2 m_l) (Lemma lem:badpeaks(c)). The d-sums are O(K* t) by Lemma lem:badpeaks(b).
As K_d <= C'_f K*, there is tau' in Z_f with (a) tau'_l = 0 at bad peaks and sum_{m(l)=m} q_l tau'_l = 0, (b) V' := sum_{l in B}
epsilon_l tau'_l u_l 1_{F^c} z-signed and supported in K, (c) sum_l|tau_l - tau'_l| <= C_f K* t and ||Delta B 1_{F^c} - V'||_1 <= C_f K* t.

Step 3 (window two-piece data at arbitrary F). Let X := sum_{l in B} epsilon_l tau'_l u_l (a finite block combination, X 1_{F^c} = V'),
B_np := {l in B : k(l) in Q_{m(l)}}, and chi, e_+- from Lemma lem:split for e := Delta B 1_{F^c} - V', so that B_+ 1_{F^c} = chi V' + e_+,
B_- 1_{F^c} = -(1-chi)V' + e_-, ||e_+-||_1 <= C_f K* t + t/q_0.
(3a) Bounds on X over F. sum_{l in B}|tau'_l| <= sum_B |tau_l| + C_f K* t <= 6 sum_l lambda_l/t + C_f K* t <= 3/t when C_f K* t^2 <= 1
(Lemma lem:box; sum_l lambda_l <= 1/3). By (H4-inf), |X_j| <= 3 c_B |a_j|/t for j in F. Put C_X := 3c_B and A_j := C_A |a_j|/t with
C_A := max(2, C_X).
(3b) Common shift on F. For j in F let x_j := s_j B_+(j), y_j := s_j(B_+(j) - X_j); then x_j - y_j = s_j X_j >= -C_X|a_j|/t >= -2A_j, so by
Lemma 4.9 there is sigma_j with x_j - sigma_j >= -A_j, y_j - sigma_j <= A_j and |sigma_j| <= (y_j - A_j)_+ + (-x_j - A_j)_+. Since
A_j >= |a_j|/t: (-x_j - A_j)_+ <= f^+_j, and y_j = s_j B_-(j) + s_j(Delta B - X)_j gives (y_j - A_j)_+ <= f^-_j + |(Delta B - X)_j|.
As Delta B - X = sum_{l in B} epsilon_l(tau_l - tau'_l)u_l - sum_{l notin B} Delta theta_l u_l, ||Delta B - X||_1 <= (C_f + 1)K* t, and
  ||sigma||_1 <= t/(2q_0) + (C_f + 1)K* t.
Put b^+_1 := sum_{j in F}(B_+(j) - sigma_j s_j)e_j*. Then on F: s_j b^+_1(j) >= -A_j and s_j(b^+_1 - X)(j) <= A_j, and also
s_j b^+_1(j) <= A_j + s_j X_j, so |b^+_1(j)| <= (C_A + C_X)|a_j|/t.
(3c) Far truncation and balance. Let M_t := min{M : alpha(M) <= t^2}, F_t := F cap [1, M_t], a_t := a 1_{F_t} (a_t(zhat) >= 1/2 for
t^2 <= 1/(2(1+||U||))). Put b^+_2 := b^+_1 1_{F_t}; its omitted part has ||b^+_1 1_{F \ F_t}||_1 <= (C_A + C_X)alpha(M_t)/t <= (C_A + C_X)t.
Let kappa := (b^+_2 + chi V')(zhat)/a_t(zhat) and define
  b^+ := b^+_2 + chi V' - kappa a_t,     b^- := b^+ - X,
  omega^+_m, omega^-_m := as in Lemma lem:windowtwopiece (omega^c_m off the coordinates k(l), l in B_np; omega_{+,m}(k(l)) there;
                          omega^- := omega^+ + sum_{l in B_np, m(l)=m}(epsilon_l tau'_l/lambda_l) e_{k(l)}),
  g_t := b^+ + sum_m R_m*(omega^+_m - d_m(omega^+_m) w_m).
Since B_+(zhat) = (B_+ 1_F + chi V' + e_+)(zhat), we get (b^+_2 + chi V')(zhat) = B_+(zhat) - e_+(zhat) - (sigma s)(zhat) -
(b^+_1 1_{F\F_t})(zhat), so |kappa| <= 2[t/(2q_0) + (1+||U||)(||e_+||_1 + ||sigma||_1 + (C_A + C_X)t)] =: K_kappa t with K_kappa = O(K*).
(3d) Properties. (i) (b^+, omega^+) is side-+ admissible and (b^-, omega^-) side-- admissible: off F, b^+ = chi V' (z-signed, in K) and
b^- = chi V' - V' = -(1-chi)V'; omega^+- finitely supported in Q_m. Both represent g_t: b^+ - b^- = X = sum_m R_m*(omega^-_m - omega^+_m)
(tau'_l = 0 at bad peaks), and d_m(omega^-_m) - d_m(omega^+_m) = sum_{m(l)=m} q_l tau'_l = 0: d-neutral. b^+(zhat) = 0, hence b^+(xi) = 0 and
b^-(xi) = g_t(xi) = b^+(xi) = 0 (Lemma lem:algebra).
(ii) One-sided cushion bounds: for j in F_t, s_j b^+_j = s_j b^+_1(j) - kappa|a_j| >= -(A_j + K_kappa t|a_j|) and s_j b^-_j = s_j(b^+_1 - X)(j)
- kappa|a_j| <= A_j + K_kappa t|a_j|; for j in F \ F_t, b^+_j = 0 and b^-_j = -X_j with |X_j| <= C_X|a_j|/t. With K_kappa t^2 <= 1:
  (s_j b^+_j)_- <= (C_A + 1)|a_j|/t,   (s_j b^-_j)_+ <= (C_A + 1)|a_j|/t,   |b^+-_j| <= (C_A + 2C_X + 1)|a_j|/t   (j in F).
In particular the data are cushion-compatible (Definition 3.1) with C_R := (C_A + 2C_X + 1)/t, and ||b^+-||_1 <= C_b/t with C_b depending
only on f (||V'||_1 <= sum|tau'_l| <= 3/t).
(iii) Closeness and coefficients: B_+ - b^+ = e_+ + (sigma s) 1_F + b^+_1 1_{F\F_t} + kappa a_t has l_1-norm O(K* t); off F,
B_- - b^- = e_-; on F, B_- - b^- = (B_+ - b^+) - (Delta B - X) = O(K* t). The block parts are compared exactly as in the proof of Lemma
lem:windowtwopiece (b),(c) (which uses only Lemma lem:suplevel, Lemma lem:box, (P2), Steps 1-2). Hence ||g - g_t||_1 <= K*_2 t and
Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + K*_4 t)^2 with K*_2, K*_4 = (constant depending on f, N, design) x Lambda*_f(l_*).
The block parts satisfy (d) of Lemma lem:windowtwopiece (gap >= t^2 and |omega(k)| <= 2 gap(k)/t, or k = k(l), l in B_np, gap >= gamma_B,
|omega(k)| <= A_2/t), with gamma_B > 0 by (B_fin).

Step 4 (one-sided transfer expansion at arbitrary F). Lemma lem:onesidedtransfer holds at arbitrary F with the hypothesis
"t||b||_1 <= A_0" replaced by: t||b||_1 <= A_0 and, on F, (s_j b_j)_- <= C_+|a_j|/t for side + [(s_j b_j)_+ <= C_+|a_j|/t for side -],
with c_flat additionally <= 1/(2C_+). Proof: for 0 < r <= c_flat t (resp. -c_flat t <= r < 0) no coordinate of a + r b changes sign on F
(r(s_j b_j)_- <= |a_j|/2 for side +; the free direction never flips), off F the side conditions give zero cost, so
G_b(a + rb) = nu Psi(r U*b/nu), and the rest of the proof of lem:onesidedtransfer (which uses ||r U*b||/nu <= c_flat ||U||A_0/nu and
q*(rb) <= (1+||U||)c_flat A_0) is unchanged. Apply it with C_+ := C_A + 1 and A_0 := C_b.

Step 5 (averaging and engineering). Exactly as in the proof of Theorem thm:S: by (W*) choose windows l_j with Lambda*_f(l_j)T_hi(l_j) -> 0
and n^w_{l_j}/Lambda*_f(l_j) -> infinity; for every dyadic scale t_i of W(l_j) the data D_i of Step 3 give g_i := g_{t_i} with
p*(f + r g_i) <= 1 + (r^2/2)(1+eta_0) for |r| <= c_flat t_i (Step 4 on each side) and p*(g - g_i) <= (1+||U||)K*_2 t_i; Lemma
lem:avgfunctionals gives rho gbar_j in C(f) with rho gbar_j -> rho g. The averaged data Dbar_j are d-neutral two-piece data of gbar_j
with kappa_w(rho Dbar_j) <= rho^2(1 + eta_0/2) <= 1, and they are cushion-compatible with C_R := (C_A + 2C_X + 1)/T_lo(l_j) (each D_i
is, with C_R(t_i) <= C_R(T_lo(l_j)); the bounds of (ii) are preserved by averaging, as (.)_- is convex and the sign conditions are
linear). Corollary 3.3 (d-neutral case, I_- empty) gives (f, rho gbar_j) in cl NA. Let j -> infinity, then rho -> 1. QED

Remark 5.3. (a) Where (H4-inf) is used: only in (3a), to make the exact switching X compatible with the cushions (Lemma 4.9 needs
(s_j X_j)_- <= 2A_j). For a fast-swallowed bad carrier (|a_j|/v_l(j) -> 0 on S_l cap F) X violates the cushions at far support
coordinates and the common shift is impossible (Part 4b, 4.8(ii)).
(b) The class R_S^inf contains first rows with infinite F, with a in Y, and with signature sets inside the support (Example 5.2), none
of which is covered by the room conditions of Part 2.
(c) The resonant/d-neutral case (B_res) of Theorem thm:S with infinitely many bad carriers extends in the same way when B_F is empty
(every bad carrier contact-swallowed), (H1) holds, every bad carrier is resonant and d-neutral, and the bad carriers are cushion-dominated
with a UNIFORM constant c_B := sup_{l in B} sup_{j in F}|u_l(j)|/|a_j| < infinity: Step 2 is then the (B_res) case of the note
(tau'_l := (tau_l)_+, Lemma lem:modswallow(b), which uses S_l \ F only), and in (3a) sum_{l in B}|tau'_l| <= sum_B|tau_l| <= 2/t gives
|X_j| <= 2c_B|a_j|/t on F. PROVED by the same argument. (With support-swallowed resonant carriers, (tau_l)_- is not pinned by contacts;
one needs supp u_l contained in F for such l, and then they impose no constraint at all; we do not pursue this.)
