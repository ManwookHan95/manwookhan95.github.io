# Z1 part 1: setting, what Lemma Z really asks, two exact facts

Setting: canonical base q, finite block set I_N (p := p_N, every N; Remark martin-tail, G3_referee sec. 4, reduces the question
for Martin's p to all p_N). T = the SLD operator of G3 1.2. Notation of G3 (f = a + L*w, xi = q_0 zhat, zhat = z + Ue, F = supp a,
zeta_m, sigma_m, M_m, C_m, P_m, alpha_m, J_gamma, K = contacts, s(t) = sqrt(1+t^2), C(f), Ls(f), R, R_0).
Labels PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 1.1 Membership in R_0 is never the issue. PROVED.
(a) (G3_ref 3.3) Any (a', z') with q*(a') = 1, z' in B_{l_inf}, z' = sign a' on supp a' defines f' = a' + L*w' in S_{p*}
    (zhat' = z' + Ue', q_0' = 1/(1 + sum_m |R_m** zhat'|_m), xi' = q_0' zhat', w'_m = J_m(R_m** xi')); f' -> f in norm when a' -> a in l_1
    and z' -> z coordinatewise (boundedly).
(b) For every f there are f'_n in R_0 with f'_n -> f: e.g. canonical truncations a'_n = a 1_{[1,n]}/q*(..), z'_n = z 1_{[1,n]} (NA, hence in
    R_0 by G3 1.4(a)); or "far lowerings" z'_n = z on [1,n], z'_n = (1 - gamma) z beyond n (not NA): then N \ J'_gamma is contained in
    F' cup [1,n], every S_l with min S_l > n is entirely roomy, and the finitely many S_l meeting [1,n] keep the positive mass
    ||h_l 1_{S_l cap (n,inf)}||, so (SR) holds with this gamma and a small vartheta.
So Lemma Z is purely a LOWER SEMICONTINUITY statement: rho C(f) subset Li C(f'_n) along SOME sequence in R_0 (equivalently, by the
R3 reduction of BRIEFING, liminf r~_{f'_n}(x) >= rho r~_f(x) for x in a countable dense set, along one sequence).

## 1.2 Lemma (the exposed face of B_{p*} at a normer is a point). PROVED.
For f in S_{p*} with normer xi in S_{p**}: {phi in B_{p*} : phi(xi) = 1} = {f}.
*Proof.* Let phi in B_{p*}, phi(xi) = 1. By A Fact A, phi = a' + L*w' with q*(a') <= 1, ||w'||_{V*} <= 1 (the infimum defining p* is
attained by weak* compactness). Then 1 = phi(xi) = a'(xi) + <w', L**xi> <= q**(xi) + ||L**xi||_V = p**(xi) = 1, so a'(xi) = q**(xi) = q_0 > 0 and
<w'_m, zeta_m> = |zeta_m|_m for every m (the V-norm is the l_1-sum and ||w'||_{V*} = max_m N_m(w'_m) <= 1). q* = ||.||_1 + ||U*.|| is strictly convex
(||U*(x+y)|| = ||U*x|| + ||U*y|| forces U*x, U*y parallel, hence x, y parallel as U* is injective), so the maximiser of a'' -> a''(xi) on B_{q*}
is unique: a' = a. |.|_m is smooth at zeta_m != 0 (T3), so w'_m = J_m(zeta_m) = w_m. Hence phi = f. QED.

## 1.3 Consequence: no "free" approximants. PROVED.
Primal form of the fibre (R2): g in C(f) iff g(x)^2 <= p(x)^2 - f(x)^2 for all x. Hence for f' in S_{p*}:
  rho C(f) subset C(f')  <=  f'(x)^2 <= rho^2 f(x)^2 + (1 - rho^2) p(x)^2 for all x  (*)
(if (*) holds and g in C(f): rho^2 g^2 <= rho^2(p^2 - f^2) <= p^2 - f'^2). The right side of (*) is the square of a norm whose dual ball contains
rho^2 f + (1 - rho^2) B_{p*} (Cauchy-Schwarz). But (*) with f' in S_{p*} forces f' = f: evaluating (*) along a net x_i -> xi' (normer of f',
weak*, with the bidual extension) gives 1 <= rho^2 f(xi')^2 + 1 - rho^2, so f(xi') = 1, xi' = xi (unique normer of f, p** strictly convex),
and f' = f by 1.2. Equivalently p*(rho^2 f + (1-rho^2) phi) < 1 for every phi in B_{p*} \ {f}.
Moral: every approximant f' != f must LOSE part of rho C(f) near its own normer; recovery is a genuinely local (small-scale) statement
at f', the slack of rho < 1 helps only at scales >~ sqrt(p*(f' - f)/(1 - rho^2)).

## 1.4 Lemma (local reduction). PROVED. (P2A Lemma 1.4, valid for f' not NA.)
Let f, f' in S_{p*}, g in C(f), rho < 1, 0 < T_0 <= 1, 0 < delta <= 1 with T_0^2 <= 3 delta. If p*(f' - f) <= (1-rho^2)T_0^2/6,
p*(g' - rho g) <= (1-rho^2) T_0/6 and p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for |tau| <= T_0, then g' in C(f').
(The proof of P2A 1.4 never uses that f' attains its norm.) So Lemma Z <=> for every (f, g, rho) and small T_0 there are f' in R_0 within
c T_0^2 of f and g' within c T_0 of rho g which are "local mates" (second-order bound with deficit delta) for |tau| <= T_0.

## 1.5 Window-pinned mates (Theorem B*). PROVED (by inspection of G3 parts 2-5 + G3_ref fix of 5.3).
Definition. Let f in S_{p*} with F finite and g in C(f). g is WINDOW-PINNED if there are window indices l_1 < l_2 < ... and constants K_j >= 1
with K_j T_hi(l_j) -> 0 and n^w_{l_j}/K_j -> infinity, such that for every j and every scale t in W(l_j) SOME two-sided decomposition
(B_+-, Omega_+-) of g at scale t (G3 2.1) has  sum_l |Delta c_l| <= K_j t.
Theorem B*. For the SLD T, every N, f in S_{p_N*} with F finite: every window-pinned g in C(f) lies in Ls(f).
*Proof.* G3 uses the signature room (SR) ONLY to derive the conclusion of G3 Lemma 3.4 (with K = K_1 Lambda_f(l_*)) on the windows; parts 2, 4
and 5 use only that conclusion (3.5(a)-(c) are consequences of it and of 2.3, 2.4, valid for any admissible T and any f), applied to one
decomposition per scale. Replace K_1 Lambda_f(l) by K_j throughout part 4 (the constants K_b, K_2, K_4 depend only on f, gamma, N; here
gamma enters only through K_1, which is no longer used) and in 5.3 take t^(j) = T_hi(l_j), n_j = n^w_{l_j}, K_j' := (1 + ||U||) K_2 K_j: the
hypotheses of G3 5.2 hold for large j because K_j T_hi(l_j) -> 0 (giving t <= t_*, K t <= 1, K_4 K_j t <= kappa_0, G3_ref fix) and
n^w_{l_j}/K_j -> infinity. QED.
Remarks. (i) At f in R_0 every mate is window-pinned (G3 3.4, 5.3). (ii) So Lemma Z (and density) needs to be shown only for mates that
are NOT window-pinned at f: on every late window some swallowed carrier switches by >> K t, i.e. "persistent switching through
unpinned carriers". Every such mate lives at a signature-resonant f (outside R_0) or has F infinite.
