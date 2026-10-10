# cert1 — Round 11 independent re-verification, cluster B: generic-weight threshold protection (X1's real-algebraic chain)

Referee: independent adversarial pass (Banach space theory / real algebraic geometry).  Root ctx = scratchpad/ctx.
Sources re-read: r9/X1_notes.md 1.1, 1.4, 2.1-2.6, 3.1; r9/X1_ref_notes.md 1-9 and X1_ref_part2.md; r10/Q1_notes.md 1.1-1.7
(esp. (S4)-(S6)); r10/Q1_refb_notes.md 1.1, 1.6, 2.2, 4 (E5-E8); r8/U1_notes.md 1.1-1.5, 2.1; r8/U1_ref_notes.md 1-5;
r7/V2_notes.md 1.2, 2 (Lemma L, D^{V2}); paper/martin_density_note.tex (lem:threshold, setting); paper2 cor:II-Rkt, lem:II-loj,
def:II-Gamma, lem:II-firsttouch.  Work files and scripts: r11/cert1_work/ (progress.md, blockK_check.py/.out,
nlm_qc_toy.py/.out, wfix_bounds.py/.out).
Every proof below was re-derived line by line from the definitions (block norm, lem:threshold, formula-1 kappa, U1 Lemma 1.1/1.3,
the cone rows), NOT by citing the earlier passes.  Numerics were written independently of the earlier solvers (different algorithm).

## 0. Verdicts

| # | Result | Verdict | Fix / remark |
|---|---|---|---|
| 1 | Lemma K (k = K(sigma,R^2), root choice, strict monotonicity in sigma and R^2, a^2 = E), K1, Lemma EC | CORRECT | none (numerics: closed form 1.6e-30, K1 8e-60, independent solver) |
| 2 | Weight-freeness of all rows / cofactor polynomials of Gamma^#(kappa,a) and of psi_d; W-fix region K_kappa = {R_a(m)^2 <= 1 - sigma_rob(m)/4} | CORRECT (given the W-fix and the K1 convention, both already in Q1) | remark: K1 is needed not only for tau_m but also for the aggregated signature row of an N_T carrier (as a peak trace that row would carry lambda_d); data interior with margin >= 3 sigma_rob/4 - O(b) |
| 3 | Lemma NLM (dim B_kappa < \|N_T\| on the W-fix region) | CORRECT | none |
| 4 | Lemma GEN (Tarski transfer over k = k_0(weights outside N_T), norm of conjugates) | CORRECT | none (equivalently: dim of a k-definable set >= trdeg_k of each of its points) |
| 5 | Lemma QC (a)-(c), Q1-Q3, design-number constants | CORRECT | cosmetic P-CY (normalization of C_Y), P-CHOICE (canonical choice of C_Y, alpha_Y, c, beta, h) |
| 6 | T_fin (S5)-(S6): QC objects, b_X1(w) by (D1), (D2) | CORRECT WITH FIXABLE GAPS | P-LIP (refb; needed), NEW P-SFAR (forward reference to c_{L+1} through s_far(w) in the level-L rate objects), P-CY |
| 7a | P-LIP (Lip* must dominate Lip_kappa of F_Phi in delta_0, and (D1)) | CORRECT; fix valid and sufficient | extend Lip* to the status functions of ALL active coarse carriers ("robust statuses move by <= Lip eta'"); in (D1) Lip* is harmless but not needed |
| 7b | alpha-mass identity sum_P (rho_k - 1) Phi_k^2 = C/M; sigma_rob > 0; natural peak | CORRECT | it is (E1) of U1 Lemma 1.2 divided by theta (refereed identity); numerics 6e-32 |

Answers to the six required checks: (i) YES; (ii) YES; (iii) YES; (iv) YES (with P-CY, P-CHOICE cosmetic); (v) YES after P-LIP
(Q1's literal "Lip" = Lip(l) of the determinantal objects is not shown to dominate Lip_kappa, which carries the factor 1/Phi_d);
(vi) YES: b_X1(w) > 0 needs mu_kappa(eta'/3) > 0 for every pattern of level l, i.e. non-coincidence, i.e. GEN for c_1..c_l, and
in T_fin's order c_l is chosen in (S4) before the level-l QC data (S5) and the sub-windows (S6).  No counterexample found.
After this pass every item of cluster B has two independent passes (X1-ref or refb + cert1).

## 1. Lemma K, K1, Lemma EC — CORRECT

Setting (lem:threshold): zeta = R_m^** zhat, A = |zeta|_m, w = J(zeta), M = ||w||_inf, C = ||Dw||_2, M + C = 1, theta = AM/C,
nu_k = |zeta_k|/Phi_k^2 = m|u_k(zhat)|/Phi_k, rho_k = nu_k/theta.  From zeta/A = alpha + D^2 w/C (||alpha||_1 = 1, supp alpha ⊂ P with the
signs of w): off P, w(k) = C zeta(k)/(Phi_k^2 A), so |w(k)| = M rho_k < M; on P, rho_k = 1 + |alpha_k| C/(M Phi_k^2) >= 1.  Hence P = {rho >= 1}.
(E2): C^2 = sum Phi^2 w^2 = M^2 (Phi_P^2 + sum_Q rho^2 Phi^2), i.e. a^2 = (C/M)^2 = Phi_P^2 + sum_Q rho^2 Phi^2 (a := A/theta = C/M); this is
also the uniform form a^2 = sum_k Phi_k^2 min(rho_k,1)^2.
Formula 1 with Omega ⊂ Q: kappa = [A(A + theta) - sum_Omega nu^2 Phi^2]/theta = A + theta Phi_P^2 + S_f/theta (insert (E2)), so
k := kappa/theta = a + sigma, sigma := Phi_P^2 + s_f; and sum_Omega nu^2 Phi^2 = m^2 sum_Omega u_l(zhat)^2 = kappa^2 R^2 gives
a^2 = sigma + k^2 R^2.  sigma > 0 because P is nonempty (lem:threshold), hence a^2 > k^2 R^2 and k > a, so R < 1 and a > kR.
Eliminating a: (1 - R^2)k^2 - 2 sigma k + sigma^2 - sigma = 0 (equivalently (k - sigma)^2 = sigma + k^2 R^2), roots
k_+- = [sigma +- sqrt(sigma^2 R^2 + sigma(1 - R^2))]/(1 - R^2).  k_- <= sigma <=> sigma R^2 <= sqrt(...) <=> 0 <= sigma(1-R^2)(1 + sigma R^2):
true, so k_- would give a <= 0; k_+ - sigma = [sigma R^2 + sqrt(...)]/(1 - R^2) > 0.  So k = K(sigma, R^2).
Monotonicity.  d/ds of the numerator = 1 + (2sx + 1 - x)/(2 sqrt(s^2 x + s(1-x))) > 0.  In x = R^2 (sigma fixed), along the + branch
(a := k - sigma satisfies a^2 = sigma + k^2 x): 2a dk = k^2 dx + 2kx dk, dk/dx = k^2/(2(a - kx)) and a = sqrt(sigma + k^2 x) > k sqrt(x) >= kx,
so dk/dx > 0 on all of [0, 1).  K is real-analytic (Nash) on (0, inf) x [0, 1) (discriminant > 0).  rho_l = m|u_l|/(Phi_l theta) =
m|r_l| k/Phi_l.  [II] cor:II-Rkt states the same identities with r^II = m|r| and proves uniqueness of the root on {a > c_0 R/(1-R)}:
consistent.
K1 (active weak peaks in Omega).  kappa(Omega) = A + [theta^2 Phi_P^2 + sum_Q nu^2 Phi^2 - sum_Omega nu^2 Phi^2]/theta
= A + theta sigma', sigma' = Phi_{P\Omega}^2 + sum_{Omega∩P}(1 - rho^2) Phi^2 + s_f, and a^2 = sigma' + sum_Omega rho^2 Phi^2 = sigma' + k^2 R^2.
Same system; for active weak peaks rho in [1, 1+b], the correction is in [-3b Phi^2, 0], so sigma' >= sigma_rob - 3b||Phi||^2 > 0.
Lemma EC.  U1 Lemma 1.1(a): V(Domega) = sum_l gamma_l u_l, gamma_l = lambda_l(Domega(l) - Delta_m w(l)); coarse peaks p: gamma_p =
-Delta'_m lambda_p vs_p; inactive Omega carriers: gamma = 0; so on E_c, L = sum_{Omega_a} gamma_l u_l - sum_m Delta'_m tau_m,
tau_m = sum_{coarse peaks p of m} vs_p lambda_p u_p|_{E_c}.  (X3)/kappa_m: Delta'_m = sum_{Omega_a(m)} r_l gamma_l.  Substituting,
L = sum_l gamma_l (u_l - r_l tau_{m(l)}).  Columns depend on their own ratio and on tau_m (peak vectors in k_0, peak weights).  CORRECT.
Numerics (cert1_work/blockK_check.out; independent solver: outer golden-section maximization of the concave function
M -> max{<w,zeta> : |w_k| <= M, ||Dw||_2 <= 1 - M}, inner bisection; 60 digits; 40 random blocks, m in 1..4, 4-8 carriers):
threshold structure |w_k| = M min(1, rho_k) 7e-30; (E2) 1.3e-30; alpha-mass 6.3e-32; Lemma K closed form 1.6e-30 (solver-limited);
K1 8.0e-60; rho = m|r|k/Phi 1.2e-61; E5: min (1 - R^2) - sigma = 0.467 >= 0, closed form 1 - R^2 = sigma(1+2a+sigma)/(a+sigma)^2 to 4e-32;
monotonicity (finite differences) and the floor inequality of Lemma F hold in every block.

## 2. Weight-freeness and the W-fix region — CORRECT

Variables (Delta', gamma) with gamma_l = lambda_l(Domega(l) - Delta w(l)) (the variable gamma absorbs lambda_l).  Row by row
(U1 2.1, U1-ref 4.1-4.3, [II] def:II-Gamma, X1 2.2(iv)):
 (X1) on T(L) \ F^#: entries u_l(j) (l in Omega_a; u_l = (y_l + delta_l h_l)/n_l, in k_0 by GEN_fin(a)) and Delta'_m-entries -tau_m(j)
      (peak weights lambda_p, p in the pattern's coarse peaks).  On S_l ∩ (L, s_far(w)] only l lives among coarse carriers:
      aggregated row with coefficient ||v_l 1_{S_l ∩ (L, s_far]}||_1 = (delta_l/n_l) sum 2^{-s} in k_0 for EVERY integer s_far,
      multiplying gamma_l if l in Omega, or -Delta'_m vs_l lambda_l if l is a peak.
      ATTACK: an active near-threshold carrier d of a (T)-block that is a WEAK PEAK of f would, as a peak, put lambda_d into tau_m AND into
      its own aggregated row.  K1 (active weak peaks belong to the pattern's Omega; at f^# they are strict non-peaks after Step 0 and
      Step 3) removes both.  So K1 is necessary and sufficient here; with K1 neither row contains lambda_d.
 (X2)/(X5): signs/zero rows (entries +-1).   (X3)/kappa: Delta'_m - sum_{Omega_a(m)} r_l gamma_l = 0 (entries 1, r_l).
 (X4^0) in (T)-blocks: vs_l gamma_l + Delta'_m m^2 |r_l| K(sigma_rob(m), R_a(m)^2) >= 0.  Re-derived: off P, w(l) = vs_l M rho_l, so
      lambda_l vs_l Domega(l) = vs_l gamma_l + Delta'_m lambda_l rho_l, and lambda_l rho_l = m Phi_l (m|r_l| k/Phi_l) = m^2 |r_l| k; (X4^0)
      replaces k by the floor.  Weight-free (sigma_rob = sum of peak weights).  U1-ref's (X4) "vs gamma/lambda + Delta' >= 0" carries
      1/lambda_l: the ONLY row that could carry an N_T weight; it is kept only in (KN)-blocks (weights outside N_T, in k).
 (U)-rows: vs_l gamma_l >= 0.  Cofactor polynomials: polynomials in the entries of the same matrix.
 psi_d(r) = m|r_d| K(sigma_rob(m(d)), R_a(m(d))(r)^2), rho^0_d = psi_d/Phi_d.
So Z_kappa (tiny minors and tiny cofactor polynomials) and psi_d are functions of: k_0-data, peak vectors/weights, sigma_rob, signs and
labels, (KN)-block weights, the ratio variables r.  No N_T weight and no continuous datum of f (refb F1, re-confirmed).
Disjointness checks: N_T ∩ P_rob = {} (near-threshold vs robust peaks); each stage has one block, so lambda_d (d in N_T) cannot enter
tau_{m'} for m' != m(d); (T)-blocks contain no inactive near-threshold carrier by definition, and class-R/anti-type near-threshold carriers
would make the block (KN) (an inactive carrier with rho in [u, 1+b]).
W-fix region.  X1's original region contained |r_l| <= 2 Phi_l/(m k_min) (N_T weights!) — X1-ref's W-fix (a) is needed and correct:
K_kappa := {r : R_a(m)^2 <= 1 - sigma_rob(m)/4, all active m} is compact (|r_l| <= 1/m), semialgebraic, defined over k.
Interiority of the data (refb E5 re-derived): 1 - R^2 = sigma(1 + 2a + sigma)/(a + sigma)^2 >= sigma because a + sigma <= ||Phi_m||_2 +
||Phi_m||_2^2 <= 0.372 (a = C/M <= ||Phi||_2 since C = ||Dw||_2 <= M||Phi||_2; sigma <= ||Phi||_2^2; ||Phi_m||_2^2 <= 4^{-m}/3).  With K1:
R_a^2 <= R^2 <= 1 - sigma' <= 1 - sigma_rob + 3b||Phi||^2, margin >= 3 sigma_rob/4 - 3b/12 (sigma_rob >= Phi_min(L)^2 >> b).  r_1 (Step 0
moves ratios by O(b)) and every point within eta' of it are interior as well.
Bounds on the region (wfix_bounds.out): K <= 4(1 + sqrt(5/4 - sigma_rob/4)) ~ 8.47, a - kx >= 1.11 sigma_rob, dK/dx <= 32.1/sigma_rob;
hence Lip(psi_d) on K_kappa <= C m/(sigma_rob) and Lip_kappa <= C m/(sigma_rob Phi_d) <= C L D(L)^3: finite design numbers.

## 3. Lemma NLM — CORRECT
Statement (with W-fix): Z := Z_kappa ∩ K_kappa (compact, semialgebraic, defined over k, independent of Phi := (Phi_d)_{d in N_T});
F_Phi := max_{d in N_T} psi_d/Phi_d on Z; B_kappa := {Phi in (0,inf)^{N_T} : some r_0 in Z with F_Phi(r_0) = 1 is a (possibly non-strict)
local minimum of F_Phi on Z}.  Claim: dim B_kappa < |N_T|.
Re-derivation.  B_kappa = {Phi : exists r_0 in Z, F_Phi(r_0) = 1, exists eps > 0 forall r in Z (|r - r_0| < eps -> F_Phi(r) >= 1)} is
first-order definable over k, hence semialgebraic (Tarski-Seidenberg).  Take a finite partition of Z into connected Nash submanifolds S
compatible with {r_d > 0}, {r_d = 0}, {r_d < 0} (d in N_T) [BCR 9.1.8]; on each S, |r_d| = +-r_d or 0 and R_a^2 < 1, so every psi_d|_S is
Nash.  Let Phi in B_kappa with witness r_0 in S and D := {d : psi_d(r_0) = Phi_d} (nonempty since F(r_0) = 1; r_{0,d} != 0 for d in D).
A local minimum on Z is one on S.  If d(Psi_{D,S})(r_0) : T_{r_0}S -> R^D were onto, pick v with d psi_d(r_0) v = -1 (d in D) and a Nash
arc gamma in S (straight segment in a Nash chart) with gamma'(0) = v: psi_d(gamma(s)) = Phi_d - s + o(s) < Phi_d for d in D, and
psi_d(gamma(s)) < Phi_d for d notin D by continuity; so F(gamma(s)) < 1 for small s > 0 — contradiction.  Hence Phi_D is a critical value
of the Nash map Psi_{D,S} : S -> R^D, and the semialgebraic Sard theorem [BCR 9.6.2] gives dim CV_{D,S} < |D| (this contains the case
dim S < |D|).  B_kappa ⊂ U_{D,S} {Phi : Phi_D in CV_{D,S}}, finite union of sets of dimension < |D| + |N_T \ D| = |N_T|.  QED.
Attacks tried (all fail): (a) isolated points r* of Z (0-dim strata) are automatically local minima: the corresponding Phi form
{max_d psi_d(r*)/Phi_d = 1}, of codimension 1 — included in the Sard count, and avoided generically because psi_d(r*) is algebraic over k;
(b) kinks of the max: handled by the active set D; (c) minima on the boundary of K_kappa: boundary strata are strata of Z, same argument;
(d) non-strict minima / flat pieces: only "local min on Z => local min on S" is used; (e) non-smoothness of |r_d| at r_d = 0: witnesses
have r_d != 0 for d in D, and for d notin D only continuity is used; (f) dependence of Z on Phi: none after the W-fix (Section 2); the
labels tiny/robust, N_T, signs are discrete pattern data.
Numerics (nlm_qc_toy.out, independent of X1's sard_toy2): EC-structured toy (2x2 minor det[u_1 - r_1 tau, u_2 - r_2 tau], affine in r, so Z is
a line; psi_d with the true K and the W-fix region): coincidence weights give min_Z F = 1.000000000000 at a crossing with tangential slopes
-2.39 / +1.37 (critical for Psi_D, D = {1,2}) and mu(h) = 0; random weights in [0.06,0.10]^2 give P(|min_Z F - 1| < eps) = 0.34, 0.032,
0.0032 for eps = 0.1, 0.01, 0.001 (codimension one); a cusp-shaped Z with the coincidence at the cusp tip behaves the same way.

## 4. Lemma GEN — CORRECT
Let k := k_0(weights of the pattern's carriers outside N_T) (finitely many; the integer s_far(w) and all signs/labels are in Q).  B_kappa is
defined by a formula with parameters in k.  Let k^rc be the real closure of k in R and B_0 the k^rc-semialgebraic set defined by the same
formula; then B_kappa = (B_0)_R (extension) and dim B_0 = dim B_kappa < n := |N_T| [BCR Ch. 5, invariance of dimension under extension of
real closed fields].  The Zariski closure of B_0 over k^rc has dimension = dim B_0 < n, so some nonzero P in k^rc[X_1..X_n] vanishes on
B_0; the sentence "forall x (x in B_0 -> P(x) = 0)" transfers to R, so B_kappa ⊂ V(P).  The coefficients of P lie in a finite (separable,
char 0) extension k' of k; N(P) := prod over the k-embeddings sigma of k' into an algebraic closure of sigma(P) has coefficients in k, is
nonzero (product of nonzero polynomials), and vanishes on V(P).  If Phi in B_kappa, N(P)(Phi) = 0 is a nontrivial algebraic relation
over k.  But (c_l) a.i. over k_0 (GEN_fin(b), 2 passes; transcendence induction re-checked) implies that the finitely many Phi_d =
2^{-m(d)-k(d)} c_d (d in N_T) are a.i. over k_0(Phi_l : l outside N_T) ⊇ k.  Contradiction.  QED.
(Equivalent one-line form: for a k-definable set B, dim B >= trdeg_k k(x) for every x in B; a point with a.i. coordinates has
trdeg n.)  X1's CAD version is also correct (if the polynomial relation P(x, Y) degenerates in Y at the point, a nonzero coefficient
gives a relation among the earlier coordinates).
Attacks tried: (a) B_kappa might depend on thresholds b, u, T_lo, Design (weight-dependent, not in k_0): NO — they only decide which minors
are tiny, i.e. which pattern; B_kappa of a fixed pattern does not contain them; (b) s_far(w) depends on c_{L+1}: enters only as an integer
(coefficients in k_0 for every s) and, by row scaling, not at all in Z (Section 6, P-SFAR); (c) peak weights / (KN)-weights in k: they are
outside N_T and a.i. together with the N_T weights over k_0 (one a.i. family), so the N_T weights remain a.i. over k; (d) option (b):
c_1 = 1 is rational, so patterns with stage 1 in N_T are excluded (as Q1 does); option (a): c_1 transcendental.  No order-of-choices
issue: algebraic independence of the WHOLE family is used, not the order.

## 5. Lemma QC (a)-(c), Q1-Q3 — CORRECT (cosmetic precisions P-CY, P-CHOICE)
(a) G_h(r) := inf{F(r'') : r'' in Z, |r'' - r| < h} is upper semicontinuous (an admissible r'' for r is admissible for r_n near r);
Y_1 := Z ∩ {F <= 1} is compact; on Y_1, G_h < 1: if F(r) < 1 trivially, if F(r) = 1 because r is not a local minimum (Phi notin B_kappa,
Section 4).  An usc function attains its sup on a compact set, so mu_kappa(h) := 1 - max_{Y_1} G_h > 0 (mu := 1 if Y_1 is empty).
For KN^tr Step 3 note that the inf over the OPEN ball need not be attained; take r'' in the CLOSED ball (Z compact, F continuous):
F(r'') <= G_h(r_1') <= 1 - mu(h), |r'' - r_1'| <= h.  Harmless.
(b) Y_1 empty: F - 1 > 0 continuous on compact Z, so F >= 1 + m_0.  Otherwise f_1 = dist(., Y_1), f_2 = (F - 1)_+ are continuous semialgebraic
on compact Z with f_2^{-1}(0) = Y_1 = f_1^{-1}(0); Lojasiewicz [BCR 2.6.7]: f_1^N <= C f_2.
P-CY (cosmetic): X1 2.5(b) normalizes dist <= C_Y (F - 1)_+^{alpha_Y}; X1-ref 7(b), the MTVI graph and Q1 (S5) quote dist^{1/alpha_Y} <=
C_Y (F - 1)_+.  Q1's (D2) clause delta_0(b) <= (eta'/(3 C_Y))^{1/alpha_Y} gives dist <= eta'/3 in X1's normalization, and in X1-ref's only
if C_Y >= 1 (dist <= C_Y^{alpha - 1} eta'/3).  Fix: state X1's normalization in (S5), or put C_Y := max(1, C_Y).
(c) h -> mu_kappa(h) is first-order definable (parameters k and Phi), positive (a) and nondecreasing (G_h nonincreasing in h), bounded by 1
(F >= 0).  A one-variable semialgebraic function has a convergent Puiseux expansion at 0+ (the real closure of R(t) is the field of
algebraic Puiseux series; van den Dries, Tame Topology Ch. 7, or BCR Ch. 2 — X1's "BCR Section 2.6" is a loose reference): mu(h) =
c h^{p/q}(1 + o(1)) with c > 0, p/q >= 0 (p/q = 0 if mu has a positive limit).  So mu >= c_kappa h^{beta_kappa} on (0, h_kappa] with
c_kappa := c/2, beta_kappa := p/q.
P-CHOICE (cosmetic, well-definedness of the recursion): the design needs DEFINITE values; e.g. N := least admissible Lojasiewicz exponent,
C_Y := least admissible constant for it (a sup of a ratio, finite), beta_kappa := Puiseux exponent, c_kappa := half the leading coefficient,
h_kappa := min(1, sup{h : mu >= c_kappa t^beta on (0, h]}); V2's remark (a) to Lemma L uses the same device.  Only existence is used.
Q1: if r* in Y_1 has F(r*) = 1 then G_h(r*) >= 1 - Lip_kappa h, so mu(h) <= Lip_kappa h — correct as a conditional statement (it can fail
when F < 1 on all of Y_1; then the uses of "mu small" in S-0 must be replaced by the case split mu >= T_lo^4 / mu < T_lo^4, which gives the
same conclusion drift << mu: cluster A remark, not needed here).
Q2: eta'/3 = T_lo^4/(3 L Design(L)) <= 1/Design(L) <= h_kappa because (S5) puts max(1, 1/h_kappa) into Design(l); likewise
c_kappa >= 1/Design, beta_kappa <= Design (each factor of the product is >= 1, so each is <= Design(l)).
Q3: V2 Lemma L for continuous semialgebraic functions on the compact semialgebraic K_kappa, with the zero set taken inside K_kappa:
re-derived — Pi_S := sum_{i in S} pi_i^2, Z_S := Pi_S^{-1}(0) ∩ K_kappa, g_S := dist(., Z_S) (or 1 if Z_S is empty); BCR 2.6.7 on
K_kappa gives g_S^{N_S} <= C_S Pi_S; alternative (i) (Z_S empty) is excluded at f's pattern because beta := (1 + Lip* C_*) b <= eta < 1/C_L
(b <= b_U4, Design >= C_L).  The nearest point lies in K_kappa, so Step 2 (QC(b)) and Step 3 (QC(a)) apply to it.  r_1 must be in K_kappa:
Section 2 (interior, margin ~3 sigma_rob/4).
Numerics (nlm_qc_toy.out): generic weights mu(h) = 1.336e-2, 4.02e-3, 1.34e-3, 4.03e-4 at h = 1e-2..3e-4 (fitted beta = 0.999);
coincidence weights mu = 0; weights x(1 + 1e-3): mu(1e-3) = 1.0e-3.

## 6. T_fin (S5)-(S6): QC objects and b_X1(w) — CORRECT WITH FIXABLE GAPS (P-LIP, P-SFAR, P-CY)
Order at stage l (re-checked against Q1 1.3 and refb 1.1): target -> (GM) delta_l -> n_l, u_l -> c^max_l (uses b(l-1, M(l-1)),
T_lo(l-1, M(l-1)) or, at clusters, level-p data) -> GENERIC c_l (transcendental over k_0(c_1..c_{l-1}); possible: interval of positive length,
countable field) -> (S5) level data: rate objects, Lip(l), C_L(l), N_L(l) on the K_kappa, and for every pattern of level l (carriers <= l,
their blocks; N-free) the QC data Z_kappa, F_Phi, Lip_kappa, mu_kappa(.), m_0, C_Y, alpha_Y, c_kappa, beta_kappa, h_kappa with the ACTUAL
weights c_1..c_l -> Design(l) (dominates max(1, Lip_kappa), C_Y, 1/m_0, 1/c_kappa, beta_kappa, 1/h_kappa) -> (S6) for w = (l, i): u(w) =
b(w^-), Q(w), n(w), T_hi, T_lo, eta'(w) = T_lo^4/(l Design(l)), then b(w) = min(b_U4, b_X1).
(vi) b_X1(w) > 0.  Left sides of (D1), (D2) are continuous, strictly increasing in b, -> 0; right sides are positive (possibly +inf by the
conventions m_0 = inf, C_Y = 0) numbers already computed; the clause b <= min_kappa mu_kappa(eta'/3)/8 is positive iff every pattern of
level l is non-coincident, i.e. iff Phi_{N_T(kappa)} notin B_kappa for all kappa — GEN applied to c_1..c_l (and only to them: a pattern of
level l involves carriers <= l), all chosen in (S4) of stages <= l.  So b_X1(w) > 0 is reached only after the generic choice of c_l, and no
earlier quantity uses it (c^max_l uses level l-1 data only; (W2), (W7), (W_exp) are imposed at the next stage).  Option (b): minima over
patterns with stage 1 notin N_T only (as Q1 states).  CORRECT.
Monotonicity/no lower-bound use: b(w) enters later quantities only through upper bounds (c_{L+1} <= b^2, u(w^+) = b(w), Q(w^+) grows), so the
non-explicit exponents 1/alpha_Y, N_L/2 in b_X1 need not be dominated by Design; u(w) >= T_lo(w) holds automatically (T_hi(w) <=
2^{-l^3}/(l Q(w)) <= u(w)/(l 2^{l^3}) since Q(w) >= 4 Design/u(w) >= 1/u(w)).
P-LIP (refb; NEEDED).  KN^tr Step 1 uses F(r') <= F(r_1) + Lip_kappa |r' - r_1|; Q1's delta_0(b) has Lip(l) = Lipschitz constant of the
determinantal objects, which is NOT shown to dominate Lip_kappa: d(psi_d/Phi_d)/dr_d >= m K(sigma_rob, 0)/Phi_d >= m sqrt(sigma_rob)/Phi_d
contains the factor 1/Phi_d = 2^{m+k}/c_d, which no determinantal entry contains (the (X4^0) entry m^2|r_d|K has Lipschitz constant
<= 8.5 m^2 + 64 m^2/sigma_rob on K_kappa).  If Lip(l) < Lip_kappa the bound F(r') <= 1 + delta_0 can fail,
and with it Step 2 (Y_1 nonempty, dist(r', Y_1) <= eta'/3).  Fix (refb): Lip*(l) := max(Lip(l), max_kappa Lip_kappa) in the middle term of
delta_0(b) (in (D1) it is harmless but not needed).  Extension P-LIP+: the claim "robust statuses move by <= Lip eta' << u" needs the
Lipschitz constants of the floor/status functions m|r_l|K(sigma_rob, R_a^2)/Phi_l of ALL active coarse carriers l on K_kappa; by Section 2
these are <= C m/(sigma_rob Phi_l) <= C L D(L)^3 <= Design(L), so include them in Lip*.  Lip*(l) <= Design(l) (S5), nothing else changes.
NEW P-SFAR (forward reference; cosmetic).  The level-L rate objects of (S5) are minors/cofactor polynomials of Gamma^#(kappa, a), whose
aggregated (X1) rows on S_l ∩ (L, s_far(w)] carry the coefficient ||v_l 1_{S_l ∩ (L, s_far(w)]}||_1 (U1-ref 4.2, [II] def:II-Gamma), and
s_far(w) := least s with 2^{-s} <= c_{L+1}^2 ([II] lem:II-firsttouch, U1 3.3) depends on c_{L+1}, chosen at stage L+1 AFTER the level-L
sub-windows, which need omega(L), i.e. the rate objects.  Literally this contradicts Lemma W_fin(a) ("every quantity of stage l is a function
of earlier quantities").  No source addresses it (grep of r9, r10, paper2: s_far appears only in the k_0-membership remarks GEN_fin(a),
refb 1.6).  Fix: in (S5) use the s-free coefficient alpha_l := ||v_l 1_{S_l ∩ (L, inf)}||_1 = (delta_l/n_l) sum_{s in S_l, s > L} 2^{-s}
(in k_0).  The cone at w differs from the rate-object matrix by positive row scalings t_l in [1 - 2^{1 + s_1(l) - s_far}, 1], s_1(l) := least
element of S_l beyond L (s_1(l) <= L + 3 * 2^L, while (W5) — imposed at PRE/MAIN stages and, via c^cl(p), at p+1 — gives c_{L+1} <= 2^{-min S_{L+1}} =
2^{-3 * 2^{L+1}}, so s_far >= 12 * 2^L and t_l >= 1 - 2^{1 + L - 9 * 2^L}).  Positive row scaling multiplies every minor and every
cofactor-vector component (hence every minor of g_J) by a product of the t_l: zero sets are identical (Z_kappa, hence B_kappa, the QC data,
F_Phi, mu_kappa unchanged), tiny objects stay <= b, robust ones stay >= u (1 - eps)^n >= u/2, Hoffman (V2 Lemma H) and Lojasiewicz constants
change by factors <= 2.  The label "type of the aggregated row" (sign row eps / equality row / absent) is a finite datum, enumerated.
Weight-freeness is unaffected (coefficients in k_0 for every s).
P-CY: see Section 5 (b).
N-independence: patterns range over carriers <= l and their blocks; for p_N the pattern is the design pattern with blocks > N inactive (they
contribute no row: Delta'_m = 0 kills tau_m, gamma = 0 kills columns and aggregated rows); QC data involve only (T)-blocks.  CORRECT.

## 7. P-LIP and the alpha-mass identity — CORRECT
P-LIP: Section 6 (valid, sufficient; P-LIP+ extension).
alpha-mass: pairing zeta/A = alpha + D^2 w/C with w gives 1 = <w, alpha> + C = M ||alpha||_1 + C, so ||alpha||_1 = 1; for k in P,
rho_k - 1 = |alpha_k| C/(M Phi_k^2), hence sum_{k in P} (rho_k - 1) Phi_k^2 = C/M (= a = A/theta; it is (E1) of U1 Lemma 1.2 divided by
theta).  Consequences re-derived: (i) a strict peak exists (C/M > 0) and a natural peak maximizing (rho_k - 1) Phi_k^2 exists (terms <=
lambda_k/theta -> 0), with an f-margin; (ii) at a clean w, coarse weak peaks (rho in [1, 1+b]) contribute <= b ||Phi_m||_2^2 <= b/12, fine
peaks <= sum_{fine} rho Phi^2 = sum_{fine} |zeta_k|/theta <= sum_{fine} lambda_k/theta <= C_f c_{L+1} (|u_k(zhat)| <= q*(u_k) q**(zhat) = 1), so
robust coarse peaks (rho >= 1 + u) carry >= C/M - b/12 - C_f c_{L+1} > 0 for L >= l_f: sigma_rob(m) >= Phi_min(L)^2 > 0.  Numerics: 6.3e-32
(blockK_check.out), consistent with refb's alpha_mass.out (6.5e-51).

## 8. Numerics (r11/cert1_work/)
 blockK_check.py/.out — independent 60-digit block solver (outer concave maximization in M, inner bisection), 40 blocks: lem:threshold
   structure, (E2), alpha-mass, Lemma K, K1, rho = m|r|k/Phi, E5 margin (min 0.467), monotonicity, Lemma F floor.
 nlm_qc_toy.py/.out — EC-structured NLM/QC toy (affine 2x2 minor, true K, W-fix region), coincidence vs generic weights, codimension
   sampling, cusp-shaped Z.
 wfix_bounds.py/.out — K <= 8.47, a - kx >= 1.11 sigma_rob, dK/dx <= 32.1/sigma_rob on the W-fix region; a + sigma <= 0.372.
 progress.md — step log.

## 9. Fixes / precisions to record (none changes a statement or the design's logic)
 P-LIP (refb, confirmed NEEDED) + P-LIP+: Lip*(l) := max(Lip(l), max_kappa Lip_kappa, Lipschitz constants on K_kappa of the floor statuses
   m|r_l| K(sigma_rob, R_a^2)/Phi_l of all active coarse carriers) in delta_0(b) and in "robust statuses move by <= Lip* eta'"; Lip* <= Design(l).
 P-SFAR (NEW): level-L rate objects with s-free aggregated coefficients ||v_l 1_{S_l ∩ (L, inf)}||_1; the cone at w differs by positive row
   scalings in [1 - 2^{1 + s_1 - s_far}, 1]; zero sets identical, robust values/Hoffman/Lojasiewicz constants within factor 2.  Removes the
   forward reference to c_{L+1} in (S5) (the same wording appears in [II] def:II-Gamma with lem:II-firsttouch's s_far(w); the same
   one-line fix applies there; [II]'s design order was not re-audited here).
 P-CY: fix the normalization dist(., Y_1) <= C_Y (F - 1)_+^{alpha_Y} (X1 2.5(b)) in (S5), or C_Y := max(1, C_Y).
 P-CHOICE: canonical choice rules for C_Y, alpha_Y, c_kappa, beta_kappa, h_kappa (and C_L, N_L as in V2's remark (a)).
 K1 remark: K1 is what keeps BOTH tau_m and the aggregated signature row of an N_T carrier weight-free; state it in X1 2.2(iv) / Q1 (S5).
 Step 3 of KN^tr: take r'' in the closed h-ball (the inf over the open ball need not be attained).
 References: Puiseux for one-variable semialgebraic functions — cite van den Dries Ch. 7 or the algebraic Puiseux series description of the
   real closure of R(t), rather than "BCR Section 2.6".

## 10. Pass count after this round
Items (1)-(7) of cluster B (MTVI graph 7.1 items 7, 8 (Lemma K part), 9, 23 (P-LIP, alpha-mass) and the (S5)-(S6) QC objects) now have
two independent written passes (X1-ref / refb + cert1).  Lemma F (graph item 8, second half) and the uses of these lemmas inside KN^tr
(Steps 0-4, KN-1, S-0, (X4^0) data/kind [3]) belong to cluster A and were not re-certified here beyond the inequalities quoted in Sections 2, 5, 6.
