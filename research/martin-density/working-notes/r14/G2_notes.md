# G2 notes (Round 14): the refined residuals of Round 13 -- minimax over the certificate hull, the joint Farkas form,
# coupled directions, margin levers, and why counting cannot exclude persistence

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED (mod chain)" = proved here modulo the refereed chain that J1.15' (J1-ref E),
J2's Theorem J2.1, H1-ref (Lemma SLP, Lemma PC, Proposition MA') and H2-ref already cite (X1/X1-ref, X2/X2-ref, Q1/Q1-ref a,b, cert0-3,
Q2/Q2-ref a, K1/K1-ref, K2/K2-ref, J1/J1-ref, J2/J2-ref, H1/H1-ref, H2/H2-ref; several links once-refereed).  Part files: r14/G2_part1.md
(Lemma MS, Theorem JF, Lemma NP'), G2_part2.md (coupled directions, Lemma 3.4(c), Theorem H2.A'), G2_part3.md ((W4''), capped generators,
obstruction decomposition, margin levers, Proposition EX), G2_part4.md ((R0) readings, Lemma NL, peak conversion).  This file supersedes
the part files where they differ (constants of Lemma NL, Theorem ML in the per-block form, Theorem R1-P).  Scripts: r14/G2_work/.

## 0. Bottom line
(1) NEW TOOL, PROVED (mod chain): LEMMA MS (minimax over the certificate hull).  All first-order status-safe, exactly admissible target
    displacements of a stage form ONE compact convex polytope D_h; the near-certificates form a compact set Y whose convex hull stays
    away from 0 because the common mode gamma(y) = y^T gt^A is LINEAR and <= -c_* on Y.  Von Neumann/Sion: either one displacement
    realizes Step A against all certificates at once, or one hull element z* pairs below c_MS with every admissible displacement; z*
    inherits every LINEAR property of near-certificates (Lemma AL, J1.6(a), R-PK, Lemma NP, H2 (1.2), Proposition 3.1).  Its LP dual is
    the JOINT FARKAS FORM (Theorem JF): kappa z* = A^T lambda + nu + err with status multipliers lambda >= 0 and nu normal to the exact set.
    This is the minimax version of H1-ref's Lemma SLP asked for in (R0): objects containing non-thick kind-(iv) rows, all blocks at once,
    multi-block affine groups, shared target-coordinate generators (they enter through z*^T g >= -eps) and shifted blocks with one-sided
    kappa levers are covered.
(2) (R1), PROVED (mod chain): Lemma 3.4(c) (outward K^+ rows in protected blocks) via explicit COUPLED DIRECTIONS v_lp = sgn(r_l) e_l -
    c_lp sgn(r_p) e_p, status-safe to first order by Lemma K (checked numerically with the true K, N1); the (U)-block coupling with the block
    scaling replaces G-CPL's Brouwer-in-s; THEOREM H2.A' (H2.A with one fixed displacement); THEOREM R1-J (the (R1) residual in joint form);
    LEMMA 4.1: the (W4'') re-check for (D-abs) passes (the cluster constraint set only shrinks), so (D-abs)'s memory holds: at most N
    (up)/(down) events per round range.
(3) Persistence, PROVED as statements about the method: the counting/pigeonhole route of the task CANNOT exclude (R1) (Corollary 4.8):
    in the restricted model an EXACT one-signed resonance (value 0, tiny at every sub-window) already obstructs A-regularity (Proposition
    4.7) -- the obstruction is the one-sidedness of pinned kind-(iv) rows at the ERROR SCALE of the realization (second-order margin rho_0,
    dual error c_MS eta', status descent S_prot), not the size of the resonance; and a wrong-signed resonance obstructs every sub-window
    coarser than the one it spoils.  Memory gives freshness of CARRIERS only.
(4) NEW POSITIVE RESULT, PROVED (mod chain; the depth extension of K1's pull bookkeeping is an inspection claim): THEOREM ML (margin
    levers).  A pinned kind-(iv) row with a pullable coordinate at depth v in [cap_min/2, c_0 W] (cap_min ~ eta' Des^{-C}: an interval of
    design length JUST BELOW the Step-A pull range that defines kind (iv)) is "controlled": a TU pair there is a CAPPED downward generator,
    and by the capped minimax (Lemma 4.3) and the obstruction decomposition (Lemma 4.4) the residual certificate carries no weight on
    it.  Hence a non-realized (R1) stage needs, in some block, an UNCONTROLLED pinned row: deep-swallowed (no pullable coordinate in
    [cap_min/2, x''_max]), or in a non-affine group at a singular target, or the status-descent class (P-prot) (Theorem 4.9).
(5) (R0), PROVED (mod chain): Theorem 5.2 (the (R0) residual in joint form; H1-ref's (H-3') extended to objects containing kind-(iv)
    rows; the (H-4') multiplier identity); LEMMA NP' (thick-type robust peaks of SHIFTED blocks force sigma_m = sgn Delta''_m and no
    two-sided peak resource; otherwise realized); LEMMA NL = 5.3 (non-affine pinned groups -- (X4^0)-minors, cofactor polynomials -- have exact
    tangent levers wherever their Jacobian is robust; the remaining (H-6') is non-affine groups at SINGULAR targets); Proposition 5.4
    (peak conversion is never needed in (U)-blocks with a peak resource); Lemma 5.5 (the (FC)-consistency gap of peak conversion is
    closed: freezing d as a peak with the band row is consistent by J2.1); Remark 1.8 (P-KN: every Lemma-MS lever is legitimate in
    (KN)-blocks under the pre-move convention).  Peak conversion itself stays SKETCH (two precise gaps G1, G2).
(6) NOT PROVED: that the residual stages are non-persistent.  The precise remaining (R1) step is: fresh deep-swallowed pinned kind-(iv)
    carriers in a one-signed (possibly exact) resonance at every main stage, or (P-prot), or (P-naff) -- none excluded.  (R0): the
    coincidence classes of Theorem 5.2 and (H-7).  (LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of
    NA((c_0, p), l_2^2) for the Martin-type p: OPEN.  No counterexample is claimed; nothing found suggests one (the residual consists of
    sign/coincidence conditions on stage data and of deep swallowing patterns that a row must renew at every stage).

| # | Result | Status | Section |
|---|---|---|---|
| 1 | Lemma 1.1 (linearity of certificate properties; hull away from 0) | PROVED (mod chain) | 2 |
| 2 | Lemma 1.3 (exactness and legitimacy of D_h) | PROVED (mod chain) | 2 |
| 3 | Lemma MS (minimax over the certificate hull; LP dual) | PROVED (mod chain) | 2 |
| 4 | Theorem JF, Corollary JF' (joint Farkas form; multi-block, shared generators, shifted blocks) | PROVED (mod chain) | 2 |
| 5 | Lemma NP' (thick-type robust peaks in any block) | PROVED (mod chain) | 2 |
| 6 | Remark 1.8 (P-KN for Lemma-MS levers, pre-move convention) | PROVED (mod chain) | 2 |
| 7 | Lemma 3.1' (status calculus of coupled directions) | PROVED | 3 |
| 8 | Lemma 3.2 (= H2 Lemma 3.4(c): outward K^+ rows with a partner) | PROVED (mod chain) | 3 |
| 9 | Theorem H2.A' (H2.A by one fixed displacement) | PROVED (mod chain) | 3 |
| 10 | Theorem R1-J ((R1) residual in joint form) | PROVED (mod chain) | 3 |
| 11 | Lemma 4.1 ((W4'') re-check for (D-abs)) | PROVED (inspection of the complete weight list) | 4 |
| 12 | Lemma 4.2 (CAP), Lemma 4.3 (MS^cap) (capped generators) | PROVED (mod chain) | 4 |
| 13 | Lemma 4.4 (OD, obstruction decomposition), Lemma 4.5 (MV, multiplier vanishing) | PROVED (mod chain) | 4 |
| 14 | Theorem ML (margin levers) | PROVED (mod chain + inspection claim (K1-depth)) | 4 |
| 15 | Proposition 4.7 (= EX: exact one-signed resonances obstruct; restricted model) | PROVED | 4 |
| 16 | Corollary 4.8: premise of the suggested counting route ('each fresh resonance obstructs at most one sub-window'; exact resonances harmless) | FALSE (PROVED in the restricted model of Prop. 4.7) | 4 |
| 17 | Theorem 4.9 (= R1-P: precise persistent (R1) residual) | PROVED (mod chain) as a necessary condition | 4 |
| 18 | (R1) at all large main stages impossible | OPEN | 4, 7 |
| 19 | Lemma 5.1, Theorem 5.2 (= R0-J: (R0) in joint form) | PROVED (mod chain) | 5 |
| 20 | Lemma 5.3 (= NL: tangent levers of non-affine groups with robust Jacobian) | PROVED | 5 |
| 21 | Proposition 5.4, Lemma 5.5 (peak conversion: where needed; (FC) consistency) | PROVED (mod chain / mod J2.1) | 5 |
| 22 | Peak conversion of anti-aligned near-threshold rows | SKETCH (gaps G1, G2) | 5 |
| 23 | (R0) at all large main stages impossible | OPEN | 5, 7 |
| 24 | (LSC-trunc)_N for every f; density for p_N, p | OPEN | 7 |

## 1. Setting
Design T_fin^{K2} (K2 6.1) with J2's frozen convention (FC), J1-ref's P-TU windows and F-2, (D-enum), diagonal base; N >= 1; f in S_{p_N*}
with forced data; g in C(f); rho in (0, 1).  Main stage L >= l_f, clean sub-window w, class a; b, u, T = T_lo(w), eta' = T^4/(L Des(L)),
x = C Des eta' (Step-A scale), D = D(L).  Step A at admissible targets rt (J1.13 (i)-(ii)): rows l in Lambda_A, Ft_l(rt) = val_l -
rt_l kappa_{m(l)}, b(rt) = -Ft(rt), generators G (Definition III-Areg), W = Des^{C_A} u^{-3} max(x, ||b||), rho_0 = C_2 W^2.  rc :=
(val_l/kappa_{m(l)})_l = realized ratios of the start row.  A near-certificate of size eps is a unit y with y^T g >= -eps for all g in G;
phi_y(rt) := y^T Ft(rt) = <kappa y, rc - rt>, <kappa y, Delta> := sum_l kappa_{m(l)} y_l Delta_l.  Lemma TF' (H1): targets rt' with
||kappa (rt' - rt)|| <= Des^C u^{-C}(||b|| + x) (H1-ref P-TF) are realized if no near-certificate at rt' has phi_y(rt') > -rho_0(rt'); near-
certificates at rt' of size < 4 Des^{-C_A} u^3 are near-certificates at rt of size <= eps_* = u^3 Des^{-C} (generators Lipschitz in rt).
Lemma K (X1 1.1, J2.1(d)): rho_d = m |r_d| K(sigma, R^2)/Phi_d, sigma fixed by the frozen peak pattern, K increasing in R^2 with dK/dR^2 >=
c_K, K <= 8.5 on the W-fix region; kappa'_m := d log K/d R^2 in [c_K/8.5, C D^C].

## 2. The minimax target lemma and the joint Farkas form (details: G2_part1.md)

LEMMA 1.1 (linearity).  PROVED (mod chain).  Fix the stage and targets rt_0; eps_1 := eps_*; Y := {y : ||y||_2 = 1, y^T g >= -eps_1 for all g in G}.
(a) gamma(y) := <U^* Psi^A_y, e_1> = y^T gt^A is linear in y, ||gt^A||_2 <= Des^{C_g} (Lemma III-Euler(c); Psi^A_y = sum y_l eps_l u_l -
    sum_m beta^A_m K_m with beta^A_m = sum_{l in m} y_l rt_l linear in y).
(b) gamma(y) <= -c_* on Y (Theorem III-Aobs(3); at (R1) stages kappa_y <= -c_1/(8H(L)), H2 Fact 1.2).
(c) Every z in conv(Y) has z^T g >= -eps_1 (g in G), gamma(z) <= -c_*, ||z||_2 >= c_* Des^{-C_g}.
(d) Every conclusion of the structure theory that is a LINEAR inequality "Lin(y) >= -E" or a linear approximate identity "|Lin(y) -
    kappa_y Q| <= E" with E independent of y holds for every z in conv(Y) with the same E (kappa_z := gamma(z)/nu_1).  This covers Theorem
    III-Aobs (2), (2a)-(2c), (3), (4), (5) [not (6), whose hypothesis phi_y > -rho_0 is not inherited by convex combinations]; J1.6(a) coef_k = kappa_y rho_k + O(eps Des^2) on thick-type carriers; Lemma AL; R-PK |zeta_m| <= (4/3) eps
    Des; Lemma NP(b) (sgn zeta_m = sigma_m, |zeta_m| >= c_* u/(4 nu_1)); H2 (1.2) y_l >= -e_1 on kind (iv); H2 Proposition 3.1(a)-(c).
Proof.  (a) linearity; |g_l| <= ||U|| ||u_l||_1, |rt_l G^A_m| <= Des^C, |Lambda_A| <= Des.  (b) cited.  (c) the constraints are convex; gamma(z)
= sum theta_i gamma(y_i) <= -c_*; c_* <= |gamma(z)| <= ||gt^A|| ||z||.  (d) apply the structure theory to each y_i in Y (size <= eps_*, so it
applies) and average: sum theta_i Lin(y_i) >= -E; |sum theta_i (Lin(y_i) - kappa_{y_i} Q)| <= E with sum theta_i kappa_{y_i} = kappa_z.  Sign
statements: if sgn zeta_m(y_i) = sigma_m and |zeta_m(y_i)| >= z_0 for all i, then the same holds for z.  QED

DEFINITION 1.2 (admissible displacements).  MOV := movable rows (inactive rows incl. holds, D2/KN-pushed rows; active rows with a free
ratio).  Pinned group G = connected component of the linking graph of pinned active ratios (H1 GS).  V_G := tangent space of the zero set
of G's tiny polynomials if all of them are affine in r^G (other groups fixed) or have a robust Jacobian (Lemma NL, Section 5); otherwise
V_G := span{rt_0^{G ∩ m} : m a (U)-block} (piece scalings, H1-ref Lemma PC).  V := span{e_l : l in MOV} ⊕ (⊕_G V_G).  N := protected rows
(near-threshold actives incl. (FC)-frozen weak peaks, D2/KN-pushed rows; Puiseux statuses of (T)-blocks).  For d in N of block m:
l_d(Delta) := Delta_d/rt_{0,d} + 2 kappa'_m m^2 sum_{l in Omega_{(d)}} rt_{0,l} Delta_l (Omega_{(d)} = coarse non-P_rob carriers of m, or the
actives of m for a Puiseux status), with coefficient vector a_d.  rbar_l := max(|rt_{0,l}|, u Des^{-C_3}), ||Delta||_rt := max_l |Delta_l|/rbar_l,
D_h := {Delta in V : l_d(Delta) <= 0 (d in N), ||Delta||_rt <= h} (compact convex; D_h = h D_1).

LEMMA 1.3 (exactness and legitimacy).  PROVED (mod chain).  For h <= h_max := Des^{C_h} u^{-4}(||b(rt_0)|| + x) and Delta in D_h, the targets
rt' := rt_0 + Delta (+ E(Delta) on robust-Jacobian groups, Lemma NL) lie EXACTLY on Z_kappa; protected statuses increase by <= Des^C h^2
<< eta'/(12 Des) (the slack at the targets); robust statuses/peaks move by <= Des^C h << u; nearly neutral rows stay below Des^C h/u <<
eta'^{1/2}/Des^C (inside Corollary 2.4's band for KN-1 holds, as for H1's nearly-neutral displacement); the class data
projected at the realized ratios meet J1.13 (violations <= Des^C u^{-C} x/t << K t); ||kappa(rt' - rt_0)|| <= Des^C h_max (Lemma TF' with P-TF).
Proof.  Each tiny polynomial involves the ratios of one group only and no movable row.  Affine G: P(rt_0 + Delta) = P(rt_0) + dP(Delta) = 0.
Piece scalings: P(.., s r^{(m)}, ..) = s^{e_m(P)} P(..) separately per (U)-block (Lemma PC), and s rt^{G∩m} - rt^{G∩m} = (s - 1) rt^{G∩m}
exactly.  Robust-Jacobian groups: Lemma NL.  Statuses: log rho_d = log(m |r_d|/Phi_d) + log K(sigma, R^2), first variation l_d <= 0, second
derivatives <= Des^C (|r_d| >= u Des^{-C}, K Nash on the W-fix region); h^2 Des^C <= Des^C u^{-8} (||b|| + x)^2 << eta'/Des since ||b|| + x
<= Des^C eta' and eta' <= (u/(4 Des))^{4L^2 + 80}.  Slack: H1-ref SLP(a) ((U): <= 1 - eta' at targets; (T): Puiseux margin mu >= eta'/(3 Des),
J1.11; (KN): Remark 1.8).  Data: as in H1 Theorem IN.  QED

LEMMA MS (minimax over the certificate hull).  PROVED (mod chain).  Put Phi(Delta, y) := <kappa y, Delta> - phi_y(rt_0) and, with
rho_0^max := max_{Delta in D_{h_max}} rho_0(rt_0 + Delta) (<= x/4), V_MS := max_{Delta in D_{h_max}} min_{y in Y} Phi(Delta, y).
 (a) If V_MS >= rho_0^max (plus the Lemma NL error, Section 5), Step A is realized at rt_0 + Delta* (Delta* a maximizer): A-regular, exact
     on Z_kappa, statuses protected, data projected at the realized ratios.
 (b) Otherwise there is z* in conv(Y) with
        h_max max_{Delta in D_1} <kappa z*, Delta> < phi_{z*}(rt_0) + rho_0^max,   phi_{z*}(rt_0) > -rho_0^max,                           (2.1)
     hence max_{D_1} <kappa z*, Delta> < c_MS := (||b(rt_0)|| + rho_0^max)/h_max <= u^4 Des^{-C_h}; and z* has every property of Lemma 1.1(c),(d).
 (c) (LP dual) There are lambda >= 0 on N and nu in V^perp with
        sum_l rbar_l | kappa_{m(l)} z*_l - (A^T lambda)_l - nu_l | < c_MS,   (A^T lambda)_l = sum_{d in N} lambda_d (a_d)_l.                     (2.2)
Proof.  (a) Lemma 1.3 gives admissibility and the TF' size.  If Step A at rt' were not A-regular, Lemma III-cone(b) would give a near-
certificate y at rt' of size < 4 Des^{-C_A} u^3 with phi_y(rt') > -rho_0(rt'); by Lipschitz dependence of the generators on the targets,
y is in Y; phi_y(rt') = phi_y(rt_0) - <kappa y, Delta*> = -Phi(Delta*, y) <= -V_MS <= -rho_0^max: contradiction.  Realization: Lemma
III-cone(c) for the (FC)-frozen map (J2.1 (ii)-(iii)).  (b) Phi is affine in each variable; D_{h_max} and conv(Y) are compact convex; von
Neumann/Sion: max_D min_{conv Y} Phi = min_{conv Y} max_D Phi, and the minimum of an affine function over conv(Y) is attained on Y.  A
minimizer z* has max_D Phi(., z*) < rho_0^max; Delta = 0 gives phi_{z*} > -rho_0^max; D_h = h D_1 and |phi_{z*}| <= ||b(rt_0)|| give the
bound on max_{D_1}.  (c) LP duality for max{c^T Delta : Delta in V, A Delta <= 0, |Delta_l| <= rbar_l}, c = (kappa_{m(l)} z*_l)_l: the dual
function of the multipliers lambda >= 0 (for A Delta <= 0) and nu in V^perp (for Delta in V) is sum_l rbar_l |c - A^T lambda - nu|_l; strong
duality (Delta = 0 feasible, bounded).  QED
REMARK 2.1.  H1-ref's Lemma SLP is the case where every object consists of thick-type and kind-(i) rows (then <kappa z, Delta> = kappa_z
(Xi . delta) + small for every z in conv(Y), Lemma AL being linear).  Every lever of H1 (TF', IN, OUT, GS, DS, UC, RL, KC, TG) and of H2
(bands on free K^- rows; K^+ bands with F-2 coupling; Lemma 3.4) is a displacement in D_h up to second order (the OUT(b) exchange is
R^2-neutral to first order; the coupled forms are Lemma 3.2 below), so Lemma MS(b) is the exact dual residual of all of them at once.
Numerics N3 (G2_work/n3_minimax_lp.py): minimax identity and the LP duality (2.2) to 1e-13 on 400 random instances.

THEOREM JF (joint Farkas form).  PROVED (mod chain).  If Step A is not realized, there are z* in conv(Y), lambda >= 0, nu in V^perp with
(2.1)-(2.2) and:
 (JF1) [movable rows] for l in MOV: |kappa_m z*_l - lambda_l 1[l in N]/rt_{0,l} - 2 kappa'_m m^2 rt_{0,l} Lambda^{(l)}_m| <= c_MS/rbar_l,
       Lambda^{(l)}_m := sum{lambda_d : d in N, l in Omega_{(d)}} >= 0; in an unprotected block |z*_l| <= c_MS/(kappa_m rbar_l);
 (JF2) [affine or robust-Jacobian groups G, also multi-block] ||(kappa z* - A^T lambda)|_G - sum_i mu_i grad_G P_i(rt_0)||_{rbar,1} < c_MS
       for some numbers mu_i (normal space of Z_kappa at rt_0, restricted to G);
 (JF3) [non-affine groups at singular targets] for every (U)-piece G ∩ m: |sum_{l in G ∩ m} (kappa_m z*_l - (A^T lambda)_l) rt_{0,l}| < c_MS;
 (JF4) [certificate structure] z*^T g >= -eps_1 for every generator (private, shared target-coordinate TS/FR/ZD moves, peak levers,
       pre-placed TU levers) and the whole list of Lemma 1.1(d);
 (JF5) [wrong side] phi_{z*}(rt_0) = <kappa z*, rc - rt_0> > -rho_0^max.
Proof.  (2.2) splits over V = span(MOV) ⊕ (⊕ V_G): nu vanishes on MOV and nu|_G is in V_G^perp; V_G^perp is spanned by the gradients when V_G
is the tangent space, and is the orthogonal complement of the piece vectors otherwise (pair with rt^{G∩m}, |rt_{0,l}| <= rbar_l).  QED
COROLLARY JF' (single (U)-block; H2 Proposition 4.1 in the joint system).  PROVED (mod chain).  For an internal affine group of a (U)-block
with a peak resource, pinned kind-(iv) rows P and kind-(i) rows Q, at an (R1) stage: C'_mu := sum mu_i grad P_i satisfies (C'_mu)_l >=
-kappa_m e_1 - (A^T lambda)_l - err_l on the oriented rows of P and |(C'_mu)_l| <= kappa_m(eps Des^2 + e_X) + |(A^T lambda)_l| + err_l on Q, and
(JF5) reads sum_i mu_i P_i(rc) + S_prot + (other terms) > -rho_0^max (Lemma OD).  With lambda = 0 on the block this is H2's one-signed linear
resonance, now derived with all other blocks, shared generators and multi-block affine groups present (P-41 (i), (ii) removed; P-41 (iii),
the margin, is the threshold rho_0^max).  Proof: (JF2) with z*_l >= -e_1 on kind (iv) and |z*_l| <= eps Des^2 + e_X on kind (i).  QED

LEMMA NP' (thick-type robust peaks in any block).  PROVED (mod chain).  If a robust coarse peak c of a block m (shifted or not) is
thick-type (thick private p in S_c ∩ [1, D]), then for every y in Y (and every z in conv(Y)): zeta_m(y) = -kappa_y rho_c vs_c/(lambda_c (1 -
X_m)) + O(eps Des^2/lambda_c); so sgn zeta_m = sigma_m := sgn(rho_c vs_c), |zeta_m| >= c_* u/(4 nu_1), common to all thick-type robust peaks of
m.  Hence Step A is realized if (i) m has a private two-sided peak resource (R-PK contradicts the lower bound), or (ii) m has a one-sided
peak lever and sigma_m != sgn(Delta''_m) (H2 Proposition 3.1(b): kappa-raising iff Delta''_m < 0 forces zeta_m <= small), or (iii) a thick-type
robust peak has a private S_th coordinate s' carrying data with z_{s'} = sgn a_p (Corollary III-Asuff(d); data sign eps_c = -sgn(Delta''_m)
vs_c, J2 1.3, so (iii) is again sigma_m != sgn(Delta''_m)).  If moreover rt^{(m)} is in V, Step A is realized when sigma_m = -1 (down-scaling,
pairing -delta kappa_m zeta_m >= delta kappa_m c_* u/(4 nu_1)) or sigma_m = +1 and m is unprotected.  In a shifted block a tiny minor through
(X3)_m is M = C_{Delta'} - sum_l r_l C_l; scaling preserves it iff C_{Delta'} = 0.
Proof.  H1 Lemma NP(b)'s computation: c untuned (robust peaks are not Sys-A rows under (FC)), coef_c = -zeta_m lambda_c d kappa_m/d zeta(c),
d kappa_m/d zeta(c) = vs_c(1 - X_m) with 1 - X_m = 1 - a_f s_f/(Phi'^2(1 + a_f)) in [3/4, 1] (J2.1(d); route V: s_f contains only fine
non-peaks), and coef_c = kappa_y rho_c + O(eps Des^2) (Theorem III-Aobs (2b), valid for any coarse carrier with a thick private coordinate).
Delta'_m = 0 was used in H1 only to show that (U)-block peaks carry no data.  (i)-(iii) and the last claim: as stated (Lemma MS(a) with
Delta = -/+ delta rt^{(m)}).  QED

REMARK 1.8 ((KN)-blocks, P-KN).  PROVED (mod chain: U1-ref Proposition KN(b), cert0 3.2, J2-ref Q-KN).  With the one-shot pre-move
convention for the KN lever d_0 (its push raises theta by >= C' D eta' theta before Step A), a (KN)-block enters Step A with protected
statuses of margin >= c D eta' >> Des^C h_max^2; every displacement of D_h keeps them at first order and moves them by <= Des^C h^2 at second
order; d_0 is a movable row of N.  So every Lemma-MS lever is legitimate in (KN)-blocks with no lever coupling.

## 3. (R1): coupled directions, Lemma 3.4(c), Theorem H2.A' (details: G2_part2.md)
At an (R1) stage every tuned row is kind (i) or kind (iv); K^+_m / K^-_m = kind-(iv) rows of block m with eps-oriented target ratio > 0 / < 0.
Inward = |rt_l| decreases.  The helpful direction of a kind-(iv) row (pairing >= -kappa e_1 with every certificate) is oriented up: inward
for K^-, outward for K^+.

LEMMA 3.1' (status calculus; = Part 2 Lemma 2.1).  PROVED.  Let d in N ∩ m and l, p rows of m.
 (a) l_d(-sgn(rt_l) e_l) = -(1[l = d] + 2 kappa'_m m^2 rt_l^2 1[l in Omega_{(d)}])/|rt_l| <= 0;
 (b) l_d(sgn(rt_l) e_l) >= 0, > 0 iff l = d or l in Omega_{(d)};
 (c) if p != l is movable with |rt_p| >= u Des^{-C_3} and p in Omega_{(d)} whenever l in Omega_{(d)} (a PARTNER), then with c_lp := (|rt_l| +
     1[l in N]/(2 kappa'_m m^2 |rt_l|))/|rt_p| <= Des^C/u^2 the coupled direction v_lp := sgn(rt_l) e_l - c_lp sgn(rt_p) e_p has l_d(v_lp) <= 0;
 (d) with c_l := 1[l in N]/|rt_l| + 2 kappa'_max m^2 |rt_l| <= Des^C/u (kappa'_max := max over the statuses d of m of kappa'_{(d)}),
     v_l := sgn(rt_l) e_l - c_l rt^{(m)} has l_d(v_l) <= 0; in a (U)-block rt^{(m)} is in V (sum of all piece scalings and movable rows), so
     v_l is in V for movable l.
Here kappa'_{(d)} := d log K/d R^2 for the status of d (route V: common to the block; a Puiseux status: at (sigma_rob, R_a^2)); in (c) the
kappa' in c_lp is that of l's own status (for d = l), and the inequality for d != l uses only c_lp |rt_p| >= |rt_l|.
Proof.  l_d(Delta) = Delta_d/rt_d + 2 kappa'_{(d)} m^2 sum_{Omega_{(d)}} rt_k Delta_k.  (c): for d notin {l, p}: 2 kappa'_{(d)} m^2 (|rt_l| - c_lp |rt_p|)
<= 0; for d = l: 1/|rt_l| + 2 kappa'_{(l)} m^2 (|rt_l| - c_lp |rt_p|) = 0; for d = p: -c_lp/|rt_p| + 2 kappa'_{(p)} m^2 (|rt_l| - c_lp |rt_p|) <= 0.
Size: kappa' >= c_K/8.5.  (d): l_d(rt^{(m)}) = 1 + 2 kappa'_{(d)} R^2_{(d)} >= 1, so l_d(v_l) <= 1[l = d]/|rt_l| + 2 kappa'_{(d)} m^2 |rt_l| - c_l <= 0.  QED
Numerics N1 (G2_work/n1_status_calculus.py, true Lemma-K function, 3657 random blocks): max first-order l_d over d in N: inward -2e-6,
coupled with partner 1e-13, coupled with block scaling 9e-14 (i.e. <= 0 up to rounding); true second-order increase of log statuses <=
0.56 (h(1 + ||v||_rt))^2.

LEMMA 3.2 (= H2 Lemma 3.4(c), outward rows in protected blocks).  PROVED (mod chain).  Let l in K^+_m be free in a protected block m with a
partner p (kind (i); free K^- with robust ratio; an inactive movable row -- hold, D2- or KN-pushed row, the KN lever d_0; for Puiseux
statuses of a (T)-block p must be active).  Then v_lp/||v_lp||_rt is in D_1 (||v_lp||_rt <= Des^C u^{-3}) and every hull element z (in
particular z* of Lemma MS(b)) satisfies kappa_m (z_l - c_lp sgn(rt_p) z_p) <= Des^C u^{-3} c_MS; with (JF1) or Lemma 1.1(d) for z*_p:
z*_l <= delta_2 := Des^C u^{-3}(c_MS + e_1 + eps Des^2 + e_X).
Proof.  Lemma 3.1'(c) and (2.1).  QED
Remarks.  This replaces H2's SKETCH of Lemma 3.4(c), including its all-at-once version: in Lemma MS each coupled direction is a point of
D_1 and (2.1) holds for all of them simultaneously; no bands and no Brouwer coupling are needed.  R_a^2 in (X4^0) rows: a free ratio lies in
no tiny polynomial; if a tiny minor of m contains an (X4^0) row, all active ratios of m are pinned (J1-ref P-MT).

DEFINITION 3.3.  At an (R1) stage a free K^+ row of a protected shifted block without a partner is LOCKED.  A kind-(iv) row is CONTROLLED if
it is free and not locked, or it is pinned in a group with V_G = tangent space (affine or robust Jacobian) and has a MARGIN LEVER of
capacity >= cap_min (Definition 4.6); otherwise UNCONTROLLED.  (Free K^- rows and free K^+ rows of (U)-blocks are always controlled.)

THEOREM H2.A' .  PROVED (mod chain).  At an (R1) stage, Step A is realized unless some block m is RESIDUAL: (two) m has a two-sided
peak resource and contains an uncontrolled K^- row AND an uncontrolled K^+ row; (up) m has only a kappa-raising lever and an uncontrolled
K^- row; (down) m has only a kappa-lowering lever and an uncontrolled K^+ row -- where in this theorem "controlled" means "free and not
locked" (pinned rows count as uncontrolled; the margin-lever clause is added in Theorem ML).  (This is H2's Theorem H2.A, realized by one
fixed displacement.)
Proof.  If not realized take z* (Lemma MS(b)).  Free K^- row: the inward (= oriented-up) direction rbar_l e_l is in D_1 (Lemma 3.1'(a)), so
kappa_m z*_l rbar_l <= c_MS, and z*_l >= -e_1: |z*_l| <= delta_1' := max(e_1, c_MS Des^{C_3}/(kappa_min u)).  Free K^+ rows: (U)-block: v_l of
Lemma 3.1'(d) gives kappa_m(z*_l - c_l zeta_m(z*)) <= Des^C c_MS/u with |zeta_m(z*)| <= (4/3) eps Des (R-PK; every (U)-block has a two-sided
peak resource at (R1) stages, H2 Fact 1.1(d)); unprotected shifted block: Lemma 3.1'(b); with a partner: Lemma 3.2.  Kind (i): |z*_l| <= eps
Des^2 + e_X.  Then H2's case analysis applies verbatim to z* (it uses only (1.2), Proposition 3.1 and these bounds, all linear): e.g. two-sided
lever with all K^- rows controlled: |zeta_m(z*)| <= (4/3) eps Des gives sum_{K^+} z*_l rt_l <= sum_{K^-} |z*_l||rt_l| + e_2 + (4/3) eps Des, each
K^+ term >= -e_1 Des^{C_4}, so z*_l <= Des^{C_3}(Z_m + |Lambda_A| e_1 Des^{C_4})/u on every K^+ row; symmetric cases likewise.  So |z*_l| <=
c_1/(16 |Lambda_A|) on all kind-(iv) rows and sum_{(iv)} z*_l < c_1/4, against Proposition 3.1(a) for z*.  QED

THEOREM R1-J ((R1) residual in joint form).  PROVED (mod chain).  If Step A is not realized at an (R1) stage: some block is residual (H2.A');
on locked rows (JF1) gives kappa_m z*_l = lambda_l 1[l in N]/rt_l + 2 kappa'_m m^2 rt_l Lambda^{(l)}_m + O(c_MS/rbar_l) (an R^2-proportional
weight supported by the multipliers of the block's protected statuses); on affine groups (JF2) with Corollary JF' (one-signed form); on
non-affine singular groups only (JF3); and (JF5).  Shared target-coordinate generators restrict z* through (JF4).  Proof: Theorem JF,
Lemma 1.1(d), Theorem H2.A'.  QED

## 4. Persistence of (R1) (details: G2_part3.md)

LEMMA 4.1 ((W4'') re-check for (D-abs)).  PROVED (inspection of the complete weight list, Q1-refb 1.2, cert3 3.4).  In (D-abs) the cluster
absorber targets live on E^ch'(p) = T(p) ∪ (Z_0 ∩ [1, p]) instead of E^ch(p) = T(p) ∪ union_{l''<=p}(S_{l''} ∩ [1, p]).  (a) The pairs (stage,
coordinate in some S_{l'}) at which (W4'') bounds a cluster weight form a SUBSET of the old ones (E^ch' ∩ union S_k = T(p) ∩ union S_k ⊂
E^ch ∩ union S_k; Z_0 meets no signature set).  (b) Allowedness (b) (= (W4), used by (T-b), (T-c)) still holds for every absorber target: its
signature coordinates lie in T(p) (H2 Lemma 2.2), where (W4'') is imposed.  (c) No LOWER bound on a weight involves E^ch(p) (the lower-bound
uses are W6 and P-R: the absorber's least entry and the factor 1 - 2^{-l}).  So c^max_l does not decrease, every admissible weight choice of
T_fin^{K2} (including the generic choice (QC1) in [(1 - 2^{-l}) c^max_l, c^max_l]) remains admissible.  QED
CONSEQUENCE (with H2-ref B.10; PROVED mod those).  In (D-abs) the cluster stage p + 1 still exists (1 in Z_0 ∩ [1, p]) and pushes s_max(p+1)
>= 4/T_lo(p, M(p)); within a round range [r, s_max(p_r)) every kind-(iv) carrier of an (R1) main stage is inactive at every later (R1) main
stage, switching signs do not flip, every (up)/(down) block becomes unshifted at every later (R1) stage: at most N (up)/(down) events per range.

LEMMA 4.2 (cone realization with capped generators, CAP).  PROVED.  Split the generators into G_u (Definition III-Areg, capacity W/2) and
G_c with capacities cap_g in (0, W/2]; R := {sum_g t_g g : 0 <= t_g <= cap_g}.  (a) If B(b, rho_0) ⊂ R, Step A is realized.  (b) Otherwise a
unit y has (W/2) sum_{G_u} (y^T g)_- + sum_{G_c} cap_g (y^T g)_- < phi_y + rho_0 (s_- := max(-s, 0)).
Proof.  (a) As Lemma III-cone(c): the minimal-norm selection S(b') := argmin{||s|| : sum s_g g = b', 0 <= s <= cap} is continuous on R
(strictly convex parametric QP, Hoffman-continuous feasible sets); Brouwer on the box; frozen bookkeeping unchanged.  (b) Separate b'' in
B(b, rho_0) \ R: y^T b'' < min_R y^T sigma = -sum_g cap_g (y^T g)_-, and -y^T b'' <= -y^T b + rho_0 = phi_y + rho_0.  QED
LEMMA 4.3 (MS^cap).  PROVED (mod chain).  With Phi^cap(Delta, y) := Phi(Delta, y) + sum_{G_c} cap_g (y^T g)_- (affine in Delta, convex in y),
Sion's theorem gives: either some Delta* realizes Step A with the capped generators, or some z* in conv(Y) has
      max_{Delta in D_{h_max}} <kappa z*, Delta> - phi_{z*}(rt_0) + sum_{G_c} cap_g (z*^T g)_- < rho_0^max,                                   (4.1)
so sum_{G_c} cap_g (z*^T g)_- < phi_{z*}(rt_0) + rho_0^max, and (2.1)-(2.2) hold.  Proof: Lemma 4.2(b) replaces Lemma III-cone(b) in Lemma
MS(a) (a certificate of Lemma 4.2(b) at rt_0 + Delta is in Y and has Phi^cap(Delta, y) < rho_0^max); for the maximizer Delta* of max_D
min_{conv Y} Phi^cap, min over Y >= min over conv Y.  QED

LEMMA 4.4 (obstruction decomposition, OD).  PROVED (mod chain).  For z* as in Lemma MS(b) or (4.1), with lambda, nu, mu of Theorem JF, and
for ANY admissible targets rt_0 on Z_kappa:
      phi_{z*}(rt_0) = S_prot + S_res + S_naff + O(c_MS ||rt_0 - rc||_rt + Des^C |mu| ||rt_0 - rc||^2),
 S_prot := -sum_{d in N} lambda_d l_d(rt_0 - rc)  (status change from the start row to the targets, weighted by the multipliers),
 S_res := sum over groups with V_G = tangent space of sum_i mu_i P_i(rc)  (tiny-polynomial values at the start row),
 S_naff := sum over the other groups of <nu|_G, rc^G - rt_0^G>.
Proof.  phi_{z*}(rt_0) = <kappa z*, rc - rt_0>; insert (2.2); <A^T lambda, rc - rt_0> = S_prot; nu = 0 on MOV; on a tangent-space group nu|_G =
sum mu_i grad P_i(rt_0) and grad P_i(rt_0).(rc - rt_0) = P_i(rc) - P_i(rt_0) + O(Des^C ||rc - rt_0||^2) with P_i(rt_0) = 0 (exact for affine P_i).
The tangential part of rt_0 - rc pairs to zero with the normal part of kappa z*: the decomposition holds for every choice of targets.  QED
LEMMA 4.5 (multiplier vanishing, MV).  PROVED (mod chain).  Lambda_m := sum_{d in N ∩ m} lambda_d.
 (a) In a (U)-block with a private two-sided peak resource: sum_{d in N ∩ m} lambda_d (1 + 2 kappa'_m R^2_{(d)}) = kappa_m zeta_m(z*) + O(c_MS),
     hence Lambda_m <= Des^C (eps + c_MS).
 (b) If m contains a movable row l with |rt_l| >= u Des^{-C_3}, l in Omega_{(d)} for all d in N ∩ m, and |z*_l| <= e_3 := eps Des^2 + e_X (kind
     (i), or an inactive row with two-sided private resources) or l in K^- (z*_l >= -e_1), then Lambda_m <= Des^C (e_1 + e_3 + c_MS)/u^2.
 In either case the block's contribution to S_prot is <= Des^C (eps + e_1 + e_3 + c_MS) eta'/u^3.
Proof.  (a) rt^{(m)} is in V, so <nu, rt^{(m)}> = 0; pair (2.2) with rt^{(m)} (|rt_l| <= rbar_l): kappa_m zeta_m(z*) - sum_d lambda_d l_d(rt^{(m)})
= O(c_MS), l_d(rt^{(m)}) = 1 + 2 kappa' R^2_{(d)} for d in m, 0 otherwise; |zeta_m(z*)| <= (4/3) eps Des (R-PK).  (b) (JF1) at l: the two
multiplier terms lambda_l 1[l in N]/rt_l and 2 kappa' m^2 rt_l Lambda_m have the sign of rt_l; for |z*_l| <= e_3 each is <= kappa_m e_3 +
c_MS/rbar_l; for rt_l < 0 their sum equals kappa_m z*_l + O(c_MS/rbar_l) >= -kappa_m e_1 - c_MS/rbar_l.  S_prot: |l_d(rt_0 - rc)| <= Des^C eta'/u.  QED

DEFINITION 4.6 (margin lever).  A pinned kind-(iv) row l has a margin lever of capacity cap if S_l contains a pullable coordinate j (K1 2.0:
a data-sign contact or near-contact of the companion, pull capacity (1 + eps_l z(j)) v_l(j) >= v_l(j)) with v_l(j) in [cap/2, c_0 W]; the lever
is the TU pair (pre-placed pull of mass 24 lambda_l v_l(j), sign -eps_l, at j, plus a compensating base bank at a near S_th coordinate of l):
a capped generator g_l^- with column -eff_l e_l + O(mu_s^2 theta_0 + v^2) and capacity >= v_l(j) (V1 Lemma TU, K1 2.1(b)).  Put
      cap_min := Des^{C_m} (Des^{-C_A} eta'/u + beta(b)/u^2 + c_MS eta'/u^4 + rho_0^max/u)/eff_min        (a design-small multiple of eta');
the depth range [cap_min/2, c_0 W] is nonempty when C_A >= C_m + 1, since c_0 W >= c_0 Des^{C_A + 1} u^{-3} eta', beta(b) <= eta'/3 (QC4),
c_MS eta'/u^4 <= Des^{-C_h} eta' and rho_0^max <= eta' (u/Des)^{4L^2} (u <= 1/4 and u(w) = b(w^-) may be tiny: only powers of Des/u are moderate).
(K1-depth) [INSPECTION CLAIM, not re-derived]: K1's bookkeeping of pre-placed pulls (cushion 24 lambda_l v >= t|c_l| v, tolerated
violations, cost C Des v log(1/v), window bookkeeping, P-RANGE) does not use v >= x and holds for depths v >= cap_min/2.

THEOREM ML (margin levers).  PROVED (mod chain and (K1-depth)).  At an (R1) stage assume
 (S) every protected block whose protected statuses are lowered from the start row to the targets satisfies a hypothesis of Lemma 4.5;
 (G) every pinned group containing a kind-(iv) row has V_G = tangent space (affine, or robust Jacobian: Lemma 5.3);
 (B) for every block m: if m has a two-sided peak resource, all K^- rows of m or all K^+ rows of m are controlled (Definition 3.3); if m has
     only a kappa-raising lever, all its K^- rows are controlled; if only a kappa-lowering lever, all its K^+ rows are controlled.
Then Step A is realized.
Proof.  Lemma 4.3 with G_c := the margin levers of the controlled pinned rows.  Suppose (4.1) holds for some z*.  Since 0 is in D_h,
sum_l cap_l (z*^T g_l^-)_- < phi_{z*} + rho_0^max, and (z*^T g_l^-)_- >= eff_l (z*_l)_+ - O((mu_s^2 theta_0 + v^2)|z*|).  By Lemma 4.4: S_naff
is restricted by (G) to groups of kind-(i) rows (see below); |S_res| <= Des^C beta(b)/u (start values of tiny polynomials <= beta(b), Part III
(QC4); |mu| <= Des^C/u by V2 Lemma H for robust minors (least nonzero minor >= u/2), resp. the robust Jacobian); |S_prot| <= Des^C (eps + e_1 +
e_3 + c_MS) eta'/u^3 <= Des^{C - C_A} eta' + Des^C c_MS eta'/u^3 + (terms <= Des^C b eta'/u^3) by (S) and Lemma 4.5 (eps <= 4 u^3 Des^{-C_A},
e_1 <= (eps Des + C theta_0) Des + e_X, theta_0 <= b, e_X <= C Des^4 b^2), or <= 0 for blocks whose statuses are not lowered; the error
terms are <= c_MS Des^C eta'/u + Des^C u^{-2} eta'^2.  So phi_{z*} + rho_0^max <= Des^{C}(Des^{-C_A} eta' + beta(b)/u + c_MS eta'/u^3 + rho_0^max)
<= cap_min eff_min u Des^{C - C_m}, and (z*_l)_+ <= u Des^{C - C_m} on every margin-levered row; with z*_l >= -e_1 these rows carry |z*_l| <=
u Des^{C - C_m}, which the case analysis below needs (it loses a factor Des^{C_3 + C_4}|Lambda_A|^2/u; take C_m large).  Pinned groups of kind-(i) rows only
contribute to S_naff at most ||nu|_G|| ||rc - rt_0|| <= Des^C (eps Des^2 + e_X + c_MS) eta' (z* is small on kind-(i) rows), which is absorbed.  Free controlled rows: the bounds of Theorem H2.A'.  The per-block case analysis of Theorem H2.A', run with "controlled" in place
of "free and not locked", bounds z*_l on every kind-(iv) row by c_1/(16|Lambda_A|), against Proposition 3.1(a) for z*.  QED
Numerics N2 (G2_work/n2_margin_model.py; one (U)-block, exact one-signed resonance, A-regularity tested by LP at all vertices of the
l_inf ball): restricted model without capped resource: NOT A-regular in 300/300; with margin levers of capacity 4(rho_0 + max|b_P|):
A-regular in 300/300; with two random shared two-sided generators instead (hypothesis of Proposition 4.7 violated): A-regular in 299/300.

PROPOSITION 4.7 (= EX: exact one-signed resonances obstruct A-regularity).  PROVED (restricted linear model).  Let m be a (U)-block with
a two-sided peak resource, G an internal affine pinned group with kind-(iv) rows P and kind-(i) rows Q, tiny minors M_i(r) = sum_l C_{il} r_l
(homogeneous linear in r^{(m)}) with M(rc) = 0, and mu a one-signed form ((mu^T C')_P >= 0 oriented, not all 0; (mu^T C')_Q = 0).  If every
generator acts on the rows of G by a vector of span{e_l (l in P, upward only), +-e_l (l in Q), +-rt^G} ⊕ (C'^T mu)^perp and there is no
capped downward resource, then Step A is NOT A-regular at any admissible targets rt' with rt'^G in Z_G.
Proof.  y := C'^T mu/||C'^T mu|| on G, 0 elsewhere: y^T e_l >= 0 (P), = 0 (Q), y^T rt^G = mu^T M(rt)/||.|| = 0 on Z_G (homogeneity), y annihilates
(C'^T mu)^perp; so y^T g >= 0 for every generator.  phi_y(rt') = kappa_m mu^T (M(rc) - M(rt'))/||.|| = 0.  b'' := b(rt') - rho_0 y is in B(b, rho_0)
with y^T b'' = -rho_0 < 0 <= min over (W/2)Q of y^T sigma.  QED
Remark.  In the real system a TS generator at a thick design-depth coordinate s acts on y by eff_s (Psi_y(s) - kappa_y a_s) and FR/ZD
generators by eff_s Psi_y(s): y = C'^T mu/||.|| is a near-certificate only if a satisfies the normal form a_s = Psi_y(s)/kappa_y + O(eps Des) at
thick s and Psi_y vanishes at free/ZD design-depth coordinates (kappa_y <= -c_* is then automatic).  These coincidences are part of the
residual description; granted them, the SIZE of the resonance plays no role.

COROLLARY 4.8 (counting cannot exclude (R1)).  PROVED (as statements about the method).  (a) An exact resonance P(r(f)) = 0 is tiny at
every sub-window, so no pigeonhole over sub-windows or classes based on the tiny/robust dichotomy removes it, and by Proposition 4.7 it
obstructs A-regularity (in that model) at every clean sub-window where its kind-(iv) rows are pinned and have no capped downward resource;
the preparation bias of H2 Lemma 5.2 is not needed for this.  (b) In that model a wrong-signed resonance obstructs at every sub-window where
it is tiny, whatever its size, i.e. at every sub-window coarser than the one its value spoils: the "fresh resonance per sub-window" count
suggested by the task does not hold.  (c) Memory (Lemma 4.1, H2 Lemmas 2.6, 2.7) gives freshness of CARRIERS, not of resonance values, and the
supply of carriers is unbounded (one new coarse carrier per block and level).  Hence the counting/pigeonhole route, as a proof that
fresh resonances cannot occur at all large stages, is FALSE as a strategy; the obstruction must be removed by a resource (Theorem ML) or a
different realization.  Proof: (a) |0| <= b(w) for all w; (b) the proof of Proposition 4.7 uses only the sign of mu^T M(rc) (and the right
sign below rho_0 ||C'^T mu||/kappa_m still obstructs, H2-ref B.9); (c) H2 Lemma 2.7(b).  QED

THEOREM 4.9 (= R1-P: the persistent (R1) residual).  PROVED (mod chain, (K1-depth), and (D-abs) mod H2-ref B.10 + Lemma 4.1).  Design
T_fin^{K2} with (FC), P-TU, F-2, (D-enum), (D-abs).  If at all main stages L >= L_0 every clean sub-window and class is an (R1) stage at which
Step A is not realized, then at every such sub-window and class one of the following holds:
 (P-prot) some SHIFTED block (Lemma 4.5(a) covers (U)-blocks) has a protected status lowered from the start row to the targets and no
          movable kind-(i)/two-sided-inactive/K^- row of robust ratio seen by all its protected statuses;
 (P-naff) some kind-(iv) row is pinned in a non-affine group whose Jacobian is not robust at the targets (singular point of its zero set);
 (P-res) some block is residual in the sense of Theorem H2.A' with "controlled" as in Definition 3.3: (two) an uncontrolled K^- row and an
          uncontrolled K^+ row; (up) an uncontrolled K^- row; (down) an uncontrolled K^+ row.  An uncontrolled K^- row is a pinned row
          WITHOUT a margin lever (deep-swallowed: no pullable coordinate of S_l at depths v in [cap_min/2, c_0 W], and none of capacity
          >= 4W' in [c_0 W, x''_max] by H2 (U')); an uncontrolled K^+ row is such a pinned row or a locked row.
Moreover, in every round range, at all (R1) main stages outside at most N (the (up)/(down) events), (P-res) is of type (two), so it involves
a deep-swallowed pinned K^- carrier, which is FRESH (not of kind (iv) at any earlier (R1) main stage of the range).
Proof.  Contrapositive of Theorem ML ((S), (G), (B) are the negations of (P-prot), (P-naff), (P-res)); Lemma 4.1 for the events and the
freshness.  QED
Remarks.  (1) In (P-res) the residual also carries the normal form of Theorem III-Aobs (4): at every thick design-depth coordinate s,
a_s = Psi_{z*}(s)/kappa_{z*} + O(eps Des); inactive carriers are kind (i) and contribute O(eps Des^2), so at a fixed thick coordinate the fresh
active carriers and the peaks of every stage must reproduce kappa_{z*} a_s.  Compatible with (D-enum) and pool density: no contradiction.
(2) The margin-lever depth range is [eta' Des^{-C}, Des^C eta'/u^3] (coordinates j ~ 4 log_2(1/T) +- O(log Des)), just below the Step-A pull
range [c_0 W, x''_max] (j between about 2 and 5 log_2(1/T)), and far shallower than H2 5.3's Sys-DC scale r <= exp(C log^2(1/T)) s_1.  At the
next (R1) main stage these coordinates are super-thin (H2 Lemma 2.3: they lie below s_max(p+1) >= 4/T_lo), which constrains only the old
carriers.  (3) Nothing proved here excludes (P-prot), (P-naff) or (P-res) at all large stages: (R1) persistence is OPEN.

## 5. (R0): joint readings, non-affine groups, thick peaks of shifted blocks, peak conversion (details: G2_part4.md)
Thick row = thick-type row with robust or near-threshold status.

LEMMA 5.1 (alignment of hull elements).  PROVED (mod chain).  For z in conv(Y) and every thick row l: z_l rt_l = kappa_z rho_l u_l(xhat_1)/kappa_m
+ O(eps Des^2 + Des(eta' + b) + C b^2 D^2) with kappa_z in [-C, -c_*/nu_1]; so sgn(z_l rt_l) = -sgn(rho_l u_l(xhat_1)) and |z_l rt_l| >= c_* u^2
Phi_l/(2 nu_1 m K).  Proof: Lemma AL is a linear approximate identity (Lemma 1.1(d)).  QED

THEOREM 5.2 (= R0-J: the (R0) residual in joint form).  PROVED (mod chain).  If Step A is not realized at a stage with a thick-type carrier,
then with z*, lambda, nu, mu of Theorem JF:
 (a) [(U)-blocks with a private two-sided peak resource] Lambda_m <= Des^C (eps + c_MS) (Lemma 4.5(a)); there is no movable thick row (by (JF1)
     kappa_m z*_l rt_l = lambda_l 1[l in N] + 2 kappa'_m m^2 rt_l^2 Lambda_m + O(c_MS) would be small, against Lemma 5.1); every (U)-piece G ∩ m,
     whatever its rows (thick, kind (i), kind (iv)), is balanced for z*: |kappa_{z*} Xi_{G∩m}/kappa_m + sum_{(iv) l in G∩m} z*_l rt_l| <= Des^C
     (eps + c_MS) + small, the kind-(iv) terms being >= -e_1|rt_l| on K^+ and <= e_1|rt_l| on K^- rows.  [H1-ref's (H-3') extended to objects
     containing non-thick kind-(iv) rows, for one vector z*.]
 (b) [(U)-blocks without a peak resource] sigma_m = sgn(rho_c vs_c) common to the (thick-type) peaks; sigma_m = -1 is realized (Theorem RL =
     the displacement -delta rt^{(m)} in D_h); if sigma_m = +1: sum_{d in N ∩ m} lambda_d (1 + 2 kappa'_m R^2_{(d)}) = kappa_m zeta_m(z*) + O(c_MS)
     >= kappa_m c_* u/(4 nu_1) - O(c_MS) > 0 (the block is protected), and every movable row of robust ratio has kappa_m z*_l rt_l = lambda_l
     1[l in N] + 2 kappa'_m m^2 rt_l^2 Lambda_m + O(c_MS): an anti-aligned thick row or an active K^+ kind-(iv) row carrying that weight.
 (c) [shifted blocks] (JF1)-(JF3); every movable thick row is anti-aligned (aligned ones are relieved inward) with z*_l/rt_l = (lambda_l 1[l in
     N]/rt_l^2 + 2 kappa'_m m^2 Lambda_m)/kappa_m + O(c_MS/(rbar_l |rt_l|)) -- for unprotected robust rows the common value 2 kappa'_m m^2
     Lambda_m/kappa_m, i.e. H1's anti-aligned proportional resonance (z*_l rt_l being fixed by Lemma 5.1); thick-type robust peaks force
     sigma_m = sgn(Delta''_m) and no two-sided peak resource (Lemma NP'); if rt^{(m)} is in V, sigma_m = -1 is relieved by down-scaling.
 (d) [pinned groups] (JF2) on groups with V_G = tangent space (affine or robust Jacobian); (JF3) only on non-affine groups at singular targets.
 (e) phi_{z*}(rt_0) > -rho_0^max, with the decomposition of Lemma 4.4.
Proof.  (a) Lemma 4.5(a), (JF1), Lemma 5.1; pieces: (JF3)/(JF2) paired with the piece vector, kind (i) small, kind (iv) signs from z*_l >= -e_1.
(b) Lemma NP (linear); pair (2.2) with rt^{(m)} in V as in Lemma 4.5(a), zeta_m(z*) of sign sigma_m and modulus >= c_* u/(4 nu_1); (JF1).
(c) (JF1), Lemma 5.1, Lemma NP'.  (d) Theorem JF and Lemma 5.3.  (e) Lemma MS(b).  QED

LEMMA 5.3 (= NL: tangent levers of non-affine groups with a robust Jacobian).  PROVED.  Let the tiny polynomials P_1, ..., P_q of a pinned
group G be C^2 functions of r^G (other groups fixed; minors and cofactor polynomials are polynomials; (X4^0)-minors are Nash functions, K
being Nash on the W-fix region) with ||D^2 P_i|| <= Des^C, and suppose the Jacobian J := (grad_G P_i(rt_0))_i has full row rank with smallest
singular value s_J >= u^{C_J} Des^{-C_J}; s_max := ||J|| <= Des^C.  If Delta in ker J and ||Delta|| <= h with q^{1/2} Des^C h s_max <= s_J^2/8, there
is E(Delta) = J^T xi in (ker J)^perp, continuous in Delta, with ||E(Delta)|| <= q^{1/2} Des^C s_max ||Delta||^2/s_J^2 and rt_0^G + Delta + E(Delta) in
Z_G exactly.
Proof.  F(xi) := P(rt_0 + Delta + J^T xi).  F(0) = P(rt_0) + J Delta + R_2 = R_2, ||R_2|| <= q^{1/2} Des^C ||Delta||^2/2.  The map Phi(xi) := xi -
(J J^T)^{-1} F(xi) has D Phi = (J J^T)^{-1}(J - J(r)) J^T with ||J(r) - J|| <= q^{1/2} Des^C (||Delta|| + s_max ||xi||) (Lipschitz gradients), so
||D Phi|| <= 1/2 on {||xi|| <= 2||R_2||/s_J^2} under the hypothesis on h (h tiny makes s_max ||xi|| <= ||Delta||); Phi maps this ball into itself
(||Phi(0)|| <= ||R_2||/s_J^2) and is a contraction; its fixed point solves F = 0; continuity from the uniform contraction.  QED
Use.  Adding ker J to V with the exactification map Delta -> Delta + E(Delta) changes every pairing by <= ||kappa y|| ||E|| <= Des^C u^{-C}
h_max^2 <= Des^C u^{-C} eta'^2, which is added to rho_0^max in Lemmas MS, 4.3, 4.4 (it is << x).  Robust Jacobians can be made a rate object
(the minors of J are design-countable N-free polynomials of the pattern; V2's exactification makes the tiny ones exactly zero at the
targets), so (H-6')'s non-affine part reduces to groups at SINGULAR targets (rank-deficient J), where only (U)-piece scalings remain.

PROPOSITION 5.4 (where peak conversion is needed).  PROVED (mod chain).  In a (U)-block with a private two-sided peak resource no protected
movable thick row is anti-aligned at a residual stage (Theorem 5.2(a): Lambda_m ~ 0, while an anti-aligned movable row needs lambda_l + 2 kappa'
m^2 rt_l^2 Lambda_m = kappa_m z*_l rt_l robustly positive).  So peak conversion (H1 7) is needed only in (U)-blocks without peak resource with
sigma_m = +1 and in shifted blocks.
LEMMA 5.5 (frozen consistency of a converted peak).  PROVED (mod J2.1).  Freeze a coarse non-peak d of block m as a PEAK (block scalars of
Step A with P_f := P_rob ∪ {d}) and add the band row rho_d in [1 + beta_*, 1 + 3 beta_*].  The frozen system is C^{1,1} on the Brouwer domain
with the constants of J2.1(b) (|d Psi_f/d theta| >= 2 theta_f Phi_{P_rob}^2; zeta_d != 0 near the realized point), and at a realized point
satisfying the band row and the other targets it coincides with the true system (J2.1(c)).  At rho_d = 1 the descriptions with d in P_f and
with d in Omega give the same a_f^2 = sigma_f + k_f^2 R^2 (the contribution rho_d^2 Phi_d^2 = Phi_d^2 moves from k^2 R^2 to sigma), so the other
statuses are continuous across the conversion, |Delta log rho_k| <= C D^C (rho_d - 1) Phi_d^2.  [This closes gap (i) of H1-ref C.6.]
Proof.  J2.1(a)-(c) need only P_f nonempty with zeta != 0 on P_f; the Jacobian bound uses P_rob ⊂ P_f; consistency from the band row and the
protected statuses; continuity from J2.1(d) (k = a + sigma, a^2 = sigma + k^2 R^2) with (P_f, Omega) changed by d.  QED
PEAK CONVERSION: SKETCH, two precise gaps (OPEN).  (G1) The conversion changes the other protected statuses by O(beta_* Phi_d^2), beta_* ~ Des^C
x/u, above their margins eta'/Des unless compensated; the compensating down-scaling pairs by -delta kappa_m zeta_m(z*) < 0 when sigma_m = +1,
of the same order beta_* as the conversion's relief: an f-dependent comparison of |z*_d rt_d| with zeta_m(z*).  (G2) Downstream legitimacy of
a zero-data weak peak of margin ~beta_* at the companion (U1 Proposition 2.2(a)'s peak-error term, CM'(a)'s screening) is not re-derived.

## 6. Numerics (sanity only; r14/G2_work/)
 N1 n1_status_calculus.py (.out), n1b_secondorder.py (.out): Lemma 3.1' with the true Lemma-K function on 3657 random blocks: first-order
    status changes along inward, partner-coupled and scaling-coupled directions <= 0 up to rounding (max 1.1e-13); second-order constant <=
    0.56 (<= 3.6 in the n1b sampling up to the W-fix boundary).
 N2 n2_margin_model.py (.out): Proposition 4.7 and Theorem ML's mechanism in a (U)-block model: 300/300 not A-regular without capped
    resource, 300/300 A-regular with margin levers, 299/300 A-regular with two random shared two-sided generators (the restricted
    hypothesis matters; in the real system TS/FR/ZD generators impose the normal form instead).
 N3 n3_minimax_lp.py (.out): minimax identity of Lemma MS and LP duality (2.2) to <= 9e-14 on 400 random instances.
 Finite models cannot test the infinite-dimensional mechanisms (memory, swallowing, normal form); those rest on the proofs.

## 7. What remains open; main obstacle; next steps
OPEN (precise).
 (R1) at all large main stages: Theorem 4.9's classes (P-prot), (P-naff), (P-res); outside at most N events per round range (P-res) needs a
      FRESH deep-swallowed pinned K^- kind-(iv) carrier (no pullable coordinate at depths [cap_min/2, x''_max]) in a one-signed (possibly
      exact) resonance with the normal form of Theorem III-Aobs (4).
 (R0) at all large main stages: Theorem 5.2's coincidence classes -- balanced (U)-pieces (now including kind-(iv) rows), the sigma_m = +1
      multiplier identity of (U)-blocks without peak resource, anti-aligned proportional resonances and sigma_m = sgn(Delta''_m) thick
      peaks in shifted blocks, non-affine groups at singular targets -- plus (H-7) (frozen far windows, no private two-sided design-depth
      resource, tiny spreads), and peak conversion's gaps G1, G2.
 Inherited: the once-refereed links of the chain; (K1-depth) (inspection claim); (D-abs) consequences (H2-ref B.10).
 (LSC-trunc)_N for every f; density of NA((c_0, p_N), l_2^2) for any N; density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.
MAIN OBSTACLE.  One-sidedness at the error scale of the realization.  The obstruction of a pinned kind-(iv) group is not the size of its
resonance (Corollary 4.8): once the realization's errors (rho_0, c_MS eta', S_prot) are taken into account, ANY one-signed resonance -- exact
ones included -- blocks A-regularity unless the pinned rows have a downward resource of capacity ~ eta' Des^{-C}.  Such a resource is a pull
at a pullable coordinate just below the Step-A pull range (Theorem ML); rows that are anti-sign-swallowed over the whole depth range
[cap_min/2, x''_max] at every stage, with fresh carriers, are what remains.  Memory forbids reusing carriers but not renewing them.
NEXT STEPS.  (1) For deep-swallowed pinned rows: a downward resource that is not a private pull -- e.g. a SHARED pull at a target coordinate
used by the whole resonance group (its first-order action is a cofactor-weighted combination; for a one-signed form it lowers the form iff
the coordinate's evaluation vector pairs positively with C'^T mu), or a realization that solves the pinned group's exactness AFTER the other
moves (two-stage Brouwer with the pinned rows' second-order drift computed, so that only rho_0-scale corrections remain).  (2) For (P-prot):
show that a shifted block whose protected statuses must descend has a movable kind-(i)/K^- row of robust ratio (or a one-sided kappa
lever of the right direction) at clean sub-windows, or design one (a private (i)-type lever row per block that is never pinned).
(3) Test G3's persistent residual rows against Theorem ML: compute whether their pinned kind-(iv) carriers are deep-swallowed in
[cap_min/2, x''_max]; if not, Theorem ML already covers them.  (4) (R0): a minimax version of H1's alignment calculus with the hull element
of Lemma MS and the margin idea for near-threshold anti-aligned rows (replacing peak conversion).
No counterexample is claimed, and nothing found here suggests one.
