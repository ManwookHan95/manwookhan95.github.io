# U3 part 5 — Numerics (finite SOCP models; sanity checks only)

Scripts in r8/U3_work/ (cvxpy 1.9.3 with CLARABEL; double precision).  Finite models are always block-tame, so they cannot show
failure of recovery; they test the EXACT finite-dimensional statements (Lemma S / Proposition S3 / Theorem NL mechanism, Lemma QB2).

Model (nl_check.py): N = 1, m = 1 (lambda = Phi), F = {0, 1} (a > 0), all other coordinates contacts; carriers
 c1: target e_2, signature {3,4,5}, z = +1  (robust swallowing-type peak, val = 0.803);
 c2: target e_6, signature {7,8},  z = -1  (robust swallowing-type peak, val = -0.941);
 lm: target y* = (e_0 - e_1)/q*, signature {9,10}, z = +1; the ratio a_0/a_1 is tuned so that val = -0.002 (anti-type strict non-peak,
     q < 0, nu/theta small);
 o : target y*, signature {11,12} with weight delta = 0.02; z = -1 in f (aligned peak, val = -0.165), z = +1 in f_n (ANTI-TYPE peak,
     val = -0.135).
 Phi = (0.3, 0.1, 0.03, 0.01), signature weights 2^{-(s - s_0) - 1}, diagonal base s_j as in the script.
Results (nl_check2.py):
 * f and f_n have the same peak/non-peak pattern (P = {c1, c2, o}, Q = {lm}); p*(f_n - f) = 8.3e-7.
 * psi = R^* w is z-signed on all signature coordinates of f; at f_n it is anti-aligned on S_o (z psi = -7.5e-5, -3.7e-5).
 * The coherent-shift mate g of f (V4 Prop. 3.2 with chi = 1 at s_1 = 3 and 0 at s_2 = 4): V z-signed off F (min z V = 3e-7 > 0);
   profile pi_g = (2.35e-4, 0, 1.17e-4) on S_c1 (non-constant); p*(f + t g) <= s(t) on the grid |t| in [1e-3, 10] (max excess -5e-7).
 * One-sided coefficients of g (SOCP over side-admissible pairs): at f gamma^+ = 4.1e-9, gamma^- = 8.6e-4 (both finite); at f_n
   gamma^+ = +infinity (INFEASIBLE), gamma^- = 8.6e-4.  So g is not a mate of f_n at any scaling (Theorem thm:onesided at the
   block-tame f_n), as Proposition S3 predicts.
 * Maximum of pi_h(s_1) - pi_h(s_2) over all h carrying two-piece data with kappa_w <= 1: 1.60e-2 at f, 2.4e-8 at f_n (the residual is
   the difference psi_n - psi at s_1, s_2).  The oscillating part of the local fibre collapses under a far anti-type flip of norm 8.3e-7:
   the finite-dimensional shadow of Theorem NL.
 * (nl_check.py, direct grid relaxation of C(f)) — inconclusive: the SOCP over 2 x 46 scales is not accurate enough at |t| <= 1e-3
   (non-monotone values when constraints are added), and the relevant scale of the effect here is ~1e-8; the exact two-piece
   computation above is the reliable test.
Lemma QB2 (vt_check.py): the same model plus a contact j_0 touched by no carrier (a dead zone, psi(j_0) = 0); g := 0.25 x (shift mate),
g_e := g - eps e_{j_0} rebalanced by a multiple of a (so g_e(xi) = 0), rho = 0.9, grid |t| in [1e-5, 10] (97 scales per sign).
 eps      | max_t [p*(f + t rho g_e) - s(t)] | least bank mass m with rho g_e in C_grid(f_m) | m/eps^2 | p*(f_m - f)
 4.0e-3   | +2.0e-5                          | 1.33e-5                                        | 0.83    | 2.7e-5
 2.0e-3   | +4.5e-6                          | 3.16e-6                                        | 0.79    | 6.3e-6
 1.0e-3   | +1.0e-6                          | 7.50e-7                                        | 0.75    | 1.5e-6
 5.0e-4   | +2.4e-7                          | 1.78e-7                                        | 0.71    | 3.5e-7
The violation is fatal at f (positive excess), a bank of mass ~ rho^2 eps^2 (prediction 0.81 eps^2 for kappa_w ~ 0; the mass grid has
ratio 10^{1/8}) repairs it, and the companion moves by ~ 2 m: the quadratic law of Lemma QB2.
Consistency with Lemma VT: at this contact b^+(j_0) = b^-(j_0) = -eps (side + violated, viol(j_0) = eps, b^theta(j_0) = -eps); the engineered
approximant of Lemma VT carries there the window mass 4 rho s_1 |b^theta(j_0)| with s_1 >= 32 rho eps/delta, i.e. >= 128 rho^2 eps^2/delta
(about 2e2 eps^2 here, delta ~ 1/2): the same quadratic law with a non-optimised constant, above the observed least masses (~0.75 eps^2),
as it must be (Lemma VT is a sufficient condition).
