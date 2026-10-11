import numpy as np
from puiseux_toy import psi, mu_curve
# finer cone grid; fit exponent only where D(m) >= 4 x grid resolution
c = np.array([0.20, 0.15, 0.05]); ns, nt = 800, 6000
s = np.linspace(0, 0.06, ns); th = np.linspace(0, 2*np.pi, nt, endpoint=False)
S, TH = np.meshgrid(s, th, indexing='ij')
PA = np.concatenate([np.stack([c[0]+S*np.cos(TH), c[1]+S*np.sin(TH), c[2]+sg*S], -1).reshape(-1,3) for sg in (1,-1)])
res = max(0.06/ns, 0.06*2*np.pi/nt); print("grid resolution ~", res)
pc = np.array([psi(c[None],0)[0], psi(c[None],1)[0]])
ms = np.geomspace(5e-4, 2e-2, 8)
for label, Phi in [("generic", pc/(1-3e-3)*np.array([1.0,1.0+2.1e-3])), ("coincidence", pc.copy())]:
    Fv = np.maximum(psi(PA,0)/Phi[0], psi(PA,1)/Phi[1]); D = mu_curve(PA, Fv, ms)
    ok = D >= 4*res
    print(label, " m/D(m):", np.round(ms/D, 3), " fitted beta on D>=4res:", np.round(np.polyfit(np.log(D[ok]), np.log(ms[ok]), 1)[0], 3))
