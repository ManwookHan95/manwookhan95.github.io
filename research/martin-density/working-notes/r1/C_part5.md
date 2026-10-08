
---

## 7. Recovery of finite certificates

Hilbert-norm identity used throughout: for h_0 != 0 in a Hilbert space, h any vector, t real,

  (7.2)  ||h_0 + t h|| - ||h_0|| - t<h_0/||h_0||, h> = t^2 ||P_perp h||^2 / ( ||h_0 + t h|| + ||h_0|| + t<h_0/||h_0||, h> ),

P_perp the orthogonal projection onto h_0^perp; the denominator is >= 2(||h_0|| - |t| ||h||). (Multiply out:
(N - A - t b)(N + A + t b) = N^2 - (A + t b)^2 = t^2(||h||^2 - b^2).)

**Definition 7.0 (finite certificates).** Let f in S_{p*} have normer xi and forced decomposition with a in c_00,
F := supp a. A *balanced finite certificate* is a functional

  g = b + sum_m R_m^*(omega_m - d_m w_m),  supp b contained in F,  b(xi) = 0,
  omega_m finitely supported in Q_m (strict non-peaks of w_m),  d_m := <D_m w_m, D_m omega_m>/C_m .

(Then v_m := omega_m - d_m w_m satisfies v_m(z_m) = 0, z_m := R_m** xi.) Its coefficients are
H_b := ||P_{e perp} U^* b||^2/||U^* a||, H_m := (||D_m omega_m||^2 - d_m^2)/C_m (the second-order coefficients of
q*(a + t b) and N_m(w_m + t v_m)), Gamma_max := max(H_b, max_m H_m) and the **mass-weighted coefficient**

  Gamma_w := q_0 H_b + sum_m sigma_m H_m,   q_0 = q**(xi), sigma_m = |z_m|_m, q_0 + sum_m sigma_m = 1.

**Theorem 7.1 (natural certificates). [PROVED]** If (f, g) is contractive, g is a balanced finite certificate and
Gamma_max(g) <= 1, then (f, rho g) belongs to the closure of NA((c_0,p), l_2^2) for every rho in (0,1). The
approximating first rows can be chosen independently of g: they are f'_N := grad p(x'_N) for the canonical
truncations x'_N of Step 1.

Proof. *Step 1 (canonical truncations).* For N in N let z^N_j := z_j if j in F or j <= N, and z^N_j := 0
otherwise; z^N in B_{c_0}, z^N_F = sign a_F. Put x~_N := z^N + U e in c_0 and x'_N := x~_N/p(x~_N).
Since a(x~_N) = ||a||_1 + ||U^* a|| = 1 and x~_N in B_{c_0} + U(B_H) = B_q, a norms x~_N, so a = grad q(x~_N)
(q is smooth, Preprint B Lemma smoothing). As p = q + sum_m |R_m .|_m is smooth,
f'_N := grad p(x'_N) = a + sum_m R_m^* w'_{m,N}, w'_{m,N} := J_m(R_m x'_N), and f'_N attains its norm at x'_N.

*Step 2 (convergence).* z^N -> z weak* (bounded, coordinatewise), so x~_N -> z + U e = xi/q_0 weak*, and by (F3)
R_m x~_N -> R_m** xi/q_0 in l_1. Hence p(x~_N) = 1 + sum_m |R_m x~_N|_m -> 1 + (1 - q_0)/q_0 = 1/q_0,
c_N := q(x'_N) -> q_0, x'_N -> xi weak*, R_m x'_N -> z_m in l_1. By (F4): w'_{m,N} -> w_m weak*,
D_m w'_{m,N} -> D_m w_m in l_2, M'_{m,N} -> M_m, C'_{m,N} -> C_m, and R_m^* w'_{m,N} -> R_m^* w_m in l_1.
So eps_N := p*(f'_N - f) <= q*(f'_N - f) <= (1 + ||U||) sum_m ||R_m^*(w'_{m,N} - w_m)||_1 -> 0.
Let gamma_0 := (1/2) min_m min_{k in supp omega_m} (M_m - |w_m(k)|) > 0. For N >= N_0 every k in supp omega_m satisfies
M'_{m,N} - |w'_{m,N}(k)| >= gamma_0.

*Step 3 (transported certificates).* d'_{m,N} := <D_m w'_{m,N}, D_m omega_m>/C'_{m,N} -> d_m;
b'_N := b - (b(x'_N)/c_N) a (so b'_N(x'_N) = 0; b'_N -> b because b(x'_N) -> b(xi) = 0);
v'_{m,N} := omega_m - d'_{m,N} w'_{m,N}; g'_N := b'_N + sum_m R_m^* v'_{m,N}. Then eta_N := p*(g'_N - g) -> 0.

*Step 4 (uniform second-order bounds).* Base. Let beta := b'_N, A_0 := ||U^* a||, |a|_min := min_F |a_j|. For
|t| ||beta||_inf < |a|_min the signs on F do not change, so ||a + t beta||_1 = ||a||_1 + t sum_F sign(a_j) beta_j, and
by (7.2), ||U^*(a + t beta)|| <= A_0 + t<e, U^* beta> + t^2 ||P_perp U^* beta||^2/(2(A_0 - |t| ||U^* beta||)).
The first-order coefficient is sum_F sign(a_j) beta_j + <e, U^* beta> = beta(z^N) + beta(U e) = beta(x'_N)/c_N = 0.
Hence q*(a + t b'_N) <= 1 + (t^2/2) H_{b,N} A_0/(A_0 - |t| ||U^* b'_N||), H_{b,N} := ||P_perp U^* b'_N||^2/A_0 -> H_b.
Block m (drop m, N). W(t) := w' + t(omega - d' w') = (1 - t d') w' + t omega. If |t d'| <= 1/2 and |t| ||omega||_inf <= gamma_0/2,
then off supp omega |W(t)_k| <= (1 - t d') M', and on supp omega
|W(t)_k| <= (1 - t d')(M' - gamma_0) + |t| ||omega||_inf <= (1 - t d') M'; peaks are attained, so ||W(t)||_inf = (1 - t d') M'.
With h_0 := D w' (norm C') and h := D(omega - d' w'): <h_0/C', h> = d' - d' C' = d' M' and ||P_perp h||^2 = ||D omega||^2 - d'^2.
By (7.2), ||D W(t)|| <= C' + t d' M' + t^2(||D omega||^2 - d'^2)/(2(C' - |t| ||h||)). Adding,
N(W(t)) <= 1 + (t^2/2) H'_{m,N} C'/(C' - |t| ||h||), H'_{m,N} := (||D omega||^2 - d'^2)/C' -> H_m.
So there are t_1 > 0, N_1 and theta(t) -> 1 (t -> 0) such that for N >= N_1, |t| <= t_1 all these bounds hold
with the factor theta(t), and with t replaced by rho t.

*Step 5 (small t).* By (1.1) applied to f'_N + t rho g'_N = (a + t rho b'_N) + sum_m R_m^*(w'_{m,N} + t rho v'_{m,N}):
p*(f'_N + t rho g'_N) <= 1 + (rho^2 t^2/2) Gamma_{max,N} theta(t), Gamma_{max,N} -> Gamma_max <= 1.
Since sqrt(1+t^2) >= 1 + t^2/2 - t^4/8 and rho < 1, there are t_2 in (0, min(t_1,1)] and N_2 with
p*(f'_N + t rho g'_N) <= sqrt(1+t^2) for |t| <= t_2, N >= N_2.

*Step 6 (large t).* (f, g) contractive implies (f, rho g) contractive, so p*(f + t rho g) <= sqrt(1 + rho^2 t^2) and
p*(f'_N + t rho g'_N) <= sqrt(1 + rho^2 t^2) + eps_N + |t| eta_N. Now
D(t) := sqrt(1+t^2) - sqrt(1 + rho^2 t^2) = (1-rho^2) t^2/(sqrt(1+t^2) + sqrt(1+rho^2 t^2)) >= c_rho min(t^2, |t|),
c_rho := (1-rho^2)/(2 sqrt 2), hence D(t) >= c_rho t_2 |t| for |t| >= t_2. If eps_N <= c_rho t_2^2/2 and
eta_N <= c_rho t_2/2, then eps_N + |t| eta_N <= c_rho t_2 |t| <= D(t) for |t| >= t_2.

*Step 7.* For N large, p*(f'_N + t rho g'_N) <= sqrt(1+t^2) for all t, i.e. (f'_N, rho g'_N) is contractive; it attains
its norm 1 at x'_N; and (f'_N, rho g'_N) -> (f, rho g). []

**Remark 7.1' (pure block certificates at arbitrary a). [PROVED]** If b = 0, Theorem 7.1 (and Theorem 7.4 below)
holds without the hypothesis a in c_00: Definition 7.0 is read with b = 0, omega_m finitely supported in Q_m, and no
condition on F = supp a (which may be infinite; then z is not in c_0 on F and a itself attains nothing on c_0).
Proof. Replace Step 1 by: for N large put a_N := a 1_{[1,N]}/q*(a 1_{[1,N]}), F_N := supp a_N = F cap [1,N],
e_N := U^* a_N/||U^* a_N||, z^N_j := z_j for j <= N and z^N_j := 0 for j > N. Then z^N in c_00, z^N_j = sign a_N(j)
on F_N, x~_N := z^N + U e_N in B_q and a_N(x~_N) = ||a_N||_1 + ||U^* a_N|| = q*(a_N) = 1, so a_N = grad q(x~_N); put
x'_N := x~_N/p(x~_N) and f'_N := grad p(x'_N) = a_N + sum_m R_m^* J_m(R_m x'_N), which attains its norm at x'_N.
Since a_N -> a in l_1 and e_N -> e in H, x~_N -> z + U e = xi/q_0 weak*, and Step 2 goes through verbatim, with
the additional term q*(a_N - a) -> 0 in the bound for eps_N. With b = 0 the transported certificate is
g'_N := sum_m R_m^* v'_{m,N}; g'_N(x'_N) = 0 because, for N large, supp omega_m consists of strict non-peaks of
w'_{m,N}, where (R_m x'_N)(k) = |R_m x'_N| Phi_m(k)^2 w'_{m,N}(k)/C'_{m,N}, so omega_m(R_m x'_N) = d'_{m,N}|R_m x'_N|.
In Steps 4-5 the base component is a_N with q*(a_N) = 1 (no base curvature); Steps 5-7 are unchanged. In Theorem
7.4 replace a by a_N in beta_N := ((R^* y_N)(x'_N)/c_N) a_N; then e_N -> e_inf as before (R^* y_N -> R^* y in l_1,
x'_N -> xi weak*), identity (7.3) is unchanged, and Steps 3-5 go through with H_b = 0. []

**Theorem 7.4 (rebalanced certificates: the sharp second-order condition). [PROVED]** Theorem 7.1 remains true
with the hypothesis Gamma_max(g) <= 1 replaced by the weaker **Gamma_w(g) <= 1**.

Idea. The natural decomposition keeps base and blocks at the levels 1 + t^2 H_b/2 and 1 + t^2 H_m/2 and pays the
maximum. Moving "xi-mass" between base and block at second order equalises the levels at Gamma_w/2. To lower a
block's sup norm one must lower *every* coordinate near the peak level (one coordinate alone does nothing); the image
under R^* of such a uniform lowering is a fixed vector pi^ of Y, which the base cannot absorb cheaply. The
remedy is a single **transfer peak** k_*: a deep peak whose functional u_{k_*} approximates the correction needed to
turn pi^ into a multiple of a; it exists by density of every tail of (u_{k,m})_k, it is a robust peak (positive
margin), hence it is a peak of every canonical truncation as well, and it is lowered by a large but O(t^2) amount.

Proof (one block; drop m; for several blocks repeat the construction for each block, with the base as common
partner, see the remark after the proof). Fix rho in (0,1). Assume H_N >= H_b (the case H_b > H_N is
symmetric: raise instead of lower, see Step 6).

*Step 1 (cut-off and transfer functional at xi).* Choose gamma in (max_{supp omega} |w_k|, M) with |w_k| != gamma for
all k (only countably many values are excluded). Let Lset := {k not in supp omega : |w_k| >= gamma} (it contains P),
y^0 := sign(w) 1_{Lset} in l_inf, pi^ := R^* y^0 = sum_{Lset} sign(w_k) m Phi_k u_k in l_1, and
tau_* := (pi^(xi)/q_0) a - pi^, so that tau_*(xi) = 0. For delta_0 > 0 put T := tau_* + delta_0 q*(tau_*) a; then
T(xi) = delta_0 q*(tau_*) q_0 > 0 (if tau_* = 0 put T := delta_0 a). By density of the tails of (u_k) choose, for
delta_1 > 0, an index k_* with q*(u_{k_*} - T/q*(T)) <= delta_1, as large as we wish. Then
u_{k_*}(xi) >= T(xi)/q*(T) - delta_1 q**(xi) > 0 for delta_1 small, and since theta Phi_{k_*} -> 0, k_* in P° with
s_{k_*} = +1 and margin mu_* := u_{k_*}(xi) - theta Phi_{k_*} > 0. Put lambda_* := q*(T) and
y := y^0 + (lambda_*/(m Phi_{k_*})) e_{k_*}, so R^* y = pi^ + lambda_* u_{k_*}. Writing
e_inf := R^* y - ((R^* y)(xi)/q_0) a one computes e_inf = (lambda_* u_{k_*} - T) + (delta_0 q*(tau_*) - lambda_* u_{k_*}(xi)/q_0) a,
and |lambda_* u_{k_*}(xi) - T(xi)| <= lambda_* delta_1 q**(xi), so q*(e_inf) <= 2 lambda_* delta_1 (1 + q**(xi)/q_0).
Also lambda_* mu_* <= lambda_* u_{k_*}(xi) <= delta_0 q*(tau_*) q_0 + lambda_* delta_1 q**(xi). Define the **inefficiency**
eps_1 := lambda_* mu_*/q_0 + q*(e_inf); it can be made as small as we wish by choosing delta_0, then delta_1.

*Step 2 (transport).* Take x'_N, f'_N, w'_N, b'_N, d'_N, v'_N, g'_N as in Theorem 7.1. Put
Lset_N := {k not in supp omega : |w'_N(k)| >= gamma}, y_N := sign(w'_N) 1_{Lset_N} + (lambda_*/(m Phi_{k_*})) e_{k_*}.
For N large, k_* is a peak of w'_N with sign +1 and margin mu'_{*,N} -> mu_* (finitely many quantities converge).
R^* y_N -> R^* y in l_1 by dominated convergence (for k not in supp omega with |w_k| != gamma, the indicator and the sign
eventually agree; terms are dominated by m Phi_k). Put beta_N := ((R^* y_N)(x'_N)/c_N) a and e_N := R^* y_N - beta_N;
then e_N -> e_inf in l_1. Let sigma'_N := |R x'_N| and e_{y,N} := 1 + <D w'_N, D y_N>/C'_N -> e_y := 1 + <D w, D y>/C >= 1
(D y_N -> D y in l_2 by dominated convergence). Using R x'_N(k) = sigma'_N (alpha'_k + Phi_k^2 w'_N(k)/C'_N) with
alpha'_k = 0 off the peaks and sum_{P'} |alpha'_k| = 1, one gets the bookkeeping identity

  (7.3)  y_N(R x'_N) = sigma'_N e_{y,N} + lambda_* mu'_{*,N} .

*Step 3 (the decomposition).* For tau in R and t put epsilon := tau rho^2 t^2 and
  A(t) := a + t rho b'_N + epsilon R^* y_N = (1 + epsilon y_N(R x'_N)/c_N) a + t rho b'_N + epsilon e_N,
  W(t) := w'_N + t rho v'_N - epsilon y_N ;
then A(t) + R^* W(t) = f'_N + t rho g'_N.
Base: by 1-homogeneity of q* and Step 4 of Theorem 7.1,
q*(A(t)) <= (1 + epsilon y_N(Rx'_N)/c_N)(1 + (rho^2 t^2/2) H_{b,N} theta(t)) + |epsilon| q*(e_N)
         = 1 + rho^2 t^2 [ H_{b,N} theta/2 + tau (sigma'_N e_{y,N} + lambda_* mu'_{*,N})/c_N + |tau| q*(e_N) ] + O(t^4).
Block, sup norm (0 <= epsilon small): coordinates in Lset_N \ {k_*} have modulus (1 - t rho d')|w'_N(k)| - epsilon
<= (1 - t rho d') M' - epsilon (equality on the peaks); k_* has value (1 - t rho d') M' - epsilon(1 + lambda_*/(m Phi_{k_*})),
which lies in [-((1-t rho d')M' - epsilon), (1-t rho d')M' - epsilon] as soon as epsilon lambda_*/(m Phi_{k_*}) <= M', i.e. for
|t| <= t_3 := (m Phi_{k_*} M/(2 |tau| lambda_*))^{1/2} (N large); coordinates in supp omega and those outside Lset_N
have modulus <= (1 - t rho d') max(M' - gamma_0, gamma) + rho|t| ||omega||_inf < (1 - t rho d') M' - epsilon for small t.
So ||W(t)||_inf = (1 - t rho d') M' - epsilon. Hilbert part: by (7.2) and a first-order expansion in epsilon,
||D W(t)|| <= C' + t rho d' M' + (rho^2 t^2/2) H'_N theta(t) - epsilon <D w', D y_N>/C' + O(|t|^3)
(uniformly in N, since ||D y_N||_2 is bounded and C'_N is bounded below). Hence
N(W(t)) <= 1 + rho^2 t^2 [ H'_N theta/2 - tau e_{y,N} ] + O(|t|^3).

*Step 4 (equalisation).* Let N -> infinity in the coefficients and choose
tau := (H_N - H_b)/(2 (e_y/q_0 + eps_1)) >= 0. The limiting levels are
base: H_b/2 + tau(sigma e_y/q_0 + eps_1), block: H_N/2 - tau e_y; they coincide (use sigma/q_0 + 1 = 1/q_0) and equal
Gamma_eff/2 with
  Gamma_eff = H_N - q_0 (H_N - H_b)/(1 + q_0 eps_1/e_y) <= Gamma_w + H_N eps_1 .
Choose delta_0, delta_1 (hence eps_1) so small that rho^2 (Gamma_w + H_N eps_1) < 1; this is possible since Gamma_w <= 1.
By the uniform bounds of Step 3 there are t_4 > 0 and N_4 such that p*(f'_N + t rho g'_N) <= max(q*(A), N(W))
<= sqrt(1 + t^2) for |t| <= t_4 and N >= N_4.

*Step 5 (large t, conclusion).* Exactly as Steps 6-7 of Theorem 7.1.

*Step 6 (case H_b > H_N).* Take tau < 0, i.e. raise all coordinates in Lset_N by |epsilon|; to keep the transfer coordinate
inside the new sup norm, use y_N := sign(w'_N) 1_{Lset_N} - (lambda_*/(m Phi_{k_*})) e_{k_*} with the transfer peak now
chosen for the target T := -tau_* + delta_0 q*(tau_*) a (again T(xi) > 0, so k_* is a robust peak of sign +1); the same
computation gives levels converging to Gamma_eff/2 with Gamma_eff <= Gamma_w + H_b eps_1. []

Remark (several blocks). With one transfer peak k_{*,m} and one parameter tau_m per block, the base level is
H_b/2 + sum_m tau_m(sigma_m e_{y,m}/q_0 + eps_{1,m}) and block m's level is H_m/2 - tau_m e_{y,m}; equalising all of them
gives the common value Gamma_w/2 + O(max_m eps_{1,m}) (solve for tau_m in terms of the common level L, insert in the
base equation, use q_0 + sum sigma_m = 1). The ingredients of the proof are unchanged.

**Numerical confirmation** (C_work/transfer_explicit2.py; the finite model of Prop. 8.2 with one additional deep
coordinate u_6 := T/q*(T), Phi_6 = 0.45^10): the explicit decomposition of Steps 1-4 at t = 1e-2 and 3e-3 gives
Gamma_eff = 0.392, 0.327, 0.307, 0.3005 for delta_0 = 0.1, 0.03, 0.01, 0.003, against Gamma_w = 0.298 and
Gamma_max = 2.86; the measured values match the formula H_N - q_0(H_N - H_b)/(1 + q_0 eps_1/e_y) (e.g. 0.393 predicted for
delta_0 = 0.1). Without the transfer coordinate the true coefficient of the same model is about 0.36 (Prop. 8.2).

**Corollary 7.2. [PROVED]** (a) Preprint A's theorem "weighted directions" no longer depends on [Check]: the step
"local-certificate recovery" is Theorem 7.1 (or 7.4) with b = 0 and one block, for arbitrary a (Remark 7.1';
Preprint A's theorem does not assume a in c_00, so the remark is needed).
(b) Common first rows: the canonical f'_N recover simultaneously every balanced finite certificate g with
(f,g) contractive and Gamma_w(g) <= 1, and all norm limits of such (by (R3) of the briefing).
(c) Upper bound for the second-order coefficient (apply Steps 1-4 at f itself, i.e. "N = infinity"):
for every balanced finite certificate, limsup_{t->0} (p*(f + t g)^2 - 1)/t^2 <= Gamma_w(g).
(d) If f is tame with K and all Dg_m empty, then every g in C(f) with Gamma_w(g) <= 1 is recoverable
(Prop. 6.5 puts every mate in the form of Definition 7.0).

**Remark 7.2' (weighted directions with the sharp coefficient). [SKETCH]** In Preprint A's theorem on weighted
directions (unbounded omega with sum_k lambda_k omega_k^2 < infinity on a half-peak set) the hypothesis "H <= 1" can be
replaced by "Gamma_w <= 1": the transfer peak of Theorem 7.4 depends only on f and on the cut-off gamma (take gamma
above M/2, the half-peak level), not on the truncation index J, so the rebalanced bound holds uniformly in J and
Preprint A's truncation argument goes through unchanged.

**Remark 7.3 (kinks).** If b has a component on a kink coordinate j in K, q*(a + t b) has a first-order term
|t|(|b_j| - z_j b_j) for one sign of t: certificates cannot contain kink components. Mates with such components
(supported for the "bad" sign by block curvature) are not covered.

---

## 8. The second-order coefficient

For a balanced finite certificate g at f put Gamma_2^+(g) := limsup_{t->0} (p*(f+tg)^2 - 1)/t^2 and Gamma_2^- := liminf.
A necessary condition for g in C(f) is Gamma_2^+(g) <= 1.

**Proposition 8.1 (the sharp second-order coefficient). [PROVED]** Let f have a in c_00 and g be a balanced finite
certificate. Then Gamma_2^+(g) <= Gamma_w(g) <= Gamma_max(g) (Corollary 7.2(c)). If moreover every block has finitely
many strict non-peaks, no degenerate peaks, and (MS) (i.e. (T3), (T4) with Dg = empty), then Gamma_2^-(g) >= Gamma_w(g).
Hence Gamma_2(g) = Gamma_w(g), and every balanced finite certificate in C(f) satisfies Gamma_w(g) <= 1.

Proof of the lower bound. Since g(xi) = 0, for any eta_t = xi + t nu + t^2 nu_2 in X** with Delta(eta_t) = O(t^2),

  (8.1)  p*(f + t g) >= (f + t g)(eta_t)/p**(eta_t) = (f(eta_t) + t^2 g(nu) + t^3 g(nu_2))/(f(eta_t) + Delta(eta_t))
                      = 1 + t^2 g(nu) - Delta(eta_t) + O(t^3),

because f(eta_t) = 1 + O(t) and p** = f + Delta (Lemma 6.1). No constraint f(nu) = 0 is needed (the ratio is
invariant under scaling of eta_t). By Lemma 6.1, Delta(eta_t) = E_q(eta_t - xi) + sum_m E_m(R_m**(eta_t - xi)).

*(i) Base test directions.* Write sigma_F := sign a_F, so xi_j/q_0 = sigma_j + (Ue)_j on F. Fix k_perp in
E_F := span{U^* e_j^* : j in F} with <k_perp, e> = 0 (note e in E_F). Put kappa_2 := ||U^*a|| ||k_perp||^2/(2 q_0),
kappa'_2 := -kappa_2 ||a||_1/||U^*a||, and let k_{2,perp} in E_F be the solution of
<k_{2,perp}, U^* e_j^*> = -kappa_2 sigma_j - kappa'_2 (Ue)_j (j in F) [the Gram matrix of (U^* e_j^*)_{j in F} is invertible since
U^* is injective; the solution is orthogonal to e because sum_F a_j(-kappa_2 sigma_j - kappa'_2 (Ue)_j)
= -kappa_2 ||a||_1 - kappa'_2 ||U^*a|| = 0]. Set k_2 := kappa'_2 e + k_{2,perp}, so (U k_2)_j = -kappa_2 sigma_j on F. Define
nu := (U k_perp)_F + (U k_perp)_{F^c} + nu_c = U k_perp + nu_c and nu_2 := (U k_2)_{F^c}, where nu_c is finitely supported in
J (free coordinates) and will be chosen in (iii). Let H := q_0 e + t k_perp + t^2 k_2 and Z := eta_t - U H. Then
Z_j = q_0 sigma_j + t^2 kappa_2 sigma_j on F (since (U k_perp)_j - (U k_perp)_j = 0 and -(U k_2)_j = kappa_2 sigma_j), and
Z_j = q_0 z_j + t (nu_c)_j off F. For small t: |Z_j| = q_0 + t^2 kappa_2 on F, |Z_j| <= q_0 off F (coordinates outside supp nu_c
do not move; the finitely many in supp nu_c have |z_j| < 1). Also
||H||^2 = q_0^2 + t^2 ||k_perp||^2 + 2 q_0 t^2 kappa'_2 + O(t^3), so ||H|| = q_0 + t^2(||k_perp||^2/(2q_0) + kappa'_2) + O(t^3)
= q_0 + t^2 kappa_2 (1 - ||a||_1)/||U^*a|| + O(t^3) = q_0 + t^2 kappa_2 + O(t^3), using q*(a) = 1. Hence
q**(eta_t) <= q_0 + t^2 kappa_2 + O(t^3) (1.2). Since a(nu) = <U^*a, k_perp> = 0 and a(nu_2) = 0,

  E_q(eta_t - xi) <= (t^2/2) ||U^*a|| ||k_perp||^2/q_0 + O(t^3),    and   b(nu) = <k_perp, U^* b>   (b supported in F).

*(ii) Block upper bound.* General form of Lemma 5.1(a): if s_k alpha_k < 0 for some peaks, then
||alpha||_1 = 1 + 2 sum_P (-s_k alpha_k)_+, hence |y| <= Lambda(S_P(y), Y_Q(y)) + 2 sum_{k in P}(lambda rho_0 Phi_k^2 - s_k y_k)_+
(whenever 0 < Y <= S). Apply this in block m to y := z_m + t delta_1 + t^2 delta_2, delta_1 := R_m** nu,
delta_2 := R_m** nu_2, with the peak set and signs of z_m. Q_m is finite, so Y_Q(y) < infinity and Lambda is C^infinity near
(S_P(z_m), Y_Q(z_m)); since dLambda/dS = M and dLambda/dY = C Y/|z| (Lemma 5.1), the first-order terms of
Lambda(S_P(y), Y_Q(y)) equal w_m(t delta_1 + t^2 delta_2), and Lambda(...) = sigma_m + w_m(t delta_1 + t^2 delta_2)
+ (t^2/2) H^blk_m(delta_1) + O(t^3) with the quadratic form of Lemma 5.1(iii):
H^blk(delta) = (C/|z|) ||P_perp D^{-1} delta_Q||^2 + (Lambda_SS/Y^2)(Y sigma_1 - S sigma_2)^2.
Overshoot: lambda(y) rho_0(y) = |z| M/C + O(t), and for k in P, s_k y_k = |z||alpha_k| + |z| Phi_k^2 M/C + t s_k delta_{1,k}
+ t^2 s_k delta_{2,k} with |z||alpha_k| = m Phi_k mu_k and |delta_{i,k}| <= m Phi_k q**(nu_i); so each overshoot term is
<= m Phi_k (|t| B - mu_k)_+ with B bounded, and their sum is o(t^2) by (MS) (all peaks are non-degenerate).
Hence E_m(t delta_1 + t^2 delta_2) <= (t^2/2) H^blk_m(delta_1) + o(t^2).

*(iii) Decoupling.* By (F5) (independence lemma), nu_c in c_00(J) can be chosen so that the finitely many numbers
(u_{k,m}(nu))_{k in Q_m} and pi_m(nu) (m in I) take any prescribed values, k_perp being fixed. H^blk_m(delta_1) and
v_m(delta_1) depend only on ((delta_1)_{Q_m}, S_{P_m}(delta_1)), i.e. on these numbers. With (8.1):
liminf_{t->0} (p*(f+tg) - 1)/t^2 >= (1/2) [ sup_{k_perp} (2<k_perp, U^*b> - ||U^*a|| ||k_perp||^2/q_0) + sum_m L_m ],
L_m := sup over block data of [2 v_m(delta) - H^blk_m(delta)].

*(iv) The base supremum* equals q_0 ||P_perp U^* b||^2/||U^*a|| = q_0 H_b (take k_perp = (q_0/||U^*a||) P_perp U^* b, which lies in
E_F and is orthogonal to e).

*(v) The block suprema.* Drop m; write omega~ := (omega - d w)|_Q, h^ := h_0/Y with h_0 := D^{-1} z_Q, zeta := D^{-1} delta_Q =
sigma_2 h^ + zeta_perp, sigma_1 := S_P(delta), r := Y sigma_1 - S sigma_2. Then v(delta) = <D omega~, zeta> - d M sigma_1 and
2v - H^blk = [2<D omega~, zeta_perp> - (C/|z|)||zeta_perp||^2] + [2(<D omega~, h^> sigma_2 - d M sigma_1) - (Lambda_SS/Y^2) r^2].
The linear form <D omega~, h^> sigma_2 - d M sigma_1 vanishes on the radial direction (sigma_1, sigma_2) = (S, Y): indeed
Y<D omega~, h^> - d M S = (omega - d w)(z_Q) - d w(z_P) = v(z) = 0 (balance). Hence it equals (-d M/Y) r, and
L = (|z|/C) ||P_perp D omega~||^2 + d^2 M^2/Lambda_SS. Put c_Q := ||D w_Q||^2, so C^2 = c_Q + M^2 F2 and h^ = D w_Q/sqrt(c_Q).
A direct computation gives ||P_perp D omega~||^2 = ||D omega||^2 - d^2 C^2/c_Q. From Lemma 5.1 at z (rho_0 = M/C,
S/|z| = 1 + rho_0 F2, Y^2/|z|^2 = 1 - rho_0^2 F2 = c_Q/C^2) one gets sqrt(S^2 - (1-F2)Y^2) = |z| sqrt(F2)/C and
Lambda_SS = sqrt(F2) Y^2/(S^2 - (1-F2)Y^2)^{3/2} = C c_Q/(|z| F2). Therefore
L = (|z|/C)(||D omega||^2 - d^2 C^2/c_Q) + d^2 |z| M^2 F2/(C c_Q) = (|z|/C)(||D omega||^2 - d^2 (C^2 - M^2 F2)/c_Q)
  = (|z|/C)(||D omega||^2 - d^2) = sigma H_N.
(Degenerate case z_Q = 0, i.e. Y = 0, possible when u_k(xi) = 0 for all k in Q: then w_Q = 0, c_Q = 0, d = 0. Lambda
depends on Y only through Y^2 and Lambda(., 0) is linear with slope M, so the expansion of (ii) holds with
E = (t^2/2)(C/|z|)||D^{-1}(delta_1)_Q||^2 + O(|t|^3) + overshoot, there is no rank-one term, v(delta) = <D omega, D^{-1} delta_Q>,
and L = (|z|/C)||D omega||^2 = sigma H_N directly.)
Summing: liminf (p*(f + t g) - 1)/t^2 >= Gamma_w/2, i.e. Gamma_2^- >= Gamma_w. []

(Numerical cross-check of (ii)-(v): C_work/lowerbound_test.py, the finite model of Prop. 8.2 with the pure block
certificate: Lambda_SS from its closed form 0.1117438201565800 vs C c_Q/(|z| F2) = 0.1117438201565800; block Legendre value
L = 0.29824 vs sigma H_N = 0.29822; the explicit test points give 2(ratio - 1)/t^2 = 0.2636, 0.2889, 0.2952 at
t = 1e-2, 3e-3, 1e-3, converging to Gamma_w = 0.2982.)
(Numerical cross-check of (iv): C_work/base_hess.py, primal supremum 1.1106 vs q_0 H_b = 1.1086. The naive base
decomposition that keeps the cube part on its face gives the Hessian ||k_perp||^2/q_0, too large by the factor
1/||U^*a||; the decomposition above lets cube and Hilbert parts rise together to the common level kappa_2, which is
the LP-optimal choice with multipliers (|a_j|)_{j in F} and ||U^*a||.)

**Proposition 8.2 (finite-dimensional face formula). [SKETCH + numerics]** In finite-dimensional models
(c_0 replaced by R^n, one block with finitely many coordinates) transfer peaks need not exist, and the lower bound
argument shows that the unit ball has an exactly flat face through the normer along the rebalancing direction of
Lemma 6.6. Along it the base/block split (q(y_s), |R y_s|) varies affinely, H_b and H_N stay fixed, and the local
coefficients are q(y_s) H_b + |R y_s| H_N; hence Gamma_2 = the weighted average at the *most unfavourable split reachable
along the face*, between Gamma_w and Gamma_max.
Numerics (C_work/rebalance_test.py, face_test.py, dual_mech.py): n = 6, d = 3, K = 5 block coordinates, F = {3,4,5},
Q = {1}, q_0 = 0.8958, sigma = 0.1042, pure block certificate with H_N = 2.862: Gamma_w = 0.298, Gamma_max = 2.862;
numerically minimised dual decompositions give Gamma ~ 0.355-0.362; the face was traced exactly (p - 1 = 0 to 1e-16 for
s in [-0.01, 0.05]) with sigma_s ranging over [0.059, 0.113+]; predicted sigma_max H_N ~ 0.33-0.34. The optimal dual
decomposition found numerically lowers *all* peak coordinates uniformly by 0.732 t^2 (the finite-dimensional version of
the transfer in Theorem 7.4, where the finite peak set makes pi^ "cheap" but not free).

**Discussion 8.3.** In Martín's space the density of every tail of (u_{k,m})_k supplies transfer peaks at all depths,
so the infinite-dimensional second-order coefficient of a finite certificate is at most the weighted average
(Corollary 7.2(c)) - in contrast to finite-dimensional models - and, at tame supports, equal to it
(Prop. 8.1). The "rebalancing obstruction" suspected after Theorem 7.1 therefore does not occur for finite
certificates: Theorem 7.4 recovers every balanced finite certificate that satisfies the sharp second-order condition.

**Theorem 8.4 (tame supports are recoverable). [PROVED]** Let f in S_{p*} be tame (Def. 6.0) with K = empty and all
Dg_m = empty. Then (f, rho g) belongs to the closure of
NA((c_0,p), l_2^2) for every g in C(f) and every rho < 1, i.e. f lies in the recoverable set R of the briefing.
Proof. By Theorem 6.4 and Prop. 6.5 every g in C(f) is a balanced finite certificate; by Prop. 8.1 (lower bound)
Gamma_w(g) <= Gamma_2^-(g) <= Gamma_2^+(g) <= 1 (the last inequality because p*(f + t g) <= sqrt(1+t^2)); apply
Theorem 7.4. []
