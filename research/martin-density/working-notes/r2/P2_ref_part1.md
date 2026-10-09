# P2 referee — part 1: line-by-line verification of the PROVED core (claims 1-5)

Setting checked: canonical base q, finite block set I (p_N), only Lemma B's conclusion about T (+ (T3), (T4) from Preprint B /
Martin Prop 3). Imports re-read: A Facts A-F, Lemmas 4.2-4.4, 4.7, Prop 4.5, Lemma 1.4-1.5 of P2_part1.

## 1.1 Three-regime theorem (P2x 5.1 = P2_part1 1.4 + 1.5). VERDICT: PROVED (correct; content is in the hypotheses).
Re-derived: for |t| <= s_J all h_j use (i); for s_J < |t| <= T_0 the j with s_j < |t| use (ii)+(iii):
p*(f'+t h_j) <= p*(f'+t gbar) + |t| kappa s_j, and sum_{s_j<|t|} s_j < 2|t| (geometric, ratio 1/2), so the average is
<= 1 + Qt^2/2 + 2 kappa t^2/J. p*(g'-gbar) <= (kappa/J) sum s_j <= 2 kappa s_1/J. Assembly (Lemma 1.4): for |tau| <= T_0,
1 + (tau^2/2)(1-delta) <= 1 + tau^2/2 - tau^4/8 <= s(tau) needs tau^2 <= 4 delta (T_0^2 <= 3 delta OK); for |tau| >= T_0 the slack
inequality s(t) - s(rho t) = (1-rho^2)t^2/(s(t)+s(rho t)) >= (1-rho^2)min(t^2,|t|)/3 (denominator < 3 max(1,|t|)) re-derived; the
error (1-rho^2)(T_0^2 + |t|T_0)/6 is <= (1-rho^2)min(t^2,|t|)/3 in both ranges (T_0 <= 1). NA: any mate vanishes at the normer of f'.
No hidden assumption. (Remark: the theorem is a bookkeeping device; it does not by itself say when (i)-(iii) can be met.)

## 1.2 Clip formula, Bregman identity (P2x 2.1, 2.2). VERDICT: PROVED.
Clip: Fact C gives w(k) = sgn(zeta(k)) min(M, C r(k)), r(k) = |zeta(k)|/(Phi_k^2 |zeta|), zeta(k) = lambda_k u_k(y), lambda_k = m Phi_k;
C r(k)/M = |u_k(y)|/(theta Phi_k) with theta = M|zeta|/(m C). Identity: both sides equal |zeta'| + |zeta| - <w,zeta'> - <w',zeta>.
Exact form: e(y;y') = sum_{P'} |alpha'_k|(M_y - sigma'_k w_y(k)) + (C_y C_y' - <Dw_y, Dw_y'>)/C_y' uses ||alpha'||_1 = 1 and M_y + C_y = 1;
both terms >= 0 (|w_y(k)| <= M_y; Cauchy-Schwarz). Converse of Fact C (used in 4.1(d)) also re-derived: zeta''/c'' in B_{l1} + D(B_{l2})
gives |zeta''/c''| <= 1, and <w, zeta''/c''> = M + C = 1 = N(w), so w norms it; uniqueness by smoothness.

## 1.3 Bregman smallness (P2x 2.3, 2.4). VERDICT: PROVED.
(a) re-derived from the clip formula: clip 1-Lipschitz and |clip(rs) - clip(s)| <= |r-1| for r > 0 (true: for |s| <= 1 and |rs| <= 1 it is
|r-1||s|; the saturated cases are smaller). (b) split t_k <= A (Delta_k <= 2A) / t_k > A (Delta_k <= 2 t_k): correct.
(c) from the identity and e(y';y) >= 0. epsilon(s) = sum_k min(lambda_k, m s) -> 0 by dominated convergence. gamma -> 0 because M', C',
|zeta'| converge along weak*-convergent normers (Fact E / Lemma 1.2). Lemma 2.4: |u_k(z'-z)| <= sum eta_j |u_k(j)| + ||u_k 1_(N,inf)||_1
(|z'_j - z_j| = |z_j| <= 1 beyond N; their factor 2 is harmless), ||U*u_k|| <= ||U|| ||u_k||_1 <= ||U||. The normalization of a' does
not affect e'. So e_m(zhat; xhat') = o(s_1) once masses/moves are O(s_1) and T_N <= s_1^2 (N chosen after s_1).
Quantitatively for geometric Phi: e <= gamma O(A) + O(A^2 log(1/A)) + O(T_N) (my estimate of eps(A/theta)).
Remark "sum lambda_k |w'(k)-w(k)| = Theta(A) in general" is a GENERIC statement (lower bound needs u_k(xhat')-u_k(zhat) ~ A at
off-peak k with Phi_k >~ A); labelled correctly as a remark, supported by numerics. It can even be Theta(A log(1/A)) when infinitely
many off-peak coordinates sit at all dyadic depths.

## 1.4 Base mixed term (P2x 2.5, 2.6). VERDICT: PROVED (as implications; "not an obstruction" is conditional on tuning moves).
2.5: D(x/||x||) = P_{x-perp}/||x||; my bound ||D^2(x/||x||)|| <= 2/||x||^2 <= 8 on ||x|| >= 1/2 (D^2F[k,k] = -(||k_perp||^2 u + 2<u,k>k_perp)/r^2),
so the remainder is <= 4||h||^2 (P2x's 6||h||^2 is valid). 2.6(a) trivial; (b) compactness of U* on bounded sets of l_1, finite-dim
E_eta, residual eta ||e'-e|| |tau| <= eps_0 tau^2 for |tau| >= s_1 once eta <= eps_0/C. The z-part claim ("vanishes on the window")
holds because the B_tau are supported in F u K where z' = z on [1,N]. Caveat: (b) requires e'-e (which is DETERMINED by the masses up to
the tuning moves) to be steerable orthogonally to E_eta, i.e. dim E_eta extra conditions with positively spanning effects — a (TC)-type
hypothesis that grows with 1/eta. Stated as "provided tuning moves exist": acceptable.
For two-piece data the mixed term is exactly v(xhat') = sum_m Delta d_m |R_m xhat'| e_m once Delta d'_m = Delta d_m (checked), so
the base side needs |I_D| scalar tunings only. Correct.

## 1.5 Theorem 3.5 (Delta d_m >= 0, (TC)). VERDICT: PROVED (minor constant slips only).
Re-derived step by step:
* Step 2: Gfun_m = |R_m x'|(Delta d'_m - Delta d_m) once supp omega_Delta,m is off-peak at f' (Fact C at f': <omega, zeta'>/|zeta'| = d'(omega)).
  Gfun_m(zhat) = 0 (Fact C at f). |Gfun(0)| = O(s_1 + T_N) (|.|_m 1-Lipschitz for ||.||_1). C^1: |.|_m is Gateaux differentiable and
  Lipschitz, hence Hadamard differentiable; chain rule with the C^1 map mu -> xhat'(mu) in c_0 (normalisation of e' is smooth); the
  derivative <R_m*(omega_Delta - Delta d_m w'_m), dxhat'/dmu_l> is continuous (weak* x norm pairing, bounded). Jacobian -> (c_l)
  uniformly on balls of radius r_0 = 2K_0 C_1(s_1 + T_N) -> 0 by the sequential argument. Effect vectors (M1) V_m(j), (M2)
  <P_{e-perp}U*V_m, U*e_j*>/nu, (M3) z_j x (M2): re-derived. Brouwer Lemma 3.3: correct (fixed point of Psi on the ball of radius 2|Gfun(0)|).
* Step 3: Omega'-_m - Omega'+_m = omega_Delta,m - Delta d'_m w'_m + Delta d_m (w'_m - w_m) = omega_Delta,m - Delta d_m w_m; b'- = b- - b+1_(N,inf) - beta a';
  b'-(xhat') = -sum_m Delta d_m (|R_m xhat'| - <w_m, R_m xhat'>) = -sum Delta d_m |R_m xhat'| e_m(zhat;xhat') <= 0. beta = (b+1_[1,N])(xhat') -> b+(zhat) = 0.
* Step 4: supp b'+ in F u (K_+ cap [1,N]) in supp a'; no sign change on [-s_1, tau_1]; q*(a'+sigma b'+) = 1 + G(sigma; U*a', U*b'+) exactly
  (first-order term b'+(xhat') = 0, Kink = Fl = 0). Lemma 3.1(a),(b) and 3.2(a),(b) give the bounds. Lemma 3.2(a) box check:
  (1-d's)gamma/2 >= gamma/4 >= s_gamma ||omega||_inf (s_gamma <= gamma/8). P'_m nonempty (||alpha'||_1 = 1) so the sup is (1-d's)M'.
* Step 5: K cap [1,N] coordinates without mass have z'_j = z_j and sigma b-_j z_j-signed for sigma < 0 (no kink); mass coordinates have
  a'_j z_j-signed (no flip); F: no flip (Step 0). Convexity: w'_m + sigma Omega'-_m = (1-x)[w'_m + sigma~(omega-_m - d'-_m w'_m)] + x w_m
  with x = |sigma| Delta d_m >= 0 exactly iff Delta d_m >= 0 (the ONLY use of (H2)); N_m(w_m) = 1.
  Constant slip: |sigma~| <= tau_1/(1 - delta/8) > tau_1, so Lemma 3.2 must be invoked on [0, 2 tau_1] (Step 0 says "applicable on
  |s| <= 2 tau_1" but 3.2 needs 2 tau_1(|d|+1) <= 1/2); replace tau_1 by tau_1/2 in Step 0. Harmless.
* Step 6: (1-2delta)/(1-delta/8) <= 1-delta  <=>  -7delta/8 <= delta^2/8: true; margin absorbs the eta's.
No use of: rates of T, block-tameness, finiteness of K or of peak sets, c_0-membership of zhat. The data (H1) are one-sided admissible
LINEAR decompositions with FIXED finitely supported off-peak carriers; this is the real restriction.
Observation (not in P2x): nothing in the proof uses finiteness of I except through (T4)/Fact E; for I = N, (T4) is Martin's Prop 3
(X** strictly convex) and only the finitely many active blocks I_0 are touched, so Thm 3.5 should hold verbatim for p itself (SKETCH).
