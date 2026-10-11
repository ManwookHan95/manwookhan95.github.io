# H1 referee notes (Round 13): proofs of the verdicts, the fixes, and three referee additions (Lemma PC, Proposition MA', Lemma SLP)

Refereed: r13/H1_notes.md (+ H1_part1..4.md, H1_work/).  Setting and notation of r12/J1_notes 1 and r13/H1_notes 1: design T_fin^{K2} with
(FC), P-TU windows and F-2; stage (L, w, a); input row R_1; Sys-A rows l (coarse strict non-peaks + D-pushed), Ft_l(rt) = val_l - rt_l kappa_{m(l)};
near-certificates y of size eps <= eps_*; kappa_y <= -c_*/nu_1 (K2.16(3), every near-certificate); thick-type carrier k, rho_k = a_p/v_k(p);
zeta_m(y; rt) = sum_{l in m} y_l rt_l.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN; "PROVED (mod chain)" = modulo the refereed chain cited
by J1.15' and J2.1 (several links once-refereed) and J1.13's inspection.  Part files: r13/H1_ref_part1.md (Lemma 2.2, J1.11, Cor 2.4),
part2 (TF', AL, NP, RL, KC, MA'), part3 (IN, OUT, GS/DS/UC/TG, MA, SLP, peak conversion, residual).  Scripts: r13/H1_ref_work/.
This file supersedes the part files where they differ.

## A. Verdicts
| H1 claim (H1 label) | Verdict | Items |
|---|---|---|
| Lemma 2.1 regular contact points (PROVED) | correct | B.1 |
| Lemma 2.2 stratified projected flow (PROVED) | correct | B.1 |
| Proposition J1.11 first-order Puiseux margin (PROVED) | correct | B.1, PJ-1 (option (b) carrier 1) |
| Corollary 2.4 (R-T) empty (PROVED mod chain) | correct | B.1; remark (c) is an inspection claim |
| Lemma TF / TF' (PROVED mod chain) | correct (TF' form) | P-TF |
| Lemma NP (PROVED mod chain) | correct | B.2; numerics N1 |
| Theorem RL (PROVED mod chain) | correct | B.2; numerics N1 |
| Lemma KC (PROVED mod chain) | correct, strengthened | P-KC |
| Lemma AL (PROVED mod chain) | correct | B.2 (missing eps_l on an error term) |
| Theorem IN (PROVED mod chain) | correct with fixable gap | P-IN (constant), P-KN |
| Theorem OUT (PROVED mod chain) | correct | P-TF (sizes u^{-2}), P-KN |
| Theorem GS (PROVED mod chain) | correct, strengthened | P-PC |
| Proposition MA (PROVED mod chain) | correct, bookkeeping precision | P-MA; generalized by MA' |
| Lemma DS, Theorem UC, Lemma TG (PROVED mod chain) | correct, strengthened | P-PC |
| Remark 4.3 last sentence / (H-6) "linking groups not scalable" | FALSE (too pessimistic; harmless) | P-PC |
| Peak conversion (SKETCH) | label honest; three further gaps | C.6 |
| Residual (H-1)-(H-7) (PROVED as necessary condition) | correct after corrections | E |
| 4.7 "(T)-block reading" (PROVED characterization) | overclaim: HEURISTIC | C.7 |
| Persistence (PROVED, elementary) | correct under its stabilization hypothesis | E |
| (LSC-trunc)_N for every f; density for p_N, p (OPEN) | OPEN | G |

## B. Re-derivations of the main claims
B.1 Lemma 2.2, J1.11, Cor 2.4 (details: part 1).  Lemma 2.2: on every stratum S' meeting B(r_*, 2 delta) the field P_{T_x S'} v satisfies
|V| <= |v| everywhere and |V - v| <= eps|v| (Whitney (a) at r_* plus compactness of the Grassmannian, finitely many strata); a maximal integral
curve that stops converges to a point of cl(S') \ S' (escape lemma), which lies in a stratum of smaller dimension (frontier condition); the
concatenation from y has at most dim Z + 1 pieces and stays in B(r_*, 3 delta/2).  J1.11: regular contact points (semialgebraic Sard on the
cylinders of a stratification), local linear decrease along Lemma 2.2's curves, compactness of Lambda; the failure set B^lin is first-order
definable over k = k_0(other weights) (K satisfies (1 - R^2)k^2 - 2 sigma k + sigma^2 - sigma = 0), B^lin ⊂ B^reg, dim < |N_T|, GEN.  Cor 2.4:
(J-e) reads Design^{C'} eta'^2/u^2 <= eta'/(3 Design), true since eta' <= (u/(4 Design))^{4L^2 + 80}.  Remark (c) (no other use of the KN-1
exactness) agrees with X1-ref 8 ("KN-1: why the exact hold is necessary": only the non-explicit exponent) and Q1-refb F5 (P-HOLD); accepted as
an inspection claim; no H1 result depends on it.
B.2 Lemma AL, Lemma NP, Theorem RL (details: part 2).  AL: y_l = eps_l coef_l + eps_l zeta_m lambda_l d kappa/d zeta(l), coef_l = kappa_y rho_l +
O(eps Design^2), rt_l = eps_l u_l(xhat_1)/kappa_m + O(x), so y_l rt_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 + Design^2 eta' + b^2 D^2),
with a main term >= c_* u^2 Phi_l/(2 nu_1 m K) (u(w) decays only like (log 1/T)^{-1/20}, so it dominates eps_* = Design^{-C}).  NP(b): the six
private near coordinates of a peak are TS/S_th/FR/ZD (K2 4.1(d)); a (U)-block peak carries no class data, so its S_th coordinates are ZD; FR/ZD
would be peak resources; hence every peak is thick-type.  In route V kappa_m = sum_{c in P}|zeta(c)| + S_m/theta_m and the threshold equation
sees the peaks only through sum_P|zeta(c)| and Phi_P^2, so d kappa_m/d zeta(c) = vs_c (1 - X_m) with one value for all peaks (numerics:
peakderiv.py).  coef_c = -zeta_m lambda_c vs_c(1 - X_m) = kappa_y rho_c + O(eps Design^2) gives sgn zeta_m = sgn(rho_c vs_c) for every
near-certificate and |zeta_m| >= c_* u/(4 nu_1).  RL: Lemma TF' with Delta = sigma_m rt^{(m)}; whole-block rescaling of a (U)-block preserves
every tiny polynomial (homogeneity in r^{(m)}, X1-ref D1, other blocks' ratios being parameters); (RL+)'s hypothesis is "m unprotected" (in
(U)-blocks the inactive near-threshold carriers are exactly the D2-pushed ones, X1-ref D2).

## C. Findings and fixes
P-TF (Lemma TF'; precision).  H1's levers use displacements up to Design^C u^{-C'}(||b|| + x) with C' <= 4 (exchange: t/rt_k with c_ex ~ u/Design^C
and |rt_k| >= u/Design^C; KC: lambda_{d_0} ~ delta Design^C/u^2), not the u^{-1} of TF' / H1 11.  Harmless: (i) C_G|rt' - rt_0| <= eps_*/2 and
rho_0(rt') <= x/4 hold for any fixed polynomial in Design/u since eta' <= (u/(4 Design))^{4L^2+80}; (ii) choose P-TU's x_TU := Design^{C_A + C_J +
C_H} u^{-C_H} x with ONE absolute C_H covering all H1 levers (the window [x_TU, x'_max] keeps ratio >= 2^{6G(L)} for L >= l_f; a larger x_TU only
enlarges the (U)-class, as R-6/P-TU did); (iii) J1.13's distance allowance and the closeness K t tolerate Design^C u^{-C} x (violations <=
Design^C u^{-C} x/t << K t, x/t <= C T^3).  The proof of the first form TF in H1_part2 2.1 bounds ||kappa Delta||/c_Delta "by (TF2)", which gives
the opposite inequality; the endpoint form TF' assumes the size bound directly and is the form to keep.
P-IN (Theorem IN, nearly neutral clause; constant slip).  |y_l| >= c_* u/(8 nu_1) and a displacement beta_*/kappa_m give |y_l| beta_* >= 2(||b|| +
2 rho_0), not 4(||b|| + x).  Fix: displace by beta' := 2 beta_* + 32 nu_1 x/(c_* u) (same order); every estimate changes by a factor <= 4.  [The
remark "J1.9's band is the case Delta = +-e_k" is correct only up to such constants: J1.9 uses J1.8(b)'s factor 1/2.]
P-KN ((KN)-blocks).  IN/OUT/exchange/KC in (KN)-blocks need U1-ref Prop. KN(b)'s lever margin to survive target changes.  For inward moves and
exchanges (no first-order status increase) this follows from Lemma K; for the nearly-neutral displacement the R^2 change is second order.  The
bookkeeping of the KN lever push inside Step A (J2-ref Q-KN) was left SKETCH by J1 and is not re-derived by H1: (KN)-block clauses are PROVED
modulo that SKETCH.
P-KC (Lemma KC; strengthening, PROVED).  N_0 need not contain the D2-pushed rows: a D2 row outside N_0 is up-scaled with the rest and its status
is multiplied by (1 + delta) K(R'^2)/K(R^2) <= 1.  So N_0 = {d_0} suffices, and d_0 may be any MOVABLE row of m (inactive, or active with a
free ratio) with robust or near-threshold status (m|rt_{d_0}| >= u Phi_{d_0}/K still gives lambda_{d_0} <= delta Design^{C_K}/(2u^2)).  Since inactive
rows are zero-data, their S_th near coordinates are ZD; an inactive row is therefore of kind (i) (then (KC) holds), of kind (ii) (no
near-certificate), or support-swallowed thick-type.  Consequence for (H-4): EVERY movable row of m with robust or near-threshold status is an
anti-aligned thick-type carrier or an active free kind-(iv) row with rt eps sigma > 0.  (Exact form: Lemma SLP, D.3.)
P-PC (internal groups; strengthening, PROVED): Lemma PC (D.1).  GS(a)-(d), Lemma DS, Theorem UC and Lemma TG hold for PIECES G ∩ m of
arbitrary pinned groups in (U)-blocks.  Remark 4.3's last sentence ("groups linking a (U)-block to a SHIFTED block are not scalable") is FALSE
as stated: their (U)-block pieces are scalable; only their shifted-block parts belong to (H-6).  (H-3) becomes "every piece balanced".
P-MA (Proposition MA; bookkeeping).  A thick-type carrier may also be of kind (iv) (thick private coordinate deeper than N_l); by K2.17(d) its
S_th data sign is -sgn(a_p) and coef_l = kappa_y rho_l robustly: count it among the thick rows, and let the kind-(iv) sum run over non-thick
kind-(iv) rows.  Wording: H1 6 Consequence (a) / bottom line (4) say the peak-resource case "covers J1's (R-np)"; (R-np) is by definition a
no-peak-resource class (it is reduced by RL, IN, UC3 to (H-4)).
PJ-1 (J1.11 under option (b)).  GEN needs the N_T weights algebraically independent over k_0(other weights): true under option (a) (all c_l
transcendental, the goal's Martin-type setting); under option (b) (c_1 = 1) J1.11 holds for patterns with carrier 1 notin N_T (X1-ref W2).
C.6 Peak conversion (SKETCH, label honest).  Further gaps: (i) a non-robust frozen peak (margin ~beta_*) lies outside (FC) as refereed (only
robust peaks frozen as peaks); Lemma J2.1(e)'s margin hypotheses must be re-checked; (ii) the peak-error bound e_d <= t/(lambda_d mu_d) with
mu_d ~ beta_* (H1 lists it) and the screening bounds; (iii) in a (U)-block the cone is unchanged (Delta'_m = 0 kills the peak trace) and Lemma K
is continuous across the crossing (contribution Phi_d^2 to a^2 moves from k^2 R^2 to sigma) -- plausible, unproved.
C.7 Section 4.7 (table row 16, "PROVED (characterization)") is HEURISTIC: the Farkas representation is for one certificate at a smooth point;
the obstruction concerns all near-certificates at once (closed convex hull of their functionals), at singular points the tangent cone is
needed, and Lemma 2.2's delta(eps, r) is not uniform in the base point (J1.11's uniformity used compactness of Lambda).
Numerics remark.  H1's coarse puiseux_toy fits (1.49, 1.43 for the cone) are resolution artifacts (D(m) saturates at the 3.7e-4 sampling
scale); the reported 1.15/1.06 come from puiseux_toyA_fine.  Illustrations only.

## D. Referee additions (all PROVED modulo the same chain)
D.1 LEMMA PC (piece scaling).  Let m be a (U)-block and A a set of active ratios of m such that every tiny polynomial P (tiny minor or tiny
cofactor polynomial of Gamma^#(kappa, a)) satisfies A ∩ var(P) = {} or var(P) ∩ r^{(m)} ⊂ A, where var(P) is the set of ratio variables on which P
depends.  Then multiplying the ratios in A by any s > 0 preserves Z_kappa.  Every union of pieces G ∩ m (G any pinned group) and free ratios of
m is such a set.
Proof.  In a (U)-block r^{(m)} occurs only in the row (X3)_m, which has no constant entry ((X5) removes Delta'_m); hence every minor is
homogeneous of degree 0 or 1 in r^{(m)} and every cofactor polynomial is homogeneous in r^{(m)} (X1-ref D1), as identities in all ratio
variables (other blocks' ratios are parameters): P(s r^{(m)}, r') = s^{e_m(P)} P(r^{(m)}, r').  If A ∩ var(P) = {}, scaling A leaves P unchanged.
Otherwise P does not depend on r^{(m)} \ A, so scaling A has the same effect on P as scaling all of r^{(m)}: P is multiplied by s^{e_m(P)}.
For pieces: var(P) ⊂ G for every tiny P meeting a pinned group G (connected component of the linking graph), and free ratios lie in no
var(P).  QED
Also: with the other blocks' ratios frozen, every tiny MINOR meeting G ∩ m is linear in r^{G ∩ m}, so Lemma TG holds for pieces; in SHIFTED
blocks every tiny minor containing no (X4^0) row of the block is AFFINE in r^{(m)} ((X3)_m has entries 1 at Delta'_m and -r_l at gamma_l, and is
the only row containing r^{(m)}; U1-ref's (X4) in (KN)-blocks contains no ratio), so minors-only groups avoiding (X4^0) rows have affine zero
sets and exact tangent displacements there.

D.2 PROPOSITION MA' (frozen-value cancellation in every (U)-block, thick-type peaks included).  Let m be a (U)-block at a stage carrying a
near-certificate y of size eps <= eps_*.  Then
   sum over all thick-type coarse carriers k of m (rows and peaks) of rho_k u_k(xhat_1)
      = -(kappa_m/kappa_y) sum over non-thick kind-(iv) rows l of m of (rt_l eps_l sigma_l)(coef_l sigma_l) + O(Design^4 (eps + eta') + Design^2 D^2 b^2).
Proof.  From y_l = eps_l coef_l + eps_l zeta_m lambda_l d kappa/d zeta(l): zeta_m (1 - Xt_m) = sum_{rows l of m} rt_l eps_l coef_l with |Xt_m| <= C b^2 D^2
(route V).  Thick rows: rt_l eps_l coef_l = kappa_y rho_l u_l(xhat_1)/kappa_m + O(eps Design^2 + Design^2 eta') (Lemma AL, P-MA); kind (i): O(eps
Design^2); kind (ii): no near-certificate.  If m has a private peak resource, |zeta_m| <= (4/3) eps Design (R-PK) and no peak is thick-type (J1-ref
B.2): this is MA.  If not, every peak is thick-type and coef_c = -zeta_m lambda_c vs_c (1 - X_m) = kappa_y rho_c + O(eps Design^2) (Lemma NP), so
r_m := rho_c vs_c/lambda_c is common to the peaks up to O(eps Design^2/u) and zeta_m = -kappa_y r_m/(1 - X_m) + O(...).  Euler's identity (K2.8)
kappa_m = sum_k (d kappa_m/d zeta(k)) zeta(k) = (1 - X_m) sum_{c in P} lambda_c |u_c(xhat_1)| + O(b^2 D^2) gives sum_{c in P} rho_c u_c(xhat_1) =
r_m sum_P lambda_c|u_c| = r_m kappa_m/(1 - X_m) + O(...) = -(kappa_m/kappa_y) zeta_m + O(...).  Substitute and multiply by kappa_m/kappa_y.  QED
Consequences.  The stable-exact relation holds stage-wise in EVERY (U)-block (peaks included when there is no peak resource); without a peak
resource the near-certificates sit on the codimension-one resonance sum_{thick-type k of m} rho_k u_k(zhat) ~ 0; in (U+) the thick ROWS carry
the robustly negative value -sum_P rho_c u_c (anti-aligned rows dominate).

D.3 LEMMA SLP (status-constrained target LP).  Fix a block m at a stage carrying near-certificates.  OBJECTS E in M: the movable rows of m
with robust or near-threshold status and, if m is a (U)-block, the pieces G ∩ m; assume every object consists of thick-type and kind-(i) rows.
Put Xi_E := sum_{thick l in E} rho_l u_l(xhat_1), R_E^2 := m^2 sum_{l in E} rt_l^2, N := the protected rows of m (near-threshold actives incl.
(FC)-frozen weak peaks, D2/KN-pushed rows; in (T)-blocks the carriers of N(m) with the Puiseux statuses), kappa'_m := d log K(sigma, R^2)/d R^2
(in (0, C D^C], common to the block by Lemma K), a_d(E) := 1[d in E] + 2 kappa'_m R_E^2 (d in N), and
      V_LP := max{ -Xi . delta : a_d . delta <= 0 for d in N, ||delta||_inf <= 1 }.
(a) If V_LP >= c_LP := u^3/Design^{C_L}, Step A is realized with targets rt'_l := (1 + h delta_{E(l)}) rt_l, h := 8 nu_1 (||b|| + x)/(c_* c_LP).
(b) V_LP = min{ ||Xi + A^T lambda||_1 : lambda >= 0 }, (A^T lambda)_E = lambda_E + 2 kappa'_m R_E^2 Lambda, lambda_E := sum_{d in N ∩ E} lambda_d, Lambda :=
sum_{d in N} lambda_d.  Hence at a stage NOT realized by (a) there is lambda >= 0 with
      Xi_E = -(lambda_E + 2 kappa'_m Lambda R_E^2) + err_E,      sum_E |err_E| < c_LP.                         (*)
Proof.  (a) Z_kappa is preserved (movable rows enter no tiny polynomial; pieces by Lemma PC).  Pairing: <kappa y, rt' - rt> = h kappa_m sum_E
delta_E zeta^E(y), and zeta^E(y) = kappa_y Xi_E/kappa_m + O(Design^3(eps + eta') + D^2 b^2) (Lemma AL; kind (i) o(1)), so the pairing is h kappa_y
(Xi . delta) + O(h |M| Design^4 (eps + eta' + b^2)) >= h (c_*/nu_1) c_LP - small >= 4(||b|| + x) for every near-certificate (kappa_y <= -c_*/nu_1,
Xi . delta <= -c_LP).  Statuses: for d in N, log rho_d(rt') - log rho_d(rt) = h a_d . delta + O(h^2 Design^C) <= C h^2 Design^C, while every
protected status has slack >= eta'/(12 Design) at the targets ((U)-blocks: <= 1 - eta' at targets vs <= 1 - eta'/2 required; (T): F(r'') <=
1 - 3mu/4 vs 1 - mu/2 with mu >= eta'/(3 Design) by J1.11; D2/KN pushes likewise), and h^2 Design^C <= Design^C u^{-C} x^2 << eta'/Design.
Robust statuses and robust peaks move by O(h) << u.  Lemma TF' (with P-TF).  (b) LP duality for max{c . delta : A delta <= 0, -1 <= delta <= 1},
whose dual is min{1 . (mu+ + mu-) : A^T lambda + mu+ - mu- = c, lambda, mu+- >= 0} = min_{lambda >= 0} ||c - A^T lambda||_1, with c = -Xi.  QED
Readings (all PROVED from (*) together with MA/MA').
 (R-a) N = {} gives Xi_E ~ 0 for every object: impossible for a single thick row (|Xi| >= u^2/Design^C), so unprotected blocks have no movable
       thick row at residual stages (= Theorem IN + OUT(a)); objects without protected rows have Xi_E ~ -2 kappa'_m Lambda R_E^2 (anti-aligned and
       R^2-PROPORTIONAL; for single rows: common rho_l/u_l(xhat_1), = H1's anti-aligned proportional resonance, OUT(b)); objects containing
       protected rows have Xi_E <~ -2 kappa'_m Lambda R_E^2.
 (R-b) (U)-block WITH a peak resource: every row lies in an object (or is nearly neutral), so MA gives sum_E Xi_E ~ 0 (no kind (iv)); summing (*)
       gives Lambda (1 + 2 kappa'_m R^2_M) ~ 0, hence Lambda ~ 0, lambda ~ 0 and EVERY object is balanced, Xi_E ~ 0 (H1's (H-3), now for pieces).
 (R-c) (U)-block WITHOUT a peak resource: MA' gives sum_E Xi_E ~ -sum_{peaks} rho_c u_c(xhat_1); summing (*): Lambda (1 + 2 kappa'_m R^2_M) ~ sum_P
       rho_c u_c.  sigma_m = -1 forces Lambda < 0, impossible (= Theorem RL); sigma_m = +1 and N = {} contradicts sum_P rho_c u_c robust (= RL+).
       So (H-4) in exact form: N != {}, Lambda ~ sum_P rho_c u_c/(1 + 2 kappa'_m R_M^2) > 0, Xi_E ~ -2 kappa'_m Lambda R_E^2 for objects without
       protected rows and Xi_E <~ -2 kappa'_m Lambda R_E^2 for the others.
 (R-d) Extension: objects may also be unit tangent directions Delta of the affine zero sets of minors-only pinned groups (D.1), in shifted
       blocks too, with a_d(Delta) := 1[d in G] Delta_d/rt_d + 2 kappa'_m m^2 sum_{l in G} rt_l Delta_l and Xi(Delta) := kappa_m sum_{thick l in G} eps_l rho_l
       Delta_l (same proof; displacements exact on the affine zero set).
 Not covered by the LP: objects containing non-thick kind-(iv) rows (certificate-dependent coefficients; a minimax version over the convex
 hull of the near-certificate functionals would be needed), groups with nonlinear tiny polynomials ((X4^0)-minors, cofactor polynomials),
 thick-type peaks of shifted blocks.

## E. The residual after H1 and this report (necessary condition; PROVED mod chain)
A main stage L >= l_f (clean w, class a) is NOT realized only if Step A carries near-certificates (normal form J1.3) and:
 (H-1) nothing of type (R-T): it is empty (Cor 2.4, via J1.11);
 (H-2) no movable thick-type row is aligned or nearly neutral (Theorem IN, with P-IN);
 (H-3') every (U)-block WITH a private peak resource has no movable thick-type row of robust/near-threshold status, and every object (in
       particular every piece G ∩ m, internal or not) is balanced, Xi_E ~ 0 (Lemma SLP (R-b); objects with non-thick kind-(iv) rows: only
       H1's weaker statement, "zeta^E not robustly one-signed");
 (H-4') every (U)-block WITHOUT one has aligned peaks (sigma_m = +1), is protected, its frozen value including peaks vanishes (MA'), and the
       exact R^2-proportional resonance (R-c) holds; every movable row of robust/near-threshold status is anti-aligned thick-type or an
       active free kind-(iv) row with rt eps sigma > 0 (P-KC);
 (H-5') in every shifted block the movable objects (and the affine tangent directions of minors-only pinned groups, (R-d)) satisfy (*): robust
       anti-aligned movable rows share rho_l/u_l(xhat_1), near-threshold movable rows have |rho/u| at least that value, no aligned or kind-(i)
       movable row of robust/near-threshold status exists, and the block is protected;
 (H-6') the remaining pinned thick-type rows of shifted blocks lie in groups whose tiny polynomials are nonlinear ((X4^0)-minors or cofactor
       polynomials) or whose LP (R-d) is infeasible, or are thick-type peaks of shifted blocks without peak resource;
 (H-7) J1's (J-a), (J-b) fail (frozen far windows, no private two-sided design-depth resource, tiny spreads);
OR J1-ref's (R1) (no thick-type carrier; task H2).
Every item is a codimension >= 1 coincidence among f's stage data (proportional resonances, balanced pieces, vanishing frozen values) or a
persistent alignment pattern; whether such coincidences can persist at ALL large main stages for some f is OPEN.  The "Persistence"
paragraph of H1 8 is correct under its explicit stabilization hypothesis (then the relations become exact identities at f) and does not
show persistence.  No non-recoverable mate is indicated.

## F. Numerics (sanity only; r13/H1_ref_work/)
 N1 np_rl_toy2.py, np_rl_toy3.py (.out): J1-ref's consistent one-block toy with a THICK-TYPE peak (three private TS coordinates, |rho_c| = 0.1,
    aligned or anti-aligned) and NO peak resource, tuned to the no-peak-resource resonance.  sgn zeta(y; rc) = sgn(rho_c vs_c) in 26/26 runs
    (|zeta| ~ 0.088); after an obstruction (phi_y = 1e-3, min move 1.0e-2..4.9e-1) whole-block rescaling by 1 + sigma_m delta gives phi_y = -3e-3
    and min move 6.7e-4..7.1e-4 (26/26), the opposite direction phi_y = +5e-3 and no relief (26/26).  (The toy's peak TS columns have efficiency
    ~3e-3, so coef_c/(kappa_y rho_c) = 0.34-0.38: constants are not separated; only signs are meaningful.)
 N2 peakderiv.py: 397 random blocks with >= 2 peaks: d kappa_m/d|zeta(c)| is the same for all peaks to 1e-7 (route V: kappa = sum_P |zeta(c)|).
 N3 ma_peak_check.py: the near-certificate (argmin of the smallest singular value) sits at the root of rho_0 u_0 + rho_1 u_1 + rho_c u_c (zhat)
    (extended frozen value <= 4e-4 while the rows-only value is +-0.53..0.70), 10/10; kappa = Phi_c |u_c(zhat)| to all digits.
 N4 slp_check.py: LP duality of Lemma SLP (primal = dual to 9e-16, 300 instances); exact (*) gives V_LP = 0.
 [np_rl_toy.py/.out and np_debug*.py are a superseded first attempt: with |rho_c| = 0.5 the no-peak-resource resonance requires
  |Phi0| ~ 1.7 kappa, which forces carriers 0, 1 to become peaks, so no near-certificate exists there (sv_min ~ 1); np_debug2/3 locate the
  parameter range (|rho_c| = 0.1, peak deep scale 3, Phi_01 = 1) used by np_rl_toy2/3.]
 H1's own scripts (align_toy, complement_toy, rescale_toy, puiseux_toy*) were inspected; outputs match the notes (the coarse puiseux fits are
 resolution-limited; the fine run gives the reported 1.15/1.06).

## G. Most valuable idea; what remains open
Most valuable idea (H1's, it survives refereeing): the ALIGNMENT CALCULUS.  By J1.6(a), every near-certificate pairs with a target
displacement of a thick-type row l through the f-datum rho_l u_l(zhat) with ONE sign for all certificates (Lemma AL); with Lemma TF' this turns
target freedom into levers whose admissibility is pure status bookkeeping (inward moves always admissible; outward moves need room or an
R^2-neutral exchange; (U)-block pieces scale exactly).  The referee's Lemma SLP packages all of H1's levers as feasible points of one LP whose
Gordan dual is an explicit R^2-proportional anti-aligned resonance, and Proposition MA' shows that every (U)-block, with or without peak
resource, satisfies the stage-wise stable-exact relation (thick-type peaks included).  J1.11 (first-order Puiseux margin via Whitney (a) +
frontier condition + GEN) is a clean, fully proved technical result: (R-T) is empty.
OPEN (precise): (1) whether (H-1)-(H-7) [= (H-3'), (H-4'), (H-5'), (H-6'), (H-7)] can hold at all large main stages for some f; (2) objects
containing non-thick kind-(iv) rows (certificate-dependent signs; minimax version of SLP); (3) pinned groups with nonlinear tiny polynomials
((X4^0)-minors, cofactor polynomials) and thick-type peaks of shifted blocks ((H-6')); (4) the peak conversion of anti-aligned near-threshold
rows (SKETCH, C.6); (5) the (KN)-block lever bookkeeping (P-KN, inherited SKETCH); (6) (R1) (task H2); (7) the once-refereed links of the chain,
J1.13's inspection, and (FC)/J2.  (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the
Martin-type p: OPEN.  No counterexample is claimed, and nothing found here suggests one.
