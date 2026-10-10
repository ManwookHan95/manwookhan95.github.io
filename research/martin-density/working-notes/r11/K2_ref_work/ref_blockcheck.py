"""Check the threshold formula of model.block against a direct convex program:
|zeta|_Phi = max { <w, zeta> : ||w||_inf + ||Phi w||_2 <= 1 } and w attains it."""
import numpy as np, cvxpy as cp
from model import block
rng = np.random.default_rng(5)
worst = 0.0; worstw = 0.0
for t in range(60):
    K = int(rng.integers(3, 12))
    Phi = rng.uniform(0.02, 0.4, K)
    zeta = rng.normal(size=K) * Phi * rng.uniform(0.2, 3, K)
    b = block(zeta, Phi)
    w = cp.Variable(K); s = cp.Variable()
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    prob.solve(solver=cp.CLARABEL)
    worst = max(worst, abs(prob.value - b['A']) / b['A'])
    dual = np.abs(b['w']).max() + np.linalg.norm(Phi * b['w'])
    worstw = max(worstw, abs(dual - 1) + abs(b['w'] @ zeta - b['A']) / b['A'])
print("threshold formula vs convex program: max rel error in A =", worst, "; norming check (N(w)=1, <w,zeta>=A):", worstw)
