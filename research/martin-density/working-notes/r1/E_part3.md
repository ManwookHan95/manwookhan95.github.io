# E notes, part 3: candidate NC (slow cross coordinates, one-sided near-contact errors) and its death

## 3.1 The candidate (construction SKETCH; mate property SKETCH with all terms checked)

Single block. a in c_00, F = supp a, j notin F with z_j = 0. Near-contacts: far coordinates l in NC with
z_l = s_l (1 - gamma_l), s_l = +-1, gamma_l decreasing to 0 (so z is not in c_0). v0 := e_j* - xhat_j a (v0(xhat) = 0).
Cross coordinates of two types at every scale lambda_i (geometric):
   u_P = (v0 + y_P - y_P(xhat) a)/n_P,  y_P = -Z_P;   u_N = (v0 + y_N - y_N(xhat) a)/n_N,  y_N = +Z_N,
Z_P, Z_N >= 0 in the z-signed sense (Z_l s_l >= 0), ||Z||_1 = eps_0 FIXED (slow rate!), supports in near-contacts
with gamma_l <= c_gamma lambda_i, pairwise DISJOINT supports (no P/N cancellation), plus negligible Y-tails.
F-compensation gives u(xhat) = 0: every cross coordinate is off-peak with w = 0 (full gap M) at f.
Design constraint: no coordinate approximates v0 at a fast rate; every coordinate with j-mass carries errors of size
>= eps_0 * (j-mass) on near-contacts.

g = c v0 is a mate for small c (SKETCH, all terms checked): at t>0 carry t c n u_{P(t)} (lambda_{P(t)} ~ t c/M, box ok,
block Hilbert c^2 t^2/(2C)), the base absorbs t c Z_{P(t)} + (multiple of a): first-order excess
sum_l gamma_l t c Z_l <= c_gamma lambda t c eps_0 = O(t^2), B(xhat) = 0, Hilbert part of the base small (far support).
t<0 symmetric with N. Global condition by smallness of c.

Why the earlier recovery tricks fail:
 * frozen certificate: any two-sided block combination near rho c v0 carries a frozen error
   h = rho c sum_k beta_k y_k with ||h|| >= rho c eps_0 (disjoint supports): not close to rho g.
 * eta-trick on the frozen error up to the slack scale T_0 = sqrt(6 eps/(1-rho^2)) costs eps >= T_0 rho c eps_0,
   forcing T_0 >= 6 rho c eps_0/(1-rho^2): not small.
 * rigidity at NA points (part 2.2): the finest scales need a single two-sided linear representation.

## 3.2 How it dies: eta-trick ON THE FROZEN ERROR + SIDE SWITCHING (SKETCH; new mechanism T4)

At f' choose a matched window down to scale lambda_I (cross coordinates and their near-contacts matched), pick ONE
N-type coordinate N* at scale lambda_{N*} ~ 2 lambda_I, make the head of supp Z_{N*} EXACT contacts (z'_l = s_l; cost
~ gamma_l * influence(l), tiny) and put eta-masses a'_l = eta_l s_l there with eta_l = kappa |Z_{N*,l}|,
kappa = M lambda_{N*}/n. Define
   g' := rho c n_{N*} u_{N*} + B_0,   B_0 := -rho c Z_{N*}^{head}   (so g' = rho c v0 + rho c Z_{N*}^{tail}, close to rho g).
Decompositions of f' + t g':
 (a) |t| <= M lambda_{N*}/(rho c n): block carries t rho c n u_{N*} (off-peak, box ok, two-sided); base absorbs t B_0 on
     the eta-contacts: for t<0 it increases |a'_l| (no cost), for t>0 no flip while t rho c |Z_l| <= eta_l. Two-sided.
 (b) t < 0 beyond (a): carry via N(t) (matched); base absorbs |t| rho c Z_{N(t)} (cheap) - |t| rho c Z_{N*}^{tail}
     (wrong sign, cost ~ 2|t| rho c ||Z^tail||, fine once ||Z^tail|| << lambda_{N*}).
 (c) t > 0 beyond (a): SWITCH to the P-type mechanism of f: carry via P(t) (matched, lambda_{P(t)} >= lambda_{N*});
     base absorbs t rho c (Z_{N*}^{tail} + Z_{P(t)}), both z-signed, cheap. The eta-coordinates are untouched.
 (d) |t| >= T_0: slack.
||a' - a|| ~ kappa eps_0 = O(lambda_I): f' -> f as lambda_I -> 0. Hence rho g is recovered.
Principle (T4): one-sided base errors of a frozen representation are cancelled by eta-masses only up to the scale of
the finest matched one-sided structure; above it each side switches to f's own one-sided mechanism for THAT side.
The eta budget is (finest matched scale) x (error mass), not (slack scale) x (error mass).
Requirements used: both P- and N-types matched down to lambda_I (true by windowing), near-contacts of f can be
made exact contacts at f' (true: the needed ones have gamma_l <= c_gamma lambda_I, influence small).
Remaining bookkeeping (not written): the change of e' caused by the eta-masses (compensable by finitely many linear
conditions on Delta a or window moves), g'(x') = 0 normalization, Hilbert terms. Status: SKETCH, high confidence.

## 3.3 Consequence for the search

After T1 (eta-trick), T2 (averaging), T3 (conversion: destruction and convertibility come from the same far tails),
T4 (frozen error cancellation + side switching), the only remaining place for an obstruction is:
CORE mass (window coordinates with |z| bounded away from 1, where neither eta-tricks nor contacts are possible) that is
carried at f, at every scale, only by ONE-SIDED BLOCK resources (near-peak coordinates used in their long direction),
whose conversion at f' is possible only in BOUNDED BANDS of scales (e.g. if the tails of all resources of a long scale
range are collinear beyond every window, so that one scalar controls a whole group). Then the averaging lemma has only
J_max two-sided scales and the boundary excess R(J_max) > 1 may survive. Tested in part 4 (Model N).
