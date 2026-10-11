import numpy as np, cvxpy as cp
import sqrt_mu_check as M

def theory_A(m, jf, z3=0.0):
    a, z, xhat, w, f, psi, zeta = M.build_row(m, z3=z3)
    sig_hat = zeta @ w                      # |zeta'|_Phi at xhat'
    p_xhat = 1 + sig_hat                    # p(xhat') = q(xhat') + |R xhat'|
    c = 1 / p_xhat                          # c' = q(x')
    sigma = c * sig_hat                     # sigma' = |R x'|
    C = np.linalg.norm(M.Phi * w)
    alpha = zeta / sig_hat - M.Phi**2 * w / C
    S = [1, 2]
    Lam = [k for k in range(M.nb) if (abs(M.u[k][S]).sum() + abs(M.u[k][jf])) > 0]
    alpha0 = min(abs(alpha[k]) for k in Lam)
    nu = lambda j: sum(M.lam[k] * abs(M.u[k][j]) for k in Lam)
    rhoS = (abs(psi[1]) + abs(psi[2])) / abs(psi[jf])
    rf = 1 - abs(z[jf])
    A = rhoS / (c * rf) + 1 / c + (rhoS * nu(jf) + nu(1) + nu(2)) / (sigma * alpha0)
    return A, Lam, alpha0, rhoS

for jf in [3, 5, 6]:
    A, Lam, a0, rhoS = theory_A(1e-4, jf)
    print(f"j_f={jf}: Lambda={Lam} alpha0={a0:.4f} rho_S={rhoS:.3f} A={A:.2f}  predicted Osc/sqrt(mu_S) <= 2 sqrt(2A) = {2*np.sqrt(2*A):.2f}")

# maximal aligned contact: every coordinate off F' is a contact (or bank) with z_j = sgn psi'_j
def build_maximal(m):
    z = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    for it in range(5):
        a = np.array([1.0, m, m, 0, 0, 0, 0]); a = a / M.qstar_np(a)
        e = M.mu * a / np.linalg.norm(M.mu * a); xhat = z + M.mu * e
        zeta = M.lam * (M.u @ xhat)
        w = cp.Variable(M.nb)
        cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(M.Phi, w), 2) <= 1]).solve(solver=cp.CLARABEL)
        w = w.value; psi = M.Rstar @ w
        znew = z.copy()
        for j in range(3, 7):
            if abs(psi[j]) > 1e-12: znew[j] = np.sign(psi[j])
        if np.all(znew == z): break
        z = znew
    f = a + M.Rstar @ w
    return f, psi, z

print()
print("maximal aligned contact (no free coordinate at all):")
for m in [0.0, 1e-5, 1e-3]:
    f, psi, z = build_maximal(m)
    val, st = M.max_lambda(f, psi)
    print(f" m={m:8.1e} z={z} maxLambda={val:10.3e} Osc={val/max(psi[1],psi[2]):10.3e} [{st}]")
