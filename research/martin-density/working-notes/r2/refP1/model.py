# Finite model of the P1 example (one block, m = 1), with exact p* via SOCP (cvxpy/Clarabel).
# X = R^n (sup norm base), U = diag(sig) : H = R^n -> X, q*(A) = ||A||_1 + ||sig*A||_2.
# Block: K coordinates, vectors u_k in S_{q*}, Phi_k, lambda_k = Phi_k (m = 1), N(W) = ||W||_inf + ||Phi*W||_2.
# Coordinates: 0 = base coordinate "1" (supp a); 1..nK = contact set K' (z = +1); nK+1..n-1 = free J (z = 0).
import numpy as np, cvxpy as cp

def qstar(A, sig): return np.abs(A).sum() + np.linalg.norm(sig*A)

def build(seed=0, nK=10, nJ=14, K=7, spread=1.0):
    rng = np.random.default_rng(seed)
    n = 1 + nK + nJ
    sig = np.concatenate([[rng.uniform(0.5, 1.5)], rng.uniform(0.05, 0.4, n-1)])
    nu1 = sig[0]; alpha = 1/(1+nu1)
    a = np.zeros(n); a[0] = alpha
    e = np.zeros(n); e[0] = 1.0                    # U*a/||U*a|| for diagonal U
    z = np.zeros(n); z[0] = 1; z[1:1+nK] = 1
    zhat = z + sig*e
    # special block vector u (block coordinate index 1 = "k=2"): supp {0} cup K', u(zhat)=0
    h = rng.uniform(0.2, 1.0, nK) * 0.6**np.arange(nK)
    kap = (h.sum() + 0.0)/(1+nu1)                  # <U*h, e> = 0 for diagonal U (h off coordinate 0)
    u0 = np.zeros(n); u0[0] = -kap; u0[1:1+nK] = h
    u = u0/qstar(u0, sig)
    assert abs(u @ zhat) < 1e-13
    # other block vectors: random, with |u_k(zhat)| large (robust peaks)
    Us = []
    for k in range(K):
        if k == 1: Us.append(u); continue
        while True:
            v = rng.normal(size=n) * spread
            v = v/qstar(v, sig)
            if abs(v @ zhat) > 0.3: break
        Us.append(v)
    Us = np.array(Us)                               # K x n
    Phi = 2.0**(-2-np.arange(K)) * rng.uniform(0.5, 1.0, K)
    lam = Phi.copy()                                # m = 1
    return dict(n=n, nK=nK, nJ=nJ, K=K, sig=sig, a=a, e=e, z=z, zhat=zhat, u=u, Us=Us, Phi=Phi, lam=lam, alpha=alpha)

def Rmap(M, x): return M['lam'] * (M['Us'] @ x)

def block_J(M, zeta):
    # norming functional of zeta in (R^K, |.|) with dual norm N(w) = ||w||_inf + ||Phi w||_2
    K = M['K']; w = cp.Variable(K)
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(M['Phi'], w), 2) <= 1])
    prob.solve(solver=cp.CLARABEL)
    return np.array(w.value), prob.value

def first_row(M, x):
    # f = grad p(x) for x = z' + U e' with a'(x) = 1 = q(x): f = a' + R* J(R x); returns (f, w, |Rx|)
    zeta = Rmap(M, x)
    w, nrm = block_J(M, zeta)
    f = M['a'] + (M['lam'] * w) @ M['Us']
    return f, w, nrm

def pstar(M, h):
    n, K = M['n'], M['K']
    A = cp.Variable(n); W = cp.Variable(K); s = cp.Variable()
    cons = [A + (cp.multiply(M['lam'], W)) @ M['Us'] == h,
            cp.norm(A, 1) + cp.norm(cp.multiply(M['sig'], A), 2) <= s,
            cp.norm(W, 'inf') + cp.norm(cp.multiply(M['Phi'], W), 2) <= s]
    prob = cp.Problem(cp.Minimize(s), cons)
    for kw in [dict(solver=cp.CLARABEL), dict(solver=cp.CLARABEL, tol_gap_abs=1e-9, tol_gap_rel=1e-9, max_iter=500),
               dict(solver=cp.SCS, eps=1e-10, max_iters=200000)]:
        try:
            prob.solve(**kw)
            if prob.value is not None and np.isfinite(prob.value): return prob.value
        except Exception:
            pass
    return np.nan
