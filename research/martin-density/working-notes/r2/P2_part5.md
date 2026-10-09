# P2 part 5: numerical sanity checks (finite models; numpy + cvxpy/Clarabel). Scripts in ctx/r2/P2work/.

* check_clamp4.py / check_clamp5.py (Lemma 1.1). Random blocks (14 coordinates, Phi_k ~ 2^{-k}), the norming functional computed by a
  one-dimensional reduction (w = clip(mu zeta/Phi^2, -M, M), optimize over M) and certified by the primal block norm
  |zeta|_m = min{ max(||x||_1, ||beta||_2) : zeta = x + D beta } (SOCP): relative primal-dual gap <= 5e-8 in all 30 trials. On blocks
  whose strict non-peaks carry Hilbert weight >= 5% of C^2 (well-conditioned), the clamp identity mu |zeta|_m = C holds to 6.5e-7.
  (On blocks whose non-peaks have tiny zeta the multiplier mu is numerically ill-determined; the objective is still exact.)
  Caveat: a first attempt with the SUM primal ||x||_1 + ||beta||_2 gave a spurious 35% gap — the gauge of B_{l_1} + D(B_{l_2}) is the MAX;
  recorded because the same slip is easy to make elsewhere.
* check_thmC.py (Theorem 2.1 algebra in P1-referee's finite model of P1's example: base coordinate 0, 12 contacts, 10 free
  coordinates, one block of 7 coordinates with the special carrier u, u(zhat) = 0, w(1) = 0; mates g in E_u with non-constant theta(g)
  in [0, 0.15]). Construction exactly as in Thm 2.1 (window of 5 contacts with masses 4 rho s_1 |b_theta|, theta = 1/2, rho = 0.9,
  s_1 = 0.02), steering by a one-parameter path (raise: mass at contact 1; pull: partial move of the last contact, then a full flip of a
  far contact with negative mass) and bisection. Results for 6 seeds: steering reaches u(xhat') = 0 to 1e-16 and d' = 0 to 1e-16;
  max over 50 values t in +-[1e-3, 20] of p*(f' + t g') - s(t) is -5e-7 (= the solver offset; the same offset appears for the mates at f),
  i.e. (f', g') is contractive; (p*(f'+tg')-1)/t^2 <= 0.008 at |t| = 0.01, 0.03. Caveat: in a finite model every functional attains its
  norm and the true p* may use other decompositions, so the run checks the algebra of (2.1.2), the steering and the contractivity of the
  constructed pair, not the necessity of the construction (the unsteered pair is also contractive in the finite model).
