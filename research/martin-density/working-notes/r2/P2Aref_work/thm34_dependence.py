# Referee check: the "tuning span" hypothesis (iii) of P2 Thm 3.4 can never hold for nontrivial two-piece data.
# Identity: sum_k lambda_k omega_D(k) psi_k = R* omega_D - Delta d R* w   (psi_k = u_k - (u_k(xi)/|zeta|) R* w),
# so for two-piece data sum_{k,m} c_{k,m} psi_{k,m} = v = b+ - b-, which vanishes on the free coordinates J_gamma.
import numpy as np
from scipy.optimize import brentq, minimize_scalar
def wM(M, zeta, Phi):
    C = 1-M
    g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
    mu = brentq(g, 0, 1e18, xtol=1e-300, rtol=1e-15, maxiter=2000)
    return np.clip(mu*zeta/Phi**2, -M, M)
def norming(zeta, Phi):
    Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-9)
    Ms = np.linspace(Mmin, 1-1e-7, 400); ob = [wM(M,zeta,Phi)@zeta for M in Ms]; i = int(np.argmax(ob))
    r = minimize_scalar(lambda M: -(wM(M,zeta,Phi)@zeta), bounds=(Ms[max(i-1,0)], Ms[min(i+1,len(Ms)-1)]), method='bounded', options={'xatol':1e-15})
    w = wM(r.x, zeta, Phi); return w, r.x, 1-r.x
rng = np.random.default_rng(7); worst = 0
for trial in range(20):
    d, K, m = 30, 12, 1
    Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.3,1,K); lam = m*Phi
    U = rng.normal(size=(K,d)); U /= np.abs(U).sum(1, keepdims=True)      # rows u_k (l_1-normalized)
    xi = rng.uniform(-1,1,d)
    zeta = lam*(U@xi)
    nonpk = rng.choice(K, 3, replace=False)                                 # force some strict non-peaks
    for k in nonpk:                                                          # make u_k(xi) tiny
        U[k] -= (U[k]@xi)*xi/(xi@xi)*(1-1e-3*Phi[k]); 
    zeta = lam*(U@xi)
    w, M, C = norming(zeta, Phi); nz = w@zeta
    off = np.where(np.abs(w) < M*(1-1e-6))[0]
    if len(off) < 2: continue
    omD = np.zeros(K); omD[off[:2]] = rng.normal(size=2)
    dD = (Phi**2*w)@omD/C
    Rw = (lam*w)@U                                                          # R* w
    psi = U - np.outer(U@xi/nz, Rw)                                         # psi_k
    lhs = (lam*omD)@psi; rhs = (lam*omD)@U - dD*Rw
    worst = max(worst, np.abs(lhs-rhs).max()/np.abs(rhs).max())
    # Fact C check used: <omD, zeta> = |zeta| dD
    worst = max(worst, abs(omD@zeta - nz*dD)/abs(nz*dD))
print("max relative error of identity sum c_k psi_k = R*omega_D - Delta d R*w  (and Fact C):", worst)
