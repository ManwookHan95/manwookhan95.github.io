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
