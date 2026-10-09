# Y3 notes (Round 6): the infinite-support part (O4) of the open core

References: paper/martin_density_note.tex ("the note"); r5/Z5_notes.md ("Z5"; T8 = its Theorem 4.3, Lemma 1.1 = cushion lemma);
r5/Z5_ref_notes.md ("R1" = its Theorem R1, Lemma R2 = one-sided expansion with sparse flips); r5/Z3_notes.md (Theorem E, Lemma 3.1);
r5/Z4_notes.md (Theorem A = 3.1); r5/Z6_ref_notes.md ("Z6-L2.1" = one-sided expansion with inward-only coordinates).
Part files: r6/Y3_part1.md, Y3_part2.md, Y3_part3.md (first versions; THIS file supersedes them where they differ).
Scripts: r6/Y3_work/check_testpoint.py, check_Dsharp.py. Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Setting: I finite (p = p_N; Lemma lem:martintail transfers to Martin's p for one N-independent T); f in S_{p*} with forced data
(xi, q_0, a, w, F, z, zhat, e, nu); F = supp a possibly infinite; s_j := sgn a_j on F. For a two-sided decomposition (B_+-, Theta_+-)
of g in C(f) at scale t: f^+_j := (-s_jB_+(j) - |a_j|/t)_+, f^-_j := (s_jB_-(j) - |a_j|/t)_+, sum_F(f^+_j + f^-_j) <= t/(2q_0)
(lem:flip); cushion lemma (s_jB_+(j))_- <= |a_j|/t + f^+_j, (s_jB_-(j))_+ <= |a_j|/t + f^-_j. d_+-, omega_+- as in lem:suplevel
(Theta_+ = omega_+ - d_+w, Theta_- = omega_- - d_-w). Bx(j) := sum_{m in I}sum_k lambda_{k,m}|u_{k,m}(j)| (box profile).

## 0. Summary

| # | Result | Scope | Status |
|---|---|---|---|
| 1 | Flip profiles: Exc_beta(r) = 2 int_0^r m_beta; classification sparse / critical / super-critical; geometric signatures make critical profiles oscillate (factor >= 2) | any T | PROVED (1.1, 1.2) |
| 2 | Raised engineered approximants: T8 needs cushion sparsity only for the side parts (s b^+)_-, (s b^-)_+, not for b^theta; flip-extended version | any T | PROVED (2.1, 2.2) |
| 3 | Un-switching pair (exact rewriting of a d-neutral switching into one side, Gamma cost linear) | any T | PROVED (3.1) |
| 4 | Constrained-switching bound for monochromatic support swallowing (design D_sigma: new allowedness (c)); quasi-monotone dichotomy | D_sigma | PROVED (3.2-3.4) |
| 5 | Theorem SC: non-sparse SUPER-CRITICAL support swallowing (model |a_j| ~ v_l(j)^{1+b}, b > 1) is harmless (with R1: model settled for b != 1) | D_sigma | PROVED (3.5) |
| 6 | Exact one-sided coefficient at ARBITRARY F (new test points k_2 = -kappa e; no Gram system); liminf >= gamma^+-, attainment, upper bound with flips | any T | PROVED (4.1) |
| 7 | Block-tame points with infinite F: mates that are cushion-sparse are recovered | any T | PROVED (4.2) |
| 8 | Theorem N: box-dominated support (forces F = N, a > 0): EVERY mate recovered under (SC) for all blocks and a margin rate; no pinning, no design needed | any T | PROVED (5.1) |
| 9 | Theorem A at infinite F (contact-swallowed bad carriers, box domination on F) | SLD_G | SKETCH (5.2) |
| 10 | Master theorem at infinite F; (LSC-trunc) holds wherever exact data exist; truncation itself is free | any T | PROVED (6.1; Section 6 status (b), (c)) |
| 11 | Remaining (O4): CRITICAL support swallowing (m_l(y) asymp y), non-d-neutral/non-resonant non-sparse carriers, box-size switching on thin support, F = N without (SC); plus the finite-F core | — | OPEN (7) |

Bottom line: the infinite-support part of the open core shrinks to a single quantitative phenomenon — critical support swallowing,
an "exactness versus scale" rate problem of the same type as (O1)(i) — plus d-neutrality/resonance side conditions and the block-side
conditions shared with finite F. F = N with a box-dominating base (the explicit example of the task) is recovered for every admissible T
under block conditions alone. No counterexample mechanism was found; leaning positive.

## 1. Flip profiles. PROVED.

For beta in l_1, beta >= 0: m_beta(x) := sum{beta_j : j in F, |a_j| < x beta_j}, Exc_beta(r) := sum_{j in F} 2(r beta_j - |a_j|)_+.
Lemma 1.1. (a) Exc_beta(r) = 2 int_0^r m_beta(s) ds; it is convex and nondecreasing in r, Exc_beta(0) = 0.
(b) beta -> Exc_beta(r) is convex and coordinatewise nondecreasing; beta <= beta' implies m_beta <= m_beta'; m_{c beta}(x) = c m_beta(cx);
m_{beta_1 + beta_2}(x) <= 2m_{beta_1}(2x) + 2m_{beta_2}(2x).
(c) For b in l_1, r > 0: sum_{j in F}(|a_j + rb_j| - |a_j| - s_j r b_j) = Exc_{(sb)_-}(r); for r < 0 the same with (sb)_+ and |r|.
(d) m_beta(x) <= kappa x on (0, x_0] implies Exc_beta(r) <= kappa r^2 on (0, x_0]; >= likewise.
Proof. (a) d/dr 2(r beta_j - |a_j|)_+ = 2 beta_j 1[r beta_j > |a_j|] a.e.; monotone convergence. (b) Each summand is convex and
nondecreasing in beta_j. Scaling: substitute. Sum: split {|a| < x(beta_1 + beta_2)} according to which of beta_1, beta_2 is larger; on
the first part beta_1 + beta_2 <= 2beta_1 and |a| < 2x beta_1. (c) |x + y| - |x| - sgn(x)y = 2(-sgn(x)y - |x|)_+ for x != 0. (d) (a). QED
Classification, with kappa_beta(x) := m_beta(x)/x: SPARSE (kappa -> 0; Z5's (CS), Exc = o(r^2)), SUPER-CRITICAL (kappa -> infinity),
CRITICAL (0 < liminf <= limsup < infinity), mixed otherwise.
Lemma 1.2 (critical profiles oscillate for geometric signatures). Let beta := v 1_S with S = {s_1 < s_2 < ...} subset F, v(s) = c 2^{-s},
and rho(s) := |a_s|/v(s) nonincreasing along S with rho(s_i) -> 0. Then at every jump point y = rho(s_i) (with rho(s_{i+1}) < rho(s_i))
kappa_beta(y+)/kappa_beta(y) >= 2; hence limsup_{x->0} kappa_beta(x) >= 2 liminf_{x->0} kappa_beta(x) whenever the latter is positive.
Proof. Put R_i := sum_{i' >= i} v(s_{i'}). As s_{i+1} >= s_i + 1, R_{i+1} <= 2v(s_{i+1}) <= v(s_i), so R_i = v(s_i) + R_{i+1} >= 2R_{i+1}.
For y = rho(s_i): m(y) = R_{i+1} (only s_{i'} with rho < y count) and m(y+) = R_i. QED
Model (Z5 7.1): v_l(s) = c_0 2^{-s} on S_l, |a_s| = 2^{-(1+b)s}: kappa(x) ~ x^{1/b - 1}: sparse iff b < 1, super-critical iff b > 1, critical
(and, by Lemma 1.2, oscillating by a factor >= 2) iff b = 1. Numerics (check_Dsharp.py) confirm the exponents of Lemma 3.2 below.

## 2. Raised engineered approximants. PROVED.

Two-piece data at arbitrary F: side-+ pair (b^+, omega^+) and side-- pair (b^-, omega^-) representing the same g (Definition
def:twopiece with no condition on F); b^theta := (b^+ + b^-)/2, v := b^+ - b^-.
Theorem 2.1 (T8 with raised support). Let T be admissible, I finite, F arbitrary, g in C(f) with two-piece data, rho^2 kappa_w < 1,
I_- := {m : Delta d_m < 0} satisfying (SC), and
  (CS-side)  m_{(sb^+)_-}(x) = o(x)  and  m_{(sb^-)_+}(x) = o(x)  (x -> 0)   [nothing on b^theta].
Then there are norm-attaining f'_i -> f with finite base support and g'_i in C(f'_i), g'_i -> rho g; so (f, rho g) in cl NA, and (f, g)
in cl NA if kappa_w <= 1.
Proof. Z5's proof of T8 (itself a modification of thm:engineered) with one change: for j in F cap [1, N_w] put
r_j := (8 rho s_1|b^theta_j| - |a_j|)_+ and
  a'' := a 1_{[1,N_w]} + sum_{j in K cap [1,N_w]} m_j z_j e_j* + sum_{j in F cap [1,N_w]} r_j s_j e_j*,   m_j := 4 rho s_1|b^theta_j|,
i.e. support coordinates in the window are raised to modulus max(|a_j|, 8 rho s_1|b^theta_j|), same sign; all other definitions and the
order of choices are unchanged.
(1) supp a' = (F cap [1,N_w]) union {window contacts with b^theta_j != 0} and z' = sgn a' there, so f' is norm attaining; ||a'' - a||_1 <=
alpha(N_w) + 8 rho s_1||b^theta||_1, i.e. (E1) of lem:approxfacts holds with 8 in place of 4. Lemma lem:approxfacts (E2)-(E5), Lemmas
lem:F1, lem:anchor, lem:scrambling and Steps 1, 2, 4, 6 use a'' only through (E1) and the forced data of f'; at late stages q*(a'') <= 2 and
|a'_j| >= |a''_j|/2 >= |a_j|/2 on F cap [1, N_w].
(2) Step 3 (base) on j in F cap [1,N_w]: a'_j + tau B^diamond_j = (1 - tau rho c)a'_j + tau rho beta^diamond_j with |tau rho c| <= 1/2, so
s_j(1 - tau rho c)a'_j >= |a''_j|/4. For diamond = theta (|tau| <= s_1): |tau rho beta^theta_j| <= rho s_1|b^theta_j| <= |a''_j|/8: no flip.
For diamond = +- (s_1 < |tau| <= T_0, sgn tau = diamond): the anti-sign part of tau rho beta^diamond_j is <= |tau| rho beta_j with beta =
(sb^+)_- resp. (sb^-)_+, and |a''_j| >= |a_j|, so as in Z5 a flip needs |a_j| < 4 rho|tau| beta_j and costs <= 2|tau| rho beta_j: total
Fl(tau) <= 2 rho|tau| m(4 rho|tau|), m := m_{(sb^+)_-} + m_{(sb^-)_+}. All other coordinates verbatim.
(3) The Step-0 condition "2 rho|tau| m(4 rho|tau|) <= delta tau^2/16 for |tau| <= T_0" uses only the side parts and holds for small T_0 by
(CS-side); Steps 5-6 as in Z5. QED
Remark. The raises do for support coordinates what the window masses do for contacts: absorb the two-sided use of the average data
below scale s_1; their total mass is O(s_1) whatever b^theta is. Consequently R1's requirement on |bbar^theta| is superfluous.

Theorem 2.2 (flip-extended version). Same as Theorem 2.1, but instead of (CS-side) assume: for some t_0 > 0,
  rho^2 max_{diamond = +,-} [ Gamma_w(b^diamond, omega^diamond) + sup_{0 < r <= t_0} Fl_r(b^diamond) ] < 1,
  Fl_r(b^+) := 2q_0 Exc_{(sb^+)_-}(r)/r^2,  Fl_r(b^-) := 2q_0 Exc_{(sb^-)_+}(r)/r^2,  and rho^2 Gamma_w(b^theta, omega^theta) < 1.
Then (f, rho g) in cl NA. PROVED. Proof: in Step 3 the side flip cost at f' is <= Exc_{beta}(rho|tau|(1 + O(T_0))) (|a'_j| >= |a_j|(1 - O(T_0
+ s_1)) after normalization), so it contributes at most (rho^2 tau^2/2)(sup_{r <= t_0}Fl_r + o(1)) to Gammahat (weight c' -> q_0), and it is
O(tau^2), so the rebalancing constant K_sharp of Step 0 still exists. Step 5 then reads Gammahat + E <= (tau^2/2)(rho^2 kappa^fl + delta/2),
kappa^fl := max_diamond(Gamma_diamond + sup Fl) and Gamma_theta <= kappa_w; with delta := (1 - rho^2 kappa^fl)/2 (fixed before T_0 <= t_0/rho)
this is <= (tau^2/2)(1 - delta). The theta-data carry no flips (raised). QED

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
||g||_1 + 1/t, lem:box; t||b^+- - B_+-||_1 <= K_1 t^2 + Kt^2 <= 1 once (1 + M_f(L))t^2 is small, which holds on the windows of Step 5
because T_i M_f(L_i) -> 0). Blocks: for k in cQ_m, varsigma_k := sgn w_m(k) (any sign if w_m(k) = 0): varsigma_k omega^+(k) <= (1 - d_+t)gap(k)/t
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
