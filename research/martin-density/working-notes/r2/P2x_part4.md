# P2x part 4: limits and extensions of Theorem 3.5 (sign of Delta d, tuning failure, a not in c_00, carriers)

Setting of P2x_part3. N2 = parallel notes ctx/r2/N2_part*.md (unrefereed); cited where they overlap.

## 4.1 Delta d_m < 0: what fails and what is needed. PROVED (failure) / conditional (recovery).
(a) Failure of the convexity mechanism (N2 Lemma 3.2(b), 3.3, Cor 3.4 — re-checked, correct): at an NA approximant f' of a non-attaining f, every
block has infinitely many common peaks k of w_m and w'_m with w'_m(k) w_m(k) < 0 (u_{k,m} close to a functional separating zhat from xhat';
(T2)). If a block part w' + s(omega - d'w') + s c (w - w')... is moved AWAY from w (s c < 0 in the notation W = w' + ... + s'(w - w'), s' < 0), the
common opposite peak k gives |W(k)| >= (1 - s d')M' + |s'|(M' + M), and Cauchy-Schwarz on the Hilbert part gives N(W) >= 1 + 2M|s'|: a first-order
excess. Since the two sides need c- - c+ = Delta d (P2x_part3 Step 3 algebra with theta-split), Delta d < 0 forces such a move on one side.
(b) Hence for Delta d_m < 0 the mismatch Delta d_m R_m*(w'_m - w_m) must be paid in the BASE on one side, at first-order price
 |sigma| |Delta d_m| Kink'(R_m*(w'_m - w_m)) (+ flips), and recovery holds as soon as (PIN) Kink-weighted ||R_m*(w'_m - w_m)||_1 = o(s_1) at the tuned
approximants (proof: Steps 3-6 of Theorem 3.5 with Omega'-_m := omega-_m - d'-_m w'_m and the extra base term; = N2 Thm 3 under its (PC)).
(c) (PIN) is a genuine requirement: P2x_part2 Remark after 2.3 — the window masses move every off-peak value with Phi_k >~ s_1 by ~ s_1/Phi_k, so
sum_k lambda_k |w'(k) - w(k)| = Theta(s_1 * #{off-peak k : Phi_k >~ s_1}) unless the off-peak values are PINNED.
(d) Pinning at block-tame robust blocks. SKETCH. Let Q_m (strict non-peaks of w_m) be finite, every peak of w_m robust in the window
(margin mu_k := |u_k(zhat)| - theta Phi_k >= C s_1 for all peaks k <= K(s_1), K(s) := min{K : sum_{k>K} lambda_k <= s^2}), no degenerate peaks.
Converse of Fact C (PROVED, elementary): if zeta'' = c''(alpha'' + D^2 w/C) with alpha'' supported on P, sign alpha''_k = sign w(k), ||alpha''||_1 = 1, then
J(zeta'') = w (w norms zeta'': <w, zeta''/c''> = M + C = 1 >= |zeta''/c''|). Apply it to zeta^# := R x' on [1,K] and c R** zhat on (K, inf): if
  (i) u_k(x') = c u_k(zhat) for k in Q_m (|Q_m| linear conditions, c > 0 free), and
  (ii) sum_{k in P, k <= K} sigma_k lambda_k (u_k(x') - c u_k(zhat)) = 0 (one more linear condition, fixing c),
then zeta^# = c|zeta|(alpha~ + D^2 w/C) with alpha~ := alpha + (zeta^# - c zeta)/(c|zeta|) supported on P, ||alpha~||_1 = 1 (by (ii)) and sign-correct (by the
margins), so J(zeta^#) = w EXACTLY. Then w'_m = J(R x') differs from J(zeta^#) only through the deep perturbation ||R x' - zeta^#||_1 = O(s_1^2);
the missing step is a Lipschitz estimate for the finitely many scalars (M', theta') of the clip formula under such perturbations (true when
the 2x2 system defining (M, theta) — C^2 = M^2 S_2(theta), theta m (1-M) = M^2 S_1(theta), S_2 := sum Phi_k^2 clip(u_k/(theta Phi_k))^2,
S_1 := sum lambda_k u_k clip(...) — is non-degenerate at f; not verified in general). Given it, w'_m - w_m = O(s_1^2) on [1,K] and
(PIN) holds with the deep part <= 2 sum_{k>K} lambda_k <= 2 s_1^2. The tuning needs (TC) for the |Q_m| conditions (i)-(ii) (effect vectors
u_k - (u_k(zhat)/pi(zhat)) pi restricted to the moves, pi := sum_P sigma_k lambda_k u_k). This agrees with N2 Prop 3.7(a) (one non-peak).
(e) Infinitely many strict non-peaks in a block with Delta d_m < 0: pinning needs ~ #{off-peak k : Phi_k >= s_1} -> infinity conditions,
solvable with O(s_1) moves only under a quantitative tail-independence property of T (N2 3.7(c)). OPEN.

## 4.2 Failure of (TC): far pulls. SKETCH (PROVED for one block with Delta d = 0 in N2 Thm 1, not re-checked line by line here).
When every available move pushes the tuned functionals the same way (P1's example with diagonal U: the only active functional is
v = c u_{2,1}, supported on F u K', and every contact mass raises v(x')), the correction must come from FAR CONTACTS used with the flipped sign:
for j in Far subset K cap (N, N''], set z'_j := -z_j and a'_j := -m_j z_j with m_j := 2 tau_1 max(|b+_j|, |b-_j|) (so that both one-sided decompositions
are LINEAR at j for |sigma| <= tau_1: the usage of side +- at j only decreases |a'_j| by at most half). The effect on the tuned functional
Gfun_m is -2 z_j V_m(j) per pulled coordinate (plus a Hilbert effect O(m_j nu_j), nu_j = ||U*e_j*|| -> 0). Order of choices: N, then s_1 small compared
with the pull reservoir sum_{K > N} |V(j)|, then Far, then N'' (window of the decompositions) so that tails beyond N'' cost <= eps_0 s_1^2.
Improvement over P1 6.3 (the partial-pull coordinate j* of P1, whose first-order cost the P1 referee flagged): exact tuning is unnecessary.
The residual (Delta d_m - Delta d'_m) R_m* w'_m can be put in the base on side - at first-order cost <= 2 |sigma| |Delta d_m - Delta d'_m| q*(R_m* w'_m), which is
<= eps_0 sigma^2 for |sigma| >= s_1 as soon as |Delta d_m - Delta d'_m| <= c eps_0 s_1; since the pull increments 2|V_m(j)| -> 0 (j -> infinity), a finite
Far realises any required correction within c eps_0 s_1 (subset sums of a null sequence with divergent... finite total: every value in
[0, sum] is within the last increment of a finite subset sum). With Delta d_m > 0 the pulls also enter the Bregman term:
<w' - w, R(z' - z) 1_Far> <= 2 sum_k lambda_k |w'(k) - w(k)| ||u_k 1_Far||_1, which must be o(s_1): a comparison between the far tails of V and of the
other block vectors (T-dependent; N2 3.5). Status: Delta d = 0 one block PROVED (N2); several blocks / Delta d > 0: SKETCH.

## 4.3 a not in c_00 (F infinite). SKETCH.
Window truncation a' := (a 1_[1,N] + Delta)/q*(...). Base parts b+- are supported in F u K with flips allowed at f (they are included in (H1)).
(i) Flip costs at f' vs f: the normalisation changes |a'_j| by a factor 1 + O(s_1 + tail_N(a)); on the flip set {j : |a_j| < 2|sigma b_j|} this changes flip costs by
<= C (s_1 + tail_N(a)) |sigma| sum_{flip set} |b_j| = o(1) s_1 |sigma|, which is <= eps_0 sigma^2 for |sigma| >= s_1 once s_1 is small (phi(sigma) := sum_{|a_j| < 2|sigma b_j|} |b_j| -> 0);
increasing |a'_j| (masses of the sign of a_j) never increases flip costs.
(ii) The two-sided small-scale regime of side + needs no flips for |sigma| <= s_1: add masses 2 s_1 |b+_j| sign(a_j) at the j in F with |a_j| < 2 s_1 |b+_j| (total o(s_1)).
(iii) Coordinates of F beyond N: tails, first-order cost <= 2|sigma| tail_N(b+-) (N after s_1).
Everything else is as in Theorem 3.5. The only new point to check in full is the uniformity of (i) on [s_1, tau_1]; I see no obstruction.

## 4.4 Carriers. SKETCH / OPEN.
(a) Infinitely supported bounded off-peak carriers omega+- with the near-peak decay of A Lemma 6.3 on BOTH sides: truncate at a level
chosen after s_1 (D Lemma 11.5(b) gives exact first-order correction and uniform second-order control on a fixed range); the discarded part changes
the transfer v by a vector of l_1-norm o(1), put in the base at first-order cost <= eps_0 s_1 |sigma|. The delicate point is that the truncated
carriers have gaps gamma(s_1) -> 0, so Lemma 3.2(a) (exact sup part for |sigma| <= s_gamma) is not available on all of [-s_1, 0]; one needs the box-tail
argument of A Thm 6.2 (coordinates with |sigma omega_k| > gap_k/2 discarded into the base at cost o(|sigma|)) AT f', i.e. uniformly along the approximants.
Plausible (the box tails are controlled by the decay, and gaps at f' converge), not written. SKETCH.
(b) Degenerate peaks (alpha_k = 0) used one-sidedly by a linear decomposition (sigma_k Omega(k) on one side of -d M): at f' such k is a peak with
alpha'_k ~ lambda_k (|u_k(x')| - theta' Phi_k)/|zeta'| or an off-peak with tiny gap; one scalar tuning per degenerate carrier keeps it at threshold
(alpha'_k = o(s_1)), after which its one-sided use costs o(s_1)|sigma|. SKETCH.
(c) Weak (non-degenerate) peaks and off-peak carriers whose DEPTH depends on the scale: not covered — part 5.

## 4.5 Summary of the two-piece / finitely-generated class.
| class (f with a in c_00 unless stated, finite I) | status |
|---|---|
| two-piece data, Delta d_m >= 0 all m, (TC) | recovered along engineered NA sequences: PROVED (Thm 3.5) |
| two-piece, one block, Delta d = 0, (TC) fails, pull reservoir | PROVED in N2 Thm 1; P2 4.2 removes the j* issue (SKETCH) |
| two-piece, Delta d > 0 with pulls | SKETCH (far-tail comparison, T-dependent) |
| two-piece, some Delta d_m < 0 | needs (PIN): block-tame robust blocks SKETCH (4.1d); infinitely many non-peaks OPEN |
| a not in c_00 | SKETCH (4.3) |
| infinitely supported carriers with near-peak decay; degenerate-peak carriers | SKETCH (4.4) |
| P1's explicit defect mates (P1 2.3, 6.2 with kappa+- <= 1) | PROVED by Thm 3.5 if some contact has <P_{e-perp}U*u, U*e_j*> < 0; otherwise N2 Thm 1 |
