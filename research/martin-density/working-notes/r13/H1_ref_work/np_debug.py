import numpy as np
exec(open('np_rl_toy.py').read().split("for align in (True, False):")[0])
for align in (True, False):
    seed = 1
    for t in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]:
        d = setup(t, seed, align)
        st = d['st']; Phi = d['Phi']; Om = d['Om']; kap = st['kappa']; tuned = d['tuned']; eps = d['eps']; rc = d['rc']
        zeta_vec = Phi*st['val']; dk = dkappa(zeta_vec, Phi, Om)
        Phi0 = sum(d['rho'][k]*st['val'][k] for k in (0, 1))
        Xt = sum(rc[i]*eps[l]*dk[l]*Phi[l] for i, l in enumerate(tuned))
        g = Phi0 + d['rho'][2]*kap*(1 - Xt)/(dk[2]*Phi[2])
        print(f"align={align} t={t:5.2f} P={np.where(d['P'])[0]} val={np.round(st['val'],3)} kappa={kap:.3f} Phi0={Phi0:+.3f} Xt={Xt:+.3f} dk={np.round(dk,3)} g={g:+.3f} sv={svmin(t, seed, align):.2e}")
