# S3 part 3: first-order rebalancing — engineering without steering (O4, and most of the Delta d problem)

Setting and notation of parts 1-2 (finite I, admissible T only). Throughout, f in S_{p*} has F = supp a FINITE; g in C(f) carries two-piece data
(b+, omega+), (b-, omega-) (P2A 1.6: b+- in l_1(F cup K), z-signed resp. (-z)-signed on K; omega+-_m finitely supported in Q_m; ANY set I_0 of active
blocks; ANY d-coefficients). theta := 1/2, b^theta := (b+ + b-)/2, omega^theta := (omega+ + omega-)/2, d^sigma_m := d_m(omega^sigma_m) (sigma in {+,-,theta}),
Delta d_m := d^-_m - d^+_m, v := b+ - b- (supported in F cup K, z-signed on K). kappa_w := max_+- Gamma_w(b^+-, omega^+-) (part 1).

## 3.0 The idea.
P2A/N2 need exact steering (v_m(xhat') = 0, i.e. d'^+_m = d'^-_m in every block) because a first-order mismatch of size O(s_1) between the two
side decompositions at f' costs |tau| O(s_1) at first order, comparable to the slack at |tau| ~ s_1 with a constant that does not improve as
rho -> 1. But such mismatches are LINEAR: the first-order terms of the base and block pieces of an exact decomposition of f' + tau g' always
satisfy the weighted identity c' l_base + sum_m sigma'_m l_m = g'(x') = 0. Transfer peaks (C Thm 7.4; part 1, Lemma 1.1) move first-order
amounts between base and blocks at a relative cost eps_1 that can be fixed in advance as small as we like. So an O(s_1) linear mismatch costs only
|tau| O(eps_1 s_1) <= (delta/64) tau^2 for |tau| >= s_1. What remains are GENUINE (nonlinear) first-order costs: kinks of the base and the
block cost of the term c (w'_m - w_m) produced by non-neutral data (Delta d_m != 0). The latter is o(s_1) when Delta d_m > 0 (Bregman term) and,
when Delta d_m < 0, is controlled by a refined anchor (Lemma 3.2) up to the lambda-mass of the coordinates SCRAMBLED by the perturbation.

## 3.1 Lemma (first-order bookkeeping at an NA point). PROVED.
Let f' = grad p(x') be NA, x' in S_p, c' = q(x'), sigma'_m = |R_m x'|_m, xhat' := x'/c'. For any exact decomposition f' + tau g' = (a' + tau B) + sum_m R_m*(w'_m + tau Omega_m)
put l_b := B(xhat') and l_m := Omega_m(R_m x')/sigma'_m. Then c' l_b + sum_m sigma'_m l_m = g'(x'). Moreover
 (a) q*(a' + tau B) = 1 + tau l_b + G_b(tau),  G_b(tau) := Fl'(tau) + Kink'(tau B) + nu' Psi'(tau U*B/nu') >= 0  (A Lemma 7.2 at f'; no hypothesis on B);
 (b) for every block, N_m(w'_m + tau Omega_m) = 1 + tau l_m + G_m(tau) with G_m(tau) >= 0 (convexity: R_m x'/sigma'_m is a subgradient of N_m at w'_m,
     since N_m(w'_m) = 1 = <w'_m, R_m x'>/sigma'_m and |<W, R_m x'>| <= N_m(W) |R_m x'|_m).
*Proof.* g'(x') = B(x') + sum_m Omega_m(R_m x') (L* duality) = c' l_b + sum sigma'_m l_m. (a) is A Lemma 7.2 (E_q(a' + tau B) = q*(a'+tau B) - (a'+tau B)(xhat'),
a'(xhat') = 1). (b): definition of G_m; nonnegativity by the subgradient inequality. QED.
"Genuine" first-order costs are the parts of G_b, G_m that are not O(tau^2).

## 3.2 Lemma (refined anchor; "R+"). PROVED (numerically checked, S3_work/lemma_Rplus.py).
Let w, w' be block functionals of one block with N(w) = N(w') = 1, M + C = 1 = M' + C', peak sets P, P', signs s, s', and gamma := C' - C with |gamma| <= C/4.
Put S_1 := {k in P cap P' : s_k = s'_k}, S_2 := {k notin P cup P' : |2w'(k) - w(k)| <= M' - |gamma|}, A := N \ (S_1 cup S_2), and
   y(k) := 2w'(k) - w(k) (k in S_1 cup S_2),   y(k) := (1 - gamma_+/M') w'(k) (k in A).
Then  N(y) <= 1 + X/(2(C + 2 gamma)),  X := ||D(w' - w)||^2 + ||D(y - w')||^2 + 2|R_A|,  R_A := <D w', D (w'-w) 1_A> + (gamma_+/M') ||D w' 1_A||^2,
and X <= 4 ||D(w'-w)||^2 + 4 sum_{k in A} Phi(k)^2. (Unlike N2-referee Lemma R there is no first-order term gamma_+.)
*Proof.* Sup part: on S_1, |y(k)| = 2M' - M = M' - gamma (M' - M = C - C' = -gamma; 2M' - M > 0); on S_2, |y(k)| <= M' - |gamma| <= M' - gamma; on A,
|y(k)| <= (1 - gamma_+/M') M' = M' - gamma_+ <= M' - gamma. So ||y||_inf <= M' - gamma.
Hilbert part: Y := y - w' = (w' - w) 1_{S_1 cup S_2} - (gamma_+/M') w' 1_A. ||Dy||^2 = C'^2 + 2<Dw', DY> + ||DY||^2 and
<Dw', DY> = <Dw', D(w'-w)> - R_A, <Dw', D(w'-w)> = C'^2 - <Dw', Dw> = (C'^2 - C^2 + ||D(w'-w)||^2)/2. Hence
||Dy||^2 = 2C'^2 - C^2 + ||D(w'-w)||^2 + ||DY||^2 - 2R_A <= (C + 2gamma)^2 - 2gamma^2 + X <= (C + 2 gamma)^2 + X, using 2(C+gamma)^2 - C^2 = (C+2gamma)^2 - 2gamma^2.
As C + 2gamma >= C/2 > 0: ||Dy|| <= C + 2gamma + X/(2(C + 2gamma)). Adding: N(y) <= M' - gamma + C + 2gamma + X/(2(C+2gamma)) = 1 + X/(2(C+2gamma)) (M' = 1 - C - gamma).
Bound on X: ||DY||^2 <= 2||D(w'-w)||^2 + 2(gamma_+/M')^2 ||Dw' 1_A||^2, |R_A| <= ||Dw' 1_A|| ||D(w'-w)|| + (gamma_+/M')||Dw'1_A||^2, ||Dw' 1_A||^2 <= M'^2 sum_A Phi^2,
gamma_+/M' <= 1 (|gamma| <= C/4 < M' since M' >= 1 - 5C/4 > C/4... for C <= 1/2; in Martin's blocks C_m <= 2^{-m} <= 1/2). QED.
Consequence (excess of the anchor). With E_y := N(y) - <y, R x'>/sigma' (x' a normer with J(R x') = w', sigma' = |R x'|) and Bx := <w' - w, R x'> >= 0:
   E_y <= 4(||D(w'-w)||^2 + sum_A Phi^2)/C + (1/sigma') sum_{k in A} |R x'(k)| (|w'(k) - w(k)| + gamma_+),
because <y - w', R x'> = Bx - <(w'-w)1_A, Rx'> - (gamma_+/M')<w' 1_A, Rx'> >= -sum_A |Rx'(k)|(|w'(k)-w(k)| + gamma_+).

## 3.3 The engineered approximants (simplified: NO far pulls, NO tuning mass, NO steering coordinates).
Parameters chosen in the order N, s_1, N'':
  window N >= max F; scale s_1 in (0, T_0]; window masses m_j := 4 rho s_1 |b^theta_j| (j in K cap [1,N]);
  a'' := a + sum_{j in K cap [1,N]} m_j z_j e_j*,  a' := a''/q*(a''),  z'_j := z_j (j <= N''),  z'_j := 0 (j > N''),
  e' := U*a'/||U*a'||, xhat' := z' + U e', x' := xhat'/p(xhat'), f' := grad p(x') = a' + sum_m R_m* w'_m (NA; A Fact D: z' in c_00, ||z'||_inf <= 1,
  z' = sign a' on supp a' = F cup {window contacts with m_j > 0}).
Facts along any sequence with N -> infinity, s_1 -> 0, N'' -> infinity (N'' chosen after s_1):
 (E1) ||a'' - a||_1 <= 4 rho s_1 ||b^theta||_1, hence ||e' - e|| <= K_e s_1 with K_e := 8 rho ||U|| ||b^theta||_1/nu (fixed);
 (E2) for every u in S_{q*}: |u(xhat') - u(zhat)| <= K_e s_1 + ||u 1_{(N'',inf)}||_1 (xhat' - zhat = U(e' - e) - z 1_{(N'',inf)}, |<U*u, h>| <= ||h||);
 (E3) P2A Lemma 1.2: f' -> f, w'_m -> w_m coordinatewise, C', M', sigma', c' converge; Lemma 1.3 of part 1 (transfer peaks persist);
 (E4) |sigma'_m - sigma_m| + |c' - q_0| <= K s_1 + tail(N'') and |d'_m(omega) - d_m(omega)| <= K(omega) s_1 + tail(N'') for each fixed finitely supported omega
      off the peaks, where d'_m(omega) = omega(R_m x')/sigma'_m (P2A 2.1 Step 2 via A Fact C) and d_m(omega) = omega(R_m** xi)/sigma_m.
      [Convexity sandwich <w_m, R(xhat' - zhat)> <= |R xhat'| - |R** zhat| <= <w'_m, R(xhat' - zhat)>, each bounded by sum_k lambda_k |u_k(xhat' - zhat)|, and (E2);
      tail(N'') := sum_{k,m} lambda_{k,m} ||u_{k,m} 1_{(N'',inf)}||_1 -> 0, made <= s_1^2 by the choice of N''.]
 (E5) (Bregman terms) Bx_m := <w'_m - w_m, R_m xhat'> satisfies 0 <= Bx_m <= sum_k lambda_k |w'_m(k) - w_m(k)| (K_e s_1 + ||u_k 1_{(N'',inf)}||_1) = o(s_1)
      (dominated convergence: w' -> w coordinatewise, |w' - w| <= 2, sum lambda_k < infinity; tail made <= s_1^2). [N2 Thm 2's (TT) => (BR) proof; here
      no far pulls exist at all, so (BR) holds for EVERY f with F finite.]

## 3.4 Theorem D (engineered recovery of arbitrary two-piece data). PROVED.
Let f in S_{p*} have F finite and let g in C(f) carry two-piece data with rho^2 kappa_w < 1. For each active block m with Delta d_m < 0 assume
 (SC_m) along the approximants of 3.3 (for SOME sequence of parameters with N -> infinity, s_1 -> 0):
        ||D_m(w'_m - w_m)||^2 + sum_{k in A_m} ( Phi_m(k)^2 + lambda_{k,m} (|w'_m(k) - w_m(k)| + (C'_m - C_m)_+) ) = o(s_1),
        A_m := the set A of Lemma 3.2 for (w_m, w'_m) ("scrambled coordinates": status changes, and non-peaks with |2w' - w| > M' - |C' - C|).
Then (f, rho g) is in cl NA((c_0,p), l_2^2). No hypothesis on K, on the number of active blocks ((S), (TC) dropped), on mass tuning ((TT), (BR) dropped),
or on rates of T is needed; for Delta d_m >= 0 in all blocks there is no hypothesis at all beyond F finite.
*Proof.* delta := (1 - rho^2 kappa_w)/2, eps_0 := delta/64.
Step 0 (fixed data). Transfer data of part 1, Lemma 1.2, in every block m in I (Omega_m := union of the supports of omega^+-_m), with inefficiency eta_1 > 0
chosen below; the second-order equalisation coefficients t_{m,sigma} of Theorem A (sigma in {+,-,theta}). Constants: K_l (bound for the linear terms, Step 3),
K_tr := sup over the construction of max_m (|Y'_m/c'| + q*(e'_m) + Lambda m Phi mu'/c')/e'_{y,m} (finite by part 1 Lemma 1.3). Choose eta_1 with
K_l K_tr eta_1 <= eps_0 and the second-order inefficiency budget of Theorem A. Then T_0 as in P2A Step 0 (radius, no-flip and constant constraints, with
kappa_w in place of kappa), as in Theorem A Step 0' (with K_1 enlarged by 4 rho max_m |Delta d_m| + 1, so that the block pieces of Step 4, which contain
s(y - w') or s(w - w') with |s| <= T_0 rho |Delta d_m| and ||y - w'||_inf <= 3, stay within eta = K_1 T_0 of w'), and additionally T_0 rho max_m |Delta d_m| <= 1/2 and T_0^2 <= 3 delta.
Step 1 (target). With d'^theta_m := d'_m(omega^theta_m) (computed at f'),
   g'' := b^theta 1_{[1,N]} + sum_m R_m*(omega^theta_m - d'^theta_m w'_m),  c := g''(xhat'),  g' := rho(g'' - c a').
Then g'(xhat') = 0 and g' -> rho g (P2A Step 3: g'' - g = -b^theta 1_{(N,inf)} + sum R_m*(d^theta_m w_m - d'^theta_m w'_m) -> 0, c -> g(zhat) = 0).
Step 2 (the three decompositions). theta-piece: Omega^theta_m := rho(omega^theta_m - d'^theta_m w'_m), B^theta := rho(b^theta 1_{[1,N]} - c a'). It is BALANCED:
l^theta_m = 0 (d'^theta is the f'-coefficient) and l^theta_b = 0 (3.1 with g'(x') = 0).
Side pieces (sigma = +-): Omega^sigma_m := Omega^theta_m + rho(omega^sigma_m - omega^theta_m) - rho (d^sigma_m - d^theta_m) w_m and B^sigma := g' - sum_m R_m* Omega^sigma_m.
Since omega^+ - omega^theta = -theta omega_Delta, d^+ - d^theta = -theta Delta d, and v = sum_m R_m*(omega_Delta,m - Delta d_m w_m):
   B^+ = B^theta + rho theta v,   B^- = B^theta - rho (1-theta) v     (exactly as in P2A (2.1.2)),
so the BASE parts are those of P2A: B^sigma = rho(beta^sigma - c a'), beta^theta = b^theta 1_{[1,N]}, beta^+ = b^+ 1_{[1,N]} + theta v 1_{(N,inf)}, beta^- = b^- 1_{[1,N]} - (1-theta) v 1_{(N,inf)}.
Rewrite the block parts with w = w' - (w' - w):
   Omega^sigma_m = rho(omega^sigma_m - dtil^sigma_m w'_m) + rho c^sigma_m (w'_m - w_m),   dtil^sigma_m := d'^theta_m + (d^sigma_m - d^theta_m),   c^sigma_m := d^sigma_m - d^theta_m,
i.e. c^+_m = -theta Delta d_m, c^-_m = (1-theta) Delta d_m (N2 Lemma 3.1's choice, with the mismatch theta(Delta d - Delta d') R*w' left in the block).
Step 3 (linear terms are O(s_1)). Write Omega^sigma_m = rho(omega^sigma - d'_m(omega^sigma) w') + kappa^sigma_m w' + rho c^sigma (w' - w) with
kappa^sigma_m := rho(d'_m(omega^sigma_m) - dtil^sigma_m) = rho[(d'_m(omega^sigma) - d_m(omega^sigma)) - (d'_m(omega^theta) - d_m(omega^theta))] (d linear in omega).
By (E4), |kappa^sigma_m| <= K s_1 + 2 tail(N''). The linear term of block m (3.1): l^sigma_m = kappa^sigma_m (1) + rho c^sigma_m <w' - w, R x'>/sigma'_m = kappa^sigma_m + rho c^sigma_m c' Bx_m/sigma'_m,
so |l^sigma_m| <= K_l s_1 at late stages by (E5); and |l^sigma_b| = |sum_m sigma'_m l^sigma_m|/c' <= K_l s_1 (3.1, g'(x') = 0).
Step 4 (genuine block costs, |tau| <= T_0, sigma = +-). Let s := tau rho c^sigma_m (|s| <= 1/2) and W_0 := w' + tau rho(omega^sigma - d'(omega^sigma) w') + tau kappa^sigma_m w'.
 * Case s <= 0 (convexity; this is the case for both sides when Delta d_m >= 0, and trivially when Delta d_m = 0): block piece W = W_0 + |s|(w - w') = (1-|s|) V_1 + |s| w
   with V_1 := w' + (tau rho(omega - d'w') + tau kappa w')/(1 - |s|). By A Lemma 4.4(c),(d) (coordinatewise radius, P2A Step 4) and 1-homogeneity,
   N(V_1) <= 1 + tau kappa/(1-|s|) + (rho^2 tau^2/(2(1-|s|)^2)) H'_m(omega^sigma)(1 + Kc T_0) (1 + K|tau kappa|); hence
   N(W) <= 1 + tau kappa^sigma_m + rho^2 tau^2 H'_m(omega^sigma)(1 + Kc T_0 + 2|s|)/2 + O(|tau|^3 s_1), and G_m := N(W) - 1 - tau l^sigma_m <= rho^2 tau^2 H'(...)/2 + |s| Bx_m c'/sigma'_m + O(|tau|^3 s_1).
 * Case s > 0 (anchor; occurs only if Delta d_m < 0): Lemma 3.2 for (w_m, w'_m) gives y and A = A_m; Z_A := (w'-w) 1_A + (gamma_+/M') w' 1_A, so that
   w' - w = (y - w') + Z_A. Block piece W := W_0 + s(y - w') = (1-s) V_1 + s y (V_1 := (W_0 - s w')/(1-s)), and the remainder s Z_A is moved to the base
   (B^sigma is replaced by B^sigma + tau rho c^sigma_m R_m* Z_A; the decomposition remains exact). Then N(W) <= 1 + tau kappa + rho^2 tau^2 H'(...)/2 + s(N(y) - 1) + O(|tau|^3 s_1),
   and, with the linear term of the block piece l(W) = kappa + s <y - w', R x'>/(tau sigma'), the genuine cost is
   G(W) <= rho^2 tau^2 H'(...)/2 + s E_y,  E_y <= 4(||D(w'-w)||^2 + sum_A Phi^2)/C + (1/sigma') sum_A lambda_k (|w'-w|(k) + gamma_+)  (3.2 Consequence, |R x'(k)| <= lambda_k).
   The base receives tau rho c R* Z_A with ||R* Z_A||_1 <= sum_A lambda_k (|w'(k) - w(k)| + gamma_+): genuine cost (kinks, no flips at late stages) <= 2 s ||R* Z_A||_1.
   By (SC_m), s E_y + 2 s ||R*Z_A||_1 <= |tau| o(s_1).
Step 5 (genuine base costs). For B^sigma the analysis of P2A Step 5 applies verbatim except that there are no far contacts (not needed) and the first-order
term B^sigma(xhat') = l^sigma_b is no longer 0 (it is linear and is kept in the bookkeeping): no flips; Kink' = 0 on the window, on F, on non-contacts
(beta^sigma vanishes there) and on contacts in (N, N''] (designated sign); Kink' <= rho |tau| V_{>N''} <= eps_0 s_1 |tau| beyond N'' (choose N'' after s_1 with
rho V_{>N''} <= eps_0 s_1, V_{>N''} := sum_{j in K, j > N''} |v_j|) for sigma = +-, and 0 for sigma = theta. Hilbert term <= (tau^2/2) h'(B^sigma)(1 + Kc T_0).
Step 6 (rebalancing at first and second order). For 0 < |tau| <= s_1 use the theta-piece (no linear terms, no genuine first-order costs); for s_1 < |tau| <= T_0
use sigma = sign(tau). Re-split with part 1, Lemma 1.1(v), with eps_m := tau l^sigma_m/e'_{y,m} + t_{m,sigma} rho^2 tau^2 (y_m the transfer vectors with sign
varsigma = sign eps_m). Block m: by Lemma 1.1(i)-(iii) (||W - w'||_inf + ||D(W - w')|| <= K|tau| at late stages; the radius conditions hold since |eps_m| <= T_0 K_l s_1 +
t_max rho^2 T_0^2), N_m(W - eps_m y_m) <= N_m(W) - eps_m e'_{y,m} + |eps_m| 4K|tau| ||D y||/C' + eps_m^2 ||Dy||^2/C', i.e.
   level_m <= 1 + G_m(tau) - t_{m,sigma} rho^2 tau^2 e'_{y,m} + O(tau^2 (|tau| + s_1)).
Base: by 1.1(v) and 3.1(a) at the parameter tau/lambda_A (lambda_A = 1 + sum eps_m Y'_m/c' in [0.99, 1.01]):
   level_b <= lambda_A + tau l^sigma_b + 1.01 G_b(tau) + sum_m |eps_m| q*(e'_m)
            = 1 + [tau l_b + sum_m tau l_m Y'_m/(c' e'_{y,m})] + sum_m t_{m,sigma} rho^2 tau^2 Y'_m/c' + 1.01 G_b + sum |eps_m| q*(e'_m).
The bracket: by 1.1(iv), Y'_m = sigma'_m e'_{y,m} +- Lambda m Phi mu', so it equals tau(l_b + sum_m sigma'_m l_m/c') + tau sum_m l_m (+-Lambda m Phi mu')/(c' e'_y) = 0 + O(|tau| K_l s_1 K_tr eta_1)
(3.1 with g'(x') = 0). Likewise sum_m |tau l_m/e'_y| q*(e'_m) <= |tau| K_l s_1 K_tr eta_1. So the first-order linear terms are removed at total cost
<= 2|tau| K_l K_tr eta_1 s_1 <= 2 eps_0 s_1 |tau| <= 2 eps_0 tau^2 (|tau| > s_1). The second-order parts are equalised exactly as in Theorem A (levels <= Gamma_w(sigma)/2 + delta/32
after division by rho^2 tau^2). The genuine first-order costs are: base kinks <= eps_0 s_1 |tau| (Step 5) plus 2 s ||R*Z_A||_1; blocks |s| Bx c'/sigma' (convexity case) or
s E_y (anchor case); all are <= |tau| o(s_1) <= eps_0 tau^2 for |tau| > s_1 at late stages ((E5), (SC_m)). Hence for 0 < |tau| <= T_0
   p*(f' + tau g') <= max(level_b, max_m level_m) <= 1 + (tau^2/2)(rho^2 kappa_w + delta/4 + 10 eps_0) <= 1 + (tau^2/2)(1 - delta).
Step 7 (conclusion). P2A Lemma 1.4 (slack for |tau| >= T_0, using g in C(f), p*(f' - f) -> 0, p*(g' - rho g) -> 0): g' is in C(f'), (f', g') attains its norm at x',
and (f', g') -> (f, rho g). QED.

## 3.5 Corollary D1 (two-piece data with Delta d_m >= 0: no hypothesis). PROVED.
If F is finite and g in C(f) carries two-piece data with Delta d_m >= 0 in every block and kappa_w <= 1, then g is in Ls(f). This contains P2A Thm 2.1,
N2 Thm 1, N2 Thm 2 (without (TT)/(BR)), P2x Thm 3.5 (without (TC)), and Theorem A of part 1, and it needs no condition on Q_m (infinitely many strict
non-peaks, near-threshold coordinates and degenerate peaks are all allowed: they enter only through (E4)-(E5), which hold for every f).

## 3.6 Corollary D2 ((BT) points are recoverable). PROVED.
If f satisfies (BT) (part 2, 2.1: F finite, every Q_m finite, no degenerate peaks, (MS); K arbitrary), then every g in C(f) is in Ls(f); i.e. f is in R.
*Proof.* Theorem B (part 2) gives optimal two-piece data with kappa_w <= 1. For blocks with Delta d_m < 0 verify (SC_m) along the approximants of 3.3:
(i) clamp formula (P2A 1.1): Phi_m(k) w_m(k) = sign(u_k(xi)) min(Phi_m(k) M_m, C_m m |u_k(xi)|/sigma_m) is Lipschitz in (M, C, sigma, u_k(.)) uniformly in k
(a min of two Lipschitz functions, both vanishing when u_k = 0), so by (E2)-(E4) Phi_m(k)|w'_m(k) - w_m(k)| <= K(s_1 + t_k), t_k := ||u_{k,m} 1_{(N'',inf)}||_1;
also <= 2 Phi_m(k). Hence ||D(w'-w)||^2 <= sum_k min(K^2 (s_1 + t_k)^2, 4 Phi_m(k)^2) <= 2K^2 s_1^2 #{k : Phi_m(k) >= s_1} + 8 sum_{Phi_m(k) < s_1} Phi_m(k)^2 + 2K^2 sum t_k^2 wedge ...
= O(s_1^2 log(1/s_1)) + (tail, <= s_1^2 by the choice of N''), using Phi_m(k) <= 2^{-m-k}. So ||D(w'-w)||^2 = o(s_1).
(ii) Scrambled coordinates: a peak k with margin mu_k > K'(s_1 + t_k) stays a peak of the same sign (A Fact C threshold; u_k(x') - u_k(xi) and theta' Phi - theta Phi are
<= K'(s_1 + t_k)/2), and a strict non-peak k in Q_m (finitely many, gap >= gamma_0) has |w'(k) - w(k)| = O(s_1) < gamma_0/4 and |gamma| = O(s_1) (C' -> C at rate O(s_1):
C' and C are determined by the identities C^2(1 - sum_Q rho_k^2) = (1-C)^2 A, A = sum_P Phi^2, with rho, A perturbed by O(s_1) + o(s_1) — N2-referee Cor R), so
|2w'(k) - w(k)| <= M' - |gamma| at late stages. (A hypothesis-free proof of |C' - C| = O(s_1) is in part 4, Prop 4.2(b).) Hence A_m is contained in {k in P_m : mu_k <= K'(s_1 + t_k)}, and
sum_{A_m} (Phi^2 + lambda_k(|w'-w| + gamma_+)) <= 3m sum{Phi_m(k) : mu_k <= 2K' s_1} + 3m sum{Phi_m(k) : mu_k <= 2K' t_k} = o(s_1) + (-> 0 as N'' -> infinity, by
dominated convergence and the absence of degenerate peaks; made <= s_1^2 by choosing N'' after s_1). So (SC_m) holds. Theorem D applies with rho^2 kappa_w < 1. QED.
(D2 contains C Thm 8.4 (K = empty) and part 2's Corollary B2 (P1's example), and covers every (BT) point, in particular all C-tame points without degenerate
peaks, whatever the contact set.)

## 3.7 Remarks.
 (a) The steering machinery of P2A/N2 (far sign-flipped contacts with negative masses, raising mass and intermediate value theorem, steering coordinates
     (S), tuning cones (TC), two-sided mass tuning (TT)) is unnecessary: it is replaced by first-order rebalancing through transfer peaks, which costs
     |tau| x (linear mismatch) x (inefficiency), the inefficiency being fixed before the scale s_1.
 (b) Why this does not contradict P1-referee R3 (canonical truncations fail): the approximants of 3.3 are still engineered (window masses) — what is
     dropped is only the exact cancellation of the O(s_1) mismatch.
 (c) What remains for two-piece data: only (SC_m) in blocks with Delta d_m < 0 (part 4). For general mates: whether every mate has two-piece data
     (Theorem B needs (BT)) — part 4 (O1).
