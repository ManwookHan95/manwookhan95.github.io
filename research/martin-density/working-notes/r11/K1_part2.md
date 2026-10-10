# K1 part 2 (Round 11): item (O-b) -- line-by-line lever audit at infinite F; lever-regularity

Setting and notation of part 1.  "Row" = the row at which a lever acts: f_1 := f^r after Step 0 (for Step A of Q1 = KN^tr Step 4),
or the PRE-ROW f_1 of Theorem UE^inf (for Lemma DC^inf).  For a coarse carrier l: val_l := eps_l u_l(xhat_1) (eps_l the sign of l's
switching if l carries data, any fixed sign otherwise); g_l := eps_l <U^*u_l, e_1>; nu_1 := ||U^*A_1||.  x := the correction scale of
the system (x_A := C Design(L) eta' for Step A, X1-ref 8; x_DC := r, the lever radius of Lemma DC, X2-ref (p-DC1)); Lambda := the tuned
set of the system.

## 2.0 The lever menu (definitions)
NEAR COORDINATES.  N_l := the first six elements of S_l beyond s_max(L); all lie in (s_max(L), d(L)], d(L) := sigma(L) + 6 * 2^{L+1}
(bounded gaps G_l = 2^{l+1}); Design(L) contains 2^{d(L)}/(delta_min(L) (mu*_{d(L)})^2), so every near coordinate s has lever efficiency
mu*_s^2 v_l(s)/nu >= 1/Design(L) ((D-lev), X2-ref (p-LV1), U2-ref (s1)).  By (R-mod), at a clean w each near s is OFF F, THIN (|a_s| <= b) or
THICK (|a_s| >= u); by (R-lev) the SPREADS |1 - rho_s/rho_{s'}| (rho := a/v_l; s, s' thick in N_l) are tiny (<= b) or robust (>= u).
FAR COORDINATES.  Far_l(x) := {j in S_l : x <= v_l(j) <= x_max}, x_max := T^2/(L Design(L) |Lambda|) (so that zeroth-order moves of size
x_max per carrier cost o(T^2) in total).  A far j is PULLABLE for l if eps_l z_1(j) > -1/2 and j notin F, or j in F, s_j = eps_l and |a^r_j| <=
x_max (it is then lowered to a contact first).  [A far coordinate gives only ONE-sided private moves: a contact sits at the extreme of
its range, so z-moves there can only lower eps_l val_l, and a bank at a far coordinate has efficiency mu*_j^2 v_l(j), negligible.  Two-sided
private moves need a near coordinate (bank efficiency >= 1/Design) or a pull + bank pair.]
DATA STATUS.  l is ZERO-DATA if c_l(t) = 0 for all t in S (inactive Omega carriers, KN-1-held carriers, D2- and KN-pushed carriers,
coarse peaks of inactive blocks), NONZERO-DATA otherwise (active Omega carriers, coarse peaks of active blocks).
RESOURCES (all two-sided except where said):
 (P1) zero-data near lever: l zero-data and a near s in N_l that is off F, or thin (then first LOWERED to a contact of sign s_s, cost <= b):
      at a contact (Z-con of X2 2.1, with eps := z(s)): inward z-move for P <= 0, bank for P > 0; at a free coordinate: Z-gen (X2 Lemma LV(c)).
      Zero data make every state of s admissible.
 (P2) TU: l nonzero-data, a near BANK coordinate s in N_l that is off F (a contact of sign eps_l, see 2.1(b)) or thin with s_s = eps_l, and a
      PULLABLE j_p in Far_l(x) (V1 Lemma TU; U2 TR-inf (a), (a')).
 (P3) Hilbert pair: two thick s, s' in N_l with robust spread (U2 TR-inf (c)).
 (P4) single S-mass: a thick s in N_l (Q2 4.0); column e_l - h_s g, h_s := |a_1(s)|/(nu_1 v_l(s)) (normalized units).
 (P5) anchor: a thick p in F ∩ [1, d(L)] lying in supp u_k for no coarse carrier k of Lambda: column -g (plus effects on carriers meeting p,
      all outside Lambda).
 (P6) block-norm lever of block m (Sys-DC only): a two-sided resource ((P1)-(P4)) of a coarse PEAK of block m with relative margin >= u/2.
l is PRIVATELY TUNABLE if it has (P1) (zero-data) or (P2) or (P3).

## 2.1 Lemma K1.4 (first-order action of the resources).  PROVED.
(a) (P1): X2 Lemma DC (Z-con, Z-gen; refereed): slope exactly 1 on both sides (z-moves change u_l(xhat) by v_l(s) dz_s and do not change e;
    the bank has normalized slope 1 up to O(||X_lev||^2), Lemma M1(i)); the only other carriers with u_k(s) != 0 are fine (s beyond s_max(L) in
    S_l: allowedness (a), (c)), of total weight <= 2 sum_{k > L} lambda_k (W_lev, c_tiny).  The preliminary lowering of a thin s costs <= C_f b
    in p* (companion cost, Z3 Lemma 3.1) and moves e by <= 2 mu*_s b/nu (V1 Lemma B(iii)), hence every value by <= C b: a move of the size of
    (C1)/(C2), done in Step 0 BEFORE the Lojasiewicz step (so the tiny objects are re-exactified afterwards).  A far pull coordinate in F is
    lowered likewise (cost <= C_f x_max; values move by <= C mu*_j x_max << b).
(b) (P2): at a near off-F coordinate s of a NONZERO-data carrier the exact data V_t(s) = c_l v_l(s) are admissible ((X1) of the class cone on
    E_c, or the contact-row of part 1.3), so s is a contact of sign sgn(c_l) =: eps_l (a FREE near coordinate would force c_l = 0); a thin near
    coordinate of a nonzero-data carrier has s_s = eps_l (part 1, Lemma K1.3 (S): an anti-sign thin coordinate below J forces |c_l| <=
    4b/(t v_l(s)) < K_*^2 K t/(4D(L))), so after its lowering (cost <= b) it is a contact of sign eps_l whose data are contact-like.  V1 Lemma TU
    verbatim with the bank at s (a mass of sign eps_l off F^r) and the pull at j_p (if j_p in F: first lowered, cost <= C_f x_max; then the pull
    mass 24 lambda_l v_l(j_p) of sign -eps_l).  Two-sided: the pull
    shifts eps_l val_l DOWN by (1 + eps_l z_1(j_p)) v_l(j_p) >= v_l(j_p)/2 >= x/2 and the bank provides every upward correction continuously
    (V1 Lemma TU Step 2's explicit fixed point).  Cross effects: second order, C_T x^2 (V1 Lemma TU(b), X2 Lemma M1(i)).
(c) (P3): U2 Lemma TR-inf case (c) (refereed): private, two-sided, efficiency >= u/Design(L), cross effects O(Design^2 u^{-4} x^2).
(d) (P4): Q2 4.0 / Q2-refa C.1 (refereed, numerically confirmed): per unit step eps_k d val_k = delta_{kl} - g_k h_l for every carrier k with
    u_k(s) = 0 for k != l (all coarse k != l: s beyond s_max(L) in S_l); two-sided (raise unlimited; lowering by <= |a_1(s)|/2 >= u/2 >> x
    Design: Q2-refa (p2.2)).
(e) (P5): the same formula with no private part: eps_k d val_k = -g_k h_p for coarse k with u_k(p) = 0; two-sided as in (d).
(f) Every resource moves e by <= C Design(L) x (Lemma M1(iv) for support moves, V1 Lemma B for masses off F) and moves no z outside its
    own coordinates; hence robust objects of level L move by <= C Design^C x/u << u.

## 2.2 Correction to Q2-refa C.3 (bank with offset).  FALSE as stated; repaired.
Q2-refa C.3 claims that a BANK at a private contact of a peak k* of a shifted block, placed with a base mass m_0 = 2 K r beta_j and varied by
beta_j P_0 (|P_0| <= K r), is a two-sided block-norm lever satisfying the conclusions of Corollary 4.2.  This fails along the degenerate
direction.  Proof.  With N := D - gt h^T - sum_m p_m q_m^T degenerate (left null vector y, y^T p_{m*} != 0 -- the only case in which the
block-norm lever is needed), every solution of the linearized equation F(0) + N P - pi p_{m*} P_0^{tot} = 0, where P_0^{tot} := m_0/beta_j + P_0
is the lever position measured from ZERO mass (the base mass is itself a move along the lever column), satisfies
      P_0^{tot} = y^T F(0) / (pi y^T p_{m*})
(apply y^T).  So the offset does not enter the forced total; the bank requires P_0^{tot} >= 0, i.e. a SIGN condition on y^T F(0)/(pi y^T p_{m*}),
which is not controlled (F(0) is produced by the theta-masses and the pre-row moves).  Equivalently: with the base mass included in the
pre-row, |F(0)|_inf >= |pi p_{m*}| 2Kr - |F_orig(0)|, so Corollary 4.2's hypothesis K|F(0)|_inf <= r/2 fails as soon as 4K|pi p_{m*}| > 1.
[Numerics, K1_work/offset_check.py: 2000 random degenerate bordered systems; the total lever position equals y^T F(0)/(pi y^T p) to 1e-8
independently of the offset; it is negative (infeasible for a bank) in 48.7% of the instances.]
REPAIR (PROVED).  A two-sided block-norm lever of a shifted block m* is any two-sided resource of a coarse peak k* of m* with robust margin:
(P2) TU on the peak (bank at a near contact of S_{k*} + pull at a pullable far coordinate; at the pull the peak's data -Delta''_{m*} lambda_{k*}
vs v_{k*}(j_p) are anti-sign for the new support sign and are dominated by the pull mass: t|Delta''| lambda v <= C_Delta lambda v <= mu_p/24, the
peak's margin u/2 >> C_lev r), or (P3)/(P4) on the peak (its column then carries the common mode -h g as well: Q2-refa C.3(iv)'s rank-one
perturbation argument applies verbatim), or (P1) if Delta_{m*} = 0 (Q2 Corollary 4.2 as stated).

## 2.3 The audit (every lever of Q1's route-V construction; replacement at infinite F).  PROVED line by line from 2.1.
| move of Q1 (source) | carrier / data | finite-F lever | at infinite F |
|---|---|---|---|
| V1 (C1) close class-G rooms (Q1 CM^tr Step 0) | z-moves on S^nat_l = S_l \ (F ∪ T(L)) | off F | unchanged (off F by definition) |
| V1 (C2) close tiny target rooms | z-moves on T(L) \ F | off F | unchanged |
| V1 (C3) donor raise | -- | NOT on the tree of route V (U1-ref Prop. KN Step 0: "(C1), (C2) only"; X1 KN^tr Step 0) | not used |
| weak-peak push, (T)-blocks (X1 KN^tr Step 0) | active weak peak k, one-sided DOWN by <= 2b theta Phi_k/m | far pull (V1 Lemma IP) | a pullable far j of k (x := 2b theta Phi/m), or (P3)/(P4) on k (lowering direction), or (P1) if zero-data |
| TU on active values (KN^tr Step 4) | Omega_act, nonzero data | (TU) | (P2), (P3) or (P4) |
| KN-1 holds (KN^tr Step 4, Q1-refb P-HOLD) | nearly neutral Omega carriers of (T)-blocks, zero data | (TU) pull at v >= max(corr, c_{L+1}) + bank | (P1) (near Z-con/Z-gen; or TU as at finite F), (P3) or (P4) |
| D2 pushes ((U)-blocks), (KN)-block lever pushes (U1-ref Prop. KN) | inactive, zero data | TU pulls / far z-moves | (P1), (P3) or (P4) |
| peak push per block (KN^tr Step 4; U1 Lemma 1.5) | buffer peak, data iff block active | bank at first far coordinate (+ z-moves/pulls) | (P2) (active block) / (P1) (inactive), or (P3)/(P4) on the peak; in ratio form it is an optional bordering column (2.4) |
| Lemma DC levers (X2 LV (a)-(c)) | all Omega carriers | (TU) / (Z-con) / (Z-gen) at j(l) | as the corresponding Step-A row; the DC bank/Z coordinate is a near coordinate NOT used by Step A (Step A uses <= 2 near coordinates per carrier: bank, and the lowered/pull coordinate is far) |
| block-norm lever (Q2 Cor 4.2 / Q2-refa C.3) | coarse peak of block m* | zero-data lever | (P6) via 2.2's repair |
| anchors (U2 TR-inf (c')) | -- | -- | (P5) |
| Step B (G1 release, static ownership) | fine carriers, far coarse parts | z on J_fine | DISPENSABLE (part 3, Lemma K1.S) |
| theta-masses W, W_F; truncation N_w (Q2 2.3) | -- | contacts off F_0 / raised support | unchanged (Q2 Theorem UE^inf, refereed) |
Coordinate bookkeeping (PROVED).  Distinct moves act on distinct coordinates: (C1)/(C2) on S^nat and T(L) \ F; Step A uses per carrier at
most one near coordinate (bank of (P2), or the two coordinates of (P3), or one of (P4)) and one far coordinate (pull or Z-lever); Lemma DC
uses a further near coordinate (six are available: <= 2 + 2 used) and far coordinates at the scale r << x_A, disjoint from Step A's (v-windows
of ratio 2^{6G(L)} contain >= 3 elements of S_l, Q1-refa P4).  Distinct carriers have disjoint signature sets; anchors are not in any
carrier's near set of Lambda by definition.  The lowered in-F coordinates are at most 2|Lambda| per system; their total lowered mass is
<= 2|Lambda| x_max = 2 T^2/(L Design(L)) = o(T^2) (x_max := T^2/(L Design(L) |Lambda|)).

## 2.4 The linearized systems; lever-regularity
SYS-A (Step A, RATIO FORM).  Q1's Step A sets active values to r''_l kappa and restores kappa by peak pushes.  Only RATIOS enter what route V
uses: the class cone in ratio variables (U1-ref 4.3: (X3)/kappa_m reads Delta'_m = sum_l r_l gamma_l), the statuses (X1 Lemma K: rho_d =
m|r_d| K(sigma, R^2)/Phi_d; sigma depends on the peak set, R^2 on the ratios of Omega), and the true shift (with exact ratios at f^#,
Delta''_m = sum r^#_l gamma_l = Delta'_m: U1 Lemma 4.6's correction term vanishes).  So we solve
   F_A(P, s) := ( val_l/kappa_{m(l)} - rt_l )_{l in Lambda_A} = 0,   rt_l := r''_l eps_l (l in Omega_act), 0 (l in H_T),
                 val_l(f_1)/kappa_{m(l)}(f_1) (l in Hold), the pushed ratio (l in D)      [ALL rows are ratio rows],
unknowns: one resource parameter P_k per k in Lambda_A := Omega(f_1) ∪ D, where Omega(f_1) := all coarse strict non-peaks of f_1 (the
route-V Omega), H_T := its nearly neutral inactive members in (T)-blocks (held at 0: KN-1, Q1-refb P-HOLD), D := D2/KN-pushed carriers
(target = current value moved inward by eta', resp. by U1-ref Prop. KN's s_0), Hold := the remaining inactive members of Omega(f_1) (target =
their value at f_1); and optional parameters s_c (one two-sided resource of a buffer peak c per block); kappa floats.  [Holding ALL coarse
strict non-peaks is free when every resource is private (their drift is then second order, X1-ref 8 "KN-1"), and NECESSARY as soon as a
common-mode resource (P4)/(P5) is used: a common mode moves every value at FIRST order (2.1(d), (e)), which would move the (U)-block statuses
(margin eta') and R^2 in Lemma K at first order.  With Lambda_A = Omega ∪ D every coarse non-peak RATIO is exact at f^(1a), so the floating
kappa moves no status (Lemma K: rho_d = m|r_d| K(sigma, R^2)/Phi_d, R^2 a function of the Omega ratios, sigma of the peak set); common modes
then move only coarse peaks (robust margins) and fine carriers.]
Linearization (PROVED from 2.1 and U1 Lemma 1.4: d kappa_m/d|zeta_c| = 1 - X_m at peaks, = rho_d M X/C for d in Omega_m, X_m <= C b^2 D^2):
   d val = (I - g h^T) dP (+ peak columns),   d kappa_m = -G_m h^T dP + (1 - X_m) lambda_c ds_c + O(X) dP,   G_m := (1 - X_m) sum_{peaks c of m}
   lambda_c vs_c eps_c g_c,
so, after multiplying the ratio rows by kappa,
   J_A = [ I - g~ h^T | col_c ],   g~ := g - (rt_l G_{m(l)})_l,   col_c := -(1 - X) lambda_c rt^{(m(c))} - h_c g~,
up to an O(X + Design^2 x) perturbation; rt^{(m)} := the target-ratio vector restricted to block m; h_k := 0 for private resources.
SYS-DC.  Q2 4.0: L(P, P_0, P_5) = N P - sum_{m* with (P6)} pi_{m*} p_{m*} P_{0,m*} - g~~ P_5 (anchors), N := D - gt h^T - sum_m p_m q_m^T.
DEFINITION (lever-regularity).  For a level L, a clean sub-window w and a class a, put
   rho_lev(w, a) := min over the two systems of  max over admissible resource assignments  of  1/||minimal right inverse of the linearization||_inf .
(LR_{w,a}): rho_lev(w, a) >= u(w)/Design(L)^{C_0} (C_0 absolute, fixed below).  f is LEVER-REGULAR (for the mate (g, rho)) if (LR_{w(L), a(L)})
holds for infinitely many main stages L, where w(L) is the clean sub-window and a(L) the class selected by Q1's pigeonhole at L.
[rho_lev is a semialgebraic function of the level-L data of f -- near moduli (R-mod), spreads, values and block data of the coarse carriers,
signs, and the combinatorial pattern -- evaluated with the resources available at w; its arguments move by <= C Design^C (mu*_J + eta' + K_w s_1)
between f, f^r, f_1 (Lemma DR-inf, Q1 CM^tr(f), Q2-refa C.7), so it is a rate object of level L up to the availability of far resources,
which is a combinatorial property of (F, a^r) at w.]

## 2.5 Lemma K1.5 (sufficient conditions for lever-regularity).  PROVED.
(a) If every carrier of Lambda_A and of Omega (Sys-DC) is privately tunable, then (LR_{w,a}) holds with C_0 an absolute constant: J_A =
    I + O(X + Design^2 x) (block triangular in the D-columns), and J_DC is X2's J = [[I - pq^T, 0],[X, I]] (no absorbers in route V: X = 0) with
    ||J^{-1}||_inf <= 1 + 4/A_min (Sherman-Morrison, q^T p <= C_m <= 1/2).
(b) If the set Lambda_4 of carriers using (P4) is nonempty and all others are privately tunable, then the square parts are I - g~ h^T (Sys-A)
    and N (Sys-DC), with h supported in Lambda_4, and:
    (b1) Sys-A is regular with constant Design^C/beta if beta := max{ |1 - h^T g~|, max_c |(1 - X) lambda_c h^T rt^{(m(c))} + h_c|, 1[anchor] } >= u,
         the max over the two-sided peak resources c; the right inverse is Q2 Proposition 4.1's with D = I (one bordering column suffices; an
         anchor column -g~ gives y^T(-g~) = -h^T g~ = -1 on the degenerate direction y = h);
    (b2) Sys-DC is regular with constant K of Q2 Proposition 4.1 if max(|c_alpha|, |beta_*|) >= u in some block with a two-sided block-norm
         lever (P6) [Q2 Prop. 4.1, Cor. 4.2 with 2.2's repair], or an anchor exists [column -g~~ with y^T g~~ = h^T D^{-1} gt != 0 on the
         degenerate direction].
(c) In particular f is lever-regular whenever, for infinitely many main stages L, every coarse carrier of level L that is tuned in the
    selected class has an off-F or thin near coordinate and (if it carries data) a pullable far coordinate at the scales x_A and r.  This
    contains Q2 Corollary 5.2 (F ∩ (union of S_l) finite, or F meeting no S_l (l <= L) in (s_max(L), s_far(w(L))]).
Proof.  (a) 2.1(a)-(c): each column is e_k + O(Design^2 x); the D-columns affect the ratio rows through kappa only (U1 Lemma 1.4) and the
D-rows have identity diagonal; Sys-DC is X2 Lemma DC (refereed).  (b) 2.1(d)-(e) give the columns; the square part of J_A is I - g~ h^T
(the peak-mediated kappa change of a (P4) column is -G_m h_k, which in the ratio rows adds +r''_l G_m h_k); det = 1 - h^T g~; when it is
small, the left null vector is h (h^T(I - g~ h^T) = (1 - h^T g~) h^T), and h^T col_c = -(1 - X)lambda_c h^T rt^{(m(c))} - h_c h^T g~ =
-(1-X)lambda_c h^T rt^{(m)} - h_c + O(|1 - h^T g~|); Q2 Proposition 4.1's proof (choose alpha or gamma by whichever scalar is >= beta_0) applies
verbatim with D = I, giving ||R|| <= C (1 + ||g~||)(1 + ||h||)(1 + max|col|)/beta.  All entries are design-bounded: |g_k| <= ||U||, |h_k| <=
Design(L)/nu (|a| <= 1, v >= 1/Design), lambda_c, |rt| <= Design^2.  (b2) is Q2 Prop. 4.1/Cor. 4.2 (refereed) with the repaired (P6).  (c) by (a).
QED

## 2.6 Lemma K1.6 (realization under lever-regularity).  PROVED.
Assume (LR_{w,a}).  Then:
(A) Step A at f^r (KN^tr with Sys-A in ratio form) produces f^(1a) with KN^tr's conclusions (a) (active ratios exactly r'' on Z_kappa, robust
    minors >= u/2), (b) ((T)-blocks: rho_d <= 1 - mu_kappa(eta'/3)/2 for active near-threshold d, held values exactly 0; (KN)-, (U)-blocks as
    there; robust statuses kept) and (c) p*(f^(1a) - f^r) <= C_f Design(L)^{C} eta' log(1/eta') + C_f T^2/(L Design(L)) = o(T^2).
(B) Lemma DC^inf at the pre-row: F has a zero (P*, P_0*) with |(P*, P_0*)| <= K_lev r, K_lev := Design(L)^{C_0}/u(w), every Omega carrier is a
    strict non-peak with nv = nv^0 exactly, peaks keep their status, and the lever masses satisfy ||X_lev|| <= C_2 r; the window conditions
    (W-b) and (LATE) hold with K_J replaced by K_lev (S2c^tr: K_lev is a design quantity, absorbed by s_late >= exp(-C log^2(1/T))).
Proof.  (A) X1-ref 8's proof, Step 4, with the joint fixed point replaced by the Poincare-Miranda argument of Q2 Corollary 4.2 for the map
G(y) := F_A(0) + y + Rem(R_b y) on the cube |y| <= rho_A, R_b the minimal right inverse (norm <= 1/rho_lev): G_l >= rho_A - |F_A(0)| -
C_2 ||R||^2 rho_A^2 >= 0 on the faces y_l = rho_A when ||R|| |F_A(0)| <= rho_A/2 and C_2 ||R|| rho_A <= 1/4.  Here |F_A(0)| <= C Design eta' (the
Lojasiewicz displacement |r'' - r_1| <= eta' times Design, plus the KN-1/D2 targets <= C b), so rho_A := 2||R|| C Design eta' <= Design^{C}
eta'/u, and the quadratic remainder constant C_2 <= Design^C/u^C (2.1: second-order cross effects O(Design^2 u^{-4})), so C_2 ||R|| rho_A <=
Design^C u^{-C} eta' <= 1/4 because eta' = T^4/(L Design(L)) and u(w) >= T_hi(w)^{1/20} >> T (Q(w) >= (4 Design/u)^{20}).  Resource sizes are <=
||R|| rho_A in value units, i.e. masses <= Design^C eta'/u, so all the cost and status estimates of X1-ref 8 hold with eta' replaced by
Design^C eta'/u -- still << b-independent margins: robust statuses move by Design^C eta'/u << u; the Puiseux protection uses only the EXACT
ratios and the exact held values (KN-1), not the size of the moves (Q1-refa F1, Q1-refb E7).  The lowering of in-F far coordinates costs
<= 2T^2/(L Design) (2.3).  (B) Q2 Corollary 4.2's proof with R from (LR): K|F(0)|_inf <= r/2 holds for r := 4K_lev(...) as in X2-ref (p-DC1);
remainder constants are design quantities by 2.1; (S-mass) range: |P| <= K_lev r keeps |A(p)| >= |A_1(p)|/2 (Q2-refa (p2.2), (LATE)).  QED

## 2.7 Lemma K1.7 (structure of the non-lever-regular configurations).  PROVED.
If (LR_{w,a}) fails, then in at least one of the two systems the set Lambda_np of carriers that are NOT privately tunable is nonempty, and:
 (i) every l in Lambda_np is (U) UNPULLED -- nonzero-data, N_l ∩ F_thick = {} and no pullable far coordinate at the scale x -- or (S)
     SUPPORT-SWALLOWED -- N_l ⊂ F_thick with all pairwise spreads tiny;
 (ii) if Lambda_np consists of (S)-carriers only, then no anchor exists (P5), and the bordered scalars of 2.5(b) are tiny:
     |1 - h^T g~| <= u and |(1 - X)lambda_c h^T rt^{(m(c))} + h_c| <= u for every two-sided peak resource c (Sys-A), resp. |c_alpha|, |beta_*| <= u
     in every block with a two-sided block-norm lever (Sys-DC);
 (iii) EXACT LIMIT.  If (ii) holds with all tiny quantities exactly 0 for a fixed set of (S)-carriers and h^T D^{-1} p_m = 0 in every block, then
     u_h := sum_{l} h_l eps_l u_l satisfies P_F (I - e e^T) U^* u_h = 0, hence (Q2 Lemma 4.3) u_h|_F = kappa a|_F, and if kappa != 0, then
     (U2 Lemma ND) F minus the targets of these carriers lies in their signature sets with a_s = (c_l/kappa) v_l(s) there.
Proof.  (i) A carrier without (P1)-(P3): by the clean dichotomy N_l ⊂ (off F) ∪ F_thin ∪ F_thick.  If N_l meets F_thick and has no robust-spread
pair it has (P4) only (S), unless it has an off-F/thin near coordinate, in which case, being not privately tunable, it is nonzero-data
without a pullable far coordinate; if moreover N_l ∩ F_thick != {} it has (P4) and belongs to the (P4)-set of 2.5(b) -- such carriers do not
by themselves break (LR) (2.5(b) applies) -- otherwise it is (U).  A zero-data carrier with an off-F/thin near coordinate has (P1).  (ii) If only (S)-carriers lack private resources, 2.5(b) shows that (LR) can fail only if all the
listed scalars are <= u (with u = b(w^-) the next band: at a clean w they are tiny) and no anchor exists.  (iii) The left null vector of the
square part is y = h (Sys-A) resp. D^{-T}h (Sys-DC, Q2 4.4(ii)); a support move at s in F changes y^T(values) by (mu_s^2 A(s)/nu)[u_h(s) -
<U^* u_h, e> a_s/nu] (2.1(d)); its vanishing for all s in F is P_F(I - e e^T)U^* u_h = 0; Q2 Lemma 4.3 and U2 Lemma ND (both refereed).  QED
Remarks.  (1) The (U)-case is new (finite F never sees it): a data-carrying carrier whose deep signature set is support of the opposite sign
(or super-thick, |a^r_j| > x_max at every pullable depth) has only a ONE-sided private lever (its bank: eps_l val_l can only go up).
RATIO TRICK (SKETCH).  In ratio form, if block m has a two-sided buffer-peak resource and all (U)-carriers of m have target ratios rt_l of one
common sign, a correction delta of the ratios is realized with one-sided banks: if rt_l > 0 for all (U)-carriers of m, raise kappa_m by
dkappa := kappa max(0, max_U(-delta_l/rt_l)) and set the bank moves du_l := kappa delta_l + rt_l dkappa >= 0 (other carriers two-sided); if all
rt_l < 0, lower kappa_m symmetrically.  The nonlinear version needs a Brouwer argument on a cone-shaped parameter domain (not written).  Mixed
signs of the (U)-ratios inside one block are not covered.  (2) (S)-configurations at all large levels are (NDN)-type (U2 3.3, U2-ref G3) and contain Q2's (NDN2); their
exact versions have the Lemma ND structure (iii).  Both are handed over to K2 (O-c).
