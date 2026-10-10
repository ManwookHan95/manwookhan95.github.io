# U2 part 2: item (E2) -- infinitely many bad carriers at infinite F (O4-box); no bounded switching, no box domination

Setting and references as in part 1.  Design SLD^star (part 1.1).  For a window index l_* write B(l_*) := B cap [1, l_*] (coarse bad
carriers), B_np(l_*) its strict non-peaks, T_B(l_*) := union_{l in B(l_*)} supp y_l (finite, subset [1, s_max(l_*)]).
B (the set of bad = exactly swallowed carriers, r_l = 0) may now be INFINITE.

## 2.0 What changes when B is infinite (diagnosis)
V3 4.4 described (O4-box) as follows: with infinitely many bad carriers the switching on F is box-size, |X_j| <~ Bx(j)/t, so cushion
compatibility needs |a^#_j| >~ Bx(j), a SCALE-FREE raise whose mass does not tend to 0; raises give box domination on the deep part only,
and "thin shallow support remains" ((BD_B) needed on F cap [1, N(T)]).  Lemma P of part 1 removes exactly the last point: a shallow
coordinate that would be deep for the data PINS the carrier.  The scale-free raise is needed only on the deep part j >= J, whose mass
is O(2^{-J}) -> 0.  Bounded switching (Z5 Lemma 5.2, an f-dependent injectivity modulus that grows with B(l_*)) is not needed either:
box bounds plus the pigeonhole of thresholds control every size bound R1 needs.  What remains are f-dependent rates of the same kind as
at finite F (Hoffman constants of the growing exact cones, VP constants, gaps of bad strict non-peaks, rooms of good carriers).

## 2.1 Lemma W (window data at a deep-raised companion; any number of bad carriers).  PROVED.
Fix f in S_{p_N*} (F arbitrary), g in C(f), rho in (0,1) and R1's constants (eta_0, kappa_0, eps_tr, eta, with room factor 2).
Let l_* be a window index with l_* >= l_f (R1's threshold: good non-degenerate peaks k°_m of (H2) are coarse), and assume for every l
in B_np(l_*) that k(l) is a strict non-peak with gap >= gamma_B(l_*) > 0, and (H3-inf) for the bad carriers <= l_*.
Let Z := Z_f(l_*) subset R^{B(l_*)} be R1's exact-switching cone built from B(l_*) (rows: tau_l >= 0 on B_K; contact and free rows on
T_0 := T_B(l_*) \ F; tau_l = 0 on bad peaks; d-rows sum_{l <= l_*, m(l) = m} q_l tau_l = 0), and for P subset B_np(l_*) and
Sigma subset T_B(l_*) cap F let
   Z(P, Sigma) := Z cap {tau_l = 0 : l in P} cap {s_j sum_{l in B(l_*)} eps_l tau_l u_l(j) >= 0 : j in Sigma};
let H(l_*) >= 1 be the maximum of the Hoffman constants of the Z(P, Sigma) (finitely many polyhedral cones; violation measured as in
eq:hoffman plus sum_P |tau_l| plus the negative parts of the Sigma-rows).  Let K*(l_*) := (1/q_0 + 22) Lambda*_f(l_*) with the rooms
r*_l(l_*) of good l computed on S_l \ (F cup union_{l' in B(l_*), l' > l} supp y_{l'}).
Let f' be a row with forced data ((a + D)/q*(a + D), z), D = Delta a + Delta a'', where
 (R) with Bx_*(s) := sum_{l in B_np(l_*)} lambda_l |u_l(s)| (= lambda_l v_l(s) on S_l \ T_B(l_*)):
     R := {s in F : s >= J, |a_s| < 4 Bx_*(s)},   Delta a := sum_{s in R} s_s (4 Bx_*(s) - |a_s|) e_s^*   [deep raise at BOX level];
     raise mass <= psi(J) := 4 sum_{l in B} lambda_l ||u_l 1_{[J, infinity)}||_1 -> 0 (J -> infinity), footprint <= mu*_J psi(J);
 (V) Delta a'' is the VP' correction for L_0 := B_np(l_*) on its finite set F_0 (which requires (ND'_{B_np(l_*)}), F_0 cap R = {} ).
Let t be a dyadic scale with t <= min(t_eta, t_1, 1), and suppose the following SUB-WINDOW CONDITIONS at t:
 (S1) for every j in T_B(l_*) cap F with j < J: either |a_j| <= theta_1 t^2 or |a_j| >= K_top t^2   [K_top defined below; theta_1 <= 1];
 (S2) the budget at f' is (1 + eta')t^2/2 with eta' <= 1 (Corollary 2.4 of V3 at f' gives this when eps'(f') <= t^2/8 and
      lambda' - 1 <= 1/8), and K_top t <= min(1, kappa_0/K_4) (K_4 an f-constant of R1 Claim 3.2(d)).
Define the thresholds K_1 := (5/4) C_q [(1 + 2K*(l_*)) 2^{s_max(l_*)} + 2^J]/delta_min(l_*) + 4 theta_1 + 4C'_f(1 + K*(l_*)),
K_{i+1} := 4H(l_*)(C'_f(1 + K*(l_*)) + l_* K_i + s_max(l_*) K_1) + 2K_i (1 <= i <= l_*+1), K_top := K_{l_*+2}.
Then every two-sided decomposition of a mate g' of f' at scale t (with g' close to g as in V3 RS Step 3) yields d-neutral two-piece
data (b^+-, omega^+-) at f' for a functional g'_t with
   (s b^+)_- <= 3|a'|/t and (s b^-)_+ <= 3|a'|/t on F,   p*(g' - g'_t) <= C''_f K_top t,
   Gamma_w(b^+-, omega^+-) <= (sqrt(1 + eta_Gamma(eta)) + C''_f K_top t)^2,   t||b^+-||_1 <= A_0,   |omega^+-_m(k)| <= A_2/t at k = k(l),
with A_0, A_2 absolute multiples of 1 + ||a||_1 (no bounded-switching constant, no lambda_B), C''_f an f-constant.
Proof.
(1) Pinning (R1 Step 1 and lem:badpeaks at f').  Lemma modswallow(a) holds at level l_* with B replaced by B(l_*): the fine bad carriers
l > l_* have |Delta theta_l| <= 6 lambda_l/t (lem:box) and enter the good inequalities only through their targets, with total
contribution <= 8t^2 (P2); so sum_{good} |Delta theta| <= K* t, sum_{l > l_*} |Delta theta_l| <= 6t^2.  lem:badpeaks (a)-(c) at f'
(fixed good peaks of (H2)); in (b) the fine bad d-terms are bounded by sum_{l > l_*} |q_l| 6 lambda_l/t <= 6 T_lo(l_*)^3/(C_min t)
= O(t^2).  So the violation of Z by the actual amplitudes tau = (tau_l)_{l in B(l_*)} is <= C'_f(1 + K*) t (R1 Step 2, with the fine
bad targets on T_0 contributing <= 8t^2).
(2) Pigeonhole and projection.  The <= l_* numbers |tau_l| (l in B_np(l_*)) miss one of the l_*+1 intervals (K_i t, K_{i+1} t]; let
i_0 be such an index, P := {l : |tau_l| <= K_{i_0} t} (pinned), the others KEPT (|tau_l| > K_{i_0+1} t).  Sigma := {j in T_B(l_*) cap F :
j < J, |a_j| <= theta_1 t^2}.  For j in Sigma, by lem:flip at f' (cushion |a'_j| <= (3/2)|a_j|) and eq:DeltaB,
s_j sum_{B(l_*)} eps_l tau_l u_l(j) >= -3|a_j|/t - phi_j - |r_j| >= -(3 theta_1 + C'_f(1 + K*)) t (r_j: good coarse, fine and bad-peak
carriers at j), so the Sigma-rows are violated by <= s_max(l_*) K_1 t in total.  Let tau' be a nearest point of Z(P, Sigma) to tau:
sum |tau - tau'| <= H(l_*)(C'_f(1+K*) + l_* K_{i_0} + s_max K_1) t <= K_{i_0+1} t/4.  Hence tau'_l = 0 on P, and for kept l:
sgn tau'_l = sgn tau_l, (3/4)|tau_l| <= |tau'_l| <= (5/4)|tau_l| <= (15/2) lambda_l/t (lem:box).
(3) No deep set.  Let X' := sum_{B_np(l_*)} eps_l tau'_l u_l (tau' = 0 on bad peaks), so |X'_j| <= (15/2) Bx_*(j)/t.  Assume J > max F_0.
Claim: s_j X'_j >= -4|a'_j|/t for all j in F.  Suppose not, at some j in F.
 - j >= J: if j in R, |a'_j| = 4Bx_*(j)/lambda' >= 2Bx_*(j); if j notin R, |a'_j| = |a_j|/lambda' >= 2Bx_*(j); then
   4|a'_j|/t >= 8Bx_*(j)/t > |X'_j|: contradiction.
 - j < J, j in S_l \ T_B(l_*) for some l in B_np(l_*): X'_j = eps_l tau'_l v_l(j).  If l is pinned, X'_j = 0.  If l is kept, the violation
   forces s_j eps_l = -sgn tau'_l and |tau'_l| v_l(j) > 4|a'_j|/t, hence (P.2) of Lemma P at f' for the actual tau_l (|tau_l| >= (4/5)|tau'_l|),
   so |tau_l| <= C_q(1 + 2K* 1[j in T(l_*)]) t/v_l(j) <= K_1 t < K_{i_0+1} t: contradiction with "kept".
 - j < J, j in T_B(l_*) cap F: if j in Sigma, the Sigma-row gives s_j X'_j >= 0; otherwise (S1) gives |a_j| >= K_top t^2 and:
   by lem:flip at f' and eq:DeltaB, s_j X_j(tau) >= -2|a'_j|/t - phi_j
   - |r_j| >= -2|a'_j|/t - C'_f(1 + K*) t (r_j collects good coarse carriers (<= (4/3)K* t), fine carriers (<= 8t^2) and bad peaks
   (<= lambda K_d t, lem:badpeaks(c)) at j), and |X'_j - X_j(tau)| <= sum|tau' - tau| <= K_top t/4.  Since |a'_j| >= |a_j|/4 (lambda' <= 2,
   |Delta a''| <= |a|/2), 2|a'_j|/t >= K_top t/2 >= (C'_f(1 + K*) + K_top/4) t because K_top >= K_1 >= 4C'_f(1 + K*).  Hence
   s_j X'_j >= -4|a'_j|/t.
 - j < J in no S_l (l in B_np(l_*)) and not in T_B(l_*): X'_j = 0.
So the deep set of R1 Step 3 is empty.
(4) Data (R1 Step 3 with D_t = {}).  R1 Claims 3.1, 3.2 apply verbatim with C_f K* t replaced by K_top t (closeness of tau'), and give
the stated properties; the size bounds use only: sum_F A_j = 2||a'||_1/t <= 2/t, ||X'||_1 <= sum_l |tau'_l| <= (15/2) sum_l lambda_l/t <= 3/t
(sum_l lambda_l <= 1/3), so by R1 Claim 3.1(iv) t||b^+-||_1 <= 2 + 3 + 3 + 1 =: A_0 = 9; and at k = k(l): l kept,
|omega^-(k)| <= |omega^+(k)| + |tau'_l|/lambda_l <= (4 + 15/2)/t; l pinned, omega^-(k) = omega^+(k); so A_2 := 12.  Gamma_w and closeness: R1 Claim 3.2(d) with C_f K* replaced by K_top.  QED

## 2.2 Theorem RS*_inf (infinitely many bad carriers at arbitrary F).  PROVED (conditional on the rate condition (W_inf)).
Design SLD^star, N >= 1.  Let f in S_{p_N*} (F arbitrary, B possibly infinite) satisfy (H2), (H3-inf) for all bad carriers, every bad
carrier at a strict non-peak has positive gap, (ND'_{B_np(l)}) for every l, and
 (W_inf)  liminf_l  Xi_f(l)/(l 2^{l^3} Lambda°(l)) = 0,   Xi_f(l) := (4 H(l) l + 3)^{l+2} (1 + K*(l)) C_VP(l)/gamma_B(l),
where H(l) is as in Lemma W, C_VP(l) := C_0(B_np(l)) 2^{max F_0(B_np(l))}/min_{s in F_0} |a_s| (VP' constants: conditioning, location and capacity of the correction), gamma_B(l) := min of the
gaps of the bad strict non-peaks <= l and of min_m M_m.  Then f in Rec.
Proof.  As the proof of RS* (part 1.3) with Lemma W in place of Step 4', and with these changes.
(i) Levels: by (W_inf) choose l_j with Xi_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0; by the window factor Omega(l) of SLD^star,
Xi_f(l_j) Omega_K(l_j) Omega_log(l_j) T_hi(l_j) -> 0 and Xi_f(l_j) Omega_K(l_j) Omega_log(l_j)/n^w_{l_j} -> 0 (Omega_K contains 2^{s_max},
s_max and 1/delta_min, which enter K_1, the thresholds and the pigeonhole count (iii); Omega_log absorbs the logarithmic factors coming from
the pinning term 2^{J_j}, which is MULTIPLIED by the threshold factor (4H l + 3)^{l+1}, see (iv)).
(ii) Local validity: Lemma R2 with U_* = 0, A_0, A_2 = 12, gamma_B = gamma_B(l_j): its c_flat is >= c gamma_B(l_j) (c an f-constant;
c_flat <= gamma_B/(2A_2) is the only place where the bad gaps enter), and t_1 >= c' gamma_B(l_j)^2 (R2's r^4-terms); both enter n_j and the
smallness of T_j through Xi_f.
(iii) Sub-window: the inner sub-window S_j = {T_j 2^{1-i} : i <= n_j} with n_j the least n >= A K_top(l_j, J_j(n))/c_flat(l_j)
(A := 48 rho^2/(1 - rho^2)) must satisfy (S1) at all its scales: every j in T_B(l_j) cap F with j < J_j must have |a_j| outside
(theta_1 T_lo'^2, K_top T'^2) where [T_lo', T'] is the sub-window.  Each of the <= s_max(l_j) such coordinates excludes, in log_2 of the
position T', an interval of length <= n_j + log_2(K_top/theta_1) + 1; so among the first P_j := (s_max(l_j) + 2)(n_j + log_2 K_top + 2)
dyadic positions below T_hi(l_j) there is one avoiding all of them (theta_1 := 1); P_j = o(n^w_{l_j}) by (i), and the sub-window satisfies
log_2(1/T_lo') <= L_j + P_j (L_j := log_2(1/T_hi(l_j))).
(iv) Raise depth: J_j := max(J°_j, 1 + max F_0(B_np(l_j))), J°_j := min{J : mu*_J <= x_j^2}, x_j := theta_j c_flat^2 2^{-2(L_j + P_j)}/
(C_e(1 + C_VP(l_j))) [the raise footprint is <= mu*_{J} (4 sum_l lambda_l ||v_l|| + 4 sum_j Bx_B(j)) <= C mu*_J, NOT proportional to T_j, so
x_j must be compared with T_lo'^2 >= 2^{-2(L_j + P_j)}]; then 2^{J°_j} <= 2 log_2(2 log_2(1/x_j)) = O(log(L_j + P_j + log C_VP(l_j))) and
2^{1 + max F_0} <= 2 C_VP(l_j).  Since n_j, P_j, K_top depend on J_j only through the additive-then-multiplied term 2^{J_j}, the least n_j
with n_j >= A K_top(l_j, J_j)/c_flat(l_j) exists and satisfies n_j <= C Xi_f(l_j) Omega_K(l_j) [log L_j + log(Xi_f(l_j) Omega_K(l_j))]
(the bracket comes from 2^{J°_j}); since log L_j + log(Xi_f Omega_K) <= C Omega_log(l_j) for large j (L_j <= log_2(1/T_lo(l_j - 1)) + l_j^3 +
log_2(l_j Omega Lambda°), and Xi_f <= l 2^{l^3} Lambda° along the levels of (i)), we get n_j/n^w_{l_j} <= C Xi_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j))
-> 0 and K_top T_hi(l_j) <= C Xi_f(l_j)/(l_j 2^{l_j^3} Lambda°(l_j)) -> 0.
The raise mass is <= C 2^{-J_j} -> 0, so lambda_j -> 1 and p*(f_j - f) -> 0.
(v) Theorem 2.5 and Y3 Theorem 2.1 at f_j exactly as in part 1.3 (averaged data d-neutral, side parts cushion-compatible).  QED

## 2.3 Remarks
(a) (O4-box) is settled up to the rate condition (W_inf): box-size switching on thin shallow support is pinned (Lemma P), on the deep part
it is absorbed by a scale-free raise of mass O(2^{-J}); no box domination (BD_B), no (RR), no bounded switching.
(b) The rates in Xi_f.  K*(l): rooms of good carriers (as in (W*)); H(l): Hoffman constants of the exact cones over B(l) augmented by
pinned sets and shallow target rows (f-dependent through the d-rows q_l = eps_l q_0 val_l/sigma_m and the contact pattern on T_B(l) \ F);
C_VP(l): conditioning of the value-preserving correction for B_np(l); gamma_B(l): gaps of bad strict non-peaks.  For B finite all are
f-constants (Theorem RS*).  For B infinite they are exactly the kind of f-dependent rates that the pigeonhole / exactification machinery
of V1/V2 converts into design constants at clean sub-windows (H(l): V2 Theorem B -- minors are polynomials in VALUES; gamma_B: V1's
donor raise / status steering; C_VP: part 3 below).  So RS*_inf + (V1/V2 at clean sub-windows) is the natural route to an unconditional
statement; what that transport needs at infinite F is isolated in part 3.
(c) Simplification of RS*: Lemma W also proves RS* (B finite) without Z5's bounded-switching lemma (box-level deep raise, A_2 = 12).
