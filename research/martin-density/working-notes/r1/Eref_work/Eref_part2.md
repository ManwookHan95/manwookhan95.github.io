# E referee — part 2: N1, Thm 5.1, Cor 5.2, box tails

## N1 (necessary conditions) — verdict: correct (one overstatement in an imported fact)
(N-a) f NA => (f,g) NA for g in C(f) (g vanishes at the normer of f in S_p). f in Omega => Hausdorff continuity => recovery.
      If C(f) is in Li C(f'_n) for one NA sequence, everything recovered (A Cor 3.3). Correct.
(N-b) cl Cert^sh(f) is in Li C(f_n) for every sequence (A Thm 4.17, refereed), and Li C(f_n) is convex with 0, so
      rho g recovered if g in cl Cert^sh. Correct. NOTE: the sharp necessary condition is rho g notin cl Cert^sh(f)
      (stronger than g notin), since cl Cert^sh is a convex symmetric set containing 0.
(N-c) If one-sided linear decompositions (Prop 7.4 sense, Omega+- in V*) have b+ - b- in c_00 then Fact F(a) gives
      equality; Prop 7.4(a) kills K-part; Theorem L gives g in cl Cert. Correct. (Linear decompositions admissible on
      (0,r] automatically have bounded block parts: |Omega(k)| <= 2/r + |mu| off peak, so V* is not an extra assumption.)
(N-d) G_referee 4.7. Correct.
Overstatement: E's (F3) "(f, rho g) in cl NA for all g, rho iff C(f) in Li C(f'_n) for SOME NA sequence" — only "if" is
in A Cor 3.3; A Remark 3.4 explicitly leaves "only if" open for l_2^2. Harmless: the single-pair characterization
"(f, rho g) notin cl NA iff exists delta: dist(rho g, C(f')) >= delta for all NA f' in S with ||f'-f|| < delta" is TRUE
(proof: adjoint of (f, rho g) peaks only at +-e_1 because of the strict slack; nearby NA operators peak near +-e_1;
rotate by Q_n -> I after replacing x_n by -x_n if needed; the rotated first row is NA, second row is in C(f'_n)).

## Thm 5.1 (Averaging Criterion) — verdict: correct (duplicate of A Thm 6.8, slightly weaker hypotheses form)
Re-derived every inequality:
 - fine/coarse split, sum_{s_j<|t|} s_j < 2|t|; bound 1 + (rho^2 t^2/2)(1+kappa_0|t|) + 2 rho K_0 t^2/J;
 - rho^2/2 = 1/2 - 4 e1; total <= 1 + t^2(1/2 - 2 e1) <= 1 + t^2/2 - t^4/8 needs t^2 <= 16 e1, given t_*^2 <= 8 e1;
 - Step 2: min(t^2,|t|) >= t_*|t| for |t| >= t_* (t_* <= 1); s_J <= (1-rho^2) t_* J/(6 rho K_0).
 - H(c') <= rho^2 by convexity/homogeneity (L4.2). p*(g' - rho g) <= 2 rho K_0 s_J/J.
All correct. Radius: either Def 4.1 radius or coordinatewise; P4.5 holds for both.
Weakness vs A Thm 6.8: requires H(c_s) <= 1 EXACTLY. Truncation-type applications produce H(c_s) -> H <= 1 possibly
from above; rescaling c_s by H^{-1/2} costs o(1)||g||, not O(s). So applications with H(c_s) = 1 + o(1) must use
A Thm 6.8 (allows H <= 1 + eta(t)). The extension of 5.1 is immediate (replace rho^2 by rho^2(1+eta_0)).

## Cor 5.2 — verdict: correct for g_0 = 0 (= A Cor 6.10(c) with H explicit); g_0 != 0 fixable
Checked: i(s) = largest index with lambda_i >= 2 c q*(v) s/gamma exists for s small (lambda_i -> 0) and
lambda_i < thr/theta_0 (from lambda_{i+1} < thr and lambda_{i+1} >= theta_0 lambda_i). No monotonicity of lambda_i needed.
R_m* omega_s = c q*(v) u_{k_i}. d_s = Phi(k_i) w(k_i) c q*(v)/(m C_m), O(lambda_i). ||D omega_s||^2 = c^2 q*(v)^2/m^2,
H = (c^2 q*(v)^2/m^2 - d_s^2)/C_m <= 1 EXACTLY. radius gap/(2|omega|) >= gamma lambda_i/(2 c q*(v)) >= s. kappa -> 0.
Error: c q*(v)(u - vhat) - d_s R_m* w_m; p* <= q* <= (1+||U||)||.||_1, so the bound is (1+||U||) c q*(v) K lambda_i
+ O(lambda_i) — E dropped the factor (1+||U||) (harmless, O(s) either way).
g_0 != 0: H_m(omega_0 + omega_s) -> H_m(omega_0) + c^2 q*(v)^2/(m^2 C_m) (cross term = -d_0 d_s -> 0 by disjoint
supports). So the correct hypothesis is H_m(omega_0) + c^2 q*(v)^2/(m^2 C_m) < 1 (or <= 1 using A Thm 6.8 with 1+o(1)),
if omega_0 lives in block m; if in other blocks, max structure gives it for free. Radius of the sum with Def 4.1:
>= s min(gap_0,gamma)/gamma — rescale s. So the SKETCH is completable; E's hypothesis "H(c_0 + single-coordinate part)
<= 1" is ambiguous (the single-coordinate part depends on s) and should be replaced by the explicit limit condition.
Scope: gaps >= gamma > 0 and scale density lambda_{i+1} >= theta_0 lambda_i are essential; D's 12.2 critical regime with
near-peak carriers or scale-sparse carriers is NOT covered. "Not an obstruction for two-sided resources" is accurate
only with these two hypotheses.

## A_notes 7.4 box tails (SKETCH) — verdict: correct with fixable gaps; already PROVED as A Cor 6.10(a) (+ G1 fix)
E's literal wording "truncations omega 1_{[1,N(s)]} at the level where the box holds at scale s" (index truncation) is
WRONG as stated: counterexample — near-peak coordinates k_i with gap(k_i) = 2 s_i |omega(k_i)|, s_i -> 0 super fast:
at scale s in (s_{i+1}, s_i], E(s) = {k_j : j > i}, the index truncation at min E(s) - 1 discards the whole tail
beyond k_{i+1}, a FIXED positive amount for s down to s_{i+1}; error/s unbounded. Correct truncation (A Cor 6.10(a)):
omega 1_{k <= J_s, |s omega(k)| <= gap(k)/2} with the COORDINATEWISE radius (A-referee G1). Also needs H <= 1 + o(1)
version of the averaging theorem (A Thm 6.8), not E's Thm 5.1 (H <= 1 exactly).
