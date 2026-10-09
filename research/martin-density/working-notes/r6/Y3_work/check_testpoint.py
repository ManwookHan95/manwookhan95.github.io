# Check Theorem 2.1 Step 1': test point eta_t = xi + t(Uk+chi_c) + t^2 U k_2, k_2 = -(|k|^2/(2q0)) e
# Base excess E_q = q**(eta_t) - a(eta_t) <= t^2 nu |k|^2/(2 q0) + O(t^4).
# q**(eta) = inf_h max(||eta - U h||_inf, ||h||)  (gauge of B_inf + U B_H), computed with cvxpy.
import numpy as np, cvxpy as cp
rng = np.random.default_rng(1)
n, d = 40, 6
U = rng.normal(size=(n, d)) / np.sqrt(n) * 1.5
for trial in range(5):
    # a with support F (size 25 of 40, "large F"), random signs, decaying
    F = rng.choice(n, 25, replace=False)
    a = np.zeros(n); a[F] = rng.choice([-1, 1], len(F)) * np.exp(-0.15*np.arange(len(F)))
    def qstar(x): return np.abs(x).sum() + np.linalg.norm(U.T @ x)
    a = a / qstar(a)
    nu = np.linalg.norm(U.T @ a); e = U.T @ a / nu
    z = np.zeros(n); z[F] = np.sign(a[F])
    Kset = [j for j in range(n) if j not in F][:5]   # contacts
    for j in Kset: z[j] = rng.choice([-1, 1])
    Jset = [j for j in range(n) if j not in F and j not in Kset]
    for j in Jset: z[j] = rng.uniform(-0.8, 0.8)
    q0 = 0.6  # any value in (0,1); xi = q0*(z + U e)
    xi = q0 * (z + U @ e)
    k = rng.normal(size=d); k -= (k @ e) * e   # k perp e
    chi_c = np.zeros(n)
    for j in Kset[:2]: chi_c[j] = -z[j] * rng.uniform(0.1, 1)   # inward contacts
    for j in Jset[:2]: chi_c[j] = rng.normal()
    kap = (k @ k) / (2*q0); k2 = -kap * e
    def qss(eta):
        h = cp.Variable(d)
        prob = cp.Problem(cp.Minimize(cp.maximum(cp.norm(eta - U @ h, 'inf'), cp.norm(h, 2))))
        prob.solve(solver=cp.CLARABEL)
        return prob.value
    print("trial", trial, " q**(xi)/q0 =", qss(xi)/q0, " a(xi)/q0 =", a@xi/q0)
    for t in [0.2, 0.1, 0.05, 0.025]:
        eta = xi + t*(U @ k + chi_c) + t**2 * (U @ k2)
        Eq = qss(eta) - a @ eta
        bound = t**2 * nu * (k@k) / (2*q0)
        print(f"   t={t:6.3f}  E_q={Eq:.3e}  bound={bound:.3e}  (E_q-bound)/t^4={(Eq-bound)/t**4:+.3e}")
