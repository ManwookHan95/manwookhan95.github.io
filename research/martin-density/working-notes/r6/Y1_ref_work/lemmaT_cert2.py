# Certify Lemma T's norming functional: w_pred(k) = sgn(zeta_k) (C/A) min(theta, nu_k) must satisfy
# N(w_pred) = ||w||_inf + ||Phi w||_2 = 1 and <w_pred, zeta> = |zeta| (primal norm from SOCP min max(||x||_1, ||y||_2), zeta = x + Phi y).
import numpy as np, cvxpy as cp, warnings
warnings.filterwarnings("ignore")
exec(open('lemmaT_indep.py').read().split("# ---- 1.")[0])
def primal(zeta, Phi):
    n = len(zeta); x = cp.Variable(n); y = cp.Variable(n)
    p = cp.Problem(cp.Minimize(cp.maximum(cp.norm1(x), cp.norm2(y))), [x + cp.multiply(Phi, y) == zeta])
    p.solve(solver=cp.CLARABEL, tol_gap_abs=1e-13, tol_gap_rel=1e-13, tol_feas=1e-13); return p.value
rng = np.random.default_rng(5)
eN = eV = eP = 0; badsolver = 0
for trial in range(150):
    n = int(rng.integers(6, 30))
    Phi = 2.0**(-np.arange(1, n+1)) * rng.uniform(0.2, 1.0, n)
    zeta = rng.normal(size=n) * Phi**rng.uniform(0.0, 3.0, n)
    th, A = theta_of(zeta, Phi); M = th/(th + A); C = A/(th + A); nu = np.abs(zeta)/Phi**2
    wp = np.sign(zeta)*(C/A)*np.minimum(th, nu)
    Nw = np.max(np.abs(wp)) + np.linalg.norm(Phi*wp)
    eN = max(eN, abs(Nw - 1)); eV = max(eV, abs(wp @ zeta - A)/A)
    pv = primal(zeta, Phi); eP = max(eP, abs(pv - A)/A)
    # the dual SOCP solution: does it also norm zeta? (non-uniqueness would contradict smoothness)
    val, w = norming(zeta, Phi)
    if abs(np.max(np.abs(w)) + np.linalg.norm(Phi*w) - 1) > 1e-6 or abs(w @ zeta - A)/A > 1e-6: badsolver += 1
print("max |N(w_pred) - 1| = %.2e, max rel |<w_pred,zeta> - A| = %.2e, max rel |primal - A| = %.2e" % (eN, eV, eP))
print("dual SOCP solutions failing feasibility/optimality at 1e-6:", badsolver)
