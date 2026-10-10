"""Referee (a): independent check of Q2 Proposition 4.1 (explicit right inverse of the bordered d-consistency map) and of the
capacitance/Woodbury structure claimed in 4.0; adversarial: exactly degenerate square system (det C = 0), c_alpha = 0, beta_* = 0,
and the doubly degenerate case (both zero), where no right inverse can exist.
L(P, P0) = D P - g (h.P) - sum_m p_m (q_m.P) - pi p_{m*} P0,  D = I + X (absorber rows, X^2 = 0, q_m^T X = 0).
"""
import numpy as np
rng = np.random.default_rng(5)

def build(nb=3, sizes=(3, 2, 3), nabs=2):
    n0 = sum(sizes); n = n0 + nabs
    idx = []; s = 0
    for sz in sizes:
        idx.append(list(range(s, s + sz))); s += sz
    p = []; q = []
    for m in range(nb):
        pm = np.zeros(n); qm = np.zeros(n)
        pm[idx[m]] = rng.uniform(-1, 1, len(idx[m]))
        qm[idx[m]] = rng.uniform(-1, 1, len(idx[m]))
        qm *= rng.uniform(0.05, 0.5) / max(abs(qm @ pm), 1e-3)      # q^T p in (-0.5, 0.5)
        if qm @ pm > 0.5: qm *= 0.5 / (qm @ pm)
        p.append(pm); q.append(qm)
    X = np.zeros((n, n))
    for a in range(n0, n):
        X[a, :n0] = rng.uniform(-0.5, 0.5, n0)                         # absorber rows; columns of Omega^0 only
    g = rng.uniform(-1, 1, n); h = rng.uniform(-1, 1, n)
    return n, np.eye(n) + X, X, g, h, p, q

def quantities(Dm, g, h, p, q, ms):
    Di = np.linalg.inv(Dm)
    ca = 1 - h @ Di @ g - sum((h @ Di @ p[m]) * (q[m] @ Di @ g) / (1 - q[m] @ p[m]) for m in range(len(p)) if m != ms)
    bs = h @ Di @ p[ms]
    return ca, bs

def right_inverse(b, Dm, g, h, p, q, ms, pi_, beta0):
    Di = np.linalg.inv(Dm)
    ca, bs = quantities(Dm, g, h, p, q, ms)
    rhs = h @ Di @ b + sum((h @ Di @ p[m]) * (q[m] @ Di @ b) / (1 - q[m] @ p[m]) for m in range(len(p)) if m != ms)
    if abs(bs) >= beta0:
        al, gs = 0.0, -rhs / bs
    else:
        al, gs = rhs / ca, 0.0
    gam = {m: (q[m] @ Di @ b + (q[m] @ Di @ g) * al) / (1 - q[m] @ p[m]) for m in range(len(p)) if m != ms}
    gam[ms] = gs
    P = Di @ (b + g * al + sum(p[m] * gam[m] for m in gam))
    P0 = (gs - q[ms] @ P) / pi_
    return P, P0

def Lmap(P, P0, Dm, g, h, p, q, ms, pi_):
    return Dm @ P - g * (h @ P) - sum(p[m] * (q[m] @ P) for m in range(len(p))) - pi_ * p[ms] * P0

res_max, ratio_max, sq_det_err, n_deg = 0.0, 0.0, 0.0, 0
for trial in range(3000):
    n, Dm, X, g, h, p, q = build()
    ms = rng.integers(0, 3); pi_ = rng.choice([-1, 1]) * rng.uniform(0.05, 1)
    mode = trial % 3
    Di = np.linalg.inv(Dm)
    if mode == 1:      # force beta_* = 0 by adjusting h along a direction
        v = Di @ p[ms]; h = h - (h @ v) / (v @ v) * v
    if mode == 2:      # force c_alpha = 0 by scaling the g-component (c_alpha is affine in g for fixed others)
        ca0, _ = quantities(Dm, g, h, p, q, ms)
        # c_alpha(g) = 1 - k^T g with k := Di^T h + sum (h Di p_m)/(1 - q p) Di^T q_m ; choose g := g + t k/|k|^2
        k = Di.T @ h + sum((h @ Di @ p[m]) / (1 - q[m] @ p[m]) * (Di.T @ q[m]) for m in range(3) if m != ms)
        g = g + (ca0) / (k @ k) * k
    ca, bs = quantities(Dm, g, h, p, q, ms)
    beta0 = max(abs(ca), abs(bs))
    if beta0 < 1e-8:
        n_deg += 1; continue
    # capacitance determinant check for the square system (P0 = 0)
    Nmat = Dm - np.outer(g, h) - sum(np.outer(p[m], q[m]) for m in range(3))
    Cm = np.eye(4); cols = [g] + p; rows = [h] + q
    Cm = np.eye(4) - np.array([[rows[i] @ Di @ cols[j] for j in range(4)] for i in range(4)])
    sq_det_err = max(sq_det_err, abs(np.linalg.det(Nmat) - np.linalg.det(Dm) * np.linalg.det(Cm)) / max(1, abs(np.linalg.det(Nmat))))
    b = rng.uniform(-1, 1, n)
    P, P0 = right_inverse(b, Dm, g, h, p, q, ms, pi_, beta0)
    r = Lmap(P, P0, Dm, g, h, p, q, ms, pi_) - b
    res_max = max(res_max, np.abs(r).max())
    KD = 1 + np.abs(X).sum(1).max(); Q = sum(np.abs(qm).sum() for qm in q); pb = max(np.abs(pm).max() for pm in p)
    H = np.abs(h).sum(); Kc = 4 * (1 + 1 / abs(pi_)) * KD**4 * (1 + pb)**2 * (1 + Q)**3 * (1 + H) * (1 + np.abs(g).max()) * (1 + 1 / beta0)
    ratio_max = max(ratio_max, (np.abs(P).max() + abs(P0)) / (Kc * np.abs(b).max()))
print(f"residual max {res_max:.2e}; max (|P|+|P0|)/(K|b|) {ratio_max:.2e}; Woodbury det rel err {sq_det_err:.2e}; skipped doubly-degenerate {n_deg}")
# doubly degenerate case: c_alpha = beta_* = 0 -> the bordered map has a left null vector y; check y^T L = 0
n, Dm, X, g, h, p, q = build(); ms = 0; pi_ = 0.7; Di = np.linalg.inv(Dm)
v = Di @ p[ms]; h = h - (h @ v) / (v @ v) * v
k = Di.T @ h + sum((h @ Di @ p[m]) / (1 - q[m] @ p[m]) * (Di.T @ q[m]) for m in range(3) if m != ms)
ca0, _ = quantities(Dm, g, h, p, q, ms); g = g + ca0 / (k @ k) * k
ca, bs = quantities(Dm, g, h, p, q, ms)
y = Di.T @ (h + sum((h @ Di @ p[m]) / (1 - q[m] @ p[m]) * q[m] for m in range(3) if m != ms))
Lfull = np.column_stack([np.column_stack([Lmap(e, 0.0, Dm, g, h, p, q, ms, pi_) for e in np.eye(n)]), Lmap(np.zeros(n), 1.0, Dm, g, h, p, q, ms, pi_)])
print(f"doubly degenerate: c_alpha={ca:.1e}, beta_*={bs:.1e}, |y^T L| = {np.abs(y @ Lfull).max():.1e} (left null vector y = D^-T (h + sum theta_m q_m)), rank {np.linalg.matrix_rank(Lfull, 1e-9)} of {n}")
