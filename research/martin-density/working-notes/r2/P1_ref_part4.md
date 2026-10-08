# P1 referee — part 4 (6.3 engineered recovery; remaining items)

## 6.3 (SKETCH) — checked regime by regime; plausible, with three fixable gaps
Verified: Fact D compatibility (z' = sign a' on supp a': +1 at 1 and on window/tuning contacts, -1 on Far), a' -> a in l_1
(window masses O(t_m), far masses 2 T_0 S sum_Far u_j = O(T_0 S t_m)), z' -> z coordinatewise, hence f' -> f.
(i) exact carrier: u(x') = <U*u, e'-e> - sum_{K'} u_j (1 - z'_j) (re-derived); j_+ exists (P_{e-perp}U*u != 0 because u is not a multiple
    of e_1*); for diagonal U the window masses raise <U*u, e'-e> by ~ sum u_j sigma_j^2 m_j/nu > 0 (re-derived), the Far pulls lower u(x')
    by 2 sum_Far u_j, the Far masses' own effect is O(T_0 S max_{j>N} nu_j sum_Far u_j). u(x') is affine in a partial value z'_{j*} that
    does not affect e', so u(x') = 0 is attainable. CORRECT.
(ii) |t| <= t_m: base part g' - mu_inf u is supported in supp a' and dominated by the masses; first-order term (g' - mu_inf u)(x') = 0;
    block part exact because w'_1(2) = 0. Convexity bound phi(mu_inf) <= max(kappa+, kappa-). CORRECT.
(iii) t_m <= |t| <= T_0: signs re-checked coordinate class by coordinate class (window, contacts in (N,N''] \ Far, Far absorbed by the
    negative masses: |a'_j + t rho B_j| = |a'_j| + z'_j t rho B_j, tail beyond N''). CORRECT.
(iv) slack. CORRECT given g in C(f).
Gaps: (G1) the statement lacks the hypothesis g in C(f) (needed in (iv); rho^2 max(kappa+,kappa-) < 1 is only a small-scale condition);
(G2) the partial-pull coordinate j* has first-order cost <= 2|t| S u_{j*} in regime (iii): choose it beyond the tail threshold
(u_{j*} <= (1-rho^2) t_m/(96 S)) after making the residual of the Far-mass equation smaller than 2u_{j*}; (G3) the order of quantifiers
(T_0 first, depending on rho and on uniformity of the second-order expansions; then N, t_m, Far, N'', j*) should be stated.
Sharpening (not an error): on side + any carrier coefficient mu <= inf theta is admissible (contacts absorb (theta_j - mu)u_j >= 0), on side -
any mu >= sup theta; so kappa+ can be replaced by min_{mu <= inf theta} phi(mu), kappa- by min_{mu >= sup theta} phi(mu),
phi(mu) := max(h(g - mu u), mu^2/C_1). With C's transfer peaks (C Thm 7.4) inserted in the approximants, the max should be replaceable by
the mass-weighted average q_0 h + sigma_1 mu^2/C_1 (HEURISTIC). A one-sided version of C Prop 8.1 (lower bound) would then give
"every g in C(f) satisfies the condition", i.e. f in R for the example (route for (O4); HEURISTIC).
Correction to A_referee §5.4: VALID. In the diagonal case every sign-compatible mass raises u(x''); pulls beyond N' are limited by the
tail mass (<= (1-rho^2) t_m/(6c)), pulls inside the window cost first order; the mismatch ratio ~ c^2/(1-rho^2) blows up as rho -> 1.
The same objection applies verbatim to E_notes 1.4(i) ("eta-trick + truncation", SKETCH), which also needs the far negative masses.

## Remaining items
* 4.1 exact resonances: PROVED (derivative inequality q*(a+sD) >= 1 + s D(zhat) + s kappa(D) for s > 0, block inequality, cancellation
  D(xi) = <Omega_D, L**xi>).
* 4.2 sign rule: PROVED; essentially tautological (|u(xi)| = (1-gamma) theta Phi off P). The application in §0/§7.1 ("switching needs
  perturbations >~ Phi ... and then (4.4) the mate is in cl Cert(f) unless the gaps are summable") over-generalizes 4.4, which needs a
  single carrier family with rate ||u_{k_i} - v|| = O(lambda_i), the H-condition (c) and monotone gaps: HEURISTIC in that generality.
* 4.3: PROVED; bound chain checked numerically (refP1/t4_wavg.py, 3000 random (rho, s0), cancellation-free: max (bound - s(s))/min(s^2,s)
  = -9.5e-5 < 0). 4.4: PROVED; the case s > r(c^0)/rho (all components "fine") is covered by choosing i_0 with K' lambda_{i0} small — say so.
* 5.1-5.3: PROVED. 5.4 bullet 2's description of "minimizing families" is HEURISTIC (not derived).
* 6.0-6.2: PROVED (all six steps of 6.1 re-derived; margins mu >= q_0 min(1/4, 2 sqrt Phi) re-derived for all three peak types).
* 7.1 bullet 1 (Conjecture A 7.5 cannot hold as stated): correct, modulo A's informal notion of scale separation; for the T of 2.1 the
  non-special vectors differ from their targets by ~ rho_l + delta_l >> lambda, and signature tails force tiny coefficients in any
  combination approximating a block vector at scale lambda, so T is scale separated under any reasonable formalization.
* (T3) (injectivity of R_m**) is used implicitly in 2.2 (via Fact B/C); it follows from (T-d).
* (T4) for P1's T: Preprint B Thm finite-blocks(b) uses only density of block tails (block-sign argument), which (T-d) gives. OK.
