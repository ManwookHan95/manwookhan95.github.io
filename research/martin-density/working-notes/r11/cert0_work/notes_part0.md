# cert0 working notes, part 0: source map (read so far)

Sources read: MTVI_graph.md; Q1_notes 1.1-1.3, 2.0-2.3; X1_notes 1-2.6 (all), X1_ref_notes (all); X2_ref_notes (all);
Q1_refa_notes (all); Q1_refb_notes (all); U1_ref_notes (all); U1_notes parts 1-4 (Lemmas 1.1-1.5, 2.1-2.4, 3.1-3.5, 4.1-4.6).

Key objects:
- Block m at a first row: zeta = R_m^** zhat, A = |zeta|_m, M + C = 1, theta = AM/C, nu_k = m|u_k(zhat)|/Phi_k, rho_k = nu_k/theta.
- kappa(Omega) = [A(A+theta) - sum_Omega nu^2 Phi^2]/theta = A + theta Phi_P^2 + S_f/theta  (formula 1; S_f over Q\Omega).
- Lemma R-kt: a^2 = Phi_P^2 + k^2 R^2 + s_f, k = a + Phi_P^2 + s_f, rho_l = m|r_l|k/Phi_l, R < 1.
- Lemma K: k = K(sigma, R^2) = [sigma + sqrt(sigma^2 R^2 + sigma(1-R^2))]/(1-R^2).
- K1 (Omega meets P): sigma' = Phi_{P\Omega}^2 + sum_{Omega∩P}(1-rho^2)Phi^2 + s_f.
- Lemma 1.1 (U1): V(Domega) = sum_l gamma_l u_l, gamma_l = lambda_l(Domega(l) - Delta_m w(l)); outside Omega forced -Delta lambda w.
- Lemma 1.3: Delta'_m kappa_m = sum_{Omega_m} u_l(zhat) gamma_l.
- Lemma 4.1 (U1): owner recursion; config (i) self-aligned => |u_k(zhat#)| >= ||v_k||_1 = delta_k H_k/n_k => peak, margin >= q0 delta_k H_k/(2n_k).
- Lemma 4.2: dominance owner coefficient vs later carriers: (i) signature coords via (W4') and (ii) target coords via n(k) >= Design(k) >= 1/(eta_k lambda_k).
- Lemma 4.3: (SC): Scr_m(x) <= sum_{a_k <= X} a_k^2 <= 2X^2, X = 2 n_k x/q0.
- Lemma 4.5: cost; Lemma 4.6: Delta'' = Delta' kappa'/kappa^# (config (ii)); trace correction (Delta''-Delta')P_m on E_c.
- CM' (X2-ref 4): route-V companion: (1a) KN, (1c') restore kappa + Omega_act values, no absorber tuning; (2') G1 release + static ownership
  on J_fine with owners (a) Omega_act, (b) coarse peaks of active blocks, (d) every carrier at stage > L of an active block; negative fine owners
  self-aligned, positive anti-aligned; unowned z := 0.

TODO: U1 part 5 (Lemmas 5.1-5.4: mixed classes, frustration), V1 Lemma TU/TR/ST/CO; Part II lem:II-recursion, domfine, SCi, coststat,
trueshift; X2_notes CM, C_mix; Q1_refa_part2 (C1-C4); Q1_refb_part3; Part I def:SC, lem:scrambling, kinds [1]-[3] (Y1 Prop 5.2 / V1 TR).
