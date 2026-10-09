# P2x part 5: the general replication–averaging–transfer theorem, the scale-dependent regime, the implant scale gap, the residual class

## 5.1 Theorem (three-regime theorem, abstract form). PROVED.
Let f in S_{p*}, g in C(f), rho in (0,1), delta in (0,1]. Let f' in S_{p*}, gbar, h_1..h_J in X*, scales s_1 > s_2 > ... > s_J > 0 with s_{j+1} = s_j/2, and
Q, kappa >= 0, T_0 in (0,1] such that
 (i)   (small scales: two-sided certificates)   p*(f' + t h_j) <= 1 + Q t^2/2 for |t| <= s_j;
 (ii)  (transfer regime)                        p*(f' + t gbar) <= 1 + Q t^2/2 for s_J <= |t| <= T_0;
 (iii) (frozen errors)                           p*(h_j - gbar) <= kappa s_j;
 (iv)  (constants) Q + 4kappa/J <= 1 - delta, T_0^2 <= 3 delta;
 (v)   (slack regime) p*(f' - f) <= (1-rho^2)T_0^2/6 and p*(gbar - rho g) + 2 kappa s_1/J <= (1-rho^2)T_0/6.
Then g' := (1/J) sum_j h_j lies in C(f'); if f' is NA then (f', g') is NA and ||(f',g') - (f, rho g)|| <= p*(f'-f) + p*(gbar - rho g) + 2kappa s_1/J.
*Proof.* P2_part1 Lemma 1.5 (averaging; the sum over s_j < |t| of s_j is <= 2|t|) gives p*(f' + t g') <= 1 + (Q + 4kappa/J)t^2/2 on |t| <= T_0 and
p*(g' - gbar) <= 2kappa s_1/J; P2_part1 Lemma 1.4 (assembly) with (iv), (v). QED.
(J = 1, h_1 = gbar is the form used in P2x_part3; then (iii) is void.)

## 5.2 Where the three regimes come from, and what each costs (the bookkeeping). PROVED statements.
(a) Slack: covers |t| >= T_0 with T_0 ~ sqrt(6 eps/(1-rho^2)), eps := p*(f' - f) (Lemma 1.4). Any engineering creating two-sided structure for
    regime (i) at scale s contributes to eps (5.3), so regime (ii) must cover a band [s, ~sqrt(s)] at least.
(b) Transfer, base side: exact up to (1) flip changes O(s|t|) x (mass of the flip set), (2) window tails (choose N late), (3) the mixed term
    (P2x_part2 2.5-2.6: finitely many tunings, or compactness). None is an obstruction.
(c) Transfer, block side: the first-order block term is zero when d-coefficients are computed at f'; the price is a consistency mismatch
    sum_m (Delta d-type coefficient) R_m*(w'_m - w_m), which is Theta(s) in l_1 (P2x_part2 Remark 2.3) and is admissible only (1) in the convexity
    form (sign condition), paid by a Bregman excess o(s) (P2x_part2 2.3), or (2) after pinning (P2x_part4 4.1).
(d) Transfer of SCALE-DEPENDENT carriers (Proposition 5.4): not robust.

## 5.3 Lemma (conversion cost identity: the implant scale gap made precise). PROVED.
Let k be a peak of w_m at f and suppose at f' it is an off-peak coordinate with gap'_k = M'_m - |w'_m(k)| (an "implant" or "conversion"). To carry,
two-sidedly at scales |t| <= t_cap, a component c u_{k,m} of the direction through k alone (coefficient c/lambda_k at k), the box condition requires
|t| |c|/lambda_k <= gap'_k/2, i.e. t_cap <= lambda_k gap'_k/(2|c|). The block part of f' - f contains the term lambda_k (w'_m(k) - w_m(k)) u_{k,m}, of q*-norm
lambda_k |w'_m(k) - w_m(k)| >= lambda_k (gap'_k - |M'_m - M_m|) >= 2|c| t_cap - lambda_k |M'_m - M_m|.
So the contribution of the conversion to f' - f is at least 2|c| t_cap (up to the global level change), unless cancelled by other changes of f'.
*Proof.* |w_m(k)| = M_m at a peak; |w'(k) - w(k)| >= |w(k)| - |w'(k)| = M - M' + gap'. QED.
Consequence (HEURISTIC as an obstruction, because cancellations in f' - f are not excluded): an engineered two-sided carrier of capacity t_cap costs
eps >~ |c| t_cap, the slack then covers only |t| >~ sqrt(|c| t_cap/(1-rho^2)), and the band [t_cap, sqrt(t_cap)] must be covered by structure that f and f'
share. This is C's "implant scale gap" (C_notes 9.3), CONFIRMED in this quantitative form; it applies equally to near-threshold conversions
(E_part2 2.4): their low cost buys proportionally low capacity. The same identity holds for window masses on base contacts: a mass m_j at a contact used
with coefficient b_j gives capacity m_j/|b_j| and costs m_j in ||a' - a||_1.
C's conclusion "implants are useful only below the slack scale created by other mismatches, never as the sole support at intermediate scales" is
CORRECT but not an obstruction to the three-regime scheme: Theorem P2x_part3 3.5 covers the band by EXACT transfer of the one-sided decompositions of f.

## 5.4 Proposition (precision obstruction for scale-dependent block carriers). PROVED (as a statement about transferred decompositions).
Let f' be an engineered approximant whose normer differs from zhat by Delta_k := |u_k(xhat') - u_k(zhat)| at a block coordinate k that is off-peak at f and f'.
(a) (clip formula) |w'(k) - w(k) - (M/theta)(u_k(xhat') - u_k(zhat))/Phi_k| <= |M'/theta' - M/theta| theta' = o(1): the value moves by ~ Delta_k/Phi_k.
(b) Suppose a decomposition of f + t rho g at f uses k beyond its box, i.e. the sup norm of W = w + t Omega is attained at k: |w(k) + t Omega(k)| = ||W||_inf.
    Transferring it to f' with the same coefficient changes the sup part by w'(k) - w(k) (zero order in t); re-tuning the coefficient to
    Omega'(k) = Omega(k) - (w'(k) - w(k))/t keeps the sup part but changes the represented direction by lambda_k (w'(k) - w(k)) u_k, which must be carried by the
    base: first-order cost in the base of order |t| (lambda_k |w'(k) - w(k)|/|t|) times the kink weight = lambda_k |w'(k) - w(k)| x O(1) (zero order in t).
    Either way the error is ~ lambda_k Delta_k/Phi_k ~ m Delta_k, to be compared with eps_0 t^2.
(c) With window masses of size s (needed for regime (i) at scale s, by 5.3), Delta_k ~ s for every k (P2x_part2 2.4; generically sharp), so a carrier used at
    scale t ~ Phi_k (a scale-dependent carrier: depth tied to the scale) transfers only for t >~ sqrt(s/eps_0): the band [s, sqrt(s/eps_0)] is NOT covered.
(d) Averaging does not help: in 5.1 the transfer (ii) of gbar is needed down to the SMALLEST scale s_J, but the engineering for the largest
    certificate h_1 (scale s_1 = 2^{J-1} s_J) perturbs the normer by ~ s_1.
*Proof.* (a) P2x_part2 2.1 (off-peak: w = M u/(theta Phi)). (b),(c) are direct computations from (a) and P2x_part2 2.4. (d) Lemma 1.5's hypothesis (ii). QED.
So the only structure that crosses the band is "robust" structure: base coordinates (contacts, near-contacts, flips: P2x_part2 2.6), finitely many FIXED
block carriers with d-coefficients recomputed at f' (P2x_part3 3.2), and Bregman pairings. Pinning the ~log(1/s) values of the scale-dependent carriers
in the band would need a quantitative tail-independence of T (N2 3.7(c)): OPEN.

## 5.5 Which mates admit regime (i) (two-sided small-scale structure at an engineered f'). Classification.
Let g in C(f), a in c_00 (finite I). Regime (i) at scale s can be supplied, at cost eps = O(s), for a component of g carried at scales <= s by:
 (1) base contacts or near-contacts (window masses / small shifts of z'_j; P2x_part3 Step 4) — YES;
 (2) finitely many fixed off-peak carriers of w (already two-sided within their box) — YES;
 (3) degenerate peaks (alpha_k = 0) used one-sidedly — YES after one scalar tuning each (P2x_part4 4.4(b), SKETCH);
 (4) weak non-degenerate peaks, super-near-threshold carriers (summable gaps), off-peak carriers whose depth grows as t -> 0 — only by conversions
     (5.3), whose perturbation destroys the transfer of the other scale-dependent carriers in the band (5.4): NO with the present tools.
Regime (ii) must transfer both sides on [s, ~sqrt(s)]; by 5.4 this holds for robust decompositions.
**Answer to the task's question.** (ii)/(i) can be supplied exactly for mates which, on each side, have decompositions near 0 using only robust structure:
one-sided linear decompositions (two-piece data, arbitrary contact splitting, contacts on both sides, fixed carriers pushed beyond their gap at
fixed scales) — Theorem 3.5 with (H2) Delta d_m >= 0 and (TC), or pinning when Delta d_m < 0 (4.1). "Finitely generated" switching (carriers in a fixed finite set,
base parts varying with t) should go through the same proof with Prop 2.6(b) for the base and a per-piece convexity sign condition
sign(t)(d_t - d_ref) <= 0 (SKETCH, not written). Switching through scale-dependent BLOCK carriers on either side is not covered.

## 5.6 The exact residual class (relative to all recovery mechanisms now available). 
For f in S_{p_N*}, call g in C(f) COVERED if one of the following holds (recovery along engineered sequences depends on g, so convex combinations
of covered mates are not automatically covered — only (C1) is a closed convex set recovered along every sequence):
 (C1) g in cl Cert^sh(f) (A: transport along every sequence; includes Theorems W, L, averaging class, weighted averaging P1 4.3-4.4, C Thm 7.1/7.4);
 (C2) g is locally split (D Thm 11.6);
 (C3) g has two-piece data with finitely supported off-peak carriers, a in c_00, (H1), Delta d_m >= 0 for all m, and (TC) (P2x Thm 3.5, PROVED);
      or one active block, Delta d = 0 and a pull reservoir (N2 Thm 1, PROVED there);
 (C4) [SKETCH-level] as (C3) with a not in c_00, with bounded infinitely supported carriers with near-peak decay, with degenerate-peak carriers,
      with Delta d_m < 0 at block-tame blocks with robust window peaks (pinning), or with pulls and Delta d > 0.
RESIDUAL (not covered by any PROVED mechanism; the candidates for a counterexample live here):
 (R1) two-piece mates with some Delta d_m < 0 in a block with infinitely many strict non-peaks (pinning needs quantitative tail independence);
 (R2) two-piece mates where (TC) fails and the pull reservoir comparison fails (T-dependent);
 (R3) SCALE-DEPENDENT SWITCHING: mates with no one-sided linear (or finitely generated) decomposition near 0 on at least one side, even modulo
      cl Cert(f), whose one-sided resources at scale t include block carriers of depth -> infinity as t -> 0: weak non-degenerate peaks,
      super-near-threshold carriers with summable gaps (P1 4.4 Rem), deep off-peak carriers at generic f (Q_m infinite). Here the precision obstruction
      5.4 applies to every scheme based on window masses or conversions;
 (R4) infinitely many blocks (avoided by Remark martin-tail).
No element of (R1)-(R3) is known to exist outside cl NA; no argument here produces a counterexample (every obstruction above is an obstruction to a
METHOD: cancellations in f' - f and other decompositions are not excluded).
