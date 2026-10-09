import numpy as np, cvxpy as cp
from scipy.optimize import brentq, minimize_scalar

def N(w, Phi):
    return np.max(np.abs(w)) + np.linalg.norm(Phi*w)

def J_clip(zeta, Phi, tol=1e-13):
    """norming functional of zeta for the block norm with dual N(w)=||w||_inf+||Phi w||_2, via
    w = clip(mu zeta/Phi^2, -M, M), ||Phi w|| = 1-M, maximize <w,zeta> over M."""
    def wM(M):
        C = 1-M
        g = lambda mu: np.linalg.norm(Phi*np.clip(mu*zeta/Phi**2, -M, M)) - C
        hi = 1.0
        while g(hi) < 0:
            hi *= 2
            if hi > 1e300: return np.clip(hi*zeta/Phi**2, -M, M)
        mu = brentq(g, 0, hi, xtol=1e-300, rtol=1e-15, maxiter=3000)
        return np.clip(mu*zeta/Phi**2, -M, M)
    Mmin = 1/(1+np.linalg.norm(Phi))*(1+1e-12)
    Ms = np.linspace(Mmin, 1-1e-9, 400)
    ob = np.array([wM(M)@zeta for M in Ms]); i = int(np.argmax(ob))
    r = minimize_scalar(lambda M: -(wM(M)@zeta), bounds=(Ms[max(i-1,0)], Ms[min(i+1,len(Ms)-1)]),
                        method='bounded', options={'xatol':1e-15})
    return wM(r.x)

def J_cvx(zeta, Phi):
    n = len(zeta); w = cp.Variable(n)
    pr = cp.Problem(cp.Maximize(zeta@w), [cp.norm(w,'inf') + cp.norm(cp.multiply(Phi,w),2) <= 1])
    pr.solve(solver=cp.CLARABEL)
    return w.value

def primal(zeta, Phi):
    n=len(zeta); x=cp.Variable(n); b=cp.Variable(n)
    pr=cp.Problem(cp.Minimize(cp.maximum(cp.norm(x,1), cp.norm(b,2))), [x+cp.multiply(Phi,b)==zeta]); pr.solve(solver=cp.CLARABEL)
    return pr.value
