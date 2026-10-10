# V3 referee, part 3: Theorem RS (support swallowing of any profile)

Verdict: CORRECT, with the (ND_B) statement fix of part 2; the inspection items (I1)-(I3) were checked constant by constant;
I also prove the two relaxations V3 left as SKETCH-level remarks ((H3') -> (H3-inf); L_0 := B_np).

## Structure (re-derived). Theorem RS = Theorem R1 (Z5_ref) run AT a raised companion f_j, fed into Theorem 2.5.
R1 used (CS_B) at exactly one place: the deep set D_t = {j in F : s_j X_j < -2A_j}, A_j = 2|a_j|/t, where the exact switching
X = sum_{l in B} eps_l tau'_l u_l (|X| <= C_tau U_B, bounded switching, R1 Step 2') exceeds the cushions. Claim 3.2(b) of R1 gives
(s b^+)_- <= 3|a|/t everywhere and (s b^-)_+ <= 3|a|/t OFF D_t; Lemma R2 needs only these side parts; Y3 Theorem 2.1 needs only
the side parts (nothing on b^theta). Steps 1, 2, 2', 3 of R1 never use (CS_B). So D_t = {} at every window scale is exactly what is
needed, and the raise y_j = 4C_tau T_j gives |a^{(j)}| >= 2C_tau T_j U_B, hence 4|a^{(j)}|/t >= 8C_tau U_B >= |X| for t <= T_j. OK.
(F_0, where the VP correction acts, is a fixed finite set with |a_s| > 0; for t <= T_j -> 0 it is cushion-dominated.)

## Step-by-step.
Step 1 (windows): with n_j = O(Lambda*_f(l_j)) = o(n^w_{l_j}) by (W*), the depth m_j ~ (2/eps)(2n_j + log(C/theta_j c_flat^2))
fits; the bookkeeping T_j^eps log(1/T_j) <= ... is fine because T_hi(l_j)^eps log(1/T_hi(l_j)) -> 0 as well. OK.
Step 2 (companion): ||U*Da|| <= y M_mu^{U_B}(y) = O(y^{2+eps}); ||Da''||_1 <= C_0||U*Da||; eps_e = O(||U*D||/nu);
eps'_j = O(y^{2+eps} log(1/y)); lam_j <= 2 for small y. (i) re-derived (lam_j <= 2). (ii): rooms, F, K, J, z, B, B_K, B_F, eps_l,
T_0, B_pk, (W*)-data are z/F-data, unchanged. For l in B_np (bad strict non-peak) q_l = eps_l q_0 val_l/sigma_m (lem:threshold:
w_m(k) = C_m m q_0 val_k/(Phi_m(k) sigma_m)); with val_l preserved, the d-row of block m at f_j is the d-row at f times
q_0^{(j)} sigma_m/(q_0 sigma^{(j)}_m); tau'_l = 0 on B_pk, so the cone Z_f is literally the same set; violations measured with
f_j's rows dominate those with f's rows up to that factor and O(sum_{B_pk}|tau_l|). Hoffman constant unchanged. OK.
Step 3 (I1): every lemma in the list uses the mate budget only through s(t) - 1 <= t^2/2 and g(xi) = 0; at f_j the budget is
(1 + eta'_j)t^2/2 with eta'_j <= (lam_j - 1)lam_j^2 + 2theta_j + O(eps_e/t) -> 0 on [T_j 2^{-n_j}, T_j] (the last term from
g_j - g, |g(xi_j)| <= ||g||_1 ||xi_j - xi||_inf = O(eps_e)). lem:smallness: the contradiction argument along pairs (j_n, t_n):
for fixed j only t >= T_j 2^{-n_j} > 0 occur, so j_n -> infinity, f_{j_n} -> f in norm, and the original argument applies
(A_n -> a weak*, ||U*A_n|| -> nu, ||A_n||_1 -> ||a||_1, a^{(j_n)} -> a in l_1). lem:flip, lem:split, lem:switchbudget: budget only.
eta_* and eta_Gamma involve nu, ||U||, C_m: continuous along f_j. OK.
Step 4 (I2): Z5 Lemma 5.2 map c -> (P^perp_{e_j}U* sum_B c_l u_l, (sum_B c_l u_l)(zhat_j)) converges in operator norm on R^B
(||P_{e_j} - P_e|| <= 2||e_j - e||, |u(zhat_j) - u(zhat)| <= ||U*u|| ||e_j - e||); injective limit => uniformly injective. OK.
lem:badpeaks at f_j: K_d uses sigma_m |alpha_m(k°_m)| = lambda_k mu_k (eq:margin), margins move by O(eps_e). OK.
Step 5 (I3): Lemma R2 with U_* = 0: no flips since r(s b)_- <= (c_flat t)(3|a^{(j)}|/t) <= |a^{(j)}|/4; the rest is
lem:onesidedtransfer with transfer data chosen at f and transported by lem:persistence (Z3 Lemma U's argument; a_min is not used
because the cushion bound replaces it). A_0 = 3 + 3C_tau|B|, A_2 = 4 + C_tau/lambda_B, gamma_B: uniform. OK.
Step 6: Theorem 2.5 (a) Cor 2.4 + VP extra term; (b) Steps 4-5 with K_j t + O(eps_e log) <= 2K_j t; (c), (d) Steps 1-2;
(e) averaged data: d-neutral (linear), kappa_w(rho Dbar_j) <= rho^2(1 + eta_0/2) < 1, side parts <= 3|a^{(j)}|/T_lo, so
m(x) = 0 for x < T_lo/3: Y3 Theorem 2.1 at f_j (I_- empty) applies to the mate rho gbar_j in C(f_j) and gives (f_j, rho gbar_j)
in cl NA directly (kappa_w <= 1 case). OK.

## Fix 1 (statement): (ND_B) must be read as (ND'_{L_0}) (part 2); otherwise RS excludes every f having a bad carrier with
u_l|_F = 0, for which nothing needs to be done.

## Improvement 1 (PROVED): L_0 := B_np suffices, and W := U_{B_np} suffices.
VP is used only (a) to keep the d-rows (which involve only B_np, tau' = 0 on B_pk) and (b) for statuses; bad peaks are
non-degenerate under (H3'), their margins move by O(eps_e) without VP. X = sum_{B_np} eps tau' u_l, so the raise along U_{B_np}
already empties D_t. Hence (ND') and (RR) are needed only for B_np.

## Improvement 2 (PROVED): (H3') can be weakened to R1's (H3-inf).
Let l in B_K sit at a degenerate peak k = k(l) of block m at f with sgn w_m(k) = -eps_l (allowed by (H3-inf)). Do NOT include l in
L_0; keep l in B_pk, i.e. keep the cone Z_f (row tau_l = 0). At f_j the status of k may change; in every case |tau_l| = O(K* t):
(a) if k is a peak of f_j, lem:badpeaks(c) gives tau_l <= lambda_l K_d t; (b) if k is a strict non-peak of f_j, its gap is
g_j = M^{(j)}(1 - q_0^{(j)}|val^{(j)}_k|/(vartheta^{(j)}_m Phi_m(k))) = O(eps_e) (at f, q_0|val_k| = vartheta_m Phi_m(k)); with
X := varsigma omega_+(k), Y := varsigma omega_-(k), varsigma = -eps_l, lem:suplevel(f) gives X <= 3g_j/(2t), Y >= -3g_j/(2t), and
varsigma(omega_- - omega_+)(k) = -varsigma Delta Theta_m(k) - Delta d_m (M - g_j) = -tau_l/lambda_l - Delta d_m(M - g_j), so
  tau_l <= lambda_l(|Delta d_m| M + 3g_j/t) <= lambda_l(K_d t + 3g_j/t),   |X| + |Y| <= |tau_l|/lambda_l + |Delta d_m|M + 7g_j/t;
(c) in both cases (tau_l)_- <= c(tau)/(2 m_l) (sign row of B_K, m_l > 0). Since g_j = O(eps_e) = o(t^2) on the window, the
violation of the row tau_l = 0 is O(K* t). Z_f is contained in Z_{f_j} (with tau_l = 0 the f_j-coefficient of l in its d-row is
irrelevant, the other coefficients are proportional by VP), so the Hoffman projection onto Z_f at f_j gives tau' in Z_{f_j} with
sum|tau - tau'| <= C_f K* t. In the data put omega^pm_m(k) := 0 (as R1 does at bad peaks); the closeness estimate at k uses
lambda_k(|omega_+(k)| + |omega_-(k)|) <= |tau_l| + lambda_k(|Delta d_m|M + 7g_j/t) = O(K* t) + o(t). Lemma R2 sees no omega at k.
All other steps are unchanged. So Theorem RS holds under (W*), (H2), (H3-inf), (B_fin), (ND'_{B_np}), (RR_{U_{B_np}}).
(Degenerate bad peaks with sgn w = +eps_l, and degenerate peaks of B_F carriers, stay excluded, exactly as in R1.)

## What RS does NOT cover (precise): mu-thin profiles on F cap supp U_{B_np} ((RR) fails; relative to the chosen mu, and for any
fixed mu such f exist); a|_F in span{u_l|_F : l in B_np} ((ND') fails; then a combination of bad values drifts at second order
kappa nu ||e^# - e||^2/2 and a d-neutral block cone can collapse, so Remark 3.5(d) is NOT a routine repair); B infinite;
(W*)/(H2) failure; degenerate bad peaks of the swallowing sign.
