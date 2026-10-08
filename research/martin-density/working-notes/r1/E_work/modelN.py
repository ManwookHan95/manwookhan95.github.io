"""Model N: one-sided block resources (near-threshold peaks of both signs) + conversion band.

Each resource i: scale lam_i, relative position rho_i (|rho|<1 off-peak with w = M rho; rho>=1 peak w=+M;
rho<=-1 peak w=-M).  At signed scale t = sigma*tau, carrying amount x_i moves the block coordinate to
w_i + sigma*x_i*tau/lam_i, which must stay in [-M, M]; at a peak only inward moves are allowed and cost
c_i |x_i| / tau per t^2, c_i = a0 * lam_i * |rho_i|.  Error cost A |eta_i - lam_i x_i| / tau (eta = frozen error),
Hilbert cost B x_i^2.  cost(t)/t^2 = min_x sum_i [...] s.t. sum x_i = S.
"""
import numpy as np

def boxes(rho, lam, tau, sigma, M):
    lo = np.empty_like(lam); hi = np.empty_like(lam); c = np.zeros_like(lam)
    off = np.abs(rho) < 1
    w = M*np.clip(rho, -1, 1)
    # sigma*x in [(-M-w) lam/tau, (M-w) lam/tau]
    a = (-M - w)*lam/tau; b = (M - w)*lam/tau
    # peaks: +M only inward (sigma x <= 0); -M only sigma x >= 0
    pp = rho >= 1; pm = rho <= -1
    b = np.where(pp, 0.0, b); a = np.where(pm, 0.0, a)
    if sigma > 0:
        lo, hi = a, b
    else:
        lo, hi = -b, -a
    return lo, hi

def solve(tau, sigma, lam, rho, eta, S, A, B, M, a0, iters=120):
    lo, hi = boxes(rho, lam, tau, sigma, M)
    cpk = np.where(np.abs(rho) >= 1, a0*lam*np.abs(rho), 0.0)/tau
    ae = A*lam/tau
    k2 = eta/lam
    if hi.sum() < S - 1e-12:
        return np.inf, None
    def xmin(mu):
        # minimize psi(x) = A|eta-lam x|/tau + cpk|x| + B x^2 - mu x on [lo,hi]; candidates
        cands = [lo, hi, np.clip(np.zeros_like(lo), lo, hi), np.clip(k2, lo, hi)]
        for s1 in (-1.0, 1.0):
            for s2 in (-1.0, 1.0):
                x = (mu - s1*cpk - s2*ae)/(2*B)
                cands.append(np.clip(x, lo, hi))
        C = np.stack(cands)
        val = A*np.abs(eta - lam*C)/tau + cpk*np.abs(C) + B*C**2 - mu*C
        idx = np.argmin(val, axis=0)
        return C[idx, np.arange(C.shape[1])]
    mlo, mhi = -1.0, 1.0
    while xmin(mlo).sum() > S: mlo *= 2
    while xmin(mhi).sum() < S: mhi *= 2
    for _ in range(iters):
        mid = 0.5*(mlo+mhi)
        if xmin(mid).sum() < S: mlo = mid
        else: mhi = mid
    x = xmin(0.5*(mlo+mhi))
    cost = np.sum(A*np.abs(eta - lam*x)/tau + cpk*np.abs(x) + B*x**2)
    return cost, x

def f_config(r, imin, imax, delta):
    idx = np.arange(imin, imax+1).astype(float)
    lam1 = r**idx
    lam = np.concatenate([lam1, lam1])
    rho = np.concatenate([np.full_like(lam1, 1+delta), np.full_like(lam1, -(1+delta))])
    return lam, rho

def sup_profile(lam, rho, eta, S, A, B, M, a0, taus):
    best = 0.0
    for t in taus:
        for sg in (1, -1):
            v = solve(t, sg, lam, rho, eta, S, A, B, M, a0)[0]
            best = max(best, v)
    return best
