# S3 part 1: second-order rebalancing at engineered approximants (O2, first half)

Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; Preprint B Remark martin-tail). Only Lemma B's conclusion
about T (admissible T) is used. Notation of A_notes §1, P2_notes (=P2A) §1, C_notes §1, §7. For f in S_{p*}: xi, q_0 = q**(xi), a, nu = ||U*a||,
e = U*a/nu, zhat = xi/q_0 = z + Ue, w = (w_m), zeta_m = R_m** xi, sigma_m := |zeta_m|_m (so q_0 + sum_{m in I} sigma_m = 1), M_m, C_m, P_m, Q_m.
For an NA point f' = grad p(x') (x' in S_p): c' := q(x') = a'(x'), sigma'_m := |R_m x'|_m, c' + sum_m sigma'_m = 1, primes on all data.
Coefficients: h(b) := ||P_{e-perp}U*b||^2/nu, H_m(omega) := (||D_m omega||^2 - d_m(omega)^2)/C_m, d_m(omega) := <D_m w_m, D_m omega>/C_m, and the
MASS-WEIGHTED coefficient of a pair (b, omega = (omega_m)):
    Gamma_w(b, omega) := q_0 h(b) + sum_{m in I} sigma_m H_m(omega_m)     (C_notes Def 7.0; H_m := 0 if omega_m = 0).
For two-piece data (P2A 1.6) with sides (b+, omega+), (b-, omega-):
    kappa_max := max_{sigma = +-} max( h(b^sigma), max_m H_m(omega^sigma_m) )  (P2A's kappa),   kappa_w := max_{sigma = +-} Gamma_w(b^sigma, omega^sigma).
Always kappa_w <= kappa_max (q_0 + sum sigma_m = 1); kappa_w can be much smaller (C_notes: 0.298 vs 2.86).
Both h and H_m are positive semidefinite quadratic forms, so Gamma_w is convex and Gamma_w(b_theta, omega_theta) <= kappa_w for every theta in [0,1].

## 1.1 Lemma (rebalancing add-on at an arbitrary NA point). PROVED.
Let f' = grad p(x') be NA (data as above). Let m in I, gamma in (0, M'_m), eta > 0, and let V in l_inf (a "block piece") satisfy
  (a) ||V - w'_m||_inf <= eta,   (b) eta <= (M'_m - gamma)/4.
Put L' := {k : |w'_m(k)| >= gamma} and let k_* in L' be a peak of w'_m with w'_m(k_*) = +M'_m, Lambda >= 0, s' := sign w'_m.
 (i) (lowering) y := s' 1_{L'} + Lambda e_{k_*}. If 0 <= eps and eps (2 + Lambda) <= gamma - eta and eps <= (M'_m - gamma)/4, then
     ||V - eps y||_inf <= ||V||_inf - eps.
 (ii) (raising) y := s' 1_{L'} - Lambda e_{k_*}. If eps <= 0 and |eps| (Lambda + 1) <= gamma - eta, then ||V - eps y||_inf <= ||V||_inf - eps.
 (iii) (Hilbert part) If ||D_m V|| > 0 then ||D_m(V - eps y)|| <= ||D_m V|| - eps <D_m V, D_m y>/||D_m V|| + eps^2 ||D_m y||^2/(2||D_m V||), and
     | <D_m V, D_m y>/||D_m V|| - <D_m w', D_m y>/C'_m | <= 4 ||D_m(V - w'_m)|| ||D_m y||/C'_m  whenever ||D_m(V - w'_m)|| <= C'_m/2.
 (iv) (bookkeeping, C_notes (7.3)) If every peak of w'_m lies in L', then y(R_m x') = sigma'_m e'_y + (+-) Lambda m Phi_m(k_*) mu'_*, where
     e'_y := 1 + <D_m w'_m, D_m y>/C'_m and mu'_* := u_{k_*,m}(x') - theta'_m Phi_m(k_*) >= 0 is the margin of k_* at f' (sign + in (i), - in (ii)).
 (v) (exact re-splitting) For every eps_m (m in I) and every decomposition f' + tau g' = (a' + tau B) + sum_m R_m* V_m:
       f' + tau g' = (A + tau B) + sum_m R_m*(V_m - eps_m y_m),  A := a' + sum_m eps_m R_m* y_m = (1 + sum_m eps_m Y'_m/c') a' + sum_m eps_m e'_m,
     with Y'_m := y_m(R_m x'), e'_m := R_m* y_m - (Y'_m/c') a'; and, if 1 + sum eps_m Y'_m/c' =: lambda_A > 0,
       q*(A + tau B) <= lambda_A q*(a' + (tau/lambda_A) B) + sum_m |eps_m| q*(e'_m).
*Proof.* (i) For k in L', |w'(k)| >= gamma and |V(k) - w'(k)| <= eta give sign V(k) = s'(k) and |V(k)| >= gamma - eta >= eps; hence for
k in L' \ {k_*}: |V(k) - eps s'(k)| = |V(k)| - eps <= ||V||_inf - eps. At k_*: V(k_*) > 0 and V(k_*) - eps(1 + Lambda) <= ||V||_inf - eps;
also V(k_*) - eps(1+Lambda) >= -(||V||_inf - eps), because ||V||_inf + V(k_*) >= 2(gamma - eta) >= eps(2 + Lambda). For k notin L': |V(k)| <= |w'(k)| + eta < gamma + eta
<= M'_m - eta - eps <= ||V||_inf - eps (the last because ||V||_inf >= |V(k_*)| >= M'_m - eta, and gamma + 2 eta + eps <= M'_m by (b) and eps <= (M'-gamma)/4).
(ii) With e := |eps|: V - eps y = V + e y. For k in L' \ {k_*}: |V(k) + e s'(k)| = |V(k)| + e <= ||V||_inf + e. At k_*: V(k_*) + e(1 - Lambda) lies in
[-(||V||_inf + e), ||V||_inf + e] since V(k_*) + ||V||_inf + e(2 - Lambda) >= 2(gamma - eta) - e(Lambda - 2) >= 0 by the hypothesis. For k notin L': |V(k)| <= ||V||_inf.
(iii) ||h_0 - eps h||^2 = ||h_0||^2 - 2 eps <h_0,h> + eps^2 ||h||^2 and sqrt(A^2 + x) <= A + x/(2A) (A > 0, A^2 + x >= 0). For the second claim:
|<a,y>/|a| - <b,y>/|b|| <= |<a - b, y>|/|a| + |<b,y>| | 1/|a| - 1/|b| | <= |a-b||y|/|a| + |y||a-b|/|a| <= 4|a-b||y|/|b| when |a| >= |b|/2.
(iv) A Fact C at x': R_m x' = sigma'_m (alpha' + D^2 w'/C') with alpha' supported on P'_m, sign alpha'_k = s'(k), ||alpha'||_1 = 1. If P' is contained in L',
y(alpha') = sum_{P'} |alpha'_k| +- Lambda alpha'_{k_*} = 1 +- Lambda |alpha'_{k_*}|, y(D^2 w')/C' = <Dw', Dy>/C', and sigma'|alpha'_{k_*}| = |R x'(k_*)| - sigma' Phi_*^2 M'/C'
= m Phi_* (u_*(x') - theta' Phi_*) with theta' := M' sigma'/(m C') (A Fact C threshold).
(v) Algebra (R_m* y_m = (Y'_m/c') a' + e'_m), 1-homogeneity and the triangle inequality for q*. QED.

## 1.2 Lemma (transfer data at f; C_notes Thm 7.4 Step 1, several blocks). PROVED.
Let f in S_{p*}, let Omega_m be finite sets of strict non-peaks of w_m (m in I), and let eta_1 > 0. For each m in I and each sign varsigma in {+,-}
there are gamma_m, a peak k_{m,varsigma} and Lambda_{m,varsigma} >= 0 such that, with L_m := {k : |w_m(k)| >= gamma_m} and
y^varsigma_m := sign(w_m) 1_{L_m} + varsigma Lambda_{m,varsigma} e_{k_{m,varsigma}}:
 (a) max_{k in Omega_m} |w_m(k)| < gamma_m < M_m and |w_m(k)| != gamma_m for every k;
 (b) k_{m,varsigma} is a peak of w_m with w_m(k) = +M_m and margin mu_{m,varsigma} := u_{k,m}(xi) - theta_m Phi_m(k) > 0 (theta_m := M_m sigma_m/(m C_m));
 (c) the inefficiency eps_{1,m,varsigma} := Lambda_{m,varsigma} m Phi_m(k_{m,varsigma}) mu_{m,varsigma}/q_0 + q*(e^varsigma_m) <= eta_1, where
     e^varsigma_m := R_m* y^varsigma_m - ((R_m* y^varsigma_m)(xi)/q_0) a;
 (d) e_{y,m} := 1 + <D_m w_m, D_m y^varsigma_m>/C_m satisfies |e_{y,m} - e^0_{y,m}| <= eta_1 with e^0_{y,m} := 1 + sum_{k in L_m} Phi_m(k)^2 |w_m(k)|/C_m >= 1
     (independent of varsigma and of the transfer peak).
*Proof.* This is C_notes Thm 7.4 Step 1 (lowering: target T = tau_* + delta_0 q*(tau_*) a; raising: Step 6, target -tau_* + delta_0 q*(tau_*) a), done
block by block; (d): <D w, D y> - sum_L Phi^2|w| = varsigma Lambda Phi_*^2 M and Lambda Phi_* = lambda_*/m with lambda_* = q*(T) bounded, so the difference
is <= Phi_*(k_*) q*(T) M/m -> 0 as k_* -> infinity, and the transfer peak can be taken as deep as we wish (density of every tail, A Fact/T2).
The choice of gamma_m in (a) excludes countably many values. QED.

## 1.3 Lemma (persistence along converging NA data). PROVED.
Let f'_n = grad p(x'_n) be NA with x'_n -> xi weak* (as elements of l_inf after normalisation, as in P2A Lemma 1.2), a'_n -> a in l_1, w'_{n,m}(k) -> w_m(k)
for all k, C'_{n,m} -> C_m, M'_{n,m} -> M_m, sigma'_{n,m} -> sigma_m, c'_n -> q_0. With the data of 1.2 define at f'_n:
L'_{n,m} := {k : |w'_{n,m}(k)| >= gamma_m}, y'^varsigma_{n,m} := sign(w'_{n,m}) 1_{L'_{n,m}} + varsigma Lambda_{m,varsigma} e_{k_{m,varsigma}}. Then for n large:
 (a) k_{m,varsigma} is a peak of w'_{n,m} of sign + with margin mu'_{n,m,varsigma} -> mu_{m,varsigma}; every peak of w'_{n,m} lies in L'_{n,m}; Omega_m is disjoint from L'_{n,m};
 (b) R_m* y'_{n,m} -> R_m* y_m in l_1, D_m y'_{n,m} -> D_m y_m in l_2, Y'_{n,m}/c'_n -> (R_m* y_m)(xi)/q_0, e'_{n,m} -> e^varsigma_m in l_1, e'_{y,n,m} -> e_{y,m}.
*Proof.* (a) Peak criterion (P2A Lemma 1.1 / A Fact C): k is a peak iff C r(k) >= M with r(k) = m|u_k(x)|/(Phi_k |R x|). At f, k_* has strict
inequality (margin > 0); u_{k_*}(x'_n) -> u_{k_*}(xi) (u in l_1, weak* convergence), and C', M', sigma' converge, so strict inequality persists.
Peaks of w' have |w'| = M'_n > gamma_m for n large. Omega_m: |w'_n(k)| -> |w(k)| < gamma_m (finitely many k). (b) For each k, |w_m(k)| != gamma_m, so
1_{L'_n}(k) sign w'_n(k) -> 1_L(k) sign w(k) (if w(k) = 0 then k notin L and eventually notin L'_n); dominated convergence with the summable majorants
m Phi_m(k) ||u_{k,m}||_1 and Phi_m(k) gives the l_1 and l_2 limits; Y'_n = (R* y'_n)(x'_n) -> (R* y)(xi) since R* y'_n -> R* y in norm and
x'_n -> xi weak* boundedly. QED.

## 1.4 Theorem A (rebalanced engineered recovery). PROVED.
Let f in S_{p*} with F = supp a finite and let g in C(f) carry d-neutral two-piece data (P2A 1.6) with active block set I_0 (if |I_0| >= 2 assume
the steering hypothesis (S) of P2A Thm 2.1). If rho in (0,1) and rho^2 kappa_w < 1, then (f, rho g) is in cl NA((c_0,p), l_2^2).
In particular, if kappa_w <= 1 then g is in Ls(f) (every rho < 1).
*Proof.* If v = b+ - b- = 0, then b+ = b- vanishes on K (it is both z-signed and (-z)-signed there), so g is a balanced finite certificate
(C_notes Def 7.0) with Gamma_w(g) <= kappa_w; since g is in C(f), (f,g) is contractive, and C_notes Thm 7.4 gives (f, rho g) in cl NA (its proof uses
Gamma_w <= 1 only in Step 4, to choose the inefficiency with rho^2(Gamma_w + H eps_1) < 1; rho^2 Gamma_w < 1 suffices). Assume v != 0 and run the proof of P2A Thm 2.1 with the following changes.
Step 0'. delta := (1 - rho^2 kappa_w)/2. Apply Lemma 1.2 with Omega_m := union over sigma in {+,-,theta} of supp omega^sigma_m (m in I_0; empty otherwise)
and eta_1 to be fixed. For each piece sigma in {+, -, theta} solve the equalisation system (with e^0_{y,m} of 1.2(d)):
   H_{m,sigma}/2 - t_{m,sigma} e^0_{y,m} = Lev_sigma (m in I),   h_sigma/2 + sum_{m in I} t_{m,sigma} sigma_m e^0_{y,m}/q_0 = Lev_sigma,
where h_sigma := h(b^sigma), H_{m,sigma} := H_m(omega^sigma_m) (0 for m notin I_0). Eliminating t_{m,sigma} = (H_{m,sigma}/2 - Lev_sigma)/e^0_{y,m}:
q_0 h_sigma/2 + sum_m sigma_m H_{m,sigma}/2 = Lev_sigma (q_0 + sum_m sigma_m) = Lev_sigma, i.e. Lev_sigma = Gamma_w(b^sigma, omega^sigma)/2 <= kappa_w/2.
Put t_max := max |t_{m,sigma}| (depends on f, g only). Choose eta_1 so small that (i) the inefficiency terms satisfy
sum_m |t_{m,sigma}| (eps_{1,m} + |e_{y,m} - e^0_{y,m}| (sigma_m/q_0 + 1)) <= delta/64 for every sigma, using the transfer data with sign varsigma = sign t_{m,sigma}.
Additional constraint on T_0 (besides those of P2A Step 0): with eps_m := t_{m,sigma} rho^2 tau^2 and |tau| <= T_0, the hypotheses of Lemma 1.1(i)/(ii)
hold with eta := K_1 T_0 (K_1 := rho max_sigma max_m (||omega^sigma_m||_inf + 2|d_m| + 1)) and gamma := gamma_m, M' >= (M_m + gamma_m)/2, i.e.
   K_1 T_0 <= (M_m - gamma_m)/16,  t_max rho^2 T_0^2 (2 + max Lambda) <= (gamma_m - (M_m - gamma_m)/16)/2,  t_max rho^2 T_0^2 <= (M_m - gamma_m)/16,
and the error terms below are <= delta tau^2/64: 4 t_max rho^2 tau^2 (K_1 |tau| ||D y||/C'_m) + t_max^2 rho^4 tau^4 ||D y||^2/C'_m + (cross terms of order tau^4)
for |tau| <= T_0 (finitely many constants; all are bounded uniformly along the construction by 1.3(b)).
Steps 1-5 of P2A Thm 2.1 are unchanged (the steering, the target g', and the three decompositions (2.1.3)). For 0 < |tau| <= T_0 choose the piece
sigma = theta (|tau| <= s_1) or sigma = sign tau (|tau| > s_1) as in P2A Step 5, and re-split with Lemma 1.1(v), eps_m := t_{m,sigma} rho^2 tau^2, y_m := y'^{varsigma}_{n,m}
(varsigma := sign t_{m,sigma}), the block pieces V_m := w'_m + tau rho(omega^sigma_m - d'_m w'_m) (m in I_0), V_m := w'_m (m notin I_0), and B := B^sigma.
Blocks: ||V_m - w'_m||_inf <= K_1 |tau| and ||D(V_m - w'_m)|| <= K_1|tau| (late stages). Lemma 1.1 (i)/(ii) (L' contains all peaks and avoids Omega_m by 1.3(a)),
(iii) and P2A Step 4 give
   N_m(V_m - eps_m y_m) <= 1 + (rho^2 tau^2/2)(H'_m(omega^sigma_m)(1 + Kc T_0)) - eps_m e'_{y,m} + delta tau^2/64.
Base: by 1.1(v) with lambda_A = 1 + sum eps_m Y'_m/c' and P2A Step 5 applied at the parameter s := tau/lambda_A. Since |Y'_m/c'| is bounded
uniformly along the construction (1.3(b)), lambda_A in [0.99, 1.01] once t_max rho^2 T_0^2 sum_m sup|Y'_m/c'| <= 0.01 (one more constraint on T_0).
The no-flip estimates of P2A Step 5(a) hold at s because they hold with a factor-2 margin (window masses m_j = 4 rho s_1|b^theta_j| against the
needed 2 rho s_1 |b^theta_j|; far masses and F-coordinates likewise after replacing T_0 by T_0/2 in P2A's constraints); the kink estimate of Step 5(b)
gives Kink' <= rho|s| V_{>N''} <= eps_0 s_1 |s| <= 1.02 eps_0 tau^2 on the intermediate range (|tau| > s_1), and 0 for sigma = theta. Hence
   q*(A + tau B^sigma) <= lambda_A (1 + (rho^2 s^2/2) h'(B^sigma/rho)(1 + Kc T_0) + 1.02 eps_0 tau^2) + sum_m |eps_m| q*(e'_m)
                      <= 1 + sum_m eps_m Y'_m/c' + 1.01 (rho^2 tau^2/2) h'(B^sigma/rho)(1 + Kc T_0) + 1.04 eps_0 tau^2 + sum_m |eps_m| q*(e'_m),
and the factor 1.01 is absorbed into the delta/64 budget by the constraint (0.01 + Kc T_0) max_sigma h(b^sigma) <= delta/64 (replace 0.01 by a smaller
absolute constant if needed; lambda_A -> 1 as T_0 -> 0).
Late stages (Lemma 1.3, P2A Step 3): h'(B^sigma/rho) -> h(b^sigma), H'_m -> H_m, Y'_m/c' -> sigma_m e_{y,m}/q_0 +- Lambda m Phi_* mu_*/q_0, e'_y -> e_y, q*(e'_m) -> q*(e^varsigma_m).
Dividing by rho^2 tau^2, the base level is <= h_sigma/2 + sum_m t_{m,sigma} sigma_m e^0_{y,m}/q_0 + delta/32 and each block level is <= H_{m,sigma}/2 - t_{m,sigma} e^0_{y,m} + delta/32
(the deviations e_y - e^0_y and the inefficiencies are within the eta_1-budget, and the T_0-dependent factors are within delta/64 by the choice of T_0),
i.e. all levels are <= Lev_sigma + delta/32 <= kappa_w/2 + delta/32. Hence, by A Fact A (p* <= max of the pieces),
   p*(f' + tau g') <= 1 + (tau^2/2)(rho^2 kappa_w + delta/8 + 4 eps_0) <= 1 + (tau^2/2)(1 - delta)     (0 < |tau| <= T_0),
(eps_0 = delta/8 as in P2A), and P2A Step 6 / Lemma 1.4 conclude: g' in C(f'), (f', g') is NA and converges to (f, rho g). QED.

## 1.5 Corollary A' (the same upgrade for the other engineered theorems). PROVED modulo the hypotheses of the quoted theorems.
In N2 Thm 1 (Delta d = 0), N2 Thm 2 (Delta d > 0 under (TT) or (BR)), N2-referee Thm 3* (Delta d < 0 under (PC*)), N2-referee Corollary R, and P2x Thm 3.5
(Delta d_m >= 0 under (TC)), the hypothesis rho^2 kappa_max < 1 can be replaced by rho^2 kappa_w < 1.
*Proof.* In each of these proofs, for every 0 < |tau| <= T_0 the bound for p*(f' + tau g') is obtained from an exact decomposition
f' + tau g' = (a' + tau B) + sum_m R_m* V_m with: (1) a base estimate q*(a' + s B) <= 1 + (rho^2 s^2/2)(h(b^sigma) + o(1)) + r(s) with first-order remainders
r(s) <= c delta s^2 on the relevant range (kinks, B(xhat') terms, (PC)/(PC*)/(BR) terms), stable under s -> s/lambda_A with lambda_A in [1/2,2];
(2) block pieces V_m with ||V_m - w'_m||_inf + ||D_m(V_m - w'_m)|| <= K|tau| (in Lemma 3.2(a) of N2 and Thm 3*: V = (1-s)[(1-tau~ d')w' + tau~ omega] + s y'',
s = O(|tau|), ||y'' - w'||_inf <= 2, so the bound holds with K := rho(||omega||_inf + 2|d'| + 2|Delta d| + 1)) and N_m(V_m) <= 1 + (rho^2 tau^2/2)(H_m(omega^sigma_m) + o(1)) + r_m
with r_m <= c delta tau^2. Lemma 1.1 needs nothing else, so the re-splitting of 1.4 applies verbatim. QED.
Remark. Since kappa_w <= kappa_max always, Theorem A strictly contains P2A Thm 2.1 / N2 Thm 1. The quantity kappa_w is not yet the sharp one-sided
invariant (the given side data need not be optimal); part 2 identifies the sharp invariant and shows it is attained by side data.
