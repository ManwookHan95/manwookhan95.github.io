# G2 part 1: the minimax target lemma over the certificate hull, and the joint Farkas form of the residual

Setting and notation: r13/H1_notes 1, r13/H2_notes 1, Part III Subsection 5.6 (Definition III-SysA, III-Areg, Lemma III-cone,
Theorem III-Aobs).  Design T_fin^{K2} with (FC) (J2 2.2), P-TU windows, F-2, (D-enum); N >= 1; f in S_{p_N*}; g in C(f); rho in (0,1);
main stage L >= l_f, clean sub-window w, class a; b, u, T, eta', x = C Design(L) eta', D = D(L).  Step A at admissible targets rt
(J1.13 (i)-(ii)): rows l in Lambda_A, Ft_l(rt) = val_l - rt_l kappa_{m(l)}, b(rt) = -Ft(rt), generator set G = G(rt), near-certificates.
"PROVED (mod chain)" = modulo the refereed chain cited by J1.15' and J2.1 (as in H1/H2), plus H1-ref's Lemma SLP / Lemma PC.

## 1.1 Linear properties of near-certificates (bookkeeping lemma)

LEMMA 1.1 (linearity).  PROVED (mod chain).  Fix the stage and the targets rt_0.  Let eps_1 := eps_* (the size used in Lemma TF').
(a) The common-mode functional is linear: gamma(y) := <U^* Psi^A_y, e_1> = y^T gt^A (Lemma III-Euler(c)), with ||gt^A||_2 <= Design^{C_g}.
(b) Every near-certificate y of size <= eps_1 satisfies gamma(y) <= -c_* (Theorem III-Aobs(3); at (R1) stages kappa_y <= -c_1/(8H(L)),
    H2 Fact 1.2).
(c) Let Y := {y : ||y||_2 = 1, y^T g >= -eps_1 for all g in G} and z in conv(Y).  Then ||z||_2 >= c_*/Design^{C_g}, z^T g >= -eps_1 for
    all g in G, gamma(z) <= -c_*, and z/||z||_2 is a near-certificate of size <= eps_1 Design^{C_g}/c_*.
(d) Every conclusion of the structure theory that is a LINEAR inequality or a linear approximate identity in y with an error bound
    independent of y holds for every z in conv(Y) with the same error bound.  This includes: Theorem III-Aobs (2), (2a)-(2c), (4)-(6)
    in the form c_s(Psi_z) >= -eps Design etc.; J1.6(a): coef_k(z) = kappa_z rho_k + O(eps Design^2) on thick-type carriers with
    kappa_z := gamma(z)/nu_1; Lemma AL: z_l rt_l = kappa_z rho_l u_l(xhat_1)/kappa_m + O(...); J1-ref R-PK |zeta_m(z)| <= (4/3) eps Design in
    blocks with a private two-sided peak resource; Lemma NP(b): sgn zeta_m(z) = sigma_m and |zeta_m(z)| >= c_* u/(4 nu_1); H2 (1.2):
    z_l >= -e_1 on kind-(iv) rows; H2 Proposition 3.1(a) sum_{(iv)} z_l >= c_1/4, 3.1(b) (per-block lever balance), 3.1(c).
Proof.  (a) Psi^A_y = sum_l y_l eps_l u_l - sum_m beta^A_m K_m with beta^A_m = sum_{l in m} y_l rt_l is linear in y, hence so is gamma.
The bound on gt^A: |g_l| <= ||U|| ||u_l||_{l_1} <= C and |rt_l G^A_m| <= Design^{C_4} ||K_m||_{l_1} <= Design^C; |Lambda_A| <= Design.
(b) is cited.  (c) z = sum_i theta_i y_i (theta_i >= 0, sum = 1): the constraints y^T g >= -eps_1 are preserved by convex combinations;
gamma(z) = sum theta_i gamma(y_i) <= -c_*; c_* <= |gamma(z)| <= ||gt^A|| ||z||.  Normalizing multiplies the size by 1/||z||.
(d) Each listed statement is of the form "Lin(y) >= -E" or "|Lin(y) - kappa_y Q| <= E" with Lin linear in y and E independent of y; both
forms are preserved by convex combinations (for the second: |sum theta_i (Lin(y_i) - kappa_{y_i} Q)| <= sum theta_i E = E, and
kappa_z = sum theta_i kappa_{y_i}).  Lemma NP(b): sgn zeta_m(y_i) = sigma_m for all i and |zeta_m(y_i)| >= z_0, so the same holds for z.
For statements proved for near-certificates of size <= eps_* that are applied to z/||z|| (size <= eps_1 Design^{C_g}/c_*), take the design
constant C in eps_* = u^3 Design^{-C} larger by C_g + 1 (c_* >= Design^{-1}); this changes no other step.  QED

## 1.2 The admissible displacement space

DEFINITION 1.2.  At the targets rt_0 let:
 (V1) MOV := the movable rows (inactive rows, incl. holds/D2/KN-pushed rows, and active rows with a FREE ratio: in no tiny minor and no tiny
      cofactor polynomial, J1.13);
 (V2) for every pinned group G (connected component of the linking graph of pinned active ratios, H1 GS): V_G := the tangent space of the
      zero set of G's tiny polynomials if all of them are AFFINE functions of r^G (the other groups' ratios being fixed) -- e.g. single-block
      groups whose tiny polynomials are minors avoiding (X4^0) rows (H1-ref D.1), or (U)-block internal minors-only groups (H1 TG);
      otherwise V_G := span{rt_0^{G ∩ m} : m a (U)-block} (piece scalings, H1-ref Lemma PC);
 V := span{e_l : l in MOV} ⊕ (⊕_G V_G)   (direct sum: groups and MOV are disjoint sets of coordinates).
 N := the protected rows (near-threshold actives incl. (FC)-frozen weak peaks of all blocks, D2/KN-pushed rows; in (T)-blocks the carriers
      of N(m) with their Puiseux statuses).  For d in N of block m:  l_d(Delta) := Delta_d/rt_{0,d} + kappa'_m dR^2_{(d)}(Delta), where
      dR^2_{(d)}(Delta) := 2 m^2 sum_{l in Omega_{(d)}} rt_{0,l} Delta_l, Omega_{(d)} = Omega(m) (route V: all coarse non-P_rob carriers of m), or
      the active set of m when d is a Puiseux-protected carrier of a (T)-block (psi_d = m|r_d| K(sigma_rob, R_a^2)); kappa'_m := d log K/d R^2
      in (0, C D^C] (Lemma K); the term Delta_d/rt_{0,d} is absent if d is not displaced or rt_{0,d} = 0.
 rbar_l := max(|rt_{0,l}|, u Design^{-C_3}) and ||Delta||_rt := max_l |Delta_l|/rbar_l.
 D_h := {Delta in V : l_d(Delta) <= 0 for all d in N, ||Delta||_rt <= h}   (a compact convex polytope; D_h = h D_1).

LEMMA 1.3 (exactness and legitimacy of the displacements).  PROVED (mod chain).  Let h <= h_max := Design^{C_h} u^{-4} (||b(rt_0)|| + x)
(C_h absolute, as in H1-ref P-TF) and Delta in D_h.  Then:
 (a) [Z_kappa] the target vector rt' := E(rt_0, Delta) is an exact point of Z_kappa, where E acts groupwise: on MOV and on affine groups
     rt'^G = rt_0^G + Delta^G; on a non-affine group with Delta^G = sum_m (s_m - 1) rt_0^{G ∩ m}, rt'^{G ∩ m} = s_m rt_0^{G ∩ m}; so rt' - rt_0 =
     Delta exactly; every robust minor changes by <= Design^C h << u;
 (b) [statuses] every protected status satisfies log rho_d(rt') <= log rho_d(rt_0) + C Design^C h^2, and C Design^C h^2 << eta'/(12 Design)
     (the slack of every protected status at the targets, as in H1-ref SLP (a)); robust statuses, robust peaks and nearly neutral statuses move
     by <= Design^C h << u, resp. stay <= 2b;
 (c) [data] the class data projected at the realized ratios meet J1.13 (i)-(iii) (violations <= Design^C u^{-C} x/t << K t);
 (d) [size] ||kappa (rt' - rt_0)|| <= Design^C h_max, the size allowed by Lemma TF' with H1-ref P-TF (x_TU enlarged by one absolute power).
Proof.  (a) Each tiny polynomial involves the ratios of exactly one group (definition of groups) and no movable row.  Affine groups:
P(rt_0^G + Delta^G) = P(rt_0^G) + dP(Delta^G) = 0 for Delta^G in the tangent space (P affine).  Non-affine groups: H1-ref Lemma PC gives
P(.., s_m r^{(m)}, ..) = s_m^{e_m(P)} P(..) separately for each (U)-block m (the other blocks' ratios are parameters), so the scaled point is in
Z_kappa; and s_m rt_0^{G ∩ m} - rt_0^{G ∩ m} = (s_m - 1) rt_0^{G ∩ m} is exactly the prescribed displacement.  Robust minors are polynomials
with Design^C coefficients on the compact W-fix region.  (b) Lemma K: log rho_d = log(m |r_d|/Phi_d) + log K(sigma, R^2) with sigma depending on
the frozen pattern only (X1 1.1, J2.1(d)); the first-order change is l_d(Delta) <= 0 and the second derivatives of log|r_d| (|r_d| >= u
Design^{-C}) and of log K (K Nash on the W-fix region) are <= Design^C; ||Delta||_rt <= h gives the bound.  h^2 Design^C <= Design^C u^{-8}
(||b|| + x)^2 <= Design^C u^{-8} Design^{2C} eta'^2 << eta'/Design since eta' <= (u/(4 Design))^{4L^2 + 80}.  The slack statement is H1-ref
SLP (a) ((U)-blocks: targets <= 1 - eta' vs <= 1 - eta'/2 required; (T): Puiseux margin mu >= eta'/(3 Design) by J1.11; D2/KN pushes likewise --
for (KN)-blocks see Remark 1.8).  (c) As in H1 Theorem IN (the original data violate the moved (X3)/(X1)/(X4^0) rows by <= ||rt' - rt_0||
||gamma|| <= Design^C h/t).  (d) Definition of h_max.  QED

## 1.3 The minimax target lemma

LEMMA MS (minimax over the certificate hull).  PROVED (mod chain).  With Y as in Lemma 1.1 and h := h_max put
      Phi(Delta, y) := <kappa y, Delta> - phi_y(rt_0),     <kappa y, Delta> := sum_l kappa_{m(l)} y_l Delta_l,   phi_y(rt_0) = y^T Ft(rt_0),
      V_MS := max_{Delta in D_h} min_{y in Y} Phi(Delta, y).
 (a) If V_MS >= x/4, Step A is realized at the targets rt' = E(rt_0, Delta*) (Delta* a maximizer): A-regular, exact on Z_kappa, statuses
     protected, data projected at the realized ratios.
 (b) If V_MS < x/4, there is z* in conv(Y) with
        max_{Delta in D_1} <kappa z*, Delta>  <  c_MS := (||b(rt_0)|| + x/2)/h_max  <=  u^4 Design^{-C_h} ,                       (1.1)
        phi_{z*}(rt_0)  >  -x/4 ,                                                                                                    (1.2)
     and z* has every property of Lemma 1.1(c), (d).
 (c) [dual form of (1.1)] There are lambda in R^N_{>=0} and nu in V^perp with
        sum_l rbar_l | kappa_{m(l)} z*_l - (A^T lambda)_l - nu_l |  <  c_MS ,      (A^T lambda)_l := sum_{d in N} lambda_d (a_d)_l ,          (1.3)
     where a_d is the coefficient vector of l_d: (a_d)_l = 1[l = d]/rt_{0,d} + 2 kappa'_{m(d)} m(d)^2 rt_{0,l} 1[l in Omega_{(d)}].
Proof.  (a) Lemma 1.3 gives admissibility and the size bound of Lemma TF'.  Suppose Step A at rt' were not A-regular.  Lemma III-cone(b)
(K2.9(b)) gives a unit y, a near-certificate at rt' of size < 4 Design^{-C_A} u^3, with phi_y(rt') > -rho_0(rt').  The generator columns are
Lipschitz in the targets with constant C_G <= Design^C (J1-ref P-1; peak columns -(1 - X) lambda_c rt^{(m)}, gt-terms), and C_G ||rt' - rt_0||
<= eps_1/2, so y is in Y.  Since Ft(rt') = Ft(rt_0) - kappa (rt' - rt_0) and rt' - rt_0 = Delta* (Lemma 1.3(a)): phi_y(rt') = phi_y(rt_0) -
<kappa y, Delta*> = -Phi(Delta*, y) <= -V_MS <= -x/4 <= -rho_0(rt') (rho_0(rt') <= x/4 as in the proof of Lemma TF', using Lemma 1.3(d)):
contradiction.  Realization then follows from Lemma III-cone(c) for the (FC)-frozen map (J2.1 (ii)-(iii)).
(b) Phi is affine in Delta for fixed y and affine in y for fixed Delta; D_h and conv(Y) are compact and convex.  By von Neumann's minimax
theorem (in Sion's form), max_{Delta in D_h} min_{y in conv Y} Phi = min_{y in conv Y} max_{Delta in D_h} Phi, and for fixed Delta the minimum
of the affine function y -> Phi(Delta, y) over conv(Y) is attained on Y.  So V_MS = min_{z in conv Y} max_{Delta in D_h} Phi(Delta, z), and a
minimizer z* has max_{Delta in D_h} Phi(Delta, z*) = V_MS < x/4.  Taking Delta = 0 gives (1.2).  Since D_h = h D_1 and |phi_{z*}(rt_0)| <=
||z*|| ||Ft(rt_0)|| <= ||b(rt_0)||: h max_{D_1} <kappa z*, Delta> < x/4 + ||b(rt_0)||, which is (1.1).  The bound c_MS <= u^4 Design^{-C_h}
is the definition of h_max.  The properties of z* are Lemma 1.1.
(c) LP duality for the primal max{c^T Delta : Delta in V, A Delta <= 0, -rbar <= Delta <= rbar} with c := (kappa_{m(l)} z*_l)_l (feasible
at Delta = 0, bounded): introduce multipliers lambda >= 0 for A Delta <= 0 and nu in V^perp for the constraint Delta in V; the dual function
is max over the box of (c - A^T lambda - nu)^T Delta = sum_l rbar_l |c - A^T lambda - nu|_l, and strong LP duality gives equality of the
optimal values.  (1.1) bounds the primal value by c_MS.  QED

REMARK 1.4 (what the minimax adds).  (i) H1-ref's Lemma SLP is the special case in which every object consists of thick-type and kind-(i)
rows: then <kappa z, Delta> = kappa_z (Xi . delta) + small for EVERY z in conv(Y) (Lemma AL is linear; kappa_z in [-C, -c_*/nu_1]), and (1.3)
restricted to the object directions is SLP's (*).  (ii) Objects containing NON-THICK kind-(iv) rows (certificate-dependent coefficients),
pieces of non-affine groups, D2/KN/held rows and any combination of blocks are now covered: the residual is ONE vector z* -- a convex
combination of near-certificates -- for which every coefficient is a number; all sign information of the certificates that is linear
(z_l >= -e_1 on kind (iv), sum_{(iv)} z_l >= c_1/4, per-block lever balance, Lemma AL, NP, R-PK) is retained.  (iii) Every lever of H1 (TF', IN,
OUT, GS, DS, UC, RL, KC, TG) and of H2 (bands on free K^- rows; bands on free K^+ rows in (U)-blocks with the F-2 rescaling; Lemma 3.4(b);
Lemma 3.4(c) as proved in Part 2) is a displacement in D_h up to second-order terms (the exchange of OUT(b) is R^2-neutral to first order;
the coupled forms are in Part 2), so a stage not realized by Lemma MS(a) is not realized by any of these levers either; conversely Lemma MS(b)
is the exact dual residual of ALL first-order status-safe exactly-admissible target displacements at once.

## 1.4 The joint Farkas form (all blocks at once; shared generators; shifted blocks)

THEOREM JF (joint Farkas form of a non-realized stage).  PROVED (mod chain).  If Step A is not realized at the stage (by Lemma MS(a) at the
admissible targets rt_0), there exist z* in conv(Y), lambda >= 0 on N and nu in V^perp such that (1.1)-(1.3) hold, and in addition:
 (JF1) [movable rows] for every l in MOV not in N:  |kappa_m z*_l - 2 kappa'_m m^2 rt_{0,l} Lambda_m^{(l)} | <= c_MS/rbar_l, where
       Lambda_m^{(l)} := sum{lambda_d : d in N, l in Omega_{(d)}} >= 0; for l in MOV ∩ N: kappa_m z*_l = lambda_l/rt_{0,l} + 2 kappa'_m m^2
       rt_{0,l} Lambda_m^{(l)} + O(c_MS/rbar_l).  In particular in an UNPROTECTED block every movable row has |z*_l| <= c_MS/(kappa_m rbar_l).
 (JF2) [affine pinned groups, incl. groups spanning several blocks] for every affine group G there are numbers mu_i (one per tiny
       polynomial P_i of G) with  || (kappa z* - A^T lambda)|_G - sum_i mu_i grad_G P_i ||_{rbar,1} < c_MS  (the normal space of Z_kappa at rt_0
       restricted to G is spanned by the gradients); for (U)-block internal minors-only groups grad_G P_i = Q^{(i)} (constant cofactor vectors).
 (JF3) [non-affine groups] for every (U)-block piece G ∩ m: |sum_{l in G ∩ m} (kappa_m z*_l - (A^T lambda)_l) rt_{0,l}| < c_MS (no information
       on the shifted-block part of a non-affine group).
 (JF4) [certificate structure] z* satisfies every generator inequality z*^T g >= -eps_1 (g in G): this is where SHARED design-depth
       generators at target coordinates (TS/FR/ZD moves acting on all carriers whose targets contain the coordinate), the one-sided peak
       levers of shifted blocks, pre-placed TU levers and all private resources enter; in particular Lemma 1.1(d)'s list, including at (R1)
       stages z*_l >= -e_1 on kind (iv), sum_{(iv)} z*_l >= c_1/4, and per block: |zeta_m(z*)| <= (4/3) eps Design (two-sided peak resource),
       zeta_m(z*) <= (4/3) eps Design (only kappa-raising lever), zeta_m(z*) >= -(4/3) eps Design (only kappa-lowering lever).
 (JF5) [wrong side] phi_{z*}(rt_0) > -x/4, where phi_{z*}(rt_0) = -<kappa z*, rt_0 - rc> and rc := (val_l/kappa_{m(l)})_l are the realized
       ratios of the start row; for an affine group G (all tiny P_i vanish at rt_0^G) the G-part of -<kappa z*, rt_0 - rc> equals
       sum_i mu_i P_i(rc^G) + <(A^T lambda)|_G, rc^G - rt_0^G> + O(c_MS ||rt_0 - rc||_rt).
Proof.  (1.3) splits over the direct sum V = span(MOV) ⊕ (⊕_G V_G): V^perp = (coordinates outside MOV and groups... ) -- precisely, nu
vanishes on MOV (e_l in V), nu|_G is in V_G^perp (within the coordinates of G) for every G, and nu is arbitrary on rows that are neither
movable nor in a group (pinned rows of non-affine groups outside (U)-blocks).  (JF1): nu_l = 0 for l in MOV and the l-th term of (1.3) is
<= c_MS.  (JF2): V_G^perp (within G) is the span of grad_G P_i for affine G (the tangent space is the common kernel of the gradients).
(JF3): V_G = span{rt_0^{G ∩ m}} for non-affine G; nu|_G is orthogonal to each piece vector; pair the residual of (1.3) with rt_0^{G ∩ m}
(|rt_{0,l}| <= rbar_l).  (JF4): Lemma 1.1.  (JF5): (1.2) and Ft(rt_0) = kappa (rc - rt_0); on G, rt_0^G - rc^G is paired with kappa z*|_G =
A^T lambda|_G + sum mu_i grad P_i + err, and grad P_i . (rt_0^G - rc^G) = P_i(rt_0^G) - P_i(rc^G) = -P_i(rc^G) for affine P_i.  QED

COROLLARY JF' (single (U)-block, restricted model = H2 Proposition 4.1, now with status multipliers and shared generators).  PROVED (mod
chain).  In a (U)-block m with a private two-sided peak resource, at an (R1) stage, for an internal affine group G of pinned kind-(iv) rows
P and pinned kind-(i) rows Q of m: with mu from (JF2) and lambda from (JF1), the oriented cofactor form C'_mu := sum_i mu_i grad P_i satisfies
 (C'_mu)_l >= -kappa_m e_1 - (A^T lambda)_l - err_l (l in P),   |(C'_mu)_l| <= kappa_m (eps Design^2 + e_X) + |(A^T lambda)_l| + err_l (l in Q),
and (JF5) gives sum_i mu_i P_i(rc) > -x/4 - (contribution of the other rows of m) - <A^T lambda, rc - rt_0>.  When the block is unprotected
(lambda = 0 on m) this is H2 Proposition 4.1's one-signed linear resonance (nonnegative on oriented kind-(iv) ratios, blind to the two-sided
ones, wrong sign at the start row), now derived for the JOINT system (other blocks, shared generators and multi-block affine groups
present) rather than in P-41's restricted model; the status multipliers lambda >= 0 are the only modification in protected blocks, and they
enter with the sign (A^T lambda)_l = lambda_l/rt_l + 2 kappa'_m m^2 rt_l Lambda_m, i.e. they REINFORCE the outward pull on K^+ rows and the
inward pull on K^- rows (the alignment pattern of H1's Lemma AL).
Proof.  (JF2) with z*_l >= -e_1 on kind (iv) (orientation: rt and the eps-oriented ratios as in H2 1.2), |z*_l| <= eps Design^2 + e_X on
kind (i) (H2 3.1(c)), and (JF5).  QED

## 1.5 Thick-type peaks of shifted blocks

LEMMA NP' (thick-type robust peaks in any block).  PROVED (mod chain).  Let c be a robust coarse peak of a block m (shifted or not) which
is thick-type (a thick private coordinate p in S_c ∩ [1, D]).  Then for every near-certificate y of size <= eps_* (and, by Lemma 1.1(d),
every z in conv(Y)):  zeta_m(y) = -kappa_y rho_c vs_c/(lambda_c (1 - X_m)) + O(eps Design^2/lambda_c), so sgn zeta_m(y) = sigma_m :=
sgn(rho_c vs_c) and |zeta_m(y)| >= c_* u/(4 nu_1); all thick-type robust peaks of m have the same sigma_m and the same rho_c vs_c/lambda_c up to
O(eps Design^2/u).  Consequently Step A is realized (no near-certificate of size <= eps_*) if
 (i) m has a private two-sided peak resource (R-PK: |zeta_m| <= (4/3) eps Design), or
 (ii) m has a one-sided peak lever and sigma_m != sgn(Delta''_m) (H2 Proposition 3.1(b); the lever direction is the same for all robust
      peaks: it raises kappa_m iff Delta''_m < 0), or
 (iii) some thick-type robust peak c has a private S_th coordinate s' carrying data with z_{s'} = sgn a_p (Corollary III-Asuff(d)); its data
      sign is eps_c = -sgn(Delta''_m) vs_c (J2 1.3), so (iii) is again sigma_m != sgn(Delta''_m).
So a residual stage with a thick-type robust peak in a shifted block m has sigma_m = sgn(Delta''_m) and no two-sided peak resource in m.
If moreover the whole-block scaling rt^{(m)} lies in V (no tiny polynomial involves r^{(m)} non-homogeneously -- in a shifted block: every
tiny minor containing (X3)_m has vanishing Delta'-cofactor, and no (X4^0)-minor of m is tiny), then Step A is realized when sigma_m = -1
(down-scaling: pairing -delta kappa_m zeta_m >= delta kappa_m c_* u/(4 nu_1)), or sigma_m = +1 and m is unprotected.
Proof.  The proof of H1 Lemma NP(b) uses Delta'_m = 0 only to show that peaks carry no class data (hence their S_th coordinates are ZD);
the formula for zeta_m uses: c untuned (robust peaks are not Sys-A rows under (FC)), coef_c = -zeta_m lambda_c d kappa_m/d zeta(c) (Part III
5.6), d kappa_m/d zeta(c) = vs_c (1 - X_m) for frozen peaks with 1 - X_m = 1 - a_f s_f/(Phi'^2 (1 + a_f)) in [3/4, 1] (J2.1(d); route V: s_f
contains only fine non-peaks), and coef_c = kappa_y rho_c + O(eps Design^2) (Theorem III-Aobs (2b) at the thick private p, valid for any coarse
carrier).  Two such peaks share zeta_m and 1 - X_m.  (i) contradicts the lower bound; (ii) contradicts the one-sided balance when
sigma_m = +1 and the lever is kappa-raising (zeta_m <= small) or sigma_m = -1 and it is kappa-lowering; (iii) is the cited corollary with the
data sign.  The last claim: Lemma MS(a) with Delta = -delta rt^{(m)} (exact: rt^{(m)} in V; statuses decrease by Lemma K) resp. +delta rt^{(m)}
(robust room in an unprotected block).  For a shifted block, a tiny minor M containing (X3)_m is affine in r^{(m)}: M = C_{Delta'} - sum_l
r_l C_l (expansion along (X3)_m, entries 1 at Delta'_m and -r_l at gamma_l), so M(s r) = M(r) - (s - 1) C_{Delta'} when M(r) = 0 and
sum_l r_l C_l = C_{Delta'}: scaling preserves M iff C_{Delta'} = 0.  QED
Reading for (H-6'): thick-type peaks of shifted blocks reduce to (alpha) sigma_m = sgn(Delta''_m) with only one-sided peak levers, plus
(beta) the block scaling is not exact (some tiny shift-carrying minor: C_{Delta'} != 0) or (sigma_m = +1 and the block is protected).  In
(beta), (JF2)/(1.3) applied to rt^{(m)} gives sum_i mu_i C^{(i)}_{Delta'} = kappa_m zeta_m(z*) - <A^T lambda, rt^{(m)}> + O(c_MS): the
shift-carrying cofactors of the tiny minors carry the robust zeta_m.

## 1.6 Remarks on scope

REMARK 1.5 (band version).  Bands (overshoot boxes along directions v of D_1) give a per-CERTIFICATE residual instead of a hull element
(Lemma 3.2(b) of H2 with the box replaced by the zonotope {sum_v o_v kappa v : o_v in [0, beta]}), but the passage from finitely many band
directions to the whole cone costs the representation constant of the cone {Delta in V : A Delta <= 0} by its extreme rays, which depends
on rt_0 (f-data).  Lemma MS avoids this constant; the per-row bounds that H2.A extracts from bands are recovered from (JF1) because each
single-row inward displacement is in D_1 (Part 2, Theorem H2.A').
REMARK 1.6 (non-affine groups, shifted part).  For pinned groups whose tiny polynomials are not affine and which live (partly) in shifted
blocks ((X4^0)-minors, cofactor polynomials, minors bilinear in two blocks' ratios), V_G contains only the (U)-piece scalings.  Tangent levers
along Z_G require a quantitative regularity of Z_G at rt_0 at scale h_max (Part 4, Lemma NL); (JF3) is then the only constraint, and
(H-6') reduces to these groups (see Part 4).
REMARK 1.7 (quantifiers).  design -> N -> (f, g, rho) -> L >= l_f -> w -> class a -> preparation -> admissible targets rt_0 (Lojasiewicz/Puiseux
steps) -> Y(rt_0) -> Lemma MS.  Nothing in Lemma MS is chosen after the certificates: the minimax produces one displacement Delta* for all
certificates at once (case (a)) or one hull element z* (case (b)).
REMARK 1.8 ((KN)-blocks, P-KN).  With the one-shot pre-move convention of cert0 3.2 for the KN lever d_0 (J2-ref Q-KN: the push of d_0 is
performed before Step A and raises theta by >= C' D eta' theta, U1-ref Proposition KN(b)), a (KN)-block enters Step A as a block whose
protected statuses (the active carriers protected by the KN margin, and d_0 itself) have margins >= c D eta' >> Design^C h_max^2.  Every
displacement of D_h keeps these statuses at first order (l_d <= 0) and moves them by <= Design^C h^2 at second order (Lemma 1.3(b)); the held
target of d_0 is a movable row of N.  Hence every LEVER OF LEMMA MS is legitimate in (KN)-blocks with no lever coupling: the bookkeeping gap
P-KN (inherited from J1's SKETCH of the KN-lever push inside Step A) does not arise for Lemma MS, under the pre-move convention.  PROVED (mod
chain: U1-ref Proposition KN(b), cert0 3.2, J2-ref Q-KN).  [Under the alternative convention (push inside the fixed point) the KN push is an
additional generator, and the statement needs J1's SKETCH.]
