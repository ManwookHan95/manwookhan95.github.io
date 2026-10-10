# U2 referee, part 3: Lemma DR-inf, Lemma TR-inf, the residual (NDN), Theorem M-inf, (E3), (E4)(ii)

## 3.1 Lemma DR-inf.  VERDICT: correct (PROVED) for (R1)-(R5), (R7) and V2's minors; (R6) is in fact EXACTLY invariant
## (upgrade from SKETCH to PROVED, my remark (D1)); one omission (D2) (V2's shift-pinning rate rho^sh), one fix (G1).
Re-derived: the raise changes neither z nor F (nor K, J, rooms), so (R1), (R2) are unchanged; ||e^r - e|| <= 2||U^*Delta a||/nu <=
C mu*_J psi(J) (V3 Lemma 2.1(b)); |u_k(zhat^r) - u_k(zhat)| <= ||U^*u_k|| ||e^r - e||; block scalars move by C_f eps_e (V3 Lemma 2.2).
(R3)/(R4): rho = |u(zhat)| m/(Phi theta): absolute change <= C m b^2 Phi_min/(Phi theta) + rho |Delta theta|/theta, i.e. tiny stays
<= 2b and robust stays >= u/2 (relative perturbation for large rho).  (R5): change <= C b^2 Phi_min/Phi_max <= C b^2.  (R7): Weyl.
Minors (V2 Def. 2.1): multi-affine in values with Lipschitz constant Lip(l) <= Design(l): change <= Lip C b^2 <= b; compatible with
V2 Theorem B's hypothesis (A1) (absorb the raise's value motion into C_*(l) b(w)).
(D1) (R6) is invariant, not merely continuous.  V1 2.5: c(delta; pi) = inf_{x >= 0} sum_{j notin F} phi_{z_j}(sum_m delta_m Pi_m(j) +
   sum x eps u(j)), Pi_m = sum_{P*} vs lambda u 1_{F^c}: for a FIXED shift pattern pi it depends only on F, z|_{F^c} and design vectors.
   The deep raise changes neither F nor z, so c_pi(f^r) = c_pi(f) for every pi.  With the pattern pi(w) taken from the classification
   of f (as V1's assembly does), (SH_w) at f^r is literally (SH_w) at f.  So U2's flagged item "(R6) continuity" is RESOLVED.
(D2) Omission.  V2's shift-pinning rate rho^sh(kappa, f) (Def. 3.2; the object that, together with c_pi, defines (C*)) is not
   (R6) and is not covered by the Lipschitz argument as stated: it is an infimum over unbounded tau of a piecewise-linear
   violation with value-dependent coefficients (q_l = val_l/A_m in (R4), |w(k)|/M in (R7)).  With V2's convention (q' := 0 for
   nearly neutral carriers; all other coefficients robust, >= c u Phi_min/Design at a clean w) the minimizers can be taken
   bounded by (Design/u)^C (Hoffman), so rho^sh moves by <= (Design/u)^C b^2 <= b under the raise: SKETCH (plausible, routine).
   Since Theorem M-inf reads (C*) AT f^r, the residual statement is unaffected; what needs rho^sh-continuity is only the claim
   "w clean for f => w clean (factor 2) for f^r" used for case (I) of V2's Theorem C1.
(G1) GAP + FIX (raise depth versus tuning depth).  DR-inf only requires C mu*_J psi(J) <= b^2 Phi_min, which gives 2^J ~ log log(1/b),
   far below the tuning depth d(l) = sigma(l) + 2^{l+2} of Lemma TR-inf.  Coordinates s in F ∩ [J, d(l)] are then RAISED to
   4Bx_*(s)/lambda, a number that is a design quantity times the box level of the kept carriers and need NOT be tiny or robust
   (c_{l''} for coarse l'' is >> b(w)); but TR-inf's case analysis ((a') tiny, (c)/(c') robust) uses exactly the moduli |a_s|,
   s <= d(l), as rate objects of f.  FIX: take J >= d(l) + 1 (and J > s_max(l)).  Then no coordinate <= d(l) is raised, the moduli
   at f^r are those of f divided by lambda in [1, 1 + o(1)], and the pinning constant 2^J/delta_min of Lemma P becomes
   max(2^{J°}, 2^{d(l)+1})/delta_min: a design factor (Design(l) >= 2^{d(l)} once B_mu*(l) is defined with d(l), part 1 (s1)) times
   O(log log(1/b(w))), absorbed by Q(w).  The footprint condition is only easier for larger J.

## 3.2 Lemma TR-inf.  VERDICT: correct (PROVED) in cases (a), (a'), (c), (c'), with precisions (T1)-(T3); numerics confirm.
(a) = V1 Lemma TU: its proof uses finiteness of supp A^2 nowhere except to place j, j' off the support (Lemma B (3.1) holds for any
    A^0 in l_1 with J ∩ supp A^0 = {}); Z3 Lemma 3.1 is F-free.  OK at infinite F.
(a') Lowering a support coordinate of modulus <= b (bank coordinate) or <= theta b^{1/2}/|L_0| (pull coordinate) to a contact costs
    2|a_j| in the transfer error (V3 2.3 Remark) and moves e by <= 2 mu_j |a_j|/nu; afterwards Lemma B applies.  With the opposite
    sign the coordinate becomes a temporary contact of sign -eps, but the subsequent bank/pull mass makes it a SUPPORT coordinate of f^#,
    so exact swallowing off F^# is not broken.  OK.  Remark: after the deep raise every raised PULL coordinate (depth ~ log(1/eta) >> J)
    has |a^r_j| = 4Bx_*(j)/lambda <= 4 lambda_{l''} v(j) <~ eta <= Design b << theta b^{1/2}: raised pull coordinates are always
    convertible; the deep raise never obstructs (a').
(c) First-order formula re-derived: d val_k/d a_s = (mu_s^2/nu)(u_k(s) - gamma_k a_s/nu^2) (e = U^*A/||U^*A||, z fixed); pair rule
    alpha_s Delta + alpha_{s'} Delta' = 0 kills the common term; private effect (mu_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta';
    |Delta| <= u^{-1}|Delta'| because mu* decreases (the order s < s' matters, as U2 says).
(T1) Correction of a scale in U2's heuristics (the conclusion stands): the e-vector moves by ~ eta/(mu_{s'} v(s')) (not ~ eta/v), the
    second-order COMMON term is ~ (mu_{s'}Delta'/nu)^2 ~ eta^2/(mu_{s'}^2 v(s')^2) <= Design^2 eta^2 (Design >= (mu*_{d})^{-2} 2^{d}/delta,
    1/v <= Design), so U2's bound O(Design^2 u^{-4} eta^2) is right; it is << b because Design^4 b << 1.  Numerics (my script
    r8/U2_ref_work/tr_inf_joint3.py, 600 digits, diagonal base 2^{-(s+2)^1.6}, every coordinate in F, three tuned carriers, Newton on
    the reduced unknowns): exact tuning to residual/eta <= 1e-164; untuned clean carriers move by eta^2 x (1e63..1e66) ~ eta^2/(mu^2 v^2)
    (second order, as above); Jacobian off-diagonal/diagonal -> 0 like eta/eff (1e-1, 1e-5, 1e-13 for eta/eff = 1e-4, 1e-8, 1e-12).
(c') Anchor: re-derived; numerics: anchor-met carriers move FIRST order, ~ 1e4 eta ~ eta u(s_0)/v(s') (<= C_T eta with C_T ∋ Design),
    untuned carriers second order; tuning exact.
(T2) Precision (design): the constant Design(L) >= (mu*_{d(L)})^{-2} 2^{d(L)}/delta_min(L) must be part of T_final^* (part 1 (s1)); the
    stated B_mu*(l) with sigma(l) is insufficient for the coordinates in (sigma(l), d(l)].
(T3) Precision (anchor side effects): anchor-met coarse carriers outside L_0 move at FIRST order by <= C_T eta.  This is harmless
    because every carrier occurring in a tiny object belongs to L_0 (definition of L_0 / V2's tuning set), so the others are either
    robust (Lemma RR: moves << u) or nearly neutral non-exact (rho stays <= C Design^C u^{-C} b << u), and C_T eta << Lam = T_lo^3 keeps
    V1's threshold buffer (Lemma ST).  I checked these three uses; U2 states only "robust".
Joint solution: with private first-order Jacobian (diagonal up to O(eta/eff)) the quantitative inverse function theorem gives the exact
solution for all carriers at once (contraction constant <= C Design^C u^{-C} eta); combined with the explicit scalar fixed point of
Lemma TU for (a)/(a') carriers, the same Newton/Graves argument applies.  PROVED.

## 3.3 The residual (NDN).  VERDICT: correctly located, but the "iff" characterization is too narrow (N-fix); OPEN as stated.
(N-fix) The negation of "(a) or (a') or (c) or (c')" for a carrier is NOT (N1) & (N2): e.g. a carrier whose bank coordinate j' is a
   thick support coordinate but which has off-F pull coordinates fails (a), (a') while (N1) fails.  Such a carrier has only a ONE-SIDED
   private resource (pulls lower eps.val) plus single support moves at its robust coordinates (two-sided, with common term).  U2 itself
   uses single support moves (the Sherman-Morrison case).  The exact residual of the tuning is: the combined first-order resource map
   (private columns of (a), (a'), (c), (c'); one-sided pull columns; single-support columns (mu_s^2/nu)(e_{l''} - rho_s gamma/nu^2)) has
   no right inverse onto R^{L_0}, within the sign constraints, with constant <= Design^C/u.  This is a finite family of determinantal /
   Robinson-regularity quantities in (a_s)_{s <= d(l)} and values: rate objects; robust => tuning; tiny => residual.  (NDN_w) of U2 is
   the special case "only single support columns" (Sherman-Morrison determinant 1 - sum rho gamma/nu^2 tiny).
   Numerics (sm_check.py): det of the single-move Jacobian = det(D)(1 - sum rho_k gamma_k/nu^2) to 8 digits; for a|_F = sum c_k u_k|_F the
   denominator vanishes; the kernel drift identity sum c_k Delta val_k = -kappa nu ||e' - e||^2/2 holds EXACTLY (12 digits), as
   <U^*(sum c u), e> = kappa nu <e, e'> for every move on F (diagonal base).
Remark (agree with U2): for FIXED carriers (NDN) is an f-constant phenomenon except in the exactly proportional case; the rate character
comes from carriers entering L_0 at growing levels.  OPEN.

## 3.4 Theorem M-inf.  VERDICT: SKETCH as labelled; plausible; flagged items partly resolved, two more gaps added.
Resolved here: (R6) continuity (exact invariance, (D1)).  Plausible/checked: Lemma ST with anchor side effects ((T3));
window arithmetic: thresholds (4H l + 3)^{l+2} with H = C_f^l Design^2/u (V2 Theorem B(d)) are <= C_f^{l(l+2)} (Design^2 l/u)^{l+2},
dominated by Q(w) = (4 Design/u)^{omega+20} (omega >= 3l) and 2^{l^3}; 2^J = O(log n(w)) (or 2^{d(l)+1} after (G1)) absorbed.
Shallow thin target coordinates: at a clean w the moduli |a_j|, j <= d(l), are tiny (<= b <= theta_1 t^2 for t >= T_lo) or robust
(>= u >= K_top t^2 for t <= T_hi(w)): condition (S1) of Lemma W is AUTOMATIC at clean sub-windows (no second pigeonhole).
New gaps:
(G1) (part 3.1) raise depth J must exceed d(l): fixed.
(G2) Which row the decompositions live at.  U2's route mixes V1's transplant (Prop. TR: decompositions of g at f, data at f^#; its proof
   uses lem:finitebase (F finite) for t||b^+-||_1 <= A_0 and copies B_+ 1_F into b^+) with Lemma W (decompositions at the companion).
   At infinite F, Prop. TR must be re-run with R1's CLAMPED base data (Claim 3.1: b^+_1 per coordinate, |b^+_1| <= A_j + |X_j|) and with
   Lemma P applied AT THE DECOMPOSITION ROW (Lemma P holds at any row, part 1 (p2)); the cushions at f^# dominate those at the
   decomposition row on deep coordinates (raised) and equal them up to lambda on shallow ones (J > d(l)), except at tuned robust
   coordinates (cushion >= u/2 >> t|X|) and at pulls/banks (V1 Prop. TR(iv)).  This is routine but not written.
(G3) (NDN) must be replaced by the determinantal residual of 3.3 (otherwise the exclusion list of M-inf is incomplete).
(D2) rho^sh under the deep raise (needed for "clean for f => clean for f^r").
So M-inf: SKETCH, with an explicit list of four inspection items ((G2), (D2), V2 Theorem B with Lemma W's pinned faces -- faces of the
exact cones are subsystems whose minors V2 lists, fine --, the joint fixed point of 3.2) and the corrected residual (G3).

## 3.5 (E3).  VERDICT: (a) correct as a structural statement for RS*, RS*_inf (PROVED) and conditional on M-inf for the transport;
## (b) PROVED; (c) SKETCH as labelled.
(a) In RS*/RS*_inf the data are built from decompositions AT the companion and are d-neutral because the cone contains the d-rows
    (R1 Claim 3.2(a)); Y3 Theorem 2.1 with I_- = {}.  For M-inf the data are d-neutral at f^# by the exact d-repair at f^# (V1 Prop. TR
    Step 3 / V2 Cor. B.1), outside (C*).  Correct.
(b) D = Delta' - Delta in Y (R_m^* W in Y), Y ∩ c_00 = {0}, L^* injective on bounded block families: correct.  (Also D = O(|Delta d| eps_e).)
(c) (SC) (def:SC) is defined through the block data (peak margins, gaps, Phi) only; "independent of F" is right in that sense.  But (SC) at
    f does NOT transfer to f^r by "an O(eps_e) perturbation": Scr_m(s) as s -> 0 at the FIXED row f^r involves margins and gaps below
    eps_e, which the perturbation can change for infinitely many fine coordinates.  Only Scr^{f^r}(Upsilon s) <= Scr^f(2 Upsilon s) for
    s >= C eps_e holds.  So the reduction "(E3) inside (C*) = (C*-2)" is right as a classification, but the transfer of (SC) along the deep
    raise is itself unproved; U2 labels the last sentence SKETCH: agree, and the gap is this one.

## 3.6 (E4)(ii).  VERDICT: SKETCH as labelled; the "not admissible" claim for a single unpaired support raise is correct (PROVED).
Re-derived: a donor raise of size Lam/lambda_c at a robust support coordinate s needs Delta = Lam nu/(lambda_c mu_s^2 v_c(s)) and moves
every other value by gamma_k rho_s Lam/(nu^2 lambda_c) (rho_s = a_s/v_c(s)), which is >> b(w) = T_lo^4/(l Design) since Lam = T_lo^3.  With a
pair (c) or anchor (c') the common term cancels and the second-order motion is ~ (Lam/lambda_c)^2 Design^2 <= T_lo^6 Design^4 << b.
Degenerate swallowing-sign bad peaks are (K4) carriers at clean w (rho = 1, class G), or dropped (P-iv) in one-signed blocks: the reduction
to V1's donor raise is correct, conditional on M-inf.  OPEN when every donor of the block lacks a resource (now: when the donor's
determinantal resource object of 3.3 is tiny).
