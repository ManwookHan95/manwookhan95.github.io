"""N3: Lemma MS (minimax over the certificate hull) and its LP dual (1.3), on random finite instances.

Y = finite set of 'certificates' y_i (unit vectors); D = {Delta in V : A Delta <= 0, |Delta_l| <= rbar_l} with V = span(B).
(1) minimax: max_{Delta in D} min_i <c_i, Delta> - phi_i  ==  min_{theta in simplex} max_{Delta in D} <sum theta_i c_i, Delta> - sum theta_i phi_i
    (c_i = kappa * y_i, phi_i given), both sides computed by LP.
(2) LP duality for one z: max{c^T Delta : Delta in V, A Delta <= 0, |Delta| <= rbar} == min{sum rbar |c - A^T lam - nu| : lam >= 0, nu in V^perp}.
"""
import numpy as np
from scipy.optimize import linprog
from scipy.linalg import null_space

rng = np.random.default_rng(11)

def primal_value(c, B, A, rbar):
    # Delta = B s ; maximize c^T B s ; A B s <= 0 ; -rbar <= B s <= rbar
    k = B.shape[1]
    Aub = np.vstack([A @ B, B, -B]); bub = np.concatenate([np.zeros(A.shape[0]), rbar, rbar])
    res = linprog(-(c @ B), A_ub=Aub, b_ub=bub, bounds=[(None, None)] * k, method="highs")
    return -res.fun

def dual_value(c, B, A, rbar):
    # variables: lam (>=0, size p), w (size r) with nu = Nperp w, u (>=0, size n) with u >= |c - A^T lam - nu|
    n = len(c); p = A.shape[0]
    Np = null_space(B.T)            # basis of V^perp
    r = Np.shape[1]
    nv = p + r + n
    cost = np.concatenate([np.zeros(p + r), rbar])
    # u - (c - A^T lam - Np w) >= 0  and  u + (c - A^T lam - Np w) >= 0
    M1 = np.hstack([-A.T, -Np, -np.eye(n)]); h1 = -c          # -(A^T lam) - Np w - u <= -c   <=>  c - A^T lam - Np w <= u
    M2 = np.hstack([A.T, Np, -np.eye(n)]); h2 = c             #  A^T lam + Np w - u <= c      <=> -(c - A^T lam - Np w) <= u
    bounds = [(0, None)] * p + [(None, None)] * r + [(0, None)] * n
    res = linprog(cost, A_ub=np.vstack([M1, M2]), b_ub=np.concatenate([h1, h2]), bounds=bounds, method="highs")
    return res.fun

def maxmin(C, phi, B, A, rbar):
    # max_{s, tau} tau  s.t.  tau <= c_i^T B s - phi_i ; Delta = Bs in D
    k = B.shape[1]; m = C.shape[0]
    obj = np.concatenate([np.zeros(k), [-1.0]])
    Aub = [np.hstack([-(C @ B), np.ones((m, 1))])]; bub = [-phi]
    Aub += [np.hstack([A @ B, np.zeros((A.shape[0], 1))]), np.hstack([B, np.zeros((B.shape[0], 1))]), np.hstack([-B, np.zeros((B.shape[0], 1))])]
    bub += [np.zeros(A.shape[0]), rbar, rbar]
    res = linprog(obj, A_ub=np.vstack(Aub), b_ub=np.concatenate(bub), bounds=[(None, None)] * (k + 1), method="highs")
    return -res.fun

def minmax(C, phi, B, A, rbar):
    # min_theta [ max_{Delta in D} <C^T theta, Delta> - phi.theta ] = min_theta [ dual LP of the inner max ] - phi.theta
    m, n = C.shape; p = A.shape[0]; Np = null_space(B.T); r = Np.shape[1]
    # variables theta (m, >=0, sum 1), lam (p, >=0), w (r), u (n, >=0): minimize rbar.u - phi.theta
    nv = m + p + r + n
    cost = np.concatenate([-phi, np.zeros(p + r), rbar])
    # |C^T theta - A^T lam - Np w| <= u
    M1 = np.hstack([C.T, -A.T, -Np, -np.eye(n)]); M2 = np.hstack([-C.T, A.T, Np, -np.eye(n)])
    Aeq = np.concatenate([np.ones(m), np.zeros(p + r + n)])[None, :]
    bounds = [(0, None)] * m + [(0, None)] * p + [(None, None)] * r + [(0, None)] * n
    res = linprog(cost, A_ub=np.vstack([M1, M2]), b_ub=np.zeros(2 * n), A_eq=Aeq, b_eq=[1.0], bounds=bounds, method="highs")
    return res.fun

errs1, errs2 = [], []
for trial in range(400):
    n = rng.integers(3, 9); k = rng.integers(1, n + 1); p = rng.integers(0, 4); m = rng.integers(1, 6)
    B = rng.normal(size=(n, k)); A = rng.normal(size=(p, n)) if p > 0 else np.zeros((0, n))
    rbar = rng.uniform(0.2, 2.0, size=n)
    C = rng.normal(size=(m, n)); phi = rng.normal(size=m) * 0.3
    errs1.append(abs(maxmin(C, phi, B, A, rbar) - minmax(C, phi, B, A, rbar)))
    c = C[0]
    errs2.append(abs(primal_value(c, B, A, rbar) - dual_value(c, B, A, rbar)))
print("minimax identity  max-min vs min-max over the hull: max |difference| = %.2e over %d instances" % (max(errs1), len(errs1)))
print("LP duality (1.3): max |primal - dual| = %.2e over %d instances" % (max(errs2), len(errs2)))
