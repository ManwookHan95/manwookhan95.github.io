# S3 notes — rebalancing at engineered approximants, the exact one-sided invariant, engineering without steering (O1, O2, O4)

Round 3, task S3. Setting: canonical base q, Martin's norm with a FINITE block set I (p_N; Preprint B Remark martin-tail reduces density for p to
density for all p_N). About T only Lemma B's conclusion is used ("admissible T"). Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: ctx/r3/S3_part1.md .. S3_part4.md (assembled below). Scripts: scratchpad/S3_work/ (gamma_side.py, lemma_Rplus.py).
Imports (all refereed in Rounds 1-2): A Facts A-F, A Lemmas 4.2-4.4, 4.7, 7.2, A Thm 4.10, 6.8, Cor 6.10; C Thm 7.1, 7.4 (Steps 1-6), C Lemma 5.1, 5.2, 6.1,
C Prop 8.1 parts (i), (ii), (v) (the parts the C referee re-derived; part (iii), the decoupling, is NOT used); P2A Lemmas 1.1-1.4; N_part1 Thm 1
(g in Ls(f) iff (f, rho g) in cl NA for all rho < 1; density iff Ls(f) = C(f) for all f); P1 2.1-2.2, 6.0-6.1; N2 Lemma 3.1-3.2; N2-referee Lemma R.

## 0. Summary

**O2 (second-order rebalancing at engineered approximants) — solved for two-piece data.**
 * Rebalancing add-on (Lemma 1.1, PROVED): at ANY point (NA or not), transfer peaks (C Thm 7.4) can be attached to ANY decomposition whose block pieces
   stay O(|tau|)-close to w'_m; levels are moved between base and blocks at a relative cost eps_1 fixed in advance.
 * Theorem A (PROVED): P2A Thm 2.1 / N2 Thm 1 (and, Cor A', N2 Thm 2, N2-ref Thm 3*, P2x Thm 3.5) hold with the max-form coefficient kappa_max replaced by the
   mass-weighted kappa_w := max_+- [q_0 h(b^+-) + sum_m sigma_m H_m(omega^+-_m)].
 * Theorem B (PROVED): the EXACT one-sided second-order coefficient. At every f with F finite, all Q_m finite, no degenerate peaks and (MS) — "(BT)",
   with ARBITRARY contact set K —
      lim_{t -> 0+-} 2(p*(f + t g) - 1)/t^2 = gamma^+-(g) := min over side-+- admissible decompositions of q_0 h(b) + sum_m sigma_m H_m(omega_m),
   the minimum being attained. Proof by Fenchel duality (no decoupling needed), which also repairs the C-referee gap in C Prop 8.1 and explains the
   referee's kink phenomenon (Gamma_2 < Gamma_w): numerically gamma^+ = 0.29567, gamma^- = 0.28325 reproduce the referee's exact one-sided coefficients
   (0.29567/0.29568 and 0.28325/0.28324) in his all-kinks model (2.7).
 * Corollary B2 (PROVED): at P1's example EVERY g in C(f) is recovered (f is in R). This answers the task's question and upgrades P2A 2.4 (SKETCH).

**O4 (several active blocks without (S)/(TC)) — solved, and much of the Delta d problem with it.**
 * Theorem D (PROVED): FIRST-ORDER rebalancing removes the need for steering. Engineered approximants with window masses and a far truncation ONLY
   (no far sign-flipped contacts, no tuning mass, no steering coordinates) recover every two-piece mate with rho^2 kappa_w < 1, for ANY number of active
   blocks and ANY d-coefficients, provided the blocks with Delta d_m < 0 satisfy a scrambling condition (SC_m). For Delta d_m >= 0 in all blocks there
   is no hypothesis at all beyond F finite (Corollary D1): this contains P2A Thm 2.1, N2 Thms 1-2, P2x Thm 3.5 and drops (S), (TC), (TT), (BR).
 * Lemma 3.2 ("R+", PROVED, numerically checked to 2.2e-16): the anchor of N2-referee Lemma R can be modified so that the first-order term (C'-C)_+ disappears.
 * Corollary D2 (PROVED): every (BT) point is recoverable (all mates in Ls(f)). This contains C Thm 8.4 (which needed K = empty) and Corollary B2.

**O1 (generic supports) — reduced to one explicit quantity.**
 * Infinitely many strict non-peaks are harmless for two-piece mates with Delta d_m >= 0 (D1), and for Delta d_m < 0 under (MS) + (MS-Q*) along SOME sequence of
   scales (Prop 4.2): Scr_m(s) := lambda-mass (truncated at s) of near-threshold peaks (mu <= s) and of non-peaks with Phi gap <= s or gap <= s must be o(s).
 * Without it, recovery holds for rho below an explicit threshold (4.3): the defect can only be a "rho near 1" phenomenon.
 * (MS-Q*) CAN fail for admissible T (4.4, SKETCH: prescribe a dense family of block vectors in zhat-perp at even indices), and then the simplified
   approximants do not recover Delta d < 0 mates for rho near 1; whether other approximants do is OPEN (a T-independent "compensation property" of U would suffice, HEURISTIC).
 * The deep-coefficient borderline c_k ~ sqrt(Phi_k) of C 9.2 is covered for certificate-type mates by A Cor 6.10(a) (PROVED, refereed); mixed
   deep + switching mates are OPEN.

**Density of NA((c_0,p), l_2^2):** still OPEN. Nothing found points to a counterexample; the open core shrinks to (i) Delta d < 0 switching mates at blocks
violating (MS-Q*), (ii) mates at generic supports that are not limits of two-piece data (scale-dependent, = O3), (iii) mixed deep + switching mates.

| # | Statement | Status | Where |
|---|---|---|---|
| 1 | Rebalancing add-on lemma (any point, any block pieces O(tau)-close to w') | PROVED | 1.1 |
| 2 | Transfer data with prescribed inefficiency in every block; persistence along converging NA data | PROVED | 1.2, 1.3 |
| 3 | Theorem A: engineered recovery with kappa_w (weighted) instead of kappa_max | PROVED | 1.4 |
| 4 | Cor A': same upgrade for N2 Thm 2, N2-ref Thm 3*, Cor R, P2x Thm 3.5 | PROVED mod. their hypotheses (superseded by D) | 1.5 |
| 5 | Theorem B: exact one-sided coefficient = gamma^+- at (BT) points, any K; minimiser exists | PROVED (+ numerics) | 2.3, 2.7 |
| 6 | Every g in C(f) at a (BT) point has optimal two-piece data with kappa_w <= 1 | PROVED | 2.3(c), 2.4 |
| 7 | P1's example: every mate recovered (f in R) | PROVED | 2.6 |
| 8 | First-order bookkeeping identity c' l_b + sum sigma'_m l_m = g'(x') | PROVED | 3.1 |
| 9 | Lemma R+: anchor without the (C'-C)_+ term | PROVED (+ numerics) | 3.2 |
| 10 | Theorem D: engineering without steering; any blocks; Delta d >= 0 free; Delta d < 0 under (SC) | PROVED | 3.4 |
| 11 | D1: Delta d_m >= 0 two-piece mates recovered with no hypothesis on Q, K, T | PROVED | 3.5 |
| 12 | D2: every (BT) point is in R | PROVED | 3.6 |
| 13 | (MS) + (MS-Q*) along a sequence of scales => (SC) | PROVED | 4.2 |
| 14 | Quantitative recovery without (SC) (rho below explicit threshold) | PROVED | 4.3 |
| 15 | (MS-Q*) can fail for admissible T; simplified approximants then fail for Delta d < 0, rho near 1 | SKETCH | 4.4 |
| 16 | Whether some engineering always handles Delta d < 0 at (MS-Q*)-violating blocks | OPEN | 4.4 |
| 17 | Compensation property of U as a T-independent route | HEURISTIC | 4.4 |
| 18 | Deep coefficients c_k ~ sqrt(Phi_k): certificate-type mates in cl Cert(f) (A Cor 6.10(a)); weighted Gamma_w upgrade | PROVED / SKETCH | 4.5 |
| 19 | Mixed deep + switching mates; mates at generic supports beyond two-piece data | OPEN | 4.5, 4.6 |

Corrections to earlier notes (all PROVED by the results above):
 * C_notes 9.2 "the borderline c_k ~ sqrt(Phi_k) is not covered by any known technique": superseded by A Cor 6.10(a) (certificate-type mates).
 * C Prop 8.1 lower bound: its decoupling gap (C referee 1.20) is bypassed; the correct sharp coefficient at supports with infinitely many kinks is
   gamma^+- (one-sided, minimised over side-admissible decompositions), not Gamma_w of a fixed certificate (Theorem B).
 * N2-referee Lemma R / Theorem 3* / Cor R: the scalar condition (C'-C)_+ = o(t_n) and the tuning Delta d' = Delta d are unnecessary (Lemma R+, first-order rebalancing).
 * P2A Thm 2.1 / N2 Thm 1-3 / P2x Thm 3.5: hypotheses (S), (TC), (TT), (BR), far pulls and exact steering are unnecessary (Theorem D).
 * P1 6.3 Remark and P2A 2.4 ("recovery of all of C(f) at P1's example would follow ... not proved"): PROVED (Cor B2/D2), without shifted transport.
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
# S3 part 2: the exact one-sided second-order invariant (O2, second half) and complete recovery at P1's example

Setting and notation of part 1 (finite I, admissible T). Lemma 1.1 of part 1 holds verbatim at ANY f in S_{p*} with normer xi in place of x'
(replace c' by q_0, sigma'_m by sigma_m): its proof only uses A Fact C at the normer.

## 2.1 Definition (block-tame with arbitrary contacts: hypothesis (BT)).
f in S_{p*} satisfies (BT) if: F = supp a is finite; every Q_m (strict non-peaks of w_m) is finite; no block has degenerate peaks
(every peak k has margin mu_{k,m} := |u_{k,m}(xi)| - theta_m Phi_m(k) > 0, theta_m := M_m sigma_m/(m C_m)); and margin sparsity holds in every block:
   (MS)  sum{ Phi_m(k) : k in P_m, mu_{k,m} < s } = o(s)  as s -> 0+.
NO assumption is made on the contact set K = {j notin F : |z_j| = 1} (it may be infinite, even cofinite) or on z off F cup K.
(C-tame points (C_notes Def 6.0 with Dg = empty) are the (BT) points with K finite; P1's example (P1 2.2) is (BT) with K infinite, see 2.6.)

## 2.2 Definition (side-admissible decompositions; the one-sided invariant).
Let f satisfy (BT) and g in X* = l_1 with g(xi) = 0. For omega = (omega_m)_{m in I}, omega_m in R^{Q_m} (extended by 0), put d_m := d_m(omega_m) =
<D_m w_m, D_m omega_m>/C_m and b(omega) := g - sum_m R_m*(omega_m - d_m w_m) in l_1. The decomposition omega is SIDE-+ (resp. SIDE--) ADMISSIBLE if
   b(omega)_j = 0 for every j notin F cup K,   and  z_j b(omega)_j >= 0 (resp. <= 0) for every j in K.
Note b(omega)(zhat) = g(zhat) - sum_m <omega_m - d_m w_m, zeta_m>/q_0 = 0 automatically (A Lemma 4.2: <omega - d w, zeta_m> = 0).
The ONE-SIDED INVARIANTS are
   gamma^+(g) := inf{ Gamma_w(b(omega), omega) : omega side-+ admissible },  gamma^-(g) := inf{ ... side-- admissible }   (inf of the empty set = +infinity).
Two-piece data in the sense of P2A 1.6 are exactly pairs (omega+ side-+ admissible, omega- side-- admissible); kappa_w of part 1 is
max(Gamma_w(+), Gamma_w(-)), so min over two-piece data of kappa_w equals max(gamma^+, gamma^-) when both infima are attained.

## 2.3 Theorem B (exact one-sided second-order coefficient). PROVED.
Let f satisfy (BT) and g in l_1 with g(xi) = 0. Then
  (a) lim_{t -> 0+} 2(p*(f + t g) - 1)/t^2 = gamma^+(g)  and  lim_{t -> 0-} 2(p*(f + t g) - 1)/t^2 = gamma^-(g)   (in [0, +infinity]);
  (b) if gamma^+-(g) < infinity the infimum defining it is attained;
  (c) consequently every g in C(f) satisfies gamma^+(g) <= 1 and gamma^-(g) <= 1, and therefore carries two-piece data (P2A 1.6: b+- in l_1(F cup K),
      z-signed resp. (-z)-signed on K; omega+-_m finitely supported in Q_m) with kappa_w <= 1.
Remarks. (i) For K finite (C-tame), (c) recovers P1 3.8 (b(omega)_K must be both z- and (-z)-signed, so 0) and C Prop 8.1 with the referee's
missing hypothesis removed differently: the lower bound no longer needs decoupling. (ii) The C_referee counter-phenomenon (1.20: Gamma_2 < Gamma_w
at supports with many kinks) is exactly gamma^+- < Gamma_w(certificate): the optimal side decompositions re-split the certificate through
contacts with the cheap sign. Numerical confirmation in 2.7.

*Proof of the upper bound (limsup <= gamma^+).* Let omega be side-+ admissible with Gamma := Gamma_w(b, omega) < infinity, b := b(omega).
Base: for 0 < t < min_F|a_j|/(||b||_inf + 1) no coordinate of F changes sign, b vanishes off F cup K and z_j b_j = |b_j| on K, F and K are disjoint, so
||a + t b||_1 = ||a||_1 + t sum_F sign(a_j) b_j + t sum_K z_j b_j = ||a||_1 + t b(z). By (C 7.2), ||U*(a + t b)|| <= nu + t <e, U*b> + t^2 ||P_perp U*b||^2/(2(nu - t||U*b||)).
Adding and using b(z) + <e, U*b> = b(zhat) = 0: q*(a + t b) <= 1 + (t^2/2) h(b) nu/(nu - t||U*b||).
Blocks: V_m := w_m + t(omega_m - d_m w_m) satisfies N_m(V_m) <= 1 + (t^2/2) H_m(omega_m) C_m/(C_m - t||D_m(omega_m - d_m w_m)||) for small t (C Thm 7.1 Step 4
with N = infinity; omega_m is supported on finitely many strict non-peaks). Now f + t g = (a + t b) + sum_m R_m* V_m. Apply Lemma 1.1 (at f) with the transfer
data of Lemma 1.2 (Omega_m := Q_m) and eps_m := t_m t^2, the t_m solving the equalisation system of 1.4 for (h(b), H_m(omega_m)); exactly as in the
proof of Theorem A (with f' = f, no engineering), all pieces are <= 1 + (t^2/2)(Gamma + eta) + O(|t|^3) for any prescribed eta > 0 (eta controls the
inefficiency eta_1 of the transfer peaks). By A Fact A, limsup_{t->0+} 2(p*(f + t g) - 1)/t^2 <= Gamma + eta. Take the infimum over omega and eta -> 0.
(This is C Cor 7.2(c) for side-admissible rather than F-supported base parts.) Side - is symmetric (t < 0, (-z)-signed).

*Proof of the lower bound (liminf >= gamma^+).* Step 1 (test points). Let C_+ := { nu_c in c_00 : nu_c = 0 on F, z_j nu_{c,j} <= 0 for j in K } (inward moves of
contacts, arbitrary finitely supported moves of the other coordinates off F), and let k in H with <k, e> = 0. Put nu := U k + nu_c (in c_0),
kappa_2 := nu ||k||^2/(2 q_0) [here nu = ||U*a||], and choose k_2 in H with <U*e_j*, k_2> = -kappa_2 sign(a_j) (j in F) and <e, k_2> = kappa_2 - ||k||^2/(2q_0):
k_2 := kappa'_2 e + k_{2,perp}, kappa'_2 := -kappa_2 ||a||_1/nu, k_{2,perp} in E_F := span{U*e_j* : j in F} solving the Gram system
<k_{2,perp}, U*e_j*> = -kappa_2 sign(a_j) - kappa'_2 (Ue)_j (j in F) (U* injective, so the Gram matrix is invertible); it is orthogonal to e because
sum_F a_j(-kappa_2 sign a_j - kappa'_2 (Ue)_j) = -kappa_2 ||a||_1 - kappa'_2 nu = 0; and then ||k||^2/(2q_0) + <e,k_2> = ||k||^2/(2q_0) - kappa_2||a||_1/nu = kappa_2 because
||a||_1 + nu = q*(a) = 1. (This is C Prop 8.1 (i), re-derived by C_referee 1.20, with k no longer restricted to E_F.) For t > 0 put
   H_t := q_0 e + t k + t^2 k_2,   nu_2 := (U k_2) 1_{N \ F},   eta_t := xi + t nu + t^2 nu_2,   Z_t := eta_t - U H_t.
Coordinates: for j in F, Z_{t,j} = q_0 sign(a_j) + t^2 kappa_2 sign(a_j); for j notin F, Z_{t,j} = q_0 z_j + t nu_{c,j}. Since nu_c is finitely supported, inward on K
(where |z_j| = 1) and |z_j| < 1 on its support off F cup K, for 0 < t <= t_0(nu_c): |Z_{t,j}| <= q_0 for j notin F. Also ||H_t|| = q_0 + t^2 kappa_2 + O(t^3) (k orthogonal to e).
As B_{q**} = B_{l_inf} + U(B_H), q**(eta_t) <= max(||Z_t||_inf, ||H_t||) <= q_0 + t^2 kappa_2 + O(t^3). Since a is supported on F, a(nu_c) = 0, a(nu_2) = 0, and
a(U k) = <U*a, k> = 0, we get a(eta_t - xi) = 0 and the base excess E_q(eta_t - xi) := q**(eta_t) - q_0 - a(eta_t - xi) <= (t^2/2) (nu/q_0)||k||^2 + O(t^3).
Step 2 (blocks). With delta_1 := R_m nu, delta_2 := R_m nu_2 (both in l_1, nu, nu_2 in c_0), C Prop 8.1 (ii) (general Lemma 5.1(a) with overshoot; Q_m finite;
no degenerate peaks; (MS); re-derived by C_referee 1.20) gives E_m(t delta_1 + t^2 delta_2) <= (t^2/2) Hb_m(delta_1) + o(t^2), where Hb_m is the block quadratic
form of C Lemma 5.1(iii) (with the degenerate case z_Q = 0 as in C Prop 8.1 (v)). Hb_m(delta) depends on delta only through the finitely many numbers
ell_m(nu) := ( (u_{k,m}(nu))_{k in Q_m}, pi_m(nu) ), pi_m := R_m*(sign(w_m) 1_{P_m}) in l_1 (delta_Q = (m Phi_m(k) u_{k,m}(nu))_Q and S_P(delta) = pi_m(nu)).
Write Hb_m(R_m nu) = Qf_m(ell_m(nu)) with Qf_m a positive semidefinite quadratic form on R^{|Q_m|+1}.
Step 3 (the test inequality). C (8.1): since g(xi) = 0 and p** = f + Delta with Delta(eta) = E_q(eta - xi) + sum_m E_m(R_m**(eta - xi)) (C Lemma 6.1; exact),
p*(f + t g) >= (f + t g)(eta_t)/p**(eta_t) = 1 + t^2 g(nu) - Delta(eta_t) + O(t^3). Hence, for every admissible test pair (k, nu_c),
   liminf_{t->0+} 2(p*(f + t g) - 1)/t^2 >= Phi(k, nu_c) := 2 g(U k + nu_c) - (nu/q_0)||k||^2 - sum_m Qf_m(ell_m(U k + nu_c)).
Step 4 (Fenchel duality). Let ell := (ell_m)_m : c_0 -> R^n (n := sum_m (|Q_m| + 1)), Qf := sum_m Qf_m on R^n, and define on R^n the concave function
   Psi(y) := sup{ 2 g(U k + nu_c) - (nu/q_0)||k||^2 : k perp e, nu_c in C_+, ell(U k + nu_c) = y }  (sup of the empty set = -infinity).
Psi is concave (the constraint set is convex, the objective jointly concave), Psi(0) >= 0. If Psi(y_0) = +infinity for some y_0 then sup Phi = +infinity and
the lower bound holds trivially. Otherwise Psi is a proper concave function and Qf is finite and convex on all of R^n, so ri(dom Qf) meets ri(dom Psi);
by Fenchel's duality theorem (Rockafellar, Convex Analysis, Thm 31.1)
   sup_y [Psi(y) - Qf(y)] = min_{lambda in R^n} [ Qf^*(lambda) - Psi_*(lambda) ],
with Qf^*(lambda) := sup_y [<lambda, y> - Qf(y)], Psi_*(lambda) := inf_y [<lambda, y> - Psi(y)], and the minimum attained. Clearly sup_{k,nu_c} Phi = sup_y [Psi - Qf].
Compute both conjugates. Write phi_lambda := sum_i lambda_i ell_i in l_1 (ell_i ranging over the u_{k,m}, k in Q_m, and pi_m), so <lambda, ell(nu)> = phi_lambda(nu).
 * -Psi_*(lambda) = sup_{k perp e, nu_c in C_+} [ 2(g - phi_lambda/2)(U k + nu_c) - (nu/q_0)||k||^2 ] =: Bconj(g - phi_lambda/2). For beta in l_1:
   sup over k perp e of 2<U*beta, k> - (nu/q_0)||k||^2 equals (q_0/nu)||P_perp U*beta||^2 = q_0 h(beta); sup over nu_c in the cone C_+ of 2 beta(nu_c) is 0 if
   beta(nu_c) <= 0 on C_+, i.e. beta_j = 0 for j notin F cup K and z_j beta_j >= 0 on K, and +infinity otherwise. So Bconj(beta) = q_0 h(beta) on side-+ admissible beta,
   +infinity otherwise.
 * Qf^*(lambda) = sum_m sup_{y_m} [<lambda_m, y_m> - Qf_m(y_m)]. Block m: every linear functional of the block data (delta_Q, S_P(delta)) is
   delta -> 2 v(delta) with v = R_m*(omega~ + c w_m)-type, i.e. v(delta) = <omega~, delta> + c w_m(delta) restricted, omega~ on Q_m; C Prop 8.1 (v) (re-derived by the
   C referee, including the degenerate case) shows sup_delta [2 v(delta) - Hb_m(delta)] = sigma_m H_m(omega~) if v is BALANCED (v(zeta_m) = 0, i.e. c = -d_m(omega~)),
   and +infinity otherwise (Hb_m vanishes on the radial direction delta = zeta_m, along which 2v(delta) = 2 s v(zeta_m) is unbounded). Hence
   Qf^*(lambda) = sum_m sigma_m H_m(omega_m) if phi_lambda/2 = sum_m R_m*(omega_m - d_m(omega_m) w_m) for some omega_m in R^{Q_m}, and +infinity otherwise
   (phi_lambda determines the omega_m: T injective and Q_m is not all of N).
Therefore min_lambda [Qf^* - Psi_*] = min over omega with g - sum_m R_m*(omega_m - d_m w_m) side-+ admissible of [q_0 h(b(omega)) + sum_m sigma_m H_m(omega_m)] = gamma^+(g),
and the minimum is attained. With Step 3: liminf_{t->0+} 2(p*(f+tg) - 1)/t^2 >= sup Phi = gamma^+(g). Side -: replace C_+ by C_- (z_j nu_{c,j} >= 0) and t by -t
(the test points eta_t := xi + t nu + t^2 nu_2 with t < 0 move the contacts inward iff z_j nu_{c,j} >= 0). This proves (a) and (b).
(c): g in C(f) gives p*(f + t g) <= s(t) = 1 + t^2/2 + O(t^4), so both one-sided limits are <= 1. QED.

Comment on rigor. The only imported steps are C Prop 8.1 (i), (ii), (v) and C Lemma 6.1, (8.1), all re-derived by the C referee (1.20 lists them as
correct); the referee's gap was step (iii) (decoupling), which is replaced by Step 4 here. The weak-duality direction of Step 4 is elementary:
for side-+ admissible omega and any test pair, 2g(nu) = 2b(nu) + sum_m 2 v_m(nu) with 2b(nu) <= 2<U*b,k> (b(nu_c) <= 0) <= q_0 h(b) + (nu/q_0)||k||^2 and
2 v_m(nu) <= sigma_m H_m(omega_m) + Qf_m(ell_m(nu)).

## 2.4 Corollary B1 (structure of the fibre at (BT) points). PROVED.
If f satisfies (BT), then every g in C(f) satisfies g(xi) = 0, gamma^+(g) <= 1 and gamma^-(g) <= 1, and has two-piece data with kappa_w <= 1 whose
two sides are OPTIMAL side decompositions. (Conversely, if g(xi) = 0 and gamma^+-(g) < 1, then p*(f + t g) <= s(t) for all small |t|; membership in C(f)
then only depends on the large-|t| behaviour.) For P1's example this is P1 Thm 6.1 (C(f) in E_u) with the exact second-order constraint added.

## 2.5 Theorem C (recovery at (BT) points). PROVED under the stated alternatives.
Let f satisfy (BT), g in C(f), and let (omega+, omega-) be optimal side decompositions (2.3(b)); write Delta d_m := d_m(omega-_m) - d_m(omega+_m) and let I_0 be the
set of blocks where omega+_m or omega-_m is nonzero. Then g is in Ls(f) (i.e. (f, rho g) in cl NA for every rho < 1) in each of the cases
 (C1) Delta d_m = 0 for all m and |I_0| <= 1, or |I_0| >= 2 with the steering condition (S) of P2A 2.1;  [part 1, Theorem A]
 (C2) |I_0| = 1, Delta d > 0, and (TT) or (BR) of N2 Thm 2;                                                   [part 1, Cor A' + N2 Thm 2]
 (C3) |I_0| = 1, Delta d < 0, |Q_{m_0}| = 1 and (TT);                                                          [part 1, Cor A' + N2-referee Cor R]
 (C4) Delta d_m >= 0 for all m and the tuning-cone condition (TC) of P2x Thm 3.5.                              [part 1, Cor A' + P2x Thm 3.5]
Proof. By 2.3(c) the optimal data have kappa_w = max(gamma^+, gamma^-) <= 1, so rho^2 kappa_w < 1 for every rho < 1. Apply Theorem A / Corollary A'. QED.
(SUPERSEDED by part 3, Corollary D2: at (BT) points none of (S), (TT)/(BR), |Q_{m_0}| = 1, (TC) is needed; every mate is recovered.)

## 2.6 Corollary B2 (P1's example: every mate is recovered). PROVED.
Let T, f be as in P1 2.1-2.2 (any finite I containing 1). Then (f, rho g) is in cl NA((c_0,p), l_2^2) for EVERY g in C(f) and every rho < 1; i.e. f is in the
recoverable set R, and all of P1's "defect" is recovered by rebalanced engineered approximants.
*Proof.* (BT): F = {1}; Q_1 = {2}, Q_m = empty (m != 1) (P1 2.2(b)); every peak has margin mu_{k,m} >= q_0 psi(Phi_m(k)) > 0 with psi(phi) = min(1/4, 2 sqrt phi)
(P1 6.0), so there are no degenerate peaks, and for s < q_0/4: mu_{k,m} < s forces Phi_m(k) < s^2/(4 q_0^2), whence sum{Phi_m(k) : mu_{k,m} < s} <= 2 s^2/(4q_0^2) = o(s)
(Phi_m(k+1) <= Phi_m(k)/2: Phi_m(k) = 2^{-m-k} c_{l(k,m)} with c_l decreasing along k). (MS) holds. K = K' (infinite) is allowed.
Side decompositions: omega_1 = (mu/lambda_0) e_2 (mu real), all other omega_m = 0; d_1 = <D_1 w_1, D_1 omega_1>/C_1 = Phi_1(2)^2 w_1(2) mu/(lambda_0 C_1) = 0 since w_1(2) = 0; so
R_1*(omega_1 - d_1 w_1) = mu u (u = u_{2,1}), H_1(omega_1) = (Phi_1(2) mu/lambda_0)^2/C_1 = mu^2/C_1 (lambda_0 = Phi_1(2), m = 1), b = g - mu u. Side-+ admissibility:
supp(g - mu u) in {1} cup K' and g_j - mu u_j >= 0 on K' (z = 1 there; u_j > 0), i.e. g in E_u-type support and mu <= inf theta(g), theta_j := g_j/u_j. Hence
   gamma^+(g) = min_{mu <= inf theta(g)} Phi_g(mu),  gamma^-(g) = min_{mu >= sup theta(g)} Phi_g(mu),  Phi_g(mu) := q_0 h(g - mu u) + sigma_1 mu^2/C_1,
(Phi_g is a strictly convex quadratic in mu, so the minima are attained). For g in C(f), 2.3(c) gives gamma^+-(g) <= 1. The optimal data
(b+- = g - mu+- u, omega+- = (mu+-/lambda_0) e_2) are two-piece data with a single active block, Delta d = 0 (d = 0 on both sides), kappa_w <= 1. Theorem A
gives (f, rho g) in cl NA for every rho < 1. QED.
This answers the question "is every g in C(f) recovered at P1's example?": YES (PROVED). It upgrades P2A 2.4 (SKETCH, via shifts) to a proof and shows
that the shifted transport of A Thm 4.17 is not needed: the transfer-peak rebalancing (C Thm 7.4) is the exact mechanism, and the exact invariant is the
weighted coefficient minimised over side-admissible carriers mu (not the max-form kappa+- of P1 6.3).

## 2.7 Numerical confirmation (S3_work/gamma_side.py). 
Finite model of the C referee (C_work/Cref_work model.py, seed 21: n = 6, d = 3, F = {3,4,5}, one block with 5 coordinates + a non-peak transfer
coordinate, pure block certificate on k_0 = 1). gamma+- computed by a convex QP over omega in R^Q with the side constraints of 2.2:
| model | Gamma_w(certificate) | gamma^+ (QP) | referee's exact coefficient t>0 | gamma^- (QP) | referee's exact t<0 |
|---|---|---|---|---|---|
| free coordinates J = {0,1,2} | 0.29824 | 0.29824 | 0.29814 (t=1e-3) | 0.29824 | 0.29834 (t=-1e-3) |
| all off-support coordinates kinks (J empty) | 0.48511 | 0.29567 | 0.29567 (3e-4), 0.29568 (1e-4) | 0.28325 | 0.28325 (-3e-4), 0.28324 (-1e-4) |
The one-sided invariant reproduces the referee's exact one-sided coefficients to 5 digits, including the asymmetry between the two sides. (In a
finite model the upper bound needs a transfer coordinate, which the referee's model supplies; the lower bound of 2.3 holds in any finite model.)
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
# S3 part 4: generic supports (O1) — what is proved, the exact residual property, and whether it can fail

Setting of parts 1-3. "Generic support": some block has infinitely many strict non-peaks (Q_m infinite), possibly with non-peaks at a positive
proportion of fine scales; near-threshold coordinates and degenerate peaks allowed unless stated.

## 4.1 What Theorem D already gives at generic supports. PROVED.
Corollary D1 (part 3) has NO hypothesis on Q_m: if F is finite and g in C(f) carries two-piece data (finitely supported omega^+-) with Delta d_m >= 0
in all blocks and kappa_w <= 1, then g is in Ls(f) — whatever the non-peak structure of f (infinitely many strict non-peaks at all scales, near-threshold
non-peaks, degenerate peaks). The only place where the fine structure of f enters Theorem D is (SC_m) in blocks with Delta d_m < 0.
Reason: the deep coordinates scrambled by the window perturbation (size s_1) enter the proof only through
 (i) ||D_m(w'_m - w_m)||^2 = O(s_1^2 log(1/s_1)) (always; proof of D2(i), which uses only the clamp formula and Phi_m(k) <= 2^{-m-k});
 (ii) the Bregman terms Bx_m = o(s_1) (always; (E5));
 (iii) the anchor remainder sum_{A_m} lambda_k |w'_m(k) - w_m(k)| — needed only on the "wrong" side, i.e. when Delta d_m < 0.

## 4.2 The exact residual quantity and a sufficient structural condition. PROVED.
For a block m and s > 0 let
   Scr_m(s) := sum{ min(Phi_m(k), s) : k in P_m, mu_{k,m} <= s }  +  sum{ min(Phi_m(k), s) : k in Q_m, Phi_m(k) gap_m(k) <= s  or  gap_m(k) <= s }
(lambda-weighted mass, truncated at s, of near-threshold peaks and of non-peaks that a perturbation of relative size s can scramble), and say that
block m satisfies
   (MS-Q*)  liminf_{s -> 0} Scr_m(K s)/s = 0 for every K < infinity  [equivalently along one sequence s_i -> 0 for each K; it suffices: Scr_m(s) = o(s)],
and has no degenerate peaks and no non-peak with gap 0 (i.e. every k off P_m has |w_m(k)| < M_m: automatic for strict non-peaks).
Proposition 4.2. If block m has no degenerate peaks and Scr_m(K s) = o(s) along a sequence s -> 0 for every K, then (SC_m) holds along the approximants
of part 3, 3.3 (with s_1 running through that sequence). Consequently (Theorem D): if F is finite and every block with Delta d_m < 0 satisfies these
conditions, every two-piece mate with kappa_w <= 1 is in Ls(f).
*Proof.* (a) As in D2(i): Phi_k |w'(k) - w(k)| <= K_0(s_1 + t_k) (clamp formula, uniform Lipschitz bound; t_k := ||u_{k,m} 1_{(N'',inf)}||_1) and <= 2 Phi_k,
so ||D(w'-w)||^2 = O(s_1^2 log(1/s_1)) + (tail).
(b) |C' - C| <= K_g s_1 (no hypothesis): with Delta := D(w' - w), |<Dw, Delta>| <= sum_k Phi_k |w(k)| Phi_k |w'(k) - w(k)| <= sum_k Phi_k K_0 (s_1 + t_k) = O(s_1),
and | ||Dw'|| - ||Dw|| - <Dw,Delta>/C | <= ||Delta||^2/C (expand ||Dw + Delta||; C' -> C > 0), so |C' - C| = O(s_1) + O(||Delta||^2) = O(s_1); |M' - M| = |C' - C|.
(c) A peak with mu_k > K_1(s_1 + t_k) stays a same-sign peak of w' (threshold perturbation O(s_1 + t_k)). A strict non-peak with Phi_k gap_k > K_1(s_1 + t_k) and
gap_k > K_1 s_1 satisfies |w'(k) - w(k)| <= K_0(s_1 + t_k)/Phi_k <= gap_k/4 (K_1 >= 4K_0) and |gamma| + |M' - M| <= 2K_g s_1 <= gap_k/4 (K_1 >= 8K_g), so it remains a
non-peak and |2w'(k) - w(k)| <= |w(k)| + 2|w'(k) - w(k)| <= M - gap_k/2 <= M' - |gamma|. Hence A_m is contained in {k in P: mu_k <= K_1(s_1 + t_k)} union
{k in Q: Phi_k gap_k <= K_1(s_1 + t_k) or gap_k <= K_1 s_1}.
(d) On A_m: Phi_k^2 + lambda_k(|w'(k) - w(k)| + gamma_+) <= m(3 min(Phi_k, K_0(s_1 + t_k)) + 2 Phi_k K_g s_1) (Phi_k <= 1). Summing over A_m: the part with t_k <= s_1 is
<= 3mK' Scr_m(2K_1 s_1) + 2 m K_g s_1 sum_{A_m} Phi_k, and sum_{A_m} Phi_k -> 0 (A_m shrinks to the empty set coordinatewise; dominated convergence), so this is o(s_1)
under the hypothesis; the part with t_k > s_1 tends to 0 as N'' -> infinity for fixed s_1 (dominated convergence: every peak has mu_k > 0, every non-peak gap_k > 0, and
t_k -> 0 for each k) and is made <= s_1^2 by choosing N'' after s_1. With (a), (SC_m) holds. QED.

## 4.3 Quantitative recovery without (SC). PROVED.
Without any condition on the Delta d < 0 blocks, the proof of Theorem D gives: (f, rho g) is in cl NA whenever
   rho^2 kappa_w + 8 rho sum_{m : Delta d_m < 0} |Delta d_m| K_m^scr < 1,    K_m^scr := limsup along the construction of (anchor and remainder costs)/s_1,
since the genuine first-order cost on the wrong side is <= |tau| rho |Delta d_m| (E_y + 2||R*Z_A||_1) <= |tau| rho |Delta d_m| K_m^scr s_1 (1 + o(1)) <= rho |Delta d_m| K_m^scr tau^2 (|tau| >= s_1).
K_m^scr <= C_abs m (limsup Scr_m(K s_1)/s_1) is finite when non-peak gaps are bounded below off a finite set (Scr_m(s) <= sum_{Phi <= s/g_0} Phi + ... = O(s)).
So the non-recovered part of a Delta d < 0 two-piece mate is confined to rho close to 1: "ρ-defect" only, never a first-order obstruction.

## 4.4 Can (MS-Q*) / (SC) fail for an admissible T? SKETCH (yes for (MS-Q*); whether recovery fails is OPEN).
Construction (adaptation of P1 2.1, which allows any finite or "density-zero" set of prescribed vectors; and of N2 3.8 for Delta d < 0): fix the first row's
contact vector zhat as in P1 2.2, and in block 1 prescribe u_{2k,1} in zhat-perp cap S_{q*} for all k >= k_0 (a sequence dense in zhat-perp cap S_{q*}), with the odd
indices (and all other blocks) carrying the dense targets of P1 2.1 (so the tail of every block is still dense in S_{q*}, (T-d)); injectivity and Ran T cap c_00 = {0}
via signature tails h_l as in P1 2.1. Then every (2k,1), k >= k_0, is a strict non-peak of f with w_1(2k) = 0 and gap M_1, and
   Scr_1(s) >= sum{Phi_1(2k) : Phi_1(2k) <= s} ~ s/3:   (MS-Q*) FAILS at every scale.
Along the approximants of 3.3, u_{2k,1}(xhat') = s_1 <U*u_{2k,1}, h_N> + o(s_1) with h_N := (e' - e)/s_1 + o(1) fixed by the window masses; since the u_{2k,1}
are dense in zhat-perp cap S, a positive proportion of the deep (2k,1) with Phi_1(2k) << s_1 become peaks of w'_1 (new peaks, |w' - w| = M'), so the anchor remainder
is >= c s_1: (SC_1) FAILS for these approximants. Combined with a Delta d < 0 exact resonance in block 1 (N2 3.8 design; compatible, since the resonance vector is a
single prescribed u_{2,1}), Theorem D does not apply for rho close to 1.
OPEN: whether other approximants pin the deep non-peaks. A sufficient "compensation property" (HEURISTIC): masses at far free coordinates (z'_j := sign of the
mass, j -> infinity; no cost for the two-piece pieces since beta^sigma vanishes on J) that cancel P_perp U*(window masses) up to relative error eta, with total l_1 mass -> 0,
would reduce the scrambling to eta s_1 and give (SC) with an eta-dependent constant, hence recovery (by 4.3 with eta -> 0). This is a property of U and of the
far free coordinates, NOT of T; it needs, roughly, that the tail spans of {P_perp U*e_j* : j in J, j > N_1} approximate the (N-dependent) perturbation direction with
coefficients o(1/s_1) — not proved.

## 4.5 Deep coefficients c_k ~ sqrt(Phi_k) (C_notes 9.2 borderline). PROVED (max-form) / SKETCH (weighted form).
C_notes 9.2 states that sum c_k^2/Phi_k = infinity with |c_k| ~ sqrt(Phi_k) is "not covered by any known recovery technique". This is superseded by A Cor 6.10(a)
(Theorem W with O(sigma) box tails, via the Averaging Theorem 6.8; refereed): for g = b + sum_m R_m*(omega_m - d_m w_m) with b supported in F and
omega_m(k) = c_k/(m Phi_m(k)), gaps bounded below on supp omega_m, the box tail is T_m(sigma) = sum{|c_k| : |c_k| > gap_k Phi_k/(2 sigma)} <= sum{|c_k| : Phi_k <~ sigma^2/g_0^2} = O(sigma)
when |c_k| <= K sqrt(Phi_k) (geometric Phi), so g is in cl Cert(f) provided g is in C(f) and max(h(b), H_m(omega_m)) <= 1 (note ||D omega||^2 = sum c_k^2/m^2 < infinity).
Upgrade to Gamma_w <= 1 (SKETCH): run the averaging with rebalanced certificates; Lemma 1.1 of part 1 applies at f uniformly in the truncation level provided the
cut-off gamma of the transfer vectors is chosen with |tau omega(k)| <= gap_k/2 on L cap supp omega (then lowering coordinates of supp omega in L does not change signs),
which holds for the truncated certificates c_t of A Cor 6.10(a) (box condition). Not written in full.
Mixed case (deep weighted part + switching part, i.e. two-piece data whose COMMON part omega^0 is infinitely supported with O(sigma) tails and whose switching
part omega_Delta is finite): Theorem D at f' plus averaging over scales at f' (P2A Lemma 1.5) is the natural route; the obstruction is that the window
perturbation scrambles the deep part of omega^0 below scale s_1 at f', so the target must drop it (cost sum_{Phi_k <~ s_1}|c_k| ~ sqrt(s_1)) and this must be
paid by the slack at the scale where the truncated certificate's radius ends (~ sqrt(Phi_cut)) — the same borderline as in C 9.2, now at f'. OPEN (SKETCH of the
difficulty only).

## 4.6 Answer to O1 (summary).
 * Generic supports are NOT an obstruction for two-piece mates with Delta d_m >= 0 (PROVED, D1), nor for Delta d_m < 0 when the carrier blocks satisfy
   (MS-Q*) along some sequence of scales (PROVED, 4.2), nor for rho below an explicit threshold in general (PROVED, 4.3).
 * The precise quantitative property needed for Delta d < 0: o(s)-smallness of the lambda-mass (truncated at s) of coordinates scrambled by a perturbation of
   relative size s — (MS) for peaks and (MS-Q*) for non-peaks — along SOME sequence of scales. It is a property of f and T; it CAN fail for admissible T (4.4, SKETCH),
   and then the simplified approximants do not recover Delta d < 0 two-piece mates for rho near 1. Whether some engineering always works is OPEN; a sufficient
   T-independent route is the compensation property of 4.4 (HEURISTIC).
 * The deep-coefficient borderline of C 9.2 is covered by A Cor 6.10(a) for certificate-type mates (PROVED); for mixed switching + deep mates it is OPEN.
 * Beyond two-piece data: at generic supports (Q infinite) Theorem B's lower bound is not available (the block expansion is multiscale: coordinates with
   Phi_k <~ |t| contribute linearly, total O(t^2) "persistent curvature"); whether every mate at such f is a limit of two-piece data is OPEN (this is O3).
# S3 part 5: O4 summary, infinite block sets, robustness notes, open problems

## 5.1 O4. PROVED.
"Several active blocks without (S)/(TC)": Theorem D (3.4) needs neither. The reason: P2A needed v_m(xhat') = 0 in EVERY block because a d'-mismatch
Delta d'_m R_m* w'_m between the two sides must otherwise be paid at first order; first-order rebalancing (3.1 + Lemma 1.1) moves it between the base and block m at
cost |tau| x O(s_1) x eps_1 (eps_1 the transfer inefficiency, fixed before s_1). Every block's mismatch is O(s_1) automatically because the only perturbation
of the normer is the window-mass perturbation of e' (size O(s_1)) and the far truncation (made o(s_1)).
"Infinite block sets": not treated directly; Remark martin-tail (Preprint B) reduces density for p to density for every p_N, and all results here are uniform in
nothing that depends on |I| except the number of transfer peaks (one pair per block), which is finite for p_N.

## 5.2 Where the results could be fragile (self-review).
 * Theorem B uses C Prop 8.1 (ii) (block expansion with overshoot) for test directions nu = U k + nu_c with k arbitrary in e-perp (C used k in E_F). (ii) is stated and
   re-derived for arbitrary delta_1, delta_2 in l_1 (C referee 1.20), so this is legitimate; the base estimate with general k is re-proved in 2.3 Step 1.
 * Theorem D Step 6 treats the first-order linear terms by transfer peaks whose radius condition (Lemma 1.1(i)/(ii): eps(2 + Lambda) <= gamma - eta) holds because
   |eps^{(1)}| <= T_0 K_l s_1 -> 0 along the construction while the transfer data are fixed — the order of choices (transfer data and T_0 first, then N, s_1, N'')
   is essential and is respected.
 * In Theorem D the theta-piece is used for ALL |tau| <= s_1; it has no linear terms and no genuine first-order costs (balanced at f', window masses cover
   |tau| <= s_1, base supported in supp a'), so no first-order bound is needed at scales below s_1 — this is what makes o(s_1)|tau| costs on the side pieces
   acceptable (they are only used for |tau| > s_1).
 * Consistency with P1-referee R3 (canonical truncations do not recover switching mates): the approximants of 3.3 carry window masses (they are not canonical
   truncations); g' is a finite certificate at f' whose base part lives on supp a' (which contains the window contacts), so g' is in S(f'), as R1-R3 require.
 * Numerics: Theorem B's invariant matches the C referee's independent exact coefficients (5 digits, both sides); Lemma R+ checked on 400 random blocks
   (231 with C' > C; max violation 2.2e-16). Theorem D itself was not simulated (infinite-dimensional construction); its ingredients are elementary estimates.

## 5.3 Open problems after S3 (precise).
 (P1) Delta d < 0 switching mates at blocks violating (MS-Q*) at all scales (positive lambda-density of non-peaks at fine scales): either engineer approximants that
      pin the deep non-peaks to precision ~ Phi_k gap_k (compensation of the window perturbation of e', 4.4), or prove a lower bound for dist(rho g, C(f')) over
      all NA f' near f (a counterexample route; nothing suggests it).
 (P2) Generic supports (Q infinite): exact one-sided invariant. Theorem B's proof breaks because the block expansion is multiscale (coordinates with Phi_k <~ |t|
      contribute linearly, total O(t^2)); the natural conjecture is lim 2(p*(f+tg)-1)/t^2 = inf over side-admissible WEIGHTED decompositions of Gamma_w, which would
      need infinite-dimensional duality with the Huber-type block excess (C Lemma 5.3). Then recovery would need Theorem D with infinitely supported omega
      (averaging over scales at f', P2A Lemma 1.5), facing the same scrambling issue as (P1) for the deep part.
 (P3) Mixed deep + switching mates (4.5).
 (P4) Approximate resonances / scale-dependent switching (O3): untouched here, but note that first-order rebalancing makes linear O(s_1)-mismatches harmless,
      which removes one of the obstacles listed in P2A 4.4 (the consistency identity 3.2 of P2A required exact replication of relative block positions only
      because mismatches were not rebalanceable). Worth re-examining with Theorem D's mechanism.
