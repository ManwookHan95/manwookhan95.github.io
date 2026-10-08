import numpy as np, sys
from modelN import solve, f_config, sup_profile
from modelM_opt import nelder_mead

r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.3
imin, imax = -22, 26
taus = np.exp(np.linspace(np.log(r**7), np.log(r**-16), 44))
for delta in [1.0, 2.0]:
    lam, rho = f_config(r, imin, imax, delta)
    n1 = len(lam)//2
    taus_f = np.exp(np.linspace(0, np.log(1/r), 10, endpoint=False))
    supf = sup_profile(lam, rho, np.zeros_like(lam), 1.0, A, B, M, a0, taus_f)
    best = None
    for spc in [0.75, 1.0, 1.3]:
        for smc in [0.75, 1.0, 1.3]:
            rho_p = rho.copy()
            rho_p[:n1] = rho[:n1] - (1+delta)*spc/lam[:n1]
            rho_p[n1:] = rho[n1:] + (1+delta)*smc/lam[n1:]
            band = np.where(np.abs(rho_p) < 1)[0]
            if len(band) == 0: continue
            band = band[np.argsort(-lam[band])]
            room = M*(1-np.abs(rho_p[band]))*lam[band]; w0 = room/room.sum()
            def obj(z):
                xfr = np.append(z, 1.0 - np.sum(z))
                eta = np.zeros_like(lam); eta[band] = lam[band]*xfr
                return sup_profile(lam, rho_p, eta, 1.0, A, B, M, a0, taus)
            if len(band) == 1:
                vb = obj(np.array([]))
            else:
                zb, vb = nelder_mead(obj, w0[:-1], step=0.1, iters=150)
            print(f"delta={delta} s+={spc} s-={smc} J={len(band)} R={vb/supf:.4f}"); sys.stdout.flush()
            if best is None or vb < best[0]: best = (vb, spc, smc)
    print(f"delta={delta}: BEST R={best[0]/supf:.4f} at s+={best[1]} s-={best[2]}"); sys.stdout.flush()
