# Canonical truncation f_N: a' = a, z' = z on {0} cup K'[1..N], 0 beyond. Test (i) the single-contact direction
# at a contact j <= N: is it still a mate direction (second-order on both sides)? (ii) support function at x_*.
import numpy as np, sys, warnings, cvxpy as cp
warnings.filterwarnings("ignore")
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/refP1')
from model import *

def fibre_support(M, f, xnorm, xstar, ts):
    # max g(xstar) s.t. g(xnorm) = 0 and p*(f + t g) <= s(t) for t in ts (outer approximation of C(f))
    n, K = M['n'], M['K']; g = cp.Variable(n); cons = [g @ xnorm == 0]
    for t in ts:
        A = cp.Variable(n); W = cp.Variable(K); s = np.sqrt(1+t*t)
        cons += [A + (cp.multiply(M['lam'], W)) @ M['Us'] == f + t*g,
                 cp.norm(A, 1) + cp.norm(cp.multiply(M['sig'], A), 2) <= s,
                 cp.norm(W, 'inf') + cp.norm(cp.multiply(M['Phi'], W), 2) <= s]
    prob = cp.Problem(cp.Maximize(g @ xstar), cons)
    try: prob.solve(solver=cp.CLARABEL)
    except Exception: prob.solve(solver=cp.SCS, eps=1e-9, max_iters=100000)
    return prob.value, g.value

ts = np.concatenate([-np.logspace(-4, 1, 11)[::-1], np.logspace(-4, 1, 11)])
for seed in range(3):
    M = build(seed); nK = M['nK']; u = M['u']; zhat = M['zhat']
    f, w, _ = first_row(M, zhat)
    j1, j2 = 1, 2                                     # two contacts (indices in K')
    xstar = np.zeros(M['n']); xstar[j1] = 1; xstar[j2] = -u[j1]/u[j2]
    hf, gf = fibre_support(M, f, zhat, xstar, ts)
    print(f"seed {seed}: at f      : max g(x*) over discretized C(f)   = {hf:.5f}   (u(x*) = {u@xstar:.1e})")
    for N in [8, 5]:
        z = M['z'].copy(); z[1+N:1+nK] = 0.0           # contacts beyond N removed
        x = z + M['sig']*M['e']
        fN, wN, _ = first_row(M, x)
        tauN = -(u @ x)
        hN, gN = fibre_support(M, fN, x, xstar, ts)
        # single contact direction at j1 (still a contact at f_N)
        g = np.zeros(M['n']); g[j1] = 1.0; g[0] = -x[j1]*M['alpha']
        r = [(t, round((pstar(M, fN + t*g) - 1)/abs(t), 5)) for t in [-1e-3, -1e-4, -1e-5]]
        print(f"   N={N}: tail tau_N={tauN:.2e}, w'_2={wN[1]:.2e}; max g(x*) over C(f_N) = {hN:.2e};"
              f" contact dir (p*-1)/|t| at t<0: {r}")
