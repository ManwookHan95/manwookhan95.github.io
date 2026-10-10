"""K1 referee: the correct bordered scalars for a block-norm lever realized by an S-mass (P4) lever on a coarse peak k* of block m*.

Linearization (Q2 4.0 / Prop 4.1 notation, D = I + X, route V: X = 0 allowed):
   L(P, P0) = D P - g (h^T P) - sum_m p_m (q_m^T P) - (pi p_{m*} + h0 g) P0,
the last column being the private block-norm action -pi p_{m*} plus the common mode -h0 g of the peak's S-mass step (h0 = |A(s)|/(nu |u_{k*}(s)|)).
Claim (referee, re-derived from Q2 Prop. 4.1's proof): L is onto with an explicit right inverse as soon as max(|c'_alpha|, |beta'_*|) >= beta_0 > 0, where
   c'_alpha := c_alpha + (h0/pi) q_{m*}^T D^{-1} g,      beta'_* := beta_* + (h0/pi)(1 - q_{m*}^T p_{m*}),
c_alpha, beta_* being Q2's scalars.  Conversely, if c'_alpha = beta'_* = 0 then L is not onto.  We test both statements and the explicit inverse.
"""
import numpy as np
rng = np.random.default_rng(23)

def instance():
    M = int(rng.integers(1, 4))
    sizes = rng.integers(1, 4, size=M)
    n = int(sizes.sum())
    idx = np.split(np.arange(n), np.cumsum(sizes)[:-1])
    p = [np.zeros(n) for _ in range(M)]; q = [np.zeros(n) for _ in range(M)]
    for m in range(M):
        while True:
            pm = rng.normal(size=len(idx[m])); qm = rng.normal(size=len(idx[m])) * 0.3
            if pm @ qm <= 0.45:
                break
        p[m][idx[m]] = pm; q[m][idx[m]] = qm
    X = np.zeros((n, n))
    D = np.eye(n) + X
    g = rng.normal(size=n); h = rng.normal(size=n)
    return n, M, D, g, h, p, q

def scalars(D, g, h, p, q, mstar):
    Di = np.linalg.inv(D)
    M = len(p)
    ca = 1 - h @ Di @ g - sum((h @ Di @ p[m]) * (q[m] @ Di @ g) / (1 - q[m] @ p[m]) for m in range(M) if m != mstar)
    bs = h @ Di @ p[mstar]
    return ca, bs, Di

worst_res, worst_ratio, n_onto_fail_when_zero, n_zero_cases, n_cases = 0.0, 0.0, 0, 0, 0
for trial in range(3000):
    n, M, D, g, h, p, q = instance()
    mstar = int(rng.integers(0, M))
    pi = rng.uniform(0.2, 1.0) * rng.choice([-1, 1])
    ca, bs, Di = scalars(D, g, h, p, q, mstar)
    qs, ps = q[mstar], p[mstar]
    # generic h0
    h0 = rng.normal() * 2
    cap = ca + (h0 / pi) * (qs @ Di @ g)
    bsp = bs + (h0 / pi) * (1 - qs @ ps)
    Lmat = np.hstack([D - np.outer(g, h) - sum(np.outer(p[m], q[m]) for m in range(M)), (-(pi * ps + h0 * g))[:, None]])
    b = rng.normal(size=n)
    # explicit right inverse (referee's derivation)
    rhs0 = h @ Di @ b + sum((h @ Di @ p[m]) * (q[m] @ Di @ b) / (1 - q[m] @ p[m]) for m in range(M) if m != mstar)
    rhs = rhs0 - (h0 / pi) * (qs @ Di @ b)
    if abs(bsp) >= abs(cap):
        alpha, gs = 0.0, -rhs / bsp
    else:
        gs, alpha = 0.0, rhs / cap
    gam = [((q[m] @ Di @ b) + (q[m] @ Di @ g) * alpha) / (1 - q[m] @ p[m]) if m != mstar else gs for m in range(M)]
    P = Di @ (b + g * alpha + sum(p[m] * gam[m] for m in range(M)))
    P0 = ((1 - qs @ ps) * gs - qs @ Di @ b - (qs @ Di @ g) * alpha) / pi
    res = np.abs(Lmat @ np.concatenate([P, [P0]]) - b).max()
    if max(abs(cap), abs(bsp)) > 1e-2:
        n_cases += 1
        worst_res = max(worst_res, res / (1 + np.abs(P).max() + abs(P0)))
    # converse: choose h0 to make beta'_* = 0 and check whether c'_alpha = 0 too and L not onto
    h0z = -pi * bs / (1 - qs @ ps)
    capz = ca + (h0z / pi) * (qs @ Di @ g)
    Lz = np.hstack([D - np.outer(g, h) - sum(np.outer(p[m], q[m]) for m in range(M)), (-(pi * ps + h0z * g))[:, None]])
    smin = np.linalg.svd(Lz, compute_uv=False)[-1]
    if abs(capz) < 1e-9:
        n_zero_cases += 1
        if smin > 1e-8:
            n_onto_fail_when_zero += 1
print(f"explicit right inverse with (c'_alpha, beta'_*): {n_cases} instances, max relative residual {worst_res:.2e}")
print(f"instances where beta'_* = 0 forces c'_alpha = 0 (N degenerate, one-block-like): {n_zero_cases}; among them L still onto: {n_onto_fail_when_zero}")

# doubly degenerate Q2 case (c_alpha = beta_* = 0): a (P4) peak lever with h0 != 0 has beta'_* = (h0/pi)(1 - q^T p) != 0
cnt, ok = 0, 0
for trial in range(2000):
    n = int(rng.integers(3, 7))
    p = rng.normal(size=n); q = rng.normal(size=n) * 0.3
    if p @ q > 0.45:
        continue
    # make beta_* = h^T p = 0 and c_alpha = 1 - h^T g = 0
    h = rng.normal(size=n); h -= (h @ p) / (p @ p) * p
    g = rng.normal(size=n); g = g / (h @ g)
    N = np.eye(n) - np.outer(g, h) - np.outer(p, q)
    pi = rng.uniform(0.2, 1.0)
    s_pure = np.linalg.svd(np.hstack([N, (-pi * p)[:, None]]), compute_uv=False)[-1]
    h0 = rng.uniform(0.2, 2.0)
    s_p4 = np.linalg.svd(np.hstack([N, (-(pi * p + h0 * g))[:, None]]), compute_uv=False)[-1]
    cnt += 1
    ok += (s_pure < 1e-9) and (s_p4 > 1e-4)
print(f"Q2 doubly degenerate case: {cnt} instances; pure column fails and (P4)-type column succeeds in {ok}")
