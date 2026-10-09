import numpy as np, cvxpy as cp
from scipy.optimize import brentq, minimize_scalar
def wM(M, zeta, Phi):
    C = 1-M
    g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
    mu = brentq(g, 0, 1e18, xtol=1e-300, rtol=1e-15, maxiter=2000)
    return np.clip(mu*zeta/Phi**2, -M, M), mu
rng = np.random.default_rng(1); worst_gap = 0; worst_h = 0
for trial in range(30):
    K = 14; Phi = 2.0**(-1-np.arange(K))*rng.uniform(0.5,1,K)
    zeta = rng.normal(size=K)*Phi
    idx = rng.choice(6, 3, replace=False); zeta[idx] *= 0.05   # moderate off-peaks at coarse coordinates
    Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-9)
    Ms = np.linspace(Mmin, 1-1e-6, 3000); ob = [wM(M,zeta,Phi)[0]@zeta for M in Ms]; i = int(np.argmax(ob))
    r = minimize_scalar(lambda M: -(wM(M,zeta,Phi)[0]@zeta), bounds=(Ms[max(i-1,0)], Ms[min(i+1,len(Ms)-1)]), method='bounded', options={'xatol':1e-15})
    w, mu = wM(r.x, zeta, Phi); C = 1-r.x; nz = w@zeta
    x = cp.Variable(K); b = cp.Variable(K)
    pr = cp.Problem(cp.Minimize(cp.maximum(cp.norm(x,1), cp.norm(b,2))), [x + cp.multiply(Phi,b) == zeta]); pr.solve(solver=cp.CLARABEL)
    worst_gap = max(worst_gap, abs(nz - pr.value)/pr.value); off = np.abs(w) < r.x - 1e-9
    if np.sum((Phi*w)[off]**2) > 0.05*C**2: worst_h = max(worst_h, abs(mu*nz - C)/C)
print("relative gap <w,zeta> vs primal |zeta|:", worst_gap, " |mu |zeta| - C|/C (clamp consistency):", worst_h)
