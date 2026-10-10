"""Check of Q2 Proposition 4.1 (block-norm bordering): explicit right inverse of
   L(P, P0) = D P - g (h^T P) - sum_m p_m (q_m^T P) - pi p_{m*} P0,  D = I + X  (X: absorber rows <- Omega^0 columns),
in both cases (|beta_*| >= beta_0: alpha = 0;  |c_alpha| >= beta_0: gamma_{m*} = 0), including EXACT Sherman-Morrison degeneracy
(h^T D^{-1} g chosen so that X2's square system is singular), and of the bound ||P||_inf + |P0| <= K ||b||_inf."""
import numpy as np
rng = np.random.default_rng(5)

def build(nblk=3, per=4, nabs=3):
    n0 = nblk * per; n = n0 + nabs
    blocks = [np.arange(m * per, (m + 1) * per) for m in range(nblk)]
    X = np.zeros((n, n)); X[n0:, :n0] = rng.standard_normal((nabs, n0)) * 0.3
    D = np.eye(n) + X
    p = []; q = []
    for B in blocks:
        pm = np.zeros(n); qm = np.zeros(n)
        pm[B] = rng.standard_normal(per); qm[B] = rng.standard_normal(per)
        qm *= rng.uniform(-0.5, 0.5) / (qm @ pm)          # q_m^T p_m in [-1/2, 1/2]
        p.append(pm); q.append(qm)
    g = rng.standard_normal(n); h = rng.standard_normal(n)
    return n, blocks, X, D, p, q, g, h

def solve(n, D, p, q, g, h, ms, pi, b):
    Di = np.linalg.inv(D)
    M = len(p)
    beta = h @ Di @ p[ms]
    coef = {m: (h @ Di @ p[m]) / (1 - q[m] @ p[m]) for m in range(M) if m != ms}
    calpha = 1 - h @ Di @ g - sum(coef[m] * (q[m] @ Di @ g) for m in coef)
    rhs = h @ Di @ b + sum(coef[m] * (q[m] @ Di @ b) for m in coef)
    if abs(beta) >= abs(calpha):
        alpha, gms = 0.0, -rhs / beta
    else:
        alpha, gms = rhs / calpha, 0.0
    gam = {m: (q[m] @ Di @ b + (q[m] @ Di @ g) * alpha) / (1 - q[m] @ p[m]) for m in coef}
    gam[ms] = gms
    P = Di @ (b + g * alpha + sum(p[m] * gam[m] for m in range(M)))
    P0 = (gam[ms] - q[ms] @ P) / pi
    return P, P0, beta, calpha

worst_res, worst_ratio = 0.0, 0.0
for trial in range(3000):
    n, blocks, X, D, p, q, g, h = build()
    ms = rng.integers(0, 3); pi = rng.uniform(0.1, 2.0) * rng.choice([-1, 1])
    Di = np.linalg.inv(D)
    mode = trial % 3
    if mode == 0:      # exact SM-type degeneracy of X2's square system: force c_alpha = 0
        coef = [(h @ Di @ p[m]) / (1 - q[m] @ p[m]) for m in range(3) if m != ms]
        others = [m for m in range(3) if m != ms]
        target = 1 - sum(c * (q[m] @ Di @ g) for c, m in zip(coef, others))
        h *= target / (h @ Di @ g)  if abs(h @ Di @ g) > 1e-8 else 1.0
    if mode == 1:      # force beta_* = 0 (then c_alpha must carry it)
        v = Di @ p[ms]; h -= (h @ v) / (v @ v) * v
    b = rng.standard_normal(n)
    P, P0, beta, calpha = solve(n, D, p, q, g, h, ms, pi, b)
    L = D @ P - g * (h @ P) - sum(p[m] * (q[m] @ P) for m in range(3)) - pi * p[ms] * P0
    worst_res = max(worst_res, np.abs(L - b).max())
    beta0 = max(abs(beta), abs(calpha))
    KD = 1 + np.abs(X).sum(axis=1).max(); Q = sum(np.abs(qm).sum() for qm in q)
    pbar = max(np.abs(pm).max() for pm in p); H = np.abs(h).sum(); G = np.abs(g).max()
    K = 4 * (1 + 1 / abs(pi)) * KD**4 * (1 + pbar)**2 * (1 + Q)**3 * (1 + H) * (1 + G) * (1 + 1 / beta0)
    worst_ratio = max(worst_ratio, (np.abs(P).max() + abs(P0)) / (K * np.abs(b).max()))
print("max residual |L(P,P0) - b|_inf:", worst_res)
print("max (||P||+|P0|)/(K ||b||)  (must be <= 1):", worst_ratio)

# the square system of X2 (no bordering) at c_alpha = 0 with one block: singular; bordered: solvable with beta_* robust
n, blocks, X, D, p, q, g, h = build(nblk=1, per=5, nabs=2)
Di = np.linalg.inv(D); h *= 1.0 / (h @ Di @ g)
N = D - np.outer(g, h) - np.outer(p[0], q[0])
print("one block, 1 - h^T D^-1 g = %.1e: det of X2's square system = %.3e (formula (1-q^Tp)(1-h^TD^-1g)-(q^TD^-1g)(h^TD^-1p) = %.3e)"
      % (1 - h @ Di @ g, np.linalg.det(N) / np.linalg.det(D),
         (1 - q[0] @ p[0]) * (1 - h @ Di @ g) - (q[0] @ Di @ g) * (h @ Di @ p[0])))
