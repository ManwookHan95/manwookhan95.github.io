# Z5 referee, part 2: verdicts on T8, T12, T14, T15, T16

## T8 (engineered recovery at arbitrary F; (R-inf) and (CS-data)). CORRECT (PROVED).
Checked every use of F finite in thm:engineered: (1) N_w >= max F -> replaced by a'' := a1_[1,N_w] + window masses, with
alpha(N_w) <= s_1^2 so (E1) ||a''-a||_1 = O(s_1), ||e'-e|| <= K_e s_1; (E2) x^' - zhat = -z1_(N'',inf) + U(e'-e) unchanged, hence
(E3)-(E5), lem:F1, lem:anchor, lem:scrambling unchanged; (2) a_min in (T_1) -> rho T_0 C_R <= 1/8 (R-inf) or the flip budget
2 rho|tau| m(4 rho|tau|) <= delta tau^2/16 (CS-data), K_sharp fixed after T_1 (so that Fl <= tau^2 uniformly); (3) far support
F cap (N_w, N''] are contacts of f' with signs s_j: summand 2(s_j tau rho beta_j)_- = |tau| rho (s_j v_j)_- for diamond = sgn tau
(checked both signs), and = 0 for theta (beta^theta = 0 there); beyond N'': <= (1/2) rho|tau||v_j|. Budget delta/8 added in Step 5:
rho^2 kappa_w + 5delta/8 + delta/8 = 1 - 2delta + 3delta/4 <= 1 - delta. g'' - g = -b^theta 1_(N_w,inf) + blocks -> 0 needs only
b^theta in l_1. The approximants are norm attaining with finite base support F_{<=N_w} cup window contacts. Corollaries D1 and
weightedengineered follow (I_- empty).

## T12 (Theorem S-inf). CORRECT (PROVED), two minor points.
Step 1: lem:modswallow(a) at infinite F: good inequalities use S*_l (disjoint from F and from bad targets), E_l over S_l \ F,
sum <= t/q_0. Product over GOOD l'' only is correct for part (a) (bad x_l := 0). Step 2: T_0 finite (B finite, targets c_00,
S_l \ F finite for B_F); off F cup T_0 only B_K signatures, phi_{eps_l}(eps_l tau_l v_l) = 2(tau_l)_- v_l; Hoffman on a fixed
finite system (constants depend on f only); (H3-inf) needed for B_F peaks (no contact lower bound on tau_l). Step 3: common shift
re-derived: sigma_j in [y_j - A_j, x_j + A_j], |sigma_j| <= f^+_j + f^-_j + |(Delta B - X)_j| (uses A_j >= |a_j|/t); identities
B_+ - b^+ = e_+ + (sigma s)1_F + b^+_1 1_{F\F_t} + kappa a_t and B_- - b^- = (B_+ - b^+) - (Delta B - X) on F, = e_- off F, checked;
one-sided cushion bounds (ii) checked (on F\F_t: b^+ = 0, b^- = -X, |X_j| <= C_X|a_j|/t <= (C_A+1)|a_j|/t). Step 4: no flips for
0 < r <= c_flat t on the + side (free direction never flips); Step 5: averaging preserves (ii) (convexity of x_+, x_-, |x|),
C_R = (C_A + 2C_X + 1)/T_lo(l_j) is a FIXED constant for each window, T8 applies (d-neutral, I_- empty). Example 6.2 checked:
a = u_{l_0}, F = supp y_{l_0} cup S_{l_0}, z = 0 off F: B = {l_0} subset B_F, c_B = 1, Lambda*_f(l) <= C (3/2)^l Lambda°(l).
Minor 1: in Remark 6.3(b) (B_res with infinitely many bad carriers) Lemma lem:modswallow(b) is used, whose unrolling contains the
BAD inequalities; the product must then be the note's Lambda*_f over ALL l'' in L_N (bad factors 1 + 3/(2||v_l 1_{S_l\F}||_1),
positive since B_F is empty). Z5's good-only product in (W*) does not suffice for (b). Fix: state (W*) with the note's Lambda*_f
in the (B_res) extension.
Minor 2: the truncation b^+_2 := b^+_1 1_{F_t} in Step 3c is unnecessary (T8 accepts infinite support); it is harmless under
(H4-inf) but must be dropped in the cushion-sparse extension (part 3), where the tail of X beyond M_t need not be O(t).
Improvement available: Lemma 5.2 (bounded switching, T10) gives |tau'_l| <= C_tau uniformly in t, so |X_j| <= C_tau U_B(j)
(not O(1/t)). This is the key to Theorem R1 (part 3), which replaces (H4-inf) by cushion sparsity.

## T14 (limitation of base pinning). Arithmetic CORRECT; conclusion OVERCLAIMED (fixable).
(1) D*_l(t)/t -> infinity holds for EVERY support-swallowed carrier, not only fast-swallowed ones: Phi_l(Kt, t) <= Kt m_l(Kt^2/2)
with m_l(y) := sum{v_l(j): j in S_l cap F, |a_j| < y v_l(j)} -> 0, so D*_l(t) >= Kt for small t, every K (and D* >= 2c/t in
the cushion-dominated case). So "no scale-independent pinning constant" is not what separates fast from cushion-dominated
swallowing; exactifiability is (T15, Theorem R1).
(2) "windowed averaging cannot apply" is FALSE as stated: windowed averaging applies via exact (or cushion-sparse) two-piece data
whenever the unpinned switching can be exactified (T12 under (H4-inf); Theorem R1 under (CS_B), which includes fast-swallowed
carriers, e.g. v_l ~ 2^{-j}, |a_j| ~ 2^{-(1+beta)j} with beta < 1). Correct statement: window PINNING cannot be derived from the
base budget for support-swallowed carriers.
(3) The exponent (beta-1)/(beta+1) is for S = {j >= j_0}; in the SLD the S_l are disjoint infinite sets (none cofinite); the
exponent is unchanged if S_l has bounded gaps (constants depend on l), different for very sparse S_l. Typo in Z5_part4b l.30:
"(1-beta)/(1+beta)" should be "(beta-1)/(beta+1)" (the main notes have the correct sign). Numerical script reproduced.
(4) The full constraint system also contains bounded switching |Delta theta_l| <= C_U (T10), which is the binding constraint for
beta < 1 (D* -> infinity there).

## T15 (deep flips). Lemma 7.4 CORRECT; necessity holds for ANY data with b^+ - b^- = X on F (not only common shifts):
s(b^+ - b^-) = sX < -2A forces (s b^+)_- > A or (s b^-)_+ > A. Interpretation partly OVERCLAIMED: "fixed data reproducing deep
flips pay a first-order cost at smaller scales" is true coordinatewise, but the TOTAL cost is 2|r| sum{beta_j : |a_j| < |r| beta_j},
which is o(r^2) under cushion sparsity when the deep usage is bounded (bounded switching): Theorem R1. The obstruction is the
NON-sparse regime (limsup m_l(y)/y > 0): there fixed data with a nonzero constrained-direction deep part |c| v_l have flip cost
>= r|c| m_l(r|c|/2), not o(r^2) along a sequence r -> 0 (part 3, Remark R1.2).

## T16 (no design removes support swallowing). CORRECT (trivial): |a_j| := 2^{-j} min_{l<=j, v_l(j) != 0}|v_l(j)| (or 2^{-j} if
no such l), normalized; full support, ratio -> 0 along every signature. Also defeats (CS_B) (take |a_j| <= v_l(j)^2 2^{-j}).
