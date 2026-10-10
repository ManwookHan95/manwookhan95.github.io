"""
Toy sanity check of Theorem B's mechanism (determinantal exactification), V2-ref.  NOT a proof.
Three blocks, three TWO-BLOCK rays (r1: blocks 1,2; r2: blocks 2,3; r3: blocks 1,3), six carriers with values v.
tau-system: tau >= 0, configuration rows tau_a = tau_b along each ray, (Z5)-rows sum_{carriers of block m} v_l tau_l = 0.
Random values are perturbed so that the 3x3 d-determinant (and possibly some 2x2 minors) are TINY (~beta).
Step A: enumerate all square minors containing >= 1 (Z5)-row (multi-affine polynomials in v); classify tiny (<= beta) /
        robust (>= u) / band.  Step B: nearest common zero v' of the tiny minors (SLSQP, equality constraints).
Step C: check |v' - v| ~ beta^{2/N} (here N = 2 typically), robust minors stay >= u/2, tiny ones are ~0, and the true l1
        Hoffman ratio max dist_1(tau, P)/viol_1(tau) drops from ~1/beta to O(1), bounded by Lemma H with least NONZERO minor.
"""
import itertools
import numpy as np
import cvxpy as cp
from scipy.optimize import minimize

# carriers: 0:(b1,r1) 1:(b2,r1) 2:(b2,r2) 3:(b3,r2) 4:(b1,r3) 5:(b3,r3)
block = [0, 1, 1, 2, 0, 2]
pairs = [(0, 1), (2, 3), (4, 5)]

def matrices(v):
    n = 6
    E = []
    for (a, b) in pairs:
        row = np.zeros(n); row[a] = 1; row[b] = -1; E.append(row)
    D = []
    for m in range(3):
        row = np.zeros(n)
        for l in range(n):
            if block[l] == m: row[l] = v[l]
        D.append(row)
    A = -np.eye(n)
    return A, np.array(E), np.array(D)

def dminors(v):
    """all square minors of [A; E; D] that contain >= 1 D-row and no row with its negative (A rows are -e_l only)."""
    A, E, D = matrices(v)
    M = np.vstack([A, E, D]); p = M.shape[0]; drows = set(range(p - 3, p))
    out = {}
    for k in range(1, 7):
        for J in itertools.combinations(range(p), k):
            if not (set(J) & drows): continue
            for K in itertools.combinations(range(6), k):
                out[(J, K)] = np.linalg.det(M[np.ix_(J, K)])
    return out

def hoffman_ratio(v, rng, npts=150):
    A, E, D = matrices(v)
    Eq = np.vstack([E, D]); worst = 0.0
    pts = [rng.exponential(size=6) for _ in range(npts)]
    # points on the configuration cone (rays), where the d-rows are the only violated rows
    for _ in range(npts):
        mu = rng.exponential(size=3); tau = np.zeros(6)
        for i, (a, b) in enumerate(pairs): tau[a] = tau[b] = mu[i]
        pts.append(tau)
    pts.append(np.ones(6))   # tau* = r1 + r2 + r3 (mu = (1,1,1)): the near-kernel direction of the ray d-matrix
    for tau in pts:
        viol = np.abs(Eq @ tau).sum() + np.maximum(A @ tau, 0).sum()
        x = cp.Variable(6)
        cp.Problem(cp.Minimize(cp.norm1(x - tau)), [A @ x <= 0, Eq @ x == 0]).solve(solver=cp.CLARABEL)
        if viol > 1e-12: worst = max(worst, (cp.norm1(x - tau).value) / viol)
    return worst

rng = np.random.default_rng(11)
for trial in range(4):
    beta = 10.0 ** (-2 - trial)
    u = 0.05
    # values: start robust, then tune v[5] so that det of the 3x3 ray d-matrix is ~ beta
    # near-kernel direction mu* = (1,1,1) > 0: block equations v0 + v4 ~ 0, v1 + v2 ~ 0, v3 + v5 ~ 0
    s0 = rng.uniform(0.5, 1.0, size=3)
    eps_ = beta * rng.uniform(0.2, 1.0, size=3) * rng.choice([-1, 1], size=3)
    v = np.array([s0[0], s0[1], -s0[1] + eps_[1], s0[2], -s0[0] + eps_[0], -s0[2] + eps_[2]])
    def detray(vv):
        Dm = np.zeros((3, 3))
        for i, (a, b) in enumerate(pairs):
            Dm[block[a], i] += vv[a]; Dm[block[b], i] += vv[b]
        return np.linalg.det(Dm)
    mins = dminors(v)
    tiny = [k for k, val in mins.items() if 1e-13 < abs(val) <= 3*beta]
    band = [k for k, val in mins.items() if 3*beta < abs(val) < u]
    robust = [k for k, val in mins.items() if abs(val) >= u]
    def pi(vv, key):
        A, E, D = matrices(vv); M = np.vstack([A, E, D]); J, K = key
        return np.linalg.det(M[np.ix_(J, K)])
    cons = [{'type': 'eq', 'fun': (lambda vv, key=key: pi(vv, key))} for key in tiny]
    res = minimize(lambda vv: np.sum((vv - v) ** 2), v, constraints=cons, method='SLSQP',
                   options={'ftol': 1e-15, 'maxiter': 500})
    vp = res.x
    mins2 = dminors(vp)
    max_tiny_after = max([abs(mins2[k]) for k in tiny], default=0.0)
    min_robust_after = min([abs(mins2[k]) for k in robust], default=np.inf)
    h_before = hoffman_ratio(v, rng); h_after = hoffman_ratio(vp, rng)
    nz_after = [abs(x) for x in mins2.values() if abs(x) > 1e-9]
    print(f"beta={beta:.0e}: det(ray d-matrix)={detray(v):.1e} #tiny={len(tiny)} #band={len(band)} #robust={len(robust)}  |v'-v|={np.linalg.norm(vp - v):.2e}"
          f"  max tiny after={max_tiny_after:.1e}  min robust after={min_robust_after:.3f}"
          f"  Hoffman l1 ratio before={h_before:.2e} after={h_after:.2e}  least nonzero minor after={min(nz_after):.3f}")
