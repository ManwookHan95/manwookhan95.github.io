# J1 part 4: first-order Puiseux margin; active thick-type carriers (mismatch tolerance, gauge); target freedom as a characterization

## 4.1 Proposition J1.11 (first-order Puiseux margin for the generic-weight design).  SKETCH (strong).
Claim: for every pattern kappa of level L with (Phi_d)_{d in N_T} as chosen by T_fin (algebraically independent over k_0(other weights)), the
modulus of Lemma QC satisfies mu_kappa(h) >= c_kappa h for 0 < h <= h_kappa (Puiseux exponent beta_kappa = 1), c_kappa, h_kappa design numbers.
Argument.  (1) The proof of Lemma GEN applies to ANY semialgebraic subset of R^{N_T} of dimension < |N_T| definable over k = k_0(other
weights); the union over (D, S) of the cylinders {Phi : (Phi_d)_{d in D} in CV_{D,S}} (critical values of Psi_{D,S} = (psi_d)_{d in D}|_S on the
strata S of a Whitney stratification of Z compatible with the sign conditions, definable over k [BCR 9.7]) is such a set (Sard, BCR 9.6.2).
Hence EVERY point r_0 of Lambda := Z ∩ {F_Phi = 1} is a regular point of Psi_{D(r_0), S(r_0)}: there is v in T_{r_0} S(r_0) with
d psi_d(r_0) v = -Phi_d for all active d.  (2) Suppose mu(h)/h does not stay bounded below.  mu is semialgebraic; by the curve selection
lemma there is a Nash curve h -> r(h) in Y_1 with G_h(r(h)) >= 1 - o(h), r(h) -> r_* in Lambda.  For small h, r(h) lies in one stratum S'
with S_* := S(r_*) ⊂ closure(S'); by Whitney (a) the limit tau of T_{r(h)} S' contains T_{r_*} S_*, so there are v(h) in T_{r(h)} S' with
v(h) -> v (the regular direction at r_*).  If |r(h) - r_*| = o(h), go first to r_* (F changes by o(h)) and then along a curve in S_* with
velocity v for time h/2: F decreases by >= c h, contradiction.  Otherwise |r(h) - r_*| >= c' h along the curve, and one needs a curve
in S' of length ~h starting at r(h) with velocity ~v(h) and second-order deviation o(h): this requires a lower bound on the "local
reach" of S' at r(h) of order >= h, which holds for semialgebraic curves r(h) approaching r_* at a rate >= h by Whitney (b)-type
regularity (the gap in this sketch).  (3) Inactive d (psi_d(r_*) < Phi_d) stay inactive for moves of size O(h).
Status: SKETCH (step (2), second case, needs a precise semialgebraic lemma; I did not complete it).  Why it matters: with mu >= c_kappa eta'/3
the KN-1 exactness (inactive nearly-neutral values of (T)-blocks held EXACTLY at 0, Q1-refb P-HOLD) becomes a band of half-width
<< sqrt(mu) ~ eta'^{1/2}; in particular bands of half-width beta_* ~ Design^C eta'/u are legitimate for KN-1 rows (B2 holds:
Design^{2C} eta'^2/u^2 << c_kappa eta'), and Theorem J1.9 then removes every configuration with a thick-type KN-1 carrier (item (R-T) of 4.5).

## 4.2 Active thick-type carriers: where their exact ratio is used.  PROVED (inspection of the cited chain).
For an ACTIVE coarse carrier l the target ratio r''_l is used (i) in Z_kappa (vanishing of tiny minors and cofactor polynomials, X1 2.2(iv)),
(ii) in (X3)_m: Delta'_m = sum_{active l in m} r_l gamma_l, i.e. the TRUE shift of block m at the companion is Delta''_m = sum r^#_l gamma_l
(U1 Lemma 4.6: with exact ratios Delta'' = Delta'), (iii) in statuses (Lemma K; (X4^0) coefficients m^2 |r_l| K(sigma_rob, R_a^2)), (iv) nowhere
else (Sys-DC uses the companion's values as targets; UE^inf/E^{eng,RT,inf} use data, not ratios).  If the realized ratio is r^#_l = r''_l +
delta (delta small) while the class data (Delta', gamma) are exact points of Gamma^#(kappa, a) at r'', the TRUE data at the companion are
(Delta'' , gamma) with Delta''_m = Delta'_m + delta gamma_l(t) (scale t); every row of Gamma^# not involving Delta'_m or r_l is unchanged.

## 4.3 Proposition J1.12 (mismatch tolerance).  PROVED (as a conditional statement).
Let l be an active thick-type carrier of a block m that is SHIFTED in the class (|Delta'_m(t)| >= A_{i+1} K t on the class scales).  Suppose
 (MT1) every E_c coordinate j with tau_m(j) != 0 (peak traces of block m) is a contact of the peak's sign or lies in F^# (no FREE coordinate
       in supp tau_m ∩ E_c), and every target coordinate in supp tau_m ∩ E_c is a contact at which the class data have slack
       s_j(t) := z_j L(Delta', gamma)(j) >= |delta| |gamma_l(t)| |tau_m(j)|;
 (MT2) l is not near-threshold, the block is not a (T)-block, or the (X4^0) rows of block m have slack >= C |delta| |gamma_l(t)| on the class
       data;
 (MT3) the status of l and the R^2 of block m tolerate |delta| (as (B1), (B2) of J1.10).
Then the row of l in Sys-A may be relaxed to the band |r_l - r''_l| <= delta_0 with delta_0 := min over the class scales of the slacks in
(MT1)-(MT2) divided by |gamma_l(t)| (and the (MT3) bound): the companion's true data (Delta'', gamma) lie in Gamma^#(kappa, a) evaluated at the
realized ratios, with the same Hoffman/minor bounds as at r'' (the cone at r'' was used for the projection; the realized data are an exact
point of the cone at r^# because only Delta-sensitive rows change and they keep their sign by (MT1), (MT2)).
Proof.  By 4.2 the true data differ from the projected data only in Delta'_m by delta gamma_l(t).  Rows (X1) at coordinates outside supp tau_m:
unchanged.  At peak-private contacts: L = -Delta' lambda_p vs_p v_p(j) has modulus >= |Delta'| lambda_p |v_p(j)| (robust: shifted block) and
changes by |delta gamma_l lambda_p v_p(j)| << that (|delta| <= delta_0 <= eta'... << A K t / |gamma|); sign kept.  At target coordinates: (MT1).
(X2) sign rows of Delta': kept (|delta gamma| << |Delta'|).  (X4^0): (MT2).  (X5): the block is shifted, no zero row on Delta'.  QED
Combined with J1.9: if some thick-type carrier is ACTIVE in a shifted block satisfying (MT1)-(MT3) with delta_0 >= beta_*/kappa_m, Step A is
realized.  [(MT1) fails in general when a peak of block m has a target coordinate that is FREE with robust room; this is a pattern
property (design + f at level L), and is the main limitation.]

## 4.4 The gauge (re-representation of switching through thick-type carriers).  PROVED (identity, admissibility, curvature dichotomy);
## its use as a bypass is a SKETCH.
(a) IDENTITY.  For a block vector rhot (supported on coarse non-peaks) put B(rhot) := sum_m R_m^*(rhot_m - d_m(rhot_m) w_m).  For any two-piece
data (b^+-, omega^+-) of g_t and reals s_+, s_-, the pieces (b^+- - s_+- B(rhot), omega^+- + s_+- rhot) represent the same g_t; the switching
changes to Domega + (s_- - s_+) rhot and the base switching to V - (s_- - s_+) B(rhot) (U1 Lemma 1.1(a): V = B(Domega)).
(b) THE NATURAL DIRECTION.  Let K_0 be the thick-type coarse non-peaks and rho_k := a_p/v_k(p) (J1.6(a)); rhot(k) := rho_k/lambda_k on K_0.
Then B(rhot) = Phi_0 - sum_m d_m(rhot_m) R_m^* w_m with Phi_0 := sum_{K_0} rho_k u_k, Phi_0 = a on the thick private coordinates, and
d_m(rhot_m) = (sum_{K_0 ∩ m} rho_k u_k(xi))/A_m.
(c) ADMISSIBILITY (coordinatewise; PROVED).  Adding -s Phi_0 to a piece's base part is admissible at: thick F-coordinates (it is -s a_j there;
cushion (U3^inf) with C_+ increased by |s| t, fine for |s| <= C/t); data-sign contacts/banks where Phi_0 z < 0 (the holes of anti-aligned
carriers): for s >= 0; contacts where Phi_0 z > 0: for s <= -(slack); FREE E_c coordinates with Phi_0(j) != 0: never (exact zero needed).
(d) CURVATURE DICHOTOMY (PROVED).  Let Q(P) := Gamma_w(P) be the curvature budget of a piece (C's invariant q_0 H_b + sum sigma_m H_m, a positive
semidefinite quadratic form on representations) and G := (-B(rhot), rhot).  For the two-piece gauge with s_+ - s_- = s_0 (to change the
switching coefficient along rhot by -s_0), the minimum over s_- of max(Q(P^+ + s_+ G) - Q(P^+), Q(P^- + s_- G) - Q(P^-)) is <= 0 whenever
0 <= s_0/s_0^Gamma <= 2, s_0^Gamma := Q(P^- - P^+, G)/Q(G) (Gamma-component of the switching (-V, Domega) along G); in particular, if the
switching through K_0 is EXACTLY along rhot (single thick-type carrier, or Domega|_{K_0} ∝ rhot), s_0 = s_0^Gamma and one of the two pieces
absorbs the gauge with non-increasing curvature.
Proof of (d).  t -> Q(P + tG) is a convex parabola with minimizer s^*(P) := -Q(P, G)/Q(G) and Q(P + tG) <= Q(P) for t between 0 and 2 s^*(P).
Choose s_+ in [0, 2 s^*(P^+)] and s_- in [0, 2 s^*(P^-)] (intervals oriented); their difference covers [2 s^*(P^-)... ] -- precisely, the set
{s_+ - s_-} contains every value between 0 and 2(s^*(P^+) - s^*(P^-)) = 2 Q(P^- - P^+, G)/Q(G) = 2 s_0^Gamma.  If (-V, Domega) = s_0 G + G^perp with
Q(G^perp, G) = 0 then s_0^Gamma = s_0.  QED
(e) USE (SKETCH).  If K_0 = {k_0} (one thick-type carrier), Phi_0 = rho u_{k_0} has no free E_c coordinate in its support (in particular no
free target coordinate of k_0), d_m(rhot) = 0 (the frozen value of k_0 vanishes; automatic in the stable exact residual, 4.5), then the gauge
removes the switching of k_0 at every class scale without increasing any piece's curvature; k_0 becomes INACTIVE in the gauged data, its row
becomes a hold, and J1.10/J1.9 apply if k_0 is status-safe.  Missing for a proof: the re-pigeonhole of the gauged data into classes (n(w)/D_cl^2
scales -- plausible), the exactness of the gauged data in the cone of the new pattern (needs d_m(rhot) = 0 EXACTLY; near-resonant d_m(rhot) ~ b
leaves violations ~ b >> s_1), and several thick-type carriers (one gauge scalar per Phi_0, curvature cost Q(G)(s_0 - s_0^Gamma)^2).

## 4.5 Target freedom (characterization) and the stable exact case.  PROVED (characterization); the conclusions on the residual are PROVED.
(a) CHARACTERIZATION.  Let C_ach := V_2 + cone(G_1) be the cone of first-order achievable changes of Ft (V_2 the span of the two-sided generators,
G_1 the one-sided ones; peak columns with the TARGET-dependent entries included).  With targets r'' (displacement delta := r'' - r_1 in ratio
units, b = kappa delta on active rows): Step A is A-regular iff B(kappa delta + b_inact, rho_0) ⊂ (W/2) conv(G ∪ {0}) (K2.9), i.e. iff the
displacement lies robustly in the interior of C_ach.  Target freedom therefore means: some point of Tgt := Z_kappa ∩ B(r_1, eta') ∩ {F <=
1 - 3mu/4} lies in r_1 + kappa^{-1}(int C_ach - b_inact).  [Restatement; PROVED.]
(b) NECESSITY (from J1.5).  In the residual, (r_1 + kappa^{-1} C_ach) ∩ Tgt must be empty for EVERY admissible target choice; since C_ach is
(up to eps-fuzz) the half-space-like set {Phi decreasing} of J1.4 (or a polyhedral cone whose dual contains all residual certificates), the
residual is exactly the statement that the Lojasiewicz/Puiseux target set lies on the "frozen" side of every residual certificate.
(c) FUZZ.  Near-certificates are orthogonal to two-sided generators only up to eps <= 4 Design^{-C_A} >> eta'; any target-freedom argument must
produce displacements with <kappa y, delta> >= Design^C eps eta' (not just > rho_0).  This is the quantitative reason why the per-block relation
zeta_m ~ 0 of residual certificates (private peak resources) does NOT make target freedom automatic: zeta_m is only known to be <= 2 eps Design.
(d) STABLE EXACT CASE.  If the set K_0 and the certificate structure stabilize as L -> infinity (finitely many fixed thick-type carriers with
rho_k fixed), the residual relations become EXACT identities at f: a = sum_{K_0} rho_k u_k on the thick part of F, and every per-block
frozen value Phi_0^{(m)}(zhat_f) = 0 (they are <= C eps(L) Design(L) at every stage and fixed numbers).  Then Phi_0 = sum_{K_0} rho_k u_k satisfies
p*(f + t Phi_0) <= 1 + O(t^2) through its pure block representation (sum_m R_m^* rhot_m with d_m(rhot_m) = 0): a FLAT direction at f, i.e. a
block-representable mate direction whose base trace is a.  In this case every first-order target displacement along the certificates comes only
from the preprocessing (deep raise, preparation banks), which moves Phi_0 by O(mu*_J + theta_0-effects) -- by J1.4 always to the blocked side.
[PROVED; the bank part can be undone two-sidedly at scale theta_0, the deep-raise part (<= C mu*_J) cannot -- it is far below s_1, so a
violation-tolerant variant would absorb it, but this needs exact Z-targets for the K_0 ratios, which I did not establish.]
