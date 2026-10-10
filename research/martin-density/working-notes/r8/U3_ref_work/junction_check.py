"""U3-ref F6a: first-order mismatch kappa = (d' - d)(Dom) created by the window masses of the engineered approximant.
Finite N = 1 model (nl_check + vt_check.extend).  Window data of 'scale t': b^theta and Dom scaled by 1/t (shape of the vt_check datum).
Masses m_j = 4 rho s_1 |b^theta_j| on contacts.  Prediction: kappa(t, s_1) = rho (d' - d)(Dom)/2 is linear in s_1 and scales like 1/t^2;
with d-consistent tuning (normalized value of the switching carrier restored) it vanishes.
"""
import numpy as np, cvxpy as cp, importlib.util, os
here = os.path.dirname(os.path.abspath(__file__))
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
nl = load('nl', os.path.join(here, 'nl_check.py')); vt = load('vt', os.path.join(here, 'vt_check.py'))

def block_data(lam, Phi, U, xh):
    zeta = lam*(U @ xh)
    w = cp.Variable(len(lam))
    pr = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    pr.solve(solver='CLARABEL', tol_gap_abs=1e-13, tol_gap_rel=1e-13, tol_feas=1e-13)
    return zeta, pr.value

M0 = nl.build(flip=False); F0 = vt.extend(M0)
n = F0['n']; lam, U, Phi, s, a, z = F0['lam'], F0['U'], F0['Phi'], F0['s'], F0['a'], F0['z']
w = F0['w']; psi = (lam*w) @ U; km = 2
V = U[km] - (F0['val'][km]/F0['normz'])*psi
chi = np.zeros(n); chi[[3, 5, 7, 8, 9, 10, 11, 12]] = 1.0
v0 = lam[km]*V                       # unit switching datum (Dom = e_km)
bth0 = (chi - 0.5)*v0; bth0[:2] = 0
zeta0, nz0 = block_data(lam, Phi, U, F0['zhat'])
d_at = lambda zeta, nz, om: om @ zeta / nz   # d(omega) = omega(R zhat)/|R zhat| for omega off the peaks (k_m is a strict non-peak)
rho = 0.9
print(' t      s_1      kappa=rho(d\'-d)(Dom)/2    kappa*t^2/s_1')
for t in (1.0, 0.3, 0.1, 0.03):
    for s1 in (1e-4, 1e-5):
        bth = bth0/t; Dom = np.zeros(4); Dom[km] = 1.0/t
        m = 4*rho*s1*np.abs(bth); m[:2] = 0
        a2 = a + m*z; a2[:2] = a[:2]
        a1 = a2/(np.abs(a2).sum() + np.linalg.norm(s*a2)); e1 = s*a1/np.linalg.norm(s*a1)
        xh = z + s*e1
        zeta1, nz1 = block_data(lam, Phi, U, xh)
        kap = rho*(d_at(zeta1, nz1, Dom) - d_at(zeta0, nz0, Dom))/2
        print('%5.2f  %.0e   %+.4e              %+.4e' % (t, s1, kap, kap*t*t/s1))
