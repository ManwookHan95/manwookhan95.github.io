"""Y2 numerics: the companion mechanism of Proposition Q in one finite block.
A degenerate peak k_D is created by tuning; a donor coordinate (a non-degenerate peak, mass increased, or a strict
non-peak, mass decreased) is moved; we check (1) theta rises strictly, (2) k_D becomes a strict non-peak,
(3) for coordinates whose zeta is unchanged and which are strict non-peaks (or degenerate) before and non-peaks after,
the d-coefficient Phi^2 w(k)/C is multiplied by the common factor |zeta|/|zeta'| (exact d-neutrality is preserved)."""
import numpy as np, cvxpy as cp
from threshold_check import block_norm, theta_root

rng = np.random.default_rng(11)
bad = 0; maxdev = 0.0; trials = 0
for trial in range(150):
    n = 9
    Phi = rng.uniform(0.05, 0.3, n); Phi *= 0.8 / Phi.sum()
    zeta = rng.normal(size=n)
    kD = 2
    for it in range(300):
        th, _ = theta_root(zeta, Phi)
        zeta[kD] = np.sign(zeta[kD] if zeta[kD] != 0 else 1.0) * th * Phi[kD]**2
    th, A = theta_root(zeta, Phi)
    nu = np.abs(zeta) / Phi**2
    peaks = [k for k in range(n) if k != kD and nu[k] > th * 1.01]
    nonpk = [k for k in range(n) if nu[k] < th * 0.99 and abs(zeta[k]) > 1e-6]
    if not peaks or len(nonpk) < 2: continue
    donor = peaks[0] if trial % 2 == 0 else nonpk[0]
    others = [k for k in nonpk if k != donor]
    z2 = zeta.copy()
    z2[donor] *= (1.03 if donor in peaks else 0.97)
    th2, A2 = theta_root(z2, Phi)
    trials += 1
    if not (th2 > th and np.abs(z2[kD]) / Phi[kD]**2 < th2): bad += 1
    # d-coefficients via SOCP norming functionals
    v1, w1 = block_norm(zeta, Phi); C1 = np.linalg.norm(Phi * w1)
    v2, w2 = block_norm(z2, Phi);  C2 = np.linalg.norm(Phi * w2)
    for k in others + [kD]:
        r1 = Phi[k]**2 * w1[k] / C1; r2 = Phi[k]**2 * w2[k] / C2
        # predicted: r2 = r1 * v1/v2 (zeta(k) unchanged)
        maxdev = max(maxdev, abs(r2 - r1 * v1 / v2) / max(abs(r1), 1e-9))
print("trials:", trials, " failures of (theta up and k_D strict non-peak):", bad)
print("max relative deviation of d-coefficient ratio from |zeta|/|zeta'|:", maxdev)
