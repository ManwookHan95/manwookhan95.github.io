# Referee report on P1 ("Is the defect empty? matching at scale, resonances, explicit nonempty defect")

Referee: Round 2, adversarial check of ctx/r2/P1_notes.md (and P1_part1-6). Setting as in P1: canonical base q, Martin's norm with a
FINITE block set I (p_N; Preprint B Remark martin-tail), imports A_notes Facts A-F, Lemmas 4.3/4.4/7.1/7.2, (T4) strict convexity of
p** (Preprint B Thm finite-blocks(b), valid for P1's T because it only uses density of block tails). Part files: P1_ref_part1-4.md.
Scripts: ctx/r2/refP1/ (model.py, t1_structure.py, t2_mates.py, t3_trunc.py, t4_wavg.py; numpy + cvxpy/Clarabel exact p* by SOCP).
Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.

## 0. Summary
* The central results are CORRECT: the construction of an admissible T (2.1), the non-attaining first row f with Q_1 = {2}, w_1(2) = 0
  and all other block coordinates peaks (2.2), the two-piece mates (2.3), Def(f) != empty relative to all certificate-type classes
  (2.4), the rigidity C(f) in E_u and the slab of mates (6.1-6.2), the exact-resonance proposition (4.1), the weighted averaging theorem
  (4.3-4.4), the dual route (5.1-5.3), and C-tame => C(f) in S(f) (3.8). I re-derived every step of these by hand.
* No counterexample to density is claimed, and none follows: the defect mates are recoverable along engineered sequences (6.3, SKETCH,
  checked; three fixable gaps). The question remains OPEN.
* Main corrections:
  (C1) Thm 3.7 / Cor 3.8 / (O1) ignore C_notes Thm 7.4 (transfer-peak rebalancing: every balanced finite certificate with
       Gamma_w = q_0 H_b + sum sigma_m H_m <= 1 is recovered) and C Prop 8.1 (Gamma_2 = Gamma_w at finite-Q, Dg-free, (MS) points). Since
       Hhat >= Gamma_w (proved below), P1's "second-order defect" {Hhat > 1} is mis-specified; relative to all Round-1 classes it is
       {Gamma_w > 1}, and it is EMPTY when there are no degenerate peaks. Combining P1 3.8 with C: every C-tame f without degenerate
       peaks lies in R (all mates recovered) [PROVED mod unrefereed C results]. P1's remark that finite models "suggest" a nonempty
       second-order defect points the wrong way (finite models lack transfer peaks; C Prop 8.2/Discussion 8.3).
  (C2) The meta-claim "Thm 2.4 shows density cannot be proved by intrinsic (sequence-independent) recovery" does not follow from 2.4
       (a mate outside cl Cert^sh could still be recovered along every sequence). I prove it (R3 below) for a mild modification of
       P1's T: along the canonical truncations f_n, C(f_n) is contained in a line converging to R u, so the defect mates are NOT
       recovered along (f_n). The tool is a linear obstruction AT THE APPROXIMANTS (R1): along C-tame NA approximants,
       Li C(f_n) is contained in Li S(f_n).
  (C3) 3.5(d)/3.6 ("matching at scale in its true form") are SKETCH, not PROVED: the level shift ell_m - M_m is O(|t|), not O(eps),
       so the sign claim for beyond-window coordinates fails for gaps <~ |t|, and M_{c_0} is not precisely defined. 3.3: near-contacts
       are not scale-free (room r_j costs r_j |tau B_j|); the "gap bounded below => depth <~ |t|" claim needs (K2), not (K3).
  (C4) 6.3 lacks the hypothesis g in C(f); the partial-pull coordinate has a first-order cost that must be put beyond the tail
       threshold; quantifier order should be stated. Its correction of A_referee §5.4 is VALID (and applies equally to E 1.4(i)).
  (C5) Over-generalizations in §0/§7.1: "(4.4) the mate is in cl Cert(f) unless the gaps are summable" is HEURISTIC in that generality.

## 1. Verdicts (claims as listed in the task)
| Claim | Verdict | Issues |
|---|---|---|
| Linear obstruction (1.2-1.3) | correct | Also covers C Thm 7.1/7.4 and E Thm 5.1 (all in S(f) or cl Cert(f)). |
| Admissible T (2.1) | correct | (T3) not stated but follows from (T-d); (T4) applies. |
| Two-piece mates (2.3) | correct | P1's numerics only test explicit-decomposition algebra with ad hoc block data; my exact-SOCP check in a consistent finite model confirms. |
| Nonempty defect (2.4) | correct with fixable gap | True relative to the listed classes; the "sequence-independent" meta-claim needs R3. |
| Single-scale bounds/capacities (3.1-3.3) | correct with fixable gaps | (B1)-(K3) PROVED; 3.3 qualitative statements partly inaccurate (near-contacts; K2 needed). |
| Transfer identity / sign opposition (3.4-3.6) | correct with fixable gaps | 3.4, 3.5(a)-(c) PROVED; 3.5(d), 3.6 SKETCH (level shift O(t)). |
| Exact defect at block-tame f (3.7) | correct with fixable gaps | Correct relative to P1's list only; second piece should be {Gamma_w > 1} (C Thm 7.4), empty without degenerate peaks (C Prop 8.1). |
| C-tame => no switching defect (3.8) | correct | Re-derived (a),(b) and C Thm 6.4/Prop 6.5; with C it yields f in R when Dg = empty. |
| Exact resonances (4.1) | correct | — |
| Sign rule, near-duplicates (4.2) | correct with fixable gap | Near-tautological; the §0/§7.1 extrapolation via 4.4 is HEURISTIC. |
| Weighted averaging (4.3-4.4) | correct | Bound chain checked numerically; mention the case s > r(c^0)/rho in 4.4. |
| Dual route (5.1-5.3) | correct | 5.4's description of minimizing families is HEURISTIC. |
| Fibre at the example (6.0-6.2) | correct | All six steps of 6.1 and the margins of 6.0 re-derived. |
| Engineered recovery (6.3, SKETCH) | correct with fixable gaps | Missing g in C(f); j* cost; quantifier order; can be sharpened. |

## 2. Verification notes (condensed; details in P1_ref_part1.md, part4.md)
2.1: (T-a) ||T|| = sup c_l = 1; (T-d) ||u_{n,m} - y^{(i(n,m))}|| -> 0 since rho_l, delta_l -> 0, n_l -> 1, and each i is allowed at all large l;
(T-b),(T-c): for s in S_{l'}, |Z(s)| >= c_{l'} delta_{l'} 2^{-s}(|x_{l'}|/n_{l'} - (8/3)||x||_inf 2^{-s}) (uses sum_{l>=L} c_l <= 2c_L, |y_l(s)| <= 1,
n_l >= 3/4, allowedness at L(s), and that pi and the special/first-coordinate vectors live on {1}, 1 notin J_0); (P1): kappa >= ||h||_1/(2(1+nu_1));
(P2) >= 7/9; (P3) non-exceptional |u(zhat)| >= 2 rho_l > pi, exceptional >= 31/33.
2.2: f(xi) = 1, p*(f) <= 1 (Fact A), uniqueness (T4); peaks: |zeta_m| <= q_0 m 2^{-m}, (1,m) peaks, C_m >= Phi_m(1)M_m, theta_m Phi_m(k) <= q_0 pi_{k,m}.
2.3: side +: ||v1_{K1}||_1 + <e,h_1> = beta (z = 1, v > 0 on K'); side -: the first-order bracket equals v(zhat) = c u(zhat) = 0; Hilbert bound
||xe+y|| <= x + <e,y> + ||y||^2/(2x) (from (<e,h> + ||h||^2/2)^2 >= 0); block N_1 = M_1 + sqrt(C_1^2 + s^2c^2) (w_1(2) = 0, Phi_1(2)/lambda_0 = 1).
2.4: S(f) = R u since F = {1}, zhat_1 = 1/alpha != 0, Q_1 = {2}, y_{2,1} = lambda_0 u (w_1(2) = 0); g_{K1} = mu u forces c 1_{K1} = mu on K'.
3.1: budget identity + exact excess formulas; |alpha_{m,k}| = lambda_k mu_k/|zeta_m| re-derived. 3.4: average of the +-t decompositions.
3.7: injectivity via Y cap c_00 = {0}; theta bounded (theta_m <= 1/2, sum theta_m|zeta_m| >= -q_0/2, I finite); H^sh coercive in theta, so
Hhat is a minimum. (kappa_q is 2-Lipschitz, not 1-Lipschitz: harmless.)
3.8: (a) nu = -z_j e_j + nu_J, xi + s nu moves the contact inward, base excess 0, blocks o(s^2) by Lemma 5.2 + (MS); (b) degenerate peak
moved outward costs 0. Both re-derived; C Thm 6.4 and Prop 6.5/Lemma 6.6 re-checked.
4.1: q*(a+sD) >= 1 + sD(zhat) + s kappa(D) (s > 0), N_m(w_m - s Omega_m) >= 1 - s<Omega_m,zeta_m>/|zeta_m|; weighted sum and D(xi) = <Omega_D, L**xi>.
4.3: chain re-derived: (1+rho^2)/4 + (1-rho^2)/12 = (2+rho^2)/6, and s^2(1-rho^2)/6 >= s^4/8 for s^2 <= 1 - rho^2.
5.1: Mazur (Gateaux differentiability of h_B on a dense G_delta), subdifferential = exposed face. 5.2: one-scale minimum sqrt(P^2 - F^2).
6.1: (1) peaks carry <= C t^{1/3} (split at Phi = t^{4/3}, margins >= q_0 min(1/4, 2 sqrt Phi)); (2) |t<Omega_m,zeta_m>| <= eps from the
first-order balance g(xi) = 0, hence |ell_m - M_m| <= C t^{4/3} (only possible because the unique non-peak has zeta_1(2) = 0); (3) mu_t^2 <= s/|zeta_1|
(D_1 e_2 orthogonal to D_1 w_1); (4)-(6) free coordinates and paid contact usage from (B1). 6.2: explicit side decompositions with mu+ = inf theta,
mu- = sup theta.

## 3. Correction C1 in detail (second-order defect)
Claim (PROVED, elementary): for every shifted certificate, Hhat(c) >= Gamma_w(g_c) := q_0 h(b) + sum_m |zeta_m| H_m(omega_m).
Proof: if L := H^sh(c,theta), then theta_m <= (L - H_m)/2 for all m, and L >= h(b) - 2 sum theta_m|zeta_m|/q_0 + 2 kappa_q >= h(b) - sum (L - H_m)|zeta_m|/q_0;
multiply by q_0 and use q_0 + sum|zeta_m| = 1: L >= Gamma_w + 2 q_0 kappa_q(v_theta) >= Gamma_w. (Pure block: Hhat = H r_2/(1+r_2) >= (1-q_0)H with
equality iff kappa_q(-R*w) = 0.)
C Thm 7.4 (transfer peak: a robust deep peak k_* with u_{k_*} ~ (tau_* + delta_0 q*(tau_*) a)/q*(.), lowered by O(t^2); its R*-image turns the
uniform lowering pi^ = R*(sign w 1_{Lset}) into a multiple of a) recovers every balanced finite certificate with Gamma_w <= 1; C Prop 8.1 gives
Gamma_2 = Gamma_w when Q_m finite, Dg empty, (MS). Hence:
 * Thm 3.7 holds relative to P1's list; relative to all Round-1 classes, Def(f) = (C(f) \ S(f)) u {g_c in C(f) : Gamma_w(c) > 1} (the second set is
   closed in the finite-dimensional S(f)), and the second set is EMPTY under (MS) when Dg is empty.
 * Theorem (P1 3.8 + C Prop 8.1 + C Thm 7.4; PROVED modulo the unrefereed C results): if a in c_00, K finite, every Q_m finite, no degenerate peaks
   and (MS), then f is in R. (C Thm 8.4 needed K = empty; P1 3.8(a) removes this.)
 * (O1) should become: is there f with degenerate peaks, or with infinitely many non-peaks, and g in C(f) cap S(f) with Gamma_w(g) > 1? OPEN.

## 4. New results (full proofs; correction C2)
R1 (Lemma, linear obstruction at the approximants; PROVED mod C Thm 6.2, Prop 6.5). If f_n -> f in S_{p*} and each f_n is a C-tame NA point
(Qbar_{n,m} finite, (MS) at x'_n), then Li C(f_n) is contained in Li S(f_n).
Proof: C Thm 6.2 gives C(f_n) in W(x'_n): directions v supported on the free coordinates J'_n and annihilated by the finitely many functionals
u_{k,m}|_{J'} (k in Qbar') and R_m*w'_m|_{J'} have p(x'_n + tv) - 1 = o(t^2) (base exactly flat inside the room, blocks = peak overshoots, o(t^2) by
(MS)), so every mate kills them, and a functional vanishing on a finite intersection of kernels is a combination of them. P1 3.8(a) at x'_n
kills contact components; C Lemma 6.6 (rebalancing direction lambda x' + nu_J) gives c_m = -d_m and b(x'_n) = 0. So C(f_n) in S(f_n). QED.
R2 (modified T; PROVED). In P1 2.1 fix N_n increasing, z^{(n)} := e_1 + 1_{K' cap [1,N_n]}, x^{(n)} := z^{(n)} + U e. For a non-special, non-exceptional l with
target y^{(i)}, let Lambda(i) := {n : supp y^{(i)} meets K' cap (N_n, inf)} (finite) and choose pi_l := s_l alpha e_1* with |s_l| <= 3 rho_l(2|Lambda(i)|+3)
and |(y^{(i)} + pi_l)(x)| >= 3 rho_l for x in {zhat} u {x^{(n)}: n in Lambda(i)} (possible: (alpha e_1*)(x) = 1 for all these x; the forbidden s form
|Lambda(i)|+1 intervals of length 6 rho_l). Add to allowedness: rho_l(2|Lambda(i)|+3) <= min(rho_l^{1/2}, 1/(26(1+||U||))). Then (T-a)-(T-d), (P1)-(P3)
hold as before (pi_l still lives on {1}), and (P4): |u_{k,m}(x^{(n)})| >= 2 rho_l for all n and all (k,m) != (2,1), k >= 2 (if n notin Lambda(i),
x^{(n)} - zhat = -1_{K' cap (N_n,inf)} is invisible to y^{(i)}, pi_l and h_l); u_{1,m}(x^{(n)}) = u_{1,m}(zhat); exceptional vectors unchanged.
R3 (Proposition; PROVED mod R1's imports). With T as in R2, f as in P1 2.2 and f_n := grad p(x^{(n)}) (NA):
(a) f_n -> f; (b) for large n, f_n is C-tame, Q_{n,1} = {2}, Q_{n,m} = empty (m != 1), no degenerate peaks; (c) C(f_n) is contained in R y^{(n)},
y^{(n)} = lambda_0 u - (Phi_1(2)^2 w^{(n)}_1(2)/C^{(n)}_1) R_1*w^{(n)}_1 -> lambda_0 u; (d) Li C(f_n) is contained in R u, so rho g_{K1} notin Li C(f_n) for
empty != K1 != K' and every rho in (0,1].
Proof. (a) a(x^{(n)}) = 1, x^{(n)} in B_q, so grad q(x^{(n)}) = a; x^{(n)} -> zhat weak*, L compact, J_V norm-to-weak* continuous, L* weak*-to-norm.
(b) As in P1 2.2(b) with (P2),(P4): (1,m) peaks, theta'_m Phi_m(k) <= q'_0 pi_{k,m}, every other (k,m) != (2,1) a peak with margin
mu' >= q'_0 rho_l >= q'_0 sqrt(2 Phi_m(k)) (non-exceptional), >= q'_0/4 otherwise; (MS): sum_{mu' < s} Phi <= s^2/q'_0^2; u(x^{(n)}) = -sum_{K'>N_n} u_j -> 0
while theta'_1 Phi_1(2) -> theta_1 Phi_1(2) > 0, so (2,1) is a strict non-peak for large n. (c) R1 and S(f_n) = R y^{(n)} (F = {1}, xhat_n(1) != 0).
(d) gamma_n y^{(n)} -> g forces gamma_n bounded. QED.
Meaning: for this T the set of mates recovered along EVERY sequence is contained in R u = the certificate line; universal ("intrinsic")
recovery fails exactly as P1 asserted, and any recovery of the switching mates must put base mass on the contact windows (as 6.3 does;
consistent with R1: there g' lies in S(f')). For P1's unmodified T the same is very likely true but needs control of the infinitely many
targets meeting K' far out.

## 5. Numerics (independent; finite model of the example, exact p* by SOCP)
Consistent finite model (U diagonal, 10 contacts, 14 free coordinates, 7 block coordinates, special u with u(zhat) = 0): forced data reproduce
2.2 (all block coordinates peaks except the special one, w = 0 there; p*(f) = 1 = f(xi) to 1e-9). Two-piece mates (c = 0.05, 0.2, random K1):
max_t [p*(f+tg) - s(t)] <= -3.7e-9 on 32 values |t| in [1e-4, 10]. Free-coordinate direction: (p*-1)/|t| ~ 0.95-0.99 on both sides (6.1 step 5).
Single contact direction: O(t^2) on both sides at f, but at the canonical truncation f_N the side t < 0 becomes first order ((p*-1)/|t| ~ 0.045-0.07
for N = 8, ~1.9 for N = 5); the discretized support max{g(x_*) : g in C(f_N)} drops from 0.20-0.40 to 0.04-0.06 (N = 8) and <= 3e-3 (N = 5), the
remainder being the line R y^{(N)} (w^{(N)}(2) != 0 in a finite model) and grid effects — consistent with R3. Weighted averaging bound chain: no
violation in 3000 random parameter sets (cancellation-free evaluation).

## 6. Recommendations
1. Restate 3.7/(O1) with Gamma_w and cite C Thm 7.4/Prop 8.1; state the positive theorem "C-tame without degenerate peaks => f in R".
2. Replace the meta-claim in §0/§7.3 by R1-R3 (or prove R3 for the unmodified T).
3. Downgrade 3.5(d), 3.6 to SKETCH; fix 3.3's wording.
4. For (O4) (f in R for the example): sharpen 6.3 (side + may use any mu <= inf theta, side - any mu >= sup theta), insert C's transfer peaks in the
   engineered approximants to replace max by mass-weighted coefficients, and prove a one-sided version of C Prop 8.1 (HEURISTIC route).
5. The general lesson (R1): along tame NA approximants recovery is a LINEAR-ALGEBRA design problem — g must lie in Li S(f_n); a density proof
   must build approximants whose base supports (masses on contact windows), exact carriers and non-peak sets make S(f_n) approximate the mate,
   with the second-order condition Gamma_w <= 1 carried along.

## 7. Most valuable idea
The certificate span S(f) as a LINEAR obstruction, used on both ends: at f it detects the defect (P1 Thm 2.4: one exact resonance — a block
vector supported on supp a plus an infinite contact set with u(zhat) = 0 — creates an infinite-dimensional family of switching mates while
all certificate-type mates lie on one line), and at C-tame NA approximants it is a necessary condition for recovery (R1: Li C(f_n) in
Li S(f_n)). Together they show that density must be proved by approximants engineered so that their finite-dimensional certificate spans
converge to the fibre (window masses on contacts, exact carriers, far negative masses), with C's transfer peaks handling the second order.
