# Y1 part 0 — reading digest (for my own use; not a result file)

Setting: note paper/martin_density_note.tex, Section 8. I = {1..N}, p = p_N. Carrier l = j(k,m); u_l = (y_l + delta_l h_l)/n_l,
v_l := delta_l h_l/n_l (= u_l on S_l), lambda_l = m Phi_m(k) <= c_l/4, Phi_l := Phi_{m(l)}(k(l)) = 2^{-m-k} c_l.
(P1) supp y_l cap S_{l'} = {} for l' >= l; (P2) sum_{l'>l} lambda_{l'} <= T_lo(l)^3; (P3) window factor.
Two-sided decomposition (B_pm, Theta_pm) at scale t; Delta theta_l; Delta B = -sum Delta theta_l u_l. Box: |theta^pm_l| <= 3 lambda_l/t.
Budget: sum_{j notin F} phi_{z_j}(Delta B(j)) <= t/q_0. Swallowed (bad) l: z = eps_l on S_l\F; tau_l := -eps_l Delta theta_l.
q_l := eps_l Phi_l w_m(k)/(m C_m) (for strict non-peaks = eps_l u_l(xi)/sigma_m; |q_l| = (M - gap)Phi/(mC)).
(peakshift) at a peak k: |omega_+(k)| + |omega_-(k)| = -vs_k Delta Theta(k) - Delta d M >= 0, <= t/(lambda_k mu_k) if alpha(k) != 0.
(didentity) Delta d_m M_m = (1/(m C_m)) sum_k Phi w Delta theta_{k,m} + r_m, |r_m| <= 2t/sigma_m.

Key Round-5 tools:
* Z3 Theorem E (PROVED, any admissible T): first rows f_j -> f, supp a_j = F, with exact d-neutral two-piece data at f_j on windows
  (T_j, n_j) [(E-a) b(xi_j)=0, t||b|| <= A_0, Gamma_w^{(j)} <= 1 + eta_0/2; (E-b) size conditions of Lemma U with A_2, gamma_B;
  (E-c) p*(g - g_{j,t}) <= K_j t; (E-d) K_j T_j -> 0, n_j/K_j -> inf; (E-e) p*(f_j - f) <= theta_j (T_j 2^{-n_j})^2, theta_j -> 0]
  => (f, rho g) in cl NA. Any sub-window allowed. Lemma U: constants uniform along f_j -> f (supp a_j = F).
* Z3 Lemma 3.1 (PROVED): companion f^# (same a, z^# = z on F, delta := z^# - z), Delta_m = sum_k lambda_k |u_k(delta)|,
  c(delta) = sum_m [Delta_m log(e/Delta_m) + sum_k min(lambda_k, |u_k(delta)|)]; if max Delta_m <= c_f: p*(f^# - f) <= C_f c(delta),
  sum ||R_m^*(w^# - w)||_1 <= C_f c(delta), ||D(w^# - w)||^2 <= C_f c(delta)^2, |C^# - C| etc <= C_f Delta.
* Z3 Lemma 1.2/1.3/1.4 (PROVED): |R^** zhat^#| d^#(omega) - |R^** zhat| d(omega) = (R^* omega)(delta); exactifying an approximately
  resonant d-neutral carrier gives q^#_l = Re(u_l)/|R^**zhat^#| > 0 (destroys d-neutrality).
* Z3 Prop T (+ referee fixes T2-T6) / Cor 3.4: coarse exactification at windows; frozen error C(1 + C_H^#)(K^#_* + theta)t.
* Z3 referee explosive design (D1^F): F(l+1) >= max{F(l)^2, (l+1)2^{(l+1)^3}, b(l)^{-4(l+1)}}, b(l) := 4^{-2n^w_l} T_hi(l)^4
  delta_min(l) 2^{-s_max(l)}/l, u(l) := F(l)^{-1/(4l)}; bands (b(l), u(l)) pairwise disjoint; at most |L_N cap [1,L]| windows
  in [1,L] blocked by any sequence rho_l; Prop 4.3.1 (conditional).
* Z4 Theorem A'' (S_Binf) for SLD_G (G*(l) over all subsets of [1,l]; N-free): F finite, (H2''), (H3), (DR), (W_inf).
  Active sets U(t) = {l in B cap [1,l*] : lambda_l >= t^2}. Lemma R: without (DR) Hoffman >= 1/q_l'.
  Ref Lemma 9.2 free channels; Sketch 9.3 (FS) for degenerate swallowing-sign peaks.
* Z6 (ref): design D''' (Xi'(l) = [l H_comb G* D(l)]^4 (l 2^{l^3} Lambda° G*)^5, D(l) = 1 + sum(1/m^nat + 1/Phi)); Theorem U'
  (blocks compensated or rigid; rates Lambda_g, K_P, K_R, gamma_B; hypotheses (E1),(E2),(E3'),(E4'),(E5)=(H2'),(W_U')).
  Prop P (Farkas pinning of d-rigid carriers), Theorem V, Cor V.1, Prop R1, Theorem C (SLD, (H1), compensated resonant).
  Lemma 2.1 (inward-only third kind coordinates in one-sided transfer expansion).
