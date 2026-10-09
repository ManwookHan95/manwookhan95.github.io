"""Sanity checks for Z3 part 1 (Lemma 1.2a) and part 5 (Lemma 5.1, inward moves need no gap).
Finite block model: coordinates k = 0..n-1, weights Phi_k, dual norm N(w) = ||w||_inf + ||D w||_2.
We build w with N(w)=1, a peak set P (|w| = M), alpha >= 0 on P (some peaks degenerate: alpha = 0),
zeta := alpha*sgn(w) + D^2 w / C, so that w norms zeta and |zeta|_Phi = 1.
"""
import numpy as np
rng = np.random.default_rng(1)

def N(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi * w)

def build(n=12):
    Phi = 0.5 ** (np.arange(n) + 2) * rng.uniform(0.5, 1.0, n)
    # pick C small, M = 1 - C
    # choose w: peaks on P with |w| = M, others with |w| < M, then rescale so that ||D w|| = C
    P = rng.choice(n, size=4, replace=False)
    sgn = rng.choice([-1.0, 1.0], n)
    w = sgn * rng.uniform(0.0, 0.9, n)
    w[P] = sgn[P] * 1.0
    # w = M * (w/1) ; need ||D w||_2 = C with M = 1 - C: ||D w|| = M * ||D w0|| => C = M a, a = ||D w0||
    a = np.linalg.norm(Phi * w)
    M = 1.0 / (1.0 + a)
    C = 1.0 - M
    w = M * w
    alpha = np.zeros(n)
    wts = rng.uniform(0, 1, len(P))
    wts[0] = 0.0  # P[0] is a degenerate peak
    wts = wts / wts.sum()
    alpha[P] = wts * np.sign(w[P])
    zeta = alpha + Phi ** 2 * w / C
    return Phi, w, M, C, P, alpha, zeta

def d_coef(w, Phi, C, om):
    return np.dot(Phi * w, Phi * om) / C

def H(w, Phi, C, om):
    d = d_coef(w, Phi, C, om)
    return (np.linalg.norm(Phi * om) ** 2 - d ** 2) / C

worst_ratio = -np.inf
worst_first_order = 0.0
outward_viol = []
for trial in range(2000):
    Phi, w, M, C, P, alpha, zeta = build()
    n = len(w)
    k0 = P[0]  # degenerate peak
    Q = np.array([k for k in range(n) if k not in P])
    om = np.zeros(n)
    kq = rng.choice(Q, size=2, replace=False)
    om[kq] = rng.normal(size=2)
    om[k0] = -np.sign(w[k0]) * abs(rng.normal())  # inward for s > 0
    d = d_coef(w, Phi, C, om)
    gaps = M - np.abs(w)
    # admissible s > 0 range
    smax = min([gaps[k] / (2 * abs(om[k])) for k in kq] + [0.5 / (abs(d) + 1e-12), C / (2 * abs(d) * M + 1e-12),
               (M + abs(w[k0])) * 0.5 / abs(om[k0])])
    for s in np.linspace(smax / 50, smax, 7):
        W = (1 - d * s) * w + s * om
        lhs = N(W, Phi) - 1.0
        rhs = 0.5 * s ** 2 * H(w, Phi, C, om) * (1 + 2 * abs(d * s) * M / C)
        worst_ratio = max(worst_ratio, lhs - rhs)
        # first-order term <W - w, zeta> must vanish
        worst_first_order = max(worst_first_order, abs(np.dot(W - w, zeta)) / s)
        # outward move at k0 (s < 0 with the same omega) : first-order increase of the sup norm
        W2 = (1 + d * s) * w - s * om
        outward_viol.append((N(W2, Phi) - 1.0) / s)
print("max (N(W)-1) - bound over all trials (should be <= ~1e-15):", worst_ratio)
print("max |<W-w,zeta>|/s (should be ~0):", worst_first_order)
print("outward moves: min first-order slope (N(W)-1)/|s| (positive => genuine kink):", np.min(outward_viol))
