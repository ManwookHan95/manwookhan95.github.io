# Sanity check of Lemma 4.1 (exact transfer of pure base mates along truncations)
# finite model: X = R^n with q*(a) = ||a||_1 + ||U^T a||_2, U: R^d -> R^n with decaying rows (compact-like).
import numpy as np
rng = np.random.default_rng(1)
n, d = 60, 8
U = rng.standard_normal((n, d)) * (0.5 ** (np.arange(n) / 6.0))[:, None] * 0.3
def qstar(x):
    return np.abs(x).sum() + np.linalg.norm(U.T @ x)
s = lambda t: np.sqrt(1 + t * t)
# base vector a with full support, geometric decay, mixed signs
a = (0.7 ** np.arange(n)) * rng.choice([-1, 1], n)
a = a / qstar(a)
nu = np.linalg.norm(U.T @ a); e = U.T @ a / nu
z = np.sign(a); zhat = z + U @ e
# candidate base direction b0 supported in F with flips at all scales (ratio |b0|/|a| unbounded along the tail)
b0 = (0.85 ** np.arange(n)) * rng.standard_normal(n)
b0 = b0 - (b0 @ zhat) * a   # balance: b0(zhat) = 0  (a(zhat) = 1)
ts = np.concatenate([-np.logspace(-6, 2, 400), np.logspace(-6, 2, 400)])
def ok(c, aa, bb):
    return all(qstar(aa + t * c * bb) <= s(t) + 1e-13 for t in ts)
# largest c with c*b0 a pure base mate at a (bisection)
lo, hi = 0.0, 10.0
for _ in range(60):
    mid = (lo + hi) / 2
    (lo, hi) = (mid, hi) if ok(mid, a, b0) else (lo, mid)
c = lo; b = c * b0
print("max scaling c =", c, " check a(zhat)=", a @ zhat, " b(zhat)=", b @ zhat)
for rho in [0.9, 0.99]:
    for M in [5, 10, 20, 30, 40]:
        aM = a.copy(); aM[M:] = 0; aM = aM / qstar(aM)
        nuM = np.linalg.norm(U.T @ aM); eM = U.T @ aM / nuM
        zM = z.copy()           # far values irrelevant (b^M supported in [1,M])
        zhatM = zM + U @ eM
        bM = b.copy(); bM[M:] = 0
        kap = bM @ zhatM; bM = bM - kap * aM
        worst = max(qstar(aM + t * rho * bM) - s(t) for t in ts)
        print(f"rho={rho} M={M:3d}  ||b^M-b||_1={np.abs(bM-b).sum():.2e}  max_t [q*(a^M+t rho b^M)-s(t)] = {worst:.3e}")
print("--- ratios (q*-1)/(s(t)-1); must be <= 1 ---")
ts2 = np.concatenate([-np.logspace(-4, 2, 600), np.logspace(-4, 2, 600)])
r0 = max((qstar(a + t*b) - 1)/(s(t)-1) for t in ts2)
print("at f itself (tightness of b):", r0)
for rho in [0.9, 0.99]:
    for M in [5, 10, 20, 30, 40]:
        aM = a.copy(); aM[M:] = 0; aM = aM / qstar(aM)
        nuM = np.linalg.norm(U.T @ aM); eM = U.T @ aM / nuM
        zhatM = z + U @ eM
        bM = b.copy(); bM[M:] = 0; bM = bM - (bM @ zhatM) * aM
        r = max((qstar(aM + t*rho*bM) - 1)/(s(t)-1) for t in ts2)
        # also the flip comparison Fl^M <= rho Fl_b
        print(f"rho={rho} M={M:3d} max ratio = {r:.4f}")
