"""J2 numerics (sanity only): C^{1,1} regularity of the frozen map used in K2.9(c) with (FC), across TRUE threshold crossings.
For random blocks with robust peaks P_f, weak peaks W (rho in (1, 1+b)), strict non-peaks, and fine carriers (true statuses), take random
directions d in value space and t in [0, T]; compare the frozen kappa_f(t) and theta_f(t) with their second-order Taylor model at t = 0:
the remainder |g(t) - g(0) - t g'(0)| / t^2 must stay bounded (C^{1,1}), while the TRUE formula-1 kappa (true A, theta) along the same path
shows a first-order remainder (|.|/t^2 blowing up like 1/t) whenever a weak peak crosses the true threshold."""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(21)

def true_block(zeta, Phi):
    nu = np.abs(zeta) / Phi**2
    def Psi(th):
        A = np.maximum(np.abs(zeta) - th * Phi**2, 0).sum(); B = (Phi**2 * np.minimum(th, nu)**2).sum(); return A**2 - B
    th = brentq(Psi, 1e-14 * nu.max(), nu.max(), xtol=1e-17, rtol=1e-15, maxiter=1000)
    return th, np.maximum(np.abs(zeta) - th * Phi**2, 0).sum(), nu

def frozen(zeta, Phi, Pf, fine):
    nu = np.abs(zeta) / Phi**2
    coarseQ = (~Pf) & (~fine)
    def Af(th): return (np.abs(zeta[Pf]) - th * Phi[Pf]**2).sum() + np.maximum(np.abs(zeta[fine]) - th * Phi[fine]**2, 0).sum()
    def Bf(th): return th**2 * (Phi[Pf]**2).sum() + (nu[coarseQ]**2 * Phi[coarseQ]**2).sum() + (Phi[fine]**2 * np.minimum(th, nu[fine])**2).sum()
    hi = (np.abs(zeta[Pf]).sum() + np.abs(zeta[fine]).sum()) / (Phi[Pf]**2).sum()
    while Af(hi) <= 0: hi *= 0.999
    th = brentq(lambda t: Af(t)**2 - Bf(t), 1e-14 * hi, hi, xtol=1e-17, rtol=1e-15, maxiter=1000)
    return th, Af(th), nu

def kappa_frozen(zeta, Phi, Pf, fine, Om):
    t, A, n = frozen(zeta, Phi, Pf, fine)
    return A + (A**2 - (n[Om]**2 * Phi[Om]**2).sum()) / t

def kappa_true(zeta, Phi, Om):
    t, A, n = true_block(zeta, Phi)
    return A + (A**2 - (n[Om]**2 * Phi[Om]**2).sum()) / t

def make(b=1e-3):
    nP, nW, nQ, nF = 2, 2, 4, 3
    K = nP + nW + nQ + nF
    Phi = np.concatenate([rng.uniform(0.05, 0.25, nP + nW + nQ), rng.uniform(1e-4, 1e-3, nF)])
    rho = np.concatenate([[np.nan], rng.uniform(1.5, 3, nP - 1), 1 + b * rng.uniform(0.05, 0.95, nW), rng.uniform(0.2, 0.9, nQ), rng.uniform(0, 0.6, nF)])
    P = np.zeros(K, bool); P[:nP + nW] = True
    a = np.sqrt((Phi[P]**2).sum() + (rho[~P]**2 * Phi[~P]**2).sum())
    rho[0] = 1 + (a - ((rho[1:nP + nW] - 1) * Phi[1:nP + nW]**2).sum()) / Phi[0]**2
    sg = rng.choice([-1.0, 1.0], K)
    Pf = np.zeros(K, bool); Pf[:nP] = True
    fine = np.zeros(K, bool); fine[nP + nW + nQ:] = True
    Om = (~Pf) & (~fine)
    return sg * rho * Phi**2, Phi, Pf, fine, Om, nP, nW

worst_frozen = 0.0; worst_true = 0.0; crossings = 0
for trial in range(150):
    zeta, Phi, Pf, fine, Om, nP, nW = make()
    d = np.zeros(len(zeta)); d[nP:nP + nW] = -np.sign(zeta[nP:nP + nW]) * Phi[nP:nP + nW]**2 * rng.uniform(0.5, 1.5, nW)  # weak peaks pushed inward
    d[:nP] = np.sign(zeta[:nP]) * Phi[:nP]**2 * rng.uniform(-0.5, 0.5, nP)
    d[Om & ~np.isin(np.arange(len(zeta)), range(nP, nP + nW))] = rng.normal(scale=0.01, size=(Om.sum() - nW))
    h0 = 1e-7
    g0 = kappa_frozen(zeta, Phi, Pf, fine, Om)
    gp = (kappa_frozen(zeta + h0 * d, Phi, Pf, fine, Om) - kappa_frozen(zeta - h0 * d, Phi, Pf, fine, Om)) / (2 * h0)
    k0 = kappa_true(zeta, Phi, Om)
    kp_right = (kappa_true(zeta + h0 * d, Phi, Om) - k0) / h0           # one-sided derivative at t = 0 (weak peaks still peaks)
    for t in [1e-2, 3e-3, 1e-3, 3e-4]:
        gt = kappa_frozen(zeta + t * d, Phi, Pf, fine, Om)
        worst_frozen = max(worst_frozen, abs(gt - g0 - t * gp) / t**2)
        kt = kappa_true(zeta + t * d, Phi, Om)
        th_t, _, n_t = true_block(zeta + t * d, Phi)
        if any(n_t[nP:nP + nW] < th_t):        # some weak peak crossed the true threshold along the path
            crossings += 1
            worst_true = max(worst_true, abs(kt - k0 - t * kp_right) / t**2)
print(f"frozen kappa_f: max |g(t) - g(0) - t g'(0)|/t^2 over t in [3e-4, 1e-2] = {worst_frozen:.3e}  (bounded: C^(1,1))")
print(f"true formula-1 kappa at {crossings} crossing points: max |k(t) - k(0) - t k'(0+)|/t^2 = {worst_true:.3e}  (large: first-order kink)")
