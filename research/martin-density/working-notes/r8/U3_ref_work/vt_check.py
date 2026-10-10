"""U3 Part 5: violation tolerance with a bank (finite N = 1 model).
Model of nl_check.py plus one extra contact coordinate j0 = 13 (z = +1) touched by NO carrier: a dead zone
(psi(j0) = 0, so every exact two-piece datum has b^+(j0) = b^-(j0) and side admissibility forces it to vanish).
g := c * (coherent-shift mate of V4 Prop. 3.2 type), g_e := g - eps e_{j0}  (a dead-zone violation of mass eps,
admissible on side - only).  We measure
   E(f', h) := max over a t-grid of [ p*(f' + t h) - s(t) ]
for f' = f and for the banked rows f_m (a := (a + m e_{j0})/q*(...), z unchanged), m on a grid, and find the least m
with E(f_m, rho g_e) <= 0.  Lemma VT predicts m_min ~ C eps^2 /(1 - rho^2 kappa) (quadratic in eps), while the distance
p*(f_m - f) ~ m.
"""
import numpy as np, cvxpy as cp, importlib.util
spec = importlib.util.spec_from_file_location('nl', __file__.replace('vt_check.py', 'nl_check.py'))
nl = importlib.util.module_from_spec(spec); spec.loader.exec_module(nl)

def extend(M, bank=0.0):
    """add coordinate 13 (z=+1, no carrier) and optionally a bank of mass `bank` there; recompute forced data."""
    n = M['n'] + 1
    s = np.append(M['s'], 0.3*0.7**11)
    U = np.hstack([M['U'], np.zeros((4, 1))])
    z = np.append(M['z'], 1.0)
    a = np.append(M['a'], bank)
    qs = np.abs(a).sum() + np.linalg.norm(s*a)
    a = a/qs
    nu = np.linalg.norm(s*a)
    zhat = z + s**2*a/nu
    val = U @ zhat
    lam, Phi = M['lam'], M['Phi']
    zeta = lam*val
    w = cp.Variable(4)
    prob = cp.Problem(cp.Maximize(zeta @ w), [cp.norm(w, 'inf') + cp.norm(cp.multiply(Phi, w), 2) <= 1])
    prob.solve(solver='CLARABEL')
    w = w.value
    f = a + (lam*w) @ U
    return dict(n=n, U=U, lam=lam, Phi=Phi, s=s, a=a, z=z, zhat=zhat, val=val, w=w, f=f, normz=prob.value)

def worst(M, h, grid):
    return max(nl.pstar(M, M['f'] + t*h) - np.sqrt(1 + t*t) for t in grid)

if __name__ == '__main__':
    M0 = nl.build(flip=False)
    F0 = extend(M0)
    n = F0['n']; lam, U, w = F0['lam'], F0['U'], F0['w']
    psi = (lam*w) @ U
    km = 2
    V = U[km] - (F0['val'][km]/F0['normz'])*psi
    chi = np.zeros(n); chi[[3, 5, 7, 8, 9, 10, 11, 12]] = 1.0
    v = 30.0*lam[km]*V
    bplus = chi*v; bplus[:2] = 0
    bplus = bplus - (bplus @ F0['zhat'])*F0['a']
    g = bplus.copy()            # omega^+ = 0 (alpha = 0)
    print('psi(j0) =', psi[13], '  profile of g on S_c1:', np.round((g/np.where(psi == 0, 1, psi))[[3, 4, 5]], 6))
    grid = np.concatenate([10**np.arange(-5, 1.01, 0.125), -10**np.arange(-5, 1.01, 0.125)])
    rho = 0.9
    c = 1.0
    while worst(F0, c*g, grid) > 0:
        c *= 0.5
    g = c*g
    print('scale c =', c, '  E(f, g) =', worst(F0, g, grid), '  E(f, rho g) =', worst(F0, rho*g, grid))
    print('profile of g on S_c1:', np.round((g/np.where(psi == 0, 1, psi))[[3, 4, 5]], 6))
    for eps in (4e-3, 2e-3, 1e-3, 5e-4):
        ge = g.copy(); ge[13] -= eps; ge = ge - (ge @ F0['zhat'])*F0['a']   # keep g_e(xi) = 0
        e0 = worst(F0, rho*ge, grid)
        ms = [0.0] + list(10**np.arange(-9, -0.9, 0.125))
        mmin = None
        for m in ms:
            Fm = extend(M0, bank=m)
            if worst(Fm, rho*ge, grid) <= 1e-10:
                mmin = m; break
        dist = nl.pstar(F0, extend(M0, bank=mmin)['f'] - F0['f']) if mmin is not None else None
        print('eps = %.1e : E(f, rho g_e) = %.3e ;  least bank m on grid with E(f_m, rho g_e) <= 0 : %s ;  p*(f_m - f) = %s'
              % (eps, e0, mmin, dist))
