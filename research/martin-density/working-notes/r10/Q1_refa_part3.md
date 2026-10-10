# Q1 referee (a) — part 3: design claims, S2c^tr, C^tr, MT VI, VI.2 (working file)

## D. Design claims (T_fin, W_fin, A_fin, GEN_fin, I1-I10)

D1 Lemma W_fin.  CORRECT.  Order inside stage l: (S1) [absorber stages: lb_l, then R(l), then y_l] -> (S2) delta_l = delta(y_l, l)
   -> (S3) -> (S4) c^max_l from actual earlier data, generic c_l -> (S5) rate objects, QC data with the actual weights of carriers <= l
   -> (S6) Design(l), M(l), sub-windows; (W2), (W7), (W_exp) are imposed at stage l+1.  b_X1(w): the left sides of (D1), (D2) are
   continuous, increasing, -> 0 as b -> 0 and the right sides are positive numbers already computed: the admissible set is (0, b_X1(w)].
   c^low_l <= c^max_l at PRE stages (delta_l >= delta^max_l/2 in (W3), (W5)); so lb_l <= c_l.  Positivity of mu_kappa uses GEN_fin
   (option (b): only patterns with stage 1 notin N_T enter the minima/maxima).
   PRECISION P7 (N-freeness): the patterns of p_N at level L must be among the enumerated patterns of level L.  This needs: for L >= l_f
   every block m <= N has a coarse carrier (its natural peak, Lemma M2 / V1 Lemma D), so the blocks entering the cone are among the blocks
   of the stages <= L; the class count (J + 1) 3^J has J = |Omega| + N <= 2L there.  Q1 1.4(c) should say "patterns over the blocks of the
   stages <= l" and state l_f >= the least stage after which all N blocks have coarse carriers.  No change of substance.
D2 Theorem A_fin.  CORRECT.  Re-derived the (T-b)/(T-c) estimate: for s in S_{l'}, Z(s) = x_{l'} c_{l'} delta_{l'} 2^{-s}/n_{l'} +
   sum_{l >= L(s)} x_l c_l y_l(s)/n_l with |sum| <= ||x||_inf (4/3)(4/3) c_{L(s)} <= (8/9) ||x||_inf 2^{-2s} c_{l'} delta_{l'}
   ((W4) at every target meeting s, including PRE and CLUSTER absorber targets; c^cl(p) contains (W4'') for every s in E^ch(p));
   so Z(s) != 0 for all large s in S_{l'}.  (T-d): allowed-with-margin at all main stages p >= max supp y + 2|supp y| + 1; q^*(u_l - y) <=
   2 q^*(delta_l h_l)/n_l -> 0.  Option (a): Phi_m(k) <= 2^{-m-k} still holds, which is all lem:martintail, prop:smooth, prop:approximants,
   prop:reduction, lem:pair use; the equality clause of (T-a) occurs in the note only in def:admissible and in verifications of
   admissibility (checked by grep: lines 144-154, 2344-2345, 3990; line 2437's c_1 is an unrelated local constant).
D3 Lemma GEN_fin.  CORRECT.  delta(y, l) in Q(y(j) : j) (H_l and delta^max_l are rational: H_l = 2^{-3 2^l}/(1 - 2^{-2^{l+1}}), ||U|| = 1/4);
   n(y, l) is put into k_0 by definition; absorber targets x/q^*(x) have algebraic entries and lie in A_pool whatever R, p_i, s are.
   Which weights must be generic: ONLY those of N_T (active near-threshold carriers of (T)-blocks).  Peak weights (sigma_rob, traces),
   weights of (KN)-block carriers (1/lambda in U1-ref's (X4)), weights of carriers outside the pattern lie in k = k_0(other weights).
D4 I1-I10.  CORRECT.  Cluster lower bound: c_{L+i} >= prod_{j <= i}(1 - 2^{-(L+j)}) c^cl 4^{1-i} >= c^cl 4^{1-i}/2 (induction through
   c^max_{L+i} = min(c^cl 4^{1-i}, c_{L+i-1}/4)).  Block-1 ratio uses only c_{l+1} <= c_l/4.  Route V uses NO lower bound on a weight except
   design-computed ones (lambda_l >= 1/D(l), Phi_min(L) >= 1/D(L)); the absorber items (I2 capacity, I3 R, I6) matter only for route X,
   which is not on the tree of MT VI.

## E. The window count (precision P8 — the only point where T_fin's definition must be amended)
U1 2.4(c)-(d): D_cls(w) = (J + 1) 3^J (A_max/eps)^p, p = number of extreme rays of Gamma^#(kappa, a), A_max <= C_f (Design/u)^C,
eps = c_f (u/Design)^C (and eps <= c/(C_f p) so that the - side Gamma grows by <= C_f p eps).  The exponent p is a DESIGN quantity that
grows with the level, and the f-constant enters as C_f^p.  Q1 (S6) asserts D_cls(w) <= C_{f,N} (Design/u)^{C_D} with an ABSOLUTE C_D
and builds Q(w) := max{(4 Design/u)^{omega(l)+20}, (Design/u)^{C_U1}}, C_U1 = 2 C_D + C_K + 1, and Theorem C^tr's (E-d) uses
C_U1 - 2 C_D = C_K + 1.  As stated this is unjustified (U1/U1-ref wrote "(Design/u)^{C'}" without tracking p).
FIX (either suffices; both keep Lemma GW, since Q only grows):
 (a) refined pigeonhole: a basic representation of Delta'(t) uses at most N rays (dimension of the Delta'-space); pigeonhole first over
     the support J of the basic solution (<= C(p, N) <= p^N choices), then over eps-cubes in [0, A_max]^J.  The normalization of U1 2.4(c)
     works verbatim on one support (Delta'^* := sum_{j in J} a^max_j g_j, incr(t) := sum_{j in J}(a^max_j - a_j(t)) r_j).  Then
     D_cls <= (J+1) 3^J p^N (C_f p (Design/u)^{2C})^N, whose exponent is O(N); since omega(l) -> infinity and p_max(l), 3^{2l} <= Design(l)^C
     (design numbers), (4 Design/u)^{omega(l)+20} >= D_cls^2 (Design/u)^{C_K+1} C_{f,N} for l >= l_f(f, N).
 (b) or add the factor (Design(l)/u(w))^{C_0 (p_max(l) + 1)} (C_0 absolute) to Q(w).
With (a) or (b), (E-d) holds: |S| c_flat/K >= c_f l 2^{l^3}/C_{f,N}' -> infinity and K T_hi/|S| -> 0.

## F. Lemma S2c^tr (re-derived)
 (i) h := eta'/3 = T^4/(3 L Design) <= 1/Design <= h_kappa; mu_kappa(h) >= c_kappa h^{beta_kappa} >= Design^{-1} (T^5)^{Design}
     (eta'/3 >= T^5 because 3 L Design <= 3 n^2 <= 2^n <= 1/T, n >= 10); g_min >= (1/8) min(c_f T^5, T^{5 Design + 1}) >= T^{5 Design + 2};
     Design <= n <= log_2(1/T) gives g_min >= 2^{-(5 log_2(1/T) + 2) log_2(1/T)} >= 2^{-6 log_2^2(1/T)}.  x_0 = c_f g_min Phi_min(L) with
     Phi_min(L) >= 1/D(L) >= T.  CORRECT.
 (ii) K_w is a polynomial with absolute exponents in n, A_0/T, 1/gap_min, 1/x_0, C_S, lever constants, f-constants (X2 Lemma UE-1);
     the lever constants: r_0 is LINEAR in g_min (r_0 <= c g_min Phi_min A_min/(m C_lev)); C_2, C_lev, K_J are Design^C (the clamp-formula
     Lipschitz constant C/(Phi^2 A) has no gap in it).  Hence K_w <= exp(C_1 log^2(1/T)), s_late >= exp(-C_2 log^2(1/T)).  CORRECT.
     (Even an exponent proportional to Design would give exp(C log^3(1/T)), still << exp(1/(2T)).)
 (iii) (W_exp) applies at T_lo(L, M(L)) <= T_lo(w); eps^viol <= C_f Design c_{L+1} + C_f c_{L+1}^2/T <= exp(-1/(2T))/2 for T small;
     s_1 := max(64 rho eps/delta, exp(-1/(2T))) <= max(32 rho/delta, 1) exp(-1/(2T)) <= s_late.  CORRECT.  Numerics (Q1 N2) reproduce the
     log-scale comparison.

## G. Theorem C^tr, MT VI, VI.1-VI.3
G1 Theorem C^tr.  CORRECT modulo P8 (window count) and P6 (Theorem E^eng is stated "with FIXED A_0, A_2, gamma_B" but its proof uses
   gamma_B only through c_flat(j), which (E-d) tracks; gamma_B(w) = min M u(w)/4 is window-dependent exactly as in V1's E''.  Read E^eng
   with c_flat(j) >= c_f u(w_j); t_1, K_sharp, c_late are f-constants independent of gamma_B (UE Step 0': only (c4) involves gamma_B, and
   decreasing c_flat only weakens (c5)).)  Subset averaging: U1 Lemma 2.4 transfers verbatim to E^eng's proof (Case |r| <= r_0 uses
   sum_{I_r} t < 2|r|/c_flat and |r| > c_flat min S; Case |r| >= r_0 uses mean_{S} t <= 2 T_hi/|S|).
G2 MT VI(a).  CORRECT modulo P2 (order class -> Step A -> cube -> Step B) and P8.  Quantifier order verified:
   design T_fin -> N -> f -> (g, rho) -> l_f(f, N, g, rho) [f-constants absorbed, T_hi <= t_1, companions in the ball of Lemma M2,
   all blocks <= N have coarse carriers, T below the thresholds of S2c^tr] -> main stage L >= l_f -> clean w(L) (rate objects of f only)
   -> class a (decomposition data of (g, rho) at f) -> Step A -> cube -> Step B -> data -> N_w -> s_1 -> N'' -> levers (Lemma DC)
   -> f'_L, averaged second row; L -> infinity along all main stages >= l_f.  No window constant is used before its window is fixed.
G3 MT VI(b).  (b1) CORRECT (stage 1 in block 2, absent from p_1).  (b2) CORRECT: |rho_1(f) - 1| > 0 fixed and b(w) <= T_lo(w)^4 -> 0, so
   for L >= L_1 carrier 1 is robust at every clean w, hence not in N_T; only N_T weights need genericity (D3).
G4 Corollary VI.1, Theorem VI.2, Corollary VI.3.  CORRECT (given MT VI).  (i) => (ii) holds for every T (lem:pair + prop:smooth(c): a
   norm-attaining f_n has forced base part nabla q(x_n) in c_00).  (ii) => (i): f' from (LSC-trunc), g' in C(f') with p^*(g' - rho g) < eps,
   (f', g') in cl NA by MT VI, so (f, rho g) in cl NA; prop:reduction(b).  VI.3: lem:martintail uses only |R_m x|_m <= m 2^{-m} q(x).
