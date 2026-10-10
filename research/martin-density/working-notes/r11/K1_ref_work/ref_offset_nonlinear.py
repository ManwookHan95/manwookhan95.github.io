"""K1 referee: independent NONLINEAR check of K1 2.2 (bank with offset is one-sided along the degenerate direction).

Model: F(P, Ptot) = F0 + N P - pi p Ptot + eps2 * Q(P, Ptot), Ptot := total bank position measured from zero mass (the offset m0/beta is part
of Ptot), N = I - g h^T - p q^T exactly degenerate (left null vector y), Q a fixed random quadratic map.  A bank requires Ptot >= 0.
For instances with y^T F0/(pi y^T p) < 0 we minimise ||F||^2 over the box |P|_inf <= R, 0 <= Ptot <= R by SLSQP from many starts and record the
minimum; by K1's linear argument the minimum is bounded below by ~ (y^T F0)^2/||y||^2 - O(eps2 R^2) > 0.  Control: the same with Ptot free in
[-R, R] (a two-sided lever) must reach ~ 0.
"""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(5)

def make_deg(n):
    while True:
        p = rng.normal(size=n); q = rng.normal(size=n) * 0.2
        if q @ p > 0.4:
            continue
        h = rng.normal(size=n); g0 = rng.normal(size=n)
        A = np.eye(n) - np.outer(p, q)
        c = h @ np.linalg.solve(A, g0)
        if abs(c) < 0.3:
            continue
        g = g0 / c
        return A - np.outer(g, h), p

res_bank, res_free = [], []
for trial in range(60):
    n = int(rng.integers(3, 6))
    N, p = make_deg(n)
    u_, s_, vt_ = np.linalg.svd(N.T); y = vt_[-1]
    pi = rng.uniform(0.3, 1.0)
    F0 = rng.normal(size=n) * 1e-2
    if (y @ F0) / (pi * (y @ p)) >= -2e-3:          # keep only instances where the forced total position is clearly negative
        continue
    Qt = rng.normal(size=(n, n + 1, n + 1)) * 0.5
    eps2 = 1e-2
    R = 0.2
    def F(x):
        P, Pt = x[:n], x[n]
        z = np.concatenate([P, [Pt]])
        return F0 + N @ P - pi * p * Pt + eps2 * np.einsum('ijk,j,k->i', Qt, z, z)
    obj = lambda x: float(F(x) @ F(x))
    best_b, best_f = np.inf, np.inf
    for s in range(12):
        x0 = rng.uniform(-R, R, size=n + 1)
        bb = [(-R, R)] * n + [(0.0, R)]
        rb = minimize(obj, np.clip(x0, [b[0] for b in bb], [b[1] for b in bb]), method='SLSQP', bounds=bb, options={'ftol': 1e-14, 'maxiter': 500})
        best_b = min(best_b, rb.fun)
        rf = minimize(obj, x0, method='SLSQP', bounds=[(-R, R)] * (n + 1), options={'ftol': 1e-14, 'maxiter': 500})
        best_f = min(best_f, rf.fun)
    lower = max(0.0, abs(y @ F0) - eps2 * np.abs(Qt).sum(axis=0).max() * ((n + 1) * R) ** 2) ** 2   # crude linear lower bound
    res_bank.append((best_b, (y @ F0) ** 2, lower)); res_free.append(best_f)
res_bank = np.array(res_bank); res_free = np.array(res_free)
print(f"instances with negative forced total position: {len(res_bank)}")
print(f"one-sided bank (Ptot >= 0): min over instances of min||F||^2 = {res_bank[:,0].min():.3e};  ratio min||F||^2/(y^T F0)^2: "
      f"min {np.min(res_bank[:,0]/res_bank[:,1]):.3f}, median {np.median(res_bank[:,0]/res_bank[:,1]):.3f}")
print(f"two-sided control (Ptot free): max over instances of min||F||^2 = {res_free.max():.3e}")
