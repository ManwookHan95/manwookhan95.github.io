# Referee report on S3 (second-order rebalancing, exact one-sided invariant, engineering without steering)

Setting checked: canonical base, Martin's norm with a FINITE block set I (p_N; Remark martin-tail), admissible T (Lemma B's conclusion
only). Every PROVED/SKETCH item of ctx/r3/S3_notes.md (= S3_head + S3_part1..4 + S3_tail, byte-identical) was checked line by line.
Details and full proofs of the fixes: ctx/r3/S3_ref_part1.md .. S3_ref_part6.md, assembled in ctx/r3/S3_ref_notes.md.
Referee scripts: ctx/r3/S3ref_work/ (thmB_check.py, thmB_small.py, rplus_indep.py).

## 0. Bottom line
The two main new ideas are sound and the main theorems are CORRECT:
 * Theorem B (exact one-sided second-order coefficient via Fenchel duality) is correct at (BT) points with arbitrary contact set K. It
   bypasses the decoupling gap of C Prop 8.1. I confirmed its finite analogue independently (different solver) for the C-referee certificate
   AND for random directions g, on both sides, including infeasible sides.
 * Theorem D (first-order rebalancing through transfer peaks; no steering) is correct. Corollary D1 (two-piece data with Delta d_m >= 0 in
   every block, kappa_w <= 1, F finite: recovered, no hypothesis on Q_m, K or T) and Corollary D2 (every (BT) point is in R) hold. D2 has one
   circular auxiliary estimate (|C' - C| = O(s_1)), which I repaired (part 6, Lemma F1).
 * Corollary B2: every mate at P1's example is recovered (f in R). Correct.
Over-statements, all in part 4 of S3: the "rho-defect only" reading of 4.3 needs K^scr < infinity (not automatic). 4.4 claims that the
simplified approximants fail, but only shows that a sufficient condition fails. 4.5 needs a regularity hypothesis on Phi that Lemma B does
not supply, and the result is already in A_notes §7.4. No counterexample is claimed, and nothing found here points to one.
Density of NA((c_0,p), l_2^2) remains OPEN.

## 1. Verdicts
| Claim | S3 label | Verdict | Issues |
|---|---|---|---|
| Lemma 1.1 (rebalancing add-on) | PROVED | correct | Every inequality re-derived. Uses ||alpha'||_1 = 1, which is true. The inefficiency is a cost for both raising and lowering. Valid at any f with the normer xi. |
| Lemmas 1.2-1.3 (transfer data, persistence) | PROVED | correct | Lambda m Phi_* = q*(T) is bounded independently of eta_1, which makes "eta_1 before s_1" legitimate in Theorem D. |
| Theorem A (kappa_w for P2A 2.1 / N2 1) | PROVED | correct | Superseded by Theorem D. Cor A' is right in outline; not re-checked line by line. |
| Theorem B (exact one-sided invariant) | PROVED | correct | Re-derived Steps 1-4: Gram system, Z_t/H_t split (contacts are never moved by U k), the conjugates Bconj and Qf_m^*, and the kernel of Qf_m (radial line, also in the degenerate case z_Q = 0). Rockafellar 31.1(a) needs no closedness. Minimum attained. |
| Numerical check of Theorem B | PROVED (numerics) | correct | Reproduced 0.29824 / 0.29567 / 0.28325. Independent SOCP check extends it to non-certificate g (part 3). The script's unreported third case (gamma+ > Gamma_w(cert)) is not a contradiction: k_0 has become a peak there. |
| Cor B2 (P1's example, f in R) | PROVED | correct | (BT) verified from P1 2.2(b), 6.0. (MS): sum <= s^2/(2q_0^2). Side admissibility is mu <= inf theta(g) (resp. >= sup theta(g)). Delta d = 0 with one block, so Theorem A (or D) applies. |
| Lemma R+ (anchor without (C'-C)_+) | PROVED | correct | The displayed intermediate bound gives only 5||Dw'1_A||^2. Disjointness of the supports of Y gives the stated 4 (cosmetic). Independent test on 17076 random/adversarial blocks: no violation. |
| Theorem D (engineering without steering) | PROVED | correct | Theta piece exactly balanced below s_1. Side pieces have O(s_1) linear mismatches, removed at cost O(|tau| s_1 eta_1). Convexity case (Delta d >= 0) pays only the Bregman term o(s_1). Anchor case pays s E_y + 2s||R*Z_A||. Order of choices respected. |
| Cor D1 (Delta d >= 0: no hypothesis) | PROVED | correct | Deep structure enters only via (E4)-(E5), which hold for every F-finite f. The restriction is the existence of finitely supported two-piece data. |
| Cor D2 ((BT) points are in R) | PROVED | correct with fixable gap | abs(C'-C) = O(s_1) is used to prove the Lipschitz bound, which is used to prove abs(C'-C) = O(s_1) (circular). Fixed by the monotone root equation F(C;v) = 1 (part 6, F1). Contains C Thm 8.4 ((MS) is part of C-tameness). |
| Prop 4.2 ((MS-Q*) => (SC)) | PROVED | correct with fixable gaps | (1) Same circularity, same fix. (2) Several Delta d < 0 blocks need ONE common sequence of scales (liminf hypotheses can live on disjoint scales; F2). (3) Bounding Phi^2 on A_m uses the hypothesis implicitly. |
| 4.3 quantitative recovery | PROVED | correct (implication); interpretation overstated | The implication holds; the factor 8 is conservative (factor 1 suffices with K^scr := limsup (E_y + 2||R*Z_A||)/s_1). "rho-defect only" needs K^scr < infinity. The given sufficient condition ignores near-threshold PEAKS, whose truncated mass can be ~ s log(1/s) for admissible T (F4, SKETCH). Add (MS). |
| 4.4 (MS-Q*) can fail | SKETCH | (MS-Q*)-failure: fair SKETCH; "approximants then fail": unsupported (HEURISTIC) | Only an upper-bound sufficient condition fails. No lower bound on dist(rho g, C(f'_n)) is given. The body says "Theorem D does not apply"; the head and table say more. |
| 4.5 deep coefficients c_k ~ sqrt(Phi_k) | PROVED / SKETCH | correct with fixable gaps; not new | O(sigma) box tails need Phi regularity (e.g. Phi_m(k+1) <= beta Phi_m(k)). Lemma B does not give it: column rescaling keeps T admissible and can cluster Phi (F3). Also needs b supported in F, gaps bounded below, and max-form H <= 1. A_notes §7.4 already states this result. The Gamma_w upgrade is a fair SKETCH; the transfer radius shrinks as eta_1 -> 0, so take eta_1 -> 0 last. |
| Open-core summary | — | incomplete | All of S3 assumes F = supp a finite. Mates at f with a not in c_00 (briefing R7(iii)) are untouched and should be listed in the open core. |

## 2. Main checks (short; full re-derivations in the part files)
**Lemma 1.1.** (i)-(ii) are a direct coordinate count (k in L' keeps its sign since eta < gamma; k notin L' stays below ||V|| - eps since
gamma + 2eta + eps <= M'). (iv) needs ||alpha'||_1 = 1, which holds: norming forces equality in w'(x_0) + <Dw', b> <= M'||x_0||_1 + C'||b||.
(v) is algebra.

**Theorem B.** Upper bound: the base expansion is exact for side-admissible b (no flips on F, cheap sign on K). Blocks: N(w + t(omega - dw))
= 1 + (t^2/2) H C/(C + tdM). All blocks, including inactive ones (they absorb level), are equalised at Gamma_w/2.
Lower bound: test points eta_t = xi + t(Uk + nu_c) + t^2 nu_2. The Hilbert part H_t absorbs U k, so q**(eta_t) <= max(||Z_t||, ||H_t||)
= q_0 + t^2 kappa_2 + O(t^3) with contacts moved only inward. The block expansion (C Lemma 5.1/5.2 + (MS)) is o(t^2)-exact.
Duality: -Psi_* = q_0 h on side-admissible beta (dual cone of C_+), Qf_m^* = sigma_m H_m on balanced v (the kernel of Qf_m is the radial line;
I re-did the degenerate case by hand). Rockafellar 31.1(a): ri dom Qf = R^n, Psi proper concave. Hence lim = gamma^+-, attained.

**Theorem D.** The bookkeeping identity c' l_b + sum sigma'_m l_m = g'(x') = 0 makes a linear mismatch a pure level shift. Transfer peaks
move it at relative cost eta_1, fixed before s_1. The bracket tau(l_b + sum sigma' l_m/c') vanishes exactly, and the remainder is
O(|tau| s_1 eta_1) <= eps_0 tau^2 on |tau| > s_1. Below s_1 the theta piece has l^theta = 0 exactly (d'^theta is the f'-coefficient,
c = (b^theta 1_[1,N])(xhat')) and no kinks or flips (window masses). Convexity case: W = (1-|s|)V_1 + |s| w with N(w) = 1, so the only genuine
cost is |s| Bx c'/sigma'. Bx = o(s_1) by dominated convergence along the sequence. Lemma 1.1's radius condition holds since Lambda is fixed
before s_1.

**Numerics (part 3).** Below the onset radius min gap/|omega| of the optimal decomposition, the exact coefficients (SOCP, tol 1e-14) match
gamma^+- for the certificate (0.29567, 0.28325) and for a random g (1.10419 vs 1.10425; 1.75850 vs 1.75872, 1.75852). Above that radius
they can be 50 times larger. This is harmless for limit statements, but gamma^+- carries no uniform-scale information.

## 3. Required corrections (all fixable; proofs in part 6)
1. D2(i) and Prop 4.2(a)-(b): replace the circular argument by Lemma F1 (C is the root of a strictly decreasing equation, so
   |C' - C| <= K sum_k Phi_k |v'_k - v_k| = O(s_1)).
2. Prop 4.2 "Consequently": require a common sequence of scales for all Delta d < 0 blocks.
3. 4.3: state K^scr < infinity, or add (MS), before concluding "rho-defect only"; the factor 8 can be 1 with
   K^scr := limsup (E_y + 2||R*Z_A||_1)/s_1.
4. 4.4 / head / table row 15: replace "the simplified approximants then do not recover" by "Theorem D's estimate does not apply
   (failure of recovery along these approximants: HEURISTIC/OPEN)".
5. 4.5: add the Phi-regularity hypothesis. Keep b in l_1(F), gaps bounded below and max-form H <= 1 in the statement. Cite A_notes §7.4
   for priority.
6. Lemma 3.2: use disjointness of S and A in the bound for ||DY||^2 (constant 4, not 5).
7. Open core: add "a not in c_00 (F infinite)". Every S3 theorem needs F finite (no flips on F for |tau| <= T_0).
8. gamma_side.py: flag the third case (k_0 is a peak there, so the "certificate" is invalid).

## 4. Most valuable idea
First-order rebalancing. In any exact decomposition of f' + tau g' at an NA point, the first-order terms of the pieces satisfy
c' l_base + sum_m sigma'_m l_m = g'(x') = 0. A linear mismatch between base and blocks is therefore a pure level shift. Transfer peaks move
it at a cost (mismatch) x (inefficiency), and the inefficiency is fixed before the mismatch scale. This makes all exact steering
unnecessary: far pulls, IVT tuning, (S), (TC), (TT), (BR). Only genuinely nonlinear first-order costs remain (kinks, Bregman terms, anchor
remainders). Together with Theorem B's duality (optimal side decompositions exist and have kappa_w <= 1), this reduces recovery at
F-finite points to two questions: existence of two-piece data, and the Delta d < 0 scrambling quantity. The same mechanism should be
tried on O3 (scale-dependent switching): P2A's consistency identity needed exact replication only because mismatches were not
rebalanceable.

## 5. Status after S3 (referee's view)
PROVED (with fixes): all (BT) points are in R for any contact set; all F-finite two-piece mates with Delta d >= 0 (kappa_w <= 1) are in Ls(f),
for every admissible T. OPEN: Delta d < 0 at blocks violating (MS-Q*); mates at generic supports (Q infinite, (MS) failing, degenerate
peaks) that are not limits of two-piece data (O3); mixed deep + switching mates; F infinite. Nothing in S3 or in this check points toward
a counterexample.
