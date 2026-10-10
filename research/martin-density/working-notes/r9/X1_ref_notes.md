# X1-ref notes (Round 9): proofs of the fixes and the corrected statements

Setting and notation of X1 / U1 / U1-ref: finite block set I = {1..N}, first rows f with finite base support F, design T^tr (X1 3.1 =
T_final + D^{U1'} with generic weights), clean sub-window w of a main stage L >= l_f, activity class a, pattern kappa.  Block m of a row:
zeta = R_m^** zhat, A = |zeta|_m, M + C = 1, theta = AM/C, nu_k = |zeta(k)|/Phi_k^2 = m|u_k(zhat)|/Phi_k, rho_k = nu_k/theta, P = {rho >= 1},
Q = complement, lambda_k = m Phi_k.  For a finite set Omega of carriers of the block
      kappa(Omega) := [A(A + theta) - sum_{k in Omega} nu_k^2 Phi_k^2]/theta                    (formula 1, U1 Lemma 1.3),
r_l := u_l(zhat)/kappa(Omega), R^2 := m^2 sum_Omega r_l^2, a := A/theta, k := kappa/theta, K(s, x) := [s + sqrt(s^2 x + s(1 - x))]/(1 - x).
Labels: PROVED / SKETCH / HEURISTIC / OPEN.  "PROVED" = complete proof here using refereed results of Rounds 5-8 and standard real
semialgebraic geometry [BCR = Bochnak-Coste-Roy].  Scripts: r9/X1_ref_work/.

## 0. Summary of verdicts
Correct: Lemma K, Lemma F, Lemma EC, Lemma NLM (after W-fix), Lemma GEN, Lemma QC, Theorem S1 (given KN^tr).
Correct with fixable gaps (fixed here): 2.1 (D1-D3), (X4^0) and weight-freeness (K1, W-fix), Proposition KN^tr (KN-1, D2, S-0, Q2, Q3),
Lemma W' (W1, W3), Master Theorem IV^tr and Corollary IV^tr.1 (inherit; W2 places Corollary IV^tr.1 inside the note's admissible class).
SKETCH, label appropriate: Corollary IV^tr.2 (X2 unrefereed).  OPEN: option-(b) exception for N >= m(1); mixed classes N >= 2 (X2);
infinite F; Martin's p.  No counterexample.

## 1. Lemma K and the convention K1.  PROVED.
Lemma K (X1).  If Omega ⊂ Q then k = K(sigma, R^2) with sigma = Phi_P^2 + s_f, s_f = theta^{-2} sum_{Q \ Omega} nu^2 Phi^2; K is strictly
increasing in both arguments; a^2 = sum_{all k} Phi_k^2 min(rho_k, 1)^2; rho_l = m|r_l| k/Phi_l for every carrier l.
Proof.  U1 Lemma 1.2 (E2): A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2; divided by theta^2 this is the uniform form, and with
sum_Omega nu^2 Phi^2 = m^2 sum_Omega u_l(zhat)^2 = kappa^2 R^2 it reads a^2 = sigma + k^2 R^2.  Inserting (E2) into formula 1 gives
kappa = A + theta Phi_P^2 + S_f/theta, i.e. k = a + sigma.  R < 1 (U1-ref Lemma R-kt).  Eliminating a: (1 - R^2) k^2 - 2 sigma k + sigma^2 -
sigma = 0, roots [sigma +- sqrt(sigma^2 R^2 + sigma(1 - R^2))]/(1 - R^2); the smaller root is <= sigma (equivalent to 0 <= sigma(1 - R^2)(1 +
sigma R^2)) and would give a <= 0.  Monotonicity in sigma: obvious; in x = R^2: differentiating a^2 = sigma + k^2 x, a = k - sigma gives
dk/dx = k^2/(2(a - kx)) > 0 since a > kR >= kx.  rho_l = nu_l/theta = m|u_l|/(Phi_l theta) = m|r_l| kappa/(Phi_l theta).  QED
K1 (Omega meeting P).  If Omega ∩ P is non-empty (active weak peaks of f belong to the pattern's Omega), the same computation with formula 1
gives a^2 = sigma' + k^2 R^2, k = a + sigma', sigma' := Phi_{P \ Omega}^2 + sum_{l in Omega ∩ P} (1 - rho_l^2) Phi_l^2 + s_f.
Proof.  kappa(Omega) = A + [theta^2 Phi_P^2 + sum_Q nu^2 Phi^2 - sum_Omega nu^2 Phi^2]/theta = A + theta(Phi_{P\Omega}^2 + sum_{Omega∩P}
(1 - rho^2)Phi^2) + S_f/theta, and a^2 = Phi_P^2 + sum_Q rho^2 Phi^2 = sigma' + sum_Omega rho^2 Phi^2 = sigma' + k^2 R^2.  QED
For a weak peak (rho in [1, 1 + b]) the correction lies in [-3b Phi_l^2, 0].  Consequently the rate objects (minors in ratio variables) and
the Step-0 push of KN^tr must use formula 1 with the PATTERN's Omega; then the push of an active weak peak from rho = 1 + b' to 1 - b
changes the ratios by O(b).  In the "peak convention" the ratios of the whole block jump by a relative O(Phi_l^2/k) (numerically 0.7%-7%,
weakpeak_ref.out), and the estimate |rho - rho^0| <= C D^2 (b + c^2) of X1 2.1(T) is false.
Numerics: indep_block.out (independent solver, 60 digits; 99 blocks: 3.0e-61), cvx_check2.out (solver vs convex dual: A 1e-11, M, C 1e-8).

## 2. Lemma F.  PROVED.
If P ⊇ P_rob, Omega_a ⊂ Omega ⊂ Q and ratios are computed with kappa(Omega), then for l in Omega_a: rho_l = m|r_l| K(sigma, R^2)/Phi_l >=
m|r_l| K(sigma_rob, R_a^2)/Phi_l =: rho^0_l, because sigma >= sigma_rob = Phi_{P_rob}^2, R^2 >= R_a^2 and K is increasing.  Equality iff P =
P_rob, s_f = 0, r = 0 on Omega \ Omega_a.  QED.  Quantitative complements (floor_ref.out): inactive carriers at relative position <= b raise
the active statuses only by O(D^2 b^2) (they enter through rho^2 Phi^2/k^2 in R^2); fine terms by O(D^2 c_{L+1}^2); with K1, active weak
peaks change the floor by O(b).

## 3. The floor-form row and weight-freeness.  PROVED (with the W-fix).
3.1 Identity.  Off P the duality map is w(l) = C zeta(l)/(Phi_l^2 A) = vs_l M rho_l (theta = AM/C).  With Domega(l) = gamma_l/lambda_l + Delta_m
w(l) (U1 Lemma 1.1(a)) and Delta' = Delta M: lambda_l vs_l Domega(l) = vs_l gamma_l + Delta'_m lambda_l rho_l = vs_l gamma_l + Delta'_m m^2 |r_l| k.
(X4^0) is the same expression with k replaced by K(sigma_rob, R_a^2).  (Checked: indep_block.out (3), 7.5e-62.)
3.2 Data.  At strict non-peaks of f, lem:suplevel(f): vs Domega_dec >= -3 gap(f)/t.  At weak peaks of f, eq:peakshift: vs(omega_- - omega_+) =
e >= 0, i.e. vs gamma_dec + Delta'_dec lambda >= 0.  The (X4^0)-coefficient at the companion is lambda rho^0_l(r'') with |rho^0_l(r'') - rho_l(f)|
<= C D^2 (b + c_{L+1}^2) + Lip eta' (K1, Lemma F's complements, |r'' - r_1| <= eta') and, at weak peaks, |1 - rho^0_l(r'')| <= C b + Lip eta'.
Hence the violation of (X4^0) by (Delta'_dec, gamma_dec) is <= lambda C_f (3 gap(f)/t + C D^2 (b + c^2) + C b + Lip eta') <= K t for t >= T_lo(w)
(gap(f) <= M b, b <= eta' <= T_lo^4).  For Delta'_dec < 0 the bound needs only rho^0 <= rho (Lemma F), for Delta'_dec > 0 it needs the small
inactive mass of a (T)-block.
3.3 Kind [3] at f^#.  If at f^# the inactive Omega values of the (T)-blocks are 0 (KN-1) then rho^#_l - rho^0_l(r'') <= C D^2 c_{L+1}^2 and every
point of the cone has vs Domega(l) >= -|Delta'_m| C D^2 c_{L+1}^2 >= -3 gap^#(l)/t (gap^# >= M mu/2 >> c_{L+1}^2, t <= 1).  The + side: vs omega^+(l)
<= gap(f)/t <= gap^#/(4t) when M b <= gap^#/4 ((D2)).  V1 TR Step 5 (shift trick) then gives Y1 Prop. 5.2(iii) kind [3]; its cost is
lambda|x| <= lambda (|Delta'| |rho^# - rho(f)| + K t/lambda) = O(K t) since |rho^# - rho(f)| <= Lip eta' + C D^2 b.  Increments of the
normalization (U1 Prop. 2.2(c)) lie in the cone and have Delta' of the same sign (U1-ref (p-d)), so the bound persists for the sums.
3.4 Weight-freeness.  Rows of Gamma^#(kappa, a) in (Delta', gamma): (X1) with entries u_l(j) (l in Omega_a; u_l = (y_l + delta_l h_l)/n_l, weight-
free) and Delta'_m tau_m(j) (tau_m = sum_{coarse peaks p} vs_p lambda_p u_p|_{E_c}: peak weights only); aggregated signature rows (U1-ref 4.2;
the coefficient scales the row, which does not change the vanishing of any minor); (X2), (X5); (X3)/kappa: Delta'_m - sum r_l gamma_l = 0;
(X4^0) in (T)-blocks; vs gamma >= 0 in (U)-blocks; U1-ref's (X4) (with 1/lambda_l of (KN)-block carriers) in (KN)-blocks; cofactor polynomials
of the same matrix.  None contains the weight of a carrier of N_T (the active near-threshold carriers of the (T)-blocks); psi_d(r) := m|r_d|
K(sigma_rob(m(d)), R_a(m(d))^2) neither.
W-fix.  Replace X1's region K_kappa by K_kappa := {r : R(m)^2 <= 1 - eps_K(m) for all active blocks m}, eps_K(m) := sigma_rob(m)/4 (peak weights
only; compact since |r_l| <= 1/m).  Data are interior: from a^2 = sigma + k^2 R^2 >= k^2 R^2 and k = a + sigma, 1 - R^2 >= 1 - (1 - sigma/k)^2 >=
sigma/k >= sigma_rob/2 (k <= 2 because a = C/M <= 1 and sigma <= 1).  [Alternatively keep X1's bounds: on the face |r_d| = 2 Phi_d/(m k_min)
(d in N_T) one has F >= 2K/k_min >= 2 when k_min <= min K, so no witness of a coincidence lies on it, and a local minimum with value 1 is a
local minimum on the weight-free set.]

## 4. Three kinds of blocks: precisions D1-D3.  PROVED.
D1.  In a (U)-block (Delta'_m := 0) r^(m) occurs only in the single row (X3)_m: minors are homogeneous of degree 0 or 1 in r^(m).  A cofactor
polynomial (minor of g_J, whose columns are Delta'-parts of cofactor vectors of subsystems J) is a sum of products with one entry per column,
each column homogeneous of degree e_J in {0, 1}: it is homogeneous of degree <= n.  Under r^(m) -> s r^(m) vanishing is preserved and robust
values change by a factor >= s^n >= 1 - n(1 - s) >= 1/2 when 1 - s = C Lip eta' <= 1/(2n).  By Lemma K every active status of the block is
multiplied by at most s (|r_l| scales by s, K decreases).
D2.  Inactive near-threshold carriers can occur in (U)-blocks (in (T)-blocks they are excluded by definition, in (KN)-blocks they are the
levers).  At f^# they must be strict non-peaks or robust peaks: push each inward by eta' (they are not variables of Gamma^#; d kappa = O(X) per
unit, restored by a peak push), exactly as in the last clause of U1-ref Proposition KN(b).
D3.  The (T)-block estimate |rho_l(f) - rho^0_l(r(f))| <= C D^2 (b + c_{L+1}^2) holds in the formula-1 convention (K1 and Section 2).

## 5. Lemma NLM.  PROVED (X1's proof with the W-fix).
Fix kappa and all its data except Phi = (Phi_d)_{d in N_T}; Z := zero set of the tiny minors and tiny cofactor polynomials in K_kappa
(compact, semialgebraic, independent of Phi); F_Phi := max_{d in N_T} psi_d/Phi_d on Z; B := {Phi : some r_0 in Z with F_Phi(r_0) = 1 is a local
minimum (possibly non-strict) of F_Phi on Z}.  Then dim B < |N_T|.
Proof.  B is first-order definable, hence semialgebraic.  Stratify Z into finitely many connected Nash manifolds S compatible with the sign
conditions on r_d (d in N_T) [BCR 9.1.8]; psi_d is Nash on strata contained in {r_d != 0} (K is Nash on {R^2 < 1}).  Let Phi in B with witness
r_0 in S and D := {d : psi_d(r_0) = Phi_d} (non-empty; r_d != 0 for d in D).  A local minimum on Z is a local minimum on S.  If d Psi_{D,S}(r_0)
were onto R^D, choose v in T_{r_0} S with d psi_d(r_0) v = -1 (d in D) and a Nash arc gamma in S with gamma'(0) = v: psi_d(gamma(s)) < Phi_d for d
in D and small s > 0, and psi_d(gamma(s)) < Phi_d for d notin D by continuity; so F_Phi(gamma(s)) < 1, a contradiction.  Hence Phi_D is a
critical value of Psi_{D,S}; by the semialgebraic Sard theorem [BCR 9.6.2] the critical values form a set of dimension < |D| (this includes
dim S < |D|).  B ⊂ union_{D,S} {Phi : Phi_D in CV_{D,S}}, of dimension < |N_T|.  QED

## 6. Lemma GEN.  PROVED.
Let k_0 be the field generated by the non-weight data of the design and k := k_0(weights of the carriers of kappa outside N_T).  If the
family (c_l) is algebraically independent over k_0 then (Phi_d)_{d in N_T} notin B_kappa.
Proof.  B_kappa is defined over k (W-fix: eps_K in k).  By Tarski transfer B_kappa = (B_0)_R for a k^rc-semialgebraic B_0 with dim B_0 = dim
B_kappa < n := |N_T|; the Zariski closure of B_0 has dimension < n, so B_0 ⊂ V(P) for a nonzero P in k^rc[X_1..X_n], and B_kappa ⊂ V(P) (transfer).
The coefficients of P lie in a finite extension k' of k; the product of the conjugates sigma(P) over the k-embeddings of k' is a nonzero polynomial
with coefficients in k vanishing wherever P does.  The coordinates Phi_d = 2^{-m(d)-k(d)} c_d are algebraically independent over k (they are
part of a family algebraically independent over k_0, disjoint from the weights generating k).  Hence (Phi_d) notin V(P).  QED
Design side.  Choosing c_l in an interval and transcendental over the countable field k_0(c_1, ..., c_{l-1}) makes the family algebraically
independent over k_0.  For this, k_0 must not depend on the weights: in T_final / D^{U1'} the targets come from the fixed countable pool by
support rules (allowedness (a), (c), schedule), delta_l is determined by (GM) from y_l and l only (U4 1.3(2)), n_l, u_l, h_l, S_l, H_l, mu_s
are algebraic over these, FD and absorber targets use fresh coordinates with binary values, and the integer R of an absorber target depends on
weights but takes values in Z.  Window thresholds (b, u, T_lo, Design) may depend on weights: they are not coefficients of any cone.

## 7. Lemma QC.  PROVED, with Q1-Q3.
(a) mu_kappa(h) := 1 - max_{Y_1} G_h > 0, Y_1 := Z ∩ {F <= 1}, G_h(r) := inf{F(r'') : r'' in Z, |r'' - r| < h}: G_h is upper semicontinuous
(if r'' is admissible for r it is admissible for r_n near r), Y_1 compact, G_h < 1 on Y_1 by non-coincidence (and trivially where F < 1).
(b) If Y_1 = {} then F >= 1 + m_0 on Z; otherwise dist(., Y_1)^{1/alpha_Y} <= C_Y (F - 1)_+ on Z [BCR 2.6.7].  (c) mu_kappa is definable,
positive, nondecreasing; Puiseux at 0+ gives mu >= c_kappa h^{beta_kappa} on (0, h_kappa].
Q1.  If some r* in Y_1 has F(r*) = 1 then G_h(r*) >= 1 - Lip(F) h, so mu_kappa(h) <= Lip(F) h.
Q2.  KN^tr uses h = eta'(w)/3; require Design(L) >= 1/h_kappa for all kappa of level L (or use mu(h) >= mu(h_kappa) for h >= h_kappa).
Q3.  The Lojasiewicz step uses V2 Lemma L for continuous semialgebraic functions on the compact semialgebraic K_kappa; V2's proof [BCR 2.6.7]
applies verbatim with Q := K_kappa and the zero set taken inside K_kappa.

## 8. Proposition KN^tr (corrected statement and proof).  PROVED modulo U1-ref Proposition KN and the refereed tools.
Design T^tr with: the rate scheme enlarged by the minors and cofactor polynomials of Gamma^#(kappa, a) written with (X4^0) / (X4) / U-rows for all
patterns and classes of level L; Design(L) dominating Lip, C_L, N_L, C_Y, 1/m_0, 1/c_kappa, beta_kappa, 1/h_kappa of the level-L patterns;
eta'(w) := T_lo(w)^4/(L Design(L)); b(w) := min(U4's b(w), the largest b with (D1) C_L((1 + Lip C_*) b)^{2/N_L} <= eta'/3 and (D2) delta_0(b) <=
min_kappa min(m_0/2, (eta'/(3 C_Y))^{1/alpha_Y}), M b <= min_kappa mu_kappa(eta'/3)/8).  [(D3) is not needed: see S-0.]
Statement.  At every clean sub-window w of a main stage L >= l_f and every class a there is a companion f^(1a), p*(f^(1a) - f) <= C_f Design(L)
eta' log(1/eta') = o(T_lo(w)^2), with: (a) the active ratios r'' lie on Z_kappa, robust minors and cofactor polynomials >= u/2; (b) (T)-blocks:
every active near-threshold carrier has rho <= 1 - mu_kappa(eta'/3)/2 and every inactive Omega carrier has value exactly 0; (KN)-blocks: U1-ref
Prop. KN(b) with eta' in place of eta; (U)-blocks: active statuses <= 1 - eta', inactive near-threshold carriers pushed inward by eta' (D2);
every other coarse carrier keeps its robust status.
Proof.  Step 0: V1's (C1), (C2); active weak peaks of (T)-blocks pushed to rho = 1 - b (formula-1 convention, K1).  Tiny minors <= (1 + Lip C_*) b
at r_1; F(r_1) <= max_{d in N_T} rho_d(f_1) <= 1 + C_* b by Lemma F.  Step 1: r' in Z_kappa, |r' - r_1| <= eta'/3 (Q3, (D1)); F(r') <= 1 +
delta_0.  Step 2: Y_1 non-empty and r_1' in Y_1 with |r_1' - r'| <= eta'/3 (QC(b), (D2)).  Step 3: r'' in Z, |r'' - r_1'| < eta'/3, F(r'') <= 1 -
mu_kappa(eta'/3) (QC(a), non-coincidence by GEN).  |r'' - r_1| <= eta': robust minors stay >= u/2, robust statuses move by <= Lip eta' << u,
signs of the r_d are kept (|r_d| ~ Phi_d/(mK) >> eta').  Step 4 (realization, one joint fixed point over all blocks): V1 Lemma TU sets the
active values to r''_l kappa ((U)-blocks: s_m r''_l kappa, D1) and HOLDS the inactive Omega values of the (T)-blocks at exactly 0 (KN-1 below);
(KN)-blocks receive U1-ref's lever push; one peak push per block restores kappa (continuity of kappa, U1-ref 1); D2 pushes; the Jacobian is block
triangular with identity blocks for the tuned values (d(u/kappa)/d(TU) = I/kappa, dkappa/d(TU) = O(X), cross effects second order), so V1's explicit
fixed point converges.  Statuses in (T)-blocks: sigma = sigma_rob + O(c_{L+1}^2) (coarse peaks at f^# are exactly P_rob: no coarse carrier lies in
(b, u) ∪ (1 + b, 1 + u), active near-threshold peaks were pushed, inactive near-threshold carriers do not exist in (T)-blocks), R^2 = R_a(r'')^2
exactly, so rho^#_d <= F(r'') + C D^2 c_{L+1}^2 <= 1 - mu/2 (c_{L+1}^2 <= b^4 << mu).  Costs: V1 Lemmas CO, TU(d).  QED
KN-1 (why the exact hold is necessary).  mu(eta'/3) >= c(eta'/3)^beta with a non-explicit beta.  The other blocks' moves act on a (T)-block at
second order (V1 Lemma B: remainder <= C Design^2 size^2), i.e. by ~ Design^2 eta'^2 on values.  An inactive Omega carrier left at such a value
contributes ~ D^2 Design^4 eta'^4 to the active statuses (through R^2), which is not << c (eta'/3)^beta when beta > 4.  Active ratios are exact
by the fixed point and sigma depends only on the peak set, so the inactive values are the only such term; holding them at 0 is available (V1
Lemma TU for exactly swallowed carriers, far z-moves for carriers with room; V2 Theorem B does this for tiny objects; U1 holds its absorbers at
value 0 in (1b)-(1c)).  In (KN)-blocks (margin c_f D eta' M) and (U)-blocks (margin eta') second-order effects are harmless.
S-0 (later drifts).  U1-ref's steps (1b), (1c), (2), the G1 release and the true-versus-reference shift (U1 Lemma 4.6) move statuses and shifts
by <= C Design(L) c_{L+1} (active values: <= C c_{L+1}^2; kappa: <= C c_{L+R_cl+1}, Lipschitz constant Design/u).  Since c_{L+1} <= b(L, M(L))^2
<= b(w)^2 ((W2); b decreases along the sub-windows of a level) and b(w) <= mu/(8M) ((D2)), these drifts are <= C Design mu^2 << mu (Q1: mu <=
Lip eta' << 1/Design).  Hence the margin mu/2 survives the whole companion, and in U1 Lemma 4.6 the kind-[3] bound with the TRUE shift holds:
lambda(|Delta'' - Delta'| + |Delta'| |rho^# - rho^0|) <= C lambda (Design c_{L+1} + c_{L+1}^2/t + D^2 c_{L+1}^2) << 3 lambda gap^#/t.
Quantifier order: design -> f -> L, clean w (rate objects of f, all patterns and classes) -> g, rho -> class, pattern -> companion -> data.

## 9. Design T^tr, Lemma W': precisions W1-W4.  PROVED.
W1.  Under option (a) (c_1 < 1) T^tr violates the equality clause of def:admissible (T-a); Martin's Lemma B gives norm one.  Martin's proof uses
only ||T|| <= 1 (v*_{n,m} in B_Y; ||Phi_m||_1 <= 2^{-m} < 1 in Lemma A; |R_m x|_m <= m 2^{-m} |||x|||; norm density of the normalized vectors in
Proposition 3), so the norm is a Martin-type norm, but option-(a) statements are outside the note's class.  T^tr(a)/c_1 is admissible with
c_1 = 1, i.e. option (b).
W2 (Corollary IV^tr.1 inside the note's class).  Under option (b) only carrier 1 has a rational weight.  Choose the block of carrier 1 to be
m(1) = 2: in T_final's ladder (U4 1.2(i): any bijection j with j(k, m) < j(k', m) for k < k') take j(1, 2) = 1; in D^{U1'} start the fixed block
sequence of the rounds with block 2 (round 1 has no PRE stage: at stage 1 no target meeting a signature set is allowed, so y = y^(1) or another
Z_0-supported target).  Nothing on the dependency trees uses m(1) = 1 (block-1 absorbers are later carriers; (GM) is imposed only for l >= 2,
and with m(1) = 2 it would force c_1 <= 2^3/240 < 1, so U4's fix C7 is still needed and suffices).  For p_N with N < m(1) the rate objects of
block-m(1) carriers are constant (V1-ref p0) and no pattern contains carrier 1, so Lemma GEN applies to every pattern.  Hence for N = 1
Corollary IV^tr.1 holds for an operator satisfying (T-a) WITH equality.  For N >= m(1) the carrier-1 exception remains OPEN.  [Slice remark:
if 2^{-m(1)-1} is a regular value of psi_1 on every stratum S, then S ∩ {psi_1 = 2^{-m(1)-1}} is a Nash submanifold and r_0 critical for
Psi_{D,S} with 1 in D iff r_0 critical for Psi_{D\{1}} on it (rank count with d psi_1 != 0), so the slice of B has dimension < |N_T| - 1 and the
other generic weights avoid it; whether 2^{-m(1)-1} can be a critical value of psi_1 identically in the transcendental parameters is OPEN.]
W3.  D^{U1'} chooses the integer R of an absorber target from c_p^low by 2^{3-R} <= mu_{p_0}^2 c_p^2/4 (a lower-bound use of c_p).  With c_p in
[(1 - 2^{-p}) c_p^max, c_p^max] compute R from (1 - 2^{-p}) c_p^low (R increases by at most 1; still fixed before c_p).  Cluster weights:
c^max_{p+i} := min(c^low_{p+1} 4^{1-i}, c_{p+i-1}/4), so that (W1) holds with the perturbed predecessor; U1-ref 7's block-1 ratio (partner term <=
1/4 + o(1) of the owner's) follows from (W1) and the factor 2 of 2^{-k}.
W4.  Lower bounds on weights are used only at: s_1 = T_lo^8 c_l and (VT) c_l >= C' D T_lo (U3-ref RT*(f), F7), absorber capacity c_{L+1}/(Design
t) (U1 3.5), W3; and design-computed lower bounds lambda >= 1/D(l) computed after c_l (U4-ref C2-C6).  All survive the factor 1 - 2^{-l} >= 1/2.
Admissibility (T-b), (T-c), (T-d) and N-freeness: unchanged (upper bounds computed from the actual earlier weights).  The rate scheme gains
finitely many objects per level and b(w) only decreases (u(w^+) = b(w), Q(w) adapts), so U4-ref's Lemma GW applies.

## 10. Theorem S1, Master Theorem IV^tr, Corollaries.
Theorem S1: (a), (b) from Section 8 + V2 Lemma H + U1-ref 4.3; (c) the identity U1 Lemma 1.3 (with Lemma 1.1 the coupling rows Delta_m =
d^#(Domega) are equivalent to (X3) for data supported in Omega); RT*(c): per-scale cancellation of the coarse residues by the absorbers'
switching coefficients (U1 Prop. 3.4, U1-ref G1), whose bound is independent of the configuration.  Theorem S1 says nothing about the fine
structure of mixed classes (X2).  PROVED (given Section 8).
Master Theorem IV^tr: U1-ref's proof of IV' uses (KN_{w,a}) only through Proposition KN (statuses), the row (X4) (data violation <= K t; kind
[3] for points and increments of the cone) and the positive coarse gaps of U1 Lemma 4.3; Sections 3, 8 supply all three; the window constants
contain no 1/gap^# (kind [3] has no gap lower bound; c_flat uses the kind-[2] threshold gamma(w) = min M u/4).  PROVED modulo U1-ref's assembly.
Corollary IV^tr.1 (N = 1): every class is one-signed or unshifted; clean sub-windows exist at every main stage; pigeonhole gives a class with
>= n(w)/D_cls(w) scales for every g.  So every F-finite row of p_1 is in Rec(p_1), for T^tr(a), and by W2 for an admissible T^tr(b).  PROVED
modulo U1-ref's assembly (single referee pass).  Corollary IV^tr.2: SKETCH (X2 unrefereed; the polynomial gap with exponent beta <= Design(L)
enters X2's K_w as T^{-C beta}, dominated by (W_exp) c_{l+1} <= exp(-1/T_lo(l, M(l))) since 1/T >> C Design(L) log(1/T)).

## 11. Open
(1) Option (b) for N >= m(1) (carrier-1 exception).  (2) Mixed classes, N >= 2 (X2's C_mix).  (3) Infinite F: (E1)-(E5), U2's items, status
coherence at infinite F.  (4) Martin's p.  Lemma Z and density for p_N (every N, including N = 1) and for p: OPEN.  No counterexample.
