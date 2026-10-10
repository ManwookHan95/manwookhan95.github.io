# U1 referee notes (Round 8): proofs of the fixes, the status-rigidity lemma, and the corrected Master Theorem IV'

Notation of U1 and of the note (lem:threshold): for a block m and a first row, zeta = R_m^** zhat, A = |zeta|_m, M + C = 1, theta = A M/C,
nu_k = |zeta(k)|/Phi_k^2 = m |u_k(zhat)|/Phi_k, rho_k = nu_k/theta (peak iff rho >= 1), P = peaks, Q = strict non-peaks, Phi_P^2 = sum_P Phi^2.
Omega ⊂ Q is the switching set, kappa = [A(A + theta) - sum_Omega nu^2 Phi^2]/theta = A + theta Phi_P^2 + S_f/theta, S_f := sum_{Q\Omega} nu^2 Phi^2.
Data convention Delta = d(omega^-) - d(omega^+), Delta' = Delta M.  Labels PROVED / SKETCH / HEURISTIC / OPEN.

## 1. Continuity of kappa (no jumps).  PROVED.
kappa = [A(A + theta) - sum_{k in Omega} nu_k^2 Phi_k^2]/theta depends on zeta through A (a norm), theta (the unique root of the threshold
equation of Y1 Lemma T, continuous in zeta in l_1) and nu_k, k in Omega; so it is continuous in zeta as long as Omega ⊂ Q (the hypothesis of
U1 Lemma 1.3).  In the second form, a carrier k notin Omega crossing the threshold (nu_k = theta) contributes theta Phi_k^2 to theta Phi_P^2 on
one side and nu_k^2 Phi_k^2/theta = theta Phi_k^2 to S_f/theta on the other: no jump.  Hence in U1 4.1 (1a), (1c) the intermediate value
theorem is exact (|kappa^# - kappa'| = 0 after the push), and Lemma 4.6(a)'s first term is only the drift of step (2).

## 2. Lemma R-kt (status rigidity in ratio space).  PROVED.
Statement.  Fix a block (index m), its peak set P and its switching set Omega ⊂ Q.  Put r_l := u_l(zhat)/kappa (l in Omega), R^2 := m^2 sum_Omega r_l^2,
a := A/theta, k := kappa/theta, s_f := S_f/theta^2.  Then
     a^2 = Phi_P^2 + k^2 R^2 + s_f,     k = a + Phi_P^2 + s_f,     rho_l = m |r_l| k/Phi_l  (l in Omega).
Moreover R < 1, a > k R, and for fixed (Phi_P^2, s_f) the pair (a, k) is a smooth function of R^2 with dk/dR^2 = k^2/(2(a - k R^2)) > 0 (s_f = 0).
Proof.  (E2) of U1 Lemma 1.2: A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2, and sum_Omega nu_l^2 Phi_l^2 = sum_Omega (m u_l)^2 = kappa^2 R^2; divide by theta^2.
The second form of kappa divided by theta gives k.  rho_l = nu_l/theta = m |u_l|/(Phi_l theta) = m |r_l| k/Phi_l.  If R >= 1, then
a^2 >= k^2 R^2 >= k^2 > a^2 (k > a), impossible; so R < 1 and a^2 > k^2 R^2.  Differentiate a^2 = Phi_P^2 + k^2 R^2 with a = k - Phi_P^2 (s_f = 0):
2 a dk = 2 k R^2 dk + k^2 dR^2.  QED
Consequences (PROVED).
(i) The exact shifted coarse system Gamma^#(kappa, a) (U1 2.1, with (X4) as in Section 4) depends on the block data ONLY through r: the
    values and kappa enter only the rows (X3)_m: Delta'_m kappa_m = sum u_l gamma_l, i.e. Delta'_m = sum r_l gamma_l.
(ii) A push of any peak changes (theta, A, kappa) in the same direction (C/Phi_P^2, M, 1 - X) (U1 Lemma 1.4(a)); with the Omega values fixed it
    rescales all ratios of the block by the common factor kappa_old/kappa_new.  If afterwards the ratios are restored (values of Omega multiplied
    by kappa_new/kappa_old), then by the lemma every rho_l (l in Omega) returns to its old value up to the change of s_f and Phi_P^2 (fine terms,
    O(sum_{fine} Phi^2) = O(c_{L+1}^2)) and up to the inactive carriers' share of R^2 (see (iii)).
(iii) An inward push of an Omega carrier d_0 whose ratio is NOT a variable of the minors changes R^2 by 2 m^2 r_{d_0} dr_{d_0} and kappa only by
    rho M X/C ds = O(c_{L+1}^2 D(l)^2) ds (Lemma 1.4(c)); it lowers k and hence every rho_l at fixed (r_l)_{l != d_0}.
Numerics (status_rigidity2.out): (ii) restoring kappa by a second peak push gives theta - theta_0 = 0 (40 digits); restoring the active ratios
gives rho changes ~1e-22; (iii) with a robust inactive carrier the active rho drop by 1.2e-4 ... 2.1e-4 at fixed kappa and fixed active ratios.

## 3. The gap in U1 Theorem 2.3 and the fix under (KN).
3.1 The gap (PROVED that the argument fails; no claim that the conclusion fails).  V1's (C3) raises |u_{c_m}(zhat)| by [Lam, 3 Lam]/lambda_{c_m}
(V1 Lemma DR(i)), i.e. zeta(c_m) by [Lam, 3 Lam], so kappa_m moves by (1 - X)[Lam, 3 Lam] >= (3/4) Lam (Lemma 1.4(a)); U1's claim "(C1)-(C3) move
kappa by <= Design b" is false (Lam = T_lo^3 >> Design b).  If kappa' is a Lojasiewicz value near kappa(f_1) (before (C3)), the kappa-push
restores theta (2(ii)), so V1 Lemma ST(c) (gap >= c_f Lam M/3 at (K4) carriers), used in U1 Lemma 4.5 and Lemma 4.3, fails.  If kappa' is
near kappa after (C3), the tiny minors at the raised point are only <= b + Lip(l) Lam and Lemma L gives a distance C_L (Lip Lam)^{2/N_L} which is
not <= T_lo^4 (it exceeds Lam when N_L > 2), and moves of that size destroy the statuses.
3.2 Hypothesis.  For a clean sub-window w and an activity class a call an Omega carrier NEAR-THRESHOLD if |rho - 1| <= b(w) at f, ACTIVE if its
switching component is active in a.  (KN_{w,a}): every active block containing an active near-threshold Omega carrier contains an Omega carrier
d_0 that is inactive in a (gamma_{d_0} = 0 in the class) with rho_{d_0} >= u(w) at f.
3.3 Proposition KN (exactification with threshold protection).  PROVED.  Let w be a clean sub-window of a main stage L >= l_f of D^{U1'} with
the enlarged rate scheme (minors of Gamma^#(kappa, a) in the ratio variables, Section 4.3, for all patterns and classes of level L), and let a be
a class satisfying (KN_{w,a}).  Then there is a companion f^(1a) with: (a) the ratios r_l (l active in Omega) equal a point r' at which every
tiny minor of Gamma^#(kappa, a) vanishes and every robust one is >= u/2; (b) every active near-threshold Omega carrier is a strict non-peak with
gap >= c_f eta D(L) M, every other coarse carrier keeps its robust status, inactive near-threshold Omega carriers are strict non-peaks with gap
>= c_f eta M; (c) p*(f^(1a) - f) <= C_f Design T_lo^4 log(1/T_lo) = o(T_lo^2).
Proof.  Step 0: V1's (C1), (C2) only (no donor raise in active blocks); values and kappa move by <= C_* b (V1 Lemma ST(a); kappa by Lemma 1.4,
Lipschitz).  Step 1 (Lojasiewicz in ratio space): the tiny minors are <= beta at r(f_1); Lemma L (V2) gives r' with |r' - r(f_1)| <= C_L
beta^{2/N_L} <= eta = T_lo^4/(L Design).  Step 2 (realization): Lemma TU on the active Omega carriers with targets u_l := r'_l kappa (kappa held at
its current value), then, in every active block, an inward push of d_0 (Lemma TU pulls or z-moves on its far part, two-sided) of size
s_0 := C D(L) eta theta Phi_P^2/(rho_{d_0} M) in zeta units, then a peak push restoring kappa exactly (IVT, Section 1; size O(c_{L+1}^2 D^2 s_0)),
then a re-solve of TU (block-triangular Jacobian: d(u/kappa)/d(TU) = I/kappa, dkappa/d(TU) = O(X), d(u/kappa)/d(pushes) = second order) by V1's
explicit fixed point.  (a) holds by construction.  (b): by Lemma R-kt(iii) theta rises by >= c rho_{d_0} M s_0/Phi_P^2 >= C' D eta theta while the
active values moved by <= eta (in u-units, i.e. <= m eta D in nu-units): an active carrier with rho(f) <= 1 + b ends with
rho^# <= (1 + b + C D eta)(1 - C' D eta) < 1 - c D eta once C' is large (b <= eta); robust carriers move by O(D eta) << u; the capacity of d_0
(|zeta(d_0)| = rho theta Phi_{d_0}^2 >= u theta/D^2) exceeds s_0.  Inactive near-threshold carriers are pushed inward individually by eta
(their values are not variables of Gamma^#(kappa, a); kappa changes by O(X) and is restored as above).  (c): Lemma TU(d), V1 Lemma CO.  QED
3.4 What remains (OPEN, precise).  Without (KN_{w,a}): an active block whose inactive Omega carriers are all nearly neutral (rho <= b), with an active
near-threshold switching carrier d.  By Lemma R-kt the statuses are functions of the ratios; the needed point of the exact zero set Z (ratio space)
with rho_d < 1 may not exist near r(f).  If d ends as a peak, the decomposition's excess e_d = |omega_+(d)| + |omega_-(d)| must be O(K t/lambda_d),
which nothing proved implies.  (SKETCH refinement: near-threshold carriers whose inward EXCESS e_d := vs Domega(d) is inactive can be taken out of
Omega with the continuous coefficient -Delta' lambda_d min(rho_d, 1) vs_d, which needs no status; so only active-EXCESS near-threshold carriers
need a lever.  HEURISTIC: for a finite Z the bad case requires a design coincidence rho_d(point of Z) = 1 + O(c_{L+1}^2).)
Possible route (HEURISTIC, not proved).  At a clean w with small b, Lojasiewicz applied to {tiny minors} ∪ {rho_d - 1 : d near-threshold}
(semialgebraic, design data up to O(c_{L+1}^2)) puts r(f) within a design power of b of W_N := Z ∩ {rho_d = 1, d in N}, or excludes the
configuration altogether (alternative (i) of Lemma L).  If the design is GENERIC in the sense that the map (rho_d)_{d in N} restricted to every
stratum of every Z_S is transversal to (1, ..., 1) (critical values avoid 1), then Z enters the open orthant {rho_d < 1, d in N} near W_N with
design-controlled depth, and the status coherence holds with margin >> c_{L+1}^2.  Missing: (a) a construction of the design making all these
transversality conditions hold (new objects at level l involve earlier parameters; only the stage-l parameters, e.g. delta_l and c_l, are
free), (b) quantitative transversality near singular strata, (c) the case dim Z_S < |N| (then W_N is generically empty and the configuration
is excluded, which must be made quantitative).

## 4. The coarse cone Gamma^#(kappa, a): corrected rows and precisions.  PROVED.
4.1 (X4).  For every coarse strict non-peak k = k(l) of f^# in Omega with gap^#(k) < t^2 for t in W(w) (near-threshold), impose
    vs_l gamma_l/lambda_l + Delta'_m >= 0     (vs_l := sgn w^#(k), design coefficients).
Points of the cone then satisfy vs Domega(k) = (vs gamma/lambda + Delta') - Delta'(1 - rho^#) >= -|Delta'| gap^#/M >= -3 gap^#/t (|Delta'| <= C_f,
t <= T_hi small), which with the shift trick of V1 TR Step 5 is kind [3].  The decomposition satisfies the row up to lambda(4 gap(f)/t + C_f b):
at strict non-peaks of f by lem:suplevel(f), at peaks of f by eq:peakshift (vs(omega_- - omega_+) = e_k >= 0).  U1's "vs gamma >= 0" is wrong:
in configuration (ii) the decomposition violates it by up to lambda Delta'; in configuration (i) it does not imply kind [3].
Exclusions (PROVED).  A class-R or a (P-ii) near-threshold strict non-peak of f in block m forces Delta'_dec,m >= -C_f D(L) K_g t (lem:suplevel(f):
-vs Delta theta/lambda - Delta d M rho >= -4 gap/t with |Delta theta| <= K_g t (class R) resp. tau >= -K_g t (class G, anti type)); so neither
occurs in an active negative block.  A class-R or anti-type peak forces the same (eq:peakshift; V1's sources (U1), (U2)).
4.2 Aggregation.  On a near signature set S_l ∩ [1, s_far] only l lives among coarse carriers, so the (X1) rows there are positive multiples
v_l(s) of one sign row (or equality row at free coordinates); replace them by the single row with coefficient ||v_l 1_{near}||_1 (a design
number): l_1 violations are unchanged, and Lemma H no longer sees the coefficients 2^{-s} down to 2^{-s_far}.
4.3 Ratio variables and cofactor minors.  Divide (X3)_m by kappa_m: Delta'_m - sum_{Omega_m} r_l gamma_l = 0.  The minors of the resulting matrix
are polynomials in r with design coefficients; add also the minors of the matrices g_J formed by the Delta'-parts of the cofactor vectors of
(n-1)-row subsystems (the unnormalized extreme rays), which are polynomials as well.  At a point where all these are 0 or >= u/(2 Design^C):
Hoffman constant <= C Design^C/u (V2 Lemma H) and A_max <= C_f (Design/u)^C (Cauchy-Binet: sigma_min(g_J) >= max_K |det g_{J,K}|/||g_J||^{|J|-1}).
4.4 Signs of increments.  By Lemma D every block has a robust coarse peak; in an active block it is a class-G peak (class-R peaks are sources of
both kinds) of swallowing type (negative block) or anti type (positive block), and (X2) on its near signature set gives sgn Delta'_m on the whole
cone.  Hence incr(t) in Gamma^#(kappa, a) has |Delta'^*_m| >= |Delta'_m(t)| with the same sign, and eps-signs of active gamma are kept: the class
of every scale is preserved by the normalization.
4.5 Classes.  Read the class off the decomposition data (Delta'_dec, gamma_dec) with thresholds A_{i+1} = K_* A_i, K_* >= 2 D(L) x (Hoffman
constant); fix (class, then cube after the companion's step (1c)) by pigeonhole; the count is (Design/u)^{C}.

## 5. Gap G1 (far parts of non-owner coarse signature sets) and the release.  PROVED.
At f^#, V1's (C1) closes S^nat_{l''} (near AND far) for class-G coarse carriers; U1's J_fine excludes these coordinates and E_c contains only
S_{l''} ∩ [1, s_far(w)].  For j in S_{l''} ∩ (s_far, infinity), V(j) = gamma_{l''} v_{l''}(j) (or the peak trace) + contributions of later carriers.
If l'' is not an owner-candidate (gamma_{l''} = 0 in the class, or l'' a peak of an inactive block), only later contributions remain; in
configuration (i) a later type-(d) carrier k contributes with sign varsigma_k sgn y_k(j), varsigma_k = sgn Y_k determined by other coordinates,
so z_j V(j) >= 0 with z_j = eps_{l''} fails in general.  Release: in step (2) put S_{l''} ∩ (s_far(w), infinity) into J_fine for every such l''.
Then: configuration (i): each released j is owned by the first later owner-candidate meeting it (through its target), which dominates by Lemma
4.2(ii) (Section 7), and z_j := its sign; configuration (ii) and mixed classes: j in J_free of the Schauder map.  Cost: |Delta u_{l''}(zhat)| <=
2 delta_{l''} sum_{s > s_far} 2^{-s}/n <= 4 c_{L+1}^2 (2^{-s_far} <= c_{L+1}^2); these values are not variables of Gamma^#(kappa, a); kappa moves by
<= C Design c_{L+1}^2, giving a trace correction <= C_f Design c_{L+1}^2 on T(L), far below the cluster capacity A_2 c_{L+1}/(Design t).

## 6. The design D^{U1'}.  PROVED.
6.1 Inconsistency of D^{U1} with (W6).  (W6) gives c_p <= g_p 2^{m+k-p} <= 2^N/(1440 * 3^{|supp y_p|}); for an absorber target |supp y_p| = R + 2 with
R the least integer with 2^{3-R} <= mu_{p_0}^2 c_p^2/4.  Inserting: 8 (9/2)^R <= mu_{p_0}^2 4^N/(4 * 1440^2), impossible since mu_{p_0} = 2^{-p_0^2-1}
and p_0 exceeds every earlier target coordinate.  At cluster stages U1's c_{L+1} even includes (W6) for a target whose R depends on c_{L+1}.
6.2 Definition.  Rounds r = 1, 2, ...: block m_r from a fixed sequence containing every block infinitely often; y := T_final's candidate for
m_r (allowedness (a) and (c) with margin: supp y ∩ S_{l'} ⊂ [1, p - 2|supp y| - 1], p the stage where y will be placed).  PRE: for every s in
supp y ∩ (union S_{l'}) a biased absorber pair (block 1, consecutive stages); MAIN: y at stage p (block m_r); CLUSTER: a biased pair for every
s in E^ch(p) = T(p) ∪ union_{l''<=p} (S_{l''} ∩ [1, p]).  Absorber targets as U1 (A0) with R chosen from c_p^low := min{c_{p-1}/4,
b(p-1, M(p-1))^2, (delta^max_p H_p/2)^2, (W4'') at s, (W5), (W7)}, which does not depend on R.  Weights: T_final's (W1)-(W5), (W7) with (W4'')
at PRE and MAIN stages (no (W6) at absorber stages); at cluster stages c_{p+i} := c_{p+1}^low 4^{1-i}, where in (W4'') the factor T_lo(.)^3 is
read with the main stage p (satisfied, since c_{p+1}^low <= b(p, M(p))^2; this is all Lemma 4.2(i) uses: a factor T_lo(w)^3 for windows w at
main stages L <= p).  Step (6) (sub-window data) at EVERY stage; windows are used only at main stages.  Design(main stage) as U1 plus the rate
objects of Section 4.3.
6.3 Admissibility and N-freeness.  (T-a), (T-b), (T-c): (W4) at every stage (cluster weights <= c_{p+1}^low which includes (W4) for every s of
E^ch(p)), so T_final's argument applies; (T-d): no target is ever blocked, every y^(i) is placed infinitely often in every block (rounds).
(W3) at cluster stages: c_{p+i} <= b(p, M(p))^2 <= 2^{-8 n(p, M(p))}, (delta_{p+i} H_{p+i})^2 >= 2^{-2(p+i) - 6 * 2^{p+i} - 4}, and p + i <=
3p + 2 s_max(p) while n(p, M(p)) >= p 2^{p^3} Design(p) >= 2^{6 s_max(p)}.  (P2) at main stages as U1.  N-free: absorbers live in block 1.
Lost features: (W5), (W7) (V4's (SF*), (SF_tau)) and (W6) at absorber/cluster stages — none is used on U1's dependency tree.
6.4 Lemma 3.2 under D^{U1'}.  For a main stage L and s in E_c(w) \ F^#: if s in E^ch(L), the cluster of L comes first; otherwise s in
S_{l''}, l'' <= L, s > L; after L the carriers meeting s are absorber pairs for s (pre-pairs, cluster pairs), main targets containing s (each
preceded by its pre-pair for s), and nothing else (absorber/FD targets use fresh coordinates; signature sets are disjoint).  Hence the first
two carriers after L meeting s form a consecutive biased pair, or no carrier after L meets s (then the residue is 0).

## 7. Lemma 4.2(ii) (target coordinates) for owners inside absorber blocks.  PROVED.
Let k be an owner at a cluster or pre-pair stage and j one of its target coordinates (its s or a fresh coordinate).  Inside the block, only its
partner meets j; lambda decreases by >= 8 between consecutive block-1 stages, so the partner's term is <= 1/4 of k's (|y(j)| equal up to 1 + o(1)).
The first later non-absorber stage p' has c_{p'} <= b(p' - 1, M(p' - 1))^2 <= 2^{-8 n(p'-1)} and n(p'-1) >= Design(p'-1) >= (B_mu D)^6 >=
(1/(eta_k lambda_k))^6 (B_mu >= 2^{2 p_0^2} >= 1/mu_{p_0}^2, eta_k >= mu_{p_0}^2 c_k^2/64, D >= 1/Phi_k); all later carriers sum to <= 2 c_{p'}.  So the ratio
of later to own terms is <= 1/4 + C_f 2^{-n(p'-1)}/(T_lo(w) eta_k lambda_k) < 1/2.  For main-stage owners U1's argument (c_{k+1} <= b(k, M(k))^2)
stands.

## 8. Master Theorem IV' (corrected).  PROVED (modulo the refereed tools listed by U1 and the fixes above).
Design D^{U1'}, N fixed, diagonal mu-base, f in S_{p_N^*} with finite base support.  Suppose that for infinitely many main stages L some clean
sub-window w of L has at least n(w)/D_cls(w) dyadic scales whose activity class a has no active shift, or is one-signed and satisfies
(KN_{w,a}).  Then f is in Rec(p_N).
Proof (assembly).  Pigeonhole: a class a and, after step (1c), a cube with |S| >= n(w)/D_cls(w)^2 scales (Q(w) >= D_cls^2 (Design/u)^C).
Companion: (1a) Proposition KN (classes with no active shift: V2 Theorem B, values only); (1b) zero-value absorbers (Lemma 3.3) for the first
pairs of E_c(w) and the cluster of L; (1c) restore kappa and the exact ratios (joint fixed point, Section 1 continuity); (2) fine structure with
the G1 release: configuration (i) U1 Lemma 4.1 recursion (dominance by Lemma 4.2 with Section 7), configuration (ii) U1 Lemma 4.4 (Schauder on
the common ray).  Data at each t in S: Proposition 2.2 with the rows of Section 4 (projection error K t, minus-side increments <= p epsilon),
absorption on E_c (Proposition 3.4), admissibility on J_fine (Lemmas 4.2, 4.4), true shift (Lemma 4.6).  Statuses: Proposition KN(b) plus
inward pushes; kinds [2] (robust gaps, absorbers gap M) and [3] (near-threshold, Section 4.1).  (SC) for the negative blocks in configuration
(i): U1 Lemma 4.3 (coarse statuses from Proposition KN).  Recovery: Theorem E^SC / E^>= (V2) with banked, pulled and absorber supports (V1
Theorem E'', no flips: t|b| <= theta_a), on the subset S (U1 Lemma 2.4).  QED
Corollaries.  (N = 1) f in Rec(p_1) whenever (KN) holds at the one-signed classes of a clean sub-window for infinitely many main stages; this
does NOT cover every finite-F row (an active negative block's (K4) carriers are forced to be active).  (Intrinsic) if moreover I_up(w) = {}
or I_lo(w) = {} at these sub-windows, every class is one-signed (U1 Cor. IV.4's reduction, correct).
