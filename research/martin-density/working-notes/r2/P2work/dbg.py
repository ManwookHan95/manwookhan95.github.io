import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(1)
K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5,1,K)
zeta = rng.normal(size=K)*Phi
idx = rng.choice(K, 4, replace=False); zeta[idx] *= 1e-2*Phi[idx]
def wM(M):
    C = 1-M
    g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
    mu = brentq(g, 0, 1e18, xtol=1e-300, rtol=1e-15, maxiter=2000)
    return np.clip(mu*zeta/Phi**2, -M, M), mu
Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-9)
for M in np.linspace(Mmin, 0.999, 15):
    w, mu = wM(M); print("M=%.4f  obj=%.8f  mu*obj-C=%.3e  #peaks=%d" % (M, w@zeta, mu*(w@zeta)-(1-M), np.sum(np.abs(w)>=M-1e-13)))
