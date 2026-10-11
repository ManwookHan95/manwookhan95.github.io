# H1 notes (Round 13): the (R0) residual of Step A -- first-order Puiseux margin, target freedom as a lever, the alignment
# calculus and the unit calculus; precise remaining sub-class

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED (mod chain)" = proved here modulo the refereed chain that J1.15' (J1-ref) and
J2's Theorem J2.1 already cite (X1/X1-ref, X2/X2-ref, Q1/Q1-ref a,b, cert0-3, Q2/Q2-ref a, K1/K1-ref, K2/K2-ref, J1/J1-ref, J2/J2-ref; several
links once-refereed).  Part files: r13/H1_part1.md (J1.11), H1_part2.md (Lemma TF, Lemma NP, Theorem RL, Lemma KC), H1_part3.md (alignment
calculus), H1_part4.md (unit calculus, residual).  Scripts and outputs: r13/H1_work/.  This file supersedes the part files where they differ.

## 0. Bottom line
(1) PROPOSITION J1.11 IS PROVED (Section 2): for the generic-weight design every pattern has a FIRST-ORDER Puiseux margin, mu_kappa(h) >=
    c_kappa h.  The missing "semialgebraic uniformity lemma" is supplied by a stratified projected flow: Whitney (a) alone lets the flow of
    P_{T S'} v drop through finitely many strata with velocity within eps|v| of v (no reach/curvature bound is needed), and genericity is
    applied to the k-definable set where the linear margin fails, which lies inside the critical-value cylinders of semialgebraic Sard.
    Consequence: (R-T) is EMPTY, and KN-1 exactness (inactive nearly neutral values of (T)-blocks held exactly at 0) can be relaxed to bands
    of half-width >> beta_*, with no design change (Corollary 2.4).
(2) TARGET FREEDOM IS A LEVER (Lemma TF, Section 3): any admissible target displacement whose pairing <kappa y, Delta> is robustly positive
    for ALL near-certificates makes Step A A-regular.  J1.9's band is the special case Delta = +-e_k.
(3) ALIGNMENT CALCULUS (Sections 4-5).  Call a thick-type carrier l ALIGNED if rho_l u_l(xhat) > 0 (its thick private coordinates carry the
    sign of its own value), ANTI-ALIGNED otherwise.  Every near-certificate asks aligned carriers to move INWARD and anti-aligned ones
    OUTWARD (Lemma AL; the sign does not depend on the certificate).  Inward moves never hurt statuses, so every MOVABLE aligned thick-type
    row (inactive, or active with a free ratio) relieves Step A in ANY block, without peak resource or coupling (Theorem IN).  Anti-aligned
    movable rows relieve when the block is unprotected or has an exchange partner (Theorem OUT).
(4) PEAK-RESOURCE DICHOTOMY AND RESCALING LEVERS IN UNSHIFTED BLOCKS (Sections 4, 6).  In a (U)-block either a private two-sided peak resource
    kills zeta_m (R-PK), or every peak is thick-type and zeta_m has a robust sign sigma_m = sgn(rho_c vs_c) common to all certificates
    (Lemma NP).  Down-scaling any union of "units" (pinned groups, single movable rows) is always admissible (Lemma DS); with a peak resource
    the whole block is neutral, so the complement of a unit may be scaled instead (Theorem UC).  Hence in a (U)-block with a peak resource
    a residual stage has NO movable thick row at all (this covers J1's (R-np), (R-D2), (J-c)/(J-d) without bands), and every pinned group is
    BALANCED (sum of rho_l u_l over its thick rows ~ 0); without a peak resource, sigma_m = -1 is relieved by whole-block down-scaling
    (Theorem RL) and sigma_m = +1 leaves the class (U+).
(5) FORCED MIXED ALIGNMENT (Proposition MA): in a block with a peak resource the frozen value sum rho_l u_l(xhat) of the thick rows vanishes up
    to kind-(iv) compensation; so at residual stages the stable-exact relation Phi_0^{(m)}(zhat) ~ 0 holds by CANCELLATION between aligned and
    anti-aligned PINNED carriers.
(6) RESIDUAL (Section 8; precise, necessary condition): (H-1)-(H-7).  In words: in unshifted blocks only balanced pinned groups (with a peak
    resource) or the aligned-peak class (U+) (without); in shifted blocks only anti-aligned movable rows without exchange partner (an
    anti-aligned proportional resonance) and "outward-wanting near-threshold rows" (the polar/normal resonance of the exact set).  All are
    codimension >= 1 coincidences of f's stage data or alignment patterns that must persist at ALL large main stages.
(7) (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): OPEN (reduced further).  No counterexample is
    claimed or suggested.

| # | Result | Status | Section |
|---|---|---|---|
| 1 | Lemma 2.2 (stratified projected flow: almost-straight curves inside Z) | PROVED | 2 |
| 2 | Proposition J1.11 (first-order Puiseux margin for the T_fin weights) | PROVED | 2 |
| 3 | Corollary 2.4 ((J-e) holds at every main stage: (R-T) empty; KN-1 exactness unnecessary) | PROVED (mod chain) | 2 |
| 4 | Lemma TF / TF' (target freedom as a lever) | PROVED (mod chain) | 3 |
| 5 | Lemma NP (peak-resource dichotomy in (U)-blocks; robust fixed-sign zeta_m) | PROVED (mod chain) | 4 |
| 6 | Theorem RL (block-rescaling lever) | PROVED (mod chain) | 4 |
| 7 | Lemma KC (inward compensation in case (U+)) | PROVED (mod chain) | 4 |
| 8 | Lemma AL (needed direction: inward iff aligned) | PROVED (mod chain) | 5 |
| 9 | Theorem IN (inward relief, any block) | PROVED (mod chain) | 5 |
| 10 | Theorem OUT (outward relief: unprotected block, exchange, coupling) | PROVED (mod chain) | 5 |
| 11 | Theorem GS (group rescaling of pinned ratios in (U)-blocks) | PROVED (mod chain) | 5 |
| 12 | Proposition MA (forced mixed alignment with a peak resource) | PROVED (mod chain) | 5 |
| 13 | Lemma DS, Theorem UC, Lemma TG (unit calculus and linear-group tangent directions in (U)-blocks) | PROVED (mod chain) | 6 |
| 14 | Peak conversion of anti-aligned near-threshold zero-data rows | SKETCH | 7 |
| 15 | Residual (H-1)-(H-7) | PROVED as a necessary condition; OPEN whether it can persist | 8 |
| 16 | (T)-block reading: residual = outward-wanting near-threshold actives | PROVED (characterization) | 8 |
| 17 | (LSC-trunc)_N for every f; density for p_N, p | OPEN | 10 |

## 1. Setting and notation
Design T_fin^{K2} (K2 6.1) with J2's frozen convention (FC), J1-ref's P-TU windows and F-2 coupling.  N >= 1; f in S_{p_N*} with forced data
f = a + L^*w, q*(a) = ||a||_1 + nu = 1, e = U^*a/nu, zhat = z + Ue (diagonal base); g in C(f); rho in (0, 1).  Main stage L >= l_f, clean
sub-window w, class a; b = b(w), u = u(w), T = T_lo(w), eta' = T^4/(L Design(L)), x = C Design(L) eta' (Step-A scale), D = D(L).  Step A
(Sys-A, K2 5) at the input row R_1 = f_1 + Pi: rows l (all coarse strict non-peaks, plus D-pushed), Ft_l(rt) = val_l - rt_l kappa_{m(l)},
val_l = eps_l u_l(xhat_1), targets rt; b(rt) := -Ft(rt), W(rt) := Design^{C_A} u^{-3} max(x, ||b(rt)||), rho_0(rt) := C_2 W(rt)^2.  A NEAR-
CERTIFICATE of size eps at rt is a unit y with y^T g >= -eps for all generators g (|y^T g| <= eps for two-sided ones); phi_y(rt) := y^T Ft(rt);
eps_* := Design(L)^{-C} (K2.16); kappa_y := <U^*Psi_y, e_1>/nu_1 <= -c_*/nu_1 (K2.16(3)); zeta_m(y; rt) := sum_{l in m} y_l rt_l;
<kappa y, Delta> := sum_l kappa_{m(l)} y_l Delta_l.  THICK-TYPE carrier l: a coarse carrier (row or peak) with a thick private coordinate p in
S_l ∩ [1, D] (|a_p| >= u/2); rho_l := a_p/v_l(p) (J1.6(a): coef_l = kappa_y rho_l + O(eps Design^2) for every near-certificate).  vs_l :=
sgn u_l(xhat_1).  A row is MOVABLE if it is inactive (hold, D2/KN-pushed, KN-1) or active with a FREE ratio (in no tiny minor or tiny cofactor
polynomial, J1.13); otherwise PINNED.  Status classes at f: nearly neutral (rho <= b), robust (u <= rho <= 1 - u), near-threshold (|rho - 1|
<= b, incl. D2/KN-pushed and (FC)-frozen active weak peaks).  A block is PROTECTED if it contains a row whose status must stay below 1 with a
margin <= Design^C eta' (near-threshold actives, D2/KN-pushed rows).

## 2. Proposition J1.11: the first-order Puiseux margin.  PROVED.
Objects (X1 2.3-2.5, cert1 2, W-fix).  Fix a level L and a pattern kappa; N_T := the active near-threshold carriers of its (T)-blocks, n := |N_T|.
K_kappa := {r : R_a(m)(r)^2 <= 1 - sigma_rob(m)/4 for every active block m}; Z := Z_kappa ∩ K_kappa (compact semialgebraic); psi_d(r) :=
m(d) |r_d| K(sigma_rob(m(d)), R_a(m(d))(r)^2) (d in N_T; K Nash on (0, inf) x [0, 1)); for Phi in (0, inf)^{N_T}: F_Phi := max_d psi_d/Phi_d,
Y_1 := Z ∩ {F_Phi <= 1}, G_h(r) := inf{F_Phi(r'') : r'' in Z, |r'' - r| < h}, mu_Phi(h) := 1 - max_{Y_1} G_h (:= 1 if Y_1 = {}).  k := k_0(weights of
the carriers of kappa outside N_T); Z, K_kappa, psi_d are defined over k and independent of Phi (X1 2.2(iv)); the T_fin weights Phi^T :=
(Phi_d)_{d in N_T} are algebraically independent over k (GEN_fin).
Tools: [W] every semialgebraic set has a finite stratification into connected Nash submanifolds satisfying the frontier condition (if
S' ∩ cl(S) != {} for strata S != S' then S' ⊂ cl(S) \ S and dim S' < dim S) and Whitney's condition (a) (if x_n in S, x_n -> y in S', T_{x_n} S
-> tau, then T_y S' ⊂ tau), compatible with finitely many given semialgebraic subsets [Bochnak-Coste-Roy 9.7.11; van den Dries-Miller, Duke
Math. J. 84 (1996) 4.8; Loi, Illinois J. Math. 42 (1998)]; [SS] semialgebraic Sard: the critical values of a Nash map S -> R^D form a
semialgebraic set of dimension < D [BCR 9.6.2]; [TS] Tarski-Seidenberg; [GEN] a k-definable semialgebraic set of dimension < n contains no
point with coordinates algebraically independent over k (cert1 4).

2.1 Regular contact points.  Fix a stratification Sigma of Z as in [W], compatible with {r_d > 0}, {r_d = 0}, {r_d < 0} (d in N_T).  For
nonempty D ⊂ N_T and a stratum S ⊂ ∩_{d in D}{r_d != 0}, Psi_{D,S} := (psi_d)_{d in D}|_S is Nash; CV_{D,S} := its critical values;
B^reg := ∪_{(D,S)} {Phi : (Phi_d)_{d in D} in CV_{D,S}}, of dimension < n by [SS].
LEMMA 2.1.  PROVED.  If Phi notin B^reg, r_* in Lambda := Z ∩ {F_Phi = 1}, D := {d : psi_d(r_*) = Phi_d}, S := the stratum of r_*, then there is
v in T_{r_*} S with d psi_d(r_*) v = -Phi_d for all d in D.
Proof.  psi_d(r_*) = Phi_d > 0 forces r_{*,d} != 0, so S ⊂ {r_d != 0} (d in D); if d Psi_{D,S}(r_*) were not onto, Phi_D = Psi_{D,S}(r_*) would be a
critical value.  QED

LEMMA 2.2 (stratified projected flow).  PROVED.  Let r_* in Z, S its stratum, 0 != v in T_{r_*} S, eps in (0, 1).  There is delta > 0 such that
for every y in Z with |y - r_*| < delta and every t in [0, delta/(2|v|)] there is a Lipschitz curve gamma : [0, t] -> Z with gamma(0) = y,
|gamma(s) - r_*| < 2 delta, |gamma'| <= |v| and |gamma' - v| <= eps |v| almost everywhere.
Proof.  (i) Finitely many strata; those with r_* notin cl(S') have positive distance from r_*: choose delta so that B(r_*, 2 delta) meets only
strata S' with r_* in cl(S').  For S' != S the frontier condition gives S ⊂ cl(S'), dim S < dim S', and (W2) holds for (S', S) at r_*.  Shrinking
delta: dist(v, T_x S') <= eps|v| for all such S' and x in S' ∩ B(r_*, 2 delta) -- for S' = S by continuity of T S; for S' != S, otherwise
x_n -> r_* with dist(v, T_{x_n} S') > eps|v|, and a subsequence T_{x_n} S' -> tau (compact Grassmannian) with v in T_{r_*} S ⊂ tau gives
dist(v, T_{x_n} S') -> 0.  (ii) On such S', V_{S'}(x) := P_{T_x S'} v is a smooth tangent field with |V_{S'}| <= |v|, |V_{S'} - v| <= eps |v|.  Its
maximal integral curve in S' from x_0, if it stops at tau_max before the budget, converges (|gamma'| <= |v|) to x_1 in cl(S') \ S' (if x_1 were
in S', a compact neighbourhood of x_1 in S' would contain gamma(s) near tau_max, contradicting the escape lemma), and x_1 lies in a stratum
of smaller dimension (frontier condition).  (iii) Concatenate from y: dimensions strictly decrease, so at most dim Z + 1 pieces; the curve
stays in Z (pieces in strata, junctions in Z) and in B(r_*, 2 delta) (|gamma(s) - y| <= |v| s <= delta/2).  No piece lies in a point stratum
(dist(v, {0}) = |v| > eps|v|).  QED

PROPOSITION J1.11.  PROVED.  (a) If Phi notin B^reg there are c, h_0 > 0 with mu_Phi(h) >= c h for 0 < h <= h_0.  (b) For the T_fin weights,
for every pattern kappa of every level: mu_kappa(h) >= c_kappa h on (0, h_kappa] (Puiseux exponent beta_kappa <= 1 in Lemma QC(c)).
Proof.  (a) Local step at r_* in Lambda (Lemma 2.1 gives D, v): psi_d (d in D) is real analytic near r_*; m_* := (1 - max_{d notin D}
psi_d(r_*)/Phi_d)/4 > 0 (1/4 if D = N_T).  Choose eps with eps(1 + |v| max_D sup |d psi_d|/Phi_d) <= 1/4, then delta from Lemma 2.2 and so small
that |d psi_d(x) - d psi_d(r_*)||v| <= eps Phi_d (d in D) and psi_d/Phi_d <= 1 - 2 m_* (d notin D) on B(r_*, 2 delta).  For y in Z ∩ B(r_*, delta),
t <= delta/(2|v|), d in D:  psi_d(gamma(t)) - psi_d(y) = int_0^t [d psi_d(r_*) v + (d psi_d(gamma) - d psi_d(r_*)) v + d psi_d(gamma)(gamma' - v)] ds
<= -(3/4) t Phi_d; hence F(gamma(t)) <= max(F(y) - 3t/4, 1 - 2 m_*).  Covering: Lambda compact; if Lambda = {} then F <= 1 - m_U on the compact
Y_1 and mu >= m_U.  Else cover Lambda by finitely many B(r_*^i, delta_i), U their union; F <= 1 - m_U on Y_1 \ U; V := max|v_i|.  For r in Y_1 ∩
B(r_*^i, delta_i) and h small, t := h/(2|v_i|): |gamma(t) - r| <= h/2 and F(gamma(t)) <= 1 - 3h/(8V); for r notin U, G_h(r) <= 1 - m_U.  So mu(h) >=
3h/(8V) for h <= h_0.  (b) B^lin := {Phi : no c, h_0 > 0 with mu_Phi(h) >= ch on (0, h_0]} is first-order definable over k ("for all r in Z with
F_Phi(r) <= 1 and all e > 0 there is r'' in Z, |r'' - r| < h, F_Phi(r'') < 1 - ch + e"), hence k-semialgebraic [TS]; by (a) B^lin ⊂ B^reg, so
dim B^lin < n; by [GEN], Phi^T notin B^lin.  QED
Remarks.  (1) This fills the gap in J1 4.1 / J1-ref B.4: no local reach of the strata is needed, because the flow may drop to lower strata
and Whitney (a) gives every nearby stratum a velocity within eps|v| of v.  (2) Sigma need not be defined over k (dimension is intrinsic;
genericity is applied to B^lin).  (3) If Lambda != {} also mu <= Lip_kappa h (cert1 Q1): the exponent is exactly 1.  (4) Design(L) >=
max(1/c_kappa, 1/h_kappa) (P-CHOICE, cert1 Q2), so mu_kappa(eta'(w)/3) >= eta'(w)/(3 Design(L)).

COROLLARY 2.4 ((R-T) is empty).  PROVED (mod chain).  At every main stage L >= l_f, every w, a: mu_kappa(eta'/3) >= C D^C m^2 (beta_*/kappa_m)^2 (condition
(J-e) of J1.15').  Hence a zero-data (KN-1) thick-type carrier of a (T)-block is always band-relievable, and X1's KN-1 exactness can be
relaxed to |value| <= kappa_m (mu_kappa(eta'/3)/(C D^C m^2))^{1/2} (>= eta'^{1/2}/Design^C >> beta_*).
Proof.  beta_* = 16 nu_1 (||b|| + 2 rho_0)/(c_* u), ||b|| <= Design^C x, rho_0 << x, and nu_1, c_*, kappa_m, m, |Lambda_A| are bounded by Design^C for
L >= l_f: the right side is <= Design^{C'} eta'^2/u^2; the left side is >= eta'/(3 Design) (Remark 4); eta' = T^4/(L Design) with T <= (u/(4 Design))^{L^2
+ 20} gives eta' <= u^2/Design^{C'+1}.  No design change: beta_kappa <= 1 is a property of the existing generic weights.  QED
Numerics (H1_work/puiseux_toy*.py): cone-shaped Z with the threshold set near the vertex: m/D(m) in [2.35, 4.26] (fitted exponent 1.06-1.15
on resolved scales); cusp-shaped Z with a CRITICAL tip on Lambda (coincidence weights): mu ~ h^{1.495}; weights perturbed by 1e-3: exponent
1.05-1.07 (m/D(m) -> 0.46).  Genericity is necessary and sufficient as proved.

## 3. Lemma TF (target freedom as a lever).  PROVED (mod chain).
LEMMA TF'.  Let rt_0 be admissible targets (J1.13 (i)-(ii)) and rt' another admissible target vector with ||kappa (rt' - rt_0)|| <= Design^C
(||b(rt_0)|| + x)/u.  If every near-certificate y of size <= eps_* at rt_0 satisfies <kappa y, rt' - rt_0> >= 4(||b(rt_0)|| + x), then Step A at
the targets rt' is A-regular, hence realized (K2.9(c); data projected at the realized ratios, J1.13 (iii)).
Proof.  Ft(rt') = Ft(rt_0) - (kappa_{m(l)} (rt'_l - rt_{0,l}))_l, so ||b(rt')|| <= Design^C (||b(rt_0)|| + x)/u, W(rt') <= Design^{C_A+C} u^{-4}
(||b(rt_0)|| + x) (the order of J1.9's bands; P-TU's x_TU >= 24 W(rt') as for J1's bands) and rho_0(rt') <= x/4 (x, ||b|| <= Design^C eta',
eta' <= (u/Design)^{4L^2}).  If Step A were not A-regular at rt', K2.9(b) would give a near-certificate y at rt' of size < 4 Design^{-C_A} u^3 with
phi_y(rt') > -rho_0(rt').  The normalized generator columns depend on the targets Lipschitz-continuously with constant C_G <= Design^C (peak
columns -(1 - X) lambda_c rt^{(m)} and the gtil-terms, J1-ref P-1), and C_G |rt' - rt_0| <= eps_*/2, so y is a near-certificate of size <= eps_* at
rt_0.  Then phi_y(rt') = phi_y(rt_0) - <kappa y, rt' - rt_0> <= ||b(rt_0)|| - 4(||b(rt_0)|| + x) < -x/4 <= -rho_0(rt'): contradiction.  QED
Remark.  J1.9 (band of half-width beta_* on a thick-type row k) is the case rt' - rt_0 = +-(beta_*/kappa_m) e_k.

## 4. Unshifted blocks: the peak-resource dichotomy and the rescaling levers
LEMMA NP.  PROVED (mod chain).  Let m be a (U)-block (Delta'_m = 0 in the class) at a stage carrying a near-certificate of size <= eps_*.
 (a) If m has a private two-sided peak resource (FR z-move or ZD composite at a design-depth coordinate private to a coarse peak of m), then no
     coarse peak of m is thick-type and |zeta_m(y; rt)| <= (4/3) eps Design for every near-certificate (J1-ref R-PK, B.2).
 (b) Otherwise every coarse peak c of m is thick-type; rho_c vs_c/lambda_c is the same for all peaks up to C eps Design^2/u; and for every
     near-certificate y:  sgn zeta_m(y; rt) = sigma_m := sgn(rho_c vs_c)  and  |zeta_m(y; rt)| >= z_0 := c_* u/(4 nu_1).
     sigma_m = +1 means ALIGNED peaks (their thick private coordinates carry the peak's sign).
Proof of (b).  Peaks of a (U)-block carry no class data (gamma_p = -Delta'_m lambda_p vs_p = 0; the aggregated (X1) row on a peak's private
coordinates multiplies -Delta'_m vs_p lambda_p = 0).  A design-depth coordinate private to c lies in U_L, hence is TS, S_th, FR or ZD (K2 4.1(d));
an S_th coordinate of c carries no data and is ZD.  FR and ZD private coordinates are peak resources; so all private design-depth coordinates
of all peaks are TS; the near coordinates N_c ⊂ [1, D] are private: c is thick-type.  J1.6(a) (valid for peaks): coef_c = kappa_y rho_c +
O(eps Design^2), |rho_c| >= u/2.  For an untuned carrier coef_c = -zeta_m lambda_c (d kappa_m/d zeta(c)); kappa_m depends on the block vector only
through |zeta(k)| (the block norm is invariant under coordinate sign changes), so d kappa_m/d zeta(c) = vs_c (1 - X_m) with 1 - X_m in [3/4, 1]
under (FC) (U1 Lemma 1.4(a)).  Hence zeta_m = -kappa_y rho_c vs_c/(lambda_c (1 - X_m)) + O(eps Design^2/lambda_c): sign sgn(rho_c vs_c) (kappa_y < 0),
modulus >= c_* u/(4 nu_1) (lambda_c <= 1).  Two peaks share zeta_m and 1 - X_m.  QED  [Numerics: d kappa/d zeta(c) = +-1.0000, flipping with
sgn zeta(c), H1_work/rescale_toy.out.]

THEOREM RL (block-rescaling lever).  PROVED (mod chain).  Let m be a (U)-block without private two-sided peak resource at a stage carrying a
near-certificate.  If sigma_m = -1, or sigma_m = +1 and m has no near-threshold coarse non-peak (every coarse strict non-peak and weak peak
of m has rho(f) <= 1 - u), then Step A is realized with all targets of m (actives, holds, D2/KN-pushed; KN-1 zeros unchanged) multiplied by
s := 1 + sigma_m delta, delta := 4(||b|| + x)/(kappa_m z_0).
Proof.  Lemma TF' with rt' - rt = sigma_m delta rt^{(m)}: pairing sigma_m delta kappa_m zeta_m >= delta kappa_m z_0 = 4(||b|| + x).  Admissibility:
in a (U)-block r^{(m)} occurs only in (X3)_m, minors and cofactor polynomials are homogeneous in r^{(m)} (X1-ref D1): Z_kappa is preserved, robust
minors change by a factor >= 1/2; inactive targets enter only through statuses.  Statuses (Lemma K, rho_d(s rt) = m s|rt_d| K(sigma, s^2 R^2)/
Phi_d): s < 1 lowers all of them; for s > 1 under the hypothesis every non-peak status of m is <= 1 - u at f, hence <= 1 - u/2 after the
rescaling (delta << u), nearly neutral ones stay tiny, robust peaks move by << u.  Distance and the size condition: delta ||rt^{(m)}|| <=
Design^C (||b|| + x)/u.  QED

LEMMA KC (inward compensation in case (U+)).  PROVED (mod chain).  Let m be a (U)-block without peak resource, sigma_m = +1, and N_0 a set of
INACTIVE rows of m containing every D2-pushed row of m and a row d_0 with robust status, such that y_l rt_l <= z_0 u^2/(4|N_0| Design^{C_K}) for
every near-certificate y and l in N_0 (e.g. l of kind (i), or l aligned thick-type: y_l rt_l <= 0 by Lemma AL).  Then Step A is realized.
Proof.  rt'_l := (1 + delta) rt_l for rows of m outside N_0 (KN-1 zeros unchanged), rt'_l := (1 - lambda_l) rt_l on N_0 with lambda_l := delta on
N_0 \ {d_0} and lambda_{d_0} chosen so that R^2 of m decreases by 3 delta (R^2 + 8.5/c_K): then K(sigma, R'^2) <= K(sigma, R^2)/(1 + delta)
(dK/dR^2 >= k^2/(2a) >= c_K > 0 and K <= 8.5 on the W-fix region, cert1 1), so no status of m increases; lambda_{d_0} <= delta Design^{C_K}/(2u^2)
because m|rt_{d_0}| = rho_{d_0} Phi_{d_0}/K >= u Phi_{d_0}/K.  Pairing: kappa_m (delta zeta_m - sum_{N_0} (delta + lambda_l) y_l rt_l) >= kappa_m delta z_0/2.
Lemma TF'.  QED

## 5. The alignment calculus
DEFINITION.  A thick-type carrier l with robust or near-threshold status is ALIGNED if rho_l vs_l > 0 (equivalently rho_l u_l(xhat_1) > 0: its
thick private coordinates contribute to u_l(xhat) with the sign of u_l(xhat)), ANTI-ALIGNED if rho_l u_l(xhat_1) < 0.  These are f's data (up
to O(b) preprocessing), constant along the stages at which l is thick-type.  For a row l with robust or near-threshold status put
Q_l(y) := y_l/rt_l.

LEMMA AL (needed direction).  PROVED (mod chain).  For every near-certificate y of size eps <= eps_* and every thick-type row l with robust or
near-threshold status:
      y_l rt_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 + Design(eta' + b) + C b^2 D^2),
which is robust (|kappa_y rho_l u_l(xhat_1)|/kappa_m >= (c_*/nu_1)(u/2) u Phi_l/(m K)); so sgn(y_l rt_l) = -sgn(rho_l u_l(xhat_1)) for ALL
near-certificates, and Q_l(y) = kappa_y kappa_m rho_l/u_l(xhat_1)(1 + o(1)) (< 0 aligned, > 0 anti-aligned).  For kind-(i) rows, Q_l(y) = o(1).
Proof.  y_l = eps_l coef_l + zeta_m lambda_l (d kappa_m/d zeta(l)) with |d kappa/d zeta(l)| = rho_l M X_m/C <= C b^2 D^2 for coarse strict non-peaks in
route V under (FC) (J1-ref B.3) and |zeta_m| <= C; coef_l = kappa_y rho_l + O(eps Design^2) (J1.6(a)); rt_l = rc_l + O(eta' + b) with rc_l =
eps_l u_l(xhat_1)/kappa_m; |rc_l| >= u Phi_l/(m K) by Lemma K.  Multiply (eps_l^2 = 1).  Kind (i): |coef_l| <= eps Design^2 (K2.16(2a)).  QED
Reading: a displacement Delta_l pairs positively (kappa_m y_l Delta_l > 0) iff sgn(Delta_l rt_l) = -sgn(rho_l u_l): aligned rows must move
INWARD (|rt_l| down), anti-aligned rows OUTWARD.

THEOREM IN (inward relief).  PROVED (mod chain).  If some movable thick-type row l is aligned (robust or near-threshold status), or is movable
and nearly neutral (any alignment), then Step A is realized -- in any block, with no peak resource and no coupling.
Proof.  Aligned: rt'_l := (1 - s) rt_l, s := 8 nu_1 (||b|| + x)/(c_* u kappa_m |rc_l|) (<= Design^C x/u << 1).  Pairing -s kappa_m y_l rt_l = s |kappa_y
rho_l u_l| (1 + o(1)) >= 4(||b|| + x) (Lemma AL).  Admissibility: l is inactive or free (Z_kappa untouched; robust minors move by << u);
l's own status decreases (Lemma K: |r_l| and K decrease); R^2 (full Omega sum; R_a^2 in (T)-blocks if l is active) decreases, so every other
status of the block decreases; robust peaks move by << u; (X4^0) rows (only in (T)-blocks) are not tiny for a free ratio; the class data are
projected at the realized ratios (the original data violate the moved (X3)/(X1)/(X4^0) rows by <= |rt' - rt| ||gamma|| <= Design^C x/(u t) <<
K t).  Lemma TF'.  Nearly neutral: |y_l| >= c_* u/(8 nu_1) (J1.6(a)); rt'_l := rt_l + sgn(y_l) beta_*/kappa_m; pairing >= |y_l| beta_* >= 4(||b|| + x);
the R^2 change m^2 (beta_*/kappa_m)^2 + 2 m^2 |rt_l| beta_*/kappa_m <= Design^C ((x/u)^2 + bx/u) moves every protected status by << eta' in
(U)/(KN)-blocks and by << mu_kappa(eta'/3) in (T)-blocks (Corollary 2.4).  QED

THEOREM OUT (outward relief).  PROVED (mod chain).  Let k be a movable anti-aligned thick-type row with robust status in block m.  Step A is
realized if (a) m is not protected; or (b) m contains another movable row d with robust or near-threshold status and Q_d(y) <= Q_k(y) - c_ex
for all near-certificates (c_ex := c_* u kappa_m/(C nu_1 Design^C); e.g. d aligned, or d of kind (i)); or (c) m is a (U)-block with a private
peak resource (J1.15' (J-c)/(J-d) with F-2, or Theorem UC below); or (d) m is a (U)-block without peak resource with sigma_m = -1 (Theorem RL).
Proof.  (a) rt'_k := (1 + s) rt_k: pairing s kappa_m y_k rt_k = s |kappa_y rho_k u_k| > 0; k robust (room u); the R^2 increase moves the other
(robust or nearly neutral) statuses of m by <= Design^C x/u << u.  (b) EXCHANGE: rt'_k := rt_k + t/rt_k (outward), rt'_d := rt_d - t/rt_d (inward),
t := Design^C (||b|| + x)/c_ex: R^2 changes by 2m^2 (t - t) + O(t^2 (rt_k^{-2} + rt_d^{-2})) = O(Design^C t^2) << eta' (second order); k has room
u, d decreases; pairing kappa_m t (Q_k - Q_d) >= kappa_m t c_ex >= 4(||b|| + x).  Lemma TF'.  (c), (d): as cited.  QED

THEOREM GS (group rescaling of pinned ratios).  PROVED (mod chain).  Two pinned active ratios are LINKED if a tiny minor or tiny cofactor
polynomial contains both; a GROUP is a connected component of the linking graph.  Let G be a group contained in (U)-blocks.  Then
(a) rt^G(s) := (s rt_l for l in G, rt_l otherwise) lies in Z_kappa for every s > 0 (a tiny polynomial P involves the ratios of exactly one
group; X1-ref D1: in a (U)-block m, P(.., s r^{(m)}, ..) = s^{e_m} P(..), and P does not depend on the ratios of m outside G); robust minors move
by << u for |s - 1| <= Design^{-C};
(b) if for all near-certificates zeta^G_kappa(y) := sum_{l in G} kappa_{m(l)} y_l rt_l <= -kappa_max(G) z_G (z_G := c_* u^3/(C nu_1 Design^C)),
Step A is realized with s := 1 - 4(||b|| + x)/(kappa_max(G) z_G) (down-scaling lowers every status; Lemma TF');
(c) if zeta^G_kappa(y) >= kappa_max(G) z_G for all y, Step A is realized with s > 1 provided no row of G is near-threshold and each block met by
G is unprotected or has an inward exchange row d with Q_d <= -c_ex (aligned or kind (i));
(d) for groups of thick-type and kind-(i) rows, zeta^G_kappa(y) = kappa_y Xi_G (1 + o(1)) with Xi_G := sum_{thick l in G} rho_l u_l(xhat_1): (b) holds iff G
is aligned-dominated (Xi_G >= u^3 Design^{-C} robustly), (c) needs Xi_G <= -u^3 Design^{-C}.  Kind-(iv) rows contribute (eps_l sigma_l rt_l)(coef_l
sigma_l) with coef_l sigma_l >= -small (K2.16(2c)): a fixed sign set by the target data.
Proof.  As stated; (b), (c) are Lemma TF' with rt' = rt^G(s) (plus the exchange of OUT(b) in (c)); (d) Lemma AL.  QED

PROPOSITION MA (forced mixed alignment).  PROVED (mod chain).  If block m (any kind) has a private two-sided peak resource and contains a
thick-type row with robust or near-threshold status, then for every near-certificate
   sum_{thick rows l of m} rho_l u_l(xhat_1) = -(kappa_m/kappa_y) sum_{kind-(iv) rows l of m} (rt_l eps_l sigma_l)(coef_l sigma_l) + O(Design^3 (eps + eta')).
Hence either the thick rows of m have MIXED alignment, or a kind-(iv) row with a robust coefficient compensates (orientation rt eps sigma of
the sign of sum rho u).
Proof.  zeta_m (1 - Xt_m) = sum_{tuned l in m} rt_l eps_l coef_l (K2.16), |zeta_m| <= (4/3) eps Design (R-PK), Lemma AL for thick rows, |coef_l| <=
eps Design^2 for kind (i), kind (ii) excluded at near-certificate stages.  QED
So R-PB's necessary condition |Phi_0^{(m)}(zhat_1)| ~ 0 (the stable-exact relation) is a CANCELLATION between aligned and anti-aligned carriers.
Numerics (H1_work/align_toy.py; J1-ref's consistent toy at exact resonance): rho_0 u_0 = -rho_1 u_1 (one aligned, one anti-aligned) in 8/8
cases; sign(y_k rt_k) = -sign(rho_k u_k) in 16/16; after the obstruction (targets displaced along y, phi_y = 1e-3, min move 2e-2..1e-1 with
peak resource, 29..175 without), moving the aligned row inward or the anti-aligned row outward gives phi_y = -3e-3 and min move 6.9e-4..7.1e-4
(16/16); the opposite directions keep or worsen the obstruction (up to 8.7e2).

## 6. The unit calculus in unshifted blocks
A UNIT of a (U)-block m is a pinned group G contained in m ("internal"), or a single movable row of m.  zeta^E(y) := sum_{l in E} y_l rt_l;
for thick/kind-(i) units zeta^E(y) = kappa_y Xi_E/kappa_m (1 + o(1)), Xi_E := sum_{thick l in E} rho_l u_l(xhat_1).
LEMMA DS (down-scaling of unions of units).  PROVED (mod chain).  For units E_1, ..., E_q of m and s in [1 - Design^{-C}, 1], the targets
rt'_l := s rt_l on E_1 ∪ ... ∪ E_q, rt'_l := rt_l otherwise, are admissible, and <kappa y, rt' - rt> = -(1 - s) kappa_m sum_i zeta^{E_i}(y).
Proof.  Z_kappa: Theorem GS(a) for groups, nothing for movable rows; robust minors move by << u.  Statuses: R^2 does not increase; scaled rows
lower |r| and K, unscaled rows lower K (Lemma K); robust peaks move by << u; no (X4^0) rows and no Puiseux constraint in (U)-blocks.  Data
projected at the realized ratios ((X3)_m violated by the original data by << K t).  QED
THEOREM UC.  PROVED (mod chain).  Step A is realized if some (U)-block m has
 (UC1) a unit E with zeta^E(y) <= -z_E for all near-certificates (z_E := c_* u^3/(C nu_1 Design^C); thick/kind-(i) units: Xi_E >= u^3 kappa_m
       Design^{-C}, ALIGNED-dominated): down-scale E;
 (UC2) a private peak resource and a unit E with zeta^E(y) >= z_E for all y (ANTI-ALIGNED-dominated): down-scale all other units of m (the
       complement of E; every row of m lies in a unit when all groups meeting m are internal), pairing -(1 - s) kappa_m (zeta_m - zeta^E) >=
       (1 - s) kappa_m (z_E - 2 eps Design) by R-PK;
 (UC3) no peak resource and a union of units E with zeta^E(y) - zeta_m(y) >= z_E for all y: down-scale the complement of E.
Proof.  Lemma DS and Lemma TF' with 1 - s := 4(||b|| + x)/(kappa_m z_E).  QED
CONSEQUENCES (PROVED).  (a) In a (U)-block WITH a private peak resource, at a residual stage: no movable thick-type row with robust or near-
threshold status (|y_l rt_l| robust by Lemma AL: (UC1) if aligned, (UC2) if anti-aligned) -- this covers J1's (R-np) and (R-D2) for such blocks
(a D2-pushed anti-aligned row keeps its target while the rest of the block is scaled down; its own status only decreases) and (J-c)/(J-d)
without bands; and every internal pinned group is BALANCED: zeta^G is not robustly of one sign over the near-certificates (for thick/kind-(i)
groups |Xi_G| <= u^3 kappa_m Design^{-C}: cancellation between aligned and anti-aligned pinned carriers inside the group).  With Proposition MA:
the block has mixed alignment or kind-(iv) compensation.
(b) In a (U)-block WITHOUT a peak resource: sigma_m = -1 is Theorem RL; for sigma_m = +1 a residual stage has -z <~ zeta^E <~ zeta_m + z for all
unions of units, the block is protected (else Theorem RL), and Lemma KC fails.
(c) Groups linking several (U)-blocks: Lemma DS and (UC1) hold with zeta^G_kappa; (UC2) needs the complement in the union of the blocks met
(each with a peak resource).  Groups linking a (U)-block to a shifted block are not scalable and fall under (H-6).
Numerics (H1_work/complement_toy.py): (UC2) for the anti-aligned row: phi_y -> -3e-3, min move 7.0e-4..9.2e-3 (8/8); the same operation for the
aligned row: phi_y = +5e-3, move unchanged or worse (8/8).

LEMMA TG (tangent directions of linear pinned groups).  PROVED (mod chain).  Let m be a (U)-block with a private two-sided peak resource
and G an internal pinned group of m consisting of thick-type and kind-(i) rows, all of whose tiny polynomials are MINORS.  Then near rt^G the
zero set of G's tiny polynomials is the linear space V_G := {r^G : sum_{l in G} r_l Q^{(i)}_l = 0 for every tiny minor i} (Q^{(i)} constant).
Put w^G_l := eps_l rho_l (thick rows), 0 (kind-(i) rows).  If the orthogonal projection of w^G onto V_G has norm >= u^3 Design^{-C} ||w^G||, Step A
is realized.
Proof.  In a (U)-block r^{(m)} occurs only in the row (X3)_m, so a tiny minor containing r^G is linear in r^{(m)}: expanding along (X3)_m it is
sum_l r_l Q_l with Q_l a minor not containing (X3)_m; Q_l contains no ratio of another block (G is internal) and no free ratio (by definition).
Let Delta := -P_{V_G} w^G/||P_{V_G} w^G|| (supported on G).  Targets rt'' := s (rt + h Delta) on m (all rows of m scaled by s; Delta only on G), with
h := 8(||b|| + x)/(kappa_m |kappa_y|_min ||P_{V_G} w^G||) and 1 - s := 2 h max_{l in G} |Delta_l|/|rt_l| + C h^2 (so that every status of m is <= its
value at rt: Lemma K, s(1 + h|Delta_l|/|rt_l|) <= 1 and R^2 does not increase to first order).  Z_kappa: rt^G + h Delta in V_G (linear), scaling by s
preserves every tiny polynomial (Theorem GS(a)).  Pairing: <kappa y, rt'' - rt> = s h <kappa y, Delta> - (1 - s) kappa_m zeta_m(y; rt) = s h kappa_m kappa_y
<w^G, Delta>(1 + o(1)) + O((1 - s) eps Design) >= 4(||b|| + x) (Lemma AL, kind (i) o(1), R-PK).  Size: h, 1 - s <= Design^C x/u^{C}.  Lemma TF'.  QED
So in (H-3) a residual internal group of this kind must satisfy the NORMAL RESONANCE ||P_{V_G} w^G|| < u^3 Design^{-C} ||w^G||: the signed thick
ratios (eps_l rho_l) of the group lie (up to tolerance) in the span of the cofactor vectors Q^{(i)} of its tiny minors (balance, <w^G, rt^G> ~ 0, is
the special case of the direction rt^G in V_G).

## 7. Peak conversion of anti-aligned near-threshold zero-data rows.  SKETCH.
An inactive near-threshold anti-aligned thick-type row d of a (U)-block without exchange partner needs OUTWARD, but its status must stay
below threshold.  Proposal: freeze d as a PEAK ((FC) with P_f := P_rob ∪ {d}) and add the one-sided band row rho_d in [1 + beta_*, 1 + 3 beta_*].
Peaks of (U)-blocks carry no class data (Lemma NP's proof), so Gamma^#(kappa, a) is unchanged; (FC)-consistency at the realized point is
enforced by the band row; with a peak resource J1.6's Corollary and J1.8(b) give relief.  Missing: downstream legitimacy of a zero-data weak
peak of margin ~beta_* (the peak-error term e_d <= t/(lambda_d mu_d) in U1 Prop. 2.2(a), plausible because inactive components are below A_i K t;
and the screening bounds CM'(a) Scr_m for coarse peaks of non-robust margin).  The same idea for ACTIVE near-threshold rows of shifted blocks
would change the pattern (an active weak peak with peak data) and is not covered.

## 8. The residual after H1 (precise; a necessary condition for a main stage NOT to be realized).  PROVED (mod chain) as a consequence of
## Corollary 2.4, Lemma TF', Lemma NP, Theorem RL, Lemma KC, Lemma AL, Theorems IN, OUT, GS, UC, Proposition MA.
"Thick row" = thick-type row with robust or near-threshold status (nearly neutral thick rows are always relieved, Theorem IN).
(f, g, rho) is not covered at a main stage only if Step A carries near-certificates and ALL of the following hold:
 (H-1) (R-T) does not occur (it is empty);
 (H-2) no movable aligned thick row exists, in any block;
 (H-3) in every (U)-block with a private peak resource: every thick row is pinned, every internal pinned group is balanced, internal groups
       of thick/kind-(i) rows with only minors as tiny polynomials satisfy the normal resonance of Lemma TG (w^G nearly orthogonal to V_G),
       and the block has mixed alignment or kind-(iv) compensation;
 (H-4) every (U)-block without a peak resource has aligned peaks (sigma_m = +1), is protected, violates Lemma KC, and all its unions of units
       satisfy -z <~ zeta^E <~ zeta_m + z;
 (H-5) in shifted blocks ((T), (KN)) every movable thick row is anti-aligned (H-2); robust ones lie in protected blocks and have no exchange
       partner: in every such block all robust anti-aligned movable thick rows share rho_l/u_l(xhat_1) (the ANTI-ALIGNED PROPORTIONAL RESONANCE
       a_p = -alpha_m u_l(xhat_1) v_l(p), alpha_m > 0) and the block has no kind-(i) movable row with robust status (it would be an exchange
       partner; in (KN)-blocks the KN lever d_0 is therefore itself an anti-aligned thick row with the common ratio); near-threshold anti-
       aligned movable rows (KN-pushed inactive rows, free near-threshold actives) are unrelieved;
 (H-6) pinned thick rows of shifted blocks (and groups linking a (U)-block to a shifted block), and thick-type peaks of shifted blocks without
       peak resource: no admissible point of Z_kappa pairs by >= 4(||b|| + x) with every near-certificate (the polar/normal resonance).  In a
       (T)-block, at a smooth point of Z with near-active set D, this reads kappa y|_{T Z} = sum_{d in D} c_d d(psi_d/Phi_d)|_{T Z}, c_d >= 0 (Farkas),
       and every admissible endpoint r''' has first-order pairing sum_d c_d (psi_d(r''')/Phi_d - psi_d(r'')/Phi_d): the certificate pairs positively
       only with displacements raising near-threshold statuses, i.e. it wants some near-threshold ACTIVE carriers to move OUTWARD;
 (H-7) J1's conditions: frozen far windows and no private two-sided design-depth resource on every thick-type carrier, tiny spreads (J1.15'
       (J-a), (J-b)).
OR J1-ref's (R1) (no thick-type carrier; parallel task H2).
Relation to J1-ref's list: (R-T) empty; (R-np), (R-D2) in (U)-blocks with peak resource: gone; (R-np), (R-pk) in (U)-blocks without peak
resource: only (H-4) (aligned peaks, protected); (R-KN), (R-Ts), (R-D2) in shifted blocks: (H-5); (R-pin): (H-3) balanced groups or (H-6);
(R-pk) in shifted blocks: (H-6).
Persistence (PROVED, elementary): if the same carriers, groups and units occur at all large main stages, the near-relations become EXACT
identities at f (the tolerances u^3 Design^{-C}, eps Design, eta' tend to 0 and xhat_1 -> zhat_f): balanced groups give sum_{l in G} rho_l u_l(zhat_f) = 0,
proportional resonances give rho_l = -alpha_m u_l(zhat_f) exactly, and tiny polynomials involving only fixed carriers vanish exactly at the
ratio vector of f.  These are algebraic coincidences among f's data; they are not excluded (f is arbitrary), and no non-recoverable mate is
indicated.

## 9. Numerics (sanity only; r13/H1_work/)
 puiseux_toy.py / puiseux_toyA_fine.py (+ .out): J1.11 on singular Z (cone: linear margin, ratios 2.35-4.26; critical cusp coincidence:
   exponent 1.495; generic: 1.05-1.07).
 align_toy.py (.out): Lemma AL (16/16), forced mixed alignment at resonance (8/8), Theorems IN/OUT (16/16 relieved in the predicted
   direction, 16/16 not in the opposite one).
 rescale_toy.py (.out): signed peak derivative (Lemma NP bookkeeping); block rescaling pairing algebra (the toy's peak is not thick-type,
   so Lemma NP's robustness is not exercised there).
 complement_toy.py (.out): Theorem UC (UC2) (8/8 relieved for the anti-aligned row, 8/8 not for the aligned row).

## 10. Main obstacle; what remains open; next steps
MAIN OBSTACLE.  Rows whose needed displacement points OUTWARD while their statuses forbid it: near-threshold anti-aligned rows (inactive D2/KN-
pushed rows or near-threshold actives) in blocks without a neutral rescaling (shifted blocks; unshifted blocks with aligned peaks), and pinned
rows whose exact set Z_kappa only offers status-raising directions (the normal resonance (H-6)).  In unshifted blocks with a peak resource
everything except balanced pinned groups is relieved.
OPEN: (1) whether (H-3)-(H-6) can hold at all large main stages for some f (each is a codimension >= 1 coincidence or a persistent alignment
pattern); (2) the peak conversion of Section 7 (would remove the inactive part of (H-5)/(M2) and of (H-4)'s near-threshold obstruction);
(3) balanced pinned groups in (U)-blocks with a peak resource whose tiny polynomials include cofactor polynomials (nonlinear in r^G), or
which contain kind-(iv) rows: Lemma TG's tangent directions need a quantitative curvature bound of Z_G at the scale Design^C x/u, resp. control of
the kind-(iv) certificate weights; (4) (R1) (task H2); (5) the once-refereed links of the chain, J1.13's inspection, J2.
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.

## 11. Points checked against attacks (for the referee)
 - Sign conventions: kappa_m depends on |zeta(k)| only, so d kappa/d zeta(c) = vs_c (1 - X_m) at peaks (checked numerically, +-1.0000); all
   alignment statements are invariant under the arbitrary row signs eps_l (eps_l^2 = 1 cancels in y_l rt_l).
 - Quantifiers: every lever is applied through Lemma TF', which needs the pairing sign for ALL near-certificates of size <= eps_* at the
   ORIGINAL targets; the signs used (Lemma AL, Lemma NP, R-PK) are uniform because kappa_y in [-C, -c_*/nu_1] for every near-certificate.
 - Target dependence of the generators (J1-ref P-1): covered by C_G |rt' - rt| <= eps_*/2 in Lemma TF'.
 - Exactness on Z_kappa: only uniform scalings of internal pinned groups of (U)-blocks (homogeneity, X1-ref D1), free/inactive rows (not
   in tiny polynomials), and linear tangent directions (Lemma TG) are used; no move of a pinned ratio of a shifted block is claimed.
 - Statuses: every lever either lowers all statuses of the block (inward moves, down-scalings, R^2 decrease via Lemma K), keeps R^2 to
   second order (exchange), or uses robust room u (outward moves of robust rows); near-threshold rows never move outward.
 - Sizes and costs: all displacements are <= Design^C (||b|| + x)/u in kappa-units, the order of J1.9's bands (P-TU windows enlarged as for
   J1's bands); W(rt') and the realization cost are o(u^2 T^2) as in J1.15'.
 - J1.11: the flow uses the frontier condition (dimension drops at every exit) and Whitney (a) only; the genericity step applies GEN to the
   k-definable set B^lin, not to the (possibly non-k-definable) stratification.
 - Not claimed: the peak conversion (SKETCH); any statement about (R1); persistence-based exclusion of (H-3)-(H-6).
