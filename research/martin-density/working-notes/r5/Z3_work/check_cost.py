"""Sanity check for Z3 Lemma 3.1 (cost of a companion), one block.
zeta(k) = lambda_k * U_k  (U_k plays the role of q_0 u_k(zhat)), lambda_k = m Phi_k.
Perturbation: U_k -> U_k + dU_k  (dU_k plays u_k(delta)).
Compare L := sum_k lambda_k |w'(k) - w(k)| with R := Delta*log(e/Delta) + sum_k min(lambda_k, |dU_k|),
Delta := sum_k lambda_k |dU_k|.  Lemma 3.1 claims L <= C_f R for small Delta (C_f depends on the block).
Norming functional via the clamp formula; |zeta|_Phi via the alpha-mass equation (bisection), certified by N(w)=1, <w,zeta>=|zeta|.
"""
import numpy as np
rng = np.random.default_rng(7)

def norming(zeta, Phi):
    # returns w, M, C, s=|zeta|
    a = np.abs(zeta)
    def C_of_s(s):
        v = a / (Phi * s)
        lo, hi = 1e-12, 1 - 1e-12
        for _ in range(200):
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
    lo, hi = 1e-6 * a.sum(), 10 * a.sum()
    for _ in range(200):
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

m = 1
n = 30
worst = 0.0
cert = 0.0
for trial in range(300):
    Phi = 0.5 ** (np.arange(n) + 2) * rng.uniform(0.5, 1.0, n)
    lam = m * Phi
    U = rng.normal(size=n)
    zeta = lam * U
    w, M, C, s = norming(zeta, Phi)
    cert = max(cert, abs(N(w, Phi) - 1), abs(np.dot(w, zeta) - s) / s)
    for eps in [1e-3, 1e-4, 1e-5]:
        dU = np.zeros(n)
        # unweighted-large perturbations at a few fine coordinates, plus a small global one
        idx = rng.choice(np.arange(10, n), size=3, replace=False)
        dU[idx] = rng.normal(size=3) * 0.5
        dU += eps * rng.normal(size=n)
        z2 = lam * (U + dU)
        w2, M2, C2, s2 = norming(z2, Phi)
        L = np.sum(lam * np.abs(w2 - w))
        Delta = np.sum(lam * np.abs(dU))
        R = Delta * np.log(np.e / Delta) + np.sum(np.minimum(lam, np.abs(dU)))
        worst = max(worst, L / R)
print("certification error of the norming functionals (should be ~1e-10):", cert)
print("max L/R over trials (bounded => consistent with Lemma 3.1):", worst)
