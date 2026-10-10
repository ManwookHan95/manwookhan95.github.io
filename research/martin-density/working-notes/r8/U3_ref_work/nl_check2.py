"""U3 Part 5 (numerics for Theorem NL / Proposition S3), well-conditioned version.
Finite N = 1 model from nl_check.py (carriers c1, c2 robust peaks; lm tuned anti-type strict non-peak (q<0);
o: target y*, aligned peak in f (z=-1 on S_o), ANTI-TYPE peak in f_n (z=+1 on S_o)).
Checks:
 (1) the explicit coherent-shift mate g of f (V4 Prop 3.2 with split chi = 1 at s1, 0 at s2): two-piece data at f,
     V z-signed off F, profile pi_g(s1) != pi_g(s2), p*(f + t c g) <= s(t) on a grid;
 (2) at f_n: p*(f_n + t c g) - s(t) > 0 for small |t| of one sign (linear excess), i.e. c g notin C(f_n);
 (3) at f_n: side-+ and side-- one-sided coefficients gamma^+-(c g) via SOCP: one side infeasible;
 (4) at f_n: the maximum of pi_h(s1) - pi_h(s2) over h with BOTH sides admissible (two-piece data, kappa_w <= 1) is 0.
"""
import numpy as np, cvxpy as cp
import importlib.util, sys
spec = importlib.util.spec_from_file_location('nl', __file__.replace('nl_check2.py', 'nl_check.py'))
nl = importlib.util.module_from_spec(spec); spec.loader.exec_module(nl)

def data(M):
    lam, Phi, w, U = M['lam'], M['Phi'], M['w'], M['U']
    psi = (lam*w) @ U
    Mx = np.max(np.abs(w)); C = np.linalg.norm(Phi*w)
    q0 = 1/(1 + M['normz']); sigma = q0*M['normz']
    nu = np.linalg.norm(M['s']*M['a']); e = M['s']*M['a']/nu
    P = [k for k in range(4) if abs(abs(w[k]) - Mx) < 1e-7]
    Q = [k for k in range(4) if k not in P]
    return dict(psi=psi, M=Mx, C=C, q0=q0, sigma=sigma, nu=nu, e=e, P=P, Q=Q)

def dfun(M, D, om):   # d(omega) = <D w, D omega>/C
    return (M['Phi']**2*M['w']) @ om / D['C']

def gamma_side(M, D, h, side):
    """min Gamma_w(b, omega) over side-admissible pairs representing h; returns (value or None)."""
    n = M['n']; z = M['z']
    b = cp.Variable(n); om = cp.Variable(4)
    cons = [om[k] == 0 for k in D['P']]
    dom = (M['Phi']**2*M['w']) @ om / D['C']
    cons += [b + cp.multiply(M['lam'], om - dom*M['w']) @ M['U'] == h]
    for j in range(2, n):            # all coordinates off F are contacts in this model
        cons += [side*z[j]*b[j] >= 0]
    Ub = cp.multiply(M['s'], b)
    Pperp = Ub - (D['e'] @ Ub)*D['e']
    hb = cp.sum_squares(Pperp)/D['nu']
    Hom = (cp.sum_squares(cp.multiply(M['Phi'], om)) - cp.square(dom))/D['C']
    # H(omega) = ||P_perp D omega||^2/C is convex; write it as ||D om - (dom/C) D w||^2 / C
    Dw = M['Phi']*M['w']
    Hom = cp.sum_squares(cp.multiply(M['Phi'], om) - dom*Dw/D['C'])/D['C']
    prob = cp.Problem(cp.Minimize(D['q0']*hb + D['sigma']*Hom), cons)
    try:
        prob.solve(solver='CLARABEL')
    except Exception as ex:
        return None, str(ex)
    return prob.value, prob.status

if __name__ == '__main__':
    M0 = nl.build(flip=False)
    M1 = nl.build(flip=True, ratio=M0['ratio'])
    D0, D1 = data(M0), data(M1)
    n = M0['n']; z = M0['z']
    print('f : P =', D0['P'], 'Q =', D0['Q'], ' M, C =', round(D0['M'], 6), round(D0['C'], 6), ' q0 =', round(D0['q0'], 6))
    print('f_n: P =', D1['P'], 'Q =', D1['Q'])
    km = 2   # the tuned anti-type strict non-peak
    lam, U, w = M0['lam'], M0['U'], M0['w']
    psi = D0['psi']
    V = U[km] - (M0['val'][km]/M0['normz'])*psi
    offF = np.arange(2, n)
    print('z*V off F (should be >= 0):', np.round((z*V)[offF], 7))
    s1, s2 = 3, 4
    chi = np.zeros(n); chi[s1] = 1.0; chi[[5,7,8,9,10,11,12]] = 0.5
    alpha, dalpha = 0.0, 1.0
    v = dalpha*lam[km]*V
    bplus = chi*v; bplus[:2] = 0
    bplus = bplus - (bplus @ M0['zhat'])*M0['a']          # b^+(zhat) = 0  (a(zhat) = 1)
    om_p = np.zeros(4); om_p[km] = alpha
    g = bplus + (lam*(om_p - dfun(M0, D0, om_p)*w)) @ U
    pi = g/psi
    print('profile pi_g at s1, s2, S_c1:', np.round(pi[[3,4,5]], 6))
    # scale so that p*(f + t c g) <= s(t) on a grid
    for c in (1.0, 0.3, 0.1, 0.03, 0.01):
        worst = -1e9
        for t in np.concatenate([10**np.arange(-3, 1.01, 0.25), -10**np.arange(-3, 1.01, 0.25)]):
            ex = nl.pstar(M0, M0['f'] + t*c*g) - np.sqrt(1 + t*t)
            worst = max(worst, ex)
        print('c = %.2f : max_t [p*(f + t c g) - s(t)] on grid = %.3e' % (c, worst))
        if worst <= 1e-9:
            break
    cg = c*g
    print('\nAt f_n: p*(f_n + t c g) - s(t):')
    for t in (1e-1, 3e-2, 1e-2, 3e-3, 1e-3):
        print('  t = %+.0e : %.3e    t = %+.0e : %.3e' % (t, nl.pstar(M1, M1['f'] + t*cg) - np.sqrt(1+t*t),
                                                       -t, nl.pstar(M1, M1['f'] - t*cg) - np.sqrt(1+t*t)))
    print('\nOne-sided coefficients of c g:')
    for name, M, D in (('f', M0, D0), ('f_n', M1, D1)):
        for side in (+1, -1):
            val, st = gamma_side(M, D, cg, side)
            print('  %s side %+d : gamma = %s (%s)' % (name, side, val, st))
    print('p*(f_n - f) =', nl.pstar(M0, M1['f'] - M0['f']))

def max_osc_twopiece(M, D, s1, s2, kappa=1.0):
    """max of pi_h(s1) - pi_h(s2) over h carrying two-piece data (both sides) with Gamma_w <= kappa on each side."""
    n = M['n']; z = M['z']; psi = D['psi']; Dw = M['Phi']*M['w']
    h = cp.Variable(n)
    cons = []
    for side in (+1, -1):
        b = cp.Variable(n); om = cp.Variable(4)
        cons += [om[k] == 0 for k in D['P']]
        dom = (M['Phi']**2*M['w']) @ om / D['C']
        cons += [b + cp.multiply(M['lam'], om - dom*M['w']) @ M['U'] == h]
        cons += [side*z[j]*b[j] >= 0 for j in range(2, n)]
        Ub = cp.multiply(M['s'], b); Pperp = Ub - (D['e'] @ Ub)*D['e']
        G = D['q0']*cp.sum_squares(Pperp)/D['nu'] + D['sigma']*cp.sum_squares(cp.multiply(M['Phi'], om) - dom*Dw/D['C'])/D['C']
        cons += [G <= kappa]
    obj = h[s1]/psi[s1] - h[s2]/psi[s2]
    p = cp.Problem(cp.Maximize(obj), cons); p.solve(solver='CLARABEL')
    return p.value, p.status

if __name__ == '__main__':
    for name, M, D in (('f', M0, D0), ('f_n', M1, D1)):
        val, st = max_osc_twopiece(M, D, 3, 4)
        print('%s: max over two-piece data (kappa_w <= 1) of pi_h(s1) - pi_h(s2) = %s (%s)' % (name, val, st))
