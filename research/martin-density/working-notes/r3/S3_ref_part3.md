# S3 referee, part 3: independent numerical test of Theorem B (finite analogue), beyond certificates

Script: ctx/r3/S3ref_work/thmB_check.py and thmB_small.py. Same finite model as the C referee / S3 (seed 21, n = 6, d = 3, one block
with 5 coordinates + transfer coordinate), but p* computed INDEPENDENTLY as the SOCP p*(h) = min_W max(q*(h - R^T W), N(W)) (exact
formula, since B_{p*} = B_{q*} + L*(B_{V*}) is a Minkowski sum), solved with Clarabel at tolerance 1e-14 (p*(f) - 1 = 5e-15 in the
kink model). gamma^+- computed by the QP of 2.2 (side-admissible omega in R^Q).

Results (kink model, every off-support coordinate a contact):
| g | side | gamma (QP) | exact 2(p*(f+tg)-1)/t^2 at |t| = 2e-3, 5e-4, 1e-4 |
|---|---|---|---|
| C-referee certificate | + | 0.29567 | 0.35981, 0.29567, 0.29588 (precision drift at 1e-4) |
| C-referee certificate | - | 0.28325 | 0.28323, 0.28325, 0.28325 |
| random g, g(xi) = 0 (rand0) | + | 1.10419 | 1.97333, 1.25569, 1.10425 |
| random g, g(xi) = 0 (rand0) | - | 1.75850 | 84.315, 28.829, 1.75872 (and 1.75852 at 2.5e-5) |
Free-coordinate model: certificate 0.29824 both sides (Richardson 0.29825); random g are side-infeasible (gamma = +infinity) and the
exact coefficients blow up like 1/|t| (8.6, 15.1, 27.6 at t = .02, .01, .005), as Theorem B predicts.

Conclusions.
 (1) The finite analogue of Theorem B holds for NON-certificate directions too (random g with g(xi) = 0, both sides, asymmetric values,
     infeasible sides): strong independent evidence that the duality formula is right.
 (2) ONSET SCALE: the exact coefficient reaches gamma only for |t| below the radius min_k gap_k/|omega_k| of the OPTIMAL side
     decomposition (here the transfer coordinate k = 5 with Phi = 0.45^10 carries omega_5 ~ 800-2400, radius ~3e-4). Above that the
     coefficient can be 50 times larger (rand0, side -). This is harmless for Theorem B (a limit) and for Theorem D (T_0 is chosen after
     the data are fixed), but it means "gamma^+- <= 1" says nothing about any FIXED scale; any argument needing uniformity of the
     second-order behaviour across a family of points/data (O3, averaging over scales, generic supports) must not use gamma as if it
     were attained at a data-independent scale.
