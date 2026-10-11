# Toy check of H2 Theorem 3.3 (per-block case analysis for one-sided rows, kappa levers, one-sided bands).
# Ratio-form Step A, nonlinear in kappa: rows l in block m: val_l + P_l (kind iv, P>=0) or val_l + t_l (kind i, free)
# must equal rt_l * kappa_m' (+ sigma_l, sigma in [0,beta] for banded rows), kappa_m' = kappa_m + d_m (lever type).
# Exact feasibility is decided by an LP in (P, t, d, sigma) (the equations are linear in these unknowns for fixed rt).
# Near-certificates: Farkas dual of the LP. We compare feasibility over random right-hand sides with the prediction.
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(1)

def feasible(rows, levers, beta, kappa, f0):
    # rows: list of dicts {m, kind ('i','iv'), rt, banded}
    # unknowns: for each row: P_l (iv: >=0) or t_l (i: free); sigma_l (banded: [0,beta]); for each block: d_m
    nR = len(rows); nB = len(levers)
    nvar = nR + nR + nB
    A = np.zeros((nR, nvar)); b = np.zeros(nR)
    bounds = []
    for i, r in enumerate(rows):
        A[i, i] = 1.0                     # P or t
        A[i, nR + i] = -1.0               # -sigma
        A[i, 2 * nR + r['m']] = -r['rt']  # -rt * d_m
        b[i] = -f0[i]                     # val - rt*kappa = f0  => f0 + P - rt d - sigma = 0
    for r in rows:
        bounds.append((0, None) if r['kind'] == 'iv' else (None, None))
    for r in rows:
        bounds.append((0, beta) if r['banded'] else (0, 0))
    for lt in levers:
        bounds.append({'two': (None, None), 'up': (0, None), 'down': (None, 0), 'none': (0, 0)}[lt])
    res = linprog(np.zeros(nvar), A_eq=A, b_eq=b, bounds=bounds, method='highs')
    return res.status == 0

def predicted_ok(rows, levers):
    # Theorem 3.3: realized for every rhs unless some block has an unbanded kind-(iv) configuration of type (two)/(up)/(down)/(none)
    for m, lt in enumerate(levers):
        Kp = [r for r in rows if r['m'] == m and r['kind'] == 'iv' and r['rt'] > 0 and not r['banded']]
        Km = [r for r in rows if r['m'] == m and r['kind'] == 'iv' and r['rt'] < 0 and not r['banded']]
        if lt == 'two' and Kp and Km: return False
        if lt == 'up' and Km: return False
        if lt == 'down' and Kp: return False
        if lt == 'none' and (Kp or Km): return False
    return True

agree = 0; tot = 0; mism = []
for trial in range(4000):
    nB = rng.integers(1, 4)
    levers = list(rng.choice(['two', 'up', 'down', 'none'], size=nB))
    rows = []
    for m in range(nB):
        for _ in range(rng.integers(1, 5)):
            kind = rng.choice(['i', 'iv'])
            rt = rng.choice([-1, 1]) * rng.uniform(0.2, 2.0)
            banded = bool(rng.random() < 0.4) if kind == 'iv' else False
            rows.append(dict(m=m, kind=kind, rt=rt, banded=banded))
    beta = 50.0
    pred = predicted_ok(rows, levers)
    # "realized for all rhs in the unit ball": test many random rhs; infeasible for some rhs <=> obstruction
    allok = True
    for k in range(40):
        f0 = rng.normal(size=len(rows)); f0 /= max(1.0, np.linalg.norm(f0))
        if not feasible(rows, levers, beta, 1.0, f0):
            allok = False; break
    tot += 1; agree += (allok == pred)
    if allok != pred: mism.append((levers, rows))
print("trials", tot, "agree", agree, "mismatches", len(mism))
if mism:
    print(mism[0])
