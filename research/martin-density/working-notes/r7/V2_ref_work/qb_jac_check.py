"""
V2-ref numerics (sanity only).
(1) Lemma QB (threshold buffer): push a peak c outward by s, perturb the other coordinates by E (l1) with
    E <= A s/(8(A+theta+1)); check (a) theta' >= theta + R(s); (b) every k != c with nu_k < theta + R(s) - X is a
    strict non-peak of zeta'; (c) if C1(s+E) < h0 then theta' <= theta + C1(s+E) and nu_k > theta + C1(s+E) + X
    implies k peak with the same sign.  C1, h0 computed with k0 = any non-degenerate peak (also k0 = c allowed).
(2) Remark 4.5: Jacobian of (theta, A) w.r.t. (outward push at a peak, outward push at a strict non-peak):
    predicted [[C/PhiP2, -rho M/PhiP2], [M, rho M]], det = rho M/PhiP2.
"""
import numpy as np

def theta_eq(zeta, Phi):
    a = np.abs(zeta)
    def Psi(x):
        A = np.sum(np.maximum(a - x*Phi**2, 0)); B = np.sum(np.minimum(x*Phi, a/Phi)**2)
        return A*A - B
    lo, hi = 1e-300, 1.0
    while Psi(hi) > 0: hi *= 2
    for _ in range(400):
        mid = 0.5*(lo+hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    th = 0.5*(lo+hi); A = np.sum(np.maximum(a - th*Phi**2, 0))
    return th, A

rng = np.random.default_rng(2026)
nviol = {'a': 0, 'b': 0, 'c_up': 0, 'c_pk': 0}; ntest = {'a': 0, 'b': 0, 'c_up': 0, 'c_pk': 0}
for trial in range(3000):
    n = 14
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.3, 2.5, n)
    th, A = theta_eq(zeta, Phi)
    nu = np.abs(zeta)/Phi**2
    phi = np.sum(Phi**2)
    pk = [k for k in range(n) if nu[k] >= th]
    c = pk[rng.integers(len(pk))]
    ndp = [k for k in pk if nu[k] > th]
    k0 = ndp[rng.integers(len(ndp))]          # may coincide with c
    phi0 = Phi[k0]**2; h0 = min(1.0, nu[k0]-th); C1 = (1 + 2*(th+1)/A)/phi0
    s = A*10**rng.uniform(-7, -1)
    Emax = A*s/(8*(A+th+1))
    pert = rng.normal(size=n); pert[c] = 0
    pert *= rng.uniform(0, 1)*Emax/np.sum(np.abs(pert))
    z2 = zeta + pert; z2[c] = zeta[c] + np.sign(zeta[c])*s
    th2, A2 = theta_eq(z2, Phi)
    nu2 = np.abs(z2)/Phi**2
    E = np.sum(np.abs(pert))
    R = min(1.0, A*s/(8*phi*(A+th+1)))
    X = max(np.abs(pert[k])/Phi[k]**2 for k in range(n) if k != c)
    ntest['a'] += 1
    if th2 - th < R*(1-1e-9): nviol['a'] += 1
    for k in range(n):
        if k == c: continue
        if nu[k] < th + R - X:
            ntest['b'] += 1
            if nu2[k] >= th2: nviol['b'] += 1
    if C1*(s+E) < h0:
        ntest['c_up'] += 1
        if th2 - th > C1*(s+E)*(1+1e-9): nviol['c_up'] += 1
        for k in range(n):
            if k == c: continue
            if nu[k] > th + C1*(s+E) + X:
                ntest['c_pk'] += 1
                if not (nu2[k] >= th2 and np.sign(z2[k]) == np.sign(zeta[k])): nviol['c_pk'] += 1
print("Lemma QB tests:", ntest, "violations:", nviol)

# (2) Jacobian of (theta, A)
ratios = []; dets = []
for trial in range(400):
    n = 12
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.5, 2.5, n)
    th, A = theta_eq(zeta, Phi)
    nu = np.abs(zeta)/Phi**2
    P = nu >= th
    pk = [k for k in range(n) if nu[k] > th*1.05]
    npk = [k for k in range(n) if 0.05*th < nu[k] < th*0.95]
    if not pk or not npk: continue
    c = pk[0]; k = npk[0]
    M = th/(th+A); C = A/(th+A); PhiP2 = np.sum(Phi[P]**2); rho = nu[k]/th
    h = 1e-7*min(A, abs(zeta[k]))
    z1 = zeta.copy(); z1[c] += np.sign(zeta[c])*h; t1, a1 = theta_eq(z1, Phi)
    z2 = zeta.copy(); z2[k] += np.sign(zeta[k])*h; t2, a2 = theta_eq(z2, Phi)
    J = np.array([[(t1-th)/h, (t2-th)/h], [(a1-A)/h, (a2-A)/h]])
    Jp = np.array([[C/PhiP2, -rho*M/PhiP2], [M, rho*M]])
    ratios.append(np.max(np.abs(J - Jp)/np.abs(Jp)))
    dets.append(np.linalg.det(J)/(rho*M/PhiP2))
print("Remark 4.5 Jacobian: max rel. entry error %.2e over %d blocks; det ratio in [%.6f, %.6f]"
      % (max(ratios), len(ratios), min(dets), max(dets)))
