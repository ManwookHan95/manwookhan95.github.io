# P2 referee — part 2: Theorem 2.1 (engineered recovery of d-neutral two-piece mates)
Verdict: CORRECT (PROVED), one trivial gap (G-a) and two remarks. Every step re-derived by hand.

Re-derivations (all OK):
* v != 0 => v not in R a (a in c_00, Y cap c_00 = {0}) => P_{e-perp}U*v != 0 (U* injective). Identity
  sum_F v_j<PU*v,U*e_j*> + sum_K |v_j| z_j<PU*v,U*e_j*> = ||PU*v||^2 > 0 (v z-signed on K) gives j_+ and s_+ (any sign on F,
  s_+ = z_{j+} on K). Also: v != 0 forces K infinite, so the theorem is only non-trivial at non-attaining f.
* Compatibility (Fact D): z' in c_00, |z'| <= 1 (|z_{j_i}| <= 1-gamma, |p_i| <= gamma), z' = sign a' on supp a' (F: sign kept for
  mu <= |a_{j+}|/2; window: m_j z_j; Far: -m'_j z_j with z' = -z; j_+ in K: mass sign z_{j+}). a'(xhat') = q*(a') = 1 >= q(xhat').
* Step 1: v(xhat') = v(z'-z) + <U*v, e'-e>, v(z'-z) = -2V_Far - V_{>N''} (z_j v_j = |v_j| on K, v = 0 off F cup K, F in [1,N]).
  Lipschitz ||x/|x| - y/|y||| <= 2|x-y|/|y|; |<U*v,e(a''(0))-e>| <= (A_0-1)s_1 + V_Far/2 <= V_Far using 16 rho T_0||U||||U*v|| <= nu
  and V_Far >= 2A_0 s_1. z' does not depend on mu (j_+ keeps its sign); dPsi/dmu = s_+<U*v, P_{e(a'')perp}U*e_{j+}*>/||U*a''||
  >= gamma_+/2 near a; MVT + IVT give mu_* in [0, mu_max]. Psi independent of p (v_{j_i} = 0). Multi-block: v_m(xhat') affine in p
  with slope (v_{m,j_i})_m, y in H_0 (d-neutral: sum_m v_m = v), y -> 0 since v_m(zhat) = |zeta_m| Delta d_m/q_0 = 0.
* Step 2: <D w', D omega> = (C'/|R x'|)(R* omega)(x') for omega off P' (Fact C at f') => d'^+ = d'^- = d'^theta; (2.1.2) re-derived:
  B^+ = B^theta + rho theta v, B^- = B^theta - rho(1-theta)v (uses omega^theta - omega^+ = theta omega_Delta and d-neutrality).
* Step 3: z' -> z coordinatewise (Far in (N, N_2], cut-off beyond N'', p -> 0), masses -> 0 (s_1 <= tau_N/(4A_0) -> 0,
  V_Far <= 2A_0 s_1 + eps_N -> 0); Lemma 1.2; c = (g''-g)(xhat') + g(xhat') -> g(zhat) = 0; g' -> rho g; B^sigma -> rho b^sigma.
* Step 4: coordinatewise radius (fix G1) re-derived from A Lemma 4.4(c): |W(k)| <= (1-d sigma)M - gap(k)(1/2 - d sigma) on supp omega.
* Step 5: no flips (F: |tau rho beta| <= rho T_0 beta_max <= a_min/8 <= (1 - tau rho c)|a'_j|; window masses: m_j/4 vs |a'_j| >= m_j/2
  for sigma = theta; one-sided signs for sigma = +-; Far: |a'_j| >= 2 rho T_0|v_j| >= 2|tau rho beta_j|); kinks: 0 on J, 0 on
  contacts <= N'' with z' = z (designated sign), <= rho|tau|V_{>N''}/2 beyond N'' (z' = 0), 0 for sigma = theta (beta^theta = 0 beyond N).
* Step 6: (tau^2/2)(rho^2 kappa + delta/4) + eps_0 tau^2 = (tau^2/2)(1 - 3delta/2) <= (tau^2/2)(1-delta); Lemma 1.4 with T_0 FIXED.
  The decisive structural point is correct: T_0 depends only on (f, g, rho), so p*(f'-f) need only be small compared with T_0^2,
  not with s_1^2; the window (s_1, T_0) is covered by the EXACT transfer of the one-sided decompositions.

(G-a) [trivial] Step 1 uses Psi(0) >= -4V_Far, i.e. V_{>N''} <= V_Far. From (C4), V_{>N''} <= eps_0 s_1/rho = delta s_1/(8 rho) and
  V_Far >= 2A_0 s_1 >= 2 s_1: this holds only for rho >= 1/32. Fix: require V_{>N''} <= min(eps_0 s_1/rho, V_Far) in (C4)
  (or deduce small rho from rho = 1/2 by scaling g' -> (rho/rho_1) g', which keeps (f', g') NA since g'(x') = 0 is not even needed:
  ||(f', lambda g')|| <= 1 = f'(x') for |lambda| <= 1).
(R-a) Sharper reading of the hypotheses: kappa only enters through rho^2 kappa < 1; g in C(f) is used (only) in Lemma 1.4 for
  |tau| >= T_0. Both are needed; in Cor 2.3(b) the hypothesis g in C(f) has been dropped (see part 4).
(R-b) Nothing about T beyond Lemma B is used: no rates, tails, or independence (tau_N > 0 only needs v not in c_00).
  Hidden-assumption hunt (weak* vs norm, uniformity in tau, attained infima, c_0 vs l_inf): all OK — z' in c_00, all estimates are
  uniform on the FIXED interval |tau| <= T_0, Lemma 1.2 gives norm convergence of f' (L compact), and only finitely many data
  (gaps on supp omega^sigma, d', C', nu', e') need to converge.
