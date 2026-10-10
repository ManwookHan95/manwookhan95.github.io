# U2 referee, part 4: proofs of the fixes that upgrade or correct U2's statements

## 4.1 Fix W1 (bad-peak margins in Lemma W / RS*_inf).  PROVED.
Notation: for a coarse bad carrier l at a peak k = k(l) of block m with alpha_m(k) != 0, eq:margin gives sigma_m |alpha_m(k)| =
lambda_l mu_k, mu_k := q_0 Phi_m(k) theta_m (rho_l - 1)/m the absolute margin.  Put
   mu_B(l_*) := min{ mu_{k(l)} : l in B_pk(l_*), alpha_{m(l)}(k(l)) != 0 }   (min over an empty set := 1).
Claim A.  At a row f' with the same peaks as f (see Claim B), for every l in B_pk(l_*) with alpha != 0:
|tau_l| <= lambda_l (t/(lambda_l mu'_k) + K_d t) <= t/mu'_k + lambda_l K_d t, and for a degenerate bad peak with sgn w = -eps_l in B_K:
tau_l <= lambda_l K_d t and (tau_l)_- <= c(tau)/(2 m_l) (as in RS'(b)).  Hence the violation of the rows tau_l = 0 (l in B_pk(l_*)) is
<= (|B_pk(l_*)|/mu'_B + K_d + C_0 c(tau)) t, and Lemma W holds with C'_f replaced by C'_f(l_*) := C'_f (1 + l_*/mu_B(l_*)).
Proof.  lem:badpeaks(c) at f' (it uses only eq:peakshift at k, lem:suplevel(c) and the shift bound (a)); insert sigma|alpha| = lambda mu.
Claim B (status stability).  If the raise moves values by at most eps_e and block scalars by at most C_f eps_e (V3 Lemma 2.2), and
C_f' eps_e <= mu_B(l_*)/2 (C_f' an f-constant), then every coarse non-degenerate bad peak of f is a peak of f' with mu'_k >= mu_k/2.
Proof.  k is a peak iff rho >= 1 (Lemma T); rho - 1 = m mu_k/(q_0 Phi theta); |rho' - rho| <= C m (eps_e + rho C_f eps_e)/(Phi theta)
(Lipschitz in the value and in theta), so mu'_k >= mu_k - C'' eps_e.  QED
Consequence for RS*_inf: add 1/mu_B(l) to Xi_f, i.e. Xi_f(l) := (4H(l) l + 3)^{l+2} (1 + K*(l)) C_VP(l)/(gamma_B(l) mu_B(l)), and choose
J with C mu*_J psi(J) <= min(x_j^2, mu_B(l_j)^2) (adds O(log log(1/mu_B)) to 2^J, absorbed by Omega_log as long as
log log(1/mu_B(l)) <= log(Xi_f(l))).  With these changes the proof of RS*_inf goes through verbatim.

## 4.2 Fix G1 (raise depth beyond the tuning depth).  PROVED.
In T_final^*-type transports, choose J(w) := max{ J°(w), d(l) + 1, s_max(l) + 1 }, J°(w) := min{J : C mu*_J psi(J) <= b(w)^2 Phi_min(l)}.
(i) No coordinate s <= d(l) is raised; for s <= d(l), a^r_s = a_s/lambda, lambda in [1, 1 + psi(J)]: the rate objects |a_s| (tiny/robust
    at a clean w for f) are tiny/robust at f^r up to the factor lambda.  (ii) The pinning constant of Lemma P on unraised coordinates
    s < J is <= C_q (1 + 2K*) 2^{J}/delta_min(l) <= C_q (1 + 2K*) max(2^{J°(w)+1}, 2^{d(l)+2})/delta_min(l); 2^{J°(w)} <= 2 log_2(2 log_2(
    C/(b(w)^2 Phi_min))) = O(log n(w)) and 2^{d(l)}/delta_min(l) <= Design(l) (after Fix s1), so the window conditions K T_hi(w) -> 0,
    n(w)/K -> infinity hold with Q(w) = (4 Design/u)^{omega+20}.  (iii) The footprint condition is monotone in J.  QED

## 4.3 Fix D1 ((R6) is invariant under the deep raise).  PROVED.
For a shift pattern pi = (I_up, I_lo, P*, vs, Bf, eps), c(delta; pi) = inf_{x >= 0} sum_{j notin F} phi_{z_j}(sum_m delta_m Pi_m(j) +
sum_{Bf} x eps u(j)), Pi_m = sum_{P*, m} vs lambda u 1_{F^c}, depends only on (F, z|_{F^c}) and design data; a raise changes neither F
nor z.  Hence c_pi(f^r) = c_pi(f) for every pi; with V1's convention that the pattern of the assembly is computed from the
classification of f, (SH_w) at f^r is (SH_w) at f.  QED

## 4.4 Fix N-fix / G3 (the exact tuning residual).  PROVED (as a reformulation); the residual itself OPEN.
Let f° be the current row, L_0 the tuning set (all carriers of tiny objects), eta <= Design(L) b(w).  The FIRST-ORDER RESOURCE MAP is the
linear map R : (moves) -> R^{L_0} whose columns are (1) private columns of (a), (a'), (c), (c') (two-sided), (2) pull columns (one-sided:
they lower eps.val), (3) single-support columns (mu_s^2/nu)(u_k(s) - gamma_k a_s/nu^2)_{k in L_0} for robust s in S_{l''} ∩ F ∩ (s_max, d(L)]
(two-sided).  Exact two-sided tuning with design x u^{-C} constants holds whenever R maps the move cone ONTO R^{L_0} with a right inverse
of norm <= Design^C/u^C (Robinson's regularity; quantitative Graves theorem as in VP' and Lemma TU, second-order terms <= Design^2 eta^2
by 3.2 (T1)), PROVIDED the first-order motion of the coarse carriers outside L_0 caused by columns (3) (<= Design^C u^{-C} eta) is admissible,
which holds because every carrier of a tiny object is in L_0 (3.2 (T3)).  The regularity modulus of R is a finite minimum of determinantal
quantities in (a_s)_{s <= d(l)} and the values: a rate object of level l (finitely many, N-free, design-indexed), hence tiny or robust at a
clean sub-window.  The TUNING RESIDUAL is: this modulus is tiny.  U2's (NDN) is the sub-case in which only columns (3) exist (then the
modulus is the Sherman-Morrison determinant |1 - sum rho gamma/nu^2| up to design factors); the configuration "bank coordinate thick, pulls
off F, tiny pair spreads, no anchor, Sherman-Morrison denominator tiny" is in the residual but not in U2's (NDN) (U2's 'iff' is FALSE).

## 4.5 Fix 2.3 (RS*_inf without (ND'): the corner case is a rate).  PROVED (conditional on the rate below).
Suppose (ND'_{B_np(l_0)}) fails, with kernel coefficients c (Lemma ND), so for l_* >= l_0 the raise set R is empty and no VP is used
(f' = f, lambda' = 1).  For a kernel carrier k put S^hat_k(l_*) := S_k ∩ F \ T_B(l_*) and m^F_k(l_*) := ||v_k 1_{S^hat_k(l_*)}||_1.
Claim.  If k is KEPT at scale t (|tau_k| > K_{i_0+1} t) and K_1 >= 3 C_q (1 + 2K*)/m^F_k(l_*), then |tau'_k| < (15/4)|c_k/kappa|/t; in
particular the data are not deep on S_k ∩ F off a finite fixed set.
Proof.  On S^hat_k, a_s = (c_k/kappa) v_k(s) has the constant sign sgn(c_k/kappa).  If s_s eps_k = +sgn tau_k there, the kernel part is
aligned (s_s X'_s >= 0).  Otherwise sum (P.1) over s in S^hat_k (good-target coordinates with r'_s): sum_s (|tau_k| v_k(s) - 2|c_k/kappa| v_k(s)/t)_+
<= sum phi_s + sum |r_s| + sum |r'_s| <= (1 + eta')t/(2q_0) + 8t^2 + (4/3)K* t.  If |tau_k| >= 3|c_k/kappa|/t, the left side is >= (|tau_k|/3)
m^F_k, so |tau_k| <= 3 (t/q_0 + 8t + (4/3)K* t)/m^F_k <= K_1 t: contradiction with "kept".  So |tau_k| < 3|c_k/kappa|/t and |tau'_k| <=
(5/4)|tau_k| < (15/4)|c_k/kappa|/t.  At a coordinate j of S_k ∩ F ∩ T_B(l_*), j notin T_{B_np(l_0)}: s_j X'_j >= -|tau'_k| v_k(j) -
(15/2) sum_{l > k, j in supp y_l} lambda_l |y_l(j)|/(n_l t) >= -(15/4)|c_k/kappa| v_k(j)/t - 5 2^{-2j} delta_k/t (allowedness (b), design c <= 1),
which is >= -4|a_j|/t as soon as 2^j >= 20 n_k |kappa/c_k| (a fixed threshold).  The finitely many remaining coordinates (j below that
threshold, and T_{B_np(l_0)} ∩ F) are fixed coordinates of F with |a_j| > 0: they are thick (|a_j| >= K_top t^2) on the windows of large
levels because K_top T_hi -> 0.  Coordinates of S_l ∩ F for non-kernel bad l lie in T_{B_np(l_0)} (Lemma ND): same.  QED
So "RS*_inf without (ND')" holds when (W_inf) is augmented by max over the finitely many kernel carriers of 1/m^F_k(l).  If S_k ∩ F has
bounded gaps beyond s_max(l) (e.g. S_k ⊂ F up to finitely many points), 1/m^F_k(l) <= C_k 2^{s_max(l)}/delta_k is absorbed by Omega_K:
no rate at all.  The rate is genuine only for kernel signature sets meeting F sparsely.

## 4.6 Fix E3(c) (what exactly is missing for (SC) along the deep raise).  OPEN, precisely located.
For a block m and the deep-raised row f^r with value motion eps_e: Scr^{f^r}_m(s) <= Scr^f_m(s + C eps_e) for s >= C eps_e (margins and gaps move
by <= C eps_e), hence (SC) at f gives max_m Scr^{f^r}_m(Upsilon s_i)/s_i -> 0 only along s_i >= C eps_e.  (SC) at f^r (a property of the
fixed row f^r as s -> 0) is not implied.  What the window theorems need is however only a quantitative version on the scales of one
window (Theorem E^SC uses (SC) through lem:scrambling at the construction scales); whether these scales stay above C eps_e in V2's route
is the precise open point (plausible, since eps_e <= b(w)^2 << T_lo(w)^2).

## 4.7 Constant precision in M-inf (box rows).  PROVED.
V1's zero-cost projection uses box rows |tau'| <= beta_{l''} = 12 lambda_{l''}/t, so |X'_j| <= 12 Bx_*(j)/t; the deep raise must lift |a_j| to
>= 8 Bx_*(j) (not 4 Bx_*(j)) so that 4|a^r_j|/t >= 16 Bx_*(j)/(lambda t) > |X'_j| for lambda <= 4/3.  Mass and footprint bounds change by
the factor 2.
