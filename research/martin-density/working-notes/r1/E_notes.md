# Notes E — Strategy (E): adversarial search for a counterexample to density of NA((c_0,p), l_2^2)

Author: strategy-E agent, 2026-10-08. Setting: canonical base, Martin-type norm p = q + ||L.||_V (finite block set
unless said otherwise; Preprint B Remark martin-tail reduces Martin's norm to the p_N). Files read: BRIEFING.md,
residual_recovery.tex (Preprint A), hmr_c0_renormings.tex (Preprint B), G_notes §3.8-3.10 and §6.6, and the round-1
notes A_notes, D_notes, G_referee (I rely on A_notes §4 certificate machinery, marked as imported).
arXiv (Martin 2406.07273, KLMW 1905.08272) and Martin's homepage were UNREACHABLE (proxy 403 / DNS); I used only the
description of Martin's T in Preprint B (M1)-(M7).
Status labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN / NUMERICAL (= numerical evidence in an explicit cost model).

## Bottom line

No counterexample. Every natural mechanism I could construct either dies (with an identified recovery mechanism) or,
in one case, survives only inside an idealized cost model under a long list of unverified adversarial design conditions.
New rigorous results:
 * Averaging Criterion (Theorem 5.1, PROVED mod A_notes Prop 4.5): if a mate g of f can be approximated at EVERY small
   scale s by a finite certificate of radius >= s with error O(s) (any constant), then g is in cl Cert(f), hence
   recovered along every sequence. Corollary 5.2 (PROVED): "critical-rate" cross mates carried by off-peak (two-sided)
   coordinates are recoverable — the danger zone flagged by A_notes 7.3 / D_notes 12.6 is NOT an obstruction for
   two-sided resources; A_notes 7.4 (box tails of exact order sigma) is settled the same way (SKETCH).
 * Structural lemmas (PROVED): duality lemma and "destroyed implies convertible" (Lemma 6.1, Cor 6.2); impossibility of
   exactly collinear tails (Lemma 6.3); a single far detector can be neutralized (Lemma 6.4, first part); window moves
   must be o(1) along NA approximants (Prop 8.2, from (F1)/Prop 3.9); rigidity of two-sided certificates at NA points
   (part 2.2, from A_notes Prop 7.4).
Recovery mechanisms identified (SKETCH): T1 eta-trick at contacts of f; T2 multi-scale averaging of frozen
certificates; T3 conversion of destroyed resources through their own far tails (destruction-conversion duality);
T4 eta-trick on the frozen error's support + side switching (kills slow cross mates with one-sided near-contact
errors, candidate NC).
Residual loophole (part 7, HEURISTIC/OPEN): one-sided (peak) carriers of a core direction at all scales, error-dominated
costs, and a "rigid" T whose far tails are nearly collinear inside long detector groups. In Model N the boundary excess
is R(J) = 1.194, 1.043, 1.0093, 1.0017 for J = 1..4 converted scales (delta = 1; 1.180, 1.037, 1.006 for J = 1..3 at
delta = 2): positive for every bounded J, tending to 1 as J grows. Whether an approximant
always has unbounded conversion capacity or cheap carriers for frozen errors (part 7.5) is OPEN; I give concrete
counter-strategies (C1)-(C3) that an adversary would have to block, and I could not certify any consistent design.
Leaning: POSITIVE for Martin's own (presumably generic) T; the question might in principle depend on T.

## Status table (all claims)

| # | Claim | Status | Where |
|---|---|---|---|
| 1 | Necessary conditions for a counterexample (f non-NA, not in Omega, g not in cl Cert^sh, scale-dependent decompositions, all approximants of form (F1)) | PROVED (collection) | 1.1 |
| 2 | Critical cross mate with destroyed fine coordinates exists at suitable f (construction) | SKETCH | 1.2 |
| 3 | Single frozen coordinate recovers only up to a boundary factor ~2 | NUMERICAL (Model M) | 1.3 |
| 4 | Multi-frozen geometric averaging removes the boundary excess: R(J) = 2.0, 1.27, 1.08, 1.007, 1.0008, 1.0000 (J = 1,2,3,5,8,12) | NUMERICAL (Model M) | 1.3 |
| 5 | Two-piece mates over infinite contact sets are recovered (eta-trick + truncation) | SKETCH | 1.4(i) |
| 6 | Averaging skeleton: convexity bound p*(f'+t g') <= 1 + Q t^2/2 + kappa |t| sum_{s_j<|t|} w_j s_j | PROVED | 2.1 |
| 7 | Rigidity: one-sided resources cannot form a two-sided linear certificate at an NA point | PROVED (from A_notes 7.4) | 2.2 |
| 8 | One-sided cross mates: conversion bands via the scalar v(x') | SKETCH | 2.4 |
| 9 | Candidate NC (slow cross, near-contact errors) is a mate at f | SKETCH | 3.1 |
| 10 | NC is recovered (T4: eta on frozen error support + side switching) | SKETCH (high confidence) | 3.2 |
| 11 | Model N: one shift R = 2.82 (delta=1); two coincident shifts R = 1.031; best scanned 1.0021 (delta=1), 0.9987 (delta=2, fine scan); group transitions R ~ 1 (a0 = 0.3) | NUMERICAL | 4.2-4.4 |
| 12 | Theorem 5.1 (Averaging Criterion for cl Cert(f)) | PROVED (mod A_notes P4.5, L4.2, L4.7, C4.11) | 5 |
| 13 | Corollary 5.2 (critical two-sided cross mates in cl Cert(f)), case g_0 = 0 | PROVED (same imports) | 5 |
| 14 | A_notes §7.4 borderline box tails are in cl Cert(f) | SKETCH | 5 |
| 15 | Lemma 6.1 (duality), Cor 6.2 (destroyed => convertible, with guards) | PROVED | 6 |
| 16 | Lemma 6.3 (no exact collinearity of tails) | PROVED | 6 |
| 17 | Lemma 6.4 (single detector neutralizable; need for infinitely many groups) | PROVED (first part) / HEURISTIC (consequence) | 6 |
| 18 | Error-dominated Model N (a0 = 0.03): R(J) = 1.194, 1.043, 1.0093, 1.0017 (J = 1..4 converted scales, delta = 1); 1.180, 1.037, 1.006 (J = 1..3, delta = 2); two groups at delta = 1 can convert 3 scales (R = 1.017); excess located a few octaves above the band (frozen-error absorption) | NUMERICAL | 7.4 |
| 19 | Rigid design (A1)-(A5) gives bounded conversion capacity and a model-level obstruction | HEURISTIC / OPEN (consistency unverified; counter-strategies C1-C3 not excluded) | 7.3-7.5 |
| 20 | Gordan equivalence for the sign obstruction (A3) | PROVED (Gordan's alternative) | 7.3 |
| 21 | Prop 8.2: along NA approximants window moves are o(1); only absolute shifts act on fine resources | PROVED (statement) / SKETCH (consequence) | 8 |
| 22 | My earlier claims "deep peaks do not matter" and "individual window conversions are cheap" | FALSE (corrected) | 8.1, 7.2(iv) |
| 23 | Density of NA((c_0,p), l_2^2) | OPEN (leaning positive) | 9 |


---

# E notes, part 1: framework for an adversarial search; first candidates and how they die

Status labels: PROVED / SKETCH / HEURISTIC / FALSE / OPEN / NUMERICAL (numerical evidence in an explicit model).

## 1.0 Setting (finite block set I unless said otherwise)

X = c_0, q*(a) = ||a||_1 + ||U*a||, p = q + ||L.||_V, blocks m with lambda_{k,m} = m Phi_m(k), u_{k,m} in S_{q*},
N_m(w) = ||w||_inf + ||D_m w||_2. For f in S_{p*}: normer xi, q_0 = q**(xi), forced decomposition f = a + L*w,
xhat := xi/q_0 = z + U e, e = U*a/||U*a||, z in B_{l_inf}, z = sign a on supp a.
Budget identity (A_notes Lemma 7.1): for an admissible decomposition f + t g = A_t + L* W_t,
  q_0 E_q(A_t) + (1-q_0) sum_m pi_m e_m(W_{t,m}) <= s(t) - 1,  s(t) = sqrt(1+t^2).
Base first-order excess of a + tB: sum_{j notin supp a} (|tB_j| - z_j t B_j) (plus flips and Hilbert terms).

Facts imported (all PROVED in the r1 notes, re-checked by me where used):
(F1) [G_referee 4.7] f'_n in NA cap S_{p*} tends to f iff f'_n = grad p(z'_n + U(U*a'_n/||U*a'_n||)) with
     a'_n in c_00 cap S_{q*}, a'_n -> a in l_1, z'_n in B_{c_0}, z'_n = sign a'_n on supp a'_n, z'_n -> z coordinatewise.
(F2) [Preprint A Thm 2.1; A_notes 3.1] C(f) compact, f -> C(f) upper semicontinuous.
(F3) [A_notes Cor 3.3] (f, rho g) in cl NA for all g in C(f), rho<1  iff  C(f) is contained in Li_n C(f'_n) for
     some NA sequence f'_n -> f.  A counterexample = (f, g in C(f), rho<1, delta>0) with dist(rho g, C(f')) >= delta
     for every NA f' with ||f'-f|| < delta.
(F4) [A_notes Thms 4.10, 4.17, 6.2, 6.5] every mate in cl Cert^sh(f) (finite/shifted/weighted certificates,
     locally admissible linear decompositions) is recovered along EVERY sequence f_n -> f.

## 1.1 Necessary conditions for a counterexample (PROVED, by collecting the above)

If (f, g, rho) is a counterexample then:
 (N-a) f is not NA, f is not in the residual set Omega of Preprint A, and C is not lower semicontinuous at f.
 (N-b) g is not in cl Cert^sh(f): g has no locally admissible linear decomposition, is not a weighted direction, etc.
 (N-c) [A_notes Prop 7.4] g has no pair of one-sided linear decompositions whose difference is in c_00
       (in particular, if supp a cup K is finite, K = contact set, g has no one-sided linear decompositions on both sides).
 (N-d) Every NA f' near f has the form (F1); so a counterexample must defeat EVERY choice of (a', z'), including the
       completely free far coordinates of z'.
So the decompositions of f + t g must be genuinely scale dependent (A_notes 7.2: mechanisms N1-N4).

## 1.2 The "critical cross mate" candidate and its natural destruction mechanism

Single block, a in c_00, j notin supp a with |z_j| < 1 (two-sided base kink; the base cannot carry e_j* at
first order on either side, and z'_j must stay close to z_j for f' close to f, so the eta-trick of A_notes 8.3 is
not available at j: for fixed j, z'_j = +-1 forces ||f'-f|| >= delta_j > 0).
v := (e_j* - xhat_j a)/norm, so v(xi) = 0. Cross coordinates k_i (i = 1,2,...) with geometric lambda_i and
   u_{k_i} = (v + K lambda_i sigma_i)/n_i,   sigma_i(xhat) = 0,
where sigma_i = avg_{B_i} e* - c_i e_{j_0}*, j_0 in supp a, B_i far disjoint blocks with z = 1/2 on B_i (so xhat is
not in c_0). At f: u_{k_i}(xi) = 0, so every k_i is off-peak with w(k_i) = 0 and full gap M.
Mate g = c v: at scale t carry t c v through k_i with lambda_i ~ |t| c/M; base absorbs t c K lambda_i sigma_i at
first-order cost ~|t| c K lambda_i = O(t^2); block Hilbert cost t^2 c^2/(2C). For c small enough g in C(f). (SKETCH;
the computation is the one in A_notes 7.3 / D_notes 12.2.)

Destruction at NA approximants (SKETCH, elementary): for x' = z' + U e with a' = a and z' = z on a window,
sigma_i(x') = avg_{B_i}(z' - z) -> -1/2 as i -> infinity because z' in c_0. Hence u_{k_i}(x') ~ -K lambda_i/2 and,
if K/2 exceeds the block threshold constant, all but finitely many k_i are PEAKS of w' (with w'(k_i) = -M').
So at every NA f' near f the cross mechanism is available only down to a finite scale lambda_I (I chosen by the
approximant through the window), and below lambda_I the fine cross coordinates are gone on at least one side
(deep peaks with w' = -M serve only t>0 one-sidedly; on t<0 nothing).
This is the cleanest "lack of lower semicontinuity" I could build: the structure exists at all scales at f
and is truncated at a finite scale at every f'.

## 1.3 How it dies: the (multi-)frozen representation trick

Single frozen coordinate (SKETCH): put g' := rho c n_I u_{k_I} (an exact block vector at the finest available
off-peak coordinate). Then g' - rho g = rho c K lambda_I sigma_I -> 0, at scales |t| <= M lambda_I/(rho c) g' is
carried exactly by k_I (finite certificate, two-sided), and at larger scales the transferred cross mechanism of f
plus absorption of rho c K lambda_I sigma_I works. Cost bookkeeping shows the absorption roughly DOUBLES the
error part of the cost at scales ~ lambda_I, so a single frozen coordinate recovers only rho^2 < 1/(boundary factor).

Model M (NUMERICAL). Isolate the critical cross mechanism: coordinates i with lambda_i = r^i, at scale tau,
  P(tau) = min_x sum_i [ A |eta_i - lambda_i x_i| / tau + B x_i^2 ]   s.t. sum x_i = S, |x_i| <= M lambda_i/tau,
(A = q_0 K error weight, B = (1-q_0)/(2C) Hilbert weight; mate condition P <= 1/2 at all scales; two-sided symmetric).
At f: all i, eta = 0, S = c.  At f': only i <= 0 (lambda_i >= 1), eta = lambda_i x^fr_i free (frozen representation
g' = rho c v + K sum_i x^fr_i lambda_i sigma_i, sum x^fr_i = rho c).  Scaling: sup_tau P is 2-homogeneous in S, so the
relevant number is the boundary ratio R(J) = min over frozen data on J coordinates of sup_tau P_{f'} / sup_tau P_f.
Results (r = 1/2, M = 1/2; four (A,B) pairs, all consistent):
  J = 1: R ~ 2.00;  J = 2: R ~ 1.27;  J = 3: R ~ 1.08;  J = 5: R ~ 1.007 (Nelder-Mead);
  geometric ansatz x^fr_i proportional to 0.6^{-i} on the J finest available coordinates (finest gets most):
  J = 8: R = 1.0008;  J = 12: R = 1.0000 (to 4 digits), scale window tau in [2^-12, 2^30].
Conclusion (HEURISTIC for Martin's norm, NUMERICAL in Model M): the boundary layer created by truncating the
fine cross coordinates can be made to cost an arbitrarily small factor by spreading the frozen representation
geometrically over many available coordinates. Hence for every rho < 1 the truncated structure recovers rho g.
Mechanism that kills the candidate: MULTI-SCALE FROZEN REPRESENTATION (a geometric "partition of unity in scale"
for the block coefficients, finest coordinate heaviest). Scripts: E_work/modelM.py, modelM_opt.py, modelM_opt2.py.

## 1.4 Other natural candidates already dead (SKETCH arguments)

(i) Two-piece mates over an infinite contact set K (A_notes Remark 7.6): g = y_+ + b_F = -y_- + b_F + L*W with
    y_+- z-signed on K. Killed by the eta-trick at the contacts K cap [1, N'] (contacts of f, so z'_j = z_j = +-1 is
    compatible with (F1)) combined with truncation of the far part: base two-sided for |t| <= eta, one-sided linear
    decompositions transferred for |t| in [tau'/c, T_0] with tau' = ||y|_{>N'}||_1 << eta.
(ii) Cross mates through ONE-SIDED carriers (near-threshold peaks of both signs, P+ for t<0, P- for t>0): a single
    frozen coordinate is one-sided, so 1.3 fails as stated; killed instead by CONVERSION of a near-threshold peak k* into
    an off-peak coordinate at f' (shift u_{k*}(x') by ~theta Phi(k*) through the far tail of u_{k*}, or by an ABSOLUTE
    shift of all v-carriers through v(x') / Delta a), after which 1.3 applies. [Correction, see part 8: individual
    conversions through WINDOW coordinates are NOT available along NA approximants, since window moves must be o(1)
    (Prop 8.2); only far tails and absolute shifts remain.] Whether enough conversions are always available is the
    subject of parts 4 and 7; in the error-dominated regime this is OPEN.


---

# E notes, part 2: the averaging (multi-frozen) principle, one-sided resources, conversion

## 2.1 Averaging Lemma (SKETCH; the abstract skeleton is PROVED, the hypotheses are the issue)

Skeleton (PROVED, elementary convexity). Let f' in S_{p*}, rho in (0,1), gbar in X*, and let h_1,...,h_J in X*,
weights w_j >= 0 summing to 1, scales 0 < s_1 < ... < s_J, constants kappa, Q >= 0 such that
 (i)  p*(f' + t h_j) <= 1 + Q t^2/2                for |t| <= s_j        (h_j is a two-sided local certificate);
 (ii) p*(f' + t gbar) <= 1 + Q t^2/2               for s_1 <= |t| <= T_0  (transfer regime);
 (iii) p*(h_j - gbar) <= kappa s_j                 (frozen error is of the order of its scale).
Then g' := sum_j w_j h_j satisfies, for every |t| <= T_0,
   p*(f' + t g') <= 1 + Q t^2/2 + kappa |t| sum_{j : s_j < |t|} w_j s_j ,
and for |t| <= s_1 simply p*(f' + t g') <= 1 + Q t^2/2.
Proof: p*(f' + t g') <= sum_j w_j p*(f' + t h_j) (convexity, sum w_j = 1). For j with s_j >= |t| use (i). For
j with s_j < |t| (so |t| >= s_1) use p*(f' + t h_j) <= p*(f' + t gbar) + |t| p*(h_j - gbar) and (ii), (iii). QED.
With w_j = 1/J and geometric s_j = s_1 2^{j-1}: kappa |t| sum_{s_j<|t|} s_j/J <= 2 kappa t^2/J.
So if Q <= rho^2 (+o(1)) and J >= 4 kappa/(1-rho^2), then p*(f' + t g') <= 1 + t^2/2 <= s(t) on |t| <= T_0 (up to the
standard quartic correction), and the slack (A_notes Lemma 4.7) handles |t| >= T_0 once ||g' - rho g|| and
||f' - f|| are small. ||g' - gbar|| <= kappa sum_j w_j s_j <= 2 kappa s_J / J.

This is exactly what Model M (part 1) found numerically: the boundary excess decays like 1/J.

What has to be supplied in Martin's setting (the hypotheses):
 (H-transfer) gbar ~ rho g satisfies (ii) at f' on [s_1, T_0]: needs the structure of f at scales >= s_1 to be
   matched at f' (finitely many block coordinates, window choice; A_notes 8.1, (F1)) and the contribution of the
   UNMATCHED fine coordinates (scales <= lambda_0) at scale t to be O(delta) with delta = lambda_0/s_1 (geometric
   Phi): choose s_1 = lambda_0 * C/(1-rho^2). HEURISTIC (bookkeeping of first-order Hilbert mismatch not written).
 (H-cert) two-sided certificates h_j at the scales s_j with p*(h_j - rho g) = O(s_j): REQUIRES TWO-SIDED RESOURCES
   at f' near the scales s_j. This is the crux.

## 2.2 Why two-sided resources are indispensable at NA points (PROVED, from A_notes Prop 7.4)

At an NA point f' (a' in c_00, z' in c_0, contact set K' finite), suppose h = B+ + L*Om+ = B- + L*Om- where
(B+, Om+) is admissible for 0 < t <= r and (B-, Om-) for -r <= t < 0, both with zero first-order base excess
(B+- supported in supp a' cup K', with the contact signs). Then B+ - B- in c_00 cap Y = {0}, so B+ = B-, Om+ = Om-.
Consequently, if Om+ is supported on peaks of w'_m used "downwards" for t>0 and Om- on peaks used downwards
for t<0 (disjoint sets), both vanish. So one-sided block resources (peaks, near-peak off-peak coordinates used in
their long direction) can NEVER be combined into a two-sided linear certificate at an NA point: the frozen
certificate must use genuinely two-sided resources (off-peak coordinates within their symmetric room, supp a').

## 2.3 The refined candidate: one-sided resources of both signs at all scales

f carries the v-component of g at every scale by near-threshold PEAKS: P+ (w = +M, serve t<0, carry positive
multiples of u_k) and P- (w = -M, serve t>0), at all scales, with good approximation rates u_k ~ v, and NO
off-peak coordinate approximating v. At NA approximants: matched down to lambda_0, destroyed below (deep -M
peaks if the far tails see z = 1/2 on far blocks). By 2.2, the frozen certificate needs two-sided resources.

## 2.4 How it dies (SKETCH): conversion bands through the scalar v(x')

v = (e_j* - xhat_j a)/norm has v(xhat) = 0 and is c_00. The scalar v(x') is freely adjustable at f' by tiny window
moves (delta_j at the non-contact coordinate j) or by Delta a (U*v has a component orthogonal to e by injectivity of
U*). Writing u_k = (v + K lambda_k sigma_k)/n_k, the relative position of k is
   rho_k(x') = v(x')/(K lambda_k) + sigma_k(x'),   off-peak iff |rho_k| < theta~ (threshold, rescaled).
If the near-threshold P+ resources have sigma_k(xhat) = theta~(1+delta), the shift v(x') = -K Lambda_0 theta~(1+delta)
gives rho_k = theta~(1+delta)(1 - Lambda_0/lambda_k), so ALL P+ resources with
lambda_k in ( Lambda_0 (1+delta)/(2+delta), Lambda_0 (1+delta)/delta ) (a band of scale ratio (2+delta)/delta) become
OFF-PEAK (two-sided), with full gap at lambda_k = Lambda_0, while P- become deeper peaks and everything far below
Lambda_0 becomes a deep peak.
One scalar therefore creates a whole BAND of two-sided resources, which is what 2.1 needs. Cost: ||Delta f'|| =
O(K Lambda_0) (only coordinates at scales <~ Lambda_0 change status). The coarse structure is shifted by relative
amounts K Lambda_0/lambda_k, negligible above the band.
Caveat (open in this part): inside the band the t<0 room of the converted P+ resources drops from 2M (one-sided)
to M (symmetric), so the band's own cost profile is worse than f's by a constant factor; for small delta the band
is wide. Whether the averaging still closes is tested numerically in part 4 (Model N).


---

# E notes, part 3: candidate NC (slow cross coordinates, one-sided near-contact errors) and its death

## 3.1 The candidate (construction SKETCH; mate property SKETCH with all terms checked)

Single block. a in c_00, F = supp a, j notin F with z_j = 0. Near-contacts: far coordinates l in NC with
z_l = s_l (1 - gamma_l), s_l = +-1, gamma_l decreasing to 0 (so z is not in c_0). v0 := e_j* - xhat_j a (v0(xhat) = 0).
Cross coordinates of two types at every scale lambda_i (geometric):
   u_P = (v0 + y_P - y_P(xhat) a)/n_P,  y_P = -Z_P;   u_N = (v0 + y_N - y_N(xhat) a)/n_N,  y_N = +Z_N,
Z_P, Z_N >= 0 in the z-signed sense (Z_l s_l >= 0), ||Z||_1 = eps_0 FIXED (slow rate!), supports in near-contacts
with gamma_l <= c_gamma lambda_i, pairwise DISJOINT supports (no P/N cancellation), plus negligible Y-tails.
F-compensation gives u(xhat) = 0: every cross coordinate is off-peak with w = 0 (full gap M) at f.
Design constraint: no coordinate approximates v0 at a fast rate; every coordinate with j-mass carries errors of size
>= eps_0 * (j-mass) on near-contacts.

g = c v0 is a mate for small c (SKETCH, all terms checked): at t>0 carry t c n u_{P(t)} (lambda_{P(t)} ~ t c/M, box ok,
block Hilbert c^2 t^2/(2C)), the base absorbs t c Z_{P(t)} + (multiple of a): first-order excess
sum_l gamma_l t c Z_l <= c_gamma lambda t c eps_0 = O(t^2), B(xhat) = 0, Hilbert part of the base small (far support).
t<0 symmetric with N. Global condition by smallness of c.

Why the earlier recovery tricks fail:
 * frozen certificate: any two-sided block combination near rho c v0 carries a frozen error
   h = rho c sum_k beta_k y_k with ||h|| >= rho c eps_0 (disjoint supports): not close to rho g.
 * eta-trick on the frozen error up to the slack scale T_0 = sqrt(6 eps/(1-rho^2)) costs eps >= T_0 rho c eps_0,
   forcing T_0 >= 6 rho c eps_0/(1-rho^2): not small.
 * rigidity at NA points (part 2.2): the finest scales need a single two-sided linear representation.

## 3.2 How it dies: eta-trick ON THE FROZEN ERROR + SIDE SWITCHING (SKETCH; new mechanism T4)

At f' choose a matched window down to scale lambda_I (cross coordinates and their near-contacts matched), pick ONE
N-type coordinate N* at scale lambda_{N*} ~ 2 lambda_I, make the head of supp Z_{N*} EXACT contacts (z'_l = s_l; cost
~ gamma_l * influence(l), tiny) and put eta-masses a'_l = eta_l s_l there with eta_l = kappa |Z_{N*,l}|,
kappa = M lambda_{N*}/n. Define
   g' := rho c n_{N*} u_{N*} + B_0,   B_0 := -rho c Z_{N*}^{head}   (so g' = rho c v0 + rho c Z_{N*}^{tail}, close to rho g).
Decompositions of f' + t g':
 (a) |t| <= M lambda_{N*}/(rho c n): block carries t rho c n u_{N*} (off-peak, box ok, two-sided); base absorbs t B_0 on
     the eta-contacts: for t<0 it increases |a'_l| (no cost), for t>0 no flip while t rho c |Z_l| <= eta_l. Two-sided.
 (b) t < 0 beyond (a): carry via N(t) (matched); base absorbs |t| rho c Z_{N(t)} (cheap) - |t| rho c Z_{N*}^{tail}
     (wrong sign, cost ~ 2|t| rho c ||Z^tail||, fine once ||Z^tail|| << lambda_{N*}).
 (c) t > 0 beyond (a): SWITCH to the P-type mechanism of f: carry via P(t) (matched, lambda_{P(t)} >= lambda_{N*});
     base absorbs t rho c (Z_{N*}^{tail} + Z_{P(t)}), both z-signed, cheap. The eta-coordinates are untouched.
 (d) |t| >= T_0: slack.
||a' - a|| ~ kappa eps_0 = O(lambda_I): f' -> f as lambda_I -> 0. Hence rho g is recovered.
Principle (T4): one-sided base errors of a frozen representation are cancelled by eta-masses only up to the scale of
the finest matched one-sided structure; above it each side switches to f's own one-sided mechanism for THAT side.
The eta budget is (finest matched scale) x (error mass), not (slack scale) x (error mass).
Requirements used: both P- and N-types matched down to lambda_I (true by windowing), near-contacts of f can be
made exact contacts at f' (true: the needed ones have gamma_l <= c_gamma lambda_I, influence small).
Remaining bookkeeping (not written): the change of e' caused by the eta-masses (compensable by finitely many linear
conditions on Delta a or window moves), g'(x') = 0 normalization, Hilbert terms. Status: SKETCH, high confidence.

## 3.3 Consequence for the search

After T1 (eta-trick), T2 (averaging), T3 (conversion: destruction and convertibility come from the same far tails),
T4 (frozen error cancellation + side switching), the only remaining place for an obstruction is:
CORE mass (window coordinates with |z| bounded away from 1, where neither eta-tricks nor contacts are possible) that is
carried at f, at every scale, only by ONE-SIDED BLOCK resources (near-peak coordinates used in their long direction),
whose conversion at f' is possible only in BOUNDED BANDS of scales (e.g. if the tails of all resources of a long scale
range are collinear beyond every window, so that one scalar controls a whole group). Then the averaging lemma has only
J_max two-sided scales and the boundary excess R(J_max) > 1 may survive. Tested in part 4 (Model N).


---

# E notes, part 4: Model N (one-sided resources, conversion bands) — the only surviving signal

## 4.1 The model (precise definition; all results here are NUMERICAL in this model)

Resources i with scale lambda_i = r^i and relative position rho_i (|rho|<1: off-peak, block value w = M rho;
rho >= 1: peak w = +M; rho <= -1: peak w = -M). At signed scale t = sigma tau, carrying x_i (units of v) moves
the coordinate to w_i + sigma x_i tau/lambda_i, which must stay in [-M, M]; at a peak only inward moves are allowed
and they cost a0 lambda_i |rho_i| |x_i| / tau (first-order peak cost alpha_i |t Omega_i| with alpha_i ~ lambda_i Phi_i |rho_i|).
Core error cost A |eta_i - lambda_i x_i| / tau (eta = frozen error), Hilbert cost B x_i^2. Profile
P(tau, sigma) = min_x sum_i [...] s.t. sum x_i = S. Mate condition P <= 1/2 on both sides; 2-homogeneous scaling.
At f: two resources per scale, P+ (rho = 1+delta, serves t<0) and P- (rho = -(1+delta), serves t>0): one-sided
near-threshold peaks of both signs at ALL scales (margin delta).
At f': a shift moves positions, rho -> rho -+ s/lambda (an ABSOLUTE shift of u_k(x') of size s theta, which is what
window moves, Delta a and collinear far tails produce): coarse resources unchanged, a BAND of resources becomes
off-peak (two-sided), finer resources become deep peaks (cost ~ a0 s, useless at small scales).
Frozen certificate: weights x^fr on band resources (eta_i = lambda_i x^fr_i), optimized (the outer problem is convex
in x^fr, Nelder-Mead). R := min sup_{tau,sigma} P_{f'} / sup P_f (independent of the mate size c).
Parameters used: r = 1/2, M = 1/2, A = 1, B = 1/2, a0 = 0.3. Scripts: E_work/modelN.py, modelN_run*.py, modelN_scan.py.

## 4.2 Results

ONE shift parameter (converts one type only; the other type is pushed deeper):
   delta = 1: band J = 1, R = 2.82;  delta = 0.3: J = 3, R = 1.17;  delta = 0.1: J = 4, R = 1.055.
TWO independent shifts (P+ shifted down, P- shifted up), band centres s+, s- (in units of (1+delta)):
   delta = 1: (1,1): J = 2, R = 1.031 (best of the 3x3 scan); (0.75,0.75): 1.051; (1,1.3): 1.048; (1,0.75): 1.118.
   delta = 0.3: (1,1): J = 6, R = 1.005.
Full 3x3 scan of band centres (s+, s-) in {0.75, 1, 1.3} x (1+delta):
   delta = 1: best R = 1.0021 at (1.3, 1.3) (two converted scales per type, J = 4); (1,1): 1.031.
   delta = 2: best R = 1.0009 at (1, 1) (J = 2); off-centre choices are much worse (up to 3.35).
   delta = 0.3, centred (1,1): R = 1.005 (J = 6).
Interpretation: once BOTH types are converted at the same scale(s), the boundary excess is at most a few tenths of a
per cent in this model. Deeper margins do not help the adversary: conversion also REMOVES the first-order peak cost
a0 lambda (1+delta) of f's one-sided carriers, which compensates the lost fine structure. The excess decreases with the
number of converted scales (cf. Model M, part 1: R -> 1 as J -> infinity).

## 4.3 What an actual obstruction would need (HEURISTIC analysis)

A counterexample along these lines needs, at EVERY NA approximant, only boundedly many independent conversion
parameters near the boundary of the matched structure, with deep enough margins (delta of order 1), and a mate that is
tight (cost profile at the budget at all scales). Then rho^2 > 1/R excludes recovery. Obstacles found:
 (O1) Destruction-conversion duality (SKETCH, general): a resource k destroyed at f' has a heavy far tail,
      ||u_k|_{>W}||_1 >= c Phi_k; after enlarging the window so that matched guards have tails << their tolerances,
      moving z' on the far support shifts u_k(x') by ~||u_k|_{>W}|| without disturbing any guard. So destroyed
      resources are always adjustable by the amount that destroyed them.
 (O2) Exact collinearity of far tails inside a group is IMPOSSIBLE: if u_k|_{>W} = c_k psi|_{>W} for all W >= W_0, then
      u_k - (c_k/c_k') u_k' is in Y cap c_00 = {0}, contradicting injectivity of T (PROVED; uses only Y cap c_00 = {0} and
      injectivity). Tail independence (A_notes Fact F(b), PROVED) gives linear independence of any finitely many
      restrictions u_k|_{[N,inf)}; only QUANTITATIVE near-collinearity (condition numbers) can limit the parameters.
 (O3) Nested-window designs (heads of group n+1 inside the window of group n, far detector psi_n shared in group n)
      still leave a cut W through the heads of the group just below the boundary, which are then individually
      adjustable (SKETCH). To block this, every resource would have to be, up to << Phi_k, a combination of coarser
      resources; this destroys the l_1-independence of the critical errors that the adversary needs elsewhere (HEURISTIC).
 (O4) One-sided O(1) detector errors force P+ and P- to have opposite detector coefficients (part 3 sign analysis),
      which gives at least two independent shifts (the v-direction shift and the detector scalar): R ~ 1.03 at best.
 (O5) At group transitions the approximant gets the scalars of two groups plus the v-shift (three parameters).
Conclusion for COMPARABLE peak and error costs (a0 = 0.3; HEURISTIC, moderate confidence): the bounded-parameter
loophole yields at most ~0.1-0.5 per cent boundary excess in the idealized model once band centres are optimized (a few
per cent for badly placed bands), and is attacked from several sides. CAVEAT (found later, part 7): in the
ERROR-DOMINATED regime the excess with a bounded number of converted scales is larger (R(2) = 1.043) and does not vanish.
It is, however, the precise point where a positive proof must show that "enough" two-sided resources can be created at
the boundary of the matched structure (a quantitative tail-independence statement).

## 4.4 Group transitions close the loophole in Model N when peak costs matter (NUMERICAL)

Script E_work/modelN_groups.py: both types converted at g adjacent scales (one detector-group scalar per scale,
opposite P+/P- coefficients, which is exactly what a boundary placed at a transition between detector groups gives):
   delta = 1: g = 2 (J = 4): R = 1.0000 (room-weighted 1.0058);  g = 3 (J = 6): R = 0.9999.
   delta = 2: g = 1 (J = 2): R = 1.0022;  g = 2 (J = 4): R = 0.9999.
(Values below 1 are scale-grid discretization, ~1e-4.) So two adjacent converted scales already remove the boundary
excess in the model.

Why an approximant always has a group transition available (SKETCH): destruction of resources at all fine scales at
EVERY NA approximant needs detectors reaching beyond every window; a single far detector psi in l_1 can be neutralized by
one scalar condition (choose z' beyond W with psi_{>W}(z' - z) = 0), after which nothing is destroyed and f' carries
f's full structure. Hence infinitely many independent detector groups are needed, so transitions between groups occur
at arbitrarily small scales; scale gaps between groups would make g fail to be a mate at f (no carriers at those
scales). At a transition the approximant controls two group scalars (plus the global v-shift), i.e. it can convert
both types at two adjacent scales.

Status of the one-sided (peak) mechanism: DEAD in Model N when the first-order peak cost is comparable to the critical
error cost (a0 = 0.3 above: two converted scales give R <= 1 within 1e-3; with the fine continuous band-position scan
even ONE group gives R = 0.9987 for delta = 2). NOT dead in the ERROR-DOMINATED regime (small a0): there R(J) stays above
1 for every bounded number J of converted scales (part 7.4), and everything hinges on the conversion capacity of the
approximant (parts 7-8). All Model N statements are NUMERICAL; for Martin's norm they are HEURISTIC, because Model N
idealizes the Hilbert coupling (d-corrections, projections), multiple blocks, generic coordinates and the exact
first-order exchange between base and block budgets.


---

# E notes, part 5: the Averaging Criterion for cl Cert(f) (PROVED, given A_notes Prop 4.5 and Lemma 4.7)

Notation from A_notes §4: finite certificate c = (b, omega) at f (Def 4.1), direction g_c, coefficient H(c),
radius r(c), cubic constant kappa(c); Cert(f) = {g_c : H(c) <= 1, g_c in C(f)}.
Imported (PROVED in A_notes, I re-checked the statements):
 (P4.5) for |sigma| <= r(c): p*(f + sigma g_c) <= 1 + (sigma^2/2) H(c) (1 + kappa(c)|sigma|);
 (L4.2) c -> g_c linear; H convex and 2-homogeneous; finite certificates form a vector space;
 (L4.7) s(t) - s(rho t) >= (1 - rho^2) min(t^2, |t|)/3, s(t) = sqrt(1+t^2);
 (C4.11) every g in cl Cert(f) is recovered along EVERY sequence f_n -> f in S_{p*} (transport theorem).

## Theorem 5.1 (Averaging Criterion). PROVED (mod. P4.5, L4.2, L4.7, C4.11)

Let f in S_{p*}, g in C(f). Assume there are K_0, kappa_0 >= 0, s_0 > 0 and, for every s in (0, s_0], a finite
certificate c_s at f with
  (a) H(c_s) <= 1,  (b) r(c_s) >= s,  (c) kappa(c_s) <= kappa_0,  (d) p*(g_{c_s} - g) <= K_0 s.
Then g in cl Cert(f); hence (f, g) is in cl NA((X,p), l_2^2), and g is recovered along every sequence f_n -> f.

Proof. Fix rho in (0,1), put e1 := (1 - rho^2)/8. Choose J in N with 2 rho K_0 / J <= e1, and t_* in (0, 1] with
rho^2 kappa_0 t_*/2 <= e1 and t_*^2/8 <= e1. Choose s_J in (0, s_0] (fixed below), s_j := s_J 2^{j-J} (j = 1..J),
h_j := rho g_{c_{s_j}}, and g' := (1/J) sum_j h_j = g_{c'}, c' := (rho/J) sum_j c_{s_j} (a finite certificate, L4.2).
H(c') <= (1/J) sum_j H(rho c_{s_j}) = rho^2 (1/J) sum_j H(c_{s_j}) <= rho^2 (convexity, homogeneity).
Step 1 (|t| <= t_*). By convexity of p*, p*(f + t g') <= (1/J) sum_j p*(f + t h_j).
 - If s_j >= |t|: |rho t| <= s_j <= r(c_{s_j}), so by P4.5
     p*(f + t h_j) <= 1 + (rho^2 t^2/2)(1 + kappa_0 |t|).
 - If s_j < |t|: p*(f + t h_j) <= p*(f + t rho g) + |t| rho p*(g_{c_{s_j}} - g) <= s(rho t) + rho K_0 |t| s_j,
   and s(rho t) <= 1 + rho^2 t^2/2.
 Since sum_{j : s_j < |t|} s_j < 2|t| (geometric), averaging gives
   p*(f + t g') <= 1 + (rho^2 t^2/2)(1 + kappa_0|t|) + 2 rho K_0 t^2/J <= 1 + t^2 (rho^2/2 + 2 e1)
              = 1 + t^2 (1/2 - 2 e1) <= 1 + t^2/2 - t^4/8 <= s(t),
 using rho^2/2 = 1/2 - 4 e1, the choices of J and t_*, and sqrt(1+x) >= 1 + x/2 - x^2/8 (x >= 0).
Step 2 (|t| >= t_*). p*(f + t g') <= p*(f + t rho g) + |t| p*(g' - rho g) <= s(rho t) + |t| rho K_0 (1/J) sum_j s_j
   <= s(rho t) + 2 |t| rho K_0 s_J / J. By L4.7, s(t) - s(rho t) >= (1-rho^2)|t| t_*/3 for |t| >= t_* (t_* <= 1).
   So p*(f + t g') <= s(t) once s_J <= (1-rho^2) t_* J/(6 rho K_0) (any s_J if K_0 = 0).
Step 3. g' in C(f) and H(c') <= 1, so g' in Cert(f), and p*(g' - rho g) <= 2 rho K_0 s_J/J -> 0 as s_J -> 0.
 Hence rho g in cl Cert(f) for every rho < 1; cl Cert(f) is closed, so g in cl Cert(f). The last assertions are C4.11
 and A_notes Cor 3.3. QED

Remarks.
 * Compared with the (CA) test of A_notes Remark 4.9 (one certificate per rho with error <= (1-rho^2) r_*/6, i.e. a
   SMALL constant times the radius), Theorem 5.1 accepts ANY constant K_0, provided certificates exist at all small
   scales. The averaging over J dyadic scales divides the boundary error by J. This is the rigorous form, at f itself,
   of the Model M phenomenon (part 1).
 * Only convexity of p* and the certificate expansion are used; no NA engineering is needed: transport does the rest.

## Corollary 5.2 (critical two-sided cross mates). PROVED (mod. the same imports)

Fix a block m and v in X*, v != 0, write vhat := v/q*(v). Suppose there are off-peak coordinates k_1, k_2, ... of
w_m (at f) with lambda_i := lambda_{k_i,m} -> 0, lambda_{i+1} >= theta_0 lambda_i (theta_0 in (0,1)), gaps
gap_m(k_i) >= gamma > 0, and ||u_{k_i,m} - vhat||_1 <= K lambda_i (a CRITICAL rate: any constant K). Let c > 0 with
c^2 q*(v)^2/(m^2 C_m) <= 1 and suppose g := c v + g_0 in C(f), where g_0 = g_{c_0} for a fixed finite certificate c_0
whose block part is supported away from {k_i} and whose radius is positive, with H(c_0 + single-coordinate part) <= 1
(e.g. g_0 = 0). Then g in cl Cert(f).
Proof with all estimates: for small s let i = i(s) be the LARGEST index with lambda_i >= 2 c q*(v) s/gamma, so that
lambda_i < 2 c q*(v) s/(gamma theta_0) (geometric density). Put omega_s := (c q*(v)/lambda_i) e_{k_i}
(so R_m* omega_s = lambda_i omega_s(k_i) u_{k_i,m} = c q*(v) u_{k_i,m}); then
 r((0,omega_s)) >= min(gamma lambda_i/(2 c q*(v)), 1/(2|d_s|), C_m/(2|d_s| M_m)) >= s for s small, since
 |d_s| = Phi_m(k_i)|w_m(k_i)| c q*(v)/(m C_m) = O(lambda_i) -> 0;
 H = ||P-perp D omega_s||^2/C_m <= (c q*(v)/m)^2/C_m <= 1 (Phi = lambda/m);
 kappa = 2|d_s| M/C bounded;
 g_{(0,omega_s)} - c v = c q*(v)(u_{k_i,m} - vhat) - d_s R_m* w_m, of norm <= c q*(v) K lambda_i + |d_s| q*(R_m* w_m)
   = O(lambda_i) = O(s) because lambda_i < 2 c q*(v) s/(gamma theta_0).
Adding c_0 (fixed, positive radius) keeps (a)-(d) for s small (H of the sum: the two block parts are supported on
disjoint coordinates; the hypothesis on c_0 is used here). Apply Theorem 5.1. QED (the case g_0 != 0 is a SKETCH:
H of a sum of certificates with disjoint supports is not additive in general because of the projection P-perp;
for g_0 = 0 the proof is complete).

Consequences.
 * The "intermediate / critical regime" of D_notes 12.6 and A_notes 7.3 is NOT an obstruction when the carrying
   coordinates are off-peak (two-sided) at f: such mates lie in cl Cert(f) and are recovered along every sequence.
 * A_notes §7.4 (box tails of exact order sigma) is settled in the same way: truncations omega 1_{[1,N(s)]} at the
   level where the box holds at scale s are finite certificates with radius ~ s and error T(s) = O(s) (SKETCH: the
   uniform bound on kappa and H for the truncations is as in A_notes Theorem 6.2).
 * Hence a counterexample must use ONE-SIDED resources at f at a cofinal set of scales (peaks or near-peak
   coordinates used in their long direction, or one-sided base contacts), i.e. resources that are not certificates.
   For base contacts, T4 (part 3) applies; for block peaks, conversion at f' is needed (parts 2, 4).


---

# E notes, part 6: structural lemmas about destruction and conversion at NA approximants

Setting: f with normer xi, xhat = xi/q_0 = z + U e. An NA approximant is f' = grad p(x'), x' = z' + U e'
(F1). In this part a' = a (possible when a in c_00; otherwise add the truncation error, which only changes e' by a
norm-small amount) and z' = z on a window [1, W]. For a block coordinate k write
   Delta_k(z') := u_{k,m}(x') - u_{k,m}(xhat) = u_{k,m}((z' - z) 1_{(W,inf)}).
Status of k at f' vs f is governed by Delta_k relative to Phi_m(k) (block threshold, Preprint B).

## Lemma 6.1 (duality; PROVED)

Let E be a finite-dimensional subspace of l_1(W, inf) and y in l_1(W, inf). Then
   sup { y(eta) : eta in c_00(W, inf), ||eta||_inf <= 1, h(eta) = 0 for all h in E } = dist_{l_1}(y, E).
Proof. "<=": for h in E, y(eta) = (y - h)(eta) <= ||y - h||_1. ">=": the annihilator E_perp := {eta in c_0(W,inf) :
h(eta) = 0, h in E} is a closed subspace of c_0 and (E_perp)* = l_1/(E_perp)^perp = l_1/E (E is finite-dimensional, hence
weak*-closed, so (E_perp)^perp = E). Hence sup over the unit ball of E_perp of y(eta) is the quotient norm
dist(y, E). The unit ball of E_perp cap c_00 is norm dense in that of E_perp (truncate and correct on finitely many
coordinates using a finite set where E is "injective"; standard), so the sup over c_00 is the same. QED

## Corollary 6.2 (destroyed implies convertible; PROVED)

Let G be a finite set of block coordinates ("guards") and k notin G. Put
   tau_k := dist_{l_1}( u_{k,m}|_{(W,inf)},  span{ u_g|_{(W,inf)} : g in G } )    (the FREE TAIL MASS of k).
(a) If z' (beyond W) keeps the guards exactly matched, Delta_g(z') = 0 for g in G, then |Delta_k(z')| <= 2 tau_k.
(b) Conversely, for every s with |s| < tau_k there is eta in c_00(W,inf) with ||eta||_inf <= 1, Delta_g unchanged for
    all g in G, and Delta_k shifted by exactly s (replace z' by z' + eta / 2 when ||z'||_inf <= 1/2 far out).
So the amount by which k can be DESTROYED while the guards are kept is at most twice the amount by which the approximant
can SHIFT k (for instance back to off-peak) without touching the guards.
Proof. (a) (z' - z)1_{(W,inf)} annihilates E := span{u_g|_{(W,inf)}} and has sup norm <= 2; apply Lemma 6.1 to y = u_k|_{(W,inf)}
(by homogeneity). (b) Lemma 6.1 gives eta with value arbitrarily close to tau_k, then scale. QED
Remarks. (1) Matching the guards exactly is a finite set of linear conditions on z' beyond W; by tail independence
(A_notes Fact F(b): finitely many restrictions u_{k_i,m_i}|_{[N,inf)} are linearly independent, PROVED from Y cap c_00 = {0})
it is solvable; quantitatively the size of the correction depends on condition numbers. (2) tau_k > 0 always (same fact).

## Lemma 6.3 (no exact collinearity of tails; PROVED)

If k != k' are coordinates of the same or different blocks and there are W_0 and c in R with
u_{k,m}|_{(W_0,inf)} = c u_{k',m'}|_{(W_0,inf)}, then contradiction. Proof: u_{k,m} - c u_{k',m'} is in Y (Y linear)
and finitely supported, hence 0 (Y cap c_00 = {0}); so T(e_{k,m}/q*(T e_{k,m}) - c e_{k',m'}/q*(T e_{k',m'})) = 0,
contradicting injectivity of T. QED
Consequence: an adversary can only make tails APPROXIMATELY collinear; the deviations give individual conversion
capacity equal to their free tail mass (Cor 6.2(b)), which the adversary must keep below the conversion threshold.

## Lemma 6.4 (a single far detector can always be neutralized; PROVED for the first statement)

Let psi in l_1, W in N, psi_{>W} := psi 1_{(W,inf)}, and z in B_{l_inf}. Then
   { psi_{>W}(z') : z' in B_{c_0} } = ( -||psi_{>W}||_1 , ||psi_{>W}||_1 )   (plus an endpoint if psi_{>W} in c_00).
Hence if |psi_{>W}(z)| < ||psi_{>W}||_1 (true whenever |z| < 1 on a set carrying a positive part of |psi_{>W}|, e.g. on
near-contacts), there is z' in B_{c_0} with z' = z on [1,W] and psi((z' - z) 1_{(W,inf)}) = 0.
Proof: for z' finitely supported with |z'| <= 1, psi_{>W}(z') ranges over [-S_N, S_N], S_N = sum_{W<l<=N} |psi_l| (take
z'_l = c sign(psi_l)); S_N increases to ||psi_{>W}||_1; c_0 vectors give the open interval by approximation. QED
Consequence (HEURISTIC as a description of all adversarial designs): resources whose far parts are all proportional to
ONE detector psi can be matched simultaneously by a single scalar condition, so an adversary who wants destruction at
all fine scales at EVERY approximant needs infinitely many independent detectors ("groups"); the approximant can then
place the matched/destroyed boundary at a transition between two groups (two independent scalars), which is exactly
the configuration where Model N gives R ~ 1 when peak costs matter (part 4.4), but R(2) = 1.043 in the error-dominated
regime (part 7.4).


---

# E notes, part 7: the residual loophole (error-dominated one-sided resources) and the conversion-capacity question

## 7.1 Sensitivity of Model N to the peak-cost weight (NUMERICAL)

Dense scale grid (61 points per 12 octaves around the band, 24 points per octave for f), delta = 1:
   a0 = 0.3 (peak cost comparable to the error weight A = 1), both types converted at 2 adjacent scales: R = 0.999
     (i.e. 1 within the sampling error of the sup over tau, ~1e-3).
   a0 = 0.03 (error-dominated), both types converted at ONE scale: R = 1.19.
   [multi-scale a0 = 0.03 results: see 7.4]
Mechanism: conversion removes the first-order peak cost a0 lambda (1+delta) of f's one-sided carriers. When this cost is
comparable to the critical error cost, the saving compensates the missing fine structure even with 1-2 converted
scales. When the critical error cost dominates (large rate constant K), the boundary behaves like Model M, where
R(J) = 2.0, 1.27, 1.08, 1.007, 1.0008 for J = 1, 2, 3, 5, 8 two-sided scales: many converted scales are needed.

## 7.2 The decisive quantity: conversion capacity at the boundary

For an NA approximant with matched structure down to a boundary scale lambda_b, call the CONVERSION CAPACITY the
number J of adjacent dyadic scales below lambda_b at which the approximant can make both resource types two-sided
(off-peak with room ~M), at total cost ||f' - f|| -> 0. By the averaging skeleton (part 2.1) and Model M/N,
J -> infinity (along approximants) suffices for recovery of error-dominated one-sided mates (HEURISTIC); bounded J does
not in Model M/N (NUMERICAL; no lower bound for the real norm).
Sources of conversion capacity (all at cost o(1) in ||f' - f||):
 (i)  detector-group scalars s_n (Lemma 6.4): two at a group transition;
 (ii) the v-direction scalar V = v(x' - xhat) (one);
 (iii) individual far tails (Cor 6.2): capacity = free tail mass tau_k of each boundary resource relative to the guards;
 (iv) individual window moves through the core errors: a window move eta with v(eta) = a(eta) = 0, orthogonal to the
      finitely many sensitive coarse coordinates, shifts boundary resource k by K lambda_k sigma_k(eta); conversion needs
      |eta| ~ (1+delta) theta n/(K m ||sigma_k|_W||), and the cost of such a move is only O(lambda_b) (all coordinates at
      scales >= lambda_b other than the boundary ones are kept fixed by orthogonality; finer ones are destroyed anyway).
      So (iv) gives individual conversions UNLESS the window parts of the boundary errors are (nearly) in the span of
      the window parts of the sensitive coarse coordinates.
      [FALSE as stated; corrected in part 8. The cost estimate O(lambda_b) ignores the first-order effect of the deep
      peaks on |zeta'| and the sign changes of moderately deep peaks; and in any case window moves must be o(1) along a
      sequence f'_n -> f (Prop 8.2), so (iv) yields NO individual conversions. At window level only the absolute
      shift V of (ii) (and Delta a, which acts the same way) remains.]
To keep J bounded the adversary must therefore make every boundary resource RIGID: up to << lambda_b,
   u_k in span{u_{k'} : k' sensitive and coarser} + span{v, psi_n, a} ,
at EVERY scale, while (A1) keeping one-sided critical-rate carriers of v at all scales at f, and (A3) avoiding
combinations of coarse resources that carry v with errors o(scale) (which would make v cheaper at f' than at f).
[After the correction of (iv) (part 8.3) the WINDOW part of this rigidity requirement is unnecessary: Prop 8.2 already
blocks individual window conversions. What the adversary still needs is FAR rigidity (far parts of the boundary
resources nearly collinear inside long detector groups, limiting source (iii)), together with (A1), (A3)-(A5) below.]

## 7.3 The "rigid design" (the one candidate that survives at model level) — HEURISTIC / OPEN

Conditions an adversary would need (all at once):
 (A1) one-sided carriers of a core direction v at all scales at f: near-threshold peaks of both types P+, P-, with
      critical errors u_k - vhat ~ K lambda_k sigma_k on CORE window coordinates (|z| <= 1 - gamma_0), K large so that the
      error cost dominates the peak cost (a0 small);
 (A2) RIGIDITY: for every k, up to << lambda_k, u_k lies in span{u_k' : k' coarser and sensitive} + span{v, a, psi_n(k)}
      (blocks individual window conversions, Delta a, and far-tail conversions; Lemma 6.3 only forbids EXACT collinearity);
      consequently the core errors live (up to << 1/K) in a fixed finite-dimensional space E_c;
      [By part 8.3 only the FAR half of (A2) is needed; the window half was motivated by the false claim 7.2(iv). The
      finite-dimensionality of E_c is then an additional adversarial CHOICE (used for (A3)), not a consequence.]
 (A3) SIGN OBSTRUCTION: no zero-core-error combination is realizable by one-sided carriers on either side. By Gordan's
      alternative this holds iff there is a functional Lambda on E_c with tau_k Lambda(sigma_k) > 0 for all k
      (tau = +1 on P-, -1 on P+); then on each side the Lambda-components of the absorbed errors add up;
 (A4) destruction through infinitely many detector groups psi_n (Lemma 6.4), opposite detector coefficients for P+/P-
      (needed for one-sided cheapness of the detector errors, part 3), long groups;
 (A5) E_c-directions (and v) not approximable at critical rates by convertible generic coordinates (else frozen
      errors are re-carried by blocks and the effective error constant drops).
Under (A1)-(A5) the approximant's conversion capacity is bounded (two group scalars at a transition, plus v-shift and
Gordan-direction moves), and Model N predicts R(J_conv) > 1 in the error-dominated regime (7.4), i.e. non-recovery of
rho g for rho close to 1 AT MODEL LEVEL.
Duality remark (PROVED, Gordan): (A3) is equivalent to the existence of Lambda as stated; Lambda is represented by a core
window vector eta, and the window move along eta shifts EVERY resource toward its threshold (P+ down, P- up) by a
scale-independent relative amount. Small such moves lower all peak costs at cost o(1) in ||f' - f|| (peak values of w'
do not change while statuses are kept); large moves convert everything but cost O(1). With small a0 this global saving
is small, so it does not obviously close the gap.
Why this is NOT a counterexample (reasons for skepticism, each a concrete open point):
 * Model N omits approximant freedoms of the real norm: the block-base first-order exchange (A_notes shifted
   certificates) is idealized as a single budget; generic coordinates of other blocks; partial engineering of many
   coordinates at once; the exact Hilbert coupling.
 * Consistency of (A1)-(A5) with Martin's constraints (T norm one and injective into the operator range Y, Y cap c_00 = {0},
   every tail of (u_{k,m})_k dense in S_{q*}, Phi_m(k) = 2^{-m-k} q*(T e_{k,m})) is NOT verified; (A2) plus density of
   tails is delicate (the rigid families must coexist with a dense generic family that must itself be rigid or useless).
 * Even granting the model, a proof of non-recovery needs a LOWER bound on the cost over ALL decompositions at ALL NA
   approximants; nothing like that is available.
 * If Martin's actual T is "generic" (no rigidity), conversion capacity is unbounded and Model M/N predict recovery.
   So the answer could depend on T; for Martin's own T (unknown to me in detail: arXiv was unreachable) I lean to density.

## 7.4 multi-scale results for a0 = 0.03 (error-dominated), delta = 1, dense grid
   both types converted at J adjacent scales: J = 1: R = 1.194;  J = 2: 1.043;  J = 3: 1.0093;  J = 4: 1.0017
   (excess decays by a factor ~4.5-5.5 per extra converted scale; positive for every bounded J in the model).
   Diagnostic for J = 2 (E_work/modelN_diag.py): the f-profile is flat (0.5200-0.5225 over an octave); the f'-profile
   exceeds sup P_f on tau in [3, 60] x (band scale), maximum ratio 1.043 near tau ~ 5-10; the tau -> 0 limit (Hilbert
   cost of the frozen certificate) is 0.20, far below. So the excess is FROZEN-ERROR ABSORPTION a few octaves above the
   band (missing fine capacity in an error-dominated regime), not an artifact of the small-scale certificate.
   Phase scan, two groups, delta = 1 (both group shifts multiplied by a common factor; E_work/modelN_phase.py):
     phase 0.85: R = 1.0459;  1.0: 1.0430;  1.15: R = 1.0194;  1.30: R = 1.0174.
     At phases 1.15 and 1.3 the coarser group scalar converts TWO dyadic scales (lambda = 2 and 1, |rho| = 0.85/0.3 and
     0.7/0.6), so two groups give three converted scales. Reason: for margin delta a single shift converts a band of scale
     ratio (2+delta)/delta (part 2.4), which is 3 for delta = 1 and contains up to two dyadic scales with positive room.
     An adversary limits this by taking delta >= 2 (band ratio <= 2, at most one dyadic scale with room per scalar) or
     sparser scales; in the error-dominated regime the extra peak cost of a larger delta is cheap.
   delta = 2, a0 = 0.03, one centred converted scale per group (E_work/modelN_groups_a0_d2_g*.out):
     1 group: R = 1.180;  2 groups: R = 1.0366;  3 groups: R = 1.0061
   (same pattern as delta = 1: positive for every bounded number of converted scales, decaying geometrically).
For comparison a0 = 0.3, dense grid: 2 scales R = 0.999 (delta = 1), 0.9987 (delta = 2); 3 scales 0.9987 (delta = 2).

## 7.5 Further approximant counter-strategies against the rigid design (HEURISTIC) — the game tree does not close

The model excess comes ONLY from absorbing the frozen core errors h = sum_i x_i^fr K lambda_i sigma_i (size ~ K lambda_b)
in the base at scales a few octaves above the band. Any block mechanism that carries h (or cancels it inside g')
removes the excess. Candidates:
 (C1) sigma-carriers from FINE detector groups: a generic coordinate u ~ hhat + (far part c psi_{n'}) in a group n'
      lying entirely below the boundary has a FREE group scalar (its v-resources are destroyed anyway), so it can be
      converted at f'; it needs room only ~ K lambda_b at scales up to ~60 lambda_b, i.e. scale >= ~K lambda_b^2, and core
      error << 1/(A K). Density of tails produces such coordinates for every FIXED target at some fixed scale; as
      lambda_b -> 0 they become usable UNLESS the targets h change with lambda_b and the adversary delays good
      approximants of each sigma_i to scales << lambda_i^2 (consistent with density). Its detector part must then be
      made two-sided cheap by eta-contacts on supp psi_{n'} (possible, far coordinates).
 (C2) one-sided COARSE carriers of core directions (generic coordinates approximating e_l* - xhat_l a, l in the core
      window, with error eps_g): matched at f', usable above the band at peak cost ~ eps_g K lambda_b |t|, cheap when
      eps_g << 1/K. Fixed targets, so density provides them at fixed scales, i.e. COARSE relative to lambda_b -> 0. The
      adversary can only block one side by giving all such carriers the same peak type; then on that side the error
      cost at f is also affected (asymmetric costs at f), which changes the tightness bookkeeping.
 (C3) combinations of converted generic coordinates from several fine groups (one scalar each) approximating h with a
      FIXED precision eps_0 at scales >= K lambda_b^2: needs only fixed-target approximations (core unit vectors) and
      therefore seems unavoidable as lambda_b -> 0 — except that converting a coordinate requires its group scalar to
      take one specific value, and coordinates approximating fixed targets sit in FIXED (hence eventually coarse,
      matched) groups. Status: unresolved.
Net assessment: every obstruction I can build needs the adversary to control the rates, signs and group memberships
of approximants of ALL core directions, on top of far rigidity; the approximant has tools (C1)-(C3) whose blocking I
could not certify. The rigid design is therefore NOT an established obstruction even at heuristic level; it is the
precise remaining place where a positive proof has to work (a "frozen-error carrying" or "unbounded conversion" lemma).


---

# E notes, part 8: what o(1) moves can and cannot do (corrects an error in my earlier reasoning)

## 8.1 A false intermediate claim and its correction

Earlier (part 7.2(iv)) I assumed that a window move eta orthogonal to all SENSITIVE coarse coordinates changes f' only
through coordinates finer than the boundary ("deep peaks do not care"). That is FALSE as stated:
 * a change Delta of zeta' = L x' at deep peaks changes the block norm |zeta'| at first order (by sum over peaks of
   M sign(k) Delta(k), up to normalization) and therefore rescales ALL off-peak values w'(k) = C' zeta'(k)/(Phi_k^2 |zeta'|);
 * moderately deep peaks with |u_k(xhat)| <~ |u_k(eta)| change sign; the coarse ones change w' by O(M lambda_k).
Sanity check that something must fail (PROVED): if a fixed window coordinate l could be moved by a fixed amount gamma at
cost o(1) in ||f' - f||, we would get NA f'_n -> f with x'_n(l) not converging to xhat(l), contradicting
G_notes Prop 3.9 (normers converge weak* when first rows converge in norm; uses uniqueness of the normer).

## 8.2 Proposition (o(1) window moves). PROVED (as a consequence of (F1))

If f'_n -> f in S_{p*} with normers x'_n = q-normalized z'_n + U e'_n, then for every fixed coordinate l,
z'_n(l) -> z(l) and e'_n -> e. Consequently, for every fixed finite window F_0 and every fixed vector y in l_1 supported
in F_0 (in particular every fixed vector u restricted to F_0), y(x'_n) - y(xhat) -> 0.
Proof: G_referee 4.7 / (F1) and Prop 3.9 (e'_n -> e because a'_n -> a in l_1 and U* is bounded, nu_n -> nu > 0). QED

Consequence for conversions (SKETCH, all steps elementary): let resources u_k = (v + K lambda_k sigma_k + (far part_k))/n_k
with sigma_k supported in a fixed window and v fixed. Along any sequence f'_n -> f, the window contribution to the shift
of u_k(x'_n) is v(x'_n - xhat)/n_k + K lambda_k sigma_k(x'_n - xhat)/n_k = V_n/n_k + o(lambda_k): the second term is
o(1) RELATIVE to the scale. So window moves (and moves of a', which act through U(e' - e) in the same way) give exactly
ONE effective conversion parameter for all v-resources: the absolute shift V_n. Individual conversions must come from
the FAR parts (coordinates escaping to infinity), whose capacity is governed by Cor 6.2 (free tail mass) and can be
limited to one scalar per detector group by an adversary (Lemma 6.4 discussion, tiny deviations allowed by Lemma 6.3).

## 8.3 Consequences

 * The bounded-conversion scenario of part 7 does NOT need guard coordinates: Prop 8.2 already blocks individual window
   conversions. The adversary's remaining requirements are (A1), (A3)-(A5) of part 7.3 and "far rigidity": far parts
   of the v-resources nearly collinear inside long detector groups.
 * Then the approximant has about three conversion parameters at a group transition (two group scalars and V), i.e.
   two adjacent scales with both types converted (plus one extra single-type band), and Model N predicts a positive
   boundary excess in the error-dominated regime (part 7.4 / final table).
 * Conversely, for a "generic" T (far parts of distinct resources quantitatively independent), the approximant can
   convert arbitrarily many adjacent scales through far moves (Cor 6.2), and Model M/N predict recovery.
Status: Prop 8.2 PROVED; the consequences SKETCH/HEURISTIC.


---

# E notes, part 9: conclusions, refined necessary conditions, recommendations

## 9.1 Refined necessary conditions for a counterexample (combining parts 1-8)

A counterexample (f, g, rho) must satisfy, in addition to 1.1:
 (R-a) g is not in cl Cert(f). By Theorem 5.1 this means: there is NO family of finite certificates c_s (H <= 1,
       radius >= s, bounded kappa) with p*(g_{c_s} - g) = O(s). Equivalently (HEURISTIC reading): at a cofinal set of
       small scales the decompositions of f + t g must use ONE-SIDED resources carrying an O(1) share of g:
       block peaks / near-peak coordinates used in their long direction, or one-sided base contacts/near-contacts.
 (R-b) One-sided BASE resources are not enough: T1 (eta-trick) and T4 (eta on frozen error support + side switching)
       recover them (SKETCH). So the one-sided resources must be BLOCK peaks carrying a CORE direction (window
       coordinates with |z| bounded away from 1, where (F1) forbids eta-tricks).
 (R-c) Destroyed peaks are convertible through the far tails that destroy them (Cor 6.2); window moves are o(1)
       (Prop 8.2). So the far tails of the carriers near every possible boundary must be quantitatively RIGID (nearly
       collinear in long groups), otherwise the approximant converts unboundedly many adjacent scales and the averaging
       (T2) closes the boundary (Model M/N: R -> 1).
 (R-d) Costs must be ERROR-dominated (first-order peak cost small compared with the critical core error cost): when
       the peak cost is comparable, conversion removes it and two converted scales already give R <= 1 (Model N, a0=0.3).
 (R-e) Frozen core errors must not be carriable by blocks at the boundary, neither by converted generic coordinates of
       fine groups (C1), nor by one-sided coarse carriers of core directions (C2), nor by combinations (C3).
I could not decide whether (R-a)-(R-e) can hold simultaneously for an admissible T. Each additional requirement made the
adversarial design more delicate; none led to a contradiction I could prove.

## 9.2 What the adversarial search contributes to a positive proof

 * Reduce to one-sided resources: Theorem 5.1 removes all mates that are O(s)-approximable by certificates at f.
 * For one-sided base resources use T1/T4 (eta-tricks with budget = finest matched scale x error mass).
 * For one-sided block resources the needed lemma is QUANTITATIVE TAIL INDEPENDENCE: near any boundary scale an NA
   approximant can convert (make two-sided) the carriers at an unbounded number of adjacent scales at cost o(1);
   or alternatively a FROZEN-ERROR CARRYING lemma: the core errors of finitely many boundary carriers can be carried
   by block coordinates that are two-sided at f' (C1) or one-sided above the boundary on both sides (C2).
   Lemma 6.1/Cor 6.2 (free tail mass) and Lemma 6.3 (no exact collinearity) are the qualitative versions.
 * Use group transitions (two independent scalars) and conversion of BOTH carrier types at the same scales; Model N
   shows these choices matter (one-type bands give R ~ 2.8, coincident two-type bands R ~ 1.03, two groups R ~ 1).

## 9.3 Toy models (as requested)

Model M (two-sided critical cross resources only) and Model N (one-sided resources of both types + conversion bands)
are explicit convex cost models (definitions in 1.3 and 4.1) in which the question "can the truncated structure at an
NA approximant recover rho g for every rho < 1?" is SETTLED NUMERICALLY:
 * Model M: yes, by multi-scale averaging (R(J) -> 1); Theorem 5.1 is the rigorous counterpart at f.
 * Model N with >= 2 adjacent converted scales and comparable peak cost: yes (R <= 1 within 1e-3).
 * Model N error-dominated with a bounded number J of converted scales: no for rho^2 > 1/R(J) (delta = 1: R(2) = 1.043,
   R(3) = 1.0093, R(4) = 1.0017; delta = 2: R(2) = 1.037, R(3) = 1.006); yes if J is unbounded.
The models are proxies; they do not include every approximant strategy of the real norm (part 7.5), and no lower
bound for the real norm is proved. Single-block and "simple u_k" versions of Martin's norm reduce to the same
mechanisms (the analysis above is single-block throughout).

## 9.4 Suggested next steps

 1. Prove the quantitative tail independence / frozen-error carrying lemma for Martin's ACTUAL T (needs the details of
    Martin's Lemma B; arXiv was not reachable from this sandbox).
 2. Try to build an explicit "rigid" T satisfying (M1)-(M7) and (A1)-(A5); if this is impossible (e.g. because density
    of tails forces counter-strategy C1 or C3), the remaining loophole closes and Theorem 5.1 + T1-T4 + conversion give a
    complete heuristic picture of density; the proof would then be a matter of bookkeeping.
 3. Extend Theorem 5.1 to shifted certificates (needs a quantitative radius in A_notes Prop 4.16) and to joint fibres
    C_d(f) (ranges l_2^{d+1}); the averaging argument is convexity-based and should extend verbatim along rays.

## Appendix: numerical scripts (all in ctx/r1/E_work/, numpy only)

 * modelM.py, modelM_opt.py, modelM_opt2.py — Model M (part 1.3).
 * modelN.py (solver; unit-tested against hand computations and brute force, see part 9 log), modelN_run.py,
   modelN_run2.py, modelN_scan.py, modelN_fine.py, modelN_groups.py, modelN_groups_dense.py, modelN_groups_a0.py,
   modelN_phase.py, modelN_diag.py — Model N (parts 4 and 7). Outputs: *.out files in the same directory
   (error-dominated runs: modelN_groups_a0.out (delta = 1), modelN_groups_a0_d2_g{1,2,3}.out (delta = 2),
   modelN_phase.out). Typical run time 5-20 minutes per configuration (Nelder-Mead over the frozen weights, sup over
   ~80 scales).
 * Solver unit tests (run 2026-10-08): off-peak single resource cost 0.48 (expected 0.48); peak inward cost 0.72
   (0.72); wrong side infeasible (inf); exact frozen cancellation 0.08 (0.08); two-resource box case 0.626875
   (brute force 0.626875).


---

