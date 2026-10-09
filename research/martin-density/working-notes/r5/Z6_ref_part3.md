# Z6 referee, part 3: candidate (6.1), modules (6.2), module sums (6.3(iii)), candidate under D'' (6.3(ii)), numerics

## Numerical checks (scripts in r5/Z6_ref_work/)
check_farkas_shift.py:
 (1) Proposition P: 1232 random rigid instances (cones with sign rows, contact rows, room rows, anti-peak rows and two
     d-rows), certificate of least sup-norm by LP (HiGHS), 200 random tau each: max(lhs - rhs) = -3.7e-5 < 0. Signs OK.
 (2) Shift trick (Theorem C step 5): 2000 random blocks with a near-threshold coordinate (gap 1e-8..1e-1), data with
     P <= a, Q >= -a - e, Q - P in [0, A_2/t], after the shift: max(||W||_inf - (1 - r d) M) = 0.0 and
     max(N(W) - 1 - (r^2/2) H(omega)(1 + 2|r d| M/C)) = 1.9e-16 on both sides, r = (0.1, 0.5, 1) c_flat t.
Re-run of Z6's R4 (scan_cap.py; outputs rerun_R4_k01.txt, rerun_R4_k098.txt): reproduced exactly
 (kappa = 0.1, c = 0.04: forced switching 0 at all 14 scales under the true cap s(t); kappa = 0.98, c = 0.085: forced
 switching/t = 23.4 at t = 3e-3 decreasing to 0 at t >= 0.23).  Observation: for kappa = 0.98 the forced switching itself
 is ~0.07 (nearly constant) on [3e-3, 1e-2], i.e. ~0.8 t/q (1/q = 29.5): the 2.4 bound O(t)/|q| is essentially attained
 in this model -- supports "2.4 is sharp" (design-scale constant genuinely needed for near-threshold same-sign carriers).

## 6.1 Candidate data. SKETCH: plausible, with an inconsistency.
 - With F = {j0} and z ≡ 1 off F the forced data (a, z) are completely determined (a = ± e*_{j0}/q*(e*_{j0})); there is NO
   free parameter, so "existence by a nested Baire/intermediate-value construction" cannot be run at F = {j0}: whether this
   single point has (C2)/(C3) is decided by the design, generically not.  The construction needs |F| >= 2 (parameters
   a in S_{q*} ∩ l_1(F) with fixed signs, dimension |F| - 1, e(a) = U*a/||U*a|| non-constant), as the text itself hints
   ("or on a and further coordinates added to F").  With |F| >= 2: each requirement (near-threshold, weak margin, nearly
   neutral, u_l(xi) > 0) is an open condition in a, a target crossing zero inside every open set of parameters exists by
   density and the intermediate value theorem, and nested closed balls give a point with infinitely many of each:
   plausible SKETCH (also: the other carriers must avoid becoming q < 0 strict non-peaks -- a countable family of
   closed nowhere dense conditions, avoidable by interleaving; not mentioned).
 - (C2) says "failure of (MS) and of (W_U)"; but K_P in (W_U) counts only compensated blocks and the candidate block is
   uncompensated, so (C2) does NOT violate (W_U) (as 6.1 "Position" and 6.3(ii) correctly say).  Typo-level.
 - (C4) "forced by density": correct (every target recurs and is allowed at all large l; dense targets must meet S_l).
 - "Position": correct given the data.

## 6.2 Single-module mates. SKETCH: plausible; one omitted step.
 + side beyond the radius gamma lambda/(2c): f + r g_c = (a + r c u_l) + R*((1 - r c q) w); levels
   1 + r c q sigma/q0 + O(r^2 c^2) (2.1: u_l(zhat) = q sigma/q0) and 1 - r c q: OK for r >= 4 c q sigma/q0; overlap with the
   radius iff c^2 <= gamma lambda q0/(8 q sigma): OK.
 - side beyond (M + |w|) lambda/(2c): the base decomposition has levels 1 - |r| c q sigma/q0 + 2|r| c m_u (base) and
   1 + |r| c q (block) -- UNBALANCED; the budget identity gives weighted excess 2 q0 |r| c m_u + O(r^2), and a rebalancing
   (Prop. rebalancing with transfer vectors) is needed to equalize the levels; then |r| >= 8 c m_u q0-type thresholds follow.
   Not mentioned; routine.  Membership in Cert(f) and recovery (Theorem transfer) then follow.
 Heuristic consistency check (referee): for a nearly neutral module (gap ~ M) the switching band is [M lambda/c, c m_u],
 which is EMPTY under the validity bound c^2 <= (M + |w|) lambda/(16 m_u); this explains R4 (kappa = 0.1: no forced
 switching) and is the single-module case of Conjecture G.

## 6.3(iii) Module sums. SKETCH: plausible ONLY in the non-switching regime it states.
 With c_i^2 <= eps gamma_i lambda_i, a module dropped at scale t (radius gamma_i lambda_i/c_i < c0 t) has c_i < eps c0 t, so the
 truncation error is O(t) with a bounded constant and the averaging theorem applies; but these are modules far below
 the validity limit, which (Section 7) do not switch.  The switching module sums (near the validity limit) are not
 covered; at a band module the truncation constant is ~ 1/q_i ~ 1/Phi_i, unbounded over i.  Z6 labels those HEURISTIC:
 consistent.  The constant "K ~ 1/(gamma_i delta°_i)" is unexplained (harmless).

## 6.3(ii) Candidate under D''. CORRECT WITH A FIXABLE GAP.
 Uncompensated: yes (all bad q != 0 strict non-peaks have u_l(xi) > 0; positive peaks have q > 0; anti-sign peaks are not
 in Sigma).  (E1),(E2) vacuous, (E4) void, (E5) automatic (2.2: positive non-degenerate peak + any negative peak).
 But with (W_U) as written, Lambda*_f(l) ≍ Lambda°(l) at maximal contact and the squared bracket requires Lambda°(l) =
 o(l 2^{l^3}) along a subsequence, a design condition not imposed.  With the corrected Theorem U' (Lambda*_good = 1 at
 maximal contact; linear bookkeeping) the hypothesis is exactly liminf K_nn(l)/(l 2^{l^3} Lambda°(l)) = 0, i.e. the
 candidate is recovered for D''' unless the relative d-coefficients |q_l|/Phi_l of its nearly neutral swallowed
 non-peaks are <= C/(l 2^{l^3} Lambda°(l)) for ALL large l (sup over l' <= l).  So the claim holds after the fix.
 6.3(i) "[PROVED: the hypotheses fail]": correct for Theorems S, C ((H2), (B_fin)/(B_res), (H1), (Cmp) fail); for Theorem
 Bstar "fail" means "window pinning is not established", not that the mates are not window-pinned (no lower bound on the
 switching of a specific mate is proved).  Overstatement, harmless.
