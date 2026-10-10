"""K2 referee (precision K-8): one-sided derivatives of the block scalar kappa(Omega) (U1 Lemma 1.3, first expression
kappa = [A(A + theta) - sum_{k in Omega} nu_k^2 Phi_k^2]/theta, with Omega containing d) when the Omega carrier d crosses the threshold,
compared with the frozen-status formula (peak set fixed).  Also checks that A (the block norm) is C^1 across (Martin Lemma A(d))."""
import numpy as np
from scipy.optimize import brentq
from model import block
rng = np.random.default_rng(3)

def kappa_true(zeta, Phi, Om):
    b = block(zeta, Phi)
    return (b['A'] * (b['A'] + b['theta']) - (b['nu'][Om]**2 * Phi[Om]**2).sum()) / b['theta'], b

def kappa_frozen(zeta, Phi, Om, P):
    nu = np.abs(zeta) / Phi**2
    def G(th):
        A = (Phi[P]**2 * (nu[P] - th)).sum()
        return A**2 - th**2 * (Phi[P]**2).sum() - (nu[~P]**2 * Phi[~P]**2).sum()
    th = brentq(G, 1e-12, (nu[P].min()) * (1 - 1e-14))
    A = (Phi[P]**2 * (nu[P] - th)).sum()
    return (A * (A + th) - (nu[Om]**2 * Phi[Om]**2).sum()) / th, A

for trial in range(6):
    K = 6
    Phi = rng.uniform(0.1, 0.3, K)
    zeta = rng.uniform(0.2, 1.0, K) * Phi**2
    zeta[:2] *= 6.0                                   # two robust peaks
    zeta[2:] *= 0.3                                   # Omega carriers strict non-peaks (U1 regime: Q minus Omega = {} here)
    d = 3; Om = np.zeros(K, bool); Om[2:] = True
    b = block(zeta, Phi)
    # move zeta_d to the threshold: find s with nu_d = theta
    def gap(s):
        z = zeta.copy(); z[d] = s; bb = block(z, Phi); return bb['nu'][d] - bb['theta']
    s0 = brentq(gap, 1e-6 * Phi[d]**2, 50 * Phi[d]**2 * b['theta'])
    h = 1e-7 * s0
    out = []
    for side in (-1, +1):
        z1 = zeta.copy(); z1[d] = s0 + side * 2 * h; z2 = zeta.copy(); z2[d] = s0 + side * h
        k1 = kappa_true(z1, Phi, Om)[0]; k2 = kappa_true(z2, Phi, Om)[0]
        A1 = block(z1, Phi)['A']; A2 = block(z2, Phi)['A']
        out.append(((k1 - k2) / (side * h), (A1 - A2) / (side * h)))
    zN = zeta.copy(); zN[d] = s0 * (1 - 1e-4); P = block(zN, Phi)['P']
    kf = [(kappa_frozen(zeta + np.eye(K)[d] * (s0 - zeta[d] + e), Phi, Om, P)[0]) for e in (-h, h)]
    dkf = (kf[1] - kf[0]) / (2 * h)
    print(f"trial {trial}: d kappa/d zeta_d below threshold = {out[0][0]:+.4f}, above = {out[1][0]:+.4f};  "
          f"dA/dzeta_d below = {out[0][1]:+.4f}, above = {out[1][1]:+.4f};  frozen-status d kappa/d zeta_d at threshold = {dkf:+.4f}")
