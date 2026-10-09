# Lemma 1.1 check: build w by the clamp formula self-consistently and verify it norms zeta (primal value via SOCP).
import numpy as np, cvxpy as cp
from scipy.optimize import brentq
def clamp_w(zeta, Phi):
    def wM(M):
        C = 1-M
        g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
        mu = brentq(g, 0, 1e18, xtol=1e-300, rtol=1e-15, maxiter=2000)
        return np.clip(mu*zeta/Phi**2, -M, M), mu
    def h(M):
        w, mu = wM(M); return mu*(w@zeta) - (1-M)
    # h changes sign on (0,1): find root
    Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-9)   # need M ||Phi|| >= 1 - M
    Ms = np.linspace(Mmin, 1-1e-6, 400); vals = [h(M) for M in Ms]
    i = next(i for i in range(len(Ms)-1) if vals[i]*vals[i+1] <= 0)
    M = brentq(h, Ms[i], Ms[i+1], xtol=1e-15)
    return wM(M)[0]
rng = np.random.default_rng(1); worst = 0
for trial in range(30):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5,1,K)
    zeta = rng.normal(size=K)*Phi
    idx = rng.choice(K, 4, replace=False); zeta[idx] *= 1e-2*Phi[idx]
    w = clamp_w(zeta, Phi)
    Nw = np.abs(w).max() + np.linalg.norm(Phi*w)
    x = cp.Variable(K); b = cp.Variable(K)
    pr = cp.Problem(cp.Minimize(cp.norm(x,1) + cp.norm(b,2)), [x + cp.multiply(Phi,b) == zeta]); pr.solve(solver=cp.CLARABEL, tol_gap_abs=1e-12, tol_gap_rel=1e-12)
    worst = max(worst, abs(Nw-1), abs(w@zeta - pr.value)/pr.value)
    offp = np.sum(np.abs(w) < np.abs(w).max()-1e-12)
print("max of |N(w)-1| and relative gap <w,zeta> vs |zeta|_m:", worst, "(off-peak count last trial:", offp, ")")
