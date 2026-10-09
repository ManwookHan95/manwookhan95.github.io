# Same test as ytrick_check.py but with a high-precision J: maximize <zeta,w> s.t. ||w||_inf + ||Phi w||_2 <= 1.
# For level M (C = 1-M): w_M(k) = clip(c zeta(k)/Phi(k)^2, -M, M) with c >= 0 s.t. ||Phi w_M|| = C (bisection);
# V(M) = <zeta, w_M> is concave in M; maximize by golden section. Uses mpmath-free float64 with tight tolerances.
import numpy as np
def wM(zeta, Phi, M):
    C = 1 - M
    f = lambda c: np.linalg.norm(Phi*np.clip(c*zeta/Phi**2, -M, M)) - C
    if f(1e30) < 0: return np.sign(zeta)*M          # box binding everywhere (not expected)
    lo, hi = 0.0, 1.0
    while f(hi) < 0: hi *= 2
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if f(mid) < 0: lo = mid
        else: hi = mid
    return np.clip(0.5*(lo+hi)*zeta/Phi**2, -M, M)
def J(zeta, Phi):
    g = (np.sqrt(5)-1)/2; a, b = 1e-9, 1-1e-9
    V = lambda M: zeta @ wM(zeta, Phi, M)
    x1, x2 = b - g*(b-a), a + g*(b-a); f1, f2 = V(x1), V(x2)
    for _ in range(200):
        if f1 < f2: a, x1, f1 = x1, x2, f2; x2 = a + g*(b-a); f2 = V(x2)
        else: b, x2, f2 = x2, x1, f1; x1 = b - g*(b-a); f1 = V(x1)
    return wM(zeta, Phi, 0.5*(a+b))
N = lambda W, Phi: np.abs(W).max() + np.linalg.norm(Phi*W)
rng = np.random.default_rng(7); worst = -1e9; worst_rel = -1e9; tol = 1e-10; cnt = 0; worst_naive = 1e9
for trial in range(300):
    K = 16; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5, 1, K)
    zeta = rng.normal(size=K)*Phi**rng.uniform(0.2, 1.0, K)
    Q0 = rng.choice(np.arange(1, 10), size=rng.integers(1, 4), replace=False); zeta[Q0] *= 1e-3
    w = J(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    t = 10**rng.uniform(-4, -2)
    zeta2 = zeta + t*Phi*rng.normal(size=K)
    flip = rng.choice(np.arange(11, K), size=rng.integers(0, 3), replace=False); zeta2[flip] *= -1
    w2 = J(zeta2, Phi); M2 = np.abs(w2).max(); C2 = np.linalg.norm(Phi*w2)
    pk, pk2 = np.abs(np.abs(w)-M) < tol, np.abs(np.abs(w2)-M2) < tol
    S = (pk & pk2 & (w*w2 > 0)) | ((~pk) & (~pk2) & (np.abs(w2-w) <= M2 - np.abs(w2)))
    Y = (w2 - w)*S; y = w2 + Y; gam = C2 - C
    Delta = Phi*(w2 - w); R1 = (Phi*w2) @ (Phi*(w2-w)*(~S))
    extra = (Delta@Delta + (Phi*Y)@(Phi*Y) + 2*abs(R1))/(2*(C+2*gam))
    bound = 1 + max(gam, 0) + extra
    worst = max(worst, N(y, Phi) - bound); cnt += 1
    worst_rel = max(worst_rel, (N(y, Phi) - 1 - max(gam, 0))/max(extra, 1e-300))
    opp = pk & pk2 & (w*w2 < 0)
    if opp.any(): worst_naive = min(worst_naive, (N(2*w2 - w, Phi) - 1)/(2*M))
print('cases', cnt, ' max [N(y) - bound] =', worst, '  max (N(y)-1-(C2-C)_+)/extra =', worst_rel)
print('naive y = 2w2-w with opposite peaks: min (N-1)/(2M) =', worst_naive)
