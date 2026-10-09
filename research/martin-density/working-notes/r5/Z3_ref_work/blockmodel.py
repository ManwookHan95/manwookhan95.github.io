"""Finite block model (one block): Phi_k weights, zeta = lam * U (U_k plays u_k(zhat)), N(w) = ||w||_inf + ||Phi w||_2.
norming(zeta) returns the norming functional w of zeta for |.|_Phi together with M, C, sigma=|zeta|_Phi (clamp formula,
certified by N(w) = 1 and <w, zeta> = sigma)."""
import numpy as np

def norming(zeta, Phi, iters=64):
    a = np.abs(zeta)
    def C_of_s(s):
        v = a / (Phi * s)
        lo, hi = 1e-14, 1 - 1e-14
        for _ in range(iters):
            c = 0.5 * (lo + hi)
            F = np.sum(np.minimum(Phi * (1 - c) / c, v) ** 2)
            if F > 1: lo = c
            else: hi = c
        return 0.5 * (lo + hi)
    def alpha_mass(s):
        c = C_of_s(s)
        v = a / (Phi * s)
        thr = Phi * (1 - c) / c
        pk = v > thr
        return np.sum(a[pk] / s - Phi[pk] ** 2 * (1 - c) / c), c
    lo, hi = 1e-8 * a.sum(), 10 * a.sum()
    for _ in range(iters):
        s = np.sqrt(lo * hi)
        mass, c = alpha_mass(s)
        if mass > 1: lo = s
        else: hi = s
    s = np.sqrt(lo * hi)
    mass, C = alpha_mass(s)
    M = 1 - C
    w = np.sign(zeta) * np.minimum(Phi * M, C * a / (Phi * s)) / Phi
    return w, M, C, s

def N(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi * w)
