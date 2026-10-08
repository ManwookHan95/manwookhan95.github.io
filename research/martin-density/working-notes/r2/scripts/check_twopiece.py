# Sanity check of Prop 2.3 (two-piece mates) in a truncated model with diagonal U.
# Coordinates: 0 = the base coordinate "1"; 1..n-1 = contact set K' (z = +1).
import numpy as np
rng = np.random.default_rng(0)
def qstar(a, sig):
    return np.abs(a).sum() + np.linalg.norm(sig*a)
worst = -1e9
for trial in range(200):
    n = rng.integers(5, 40)
    sig = np.concatenate([[rng.uniform(0.2, 2.0)], rng.uniform(0.0, 0.5, n-1)/np.arange(1, n)])  # U = diag(sig)
    nu1 = sig[0]
    alpha = 1/(1+nu1)
    a = np.zeros(n); a[0] = alpha                     # q*(a) = 1
    e = np.zeros(n); e[0] = 1.0                       # e = U*a/||U*a|| (diagonal U)
    z = np.ones(n)                                    # z = sign a on F, z = 1 on K'
    zhat = z + sig*e                                  # zhat = z + U e
    r = rng.uniform(0.1, 1.0, n-1) * 2.0**(-np.arange(1, n))
    kappa = (r.sum() + (sig[1:]*r*e[1:]).sum())/(1+nu1)
    u0 = np.concatenate([[-kappa], r]); u = u0/qstar(u0, sig)
    assert abs(u @ zhat) < 1e-12, u @ zhat
    M = rng.uniform(0.5, 0.95); C = 1 - M; lam0 = rng.uniform(1e-3, 1e-1)
    # c small as in the proof
    nu = alpha*nu1; Unorm = sig.max()
    c = min(nu/(4*(1+Unorm)), 1/(4*(1+Unorm)), alpha/4, M*lam0, np.sqrt(3*nu/16)/Unorm,
            np.sqrt(3*C/4), 0.2/(1+Unorm))
    K1 = rng.random(n-1) < 0.5
    v = c*u
    v1K1 = np.zeros(n); v1K1[1:][K1] = v[1:][K1]
    beta = v1K1 @ zhat
    g = v1K1 - beta*a
    assert abs(g @ zhat) < 1e-12
    for t in np.linspace(-1, 1, 401):
        s = np.sqrt(1+t*t)
        if t >= 0:
            base = qstar(a + t*g, sig); block = 1.0
        else:
            base = qstar(a + t*(g - v), sig)
            W2 = -abs(t)*c/lam0
            assert abs(W2) <= M + 1e-15
            block = M + np.sqrt(C**2 + (t*c)**2)    # m = 1: Phi_1(2)/lambda_0 = 1
        worst = max(worst, max(base, block) - s)
    # large t crude bound
    assert qstar(g, sig) <= np.sqrt(2) - 1 + 1e-12
print("max over trials of max(component costs) - s(t) on |t|<=1:", worst)
