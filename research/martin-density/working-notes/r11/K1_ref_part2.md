# K1 referee, part 2: Section 2 of K1 (item (O-b)): Lemma K1.4, the offset correction, the audit, Sys-A/Sys-DC, (LR), Lemmas K1.5-K1.7

## 2.1 Lemma K1.4 (first-order action of (P1)-(P6)).  Verdict: CORRECT for (P1)-(P5); (P6) see 2.3 below.
 (P1) Z-con/Z-gen: z-moves change no e; slope 1; only fine carriers meet near coordinates of S_l beyond s_max(L) (allowedness (a), (c)).  Lowering
      a thin near coordinate: cost <= C_f b, e moves by <= 2 mu*_s b/nu.  OK (done in Step 0; Step-0 displacements must stay inside (D1), see R-8).
 (P2) The sign facts are right: a near off-F coordinate of a data-carrying carrier is a contact of the data sign (cone row (X1), aggregated as in
      U1-ref 4.2: a free near coordinate forces gamma_l = 0); a thin near coordinate of a data-carrying carrier has s_s = eps_l (Lemma K1.3 (S) gives
      |c_l| <= 4b/(t v_l(s)) <= 4 Design T^3 < K_*^2 K t/(4D) for t >= T, contradicting Lemma K1.2).  TU two-sidedness: the pull gives a genuine
      NEGATIVE shift (z flip) and the bank a nonnegative one, so the net range is [-d_p, +infinity) with d_p >= v_l(j_p)/2: two-sided around 0.
 (P3) U2 TR-inf (c): the compensating move is placed at the SHALLOWER coordinate (dA(s) = -(mu_{s'}^2 a_{s'}/(mu_s^2 a_s)) dA(s'), tiny), the efficiency
      is (mu_{s'}^2 v_l(s')/nu)|1 - rho_{s'}/rho_s| >= u/Design.  [With the doubly exponential base the other orientation would require astronomically
      large moves; the refereed lemma uses the right one.]  OK.
 (P4), (P5): Jacobian eps_k d val_k = delta_{kl} - g_k h_l (Q2 4.0, Q2-refa C.1, numerically confirmed there).  OK.
 (f): resource moves of size x in value units move e by <= mu_s Design x.  OK.

## 2.2 Correction (C2) to Q2-refa C.3 (bank with offset).  Verdict: CORRECT (K1's finding stands).
Re-derivation: the offset mass m_0 at the private contact of k* raises u_{k*}(xhat) by eps m_0/beta_j at first order, hence A_{m*} by pi m_0/beta_j, hence
F(0) by -pi p_{m*} m_0/beta_j.  Applying the left null vector y of the degenerate square part to F(0) + N P - pi p_{m*} P_0 = 0 gives
pi (y^T p_{m*}) (m_0/beta_j + P_0) = y^T F_orig(0): the TOTAL bank position is forced, its sign is that of y^T F_orig(0)/(pi y^T p_{m*}), uncontrolled.
Q2-refa C.3(iv) treated only the first-order common mode h_0 of the offset, not the zeroth-order shift of F(0).  (K1's "4K|pi p| > 1" should read
"4K^2 |pi| |p_{m*}|_inf > 1 + 2K|F_orig(0)|/r"; immaterial.)  Numerics: K1's linear check re-run (identical); referee's NONLINEAR check
(K1_ref_work/ref_offset_nonlinear.py: quadratic remainder, SLSQP with the bank constraint): in all 23 instances with negative forced position the
minimum of ||F||^2 over the one-sided domain stays >= 0.52 (y^T F_0)^2, while the two-sided control reaches <= 4.5e-13.
REPAIR (K1): TU on the peak (pull + bank) is two-sided (net range [-d_p, infinity)); (P1) if Delta_{m*} = 0; (P3) on the peak (first-order common mode
cancelled).  CORRECT for these three.

## 2.3 (P6) realized by an S-mass lever (P4) on the peak.  Verdict: K1's claim "Q2-refa C.3(iv)'s rank-one perturbation argument applies verbatim"
## is FALSE; the correct bordered scalars differ.  [R-7, fixable.]
C.3(iv) needs h_0 ||gt||_inf K <= 1/2 (small common mode).  A thick S-mass step on the peak has h_{k*} = |A(s)|/(nu |u_{k*}(s)|) = O(Design/u), NOT small.
Referee derivation (Q2 Prop. 4.1's proof with the column -(pi p_{m*} + h0 g)): seek P = D^{-1}(b + g alpha + sum_m p_m gamma_m) with alpha := h^T P + h0 P_0,
gamma_m := q_m^T P (m != m*), gamma_{m*} := q_{m*}^T P + pi P_0.  The m != m* equations give gamma_m as in Prop. 4.1, P_0 = [(1 - q_*^T p_*) gamma_* -
q_*^T D^{-1} b - (q_*^T D^{-1} g) alpha]/pi, and the remaining scalar equation is
    c'_alpha alpha - beta'_* gamma_{m*} = rhs - (h0/pi) q_{m*}^T D^{-1} b,
    c'_alpha := c_alpha + (h0/pi) q_{m*}^T D^{-1} g,      beta'_* := beta_* + (h0/pi)(1 - q_{m*}^T p_{m*}).
So L is onto with an explicit right inverse of norm <= K(beta_0) when max(|c'_alpha|, |beta'_*|) >= beta_0 (Prop. 4.1's bounds with H replaced by
H + |h0|/|pi|); for one block and N exactly degenerate, c'_alpha = (q^T D^{-1} g/(1 - q^T p)) beta'_*, so L fails to be onto exactly when
h0 = -pi beta_*/(1 - q^T p).  Numerics (K1_ref_work/ref_bordered.py Part B, ref_p4_peak_scalars.py): explicit inverse residual 3e-15 over 3000 random
multi-block instances; in 2797 exactly degenerate one-block systems with ROBUST Q2 scalar (s_min[N | -pi p] >= 1.4e-2) the (P4)-type column with
h0 = -pi y^T p/y^T gt (median |h0| = 0.66) is NOT onto.  FIX: for a (P4)-type (P6) put (c'_alpha, beta'_*) (for the finitely many lever assignments of level
L) into (R-lev) and require max(|c'_alpha|, |beta'_*|) >= u in Lemma K1.5(b2).  Side remark (PROVED by the same formula): in Q2's doubly degenerate case
c_alpha = beta_* = 0, a (P4) peak lever with h0 != 0 has beta'_* = (h0/pi)(1 - q^T p) != 0 and IS a valid bordering (1577/1577 random instances); but
in the EXACT full degeneracy with kappa != 0 peaks have no thick near coordinates (Q2 Lemma 4.3(c), Q2-refa C.4(2)), so this does not resolve (O-c).

## 2.4 The audit table (K1 2.3).  Verdict: CORRECT as an inventory; two omissions.
Checked against Q1 CM^tr Step A/B, X1 KN^tr Steps 0-4, X1-ref 8, U1-ref Prop. KN, X2 Lemma LV, Q2 3.3/4.2, V1 (C1)-(C3): (C3) is not on route V's tree
(Q1 2.2: Step 0 = (C1), (C2) and weak-peak pushes); (C1), (C2) act off F; the DC pull window [r, 2^{3G} r] lies far below Step A's window (r <= K_w s_1);
the coordinate bookkeeping (<= 2 + 2 near coordinates of six; disjoint far windows; disjoint signature sets) is right.
 OMISSION R-8 (Step 0's weak-peak pushes are not covered by (LR)).  In (T)-blocks, Step 0 pushes every ACTIVE weak peak k inward by <= 2b theta Phi_k/m
   BEFORE the Lojasiewicz step.  The audit lists the replacements (far pull, (P3)/(P4) lowering, (P1)) but the definition of (LR) (2.4) involves only
   Sys-A and Sys-DC, and Theorem 5.1 assumes nothing about Step 0.  An active weak peak is data-carrying; its data sign is eps_k = -sgn(Delta''_m) vs_k,
   so a near bank lowers vs_k val_k (the push direction) iff Delta''_m > 0; for Delta''_m < 0 the push needs a pull, (P3) or (P4).  If none exists the
   push is impossible and Step A cannot start.  Moreover a (P4) push has a first-order common mode of size h * 2b theta Phi/m <= C Design b/u, which moves
   every rate object by Design^C b/u > b: (D1) (the Lojasiewicz radius condition C_L((1 + Lip C_*) b)^{2/N_L} <= eta'/3) must be enlarged to
   C_L((1 + Lip C_*) Design(L)^C b/u(w))^{2/N_L} <= eta'(w)/3 -- legitimate since u(w) = b(w^-) is fixed before b(w) -- and robust objects survive since
   Design^C b/u << u (b <= T^4 << u^2).  FIX: (a) add to (LR_{w,a}): "every active weak peak of a (T)-block has a push resource: a pullable far coordinate
   at the scale 2b theta Phi/m, (P3), (P4), or a near bank when Delta''_m > 0"; (b) add the enlarged (D1) to (D-K1).  Since a weak peak without such a
   resource is, after a hypothetical push, a (U)-type tuned carrier, the non-lever-regular class of 4.3 changes only by listing these peaks.
 OMISSION R-9: (P6) via (P4) (2.3 above).

## 2.5 Sys-A in ratio form; the definition of (LR).  Verdict: Sys-A CORRECT; (LR) is a coherent DEFINITION (not a theorem) once R-8 is added.
Re-derivation of J_A: ratio rows times kappa: d val_l - rt_l d kappa_m; d val = (I - g h^T) dP (+ private parts); peaks move by the common mode only,
d|zeta(c)| = lambda_c vs_c d u_c, d kappa_m = (1 - X_m) sum_c d|zeta(c)| + O(X) = -G_m h^T dP + (1 - X_m) lambda_c ds_c, G_m = (1 - X_m) sum_c lambda_c vs_c
eps_c g_c.  Hence J_A = [I - g~ h^T | col_c], g~_l = g_l - rt_l G_{m(l)}, col_c = -(1 - X) lambda_c rt^{(m(c))} - h_c g~ (U1 Lemma 1.4(a) for d kappa/ds).
Correct.  Why all coarse non-peak ratios must be held once a common mode is used: correct (U-block statuses have margin eta' only; R^2 in Lemma K).
Kappa may float: correct -- the cone (X3)/kappa, Lemma K and the true shift (Delta'' = sum r^# gamma = Delta' at exact ratios) use ratios only; PM uses
normalized values u/A_m, frozen by Lemma DC.  (LR) as defined is evaluated at the selected (w(L), a(L)); it is window dependent (far availability),
hence a HYPOTHESIS, not a rate object -- K1 says so correctly ("up to the availability of far resources").  Precision: the class a(L) should be
"some class with >= n(w)/D_cl scales" (the pigeonhole may return several).

## 2.6 Lemma K1.5.  Verdict: (a) CORRECT; (b1) CORRECT; (b2) CORRECT for private (P6), INCOMPLETE for (P4)-type (P6) (R-7); (c) CORRECT once
## "tuned" includes the Step-0 weak peaks (R-8).
(b1) re-derived: P = b + g~ alpha - col_c P_0, (1 - h^T g~) alpha + (h^T col_c) P_0 = h^T b; with 1 - h^T g~ tiny take alpha := 0, P_0 := h^T b/(h^T col_c):
the bound ||P|| <= ||b||(1 + ||col_c|| ||h||_1/beta) does not involve 1 - h^T g~; h^T col_c = -[(1 - X) lambda_c h^T rt^{(m)} + h_c] + h_c(1 - h^T g~).
Numerics (ref_bordered.py Part A): identity to 4e-14, explicit inverse residual 1.8e-12 over 3000 exactly degenerate instances.  An anchor column -g~
gives h^T(-g~) = -1 + O(tiny).  The design bounds |g| <= ||U||, |h| <= Design/nu, |rt| <= Design^2: OK.
(a): with private levers only, N_DC = D - sum_m p_m q_m^T (no h-term), invertible with ||N^{-1}|| <= 1 + 2 max ||p_m|| ||q_m||_1 (q^T p <= 1/2): correct.

## 2.7 Lemma K1.6 (realization under (LR)).  Verdict: CORRECT up to R-6 (cost) and R-8 (Step 0).
Poincare-Miranda on G(y) = F_A(0) + y + Rem(R_b y): needs ||R|| |F_A(0)| <= rho_A/2 and C_2 ||R||^2 rho_A <= 1/4 (K1 writes C_2||R|| rho_A; with
rho_A = 2||R|| C Design eta' the needed inequality is Design^C u^{-C} eta' <= 1/4, true since T <= (u/4Design)^{omega+20} and C <= 4 omega for L large).
kappa is continuous in the parameters (U1-ref 1), so G is continuous.  Cost: Step-A resource moves <= Design^C eta'/u (fine); the far moves of the TU
levers and the in-F lowerings are NOT bounded by "2T^2/(L Design)" in a way usable by E^eng (R-6: needs x'_max).
(B) Lemma DC^inf under (LR): Q2 Cor. 4.2's proof with R from (LR); S-mass range |P| <= K_lev r keeps |A(p)| >= |A_1(p)|/2 under (LATE) (Q2-refa (p2.2));
DC pull coordinates in F must be lowered at the pre-row: cost <= 2(1 + ||U||) x'_max per lever, inside theta' (R-6).  OK.

## 2.8 Lemma K1.7 (structure of non-(LR) configurations).  Verdict: (i) FALSE AS STATED (missing type); (ii) correct for the corrected type;
## (iii) OVERSTATED.  [R-10, R-11, fixable.]
(i) Case analysis of a carrier l without (P1), (P2), (P3):
   - N_l ⊂ F_thick (all pairwise spreads tiny): (S).
   - N_l contains an off-F/thin coordinate: l is data-carrying (else (P1)) and has no pullable far coordinate (else (P2)).  If N_l ∩ F_thick = {}: (U).
     If N_l ∩ F_thick != {} (no robust-spread thick pair): l has (P4) but is NEITHER (U) (it has a thick near coordinate) NOR (S) (not all near
     coordinates thick).  Call it (M) MIXED.  K1's proof notices this ("such carriers do not by themselves break (LR)") but the statement of (i), of 4.3 and
     of the Characterization omits it.
   CORRECTED (i): every non-privately-tunable tuned carrier is (U), or (S') := "(P4) is its only two-sided private resource" = (S) ∪ (M).  (ii) and the
   bordered analysis of K1.5(b) apply to (S') verbatim (they use only the (P4) column).  (iii)'s exact-limit structure applies to (S') carriers too.
(ii) correct for (S') (if all non-private carriers are (S'), (LR) fails only if no anchor exists and every bordered scalar of K1.5(b) is <= b; for Sys-DC
   additionally N degenerate, i.e. the square system itself is singular -- implicit in "(LR) fails"), with R-7's scalars for (P4)-type (P6).
(iii) The vanishing "y^T(values) unchanged by every support move at s in F" is implied by "no usable resource" only at USABLE coordinates, i.e. s in
   F_thick ∩ [1, d(L)] (thin coordinates move y^T(values) only proportionally to A(s); coordinates beyond d(L) have efficiency mu*_s^2 v negligible).  So
   the exact limit gives u_h(s) = kappa a_s for s in F_thick ∩ [1, d(L)] only, not P_F(I - e e^T)U* u_h = 0 on all of F; Q2 Lemma 4.3(b) ("F ⊂ supp u_h")
   and U2 Lemma ND's conclusion on all of F do NOT follow.  Correct version: if kappa != 0, then F_thick ∩ [1, d(L)] ⊂ supp u_h and a_s = (h_l eps_l/kappa)
   v_l(s) on F_thick ∩ N_l (= the "no anchor" + proportionality statement).  This is a remark-level statement; label it HEURISTIC/structural, or restrict
   as above (then PROVED).
Remark (1) (U) is new: CORRECT and well explained (deep anti-sign support or super-thickness; z cannot move inward at data-carrying contacts; deep
   masses have negligible efficiency).
RATIO TRICK (SKETCH): the linear algebra is right (du_l = kappa delta_l + rt_l dkappa >= 0 for dkappa >= kappa max(-delta_l/rt_l) when rt_l > 0 on the
   (U)-carriers of block m, provided the block has a two-sided buffer-peak resource and its other carriers are two-sided); the nonlinear realization
   (a degree/Brouwer argument on a cone of parameters) and the Sys-DC analogue (A_m in place of kappa) are not written.  SKETCH label honest.
