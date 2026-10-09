import numpy as np, warnings; warnings.filterwarnings('ignore')
from thmB_check import *
import cvxpy as cp
D = setup('kinks')
Phi, w, C, m, Rmat, U = D['Phi'], D['w'], D['C'], D['m'], D['Rmat'], D['U']
M = D['M']; Q = D['Q']
print('M', M, 'C', C, 'gaps on Q', [M - abs(w[k]) for k in Q], 'Phi_Q', Phi[Q])
rng = np.random.default_rng(7)
om = np.zeros(len(Phi)); om[1] = 1.0 / (m * Phi[1]); dd = np.dot(Phi * w, Phi * om) / C
gs = [('cert', Rmat.T @ (om - dd * w))]
for i in range(3):
    g = rng.normal(size=len(D['x'])) * 0.3
    g = g - (g @ D['x']) * D['a'] / (D['a'] @ D['x'])
    gs.append((f'rand{i}', g))
def gamma_side_om(D, g, side):
    U, Phi, Rmat, a, z, w, C, Q, Jall = D['U'], D['Phi'], D['Rmat'], D['a'], D['z'], D['w'], D['C'], D['Q'], D['Jall']
    nu = np.linalg.norm(U.T @ a); ee = U.T @ a / nu; Pp = np.eye(len(ee)) - np.outer(ee, ee)
    omQ = cp.Variable(len(Q)); E = np.eye(len(Phi))[Q].T
    omv = E @ omQ
    d = (Phi * w) @ cp.multiply(Phi, omv) / C
    b = g - Rmat.T @ (omv - d * w)
    DQ = np.diag(Phi[Q]); wv = (Phi[Q]**2 * w[Q]) / C
    Hmat = (DQ @ DQ - np.outer(wv, wv)) / C; Hmat = (Hmat + Hmat.T) / 2
    obj = D['q0'] * cp.sum_squares(Pp @ (U.T @ b)) / nu + D['sig'] * cp.quad_form(omQ, cp.psd_wrap(Hmat))
    Kc = [j for j in Jall if abs(abs(z[j]) - 1) < 1e-12]
    cons = [cp.multiply(side * z[Kc], b[Kc]) >= 0]
    pr = cp.Problem(cp.Minimize(obj), cons); pr.solve(solver=cp.CLARABEL)
    return pr.value, omQ.value
for name, g in gs[:2]:
    for side in [+1, -1]:
        gv, omv = gamma_side_om(D, g, side)
        print(name, side, 'gamma', round(gv, 5), 'omega_Q', np.round(omv, 3), ' |t| radius ~ gap/|omega| =', [ (M-abs(w[k]))/max(abs(o),1e-12) for k, o in zip(Q, omv)])
        for t in [2e-3, 5e-4, 1e-4, 2.5e-5]:
            tt = side * t
            val = pstar_socp(D['f'] + tt * g, U, Rmat, Phi)
            print('    t=%.1e coeff=%.6f' % (tt, 2 * (val - 1) / t**2))
