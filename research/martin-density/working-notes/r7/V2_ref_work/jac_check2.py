import numpy as np
exec(open('qb_jac_check.py').read().split("rng = np.random.default_rng(2026)")[0])
rng = np.random.default_rng(5)
errs = []; dets = []; skipped = 0
for trial in range(1500):
    n = 10
    Phi = 2.0**(-np.arange(1, n+1)/2) * rng.uniform(0.3, 1.0, n) * 0.3
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.5, 2.0, n)
    th, A = theta_eq(zeta, Phi)
    nu = np.abs(zeta)/Phi**2
    P = nu >= th
    pk = [k for k in range(n) if nu[k] > th*1.05]
    npk = [k for k in range(n) if 0.05*th < nu[k] < th*0.95]
    if not pk or not npk: continue
    c = pk[0]; k = npk[0]
    M = th/(th+A); C = A/(th+A); PhiP2 = np.sum(Phi[P]**2); rho = nu[k]/th
    hc = 1e-5*min(A, (nu[c]-th)*Phi[c]**2)
    hk = 1e-5*min(abs(zeta[k]), (th-nu[k])*Phi[k]**2)
    if min(hc, hk) < 1e-9*A: skipped += 1; continue
    def fd(idx, h):
        zp = zeta.copy(); zp[idx] += np.sign(zeta[idx])*h; tp, ap = theta_eq(zp, Phi)
        zm = zeta.copy(); zm[idx] -= np.sign(zeta[idx])*h; tm, am = theta_eq(zm, Phi)
        return (tp-tm)/(2*h), (ap-am)/(2*h)
    t1, a1 = fd(c, hc); t2, a2 = fd(k, hk)
    J = np.array([[t1, t2], [a1, a2]])
    Jp = np.array([[C/PhiP2, -rho*M/PhiP2], [M, rho*M]])
    errs.append(np.max(np.abs(J - Jp)/np.abs(Jp)))
    dets.append(np.linalg.det(J)/(rho*M/PhiP2))
print("Jacobian check: %d blocks (skipped %d with steps below precision); max rel entry err %.2e; det ratio in [%.6f, %.6f]"
      % (len(errs), skipped, max(errs), min(dets), max(dets)))
