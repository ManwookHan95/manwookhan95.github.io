# cert0 notes part 2: floor row, CM'(a)-(d), (U3), reduction claim, single-referee fixes; numerics

## Numerics done
- tu_bank_check.py/.out (exact model of V1 Lemma TU Step 2, 50 digits): literal per-carrier floor v_h = max(|x_h|, c), c << eta^2:
  hold bank m_h < 0 whenever beta_h < 0 (eta = 1e-6, 1e-8, 1e-10); threshold -beta_h (N - nu_p)/N = 7.2e4 eta^2 (scales like eta^2);
  common window eta_* -> m_h = 2000 eta > 0.  With beta_h > 0 no failure.  => FINDING F1 confirmed (precision, fixable).
- k1_check.py/.out (own block solver from lem:threshold, 60 digits): K1/Lemma K identities a^2 = sigma'+k^2R^2, k = a+sigma',
  k = K(sigma',R^2), theta = AM/C: 59 blocks (45 with Omega ∩ P = weak peak in Omega): max error 5.2e-61.
  KN-1 sensitivity at fixed active ratios (floor status 1 - 1e-6): inactive Omega value v -> rho_2 - floor ~ 2e3 v^2 (v = 1e-5: 2e-7;
  v = 1e-4: 1.4e-5, carrier becomes a PEAK).  Confirms: inactive values enter quadratically (release drift 4c^2 harmless, O(c^4));
  second-order VALUE errors ~ Design^2 eta'^2 left on inactive carriers would destroy a Puiseux margin mu << (Design eta')^4 => exact hold needed.

## (2) Lemma F / floor row (X4^0)
- Lemma F: rho_l = m|r_l|K(sigma,R^2)/Phi_l >= rho^0_l since sigma >= sigma_rob (P ⊇ P_rob; s_f >= 0) and R^2 >= R_a^2.  Exact (no "up to fine").
  With K1 (weak peaks in Omega): sigma' >= sigma_rob - 3b sum Phi^2 -> rho >= rho^0 - C D^C b.
- (ii) data: lambda vs Domega_dec = vs gamma_dec + Delta'_dec lambda rho(f) (strict non-peak) / + Delta'_dec lambda (weak peak);
  violation of (X4^0) at r'' <= 3 lambda gap(f)/t + |Delta'| lambda |rho(f) - rho^0(r'')|,
  |rho(f)-rho^0(r(f))| <= C D^C (b + c^2) [(T): |sigma'-sigma_rob| <= 3b + c^2, |R^2-R_a^2| <= C b^2], |rho^0(r(f)) - rho^0(r'')| <= Lip*(eta' + Cb).
  => <= C_f lambda (b/t + D^C b + Lip* eta') <= K t (b <= T^4, eta' <= T^4/(L Design), t >= T).  CORRECT.
- (iii) kind [3] at f^# with TRUE shift: lambda vs Domega^# = vs gamma + Delta'' lambda rho^# >= (Delta''-Delta'^*) lambda rho^# + Delta'^* lambda (rho^# - rho^0)
  >= -C_f lambda (Design c + D^C c^2) [S-0 route V: |Delta''-Delta'^*| = |Delta'^*||1 - kappa'/kappa^#| <= C_f c; rho^# - rho^0 in [-C_f c, C D^C c^2 + C_f c]]
  >= -3 lambda gap^#/t since gap^# >= M mu/4, c <= mu^2/64.  Same for increments (homogeneous rows).  + side: needs gap(f) <= 1.5 gap^#
  (vs omega^+ <= gap(f)/t): gap(f) <= M b <= M mu/8 (Q1 (S6): b <= mu/8) <= 1.5 * 7 M^# mu/16.  OK.
  COSMETIC: the intermediate claim "M b <= gap^#/4" (X1 2.2(iii), Q1 2.2) is not literally true after Step B (gap^# >= 7M mu/16 gives
  gap^#/4 >= 7M mu/64 < M mu/8 possible); the inequality actually needed (gap(f) <= 1.5 gap^#) holds with room.
  Step B does not change the cone (it is fixed at the end of Step A) => data satisfaction unaffected.  CORRECT.

## (3) CM'(a)-(d) at the KN^tr companion (route V), re-derived
(a) Static ownership: own(j) = first candidate meeting j; S_k ⊂ O(k) (allowedness (a): no earlier target meets S_k; S_k ∩ (E_c ∪ F^A ∪ Step-A coords)
 = {} for k > L >= l_f).  supp u_k \ O(k) fixed before k (own(j) <= k for j in supp u_k ∩ J_fine).  zhat = z on J_fine (diag base, a unchanged in B).
 Negative k: u_k(zhat^#) = Y_k + varsigma_k own_k, |.| >= delta°_k >> theta Phi_k/m (W3) -> (R) peak, margin >= q0 delta°_k/2.  Holds in MIXED classes
 (only sigma_{m(k)} = -1 used) and for absorbers (block 1 negative: untuned absorbers are type-(d) peaks; X2-ref A5 obstruction absent).
 Scr_m(x): coarse carriers: peaks margin >= q0 vartheta Phi_min u/2 > x_0, strict non-peaks gap >= g_min, Phi gap >= Phi_min g_min > x_0
 (CM^tr(b); KN-1-held after release |val| <= 4c^2: gap ~ M); fine: sum_{delta°_k <= 2x/q0} (delta_k H_k)^2 <= C (x/q0)^2 (super-exponential decay).
 => Scr_m(x) <= C (x/q^#_0)^2 for x <= x_0 = c_f g_min Phi_min(L).  CORRECT.
(b) Representation: g_t = b^+ + sum R^*(omega^+ - d omega^+ w); vs U1 Prop 2.2(e) only b^+ off F differs: V_fine/2 vs chi_f V_fine and no absorber
 coefficients: change <= (1+||U||)||V_fine||_1 <= C_f (Design c + c^2/t + c) <= K t.  Gamma: sqrt seminorm, change <= C||V_fine||_1/nu^{1/2}.
 Companion block data within C_f Design eta' log(1/eta') of f's => V1 TR Step 5 estimates (t^{-2} x block-data change <= C T^2 log -> 0).
 Kinds: active robust [2]; active near-threshold (T) [3] via (X4^0) (above); (KN) [3] via U1-ref (X4) with true shift (|Delta''-Delta'^*| <= C_f c << gap^#/t);
 (U): Delta'' = 0, vs Domega = vs gamma/lambda >= 0 [3]; inactive nearly neutral / KN-1-held [2] (Domega = Delta'' w^# ~ 0, gap ~ M);
 KN lever: [2] neg / [3] pos; D2-pushed: [1'] (gap >= c eta' M may be < t^2).  CORRECT (P1 needed).
(c) Violations: E_c contact: z V_proj >= 0 ((X1) at the cube corner: (Delta'^*, gamma(t)) in cone), b^+ = chi V_proj + V_fine/2 => (z b^+)_- <= |V_fine|/2,
 (z b^-)_+ <= |V_fine|/2; E_c free: V_proj = 0, b^± = ±V_fine/2, b^theta = (chi - 1/2)V_proj = 0 ((H3)).  V_fine|E_c = -(Delta''-Delta'^*) P (trace
 correction; ||P_m||_1 <= 1) + fine terms: l1 <= C_f c + C_f sum_{k>L} lambda_k.  Owners' far parts (j > s_far, fixed in A): V = gamma_l v_l(j) + fine,
 z = eps_l, dominance (lem:II-domfine (i) types (a),(b)) => admissible.  J_fine: b^± = ±V/2; coarse owners & negative fine owners: dominance
 (proof of lem:II-domfine uses only |coef_own| lower bounds + later coefficients <= C_f lambda; signs of other blocks not used) => admissible;
 unowned: V = 0, z := 0 admissible; positive-owned: viol <= |V(j)| <= sum_{fine k' meeting j} |coef_{k'}||u_{k'}(j)| (no coarse candidate meets j).
 Total eps <= C_f c_{L+1} + C_f sum_{l>L} lambda_l <= C_f Design c_{L+1} (+ c^2/T harmless).  CORRECT.
 Absorber owners (block 1 active): U1-ref 7 / lem:II-domfine(ii) + P-R: partner coefficient <= (1/8)(M/(M or M/2)) <= 1/4 of owner's; later carriers
 (first stage after the cluster/PRE pair has (W2)) give C_f 2^{-n}/(T_lo eta_k lambda_k); eta_k >= mu_{p0}^2 c_k^2/2^13 (P-R, re-derived: R minimal =>
 2^{-R} > mu^2 lb^2/64, lb >= c/8, least entry 4*2^{-R}/q^*(x) >= 2^{-R}/2), 1/(eta lambda) <= 2^13 D^3/mu_{p0}^2 <= (B_mu D)^6 <= n.  OK.
 Wording: "first later non-absorber stage" should be "first stage after the cluster/PRE sequence" (PRE stages are absorber stages but carry (W2)); harmless.
(d) Cost: Step A C_f Design eta' log(1/eta') = C_f (T^4/L) log; Step B: delta supported in J_fine, coarse |u(delta)| <= 4c^2, fine <= sum lambda <= C c
 -> C_f c log(1/c).  <= theta_w T^2.  CORRECT.
Applicability of lem:II-recursion/domfine/SCi/coststat/trueshift at the route-V companion: recursion's rule z_j = sgn(-sigma_m varsigma_k u_k(j)) already
 contains the anti-aligned positive rule; route V removes type (c) and enlarges (d) to absorbers; SCi's proof with "tuned absorbers" replaced by
 "absorbers of negative blocks are (R) peaks" and Prop II-KN(b) replaced by CM^tr(b); coststat with KN^tr(c); trueshift (a): first term becomes
 C_f c_{L+1} (cluster carriers untuned, they change status in Step B) - still << everything; middle term 0; (b) trace correction NOT absorbed but
 a tolerated violation (counted in (c)).  CORRECT (as X2-ref claimed).

## (4) (U3) at Step-A supports
 Pulls: |a^#(j_p)| >= 12 lambda v (normalized), data t|b| <= t(|gamma| v + |V_fine|) <= (2A_2 + C) lambda v + t C_f c <= K_3 |a^#| with v >= eta_* >= c
 (F1 window) and t <= T_hi << 1/(C_f Design).  Banks: contact-like part chi gamma v (eps gamma >= 0, (X2)) / peak coefficient (sign eps_c) + V_fine/2;
 P3: support-coordinate excess |a+x| - |a| - z x <= 2(z x)_- (checked: 0 without flip, 2(-zx) - 2|a| with flip) => residue is a tolerated violation,
 b^theta = (chi - 1/2)V_proj independent of V_fine.  CORRECT (with F1's window; the c_{L+1} floor is needed exactly here).

## (5) Reduction claim + identification
 Every use of Prop KN in X2-ref's CM' proof located: (i) statuses: x_0, coarse owners' |w| = M, "coarse carriers do not change status in Step B"
 (trueshift (a)), cost/statuses (coststat); (ii) kind-[3] rows: (b) kinds; (iii) exactness: projection error K t, normalization (A_max), (X1) at the cube
 corner used in (c), Hoffman.  Dominance uses no Prop-KN property (activity thresholds, (W4''), Design >= 1/(eta lambda)).  Trace correction uses only
 the S-0 kappa drift and "Omega_act values exact at the end of Step A and untouched by Step B" (a property of KN^tr's realization (Step 4)).
 End of Step A = state after X2-ref's (1c'): (1c') = joint fixed point restoring kappa and Omega_act values with no absorber tuned; route V has no (1b),
 Step 4 of KN^tr is such a joint fixed point.  CORRECT.

## (6) single-referee fixes
 P1 correct (kind [1'] needed: gap >= c eta' M < t^2 possible; V1 E'' allows [1']).  P2 correct; moreover route V's Step B depends only on the class
 signs (z on J_fine), so its position relative to the cube is immaterial except for Delta''^* (needs the cube).  P4 correct (bounded number of S_l
 coordinates: Step-0 push, realization/hold pull+bank, lever/D2 push, peak push).  P-HOLD correct (by (T): non-active coarse strict non-peaks of a
 (T)-block are exactly its nearly neutral ones; KN-1 sensitivity numerics).  P-R correct (re-derived).
 Additional cosmetic: KN^tr Step 4's TU hypotheses ("exactly swallowed far out", F^2 ⊂ [1,s_max] ∪ S_c for c notin L_0) are disturbed by the Step-0
 push of active weak peaks (a pull already sits in S_d, d in L_0): use distinct pull coordinates and merge banks at j', or drop the Step-0 move
 and bound F(r(f)) <= 1 + C D^C b directly by K1.
