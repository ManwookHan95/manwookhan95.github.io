import numpy as np
exec(open("ytrick_exact.py").read().split("N = lambda")[0])     # wM, J
N = lambda W, Phi: np.abs(W).max() + np.linalg.norm(Phi*W)
rng = np.random.default_rng(12); tol = 1e-10; worst = -1; R = []; cnt = 0
for trial in range(200):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5, 1, K)
    zeta = rng.normal(size=K)*Phi**rng.uniform(0.2, 1.0, K)
    Q0 = rng.choice(np.arange(1, 7), size=rng.integers(1, 3), replace=False); zeta[Q0] = 0
    w = J(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w); nz = zeta @ w
    zeta[Q0] = rng.uniform(0.3, 0.8, len(Q0))*rng.choice([-1, 1], len(Q0))*Phi[Q0]**2*M*nz/C   # w(k) ~ frac*M
    w = J(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    pk = np.abs(np.abs(w)-M) < tol
    if pk[Q0].any(): continue
    t = 10**rng.uniform(-4, -2.5); zeta2 = zeta.copy()
    zeta2[Q0] *= (1 + t*rng.normal(size=len(Q0))*20)            # first-order move of the non-peaks
    w2 = J(zeta2, Phi); M2 = np.abs(w2).max(); C2 = np.linalg.norm(Phi*w2)
    pk2 = np.abs(np.abs(w2)-M2) < tol
    S = (pk & pk2 & (w*w2 > 0)) | ((~pk) & (~pk2) & (np.abs(w2-w) <= M2 - np.abs(w2)))
    Y = (w2 - w)*S; y = w2 + Y; gam = C2 - C
    Delta = Phi*(w2 - w); R1 = (Phi*w2) @ (Phi*(w2-w)*(~S))
    extra = (Delta@Delta + (Phi*Y)@(Phi*Y) + 2*abs(R1))/(2*(C+2*gam))
    worst = max(worst, N(y, Phi) - (1 + max(gam, 0) + extra)); cnt += 1
    if abs(gam) > 20*extra: R.append((np.sign(gam), (N(y, Phi) - 1)/abs(gam)))
print('cases', cnt, 'max violation', worst)
for sgn in [1, -1]:
    r = [x for s, x in R if s == sgn]
    if r: print('C2-C %s 0: %d cases, (N(y)-1)/|C2-C| in [%.4f, %.4f]' % ('>' if sgn > 0 else '<', len(r), min(r), max(r)))
