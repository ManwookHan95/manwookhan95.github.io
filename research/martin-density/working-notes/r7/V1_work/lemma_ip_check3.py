"""Lemma IP with perturbations, in high precision (mpmath) for the few cases flagged in float arithmetic."""
import numpy as np
import mpmath as mp
mp.mp.dps = 60
rng = np.random.default_rng(3)

def theta_of(zeta, Phi):
    a = [abs(z) for z in zeta]
    nu = [a[i] / Phi[i]**2 for i in range(len(a))]
    def psi(x):
        A = mp.fsum([max(a[i] - x * Phi[i]**2, 0) for i in range(len(a))])
        B = mp.fsum([Phi[i]**2 * min(x, nu[i])**2 for i in range(len(a))])
        return A * A - B
    lo, hi = mp.mpf(0), max(max(nu), mp.mpf(1))
    while psi(hi) > 0:
        hi *= 2
    for _ in range(260):
        mid = (lo + hi) / 2
        if psi(mid) > 0: lo = mid
        else: hi = mid
    th = (lo + hi) / 2
    A = mp.fsum([max(a[i] - th * Phi[i]**2, 0) for i in range(len(a))])
    return th, A

tests = viol_raise = viol_gap = 0
worst = mp.inf
for trial in range(600):
    n = int(rng.integers(6, 16))
    Phi = [mp.mpf(2) ** (-(i + 1)) * mp.mpf(rng.uniform(0.3, 1.0)) for i in range(n)]
    zeta = [mp.mpf(rng.normal()) * mp.mpf(rng.uniform(0, 1)) * Phi[i] for i in range(n)]
    th, A = theta_of(zeta, Phi)
    b = mp.mpf(10) ** rng.uniform(-8, -3)
    kk = rng.choice(n, size=int(rng.integers(1, min(5, n))), replace=False)
    eps = rng.uniform(-1, 1, size=len(kk)) * 0.5
    for _ in range(80):
        for t_, k in enumerate(kk):
            s = 1 if zeta[k] >= 0 else -1
            zeta[k] = s * th * Phi[k]**2 * (1 + b * eps[t_])
        th_new, A = theta_of(zeta, Phi)
        if abs(th_new - th) < mp.mpf(10)**-50 * th:
            th = th_new; break
        th = th_new
    nu = [abs(zeta[i]) / Phi[i]**2 for i in range(n)]
    N = [k for k in range(n) if abs(nu[k] - th) <= th * b]
    if not N:
        continue
    cmin = 4 * b * (A + th) * mp.mpf('1.001'); cmax = th / 2
    if cmin >= cmax / 2:
        continue
    c = mp.e ** (mp.mpf(rng.uniform(0, 1)) * (mp.log(cmax / 2) - mp.log(cmin)) + mp.log(cmin))
    zeta2 = list(zeta)
    for k in N:
        ck = min(c * mp.mpf(2) ** rng.uniform(0, 2), cmax)
        s = 1 if zeta[k] >= 0 else -1
        zeta2[k] = s * (abs(zeta[k]) - ck * Phi[k]**2)
    Emax = th * c * mp.fsum([Phi[k]**2 for k in N]) / (8 * (A + th))
    others = [k for k in range(n) if k not in N]
    if others:
        d = rng.normal(size=len(others)); d = d / np.sum(np.abs(d))
        fr = mp.mpf(rng.uniform(0, 1))
        for t_, k in enumerate(others):
            zeta2[k] += Emax * fr * mp.mpf(d[t_])
    th2, _ = theta_of(zeta2, Phi)
    nu2 = [abs(zeta2[k]) / Phi[k]**2 for k in range(n)]
    tests += 1
    if not th2 > th: viol_raise += 1
    if not all(nu2[k] <= th2 - (c - th * b) for k in N): viol_gap += 1
    worst = min(worst, (th2 - th) / th)
print("mp tests", tests, "raise violations", viol_raise, "gap violations", viol_gap, "min rel raise", mp.nstr(worst, 5))
