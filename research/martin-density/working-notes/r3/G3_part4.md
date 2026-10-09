# G3 part 4: extraction of a balanced finite certificate on every window scale

Standing: as in part 3 (SLD operator, f in R_0, g in C(f), window index l_*, t in W(l_*), t <= min(t_eta, 1), eta <= eta_1 :=
min(eta_*, min_m M_m/2), a two-sided decomposition at scale t). K := K_1 Lambda_f(l_*) (3.4). We also assume K t <= 1 (true in the windows
used later: K T_hi(l_*) -> 0, see 5.3). "Coarse coordinates" of block m: Cset_m := {k : iota(k,m) <= l_*}; fine: the others.
Constants written K_b, K_2, K_4, C' depend only on f, gamma, N (not on g, t, l_*).

## 4.1 Definition (the window certificate c_t).
 * Base: kappa_t := (B_+ 1_F)(zhat), b_t := B_+ 1_F - kappa_t a.
 * Block m: for k in Cset_m cap Q_m with g_k := gap_m(k) >= t^2 put omega^c_m(k) := clamp(omega_{+,m}(k); [-2 g_k/t, 2 g_k/t]); put omega^c_m(k) := 0 at all
   other k (peaks, coarse non-peaks with gap < t^2, fine coordinates). Here omega_+ = Omega_+ + d_+ w (2.4).
 * c_t := (b_t, (omega^c_m)_m), g_{c_t} := b_t + sum_m R_m*(omega^c_m - d(omega^c_m) w_m), d(omega) := <D_m w_m, D_m omega>/C_m.

## 4.2 Proposition (window certificate). PROVED.
 (a) c_t is a balanced finite certificate in the sense of C Def 7.0 (supp b_t in F, b_t(xi) = 0, omega^c_m finitely supported in Q_m), with
     gap_m(k) >= t^2 and |omega^c_m(k)| <= 2 gap_m(k)/t on supp omega^c_m, ||D_m omega^c_m||_2 <= 2/t and |d(omega^c_m)| <= 2/t.
 (b) ||b_t||_1 <= K_b.
 (c) (remainder) ||g - g_{c_t}||_1 <= K_2 Lambda_f(l_*) t.
 (d) (weighted coefficient) sqrt(Gamma_w(c_t)) <= sqrt(1 + eta_Gamma(eta)) + K_4 Lambda_f(l_*) t, where Gamma_w(c) := q_0 h(b) + sum_m sigma_m H_m(omega_m)
     is C's mass-weighted coefficient (C Def 7.0; H_m(omega - d(omega) w) = H_m(omega)).
*Proof.* (a) b_t(zhat) = kappa_t - kappa_t a(zhat) = 0, and xi = q_0 zhat. The coarse set is finite. The bounds on omega^c are the clamp;
||D omega^c||_2 <= (2/t)||Phi_m||_2 <= 2/t, and |d(omega)| <= ||D omega||_2 ||D w||_2 / C = ||D omega||_2.
(b) |kappa_t| <= |B_+(zhat)| + ||zhat||_inf ||B_+ 1_{F^c}||_1 <= t/(2q_0) + (1 + ||U||)(K t + t/q_0) by 2.3(a), 3.5(b); and ||B_+ 1_F||_1 <= K_F(1 + Kt + t/q_0)
by 2.5. Use K t <= 1, t <= 1.
(c) g - g_{c_t} = (B_+ - b_t) + sum_m R_m* X_m with X_m := Omega_{+,m} - omega^c_m + d(omega^c_m) w_m. Base: B_+ - b_t = B_+ 1_{F^c} + kappa_t a, so
||B_+ - b_t||_1 <= (2 + ||U||)(K t + t/q_0) + t/(2q_0) (||a||_1 <= 1). Block m (index dropped): with Omega_+ = omega_+ - d_+ w and 1_C, 1_F the
indicators of coarse and fine coordinates,
   X = [ (omega_+ - omega^c) 1_C - (d_+ - d(omega^c)) w 1_C ] + [ Omega_+ 1_F + d(omega^c) w 1_F ],
and ||R* x||_1 <= sum_k lambda_k |x(k)|.
 Fine part: sum_F lambda_k |Omega_+(k)| = sum_{Fset} |c^+_l| <= 3 sum_{l > l_*} lambda_l / t <= 3 t^2 (3.1, (P2), t >= T_lo(l_*)), and
 |d(omega^c)| sum_F lambda_k |w(k)| <= (2/t) c_{l_*+1} <= 2 t^2.
 Coarse excess: rho_k := |omega_+(k) - omega^c(k)|. CLAIM: lambda_k rho_k <= |Delta c_k| + lambda_k |Delta d| M + 2 t lambda_k for every coarse k, where
 Delta c_k := lambda_k (Omega_+(k) - Omega_-(k)), so that lambda_k |omega_+(k) - omega_-(k)| <= |Delta c_k| + lambda_k |Delta d| M.
  - Peak k: omega^c(k) = 0 and, by 2.4(c), omega_+(k) and omega_-(k) have opposite signs (weakly), so rho_k = |omega_+(k)| <= |omega_+(k) - omega_-(k)|.
  - Non-peak k (gap g_k > 0), if |omega_+(k)| > 2 g_k/t: by 2.4(f) and |d_+ t| <= 1, sigma_k omega_+(k) <= 2 g_k/t, so sigma_k omega_+(k) < -2 g_k/t and the
    clamp excess is e_k := -sigma_k omega_+(k) - 2 g_k/t > 0; by 2.4(f) and |d_- t| <= 1, sigma_k omega_-(k) >= -2 g_k/t, hence
    sigma_k(omega_-(k) - omega_+(k)) >= e_k: the part of omega_+(k) beyond the clamp is ONE-SIDED and is bounded by the two-sided difference.
    If g_k >= t^2 then rho_k = e_k (or 0); if g_k < t^2 then omega^c(k) = 0 and rho_k <= 2 g_k/t + e_k <= 2t + |omega_+(k) - omega_-(k)|.
 Summing, with sum_k lambda_k <= 1, 3.4 and 3.5(c): sum_C lambda_k rho_k <= K t + K_d K t M + 2t.
 d-difference: |d_+ - d(omega^c)| <= |d_+ - d(omega_+)| + |d(omega_+ - omega^c)| <= t/sigma_m + sum_k Phi_k |omega_+(k) - omega^c(k)|
 (|d(x)| <= ||Dx||_2 <= ||Dx||_1), and sum_k Phi_k |...| <= (1/m) sum_C lambda_k rho_k + sum_F Phi_k (|Omega_+(k)| + |d_+| M)
 <= (1/m) sum_C lambda_k rho_k + 3t^2 + (3/t + 1/sigma_m) t^3 (2.4(e), (P2)). Multiply by sum_C lambda_k |w(k)| <= 1.
 Collecting terms, ||g - g_{c_t}||_1 <= C'(K t + t) <= K_2 Lambda_f(l_*) t (Lambda_f >= 1).
(d) sqrt(Gamma_w) is a seminorm on pairs (base vector, block vectors) (part 2), and H_m vanishes on multiples of w_m, so
sqrt(Gamma_w(c_t)) <= sqrt(Gamma_w(B_+, Omega_+)) + sqrt(Gamma_w(B_+ - b_t, (omega_+ - omega^c)_m)). The first term is <= sqrt(1 + eta_Gamma(eta)) (2.3(d)).
For the second: q_0 h(x) <= ||U||^2 ||x||_1^2/nu and sigma_m H_m(x) <= ||D x||_2^2/C_m <= (sum_k Phi_k |x(k)|)^2/C_m; both were bounded by C'(K t + t) in (c). QED.

## 4.3 Remarks.
 (i) Nothing about the blocks of f was assumed: Q_m may be infinite, peaks may be degenerate or weak, (MS) may fail, several blocks may be
     active, contact sets may be infinite. All one-sided resources (peaks, coordinates pushed beyond 2 gap/t, contacts, near-contacts) enter
     only through the two-sided differences |Delta c_k|, ||Delta B||, which are pinned (part 3).
 (ii) The certificate is built from the + side only; the - side is used solely to bound the one-sided excess of the + side.
 (iii) Gamma_w, not Gamma_max = max(h, H_m), is the controlled quantity: the first-order terms of base and blocks are individually only O(t)
     (2.3(a)), so each piece separately can exceed the s(t)-level at second order (this is the second-order rebalancing of the open core
     item O2); the budget identity controls exactly the mass-weighted sum. Part 5 therefore uses transfer peaks (C Thm 7.4).
