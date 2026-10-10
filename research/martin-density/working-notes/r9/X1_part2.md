# X1 part 2 — Status coherence WITHOUT (KN): the weights of the switching carriers never enter the exact cone

Setting: U1 + U1-ref (design D^{U1'} on T_final, diagonal mu-base, N fixed, F finite), clean sub-window w of a main stage L >= l_f,
activity class a, companion construction of U1-ref Prop. KN.  Notation of part 1.  For a block m: Omega_a(m) active Omega carriers,
N(m) ⊂ Omega_a(m) the active NEAR-THRESHOLD ones (|rho - 1| <= b(w) at f), P_rob(m) the coarse peaks with rho >= 1 + u(w),
sigma_rob(m) := sum_{P_rob(m)} Phi^2, K_floor := K(sigma_rob(m), R_a(m)^2).

## 2.1 Two cases per block (a dichotomy of rate objects).  PROVED.
At a clean w every coarse carrier has rho in [0,b] ∪ [u,1-u] ∪ [1-b,1+b] ∪ [1+u, inf) ((R3), (R4)).  Call block m
 (KN-block) if some coarse carrier of m that is INACTIVE in a has rho in [u, 1+b]  (an inactive strict non-peak of robust relative position,
            or an inactive near-threshold carrier, peak or not: robust inactive k-mass, part 1 Lemma F);
 (T-block)  otherwise: every inactive coarse carrier of m is nearly neutral (rho <= b) or a robust peak (rho >= 1 + u).
In a KN-block U1-ref Prop. KN applies verbatim (an inactive near-threshold peak is first pushed below threshold; it is then an inactive
Omega carrier with rho >= u).  The new case is the T-block; there the inactive k-mass is <= C D(L)^2 (b + c_{L+1}^2) (nearly neutral
inactive carriers and fine carriers only), so by Lemma F every active status at f is within C D^2 (b + c_{L+1}^2) of its floor value.

## 2.2 The weight-free inward rows.  PROVED.
For l in N(m) of a T-block, replace U1-ref's row (X4) "vs_l gamma_l/lambda_l + Delta'_m >= 0" by the FLOOR-FORM row
    (X4^0)   vs_l gamma_l + Delta'_m m^2 |r_l| K_floor(r) >= 0          (r = active ratios; K_floor as above).
(i) It is the exact inward condition at the floor: lambda_l Domega(l) = gamma_l + Delta'_m lambda_l vs_l rho_l and lambda_l rho^0_l =
    m^2 |r_l| K_floor (rho^0_l = m |r_l| K_floor/Phi_l, lambda_l = m Phi_l).
(ii) The decomposition at f satisfies it up to lambda_l (3 gap(f)/t + C_f D^2 (b + c_{L+1}^2)) <= K t (lem:suplevel(f) at strict non-peaks,
    eq:peakshift at weak peaks, |rho_l(f) - rho^0_l(r(f))| <= C D^2 (b + c_{L+1}^2) in a T-block).
(iii) Points of the cone are kind [3] at the companion f^# as soon as rho_l(f^#) <= 1 - mu/2 with mu >> |Delta'| (rho_l(f^#) - rho^0_l(r)):
    vs Domega(l) >= -|Delta'_m| (rho_l(f^#) - rho^0_l(r)) >= -3 gap^#(l)/t.
(iv) WEIGHT-FREENESS.  In the variables (Delta', gamma) every row of the shifted exact cone Gamma^#(kappa, a) of U1 2.1 (with (X3)
    divided by kappa, part 1 Lemma 1.3) has coefficients that are functions of: the vectors u_l on E_c (l in Omega_a), the peak traces
    tau_m (vectors of the peaks times their weights lambda_p), the active ratios r, sigma_rob (peak weights) and signs.  The weights
    Phi_l, lambda_l of the carriers l in N do NOT occur: (X1) has entries u_l(j) and Delta'_m tau_m(j); (X2), (X5) are sign/zero rows;
    (X3)/kappa has entries r_l; (X4^0) has entries vs_l, m^2 |r_l| K_floor(r); aggregated signature rows have one nonzero entry (their
    design coefficient does not affect the vanishing of any minor).  [U1-ref's row with "1" in place of rho^0 contains 1/lambda_l: this
    is the ONLY place where an N-weight could enter, and (X4^0) removes it.]  Also the cofactor polynomials of U1-ref (p-c) are built
    from the same matrix.  Hence the zero set Z_kappa (in ratio space) of the tiny minors of a pattern kappa is independent of the
    N-weights, and the floor statuses are
        rho^0_d(r) = psi_d(r)/Phi_d,     psi_d(r) := m |r_d| K(sigma_rob, R_a(r)^2)      (d in N),
    with psi_d independent of the N-weights.  The N-weights enter the whole problem ONLY as the denominators Phi_d.

## 2.3 Lemma NLM (no local minimum at the threshold for generic N-weights).  PROVED.
Fix a pattern kappa (finite combinatorial data of level L: active set Omega_a with signs, peak sets and signs, classes R/G, contact/free
types on E_c, tiny/robust labels of the minors, the case labels of 2.1, the set N_T of near-threshold active carriers of the T-blocks),
and all its non-N_T data (vectors, peak weights).  Let K_kappa be the compact region {r : |r_l| <= 2 Phi_l/(m k_min), R^2 <= 1 - eps_K}
(design numbers k_min, eps_K > 0), Z := Z_kappa ∩ K_kappa, and for a weight vector Phi = (Phi_d)_{d in N_T} in (0, inf)^{N_T}
     F_Phi(r) := max_{d in N_T} psi_d(r)/Phi_d     (r in Z).
COINCIDENCE: some r_0 in Z with F_Phi(r_0) = 1 is a local minimum of F_Phi on Z.  Let B_kappa := {Phi : coincidence}.
Claim: B_kappa is a semialgebraic subset of R^{N_T} of dimension < |N_T|, defined with parameters from the non-N_T data of kappa.
Proof.  Z and the psi_d are semialgebraic (minors are polynomials in the entries; K is algebraic: (1 - R^2)k^2 - 2 sigma k + sigma^2 -
sigma = 0, k > sigma), and they do not depend on Phi (2.2(iv)); B_kappa is first-order definable, hence semialgebraic (Tarski-Seidenberg).
Take a finite stratification of Z into connected Nash manifolds S compatible with {r_d > 0}, {r_d = 0}, {r_d < 0} (d in N_T)
[BCR 9.1.8]; on each S every psi_d is a Nash function.  For a nonempty D ⊂ N_T and a stratum S let CV_{D,S} be the set of critical
values of the Nash map Psi_{D,S} := (psi_d)_{d in D}|_S : S -> R^D; by the semialgebraic Sard theorem [BCR 9.6.2] dim CV_{D,S} < |D|.
Let Phi in B_kappa with witness r_0 in S and D := {d : psi_d(r_0) = Phi_d} (nonempty; psi_d(r_0) > 0 forces r_0 notin {r_d = 0}).
If (Phi_d)_{d in D} were a regular value attained at the regular point r_0, there would be v in T_{r_0} S with d psi_d(v) = -1 for all
d in D, and a Nash curve gamma in S with gamma(0) = r_0, gamma'(0) = v; then psi_d(gamma(s)) < Phi_d (d in D) and, by continuity,
psi_d(gamma(s)) < Phi_d (d notin D) for small s > 0, i.e. F_Phi(gamma(s)) < 1 = F_Phi(r_0): not a local minimum on Z.  So r_0 is a
critical point of Psi_{D,S} and (Phi_d)_{d in D} in CV_{D,S}.  Therefore B_kappa ⊂ union_{D,S} pi_D^{-1}(CV_{D,S}), a finite union of
semialgebraic sets of dimension < |D| + |N_T \ D| = |N_T|.  QED

## 2.4 Lemma GEN (algebraically independent weights avoid every coincidence).  PROVED.
Let k_0 ⊂ R be the field generated by all non-weight data of the design (entries of all candidate targets of the countable pool,
signature data delta_l, H_l, normalizations n_{l,i} for every candidate, base data mu_s, ||U||): a countable field.  If the weights
(c_l)_{l in Lambda} of a set Lambda of carriers are algebraically independent over k_0 (together with the remaining weights), then for
every pattern kappa with N_T(kappa) ⊂ Lambda the actual vector (Phi_d)_{d in N_T} is NOT in B_kappa.
Proof.  B_kappa is semialgebraic of dimension < n := |N_T|, definable over k := k_0(peak weights of kappa, weights of carriers of kappa not
in N_T) (2.3).  By cylindrical decomposition over the real closure k^rc of k [BCR 2.3.1], B_kappa is a finite union of cells; a cell of
dimension < n is contained, after a permutation of the coordinates, in the graph {x_i = phi(x_1, ..., x_{i-1})} of a continuous
semialgebraic function phi defined over k^rc, and phi satisfies a nonzero polynomial relation P(x_1, ..., x_{i-1}, phi) = 0 with
coefficients in k^rc [BCR 2.6.6].  A point of such a cell therefore has a coordinate algebraic over k^rc(other coordinates), hence over
k(other coordinates).  The coordinates Phi_d = 2^{-m(d)-k(d)} c_d (d in N_T) are algebraically independent over k (they are part of an
algebraically independent family over k_0, disjoint from the weights generating k over k_0).  QED
REMARK (the norm-one carrier).  (T-a) demands q*(Te_l) = 1 for some l; with c_1 = 1 the weight of carrier 1 is rational.  Lemma GEN
then covers every pattern with 1 notin N_T.  Two options: (a) relax (T-a) to "q*(Te_l) <= 1" (Martin's proof uses only ||T|| <= 1:
Step 2 of his Theorem 1 needs v*_{n,m} in B_Y), choose c_1 in (1/2, 1) generic; (b) keep c_1 = 1 and leave the patterns with
carrier 1 in N_T (rows with rho_1(f) = 1 EXACTLY and carrier 1 active at all large levels) as an explicit exception (OPEN).

## 2.5 Lemma QC (quantitative coherence, design constants).  PROVED.
Fix kappa with Phi notin B_kappa (Lemma GEN).  Put Y_1 := Z ∩ {F <= 1} (F := F_Phi), and for h > 0
     G_h(r) := inf{ F(r'') : r'' in Z, |r'' - r| < h }   (r in Z).
(a) mu_kappa(h) := 1 - max_{r in Y_1} G_h(r) > 0 (if Y_1 is empty put mu := 1).
(b) There are design numbers C_Y, alpha_Y in (0, 1], m_0 > 0 with: Y_1 = {} implies F >= 1 + m_0 on Z, and dist(r, Y_1) <=
    C_Y (F(r) - 1)_+^{alpha_Y} for every r in Z.
Proof.  (a) G_h is upper semicontinuous on Z (if r_n -> r and r'' in Z ∩ B(r, h) then r'' in B(r_n, h) eventually, so limsup G_h(r_n)
<= F(r'')).  Y_1 is compact.  For r in Y_1: if F(r) < 1 then G_h(r) <= F(r) < 1; if F(r) = 1 then r is not a local minimum of F on Z
(Phi notin B_kappa), so G_h(r) < 1.  A usc function on a compact set attains its maximum.  (b) If Y_1 = {} the continuous function F - 1
is positive on the compact Z, so has a positive minimum m_0.  Otherwise f_1 := dist(., Y_1) and f_2 := (F - 1)_+ are continuous
semialgebraic on the compact Z with f_2^{-1}(0) = Y_1 = f_1^{-1}(0); the Lojasiewicz inequality [BCR 2.6.7] gives f_1^{1/alpha_Y} <= C f_2.  QED
All of mu_kappa(.), C_Y, alpha_Y, m_0 are determined by kappa (design data of level L); there are finitely many kappa at level L.

## 2.6 Proposition KN^tr (exactification with threshold protection, no (KN)).  PROVED (modulo U1-ref Prop. KN, refereed tools).
Design: D^{U1'} on T_final with the weights c_l (l >= 2; and c_1 under option (a)) algebraically independent over k_0 [Lemma W'], and
the rate scheme enlarged by: the minors (in the variables (Delta', gamma) of the cone with rows (X4^0) in T-blocks and U1-ref's (X4) in
KN-blocks) and their cofactor polynomials, for all patterns and classes of level L; the sub-window thresholds re-defined by
     eta'(w) := T_lo(w)^4/(L Design(L)),   b(w) := min over patterns kappa of level L of the largest b satisfying
     C_L b^{2/N_L} <= eta'/3,   b + C_* (Lip C_L b^{2/N_L} + D(L)^2 b) <= min(m_0(kappa)/2, (eta'/(3 C_Y))^{1/alpha_Y}),
and c_{L+1} so small that C D(L)^2 (c_{L+1}^2 + Design(L) b(w)) <= mu_kappa(eta'(w)/3)/8 for all w, kappa of level L.
Statement.  At a clean sub-window w of a main stage L >= l_f and a class a, there is a companion f^(1a) such that: (i) the active ratios
lie on Z_kappa (all tiny minors vanish exactly), every robust minor is >= u/2; (ii) in T-blocks every active near-threshold carrier has
rho <= 1 - mu_kappa(eta'/3)/2 (a strict non-peak with gap >= M mu/2), in KN-blocks U1-ref Prop. KN(b) holds; every other coarse carrier
keeps its robust status; (iii) p*(f^(1a) - f) <= C_f Design(L) eta' log(1/eta') = o(T_lo(w)^2).
Proof.  Step 0: V1's (C1), (C2).  Step 1 (Lojasiewicz in ratio space, V2 Lemma L in its semialgebraic form): r' in Z_kappa with
|r' - r(f_1)| <= C_L b^{2/N_L} <= eta'/3.  At r', F(r') <= 1 + b + Lip C_L b^{2/N_L} + C D^2 b =: 1 + delta_0 (floor statuses at f are
within C D^2 b of the true ones in a T-block, 2.1).  Step 2: by 2.5(b), Y_1 is nonempty (delta_0 < m_0) and there is r_1 in Y_1 with
|r_1 - r'| <= C_Y delta_0^{alpha_Y} <= eta'/3.  Step 3: by 2.5(a) there is r'' in Z with |r'' - r_1| < eta'/3 and F(r'') <=
1 - mu_kappa(eta'/3).  Step 4 (realization, as U1-ref Prop. KN Step 2): push the (nearly neutral) inactive Omega carriers of T-blocks to
value 0 (cost <= C b), Lemma TU on the active values with targets u_l := r''_l kappa, peak push restoring kappa (IVT), re-solve (block
triangular Jacobian); in KN-blocks additionally the inward lever push of U1-ref.  Statuses: by Lemma K/F, in a T-block every
rho_l = m |r''_l| K(sigma, R^2)/Phi_l with sigma - sigma_rob, R^2 - R_a^2 <= C (c_{L+1}^2 + nothing else), so rho_d <= F(r'') + C D^2
c_{L+1}^2 <= 1 - mu/2 for d in N_T; robust statuses move by <= Lip eta' << u.  Costs: V1 Lemma CO / TU(d).  QED

## 2.7 Addenda to 2.5-2.6 (polynomial margin; gap(f) <= gap^#).  PROVED.
(c) of Lemma QC: h -> mu_kappa(h) is semialgebraic (first-order definable from the pattern data), positive and nondecreasing on
    (0, h_0); by the Puiseux expansion of one-variable semialgebraic functions at 0 there are design numbers c_kappa > 0, beta_kappa > 0
    with mu_kappa(h) >= c_kappa h^{beta_kappa} for 0 < h <= h_kappa.  Hence in Proposition KN^tr the T-block gaps satisfy
       gap^# >= (M/2) c_kappa (eta'(w)/3)^{beta_kappa} = (M/2) c_kappa (T_lo(w)^4/(3 L Design(L)))^{beta_kappa},
    a POLYNOMIAL bound in T_lo(w) with design exponent (U1-ref's KN-gaps are c_f eta D M, linear in eta').
(d) Add to the definition of b(w): b(w) <= M_min mu_kappa(eta'(w)/3)/8 for all kappa of level L (M_min := 1/2 <= M_m).  Then every
    active near-threshold carrier of a T-block has gap(f) <= M b(w) <= gap^#/4, so the clamped + side of V1 TR (vs omega^+(k) <=
    (1 - d_+ t) gap(f)/t, lem:suplevel(f)) satisfies the kind-[3] bound vs omega^+(k) <= 1.5 gap^#/t at the companion, and U1-ref 4.1's
    derivation of kind [3] for the - side (cone row + V1 TR Step 5 shift trick) applies with (X4^0) in place of (X4) (2.2(iii)).
(e) The gaps enter U1-ref's assembly only through kind [3] (qualitative, given (d)); no window constant K (Hoffman constants, A_max,
    D_cls) contains 1/gap^#, so the window arithmetic of U1-ref (Q(w) >= D_cls (Design/u)^C) is unchanged.
