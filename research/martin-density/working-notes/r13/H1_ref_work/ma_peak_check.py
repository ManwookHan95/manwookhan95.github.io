"""Proposition MA' check: at the near-certificate stage of the no-peak-resource toy (np_rl_toy2 setting), the frozen value INCLUDING the
thick-type peak, rho_0 u_0 + rho_1 u_1 + rho_c u_c (zhat), vanishes (carrier 3 is kind (i)); and kappa_m = sum_peaks |zeta(c)| (route V)."""
import numpy as np
src = open('np_rl_toy2.py').read().split("for align in (True, False):")[0]
exec(src)
from scipy.optimize import brentq, minimize_scalar
for align in (True, False):
    for seed in range(1, 6):
        def gres(t):
            d = setup(t, seed, align); st = d['st']
            return sum(d['rho'][k]*st['val'][k] for k in (0, 1, 2))
        t0 = brentq(gres, 0.2, 1.0, xtol=1e-14)
        res = minimize_scalar(lambda t: svmin(t, seed, align), bounds=(t0 - 0.06, t0 + 0.06), method='bounded', options=dict(xatol=1e-14))
        d = setup(res.x, seed, align); st = d['st']
        ext = sum(d['rho'][k]*st['val'][k] for k in (0, 1, 2)); rows = sum(d['rho'][k]*st['val'][k] for k in (0, 1))
        print(f"{'aligned' if align else 'anti   '} seed {seed}: root of extended frozen value t*={t0:.5f}, argmin sv_min t={res.x:.5f} (sv={res.fun:.1e}); "
              f"at argmin: rows-only Phi0={rows:+.4f}, extended (rows+peak)={ext:+.2e}; kappa={st['kappa']:.4f} vs Phi_c|u_c|={d['Phi'][2]*abs(st['val'][2]):.4f}")
