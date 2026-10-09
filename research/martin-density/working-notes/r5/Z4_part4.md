# Z4 part 4: Theorem S_Binf, end of proof; consequences

Continuation of part 3 (same f, g, rho, l_*, t, U, tau, tau').

**Step 6 (window two-piece data).** Assume moreover C_diamond t <= 1. Let V' := sum_{l in U} eps_l tau'_l u_l 1_{F^c} (z-signed, supported in K:
Lemma 2.1, tau' in Z^0_U), e := Delta B 1_{F^c} - V' (so ||e||_1 <= (K_0 + C_diamond) t), chi and frak e_± from Lemma lem:split. Let
U_np := {l in U : k(l) in Q_{m(l)}} (then V' = sum_{U_np} eps_l tau'_l u_l 1_{F^c}). Define, exactly as in Lemma lem:windowtwopiece with
B_np replaced by U_np:
 + : omega^+_m := omega^c_m (Definition def:windowcert) off {k(l) : l in U_np}, omega^+_m(k(l)) := omega_{+,m}(k(l)) for l in U_np, m(l) = m;
     b^+ := B_+ 1_F + chi V' - kappa a, kappa := (B_+ 1_F + chi V')(zhat);
 - : omega^-_m := omega^+_m + sum_{l in U_np, m(l)=m} (eps_l tau'_l/lambda_l) e_{k(l)},  b^- := b^+ - sum_{l in U_np} eps_l tau'_l u_l;
 g_t := b^+ + sum_m R_m^*(omega^+_m - d_m(omega^+_m) w_m).
Then, with K_2, K_4 <= C_4 C_diamond and A^star_0 f-constants:
 (a) (b^±, omega^±) are d-neutral two-piece data for g_t (Definition def:twopiece), b^±(xi) = 0;
 (b) ||g - g_t||_1 <= K_2 t;  (c) Gamma_w(b^±, omega^±) <= (sqrt(1 + eta_Gamma(eta)) + K_4 t)^2;
 (d) t ||b^±||_1 <= A^star_0, and every k in supp omega^±_m has either gap_m(k) >= t^2 and |omega^±_m(k)| <= 2 gap_m(k)/t, or k = k(l),
     l in U_np, gap_m(k) >= gamma_f(l_*) and |omega^±_m(k)| <= A_2/t with A_2 := 10 + C_diamond.
*Proof.* The proof of Lemma lem:windowtwopiece applies line by line with B_np -> U_np, with the following replacements.
(a) d_m(omega^-_m) - d_m(omega^+_m) = sum_{l in U_np, m(l)=m} q_l tau'_l = sum_{l in U, m(l)=m} q_l tau'_l = 0 because tau' vanishes at the
peaks of U and satisfies the d-rows (Step 5). Signs: b^+ 1_{F^c} = chi V' and b^- 1_{F^c} = -(1-chi) V'.
(b) Coarse coordinates: good ones as in Proposition prop:windowcert(c) (claim there, with sum over good |Delta theta| <= K* t and |Delta d_m| M_m
<= K_d t); k(l), l in U_np: rho_k = 0; k(l), l in U ∩ P: omega^+(k) = 0 and rho_k <= e_k, lambda_l e_k <= |tau_l| + lambda_l |Delta d M|
with |tau_l| = |tau_l - tau'_l| (tau'_l = 0), total <= C_diamond t + K_d t; swallowed coarse l notin U (lambda_l < t^2): treated as good coarse
coordinates of the window certificate, lambda rho <= |Delta theta_l| + lambda |Delta d| M + 2t lambda with |Delta theta_l| < 6t, total <= 6 l_* t
+ K_d t + 2t. Fine coordinates and d-terms: as in the note (|omega^+| <= 4/t by Lemma lem:suplevel(a),(e), so |d_m(omega^+_m)| <= 2/t). Base:
B_+ - b^+ = frak e_+ + kappa a, ||frak e_+||_1 <= ||e||_1 + t/q_0, |kappa| <= t/(2q_0) + (1+||U||)||frak e_+||_1.
(c) Seminorm comparison with (B_±, Theta_±) and Lemma lem:budget(d) as in the note; on the - side the lambda-weighted discrepancy at k(l),
l in U, is |tau_l - tau'_l|, at good/fine/inactive coordinates |Delta theta_k|: total <= (K_0 + C_diamond) t.
(d) |tau'_l| <= |tau_l| + C_diamond t <= 6 lambda_l/t + C_diamond t and lambda_l >= t^2 on U, so |tau'_l|/lambda_l <= (6 + C_diamond)/t;
|omega^+_m(k(l))| <= (3 + eta)/t <= 4/t; gap_m(k(l)) >= gamma_f(l_*) for l in U_np. ||V'||_1 <= sum_U |tau'_l| <= 2/t + C_diamond t <= 3/t.
The rest as in the note. QED.

**Step 7 (one-sided expansion).** Lemma lem:onesidedtransfer with (eps_tr, A^star_0, A_2, gamma_B := gamma_f(l_*)) gives c_flat >=
c_f gamma_f(l_*)/A_2 >= c'_f gamma_f(l_*)/C_diamond (c_f an f-constant) and t_1 depending only on f and eps_tr. PROVED: in the proof of that
lemma the conditions involving A_2 and gamma_B are conditions on c_flat only (c_flat <= gamma_B/(2A_2), c_flat <= C_min/(2A_3), and the
O(c_flat) relative errors with constants linear in A_3 = 2 + A_2), while t_1 is constrained only through terms of order r^4 with |r| <= c_flat t
<= t and through the transfer data. Hence for every dyadic t in W(l_*) with t <= min(t_eta, t_1, 1), C_diamond t <= 1 and K_4 t <= kappa_0:
p*(f + r g_t) <= 1 + (r^2/2)(1 + eta_0) for |r| <= c_flat t (+ data for r > 0, - data for r < 0), and p*(g - g_t) <= (1 + ||U||) K_2 t.

**Step 8 (window arithmetic).** Put K_j := (1+||U||) K_2(l_j) for window indices l_j. Lemma lem:avgfunctionals (in the form of Lemma 6.1,
which allows c_flat = c_flat(l_j) to depend on the window) needs, along l_j -> infinity,
 (i) n^w_{l_j} >= 24 rho^2 K_j/(c_flat(1 - rho^2)), (ii) K_j T_hi(l_j) -> 0 (which also gives all smallness conditions of Steps 6-7 on W(l_j)).
Now K_j/c_flat <= C C_diamond^2/gamma_f <= C' G*(l)^4 (Lambda* + l + M_f)^2/(gamma_T^2 gamma_f) = C' G*(l)^4 Lambda°(l)^2 Xi_f(l), and for SLD_G,
n^w_l >= (l 2^{l^3} Lambda°(l) G*(l))^6 and T_hi(l) <= (l 2^{l^3} Lambda°(l) G*(l))^{-6}. Hence (i) holds as soon as C' Xi_f(l) <= c (l 2^{l^3})^6,
and K_j T_hi(l_j) <= C'' G*^2 (Lambda* + l + M_f)/gamma_T * (l 2^{l^3} Lambda° G*)^{-6} <= C'' Xi_f(l)^{1/2} (l 2^{l^3})^{-6} -> 0. By (W_inf) choose
l_j with Xi_f(l_j)/(l_j 2^{l_j^3})^6 -> 0. Lemma lem:avgfunctionals: rho bar g_j in C(f), rho bar g_j -> rho g.

**Step 9 (engineering).** The averaged data bar D_j are d-neutral two-piece data for bar g_j (sign conditions, vanishing off F ∪ K, finite
supports in Q_m, both representations and Delta d = 0 are preserved by averaging); by convexity kappa_w(rho bar D_j) <= rho^2 (1 + eta_0/2) <= 1.
Corollary cor:D1 (no hypothesis on Q_m, K or T) gives (f, rho bar g_j) in cl NA; let j -> infinity, then rho -> 1. QED (Theorem 3.1).

## 4.1 Consequences and remarks
**Corollary 4.1 (original design; f-dependent Hoffman constants).** PROVED. Let H^Z_f(l) be the largest l_1-Hoffman constant, over finite U with
U_fix ⊂ U ⊂ B ∩ [1, l], of the systems defining Z'_{kappa(f,U)} (violation viol') and Z_U (violation viol_{kappa(f,U)} + sum_m |delta_m|).
Steps 3-5 hold with G*(l_*) and the repair step replaced by H^Z_f(l_*) (then C_diamond <= C_3 H^Z_f(l_*)^2 (Lambda* + l_* + M_f)/gamma_T, and
(DR) is not needed). Consequently, for the ORIGINAL SLD, f in R provided F finite, (H2'), (H3) and
  (W_inf^orig)  liminf_l H^Z_f(l)^4 Lambda°(l) Xi_f(l)/(l 2^{l^3}) = 0
(Step 8 with n^w_l >= l 2^{l^3} Lambda°(l), T_hi(l) <= 2^{-l^3}/(l Lambda°(l))). Under (DR), H^Z_f(l) <= C_f G*(l) by Lemma 2.3.

**Corollary 4.2 (Theorem thm:S revisited).** PROVED. (a) Under (B_res): q_l = 0 on B (d-neutral strict non-peaks), so (DR) is trivial and
M_f = 0; resonance gives T(B) \ F ⊂ K, so gamma_T = 1; gamma_f = min_m M_m; (H2) implies (H2'); the r*_l(l_*) of 3.1 dominate those of
def:swallowed (fewer points are removed), so (W*) implies (W_inf). Hence R_S ∩ (B_res) ⊂ R_SBinf for SLD_G.
(b) Under (B_fin): U = B for small t, so H^Z_f, M_f, gamma_f, gamma_T are eventually constant, and once C_diamond t^2 <= lambda_B :=
min_B lambda_l the bound |tau'_l|/lambda_l <= (6 + 1)/t keeps A_2 = 11 fixed; then c_flat is an f-constant and Step 8 needs only
C_diamond(l) = o(n^w_l), which (W*) gives (C_diamond <= C Lambda*_f). This is Theorem thm:S (B_fin) for both designs.
So Theorem 3.1 / Corollary 4.1 contain Theorem thm:S and remove from it (H1), resonance, d-neutrality and the finiteness of B, and weaken (H2)
to (H2'); the price is the growth hypothesis (W_inf) (resp. (W_inf^orig)) and, for SLD_G, (DR).

Remark 4.3 (what the new ingredients are). (1) Scale-dependent active set U = {l in B ∩ [1,l_*] : lambda_l >= t^2}: inactive swallowed carriers
are box-negligible in total (at most 6 l_* t), and active ones have lambda_l >= t^2, which converts the l_1-displacement of the projection into
the coordinate bound |omega| <= A_2/t needed by the one-sided expansion. (2) Configuration Hoffman constants G*(l) (part 2): the f-dependence of
the zero-cost cone is finite-combinatorial on T(U); the continuous f-data are isolated in gamma_T (rooms of free target points), the peak rows
(margins, M_f), the d-rows (repair, R_f) and gamma_f (gaps). (3) The uniform shift is pinned without (H2) through BASE peaks: at an anti-sign
swallowed peak the zero-cost condition (Z1) bounds (tau_l)_- by the projection distance, which bounds Delta d_m M_m from above; at a
swallowing-sign swallowed peak the margin bounds the excess e_k, which bounds Delta d_m M_m from below (Step 3).
