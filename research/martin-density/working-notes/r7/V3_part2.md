# V3 part 2: raise companions and the raise-transfer lemma (any admissible T, I finite, F arbitrary)

Notation of the note (Sections 1, 7, 8). f in S_{p*}, forced data (xi, q_0, a, w, F, z, zhat, e, nu), s_j := sgn a_j (j in F).

## 2.0 Definition (raise; raised companion)
A RAISE of f is Delta a in l_1 with supp Delta a subset F and s_j Delta a_j >= 0 for j in F. Put
  lambda := q*(a + Delta a),  a^# := (a + Delta a)/lambda,
and let f^# be the first row with forced data (a^#, z) (Remark rem:lemmaZ(c): e^# := U*a^#/||U*a^#||, zhat^# := z + U e^#,
q_0^# := (1 + sum_m |R_m** zhat^#|_m)^{-1}, xi^# := q_0^# zhat^#, w^# := J_V(L** xi^#), f^# := a^# + L* w^#; admissible because
supp a^# = F and sgn a^# = sgn a = z on F). Nothing off F changes: K, J, the rooms, the signature sets' states, the bad set are those of f.
More generally a MONOTONE MOVE also allows masses of sign z_j at contacts j in K (banks); everything below holds verbatim for them.

## 2.1 Lemma (basic facts). PROVED.
(a) 1 + ||Delta a||_1 - ||U*Delta a|| <= lambda <= 1 + ||Delta a||_1 + ||U*Delta a||; hence lambda >= 1 whenever ||U*Delta a|| <= ||Delta a||_1
    (e.g. ||U|| <= 1).
(b) ||e^# - e|| <= 2||U*Delta a||/nu.
(c) For u in l_1: |u(zhat^#) - u(zhat)| <= ||U*u|| ||e^# - e||; ||zhat^# - zhat||_inf <= ||U|| ||e^# - e||.
(d) ||a^# - a||_1 <= 2||Delta a||_1 + ||U*Delta a||, and f^# -> f in norm as ||Delta a||_1 -> 0.
Proof. (a) On F, |a_j + Delta a_j| = |a_j| + |Delta a_j| (same signs), Delta a = 0 off F, so ||a + Delta a||_1 = ||a||_1 + ||Delta a||_1;
||U*a|| - ||U*Delta a|| <= ||U*(a + Delta a)|| <= ||U*a|| + ||U*Delta a||; q*(a) = 1. (b) e^# = U*(a+Delta a)/||U*(a+Delta a)|| (scale
invariance) and ||x/||x|| - y/||y|| || <= 2||x - y||/||y|| with y = U*a, ||y|| = nu. (c) zhat^# - zhat = U(e^# - e) and u(Uh) = <U*u, h>.
(d) a^# - a = Delta a/lambda + (1/lambda - 1)a and |1/lambda - 1| <= lambda - 1. Convergence of f^#: a^# -> a in l_1 with z fixed; the
argument of Proposition prop:approximants ((ii) => (i)) applies verbatim to non-norm-attaining rows given by forced data (Remark rem:lemmaZ(c)).
QED

## 2.2 Lemma (cost of the normer change). PROVED.
Put delta := zhat^# - zhat, eps_e := ||U|| ||e^# - e||, Delta_m := sum_k lambda_{k,m}|u_{k,m}(delta)| (<= m 2^{-m} eps_e). There are c_f, C_f
(depending only on f, N, T) such that, if max_m Delta_m <= c_f:
  |q_0^# - q_0| + |sigma^#_m - sigma_m| + |C^#_m - C_m| <= C_f eps_e,   p*(L*(w^# - w)) <= (1 + ||U||) sum_m ||R_m*(w^#_m - w_m)||_1 <= C'_f eps_e log(e/eps_e).
Proof. Z3 Lemma 3.1 (refereed PROVED): its proof uses only the clamp formula for w_m, w^#_m in terms of zhat, zhat^# (v_k := m|u_k(zhat)|/
|R** zhat|, C = root of sum_k min(Phi_k(1-c)/c, v_k)^2 = 1), never the base parts, and gives sum_m ||R_m*(w^#_m - w_m)||_1 <= C_f c(delta),
c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)]. Here |u_k(delta)| <= ||U*u_k|| ||e^# - e|| <= eps_e (q*(u_k) = 1),
and sum_k min(lambda_{k,m}, x) <= x(log_2(2m/x) + 3). Finally p* <= q* <= (1 + ||U||)||.||_1 on X*. QED

## 2.3 Lemma (raise transfer, RT). PROVED.
Assume lambda >= 1. For every h in X* and every r in R,
  p*(f^# + r h) <= 1 + (p*(f + lambda r h) - 1 + 2||U*Delta a||)/lambda + p*(L*(w^# - w)).
Proof. By Lemma lem:dualball choose A, W with f + lambda r h = A + L*W and max(q*(A), ||W||_{V*}) = pi := p*(f + lambda r h). Put
B := (A - a)/(lambda r), Theta := (W - w)/(lambda r) (r != 0; r = 0 is trivial), so h = B + L*Theta. Then the identity
  f^# + r h = (a^# + r B) + L*(w + r Theta) + L*(w^# - w)
holds (a^# + L*w^# = f^#). Base: by the triangle inequality in l_1 and in H,
  q*(a + Delta a + lambda r B) <= q*(a + lambda r B) + ||Delta a||_1 + ||U*Delta a|| = q*(A) + ||Delta a||_1 + ||U*Delta a||
                              <= pi + (lambda - 1) + 2||U*Delta a||          (Lemma 2.1(a)),
and q*(a^# + rB) = q*(a + Delta a + lambda r B)/lambda <= 1 + (pi - 1 + 2||U*Delta a||)/lambda. Blocks: w_m + r Theta_m = (1 - 1/lambda) w_m
+ (1/lambda) W_m, so N_m(w_m + r Theta_m) <= (1 - 1/lambda) + pi/lambda (N_m(w_m) = 1, convexity). By Lemma lem:dualball,
p*((a^# + rB) + L*(w + r Theta)) <= max(q*(a^# + rB), ||w + r Theta||) <= 1 + (pi - 1 + 2||U*Delta a||)/lambda. Add p*(L*(w^# - w)). QED
Remark. No smallness of ||Delta a||_1 relative to r^2 is needed: a same-sign raise on F commutes with the triangle inequality. The only
zeroth-order errors are 2||U*Delta a|| (Hilbert part) and the normer change p*(L*(w^# - w)) (Lemma 2.2), both controlled by ||U*Delta a||.

## 2.4 Corollary. PROVED.
If g in C(f), rho in (0,1] and lambda >= 1, then for all r:
  p*(f^# + r rho g) <= 1 + (s(lambda rho r) - 1)/lambda + eps',   eps' := 2||U*Delta a|| + p*(L*(w^# - w)),
and (s(lambda x) - 1)/lambda <= s(x) - 1 + (lambda - 1) min(lambda^2 x^2/2, 1).
Proof. Lemma 2.3 with h = rho g and pi <= s(lambda rho r). For the inequality: phi(lambda) := (s(lambda x) - 1)/lambda has
phi'(lambda) = (s(u) - 1)/(lambda^2 s(u)) with u = lambda x, and 0 <= (s(u)-1)/s(u) <= min(u^2/2, 1). Integrate over [1, lambda]. QED

## 2.5 Theorem E_RT (windowed recovery through raised companions). PROVED.
Let T be admissible, I finite, f in S_{p*} (F arbitrary), g in C(f), rho in (0,1), eta_0 in (0,2] with rho^2(1 + eta_0) <= (1 + rho^2)/2.
Suppose there are first rows f_j and lambda_j >= 1, eps'_j >= 0, c_flat in (0,1], windows (T_j, n_j, K_j) with T_j in (0,1], n_j in N,
K_j >= 0, such that:
 (a) (transfer) p*(f_j + r rho g) <= 1 + (s(lambda_j rho r) - 1)/lambda_j + eps'_j for all r in R;
 (b) (pieces) for each t in S_j := {T_j 2^{1-i} : 1 <= i <= n_j} a functional g_{j,t} with p*(g - g_{j,t}) <= K_j t and
     p*(f_j + r rho g_{j,t}) <= 1 + (rho^2 r^2/2)(1 + eta_0) for 0 < rho|r| <= c_flat t;
 (c) K_j T_j -> 0, n_j >= 48 rho^2 K_j/(c_flat(1 - rho^2)) for large j, lambda_j -> 1, p*(f_j - f) -> 0;
 (d) (decoupling) eps'_j <= theta_j (T_j 2^{-n_j})^2 with theta_j -> 0;
 (e) (closure at f_j) for every j, rho gbar_j in C(f_j) implies (f_j, rho gbar_j) in cl NA, where gbar_j := (1/n_j) sum_{t in S_j} g_{j,t}.
Then (f, rho g) in cl NA((c_0, p), l_2^2).
Proof. Fix r_0 in (0,1] with r_0^2 <= 1 - rho^2. Take j so large that (c) holds, theta_j rho^2/c_flat^2 <= (1-rho^2)/48,
(lambda_j - 1)(1 + lambda_j^2) <= (1-rho^2)r_0/48, eps'_j <= (1-rho^2)r_0^2/48 and 2 rho K_j T_j/n_j <= (1-rho^2)r_0/48. Two bounds, for t in S_j:
 (A) if rho|r| <= c_flat t: p*(f_j + r rho g_{j,t}) <= 1 + (rho^2 r^2/2)(1 + eta_0)  [(b)];
 (B'') always: p*(f_j + r rho g_{j,t}) <= p*(f_j + r rho g) + rho|r| K_j t <= s(rho r) + (lambda_j - 1) min(lambda_j^2 rho^2 r^2/2, 1) + eps'_j
       + rho|r| K_j t  [(a), Corollary 2.4].
By convexity p*(f_j + r rho gbar_j) <= (1/n_j) sum_t p*(f_j + r rho g_{j,t}).
Case |r| <= r_0. Let I_r := {t : c_flat t < rho|r|}; sum_{I_r} t < 2 rho|r|/c_flat (dyadic). If I_r is empty all terms obey (A) and
1 + (rho^2 r^2/2)(1 + eta_0) <= 1 + r^2(1 + rho^2)/4 <= s(r) (r^2 <= 1 - rho^2, as in thm:windowed). Otherwise rho|r| > c_flat T_j 2^{1-n_j}, so
eps'_j <= theta_j (T_j 2^{-n_j})^2 < theta_j rho^2 r^2/c_flat^2 <= (1-rho^2) r^2/48, and (lambda_j - 1)lambda_j^2 rho^2 r^2/2 <= (1-rho^2)r^2/48; hence
  p*(f_j + r rho gbar_j) <= max{1 + (rho^2 r^2/2)(1 + eta_0), s(rho r)} + (1-rho^2) r^2/24 + 2 rho^2 K_j r^2/(c_flat n_j)
                         <= max{1 + r^2(1+rho^2)/4, s(rho r)} + (1-rho^2) r^2/12 <= s(r),
by 1 + r^2(2 + rho^2)/6 <= 1 + r^2/2 - r^4/8 <= s(r) (r^2 <= 1 - rho^2) and s(rho r) + (1-rho^2)r^2/12 <= s(r) (Lemma lem:slack(a), |r| <= 1).
Case |r| > r_0. (B'') for every t: p*(f_j + r rho gbar_j) <= s(rho r) + (lambda_j - 1)(1 + lambda_j^2)min(r^2,|r|)/... <= s(rho r) +
(1-rho^2)min(r^2,|r|)/16 <= s(r): indeed (lambda_j-1)min(lambda_j^2 rho^2 r^2/2, 1) + eps'_j + 2 rho K_j T_j|r|/n_j <= (1-rho^2)r_0|r|(1/48 + 1/48 + 1/48)
<= (1-rho^2)min(r^2,|r|)/16 (min(r^2, |r|) >= r_0|r| for |r| >= r_0), and s(r) - s(rho r) >= (1-rho^2)min(r^2,|r|)/3 (Lemma lem:slack(a)).
So rho gbar_j in C(f_j); p*(rho gbar_j - rho g) <= (rho/n_j) sum_t K_j t <= 2 rho K_j T_j/n_j -> 0. By (e), (f_j, rho gbar_j) in cl NA, and
||(f_j, rho gbar_j) - (f, rho g)|| <= p*(f_j - f) + 2 rho K_j T_j/n_j -> 0; cl NA is closed. QED
Remarks. (i) With f_j = f, lambda_j = 1, eps'_j = 0 this is the mechanism of thm:windowed/thm:S; with eps'_j := p*(f_j - f) and lambda_j = 1
(a) follows from the triangle inequality and this is Z3's Theorem E (at arbitrary F). (ii) The point of (a) for RAISED companions
(Corollary 2.4): eps'_j involves only ||U* Delta a_j|| (Lemmas 2.1-2.2), NOT the raise mass ||Delta a_j||_1, which may be ~ T_j (first order).
(iii) K_j may be 0 (exact pieces); then n_j = 1 is allowed.
