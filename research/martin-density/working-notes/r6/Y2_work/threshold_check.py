"""Y2 numerics: block threshold theta(zeta) = |zeta| M / C.
Checks (1) the identities |zeta| = sum (|zeta_k| - theta Phi_k^2)_+ and |zeta|^2 = sum Phi_k^2 min(theta, |zeta_k|/Phi_k^2)^2
against an SOCP computation of the block norm and its norming functional; (2) strict monotonicity of theta:
increase |zeta| at a peak, decrease |zeta| at a strict non-peak (nonzero) => theta increases.
"""
import numpy as np, cvxpy as cp

def block_norm(zeta, Phi):
    n = len(zeta)
    w = cp.Variable(n)
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    prob.solve(solver=cp.CLARABEL)
    return prob.value, w.value

def theta_root(zeta, Phi):
    a = np.abs(zeta)
    def Psi(th):
        A = np.sum(np.maximum(a - th * Phi**2, 0.0))
        B = np.sum(Phi**2 * np.minimum(th, a / Phi**2)**2)
        return A**2 - B
    lo, hi = 0.0, 1.0
    while Psi(hi) > 0: hi *= 2
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    th = 0.5 * (lo + hi)
    nrm = np.sum(np.maximum(a - th * Phi**2, 0.0))
    return th, nrm

if __name__ == "__main__":
    rng = np.random.default_rng(7)
    worst_id, worst_mono = 0.0, np.inf
    for trial in range(300):
        n = rng.integers(5, 14)
        Phi = rng.uniform(0.02, 0.35, n) * 2.0**(-np.arange(n) * rng.uniform(0, 0.4))
        Phi *= rng.uniform(0.3, 0.95) / Phi.sum()
        zeta = rng.normal(size=n) * rng.uniform(0.01, 1.0, n)
        val, w = block_norm(zeta, Phi)
        M = np.max(np.abs(w)); C = np.linalg.norm(Phi * w)
        th_socp = val * M / C
        th, nrm = theta_root(zeta, Phi)
        worst_id = max(worst_id, abs(th - th_socp) / th, abs(nrm - val) / val)
        # monotonicity: pick a peak and a nonzero strict non-peak
        nu = np.abs(zeta) / Phi**2
        peaks = np.where(nu > th * (1 + 1e-6))[0]
        nonpk = np.where((nu < th * (1 - 1e-6)) & (np.abs(zeta) > 1e-9))[0]
        for k in peaks[:2]:
            z2 = zeta.copy(); z2[k] *= 1.05
            th2, _ = theta_root(z2, Phi)
            worst_mono = min(worst_mono, (th2 - th) / th)
        for k in nonpk[:2]:
            z2 = zeta.copy(); z2[k] *= 0.95
            th2, _ = theta_root(z2, Phi)
            worst_mono = min(worst_mono, (th2 - th) / th)
    print("max rel. discrepancy identities vs SOCP:", worst_id)
    print("min rel. increase of theta under raising moves (should be > 0):", worst_mono)

    # degenerate peak: tune zeta_k so that nu_k = theta exactly, then move it both ways
    fails = 0
    for trial in range(200):
        n = 8
        Phi = rng.uniform(0.05, 0.3, n); Phi *= 0.8 / Phi.sum()
        zeta = rng.normal(size=n)
        k = 3
        # fixed point: set |zeta_k| = theta(zeta) Phi_k^2 iteratively
        for it in range(200):
            th, _ = theta_root(zeta, Phi)
            zeta[k] = np.sign(zeta[k] if zeta[k] != 0 else 1.0) * th * Phi[k]**2
        th, _ = theta_root(zeta, Phi)
        for fac in (1.01, 0.99):
            z2 = zeta.copy(); z2[k] *= fac
            th2, _ = theta_root(z2, Phi)
            if th2 <= th: fails += 1
    print("degenerate peak: number of moves NOT raising theta (should be 0):", fails)
