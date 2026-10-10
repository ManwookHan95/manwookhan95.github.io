import numpy as np
exec(open('qb_jac_check.py').read().split("rng = np.random.default_rng(2026)")[0])

rng = np.random.default_rng(2026)
for trial in range(3000): pass
rng = np.random.default_rng(5)
bad = 0; tot = 0
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
    # step relative to the margins so that the peak set stays fixed
    hc = 1e-6*min(A, (nu[c]-th)*Phi[c]**2)
    hk = 1e-6*min(abs(zeta[k]), (th-nu[k])*Phi[k]**2)
    z1 = zeta.copy(); z1[c] += np.sign(zeta[c])*hc; t1, a1 = theta_eq(z1, Phi)
    z2 = zeta.copy(); z2[k] += np.sign(zeta[k])*hk; t2, a2 = theta_eq(z2, Phi)
    J = np.array([[(t1-th)/hc, (t2-th)/hk], [(a1-A)/hc, (a2-A)/hk]])
    Jp = np.array([[C/PhiP2, -rho*M/PhiP2], [M, rho*M]])
    err = np.max(np.abs(J - Jp)/np.abs(Jp)); tot += 1
    if err > 1e-3:
        bad += 1
        if bad <= 3: print(err, J, Jp, nu[c]/th, nu[k]/th, hc, hk)
print("bad", bad, "of", tot)
