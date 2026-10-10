"""Check of U1 Lemma 2.1: for x supported in Omega ⊂ Q (strict non-peaks),
   d(x)^2 <= H(x) * C * chi/(1 - chi),  chi := ||D w 1_Omega||^2 / C^2,  1 - chi >= M^2 Phi_P^2 / C^2,
where d(x) = <Dw, Dx>/C and H(x) = ||P^perp D x||^2 / C (P^perp: orthogonal projection onto (Dw)^perp).
Random single blocks, w the norming functional (clamp formula, solved by bisection as in kappa_check.py)."""
import numpy as np
from kappa_lib import norming  # reuse the solver
rng = np.random.default_rng(5)
worst = 0.0; min_ratio = float('inf'); n = 0
for trial in range(300):
    K = rng.integers(5, 12); m = rng.integers(1, 3)
    Phi = 2.0 ** (-(m + np.arange(1, K + 1))) * rng.uniform(0.3, 1.0, K)
    zeta = m * Phi * rng.normal(size=K) * rng.choice([1.0, 1e-2, 1e-3], size=K)
    A, w, M, C = norming(zeta, Phi)
    theta = A * M / C
    nu = np.abs(zeta) / Phi ** 2
    P = nu >= theta * (1 - 1e-12); Q = ~P
    if Q.sum() == 0 or P.sum() == 0:
        continue
    Omega = Q & (rng.random(K) < 0.7)
    if Omega.sum() == 0:
        continue
    Dw = Phi * w
    chi = np.sum((Dw * Omega) ** 2) / C ** 2
    lower = M ** 2 * np.sum(Phi[P] ** 2) / C ** 2
    for rep in range(20):
        x = np.zeros(K); x[Omega] = rng.normal(size=Omega.sum())
        Dx = Phi * x
        d = np.dot(Dw, Dx) / C
        perp = Dx - np.dot(Dw, Dx) / np.dot(Dw, Dw) * Dw
        H = np.dot(perp, perp) / C
        bound = H * C * chi / (1 - chi)
        n += 1
        worst = max(worst, d ** 2 / bound)
        min_ratio = min(min_ratio, (1 - chi) / max(lower, 1e-300))
    # the extremal direction x = w 1_Omega attains equality
    x = w * Omega; Dx = Phi * x
    d = np.dot(Dw, Dx) / C
    perp = Dx - np.dot(Dw, Dx) / np.dot(Dw, Dw) * Dw
    H = np.dot(perp, perp) / C
    eq = d ** 2 / (H * C * chi / (1 - chi))
print('tests', n, 'max d^2/bound', worst, '(must be <= 1)')
print('min over tests of (1-chi)/(M^2 Phi_P^2/C^2) (must be >= 1):', min_ratio)
print('equality case ratio (last block):', eq)
