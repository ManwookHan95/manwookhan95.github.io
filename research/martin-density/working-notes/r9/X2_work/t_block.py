import numpy as np, cvxpy as cp, sys
sys.path.insert(0, '.')
from xmodel import Model
M = Model()
rng = np.random.default_rng(1)
for trial in range(5):
    zeta = rng.normal(size=M.K)*np.array([1, 0.1, 0.01, 0.001])
    B = M.block(zeta)
    w = cp.Variable(M.K)
    pr = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(M.Phi, w), 2) <= 1])
    pr.solve(solver='CLARABEL', tol_gap_abs=1e-13, tol_gap_rel=1e-13, tol_feas=1e-13)
    print('A closed %.12f  cvx %.12f  |w diff| %.2e  N(w)=%.12f  peaks %s' % (B['A'], pr.value, np.abs(B['w']-w.value).max(),
          np.abs(B['w']).max() + np.linalg.norm(M.Phi*B['w']), B['P']))
