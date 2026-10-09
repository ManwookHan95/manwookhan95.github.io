# Y3 part 3 — item (3): F = N and infinitely many swallowed carriers; item (2): (LSC-trunc); what remains of (O4)

Notation as in parts 1-2. Bx(j) := sum_{m in I} sum_k lambda_{k,m}|u_{k,m}(j)| (box profile; ||Bx||_1 <= sum lambda <= 1/3).
Block quantities: d_+-, omega_+- of a two-sided decomposition as in Lemma lem:suplevel (Theta_+ = omega_+ - d_+ w,
Theta_- = omega_- - d_- w); margins mu_{k,m}; M_f(L) := sum{1/mu_{k,m} : m in I, k in P_m, k in the coarse set C_L} where, for an
enumeration (k,m) -> l of all carriers fixed once and for all (for SLD-type designs: the ladder j), C_L := {(k,m) : l(k,m) <= L}.
For t > 0 let L(t) := min{L : sum_{l(k,m) > L} lambda_{k,m} <= t^3}.

## 3.1 Theorem N (box-dominated support, e.g. F = N). PROVED, every admissible T.

Theorem 3.1. Let T be admissible and I finite. Let f in S_{p*} satisfy
 (BD) there is C_a with Bx(j) <= C_a |a_j| for every j in N (this forces F = N: every coordinate lies in the support of some u_{k,m});
 (SC_I) the set I of all blocks satisfies the scrambling condition (Definition def:SC; it excludes degenerate peaks);
 (W_M) for every n in N: liminf_{T -> 0} T * M_f(L(2^{-n} T)) = 0.
Then f in Rec. No pinning, no room, no condition on strict non-peaks (infinitely many, near-threshold) and no condition on the mates
is needed; every carrier is swallowed by the support.

Proof. Fix g in C(f) and rho in (0,1). Choose eta_0, kappa_0, eps_tr := eta_0/2, eta <= eta_* with sqrt(1 + eta_Gamma(eta)) <= 1 +
kappa_0/2, as in the proof of Theorem thm:R0. All "f-constants" below depend only on f, g, rho, N, T (not on the scale).
Step 1 (data at one scale). Let t <= min(t_eta, 1), L := a coarse level with sum_{l > L} lambda_l <= t^3, and (B_+-, Theta_+-) a
two-sided decomposition of g at scale t. Put cQ_m := Q_m cap C_L (finite) and
  omega^+-_m := omega_{+-,m} 1_{cQ_m},   b^+-_0 := g - sum_m R_m*(omega^+-_m - d_m(omega^+-_m) w_m).
Both (b^+_0, omega^+) and (b^-_0, omega^-) represent g exactly. Estimates (m fixed, index dropped):
 (a) At peaks k: omega_+(k) is inward and |alpha(k)||omega_+(k)| <= t/(2 sigma) (Lemma suplevel(c)); by (eq:margin)
     sigma|alpha(k)| = lambda_k mu_k, so lambda_k|omega_+(k)| <= t/(2 mu_k). At carriers outside C_L, lambda_k|omega_+(k)| <= 4 lambda_k/t
     (|omega_+| <= (3+eta)/t, Lemma suplevel(a),(e)). Hence E_+ := sum_{k notin cQ} lambda_k|omega_+(k)| <= (t/2) M_f(L) + 4t^2;
     the same for omega_- (with the two-sided bound |omega_+(k)| + |omega_-(k)| <= t/(sigma|alpha(k)|) at peaks).
 (b) |d_+ - d(omega^+)| <= |d_+ - d(omega_+)| + |d(omega_+ 1_{notin cQ})| <= t/sigma + ||D(omega_+ 1_{notin cQ})||_2 <= t/sigma + E_+/m
     (Lemma suplevel(d); |d(omega)| = |<Dw, D omega>|/C <= ||D omega||_2 <= sum_k Phi_k|omega(k)|).
 (c) b^+_0 - B_+ = sum_m R_m*(omega_{+,m} 1_{notin cQ_m}) - sum_m (d_{+,m} - d_m(omega^+_m)) R_m* w_m, so
     ||b^+_0 - B_+||_1 <= K_1 t with K_1 := C_f(1 + M_f(L)) (C_f an f-constant; ||R_m* w_m||_1 <= 1), and pointwise
     |(b^+_0 - B_+)_j| <= (4/t) Bx(j) + |d_+ - d(omega^+)| Bx(j) <= 5 C_a |a_j|/t for t <= t_f. Same for b^-_0 - B_-.
 (d) X := b^+_0 - b^-_0 = sum_m R_m*((omega^-_m - omega^+_m) - Delta d^0_m w_m), Delta d^0_m := d_m(omega^-_m) - d_m(omega^+_m);
     |omega^+-| <= 4/t and |Delta d^0| <= ||D omega^-|| + ||D omega^+|| <= 4/t, so |X_j| <= (12/t) Bx(j) <= 12 C_a|a_j|/t.
Step 2 (common shift; exact cushion bounds). Put A_j := C_A|a_j|/t with C_A := 6C_a + 1, x_j := s_j b^+_{0,j}, y_j := s_j b^-_{0,j}.
By the cushion lemma and (c), x_j >= -|a_j|/t - f^+_j - 5C_a|a_j|/t >= -A_j - f^+_j and y_j <= A_j + f^-_j; by (d), x_j - y_j = s_j X_j >=
-2A_j. Let sigma_j be the point of [y_j - A_j, x_j + A_j] closest to 0; |sigma_j| <= (-x_j - A_j)_+ + (y_j - A_j)_+ <= f^+_j + f^-_j, so
sigmat := sum_j s_j sigma_j e_j* has ||sigmat||_1 <= t/(2q_0). Put kappa' := -(sigmat)(zhat) (|kappa'| <= (1+||U||) t/(2q_0)) and
  b^+- := b^+-_0 - sigmat - kappa' a,  g_t := g - sigmat - kappa' a.
Then (b^+, omega^+) and (b^-, omega^-) both represent g_t; b^+-(xi) = q_0(g(zhat) - sigmat(zhat) + sigmat(zhat)) = 0; b^+ - b^- = X;
(s_j b^+_j)_- <= A_j + |kappa'||a_j| <= (C_A + 1)|a_j|/t and (s_j b^-_j)_+ <= (C_A + 1)|a_j|/t (t <= 1); and
  p*(g - g_t) <= (1 + ||U||)(||sigmat||_1 + |kappa'| ||a||_1) <= K t,  K := (1+||U||)^2/q_0   (an f-constant).
F = N, so there is no side condition off F; omega^+-_m in c_00(Q_m): (b^+-, omega^+-) are two-piece data for g_t (Definition def:twopiece
at arbitrary F), with d-mismatch Delta d^0 of arbitrary sign.
Step 3 (Gamma_w). The difference (b^+, omega^+ - d(omega^+)w) - (B_+, Theta_+) = (b^+_0 - B_+ - sigmat - kappa'a, -omega_+1_{notin cQ} +
(d_+ - d(omega^+))w) has base part of l_1-norm <= (K_1 + K)t and block part with sigma_m H_m <= sigma_m ||D omega_+ 1_{notin cQ}||^2/C_m
<= (E_+/m)^2 sigma_m/C_m (H_m ignores multiples of w_m). As sqrt(Gamma_w) is a seminorm and Gamma_w(B_+, Theta_+) <= 1 + eta_Gamma(eta)
(Lemma budget(d)), sqrt(Gamma_w(b^+, omega^+)) <= sqrt(1 + eta_Gamma(eta)) + K_4 t with K_4 := C'_f(1 + M_f(L)). Same for the - data.
Step 4 (local validity). On the base, the bounds of Step 2 are cushion-proportional with constant C_+ := C_A + 1, and t||b^+-||_1 <= A_0
(||B_+-||_1 <= ||g||_1 + sum lambda_k|Theta_+-(k)| <= ||g||_1 + 1/t by Lemma box; plus (K_1 + K)t). On the blocks, for k in cQ_m and
varsigma_k := sgn w_m(k) (any sign if w_m(k) = 0): varsigma_k omega^+(k) <= (1 - d_+t) gap(k)/t <= 1.5 gap(k)/t (Lemma suplevel(f),
|d_+ t| <= 1/2) and varsigma_k omega^+(k) >= -4/t; symmetrically varsigma_k omega^-(k) >= -1.5 gap(k)/t and <= 4/t: every coordinate
is of the "inward-only" third kind of Z6-referee Lemma 2.1 with A' = 4. Lemma onesidedtransfer in the form of Z6-referee Lemma 2.1,
with the base step of Z5 Lemma 3.2 (no flips: r(s_j b_j)_- <= c_flat C_+|a_j| <= |a_j|/2 for c_flat <= 1/(2C_+)), gives c_flat, t_1 > 0
(f-constants, independent of L) with p*(f + r g_t) <= 1 + (r^2/2)(Gamma_w + eps_tr) for 0 < r <= c_flat t (+ data) and
-c_flat t <= r < 0 (- data). With Step 3: p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t as soon as K_4 t <= kappa_0/2.
Step 5 (averaging). Fix n_0 >= 24 rho^2 K/(c_flat(1 - rho^2)) (an f-constant). By (W_M) with n = n_0 choose T_i -> 0 with
T_i M_f(L(2^{-n_0}T_i)) -> 0; use the n_0 dyadic scales t = T_i 2^{1-s}, 1 <= s <= n_0, all with the coarse level
L_i := L(2^{-n_0} T_i) (so sum_{l > L_i} lambda_l <= t^3 for each of them), and i so large that T_i <= min(t_eta, t_1, t_f, 1) and
K_4(L_i) T_i <= kappa_0/2. Lemma avgfunctionals (closeness constant K, window length n_0, c_flat): rho gbar_i in C(f) and
p*(rho gbar_i - rho g) <= 2 rho K T_i/n_0 -> 0, gbar_i := (1/n_0) sum_s g_{t_s}.
Step 6 (engineering). The averaged data Dbar_i := (1/n_0) sum_s (b^+-_s, omega^+-_s) are two-piece data for gbar_i (representation
is linear, d_m is linear, supports in Q_m), with kappa_w(Dbar_i) <= (1 + kappa_0)^2... precisely kappa_w <= (sqrt(1+eta_Gamma)+kappa_0/2)^2
<= 1 + eta_0/2 by convexity, so kappa_w(rho Dbar_i) <= rho^2(1 + eta_0/2) <= 1; their one-sided parts satisfy
(s bbar^+)_- , (s bbar^-)_+ <= (C_A + 1)|a|/(2^{-n_0}T_i): cushion compatibility (R-inf) with C_R := (C_A+1)2^{n_0}/T_i, which
implies (CS-side). By (SC_I) every set of blocks with Delta dbar_m < 0 satisfies (SC). Theorem 1.2 (or Z5 Theorem 4.3) applied to the mate
rho gbar_i in C(f) with data rho Dbar_i gives (f, rho' rho gbar_i) in cl NA for every rho' < 1, hence (f, rho gbar_i) in cl NA.
Let i -> infinity, then rho -> 1. QED

Remarks 3.2. (a) Why no pinning is needed: under (BD) every switching, even of box size (|Delta theta_l| <= 6 lambda_l/t), is absorbed by
the cushions (Step 1(d)), so EXACT two-piece data exist at every scale; the block parts that two-piece data cannot carry (peak usage,
fine carriers) are moved into the base, where they cost only second order (Step 3, via the margins) and are cushion-proportional by (BD).
The closeness constant K is an f-constant, so windows of FIXED length n_0 suffice; the design plays no role.
(b) The critical-mate issue of part 2 (Section 2.3) does not arise here: window data built at scale t remove the scale-t flips by a
common shift at closeness cost O(t), and are cushion-proportional (flip-free) below scale c_flat t. Corollary 2.4 (fixed optimal data)
needs (CS) for g; Theorem 3.1 needs nothing on g but (SC_I) and (W_M) on the blocks.
(c) (W_M) is a rate condition on the margins of coarse peaks against the lambda-tail; for SLD-type designs L(t) <= l whenever
t in W(l), so (W_M) follows from liminf_l T_hi(l) M_f(l) = 0, i.e. M_f(l) = o(l 2^{l^3} Lambda°(l)) along a subsequence.
(d) Without (BD) the method fails exactly where box-size switching meets thin support: on {j : |a_j| << Bx(j)} the data at scale t would
violate the cushions by (8/t) Bx(j), and a violation of size ~1/t at fixed data pays first-order flips at every smaller scale.
Sufficient for avoiding this: (BD) on F together with pinning of all but finitely many carriers (part 1, Theorem R1 / 1.9).

## 3.2 Infinitely many swallowed carriers at infinite F with contacts (Z4 Theorem A, Z6 Theorem U'). SKETCH (modifications listed).
Claim A_inf. Z4 Theorem 3.1 (S_Binf; SLD_G made N-independent) holds for f with F infinite provided: (i) every bad carrier is contact
swallowed (S_l \ F infinite), (ii) (BD_B) on F: sum_{l in B} lambda_l|u_l(j)| <= C_a|a_j| for j in F, (iii) (H2'), (H3), (DR) as in Z4
with the repair directions cushion-compatible on F (automatic under (ii)), (iv) (W_inf) with Xi_f multiplied by C_a^2/mu_f(l)^2, where
mu_f(l) := min_{l' in B cap [1,l]} ||v_{l'} 1_{S_{l'} \ (T(B cap [1,l]) union F)}||_1.
Changes to Z4 Steps 1-9: Step 1 verbatim (rooms off F). Step 2 verbatim (switching budget off F). Step 3: Lemma 2.2's weights
m_l(U, max F) are replaced by unit weights in the configuration systems (Hoffman constants H_1(kappa), still finitely many configurations
per level, still a design constant) and viol'_1 <= c_U/min(gamma_T, 2 mu_f); this is the factor 1/mu_f. Steps 4-5 verbatim. Step 6: the
base part B_+ 1_F is replaced by the common shift of Step 2 of Theorem 3.1 with A_j := C_A(l_*)|a_j|/t, C_A(l_*) ~ C_a C_diamond(l_*)
(|X_j| <= (6 + C_diamond) Bx_B(j)/t on F because |tau'_l| <= 6 lambda_l/t + C_diamond t and lambda_l >= t^2 on the active set); closeness
as in R1 Claim 3.1. Step 7: the one-sided expansion with cushion-proportional base (Z5 Lemma 3.2), c_flat ~ 1/(C_A(l_*) + A_2) — the factor
C_a in (iv). Steps 8-9: windows as in Z4; Theorem 1.2 with (R-inf) data. Not written out line by line; the same modifications apply to
Z6 Theorem U' (its additional ingredients — Farkas pinning, rigid blocks — concern off-F and block data only).
F = N is NOT covered by A_inf ((H2') needs good or contact-swallowed peaks to pin the shift; at F = N none exist and the shift is free);
it is covered by Theorem 3.1 instead, at the price of (SC_I).

## 3.3 A master theorem at infinite F, and (LSC-trunc). PROVED / OPEN.

Theorem 3.3 (master theorem; any admissible T, I finite, F arbitrary). Let g in C(f), rho in (0,1), eta_0 with rho^2(1+eta_0) <=
(1+rho^2)/2. Suppose there are c_flat > 0, beta in l_1 with beta >= 0 and m_beta(x) = o(x), C_+ >= 1, and windows (T_j, n_j, K_j) with
T_j -> 0, n_j >= 24 rho^2 K_j/(c_flat(1-rho^2)), K_j T_j/n_j -> 0, such that for every j and every t in {T_j 2^{1-s} : s <= n_j} there
are two-piece data (b^+-, omega^+-) (at arbitrary F) for a functional g_t with:
 (i) p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for 0 < r <= c_flat t (+ data) and -c_flat t <= r < 0 (- data);
 (ii) p*(g - g_t) <= K_j t;  (iii) Gamma_w(b^+-, omega^+-) <= 1 + eta_0/2;
 (iv) (s b^+)_- <= C_+|a|/t + beta and (s b^-)_+ <= C_+|a|/t + beta on F;
 (v) for every m, either Delta d_m >= 0 for all these data, or the set of blocks with some Delta d_m < 0 satisfies (SC).
Then (f, rho g) in cl NA, along norm-attaining approximants with FINITE base support. If this holds for every rho < 1, (f, g) in cl NA.
Proof. Lemma avgfunctionals: rho gbar_j in C(f), rho gbar_j -> rho g. The averaged data are two-piece data with kappa_w <= 1 + eta_0/2
(convexity), Delta dbar_m = average (so (v) passes to the averages: if all Delta d_m >= 0, then Delta dbar_m >= 0; otherwise (SC) is
assumed for the relevant blocks), and (iv) passes to the averages with T_j 2^{1-n_j} in place of t (convexity of x_+-); by Lemma 2.3 the
side parts satisfy m(x) <= 2 m_{C_+|a|/T}(2x) + 2 m_beta(2x) = 0 + o(x) for x < T/(2C_+), i.e. (CS-side). Theorem 1.2. QED
Remark. (i) is what Lemma R2 (one-sided transfer with sparse flips) gives from (iv) with beta = C_* U_* and bounded Gamma_w, sizes and
block conditions; so Theorem 3.3 is the common skeleton of Theorems R1, 1.9 and 3.1 and of Z5 Theorems 3.3-6.1.

Status of (LSC-trunc) [for all f, g in C(f), rho < 1, eps > 0 there is f' with FINITE base support, p*(f'-f) < eps, dist(rho g, C(f')) < eps].
(a) PROVED: (LSC-trunc) is equivalent, given Lemma Z at all f with finite base support, to Lemma Z at all f (Z5 Proposition 5.4).
(b) PROVED: (LSC-trunc) holds for every (f, g) satisfying the hypotheses of Theorem 3.3 (the approximants are norm attaining with
finite support). This now includes: Z5 Theorems 3.3-3.6 and 6.1, R1, Theorem 1.9 (super-critical support swallowing), Corollary 2.4
(block-tame points, cushion-sparse mates), Theorem 3.1 (box-dominated support: every mate), pure base mates (Z5 Lemma 5.1), cl Cert(f).
(c) PROVED (truncation is free): in Theorem 1.2 the far support becomes contacts of f' with first-order cost rho|tau| sum_{j > N_w}
(s_j v_j)_- <= delta s_1|tau|/32, controlled by the tail of the FIXED vector v = b^+ - b^-; the near support keeps its cushions, raised
where the average data need it. Hence "truncation" is never the obstruction: (LSC-trunc) fails for (f, g) only if NO exact data
(fixed, or window data at f or at a companion with o(T_lo^2) cost, Z3 Theorem E) exist for (approximations of) g. Per-mate far contact
signs (Z5 next step 3) are unnecessary: the far switching of fixed data is z-signed automatically (side admissibility), and the far
cushions are not needed.
(d) OPEN (precise remaining step of (LSC-trunc) beyond the finite-F core): produce data with property (iv) for mates whose window
decompositions carry CRITICAL constrained switching through support-swallowed carriers, i.e. bounded switching (not box size) in the
cushion-violating direction on a set of support coordinates of v_l-mass comparable to the scale (m_l(y) asymp y along y -> 0, not
super-critical, not sparse), or through non-d-neutral / non-resonant-target support-swallowed carriers (part 1, Remark 1.10(c),(d)).
At such f, fixed data reproduce the scale-t decomposition's flips at every smaller scale with the local constant kappa_l(r) =
m_l(r)/r, which oscillates (log-periodically for geometric signatures), while the mate pays kappa_l(t) at scale t; un-switching saves the
flips but costs Gamma of the same order (part 2, 2.3 and Remark 1.10). Two-stage approximation (cushion-sparse companion, then
truncation) meets the same quantitative obstruction: a companion making the constrained switching cushion-compatible on a window
[T_lo, T_hi] raises the support at level ~ T_hi D on the deep set, cost ~ T_hi D m_l(T_hi D) ~ T_hi^2 (critical), while Theorem E needs
o(T_lo^2) = o(4^{-n} T_hi^2). PROVED as statements about these methods (the arithmetic of 1.8, 2.3); not a non-recovery claim.

## 3.4 What remains of (O4) after Y3 (precise). Labels as indicated.
For the design D_sigma (part 1) — or SLD/SLD_G/D''' where no design feature is used — and every N, a first row f with infinite F is
in Rec (PROVED) if one of the following holds:
 (1) (SR) or sign-mixed/cushion room [Z5 Theorems 3.4-3.6]; window-pinned mates [Z5 Theorem 3.3];
 (2) finitely many bad carriers, (W*), (H2), (H3-inf), and every bad carrier with S_l cap F infinite is either cushion-sparse [R1] or
     super-critical swallowed (supp u_l in F, d-neutral, monochromatic, (QM), m_l(y)/y -> infinity) [Theorem 1.9];
 (3) a box-dominates the design (then F = N), all blocks satisfy (SC), and the margin rate (W_M) [Theorem 3.1, every admissible T];
 (4) block-tame f (any F) and the mate is cushion-sparse and V_f is cushion-sparse [Corollary 2.4, every admissible T];
 (5) infinitely many contact-swallowed bad carriers with box domination on F [Claim A_inf, SKETCH].
OPEN (consensus core, (O4) part):
 (O4-crit) critical support swallowing: a bad support-swallowed carrier with 0 < liminf m_l(y)/y and limsup m_l(y)/y < infinity
     (model |a_j| ~ v_l(j)^2), or mixed (oscillating between sparse and super-critical), whose constrained switching does not vanish;
 (O4-nd) non-d-neutral, or non-resonant-target, non-sparse support-swallowed carriers (Remark 1.10(c),(d));
 (O4-box) infinitely many bad carriers without box domination of F (box-size switching on thin support), and F = N without (SC_I);
 (O4-fin) all finite-F core items (O1)-(O3), (r), (d), (m), (h) of ADDENDUM 5, which reappear verbatim at infinite F.
No counterexample mechanism was found. Leaning: positive; the infinite-F part of the core is now a single quantitative phenomenon
(critical support swallowing), of the same "exactness vs scale" type as (O1)(i).
