"""cert2: scalar check of Theorem E^eng's averaging with window-dependent c_flat and a (class, cube) SUBSET of scales.
Per-piece upper bounds (the only inputs of the proof):
   (A) |r| <= c t_i :  1 + (r^2/2)(1 - delta)
   (B) always      :  s(rho r) + eps' + 2 |r| K t_i
Average over a random subset S of the dyadic window {T_hi 2^{1-i}}, |S| = n', and test  avg(r) <= s(r)  on a dense r-grid.
We scan c (= c_flat) down to tiny values and record the least n' c / K for which the inequality holds, to confirm that the
proof's requirement is a condition on n' c / K (plus theta'/c^2 -> 0), with no hidden dependence on c otherwise.
"""
import numpy as np
s = lambda t: np.sqrt(1 + t*t)
rng = np.random.default_rng(3)

def ok(rho, delta, c, K, Thi, n, nsub, theta):
    scales = Thi*2.0**(1 - np.arange(1, n + 1))
    S = np.sort(rng.choice(scales, size=nsub, replace=False))[::-1]
    Tmin = scales[-1]
    eps = 2*theta*Tmin**2                         # eps'_j <= 2 theta' T_min^2
    r = np.concatenate([np.geomspace(1e-30, 50, 40000), -np.geomspace(1e-30, 50, 400)])
    E = lambda x: x*x/(1 + s(x))                 # s(x) - 1, computed stably
    A = r*r/2*(1 - delta)
    B = E(rho*r)[:, None] + eps + 2*np.abs(r)[:, None]*K*S[None, :]
    per = np.where(np.abs(r)[:, None] <= c*S[None, :], A[:, None], B)
    avg = per.mean(axis=1)
    return np.all(avg <= E(r)*(1 + 1e-12))

rho, eta0 = 0.9, 0.2
delta = (1 - rho**2*(1 + eta0/2))/2
print(f"rho {rho} delta {delta:.4f}")
for c in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
    K = 5.0; Thi = 1e-3*c/K; n = 60
    # smallest subset size for which the averaged bound holds (theta tiny), and the resulting n' c / K
    best = None
    for nsub in range(1, n + 1):
        if all(ok(rho, delta, c, K, Thi, n, nsub, theta=1e-6*c*c) for _ in range(3)):
            best = nsub; break
    print(f"c_flat {c:.0e}: least |S| = {best}, |S| c_flat / K = {best*c/K if best else float('nan'):.3e}")
# theta'/c^2 dependence: with |S| c/K large, increase theta until failure
c = 1e-3; K = 5.0; Thi = 1e-3*c/K; n = 60
for th_over_c2 in [1e-4, 1e-3, 1e-2, 1e-1, 1.0]:
    print(f"theta'/c^2 = {th_over_c2:.0e}: holds = {all(ok(rho, delta, c, K, Thi, n, 60, theta=th_over_c2*c*c) for _ in range(3))}")
