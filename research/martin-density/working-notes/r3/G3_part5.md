# G3 part 5: uniform transfer expansion, windowed averaging, proofs of Theorems B and C

## 5.1 Lemma (uniform transfer expansion at f). PROVED. (Any admissible T.)
Let f in S_{p*} with F finite. For every eps_tr > 0 and A_0 >= 1 there are c_1 in (0, 1/8] and t_1 > 0 such that for every t in (0, t_1] and every
balanced finite certificate c = (b, (omega_m)) at f (C Def 7.0) with
  (C-a) ||b||_1 <= A_0 and Gamma_w(c) <= 2;  (C-b) supp omega_m subset {k in Q_m : gap_m(k) >= t^2} and |omega_m(k)| <= 2 gap_m(k)/t,
we have  p*(f + s g_c) <= 1 + (s^2/2)(Gamma_w(c) + eps_tr)  for all |s| <= c_1 t.
*Proof.* This is C Thm 7.4, Steps 1-4, run at f itself ("N = infinity", C Cor 7.2(c)) with constants made uniform over the class (C-a), (C-b).
Step 0 (transfer peaks; they depend on f and eps_tr only). For each block m put pihat_m := R_m*(sgn(w_m) 1_{P_m}) in l_1 and tau_m := pihat_m(zhat) a - pihat_m
(so tau_m(zhat) = 0). For delta_0, delta_1 > 0 let T^dn := tau_m + delta_0 q*(tau_m) a and T^up := -tau_m + delta_0 q*(tau_m) a (if tau_m = 0 take T := delta_0 a);
T(zhat) > 0. By density of every tail of (u_{k,m})_k choose k_* = k_*^{m,dn}, k_*^{m,up} with q*(u_{k_*,m} - T/q*(T)) <= delta_1 so deep that k_* is a peak
of sign +1 with positive margin mu_* := u_{k_*,m}(xi) - theta_m Phi_m(k_*) (theta_m := M_m sigma_m/(m C_m)): indeed u_{k_*}(zhat) >= T(zhat)/q*(T) - delta_1 > 0
(|v(zhat)| <= q*(v) as q**(zhat) = 1) while Phi_m(k_*) -> 0 (Fact C). Put lambda_* := q*(T), Phi_* := Phi_m(k_*) and, for t > 0,
  Lset_t := {k : |w_m(k)| >= M_m - t^2/2} (contains P_m),  y_t := sgn(w_m) 1_{Lset_t} +- (lambda_*/(m Phi_*)) e_{k_*}  (+ for dn, - for up),
  beta_t := (R_m* y_t)(zhat),  e_t := R_m* y_t - beta_t a (so e_t(zhat) = 0),  e_{y,t} := 1 + <D w, D y_t>/C.
Facts. (T1) q_0 beta_t = sigma_m e_{y,t} +- lambda_* mu_* (C (7.3) at f): from zeta = sigma_m(alpha + D^2 w/C), <sgn(w) 1_{Lset_t}, alpha> = sum_P |alpha_k| = 1, and
sigma_m |alpha_{k_*}| = m Phi_* mu_* (Fact C at the peak k_*). (T2) q*(e_t) <= 2 lambda_* delta_1 + 2(1 + ||U||) sum_{k in Lset_t \ P} lambda_k: at t = 0 (Lset = P),
e_0 = +-[(lambda_* u_{k_*} - T) + (T(zhat) - lambda_* u_{k_*}(zhat)) a] (C Step 1), and y_t - y_0 = sgn(w) 1_{Lset_t \ P}. The sum tends to 0 as t -> 0
(dominated convergence; the sets Lset_t \ P decrease to the empty set). (T3) lambda_* mu_* <= q_0 (T(zhat) + lambda_* delta_1) = q_0(delta_0 q*(tau) + lambda_* delta_1).
(T4) For k_* deep, e_{y,t} in [1/2, Y_1] with Y_1 independent of t, and Y_0 := sup_t ||D y_t||_2 < infinity.
Choose delta_0, then delta_1, then t_1, so that eps_1 := max_{m, dn/up} sup_{t <= t_1} (lambda_* mu_*/q_0 + q*(e_t)) <= eps_tr/(16 N (2 + 2/sigma_min)).
Step 1 (equalisation parameters). Let c satisfy (C-a), (C-b); Gamma := Gamma_w(c), h := h(b) <= 2/q_0, H_m := H_m(omega_m) <= 2/sigma_m, d_m := d(omega_m),
|d_m| <= ||D omega_m||_2 <= 2/t. For each m use the dn-peak if H_m >= Gamma and the up-peak otherwise, and put tau_m := (H_m - Gamma)/(2 e_{y,m,t}),
eps_m := tau_m s^2; |tau_m| <= tau_max := 2 + 2/sigma_min, and tau_m(+-lambda_* mu_*) = |tau_m| lambda_* mu_* >= 0 in both cases.
Step 2 (decomposition). A(s) := a + s b + sum_m eps_m R_m* y_m and W_m(s) := w_m + s(omega_m - d_m w_m) - eps_m y_m satisfy A(s) + sum_m R_m* W_m(s) = f + s g_c,
so p*(f + s g_c) <= max(q*(A(s)), max_m N_m(W_m(s))) (A Fact A).
Step 3 (block sup norm). Let |s| <= c_1 t with c_1 <= 1/8 and c_1^2 tau_max <= 1/8, and t_1 so small that t^2 (2 + lambda_*/(m Phi_*)) <= M_m for all m.
Then |s d| <= 1/4 and |eps| <= t^2/8, and ||W(s)||_inf = (1 - s d) M - eps:
 (i) k in Lset_t, k != k_*: omega(k) = 0 (supp omega has gap >= t^2), W(k) = sgn(w(k))((1 - sd)|w(k)| - eps), and (1 - sd)|w(k)| >= |eps|; equality at peaks.
 (ii) k = k_*: W(k_*) = (1 - sd) M - eps(1 +- lambda_*/(m Phi_*)) lies in [-((1 - sd)M - eps), (1 - sd)M - eps] (dn: eps >= 0; up: eps < 0; the
     choice of t_1).
 (iii) k notin Lset_t cup supp omega: |W(k)| = (1 - sd)|w(k)| <= (1 - sd)(M - t^2/2) <= (1 - sd) M - eps.
 (iv) k in supp omega (gap g >= t^2): |W(k)| <= (1 - sd)(M - g) + |s| 2g/t <= (1 - sd) M - g(3/4 - 2c_1) <= (1 - sd)M - t^2/2 <= (1 - sd)M - eps.
Step 4 (block Hilbert part). D W = D w + h, h := -s d D w + s D omega - eps D y, ||h|| <= 4 c_1 + Y_0 t^2 <= C_min/2 (c_1 <= C_min/16, t_1 small).
By C (7.2), ||Dw + h|| <= C + <Dw, h>/C + ||P-perp h||^2/(2(C - ||h||)), with <Dw, h>/C = s d M - eps(e_y - 1) and
||P-perp h||^2 <= (1 + th) s^2 C H + (1 + 1/th) eps^2 Y_0^2 (th > 0 to be chosen). Since eps e_y = s^2 (H - Gamma)/2,
  N(W(s)) <= 1 + (s^2/2) Gamma + (s^2/2) H [(1 + th)(1 + 2||h||/C) - 1] + (1 + 1/th) tau_max^2 Y_0^2 s^4/C.
Step 5 (base). With E := sum_m eps_m beta_m, A(s) = (1 + E) a + s b + sum_m eps_m e_m, so q*(A(s)) <= (1 + E) q*(a + s' b) + sum_m |eps_m| q*(e_m),
s' := s/(1 + E). A Lemma 4.3 (b(zhat) = 0, supp b in F finite, ||b/a||_inf <= A_0/min_F |a_j|, ||U*b|| <= ||U|| A_0) gives, for |s| <= c_1 t_1 small,
q*(a + s'b) <= 1 + (s'^2/2) h (1 + 2|s'| ||U|| A_0/nu). By (T1) and Step 1, sum_m tau_m sigma_m e_{y,m}/q_0 = sum_m sigma_m (H_m - Gamma)/(2 q_0) = (Gamma - h)/2
(sum_m sigma_m H_m = Gamma - q_0 h, sum_m sigma_m = 1 - q_0), hence E = (s^2/2)(Gamma - h) + s^2 sum_m |tau_m| lambda_* mu_*/q_0 and
  q*(A(s)) <= 1 + (s^2/2) Gamma + (s^2/2) h [ (1 + 2|s'| ||U|| A_0/nu)/(1 + E) - 1 ] + s^2 N tau_max eps_1.
Step 6. Choose th, then c_1 and t_1, so small that every bracket times its bounded coefficient (H <= 2/sigma_min, h <= 2/q_0, |E| <= 4 s^2 + s^2 N tau_max eps_1)
plus the s^4 term is <= (s^2/2) eps_tr/2, and recall s^2 N tau_max eps_1 <= (s^2/2) eps_tr/8. QED.

## 5.2 Theorem (windowed averaging over scales). PROVED.
Let f in S_{p*} with F finite, g in C(f), rho in (0,1), and eta_0 > 0 with rho^2(1 + eta_0) <= (1 + rho^2)/2. Suppose there are c_1 in (0,1] and a sequence of
triples (t^(j), n_j, K_j) with t^(j) -> 0, n_j >= 24 rho^2 K_j/(c_1(1 - rho^2)) and K_j t^(j)/n_j -> 0 such that for every j and every t in
{t^(j) 2^{1-i} : i = 1, ..., n_j} there is a balanced finite certificate c_t at f with
 (i) p*(f + s g_{c_t}) <= 1 + (s^2/2)(1 + eta_0) for |s| <= c_1 t;  (ii) p*(g - g_{c_t}) <= K_j t;  (iii) Gamma_w(c_t) <= 1 + eta_0.
Then (f, rho' rho g) is in cl NA((c_0,p), l_2^2) for every rho' < 1.
*Proof.* A Thm 6.8's proof, with the expansion (A) replaced by (i), the n certificates taken only on ONE window of n_j dyadic scales, and
the final recovery by C Thm 7.4. Fix s_0 in (0,1] with s_0^2 <= 1 - rho^2 and j so large that c_1 t^(j) <= rho s_0 and 2 rho K_j t^(j)/n_j <= (1 - rho^2) s_0/3.
Write n = n_j, K = K_j, t_i := t^(j) 2^{1-i}, c := (1/n) sum_i c_{t_i} (a balanced finite certificate; g_c = (1/n) sum_i g_{c_{t_i}}).
(A) if rho|s| <= c_1 t_i: p*(f + s rho g_{c_{t_i}}) <= 1 + (rho^2 s^2/2)(1 + eta_0) by (i);
(B) always: p*(f + s rho g_{c_{t_i}}) <= p*(f + s rho g) + rho|s| K t_i <= s(rho s) + rho|s| K t_i (g in C(f), (ii)).
By convexity p*(f + s rho g_c) <= (1/n) sum_i p*(f + s rho g_{c_{t_i}}).
|s| <= s_0: with I_f := {i : c_1 t_i < rho|s|}, sum_{I_f} t_i < 2 rho|s|/c_1 (geometric), so p*(f + s rho g_c) <= max{1 + (rho^2 s^2/2)(1 + eta_0), s(rho s)} + Q s^2,
Q := 2 rho^2 K/(c_1 n) <= (1 - rho^2)/12; and 1 + (rho^2 s^2/2)(1 + eta_0) + Q s^2 <= 1 + (s^2/2)(1 - (1 - rho^2)/3) <= 1 + s^2/2 - s^4/8 <= s(s)
(s^2 <= 1 - rho^2), while s(rho s) + Q s^2 <= s(s) by A Lemma 4.7.
|s| >= s_0: all i use (B): p*(f + s rho g_c) <= s(rho s) + 2 rho K t^(j)|s|/n <= s(rho s) + (1 - rho^2) s_0 |s|/3 <= s(s) (A Lemma 4.7).
Hence rho g_c is in C(f). Gamma_w is a convex quadratic form, so Gamma_w(rho c) <= rho^2 (1 + eta_0) <= 1. C Thm 7.4 (a in c_00, (f, rho g_c) contractive,
rho g_c a balanced finite certificate with Gamma_w <= 1) gives (f, rho' rho g_c) in cl NA for all rho' < 1. Finally
p*(rho g_c - rho g) <= (rho/n) sum_i K t_i <= 2 rho K t^(j)/n -> 0 (j -> infinity), and cl NA is closed. QED.

## 5.3 Proof of Theorem B. PROVED.
Fix N, the SLD operator T, f in R_0 (constants gamma, vartheta), g in C(f) and rho in (0,1). Choose eta_0 with rho^2(1 + eta_0) <= (1 + rho^2)/2,
eps_tr := eta_0/2, A_0 := K_b + 1 (4.2(b)), and c_1, t_1 from 5.1. Choose eta <= eta_1 with sqrt(1 + eta_Gamma(eta)) <= sqrt(1 + eta_0/2) - 1/100 (possible
since eta_Gamma(eta) -> 0), and put t_* := min(t_eta, t_1, 1).
For a window index l put t^(l) := T_hi(l), n_l := n^w_l, K_l := (1 + ||U||) K_2 Lambda_f(l) (p* <= q* <= (1 + ||U||)||.||_1). The n_l scales
t_i = T_hi(l) 2^{1-i} lie in W(l) (t_{n_l} = 2 T_lo(l)). By 3.3 and (P3),
  Lambda_f(l) T_hi(l) <= vartheta^{-l^2} Lambda°(l) T_hi(l) <= vartheta^{-l^2} 2^{-l^3}/l -> 0   (l -> infinity).
Hence for all large l and every window scale t: t <= t_*, K t <= 1 (part 4), K_4 Lambda_f(l) t <= 1/100, so by 4.2 the window certificate c_t satisfies
(C-a) (||b_t|| <= K_b <= A_0, Gamma_w(c_t) <= 1 + eta_0/2 <= 2) and (C-b); by 5.1, p*(f + s g_{c_t}) <= 1 + (s^2/2)(1 + eta_0) for |s| <= c_1 t; and
p*(g - g_{c_t}) <= K_l t. The window conditions of 5.2 hold for l large:
  n_l >= l 2^{l^3} Lambda°(l) >= 24 rho^2 (1 + ||U||) K_2 vartheta^{-l^2} Lambda°(l)/(c_1(1 - rho^2)) = 24 rho^2 K_l/(c_1(1 - rho^2))
(because l 2^{l^3} vartheta^{l^2} -> infinity), and K_l t^(l)/n_l <= (1 + ||U||) K_2 vartheta^{-l^2} 2^{-l^3}/l -> 0. Theorem 5.2 gives
(f, rho' rho g) in cl NA for all rho, rho' < 1, i.e. g in Ls(f). As g in C(f) was arbitrary, f is in R. QED.

## 5.4 Proof of Theorem C. PROVED.
(<=) Let f in S_{p*}, g in C(f), rho < 1, eps > 0. Lemma Z gives f' in R_0 and g' in C(f') with p*(f' - f) < eps, p*(g' - rho g) < eps. By Theorem B,
(f', rho' g') is in cl NA for every rho' < 1; letting eps -> 0 and rho' -> 1, (f, rho g) is in cl NA. By A Prop 2.1 (R1) NA((c_0,p), l_2^2) is dense.
(=>) Assume density; let f, g in C(f), rho < 1, eps > 0. S_0 := (f, rho g) has norm 1 (g in C(f) and rho < 1). Take S in NA with ||S - S_0|| < eps', attaining
its norm at x in S_p, and replace x by -x if necessary. Since (f, g) is contractive, f(x)^2 + g(x)^2 <= 1, while f(x)^2 + rho^2 g(x)^2 = ||S_0 x||^2 >= (1 - 2eps')^2;
hence |g(x)| <= 2 (eps'/(1 - rho^2))^{1/2} and |f(x)| >= 1 - 2 eps' - ..., so v := Sx/||Sx|| is within o(1) of +-e_1 as eps' -> 0. Let Q be the rotation of
l_2^2 with Q v = e_1 (Q -> identity) and S' := QS/||S|| = (f', g'). Then f'(x) = 1, g'(x) = 0, ||S'|| = 1, so f' in S_{p*} attains its norm, g' in C(f')
(A Prop 2.1), and (f', g') -> (f, rho g) as eps' -> 0. NA points belong to R_0 (1.4(a)). So Lemma Z holds. QED.
