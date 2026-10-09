# Y4 part 3 — Finite-model numerics (scripts in ctx/r6/Y4_work/)

Model (toy.py, copied from r5/Z6_work): X = R^n, q*(A) = ||A||_1 + ||U^T A||_2, one block with carriers
u_k = y_k + 0.15 h_k (private signature coordinates), N_m(W) = ||W||_inf + ||D W||_2, p* by SOCP (Clarabel).  Finite
models are DEGENERATE (every functional attains its norm, every fibre is locally robust); they test signs, first-order
formulas and multi-scale profiles only, never recoverability.

## N1 (n1_channels.py): channel signs and the raising derivative.  CONFIRMS Lemma 2.6 and Proposition 2.8.
n = 40, F = {0,1}, maximal contact with random contact signs, 300 random z-signed W per base.  Quantity: first-order effect
of a unit mass at a contact j on W(zhat), i.e. z_j h_W(j)/nu, h_W = U P^perp U^T W.
 * diagonal U (U^T e_j = s_j k_j):  min_j z_j h_W(j) = 0.000 (never negative): masses only RAISE z-signed functionals;
 * mixing U (U^T e_j = s_j(k_j + (-1)^j 0.6 g)): 46% of the contacts lower W(zhat); min -0.43;
 * random U (rank 6): 48% lowering contacts; min -1.49.
 * raising derivative d/dm W(zhat(a + mW)) vs ||P^perp U^T W||^2/nu: max relative error 2e-8 (all three bases).
Reading: the directional obstruction of Proposition 2.8(b) is real for diagonal bases and absent (to first order, for a
single W) for generic bases.

## N2 (n2_lsc.py): fibre along tuned rows (sanity).  Maximal contact, F = {0,1}, nearly neutral carrier (kappa = 0.05,
q_l = 1.5e-3 > 0), module mate g = c(u_l - q_l L^*w), c = 0.06 (largest valid on the grid), rho = 0.99, scale grid
1e-5..3 (both signs) plus the exact first-order condition h(xi') = 0.
 bank-raise (a' ~ a + mW): cost 3.0e-2 / 1.5e-2 / 7.5e-3 -> dist(rho g, C(f')) = 2.2e-5 / 1.1e-5 / 5.9e-6;
 F-tune to exact neutrality (u_l(zhat') = 8e-17): cost 2.3e-3 -> dist 4.4e-6.
So dist ~ 7e-4 x cost: lower semicontinuity holds trivially in the finite model (degenerate, as expected); no rate
phenomenon can appear in finite dimension.  (The lowering family (C) was not reached within the mass range tried.)

## N3 (n3_ray.py, n3_scan.py): the directional residual (UN+) — switching along a tiny positive ray.
Construction: maximal contact, F = {0}; carriers l1 (q1 > 0) and l2 (q2 < 0), neither z-signed alone; their combinations
mu1 u1 + mu2 u2 are z-signed exactly for mu2/mu1 in [1/2, 2]; extreme rays A (D_A = q1 + q2/2 ~ 1.6e-2, robust) and B
(D_B = q1 + 2q2 = eps_rel |q2|, tiny); NO ray with negative d-sum (uncompensated: the configuration (UN+) of 2.4).  Mate:
ray module g = c(V_B - d-correction).  Measured: min over two-sided decompositions with the TRUE cap s(t) of
(|tau1| + |tau2|)/t (forced switching), at the largest valid c.
 eps_rel = 1:     c_max = 0.024, max_t forced/t = 1.54e-2 (band t in [2.6e-2, 7.1e-2], zero elsewhere)
 eps_rel = 0.1:   c_max = 0.026, max_t forced/t = 1.45e-2
 eps_rel = 0.01:  c_max = 0.026, max_t forced/t = 1.38e-2   (D_B = 8.6e-5)
 eps_rel = 0.001: c_max = 0.026, max_t forced/t = 1.37e-2
At c = 0.02 the forced switching is 0 (< 1e-10) at all 14 scales.
Reading (HEURISTIC): the forced switching through a nearly neutral positive ray is a transient band of height ~1.4e-2
(t-relative) that does NOT grow as its d-sum D_B -> 0 (three decades), whereas the method's pinning bound (Z6 2.4 /
Lemma 1.8) is ~ K/D_B.  The size is set by mate validity (c_max) and gaps (here 0.38, 0.66), i.e. by design-type
quantities.  This is evidence for a RAY version of Z6 Conjecture G and suggests that (UN+) is an artifact of the bound,
not of the geometry.  Caveat: finite models cannot exhibit persistence across infinitely many levels.
