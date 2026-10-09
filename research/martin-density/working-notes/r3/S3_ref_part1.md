# S3 referee, part 1: Lemma 1.1 (rebalancing add-on), Lemma 3.2 (R+), first pass on Theorem B and Theorem D

Setting checked: finite block set I (p_N), canonical base, admissible T (Lemma B conclusion only). Notation of S3_notes.

## 1.1 Lemma 1.1 (rebalancing add-on). Verdict: CORRECT (line-by-line re-derivation).
(i) lowering, y = s'1_{L'} + Lambda e_{k*}, eps >= 0.
 - k in L' \ {k*}: |w'(k)| >= gamma, |V(k) - w'(k)| <= eta < gamma (eps(2+Lambda) <= gamma - eta forces gamma > eta when eps > 0),
   so sign V(k) = s'(k) and |V(k)| >= gamma - eta >= eps; hence |V(k) - eps s'(k)| = |V(k)| - eps <= ||V|| - eps.
 - k*: upper bound trivial (Lambda >= 0); lower bound V(k*) + ||V|| >= 2(gamma - eta) >= eps(2 + Lambda). OK.
 - k notin L': |V(k)| < gamma + eta, and ||V|| >= V(k*) >= M' - eta, so need gamma + 2eta + eps <= M': true from
   eta, eps <= (M' - gamma)/4. OK.
(ii) raising: same, with V(k*) + ||V|| + e(2 - Lambda) >= 2(gamma - eta) - e(Lambda + 1) >= 0. OK.
(iii) elementary (sqrt(A^2 + x) <= A + x/(2A); the 4|a-b||y|/|b| bound uses |a| >= |b|/2). OK.
(iv) bookkeeping. Needs ||alpha'||_1 = 1 exactly: true (if R x'/sigma' = x_0 + D b with ||x_0||_1, ||b|| <= 1, then
   1 = w'(x_0) + <Dw', b> <= M' ||x_0||_1 + C' ||b|| <= 1 forces ||x_0||_1 = 1 when M' > 0, b = Dw'/C'). Then
   y(R x') = sigma'(1 +- Lambda |alpha'_{k*}|) + sigma'<Dw', Dy>/C' and sigma'|alpha'_{k*}| = m Phi_*(u_*(x') - theta' Phi_*). OK.
(v) algebra: R_m* y = (Y'/c') a' + e' with e'(x') = 0; q*(lambda_A a' + tau B + sum eps e') <= lambda_A q*(a' + (tau/lambda_A)B) + sum|eps| q*(e'). OK.
Remark: the inefficiency is always a COST in both directions (lowering: +eps Lambda m Phi mu'/c' added to the base; raising:
eps < 0 and Y' = sigma' e'_y - Lambda m Phi mu', so the base again gets +|eps| Lambda m Phi mu'/c'). Checked.
Valid at a non-NA f with xi in place of x' (A Fact C at the normer is all that is used). OK.

## 1.2 Lemma 1.2 / 1.3 (transfer data, persistence). Verdict: CORRECT.
Key points checked: tau_* := -(R*(s 1_L) - (R*(s 1_L)(xi)/q_0) a) has tau_*(xi) = 0, so the target T = tau_* + delta_0 q*(tau_*) a has
T(xi) = delta_0 q_0 q*(tau_*) > 0 and a deep u_{k*} ~ T/q*(T) is a positive peak with margin ~ delta_0 q_0 (density of every tail);
Lambda m Phi_* = q*(T) is BOUNDED independently of the inefficiency target (q*(tau_*) <= 2 sum_k m Phi_m(k) q*(u_k)), so the
"exchange-rate" terms Y'/c' are bounded independently of eta_1 — this matters for Theorem D (K_l, K_tr independent of eta_1).
Lambda Phi_*^2 = q*(T) Phi_*/m -> 0, so e_y -> e^0_y. Persistence: coordinatewise convergence of w' plus |w(k)| != gamma for all k
and dominated convergence (majorant m Phi_m(k) q*(u_{k,m})). OK.

## 1.3 Lemma 3.2 (R+). Verdict: CORRECT (constant in the displayed intermediate bound is loose but the final bound holds).
Re-derived: ||y||_inf <= M' - gamma (S_1: |y| = 2M' - M = M' - gamma; S_2: <= M' - |gamma|; A: <= M' - gamma_+).
||Dy||^2 = 2C'^2 - C^2 + ||D(w'-w)||^2 + ||DY||^2 - 2R_A and 2(C+gamma)^2 - C^2 = (C+2gamma)^2 - 2gamma^2. OK.
X-bound: the note writes ||DY||^2 <= 2||D(w'-w)||^2 + 2(...)||Dw'1_A||^2, which with the stated |R_A| bound gives only
X <= 4||D(w'-w)||^2 + 5||Dw' 1_A||^2 (M' close to 1 in Martin's blocks, so 5M'^2 > 4). But Y has DISJOINT pieces on S and A, so
||DY||^2 = ||D(w'-w)1_S||^2 + (gamma_+/M')^2 ||Dw'1_A||^2 and then X <= 3||D(w'-w)||^2 + 4||Dw'1_A||^2 <= 4||D(w'-w)||^2 + 4 sum_A Phi^2.
So the stated final bound is TRUE (cosmetic fix: use disjointness). gamma_+/M' <= 1 needs C <= 2/3: fine (C_m <= 2^{-m}).
Consequence (E_y bound): <y - w', R x'> >= -sum_A |Rx'(k)|(|w'-w| + gamma_+) uses Bx = <w'-w, Rx'> >= 0 (w' norms Rx'). OK.
Numerical re-check: see part 2 (independent script).

## 1.4 First pass on Theorem B upper bound. Verdict: CORRECT.
Base: ||a + tb||_1 = ||a||_1 + t b(z) for 0 < t < min_F|a_j|/||b||_inf uses b vanishing off F cup K and z_j b_j = |b_j| on K. OK.
b(zhat) = 0 uses A Lemma 4.2 (<omega - d w, zeta_m> = 0 for omega supported off peaks). Re-derived: zeta_m = sigma_m(alpha + D^2 w/C),
<omega, zeta> = sigma d, <w, zeta> = sigma (M + C) = sigma. OK.
Block: N(w + t(omega - d w)) first-order term -dM + (d - dC) = d(1 - M - C) = 0. OK.
Rebalancing at f (no engineering): all blocks, including omega_m = 0 blocks (which ABSORB level via raising), equalised at
Lev = Gamma_w/2. Elimination verified: q_0 h/2 + sum sigma_m H_m/2 = Lev (q_0 + sum sigma_m) = Lev.
