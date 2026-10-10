"""Sanity check of Lemma IP (inward push of near-threshold coordinates).

Block: Phi_k > 0, zeta in l_1.  theta(zeta) = unique root of Psi(x) = A(x)^2 - B(x),
A(x) = sum (|zeta_k| - x Phi_k^2)_+, B(x) = sum Phi_k^2 min(x, nu_k)^2, nu_k = |zeta_k|/Phi_k^2.
Lemma IP: let N = {k : |nu_k/theta - 1| <= b}; push nu_k -> nu_k - c_k (k in N) with
c_k in [c, 2^G c], 2 b (A + theta) < c, 2^G c <= theta.  Then theta(zeta') >= theta and
nu'_k <= theta(zeta') - (c - theta b) for k in N.
"""
import numpy as np

rng = np.random.default_rng(7)


def theta_of(zeta, Phi):
    a = np.abs(zeta)
    nu = a / Phi**2

    def psi(x):
        A = np.sum(np.maximum(a - x * Phi**2, 0.0))
        B = np.sum(Phi**2 * np.minimum(x, nu) ** 2)
        return A * A - B

    lo, hi = 0.0, max(nu.max(), 1.0)
    while psi(hi) > 0:
        hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if psi(mid) > 0:
            lo = mid
        else:
            hi = mid
    th = 0.5 * (lo + hi)
    A = np.sum(np.maximum(a - th * Phi**2, 0.0))
    return th, A


def make_block(n):
    Phi = 2.0 ** (-np.arange(1, n + 1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * rng.uniform(0.0, 1.0, n) * Phi
    return Phi, zeta


viol = 0
tests = 0
min_ratio = np.inf
for trial in range(3000):
    n = rng.integers(6, 25)
    Phi, zeta = make_block(n)
    th, A = theta_of(zeta, Phi)
    # make some coordinates near-threshold (fixed point iteration)
    b = 10.0 ** rng.uniform(-8, -3)
    kk = rng.choice(n, size=rng.integers(1, min(5, n)), replace=False)
    eps = rng.uniform(-1, 1, size=len(kk)) * b * 0.5
    for _ in range(60):
        zeta[kk] = np.sign(zeta[kk] + 1e-300) * th * Phi[kk] ** 2 * (1 + eps)
        th_new, A = theta_of(zeta, Phi)
        if abs(th_new - th) < 1e-15 * th:
            th = th_new
            break
        th = th_new
    nu = np.abs(zeta) / Phi**2
    N = np.where(np.abs(nu / th - 1) <= b)[0]
    if len(N) == 0:
        continue
    G = int(rng.integers(0, 4))
    cmin = 2 * b * (A + th) * 1.01
    cmax = th / 2**G
    if cmin >= cmax:
        continue
    c = np.exp(rng.uniform(np.log(cmin), np.log(cmax)))
    ck = c * 2.0 ** rng.uniform(0, G, size=len(N))
    zeta2 = zeta.copy()
    nu2 = nu.copy()
    nu2[N] = nu[N] - ck
    zeta2[N] = np.sign(zeta[N]) * nu2[N] * Phi[N] ** 2
    th2, A2 = theta_of(zeta2, Phi)
    tests += 1
    ok1 = th2 >= th * (1 - 1e-12)
    gapreq = c - th * b
    ok2 = np.all(nu2[N] <= th2 - gapreq + 1e-12 * th)
    if not (ok1 and ok2):
        viol += 1
    min_ratio = min(min_ratio, (th2 - np.max(nu2[N])) / gapreq)
print("tests", tests, "violations", viol, "min (theta'-max nu'_N)/(c - theta b)", min_ratio)
