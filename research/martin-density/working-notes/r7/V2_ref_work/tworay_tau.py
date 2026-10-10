"""
Two-ray example of V2 2.1 embedded in tau-coordinates of an exact-cone system (sanity only).
Carriers 1,2 in block 1, carriers 3,4 in block 2; configuration rows tau_1 = tau_3, tau_2 = tau_4 (two-block rays
r1 = e1+e3, r2 = e2+e4), tau >= 0, d-rows (Z5): v1 tau1 + v2 tau2 = 0 (block 1), v3 tau3 + v4 tau4 = 0 (block 2).
With v = (1, -1, 1, -1+delta) the ray d-vectors are (1,1), (-1,-1+delta).
Checks: (i) the 4x4 minor containing both d-rows equals +-delta = +-(v1 v4 - v2 v3) (a minor of A_kappa(v));
(ii) the true l1 Hoffman ratio dist_1(tau, P)/viol_1(tau) is ~ 1/delta, while at delta = 0 (minor exactly 0) it is bounded;
(iii) Lemma H (1.3) bound with the least NONZERO minor dominates the true ratio.
"""
import itertools
import numpy as np
import cvxpy as cp

def system(delta):
    v = np.array([1.0, -1.0, 1.0, -1.0 + delta])
    E = np.array([[1, 0, -1, 0], [0, 1, 0, -1],            # configuration equalities
                  [v[0], v[1], 0, 0], [0, 0, v[2], v[3]]],  # d-rows
                 dtype=float)
    A = -np.eye(4)                                          # tau >= 0
    return A, E

def least_nonzero_minor(Mfull, tol=1e-13):
    p, n = Mfull.shape
    best = np.inf
    for k in range(1, n + 1):
        for J in itertools.combinations(range(p), k):
            for K in itertools.combinations(range(n), k):
                d = abs(np.linalg.det(Mfull[np.ix_(J, K)]))
                if d > tol: best = min(best, d)
    return best

rng = np.random.default_rng(3)
for delta in [1e-1, 1e-2, 1e-3, 1e-4, 0.0]:
    A, E = system(delta)
    full4 = np.linalg.det(E)
    worst = 0.0
    pts = [rng.exponential(size=4) for _ in range(200)]
    # points ON the configuration cone C = cone{r1, r2} (the dangerous directions)
    pts += [m1*np.array([1.0, 0, 1.0, 0]) + m2*np.array([0, 1.0, 0, 1.0]) for (m1, m2) in rng.exponential(size=(100, 2))]
    pts += [np.array([1.0, 1.0, 1.0, 1.0])]
    for tau in pts:
        viol = np.abs(E @ tau).sum() + np.maximum(A @ tau, 0).sum()
        x = cp.Variable(4)
        prob = cp.Problem(cp.Minimize(cp.norm1(x - tau)), [A @ x <= 0, E @ x == 0])
        prob.solve(solver=cp.CLARABEL)
        if viol > 1e-9: worst = max(worst, prob.value / viol)
    Mfull = np.vstack([A, E])
    dmin = least_nonzero_minor(Mfull)
    nrm = np.linalg.norm(Mfull, 2)
    bound = max(1, nrm) ** 3 / dmin * np.sqrt(4) * 1.0   # l2->l1 conversion factor sqrt(n); residual l1 >= l2
    print(f"delta={delta:7.1e}: det(E)={full4: .3e}, true l1 Hoffman ratio={worst:9.3e}, least nonzero minor={dmin:.3e}, "
          f"Lemma H bound={bound:9.3e}, ratio/bound={worst/bound:.3f}")
