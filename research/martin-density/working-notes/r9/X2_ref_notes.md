# X2 referee notes (Round 9): d-consistent engineered approximants, uniform composition (S2), mixed classes (C_mix)

Refereed: r9/X2_notes.md (= X2_head + X2_part1..6, identical up to blank lines, checked with diff), r9/X2_work/*.py (re-run: dcons_check,
dcons_check2, dc_jacobian, ue_check — numeric output identical).  Against: paper/martin_density_note.tex (lem:threshold, def:certificate,
lem:base, lem:block, lem:bookkeeping, lem:TV, prop:rebalancing, lem:transferdata, lem:persistence, lem:assembly, def:twopiece, def:engineered,
lem:approxfacts, lem:F1, lem:anchor, def:SC, lem:scrambling, thm:engineered with proof, lem:slack, prop:reduction), U1 parts 1-5, U1-ref
(Lemma R-kt, Proposition KN, Sections 4-8), U3 Lemma VT and U3-ref (F6), U4/U4-ref (T_final), V1 Proposition TR.
Part files: r9/X2_ref_part1..4.md.  Scripts (new, independent model written from scratch): r9/X2_ref_work/rmodel.py, check_J.py, check_J2.py,
absorber_check.py (+ .out); re-runs of X2's scripts in r9/X2_ref_work/rerun/.
Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  Setting: finite block set I = {1..N}, p = p_N, diagonal base, design D^{X2} (= D^{U1'} on
T_final + (D-lev) + (W_exp)), F finite.

## 0. Summary of verdicts
| X2 claim (label) | Verdict |
|---|---|
| Lemma M1, Cor. M1' (PROVED) | correct |
| Proposition J (PROVED; attainment HEURISTIC) | correct upper bound, precision (p-J); the precision of U3-ref F6a is right |
| d-consistency identities 1.4 (PROVED) | correct; REFEREE ADDITION: with Omega = all coarse strict non-peaks, d-consistency freezes C up to fine carriers |
| Lemma M2 (PROVED) | correct; "peaks remain peaks" only above the perturbation (p-DC3) |
| Lemma DC (PROVED) | correct as an abstract lemma after (p-DC1) radius, (p-DC2) pulls are fixed O(1) moves, (p-DC3) |
| Lemma LV (PROVED) | (a)-(c) correct for COARSE carriers (p-LV1, p-LV2); (d) FALSE in the application: zero-value absorbers cannot be re-tuned (Section 2) |
| Lemma UE-1, Theorem UE (PROVED) | correct as conditional statements after (p-UE1)-(p-UE7); K_sharp and c_flat are f-constants — the substance is right |
| Theorem E^eng (PROVED) | correct as a conditional theorem; one missing hypothesis (p-E1) |
| (S2c) with (W_exp) (PROVED arithmetic) | correct for coarse levers; false for X2's absorber levers; (W_exp) must be imposed after MAIN stages only (p-W) |
| Lemma CM (PROVED) | the self-aligned / anti-aligned rule and the violation count are correct (key idea); its use with tuned absorbers fails |
| Theorem C_mix (PROVED) | GAP as written; TRUE after repair (R-abs) (Lemma CM', Theorem C_mix', PROVED here) |
| Master Theorem V + contrapositive (PROVED mod refereed tools) | statement PROVED after (R-abs); contrapositive correct |
| Design D^{X2} (PROVED by inspection) | correct with (p-W) and n_l in (D-lev) |

## 1. Proposition J and the d-consistency identities (proofs of the precisions and of the referee addition)
1.1 (Proposition J re-derived.)  For valid data (Gamma_w <= Gamma_max), ||D Domega||^2 = Delta^2 + C H(Domega), Delta^2 <= C^3 H/(M^2 Phi_P^2)
(D Domega vanishes on P, so the component orthogonal to Dw has norm >= |Delta| M Phi_P/C), H(Domega) <= 4 Gamma_max/sigma.  The identity
(d' - d)(Domega) = sum_k Domega(k) lambda_k (u_k(xhat') - u_k(zhat))/A' + Delta (A - A')/A' is exact (formula (1.0) at both rows), and Cauchy-
Schwarz gives |kappa^+-| <= (rho/2)[m ||D Domega||_2 |Omega|^{1/2} max_Omega |Delta u_k|/A' + |Delta||A' - A|/A'].  Numerically
(check_J2.py, independent model, |Omega| = 2): max ratio 1 - 6.8e-3; attained (ratio 1) when |Omega| = 1 and the two terms have equal signs.
(p-J) The cut-off contribution is max_{Omega} t_k (<= t(N'')/min lambda_Omega), not t(N''); harmless.
Uniformity in t: by the SHARP bound of Corollary M1' (masses off the support, as in def:engineered), ||X|| <= 4 rho s_1 (nu sum_i h(b^theta_i))^{1/2}
= O(s_1 n^{1/2}) for valid data, uniformly in the piece scales.  U3-ref's "kappa ~ s_1/t^2 with equality up to constants" used ||e'-e|| <=
K_e s_1 with K_e ~ ||b^theta||_1 ~ 1/t and ||lambda Domega||_1 ~ 1/t, and was tested on a datum scaled by 1/t (Gamma_w ~ t^{-2}, excluded by
rho^2 kappa_w < 1).  X2's correction is right; the non-uniformity in (n, |Omega|) is real, so an exact cancellation is the right remedy.
1.2 (REFEREE ADDITION, PROVED: d-consistency freezes the block scalars.)  Let Omega_m = Q_m \ (fine carriers) as in U1, and let f' be
d-consistent with f_0 on Omega with the same peak set.  Then
      |C'_m - C_m| <= (2(1 - C_m)/(C_m c_*)) sum_{k in Q_m \ Omega_m} Phi_k |v'_k - v_k|,     v_k := |nv_k|/Phi_k.
Proof.  By the clamp formula (proof of lem:F1), C is the root of F(c; v) = sum_k min(Phi_k (1 - c)/c, v_k)^2 = 1.  Near c = C the peak terms equal
Phi_k^2 ((1-c)/c)^2 (independent of the values); the Omega terms equal v_k^2 = (nv_k/Phi_k)^2, unchanged; only Q \ Omega terms move.  lem:F1's
monotonicity argument through the natural peak gives the bound.  QED
Consequences: with Q \ Omega = fine carriers, |C' - C| <= K (c_fine Pi + W_pull); by (1.1) every Omega carrier keeps its gap and its relative
position rho_k = |nv_k| C/(Phi_k^2 M) up to this error.  So d-consistency preserves all statuses of the switching carriers (compare U1-ref
Lemma R-kt: no second lever is needed for d-CONSISTENCY; R-kt concerns moving statuses at fixed ratios).  Numerically: Omega = Q gives
|C' - C| <= 1.1e-16 (25 instances), Omega = Q minus one carrier gives ~5e-11 (check_J2.py).

## 2. Lemma DC and Lemma LV
2.1 Lemma DC (abstract) is correct: slopes are exactly 1 (z-moves by construction, banks through Lemma M1(i)), dA_m = <w_m, R_m dxhat> so the
Jacobian is I - p q^T per block with q^T p = sum_{Omega_m} Phi_k^2 w_m(k)^2/C_m in [0, C_m] subset [0, 1/2], Sherman-Morrison bound 1 + 2/A_min,
Poincare-Miranda on the cube.  Precisions (proofs):
(p-DC1) |F(0)|_inf <= delta_1 (1 + 1/A_min) + 2 W_pull/A_min (since |A_m(1) - A_m^0| <= sum_k lambda_k |Delta u_k|), so take
        r := 4 K_J (1 + 1/A_min)(delta_1 + T^4 s_1) + 8 K_J W_pull/A_min (X2's r := 4 K_J (Pi_X + T^4 s_1) misses the factor).
(p-DC2) A TU pull is a FIXED move (z(j_p) flips by 2), so a carrier k != l meeting j_p moves by 2|u_k(j_p)|, not by C_lev r.  Such carriers are at
        stages >= j_p (allowedness (c): supp y_k ∩ S_l ⊂ [1, k]); with j_p ~ log_2(1/r) their total weight W_pull <= 2m sum_{stages >= j_p} c is
        super-small.  It enters F(0) (above), the Bregman bound (<= 4 W_pull), the scrambled set (<= 4m W_pull and 4 W_pull^2) and Z3 Lemma 3.1's cost.
(p-DC3) "Peaks of f_0 remain peaks": only peaks with margin above the value moves (all coarse peaks).
2.2 Lemma LV.  (p-LV1) (D-lev) gives mu_j^2 delta_l 2^{-j} >= 1/Design; with v_l = delta_l 2^{-s}/n_l add n_l to Design.  (p-LV2) For X2's parameters
(r >= 4 K_J T^4 s_1, s_1 >= exp(-1/(2T)) >> c_{L+1}^2 >= 2^{-s_far(w)}-scale) the pull coordinates lie in S_l ∩ (s_max, s_far] ⊂ E_c(w), not in
J_fine; their data are contact-like by exactness on E_c (U1 Prop. 3.4), not by ownership.
2.3 THE ABSORBER OBSTRUCTION (Lemma LV(d) fails in the application).  PROVED.
Setting: X2's companions (U1's f^# with every first pair P(s), s in E_c(w), and the cluster of L tuned to value 0 and carrying switching
coefficients), Lemma DC with Omega ⊃ these absorbers and (S-mass) levers at their tuning coordinates p_0.
(A1) Every lever of a coarse carrier acts at coordinates of E_c (the bank / Z-coordinate j(l) and, by (p-LV2), the pull j_p); each such s has a
     tuned first pair, with |u_a(s)| = |y_a(s)|/n_a >= 1/(8 n_a) (U1 (A0)).  A z-move Delta z at s moves u_a by |u_a(s)| Delta z: the pull flip by
     >= 1/(4 n_a), a Z/bank lever by >= r/(8 n_a Design).  A theta-mass m_s at s moves u_a by m_s mu_s^2 |u_a(s)|/nu.
(A2) An absorber is a strict non-peak iff m |u_a(xhat)| < theta Phi_a (lem:threshold): its value room is theta Phi_a/m ~ lambda_a <= c_{L+1}, and
     for s in (L, N_w] the first pair sits at a stage >= s with a weight super-exponentially small in s.
(A3) The (S-mass) lever changes u_a by Delta m mu_{p0}^2 u_a(p_0)/nu; m_0 must stay > 0 (and >= t|b_t(p_0)| for no flips), so the range in the
     decreasing direction is <= m_0 mu_{p0}^2/nu ~ lambda_a T_hi mu_{p0}^2 (p_0 fresh, beyond every earlier coordinate); in the increasing direction a
     correction Delta u needs the mass Delta u nu/(mu_{p0}^2 |u_a(p0)|), astronomically larger than 1, which replaces the base part of the row.  These
     are not design quantities of level L: the "Consequence" of Lemma LV (r_0, C_2, K_J <= f-constant x Design^C) is false for (d).
(A4) Hence, with r >= 4 K_J T^4 s_1 and s_1 >= exp(-1/(2T)), Lemma DC's hypotheses (r <= r_0, K_J|F(0)| <= r/2 — the pulls alone put
     |F_a(0)| >= 1/(4 n_a)) fail.  Without re-tuning, every absorber touched becomes a PEAK of f', and since Domega(a) = gamma_a/lambda_a != 0
     (biased pairs: gamma_a >= c_0/4 > 0; used pairs |Domega(a)| up to C_f Design^2), lem:block(c) fails at a: the block expansion acquires the
     first-order term |sigma omega^diamond(a)|, i.e. rho|tau||Domega(a)|/2 in the theta regime — not O(tau^2), so (UE) is not proved near tau = 0.
     A smaller s_1 (below the rooms of the finitely many touched absorbers; N_w is fixed before s_1) avoids this only if 64 rho eps/delta is below
     those rooms, which fails generically in mixed classes (a frustrated positive carrier at a main stage L' > L violates with mass ~ c_{L'} delta_{L'};
     first pairs of theta-mass coordinates s in (L', N_w] sit at stages > L' with weights << c_{L'}).
(A5) Lemma CM(a)'s "x_0(f^#) >= c_f gap_min Phi_min(L) (tuned absorbers gap 3M/4)" is wrong for absorbers of a negative block 1: they contribute
     Phi_a to Scr_1(x) for x >= Phi_a M (the condition is Phi gap <= x, and Phi_a gap ~ Phi_a M is tiny), so Scr_1(x) <= C_S x^2 fails at x ~ Phi_a.
Numerical illustration (absorber_check.py): absorber with Phi_a = 1e-7, mu_{p0} = 1e-3, tuned to value 0 by m_0 = 1.6e-2; an inward lever move of
the coarse carrier at s lowering its value by P = 1e-6 moves u_a 90-170 times beyond the room theta Phi_a = 8.3e-8 (the absorber becomes a peak);
restoring u_a = 0 needs a negative S-mass (beta = -1: none in [0, 1e14 m_0]) or 10^3 m_0 (beta = +1); for P = 1e-3 neither sign is restorable.

## 3. Theorem UE, Theorem E^eng, (S2c): precisions (all window-quantity adjustments; no conclusion changes)
Re-derived line by line against thm:engineered: Step 0' order of choices consistent; decompositions exact for violated pairs; with d' = d on Omega,
Omega^+- = rho(omega^+- - d^+- w') + rho(d^+- - d^theta)(w' - w^0), kappa = 0, lin'_m = r_m <V^an - w', R x'>/sigma' (lem:algebra at f'); radius
conditions of kinds [1]-[3] ((c4) implies 4 rho c_flat <= 1/4); base claim (*) at every new coordinate type; Steps 4-5 with T_0 = c_flat t_i (all
cubic/quartic errors are (const) c_flat tau^2 since the data enter as K/t); Assembly-type inequalities in E^eng; subset averaging.
(p-UE1) Lemma UE-1(b): carriers meeting a pull coordinate move by 2|u_k(j_p)| (p-DC2); lever masses affect carriers not meeting their coordinates
        only at second order (Lemma M1(i)), so (b) can be sharpened to Pi_X + C(||X|| + ||X_lev||)^2/nu^2 + t_k.
(p-UE2) Lemma UE-1(d), (e): add 4 W_pull (Bregman), 4m W_pull and 4 W_pull^2 (scrambling); d-consistent Omega carriers belong to S_2 of lem:anchor
        whatever Phi_k gap_k is (w'(k) = (C'/C) w(k), gap' >= gap/2), so (U5) is needed only off Omega.
(p-UE3) |c_i| <= K_w (Pi + c_fine + tail_W)/t_i (the 2 c_fine from ||R^*(w^0 - w')||_1 is missing in the first bound of (g)).
(p-UE4) = (p-DC1).
(p-UE5) (LATE) as displayed does not imply the inequalities used (K_w^3 s_1 log(e/s_1) <= c delta; r <= r_0 and K_J (C_2 + C) r <= 1/4; Pi <= 1/K_w;
        K_w^2 s_1 log(e/s_1) <= theta T^2 in E^eng).  Define s_late := c delta (T gap_min x_0/(n A_0 K_w))^{C} with a suitable absolute C; still >= T^{C''}
        at U1's companions (after (R-abs)).
(p-UE6) (W-a) must read c_fine <= c_late delta T/(n A_0 (1 + C_2 K_J)) (or use (p-UE1)'s sharpening), and W_pull <= c delta s_1 must be added.
(p-UE7) "Lever coordinates carry zero or contact-like data" at U1's companions holds only with the tuned absorbers (exactness on E_c) — which is
        what fails (Section 2); after (R-abs) the data there are zero/contact-like up to the fine residue V_fine, tolerated as violations.
(c3') At a TU pull the data are (chi, chi - 1) gamma_l v_l(j_p) (+ residue), |gamma_l| <= lambda_l (2 A_2/t + C_Delta) (|Domega| <= 2 A_2/t); no flip
        needs rho c_flat (2 A_2 + C_Delta) <= 7 rather than X2's (c3).  Likewise (U3) at the supports of (1a) holds as t|b| <= K_3 |a^#| (V1 TR(iv)
        with V1's constants; U1-ref's Proposition KN pulls carry data up to (2 A_2 + C) lambda v/t against mass 24 lambda v), absorbed in (c2).
(p-E1) Theorem E^eng needs K_w (K_w s_1 + c_fine + tail_W) <= K T^2: add K_w c_fine <= K_j T_j^2 2^{-2 n_j} to (E-f) and choose tail_W <= K T^2/K_w.
(p-W)  (W_exp) "at every stage l+1" contradicts D^{U1'}'s cluster weights c_{p+i} = c_{p+1}^low 4^{1-i} (sub-window data exist at every stage, and
        exp(-1/T_lo(p+1, M(p+1))) << c_{p+1}^low/4).  Only c_{L+1} after MAIN stages is used: impose (W_exp) in c_{L+1}^low for main stages L.  Then it
        is an extra upper bound on one weight per round, computed after the level's sub-windows; R of absorber targets is computed from c^low;
        (T-a)-(T-d), (P1), (P2), N-freeness unaffected.
(S2c) after the corrections: K_w <= T^{-C'} (n <= log_2(1/T), Design <= n, gap_min >= c_f T^4/(L Design), x_0 >= c_f gap_min Phi_min(L) for COARSE
carriers, coarse lever constants <= Design^C), s_late >= T^{C''}; eps <= C_f Design c_{L+1} <= C_f Design exp(-1/T) (W_exp); s_1 := max(64 rho eps/delta,
exp(-1/(2T))) lies in [64 rho eps/delta, s_late] and also dominates C Design c_{L+1}/delta (needed for the fine-carrier lever effects).  PROVED.

## 4. The repair (R-abs): mixed classes without absorber switching.  PROVED (modulo the refereed tools cited by X2).
Lemma CM' (completion without absorber switching).  Design D^{X2} with (p-W); F finite; w a clean sub-window of a main stage L >= l_f; a class a
(no active shift, one-signed or mixed) with (KN_{w,a}); S a (class, cube) set.  Companion f^#: (1a) Proposition KN (U1-ref 3.3); (1c') restore
kappa exactly (U1-ref Section 1: kappa continuous) and re-realize the values of Omega_act exactly (explicit joint fixed point of V1 Lemma TU, block-
triangular Jacobian as in Proposition KN Step 2); no absorber is tuned; (2') on J_fine := N \ (F^(1a) ∪ E_c(w) ∪ coordinates fixed in (1a), (1c'))
with U1-ref's G1 release, the static-ownership recursion with owner-candidates (a) Omega_act, (b) coarse peaks of active blocks, (d) every carrier at
a stage > L of an active block (D^{U1'}'s absorbers included, with their forced coefficients); negative blocks self-aligned, positive blocks anti-
aligned, coarse owners by the sign of their coefficient, unowned coordinates z = 0.  Data at t in S: Domega(t) of U1 Proposition 2.2(e) supported in
Omega := all coarse strict non-peaks (no absorber coefficients), with the common true shift (U1 Lemma 4.6(a); its middle term vanishes by (1c'));
V := V(Domega(t)), V_proj := L(Delta'^*, gamma(t)) on E_c (0 elsewhere), V_fine := V - V_proj off F^#,
    b^+ := beta + chi V_proj + V_fine/2,    b^- := b^+ - V,    omega^+ as in U1 2.2(e),    omega^- := omega^+ + Domega(t).
Claims, for every t in S: (a) every carrier at a stage > L of a negative active block is an (R) peak with margin >= q^#_0 delta°_k/2, and for m in A_-,
Scr_m(x) <= C (x/q^#_0)^2 for 0 < x <= x_0 := c_f gap_min Phi_min(L); (b) (b^+-, omega^+-) represent g_t with p*(g - g_t) <= K t, kappa_w <= 1 + eta_0/2,
kinds [1]-[3]; (c) the violation mass satisfies eps(t) <= C_f Design(L) c_{L+1} + C_f c_{L+1}^2/T_lo(w), all free violated coordinates have
b^theta = 0 ((H3)); (d) p*(f^# - f) <= theta_w T_lo(w)^2, theta_w -> 0, and the coarse statuses of Proposition KN(b).
Proof.  (a), (d): Proposition KN(b), U1 Lemmas 4.1, 4.3, 4.5 and U1-ref Section 7; absorbers enter only as fine carriers, which those statements
cover (at absorber stages c_p <= (delta^max_p H_p/2)^2 and (W4'') hold, U1-ref 6.2).  (b): U1 Proposition 2.2(e); removing the absorber coefficients
and re-splitting V_fine changes g_t by <= ||V_fine||_1 + sum_a |gamma_a| <= C_f Design c_{L+1} <= K t, and Gamma by O(c_{L+1}^2) (q_0 h(y) <=
||U||^2 ||y||_1^2/nu, sigma H(x) <= (sum lambda |x|)^2/C).  (c): at an E_c contact, z V_proj >= 0 (cone row (X1)) and chi in [0,1] give
(z b^+)_- <= |V_fine|/2 and (z b^-)_+ <= |V_fine|/2; at a free coordinate off F^#, V_proj = 0 ((X1)), so b^+- = +-V_fine/2, b^theta = 0 and
viol = |V_fine|; on J_fine, V_proj = 0, b^+- = +-V/2: admissible on coordinates owned by coarse owners and negative fine owners (U1 Lemma 4.2
dominance, signs not used), V = 0 on unowned (= free) coordinates, viol <= |V| on coordinates owned by positive fine carriers.  On E_c,
V_fine = [L(Delta'', gamma) - L(Delta'^*, gamma)] + (carriers at stages > L): the first is U1 Lemma 4.6(b)'s trace correction (admissible on near
signature sets of coarse peaks, l_1-norm <= C_f Design c_{L+1} + C_f c_{L+1}^2/t on T(L)), the second has l_1-norm <= C_f sum_{l > L} lambda_l
(coefficients <= C_f lambda, ||u||_1 <= 1); the same bound covers the positive-owned coordinates of J_fine.  QED
Theorem C_mix' (= X2's Theorem C_mix with Lemma CM').  Design D^{X2} with (p-W), N fixed, F finite.  If for infinitely many main stages L some clean
sub-window w of L has a (class, cube) set S of >= n(w)/D_cls(w)^2 scales of one class a (no active shift, one-signed or mixed) with (KN_{w,a}),
then f in Rec(p_N).
Proof.  Window family at f_0 := f^# of Lemma CM': (U1), (U2) by (b); (U3) at the supports of (1a) by V1 TR(iv) (constant K_3 absorbed in (c2));
(U4) by (c); (U5) by (a); (U6) Lemma LV(a)-(c) for Omega = coarse strict non-peaks (no (S-mass) lever) with (p-LV1), (p-LV2): the data at a lever
coordinate j are gamma_l v_l(j) + V_fine(j) (TU) or V_fine(j) (Z), contact-like up to V_fine, with b^theta(j) = (chi - 1/2) V_proj(j) = 0 at Z-coordinates
— covered by (c); (U7) U1 Lemma 2.1.  Lemma DC applies with design-quantity constants; the levers move, besides their own carriers, only carriers
at stages > L (allowedness), which carry no switching coefficient, so their effect on the Bregman and scrambling terms is <= C (c_tiny + W_pull) <=
C Design c_{L+1} <= c delta s_1.  Theorem UE (with Section 3's precisions) at f^#, s_1 := max(64 rho eps/delta, exp(-1/(2T))); Theorem E^eng on the
subset S (U1 Lemma 2.4), (E-c), (E-d), (E-e) as in U1-ref's MT IV', (E-f) and (p-E1) by (W_exp).  QED
Master Theorem V (X2's statement) follows: PROVED modulo the refereed tools, with (R-abs) in the mixed case (one-signed classes may use either
MT IV' or Theorem C_mix').  Contrapositive (correct): an F-finite f notin Rec(p_N) is a (C*) row at which, for all but finitely many main stages L
and every clean sub-window w of L, more than n(w)(1 - 1/D_cls(w)) scales lie in classes violating (KN) — U1-ref's status coherence.
Remark (why (R-abs) is natural).  Absorbers were invented (U1) to make coarse data EXACT; in the violation-tolerant regime exactness is not
needed, and absorbers are harmful there: their value rooms are of the size of their weights, far below the perturbation size s_1 that (VT') forces.

## 5. Attacks attempted
weak* vs norm (companions and approximants converge in p*; transfer data persist on the ball of Lemma M2); uniformity in t (per-piece radius
c_flat t_i, K_sharp an f-constant, theta regime common to all pieces, pieces with c_flat t_i <= s_1 only use the theta regime); in the window (K_w,
s_late polynomial in T after (R-abs)); number of carriers (|Omega| <= L N, n pieces: window constants); along companions (Lemma M2 ball); simultaneous
exactifications/levers (FOUND: absorber levers incompatible with the coarse levers and the theta-masses, Section 2; Prop. KN's levers and Lemma
DC's use disjoint coordinates of different scales); two-lever count of R-kt (no conflict: d-consistency is rank one, statuses frozen by 1.2);
Hoffman constants (only through the refereed Prop. KN); design (FOUND: (W_exp) placement, n_l in (D-lev)); signs/one-sidedness (FOUND: the (S-mass)
lever is one-sided with a tiny range); quantifier order (design -> f -> g, rho -> transfer data -> main stage, clean w -> companion -> class, cube
-> data -> N_w -> s_1 -> levers -> N''); counterexample: none suggested — every obstruction found is a bookkeeping/route defect with a repair.

## 6. What remains open (design D^{X2} with the repairs; finite I)
F finite: status coherence — (C*) rows at which, at all large main stages and all clean sub-windows, almost all scales lie in activity classes
violating (KN_{w,a}) (an active block with an active near-threshold switching carrier and no inactive Omega carrier of robust relative position).
This is exactly U1-ref's residual (X1's task).  F infinite: (E1)-(E5) / U2's items (transport of MT III', tuning regularity modulus, (W_inf), (SC)
along deep raises), plus (C*) at infinite F.  Lemma Z, density of NA((c_0, p_N), l_2^2) for every N and of NA((c_0, p), l_2^2): OPEN for every
admissible T.  No counterexample; nothing found points to one.

## 7. Single most valuable idea
In the violation-tolerant regime no EXACT completion of the fine structure is needed: negative fine carriers are made self-aligned (state (R),
explicit quadratic scrambling bound), positive ones anti-aligned, and every failure (frustration, fine residues on coarse coordinates, trace
corrections) is a contact or theta-free violation of mass O(Design c_{L+1}), which d-consistent engineered approximants tolerate uniformly in
the scale (Theorem UE + averaging at the norm-attaining point, Theorem E^eng) once the weights are super-small ((W_exp)).  The referee's
complements: d-consistency freezes the block scalars and the statuses of the switching carriers up to fine terms (1.2), and the zero-value
absorbers must be DROPPED from the violation-tolerant route (they cannot follow the levers), which (R-abs) shows is possible at no cost.
