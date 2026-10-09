# Check of N2 Lemma 3.2: W = w' + tau(omega - d' w') + s(w - w'), N(W) = ||W||_inf + ||Phi W||_2.
# (a) s >= 0: N(W) <= 1 + O(tau^2) (convex combination);  (b) s < 0 with a common peak of opposite sign: N(W) >= 1 + 2M|s|.
import numpy as np, cvxpy as cp
def J(zeta, Phi):
    w = cp.Variable(len(zeta))
    pr = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1]); pr.solve(solver=cp.CLARABEL)
    return np.array(w.value)
N = lambda W, Phi: np.abs(W).max() + np.linalg.norm(Phi*W)
rng = np.random.default_rng(1); worst_a, worst_b, cnt = -1e9, 1e9, 0
for trial in range(200):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5, 1, K)
    zeta = rng.normal(size=K)*Phi**rng.uniform(0.3, 1.2, K); zeta[3] = 0.0     # coordinate 3 off-peak (w = 0)
    zeta2 = zeta.copy(); zeta2[-4:] = -zeta[-4:]                               # flip the fine coordinates (common opposite peaks)
    zeta2[:6] += rng.normal(size=6)*1e-3; zeta2[3] = 0.0
    w, w2 = J(zeta, Phi), J(zeta2, Phi)
    M, M2, C2 = np.abs(w).max(), np.abs(w2).max(), np.linalg.norm(Phi*w2)
    pk = np.abs(np.abs(w2) - M2) < 1e-7; opp = pk & (np.abs(np.abs(w) - M) < 1e-7) & (w*w2 < 0)
    if not opp.any() or abs(w2[3]) > 1e-6: continue
    cnt += 1
    om = np.zeros(K); om[3] = 1.0; d2 = (Phi**2*w2) @ om / C2
    for tau in [1e-3, 1e-2]:
        for s in [0.02, 0.1]:
            W = w2 + tau*(om - d2*w2) + s*(w - w2)
            worst_a = max(worst_a, (N(W, Phi) - 1)/tau**2)          # should stay bounded (~ H/(2(1-s)))
            W = w2 + tau*(om - d2*w2) - s*(w - w2)
            worst_b = min(worst_b, (N(W, Phi) - 1)/(2*M*s))         # should be >= 1
print("cases with common opposite peaks:", cnt)
print("(a) s>=0: max (N(W)-1)/tau^2 =", round(worst_a, 4))
print("(b) s<0 : min (N(W)-1)/(2M|s|) =", round(worst_b, 6))
