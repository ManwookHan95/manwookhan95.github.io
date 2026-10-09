"""Extension of Z3 Lemma 5.1 to SEVERAL inward coordinates: two degenerate peaks and two strict non-peaks of small gap, all moved
inward (varsigma_k s omega(k) <= 0) without overshoot and with NO gap condition, plus ordinary strict non-peaks moved within half
their gap.  Claim: ||W(s)||_inf = (1 - ds)M, <W - w, zeta> = 0, N(W) - 1 <= (s^2/2) H (1 + 2|ds|M/C)."""
import numpy as np
rng = np.random.default_rng(2)
def N(w, Phi): return np.max(np.abs(w)) + np.linalg.norm(Phi * w)
worst, worst_fo, worst_sup = -np.inf, 0.0, 0.0
for trial in range(3000):
    n = 14
    Phi = 0.5 ** (np.arange(n) + 2) * rng.uniform(0.5, 1.0, n)
    P = rng.choice(n, size=5, replace=False)
    sgn = rng.choice([-1.0, 1.0], n)
    w = sgn * rng.uniform(0.0, 0.9, n); w[P] = sgn[P]
    Q = np.array([k for k in range(n) if k not in P])
    small = rng.choice(Q, size=2, replace=False)               # strict non-peaks of tiny gap
    w[small] = sgn[small] * (1 - 10.0 ** rng.uniform(-6, -3, 2))
    a = np.linalg.norm(Phi * w); M = 1 / (1 + a); C = 1 - M; w = M * w
    alpha = np.zeros(n); wts = rng.uniform(0, 1, 5); wts[:2] = 0.0; wts /= wts.sum()   # P[0], P[1] degenerate
    alpha[P] = wts * np.sign(w[P])
    zeta = alpha + Phi ** 2 * w / C
    gaps = M - np.abs(w)
    inward = list(P[:2]) + list(small)
    ordinary = rng.choice([k for k in Q if k not in small], size=2, replace=False)
    om = np.zeros(n)
    om[inward] = -np.sign(w[inward]) * np.abs(rng.normal(size=4))
    om[ordinary] = rng.normal(size=2)
    d = np.dot(Phi * w, Phi * om) / C
    H = (np.linalg.norm(Phi * om) ** 2 - d ** 2) / C
    smax = min([gaps[k] / (2 * abs(om[k])) for k in ordinary] + [0.5 / (abs(d) + 1e-15), C / (2 * abs(d) * M + 1e-15)]
               + [0.5 * (M + abs(w[k])) / abs(om[k]) for k in inward])
    for s in np.linspace(smax / 40, smax, 6):
        W = (1 - d * s) * w + s * om
        worst = max(worst, (N(W, Phi) - 1) - 0.5 * s * s * H * (1 + 2 * abs(d * s) * M / C))
        worst_fo = max(worst_fo, abs(np.dot(W - w, zeta)) / s)
        worst_sup = max(worst_sup, abs(np.max(np.abs(W)) - (1 - d * s) * M))
print("max (N(W)-1) - bound:", worst)
print("max |<W-w,zeta>|/s:", worst_fo)
print("max | ||W||_inf - (1-ds)M |:", worst_sup)
