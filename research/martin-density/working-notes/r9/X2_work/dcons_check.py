"""X2 numerics (sanity): Proposition J (junction mismatch ~ ||X|| for VALID data) and exact d-consistency by levers."""
import numpy as np, sys
sys.path.insert(0, '.')
from xmodel import Model
from scipy.optimize import brentq
np.set_printoptions(linewidth=150)
M = Model(tg=[(1.0,0.2), (1.0,-0.6), (0.5,1.0), (-1.0,0.3)])
D0 = M.forced(M.a0, M.z0)
rho = 0.9; k0 = 1
print('statuses rho_k =', np.round(D0['nuk']/D0['theta'], 4), ' val =', np.round(D0['val'], 5), ' w =', np.round(D0['w'], 5))
psi = (M.lam*D0['w']) @ M.U
def piece(x, y0, chi):
    om_p = np.zeros(M.K); om_p[k0] = y0
    Dom = np.zeros(M.K); Dom[k0] = x
    om_m = om_p + Dom
    Delta = M.d(D0, Dom)
    v = (M.lam*Dom) @ M.U - Delta*psi
    off = np.ones(M.n, bool); off[[0, 1]] = False
    bp = np.where(off, chi*v, 0.0)
    bp = bp - (bp @ D0['zhat'])*D0['a']          # balance on F: b^+(zhat) = 0
    bm = bp - v
    Gp = D0['q0']*M.h(D0, bp) + (1 - D0['q0'])*M.H(D0, om_p)
    Gm = D0['q0']*M.h(D0, bm) + (1 - D0['q0'])*M.H(D0, om_m)
    viol = sum(max(0, -M.z0[j]*bp[j]) + max(0, M.z0[j]*bm[j]) for j in range(2, M.n))
    return dict(om_p=om_p, om_m=om_m, Dom=Dom, Delta=Delta, v=v, bp=bp, bm=bm, Gp=Gp, Gm=Gm, viol=viol)
P = piece(x=-3.0, y0=1.0, chi=0.8)
print('piece: Delta = %.5f, Gamma+ = %.4f, Gamma- = %.4f, violation mass = %.2e' % (P['Delta'], P['Gp'], P['Gm'], P['viol']))
bth = (P['bp'] + P['bm'])/2
nv = lambda D: D['zeta']/D['A']
for s1 in (1e-2, 1e-3, 1e-4, 1e-5):
    m = 4*rho*s1*np.abs(bth); m[[0, 1]] = 0
    A2 = D0['a'] + m*M.z0
    X = np.linalg.norm(M.s*m)
    D1 = M.forced(A2, M.z0)
    kap = rho/2*(M.d(D1, P['Dom']) - M.d(D0, P['Dom']))
    # levers on Omega = {k0}: pull at the last coordinate of S_k0 (flip z), bank (sign z) at the first coordinate
    jp, jb = M.S[k0][-1], M.S[k0][0]
    def F(mb, pull=True):
        A3 = A2.copy(); z3 = M.z0.copy()
        if pull:
            mu = 24*M.lam[k0]*M.U[k0, jp]; z3[jp] = -M.z0[jp]; A3[jp] = z3[jp]*mu
        A3[jb] += mb*M.z0[jb]
        D3 = M.forced(A3, z3)
        return nv(D3)[k0] - nv(D0)[k0], D3
    g0, _ = F(0.0, pull=False)
    gp, _ = F(0.0, pull=True)
    # bank at jb moves nv_k0 in the direction z_jb*sign...; choose pull or not so that a bank root exists
    use_pull = (np.sign(gp) != np.sign(F(5.0, pull=True)[0]))
    lo, hi = 0.0, 5.0
    mb = brentq(lambda t: F(t, pull=use_pull)[0], lo, hi, xtol=1e-16, rtol=1e-15) if np.sign(F(lo, use_pull)[0]) != np.sign(F(hi, use_pull)[0]) else np.nan
    res, D3 = F(mb, pull=use_pull)
    kap3 = rho/2*(M.d(D3, P['Dom']) - M.d(D0, P['Dom']))
    print('s1=%.0e  ||X||=%.3e  kappa=%+.3e  kappa/||X||=%+.4f | tuned: pull=%s bank mass=%.3e  nv residual=%.1e  kappa=%+.1e  |C3-C0|=%.2e' %
          (s1, X, kap, kap/X, use_pull, mb, res, kap3, abs(D3['C'] - D0['C'])))
