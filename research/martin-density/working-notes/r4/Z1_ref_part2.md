# Z1 referee, part 2: Z1 part 2 (defect terms, budget form, ray lemma, consequences)

## 2.1 Homogeneity/convexity (Z1 2.1). Verdict: CORRECT (PROVED).
Kink is positively homogeneous. Each flip term tau -> 2(-sign(a_j) tau B_j - |a_j|)_+ is convex and vanishes at 0. For k in P_m,
tau -> ||w + tau Omega||_inf - sigma_k (w + tau Omega)(k) is convex (sup of affine maps minus an affine map) and vanishes at tau = 0 because
|w(k)| = M. A convex phi with phi(0) = 0 satisfies phi(tau) <= (tau/t) phi(t) on [0, t]. Random check (scalar_checks.py): max violation 0.

## 2.2 Budget form (Z1 2.2). Verdict: CORRECT (PROVED).
Re-derived A Lemma 7.1: q_0 q*(A) + sum_m sigma_m N_m(W_m) = q_0 E_q(A) + sum_m sigma_m e_m(W_m) + (A + L*W)(xi), with (A + L*W)(xi) =
f(xi) + t g(xi) = 1 and the left side <= s(t). A Lemma 7.2 (re-derived): E_q(a + tB) = Fl_B(t) + t Kink(B) + nu Psi(t U*B/nu)
(for j in F: |a_j + tB_j| - sign(a_j)(a_j + tB_j) = 2(-|a_j| - sign(a_j) t B_j)_+), and
e_m(W) = sum_P |alpha_k| (||W||_inf - sigma_k W(k)) + ||P-perp D(W - w)||^2/(||DW|| + <DW, Dw>/C), using ||alpha||_1 = 1 (from <w, alpha> = 1 - C = M).
Lower bounds of the two quadratic terms as in G3 2.3(d). Dividing by t gives Delta1(t) + (t/2) Gamma_w/(1 + eta_Gamma) <= t/2.

## 2.3 Ray lemma (Z1 2.3). Verdict: CORRECT (PROVED).
Checked line by line:
 (i) q_0 beta_0 + sum sigma_m beta_m = g(xi) + Delta1 - Delta1 (q_0 + sum sigma_m) = 0, hence g_t(xi) = 0 (a(xi) = q_0, <w_m, zeta_m> = sigma_m).
     |beta_0| <= t/(2 q_0) + t/(2 q_0) + t/2 <= 3t/(2 q_0) and |beta_m| <= 3t/(2 sigma_m) (2.3(a) of G3 and 2.2); p*(a), p*(R_m* w_m) <= 1.
 (ii) f + tau g_t = [(1 - tau beta_0) a + tau B] + sum_m R_m*[(1 - tau beta_m) w_m + tau Omega_m] (exact), and p*(A + L*W) <= max(q*(A), max_m N_m(W_m)).
 (iii) With X := B(zhat) + Kink(B) + Fl_B(t)/t: (1 - tau beta_0)(1 + tau_0 X) = 1 + tau (X - beta_0) = 1 + tau Delta1, tau_0 = tau/(1 - tau beta_0)
     (identity checked numerically to 2e-16). The quadratic bound uses Psi(h) <= ||h-perp||^2/(2(1 - ||h||)) (from
     ||e + h|| - 1 - <e,h> = ||h-perp||^2/(||e+h|| + 1 + <e,h>)) and ||s U*B/nu|| <= ||U|| eta/nu, s <= t. Fl_B(tau_0) <= (tau_0/t) Fl_B(t) needs
     tau_0 <= t, true for tau <= t/2 and t small.
 (iv) Block: N(w + s Omega) = 1 + s<Omega, zeta>/sigma + peak(s) + s^2 ||P-perp D Omega||^2/(||DW_s|| + <DW_s, Dw>/C); the denominator is >= 2(C - eta)
     since ||s D Omega|| <= ||t D Omega|| <= eta. Same algebra with beta_m.
 Two bookkeeping remarks (no effect): the factor (1 + c t) is absorbed into (1 + c_f eta) only if t_eta <= eta, which may be assumed WLOG;
 and the conclusion holds with Gamma_max = max(h(B), max_m H_m(Omega_m)), which can exceed 1 even though Gamma_w <= 1 + o(1).

## 2.4 Consequences (Z1 2.4). Verdict: (a) CORRECT; (b) CORRECT as an upper bound, the clause "and in general NOT below" is unproved;
## (c) a correct explanation of why the averaging upper bound fails, labelled PROVED but it proves no necessity.
(a) Immediate from 2.3 with Delta1 = 0.
(b) Re-derived: for tau in [c_rho Delta1, t/2], rho tau Delta1 <= tau^2 (1 - rho^2 Gamma')/4 and tau^4/8 <= tau^2 (1 - rho^2 Gamma')/4 for tau^2 <=
    2(1 - rho^2 Gamma'), so 1 + rho tau Delta1 + rho^2 tau^2 Gamma'/2 <= s(tau) (Gamma' := Gamma_max(1 + c_f eta) < 1/rho^2). Random check: max
    violation 0. "In general NOT below" would need a LOWER bound p*(f + tau rho g_t) >= 1 + c tau Delta1, which is not shown (the decomposition
    need not be optimal). It should be labelled HEURISTIC.
(c) The computation shows that the specific bound "average of the scale-t_i ray bounds" has an uncompensated first-order term. It does not show
    that no other decomposition of the averaged functional works. Label: HEURISTIC (method-level), not PROVED.
