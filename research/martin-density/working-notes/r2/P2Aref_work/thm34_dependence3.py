# Accurate norming via the clamp consistency equation mu(M) <w(M),zeta> = C(M) (P2 Lemma 1.1 / A Fact C), then:
# (1) Fact C: <omega, zeta> = |zeta| <Dw, D omega>/C for omega off-peak;  (2) identity sum_k lam_k omega(k) psi_k = R*omega - d R*w.
import numpy as np
from scipy.optimize import brentq
def wmu(M, zeta, Phi):
    C = 1-M
    g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
    mu = brentq(g, 0, 1e18, xtol=1e-300, rtol=1e-15, maxiter=2000)
    return np.clip(mu*zeta/Phi**2, -M, M), mu
def norming(zeta, Phi):
    Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-12)
    h = lambda M: (lambda w_mu: w_mu[1]*(w_mu[0]@zeta) - (1-M))(wmu(M, zeta, Phi))
    Ms = Mmin + (1-1e-9-Mmin)*np.geomspace(1e-13, 1, 300); hs = [h(M) for M in Ms]
    ii = [i for i in range(len(Ms)-1) if np.sign(hs[i]) != np.sign(hs[i+1])]
    if not ii:   # optimum at the boundary M = Mmin: every coordinate is a peak
        M = 1/(1+np.linalg.norm(Phi)); return M*np.sign(zeta), M, 1-M
    M = brentq(h, Ms[ii[0]], Ms[ii[0]+1], xtol=1e-16, rtol=1e-15)
    w, mu = wmu(M, zeta, Phi); return w, M, 1-M
rng = np.random.default_rng(11); worstC = 0; worstI = 0; cnt = 0; worstN = 0
for trial in range(25):
    d, K, m = 30, 12, 2
    Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.3,1,K); lam = m*Phi
    U = rng.normal(size=(K,d)); U /= np.abs(U).sum(1, keepdims=True)
    xi = rng.uniform(-1,1,d)
    nonpk = rng.choice(K, 3, replace=False)
    for it in range(6):
        zeta = lam*(U@xi); w, M, C = norming(zeta, Phi); nz = w@zeta
        thr = Phi*M*nz/(C*m)
        for k in nonpk:
            U[k] += (0.5*thr[k]*np.sign(U[k]@xi + 1e-300) - U[k]@xi)*xi/(xi@xi)
    zeta = lam*(U@xi); w, M, C = norming(zeta, Phi); nz = w@zeta
    worstN = max(worstN, abs(np.abs(w).max() + np.linalg.norm(Phi*w) - 1))
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
print(cnt, "instances; |N(w)-1| <=", worstN, "; Fact C rel err:", worstC, "; identity rel err:", worstI)
