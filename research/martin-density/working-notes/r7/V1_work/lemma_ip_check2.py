"""Lemma IP with perturbations: hypotheses b <= 1/2, N subset {|nu_k - theta| <= theta b}, c_k in [c, theta/2],
c >= 4 b (A + theta), other coordinates perturbed with l1 size E <= theta c sum_N Phi^2/(8(A+theta)).
Claim: theta' > theta and nu'_k <= theta' - (c - theta b) on N."""
import numpy as np

def theta_of(zeta, Phi):
    a = np.abs(zeta); nu = a / Phi**2
    def psi(x):
        return np.sum(np.maximum(a - x * Phi**2, 0.0))**2 - np.sum(Phi**2 * np.minimum(x, nu) ** 2)
    lo, hi = 0.0, max(nu.max(), 1.0)
    while psi(hi) > 0: hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if psi(mid) > 0: lo = mid
        else: hi = mid
    th = 0.5 * (lo + hi)
    return th, np.sum(np.maximum(a - th * Phi**2, 0.0))
rng = np.random.default_rng(3)
tests = viol = 0
bad = []
worst = np.inf
for trial in range(4000):
    n = int(rng.integers(6, 25))
    Phi = 2.0 ** (-np.arange(1, n + 1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * rng.uniform(0.0, 1.0, n) * Phi
    th, A = theta_of(zeta, Phi)
    b = 10.0 ** rng.uniform(-8, -3)
    kk = rng.choice(n, size=int(rng.integers(1, min(5, n))), replace=False)
    eps = rng.uniform(-1, 1, size=len(kk)) * b * 0.5
    for _ in range(60):
        zeta[kk] = np.sign(zeta[kk] + 1e-300) * th * Phi[kk] ** 2 * (1 + eps)
        th_new, A = theta_of(zeta, Phi)
        if abs(th_new - th) < 1e-15 * th:
            th = th_new; break
        th = th_new
    nu = np.abs(zeta) / Phi**2
    N = np.where(np.abs(nu - th) <= th * b)[0]
    if len(N) == 0:
        continue
    cmin = 4 * b * (A + th) * 1.001
    cmax = th / 2
    if cmin >= cmax / 2:
        continue
    c = np.exp(rng.uniform(np.log(cmin), np.log(cmax / 2)))
    ck = np.minimum(c * 2.0 ** rng.uniform(0, 2, size=len(N)), cmax)
    zeta2 = zeta.copy()
    zeta2[N] = np.sign(zeta[N]) * (np.abs(zeta[N]) - ck * Phi[N] ** 2)
    Emax = th * c * np.sum(Phi[N] ** 2) / (8 * (A + th))
    others = np.setdiff1d(np.arange(n), N)
    if len(others) > 0:
        d = rng.normal(size=len(others)); d *= Emax * rng.uniform(0, 1) / np.sum(np.abs(d))
        zeta2[others] += d
    th2, _ = theta_of(zeta2, Phi)
    nu2 = np.abs(zeta2) / Phi**2
    tests += 1
    raise_rel = (th2 - th) / th
    gap_def = np.max(nu2[N] - (th2 - (c - th * b))) / th
    # predicted resolvable scale: Psi'(theta) >= theta c sum_N Phi^2/4; slope |dPsi/dtheta| <= 2(A+theta) sum Phi^2
    pred = c * np.sum(Phi[N]**2) / (8 * (A + th) * np.sum(Phi**2))
    if raise_rel <= 0 or gap_def > 0:
        viol += 1
        bad.append((raise_rel, gap_def, pred))
    worst = min(worst, raise_rel / pred if pred > 0 else np.inf)
print("tests", tests, "flagged", viol, "min raise/predicted lower scale", worst)
print("flagged (rel raise, rel gap defect, predicted rel scale):")
for x in bad[:15]: print(["%.3e" % v for v in x])
