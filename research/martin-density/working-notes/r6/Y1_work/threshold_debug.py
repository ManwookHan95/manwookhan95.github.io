import numpy as np, cvxpy as cp
exec(open('threshold_check.py').read().split("errs = []")[0])
rng = np.random.default_rng(7)
bad=[]
for trial in range(200):
    n = 12
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.5, 2.5, n)
    th, A = theta_eq(zeta, Phi)
    nb = block_norm(zeta, Phi)
    nu = np.abs(zeta)/Phi**2
    pk = [k for k in range(n) if nu[k] > th*1.01]
    npk = [k for k in range(n) if 0 < nu[k] < th*0.99]
    s = 1e-7*A
    r = None
    if npk:
        k = npk[0]; z2 = zeta.copy(); z2[k] += np.sign(zeta[k])*s
        th2, A2 = theta_eq(z2, Phi)
        r = (th2 - th)/th
    if abs(A-nb)/nb > 1e-4 or (r is not None and r >= 0):
        bad.append((trial, abs(A-nb)/nb, r, th, A, nb, len(pk)))
for b in bad[:10]: print(b)
print(len(bad))
