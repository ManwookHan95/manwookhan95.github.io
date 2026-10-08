import numpy as np, sys
from modelN import solve, f_config, sup_profile
from modelM_opt import nelder_mead

r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.3
imin, imax = -24, 30
delta = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
lam, rho = f_config(r, imin, imax, delta)
n1 = len(lam)//2
eta0 = np.zeros_like(lam)
taus_f = np.exp(np.linspace(0, np.log(1/r), 12, endpoint=False))
supf = sup_profile(lam, rho, eta0, 1.0, A, B, M, a0, taus_f)
taus = np.exp(np.linspace(np.log(r**8), np.log(r**-18), 60))
print(f"delta={delta} supP_f={supf:.4f}")
for (sp_c, sm_c, label) in [(1.0, 1.0, "both bands centred at lam=1"),
                            (1.0, 2.0, "P- band centred at lam=2"),
                            (1.0, 0.5, "P- band centred at lam=0.5")]:
    rho_p = rho.copy()
    sp = (1+delta)*sp_c; sm = (1+delta)*sm_c
    rho_p[:n1] = rho[:n1] - sp/lam[:n1]       # P+ shifted down
    rho_p[n1:] = rho[n1:] + sm/lam[n1:]       # P- shifted up
    band = np.where(np.abs(rho_p) < 1)[0]
    band = band[np.argsort(-lam[band])]
    room = M*(1-np.abs(rho_p[band]))*lam[band]
    w0 = room/room.sum()
    def obj(z):
        xfr = np.append(z, 1.0 - np.sum(z))
        eta = np.zeros_like(lam); eta[band] = lam[band]*xfr
        return sup_profile(lam, rho_p, eta, 1.0, A, B, M, a0, taus)
    v0 = obj(w0[:-1])
    zb, vb = nelder_mead(obj, w0[:-1], step=0.1, iters=300)
    print(f"  {label}: J={len(band)}  R(room-weighted)={v0/supf:.4f}  R(opt)={vb/supf:.4f}")
    sys.stdout.flush()
