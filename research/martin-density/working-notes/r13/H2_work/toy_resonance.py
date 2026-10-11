# Toy check of H2 Proposition 4.1 ((U)-block one-signed resonance):
# oriented pinned ratios x (kind-(iv): one-sided x_l >= c_l after the free effective rescaling rho>0 is absorbed),
# two-sided pinned ratios y (free), tiny minors linear and homogeneous: C' [x; y] = 0 (rows = minors).
# Feasible (some realization exists) iff NOT exists lambda with (lambda^T C')_P >= 0, (lambda^T C')_Q = 0, lambda^T C' [c; *] > 0
# where the value lambda^T C'[c, y] does not depend on y because (lambda^T C')_Q = 0.
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(7)

def primal_feasible(Cp, Cq, c):
    # find x >= c, y free with Cp x + Cq y = 0 ; also allow overall positive scaling rho (absorbed: homogeneous)
    nP = Cp.shape[1]; nQ = Cq.shape[1]
    A = np.hstack([Cp, Cq]); b = np.zeros(Cp.shape[0])
    bounds = [(c[i], None) for i in range(nP)] + [(None, None)] * nQ
    res = linprog(np.zeros(nP + nQ), A_eq=A, b_eq=b, bounds=bounds, method='highs')
    return res.status == 0

def dual_certificate(Cp, Cq, c):
    # exists lambda: lambda^T Cp >= 0, lambda^T Cq = 0, lambda^T Cp c >= 1 ?
    k = Cp.shape[0]
    A_ub = -Cp.T; b_ub = np.zeros(Cp.shape[1])
    A_eq = np.vstack([Cq.T, (Cp @ c)[None, :]]); b_eq = np.concatenate([np.zeros(Cq.shape[1]), [1.0]])
    res = linprog(np.zeros(k), A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(None, None)] * k, method='highs')
    return res.status == 0

agree = 0; N = 3000; infeas = 0
for trial in range(N):
    nP = rng.integers(1, 4); nQ = rng.integers(0, 3); k = rng.integers(1, 3)
    Cp = rng.normal(size=(k, nP)); Cq = rng.normal(size=(k, nQ)) if nQ > 0 else np.zeros((k, 0))
    if rng.random() < 0.5:           # force one-signed cofactors on kind-(iv) columns sometimes
        Cp = np.abs(Cp)
        if nQ > 0 and rng.random() < 0.5: Cq[:] = 0.0
    c = rng.normal(size=nP)
    p = primal_feasible(Cp, Cq, c); d = dual_certificate(Cp, Cq, c)
    agree += (p != d); infeas += (not p)
print("trials", N, "Farkas alternative holds in", agree, "infeasible cases", infeas)
# Example 4.3: two kind-(iv) rows, one minor with positive oriented cofactors
Cp = np.array([[1.0, 0.7]]); Cq = np.zeros((1, 0))
for m in [-1e-3, -1e-6, 1e-6, 1e-3]:
    c = np.array([0.5, (m - 0.5) / 0.7])   # M(c) = c_+ + 0.7 c_- = m
    print("M(rc) = %+.1e  feasible:" % m, primal_feasible(Cp, Cq, c))
