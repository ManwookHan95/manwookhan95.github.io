"""Minimal switching through the module carrier when the cap is s(t) (the actual mate criterion, as in
Lemma twosided), versus the near-optimal cap p*(f -+ t g) + 0.05 t^2.  Also scale the module up to the validity limit."""
import sys
import numpy as np
import cvxpy as cp
from exp_module import build, module
from toy import s_of, SOLVER


def min_switch(M, D, g, l, t, cap_p, cap_m):
    f = D['f']; b = M.blocks[0]; w = D['w'][0]; lam = b['lam'][l]
    n = M.n; K = len(b['Phi'])
    Ap, Am = cp.Variable(n), cp.Variable(n); Wp, Wm = cp.Variable(K), cp.Variable(K)
    cons = [cp.norm1(Ap) + cp.norm(M.U.T @ Ap) <= cap_p,
            cp.norm_inf(Wp) + cp.norm(cp.multiply(b['Phi'], Wp)) <= cap_p,
            Ap + b['u'].T @ cp.multiply(b['lam'], Wp) == f + t * g,
            cp.norm1(Am) + cp.norm(M.U.T @ Am) <= cap_m,
            cp.norm_inf(Wm) + cp.norm(cp.multiply(b['Phi'], Wm)) <= cap_m,
            Am + b['u'].T @ cp.multiply(b['lam'], Wm) == f - t * g]
    sw = (lam / t) * (Wp[l] + Wm[l] - 2 * w[l])
    pr = cp.Problem(cp.Minimize(cp.abs(sw)), cons)
    try:
        pr.solve(solver=SOLVER)
    except Exception:
        pr.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
    return pr.value


Phil = float(sys.argv[1]); kappa = float(sys.argv[2]); c = float(sys.argv[3])
M, D, l = build(kappa=kappa, Phi_l=Phil)
g, q = module(M, D, l, c)
print('kappa=%.2f Phi_l=%.1e c=%.3f q=%.2e' % (kappa, Phil, c, q))
print('   t       pp-s        pm-s     minSw(cap=s)/t   minSw(near-opt)/t')
for t in np.geomspace(3e-3, 0.5, 14):
    pp = M.pstar(f := D['f'] + 0 * g, ) if False else None
    pp = M.pstar(D['f'] + t * g); pm = M.pstar(D['f'] - t * g)
    a1 = min_switch(M, D, g, l, t, s_of(t), s_of(t))
    a2 = min_switch(M, D, g, l, t, pp + 0.05 * t * t, pm + 0.05 * t * t)
    print('%.2e  %+.2e  %+.2e   %.4f          %.4f' % (t, pp - s_of(t), pm - s_of(t), a1 / t, a2 / t), flush=True)
