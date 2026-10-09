# S3 referee, part 4: Theorem A, Theorem D (first-order rebalancing), D1, D2, Prop 4.2, Lemma R+ numerics

## 4.1 Theorem A / Cor A'. Verdict: Theorem A CORRECT; Cor A' correct in outline (superseded by D, not re-checked line by line).
Theorem A = P2A Thm 2.1 (refereed) + second-order equalisation through Lemma 1.1. Checked: block pieces V_m = w'_m + tau rho(omega - d'w')
satisfy ||V - w'|| <= K_1|tau|; the T_0-constraints make Lemma 1.1(i)/(ii) applicable with the (huge but FIXED) Lambda; the base no-flip
estimates of P2A Step 5 survive the rescaling s = tau/lambda_A (factor-2 margins, lambda_A in [0.99, 1.01]); the theta piece gets
Lev_theta = Gamma_w(b^theta, omega^theta)/2 <= kappa_w/2 by convexity of Gamma_w. Order of choices: delta -> eta_1 -> transfer data -> T_0
-> (N, s_1, ...). OK.

## 4.2 Theorem D. Verdict: CORRECT for Delta d_m >= 0 (no extra hypothesis) and, under (SC_m), for Delta d_m < 0.
Re-derived:
 * Bookkeeping 3.1: g'(x') = B(x') + sum Omega_m(R_m x') = c' l_b + sum sigma'_m l_m; G_b, G_m >= 0 (A Lemma 7.2; subgradient R_m x'/sigma' of N_m at w').
 * Theta piece: c = g''(xhat') = (b^theta 1_[1,N])(xhat') (the block terms vanish since d'^theta is the f'-coefficient), so l^theta_b = 0 and
   l^theta_m = 0 EXACTLY; window masses cover |tau| <= s_1 (no flips, no kinks). So no first-order term at scales below s_1. OK.
 * Side pieces: B^+ = B^theta + rho theta v, B^- = B^theta - rho(1-theta)v, beta^+- as in P2A; Omega^sigma decomposition
   rho(omega^sigma - d'(omega^sigma)w') + kappa^sigma w' + rho c^sigma(w' - w), with c^+ = -theta Delta d, c^- = (1-theta)Delta d. Algebra checked.
 * Linear terms: l^sigma_b = rho theta v(xhat') resp. -rho(1-theta)v(xhat'), v(xhat') = -V_{>N''} + <U*v, e' - e> = O(s_1); l^sigma_m =
   kappa^sigma + rho c^sigma c' Bx_m/sigma', kappa^sigma = rho (d' - d)(omega^sigma - omega^theta) = O(s_1 + tail). The constant K_l does NOT
   depend on eta_1 (I checked: Lambda m Phi_* = q*(T) is bounded independently of eta_1, cf. part 1), so choosing eta_1 BEFORE s_1 is legitimate.
 * Convexity case (s = tau rho c^sigma <= 0, i.e. both sides when Delta d_m >= 0): W = (1-|s|)V_1 + |s| w, N(w) = 1, genuine cost
   rho^2 tau^2 H'/2 + |s| c' Bx/sigma'. Bx_m = <w' - w, R xhat'> in [0, sum_k lambda_k |w'-w|(k)(K_e s_1 + t_k)] = o(s_1) by dominated convergence
   (w' -> w coordinatewise along the sequence, P2A Lemma 1.2). OK.
 * Anchor case (s > 0): W = (1-s)V_1 + s y, s Z_A moved to the base; G(W) <= rho^2tau^2H'/2 + s E_y with E_y = N(y) - <y, Rx'>/sigma' >= 0. OK.
 * First-order rebalancing (Step 6): eps_m = tau l_m/e'_y + t_m rho^2 tau^2; the bracket tau(l_b + sum sigma'_m l_m/c') vanishes by 3.1; what is left
   is |tau| |l_m| x (transfer inefficiency) = O(|tau| s_1 eta_1) <= eps_0 tau^2 for |tau| > s_1. Lemma 1.1's radius condition
   |eps|(2 + Lambda) <= gamma - eta holds because |eps^(1)| <= T_0 K_l s_1 -> 0 with Lambda fixed. Error terms of Lemma 1.1(iii):
   O(|eps||tau| ||Dy||/C') with ||Dy|| bounded independently of eta_1 (Lambda Phi_* = q*(T)/m). OK.
 * The essential new point is sound: a LINEAR first-order mismatch between pieces of an exact decomposition is a pure level shift and can be
   moved through transfer peaks at a cost proportional to (mismatch) x (inefficiency), the inefficiency being fixed before the mismatch scale s_1;
   only the theta piece (exactly balanced) is used below s_1. This is why steering (far pulls, IVT tuning, (S), (TC), (TT), (BR)) is unnecessary.
Minor presentation issues (no effect): K_tr as written mixes the bounded exchange rate with the inefficiency; what is needed (and true) is
"rebalancing cost <= |eps| (Lambda m Phi mu'/c' + q*(e'_m))" with the bracket <= 2 eta_1 at late stages.

## 4.3 Corollary D1. Verdict: CORRECT.
Nothing about Q_m, K, degenerate peaks or rates of T is used: the deep structure enters only via (E4)-(E5), which hold for every f with F finite.
(The two-piece data themselves are finitely supported in the blocks — that is where the restriction lies; D1 does not say that mates at
generic supports HAVE such data.)

## 4.4 Corollary D2. Verdict: CORRECT, with one fixable circularity in the auxiliary rate |C' - C| = O(s_1).
D2 = Theorem B (optimal two-piece data, kappa_w <= 1) + Theorem D + (SC) under (BT). Checked (SC): ||D(w'-w)||^2 <= sum_k min(K^2(s_1+t_k)^2, 4Phi_k^2)
= O(s_1^2 log(1/s_1)) + (tail made <= s_1^2; note sum_k t_k^2 itself may diverge — the min with 4Phi_k^2 is essential, as written);
A_m within {peaks with mu_k <= K'(s_1 + t_k)} under (BT) (finite Q with gaps >= gamma_0); (MS) and dominated convergence give o(s_1).
GAP (fixable): D2(i) and Prop 4.2(a) use a Lipschitz bound Phi_k|w'(k) - w(k)| <= K_0(s_1 + t_k) whose constant needs |C' - C| = O(s_1), while
Prop 4.2(b) derives |C' - C| = O(s_1) FROM that bound (circular as written). Fix: C is the unique root of the strictly decreasing
F(C; v) := sum_k min(Phi_k(1-C)/C, v_k)^2 = 1, v_k := m|u_k(.)|/|R .|; |F(C; v') - F(C; v)| <= (2(1-C)/C) sum_k Phi_k |v'_k - v_k| = O(s_1) + o(s_1^2-tail)
by (E2)/(E4), and |dF/dC| >= 2 Phi_*^2 (1-C)/C^3 > 0 near the root as long as one fixed peak with positive margin (e.g. a transfer peak) stays
active; hence |C' - C| = O(s_1) with no hypothesis. After this, (a) and the rest go through. C Thm 8.4 is contained ((T4) = (MS) is part of
C-tameness, checked in C_notes Def 6.0).

## 4.5 Prop 4.2 ((MS-Q*) => (SC)). Verdict: CORRECT with two small fixes.
 (1) The circularity above (same fix).
 (2) "Consequently (Theorem D): if every block with Delta d_m < 0 satisfies these conditions ..." needs ONE common sequence of scales s_1
     for all such blocks: with a liminf-type hypothesis per block the good scales of different blocks can be disjoint (Scr_m is monotone,
     so goodness transfers only within bounded scale ratios). State the hypothesis along a common sequence, or with lim instead of liminf.
 (d) of the proof bounds Phi_k^2 by 3m min(Phi_k, K_0(s_1 + t_k)): this needs Phi_k <~ s_1 on A_m, which follows from the hypothesis
     (a scrambled coordinate with Phi_k >= K s_1 contributes K s_1 to Scr_m(K s_1) = o(s_1), so there are none at late stages). Cosmetic.

## 4.6 Lemma R+ numerics. Independent test (S3ref_work/rplus_indep.py): 17076 random/adversarial blocks (5-40 coordinates, flipped peaks,
created peaks, perturbations 1e-4..0.5, 3615 cases with C' > C): max N(y) - bound = 0.0, max X - (4||D(w'-w)||^2 + 4 sum_A Phi^2) = -1.4e-13.
