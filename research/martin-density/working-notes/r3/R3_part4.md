# R3 part 4: error carrying defeats the rigid design (bounded conversion capacity is not an obstruction)

## 4.1 Lemma (disjoint block addition). PROVED.
Let f'' in S_{p*}, m_0 in I, S a finite set of strict non-peaks of block m_0 of f'' with w''_{m_0}(k) = 0 for k in S. Let W in V*
with W_{m_0}(k) = 0 for k in S, and let omega in c_00(S) with ||omega||_inf <= ||W_{m_0}||_inf. Then
  N_{m_0}(W_{m_0} + omega) <= N_{m_0}(W_{m_0}) + ||D omega||_2^2 / (2 ||D W_{m_0}||_2).
*Proof.* Disjoint supports: ||W + omega||_inf = max(||W||_inf, ||omega||_inf) = ||W||_inf and ||D(W + omega)||^2 = ||DW||^2 + ||D omega||^2;
sqrt(A^2 + B^2) <= A + B^2/(2A). QED.
With omega = t sum_{k in S} (c_k/lambda_k) e_k one has R_{m_0}* omega = t sum_k c_k u_k, ||D omega||^2 = t^2 ||c||_2^2/m_0^2, and the
condition ||omega||_inf <= ||W||_inf reads |t| |c_k| <= lambda_k ||W_{m_0}||_inf (room).

## 4.2 Theorem 4-EC (averaging at an approximant with carried errors). PROVED (as an implication).
Let f in S_{p*}, g in C(f), rho in (0,1), T_0 in (0, sqrt((1-rho^2)/2)]. Let f'' in NA cap S_{p*} and S, m_0 as in 4.1, and let
gbar, h_1, ..., h_J in X*, Q, Q_S, kappa' >= 0, scales s_j := s_1 2^{j-1} <= T_0 satisfy:
 (HC) p*(f'' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j;
 (HT-EC) for s_1 <= |t| <= T_0 there are A_t in X*, W_t in V* and y_t in X* with f'' + t gbar = A_t + L* W_t + t y_t,
      max(q*(A_t), ||W_t||_{V*}) <= 1 + Q t^2/2, W_{t,m_0} = w''_{m_0} on S, ||D_{m_0} W_{t,m_0}|| >= C''_{m_0}/2, ||W_{t,m_0}||_inf >= M''_{m_0}/2,
      and y_t = sum_{k in S} c_k(t) u_k + e_t with p*(e_t) <= kappa' |t| and ||c(t)||_2^2 <= Q_S m_0^2 C''_{m_0}/4,
      |t| |c_k(t)| <= lambda_k M''_{m_0}/2   (errors at scale t carried by the generic coordinates S, up to kappa'|t|);
 (HE-EC) h_j - gbar = sum_{k in S} c^j_k u_k + e^j with p*(e^j) <= kappa' s_j and, for s_j <= |t| <= T_0,
      ||c(t) + c^j||_2^2 <= Q_S m_0^2 C''_{m_0}/4 and |t| |c_k(t) + c^j_k| <= lambda_k M''_{m_0}/2;
with Q + Q_S <= 1 - 3(1-rho^2)/8 and J >= 32 kappa'/(1-rho^2). Put g' := (1/J) sum_j h_j. Then p*(f'' + t g') <= s(t) for |t| <= T_0. If
moreover p*(f'' - f) <= (1-rho^2)T_0^2/6 and p*(g' - rho g) <= (1-rho^2) T_0/6, then g' is in C(f'') and (f'', g') is in NA.
*Proof.* Convexity: p*(f'' + t g') <= (1/J) sum_j p*(f'' + t h_j). If s_j >= |t|, use (HC). If s_j < |t| (so |t| >= s_1): write
f'' + t h_j = A_t + L*W_t + t(y_t + h_j - gbar) = [A_t + t(e_t + e^j)] + L*[W_t + omega], omega := t sum_{k in S} ((c_k(t) + c^j_k)/lambda_k) e_k
(block m_0), using R_{m_0}* (e_k/lambda_k) = u_k. By Fact A, the triangle inequality for q* and Lemma 4.1 (applicable: W_{t,m_0} vanishes
on S since w'' does, and the room condition gives ||omega||_inf <= M''/2 <= ||W_{t,m_0}||_inf),
p*(f'' + t h_j) <= max(q*(A_t), ||W_t||) + t^2 ||c(t) + c^j||^2/(2 m_0^2 ||D W_{t,m_0}||) + |t|(p*(e_t) + p*(e^j))
              <= 1 + Q t^2/2 + Q_S t^2/4 + kappa' t^2 + kappa' |t| s_j     (p* <= q* on the base part).
Averaging, with sum_{s_j < |t|} s_j <= 2|t|: p*(f'' + t g') <= 1 + (Q + Q_S/2) t^2/2 + kappa' t^2 + 2 kappa' t^2/J
<= 1 + t^2 [ (1 - 3(1-rho^2)/8)/2 + kappa'(1 + 2/J) ]. Hmm: this needs kappa' itself small; restate: if kappa'(1 + 2/J) <= (1-rho^2)/16,
then p*(f'' + t g') <= 1 + t^2 [1/2 - 3(1-rho^2)/16 + (1-rho^2)/16] = 1 + t^2 [1/2 - (1-rho^2)/8] <= s(t) for t^2 <= (1-rho^2)/2
(s(t) >= 1 + t^2/2 - t^4/8). For |t| >= T_0 use the slack exactly as in N2 Theorem 4 / Theorem 1 Step 7. QED.
**Correct form of the hypothesis on kappa'** (replacing "J >= 32 kappa'/(1-rho^2)" above, which is not what the proof uses):
the e_t-term costs kappa'|t| at EVERY scale t >= s_1, so the theorem needs kappa' <= (1-rho^2)/32 (then J = 1 is allowed), and the
e^j-terms are what averaging over J scales reduces; if the e_t are absent (e_t = 0) and only e^j remain, the condition is
J >= 32 kappa'/(1-rho^2) as in N2 Thm 4. In words: Theorem 4-EC = N2 Theorem 4 in which the frozen errors h_j - gbar and the
transport errors y_t are split into a part carried by finitely many generic strict non-peaks S (cost Q_S, quadratic) and a
remainder (first-order cost kappa'). Only the remainder needs averaging over many converted scales.

## 4.3 Proposition (EC supplies (HT-EC)/(HE-EC) for compact error directions). PROVED (from Theorem EC and the room lemma).
Let E be a finite-dimensional subspace of zhat-perp with a basis b_1..b_d in S_{q*} satisfying hypothesis (ii) of Theorem EC on a
fixed finite G subset J modulo a fixed finite protected set Pi (beta := ||B^{-1}||). Given any NA data x'_N -> zhat (as in 2.1) and
any lambda_gen > 0, Theorem EC yields, for every n, an NA f''_n (window move o(1), Pi-values unchanged) with generic strict
non-peaks S_n = {k_{n,1..d}} at depths Phi(k) <= Phibar_n, u_{k_{n,i}} within eps_n of b_i, w'' = 0 on S_n. Every y in E with
||y||_1 <= kappa s, s <= sqrt(M''_n lambda_min,n/(4 beta kappa)), is then of the form y = sum_i c_i u_{k_{n,i}} + e with
||c||_inf <= 2 beta kappa s, ||e||_1 <= 2 d beta eps_n kappa s, and the room condition |t||c_i| <= lambda_{k_{n,i}} M''_n/2 holds for |t| <= s.
*Proof.* Write y = sum_i mu_i b_i; evaluating on the eta_l gives B^T-type system with ||mu||_inf <= beta ||y||_1 (as |y(eta_l)| <= ||y||_1).
Replace b_i by u_{k_{n,i}}: e := sum_i mu_i (b_i - u_{k_{n,i}}), ||e|| <= d ||mu||_inf eps_n. The room inequality is the room lemma 2.3. QED.
(The constant 2 absorbs the normalisation; any fixed constant would do.)

Consequence (the quantifier order that defeats rate control): choose the generic depth FIRST (Phibar_n, hence lambda_min,n), then the
destruction boundary lambda_b(n) and all scales s_j, s_1 so small that every error that has to be carried (size <= kappa s at scales
s <= T_n, where T_n is the top of the boundary layer, T_n = C lambda_b/(1-rho^2) in the transport bookkeeping, or up to
tau_F = M'' lambda_min/(2 beta kappa lambda_b) for the frozen errors of size kappa lambda_b) satisfies the room condition. Then all
E-components of the frozen errors and of the boundary-layer transport errors are carried with Q_S -> 0 and kappa' -> 0.

## 4.4 The rigid design of E 7.3 is not an obstruction. SKETCH (rigorous ingredients: Thm EC, 4.1-4.3; open ingredient: (HT)).
E's design (A1)-(A5): carriers u_k = (v + K lambda_k sigma_k + delta_k psi_{n(k)} + ...)/n_k of both peak types at all scales, core
errors sigma_k on core window coordinates (|z| <= 1 - gamma_0) lying, up to << 1/K, in a FIXED finite-dimensional E_c (this is how
(A2) and the Gordan form of (A3) are formulated in E 7.3), destruction through detector groups psi_n with pairwise disjoint far
supports G_n, far rigidity (tails collinear inside groups: one scalar s_n = psi_n(z' - z) per group), and (A5) "no critical-rate
convertible generic carriers of E_c".
Recovery scheme for given rho (quantifier order rho -> T_0 -> n -> generic depth -> boundary -> far choices):
 1. Window: x'_N matched on a window containing the supports of E_c, v, a (|z| <= 1 - gamma_0 there, so G := core coordinates is
    in J and E_c cap zhat-perp satisfies (ii) of Theorem EC modulo Pi := {v, finitely many designated carrier functionals}
    in generic position; components of the errors along zhat are absorbed in the d-terms/normalisation of the band
    certificate, see 4.5(3)).
 2. EC (Theorem EC with fixed targets = basis of E_c cap zhat-perp): generic carriers S_n at depth <= Phibar_n, w'' = 0.
    Precision eps_n -> 0 is free; NO rate is used, so (A5) is irrelevant.
 3. Boundary: pick a detector group n_b whose band lies at depth lambda_b << (1-rho^2) sqrt(lambda_min,n) (possible: groups occur at
    arbitrarily small scales, E 4.4). Keep groups coarser than n_b matched (z' = z on their detectors), make every coordinate of
    G_{n_b} a CONTACT carrying a small mass (masses ~ T_0 times the detector mass; they are o(1)), with signs chosen by the LP
    lemma 4.6 so that the group scalar s_{n_b} takes a value that converts a band of group n_b; finer groups: z' -> 0 (destroyed).
    If psi_{n_b} is concentrated on one coordinate, s_{n_b} in {1 - z_j, -1 - z_j}: the band position is then fixed, and the
    absolute shift V = v(x' - zhat) (window move along a protected-free direction, o(1)) is used to place one carrier of one
    type in the band (one carrier of one type suffices once errors are carried: 4.5).
 4. Band certificate h := rho times the switching component carried by the converted band carrier(s) (exact, two-sided for
    |t| <= s_1 ~ lambda_b). Its frozen error h - gbar = (E_c-part, size K lambda_b: carried by S_n, 4.3) + (detector part:
    supported on the contacts of G_{n_b}, absorbed with zero first-order base cost because the masses are larger than
    |t| times the entries for |t| <= T_0, N2 Lemma 1.4) + (o(1) lambda_b remainder). So kappa' -> 0 and J = 1.
 5. Transport (HT-EC) on [s_1, T_0]: matched structure of f; its transport errors near the boundary are E_c-valued (carried by
    S_n up to scale tau_gen ~ sqrt(lambda_min)) — this is exactly the boundary layer which E's Model N charges.
 6. Theorem 4-EC gives (f'', g') in NA with g' -> rho g; hence g in Ls(f).
The only non-rigorous step is (HT-EC) itself (transport of the matched one-sided structure of f to f'' above the boundary, with the
destroyed fine carriers contributing O(lambda_b/t) at scale t): the same transport hypothesis N2 Theorem 4 needs (HEURISTIC there),
now WITHOUT any conversion-capacity requirement.

## 4.5 Numerical confirmation in E's Model N. NUMERICAL.
Scripts: ctx/r3/work/ec_modelN.py, ec_frozen_only.py, ec_onetype.py (E's solver modelN.py unchanged). Model N (E 4.1) with error
weight A = 1, Hilbert B = 1/2, M = 1/2, scale ratio 1/2, error-dominated a0 = 0.03; EC modelled by setting the core-error cost to 0 for
tau <= tau_gen (resource errors carried) and the frozen error to 0 for tau <= tau_F = tau_gen^2 in band units (room lemma:
tau_F/tau_gen = tau_gen/lambda_b). R := sup_tau P_{f'}/sup_tau P_f (mate recovered for rho^2 < 1/R; R <= 1 means no obstruction).
 (1) Both types converted at one scale (one group scalar), delta = 1: without EC R = 1.194 (E's value reproduced);
     with EC, tau_gen = 2^2, 2^3, 2^4 octaves above the band: R = 1.088, 1.023, 1.005; delta = 2: R = 1.082, 1.021 (2^2, 2^3).
 (2) Frozen error carried but resource errors not (tau_gen = band): R = 1.088, 1.023, 1.021 for tau_F = 16, 64, 256 (the last value is
     a boundary-layer excess just above the band, removed by also carrying resource errors: (1)).
 (3) ONE absolute shift (one type converted, one carrier, the other type pushed deeper): without EC R = 3.41 (a0 = 0.03), 2.83
     (a0 = 0.3); with EC tau_gen = 2^4, 2^6, 2^8: R = 1.168, 1.041, 1.009.
In all cases the residual excess sits just above tau_gen or tau_F and decays like (band scale)/tau_gen, i.e. -> 0 when the band is
chosen deep relative to the generic depth, which the quantifier order of 4.3 allows. In the model, conversion capacity J = 1 (even
one carrier of one type) suffices once errors are carried. (Model N omits Hilbert couplings, d-terms and multi-block effects;
it is a proxy, not a lower or upper bound for p*.)

## 4.6 Lemma (contacts with tuned linear constraints). PROVED.
Let G be finite, z_G in [-1,1]^G, Lambda: R^G -> R^r linear and c in Lambda([-1,1]^G). Then there is y in [-1,1]^G with Lambda y = c and
at most r coordinates of y in (-1,1).
*Proof.* P := {y in [-1,1]^G : Lambda y = c} is a nonempty compact polytope, so it has a vertex y. At a vertex the active constraints
have rank |G|; the active ones among the box constraints are the coordinates with |y_j| = 1, and the equality constraints contribute
rank <= r. Hence at least |G| - r coordinates are at +-1. QED.
Use: on a far detector support G (or any far set) one can make all but r coordinates contacts (z'_j = +-1, carrying masses of sign
z'_j, so that the base absorbs any small multiple of a vector supported there two-sidedly with zero first-order cost, N2 Lemma 1.4)
while prescribing r linear quantities (group scalars, values of designated carriers). The unabsorbed part lives on <= r coordinates.
