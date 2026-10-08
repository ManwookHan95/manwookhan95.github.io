# Worst-case bound chain of P1 Thm 4.3 (weighted averaging), computed with cancellation-free formulas.
import numpy as np
rng = np.random.default_rng(1)
Sm1 = lambda t: t*t/(1+np.sqrt(1+t*t))          # s(t) - 1
worst = -1
for trial in range(3000):
    rho = rng.uniform(0.01, 0.9999)
    s0 = rng.uniform(1e-4, 1.0) * min(1.0, np.sqrt(1-rho**2))
    s = np.concatenate([np.logspace(-6, 0, 400)*s0, s0*np.logspace(0, 4, 400)])
    small = s <= s0
    bm1 = np.where(small, np.maximum(s**2*(1+rho**2)/4, Sm1(rho*s)) + (1-rho**2)*s**2/12,
                   Sm1(rho*s) + (1-rho**2)*s0*s/3)
    worst = max(worst, np.max((bm1 - Sm1(s))/np.minimum(s**2, s)))
print("max over trials of (bound - s(s))/min(s^2,s):", worst)
