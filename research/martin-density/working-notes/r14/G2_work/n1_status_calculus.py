"""N1: status calculus of Lemma 2.1 (coupled directions) with the true Lemma-K function.

Lemma K (X1 / J2.1(d)): k = K(sigma, R^2) is the root k > sigma of (1 - R^2) k^2 - 2 sigma k + sigma^2 - sigma = 0,
status rho_d = m |r_d| K(sigma, R^2) / Phi_d, R^2 = m^2 sum_{Omega} r^2 (sigma fixed by the frozen peak pattern).
We check: for random blocks, protected set N, row l and partner p,
  (a) single inward displacement never raises any status at first order (and the true change is <= C h^2),
  (c) coupled direction v_lp = sgn(r_l) e_l - c_lp sgn(r_p) e_p with c_lp = (|r_l| + 1[l in N]/(2 kappa' m^2 |r_l|))/|r_p|
      has l_d(v) <= 0 for all d in N, and the true status change along h*v is <= C h^2,
  (d) v_l = sgn(r_l) e_l - c_l r with c_l = (1[l in N]/|r_l| + 2 kappa' m^2 |r_l|)/(1 + 2 kappa' R^2) likewise.
"""
import numpy as np

rng = np.random.default_rng(14)

def K(sigma, R2):
    a, bq, c = (1 - R2), -2 * sigma, sigma ** 2 - sigma
    disc = bq * bq - 4 * a * c
    return (-bq + np.sqrt(disc)) / (2 * a)

def statuses(r, m, Phi, sigma):
    R2 = m ** 2 * np.sum(r ** 2)
    return m * np.abs(r) * K(sigma, R2) / Phi

def kprime(sigma, R2, eps=1e-7):
    return (np.log(K(sigma, R2 + eps)) - np.log(K(sigma, R2 - eps))) / (2 * eps)

def lin_status(r, m, sigma, d, Delta):
    R2 = m ** 2 * np.sum(r ** 2)
    kp = kprime(sigma, R2)
    return Delta[d] / r[d] + kp * 2 * m ** 2 * np.dot(r, Delta)

worst = {"a_first": -np.inf, "c_first": -np.inf, "d_first": -np.inf, "a_sec": 0.0, "c_sec": 0.0, "d_sec": 0.0}
ntr = 0
for trial in range(4000):
    n = rng.integers(3, 9)
    m = rng.integers(1, 4)
    sigma = rng.uniform(0.05, 0.9)
    # ratios with R^2 well inside the W-fix region
    r = rng.normal(size=n)
    r *= rng.uniform(0.05, 0.6) / (m * np.linalg.norm(r))
    if np.min(np.abs(r)) < 1e-3:
        continue
    R2 = m ** 2 * np.sum(r ** 2)
    if R2 > 1 - sigma / 4:
        continue
    Phi = m * np.abs(r) * K(sigma, R2) / rng.uniform(0.3, 1.0, size=n)   # statuses in [0.3, 1)
    N = [d for d in range(n) if rng.random() < 0.4]
    if not N:
        N = [0]
    l, p = rng.choice(n, size=2, replace=False)
    kp = kprime(sigma, R2)
    rho0 = statuses(r, m, Phi, sigma)
    h = 1e-4
    # (a) inward single displacement of l
    va = np.zeros(n); va[l] = -np.sign(r[l]) * abs(r[l])
    # (c) coupled
    cl = (abs(r[l]) + (1.0 if l in N else 0.0) / (2 * kp * m ** 2 * abs(r[l]))) / abs(r[p])
    vc = np.zeros(n); vc[l] = np.sign(r[l]); vc[p] = -cl * np.sign(r[p])
    # (d) block-scaling coupling
    cd = ((1.0 if l in N else 0.0) / abs(r[l]) + 2 * kp * m ** 2 * abs(r[l])) / (1 + 2 * kp * R2)
    vd = np.zeros(n); vd[l] = np.sign(r[l]); vd = vd - cd * r
    hstep = h / max(1.0, np.linalg.norm(vc / r, np.inf), np.linalg.norm(vd / r, np.inf))
    if m ** 2 * np.sum((r + hstep * vc) ** 2) > 1 - sigma / 8 or m ** 2 * np.sum((r + hstep * vd) ** 2) > 1 - sigma / 8:
        continue
    for key, v in (("a", va), ("c", vc), ("d", vd)):
        firsts = [lin_status(r, m, sigma, d, v) for d in N]
        worst[key + "_first"] = max(worst[key + "_first"], max(firsts))
        hv = 1e-3 / max(1.0, np.linalg.norm(v / r, np.inf))      # per-direction step, relative move <= 1e-3
        rho1 = statuses(r + hv * v, m, Phi, sigma)
        incr = np.max(np.log(rho1[N]) - np.log(rho0[N]))
        assert np.isfinite(incr)
        if incr > 1e-12:                                          # ignore rounding noise
            worst[key + "_sec"] = max(worst[key + "_sec"], incr / (hv * (1 + np.linalg.norm(v / r, np.inf))) ** 2)
    ntr += 1

print("trials:", ntr)
print("max first-order l_d over d in N:  inward %.3e   coupled(partner) %.3e   coupled(block scaling) %.3e"
      % (worst["a_first"], worst["c_first"], worst["d_first"]))
print("max (true log-status increase)/(h(1+||v||_rt))^2 [increments > 1e-12]:  inward %.3e   partner %.3e   scaling %.3e"
      % (worst["a_sec"], worst["c_sec"], worst["d_sec"]))
