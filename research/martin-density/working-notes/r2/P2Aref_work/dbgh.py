import numpy as np
exec(open('thm34_dependence3.py').read().split("rng = np.random.default_rng(11)")[0])
rng = np.random.default_rng(11)
d, K, m = 30, 12, 2
Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.3,1,K); lam = m*Phi
U = rng.normal(size=(K,d)); U /= np.abs(U).sum(1, keepdims=True)
xi = rng.uniform(-1,1,d); zeta = lam*(U@xi)
Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-12)
for M in np.linspace(Mmin, 1-1e-9, 12):
    w, mu = wmu(M, zeta, Phi); print("%.6f  h=%.3e  obj=%.6e  mu*nz=%.4e C=%.4e" % (M, mu*(w@zeta)-(1-M), w@zeta, mu*(w@zeta), 1-M))
