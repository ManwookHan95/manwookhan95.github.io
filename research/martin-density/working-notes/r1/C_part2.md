
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
