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

---

## 3. The transfer lemma

Standing notation for this section: f in S_{p*} with normer xi, g in C(f); f' in S_{p*} attaining its norm at
x' in S_p; eps := p*(f - f') <= 1; delta_0 := 1 - f(x') in [0, eps]; e := f - f' (so f = f' + e on X,
|e(y)| <= eps p(y)); g^ := g - g(x') f' (so g^(x') = 0 and p*(g^ - g) = |g(x')|).

**Lemma 3.0. [PROVED]** |g(x')| <= sqrt(2 eps).
Proof. (f,g) contractive at x': g(x')^2 <= 1 - f(x')^2 <= 1 - (1-eps)^2 <= 2 eps (f(x') >= 1 - eps). []

**Lemma 3.1 (slack lemma). [PROVED]** For every K >= 1 and every v in ker f' with phi'(v) >= K eps,

  |g^(v)| <= (1 + 2/sqrt K) sqrt( phi'(v)(2 + phi'(v)) ).

Proof. Put Phi := phi'(v), y := x' + v, so p(y) = 1 + Phi, f'(y) = 1, f(y) = 1 + e(y), |e(y)| <= eps(1+Phi).
Since (f,g) is contractive, g(y)^2 <= (1+Phi)^2 - (1 + e(y))^2 <= (1+Phi)^2 - 1 + 2|e(y)|
<= Phi(2+Phi) + 2 eps (1+Phi). As v in ker f', g^(v) = g(v) = g(y) - g(x'). With eps <= Phi/K:
2 eps(1+Phi) <= (2/K) Phi(1+Phi) <= (2/K) Phi(2+Phi) and, by Lemma 3.0, |g(x')| <= sqrt(2 eps) <= sqrt(2 Phi/K)
<= sqrt(Phi(2+Phi))/sqrt K. Therefore |g^(v)| <= sqrt(Phi(2+Phi)) (sqrt(1+2/K) + 1/sqrt K)
<= (1 + 2/sqrt K) sqrt(Phi(2+Phi)). []

**Corollary 3.2 (localisation). [PROVED]** Let rho_K := (1 + 2/sqrt K)^{-1} and 0 < rho <= rho_K. Then
(f', rho g^) is contractive (hence NA) iff rho^2 g^(v)^2 <= phi'(v)(2+phi'(v)) for all v in the *small region*
S'(K eps) := {v in ker f' : phi'(v) < K eps}. Moreover p*(rho g^ - rho g) <= sqrt(2 eps).
Proof. Lemma 2.1 (g^(x') = 0) plus Lemma 3.1 outside S'(K eps), and Lemma 3.0. []

Interpretation. Write v = t v^ with v^ normalised; the condition "phi'(v) < K eps" means: v lies below the
slack scale in its own direction. For a direction with quadratic curvature kappa, the slack covers
|t| >~ sqrt(K eps/kappa); in low-curvature directions the small region is long.

**Lemma 3.3 (ray criterion). [PROVED]** Let lambda >= 1 and rho <= rho_K. Suppose that for every
v in S'(K eps) there is s >= 1 with phi'(s v) >= K eps and
phi'(s v)(2 + phi'(s v)) <= lambda^2 s^2 phi'(v)(2+phi'(v)). Then (f', (rho/lambda) g^) is contractive.
If, along every ray, s -> phi'(s v)/s^2 is non-increasing on [1, infinity) ("subquadratic profile"), the
hypothesis holds with lambda^2 = 1 + K eps/2.

Proof. rho^2 g^(v)^2 = rho^2 g^(sv)^2/s^2 <= phi'(sv)(2+phi'(sv))/s^2 <= lambda^2 phi'(v)(2+phi'(v)) by Lemma 3.1.
For the second statement take s minimal with phi'(sv) = K eps (phi' is convex, continuous, phi'(0)=0,
phi'(sv) -> infinity); then phi'(sv)/s^2 <= phi'(v) and 2 + K eps <= (1 + K eps/2)(2 + phi'(v)). []

Superquadratic portions of profiles (flat pieces followed by growth) are exactly what violates Lemma 3.3. They
come from faces: base rooms (Lemma 4.2), peak simplices (Lemma 5.2) and their delays.

**Lemma 3.4 (comparison form). [PROVED]** Let T: ker f' -> ker f (in X**), T v := v - f(v) xi. If
phi'(v)(2+phi'(v)) >= kappa^2 phi(Tv)(2 + phi(Tv)) for all v in S'(K eps), then (f', rho g^) is contractive for
rho <= min(kappa, rho_K).
Proof. For v in ker f': g^(v) = g(v) = g(Tv) (as xi(g) = 0), and g(Tv)^2 <= phi(Tv)(2+phi(Tv)) by Lemma 2.2. []

**Lemma 3.5 (pointwise lower semicontinuity of the excess). [PROVED]** Let f'_n in NA cap S_{p*}, f'_n -> f,
with normers x'_n. Then x'_n -> xi weak*, and for every v in X, with v_n := v - f'_n(v) x'_n in ker f'_n,

  liminf_n phi'_n(v_n) >= phi(v - f(v) xi).

Proof. (F2) gives x'_n -> xi weak*. x'_n + v_n = (1 - f'_n(v)) x'_n + v -> (1 - f(v)) xi + v = xi + T v weak*,
and p** is weak* lower semicontinuous. []

So for each **fixed** v the excess at x'_n eventually dominates the excess at xi. Lemma 3.4 needs this on
the whole small region S'_n(K eps_n), i.e. on scales that shrink with eps_n. This **uniformity across
scales** is the entire difficulty (HEURISTIC summary, made precise in Sections 6-9).

**Lemma 3.6 (Hessian necessary condition). [PROVED]** If g' in C(f') then for all v in ker f':
g'(v)^2 <= 2 liminf_{t -> 0+} phi'(tv)/t^2. In particular g' vanishes on {v : phi'(tv) = o(t^2)}. The same
holds at xi for g in C(f) (Lemma 2.2), and also with "v in ker f'" replaced by "any v in X" provided one
uses the excess Delta'(x'+tv) := p(x'+tv) - f'(x'+tv) (Lemma 6.1 below).
Proof. From Lemma 2.1, t^2 g'(v)^2 <= phi'(tv)(2 + phi'(tv)); divide by t^2. []

**Remark 3.7 (what the slack really covers). [HEURISTIC]** In a direction where, at scale t, the
excess at x' behaves like kappa(t) t^2/2, the slack covers t >= sqrt(2 K eps/kappa(t)). Below that scale the mate
condition at f' must come from the local geometry of p at x'. Section 5 shows that a block coordinate k
contributes quadratically (coefficient ~ m^2 C u_k(v)^2/|z|) only for |t| <~ W_k ~ gap_k |z| Phi_k/(C m |u_k(v)|)
and linearly (slope gap_k m Phi_k |u_k(v)|) beyond. Hence, at scale t, coordinates with Phi_k >~ t are in the
quadratic regime and those with Phi_k <~ t contribute linearly, the latter summing to O(t^2) (geometric Phi):
every depth matters at its own scale. If x' reproduces the structure of xi only down to depth K (which is
what norm-closeness f' ~ f can enforce, with eps >~ Phi_K), then scales t <~ Phi_K are not reproduced while
the slack only covers t >~ sqrt(eps) >~ sqrt(Phi_K) >> Phi_K. This is the scale gap of the briefing (R5).

---

## 4. Excess profiles of the base

Throughout, eta in {x', xi} with base data (a, F, c, z, e, J, K, r_j) as in 1.3. The base excess is
E_q(nu) := q**(eta + nu) - c - a(nu) >= 0 (q** = q on X).

**Lemma 4.1 (exact flatness on free coordinates). [PROVED]** Let nu in l_inf with supp nu contained in J and
|nu_j| <= c r_j for all j. Then q**(eta + nu) = c, i.e. E_q(nu) = 0 (and a(nu) = 0).
Proof. eta + nu = c( (z + nu/c) + U e ) and |z_j + nu_j/c| <= |z_j| + r_j = 1 on J, z unchanged off J; so
eta + nu in c B_{q**} (1.2), q**(eta+nu) <= c; and q**(eta+nu) >= a(eta+nu) = c since supp a = F is disjoint from J. []

For eta = x' in c_0 the room is uniformly positive on J (z in c_0), so every v in c_0 supported in J is
exactly flat for |t| <= c r/||v||_inf, r := min_J r_j > 0. At xi, uniform room may fail (|z_j| -> 1).

**Lemma 4.2 (dual-test lower bound). [PROVED]** For every beta in l_1 with q*(a+beta) > 0 and every nu:
  q**(eta + nu) >= (a + beta)(eta + nu)/q*(a+beta), where q*(a+beta) = ||a+beta||_1 + ||U^*a + U^* beta||_H.
Trivial (definition of q** as a sup over B_{q*}). The useful choices:

(a) **Outward kink.** j in K, sigma := z_j, beta = s sigma e_j^* (s > 0). Then
q*(a+beta) = 1 + s chi_j + ||U^*a + s sigma U^* e_j^*|| - ||U^*a|| - s sigma <e, U^* e_j^*> where
chi_j := 1 + sigma (Ue)_j = sigma eta_j/c, and the Hilbert remainder is <= (s^2 kappa_j/2)(1 + O(s)) with
kappa_j := ||P_{e perp} U^* e_j^*||^2/||U^* a|| (exact Hilbert-norm identity, see (7.2) below).
(a+beta)(eta + t e_j) = c(1 + s chi_j) + s sigma t. Hence for sigma t > 0:
  E_q(t e_j) >= sup_{s>0} [ s|t| - c s^2 kappa_j (1+O(s))/2 ] / (1 + s chi_j + O(s^2))  =  t^2/(2 c kappa_j) (1 + O(|t|/kappa_j)),
the optimal s being ~ |t|/(c kappa_j); so the quadratic regime is |t| <~ c kappa_j (beyond it the bound is linear).
Since kappa_j -> 0 as j -> infinity (U^* compact), **far kinks are extremely stiff outward**; inward
(sigma t < 0) the coordinate is exactly flat for |t| <= 2c (Lemma 4.1 does not apply verbatim since j is not in
J, but the same proof works: |z_j + t/c| <= 1).

(b) **Support coordinate, inward and outward.** j in F, sigma := sign a_j, beta = s sigma e_j^* with
-|a_j| < s. Same computation with chi_j = 1 + sigma (Ue)_j = sigma eta_j/c:
outward (sigma t > 0): E_q(t e_j) >= (1 - |a_j| chi_j)^2 t^2/(2 c kappa_j) (1 + O(|t|/kappa_j)) when kappa_j > 0;
inward (sigma t < 0): E_q(t e_j) <= |a_j||t| for |t| <= 2c (eta + t e_j stays in c B_{q**}), and a
quadratic lower bound comes from moving the dual onto a kink i in K (sigma_i := z_i, chi_i := sigma_i eta_i/c):
with beta = s sigma_i e_i^*, s > 0, q*(a+beta) <= 1 + s chi_i + s^2 kappa_i/2 and
(a+beta)(eta + t e_j) = c(1 + s chi_i) + t a_j, whence
  E_q(t e_j) >= sup_{s>0} [ s |t| |a_j| chi_i - (c + t a_j) s^2 kappa_i/2 ] / (1 + s chi_i + s^2 kappa_i/2)
            = (t a_j chi_i)^2/(2 c kappa_i) (1 + O(|t|/kappa_i))      whenever t a_j < 0 and chi_i > 0.
(The dual "rebalances" onto the kink at zero first-order cost.) If |F| = 1 and K is empty, these tests give
no quadratic lower bound in the inward direction of the only support coordinate (its Hilbert direction is
radial).

(c) **Free coordinate beyond its room.** j in J, sigma t > 0, |t| > c(1 - sigma z_j): with beta = s sigma e_j^*:
E_q(t e_j) >= (|t| - c(1 - sigma z_j))_+^2/(2 c kappa_j)(1 + O(|t|/kappa_j)) (delayed quadratic).

Proof of (a)-(c): insert the indicated beta into Lemma 4.2 and expand; the only nonlinear term is the Hilbert
norm, handled by the exact identity (7.2); the error terms come from the denominators and from s ~ |t|/kappa. []

**Numerical confirmation** (C_work/base_profiles.py, n=5, d=3, F={0}, kink at 1, free coordinate z_2 = 0.3):
free coordinate flat on [-0.8, 0.4] (rooms 1.3 and 0.7), positive outside; kink: inward exactly 0, outward
E/t^2 = 0.3214 at t = 0.01 vs predicted 1/(2 c kappa_1) = 1/(2 x 1.554) = 0.3218; support coordinate with
|F| = 1: outward exactly flat (kappa_0 = 0: radial), inward E/t^2 = 0.31 at small t (curvature supplied by the
kink, as in (b)).

**Remark 4.3 (stiffness and its harmlessness for l_1 data). [PROVED for fixed finite data]** At xi the set K
of kinks may be infinite (z in l_inf), giving huge outward curvature in far coordinates; at x' in c_0 there are
only finitely many kinks and the far coordinates are free with room ~ 1. Any *fixed* finitely supported
transfer vector or any fixed l_1 vector beta sees the difference only through
sum_{j > N} (|beta_j| - z'_j beta_j) - (|beta_j| - z_j beta_j) <= 2 ||beta|_{(N,inf)}||_1 -> 0
as the agreement region [1,N] of z' and z grows. So far stiffness can only matter through objects that are not
tail-small in l_1 (block structure at all depths, or vectors whose support moves to infinity).

---

## 5. Excess profiles of a block

Fix one block and drop m. Phi = (Phi_k) positive with sum Phi_k^2 < 1, D = diag(Phi), |.| = gauge of
B := B_{l_1} + D(B_{l_2}) on l_1, N(v) = ||v||_inf + ||D v||_2 its dual norm on l_inf. Block excess at z != 0:
E(delta) := |z + delta| - |z| - w(delta) >= 0, w := J(z). Data (P, Q, Dg, P°, s, alpha, M, C) as in 1.3.

### 5.1 The two-variable formula

**Lemma 5.1 (exact local formula). [PROVED]** Let y in l_1, P a nonempty set of indices, Q its complement,
s in {+1,-1}^P. Put S := sum_{k in P} s_k y_k, Y := (sum_{k in Q} y_k^2/Phi_k^2)^{1/2} in [0, infinity],
F2 := sum_{k in P} Phi_k^2 in (0,1). Assume 0 < S < infinity and Y <= S. Define

  Lambda(S,Y) := [ S - sqrt(F2) sqrt(S^2 - (1-F2) Y^2) ] / (1 - F2),   lambda := Lambda(S,Y),
  rho_0 := (S/lambda - 1)/F2.

Then lambda > 0, rho_0 >= 0 and (S/lambda - 1)^2/F2 + Y^2/lambda^2 = 1. Moreover:
(a) if s_k y_k >= lambda rho_0 Phi_k^2 for every k in P, then |y| <= lambda;
(b) if |y_k| <= lambda rho_0 Phi_k^2 for every k in Q, then |y| >= lambda, attained by the dual vector
    w_k = M s_k (k in P), w_k = C y_k/(lambda Phi_k^2) (k in Q), M = rho_0/(1+rho_0), C = 1/(1+rho_0),
    for which N(w) = 1 and w(y) = lambda;
(c) if (a) and (b) hold, then |y| = Lambda(S_P(y), ||D^{-1} y_Q||_2) and J(y) = w.

Proof. Delta := S^2 - (1-F2)Y^2 >= F2 S^2 > 0 because Y <= S. The roots of
(1-F2) l^2 - 2 S l + (S^2 + F2 Y^2) = 0 are [S +- sqrt(F2 Delta)]/(1-F2); lambda is the smaller one, and this
equation is equivalent to (S - l)^2 + F2 Y^2 = F2 l^2, i.e. (S/l - 1)^2/F2 + Y^2/l^2 = 1. lambda > 0 since
sqrt(F2 Delta) <= sqrt(F2) S < S. rho_0 >= 0 iff lambda <= S iff S F2 <= sqrt(F2 Delta) iff F2 S^2 <= Delta
iff Y <= S.
(a) Define h in l_2 by h_k := rho_0 Phi_k s_k (k in P), h_k := y_k/(lambda Phi_k) (k in Q). Then
||h||_2^2 = rho_0^2 F2 + Y^2/lambda^2 = 1. Put alpha := y/lambda - D h: alpha_k = 0 on Q and
alpha_k = y_k/lambda - rho_0 Phi_k^2 s_k on P. Under (a), s_k alpha_k >= 0, so
||alpha||_1 = sum_P s_k alpha_k = S/lambda - rho_0 F2 = 1. Thus y/lambda = alpha + D h in B.
(b) ||w||_inf = M since |w_k| = C|y_k|/(lambda Phi_k^2) <= C rho_0 = M on Q. ||D w||_2^2 = M^2 F2 + C^2 Y^2/lambda^2
= C^2(rho_0^2 F2 + Y^2/lambda^2) = C^2, so N(w) = M + C = 1. Using S/lambda = 1 + rho_0 F2 and
Y^2/lambda^2 = 1 - rho_0^2 F2: w(y) = M S + C Y^2/lambda = C lambda (rho_0(1 + rho_0 F2) + 1 - rho_0^2 F2) = C lambda(1+rho_0) = lambda.
Hence |y| >= w(y)/N(w) = lambda.
(c) Both bounds; w attains, and the norming functional of y is unique (|.| is smooth). []

Consistency with the block-threshold lemma: at z with its own (P, s), (a) and (b) hold (alpha is the l_1 part,
h = D w/C), so the lemma reproduces |z|; one checks dLambda/dS = M and dLambda/dY = C Y/lambda.
**Numerical verification** (C_work/lam_check.py, six random instances, n = 6): |y| from an exact
peak-enumeration solver and Lambda agree to 12 digits; dLambda/dS = M and dLambda/dY = C Y/|y| to 6 digits.

Consequences. (i) Near z, as long as (a)-(b) persist, |.| depends on y only through the two numbers
(S_P(y), ||D^{-1} y_Q||): the peak coordinates enter only through their signed sum (the **peak simplex is
exactly flat**), the non-peaks through a Hilbert norm. (ii) If Q is empty (no non-peaks), Lambda(S,0) =
S/(1 + sqrt F2) is linear: the block is locally *affine*, all its curvature comes from structure changes
(peaks crossing the threshold). (iii) Second order (structure-preserving delta, Y > 0): with
h_0 := D^{-1} z_Q, sigma_1 := S_P(delta), sigma_2 := <h_0/Y, D^{-1} delta_Q>,

  E(delta) = (C/(2|z|)) ||P_{h_0 perp} D^{-1} delta_Q||^2 + (Lambda_SS/(2 Y^2)) (Y sigma_1 - S sigma_2)^2 + O(|.|^3),

because Lambda is 1-homogeneous (its Hessian is Lambda_SS/Y^2 times (Y,-S) tensor (Y,-S)) and
dLambda/dY = C Y/|z| multiplies the Hilbert excess ||h_0 + D^{-1}delta_Q|| - Y - sigma_2 = ||P_perp D^{-1}delta_Q||^2/(2Y) + O(.).

### 5.2 Upper bound by peak overshoots

**Lemma 5.2 (overshoot bound). [PROVED]** Let delta = mu z + delta' with mu > -1, delta' supported in P and
sum_{k in P} s_k delta'_k = 0. Then

  E(delta) <= 2 sum_{k in P} ( -s_k delta'_k - (1+mu)|z||alpha_k| )_+ <= 2 sum_{k in P} ( |delta'_k| - (1+mu)|z||alpha_k| )_+.

Proof. For a with s a = |a| (s = +-1) and any d: |a + d| = |a| + s d + 2(-s d - |a|)_+. Write
z + delta = [(1+mu)|z| alpha + delta'] + (1+mu)|z| D(Dw/C). The first bracket has l_1 norm
sum_P |(1+mu)|z|alpha_k + delta'_k| = (1+mu)|z| + sum_P s_k delta'_k + 2 sum_P(-s_k delta'_k - (1+mu)|z||alpha_k|)_+
= (1+mu)|z| + 2 ov; the second is (1+mu)|z| times an element of D(B_{l_2}). Hence
|z + delta| <= (1+mu)|z| + 2 ov, while w(delta) = mu|z| + M sum_P s_k delta'_k = mu|z|. []

In the Martín block: |z||alpha_k| = m Phi_k mu_k with the margin mu_k = |u_k(eta)| - theta Phi_k (1.3). For a
primal direction v with R v supported in P° (i.e. u_k(v) = 0 on Q and Dg) and zero peak sum,

  (5.1)  E(t R v) <= 2 m sum_{k in P°} Phi_k ( |t||u_k(v)| - mu_k )_+ <= 2 m |t| q(v) sum_{k in P°: mu_k < |t| q(v)} Phi_k .

### 5.3 Lower bounds

**Lemma 5.3 (single-coordinate Huber bound). [PROVED]** Let k in Q and sigma real with |w_k + sigma| <= M.
Put X := sigma Phi_k^2 w_k/C, Y_s := sigma^2 Phi_k^2/(2C). For delta in l_1 with |z|(1+X) + w(delta) + sigma delta_k >= 0:

  E(delta) >= [ sigma delta_k - |z| Y_s - (X + Y_s) w(delta) ] / (1 + X + Y_s).

Proof. N(w + sigma e_k) = M + (C^2 + 2 sigma Phi_k^2 w_k + sigma^2 Phi_k^2)^{1/2} <= 1 + X + Y_s
(using sqrt(C^2+u) <= C + u/(2C)), and (w + sigma e_k)(z) = |z| + sigma z_k = |z|(1 + X) because
z_k = |z| Phi_k^2 w_k/C on Q. Then |z + delta| >= (w + sigma e_k)(z + delta)/N(w + sigma e_k). []

Optimising sigma when w(delta) = 0: E(delta) >= H_k(delta_k)/(1 + O(Phi_k^2)) with the Huber function
H_k(d) = C d^2/(2|z| Phi_k^2) for |d| <= gamma^{+-}|z|Phi_k^2/C, and gamma^{+-}|d| - |z|(gamma^{+-})^2 Phi_k^2/(2C) beyond,
where gamma^+ = M - w_k (for d > 0), gamma^- = M + w_k (for d < 0). In the primal variable, delta_k = t m Phi_k u_k(v):
quadratic coefficient t^2 m^2 C u_k(v)^2/(2|z|), linear slope gamma m Phi_k |u_k(v)|, transition at
|t| = W_k := gamma |z| Phi_k/(C m |u_k(v)|).

**Lemma 5.4 (sign-flip bound). [PROVED]** For every set A of indices, N(w - 2 sum_{k in A} w_k e_k) = 1.
Consequently, for all delta in l_1,

  E(delta) >= 2 sum_k |w_k| ( -s_k delta_k - |z_k| )_+ ,  s_k := sign z_k = sign w_k.

Proof. Flipping signs of coordinates changes neither ||w||_inf nor ||D w||_2. With w^A := w - 2 sum_A w_k e_k:
|z + delta| >= w^A(z + delta) = |z| + w(delta) - 2 sum_A w_k (z_k + delta_k), and w_k z_k = |w_k||z_k|
(w_k and z_k have the same sign: on P by block-threshold, on Q by the formula for w_k). Take
A = {k : -s_k delta_k > |z_k|}. []

Lemmas 5.2 and 5.4 give two-sided control of the cost of a peak crossing to the opposite sign: between
2M(-s_k delta_k - |z_k|)_+ and 2(-s_k delta_k - |z||alpha_k|)_+; the thresholds differ by the Hilbert share
|z|Phi_k^2 M/C of |z_k| (in which the coordinate is not a peak any more but a non-peak with huge curvature).

### 5.4 Scale picture (HEURISTIC, used as guide only)
Along a primal direction v at a point with block data as above, at displacement t:
* non-peak k: Huber, quadratic (coefficient m^2 C u_k(v)^2/|z|) for |t| <~ W_k ~ Phi_k, linear beyond;
* peak k: zero until its delay T_k ~ mu_k/|u_k(v)| (simplex flatness), then like a non-peak with range 2M;
* rank-one terms from Lambda (peak sum vs Hilbert mass) and the Hilbert transverse term.
The linear contributions of the coordinates with Phi_k <~ |t| sum to O(t^2) ("persistent curvature" at depth
log(1/|t|)); this is the multiscale structure referred to in R5.

---

## 6. Mate fibres at tame points: finite certificates

**Lemma 6.1 (excess splitting). [PROVED]** Let eta be the normer of f (eta = x' or xi) with data as in 1.3. For
every nu in X** (resp. X):
  Delta(eta + nu) := p**(eta + nu) - f(eta + nu) = E_q(nu) + sum_m E_m(R_m** nu),
with E_q(nu) = q**(eta+nu) - c - a(nu) >= 0 and E_m(delta) = |z_m + delta|_m - sigma_m - w_m(delta) >= 0.
Proof. p**(eta) = 1 = f(eta) = c + sum sigma_m, f = a + sum R_m^* w_m, p** = q** + sum |R_m** .|_m. []
Since f(eta + t nu) = 1 + t f(nu): if f(nu) = 0 then Delta(eta + t nu) = phi(t nu) (resp. phi'(t nu)).

**Definition 6.0.** For a block m at eta: the margin of a peak k is mu_{k,m} := |u_{k,m}(eta)| - theta_m Phi_m(k)
(1.3). eta satisfies **margin sparsity (MS)** in block m if sum_{k in P°_m, mu_{k,m} < s} Phi_m(k) = o(s) as s -> 0+.
eta (or f) is **tame** if: (T1) a in c_00; (T2) the kink set K is finite; (T3) for every m the set
Qbar_m := Q_m cup Dg_m of strict non-peaks and degenerate peaks is finite; (T4) (MS) holds in every block.
For eta = x' in c_0, (T1) and (T2) are automatic.
Let J := N \ (F cup K) (free coordinates) and

  W(eta) := span{e_j^* : j in F cup K} + span{u_{k,m} : k in Qbar_m, m in I} + span{R_m^* w_m : m in I}   (finite-dimensional).

**Theorem 6.2 (Theorem A: tame NA points). [PROVED]** If f' in S_{p*} attains its norm at a tame x' in c_0, then
C(f') is contained in W(x').

Proof. Let psi_1,...,psi_N be the restrictions to the coordinates in J' of the functionals
u_{k,m} (k in Qbar'_m, m in I) and R_m^* w'_m (m in I), and V := {v in c_0 : supp v in J', psi_i(v) = 0 for all i}.
Fix v in V and t != 0 small.
Base: a'(v) = 0 (supp a' = F' is disjoint from J'), and since z' in c_0 the room r' := min_{J'} (1 - |z'_j|) is
positive; for |t| ||v||_inf <= c' r' Lemma 4.1 gives E_q(tv) = 0.
Block m: delta := t R_m v vanishes on Qbar'_m (u_{k,m}(v) = 0 there) and
0 = w'_m(R_m v) = M'_m sum_{P'_m} s_k (R_m v)_k + sum_{Q'_m} w'_m(k)(R_m v)_k = M'_m S_{P'}(R_m v);
so delta is supported in P°'_m with zero peak sum. By (5.1) (Lemma 5.2 with mu = 0),
E_m(t R_m v) <= 2 m |t| q(v) sum_{k in P°'_m : mu'_{k,m} < |t| q(v)} Phi_m(k) = o(t^2) by (MS).
Also f'(v) = a'(v) + sum_m w'_m(R_m v) = 0. Hence by Lemma 6.1, p(x' + tv) - 1 = Delta'(x'+tv) = o(t^2).
For g' in C(f') (g'(x') = 0, Lemma 2.1): t^2 g'(v)^2 = g'(x'+tv)^2 <= p(x'+tv)^2 - 1 = o(t^2), so g'(v) = 0.
Thus g'|_{c_0(J')} vanishes on the finite-codimensional subspace V of c_0(J'); by linear algebra in the dual pair
(c_0(J'), l_1(J')) it is a combination sum_i c_i psi_i. Then g' - sum_i c_i (corresponding functional) vanishes on
c_0(J'), i.e. is supported in the finite set F' cup K', hence lies in span{e_j^* : j in F' cup K'}. []

**Remark 6.3 (absorption by free coordinates). [PROVED content of the proof]** The proof shows *why* mates at
NA points are so constrained: the base is exactly flat on the infinitely many free coordinates of x' (room ~1 far
out), and by the independence lemma (F5) any finite set of block functionals restricted to the free coordinates
is linearly independent; so every direction can be corrected by a free-coordinate vector so as to become
invisible to the non-peaks and to the peak sum. Such directions are second-order flat (only peak overshoots,
o(t^2) under (MS)), hence killed by all mates. Consequence: **every mate at a tame NA point is a finite
certificate** (a finite combination of support coordinates, non-peak block functionals and R_m^* w'_m). To
approximate a mate g of f that is not (close to) such a finite combination, the NA approximants must be
non-tame: infinitely many non-peaks, or many near-threshold peaks (failure of (MS)), engineered by the free far
coordinates of z' (R4).

**Numerical confirmation** (C_work/thmA_test.py; n = 7, d = 3, one block with 5 coordinates, all peaks): the
subspace V' (free coordinates, w'(Rv) = 0) has dimension 3 and the excess along each of its basis vectors is
exactly 0 (|.| < 3e-16) for t up to 0.3, while a generic direction has excess/t^2 between 0.12 and 1.19.

**Theorem 6.4 (Theorem C: tame non-attaining supports). [PROVED]** If f in S_{p*} has a tame normer xi, then
C(f) is contained in W(xi). In particular C(f) is finite-dimensional.

Proof. Same as Theorem 6.2 with two changes. (i) Room: xi need not have uniform room, so work with
V_00 := {nu in c_00(J) : psi_i(nu) = 0}; for nu in V_00 only finitely many coordinates move and Lemma 4.1 applies
for small t (each moved coordinate has |z_j| < 1). The block computation is identical (R_m** nu = R_m nu, margins
mu_{k,m} at xi, (MS) at xi), so phi(t nu) = o(t^2), nu in ker f, and g(nu) = 0 for g in C(f) by Lemma 3.6.
(ii) Density: by (F5) the psi_i are linearly independent on c_00(J), so there are nu^1,...,nu^N in c_00(J) with
psi_i(nu^j) = delta_ij; for nu in V_0 := {nu in c_0(J) : psi_i(nu) = 0}, truncations nu_n -> nu in c_0 and
nu_n - sum_i psi_i(nu_n) nu^i in V_00 converge to nu. So g (continuous on c_0) vanishes on V_0, and the
linear-algebra step of Theorem 6.2 applies. []

**Lemma 6.6 (rebalancing directions). [PROVED]** Let xi be tame and m_0 in I, lambda real. There is
nu = lambda xi + nu_J with nu_J in c_00(J) such that f(nu) = 0, phi(t nu) = o(t^2) as t -> 0, and for every
g = b + sum_m R_m^* v_m in W(xi) (b supported in F cup K, v_m = omega_m + c_m w_m, omega_m supported in Qbar_m):

  g(nu) = lambda g(xi) - (lambda/sigma_{m_0}) v_{m_0}(z_{m_0}).

Proof. Let pi_m := sum_{k in P_m} s_k m Phi_m(k) u_{k,m} (so pi_m(y) = S_{P_m}(R_m y)); it is an absolutely
convergent series in l_1. By (F5), the restrictions to J of {u_{k,m} : k in Qbar_m} cup {pi_m} are linearly
independent (a relation would give an element of Y vanishing on the cofinite set J, hence 0, and the
T-coefficients at the infinitely many (k,m), k in P°_m, force the pi_m-coefficients to vanish, then the others).
So we can choose nu_J in c_00(J) with
  u_{k,m}(nu_J) = -(lambda/sigma_m) u_{k,m}(xi) [m = m_0] (k in Qbar_m),   pi_m(nu_J) = -(lambda/sigma_m) pi_m(xi) [m = m_0],
where [m = m_0] is 1 or 0. Put nu := lambda xi + nu_J.
* f(nu) = lambda + a(nu_J) + sum_m w_m(R_m nu_J), a(nu_J) = 0, and
  w_m(R_m nu_J) = M_m pi_m(nu_J) + sum_{k in Q_m} w_m(k) m Phi_m(k) u_{k,m}(nu_J) equals 0 for m != m_0 and
  -(lambda/sigma) w(z) = -lambda for m = m_0. So f(nu) = 0.
* Base: xi + t nu = (1 + t lambda)(xi + t nu_J/(1+t lambda)), so E_q(t nu) = 0 for small t (Lemma 4.1 and homogeneity).
* Block m != m_0: R_m**(t nu) = t lambda z_m + t R_m nu_J with R_m nu_J vanishing on Qbar_m and of zero peak sum;
  Lemma 5.2 (mu = t lambda) and (MS) give E_m = o(t^2).
* Block m_0: R**(t nu) = t(lambda - lambda/sigma) z + t delta'' with delta'' := R nu_J + (lambda/sigma) z, which vanishes
  on Qbar and has zero peak sum, and |delta''_k| <= m Phi_k (q(nu_J) + |lambda| q**(xi)/sigma); Lemma 5.2 and (MS)
  give E_{m_0} = o(t^2).
* By Lemma 6.1, phi(t nu) = o(t^2).
* g(nu) = lambda g(xi) + b(nu_J) + sum_m v_m(R_m nu_J); b(nu_J) = 0; for m != m_0 both omega_m(R_m nu_J) and
  w_m(R_m nu_J) vanish; for m_0: v(R nu_J) = -(lambda/sigma)(omega(z) + c w(z)) = -(lambda/sigma) v(z). []

**Proposition 6.5 (mates at tame f are balanced finite certificates). [PROVED]** Let xi be tame and g in C(f).
Then g = b + sum_m R_m^*(omega_m + c_m w_m) with b supported in F cup K, omega_m supported in Qbar_m (finitely
supported), and the decomposition is unique; moreover v_m(z_m) = 0 for every m and b(xi) = 0. If omega_m is
supported in Q_m, then c_m = -d_m with d_m := <D_m w_m, D_m omega_m>/C_m (the form used in Preprint A).

Proof. Theorem 6.4 gives the form; uniqueness from (F5) (R_m^* injective, Y cap c_00 = {0}, T injective across
blocks). Lemma 6.6 with g(xi) = 0 and Lemma 3.6 (phi(t nu) = o(t^2), nu in ker f) give g(nu) = 0, i.e.
v_{m_0}(z_{m_0}) = 0 for each m_0; then b(xi) = g(xi) - sum_m v_m(z_m) = 0. Finally omega(z) = sigma d
(z_k = sigma Phi_k^2 w_k/C on Q), so v(z) = sigma(d + c) = 0 gives c = -d. []

**Remark 6.7.** The rebalancing direction of Lemma 6.6 moves xi radially in the base and shifts block mass:
at xi + s nu the base norm is (1 + s lambda) q_0 and the m_0-block mass is (1 + s lambda - s lambda/sigma) sigma
(to first order), while the total p** stays 1 + o(s^2). It is a *second-order flat face* of the bidual ball,
parametrising the base/block split. It forces balance (Prop. 6.5) and governs the sharp second-order
coefficient (Section 8). At an NA point x' the same construction works (Theorem 6.2 setting).

**Remark 6.8 (existence of tame non-attaining f). [SKETCH]** Take a in c_00 cap S_{q*}, z in B_{l_inf} with
z_F = sign a_F, |z_j| <= 1/2 off F, z not in c_0; put xi := (z + U e)/p**(z + U e) and f := a + sum_m R_m^* J_m(R_m** xi);
then p*(f) = 1 = f(xi) (decomposition (1.1)) and f is not NA (xi not in c_0, strict convexity). Tameness needs
(T3)-(T4), i.e. |u_{k,m}(xi)| must avoid the windows [0, theta_m Phi_m(k) + o(Phi_m(k))] for all large k. If one
perturbs z by an i.i.d. random sequence on the coordinates off F and the u_{k,m} are not too spread
(e.g. ||u_{k,m}||_2 >= c 2^{-k/3}), Borel-Cantelli gives (T3)-(T4) almost surely. Without information on T,
existence is not proved here. (Preprint A's remark shows that the opposite property, infinitely many
half-peaks, is residual in the bidual face, so tame supports are meagre there.)

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

---

## 9. Beyond tame supports: the multiscale obstruction

### 9.1 What tameness excludes
(i) infinitely many strict non-peaks in a block (Q_m infinite) - by Preprint A's remark this is the *generic*
situation in the bidual face; (ii) failure of (MS): many near-threshold peaks; (iii) infinitely many kinks or
rooms 1 - |z_j| -> 0 off F; (iv) a not in c_00; (v) infinitely many degenerate peaks.

**Proposition 9.1 (general kernel statement). [PROVED]** Without (T3), but with (T1), (T2), (T4): every g in C(f)
vanishes on V_00 := {nu in c_00(J) : u_{k,m}(nu) = 0 for k in Qbar_m, w_m(R_m nu) = 0, m in I}. Same at NA points
(with J', Qbar'_m). Proof: verbatim the first half of Theorem 6.4 (only finitely many coordinates move; overshoot
o(t^2) by (MS)). []
If V_00 is dense in V_0 := {nu in c_0(J): same constraints}, then g|_J lies in the weak*-closed span of the
restrictions of u_{k,m} (k in Qbar_m) and R_m^* w_m. With infinitely many constraints this density is not
automatic. [SKETCH]

So in the generic case mates are "infinite certificates" g = b + sum_m R_m^*(sum_k omega_m(k) e_k + c_m w_m)
(in a weak sense). Recovery then needs approximation by finite certificates *inside* C(f) (or directly at NA
points), which is a statement about decay of the coefficients.

### 9.2 Necessary decay of deep coefficients. [SKETCH]
Single block, write g = b + sum_{k in Q} c_k u_k + mu R^* w (c_k = m Phi(k) omega(k)). Suppose that for K < K' there is
nu in c_00(J) with: u_k(nu) = 0 for k in Q, k <= K; zero peak sum on the shallow peaks k <= K; u_k(nu) = sign c_k
for k in Q cap (K, K']; w(R nu) = 0; and ||nu||_inf <= B, q(nu) <= B (a "sign-representing" vector; its existence
with B independent of K, K' is a quantitative independence property of (u_k), not proved here). Splitting
delta = t R nu into its shallow part (supported on shallow peaks, zero peak sum: overshoot o(t^2), Lemma 5.2) and its
deep part (|z + delta| <= |z + delta_shallow| + ||delta_deep||_1) gives
phi(t nu) <= o(t^2) + 2 m |t| B sum_{k > K} Phi(k), valid for |t| <= r/B (room). With Lemma 2.2 at |t| = r/B:

  ( sum_{k in Q cap (K,K']} |c_k| - B sum_{k > K'} |c_k| )^2 <= 4 m B^3 Phi'(K)/r (1 + o(1)),   Phi'(K) := sum_{k>K} Phi(k).

Hence (under the hypothesis) **sum_{k>K} |c_k| = O(sqrt(Phi'(K)))**, i.e. roughly |c_k| <~ sqrt(Phi(k)). Preprint A's
weighted-direction theorem needs sum_k c_k^2/Phi(k) < infinity (in its notation sum lambda_k omega_k^2 < infinity).
The gap between these - "borderline" mates with c_k^2/Phi(k) of order one - is not covered by any known
recovery technique. For such c, the truncation cost in Preprint A's proof is
|t| sum_{|t omega_k| > delta} lambda_k |omega_k| ~ t^2/delta, i.e. of the same order as the slack itself.

### 9.3 Why NA points cannot simply copy deep structure. [HEURISTIC, partial proofs]
* (Absorption, PROVED: Theorem 6.2/Remark 6.3.) At tame NA points all mates are finite certificates; deep
  structure is invisible to them. To carry an infinite certificate, x' must have infinitely many non-peaks or
  near-threshold peaks in suitable directions, engineered via the free far coordinates of z' (R4). Such
  engineering is possible coordinate by coordinate (adjust a far coordinate so that u_k(x') ~ 0 for a chosen k with
  u_k close to a target u in ker x'; later adjustments much smaller), as in Preprint A's remark.
* (Implant scale gap, HEURISTIC.) A non-peak implanted at depth k (where xi has a robust peak, margin >> Phi(k))
  changes w(k) by ~ M, so f' - f contains the term m Phi(k)(w'(k) - w(k)) u_k of size ~ M m Phi(k); unless cancelled
  by other coordinates, eps >~ Phi(k) and the slack covers only |t| >~ sqrt(Phi(k)), while the implant is quadratic
  only for |t| <~ W_k ~ Phi(k). The scale window (Phi(k), sqrt(Phi(k))) must be covered by structure that xi and x'
  share. Implants are therefore useful only below the slack scale created by *other* mismatches, never as the
  sole support of a mate component at intermediate scales.
* (Near-threshold implants are cheap.) Making a deep peak *near-threshold* (|u_k(x')| slightly above theta' Phi(k))
  does not change w'(k), hence costs nothing in eps; such peaks shorten near-flat faces (Prop. 8.2) and add
  curvature after their (tiny) delays. This is the natural tool for the rebalancing problem of Section 8 and
  for reproducing the "persistent curvature" of xi at small scales.
* (Far stiffness, PROVED for fixed data: Remark 4.3.) Kinks of xi on far coordinates cost nothing for l_1 data.

### 9.4 The candidate configurations (seed). [OPEN / partly resolved]
For each configuration, either a uniform reproduction at the NA approximants is possible (density) or it is not
(a counterexample would follow, by Lemma 2.3, from a uniform lower bound dist(rho g, C(f')) >= c > 0 for all NA
f' near f):
(A) **Rebalancing configuration (tame f)** - *resolved positively*: g = R^*(omega - d w) with
Gamma_w(g) = sigma H_N <= 1 < H_N = Gamma_max(g). Natural certificates fail, but rebalanced certificates with a transfer
peak (Theorem 7.4) recover it along the canonical truncations.
(B) **Borderline deep configuration** - *open*: f with infinitely many non-peaks (generic), and g with deep
coefficients c_k ~ kappa sqrt(Phi(k)) along non-peaks k_j -> infinity whose u_{k_j} approximate a fixed direction.
At every NA approximant the deep non-peaks must be reproduced down to scales ~ sqrt(eps), or replaced by
near-threshold peaks of x' (free in eps) together with transfer peaks. Whether the density of (u_{k,m})_k at every
depth (fine nets) allows this uniformly depends on quantitative properties of Martín's T (approximation rates
versus Phi). This is where a counterexample, if any, should be sought; equally, a positive proof must control
precisely this.
(C) **Kink components** (Remark 7.3): mates whose base part charges kink coordinates of xi are not finite
certificates in the sense of Definition 7.0 and are not covered. (Far base stiffness itself - rooms tending to 0 or
infinitely many kinks - does not affect finite certificates without kink components: the second-order lower bound of
Prop. 8.1 uses test points in l_inf that leave all coordinates off F fixed.)
(D) **Second-order effect of deep non-peaks on finite certificates.** At a generic f (Q infinite) the dual upper
bound Gamma_2 <= Gamma_w still holds for balanced finite certificates (Corollary 7.2(c)), but the test-point lower
bound of Prop. 8.1 breaks down: any test direction realising the finite data of g excites infinitely many non-peaks,
and the deep ones contribute "persistent" curvature (linear-regime terms of total size ~ t^2 at every scale t).
If Gamma_2(g) < Gamma_w(g) for some mate, transported certificates (coefficient -> Gamma_w at the canonical NA
approximants) cannot recover it, and the approximants would have to reproduce the persistent curvature of xi at
all scales below their slack scale (possible in principle with near-threshold peaks of x', which are free in eps,
placed at every depth with u_k close to the relevant directions; this needs fine nets of (u_{k,m}) at every
depth). HEURISTIC counter-argument: a decomposition beating Gamma_w must use deep coordinates at *first* order
(second-order transfers are already optimal at Gamma_w), and first-order transfers between base and blocks
require u_k to approximate vectors supported in supp a at precision ~ Phi_k (approximation rates); without such
rates I expect Gamma_2 = Gamma_w at all supports with a in c_00, in which case (D) is void. Not proved.

---

## 10. Failed attempts and why they fail

1. **Pointwise excess domination** phi'(v) >= rho_1^2 phi(Tv) on the small region (Lemma 3.4). Fails in
   general: at tame x' the subspace V' of Theorem 6.2 has phi' = o(t^2), while phi(T v) may be of order t^2 there
   (deep non-peaks or near-threshold peaks of xi see v). The comparison must therefore be made *after* using the
   structure of g (e.g. g vanishes on V'), not for all directions.
   [FALSE as a general principle; rigorous instance:] suppose some strict non-peak k of xi (block m; data w, M, C,
   |z| of xi) is a non-degenerate peak of the tame NA point x' (data w', M', P°'), and C > 2 Phi_m(k)^2 M^2.
   Optimising sigma in Lemma 5.3 (with w(delta) != 0 allowed) gives, for delta = t R_m**(T v), Tv := v - f(v) xi,
   E_m(delta) >= C kappa(v)^2 t^2/(2 Phi_k^2 |z|)(1 + o(1)), where kappa(v) := delta_k/t - Phi_k^2 w_k w(delta)/(C t)
   = [m Phi_k u_{k,m} - (Phi_k^2 w_k/C) R_m^* w](v) (the f(v)-terms cancel because z_k = |z| Phi_k^2 w_k/C on Q).
   Claim: kappa restricted to J' is not in the span of the constraint functionals psi'_i defining V'. Otherwise (F5)
   turns the relation into an identity of T-coefficients in block m (other blocks drop out): on the infinitely many
   j in P°'_m \ {k}: c_R w'_j = -(Phi_k^2 w_k/C) w_j (c_R the coefficient of R_m^* w'_m); at (k,m), k not in Qbar'_m:
   1 - Phi_k^2 w_k^2/C = c_R w'_k. If c_R = 0 the latter says Phi_k^2 w_k^2/C = 1, impossible because
   C = ||D w||_2 >= Phi_k|w_k| gives Phi_k^2 w_k^2/C <= Phi_k|w_k| < 1. If c_R != 0, then (|w'_k| = |w'_j| = M', peaks
   of x') |c_R w'_k| = |c_R w'_j| = (Phi_k^2|w_k|/C)|w_j| <= Phi_k^2 M^2/C, while 1 - Phi_k^2 w_k^2/C >= 1 - Phi_k^2 M^2/C;
   so 1 <= 2 Phi_k^2 M^2/C, contradicting the assumption. Hence there is v in V' with kappa(v) != 0, so phi(t T v) >= c_v t^2 (c_v > 0) for
   small t, while phi'(t v) = o(t^2) (proof of Theorem 6.2): phi'(t v) < rho_1^2 phi(t T v) for all small t != 0,
   and t v lies in the small region. (The assumption C > 2 Phi^2 M^2 holds unless C < M^2/8, since Phi_m(k) <= 1/4.)
2. **Additive corrections.** Remark 2.4: g^ + h with ||h|| = O(sqrt eps) chosen pointwise does not give a mate;
   two-point combinations along low-curvature directions break it.
3. **Ray criterion with subquadratic profiles** (Lemma 3.3): profiles at x' have superquadratic portions from base
   rooms (Lemma 4.1) and peak delays (Lemma 5.2), so the criterion fails in the directions that matter.
4. **Hessian domination** (g(v)^2 <= Hessian(v)) is necessary (Lemma 3.6) but not sufficient: each block coordinate
   is quadratic only on a window ~ Phi(k).
5. **Implants of non-peaks** cannot bridge (Phi(k), sqrt Phi(k)) (Section 9.3).
6. **Permanence via truncated blocks.** p'_K := q + |P_K R .| + |(I - P_K) R .| has s_K := |(I-P_K)R.| <= eta_K q, so
   density for q + |P_K R .| would transfer to p'_K by Preprint B Thm permanence; but p'_K != p and
   p - (q + |P_K R .|) is not a seminorm (|.| is not additive over coordinate splits), so nothing transfers to p.
7. **Rebalancing through a single deep peak alone.** Lowering one peak coordinate does not lower ||W||_inf; the block
   level drops only through the Hilbert part, by s Phi(k)^2 M/C per unit s, while the base absorbs
   m Phi(k) u_k: efficiency ~ Phi(k) M/(m C) -> 0. Efficient transfers must lower all near-peak coordinates
   uniformly; a single deep peak is then useful only as the *corrector* of the resulting vector (Theorem 7.4).
   Also a local optimiser (Nelder-Mead) started at the natural decomposition does not find the transfer-peak
   decomposition (it needs a large O(t^2/Phi_{k_*}) move of one coordinate): numerics must use the explicit form.
8. **Naive primal base decomposition** (cube part frozen on its face, Hilbert part adjusted): gives the base
   Hessian ||k_perp||^2/q_0, too large by the factor 1/||U^* a|| (numerically 0.788 vs 1.359 => ratio 0.58 =
   ||U^* a||); the correct Hessian rebalances cube and Hilbert parts inside q.
9. **"Truncations of mates are mates"** via a separable Legendre argument requires |c_k| <= gamma_k m Phi(k)
   (the Huber conjugate is infinite beyond the slope); this is far stronger than the necessary decay of 9.2,
   because the separable bound ignores the redundancy of the dense family (u_k). Neither proved nor refuted.
10. **Engineering x' with all far coordinates non-peaks**: impossible, since every tail of (u_k) is dense in the
   sphere, so |u_k(x')| < theta' Phi(k) for all large k would force x' = 0.

---

## 11. Numerical experiments (all in scratchpad/C_work; numpy only)

| script | purpose | key output |
|---|---|---|
| blocknorm.py, blockexact.py | exact block norm by peak-set enumeration, cross-checked with a primal bisection | agreement ~1e-9 |
| lam_check.py | Lemma 5.1 (Lambda formula) and its gradient | 12-digit agreement; dLambda/dS = M, dLambda/dY = C Y/|y| |
| basenorm.py | exact base norm q by support enumeration | agrees with random dual search |
| base_profiles.py | Section 4 profiles | free: flat within rooms; kink: 0 inward, 0.3214 t^2 outward (pred. 0.3218); inward support coordinate 0.3118 (pred. 0.3094) |
| thmA_test.py | Theorem 6.2 | 3-dim subspace with excess 0 (<3e-16) up to t = 0.3 |
| base_hess.py | Prop. 8.1(i) | primal sup 1.1106 vs q_0 H_b = 1.1086; naive Hessian off by ||U^*a|| |
| rebalance_test.py, face_test.py, dual_mech.py | Prop. 8.2 | Gamma_w 0.298 < true ~0.355 < Gamma_max 2.86; face traced exactly; optimal dual lowers all peaks uniformly |
| transfer_peak_test.py, transfer_explicit.py, transfer_explicit2.py | Theorem 7.4 | explicit rebalanced decomposition with a transfer coordinate: Gamma_eff = 0.392, 0.327, 0.307, 0.3005 (delta_0 = 0.1, 0.03, 0.01, 0.003) -> Gamma_w = 0.298; Nelder-Mead from the natural decomposition misses it (stays at 0.362) |
| lowerbound_test.py | Prop. 8.1 lower bound | Lambda_SS closed form = C c_Q/(|z| F2) to 15 digits; Legendre value 0.29824 vs sigma H_N 0.29822; test points 0.2636, 0.2889, 0.2952 -> 0.2982 |

Caveat: these are finite-dimensional models; in finite dimensions every functional attains its norm, so they
test lemmas, not density.

---

## 12. Open problems and recommended next steps

(Q1) **Existence and abundance of tame non-attaining supports** (Remark 6.8) for Martín's actual T; and the
extension of Theorem 8.4 to finitely many degenerate peaks and kinks.
(Q2) **Generic f (Q infinite) with (MS).** Prove or refute: every g in C(f) is a norm limit of
balanced finite certificates g_n with Gamma_w(g_n) <= 1 + o(1) and (f, g_n/(1+o(1))) contractive. Combined with
Theorem 7.4 and (R3) this would give density on such supports. The critical regime is the borderline decay of 9.2;
the new tools available are transfer peaks and (free) near-threshold implants.
(Q3) Kink components (Remark 7.3), rooms -> 0 (9.4(C)), failure of (MS) and degenerate peaks, a not in c_00
(infinite base support, sign-flip costs).
(Q4) Quantitative properties of Martín's T relevant here: (a) existence of bounded sign-representing vectors
(9.2); (b) approximation rates of targets by u_{k,m} at depth k relative to Phi_m(k) (fine nets); these decide
whether the borderline configuration (B) can be reproduced at NA points.
(Q5) Combine with Preprint A's residual set Omega: Omega and the tame supports are both contained in R; R is
closed under the "transitivity" of (R3). Is R closed? If R were closed, density would follow from density of
Omega - but R is defined through fibres, and upper semicontinuity of C goes the wrong way; a lower-limit argument
along *tame* approximants f_n -> f (tame supports are meagre but may be dense) is a possible route: it would need
liminf C(f_n) >= rho C(f), i.e. that every mate of f is approximated by finite certificates of nearby tame supports.

Overall assessment. Strategy C produced a clean framework (localisation to the small region, kernel slices,
exact block geometry, absorption theorem), a complete recovery theorem for finite certificates under the sharp
second-order condition, and density along the tame supports (Theorem 8.4). The main new insights:
(1) at NA points the free coordinates absorb all curvature not certified by finitely many ingredients (Theorem A),
so density is equivalent in substance to approximability of every mate by finite certificates uniformly across
scales; (2) the sharp second-order coefficient is the mass-weighted Gamma_w, and it is achieved at NA points thanks
to transfer peaks supplied by the density of (u_{k,m}). The open core is the borderline deep regime of infinite
certificates at generic supports.
