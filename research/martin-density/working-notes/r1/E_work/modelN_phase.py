import numpy as np, sys
from modelN import solve, f_config, sup_profile
from modelM_opt import nelder_mead
r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.03; delta = 1.0
imin, imax = -20, 24
lam, rho = f_config(r, imin, imax, delta)
n1 = len(lam)//2
taus_f = np.exp(np.linspace(0, np.log(1/r), 24, endpoint=False))
supf = sup_profile(lam, rho, np.zeros_like(lam), 1.0, A, B, M, a0, taus_f)
taus = np.unique(np.concatenate([np.exp(np.linspace(np.log(r**6), np.log(r**-6), 61)),
                                 np.exp(np.linspace(np.log(r**-6), np.log(r**-16), 21))]))
lam1 = lam[:n1]
for phase in [0.85, 1.0, 1.15, 1.3]:
    S = np.where(lam1 >= 1.0, (1+delta)*1.0*phase, (1+delta)*0.5*phase)
    rho_p = rho.copy(); rho_p[:n1] = rho[:n1] - S/lam1; rho_p[n1:] = rho[n1:] + S/lam1
    band = np.where(np.abs(rho_p) < 1)[0]; band = band[np.argsort(-lam[band])]
    room = M*(1-np.abs(rho_p[band]))*lam[band]; w0 = room/room.sum()
    def obj(z):
        xfr = np.append(z, 1.0 - np.sum(z)); eta = np.zeros_like(lam); eta[band] = lam[band]*xfr
        return sup_profile(lam, rho_p, eta, 1.0, A, B, M, a0, taus)
    zb, vb = nelder_mead(obj, w0[:-1], step=0.1, iters=200)
    print(f"phase={phase} J={len(band)} lam={np.round(lam[band],2)} rho={np.round(rho_p[band],2)} R={vb/supf:.4f}"); sys.stdout.flush()
