# Independent check of Theorem B (finite analogue): exact one-sided coefficient of p* via SOCP (cvxpy/Clarabel)
# versus the QP value gamma^{+-} = min over side-admissible omega of q0 h(b) + sigma H(omega).
import numpy as np, sys, cvxpy as cp
base = '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/'
sys.path.insert(0, base + 'Cref_work'); sys.path.insert(0, base + 'C_work')
from model import build
from solvers import qstar, block_norm as bn_mine
from basenorm import q_norm

def pstar_socp(h, U, Rmat, Phi):
    K = Rmat.shape[0]
    W = cp.Variable(K); r = cp.Variable()
    A = h - Rmat.T @ W
    cons = [cp.norm1(A) + cp.norm(U.T @ A, 2) <= r, cp.norm_inf(W) + cp.norm(cp.multiply(Phi, W), 2) <= r]
    pr = cp.Problem(cp.Minimize(r), cons)
    pr.solve(solver=cp.CLARABEL, tol_gap_abs=1e-14, tol_gap_rel=1e-14, tol_feas=1e-14, max_iter=500)
    return pr.value

def setup(zmode):
    md = build()
    U, Phi0, Ub0, m, x0 = md['U'], md['Phi'], md['Ub'], md['m'], md['x']
    qv0, a, z0, e, F = q_norm(x0, U)
    Jall = [j for j in range(len(x0)) if j not in F]
    z = z0.copy()
    if zmode == 'kinks': z[Jall] = np.sign(z0[Jall])
    xt = z + U @ e
    Rm0 = (m * Phi0)[:, None] * Ub0
    val0, w0 = bn_mine(Rm0 @ xt, Phi0); M0 = np.max(np.abs(w0))
    P0 = [k for k in range(len(Phi0)) if abs(abs(w0[k]) - M0) < 1e-9]
    s0 = np.sign(w0)
    pi = sum(s0[k] * m * Phi0[k] * Ub0[k] for k in P0)
    tau = (pi @ xt) * a - pi
    Ub = np.vstack([Ub0, tau / qstar(tau, U)]); Phi = np.append(Phi0, 0.45 ** 10)
    Rmat = (m * Phi)[:, None] * Ub
    bv, w = bn_mine(Rmat @ xt, Phi)
    x = xt / (1.0 + bv); q0 = 1.0 / (1.0 + bv); sig = bv / (1.0 + bv)
    w = bn_mine(Rmat @ x, Phi)[1]; M = np.max(np.abs(w)); C = np.linalg.norm(Phi * w)
    f = a + Rmat.T @ w
    P = [k for k in range(len(Phi)) if abs(abs(w[k]) - M) < 1e-7]; Q = [k for k in range(len(Phi)) if k not in P]
    return dict(U=U, Phi=Phi, Rmat=Rmat, a=a, z=z, e=e, F=F, Jall=Jall, x=x, q0=q0, sig=sig, w=w, M=M, C=C, f=f, P=P, Q=Q, m=m)

def gamma_side(D, g, side):
    U, Phi, Rmat, a, z, w, C, Q, Jall = D['U'], D['Phi'], D['Rmat'], D['a'], D['z'], D['w'], D['C'], D['Q'], D['Jall']
    nu = np.linalg.norm(U.T @ a); ee = U.T @ a / nu; Pp = np.eye(len(ee)) - np.outer(ee, ee)
    omQ = cp.Variable(len(Q)); E = np.eye(len(Phi))[Q].T   # K x |Q|
    om = E @ omQ
    d = (Phi * w) @ cp.multiply(Phi, om) / C
    b = g - Rmat.T @ (om - d * w)
    DQ = np.diag(Phi[Q]); wv = (Phi[Q]**2 * w[Q]) / C
    Hmat = (DQ @ DQ - np.outer(wv, wv)) / C; Hmat = (Hmat + Hmat.T) / 2
    obj = D['q0'] * cp.sum_squares(Pp @ (U.T @ b)) / nu + D['sig'] * cp.quad_form(omQ, cp.psd_wrap(Hmat))
    Kc = [j for j in Jall if abs(abs(z[j]) - 1) < 1e-12]; Jf = [j for j in Jall if j not in Kc]
    cons = ([cp.multiply(side * z[Kc], b[Kc]) >= 0] if Kc else []) + ([b[Jf] == 0] if Jf else [])
    pr = cp.Problem(cp.Minimize(obj), cons); pr.solve(solver=cp.CLARABEL)
    return pr.value

if __name__ == '__main__':
    for zmode in ['free', 'kinks']:
        D = setup(zmode)
        print('model', zmode, 'Q', D['Q'], 'p*(f)=', pstar_socp(D['f'], D['U'], D['Rmat'], D['Phi']))
        rng = np.random.default_rng(7)
        # test directions: the C-referee certificate, plus random g with g(xi)=0
        Phi, w, C, m, Rmat = D['Phi'], D['w'], D['C'], D['m'], D['Rmat']
        om = np.zeros(len(Phi)); om[1] = 1.0 / (m * Phi[1]); dd = np.dot(Phi * w, Phi * om) / C
        gs = [('cert', Rmat.T @ (om - dd * w))]
        for i in range(3):
            g = rng.normal(size=len(D['x'])) * 0.3
            g = g - (g @ D['x']) * D['a'] / (D['a'] @ D['x'])   # g(xi) = 0
            gs.append((f'rand{i}', g))
        for name, g in gs:
            gp, gm = gamma_side(D, g, +1), gamma_side(D, g, -1)
            co = []
            for t in [2e-2, 1e-2, 5e-3, -2e-2, -1e-2, -5e-3]:
                co.append(2 * (pstar_socp(D['f'] + t * g, D['U'], Rmat, Phi) - 1) / t**2)
            # Richardson (coefficient ~ c0 + c1 t): 2*co(t/2) - co(t)
            rp = 2 * co[2] - co[1]; rm = 2 * co[5] - co[4]
            print(f"  {name}: gamma+={gp:.5f} exact(t=.02,.01,.005)={co[0]:.5f},{co[1]:.5f},{co[2]:.5f} Rich={rp:.5f} | gamma-={gm:.5f} exact={co[3]:.5f},{co[4]:.5f},{co[5]:.5f} Rich={rm:.5f}")
