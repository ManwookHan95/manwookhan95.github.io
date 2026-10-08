
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
