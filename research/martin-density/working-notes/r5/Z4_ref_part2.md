# Z4 referee, part 2: Theorem A (= Theorem 3.1, S_Binf), Corollaries 4.1, 4.2 -- line-by-line check

Numerical check of the Prop 1.2 fix: Z4_ref_work/clamp_lowering.py (one block, clamp formula, coarse v scaled by a common ratio,
fine v arbitrary): sum_k Phi_k|w^L-w| / eps_L and sup_coarse |w^L-w| / eps_L stay bounded (0.02 .. 37, the large value when C = 0.003,
consistent with K_w ~ 1/C) while sum_k v_k grows linearly with the number of carriers (11.8, 26.5, 49.1 for n = 40, 80, 160).

## Step 1 (good pinning). CORRECT. S*_l(l_*) removes only coarse swallowed targets; fine targets (good or swallowed, l' > l_*) are in the
box remainder <= 6t^2. Unrolling: for swallowed l the recursion has factor 1 (x_l = 0), the factor (1+3/r*_l) with r*_l := 2||v_l 1_{S_l\F}||
is harmless. Needs r*_l(l_*) > 0 for all good l <= l_* (built into Lambda* < infinity, hence into (W_inf) along the chosen subsequence).
## Step 2. CORRECT. e_0 = -sum_{l notin U} Delta theta_l u_l 1_{F^c} (using -Delta theta_l = eps_l tau_l on B). Inactive swallowed carriers:
<= l_* of them, |Delta theta_l| <= 6 lambda_l / t < 6t. c_U(tau|_U) = sum phi(Delta B - e_0) <= t/q_0 + 2||e_0||.
## Step 3. CORRECT. Level of kappa(f,U) is <= l_* (U ⊂ [1,l_*], n = max F <= l_*); Z'_{kappa(f,U)} = zero-cost cone of f (Lemma 2.2).
Upper bound through an anti-sign swallowed peak: eq:peakshift gives Delta d M <= -tau_l/lambda_l <= (tau_l)_-/lambda_l <= |tau_l - tau°_l|/lambda_l;
l^dn_m ∈ U_fix ⊂ U (t^2 <= min_{U_fix} lambda). Lower bound through a swallowing-sign non-degenerate swallowed peak: e_k <= t/(sigma|alpha(k)|)
= t/(lambda_l mu_l) by suplevel(c) and eq:margin. Good non-degenerate peaks: badpeaks(a), whose proof needs only Step 1.
IMPROVEMENT (PROVED, one line): the UPPER bound holds at every good peak, degenerate or not: eq:peakshift gives
Delta d_m M_m = -varsigma_k Delta Theta_m(k) - e_k <= |Delta theta_l|/lambda_l <= K* t/lambda_l. So in (H2') the carrier l^dn_m may be ANY good
peak (non-degeneracy is needed only for the lower bound, i.e. for l^up_m).
## Step 4. CORRECT. Peak rows: tau_l = varsigma_l eps_l lambda_l (Delta d M + e_k). Swallowing sign: |tau_l| <= lambda_l K_d t + t/mu_l (needs (H3)).
Anti sign (degenerate allowed): tau_l <= lambda_l K_d t and (tau_l)_- <= |tau_l - tau°_l|.
## Step 5. CORRECT. d-row identity from eq:didentity; inactive swallowed coarse: |q_l tau_l| <= 6 Phi_l^2 M/(C t) with Phi_l < t^2/m;
fine: Phi_l <= c_{l_*+1} <= T_lo(l_*)^3 <= t^3. Repair (Lemma 2.3) needs U ⊃ U_R (true since U_R ⊂ U_fix).
## Step 6. CORRECT. Representation of g_t by both pairs (R_m^* e_k = lambda_k u_k cancels the base difference; d-neutral since tau' = 0 at peaks
and the d-rows of Z_U hold). Sides: b^+ 1_{F^c} = chi V', b^- 1_{F^c} = -(1-chi) V'. (b),(c): every discrepancy is listed (good coarse via the
claim of prop:windowcert(c), inactive swallowed coarse < 6t each, U ∩ P via eq:peakshift with tau'_l = 0, U_np exact, fine via box).
(d): |omega^-(k(l))| <= 4/t + (6 lambda_l/t + C_dia t)/lambda_l <= (10 + C_dia)/t because lambda_l >= t^2 on U -- this is the point of the
scale-dependent active set; gap >= gamma_f(l_*).
## Step 7. CORRECT (re-derived from the proofs of lem:uniformtransfer, lem:onesidedtransfer and Lemma lem:block(d)): the radius conditions
are gap/(2|omega|) >= gamma_B t/(2A_2), 1/(2|d|) >= t/A_3, C/(2|d|M) >= C t/A_3; all relative errors are O(A_3 c_flat); t_1 is constrained
only by r^4-terms and by K_3 c_flat^2 t_1^2 (2 + Lambda^varsigma) <= gamma/2, which do not involve A_2 or gamma_B. So c_flat >= c_f gamma_f/C_dia.
## Step 8. CORRECT. Lemma 6.1 is correct (c_flat enters Theorem thm:windowed only through I_r and Q, at fixed j). Arithmetic:
K_j/c_flat <= C G*^4 (Lambda* + l + M_f)^2/(gamma_T^2 gamma_f) = C G*^4 Lambda°^2 Xi_f; n^w >= (l 2^{l^3} Lambda° G*)^6; and
K_j T_hi <= C G*^2 Lambda° Xi_f^{1/2} (l 2^{l^3} Lambda° G*)^{-6}. (W_inf) is MORE than enough (the true requirement allows an extra factor
Lambda°^4 G*^2 in (i)); C_dia T_hi -> 0 by the same computation.
## Step 9. CORRECT. Averaging preserves every linear condition of d-neutral two-piece data; Gamma_w convex; rho^2(1+eta_0/2) <= 1; Cor cor:D1.
## Hidden-assumption audit (all pass): F finite; I = {1..N} finite; f' (engineered) chosen after g, rho inside Cor cor:D1; uniformity in t,
window and number of active carriers: G*(l_*) covers all U ⊂ [1,l_*]; Lambda*, M_f, 1/gamma_f, 1/gamma_T are monotone in l_* and evaluated at
l_*; C_1..C_4, c_f, A*_0, R_f depend only on f (fixed carriers l^up, l^dn, U_R) -- checked. No (H1) needed: targets of swallowed carriers
on other swallowed signature sets lie in T(U) and are handled by (Z2). (MS) not needed: margins enter only via M_f (swallowing sign).
## Fixable gap (N-dependence): G*(l) is defined with U ⊂ L_N ∩ [1,l]; to keep ONE operator for all N (needed for Lemma martintail),
let U range over all subsets of [1,l]. Then SLD_G is N-independent and Theorem A holds for every N. (Same remark for Prop 2.4.)
VERDICT Theorem A: PROVED (with the N-independence fix; optional weakening of (H2') as above).

## Corollary 4.1: CORRECT as a conditional statement. H^Z_f(l) is a max over finitely many U, each system has a finite Hoffman constant
(0 is feasible). Under (DR): dist(tau, Z_U) <= G* viol + R_f sum|delta_m(tau_0)| <= C_f G* (viol + sum|delta_m|), so H^Z_f <= C_f G*.
CAVEAT: (W_inf^orig) contains Lambda°(l) in the numerator: H^4 (Lambda* + M + l)^2/(Lambda° gamma_T^2 gamma_f l 2^{l^3}) -> 0. Since
Lambda*_f(l) >= Lambda°_N(l) := prod_{l'' <= l, l'' in L_N}(1 + 2/delta°_{l''}) (r*_l <= ||v_l||_1 = delta°_l), the condition can only hold
if Lambda°_N(l)^2/Lambda°(l) = o(l 2^{l^3}) along a subsequence; this depends on the sets S_l and the ladder bijection, which
Definition def:SLD leaves free (log2 Lambda° >= sum_{l''<=l}(l'' + min S_{l''}) - O(l)). So Corollary 4.1 can be vacuous for some
admissible choices of (S_l) in the ORIGINAL design. Not an error, but it should be stated.
## Corollary 4.2: CORRECT. (a) (B_res): q_l = 0 on B so the "or" clause of (DR) applies; M_f = 0; supp y_l ⊂ supp u_l (allowedness (a) at
l' = l) gives T(B)\F ⊂ K, gamma_T = 1; gamma_f = min M_m; S*_l(l_*) ⊃ S*_l(def:swallowed) so (W*) => (W_inf). (b) (B_fin): U = B once
t^2 <= lambda_B and l_* >= max B; C_dia t^2 <= lambda_B keeps A_2 = 11; needs (W*) (as stated).
