# P2 referee — part 3: further observations, overstatements, and the overall picture

## 3.1 Lemma 3.2(b) / "carriers pushed beyond their gap at fixed scales" is superfluous (observation, PROVED).
Lemma 1.4 (assembly) works with ANY fixed T_0 in (0, sqrt(3 delta)]: the slack covers |tau| >= T_0 as soon as p*(f'-f) <= (1-rho^2)T_0^2/6
and p*(g' - rho g) <= (1-rho^2)T_0/6, which holds at late stages because T_0 does not depend on s_1. Hence in Thm 3.5 one may take
tau_1 <= s_gamma; then Lemma 3.2(a) alone suffices and the box is never left. "Pushed beyond the gap at fixed scales" is therefore
covered trivially (by the slack), and the only genuinely hard "pushed beyond gap" situations are scale-dependent ones (gap or
coefficient depending on t), which P2x correctly puts in the residual class. Not an error, but the summary should not list it as an
achievement of the transfer regime.

## 3.2 Prop 2.6(b) needs relative compactness in l_1, not boundedness (minor gap).
The U-part of the first-order coefficient is controlled for any BOUNDED family (U* compact), as stated. The z-part beyond the window,
(B_tau - b_0)(z' - z) restricted to (N, inf), is <= ||(B_tau - b_0) 1_(N,inf)||_1 and must be <= eps_0 s_1 UNIFORMLY in tau; this needs uniformly
small tails, i.e. relative norm compactness of {B_tau} in l_1 (or an explicit tail hypothesis). A bounded family of l_1 vectors can have
non-uniform tails (e.g. B_tau = e_{n(tau)}*-type pieces on far contacts). Replace "any bounded family" by "any relatively compact family".

## 3.3 Overstatements to correct in the summary of P2x.
(O1) "Recovery holds iff (PIN)" (4.1) — only "if", and "only if" within the transfer scheme (part 2, 2.2(b)).
(O2) "fatal, for every mass/conversion-based scheme, for scale-dependent block carriers" (Sect. 0) / 5.4 "PROVED": 5.4(a) and (d) are
     proved; 5.4(b),(c) compute the cost of two specific transfer options (same coefficient / re-tuned coefficient). The phrase "either
     way the error is ~ lambda_k Delta_k/Phi_k" is inaccurate for the first option (its error in N_m is |w'(k) - w(k)| ~ Delta_k/Phi_k, larger by
     1/lambda_k); the conclusion uses the better second option. Pinning/retuning schemes ((QI)) are not excluded, as P2x itself says at the
     end of 5.4. Correct label: (a),(d) PROVED; (b),(c) SKETCH computations; "fatal for every scheme" HEURISTIC.
(O3) "A_referee 5.4 made rigorous (PROVED)" — true for one active block (any split) and for several blocks under (S) or (TC); the
     multi-block d-neutral case without (S)/(TC) remains open (part 2, 2.5).
(O4) 4.2 subset-sum parenthetical is false in general (Cantor-type reservoirs); repaired by the continuous raising move (part 2, 2.3).
(O5) 4.3(i) estimate not uniform on [s_1, tau_1] as written; correct argument by splitting the range (part 2, 2.6).

## 3.4 Positive additions found during refereeing.
(P1) The "Lipschitz step" of the pinning sketch (4.1(d)) is supplied by the replication identity of the other instance (P2A Lemma 4.1),
     extended to approximately tuned ratios r'(k) = r(k)(1 + O(s_1^2)) — part 2, 2.2(c). No non-degeneracy of the (M, theta) system is needed.
(P2) Theorem 3.5 and P2A Thm 2.1 do not use finiteness of I except through (T4)/Fact E; for I = N, (T4) is Martin's Proposition 3 (X**
     strictly convex) and only the finitely many active blocks are touched (inactive blocks contribute N_m(w'_m) = 1 exactly; the Bregman
     tail T_N = 2 sum_{k,m} lambda_{k,m}||u_{k,m}1_(N,inf)||_1 is finite since sum_m m 2^{-m} < inf). So both theorems should hold for p itself
     (SKETCH; imports of A for I = N to be re-read), making Remark martin-tail unnecessary for this class.
(P3) For two-piece data with Delta d_m >= 0 and (TC), P2x Thm 3.5 strictly improves P2A 3.3/3.4 (which puts the garbage
     E = -sum Delta d_m R_m*(w'_m - w_m) in the base and therefore needs ||E||_1 <= eps_0 s_1, i.e. pinning and block-tameness): the convexity
     placement needs no tameness, no margins, no rates.
(P4) Necessity of Delta d >= 0 within the "fixed carriers + block-functional multiples" family: any anchor wtilde with Omega'- containing
     c(w' - wtilde) must be the extrapolation wtilde = w' + (|Delta d|/c)(w' - w) when Delta d < 0, and N(wtilde) >= 1 + 2M|Delta d|/c at common
     opposite peaks (part 2, 2.2(a)). So Delta d < 0 needs genuinely new ideas (pinning or other decompositions).

## 3.5 What the P2 results do and do not say about the density problem.
* No counterexample is claimed; none of the obstructions is an obstruction to RECOVERY (only to methods). Agreed.
* New rigorous coverage: (i) d-neutral two-piece switching mates, one block, any contact split, no (TC) (P2A Thm 2.1) — this includes
  all explicit defect mates of P1 (exact resonance), which are therefore NOT counterexamples; (ii) two-piece switching mates with
  Delta d_m >= 0 in all blocks under (TC), several blocks, carriers fixed (P2x Thm 3.5).
* Residual (my reading, agreeing with P2x 5.6 / P2A 4.6): non-neutral data with Delta d < 0 at blocks with infinitely many strict
  non-peaks; multi-block data where neither (S) nor (TC) holds and pulls interact with the Bregman term; scale-dependent switching
  (one-sided carriers of depth ~ t). Density for p_N remains OPEN.

## 3.6 Correction to 3.4(P2).
Martin's Proposition 3 (X** strictly convex) is for HIS base norm (DGS smoothing |||.|||), not for the canonical base q used here.
For the canonical base with I = N, (T4) is the unavailable [Recovery] result. So: Thm 3.5 / P2A Thm 2.1 extend to I = N GIVEN (T4) for
I = N (expected to follow by adapting Martin's proof of Prop 3, not checked). Until then the finite-I setting (p_N) + Remark martin-tail
(imported from Preprint B, stated tersely there) is the honest setting.

## 3.7 Structure of (TC) (observation).
For free coordinates j, sum_m V_m(j) = v(j) = 0 (v lives on F u K), so the (M1) effects lie in H_0 = {sum y_m = 0}: free moves alone can
never correct the "total" direction (1,...,1); that direction must come from (M2)/(M3) (two-sided at F, one-sided at contacts) — or from
pulls (P2A). So (TC) = [(M1) span H_0 modulo (M2)/(M3)] + [two-sided control of the total direction]; P2A's (S) is the first half,
raising+pulls the second. The uncovered multi-block case is exactly "(M1) does not span H_0 and (M2)/(M3) do not fill the gap".
