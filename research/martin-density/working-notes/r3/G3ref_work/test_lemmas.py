import numpy as np, warnings
warnings.filterwarnings('ignore')
from model import build_f, pstar, qstar, Nblk
from model2 import make_model2
from mates import scale_to_boundary
M = build_f(make_model2())
G = np.load('Gbasis.npy')
rng = np.random.default_rng(11)
g0 = G.T @ rng.standard_normal(G.shape[0])
c = scale_to_boundary(M, g0); g = 0.999*c*g0
print('mate scale c =', c, ' g =', np.round(g, 4))
F = [0, 1]; notF = [j for j in range(M['n']) if j not in F]
z, q0, w, Phi, lam, u = M['z'], M['q0'], M['w'], M['Phi'], M['lam'], M['u']
gamma = 0.7; J = [j for j in notF if abs(z[j]) <= 1-gamma]
Mw, C = M['Mw'], M['C']
peaks = np.isclose(np.abs(w), Mw, atol=1e-6)
for t in [3e-2, 1e-2, 3e-3, 1e-3]:
    vp, Ap, Wp = pstar(M, M['f'] + t*g, ret=True)
    vm, Am, Wm = pstar(M, M['f'] - t*g, ret=True)
    Bp, Bm = (Ap - M['a'])/t, (M['a'] - Am)/t
    Op, Om = (Wp - w)/t, (w - Wm)/t
    # 2.3(b)
    lhs_p = sum(abs(Bp[j]) - z[j]*Bp[j] for j in notF); lhs_m = sum(abs(Bm[j]) + z[j]*Bm[j] for j in notF)
    # pinning: Delta c_k and E_k
    cp_, cm_ = lam*Op, lam*Om; dc = cp_ - cm_
    dB = Bp - Bm
    resid = dB + (u.T @ dc)      # should be 0 (both represent g)
    E = np.array([abs(dB[M['sig'][k]]) if M['sig'][k] in J else np.nan for k in range(M['K'])])
    dprime = np.array([abs(u[k, M['sig'][k]]) for k in range(M['K'])])
    # pinning inequality per k: dprime_k |dc_k| <= E_k + sum_{k'>k} |u_{k'}(sig_k)| |dc_k'|
    pin = [dprime[k]*abs(dc[k]) - (E[k] + sum(abs(u[kk, M['sig'][k]])*abs(dc[kk]) for kk in range(k+1, M['K']))) for k in range(M['K'])]
    print(f't={t:.0e} p*(+)-s={vp-np.sqrt(1+t*t):.1e} p*(-)-s={vm-np.sqrt(1+t*t):.1e} | 2.3b: {lhs_p:.2e},{lhs_m:.2e} <= {t/(2*q0):.2e}'
          f' | resid {np.abs(resid).max():.1e} | sum|dc| {np.abs(dc).sum():.2e} (/t={np.abs(dc).sum()/t:.2f}) | max pin viol {max(pin):.1e}')
