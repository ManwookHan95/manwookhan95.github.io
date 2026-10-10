"""X2 numerics: d-consistency by a TU-type lever (pull at a far signature coordinate with v ~ needed correction + bank),
long signature sets (40 coordinates), lever sizes vs ||X||."""
import numpy as np, sys
sys.path.insert(0, '.')
from xmodel import Model
from scipy.optimize import brentq
M = Model(nsig=40, tg=[(1.0,0.2), (1.0,-0.6), (0.5,1.0), (-1.0,0.3)], sdiag=[0.6, 0.5] + [0.3]*160)
D0 = M.forced(M.a0, M.z0); rho = 0.9; k0 = 1
psi = (M.lam*D0['w']) @ M.U
x, y0, chi = -3.0, 1.0, 0.8
om_p = np.zeros(M.K); om_p[k0] = y0; Dom = np.zeros(M.K); Dom[k0] = x
Delta = M.d(D0, Dom); v = (M.lam*Dom) @ M.U - Delta*psi
off = np.ones(M.n, bool); off[[0, 1]] = False
bp = np.where(off, chi*v, 0.0); bp -= (bp @ D0['zhat'])*D0['a']; bm = bp - v; bth = (bp + bm)/2
print('rho_k', np.round(D0['nuk']/D0['theta'], 4), ' Delta %.4f  Gamma+ %.4f Gamma- %.4f' % (Delta, D0['q0']*M.h(D0,bp)+(1-D0['q0'])*M.H(D0,om_p),
      D0['q0']*M.h(D0,bm)+(1-D0['q0'])*M.H(D0,om_p+Dom)))
nv = lambda D: D['zeta']/D['A']
for s1 in (1e-3, 1e-4, 1e-5, 1e-6):
    m = 4*rho*s1*np.abs(bth); m[[0, 1]] = 0
    A2 = D0['a'] + m*M.z0; X = np.linalg.norm(M.s*m)
    D1 = M.forced(A2, M.z0)
    res0 = nv(D1)[k0] - nv(D0)[k0]
    du = abs(res0)*D1['A']/M.lam[k0]              # needed change in u-units (first order)
    vk = M.U[k0, M.S[k0]]
    cand = [j for j, vv in zip(M.S[k0], vk) if vv >= 2*du]
    jp = cand[-1]; jb = M.S[k0][0]
    def F(mb, pull):
        A3 = A2.copy(); z3 = M.z0.copy()
        if pull:
            mu = 24*M.lam[k0]*M.U[k0, jp]; z3[jp] = -M.z0[jp]; A3[jp] = z3[jp]*mu
        A3[jb] += mb*M.z0[jb]
        D3 = M.forced(A3, z3); return nv(D3)[k0] - nv(D0)[k0], D3
    # bank direction: sign of d nv/d mb
    eps_b = 1e-9; slope = (F(eps_b, False)[0] - F(0, False)[0])/eps_b
    pull = np.sign(res0) == np.sign(slope)        # bank alone moves the wrong way -> pull first
    r0 = F(0, pull)[0]
    hi = 1e-12
    while np.sign(F(hi, pull)[0]) == np.sign(r0) and hi < 1e3: hi *= 2
    mb = brentq(lambda t: F(t, pull)[0], 0, hi, xtol=1e-20, rtol=1e-15)
    res, D3 = F(mb, pull)
    kap = rho/2*(M.d(D1, Dom) - M.d(D0, Dom)); kap3 = rho/2*(M.d(D3, Dom) - M.d(D0, Dom))
    print('s1=%.0e ||X||=%.2e kappa=%+.2e | pull=%s v(jp)=%.2e (needed du=%.2e) bank=%.2e  mb/||X||=%.2f  residual %.1e  kappa_tuned %+.1e' %
          (s1, X, kap, pull, M.U[k0, jp] if pull else 0, du, mb, mb/X, res, kap3))
