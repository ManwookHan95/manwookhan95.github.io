# X1-ref part 2 — 2.1 (three kinds of blocks), (X4^0), weight-freeness, Lemmas NLM, GEN, QC

## 1. Section 2.1 (U)/(KN)/(T).  Verdict: CORRECT, with precisions D1-D3.
The trichotomy is exhaustive at a clean sub-window: an active block (Delta'_m active) either has an inactive coarse carrier with rho in
[u, 1 + b] (KN), or every inactive coarse carrier has rho <= b or rho >= 1 + u (T) (no rate object lies in (b, u) or (1 + b, 1 + u));
blocks with Delta'_m inactive are (U).  Blocks with no active near-threshold carrier need nothing.
D1 ((U)-blocks, homogeneity).  r^(m) occurs only in the single row (X3)_m, so every minor of the cone is homogeneous of degree 0 or 1 in
r^(m) (correct).  The COFACTOR polynomials (minors of the matrices g_J of U1-ref 4.3) are multi-homogeneous of degree <= n (one degree in
{0,1} per column), so the rescaling r^(m) -> s r^(m) multiplies them by s^e, 0 <= e <= n: vanishing is preserved and robust ones change by
a factor >= s^n >= 1 - n(1 - s); with 1 - s = C Lip eta' << 1/n this is harmless.  X1's "factor in [s, 1]" is true for minors only.
D2 (inactive near-threshold carriers outside (KN)-blocks).  (T)-blocks have none by definition.  In (U)-blocks they may exist; they must
be strict non-peaks or robust peaks at f^#.  Fix: push them inward individually by eta' (U1-ref Prop. KN(b), last clause: they are not
variables of Gamma^#, kappa moves by O(X) and is restored).  X1's 2.6(b) "every other coarse carrier keeps its robust status" omits them.
D3 ((T)-block deviation).  "|rho_l(f) - rho^0_l(r(f))| <= C D^2 (b + c_{L+1}^2)" holds in the formula-1 convention (part 1, K1): nearly
neutral inactive carriers contribute O(D^2 b^2) (numerically O(b^2)), fine carriers O(D^2 c_{L+1}^2), active weak peaks O(b) through
sigma' (numerically 0.54 b).  Only the UPPER bound rho^0 <= rho (Lemma F, no (T) needed) is used in Step 1 of 2.6; the two-sided bound is
used only in 2.2(ii), and there only for positive blocks (for Delta' < 0 replacing rho by the smaller rho^0 makes (X4^0) weaker).

## 2. The floor-form row (X4^0).  Verdict: CORRECT (identity re-derived and checked numerically).
Identity: off the peak set the duality map is w(l) = C zeta(l)/(Phi_l^2 A) = vs_l (C theta/A) rho_l = vs_l M rho_l, so with Domega(l) =
gamma_l/lambda_l + Delta_m w(l) (U1 Lemma 1.1(a)) and Delta' = Delta M,
     lambda_l vs_l Domega(l) = vs_l gamma_l + Delta'_m lambda_l rho_l = vs_l gamma_l + Delta'_m m^2 |r_l| k        (lambda rho = m^2 |r| k).
indep_block.py (3): 200 random blocks, w from the duality map, relative error 7.5e-62.  (X4^0) is this identity with k replaced by the floor
K(sigma_rob, R_a^2).
(ii) Data at f.  Strict non-peaks of f: lem:suplevel(f) gives vs Domega_dec >= -3 gap(f)/t (as in U1-ref 4.1).  Weak peaks of f: eq:peakshift
gives vs(omega_- - omega_+) = e >= 0, i.e. vs gamma_dec + Delta'_dec lambda >= 0 (coefficient 1, since |w| = M at peaks); the (X4^0)
coefficient at the companion is lambda rho^0_l(r'') with |1 - rho^0_l(r'')| <= C b + Lip eta' (the weak peak sits at rho = 1 - b at f_1 and
r'' is within eta' of r_1).  The coefficient change from f to f^# is <= C_f lambda Lip eta' (ratios move by <= eta').  Altogether the
violation is <= lambda C_f (3 gap(f)/t + C D^2 (b + c^2) + Lip eta' + C b) <= K t for t >= T_lo(w) (gap(f) <= M b, b <= eta' <= T_lo^4).
(iii) Kind [3] at f^#.  vs Domega = [vs gamma + Delta' lambda rho^0]/lambda + Delta'(rho^# - rho^0) >= -|Delta'| (rho^# - rho^0) >=
-C_f C D^2 c_{L+1}^2 (inactive values 0 at f^#, so only fine terms separate rho^# from rho^0); this is >= -3 gap^#/t since gap^# >= M mu/2 >>
c_{L+1}^2.  The + side: vs omega^+ <= gap(f)/t <= gap^#/(4t) once M b <= gap^#/4; the shift trick of V1 TR Step 5 then gives kind [3]
(Y1 Prop. 5.2(iii): strict non-peak, inward up to 1.5 gap^#/t, |omega| <= A_2/t).  The shift trick's cost is lambda |x| with |x| <=
|Delta'| |rho^# - rho(f)| + K t/lambda; |rho^# - rho(f)| <= Lip eta' + C D^2 b (statuses move only through the ratio displacement), so the
cost is O(K t) as in V1.  [Note: mu(h) <= Lip h whenever Y_1 contains a point with F = 1 (G_h(r) >= 1 - Lip h there), so the companion
statuses are never far from those of f.]

## 3. Weight-freeness (2.2(iv)).  Verdict: CORRECT after one fix (W-fix).
Rows of Gamma^#(kappa, a) in the variables (Delta', gamma): (X1) entries u_l(j) (l in Omega_a; u_l = (y_l + delta_l h_l)/n_l on T(L) and on
near signature sets: weight-free) and Delta'_m tau_m(j) (peak vectors and PEAK weights lambda_p); aggregated signature rows (U1-ref 4.2: one
sign/zero row per near signature set; the coefficient ||v 1_near||_1 or lambda_p ||v_p 1_near||_1 scales a row and does not affect the
vanishing of minors); (X2), (X5) sign/zero rows; (X3)/kappa: entries r_l; (X4^0): vs_l and m^2 |r_l| K(sigma_rob, R_a^2) with sigma_rob a sum
of PEAK weights; (U)-rows vs gamma >= 0; (KN)-block rows (X4) with 1/lambda_l of (KN)-block carriers (not in N_T).  The cofactor polynomials
are built from the same matrix.  So Z_kappa and psi_d(r) = m |r_d| K(sigma_rob(m(d)), R_a(m(d))^2) contain no weight of a carrier of N_T. (Checked
row by row against U1 2.1 and U1-ref 4.1-4.3; nothing else enters: absorbers have r = 0 and weight-free vectors; class-R zero rows are
weight-free.)
W-fix.  X1's compact region K_kappa := {|r_l| <= 2 Phi_l/(m k_min), R(m)^2 <= 1 - eps_K} DOES contain the weights Phi_l of the carriers l
in N_T, so "Z independent of Phi" is literally false.  Two equivalent repairs: (a) drop the bounds |r_l| <= 2 Phi_l/(m k_min) for l in N_T
(R(m)^2 <= 1 - eps_K already makes the region compact, |r_l| <= 1/m), with eps_K(m) := sigma_rob(m)/4 (a function of peak weights): every
data point is interior because 1 - R^2 >= sigma/k >= sigma_rob/2 (from a^2 = sigma + k^2 R^2 >= k^2 R^2, k = a + sigma <= 2); (b) keep the
bounds and note that on the face |r_d| = 2 Phi_d/(m k_min) one has F >= psi_d/Phi_d >= 2K/k_min >= 2 (take k_min <= min K), so no witness of a
coincidence lies there and local minima with value 1 are local minima on the weight-free set.  With (a) the proofs of NLM, GEN, QC go through
verbatim.

## 4. Lemma NLM.  Verdict: CORRECT (re-derived).
B_kappa is first-order definable (Tarski-Seidenberg), so semialgebraic.  Stratify the compact semialgebraic Z (W-fix (a)) into finitely many
connected Nash manifolds compatible with the sign conditions on r_d (d in N_T) [BCR 9.1.8]; psi_d is Nash on each stratum contained in
{r_d != 0} (K is Nash on {R^2 < 1}).  If Phi in B_kappa with witness r_0 in a stratum S, D := {d : psi_d(r_0) = Phi_d} is non-empty and
r_0 lies in {r_d != 0} for d in D.  If r_0 were a regular point of Psi_{D,S} = (psi_d)_{d in D}|_S (differential onto R^D), a tangent vector
v with d psi_d(v) = -1 (d in D) and a Nash arc in S tangent to v would give F_Phi < 1 at points of S ⊂ Z arbitrarily close to r_0
(the d notin D stay below 1 by continuity): not a local minimum.  So r_0 is critical and Phi_D in CV_{D,S}; semialgebraic Sard [BCR
Thm 9.6.2] gives dim CV_{D,S} < |D| (this includes dim S < |D|, where every point is critical).  Hence B_kappa ⊂ union_{D,S} CV_{D,S} x
R^{N_T \ D}, of dimension < |N_T|.  The only property of "local minimum" used is: a local minimum on Z is a local minimum on the stratum
containing it.  Non-strict minima are included.  Correct.
Sanity (X1's sard_toy2, re-read): coincidence curve in the (Phi_1, Phi_2)-plane, minimizer critical for Psi_D, mu = 7.8e-16 at the
coincidence and 1.0e-3, 4.0e-3 after scaling the weights by 1.001, 1.01: consistent.

## 5. Lemma GEN.  Verdict: CORRECT (with a cleaner proof).
Proof (alternative to the CAD argument, same content).  Let k := k_0(weights of the pattern's carriers outside N_T); B_kappa is defined
over k (W-fix (a): eps_K in k).  By Tarski transfer B_kappa is the extension to R of a k^rc-semialgebraic set of the same dimension < n;
a semialgebraic set of dimension < n is contained in the zero set of a nonzero polynomial P with coefficients in k^rc (its Zariski closure
has dimension < n and is defined over k^rc).  If x := (Phi_d)_{d in N_T} were in B_kappa, then P(x) = 0; multiplying the finitely many
conjugates of P over k gives a nonzero polynomial with coefficients in k vanishing at x, contradicting the algebraic independence of the
Phi_d = 2^{-m(d)-k(d)} c_d over k (they are part of a family algebraically independent over k_0 and disjoint from the weights generating k).
The design side (choose c_l transcendental over k_0(c_1, ..., c_{l-1}) in an interval) makes the whole family algebraically independent.
Points to watch (all fine): (1) every non-weight datum must lie in k_0 WHATEVER the weights are — true for T_final/D^{U1'}: targets come
from the fixed countable pool by support rules, delta_l by (GM) from y_l and l only (U4 1.3(2)), n_l, u_l, h_l, S_l, mu_s rational/algebraic
over these, FD and absorber targets from fresh coordinates with binary values and integer R; (2) design THRESHOLDS (b(w), u(w), T_lo,
Design) may depend on weights — they are not coefficients of the cone (they only decide which minors are "tiny"), so they need not lie in k_0.

## 6. Lemma QC.  Verdict: CORRECT, with precisions Q1-Q3.
(a) G_h is upper semicontinuous on Z (re-derived); Y_1 compact; at r in Y_1 with F(r) = 1 the non-coincidence gives points of Z within h
with F < 1; usc attains its maximum: mu_kappa(h) > 0.  (b) Lojasiewicz [BCR 2.6.7] for f_1 = dist(., Y_1), f_2 = (F - 1)_+ on the compact Z,
f_2^{-1}(0) = Y_1 = f_1^{-1}(0); if Y_1 is empty, min_Z (F - 1) = m_0 > 0.  (c) mu_kappa is first-order definable in h, positive and
nondecreasing; by the Puiseux expansion of one-variable semialgebraic functions at 0+ (BCR 2.6 / van den Dries, Ch. 7) mu(h) = c h^{p/q}(1 + o(1)),
c > 0 (or mu has a positive limit), so mu >= c_kappa h^{beta_kappa} on (0, h_kappa].
Q1: mu_kappa(h) <= Lip(F) h whenever Y_1 contains a point with F = 1 (so beta_kappa >= 1 can be assumed); the companion statuses are then
within Lip eta' of those of f (used in part 2.2(iii) above).
Q2: Proposition KN^tr uses h = eta'(w)/3; one needs eta'(w)/3 <= h_kappa, i.e. Design(L) >= 1/h_kappa (add to the list of constants dominated
by Design(L); for h > h_kappa monotonicity gives mu(h) >= mu(h_kappa) anyway).
Q3: The Lojasiewicz step of 2.6 uses V2 Lemma L for continuous SEMIALGEBRAIC functions (the (X4^0) entries contain K and |r|) on the compact
region K_kappa: V2's proof (BCR 2.6.7) applies verbatim with Q := K_kappa and Z_S := zero set inside K_kappa (nearest points taken in K_kappa);
alternatively make everything polynomial by adjoining k_m as variables with the equations (1 - R_a(m)^2) k_m^2 - 2 sigma_rob k_m + sigma_rob^2
- sigma_rob = 0 and the signs vs_l r_l = |r_l| fixed by the pattern.
