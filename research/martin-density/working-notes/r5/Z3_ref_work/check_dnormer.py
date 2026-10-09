"""Lemma 1.2: d(omega) = <omega, zeta>/sigma for omega supported on strict non-peaks, and the companion identity
sigma# d#(omega) - sigma d(omega) = sum_k omega_k lam_k dU_k  (dU_k = u_k(delta)), in the one-block model, m = 1."""
import numpy as np
from blockmodel import norming, N
rng = np.random.default_rng(11)
n = 25; worst_a = 0.0; worst_b = 0.0; cert = 0.0
for trial in range(150):
    Phi = 0.5 ** (np.arange(n) + 2) * rng.uniform(0.5, 1.0, n)
    lam = Phi.copy()
    U = rng.normal(size=n)
    w, M, C, s = norming(lam * U, Phi)
    cert = max(cert, abs(N(w, Phi) - 1), abs(np.dot(w, lam * U) - s) / s)
    dU = 1e-3 * rng.normal(size=n) * rng.uniform(0, 1, n)
    w2, M2, C2, s2 = norming(lam * (U + dU), Phi)
    Q = (np.abs(w) < M * (1 - 1e-9)) & (np.abs(w2) < M2 * (1 - 1e-9))
    om = np.zeros(n); idx = np.where(Q)[0]
    if len(idx) == 0: continue
    om[idx] = rng.normal(size=len(idx))
    d1 = np.dot(Phi * w, Phi * om) / C
    d2 = np.dot(Phi * w2, Phi * om) / C2
    worst_a = max(worst_a, abs(d1 - np.dot(om, lam * U) / s) / (1 + abs(d1)))
    lhs = s2 * d2 - s * d1
    rhs = np.dot(om, lam * dU)
    worst_b = max(worst_b, abs(lhs - rhs) / (abs(rhs) + 1e-12 * (1 + abs(s * d1))))
print("certification error:", cert)
print("Lemma 1.2(a) max rel. error:", worst_a)
print("Lemma 1.2(b) max rel. error:", worst_b)
