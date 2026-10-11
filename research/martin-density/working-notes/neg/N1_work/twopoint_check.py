"""Sanity check (finite-dimensional, smooth strictly convex norm) of
   (i)  h_{C(f')}(v) <= sqrt((1+tau p(v))/2) (sqrt(beta(x'+tau v)) + sqrt(beta(x'-tau v)))/tau  for all tau>0,
   (ii) h_{C(f')}(v) <= sqrt(D^2 p(x')[v,v])   (tau -> 0 limit),
 where f' = grad p(x'), p(x') = 1, beta(y) = p(y) - f'(y) (Bregman divergence), and
 C(f') = {g : f'(y)^2 + g(y)^2 <= p(y)^2 for all y}.  h is computed by an LP over many sampled y
 (outer approximation => LP value >= true h; we check LP value <= bound + tol, which is the
 meaningful direction only if LP value is close to h; we refine the sample to see convergence).
 Norm: p = l_q norm on R^3 (q = 4), and a mixed norm p(x) = ||x||_4 + 0.3 ||A x||_2.
"""
import numpy as np
from scipy.optimize import linprog

rng = np.random.default_rng(0)

def make_norm(kind):
    if kind == "l4":
        q = 4.0
        def p(x):
            return np.sum(np.abs(x) ** q, axis=-1) ** (1 / q)
        def grad(x):
            n = p(x)
            return np.sign(x) * np.abs(x) ** (q - 1) / n ** (q - 1)
    else:
        A = np.array([[1.0, 0.2, 0.0], [0.0, 0.5, 0.3], [0.1, 0.0, 0.8]])
        q = 4.0
        def p(x):
            return np.sum(np.abs(x) ** q, axis=-1) ** (1 / q) + 0.3 * np.linalg.norm(x @ A.T, axis=-1)
        def grad(x):
            n4 = np.sum(np.abs(x) ** q) ** (1 / q)
            g1 = np.sign(x) * np.abs(x) ** (q - 1) / n4 ** (q - 1)
            Ax = A @ x
            g2 = 0.3 * (A.T @ Ax) / np.linalg.norm(Ax)
            return g1 + g2
    return p, grad

def hessian_quad(p, x, v, h=1e-4):
    return (p(x + h * v) + p(x - h * v) - 2 * p(x)) / h ** 2

def support_LP(p, fp, xprime, v, nsamp):
    Y = rng.normal(size=(nsamp, 3))
    Y /= np.linalg.norm(Y, axis=1, keepdims=True)
    # add points clustered near +-x' (where the constraints bind at small scale)
    eps = 10 ** rng.uniform(-4, -0.5, size=nsamp)
    D = rng.normal(size=(nsamp, 3))
    Y2 = xprime[None, :] + eps[:, None] * D
    Y = np.vstack([Y, Y2])
    pY = p(Y)
    fY = Y @ fp
    r = np.sqrt(np.maximum(pY ** 2 - fY ** 2, 0.0))
    # LP: max g.v  s.t. |g.y_i| <= r_i, g.x' = 0
    A_ub = np.vstack([Y, -Y])
    b_ub = np.concatenate([r, r])
    res = linprog(-v, A_ub=A_ub, b_ub=b_ub, A_eq=xprime[None, :], b_eq=[0.0],
                  bounds=[(None, None)] * 3, method="highs")
    return -res.fun

for kind in ["l4", "mixed"]:
    p, grad = make_norm(kind)
    for trial in range(3):
        x = rng.normal(size=3)
        x /= p(x)
        fp = grad(x)
        assert abs(fp @ x - 1) < 1e-9
        v = rng.normal(size=3)
        v -= (fp @ v) * x  # any v is fine; project so that f'(v)=0 for readability
        v /= p(v)
        hq = hessian_quad(p, x, v)
        best = np.inf
        for tau in np.logspace(-4, 0, 41):
            bp = p(x + tau * v) - (1 + tau * (fp @ v))
            bm = p(x - tau * v) - (1 - tau * (fp @ v))
            bnd = np.sqrt((1 + tau * p(v)) / 2) * (np.sqrt(max(bp, 0)) + np.sqrt(max(bm, 0))) / tau
            best = min(best, bnd)
        lps = [support_LP(p, fp, x, v, n) for n in (2000, 20000, 100000)]
        print(f"{kind} trial {trial}: LP h(v) (n=2e3,2e4,1e5) = {lps[0]:.5f} {lps[1]:.5f} {lps[2]:.5f};"
              f"  inf_tau two-point bound = {best:.5f};  sqrt(Hess) = {np.sqrt(hq):.5f};"
              f"  OK = {lps[-1] <= best + 1e-3}")
