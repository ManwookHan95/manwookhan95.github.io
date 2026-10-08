# N5: Theorem 12.4'(i) test. Finite model: X* = R^n with q*(a) = ||a||_1 + ||G a||_2, V = R^r Hilbert,
# L* = M (n x r).  f = a + M w with supp a = F finite, base contact z with |z_j| <= 0.7 off F.
# g = b0 + M v0 split mate.  For each t, compute D(t) = max deviation |W - (w + t v0)| over ALL
# admissible W (q*(f+tg-MW) <= s, |W| <= s, s = sqrt(1+t^2)), via bisection along rays.
import numpy as np
rng = np.random.default_rng(5)
n, h, r = 30, 4, 2
G = rng.normal(size=(h, n)) / np.sqrt(n)
M = rng.normal(size=(n, r)) * (0.6 ** np.arange(n))[:, None]       # columns = L*e_i, l1-summable
def qs(x): return np.abs(x).sum() + np.linalg.norm(G @ x)
F = [0, 1, 2]
a = np.zeros(n); a[F] = rng.normal(size=3); a /= qs(a)
h0 = G @ a / np.linalg.norm(G @ a)
z = rng.uniform(-0.7, 0.7, size=n); z[F] = np.sign(a[F])
xihat = z + G.T @ h0                                    # q**-normer of a
assert abs(a @ xihat - 1) < 1e-12
Lxi = M.T @ xihat                                       # L** xihat in V
w = Lxi / np.linalg.norm(Lxi)
q0 = 1 / (1 + np.linalg.norm(Lxi))
f = a + M @ w
# split mate g = b0 + M v0: b0 supported in F with b0(xihat)=0; v0 orthogonal to w; scale small
b0 = np.zeros(n); b0[F] = rng.normal(size=3); b0 -= (b0 @ xihat) * a
v0 = rng.normal(size=r); v0 -= (v0 @ w) * w
scale = 1.0
for _ in range(80):
    ok = all(qs(a + t*scale*b0) <= np.sqrt(1+t*t) + 1e-14 and np.linalg.norm(w + t*scale*v0) <= np.sqrt(1+t*t) + 1e-14
             for t in np.linspace(-3, 3, 241))
    if ok: break
    scale *= 0.8
b0 *= scale; v0 *= scale
g = b0 + M @ v0
print("q0 = %.4f, margin 1-max|z_off| = %.3f, |b0|=%.3e, |v0|=%.3e" % (q0, 1 - np.max(np.abs(np.delete(z, F))), np.abs(b0).sum(), np.linalg.norm(v0)))
def feasible(W, t):
    s = np.sqrt(1 + t*t)
    return qs(f + t*g - M @ W) <= s + 1e-15 and np.linalg.norm(W) <= s + 1e-15
for t in [0.2, -0.2, 0.1, -0.1, 0.05, 0.025, -0.025, 0.0125, 0.00625]:
    W0 = w + t*v0
    assert feasible(W0, t)
    D = 0.0
    for th in np.linspace(0, 2*np.pi, 721)[:-1]:
        e = np.array([np.cos(th), np.sin(th)])
        lo, hi = 0.0, 1.0
        while feasible(W0 + hi*e, t): hi *= 2
        for _ in range(60):
            mid = 0.5*(lo+hi)
            if feasible(W0 + mid*e, t): lo = mid
            else: hi = mid
        D = max(D, lo)
    print("t=%+.5f  D(t)=%.3e  D/|t|=%.3e  D/t^2=%.3f" % (t, D, D/abs(t), D/(t*t)))
