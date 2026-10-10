"""X1 toy check of Lemma NLM / GEN / QC (part 2), corrected scales.  One block (m = 1), two active near-threshold carriers, ratios
r = (r1, r2) > 0 on the exact zero set Z = {det[[u1(j1)-r1 t1, u2(j1)-r2 t1],[u1(j2)-r1 t2, u2(j2)-r2 t2]] = 0} (one tiny 2x2 minor,
multi-affine in r); floor statuses rho0_d = m r_d K(sigma, m^2|r|^2)/Phi_d; F = max_d rho0_d on Z.  Z, K do not involve Phi."""
import numpy as np
from scipy.optimize import brentq, minimize_scalar
m = 1; sigma = 0.02
def K(sig, R2): return (sig + np.sqrt(sig**2*R2 + sig*(1-R2)))/(1-R2)
u1 = np.array([0.6, -0.3]); u2 = np.array([0.2, 0.5]); t = np.array([0.9, 0.4])
def r2_of_r1(r1):
    A = (u1[0]-r1*t[0])*u2[1] - u2[0]*(u1[1]-r1*t[1]); B = -(u1[0]-r1*t[0])*t[1] + t[0]*(u1[1]-r1*t[1]); return -A/B
def psi(r1):
    r2 = r2_of_r1(r1); R2 = m**2*(r1**2 + r2**2)
    if r2 <= 0 or R2 >= 0.95: return None
    k = K(sigma, R2); return np.array([m*r1*k, m*r2*k])
def F(r1, Phi):
    p = psi(r1); return np.inf if p is None else max(p[0]/Phi[0], p[1]/Phi[1])
grid = np.linspace(1e-4, 0.5, 5001)
def local_mins(Phi):
    vals = np.array([F(x, Phi) for x in grid]); out = []
    for i in range(1, len(grid)-1):
        if np.isfinite(vals[i]) and vals[i] <= vals[i-1] and vals[i] <= vals[i+1]:
            res = minimize_scalar(lambda x: F(x, Phi), bounds=(grid[i-1], grid[i+1]), method='bounded', options={'xatol':1e-14})
            out.append((res.x, res.fun))
    return out
print('(1) coincidence set in the (Phi1, Phi2) plane: for fixed Phi1, the Phi2 with min local-min value of F = 1')
for Phi1 in (0.03, 0.05, 0.08, 0.12):
    def g(Phi2):
        lm = local_mins((Phi1, Phi2)); return (min(v for _, v in lm) - 1.0) if lm else np.nan
    Ps = np.linspace(0.01, 0.5, 50); gs = np.array([g(p) for p in Ps]); roots = []
    for i in range(len(Ps)-1):
        if np.isfinite(gs[i]) and np.isfinite(gs[i+1]) and gs[i]*gs[i+1] < 0: roots.append(brentq(g, Ps[i], Ps[i+1], xtol=1e-13))
    print('  Phi1=%.2f: Phi2 roots %s ; local-min value ranges over [%.3f, %.3f] on the grid' % (Phi1, [round(r, 8) for r in roots],
          np.nanmin(gs)+1, np.nanmax(gs)+1))
print('(2) at a coincidence point, the minimizer is a critical point of Psi_D (D = carriers attaining the max):')
Phi1 = 0.05
def g(Phi2):
    lm = local_mins((Phi1, Phi2)); return min(v for _, v in lm) - 1.0
Phi2c = brentq(g, 0.09, 0.13, xtol=1e-14)
if Phi2c is not None:
    Phic = (Phi1, Phi2c); x0, v = min(local_mins(Phic), key=lambda p: p[1]); p0 = psi(x0)
    D = [d for d in range(2) if abs(p0[d]/Phic[d] - 1) < 1e-6]
    eps = 1e-6; dp = (psi(x0+eps) - psi(x0-eps))/(2*eps)
    print('   Phi=(%.5f, %.8f), r1=%.8f, statuses %s, D=%s, tangential derivatives dpsi/ds = %s (opposite signs <=> critical for the max)'
          % (Phic[0], Phic[1], x0, np.round(p0/np.array(Phic), 8), D, np.round(dp, 6)))
    def G(x, Phi, h):
        r = np.array([x, r2_of_r1(x)]); best = np.inf
        for y in np.linspace(max(1e-4, x-h), x+h, 4001):
            q = np.array([y, r2_of_r1(y)])
            if np.linalg.norm(q - r) < h: best = min(best, F(y, Phi))
        return best
    print('(3) quantitative coherence mu(h) = 1 - max_{Y1} G_h:')
    for scale in (1.0, 1.001, 1.01):
        Phi = (Phic[0]*scale, Phic[1]*scale)
        xs = [x for x in grid if F(x, Phi) <= 1.0 + 1e-12]
        xs = xs + [x0]
        worst = max(G(x, Phi, 0.003) for x in xs[::max(1, len(xs)//40)])
        print('   weights scaled by %.3f: |Y1| grid points %d, mu(0.003) = %.3e' % (scale, len(xs)-1, 1 - worst))
