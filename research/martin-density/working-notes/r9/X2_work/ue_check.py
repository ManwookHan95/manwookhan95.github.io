"""X2 numerics: Theorem UE sanity check in the finite N = 1 model.
Violated piece (one contact of a peak carrier's signature set flipped at the base row -> V has the wrong sign there),
engineered approximant with theta-masses m_j = 4 rho s1 |b^theta_j|, d-consistent lever (pull + bank on the switching carrier),
true p* by SOCP.  Reports max_tau [p*(f'+tau g') - 1 - tau^2 (1-delta)/2] for tuned / untuned approximants and several s1."""
import numpy as np, cvxpy as cp, sys
sys.path.insert(0, '.')
from xmodel import Model
from scipy.optimize import brentq
M = Model(nsig=22, tg=[(1.0,0.2), (1.0,-0.6), (0.5,1.0), (-1.0,0.3)], sdiag=[0.6, 0.5] + [0.3]*88)
k0, rho = 1, 0.9
z0 = M.z0.copy(); jv = M.S[0][2]; z0[jv] = -z0[jv]          # violated contact (peak carrier 0, far coordinate)
D0 = M.forced(M.a0, z0)
psi = (M.lam*D0['w']) @ M.U
x, y0, chi = -3.0, 1.0, 0.8
om_p = np.zeros(M.K); om_p[k0] = y0; Dom = np.zeros(M.K); Dom[k0] = x; om_m = om_p + Dom; om_t = (om_p + om_m)/2
Delta = M.d(D0, Dom); v = (M.lam*Dom) @ M.U - Delta*psi
off = np.ones(M.n, bool); off[[0, 1]] = False
bp = np.where(off, chi*v, 0.0); bp -= (bp @ D0['zhat'])*D0['a']; bm = bp - v; bth = (bp + bm)/2
viol = sum(max(0, -z0[j]*bp[j]) + max(0, z0[j]*bm[j]) for j in range(2, M.n))
Gp = D0['q0']*M.h(D0, bp) + (1-D0['q0'])*M.H(D0, om_p); Gm = D0['q0']*M.h(D0, bm) + (1-D0['q0'])*M.H(D0, om_m)
kw = max(Gp, Gm); delta = (1 - rho**2*kw)/2
print('rho_k', np.round(D0['nuk']/D0['theta'], 3), 'Delta %.4f Gamma+ %.4f Gamma- %.4f delta %.4f violation eps %.3e' % (Delta, Gp, Gm, delta, viol))
nv = lambda D: D['zeta']/D['A']
def approx(s1, tune):
    m = 4*rho*s1*np.abs(bth); m[[0, 1]] = 0
    A2 = D0['a'] + m*z0
    if not tune:
        return A2, z0.copy()
    D1 = M.forced(A2, z0); res0 = nv(D1)[k0] - nv(D0)[k0]; du = abs(res0)*D1['A']/M.lam[k0]
    jb = M.S[k0][0]
    cand = [j for j in M.S[k0][1:] if M.U[k0, j] >= 2*du]
    jp = cand[-1] if cand else M.S[k0][1]
    def F(mb, pull):
        A3 = A2.copy(); z3 = z0.copy()
        if pull:
            mu = 24*M.lam[k0]*M.U[k0, jp]; z3[jp] = -z0[jp]; A3[jp] = z3[jp]*mu
        A3[jb] += mb*z0[jb]
        return nv(M.forced(A3, z3))[k0] - nv(D0)[k0], A3, z3
    slope = (F(1e-9, False)[0] - F(0, False)[0])/1e-9
    pull = np.sign(res0) == np.sign(slope)
    r0 = F(0, pull)[0]; hi = 1e-12
    while np.sign(F(hi, pull)[0]) == np.sign(r0) and hi < 1e3: hi *= 2
    mb = brentq(lambda t: F(t, pull)[0], 0, hi, xtol=1e-22, rtol=1e-15)
    _, A3, z3 = F(mb, pull)
    return A3, z3
def pstar(h):
    W = cp.Variable(M.K); tau = cp.Variable()
    Ar = h - cp.multiply(M.lam, W) @ M.U
    cons = [cp.norm(Ar, 1) + cp.norm(cp.multiply(M.s, Ar), 2) <= tau,
            cp.norm(W, 'inf') + cp.norm(cp.multiply(M.Phi, W), 2) <= tau]
    p = cp.Problem(cp.Minimize(tau), cons)
    for solver, kw in (('CLARABEL', dict(tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12, max_iter=400)), ('ECOS', dict(abstol=1e-12, reltol=1e-12, feastol=1e-12, max_iters=400)), ('SCS', dict(eps=1e-12, max_iters=200000))):
        try:
            p.solve(solver=solver, **kw)
            if p.value is not None and np.isfinite(p.value): return p.value
        except Exception:
            pass
    return np.nan
taus = np.concatenate([-np.logspace(-4, np.log10(0.05), 20), np.logspace(-4, np.log10(0.05), 20)])
for s1fac, lab in ((64*rho/delta, '64 rho eps/delta'), (4*rho/delta, '4 rho eps/delta'), (1/20, 'eps/20')):
    s1 = s1fac*viol
    for tune in (True, False):
        A3, z3 = approx(s1, tune)
        D3 = M.forced(A3, z3)
        dmis = rho/2*(M.d(D3, Dom) - M.d(D0, Dom))
        gpp = bth + (M.lam*(om_t - M.d(D3, om_t)*D3['w'])) @ M.U
        c = gpp @ D3['zhat']
        gp = rho*(gpp - c*D3['a'])
        worst = max(pstar(D3['f'] + t*gp) - 1 - t*t*(1 - delta)/2 for t in taus)
        print('s1 = %-17s (%.2e) tuned=%-5s kappa=%+.2e  p*(f\') - 1 = %+.1e  max excess over bound = %+.3e' %
              (lab, s1, tune, dmis, pstar(D3['f']) - 1, worst))
