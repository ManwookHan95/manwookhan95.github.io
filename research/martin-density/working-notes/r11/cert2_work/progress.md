# cert2 progress (cluster C: X2 analytic core)

## Sources read so far
- MTVI_graph.md (cluster C items 12-17, 22 P6)
- X2_notes.md 0-4.2 (M1, M1', J, 1.4, M2, levers 2.1, DC 2.2, LV 2.3, 3.1-3.6 UE-1/UE, 4.1 E^eng, 4.2 S2c)
- X2_ref_notes.md 0-3 (p-DC1..3, p-LV1,2, absorber obstruction, p-UE1..7, c3', p-E1, p-W)
- Q1_notes 2.3 (BR), 2.4 (PM), 2.5 (S2c^tr), 2.6 (C^tr)
- Q1_refa_notes full (2.1 clamp eq, P1 kind [1'], P3, P4, P6 (2.8), P8)
- Part I: setting (lambda_{k,m} = m Phi_m(k), Phi <= 2^{-m-k}), lem:threshold, prop:forced, smooth, continuity,
  approximants, def:certificate, lem:algebra, lem:base, lem:block, prop:expansion, lem:slack.

## Key facts captured
- lem:threshold: |w(k)| = min(M, C|zeta(k)|/(Phi_k^2 |zeta|)) off peaks; M + C = 1; ||Dw||_2 = C.
- nv_k = zeta(k)/A = Phi_k^2 w(k)/C off P. d(omega) = sum omega(k) nv_k for omega off P.
- lem:block(c): needs |d sigma| <= 1/2 and |sigma omega(k)| <= gap(k)/2 on supp omega -> ||W||_inf = (1-d sigma)M.
  Proof uses only: on supp omega, |W(k)| <= (1-d sigma)(M-gap) + gap/2 <= (1-d sigma) M  [needs (1-d sigma) >= 1/2].
- lem:block(d): N(W) <= 1 + (sigma^2/2) H (1 + 2|d sigma| M/C) when radius ok.
- lem:base(b): q*(a + t b) <= 1 + (t^2/2) h(b)(1 + 2|t| beta/nu) when no flip and |t| beta <= nu/2.
- lem:slack(a): s(t) - s(rho t) >= (1-rho^2) min(t^2,|t|)/3.

## Pending
- Part I lem:bookkeeping, TV, rebalancing, transferdata, persistence (2707-2972); def:engineered, approxfacts,
  F1, anchor, SC, scrambling, thm:engineered (3238-3800).
- [II] lem:II-VT; U3 Lemma VT.

## Sources read (cont.)
- Part I lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:assembly, def:twopiece,
  def:engineered, lem:approxfacts (E1-E5), lem:F1 (clamp formula), lem:anchor, def:SC, lem:scrambling, thm:engineered (full proof).
- [II] lem:II-VT (proof: claim (VT*) coordinatewise list), lem:II-subset, thm:II-E, lem:II-cert.
- Q1_refb_notes 1.4, 2.1-2.4 (clamp eq, alpha-mass), 3 (S2c^tr; robustness remark exp(C ln^3)).

## RESULT (6)/(iv): M1, M1', identities 1.4, M2 -- re-derived
- M1(i)-(iii): exact (diagonal base: X = U*(A-a) ⊥ U*a; <e_A,e> = nu/nu_A; ||e_A-e||^2 = 2||X||^2/(nu_A(nu_A+nu)) <= ||X||^2/nu^2). CORRECT.
- M1(iv): ||x/|x|-y/|y||| <= 2|x-y|/|y|; first-order cross effect via nu-change. CORRECT.
- M1' crude: ||X|| <= sum m_s mu_s <= 4 rho s_1 mu_1 n A_0/T. Sharp: ||P^perp U*b||^2 = ||P^perp U*(b1_F)||^2 + ||U*(b1_{F^c})||^2
  (orthogonal pieces) => sum_{s notin F} mu_s^2 b_s^2 <= nu h(b). CORRECT. NOTE: UE's W also puts theta-masses on E ⊂ F_0 (on supp a_0);
  there M1(iv) applies (factor 2 in ||e'-e||), harmless for value bounds; those masses are in the pre-row f_1, not lever variables.
- 1.4: d' = d on Omega; w' = (C'/C)w; gap' = (C'/C)gap + 1 - C'/C (algebra re-done); H' = (C/C')H; kappa = 0. CORRECT.
- M2: contradiction + prop:continuity + lem:persistence. CORRECT. PRECISION (M2-a): state "k^nat_m is a peak of f'' with the same sign
  AND margin >= mu^nat_m/2" (same contradiction argument: margin is continuous: u_k(xi'') -> u_k(xi), vartheta'' -> vartheta). This uniform
  margin is what Lemma PM's slope bound on [C - x, C + x] actually needs (needs v_* >= Phi_*(1-c)/c on the whole interval).
  e''_y >= 1/2 from e_y >= 1 - eta_1 >= 3/4 (lem:transferdata(d)); |Y|/q_0 <= sigma e_y/q_0 + Lambda_0 (mu_* <= q_0): K_Y indep. of eta_1. OK.

## RESULT (4)/(iii): Lemma DC -- re-derived (analysis; numerics pending in dc_cert.py)
Derivation: F_l(P) = eps_l(u_l(x1) - u_l(z0)) + P_l + E_l(P) - p_l (A_m(P) - A_m^0), p_l = eps_l u_l(z0)/A_m^0,
A_m(P) - A_m(1) = <w_m(1), R_m dx> + Bregman in [0, <w(P)-w(1), R dx>]; <w(1), R dx> = sum_{Omega_m} q_k P_k + fine + O(|P|^2), q_k = eps_k lambda_k w^0(k).
J = I - p q^T per block; q^T p = sum_{Omega_m} Phi_k^2 w^0(k)^2 / C_m <= C_m^2/C_m = C_m <= ||Phi_m||_2 < 1/2.  SM: ||J^{-1}||_inf <= 1 + ||p||_inf ||q||_1/(1 - q^T p)
<= 1 + 2/A_min (|u_l(zhat)| <= q*(u_l) = 1, so ||p||_inf <= 1/A_min; X2's 1 + 4/A_min is conservative).  P-M on cube with weak inequalities: valid.
Slopes: Z-move dz = eps P/v gives eps*du_l = P exactly; bank beta = nu_1/(mu_j^2 v_l(j)) gives P nu_1/nu_A (M1(i)) = P + O(||X_lev||^2/nu^2).
TU: pull flip -2v(j_p) + bank 2v(j_p) nu_1/nu_A - pull-mass Hilbert term (24 lambda v^2 mu_{jp}^2/nu, tiny) => net O(second order) at P=0.
||X_lev||/nu <= (|P| + 2v) / (mu_{j'} v_l(j')) <= Design 2^{G+2} r  (efficiency mu^2 v >= 1/Design, mu <= 1)  => C_2 ~ Design^2 2^{2G} + m^2|Omega|/A_min.
PRECISIONS found (all harmless in the application, none changes a conclusion):
 (DC-a) delta_1 must be max over Omega (plus weighted sums), not over ALL carriers (late carriers with support beyond N'' move by O(1));
        choose N'' (last) with max_{k in Omega} t_k(N'') <= T^4 s_1.  [X2-ref p-J noted max_Omega t_k <= t(N'')/lambda_min(Omega).]
 (DC-b) linear remainder: the lever effects on fine carriers sum over ALL levers: |R| <= C_2|P|^2 + (|Omega| c_tiny / A_min)|P| + ...,
        and F(0) also contains the FIXED bank part (2 v(j_p) beta at j') acting on fine carriers: <= 2^{G+2} r c_tiny/A_min, and the second-order
        terms of the fixed pull/bank (<= C_2 r^2).  (p-DC1)'s F(0) bound omits both; absorbed when K_J 2^{G+3}|Omega| c_tiny/A_min <= 1/8 and
        K_J C_2 r <= 1/8 (c_tiny <= Design^C c_{L+1} super-small in the application).
 (DC-c) gap preservation: gap' - gap = (1 - C'/C)(1 - gap), so |gap' - gap| = |C'-C|(1-gap)/C <= |C'-C|/C.  X2's "gap >= gap^0/2 once
        |C - C^0| <= gap_min/4" is off by the factor 1/C (C < 1/2 always): need |C - C^0| <= C_min gap_min/4.  Same in UE-1(c).  Harmless
        (C_min is an f-constant; at the companion |C'-C| <= C_f c_{L+1}).
 (DC-d) status radius must be in VALUE units: l in Omega stays strict non-peak iff |u_l| < hat-theta Phi_l, hat-theta = A M/(m C);
        room = Phi_l A gap_l/(m C).  So r_0 <= c min_Omega Phi_l gap^0_l A_min/(m C_lev') and <= c (coarse-peak margins); along the WHOLE cube
        C(P) moves at first order (Omega values move by O(r) away from P*), |C(P)-C^0| <= K(r + delta_1)/A_min (clamp eq. + natural peak),
        so gaps move by O(r/Phi_l).  Consistent with Q1's r_0 >= c g_min/(C_lev Design^C) because Phi_min(L) >= 1/Design(L) (and x_0 = c g_min Phi_min).
 (DC-e) no circularity: W_pull depends on j_p(r); use monotone bound W(j_*) for v(j_p) <= 2^{G+1} r_*; N'' after r (pull coordinates satisfy
        v(j_p) >= r >= r_min := 4K_J T^4 s_1, so j_p <= J(r_min) < N'').
Verdict DC: CORRECT_WITH_FIXABLE_GAPS (precisions DC-a..e + X2-ref p-DC1..3).

## RESULT (5): Lemma LV(a)-(c) internal logic
 (D-lev) arithmetic: mu_j^2 v_l(j) = mu_j^2 delta_l 2^{-j}/n_l monotone decreasing in j; j(l) <= sigma_2(L) => >= 1/Design.  OK (refb 1.4 same).
 Bounded gaps G => an element with v in [r, 2^G r): OK.  (SEP)(ii) from allowedness (c).  K_X = 0 after (R-abs).
 (H3)/(U4) at Z-con lever coordinates after an INWARD move (j becomes free): requires b^theta(j) = 0.  Holds because CM'(b) represents
 b^+ = beta + chi V_proj + V_fine/2 => b^theta = beta + (chi - 1/2)V_proj, and V_proj(j(l)) = gamma_l v_l(j) = 0 for inactive l, beta off F^#.
 So b^±(j) = ±V_fine(j)/2: tolerated violation with b^theta = 0. OK (depends on cluster-A representation; flag as dependency).
 TU pull: |tau rho b(j_p)| <= rho c_flat (2A_2 + C_Delta) lambda v + |V_fine| vs |(1 - tau rho c)a'| >= 12 lambda v: (c3') with 7 < 12 OK.
Verdict LV(a)-(c): CORRECT (given cluster-A inputs: exactness on E_c / V1 (C1) contacts / CM'(b) representation).

## Numerics DC (dc_cert2.py -> dc_cert2.out; dc_fixedmove.py -> dc_fixedmove.out)
- 45 instances (1-2 blocks, |Omega| 1-4, TU + Z-con levers, pull at v in [r, 2r), theta-masses 1e-6): zero P* found in every
  instance with |P*| <= 2K_J|F(0)| (max ratio 0.017), nv exact to 1e-16, statuses of all coarse carriers kept, gap identity
  gap' = (C'/C)gap + 1 - C'/C exact to 1e-15.  Jacobian at 0 = I - pq^T up to O(||X_lev||/nu) (0.004..0.19 in this low-efficiency model).
- IMPORTANT for the radius formula: |F(0)| was 10..2000 x delta_1: it is dominated by the second-order effect of the FIXED TU pull+bank
  (per-instance exponent in v(j_p) ~ 2.0; lower exponents 1.5-1.8 when fine carriers meet the bank/pull coordinates = c_tiny / W_pull
  terms).  So (p-DC1)'s bound |F(0)| <= delta_1(1+1/A_min) + 2W_pull/A_min is INCOMPLETE; the correct bound adds
  C_2 (2^{G+1} r)^2 + 2^{G+2} r |Omega| c_tiny/A_min.  In the application: C_2 <= C_f Design^C 4^{G} <= Design^{C'} (Q1: 2^{2G(L)} <= Design(L)),
  r ~ exp(C log^2(1/T)) e^{-1/(2T)} => K_J C_2 2^{2G+2} r << 1: absorbed.  The radius r stays as in (p-DC1) (self-consistent).

## RESULT (2)/(ii): Lemma UE-1 re-derived item by item
(a) theta masses: ||.||_1 <= 4 rho s_1 n A_0/T; lever masses <= |Omega| (nu Design 2^{G+2} + 24 lambda 2^G) r; q*(A) <= 1 + K_w s_1 <= 2.
    p*(f'-f_0) <= q*(a'-a_0) + C sum_k min(2 lambda_k, K|Du_k|) (+ 2 W_pull: pull-meeting fine carriers move O(1)) <= K_w Pi log(e/Pi) + C W_pull.
(b) |Du_k| <= 2 Pi_X + C_2 r + t_k (factor 2 when theta masses sit on E ⊂ F_0, M1(iv)); pull-meeting carriers: 2|u_k(j_p)| (p-DC2).
(c) clamp eq. via natural peak (M2): |C'-C| <= (2(1-C)/(C c_*)) (1/A)(sum lambda|Du| + |DA|/A) = O(Pi) f-const.  gap: needs K_w Pi <= C_min gap_min/4 (DC-c).
(d) Bx: coarse (Omega: w' = (C'/C)w; peaks margin > K_w Pi): K_w Pi^2; others: 2 sum lambda (2Pi_X + C_2 r + t_k) <= K Pi c_fine + 2t(N'');
    lever-meeting fine: <= 2 W_lev r (X2's "4 C_lev W_lev r^2" double counts r; harmless); pull-meeting: 4 W_pull (p-UE2).
(e) scrambling: K_* is an f-CONSTANT (Lipschitz consts of values/threshold/clamp), not K_w (X2's "K_* := K_w" is only an upper bound);
    Omega carriers in S_2 since w' = (C'/C)w and gap >= 2|C'-C|(1+(M-gap)/C) (p-UE2); A^(1) Phi-mass <= Scr(2K_*Pi) <= C_S(2K_*Pi)^2 needs
    2K_*Pi <= x_0, 2K_*Pi C_S < 1; A^(2) ⊂ {t_k > Pi} ⊂ {t_k > s_1 T^4} (Pi >= r >= 4K_J T^4 s_1). ||D(w'-w)||^2 <= (K Pi)^2 log2(2/(K Pi)) + ... (Phi_k <= 2^{-k}). OK.
(f) three changes, each K (A_0/T)^2 Pi or K A_0 tail_W/T. OK.
(g) c_i = (g''-g)(x') + g(x' - z_0): pull flips contribute 2|g_i(j_p)| <= K r/t (data at j_p ~ lambda (2A_2/t + C_D) v(j_p)); cut-off contributes
    ||g_i 1_{(N'',inf)}||_1 -- NOT in tail_W as defined (tail_W has b^± and v only).  PRECISION (UE-g): put max_i ||g_i 1_{(N_w,inf)}||_1 into tail_W.
K_w EXPONENT AUDIT: every estimate is a FIXED finite product of: n, A_0/T, 1/gap_min, 1/x_0, C_S, |Omega|, Design (via beta <= nu Design,
  2^{2G} <= Design, 1/Phi_min <= Design, 1/r_0 <= Design^C C_lev/(g_min Phi_min A_min)), K_J, C_2, C_lev, m <= N, and f-constants
  (1/c_* natural peak, 1/A_min, 1/C_min, nu, ||U||, transfer data).  No estimate is iterated a window-dependent number of times
  (Sherman-Morrison is rank one per block; Poincare-Miranda no iteration; clamp eq. through ONE natural peak; sums over Omega/levers enter
  LINEARLY as |Omega| factors).  => K_w <= C_f (n A_0 |Omega| Design C_S / (T gap_min x_0))^{C_abs}, C_abs absolute.  Design enters the BASE
  (gap_min >= T^{5 Design + 2}), not the exponent.  CONFIRMED.  (Even a Design-dependent exponent would give exp(C ln^3(1/T)) << e^{1/(2T)}.)

## RESULT (1)/(i): Theorem UE re-derived
Step 2 decomposition identity re-verified algebraically (difference = rho(±1/2)[v - sum R*(Domega - Delta w^0)] = 0).
Radius: kind [1]/[1']: |sigma omega| <= 4 rho c_flat gap^0 <= gap'/2 needs rho c_flat <= 1/16 (with gap' >= gap^0/2).  (c4) gives
  rho c_flat <= 1/(3(A_2+2)) -> implies 1/16 only if A_2 >= 4 (A_2 = 22 in BR: OK).  PRECISION (UE-c4): add rho c_flat <= 1/16.
  kind [2]: 2 rho c_flat A_2 <= gamma_B/4 = (c4) last cond. OK.  kind [3]: outward <= 3 rho c_flat gap^0 <= gap'/2, inward <= 2 rho c_flat A_2
  <= (1 - d sigma)M' => (c) of lem:block via coordinatewise bounds, then (d)'s computation (needs only (c)'s conclusion + |d sigma| M/C <= 1/2;
  |d'| <= ||D omega||_2 by C-S since ||Dw'|| = C'). OK.  theta regime: s_1 rho A_2/T <= gap_min/4 (LATE). OK.
Base claim (*) coordinate list re-done (W, F, E (U3 incl. K_3 in (c2), P3 residues as violations), Z-levers (b^theta = 0 there), TU banks
  (contact-like + theta-mass protection), TU pulls (c3') 7 < 12 = |(1 - tau rho c)a'_{jp}| / (lambda v), contacts (N_w,N''], free, beyond N''). OK.
Linear terms for |tau| > s_1: (1/128 + 1/32 + 1/128) delta |tau| s_1 <= delta tau^2/16. OK.  Step 4/5 arithmetic: 1 - 2d + 3d/4 <= 1 - d. OK.
MISSING HYPOTHESIS (UE-W): |tau rho c_i| <= 1/2 and K_A = 2(1+||U||)A_0 + 1 need K_w (c_fine + tail_W) <= 1/4 (|c_i| <= K_w(Pi + c_fine +
  tail_W)/t_i).  (W-a) c_fine <= c_late delta T/(n A_0) and (W-c) tail_W <= c_late delta T/A_0 do NOT imply this (K_w >> n A_0/T).  Also Step 5's
  bracket needs K_w A_0 tail_W/T <= delta/16.  FIX: (W-a') K_w c_fine <= c_late delta, (W-c') tail_W <= c_late delta T/(A_0 K_w) (N_w is chosen
  after K_w is known -- K_w depends only on window quantities fixed before N_w).  Application: K_w c_fine <= e^{C ln^2(1/T)} C_f e^{-1/T} << 1;
  E^eng already imposes K_w c_fine <= K T^2 and tail_W <= K T^2/K_w (p-E1).  => no conclusion of MT VI affected.
(LATE) uses listed L1-L13 (Pi <= 1/K_w, K_w^3 s_1 log(e/s_1) <= c delta, theta radius, |tau rho c_i|, bracket, gap', scrambling 2K_*Pi <= x_0,
  coarse peaks, r <= r_0 & K_J C_2 r <= 1/8, ball, q*(A) <= 2, E^eng K_w^2 s_1 <= K T^2): all implied by s_late = c(f,delta)(T gap_min x_0/(n A_0 K_w))^C
  with C >= 7 (X2's displayed (LATE) does not imply L2: p-UE5 correct).
Verdict UE: CORRECT_WITH_FIXABLE_GAPS (X2-ref p-UE1..7, c3' + UE-W, UE-c4, UE-g, DC-c).

## RESULT (3)/(v): Theorem E^eng re-derived (with window-dependent c_flat(j) and subset S)
(A),(B) per-piece bounds; convexity of p*; r_0^2 <= min(delta, 1-rho^2) (no c_flat t_1 needed: I_r empty => all (A)).
|r| <= r_0: sum_{I_r} t < 2|r|/c_flat (dyadic, any subset); I_r != {} => |r| > c_flat T_min => eps' <= 2 theta' r^2/c_flat^2;
  need 2 theta'_j/c_flat(j)^2 + 4 K_j/(|S_j| c_flat(j)) <= min(delta/4, (1-rho^2)/6): (E-d) with c_flat(j); then
  1 + r^2/2 - delta r^2/4 <= 1 + r^2/2 - r^4/8 (r^2 <= 2 delta) and lem:slack(a).  OK.
|r| >= r_0: eps' + 4 K T_hi |r|/|S| <= (1-rho^2) r_0 |r|/3 <= (1-rho^2) min(r^2,|r|)/3.  OK.
theta'_j must include the UE cost: eps'_j <= eps_j + K_w Pi log(e/Pi) + C W_pull; with s_1 <= s_late ∝ (T/K_w)^C (C >= 7):
  K_w^2 s_late log/T^2 <= (T/K_w)^{C-3} -> 0 FASTER than c_flat(j)^2 >= c u(w)^2 >= c log(1/T)^{-1/10} (T <= 2^{-(4/u)^20}).  OK.
P6: only (c4)'s last inequality involves gamma_B; (c1)-(c3'),(c5)-(c7) are upper bounds on c_flat, so they persist when c_flat decreases;
  t_1, K_sharp, eta_1, transfer data, r_f, c_late are gamma_B-free.  E^eng uses c_flat only through (A)'s range, the dyadic count and
  |r| > c_flat T_min: exactly where (E-d) tracks c_flat(j).  P6 CONFIRMED.
Subset: UE applies to any subfamily (K_w monotone in n); min S' >= T_lo; averages over S' as above; final distance <= eps' + 4K T_hi/|S'|.  OK.
(p-E1) needed: K_w(K_w s_1 + c_fine + tail_W) <= K T^2 so that e_{j,i} <= K t_i at the smallest scale.  OK.
Verdict E^eng: CORRECT (statement to be read with P6 and p-E1; subset version included).

## Lemma M2 extra precision (M2-b)
lem:TV at f' needs gamma_m < M'_m with M'_m - gamma_m >= gamma_0/2 (conditions (c5) use gamma_0/8).  M2(a) gives |C''-C| <= C/8 only,
  which does not imply M'' - gamma >= gamma_0/2 when gamma_0 < C/4.  FIX: add |M''_m - M_m| <= gamma_0/4 to M2(a) (same contradiction
  argument, M'' -> M by prop:continuity).  Harmless.

## Numerics E^eng (eeng_avg2.py -> eeng_avg2.out)
Scalar model of the proof's inputs (A),(B) averaged over a random half-subset of a 300-scale dyadic window, stable excess arithmetic:
the averaged bound <= s(r) holds iff n'c_flat/K >~ 133, IDENTICAL for c_flat = 1e-1 ... 1e-5 (proof's sufficient: 4/min(delta/4,(1-rho^2)/6) = 294);
theta'/c^2 tolerance ~1.8-7.5 vs proof's 0.0034.  => the averaging depends on c_flat only through n'c_flat/K and theta'/c_flat^2 (P6 confirmed).

## Open check in progress: (U5) at companions vs fine strict non-peaks
Scr_m(s) >= sum_{k in Q_m, Phi_k <= s} Phi_k (Phi gap <= Phi <= s).  If infinitely many FINE strict non-peaks exist, Scr may be LINEAR in s.
(U5) Scr <= C_S x^2 is a cluster-A input (U1 Lemma 4.3 / CM'(a)); check how fine carriers are handled.

## (U5) check resolved (dependency): U1 Lemma 4.3 / CM'(a): fine carriers of negative blocks are made PEAKS (self-aligned owners, state (R))
with margin >= q_0 delta_k H_k/(2 n_k) and Phi_k <= (delta_k H_k)^2 (W3) => quadratic Scr.  So (U5) is a cluster-A input; no UE issue.
Extra precision (UE-e'): fine carriers meeting lever (bank/Z) coordinates move by C_lev r (C_lev window const) and may leave S_1 although
their margin > K_* Pi (K_* f-const): add 4m * Phi(lever-meeting fine carriers) (<= 8 c_{L+1}) to S_m, or take K_* >= C_lev.  Harmless.

## Numerics (DC-c) gap_cfactor.py -> gap_cfactor.out
Block with C = 0.243, Omega carrier gap 0.0100, nv held EXACT, C moved via a non-Omega carrier:
 |C'-C| = 0.00186 (< gap/4 = 0.0025): gap' = 0.00242 < gap/2 = 0.005 (identity exact);  |C'-C| = 0.00249 (< gap/4): k0 BECOMES A PEAK.
 => X2's "gap(P*) >= gap^0/2 once |C - C^0| <= gap_min/4" is FALSE as stated; correct: |C'-C| <= C gap/(2(1-gap)) (= 0.00122 here).
 Harmless in the application (|C'-C| <= C_f c_{L+1} << C g_min; UE-1(c) can take Pi <= c C_min g_min/K_w).

## RETRACTION of (UE-W) -> replaced by (UE-c_i)
Bregman identity: (g''_i - g_i)(x') = -(b^theta_i 1_{(N_w,inf)})(x') - sum_m d^theta_{i,m} Bx_m, since R_m^*(w^0 - w')(x') = <w^0 - w', R_m x'> = -Bx_m.
Hence |c_i| <= (1+||U||) tail_W + (K/t_i) sum_m Bx_m + |g_i(z'-z_0)| + ||U^*g_i|| ||e'-e_0||
            <= (1+||U||) tail_W + ||g_i 1_{(N'',inf)}||_1 + K_w (Pi + c_late delta s_1)/t_i      (lever z-moves: |g_i(j)| |dz_j| <= K r/t).
No standalone c_fine, and tail_W enters with an f-constant: |tau rho c_i| <= 1/2 and K_A hold under X2's (W-a) [with p-UE6] and (W-c).
The bracket of Step 5 also uses only K_f A_0 tail_W/T (f-constant).  => Theorem UE's hypotheses as amended by X2-ref suffice; X2-ref's
(p-UE3) bound is valid but crude.  K_w c_fine enters ONLY the conclusion p*(g'_i - rho g_i) <= K_w(K_w s_1 + c_fine + tail_W)/t_i, which E^eng
handles by (p-E1).  Remaining precision (UE-g): choose N'' (last) also with max_i ||g_i 1_{(N'',inf)}||_1 <= T^4 s_1.
## DONE: report written to r11/cert2_report.md
