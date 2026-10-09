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
