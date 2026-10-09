# Well-conditioned version: non-peaks with |w(k)| ~ M/2 (not tiny), so Fact C is numerically sharp.
import numpy as np
exec(open('thm34_dependence.py').read().split("rng = np.random.default_rng(7)")[0])
rng = np.random.default_rng(11); worstC = 0; worstI = 0; cnt = 0
for trial in range(12):
    d, K, m = 30, 12, 2
    Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.3,1,K); lam = m*Phi
    U = rng.normal(size=(K,d)); U /= np.abs(U).sum(1, keepdims=True)
    xi = rng.uniform(-1,1,d)
    nonpk = rng.choice(K, 3, replace=False)
    for it in range(6):                     # place u_k(xi) at half the peak threshold for k in nonpk
        zeta = lam*(U@xi); w, M, C = norming(zeta, Phi); nz = w@zeta
        thr = Phi*M*nz/(C*m)
        for k in nonpk:
            target = 0.5*thr[k]*np.sign(U[k]@xi + 1e-300)
            U[k] += (target - U[k]@xi)*xi/(xi@xi)
    zeta = lam*(U@xi); w, M, C = norming(zeta, Phi); nz = w@zeta
    off = [k for k in nonpk if abs(w[k]) < 0.9*M]
    if len(off) < 2: continue
    cnt += 1
    omD = np.zeros(K); omD[off[:2]] = rng.normal(size=2)
    dD = (Phi**2*w)@omD/C
    Rw = (lam*w)@U
    psi = U - np.outer(U@xi/nz, Rw)
    lhs = (lam*omD)@psi; rhs = (lam*omD)@U - dD*Rw
    worstC = max(worstC, abs(omD@zeta - nz*dD)/(np.abs(omD)@np.abs(zeta)))
    worstI = max(worstI, np.abs(lhs-rhs).max()/np.abs(rhs).max())
print(cnt, "instances; Fact C rel err:", worstC, " identity rel err:", worstI)
