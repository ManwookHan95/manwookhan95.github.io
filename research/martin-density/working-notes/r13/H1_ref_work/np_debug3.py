import numpy as np
src = open('np_rl_toy.py').read().split("for align in (True, False):")[0]
src = src.replace("U[2, S[2]['hole']] = r.uniform(0.5, 0.8, 3)", "U[2, S[2]['hole']] = DS*r.uniform(0.5, 0.8, 3)")
src = src.replace("Phi = np.array([0.4, 0.38, 0.3, 0.42])", "Phi = np.array([P01, P01*0.95, PC, 0.42])")
src = src.replace("rc_ = 0.5 if align else -0.5", "rc_ = RC if align else -RC")
for DS, P01, PC, RC in [(3, 1.0, 0.6, 0.08), (2, 1.0, 0.6, 0.05), (3, 1.0, 0.8, 0.1), (2, 0.8, 0.8, 0.1)]:
    exec(src)
    for align in (True, False):
        seed = 1; row = []
        for t in [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.85, 1.0, 1.25, 1.5]:
            d = setup(t, seed, align)
            st = d['st']; Phi = d['Phi']; Om = d['Om']; kap = st['kappa']; tuned = d['tuned']; eps = d['eps']; rc = d['rc']
            dk = dkappa(Phi*st['val'], Phi, Om)
            Phi0 = sum(d['rho'][k]*st['val'][k] for k in (0, 1))
            Xt = sum(rc[i]*eps[l]*dk[l]*Phi[l] for i, l in enumerate(tuned))
            g = Phi0 + d['rho'][2]*kap*(1 - Xt)/(dk[2]*Phi[2]) if dk[2] != 0 else np.nan
            row.append(f"{t}:{''.join(map(str,np.where(d['P'])[0]))},{g:+.2f}")
        print(f"DS={DS} P01={P01} PC={PC} RC={RC} align={align}: " + " ".join(row))
