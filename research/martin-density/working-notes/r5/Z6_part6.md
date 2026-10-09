# Z6 part 6: finite-model numerics (scripts in r5/Z6_work: toy.py, exp_module.py, scan_module.py)

Model (toy.py): R^26, base q*(A) = ||A||_1 + ||U^T A||_2 (U 26x4, rows decaying like 2^{-0.3 j}), one block (m=1) with 6
carriers u_k = y_k + 0.15 h_k (h_k on 3 private signature coordinates, weights 2^{-1..-3}); five strong peaks of BOTH
signs (u_k(xi)/threshold = 14.4, -20.5, 55.9, -68.2, 77.9) and one module carrier l with y_l >= 0 off F = {0} and y_l(0)
tuned so that w(k_l) = kappa*M (strict non-peak, gap = (1-kappa)M, q_l = Phi_l w(k_l)/C > 0, uncompensated).
MAXIMAL CONTACT: a = e_0/q*(e_0), z = 1 on all coordinates.  p* is computed exactly (SOCP, Clarabel).
Module mate g = c (u_l - q_l L^* w) (balanced: |g(xi)| < 1e-7).  For each scale t in [3e-3, 0.5] we check
p*(f +- t g) <= s(t), and compute the MINIMAL switching |Delta theta_l| over pairs of decompositions of f+tg, f-tg whose
max(q*, N) is at most p*(f -+ t g) + 0.05 t^2 ("forced switching"), and the extreme signed switching ("spurious").
Finite models are degenerate (all functionals attain their norm); these runs test only the local multi-scale geometry.

Results.
(R1) Band structure (Phi_l = 2e-3, kappa = 0.5, c = 0.02): mate at all t; forced switching = 0 (to 1e-11) for
     t <= 0.046, positive on t in [0.065, 0.18] (max 6.4e-3, sign = the resonant direction tau > 0), and 0 again for
     t >= 0.25.  Spurious switching up to 0.5 in the resonant direction is allowed at small t (box freedom).  This
     confirms: two-sided carrier usage below the radius ~ gap lambda/c, switching in a band, base on both sides above.
(R2) Transience/scale (Phi_l = 2e-4): c = 0.02 valid with max forced switching/t = 0.99; c = 0.03 and 0.05 are NOT mates
     (the - side fails on t in [8e-3, 9e-2], max excess +1.0e-3): the validity threshold c^2 <~ 2(M + w)lambda/m_u
     (m_u := ||u_l 1_{F^c}||_1 = 0.73) predicted by the module geometry (part 5) is matched within a factor ~2.
(R3) Dependence on the gap (Phi_l = 2e-3), max over t of forced switching/t at valid c:
       kappa=0.10 (gap 0.85, nearly neutral, q=3.5e-3): <= 0.034 (c=0.04 valid, 0.07 invalid);
       kappa=0.50 (gap 0.47, q=1.7e-2): 1.21 at c=0.07;
       kappa=0.90 (gap 0.092, q=3.1e-2): 6.4 at c=0.07 (c=0.085 invalid);
       kappa=0.98 (gap 0.020, q=3.4e-2): 23.9 at c=0.085 (still valid; maximum at the smallest grid scale).
     Empirical law: max forced switching/t ~ c^2/(4 gap lambda_l) (checked: ratio 3.0 for c 0.04 -> 0.07 vs 3.06
     predicted; prefactor 1/4.3 for kappa = 0.5), hence <= (M + w)/(2 gap m_u) at the validity limit.
     Near-threshold carriers with q > 0 produce forced switching >> t (unbounded as gap -> 0 relative to m_u), but
     always <= K_d t/q_l with q_l ~ M Phi_l/(m C) (Prop. 3.4), consistent with 24 vs 1/q ~ 30 K_d-scale.
     Nearly neutral carriers (large gap) produce forced switching << t.
Reading [HEURISTIC]: transient (uncompensated) switching through a swallowed carrier at scale t is bounded by
 min( c_1 M t/(gap_l m_u(l)) , K_d t/|q_l| ),  and |q_l| >= M_m Phi_l/(2 m C_m) when gap_l <= M_m/2,
so it is controlled by DESIGN quantities (1/Phi_l when gap <= M/2, 1/m_u(l) <= n_l/delta°_l-type when gap > M/2), never by
f-dependent rates.  The second bound is PROVED (Prop. 3.4 with Delta d pinned); the first is only supported by the
module geometry and these numerics (Conjecture G in the notes).
