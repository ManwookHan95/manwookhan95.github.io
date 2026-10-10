# U2 referee notes (Round 8): verified results, fixes and their proofs

Part files: r8/U2_ref_part1.md (design, Lemma P, RS*, ND'), U2_ref_part2.md (Lemma W, RS*_inf, RS*_inf without (ND')), U2_ref_part3.md
(DR-inf, TR-inf, residual, M-inf, (E3), (E4)), U2_ref_part4.md (proofs of the fixes).  Scripts: r8/U2_ref_work/tr_inf_joint3.py (joint
exact tuning, cases (c), (c'), 600 digits), sm_check.py (Sherman-Morrison determinant, exact kernel drift).
References: the note paper/martin_density_note.tex; Z5-ref (R0, R1, R2); V3 + V3-ref (2.1-2.5, VP', RS', I1-I3); V1 (D_Omega, Lemma S, B,
DR, TU, CO, ST, NS, RR, Prop. TR); V2 (Def. 2.1-2.2, Theorem B, Def. 3.2, Theorem C1); U4-ref.  Setting: I = {1..N}, p = p_N, f in S_{p*} with
forced data (xi, q_0, a, w, F, z, zhat, e, nu), F = supp a arbitrary, s_j := sgn a_j.  Labels PROVED / SKETCH / HEURISTIC / OPEN / FALSE.

## 0. Verdict summary
PROVED and correct as stated (after minor precisions): Design SLD^star; Lemma P; Theorem RS*; Lemma ND; Theorem ND'; Lemma TR-inf (cases (a),
(a'), (c), (c')); Lemma DR-inf for (R1)-(R5), (R7), V2's minors; (E3)(a), (b); "single unpaired support raise not admissible" (E4).
PROVED after a fix given here: Lemma W and Theorem RS*_inf (add the bad-peak margin rate 1/mu_B(l), Fix 1); T_final^* (B_mu* with d(l), new
rate objects in omega(l), Fix 2); DR-inf with (R6) (exact invariance, Fix 3); raise depth J > d(l) in the transport (Fix 4).
Upgraded: "RS*_inf without (ND')" from SKETCH to PROVED conditional on an explicit kernel rate (Fix 5).
FALSE: the 'iff' description of the tuning residual (NDN) (too narrow); corrected residual (Fix 6).
SKETCH (as labelled, plausible): Theorem M-inf (items: G2, D2, Theorem B with pinned faces, joint fixed point); (E3)(c) ((SC) along the
raise: precise gap, Fix 7); (E4)(ii).
No counterexample; density, Lemma Z: OPEN.

## 1. Design SLD^star.  PROVED.
(B*) U k_s := mu*_s e_s, mu*_s = 2^{-2^{2^s}}: compact, dense range, U^* injective on l_1, ||U|| = 1/16.  (W*) n^w_l := ceil(l 2^{l^3}
Omega(l) Lambda°(l)), T_hi(l) := min{T_lo(l-1), 2^{-l^3}/(l Omega(l) Lambda°(l))}, Omega = Omega_K Omega_log as in U2 1.1; all ingredients are
fixed at stage l before the window parameters; c_{l+1} := min{c_l/4, T_lo(l)^3}.  thm:SLD uses only allowedness (a), (b), c_{l+1} <= c_l/4;
(P3) holds a fortiori (Omega >= 8).  N-free.
Why the exponent must grow super-exponentially (for the proof of RS*): Step 1'' needs a least n with n >= A K'(l, J(n)), J(n) :=
min{J : mu_J <= x(n)^2}, log_2(1/x(n)) = L + 2n + O(log l), K' = C'_B[(1 + K*) 2^{s_max} + 2^{J}]/delta_B.  For mu_J = 2^{-E(J)} one has
2^{J(n)} ~ 2^{E^{-1}(2(L + 2n))}; a solution exists iff this is o(n) uniformly, i.e. E(J)/2^J -> infinity.  mu = 2^{-s^2-1} (E = J^2):
2^{sqrt(2(L+2n))}, no solution; mu = 2^{-2^s}: ~2(L + 2n) with slope 4A C'_B/delta_B >> 1, no solution; mu*: 2^{J(n)} <= 2 log_2(2 log_2(1/x)).
Fix 2 (T_final^*, PROVED as a design statement).  For the D_Omega/D^{V2} version: B_mu*(l) := 2^{d(l)}/(delta_min(l) (mu*_{d(l)})^2) with
d(l) := sigma(l) + 2^{l+2} (the first three coordinates of every S_{l''}, l'' <= l, beyond s_max(l) lie in (s_max(l), d(l)]), and omega(l) must
count the new rate objects of level l: |a_s| (s <= d(l)), ratio spreads |1 - rho_s/rho_{s'}| of those triples, and the regularity
determinants of Fix 6 (finitely many, N-free, design-indexed); Theorem 2' (clean sub-windows) and admissibility are unaffected (only
window lengths and the base change).

## 2. Lemma P.  PROVED.
Statement.  Any SLD-type T, any row f' with forced data (a', z', ...), F' = supp a', a functional g' with g'(xi') = 0 and p*(f' + r g') <=
1 + (1 + eta')r^2/2 at r = +-t (eta' <= 1), a two-sided decomposition at scale t in the window W(l_*), a coarse carrier l <= l_* with sign
eps_l, tau_l := -eps_l Delta theta_l, sigma := sgn tau_l, and s in S_l ∩ F' with s notin T(l_*) and s_s eps_l = -sigma.  Then
   |tau_l| v_l(s) <= 2|a'_s|/t + phi_s + |r_s|,  phi_s := f^+_s + f^-_s,  sum_{F'} phi_s <= (1 + eta')t/(2q'_0),  sum_s |r_s| <= 8t^2,   (P.1)
and if |tau_l| v_l(s) >= (16/5)|a'_s|/t then |tau_l| <= (8/3)(phi_s + |r_s|)/v_l(s) <= C_q t/v_l(s), C_q := (8/3)(1/q'_0 + 8).  For s in
T(l_*) minus the targets of ALL bad carriers, add r'_s (coarse good targets), |r'_s| <= (4/3) sum_good |Delta theta|, giving C_q(1 + 2K*).
Proof.  (P1) of thm:SLD and allowedness (a): u_l(s) = v_l(s), other signatures vanish, targets of l'' < l vanish on S_l, targets of
l < l'' <= l_* would put s into T(l_*); so Delta B(s) = eps_l tau_l v_l(s) - r_s, r_s := sum_{l'' > l_*, s in supp y_{l''}} Delta theta_{l''}
y_{l''}(s)/n_{l''}, sum|r_s| <= (4/3) sum_{l''>l_*} 6 lambda_{l''}/t <= 8 T_lo(l_*)^3/t <= 8t^2 (lem:box, (P2), t >= T_lo(l_*)).  lem:flip (its
proof uses only G_b(a' + tB_+) <= budget/q'_0, valid at every t): s_s B_+(s) >= -|a'_s|/t - f^+_s, s_s B_-(s) <= |a'_s|/t + f^-_s, so
s_s Delta B(s) >= -2|a'_s|/t - phi_s; and s_s Delta B(s) = -|tau_l| v_l(s) - s_s r_s.  Under the deep hypothesis 2|a'_s|/t <= (5/8)|tau_l|
v_l(s).  QED  (The bound needs t >= T_lo(l_*) for |r_s| <= 8t^2; all uses are in the window.)

## 3. Theorem RS*.  PROVED (V3's I1-I3 unchanged), with precisions.
Design SLD^star, every N: every f in S_{p_N*} (F arbitrary) satisfying (W*), (H2), (H3-inf), (B_fin) and (ND'_{B_np}) is in Rec.  I re-derived
U2 1.3: thresholds K_1 = (5/4)C_q[(1 + 2K*)2^{s_max} + 2^J]/delta_B, K_{i+1} = 4H(C'_f K* + |B|K_i) + 2K_i; pigeonhole; nearest point tau' of
Z_f(L') with sum|tau - tau'| <= K_{i_0+1} t/4; kept amplitudes keep sign and (3/4)|tau| <= |tau'| <= (5/4)|tau|; empty deep set (finite
target set; outside supports; pinned; kept: deep j >= J_j raised or thick (4|a^{(j)}_j|/t >= 8 C_tau v_l(j)), shallow j < J_j pinned by Lemma P);
fixed point n_j (exists; n_j = o(n^w)); footprint eps'_j <= 2 C x_j y_j <= theta_j c_flat^2 (T_j 2^{-n_j})^2 for C_e >= 8 C C_tau.
(r1) T_B must be the union of the targets of ALL bad carriers (bad-peak targets were missing from r'_s; with this definition they fall into
the finite case (i)).  (r2) T_0 includes the finite contact sets S_l \ F of B_F carriers (Z5 Step 2).
Theorem ND' (PROVED): if (ND'_{B_np}) fails, Lemma ND gives F \ T_B ⊂ union of kernel signature sets with a = (c_k/kappa) v_k there, so
sup_{l in B, j in F} |u_l(j)|/|a_j| < infinity, (H4-inf), (CS_B) by Lemma R0(a), and Theorem R1 applies without raise.

## 4. Lemma W and Theorem RS*_inf.  PROVED after Fix 1.
Lemma W (U2 2.1) is correct in mechanism: box-level deep raise R := {s in F : s >= J, |a_s| < 4 Bx_*(s)}, mass <= psi(J) -> 0, footprint <=
mu*_J psi(J); threshold pigeonhole over the coarse bad strict non-peaks; Sigma-rows for thin shallow targets; Lemma P for thin shallow
signature coordinates; R1 Claims 3.1-3.2 with D_t empty give t||b^+-||_1 <= 9, A_2 = 12, no bounded switching, no box domination, no (RR).
Fix 1 (bad-peak margins).  PROVED.  Let mu_k := q_0 Phi_m(k) theta_m (rho - 1)/m be the absolute margin of a peak (eq:margin: sigma_m
|alpha_m(k)| = lambda_k mu_k) and mu_B(l_*) := min{mu_{k(l)} : l in B_pk(l_*), alpha(k(l)) != 0}.
 Claim A.  At a row f' at which these peaks are peaks with mu'_k >= mu_k/2: for swallowing-sign non-degenerate bad peaks -lambda K_d t <= tau_l
 <= t/mu'_k + lambda K_d t; for anti-sign ones -t/mu'_k - lambda K_d t <= tau_l <= lambda K_d t (the lower bound also follows from the
 B_K sign row when S_l \ F is infinite); for degenerate anti-sign B_K peaks tau_l <= lambda K_d t, (tau_l)_- <= c(tau)/(2 m_l).
 Proof: eq:peakshift at k with Delta Theta_m(k) = -eps_l tau_l/lambda_l: sgn(w(k)) eps_l tau_l/lambda_l = |omega_+(k)| + |omega_-(k)| +
 Delta d_m M_m, with |omega_+| + |omega_-| in [0, t/(sigma|alpha|)] (lem:suplevel(c)) and |Delta d_m| M_m <= K_d t (lem:badpeaks(a)).
 Claim B.  If the raise moves values by <= eps_e and block scalars by <= C_f eps_e and C eps_e <= mu_B(l_*)/2, every coarse non-degenerate bad
 peak stays a peak with mu' >= mu/2.  Proof: rho - 1 = m mu/(q_0 Phi theta) is Lipschitz in the value and in theta (Lemma T).
 Consequence: in Lemma W replace C'_f by C'_f(1 + l_*/mu_B(l_*)); in RS*_inf use Xi_f(l) := (4H(l)l + 3)^{l+2}(1 + K*(l)) C_VP(l)/(gamma_B(l)
 mu_B(l)) and choose J with C mu*_J psi(J) <= min(x_j^2, mu_B(l_j)^2/4).  For B finite (RS*) mu_B is an f-constant: nothing changes.
Precisions: (W2) H(l_*) := C_H(l_*) max(1, C_0(l_*)), C_0 ~ max 1/(2 m_l(l_*)) (eq:hoffman's conversion of the cost c(tau)); (W3) T_0 includes
the contact sets of coarse B_F carriers; (W4) t_1 >= c/c_flat (all r-conditions of lem:onesidedtransfer/R2 are conditions on r = c_flat t
with f-constants persisting along companions), so U2's "t_1 >= c' gamma_B^2" is unnecessary; (W5) VP' radius ~ C_VP^{-2} is met by x_j^2.
Theorem RS*_inf (with Fix 1): design SLD^star, N >= 1; if (H2), (H3-inf) for all bad carriers, (ND'_{B_np(l)}) for every l and
liminf_l Xi_f(l)/(l 2^{l^3} Lambda°(l)) = 0, then f in Rec.  PROVED (U2 2.2 with Fix 1; the fixed point J -> K_top(J) -> n(J) -> P(J) ->
x(J) -> J° has a least solution because mu*_J is doubly exponential in 2^J while the right side is linear in 2^J).

## 5. Fix 5: RS*_inf without (ND').  PROVED conditional on the kernel rate.
If (ND'_{B_np(l_0)}) fails (then it fails for all l >= l_0), Lemma ND gives kernel carriers k (finitely many) with a = (c_k/kappa) v_k on
S_k ∩ F \ T_{B_np(l_0)}, and F \ T_{B_np(l_0)} ⊂ union S_k.  For l_* >= l_0 large, R = {} (no raise, no VP, f' = f).  Put S^hat_k := S_k ∩ F \
T_B(l_*), m^F_k(l_*) := ||v_k 1_{S^hat_k}||_1, and require K_1 >= 3 C_q(1 + 2K*)/m^F_k(l_*).
Claim: every kernel carrier has |tau'_k| < (15/4)|c_k/kappa|/t, and the deep set is empty.  Proof: on S^hat_k the sign of a is constant; if
aligned with the switching, s_s X'_s >= 0; otherwise summing (P.1) over S^hat_k (good-target corrections included) gives (|tau_k| - 2|c_k/kappa|/t)_+
m^F_k <= t/q_0 + 8t^2 + (4/3)K* t, so |tau_k| >= 3|c_k/kappa|/t would give |tau_k| <= K_1 t, contradicting "kept"; pinned carriers have tau' = 0.
At j in S_k ∩ F ∩ T_B(l_*) \ T_{B_np(l_0)}: the non-kernel part of X'_j is <= (15/2) sum_{l > k, j in supp y_l} lambda_l |y_l(j)|/(n_l t) <=
5 2^{-2j} delta_k/t (allowedness (b)), and (1/4)|c_k/kappa| v_k(j)/t >= 5 2^{-2j} delta_k/t once 2^j >= 20 n_k |kappa/c_k|; the finitely many
remaining coordinates of F (fixed, |a_j| > 0) are thick on the windows of large levels (K_top T_hi -> 0); coordinates of S_l ∩ F for non-kernel
bad l lie in T_{B_np(l_0)} (finite).  QED
So the corner case of U2 4.2(b) is the rate max_k 1/m^F_k(l) (to be added to Xi_f); it is absent when F ∩ S_k has bounded gaps beyond s_max(l)
(then 1/m^F_k(l) <= C_k 2^{s_max(l)}/delta_k is absorbed by Omega_K).  OPEN unconditionally for very sparse F ∩ S_k.

## 6. Lemma DR-inf; Fix 3 ((R6)), Fix 4 (J > d(l)).
DR-inf (PROVED for (R1)-(R5), (R7), minors): z, F, K unchanged; ||e^r - e|| <= 2||U^*Delta a||/nu <= C mu*_J psi(J) <= C b^2 Phi_min; values,
block scalars, rho (absolute change for tiny, relative for robust), ray components (<= C b^2), singular values (Weyl), minors (Lip(l) C b^2)
move by <= C Design(l) b(w)^2 <= b(w); compatible with V2 Theorem B's (A1).
Fix 3 (PROVED): for every fixed shift pattern pi, c_pi depends only on (F, z|_{F^c}) and design data (V1 2.5); the raise changes neither F nor
z, so c_pi(f^r) = c_pi(f): U2's flagged item "(R6) continuity" is resolved (no SKETCH).
D2 (SKETCH): V2's shift-pinning rate rho^sh (Def. 3.2) is an infimum over unbounded tau with value-dependent coefficients; with V2's
convention (q' := 0 for nearly neutral carriers, other coefficients robust) minimizers are bounded by (Design/u)^C and rho^sh moves by <=
(Design/u)^C b^2 <= b.  Needed only for "w clean for f => clean for f^r" in case (I) of Theorem C1; M-inf reads (C*) at f^r anyway.
Fix 4 (PROVED): take J(w) := max{J°(w), d(l) + 1, s_max(l) + 1}, J°(w) := min{J : C mu*_J psi(J) <= b(w)^2 Phi_min(l)}.  Then no coordinate <=
d(l) is raised (the rate objects |a_s|, s <= d(l), keep their tiny/robust status up to lambda in [1, 1 + psi(J)]), the pinning constant of
Lemma P is <= C_q(1 + 2K*) max(2^{J°+1}, 2^{d(l)+2})/delta_min(l) = (design) x O(log n(w)), absorbed by Q(w).  Without this, raised
coordinates in [J, d(l)] carry moduli 4 Bx_*(s)/lambda (design numbers times c_{l''} >> b(w)) that are not rate objects of f (for the first
sub-window of a level they can lie in the band (b(w), u(w)) = (b(l,1), b(l-1,M(l-1)))), so TR-inf's case analysis is not controlled there;
moreover their ratios rho^r_s = 4 Bx_*(s)/(lambda v_{l''}(s)) = (4/lambda)(lambda_{l''} + finer-target terms/v_{l''}(s)) are nearly constant
along S_{l''}: the raise itself manufactures a spread-free (proportional) profile, i.e. raised coordinates are useless as pair resources.

## 7. Lemma TR-inf.  PROVED (cases (a), (a'), (c), (c')), with precisions.
First-order formula (diagonal U, z fixed, A = a + Delta e_s): d e/d Delta = (mu_s/nu)(k_s - (mu_s a_s/nu) e), so d val_k/d Delta =
(mu_s^2/nu)(u_k(s) - gamma_k a_s/nu^2), gamma_k = <U^*u_k, U^*a>.  Pair (c): alpha_s Delta + alpha_{s'} Delta' = 0 (alpha_s = mu_s^2 a_s/nu^2)
cancels the common term; private effect (mu_{s'}^2 v(s')/nu)(1 - rho_{s'}/rho_s) Delta'; |Delta| <= u^{-1}|Delta'| since mu* decreases.
Anchor (c'): Delta_0 := -sum alpha_{s'} Delta_{s'}/alpha_{s_0} with s_0 <= every tuned s'.  (a): Lemma TU needs only j, j' off the support
(Lemma B (3.1) holds for any A^0 in l_1).  (a'): lowering a tiny support coordinate to a contact costs 2|a_j| and moves e by <= 2 mu_j|a_j|/nu;
the later bank/pull mass returns it to the support (exact swallowing off F^# intact); after the deep raise every raised pull coordinate is
automatically convertible (|a^r_j| <~ eta << theta b^{1/2}).
(T1) Scale: e moves by ~ eta/(mu_{s'} v(s')); second-order common motion ~ eta^2/(mu_{s'}^2 v(s')^2) <= Design^2 eta^2 << b.
(T2) Design(L) >= (mu*_{d(L)})^{-2} 2^{d(L)}/delta_min(L) (Fix 2).
(T3) Anchor-met carriers outside L_0 move at FIRST order by <= C_T eta; harmless since every carrier of a tiny object lies in L_0, the others
are robust (Lemma RR) or non-exact nearly neutral, and C_T eta << Lam = T_lo^3 (Lemma ST buffer).
Joint solution: private (block-diagonal) first-order Jacobian, second-order terms <= Design^2 eta^2: quantitative inverse function theorem.
Numerics (tr_inf_joint3.py, 600 digits, base 2^{-(s+2)^{1.6}}, all coordinates in F, three tuned carriers jointly): residual/eta <= 1e-164;
untuned carriers move by eta^2 x (1e63..1e66) (second order, consistent with T1); off-diagonal/diagonal Jacobian ratio 1e-1, 1e-5, 1e-13 for
eta/eff = 1e-4, 1e-8, 1e-12 (first-order privacy); case (c'): anchor-met carriers move ~ 1e4 eta (first order, ~ eta u(s_0)/v(s')).

## 8. Fix 6: the tuning residual.  FALSE 'iff' corrected; residual OPEN.
U2 3.3 claims: no resource iff (N1) & (N2).  FALSE: a carrier with thick bank coordinate j' in F, off-F pull coordinates (contacts of sign eps),
tiny pair spreads and no anchor has no resource of (a), (a'), (c), (c') (pulls only LOWER eps.val), but (N1) fails.  Correct formulation
(PROVED as a reformulation): the first-order resource map R (private two-sided columns of (a), (a'), (c), (c'); one-sided pull columns;
single-support columns (mu_s^2/nu)(u_k(s) - gamma_k a_s/nu^2)_{k in L_0}, s robust in S_{l''} ∩ F ∩ (s_max, d(L)]) must map the move cone onto
R^{L_0} with a right inverse of norm <= (Design/u)^C (Robinson regularity); then quantitative Graves gives exact two-sided tuning, the
first-order motion of non-L_0 carriers caused by single-support columns being admissible by (T3).  The regularity modulus is a finite
minimum of determinantal quantities in (a_s)_{s <= d(l)} and values: a rate object; robust => tuning; TINY => the tuning residual (contains
U2's (NDN), where only single-support columns exist and the modulus is the Sherman-Morrison determinant |1 - sum rho gamma/nu^2|).
Numerics (sm_check.py): det of the single-move Jacobian = det(D)(1 - sum rho_k gamma_k/nu^2) to 8 digits; for a|_F in span{u_k|_F} the
denominator vanishes and sum c_k Delta val_k = -kappa nu ||e' - e||^2/2 holds exactly (12 digits) for a general move on F, as <U^*(sum c u), e>
= kappa nu <e, e'> (diagonal base).

## 9. Theorem M-inf.  SKETCH (agree), with the corrected item list.
Plausible route: deep raise (Fix 4 depth) -> V1/V2 moves at f^r with TR-inf resources -> transplant -> E_RT + Y3 Theorem 2.1.  Checked: window
arithmetic (thresholds (4Hl + 3)^{l+2} with H = C_f^l Design^2/u dominated by Q(w) and 2^{l^3}); (S1) of Lemma W automatic at clean
sub-windows (tiny |a_j| <= b <= t^2, robust >= u >= K_top t^2); Lemma ST with anchor side effects (T3).  Open inspection items: (G2) V1's
Prop. TR copies B_+ 1_F and uses lem:finitebase (F finite): re-run with R1's clamped base data (|b^+_1| <= A_j + |X_j|) and Lemma P at the
decomposition row (Lemma P holds at any row; cushions at f^# dominate those of the decomposition row on raised coordinates and equal them up
to lambda on unraised ones; tuned robust coordinates and pulls/banks as in V1 Prop. TR(iv)); (D2) rho^sh under the raise; V2 Theorem B with
Lemma W's pinned faces (faces are subsystems; V2 lists their minors); joint fixed point of TR-inf with V2's buffer push; constant: raise to
8 Bx_* because V1's box rows allow |tau'| <= 12 lambda/t.  Residual list of M-inf: (C*) at f^r, the tuning residual of Fix 6 (not only (NDN)),
failure of (H2), degenerate swallowing-sign bad peaks without donor resources.

## 10. (E3), (E4).
(E3)(a) PROVED for RS*, RS*_inf (data at the companion, d-rows in the cone, I_- = {}); for M-inf conditional on M-inf.  (b) PROVED (D in Y,
Y ∩ c_00 = {0}, L^* injective on bounded block families).  (c) Fix 7 (precise gap): Scr^{f^r}_m(s) <= Scr^f_m(2s) only for s >= C eps_e;
(SC) at the fixed row f^r as s -> 0 is not implied; what is needed is its quantitative form on the construction scales of one window
(plausible since eps_e <= b^2 << T_lo^2): OPEN/SKETCH.
(E4)(i) PROVED (Theorem ND'; level-by-level version: Fix 5).  (E4)(ii) SKETCH: degenerate swallowing-sign bad peaks are (K4) carriers (or
dropped in one-signed blocks) at clean w; V1's donor raise needs a resource for a robust-margin donor; single unpaired support raises are
NOT admissible (PROVED: common motion gamma_k rho_s Lam/(nu^2 lambda_c) >> b), pairs/anchors are (second order <= T_lo^6 Design^4 << b).
OPEN when every donor of the block has a tiny resource modulus.

## 11. What remains open
Density of NA((c_0,p_N), l_2^2) for every N, Lemma Z, density for Martin's p: OPEN.  Infinite F, designed norm:
 - RS-type rows (finitely many bad carriers, any profile): RECOVERED (PROVED).
 - Infinitely many bad carriers: PROVED under (W_inf) with 1/mu_B(l) (and the kernel rate if (ND') fails); unconditional only via M-inf.
 - M-inf: SKETCH (items G2, D2, Theorem B with pinned faces, joint fixed point).
 - Infinite-F residuals: tiny tuning-regularity modulus (Fix 6); donors without resources ((E4)(ii)); (SC) along the deep raise ((E3)(c)).
 - Shared with finite F: (C*) and its gaps (C*-1)-(C*-5); failure of (H2).
