import numpy as np
src = open('np_rl_toy.py').read().split("for align in (True, False):")[0]
src = src.replace("U[2, S[2]['hole']] = r.uniform(0.5, 0.8, 3)", "U[2, S[2]['hole']] = DS*r.uniform(0.5, 0.8, 3)")
src = src.replace("Phi = np.array([0.4, 0.38, 0.3, 0.42])", "Phi = np.array([P01, P01*0.95, 0.3, 0.42])")
for DS, P01 in [(3, 0.4), (3, 1.0), (6, 1.0), (6, 2.0), (10, 2.0)]:
    exec(src)
    for align in (True, False):
        seed = 1; row = []
        for t in [0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0]:
            d = setup(t, seed, align)
            st = d['st']; Phi = d['Phi']; Om = d['Om']; kap = st['kappa']; tuned = d['tuned']; eps = d['eps']; rc = d['rc']
            dk = dkappa(Phi*st['val'], Phi, Om)
            Phi0 = sum(d['rho'][k]*st['val'][k] for k in (0, 1))
            Xt = sum(rc[i]*eps[l]*dk[l]*Phi[l] for i, l in enumerate(tuned))
            g = Phi0 + d['rho'][2]*kap*(1 - Xt)/(dk[2]*Phi[2]) if dk[2] != 0 else np.nan
            row.append(f"t={t}:P={''.join(map(str,np.where(d['P'])[0]))},g={g:+.2f}")
        print(f"DS={DS} P01={P01} align={align}: " + " ".join(row))
