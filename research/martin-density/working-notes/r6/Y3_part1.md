# Y3 part 1 — infinite base support: flip profiles, raised engineering, un-switching, super-critical support swallowing

Notation: paper/martin_density_note.tex ("the note"), r5/Z5_notes.md ("Z5"), r5/Z5_ref_notes.md ("R1" = its Theorem R1 and
Lemmas R0-R3). I finite, p = p_N. f in S_{p*} has forced data (xi, q_0, a, w, F, z, zhat, e, nu); F = supp a may be infinite;
s_j := sgn a_j (j in F). For a two-sided decomposition (B_+-, Theta_+-) of g in C(f) at scale t: Delta B := B_+ - B_-,
f^+_j := (-s_jB_+(j) - |a_j|/t)_+, f^-_j := (s_jB_-(j) - |a_j|/t)_+ (j in F), and sum_F (f^+_j + f^-_j) <= t/(2q_0)
(note lem:flip). Cushion lemma (Z5 Lemma 1.1): (s_j B_+(j))_- <= |a_j|/t + f^+_j, (s_j B_-(j))_+ <= |a_j|/t + f^-_j.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Flip profiles. PROVED (elementary).

For beta in l_1, beta >= 0, put m_beta(x) := sum{beta_j : j in F, |a_j| < x beta_j} (x > 0) and
Exc_beta(r) := sum_{j in F} 2 (r beta_j - |a_j|)_+ (r >= 0).

Lemma 1.1. (a) Exc_beta(r) = 2 int_0^r m_beta(s) ds; r -> Exc_beta(r) is convex, nondecreasing, Exc_beta(0) = 0.
(b) beta -> Exc_beta(r) is convex and nondecreasing (coordinatewise) for each r; beta -> m_beta(x) is NOT convex in general,
but m_beta(x) <= m_{beta'}(x) whenever beta <= beta'.
(c) For b in l_1 and r > 0: sum_{j in F}(|a_j + r b_j| - |a_j| - s_j r b_j) = Exc_{(s b)_-}(r), and the same with r < 0 and
(s b)_+ (|r| in place of r). [Z5 Lemma 4.2.]
(d) (scale behaviour) If m_beta(x) <= kappa x for 0 < x <= x_0 then Exc_beta(r) <= kappa r^2 for r <= x_0; if m_beta(x) >= kappa x
for 0 < x <= x_0 then Exc_beta(r) >= kappa r^2 for r <= x_0.
Proof. (a) For each j the function r -> 2(r beta_j - |a_j|)_+ has derivative 2 beta_j 1[r beta_j > |a_j|] (a.e.); sum (monotone
convergence) and integrate. Convexity: m_beta is nondecreasing in s. (b) Each summand is convex and nondecreasing in beta_j.
(c) |x + y| - |x| - sgn(x) y = 2(-sgn(x) y - |x|)_+ (x != 0), with x = a_j, y = r b_j, and -s_j r b_j <= r (s_j b_j)_-, with
equality where s_j b_j < 0; where s_j b_j >= 0 the summand is 0. (d) Integrate (a). QED

Classification (for a fixed beta, or a fixed carrier profile below). With kappa_beta(x) := m_beta(x)/x:
 * SPARSE: kappa_beta(x) -> 0 (this is Z5's (CS)); then Exc_beta(r) = o(r^2).
 * SUPER-CRITICAL: kappa_beta(x) -> infinity; then Exc_beta(r)/r^2 -> infinity.
 * CRITICAL: 0 < liminf kappa_beta <= limsup kappa_beta < infinity.
 * mixed (liminf 0 < limsup, or liminf < infinity = limsup).
Model (Z5 7.1): beta = v_l 1_{S_l}, v_l(s) = c_0 2^{-s}, |a_s| = 2^{-(1+b)s} on S_l (bounded gaps): kappa(x) ~ x^{1/b - 1}: sparse iff
b < 1, super-critical iff b > 1, critical iff b = 1. For b = 1, kappa(x) is LOG-PERIODIC (not convergent): m is a step function
with jumps of relative size about 1/2 at x = rho_l(s) := |a_s|/v_l(s); sup kappa/inf kappa >= 2 (more on this in part 2).

## 1.2 Raised engineered approximants: (CS) is needed only for the side parts. PROVED.

Theorem 1.2 (improvement of Z5 Theorem 4.3 = T8). Let T be admissible, I finite, f in S_{p*} with F arbitrary, g in C(f) carrying
two-piece data (b^+-, omega^+-) (Definition def:twopiece read at arbitrary F: b^+- vanish on J, z-signed / anti-z-signed on K,
NO condition on F; omega^+-_m in c_00(Q_m)), rho in (0,1) with rho^2 kappa_w < 1, and I_- := {m : Delta d_m < 0} satisfying (SC).
Assume the ONE-SIDED cushion sparsity
  (CS-side)  m_{(s b^+)_-}(x) = o(x)  and  m_{(s b^-)_+}(x) = o(x)  as x -> 0.
(No condition on b^theta = (b^+ + b^-)/2.) Then there are norm-attaining f'_i -> f with finite base supports and g'_i in C(f'_i),
g'_i -> rho g. In particular (f, rho g) in cl NA, and (f, g) in cl NA if kappa_w <= 1.

Proof. Z5's proof of Theorem 4.3 (which modifies Definition def:engineered and the proof of Theorem thm:engineered) with ONE change
in the definition of a'': for j in F cap [1, N_w] put r_j := (8 rho s_1 |b^theta_j| - |a_j|)_+ and
  a'' := a 1_{[1,N_w]} + sum_{j in K cap [1,N_w]} m_j z_j e_j* + sum_{j in F cap [1,N_w]} r_j s_j e_j*,  m_j := 4 rho s_1|b^theta_j|,
i.e. every support coordinate in the window is RAISED to modulus max(|a_j|, 8 rho s_1 |b^theta_j|) (same sign). Everything else
(a' := a''/q*(a''), z', xhat', x', f', N'', the order of choices T_1 -> K_sharp -> eta_1 -> transfer data -> T_0 -> (s_{1,i}) ->
(N_{w,i}) -> (N''_i)) is unchanged.
(1) Lemma lem:approxfacts. supp a' = (F cap [1,N_w]) union {window contacts with b^theta_j != 0}; z' = sgn a' there (the raises keep
the sign s_j = z_j); so f' is norm attaining (Prop prop:smooth(c)). ||a'' - a||_1 <= alpha(N_w) + 4 rho s_1||b^theta 1_K||_1 +
sum_F r_j <= alpha(N_w) + 8 rho s_1 ||b^theta||_1, i.e. (E1) holds with 8 in place of 4 (K_e doubled); (E2)-(E5), Lemma lem:F1,
Lemma lem:anchor, Lemma lem:scrambling and Steps 1, 2, 4, 6 use a'' only through (E1) and the forced data of f', hence are
unchanged. At late stages q*(a'') <= 2, so |a'_j| >= |a''_j|/2 >= |a_j|/2 on F cap [1,N_w].
(2) Step 3 (base), coordinates j in F cap [1,N_w]. As in the note, a'_j + tau B^diamond_j = (1 - tau rho c) a'_j + tau rho
beta^diamond_j with |tau rho c| <= 1/2, so s_j(1 - tau rho c)a'_j >= |a''_j|/4.
  diamond = theta (0 < |tau| <= s_1): |tau rho beta^theta_j| <= rho s_1|b^theta_j| <= |a''_j|/8 < |a''_j|/4: NO flip (if r_j > 0,
  |a''_j| = 8 rho s_1|b^theta_j|; otherwise |a''_j| = |a_j| >= 8 rho s_1|b^theta_j|).
  diamond = +- (s_1 < |tau| <= T_0, sgn tau = diamond): the anti-sign part of tau rho beta^diamond_j is <= |tau| rho beta_j with
  beta = (s b^+)_- for diamond = +, (s b^-)_+ for diamond = -, and |a''_j| >= |a_j|; exactly as in Z5 (i): a flip needs
  |a_j| < 4 rho|tau| beta_j and costs <= 2|tau| rho beta_j, so the flip cost is <= Fl(tau) := 2 rho|tau| m(4 rho|tau|),
  m := m_{(sb^+)_-} + m_{(sb^-)_+}.
All other coordinates are treated verbatim (window contacts, K, (N_w, N''], beyond N''). Step 0 condition "2 rho|tau| m(4rho|tau|)
<= delta tau^2/16 for |tau| <= T_0" is now imposed with this m (side parts only); it can be met because m(x) = o(x).
(3) Step 5: Fl enters only for |tau| > s_1 and is <= delta tau^2/16; the bound p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for
|tau| <= T_0 follows as in Z5; Step 6 and Lemma lem:assembly conclude. QED

Remark 1.3. (a) The raises play for support coordinates exactly the role that the window masses m_j play for contacts: they
absorb the TWO-SIDED use of the average data at scales <= s_1; their total mass is O(s_1) whatever the sparsity of b^theta.
(b) Consequently, in Theorem R1 (Z5 referee) the requirement on |bbar^theta| in Step 5 is superfluous; only the one-sided parts
need (CS). This matters below: free switching through a non-sparse carrier makes |b^theta| non-sparse (Remark 1.9).

## 1.3 Un-switching (exact rewriting). PROVED (any admissible T, any F).

Lemma 1.4 (un-switching pair). Let l = (k, m) be a carrier with w_m(k) = 0 (d-neutral; then k in Q_m) and c in R. The pair
  P_l(c) := (b, omega) = (c u_l, -(c/lambda_l) e_k in block m)
represents the zero functional: b + R_m*(omega - d_m(omega) w_m) = 0, with d_m(omega) = 0, b(xi) = 0, and
  Gamma_w(P_l(c)) = c^2 [ q_0 h(u_l) + sigma_m H_m(e_k/lambda_l) ] <= c^2 C_un(l)^2,  C_un(l)^2 := q_0||U||^2/nu + sigma_m/(m^2 C_m).
Proof. R_m* e_k = lambda_l u_l, and d_m(e_k) = Phi_m(k)^2 w_m(k)/C_m = 0. u_l(xi) = q_0 u_l(zhat) and, k being a strict non-peak,
(R_m** xi)(k) = lambda_l q_0 u_l(zhat) = sigma_m Phi_m(k)^2 w_m(k)/C_m = 0 (Lemma lem:threshold). h(u) = ||P^perp U*u||^2/nu <=
||U||^2/nu (||u_l||_1 <= 1); H_m(e_k/lambda) = ||P_m^perp D_m e_k||^2/(lambda^2 C_m) <= Phi_m(k)^2/(lambda^2 C_m) = 1/(m^2 C_m). QED

Corollary 1.5 (moving a switching into one side). If (b^+, omega^+) and (b^-, omega^-) represent the same functional and l is a
d-neutral carrier, then for every c the pair (b^- , omega^-) + P_l(c) represents the same functional, and
sqrt(Gamma_w((b^-,omega^-) + P_l(c))) <= sqrt(Gamma_w(b^-, omega^-)) + |c| C_un(l) (sqrt(Gamma_w) is a seminorm on data).
In words: a d-neutral switching amplitude c through l may be transferred from the block part of one representation to its base
part at a second-order cost linear in |c|; the represented functional (hence the closeness to g) does not change.

## 1.4 The constrained-switching bound (design D_sigma). PROVED.

Definition 1.6 (design D_sigma). The SLD operator of Definition def:SLD (or its variants SLD_G, D''', the explosive design; the
modification is compatible with all of them) with two changes: (D0') each S_l has bounded gaps (e.g. S_l := {2^l(2i+1): i >= 1}
minus {j_0}); (D1)(c) [new allowedness clause] a target y allowed at l meets S_{l'} (l' < l) only at coordinates s <= l.
Proposition 1.7. D_sigma is admissible and satisfies (P1)-(P3); every result of Section 8, of Z3-Z6 and of R1 that holds for the
underlying design holds for D_sigma; the design does not depend on N.
Proof. (D1)(c) only removes targets from the allowed set at each l; a finitely supported target y^{(i)} satisfies (c) as soon as
l >= max supp y^{(i)}, and (a), (b) at all large l (proof of Theorem thm:SLD), so (T-d) holds; (T-a), (T-b), (T-c) and (P1)-(P3)
use only (a), (b) and c_{l+1} <= c_l/4, unchanged. All cited results use only (T-a)-(T-d), (P1)-(P3) and allowedness (a), (b)
(the note states this after Theorem thm:SLD; Z4 Prop 2.4, Z6 D''' and Z3-ref's explosive design are recursions of the same form,
in which (c) is one more finite condition at each step). Nothing depends on N. QED

Setting for 1.8. f in S_{p*} (F arbitrary), l_0 a carrier of block m_0 with S_{l_0} subset F up to finitely many points, and a
sign eps with s_j = eps for all j in S_{l_0} cap F, j >= s_* (monochromatic support swallowing). Put v := v_{l_0},
rho(s) := |a_s|/v(s) (s in S_{l_0} cap F), tau := -eps Delta theta_{l_0} (tau >= 0: free direction; tau < 0: constrained), and
  m(y) := sum{ v(s) : s in S_{l_0} cap F, s >= s_*, rho(s) < y }.
Quasi-monotonicity (QM): there is C_Q >= 1 with rho(s') <= C_Q rho(s) for s_* <= s < s' in S_{l_0} cap F.

Lemma 1.8 (constrained-switching bound). Design D_sigma. Let l_* >= max(l_0, s_*, max(S_{l_0} minus F)), t in W(l_*),
t <= min(t_eta, 1), and (B_+-, Theta_+-) a two-sided decomposition of g in C(f) at scale t; put D := (tau)_-. Then
 (a) D * m^{>l_*}(tD/4) <= t/q_0 + 32 t^2, where m^{>l_*}(y) := sum{v(s) : s in S_{l_0} cap F, s > l_*, rho(s) < y};
 (b) under (QM): D <= max( D^#(t), K_sigma(l_*) t ), where
     D^#(t) := sup{ D > 0 : D m(tD/(4C_Q)) <= t/q_0 + 32t^2 } and K_sigma(l_*) := (1/q_0 + 32)/M(l_*),
     M(l_*) := sum{ v(s) : s in S_{l_0}, s > l_* } >= v(l_* + G_0) (G_0 := max gap of S_{l_0});
 (c) if m(y)/y -> infinity as y -> 0 ("super-critical"), then D^#(t) -> 0 as t -> 0. Hence along any windows,
     sup_{t in W(l_*)} D <= sup_{t <= T_hi(l_*)} D^#(t) + K_sigma(l_*) T_hi(l_*) -> 0 as l_* -> infinity
     (K_sigma(l) T_hi(l) <= C_f 2^{l} 2^{-l^3} -> 0 by (P3)).
Proof. (a) Let s in S_{l_0}, s > l_*. By (P1) and (eq:DeltaB), -Delta B(s) = Delta theta_{l_0} v(s) + sum_{l' > l_0} Delta theta_{l'}
y_{l'}(s)/n_{l'} (coarser targets vanish on S_{l_0} by allowedness (a), other signatures vanish there). For l_0 < l' <= l_*,
allowedness (c) at l' gives supp y_{l'} cap S_{l_0} subset [1, l'] subset [1, l_*], so only l' > l_* contribute:
r(s) := sum_{l' > l_*} Delta theta_{l'} y_{l'}(s)/n_{l'}, and sum_s |r(s)| <= (4/3) sum_{l'>l_*}|Delta theta_{l'}| <= 8t^2
(Lemma lem:box and (P2): sum_{l'>l_*}|Delta theta_{l'}| <= 6t^2 for t >= T_lo(l_*)). For s in F with s_s = eps:
s_s Delta B(s) = -eps Delta theta_{l_0} v(s) - eps r(s) = tau v(s) - eps r(s), so (s_s Delta B(s))_- >= D v(s) - |r(s)|. By the
cushion lemma, (s_s Delta B(s))_- <= (s_s B_+(s))_- + (s_s B_-(s))_+ <= 2|a_s|/t + f^+_s + f^-_s. If rho(s) < tD/4, then
2|a_s|/t = 2 rho(s) v(s)/t < D v(s)/2, hence D v(s)/2 <= f^+_s + f^-_s + |r(s)|. Summing over these s:
(D/2) m^{>l_*}(tD/4) <= t/(2q_0) + 8t^2.
(b) Case A: no s in S_{l_0} cap F with s_* <= s <= l_* has rho(s) < tD/(4C_Q). Then every s >= s_* with rho(s) < tD/(4C_Q) is > l_*,
so m(tD/(4C_Q)) <= m^{>l_*}(tD/(4C_Q)) <= m^{>l_*}(tD/4); by (a), D m(tD/(4C_Q)) <= t/q_0 + 32t^2, i.e. D <= D^#(t) (the map
D -> D m(tD/(4C_Q)) is nondecreasing). Case B: some s_1 in [s_*, l_*] has rho(s_1) < tD/(4C_Q). By (QM) every s > l_* in S_{l_0} cap F
has rho(s) <= C_Q rho(s_1) < tD/4, so m^{>l_*}(tD/4) = sum{v(s): s in S_{l_0} cap F, s > l_*} = M(l_*) (S_{l_0} cap (l_*,infinity)
subset F because l_* >= max(S_{l_0} minus F)); by (a), D <= (t/q_0 + 32t^2)/M(l_*) <= K_sigma(l_*) t.
(c) If D^#(t_n) >= eta_1 > 0 along t_n -> 0, then (monotonicity) eta_1 m(t_n eta_1/(4C_Q)) <= t_n/q_0 + 32 t_n^2, i.e.
m(y_n)/y_n <= 4C_Q(1/q_0 + 32)/eta_1^2 along y_n := t_n eta_1/(4C_Q) -> 0, contradicting super-criticality. D^#(t) < infinity because
m(y) > 0 for y > 0 (rho(s) -> 0 along S_{l_0} would be needed for m(y) > 0 for all y; if m vanishes near 0 then D^#(t) := 0 is not
needed: m(y) = 0 for small y contradicts super-criticality). M(l_*) >= v(s^+) with s^+ := min(S_{l_0} cap (l_*, infinity)) <= l_* + G_0,
and v(s) = delta_{l_0}2^{-s}/n_{l_0}; T_hi(l) <= 2^{-l^3}/l by (P3). QED

Remark (where the design enters). Without (D1)(c), targets of COARSE good carriers may meet the deep part of S_{l_0}; their switching
is only pinned in total (<= K_* t), and K_* t can absorb all constrained usage of the deep coordinates: then the budget gives
D m(tD/4) <~ K_* t, useless at design windows (K_* t << 1 but K_* t^{1 - 1/b} >> 1 in the model). (D1)(c) confines coarse targets to
the shallow coordinates s <= l_*, where the dichotomy (QM) applies. HEURISTIC remark; the lemma itself is PROVED.

## 1.5 Theorem SC: super-critical support swallowing is harmless. PROVED.

Definitions (R1/Z5 Section 6 at arbitrary F): r_l := min_{sigma = +-1} sum_{s in S_l \ F} v_l(s)(1 + sigma z_s); B := {l : r_l = 0};
good l: S*_l, r*_l, Lambda*_f as in R1; (W*), (H2), (H3-inf), (B_fin) as in R1; U_E(j) := sum_{l in E}|u_l(j)| for E subset B,
m_E(y) := sum{U_E(j) : j in F, |a_j| < y U_E(j)}.
A bad carrier l is SUPER-CRITICAL SWALLOWED (l in B_sc) if:
 (i) supp u_l subset F (signature AND target inside the support);
 (ii) w_{m(l)}(k(l)) = 0 (d-neutral);
 (iii) a is monochromatic on S_l from some s_* on (sign eps_l) and (QM) holds for l;
 (iv) m_l(y)/y -> infinity as y -> 0, m_l as in 1.4.
Theorem 1.9 (SC). Design D_sigma, every N. Let f in S_{p*} (F arbitrary) satisfy (W*), (H2), (H3-inf), (B_fin), and
  (CS_{B \ B_sc})  m_{B \ B_sc}(y) = o(y).
Then f in Rec. [Every bad carrier is either cushion-sparse or super-critical swallowed; the latter may be non-sparse.]

Proof. We follow the proof of Theorem R1 (Z5_ref_notes Section 2) and indicate the changes. Fix g in C(f), rho, eta_0, kappa_0,
eps_tr, eta as there; l_* >= l_f, t in W(l_*), t <= min(t_eta,1), (B_+-, Theta_+-), K* := (1/q_0 + 22)Lambda*_f(l_*).
Step 1 (good pinning) and Lemma lem:badpeaks: verbatim.
Step 2 (exact switching): verbatim; tau' in R^B with ||tau - tau'||_1 <= C_f K* t, tau' in the cone Z_f. For l in B_sc no row of Z_f
involves tau_l (no target row: supp u_l subset F, so l contributes to no L_j with j notin F; no peak row: k(l) in Q; no d-row:
q_l = 0), so we may and do take tau'_l := tau_l for l in B_sc.
Step 2' (bounded switching): verbatim, |tau'_l| <= C_tau.
Step 3 (data) with X replaced by
  Xt := sum_{l in B \ B_sc} eps_l tau'_l u_l + sum_{l in B_sc} eps_l (tau'_l)_+ u_l,   tau~_l := tau'_l (l notin B_sc), (tau'_l)_+ (l in B_sc).
Since supp u_l subset F for l in B_sc, Xt 1_{F^c} = X 1_{F^c} = V'; chi, e_+- from Lemma lem:split are as in R1. Define A_j := 2|a_j|/t,
D_t := {j in F : s_j Xt_j < -2A_j}, b^+_1 by the common shift off D_t and b^+_1(j) := -s_j A_j on D_t (R1 Step 3 with Xt).
Claim A (= R1 Claim 3.1 with Xt; the error term is the ORIGINAL one): for t <= t_sc (an f-constant) and every j in F,
  |B_+(j) - b^+_1(j)| <= f^+_j + f^-_j + |(Delta B - X)_j|,   s_j b^+_1(j) >= -A_j,   s_j(b^+_1 - Xt)(j) <= A_j off D_t.
Proof. Put x_j := s_j B_+(j), y_j := s_j(B_+(j) - Xt_j) = s_j B_-(j) + e_j + d_j with e_j := s_j(Delta B - X)_j and
d_j := s_j(X - Xt)_j = -sum_{l in B_sc}(tau'_l)_- s_j eps_l u_l(j). On S_l cap F (l in B_sc, j >= s_*) s_j eps_l u_l(j) = v_l(j) >= 0, so
d_j <= 0 there; the remaining j with d_j != 0 lie in the finite set T_sc := union_{l in B_sc} (supp y_l union (S_l cap [1,s_*])), where
|d_j| <= C_tau sum_{B_sc}|u_l(j)|; with a_T := min_{T_sc}|a_j| > 0 and t_sc := a_T/(C_tau |B|), (d_j)_+ <= |a_j|/t on T_sc.
Off D_t (x_j - y_j = s_j Xt_j >= -2A_j) the common shift sigma_j (point of [y_j - A_j, x_j + A_j] closest to 0) has
|sigma_j| = (-x_j - A_j)_+ + (y_j - A_j)_+ <= f^+_j + (f^-_j + |e_j| + (d_j)_+ - |a_j|/t)_+ <= f^+_j + f^-_j + |e_j|
(using x_j >= -|a_j|/t - f^+_j, s_j B_-(j) <= |a_j|/t + f^-_j). On D_t, |x_j + A_j| <= f^+_j + f^-_j + |e_j| as in R1 (the upper
bound x_j + A_j < y_j - A_j <= f^-_j + |e_j| + (d_j)_+ - |a_j|/t <= f^-_j + |e_j|). The other two statements are R1 (ii), (iii). QED
Consequently ||B_+ 1_F - b^+_1||_1 <= t/(2q_0) + (C_f + 1)K* t (as in R1).
Claim B (location of deep coordinates). For t <= t_sc' (an f-constant), D_t subset {j : C_tau U_{B \ B_sc}(j) > 2A_j} and
|Xt_j| <= C_tau U_{B \ B_sc}(j) on D_t.
Proof. On S_l cap F (l in B_sc), outside T_sc and outside the finite set T'_l of target coordinates of the other bad carriers,
s_j Xt_j = (tau'_l)_+ v_l(j) >= 0 (only l's signature is nonzero there among bad vectors: other signatures vanish, coarser targets vanish
by (a), finer bad targets are finitely supported), so j notin D_t. On the finite shallow set T_sc union T' (|a_j| >= a'_T > 0),
|Xt_j| <= C_tau|B| <= 2A_j once t <= 2a'_T/(C_tau|B|). Elsewhere sum_{B_sc}|u_l(j)| = 0, so |Xt_j| <= C_tau U_{B \ B_sc}(j). QED
Data: kappa := (b^+_1 + chi V')(zhat), b^+ := b^+_1 + chi V' - kappa a, b^- := b^+ - Xt; omega^+ as in R1; omega^- := omega^+ +
sum_{l in B_np}(eps_l tau~_l/lambda_l) e_{k(l)}; g_t := b^+ + sum_m R_m*(omega^+_m - d_m(omega^+_m) w_m).
(a) Two-piece data: off F, b^+ = chi V' and b^- = -(1-chi)V'; b^+ - b^- = Xt = sum_m R_m*(omega^-_m - omega^+_m) and
d_m(omega^-_m) - d_m(omega^+_m) = sum_{m(l)=m} q_l tau~_l = sum_{m(l)=m} q_l tau'_l = 0 (q_l = 0 on B_sc; tau'_l = 0 at bad peaks;
d-rows of Z_f). b^+-(xi) = 0 as in R1.
(b) Cushion bounds on F: (s_j b^+_j)_- <= 3|a_j|/t; (s_j b^-_j)_+ <= 3|a_j|/t off D_t and <= |Xt_j| <= C_tau U_{B\B_sc}(j) on D_t
(Claims A, B and |kappa||a_j| <= |a_j|/t). Also |b^+-_j| <= 3|a_j|/t + 2C_tau U_B(j), so t||b^+-||_1 <= A^R_0 (R1 Claim 3.2(c)).
(c) Closeness and Gamma_w of the + data: as in R1 (b^+ is O(K* t)-close to B_+ by Claim A; block parts as in R1).
(d) Gamma_w of the - data. Write (b^-, omega^-) = [(b^-, omega^-) + sum_{l in B_sc} P_l(c_l)] - sum_{l in B_sc} P_l(c_l) with
c_l := eps_l (tau'_l)_-. The bracket is the pair R1 would build from X (b^- + sum c_l u_l = b^+ - Xt + (Xt - X) + ... indeed
b^+ - Xt - sum_{B_sc} eps_l(tau'_l)_- u_l = b^+ - X, and omega^- - sum (c_l/lambda_l) e_{k(l)} = omega^+ + sum_{B_np}(eps_l tau'_l/lambda_l)e),
whose Gamma_w is bounded exactly as in R1 Claim 3.2(d) (comparison with (B_-, Theta_-)) — note that R1's comparison of the - data with
(B_-, Theta_-) uses only Delta B - X = O(K*t) and the box bounds, not cushion bounds. By Corollary 1.5,
  sqrt(Gamma_w(b^-, omega^-)) <= sqrt(1 + eta_Gamma(eta)) + K^R_4 t + C_un sum_{l in B_sc}(tau_l)_-,   C_un := max_{B_sc} C_un(l).
By Lemma 1.8 (tau'_l = tau_l), for windows l_j -> infinity, sup_{t in W(l_j)} sum_{B_sc}(tau_l)_- -> 0.
(e) Block size conditions for Lemma R2: as in R1 (A_2 := 4 + C_tau/lambda_B).
Step 4 (one-sided expansion): Lemma R2 with U_* := U_{B \ B_sc}, C_* := 2C_tau: its hypothesis is exactly (b) for the + data
((s b^+)_- <= 3|a|/t) and the - data ((s b^-)_+ <= 3|a|/t + C_tau U_*), and m_*(y) = o(y) is (CS_{B \ B_sc}).
Step 5 (windows, averaging, engineering): choose windows l_j by (W*) as in R1 and, in addition, j so large that
C_un sup_{W(l_j)} sum_{B_sc}(tau_l)_- <= kappa_0/2 and the smallness conditions t <= t_sc, t_sc' hold on W(l_j); then every piece has
Gamma_w <= (1 + 2kappa_0)^2 = 1 + eta_0/2 on both sides (with K^R_4 t <= kappa_0/2). Lemma lem:avgfunctionals gives rho gbar_j in C(f),
rho gbar_j -> rho g. The averaged data are d-neutral two-piece data with kappa_w(rho Dbar_j) <= 1; their side parts satisfy, by (b) and
convexity of x -> x_+-, (s bbar^+)_- <= 3|a|/T_lo(l_j) and (s bbar^-)_+ <= 3|a|/T_lo(l_j) + C_tau U_{B\B_sc}; as in R1 Step 5 this gives
(CS-side) (m_beta(x) <= 2C_tau m_{B\B_sc}(2C_tau x) = o(x) for x <= T_lo/6). Theorem 1.2 (raised engineered approximants; no
condition on |bbar^theta|, which is NOT sparse in general here, see Remark 1.10) with I_- empty gives (f, rho gbar_j) in cl NA.
Let j -> infinity, then rho -> 1. QED

Remark 1.10. (a) Why Theorem 1.2 is needed: on S_l cap F (l in B_sc), s_j b^+_1(j) lies in [-A_j, A_j + (tau'_l)_+ v_l(j)] and
s_j b^-_j in [-A_j - (tau'_l)_+ v_l(j), A_j]; so |b^theta_j| can be of size (tau'_l)_+ v_l(j)/2 on the deep part of S_l, which is
non-sparse. The free switching (tau_l)_+ need not vanish: if the signature profile gamma_j := eps_l g_j/v_l(j) of the mate oscillates on
the deep part of S_l, every decomposition at every small scale must have (tau_l)_+ >= limsup gamma - liminf gamma (deep coordinates
force theta^+ <= gamma_j + o(1) <= theta^- ... ), PROVED by the cushion lemma; this is harmless now.
(b) Scope. Model (Z5 7.1): v_l(s) = c_0 2^{-s}, |a_s| = 2^{-(1+b)s} on S_l: (QM) holds, and (iv) holds iff b > 1. Together with
Theorem R1 (b < 1) this settles the model for b != 1, for d-neutral carriers with supp u_l subset F. The critical case b = 1 is
discussed in part 2 (OPEN).
(c) Hypothesis (i) cannot simply be dropped: if u_l has a target coordinate j notin F, un-switching moves eps_l (tau'_l)_- y_l(j)/n_l into
the - base at j, which is side-admissible only if z_j eps_l y_l(j) <= 0 with |z_j| = 1; but if z_j eps_l y_l(j) > 0 or |z_j| < 1 the
constrained direction is PINNED at O(t) by that coordinate (switching budget), and then no un-switching is needed: the projection of
Step 2 handles it (put the row "tau_l >= 0" into Z_f; violation O(t/||y_l 1_{target}||)). So (i) can be relaxed to: every target
coordinate j notin F of l is a contact with z_j eps_l y_l(j) < 0 (un-switching admissible), or l's constrained direction is pinned by a
resonant/free target coordinate. PROVED by the same argument (we do not write the bookkeeping out).
(d) Hypothesis (ii): un-switching a non-d-neutral carrier creates Delta d_m = q_l (tau'_l)_- != 0, whose representation requires
-Delta d_m R_m* w_m inside b^+ - b^-; off F this is not side-admissible. At F = N (no off-F coordinates) and q_l > 0 it would be harmless
(Delta d >= 0 is allowed by Corollary cor:D1), but cushion compatibility of R_m* w_m must then be checked (part 3). OPEN in general.
