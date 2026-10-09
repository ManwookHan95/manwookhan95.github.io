# N2 part 5: can engineering provably fail? (task item 3), localization of any obstruction, numerics, assessment

## 5.1 What a non-recovery proof must show (reformulation; PROVED in N_part1)
By N_part1 Thm 1 and Prop 1.5(c), (f, rho g) is NOT in cl NA for some rho < 1 iff rho g is not in Ls(f) iff there are x_1, ..., x_k in c_0 and
delta > 0 with  max_i ( rho g(x_i) - r~_{f'}(x_i) ) >= delta  for EVERY f' in NA cap S_{p*} with p*(f' - f) < delta,
where r~_{f'}(x) = max{h(x) : h in C(f')} = inf{ sum_j (p(y_j)^2 - f'(y_j)^2)^{1/2} : sum_j y_j = x }.
So a counterexample needs UPPER bounds for r~_{f'} uniformly over all NA f' near f, i.e. for every such f' explicit primal
decompositions of the x_i that make the excess p - f' large. Every engineering device (masses on contacts, far flips with negative
masses, tuning masses, implanted off-peak coordinates, transfer peaks, averaging over scales) LOWERS such upper bounds in specific
directions, and the adversary (the approximant) chooses f' after the x_i are fixed. I found no configuration in which a uniform upper
bound can be established; for every candidate examined, an engineering device either provably recovers the mate (Theorems 1-2) or
the failure of the devices I know is reduced to an explicit quantitative property ((PC), (CC)) whose failure is NOT shown to imply
non-recovery (other devices remain). Hence: no counterexample, and no claim of one.

## 5.2 Proposition (where any obstruction must live: the near-free part). PROVED modulo R1 (P1_referee, itself mod C Thm 6.2/Prop 6.5).
Let f'_n -> f be NA approximants that are C-tame (finitely many strict non-peaks and degenerate peaks in each block, (MS) at x'_n), and let
g be in Li_n C(f'_n). Then for every finite set J_0 of free coordinates of f (|z_j| < 1, j notin F):
  P_{J_0} g = lim_n P_{J_0} ( sum_m R_m*( omega'_{n,m} - d'_{n,m}(omega'_{n,m}) w'_{n,m} ) )  for suitable omega'_{n,m} in c_00(Q'_{n,m}),
i.e. the free-coordinate part of g must be carried by OFF-PEAK BLOCK coordinates of the approximants; base masses cannot carry it.
*Proof.* By R1, g = lim g'_n with g'_n in S(f'_n) = (l_1(supp a'_n) cap xhat'_n-perp) + span{R_m* (e_k - d'(e_k) w'_m) : k in Q'_{n,m}}. For j in J_0,
z'_n(j) -> z(j) with |z(j)| < 1, so |z'_n(j)| < 1 for n large, hence j notin supp a'_n (z' = sign a' on supp a'). Apply P_{J_0}. QED.
Reading. EXACT two-piece mates have their switching part on F cup K (v is supported there), so their J-part is carried by the fixed
certificate parts omega+-; Proposition 5.2 is no obstacle and indeed Theorem 1 recovers them. A mate whose switching component has a
nonzero J-part (approximate resonances with core errors on free coordinates; E's rigid design) can only be recovered by CONVERTED or
IMPLANTED off-peak block coordinates of the approximants: this is the rigorous reason why conversion capacity (part 4) is the
decisive quantity there, and why base engineering alone (masses, flips) cannot suffice for such mates.

## 5.3 The candidates, examined against the full list of approximant devices
 (a) Exact resonances, Delta d = 0 (P1's defect, A_referee 5.2, constant or non-constant splits, cross-block exact relations): RECOVERED
     (Thm 1, rigorous; multi-block under a rank condition).
 (b) Exact resonances, Delta d > 0: RECOVERED under two-sided mass tuning (Thm 2); otherwise under (BR) (a far-tail comparison).
 (c) Exact resonances, Delta d < 0, and the C_referee kink class with c' > 0: the convexity mechanism provably fails on one side (3.4); recovery
     reduces to pinning R*(w' - w) on near free coordinates at precision o(t) (Thm 3). A non-recovery proof would have to show that EVERY
     approximant violates (PC) AND that no other decomposition of f' + tau g' on the bad side avoids the mismatch; e.g. extra absorbing masses
     (3.6 Rem 1), implanted off-peak coordinates (A Lemma 8.2) whose R*-images cancel the J-part of the mismatch, or transfer peaks
     (C Thm 7.4) acting at second order. None of these is excluded. No proof of non-recovery is in sight; in the block-tame robust case (PC)
     holds up to a perturbation lemma (3.7(a), SKETCH).
 (d) Approximate resonances through one-sided block carriers (weak peaks, super-near-threshold non-peaks, perturbed cross-block duplicates):
     recovery needs J(rho) ~ 16 kappa/(1-rho^2) two-sided carriers with frozen errors O(scale) at adjacent scales below the destruction
     boundary (Thm 4). Far rigidity can limit conversions of the ORIGINAL carriers (4.5, consistent with Lemma B), but implanted /
     generic-coordinate carriers (4.6(ii)) are not excluded, and averaging over scales (Thm 4) needs only finitely many for each rho.
     Model N's excess is model-level (NUMERICAL), not a lower bound.
 (e) Second-order (rebalancing) defects ({Gamma_w > 1} with Gamma_2 <= 1): at f with infinitely many kinks these are exactly (c)/(b) (1.6, 3.9);
     at kink-free tame points they are empty (C Thm 8.4 + P1 3.8, PROVED mod unrefereed C).
Conclusion of item 3: no configuration was found in which engineering provably fails; consequently no lower bound dist((f, rho g), NA) > 0 is
claimed. Lindenstrauss property B for l_2^2 is not contradicted by anything established here.

## 5.4 Numerical sanity checks (scripts in ctx/r2/N2_work/)
 * thm1_check.py: finite model of P1's example (referee's model.py: diagonal U, 12 contacts, 10 free coordinates, 7 block coordinates,
   special vector u with u(zhat) = 0), two-piece mate g_{K1} (c = 0.15, random K1), engineered approximant exactly as in Theorem 1
   (window masses 4t|b_theta| on the first 5 contacts, theta = 1/2, one far contact flipped to z' = -1 with negative mass 2 T_0 rho |v_j|,
   tuning mass at a window contact fixed by bisection so that u(x') = 0, hence w'(k_0) = 0 and Delta d' = 0), target g' as in Step 4.
   Exact p* by SOCP (Clarabel). Result (rho = 0.9, 4 seeds, 42 values of t in +-[1e-4, 10]): max_t [p*(f' + t rho g') - s(t)] in
   [-8.4e-9, -1.1e-9] (i.e. rho g' in C(f') to solver accuracy), u(x') = 0 and w'(k_0) = 0 to 1e-15, g'(x') = 0 to 1e-17, ||g' - g||_1 ~ 2-3e-3.
   (In a finite model the far contacts are not small, so the tuning mass and ||f' - f|| are O(0.05-0.4): the check validates the algebra,
   the sign/no-flip structure and the exact tuning, not the asymptotics.) Variant with the last contact set to z' = 0 ("beyond N''"):
   same conclusion (max excess <= -4e-9).
 * lemma32_check.py: random 14-coordinate blocks with a strict non-peak k_0 (w = 0) and 4 flipped fine peaks (176 admissible cases):
   for s >= 0, (N(W) - 1)/tau^2 <= 0.012 (no first-order term, Lemma 1.3/3.2(a)); for s < 0, min (N(W) - 1)/(2M|s|) = 0.999998
   (Lemma 3.2(b) is sharp).

## 5.5 Assessment
 * The only rigorously known defect of intrinsic recovery (P1 Thm 2.4: exact resonance, Delta d = 0) is recovered along engineered
   NA sequences: PROVED (Thm 1). Exact resonances with Delta d > 0 are recovered under a mild tuning condition (Thm 2).
 * The two remaining mechanisms that might defeat engineering are: Delta d < 0 exact resonances (pinning on near free coordinates) and
   approximate resonances with core errors on free coordinates (conversion/implant capacity). Prop 5.2 shows rigorously that the
   second kind can only be recovered through off-peak block coordinates of the approximants; neither kind is shown to resist the full
   list of devices.
 * Leaning: positive (density), with the open core now located precisely: (PC) for Delta d < 0 in the generic (infinitely many
   non-peaks) case, and the supply of two-sided carriers with frozen error O(scale) near the destruction boundary for approximate
   resonances. Both are quantitative tail-independence statements at the scale of the perturbation, i.e. properties of T relative to f.
