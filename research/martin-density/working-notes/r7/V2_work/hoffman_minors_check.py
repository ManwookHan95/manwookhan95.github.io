"""
V2 numerics (sanity only): Lemma H (Hoffman bound via linearly independent row subsets and via minors).
For random small systems A x <= b (with P nonempty) and random x:
  dist_2(x, P) <= ||(Ax-b)_+||_2 * max_{J lin.indep.} 1/sigma_min(A_J)          (bound 1)
  1/sigma_min(A_J) <= ||A_J||_2^{|J|-1} / max_K |det A_{J,K}|                    (bound 2, per J)
Also: the 2-ray determinantal example of V2 part 2 (Hoffman ratio blows up like 1/delta, finite at delta = 0).
"""
import itertools
import numpy as np
import cvxpy as cp

rng = np.random.default_rng(7)

def proj_dist(A, b, x):
    n = A.shape[1]
    y = cp.Variable(n)
    prob = cp.Problem(cp.Minimize(cp.sum_squares(y - x)), [A @ y <= b])
    prob.solve(solver=cp.CLARABEL)
    return np.sqrt(max(prob.value, 0.0)), y.value

def lin_indep_subsets(A, tol=1e-10):
    p = A.shape[0]
    out = []
    for r in range(1, min(p, A.shape[1]) + 1):
        for J in itertools.combinations(range(p), r):
            M = A[list(J), :]
            s = np.linalg.svd(M, compute_uv=False)
            if s[-1] > tol * max(1.0, s[0]):
                out.append((J, s[-1]))
    return out

def max_minor(MJ):
    k, n = MJ.shape
    best = 0.0
    for K in itertools.combinations(range(n), k):
        best = max(best, abs(np.linalg.det(MJ[:, list(K)])))
    return best

worst1 = 0.0
worst2 = 0.0
ntests = 0
for trial in range(300):
    n = rng.integers(2, 5)
    p = rng.integers(2, 8)
    A = rng.normal(size=(p, n))
    if trial % 3 == 0:  # make some rows nearly dependent / duplicated with sign (equalities)
        A[1] = -A[0]
    x0 = rng.normal(size=n)
    b = A @ x0 + rng.exponential(size=p) * (rng.random(p) < 0.5)
    subsets = lin_indep_subsets(A)
    H1 = max(1.0 / s for (J, s) in subsets)
    # per-J minor bound
    for (J, s) in subsets:
        MJ = A[list(J), :]
        mm = max_minor(MJ)
        normJ = np.linalg.norm(MJ, 2)
        bound2 = normJ ** (len(J) - 1) / mm
        worst2 = max(worst2, (1.0 / s) / bound2)
    for _ in range(5):
        x = rng.normal(size=n) * 3
        r = np.maximum(A @ x - b, 0.0)
        d, _ = proj_dist(A, b, x)
        rhs = np.linalg.norm(r) * H1
        if rhs > 1e-12:
            worst1 = max(worst1, d / rhs)
        ntests += 1
print(f"Lemma H: {ntests} tests; max dist/(H1*residual) = {worst1:.4f} (must be <= 1)")
print(f"Lemma H: max over J of (1/sigma_min)/(minor bound) = {worst2:.4f} (must be <= 1)")

# 2-ray determinantal example: d-vectors D1 = (1, 1), D2 = (-1, -1 + delta), cone {mu >= 0}, Z = {mu >= 0: M mu = 0}
print("2-ray example: ratio dist_1(mu, Z)/|M mu|_1 at mu = (1,1):")
for delta in [1e-1, 1e-2, 1e-3, 1e-4, 0.0]:
    M = np.array([[1.0, -1.0], [1.0, -1.0 + delta]])
    mu = np.array([1.0, 1.0])
    e = M @ mu
    # Z: mu' >= 0, M mu' = 0 ; minimize ||mu - mu'||_1
    v = cp.Variable(2)
    prob = cp.Problem(cp.Minimize(cp.norm1(mu - v)), [v >= 0, M @ v == 0])
    prob.solve(solver=cp.CLARABEL)
    dist = prob.value
    det = np.linalg.det(M)
    ratio = dist / max(np.abs(e).sum(), 1e-300) if np.abs(e).sum() > 0 else 0.0
    print(f"  delta={delta:8.1e}  det={det: .2e}  dist={dist:.4f}  |M mu|_1={np.abs(e).sum():.2e}  ratio={ratio:.3e}")
# at delta = 0 check the worst ratio over random mu
M = np.array([[1.0, -1.0], [1.0, -1.0]])
worst = 0.0
for _ in range(200):
    mu = rng.exponential(size=2)
    e = M @ mu
    v = cp.Variable(2)
    prob = cp.Problem(cp.Minimize(cp.norm1(mu - v)), [v >= 0, M @ v == 0])
    prob.solve(solver=cp.CLARABEL)
    if np.abs(e).sum() > 1e-9:
        worst = max(worst, prob.value / np.abs(e).sum())
print(f"  delta = 0: worst ratio over 200 random mu = {worst:.4f} (bounded)")
