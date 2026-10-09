# Z2 referee, part 2: pinning modulo swallowed carriers (Z2 2.4-2.6) and Theorem S (Z2 part 3)

## 1. Lemma 2.5 (pinning modulo swallowed carriers). PROVED, correct; one step must be rewritten.
(a) For l notin B, on S*_l = S_l \ (F cup U_{l' in B, l'>l} supp y_{l'}) the only non-zero vectors are u_l's signature and GOOD finer targets
    (coarser targets avoid S_l by allowedness (a), other signatures live elsewhere, bad finer targets removed by definition), so
    theta*_l|Delta c_l| <= E_l + 2 sum_{l'>l, l' notin B} kappa_{l',l}|Delta c_{l'}|. The good system is closed (bad indices never appear on the right),
    and the unrolling of Z2 1.5 gives sum_{l notin B} |Delta c_l| <= K* t on window scales. No resonance and no (H3) are used. Correct.
    Remark: this is exactly the repair of the G3-referee objection "a coarser carrier touched by an unpinned target is slaved": the touched points
    are removed from the room (finitely many if B is finite); the price is that room must exist on S*_l, which (W*) assumes.
(b) For l in B, under (H3): on S_l \ F only u_l's signature and good finer targets live, z == sigma_l there, phi_{sigma}(-Delta c v) = 2(sigma Delta c)_+ v,
    so rho_l (tau_l)_- <= E_l + 2 sum_{l'>l good} kappa|Delta c_{l'}|. The claimed bound sum_{B cap Cset}(tau_l)_- <= K* t does NOT follow from (a) and
    "rho_l >= 1/Lambda*" as written in Z2 2.5's proof (that route gives Lambda*^2 t). It DOES follow from the UNIFIED triangular system: put
    x_l := |Delta c_l| (good) or (tau_l)_- (bad), S_l := sum_{l <= l' <= l_*} x_{l'}; every inequality has the form x_l <= (X_l + (8/3)S_{l+1})/rho_l
    (right sides contain only good later x's, which are <= S_{l+1}); unrolling gives sum_{Cset} x_l <= Lambda*(l_*)(t/q_0 + 16t^2). Since Lambda*
    already contains the factors (1 + 3/rho_l) of the bad indices, this is what the definition of Lambda* was made for. (Checked numerically:
    Z2ref_work/checks.py, worst ratio S_1/bound = 1/3.) Fixable gap (one paragraph).
(c) Delta B 1_{F^c} = -sum_l Delta c_l u_l 1_{F^c} = sum_{B cap Cset} tau_l u~_l + (good and fine terms) and tau = tau_+ - tau_-: ||e|| <= 2K* t + 6t^2. Correct.
Scope remark on the task's summary sentence "the switching through swallowed carriers is one-sided": PROVED under (H3) (Lemma 2.5(b)), or for
B finite through the cost function c(tau) of 3.2 (each S_l \ (F cup T_0) is infinite); without (H3) and with B infinite it is not proved.

## 2. Lemma 2.6. PROVED, correct.
(a) Lemma 2.1 at a good non-degenerate peak k_1 of index <= l_* (exists by (H4) for l_* large) and |Delta c_{k_1}| <= K* t.
(b) Lemma 2.2 split into good (<= K* t/(mC)), fine (<= 6t^2/(mC)) and bad coarse terms (Delta c_l = -sigma_l tau_l). Correct.
(c) (2.1.1) at k = k_l: |omega_+| + |omega_-| = sigma_k sigma_l tau_l/lambda_l - Delta d M >= 0, and <= t/(sigma_m|alpha_{k_l}|) when alpha_{k_l} != 0.
    So |tau_l| <= lambda_l(t/(sigma_m|alpha|) + K_d* t) (non-degenerate) and tau_l <= lambda_l K_d* t when sigma_k = -sigma_l. Correct.
Note: in case (S_inf) (H4) is automatic (bad carriers are strict non-peaks and every block has a non-degenerate peak since ||alpha_m||_1 = 1)
and (H5) is vacuous.

## 3. Theorem S. PROVED (modulo the imports G3 2-5 with the kappa_0 fix, S3 Cor D1), correct with fixable gaps.
Re-derivation, step by step.
* 3.2 (S_fin), cost function: for j in S_l \ F (l in B) the bad vectors that can be non-zero are u_l (signature) and targets of bad l' > l;
  off U_B S_l only bad targets; T_0 := U_{l in B} supp y_l is finite. So c(tau) = sum_B 2(tau_l)_-||v_l 1_{S_l\(F cup T_0)}|| + sum_{T_0\F} phi_{z_j}(L_j tau):
  finite sum of convex piecewise-linear functions, each >= c_0 x (violation of one linear inequality or equality defining Z_0). Hoffman's bound applies
  to Z = Z_0 cap {tau_l = 0, l in Bpk} cap {sum_{m(l)=m} a_l tau_l = 0} (0 in Z, so non-empty), with H = H(f). Correct.
* Window bounds: c(tau) <= t/q_0 + 2||e_0|| ((F2)); for l in Bpk: non-degenerate peak -> 2.6(c); degenerate peak with sign -sigma_l -> upper bound by
  2.6(c) and lower bound (tau_l)_- <= c(tau)/(2||v_l 1_{S_l\(F cup T_0)}||); (H5) excludes the remaining case. d-constraint: 2.6(b) (the Bpk terms
  are O(K t) and can be moved to the right side). So ||tau - tau'||_1 <= K_H t with K_H = C(f) H K*. Correct.
* (S_inf): tau' = tau_+, cost zero by resonance, a_l = 0 by d-neutrality, ||tau - tau'|| <= K* t by 2.5(b) (unified system). Correct.
* 3.3 two-piece data. Verified: b^+ 1_{F^c} = theta V' (z-signed), b^- 1_{F^c} = theta V' - V' = -(1-theta)V' ((-z)-signed), both in K;
  omega^± finitely supported in Q_m (good coarse non-peaks with gap >= t^2 and bad coarse strict non-peaks); R_m*(sigma tau'/lambda e_{k_l}) = sigma tau' u_l
  gives the second representation; d(omega^-) - d(omega^+) = sum (sigma tau'/lambda)Phi^2 w(k_l)/C = sum a_l tau'_l = 0; b^+(zhat) = 0 by construction and
  b^-(xi) = -sum sigma_l tau'_l u_l(xi) = -sigma_m sum a_l tau'_l = 0 (u_l(xi) = sigma_m Phi w(k_l)/(mC) at non-peaks), i.e. both sides balanced.
  These ARE data in the sense of P2A 1.6 with Delta d_m = 0. Correct.
  (b) g - g_t = r_+ + kappa a + sum R*(Omega_+ - omega^+ + d(omega^+)w) with kappa = B_+(zhat) - r_+(zhat): correct; the block term follows G3 4.2(c)
  verbatim at good coordinates, is 0 at bad non-peaks (kept exactly), and the bad peaks are pinned; Delta d is pinned by 2.6(a) instead of G3 3.5(c).
  (c) seminorm comparison with (B_±, Omega_±): the - side differences are r_- off F, O(K't) on F, and at bad coordinates
  sigma(tau' - tau)/lambda + Delta d w(k_l) (lambda-weighted mass |tau - tau'| + lambda|Delta d|M). Correct.
  (d) constant slip: |omega_+(k_l)| <= (3 + eta)/t (|t Omega| <= 3 and |t d_+ w| <= eta), not 3M/t; immaterial. In fact the budget gives much more:
  for a d-neutral bad non-peak D e_{k_l} is orthogonal to D w, so Phi(k_l)|Omega_±(k_l)| <= sqrt((1+eta)C_m/sigma_m): the switching amplitude through a
  FIXED coarse carrier is O(1), not O(1/t). (Harmless; it shows that the "1/t-size" two-piece data never actually occur at fixed carriers.)
* 3.4 one-sided transfer expansion: re-derived. Base: for sigma s > 0, E_q(a + s'b) = Fl + sum_{j notin F} phi_{z_j}(s'b_j) + nu Psi(s'U*b/nu) exactly (A Lemma 7.2
  is an identity), Fl = 0 if c_1 A_0' <= min_F|a_j|, the phi-terms vanish (s'b is z-signed on K, 0 elsewhere off F), and
  Psi(y) <= ||P_{e-perp}y||^2/(2(1 - ||y||)). Blocks: bad coordinates (gap >= gamma_B) are outside Lset_t and are not the transfer peak, |s omega| <= c_1 A_2,
  so |W(k)| <= (1-sd)M - gamma_B/2. Hilbert and d-terms O(c_1). Correct. (The uniformity in G3 5.1 is over (C-a), (C-b); here (C-a) is replaced by
  t||b|| <= A_0' and Gamma_w <= 2, which is what the base step needs.)
* 3.5: G3 5.2's proof uses only (i) the local expansion for |s| <= c_1 t (here: + data for s > 0, - data for s < 0), (ii) p*(g - g_i) <= K t_i, (iii) g in C(f),
  convexity of p*. So rho g_avg in C(f). Averaged data: z-signs, supports, the two vector identities and d-neutrality are preserved by averaging;
  Gamma_w is convex on each side; scaling by rho multiplies Gamma_w by rho^2. S3 Cor D1 (F finite, Delta d = 0, kappa_w < 1) gives rho g_avg in Ls(f);
  Ls(f) is closed. Correct.
* Requirements of S3 Cor D1 checked against its proof (S3 3.3-3.5): b^± in l_1(F cup K) with the sign conditions on K, omega^± in c_00 off the peaks,
  g in C(f), F finite, Delta d_m >= 0, kappa_w <= 1 (or rho^2 kappa_w < 1). Nothing else (no bound on ||b||, no finiteness of K, no condition on Q_m).
  All satisfied. The data change with l_*, but S3 Cor D1 is applied for each fixed l_* separately and Ls(f) is closed, so no uniformity is needed.
Verdict: Theorem S is correct. Fixable gaps: the unified triangular system in 2.5(b) (needed for S_inf); the constant in 3.3(d); stating that
(H4) is automatic and (H5) vacuous under (S_inf). The mixture remark in 3.1 (finitely many exceptional + infinitely many resonant d-neutral bad carriers)
is plausible but not proved in Z2 (only asserted "works verbatim"); it is not part of the theorem.
What Theorem S genuinely adds: at first rows with finitely many EXACTLY swallowed signature sets, the unpinned switching is a polyhedral cone
quantity; Hoffman's bound projects the actual switching onto that cone at cost O(H K* t), the theta-split turns the projected switching into exact
two-piece data window by window, and S3 Cor D1 accepts arbitrary contact sets and block structure. This settles G3 6.3(d) for finitely generated
exact resonances under (H4), (H5), (W*). It does NOT touch approximate swallowing (theta_l > 0 tiny), which is where the scale-dependent switching
(O3) lives.
