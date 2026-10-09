
## 5. Item (3): F = N and infinitely many swallowed carriers.

Fix an enumeration l(k,m) of all carriers (for SLD-type designs the ladder j); C_L := {(k,m) : l(k,m) <= L} (coarse set);
L(t) := min{L : sum_{l(k,m) > L} lambda_{k,m} <= t^3}; M_f(L) := sum{1/mu_{k,m} : (k,m) in C_L, k in P_m} (coarse peak margins).

### 5.1 Theorem N (box-dominated support). PROVED, every admissible T.
Theorem 5.1. Let T be admissible and I finite. Suppose f in S_{p*} satisfies
 (BD) Bx(j) <= C_a|a_j| for every j (this forces F = N and a_j != 0 for all j: every coordinate lies in supp u_{k,m} for some k,
      because {u_{k,m}}_k is dense in S_{q*});
 (SC_I) the set of all blocks satisfies (SC) (Definition def:SC; it excludes degenerate peaks);
 (W_M) for every n in N, liminf_{T->0} T M_f(L(2^{-n}T)) = 0.
Then f in Rec: (f, g) in cl NA((c_0,p), l_2^2) for every g in C(f). Every carrier is swallowed by the support; no room, pinning, design
feature or condition on the mates or on the strict non-peaks (infinitely many, near-threshold) is used.
Proof. Fix g in C(f), rho in (0,1); eta_0 in (0,2] with rho^2(1+eta_0) <= (1+rho^2)/2; kappa_0 := (sqrt(1+eta_0/2) - 1)/2;
eps_tr := eta_0/2; eta <= eta_* with eta_Gamma(eta) <= 1 and sqrt(1 + eta_Gamma(eta)) <= 1 + kappa_0. "f-constant": depends only on
f, g, rho, N, T.
Step 1 (exact data at one scale). Let t <= min(t_eta, 1), L with sum_{l > L}lambda_l <= t^3, (B_+-, Theta_+-) a two-sided decomposition
at scale t; cQ_m := Q_m cap C_L (finite);
  omega^+-_m := omega_{+-,m} 1_{cQ_m},   b^+-_0 := g - sum_m R_m*(omega^+-_m - d_m(omega^+-_m) w_m).
Both pairs represent g exactly. Estimates (block index dropped):
(a) At a coarse peak k: |alpha(k)||omega_+-(k)| <= t/(2 sigma) (lem:suplevel(c)) and sigma|alpha(k)| = lambda_k mu_k (eq:margin), so
    lambda_k|omega_+-(k)| <= t/(2 mu_k). Outside C_L: lambda_k|omega_+-(k)| <= 4lambda_k/t (|omega_+-| <= (3+eta)/t). Hence
    E_+- := sum_{k notin cQ}lambda_k|omega_+-(k)| <= (t/2)M_f(L) + 4t^2.
(b) |d_+- - d(omega^+-)| <= t/sigma + E_+-/m (lem:suplevel(d); |d(omega)| <= ||D omega||_2 <= sum_k Phi_k|omega(k)|).
(c) b^+-_0 - B_+- = sum_m R_m*(omega_{+-,m}1_{notin cQ_m}) - sum_m (d_{+-,m} - d_m(omega^+-_m))R_m*w_m. Hence ||b^+-_0 - B_+-||_1 <= K_1 t,
    K_1 := C_f(1 + M_f(L)), and, if t^2 M_f(L) <= 1 and t <= t_f, pointwise |(b^+-_0 - B_+-)_j| <= (4/t + 1/t)Bx(j) <= 5C_a|a_j|/t
    (|(R*w)_j| <= Bx(j), |w| <= 1).
(d) X := b^+_0 - b^-_0 = sum_m R_m*((omega^-_m - omega^+_m) - Delta d^0_m w_m), Delta d^0_m := d_m(omega^-_m) - d_m(omega^+_m), satisfies
    |X_j| <= (8/t + 4/t)Bx(j) <= 12C_a|a_j|/t (|omega^+-| <= 4/t, |Delta d^0| <= ||D omega^-|| + ||D omega^+|| <= 4/t as ||Phi_m||_2 <= 1/2).
Step 2 (common shift). A_j := (6C_a + 1)|a_j|/t; x_j := s_j b^+_{0,j}, y_j := s_j b^-_{0,j}. By the cushion lemma and (c),
x_j >= -A_j - f^+_j and y_j <= A_j + f^-_j; by (d), x_j - y_j >= -2A_j. Let sigma_j be the point of [y_j - A_j, x_j + A_j] closest to 0:
|sigma_j| <= f^+_j + f^-_j. Put sigmat := sum_j s_j sigma_j e_j* (||sigmat||_1 <= t/(2q_0)), kappa' := -sigmat(zhat),
  b^+- := b^+-_0 - sigmat - kappa' a,   g_t := g - sigmat - kappa' a.
Both pairs (b^+-, omega^+-) represent g_t; b^+-(xi) = 0 (lem:algebra: b^+-_0(xi) = g(xi) = 0, and kappa' compensates); b^+ - b^- = X;
(s_jb^+_j)_- <= (6C_a + 2)|a_j|/t and (s_jb^-_j)_+ <= (6C_a + 2)|a_j|/t for t^2 <= q_0/(1+||U||); and
p*(g - g_t) <= (1 + ||U||)(||sigmat||_1 + |kappa'|) <= K t with K := (1+||U||)^2/q_0, an f-constant. F = N: no side condition off F.
So (b^+-, omega^+-) are two-piece data for g_t (at arbitrary F), with d-mismatch Delta d^0 of arbitrary sign.
Step 3 (Gamma_w). The pair (b^+, omega^+ - d(omega^+)w) - (B_+, Theta_+) has base part of l_1-norm <= (K_1 + K)t and block part
-omega_+ 1_{notin cQ} + (d_+ - d(omega^+))w, with sigma_m H_m <= sigma_m(E_+/m)^2/C_m (H_m ignores multiples of w_m). Since sqrt(Gamma_w) is a
seminorm and Gamma_w(B_+, Theta_+) <= 1 + eta_Gamma(eta) (lem:budget(d), valid at every F), sqrt(Gamma_w(b^+,omega^+)) <=
sqrt(1 + eta_Gamma(eta)) + K_4 t with K_4 := C'_f(1 + M_f(L)); the same for the - data.
Step 4 (local validity). Base: cushion-proportional one-sided bounds with C_+ := 6C_a + 2, so no flips for |r| <= c_flat t if
c_flat <= 1/(2C_+) (Z5 Step 4 of Theorem 6.1); t||b^+-||_1 <= A_0 := ||g||_1 + 2 (||B_+-||_1 <= ||g||_1 + sum_k lambda_k|Theta_+-(k)| <=
||g||_1 + 1/t, lem:box). Blocks: for k in cQ_m, varsigma_k := sgn w_m(k) (any sign if w_m(k) = 0): varsigma_k omega^+(k) <= (1 - d_+t)gap(k)/t
<= 1.5gap(k)/t (lem:suplevel(f), |d_+t| <= 1/2) and >= -4/t; symmetrically for the - side; so every coordinate is of the inward-only kind of
Z6-L2.1 with A' = 4 (if w_m(k) = 0, the box gives |omega_+(k)| <= 1.5M/t = 1.5gap(k)/t). Z6-L2.1 (Lemma onesidedtransfer with inward-only
coordinates) with Z5's base step gives f-constants c_flat, t_1 (independent of L) such that p*(f + r g_t) <= 1 + (r^2/2)(Gamma_w + eps_tr)
for 0 < r <= c_flat t (+ data) and -c_flat t <= r < 0 (- data). With Step 3, p*(f + rg_t) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t
whenever K_4 t <= kappa_0/2.
Step 5 (averaging over a window of FIXED length). Let n_0 >= 24 rho^2 K/(c_flat(1 - rho^2)) (f-constant). By (W_M) with n = n_0 pick
T_i -> 0 with T_i M_f(L_i) -> 0, L_i := L(2^{-n_0}T_i). For s = 1..n_0 use the scales t_s := T_i 2^{1-s} with the common coarse level L_i
(sum_{l > L_i}lambda_l <= t_s^3). For i large: T_i <= min(t_eta, t_1, t_f, 1), T_i^2 M_f(L_i) <= 1, K_4(L_i)T_i <= kappa_0/2. Lemma
lem:avgfunctionals: rho gbar_i in C(f) and p*(rho gbar_i - rho g) <= 2rho K T_i/n_0 -> 0, gbar_i := (1/n_0)sum_s g_{t_s}.
Step 6 (engineering). The averaged data Dbar_i are two-piece data for gbar_i (representation and d_m are linear; supports in Q_m; F = N),
kappa_w(Dbar_i) <= (1 + 2kappa_0)^2 = 1 + eta_0/2 (convexity), so kappa_w(rho Dbar_i) <= 1. Their side parts satisfy (s bbar^+)_-,
(s bbar^-)_+ <= (6C_a + 2)2^{n_0}|a|/T_i (cushion compatible, hence (CS-side)). By (SC_I) the blocks with Delta dbar_m < 0 satisfy (SC).
Theorem 2.1 applied to the mate rho gbar_i in C(f) gives (f, rho' rho gbar_i) in cl NA for all rho' < 1, hence (f, rho gbar_i) in cl NA.
Let i -> infinity, then rho -> 1. QED
Remarks 5.2. (a) Mechanism: under (BD) every switching, even of box size, is absorbed by the cushions (Step 1(d)), so EXACT two-piece data
exist at every scale without pinning; the block parts two-piece data cannot carry (peak usage, fine carriers) are moved into the base, where
they cost only second order (Step 3, controlled by the margins) and are cushion-proportional by (BD). The closeness constant is an
f-constant, so windows of fixed length suffice. (b) Critical mates (Lemma 4.3) are recovered here: window data built at scale t remove the
scale-t flips by the common shift at closeness cost O(t), and are flip-free below scale c_flat t. (c) For SLD-type designs L(t) <= l for
t in W(l), so (W_M) follows from M_f(l) T_hi(l) -> 0 along a subsequence, e.g. M_f(l) = o(l 2^{l^3} Lambda°(l)). (d) Without (BD), box-size
switching on {|a_j| << Bx(j)} violates the cushions by ~ Bx(j)/t, and fixed data with such violations flip at first order at all smaller
scales; pinning (finitely many unpinned carriers: Theorems R1, 3.5) is then needed. (e) The example "F = N, a > 0" of the task is covered
whenever a box-dominates, the blocks satisfy (SC) and (W_M); it remains open for thin a (not box-dominating on a non-sparse set) and for
blocks violating (SC) (degenerate peaks, non-sparse near-threshold coordinates along every common sequence).

### 5.2 Infinitely many contact-swallowed carriers at infinite F (Z4 Theorem A). SKETCH.
Claim. Z4 Theorem 3.1 (design SLD_G made N-independent) extends to F infinite if (i) every bad carrier is contact swallowed (S_l \ F
infinite), (ii) (BD_B) sum_{l in B}lambda_l|u_l(j)| <= C_a|a_j| on F, (iii) (H2'), (H3), (DR) as in Z4 (repair directions are
cushion-compatible on F by (ii)), (iv) (W_inf) with Xi_f multiplied by C_a^2/mu_f(l)^2, mu_f(l) := min_{l' in B cap [1,l]}
||v_{l'}1_{S_{l'} \ (T(B cap [1,l]) union F)}||_1.
Changes: Steps 1, 2, 4, 5 of Z4 verbatim (rooms and switching budget off F). Step 3: configuration systems with unit weights (design
Hoffman constants), viol'_1 <= c_U/min(gamma_T, 2mu_f). Step 6: B_+1_F replaced by the common shift of Theorem 5.1 Step 2 with
A_j := C_A(l_*)|a_j|/t, C_A(l_*) of order C_a C_diamond(l_*) (|tau'_l| <= 6lambda_l/t + C_diamond t and lambda_l >= t^2 on the active set give
|X_j| <= (6 + C_diamond)Bx_B(j)/t), closeness as in R1 Claim 3.1. Step 7: one-sided expansion with cushion-proportional base, c_flat of
order 1/(C_A(l_*) + A_2). Steps 8-9: windows; Theorem 2.1 with cushion-compatible data. Not written line by line. F = N is not covered
((H2') needs good or contact-swallowed peaks to pin the shift; at F = N the shift is free) — Theorem 5.1 covers it via (SC_I).
The same modifications apply to Z6 Theorem U' (its extra ingredients concern off-F and block data only). SKETCH.

## 6. Item (2): a master theorem at infinite F and (LSC-trunc).

Theorem 6.1 (master theorem; any admissible T, I finite, F arbitrary). Let g in C(f), rho in (0,1), eta_0 with rho^2(1+eta_0) <=
(1+rho^2)/2. Suppose there are c_flat > 0, beta >= 0 in l_1 with m_beta(x) = o(x), C_+ >= 1 and windows (T_j, n_j, K_j), T_j -> 0,
n_j >= 24rho^2K_j/(c_flat(1-rho^2)), K_jT_j/n_j -> 0, such that for each j and each t in {T_j 2^{1-s} : 1 <= s <= n_j} there are two-piece
data (b^+-, omega^+-) (arbitrary F) for a functional g_t with
 (i) p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for 0 < r <= c_flat t (+ data) and -c_flat t <= r < 0 (- data);
 (ii) p*(g - g_t) <= K_j t;  (iii) Gamma_w(b^+-, omega^+-) <= 1 + eta_0/2;
 (iv) (sb^+)_- <= C_+|a|/t + beta and (sb^-)_+ <= C_+|a|/t + beta on F;
 (v) either Delta d_m >= 0 for all these data and all m, or the set of blocks in which some Delta d_m < 0 satisfies (SC).
Then (f, rho g) in cl NA, along norm-attaining approximants with finite base support.
Proof. Lemma lem:avgfunctionals: rho gbar_j in C(f), rho gbar_j -> rho g. The averages of the data are two-piece data for gbar_j with
kappa_w <= 1 + eta_0/2 (convexity); Delta dbar_m is an average, so (v) passes to it; by convexity (iv) holds for the averages with t replaced
by the smallest scale T := T_j 2^{1-n_j}, and Lemma 1.1(b) gives m(x) <= 2m_{C_+|a|/T}(2x) + 2m_beta(2x) = o(x) (the first term vanishes for
x < T/(2C_+)): (CS-side). Theorem 2.1 for rho' rho, rho' < 1. QED
Theorems R1, 3.5, 5.1, Z5 3.3-3.6 and 6.1 are instances (Lemma R2 turns (iv) plus the size conditions into (i)).

Status of (LSC-trunc) [for all f, g in C(f), rho < 1, eps > 0 there is f' with finite base support, p*(f' - f) < eps and
dist(rho g, C(f')) < eps].
(a) PROVED (Z5 Prop 5.4): given Lemma Z at every f with finite F, (LSC-trunc) is equivalent to Lemma Z at every f.
(b) PROVED: (LSC-trunc) holds for every (f, g) satisfying Theorem 6.1, in particular for: f in R_0^inf, R_0^{pm,inf}, (W^c), R_S^inf
(Z5), the class of R1, the class of Theorem 3.5 (super-critical support swallowing), block-tame f with cushion-sparse V_f and mate
(Corollary 4.2), box-dominated f (Theorem 5.1, every mate), window-pinned mates (Z5 3.3), pure base mates (Z5 Lemma 5.1), cl Cert(f).
(c) PROVED (truncation is free): in Theorem 2.1 the support beyond the window N_w becomes contacts of the norm-attaining approximant with
first-order cost rho|tau| sum_{j > N_w}(s_j v_j)_- <= delta s_1|tau|/32, controlled by the tail of the FIXED vector v = b^+ - b^-, and the
near support is raised where the average data need it. Truncation is therefore never the obstruction; per-mate far contact signs (Z5's
suggested next step) are unnecessary, and "two-stage approximation" reduces to the production of exact data (fixed, or window data at f,
or at a companion of cost o(T_lo^2) as in Z3 Theorem E).
(d) OPEN, precise: produce data with (iv) for mates whose window decompositions carry CRITICAL constrained switching through
support-swallowed carriers (Section 3.5), or constrained switching through non-d-neutral or non-resonant-target non-sparse
support-swallowed carriers (Remark 3.6(b),(c)), or box-size switching on thin support (Remark 5.2(d)). The arithmetic of 3.5(i) shows that
un-switching, deep assignment (R1), raised companions (Theorem E) and two-stage approximation all lose a factor of order 1 (critical:
sup/inf of the oscillating local constant) or 4^n (window length); PROVED as statements about these methods, not as non-recovery.

## 7. What remains of (O4) after Y3; leaning; next steps.

Recovered at infinite F (PROVED): (SR)/sign-mixed/cushion room and window-pinned mates (Z5); finitely many bad carriers with each
infinite support-swallowed one cushion-sparse (R1) or super-critical swallowed (Theorem 3.5, design D_sigma); box-dominated support,
i.e. F = N with a >= Bx/C_a, under (SC) and the margin rate (Theorem 5.1, every admissible T); block-tame points for cushion-sparse mates
(Corollary 4.2, every T); pure base mates and cl Cert(f). SKETCH: infinitely many contact-swallowed carriers with box domination on F (5.2).
OPEN (the (O4) part of the consensus core):
 (O4-crit) critical support swallowing: a bad carrier with S_l cap F infinite and 0 < liminf m_l(y)/y <= limsup m_l(y)/y < infinity (model
     |a_j| ~ v_l(j)^2; for geometric signatures the local constant necessarily oscillates by a factor >= 2, Lemma 1.2), or mixed profiles;
 (O4-nd) non-sparse support swallowing through non-d-neutral carriers or carriers with non-resonant targets off F;
 (O4-box) infinitely many bad carriers with thin support (box-size switching where |a_j| << Bx(j) on a non-sparse set), and F = N
     without (SC_I) or (W_M);
 (O4-fin) the finite-F core ((O1)-(O3), (r), (d), (m), (h) of ADDENDUM 5), which reappears verbatim at infinite F.
Corrections to earlier rounds (PROVED): (1) Theorem thm:onesided does not need F finite for its lower bound; the Gram system is avoidable
(Theorem 4.1). (2) Z5 T8 / R1 need cushion sparsity only for the one-sided parts of the data (Theorem 2.1). (3) The Z5-referee example
"F = N, a > 0" of open case (c) is recovered whenever a box-dominates the design and the blocks satisfy (SC) and (W_M) (Theorem 5.1).
Leaning: positive. Every infinite-F mechanism found is either harmless (sparse, super-critical, box-dominated) or a rate phenomenon of the
"exactness versus scale" type already present at finite F; no counterexample mechanism. Density remains OPEN for every admissible T.
Next steps (suggested): (1) critical case: prove the worst-scale principle of 3.5(ii) for log-periodic profiles (select window pieces at
upper points of the flip profile; the averaging lemma only needs scales with ratio >= 2), or find a scale-adaptive engineered approximant
whose base cushions follow the scale (e.g. a nested family of raises at levels 2^{-i}T_0 with masses summing to o(T_0^2)); (2) Remark 3.6(b),(c):
write the bookkeeping for non-resonant targets and handle q_l != 0 by d-repair directions inside F; (3) Theorem 5.1 for thin a: combine
box domination outside a finite set of carriers with bounded switching (needs pinning without room — e.g. via the first-order pin
|Delta B(zhat)| <= t/q_0 and Z6's Farkas pinning).

Numerical sanity checks (evidence only): check_testpoint.py — the test points of Theorem 4.1 have base excess
t^2 nu||k||^2/(2q_0) + c t^4 (five random models, n = 40, |F| = 25, contacts and free coordinates moved by chi_c; (E_q - bound)/t^4 stable
in t = 0.1 ... 0.025); check_Dsharp.py — D^#(t) of Lemma 3.4 in the model: fitted exponents -0.323, -0.008, +0.204, +0.348, +0.504 for
b = 0.5, 1, 1.5, 2, 3 (predicted (b-1)/(b+1): -0.333, 0, 0.2, 0.333, 0.5); at b = 1, D^# oscillates in [6.9, 9.2] without decaying.
