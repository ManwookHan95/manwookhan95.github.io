# P1 part 4: resonance types; cross-block near-duplicates; a weighted averaging theorem

## 4.1 Proposition (exact resonances need infinitely many one-sided base coordinates). PROVED.
Let (D, Omega_D) with D = L*Omega_D != 0, Omega_D in V*, and suppose that for a sequence s_n -> 0+ the transfers
f = (a + s_n D) + L*(w - s_n Omega_D) have cost <= s(2 s_n) (an "exact", scale-free resonance). Then
  kappa(D) := sum_{j notin F} (|D_j| - z_j D_j) = 0,
i.e. off F the vector D lives on the contact set K with the sign of z; D is in Y \ {0}, hence not in c_00; so F cup K is infinite.
In particular: at every NA point, and at every f with a in c_00 and K finite, there are no exact resonances (cf. A Prop 7.4).
*Proof.* q*(a + sD) >= 1 + s D(zhat) + s kappa(D) (one-sided derivative of q* at a, A Lemma 7.2), and N_m(w_m - s Omega_m) >=
1 - s <Omega_m, zeta_m>/|zeta_m|. Both are <= s(2s) = 1 + O(s^2); divide by s, let s = s_n -> 0, multiply the block inequalities
by |zeta_m| and the base inequality by q_0, add: q_0 D(zhat) - <Omega_D, L**xi> + q_0 kappa(D) <= 0. The first two terms cancel
(D(xi) = <Omega_D, L**xi> since D = L*Omega_D, and D(xi) = q_0 D(zhat)), so kappa(D) <= 0, hence = 0. D in Y \ {0} and
Y cap c_00 = {0}. QED.
So there are two resonance types: (R-exact) scale-free transfers through infinite contact sets (or near-flip sets when a is not
in c_00) — Theorem 2.4 realizes this; (R-approx) scale-dependent transfers, in which one-sided carriers at depth Phi ~ t
(weak peaks, near-threshold off-peak coordinates, near-contacts) approximately represent the same functional on the two sides.

## 4.2 Proposition (sign rule; which side a one-sided carrier serves). PROVED.
For every block m and k with u_{k,m}(xi) != 0: sign w_m(k) = sign u_{k,m}(xi) (on P by Fact C: sign zeta(k) = sign alpha_k =
sigma_k; off P: w(k) = C zeta(k)/(Phi_k^2|zeta|)). A one-sided usage of (k,m) at scale tau (inward peak deviation, or an off-peak
push beyond the gap in the long direction) has sign(tau Omega(k)) = -sign u_{k,m}(xi). Hence, if (k,m) carries tau c v with
c > 0 and u_{k,m} close to v, then sign(tau) = -sign u_{k,m}(xi): carriers with u(xi) < 0 serve tau > 0, carriers with
u(xi) > 0 serve tau < 0. One-sided carriers are near or above the threshold: |u_{k,m}(xi)| >= (1 - gamma) theta_m Phi_m(k) with
gamma the relative gap (gamma = 0 for peaks). Consequently two carriers (k,m), (k',m') can SWITCH (serve opposite sides) only if
  ||u_{k,m} - u_{k',m'}||_{q*} q**(xi) >= (1 - gamma) theta_m Phi_m(k) + (1 - gamma') theta_{m'} Phi_{m'}(k').
*Application to Martin's built-in cross-block near-duplicates.* If u_{n,m} and u_{n,m'} follow the same w'_n up to a perturbation
that is o(Phi) in the xi-direction (in particular exact duplicates), then u_{n,m}(xi) and u_{n,m'}(xi) have the same sign whenever
they are near the threshold: such pairs serve the SAME side and cannot switch with each other. Switching between near-duplicates
requires perturbations of order >= Phi in the xi-direction AND placement of the two members on opposite sides of 0 near their
respective thresholds. Lemma B's conclusion neither forces nor excludes this (cf. Remark 2.1.1: such pairs can be inserted).

## 4.3 Theorem (weighted averaging). PROVED.
Let g in C(f), rho in (0,1). Suppose there are finite certificates c_1, ..., c_n at f and weights mu_i >= 0, sum mu_i = 1, with
coordinatewise radii r_i := r^cw(c_i) > 0 and errors e_i := p*(g - g_{c_i}), and numbers s_0 in (0, min(1, sqrt(1-rho^2))],
eta_0, kappa_0 >= 0 with rho^2 (1+eta_0)(1+kappa_0) <= (1+rho^2)/2, such that
 (i) H(c_i) <= 1 + eta_0 and kappa(c_i) r_i <= kappa_0 for all i;
 (ii) for every s in (0, s_0]:  sum_{i : r_i < rho s} mu_i e_i <= (1 - rho^2) s/(12 rho);
 (iii) sum_i mu_i e_i <= (1 - rho^2) s_0/(3 rho).
Then rho g_c is in Cert(f) for c := sum_i mu_i c_i, and ||rho g_c - rho g||_{p*} <= rho sum_i mu_i e_i.
Consequently, if for every rho < 1 and eps > 0 such families exist with sum mu_i e_i <= eps, then g in cl Cert(f).
*Proof.* As in A Thm 6.8. By convexity p*(f + s rho g_c) <= sum_i mu_i p*(f + s rho g_{c_i}). For i with r_i >= rho|s| use
A Prop 4.5 (with the coordinatewise radius, referee fix G1): p*(f + s rho g_{c_i}) <= 1 + (rho^2 s^2/2) H(c_i)(1 + kappa(c_i) rho|s|)
<= 1 + (s^2/2)(1+rho^2)/2. For r_i < rho|s|: p*(f + s rho g_{c_i}) <= s(rho s) + rho|s| e_i (g in C(f)). Hence for |s| <= s_0,
p*(f + s rho g_c) <= max(1 + s^2(1+rho^2)/4, s(rho s)) + (1-rho^2)s^2/12 <= s(s) (the two cases exactly as in Thm 6.8, using
s^2 <= 1 - rho^2 and s(s) - s(rho s) >= (1-rho^2)s^2/3). For |s| >= s_0: p*(f + s rho g_c) <= s(rho s) + rho|s| sum mu_i e_i
<= s(rho s) + (1-rho^2)s_0|s|/3 <= s(s). H(rho c) <= rho^2 max_i H(c_i) <= 1 by convexity of H. QED.

## 4.4 Corollary (near-threshold carriers with non-summable gaps are not a defect source). PROVED.
Let g in C(f) and suppose there are a finite certificate c^0, a real c != 0 and strict non-peaks (k_i, m_i), i >= 1, with
lambda_i := lambda_{k_i,m_i}, gamma_i := gap_{m_i}(k_i), such that
 (a) lambda_{i+1} <= lambda_i/2 and gamma_i is nonincreasing;
 (b) p*(g - g_{c^0} - c u_{k_i,m_i}) <= K lambda_i;
 (c) limsup_i H(c^0 + (0, (c/lambda_i) e_{k_i} in block m_i)) <= 1;
 (d) sum_i gamma_i = infinity.
Then g in cl Cert(f). (Thm 6.8/Cor 6.10(c) is the case inf gamma_i > 0.)
*Proof.* c_i := c^0 + (c/lambda_i)e_{k_i}. Its d-coefficient d_i = c Phi_i w(k_i)/(m_i C) -> 0, so for large i the coordinatewise radius is
r_i = min(r(c^0), gamma_i lambda_i/(2|c|)) = gamma_i lambda_i/(2|c|), kappa(c_i) is bounded, kappa(c_i) r_i -> 0, and
e_i <= K lambda_i + |d_i| p*(R*w) <= K' lambda_i. Fix rho; choose eta_0, kappa_0, s_0 as in 4.3. On a stretch i_0 <= i <= i_1 put
mu_i := gamma_i/Gamma, Gamma := sum_{i_0}^{i_1} gamma_i. Since gamma_i lambda_i decreases at least by the factor 1/2,
sum_{i : r_i < rho s} mu_i e_i <= (K'/Gamma) sum_{i : gamma_i lambda_i < 2|c| rho s} gamma_i lambda_i <= 4 K'|c| rho s/Gamma,
which is <= (1 - rho^2)s/(12 rho) once Gamma >= 48 K'|c| rho^2/(1 - rho^2); by (d) such stretches exist with i_0 arbitrarily large, and
then sum mu_i e_i <= 2K' lambda_{i_0} is as small as we like ((iii) and the approximation). (i) holds for i_0 large by (c). QED.
Remarks. (1) Uniform weights (Thm 6.8) need inf gamma > 0; the gap-proportional weights need only sum gamma_i = infinity
(e.g. gamma_i ~ 1/i suffices). (2) For sum gamma_i < infinity the single-coordinate averaging fails (with mu_i <= A gamma_i forced
by (ii) at s ~ gamma_i lambda_i, sum mu_i <= A sum gamma_i). Whether such "super-near-threshold" switching mates lie in cl Cert(f) is
OPEN: there is no linear obstruction (their limit direction v is in cl S(f), being a limit of strict non-peak vectors), so
part 1's method does not apply; a proof of non-membership would need a quantitative obstruction (e.g. a sequence test
f_n -> f with g notin Li C(f_n), using that cl Cert(f) is contained in Li C(f_n) for every sequence, A Cor 4.11).
(3) Weak-peak carriers (margins mu_k -> 0 relative to Phi_k) are never certificate coordinates; switching mates carried only by
weak peaks on both sides are outside the scope of every averaging argument and are the approximate analogue of Theorem 2.4.
