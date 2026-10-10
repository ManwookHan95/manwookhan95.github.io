# K1 referee, part 1: Section 1 of K1 (item (O-a)): Lemma K1.1, deep raise, Lemma K1.2, Lemma K1.3, Proposition K1.A, Corollary K1.B

Sources re-read for this part: r11/K1_notes.md 1.0-1.5; r10/Q1_notes.md 2.2-2.6 (CM^tr, BR, PM, S2c^tr, C^tr); r10/Q1_referee_a.md + Q1_refa_notes 2.7-2.9
(P2, P6, P8); r10/Q2_notes.md 2.2-2.5, 3.2; r10/Q2_refa_notes.md B.1, B.2, C.7; r8/U1_notes.md 1.1-1.5, 2.1-2.6, 4.1-4.3; r8/U1_ref_notes.md 4;
r8/U2_notes.md 1.2 (Lemma P); r5/Z5_ref_notes.md 2 (Claim 3.1); r9/X2_notes.md 3.1-3.5, 4.1 (E^eng, with (E-d)); r9/X2_ref_notes.md 3-4.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.  "R-" numbers are this referee's items.

## 1.1 Lemma K1.1 (route V needs no cube normalization).  Verdict: CORRECT.
Where the common shift was used before: U1 Proposition 2.2(c)-(e) normalizes the scales of a class onto ONE ray Delta'^* so that (i) the fine
structure of U1 Part 4 (configuration (ii): Schauder completion) is built for one ray and (ii) the averaged exact data have one shift (route X,
Theorem E with exactness of the averaged data).  Route V averages at the norm-attaining approximant (X2 Theorem E^eng, Remark (a) after it:
"no exactness of the averaged data ... is needed"), and Theorem UE uses per-piece shifts (I_- := {m : Delta_{i,m} < 0 for SOME i}, (U7) per piece).
Checked items:
 (1) Static ownership (if Step B is kept): U1 Lemma 4.1's rules use only sigma_m = sgn(Delta''_m), eps_l and Y_k (a function of z, not of the data);
     U1 Lemma 4.2 (dominance) is stated "for every Delta'' in the class ... and every gamma(t) of the class" (verified in U1_notes 4.3, lines 499-516).
     So Step B is shift-magnitude independent in configuration (i).  Q1-refa P2's remark "Step B is built for the ray Delta'^*" therefore refers
     to a convenience, not a necessity.  Moot anyway after Lemma K1.S.
 (2) True versus reference shift: per scale.  In K1's ratio-form Step A all coarse non-peak ratios are exact at f^#, so Delta'' = Delta' exactly
     (the trace terms tr_j of 1.4 then vanish; keeping them is harmless).
 (3) Kind [3]: U1-ref 4.1 shows every point of the cone is inward with the true shift; the increment was one more cone point.
 (4) Window family: (U1)-(U7) are per-piece; E^eng averages functionals.
 (5) The Gamma estimate: without increment the - side differs from the decomposition's only by projection/zeroing errors; the additive error
     is K_data t (K_data = J K_*^{J+1} K, the zeroing threshold A_{i(t)} K t enters), not literally "K t" -- notation only; (U1) then needs
     K_data T_hi -> 0, which is (E-d).
Class count D_cl = (J_Om + 1) 3^{J_Om} (U1 2.3).  PROVED.  Remark K1.1' (cube increment can break cushion domination) is correctly labelled
HEURISTIC: the increment is a nonnegative combination of extreme rays with coefficients ~ eps independent of t, and the enlarged cone has no row
at shallow anti-sign support coordinates of S_l outside T(L), so nothing bounds the increment there by |a_j|/t.

## 1.2 Deep raise and the choice of J(w).  Verdict: CORRECT (two notational precisions).
 * R(J), Delta a, lambda_r as stated; raise mass <= 8 sum_{j>=J} Bx_L(j) <= 8 sum_{l<=L} lambda_l delta_l 2^{1-J}/n_l (targets lie below s_max(L) < J),
   so lambda_r - 1 = O(2^{-J}) -> 0 as L -> infinity (J >= d(L) + 1).
 * Rate objects under the raise: values and block data move by O(mu*_J) (z unchanged, ||e^r - e|| <= 2||U* Delta a||/nu <= 16 mu*_J/nu).  The moduli
   (R-mod) |a_s|, s <= d(L) < J, change by the COMMON FACTOR 1/lambda_r (relative change O(2^{-J}), NOT O(mu*_J) as 1.2(c) says); this is harmless:
   tiny stays tiny, robust >= u/lambda_r >= u/2; spreads rho_s/rho_s' and h = |A(s)|/(nu v_l(s)) are scale invariant.  [Precision R-1.]
 * J(w) estimate: mu*_J = 2^{-2^{2^J}}; the least J with C_f mu*_J log(e/mu*_J) <= min{theta_w T^2, b^2 Phi_min/(C Design)} satisfies
   2^{2^{J-1}} < C log_2(1/(b^2 Phi_min T^2)) <= C Design(L) log_2(1/T) (b is a design power of T), hence 2^{J(w)} <= 2^{d(L)+1} + 2 log_2(C Design(L) log_2(1/T))
   <= Design(L) + 2 log_2(C n(w)) (log_2(1/T) <= 3 n(w); Design(L) >= 2^{d(L)}/mu*_{d(L)}^2).  K1 omits the b-dependence (writes log_2(8 log_2(1/T)));
   the final bound is right.  [Precision R-2.]
 * The |g_j| term of Q2's raise level is indeed unnecessary: the deep assignment gives s_j b^+_1(j) >= -A_j whatever g is (Z5-ref Claim 3.1(ii)),
   and the closeness of b^+_1 to B_+ 1_F uses only flip budgets and switching errors.  PROVED.

## 1.3 Lemma K1.2 (data coefficients track actual coefficients).  Verdict: CORRECT WITH A CONSTANT SLIP (fixable).
Re-derivation (classes read off the decomposition, U1-ref 4.5): for an active component |x_dec,l| >= A_{i+1} K t = K_* A_i K t; zeroing moves the
vector by <= J A_i K t; the projection onto Gamma^#(kappa, a) moves it by <= H (K t + C J A_i K t).  So |c_l - c^act_l| <= (H C J + H + 1) A_i K t
<= |c^act_l|/5 when K_* >= 5(HCJ + H + 1).  The claimed form "|c_l - c^act_l| <= |c_l|/5" needs K_* >= 6(HCJ + H + 1): with K1's K_* >= 5(H J_Om + 2)
one gets only (HJ+1)/(4HJ+9) <= 1/4 relative to |c_l|.  Consequence for Lemma K1.3 (S): with the relative bound w.r.t. c^act one has |c^act| >=
(5/6)|c_l|, (P.2) still holds ((5/6)*4 = 10/3 >= 16/5), and |c_l| <= (6/5)(5/4) C_q 2^J t/delta_min = (3/2) C_q 2^J t/delta_min < 2 C_q 2^J t/delta_min:
the contradiction survives.  FIX: either state K1.2 relative to |c^act_l|, or take K_* >= 6(H J_Om C + 2).  [R-3, cosmetic.]
Peaks: c^act_k = -Delta'_dec lambda_k vs_k + lambda_k e_k with lambda_k e_k <= t/mu_k <= C_f D t/u (eq:peakshift, robust margin u/2 after Step 0's
weak-peak pushes); absorbed by K_*^{U1} >= C_f D/u.  Lower bound |c_l| >= K_*^2 K t/(4 D(L)) for active coarse l: PROVED (Omega: >= (4/5)A_2 K t;
peaks: |Delta''| lambda >= (4/5) K_*^2 K t/D).

## 1.4 Lemma K1.3 (no deep anti-sign set at f^r).  Verdict: CORRECT (with R-3).
Exhaustiveness of the four cases checked: j in F with j >= J (D; J > d(L) >= s_max(L), so D and T(L) are disjoint); j < J in T(L) ((Tr)/(Tt); T(L)
⊂ [1, d(L)] so (R-mod) applies); j < J, j notin T(L), j in S_l with l <= L (S); otherwise (O).  In (S) only l lives at j among coarse carriers
((P1) of thm:SLD and j notin T(L)).  Lemma P's hypotheses at f' = f^r: budget p*(f^r + r g^r) <= 1 + (1 + eta')r^2/2 on the window (raise transfer
with eps'_r <= theta_w T^2 <= theta_w t^2), s notin T(L), tail sum |r_s| <= 8 t^2 (sum_{l>L} lambda <= C T^8 <= t^3).  v_l(j) >= (4/5) delta_min 2^{-J}
for j < J.  Arithmetic: 8 > 25/4 (or 8 > 6 with R-3).  (D): |a^r_j| >= 8 Bx_L(j)/lambda_r >= 4 Bx_L(j) and |V_c(j)| <= C_f D Bx_L(j) <= 16 Bx_L(j)/t for
t <= T_hi(w).  (Tr): T_hi(w) <= 1/Q(w) <= (u/(4 Design))^{omega+20}, so 2u/T_hi >= C_f D(L).  (Tt): the decomposition violates the new contact rows
(X1^F) by <= sum_j (2b/t + phi_j) <= 2 s_max(L) T^3 + t/q_0 = O(t), so the projection error stays O(H K t); the enlarged patterns are patterns of
the same form as V1/Y1's "arbitrary contact patterns on T(l)" (G**(l)), design-countable, weight-free rows.  PROVED.
Remark: the bound on sum tr_j quoted from U1 Lemma 4.6 is not needed in K1's ratio form (Delta'' = Delta' exactly); keeping it is harmless.

## 1.5 Proposition K1.A (Q2 Prop. 3.2 corrected).  Verdict: CORRECT (constants as stated are fine; two precisions).
 (i) Deep assignment with trace slack re-derived: the interval [y - A - tr, x + A] is nonempty iff s_j V_c(j) >= -2A_j - tr_j (Lemma K1.3); its point
     closest to 0 has modulus (-x - A)_+ + (y - A - tr)_+ <= f^+_j + f^-_j + |(Delta B - V_c)_j|; (ii) s b^+_1 >= -A, (iii) s(b^+_1 - V_c) <= A + tr.
     Numerics: K1's deep_assign_check re-run (identical) and an independent check (K1_ref_work/ref_deep_assign.py, exact rational corner cases
     included): no violation.
 F_low: the projection chi_j = proj_[0,1](s_j B_+/(s_j V_c)) gives |B_+(j) - chi_j V_c(j)| <= A_j/2 + f^+ + f^- + E_j (re-derived); sum_{F_low} A_j
     <= 2|Lambda|(b + x_max)/T = O(t) (t >= T).  At a pulled coordinate t|V(j)| <= C_f D lambda_l v_l(j) t <= 24 lambda_l v_l(j).  PROVED.
 (ii) ||Delta B - V_c||_{l_1(F)} <= sum_{l<=L}|c^act_l - c_l| + 6 sum_{l>L} lambda_l/t: the first sum is <= K_data t (zeroing/projection/peak errors, with the
     thresholds A_i <= K_*^{J+1}); K1 writes "K t" in the l_1 bound and K_data in the closeness bound -- consistent once K := K_data.  [R-4, notation.]
 (iii) Cushion: |kappa| <= K t (|B_+(zhat^r)| <= t/(2q_0); |<U* B_+, e^# - e^r>| <= (C/t) Design^C T^4/u <= t since T^2 Design^C <= u);
     (s b^+)_- <= 4|a^#|/t + 2Kt|a^#| <= 5|a^#|/t; (s b^-)_+ <= 5|a^#|/t + tr + |V_f|.  The excess |V_f| + tr at support coordinates costs 2 rho |tau|
     (excess) in Exc' (no flip beyond it: same computation as Q1-refa P3), tolerated under (VT') because its mass is <= C_f Design c_{L+1} + C_f c_{L+1}^2/T.
     PROVED.  (U1): t||b^+-||_1 <= 2||a^r||_1 + C_f(1 + D t) + ... <= A_0 = O(1).  PROVED.
 Precision R-5: (U3^inf) is a statement at f_0 = f^#; on F \ F_low the cushion used is |a^r_j| <= 2|a^#_j| (P#1).  (P#1) for S-mass coordinates
 needs |P| <= ||R|| rho_A with mass change <= Design^C eta'/u << u <= |a_s|/2: true.  OK.

## 1.6 Corollary K1.B (window bookkeeping).  Verdict: INCOMPLETE -- (E-e') with window-dependent c_flat is NOT verified and FAILS for K1's x_max.
 * c_flat(w) >= c_f u(w) with C_+ = 5: correct (c_flat = min(c^f_flat, gamma_B(w)/(8 rho A_2), 1/(8 rho C_+)), gamma_B(w) = min_m M_m u/4).
 * K_data, D_cl and (E-d)'s first two parts: re-derived; correct (K_data <= C_{f,N}(Design/u)^{C(L+N)}(log n)^{(L+N+2)/2}, (log n)^{(L+N+2)/2} <= n^{1/4}
   once log_2 n >= L^3 and L >> N; (Design/u)^{C(L+N)+1} <= Q(w)^{1/2} for L large since Q = (4Design/u)^{omega + L^2 + 20}).
 * MISSING CONDITION.  X2's Theorem E^eng (r9/X2_notes 4.1, (E-d)) and Q2-refa B.1 require theta_j/c_flat(j)^2 -> 0 when c_flat depends on the window
   (the proof bounds eps''_j <= 2 theta'_j T_lo^2 <= 2 theta'_j r^2/c_flat^2 for |r| > c_flat T_lo).  Q1 Theorem C^tr checks it explicitly
   (theta/c_flat^2 <= C_f T^2 log(1/T)/u^2 -> 0).  K1's companion contains, besides the Step-A cost, the LOWERING of in-F far pull coordinates and the
   TU bank compensation of pulls placed anywhere in Far_l(x) = {x <= v_l <= x_max}, with x_max := T^2/(L Design(L) |Lambda|) (K1 2.0, 2.3):
      p*(f^# - f^r) >= (up to constants) 2|Lambda| x_max = 2 T^2/(L Design(L))   in the worst case,
   so theta' >= 2/(L Design(L)) and theta'/c_flat^2 >= 2/(c_f^2 L Design(L) u(w)^2).  For a clean sub-window w = (L, i) with i >= 2 one has
   u(w) = b(w^-) <= eta(w^-) = T_lo(w^-)^4/(L Design(L)), so the ratio is >= 2 L Design(L)/(c_f^2 T_lo(w^-)^8) -> INFINITY; the clean sub-window is
   selected by the pigeonhole and cannot be forced to be the first one of its level.  So Corollary K1.B's "(E-e') eps' <= 2 theta_w T^2"
   (which silently ignores the lowering cost) and Theorem 5.1 Step 4/7 ("<= 2T^2/(L Design) ... theta'_w -> 0") do not give the hypothesis that
   E^{eng,RT,inf} needs with c_flat(w) ~ u(w).  [R-6, GAP, fixable.]
 * FIX R-6 (PROVED): replace x_max by x'_max := u(w)^2 T^3/(Design(L)^2 |Lambda|) (T = T_lo(w)) and always take the pull at the smallest pullable
   depth.  Costs of the far moves of one carrier with pull depth v := v_l(j_p) <= x'_max: lowering an in-F pull coordinate <= 2(1 + ||U||)|a^r_j| <=
   4 x'_max; the z-flip of the pull <= C_f lambda_l v log(e/v) (Z3 Lemma 3.1, c(delta) with |u_l(delta)| = 2v); the pull mass 24 lambda_l v; the
   compensating TU bank mass <= 2 v nu/(mu_s^2 v_l(s)) <= 2 Design(L) nu v.  Since v >= x_A >= T^5, log(e/v) <= 6 log(1/T), and the total over Lambda is
   <= C Design(L) |Lambda| x'_max log(1/T) = C u^2 T^3 log(1/T)/Design(L).  So the extra theta' is <= C u^2 T log(1/T) and theta'/c_flat^2 <=
   C T log(1/T)/c_f^2 -> 0.  The window stays wide: x_A = C Design eta' = C T^4/L, x'_max/x_A = L u^2/(C Design^3 |Lambda| T) >= 2^{6G(L)} because
   T <= (u/(4 Design))^{20}; for Lemma DC, x = r <= K_w s_1 is far below.  All other uses of x_max (super-thickness threshold, pullability) take x'_max;
   Corollary K1.C's Example (2) is unaffected.  The class of pullable carriers shrinks (more carriers become (U)); this moves rows into the
   non-lever-regular class and invalidates no other statement.  (Remark: the original choice also fails for a second reason: with v up to x_max the
   log(e/v) factor of the z-flip cost is ~ log(1/T), and log(1/T) >= n(w) >> L Design(L).)
 * Remaining parts of (E-e'): eps'_r <= C_f mu*_J log(e/mu*_J) <= theta_w T^2 = C_f T^4 log(1/T): ratio to c_flat^2 T^2 is C_f T^2 log(1/T)/(c_f u)^2 -> 0;
   Step-A cost C_f Design^C eta' log(1/eta')/u: ratio Design^C T^2 log(1/T)/u^3 -> 0.  OK.
