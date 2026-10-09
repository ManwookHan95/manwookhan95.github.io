# Z1 part 2: the ray lemma (what makes a decomposition scale-dependent), any admissible T

Standing: f in S_{p*}, g in C(f), eta <= eta_* (G3 2.3), t <= t_eta, and a "+ side" decomposition at scale t: g = B + L*Omega with
q*(a + tB) <= s(t), N_m(w_m + t Omega_m) <= s(t) (G3 2.1). Notation: Kink(B) := sum_{j notin F} (|B_j| - z_j B_j) >= 0,
Fl_B(tau) := sum_{j in F} 2(-sign(a_j) tau B_j - |a_j|)_+ (A Lemma 7.2), peak_m(tau) := sum_{k in P_m} |alpha_{m,k}| (||W_tau||_inf - sigma_k W_tau(k)),
W_tau := w_m + tau Omega_m, h(B) = ||P_{e-perp} U*B||^2/nu, H_m(Omega) = ||P_m-perp D_m Omega||^2/C_m.
FIRST-ORDER (one-sided-linear) DEFECT of the decomposition:
  Delta1(t) := q_0 [Kink(B) + Fl_B(t)/t] + sum_m sigma_m peak_m(t)/t  >= 0.
Exact one-sided resources contribute nothing to Delta1: base mass on exact contacts with the contact sign, inward use of DEGENERATE peaks
(alpha_k = 0), anything on non-peaks inside the box. Near-contacts (0 < 1 - |z_j| small), wrong-signed contact mass, flips, inward use of
peaks with alpha_k > 0 (weak peaks) contribute linearly.

## 2.1 Lemma (homogeneity / convexity of the defect terms). PROVED.
For 0 < tau <= t: Kink(tau B) = tau Kink(B); Fl_B(tau) <= (tau/t) Fl_B(t); peak_m(tau) <= (tau/t) peak_m(t).
*Proof.* Kink is positively homogeneous. Each flip term tau -> 2(-sign(a_j) tau B_j - |a_j|)_+ is convex and vanishes at 0. For k in P_m,
tau -> ||W_tau||_inf - sigma_k W_tau(k) is convex (a sup of affine functions minus an affine function) and vanishes at tau = 0 (|w(k)| = M,
sigma_k = sign w(k)). A convex function phi with phi(0) = 0 satisfies phi(tau) <= (tau/t) phi(t) on [0,t]. QED.

## 2.2 Lemma (budget form). PROVED.
  Delta1(t) + (t/2) Gamma_w(B, Omega) / (1 + eta_Gamma(eta)) <= t/2,  in particular Delta1(t) <= t/2.
*Proof.* A Lemma 7.1: q_0 E_q(a + tB) + sum_m sigma_m e_m(W_t) <= t^2/2. A Lemma 7.2: E_q(a + tB) = Fl_B(t) + t Kink(B) + nu Psi(t U*B/nu) and
e_m(W_t) = peak_m(t) + t^2 ||P-perp D Omega||^2/(||D W_t|| + <D W_t, D w>/C). Bound the two quadratic terms from below exactly as in G3 2.3(d). QED.

## 2.3 Ray Lemma. PROVED.
There are c_f, eta_r > 0 (depending only on f) such that if eta <= eta_r then: with
  beta_0 := B(zhat) + Kink(B) + Fl_B(t)/t - Delta1(t),   beta_m := <Omega_m, zeta_m>/sigma_m + peak_m(t)/t - Delta1(t),
  g_t := g - beta_0 a - sum_m beta_m R_m* w_m,
one has g_t(xi) = 0, ||g - g_t||_{p*} <= c_f t, and for 0 < tau <= t/2
  p*(f + tau g_t) <= 1 + tau Delta1(t) + (tau^2/2) Gamma_max(B, Omega) (1 + c_f eta),   Gamma_max := max(h(B), max_m H_m(Omega_m)).
*Proof.* (i) q_0 beta_0 + sum_m sigma_m beta_m = [q_0 B(zhat) + sum_m <Omega_m, zeta_m>] + Delta1 - Delta1 (q_0 + sum sigma_m) = g(xi) + 0 = 0
(A Remark 2.3: g(xi) = 0; q_0 + sum sigma_m = 1). Hence g_t(xi) = g(xi) - beta_0 q_0 - sum beta_m <w_m, zeta_m> = 0. By G3 2.3(a) and 2.2,
|beta_0| <= 3t/(2q_0) and |beta_m| <= 3t/(2 sigma_m); since p*(a), p*(R_m* w_m) <= 1, ||g - g_t|| <= c_f t.
(ii) Decomposition: f + tau g_t = [(1 - tau beta_0) a + tau B] + sum_m R_m*[(1 - tau beta_m) w_m + tau Omega_m], so by A Fact A
p*(f + tau g_t) <= max( (1 - tau beta_0) q*(a + tau_0 B), max_m (1 - tau beta_m) N_m(w_m + tau_m Omega_m) ), tau_i := tau/(1 - tau beta_i) <= t for
tau <= t/2 and t small.
(iii) Base: q*(a + sB) = 1 + s B(zhat) + Fl_B(s) + s Kink(B) + nu Psi(s U*B/nu) <= 1 + s (B(zhat) + Kink(B) + Fl_B(t)/t) + (s^2/2) h(B)/(1 - ||U|| eta/nu)
for 0 < s <= t (2.1; Psi(h) <= ||h-perp||^2/(2(1 - ||h||)), ||sU*B/nu|| <= ||U|| eta/nu <= 1/2). With s = tau_0 and the factor (1 - tau beta_0):
(1 - tau beta_0)(1 + tau_0 X) = 1 - tau beta_0 + tau X = 1 + tau Delta1 (X := B(zhat) + Kink + Fl/t), and the quadratic term gets the factor
1/(1 - tau beta_0) <= 1 + c t.
(iv) Block m: N_m(w + sOmega) = 1 + s<Omega, zeta>/sigma_m + peak_m(s) + s^2 ||P-perp D Omega||^2/(||D W_s|| + <D W_s, Dw>/C) and the denominator is
>= 2(C_m - eta) (||s D Omega|| <= ||t D Omega|| <= eta, G3 2.2). With 2.1 and the same algebra, (1 - tau beta_m) N_m(w + tau_m Omega) <=
1 + tau Delta1 + (tau^2/2) H_m(Omega) C_m/(C_m - eta) (1 + c t). Take c_f eta >= the collected relative errors (t <= t_eta and t_eta -> 0 with eta). QED.

## 2.4 Consequences. PROVED.
(a) If Delta1(t) = 0 (only exact one-sided resources are used), the single normalized decomposition g_t is a ONE-SIDED LINEAR (two-piece-type)
    decomposition valid on the whole ray 0 < tau <= t/2, with second-order coefficient Gamma_max(1 + O(eta)).
(b) If Delta1(t) > 0, the same decomposition at scale tau << t costs the first-order excess tau Delta1(t), which by 2.2 can be as large as
    tau t/2: a decomposition that uses near-resources is useful only at its own scale. With rho: the bound
    p*(f + tau rho g_t) <= s(tau) holds for tau in [c_rho Delta1(t), t/2], c_rho := 4 rho/(1 - rho^2 Gamma_max(1 + c_f eta)) (when that number is < 1),
    and in general NOT below.
(c) (Why averaging over scales needs two-sided objects.) Let ghat := (1/n) sum_i rho g_{t_i} over a geometric window. For a target scale tau,
    the summands with t_i >> tau contribute (rho tau/n) sum_{t_i >> tau} Delta1(t_i), which can be of order tau t_1/n (Delta1(t_i) <= t_i/2) and is then >> tau^2 for tau << t_1/n;
    so averaging (G3 5.2, A Thm 6.8) closes the scale gap only if, for the + side AND the - side separately, the near-resource usage
    Delta1 is removable at cost O(K t) in norm (as at R_0 points, where it is bounded by pinned two-sided differences, G3 4.2(c)), or if
    Delta1 = 0. This isolates the exact obstruction for Lemma Z: PERSISTENT SWITCHING THROUGH UNPINNED CARRIERS WHOSE ONE-SIDED RESOURCES ARE NEAR
    (not exact) RESOURCES, or exact resources that differ between the two sides by O(1).
