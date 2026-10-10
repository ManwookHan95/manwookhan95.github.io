"""U3-ref: independent finite-model check of Lemma VT (violation tolerance at a single stage of thm:engineered).
Model: nl_check.build (N = 1) extended by a dead-zone contact j0 = 13 (vt_check.extend).  Data: the coherent-shift mate g
of vt_check (two-piece data (b^+, 0), (b^-, Dalpha e_km)), then g_e := g - eps e_j0 + eps a  (side + violated at j0 by eps).
Engineered approximant (Definition def:engineered, finite model, N_w = N'' = n): masses m_j = 4 rho s_1 |b^theta_j| on all
contacts, a'' = a + sum m_j z_j e_j, f' = grad p(xhat'), g'' = b^theta + R^*(omega^theta - d'(omega^theta) w'), g' = rho(g'' - c a').
Prediction (Lemma VT): if s_1 >= 32 rho eps / delta, then p*(f' + tau g') <= 1 + (tau^2/2)(1 - delta) for small |tau|;
if s_1 << eps, the linear flip cost at j0 makes p*(f' + tau g') - 1 - (tau^2/2)(1 - delta) > 0 for tau in (~s_1, ~4 rho eps/delta).
"""
import numpy as np, cvxpy as cp, importlib.util, sys
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
import os
here = os.path.dirname(os.path.abspath(__file__))
nl = load('nl', os.path.join(here, 'nl_check.py'))
vt = load('vt', os.path.join(here, 'vt_check.py'))

def norming(lam, Phi, U, xhat):
    zeta = lam*(U @ xhat)
    w = cp.Variable(len(lam))
    pr = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    pr.solve(solver='CLARABEL', tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12)
    return w.value, pr.value

def gamma_w(M, b, om, w, C, q0, sigma, nu, e):
    Ub = M['s']*b; Pp = Ub - (e @ Ub)*e
    Dw = M['Phi']*w; dom = (M['Phi']**2*w) @ om / C
    Hom = np.sum((M['Phi']*om - dom*Dw/C)**2)/C
    return q0*np.sum(Pp**2)/nu + sigma*Hom

if __name__ == '__main__':
    M0 = nl.build(flip=False)
    F0 = vt.extend(M0)
    n = F0['n']; lam, U, w, Phi, s = F0['lam'], F0['U'], F0['w'], F0['Phi'], F0['s']
    a, z, zhat = F0['a'], F0['z'], F0['zhat']
    psi = (lam*w) @ U
    km = 2
    V = U[km] - (F0['val'][km]/F0['normz'])*psi
    chi = np.zeros(n); chi[[3, 5, 7, 8, 9, 10, 11, 12]] = 1.0
    c = 0.25; Dal = 30.0
    v = c*Dal*lam[km]*V
    bp = chi*v; bp[:2] = 0; bp = bp - (bp @ zhat)*a
    bm = bp - v
    omp = np.zeros(4); omm = np.zeros(4); omm[km] = c*Dal
    Mx = np.max(np.abs(w)); C = np.linalg.norm(Phi*w); q0 = 1/(1 + F0['normz']); sigma = q0*F0['normz']
    nu = np.linalg.norm(s*a); e = s*a/nu
    # check representation identity: b^+ + R^*(om^+ - d^+ w) == b^- + R^*(om^- - d^- w)
    d = lambda om: (Phi**2*w) @ om / C
    gp = bp + (lam*(omp - d(omp)*w)) @ U; gm = bm + (lam*(omm - d(omm)*w)) @ U
    print('representation residual:', np.abs(gp - gm).max(), '  g(zhat) =', gp @ zhat)
    rho = 0.9
    for eps in (2e-3, 5e-4):
        bpe = bp.copy(); bme = bm.copy()
        bpe[13] -= eps; bme[13] -= eps
        bpe += eps*a; bme += eps*a          # keep b(zhat) = 0 (a(zhat) = 1, zhat_13 = 1)
        kap = max(gamma_w(F0, bpe, omp, w, C, q0, sigma, nu, e), gamma_w(F0, bme, omm, w, C, q0, sigma, nu, e))
        delta = (1 - rho**2*kap)/2
        viol = (z[13]*bpe[13] < 0)*abs(bpe[13]) + (z[13]*bme[13] > 0)*abs(bme[13])
        print('\neps = %.1e : kappa_w = %.4f, delta = %.4f, viol(j0) = %.2e, (VT) threshold 32 rho eps/delta = %.2e'
              % (eps, kap, delta, viol, 32*rho*eps/delta))
        bth = (bpe + bme)/2; omth = (omp + omm)/2
        for s1 in (32*rho*eps/delta, 4*rho*eps/delta, eps/20):
            m = np.zeros(n); offF = np.arange(2, n)
            m[offF] = 4*rho*s1*np.abs(bth[offF])
            a2 = a + m*z; a2[:2] = a[:2]
            a1 = a2/(np.abs(a2).sum() + np.linalg.norm(s*a2))
            e1 = s*a1/np.linalg.norm(s*a1)
            xh = z + s*e1                    # (U e')_j = s_j e'_j for the diagonal model (U^* e_j^* = s_j kappa_j)
            w1, nz1 = norming(lam, Phi, U, xh)
            f1 = a1 + (lam*w1) @ U
            C1 = np.linalg.norm(Phi*w1)
            d1 = lambda om: (Phi**2*w1) @ om / C1
            g2 = bth + (lam*(omth - d1(omth)*w1)) @ U
            cc = g2 @ xh
            g1 = rho*(g2 - cc*a1)
            worst = -1e9; worst_t = None; fails = []
            for t in np.concatenate([10**np.arange(-5, -0.99, 0.125), -10**np.arange(-5, -0.99, 0.125)]):
                ex = nl.pstar(dict(n=n, U=U, lam=lam, Phi=Phi, s=s), f1 + t*g1) - 1 - (t*t/2)*(1 - delta)
                if ex > worst: worst, worst_t = ex, t
                if ex > 1e-11: fails.append(t)
            print('  s_1 = %.2e (mass at j0 = %.2e): max_tau [p*(f'' + tau g'') - 1 - tau^2(1-delta)/2] = %.3e at tau = %.2e ; '
                  'failing taus in [%s]' % (s1, m[13], worst, worst_t,
                  ('%.1e .. %.1e' % (min(fails), max(fails))) if fails else 'none'))
            sys.stdout.flush()
