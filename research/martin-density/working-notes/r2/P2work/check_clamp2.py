import numpy as np, cvxpy as cp
from scipy.optimize import brentq
def Jexact(zeta, Phi):
    # maximize <w,zeta> s.t. ||w||_inf + ||Phi w|| <= 1 : for fixed M, w = clip(mu zeta/Phi^2, -M, M) with ||Phi w|| = 1-M; optimize M (1-d)
    def inner(M):
        C = 1-M
        g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
        if g(1e15) < 0: return None
        mu = brentq(g, 0, 1e15, xtol=1e-300, rtol=1e-15, maxiter=1000)
        return np.clip(mu*zeta/Phi**2, -M, M)
    Ms = np.linspace(1e-6, 1-1e-6, 20001); best=None; bv=-1
    for M in Ms:
        w = inner(M)
        if w is not None and w@zeta > bv: bv, best, bM = w@zeta, w, M
    # refine
    lo, hi = max(bM-1e-4,1e-9), min(bM+1e-4,1-1e-9)
    from scipy.optimize import minimize_scalar
    r = minimize_scalar(lambda M: (1e9 if inner(M) is None else -(inner(M)@zeta)), bounds=(lo,hi), method='bounded', options={'xatol':1e-14})
    w = inner(r.x); return w, w@zeta
rng = np.random.default_rng(1); worst=0; worst_cv=0
for trial in range(40):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5,1,K)
    zeta = rng.normal(size=K)*Phi
    idx = rng.choice(K, 4, replace=False); zeta[idx] *= 1e-2*Phi[idx]
    w, nz = Jexact(zeta, Phi); M = np.abs(w).max(); C = np.linalg.norm(Phi*w)
    r = np.abs(zeta)/(Phi**2*nz); wc = np.sign(zeta)*np.minimum(M, C*r)
    worst = max(worst, np.abs(w-wc).max())
    v = cp.Variable(K); pr = cp.Problem(cp.Maximize(zeta@v), [cp.norm(v,'inf') + cp.norm(cp.multiply(Phi,v),2) <= 1]); pr.solve(solver=cp.CLARABEL)
    worst_cv = max(worst_cv, np.abs(v.value - w).max())
print("clamp vs exact 1-d solver:", worst, "  cvxpy vs exact:", worst_cv)
