# J1 referee notes (Round 12): proofs of the verdicts, the fixes, and two new lemmas (R-PK, R-PB) for r12/J1_notes.md

Setting and notation of r12/J1_notes.md 1: design T_fin^{K2} (K2 6.1) with K2-ref K-1..K-8 and J2's frozen convention (FC); N >= 1; f in S_{p_N*}
with forced data f = a + L^*w, q*(a) = ||a||_1 + nu = 1, e = U^*a/nu, zhat = z + Ue, diagonal base U k_s = mu_s e_s; g in C(f); rho in (0,1); main stage
L >= l_f, clean sub-window w, class a; b, u, T = T_lo(w), eta', x = C Design(L) eta', W, rho_0 = C_2 W^2, D = D(L), x'_max.  Sys-A rows l in Lambda_A,
Ft_l = val_l - rt_l kappa_{m(l)}; near-certificate y (unit, y^T g >= -eps for every generator g); phi_y = y^T Ft(R_1); zeta_m(y; rt) := sum_{l in m}
y_l rt_l; Psi = Psi^A_y = sum_l y_l eps_l u_l - sum_m zeta_m K_m; coef_k its coefficient on u_k; thick-type carrier k: thick private p in S_k ∩ [1, D],
rho_k := a_p/v_k(p); K_0 := thick-type tuned carriers.  Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = modulo the refereed chain
cited by K2.15 (X1/X2/Q1/Q2/K1/K2 with referee fixes; several links once-refereed) and, where stated, J2 (refereed separately).
Part files: r12/J1_ref_part1.md (J1.1-J1.5, numerics), part2 (J1.6-J1.9, P-TU, R-W), part3 (J1.10-J1.15, F-2, R-PB), part4 (gauge, 7.4,
residual).  Scripts/outputs: r12/J1_ref_work/.  This file supersedes the part files where they differ.

## A. Verdicts
| J1 claim (J1 label) | Verdict | Items |
|---|---|---|
| Lemma J1.1 deviation identity (PROVED) | correct | B.1 |
| Lemma J1.2 target form (PROVED) | identities correct; "Consequence" imprecise | P-1, R-PK |
| Lemma J1.3 normal form (PROVED) | correct | P-2 |
| Lemma J1.4 global rigidity (PROVED) | correct as an inequality with explicit errors | B.1 |
| Corollary J1.5 (PROVED) | inequality correct; stated conclusion FALSE | F-1 |
| Lemma J1.6 (a), (b) (PROVED) | correct | B.2 |
| Theorem J1.7 (PROVED mod chain) | correct after P-TU (realization ranges) | P-TU |
| Lemma J1.8 (PROVED) | correct | B.3 |
| Theorem J1.9 (PROVED) | correct; its numerical illustration used stale generators | N3 |
| Proposition J1.10 (PROVED; KN SKETCH) | (a), (c) correct ("iff" -> "if"); (b) wrong as worded, fixed | P-D2 |
| Proposition J1.11 (SKETCH) | unproved, plausible; label honest | B.4 |
| Proposition J1.12 (PROVED, conditional) | correct with precision | P-MT |
| Lemma J1.13 (PROVED, inspection) | correct as far as checked; one addition | B.5 |
| Lemma J1.14 (PROVED; KN SKETCH) | non-circularity GAP; fixed (rescale ALL targets) | F-2 |
| Theorem J1.15 (PROVED mod chain) | correct after F-2, P-TU, P-D2 (mod J1.13, J2, chain) | D |
| Gauge 7.3 (identity etc. PROVED; use SKETCH) | (a)-(c) correct; (d)'s "in particular" unjustified | P-G |
| Target freedom 7.4(a),(b) (PROVED) | correct (restatement; cone depends on targets) | P-1 |
| Stable exact case 7.4(c) (PROVED) | correct under two unstated hypotheses | P-S, R-PB |
| Residual 8 (OPEN) | correct as necessary condition after corrections | E |
| (LSC-trunc)_N for every f; density for p_N, p | OPEN | G |

## B. Re-derivations (correct claims)
B.1 J1.1-J1.4.  <U^*Dev_u, e> = 0 and u(zhat) = kappa_u + Dev_u(z) since a(zhat) = ||a||_1 + nu = 1; first-order actions are K2.4 with D_u = Dev_u
on F (off F a bank has no common-mode term because e_s = 0).  J1.3: Dev_Psi = kappa Theta + E by definition; the raise at s in S_1 acts by eff_s
kappa Theta(s) z_s >= -eps with kappa < 0, so Theta(s) z_s <= eps Design/|kappa|; Psi(zhat_1) = phi_y gives 1 + Theta(z) = (phi_y - E(z))/kappa.
J1.4: a(zhat') <= ||a||_1 + ||U^*a|| = 1, Theta(zhat') = Theta(z) + sum_{S_1} mu_s^2 Theta(s) a'_s/nu'.  P-2: on S_0, Psi(s) is the fine part (not 0).
B.2 J1.6.  (a) K2.16(3) holds for EVERY near-certificate of size <= eps_* (phi_y enters only through |phi_y| <= |Lambda_A|^{1/2} max(x, ||b||)); the
TS generator at a thick private p is two-sided, so |coef_k v_k(p) - kappa_y a_p| <= eps Design and |coef_k - kappa_y rho_k| <= eps Design^2,
|kappa_y rho_k| >= c_* u/(2 nu_1); valid for peaks too.  Corollary (PROVED): in a block with a private two-sided peak resource no coarse peak is
thick-type at a stage carrying a near-certificate (R-PK makes coef_c = -zeta_m lambda_c (1 - X_m) tiny).  (b) signs: coef_k v_k(j)(tau - z_j) =
kappa_y |rho_k| |v_k(j)| (1 - tau z_j) + O(eps Design^2 |v_k(j)|) < 0; admissibility: for data-carrying k a helpful j is a data-sign contact (the
placement is a V1 pull) or anti-data-sign support with |a_j| <= x'' (lowered, then aligned support); free or anti-sign far contacts of a
data-carrying carrier cannot occur (they force c_k = 0); peaks: K1 2.2's repaired peak pull.
B.3 J1.8, J1.9.  Brouwer on {||t|| <= W} x Box with the joint minimal-norm selection; separation from (W/2)Q + Box (support function (W/2)max(0,
max_g(-y^T g)) + (1/2) sum_B |y_l| beta_l).  J1.9: |y_k| >= c_* u/(8 nu_1) (dkappa/dzeta(k) = rho_k M X_m/C <= C b^2 D^2 in route V, (FC) for near-
threshold k), so phi_y > ||b|| + rho_0 >= |phi_y| + rho_0.
B.4 J1.11.  F is Lipschitz on the compact region, so mu_kappa(h) <= Lip h (exponent >= 1); J1.11 asserts exponent 1.  GEN + Whitney stratification
gives regularity at every point of Z ∩ {F = 1}; the missing step is a uniform decrease along curves approaching lower strata (a genuine
semialgebraic uniformity lemma).  Unproved.
B.5 J1.13.  Uses of ratios/values re-checked: Gamma^#(kappa, a) involves only ACTIVE ratios, sigma_rob and peak traces (X1 2.2(iv)); inactive
carriers have gamma_l = 0 (X1 Lemma EC), so V does not see their values; statuses via Lemma K; true shift sum r^#_l gamma_l = cone shift when
data are projected at r^# (U1 4.6); Lemma H at r^# (tiny minors involve pinned ratios only and vanish; robust >= u/4); (U)-block minors homogeneous
(cert0 3.4 D1); Sys-DC targets = companion values; Lemma PM.  ADDITION: in SHIFTED blocks an inactive carrier switches by Delta'' w(l)
(cert0 3.5), so its value enters H_m and the kind of l; a band changes these by O(Design^C beta_*), inside the curvature slack and kind [2].

## C. Findings and fixes
F-1 (Corollary J1.5; the stated conclusion is FALSE).  The inequality phi_y <= |kappa| Bound_{J1.4}(R') + sum_m zeta_m(kappa_m(R') - kappa_m(R_1)) +
2 eta_K (1 + ||U||) is correct, but it does not give "no companion that keeps the one-sided signs realizes the targets ... larger moves, degree
arguments, two-sided levers cannot do it":
 (i) its error terms are not small: 2 eta_K (1 + ||U||) = 4 eps Design (1 + ||U||) sum_m ||K_m||_1 with eps up to 4u^3 Design^{-C_A} >> ||b|| >= |phi_y|;
     even sharpened (eta_K ||zhat' - zhat_1||_inf, Bound at moves of size W) the error is ~ Design eps W ~ Design (rho_0 + ||b||) (K2.9(b));
 (ii) Bound_{J1.4}(R') contains the Deep term E(j)(z'_j - z_j), which is exactly the action of a far placement; J1.7 itself shows that a far
     placement (keeping every S_1 sign) makes Step A A-regular for the same targets;
 (iii) two-sided coordinates keep residual actions <= eps Design per unit, so moves of size ~ phi_y/(eps Design) are not excluded.
Numerics N2 (ref_j15_placement_B.out; consistent generators, a genuinely obstructed toy): minimal move 31-175 before, 2.8e-3 (v = 1e-2) resp.
6.6e-4 (v = 3e-3) after a pull at a helpful far coordinate of a thick-type carrier, all S_th signs kept; the frozen functional changes by exactly the
Deep term.  Correct replacement (PROVED): a row R' keeping the S_1 signs and realizing the targets must have first-order E-action (on S_0 ∪ S_2,
on Deep, and through <U^*E, e' - e>) >= phi_y - (second-order and eta_K terms): a LOCALIZATION of the obstruction (two-sided moves of size
>= c phi_y/(eps Design D), far coordinates, or a change of the direction of U^*a), not an impossibility.  J1 0(1)'s meta-claim must be withdrawn.

F-2 (Lemma J1.14 / Theorem J1.15 non-circularity; GAP; FIX PROVED).  J1.14 rescales the ACTIVE targets of a (U)-block (X1 2.1(U)), and J1.15 bounds
the change of phi_y by kappa_m (1 - s_m) zeta_m(r') using |zeta_m| <= 2 eps Design.  The peak resource controls the FULL sum zeta_m(y; rt) (all rows
of block m; Lemma R-PK), not the active partial sum.  In (J-c) the banded carrier k is a robust HOLD with |y_k| >= c_* u/(8 nu_1) and robust rt_k, so
zeta_act = -y_k rt_k + O(eps Design) is robust; restoring the active statuses after the band's R^2 drift needs 1 - s ~ (dK/dR^2/K) 2 m^2 |r_k| beta/kappa,
so phi_y moves by ~ (dK/dR^2/K) 2 m^2 r_k^2 beta |y_k| against the band's gain beta |y_k|/2; the ratio is 4 m^2 r_k^2 (dK/dR^2)/K = 2 rho_k^2 Phi_k^2/(K(a -
K R^2)) (Lemma K), which ranges over 0.01 ... 14 for admissible data (N4, ref_noncirc.out).  The same occurs in (J-d) when the block also contains a
thick-type robust hold, and for enlarged D2 pushes.
FIX.  Rescale ALL targets of block m by one s_m (active ratios, holds, D2/KN-pushed targets; KN-1 zeros unchanged), s_m := the largest s <= 1 - C Lip
eta' at which every protected status of the block (actives <= 1 - eta'/2, D2-pushed <= 1 - c eta'/2) holds at the realized values.  Proof: (a)
Z_kappa preserved (minors homogeneous of degree 0/1 in the active part of r^{(m)}), robust minors scale by >= s^n >= 1/2; (b) Lemma K with R^2 the
full Omega sum: rho_d(s rt) = m s|rt_d| K(sigma, s^2 R^2)/Phi_d <= s rho_d(rt) for every carrier d, every rho_d strictly increasing in s (rt_d != 0), so
s_m is continuous in the realized values and 1 - s_m <= C(Lip eta' + D^C sum_l (|r_l| beta_l/kappa_m + beta_l^2/kappa_m^2)); inactive values are used
only through statuses (B.5); (c) for a near-certificate at rt(s) = s rt(1) on block m, |zeta_m(y; rt(1))| <= (8/3) eps Design (R-PK, s >= 1/2) and
phi_y(s) = phi_y(1) + kappa_m (1 - s) zeta_m(y; rt(1)), a change <= 3 kappa_m (1 - s) eps Design; (d) the coupled Brouwer argument needs W >=
Design^{C_A} u^{-3} sup_s ||b(s)||, ||b(s)|| <= ||b(1)|| + kappa_m (1 - s)||rt^{(m)}||; beta_* = 16 nu_1 (||b|| + 2 C_2 W(beta_*)^2)/(c_* u) has a solution near
16 nu_1 ||b||/(c_* u) since C_2 Design^{2C} u^{-7} beta << 1; continuity of the selection jointly in (s, right-hand side) from uniform Hoffman bounds.

P-TU (realization ranges; inherited GAP in K2.9(c) and K1 Lemma K1.6(A), amplified in J1.7; FIX PROVED).  Every point of the Brouwer domain
{t >= 0, ||t|| <= W} must be admissible.  A pre-placed TU lever (pull + compensating base bank; K1 2.1(b), K2-ref K-1) can lower eps_l val_l only by
the pull's shift D_p = (1 + eps_l z_1(j_p)) v_l(j_p), and K1-ref R-6 places pulls at the SMALLEST pullable depth v >= x, so D_p may be ~ x/2 << W =
Design^{C_A} u^{-3} max(x, ||b||); in J1.7, W' ~ Design^{C_A} u^{-3} x'_max >> every D_p.  FIX: choose x'' >= Design^{C_J} x/u and x_TU with
24 Design^{C_A} u^{-3} (|Lambda|^{1/2} x + 3x'') <= x_TU <= 2^{-6G(L)} x'_max; pre-place pulls in [x_TU, x'_max] (pullability and the (U)-class
re-defined on this window, as R-6 did; costs bounded by R-6's worst case); FW_k := {Design^{C_J} x/u <= |v_k(j)| <= x''}.  Then all radii are <=
x_TU/24 <= D_p/4; other two-sided generators have ranges >= u/2 or none.  Example: x'' = Design^{C_J+1} x/u, x_TU = Design^{C_A+C_J+2} u^{-4} x (both
windows have ratio >= 2^{6G(L)} because T <= (u/(4 Design))^{L^2 + 20}).

P-1 (J1.2).  For each y, ALL generator actions depend on the targets through zeta_m(y; rt) (K2.8(b); K1 2.4: (P4)/TS columns contain -h gtil,
gtil = g - (rt_l G_m)_l).  The set of near-certificates moves with the targets.
P-D2 (J1.10(b)).  Inactive blocks may contain D2-pushed carriers (margin c eta'); a band on a robust row moves their statuses by ~ Design^C eta'/u.
"Without protected statuses" must mean: no active near-threshold carrier and no D2/KN-pushed carrier; otherwise use the coupling (F-2).
P-MT (J1.12).  (X4^0) coefficients m^2 |r_l| K(sigma_rob, R_a^2) depend on r_k through R_a^2: (MT2) needs slack >= C(|gamma_k| + D^C |Delta'_m|)|delta_0|.
P-G (gauge (d)).  "Switching through K_0 exactly along rhot" does not imply Q(G^perp, G) = 0 (Q couples K_0 with other carriers and the base part):
Q = [[2,1],[1,2]], G = (1,0), switching s_0 G + (0,1) gives s_0^Gamma = s_0 + 1/2.  Use the Q-orthogonal coefficient.
P-S (7.4(c)).  "a = Phi_0 on the thick part of F" fails on thick TARGET coordinates unless the non-thick-type coefficients are negligible, and
per-block vanishing needs the block contribution sum_{l in m} y_l val_l to equal kappa_y Phi_0^{(m)}(zhat_1).  Needed: (H-pure) robust coefficients
only on thick-type non-peaks; (H-pk) a private two-sided peak resource in every block meeting K_0.  Under these the statement holds (via R-PB,
stage-wise; exact in the limit if K_0 and the rho_k stabilize).  Flatness re-derived: N_m(w_m + t rhot_m) = 1 + t Phi_0^{(m)}(xi)/A_m + O(t^2)
(<D w, D rhot> = (C/A) Phi_0^{(m)}(xi) by the block-threshold lemma), and p*(f + t Phi_0) <= max(q*(a), max_m N_m(w_m + t rhot_m)).
N3 (numerics).  J1's check_band builds the generator matrix at rt = rc and the right-hand side at displaced targets ("stale" generators).  With
consistent generators (ref_band_consistent.out): in J1's toy (private peak FR resource) a displacement along y destroys the certificate
(sv_min 1.6e-5 -> 9e-3..4e-2, zeta(y; rt) = -3.9e-3) and Step A needs no band (minimal move 2e-2..1e-1); orthogonal displacement keeps y but phi_y ~
1e-17.  Without the peak resource (variant B) the obstruction is genuine (29-175) and the band removes it (1.6e-4): J1.9 confirmed there.

## D. New results
LEMMA R-PK (peak-column constraint; PROVED).  If block m has a private two-sided peak resource (z-move or ZD composite at a design-depth coordinate
s private among coarse carriers to a coarse peak c of m), then every near-certificate y of size eps satisfies |zeta_m(y; rt)| <= eps/((1 - X_m)
lambda_c |v_c(s)|) <= (4/3) eps Design.  Proof: the move changes only u_c(xhat) (by v_c(s) dz; e unchanged, since a_s = 0 there is no common mode);
under (FC) dkappa_m/dzeta(c) = 1 - X_m >= 3/4 (U1 1.4(a)); so the column is -(1 - X_m) lambda_c v_c(s) rt^{(m)}.  QED  Consequently the block's
contribution to phi_y is kappa_m zeta_m(y; rc) + O(eps Design kappa_m) = sum_{l in m} y_l val_l(R_1) + O(...): a row quantity.

LEMMA R-PB (per-block target hyperplane; PROVED).  Let block m satisfy: (i) a private two-sided peak resource; (ii) every tuned carrier of m is
thick-type, privately tunable (kind (i) of K2.16), or of kind (iv) with rt_l eps_l sigma_l of sign opposite to S_m (or 0); (iii) K_0 ∩ m != {} and
|S_m| > tau_* := C eps_* Design(L)^3 nu_1/c_*, where S_m := sum_{l in K_0 ∩ m} eps_l rho_l rt_l.  Then Step A has no near-certificate of size <= eps_*,
hence is A-regular (K2.9(b)).
Proof.  For tuned l, y_l = eps_l coef_l + zeta_m lambda_l dkappa/dzeta(l), hence zeta_m (1 - Xt_m) = sum_{tuned l in m} rt_l eps_l coef_l, Xt_m <= 1/4.
On K_0 ∩ m, coef_l = kappa_y rho_l + O(eps Design^2) (J1.6(a)); on kind (i), |coef_l| <= eps Design^2 (K2.16(2a)); on kind (iv), rt_l eps_l coef_l =
(rt_l eps_l sigma_l)(coef_l sigma_l) with coef_l sigma_l >= -(eps Design + |kappa| theta_0) Design (K2.16(2c)), so these terms have the sign of
rt_l eps_l sigma_l up to O(eps Design^2 + theta_0 Design^2).  If S_m > tau_*: kappa_y S_m <= -(c_*/nu_1) tau_* = -C eps_* Design^3 and the other terms
are <= C' eps Design^2 |Lambda| max|rt| + theta_0-terms, so zeta_m <= -(C/2) eps Design^3 for C large (Design dominates |Lambda| and the f-constants
for L >= l_f), against R-PK.  S_m < -tau_* is symmetric.  QED
NECESSARY CONDITION (contrapositive; PROVED).  At every stage carrying a near-certificate, every block with (i)-(ii) has |S_m| <= tau_*.  Since
eps_l rho_l rc_l = rho_l u_l(zhat_1)/kappa_m,
      |Phi_0^{(m)}(zhat_1)| <= kappa_m (tau_* + C Design max_{l in K_0 ∩ m} |rt_l - rc_l|),     Phi_0^{(m)} := sum_{l in K_0 ∩ m} rho_l u_l:
the per-block frozen value nearly vanishes at EVERY residual stage; with K2.16(4) this is the stage-wise form of the stable exact case.
Relation: with h_l = eps_l rho_l/nu_1, S_m = nu_1 h^T rt^{(m)}: R-PB is a per-block, tiny-threshold form of K2.17(f)'s bordered scalar (h_c = 0), and
its kind-(iv) clause complements K2.17(g).  N3 is an instance (displacing targets along y gives S_m != 0).

REMARK R-W (the A-regularity radius is a window quantity; PROVED modulo P-TU).  K2.9, J1.7-J1.9 use W only through admissibility (W <= x_TU/24),
cost C_f Design^C W log(1/W) = o(u^2 T^2), moves << u, and rho_0 = C_2 W^2.  Any W in [Design^{C_A} u^{-3} max(x, ||b||), min(x_TU/24, u^2 T^2/(C_f
Design^C log^2(1/T)))] works, and non-A-regularity then gives near-certificates of size < 2(||b|| + C_2 W^2)/W: obstructions are near-exact when the
pulls of the stage sit high (trade-off: a higher x_TU enlarges the (U)-class).

OBSERVATION R-G (structure of the residual; PROVED from K2 4.1(d), K2.16(4), K2.17(b), (e)).  (R1) at a stage forces |a_s| <= 2b(w) for every s in
F ∩ (s_max(L), D(L)] (a thick s there would lie in U_L, beyond the targets, hence in a coarse signature set, making its carrier thick-type; off U_L
it would be an anchor).  (R0) forces, for every thick-type carrier, all thick private coordinates in S_k ∩ [1, D(L)] proportional to v_k up to the
tiny spread of J1.6(a).  Both are strong non-generic conditions on f.

## E. Theorem J1.15 as accepted, and the residual
THEOREM J1.15' (PROVED modulo the chain, J1.13's inspection and J2).  At a stage (L, w, a), with the P-TU windows, Step A is realized if there is no
near-certificate of size <= eps_*, or some thick-type carrier k satisfies: (J-a) a helpful coordinate in FW_k; (J-b) K2.17(c)-(e); (J-c) k zero-data
strict non-peak of tiny status in a (U)- or (KN)-block [(KN): SKETCH] (no peak resource needed: J1.10(a)), or of robust status in a (U)-block or an
inactive block having a private two-sided peak resource (coupling F-2; P-D2); (J-d) k active with a FREE ratio in a (U)-block with a private
two-sided peak resource (coupling F-2); (J-e) k KN-1 in a (T)-block with mu_kappa(eta'/3) >= C D^C m^2 (beta_*/kappa)^2; (J-f) k active in a shifted
block under (MT1)-(MT3) (with P-MT) and delta_0 >= beta_*/kappa_m, or free with no R^2-sensitive protected status; or (J-g) some block satisfies
Lemma R-PB's (i)-(iii).  Then (with J2's Theorem J2.1 for Step 0) (LSC-trunc)_N holds at (f, g, rho) if this happens at infinitely many main stages.
RESIDUAL (OPEN; necessary condition for not being covered).  At all but finitely many main stages, at every clean sub-window and class, Step A
carries a near-certificate (normal form J1.3) and: (R0) every thick-type carrier is rigid (frozen far window on FW_k; no private two-sided
design-depth resource; tiny spreads; of type (R-pin), (R-T) [empty under J1.11], (R-Ts), (R-KN), (R-D2), (R-np) restricted to ROBUST-status
zero-data or free-active carriers, or (R-pk)), AND every block satisfying R-PB's (i)-(ii) has |S_m| <= tau_* (so |Phi_0^{(m)}(zhat_1)| <= kappa_m(tau_* + C
Design eta'')); or (R1) no thick-type carrier (then a is b(w)-thin on F ∩ (s_max(L), D(L)], R-G) and the certificates are of type (U*), with robust
coefficients on kind-(iv) carriers (unpulled on the TU window) and possibly on non-thick-type peaks of blocks without a private peak resource.

## F. Numerics (sanity only; r12/J1_ref_work/)
 rerun/: J1's check_part1, check_resonant2, check_band reproduced exactly.
 ref_band_consistent.py/.out (N3): stale vs consistent generators; variants A (peak resource) and B (none).
 ref_j15_placement.py, .out (J1's toy) and _B.out (variant B) (N2): far pull keeps S_th signs and realizes the same targets; frozen functional
   change = Deep term.
 ref_noncirc.py/.out (N4): F-2's ratio 2 rho_k^2 Phi_k^2/(K(a - K R^2)) between 0.01 and 14.3.

## G. Most valuable idea; what remains open
Most valuable idea (J1's, it survives refereeing): every near-certificate carries the SAME robust coefficient of FIXED sign, coef_k ~ kappa_y a_p/
v_k(p), on EVERY thick-type carrier (J1.6(a)); hence relieving one thick-type carrier -- a helpful far placement (J1.7), or a band on its row with
the block's targets rescaled uniformly (J1.9 + F-2) -- removes all Step-A obstructions at once.  The referee's complement (R-PK/R-PB): a private
peak resource forces zeta_m(y; rt) ~ 0, so residual stages force the per-block frozen values Phi_0^{(m)}(zhat_1) to nearly vanish.
OPEN: (1) the residual of E at all large main stages (R0 with the R-PB condition; R1); (2) J1.11 (uniform first-order Puiseux margin);
(3) (R-pin): a constrained Lojasiewicz step for pinned thick-type ratios; (4) the (KN)-lever coupling; (5) pure (U*) on target-supported,
b(w)-thin rows; (6) the once-refereed links of the chain, J2's refereeing, and the J1.13 inspection.  (LSC-trunc)_N for every f, density of
NA((c_0, p_N), l_2^2) for any N and of NA((c_0, p), l_2^2): OPEN.  No counterexample: every residual configuration is a near-resonance of the stage
data (codimension >= 1 relations among f's data and the targets), not a property of a mate.
