# J2 part 1 (Round 12): Step 0 of KN^tr and the joint push problem (H1*) -- precise formulation, role in the chain, sign precision

Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "PROVED" = proved here modulo the refereed chain cited (X1/X1-ref, X2/X2-ref,
Q1/Q1-ref a,b/cert0-3, Q2/Q2-ref a, K1/K1-ref, K2/K2-ref; several links once-refereed, as recorded there).

## 1.0 Setting and notation
Design T_fin^{K2} (K2 6.1: Q1's T_fin over the diagonal base U k_s = mu*_s e_s, mu*_s = 2^{-2^{2^s}}, option (a), with K1's (D-K1), K1-ref R-6,
R-8(ii) and K2's (K2-a)-(K2-e)).  N >= 1, f in S_{p_N*} with forced data f = a + L^*w, F = supp a arbitrary, g in C(f), rho in (0,1).  Main
stage L >= l_f, clean sub-window w, b := b(w), u := u(w), T := T_lo(w), eta' := T^4/(L Design(L)), D := D(L) (K2 1).  Row after the deep raise:
f^r (K1 1.2).  Block m of a row: zeta = zeta_m = (lambda_k u_k(xhat))_k, lambda_k = m Phi_k (Phi_k := Phi_m(k)), A = |zeta|_m, w_m its norming
functional, M = ||w_m||_inf, C = ||D_m w_m||_2, M + C = 1, theta = AM/C, nu_k = |zeta_k|/Phi_k^2, rho_k = nu_k/theta (relative position),
P = {rho >= 1} (peaks), Q = {rho < 1}; vs_k := sgn u_k(xhat) (value sign), val_k := eps_k u_k(xhat) with eps_k the data sign of k (below).
Threshold equation (Y2 Lemma T, refereed): with A(th) := sum_k (|zeta_k| - th Phi_k^2)_+ and B(th) := sum_k Phi_k^2 min(th, nu_k)^2, theta is
the unique zero of Psi(th) := A(th)^2 - B(th); A = A(theta), A^2 = B(theta); Psi > 0 left of the zero, < 0 right of it.
Pattern Omega (U1, X1-ref K1): the switching set of the class, containing the active near-threshold carriers N(m) of every active block,
in particular the ACTIVE WEAK PEAKS W(m) := {k in N(m) : rho_k(f^r) in [1, 1 + b]}.  Formula-1 block scalar (X1-ref K1):
      kappa_m(Omega) := A + (A^2 - S_Omega)/theta,   S_Omega := sum_{l in Omega_m} nu_l^2 Phi_l^2 = m^2 sum_{l in Omega_m} u_l(xhat)^2,
ratios r_l := u_l(xhat)/kappa_{m(l)}(Omega).  Block kinds (X1 2.1): (U) unshifted, (KN), (T).

## 1.1 What Step 0 does (X1 2.6, X1-ref 8, Q1 2.2, K1-ref R-8, K2-ref E)
Step 0 of Proposition KN^tr consists of
 (C1), (C2)  V1's closing of tiny rooms of class-G signature sets and of tiny target rooms: z-moves OFF F of size <= b (always available:
             the coordinates are free; values move by <= b);
 (WP)        in every (T)-block, every active weak peak k in W(m) is pushed inward to rho_k = 1 - b (value change <= 2 b theta Phi_k/m).
After Step 0 come the classes, the preparation (P) (K2 4.1), the Lojasiewicz/Puiseux steps 1-3 (targets r'' on Z_kappa with
|r'' - r_1| <= eta', F(r'') <= 1 - mu_kappa(eta'/3), mu := mu_kappa(eta'/3) in [8Mb, Lip eta'] by (D2) and QC Q1), and Step A = KN^tr Step 4
(realization of the targets; K2 5.2: Lemma K2.9(c) under A-regularity, with K2-ref's frozen-status precision K-8).
Only (WP) can fail: it needs a resource lowering vs_k val_k (more precisely lowering rho_k) for every k in W, jointly.

## 1.2 (H1*) as a cone/inequality problem
(H1*) (K2-ref E): admissible push moves (far pulls at depth in [2 b theta Phi/m, x'_max], near banks, (P3), (P4), design-depth moves of K2.4
admissible for their data) of total size <= Design(L)^C b/u after which rho_k <= 1 - b for every k in W := union of the W(m) over (T)-blocks.
First-order action on relative positions.  LEMMA J2.0 (PROVED).  In one block, for value changes d|zeta_j| (all j):
      d theta = [ A sum_{j in P} d|zeta_j| - sum_{j in Q} nu_j d|zeta_j| ] / ( Phi'^2 (A + theta) ),      Phi'^2 := sum_{j in P} Phi_j^2,
      d log rho_k = d|zeta_k|/|zeta_k| - d theta/theta     (every k),
(fine carriers included in P, Q by their true statuses; at a degenerate configuration the formula holds on each side).  Moreover theta is
1-homogeneous: sum_j (d theta/d|zeta_j|) |zeta_j| = theta.
Proof.  Implicit differentiation of Psi(theta; zeta) = 0: d Psi/d|zeta_j| = 2A (j in P; the A-term is |zeta_j| - theta Phi_j^2, the B-term
theta^2 Phi_j^2 does not depend on zeta_j) and = -2 nu_j (j in Q; the A-term vanishes, the B-term is zeta_j^2/Phi_j^2); d Psi/d theta =
-2A Phi'^2 - 2 theta Phi'^2 < 0.  Euler: sum_P |zeta_j| = A + theta Phi'^2 (from A = A(theta)) and sum_Q nu_j |zeta_j| = sum_Q nu_j^2 Phi_j^2 =
A^2 - theta^2 Phi'^2 (from A^2 = B(theta)); so the numerator at d|zeta| = |zeta| is A^2 + A theta Phi'^2 - A^2 + theta^2 Phi'^2 = theta Phi'^2
(A + theta).  QED
Consequences.  (a) THRESHOLD RAISERS: raising a peak value or lowering a strict non-peak value raises theta, hence lowers rho_k for EVERY k of
the block by the common factor; per unit value change of a robust peak p (|zeta_p| = lambda_p |u_p|):  d log rho_k = -(a/(1 + a))
lambda_p/(theta Phi'^2) per unit of |u_p| (a := A/theta = C/M), so pushing all of W(m) from rho <= 1 + b to rho <= 1 - b needs a raise
|d u_p| = 3 b theta Phi'^2 (1 + a)/(a lambda_p).  At a clean sub-window a >= (rho_p - 1) Phi_p^2 >= u Phi_p^2 for a robust peak p (alpha-mass
identity a = sum_P (rho - 1) Phi^2, V1 Lemma D), so |d u_p| <= Design(L)^C b/u^2 in value units, while the induced displacement of the
RATIO vector is a common factor with |d kappa_m|/kappa_m <= 3 b Phi'^2 (1 + a)/(a k) <= 6 b/a <= Design(L)^C b/u (k = kappa/theta >= sigma >=
Phi'^2; d kappa = (1 - O(s_f)) d|zeta_p| at a peak, U1 Lemma 1.4(a)): inside R-8(ii)'s enlarged (D1) radius.
(b) OWN PUSH: lowering |zeta_k| at k in W lowers rho_k: d log rho_k = d|zeta_k| [1/|zeta_k| - a/(theta Phi'^2 (1 + a))] and the bracket is
>= (1/(theta Phi_k^2 rho_k))(1 - a/(1 + a)) > 0 (|zeta_k| = rho_k theta Phi_k^2, Phi_k^2 <= Phi'^2).
So (WP) is a system of |W| linear INEQUALITIES (to first order) in the resource parameters, with one-sided (allowed-direction) generators
and two-sided generators: a cone-feasibility problem; it is A-regular in the sense of K2.9 iff the needed decrease lies in the generated
cone with margin.

## 1.3 Data signs of weak peaks (PRECISION to K1-ref R-8 / K2-ref W-1; PROVED)
R-8 and W-1 state "the peak carries data with sign eps_k = -sgn(Delta''_m) vs_k".  By Part I lem:peakshift, at every peak k of the row,
varsigma_k omega_+(k) <= 0 <= varsigma_k omega_-(k) and e_k := |omega_+(k)| + |omega_-(k)| = varsigma_k (omega_- - omega_+)(k) >= 0, bounded by
t/(sigma |alpha(k)|) when alpha(k) != 0 (for a weak peak alpha(k) is O(b) and e_k is NOT small).  With U1's convention gamma_k = lambda_k
(Domega(k) - Delta_m w(k)), Domega = omega^- - omega^+, Delta' = Delta M, w(k) = M vs_k at peaks:
      vs_k gamma_k = lambda_k (e_k - Delta'_m),   hence   eps_k := sgn gamma_k = vs_k sgn(e_k - Delta'_m).
So eps_k = vs_k whenever Delta'_m < 0 (as in R-8), but for Delta'_m > 0 one has eps_k = -vs_k only if e_k < Delta'_m; if e_k > Delta'_m the
weak peak has eps_k = vs_k (its near banks raise |val|: the "Delta'' < 0 situation") and if e_k = Delta'_m it is zero-data ((P1) two-sided).
Robust peaks (Domega(p) = 0 in the class cone) have eps_p = -sgn(Delta'_m) vs_p.  Strict non-peaks: vs_l gamma_l = lambda_l (vs_l Domega(l) -
Delta'_m rho_l), any sign; in the class, sum_{l in Omega_a(m)} r_l gamma_l = Delta'_m (row (X3)/kappa, U1 Lemma 1.3).
[None of K1-ref's or K2-ref's conclusions depends on this: their push condition lists resources of both orientations.]

## 1.4 Where the PUSHED row f_1 is used downstream (audit; PROVED by inspection of the cited proofs)
Write f^P := the row after the deep raise, (C1), (C2) and the preparation (P), WITHOUT (WP); f_1 := the same with (WP).  The pushed row is used
only at the following places:
 (L1) Lojasiewicz start (X1 2.6 Step 1, X1-ref 8, cert0 3.1): tiny minors <= (1 + Lip C_*) b at r_1 and F(r_1) <= 1 + C_* b.  cert0 3.1 already
      records the alternative "without the move: K1 gives sigma' >= sigma_rob - 3b sum Phi^2, so F(r(f)) <= (1 + b)(1 + C D^C b)" (cert0 C3).
 (L2) Lemma R-kt / Lemma K for the ratio variables: in the formula-1 convention with the pattern's Omega (X1-ref K1) they hold at every row,
      with sigma' := Phi_{P \ Omega}^2 + sum_{Omega ∩ P} (1 - rho^2) Phi^2 + s_f in place of sigma (correction in [-3b Phi^2, 0] per weak peak).
 (L3) Step A's realization (K2 5.1-5.2): K2.8 (Euler share Xt_m small, d kappa/d zeta(l) = rho_l M X/C on Omega) and K2.9(c) (C^{1,1}
      remainder) need block scalars that are smooth along the realization; K2-ref K-8 supplies this by freezing statuses.
 (L4) K2 Lemma K2.13 (clean dichotomy at depth D(L)) lists the (WP) moves among the moves that keep the classification (<= Design^C b/u << u).
 (L5) R-8(ii) enlarges (D1) by Design^C/u to absorb the common modes of (P4)-type pushes.
The classes (read off the decomposition data at f^r, U1-ref 4.5, K1-ref R-3), the preparation (P), the data (Proposition K1.A), Sys-DC
(Theorem K2.6), Theorem UE^inf and E^{eng,RT,inf} do not use (WP): they act at f^r, at f^P, or at the companion after Step A, where every
active near-threshold carrier is a strict non-peak by Step A's targets anyway (X1-ref 8(b), Q1 CM^tr(b)).
Part 2 shows that (L1)-(L3) hold at f^P with the frozen-status convention of K-8 stated with the TARGET pattern, so (WP) is dispensable.
