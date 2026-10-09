# Referee check (N2 Delta d < 0): block absorption with y = w' + (w'-w) 1_S, S = status-preserving coordinates.
# Claim: N(y) <= 1 + (C'-C)_+ + (||D(w'-w)||^2 + ||D Y||^2 + 2|R1|)/(2(C+2gamma)),  gamma = C'-C,
#        R1 = <D w', D (w'-w) 1_{S^c}>,  Y = (w'-w) 1_S.  In contrast N(2w'-w) >= 1 + 2M at common opposite peaks.
import numpy as np, cvxpy as cp
def J(zeta, Phi):
    w = cp.Variable(len(zeta))
    cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1]).solve(solver=cp.CLARABEL)
    return np.array(w.value)
N = lambda W, Phi: np.abs(W).max() + np.linalg.norm(Phi*W)
rng = np.random.default_rng(7); worst = -1e9; worst_naive = 1e9; cnt = 0; tol = 1e-7
for trial in range(300):
    K = 16; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5, 1, K)
    zeta = rng.normal(size=K)*Phi**rng.uniform(0.2, 1.0, K)
    Q0 = rng.choice(np.arange(1, 10), size=rng.integers(1, 4), replace=False)
    zeta[Q0] *= 1e-3                                   # a few strict non-peaks (exceptionally small zeta)
    w = J(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    t = 10**rng.uniform(-4, -2)
    zeta2 = zeta + t*Phi*rng.normal(size=K)            # perturbation of size t in u_k (zeta = lambda u)
    flip = rng.choice(np.arange(11, K), size=rng.integers(0, 3), replace=False); zeta2[flip] *= -1
    w2 = J(zeta2, Phi); M2 = np.abs(w2).max(); C2 = np.linalg.norm(Phi*w2)
    pk, pk2 = np.abs(np.abs(w)-M) < tol, np.abs(np.abs(w2)-M2) < tol
    same_pk = pk & pk2 & (w*w2 > 0)
    np_ok = (~pk) & (~pk2) & (np.abs(w2-w) <= M2 - np.abs(w2) + 1e-12)
    S = same_pk | np_ok
    Y = (w2 - w)*S; y = w2 + Y; gam = C2 - C
    Delta = Phi*(w2 - w); R1 = (Phi*w2) @ (Phi*(w2-w)*(~S))
    bound = 1 + max(gam, 0) + (Delta@Delta + (Phi*Y)@(Phi*Y) + 2*abs(R1))/(2*(C+2*gam))
    worst = max(worst, N(y, Phi) - bound); cnt += 1
    opp = pk & pk2 & (w*w2 < 0)
    if opp.any(): worst_naive = min(worst_naive, (N(2*w2 - w, Phi) - 1)/(2*M))
    if trial < 3: print('t=%.1e |S^c|=%d  N(y)-1=%.3e  (C2-C)_+=%.3e  bound-1=%.3e' % (t, (~S).sum(), N(y,Phi)-1, max(gam,0), bound-1))
print('cases', cnt, ' max [N(y) - bound] =', worst, '(should be <= ~1e-8)')
print('naive y = 2w2-w with opposite peaks: min (N-1)/(2M) =', worst_naive)
