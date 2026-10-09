# Y3 part 2 — item (4): the exact one-sided coefficient at arbitrary F; block-tame points with infinite support; the critical case

Notation as in part 1 and the note. "Block-tame" := every Q_m finite, no degenerate peaks, (MS) at xi (the block half of (BT));
nothing is assumed about F, K, J. Side-+ admissible pair (b, omega) at arbitrary F: b in l_1 represents g together with
omega_m in R^{Q_m} (finitely supported in Q_m), b_j = 0 on J, z_j b_j >= 0 on K, NO condition on F; side-- likewise with
z_j b_j <= 0 on K. gamma^+-(g) := inf Gamma_w over side-+- admissible pairs (in [0, infinity]).

## 2.1 Theorem 2.1 (one-sided coefficient at arbitrary F). PROVED.
Let T be admissible, I finite, f in S_{p*} block-tame with F arbitrary, and g in X* with g(xi) = 0. Then:
 (a) liminf_{t->0+} 2(p*(f + tg) - 1)/t^2 >= gamma^+(g)   (and the same for t -> 0- and gamma^-);
 (b) if gamma^+(g) < infinity, the infimum is attained;
 (c) for every side-+ admissible pair (b, omega),
     limsup_{t->0+} 2(p*(f+tg) - 1)/t^2 <= Gamma_w(b, omega) + 2 q_0 limsup_{t->0+} Exc_{(sb)_-}(t)/t^2
     (Exc as in part 1, 1.1); the same for side - with (sb)_+ and t -> 0-;
 (d) hence lim_{t->0+} 2(p*(f+tg)-1)/t^2 = gamma^+(g) whenever some optimal side-+ pair has Exc_{(sb)_-}(t) = o(t^2) (e.g. (sb)_-
     cushion-sparse, Lemma 1.1(d)); for F finite this is Theorem thm:onesided(a);
 (e) every g in C(f) has optimal two-piece data (b^+-, omega^+-) with kappa_w <= 1.

Proof. (a) We repeat Steps 1-4 of the proof of Theorem thm:onesided; only Step 1 (the test points) used F finite, through the Gram
system, and we replace it by a choice that works for every F.
Step 1'. Let k in H with <k, e> = 0, chi_c in C_+ := {chi in c_00 : chi = 0 on F, z_j chi_j <= 0 on K}, and put
  kappa := ||k||^2/(2q_0),  k_2 := -kappa e,  chi := Uk + chi_c,  chi_2 := U k_2 = -kappa U e,  eta_t := xi + t chi + t^2 chi_2,
  h_t := q_0 e + t k + t^2 k_2 = (q_0 - t^2 kappa) e + t k,   Z_t := eta_t - U h_t = q_0 z + t chi_c .
(Recall xi = q_0 zhat = q_0 z + q_0 Ue.) Since k is orthogonal to e, ||h_t||^2 = (q_0 - t^2 kappa)^2 + t^2||k||^2 = q_0^2 + t^4 kappa^2,
so ||h_t|| <= q_0 + t^4 kappa^2/(2q_0). On F, Z_{t,j} = q_0 s_j; on K, z_j chi_{c,j} <= 0 and chi_c is finitely supported, so
|q_0 z_j + t chi_{c,j}| <= q_0 for small t; on J (|z_j| < 1) the same holds for small t (finitely many j); elsewhere |Z_{t,j}| =
q_0|z_j| <= q_0. As B_{q**} = B_{l_infinity} + U(B_H), q**(eta_t) <= max(||Z_t||_infinity, ||h_t||) <= q_0 + O(t^4). Further
a(eta_t) = a(xi) + t a(Uk) + t a(chi_c) + t^2 a(U k_2) = q_0 + t<U*a, k> + 0 - t^2 kappa <U*a, e> = q_0 - t^2 kappa nu
(<U*a, k> = nu <e,k> = 0, chi_c vanishes on F, <U*a, e> = nu). Hence the base excess satisfies
  E_q(t chi + t^2 chi_2) = q**(eta_t) - a(eta_t) <= t^2 nu ||k||^2/(2q_0) + O(t^4),
which is exactly the base bound used in Step 1 of the note (there obtained from the Gram system). chi, chi_2 are in c_0 = X.
Steps 2-4 are verbatim: the block test (Step 2) uses only Q_m finite, no degenerate peaks, (MS), chi, chi_2 in X and |delta_{i,k}| <=
lambda_k q(chi_i); weak duality (Step 3) uses b(chi_c) <= 0 (chi_c in C_+, b side-+ admissible, no condition on F needed because chi_c
vanishes on F) and 2<P^perp U*b, k> <= q_0 h(b) + (nu/q_0)||k||^2; strong duality (Step 4): P(y), Q(y) as in the note; -P_*(pi) =
q_0 h(b_pi) + [0 if b_pi = 0 on J and z_j(b_pi)_j >= 0 on K, +infinity otherwise], b_pi := g - phi_pi/2 in l_1 (phi_pi = sum_m R_m* V_m is
an absolutely convergent series in l_1); so the dual problem is exactly the minimization of Gamma_w over side-+ admissible pairs, with no
constraint on F. Fenchel's theorem gives sup J = gamma^+(g) and attainment (b). With the test ratio (eq:testratio), (a) follows.
(c) The proof of Proposition prop:onesidedupper applies with one change: by Lemma lem:bookkeeping(b) and Lemma 1.1(c),
G_b(a + tb) = Exc_{(sb)_-}(t) + nu Psi(tU*b/nu) for t > 0 (off F the summands vanish by side admissibility). If the limsup of
Exc/t^2 is infinite there is nothing to prove; otherwise Exc_{(sb)_-}(t) = O(t^2), so Ghat_b := Exc_{(sb)_-}(t) + (t^2/2)h(b)(1 + Kt)
is O(t^2), and Proposition prop:rebalancing (valid for every f and every Ghat_b >= G_b(A); its error term uses
|q*(A) - 1| + q*(A - a) = O(t) for b in l_1) gives p*(f + tg) <= 1 + q_0 Exc(t) + (t^2/2)(Gamma_w(b,omega)(1 + Kt) + 2|I|K_3 eta_1) +
O(t^3); eta_1 is arbitrary. Transfer data exist at every f (Z5 T1: transfer peaks are built at xi from a in l_1).
(d) Combine (a) and (c). (e) g in C(f) gives 2(p*(f+tg) - 1)/t^2 <= 2(s(t)-1)/t^2 <= 1; by (a) gamma^+-(g) <= 1, and (b) gives
minimizers. QED

Remark 2.2. The note (and Z5, list of results not valid at infinite F) attributed the finiteness of F in thm:onesided to the Gram
system of Step 1. The test points of Step 1' (second-order correction k_2 = -kappa e, chi_2 = Uk_2, which moves a(eta_t) instead of
moving Z_t radially on F) work for every F, including F finite. What genuinely changes at infinite F is the UPPER bound: optimal data
may have flips (c), and then the exact limit can exceed gamma^+ (Section 2.4).

## 2.2 Recovery at block-tame points with infinite support. PROVED.

Put V_f := sum_{m in I}( sum_{k in Q_m} lambda_{k,m}|u_{k,m}| + |R_m* w_m| ) in l_1 (an f-datum; Q_m finite).
Lemma 2.3. For beta_1, beta_2 >= 0 and c > 0: m_{beta_1 + beta_2}(x) <= 2 m_{beta_1}(2x) + 2 m_{beta_2}(2x) and m_{c beta}(x) = c m_beta(cx).
Proof. Split {|a| < x(beta_1 + beta_2)} by which of beta_1, beta_2 is larger. QED
Corollary 2.4. Let T be admissible, I finite, f block-tame with F arbitrary, and suppose V_f is cushion-sparse: m_{V_f}(x) = o(x).
Then every g in C(f) with m_{|g| 1_F}(x) = o(x) is recovered: (f, g) in cl NA((c_0, p), l_2^2), along norm-attaining approximants
with finite base supports.
Proof. By Theorem 2.1(e), g has optimal two-piece data with kappa_w <= 1, b^+- = g - sum_m R_m*(omega^+-_m - d_m(omega^+-_m) w_m),
omega^+-_m in R^{Q_m}. Hence |b^+- - g| <= C V_f with C := max_m max(||omega^+-_m||_infinity, |d_m(omega^+-_m)|) and (s b^+)_- <=
|g| + C V_f, (s b^-)_+ <= |g| + C V_f on F; by Lemmas 1.1(b) and 2.3 both are cushion-sparse. Block-tame implies (SC) for every set of
blocks (remark after Definition def:SC; it uses only the block data). Theorem 1.2 (raised engineered approximants) with rho^2 kappa_w
< 1 for every rho < 1 gives (f, rho g) in cl NA; let rho -> 1. QED

Box domination. Put Bx(j) := sum_{(k,m) : m in I} lambda_{k,m}|u_{k,m}(j)| (the box profile; ||Bx||_1 <= 1/3). Say a BOX-DOMINATES the
design if Bx(j) <= C_a|a_j| for all j (this forces F to contain the support of Bx, essentially F = N; e.g. F = N and
a := Bx + 2^{-j} normalized). Then V_f <= 2|I| Bx <= 2|I| C_a |a| is cushion-dominated, so Corollary 2.4 applies to every block-tame f
with box-dominating a, for EVERY admissible T. This is the base-side part of item (3) at F = N: when a box-dominates, the support never
obstructs anything; the remaining conditions are on the blocks (block-tame) and on the mate (cushion-sparse).

Lemma 2.5 (mates are at most critical under box domination). If a box-dominates (constant C_a) and g in C(f), then for all t > 0
  sum_{j in F} ( (s_j g_j)_- - (1 + 3C_a)|a_j|/t )_+ <= t/(4q_0)   and the same with (s_j g_j)_+;
equivalently Exc_{(sg)_-}(r) <= (1 + 3C_a) r^2/(2q_0) for all r > 0: the one-sided parts of every mate are at most critical.
Proof. Take a two-sided decomposition at scale t: g = B_+ + L*Theta_+, |(L*Theta_+)_j| <= sum lambda_k|Theta_+(k)||u_k(j)| <= 3Bx(j)/t
(Lemma lem:suplevel(e)), so (s_j g_j)_- <= (s_j B_+(j))_- + 3Bx(j)/t <= |a_j|/t + f^+_j + 3C_a|a_j|/t; sum_F f^+_j <= t/(4q_0). The
second form: with c := 1 + 3C_a and r := t/c, sum 2(r(sg)_- - |a|)_+ = (2/c) sum (t(sg)_- - c|a|)_+ <= ... = 2t^2/(4q_0 c^2)... (direct
rescaling; constants immaterial). QED

## 2.3 What remains at block-tame points: critical mates. ANALYSIS (labels as marked).

Let a box-dominate, f be block-tame, and g in C(f) critical: 0 < liminf Exc_{(sg)_-}(t)/t^2 (or the same for (sg)_+).
(i) PROVED (data-independence of the flip term). For every side-+ pair (b, omega) and t <= 1/(2C_V),
  Exc_{(sg)_-}(t(1 - C_V t)... ) ... precisely: with |b - g| <= C_V|a| on F (C_V := C 2|I| C_a as in 2.2),
  (1 - C_V t) Exc_{(sg)_-}(t/(1 - C_V t)) <= Exc_{(sb)_-}(t) <= (1 + C_V t) Exc_{(sg)_-}(t/(1 + C_V t)).
  Proof: 2(t(sb)_- - |a|)_+ lies between 2(t(sg)_- - (1 +- C_V t)|a|)_+, and 2(tx - c|a|)_+ = 2c((t/c)x - |a|)_+. QED
  So all side-+ data have the same flip coefficient Fl_t(g) := 2q_0 Exc_{(sg)_-}(t)/t^2 up to a factor 1 + O(t), and by Theorem 2.1(c)
  limsup 2(p*(f+tg)-1)/t^2 <= gamma^+(g) + limsup Fl_t(g).
(ii) PROVED (what fixed data need). If gamma^+(g) + sup_{0 < t <= t_0} Fl_t(g) <= 1 for some t_0 > 0 (and the same on the - side),
  then the optimal data satisfy the hypothesis of the FLIP-EXTENDED engineering (Theorem 1.2 with the flip cost of Step 2 counted in the
  coefficient instead of being o(tau^2): Step 5 then reads rho^2(Gamma_diamond + sup_{r <= rho T_0} Fl_r) + 5delta/8 <= 1 - delta, which
  holds after choosing delta := (1 - rho^2)/4 and T_0 <= t_0/rho; the theta-data are raised and carry no flips), and g is recovered.
  [The flip-extended engineering is Theorem 1.2's proof with the condition "Fl(tau) <= delta tau^2/16" replaced by
  "Fl(tau) <= (rho^2 tau^2/2)(sup_{r <= rho T_0} Fl_r/q_0)(q_0) + delta tau^2/16"; PROVED by the same computation.]
(iii) The mate condition gives, at each scale t, only: there is a decomposition with total excess <= s(t) - 1. Its flip part can be
  SMALLER than q_0 Exc_{(sg)_-}(t) because the block side can absorb anti-sign mass of g on the flip set
  Phi_t := {j in F : |a_j| < t(s_j g_j)_-} through FAR carriers: a strict non-peak k with gap gamma_k, lambda_k small and u_k concentrated
  on Phi_t can carry Theta(k) up to gamma_k/t at second-order cost ~ lambda_k^2 gamma_k^2/(m^2 C) while saving flip cost
  ~ 2 lambda_k gamma_k ||u_k 1_{Phi_t}||_1 (PROVED as an inequality between these two numbers; by density (T-d) such k exist at every
  scale). The absorption capacity at j is at most M Bx(j)/t <= M C_a|a_j|/t, i.e. the effective cushion is between |a_j|/t and
  (1 + M C_a)|a_j|/t. Consequently the true one-sided value at scale t lies between gamma^+ + Fl_{t(1 + MC_a)}(g)(1+MC_a)^{-2}... and
  gamma^+ + Fl_t(g), and the condition of (ii) can fail while g in C(f): fixed data pay Fl_t(g) at every scale, the mate pays a
  scale-dependent smaller amount using scale-dependent far carriers. HEURISTIC (no example with strict failure is constructed).
(iv) PROVED (log-periodicity is unavoidable for the SLD signatures). If beta = c v_l 1_{S_l} with v_l(s) = delta_l 2^{-s}/n_l and rho_l(s) =
  |a_s|/v_l(s) nonincreasing along S_l (gaps >= 1), then m_beta is a step function whose value just above x = rho_l(s)/c is
  c sum_{s' >= s} v_l(s') <= 2 c v_l(s), and just below is <= c v_l(s)... in particular, if m_beta(x) >= kappa_0 x on (0, x_0) then
  sup_{x < x_0} m_beta(x)/x >= 2 inf_{x < x_0} m_beta(x)/x when consecutive rho-values are separated by a factor >= 2, and in general
  the jumps make kappa_beta oscillate unless the rho_l(s) accumulate super-geometrically (which forces super-criticality).
  [Statement kept qualitative; the point is that "exactly self-similar" critical profiles, for which (ii) would follow from Lemma
  2.5-type equalities, do not occur for geometric signatures.]

Precise remaining step (OPEN), item (4): at a block-tame f with box-dominating a, recover CRITICAL mates g, i.e. show that
  limsup_{t->0} [2(p*(f+tg) - 1)/t^2 - Fl_t(g)] ... more precisely, produce data whose flip coefficient at every scale r <= T_0 is at most
  the flip part of SOME decomposition at scale r, or replace fixed data by a scale-adaptive construction (far-carrier absorption).
  Pure base mates b in C_q(a) with critical flips ARE recovered (Z5 Lemma 5.1, truncation, scale by scale), which shows that criticality
  alone is not an obstruction; the open part is the interplay of critical base mass with far-carrier absorption.

## 2.4 Liminf-sparsity. SKETCH.
Claim: in Theorem 1.2 the condition m(x) = o(x) can be weakened to liminf_{x->0} m(x) log(1/x)/x = 0, for d-neutral data with |I| = 1
(or under a first-order d-repair condition).
Sketch: choose T_0 along a sequence with m(8 rho T_0) <= theta T_0/log(1/T_0), theta -> 0; raise every j in F with |a_j| < 8 rho T_0 beta_j
to 8 rho T_0 beta_j (beta := (sb^+)_- + (sb^-)_+), total mass R <= 8 rho T_0 m(8 rho T_0) = o(T_0^2/log); the raised row f^r is a
companion with p*(f^r - f) = O(R log(1/R)) = o(T_0^2) (Z3 Lemma 3.1), at which the data have NO flips at scales <= T_0. The data are
exact two-piece data at f^r up to the d-mismatch Delta d^r = X(delta)/|R** zhat^r| (Z3 Lemma 1.2), delta = U(e^r - e); X(delta) is
first order in the raise with coefficient <P^perp U*X, U*e_j>/nu at j, and can be made 0 (or >= 0, allowed by Corollary cor:D1) by a
small adjustment of one shallow coordinate j_0 in F when this coefficient is nonzero for some j_0 (|I| = 1); if it vanishes for all
j in F the residual second-order term has the sign of -X(Ue), which may be wrong. Then run Theorem 1.2 at f^r and conclude with Lemma
lem:assembly with respect to the ORIGINAL (f, g): p*(f' - f) <= p*(f' - f^r) + p*(f^r - f) <= (1-rho^2)T_0^2/6 for late stages.
Gaps: the d-repair in the degenerate case and for several blocks; the uniformity of the (T_0)-constants of Theorem 1.2 at f^r
(continuity in f^r -> f, as in Z3 Lemma U). Not used below.
