"""Is the unweighted term sum_k min(lambda_k,|dU_k|) in Lemma 3.1 necessary?  Make a fine coordinate k a strict non-peak
(|U_k| small) and perturb it by dU_k = 0.1*lambda_k (so |dU_k| << lambda_k is unweighted-small but not weighted-negligible)."""
import numpy as np
src = open("check_cost.py").read().split("m = 1\n")[0]
ns = {}; exec(src, ns)
norming = ns["norming"]
rng = np.random.default_rng(3)
n = 30; m = 1
rw, ru = [], []
for trial in range(40):
    Phi = 0.5 ** (np.arange(n) + 2) * rng.uniform(0.5, 1.0, n)
    lam = m * Phi
    U = rng.normal(size=n)
    k = int(rng.integers(15, n))
    U[k] = 0.05 * Phi[k]            # deep below threshold: strict non-peak
    w, M, C, s = norming(lam * U, Phi)
    assert abs(w[k]) < M
    dU = np.zeros(n); dU[k] = 0.1 * lam[k] * np.sign(U[k])
    w2, M2, C2, s2 = norming(lam * (U + dU), Phi)
    L = np.sum(lam * np.abs(w2 - w))
    Delta = lam[k] * abs(dU[k])
    rw.append(L / (Delta * np.log(np.e / Delta)))
    ru.append(L / (Delta * np.log(np.e / Delta) + min(lam[k], abs(dU[k]))))
print("L / (weighted term only): max %.3e  median %.3e" % (max(rw), np.median(rw)))
print("L / (weighted + unweighted): max %.3e" % max(ru))
