# G3 part 2: two-sided decompositions at a fixed first row (valid for ANY admissible T)

Throughout this part f in S_{p*} (p = p_N) and g in C(f) are fixed; T is any admissible operator. h(B) := ||P_{e-perp} U*B||^2/nu and
H_m(Omega) := ||P_m-perp D_m Omega||_2^2 / C_m, P_m-perp the orthogonal projection of l_2 onto (D_m w_m)-perp. For a pair (B, Omega) put
  Gamma_w(B, Omega) := q_0 h(B) + sum_m sigma_m H_m(Omega_m).
sqrt(Gamma_w) is a seminorm on l_1 x prod_m l_inf (each term is the square of a seminorm, with positive weights).

## 2.1 Lemma (two-sided decompositions). PROVED.
For every t > 0 there are B_+, B_- in l_1 and Omega_+ = (Omega_{+,m}), Omega_- = (Omega_{-,m}) in prod_{m <= N} l_inf with
  q*(a + t B_+) <= s(t),  N_m(w_m + t Omega_{+,m}) <= s(t),  q*(a - t B_-) <= s(t),  N_m(w_m - t Omega_{-,m}) <= s(t)  (all m),
  g = B_+ + L*Omega_+ = B_- + L*Omega_-.
(A "two-sided decomposition of g at scale t".)
*Proof.* A Fact A gives f + t g = A + L*W with max(q*(A), ||W||_{V*}) = p*(f + t g) <= s(t) (g in C(f)); put B_+ := (A - a)/t,
Omega_+ := (W - w)/t; subtracting f = a + L*w gives t B_+ + t L*Omega_+ = t g. Same with -t. QED.

## 2.2 Lemma (uniform smallness). PROVED.
For every eta > 0 there is t_eta > 0 such that every two-sided decomposition at any scale t in (0, t_eta] satisfies, for both signs and
every block m:  ||t B_+-||_1 <= eta,  ||D_m(t Omega_{+-,m})||_2 <= eta,  | ||w_m +- t Omega_{+-,m}||_inf - M_m | <= eta.
*Proof.* If not, there are t_n -> 0 and decompositions violating one inequality (say on the + side; the - side is identical). Put
A_n := a + t_n B_{+,n}, W_n := w + t_n Omega_{+,n}. They are bounded (q*, N_m <= s(t_n) <= 2), so along a subsequence A_n -> A weak* in l_1
and W_{n,m} -> W_m weak* in l_inf. L* is weak*-weak* continuous and A_n + L*W_n = f + t_n g -> f, so A + L*W = f, with q*(A) <= 1 and
N_m(W_m) <= 1 (weak* lower semicontinuity of dual norms). By uniqueness of the forced decomposition (A Fact B), A = a and W = w.
U* is weak*-to-norm continuous on bounded sets (U compact), so ||U*A_n|| -> nu and ||A_n||_1 = q*(A_n) - ||U*A_n|| <= s(t_n) - ||U*A_n|| -> 1 - nu
= ||a||_1. For a bounded coordinatewise convergent sequence in l_1 this gives ||A_n - a||_1 -> 0 (for a finite G, ||(A_n - a)1_G|| -> 0 and
limsup ||A_n 1_{G^c}|| <= ||a||_1 - ||a 1_G||_1). D_m: l_inf -> l_2 is compact (Phi_m in l_2), hence D_m W_n -> D_m w in l_2, i.e.
||D_m(t_n Omega_n)|| -> 0 and ||D_m W_n|| -> C_m; then ||W_n||_inf <= s(t_n) - ||D_m W_n|| -> M_m while liminf ||W_n||_inf >= M_m (weak* lsc).
All three quantities tend to 0, a contradiction. QED.

## 2.3 Lemma (first-order terms, budget, one-sided base bounds, weighted second order). PROVED.
Let t <= t_eta with eta <= eta_* := min(nu/(2||U|| + 2), min_m C_m)/2. Then for both signs:
 (a) |q_0 B_+-(zhat)| <= t/2 and |<Omega_{+-,m}, zeta_m>| <= t/2 for every m.
 (b) Sum_{j notin F} (|B_+(j)| - z_j B_+(j)) <= t/(2 q_0) and sum_{j notin F} (|B_-(j)| + z_j B_-(j)) <= t/(2 q_0). Consequently
     sum_{j in J_gamma} |B_+-(j)| <= t/(2 gamma q_0) for every gamma in (0,1), and
     ||B_+ 1_{F^c}||_1 + ||B_- 1_{F^c}||_1 <= ||(B_+ - B_-) 1_{F^c}||_1 + t/q_0.
 (c) sum_{k in P_m} |alpha_{m,k}| ( ||w_m + t Omega_{+,m}||_inf - sigma_k (w_m + t Omega_{+,m})(k) ) <= t^2/(2 sigma_m), and the same for
     W_- := w - t Omega_-.
 (d) Gamma_w(B_+-, Omega_+-) <= 1 + eta_Gamma(eta),  eta_Gamma(eta) := (1 + ||U|| eta/nu) max_m (1 + eta/C_m) - 1  (-> 0 as eta -> 0).
*Proof.* (a) q**(zhat) = 1, so q*(A) >= A(zhat): 1 + t B_+(zhat) <= s(t), i.e. q_0 B_+(zhat) <= q_0 t/2. By Fact C,
N_m(W) >= <W, zeta_m>/sigma_m = 1 + t<Omega_{+,m}, zeta_m>/sigma_m, so <Omega_{+,m}, zeta_m> <= sigma_m t/2. Evaluating g = B_+ + sum R_m* Omega_{+,m}
at xi = q_0 zhat gives q_0 B_+(zhat) + sum_m <Omega_{+,m}, zeta_m> = g(xi) = 0 (A Remark 2.3). The weights q_0, sigma_m sum to 1, so each term,
being <= (its weight) t/2 while the sum is 0, is >= -t/2. The - side: 1 - t B_-(zhat) <= s(t) and 1 - t<Omega_-, zeta>/sigma <= s(t),
with the same sum identity.
(b) By A Lemma 7.1, q_0 E_q(a + tB_+) + sum_m sigma_m e_m(W_{+,m}) <= s(t) - 1 <= t^2/2 with E_q, e_m >= 0, and by A Lemma 7.2
E_q(a + tB) >= sum_{j notin F} (|tB_j| - z_j t B_j). For the - side apply the same to a + (-t)B_-. On J_gamma, |x| -+ z x >= gamma |x|.
The last inequality: for |z| <= 1 and reals x, y, |x| + |y| <= |x - y| + (|x| - z x) + (|y| + z y), because the difference of the two sides
is |x - y| - z(x - y) >= 0; sum over j notin F.
(c) A Lemma 7.2 (block formula; all terms >= 0) and the budget: sigma_m e_m(W_{+,m}) <= t^2/2.
(d) A Lemma 4.3: E_q(a + tB) >= nu Psi(t U*B/nu) >= (t^2/2) h(B)/(1 + t||U*B||/nu) when t||U*B||/nu <= 1/2 (true: t||B||_1 <= eta <= eta_*).
A Lemma 7.2: e_m(W) >= t^2 ||P-perp D Omega||^2 / (||D W|| + <D W, D w>/C) and the denominator is <= 2||DW|| <= 2(C_m + eta) by 2.2.
Insert both in the budget and divide by t^2/2. QED.

## 2.4 Lemma (sup-level parametrization of a block). PROVED.
Fix m (dropped from the notation) and t <= t_eta, eta <= eta_*. Define d_+, d_- by
  ||w + t Omega_+||_inf = (1 - d_+ t) M,   ||w - t Omega_-||_inf = (1 + d_- t) M,   and   omega_+- := Omega_+- + d_+- w.
Then:
 (a) |d_+-| t <= eta/M; in particular 1 - d_+ t >= 1/2 and 1 + d_- t >= 1/2 for eta <= M/2.
 (b) (box) for every k: |(1 - d_+ t) w(k) + t omega_+(k)| <= (1 - d_+ t) M and |(1 + d_- t) w(k) - t omega_-(k)| <= (1 + d_- t) M.
 (c) (peaks) for k in P, sigma_k := sign w(k): sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k), and sum_{k in P} |alpha_k| |omega_+-(k)| <= t/(2 sigma_m).
 (d) |d(omega_+-) - d_+-| <= t/sigma_m, where d(omega) := <D w, D omega>/C.
 (e) |t Omega_+-(k)| <= 3 for all k, and |d_+-| <= (3 ||Phi_m||_2 / t + t/sigma_m)/M.
 (f) (non-peaks) for k in Q with gap g_k and sigma_k := sign w(k) (any sign if w(k) = 0):
     sigma_k omega_+(k) <= (1 - d_+ t) g_k / t   and   sigma_k omega_-(k) >= -(1 + d_- t) g_k / t.
*Proof.* (a) is 2.2. (b): w + tOmega_+ = (1 - d_+t) w + t omega_+ and w - tOmega_- = (1 + d_-t) w - t omega_-; each coordinate is bounded by the
sup norm. (c): at a peak, |(1 - d_+t) sigma_k M + t omega_+(k)| <= (1 - d_+t) M forces sigma_k t omega_+(k) <= 0, and then
||W_+||_inf - sigma_k W_+(k) = t|omega_+(k)|; insert in 2.3(c). The - side is symmetric (sigma_k omega_-(k) >= 0, ||W_-||_inf - sigma_k W_-(k) =
t|omega_-(k)|). (d): by Fact C, zeta/sigma_m = alpha + D^2 w/C, so <Omega_+, zeta>/sigma_m = <omega_+ - d_+ w, alpha> + <D(omega_+ - d_+ w), Dw>/C
= -sum_P |alpha_k||omega_+(k)| - d_+ M + d(omega_+) - d_+ C, i.e. d(omega_+) - d_+ = <Omega_+, zeta>/sigma_m + sum_P |alpha_k||omega_+(k)|; use 2.3(a)
and (c). For the - side, <Omega_-, zeta>/sigma_m = sum_P |alpha_k||omega_-(k)| + d(omega_-) - d_-. (e): |t Omega(k)| <= |W(k)| + |w(k)| <= s(t) + 1 <= 3;
d(omega) - d = <Dw, D Omega>/C + dC - d = <Dw, D Omega>/C - dM, so |d| M <= ||D Omega||_2 + |d(omega) - d| <= 3||Phi||_2/t + t/sigma_m.
(f): multiply the box inequality of (b) by sigma_k: on the + side (1 - d_+t)(M - g_k) + sigma_k t omega_+(k) <= (1 - d_+t) M; on the - side
(1 + d_-t)(M - g_k) - sigma_k t omega_-(k) <= (1 + d_-t) M. QED.

## 2.5 Lemma (base part on a finite support). PROVED.
If F is finite there is C_F < infinity with ||beta||_1 <= C_F ( ||P_{e-perp} U* beta|| + |beta(zhat)| ) for every beta supported in F.
*Proof.* On the finite-dimensional space l_1(F) the linear map beta -> (P_{e-perp} U* beta, beta(zhat)) is injective: if P_{e-perp} U* beta = 0 then
U* beta = mu e = (mu/nu) U* a, so beta = (mu/nu) a (U* injective), and beta(zhat) = mu/nu a(zhat) = mu/nu; if this also vanishes, beta = 0. QED.
Consequence (for t <= t_eta, eta <= eta_*): beta := B_+ 1_F satisfies
  ||B_+ 1_F||_1 <= C_F ( sqrt(nu h(B_+)) + ||U|| ||B_+ 1_{F^c}||_1 + t/(2 q_0) + ||zhat||_inf ||B_+ 1_{F^c}||_1 ),
using P_{e-perp} U* B_+ 1_F = P_{e-perp} U* B_+ - P_{e-perp} U* B_+ 1_{F^c}, 2.3(a) and beta(zhat) = B_+(zhat) - (B_+ 1_{F^c})(zhat). With 2.3(d),
h(B_+) <= 2/q_0, so ||B_+ 1_F||_1 <= K_F (1 + ||B_+ 1_{F^c}||_1) with K_F depending only on f.
