"""Lemma SLP sanity check: primal V = max{-Xi.delta : a_d.delta <= 0 (d in N), |delta|_inf <= 1}, a_d(E) = 1[d in E] + 2 kp R2_E,
dual W = min{ ||Xi + A^T lambda||_1 : lambda >= 0 }.  Random instances; also the resonance instances of (*) give V ~ 0."""
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(7)
def primal(Xi, A):
    M = len(Xi)
    res = linprog(Xi, A_ub=A if len(A) else None, b_ub=np.zeros(len(A)) if len(A) else None, bounds=[(-1, 1)]*M, method='highs')
    return -res.fun
def dual(Xi, A):
    M = len(Xi); n = len(A)
    if n == 0: return np.abs(Xi).sum()
    # variables lambda (n), p (M), q (M): Xi + A^T lambda = p - q, minimize sum p + q
    c = np.concatenate([np.zeros(n), np.ones(2*M)])
    Aeq = np.hstack([A.T, -np.eye(M), np.eye(M)]); beq = -Xi
    res = linprog(c, A_eq=Aeq, b_eq=beq, bounds=[(0, None)]*(n + 2*M), method='highs')
    return res.fun
worst = 0
for trial in range(300):
    M = rng.integers(2, 7); kp = rng.uniform(0.1, 3); R2 = rng.uniform(0.01, 0.5, M)
    owner = rng.integers(-1, M, rng.integers(0, 4))           # protected rows: owner object (-1 = in no object)
    A = np.array([[(1.0 if E == o else 0.0) + 2*kp*R2[E] for E in range(M)] for o in owner]) if len(owner) else np.zeros((0, M))
    Xi = rng.normal(size=M)
    worst = max(worst, abs(primal(Xi, A) - dual(Xi, A)))
print(f"random instances: max |V_primal - W_dual| = {worst:.2e}")
# resonance instance: objects without protected rows with Xi_E = -2 kp Lam R2_E, protected object with Xi = -(lam + 2 kp Lam R2)
M = 4; kp = 0.7; R2 = np.array([0.1, 0.2, 0.05, 0.3]); owner = [3]; lam = 0.4; Lam = 0.4
A = np.array([[(1.0 if E == 3 else 0.0) + 2*kp*R2[E] for E in range(M)]])
Xi = -2*kp*Lam*R2; Xi[3] -= lam
print(f"exact resonance (*): V = {primal(Xi, A):.2e} (expected 0); perturbed by 1e-3 in one object: V = {primal(Xi + np.array([1e-3, 0, 0, 0]), A):.2e}")
Xi2 = Xi.copy(); Xi2[0] = +0.05    # an aligned object: relief
print(f"one aligned object: V = {primal(Xi2, A):.2e} (> 0: lever exists)")
