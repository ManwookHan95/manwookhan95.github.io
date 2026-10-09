# Referee report on N2 ("Limits of engineering: resonant mates")

Material read: N2_notes.md (in full; the part files N2_part1-5 are identical to its sections), BRIEFING, BRIEFING_R2, Martin summary,
A_notes §1, §4 (Facts A-F, Def 4.1, Lemmas 4.3-4.7, Prop 4.5), P1_notes §2, §6 and P1_referee, C_referee §1.20, E_notes §6-7 and
E_referee §3.1, N_part1, Preprint B Remark martin-tail. Setting: canonical base, FINITE block set I (p_N); this is legitimate because
Remark martin-tail says density for p_N at arbitrarily large N gives density for p. Full verification notes: N2_ref_notes.md
(parts N2_ref_part1-4.md). Scripts: N2ref_work/.

## 0. Bottom line
* The central result is correct. Theorem 1 says that exact two-piece mates with Delta d = 0 and one active block lie in Ls(f). I re-derived
  every step: the tuning direction (Lemma 2.1), the IVT estimates of Step 2, the side identities b'+- (Step 4), the certificate radius
  ~3t_n (kappa(c) in A Def 4.1 does NOT involve ||b/a||, so K_c is legitimate), the no-sign-change bookkeeping on F, the window and Far_n,
  the tail kink, and the constants of Steps 5-7.
  * Corollary 2.5 is correct: P1's explicit defect (P1 Thm 2.4) is recovered along engineered NA sequences, which fixes gaps G1-G3 of the
    P1 referee.
  * No counterexample is claimed, and none follows.
* Theorem 2 (Delta d > 0) needs a constant fix.
* Theorem 3 (Delta d < 0) has a genuine but repairable gap in its tuning step.
* The claimed obstruction for Delta d < 0 is over-stated. "The mismatch must sit in the base" (3.4) and "the convexity mechanism provably
  cannot replace (PC)" (4.7) are FALSE as stated. I prove (Lemma R below) that the convex block lemma, applied with the anchor
  y = w' + (w'-w)1_S, absorbs every status-preserving part of w' - w at second order. Only the status-changing coordinates and one scalar
  (C'-C)_+ cost at first order.
  * Consequence: N2's 3.7(a) (block-tame carrier block) becomes PROVED (given (TT)).
  * The generic Delta d < 0 obstruction is relocated. It is not "log(1/t) pinning conditions / quantitative tail independence". It is a
    margin-sparsity property of the carrier block at the perturbation scale.

## 1. Verdicts
| Claim | Verdict | Main issue |
|---|---|---|
| Algebra of exact two-piece representations (1.2) | correct | All of (a)-(f) re-derived; the block identity N = 1 + tau^2||h_perp||^2/(sqrt(Y^2+..)+Y) is exact. |
| Convex block lemma (1.3) | correct | Holds for ANY anchor y with N(y) <= 1 (or <= 1+delta, at extra cost s*delta). N2 only uses y = w; Lemma R uses a better y. |
| Kink class = exact resonance (1.6, 3.9) | correct with fixable gaps | omega'' = v''_Q - (c'/M) w 1_Q is in c_00 only if Q is finite (true in C_referee's configuration). (E4) must be assumed. See note (a) below. |
| Theorem 1 (Delta d = 0) | correct | Fully verified; numerics reproduced. |
| Corollary 2.5 (P1 example) | correct | g_{K1}: h <= c^2||U||^2/nu <= 9/32 and c^2/C_1 <= 3/4. Slab: true after possibly shrinking theta_*. |
| Several active blocks (2.6) | correct (SKETCH label conservative) | See note (b) below; upgradable to PROVED. |
| Wrong-sign c / opposite peaks (3.2(b), 3.3, 3.4) | correct with fixable gaps | 3.2(b) and 3.3 PROVED and sharp (numerics 0.999998). The inference "mismatch must be absorbed in the base" is FALSE (Lemma R). |
| Theorem 2 (Delta d > 0) | correct with fixable gaps | Lemma 1.3 gives the factor 1/(1-s); "s <= 1/2" can double H. Need T_0 rho Delta d <= eta_0/2; mubar_n must be enlarged. (TT) => (BR) is correct. |
| Theorem 3 (Delta d < 0) | correct with fixable gaps | IVT direction unjustified without (TT) (§2.1); constant in G_n; (PC) much stronger than needed (§3). |
| (PC) in block-tame robust carrier blocks (3.7(a)) | correct (upgradable to PROVED) | No perturbation lemma for J is needed (§3, Corollary R). |
| Existence of Delta d < 0 mates (3.8) | correct (SKETCH plausible) | Algebra re-derived; pi(xi) = sum_P lambda_k \|u_k(xi)\| > 0 automatically, so Delta d < 0 iff c kappa' > 0. These mates are in fact recovered (Corollary R + P1-type far tails). |
| Theorem 4 (conditional averaging) | correct | Re-derived. (HT) remains HEURISTIC; this repackages E's skeleton rather than advancing the approximate core. |
| Far rigidity compatible with Lemma B (4.5) | correct (SKETCH plausible) | P1's signature argument survives with delta_l -> delta_l eps_l. Blocks only source (S2). |
| Localization (5.2) | correct (conditional) | PROVED mod R1 (itself mod C Thm 6.2/Prop 6.5). Scope: C-tame approximants only. |

Notes to the table:
* (a) Kink class. The C_referee class is defined by WEIGHTED coefficients (Gamma_2 <= 1 < Gamma_w), so mates in it may have
  max(h, H) > 1. Hence "no new mechanism; the open part is exactly the Delta d < 0 problem" contradicts N2's own open item 7
  (second-order rebalancing at engineered approximants).
* (b) Several active blocks. The tuning moves finitely many fixed near free coordinates. These moves leave v(x'), E and the base
  untouched. ell_m(zhat) = 0, so the moves needed are -> 0. The system is fixed and invertible under the rank condition.

## 2. Gaps (with fixes)
### 2.1 Theorem 3: tuning direction (substantive, repairable)
* "Tune psi~ = v + |Delta d| Bx to 0 (as in 3.5)" needs psi~_n(0) <= 0. Here psi~_n(0) = psi_n(0) + |Delta d| Bx_n(0), with
  psi_n(0) in [-7D_n, -D_n].
* Nothing bounds Bx_n(0) by D_n/|Delta d|. Without (TT) the only devices that LOWER psi~ are the discrete far pulls, and each pull adds
  up to 2 sum_k lambda_k |w'(k)-w(k)| |u_k(j)| to Bx.
* Common opposite peaks (Lemma 3.3) contribute POSITIVELY to Bx: each such k adds lambda_k (M+M') |u_k(x')|.
* If psi~_n(0) > 0 and only upward devices exist, Delta d' - Delta d is not o(t_n). Side minus then carries
  (Delta d' - Delta d) R*w', a first-order kink.
* Fix: add (TT), or Bx_n(0) <= D_n/(2|Delta d|) (e.g. ||E'_n||_1 = o(t_n) at mu = 0). For P1-type T both hold (only v-multiples and
  allowedness-suppressed targets have mass on K' far out).
### 2.2 Theorem 3: constant in G_n
On Far_n the v-part already uses 2/3 of |a'_j| (|tau rho v_j| <= T_0 rho |v_j| <= (2/3)|a'_j|), and the anti-signed v_j meets the
sign -z_j of a'_j. So |tau rho E'_j| <= |a'_j|/2 can flip the sign. Define G_n with 4 T_0 rho |E'_j| > |a'_j|.
### 2.3 Theorem 2: constant
Add T_0 rho Delta d <= eta_0/2 to Step 0, so that 1/(1-s) <= 1 + eta_0. Also replace mubar_n by 4 nu (7 D_n + Delta d Bx_n(0))/c_+.
### 2.4 Over-statements
* 3.4 / 4.7 / 5.3(c): see §3.
* 3.9 / 5.3(e): the kink class with kappa_max > 1 is not covered.
* 3.6 Remark (2) explains correctly why (PC) is not automatic, but it does not show that the coarse non-peak shifts are an obstruction
  (they are not; §3).

## 3. New result: status-preserving absorption (Lemma R) and the Delta d < 0 case
Notation: block functionals w, w' (N = 1, M + C = 1 = M' + C'), gamma := C' - C, Delta := D(w'-w).
Definitions:
* For eps >= 0, S := {k : |2w'(k) - w(k)| <= M' + (M'-M)_+ + eps}. These are the coordinates where the reflection of w through w' does not
  overshoot. S contains common same-sign peaks, same-sign lost peaks, and non-peaks moved within their gap.
* Y := (w'-w)1_S, y := w' + Y, R_1 := <Dw', D(w'-w)1_{S^c}>.

**Lemma R. PROVED.** If C + 2 gamma > 0, then
  N(y) <= 1 + gamma_+ + eps + (||Delta||^2 + ||DY||^2 + 2|R_1|)/(2(C + 2gamma)).

*Proof.*
1. Sup part: ||y||_inf <= M' + (M'-M)_+ + eps by the definition of S.
2. Exact identity: ||Dy||^2 = C'^2 + 2<Dw',DY> + ||DY||^2, with <Dw',DY> = <Dw',Delta> - R_1 and
   <Dw',Delta> = (C'^2 - C^2 + ||Delta||^2)/2.
3. Hence ||Dy||^2 = (C+2gamma)^2 - 2gamma^2 + ||Delta||^2 + ||DY||^2 - 2R_1.
4. Use sqrt(A^2 + x) <= A + x_+/(2A), M' = 1 - C - gamma and (M'-M)_+ + gamma = gamma_+. QED.

Numerics:
* Exact J (bisection plus golden section), 300 random blocks: max violation 2.2e-16.
* The gamma_+ term is attained: ratio up to 1.02 when C' > C.
* The single violation in the large-perturbation run has C + 2gamma = -0.086 < 0, which is outside the hypothesis.
* Compare N2 3.2(b): the FULL reflection y = 2w' - w costs 1 + 2M at every opposite peak.

**Theorem 3* (Delta d < 0). PROVED given tuning.**
Hypotheses: as in N2 Thm 3 (F finite, one active block, theta = 0), with |Delta d'_n - Delta d| = o(t_n) (e.g. under (TT)), and
  (PC*)  (C'_n - C)_+ + ||D(w'_n - w)||^2 + sum_{k in S_n^c} lambda_k |w'_n(k) - w(k)| = o(t_n).
Conclusion: g is in Ls(f).

*Proof.*
1. Side minus, with s := tau rho Delta d > 0:
   * block W = w' + tau rho(omega- - d'(omega-)w') + sY = (1-s)[...] + s y (Lemma 1.3 with anchor y), so the extra block cost is
     s(N(y)-1) <= s(gamma_+ + o(t_n));
   * base b'- = b'_0 - v + (Delta d' - Delta d)R*w' + Delta d R*((w'-w)1_{S^c});
   * first-order term tau rho b'-(x') = -s Bx + s<(w'-w)1_{S^c}, R x'> <= s sum_{S^c} lambda_k|w'-w|;
   * kink <= 2s ||R*((w'-w)1_{S^c})||_1 + o(t_n)|tau|.
2. Everything else is as in Theorems 1 and 3. QED.

**Corollary R (N2 3.7(a) made rigorous).**
Hypotheses: Q_{m0} = {k_0}, (MS), no degenerate peaks, and (TT).
Conclusion: (PC*), and even N2's (PC), hold. So Delta d < 0 mates of this type are in Ls(f).

*Proof.*
1. Status changes need mu_k <= O(t_n) or mu_k <= 2||u_k 1_{(N'',inf)}||_1, so their lambda-mass is o(t_n): by (MS), and by choosing
   N''_n after t_n.
2. The tuning means rho'_0 = rho_0, where rho_k := zeta(k)/(Phi(k)|zeta|).
3. The exact identities C^2(1-rho_0^2) = (1-C)^2 A and C'^2(1-rho_0^2) = (1-C')^2 A - sum_L Phi^2 (M'^2 - w'(k)^2) hold, with
   A = sum_P Phi^2 and L the set of lost peaks; there are no new peaks, and w'(k_0) = C' rho'_0/Phi(k_0).
   Since x -> x^2(1-rho_0^2) - (1-x)^2 A is increasing, C' - C = o(t_n).
4. Hence w' - w = o(t_n) on k_0 and on common peaks.

For |Q| >= 2 finite, (PC*) needs ONE more scalar inequality, sum_Q rho'^2 <= sum_Q rho^2 + o(t_n). This is SKETCH: one extra tuning
variable is needed.

**Relocated open core for Delta d < 0.**
* Coarse non-peaks (Phi(k) gap(k) >> t_n) are absorbed by the block.
* What matters is the lambda-mass of carrier-block coordinates SCRAMBLED by a perturbation of size t_n: fine non-peaks with
  Phi(k) gap(k) <~ t_n that change status or sign, and near-threshold peaks.
* Under (MS) and (MS-Q), sum{lambda_k : k in Q_{m0}, Phi(k) gap(k) <= s} = o(s), Delta d < 0 costs one scalar. HEURISTIC beyond that:
  if non-peaks occupy a positive proportion of fine scales, a bounded number of scales just below t_n must be pinned.
* For Delta d >= 0 none of this matters: the anchor y = w absorbs everything, and the cost is only (BR).

## 4. Numerics
* N2's scripts re-run, outputs identical:
  * lemma32_check: 176 cases; 0.0119 and 0.999998.
  * thm1_check: worst excess between -1.1e-9 and -8.4e-9. Its small-|t| end is at SOCP tolerance (p* >= 1 forces
    p* - s(t) >= -5e-9 at t = 1e-4), so only moderate t is informative.
* Referee scripts N2ref_work/ytrick_*.py: Lemma R as above.

## 5. Recommendations
1. Add (TT), or a Bx_n(0) bound, to Theorem 3. Fix the G_n constant and the Theorem 2 constant.
2. Replace (PC) by (PC*). Restate 3.4 and 4.7: "the anchor y = w fails" is true, but "the convexity mechanism fails" is false.
3. Upgrade 3.7(a) to PROVED (Corollary R) and Remark 2.6 to PROVED. Rewrite 3.7(c) as the (MS-Q) / scrambling problem.
4. In 3.9, add (E4) and Q finite. List "kappa_max > 1, weighted <= 1" (second-order rebalancing) as a separate open item.
5. Next target: exact resonances whose carrier block has strict non-peaks at a positive proportion of fine scales (Delta d < 0), and
   approximate resonances (Theorem 4's (HT)).

## 6. Most valuable idea
Use the convex block lemma with a non-trivial anchor. Reflect the approximant's block functional through the target's only on
status-preserving coordinates: y = w' + (w'-w)1_S. This costs only (C'-C)_+ at first order (Lemma R). The "wrong-sign" Delta d < 0
obstruction then collapses to the lambda-mass of coordinates whose status the engineering perturbation changes at its own scale.
Combined with N2's Theorem 1 machinery (IVT-tuned mass, far sign-flipped contacts with negative masses), this gives the following:
every exact resonance with a single carrier non-peak is recovered whatever the sign of Delta d (under (TT) or P1-type far tails).
