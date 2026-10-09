# Y3 referee, part 3: Sections 4-6 (Corollary 4.2, Lemma 4.3, Theorem 5.1, Claim 5.2, Theorem 6.1, (LSC-trunc), liminf-sparsity)

## Corollary 4.2: CORRECT (PROVED).
|b^pm - g| <= C V_f with C := max_m max(||omega^pm_m||_inf, |d_m(omega^pm_m)|) (finite: Q_m finite, data fixed); (CS-side) by
Lemma 1.1(b) (m_{|g|1_F + C V_f}(x) <= 2 m_{|g|1_F}(2x) + 2C m_{V_f}(2Cx)); (SC) for every set of blocks follows from block-tameness
(the remark after def:SC uses only Q_m finite, no degenerate peaks, (MS)); Theorem 2.1 for every rho < 1.
Remark 4.4(a): V_f <= 2 Bx (not only 2|I| Bx): harmless overestimate. Remark 4.4(b): correct up to the range change
sup_{r <= t_0} Fl_r(b) <= sup_{r <= t_0/(1 - C't_0)} Fl_r(g)/(1 - C't_0).

## Lemma 4.3: CORRECT FOR SMALL r, the statement "for every r > 0" is not proved. Fix: 0 < r <= 1/(1 + 3C_a).
The proof uses |t Theta_+(k)| <= 3 (Lemma suplevel(e)), which needs t <= 1 (N(w + t Theta) <= s(t) <= s(1)); with t = (1 + 3C_a) r this
is r <= 1/(1 + 3C_a). For larger r the same argument at t = 1 gives only Exc(r) <= 2(rc - 1)||a||_1 + r/(2q_0), which is below
c r^2/(2q_0) for large r but not necessarily for intermediate r. Only small r is ever used.

## Theorem 5.1 (Theorem N, box-dominated support): CORRECT (PROVED), every admissible T. Re-derived step by step.
Step 1: (a) at coarse peaks lambda_k|omega_pm(k)| = sigma|alpha(k)||omega_pm(k)|/mu_k <= t/(2mu_k) (suplevel(c), eq:margin);
fine carriers <= 4lambda/t each, total <= 4t^2. (b) |d_pm - d(omega^pm)| <= t/sigma + E_pm/m. (c) the identity
b^pm_0 - B_pm = sum R*(omega_pm 1_{not cQ}) - sum(d_pm - d(omega^pm)) R*w; pointwise <= (4/t + 1/t)Bx(j) once t^2 M_f(L) <= 1.
(d) |X_j| <= (8/t + 4/t)Bx(j) (||Phi_m||_2 <= 1/2 for every admissible T).
Step 2: x_j >= -(1 + 5C_a)|a_j|/t - f^+_j >= -A_j - f^+_j, y_j <= A_j + f^-_j, x_j - y_j = s_j X_j >= -12C_a|a_j|/t >= -2A_j; the
point of [y_j - A_j, x_j + A_j] nearest 0 has modulus (-x_j - A_j)_+ + (y_j - A_j)_+ <= f^+_j + f^-_j; sum <= t/(2q_0) (lem:flip, valid
at every F); b^pm(xi) = 0 (b^pm_0(xi) = g(xi) = 0 by lem:algebra; (sigmat + kappa'a)(zhat) = 0); |kappa'| <= (1+||U||)t/(2q_0).
Step 3: sqrt(Gamma_w) seminorm; Gamma_w(B_pm, Theta_pm) <= 1 + eta_Gamma (lem:budget(d), valid at every F); block difference
-omega_pm 1_{not cQ} + (d_pm - d(omega^pm))w with H ignoring w-multiples.
Step 4: base: r(s_j b^+_j)_- <= c_flat C_+|a_j| <= |a_j|/2, F = N so there are no off-F terms; G_b = nu Psi. Blocks: every k in cQ_m
satisfies vs_k omega^+(k) <= (1 - d_+t)gap(k)/t <= 1.5 gap(k)/t (suplevel(f)), >= -4/t (box); w(k) = 0 case: |t omega_+(k)| <= 1.5M;
these are the inward-only coordinates of Z6-ref Lemma 2.1 (re-derived: vs W(k) <= (1-rd)M - gap(1 - rd - 1.5c_flat) and >= -c_flat A',
needs c_flat <= 1/3, c_flat A' <= 1/4, |rd| <= 1/2 with |d(omega^+)| <= 2/t). c_flat, t_1 do not depend on L (no constant involves
the number of coordinates). Minor slip: "||B_pm||_1 <= ||g||_1 + 1/t (lem:box)" uses the SLD bound sum lambda <= 1/3; for a general
admissible T, sum_{k,m} lambda_{k,m} <= sum_{m<=N} m 2^{-m} < 2 gives ||B_pm||_1 <= ||g||_1 + 6/t. Harmless.
Step 5: fixed window length n_0 >= 24 rho^2 K/(c_flat(1 - rho^2)) works because K, c_flat are f-constants (checked against the
proof of thm:windowed: the case |r| > c_flat T_i/rho needs only n_0 >= 6 rho^2 K/(c_flat(1-rho^2))).
Step 6: Theorem 2.1 with cushion-compatible (hence (CS-side)) averaged data; I_- subset I satisfies (SC) since (SC) passes to subsets.
Improvement (PROVED, trivial): in Step 1(a), sum_{coarse peaks} lambda_k|omega(k)| <= max_{coarse peaks}(1/mu_k) * sum sigma|alpha||omega|
<= (t/2) max(1/mu_k); so M_f(L) may be replaced by M^max_f(L) := sum_m max{1/mu_{k,m} : (k,m) in C_L, k in P_m}, weakening (W_M).
Tightness (checked): the method needs (BD) and not merely cushion-sparse Bx: on D_t the one-sided assignment leaves anti-sign parts
~ Bx(j)/t, whose flip cost at r <= c_flat t is 2 int_0^{12r/t} m_Bx = Theta((r/t)^2) times a constant, not O(r^2) uniformly.

## Claim 5.2 (Z4 Theorem A / Z6 U' at infinite F): SKETCH, PLAUSIBLE, NOT VERIFIED.
The modifications are the right ones: (BD_B) on F gives |X_j| <= (6 + C_dia)Bx_B(j)/t <= (6 + C_dia)C_a|a_j|/t on F for the
active-set switching (lambda_l >= t^2), so the common shift with A_j = C_A(l_*)|a_j|/t works, with closeness as in R1 Claim 3.1;
the price is c_flat ~ 1/(C_A(l_*) + A_2), which Z4 already has in the form gamma_f/C_dia; the factor 1/mu_f(l) (f-dependent room of
S_l \ F) replaces the design weights. Points that must be checked when written out: (1) t_1 of the one-sided expansion must not
depend on C_A(l_*) (true for exact cushion bounds: no-flip condition is r C_+|a| <= |a|/2, and r^4-terms are relative O((c_flat t)^2));
(2) inactive coarse bad carriers contribute <= 6 l_* t to ||Delta B - X||_1, absorbed by the ladder as in Z4; (3) (W_inf) must
absorb K_j C_A(l_*)/gamma_f, i.e. the C_a^2/mu_f^2 scaling stated. F = N excluded: correct.

## Theorem 6.1 (master theorem): CORRECT (PROVED). It is lem:avgfunctionals + convexity + Theorem 2.1; (v) passes to averages
(I_-(averaged) is contained in the union of the blocks where some Delta d_m < 0). "Instances": R1, Theorem 3.5, Theorem 5.1, Z5 S-inf;
the window-pinned/room theorems of Z5 (3.3-3.6) use balanced window certificates (pairs admissible on both sides), which fit (iv) by the
clamp b^cl <= 2|a|/t on F.

## (LSC-trunc): (a), (b) CORRECT; (c) CORRECT AS A STATEMENT ABOUT THEOREM 2.1, the gloss "truncation is never the obstruction" is
interpretive (it says: whenever exact data with (CS-side), (SC) exist at f, finite-support NA approximants exist; it does not say
anything about pairs without such data); (d) correct description of the open step.

## Liminf-sparsity extension (Y3_part2 2.4): SKETCH, PLAUSIBLE WITH THE GAPS THE AUTHOR LISTS. Precise hypothesis in the part file:
liminf_{x->0} m(x) log(1/x)/x = 0 (stronger than "liminf m(y)/y = 0"); the log comes from Z3 Lemma 3.1's companion cost
c(delta) ~ R log(1/R). Unverified: d-repair of the first-order d-mismatch of the raised companion (degenerate case, several blocks),
uniformity of T8's (T_0)-constants at the companion (Z3 Lemma U type continuity), and that T_0 (local validity radius at f') is not
smaller than the slack radius used in lem:assembly with respect to the ORIGINAL (f, g) (flips at the raised coordinates start only at
|tau| > 2T_0, so this is consistent). It does not help the critical case (m(x) log(1/x)/x -> infinity there).
