# Z4 part 3: Theorem S_Binf — infinitely many swallowed carriers (non-resonant, non-d-neutral) via scale-dependent active sets

Setting: SLD_G (part 2.4) — or the original SLD under the hypotheses of Corollary 4.1 — N fixed, f in S_{p*} with F finite, B = B(f) arbitrary
(possibly infinite). Conventions of the note: Delta d_m := d_{+,m} - d_{-,m} (Lemma lem:suplevel), tau_l := -eps_l Delta theta_l (l in B),
q_l as in def:swallowed. For l in B with k(l) a peak, varsigma_l := sign w_{m(l)}(k(l)); the peak is of **swallowing sign** if varsigma_l = eps_l
and of **anti sign** if varsigma_l = -eps_l.

## 3.1 Growth quantities and hypotheses
For a level l_* >= 1:
* r*_l(l_*) (good l <= l_*) := min_{sigma=±1} sum_{s in S*_l(l_*)} v_l(s)(1 + sigma z_s), S*_l(l_*) := S_l \ (F ∪ union{supp y_{l'} : l' in B, l < l' <= l_*});
  r*_l := 2||v_l 1_{S_l\F}||_1 for l in B; Lambda*_f(l_*) := prod_{l <= l_*, l in L_N} (1 + 3/r*_l(l_*)) (= infinity if some r*_l(l_*) = 0).
* M_f(l_*) := sum{ 1/mu_{k(l),m(l)} : l in B ∩ [1,l_*], k(l) a peak of swallowing sign }.
* gamma_f(l_*) := min( {M_m : m in I} ∪ {gap_{m(l)}(k(l)) : l in B ∩ [1,l_*], k(l) in Q_{m(l)}} ) > 0.
* gamma_T(l_*) := min( {1} ∪ {1 - |z_j| : j in T(B ∩ [1,l_*]) \ F, |z_j| < 1} ) > 0 (T(.) as in part 2).
* Xi_f(l_*) := [ (Lambda*_f(l_*) + M_f(l_*) + l_*) / Lambda°(l_*) ]^2 / ( gamma_T(l_*)^2 gamma_f(l_*) ).
Hypotheses on f:
* (H2') for every block m there are carriers l^up_m, l^dn_m of block m such that l^up_m is a non-degenerate peak which is good or swallowed
  with swallowing sign, and l^dn_m is a non-degenerate good peak or a swallowed peak of anti sign (degenerate allowed).
* (H3) every swallowed peak of swallowing sign is non-degenerate (as in def:swallowed).
* (DR) part 2.3.
* (W_inf) liminf_{l -> infinity} Xi_f(l) / (l 2^{l^3})^6 = 0.
  (Implied by (W*)-type growth: if M_f, 1/gamma_f, 1/gamma_T grow at most like (l 2^{l^3})^{1/2} and Lambda*_f/Lambda° = O((l 2^{l^3})^2) along a
  subsequence. In particular (W*) of def:swallowed together with bounded M_f, 1/gamma_f, 1/gamma_T implies (W_inf).)
**R_SBinf** := {f : F finite, (H2'), (H3), (DR), (W_inf)}.

**Theorem 3.1 (S_Binf).** For SLD_G and every N, R_SBinf ⊂ R. PROVED (proof in 3.2-3.3 and part 4).
No resonance, no d-neutrality, no (H1) and no finiteness of B is assumed; strict non-peaks may be infinite in number, (MS) may fail,
contact sets are arbitrary.

## 3.2 Per-scale estimates
Fix g in C(f), rho in (0,1), eta_0, kappa_0, eps_tr, eta as in the proof of Theorem thm:S. "f-constant" = a number depending only on
f, g, rho, N and the design, NOT on l_* or t. Let l_* >= max(max F, l_f) where l_f is so large that the finitely many fixed carriers
U_fix := U_R ∪ {l^up_m, l^dn_m : m} are <= l_f. Let t in W(l_*) be dyadic with t <= min(t_eta, 1) and t^2 <= min_{U_fix} lambda_l, and let
(B_±, Theta_±) be a two-sided decomposition of g at scale t. Put U := {l in B ∩ [1, l_*] : lambda_l >= t^2} (the **active set**; U ⊃ U_fix).

**Step 1 (good pinning).** sum_{l notin B} |Delta theta_l| <= K* t, K* := (1/q_0 + 22) Lambda*_f(l_*).
*Proof.* For good l <= l_* and s in S*_l(l_*), (P1) and eq:DeltaB give -Delta B(s) = Delta theta_l v_l(s) + sum_{l' > l} Delta theta_{l'}
y_{l'}(s)/n_{l'}, where coarse swallowed l' (<= l_*) do not occur (definition of S*_l), coarser targets vanish on S_l (allowedness (a)) and
other signatures vanish. As in the proof of Lemma lem:signmixed, r*_l(l_*) |Delta theta_l| <= E_l + 2 sum_{l<l'<=l_*, l' good} pi_{l',l}
|Delta theta_{l'}| + 2 sum_{l' > l_*} pi_{l',l} |Delta theta_{l'}|, E_l := sum_{s in S*_l} phi_{z_s}(Delta B(s)), sum_l E_l <= t/q_0
(Lemma lem:switchbudget). Only good coarse carriers occur on the right; unroll as in Lemma lem:modswallow (x_l := |Delta theta_l| for good l,
x_l := 0 for swallowed l, X_l := E_l + 2 sum_{l'>l_*} pi_{l',l}|Delta theta_{l'}|), use sum_{l'>l_*}|Delta theta_{l'}| <= 6t^2 (Lemma lem:box,
(P2)). QED.

**Step 2 (cost of the swallowed switching).** e_0 := Delta B 1_{F^c} - sum_{l in U} eps_l tau_l u_l 1_{F^c} satisfies ||e_0||_1 <= K_0 t,
K_0 := K* + 6 l_* + 6, and c_U(tau|_U) <= (1/q_0 + 2K_0) t.
*Proof.* e_0 = -sum_{l notin U} Delta theta_l u_l 1_{F^c}, ||u_l||_1 <= 1. Good carriers: Step 1. Swallowed l <= l_* with lambda_l < t^2: at most
l_* of them, |Delta theta_l| <= 6 lambda_l/t < 6t each (Lemma lem:box). Fine carriers: <= 6t^2. Then c_U(tau) = sum_{j notin F} phi_{z_j}
(Delta B(j) - e_0(j)) <= sum phi_{z_j}(Delta B(j)) + 2||e_0||_1 <= t/q_0 + 2 K_0 t (Lemmas lem:phicalc(c), lem:switchbudget). QED.

**Step 3 (the uniform shift is pinned through base peaks).** Put K_1 := G*(l_*) K_0/gamma_T(l_*). There is tau° in Z'_{kappa(f,U)} (in
particular tau°_l >= 0 on U) with ||tau|_U - tau°||_1 <= D := (1/q_0 + 2) K_1 t, and |Delta d_m| M_m <= K_d t for every m, K_d := C_1 K_1,
C_1 an f-constant.
*Proof.* The first claim is (2.3) with Step 2. Fix m. Upper bound: if l := l^dn_m is a swallowed anti-sign peak, then by eq:peakshift (as in
the proof of Lemma lem:badpeaks(c)), varsigma_l eps_l tau_l/lambda_l - Delta d_m M_m = |omega_{+,m}(k)| + |omega_{-,m}(k)| >= 0 with
varsigma_l eps_l = -1, so Delta d_m M_m <= -tau_l/lambda_l <= (tau_l)_-/lambda_l <= D/lambda_l (tau°_l >= 0). If l^dn_m is a good
non-degenerate peak, Lemma lem:badpeaks(a) (its proof uses only |Delta theta_{l°}| <= K* t, Step 1) gives |Delta d_m| M_m <= t/(sigma_m
|alpha_m(k°)|) + K* t/lambda_{l°}. Lower bound: if l := l^up_m is swallowed of swallowing sign with margin mu > 0, then 0 <= tau_l/lambda_l -
Delta d_m M_m = e_k := |omega_+(k)| + |omega_-(k)| <= t/(lambda_l mu) (Lemma lem:suplevel(c): |alpha(k)| e_k <= t/sigma, and sigma|alpha(k)| =
lambda_k mu_k, eq:margin); hence Delta d_m M_m >= tau_l/lambda_l - t/(lambda_l mu) >= -(D + t/mu)/lambda_l. Good case as above. K_1 >= K_0 >= K*. QED.

**Step 4 (violations of the exact cone).** viol_{kappa(f,U)}(tau|_U) <= C_2 (K_1 + M_f(l_*)) t, C_2 an f-constant; hence there is tau_0 in
Z^0_{kappa(f,U)} with ||tau|_U - tau_0||_1 <= D_0 := C_2 G*(l_*)(K_1 + M_f(l_*)) t.
*Proof.* viol' <= c_U/gamma_T(l_*) <= (1/q_0 + 2)K_1 t/G* <= (1/q_0+2) K_1 t (Lemma 2.2, Step 2). Peak rows, l in U with k = k(l) a peak:
tau_l = varsigma_l eps_l lambda_l (Delta d_m M_m + e_k), e_k >= 0 (eq:peakshift). Swallowing sign: |tau_l| <= lambda_l K_d t + t/mu_l
(Step 3 bound e_k <= t/(lambda_l mu_l); mu_l > 0 by (H3)). Anti sign: tau_l = -lambda_l(Delta d M + e_k) <= lambda_l K_d t, and (tau_l)_- <=
|tau_l - tau°_l|. Summing (sum lambda_l <= 1/3): sum_{U∩P} |tau_l| <= K_d t/3 + M_f(l_*) t + D. Apply (2.2). QED.

**Step 5 (exact d-neutral projection).** There is tau' in Z_U (zero cost, tau' = 0 at peaks, all d-rows exact) with
||tau|_U - tau'||_1 <= C_diamond t,  C_diamond := C_3 G*(l_*)^2 (Lambda*_f(l_*) + l_* + M_f(l_*)) / gamma_T(l_*),  C_3 an f-constant.
*Proof.* d-rows of tau: by eq:didentity, for block m, sum_{l in B, m(l)=m} q_l tau_l = -Delta d_m M_m + (1/(mC_m)) sum_{good} Phi w Delta theta
+ r_m, |r_m| <= 2t/sigma_m (for swallowed l, Phi(k)w(k)Delta theta_l/(mC) = -q_l tau_l). Swallowed l notin U: |q_l| <= Phi_l M/(mC),
|tau_l| <= 6 m Phi_l/t; if l <= l_* then Phi_l < t^2/m, so sum |q_l tau_l| <= 6Mt/(mC) sum Phi_l <= 6t/C_m; if l > l_*, Phi_l <= c_{l_*+1} <= t^3
and the sum is <= (6M/(C_m t)) t^3 sum Phi_l <= 6t^2/C_m. Hence |delta_m(tau|_U)| <= K_q t, K_q := K_d + K*/(mC_m) + 2/sigma_m + 12/C_m <= C K_1. For tau_0 (Step 4),
|delta_m(tau_0)| <= K_q t + D_0/C_min (|q_l| <= 1/C_min). tau_0 vanishes at peaks; Lemma 2.3 (U ⊃ U_R) gives tau' in Z_U with
||tau' - tau_0||_1 <= R_f N (K_q t + D_0/C_min). Collect, using K_1 = G* K_0/gamma_T, K_0 <= (1/q_0 + 28)(Lambda* + l_*), G*, R_f >= 1. QED.
