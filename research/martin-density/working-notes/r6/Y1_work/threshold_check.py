# Sanity check of Lemma T (threshold equation) and Lemma T2 / derivative formulas.
import numpy as np, cvxpy as cp
rng = np.random.default_rng(7)

def block_norm(zeta, Phi):
    n = len(zeta); x = cp.Variable(n); y = cp.Variable(n)
    prob = cp.Problem(cp.Minimize(cp.maximum(cp.norm1(x), cp.norm2(y))), [x + cp.multiply(Phi, y) == zeta])
    prob.solve(solver=cp.CLARABEL, tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12)
    return prob.value

def theta_eq(zeta, Phi):
    a = np.abs(zeta)
    def Psi(x):
        A = np.sum(np.maximum(a - x*Phi**2, 0)); B = np.sum(np.minimum(x*Phi, a/Phi)**2)
        return A*A - B
    lo, hi = 1e-14, 1.0
    while Psi(hi) > 0: hi *= 2
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    th = 0.5*(lo+hi); A = np.sum(np.maximum(a - th*Phi**2, 0))
    return th, A

errs = []; mono = []; der = []
for trial in range(200):
    n = 12
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.3, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.5, 2.5, n)
    th, A = theta_eq(zeta, Phi)
    nb = block_norm(zeta, Phi)
    errs.append(abs(A - nb)/nb)
    nu = np.abs(zeta)/Phi**2
    P = nu >= th
    M = th/(th + A); C = A/(th + A)
    # derivative check: push a non-degenerate peak outward
    pk = [k for k in range(n) if nu[k] > th*1.01]
    npk = [k for k in range(n) if 0 < nu[k] < th*0.99]
    s = 1e-7*A
    if pk:
        k = pk[0]; z2 = zeta.copy(); z2[k] += np.sign(zeta[k])*s
        th2, A2 = theta_eq(z2, Phi)
        pred = C**2/(M*A*np.sum(Phi[P]**2))
        der.append(((np.log(th2) - np.log(th))/s)/pred)
        mono.append(th2 > th)
    if npk:
        k = npk[0]; z2 = zeta.copy(); sk = 1e-6*th*Phi[k]**2*min(1.0, (th-nu[k])/th)
        z2[k] += np.sign(zeta[k])*sk
        th2, A2 = theta_eq(z2, Phi)
        mono.append(th2 < th)
        # inward push of the strict non-peak raises the threshold (Y2 Lemma T(d)(ii))
        z3 = zeta.copy(); z3[k] -= np.sign(zeta[k])*min(sk, 0.5*abs(zeta[k]))
        th3, A3 = theta_eq(z3, Phi)
        mono.append(th3 > th)   # pushing a strict non-peak outward lowers the threshold
print("max rel err |zeta| (threshold eq vs SOCP):", max(errs))
print("monotonicity directions all correct:", all(mono), len(mono))
print("derivative ratio (numeric/predicted) min,max:", min(der), max(der))
