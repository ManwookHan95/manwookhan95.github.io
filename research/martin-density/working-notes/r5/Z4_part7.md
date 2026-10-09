# Z4 part 7: finite-model sanity check (signs and algebra only)

Script: r5/Z4_work/maxcontact_toy.py (cvxpy/CLARABEL SOCP). Model: 14 base coordinates, F = {0,1}, z = +1 on every other coordinate
(maximal contact, every signature set swallowed with eps = +1), one block of 5 carriers with private 2-point signatures, targets of both
signs on shared coordinates and finer targets touching a coarser signature (allowedness-(b)-like), so that peaks of both signs occur.
Mates g are random directions scaled to 0.999 x the contractive boundary; two-sided decompositions are SOCP-optimal decompositions of
f ± t g, t in {3e-2, 1e-2, 3e-3}, three mates per seed, seeds 3, 5, 11.
Results (max over all instances):
| check | quantity | seed 3 | seed 5 | seed 11 |
|---|---|---|---|---|
| (c1) eq:peakshift identity residual | should be ~0 | 1.6e-5 | 6.2e-5 | 7.6e-5 |
| (c2) Step 3 upper bound via anti-sign swallowed peak: Dd M - (tau)_-/lam | <= 0 | -2.3e-3 | -2.6e-3 | -2.4e-3 |
| (c3) Step 3 lower bound via swallowing-sign peak: tau/lam - t/(sigma|alpha|) - Dd M | <= 0 | -3.3e-2 | -5.5e-2 | -4.3e-2 |
| (c4) switching budget at maximal contact: sum 2(Delta B)_- - t/q0 | <= 0 | -3.5e-3 | -3.0e-3 | -2.9e-3 |
(The c1 residuals are solver noise amplified by 1/t.) Finite models are norm attaining and degenerate, so this only confirms the signs
of the new pinning mechanism of Step 3 (base peaks pin the uniform shift without (H2)); it says nothing about infinite-dimensional
phenomena (weak peaks, near-threshold carriers).
