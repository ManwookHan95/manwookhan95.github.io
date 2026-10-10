"""cert2: E^eng averaging, threshold of n' c_flat / K (subset of a dyadic window), for c_flat from 1e-1 to 1e-5.
Excess-over-1 arithmetic (stable).  Proof's sufficient condition: 4 K/(n' c) + 2 theta'/c^2 <= min(delta/4, (1-rho^2)/6)."""
import numpy as np
s = lambda t: np.sqrt(1 + t*t)
E = lambda x: x*x/(1 + s(x))
rng = np.random.default_rng(5)
def holds(rho, delta, c, K, Thi, n, nsub, theta):
    scales = Thi*2.0**(1 - np.arange(1, n + 1))
    S = np.sort(rng.choice(scales, size=nsub, replace=False))[::-1]
    eps = 2*theta*scales[-1]**2
    r = np.geomspace(scales[-1]*c*1e-3, 50, 30000)
    A = r*r/2*(1 - delta)
    B = E(rho*r)[:, None] + eps + 2*r[:, None]*K*S[None, :]
    per = np.where(r[:, None] <= c*S[None, :], A[:, None], B)
    return np.all(per.mean(axis=1) <= E(r)*(1 + 1e-12))
rho, eta0 = 0.9, 0.2
delta = (1 - rho**2*(1 + eta0/2))/2
need = 4/min(delta/4, (1 - rho**2)/6)
print(f"rho {rho}, delta {delta:.4f}; proof's sufficient threshold n'c/K >= {need:.1f}")
n = 300; nsub = 150
for c in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
    thr = None
    for X in np.geomspace(0.1, 1e4, 41):
        K = c*nsub/X; Thi = min(1.0, 0.01/K)
        if all(holds(rho, delta, c, K, Thi, n, nsub, theta=1e-9*c*c) for _ in range(2)):
            thr = X; break
    print(f"c_flat {c:.0e}: averaged bound holds from n'c/K ~ {thr:.2f}")
print("theta'/c^2 threshold at n'c/K = 2000:")
for c in [1e-1, 1e-3, 1e-5]:
    thr = None
    for Y in np.geomspace(1e-4, 10, 41)[::-1]:
        K = c*nsub/2000; Thi = min(1.0, 0.01/K)
        if all(holds(rho, delta, c, K, Thi, n, nsub, theta=Y*c*c) for _ in range(2)):
            thr = Y; break
    print(f"c_flat {c:.0e}: holds for theta'/c^2 <= ~{thr:.3g}  (proof's sufficient: 2 theta'/c^2 <= {min(delta/4,(1-rho**2)/6)/2:.4f})")
