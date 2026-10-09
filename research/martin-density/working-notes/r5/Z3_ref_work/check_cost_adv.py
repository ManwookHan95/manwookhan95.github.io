"""Adversarial check of Z3 Lemma 3.1 in the one-block model (m = 1): FIXED blocks with many strict non-peaks and several
near-threshold coordinates; perturbations dU (= u_k(delta)) of adversarial shapes with Delta -> 0;
L := sum lam|w# - w|, R := Delta log(e/Delta) + sum min(lam, |dU|).  Lemma 3.1: sup_Delta L/R < infinity for each fixed block."""
import numpy as np
from blockmodel import norming
rng = np.random.default_rng(5)
n = 22
res = {}
npk = []
for trial in range(12):
    Phi = 0.5 ** (np.arange(n) + 2) * rng.uniform(0.5, 1.0, n)
    lam = Phi.copy()
    U = rng.normal(size=n)
    U[:3] = 3.0 * np.sign(U[:3])                       # a few robust coarse peaks
    w, M, C, s = norming(lam * U, Phi)
    for _ in range(3):                                  # fine coordinates around the threshold Phi_k M s / C (m = 1)
        thr = Phi * M * s / C
        U[3:] = thr[3:] * rng.uniform(0.2, 1.8, n - 3) * rng.choice([-1, 1], n - 3)
        w, M, C, s = norming(lam * U, Phi)
    thr = Phi * M * s / C
    near = np.argsort(np.abs(np.abs(U[3:]) / thr[3:] - 1))[:4] + 3   # closest to the threshold (either side)
    pk = np.abs(w) >= M * (1 - 1e-12)
    npk.append(pk.sum())
    for shape in ["near", "peak", "sparsefine", "allmin"]:
        worst = 0.0
        for eps in 10.0 ** np.arange(-4, -10, -1.0):
            dU = np.zeros(n)
            if shape == "near":
                dU[near] = np.sign(U[near]) * eps * thr[near] / thr[near].max()   # push across the threshold
            elif shape == "peak":
                k = 0; dU[k] = -np.sign(U[k]) * eps
            elif shape == "sparsefine":
                idx = rng.choice(np.arange(n // 2, n), size=3, replace=False)
                dU[idx] = rng.choice([-1, 1], 3) * np.minimum(lam[idx], eps * 1e3)
            else:
                dU = rng.choice([-1, 1], n) * np.minimum(lam, eps)
            w2, M2, C2, s2 = norming(lam * (U + dU), Phi)
            L = np.sum(lam * np.abs(w2 - w))
            Delta = np.sum(lam * np.abs(dU))
            R = Delta * np.log(np.e / Delta) + np.sum(np.minimum(lam, np.abs(dU)))
            worst = max(worst, L / R)
        res.setdefault(shape, []).append(worst)
print("number of peaks per block:", npk)
for k, v in res.items():
    print(f"{k:11s}: sup_Delta L/R per block: median {np.median(v):.3g}, max {np.max(v):.3g}")
