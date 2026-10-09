# G3 referee, part 2: parts 4-5 (window certificate, transfer, averaging, Thms B, C) and numerics

## 4.1-4.2 window certificate -- CORRECT
* (a) balanced finite certificate: b_t(zhat) = kappa_t - kappa_t a(zhat) = 0; omega^c supported in the finite coarse set, on strict
  non-peaks with gap >= t^2, |omega^c| <= 2 gap/t, ||D omega^c|| <= (2/t)||Phi_m||_2.
* (b) ||b_t|| <= K_b with K_b depending on f only (2.5 + 3.5(b) + Kt <= 1, t <= 1).
* (c) re-derived: X = [(omega_+ - omega^c)1_C - (d_+ - d(omega^c)) w 1_C] + [Omega_+ 1_F + d(omega^c) w 1_F].
  One-sidedness checks (the heart of 4.2):
   - peak k: sigma_k omega_+(k) <= 0 <= sigma_k omega_-(k) (box at the sup level, both sides), so |omega_+(k)| <= |omega_+(k) - omega_-(k)|;
   - non-peak pushed beyond the clamp: + side capacity toward the peak level is (1 - d_+ t) g/t <= 2g/t, so the excess is on the far side,
     sigma_k omega_+(k) < -2g/t, while the - side satisfies sigma_k omega_-(k) >= -(1 + d_- t) g/t >= -2g/t; hence e_k <= |omega_+ - omega_-|;
   - omega_+ - omega_- = Delta Omega + Delta d w, so lambda_k |omega_+ - omega_-| <= |Delta c_k| + lambda_k |Delta d| M.
  Fine part: <= 3t^2 + 2t^2 using t >= T_lo(l_*). d-difference: |d_+ - d(omega_+)| <= t/sigma_m plus the D-mass of the excess.
  (Small arithmetic: the fine d-term is (3/t + t/sigma_m) * (sum_F Phi_k) <= (3/t + t/sigma_m) t^3/3; G3 writes a larger bound. Harmless.)
* (d) sqrt(Gamma_w) is a seminorm (weighted sum of squares of seminorms), H_m kills multiples of w_m, excess bounded in (c). Correct.

## 5.1 uniform transfer expansion -- CORRECT
Re-derived (T1) q_0 beta_t = sigma_m e_{y,t} +- lambda_* mu_* from zeta/sigma = alpha + D^2 w/C, sum_P|alpha| = 1, sigma|alpha_{k_*}| = m Phi_* mu_*;
(T2) e_0 = +-[(lambda_* u_* - T) + (T(zhat) - lambda_* u_*(zhat)) a], q*(e_0) <= 2 lambda_* delta_1; Lset_t \ P decreases to empty.
Step 3 sup-norm cases (i)-(iv) checked (supp omega has gap >= t^2 > t^2/2, so supp omega cap Lset_t = empty; k_* a peak, not in supp omega).
Step 4: <Dw,h>/C = s d M - eps(e_y - 1) (re-derived); ||h|| <= 4c_1 + Y_0 t^2 is O(c_1), NOT o(1): the relative error (1+th)(1+2||h||/C) - 1
is O(th + c_1/C_min), so c_1 must be chosen small depending on eps_tr -- G3 does this (Step 6). Step 5: E = (s^2/2)(Gamma - h) + s^2 sum|tau|lambda_* mu_*/q_0
re-derived (sum_m sigma_m (H_m - Gamma)/(2 q_0) = (Gamma - h)/2). Uniformity: constants depend on c only through A_0, Gamma_w <= 2, (C-b). Correct.
(The several-block version of C Thm 7.4 ALONG CANONICAL TRUNCATIONS, used in 5.2, is C's "Remark (several blocks)", accepted by the C referee
with a sign slip for tau_m < 0; G3's Step 1 handles that sign correctly: tau_m(+-lambda_* mu_*) = |tau_m| lambda_* mu_*.)

## 5.2 windowed averaging -- CORRECT (self-contained; does not need A Thm 6.8's statement)
Convexity p*(f + s rho g_c) <= (1/n) sum_i p*(f + s rho g_{c_i}); small s: indices with rho|s| > c_1 t_i have sum t_i < 2 rho|s|/c_1, giving
Q s^2 with Q = 2 rho^2 K/(c_1 n) <= (1 - rho^2)/12; checks: rho^2(1+eta_0) + 2Q <= 1 - (1 - rho^2)/3, and s^4/8 <= (s^2/2)(1-rho^2)/3 for
s^2 <= 1 - rho^2; slack s(s) - s(rho s) >= (1 - rho^2)s^2/3 for |s| <= 1. Large s: need 3|s| >= 2 s_0 sqrt(1+s^2) for |s| >= s_0, true since
|s|/sqrt(1+s^2) is increasing and sqrt(1+s_0^2) <= 3/2. (The hypothesis c_1 t^(j) <= rho s_0 is not needed.) Contractivity of (f, rho g_c) for
all s (incl. the limit s -> infinity) => rho g_c in C(f); Gamma_w(rho c) <= rho^2 max_i Gamma_w(c_i) by convexity; C Thm 7.4 applies to the
FIXED averaged certificate. Correct.

## 5.3 Theorem B -- CORRECT, one bookkeeping slip (fixable)
SLIP: "choose eta with sqrt(1 + eta_Gamma(eta)) <= sqrt(1 + eta_0/2) - 1/100" is IMPOSSIBLE when sqrt(1 + eta_0/2) < 1.01, i.e. eta_0 < 0.0201,
which is forced for rho close to 1 (eta_0 <= (1 - rho^2)/(2 rho^2); e.g. rho = 0.99 gives eta_0 <= 0.0102). Fix: margin
kappa_0 := (sqrt(1 + eta_0/2) - 1)/2 > 0 in place of 1/100, and require K_4 Lambda_f(l) t <= kappa_0 (true for large l). Nothing else changes.
Window bookkeeping checked: t_i = T_hi(l) 2^{1-i} in [2 T_lo(l), T_hi(l)]; Lambda_f(l) T_hi(l) <= vartheta^{-l^2} 2^{-l^3}/l -> 0;
n_l >= l 2^{l^3} Lambda°(l) beats 24 rho^2 (1+||U||) K_2 vartheta^{-l^2} Lambda°(l)/(c_1(1 - rho^2)) for large l. Quantifier order (T fixed
before f, g, rho) handled by the 2^{l^3} slack. Correct.

## 5.4 Theorem C -- CORRECT (both directions; (=>) is the standard rotation argument, NA subset R_0).

## Numerics (G3ref_work/model.py, model2.py, test_lemmas.py)
Finite toy model (16 base coordinates, one block of 6 carriers with private one-point signatures, a contact and a near-contact, 2 non-peaks,
a near-threshold peak). SOCP (CLARABEL) optimal decompositions of f +- t g for a boundary mate g:
 t = 3e-2 .. 1e-3: 2.3(b) holds with large margin; both decompositions represent g (residual <= 1e-6); pinning inequality 3.2 holds up to
 solver noise (max violation 1.4e-7); sum|Delta c| = 0.04 t (O(t), as 3.4 predicts).
Caveat: finite models are degenerate (p** not strictly convex; the normer face is 12-dimensional, and the mate space here is only the
3-dimensional certificate space), so this checks signs/one-sidedness only, not the switching phenomena.
