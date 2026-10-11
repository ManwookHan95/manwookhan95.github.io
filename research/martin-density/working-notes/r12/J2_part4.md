# J2 part 4 (Round 12): numerics (sanity checks only; finite one-block Martin-type models)

Scripts and outputs in r12/J2_work/.  A finite model cannot exhibit an infinite-dimensional failure; these checks only test the finite
identities and inequalities used in Lemma J2.0, Lemma J2.1 and Theorem J2.1, Step (iii).

## frozen_check.py -> frozen_check.out (mpmath, 50 digits; 40 random blocks: 2 robust peaks, 2 weak peaks with rho in (1, 1 + b),
## b = 1e-3, 4 strict non-peaks, 3 fine carriers; true threshold theta = 1 by construction)
 - construction check |theta_true - 1| <= 5.3e-51.
 - Lemma J2.1(e): theta_f <= theta always; (theta - theta_f)/(theta b Phi_W^2/Phi_Pf^2) <= 0.865 (proved bound: 3).
 - Lemma J2.1(d) (frozen Lemma K): a_f^2 - sigma_f - k_f^2 R^2 <= 6.7e-52; k_f - a_f - sigma_f <= 8.4e-52; k_f - K(sigma_f, R^2) <= 3.3e-51;
   rho^f_l - m|r_l| K/Phi_l <= 2.7e-51 (Omega = all coarse non-P_f carriers, weak peaks included).
 - Frozen statuses of the weak peaks at the start: max rho^f - 1 = 6.5e-3 (bound (1 + b)(1 + 4b Phi_W^2/Phi_Pf^2) - 1; Phi_W/Phi_Pf up to 5 here).
 - Realization A (direct push of both weak peaks to frozen rho = 1 - mu/2, mu = 0.02, solved by bisection on a common scale): the frozen
   pattern is consistent and theta_f = theta_true, A_f = A_true exactly (difference 0 at 50 digits): Lemma J2.1(c).
 - Realization B (threshold raise: raise the robust peak 0 until both weak peaks have frozen rho <= 1 - mu/2): consistent, theta_f = theta_true
   exactly.  (The finite raise is far from first order at mu = 0.02 -- relative raises of |zeta_0| up to O(1) because a = A/theta is small;
   the first-order check is in frozen_check2.)
 - Lemma J2.0 (true block): d theta/d|zeta_j| finite differences vs formula, relative error <= 5.4e-17 (h = 1e-25 |zeta_j|); Euler identity
   sum_j (d theta/d|zeta_j|) |zeta_j| = theta to 8.0e-51.

## frozen_check2.py -> frozen_check2.out (double precision; 200 random blocks)
 - (A) Lemma J2.0 for the FROZEN pattern: d theta_f/d|zeta_j| vs A_f/(Phi_Pf^2 (A_f + theta_f)) (j in P_f) and -nu_j/(Phi_Pf^2 (A_f + theta_f))
   (j in Q_f): relative error <= 7.6e-7 (central differences, step 1e-7).
 - (A') first-order threshold raise needed to lower log rho of a weak peak by 1e-6: dZ = eps theta_f Phi_Pf^2 (1 + a_f)/a_f confirmed to 8.4e-7
   relative.
 - (C) Lemma J2.1(d) derivatives of kappa_f (Omega = all non-P_f carriers but one, so s_f > 0): d kappa_f/d|zeta_l| = rho_l s_f/(Phi_Pf^2 (1 + a_f))
   (l in Omega) and 1 - a_f s_f/(Phi_Pf^2 (1 + a_f)) (p in P_f): absolute error <= 1.2e-6.
 - (B) Along a path moving a weak peak across the TRUE threshold, the formula-1 kappa with the TRUE (A, theta) has a derivative jump up to
   0.95 (reproduces K2-ref K-8, ref_kappa_jump), while the frozen kappa_f (target pattern) has jump <= 6.2e-8 (= O(h), smooth).
 - (B) On the consistent side (all frozen non-peaks below threshold) |theta_f - theta|/theta <= 8.7e-16.
## merged_stepA_toy.py -> merged_stepA_toy.out (double precision; 300 one-block toys)
 Block: robust peak p (two-sided), active WEAK PEAK k (rho in (1, 1 + b), b = 1e-3) with a ONE-SIDED resource (|zeta_k| may only increase --
 the bad case of K1-ref R-8: eps_k = vs_k, no pull), active strict non-peak l (two-sided), inactive carrier n held at 0.  Targets: r''_l = current,
 r''_k with frozen floor status 1 - mu/2 (mu = 0.02).  Realized from the UNPUSHED row with (FC) by raising the peak (kappa/threshold lever;
 by 1-homogeneity the realized configuration is the scale-s* multiple of the solution at s = 1) and letting k, l follow: 300/300 realized
 points are (FC)-consistent, |theta_frozen - theta_true|/theta <= 1.1e-15, the one-sided constraint on k holds, the TRUE status of the former
 weak peak is exactly 1 - mu/2, and the peak raise used is <= 1.05e-2 relative (~ mu/2 + b).  This is K1's ratio trick (K2.17(g)) in the
 merged Step A: a weak peak without any push resource is realized inside Step A whenever its block has a threshold/kappa lever and the
 other carriers can follow.
## lemmaJ21e_adversarial.py -> lemmaJ21e_adversarial.out (double precision; 20000 random blocks with weights in [1e-3, 0.3],
## 1-3 robust peaks, 1-5 weak peaks, 0-5 non-peaks, b in [1e-6, 1e-1]; kept only blocks satisfying the hypotheses of Lemma J2.1(e))
 16834 admissible blocks: 0 violations of Psi_f(0+) > 0, theta_f <= theta, theta - theta_f <= 3 b theta Phi_W^2/Phi_Pf^2 (max ratio 1.06),
 |A_f - A| <= 4 b theta Phi_W^2/Phi_Pf^2 (max ratio 0.004).
## frozen_c11_check.py -> frozen_c11_check.out (double precision; 150 blocks with 2 robust peaks, 2 weak peaks, 4 non-peaks, 3 fine
## carriers; paths pushing the weak peaks across the TRUE threshold, t in [3e-4, 1e-2])
 Frozen kappa_f (FC): max |g(t) - g(0) - t g'(0)|/t^2 = 1.2e-5 (bounded: C^{1,1}, as K2.9(c) needs).  True formula-1 kappa at the 506 path
 points beyond a crossing: max |k(t) - k(0) - t k'(0+)|/t^2 = 1.2e2 (first-order kink: the remainder bound C_2 t^2 fails without freezing).
Conclusion (sanity only): the frozen system with the target pattern is smooth across the threshold crossings that Step A performs, it
coincides with the true block at consistent points, and it satisfies Lemma K exactly -- the three properties Theorem J2.1 uses.
