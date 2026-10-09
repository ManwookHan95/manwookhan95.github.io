# Z1 referee, part 1: Z1 sections 1.1-1.5 (approximants in R_0, exposed face, local reduction, Theorem B*)

Setting as in Z1: canonical base q, finite block set I_N (p := p_N), the SLD operator T of G3 1.2. Notation of G3/Z1.
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN. Scripts: r4/Z1ref_work/.

## 1.1 R_0-approximants and the "lsc reformulation" (Z1 1.1). Verdict: correct, with one overstatement.
(a) Re-derived (G3_ref 3.3). Given q*(a') = 1, z' in B_{l_inf}, z' = sign a' on supp a': zhat' := z' + U e' (e' = U*a'/||U*a'||) satisfies
    a'(zhat') = ||a'||_1 + ||U*a'|| = 1 and q**(zhat') <= 1, so q**(zhat') = 1; with q_0' := 1/(1 + sum_m |R_m** zhat'|_m), xi' := q_0' zhat',
    w'_m := J_m(R_m** xi') one gets f'(xi') = q_0' + sum_m |R_m** xi'|_m = 1 = p**(xi') and p*(f') <= max(q*(a'), max_m N_m(w'_m)) = 1.
    Continuity: if a' -> a in l_1 and z' -> z coordinatewise and boundedly, then ||R_m**(zhat' - zhat)||_1 <= sum_k lambda_k |u_k(zhat' - zhat)| -> 0
    by dominated convergence (sum_k lambda_k < infinity, |u_k(zhat' - zhat)| <= 2(1 + ||U||)), so the normalisations converge, J_m is norm-to-weak*
    continuous (V_m smooth, Smulian), and L* is weak*-to-norm continuous on bounded sets (L compact). Hence f' -> f in norm. CORRECT.
(b) Canonical truncations are NA (zhat'_n in c_0), hence in R_0 (G3 1.4(a)). Far lowerings: (SR) holds because the S_l are pairwise disjoint, so
    only finitely many S_l meet [1,n] and each keeps the positive mass of S_l cap (n, inf). CORRECT, with one omission: when F is infinite,
    a must also be truncated (otherwise F' = F is infinite and f' is not in R_0); Z1 specifies only z'_n.
(c) OVERSTATEMENT. Z1 writes "Lemma Z is purely the statement rho C(f) subset Li C(f'_n) along SOME sequence in R_0 (equivalently, liminf
    r~_{f'_n}(x) >= rho r~_f(x) on a countable dense set, along one sequence)". That is the UNIFORM statement (one sequence for all mates). Lemma Z
    (G3 1.1) is a PER-MATE statement: for each (f, g, rho) there is an R_0-sequence f'_n -> f, which may depend on g, with dist(rho g, C(f'_n)) -> 0.
    The uniform statement implies Lemma Z. The converse is not shown: going from separate sequences to one common sequence is exactly the
    "common first row for finitely many mates" condition of the BRIEFING's (R3) reduction, which does not follow from ell_2^2-density.
    Fix: state the reformulation per mate. Nothing else in Z1 depends on the uniform version.

## 1.2 Exposed face (Z1 1.2). Verdict: the lemma is CORRECT (PROVED).
Re-derived: phi = a' + L*w' (A Fact A, infimum attained); phi(xi) = 1 forces a'(xi) = q**(xi) and <w'_m, zeta_m> = |zeta_m|_m for each m.
Two points that Z1 asserts or leaves implicit, both true:
 * zeta_m = R_m** xi != 0 for every m, because R_m** is injective on l_inf: if u_{k,m}(xi) = 0 for all k, then xi vanishes on a norm-dense subset
   of S_{q*} (Lemma B), so xi = 0. This is needed to invoke smoothness of |.|_m at zeta_m.
 * Uniqueness of the maximiser of a'' -> a''(xi) on B_{q*} follows from strict convexity of q* (Hilbert norm strictly convex, U* injective):
   if q*(x) = q*(y) = q*((x+y)/2) = 1, then U*x = lambda U*y with lambda >= 0, so x = lambda y and lambda = 1.

## 1.3 The "consequence" (Z1 1.3). Verdict: WRONG as stated (non sequitur; not load-bearing).
Z1 table #2 says: "hence rho C(f) subset C(f') with f' in S_{p*} forces f' = f | PROVED", and 1.3 draws the "moral" that every approximant f' != f
must lose part of rho C(f). The proof only shows that the SUFFICIENT condition (*) f'^2 <= rho^2 f^2 + (1 - rho^2) p^2 fails for f' != f.
 * Exact criterion (PROVED). Put r~_f(x) := max_{g in C(f)} g(x) (support function; C(f) is weak*-compact). Then
     rho C(f) subset C(f')  <=>  f'(x)^2 + rho^2 r~_f(x)^2 <= p(x)^2 for all x in c_0.
   Since r~_f <= r_f = sqrt(p^2 - f^2), the right side p^2 - rho^2 r~_f^2 is >= rho^2 f^2 + (1 - rho^2) p^2, with strict inequality wherever
   r~_f < r_f. So (*) is sufficient but in general far from necessary.
 * What the exact criterion forces (PROVED). For eta in X**, Goldstine gives a net x_i -> eta weak* with p(x_i) <= p**(eta); passing to the limit,
   f'(eta)^2 + rho^2 g(eta)^2 <= p**(eta)^2 for every g in C(f). At eta = xi' (normer of f') this gives g(xi') = 0 for all g in C(f), i.e.
   C(f) subset ker xi'. That is the only first-order consequence. It forces f' = f exactly when C(f)^perp = R xi in X** (then xi' = +-xi, and
   1.2 applies), e.g. when span C(f) is dense in ker xi. Nothing in Z1 shows this for general f.
 * The inference pattern "exposed faces are points => rho C(f) subset C(f') forces f' = f" is FALSE in general. In X = ell_4^3 (smooth,
   strictly convex, every exposed face of the dual ball a point), f = e_1* has C(f) = {0}: g in C(f) needs g(e_1) = 0 and
   g(s v)^2 <= ||e_1 + s v||_4^2 - 1 = O(s^4) for v in e_1-perp, so g = 0. Then rho C(f) = {0} is contained in every C(f').
 * A positive fact in the opposite direction (PROVED, new). Let C_base(a) := {b in l_1 : q*(a + s b) <= s(s) for all real s}. Then
   C_base(a) subset C(f') for EVERY f' in S_{p*} whose forced base part is a. Proof: f' + s b = (a + s b) + L*w', so by A Fact A
   p*(f' + s b) <= max(q*(a + s b), ||w'||_{V*}) = max(q*(a + s b), 1) <= s(s). So along approximants that keep a (far lowerings and the f^L of
   Z1 3.2 keep a; canonical truncations do not), the pure-base part of the fibre is never lost. This contradicts nothing in Z1 except the moral.
Impact: 1.3 is used only as motivation (0. Answer, 3.1(d) "moral"). No proof depends on it. Fix: replace "forces f' = f" by "the primal
sufficient condition (*) fails for f' != f; the exact condition only forces C(f) subset ker xi'".

## 1.4 Local reduction (Z1 1.4 = P2A Lemma 1.4 for non-NA f'). Verdict: CORRECT (PROVED).
Re-derived. For |tau| <= T_0: 1 + (tau^2/2)(1 - delta) <= s(tau) because s(tau) >= 1 + tau^2/2 - tau^4/8 and tau^2 <= T_0^2 <= 3 delta < 4 delta.
For |tau| >= T_0: p*(f' + tau g') <= s(rho tau) + eps + |tau| eta', and s(tau) - s(rho tau) = (1 - rho^2) tau^2/(s(tau) + s(rho tau)) is
>= (1 - rho^2) tau^2/(2 sqrt 2) for |tau| <= 1 and >= (1 - rho^2)|tau|/(2 sqrt 2) for |tau| >= 1, while eps + |tau| eta' <= (1 - rho^2)tau^2/3
resp. (1 - rho^2)|tau|/3, and 1/3 < 1/(2 sqrt 2). Norm attainment of f' is never used. Numerical check (scalar_checks.py): max violation 0.
The stated equivalence "Lemma Z <=> local mates" is also correct (for "=>" use rho' g'' with g'' in C(f'), rho' < 1, delta = 1 - rho'^2).

## 1.5 Theorem B* (window-pinned mates). Verdict: CORRECT (PROVED by inspection).
I traced every use of (SR) and of gamma in G3 parts 2-5 (with the G3_ref fix of 5.3):
 * gamma enters only in 2.3(b)'s consequence sum_{J_gamma} |B| <= t/(2 gamma q_0) and through it in 3.4 (K_1 = 1/(gamma q_0) + 14); (SR) enters
   only through delta'_l > 0 in 3.2-3.3. Both are consumed by 3.4, whose conclusion sum_l |Delta c_l| <= K t is all that 3.5, 4.1-4.2 and 5.3 use.
 * 3.5(a)-(c), 4.2(a)-(d): valid for any admissible T and any f with F finite, given that conclusion, K t <= 1, t <= t_*, t in W(l_*):
   the fine-carrier estimate in 4.2(c) uses only the box bound 3.1 and (P2), t >= T_lo(l_*); K_b uses 2.5 (F finite).
 * 5.1, 5.2 are for any f with F finite. 5.3 needs only: t^(j) = T_hi(l_j), n_j = n^w_{l_j}, K'_j = (1 + ||U||) K_2-type constant times K_j,
   n_j >= 24 rho^2 K'_j/(c_1(1 - rho^2)) (from n^w/K_j -> infinity), K'_j t^(j)/n_j -> 0 and K_4 K_j t <= kappa_0 (from K_j T_hi(l_j) -> 0).
Remarks. (i) The hypothesis is needed only on the n_j dyadic scales T_hi(l_j) 2^{1-i}, not on all of W(l_j), and only for coarse l <= l_j (the
fine part is <= 6 t^2 at every f, by 3.1 and (P2)). (ii) Remark (ii) of Z1 1.5 ("persistent switching through unpinned carriers") is a
paraphrase of the negation of window-pinning; correct as a description, HEURISTIC as to its consequences. (iii) Bounded free switching (Z1 4.3)
is far from window-pinning: pinning needs switching <= K_j T_lo(l_j) at the bottom of the window, i.e. super-exponentially small.
