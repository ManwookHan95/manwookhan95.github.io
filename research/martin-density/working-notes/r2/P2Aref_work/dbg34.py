import numpy as np
exec(open('thm34_dependence.py').read().split("rng = np.random.default_rng(7)")[0])
rng = np.random.default_rng(7)
d, K, m = 30, 12, 1
Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.3,1,K); lam = m*Phi
U = rng.normal(size=(K,d)); U /= np.abs(U).sum(1, keepdims=True)
xi = rng.uniform(-1,1,d)
nonpk = rng.choice(K, 3, replace=False)
for k in nonpk:
    U[k] -= (U[k]@xi)*xi/(xi@xi)*(1-1e-3*Phi[k])
zeta = lam*(U@xi)
w, M, C = norming(zeta, Phi); nz = w@zeta
print("M,C", M, C, "N(w)=", np.abs(w).max()+np.linalg.norm(Phi*w))
print("w/M", np.round(w/M,4))
print("r=C|zeta|/(Phi^2 nz)", np.round(C*np.abs(zeta)/(Phi**2*nz),4))
off = np.where(np.abs(w) < M*(1-1e-6))[0]; print("off", off, "nonpk", nonpk)
# check clamp: off-peak w(k) = C zeta(k)/(Phi^2 nz)
print("clamp err off-peak", [w[k] - C*zeta[k]/(Phi[k]**2*nz) for k in off])
