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
