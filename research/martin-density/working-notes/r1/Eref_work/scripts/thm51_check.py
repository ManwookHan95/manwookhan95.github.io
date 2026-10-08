import numpy as np
rng = np.random.default_rng(7)
s = lambda t: np.sqrt(1+t*t)
worst = -np.inf
for trial in range(300):
    rho = rng.uniform(0.05, 0.999)
    K0 = 10**rng.uniform(-2, 3)
    kap0 = 10**rng.uniform(-2, 3)
    e1 = (1-rho**2)/8
    J = int(np.ceil(2*rho*K0/e1))
    tstar = min(1.0, 2*e1/(rho**2*kap0), np.sqrt(8*e1))
    sJ = (1-rho**2)*tstar*J/(6*rho*K0)
    sJ = min(sJ, 1.0)  # s_0 = 1 say
    sj = sJ * 2.0**(np.arange(1, J+1) - J)
    ts = np.concatenate([np.logspace(-6, 4, 4000)])
    for t in ts:
        # worst case: each component saturates its bound
        fine = sj < t
        trans = s(rho*t) + rho*K0*t*sj; loc = np.where(~fine, 1 + 0.5*rho**2*t**2*(1 + kap0*rho*t), np.inf); val = np.where(np.isfinite(loc), loc, trans) if t <= tstar else trans
        B = val.mean()
        # the proof uses the inequality chain only; check B <= s(t)
        diff = (B - s(t)) / max(t*t, 1e-300) if t < 1 else (B - s(t))/t
        worst = max(worst, diff)
        if B > s(t) + 1e-12*max(1,t):
            print("VIOLATION", trial, rho, K0, kap0, J, t, B, s(t)); break
print("worst normalized excess (should be <= 0):", worst)
