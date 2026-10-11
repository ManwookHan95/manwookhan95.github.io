# Independent check of Theorem H2.A's case analysis in a richer linear model:
#  - private generators: kind (i) two-sided e_l, kind (iv) one-sided +e_l, both perturbed by a common-mode column eps_cm * g
#  - block kappa levers: column -rt^{(m)}, direction two / up (d >= 0) / down (d <= 0)
#  - optional SHARED two-sided generators (random sparse columns across rows of different carriers, "target-coordinate moves")
#  - overshoot bands sigma_l in [0, beta] on banded rows (free K^- rows always; free K^+ rows where 'bandable')
# Realization: f0 + G t - sigma = 0 with t in its cone, sigma in Box.  H2.A predicts feasibility for EVERY bounded rhs when no block is residual.
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(11)

def feasible(rows, levers, beta, f0, eps_cm, g, shared):
    nR = len(rows); nB = len(levers); nS = shared.shape[1]
    nvar = nR + nR + nB + nS
    A = np.zeros((nR, nvar))
    for i, r in enumerate(rows):
        A[:, i] += eps_cm * g          # common-mode part of the private generator of row i
        A[i, i] += 1.0
        A[i, nR + i] = -1.0
        A[i, 2 * nR + r['m']] = -r['rt']
    A[:, 2 * nR + nB:] = shared
    bounds = [((0, None) if r['kind'] == 'iv' else (None, None)) for r in rows]
    bounds += [((0, beta) if r['banded'] else (0, 0)) for r in rows]
    bounds += [{'two': (None, None), 'up': (0, None), 'down': (None, 0)}[lt] for lt in levers]
    bounds += [(None, None)] * nS
    res = linprog(np.zeros(nvar), A_eq=A, b_eq=-f0, bounds=bounds, method='highs')
    return res.status == 0

def residual(rows, levers):
    for m, lt in enumerate(levers):
        Pp = [r for r in rows if r['m'] == m and r['kind'] == 'iv' and r['rt'] > 0 and not r['banded']]
        Pm = [r for r in rows if r['m'] == m and r['kind'] == 'iv' and r['rt'] < 0 and not r['banded']]
        if (lt == 'two' and Pp and Pm) or (lt == 'up' and Pm) or (lt == 'down' and Pp):
            return True
    return False

stats = dict(pred_ok=0, pred_ok_fail=0, resid=0, resid_infeas_private=0, resid_rescued_by_shared=0)
for trial in range(1500):
    nB = int(rng.integers(1, 4)); levers = list(rng.choice(['two', 'up', 'down'], size=nB))
    rows = []
    for m in range(nB):
        for _ in range(int(rng.integers(2, 5))):
            kind = str(rng.choice(['i', 'iv'], p=[0.3, 0.7]))
            rt = float(rng.choice([-1, 1]) * rng.uniform(0.2, 2.0))
            banded = (kind == 'iv') and (rng.random() < 0.5)
            rows.append(dict(m=m, kind=kind, rt=rt, banded=banded))
    nR = len(rows); g = rng.normal(size=nR); eps_cm = 1e-3
    no_shared = np.zeros((nR, 0))
    shared = np.zeros((nR, 2))
    for k in range(2):
        idx = rng.choice(nR, size=min(2, nR), replace=False); shared[idx, k] = rng.normal(size=len(idx))
    res = residual(rows, levers)
    rhs = [rng.normal(size=nR) for _ in range(30)]
    rhs = [f / max(1.0, np.linalg.norm(f)) for f in rhs]
    if not res:
        stats['pred_ok'] += 1
        if not all(feasible(rows, levers, 50.0, f, eps_cm, g, no_shared) for f in rhs):
            stats['pred_ok_fail'] += 1
    else:
        stats['resid'] += 1
        bad = [f for f in rhs if not feasible(rows, levers, 50.0, f, eps_cm, g, no_shared)]
        if bad:
            stats['resid_infeas_private'] += 1
            if all(feasible(rows, levers, 50.0, f, eps_cm, g, shared) for f in bad):
                stats['resid_rescued_by_shared'] += 1
print(stats)
