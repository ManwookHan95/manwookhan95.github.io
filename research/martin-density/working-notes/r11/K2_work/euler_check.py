"""K2 numerics for Lemma K2.8: the block scalar kappa = A + theta*Phi_P^2 + S/theta (U1 Lemma 1.3) of the Martin-type block norm
(threshold equation as in r10/Q2_refa_work/smass_jacobian.py) is positively 1-homogeneous in zeta and satisfies Euler's identity
sum_k zeta_k d kappa/d zeta_k = kappa while the peak set is fixed; also prints the non-peak Euler share X = sum_{nonpeak} zeta_k dkappa/dzeta_k / kappa."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(7)

def kappa(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    def G(th):
        P = nu >= th
        A = (Phi[P]**2 * (nu[P] - th)).sum()
        return A**2 - th**2 * (Phi[P]**2).sum() - (nu[~P]**2 * Phi[~P]**2).sum()
    hi = nu.max()
    th = brentq(G, 1e-14 * hi, hi * (1 - 1e-15), xtol=1e-17 * hi, rtol=1e-15, maxiter=1000)
    P = nu >= th
    A = (Phi[P]**2 * (nu[P] - th)).sum()
    S = (nu[~P]**2 * Phi[~P]**2).sum()
    return A + th * (Phi[P]**2).sum() + S / th, P

maxhom = maxeul = 0.0; shares = []
for trial in range(300):
    K = rng.integers(3, 9)
    Phi = np.sort(rng.uniform(0.05, 0.4, K))[::-1]
    zeta = rng.uniform(-1, 1, K) * Phi**2 * rng.uniform(0.2, 2.0, K)
    k0, P0 = kappa(zeta, Phi)
    c = rng.uniform(0.3, 3.0)
    k1, P1 = kappa(c * zeta, Phi)
    maxhom = max(maxhom, abs(k1 - c * k0) / abs(c * k0))
    h = 1e-7; grad = np.zeros(K)
    ok = True
    for k in range(K):
        zp = zeta.copy(); zp[k] += h * max(abs(zeta[k]), 1e-3)
        zm = zeta.copy(); zm[k] -= h * max(abs(zeta[k]), 1e-3)
        kp, Pp = kappa(zp, Phi); km, Pm = kappa(zm, Phi)
        if not (np.array_equal(Pp, P0) and np.array_equal(Pm, P0)): ok = False; break
        grad[k] = (kp - km) / (2 * h * max(abs(zeta[k]), 1e-3))
    if not ok: continue
    maxeul = max(maxeul, abs(grad @ zeta - k0) / abs(k0))
    if (~P0).any(): shares.append((grad[~P0] @ zeta[~P0]) / k0)
print("homogeneity: max |kappa(c zeta) - c kappa(zeta)|/|c kappa| =", maxhom)
print("Euler: max |sum zeta_k dkappa/dzeta_k - kappa|/kappa =", maxeul)
print("non-peak Euler share X: min %.4f max %.4f (n=%d)" % (min(shares), max(shares), len(shares)))
