"""Model M: critical cross mechanism, symmetric two-sided version.

Coordinates i (integers), scale lambda_i = r**i.  At scale tau>0 (|t|),
  P(tau) = min_x  sum_i [ A*|eta_i - lam_i*x_i|/tau + B*x_i^2 ]
           s.t. sum_i x_i = S,  |x_i| <= M*lam_i/tau,  x_i = 0 for unavailable i.
A = q0*K (error cost), B = (1-q0)/(2C) (Hilbert cost).  Mate condition: P(tau) <= 1/2.
At f: all i available, eta = 0, S = c.  At f': only i <= 0 available, eta free, S = rho*c.
"""
import numpy as np

def solve_scale(tau, lam, eta, avail, S, A, B, M, iters=200):
    U = M*lam/tau
    s = A*lam/tau
    kink = np.where(lam > 0, eta/lam, 0.0)
    def x_of(mu):
        x1 = (mu - s)/(2*B)
        x2 = (mu + s)/(2*B)
        x = np.where(x1 > kink, x1, np.where(x2 < kink, x2, kink))
        x = np.clip(x, -U, U)
        return np.where(avail, x, 0.0)
    # bracket mu
    lo, hi = -1.0, 1.0
    while x_of(lo).sum() > S: lo *= 2
    while x_of(hi).sum() < S: hi *= 2
    if np.sum(np.where(avail, U, 0)) < S - 1e-12:
        return np.inf, None
    for _ in range(iters):
        mid = 0.5*(lo+hi)
        if x_of(mid).sum() < S: lo = mid
        else: hi = mid
    x = x_of(0.5*(lo+hi))
    # fix tiny mismatch by scaling free coordinates (negligible)
    cost = np.sum(A*np.abs(eta - lam*x)/tau + B*x**2)
    return cost, x

def profile_f(r, c, A, B, M, imin=-40, imax=80, ntau=60):
    idx = np.arange(imin, imax+1)
    lam = r**idx.astype(float)
    eta = np.zeros_like(lam)
    avail = np.ones_like(lam, dtype=bool)
    taus = np.exp(np.linspace(0, np.log(1/r), ntau, endpoint=False))
    vals = [solve_scale(t, lam, eta, avail, c, A, B, M)[0] for t in taus]
    return taus, np.array(vals)

def profile_fprime(r, S, A, B, M, xfr, taus, imin=-40):
    # available i in [imin, 0]; xfr given for i in [-len(xfr)+1, 0]
    idx = np.arange(imin, 1)
    lam = r**idx.astype(float)
    eta = np.zeros_like(lam)
    J = len(xfr)
    eta[-J:] = lam[-J:]*np.asarray(xfr)
    avail = np.ones_like(lam, dtype=bool)
    vals = [solve_scale(t, lam, eta, avail, S, A, B, M)[0] for t in taus]
    return np.array(vals)

if __name__ == "__main__":
    import sys
    r = 0.5; M = 0.5
    for (A, B) in [(1.0, 0.5), (4.0, 0.5), (0.25, 0.5), (1.0, 0.1)]:
        taus, vf = profile_f(r, 1.0, A, B, M)
        gf = vf.max()
        print(f"A={A} B={B}: f-profile (c=1) max {gf:.4f} min {vf.min():.4f}")
