# N2 referee, part 2: Corollary 2.5, Remark 2.6, Section 3 (Delta d != 0)

## Corollary 2.5 (P1 example) -- re-derived
R_1*(e_2/lambda_0) = u (lambda_{2,1} = Phi_1(2), m = 1), d_1(e_2) = Phi_1(2)^2 w_1(2)/C_1 = 0, z = 1 on K', u > 0 on K'
=> (E1)-(E3) for b+- = g - mu+- u, omega+- = (mu+-/lambda_0) e_2. H_1 = mu^2/C_1 (D_1 e_2 orthogonal to D_1 w_1).
g_{K1}: mu+ = 0, mu- = c; h(g) <= c^2||U||^2/nu <= 9/32, h(g - c u) = ||P_perp U*(v 1_{K2})||^2/nu <= c^2||U||^2/nu
(P_perp kills U*e_1* = nu_1 e), c^2/C_1 <= 3/4: kappa <= 1 for c <= c_* of P1 2.3. Slab: coefficients <= 4 theta_*^2||U||^2/nu
and theta_*^2/C_1, so "the whole slab" holds after possibly shrinking theta_* (wording). VERDICT: PROVED (given Thm 1, P1 2.1-2.3, 6.1-6.2).

## Remark 2.6 (several active blocks, all Delta d_m = 0) -- check
Conditions: ell_m(x') = 0 for m in I_act. sum_m ell_m = v. v(x') tuned by masses (Thm 1). Moving finitely many fixed near free
coordinates j_1..j_r (r = |I_act|-1) changes ell_m(x') by sum_i ell_m(j_i) dz_i, leaves v(x') (v = 0 on J), the base (b'+- = 0 and
a' = 0 on J) and E (depends only on masses) unchanged; ell_m(zhat) = Delta d_m |zeta_m|/q_0 = 0, so the needed moves are O(|ell_m(x'_n)|)
-> 0 and stay inside the rooms. With the rank condition this is a fixed invertible r x r system. I see no gap; the step can be
written in 5 lines (upgradable to PROVED). VERDICT: correct (SKETCH label conservative).

## Lemma 3.1 (mismatch identity) -- re-derived
b'+ = b'_0 + theta l - theta Delta d' R*w' - c+ R*(w'-w), with l = v + Delta d R*w' - Delta d R*(w'-w): matches. b'+-(x') = -c+- Bx
(g'(x') = 0, <omega - d'(omega) w', R x'> = 0, <w', R x'> = |R x'|). Tuning identity l(x') - Delta d|Rx'| = v(x') - Delta d Bx. PROVED.
Useful reformulation (not in N2): with theta = 0, c+- = 0 one has EXACTLY b'+ = b'_0 and b'- = b'_0 - v', v' := R*(Delta omega - d'(Delta omega) w')
(the transfer recomputed with f''s data), v'(x') = 0 automatically. So the side-minus cost is the kink of v' at f', and
v' - v = -Delta d R*(w'-w) - (Delta d' - Delta d) R*w'. Exact tuning is needed only to kill the second term up to o(t_n).

## Lemma 3.2 -- re-derived
(a) = Lemma 1.3 with y = w. (b) sigma'W(k) = (1 - tau rho d')M' + |s|(M'+M); <DW,Dw'>/C' >= (1 - tau rho d')C' + tau rho d' + |s|C' - |s|C
(uses <Dw,Dw'> <= C C' and s < 0); sum = 1 + |s|(1 + M - C) = 1 + 2M|s|. PROVED. Numerics reproduced (min ratio 0.999998).
## Lemma 3.3 -- re-derived. zhat notin c_0 (f non-NA), xhat' in c_0\{0}; y in S_{q*} separating; tails of (u_{k,m})_k dense;
q**(zhat) = 1 = q(xhat'); Fact C threshold theta_m Phi_m(k) -> 0 and sign w(k) = sign zeta(k) on P. PROVED (needs no closeness of f').

## Corollary 3.4 -- over-stated conclusion
PROVED: within the family Omega'+- = omega+- - d'(omega+-) w' + c+-(w' - w) (i.e. the convexity lemma with y = w), Delta d < 0 forces
tau c > 0 on one side, and then N >= 1 + 2M|s|. NOT proved: that "the mismatch must be absorbed in the base" for every decomposition
of f' + tau rho g' (p* is an inf over all decompositions; other y, partial absorption of (w'-w)1_A with A = opposite peaks, etc.).
I checked the obvious alternatives (y = 2w' - w; y = w' + (w'-w)1_{A^c}): they fail or produce first-order costs ~ |M'-M| + |C'-C|
+ (non-peak shifts), i.e. a pinning condition again; so the HEURISTIC reading is plausible, but the word "must" should be "in the
convexity mechanism". VERDICT: correct_with_fixable_gaps (wording).

## Theorem 2 (Delta d > 0) -- constants gap
Block: Lemma 1.3 gives factor 1/(1-s), s = tau rho theta Delta d <= T_0 rho Delta d. The text only imposes s <= 1/2, which allows the
second-order coefficient to DOUBLE (H'/(1-s) up to 2H'), destroying the bound <= s(tau) when H ~ 1. Fix: add T_0 rho |Delta d| <= eta_0/2
to Step 0 (then 1/(1-s) <= 1 + eta_0). Tuning: psi~_n(0) = psi_n(0) - Delta d Bx_n(0) <= psi_n(0) < 0 (good sign); mubar_n must be
enlarged to 4 nu (7 D_n + Delta d Bx_n(0))/c_+ (still -> 0). d/dmu Bx -> 0 uniformly: J(R x'_n(mu)) -> w weak* uniformly in mu because
R x'_n(mu) -> R**zhat in norm uniformly (z'_n independent of mu, E(A_n(mu)) -> e uniformly), and dE/dmu converges in norm. OK.
(TT) => (BR): Bx <= <w'-w, R(x'-zhat)> (convexity at R x'), <w'-w, RU(E-e)> <= ||E-e|| sum_k lambda_k|w'(k)-w(k)| = o(t_n),
far part <= 2 theta_{N''}; mu_n = O(t_n) since psi~_n(0) = O(t_n) (window O(t_n), tail <= D_n-scale, Bx_n(0) = o(t_n)). OK.
VERDICT: PROVED after the constant fix (correct_with_fixable_gaps).

## Theorem 3 (Delta d < 0) -- tuning-direction gap (substantive but repairable)
The proof says "tune psi~ = v + |Delta d| Bx to 0 (as in 3.5)". In 3.5 the IVT works because psi~_n(0) <= psi_n(0) < 0. For Delta d < 0,
psi~_n(0) = psi_n(0) + |Delta d| Bx_n(0) with psi_n(0) in [-7D_n, -D_n] and Bx_n(0) >= 0 NOT compared with D_n. Without (TT) the only
devices lowering psi~ are the (discrete) far pulls, whose own contribution to Bx is <= 2 sum_k lambda_k |w'(k)-w(k)| |u_k|(Far_n) --
a T-dependent far-tail comparison with sum_Far |v_j| (exactly the comparison N2 itself flags in 3.5/3.7(b)). Moreover common opposite
peaks (Lemma 3.3) contribute POSITIVELY to Bx (each flipped peak k adds lambda_k (M+M')|u_k(x')|), so Bx_n(0) cannot be assumed
negligible. If psi~_n(0) > 0 and only upward devices exist, Delta d' - Delta d is not o(t_n) and side minus carries
(Delta d' - Delta d) R*w', a first-order kink of size ~|tau| |Delta d' - Delta d| ||R*w'||.
FIX: add to the hypotheses either (TT) (then Far_n = empty and psi~ is two-sided tunable) or Bx_n(0) <= D_n/(2|Delta d|) (e.g. (BR)).
Second (minor): G_n must use a larger factor: on Far_n the v-part already eats 2/3 of |a'_j| (|tau rho v_j| <= T_0 rho|v_j| <= (2/3)|a'_j|),
so a further |tau rho E'_j| <= |a'_j|/2 can flip the sign; define G_n with 4 T_0 rho |E'_{n,j}| > |a'_{n,j}| (or double the far masses).
Everything else (side + = certificate (b'_0, omega+) for tau > 0 with no kinks; side - kink <= 2|tau| rho sum_{G_n}|E'_j| via
|a+x+y| <= |a| + sign(a)(x+y) + 2|y| when a+x has the sign of a; h'(b'-) -> h(b-)) is correct.
VERDICT: correct_with_fixable_gaps (PROVED only after adding (TT) or a Bx_n(0) bound to the hypotheses).
