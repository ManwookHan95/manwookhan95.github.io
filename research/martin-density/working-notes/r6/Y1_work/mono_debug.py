import numpy as np
src = open('threshold_check.py').read().split("errs = []")[0]
exec(src)
rng = np.random.default_rng(7)
fails=[]
for trial in range(200):
    n = 12
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.5, 2.5, n)
    th, A = theta_eq(zeta, Phi)
    nu = np.abs(zeta)/Phi**2
    pk = [k for k in range(n) if nu[k] > th*1.01]
    npk = [k for k in range(n) if 0 < nu[k] < th*0.99]
    s = 1e-7*A
    for kind, lst, want in (("peak", pk, 1), ("nonpeak", npk, -1)):
        if lst:
            k = lst[0]; z2 = zeta.copy(); z2[k] += np.sign(zeta[k])*s
            th2, A2 = theta_eq(z2, Phi)
            if np.sign(th2 - th) != want: fails.append((trial, kind, th2-th, th))
print(fails[:10], len(fails))
