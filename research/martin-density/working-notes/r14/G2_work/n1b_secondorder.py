"""N1b: size of the second-order status term along the coupled block-scaling direction, versus distance to the W-fix boundary."""
import numpy as np
exec(open('n1_status_calculus.py').read().split("worst = {")[0])
rng = np.random.default_rng(7)
rows = []
for trial in range(20000):
    n = rng.integers(3, 9); m = rng.integers(1, 4); sigma = rng.uniform(0.05, 0.9)
    r = rng.normal(size=n); r *= rng.uniform(0.05, 0.95) / (m * np.linalg.norm(r))
    if np.min(np.abs(r)) < 1e-3: continue
    R2 = m**2*np.sum(r**2)
    if R2 > 1 - sigma/4: continue
    Phi = m*np.abs(r)*K(sigma,R2)/rng.uniform(0.3,1.0,size=n)
    N = [d for d in range(n) if rng.random() < 0.4] or [0]
    l = rng.integers(n); kp = kprime(sigma, R2)
    cd = ((1.0 if l in N else 0.0)/abs(r[l]) + 2*kp*m**2*abs(r[l]))/(1+2*kp*R2)
    vd = np.zeros(n); vd[l] = np.sign(r[l]); vd = vd - cd*r
    nv = np.linalg.norm(vd/r, np.inf); h = 1e-4/max(1, nv)
    rho0 = statuses(r, m, Phi, sigma); rho1 = statuses(r+h*vd, m, Phi, sigma)
    incr = np.max(np.log(rho1[N]) - np.log(rho0[N]))
    if not np.isfinite(incr): continue
    rows.append(((1 - sigma/4) - R2, incr/(h*(1+nv))**2, kp))
rows = np.array(rows)
for lo, hi in [(0, 0.01), (0.01, 0.05), (0.05, 0.2), (0.2, 1.0)]:
    sel = (rows[:,0] >= lo) & (rows[:,0] < hi)
    if sel.any():
        print("slack in [%.2f,%.2f): n=%5d  max second-order ratio %.3e   max kappa' %.3e" % (lo, hi, sel.sum(), rows[sel,1].max(), rows[sel,2].max()))
