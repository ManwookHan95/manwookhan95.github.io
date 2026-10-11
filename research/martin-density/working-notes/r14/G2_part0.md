# G2 part 0: reading log (context digest; not results)

Read so far: BRIEFING.md, BRIEFING_R2.md (all addenda), martin_paper_summary.md, r13/H1_referee.md, r13/H1_ref_notes.md,
r13/H2_referee.md, r13/H2_ref_notes.md, r13/H2_notes.md.

Key objects (from H2 1): Step A (Sys-A) at the unpushed prepared row R_1; rows l = coarse strict non-peaks, (FC)-frozen weak peaks,
D-pushed rows; Ft_l = val_l - rt_l kappa_{m(l)}; near-certificate y (unit, size eps <= eps_*): phi_y = y^T Ft(R_1) small and
max_g(-y^T g) small over generators g; zeta_m(y; rt) = sum_{l in m} y_l rt_l. K^+_m / K^-_m kind-(iv) rows with rt > 0 / < 0.
Kind (iv) = one-sided upward value generator (bank at a near S_th coordinate with z_s = eps_l); kind (i) = two-sided private TU.
(R1) stage: no thick-type carrier; h = 0; pure (U*) certificates: y_l >= -e_1 on (iv), sum_(iv) y_l >= c_1/4 (Prop 3.1(a)); per-block
lever balance (3.1(b)).
Theorem H2.A: bands on free K^- rows and bandable free K^+ rows realize Step A unless some block is residual
(two)/(up)/(down) with PINNED (in a tiny minor / cofactor polynomial) or LOCKED rows.
Prop 4.1 ((U)-block, restricted model): residual iff exists lambda: (lambda^T C')_P >= 0 on pinned (iv) rows, (lambda^T C')_Q = 0 on pinned
two-sided rows, lambda^T M(rc) > 0.  Cor 4.2 false for several minors; repair: full row rank of C'_Q.
F-NE: b >= 8 rho A_0 Design^{C_P} s_1/T (from theta_0 = b/Design^{C_P}, s_1 <= theta_0 T/(8 rho A_0)) while delta_Z <= delta s_1/(64 rho C_f
Design^C): wrong-sided resonances of size in (delta_Z, C b] remain.
Memory (Lemmas 2.6/2.7): along CONSECUTIVE (R1) main stages: kind-(iv) carriers deactivate; switching signs never flip; (up)/(down) ->
unshifted. (D-abs) (4.4, SKETCH): unbounded memory within round range [r, s_max(p_r)).
H1-ref Lemma SLP: objects E (movable rows with robust/near-threshold status; pieces G ∩ m in (U)-blocks) consisting of thick-type and kind-(i)
rows; V_LP = max{-Xi.delta : a_d.delta <= 0 (d in N), ||delta||_inf <= 1}; V_LP >= c_LP realizes Step A; dual: Xi_E = -(lambda_E + 2 kappa'_m
Lambda R_E^2) + err.

Further digest (H1 notes, Part III 5.6):
- Lemma TF': if every near-certificate y (size <= eps_*) at rt_0 has <kappa y, rt'-rt_0> >= 4(||b(rt_0)|| + x) and rt' admissible with
  ||kappa(rt'-rt_0)|| <= Design^C(||b||+x)/u, then Step A at rt' is A-regular. (Generators Lipschitz in rt with C_G <= Design^C.)
- Lemma AL: y_l rt_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(...) for thick rows; kappa_y in [-C, -c_*/nu_1] for EVERY near-certificate.
- Lemma K: rho_d = m|r_d| K(sigma, R^2)/Phi_d, K increasing in R^2 (dK/dR^2 >= c_K > 0, K <= 8.5 on W-fix region); sigma = Phi_P^2 + s_f
  depends only on the peak PATTERN. kappa'_m := d log K/d R^2.
- Euler: kappa_m = sum_k zeta(k) d kappa_m/d zeta(k); route V: kappa_m = sum_P |zeta(c)| + S_m/theta_m; d kappa/d zeta(c) = vs_c(1-X_m) at
  peaks, |d kappa/d zeta(l)| <= C b^2 D^2 at coarse strict non-peaks.
- Thm 5.x (Aobs): coef_l = eps_l y_l - beta_m lambda_l d kappa/d zeta(l); kinds (i)-(iv); (iv): every near coordinate S_th of data sign,
  coef_l sigma_l >= -small.  kappa_Psi <= -c_*/nu_1.
- Theorems IN/OUT/GS/UC/RL, Lemma TG (linear groups: normal resonance P_{V_G} w^G small).
- Peak conversion (H1 7, SKETCH): freeze d as a peak with band row rho_d in [1+beta_*, 1+3beta_*]; gaps: non-robust frozen peak outside (FC),
  J2.1(e) margins, peak-error e_d <= t/(lambda_d mu_d), screening CM'(a).
