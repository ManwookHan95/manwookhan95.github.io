"""Componentwise cvxpy cross-check of the threshold structure (A, M, C, off-peak w), with rescaling for conditioning."""
import numpy as np, cvxpy as cp, mpmath as mp, random, warnings
warnings.filterwarnings('ignore')
import importlib.util, sys
spec = importlib.util.spec_from_file_location('ib', 'indep_block.py')
src = open('indep_block.py').read().split('# ---------- (1)')[0]
ns = {}; exec(src, ns); solve_E = ns['solve_E']
random.seed(7)
rows = []
for trial in range(12):
    n = random.randint(4, 7); m = random.randint(1, 2)
    Phi = np.array([2.0**(-(k + 1)) * random.uniform(0.5, 1) for k in range(n)])
    zeta = np.array([random.choice([-1, 1]) * Phi[k]**2 * random.uniform(0, 4) for k in range(n)])
    w = cp.Variable(n); t = cp.Variable()
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') <= t, cp.norm(cp.multiply(Phi, w), 2) <= 1 - t])
    prob.solve(solver='CLARABEL', tol_gap_abs=1e-14, tol_gap_rel=1e-14, tol_feas=1e-14, max_iter=500)
    A, th, M, C, nu, P = solve_E([mp.mpf(z) for z in zeta], [mp.mpf(p) for p in Phi])
    wv = w.value
    offP = [k for k in range(n) if k not in P]
    eA = abs(prob.value - float(A)) / float(A); eM = abs(t.value - float(M)); eC = abs(np.linalg.norm(Phi * wv) - float(C))
    ew = max([abs(wv[k] - float(C * zeta[k] / (Phi[k]**2 * A))) for k in offP] + [0])
    rows.append((eA, eM, eC, ew, len(P)))
for r in rows: print("relA %.1e  M %.1e  C %.1e  w_offP %.1e  |P|=%d" % r)
