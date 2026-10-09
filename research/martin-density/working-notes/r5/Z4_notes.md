# Z4 (Round 5): cases (O2) and (O3) of Remark rem:openZ — infinitely many swallowed signature sets and maximal contact

Setting: the note paper/martin_density_note.tex (numbering and notation as there), canonical base, finite block set I = {1,...,N} (p = p_N;
Lemma lem:martintail transfers density to Martin's norm), the signature-ladder operator of Definition def:SLD or the modified ladder SLD_G
proposed in part 2.4, first rows f with finite base support F. Parts: Z4_part1..8.md (assembled below). Script: Z4_work/maxcontact_toy.py.
No counterexample is claimed and nothing found points to one. Lemma Z and density remain OPEN for every admissible operator.

## Main results (statements in words)
**Theorem A (infinitely many swallowed signature sets; part 3, part 4).** PROVED. Use the modified ladder SLD_G (Definition def:SLD with the
window lengths and window tops inflated by a design constant G*(l), the largest Hoffman constant of the finitely many "configuration"
cones of level l; all results of Section 8 survive). Let f be a first row with finite base support, with an arbitrary (possibly infinite)
set of exactly swallowed signature sets. Assume: (H2') in every block the uniform shift can be pinned by peaks — a non-degenerate peak which
is good or swallowed with the swallowing sign, and a non-degenerate good peak or a swallowed peak of the opposite (anti) sign; (H3) every
swallowed peak of the swallowing sign is non-degenerate; (DR) the zero-cost cone admits fixed finitely supported d-repair directions with
d-sums of both signs in every block that contains a non-d-neutral swallowed strict non-peak; (W_inf) a growth condition: along a subsequence
of levels l, the quantity [(Lambda*_f(l) + M_f(l) + l)/Lambda°(l)]^2/(gamma_T(l)^2 gamma_f(l)) is o((l 2^{l^3})^6), where Lambda*_f is the room
product of the good signature sets (computed after removing the coarse swallowed targets), M_f(l) the sum of the reciprocal margins of the
swallowing-sign swallowed peaks up to level l, gamma_f(l) the least gap of the swallowed strict non-peaks up to level l, and gamma_T(l) the least
room of the free coordinates met by swallowed targets up to level l. Then f is recoverable: (f, g) lies in the closure of the norm-attaining
operators for every mate g. No resonance, no d-neutrality, no (H1) and no finiteness of the swallowed set is assumed.
For the ORIGINAL ladder the same holds without (DR) if the growth condition includes the f-dependent Hoffman constants of the actual cones
(Corollary 4.1). Theorem A and Corollary 4.1 contain Theorem thm:S — case (B_res) for SLD_G, case (B_fin) for both ladders (Corollary 4.2)
— and weaken (H2) to (H2') there. (H3) can be dropped from the window construction (Lemma 8.1, PROVED); the corresponding engineering step
is only SKETCHED (part 8, under an f-dependent steerability hypothesis).
**Mechanism (new).** (1) Scale-dependent active sets U(t) = {swallowed l <= l_* : lambda_l >= t^2}: inactive swallowed carriers cost O(l_* t)
in total, active ones satisfy lambda_l >= t^2, which turns the l_1-displacement of the projection into the coordinatewise bound needed by the
one-sided expansion. (2) The zero-cost cone depends on f only through finitely many combinatorial data on the target supports, so its
Hoffman constant is bounded by a DESIGN constant G*(l), which the super-fast ladder absorbs (T is fixed before f). (3) The uniform shift is
pinned without (H2) by BASE peaks: an anti-sign swallowed peak is pinned by the switching budget, a swallowing-sign one by its margin.
(4) d-neutrality is restored exactly by fixed repair directions (or, original ladder, by the actual Hoffman constants).

**Proposition B (far lowerings; part 1).** PROVED. p*(f^L - f) <= C_f sum_{l>L} lambda_l <= C_f c_{L+1}/2. On every scale inherited from f
through the rho-slack, the carriers made roomy by the lowering carry total switching O(t), and the coarse ones are swallowed exactly as at f;
so lower semicontinuity along far lowerings needs the same exact matching as Theorem A at f itself (far lowering localises but cannot absorb
f-dependent constants — the latter is HEURISTIC).

**Proposition C (rigidity of the d-mismatch; part 5).** PROVED. At maximal contact every two-piece data are d-neutral; in general a nonzero
d-mismatch in block m forces every far point of every peak signature set of block m to be a contact of a prescribed sign. So the option
Delta d >= 0 of Corollary cor:D1 is essentially never available on swallowed sets.

**Corollary D (maximal contact, (O3); part 5).** PROVED. At maximal contact (F finite, z = eps_0 off F) (H2') holds automatically, gamma_T = 1 and
Lambda*_f <= C Lambda°; with the design clause c_l <= (delta_l ||h_l||_1)^2, every carrier whose target does not cancel its signature lift is a
swallowing-sign peak with margin >= q_0 delta°_l/4. Hence f is recoverable under (H3), (DR) and liminf (1 + M^canc_f(l)/Lambda°(l))^2/
(gamma_f(l) (l 2^{l^3})^6) = 0 (M^canc: reciprocal margins of signature-cancelling swallowing-sign peaks). This adds to Corollary
cor:BTrecovered the maximal-contact rows that violate (BT) through infinitely many strict non-peaks or through weak/degenerate anti-sign peaks.

## What remains (precise; part 6)
(E-a) degenerate or super-weak swallowing-sign swallowed peaks (failure of (H3); margins beyond the ladder, e.g. failure of (MS) on the
swallowing side) — the degenerate part is reduced in part 8 to a steering lemma for the engineered approximants (SKETCH, needs an f-dependent
steerability hypothesis; without it OPEN); (E-b) near-threshold swallowed strict non-peaks (gaps beyond the ladder); (E-c) near-contacts met by swallowed targets;
(E-d) one-sided d-resources (failure of (DR)); (E-e) approximate swallowing of good sets ((O1)(i)). In each, the window data are exact
two-piece data only up to a first-order defect O(t) at window scale t, which neither windowed averaging nor the engineered approximants
tolerate (HEURISTIC, one-line estimates); perturbing f converts one small parameter into another of the same size (HEURISTIC). The common
open step is Problem 6.2: exact data for inexact resources, or a multi-scale engineering theorem accepting O(t) first-order defects.
(O4) (infinite F) was not treated.

## Labels
| # | Claim | Label | Where |
|---|---|---|---|
| 1 | coarse values unchanged under far lowering (Lemma 1.1) | PROVED | part 1 |
| 2 | p*(f^L - f) <= C_f c_{L+1}/2 (Prop 1.2) | PROVED | part 1 |
| 3 | band arithmetic: roomy carriers negligible on inherited scales (Prop 1.3) | PROVED | part 1 |
| 4 | zero-cost cone description and cost bound (Lemma 2.1) | PROVED | part 2 |
| 5 | configuration Hoffman constant G*(l) finite, design-computable; actual cone dominated (Lemma 2.2) | PROVED | part 2 |
| 6 | d-repair lemma (Lemma 2.3) | PROVED | part 2 |
| 7 | SLD_G admissible; all of Section 8 survives (Prop 2.4) | PROVED | part 2 |
| 8 | Theorem A = Theorem 3.1 (S_Binf) | PROVED | parts 3-4 |
| 9 | Corollary 4.1 (original ladder, f-dependent Hoffman growth) | PROVED | part 4 |
| 10 | Corollary 4.2: Theorem thm:S contained, (H2) -> (H2') | PROVED | part 4 |
| 11 | Lemma 5.0 (peaks of both signs), Prop 5.1 (d-neutral at maximal contact), Prop 5.2 ((H2') automatic) | PROVED | part 5 |
| 12 | Lemma 5.3 (signature lift; with design clause) | PROVED | part 5 |
| 13 | Corollary 5.4 / D (maximal contact) and Remark 5.5 (scope) | PROVED | part 5 |
| 14 | Prop 5.6 (general rigidity of the d-mismatch) | PROVED | part 5 |
| 15 | Lemma 6.1 (windowed averaging with window-dependent c_flat) | PROVED | part 6 |
| 16 | first-order defects O(t) cannot be averaged/engineered away; perturbations only move the smallness | HEURISTIC | parts 5, 6 |
| 17 | far lowering cannot absorb f-dependent growth | HEURISTIC | part 6 |
| 18 | (E-a)-(E-e), Problem 6.2 | OPEN | part 6 |
| 19 | finite-model check of the new pinning signs | numerical, signs only | part 7 |
| 20 | Lemma 8.1: data using degenerate peaks inwardly are exact at f; window data of Theorem 3.1 exist without (H3) | PROVED | part 8 |
| 21 | engineering (Corollary cor:D1) for data using degenerate peaks, by steering them to strict non-peaks at f', under an f-dependent steerability hypothesis | SKETCH | part 8 |
| 22 | weak peaks with intermediate margins can be neither projected nor degenerated within the window arithmetic | HEURISTIC | part 8 |

# Z4 part 1: far lowerings — the distance estimate and the band arithmetic

Setting: the note (paper/martin_density_note.tex), Section 8; SLD operator T of Definition def:SLD; N fixed, I = {1..N}, p = p_N.
f in S_{p*} with forced data (xi, q_0, a, w, F, z, zhat, e, nu), F finite. Ladder indices l, carrier (k(l), m(l)), u_l, lambda_l <= c_l/4.
Notation: v_k := m |u_k(zhat)| / |R_m** zhat|_m (block m = m(k)), so the clamp formula (proof of Lemma lem:F1) reads
Phi_k w_m(k) = sign(u_k(zhat)) min(Phi_k M_m, C_m v_k), and C_m is the root of F(c; v) := sum_k min(Phi_k (1-c)/c, v_k)^2 = 1.

## 1.1 Far lowerings f^L (recalled from rem:openZ (O2))
Let L_F be so large that S_l ∩ F = ∅ for l > L_F (F finite, S_l disjoint). For L >= L_F let G_L := union_{l>L} S_l, and let f^L be the first row
with forced data (a, z^L), z^L := 0 on G_L, z^L := z elsewhere (Remark rem:lemmaZ(c)). Then zhat^L - zhat = -z 1_{G_L}, f^L -> f, and
f^L - f = L*(w^L - w) (same base part a).

**Lemma 1.1 (coarse values unchanged).** PROVED. For l <= L: u_l(zhat^L) = u_l(zhat). For l > L: |u_l(zhat^L) - u_l(zhat)| <= ||u_l||_1 <= 1.
*Proof.* supp u_l ⊂ supp y_l ∪ S_l. For l <= L, S_l ∩ G_L = ∅ (disjointness) and supp y_l ∩ S_{l'} = ∅ for l' >= l (allowedness (a)), in
particular for every l' > L. So u_l vanishes on G_L. QED.

## 1.2 The distance estimate (settles the heuristic p*(f^L - f) = O(c_{L+1}))
**Proposition 1.2.** PROVED. Put eps_L := sum_{l>L} lambda_l (<= c_{L+1}/2 by (P2)). There are L_1 and C_f < infinity, depending only on f,
N and the design, such that for L >= L_1:  p*(f^L - f) <= q*(f^L - f) <= C_f eps_L <= C_f c_{L+1}/2.

*Proof.* Fix a block m and drop it. (i) By Lemma 1.1, ||R** zhat^L - R** zhat||_1 = sum_k lambda_k |u_k(zhat^L - zhat)| <= sum_{l>L, m(l)=m} lambda_l
<= eps_L, hence | |R** zhat^L| - |R** zhat| | <= eps_L (|.|_m <= ||.||_1). Let rho_0 := |R** zhat|/2; for L large |R** zhat^L| >= rho_0.
(ii) Increments of v. For carriers l <= L, u_k(zhat^L) = u_k(zhat), so |v^L_k - v_k| = m|u_k(zhat)| | 1/|R**zhat^L| - 1/|R**zhat| |
<= v_k eps_L/rho_0, and the signs of u_k(zhat^L), u_k(zhat) agree. For l > L, |v^L_k - v_k| <= 2m/rho_0. As sum_k Phi_k v_k <= m/(2 rho_0)
(|u_k(zhat)| <= q**(zhat) q*(u_k) = 1 and sum Phi_k <= 1) and sum_{l>L, m(l)=m} Phi_l = sum lambda_l/m <= eps_L/m,
  sum_k Phi_k |v^L_k - v_k| <= eps_L ( m/(2 rho_0^2) + 2/rho_0 ) =: C_1 eps_L.
(iii) C and M. By Proposition prop:continuity (f^L -> f), C^L -> C. The proof of Lemma lem:F1 (root localisation with a fixed peak k_natural
having alpha(k_natural) != 0) applies verbatim with (v, v^L) in place of (v, v'): for L large,
  |C^L - C| = |M^L - M| <= (2(1-C)/(C c_*)) sum_k Phi_k |v^L_k - v_k| <= K_C eps_L,  K_C := 2(1-C) C_1/(C c_*).
(iv) Coordinates. For l <= L the clamp formula with equal signs gives |Phi_k w^L(k) - Phi_k w(k)| <= |C^L - C|(Phi_k + v_k) + C^L |v^L_k - v_k|
<= eps_L ( K_C (Phi_k + v_k) + v_k/rho_0 ) (using min(x,s) Lipschitz in s and |min(Phi(1-c)/c... )| as in Lemma lem:F1; here the clamp level
Phi_k M changes by Phi_k |M^L - M|). Multiply by m (lambda_k = m Phi_k) and sum over k: sum_{l<=L} lambda_k |w^L(k) - w(k)| <= m eps_L (K_C (1 + m/(2rho_0)) + m/(2 rho_0^2)).
For l > L, lambda_l |w^L - w|(k_l) <= 2 lambda_l, summing to <= 2 eps_L.
(v) ||L*(w^L - w)||_1 <= sum_m sum_k lambda_{k,m} |w^L_m(k) - w_m(k)| ||u_{k,m}||_1, and q* <= (1 + ||U||) ||.||_1, p* <= q*. QED.

Remark. The constant C_f depends on f through rho_0, C_m, c_* (a fixed non-degenerate peak), i.e. only on coarse data; eps_L is a design
quantity. So the slack threshold of f^L is t_L(rho) := (6 C_f eps_L/(1-rho^2))^{1/2} = O(c_{L+1}^{1/2}).

## 1.3 The band arithmetic: far lowering gains nothing at inherited scales
**Proposition 1.3.** PROVED. Let g in C(f), rho in (0,1), and t >= A t_L(rho) with A >= 1. Then:
 (a) p*(f^L + tau rho g) <= s(tau) for all |tau| >= t_L(rho) (slack);
 (b) every two-sided decomposition (of g at f, or of rho g at f^L — the latter exists at every scale t >= t_L(rho) by (a) and Lemma lem:twosided,
     whose proof only uses p*(f^L + t rho g) <= s(t)) satisfies sum_{l>L} |Delta theta_l| <= 6 eps_L / t <= t (1 - rho^2)/(C_f A^2);
 (c) for l <= L the swallowing status, the signs eps_l, the values u_l(zhat) and the contact pattern on S_l and on supp y_l are the same at f and f^L.
*Proof.* (a) p*(f^L + tau rho g) <= p*(f + tau rho g) + p*(f^L - f) <= s(rho tau) + C_f eps_L, and s(tau) - s(rho tau) >= (1-rho^2) min(tau^2, |tau|)/3
(Lemma lem:slack(a)); for |tau| >= t_L, (1-rho^2) tau^2/3 >= 2 C_f eps_L. (b) Lemma lem:box: |Delta theta_l| <= 6 lambda_l / t. (c) Lemma 1.1 and
z^L = z off G_L, supp y_l ∩ G_L = ∅ for l <= L. QED.

Consequence (PROVED as stated): on the whole range of scales that f^L inherits from f through the rho-slack, the carriers made roomy by
the lowering carry total switching O(t) (they are negligible exactly like the fine carriers of a window), and the coarse carriers l <= L are
swallowed exactly as at f. Hence a proof that dist(rho g, C(f^L)) -> 0 must, on the band [A t_L, T] of inherited scales, produce exact
data for the FINITELY many swallowed coarse carriers l <= L with constants that the length of the band absorbs: this is the same matching
problem as at f itself with the scale-dependent active set U*(t) ⊂ [1, L] (part 3). Far lowering removes the fine carriers but does not
remove the matching problem; conversely, once the matching is available with absorbable constants, it can be done at f directly (part 3,
Theorem S_Binf), and f^L is not needed. (Heuristic remark: lowering by a factor or on far points of COARSE sets creates room whose pinning
is effective only at scales t^2 <~ lambda_l room_l, while the slack of that lowering covers only t^2 >~ lambda_l room_l — Z1's transition
band; Prop. 1.3 is the rigorous version for whole fine sets.)

# Z4 part 2: zero-cost cones, configuration Hoffman constants, and a modified ladder

Throughout: SLD operator (or the modified one of 2.4), N fixed, f with F finite. For a carrier l write v_l := delta_l h_l/n_l (so u_l = v_l on
S_l, (P1)). B = B(f) := {l in L_N : r_l = 0} (exactly swallowed carriers, Remark rem:Bpm(a)): z = eps_l on S_l \ F. "Good" = L_N \ B.

## 2.1 The zero-cost cone of an active set (any f with F finite)
For a finite U ⊂ B put T(U) := union_{l in U} supp y_l (finite) and, for tau in R^U, L_j(tau) := sum_{l in U} eps_l tau_l u_l(j) (j in N) and
the **cost** c_U(tau) := sum_{j notin F} phi_{z_j}(L_j(tau)) (phi_z(x) = |x| - z x, Lemma lem:phicalc).
The **zero-cost cone** is Z^0_U := {tau in R^U : c_U(tau) = 0}; the **exact cone** is Z_U := {tau in Z^0_U : tau_l = 0 for l in U with
k(l) in P_{m(l)}, and sum_{l in U, m(l)=m} q_l tau_l = 0 for every m}, where q_l := eps_l Phi_{m(l)}(k(l)) w_{m(l)}(k(l))/(m(l) C_{m(l)})
(as in Definition def:swallowed).

**Lemma 2.1 (explicit description).** PROVED. c_U(tau) = 0 iff (Z1) tau_l >= 0 for l in U, and (Z2) for j in T(U) \ F: z_j L_j(tau) >= 0
if |z_j| = 1, L_j(tau) = 0 if |z_j| < 1. Moreover, with m_l(U) := ||v_l 1_{S_l \ (T(U) ∪ F)}||_1 > 0 and gamma_T(U) := min({1} ∪
{1 - |z_j| : j in T(U) \ F, |z_j| < 1}) > 0,
  c_U(tau) >= 2 sum_{l in U} m_l(U) (tau_l)_- + 2 sum_{j in T(U)\F, |z_j|=1} (z_j L_j(tau))_- + gamma_T(U) sum_{j in T(U)\F, |z_j|<1} |L_j(tau)|.   (2.1)
If tau in Z^0_U then V(tau) := sum_{l in U} eps_l tau_l u_l 1_{F^c} is z-signed and supported in K.
*Proof.* For j notin F ∪ T(U) ∪ union_U S_l every u_l (l in U) vanishes at j. For s in S_l \ (T(U) ∪ F), l in U: the other signatures vanish
(disjointness) and no target y_{l'}, l' in U, meets s, so L_s(tau) = eps_l tau_l v_l(s) and z_s = eps_l (swallowed), hence
phi_{z_s}(L_s) = 2 (tau_l)_- v_l(s) by Lemma lem:phicalc(a); summing over s gives 2 m_l(U)(tau_l)_-; m_l(U) > 0 since S_l is infinite and
T(U) ∪ F finite. Points of T(U) \ F: phi_z(x) = 2(zx)_- if |z| = 1, phi_z(x) >= (1-|z|)|x| (Lemma lem:phicalc(a)). All summands are >= 0, so
c_U = 0 iff each vanishes, which is (Z1), (Z2). Finally phi_{z_j}(V(j)) = 0 for all j notin F means z_j V(j) = |V(j)|, which forces
|z_j| = 1 where V(j) != 0. QED.

## 2.2 Configurations and the design constant G*(l)
A **configuration of level l** is kappa = (U, P, eps, F', type, n) with U ⊂ L_N ∩ [1, l], P ⊂ U, eps in {±1}^U, F' ⊂ T(U), n in [0, l]
an integer, and type : T(U) \ F' -> {+1, -1, 0} with type(s) = eps_{l'} for s in S_{l'}, l' in U. It defines the finite linear system
in tau in R^U:
 (Z1) tau_l >= 0 (l in U), with weight m_l(U, n) := ||v_l 1_{S_l \ (T(U) ∪ [1, n])}||_1 > 0;
 (Z2) type(j) L_j(tau) >= 0 if type(j) = ±1, L_j(tau) = 0 if type(j) = 0 (j in T(U) \ F'), with L_j as in 2.1 (eps from kappa);
 (Z3) tau_l = 0 (l in P);
and the violation functionals viol'_kappa(tau) := sum_U m_l(U,n)(tau_l)_- + sum_{type ±1} (type(j) L_j)_- + sum_{type 0} |L_j| and
viol_kappa := viol'_kappa + sum_{l in P} |tau_l|. Let Z'_kappa (resp. Z^0_kappa) be the polyhedral cone of (Z1),(Z2) (resp. (Z1)-(Z3)); both contain 0.
By Hoffman's error bound [Hoffman 1952] there are finite H'(kappa), H(kappa) with
  dist_1(tau, Z'_kappa) <= H'(kappa) viol'_kappa(tau),  dist_1(tau, Z^0_kappa) <= H(kappa) viol_kappa(tau)  (tau in R^U).   (2.2)
Put **G*(l) := max(1, max over configurations kappa of level <= l of max(H(kappa), H'(kappa)))**. PROVED: G*(l) < infinity (finitely
many configurations of each level: U, P, eps, n range over finite sets and F', type over finite sets because T(U) is finite), G* is
nondecreasing, and G*(l) is determined by the design data of the carriers l' <= l (targets y_{l'}, signatures v_{l'}, sets S_{l'}).

**Lemma 2.2 (actual configuration).** PROVED. Let f have F finite, l >= max F, U ⊂ B ∩ [1, l] finite, P := {l' in U : k(l') peak},
eps := (eps_{l'}), F' := F ∩ T(U), type(j) := z_j if |z_j| = 1 and 0 otherwise (j in T(U) \ F), n := max F. Then kappa(f,U) is a configuration
of level l (type = eps_{l'} on S_{l'} \ F since l' is swallowed), Z^0_U ∩ {tau_l = 0, l in P} = Z^0_{kappa(f,U)}, and
  viol'_{kappa(f,U)}(tau) <= c_U(tau)/gamma_T(U),  hence dist_1(tau, Z'_{kappa}) <= G*(l) c_U(tau)/gamma_T(U).   (2.3)
*Proof.* m_l(U) >= m_l(U, n) because F ⊂ [1, n]; compare (2.1) with viol' termwise (gamma_T <= 1 <= 2). QED.

## 2.3 d-repair
**Definition (DR).** f satisfies (DR) if for every block m there are finitely supported tau^{m,+}, tau^{m,-} in R^B with c_{supp}(tau^{m,±}) = 0
(zero cost), vanishing at swallowed peaks, with sum_{l: m(l)=m} q_l tau^{m,±}_l = ±1 and sum_{l: m(l)=m'} q_l tau^{m,±}_l = 0 (m' != m);
or block m contains no swallowed strict non-peak with q_l != 0 (then put tau^{m,±} := 0). R_f := max ||tau^{m,±}||_1, U_R := union supp tau^{m,±}.

**Lemma 2.3 (repair).** PROVED. Let U ⊃ U_R be finite and tau in Z^0_U with tau_l = 0 at peaks. Put delta_m := sum_{m(l)=m} q_l tau_l. Then
tau' := tau + sum_m |delta_m| tau^{m, -sign(delta_m)} lies in Z_U and ||tau' - tau||_1 <= R_f sum_m |delta_m|.
*Proof.* Zero cost is preserved by sums of zero-cost vectors with nonnegative coefficients: phi_z is positively homogeneous and subadditive
(Lemma lem:phicalc(b) with y -> -y), so c_U(tau + s tau^{m,±}) <= c_U(tau) + s c_U(tau^{m,±}) = 0 (zero extension keeps zero cost: an extended
vector is zero-cost iff its V is z-signed in K, a property of V only). Peak rows and d-rows are linear. QED.

## 2.4 The modified ladder (route (1): absorb configuration constants into the design)
**Definition (SLD_G).** As Definition def:SLD, except that in (D1), after y_l, n_l, u_l, delta°_l, Lambda°(l) are fixed, put
Gamma(l) := G*(l) (computable at this stage), and
  n^w_l := ceil( (l 2^{l^3} Lambda°(l) Gamma(l))^6 ),  T_hi(l) := min{ T_lo(l-1), (l 2^{l^3} Lambda°(l) Gamma(l))^{-6} },
  T_lo(l) := 2^{-n^w_l} T_hi(l),  c_{l+1} := min{c_l/4, T_lo(l)^3}.
**Proposition 2.4 (survival).** PROVED. SLD_G is admissible and satisfies (P1), (P2) and (P3) of Theorem thm:SLD (indeed
T_hi(l) 2^{l^3} Lambda°(l) <= 1/l and n^w_l >= l 2^{l^3} Lambda°(l) because Gamma >= 1, Lambda° >= 1). Hence every result of Section 8
(Theorems thm:R0, thm:reductionZ, thm:Bstar, thm:Bpm, thm:S, all lemmas of Subsections 8.2-8.7) holds verbatim for SLD_G: their proofs use only
(T-a)-(T-d), (P1)-(P3) and allowedness (a),(b) (the note states this after Theorem thm:SLD; Theorem thm:S uses in addition only these).
*Proof.* G*(l) depends only on (S_{l'}, y_{l'}, v_{l'})_{l' <= l}, all fixed before T_hi(l) is chosen, so the recursion is well defined; the proof
of Theorem thm:SLD uses (D1) only through allowedness and c_{l+1} <= c_l/4, unchanged. QED.

Remark 2.5 (why configurations). The Hoffman constant of the actual zero-cost cone depends on f only through finitely many combinatorial data
on the finite set T(U) (contact signs vs free, F ∩ T(U), swallowing signs, peak status) and through max F; the continuous f-data (rooms of free
target points, margins, gaps, q_l) enter only through gamma_T, the peak rows and the d-rows, which part 3 treats separately. This is exactly
what makes "uniform Hoffman constants" possible: G*(l) is a DESIGN quantity, and the super-fast ladder can be chosen after it (T before f).

# Z4 part 3: Theorem S_Binf — infinitely many swallowed carriers (non-resonant, non-d-neutral) via scale-dependent active sets

Setting: SLD_G (part 2.4) — or the original SLD under the hypotheses of Corollary 4.1 — N fixed, f in S_{p*} with F finite, B = B(f) arbitrary
(possibly infinite). Conventions of the note: Delta d_m := d_{+,m} - d_{-,m} (Lemma lem:suplevel), tau_l := -eps_l Delta theta_l (l in B),
q_l as in def:swallowed. For l in B with k(l) a peak, varsigma_l := sign w_{m(l)}(k(l)); the peak is of **swallowing sign** if varsigma_l = eps_l
and of **anti sign** if varsigma_l = -eps_l.

## 3.1 Growth quantities and hypotheses
For a level l_* >= 1:
* r*_l(l_*) (good l <= l_*) := min_{sigma=±1} sum_{s in S*_l(l_*)} v_l(s)(1 + sigma z_s), S*_l(l_*) := S_l \ (F ∪ union{supp y_{l'} : l' in B, l < l' <= l_*});
  r*_l := 2||v_l 1_{S_l\F}||_1 for l in B; Lambda*_f(l_*) := prod_{l <= l_*, l in L_N} (1 + 3/r*_l(l_*)) (= infinity if some r*_l(l_*) = 0).
* M_f(l_*) := sum{ 1/mu_{k(l),m(l)} : l in B ∩ [1,l_*], k(l) a peak of swallowing sign }.
* gamma_f(l_*) := min( {M_m : m in I} ∪ {gap_{m(l)}(k(l)) : l in B ∩ [1,l_*], k(l) in Q_{m(l)}} ) > 0.
* gamma_T(l_*) := min( {1} ∪ {1 - |z_j| : j in T(B ∩ [1,l_*]) \ F, |z_j| < 1} ) > 0 (T(.) as in part 2).
* Xi_f(l_*) := [ (Lambda*_f(l_*) + M_f(l_*) + l_*) / Lambda°(l_*) ]^2 / ( gamma_T(l_*)^2 gamma_f(l_*) ).
Hypotheses on f:
* (H2') for every block m there are carriers l^up_m, l^dn_m of block m such that l^up_m is a non-degenerate peak which is good or swallowed
  with swallowing sign, and l^dn_m is a non-degenerate good peak or a swallowed peak of anti sign (degenerate allowed).
* (H3) every swallowed peak of swallowing sign is non-degenerate (as in def:swallowed).
* (DR) part 2.3.
* (W_inf) liminf_{l -> infinity} Xi_f(l) / (l 2^{l^3})^6 = 0.
  (Implied by (W*)-type growth: if M_f, 1/gamma_f, 1/gamma_T grow at most like (l 2^{l^3})^{1/2} and Lambda*_f/Lambda° = O((l 2^{l^3})^2) along a
  subsequence. In particular (W*) of def:swallowed together with bounded M_f, 1/gamma_f, 1/gamma_T implies (W_inf).)
**R_SBinf** := {f : F finite, (H2'), (H3), (DR), (W_inf)}.

**Theorem 3.1 (S_Binf).** For SLD_G and every N, R_SBinf ⊂ R. PROVED (proof in 3.2-3.3 and part 4).
No resonance, no d-neutrality, no (H1) and no finiteness of B is assumed; strict non-peaks may be infinite in number, (MS) may fail,
contact sets are arbitrary.

## 3.2 Per-scale estimates
Fix g in C(f), rho in (0,1), eta_0, kappa_0, eps_tr, eta as in the proof of Theorem thm:S. "f-constant" = a number depending only on
f, g, rho, N and the design, NOT on l_* or t. Let l_* >= max(max F, l_f) where l_f is so large that the finitely many fixed carriers
U_fix := U_R ∪ {l^up_m, l^dn_m : m} are <= l_f. Let t in W(l_*) be dyadic with t <= min(t_eta, 1) and t^2 <= min_{U_fix} lambda_l, and let
(B_±, Theta_±) be a two-sided decomposition of g at scale t. Put U := {l in B ∩ [1, l_*] : lambda_l >= t^2} (the **active set**; U ⊃ U_fix).

**Step 1 (good pinning).** sum_{l notin B} |Delta theta_l| <= K* t, K* := (1/q_0 + 22) Lambda*_f(l_*).
*Proof.* For good l <= l_* and s in S*_l(l_*), (P1) and eq:DeltaB give -Delta B(s) = Delta theta_l v_l(s) + sum_{l' > l} Delta theta_{l'}
y_{l'}(s)/n_{l'}, where coarse swallowed l' (<= l_*) do not occur (definition of S*_l), coarser targets vanish on S_l (allowedness (a)) and
other signatures vanish. As in the proof of Lemma lem:signmixed, r*_l(l_*) |Delta theta_l| <= E_l + 2 sum_{l<l'<=l_*, l' good} pi_{l',l}
|Delta theta_{l'}| + 2 sum_{l' > l_*} pi_{l',l} |Delta theta_{l'}|, E_l := sum_{s in S*_l} phi_{z_s}(Delta B(s)), sum_l E_l <= t/q_0
(Lemma lem:switchbudget). Only good coarse carriers occur on the right; unroll as in Lemma lem:modswallow (x_l := |Delta theta_l| for good l,
x_l := 0 for swallowed l, X_l := E_l + 2 sum_{l'>l_*} pi_{l',l}|Delta theta_{l'}|), use sum_{l'>l_*}|Delta theta_{l'}| <= 6t^2 (Lemma lem:box,
(P2)). QED.

**Step 2 (cost of the swallowed switching).** e_0 := Delta B 1_{F^c} - sum_{l in U} eps_l tau_l u_l 1_{F^c} satisfies ||e_0||_1 <= K_0 t,
K_0 := K* + 6 l_* + 6, and c_U(tau|_U) <= (1/q_0 + 2K_0) t.
*Proof.* e_0 = -sum_{l notin U} Delta theta_l u_l 1_{F^c}, ||u_l||_1 <= 1. Good carriers: Step 1. Swallowed l <= l_* with lambda_l < t^2: at most
l_* of them, |Delta theta_l| <= 6 lambda_l/t < 6t each (Lemma lem:box). Fine carriers: <= 6t^2. Then c_U(tau) = sum_{j notin F} phi_{z_j}
(Delta B(j) - e_0(j)) <= sum phi_{z_j}(Delta B(j)) + 2||e_0||_1 <= t/q_0 + 2 K_0 t (Lemmas lem:phicalc(c), lem:switchbudget). QED.

**Step 3 (the uniform shift is pinned through base peaks).** Put K_1 := G*(l_*) K_0/gamma_T(l_*). There is tau° in Z'_{kappa(f,U)} (in
particular tau°_l >= 0 on U) with ||tau|_U - tau°||_1 <= D := (1/q_0 + 2) K_1 t, and |Delta d_m| M_m <= K_d t for every m, K_d := C_1 K_1,
C_1 an f-constant.
*Proof.* The first claim is (2.3) with Step 2. Fix m. Upper bound: if l := l^dn_m is a swallowed anti-sign peak, then by eq:peakshift (as in
the proof of Lemma lem:badpeaks(c)), varsigma_l eps_l tau_l/lambda_l - Delta d_m M_m = |omega_{+,m}(k)| + |omega_{-,m}(k)| >= 0 with
varsigma_l eps_l = -1, so Delta d_m M_m <= -tau_l/lambda_l <= (tau_l)_-/lambda_l <= D/lambda_l (tau°_l >= 0). If l^dn_m is a good
non-degenerate peak, Lemma lem:badpeaks(a) (its proof uses only |Delta theta_{l°}| <= K* t, Step 1) gives |Delta d_m| M_m <= t/(sigma_m
|alpha_m(k°)|) + K* t/lambda_{l°}. Lower bound: if l := l^up_m is swallowed of swallowing sign with margin mu > 0, then 0 <= tau_l/lambda_l -
Delta d_m M_m = e_k := |omega_+(k)| + |omega_-(k)| <= t/(lambda_l mu) (Lemma lem:suplevel(c): |alpha(k)| e_k <= t/sigma, and sigma|alpha(k)| =
lambda_k mu_k, eq:margin); hence Delta d_m M_m >= tau_l/lambda_l - t/(lambda_l mu) >= -(D + t/mu)/lambda_l. Good case as above. K_1 >= K_0 >= K*. QED.

**Step 4 (violations of the exact cone).** viol_{kappa(f,U)}(tau|_U) <= C_2 (K_1 + M_f(l_*)) t, C_2 an f-constant; hence there is tau_0 in
Z^0_{kappa(f,U)} with ||tau|_U - tau_0||_1 <= D_0 := C_2 G*(l_*)(K_1 + M_f(l_*)) t.
*Proof.* viol' <= c_U/gamma_T(l_*) <= (1/q_0 + 2)K_1 t/G* <= (1/q_0+2) K_1 t (Lemma 2.2, Step 2). Peak rows, l in U with k = k(l) a peak:
tau_l = varsigma_l eps_l lambda_l (Delta d_m M_m + e_k), e_k >= 0 (eq:peakshift). Swallowing sign: |tau_l| <= lambda_l K_d t + t/mu_l
(Step 3 bound e_k <= t/(lambda_l mu_l); mu_l > 0 by (H3)). Anti sign: tau_l = -lambda_l(Delta d M + e_k) <= lambda_l K_d t, and (tau_l)_- <=
|tau_l - tau°_l|. Summing (sum lambda_l <= 1/3): sum_{U∩P} |tau_l| <= K_d t/3 + M_f(l_*) t + D. Apply (2.2). QED.

**Step 5 (exact d-neutral projection).** There is tau' in Z_U (zero cost, tau' = 0 at peaks, all d-rows exact) with
||tau|_U - tau'||_1 <= C_diamond t,  C_diamond := C_3 G*(l_*)^2 (Lambda*_f(l_*) + l_* + M_f(l_*)) / gamma_T(l_*),  C_3 an f-constant.
*Proof.* d-rows of tau: by eq:didentity, for block m, sum_{l in B, m(l)=m} q_l tau_l = -Delta d_m M_m + (1/(mC_m)) sum_{good} Phi w Delta theta
+ r_m, |r_m| <= 2t/sigma_m (for swallowed l, Phi(k)w(k)Delta theta_l/(mC) = -q_l tau_l). Swallowed l notin U: |q_l| <= Phi_l M/(mC),
|tau_l| <= 6 m Phi_l/t; if l <= l_* then Phi_l < t^2/m, so sum |q_l tau_l| <= 6Mt/(mC) sum Phi_l <= 6t/C_m; if l > l_*, Phi_l <= c_{l_*+1} <= t^3
and the sum is <= (6M/(C_m t)) t^3 sum Phi_l <= 6t^2/C_m. Hence |delta_m(tau|_U)| <= K_q t, K_q := K_d + K*/(mC_m) + 2/sigma_m + 12/C_m <= C K_1. For tau_0 (Step 4),
|delta_m(tau_0)| <= K_q t + D_0/C_min (|q_l| <= 1/C_min). tau_0 vanishes at peaks; Lemma 2.3 (U ⊃ U_R) gives tau' in Z_U with
||tau' - tau_0||_1 <= R_f N (K_q t + D_0/C_min). Collect, using K_1 = G* K_0/gamma_T, K_0 <= (1/q_0 + 28)(Lambda* + l_*), G*, R_f >= 1. QED.

# Z4 part 4: Theorem S_Binf, end of proof; consequences

Continuation of part 3 (same f, g, rho, l_*, t, U, tau, tau').

**Step 6 (window two-piece data).** Assume moreover C_diamond t <= 1. Let V' := sum_{l in U} eps_l tau'_l u_l 1_{F^c} (z-signed, supported in K:
Lemma 2.1, tau' in Z^0_U), e := Delta B 1_{F^c} - V' (so ||e||_1 <= (K_0 + C_diamond) t), chi and frak e_± from Lemma lem:split. Let
U_np := {l in U : k(l) in Q_{m(l)}} (then V' = sum_{U_np} eps_l tau'_l u_l 1_{F^c}). Define, exactly as in Lemma lem:windowtwopiece with
B_np replaced by U_np:
 + : omega^+_m := omega^c_m (Definition def:windowcert) off {k(l) : l in U_np}, omega^+_m(k(l)) := omega_{+,m}(k(l)) for l in U_np, m(l) = m;
     b^+ := B_+ 1_F + chi V' - kappa a, kappa := (B_+ 1_F + chi V')(zhat);
 - : omega^-_m := omega^+_m + sum_{l in U_np, m(l)=m} (eps_l tau'_l/lambda_l) e_{k(l)},  b^- := b^+ - sum_{l in U_np} eps_l tau'_l u_l;
 g_t := b^+ + sum_m R_m^*(omega^+_m - d_m(omega^+_m) w_m).
Then, with K_2, K_4 <= C_4 C_diamond and A^star_0 f-constants:
 (a) (b^±, omega^±) are d-neutral two-piece data for g_t (Definition def:twopiece), b^±(xi) = 0;
 (b) ||g - g_t||_1 <= K_2 t;  (c) Gamma_w(b^±, omega^±) <= (sqrt(1 + eta_Gamma(eta)) + K_4 t)^2;
 (d) t ||b^±||_1 <= A^star_0, and every k in supp omega^±_m has either gap_m(k) >= t^2 and |omega^±_m(k)| <= 2 gap_m(k)/t, or k = k(l),
     l in U_np, gap_m(k) >= gamma_f(l_*) and |omega^±_m(k)| <= A_2/t with A_2 := 10 + C_diamond.
*Proof.* The proof of Lemma lem:windowtwopiece applies line by line with B_np -> U_np, with the following replacements.
(a) d_m(omega^-_m) - d_m(omega^+_m) = sum_{l in U_np, m(l)=m} q_l tau'_l = sum_{l in U, m(l)=m} q_l tau'_l = 0 because tau' vanishes at the
peaks of U and satisfies the d-rows (Step 5). Signs: b^+ 1_{F^c} = chi V' and b^- 1_{F^c} = -(1-chi) V'.
(b) Coarse coordinates: good ones as in Proposition prop:windowcert(c) (claim there, with sum over good |Delta theta| <= K* t and |Delta d_m| M_m
<= K_d t); k(l), l in U_np: rho_k = 0; k(l), l in U ∩ P: omega^+(k) = 0 and rho_k <= e_k, lambda_l e_k <= |tau_l| + lambda_l |Delta d M|
with |tau_l| = |tau_l - tau'_l| (tau'_l = 0), total <= C_diamond t + K_d t; swallowed coarse l notin U (lambda_l < t^2): treated as good coarse
coordinates of the window certificate, lambda rho <= |Delta theta_l| + lambda |Delta d| M + 2t lambda with |Delta theta_l| < 6t, total <= 6 l_* t
+ K_d t + 2t. Fine coordinates and d-terms: as in the note (|omega^+| <= 4/t by Lemma lem:suplevel(a),(e), so |d_m(omega^+_m)| <= 2/t). Base:
B_+ - b^+ = frak e_+ + kappa a, ||frak e_+||_1 <= ||e||_1 + t/q_0, |kappa| <= t/(2q_0) + (1+||U||)||frak e_+||_1.
(c) Seminorm comparison with (B_±, Theta_±) and Lemma lem:budget(d) as in the note; on the - side the lambda-weighted discrepancy at k(l),
l in U, is |tau_l - tau'_l|, at good/fine/inactive coordinates |Delta theta_k|: total <= (K_0 + C_diamond) t.
(d) |tau'_l| <= |tau_l| + C_diamond t <= 6 lambda_l/t + C_diamond t and lambda_l >= t^2 on U, so |tau'_l|/lambda_l <= (6 + C_diamond)/t;
|omega^+_m(k(l))| <= (3 + eta)/t <= 4/t; gap_m(k(l)) >= gamma_f(l_*) for l in U_np. ||V'||_1 <= sum_U |tau'_l| <= 2/t + C_diamond t <= 3/t.
The rest as in the note. QED.

**Step 7 (one-sided expansion).** Lemma lem:onesidedtransfer with (eps_tr, A^star_0, A_2, gamma_B := gamma_f(l_*)) gives c_flat >=
c_f gamma_f(l_*)/A_2 >= c'_f gamma_f(l_*)/C_diamond (c_f an f-constant) and t_1 depending only on f and eps_tr. PROVED: in the proof of that
lemma the conditions involving A_2 and gamma_B are conditions on c_flat only (c_flat <= gamma_B/(2A_2), c_flat <= C_min/(2A_3), and the
O(c_flat) relative errors with constants linear in A_3 = 2 + A_2), while t_1 is constrained only through terms of order r^4 with |r| <= c_flat t
<= t and through the transfer data. Hence for every dyadic t in W(l_*) with t <= min(t_eta, t_1, 1), C_diamond t <= 1 and K_4 t <= kappa_0:
p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t (+ data for r > 0, - data for r < 0), and p*(g - g_t) <= (1 + ||U||) K_2 t.

**Step 8 (window arithmetic).** Put K_j := (1+||U||) K_2(l_j) for window indices l_j. Lemma lem:avgfunctionals (in the form of Lemma 6.1,
which allows c_flat = c_flat(l_j) to depend on the window) needs, along l_j -> infinity,
 (i) n^w_{l_j} >= 24 rho^2 K_j/(c_flat(1 - rho^2)), (ii) K_j T_hi(l_j) -> 0 (which also gives all smallness conditions of Steps 6-7 on W(l_j)).
Now K_j/c_flat <= C C_diamond^2/gamma_f <= C' G*(l)^4 (Lambda* + l + M_f)^2/(gamma_T^2 gamma_f) = C' G*(l)^4 Lambda°(l)^2 Xi_f(l), and for SLD_G,
n^w_l >= (l 2^{l^3} Lambda°(l) G*(l))^6 and T_hi(l) <= (l 2^{l^3} Lambda°(l) G*(l))^{-6}. Hence (i) holds as soon as C' Xi_f(l) <= c (l 2^{l^3})^6,
and K_j T_hi(l_j) <= C'' G*^2 (Lambda* + l + M_f)/gamma_T * (l 2^{l^3} Lambda° G*)^{-6} <= C'' Xi_f(l)^{1/2} (l 2^{l^3})^{-6} -> 0. By (W_inf) choose
l_j with Xi_f(l_j)/(l_j 2^{l_j^3})^6 -> 0. Lemma lem:avgfunctionals: rho bar g_j in C(f), rho bar g_j -> rho g.

**Step 9 (engineering).** The averaged data bar D_j are d-neutral two-piece data for bar g_j (sign conditions, vanishing off F ∪ K, finite
supports in Q_m, both representations and Delta d = 0 are preserved by averaging); by convexity kappa_w(rho bar D_j) <= rho^2 (1 + eta_0/2) <= 1.
Corollary cor:D1 (no hypothesis on Q_m, K or T) gives (f, rho bar g_j) in cl NA; let j -> infinity, then rho -> 1. QED (Theorem 3.1).

## 4.1 Consequences and remarks
**Corollary 4.1 (original design; f-dependent Hoffman constants).** PROVED. Let H^Z_f(l) be the largest l_1-Hoffman constant, over finite U with
U_fix ⊂ U ⊂ B ∩ [1, l], of the systems defining Z'_{kappa(f,U)} (violation viol') and Z_U (violation viol_{kappa(f,U)} + sum_m |delta_m|).
Steps 3-5 hold with G*(l_*) and the repair step replaced by H^Z_f(l_*) (then C_diamond <= C_3 H^Z_f(l_*)^2 (Lambda* + l_* + M_f)/gamma_T, and
(DR) is not needed). Consequently, for the ORIGINAL SLD, f in R provided F finite, (H2'), (H3) and
  (W_inf^orig)  liminf_l H^Z_f(l)^4 Lambda°(l) Xi_f(l)/(l 2^{l^3}) = 0
(Step 8 with n^w_l >= l 2^{l^3} Lambda°(l), T_hi(l) <= 2^{-l^3}/(l Lambda°(l))). Under (DR), H^Z_f(l) <= C_f G*(l) by Lemma 2.3.

**Corollary 4.2 (Theorem thm:S revisited).** PROVED. (a) Under (B_res): q_l = 0 on B (d-neutral strict non-peaks), so (DR) is trivial and
M_f = 0; resonance gives T(B) \ F ⊂ K, so gamma_T = 1; gamma_f = min_m M_m; (H2) implies (H2'); the r*_l(l_*) of 3.1 dominate those of
def:swallowed (fewer points are removed), so (W*) implies (W_inf). Hence R_S ∩ (B_res) ⊂ R_SBinf for SLD_G.
(b) Under (B_fin): U = B for small t, so H^Z_f, M_f, gamma_f, gamma_T are eventually constant, and once C_diamond t^2 <= lambda_B :=
min_B lambda_l the bound |tau'_l|/lambda_l <= (6 + 1)/t keeps A_2 = 11 fixed; then c_flat is an f-constant and Step 8 needs only
C_diamond(l) = o(n^w_l), which (W*) gives (C_diamond <= C Lambda*_f). This is Theorem thm:S (B_fin) for both designs.
So Theorem 3.1 / Corollary 4.1 contain Theorem thm:S and remove from it (H1), resonance, d-neutrality and the finiteness of B, and weaken (H2)
to (H2'); the price is the growth hypothesis (W_inf) (resp. (W_inf^orig)) and, for SLD_G, (DR).

Remark 4.3 (what the new ingredients are). (1) Scale-dependent active set U = {l in B ∩ [1,l_*] : lambda_l >= t^2}: inactive swallowed carriers
are box-negligible in total (at most 6 l_* t), and active ones have lambda_l >= t^2, which converts the l_1-displacement of the projection into
the coordinate bound |omega| <= A_2/t needed by the one-sided expansion. (2) Configuration Hoffman constants G*(l) (part 2): the f-dependence of
the zero-cost cone is finite-combinatorial on T(U); the continuous f-data are isolated in gamma_T (rooms of free target points), the peak rows
(margins, M_f), the d-rows (repair, R_f) and gamma_f (gaps). (3) The uniform shift is pinned without (H2) through BASE peaks: at an anti-sign
swallowed peak the zero-cost condition (Z1) bounds (tau_l)_- by the projection distance, which bounds Delta d_m M_m from above; at a
swallowing-sign swallowed peak the margin bounds the excess e_k, which bounds Delta d_m M_m from below (Step 3).

# Z4 part 5: the model case (O3) — maximal contact

Setting: SLD (or SLD_G), N fixed, f with F finite and z ≡ eps_0 on N \ F (eps_0 in {±1}). Then K = N \ F, J = ∅, every carrier is
swallowed with eps_l = eps_0 (r_l = 0 for all l: Remark rem:Bpm(a)), B = L_N.

**Lemma 5.0 (peaks of both signs).** PROVED. In every block m there are infinitely many peaks k with w_m(k) = +M_m and infinitely many with
w_m(k) = -M_m, all with margins >= q_0/4 for k large.
*Proof.* q**(zhat) = 1, so there is y in S_{q*} with y(zhat) > 3/4; by (T-d) there are k -> infinity with q*(u_{k,m} - y) -> 0, hence
u_{k,m}(zhat) > 1/2 for those k (|v(zhat)| <= q*(v)); as Phi_m(k) -> 0, Lemma lem:threshold makes k a peak with w = +M and margin
mu = q_0(|u(zhat)| - hat theta Phi_m(k)) >= q_0/4 for large k (hat theta := |R**zhat| M/(mC) as in the proof of Lemma lem:scrambling). Use -y. QED.

**Proposition 5.1 (rigidity: two-piece data are d-neutral at maximal contact).** PROVED. Every two-piece data (b^±, omega^±) for a
functional g at f (Definition def:twopiece) satisfy Delta d_m := d_m(omega^-_m) - d_m(omega^+_m) = 0 for every m. Consequently the
non-negative mismatch allowed by Corollary cor:D1 is never available at maximal contact.
*Proof.* v := b^+ - b^- = sum_m R_m^*(delta omega_m - Delta d_m w_m), delta omega := omega^- - omega^+ (finitely supported in the Q_m), and
eps_0 v(j) >= 0 for every j notin F (sign conditions on K = N \ F). Fix m and, by Lemma 5.0, swallowed peaks l^± of block m with
w(k(l^±)) = ±M_m and S_{l^±} ∩ F = ∅. Let T_omega be the (finite) union of the target supports of the carriers in the supports of the
delta omega_{m'}. For s in S_{l^±} \ T_omega: the delta omega-terms vanish at s (their carriers are strict non-peaks, hence != l^±, so
their signatures vanish at s, and their targets miss s). For every block m', (R_{m'}^* w_{m'})(s) = [m' = m] lambda_{l^±}(±M_m) v_{l^±}(s) +
rest, where rest collects targets y_{l'} meeting s; such l' satisfy l' > l^± (allowedness (a)) and 2c_{l'} <= 2^{-2s} c_{l^±} delta_{l^±}
(allowedness (b)), so |rest| <= (4/3) sum_{l' >= L(s)} lambda_{l'} <= (2/9) 2^{-2s} c_{l^±} delta_{l^±} per block. Since
lambda_{l^±} v_{l^±}(s) >= (4/5) m 2^{-m-k(l^±)} c_{l^±} delta_{l^±} 2^{-s}, for s in S_{l^±} large (how large depending also on
max_{m'}|Delta d_{m'}|/|Delta d_m|, since v(s) = -sum_{m'} Delta d_{m'} (R_{m'}^* w_{m'})(s); see Proposition 5.6) the sign of v(s) is the sign of
-Delta d_m (±M_m) (if Delta d_m != 0). The sign condition at such s for l^+ and for l^- gives eps_0 Delta d_m <= 0 and eps_0 Delta d_m >= 0. QED.

**Proposition 5.2 ((H2') is automatic).** PROVED. By Lemma 5.0, each block has a swallowed peak of swallowing sign (w = eps_0 M) with
positive margin (l^up_m) and a swallowed peak of anti sign (l^dn_m); so (H2') of part 3 holds.

**Lemma 5.3 (signature lift).** PROVED for designs with c_l <= (delta_l ||h_l||_1)^2 for all l (an extra clause that can be added to (D1),
since ||h_l|| is fixed by (D0) before c_l is chosen; Proposition 2.4 is unaffected). There is l_0 (depending on f) such that every carrier
l >= l_0 with eps_0 y_l(zhat) >= 0 is a peak of swallowing sign with margin mu_l >= q_0 delta°_l/4.
*Proof.* For l large, S_l ∩ F = ∅ and sup_{S_l} |Ue| <= 1/4 (Ue in c_0), so eps_0 h_l(zhat) = ||h_l||_1 + eps_0 <h_l, Ue> >= (3/4)||h_l||_1.
Then eps_0 u_l(zhat) >= (3/4) delta°_l, while hat theta Phi_l <= hat theta c_l <= hat theta delta°_l^2 (5/4)^2 <= delta°_l/4 for l large. QED.
Hence M_f(l) <= 4 l Lambda°(l)/q_0 + M^canc_f(l), where M^canc_f(l) sums 1/mu over swallowing-sign peaks l' <= l with
eps_0 y_{l'}(zhat) < 0 (**signature-cancelling** carriers: the target value cancels most of the signature lift); likewise every strict
non-peak (|u_l(zhat)| < hat theta Phi_l) is signature-cancelling, and its gap is small only if |u_l(zhat)| is close to hat theta Phi_l.

**Corollary 5.4 (maximal contact).** PROVED (from Theorem 3.1, Prop. 5.2). For SLD_G, a maximal-contact first row f with F finite is in R
provided (H3) (no degenerate peak with w = eps_0 M), (DR), and
  liminf_l (1 + M^canc_f(l)/Lambda°(l))^2 / (gamma_f(l) (l 2^{l^3})^6) = 0.
(At maximal contact gamma_T = 1, and Lambda*_f(l) <= C_F Lambda°(l) because r*_l = 2 delta°_l, 1 + 3/(2 delta°_l) <= 1 + 2/delta°_l, for the
cofinitely many l with S_l ∩ F = ∅; so Xi_f(l) <= C (1 + M_f(l)/Lambda°(l))^2/gamma_f(l), and M_f/Lambda° <= 4l/q_0 + M^canc_f/Lambda°.)
For the original SLD the same holds with the factor H^Z_f(l)^4 Lambda°(l) of Corollary 4.1 and (l 2^{l^3})^6 replaced by l 2^{l^3}; there (DR)
is not needed.

**What is left of (O3).** Maximal contact first rows not covered by Corollary 5.4 / Corollary cor:BTrecovered must have one of:
 (a) a degenerate peak of swallowing sign (failure of (H3));
 (b) signature-cancelling swallowing-sign peaks whose margins decay so fast that M^canc_f(l)/Lambda°(l) is not o((l 2^{l^3})^3) along any
     subsequence (super-fast WEAK PEAKS), or strict non-peaks with gaps decaying faster than (l 2^{l^3})^{-6} (super-fast NEAR-THRESHOLD
     carriers) — both are (O1)(ii)-type objects;
 (c) failure of (DR) for SLD_G: some block has swallowed strict non-peaks with q_l != 0 but the zero-cost cone {tau >= 0 : sum tau_l u_l is
     eps_0-signed off F} contains no element with d-sum of one of the two signs (ONE-SIDED d-RESOURCES); for the original design: growth of
     the f-dependent Hoffman constants H^Z_f.
Note that for (b) the obstruction is not the number of swallowed carriers (B = L_N is handled) but the size of 1/margin and 1/gap; and for
(c) Proposition 5.1 shows that Corollary cor:D1's Delta d >= 0 cannot help.

**Remark 5.5 (scope of Corollary 5.4 beyond (BT)).** PROVED parts: (i) if M_f(l) <= (l 2^{l^3})^3 for all large l (so that (W_inf) is not
violated by M_f), then the margin-sparsity sum of (MS) restricted to swallowing-sign peaks is o(s): every margin of a swallowing-sign peak l is >= 1/M_f(l) >= nu_l := (l 2^{l^3})^{-3}, and
sum{Phi_k : mu_k < s} <= sum_{l >= l(s)} c_l <= (4/3) c_{l(s)}, l(s) := min{l : nu_l < s}, while c_{l(s)} <= T_lo(l(s)-1)^3 = o(nu_{l(s)}) = o(s)
(anti-sign peaks are not controlled by M_f, and Theorem 3.1 does not need them to be). (ii) Hence the maximal-contact first rows that
Corollary 5.4 adds to Corollary cor:BTrecovered are those violating (BT) through infinitely many strict non-peaks (with (DR) and gaps not
decaying faster than the ladder), or through weak or degenerate peaks of ANTI sign (failure of (MS) or degenerate peaks on the anti side). Failure of (MS) through
super-weak swallowing-sign peaks (margins comparable to Phi), and degenerate swallowing-sign peaks, are NOT covered: they are case (a)/(b)
of "what is left of (O3)". HEURISTIC: perturbing f to remove a super-weak peak (pushing u_l(zhat) below or above threshold) creates room or
near-contacts of the same tiny size elsewhere (on S_l or at a target coordinate), i.e. it converts (E-a) into (E-b), (E-c) or (E-e); no
perturbation of f removes the smallness.

**Proposition 5.6 (rigidity of the d-mismatch, general F finite).** PROVED. Let (b^±, omega^±) be two-piece data at f (F finite) with
Delta d_m := d_m(omega^-_m) - d_m(omega^+_m) != 0 for some block m. Put Delta := max_{m'} |Delta d_{m'}| and let T_omega be the finite union
of the target supports of the carriers in supp omega^±. For every peak carrier l of block m with S_l ∩ F = ∅, every s in S_l with
s > max T_omega and 2^{-s} < (2/5) |Delta d_m| M_m m 2^{-m-k(l)}/(N Delta) satisfies |z_s| = 1 and z_s = -sign(Delta d_m) sign(w_m(k(l))).
In particular Delta d_m = 0 as soon as block m has one peak carrier with infinitely many free points on its signature set, or infinitely
many contact points of each sign on one signature set, or two peak carriers of opposite signs whose signature sets carry infinitely many
contact points of the same sign (maximal contact: Proposition 5.1).
*Proof.* v := b^+ - b^- = sum_{m'} R_{m'}^*(delta omega_{m'} - Delta d_{m'} w_{m'}). At s as above the delta omega-terms vanish (s is outside
T_omega and outside the signature sets of the carriers in supp omega, which are strict non-peaks, hence different from l). For m' != m only
targets of carriers l' > l meet s (allowedness (a)), so |(R_{m'}^* w_{m'})(s)| <= (2/9) 2^{-2s} c_l delta_l (allowedness (b), as in the proof of
Proposition 5.1); for m' = m the same bound holds for (R_m^* w_m)(s) - lambda_l w_m(k(l)) v_l(s), and |lambda_l w_m(k(l)) v_l(s)| >=
(4/5) M_m m 2^{-m-k(l)} c_l delta_l 2^{-s}. Hence |v(s) + Delta d_m lambda_l w_m(k(l)) v_l(s)| <= N Delta (2/9) 2^{-2s} c_l delta_l <
|Delta d_m lambda_l w_m(k(l)) v_l(s)| by the choice of s, so sign v(s) = -sign(Delta d_m) sign w_m(k(l)) != 0. Two-piece data force v = 0 off
F ∪ K and z_j v(j) >= 0 on K; so s in K and z_s = sign v(s). QED.
Consequence: the option Delta d_m >= 0 of Corollary cor:D1 can only be used at first rows whose block-m peak signatures are all swallowed far out
with signs -sign(Delta d_m) sign(w(k(l))) ("peak-aligned swallowing"); outside that configuration two-piece data are d-neutral, and route (1)'s
"handle Delta d != 0 by Corollary cor:D1" has no room. (SC)/Theorem thm:engineered for Delta d < 0 is subject to the same rigidity, since it
concerns the same two-piece data.

# Z4 part 6: what remains, precisely; route (2) verdict; the averaging lemma with scale-dependent c_flat

## 6.1 A bookkeeping lemma used in part 4
**Lemma 6.1 (windowed averaging with window-dependent c_flat).** PROVED. Theorem thm:windowed and Lemma lem:avgfunctionals remain true if
c_flat is allowed to depend on j (c_flat = c_{flat,j} in (0,1]), provided n_j >= 24 rho^2 K_j/(c_{flat,j}(1 - rho^2)) for every j.
*Proof.* In the proof of Theorem thm:windowed, j is fixed from the second sentence on; c_flat enters only through I_r := {i : c_flat t_i <
rho|r|}, the bound sum_{I_r} t_i < 2 rho|r|/c_flat and Q := 2 rho^2 K/(c_flat n) <= (1-rho^2)/12, all for that j. QED.
(Part 4, Step 8 uses this with c_{flat,j} = c_flat(l_j).)

## 6.2 The residual obstruction after Theorem 3.1 (F finite)
Theorem 3.1 (with Corollaries 4.1, 4.2, 5.4) reduces every remaining case of (O2) and (O3) with F finite to at least one of the following
**first-order inexact resources** on swallowed signature sets (for SLD_G; for the original SLD add the growth of H^Z_f):
 (E-a) swallowing-sign swallowed peaks that are degenerate ((H3) fails) or whose margins decay faster than the ladder (M_f large);
 (E-b) swallowed strict non-peaks with gaps decaying faster than the ladder (gamma_f small): near-threshold carriers;
 (E-c) free target coordinates (|z_j| < 1) with rooms decaying faster than the ladder (gamma_T small): near-contacts met by swallowed targets;
 (E-d) one-sided d-resources: (DR) fails (zero-cost cone has d-sums of one sign only in some block), so exact d-neutral data would have to
       drop genuine switching (Proposition 5.1 forbids Delta d != 0 at maximal contact);
 (E-e) good signature sets whose rooms r*_l(l_*) decay too fast or vanish once coarse swallowed targets are removed (Lambda* large) —
       this is approximate swallowing, (O1)(i).
In every case the window data at scale t are two-piece data up to a FIRST-ORDER defect of size O(t) (block excess |alpha(k)| |tau omega(k)|
at weak peaks, overshoot beyond the gap, room-weighted base mass, d-defect times wrong-signed R*w mass). HEURISTIC (but each step is a
one-line estimate): such defects cannot be averaged away, because the one-sided expansion (i) of Lemma lem:avgfunctionals must hold for
|r| <= c_flat t down to r -> 0, where a defect delta |r| with delta ~ K t is not <= eta r^2; and Theorem thm:engineered tolerates first-order
defects only of size o(s_1)|tau|, s_1 -> 0, whereas averaged data have a fixed defect ~ K t_top/n. So the common core of (O1), and of what is
left of (O2)/(O3), is:

**Problem 6.2 (exact data for inexact resources).** For the designed operator and F finite: given swallowed signature sets on which the
switching uses weak peaks, near-threshold strict non-peaks, near-contacts or one-sided d-resources, find, on long windows of scales, functionals
g_t with ||g - g_t|| <= K t and EXACT two-piece data, or an engineering theorem accepting data whose first-order defect is O(t) at window
scale t (a multi-scale version of Theorem thm:engineered, in which the engineering scale s_1 and the data scale are coupled).

## 6.3 Route (2) verdict (lower semicontinuity along far lowerings)
(a) PROVED (Prop. 1.2): p*(f^L - f) <= C_f eps_L <= C_f c_{L+1}/2.
(b) PROVED (Prop. 1.3): on all scales that f^L inherits from f through the rho-slack, the carriers made roomy are negligible (total switching
O(t)), and the coarse ones are swallowed exactly as at f. Therefore dist(rho g, C(f^L)) -> 0 requires on the band [A t_L, T] the same
exact matching of the finitely many coarse swallowed carriers that Theorem 3.1 performs at f itself; when the hypotheses of Theorem 3.1 hold,
f in R directly and no lowering is needed.
(c) HEURISTIC: when they fail because of (E-a)-(E-d) (f-dependent growth), far lowering cannot help: the band length (about
(1/2) log2(1/c_{L+1}) dyadic scales) is a DESIGN quantity, while the constants of the coarse matching at level L (1/margins, 1/gaps,
Hoffman constants of the d-rows) are f-quantities, and f is chosen after T. (A proof would need to construct, for any given design, a first row
whose level-L constants exceed any given function of L; not attempted.) Lowering by a factor, or on far points of coarse sets, is worse:
the created room pins only at scales t^2 <~ lambda_l room_l, which the slack of that lowering does not reach (Z1's transition band; part 1).
(d) The second open question of (O2), "are all finitely swallowed first rows in R?", is answered for those satisfying (H2'), (H3) and
(B_fin) by Corollary 4.2(b) — no (DR), no (H2), no resonance needed — and stays open only when (H3) or (H2') fails (a degenerate swallowing-sign
peak; or a block all of whose non-degenerate peaks are swallowed and which lacks a swallowing-sign non-degenerate swallowed peak or an
anti-sign swallowed peak). For finitely many swallowed carriers, margins, gaps, rooms of the finitely many target points and the Hoffman
constants of the finitely many cones are fixed positive (finite) numbers, so (E-a) with mu > 0, (E-b), (E-c), (E-d) are harmless there.

## 6.4 Proposal: the modified design SLD_G (summary for the note)
SLD_G = Definition def:SLD with (i) n^w_l and T_hi(l) inflated by the configuration Hoffman constant G*(l) (part 2.4), and (ii) the extra
clause c_l <= (delta_l ||h_l||_1)^2 (Lemma 5.3). All proved results of Section 8 survive verbatim (Proposition 2.4: only (T-a)-(T-d),
(P1)-(P3) and allowedness are used). New: Theorem 3.1 (S_Binf) and its corollaries hold for SLD_G with the f-dependent growth hypothesis
(W_inf) only; for the original SLD they hold under (W_inf^orig), which includes the f-dependent Hoffman constants H^Z_f.

## 6.5 Cross-reference (parallel Round-5 work, not refereed here)
Z3 (case (O1)) reports a "moved first row" version of the engineering (exact data at a nearby f_j with p*(f_j - f) = o(T_lo^2)) and a BAND
limit (carriers with room between T_lo^2 and 1/K can be neither pinned nor exactified). Part 8.2 above is the same limit for weak peaks
(margin in place of room); the obstruction (E-a)-(E-e) of 6.2 is thus the band phenomenon of (O1) appearing inside (O2)/(O3). Naming: the
theorem of part 3 is called S_Binf (infinitely many swallowed carriers, F finite); it is unrelated to the "Theorem S-inf" of Z5 (infinite F).

# Z4 part 7: finite-model sanity check (signs and algebra only)

Script: r5/Z4_work/maxcontact_toy.py (cvxpy/CLARABEL SOCP). Model: 14 base coordinates, F = {0,1}, z = +1 on every other coordinate
(maximal contact, every signature set swallowed with eps = +1), one block of 5 carriers with private 2-point signatures, targets of both
signs on shared coordinates and finer targets touching a coarser signature (allowedness-(b)-like), so that peaks of both signs occur.
Mates g are random directions scaled to 0.999 x the contractive boundary; two-sided decompositions are SOCP-optimal decompositions of
f ± t g, t in {3e-2, 1e-2, 3e-3}, three mates per seed, seeds 3, 5, 11.
Results (max over all instances):
| check | quantity | seed 3 | seed 5 | seed 11 |
|---|---|---|---|---|
| (c1) eq:peakshift identity residual | should be ~0 | 1.6e-5 | 6.2e-5 | 7.6e-5 |
| (c2) Step 3 upper bound via anti-sign swallowed peak: Dd M - (tau)_-/lam | <= 0 | -2.3e-3 | -2.6e-3 | -2.4e-3 |
| (c3) Step 3 lower bound via swallowing-sign peak: tau/lam - t/(sigma|alpha|) - Dd M | <= 0 | -3.3e-2 | -5.5e-2 | -4.3e-2 |
| (c4) switching budget at maximal contact: sum 2(Delta B)_- - t/q0 | <= 0 | -3.5e-3 | -3.0e-3 | -2.9e-3 |
(The c1 residuals are solver noise amplified by 1/t.) Finite models are norm attaining and degenerate, so this only confirms the signs
of the new pinning mechanism of Step 3 (base peaks pin the uniform shift without (H2)); it says nothing about infinite-dimensional
phenomena (weak peaks, near-threshold carriers).

# Z4 part 8: degenerate swallowing-sign peaks (failure of (H3)) — a reduction to steering; weak peaks

## 8.1 Data with one-sided use of degenerate peaks
Call (b, omega) **side-+ admissible with degenerate peaks** if it is as in Definition def:twopiece except that omega_m may also be nonzero at
degenerate peaks k (alpha_m(k) = 0), with sign(w_m(k)) omega_m(k) <= 0 there; side - with >= 0 ("inward" moves).
**Lemma 8.1 (exactness at f).** PROVED. For such data (finitely supported omega) the first-order terms vanish and the block expansion is the
one of Lemma lem:block: for 0 < r small (side +), with W := (1 - d r) w_m + r omega_m and d := d_m(omega_m),
||W||_inf = (1 - d r) M_m (inward coordinates stay below the level, peaks with alpha != 0 are untouched since omega vanishes there), and
lin_m(W) = r <omega_m, alpha_m> + r(d - d) = 0 because alpha_m vanishes at degenerate peaks; hence N_m(W) <= 1 + (r^2/2) H_m(omega_m)(1 + O(r)).
Consequently Lemma lem:onesidedtransfer holds for such data (degenerate-peak coordinates need no radius, only |r omega(k)| <= M_m), and
windowed averaging produces averaged data of the same kind.
**Window data.** In Theorem 3.1 drop (H3) and, for a degenerate swallowing-sign peak l in U, replace the row tau_l = 0 of (Z3) by nothing
((Z1) already gives tau_l >= 0); define omega^+(k(l)) := -varsigma_l min(|omega_+(k(l))|, tau'_l/lambda_l) and omega^-(k(l)) := omega^+(k(l)) +
eps_l tau'_l/lambda_l. Then varsigma omega^+ <= 0 <= varsigma omega^- (because varsigma_l eps_l = 1 and tau'_l >= 0), the d-rows are exact, and
the discrepancies with the actual decomposition are lambda rho_k <= lambda |Delta d M| + |tau_l - tau'_l| on both sides (using tau_l/lambda_l =
Delta d M + e_k, e_k >= |omega_+(k)|). PROVED (same bookkeeping as Step 6). So Steps 1-8 of Theorem 3.1 go through without (H3), and M_f only
counts NON-degenerate swallowing-sign peaks.
**The missing step (SKETCH, not proved): engineering with degenerate peaks.** Corollary cor:D1 must accept such data. At an engineered
approximant f' the used degenerate peaks k (finitely many, D) have margins mu'_k = O(s_1) of unknown sign; if mu'_k > 0 the inward move costs
alpha'(k) |tau omega(k)| = O(s_1)|tau| with a constant proportional to the switching through k, which is not <= delta s_1|tau|/16 in general.
Remedy (sketch, with an extra hypothesis): add to a'' tuning masses A_j s_1 z_j e_j (A_j >= 0 fixed) at finitely many far contacts j outside
the essential support of b^±. To first order in s_1, mu'_k changes by s_1 sum_j A_j V_j(k) + (window-mass contribution, O(s_1), sign unknown),
where V_j(k) := varsigma_k (d/dm) [u_k(zhat') - theta'_hat Phi_k] for a unit mass at j (a Hilbert-part term <P^perp U* u_k, U* e_j> z_j/nu plus
a common threshold shift in each block). Steering all k in D to the anti side needs the convex cone generated by {V_j} to contain a vector with
all coordinates negative ("steerability"); this is an f-dependent hypothesis (at maximal contact z_j = eps_0 is fixed, so the signs come only
from (U P^perp U* u_k)_j and the threshold shift). Steering through the signature of the degenerate carrier itself always has the right sign
but costs, at first order, (push) x (switching through k), which Theorem thm:engineered cannot absorb; steering through target coordinates
meets the same cost. With steerability, each k in D becomes a strict non-peak of f' at which inward moves are free, (E4) holds for omega
supported on Q ∪ D (at a degenerate peak Phi^2 w(k)/C = zeta(k)/sigma because alpha(k) = 0), and the one-sided Lemma lem:block at f' is as in
Lemma 8.1; writing out Theorem thm:engineered under steerability is the remaining step. Without steerability (H3)-failure stays OPEN.

## 8.2 Weak peaks: why degeneration does not help (HEURISTIC)
A swallowing-sign swallowed peak with small margin mu_l > 0 cannot be used in exact data at f (its inward use costs alpha(k) r|omega(k)| at
first order, and windowed averaging needs exactness as r -> 0), so its switching must be projected away at cost t/mu_l (this is M_f). Making
it degenerate by perturbing f costs p*(f' - f) of order lambda_l mu_l (heuristic lower bound; upper bound by Prop. 1.2-type estimates), so f'
inherits the mates of f only above t ~ (lambda_l mu_l)^{1/2}; for the window arithmetic one needs a whole window above that threshold and
M_f absorbed by the window, i.e. mu_l <= T_lo(l_j)^2/lambda_l for the degenerated peaks and mu_l >~ (l_j 2^{l_j^3})^{-3} for the others —
the intermediate margins are covered by neither. This is the (E-a) obstruction in its sharpest form.

