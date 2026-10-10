# Q1 part 2 — compatibility of the exact route (X1) and the violation-tolerant route (X2); the KN^tr companion as base row

Setting: T_fin of part 1 (option (a); option (b) for patterns whose N_T does not contain stage 1), N fixed, f in S_{p_N^*} with finite
base support F, g in C(f), rho < 1; w a clean sub-window of a main stage L >= l_f; T := T_lo(w), n := n(w), b := b(w), u := u(w),
D := D(L), eta' := T^4/(L Design(L)); an activity class a (U1 2.3, U1-ref 4.5: read off the decomposition data, fixed before the
companion), its pattern kappa, a (class, cube) set S of scales.  K := C_f (Design(L)/u)^C as in U1 part 2.  "Route X" = the exact route
(U1-ref MT IV' assembly with X1's KN^tr: X1 Master Theorem IV^tr).  "Route V" = the violation-tolerant route (X2's Theorem UE + E^eng with
X2-ref's repair (R-abs): Lemma CM', Theorem C_mix').  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 2.0 What the two routes need and provide (from the refereed statements)
Route X: companion = (1a) Proposition KN [now KN^tr], (1b) zero-value absorbers tuned to value EXACTLY 0 (U1 Lemma 3.3: first pairs P(s),
s in E_c(w), and the cluster of L), (1c) kappa and the exact ratios restored and absorbers re-tuned (joint fixed point), (2) fine structure
(config (i) recursion, config (ii) Schauder) with the G1 release.  Data: EXACT two-piece data at f^#; the fine residues and the trace
correction on E_c are cancelled EXACTLY by the absorbers' switching coefficients (U1 Prop. 3.4; = Theorem S1's RT*(c)).  Recovery: V2's
Theorems E^SC / E^>= (one exact averaged datum per companion, then cor:D1) on the subset S (U1 Lemma 2.4).  Classes: no active shift,
one-signed.  NOT mixed (frustrated positive carriers prevent an exact completion with (SC) for the negative blocks: U1 5.4-5.5, U1-ref).
Route V: companion = (1a) Proposition KN [now KN^tr], (1c') kappa and the exact values restored (joint fixed point), NO absorber tuned, (2')
G1 release + static-ownership recursion (negative fine carriers self-aligned, positive anti-aligned; absorbers are ordinary fine
carriers).  Data: U1 Prop. 2.2(e) on Omega := all coarse strict non-peaks, with tolerated violations (fine residues, trace corrections,
positive-owned coordinates) of l_1-mass O(Design c_{L+1}).  Recovery: d-consistent engineered approximant f' of f^# (Lemma DC with levers
of Lemma LV(a)-(c)), per-piece bounds (Theorem UE), averaging at f' (Theorem E^eng), threshold comparison (S2c) by (W_exp).  Classes: all
(no active shift, one-signed, mixed).  Hypothesis used from the coarse system: Proposition KN's conclusions only.

## 2.1 Decision (PROVED in 2.2-2.6 and part 3)
| class kind | route used in Master Theorem VI | alternative | why |
|---|---|---|---|
| no active shift | Route V with KN^tr (all active blocks are (U)-blocks: KN^tr reduces to the rescaling 2.1(U) = V2 Thm B, values only) | Route X (U1-ref MT IV', first alternative; needs neither (KN) nor genericity) | uniform proof; route X is an independent check |
| one-signed | Route V with KN^tr | Route X = X1 MT IV^tr (KN^tr + exact absorbers) | both valid for T_fin (I3, I6 of part 1); double coverage |
| mixed | Route V with KN^tr | none | route X fails for mixed classes (frustration); route V tolerates it |
The two routes are never mixed inside one companion: for each (L, w, class) ONE companion is built.  Route V never tunes an absorber and
never gives one a switching coefficient (X2-ref 2.3 shows tuned absorbers cannot follow the levers of Lemma DC); route X never builds a
d-consistent engineered approximant with violated data (its data are exact).  So X1's zero-value-absorber features (Theorem S1's RT*(c),
U1 Prop. 3.4) and X2's levers never act on the same row.

## 2.2 Lemma CM^tr (the route-V companion with KN^tr).  PROVED (modulo the refereed tools cited).
Hypotheses: as in the setting; the class a is of ANY kind (no active shift, one-signed, mixed); NO hypothesis (KN_{w,a}).
Construction.  Step A := Proposition KN^tr (X1 2.6 with X1-ref 8: K1 formula-1 kappa with the pattern's Omega, Step 0 pushes of active weak
peaks of (T)-blocks, Lojasiewicz point r', point r_1' of Y_1, point r'' of Z_kappa with F(r'') <= 1 - mu_kappa(eta'/3), realization in ONE joint
fixed point: V1 Lemma TU sets the active values to r''_l kappa ((U)-blocks: s_m r''_l kappa, D1), HOLDS the inactive Omega values of the
(T)-blocks at exactly 0 (KN-1), (KN)-blocks receive U1-ref's lever push, D2 pushes in (U)-blocks, one peak push per block restores kappa).
Since route V tunes no absorber, there is no U1 step (1b) between (1a) and (1c'), and the end of Step A is X2-ref's step (1c').
Step B := X2-ref Lemma CM' step (2'): G1 release (U1-ref 5) and the static-ownership recursion on J_fine := N \ (F^A ∪ E_c(w) ∪ coordinates
fixed in Step A), owner-candidates (a) Omega_act, (b) coarse peaks of active blocks, (d) every carrier at a stage > L of an active block
(absorbers included, with their forced coefficients -Delta''_m lambda_k w(k)); negative fine owners self-aligned, positive anti-aligned,
coarse owners by the sign of their coefficient, unowned coordinates z := 0.  f^# := the resulting row.
Claims.  With mu_min(w) := min_kappa mu_kappa(eta'/3) (minimum over the patterns of level L) and g_min(w) := (1/8) min(c_f eta', mu_min(w)):
 (a) [exactness, KN^tr(a)] the active ratios at the end of Step A lie on Z_kappa; robust minors and cofactor polynomials are >= u/2; hence the
     l_1-Hoffman constant of Gamma^#(kappa, a) is <= C (Design/u)^C (V2 Lemma H) and A_max <= C_f (Design/u)^C (U1-ref (p-c)).
 (b) [statuses at f^#] every coarse carrier of f^# is either a peak with relative margin >= u/2 or a strict non-peak with gap^#(k) >= g_min(w);
     in a (T)-block every active near-threshold carrier d has rho^#_d <= 1 - mu_kappa(eta'/3)/4; the inactive Omega carriers of (T)-blocks
     have |value| <= 4 c_{L+1}^2 (held at 0 in Step A, moved only by the G1 release).
 (c) [data] for every t in S the data of X2-ref CM' — Domega(t) of U1 Prop. 2.2(e) supported in Omega := all coarse strict non-peaks of f^#,
     with the common true shift (U1 Lemma 4.6(a); its middle term vanishes since Step B does not change active values), V := V(Domega(t)),
     V_proj := L(Delta'^*, gamma(t)) on E_c, V_fine := V - V_proj off F^#, b^+ := beta + chi V_proj + V_fine/2, b^- := b^+ - V,
     omega^- := omega^+ + Domega(t) — represent g_t with p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2, and every Omega carrier is of kind
     [1], [2] (gap >= gamma(w) := min_m M_m u/4) or [3] relative to gap^#.
 (d) [violations] eps(t) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T; every violated free coordinate has b^theta = 0 ((H3) of Lemma VT).
 (e) [scrambling] every carrier at a stage > L of a negative active block is an (R) peak with margin >= q^#_0 delta°_k/2, and for every negative
     active block m: Scr^#_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0(w) := c_f g_min(w) Phi_min(L).
 (f) [cost] p*(f^# - f) <= C_f Design(L) eta' log(1/eta') + C_f c_{L+1} log(1/c_{L+1}) <= theta_w T^2, theta_w := C_f T^2 log(1/T) -> 0.
Proof.  (a): X1-ref 8, statement (a).  (b): at the end of Step A, X1-ref 8 statement (b): (T)-blocks rho <= 1 - mu/2 for active near-threshold
carriers (gap >= M mu/2), inactive Omega values 0 (gap M); (KN)-blocks U1-ref Prop. KN(b) with eta' (gaps >= c_f eta' M); (U)-blocks
active statuses <= 1 - eta' and inactive near-threshold carriers pushed inward by eta' (D2) (gaps >= c eta' M); every other coarse carrier
keeps its robust status (relative margin >= u - Lip eta' >= u/2, or gap >= c u).  Step B changes coarse values only through the released
far parts of non-owners (<= 4 c_{L+1}^2 each, U1-ref 5) and the block scalars by <= C Design c_{L+1} (X1-ref S-0: steps (2), G1 release,
true-versus-reference shift); since c_{L+1} <= b(L, M(L))^2 <= b^2 ((W2); b decreases along the sub-windows of a level) and b <= mu_min/8
((D2) of T_fin (S6)), and mu_kappa(h) <= Lip h (X1-ref Q1) gives mu_min <= Lip eta' <= 1/(C Design) for L large, the drift is
<= C Design mu^2/64 <= mu/8 on every status: rho^# <= 1 - mu/2 + mu/8 <= 1 - mu/4 (gap >= M mu/4 >= mu/8 >= g_min, M >= 1/2), and the
robust margins/gaps are untouched at this precision.  (c), (d), (e): X2-ref Lemma CM' (a)-(c) and its proof (X2-ref 4).  That proof uses
Proposition KN only through (i) the coarse statuses (feeding U1 Lemmas 4.1, 4.3, 4.5 and the bound x_0 of the scrambling estimate: coarse
carriers do not enter the scrambled set below x_0 because their margins are >= u/2 and Phi gap >= Phi_min(L) g_min) — supplied by (b);
(ii) the kind-[3] property of the near-threshold Omega carriers, which X2-ref takes from U1-ref 4.1's row (X4) — in (T)-blocks it is supplied
by X1's floor row (X4^0): the decomposition data satisfy (X4^0) up to K t (X1-ref 3.2; data at weak peaks via eq:peakshift), every point
of the cone and every normalization increment is inward at f^# with the TRUE shift (X1-ref 3.3 and S-0: lambda(|Delta'' - Delta'| +
|Delta'| |rho^# - rho^0|) <= C lambda (Design c_{L+1} + c_{L+1}^2/t + D^2 c_{L+1}^2) << 3 lambda gap^#/t, using gap^# >= M mu/4 >> c_{L+1}^{1/2});
the + side: vs omega^+ <= gap(f)/t <= M b/t <= gap^#/(4t) by (D2); in (KN)-blocks U1-ref's (X4), in (U)-blocks vs gamma >= 0 (Delta' = 0);
(iii) exactness of Gamma^#(kappa, a) at the realized ratios (projection with error K t, normalization onto one ray, U1 Prop. 2.2(b),(c)) —
supplied by (a).  No other property of Proposition KN enters (U1 Lemmas 4.1-4.2 dominance and Lemma 4.6 do not use the statuses beyond
"robust or strict non-peak with gap >> c_{L+1}"; U1-ref 7 for owners inside absorber blocks; X2-ref CM'(c)'s violation count uses only cone
row (X1), dominance and the trace-correction bound).  (f): Step A: X1-ref 8(c) (V1 Lemmas CO, TU(d)); Step B: U1 Lemma 4.5 / Z3 Lemma 3.1
(coarse carriers meet J_fine only beyond s_far(w), carriers at stages > L have total weight <= C c_{L+1}); eta' Design = T^4/L.  QED

## 2.3 Proposition BR (the KN^tr companion is a base row of Theorem UE).  PROVED.
Let f^# be the companion of Lemma CM^tr.  For every t_i in S the data of CM^tr(c) form a window family at the base row f_0 := f^# satisfying
X2's hypotheses (U1)-(U7) with: A_0 an f-constant, A_2 = 22, gamma_B = gamma(w) = min_m M_m u/4 (so c_flat(w) >= c_f u), C_Delta an
f-constant, and window quantities
   n = n(w) <= log_2(1/T),  gap_min >= g_min(w),  x_0 = x_0(w),  C_S <= C/q_0^2,  c_fine <= C_f c_{L+1},  c_tiny <= Design(L)^C c_{L+1},
   lever constants r_0 >= c g_min(w)/(C_lev Design(L)^C), C_2, C_lev, K_J <= C_f Design(L)^C  (K_X = 0: no absorber in Omega).
Moreover the window conditions (W-a), (W-b) of Theorem UE hold for L >= l'_f.
Proof.  (U1), (U2): CM^tr(c) (and V1 TR(iii) for A_2 = 22).  (U3) at E := F^# \ F (the supports created in Step A: TU banks and pulls of
KN^tr and of the KN-1 holds, peak-push banks, (KN)-lever moves; Step B creates no support): contact-like data, or t|b| <= K_3 |a^#| by
V1 TR(iv) — the moves of KN^tr are of the same types as U1-ref's Proposition KN moves (TU pulls with mass 24 lambda v carry data <= (2A_2 + C)
lambda v/t, X2-ref (c3')); the constant K_3 is absorbed in (c2).  No absorber support coordinates exist ((R-abs)).  (U4): CM^tr(d).
(U5): CM^tr(e) for the negative blocks.  (U6): Lemma LV(a)-(c) (X2 2.3 with X2-ref (p-LV1), (p-LV2)) for Omega = all coarse strict non-peaks
of f^#: (a) active class-G carriers: (TU) levers; (b) inactive class-G carriers, including the KN-1-held carriers of (T)-blocks (value
O(c_{L+1}^2), data V_t(j) = gamma_l v_l(j) + V_fine(j) = V_fine(j) at the lever coordinate j(l)): (Z-con) levers; (c) class-R carriers: (Z-gen)
levers; lever efficiency mu_{j(l)}^2 v_l(j(l)) >= 1/Design(L) by (D-lev) with n_l.  Pull coordinates of Lemma DC are chosen among the contacts
of f^# in S_l ∩ (s_max, s_far] with v_l(j_p) in [r, 2^{3G(L)} r] NOT used by Step A: Step A uses at most two coordinates of each S_l beyond
s_max (one TU pull, one bank; U1-ref's (KN) lever push uses the far part of d_0's own set likewise), every window of v-values of ratio
2^{3G(L)} contains >= 3 elements of S_l (bounded gaps G(L) = 2^{L+1}), and every unused coordinate of S^nat_l is a contact with z = eps_l
(V1 (C1)); the extra factor 2^{2G(L)} <= Design(L) enters C_2 only.  W_lev: carriers outside Omega meeting lever coordinates are at stages > L
(allowedness (c): beyond s_max no coarse target meets S_l), total weight <= 2 c_{L+1}.  (U7): U1 Lemma 2.1.
Window quantities: n <= log_2(1/T) since T = 2^{-n} T_hi(w) <= 2^{-n}; gap_min, x_0: CM^tr(b), (e); C_S: U1 Lemma 4.3; c_fine, c_tiny: X2-ref
CM' / C_mix' (total weight of carriers at stages > L is <= C c_{L+1}, coefficients <= C_f lambda); r_0: Lemma DC (5) chooses r_0 below the
gaps of Omega carriers and the margins of the peaks of f_0 divided by C_lev; K_J = 1 + 4/A_min since K_X = 0.  (W-a): c_fine <= C_f c_{L+1}
<= C_f exp(-1/T) <= c_late delta T/(n A_0) for L large ((W_exp), T <= T_lo(L, M(L))... precisely T_lo(L, M(L)) <= T so exp(-1/T_lo(L, M(L)))
<= exp(-1/T)).  (W-b): K_J c_tiny <= C_f Design^C exp(-1/T) <= 1/4 and 2 K_J ||Y||_inf <= 2 K_J (C_f c_{L+1} + Design s_1 A_0/T) <= 1/2 for the
s_1 of Lemma S2c^tr.  QED

## 2.4 Lemma PM (the Puiseux margin survives the levers of Lemma DC).  PROVED.
Let f' be the d-consistent engineered approximant of Theorem UE built at f_0 := f^# (X2 3.2: masses on W, cut-off at N'', levers P* of
Lemma DC with |P*|_inf <= r).  Then:
 (i) nv'_k = nv^#_k for every k in Omega (exact; Lemma DC), in particular for every active near-threshold carrier d of a (T)-block and for
     every KN-1-held carrier;
 (ii) |C'_m - C^#_m| <= C_f c_{L+1} for every block m;
 (iii) for every k in Omega: rho'_k = rho^#_k (1 - C^#_m) C'_m/(C^#_m (1 - C'_m)), hence |rho'_k - rho^#_k| <= C_f c_{L+1}, gap'(k) >= gap^#(k)/2,
     and rho'_d <= 1 - mu_kappa(eta'/3)/8 for d in N_T;
 (iv) the lever moves of size O(r) change the values of carriers OUTSIDE Omega only: coarse peaks of f^# (relative margin >= u/2 >> C_lev r)
     and fine carriers (total weight <= C c_{L+1});
 (v) for every lever parameter P with |P|_inf <= r (not only at the zero P*) no Omega carrier and no coarse peak changes status.
Proof.  (i) Definition 1.4 and Lemma DC's conclusion.  (ii) By lem:threshold, for a block with data zeta, A = |zeta|_m, the norming
functional satisfies |w(k)| = min(M, C |zeta(k)|/(Phi_k^2 A)) and ||D w||_2 = C, so C is the unique root in (0,1) of the CLAMP EQUATION
   F(c; v) := sum_k min(Phi_k (1 - c)/c, v_k)^2 = 1,     v_k := |nv_k|/Phi_k,  nv_k := zeta(k)/A
(divide C^2 = sum_k Phi_k^2 w(k)^2 by C^2).  F is continuous, nonincreasing in c, and strictly decreasing near C with |d F/dc| >= 2 Phi_*^2
(1 - c)/c^3 > 0 where Phi_* is the weight of the natural peak k^nat_m of f (a peak with margin at every row of the ball of Lemma M2).  At f^#
and f' the Omega terms coincide (v'_k = v_k by (i)); the terms of the coarse peaks of f^# are Phi_k (1 - c)/c at both rows for c near C
(margins >= u/2 exceed the value moves); every remaining term belongs to a fine carrier k and changes by at most min(Phi_k^2 (1-c)^2/c^2,
2 Phi_k ((1-c)/c) |v'_k - v_k|) <= 2 ((1-c)/c) (|nv'_k| + |nv_k|), and sum_{fine} (|nv'_k| + |nv_k|) <= 2 (1 + ||U||) sum_{fine} lambda_k
/A_min <= C_f c_{L+1}.  The intermediate value theorem on [C - x, C + x] with x := C_f c_{L+1}/(2 Phi_*^2 (1 - C)/C^3) gives (ii).
(iii) For a strict non-peak, rho_k = nu_k/theta = |zeta(k)| C/(Phi_k^2 A M) = v_k/(Phi_k (1 - C)/C); with v'_k = v_k this is the displayed
formula; |C' - C| <= C_f c_{L+1} and C, 1 - C bounded away from 0 (f-constants) give the bound.  gap(k) = M(1 - rho_k) for strict non-peaks,
so gap'(k) >= gap^#(k) - C_f c_{L+1} >= gap^#(k)/2 since gap^# >= g_min(w) >> c_{L+1} (c_{L+1} <= b^2 <= mu^2/64).  For d in N_T: rho'_d <=
1 - mu/4 + C_f c_{L+1} <= 1 - mu/8.  (iv) Lemma DC: the levers act at private signature coordinates of Omega carriers (SEP) and carriers
meeting them are fine (U6 above); coarse peaks have margins >= u theta Phi/(2m) >> C_lev r because r <= r_0.  (v) Lemma DC step (5): r_0 is
below every gap of an Omega carrier and every margin of a coarse peak, divided by the Lipschitz constant C_lev of the values in P; the
largest move of a value over the cube is <= delta_1 + C_lev r <= g_min/2.  QED
Remark.  The comparison asked for — lever moves O(r) versus the Puiseux margin mu_kappa — is therefore: on Omega the levers act EXACTLY
(no O(r) error at all, only the frozen-C error C_f c_{L+1} << mu^2), and off Omega they never meet a near-threshold coarse carrier; along the
continuation the requirement r <= r_0 ~ g_min(w)/C_lev is a requirement on s_1, which (LATE) contains (Lemma S2c^tr).  The Puiseux exponent
enters only the WINDOW constants K_w, s_late, never K, D_cls, A_max, c_flat.

## 2.5 Lemma S2c^tr (late threshold and violation masses with the Puiseux margin).  PROVED.
At the companion f^# of Lemma CM^tr (main stage L >= l'_f, T = T_lo(w)):
 (i)   g_min(w) >= T^{5 Design(L) + 2} >= 2^{-6 log_2(1/T)^2} and x_0(w) >= T^{5 Design(L) + 3} >= 2^{-7 log_2(1/T)^2};
 (ii)  every window constant entering Theorem UE (K_w, the lever constants, C_S, 1/x_0, 1/gap_min, n, A_0/T) is <= exp(C_1 log^2(1/T)) and
       s_late(w) := c delta (T gap_min x_0/(n A_0 K_w))^{C} (X2-ref (p-UE5)) satisfies s_late(w) >= exp(-C_2 log^2(1/T)), C_1, C_2 absolute
       (after absorbing f-constants for T small);
 (iii) eps^viol(w) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T <= exp(-1/(2T))/2 and, with s_1 := max(64 rho eps^viol/delta, exp(-1/(2T))),
       64 rho eps^viol <= delta s_1, s_1 <= s_late(w), and K_w (K_w s_1 + c_fine + tail_W) <= K T^2 (the requirement of Theorem E^eng,
       X2-ref (p-E1)); also s_1 >= exp(-1/(2T)) >> C Design c_{L+1}/delta (fine-carrier lever effects) and r <= r_0.
Proof.  (i) Lemma QC(c) with X1-ref Q2: mu_kappa(h) >= c_kappa h^{beta_kappa} for h <= h_kappa; h := eta'/3 <= 1/Design(L) <= h_kappa
(Design(L) >= 1/h_kappa), c_kappa >= 1/Design(L), beta_kappa <= Design(L) (T_fin (S5)), and 3 L Design(L) <= 3 n^2 <= 1/T, so
eta'/3 >= T^5 and mu_kappa(eta'/3) >= Design(L)^{-1} T^{5 Design(L)} >= T^{5 Design(L) + 1} (Design <= n <= 1/T).  c_f eta' >= T^5 likewise;
so g_min >= T^{5 Design + 2} (T small).  Design(L) <= n(w) (n(w) >= L 2^{L^3} Q(w) >= Design(L)) and n <= log_2(1/T) give the second form.
x_0 = c_f g_min Phi_min(L) with Phi_min(L) >= 1/D(L) >= 1/Design(L) >= T.  (ii) K_w is a polynomial in these quantities with absolute
exponents (X2 Lemma UE-1, X2-ref (p-UE1)-(p-UE6)); the lever constants are <= C_f Design^C g_min^{-C} (Proposition BR); Design <= log_2(1/T).
(iii) (W_exp): c_{L+1} <= exp(-1/T_lo(L, M(L))) <= exp(-1/T) (T_lo(L, M(L)) <= T_lo(w)); so eps^viol <= C_f T^{-1} log_2(1/T) exp(-1/T),
which is <= exp(-1/(2T))/2 and <= delta s_late/(64 rho) as soon as 1/(2T) >= C_2 log^2(1/T) + log(C_f/(delta T)), true for T small.
s_1 = max(...) <= s_late because exp(-1/(2T)) <= exp(-C_2 log^2(1/T)) for T small.  K_w^2 s_1 <= K T^2: s_late contains the factor
(T/K_w)^C with C >= 3 (X2-ref (p-UE5)); K_w c_fine <= exp(C_1 log^2(1/T)) C_f exp(-1/T) <= K T^2; tail_W is chosen <= K T^2/K_w (X2-ref
(p-E1)).  r <= 4 K_J (1 + 1/A_min)(Pi_X + T^4 s_1) + 8 K_J W_pull/A_min <= exp(C log^2(1/T)) s_1 + (super-small) <= r_0 because r_0 >=
exp(-C log^2(1/T)) and s_1 <= s_late with C in s_late large.  QED
Comparison with X2 4.2: there gap_min >= c_f T^4/(L Design) gave K_w <= T^{-C'}; with the Puiseux margin the exponent is multiplied by
O(Design(L)) <= O(log(1/T)), so K_w <= exp(C log^2(1/T)) — still far below exp(1/T), so (W_exp) as stated (X2-ref (p-W)) suffices;
no change of the design is needed.  This confirms X1-ref's remark on Corollary IV^tr.2.

## 2.6 Theorem C^tr (every activity class is recovered; no (KN)).  PROVED (modulo the refereed tools cited).
Design T_fin (option (a); under option (b) for patterns not containing stage 1 in N_T), N fixed, f in S_{p_N^*} with F finite.  If for
infinitely many main stages L some clean sub-window w of L has a (class, cube) set S of at least n(w)/D_cls(w)^2 scales of ONE activity
class (of any kind), then f in Rec(p_N).
Proof.  Fix g in C(f), rho < 1.  For each such (L, w) take the companion f^#_L of Lemma CM^tr; by Proposition BR the data of the scales of
S form a window family at f_L := f^#_L with (U1)-(U7); Lemma PM shows that the d-consistent engineered approximants f'_L of Theorem UE
preserve every status used (Omega carriers strict non-peaks with gap' >= gap^#/2; coarse peaks peaks); Lemma S2c^tr gives (W-a), (W-b),
(VT') and (LATE) with s_1 := max(64 rho eps^viol/delta, exp(-1/(2T))), and the requirement of Theorem E^eng.  Check the hypotheses of
Theorem E^eng (X2 4.1 with X2-ref (p-E1)) along the main stages L_j -> infinity:
 (E-c) p*(g - g_{j,t}) <= K_j t with K_j = C_f (Design(L_j)/u(w_j))^C (CM^tr(c));
 (E-d) |S_j| >= n(w_j)/D_cls(w_j)^2 >= L_j 2^{L_j^3} (Design/u)^{C'} (U1 (A4): Q(w) >= D_cls(w)^2 (Design/u)^{C_U1}), so |S_j| c_flat(w_j)/K_j
       >= c_f L_j 2^{L_j^3} -> infinity (c_flat(w) >= c_f u(w)); K_j T_hi(w_j)/|S_j| <= K_j 2^{-L_j^3}/(L_j Q(w_j)) -> 0; theta_j/c_flat^2 <=
       C_f T^2 log(1/T)/u^2 -> 0 (T <= 2^{-Q(w)} <= 2^{-(4/u)^{20}});
 (E-e) eps_j = p*(f^#_{L_j} - f) <= theta_{w_j} T_lo(w_j)^2 (CM^tr(f)), and T_lo(w_j) is the least scale of the window containing S_j;
 (E-f) Lemma S2c^tr.
The subset version (U1 Lemma 2.4 applied to the proof of E^eng: only "sum over I_r of dyadic t < 2|r|/c_flat" and the count |S| are used)
gives (f, rho g) in cl NA((c_0, p_N), l_2^2).  rho < 1 arbitrary and cl NA closed: (f, g) in cl NA.  g arbitrary: f in Rec(p_N).  QED

## 2.7 Remarks on the route-X alternative (PROVED statements, for the record)
(a) For classes with no active shift or one-signed, X1's Master Theorem IV^tr (X1-ref 10: U1-ref's MT IV' assembly with KN^tr) applies to
T_fin: its design requirements are those of T^tr (X1 3.1), which T_fin satisfies (part 1: T_fin = T^tr + (D-lev) + (W_exp); (D-lev) only
enlarges Design, (W_exp) only shrinks c_{L+1}, and route X uses c_{L+1} only as an upper bound and in the absorber capacity ratio
lambda_a/c_{L+1} >= 1/(2 Design(L)) (part 1 I2, I3, I6)).  So one-signed classes are covered twice.
(b) For N = 1 every class is one-signed or has no active shift, so Corollary IV^tr.1 already gives Master Theorem VI for p_1 by route X alone
(independently of X2), for option (a) and — by X1-ref W2 (stage 1 in block m_1 = 2, absent from p_1) — for option (b).
(c) Why route X cannot replace route V for mixed classes: an exact completion of the fine structure with (SC) for the negative blocks can
fail when positive carriers are frustrated (U1 5.4-5.5, U1-ref verdict on (C_mix)); route V needs no exact completion.
(d) Why route V must not use the absorbers: X2-ref 2.3 (the absorbers' value rooms ~ their weights <= c_{L+1} are far below the lever and
theta-mass moves; untuned they would become peaks with Domega != 0, a first-order cost).  In route V they are ordinary fine carriers.
