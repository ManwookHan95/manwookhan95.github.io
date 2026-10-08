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
