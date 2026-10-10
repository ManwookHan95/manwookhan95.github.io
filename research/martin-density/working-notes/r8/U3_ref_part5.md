# U3-ref part 5 — Proofs of the fixes (F1)-(F7) and of the new finding (F6)

Conventions as in U3 (data convention Delta := d(omega^-) - d(omega^+); N = 1 in F1-F3; design with (SF*), (SF_tau), (b'), (Z0),
diagonal U; "aligned" carrier: z = sgn(val) on its signature set).

## F1. Corrected nested-tuning induction for Theorem NT (existence).  SKETCH (complete outline; every step is a one-dimensional
## intermediate value argument or a finite Lipschitz estimate).  Replaces U3 3.1 stages (i)-(iii).
Ingredients.  (a) Parameter b in the open positive orthant Omega_+ of S^2; for y supported in F, y(zhat) = <y, Phi(b)>, Phi(b) = (1 + s_j b_j)_j.
(b) HYSTERETIC owner rule for non-special carriers (V4 Prop. 5.3): reference sign eps_l fixed at the stage where l is first assigned,
kept as long as eps_l A_l(b) > -(B_l + delta_l H_l)/2; then n_l|val_l| >= (B_l + delta_l H_l)/2 with sign eps_l (aligned, robust peak by
V4 Theorem 2.2 Step 4 with |val| >= delta°/2).  For D_Omega-type ladders delta_l H_l ~ 2^{-l - 2^l} decreases super-exponentially, so the
hysteresis margin of every carrier l' < l exceeds C delta_l H_l by a huge factor.  (c) theta^{(L)}(b) := threshold of the block vector of
the carriers <= L; any completion changes it by at most eta_L := L_Theta (1 + ||U||) sum_{l > L} lambda_l (V4 Lemma 5.2(a), uniform on the
compact closure of B_0, every block vector there having the first carrier as a robust peak).  (d) A design addition (Z0+): for the fixed
triple F_0 = {p, p', p''} in Z_0 the target family contains c/q*(c) for a countable dense set of directions c in R^{F_0}, each used infinitely
often in every block (same status as (Z0)).  Then a special with target c/q*(c) has B = 0 and A(b) = <c, Phi(b)>/q*(c).
Induction data at stage i >= 1: closed ball B_i, level L_i >= l_i, specials l_1 < ... < l_i, numbers eps_j > 0 (j < i), kappa_i > 0 with
 (J1) all assignments of carriers <= L_i are constant on B_i (hysteresis; specials and l_- have eps = +1);
 (J2) for j < i: g_j^{(L_i)} := 1 - nu_{l_j}/theta^{(L_i)} lies in [eps_j, Phi_{l_{j+1}}/2 - eps_j] on B_i, and 2 eta_{L_i}/theta_min < eps_j;
 (J3) n val_{l_-} in (-eta, -eta/2) with margin on B_i; 0 < -A_{l_j} < delta_{l_j} H_{l_j} on B_i (j <= i);
 (J4) G_i := g_i^{(L_i)} takes the values >= kappa_i and <= -kappa_i in int B_i, 2 eta_{L_i}/theta_min < kappa_i.
Step i -> i + 1.  Pick b^0 in int B_i with G_i(b^0) = 0 (IVT on a path between the two points of (J4)).  Pick c_{i+1} in the dense family
with <c_{i+1}, Phi(b^0)> close to 0 and tangential gradient independent of that of <c_i, Phi> at b^0; near b^0, x_1 := <c_i, Phi(b)>,
x_2 := <c_{i+1}, Phi(b)> are coordinates.  nu_{l_i} depends on x_1 only (slope ~ m/(n Phi_{l_i} q*)), nu_l for a carrier l with target
c_{i+1}/q* on x_2 only (slope ~ m/(n Phi_l q*)), theta is Lipschitz in (x_1, x_2) with an O(1) constant.  For such a carrier l > L_i (late),
the curve Gamma_l := {G_i = Phi_l/4} is a graph x_1 = phi_l(x_2) with |phi_l'| <= C Phi_{l_i}; along it, G^l := 1 - nu_l/theta equals 1 where
x_2 = -delta_l H_l q*(c_{i+1}) (val_l = 0) and is very negative a distance ~ delta_l H_l further: by the IVT there is b^# on Gamma_l with
G^l(b^#) = 0 and val_l(b^#) > 0, at distance O(delta_l H_l) from b^0 (inside int B_i for l large).  On this path only carriers in (L_i, l) can
switch; by (b) their hysteresis margins exceed the path's O(delta_l H_l) variation, so none switches.  Put l_{i+1} := l, choose
r := c Phi_{l_i} Phi_l and B_{i+1} := closed ball of radius r around b^#: G_i in [Phi_l/8, 3 Phi_l/8] on B_{i+1} (slope ~1/Phi_{l_i}, theta
variation O(r)), and G^l takes values +-kappa_{i+1}, kappa_{i+1} ~ c' Phi_{l_i}, in int B_{i+1} (slope ~1/Phi_l).  Then choose L_{i+1} >= l_{i+1}
with 2 eta_{L_{i+1}}/theta_min < min(Phi_l/16, kappa_{i+1}, eps_j (j < i)) and shrink nothing (hysteresis keeps (J1) on B_{i+1} for the new
carriers in (l, L_{i+1}] if B_{i+1} is small compared with their margins; otherwise shrink B_{i+1} around b^# keeping a crossing of G^l,
possible because the margins exceed C r).  (J1)-(J4) hold at stage i + 1 with eps_i := Phi_l/16.
Limit.  b^infty := intersection of the B_i; z := the (constant) assignments.  By (J2) and (c), every l_i has relative gap in
(0, Phi_{l_{i+1}}/2) at the final row; l_- and the robust peaks are as in V4; (a) of Theorem NT holds with "owner sign" replaced by
"aligned with n|val| >= (B + delta H)/2" (all that (b)-(e) use).  Why U3's version fails: it confines g_{i+1} to (gamma_{i+1}, 2 gamma_{i+1})
on B_{i+1}, so the next stage (which needs g_{i+1} < Phi_{l_{i+2}}/2 << gamma_{i+1}) has an empty region.

## F2. (Z0+) and Proposition NT-M(ii)'.  PROVED.
Assume (Z0+) and that every special has a target c/q*(c) supported in F (F1 produces such rows).  Then for every finite Omega in Q
containing k_-, every omega^+ supported in Omega, every Dom supported in Omega with eps_k Dom(k) >= 0 (k in Omega \ {k_-}),
Delta := d(Dom) < 0 and Dom(k_-) > Delta w(k_-), every chi : F^c -> [0,1] and every beta supported in F with (beta + chi v 1_{F^c})(zhat) = 0,
the pairs of U3 3.2(ii) are two-piece data.
Proof.  v = R^* Dom - Delta psi.  Omega-carriers (l_- and specials) have targets in F, hence touch F^c only on their own (pairwise
disjoint) signature sets.  (1) j in S_k, k in Omega: v(j) = lambda_k (Dom(k) - Delta w(k)) v_k(j) - Delta sum_{l > k} lambda_l w(l) u_l(j).  For a
special, eps_k w(k) > 0 and eps_k Dom(k) >= 0 give eps_k (Dom(k) - Delta w(k)) >= |Delta||w(k)| >= |Delta| M/2; for k_-, d(Dom) = Delta forces
Dom(k_-) >= |Delta| C/(Phi_{k_-}^2 |w(k_-)|) >> |Delta| (U3 3.2).  The later terms have moduli <= |Delta| 2^{-5} lambda_k v_k(j) (V4 Theorem 2.2
Step 6; coefficients |w| <= 1).  So z_j v(j) >= (1/4 - 2^{-5}) |Delta| lambda_k v_k(j) > 0 (z = eps_k on S_k).  (2) j notin F u union_{k in Omega} S_k:
R^* Dom(j) = 0 and v(j) = -Delta psi(j) is z_j-signed and non-zero by U3 3.2(i) (j notin S_{l_-}).  Hence v is z-signed and non-zero off F;
b^+ = chi v 1_{F^c} + beta is z-signed, b^- = (chi - 1) v 1_{F^c} + (beta - v 1_F) is (-z)-signed off F; there are no free coordinates.  Both pairs
represent g (b^+ - b^- = v = R^*(omega^- - omega^+) - Delta psi) and g(xi) = q_0 b^+(zhat) = 0.  QED
Corollary NT-R'.  Under (Z0+), every mate of f^infty with such data, kappa_w <= 1, Delta < 0, is in cl NA (V4 Theorem 5.6): (H1) as in U3;
E = union_{k in Omega} supp y_k \ F = {}; on S_k (k in Omega) the coefficient satisfies |gamma_k| >= lambda_k |Delta|/4 >= tau_k C_1 lambda_k once
tau_k <= 1/4, so V4 Lemma 4.1' gives 32-dominance there; on the finitely many remaining coordinates of E', D = v is non-zero by (1).
Without (Z0+) the statement holds for Omega = {k_-} (supp y* = F) by the same proof.

## F3. Lemma 3.5' (dead-zone bump).  PROVED.
Add the hypothesis Delta_new := Delta + eps_k kappa Phi_k^2 w(k)/C <= 0 (automatic for anti-type k, or for kappa <= |Delta| C/(Phi_k^2|w(k)|);
otherwise raise Dom(k_-) accordingly).  Then: the new coefficient of u_k is lambda_k eps_k kappa (1 - Phi_k^2 w(k)^2/C) (sign eps_k);
v_new = v + eps_k kappa lambda_k u_k - (Delta_new - Delta) psi is z-signed off F (on S_k by the allowedness-(b) estimate for kappa >= kappa_k,
elsewhere because v_new = -Delta_new psi + (unchanged Omega terms) with Delta_new <= 0); re-split by clamping b^+_new(j) := projection of
b^+(j) onto [0, v_new(j)] (z-oriented) at every j; then ||g' - g||_1 <= ||v_new - v||_1 <= kappa lambda_k + kappa Phi_k^2 |w(k)| ||psi||_1/C <= 2 kappa lambda_k.

## F4. Lemma QB2' (sharp bank accounting).  PROVED.
Let (b^+-, omega^+-) represent g at f (F finite), be side-admissible off a finite set E of contacts, and let f^b be the banked row.  In the
bounds of prop:onesidedupper / Lemma U / thm:engineered at f^b, the flip summand at j in E is at most
   (t^2/2) ((z_j b^+_j)_-)^2/|a^b_j|  (side +, t > 0),   (t^2/2) ((z_j b^-_j)_+)^2/|a^b_j|  (side -, t < 0),   (t^2/2) (b^theta_j)^2/|a^b_j|  (theta piece),
since the summand is 2(x - m)_+ with x = -sgn(a^b_j) t B_j, which vanishes for x <= 0 and is <= x_+^2/(2m).  Consequently, if at every j in E all
three pieces are bounded by the violation, max(|b^+_j|, |b^-_j|, |b^theta_j|) <= C_E e_j with e_j := (z_j b^+_j)_- + (z_j b^-_j)_+ (true for
fine-origin violations with the clamped split |b^+-_j| <= |v_j|), masses m_j := (C_E^2 q_0 epsilon/beta) e_j (epsilon := sum_E e_j) add at most
beta (1 + o(1)) to each Gamma_diamond, and p*(f^b - f) <= C_f m log(e/m), m := sum_E m_j = C_E^2 q_0 epsilon^2/beta.

## F5. (H3) by the symmetric split.  PROVED.
Given pairs representing g with v = b^+ - b^-, and a finite set J' of free coordinates in the window, put b~^+-_j := +-v_j/2 (j in J'),
b~^+- := b^+- elsewhere, and g~ := g - sum_{j in J'} b^theta_j e_j^* + c a (c chosen with g~(xi) = 0).  Then (b~^+-, omega^+-) represent g~,
b~^theta = 0 on J' (so (H3) of Lemma VT holds), b~^+_j b~^-_j <= 0 (U3's conversion criterion holds), viol~(j) = |v_j| <= |b^+_j| + |b^-_j| = viol(j),
and, since c = sum_{J'} b^theta_j zhat_j with |zhat_j| = |z_j| < 1 off F (diagonal U: e is supported in F) and ||a||_1 <= 1,
||g~ - g||_1 <= 2 sum_{J'} |b^theta_j| <= sum_{J'} viol(j) (|b^theta_j| <= (|b^+_j| + |b^-_j|)/2).  The pairs absorb c a on F (admissible there).
So the "OPEN sub-case" of U3 (S2d) is not an obstruction.

## F6. The theta/+- junction mismatch, and d-consistent engineered approximants.
(F6a) Estimate (PROVED from the proof of thm:engineered).  For diamond = +-, lin'_m = tau kappa^diamond_m + r_m <V^an_m - w'_m, R_m x'>/sigma'_m with
kappa^diamond_m = rho (d'_m - d_m)(omega^diamond_m - omega^theta_m) and, for omega vanishing on P_m u P'_m (proof of (E4)),
   (d'_m - d_m)(omega) = sum_k omega(k) [ (R_m xhat')(k)/|R_m xhat'|_m - (R^{**}_m zhat)(k)/|R^{**}_m zhat|_m ].
With the diagonal base the window masses change (R_m xhat')(k) at first order by lambda_k sum_{j in W} u_k(j) s_j^2 m_j z_j/nu'' (m_j = 4 rho s_1 |b^theta_j|),
so for window data (||b^theta||_1 ~ A_0/t, switching ||lambda(omega^- - omega^+)||_1 up to A_2/t) the bracket is of order s_1/t and
|kappa^diamond_m| ~ s_1/t^2, generically with equality up to constants.  Hence the constant K_sharp of Step 0 (which must dominate |lin'_m|/(|tau| s_1))
is of order t^{-2}, not O(1).  (Numerical check junction_check.py, N = 1 model, datum of vt_check scaled by 1/t, exact forced data of the
engineered approximant: kappa t^2/s_1 = 4.8203e-8 to five digits for t in {1, 0.3, 0.1, 0.03} and s_1 in {1e-4, 1e-5}; the small constant
reflects the model's tiny s_j^2 at the switching carrier's signature coordinates, the scaling is exact.)  At the junction |tau| = s_1 the
mismatch is ~ tau^2/t^2; enlarging the theta-regime enlarges the masses in
proportion (scale invariance), so the mismatch must be paid by rebalancing: cost iota |eps_m| with |eps_m| ~ |lin'_m|, i.e. iota <~ delta t^2, and
Lemma TV(a) needs |eps_m| Lambda <= gamma/2.  By lem:transferdata a transfer peak of inefficiency iota needs Phi(k_*) <~ iota (peak condition) and
Lambda = ell/lambda_{k_*}; at |tau| ~ s_1 one needs Phi(k_*) in [~ s_1^2/t^2, ~ delta t^2] with u_{k_*} within ~ t^2 of the f-dependent vector T/ell.
HEURISTIC consequence: for D_Omega-type ladders (one weight per window level) only O(1) carriers have weights in that range, with fixed
targets, so in general no such transfer peak exists and the bound of Lemma VT cannot hold uniformly with T_0 >= c_flat t.
Scope: F6a does NOT affect the refereed Theorem E (Z3), E^SC (V2), E'' (V1) or thm:engineered itself: they apply thm:engineered at a
FIXED row to FIXED exact data (non-uniformly; mate property at the row from Lemma U, where f' = f and there is no mismatch).  It affects
only routes that need the engineered bound uniformly in the window scale, i.e. U3's (S2) with violated data.
(F6b) Repair (SKETCH): d-consistent engineered approximants.  After placing the window masses, re-tune at f' the normalized values
(R_m xhat')(k)/|R_m xhat'|_m of the finitely many coarse omega-carriers k (all pieces of the window) exactly back to their values at the row, by
V1 Lemma TU levers (pulls and private banks at far signature coordinates of k; with the diagonal base each lever acts at first order only on
its own carrier; explicit contraction fixed point; the lever coordinates carry clamped data with one side zero and a theta-mass, so they cost
nothing at first order).  Then (d'_m - d_m)(omega) = 0 for EVERY omega supported on the tuned set, kappa^diamond_m = 0 for all pieces, lin'_m
reduces to r_m g_m = |tau| O(|Delta d_m| (Bx_m + S_m)) = |tau| O(s_1 T_lo^3/t^2 + s_1^2/t^3), K_sharp = O(1) with FIXED transfer data, and
U3's remaining scaling arithmetic (K_W, K_A, K_h, K_H = O(1/t), T_0 >= c_flat t) goes through under s_1 <= c delta t^3 (met by U3 (f):
s_1 = T_lo^8 c_l).  Not written line by line: the lever sizes against the data at lever coordinates, and the scrambled-set bound S_m <= c delta t s_1.

## F7. Bookkeeping of Proposition RT*(d),(f) with the true size of Delta.  PROVED (arithmetic).
At window scales |Delta| <= C D(l)/t (box bound |omega| <= 6/t, coarse Phi >= 1/D(l)).  Hence fine-origin mass eps <= C D(l) sum_{c>l} lambda_c/t:
<= C D(l) T_lo(l)^2 under (P2), <= C D(l) T_lo(l)^9 under (W10).  Bank cost eps^2/beta = o(T_lo^2) in both cases; (VT) with s_1 = T_lo(l)^8 c_l
needs c_l >= C' D(l) T_lo(l), true since log(1/c_l) ~ 10 log(1/T_lo(l-1)) << n^w_l <= log(1/T_lo(l)) (D(l) is fixed before n^w_l).
