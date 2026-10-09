"""Scan: for kappa (w(k_l)/M, i.e. 1 - gap/M) and module coefficient c, test the mate property on a t-grid and
record max over t of (minimal forced switching)/t.  Output one line per (kappa, c)."""
import sys
import numpy as np
from exp_module import build, module, forced_switching
from toy import s_of

Phil = float(sys.argv[1]) if len(sys.argv) > 1 else 2e-3
kappas = [float(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [0.1, 0.5, 0.9]
cs = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [0.01, 0.02, 0.04]
ts = np.geomspace(3e-3, 0.5, 14)
for kappa in kappas:
    M, D, l = build(kappa=kappa, Phi_l=Phil)
    b = M.blocks[0]
    mu = np.abs(b['u'][l][1:]).sum()
    for c in cs:
        g, q = module(M, D, l, c)
        worst = -1.0; ratio = 0.0; tr = None
        for t in ts:
            pp, pm, mn, mx, ms = forced_switching(M, D, g, l, t)
            worst = max(worst, pp - s_of(t), pm - s_of(t))
            if mn == mn and mn / t > ratio:
                ratio = mn / t; tr = t
        print('kappa=%.2f gap=%.3f q=%.2e lam=%.1e m_u=%.3f c=%.3f  mate=%s (max excess %.2e)  max minSwitch/t=%.3f at t=%s'
              % (kappa, D['M'][0] - D['w'][0][l], q, b['lam'][l], mu, c, worst <= 1e-9, worst, ratio, tr), flush=True)
