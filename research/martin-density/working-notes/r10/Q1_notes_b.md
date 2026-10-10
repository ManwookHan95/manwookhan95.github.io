
## 2. The two routes and their combination

Setting of Section 2: T_fin (option (a); under option (b) patterns with stage 1 notin N_T), N fixed, f in S_{p_N^*} with F finite, g in C(f),
rho < 1; w a clean sub-window of a main stage L >= l_f; T := T_lo(w), n := n(w), b := b(w), u := u(w), D := D(L), eta' := T^4/(L Design(L));
an activity class a (U1 2.3, U1-ref (p-a), 4.5: read off the decomposition data and fixed before the companion), its pattern kappa, and a
(class, cube) set S of scales.  K := C_f (Design(L)/u)^C as in U1 part 2.  ROUTE X = the exact route (U1-ref's MT IV' assembly with X1's
KN^tr = X1's Master Theorem IV^tr); ROUTE V = the violation-tolerant route (X2's Theorems UE, E^eng with X2-ref's repair (R-abs)).

### 2.0 What the routes need and provide (refereed statements)
Route X: companion = (1a) Proposition KN [now KN^tr]; (1b) zero-value absorbers tuned to value EXACTLY 0 (U1 Lemma 3.3: first pairs P(s),
s in E_c(w), and the cluster of L); (1c) kappa, the exact ratios and the absorbers restored (joint fixed point); (2) fine structure (configuration
(i) recursion, configuration (ii) Schauder) with the G1 release.  Data: EXACT two-piece data at f^#; fine residues and the trace correction on
E_c cancelled EXACTLY by the absorbers' switching coefficients (U1 Proposition 3.4 = Theorem S1's RT*(c)).  Recovery: V2's Theorems E^SC/E^>=
on the subset S (U1 Lemma 2.4).  Classes: no active shift, one-signed; NOT mixed (frustrated positive carriers prevent an exact completion
with (SC) for the negative blocks: U1 5.4-5.5, U1-ref verdict on (C_mix)).
Route V: companion = (1a) Proposition KN [now KN^tr]; (1c') kappa and the exact values restored (joint fixed point), NO absorber tuned; (2') G1
release + static-ownership recursion (negative fine carriers self-aligned, positive anti-aligned, absorbers ordinary fine carriers).  Data:
U1 Proposition 2.2(e) on Omega := all coarse strict non-peaks, with tolerated violations (fine residues, trace corrections, positive-owned
coordinates) of l_1-mass O(Design c_{L+1}).  Recovery: d-consistent engineered approximant f' of f^# (Lemma DC, levers of Lemma LV(a)-(c)),
per-piece bounds (Theorem UE), averaging at f' (Theorem E^eng), threshold comparison (S2c) by (W_exp).  Classes: all.  From the coarse system
route V uses only the conclusions of Proposition KN (statuses, kind [3] rows, exactness of Gamma^#(kappa, a)).

### 2.1 Decision
| class kind | route used for Master Theorem VI | alternative | reason |
|---|---|---|---|
| no active shift | route V with KN^tr (all active blocks are (U)-blocks; KN^tr reduces to the rescaling 2.1(U) = V2 Theorem B, values only) | route X (U1-ref MT IV', first alternative: no (KN), no genericity needed) | uniform proof; route X is an independent check |
| one-signed | route V with KN^tr | route X = X1 MT IV^tr | both valid for T_fin (I3, I6, 2.7) |
| mixed | route V with KN^tr | none | route X fails (frustration); route V tolerates it |
The routes never act on the same row: for each (L, w, class) ONE companion is built.  Route V never tunes an absorber and never gives one a
switching coefficient (X2-ref 2.3: tuned absorbers cannot follow the levers of Lemma DC — their value rooms ~ their weights <= c_{L+1} are far
below the lever and theta-mass moves); route X never builds a d-consistent approximant of violated data (its data are exact).  So X1's
zero-value-absorber features (Theorem S1's RT*(c), U1 Proposition 3.4) and X2's levers never interact; what route V takes from X1 is exactly
Theorem S1(a), (b), (c) (exact cone with robust minors >= u/2, threshold protection, coupling rows (X3)) — i.e. Proposition KN^tr.

### 2.2 Lemma CM^tr (the route-V companion with KN^tr).  PROVED (modulo the refereed tools cited).
Hypotheses: as in the setting, the class a of ANY kind (no active shift, one-signed, mixed); NO hypothesis (KN_{w,a}).
Construction.  STEP A := Proposition KN^tr (X1 2.6 with X1-ref 8): formula-1 kappa with the pattern's Omega (K1); Step 0 (V1's (C1), (C2);
active weak peaks of (T)-blocks pushed to rho = 1 - b); the Lojasiewicz point r' in Z_kappa, a point r_1' of Y_1, a point r'' of Z_kappa with
|r'' - r_1| <= eta' and F(r'') <= 1 - mu_kappa(eta'/3) (Lemma QC; non-coincidence by GEN_fin); realization in ONE joint fixed point: V1 Lemma TU
sets the active values to r''_l kappa ((U)-blocks: s_m r''_l kappa, D1), HOLDS the inactive Omega values of the (T)-blocks at exactly 0 (KN-1),
(KN)-blocks receive U1-ref's lever push, D2 pushes in (U)-blocks, one peak push per block restores kappa; block-triangular Jacobian (d(u/kappa)
/d(TU) = I/kappa, dkappa/d(TU) = O(X), cross effects second order).  [For the KN-1 holds the pull of Lemma TU is taken at a contact j_p of
the carrier's own set with v_l(j_p) >= max(needed downward correction, c_{L+1}) (so j_p <= s_far(w)); the bank absorbs the rest.]  Route V
tunes no absorber, so there is no U1 step (1b) and the end of Step A IS X2-ref's step (1c').
STEP B := X2-ref Lemma CM' step (2'): the G1 release (U1-ref 5) and the static-ownership recursion on J_fine := N \ (F^A ∪ E_c(w) ∪
coordinates fixed in Step A), owner-candidates (a) Omega_act, (b) coarse peaks of active blocks, (d) every carrier at a stage > L of an active
block (absorbers included, with their forced coefficients -Delta''_m lambda_k w(k)); negative fine owners self-aligned, positive anti-aligned,
coarse owners by the sign of their coefficient, unowned coordinates z := 0.  f^# := the resulting row.
Claims.  Put mu_min(w) := min_kappa mu_kappa(eta'/3) (over the patterns of level L) and g_min(w) := (1/8) min(c_f eta', mu_min(w)).
 (a) [exactness] the active ratios at the end of Step A lie on Z_kappa; robust minors and cofactor polynomials are >= u/2; the l_1-Hoffman
     constant of Gamma^#(kappa, a) is <= C (Design/u)^C (V2 Lemma H) and A_max <= C_f (Design/u)^C (U1-ref (p-c)).
 (b) [statuses at f^#] every coarse carrier of f^# is either a peak with relative margin >= u/2 or a strict non-peak with gap^#(k) >= g_min(w);
     in a (T)-block every active near-threshold carrier d has rho^#_d <= 1 - mu_kappa(eta'/3)/4; the inactive Omega carriers of (T)-blocks
     have |value| <= 4 c_{L+1}^2.
 (c) [data] for every t in S, X2-ref CM's data — Domega(t) of U1 Proposition 2.2(e) supported in Omega := all coarse strict non-peaks of f^#,
     with the common true shift Delta''_m = Delta'^*_m kappa'_m/kappa^#_m (U1 Lemma 4.6(a); its middle term vanishes because Step B does not
     change active values), V := V(Domega(t)), V_proj := L(Delta'^*, gamma(t)) on E_c, V_fine := V - V_proj off F^#, b^+ := beta + chi V_proj +
     V_fine/2, b^- := b^+ - V, omega^- := omega^+ + Domega(t) — represent g_t with p*(g - g_t) <= K t and kappa_w <= 1 + eta_0/2, and every
     Omega carrier is of kind [1], [2] (gap >= gamma(w) := min_m M_m u/4) or [3] relative to gap^#.
 (d) [violations] eps(t) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T; every violated free coordinate has b^theta = 0 ((H3) of Lemma VT).
 (e) [scrambling] every carrier at a stage > L of a negative active block is an (R) peak with margin >= q^#_0 delta°_k/2, and for every negative
     active block m: Scr^#_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0(w) := c_f g_min(w) Phi_min(L).
 (f) [cost] p*(f^# - f) <= C_f Design(L) eta' log(1/eta') + C_f c_{L+1} log(1/c_{L+1}) <= theta_w T^2 with theta_w := C_f T^2 log(1/T) -> 0.
Proof.  (a) X1-ref 8(a).  (b) At the end of Step A (X1-ref 8(b)): (T)-blocks: active near-threshold rho <= 1 - mu/2 (gap = M(1 - rho) >= M mu/2),
inactive Omega values 0 (gap M); (KN)-blocks: U1-ref Proposition KN(b) with eta' (gaps >= c_f eta' M); (U)-blocks: active statuses <= 1 - eta',
inactive near-threshold carriers pushed inward by eta' (D2) (gaps >= c eta' M); every other coarse carrier keeps its robust status (relative
margin >= u - Lip eta' >= u/2, or gap >= c u).  Step B changes coarse values only through the released far parts of non-owners: for such l,
|Delta u_l(zhat)| <= 2 delta_l sum_{s > s_far} 2^{-s}/n_l <= 4 c_{L+1}^2 (2^{-s_far} <= c_{L+1}^2, U1-ref 5); it does not change a (hence not e)
and does not touch the active carriers (their sets were closed in Step A).  By X1-ref S-0 the statuses and shifts move by <= C Design(L) c_{L+1}.
Now c_{L+1} <= b(L, M(L))^2 <= b^2 ((W2); b decreases along the sub-windows of a level), b <= eta' (b_U4 <= eta) and b <= mu_min/8 ((D2)), so
C Design c_{L+1} <= C Design eta' mu_min/8 = (C T^4/L) mu_min/8 <= mu_min/16 for L large.  Hence rho^#_d <= 1 - mu/2 + mu/16 <= 1 - mu/4
(gap >= M mu/4 >= mu/8 >= g_min since M >= 1/2), and robust margins/gaps are untouched at this precision.
(c), (d), (e): X2-ref Lemma CM'(a)-(c) and its proof (X2-ref 4).  That proof uses Proposition KN only through (i) the coarse statuses
(feeding U1 Lemmas 4.1, 4.3, 4.5 and the bound x_0: coarse carriers do not enter the scrambled set below x_0 because their margins are >= u/2
and Phi gap >= Phi_min(L) g_min) — supplied by (b); (ii) the kind-[3] property of the near-threshold Omega carriers, which X2-ref takes from
U1-ref 4.1's row (X4) — in (T)-blocks it is supplied by X1's floor row (X4^0): the decomposition data satisfy (X4^0) up to K t (X1-ref 3.2;
weak peaks via eq:peakshift), and every point of the cone and every normalization increment is inward at f^# with the TRUE shift, because
lambda(|Delta'' - Delta'| + |Delta'| |rho^# - rho^0|) <= C lambda (Design c_{L+1} + c_{L+1}^2/t + D^2 c_{L+1}^2) <= 3 lambda gap^#/t (X1-ref 3.3,
S-0; Design c_{L+1} <= (T^4/L) mu/8 << gap^#); the + side: vs omega^+ <= gap(f)/t <= M b/t <= gap^#/(4t) by (D2); in (KN)-blocks U1-ref's (X4),
in (U)-blocks vs gamma >= 0 (Delta' = 0); (iii) exactness of Gamma^#(kappa, a) at the realized ratios (projection with error K t, normalization
onto one ray, U1 Proposition 2.2(b), (c)) — supplied by (a).  No other property of Proposition KN enters (U1 Lemmas 4.1, 4.2 and 4.6 use the
coarse statuses only as "robust, or strict non-peak with gap >> c_{L+1}"; U1-ref 7 covers owners inside absorber blocks; the violation count
of X2-ref CM'(c) uses cone row (X1), dominance and the trace-correction bound only).
(f) Step A: X1-ref 8(c) (V1 Lemmas CO, TU(d)), and Design(L) eta' = T^4/L; Step B: U1 Lemma 4.5 / Z3 Lemma 3.1 (coarse carriers meet J_fine only
beyond s_far(w); carriers at stages > L have total weight <= C c_{L+1}).  QED

### 2.3 Proposition BR (the KN^tr companion is a base row of Theorem UE).  PROVED.
For every t_i in S the data of CM^tr(c) form a window family at the base row f_0 := f^# satisfying X2's hypotheses (U1)-(U7) with A_0 an
f-constant, A_2 = 22, gamma_B = gamma(w) = min_m M_m u/4 (so c_flat(w) >= c_f u), C_Delta an f-constant, and window quantities
   n <= log_2(1/T), gap_min >= g_min(w), x_0 = x_0(w), C_S <= C/q_0^2, c_fine <= C_f c_{L+1}, c_tiny <= Design(L)^C c_{L+1},
   r_0 >= c g_min(w)/(C_lev Design(L)^C), C_2, C_lev, K_J <= C_f Design(L)^C (K_X = 0: no absorber in Omega).
The window conditions (W-a), (W-b) of Theorem UE hold for L >= l'_f.
Proof.  (U1), (U2): CM^tr(c) (V1 TR(iii) for A_2 = 22).  (U3) at E := F^# \ F, the supports created in Step A (TU banks and pulls of KN^tr and
of the KN-1 holds, peak-push banks, (KN)-lever moves; Step B creates none): data contact-like or t|b| <= K_3 |a^#| by V1 TR(iv) — the moves of
KN^tr have the types of U1-ref's Proposition KN moves (a TU pull with mass 24 lambda v carries data <= (2A_2 + C) lambda v/t, X2-ref (c3'));
at a KN-1 hold (gamma_l = 0) the data are V_fine(j) with |V_fine(j)| <= C_f c_{L+1}, while the pull mass is >= 24 lambda_l c_{L+1} >= 24 c_{L+1}/
Design(L) and the bank mass >= c_f c_{L+1} (pull chosen with v_l(j_p) >= c_{L+1}), so t|b| <= |a^#| for t <= T_hi(w); K_3 is absorbed in (c2).
No absorber support coordinates exist ((R-abs)).  (U4): CM^tr(d).  (U5): CM^tr(e).  (U6): Lemma LV(a)-(c) (X2 2.3 with X2-ref (p-LV1), (p-LV2))
for Omega = all coarse strict non-peaks of f^#: (a) active class-G carriers: (TU) levers; (b) inactive class-G carriers, including the
KN-1-held carriers of (T)-blocks (data at the lever coordinate j(l): V_t(j) = gamma_l v_l(j) + V_fine(j) = V_fine(j)): (Z-con) levers;
(c) class-R carriers: (Z-gen) levers; lever efficiency mu_{j(l)}^2 v_l(j(l)) >= 1/Design(L) by (D-lev) with n_l.  The pull coordinates of
Lemma DC are taken among the contacts of f^# in S_l ∩ (s_max, s_far] with v_l(j_p) in [r, 2^{3G(L)} r] NOT used by Step A: Step A uses at most
two coordinates of each S_l beyond s_max (one TU pull, one bank), every window of v-values of ratio 2^{3G(L)} contains >= 3 elements of S_l
(bounded gaps G(L) = 2^{L+1}), every unused coordinate of S^nat_l is a contact with z = eps_l (V1 (C1)), and the extra factor 2^{2G(L)} <=
Design(L) enters C_2 only.  W_lev: carriers outside Omega meeting lever coordinates are at stages > L (allowedness (c): beyond s_max no coarse
target meets S_l), of total weight <= 2 c_{L+1}.  (U7): U1 Lemma 2.1.
Window quantities: T = 2^{-n} T_hi(w) <= 2^{-n}; gap_min, x_0 by CM^tr(b), (e); C_S by U1 Lemma 4.3; c_fine, c_tiny by X2-ref CM'/C_mix'
(carriers at stages > L have total weight <= C c_{L+1}, coefficients <= C_f lambda); r_0 by Lemma DC step (5) (r_0 is below the gaps of Omega
carriers and the margins of the peaks of f_0, divided by C_lev); K_J = 1 + 4/A_min since K_X = 0.
(W-a): (W_exp) and T_lo(L, M(L)) <= T give c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T), so c_fine <= C_f exp(-1/T) <= c_late delta T/(n A_0)
for L large.  (W-b): K_J c_tiny <= C_f Design^C exp(-1/T) <= 1/4 and 2 K_J ||Y||_inf <= 2 K_J (C_f c_{L+1} + Design s_1 A_0/T) <= 1/2 for the s_1
of Lemma S2c^tr.  QED

### 2.4 Lemma PM (the Puiseux margin survives the levers).  PROVED.
Let f' be the d-consistent engineered approximant of Theorem UE built at f_0 := f^# (X2 3.2: theta-masses on W, cut-off at N'', lever
parameters P* of Lemma DC with |P*|_inf <= r).  Then:
 (i)   nv'_k = nv^#_k for every k in Omega (exact; Lemma DC), in particular for every active near-threshold carrier d of a (T)-block and every
       KN-1-held carrier;
 (ii)  |C'_m - C^#_m| <= C_f c_{L+1} for every block m;
 (iii) for every k in Omega, rho'_k = rho^#_k (1 - C^#_m) C'_m/(C^#_m (1 - C'_m)); hence |rho'_k - rho^#_k| <= C_f c_{L+1}, gap'(k) >= gap^#(k)/2,
       and rho'_d <= 1 - mu_kappa(eta'/3)/8 for d in N_T;
 (iv)  the lever moves of size O(r) change the values of carriers OUTSIDE Omega only: coarse peaks of f^# (relative margin >= u/2 >> C_lev r)
       and fine carriers (total weight <= C c_{L+1});
 (v)   for every lever parameter P with |P|_inf <= r (not only at the zero P*) no Omega carrier and no coarse peak changes status.
Proof.  (i) Definition 1.4 of X2 and the conclusion of Lemma DC.
(ii) By lem:threshold the norming functional of zeta_m satisfies |w(k)| = min(M, C |zeta(k)|/(Phi_k^2 A)) and ||D w||_2 = C; dividing C^2 =
sum_k Phi_k^2 w(k)^2 by C^2 shows that C_m is the unique root in (0, 1) of the CLAMP EQUATION
      F(c; v) := sum_k min(Phi_k (1 - c)/c, v_k)^2 = 1,     v_k := |nv_k|/Phi_k,   nv_k := zeta(k)/A.
Each term is nonincreasing in c, and the term of the natural peak k^nat_m of f (a peak with margin at every row of the ball of Lemma M2) is
Phi_*^2 ((1-c)/c)^2 near C, so F decreases with slope >= 2 Phi_*^2 (1 - c)/c^3 there.  At f^# and f' the Omega terms coincide (v'_k = v_k by
(i)); the terms of the coarse peaks of f^# equal Phi_k (1 - c)/c at both rows for c near C (their margins exceed the value moves); every
other term belongs to a fine carrier k and changes by at most min(Phi_k^2 ((1-c)/c)^2, 2 Phi_k ((1-c)/c) |v'_k - v_k|) <= 2 ((1-c)/c)
(|nv'_k| + |nv_k|), with sum_{fine} (|nv'_k| + |nv_k|) <= 2 (1 + ||U||) sum_{fine} lambda_k/A_min <= C_f c_{L+1} (|u_k(xhat)| <= ||u_k||_1
||xhat||_inf <= 1 + ||U||; sum_{l > L} lambda_l <= c_{L+1}/3 by (P2)).  The intermediate value theorem on [C - x, C + x] with x := C_f c_{L+1}
C^2/Phi_*^2 gives (ii).  (iii) For a strict non-peak rho_k = nu_k/theta = |zeta(k)| C/(Phi_k^2 A M) = v_k/(Phi_k (1 - C)/C); with v'_k = v_k this
is the formula; C and 1 - C are bounded away from 0 on the ball of Lemma M2, so |rho' - rho| <= C_f c_{L+1}.  gap = M(1 - rho) for strict
non-peaks, so gap'(k) >= gap^#(k) - C_f c_{L+1} >= gap^#(k)/2 (gap^# >= g_min(w) and c_{L+1} <= b^2 <= g_min^2).  For d in N_T: rho'_d <= 1 - mu/4 +
C_f c_{L+1} <= 1 - mu/8.  (iv) The levers act at private signature coordinates of Omega carriers ((SEP)); carriers meeting them are fine (2.3,
(U6)); coarse peaks have margins >= u theta Phi/(2m) >> C_lev r since r <= r_0.  (v) Lemma DC step (5): r_0 lies below every gap of an Omega
carrier and every margin of a coarse peak divided by the Lipschitz constant C_lev of the values in P; over the cube the largest value move is
<= delta_1 + C_lev r <= g_min/2.  QED
Remarks.  (1) The comparison asked for — lever moves O(r) versus the Puiseux margin mu_kappa — is: on Omega the levers act EXACTLY (no O(r) error;
only the frozen-C error C_f c_{L+1} <= C_f mu^2/64), and off Omega there is no near-threshold coarse carrier; along the continuation r <= r_0 ~
g_min(w)/C_lev is a requirement on s_1 contained in (LATE) (Lemma S2c^tr).  The Puiseux exponent enters only the WINDOW constants (K_w, r_0,
s_late), never K, D_cls, A_max or c_flat, which are of the form design x u^{-C}.  (2) Lemma PM needs the levers on ALL coarse strict non-peaks:
if one coarse strict non-peak is left untuned, C moves at first order and the margin is lost (X2-ref 1.2; numerics 4(N1) control).

### 2.5 Lemma S2c^tr (late threshold, violation masses, (W_exp)).  PROVED.
At the companion f^# of Lemma CM^tr (main stage L >= l'_f, T = T_lo(w)):
 (i)   g_min(w) >= T^{5 Design(L) + 2} >= 2^{-6 log_2(1/T)^2} and x_0(w) >= T^{5 Design(L) + 3} >= 2^{-7 log_2(1/T)^2};
 (ii)  every window constant entering Theorem UE (K_w, the lever constants, C_S, 1/x_0, 1/gap_min, n, A_0/T) is <= exp(C_1 log^2(1/T)), and
       s_late(w) := c delta (T gap_min x_0/(n A_0 K_w))^{C} (X2-ref (p-UE5), C absolute and >= 3) satisfies s_late(w) >= exp(-C_2 log^2(1/T));
 (iii) eps^viol(w) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T <= exp(-1/(2T))/2; with s_1 := max(64 rho eps^viol/delta, exp(-1/(2T))):
       64 rho eps^viol <= delta s_1 ((VT')), s_1 <= s_late(w) ((LATE)), K_w (K_w s_1 + c_fine + tail_W) <= K T^2 (Theorem E^eng's requirement,
       X2-ref (p-E1)), s_1 >= exp(-1/(2T)) >> C Design c_{L+1}/delta (fine-carrier lever effects), and r <= r_0.
Proof.  (i) Lemma QC(c) with X1-ref Q2: mu_kappa(h) >= c_kappa h^{beta_kappa} for 0 < h <= h_kappa; here h := eta'/3 <= 1/Design(L) <= h_kappa,
c_kappa >= 1/Design(L), beta_kappa <= Design(L) ((S5)); L <= n(w), Design(L) <= n(w) (n(w) >= L 2^{L^3} Q(w) >= Design(L)) and n <= log_2(1/T),
so 3 L Design(L) <= 3 n^2 <= 1/T and eta'/3 >= T^5; hence mu_kappa(eta'/3) >= T^{5 Design(L)}/Design(L) >= T^{5 Design(L) + 1} (1/Design >= T),
c_f eta' >= T^5, and g_min >= T^{5 Design(L) + 2} for T small; the second forms use Design(L) <= log_2(1/T).  x_0 = c_f g_min Phi_min(L) with
Phi_min(L) >= 1/D(L) >= 1/Design(L) >= T.  (ii) K_w is a polynomial with absolute exponents in these quantities and in f-constants (X2 Lemma
UE-1, X2-ref (p-UE1)-(p-UE6)); the lever constants are <= C_f Design^C g_min^{-C} (2.3); everything is <= exp(C_1 log^2(1/T)) for T small (log
natural; by (i) log(1/g_min) <= 9 log^2(1/T) and log(1/x_0) <= 11 log^2(1/T)), and s_late >= exp(-C_2 log^2(1/T)) with C_2 := C (C_1 + 21).  (iii) (W_exp): c_{L+1} <= exp(-1/T), so eps^viol <= C_f T^{-1} log_2(1/T) exp(-1/T),
which is <= exp(-1/(2T))/2 and <= delta s_late/(64 rho) as soon as 1/(2T) >= C_2 log^2(1/T) + log(64 rho C_f/(delta T)), true for T small;
s_1 <= s_late since exp(-1/(2T)) <= exp(-C_2 log^2(1/T)) for T small; K_w^2 s_1 <= K T^2 because s_late contains (T/K_w)^{C} with C >= 3;
K_w c_fine <= exp(C_1 log^2(1/T)) C_f exp(-1/T) <= K T^2; tail_W is chosen <= K T^2/K_w (X2-ref (p-E1)); r <= 4 K_J (1 + 1/A_min)(Pi_X + T^4 s_1) +
8 K_J W_pull/A_min <= exp(C log^2(1/T)) s_1 + (super-small W_pull term) <= r_0, as s_late contains the factor (gap_min/K_w)^C.  QED
Comparison with X2 4.2: there gap_min >= c_f T^4/(L Design) gave K_w <= T^{-C'}; the Puiseux margin multiplies the exponents by O(Design(L)) <=
O(log(1/T)), so K_w <= exp(C log^2(1/T)) — still far below exp(1/T): (W_exp) as stated (X2-ref (p-W)) suffices and NO change of the design is
needed.  This confirms X1-ref's remark on Corollary IV^tr.2.  (Arithmetic check: 4 (N2).)

### 2.6 Theorem C^tr (every activity class is recovered; no (KN)).  PROVED (modulo the refereed tools cited).
Design T_fin (option (a); option (b) for patterns with stage 1 notin N_T), N fixed, f in S_{p_N^*} with F finite, g in C(f), rho < 1.  If for
infinitely many main stages L some clean sub-window w of L has a (class, cube) set S of at least n(w)/D_cls(w)^2 scales of ONE activity class
(of any kind) for the data of (g, rho), then (f, rho g) in cl NA((c_0, p_N), l_2^2).
Proof.  For each such (L, w) let f_L := f^# be the companion of Lemma CM^tr.  By Proposition BR the data of the scales of S form a window
family at f_L with (U1)-(U7); by Lemma PM the d-consistent engineered approximants f'_L of Theorem UE keep every status used (Omega carriers strict
non-peaks with gap' >= gap^#/2, coarse peaks peaks); by Lemma S2c^tr, (W-a), (W-b), (VT') and (LATE) hold with s_1 := max(64 rho eps^viol/delta,
exp(-1/(2T))), together with Theorem E^eng's requirement.  Hypotheses of Theorem E^eng (X2 4.1 with X2-ref (p-E1)) along main stages L_j -> infinity:
 (E-c) p*(g - g_{j,t}) <= K_j t with K_j = C_f (Design(L_j)/u(w_j))^C (CM^tr(c));
 (E-d) |S_j| >= n(w_j)/D_cls(w_j)^2 >= L_j 2^{L_j^3} (Design/u)^{C_U1} (U1 (A4): Q(w) >= D_cls(w)^2 (Design/u)^{C_U1}), so |S_j| c_flat(w_j)/K_j >=
       c_f L_j 2^{L_j^3} -> infinity (c_flat(w) >= c_f u(w), C_U1 >= C + 1), K_j T_hi(w_j)/|S_j| <= K_j 2^{-L_j^3}/(L_j Q(w_j)) -> 0, and
       theta_j/c_flat^2 <= C_f T^2 log(1/T)/u^2 -> 0 (T <= 2^{-Q(w)} <= 2^{-(4/u)^{20}});
 (E-e) eps_j = p*(f_{L_j} - f) <= theta_{w_j} T_lo(w_j)^2 (CM^tr(f)), T_lo(w_j) being the least scale of the window containing S_j;
 (E-f) Lemma S2c^tr.
The subset version of the averaging (U1 Lemma 2.4 applied to the proof of E^eng: only "sum over I_r of dyadic t < 2|r|/c_flat" and the count
|S| are used) gives (f, rho g) in cl NA.  QED

### 2.7 The route-X alternative (for the record)
(a) For classes with no active shift or one-signed, X1's Master Theorem IV^tr (X1-ref 10: U1-ref's MT IV' assembly with KN^tr) applies to T_fin:
T_fin = T^tr + (D-lev) + (W_exp); (D-lev) only enlarges Design; (W_exp) only shrinks c_{L+1}; route X uses c_{L+1} only as an upper bound and in
the absorber capacity ratio lambda_a/c_{L+1} >= 1/(2 Design(L)) (I2, I3, I6).  PROVED mod refereed tools.  One-signed classes are covered twice.
(b) For N = 1 every class is one-signed or has no active shift, so Corollary IV^tr.1 gives Master Theorem VI for p_1 by route X alone,
independently of X2, for option (a) and (stage 1 lies in block 2, absent from p_1; X1-ref W2) for option (b).
(c) Route X cannot replace route V for mixed classes (frustration; U1 5.4-5.5); route V must not use the absorbers (X2-ref 2.3).
