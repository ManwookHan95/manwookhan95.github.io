# J2-ref part 2: the precision (FC) to K2-ref K-8, Theorem J2.1, Corollaries J2.2 and J2.3

## 2.1 (FC) = K-8 with the TARGET pattern.  Verdict: CORRECT (needed for K2.15 itself); one sub-claim needs a qualifier.
What K-8 needs.  K2.9(c)'s Brouwer argument needs ||Rem(t)|| <= C_2||t||^2 (+ C Design c_{L+1}||t||) on K = {t >= 0, ||t|| <= W}, W >> b; the true
kappa has derivative jumps of order 1 at threshold crossings (K2-ref ref_kappa_jump; J2's frozen_check2 (B): 0.95).  A frozen system is
smooth, but its scalars are the TRUE ones at the realized point only if the frozen pattern is consistent there (Lemma J2.1(c)); otherwise the
realized ratios are not the true ratios, and exactness on Z_kappa (tiny minors EXACTLY 0, KN-1) is lost.
Why literal K-8 fails.  "Coarse peak set frozen at f_1 + Pi" freezes as PEAKS the active weak peaks of (U)-blocks: Step 0 pushes only in
(T)-blocks (X1 2.6, X1-ref 8), and a (U)-block's active carriers reach rho <= 1 - eta' only through the rescaled targets s_m r'' (X1 2.1(U),
X1-ref D1), i.e. INSIDE the realization.  At the realized point such a carrier satisfies nu_k < theta_f while frozen as a peak: the frozen A_f
contains the negative term |zeta_k| - theta_f Phi_k^2 and B_f the term theta_f^2 Phi_k^2 instead of nu_k^2 Phi_k^2, so (A_f, theta_f) != (A, theta)
and the realized TRUE ratios differ from r'' by O(eta' Phi_k^2) relatively -- exactness on Z_kappa fails.  The same holds for D2-pushed inactive
weak peaks whenever the D2 pushes are realized as Sys-A targets ("pushed ratios for D-pushes", K2 1).  QUALIFIER: for (KN)-blocks the claim
depends on bookkeeping: if the lever push of d_0 is a one-shot pre-move (cert0 3.2: "one-shot moves first: ... (KN)-lever pushes ..., D2
pushes"), it raises theta by >= C' D eta' theta before the fixed point (U1-ref Prop. KN proof), and the active weak peaks of the (KN)-block are
already strict non-peaks at f_1 + Pi, so literal K-8 is consistent there.  The (U)-block case alone makes (FC) necessary.
(FC) is consistent at the companion: Q1 CM^tr(b) / X1-ref 8: every coarse carrier of f^(1a) is a robust peak (exactly P_rob) or a strict
non-peak; route V's Omega is all coarse strict non-peaks.  PROVED.

## 2.2 Theorem J2.1.  Verdict: CORRECT (PROVED modulo the chain cited by K2.15), with precisions P-1..P-6 below.
I re-checked each step.
Step (i) (Lojasiewicz start).  At f^0 every block satisfies Lemma J2.1(e) with P_f = P_rob (nonempty: V1 Lemma D), W' = the remaining coarse
peaks (rho in [1, 1 + b']), side conditions from Phi_min(L)^2 >= 1/Design(L), a >= u Phi_p^2 (alpha-mass identity) and b' << u/Design^2.  F(r_0) =
max_{N_T} m|r_{0,d}| K(sigma_rob, R_a(r_0)^2)/Phi_d <= max_{N_T} rho^f_d(f^0) because sigma_f >= sigma_rob, R^2 >= R_a^2 and K increases in both
arguments (frozen Lemma F); rho^f_d <= rho_d(1 + 6x).  W-fix region: 1 - R^2 >= sigma_f/k_f >= sigma_rob/2.  Numerically confirmed (part 1).
This is exactly cert0's "C3 alternative" made rigorous with frozen scalars.  CORRECT.
Step (ii) (realization).  K2.9(c) uses only: first-order generator actions (K2.4; chain rule for kappa_f), a C^{1,1} remainder, Brouwer on K,
and continuity of the minimal-norm nonnegative selection.  The (FC) map is C^infinity in the coarse variables on K (P_rob values robust, Q_f
terms polynomial), the fine kinks contribute <= C Design c_{L+1}||t|| (part 1, P-1), Psi_f(0+) stays robustly positive on K (moves <= W << u).
No true status is used.  CORRECT.
Step (iii) (consistency => truth).  (T)-blocks: R^2 = R_a(r'')^2 exactly (route V: (T)-blocks have no inactive robust non-peaks or inactive
weak peaks; nearly neutral ones held at exactly 0, P-HOLD), sigma_f in [sigma_rob, sigma_rob + C sum_fine Phi^2], so rho^f_d <= F(r'')(1 +
C D^C c_{L+1}^2) <= 1 - mu/2 for every active near-threshold d, former weak peaks included; (U)-blocks: rescaling s_m (Lemma K is monotone in
|r| and R^2); D2/KN-pushed inactive near-threshold carriers: <= 1 - c eta'; (KN)-blocks: the lever raises theta_f (frozen Lemma J2.0: lowering a
frozen non-peak raises theta_f; d kappa_f/d|zeta_{d_0}| tiny by J2.1(d)); robust objects keep their classes (moves << u).  So (FC) is consistent
in every block, J2.1(c) applies, and the frozen solution is the true companion with exact true ratios r'' on Z_kappa.  CORRECT, subject to P-5.
Step (iv) (rest).  Classes (read at f^r), (P), data (K1.A), Sys-DC (K2.6), UE^inf, E^{eng,RT,inf}: none refers to the pushed row; see P-6 for
the one omitted reference.  Costs: Pi_0 <= C_f Design^C b log(1/b)/u^2 = o(u^2 T^2); Step A as in K2 6.5.  CORRECT.
PRECISIONS (none changes a conclusion):
 P-1 (fine kinks).  The kink part of the frozen map is Lipschitz with constant C Design c_{L+1} (not C sum_fine Phi^2); K2.9(c) needs
     C Design c_{L+1} W <= rho_0/2, true (W >= Design eta' >> c_{L+1}).
 P-2 (size of b' when Pi_0 != {}).  Step (i) states that (C1), (C2), (P), Pi_0 shift relative positions by <= C Design(L) b.  With Pi_0 of size
     Design^C b/u (in particular (P4)-type pre-pushes with common modes) the shift is Design^C b/u; then b' := Design^C b/u, the side conditions
     of J2.1(e) still hold (b << u^3/Design^C), and F(r_0) <= 1 + Design^C b/u, tiny minors <= Design^C b/u: still inside R-8(ii)'s radius.
     The bound "F(r_0) <= 1 + Design(L)^2 b" is correct for Pi_0 = {} only.
 P-3 ((D2) must carry the enlargement).  Step 2 of KN^tr needs F(r') - 1 <= delta_0 with delta_0 satisfying (D2).  With the start r_0, F(r_0) - 1 is
     up to Design^C b (Pi_0 = {}) resp. Design^C b/u, and the Lojasiewicz displacement is C_L((1 + Lip C_*)Design^C b/u)^{2/N_L}; so (D2) must be
     imposed with delta_0 evaluated at Design^C b/u, not only (D1).  K1-ref R-8(ii) enlarged only (D1); K2's (K2-e) states the factor for (D1) AND
     (D2) -- that reading is required and suffices (same monotonicity argument: u(w) fixed before b(w), left sides increasing in b).
 P-4 ((H2^flat) targets).  The Lojasiewicz/Puiseux output is not unique.  Define (H2^flat) with ANY targets r'' in Z_kappa satisfying |r'' - r_0|
     <= 2 eta', F(r'') <= 1 - (3/4) mu_kappa(eta'/3), robust minors >= u/2 (the properties Steps 1-3 deliver; cert0 C1).  Every later use of eta'
     (statuses, (X4^0) data violation, shift-trick cost, Lip bounds) tolerates 2 eta'.  This makes Corollary J2.2 literal (P-4' below).
 P-5 (blocks without tuned carriers).  Step (iii) claims consistency "in every block".  In a block with no active carrier whose coarse weak peaks
     are not pushed, (FC) would be inconsistent; such blocks need the D2 push of ALL their inactive near-threshold carriers (X1-ref D2, J1.14:
     "(U)-blocks, including blocks with no active carrier") -- or, equivalently, the block scalars of blocks without Sys-A rows may be left
     unfrozen (they enter no row of Sys-A).  Either reading closes the point; the companion needs the D2 pushes anyway (CM^tr(b)).
 P-6 (audit completeness).  The audit (J2 1.4) omits one use of the start row: the (X4^0) data violation and the kind-[3] shift-trick cost
     (X1-ref 3.2, cert0 3.5) use |r'' - r_1| <= eta' and |rho^0(r'') - rho(f)| <= C D^C b + Lip eta'.  With r_0: |r'' - r_0| <= eta' (2 eta' under P-4),
     |r_0 - r(f)| <= Design^C b/u, same bounds up to constants.  No other use found (I checked K1 4.1 Steps 1-7, K1-ref R-6/R-8, K2 4.1, 6.3-6.5,
     cert0 3.1-3.6, X1-ref 3.2-3.3, 8, S-0).

## 2.3 Corollary J2.2.  Verdict: CORRECT after P-4 and with the reading of K2.15 corrected by (FC).
With Pi_0 := the (WP) moves of (H1*), f^0 = K2's f_1 after (P).  (T)-blocks: (FC) = literal K-8 (after (WP) the coarse peaks of a (T)-block are
exactly P_rob; (T)-blocks have no inactive weak peaks).  (U)-, (KN)-blocks: (FC) differs from literal K-8, and literal K-8 is defective there
(2.1), so (H2) must be read with (FC) -- a correction of K2.15, not of J2.  P-4': K2's Lojasiewicz start r_1 (formula-1 ratios at f_1) and J2's r_0
(frozen ratios at f_1) agree in (T)-blocks and differ by <= C Design b in (U)-/(KN)-blocks (Lemma J2.1(e) applied there); targets admissible for
(H2) (|r'' - r_1| <= eta') satisfy |r'' - r_0| <= eta' + C Design b <= 2 eta', so they are admissible for (H2^flat) in the sense of P-4.  PROVED.

## 2.4 Corollary J2.3.  Verdict: CORRECT.
If (H2^flat) fails at a stage, it fails in particular for Pi_0 = {}, and K2.9(b) (one-directional) gives a near-certificate y of size < 4
Design^{-C_A} with phi_y > -rho_0 for the (FC)-frozen Sys-A at f^0 + Pi.  K2.16's proof uses: (2.1) at the row (any row), K2.4 (any row), K2.8(b)
(chain rule, valid for kappa_f), the Euler share Xt_m <= 1/4 (for kappa_f: d kappa_f/d|zeta_l| = rho^f_l s_f/(Phi'^2(1 + a_f)) with s_f from fine
non-peaks only, since Omega = all coarse non-P_rob carriers; |Xt_m| <= C |Lambda| Design c_{L+1}^2 -- better than U1's regime), d kappa_f/d zeta(c)
>= 3/4 at peaks (K2.17(g)), and the kinds (i)-(iv) after (P).  A weak peak without any push resource has no (P1) (zero-data weak peaks have (P1)),
no (P3) (kind (ii)), so it is of kind (iii) or (iv).  Hence: not covered by Theorem J2.1 => at all large stages a near-certificate with K2.16's
structure at the UNPUSHED row.  The class (W)/(W*) is no longer a separate obstruction.  Moreover the new residual is contained in the old one
(Corollary J2.2).  The sentence on J1 (J1.1-J1.5 valid at f^0 + Pi) is consistent with J1's own setting (J1 1: R_1 is the unpushed row with (FC));
their correctness is the subject of J1's referee.  PROVED (the J1 sentence: conditional on J1).
