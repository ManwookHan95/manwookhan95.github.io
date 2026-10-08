# Strategy C: primal second-order / multiscale analysis of mate fibres for Martín norms

Author: research agent C (strategy R5 of the briefing). Setting: canonical base, finite block set I
(single block I = {m} whenever convenient; by Preprint B, Remark martin-tail, finite I suffices for the
density problem). All spaces real.

## 0. Summary

### 0.1 What was asked
Decide whether NA((c_0,p), l_2^2) is dense in L((c_0,p), l_2^2). Strategy C: (1) transfer lemma comparing
the primal excess of an NA approximant f' (at its normer x' in c_0) with the excess of f (at its bidual
normer xi); (2) excess profiles near x' and xi, block by block; (3) use the freedom in x' (far
coordinates) to recover mates; single block first; or isolate the configuration where every x' loses
curvature on scales the slack cannot cover.

### 0.2 Main results (status in brackets)
Notation used here is fixed in Section 1.

* **[PROVED] Kernel-slice form of the mate fibre** (Lemma 2.1, 2.2). For f' attaining at x':
  g' in C(f') iff g'(x')=0 and g'(v)^2 <= phi'(v)(2+phi'(v)) for v in ker f', phi'(v) = p(x'+v)-1.
  Same at a non-attaining f with its bidual normer xi (phi(nu) = p**(xi+nu)-1 on ker f in X**).
* **[PROVED] Slack lemma / localisation** (Lemma 3.1, Cor. 3.2). With eps = p*(f-f') and
  g^ = g - g(x') f', on {phi' >= K eps} one has |g^(v)| <= (1+2/sqrt K) sqrt(phi'(2+phi')).
  Hence (f', rho g^) is contractive iff the mate inequality holds on the small region {phi' < K eps}.
* **[PROVED] Transfer lemmas** (Lemma 3.3 ray criterion; Lemma 3.4 comparison form; Lemma 3.5 pointwise
  lower semicontinuity of the excess along x'_n -> xi weak*; Lemma 3.6 Hessian necessary condition;
  Lemma 2.3 Hahn-Banach correction; Remark 2.4: corrections must be *relative*, additive errors fail
  on low-curvature directions).
* **[PROVED] Base excess profiles** (Section 4): exact flatness on free coordinates up to the room
  c(1-|z_j|); explicit dual-test lower bounds; outward-kink curvature 1/(2 c kappa_j) with
  kappa_j = ||P_{e perp} U^* e_j^*||^2/||U^* a|| (blows up for far j: "stiffness"); numerically confirmed.
* **[PROVED] Exact local formula for a block norm** (Lemma 5.1): near z, with peak set P, signs s,
  |y| = Lambda(S_P(y), ||D^{-1} y_Q||_2), Lambda(S,Y) = [S - sqrt(F2) sqrt(S^2-(1-F2)Y^2)]/(1-F2),
  F2 = sum_P Phi_k^2, valid under explicit sign/threshold conditions (two-sided). Verified to 1e-12.
  Corollaries: peak-overshoot upper bound (Lemma 5.2), single-coordinate Huber lower bound with
  curvature C/(|z| Phi_k^2) and slope = gap (Lemma 5.3). (The briefing's "1/(2C)" constant is not right;
  the correct quadratic coefficient in the primal variable y is m^2 C u_{k,m}(y)^2/(2|z|), |z| = block mass.)
* **[PROVED] Theorem A (mate fibres at tame NA points are finite certificates)** (Thm 6.2). If x' has
  finitely many strict non-peaks and degenerate peaks in every block and satisfies the margin-sparsity
  condition (MS), then C(f') is contained in the finite-dimensional space
  span{e_j^*: j not free} + span{u_{k,m}: k non-peak} + span{R_m^* w'_m}. Mechanism: the free base
  coordinates of x' act as slack variables which "absorb" block curvature (Remark 6.3). Numerically
  confirmed (3-dimensional exactly flat subspace in a finite model).
* **[PROVED] Theorem C (bidual analogue at tame non-attaining f)** (Thm 6.4) and **balance**
  (Prop. 6.5): at a tame f, every mate is a *balanced finite certificate* g = b + sum_m R_m^*(omega_m + c_m w_m)
  with b supported in supp a cup K (K = kinks), b(xi) = 0, omega_m finitely supported on strict non-peaks and
  degenerate peaks, v_m(R_m** xi) = 0 (c_m = -d_m when omega_m lives on strict non-peaks). Balance is forced by a
  second-order-flat "rebalancing direction" of the primal ball (Lemma 6.6).
* **[PROVED] Theorem B (recovery of natural finite certificates)** (Thm 7.1). If (f,g) is contractive and
  g is a balanced finite certificate with Gamma_max(g) := max(H_b, H_1,...,H_|I|) <= 1, then
  (f, rho g) is in the closure of NA for every rho<1, along canonical NA approximants (truncations of the base
  contact) that do not depend on g. This re-proves (and extends to base + several blocks) the black-box
  "finite local-certificate theorem" of [Check] used in Preprint A (for b = 0 at arbitrary a, Remark 7.1').
* **[PROVED] Theorem B' (rebalanced certificates, sharp second-order condition)** (Thm 7.4). The same holds under
  the weaker hypothesis Gamma_w(g) <= 1, where Gamma_w = q_0 H_b + sum_m sigma_m H_m is the mass-weighted average
  (q_0 = q**(xi), sigma_m = |R_m** xi|). Mechanism: lower *all* near-peak block coordinates uniformly by O(t^2) and
  fix the resulting non-absorbable vector with one deep **transfer peak** k_* whose functional u_{k_*}
  approximates the needed correction (exists by density of tails of (u_{k,m})_k; it is a robust peak, hence
  survives in every NA approximant). Numerically: explicit coefficient 0.392 -> 0.3005 -> Gamma_w = 0.298 as the
  transfer peak improves (Gamma_max = 2.86).
* **[PROVED] Second-order coefficient** (Prop. 8.1): Gamma_2^+(g) <= Gamma_w(g) for every balanced finite
  certificate (a in c_00), with equality when every block has finitely many non-peaks, no degenerate peaks and
  margin sparsity (lower bound via explicit test points in l_inf: an LP-optimal base decomposition, Lemma 5.1 for the
  blocks, and an exact block Legendre identity Lambda_SS = C c_Q/(|z| F2)). In finite-dimensional models the true
  coefficient can exceed Gamma_w (exactly flat rebalancing face, no transfer peaks): numerics 0.36 vs 0.298.
* **[PROVED] Theorem 8.4: tame supports are recoverable.** If f is tame (a in c_00, finitely many non-peaks per
  block, margin sparsity, no kinks, no degenerate peaks), then {f} x C(f) is contained in the closure of NA, i.e.
  every operator (f, rho g) with g in C(f) and rho < 1 is a limit of norm-attaining operators into l_2^2 (along
  canonical NA approximants). Tame non-attaining f exist under mild assumptions on T (Remark 6.8, SKETCH); they are
  meagre in the bidual face, so this is a positive result on a thin but nontrivial class.
* **[HEURISTIC/OPEN] The remaining obstruction is the generic, non-tame case** (Section 9): infinitely many
  non-peaks (Preprint A: generic), near-threshold peaks, kinks, a not in c_00. Mates are then "infinite
  certificates"; necessary decay of deep coefficients sum_{k>K}|c_k| = O(sqrt Phi_K) (SKETCH, under a
  quantitative independence hypothesis) versus the sufficient sum c_k^2/Phi_k < infinity of Preprint A leaves a
  **borderline regime** c_k ~ sqrt(Phi_k) that no known technique recovers; an engineered ("implanted") non-peak at
  depth k costs eps >~ Phi_k so its quadratic window (~Phi_k) lies below the slack scale (~sqrt Phi_k) it creates
  (HEURISTIC); near-threshold implants are free and are the natural tool. Far stiffness of xi (kinks, rooms -> 0) is
  harmless for fixed l_1 data (PROVED) and for the second-order coefficient of finite certificates (PROVED: the
  test points of Prop. 8.1 leave all coordinates off supp a fixed).
* **No counterexample** was found, and no complete density proof. Leaning: mildly positive (the second-order
  "rebalancing" obstruction suspected initially is removed by transfer peaks, and density holds along all tame
  supports; the remaining difficulty is the borderline deep regime of infinite certificates at generic supports,
  which depends on quantitative properties of Martín's T).

### 0.3 Errors/caveats found in the briefing or preprints
1. Briefing R5 block heuristic: the quadratic coefficient is m^2 C u_{k,m}(y)^2/(2|z|) with |z| = |R_m x|_m
   (block mass), not m^2 u^2/(2C); the linear slope is gap_k m Phi_m(k)|u_{k,m}(y)| (gap = M - |w(k)| for the
   favourable sign, M + |w(k)| for the other), not (gap/M)(...). (Lemma 5.3, verified numerically.)
2. Preprint A / [Check]: the condition "block quadratic coefficient <= 1" is sufficient but **not
   necessary** for a block certificate to be a mate: the sharp second-order quantity is the mass-weighted
   Gamma_w (Prop. 8.1), smaller than the block coefficient by the factor sigma_m when the base is unperturbed. So
   the finite local-certificate theorem, as stated, recovers only part of the finite-certificate mates;
   Theorem 7.4 recovers all of those with Gamma_w <= 1.
3. Preprint B, Lemma base-support-stability states "z in S_{c_0}"; for the normalised base contact
   z = x/q(x) - U(U^* f_0/||U^* f_0||) one has z in B_{c_0} with z_j = sign f_0(j) on supp f_0, so
   ||z||_inf = 1 indeed (f_0 != 0); fine. No error found there.
4. Preprint A, Thm weighted-recovery uses [Check] as a black box; Theorem 7.1 below supplies a proof of
   the needed statement (single block, base fixed; Remark 7.1' for a not in c_00), so that theorem no longer depends on [Check].

---

## 1. Setting, notation, standing facts

### 1.1 Norms
X = c_0, X* = l_1, X** = l_inf. U: H -> c_0 compact, dense range; B_q = B_{c_0} + U(B_H);
q*(a) = ||a||_1 + ||U^* a||_H. U^*: l_1 -> H is injective (dense range of U) and compact; hence
||U^* e_j^*||_H -> 0 (e_j^* -> 0 weak* and U^* is weak*-to-norm continuous on bounded sets).

Blocks m in I (finite). u_{k,m} in S_{q*} cap Y, Phi_m(k) = 2^{-m-k} q*(T e_{k,m}) in (0, 2^{-m-k}].
D_m = diag(Phi_m(k))_k. Block norm |.|_m on l_1 with unit ball B_{l_1} + D_m(B_{l_2}), dual norm
N_m(w) = ||w||_inf + ||D_m w||_2 on l_inf. (R_m x)(k) = m Phi_m(k) u_{k,m}(x).
p(x) = q(x) + sum_m |R_m x|_m; p**(eta) = q**(eta) + sum_m |R_m** eta|_m.
Dual ball: B_{p*} = B_{q*} + sum_m R_m^*(B_{N_m}); consequently, for h in l_1,

  (1.1)  p*(h) = min{ max( q*(A), max_m N_m(W_m) ) : h = A + sum_m R_m^* W_m }.

(Proof: the dual of a sum of seminorms has as unit ball the Minkowski sum of the polar balls; with
V* = (sum N_m)_inf, L^*(B_{V*}) = sum_m R_m^*(B_{N_m}); the minimum is attained by weak* compactness.)
Note sum_m Phi_m(k)^2 < 1, so in each block F2 := sum_{k in P} Phi_m(k)^2 < 1 for every P.

### 1.2 Bidual base ball
B_{q**} = B_{l_inf} + U(B_H) (weak*-closure of B_{c_0}+U(B_H); U(B_H) is norm compact, so the sum of
the weak*-compact B_{l_inf} and a norm-compact set is weak*-compact; it contains B_q and is contained in
its weak*-closure). Hence q**(eta) = min_h max(||eta - U h||_inf, ||h||) (attained).

### 1.3 Data at a point (used both for x' in c_0 and for xi in l_inf)
Let eta in l_inf \ {0} be a normer of some f in S_{p*} (eta = x' in c_0 for NA f', or eta = xi).
Forced decomposition (Preprint A): f = a + sum_m R_m^* w_m, q*(a) = 1, a(eta) = q**(eta) =: c (written q_0
when eta = xi), w_m = J_m(R_m** eta) (unique; |.|_m is smooth because N_m is strictly convex),
sigma_m := |R_m** eta|_m, c + sum_m sigma_m = 1.
* Base contact: eta/c = z + U e with e := U^* a/||U^* a||_H, z in B_{l_inf}, z_j = sign a_j on F := supp a.
  (Proof: eta/c in B_{q**}; write eta/c = z + U h, ||z||_inf <= 1, ||h|| <= 1; then
  1 = a(eta/c) = a(z) + <U^* a, h> <= ||a||_1 + ||U^* a|| = 1 forces a(z) = ||a||_1 and h = e.)
* Free coordinates J := {j not in F : |z_j| < 1}; kinks K := {j not in F : |z_j| = 1}; room r_j := 1 - |z_j|.
  For eta = x' in c_0: z in c_0 (z = x'/c - U e), so K is finite and inf_{j in J} r_j > 0.
  For eta = x' in c_0 also a in c_00: a = grad q(x') attains q at x', NA(q) = c_00 (Preprint A/B).
* Block m data (drop m): z := R** eta in l_1 (here z denotes the block vector; context disambiguates),
  w = J(z), M := ||w||_inf, C := ||D w||_2, M + C = 1, C > 0, M > 0. Block-threshold (Preprint B):
  z/|z| = alpha + D D w / C with alpha in B_{l_1}, ||alpha||_1 = 1, supp alpha in P := {k : |w_k| = M},
  sign alpha_k = s_k := sign w_k on supp alpha. Off P: w_k = C z_k/(|z| Phi_k^2).
  Strict non-peaks Q := {k : |w_k| < M}; degenerate peaks Dg := {k in P : alpha_k = 0};
  non-degenerate peaks P° := P \ Dg.
  Threshold constant theta := |z| M/(m C). For k in P: |z_k| = |z|(|alpha_k| + Phi_k^2 M/C), i.e.
  |z||alpha_k| = m Phi_k mu_k with the **margin** mu_k := |u_k(eta)| - theta Phi_k >= 0 (= 0 iff k in Dg).
  For k in Q: |u_k(eta)| < theta Phi_k ... more precisely |w_k| = (M/theta)|u_k(eta)|/Phi_k < M.
  Gap of k in Q: gamma_k := M - |w_k| > 0.

### 1.4 Standing facts
(F1) p** is strictly convex (Preprint A, [Recovery]; Preprint B Thm finite-blocks (b) for p_J). Hence every
f in S_{p*} has a unique normer xi in S_{p**}.
(F2) If f_n -> f in S_{p*} and eta_n in B_{p**} with f_n(eta_n) -> 1, then eta_n -> xi weak*.
(Any weak* cluster point eta satisfies f(eta) = 1 since |f(eta_n) - f_n(eta_n)| <= p*(f - f_n); uniqueness
of the normer and weak*-metrisability of B_{p**} on the separable X give the claim.)
(F3) R_m: c_0 -> l_1 is compact, so R_m** is weak*-to-norm continuous on bounded sets. If eta_n -> eta
weak* (bounded) then R_m** eta_n -> R_m** eta in l_1.
(F4) If z_n -> z != 0 in l_1 then J(z_n) -> J(z) weak*, ||D(J(z_n) - J(z))||_2 -> 0, M_n -> M, C_n -> C,
and ||R^*(J(z_n) - J(z))||_1 -> 0.
Proof. J(z_n) is bounded (N = 1). A weak* cluster point w~ has N(w~) <= 1 (N is weak* lsc) and
w~(z) = lim J(z_n)(z_n) = lim |z_n| = |z|, so w~ = J(z) by uniqueness. Coordinatewise convergence of a
bounded sequence plus sum Phi_k^2 < infinity gives ||D(J(z_n)-J(z))||_2 -> 0 by dominated convergence, so
C_n -> C and M_n = 1 - C_n -> M. Finally ||R^*(w_n - w)||_1 <= sum_k m Phi_k |w_n(k) - w(k)| q*(u_k)... -> 0
by dominated convergence (sum Phi_k < infinity, |w_n - w| <= 2). (q*(u_k) = 1 and ||.||_1 <= q*.)
(F5) R^*: l_inf -> l_1 is injective and R^*(l_inf) is contained in Y; Y cap c_00 = {0}; T is injective.
Consequence used repeatedly ("independence lemma"): if F_0 is finite and the functionals
u_{k,m} (k in Q_m finite), pi_m := R_m^*(s 1_{P_m})-type infinite combinations, and e_j^* (j in F_0) satisfy a
linear relation sum c_{k,m} u_{k,m} + sum d_m pi_m + sum_{j in F_0} b_j e_j^* = 0, or merely
sum c_{k,m} u_{k,m} + sum d_m pi_m vanishes on a cofinite set of coordinates, then all coefficients vanish.
(The combination is in Y; if it vanishes off a finite set it is in Y cap c_00 = {0}; injectivity of T on
l_1(N x N) then kills the T-coefficients, which are (multiples of) c_{k,m} and d_m s_k m 2^{-m-k}.)

### 1.5 Mates, slack, reductions
C(f) = {g : f(y)^2 + g(y)^2 <= p(y)^2 for all y in X}. Equivalently p*(f + t g) <= sqrt(1+t^2) for all t.
(R1) of the briefing (verified): density <=> for all f in S_{p*}, g in C(f), rho in (0,1):
(f, rho g) in cl NA. For an NA point f' (normer x'), every g' in C(f') gives an NA operator (f', g')
(it attains at x'). Throughout, "recoverable" means (f, rho g) in cl NA((c_0,p), l_2^2) for every rho<1.

---

## 2. Mate fibres in primal form

**Lemma 2.1 (kernel slice at an NA point). [PROVED]** Let f' in S_{p*} attain its norm at x' in S_p and put
phi'(v) := p(x'+v) - 1 for v in ker f'. Then phi' is convex, phi' >= 0, phi'(0) = 0, and for g' in X*:
(f', g') is contractive iff g'(x') = 0 and g'(v)^2 <= phi'(v)(2 + phi'(v)) for all v in ker f'.

Proof. phi' >= 0 because p(x'+v) >= f'(x'+v) = 1. (=>) y = x' gives g'(x')^2 <= 1 - 1 = 0. For v in ker f'
and y = x'+v: f'(y) = 1, so g'(v)^2 = g'(y)^2 <= p(y)^2 - 1 = phi'(v)(2+phi'(v)).
(<=) Let y in X. If lambda := f'(y) != 0, write y = lambda(x' + v) with v = y/lambda - x' in ker f'; then
g'(y)^2 = lambda^2 g'(v)^2 <= lambda^2((1+phi'(v))^2 - 1) = p(y)^2 - f'(y)^2. If f'(y) = 0, then sy in ker f'
for s > 0 and s^2 g'(y)^2 <= (1 + phi'(sy))^2 - 1 <= (1 + s p(y))^2 - 1 (since p(x'+sy) <= 1 + s p(y));
divide by s^2 and let s -> infinity: g'(y)^2 <= p(y)^2. []

**Lemma 2.2 (bidual slice). [PROVED]** Let f in S_{p*} with normer xi in S_{p**} and put
phi(nu) := p**(xi + nu) - 1 for nu in ker f := {nu in X** : nu(f) = 0}. Then g in C(f) iff xi(g) = 0 and
nu(g)^2 <= phi(nu)(2 + phi(nu)) for all nu in ker f.

Proof. First, g in C(f) iff eta(f)^2 + eta(g)^2 <= p**(eta)^2 for all eta in X**: given eta, Goldstine gives a
net y_a in X with p(y_a) <= p**(eta) and y_a -> eta weak*; then f(y_a) -> eta(f), g(y_a) -> eta(g), and
eta(f)^2 + eta(g)^2 = lim (f(y_a)^2 + g(y_a)^2) <= p**(eta)^2. The converse is trivial. Now repeat the proof of
Lemma 2.1 in X** with x' replaced by xi (p** is a norm on X** and p**(xi) = xi(f) = 1). []

**Lemma 2.3 (support function and Hahn-Banach correction). [PROVED]** Let f' in S_{p*} and let
r_{f'} := sqrt(p^2 - f'^2) on X, r~_{f'} := its largest sublinear minorant (convex envelope). Then
C(f') = {g : g <= r~_{f'}}, the support function of C(f') at x in X is r~_{f'}(x), and for l in X*, eta >= 0:
dist_{p*}(l, C(f')) <= eta iff l(x) <= r~_{f'}(x) + eta p(x) for all x in X.

Proof. A linear g satisfies |g| <= r_{f'} iff g <= r_{f'} (r_{f'} is even) iff g <= r~_{f'}. r~_{f'} <= p is a
finite convex function, hence continuous, and C(f') is weak* compact convex; the bipolar theorem in the
pair (X*, weak*) - X gives the support function. C(f') + eta B_{p*} is weak* compact convex with support
function r~ + eta p, and l belongs to it iff l <= r~ + eta p (Hahn-Banach separation by elements of X). []

**Remark 2.4 (corrections must be relative). [relative version PROVED; failure of additive corrections HEURISTIC (mechanism explained, no explicit counterexample constructed)]** Suppose l(x') = 0 and
|l(v)| <= R'(v) + eta p(v) for all v in ker f', where R'(v) := sqrt(phi'(v)(2+phi'(v))). This does **not**
imply dist(l, C(f')) = O(eta). Indeed in a decomposition x = sum_i lambda_i(x' + v_i) the errors add up to
eta sum |lambda_i| p(v_i), which is not controlled by p(x) when sum_i lambda_i = 0 ("two-point combinations"
(x'+v) - (x'+v'), whose cost R'(v) + R'(v') can be arbitrarily small compared to p(v - v') along low-curvature
directions). What does hold trivially: if |l(v)| <= (1+eta) R'(v) for all v in ker f' and l(x') = 0, then
l/(1+eta) in C(f') (Lemma 2.1). Hence every transfer argument must produce *relative* bounds on the small
region, and "low-curvature directions" at x' (where R'(v) << p(v)) are exactly where all difficulties sit.
