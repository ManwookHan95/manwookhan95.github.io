import numpy as np, warnings, cvxpy as cp
warnings.filterwarnings('ignore')
from refmodel import MRow, qstar
rng = np.random.default_rng(1)
# replicate instance generator
def rand_instance():
    n = 16
    mu = 0.3 * 0.7 ** np.arange(n)
    a = np.zeros(n)
    F = rng.choice(n, size=rng.integers(3, 7), replace=False)
    for j in F:
        a[j] = rng.choice([-1, 1]) * (10 ** rng.uniform(-3.5, -0.3))
    z = np.zeros(n); z[F] = np.sign(a[F])
    for j in [j for j in range(n) if j not in F]:
        z[j] = rng.choice([-1, 1]) if rng.random() < 0.6 else rng.uniform(-0.9, 0.9)
    Us, Phis = [], []
    for m in range(2):
        K = 5; U = np.zeros((K, n))
        for k in range(K):
            supp = rng.choice(n, size=rng.integers(3, 7), replace=False)
            U[k, supp] = rng.normal(size=len(supp)); U[k] /= qstar(U[k], mu)
        Us.append(U); Phis.append(rng.uniform(0.05, 0.5, size=K))
    return MRow(a, z, Us, Phis, mu)
worstv = 0
for inst in range(40):
    row = rand_instance()
    for m in range(row.B):
        x = row.xs[m]; Phi = row.Phis[m]
        # high-accuracy w via exact KKT: w = argmax <w,x> s.t. ||w||_inf + ||Phi w||_2 <= 1; re-solve with SCS high accuracy
        w = row.ws[m]; M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
        P = np.where(np.abs(w) >= M - 1e-6)[0]
        alpha = row.zetas[m]/row.sigmas[m] - Phi**2*w/C
        offP = np.setdiff1d(np.arange(len(w)), P)
        v = np.abs(alpha[offP]).max() if len(offP) else 0
        if v > 1e-4:
            print(inst, m, 'C=%.3e M=%.4f' % (C, M), 'v=%.2e' % v, 'w=', np.round(w, 7), 'x=', np.round(x, 5))
            # check: near-peak off-P coordinates?
            print('   |w|-M off P:', np.round(np.abs(w[offP]) - M, 8))
