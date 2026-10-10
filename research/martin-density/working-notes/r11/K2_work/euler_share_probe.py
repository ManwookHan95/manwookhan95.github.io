"""Probe sup of the non-peak Euler share X of the block scalar kappa (one peak, many near-threshold non-peaks)."""
import numpy as np
from euler_check import kappa
rng = np.random.default_rng(3)
best = 0.0
for trial in range(2000):
    K = rng.integers(2, 40)
    Phi = np.sort(rng.uniform(0.01, 0.5, K))[::-1]
    nu = rng.uniform(0.0, 1.0, K); nu[0] = rng.uniform(1.0, 50.0)
    zeta = nu * Phi**2 * np.where(rng.random(K) < 0.5, -1, 1)
    k0, P0 = kappa(zeta, Phi)
    if (~P0).sum() == 0: continue
    h = 1e-7; g = np.zeros(K); ok = True
    for k in range(K):
        s = h * max(abs(zeta[k]), 1e-4)
        zp = zeta.copy(); zp[k] += s; zm = zeta.copy(); zm[k] -= s
        kp, Pp = kappa(zp, Phi); km, Pm = kappa(zm, Phi)
        if not (np.array_equal(Pp, P0) and np.array_equal(Pm, P0)): ok = False; break
        g[k] = (kp - km) / (2 * s)
    if not ok: continue
    X = (g[~P0] @ zeta[~P0]) / k0
    best = max(best, X)
print("max non-peak Euler share found:", best)
