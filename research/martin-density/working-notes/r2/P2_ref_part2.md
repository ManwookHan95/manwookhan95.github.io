# P2 referee — part 2: claims 6-10 (Delta d < 0, far pulls, A_referee 5.4, extensions, implant gap) + numerics

## 2.1 Numerics (scripts in ctx/r2/P2ref_work/; J computed by the clip reduction, certified against the SOCP primal)
* t1_bregman.py (one block, n = 40, Phi_k ~ 2^{-k}, 5 off-peak coordinates; random and ADVERSARIAL sign-aligned perturbations
  |u_k(y') - u_k(y)| <= A): Bregman identity holds to 1e-9 in all runs; max e/A = 1.1e-2, 4.4e-3, 2.2e-3, 6.0e-4, 2.1e-4, 7.4e-5 for
  A = 1e-2 ... 3e-5 (e = O(A^2)), while sum lambda|w'-w|/A = 0.5 ... 1.6 (Theta(A)). Confirms P2x 2.3 and its Remark.
* t2_convexity.py (block with two off-peak carriers and one far COMMON OPPOSITE peak of w, w'): for W = w' + s(omega - d'w') + s c (w' - w),
  s < 0: c = +0.5 gives excess/s^2 = 0.49 (second order, Step 5 of Thm 3.5); c = -0.5 gives excess/|s c| = 1.544 = 2M to 3 digits
  (first-order excess), exactly as in P2x 4.1(a).

## 2.2 Delta d_m < 0 (P2x 4.1). VERDICT: failure statement PROVED; "recovery iff (PIN)" OVERSTATED; pinning sketch fixable.
(a) Common opposite peaks exist at every NA approximant f' of a non-attaining f (in every block): u_{k,m} close (for large k) to
    phi in S_Y with phi(zhat) > 0 > phi(xhat'); exists since zhat (not in c_0) and xhat' (in c_0) are linearly independent and Y is
    norm dense in l_1; for large k both |u_k(zhat)| >= theta Phi_k and |u_k(xhat')| >= theta' Phi_k. Then for W = w' + s(omega - d'w') + s'(w - w')
    with s' < 0: |W(k)| = (1 - s d')M' + |s'|(M + M') and ||DW|| >= <DW, Dw'>/C' = C' + s d'M' + s'(<Dw,Dw'>/C' - C'), so
    N(W) >= 1 + |s'|(M + M') - |s'|(C' - <Dw,Dw'>/C') = 1 + 2M|s'| - o(|s'|). Re-derived and confirmed numerically.
    I also checked that NO anchor rescues the convexity trick: requiring Omega'- - Omega'+ = omega_Delta - Delta d w with side + used
    two-sidedly (no (w'-w)-term there) forces Omega'- to contain c(w' - wtilde) with wtilde = w' + (|Delta d|/c)(w' - w) (an extrapolation
    beyond w' away from w), and N(wtilde) >= 1 + 2M|Delta d|/c by the same opposite-peak computation; using side - two-sidedly instead
    gives the same sign condition. So within "fixed carriers + multiples of block functionals", Delta d >= 0 is necessary.
(b) "Recovery holds iff (PIN)": only the "if" direction is (sketch-)proved; "only if" holds for THIS scheme (fixed carriers, transfer of
    the given two-piece data, mismatch in the base) — not for recovery of the mate. A mate with Delta d < 0 for one choice of two-piece
    data may have other data, other decompositions at f', or be recovered by mechanisms not of transfer type. Must be stated as
    "within the transfer scheme".
(c) Pinning sketch 4.1(d): the converse-of-Fact-C step is correct (re-derived). The "missing Lipschitz step" is in fact supplied by the
    OTHER instance's replication identity (P2_notes 4.1 = P2A Lemma 4.1), slightly generalised: with W_off = tuned non-peaks in [1,K],
    W_P = robust peaks in [1,K], Ch subset of (K,inf), and r'(k) = r(k)(1 + O(s_1^2)) on W_off (because |zeta'| = |zeta^#| + O(||R x' - zeta^#||_1)
    and |zeta^#| = c|zeta| by the converse of Fact C), G(C') - G(C) = sum_Ch Phi^2(w'^2 - w^2) + C'^2 sum_{W_off} Phi^2 (r'^2 - r^2), with
    G(c) = c^2(1 - rho_W) - (1-c)^2 S_P strictly increasing (G' >= 2 min(C,C')(1 - rho_W) > 0, 1 - rho_W >= sum_P Phi^2 M^2/C^2 > 0).
    Hence |C' - C| = O(sum_{k>K} Phi_k^2 + s_1^2) and ||R*(w' - w)||_1 = O(s_1^2) + 2 sum_{k>K} lambda_k = O(s_1^2): (PIN) holds, no
    non-degeneracy of the 2x2 system is needed. Remaining genuine hypotheses: Q_m finite, margins >= C s_1 on all peaks k <= K(s_1) along a
    sequence s_1 -> 0 (or margin sparsity sum_{mu_k < s} lambda_k = o(s), as in P2A (MS)), and a (TC)-type spanning condition for the
    |Q_m| + 1 linear conditions. The residual Delta d'_m - Delta d_m = O(s_1^2) is then absorbed by "approximate tuning suffices" (2.3).
    Status after this fix: SKETCH with all estimates available (I would accept it as PROVED once written with the uniform IFT/Brouwer step).
(d) Infinitely many strict non-peaks: OPEN — agreed.

## 2.3 Failure of (TC) / far pulls (P2x 4.2). VERDICT: correct_with_fixable_gaps (SKETCH as labelled).
* "Approximate tuning to precision c eps_0 s_1 suffices": correct. With Delta d'_m != Delta d_m and Omega'-_m as in Thm 3.5, b'+ - b'- = v +
  sum_m (Delta d_m - Delta d'_m) R_m* w'_m; the extra side-minus base term y has first-order cost <= |sigma|(|y(xhat')| + 2||y||_1) <=
  C|sigma| max_m|Delta d_m - Delta d'_m| <= C c eps_0 s_1 |sigma| <= 2 C c eps_0 sigma^2 on |sigma| >= s_1/2; side + (which defines g') is untouched.
* FALSE as stated: "every value in [0, sum] is within the last increment of a finite subset sum" of the pull increments 2|V(j)|. If the
  increments are super-decreasing (e.g. |V(j)| ~ 3^{-j} on K), the subset sums form a Cantor set whose gaps are comparable to the
  target; the greedy error is < the increment at the LAST SKIP, which need not be small. Requiring all increments beyond some N' to be
  <= c eps_0 s_1 while the reservoir beyond N' still exceeds the O(s_1) target fails for geometric decay with ratio < 1/2.
  Fixes: (i) finish with a CONTINUOUS one-sided move (the raising coordinate j_+ of P2A Thm 2.1, which exists by the sign identity) and
  the intermediate value theorem — exact tuning, no subset sums; or (ii) choose s_1 along a sequence for which the target lies on the
  closure of the subset sums. Fix (i) is what P2A does; with it the claim stands.
* "Delta d = 0, one block: PROVED by the other instance": I re-checked P2A Thm 2.1 line by line (see 2.4). Agreed.
* "Delta d > 0 with pulls needs a far-tail comparison": correct diagnosis. With pulls, N must precede s_1 (reservoir), so T_N <= s_1^2 is
  lost and the Far flips enter the Bregman pairing through sum_k lambda_k |w'(k) - w(k)| ||u_k 1_Far||_1, not controlled by Lemma B. OPEN/T-dependent.
  Small addition: for ONE block the masses push Gfun in the direction of the mass effects; pulls are needed exactly when Gfun(0) has the
  sign that no available (M2)/(M3) move can correct.

## 2.4 Other instance's Theorem 2.1 (d-neutral, pulls) — re-checked (needed for claims 7, 8). VERDICT: PROVED.
Checked: raising coordinate (P_{e-perp}U*v != 0 since v in Y\{0}, Y cap c_00 = {0}, U* injective; sign identity
sum_F v_j<PU*v,U*e_j*> + sum_K |v_j|<PU*v, z_j U*e_j*> = ||PU*v||^2 > 0); v(z'-z) = -2V_Far - V_{>N''}; |<U*v, e(a''(0)) - e>| <= A_0 s_1 + V_Far/2
(uses 16 rho T_0 ||U|| ||U*v|| <= nu); Psi(0) <= -V_Far; IVT with derivative >= gamma_+/2 on ||a''-a||_1 <= r_+; p-moves at free j_i do not
change v(xhat') or e'; d'^+ = d'^- from (R_m* omega_Delta)(x') = v_m(x') = 0 (Fact C off-peak); B^+- = B^theta +- (theta v, -(1-theta)v);
far coordinates: z'_j = -z_j = sign a'_j and |a'_j| >= 2 rho T_0|v_j| >= 2|tau rho beta^sigma_j| (no flip); contacts in (N,N''] \ Far keep
z'_j = z_j and are z-signed on the designated side; kink only beyond N'' (<= eps_0 s_1 |tau|); theta-side has zero kink. Constants OK.
Hidden hypothesis: the block parts must stay inside their boxes for |tau| <= T_0 (finitely supported off-peak carriers, T_0 <= r_sigma/(2 rho)),
i.e. Thm 2.1 does not cover carriers "pushed beyond their gap"; P2x Thm 3.5 does (Lemma 3.2(b)).

## 2.5 A_referee 5.4 "made rigorous" (P2x 7(a), table row 15). VERDICT: correct_with_fixable_gaps (scope overstated).
* The concrete mates of A_referee 5.2 and P1 2.3 (one block, carrier with w(k_0) = 0, d-neutral, any split K_1 of an infinite contact set):
  PROVED recovered (P2A Thm 2.1; one-sided admissible for small c by P1 Prop 2.3, so kappa < 1 and every rho < 1 works). I checked the
  data: b+ = g, omega+ = 0; b- = g - v, omega- = (c/lambda_0) e_{k_0}; z_j v_j = c|u_j| >= 0 on K'; d+- = 0.
  For P1's example with diagonal U, (TC) fails (all z_j E'_j = v_j nu_j^2/nu > 0, (M1),(M2) void since |F| = 1), so Thm 3.5 does NOT apply
  there and the recovery rests entirely on P2A Thm 2.1 — fine, since that theorem is correct.
* The GENERAL form of A_referee 5.4 (d-neutral, ANY number of active blocks) is NOT fully proved: several active blocks need (S) (P2A)
  or (TC) (P2x). The case "|I_0| >= 2, d-neutral, neither (S) nor (TC)" (e.g. all v_m supported in F u K) is open (P2A's (R2)).
  P2x 6.1 states this correctly; the summary row "A_referee 5.4 made rigorous (PROVED)" should carry the qualifier.

## 2.6 Extensions (P2x 4.3, 4.4). VERDICT: SKETCH, plausible; one sloppy estimate.
4.3(i): the bound "C(s_1 + tail_N(a))|sigma| sum_{flip set}|b_j| = o(1) s_1|sigma|" is not uniform on [s_1, tau_1] (phi(sigma) is not small for
sigma ~ tau_1). Correct argument: change <= C s_1 |sigma| phi(|sigma|); for |sigma| >= (C/eps_0) phi(tau_1) s_1 it is <= eps_0 sigma^2 directly; for
s_1 <= |sigma| <= (C/eps_0)phi(tau_1)s_1 use phi(|sigma|) <= phi(C' s_1) -> 0. Conclusion survives. 4.3(ii),(iii): fine.
4.4(a): delicate point correctly identified (gaps of truncated carriers -> 0; needs the box-tail argument of A Thm 6.2 uniformly at f').
4.4(b): degenerate peaks — plausible; note that "one-sided use" must be INWARD (|W(k)| decreasing) on the designated side, otherwise
the sup norm grows at first order; the sketch should say so.

## 2.7 Conversion cost identity (P2x 5.3). VERDICT: identity PROVED (trivial); obstruction HEURISTIC — as labelled.
|w'(k) - w(k)| >= M - |w'(k)| = gap'_k - (M' - M) at a former peak: correct. Two precisions: (1) the bound is on the q*-norm of ONE term of
L*(w' - w); the slack uses p*(f' - f), and p* >= q*/(1 + sup_{||W||<=1} q*(L*W)) only up to that constant (B_{p*} = B_{q*} + L*(B_{V*}));
(2) cancellations are not excluded. Both make it a heuristic, as P2x says. The quantitative confirmation of C's implant scale gap is
correct, and so is the conclusion that it is not an obstruction to Thm 3.5 (the band [s_1, T_0] is covered by exact transfer).

## 2.8 Numerics for the pinning step (t3_replication.py).
One block, n = 36, three strict non-peaks in the window. zeta' := c zeta on [1,K] (exact replication, c in [0.8,1.2] random), zeta' ARBITRARY
(O(1) in sup norm) beyond K. Observed: K = 8, 12, 16, 20: |C'-C| = 1.2e-4, 2.8e-6, 4.7e-7, 8.5e-9; window displacement
sum_{k<=K} lambda_k|w'(k)-w(k)| = 6.8e-4, 1.5e-5, 2.6e-6, 4.7e-8; total displacement 4.4e-3, 2.1e-4, 2.0e-5, 1.2e-6 vs 2 sum_{k>K} lambda_k =
6.8e-3, 3.7e-4, 2.5e-5, 1.6e-6. So the total is dominated by the deep part 2 sum_{k>K} lambda_k (<= 2 s_1^2 by the choice K = K(s_1)), and
|C'-C| scales like sum_{k>K} lambda_k (NOT like sum_{k>K} Phi_k^2: |zeta'| != c|zeta| changes the ratios r' by a relative O(sum_{k>K} lambda_k),
which is the extra term C'^2 sum_{W_off} Phi^2 (r'^2 - r^2) of the generalised replication identity). Both are O(s_1^2) in the pinning scheme:
(PIN) holds with room to spare, confirming 2.2(c).
