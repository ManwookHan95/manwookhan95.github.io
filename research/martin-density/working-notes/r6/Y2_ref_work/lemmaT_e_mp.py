"""High-precision re-test of Lemma T(e) on near-tight random cases (decimal, 60 digits)."""
import numpy as np
from decimal import Decimal as Dm, getcontext
getcontext().prec = 60
rng = np.random.default_rng(12345)
def root(a, Phi):
    def Psi(th):
        A = sum([max(ai - th*p*p, 0) for ai, p in zip(a, Phi)])
        B = sum([p*p*min(th, ai/(p*p))**2 for ai, p in zip(a, Phi)])
        return A*A - B
    lo, hi = Dm(0), Dm(1)
    while Psi(hi) > 0: hi *= 2
    for _ in range(260):
        mid = (lo+hi)/2
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return (lo+hi)/2
viol = 0; tests = 0; minrel = Dm('Infinity')
for trial in range(3000):
    n = int(rng.integers(2, 12))
    Phi = rng.uniform(0.001, 1, n)*2.0**(-rng.uniform(0, 1)*np.arange(n)); Phi *= rng.uniform(0.05, 0.99)/Phi.sum()
    z = np.abs(rng.normal(size=n))*rng.uniform(0, 1, n)**2 + 1e-12
    Phi = [Dm(float(p)) for p in Phi]; a = [Dm(float(x)) for x in z]
    th = root(a, Phi); A = sum([max(ai - th*p*p, 0) for ai, p in zip(a, Phi)])
    nu = [ai/(p*p) for ai, p in zip(a, Phi)]
    kp = int(rng.integers(n)); a2 = list(a)
    if nu[kp] >= th and rng.random() < 0.5:
        D = a[kp]*Dm(float(rng.uniform(1e-3, 0.5))); a2[kp] += D; bound = A*D/(A+th)
    else:
        if nu[kp] > th: continue
        D = a[kp]*Dm(float(rng.uniform(1e-3, 0.99))); a2[kp] -= D; bound = nu[kp]*D/(2*(A+th))
    others = [k for k in range(n) if k != kp]
    if not others: continue
    E = bound*Dm('0.999999')
    wts = rng.dirichlet(np.ones(len(others)))
    for k, wt in zip(others, wts):
        if nu[k] >= th: a2[k] = max(a2[k] - Dm(float(wt))*E, Dm(0))
        else: a2[k] += Dm(float(wt))*E
    th2 = root(a2, Phi); tests += 1
    rel = (th2 - th)/th
    if rel <= 0: viol += 1
    minrel = min(minrel, rel)
print("tests", tests, "violations", viol, "min rel increase", '%.3e' % float(minrel))
