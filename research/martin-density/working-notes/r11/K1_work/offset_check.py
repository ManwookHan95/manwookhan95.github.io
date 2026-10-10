"""K1 sanity check: one-sidedness of a bank-with-offset lever along the degenerate direction.

Model (Q2 Prop 4.1 / Cor 4.2 linearization): F(P, P0) = F0 + N P - pi p P0 (+ quadratic remainder),
N = I - g h^T - p q^T (one block, D = I), with N exactly degenerate (left null vector y).
The block-norm lever P0 is a BANK: total mass m(P0) = m0 + beta*P0 must stay >= 0.
Claim: along the degenerate direction the TOTAL lever position (offset + adjustment) is forced:
   y^T F0 = pi (y^T p) * P0_total   (P0_total := m0/beta + P0, the position measured from zero mass),
so the offset m0 does not create two-sidedness; if y^T F0/(pi y^T p) < 0 no admissible zero exists
(for the linearized map), whatever m0 is.
We verify with random instances: solve the bordered linear system with an offset, and compare.
"""
import numpy as np

rng = np.random.default_rng(1)

def make_degenerate(n):
    # build g, h, p, q with N = I - g h^T - p q^T singular
    while True:
        p = rng.normal(size=n); q = rng.normal(size=n) * 0.2
        if q @ p > 0.4:
            continue
        h = rng.normal(size=n)
        g0 = rng.normal(size=n)
        # choose scalar s so that det(I - s g0 h^T - p q^T) = 0
        # det(I - p q^T - s g0 h^T) = det(I - p q^T) * (1 - s h^T (I - p q^T)^{-1} g0)
        A = np.eye(n) - np.outer(p, q)
        c = h @ np.linalg.solve(A, g0)
        if abs(c) < 0.3:
            continue
        s = 1.0 / c
        g = s * g0
        N = A - np.outer(g, h)
        return N, g, h, p, q

def left_null(N):
    u, sv, vt = np.linalg.svd(N.T)
    return vt[-1], sv[-1]

trials = 2000
bad_sign = 0
max_resid = 0.0
for _ in range(trials):
    n = rng.integers(3, 8)
    N, g, h, p, q = make_degenerate(n)
    y, smin = left_null(N)
    pi = rng.uniform(0.2, 1.0)
    F0 = rng.normal(size=n) * 1e-3
    m0_over_beta = rng.uniform(0.0, 0.05)   # offset (in lever units), may be large compared with |F0|
    # bordered system with the offset already applied at the base point:
    # F(P, Q) = F0 - pi p m0/beta + N P - pi p Q, unknowns (P, Q), Q = adjustment from the offset
    L = np.hstack([N, (-pi * p)[:, None]])
    rhs = -(F0 - pi * p * m0_over_beta)
    sol, *_ = np.linalg.lstsq(L, rhs, rcond=None)
    resid = np.linalg.norm(L @ sol - rhs)
    max_resid = max(max_resid, resid)
    # every solution has the same Q-component modulo the kernel of L; the kernel of L has Q = 0
    # (since N's kernel direction has zero Q-component in the bordered map); check:
    Q = sol[-1]
    total = m0_over_beta + Q
    predicted_total = (y @ F0) / (pi * (y @ p))
    assert abs(total - predicted_total) < 1e-8 * max(1.0, abs(predicted_total)), (total, predicted_total)
    if predicted_total < 0:
        bad_sign += 1

print(f"trials={trials}, max residual of bordered solve={max_resid:.2e}")
print(f"total lever position equals y^T F0/(pi y^T p) in every trial (offset-independent)")
print(f"fraction of trials where the forced total bank position is NEGATIVE (infeasible for a bank): {bad_sign/trials:.3f}")
