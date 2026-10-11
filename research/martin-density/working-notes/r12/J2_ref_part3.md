# J2-ref part 3: data-sign precision, the direct route (J2.4, J2.5, J2.6, 3.3), combination with J1; numerics on K-8

## 3.1 Data sign of a weak peak (precision to K1-ref R-8 / K2-ref W-1).  Verdict: CORRECT.
Part I lem:peakshift (martin_density_note.tex l. 4821-4856): for every peak k, varsigma_k omega_+(k) <= 0 <= varsigma_k omega_-(k), and
|omega_+(k)| + |omega_-(k)| = -varsigma_k DeltaTheta(k) - Delta d M with Delta d = d_+ - d_-; the left side is bounded by t/(sigma|alpha(k)|) only
when alpha(k) != 0, so for a weak peak (alpha(k) = O(b)) e_k := |omega_+(k)| + |omega_-(k)| is NOT small.  In U1's convention (Delta = d(omega^-) -
d(omega^+) = -Delta d, Domega = omega^- - omega^+, gamma = lambda(Domega - Delta w) = -lambda DeltaTheta, w(k) = varsigma_k M at peaks):
varsigma_k gamma_k/lambda_k = e_k - Delta'_m, so eps_k = sgn gamma_k = vs_k sgn(e_k - Delta'_m).  Robust peaks: Domega(p) = 0 in the class cone
(X1 Lemma EC), eps_p = -sgn(Delta'_m) vs_p.  R-8's "eps_k = -sgn(Delta''_m) vs_k" fails exactly when Delta'_m > 0 and e_k > Delta'_m (then
eps_k = +vs_k: a near bank moves |u_k| OUTWARD, so R-8's resource "near bank if Delta''_m > 0" is not a push for such k).  Effect on the record:
none -- K2-ref replaced (H1) by the joint (H1*), which is formulated by its effect (rho_k <= 1 - b after the moves), not by a resource list.
J2's claim "No conclusion of K1-ref or K2-ref changes" is CORRECT.

## 3.2 Proposition J2.4 (direct joint push).  Verdict: CORRECT with precisions (not needed by Theorem J2.1).
Re-derivation.  Own pushes: k in W(m) with eps_k = -vs_k uses a bank/raise at a near coordinate of the data sign (moves u_k(xhat) in direction
eps_k, i.e. inward); eps_k = vs_k uses a pull (moves u_k in direction -eps_k by 2 v_k(j), Y4-ref C.2); zero data (e_k = Delta'_m) uses (P1).
Threshold raisers: Lemma J2.0(a).  First-order privacy: a bank at a contact s notin F private to k changes u_j(xhat), j != k coarse, by
(mu_s^2/nu) D_{u_j}(s) dm = 0 (u_j(s) = 0, a_s = 0); a pull's new support mass enters other carriers only through a_j (second order).
PRECISION J4-a (thin raises).  A raise at a THIN coordinate s in F (|a_s| <= b) changes u_j(xhat), j != k, at first order by
-(mu_s^2/nu) kappa_{u_j} a_s dm: relative to the own action ((mu_s^2/nu)(u_k(s) - kappa_{u_k} a_s)) this is <= Design(L) b.  "Private moves act at
first order only on their own value" is true only up to this relative O(Design b) cross term; the overshoot absorbs it (Design b x Design^C
b/u^2 << b).
PRECISION J4-b (constants).  An own push from rho <= 1 + b to 1 - b needs <= 5 b theta Phi_k/m in u-units (J2: 3; part 1, 1.1(b)).
PRECISION J4-c (moduli created by Step-0 banks; also inherited by K2.15 through R-8).  A bank of value effect delta at a design-depth near
coordinate needs mass delta Design(L) (efficiency mu_s^2|u_k(s)|/nu >= 1/Design only), i.e. up to Design^C b for own pushes and Design^C b/u^2
for threshold raisers.  The new support coordinate is S_th with modulus outside K2-ref K-3's range [theta_0, 2b] (and outside the tiny class
<= b of K2.13 at that coordinate).  K2.16's estimates tolerate it: (1) and (6) need D(L)|kappa| max|a_s| << c_*, (2c) and (3) need
D(L)|kappa| max|a_s| << c_1/H(L); both hold for |a_s| <= Design^C b/u^2 (b << u^3/Design^C).  So: harmless, but K-3's range must read
[theta_0, Design^C b/u^2] when (WP)/Pi_0 contains banks.  The bypass with Pi_0 = {} avoids the issue (only (P) creates S_th moduli, = theta_0).
Threshold crossing during a raise: the weak peaks leave P during a finite threshold raise, so d theta changes piecewise (Phi_P^2 drops by
Phi_k^2); theta is continuous and increasing in the raised value, so the intermediate value theorem gives the needed raise; first-order sizes
hold on each piece up to constants.  No Sherman-Morrison denominator arises because no (P4)/(P5) (common-mode) column is used.  PROVED.
The remark "K2-ref E's size bound must be read in ratio units for threshold raisers" is CORRECT (theta <= Design/u, so value units carry 1/u^2).

## 3.3 Lemma J2.5.  Verdict: CORRECT.
(a) Delta'_m < 0: e_k >= 0 > Delta'_m gives eps_k = vs_k at every weak peak (no zero-data weak peak exists), and eps_p = vs_p at robust peaks; a
robust peak's bank raises |u_p| (threshold raiser).  A robust peak without bank/raise and without (P3) has all near coordinates thick with tiny
spreads (if it had an off-F or thin near coordinate it would be (U)/(M) and HAVE the bank): type (S).  Weak peaks need a pull or (P3).  (b) Delta'_m
> 0: robust peaks eps_p = -vs_p (pull raises, bank lowers theta); weak peak with e_k < Delta'_m: eps_k = -vs_k (bank pushes), e_k > Delta'_m: pull
pushes, e_k = Delta'_m: zero data, (P1).  (c) a carrier without the needed (P1)-(P3) or bank/pull is (S), (U) or (M) (K1-ref R-10; a (P2) carrier
has a two-sided TU lever and so never fails).  PROVED.

## 3.4 Remark J2.6.  Verdict: core CORRECT; last sentence interpretive.
Orientation vs_l eps_l: with rt_l = eps_l r''_l (Sys-A targets are val-ratios, val_l = eps_l u_l) and S_th coordinates of data sign sigma_l =
eps_l (v > 0 on S_l, K2-ref K-2), K2.17(g)'s sign rt_l eps_l sigma_l = vs_l eps_l -- the identification is right.  The coupling row (X3)/kappa:
sum_l |r_l| |gamma_l| vs_l eps_l = Delta'_m (exact on the class cone), so Delta'_m < 0 forces an active carrier of orientation -1, while every
active weak peak has orientation sgn(e_k - Delta'_m) = +1.  Hence two kind-(iv) carriers of opposite orientation violate K2.17(g)'s one-sign
condition.  PROVED.  The final sentence (the kappa lever must satisfy |r_k|/|r''_k| <= kappa'/kappa <= |r_l|/|r''_l|) is the one-dimensional
caricature in which only kappa and one-sided values move; as a statement about Step A it is HEURISTIC (J1 Lemma J1.2 is the precise form).

## 3.5 Step-0 Farkas certificates (3.3).  Verdict: SKETCH label honest; the identity part PROVED.
Re-derived: sum_k y_k d log rho_k = l_delta(Psi^0_y) with c_j = vs_j[y_j/|u_j(xhat)| 1_W - Y_m (d theta_m/d|zeta_j|) lambda_j/theta_m], and
Psi^0_y(xhat) = sum_W y_k - sum_m Y_m theta_m^{-1} sum_j (d theta_m/d|zeta_j|)|zeta_j| = 0 by the 1-homogeneity of theta (Lemma J2.0).  The transfer
of K2.16's structure (signed dichotomy, common mode) is not written out: SKETCH.  The conclusion "a direct proof of (H1*) at every row is as
hard as Step A" is a HEURISTIC comparison, not a theorem (it is not needed).

## 3.6 Combination with J1 (J2 Section 7).  Verdict: correct as a COMPOSITION; conditional on J1 (unrefereed in this round by me).
7.1: J1's setting (J1 1) is already the unpushed row with (FC): "Input row of Step A: R_1 = f_1 + Pi (after the deep raise, (C1), (C2), the
preparation (P) and the pre-placements)" -- no (WP).  The transfer statement is consistent.
7.2: The disjunction is logically sound given its parts: (i) "no near-certificate of size <= eps_*" implies A-regularity by the contrapositive
of K2.9(b) (needs 4 u^3 Design^{-C_A} <= eps_*, i.e. C_A >= C + 1, as in K2-ref K-7); (ii) K2.17(a), (b) give positive spanning, (f) A-regularity
for the given right-hand side; (iii) J1's (J-a)-(J-f) are J1's Theorem J1.15, which realizes Step A in some cases only with BANDS (J1.8, J1.9,
J1.13) -- this is NOT A-regularity in the sense of (H2^flat), so the combination also needs that Theorem J2.1's Steps (iii)-(iv) accept a
band-realized companion: (FC)-consistency (J1.13's status list (T) <= 1 - mu/2, (U) <= 1 - eta'/2, (KN) U1-ref margins) and exactness of the
PINNED ratios on Z_kappa (J1.13), with the data projected at the realized ratios.  These are J1's claims (J1.13-J1.15, once-written).  If they
hold, J2.1's consistency argument applies verbatim (frozen = true at any consistent point).  So the label should read "PROVED modulo the K2.15
chain AND conditional on J1's Theorem J1.15 / Lemmas J1.13-J1.14 (not refereed here)"; J2 says essentially this.
7.3 (residual): CORRECT as a necessary condition for non-coverage, conditional on J1.

## 3.7 Numerics (sanity; r12/J2_ref_work/)
 ref_K8_literal.py/.out: one (U)-block per trial (robust peak, active weak peak, two active non-peaks, an inactive non-peak, fine carriers;
 eta' in [1e-3, 1e-2], b = eta' x [1e-4, 1e-2]); realization of the rescaled ratio targets s_m r_0 from the UNPUSHED row with kappa floating.
 (FC) (weak peak frozen as non-peak): the realized point is consistent in 60/60 trials (former weak peak true status <= 0.9952) and the TRUE
 ratios equal the targets to 8e-40.  Literal K-8 (weak peak frozen as a peak): true ratios miss the targets by 1.1e-4 .. 4.4e-3 relatively,
 i.e. 5..30 times eta' Phi_k^2: exactness on Z_kappa fails.  [A first run with b comparable to eta' (violating b << eta') produced inconsistent
 (FC) points in 1/60 trials, as expected: consistency at the solution needs the margins the targets provide, b << mu <= Lip eta'.]
 This confirms the precision (FC) numerically.
