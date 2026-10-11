# J2 notes (Round 12): the joint Step-0 weak-peak push problem (H1*) -- bypassed.  Step 0's weak-peak pushes are dispensable.

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = proved here modulo the refereed chain that Theorem K2.15 already cites
(X1/X1-ref, X2/X2-ref, Q1/Q1-ref a,b/cert0-3, Q2/Q2-ref a, K1/K1-ref, K2/K2-ref; several links once-refereed, as recorded there).  Part
files: r12/J2_part1.md (formulation, audit), J2_part2.md (Lemma J2.1, Theorem J2.1, Corollaries J2.2, J2.3), J2_part3.md (direct route),
J2_part4.md (numerics); scripts and outputs r12/J2_work/.  This file supersedes the part files where they differ.

## 0. Bottom line
(1) BYPASS (Theorem J2.1, PROVED).  The weak-peak pushes (WP) of Step 0 (KN^tr Step 0 in (T)-blocks) can be deleted from the construction.
    What they provided -- a Lojasiewicz start point and a Step-A input row at which every active near-threshold carrier is a strict
    non-peak -- is supplied, without any push, by computing the block scalars with the FROZEN convention of K2-ref K-8 stated with the
    TARGET pattern (FC): only the robust peaks are frozen as peaks, every weak peak is frozen as a non-peak.  The frozen block system is
    smooth across the threshold crossings that Step A performs, satisfies Lemma K exactly, is within O(Design b) of the true one at the
    unpushed row, and coincides with the true one at the realized point (Lemma J2.1).  Hence Theorem K2.15 holds WITHOUT (H1*): (LSC-trunc)_N
    holds at (f, g, rho) as soon as, at infinitely many main stages, Step A -- with the active weak peaks frozen in Omega, after optional
    pre-pushes -- is A-regular ((H2^flat)).  (H1*) and (H2) together imply (H2^flat) (Corollary J2.2), so this strictly contains K2.15.
(2) RESIDUAL (Corollary J2.3, PROVED).  The class (W)/(W*) of K2 7.3 / K2-ref G is EMPTY as a separate obstruction.  If (H2^flat) fails at all
    large main stages, Step A carries a near-certificate with the structure of Theorem K2.16 at the unpushed row (K2.16 holds verbatim for
    the frozen map).  The only remaining hypothesis of the whole chain for (LSC-trunc)_N is Step A's A-regularity ((A*)/(U*), task J1).
(3) PRECISION to K2-ref K-8 (PROVED): literally read ("peak set frozen at f_1 + Pi"), K-8 freezes as peaks the active weak peaks of (U)- and
    (KN)-blocks, which Step 0 never pushes and which Step A moves below threshold; the frozen system would then be inconsistent at the
    realized point.  (FC) is the correct reading; it is needed for K2.15 itself.
(4) DIRECT ROUTE (Proposition J2.4, Lemma J2.5, PROVED; 3.3 SKETCH).  Threshold raisers (raise a robust peak / lower a strict non-peak:
    Lemma J2.0) push ALL weak peaks of a block at once with a private resource, so the joint push has no Sherman-Morrison feedback whenever
    each (T)-block has private own pushes or a private threshold raiser; for Delta'_m < 0 any robust peak with an off-F or thin near coordinate
    is one.  A direct proof of (H1*) at every row meets the K2.16 sign structure (3.3), i.e. is as hard as Step A -- which is why the bypass
    is the right move.
(5) PRECISION on data signs (PROVED): an active weak peak has eps_k = vs_k sgn(e_k - Delta'_m) (Part I lem:peakshift), not always
    -sgn(Delta''_m) vs_k as in K1-ref R-8 / K2-ref W-1 (fails when Delta'_m > 0 and e_k > Delta'_m).  No conclusion of K1-ref/K2-ref changes.
(6) (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) (any N) and of NA((c_0, p), l_2^2): OPEN, now reduced to Step A's
    A-regularity alone (see 7 for the combination with J1).  No counterexample; nothing found points to one.

| # | Result | Status | Section |
|---|---|---|---|
| 1 | Lemma J2.0 (first-order action on relative positions; threshold raisers; 1-homogeneity of theta) | PROVED | 1.2 |
| 2 | Data signs of weak peaks (precision to R-8/W-1) | PROVED | 1.3 |
| 3 | Audit: where the pushed row is used ((L1)-(L5)) | PROVED (inspection) | 1.4 |
| 4 | Lemma J2.1 (frozen block system: existence/uniqueness, regularity, consistency => truth, frozen Lemma K, near-consistent bounds) | PROVED | 2.1 |
| 5 | (FC) = K-8 with the target pattern (precision) | PROVED | 2.2 |
| 6 | Theorem J2.1 ((LSC-trunc)_N under (H2^flat) alone; Step 0 without (WP)) | PROVED (mod chain) | 2.3 |
| 7 | Corollary J2.2 ((H1*) and (H2) imply (H2^flat)) | PROVED | 2.4 |
| 8 | Corollary J2.3 (residual = (A*) ∪ (U*) at the unpushed row; (W*) empty) | PROVED | 2.5 |
| 9 | Proposition J2.4 (joint pushes by private resources and threshold raisers) | PROVED | 3.1 |
| 10 | Lemma J2.5 (sign structure; failures of the direct route only through (S)/(U)/(M) carriers) | PROVED | 3.2 |
| 11 | Step-0 Farkas certificates have the K2.16 structure | SKETCH | 3.3 |
| 12 | (H1*) at every row (directly) | OPEN (bypassed; as hard as Step A) | 3.3 |
| 13 | (LSC-trunc)_N for every f; density for p_N, p | OPEN (reduced to (H2^flat)) | 7 |

## 1. Formulation (details: J2_part1.md)
1.0 Setting.  Design T_fin^{K2} (K2 6.1, with K1's (D-K1), K1-ref R-6, R-8(ii), K2's (K2-a)-(K2-e)); N >= 1; f in S_{p_N*} with forced data
f = a + L^*w, F = supp a arbitrary; g in C(f); rho in (0,1); main stage L >= l_f, clean sub-window w, b = b(w), u = u(w), T = T_lo(w),
eta' = T^4/(L Design(L)).  Block m: zeta_k = lambda_k u_k(xhat), lambda_k = m Phi_k, A = |zeta|_m, theta = AM/C, nu_k = |zeta_k|/Phi_k^2,
rho_k = nu_k/theta; P = {rho >= 1}.  Threshold equation (Y2 Lemma T): theta is the unique zero of Psi(th) = A(th)^2 - B(th), A(th) := sum
(|zeta_k| - th Phi_k^2)_+, B(th) := sum Phi_k^2 min(th, nu_k)^2.  Formula-1 scalar (X1-ref K1): kappa(Omega) = A + (A^2 - S_Omega)/theta,
S_Omega = sum_Omega nu^2 Phi^2; ratios r_l = u_l(xhat)/kappa.  W(m) := active weak peaks (rho in [1, 1 + b]) of block m.
1.1 Step 0 of KN^tr = (C1), (C2) (off-F z-moves, always available) + (WP): every k in W(m), m a (T)-block, pushed to rho_k = 1 - b.  Only (WP)
can fail.  (H1*) (K2-ref E): admissible moves of total size <= Design^C b/u after which rho_k <= 1 - b for all k in W.
1.2 LEMMA J2.0.  In one block, d theta = [A sum_P d|zeta_j| - sum_Q nu_j d|zeta_j|]/(Phi'^2 (A + theta)), Phi'^2 := Phi_P^2, and d log rho_k =
d|zeta_k|/|zeta_k| - d theta/theta; theta is 1-homogeneous: sum_j (d theta/d|zeta_j|)|zeta_j| = theta.
Proof.  Implicit differentiation of Psi(theta; zeta) = 0: d Psi/d|zeta_j| = 2A (j in P), -2 nu_j (j in Q); d Psi/d th = -2(A + th) Phi_P^2 < 0.
Euler: sum_P |zeta_j| = A + theta Phi_P^2 and sum_Q nu_j |zeta_j| = A^2 - theta^2 Phi_P^2, so the numerator at d|zeta| = |zeta| is theta
Phi_P^2 (A + theta).  QED
Consequences.  (a) THRESHOLD RAISERS: raising a peak or lowering a strict non-peak raises theta and lowers every rho of the block by a common
factor.  Pushing all of W(m) from <= 1 + b to <= 1 - b by a robust peak p needs |d u_p| = 3b theta Phi'^2 (1 + a)/(a lambda_p) <= Design^C b/u^2
(a = A/theta >= u Phi_p^2 at a clean sub-window by the alpha-mass identity a = sum_P (rho - 1) Phi^2), while the ratios move by the common
factor of kappa_m with |d kappa_m|/kappa_m <= 6b/a <= Design^C b/u.  (b) OWN PUSH: lowering |zeta_k| at a peak k lowers rho_k
(d log rho_k = d|zeta_k| [1/|zeta_k| - a/(theta Phi'^2 (1 + a))], bracket > 0).  So (WP) is a first-order cone/inequality problem.
1.3 DATA SIGNS.  At a peak k (Part I lem:peakshift): varsigma_k omega_+(k) <= 0 <= varsigma_k omega_-(k), e_k := varsigma_k(omega_- - omega_+)(k)
>= 0.  With gamma_k = lambda_k (Domega(k) - Delta_m w(k)), Delta' = Delta M, w(k) = M vs_k: vs_k gamma_k = lambda_k (e_k - Delta'_m), so eps_k =
vs_k sgn(e_k - Delta'_m).  Robust peaks (Domega = 0 in the class cone): eps_p = -sgn(Delta'_m) vs_p.  [PROVED; precision to R-8/W-1.]
1.4 AUDIT (PROVED by inspection of the cited proofs).  The pushed row is used only in: (L1) the Lojasiewicz start (tiny minors <= (1 + Lip C_*)b
at r_1, F(r_1) <= 1 + C_* b; cert0 3.1 already notes the push-free alternative "C3"); (L2) Lemma R-kt/Lemma K for the ratio variables; (L3)
Step A's realization (smooth block scalars; small Euler share, K2.8, K2.16(3)); (L4) Lemma K2.13's list of moves; (L5) R-8(ii)'s enlarged (D1).
Classes (read at f^r), (P), the data (K1.A), Sys-DC (K2.6), Theorem UE^inf and E^{eng,RT,inf} do not use (WP).

## 2. The bypass (details: J2_part2.md)
### 2.1 LEMMA J2.1 (frozen block system).  PROVED.
Block m; Lambda_m its coarse carriers; a frozen pattern P_f ⊂ Lambda_m (nonempty, zeta != 0 on P_f), Q_f := Lambda_m \ P_f; fine carriers true:
  A_f(th) := sum_{P_f} (|zeta_k| - th Phi_k^2) + sum_{fine} (|zeta_k| - th Phi_k^2)_+,  B_f(th) := th^2 Phi_{P_f}^2 + sum_{Q_f} nu_k^2 Phi_k^2 + sum_{fine}
  Phi_k^2 min(th, nu_k)^2,  Psi_f := A_f^2 - B_f,  th_max := sup{A_f > 0}.
(a) Psi_f is strictly decreasing on (0, th_max) with Psi_f(th_max-) < 0; it has exactly one zero theta_f there iff Psi_f(0+) = (sum_{P_f ∪ fine}
    |zeta_k|)^2 - sum_{Q_f} nu^2 Phi^2 > 0.  A_f := A_f(theta_f) > 0.
(b) (theta_f, A_f) are 1-homogeneous, locally Lipschitz, C-infinity where the signs on P_f and the fine statuses are fixed; Lemma J2.0 holds
    with (P, Q) := (P_f ∪ fine peaks, Q_f ∪ fine non-peaks); |d Psi_f/d th| = 2(A_f + th) Phi'^2 >= 2(A_f + th) Phi_{P_f}^2; fine kinks Lipschitz
    with constant <= C sum_{fine} Phi^2.
(c) CONSISTENCY: if nu_k >= theta_f on P_f and nu_k <= theta_f on Q_f, then theta_f = theta and A_f = |zeta|_m.
(d) FROZEN LEMMA K: for Omega ⊂ Q_f, kappa_f := A_f + (A_f^2 - S_Omega)/theta_f, r_l := u_l/kappa_f, R^2 := m^2 sum_Omega r^2, a_f := A_f/theta_f,
    k_f := kappa_f/theta_f, sigma_f := (A_f^2 - S_Omega)/theta_f^2 = Phi'^2 + s_f (s_f := theta_f^{-2} sum over (Q_f \ Omega) ∪ fine non-peaks of
    nu^2 Phi^2): a_f^2 = sigma_f + k_f^2 R^2, k_f = a_f + sigma_f, R < 1, k_f = K(sigma_f, R^2), rho^f_l := nu_l/theta_f = m|r_l| K(sigma_f, R^2)/Phi_l;
    d kappa_f/d|zeta_l| = rho^f_l s_f/(Phi'^2 (1 + a_f)) (l in Omega), d kappa_f/d|zeta_p| = 1 - a_f s_f/(Phi'^2 (1 + a_f)) (p in P).
(e) NEAR-CONSISTENT ROWS: if the true peak set is P_f ∪ W' (W' ⊂ Q_f, rho in [1, 1 + b] on W'), rho <= 1 on Q_f \ W', 6b Phi_{W'}^2 <= Phi_{P_f}^2,
    2b Phi_{W'}^2 <= a, b <= 1, then Psi_f(0+) > 0, theta(1 - 3b Phi_{W'}^2/Phi_{P_f}^2) <= theta_f <= theta, |A_f - A| <= 4b theta Phi_{W'}^2/Phi_{P_f}^2,
    rho^f_k <= rho_k (1 + 6b Phi_{W'}^2/Phi_{P_f}^2), |kappa_f - kappa(Omega)| <= C b theta Phi_{W'}^2/Phi_{P_f}^2.
Proof.  (a) On (0, th_max) A_f > 0 has derivative <= -Phi_{P_f}^2 < 0 and B_f derivative >= 2 th Phi_{P_f}^2 > 0; at th_max A_f = 0, Psi_f = -B_f < 0;
limits at 0+ as stated (min(th, nu)^2 -> 0); intermediate value theorem.  (b) Implicit function theorem (d Psi_f/d th < 0); homogeneity of the
equations under (zeta, th, A) -> c(zeta, th, A).  (c) Under the hypothesis every frozen term equals the corresponding term of A(theta_f), B(theta_f),
so Psi(theta_f) = 0, theta_f = theta (Y2 Lemma T(c)) and A_f = A(theta) = |zeta|_m (Lemma T(b)).  (d) A_f^2 = B_f(theta_f) gives A_f^2 - S_Omega =
theta_f^2 sigma_f; nu_l Phi_l/theta_f = m|r_l| k_f gives S_Omega/theta_f^2 = k_f^2 R^2, so a_f^2 = sigma_f + k_f^2 R^2; k_f = a_f + sigma_f by definition;
a_f > k_f R and k_f > a_f give R < 1; eliminating a_f gives (1 - R^2)k^2 - 2 sigma k + sigma^2 - sigma = 0 whose admissible root is K (X1 Lemma K's
algebra).  Derivatives: differentiate A - A_f(th) = 0, A^2 - B_f(th) = 0 with fixed statuses: for l in Omega dth = -nu_l/(Phi'^2(A + th)), dA =
nu_l/(A + th), d kappa_f = (nu_l/(A + th))(sigma_f/Phi'^2 - 1); for p in P dth = A/(Phi'^2(A + th)), dA = th/(A + th), d kappa_f = 1 - a s_f/(Phi'^2(1+a)).
(e) A_f(theta) in [A - b theta Phi_{W'}^2, A], B_f(theta) in [B, B + 3b theta^2 Phi_{W'}^2], so -b theta Phi_{W'}^2 (2A + 3theta) <= Psi_f(theta) <= 0
and theta_f <= theta.  Psi_f(0+) >= 2A theta (Phi_{P_f}^2 - b Phi_{W'}^2) + theta^2 (Phi_{P_f}^2 - 3b Phi_{W'}^2) > 0 (true identities A = A(theta),
A^2 = B(theta)).  On [theta/2, theta]: A_f >= A/2, |Psi_f'| >= (A + theta) Phi_{P_f}^2, so Psi_f(theta/2) > 0 (6b Phi_{W'}^2 <= Phi_{P_f}^2), theta_f >
theta/2 and theta - theta_f <= |Psi_f(theta)|/((A + theta)Phi_{P_f}^2) <= 3b theta Phi_{W'}^2/Phi_{P_f}^2; the rest follows (A <= theta, A^2 - S_Omega <=
2 theta^2).  QED
### 2.2 (FC): the frozen convention with the TARGET pattern.  PROVED (precision to K2-ref K-8).
For Step A and for the Lojasiewicz start, every block is computed with P_f := P_rob (the coarse peaks with rho >= 1 + u at f^r; at a clean
sub-window coarse peaks have rho in [1, 1 + b] ∪ [1 + u, inf), all moves before the end of Step A are << u), every other coarse carrier --
every weak peak, active or inactive, of every block -- frozen as a non-peak, fine carriers true; Omega := all coarse non-P_rob carriers (route
V's Omega at the companion).  Reason: (FC) is the status pattern of the companion (Q1 CM^tr(b)), so Step A's targets make it consistent at the
realized point and Lemma J2.1(c) applies; K-8's literal "peak set frozen at f_1 + Pi" freezes the active weak peaks of (U)- and (KN)-blocks as
peaks (Step 0 pushes only (T)-blocks; Step A moves them to rho <= 1 - eta' resp. below the KN margin), and is then inconsistent.
### 2.3 THEOREM J2.1.  PROVED (modulo the chain of K2.15).
(H2^flat) at (L, w, a): there are admissible pre-pushes Pi_0 (any moves admissible in (H1*), possibly none, of size <= Design^C b/u in ratio
units) such that, with f^0 := the row after the deep raise, (C1), (C2), Pi_0 and (P), the Lojasiewicz/Puiseux steps 1-3 started at the
(FC)-ratio vector r_0 of f^0, and Step A's pre-placements Pi, Step A computed with (FC) is A-regular at f^0 + Pi (K2 5.2 with K-7's u-scaling).
STATEMENT.  Design T_fin^{K2}, N >= 1, f in S_{p_N*} (any F), g in C(f), rho in (0,1).  If (H2^flat) holds at infinitely many main stages (for
a clean sub-window and a class with >= n(w)/D_cl(w) scales), then (f, rho g) is in the closure of NA((c_0, p_N), l_2^2) along norm-attaining
rows with finite base support; in particular (LSC-trunc)_N holds at (f, g, rho).  If this holds for every (g, rho), f is in Rec(p_N).
PROOF.  (i) [Lojasiewicz start]  Every block of f^0 satisfies Lemma J2.1(e) with P_f = P_rob, b' := C Design(L) b in place of b (the moves
(C1), (C2), Pi_0, (P) shift relative positions by <= C Design b) and W' := the coarse peaks outside P_rob; the side conditions hold because
Phi_min(L)^2 >= 1/Design(L), a >= u Phi_min(L)^2 and b' << u/Design(L)^2; P_rob != {} (V1 Lemma D).  Rate objects are evaluated at f with the
formula-1 ratios r(f) (X1-ref K1); between f and f^0 values move by O(mu*_J) + C b + Design^C b/u and frozen-versus-formula-1 differs by
<= C Design b relatively (J2.1(e)); ratios are 0-homogeneous and Lipschitz with Design^C constants (as in K1-ref R-8, Q1-refa P-LIP; f-constants
absorbed for L >= l_f).  So |r_0 - r(f)| <= Design^C b/u, tiny minors and cofactor polynomials are <= (1 + Lip C_*) Design^C b/u at r_0, r_0 lies
in the W-fix region (1 - R^2 >= sigma_f/2 >= sigma_rob/2, J2.1(d)), and by Lemma F for the frozen system (sigma_f >= sigma_rob, R^2 >= R_a^2)
F(r_0) <= max_{N_T} rho^f_d(f^0) <= (1 + b')(1 + 6b' Design) <= 1 + Design^2 b.  With R-8(ii)'s enlarged (D1), (D2) (kept in T_fin^{K2}), KN^tr
Steps 1-3 give r'' in Z_kappa, |r'' - r_0| <= eta', robust minors >= u/2, F(r'') <= 1 - mu.
(ii) [realization]  K2.9(c) at f^0 + Pi for the (FC)-frozen map: it uses the generators' first-order actions (K2.4; K2.8(b) for kappa_f, C^{1,1}
by J2.1(b) with design constants: |d Psi_f/d th| >= 2 theta_f Phi_{P_rob}^2, |zeta_p| >= theta_f Phi_p^2 on P_rob), the remainder bound C_2||t||^2
(+ C c_{L+1}||t|| from fine status changes, as in K-8) and Brouwer -- no true status.  It yields frozen-exact targets: active frozen ratios r'',
KN-1/P-HOLD values 0, (U)-block targets s_m r'' kappa_f, D2/KN-pushed carriers at their pushed values; moves <= W << u; cost o(u^2 T^2).
(iii) [consistency]  At the solution: (T)-blocks: rho^f_d = m|r''_d| K(sigma_f, R_a(r'')^2)/Phi_d with sigma_f = Phi_{P_rob}^2 + s_f, s_f <= C c_{L+1}^2,
so rho^f_d <= (1 - mu)(1 + C D^C c_{L+1}^2) <= 1 - mu/2 (incl. the former weak peaks); (U)-blocks rho^f <= s_m(1 + Design^2 b + Lip eta') <= 1 - eta';
(KN)-blocks U1-ref Prop. KN(b) margins; held values 0; pushed carriers rho^f <= 1 - c eta'; robust non-peaks in [u/2, 1 - u/2]; P_rob rho^f >= 1 + u/2.
So (FC) is consistent in every block and J2.1(c) gives theta_f = theta, A_f = |zeta|_m: the frozen solution is the TRUE companion f^(1a) with
true ratios r'' on Z_kappa, true statuses and the Puiseux protection -- K1 Lemma K1.6(A)'s conclusions.
(iv) [rest]  Order: deep raise -> (C1), (C2) -> Pi_0 -> classes (read at f^r) -> (P) -> targets -> Pi -> Step A -> data -> s_1 -> N_w -> N'' ->
Sys-DC -> approximant.  K2.13's classification holds (fewer moves; Pi_0 << u).  Data (K1.A, banked coordinates as in K2 4.1(c)), Sys-DC (K2.6),
Theorem UE^inf (Lemma DC^inf), averaging (E^{eng,RT,inf}, K1-ref (E-d)) are K2.15's steps verbatim; none uses (WP) (1.4).  QED
### 2.4 COROLLARY J2.2.  (H1*) and (H2) at a stage imply (H2^flat) there (take Pi_0 := the (WP) moves; then f^0 = K2's f_1 after (P), the
Lojasiewicz start is r_1, and (FC) agrees with K-8 in the (T)-blocks).  So Theorem J2.1 contains Theorem K2.15.  PROVED.
### 2.5 COROLLARY J2.3 (residual).  PROVED.
If (H2^flat) fails at all large main stages (every clean sub-window, class and Pi_0, in particular Pi_0 = {}), K2.9(b) gives at each stage a
near-certificate for the (FC)-frozen Sys-A at f^0 + Pi, and Theorem K2.16 applies verbatim (its proof uses the identity (2.1) at the row, the
generators' actions, the Euler share Xt_m <= 1/4 -- for the frozen map d kappa_f/d|zeta_l| = rho^f_l s_f/(Phi'^2 (1 + a_f)) <= 2 Design(L) sum_{fine}
Phi^2 on Omega, J2.1(d) -- and the four kinds of tuned carriers after (P)).  Residual = (A*) ∪ (U*) at f^0 + Pi with (FC); (W)/(W*) is empty as
a separate class.  J1's Lemmas J1.1-J1.5 (r12/J1_part1.md) use only the row, the generators, K2.8(a) and K2.16, so they hold at f^0 + Pi too.
### 2.6 Remarks.  (1) Nothing is lost: in the pushed version Step A still had to move every former weak peak from rho = 1 - b to a floor status
<= 1 - mu, mu >= 8Mb ((D2)): the inward requirement was already part of (H2); (WP) only added a second cone condition at the scale b with its own
feedback (K2-ref W-1); after the merge that feedback lives in J_A = [I - gtil h^T | col_c] (K1 2.4), analyzed by K2.16, and Step A's resources
include the floating kappa / buffer-peak (threshold) levers that (WP) did not use.  (2) Keeping a weak peak as a peak (Y2 Lemma U' kind [3]) does
not help: kind [3] needs alpha(k) = 0 (exactly degenerate peaks) or strict non-peaks, i.e. an exact inward push, and route V's threshold
protection needs the active near-threshold carriers to be strict non-peaks at the companion anyway (X1-ref 8(b), Q1 CM^tr(b)).  PROVED.

## 3. The direct route (details: J2_part3.md)
3.1 PROPOSITION J2.4 (PROVED).  (H1*) holds -- own pushes <= 3b theta Phi_k/m, threshold raisers <= Design^C b/u^2 in value units and <= Design^C
b/u in ratio units -- if every (T)-block m with W(m) != {} has, for each k in W(m), a private own push ((P1) if e_k = Delta'_m; an off-F or thin
near coordinate when eps_k = -vs_k; a pullable far coordinate at depth in [3b theta Phi_k/m, x'_max] when eps_k = vs_k; (P3)), or has one private
threshold raiser (a robust peak with an off-F/thin near coordinate when Delta'_m < 0, with a pullable far coordinate when Delta'_m > 0, or with
(P3); or an active strict non-peak with rho >= u and a private resource lowering |u_l|), or a mixture.  Proof: private moves act at first order
only on their own value (K1 2.1(a)-(c); V1 Lemma B: cross effects <= C Design^2 (size)^2); by Lemma J2.0 own pushes lower their rho, a
threshold raiser lowers every rho of its block by a common factor and acts on no other block at first order; overshoot (rho <= 1 - 2b, theta
raised by 4b relatively) absorbs the second-order cross effects (<< b since b << u^C/Design^C); no (P4)/(P5) column, hence no Sherman-Morrison
denominator; admissibility as for K1's (P2) banks/pulls; robust objects move << u; rate objects by <= Design^C b/u (peak values do not enter them,
Q1-refb E7); costs o(u^2 T^2).  QED.  [Remark: K2-ref E's size bound must be read in ratio units for threshold raisers.]
3.2 LEMMA J2.5 (PROVED).  (a) Delta'_m < 0: every peak has eps = vs, so ONE robust peak with an off-F or thin near coordinate (or (P3)) is a
threshold raiser for the whole block; the direct route fails in such a block only if every robust peak is support-swallowed of type (S) and some
weak peak lacks a pull and (P3), and no strict non-peak helps.  (b) Delta'_m > 0: robust peaks' pulls raise theta (banks lower it); a weak
peak with e_k < Delta'_m pushes itself with its bank.  (c) Every failure of Proposition J2.4 involves only carriers of K1-ref R-10's types (S),
(U), (M).  Proof: 1.3 and the case analysis of 3.1.
3.3 (SKETCH) A Farkas certificate y >= 0 against (WP) defines Psi^0_y := sum_m sum_{j in m} c_j u_j, c_j := vs_j [y_j/|u_j| 1_W - Y_m (d theta_m/
d|zeta_j|) lambda_j/theta_m] (Y_m := sum_{W(m)} y_k), with Psi^0_y(xhat) = 0 by Lemma J2.0's 1-homogeneity; (2.1) and K2.3 then force K2.16's
structure (nonpositive common mode; robustly negative common mode with proportional thick design-depth support).  So (H1*) at every row
is as hard as Step A; OPEN, and bypassed by Theorem J2.1.
3.4 REMARK J2.6 (PROVED).  Orientation vs_l eps_l of tuned carriers (= K2.17(g)'s sign for SLD signatures): an active weak peak has
orientation sgn(e_k - Delta'_m) (+1 when Delta'_m < 0); by the coupling row (X3)/kappa, sum_l |r_l||gamma_l| vs_l eps_l = Delta'_m, so a block with
Delta'_m < 0 always has an active carrier of orientation -1.  So in the merged Step A a one-sided weak peak can enter a (U*)-certificate only
together with a one-sided carrier of the opposite orientation in its block (K2.17(g) fails); the kappa lever then has to satisfy kappa'/kappa
>= |r_k|/|r''_k| (weak peak) and <= |r_l|/|r''_l| (the other carrier): a TARGET-PLACEMENT condition (J1 Lemma J1.2), not a push condition.

## 4. Numerics (sanity only; J2_part4.md; r12/J2_work/)
frozen_check.py (50 digits, 40 blocks): theta_f <= theta, (theta - theta_f)/(theta b Phi_W^2/Phi_Pf^2) <= 0.87 (bound 3); frozen Lemma K identities
to 3e-51; consistent frozen points (after a direct push or a threshold raise to frozen rho = 1 - mu/2) equal the true block exactly; Lemma
J2.0 (finite differences 5e-17; Euler 8e-51).  frozen_check2.py (double, 200 blocks): frozen Lemma J2.0 (7.6e-7), first-order threshold raise
(8.4e-7), Lemma J2.1(d) derivatives (1.2e-6); along a threshold crossing the TRUE formula-1 kappa has a derivative jump up to 0.95 (K-8),
the frozen kappa_f none (6e-8 = O(h)); frozen = true on the consistent side (9e-16).  merged_stepA_toy.py (300 one-block toys): a weak
peak whose only resource is one-sided in the wrong direction for a push (the bad case of R-8) is realized INSIDE Step A from the unpushed row
by the kappa/threshold lever (peak raise <= 1.05e-2 ~ mu/2 + b) with the other carriers following; 300/300 realized points (FC)-consistent,
frozen = true to 1.1e-15, true status of the former weak peak exactly 1 - mu/2.  lemmaJ21e_adversarial.py (16834 admissible blocks with extreme
weight ratios and b up to 1e-1): 0 violations of Lemma J2.1(e) (max ratios 1.06 of the bound-3 quantity, 0.004 of the bound-4 quantity).
frozen_c11_check.py (150 blocks, paths across the true threshold): frozen kappa_f has second-order remainder/t^2 <= 1.2e-5 (C^{1,1}); the true
formula-1 kappa has remainder/t^2 up to 1.2e2 at 506 post-crossing points (first-order kink).

## 5. What changes in the record
 - Theorem K2.15 (K2-ref G): replace "(H1*) and (H2)" by "(H2^flat)"; the residual (K2 7.3, K2-ref G) loses (W)/(W*).
 - K2-ref K-8: read with the TARGET pattern (FC) (needed also for active weak peaks of (U)-/(KN)-blocks).
 - K1-ref R-8 / K2-ref W-1: the data sign of a weak peak is vs_k sgn(e_k - Delta'_m).
 - R-8(ii)'s enlarged (D1) is no longer needed when Pi_0 = {} (kept; harmless).

## 6. Main obstacle; next steps
The only remaining hypothesis for (LSC-trunc)_N is the A-regularity of Step A (now evaluated at the unpushed row with (FC)): the sign class
(A*)/(U*) of Theorem K2.16, which J1 shows to be a genuine target-placement infeasibility (J1.4-J1.5) and reduces, via the one-out-of-many
principle, far placements, bands and target sets, to the residual (R0) ∪ (R1) of J1_notes 8 (see 7.3).  Weak peaks add nothing new to it:
after the merge they are ordinary tuned carriers of kinds (iii)/(iv) of K2.16.  Next steps (shared with J1): first-order Puiseux margin
(J1.11), constrained Lojasiewicz step for pinned thick-type ratios, KN-lever coupling, a uniform-sign object for pure (U*) on target-supported
rows, and a direct treatment of stable exact resonances through J1's flat block-represented direction.

## 6a. Points for a referee (objections considered; answers PROVED unless labelled)
 (Q1) "The rate objects of the clean sub-window are defined at f with the weak peaks as peaks."  No: X1-ref K1 requires formula-1 ratios with
      the PATTERN's Omega (active weak peaks in Omega); the frozen ratios at f^0 differ from these by <= C Design b (Lemma J2.1(e)) plus the
      moves f -> f^0, all inside the enlarged (D1) radius.
 (Q2) "K2.9(c) needs a C^{1,1} map on a domain of size W >> b; the weak peaks cross the threshold inside it."  With (FC) the frozen map is
      C^{1,1} (Lemma J2.1(b)); the crossings are invisible to it (numerics: no derivative jump).  The same issue exists WITH Step 0 (moves W
      >> b cross the threshold from rho = 1 - b; K2-ref K-8) and in (U)-/(KN)-blocks, where Step 0 never pushed (U1-ref Prop. KN Step 0:
      "(C1), (C2) only"; its realization takes active carriers with rho(f) <= 1 + b below threshold by the d_0 lever, U1-ref 3.3(b)).
 (Q3) "The frozen solution might not be the true companion."  Lemma J2.1(c): at a point where the frozen pattern is consistent the frozen
      scalars ARE the true ones (unique zero of the threshold equation, Y2 Lemma T(c)); Step (iii) checks consistency block by block from
      the targets (the status pattern of the companion is exactly (FC), Q1 CM^tr(b)).
 (Q4) "Something downstream uses the pushed row."  Audit 1.4: classes are read at f^r, (P) at design depth, data/Sys-DC/UE^inf/averaging at
      the companion; Lemma K2.13 only lists moves.  Nothing else refers to (WP).
 (Q5) "Without (WP) the Lojasiewicz start may lie outside the region where F is controlled."  F(r_0) <= 1 + Design^2 b (Step (i)); cert0 3.1
      already recorded the same bound ("C3 alternative") for the formula-1 ratios at f.
 (Q6) "The merged Step A is harder than (H2)."  It is not harder than (H1*) and (H2) together (Corollary J2.2: pre-pushes are allowed), and
      the weak-peak rows are present in (H2) already (they must go from 1 - b to <= 1 - mu, mu >= 8Mb).  Whether it is EASIER in some cases
      (e.g. the toy of 4, where a weak peak without any push resource is realized by the kappa lever) is not needed.

## 7. Combination with J1 (r12/J1_notes.md, final version read at the end of J2)
7.1 Transfer of J1's results to the unpushed row (PROVED).  J1 works at Step A's input row R_1 and already uses (FC) and Theorem J2.1
    (J1_notes 1, 6).  Its tools -- Lemma J1.1 (row identity u(zhat) = kappa_u + Dev_u(z), generator actions: every row), J1.2 (Euler, valid for the
    frozen map by Lemma J2.1(b)), J1.3-J1.5 (from K2.16 and row-level Cauchy-Schwarz; at a realized point frozen = true by Lemma J2.1(c)),
    J1.6-J1.7 (K2.16(2b), (3); far placements beyond D(L)), J1.8-J1.10 (band version of K2.9), J1.12-J1.14 (what Step A must realize; rescaling
    coupling) -- never use the true status of a weak peak at R_1, so with R_1 := f^0 + Pi and (FC) they hold verbatim (Corollary J2.3).
7.2 COMBINED STATEMENT (PROVED modulo the chain of K2.15 and J1's once-written, not yet refereed proofs).  Design T_fin^{K2} (option (a)), N >= 1,
    f in S_{p_N*} with arbitrary base support, g in C(f), rho in (0,1).  Suppose that for infinitely many main stages L some clean sub-window w and
    admissible class a satisfy, at the UNPUSHED prepared row with (FC) (optional pre-pushes Pi_0 allowed): Step A carries no near-certificate of
    size <= eps_*, or SOME thick-type coarse carrier satisfies one of J1's (J-a)-(J-f) (J1_notes 6: helpful far coordinate; private two-sided
    design-depth resource / robust-spread thick pair / same-orientation thick-S_th pair; zero-data strict non-peak or free-ratio active
    carrier of a (U)-block with a private two-sided peak resource; KN-1 carrier of a (T)-block with first-order Puiseux margin; active carrier
    of a shifted block under J1's mismatch tolerance or with a free ratio and no R^2-sensitive protected status), or one of K2.17 (a), (b), (f)
    holds.  Then (f, rho g) is in the closure of NA((c_0, p_N), l_2^2) along norm-attaining rows with finite base support, i.e.
    (LSC-trunc)_N holds at (f, g, rho).  No hypothesis on Step 0 remains (Theorem J2.1), and Sys-DC needs none (K2.6).
7.3 Residual (OPEN; = J1_notes 8).  (f, g, rho) is not covered only if at all but finitely many main stages, at every clean sub-window and
    admissible class, Step A at the unpushed row carries a near-certificate in J1's normal form (kappa_y <= -c_*/nu_1, Psi_y = kappa_y(a + Theta_y)
    + E_y, one-sided hole mass >= 1 - small; targets infeasible for every companion keeping the one-sided signs, J1.5) AND either (R0) every
    thick-type carrier is rigid at once (frozen far window, no private two-sided resource, tiny spreads, and of type (R-pin), (R-T) [empty under
    J1's Proposition J1.11, a SKETCH], (R-Ts), (R-KN), (R-D2), (R-np) or (R-pk)), or (R1) there is no thick-type carrier and the certificates are
    of pure type (U*).  Weak peaks enter only as ordinary tuned carriers (kinds (iii)/(iv)); a one-sided weak peak takes part only together
    with a one-sided carrier of the opposite orientation in its block (Remark J2.6).  In the stable case J1 obtains an exact flat
    block-representable direction at f with base trace a (J1 7.4).  Neither the emptiness of this residual nor a non-recoverable mate of such a
    row is shown: (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the
    Martin-type norm built with T_fin^{K2} remain OPEN.  If the residual is shown empty (at infinitely many main stages, for every (f, g, rho)),
    then Theorem J2.1 / J1.15 with Q1's Theorem VI.2 give (LSC-trunc)_N for every f, hence density of NA((c_0, p_N), l_2^2) for every N, hence
    (Corollary VI.3; T_fin^{K2} is N-independent) density of NA((c_0, p), l_2^2).
