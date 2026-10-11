# J1 notes (Round 12): the Step-A obstruction classes (A*)/(U*) -- normal form, global rigidity, far placements, the
# one-out-of-many principle, target SETS and rescaling coupling; precise remaining class

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = proved here modulo the refereed chain that Theorem K2.15 / J2's Theorem
J2.1 already cite (X1/X1-ref, X2/X2-ref, Q1/Q1-ref a,b/cert0-3, Q2/Q2-ref a, K1/K1-ref, K2/K2-ref; several links once-refereed).  Part files:
r12/J1_part1.md (target form, normal form, rigidity), J1_part2.md (far placements), J1_part3.md (bands, one-out-of-many), J1_part4.md
(Puiseux margin, mismatch tolerance, gauge, target freedom), J1_part5.md (target sets, rescaling coupling, main theorem, residual); scripts
and outputs r12/J1_work/.  This file supersedes the part files where they differ.  Companion: r12/J2_notes.md (J2 removes (H1*): Step 0's
weak-peak pushes are dispensable; the only remaining hypothesis of the chain is Step A's A-regularity, task J1).

## 0. Bottom line
(1) THE OBSTRUCTION IS A TARGET-PLACEMENT OBSTRUCTION, AND IT IS GENUINE FOR THE CURRENT TARGETS (J1.2-J1.5, PROVED).  phi_y = y^T Ft is
    exactly the target displacement projected on the certificate; every residual certificate has the normal form Psi_y = kappa_y(a + Theta_y)
    + E_y with kappa_y < 0, Theta_y anti-signed on the data-carrying one-sided coordinates and of mass >= 1 - small; and the frozen functional
    Phi_y = Psi_y/kappa_y cannot be increased by ANY row change keeping those coordinates' signs (global, nonlinear: Cauchy-Schwarz).  Hence
    no improvement of the realization (degree arguments, larger moves, new two-sided levers on two-sided coordinates) can remove (A*)/(U*):
    one must move the targets, relax rows, or change the data.
(2) ONE-OUT-OF-MANY (J1.6(a), J1.9, PROVED).  Every near-certificate carries a ROBUST coefficient of FIXED sign, coef_k ~ kappa_y a_p/v_k(p),
    on EVERY thick-type coarse carrier k (one with a thick private design-depth coordinate p).  Hence relieving a SINGLE thick-type carrier
    removes ALL obstructions at once: (a) one helpful far placement (Theorem J1.7, makes K2.11 and K2 5.5 rigorous, overshoot included), or
    (b) relaxing its Step-A row to a band of half-width beta_* = 16 nu_1 (||b|| + 2 rho_0)/(c_* u) (Theorem J1.9), or (c) a private two-sided
    design-depth resource (K2.17).
(3) TARGET SETS (J1.13, J1.14, PROVED).  Step A need not realize target POINTS: only the active ratios occurring in tiny minors/cofactors
    ("pinned") must be realized on Z_kappa exactly; free active ratios and inactive values may be realized in bands, with the class data
    projected at the REALIZED ratios, as long as the statuses are kept.  In unshifted blocks the (Z-preserving) rescaling of the targets is
    coupled to the realized values and absorbs every R^2 drift.  Consequently (Theorem J1.15) Step A is realized whenever some thick-type
    carrier is: helpful far; zero-data with robust/tiny status in a (U)-block (or a block with no active carrier); active with a free ratio in a
    (U)-block; zero-data in a (T)-block when the Puiseux margin is first order; or active in a shifted block satisfying a mismatch tolerance
    -- in the (U)-block cases provided the block has a private two-sided peak resource.
(4) RESIDUAL (precise, 8).  At all large stages: every thick-type carrier rigid at once (frozen far window, no private two-sided resource, and
    pinned-active / KN-1 of a (T)-block without first-order Puiseux margin / R^2-sensitive shifted-block active / (KN)-block / D2-pushed /
    peak or block without private peak resource), or no thick-type carrier at all (pure (U*), thick support only on coarse targets).  In the
    stable case the residual is an exact resonance: Phi_0 = sum_{K_0} rho_k u_k equals a on the thick support and is a FLAT, purely
    block-represented direction at f (p*(f + t Phi_0) <= 1 + C t^2).
(5) (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) and of NA((c_0, p), l_2^2): OPEN, now reduced to the residual of 8 (with J2).
    No counterexample; nothing found points to one -- every residual configuration is a non-generic near-resonance of the companion
    construction (codimension >= 1 identities among f's data), not a property of a mate.

| # | Result | Status | Section |
|---|---|---|---|
| 1 | Lemma J1.1 (deviation identity Psi(zhat) = kappa_Psi + Dev_Psi(z); all generator actions through Dev_Psi) | PROVED | 2 |
| 2 | Lemma J1.2 (phi_y = target displacement along y; generators depend on targets only via peak columns) | PROVED | 2 |
| 3 | Lemma J1.3 (normal form of residual certificates; one-sided hole mass >= 1 - small) | PROVED | 3 |
| 4 | Lemma J1.4 (global rigidity of the frozen functional) | PROVED (+ numerics) | 3 |
| 5 | Corollary J1.5 (targets infeasible for every companion keeping the one-sided signs) | PROVED | 3 |
| 6 | Lemma J1.6 (orientation of thick-type coefficients; helpful placements: admissibility, cost, action) | PROVED (+ numerics) | 4 |
| 7 | Theorem J1.7 (one helpful far coordinate of one thick-type carrier => A-regular) | PROVED (mod chain) | 4 |
| 8 | Lemma J1.8 (band version of K2.9) | PROVED | 5 |
| 9 | Theorem J1.9 (one-out-of-many band) | PROVED (+ numerics) | 5 |
| 10 | Proposition J1.10 (legitimate bands; what fails and why) | PROVED ((KN)-blocks SKETCH) | 5 |
| 11 | Proposition J1.11 (first-order Puiseux margin mu_kappa(h) >= c_kappa h) | SKETCH | 7.1 |
| 12 | Proposition J1.12 (mismatch tolerance for active rows in shifted blocks) | PROVED (conditional) | 7.2 |
| 13 | Lemma J1.13 (only pinned active ratios need exact realization; data projected at realized ratios) | PROVED | 6 |
| 14 | Lemma J1.14 (rescaling coupling in unshifted blocks) | PROVED ((KN)-lever analogue SKETCH) | 6 |
| 15 | Theorem J1.15 (Step A realized at rows with one relievable thick-type carrier) | PROVED (mod chain) | 6 |
| 16 | Gauge: identity, admissibility, two-piece curvature dichotomy | PROVED; use as bypass SKETCH | 7.3 |
| 17 | Target freedom = interior of the achievable cone meets the target set | PROVED (characterization) | 7.4 |
| 18 | Stable exact case: Phi_0 flat and block-represented | PROVED | 7.4 |
| 19 | Remaining class | OPEN (precise) | 8 |
| 20 | (H2) at every row; (LSC-trunc)_N for every f; density for p_N, p | OPEN | 8, 10 |

## 1. Setting and notation
Design T_fin^{K2} (K2 6.1), with J2's frozen convention (FC) for the block scalars (weak peaks frozen as non-peaks; robust peaks as peaks).
N >= 1; f in S_{p_N*}, forced data f = a + L^*w, q*(a) = ||a||_1 + nu = 1, e = U^*a/nu, zhat = z + Ue, diagonal base U k_s = mu_s e_s (mu_s =
mu*_s = 2^{-2^{2^s}}), F = supp a arbitrary; g in C(f); rho in (0,1).  Main stage L >= l_f, clean sub-window w, class a; b = b(w), u = u(w),
T = T_lo(w), eta' = T^4/(L Design(L)), x = C Design(L) eta' (Step-A scale), W = Design^{C_A} u^{-3} max(x, ||b||) (K-7), rho_0 = C_2 W^2,
D = D(L), x'_max = u^2 T^3/(Design(L)^2 |Lambda|) (K1-ref R-6).  Input row of Step A: R_1 = f_1 + Pi (after the deep raise, (C1), (C2),
the preparation (P) and the pre-placements).  Sys-A (K1 2.4, K2 1): rows l in Lambda_A = all coarse strict non-peaks (+ D-pushed),
Ft_l = val_l - rt_l kappa_{m(l)}, val_l = eps_l u_l(zhat), targets rt: Lojasiewicz/Puiseux ratios r'' (active), current values (holds),
0 (KN-1), pushed values (D).  Generators G = G_2 (two-sided) ∪ G_1 (one-sided raises at data-carrying S_th coordinates).  Near-certificate of
size eps: unit y with y^T g >= -eps (g in G; for g in G_2 also -g).  phi_y := y^T Ft(R_1); zeta_m := sum_{l in m} y_l rt_l; Psi := Psi^A_y :=
sum_l y_l eps_l u_l - sum_m zeta_m K_m (K2.8), coef_k its coefficient on u_k.  THICK-TYPE carrier: a coarse carrier (tuned or a peak) with a
thick private coordinate p in S_k ∩ [1, D] (|a_p| >= u/2).  Far window FW_k := {j in S_k : Design^{C_J} x/u <= |v_k(j)| <= x'_max}, C_J = C_A + 4.

## 2. Step A in target form
LEMMA J1.1 (deviation identity).  PROVED.  For u in l_1 let kappa_u := <U^*u, e>/nu, Dev_u := u - kappa_u a.  Then <U^*Dev_u, e> = 0,
u(zhat) = kappa_u + Dev_u(z), and the first-order actions of K2.4 are (mu_s^2/nu) Dev_u(s) dm (mass at s in F), (mu_s^2/nu) Dev_u(s) z_s dm
(bank at a contact s notin F), Dev_u(s) dz (z-move, s notin F).
Proof.  <U^*Dev_u, e> = kappa_u nu - kappa_u <U^*a, e> = 0; a(zhat) = ||a||_1 + nu = 1 (z = sgn a on F); u(zhat) = kappa_u a(zhat) + Dev_u(z) +
<U^*Dev_u, e>; K2.4 with D_u(s) = Dev_u(s) (s in F), Dev_u(s) = u(s) (s notin F).  QED
LEMMA J1.2 (target-displacement form).  PROVED.  With rc_l := val_l(R_1)/kappa_{m(l)}(R_1): Ft_l(R_1) = kappa_m (rc_l - rt_l) and
phi_y = sum_m kappa_m sum_{l in m} y_l (rc_l - rt_l) = Psi(zhat_1) (Euler, K2.8(a)); phi_y = 0 if all targets equal the current ratios.  The
generators depend on the targets only through the peak columns col_c = -(1 - X) lambda_c rt^{(m)} - h_c gtil (action -(1 - X) lambda_c zeta_m -
h_c y^T gtil).  Proof: definitions.  QED
So every obstruction of K2.9(b) is: a near-certificate with sum_m kappa_m sum_{l in m} y_l (rt_l - rc_l) < rho_0 (the targets lie on the
wrong side of y).

## 3. Normal form and global rigidity
LEMMA J1.3 (normal form).  PROVED.  Let y be a near-certificate of size eps <= eps_* with phi_y > -rho_0, kappa := kappa_Psi <= -c_*/nu_1
(K2.16(3)).  Let S_1 (S_2, S_0) be the design-depth coordinates carrying a one-sided generator (a two-sided generator; neither), Deep :=
(D, infinity), Theta := Dev_Psi 1_{S_1}/kappa, E := Dev_Psi 1_{S_0 ∪ S_2 ∪ Deep}.  Then Psi = kappa(a + Theta) + E with
 (a) |E(s)| <= eps Design (s in S_2), <= 2|kappa| b (s in S_0), ||E 1_Deep||_1 <= tail_D + |kappa| alpha(D);
 (b) Theta(s) z_s <= eps Design^2/|kappa| on S_1 (anti-signed: z_s is the data sign there);
 (c) sum_{s in S_1} (-Theta(s) z_s) >= 1 - (rho_0 + |E(z)|)/|kappa|, |E(z)| <= D(eps Design + 2|kappa| b) + tail_D + |kappa| alpha(D).
Proof.  (a) K2.16(2),(4),(5); off U_L, Psi(s) = 0 so Dev_Psi(s) = -kappa a_s with |a_s| <= 2b; deep: K2.16's proof of (1).  (b) the raise at
s in S_1 acts by eff_s Dev_Psi(s) z_s >= -eps (J1.1), eff_s >= 1/Design, kappa < 0.  (c) J1.1: phi_y = Psi(zhat_1) = kappa + kappa Theta(z) +
E(z); divide by kappa < 0, use phi_y > -rho_0.  QED
LEMMA J1.4 (global rigidity).  PROVED.  Put Phi := Psi/kappa = a + Theta + E/kappa.  For every row R' = (a', z') (normalized) with z'_s = z_s
and a'_s z_s >= 0 for s in S_1:
      Phi(zhat') - Phi(zhat_1) <= [delta(R') - delta(R_1)] + [E(zhat') - E(zhat_1)]/kappa,   delta(R) := sum_{s in S_1} mu_s^2 Theta(s) a_s/nu(R),
and the right side is <= eps Design^2 sum_{S_1} mu_s^2 (|a'_s|/nu' + |a_s|/nu)/|kappa| + (||E 1_{S_0 ∪ S_2}||_1 ||z' - z||_inf + 2||E 1_Deep||_1 +
||U^*E|| ||e' - e||)/|kappa|.
Proof.  a(zhat') = a(z') + <U^*a, e'> <= ||a||_1 + ||U^*a|| = 1, with equality at R_1; Theta(zhat') = Theta(z) + sum_{S_1} mu_s^2 Theta(s) a'_s/nu'
(diagonal base, z'_s = z_s on S_1); each summand <= mu_s^2 (eps Design^2/|kappa|)|a'_s| by J1.3(b); E(zhat') - E(zhat_1) = E(z' - z) + <U^*E, e' - e>.  QED
[Equality in a(zhat') <= 1 iff e' = e: every move that turns U^*a strictly lowers Phi at second order; numerics: 20000 random rows, 0 violations.]
COROLLARY J1.5 (genuine infeasibility).  PROVED.  If every block meeting supp y has a private two-sided peak resource (so |zeta_m| <= 2 eps
Design) and R' satisfies the hypothesis of J1.4 with Ft(R') = 0, then
      phi_y <= |kappa| (bound of J1.4 at R') + 2 eps Design sum_m |kappa_m(R') - kappa_m(R_1)| + 2 eta_K (1 + ||U||),   eta_K := 2 eps Design sum_m ||K_m||_1.
Proof.  Psi_0 := sum_l y_l eps_l u_l = Psi + sum_m zeta_m K_m = kappa Phi + (vector of l_1-norm <= eta_K).  Ft(R') = 0 gives Psi_0(zhat') =
sum_m zeta_m kappa_m(R'); at R_1, Psi_0(zhat_1) = phi_y + sum_m zeta_m kappa_m(R_1).  J1.4 and kappa < 0: Psi_0(zhat') - Psi_0(zhat_1) >= -|kappa|
(bound) - 2 eta_K (1 + ||U||).  Combine.  QED
So when phi_y is of the size of the target displacement, NO companion keeping the data-carrying one-sided coordinates as contacts/supports of
their data sign realizes the targets, whatever its moves: targets, row relaxations or data must change.

## 4. Orientation of thick-type coefficients; far placements
LEMMA J1.6.  (a) PROVED.  If k is thick-type with thick private p, every near-certificate of size <= eps_* satisfies |coef_k - kappa_y a_p/
v_k(p)| <= eps Design^2, kappa_y <= -c_*/nu_1; so sgn coef_k = -sgn(a_p v_k(p)) and |coef_k| >= c_* u/(4 nu_1) for ALL near-certificates (if two
thick private coordinates have ratios a/v differing by a factor outside [1 - u, 1 + u], no near-certificate exists).  Proof: K2.16(2b) at p
(divide by |v_k(p)| >= 1/Design), K2.16(3) (valid for every near-certificate), K2.16(3)'s kind-(ii) case.  QED
(b) PROVED.  tau_k(j) := sgn(a_p v_k(p) v_k(j)).  j in FW_k is HELPFUL if z_j tau_k(j) <= 0 and (j notin F, or j in F with |a_j| <= x'_max).
The PLACEMENT at j (lower a_j to 0 if j in F; put support tau_k(j) of mass 24 lambda_k |v_k(j)|; for zero-data k a z-move suffices) is
admissible (aligned data impose nothing; anti-sign data are dominated by the pull mass, V1 Lemma TU / K1 2.1(b); after the deep raise far
support has |a_j| >= 8 lambda_k |v_k(j)|, K1 1.2), costs <= C Design x'_max log(1/T) (Z3 Lemma 3.1, Q2 Lemma LT; R-6 budget), and changes y^T Ft
by coef_k v_k(j)(tau_k(j) - z_j) + O(c_{L+1} + Design^C x'^2_max) for every unit y, every generator column by <= C Design^C x'_max.
Proof: J1.1(c) (Dev_Psi(j) = Psi(j) = coef_k v_k(j) + fine, j private), mass effect mu_j m_j/nu negligible, second-order terms of K2.8(b).  QED
THEOREM J1.7.  PROVED (mod chain).  If some thick-type carrier has a helpful coordinate in its far window, then after adding its placement
to the pre-placements Step A is A-regular (W' = Design^{C_A} u^{-3} max(x, ||b'||), ||b'|| <= ||b|| + 3 x'_max) and realized by K2.9(c) (K-8/(FC)).
Proof.  A failure gives (K2.9(b)) a near-certificate y at R' of size < 4 Design^{-C_A} with phi'_y > -rho'_0; it is a near-certificate of size
<= 2 eps at R_1 + Pi (columns move by << Design^{-C_A}), so by J1.6(a) coef^y_k v_k(j)(tau - z_j) <= -(c_* u/(2 nu_1))|v_k(j)| + O(eps Design^2 x'_max)
(1 - tau z_j >= 1); hence phi'_y <= |Lambda_A|^{1/2} max(x, ||b||) - (c_* u/(2 nu_1)) Design^{C_J} x/u + O(c_{L+1} + Design^C x'^2_max) < -rho'_0
(rho'_0 <= C_2 Design^{2C_A} u^{-6} 9 x'^2_max << x).  Contradiction.  Moves <= W' << u, cost <= C_f Design^C W' log(1/W') = o(u^2 T^2).  QED
The placement lowers phi_y for ALL near-certificates at once (J1.6(a)), so no new certificate can appear -- the point K2.11 left open.
FROZEN-WINDOW RESIDUAL.  PROVED (necessary condition).  If Step A is not A-regular for any pre-placements, every thick-type carrier has, on
FW_k, z_j = tau_k(j) or (j in F, sgn a_j = -tau_k(j), |a_j| > x'_max).  Proportionally swallowed rows a = sum rho_k v_k on S_k satisfy this.

## 5. Bands and the one-out-of-many principle
LEMMA J1.8 (band version of K2.9).  PROVED.  Rows split into equality rows and band rows (half-widths beta_l); Box := sum_B [-beta_l/2,
beta_l/2] e_l.  (a) If B(b, rho_0) ⊂ (W/2) conv(G ∪ {0}) + Box, the band-relaxed Step A is realized (K2.9(c)'s Brouwer argument with
unknowns (t, sigma) in {||t|| <= W} x Box and the minimal-norm selection).  (b) Otherwise some unit y with max_g(-y^T g) < 2(rho_0 + ||b||)/W
has phi_y > (1/2) sum_B |y_l| beta_l - rho_0.  Proof: separation of b'' in B(b, rho_0) from (W/2)Q + Box (the support function of Box is
(1/2) sum |y_l| beta_l), as in K2.9(b).  QED
THEOREM J1.9 (one-out-of-many).  PROVED.  If the row of one thick-type strict non-peak k is relaxed to a band of half-width beta_k >= beta_* :=
16 nu_1 (||b|| + 2 rho_0)/(c_* u), the relaxed Step A is realized.  Proof: J1.8(b) gives a near-certificate with phi_y > |y_k| beta_k/2 - rho_0;
|y_k| >= |coef_k| - |zeta_m| lambda_k d kappa/d zeta(k) >= c_* u/(8 nu_1) (J1.6(a); route V: d kappa/d zeta(k) = rho_k M X/C <= C b^2 D^2); so
phi_y > ||b|| + rho_0 >= |phi_y| + rho_0.  Contradiction.  QED
[Numerics: at resonant near-certificates, a band on the thick-type row lowers the minimal realizing move from 29-143 to 1.4e-4; the same
band rule on a row with |y_l| ~ 1e-8 changes nothing.]
PROPOSITION J1.10 (legitimate bands).  PROVED (except where marked).  Inactive targets are used downstream only through statuses (Lemma K;
(U)-block margin eta'; (KN)-lever margin; Puiseux margin mu in (T)-blocks; robust margins; X1 2.2(iii)'s floor row needs only rho - rho^0 <=
C gap/t, weaker).  A band of half-width beta on an inactive row l of block m is legitimate if (B1) l keeps its status class and (B2) the R^2
change m^2(2|r_l| beta/kappa + beta^2/kappa^2) moves the protected statuses of block m by < 1/4 of their margin.  Hence: (a) nearly neutral
inactive rows of (U)-blocks: beta_* legitimate; (b) robust inactive rows of blocks without protected statuses: beta_* legitimate;
(c) KN-1 rows of (T)-blocks: legitimate iff mu_kappa(eta'/3) >> Design^C (beta_*/kappa)^2 (true under J1.11, not known in general);
(d) robust holds of protected blocks: not legitimate as a plain band (factor Design^C/u, circular) -- but see J1.14; active rows: see 6.
[(KN)-blocks: SKETCH, needs the KN-lever margin bookkeeping.]

## 6. Target sets, rescaling coupling, main theorem
LEMMA J1.13.  PROVED (inspection).  Call an active ratio FREE if no tiny minor and no tiny cofactor polynomial of Gamma^#(kappa, a) depends on
it, PINNED otherwise.  Downstream (class data, Theorems UE^inf, E^{eng,RT,inf}) Step A must provide only: (i) realized ratios r^# on Z_kappa
(pinned ones exact), robust minors >= u/4, |r^# - r_1| <= eta' + Design^C beta_*/kappa; (ii) the statuses ((T): rho <= 1 - mu/2; (U): <= 1 -
eta'/2; (KN): U1-ref Prop. KN(b); robust ones robust; KN-1 values with m^2 sum r^2 <= mu/(C D^C)).  The class data are then projected onto
Gamma^#(kappa, a) at r^# itself (Lemma H: tiny minors exactly 0, robust ones >= u/4: same Hoffman bound), so the true shift is the cone shift.
Proof.  The projection of the decomposition data can be performed after the realization; free ratios enter no tiny minor; the other uses of
ratios are statuses (Lemma K, Lemma PM, X1 2.2(iii)) and move sizes; inactive values enter only through statuses (K1 2.4; cert0 3.2).  QED
LEMMA J1.14 (rescaling coupling).  PROVED.  In a (U)-block (Delta'_m = 0, including blocks with no active carrier) replace the targets s r'^{(m)}
by s_m r'^{(m)}, s_m := the largest s <= 1 - C Lip eta' making every active status of block m (and every D2-pushed one, with its push enlarged
likewise) <= 1 - eta'/2 at the realized values.  Z_kappa is preserved (minors homogeneous in r^{(m)}, cert0 3.4 D1), s_m is continuous in the
realized values with 1 - s_m <= C(Lip eta' + D^C sum_l (|r_l| beta_l/kappa + beta_l^2/kappa^2)), and the coupled system has a Brouwer solution
whenever J1.8(a) holds uniformly over the range of s_m.  Proof: Lemma K (statuses m|r_d| K(sigma, R^2)/Phi_d; scaling lowers |r_d| and K);
dK/dR^2 <= C D^C (X1 1.1); continuity of the minimal-norm selection in the right-hand side.  QED  [(KN)-lever analogue: SKETCH.]
THEOREM J1.15 (Step A at rows with one relievable thick-type carrier).  PROVED (mod chain).  At a stage (L, w, a) Step A is realized (and
J2's Theorem J2.1 / K2.15 apply at the stage) if there is no near-certificate of size <= eps_*, or if some thick-type carrier k satisfies:
 (J-a) a helpful coordinate in FW_k (J1.7);
 (J-b) a private two-sided design-depth resource, a robust-spread thick pair, or a same-orientation thick/S_th pair (K2.17(c)-(e));
 (J-c) zero-data strict non-peak of robust or tiny status (not D2-pushed) in a (U)-block or a block with no active carrier, the block having
       a private two-sided peak resource;
 (J-d) active strict non-peak with a FREE ratio in a (U)-block having a private two-sided peak resource;
 (J-e) zero-data in a (T)-block with mu_kappa(eta'/3) >= C D^C m^2 (beta_*/kappa)^2 (automatic under J1.11);
 (J-f) active in a shifted block satisfying (MT1)-(MT3) of J1.12 with delta_0 >= beta_*/kappa_m, or active with a free ratio in a shifted block
       without R^2-sensitive protected statuses (J1.13).
Proof.  (J-a) J1.7; (J-b) K2.17.  (J-c), (J-d): band of half-width beta_* on k's row (J1.13), statuses restored by J1.14, data projected at the
realized ratios; NON-CIRCULARITY: the coupling moves the targets of block m by (s_m - 1) r'^{(m)}, changing phi_y by kappa_m (s_m - 1) zeta_m(r'),
and |zeta_m| <= 2 eps Design (private two-sided peak resource), so this is <= C Design^C eps beta_* << c_* u beta_*/(32 nu_1); then J1.9 (for
every s_m in its range) and J1.8(a).  (J-e): (B2) holds.  (J-f): J1.12 resp. J1.13.  QED
Consequently (LSC-trunc)_N holds at (f, g, rho) as soon as, at infinitely many main stages, Step A carries no near-certificate or some
thick-type carrier satisfies one of (J-a)-(J-f).

## 7. Further tools
7.1 PROPOSITION J1.11 (first-order Puiseux margin).  SKETCH.  For the generic-weight design, mu_kappa(h) >= c_kappa h for small h.
Argument: GEN's proof applies to every semialgebraic set of dimension < |N_T| definable over k = k_0(other weights), in particular to the
union of critical-value cylinders of Psi_{D,S} over a Whitney stratification of Z; so every point of Z ∩ {F = 1} is a regular point (first-
order decrease direction).  A bad semialgebraic curve r(h) (G_h(r(h)) >= 1 - o(h)) tends to r_* in Z ∩ {F = 1}; if |r(h) - r_*| = o(h), go to r_*
and descend: contradiction.  GAP: the case |r(h) - r_*| >= c' h needs a curve in the stratum of r(h) of length ~h with second-order error o(h)
(local reach of the stratum at scale h; Whitney (a) gives the tangent direction, not the reach).  If proved: (R-T) below is empty and KN-1
exactness (X1's KN-1, Q1-refb P-HOLD) can be replaced by bands of half-width << sqrt(eta').
7.2 PROPOSITION J1.12 (mismatch tolerance).  PROVED (conditional).  An active thick-type k in a SHIFTED block m may be realized within
|r_k - r''_k| <= delta_0 if (MT1) no FREE E_c coordinate lies in supp tau_m (peak traces) and target contacts in supp tau_m have class-data
slack >= delta_0 |gamma_k(t)| |tau_m(j)|, (MT2) the (X4^0) rows of block m have slack >= C delta_0 |gamma_k(t)| (or k is not in a (T)-block
with near-threshold actives), (MT3) statuses as in (B1), (B2).  Proof: the true shift is Delta' + delta gamma_k(t) (U1 Lemma 4.6); only
Delta-sensitive rows change; peak-private contacts have robust slack |Delta'| lambda_p |v_p| (shifted block); (X2) signs kept; (MT1), (MT2).  QED
7.3 THE GAUGE.  (a) IDENTITY (PROVED): for any block vector rhot and reals s_+-, the pieces (b^+- - s_+- B(rhot), omega^+- + s_+- rhot), B(rhot) :=
sum_m R_m^*(rhot_m - d_m(rhot_m) w_m), represent the same g_t; the switching changes by (s_- - s_+) rhot.  (b) With rhot = (rho_k/lambda_k) on
the thick-type non-peaks K_0: B(rhot) = Phi_0 - sum_m d_m(rhot_m) R_m^* w_m, Phi_0 := sum_{K_0} rho_k u_k = a on the thick private coordinates,
d_m(rhot_m) = Phi_0^{(m)}(xi)/A_m.  (c) ADMISSIBILITY (PROVED): adding -s Phi_0 to a piece is admissible at thick F-coordinates (cushion, |s| <=
C/t), at anti-signed holes for s >= 0, at contacts with Phi_0 z > 0 only within slack, NEVER at free E_c coordinates with Phi_0 != 0.
(d) CURVATURE DICHOTOMY (PROVED): with Q = Gamma_w (psd quadratic form on representations) and G = (-B(rhot), rhot), the two-piece gauge
achieving a switching change s_0 along rhot exists with no piece's curvature increasing whenever 0 <= s_0/s_0^Gamma <= 2, s_0^Gamma :=
Q(P^- - P^+, G)/Q(G) (t -> Q(P + tG) is a convex parabola, <= Q(P) between 0 and twice its minimizer); if the switching through K_0 is
exactly along rhot (e.g. one thick-type carrier), s_0 = s_0^Gamma.  (e) USE: deactivating a single thick-type carrier without curvature
cost, then J1.9 -- SKETCH (needs exact d_m(rhot) = 0, no free E_c coordinate in supp Phi_0, and a re-pigeonhole of the gauged data).
7.4 TARGET FREEDOM AND THE STABLE EXACT CASE.  (a) PROVED (characterization): Step A is A-regular iff the target displacement lies robustly in
the interior of the achievable cone C_ach = span(G_2) + cone(G_1) (incl. the target-dependent peak columns); target freedom = Tgt ∩ (r_1 +
kappa^{-1}(int C_ach - b_inact)) != {}.  (b) FUZZ (PROVED): near-certificates are orthogonal to two-sided generators only up to eps <=
4 Design^{-C_A} >> eta', so target-freedom arguments need displacements with <kappa y, delta> >= Design^C eps eta', and zeta_m ~ 0 holds only up
to 2 eps Design.  (c) STABLE EXACT CASE (PROVED): if the thick-type set K_0 and the rho_k stabilize, the residual relations are exact at f
(a = Phi_0 on the thick part of F; Phi_0^{(m)}(xi) = 0 for every block); then Phi_0 = sum_m R_m^* rhot_m with d_m(rhot_m) = 0, and since
N_m(w_m + t rhot_m) = 1 + O(t^2) (rhot vanishes on peaks; <D w, D rhot> = (C/A) Phi_0^{(m)}(xi) = 0), p*(f + t Phi_0) <= max(q*(a), max_m N_m(w_m +
t rhot_m)) = 1 + O(t^2): Phi_0 is a flat, purely block-represented direction (a scaled mate) whose base trace is a.

## 8. The remaining class (precise).  OPEN.
(f, g, rho) is not covered by Theorem J1.15 + J2 only if, at all but finitely many main stages L, at every clean sub-window and every
admissible class, Step A carries a near-certificate (normal form J1.3; infeasibility J1.5) AND
 (R0) EVERY thick-type coarse carrier is rigid simultaneously: frozen far window; no private two-sided design-depth resource; spreads
      <= Design^{2 - C_A} on its thick private coordinates; and of one of the types
      (R-pin)  active with a PINNED ratio (in a tiny minor/cofactor), any block;
      (R-T)    zero-data in a (T)-block (KN-1) with mu_kappa(eta'/3) < C D^C m^2 (beta_*/kappa)^2 [empty under J1.11];
      (R-Ts)   active with a free ratio in a shifted block with an R^2-sensitive protected status, failing (MT1)-(MT3);
      (R-KN)   zero-data in a (KN)-block [covered once the KN-lever coupling is done];
      (R-D2)   zero-data, D2-pushed, in a (U)-block, with outward needed direction;
      (R-np)   zero-data or free-active in a (U)-block WITHOUT private two-sided peak resource;
      (R-pk)   a peak whose block has no private two-sided peak resource;
 or
 (R1) there is NO thick-type carrier (all thick design-depth support of a lies on coarse TARGET coordinates T(L)) and the certificates are of
      pure type (U*) on active kind-(iv) carriers (all design-depth private coordinates S_th of the data sign; far windows swallowed by anti-
      data-sign support), the one-sided hole mass >= 1 - small sitting on their S_th coordinates; here no carrier has a uniform-sign robust
      coefficient, so the one-out-of-many principle does not apply.
Comparison with K2 7.3 / K2-ref G: (W*) is gone (J2); (A*)/(U*) is now restricted to configurations in which every thick-type carrier is
simultaneously rigid in all the senses above, or there are no thick-type carriers.

## 9. Numerics (sanity only; r12/J1_work/)
 check_part1.py/.out: J1.1 identity to 1.7e-14; J1.4 on 20000 random rows (one-sided coordinates pinned): max(Phi(zhat') - bound) = -1.5e-4,
   0 violations.
 check_orient.py/.out: 106 random one-block configurations of K2-ref's model with far coordinates: no exact certificate (they are codimension-
   one phenomena; K2-ref's ref_sysA2 found none in 381 either).
 check_resonant.py, check_resonant2.py/.out: exactly resonant configurations (two anti-aligned thick-type carriers, hole profile tuned by brentq
   so that Phi_0(zhat) = 0): near-certificates of size 3e-6..2.6e-4 (-> 0 with the bank mass); one-sided actions 0.63 > 0; kappa_Psi in
   [-2.09, -1.93] < 0; coef_k/(kappa rho_k) = 1.0000 (J1.6(a)); the far pull lowers y^T Ft by exactly the predicted coef_k v_k(j)(tau - z_j).
 check_band.py/.out: J1.9: minimal realizing move 29-143 without band vs 1.4e-4 with a band on the thick-type row; no effect of a band on a row
   with negligible certificate weight.

## 10. Main obstacle; next steps
MAIN OBSTACLE.  The frozen functional Phi_y is pinned from above by the data-carrying one-sided coordinates (J1.4), so the Lojasiewicz/
Puiseux TARGETS must be on its achievable side; the targets are forced by Z_kappa (pinned ratios) and the Puiseux margin, and the
R^2-sensitivity of protected statuses forbids wide bands in shifted blocks.  The residual needs simultaneous rigidity of all thick-type
carriers, or no thick-type carriers (pure (U*) on target-supported rows).
NEXT STEPS.  (1) Prove J1.11 (first-order Puiseux margin; a semialgebraic reach lemma along curves approaching a Whitney stratum) -- this
removes (R-T) and the KN-1 exactness globally.  (2) (R-pin): a CONSTRAINED Lojasiewicz step -- exactify the tiny minors involving a thick-type
ratio by moving only the other ratios, or show that such minors are the frozen combination itself (lineality case) and use the gauge (7.3)
with exact d_m(rhot) = 0 (true in the stable exact case).  (3) Carry out the KN-lever coupling ((R-KN)).  (4) (R1): find a uniform-sign object
for pure (U*) (a combination at thick TARGET coordinates: sum_k coef_k u_k(p) ~ kappa_y a_p is uniform in y) and a corresponding combined band
or placement.  (5) Treat stable exact resonances directly through the flat block-represented direction Phi_0 of 7.4(c).
