"""Referee check of Lemma R-T (target donors): the one-sided derivative
 D(Dz) = 2A[sum_{nu>th} s Dz + sum_{nu=th} (s Dz)_+] - 2 sum_{0<nu<th} nu s Dz + 2 th sum_{nu=th} (s Dz)_-
of Psi(theta; zeta + eta Dz) at eta = 0+ predicts the sign of theta(zeta + eta Dz) - theta(zeta) for small eta;
and D(d) + D(-d) >= 0 (so one direction of a free coordinate raises theta unless both derivatives vanish)."""
import numpy as np
rng = np.random.default_rng(99)
def root(a, Phi):
    def Psi(th):
        A = np.sum(np.maximum(a - th*Phi**2, 0)); B = np.sum(Phi**2*np.minimum(th, a/Phi**2)**2); return A*A - B
    lo, hi = 0.0, 1.0
    while Psi(hi) > 0: hi *= 2
    for _ in range(100):
        mid = 0.5*(lo+hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)
def Dfun(z, Phi, th, Dz, tol=1e-9):
    a = np.abs(z); nu = a/Phi**2; s = np.sign(z); A = np.sum(np.maximum(a - th*Phi**2, 0))
    deg = np.abs(nu - th) <= tol*th; pk = (nu > th) & ~deg; npk = (nu < th) & ~deg & (a > 0)
    sD = s*Dz
    return 2*A*(np.sum(sD[pk]) + np.sum(np.maximum(sD[deg], 0))) - 2*np.sum(nu[npk]*sD[npk]) + 2*th*np.sum(np.maximum(-sD[deg], 0))
agree = 0; disagree = 0; sym_viol = 0; tot = 0
for trial in range(1500):
    n = rng.integers(3, 15)
    Phi = rng.uniform(0.01, 1, n)*2.0**(-rng.uniform(0, 1)*np.arange(n)); Phi *= rng.uniform(0.1, 0.9)/Phi.sum()
    z = rng.normal(size=n)*rng.uniform(0.05, 1, n)
    if trial % 2 == 0:   # tune a degenerate peak
        k = rng.integers(n)
        for _ in range(60):
            th = root(np.abs(z), Phi); z[k] = np.sign(z[k] or 1.0)*th*Phi[k]**2
    th = root(np.abs(z), Phi)
    Dz = rng.normal(size=n)*(rng.random(n) < 0.6)
    D1 = Dfun(z, Phi, th, Dz, 1e-6); D2 = Dfun(z, Phi, th, -Dz, 1e-6)
    if D1 + D2 < -1e-9*max(1, abs(D1)+abs(D2)): sym_viol += 1
    for D, sgn in ((D1, 1), (D2, -1)):
        if abs(D) < 1e-6: continue
        eta = 1e-9*np.sum(np.abs(z))/max(np.sum(np.abs(Dz)), 1e-12)
        th2 = root(np.abs(z + sgn*eta*Dz), Phi)
        tot += 1
        if np.sign(th2 - th) == np.sign(D): agree += 1
        else: disagree += 1
print("tests:", tot, "sign agreements:", agree, "disagreements:", disagree, " convexity violations D(d)+D(-d)<0:", sym_viol)
