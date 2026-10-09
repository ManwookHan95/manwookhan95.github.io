import numpy as np, cvxpy as cp, warnings
warnings.filterwarnings('ignore')
from model import build_f, pstar
from model2 import make_model2

def normer_face(M, nobj=30, seed=0):
    rng = np.random.default_rng(seed)
    n, K = M['n'], M['K']
    pts = []
    for i in range(nobj):
        r = rng.standard_normal(n)
        x = cp.Variable(n); h1 = cp.Variable(n); h2 = cp.Variable(K); t1 = cp.Variable(); t2 = cp.Variable()
        Rx = cp.multiply(M['lam'], M['u'] @ x)
        cons = [cp.norm(x - M['U'] @ h1, 'inf') <= t1, cp.norm(h1, 2) <= t1,
                cp.norm(Rx - cp.multiply(M['Phi'], h2), 1) <= t2, cp.norm(h2, 2) <= t2, t1 + t2 <= 1,
                ]
        pr = cp.Problem(cp.Maximize(M['f'] @ x + 1e-5*(r @ x)), cons); pr.solve(solver='CLARABEL')
        pts.append(x.value)
    P = np.array(pts)
    return P

if __name__ == '__main__':
    M = build_f(make_model2())
    P = normer_face(M)
    D = P - P.mean(0)
    sv = np.linalg.svd(D, compute_uv=False)
    print('singular values of normer-face spread', np.round(sv[:8], 6))
    print('xi', np.round(M['xi'], 4))
    print('max |P - xi|', np.abs(P - M['xi']).max())
