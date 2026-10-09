# Y1 referee, part 2: numerics for Lemma T / T2, and the pinning lemmas 3.1-3.6

## 2.1 Independent numerics (Y1_ref_work/)
* lemmaT_cert2.py: for 150 random finite blocks (n = 6..29, Phi_k = 2^{-k} U(0.2,1), zeta_k = N(0,1) Phi_k^{U(0,3)}), the functional
  predicted by Lemma T, w(k) = sgn(zeta_k)(C/A) min(theta, nu_k) with theta the root of Psi, satisfies N(w) = 1 to 2.2e-16 and
  <w, zeta> = A to 5.4e-16 (exact norming certificate), and A equals the primal SOCP value min max(||x||_1, ||y||_2), zeta = x + Phi y,
  to 2.5e-9. Since N is strictly convex in finite dimension, this IS the norming functional.
  (lemmaT_indep.py / lemmaT_peakset.py: a dual SOCP solve agrees in value but its w differs from the certificate by up to 0.99 at
  coordinates of negligible weight |zeta_k|, Phi_k ~ 2^{-30}: solver indeterminacy, not a counterexample; the certificate settles it.)
* lemmaT_indep.py part 2: 2493 adversarial tests of Lemma T2 (half with a constructed DEGENERATE peak c, nu_c = theta exactly by
  bisection; perturbation of l_1-size up to A s/(8(A+theta+1)) placed on the other peaks inward and on strict non-peaks outward, weighted
  by 1/|nu_k - theta|, i.e. in the threshold-lowering direction): 0 violations of the lower bound of T2(b) (smallest ratio
  actual/bound 8.45), 0 of the upper bound, 0 of the Lipschitz bound T2(a).
Verdict on Lemma T, T2, T3 (with part 1.3): CORRECT.

## 2.2 Lemmas 3.1-3.6 (pinning at a clean sub-window), re-derived
Setting: D_X, clean w = (l,i), l >= l_f >= max F, t in W(w), sum_{l'>l} lambda_{l'} <= b(w)^2/3, |Delta theta_l| <= 6 lambda_l/t.
* Lemma 3.1. For s in S^nat_{l''}(l) = S_{l''} \ (F ∪ T(l)): coarser targets vanish on S_{l''} (allowedness (a)), later COARSE targets
  vanish at s (s notin T(l)), other signatures vanish (disjointness); so -Delta B(s) = Delta theta_{l''} v_{l''}(s) + r(s) with r(s) a
  FINE sum only. phicalc (c),(d) and minimization over the sign give r^nat |Delta theta| <= E + 2 sum |r(s)|; the S^nat are disjoint
  subsets of F^c (budget t/q_0); for l >= max F, S^nat contains S \ ([1,l] ∪ T(l)), so ||v 1_{S^nat}|| >= m^nat >= 1/D(l). CORRECT.
  (Constant: sum_{l''} sum_s |r(s)| <= (4/3)(6/t) sum_fine lambda <= 4 b^2/t, not 2t^7 as written; harmless, b^2/t <= t^7.)
* Lemma 3.2. phi_{z_s}(eps tau v(s)) = |tau| v(s)(1 - eps z_s sgn tau) >= (tau)_- v(s)(1 + eps z_s); sum over S^nat:
  (tau)_-(2||v 1|| - r^nat) <= E + 2 sum|r|, and 2||v1|| - r^nat >= ||v1|| >= 1/D. e_0 = -sum_{R ∪ fine} Delta theta u 1_{F^c}. CORRECT.
* Lemma 3.3: eq:peakshift with Delta Theta(k) = -eps tau/lambda, eq:margin sigma|alpha(k)| = lambda mu, mu = q_0 Phi theta (rho-1)/m
  >= q_0 Phi theta u/m for rho >= 1+u; 1/(lambda mu) <= m D^2/(q_0 theta u). (a),(b),(c) CORRECT.
* Lemma 3.4 (shift pinning under (SP_w)). Upper bound via (U1)/(U2): Lemma 3.3(a),(b). Via (U3): eq:didentity, for a G-carrier
  Phi w Delta theta/(mC) = -q tau; q > 0 terms <= q (tau)_-; anti peaks tau <= -lambda Delta d M; anti near-threshold strict non-peaks:
  suplevel(f) gives vs(omega_- - omega_+)(k) >= -3 gap/t and vs(omega_- - omega_+)(k) = -tau/lambda - Delta d |w(k)|, hence
  tau <= lambda(3 gap/t - Delta d |w(k)|) (re-derived); carriers with rho <= b: |q tau| <= 6 b Phi M lambda/(m C t) <= t^3 for l large
  (1/C_m is an f-constant, b <= t^4/(l Design)). Moving the Delta d terms to the left gives Delta d M (1 + ...) <= ..., and if
  Delta d M < 0 the upper bound is trivial. Lower bounds symmetric. CORRECT.
  Observation (PROVED, minor addition): a +1-one-signed block (Lemma 3.6) automatically has an UPPER source (U3), a -1-one-signed
  block automatically a LOWER source (L3); (SP_w) is a genuine hypothesis only for the other side.
* Lemma 3.5 (a)-(d): CORRECT. (b) is a correct and useful observation: an ANTI-type near-threshold strict non-peak can be pushed
  outward on the + side only by gap/t, so tau <= lambda(3b M/t + |Delta d| M) <= 3t^3 + K_d t; its tiny gap is not a rate.
* Lemma 3.6: CORRECT, but its statement must include (SP_w) (the proof uses |Delta d| M <= K_d t from Lemma 3.4); in the master
  theorem (SP_w) is assumed, so nothing changes. |q| >= Phi M u/(mC) on Sigma (clean: rho > b => rho >= u). CORRECT.
* Classification completeness (checked): every coarse class-G carrier at a clean w is exactly one of: anti peak, swallowing peak with
  rho >= 1+u, swallowing peak with rho in [1, 1+b] (K4), strict non-peak with rho <= b (K3, incl. w = 0), near-threshold strict non-peak
  (anti: dropped; swallowing: K4), robust strict non-peak with rho in [u, 1-u] (swallowing K1, anti K2). In sigma-one-signed blocks only
  K3 is kept (Sigma contains all swallowing peaks and all strict non-peaks with rho > b that are not anti near-threshold).
* Constants: K_g <= C D/u, K_d, K_P <= C_f D^3/u, K_O <= C_f D^5/u^2 (D = D(l), u = u(w)), C_f independent of l, w, t. CORRECT.
