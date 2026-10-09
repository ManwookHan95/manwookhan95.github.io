"""N1: channel signs (Prop 2.8) and raising derivative (Lemma 2.6), finite models.
Base q*(A) = ||A||_1 + ||U^T A||_2.  e = U^T a/||U^T a||, zhat = z + U e.
z-signed W: supported in F u K, z_j W(j) >= 0 on K.  h_W = U P U^T W, P = I - e e^T.
First-order effect of unit mass at contact j: z_j h_W(j)/nu.
"""
import numpy as np
rng = np.random.default_rng(7)
n = 40
F = [0, 1]
def make_U(kind, kappa=0.6):
    s = 0.8 * 2.0 ** (-0.15 * np.arange(n))
    if kind == 'diag':
        return np.diag(s)
    if kind == 'mix':   # U^T e_j = s_j (k_j + (-1)^j kappa g)
        U = np.zeros((n, n + 1)); U[:, :n] = np.diag(s)
        U[:, n] = s * kappa * (-1.0) ** np.arange(n)
        return U
    if kind == 'rand':
        return rng.normal(size=(n, 6)) * s[:, None] * 0.5
res = {}
for kind in ['diag', 'mix', 'rand']:
    U = make_U(kind)
    worst_min, frac_neg, deriv_err = [], [], []
    for trial in range(300):
        a = np.zeros(n); a[F] = rng.normal(size=len(F)); a /= (np.abs(a).sum() + np.linalg.norm(U.T @ a))
        z = np.ones(n); z[F] = np.sign(a[F])
        # random contact pattern: K = coordinates with z = +-1 off F; maximal contact here, random signs
        z[2:] = rng.choice([-1.0, 1.0], size=n - 2)
        K = list(range(2, n))
        e = U.T @ a; nu = np.linalg.norm(e); e /= nu
        P = np.eye(U.shape[1]) - np.outer(e, e)
        # z-signed W: random support in F u K
        W = np.zeros(n); supp = rng.choice(K, size=8, replace=False)
        W[supp] = z[supp] * rng.random(8); W[F] = rng.normal(size=len(F))
        h = U @ (P @ (U.T @ W))
        zh = z[K] * h[K]
        worst_min.append(zh.min()); frac_neg.append(np.mean(zh < -1e-14))
        # raising derivative check: a + m W
        def Wzhat(m):
            A = a + m * W; ee = U.T @ A; ee /= np.linalg.norm(ee)
            return W @ (z + U @ ee)
        dm = 1e-6
        fd = (Wzhat(dm) - Wzhat(-dm)) / (2 * dm)
        pred = np.linalg.norm(P @ (U.T @ W)) ** 2 / nu
        deriv_err.append(abs(fd - pred) / pred)
    res[kind] = (min(worst_min), np.mean(frac_neg), max(deriv_err))
    print(f"{kind:5s}: min_j z_j h_W(j) over contacts = {min(worst_min):+.3e}; "
          f"mean fraction of lowering contacts = {np.mean(frac_neg):.3f}; max rel err raising derivative = {max(deriv_err):.2e}")
