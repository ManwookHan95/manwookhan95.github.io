# Referee report on P2 (engineered recovery of one-sided mates; replication–averaging–transfer)

Referee: adversarial referee for task P2, Round 2. Setting used throughout: canonical base q, FINITE block set I (p_N, any N), only
Lemma B's conclusion about T (plus (T3), (T4) of Preprint B for finite I). Labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN.
Part files: ctx/r2/P2_ref_part0..3.md; scripts: ctx/r2/P2ref_work/ (blocklib.py, t1_bregman.py, t2_convexity.py, t3_replication.py).

## 0. Provenance and scope
Two P2 agents wrote concurrently. The claims assigned to me are those of instance "P2x" (P2x_notes.md = P2x_head + P2x_part2..5 +
P2x_tail; 439 lines). During this review ctx/r2/P2_notes.md was OVERWRITTEN (00:55:52) by the other instance "P2A" (now identical to
P2A_notes.md: toolkit 1.1-1.7, Thm 2.1 (d-neutral, pulls), 3.1-3.5, 4.1-4.6). I refereed P2x in full and re-checked P2A Thm 2.1 and
Lemma 4.1 because P2x relies on them. File references below: "P2x k.l" = P2x_notes section, "P2A k.l" = P2_notes/P2A_notes section.

## 1. Verdict table
| # | Claim (P2x) | P2x label | Verdict | Main issue |
|---|---|---|---|---|
| 1 | Three-regime theorem 5.1 (abstract) | PROVED | CORRECT | none; it is bookkeeping (content sits in hypotheses (i)-(iii)) |
| 2 | Clip formula 2.1, Bregman identity + exact form 2.2 | PROVED | CORRECT | none |
| 3 | Bregman smallness 2.3-2.4 | PROVED | CORRECT | "Theta(A) displacement" is a generic remark (can be Theta(A log 1/A)) |
| 4 | Base mixed term 2.5-2.6 | PROVED | CORRECT WITH FIXABLE GAPS | 2.6(b) needs relative COMPACTNESS in l_1 (uniform tails), not boundedness; needs (TC)-type tuning |
| 5 | Main Thm 3.5 (two-piece, Delta d_m >= 0, (TC)) | PROVED | CORRECT | trivial constant slip (Lemma 3.2 used on |s| <= tau_1/(1-x) > tau_1) |
| 6 | Delta d_m < 0 (4.1) | PROVED failure / SKETCH pinning | failure CORRECT; "recovery iff (PIN)" OVERSTATED; pinning gap FIXABLE | the missing Lipschitz step follows from P2A's replication identity (generalised) |
| 7 | (TC) failure / far pulls (4.2) | SKETCH | CORRECT WITH FIXABLE GAPS | subset-sum parenthetical FALSE (Cantor reservoirs); fix = continuous raising move + IVT (P2A) |
| 8 | A_referee 5.4 made rigorous | PROVED | CORRECT WITH FIXABLE GAPS (scope) | one block (any split) and P1's mates: PROVED; several blocks only under (S) or (TC) |
| 9 | Extensions 4.3-4.4 (a not in c_00, infinite carriers, degenerate peaks) | SKETCH | plausible SKETCH | 4.3(i) estimate not uniform as written (fixable); 4.4(b) must use degenerate peaks INWARD |
| 10 | Conversion cost identity 5.3 (implant scale gap) | PROVED identity / HEURISTIC obstruction | CORRECT | bound is on a q*-norm of one term; p* only up to a constant; cancellations not excluded (as stated) |
| 11 | Precision obstruction 5.4 | PROVED (as statement on transfers) | (a),(d) CORRECT; (b),(c) are SKETCH computations; "fatal for every mass/conversion scheme" HEURISTIC | pinning ((QI)) not excluded |
| 12 | P2A Thm 2.1 (d-neutral, pulls; used by 7, 8) | PROVED (P2A) | CORRECT | carriers must stay in their boxes on |tau| <= T_0 (automatic: T_0 small) |
No claimed counterexample exists in P2; none of the "obstructions" obstructs recovery (only methods). Density of NA((c_0,p_N), l_2^2): OPEN.

## 2. Line-by-line checks of the PROVED core (details in P2_ref_part1.md)
2.1 Three-regime theorem. For |t| <= s_J all h_j use (i). For s_J < |t| <= T_0 the indices with s_j < |t| use (ii)+(iii):
p*(f'+t h_j) <= p*(f'+t gbar) + |t|kappa s_j and sum_{s_j<|t|} s_j < 2|t|; averaging gives 1 + (Q + 4kappa/J)t^2/2; p*(g'-gbar) <= 2kappa s_1/J.
Assembly (P2_part1 1.4): 1 + (tau^2/2)(1-delta) <= 1 + tau^2/2 - tau^4/8 <= s(tau) for tau^2 <= 4 delta; for |tau| >= T_0,
s(t) - s(rho t) = (1-rho^2)t^2/(s(t)+s(rho t)) >= (1-rho^2)min(t^2,|t|)/3 absorbs (1-rho^2)(T_0^2 + |t|T_0)/6. Any mate vanishes at the normer of f',
so (f',g') attains its norm. PROVED.
2.2 Clip/Bregman. Fact C: w(k) = sgn zeta(k) min(M, C r(k)), r(k) = m|u_k(y)|/(Phi_k|zeta|), so w(k) = M clip(u_k(y)/(theta Phi_k)),
theta = M|zeta|/(mC). Identity: both sides equal |zeta'| + |zeta| - <w,zeta'> - <w',zeta>. Exact form from zeta'/|zeta'| = alpha' + D^2 w'/C',
||alpha'||_1 = 1, M + C = 1; both terms >= 0. PROVED. (Converse of Fact C, used in 4.1(d), also re-derived: zeta''/c'' in B_{l1} + D(B_{l2})
and <w, zeta''/c''> = M + C = N(w) = 1.)
2.3 Bregman smallness. (a) uses |clip(rs) - clip(s)| <= |r-1| (r > 0) and 1-Lipschitz clip; (b) case split t_k <= A / t_k > A;
(c) from the identity. gamma -> 0 along weak*-convergent normers; eps(s) = sum min(lambda_k, ms) -> 0. Lemma 2.4: |z'_j - z_j| <= 1 beyond N,
||U*u_k|| <= ||U||, normalisation of a' irrelevant for e'. Hence e_m(zhat; xhat') = o(s_1) for O(s_1) masses/moves and T_N <= s_1^2. PROVED.
Numerics (t1_bregman.py, random AND adversarial sign-aligned perturbations): e/A = 1.1e-2 ... 7.4e-5 for A = 1e-2 ... 3e-5 (e = O(A^2)),
while sum lambda|w'-w|/A in [0.5, 1.6].
2.4 Mixed term. My bound ||D^2(x/||x||)|| <= 2/||x||^2 (D^2F[k,k] = -(||k_perp||^2 u + 2<u,k>k_perp)/r^2) gives remainder <= 4||h||^2 on ||h|| <= 1/2;
P2x's 6||h||^2 is valid. 2.6(a) is trivial. 2.6(b): the U-part is controlled for bounded families (U* compact), but the z-part beyond the
window, ||(B_tau - b_0)1_(N,inf)||_1, must be <= eps_0 s_1 UNIFORMLY in tau: this needs uniformly small tails (relative compactness in l_1).
Also, 2.6 handles base parts only; for several transported pieces the BLOCK d-mismatch (P2A 3.2) is a separate condition — P2x says so.
2.5 Theorem 3.5. Re-derived every step:
 * Step 2: Gfun_m = |R_m x'|(Delta d'_m - Delta d_m) once supp omega_Delta,m is off-peak at f' (Fact C at f'); Gfun_m(zhat) = 0; |Gfun(0)| = O(s_1 + T_N).
   C^1: |.|_m Lipschitz + Gateaux => Hadamard differentiable, chain rule with the C^1 map mu -> xhat'(mu) in c_0; the derivative
   <R_m*(omega_Delta - Delta d_m w'_m), dxhat'/dmu_l> is continuous (norm x bounded weak*). Effect vectors (M1)-(M3) re-derived.
   Brouwer Lemma 3.3 correct.
 * Step 3: Omega'-_m - Omega'+_m = omega_Delta,m - Delta d_m w_m (uses Delta d' = Delta d); b'- = b- - b+1_(N,inf) - beta a';
   b'-(xhat') = -sum_m Delta d_m(|R_m xhat'| - <w_m, R_m xhat'>) = -sum_m Delta d_m |R_m xhat'| e_m(zhat; xhat') <= 0, = o(s_1).
 * Step 4: supp b'+ subset of supp a'; no sign change on [-s_1, tau_1]; q*(a' + sigma b'+) = 1 + G(sigma; U*a', U*b'+) EXACTLY; blocks by 3.2(a)
   (box check: (1-d's)gamma/2 >= gamma/4 >= s_gamma||omega||_inf) and 3.1(b) for sigma < 0.
 * Step 5: contacts without mass keep z'_j = z_j and sigma b-_j is z-signed for sigma < 0 (no kink); mass coordinates z-signed (no flip).
   Convexity: w'_m + sigma Omega'-_m = (1-x)[w'_m + sigma~(omega-_m - d'-_m w'_m)] + x w_m, x = |sigma|Delta d_m >= 0 iff Delta d_m >= 0 (the only
   use of (H2)), N_m(w_m) = 1. Slip: |sigma~| <= tau_1/(1-delta/8) > tau_1; replace tau_1 by tau_1/2 in Step 0.
 * Step 6: (1-2delta)/(1-delta/8) <= 1 - delta (iff -7delta/8 <= delta^2/8). PROVED.
 Numerics (t2_convexity.py): with a common opposite peak, the side-minus block excess is 0.49 s^2 for Delta d = +0.5 and 1.544|s Delta d| = 2M|s Delta d|
 (first order) for Delta d = -0.5.
 Observation: Lemma 3.2(b) is superfluous — Lemma 1.4 works with any FIXED T_0, so tau_1 <= s_gamma may be taken and the boxes are never left;
 "carriers pushed beyond their gap at fixed scales" are covered trivially by the slack.

## 3. Claims 6-12 (details in P2_ref_part2.md, P2_ref_part3.md)
3.1 Delta d_m < 0 (P2x 4.1).
 (a) PROVED (re-derived). At every NA approximant f' of a non-attaining f, each block has infinitely many COMMON OPPOSITE peaks: zhat (not in
     c_0) and xhat' (in c_0) are linearly independent, so some phi in S_Y has phi(zhat) > 0 > phi(xhat'); by density of every tail of
     (u_{k,m})_k and Phi_m(k) -> 0, the u_{k,m} close to phi are peaks of both with opposite signs. For W = w' + s(omega - d'w') + s'(w - w'),
     s' < 0: N(W) >= 1 + |s'|(M + M') - |s'|(C' - <Dw,Dw'>/C') = 1 + 2M|s'| - o(|s'|). Numerically 2M|s'| to 3 digits.
     Strengthening (P4 in part 3): no ANCHOR rescues convexity — with side + used two-sidedly, Omega'- must contain c(w' - wtilde) with
     wtilde = w' + (|Delta d|/c)(w' - w), and N(wtilde) >= 1 + 2M|Delta d|/c at the same peaks; using side - two-sidedly gives the same sign
     condition. So within "fixed carriers + block-functional multiples", Delta d_m >= 0 is NECESSARY.
 (b) OVERSTATED: "recovery holds iff (PIN)". Only "if" is (sketch-)proved; "only if" is a statement about the transfer scheme, not about
     recovery of the mate (other data, other decompositions at f', other mechanisms are not excluded).
 (c) FIXABLE GAP, now essentially closed: the "unwritten Lipschitz step" of the pinning sketch follows from P2A's replication identity
     (P2A 4.1), generalised to approximately tuned ratios. Statement: let W_off (tuned strict non-peaks, ratio r'(k) = r(k)(1 + epsilon_k)),
     W_P (peaks at f and f' with the same sign), Ch (the rest), rho_W := sum_{W_off} Phi^2 r^2, S_P := sum_{W_P} Phi^2,
     G(c) := c^2(1 - rho_W) - (1-c)^2 S_P. Then
        G(C') - G(C) = sum_{Ch} Phi_k^2 (w'(k)^2 - w(k)^2) + C'^2 sum_{W_off} Phi_k^2 (r'(k)^2 - r(k)^2),
     G is strictly increasing on (0,1) with G' >= 2 min(C,C')(1 - rho_W) =: g_0 > 0 (1 - rho_W >= sum_P Phi^2 M^2/C^2 > 0), hence
        |C' - C| <= [sum_{Ch} Phi_k^2 + 3 C'^2 rho_W max_k |epsilon_k|]/g_0,
     and w'(k) - w(k) = sgn(w(k))(C'r'(k) - C r(k)) on W_off, = sigma_k(M' - M) on W_P.
     Proof: C^2 = sum Phi^2 w^2 with w = C sgn r on W_off and |w| = M = 1 - C on W_P (clip formula), and the same at f'. Mean value theorem.
     In the pinning scheme (Q_m finite, robust window peaks, conditions (i)-(ii) of 4.1(d)), Ch is contained in (K, inf) and
     max|epsilon_k| = O(||R x' - zeta^#||_1) = O(sum_{k>K} lambda_k) = O(s_1^2) (|zeta^#| = c|zeta| by the converse of Fact C), so
     ||R*(w' - w)||_1 = O(s_1^2): (PIN) holds. Numerics (t3_replication.py): exact replication on [1,K], arbitrary O(1) perturbation beyond K:
     total displacement 4.4e-3, 2.1e-4, 2.0e-5, 1.2e-6 vs 2 sum_{k>K} lambda_k = 6.8e-3, 3.7e-4, 2.5e-5, 1.6e-6 (K = 8, 12, 16, 20).
     Remaining hypotheses (genuine): Q_m finite; margins >= C s_1 on peaks k <= K(s_1) along a sequence s_1 -> 0 (or margin sparsity, P2A (MS));
     a (TC)-type spanning condition for the |Q_m| + 1 linear conditions; the residual Delta d' - Delta d = O(s_1^2) is absorbed by approximate
     tuning (3.2). Status: SKETCH with all estimates available.
 (d) infinitely many strict non-peaks: OPEN (agreed).
3.2 (TC) failure / far pulls (P2x 4.2). SKETCH, with one FALSE remark.
 * "Approximate tuning to precision c eps_0 s_1 suffices" — correct: the residual y = -sum_m (Delta d_m - Delta d'_m) R_m* w'_m sits only in the
   side-minus base, first-order cost <= C|sigma| max|Delta d - Delta d'| <= 2Cc eps_0 sigma^2 on |sigma| >= s_1/2; side + (which defines g') untouched.
 * FALSE: "every value in [0, sum] is within the last increment of a finite subset sum". For super-decreasing increments (e.g. |V(j)| ~ 3^{-j}
   on K) the subset sums form a Cantor set with gaps comparable to the target; one cannot have all increments beyond N' below c eps_0 s_1
   while the reservoir beyond N' still exceeds the O(s_1) target. Repair: end with a CONTINUOUS one-sided move — the raising coordinate j_+ of
   P2A Thm 2.1, which always exists by the sign identity sum_F v_j<P_{e-perp}U*v, U*e_j*> + sum_K |v_j|<P_{e-perp}U*v, z_j U*e_j*> = ||P_{e-perp}U*v||^2 > 0 —
   and the intermediate value theorem (exact tuning); or choose s_1 so that the target lies on the closure of the subset sums.
 * One block, Delta d = 0: PROVED (P2A Thm 2.1; re-checked below). Delta d > 0 with pulls: the Far flips enter the Bregman pairing through
   sum_k lambda_k|w'(k) - w(k)| ||u_k 1_Far||_1, and N must precede s_1 (reservoir), so T_N <= s_1^2 is lost: OPEN / T-dependent (agreed).
3.3 P2A Theorem 2.1 (d-neutral two-piece mates, pulls). Re-checked line by line: PROVED. (P_{e-perp}U*v != 0 because v in Y\{0},
 Y cap c_00 = {0}, U* injective; v(z'-z) = -2V_Far - V_{>N''}; |<U*v, e(a''(0)) - e>| <= A_0 s_1 + V_Far/2 by 16 rho T_0||U|| ||U*v|| <= nu;
 Psi(0) <= -V_Far; IVT with derivative >= gamma_+/2; p-moves at free j_i change neither v(xhat') nor e'; d'^+ = d'^- since
 (R_m* omega_Delta)(x') = v_m(x') = 0; B^+- = B^theta + (theta v, -(1-theta) v); Far: z'_j = -z_j = sign a'_j, |a'_j| >= 2 rho T_0|v_j|, no flip;
 kink only beyond N''; theta-side kink-free.) Its blocks stay inside their boxes on |tau| <= T_0, which costs nothing (T_0 is fixed).
3.4 A_referee 5.4 "made rigorous". The concrete mates of A_referee 5.2 and P1 2.3 (one block, carrier with w(k_0) = 0, any split K_1 of an
 infinite contact set) are PROVED recovered by P2A Thm 2.1 (data b+ = g, omega+ = 0; b- = g - v, omega- = (c/lambda_0)e_{k_0}; d+- = 0;
 one-sided admissible for small c by P1 2.3, so kappa < 1 and every rho < 1 works). In P1's example with diagonal U, (TC) fails
 (|F| = 1 makes (M2) void, v lives on F u K so (M1) is void, and all z_j E'_j = v_j nu_j^2/nu > 0): Thm 3.5 does not apply, P2A does.
 The GENERAL form (d-neutral, ANY number of active blocks) is proved only under (S) (P2A) or (TC) (P2x); the case |I_0| >= 2 with neither
 is OPEN (P2A (R2)). P2x 6.1 states this correctly; the summary row should carry the qualifier.
 Structure of (TC) (observation): on free coordinates sum_m V_m(j) = v(j) = 0, so (M1) effects lie in H_0 = {sum y_m = 0}; the total direction
 must be controlled by (M2)/(M3) or pulls. P2A's (S) is "(M1) spans H_0"; the uncovered case is exactly the failure of both halves.
3.5 Extensions (P2x 4.3-4.4): SKETCH, plausible. 4.3(i): "C(s_1 + tail)|sigma| phi(sigma) = o(1) s_1|sigma|" is not uniform on [s_1, tau_1]
 (phi(tau_1) is not small); correct by splitting at |sigma| = (C/eps_0)phi(tau_1)s_1 (above: direct; below: phi(|sigma|) <= phi(C's_1) -> 0).
 4.4(b): a degenerate peak may only be used INWARD (|W(k)| decreasing) on its side; outward use raises the sup norm at first order.
 4.4(a): the delicate point (truncated carriers have gaps -> 0; box-tail discarding at f' uniformly along approximants) is correctly identified.
3.6 Conversion cost identity (P2x 5.3): |w'(k) - w(k)| >= gap'_k - (M' - M) at a former peak — PROVED (trivial). It bounds the q*-norm of ONE
 term of L*(w' - w); the slack uses p*(f' - f) >= q*(f' - f)/(1 + sup_{||W||<=1} q*(L*W)) only up to that constant, and cancellations are not
 excluded: HEURISTIC as an obstruction, as labelled. C's implant-scale-gap heuristic is confirmed quantitatively and correctly declared
 NOT an obstruction to Thm 3.5 (the band [s_1, T_0] is covered by exact transfer of robust structure).
3.7 Precision obstruction (P2x 5.4): (a) PROVED (error = (M'/theta' - M/theta)u_k(xhat')/Phi_k, |u_k(xhat')/Phi_k| < theta'); (d) PROVED as a remark on
 Lemma 1.5. (b),(c) compute the cost of two specific transfer options; "either way the error is ~ lambda_k Delta_k/Phi_k" is inaccurate for the
 first option (its N_m-error is ~ Delta_k/Phi_k); the conclusion uses the better option. "Fatal for every mass/conversion-based scheme"
 (Sect. 0) is HEURISTIC: pinning/retuning ((QI)) is not excluded — P2x says so at the end of 5.4. Also Prop 2.6(b): see 2.4 above.

## 4. Hidden assumptions checked (task checklist)
weak* vs norm: f' -> f and g' -> g in NORM (L compact; R*w' -> R*w in l_1). Uniformity in t: all eta's in Steps 4-6 are independent of sigma.
Uniformity in the scale: s_1 -> 0, N(s_1) -> inf, mu* = O(s_1 + T_N). Non-attained infima: p* is a min (Fact A); forced decomposition
unique (T4). Signs/one-sidedness: checked coordinate class by coordinate class (F, mass contacts, massless contacts, (M1)/(M3) tuning
coordinates, tail beyond N). c_0 vs l_inf: xhat' = z' + U e' with z' in c_00. Finite vs infinite peak/contact sets: K, P_m infinite allowed;
only supp omega finite. I finite: used only via (T4)/Fact E (for the canonical base with I = N, (T4) is the unavailable [Recovery] result;
Martin's Prop 3 is for his DGS base). T beyond Lemma B: nothing; (TC) is an explicit joint hypothesis on (f, g, U, T).

## 5. Most valuable idea
The convexity placement of the d-mismatch with Bregman pricing (P2x Thm 3.5, Steps 3 and 5; Lemma 2.2-2.3): the d-mismatch
Delta d_m R_m*(w'_m - w_m) is Theta(s) in l_1 (window masses move off-peak values by ~ s/Phi_k) and cannot be paid in the base, but if it is
placed in the block decomposition of the side on which it moves TOWARD the old block functional w_m, then
w'_m + sigma Omega'_m = (1-x)[transferred one-sided part] + x w_m with N_m(w_m) = 1, so the block costs nothing extra, and the only price is
a first-order base term equal to the Bregman excess e_m = 1 - <w_m, R_m xhat'>/|R_m xhat'|_m, which is o(s) (in fact O(s^2 log 1/s) + O(T_N))
by the identity |zeta'|e(y;y') + |zeta|e(y';y) = <w' - w, zeta' - zeta>. "Displacement Theta(s), pairing o(s)" is the mechanism.

## 6. Recommendations
1. Write the pinning theorem for Delta d < 0 at block-tame blocks using the generalised replication identity of 3.1(c) (all estimates
   are now available); combine with approximate tuning.
2. Replace the subset-sum remark of P2x 4.2 by the raising-coordinate/IVT finish; then attack Delta d > 0 with pulls by choosing Far
   inside K where the u_k's carry little mass relative to v (a far-tail comparison; T-dependent).
3. Multi-block d-neutral data without (S)/(TC): try pulls in several blocks (one reservoir per block direction), with the (M1)/H_0 structure
   of 3.4.
4. State the scope precisely in the summaries (items O1-O5 of P2_ref_part3.md). Keep "density: OPEN".


===================================================================================================
# PART II — second referee: report on the P2A version (ctx/r2/P2_notes.md = P2A_notes.md)
(Appended non-destructively by the P2A referee; the P2x report above is unchanged. Standalone copies: ctx/r2/P2A_referee.md,
 full notes with appendix of detailed checks: ctx/r2/P2A_ref_notes.md.)
===================================================================================================

# Referee report on P2, version "P2A" (ctx/r2/P2_notes.md = P2A_notes.md, 512 lines)

Referee: Round 2, adversarial check of the P2A instance (toolkit 1.1-1.7, Thm 2.1, Cor 2.3, Rem 2.4, Props 3.1-3.3, Thm 3.4,
Lemmas 4.1-4.2, Prop 4.3; 4.4-4.6 in passing). The concurrent instance "P2x" is refereed separately (its report is the first part of
ctx/r2/P2_referee.md). Setting used: canonical base q, FINITE block set I (p_N, any N; Preprint B Remark martin-tail), only Lemma B's
conclusion about T. Part files: ctx/r2/P2A_ref_part1..5.md; scripts: ctx/r2/P2Aref_work/. Labels: PROVED/SKETCH/HEURISTIC/FALSE/OPEN.

## 0. Summary
* The core is CORRECT. Theorem 2.1 (engineered recovery of d-neutral two-piece switching mates: any infinite contact set K, any
  non-constant split, one active block, or several under (S)) is PROVED; I re-derived every step (part 2). Its mechanism is sound:
  the one-sided decompositions of f are transported EXACTLY to an engineered NA point f' (d-coefficients recomputed at f';
  one scalar steering condition v_m(x') = 0 per block, achieved by a far negative-mass pull, one raising mass and the IVT), window
  masses and a theta-tail serve |tau| <= s_1, and the slack is needed only beyond a FIXED T_0. Only one trivial gap (rho < 1/32).
  Consequently P1's explicit defect mates and P1's slab ARE in Ls(f) (Cor 2.3(b), slab part, PROVED): P1's nonempty defect is a defect
  of the intrinsic mechanisms only. Toolkit 1.1-1.5, 1.7 and Props 3.1, 3.2 are correct.
* Theorem 3.4 (non-neutral data at block-tame blocks) is WRONG AS STATED: its hypothesis (iii) (linear independence on J_gamma of the
  tuning functionals psi_{k,m}) can NEVER hold for non-trivial two-piece data, because
      sum_{k,m} lambda_{k,m} omega_Delta,m(k) psi_{k,m} = b+ - b- = v,  which vanishes on J_gamma   (Prop. R1, PROVED, numerically checked).
  The sketch's mechanism ("no Far set, no raising mass: steering is part of the tuning") is therefore impossible — the resonance
  direction is invisible to free moves (the authors' own remark after Lemma 4.2). A repair needs base-side steering again, and when that
  steering needs a PULL (Far flips), the flips damage the active block's peaks by amounts not controlled by (MS): a far-tail comparison
  (rate condition on T) is needed. So "A_referee §5.5 is too pessimistic" is NOT established by P2A. (For Delta d >= 0 under a cone
  condition it IS established by the other instance, P2x Thm 3.5, via a Bregman argument that also shows P2A's diagnosis "infinitely many
  strict non-peaks is what breaks it" to be an artefact of putting the d-mismatch into the base.)
* Fixable gaps: Cor 2.3(b) omits the hypothesis g in C(f) (P1-referee's correction C4, cited but not implemented); Prop 3.3 is a
  sufficient condition only and its steering needs a path-uniform E bound; Lemma 4.1's "deep replication costs O(theta)" is false for
  admissible T (correct: O(theta log(1/theta))); Prop 4.3 needs s_1 -> 0 (or J >~ kappa/(1-rho^2)); Lemma 4.2's "iff" holds for l_inf moves.
* Remark 2.4: the shifted extension of Thm 2.1 is a plausible SKETCH (I checked the domination of the shift kink costs), but "together
  with P1 6.1 this would give f in R at P1's example" is unsupported (HEURISTIC): P1 6.1 provides no shifted decompositions with H^sh <= 1.
* No counterexample is claimed or implied. Density of NA((c_0,p_N), l_2^2): OPEN.

## 1. Verdict table (assigned claims)
| Claim | Label (P2A) | Verdict | Main issue |
|---|---|---|---|
| Setting (finite I, only Lemma B, imports) | PROVED | correct | imports used as stated; no hidden property of T |
| Lemma 1.1 clamp formula | PROVED | correct | = A Fact C; also at NA points (degree-0 homogeneity) |
| Lemmas 1.2-1.5 toolkit | PROVED | correct | re-derived (L compact, J_m norm-to-weak* continuous; Lemma 7.2 at f'; slack lemma; geometric sum < 2|t|) |
| Lemma 1.7 (admissible => kappa <= 1) | PROVED | correct | general Lemma 7.2 (b+ not in supp a) + Psi lower bound; A Lemma 4.4(b) |
| Thm 2.1 main | PROVED | correct (one trivial fixable gap) | Step 1 needs V_{>N''} <= V_Far, true only for rho >= 1/32; fix in (C4) |
| Cor 2.3 | PROVED | correct with fixable gaps | (b) must assume g in C(f); (a) cites P1 2.3 (specific example) for a general setting |
| Rem 2.4 shifted data / f in R | SKETCH | unclear | extension plausible; "f in R" HEURISTIC (P1 6.1 gives no H^sh <= 1 data) |
| Prop 3.1 mixed term | PROVED | correct | — |
| Prop 3.2 consistency identity | PROVED | correct | "must be <= eps_0 s_1" is sufficient, not proved necessary |
| Prop 3.3 garbage identity | PROVED | correct with fixable gaps | sufficient only ("provided", not "exactly when"); steering for Delta d != 0 is not verbatim (path-uniform E bound; modified (S)) |
| Thm 3.4 (Delta d != 0, tame blocks) | SKETCH | wrong | hypothesis (iii) never holds (Prop. R1); tuning-only steering impossible; repair needs base steering, and if that needs pulls, Far-flip collateral damage needs a rate condition |
| Lemma 4.1 replication identity | PROVED | correct with fixable gaps | identity right; "O(theta)" consequence false (log factor); c_f depends on rho_W |
| Lemma 4.2 retuning feasibility | PROVED | correct | "iff" for l_inf(G)-moves; c_0-moves reach the relative interior |
| Prop 4.3 abstract scheme | PROVED | correct with fixable gaps | Lemma 1.4(ii) needs p*(g'-rho g) <= (1-rho^2)T_0/6; add s_1 <= eta or J >= 24 kappa/(1-rho^2) |

## 2. Line-by-line verification (condensed; details in P2A_ref_part1.md, part2.md)
2.1 Toolkit. 1.1 is Fact C: on P, |zeta(k)|/|zeta| = |alpha_k| + Phi_k^2 M/C, so C r(k) >= M; off P, |w(k)| = C r(k) < M; zeta(k) = 0 => w(k) = 0.
1.2: L compact => L** weak*-to-norm on bounded sets, L** zhat in V; J_m norm-to-weak* continuous at R_m** zhat != 0 (T3); D_m, R_m* compact;
grad q(xhat_n) = a_n since a_n norms xhat_n; J_V = (J_m)_m for finite I. 1.3: <omega - d'w', R_m x'> = 0 for omega off P'_m (Fact C at f'),
then A Lemma 7.2 at f'. 1.4: 1 + (tau^2/2)(1-delta) <= 1 + tau^2/2 - tau^4/8 <= s(tau) iff tau^2 <= 4 delta; beyond T_0 the slack lemma.
1.5: for s_j < |t|, sum s_j < 2|t|. 1.6: g(xi) = 0 for every mate; b+-(zhat) = 0; v != 0 forces K infinite (v in Y \ c_00 on F cup K).
1.7: base via Lemma 7.2 + Psi(h) >= ||h_perp||^2/(2(1+||h||)), blocks via A Lemma 4.4(b) as tau -> 0+.
2.2 Theorem 2.1. Re-derived: raising coordinate from sum_F v_j<PU*v,U*e_j*> + sum_K |v_j|z_j<PU*v,U*e_j*> = ||PU*v||^2 > 0 (P = P_{e-perp};
PU*v != 0 as v notin Ra, U* injective); Fact D compatibility of z'; v(xhat') = -2V_Far - V_{>N''} + <U*v, e'-e>; the bound
|<U*v, e(a''(0)) - e>| <= (A_0 - 1)s_1 + V_Far/2 <= V_Far; dPsi/dmu >= gamma_+/2; MVT + IVT; p-moves change neither e' nor v(xhat');
d'^+ = d'^- = d'^theta from <Dw', D omega_Delta> = (C'/|Rx'|) v_m(x') = 0; (2.1.2); convergence (z' -> z coordinatewise, masses -> 0,
Lemma 1.2, c -> g(zhat) = 0, B^sigma -> rho b^sigma); block costs within the coordinatewise radius (fix G1) on the FIXED range |tau| <= T_0;
no flips (F, window, j_+, Far: |a'_j| >= 2 rho T_0|v_j|); kinks only beyond N'' (z' = 0), <= rho|tau|V_{>N''}/2 <= eps_0 tau^2 on |tau| >= s_1,
none for sigma = theta; Step 6 arithmetic (tau^2/2)(rho^2 kappa + delta/2) <= (tau^2/2)(1 - delta).
Gap (trivial): Step 1 needs Psi(0) >= -4V_Far, i.e. V_{>N''} <= V_Far; (C4) gives V_{>N''} <= delta s_1/(8 rho) and V_Far >= 2 s_1, so this
holds for rho >= 1/32 only. Fix: V_{>N''} <= min(eps_0 s_1/rho, V_Far) in (C4) (or scale: (f', lambda g') stays NA for |lambda| <= 1).
Hidden assumptions: none found (weak* vs norm: f', g' converge in norm; uniformity: all estimates on a fixed tau-range with finitely
many converging data; c_0: z' in c_00; T: only Y cap c_00 = {0}, injectivity; K and the peak sets may be infinite).

## 3. Main problems
### 3.1 Theorem 3.4 is vacuous (WRONG as stated). Proposition R1 (PROVED).
For two-piece data (P2A 1.6) with omega_Delta != 0 and every gamma > 0, the restrictions to J_gamma = {j notin F : |z_j| <= 1-gamma} of the
functionals psi_{k,m} = u_{k,m} - (u_{k,m}(xi)/|zeta_m|) R_m* w_m (k in Qbar_m, m in I_0) are linearly dependent.
Proof. supp omega_Delta,m lies in the strict non-peaks, hence in Qbar_m. With c_{k,m} := lambda_{k,m} omega_Delta,m(k) (not all zero):
sum_k c_{k,m} u_{k,m} = R_m* omega_Delta,m = v_m and sum_k c_{k,m} u_{k,m}(xi) = <omega_Delta,m, zeta_m> = |zeta_m| Delta d_m (Fact C, omega_Delta,m off P_m).
Hence sum_{k,m} c_{k,m} psi_{k,m} = sum_m (v_m - Delta d_m R_m* w_m) = b+ - b- = v, supported in F cup K, disjoint from J_gamma. QED.
(If omega_Delta = 0 then v = 0 and g is a finite certificate.) Numerically: identity to 4e-14, Fact C to 9e-11 (thm34_dependence3.py).
Consequences. (a) The linearised tuning map in the free variables has range in the hyperplane annihilated by (c_{k,m}|zeta_m|); the
missing direction is exactly the steering quantity v(xhat') (mixed term, Prop 3.1), whose residual after the window masses is ~ s_1.
So the construction "without Far set and raising mass" cannot work. (b) The example sentence is void: at P1's example |Qbar_1| = 1 and
psi_{2,1}|_J = u_{2,1}|_J = 0. (c) Repair (SKETCH): replace (iii) by (iii') "the c-relation is the only relation among the psi_{k,m}|_{J_gamma}"
and steer the c-direction from the base. If two-sided steering by O(s_1) masses exists (some j in F with <PU*v, U*e_j*> != 0, or a contact
with z_j<PU*v, U*e_j*> < 0 — essentially P2x's (TC)), all displacements are O(s_1) in sup norm plus the last cut-off, (MS) + Lemma 4.1 give
||E||_1 = o(s_1) and Prop 3.3 applies: plausible. If a PULL is needed (e.g. |F| = 1, diagonal U: P1's situation), the Far flips
z'_j = -z_j move every u_{k,m}(xhat') by up to 2||u_{k,m} 1_Far||_1, which is not O(s_1) uniformly in k (a peak u_k ~ e_j*/q*(e_j*), j in Far,
changes w(k) by ~ 2M); controlling the resulting E needs a comparison of the tails of the first ~log(1/s_1) block vectors with the tail
tau_N of v — a rate condition not implied by Lemma B (it holds for P1's T by its allowedness rule). The P2x referee reached the same
conclusion for the Bregman variant ("Delta d > 0 with pulls: OPEN / T-dependent").
### 3.2 Cor 2.3(b) misses g in C(f).
Thm 2.1 uses g in C(f) for |tau| >= T_0; rho^2 max(h(g - mu+- u), mu+-^2/C_1) < 1 does not imply it (h sees only ||P_{e-perp}U*b||^2/nu and U* is
compact: a large contact mass far out has small h but large q*). Fix: "every g in E_u cap C(f) with ...". The slab part is fine (P1 6.2).
### 3.3 Remark 2.4's consequence is unsupported.
P1 6.1 proves C(f) in E_u and mu+ <= theta(g) <= mu- for LIMITS of carrier coefficients; it does not provide (shifted) two-piece
decompositions with H^sh <= 1 (P1's own remark: peaks, level shifts, free coordinates may contribute O(t^2) to the costs; P1-referee C1:
the sharp second-order invariant involves transfer-peak rebalancing, Gamma_w <= H^sh, which is not of shift type). "f in R at P1's
example" remains OPEN. The extension itself (shifted two-piece data) is a plausible SKETCH: at window contacts a cheap shift has the sign
of the mass (no flip) and an expensive one costs <= its cost at f; Far flips and the cut-off cost <= 2 tau^2 ||v'_theta 1_{(N,inf)}||_1 = o(1)tau^2.
### 3.4 Lemma 4.1: "deep replication costs O(theta)" is false for admissible T.
Lemma B gives no lower bound on q*(T e_{k,m}); any rescaling T e_{k,m} -> c_{k,m} T e_{k,m} is admissible. With Phi_m(k) = 2^{-m-j^2} on
[j^2 - j, j^2) and 2^{-m-k} elsewhere, sum_{Phi<theta} Phi_k / theta ~ sqrt(log2(1/theta)) at theta = 1.01*2^{-m-j^2} (exact values 4.7 ... 20.8,
lemma41_log.py). Correct bound: sum_{Phi_k<theta} Phi_k <= sum_k min(theta, 2^{-m-k}) <= theta(log2(1/theta) + 2), so O(theta log(1/theta)).
The identity itself (G(C') - G(C) = sum_Ch Phi^2(w'^2 - w^2), |C'-C| <= sum_Ch Phi^2/g_0, the l_1 bound) is correct.
### 3.5 Smaller points.
Prop 3.3: the steering function for Delta d != 0 is F(mu) = v(xhat') - Delta d beta(xhat'), beta(x) := |R_1 x| - <w_1, R_1 x> >= 0, so the
IVT needs |Delta d| beta <= ||E||_1 ||xhat'||_inf small along the whole path; several blocks need (S) for (v_{m,j} - Delta d_m (R_m*w'_m)_j)_m.
Prop 4.3: as in the table. Lemma 4.2: l_inf vs c_0 moves. 4.5: C (C_part6 9.3) claimed only that implants are never the SOLE support at
intermediate scales — Thm 2.1 is consistent with it (the band (s_1, T_0) is carried by transferred shared structure); "FALSE" overstates.
3.5(R5)/4.4(4)(c) (degenerate peaks via one tuning move "then Thm 2.1 applies"): the implanted gap gamma' gives radius ~ gamma'; a one-sided
(inward-only) box lemma is missing. 3.3/3.5(R1) "infinitely many strict non-peaks is what breaks it": an artefact of the base-garbage
method (P2x Thm 3.5's Bregman route needs no finiteness for Delta d >= 0).

## 4. Numerics (ctx/r2/P2Aref_work/)
thm34_dependence3.py (block norming via the consistency equation mu|zeta| = C; 24 random blocks; Fact C 9e-11, identity 4e-14);
lemma41_log.py (exact rational arithmetic, log-factor counterexample). No finite-model test of Thm 2.1: finite models cannot
discriminate (every functional attains its norm; the unsteered pair is also contractive there); the proof was checked by hand.

## 5. Recommendations
1. Keep Thm 2.1 and Cor 2.3 (with g in C(f) added in (b)) as the main result; fix (C4) for small rho.
2. Withdraw Thm 3.4; replace by (iii') + base steering, split into (TC)-type two-sided steering (plausible; cf. P2x Thm 3.5) and
   pull-only steering (needs a far-tail comparison; OPEN, T-dependent). Withdraw "A_referee §5.5 is too pessimistic" or attribute it to P2x
   Thm 3.5 (Delta d >= 0, (TC)).
3. Downgrade the "f in R at P1's example" sentence of Rem 2.4 to HEURISTIC/OPEN; state the needed lemma: every g in C(f) admits limit
   side decompositions (possibly with shifts or transfer peaks) of coefficient <= 1.
4. Correct Lemma 4.1's consequence (log factor) and Prop 4.3 (s_1 <= eta). Reword 4.5.

## 6. Most valuable idea
Scale decoupling by exact transfer (Thm 2.1): transport the two one-sided linear decompositions of f to an engineered NA point f' with
NO first-order error — recompute the block d-coefficients at f' and enforce the single scalar condition v_m(x') = 0 per block by a
far negative-mass pull (sign-flipped far contacts carrying masses), one raising mass and the intermediate value theorem — and use window
masses plus a theta-tail of the target only for |tau| <= s_1. Then the slack is needed only beyond a FIXED T_0, so the engineering scale
s_1 is decoupled from the slack scale sqrt(p*(f'-f)); this is what makes switching mates over infinite contact sets recoverable without any
rate condition on T. (The referee's complementary observation: the tuning functionals satisfy sum c psi = v, so resonance directions can
only be steered through the base — free coordinates never suffice.)
