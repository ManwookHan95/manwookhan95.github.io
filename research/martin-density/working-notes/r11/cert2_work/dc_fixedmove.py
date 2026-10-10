"""cert2 (DC-b): F(0) contains the second-order effect of the FIXED TU pull/bank; isolate it (no pre-row masses) and check
the scaling ~ (2 v(j_p)/(mu_j' v_l(j')))^2 (i.e. C_2 r^2 with C_2 ~ 4^G / (mu v)^2), absent from X2-ref's (p-DC1) bound."""
import numpy as np
from dc_cert2 import build
rows = []
for seed in range(30):
    md, A0, z0, sig, role, S = build(seed, 1)
    D0 = md.forced(A0, z0)
    Om = [i for i in sig if not D0['blocks'][1]['P'][list(D0['blocks'][1]['idx']).index(i)]]
    if not Om: continue
    i = Om[0]; ss = sig[i]; v = md.U[i]; j = ss[1]
    nu0 = np.linalg.norm(md.mu*A0)
    for jp in ss[6::3]:
        A = A0.copy(); z = z0.copy()
        z[jp] = -1.0; A[jp] += -24*md.lam[i]*v[jp]; A[j] += nu0/(md.mu[j]**2*v[j])*(2*v[jp])
        D = md.forced(A, z)
        F0 = D['val'][i] - D['blocks'][1]['A']/D0['blocks'][1]['A']*D0['val'][i]
        pred = (2*v[jp]/(md.mu[j]*v[j]))**2
        rows.append((v[jp], abs(F0), pred))
rows = np.array(rows)
ratio = rows[:,1]/rows[:,2]
print(f"instances {len(rows)}; |F(0)| / (2v/(mu v_bank))^2 : min {ratio.min():.3f} median {np.median(ratio):.3f} max {ratio.max():.3f}")
# scaling exponent in v(j_p): fit log|F0| vs log v
sl = np.polyfit(np.log(rows[:,0]), np.log(rows[:,1]), 1)[0]
print(f"fitted exponent of |F(0)| in v(j_p): {sl:.2f}  (2 = second order, as claimed in (DC-b))")
# per-instance slopes (fixed seed, varying pull depth)
sl_all = []
for seed in range(30):
    md, A0, z0, sig, role, S = build(seed, 1)
    D0 = md.forced(A0, z0)
    Om = [i for i in sig if not D0['blocks'][1]['P'][list(D0['blocks'][1]['idx']).index(i)]]
    if not Om: continue
    i = Om[0]; ss = sig[i]; v = md.U[i]; j = ss[1]; nu0 = np.linalg.norm(md.mu*A0)
    pts = []
    for jp in ss[8:24:2]:
        A = A0.copy(); z = z0.copy()
        z[jp] = -1.0; A[jp] += -24*md.lam[i]*v[jp]; A[j] += nu0/(md.mu[j]**2*v[j])*(2*v[jp])
        D = md.forced(A, z)
        pts.append((v[jp], abs(D['val'][i] - D['blocks'][1]['A']/D0['blocks'][1]['A']*D0['val'][i])))
    pts = np.array(pts)
    sl_all.append(np.polyfit(np.log(pts[:,0]), np.log(pts[:,1]), 1)[0])
print("per-instance exponents:", np.round(sl_all, 2))
