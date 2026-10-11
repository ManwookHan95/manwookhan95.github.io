# H1-ref part 3: Theorems IN, OUT, GS; Lemma DS, Theorem UC, Lemma TG; Proposition MA; peak conversion; the residual

## 3.1 Theorem IN (inward relief).  Verdict: CORRECT (mod chain), constant slip P-IN.
Aligned case: rt'_l = (1 - s) rt_l, pairing -s kappa_m y_l rt_l = s|kappa_y rho_l u_l(xhat_1)|(1 + o(1)) >= 4(||b|| + x); admissibility: l
inactive or free (no tiny polynomial depends on it; in a (T)-block a free ratio cannot enter a tiny minor through R_a^2 of an (X4^0) row,
since then every active ratio of the block would be pinned); statuses: |r_l| and R^2 (R_a^2 in (T)-blocks) decrease, so every status of
the block decreases by Lemma K; (X4^0) robust slacks and robust minors move by << u; data projected at the realized ratios (J1.13; in a
SHIFTED block the (X3)_m coefficients change with the free ratio and the projection absorbs it: violation <= Design^C u^{-C} x/t << K t).
Inward moves cannot create a mismatch problem of J1.12 type because the ratio is realized EXACTLY at the new target.  Correct.
In (T)-blocks inactive rows are nearly neutral by definition of (T), so movable thick rows there with robust or near-threshold status are
free ACTIVE rows: covered.  In (KN)-blocks the protected statuses are U1-ref Prop. KN(b)'s; an inward move lowers R^2 and every status;
H1's claim "KN-lever margins only improve" is right for inward moves.
Nearly neutral case: P-IN (constant slip).  |y_l| >= c_* u/(8 nu_1) and a displacement beta_*/kappa_m give pairing |y_l| beta_* >= 2(||b|| +
2 rho_0), not 4(||b|| + x) as needed by TF'.  Fix: displace by beta' := 2 beta_* + 32 nu_1 x/(c_* u) (same order Design^C x/u); the R^2 and
status estimates are unchanged up to a factor 4.  In (T)-blocks the R^2 change is (J-e)'s quantity, so Corollary 2.4 applies; in (KN)-blocks
the change is second order (<= Design^C((x/u)^2 + bx/u) << c_f D eta' M).  After the move the row's status is ~Design^C x/u >> b: it leaves
the class "<= b" but stays small (<< u); J1.10(a) (refereed) accepts this for (U)-blocks, Cor 2.4 for (T)-blocks; for (KN)-blocks H1 inherits
J1's "(KN): SKETCH" for the bookkeeping of the KN-lever margin under target changes (P-KN below).

## 3.2 Theorem OUT (outward relief).  Verdict: CORRECT (mod chain).
(a) unprotected block: k robust (room u), other statuses robust or nearly neutral, R^2 increase <= Design^C x/u^C.  (b) EXCHANGE: R^2 change
m^2 t^2 (rt_k^{-2} + rt_d^{-2}) (exactly second order: the first-order terms 2m^2 t cancel), pairing kappa_m t (Q_k - Q_d); Q_l = kappa_y kappa_m
rho_l/u_l (1 + o(1)) with the COMMON negative factor kappa_y, so for two anti-aligned rows with robustly different rho/u the exchange works in
one orientation; displacement sizes u^{-2} (P-TF).  In a (T)-block both rows are free actives (inactive rows are nearly neutral), so R_a^2 = R^2
changes at second order and the Puiseux statuses psi_d are safe.  (c) J1.15' (J-c)/(J-d) with F-2.  (d) Theorem RL.  Correct.
P-KN.  In (KN)-blocks every H1 lever (IN, OUT, exchange, KC) needs the KN-lever margin of U1-ref Prop. KN(b) to survive target changes of
size Design^C u^{-C} x.  For inward moves and exchanges (statuses do not increase at first order) this is immediate from Lemma K; for the
nearly-neutral band it is second order.  But J1 left the (KN)-block bookkeeping (lever push one-shot vs. in-system, J2-ref Q-KN) as SKETCH,
and H1 does not re-derive it: the (KN)-block clauses of IN/OUT are PROVED modulo that SKETCH.

## 3.3 Theorem GS, Lemma DS, Theorem UC, Lemma TG.  Verdicts: CORRECT; the "internal" hypothesis is UNNECESSARY (P-PC, strengthening).
GS(a): X1-ref D1 -- in a (U)-block r^{(m)} occurs only in the row (X3)_m (no constant entry since (X5) removes Delta'_m), so every minor is
homogeneous of degree 0 or 1 in r^{(m)} and every cofactor polynomial (one entry per column, each column homogeneous of degree e_J) is
homogeneous in r^{(m)}; this holds as an identity in ALL ratio variables, the ratios of other blocks being parameters.
LEMMA PC (piece scaling; referee; PROVED).  Let m be a (U)-block and A a set of active ratios of m such that for every tiny polynomial P
either A ∩ var(P) = {} or var(P) ∩ r^{(m)} ⊂ A (var(P) := the ratio variables P depends on).  Then multiplying the ratios in A by any s > 0
preserves Z_kappa.  In particular A may be any union of PIECES G ∩ m (G a pinned group, internal or not: var(P) ⊂ G for every tiny P meeting
G) and free ratios.
Proof.  If A ∩ var(P) = {}, P is unchanged.  Otherwise P does not depend on r^{(m)} \ A, so P(scale A by s) = P(scale r^{(m)} by s) = s^{e_m(P)}
P = 0.  QED
Consequences.  (1) GS(a)-(d), Lemma DS and Theorem UC hold with "unit" := a piece G ∩ m of ANY pinned group, or a movable row; H1's
restriction to internal groups and Remark 4.3's last sentence ("groups linking a (U)-block to a shifted block are not scalable") are too
pessimistic: their (U)-block pieces are scalable.  (2) (H-3) reads "every PIECE in a (U)-block with a peak resource is balanced", and (H-6)
loses the groups linking (U)-blocks to shifted blocks (only their shifted-block parts remain).  (3) Lemma TG extends to pieces: with the
ratios of the other blocks frozen, every tiny MINOR meeting G ∩ m is linear, sum_{l in G∩m} r_l Q_l (Q_l depending on frozen ratios only).
(4) Even in SHIFTED blocks the tiny minors that contain no (X4^0) row of the block are AFFINE in r^{(m)} ((X3)_m is the only row with r^{(m)}:
entries 1 at Delta'_m and -r_l at gamma_l; in (KN)-blocks U1-ref's (X4) contains no ratio): for groups whose tiny polynomials are such
minors, the zero set (other ratios frozen) is an affine subspace through rt^G and displacements along it are exact; only the status
compensation of TG (whole-block rescaling) is unavailable there -- see Lemma SLP (3.5).
UC (UC2) proof checked: for a single movable row E = {k}, "all rows of m except k" is Z-safe even without Lemma PC (k enters no tiny
polynomial); pairing -(1 - s) kappa_m (zeta_m - y_k rt_k) >= (1 - s) kappa_m (z_E - (4/3) eps Design) by R-PK.  DS: R^2 decreases, scaled rows lower
|r| and K, unscaled rows lower K.  TG: Delta in V_G, pairing kappa_m kappa_y <w^G, Delta>(1 + o(1)) = kappa_m |kappa_y| ||P_V w^G||, the
compensating whole-block scaling costs (1 - s) kappa_m |zeta_m| <= (1 - s) kappa_m (4/3) eps Design (R-PK).  Correct.

## 3.4 Proposition MA.  Verdict: CORRECT, bookkeeping precision; GENERALIZED by MA' (part 2, 2.6).
zeta_m (1 - Xt_m) = sum_{rows l of m} rt_l eps_l coef_l re-derived.  Precision P-MA: a thick-type carrier can also be of kind (iv) (a thick private
coordinate deeper than N_l with all near coordinates S_th of the data sign); by K2.17(d) its S_th data sign is then -sgn(a_p), coef_l =
kappa_y rho_l robustly, and it must be counted among the THICK rows (Lemma AL applies), the kind-(iv) sum running over non-thick kind-(iv)
rows only.  The lower bound "(u^2/2) min|rc_l| kappa_m" for same-alignment blocks is weaker than the true (u/2) kappa_m min|rc_l|: fine.
MA' (referee) shows the same cancellation in (U)-blocks WITHOUT a peak resource with the (thick-type) peaks included.

## 3.5 NEW (referee): Lemma SLP -- the status-constrained target LP and its exact dual.  PROVED (mod chain).
Setting: one block m at a stage carrying near-certificates.  OBJECTS E in M: movable rows of m with robust or near-threshold status; if m is
a (U)-block, also pieces G ∩ m (Lemma PC).  Assume every object consists of thick-type and kind-(i) rows (no non-thick kind-(iv) row in an
object).  Xi_E := sum_{thick l in E} rho_l u_l(xhat_1); R_E^2 := m^2 sum_{l in E} rt_l^2; N := protected rows of m (near-threshold actives incl.
(FC)-frozen weak peaks, D2/KN-pushed rows; in (T)-blocks the active near-threshold carriers N(m) with the Puiseux statuses psi_d);
kappa'_m := d log K/d R^2 (> 0, <= C D^C; the same for all carriers of m by Lemma K).  For d in N let a_d in R^M, a_d(E) := 1[d in E] + 2
kappa'_m R_E^2.  Let V_LP := max{ -Xi . delta : a_d . delta <= 0 (d in N), ||delta||_inf <= 1 }.
(a) If V_LP >= c_LP := u^3/Design^{C_L} then Step A is realized (targets rt'_l = (1 + h delta_{E(l)}) rt_l, h := 8 nu_1 (||b|| + x)/(c_* c_LP)).
(b) LP duality: V_LP = min{ ||Xi + A^T lambda||_1 : lambda in R_+^N }, A^T lambda = (lambda_E + 2 kappa'_m R_E^2 Lambda)_E with lambda_E := sum_{d in N ∩ E}
lambda_d, Lambda := sum_{d in N} lambda_d.  So at a residual stage there is lambda >= 0 with
     Xi_E = -(lambda_E + 2 kappa'_m Lambda R_E^2) + err_E,   sum_E |err_E| < c_LP          (*)
(the R^2-PROPORTIONAL ANTI-ALIGNED RESONANCE): every object without protected rows has Xi_E ~ -2 kappa'_m Lambda R_E^2 (anti-aligned,
proportional to its R^2-weight; for single rows this is H1's "common rho_l/u_l(xhat_1)"), objects containing protected rows have Xi_E <~
-2 kappa'_m Lambda R_E^2, and if N = {} then every Xi_E ~ 0.
Proof.  (a) Z_kappa: movable rows enter no tiny polynomial; pieces by Lemma PC.  Pairing: <kappa y, rt' - rt> = h kappa_m sum_E delta_E zeta^E(y)
and zeta^E(y) = kappa_y Xi_E/kappa_m + O(Design^3(eps + eta') + D^2 b^2) (Lemma AL; kind (i) o(1)), so the pairing is h kappa_y (Xi . delta) +
O(h |M| Design^4 (eps + eta' + b^2)); kappa_y <= -c_*/nu_1 for every near-certificate and Xi . delta <= -c_LP give >= h (c_*/nu_1) c_LP - small = 8(||b|| + x)
- small >= 4(||b|| + x).  Statuses: for a protected row d, log rho_d(rt') - log
rho_d(rt) = h a_d . delta + O(h^2 Design^C) <= C h^2 Design^C, while every protected status has slack >= eta'/(12 Design) at the targets ((U):
<= 1 - eta' vs required 1 - eta'/2; (T): F(r'') <= 1 - 3mu/4 vs 1 - mu/2 with mu >= eta'/(3 Design), Cor 2.4; D2/KN pushes likewise), and
h^2 Design^C <= Design^C u^{-C} x^2 << eta'/Design.  Robust statuses move by O(h) << u.  Lemma TF' (with P-TF).  (b) Standard LP duality for
max{c.delta : A delta <= 0, -1 <= delta <= 1} (dual: min 1.(mu+ + mu-) s.t. A^T lambda + mu+ - mu- = c, lambda, mu+- >= 0).  QED
Readings.  (i) Theorem IN = the case of one aligned object; OUT(a) = N = {}; OUT(b) = two objects without protected rows and different
Xi/R^2; Lemma KC = one unit up-scaled against one inward object; Theorem RL and (UC1)-(UC3) are feasible points of (a).
(ii) (U)-block WITH a peak resource: all rows lie in objects (pieces, movable rows; nearly neutral rows are objects with Xi = O(b) or are
relieved), and MA gives sum_E Xi_E ~ 0 (no kind (iv)); summing (*) gives Lambda (1 + 2 kappa'_m R^2) ~ 0, hence Lambda ~ 0, lambda ~ 0 and
EVERY object is balanced, Xi_E ~ 0 -- H1's (H-3), now for pieces.
(iii) (U)-block WITHOUT a peak resource: MA' gives sum_E Xi_E = -sum_{peaks} rho_c u_c(xhat_1) + small; summing (*): Lambda = sum_P rho_c u_c/
(1 + 2 kappa'_m R^2).  sigma_m = -1 makes Lambda < 0: impossible (= Theorem RL); sigma_m = +1, N = {}: Lambda = 0 contradicts sum_P rho_c u_c >=
robust (= RL+).  Residual (H-4) in exact form: N != {}, Lambda = sum_P rho_c u_c/(1 + 2 kappa'_m R^2) > 0, every object without protected rows has
Xi_E ~ -2 kappa'_m Lambda R_E^2 and objects with protected rows Xi_E <~ -2 kappa'_m Lambda R_E^2.
(iv) Shifted blocks, objects = movable rows: (H-5) in exact form (common rho/u for robust anti-aligned movable rows, near-threshold movable
rows with |rho/u| at least the common value, no kind-(i) or aligned movable row).
Extension (PROVED by the same argument): objects may also be unit directions Delta of the affine zero sets of minors-only pinned groups
(3.3 (4)) -- in shifted blocks too -- with a_d(Delta) := 1[d in G] Delta_d/rt_d + 2 kappa'_m m^2 sum_{l in G} rt_l Delta_l and Xi(Delta) :=
kappa_m sum_{thick l in G} eps_l rho_l Delta_l.  What stays outside the LP: groups whose tiny polynomials include cofactor polynomials or (X4^0)
rows (nonlinear zero sets), non-thick kind-(iv) rows (certificate-dependent signs), thick-type peaks of shifted blocks.

## 3.6 Peak conversion (H1 7).  Verdict: SKETCH (label honest).  Additional missing points:
 (i) the frozen pattern would contain a NON-robust frozen peak (margin ~beta_*), outside (FC) as refereed (J2-ref: only robust peaks frozen
     as peaks); Lemma J2.1(e)'s hypotheses (margins of frozen peaks) must be re-checked for a margin beta_*;
 (ii) the downstream screening of coarse peaks (cert0 CM'(a), Scr_m) and V1 Lemma D's robust peak are not affected for the robust peaks,
     but the new weak peak needs the peak-error bound e_d <= t/(lambda_d mu_d) with mu_d ~ beta_*: H1 lists it;
 (iii) in a (U)-block the cone Gamma^# is indeed unchanged (Delta'_m = 0 kills the peak trace tau_m), and Lemma K is continuous across the
     crossing (the carrier's contribution k^2 m^2 r_d^2 = Phi_d^2 to a^2 at rho_d = 1 moves from R^2 to sigma).  Plausible; unproved.

## 3.7 The residual (H-1)-(H-7) and the "(T)-block reading".  Verdicts.
(H-1)-(H-7) as a NECESSARY condition for a main stage not to be realized: CORRECT (mod chain), with the corrections: (H-3) for pieces (P-PC),
(H-4) in the exact LP form 3.5(iii) and with P-KC (every movable row of m with robust or near-threshold status anti-aligned thick-type), (H-6)
without the (U)-pieces of linking groups and without minors-only groups admitting a feasible LP direction (3.5 Extension).
Section 4.7 / table row 16 "(T)-block reading ... PROVED (characterization)": DOWNGRADE to HEURISTIC.  The Farkas representation is stated at a
smooth point of Z for ONE certificate; the obstruction is "no admissible displacement pairs positively with ALL near-certificates", whose
dual involves the closed convex hull of the certificate functionals; at singular points of Z the tangent space must be replaced by the
tangent cone, and Lemma 2.2's curves give displacements v + O(eps|v|) with delta(eps, r) not uniform in the base point r (J1.11's uniformity
came from compactness of Lambda, which is not available for an arbitrary target point).  The reading is a correct heuristic description.
"Persistence (PROVED, elementary)": correct under its explicit stabilization hypothesis; it does not show that the coincidences persist.

Numerics (H1_ref_work/slp_check.py): primal and dual values agree to 9e-16 on 300 random instances; an exact instance of (*) has V_LP = 0
and V_LP grows linearly off the resonance; one aligned object gives V_LP > 0.
