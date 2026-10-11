"""Referee sanity checks for N1 (finite-dimensional / scalar checks only).
(1) Prop 1.5(a) sharpness: Euclidean model X = R^2, f = e1*, g = e2* (so (f,g) = identity is contractive, g in C(f)),
    T = diag(1, rho).  Worst-case rank-one perturbations S = T + delta * y x^T (||y|| = ||x|| = 1) are searched over
    the angles of y and x; we record max |sin phi| / (2 sqrt(delta/(1-rho^2))) where (cos phi, sin phi) is the
    norming direction of S (top left singular vector).  Must be <= 1; the sqrt scaling is shown to be necessary.
(2) Slack inequality used in Prop 1.8:  s(t) - s(rho t) >= (1-rho^2) min(t^2,|t|)/3  on a fine grid.
(3) Prop 1.8 end-to-end in the Euclidean model with a random small perturbation (f', g') of (f, rho g):
    p*(f' + t g') <= s(t) for all |t| >= t_*.
"""
import numpy as np
rng = np.random.default_rng(7)

# (1)
worst = 0.0
for rho in [0.0, 0.3, 0.6, 0.9, 0.99]:
    for delta in [1e-4, 1e-3, 1e-2, 5e-2]:
        T = np.diag([1.0, rho])
        best = 0.0
        for a in np.linspace(0, np.pi, 181):
            for b in np.linspace(0, np.pi, 181):
                y = np.array([np.cos(a), np.sin(a)]); x = np.array([np.cos(b), np.sin(b)])
                S = T + 0.999 * delta * np.outer(y, x)
                U, s, Vt = np.linalg.svd(S)
                u = U[:, 0]
                if u[0] < 0: u = -u
                best = max(best, abs(u[1]))
        bound = 2 * np.sqrt(delta / (1 - rho ** 2))
        r = best / bound
        worst = max(worst, r)
        print(f"rho={rho:4.2f} delta={delta:7.1e}  max|sin phi|={best:.4e}  bound={bound:.4e}  ratio={r:.3f}")
print("(1) worst ratio:", round(worst, 4), "(must be <= 1; ~0.5-0.7 means sqrt scaling is sharp up to a constant)")

# (2)
t = np.concatenate([np.linspace(-50, 50, 200001), np.logspace(-8, 2, 20001)])
ok = True
for rho in np.linspace(0, 0.999, 200):
    lhs = np.sqrt(1 + t ** 2) - np.sqrt(1 + (rho * t) ** 2)
    rhs = (1 - rho ** 2) * np.minimum(t ** 2, np.abs(t)) / 3
    if np.any(lhs < rhs - 1e-15):
        ok = False
        print("slack inequality fails at rho", rho)
print("(2) slack inequality holds on grid:", ok)

# (3) Euclidean model: p = Euclidean norm on R^3, p* Euclidean. f = e1, g = e2 (g in C(f)).
fails = 0
for trial in range(2000):
    rho = rng.uniform(0, 0.99)
    eps = 10 ** rng.uniform(-6, -1.5); eta = 10 ** rng.uniform(-6, -1.5)
    f = np.array([1.0, 0, 0]); g = np.array([0, 1.0, 0])
    d1 = rng.normal(size=3); d1 *= eps / np.linalg.norm(d1)
    d2 = rng.normal(size=3); d2 *= eta / np.linalg.norm(d2)
    fp = f + d1; gp = rho * g + d2
    tstar = max(np.sqrt(6 * eps / (1 - rho ** 2)), 6 * eta / (1 - rho ** 2))
    if tstar > 1: continue
    ts = np.concatenate([np.linspace(tstar, 1, 300), np.logspace(0, 3, 300)])
    ts = np.concatenate([ts, -ts])
    vals = np.linalg.norm(fp[None, :] + ts[:, None] * gp[None, :], axis=1) - np.sqrt(1 + ts ** 2)
    if np.any(vals > 1e-12): fails += 1
print("(3) Prop 1.8 failures:", fails)
