# Y3 referee, part 1: flip calculus, raised T8, one-sided coefficient, un-switching, Lemma 3.4 (first pass)

Sources checked: note (def:twopiece, prop:onesidedupper, thm:onesided, prop:lowerbound block test, def:engineered,
lem:approxfacts, thm:engineered, lem:budget, lem:suplevel, lem:flip, lem:boundedfree, lem:modswallow, lem:exactswitch,
lem:windowtwopiece, lem:onesidedtransfer, lem:avgfunctionals, def:SLD, thm:SLD), Z5 T8 (Z5_notes 4.3), Z5_ref_notes (R1, R2),
Z6_ref_notes Lemma 2.1 (inward-only coordinates), Z3_notes 5.1, Z3_ref_notes part 4 (explosive design).

## Lemma 1.1 (flip calculus): CORRECT (PROVED). Re-derived (a)-(d). Note m_beta is left-continuous; Exc_beta(r) = 2 int_0^r m_beta
by monotone convergence of partial sums (each summand Lipschitz). (c) needs a_j != 0 on F (true by definition of F).

## Lemma 1.2 (critical profiles oscillate): CORRECT (PROVED). Detail: m(y+) >= R_i (equality iff rho is injective at s_i); the
inequality direction is the favourable one. Infinitely many jump points accumulate at 0 because rho > 0 on S subset F and rho -> 0.
Restriction: rho nonincreasing along S (monotone profiles) and geometric v; stated.

## Theorem 2.1 (T8 with raised support): CORRECT (PROVED).
Checked against the note's thm:engineered and Z5's T8: the raise r_j := (8 rho s_1|b^theta_j| - |a_j|)_+ keeps sgn a''_j = s_j = z'_j,
so f' is NA with finite base support; ||a'' - a||_1 <= alpha(N_w) + 8 rho s_1||b^theta||_1 (window contacts and support coordinates are
disjoint); K_e becomes 2||U||(8 rho||b^theta||_1 + 1)/nu. (E2) is unchanged (xhat' - zhat = -z 1_(N'',inf) + U(e'-e), z' does not
depend on the raise). lem:F1, lem:anchor, lem:scrambling, (E4), (E5), Steps 1,2,4,6 use a'' only through (E1)-(E3) and convergence.
Step 3: theta piece (|tau| <= s_1): |tau rho beta^theta_j| <= rho s_1|b^theta_j| <= |a''_j|/8 < |a''_j|/4 <= s_j(1-tau rho c)a'_j:
no flip. +- pieces: the raise only increases |a'_j|; flip needs |a_j| < 4 rho|tau| beta_j, cost <= 2 rho|tau| beta_j. The |b^theta|
part of Z5's (CS-data) was used ONLY for theta-flips on F_{<=N_w}; hence superfluous. Remark (R1 requirement on bbar^theta
superfluous): correct.

## Theorem 2.2 (flip-extended T8): CORRECT (PROVED), two cosmetic points.
(i) the factor (1 + O(T_0 + s_1)) should read (1 + o(1)) along the construction sequence: |a'_j|(1 - tau rho c) >= |a_j|(1 - o(1))
because q*(a'') -> 1 and c -> 0; any such factor works once T_0 < t_0/rho strictly. (ii) the hypothesis rho^2 Gamma_w(b^theta,
omega^theta) < 1 is redundant (Gamma_theta <= max(Gamma_+, Gamma_-) by convexity). K_sharp exists because Fl(tau) <= C tau^2 for
|tau| <= t_0/rho when sup_{r<=t_0} Fl_r < infinity, which the hypothesis implies.

## Theorem 4.1 (one-sided coefficient at arbitrary F): CORRECT (PROVED).
Step 1 re-derived: k perp e, kappa = ||k||^2/(2q_0), k_2 = -kappa e, chi = Uk + chi_c, chi_2 = Uk_2 (in c_0), eta_t = xi + t chi + t^2 chi_2,
h_t = q_0 e + tk + t^2 k_2. Z_t := eta_t - U h_t = q_0 z + t chi_c (uses xi = q_0 z + q_0 Ue). ||h_t||^2 = (q_0 - t^2 kappa)^2 + t^2||k||^2
= q_0^2 + t^4 kappa^2. q**(Z + Uh) <= max(||Z||_inf, ||h||) because a'(Z + Uh) <= ||a'||_1||Z|| + ||U*a'|| ||h||. a(eta_t) = q_0 +
t<U*a,k> + t a(chi_c) + t^2<U*a,k_2> = q_0 - t^2 kappa nu (chi_c vanishes on F = supp a). So E_q <= t^2 nu||k||^2/(2q_0) + O(t^4).
The note's block test (prop:lowerbound) accepts ANY chi_2 in X (it enters only through q(chi_2) in the overshoot bound and through
w(t^2 delta_2), which cancels in E_m), so Steps 2-4 go through; strong duality has no F-constraint (C_+ vanishes on F).
(c): G_b(a + tb) = Exc_{(sb)_-}(t) + nu Psi; prop:rebalancing needs Exc = O(t^2) for |eps_m| <= K_3 t^2; transfer data
(lem:transferdata) need no finiteness of F. (d), (e) follow. The remark that the Gram system was the only use of F finite in the
lower bound: correct.

## Lemma 3.1 (un-switching pair): CORRECT (PROVED). Re-derived: R_m* e_k = lambda_l u_l, d_m(e_k) = Phi^2 w(k)/C = 0, u_l(xi) = 0
(off P, w(k) = C zeta(k)/(Phi^2 sigma), zeta(k) = lambda_l xi(u_l)), h(u_l) <= ||U||^2/nu, H_m(e_k/lambda_l) <= 1/(m^2 C_m).
Side admissibility of the added base part c u_l needs supp u_l subset F (or z-compatible signs off F) -- used correctly in 3.5.

## Lemma 3.4 (constrained-switching bound): CORRECT (PROVED), constant 32 can be 16.
(a): (D/2) m^{>l_*}(tD/4) <= sum_F(f^+ + f^-) + sum|r| <= t/(2q_0) + (4/3)6t^2, i.e. D m <= t/q_0 + 16t^2. (D1)(c) is exactly what
removes the targets of l' in (l_0, l_*] from S_{l_0} cap (l_*, inf); coarser targets vanish by allowedness (a). (b) case split OK
(C_Q >= 1 WLOG). (c): use D' = eta_1/2 < D^#(t_n) (the set {D' : D' m(tD'/(4C_Q)) <= ...} is an initial interval). K_sigma(l) T_hi(l)
<= C_f 2^{l + G_0} 2^{-l^3} -> 0.
