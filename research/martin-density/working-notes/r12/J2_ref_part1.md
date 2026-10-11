# J2-ref part 1: Lemma J2.0 and Lemma J2.1 (frozen block system) -- re-derivation and numerics

Setting and notation of r12/J2_notes.md (one block m; zeta_k = lambda_k u_k(xhat), lambda_k = m Phi_k; threshold equation of
Y2 Lemma T: theta is the unique zero of Psi(th) = A(th)^2 - B(th), A(th) = sum_k (|zeta_k| - th Phi_k^2)_+, B(th) = sum_k Phi_k^2
min(th, nu_k)^2, nu_k = |zeta_k|/Phi_k^2; rho_k = nu_k/theta; P = {rho >= 1}).  Scripts: r12/J2_ref_work/.

## 1.1 Lemma J2.0 (first-order action on relative positions).  Verdict: CORRECT (one harmless slip in consequence (b)).
Re-derivation.  At the true root, for j in P the A-term is |zeta_j| - theta Phi_j^2 and the B-term theta^2 Phi_j^2 does not depend on zeta_j:
dPsi/d|zeta_j| = 2A.  For j in Q the A-term is 0 and the B-term is zeta_j^2/Phi_j^2: dPsi/d|zeta_j| = -2 nu_j.  dPsi/dth = -2A Phi_P^2 -
2 th Phi_P^2.  Hence d theta = [A sum_P d|zeta_j| - sum_Q nu_j d|zeta_j|]/(Phi_P^2 (A + theta)).  Euler: sum_P |zeta_j| = A + theta Phi_P^2
(from A = A(theta)) and sum_Q nu_j |zeta_j| = A^2 - theta^2 Phi_P^2 (from A^2 = B(theta)); the numerator at d|zeta| = |zeta| equals
theta Phi_P^2 (A + theta).  d log rho_k = d log nu_k - d log theta.  All as stated.
Consequence (a) (threshold raisers).  Raising a peak p: d theta/d|zeta_p| = A/((A + theta) Phi_P^2) > 0; lowering a strict non-peak q:
d theta/d|zeta_q| = -nu_q/((A + theta) Phi_P^2) < 0.  Both multiply every OTHER relative position of the block by theta/theta'.
Size: a relative raise 3b of theta needs d|zeta_p| = 3b theta Phi_P^2 (1 + a)/a.  With the alpha-mass identity a = A/theta =
sum_{k in P} (rho_k - 1) Phi_k^2 (from A = A(theta)) one has a >= u Phi_p^2 for a robust peak, and theta = A/a <= Design(L)/u, so the value
change is <= Design^C b/u^2 (value units) and the relative change of kappa is <= 6b/a <= Design^C b/u (ratio units).  CORRECT; the u^2 in
value units is genuine (theta can be as large as Design/u).  For a NON-PEAK threshold raiser l (rho_l >= u) the own ratio r_l moves by
|dr_l| <= C Design b/rho_l <= Design^C b/u in ABSOLUTE ratio units (relative change ~ b/rho_l^2): inside R-8(ii)'s radius.  [Checked.]
Consequence (b), SLIP (harmless).  J2 writes "the bracket 1/|zeta_k| - a/(theta Phi'^2 (1 + a)) is >= (1/(theta Phi_k^2 rho_k))(1 - a/(1 + a))".
Correct: since Phi_k^2 <= Phi'^2 (k in P), the bracket is >= (1/(theta Phi_k^2))(1/rho_k - a/(1 + a)) = (1 - a(rho_k - 1))/(theta Phi_k^2 rho_k (1 + a))
>= (1 - b)/(theta Phi_k^2 rho_k (1 + a)) > 0 for rho_k <= 1 + b, a <= 1.  The stated bound is too large by the factor 1/(1 - a(rho_k - 1)) <= 1/(1 - b).
Positivity (the only use) holds.  An own push from rho <= 1 + b to 1 - b needs d|zeta_k| <= 2b theta Phi_k^2 rho_k (1 + a)/(1 - b) <= 5 b theta Phi_k^2,
i.e. <= 5 b theta Phi_k/m in u-units (J2: 3b; X1: 2b): constants only.

## 1.2 Lemma J2.1 (frozen block system).  Verdict: CORRECT (one constant slip in (b)).
(a) PROVED.  On (0, th_max) the P_f-terms of A_f decrease with slope -Phi_k^2, fine terms are nonincreasing: A_f > 0 strictly decreasing.
B_f' = 2 th (Phi_{P_f}^2 + fine peaks' Phi^2) > 0.  So Psi_f strictly decreasing there; th_max <= sum_{P_f ∪ fine} |zeta|/Phi_{P_f}^2 < infinity,
Psi_f(th_max) = -B_f(th_max) < 0; Psi_f(0+) as stated (min(th, nu)^2 -> 0).  Unique zero in (0, th_max) iff Psi_f(0+) > 0.  NOTE (not an
error): beyond th_max, A_f < 0 and A_f^2 - B_f can vanish again; the frozen root is DEFINED as the zero in (0, th_max), which is the one
that coincides with the true root at consistent points ((c)).
(b) PROVED, with a constant slip.  1-homogeneity: the three equations are invariant under (zeta, th, A) -> c(zeta, th, A).  Smoothness: the
P_f-terms are linear in |zeta_k| (zeta_k != 0 on P_f), the Q_f-terms of B_f are zeta_k^2/Phi_k^2 (polynomial, smooth through zeta_k = 0),
|dPsi_f/dth| = 2(A_f + th) Phi'^2 >= 2 theta_f Phi_{P_f}^2; implicit function theorem.  SLIP: at a fine status change the gradient of Psi_f
in (|zeta_k|, th) jumps by 2(A_f - th)(1, -Phi_k^2) (computed: A-term jump (1, -Phi_k^2) times 2A_f, B-term jump (2th, -2th Phi_k^2)).
In move units d|zeta_k| = m Phi_k d|u_k|, so the derivative of theta_f (and kappa_f) along a move jumps by O(Phi_k/(theta_f Phi_{P_f}^2)) =
O(Design Phi_k): the kink part is Lipschitz with constant <= C Design sum_{fine} Phi_k <= C Design c_{L+1}, not "C sum_{fine} Phi^2".  The final
bound "C c_{L+1}" (K2-ref K-8) holds up to the factor Design(L); in K2.9(c) one needs C Design c_{L+1} W <= rho_0/2 = C_2 W^2/2, true since
W >= Design^{C_A} x >= Design eta' >> c_{L+1} (c_{L+1} <= exp(-1/T), (W_exp)).  No conclusion changes.
(c) PROVED.  Under the consistency hypothesis each frozen term equals the true term at th = theta_f (P_f: (|zeta| - theta_f Phi^2)_+ =
|zeta| - theta_f Phi^2 and min(theta_f, nu)^2 = theta_f^2; Q_f: (.)_+ = 0 and min(theta_f, nu)^2 = nu^2), so Psi(theta_f) = 0 and theta_f = theta
by uniqueness of the true root (Y2 Lemma T(c)); A_f = A(theta) = |zeta|_m (Lemma T(b)).
(d) PROVED.  Re-derived: A_f^2 = B_f(theta_f) gives A_f^2 - S_Omega = theta_f^2 (Phi'^2 + s_f); nu_l Phi_l = m|u_l|, so S_Omega = kappa_f^2 R^2;
a_f^2 = sigma_f + k_f^2 R^2, k_f = a_f + sigma_f (definition of kappa_f), R < 1 (a_f > k_f R, k_f > a_f), admissible root K(sigma_f, R^2).
Derivatives with fixed statuses (differentiating G1 = A - A_f(th), G2 = A^2 - B_f(th)): for l in Omega, dth = -nu_l/(Phi'^2(A + th)),
dA = nu_l/(A + th), d kappa_f = (nu_l/(A + th))(sigma_f/Phi'^2 - 1) = rho^f_l s_f/(Phi'^2 (1 + a_f)); for p in P_f, dth = A/(Phi'^2 (A + th)),
dA = th/(A + th), d kappa_f = 1 - a_f s_f/(Phi'^2(1 + a_f)).  Numerics: identities to 1e-40, derivative formulas to 3e-22 (finite differences
at 40 digits, Newton-solved frozen system), see 1.3.
(e) PROVED.  Re-derived line by line: A_f(theta) - A = -theta sum_{W'}(rho_k - 1)Phi_k^2 in [-b theta Phi_{W'}^2, 0]; B_f(theta) - B(theta) =
theta^2 sum_{W'}(rho_k^2 - 1)Phi_k^2 in [0, 3b theta^2 Phi_{W'}^2]; Psi_f(theta) in [-b theta Phi_{W'}^2 (2A + 3theta), 0]; Psi_f(0+) >=
2A theta(Phi_{P_f}^2 - b Phi_{W'}^2) + theta^2(Phi_{P_f}^2 - 3b Phi_{W'}^2) > 0; on [theta/2, theta], A_f >= A/2 and |Psi_f'| >= (A + theta)Phi_{P_f}^2,
Psi_f(theta/2) >= theta[(A + theta)Phi_{P_f}^2/2 - b Phi_{W'}^2(2A + 3theta)] > 0 (uses (2A + 3theta)/6 <= (A + theta)/2); with
x := b Phi_{W'}^2/Phi_{P_f}^2: theta - theta_f <= 3 theta x; |A_f - A| <= Phi'^2 (theta - theta_f) + b theta Phi_{W'}^2 <=
4 theta x (Phi'^2 <= 1, Phi_{P_f}^2 <= 1); rho^f_k = rho_k theta/theta_f <= rho_k(1 + 6x); kappa: |d kappa/dA| <= 3 (a <= 1), |d kappa/dth| <= 4 on
the segment, so |kappa_f - kappa(Omega)| <= 24 theta x.
Numerics (sanity): ref_frozen_indep.py (40 digits; true block cross-checked against an independent water-filling solution of the dual norm
program, A to 9e-16, theta to 7e-8; frozen system by Newton on (G1, G2)): 389 admissible blocks, theta_f <= theta always, max ratios 0.35 (of
3x), 0.0005 (of 4x), C = 0.17 for kappa; frozen Lemma K to 1e-40; W-fix region 1 - R^2 >= sigma_rob/2 always; Step (i) floor inequality
psi_d(r_0)/Phi_d <= rho^f_d always, rho^f_d - 1 <= 0.93((1 + b)(1 + 6x) - 1).  ref_boundary_e.py: 20000 blocks AT the boundary of the
hypotheses (b = (0.9..1) Phi_{P_f}^2/(6 Phi_{W'}^2), all weak peaks at rho = 1 + b): 0 violations; max ratios 0.38 and 0.0004.

## 1.3 Summary of part 1
Lemma J2.0: CORRECT (slip in (b)'s explicit lower bound; positivity holds).  Lemma J2.1 (a)-(e): CORRECT (constant slip in (b): fine kinks
contribute C Design c_{L+1}, not C sum Phi^2; immaterial).  Both confirmed numerically with an independent implementation.
