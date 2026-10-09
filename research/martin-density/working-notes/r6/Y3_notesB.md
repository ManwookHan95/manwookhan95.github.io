
## 3. Item (1): non-sparse support swallowing.

### 3.1 Un-switching. PROVED (any admissible T, any F).
Lemma 3.1. Let l = (k, m) be a carrier with w_m(k) = 0 (d-neutral; then k in Q_m) and c in R. The pair P_l(c) := (c u_l,
-(c/lambda_l) e_k in block m) represents the zero functional, d_m(e_k) = 0, its base part vanishes at xi, and
  Gamma_w(P_l(c)) <= c^2 C_un(l)^2,   C_un(l)^2 := q_0||U||^2/nu + sigma_m/(m^2 C_m).
Hence if (b^-, omega^-) represents g, so does (b^-, omega^-) + P_l(c), and sqrt(Gamma_w((b^-,omega^-) + P_l(c))) <=
sqrt(Gamma_w(b^-, omega^-)) + |c| C_un(l).
Proof. R_m* e_k = lambda_l u_l; d_m(e_k) = Phi_m(k)^2 w_m(k)/C_m = 0. u_l(xi) = q_0 u_l(zhat) and (R_m** xi)(k) = lambda_l q_0 u_l(zhat) =
sigma_m Phi_m(k)^2 w_m(k)/C_m = 0 (lem:threshold, k strict non-peak). h(u_l) <= ||U||^2||u_l||_1^2/nu <= ||U||^2/nu; H_m(e_k/lambda_l) <=
||D_m e_k||^2/(lambda_l^2 C_m) = 1/(m^2 C_m). sqrt(Gamma_w) is a seminorm on pairs (sum of positive semidefinite quadratic forms). QED

### 3.2 The design D_sigma. PROVED.
Definition 3.2. D_sigma is the SLD operator (or SLD_G, D''', or the explosive design; the change is compatible with each) with:
(D0') each S_l has bounded gaps (e.g. S_l := {2^l(2i+1) : i >= 1} minus {j_0}); (D1)(c) a target allowed at l meets S_{l'} (l' < l) only
at coordinates s <= l.
Proposition 3.3. D_sigma is admissible, satisfies (P1)-(P3), does not depend on N, and every result of Section 8, of Z3-Z6 and of R1 valid
for the underlying design holds for D_sigma.
Proof. (D1)(c) removes targets from the allowed sets; a finitely supported target satisfies (c) once l >= max supp y^{(i)}, and (a), (b) at all
large l, so (T-d) holds as in Theorem thm:SLD; (T-a)-(T-c), (P1)-(P3) use only (a), (b), c_{l+1} <= c_l/4. The cited results use only
(T-a)-(T-d), (P1)-(P3), allowedness (a), (b) and (for SLD_G, D''', explosive) recursions in which (c) is one more condition fixed before
T_hi(l) is chosen. Nothing depends on N. QED

### 3.3 The constrained-switching bound. PROVED.
Setting. l_0 a carrier of block m_0 with S_{l_0} subset F up to finitely many points; s_j = eps for all j in S_{l_0} cap F, j >= s_*
(monochromatic support swallowing); v := v_{l_0}; rho(s) := |a_s|/v(s) on S_{l_0} cap F; tau := -eps Delta theta_{l_0} (tau >= 0 free,
tau < 0 constrained); m(y) := sum{v(s) : s in S_{l_0} cap F, s >= s_*, rho(s) < y}; G_0 := max gap of S_{l_0}.
(QM) [quasi-monotonicity]: rho(s') <= C_Q rho(s) for s_* <= s < s' in S_{l_0} cap F.
Lemma 3.4. Design D_sigma. Let l_* >= max(l_0, s_*, max(S_{l_0} minus F)), t in W(l_*), t <= min(t_eta, 1), and (B_+-, Theta_+-) a
two-sided decomposition of g in C(f) at scale t; D := (tau)_-.
(a) D m^{>l_*}(tD/4) <= t/q_0 + 32t^2, where m^{>l_*}(y) := sum{v(s) : s in S_{l_0} cap F, s > l_*, rho(s) < y}.
(b) Under (QM): D <= max(D^#(t), K_sigma(l_*) t), with D^#(t) := sup{D' > 0 : D' m(tD'/(4C_Q)) <= t/q_0 + 32t^2} and
    K_sigma(l_*) := (1/q_0 + 32)/M(l_*), M(l_*) := sum{v(s) : s in S_{l_0}, s > l_*} >= delta_{l_0} 2^{-l_* - G_0}/n_{l_0}.
(c) If m(y)/y -> infinity (y -> 0) then D^#(t) < infinity and D^#(t) -> 0 (t -> 0); hence sup_{t in W(l_*)} D -> 0 as l_* -> infinity.
Proof. (a) For s in S_{l_0}, s > l_*: by (P1) and (eq:DeltaB), -Delta B(s) = Delta theta_{l_0} v(s) + sum_{l' > l_0} Delta theta_{l'}
y_{l'}(s)/n_{l'} (coarser targets vanish on S_{l_0} by (a); other signatures vanish there). For l_0 < l' <= l_*, (D1)(c) gives
supp y_{l'} cap S_{l_0} subset [1, l'] subset [1, l_*]; so only l' > l_* contribute, r(s) := sum_{l' > l_*}Delta theta_{l'}y_{l'}(s)/n_{l'},
and sum_s|r(s)| <= (4/3)sum_{l' > l_*}|Delta theta_{l'}| <= 8t^2 (lem:box, (P2), t >= T_lo(l_*)). For s in F with s_s = eps:
s_s Delta B(s) = tau v(s) - eps r(s), so (s_s Delta B(s))_- >= D v(s) - |r(s)|; and (s_s Delta B(s))_- <= (s_sB_+(s))_- + (s_sB_-(s))_+ <=
2|a_s|/t + f^+_s + f^-_s. If rho(s) < tD/4 then 2|a_s|/t < D v(s)/2, so D v(s)/2 <= f^+_s + f^-_s + |r(s)|. Sum: (D/2)m^{>l_*}(tD/4) <=
t/(2q_0) + 8t^2.
(b) Case A: no s in S_{l_0} cap F with s_* <= s <= l_* has rho(s) < tD/(4C_Q). Then m(tD/(4C_Q)) <= m^{>l_*}(tD/(4C_Q)) <= m^{>l_*}(tD/4)
and (a) gives D m(tD/(4C_Q)) <= t/q_0 + 32t^2, i.e. D <= D^#(t) (D' -> D' m(tD'/(4C_Q)) is nondecreasing). Case B: some s_1 in [s_*, l_*]
has rho(s_1) < tD/(4C_Q); by (QM) every s > l_* in S_{l_0} (all such s lie in F) has rho(s) < tD/4, so m^{>l_*}(tD/4) = M(l_*), and (a)
gives D <= K_sigma(l_*)t. The bound on M(l_*): the first element of S_{l_0} after l_* is <= l_* + G_0.
(c) m(y)/y -> infinity forces m(y) > 0 for all y > 0, so D' m(tD'/(4C_Q)) -> infinity as D' -> infinity and D^#(t) < infinity. If
D^#(t_n) >= eta_1 > 0 along t_n -> 0, then eta_1 m(t_n eta_1/(4C_Q)) <= t_n/q_0 + 32 t_n^2, i.e. m(y_n)/y_n stays bounded along
y_n := t_n eta_1/(4C_Q) -> 0: contradiction. Finally K_sigma(l)T_hi(l) <= C_f 2^{l} 2^{-l^3} -> 0 by (P3). QED
Remark (role of (D1)(c)). Without it, targets of COARSE good carriers may sit on the deep part of S_{l_0}; their switching is pinned only in
total (<= K_* t), and K_* t can absorb all constrained usage there: the budget then gives D m(tD/4) <~ K_* t, useless at design windows.
(D1)(c) confines coarse targets to s <= l_*, where (QM) yields the dichotomy. (HEURISTIC remark; Lemma 3.4 is PROVED.)

### 3.4 Theorem SC. PROVED.
Definitions (at arbitrary F, as in R1): r_l := min_{sigma = +-1} sum_{s in S_l \ F} v_l(s)(1 + sigma z_s), B := {l : r_l = 0},
good l: S*_l, r*_l, Lambda*_f; (W*), (H2), (H3-inf), (B_fin) as in R1; U_E := sum_{l in E}|u_l| and m_E(y) := sum{U_E(j) : j in F,
|a_j| < y U_E(j)} for E subset B. A bad carrier l is SUPER-CRITICAL SWALLOWED (l in B_sc) if (i) supp u_l subset F; (ii) w_{m(l)}(k(l)) = 0;
(iii) a is monochromatic on S_l beyond some s_* (sign eps_l) and (QM) holds; (iv) m_l(y)/y -> infinity.
Theorem 3.5 (SC). Design D_sigma, every N. If f (F arbitrary) satisfies (W*), (H2), (H3-inf), (B_fin) and (CS_{B \ B_sc}):
m_{B \ B_sc}(y) = o(y), then f in Rec.
Proof. R1's proof with the following changes; notation of R1 (l_*, t in W(l_*), K* := (1/q_0 + 22)Lambda*_f(l_*), C_f, C_tau, ...).
Step 1, Lemma lem:badpeaks: verbatim. Step 2 (projection onto the cone Z_f): for l in B_sc, tau_l occurs in no row of Z_f (no target row,
as u_l vanishes off F; no sign row, l in B_F; no peak row; no d-row, q_l = 0), so we take tau'_l := tau_l on B_sc. Step 2': |tau'_l| <= C_tau.
Step 3 (data) with
  Xt := sum_{l in B \ B_sc} eps_l tau'_l u_l + sum_{l in B_sc} eps_l (tau'_l)_+ u_l,  tau~_l := tau'_l (l notin B_sc), (tau'_l)_+ (l in B_sc).
Xt 1_{F^c} = X 1_{F^c} = V' (as supp u_l subset F on B_sc), so chi, e_+- of lem:split are R1's. A_j := 2|a_j|/t, D_t := {j in F :
s_j Xt_j < -2A_j}; b^+_1 := common shift off D_t (point of [y_j - A_j, x_j + A_j] closest to 0, x_j := s_jB_+(j), y_j := s_j(B_+(j) - Xt_j))
and b^+_1(j) := -s_jA_j on D_t; b^+ := b^+_1 + chi V' - kappa a with kappa := (b^+_1 + chi V')(zhat); b^- := b^+ - Xt; omega^+ as in R1;
omega^- := omega^+ + sum_{l in B_np}(eps_l tau~_l/lambda_l)e_{k(l)}; g_t := b^+ + sum_m R_m*(omega^+_m - d_m(omega^+_m)w_m).
Claim A. For t <= t_sc (f-constant) and j in F: |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B - X)_j|; s_jb^+_1(j) >= -A_j; and
s_j(b^+_1 - Xt)(j) <= A_j off D_t.
Proof. y_j = s_jB_-(j) + e_j + d_j, e_j := s_j(Delta B - X)_j, d_j := s_j(X - Xt)_j = -sum_{B_sc}(tau'_l)_- s_j eps_l u_l(j). On S_l cap F,
j >= s_* (l in B_sc), s_j eps_l u_l(j) = v_l(j) >= 0, so d_j <= 0; d_j != 0 elsewhere only on the finite set T_sc := union_{B_sc}(supp y_l
union (S_l cap [1, s_*])), where |d_j| <= C_tau sum_{B_sc}|u_l(j)| <= |a_j|/t for t <= t_sc := min_{T_sc}|a_j|/(C_tau|B|). Off D_t:
|sigma_j| = (-x_j - A_j)_+ + (y_j - A_j)_+ <= f^+_j + (f^-_j + |e_j| + (d_j)_+ - |a_j|/t)_+ <= f^+_j + f^-_j + |e_j| (x_j >= -|a_j|/t - f^+_j,
s_jB_-(j) <= |a_j|/t + f^-_j). On D_t: x_j + A_j >= -f^+_j, and x_j + A_j = y_j + s_jXt_j + A_j < y_j - A_j <= f^-_j + |e_j|. QED
Claim B. For t <= t'_sc (f-constant): D_t subset {j : C_tau U_{B\B_sc}(j) > 2A_j} and |Xt_j| <= C_tau U_{B \ B_sc}(j) on D_t.
Proof. On S_l cap F (l in B_sc) outside the finite set of target coordinates of the other bad carriers and outside T_sc,
s_jXt_j = (tau'_l)_+ v_l(j) >= 0. On these finite shallow sets |Xt_j| <= C_tau|B| <= 2A_j for small t. Elsewhere the B_sc-terms vanish. QED
(a) Two-piece data: off F, b^+ = chi V', b^- = -(1-chi)V'; b^+ - b^- = Xt = sum_m R_m*(omega^-_m - omega^+_m); d(omega^-) - d(omega^+) =
sum q_l tau~_l = sum q_l tau'_l = 0 (q_l = 0 on B_sc; cone rows); b^+-(xi) = 0 (lem:algebra).
(b) On F: (s_jb^+_j)_- <= 3|a_j|/t; (s_jb^-_j)_+ <= 3|a_j|/t off D_t and <= C_tau U_{B\B_sc}(j) on D_t (Claims A, B; |kappa||a_j| <= |a_j|/t
for small t); |b^+-_j| <= 3|a_j|/t + 2C_tau U_B(j), so t||b^+-||_1 <= A^R_0.
(c) + data: closeness ||g - g_t||_1 <= K^R_2 t and sqrt(Gamma_w(b^+, omega^+)) <= sqrt(1 + eta_Gamma) + K^R_4 t, as in R1 (Claim A gives R1's
closeness of b^+_1 to B_+ 1_F).
(d) - data: (b^-, omega^-) = Q - sum_{l in B_sc} P_l(eps_l(tau'_l)_-)... precisely (b^-, omega^-) = Q + sum_{l in B_sc}P_l(-eps_l(tau'_l)_-)
with Q := (b^+ - X, omega^+ + sum_{B_np}(eps_l tau'_l/lambda_l)e_{k(l)}) [check: P_l(-c) = (-c u_l, (c/lambda_l)e_{k(l)}) and
X - Xt = -sum_{B_sc}eps_l(tau'_l)_- u_l]. Q is the - pair R1 would build from b^+ and X; R1's comparison of it with (B_-, Theta_-) uses only
Claim A, Delta B - X = O(K* t) and the box bounds, hence sqrt(Gamma_w(Q)) <= sqrt(1 + eta_Gamma) + K^R_4 t. By Lemma 3.1,
sqrt(Gamma_w(b^-, omega^-)) <= sqrt(1 + eta_Gamma) + K^R_4 t + C_un sum_{l in B_sc}(tau_l)_-   (tau'_l = tau_l on B_sc).
(e) Block size conditions: as in R1 (A_2 := 4 + C_tau/lambda_B).
Step 4: Lemma R2 with U_* := U_{B \ B_sc}, C_* := 2C_tau ((b) is exactly its hypothesis; m_*(y) = o(y) is (CS_{B\B_sc})).
Step 5: choose windows l_j by (W*) as in R1, then j so large that, in addition, C_un sup_{t in W(l_j)} sum_{B_sc}(tau_l)_- <= kappa_0/2
(Lemma 3.4(c), applied to each l in B_sc: (iii) gives (QM) and monochromaticity, (i) gives S_l subset F) and t <= t_sc, t'_sc on W(l_j).
Every piece then has Gamma_w <= (1 + 2kappa_0)^2 = 1 + eta_0/2 on both sides; Lemma lem:avgfunctionals: rho gbar_j in C(f), rho gbar_j ->
rho g. The averaged data are d-neutral two-piece data with kappa_w(rho Dbar_j) <= 1; by (b) and convexity, (s bbar^+)_- <= 3|a|/T_lo(l_j)
and (s bbar^-)_+ <= 3|a|/T_lo(l_j) + C_tau U_{B\B_sc}, so (CS-side) holds (Lemma 1.1(b): m(x) <= 2m_{3|a|/T_lo}(2x) + 2 m_{C_tau U}(2x) =
0 + o(x) for small x). Theorem 2.1 (no condition on bbar^theta, which is NOT sparse here: on S_l cap F, |b^theta_j| can be of order
(tau'_l)_+ v_l(j)) with I_- empty gives (f, rho gbar_j) in cl NA. Let j -> infinity, then rho -> 1. QED
Remarks 3.6. (a) Scope: in the model v_l(s) = c_0 2^{-s}, |a_s| = 2^{-(1+b)s} on S_l (S_l, supp y_l subset F, w(k(l)) = 0), (QM) holds and (iv)
iff b > 1; with R1 (b < 1) the model is settled except b = 1 (critical). (b) Hypothesis (i) can be relaxed: if a target coordinate j notin F
of l is a contact with z_j eps_l y_l(j) < 0, un-switching moves an admissible amount there; if it is a contact with z_j eps_l y_l(j) > 0 or a free
coordinate, the constrained direction of l is pinned at O(t) by the switching budget at j and Step 2's projection (with the row tau_l >= 0)
handles it. (SKETCH: bookkeeping not written.) (c) Hypothesis (ii) is needed off F: un-switching a carrier with q_l != 0 creates
Delta d_m = q_l(tau'_l)_- != 0, whose representation puts -Delta d_m R_m* w_m into b^+ - b^-, which is not side-admissible off F in general
(Remark rem:S(b)). At F = N it is admissible; see Theorem 5.1, where no un-switching is needed at all. (d) Illustration (HEURISTIC): if
the signature profile gamma_j := eps_l g_j/v_l(j) of a mate oscillates on the deep part of S_l, the cushion lemma forces persistent FREE
switching (tau_l)_+ of about the oscillation range at every small scale; this makes |b^theta| non-sparse, which is why Theorem 2.1 is used.

### 3.5 The critical case b = 1. Analysis; the open step.
(i) PROVED (arithmetic of the methods). For a critical carrier, D^#(t) of Lemma 3.4 stays bounded away from 0 (check_Dsharp.py: D^# ~ 7-9 for
t = 1e-3 ... 1e-11, oscillating), so un-switching costs Gamma of order C_un D (not o(1)); deep-assignment data (R1) pay at scale r the flips
Exc_beta(r) ~ kappa_beta(r D) D^2 r^2 with an oscillating local constant (Lemma 1.2), while the decomposition at scale t paid kappa(tD) D^2 t^2;
a companion making the constrained switching cushion-compatible on a window [T_lo, T_hi] costs ~ T_hi D m_l(T_hi D) ~ T_hi^2 >> T_lo^2,
so Z3 Theorem E does not apply.
(ii) HEURISTIC (worst-scale principle). Fixed data built at scale t are valid at all smaller scales r iff their flip coefficient
Fl_r = 2q_0 Exc(r)/r^2 does not exceed Fl_t (plus slack), i.e. iff t is an "upper point" of r -> Mbar(rD) := (rD)^{-2} int_0^{rD} m;
for geometric signatures and monotone critical profiles Mbar is log-periodic (Lemma 1.2 and the scaling int_0^{2Y} = 4 int_0^Y), so upper points
recur in every bounded log-interval; a window theorem would select pieces at upper points (the averaging lemma only needs scales with ratio
>= 2). Obstacles to a proof: the phase depends on the scale-dependent amplitude D_t; non-periodic oscillation may have sparse upper points.
(iii) OPEN: critical support swallowing (0 < liminf m_l(y)/y, limsup m_l(y)/y < infinity), and mixed profiles.

## 4. Item (4): the exact one-sided coefficient at arbitrary F.

"Block-tame" := every Q_m finite, no degenerate peaks, (MS) at xi; nothing on F, K. Side-+ admissible pair at arbitrary F: b in l_1, b = 0
on J, z_jb_j >= 0 on K, no condition on F, omega_m in R^{Q_m}, representing g. gamma^+-(g) := inf Gamma_w over side-+- admissible pairs.

Theorem 4.1. T admissible, I finite, f block-tame with F arbitrary, g in X* with g(xi) = 0. Then:
(a) liminf_{t->0+} 2(p*(f+tg) - 1)/t^2 >= gamma^+(g) (same for t -> 0- and gamma^-);
(b) if gamma^+(g) < infinity the infimum is attained;
(c) for every side-+ pair (b, omega): limsup_{t->0+} 2(p*(f+tg)-1)/t^2 <= Gamma_w(b,omega) + 2q_0 limsup_{t->0+} Exc_{(sb)_-}(t)/t^2
    (side -: (sb)_+, t -> 0-);
(d) the limit equals gamma^+(g) if some optimal side-+ pair has Exc_{(sb)_-}(t) = o(t^2) (e.g. (sb)_- cushion-sparse); for F finite this is
    Theorem thm:onesided(a);
(e) every g in C(f) has optimal two-piece data with kappa_w <= 1.
Proof. (a) Steps 1-4 of the proof of Theorem thm:onesided, with Step 1 replaced by the following test points, valid for every F:
for k in H with <k,e> = 0 and chi_c in C_+ := {chi in c_00 : chi = 0 on F, z_j chi_j <= 0 on K}, put kappa := ||k||^2/(2q_0),
k_2 := -kappa e, chi := Uk + chi_c, chi_2 := Uk_2, eta_t := xi + t chi + t^2 chi_2, h_t := q_0 e + tk + t^2 k_2. Then
Z_t := eta_t - Uh_t = q_0 z + t chi_c (as xi = q_0 z + q_0 Ue), ||h_t||^2 = (q_0 - t^2 kappa)^2 + t^2||k||^2 = q_0^2 + t^4 kappa^2, and
||Z_t||_infinity <= q_0 for small t (Z_{t,j} = q_0 s_j on F; on K chi_c moves inward; finitely many free coordinates move). Since
B_{q**} = B_{l_infinity} + U(B_H), q**(eta_t) <= max(||Z_t||_infinity, ||h_t||) <= q_0 + O(t^4). Moreover a(eta_t) = q_0 + t<U*a,k> +
t a(chi_c) - t^2 kappa <U*a, e> = q_0 - t^2 kappa nu. Hence E_q(t chi + t^2 chi_2) = q**(eta_t) - a(eta_t) <= t^2 nu||k||^2/(2q_0) + O(t^4),
the bound obtained in the note from the Gram system (numerically confirmed: check_testpoint.py, remainder ~ c t^4). Steps 2-4 are
unchanged: the block test uses only the block hypotheses and chi, chi_2 in c_0; weak duality uses b(chi_c) <= 0 (chi_c vanishes on F);
strong duality: -P_*(pi) = q_0 h(b_pi) + [0 if b_pi = 0 on J, z_j(b_pi)_j >= 0 on K; +infinity otherwise], b_pi := g - phi_pi/2 in l_1 —
no constraint on F. Fenchel gives sup J = gamma^+(g), with attainment (b).
(c) In the proof of Proposition prop:onesidedupper, G_b(a + tb) = Exc_{(sb)_-}(t) + nu Psi(tU*b/nu) (lem:bookkeeping(b), Lemma 1.1(c);
off F the summands vanish by side admissibility). If limsup Exc/t^2 = infinity there is nothing to prove; otherwise Exc = O(t^2) and
Proposition prop:rebalancing (valid for every f, with Ghat_b := Exc + (t^2/2)h(b)(1 + Kt)) gives the bound; transfer data exist at every
f (Z5 T1). (d) (a) + (c). (e) 2(p*(f+tg) - 1)/t^2 <= 1 for g in C(f); (a), (b). QED
Remark. The note and Z5 attributed the restriction "F finite" in thm:onesided to the Gram system; the test points above work for every F
(also finite F). What changes at infinite F is the upper bound: optimal data may flip.

Corollary 4.2 (block-tame points with infinite F). T admissible, I finite, f block-tame, F arbitrary, and V_f := sum_m(sum_{k in Q_m}
lambda_{k,m}|u_{k,m}| + |R_m* w_m|) cushion-sparse (m_{V_f}(x) = o(x)). Then every g in C(f) with m_{|g| 1_F}(x) = o(x) is recovered.
Proof. Theorem 4.1(e): optimal data with kappa_w <= 1 and b^+- = g - sum_m R_m*(omega^+-_m - d_m(omega^+-_m)w_m), omega^+-_m in R^{Q_m};
so |b^+- - g| <= C V_f, and (sb^+)_-, (sb^-)_+ <= |g| + C V_f are cushion-sparse (Lemma 1.1(b)). Block-tame implies (SC) for every set
of blocks (remark after def:SC). Theorem 2.1 for every rho < 1. QED
Lemma 4.3 (mates are at most critical under box domination). If Bx <= C_a|a| and g in C(f), then for all r > 0,
Exc_{(sg)_-}(r) <= (1 + 3C_a)r^2/(2q_0) and the same for (sg)_+.
Proof. At scale t: (s_jg_j)_- <= (s_jB_+(j))_- + |(L*Theta_+)_j| <= |a_j|/t + f^+_j + 3Bx(j)/t (lem:suplevel(e)), so with c := 1 + 3C_a,
sum_F((sg)_- - c|a_j|/t)_+ <= t/(4q_0). Put t := cr: Exc(r) = 2r sum((sg)_- - |a_j|/r)_+ <= 2r(cr/(4q_0)). QED
Remarks 4.4. (a) Under box domination V_f <= 2|I| C_a|a| is cushion-dominated, so Corollary 4.2 covers all cushion-sparse mates; critical
mates (Lemma 4.3 allows them) are handled by Theorem 5.1 below (windows), not by fixed optimal data. (b) PROVED: under box domination the flip
coefficient of every side-+ pair is that of g up to a factor 1 + O(t) (|b - g| <= C|a| shifts the flip thresholds by a factor 1 +- Ct);
Theorem 2.2 then recovers g whenever gamma^+(g) + sup_{r <= t_0} Fl_r(g) < 1/rho^2 on both sides for some t_0. Whether g in C(f) implies this is
not known: the decomposition at scale t can reduce its flips by far-carrier absorption (HEURISTIC; capacity <= M Bx(j)/t per coordinate),
which fixed data cannot copy. Theorem 5.1 avoids the question.
