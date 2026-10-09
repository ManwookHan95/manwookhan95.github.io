"""Finite toy model of (c_0,p) with one block, private signatures, a contact and a near-contact.
Base: q*(A) = ||A||_1 + ||U^T A||_2 on R^n.  Block: N(W) = ||W||_inf + ||Phi*W||_2 on R^K.
p*(phi) = min max(q*(A), N(W)) s.t. A + sum_k lam_k W_k u_k = phi.
"""
import numpy as np, cvxpy as cp

def make_model(seed=0, delta=0.05, Unorm=0.3, resonant=True):
    rng = np.random.default_rng(seed)
    n = 10
    U = rng.standard_normal((n, n)); U *= Unorm/np.linalg.norm(U, 2)
    a = np.zeros(n); a[0], a[1] = 0.6, -0.3
    nu = np.linalg.norm(U.T @ a); a = a/(np.abs(a).sum() + nu)
    z = np.array([1.0, -1.0, 1.0, 0.97, 0.2, -0.1, 0.3, -0.4, 0.1, 0.0])  # 2 = contact, 3 = near-contact
    K = 6
    sig = [4+k for k in range(K)]          # private signature coordinate of carrier k
    Y = np.zeros((K, n))
    # targets: coarse-to-fine allowed (target of carrier k may touch signatures of COARSER carriers k' < k only)
    Y[0, 2] = 1.0 if resonant else 0.0; Y[0, 0] = 0.0 if resonant else 1.0   # carrier 0 ~ contact e_2*
    Y[1, 3] = 1.0                       # carrier 1 ~ near-contact e_3*
    Y[2, 2] = 0.7; Y[2, 4] = -0.5       # touches signature of carrier 0 (coarser) -> allowed
    Y[3, 0] = 0.5; Y[3, 5] = 0.6        # touches signature of carrier 1
    Y[4, 1] = -0.8; Y[4, 6] = 0.3
    Y[5, 2] = 0.4; Y[5, 3] = 0.5; Y[5, 7] = 0.3
    u = np.zeros((K, n))
    for k in range(K):
        v = Y[k].copy(); v[sig[k]] += delta
        u[k] = v/(np.abs(v).sum() + np.linalg.norm(U.T @ v))     # q*(u_k) = 1
    Phi = 0.3**(np.arange(K)+1)
    lam = Phi.copy()            # m = 1
    return dict(n=n, U=U, a=a, z=z, K=K, sig=sig, u=u, Phi=Phi, lam=lam, delta=delta)

def qstar(M, A):
    return np.abs(A).sum() + np.linalg.norm(M['U'].T @ A)

def Nblk(M, W):
    return np.abs(W).max() + np.linalg.norm(M['Phi']*W)

def blocknorm_and_normer(M, zeta):
    """|zeta|_Phi = max <W,zeta> s.t. N(W) <= 1 ; returns value and the (unique) maximizer w."""
    W = cp.Variable(M['K'])
    cons = [cp.norm(W, 'inf') + cp.norm(cp.multiply(M['Phi'], W), 2) <= 1]
    pr = cp.Problem(cp.Maximize(zeta @ W), cons); pr.solve(solver='CLARABEL')
    return pr.value, W.value

def pstar(M, phi, ret=False):
    n, K = M['n'], M['K']
    A = cp.Variable(n); W = cp.Variable(K); s = cp.Variable()
    L = (M['lam'][:, None]*M['u']).T          # n x K, A + L W = phi
    cons = [A + L @ W == phi,
            cp.norm(A, 1) + cp.norm(M['U'].T @ A, 2) <= s,
            cp.norm(W, 'inf') + cp.norm(cp.multiply(M['Phi'], W), 2) <= s]
    pr = cp.Problem(cp.Minimize(s), cons); pr.solve(solver='CLARABEL', tol_gap_abs=1e-10, tol_gap_rel=1e-10, tol_feas=1e-10)
    if ret: return pr.value, A.value, W.value
    return pr.value

def build_f(M):
    U, a, z = M['U'], M['a'], M['z']
    nu = np.linalg.norm(U.T @ a); e = U.T @ a/nu
    zhat = z + U @ e
    Rz = M['lam']*(M['u'] @ zhat)
    s_hat, w = blocknorm_and_normer(M, Rz)
    q0 = 1.0/(1.0 + s_hat)
    xi = q0*zhat
    f = a + (M['lam'][:, None]*M['u']).T @ w
    M.update(nu=nu, e=e, zhat=zhat, q0=q0, xi=xi, w=w, f=f, sigma=1-q0, zeta=M['lam']*(M['u'] @ xi))
    Mx = np.abs(w).max(); C = np.linalg.norm(M['Phi']*w)
    M.update(Mw=Mx, C=C)
    return M

if __name__ == '__main__':
    M = build_f(make_model())
    print('q0', M['q0'], 'sigma', M['sigma'], 'M', M['Mw'], 'C', M['C'], 'M+C', M['Mw']+M['C'])
    print('w', np.round(M['w'], 6))
    print('p*(f) =', pstar(M, M['f']), ' f(xi) =', M['f'] @ M['xi'])
