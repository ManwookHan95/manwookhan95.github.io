import numpy as np
exec(open('thm34_dependence.py').read().split("rng = np.random.default_rng(7)")[0])
rng = np.random.default_rng(7)
for trial in range(5):
    d, K, m = 30, 12, 1
    Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.3,1,K); lam = m*Phi
    U = rng.normal(size=(K,d)); U /= np.abs(U).sum(1, keepdims=True)
    xi = rng.uniform(-1,1,d)
    zeta = lam*(U@xi)
    nonpk = rng.choice(K, 3, replace=False)
    for k in nonpk:
        U[k] -= (U[k]@xi)*xi/(xi@xi)*(1-1e-3*Phi[k])
    zeta = lam*(U@xi)
    w, M, C = norming(zeta, Phi); nz = w@zeta
    off = np.where(np.abs(w) < M*(1-1e-6))[0]
    omD = np.zeros(K); omD[off[:2]] = rng.normal(size=2)
    dD = (Phi**2*w)@omD/C
    Rw = (lam*w)@U
    psi = U - np.outer(U@xi/nz, Rw)
    lhs = (lam*omD)@psi; rhs = (lam*omD)@U - dD*Rw
    print(trial, off, "factC:", omD@zeta, nz*dD, " identity err:", np.abs(lhs-rhs).max(), np.abs(rhs).max())
