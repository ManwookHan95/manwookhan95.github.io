# J2 referee notes (Round 12): proofs of the verdicts, precisions and repairs for r12/J2_notes.md

Setting and notation of r12/J2_notes.md and r11/K2_notes.md: design T_fin^{K2} (K2 6.1, with K1's (D-K1), K1-ref R-6, R-8(ii), K2's (K2-a)-(K2-e)),
N >= 1, f in S_{p_N*} with forced data f = a + L^*w, F = supp a arbitrary, g in C(f), rho in (0,1); main stage L >= l_f, clean sub-window w,
b = b(w), u = u(w), T = T_lo(w), eta' = T^4/(L Design(L)), x = C Design(L) eta' (Step-A scale), W = Design^{C_A} u^{-3} max(x, ||b||) (K-7),
rho_0 = C_2 W^2.  Block m: zeta_k = lambda_k u_k(xhat), lambda_k = m Phi_k, threshold equation of Y2 Lemma T (theta = unique zero of Psi(th) =
A(th)^2 - B(th)), nu_k = |zeta_k|/Phi_k^2, rho_k = nu_k/theta.  (FC) = the frozen convention with P_f = P_rob (J2 2.2).  Labels: PROVED /
SKETCH / HEURISTIC / FALSE / OPEN.  Part files: r12/J2_ref_part1.md (Lemmas J2.0, J2.1), part2 ((FC), Theorem J2.1, Corollaries J2.2, J2.3),
part3 (data signs, direct route, J1 combination, K-8 numerics).  Scripts and outputs: r12/J2_ref_work/.  This file supersedes the part files.

## A. Verdict table
| J2 claim (J2 label) | Verdict | Items |
|---|---|---|
| Lemma J2.0 (PROVED) | correct; slip in the explicit lower bound of consequence (b) | B.1 |
| Lemma J2.1 (a)-(e) (PROVED) | correct; constant slip in (b) (fine kinks: C Design c_{L+1}) | B.2 |
| (FC) precision to K2-ref K-8 (PROVED) | correct and needed for K2.15; the (KN)-block part depends on bookkeeping (Q-KN) | C.1 |
| Theorem J2.1 (PROVED mod K2.15 chain) | correct with precisions P-1..P-6 (no conclusion changes) | C.2 |
| Corollary J2.2 (PROVED) | correct after P-4 and with K2.15 read with (FC); "strictly contains" unproved | C.3 |
| Corollary J2.3 (PROVED) | correct | C.4 |
| Data sign of a weak peak (PROVED) | correct | D.1 |
| Proposition J2.4 (PROVED) | correct with precisions J4-a..J4-c | D.2 |
| Lemma J2.5 (PROVED) | correct | D.3 |
| Remark J2.6 (PROVED) | core correct; final sentence HEURISTIC | D.4 |
| Step-0 Farkas certificates (SKETCH) | label honest; identity PROVED; "as hard as Step A" HEURISTIC | D.5 |
| Combination with J1 (PROVED mod J1) | correct as a composition, CONDITIONAL on J1.13-J1.15 (band realization) | D.6 |
| (LSC-trunc)_N for every f; density for p_N, p (OPEN) | OPEN (agreed) | F |

## B. Lemmas J2.0 and J2.1
B.1 Lemma J2.0.  PROVED (re-derived).  dPsi/d|zeta_j| = 2A (j in P: A-term |zeta_j| - theta Phi_j^2, B-term theta^2 Phi_j^2 independent of
zeta_j), = -2nu_j (j in Q: B-term zeta_j^2/Phi_j^2), dPsi/dth = -2(A + th)Phi_P^2; hence the formula for d theta; Euler from sum_P |zeta_j| = A +
theta Phi_P^2 and sum_Q nu_j|zeta_j| = A^2 - theta^2 Phi_P^2.  (a) Threshold raisers: d theta/d|zeta_p| > 0 (p in P), d theta/d|zeta_q| < 0
(q in Q); every other rho of the block is multiplied by theta/theta'.  Alpha-mass identity a = A/theta = sum_P (rho_k - 1)Phi_k^2 (from A =
A(theta)) gives a >= u Phi_p^2 at a robust peak, so theta <= Design/u and a relative raise 3b of theta costs <= Design^C b/u^2 in value units and
moves kappa by <= 6b/a <= Design^C b/u relatively; a non-peak raiser l (rho_l >= u) moves its own ratio by <= C Design b/rho_l absolutely.
(b) SLIP: the bracket is >= (1/(theta Phi_k^2))(1/rho_k - a/(1 + a)) = (1 - a(rho_k - 1))/(theta Phi_k^2 rho_k(1 + a)) >= (1 - b)/(theta Phi_k^2
rho_k (1 + a)) > 0, not >= (1/(theta Phi_k^2 rho_k))(1 - a/(1 + a)) as written (off by the factor 1 - a(rho_k - 1)).  Positivity is all that is used.
Own push size <= 5 b theta Phi_k/m (u-units).
B.2 Lemma J2.1.  PROVED (re-derived; part 1 1.2).  (a) as stated; the frozen root is the zero in (0, th_max) (beyond th_max, A_f < 0 and A_f^2 - B_f
may vanish again; that zero is irrelevant).  (b) SLIP: at a fine status change the gradient of Psi_f in (|zeta_k|, th) jumps by 2(A_f - th)(1,
-Phi_k^2); in move units d|zeta_k| = m Phi_k d|u_k|, so derivatives of theta_f, kappa_f jump by O(Phi_k/(theta_f Phi_{P_f}^2)) = O(Design Phi_k).
The kink part is Lipschitz with constant <= C Design sum_{fine} Phi_k <= C Design c_{L+1} (not "C sum_fine Phi^2 <= C c_{L+1}"); K2.9(c) needs
C Design c_{L+1} W <= rho_0/2, which holds (W >= Design eta' >> c_{L+1}).  (c), (d), (e) exactly as stated; the constant in |kappa_f - kappa(Omega)|
is <= 24 (|d kappa/dA| <= 3 since a <= 1, |d kappa/dth| <= 4 on [theta_f, theta]).
Numerics (independent implementation: true block cross-checked with a water-filling solution of the dual norm program; frozen system by Newton
on (G1, G2) at 40 digits): ref_frozen_indep.out -- 389 admissible blocks, theta_f <= theta always, ratios 0.35 (of 3x), 5e-4 (of 4x), kappa constant
0.17, frozen Lemma K to 1e-40, derivative formulas to 3e-22, W-fix region 1 - R^2 >= sigma_rob/2, Step (i) floor inequality psi_d(r_0)/Phi_d <=
rho^f_d always; ref_boundary_e.out -- 20000 blocks at the boundary of (e)'s hypotheses, 0 violations.  J2's scripts frozen_check2,
lemmaJ21e_adversarial, frozen_c11_check re-run: outputs identical (rerun/).

## C. (FC), Theorem J2.1, Corollaries J2.2, J2.3
C.1 (FC).  PROVED that literal K-8 is defective, with qualifier Q-KN.  K2.9(c) needs a C^{1,1} map; the true kappa has O(1) derivative jumps at
threshold crossings (K-8).  A frozen map gives the TRUE ratios at the realized point only if its pattern is consistent there (B.2(c)); otherwise
exactness on Z_kappa (tiny minors exactly 0) is lost.  Literal K-8 freezes the coarse peak set of the INPUT row; in a (U)-block the active weak
peaks are peaks there (Step 0 pushes only in (T)-blocks) and are taken to rho <= 1 - eta' only by the rescaled targets s_m r'' inside the
realization.  At the realized point nu_k < theta_f while k is frozen as a peak: A_f contains the negative term |zeta_k| - theta_f Phi_k^2, B_f
contains theta_f^2 Phi_k^2 instead of nu_k^2 Phi_k^2, so (A_f, theta_f) != (A, theta).  Numerics (ref_K8_literal.out, 60 (U)-blocks, b << eta'):
with literal K-8 the true ratios miss the targets by 1.1e-4..4.4e-3 relatively (= 5..30 eta' Phi_k^2); with (FC) they equal the targets to 8e-40,
and the realized point is consistent in 60/60 trials.  Q-KN: in (KN)-blocks the claim holds only if the d_0 lever push is realized inside the
fixed point; if it is a one-shot pre-move (cert0 3.2), it raises theta by >= C' D eta' theta before the fixed point (U1-ref Prop. KN) and the
active weak peaks are already strict non-peaks at f_1 + Pi.  The (U)-block case alone shows that K2.15 needs (FC).
C.2 Theorem J2.1.  PROVED modulo the chain of K2.15, with P-1..P-6.
Proof check.  Step (i): Lemma J2.1(e) at f^0 with P_f = P_rob (nonempty, V1 Lemma D), W' = the other coarse peaks; frozen Lemma F: F(r_0) =
max_{N_T} m|r_{0,d}|K(sigma_rob, R_a(r_0)^2)/Phi_d <= max_{N_T} rho^f_d(f^0) <= (1 + b')(1 + 6x) (sigma_f >= sigma_rob, R^2 >= R_a^2, K increasing);
W-fix region from 1 - R^2 >= sigma_f/k_f.  Step (ii): K2.9(c) uses only first-order actions, a C^{1,1} remainder, Brouwer and the continuity of the
minimal-norm nonnegative selection; the (FC) map is smooth in the coarse variables on K (P_rob values robust, Q_f terms polynomial, Psi_f(0+)
robustly positive), fine kinks by P-1.  Step (iii): at the solution (T)-blocks have R^2 = R_a(r'')^2 exactly ((T)-blocks have no inactive weak
peaks or inactive robust non-peaks; nearly neutral ones are held at 0) and sigma_f <= sigma_rob + C sum_fine Phi^2, so rho^f_d <= F(r'')(1 +
C D^C c_{L+1}^2) <= 1 - mu/2 for every active near-threshold d (former weak peaks included); (U)-blocks: Lemma K monotone under the rescaling;
D2/KN-pushed carriers <= 1 - c eta'; (KN)-blocks: the lever raises theta_f (lowering a frozen non-peak raises theta_f; d kappa_f/d|zeta_{d_0}|
tiny); robust objects move << u.  Hence (FC) is consistent and B.2(c) identifies the frozen solution with the true companion.  Step (iv): the
remaining steps act at f^r or at the companion.
 P-1 Fine kinks: C Design c_{L+1}||t|| in the remainder (B.2).
 P-2 With Pi_0 != {} of size Design^C b/u (e.g. (P4)-type pre-pushes) relative positions shift by Design^C b/u, not C Design b: take b' :=
     Design^C b/u; J2.1(e)'s side conditions still hold (b << u^3/Design^C), and F(r_0) <= 1 + Design^C b/u.  "F(r_0) <= 1 + Design^2 b" is for Pi_0 = {}.
 P-3 KN^tr Step 2 needs F(r') - 1 <= delta_0 with (D2).  With the start r_0 the excess F(r_0) - 1 and the Lojasiewicz displacement are of size
     Design^C b/u resp. C_L(Design^C b/u)^{2/N_L}, so (D2) must be imposed with delta_0 evaluated at Design^C b/u.  K1-ref R-8(ii) enlarged only
     (D1); K2's (K2-e) states the factor for (D1) and (D2) -- this reading is required and suffices (u(w) is fixed before b(w); left sides
     increase with b, so the admissible b form an interval).
 P-4 Define (H2^flat) with any targets r'' in Z_kappa with |r'' - r_0| <= 2 eta', F(r'') <= 1 - (3/4) mu_kappa(eta'/3) and robust minors >= u/2
     (what Steps 1-3 deliver, cert0 C1); all later uses of eta' tolerate the factor 2.
 P-5 "Consistent in every block": blocks without tuned carriers are (U)-blocks (Delta'_m = 0) and need the D2 push of all their inactive
     near-threshold carriers (X1-ref D2; J1.14's "(U)-blocks, including blocks with no active carrier") -- or leave their scalars unfrozen
     (they enter no row).  State it.
 P-6 Audit: the (X4^0) data violation and the kind-[3] shift-trick cost (X1-ref 3.2, cert0 3.5) also use the start row (|r'' - r_1| <= eta');
     with r_0 they hold with eta' + Design^C b/u.  No other use of the pushed row (checked K1 4.1 Steps 1-7, K1-ref R-6/R-8, K2 4.1, 6.3-6.5,
     cert0 3.1-3.6, X1-ref 3.2-3.3, 8, S-0).
C.3 Corollary J2.2.  PROVED after P-4.  With Pi_0 := (WP), f^0 = K2's f_1 after (P).  In (T)-blocks (FC) = literal K-8 (after (WP) the coarse
peaks of a (T)-block are exactly P_rob).  In (U)-/(KN)-blocks (FC) is the correction of C.1, so (H2) must be read with (FC).  K2's start r_1
(formula-1 ratios at f_1) and r_0 (frozen ratios at f_1) agree in (T)-blocks and differ by <= C Design b in the others (J2.1(e)); targets admissible
for (H2) satisfy |r'' - r_0| <= 2 eta', hence are admissible for (H2^flat) under P-4.  "So this STRICTLY contains K2.15" (J2 bottom line (1)) is
NOT proved: the toy of J2 4 has a two-sided peak resource, which also gives (H1*) through Proposition J2.4(ii); a configuration with (H2^flat)
and not (H1*) (e.g. a weak peak whose only inward resource is a pull at depth >= x, too large for (H1*)'s size bound, compensated in Step A by
two-sided levers) is plausible but not exhibited.  HEURISTIC.
C.4 Corollary J2.3.  PROVED.  Failure of (H2^flat) includes Pi_0 = {}; K2.9(b) gives a near-certificate of size < 4u^3 Design^{-C_A} <= eps_* (C_A
>= C + 1, K-7) with phi_y > -rho_0 for the (FC) Sys-A at f^0 + Pi.  K2.16's proof uses (2.1) and K2.4 (any row), K2.8 for kappa_f (1-homogeneous:
Euler and chain rule hold), the Euler share (|Xt_m| <= C|Lambda| Design c_{L+1}^2: Omega = all coarse non-P_rob carriers, so s_f comes from fine
non-peaks only), d kappa_f/d zeta(c) >= 3/4 at peaks, and the kinds after (P).  A weak peak with no push resource has no (P1) and no (P3), hence
is of kind (iii) or (iv).  So non-coverage by J2.1 implies a K2.16 near-certificate at the unpushed row at all large stages; by C.3 the new
residual is contained in the old one.

## D. Data signs and the direct route
D.1 Data sign.  PROVED.  Part I lem:peakshift (martin_density_note.tex 4821-4856): varsigma_k(omega_- - omega_+)(k) = |omega_+(k)| + |omega_-(k)| =:
e_k >= 0, small only if alpha(k) is robust.  In U1's convention (Delta = d(omega^-) - d(omega^+) = -Delta d, gamma = lambda(Domega - Delta w) =
-lambda DeltaTheta, w(k) = varsigma_k M): varsigma_k gamma_k = lambda_k(e_k - Delta'_m), so eps_k = vs_k sgn(e_k - Delta'_m); robust peaks
(Domega(p) = 0, X1 Lemma EC): eps_p = -sgn(Delta'_m) vs_p.  R-8/W-1's formula fails iff Delta'_m > 0 and e_k > Delta'_m; then a near bank moves
|u_k| outward.  No K1-ref/K2-ref conclusion changes ((H1*) is stated by its effect).
D.2 Proposition J2.4.  PROVED with precisions.  J4-a: a raise at a THIN coordinate s in F changes other coarse values at first order by
-(mu_s^2/nu) kappa_{u_j} a_s dm, relative size <= Design b; absorbed by the overshoot.  J4-b: own pushes <= 5 b theta Phi_k/m.  J4-c: Step-0 banks
need mass delta x Design(L) (efficiency >= 1/Design only), so they create S_th support of modulus up to Design^C b (own pushes) or Design^C b/u^2
(threshold raisers), outside K2-ref K-3's range [theta_0, 2b]; K2.16 tolerates moduli <= Design^C b/u^2 ((1), (6) need D(L)|kappa| max|a_s| <<
c_*; (2c), (3) need D(L)|kappa| max|a_s| << c_1/H(L); b << u^3/Design^C).  The same remark applies to R-8's (WP) banks inside K2.15; the bypass with
Pi_0 = {} avoids it.  During a finite threshold raise the weak peaks leave P (d theta piecewise smooth, theta continuous and increasing in the
raised value): intermediate value theorem.  No (P4)/(P5) column, no Sherman-Morrison denominator.
D.3 Lemma J2.5.  PROVED (case analysis re-done; a robust peak without bank, raise or (P3) has only thick near coordinates with tiny spreads,
type (S); a (P2) carrier has a two-sided TU lever).
D.4 Remark J2.6.  PROVED: rt_l = eps_l r''_l and sigma_l = eps_l (v > 0) give K2.17(g)'s sign = vs_l eps_l; (X3)/kappa: sum |r_l||gamma_l| vs_l eps_l =
Delta'_m on the class cone; active weak peaks have orientation sgn(e_k - Delta'_m) = +1 when Delta'_m < 0, so some other active carrier has -1.
The kappa-window sentence is the one-dimensional caricature of J1 Lemma J1.2: HEURISTIC.
D.5 3.3.  Psi^0_y(xhat) = sum_W y_k - sum_m Y_m theta_m^{-1} sum_j (d theta_m/d|zeta_j|)|zeta_j| = 0: PROVED.  Transfer of K2.16's structure: SKETCH.
"As hard as Step A": HEURISTIC.
D.6 Combination with J1.  The composition is logically sound: no near-certificate of size <= eps_* => A-regular (contrapositive of K2.9(b));
K2.17(a), (b) => positive spanning; (f) => A-regular for the given right-hand side; J1's (J-a)-(J-f) => Step A realized (J1.15).  But (J-c)-(J-f)
realize Step A with BANDS (J1.8, J1.9, J1.13), which is not (H2^flat); Theorem J2.1's Steps (iii)-(iv) then need J1.13's claims (statuses kept,
pinned ratios exact on Z_kappa, data projected at the realized ratios).  Given those, (FC)-consistency and B.2(c) apply verbatim.  Status:
PROVED modulo the K2.15 chain and CONDITIONAL on J1.13-J1.15 (refereed separately).  J1's setting already is the unpushed row with (FC) (J1 1).

## E. Attacks attempted (all survived)
Puiseux margin (F(r'') <= 1 - mu from any start with F - 1 <= delta_0: P-3); exactness on Z_kappa (consistency at the solution; literal K-8
fails, (FC) holds: C.1 numerics); cushion domination C_+ (no new support with Pi_0 = {}; with (WP)/Pi_0 as in K1/K2, J4-c); (VT) tolerances and
closeness K t (data and cone unchanged; companion closer to f^r); cost o(c_flat^2 T^2) (Pi_0 <= C_f Design^C b log(1/b)/u^2); uniformity along main
stages and N-independence (no design change; (K2-e) needed in the form P-3); quantifier order (design -> N -> f, g, rho -> l_f -> L -> w -> class ->
Pi_0 -> (P) -> targets -> Pi -> Step A -> data); signs and one-sidedness (weak peaks enter Step A as tuned carriers with their one-sided
generators; D.1); every row in a covered case: NO -- residual (A*)/(U*) at the unpushed row (C.4).  Counterexample: none.

## F. Most valuable idea; what remains open
Most valuable idea: freeze the block scalars with the TARGET status pattern (robust peaks as peaks, every other coarse carrier as a non-peak).
The frozen system is C^{1,1} across all threshold crossings Step A performs, satisfies Lemma K exactly, is within O(Design b) of the true one at
the unpushed row, and coincides with it wherever the pattern is consistent -- which Step A's own targets guarantee at the realized point.
Status-changing pre-moves (Step 0's weak-peak pushes) become ordinary Step-A rows, the joint push problem (W*) disappears as a separate
obstruction, and literal K-8 (defective in (U)-blocks) is repaired.
OPEN: (H2^flat) at every row, i.e. the sign class (A*)/(U*) of Theorem K2.16 at the unpushed row (J1's residual (R0)/(R1)); whether (H2^flat) is
strictly weaker than (H1*) + (H2); the once-refereed links of the K2.15 chain; J1's band realization (J1.13-J1.15) and J1.11 (SKETCH).
(LSC-trunc)_N for every f, density of NA((c_0, p_N), l_2^2) for any N, and density of NA((c_0, p), l_2^2) for the Martin-type p: OPEN.
