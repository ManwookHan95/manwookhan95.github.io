# U2 referee, part 2: Lemma W, Theorem RS*_inf, "RS*_inf without (ND')"

## 2.1 Lemma W.  VERDICT: correct in mechanism; the constant bookkeeping for infinitely many bad carriers has a gap (W1),
## plus precisions (W2), (W3).  Status after my fixes: PROVED (with the level-dependent constant C'_f(l_*) of (W1)).
Checked line by line: (1) good pinning at f' with rooms r*_l(l_*) (coarse bad targets removed, fine bad targets O(t^2) by the
box bound and (P2)); fine bad d-terms <= 6 T_lo(l_*)^3/(C_min t); (2) pigeonhole over l_*+1 intervals and the projection onto
Z(P, Sigma) (violation of the Sigma-rows by the actual tau: s_j Delta B(j) >= -2|a'_j|/t - phi_j, |a'_j| <= (3/2)|a_j| for unraised j,
so >= -(3 theta_1 + C'(1 + K*))t); kept amplitudes keep their sign, (3/4)|tau| <= |tau'| <= (5/4)|tau| <= (15/2) lambda/t; (3) the
four cases of the empty deep set: deep raised/unraised coordinates (|a'_j| >= 2Bx_*(j) > (15/8) Bx_*(j) >= t|X'_j|/4), shallow
signature coordinates (Lemma P with the good-target variant), shallow target coordinates (Sigma-row, or thick: 2|a'_j|/t >=
K_top t/2 >= C'(1+K*)t + K_top t/4), coordinates outside all supports; (4) R1 Claims 3.1-3.2 with D_t empty: t||b^+||_1 <= 2 + 3 +
3 + 1 (sum_F A_j <= 2/t, ||X'||_1 <= (15/2) sum lambda/t <= 2.5/t, |kappa| = O(K_top t), K_top t <= 1), t||b^-||_1 <= 9 as well
(|b^+_1 - X'| <= A_j + |X'_j| on F); A_2 = 12 (|omega_+(k)| <= (3 + eta)/t, |tau'|/lambda <= 7.5/t).  The two NEW ideas -- box-level
deep raise of vanishing mass psi(J) and Lemma P for the shallow part -- are correct, and they do remove bounded switching (Z5
Lemma 5.2), box domination and (RR) from the argument.
(W1) GAP (constants; fixable).  Step (1) asserts that the violation of Z by the actual amplitudes is <= C'_f(1 + K*)t with an
   f-CONSTANT C'_f.  For the rows tau_l = 0 at coarse bad PEAKS this uses lem:badpeaks(c): |tau_l| <= lambda_l(t/(sigma_m
   |alpha_m(k(l))|) + K_d t) when sgn w_m(k(l)) = +eps_l (non-degenerate swallowing-sign bad peak), and for B_F peaks of either
   sign (no contact row bounds (tau_l)_-).  With B infinite the sum over B_pk(l_*) of lambda_l/(sigma_m |alpha_m(k(l))|) is a
   LEVEL-DEPENDENT f-rate: by eq:margin, sigma_m|alpha_m(k)| = lambda_k mu_k, so lambda_l/(sigma|alpha|) = 1/mu_{k(l)}, the inverse
   value-margin of the peak, which can tend to 0 along bad peaks arbitrarily fast.  (For B finite it is an f-constant, so RS*
   is unaffected.)  Second, the raise moves values by eps_e <= C mu*_J psi(J); a coarse bad peak keeps its status at f' only if its
   margin exceeds C eps_e (otherwise it may become a strict non-peak with tiny gap and its row tau_l = 0 is no longer controlled
   from the peak side).  FIX: put mu_B(l) := min{mu_{k(l)} : l in B_pk(l), k(l) non-degenerate} (and min over B_F peaks), replace
   C'_f by C'_f/mu_B(l_*), and choose J so that C mu*_J psi(J) <= mu_B(l_*)^2 (adds only O(log log(1/mu_B)) to 2^J).  Degenerate
   bad peaks with the anti-swallowing sign are controlled without margins (tau <= lambda K_d t and the B_K sign row), exactly as
   in V3-ref RS'(b).
(W2) Precision.  "Hoffman constant with violation measured as in eq:hoffman" must include the factor C_0(l_*) converting the
   switching cost c(tau) into row violations (C_0 ~ max_l 1/(2 m_l(l_*)), m_l(l_*) := ||v_l 1_{S_l \ (F ∪ T_0(l_*))}||_1 for
   l in B_K(l_*), which decreases with l_*); i.e. H(l_*) := C_H(l_*) max(1, C_0(l_*)).  With this reading every claimed
   inequality holds and H(l) in (W_inf) carries this rate.
(W3) Precision.  As in Z5 Step 2, T_0 must also contain the finite contact sets S_l \ F of coarse B_F carriers (contact rows),
   besides T_B(l_*) \ F.

## 2.2 Theorem RS*_inf.  VERDICT: PROVED conditionally, after adding to Xi_f the rate 1/mu_B(l) of (W1)
## (and the validity radius of VP', see (I2)); otherwise correct.
Checked: (i) the window factor absorbs Xi_f Omega_K Omega_log; (ii) c_flat(l) >= c gamma_B(l) (onesidedtransfer: c_flat <=
gamma_B/(2A_2)).  U2's claim "t_1 >= c' gamma_B^2" is unnecessary and slightly misleading: in lem:onesidedtransfer and Lemma R2 all
r^3, r^4 and rebalancing conditions are conditions on r = c_flat t, with f-constants (K_3, K_y, K_Y, C_min, M_m - gamma_m) that
are uniform along the companions (lem:persistence); so t_1 >= c/c_flat and no extra power of gamma_B is needed.  (iii) the
sub-window pigeonhole: each shallow target coordinate excludes at most n_j + (1/2)log_2(K_top/theta_1) + 1 positions of the top
of the sub-window, at most s_max(l_j) such coordinates; correct.  (iv) the fixed point J -> K_top(J) -> n(J) -> P(J) -> x(J) ->
J°(x(J)): the right side depends on 2^J linearly, the condition mu*_J <= x(J)^2 is doubly exponential in 2^J, so a least J exists
with 2^J = O(log(L_j + P_j + log(1 + C_VP))); the bounds n_j/n^w -> 0, K_top T_hi -> 0 follow from (W_inf).  Minor: x_j should be
compared with T_lo'^2 >= 2^{-2(L_j + P_j + n_j)}; since x_j^2 (not x_j) bounds the footprint and 2(L + P) >= 2n, U2's
2^{-2(L+P)} also works.
(I1) The missing rate of (W1) must enter Xi_f: Xi_f(l) := (4H(l)l + 3)^{l+2}(1 + K*(l)) C_VP(l)/(gamma_B(l) mu_B(l)).
(I2) VP' (V3-ref) holds for ||U^*Delta a|| <= c_0(L_0), a radius depending on the conditioning of Lambda on L_0 = B_np(l); it
   is ~ C_0(L_0)^{-2} times f-constants; since x_j carries the factor (1 + C_VP)^{-1} and the footprint is <= x_j^2, the radius
   condition is met.  Fine, but it should be said.
(I3) With B infinite, (H3-inf) and "positive gaps" are needed at every level; they are in the statement.  OK.
Does (W_inf) ever hold with B infinite?  Yes for tame data: e.g. bad strict non-peaks with gaps bounded below, bad peaks with
margins bounded below, rooms of good carriers a fixed fraction of the signature mass on their S*-sets, well-conditioned VP and Hoffman
constants growing at most exponentially, H(l) <= C_f^l (e.g. least nonzero minors >= c^l, Lemma H of V2); then Xi_f(l) <= C^{l^2} l^{l+2},
far below l 2^{l^3}.  (Growth H(l) ~ C_f^{l^2} with C_f > 2 would NOT be absorbed: (C_f^{l^2})^{l+2} >> 2^{l^3}.)  So the theorem is not
vacuous, but its rate condition is restrictive for infinitely many bad carriers.

## 2.3 "RS*_inf without (ND')" (U2 4.2(b), SKETCH).  VERDICT: SKETCH as labelled; the corner case is real but is a RATE, not
## a structural obstruction.
Checked: failure of (ND'_{B_np(l_0)}) persists for l >= l_0 (same c, extended by 0); by Lemma ND, F \ T_{B_np(l_0)} lies in finitely
many kernel signature sets with a = (c_k/kappa) v_k there, so the raise set R is empty at large levels (R subset T_{B_np(l_0)} ∩
[J, infinity) = {} once J > max T_{B_np(l_0)}); on kernel coordinates outside coarse bad targets, deepness is the s-independent
condition |tau'_k| > 4|c_k/kappa|/(lambda' t); at deep bad-target coordinates inside kernel sets the non-kernel part is
<= 5 2^{-2j} delta_k/t (allowedness (b), design c_k <= 1), negligible against 4|c_k/kappa| v_k(j)/t for large j.
Corner case (correctly identified by U2): if coarse bad targets cover S_k ∩ F up to s_max(l_*), the shallowest usable pinning
coordinate is s_k(l_*) := min(S_k ∩ F \ T_B(l_*)) > s_max(l_*), and the pinning constant 2^{s_k(l_*)}/delta_k is f-dependent.
Better constant (my remark, PROVED by summing (P.1) instead of using one coordinate): on S_k ∩ F \ T(l_*) the cushion is
proportional, so sum over these s of (|tau_k| v_k(s) - 2|a_s|/t)_+ <= (1 + eta')t/(2q') + 8t^2, whence, if the kernel part is deep
(|tau_k| >= (16/5)|c_k/kappa|/(lambda't)), |tau_k| <= C t/m^F_k(l_*), m^F_k(l_*) := ||v_k 1_{S_k ∩ F \ T(l_*)}||_1 (good-target
coordinates with the (1 + 2K*) factor as in Lemma P).  So the corner case is exactly the rate 1/m^F_k(l): adding it to Xi_f makes
"RS*_inf without (ND')" PROVED conditionally (the rest of the sketch is correct).  Unconditionally it is OPEN (the rate can decay
arbitrarily fast if F ∩ S_k is very sparse beyond s_max(l)).
