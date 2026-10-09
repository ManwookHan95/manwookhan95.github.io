import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("yt", "ytrick_exact.py")
src = open("ytrick_exact.py").read().split("N = lambda")[0]       # reuse wM, J only
exec(src)
N = lambda W, Phi: np.abs(W).max() + np.linalg.norm(Phi*W)
rng = np.random.default_rng(11); tol = 1e-10; pos = 0; ratios = []; worst = -1
for trial in range(200):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5, 1, K)
    zeta = rng.normal(size=K)*Phi**rng.uniform(0.2, 1.0, K)
    Q0 = rng.choice(np.arange(1, 9), size=rng.integers(1, 4), replace=False); zeta[Q0] *= 1e-3
    w = J(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    t = 10**rng.uniform(-4, -2); zeta2 = zeta.copy()
    zeta2[Q0] += t*Phi[Q0]*rng.normal(size=len(Q0))*50          # move only the non-peaks (gamma of either sign)
    w2 = J(zeta2, Phi); M2 = np.abs(w2).max(); C2 = np.linalg.norm(Phi*w2)
    pk, pk2 = np.abs(np.abs(w)-M) < tol, np.abs(np.abs(w2)-M2) < tol
    S = (pk & pk2 & (w*w2 > 0)) | ((~pk) & (~pk2) & (np.abs(w2-w) <= M2 - np.abs(w2)))
    Y = (w2 - w)*S; y = w2 + Y; gam = C2 - C
    Delta = Phi*(w2 - w); R1 = (Phi*w2) @ (Phi*(w2-w)*(~S))
    extra = (Delta@Delta + (Phi*Y)@(Phi*Y) + 2*abs(R1))/(2*(C+2*gam))
    worst = max(worst, N(y, Phi) - (1 + max(gam, 0) + extra))
    if gam > 10*extra and gam > 1e-9: pos += 1; ratios.append((N(y, Phi) - 1)/gam)
print('max violation', worst, '; cases with C2-C >> second order:', pos)
if ratios: print('(N(y)-1)/(C2-C) in those cases: min %.4f max %.4f' % (min(ratios), max(ratios)))
