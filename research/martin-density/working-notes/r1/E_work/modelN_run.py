import numpy as np, sys
from modelN import solve, f_config, sup_profile
from modelM_opt import nelder_mead

r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.3
imin, imax = -24, 30
for delta in [1.0, 0.3, 0.1]:
    lam, rho = f_config(r, imin, imax, delta)
    eta0 = np.zeros_like(lam)
    taus_f = np.exp(np.linspace(0, np.log(1/r), 12, endpoint=False))
    supf = sup_profile(lam, rho, eta0, 1.0, A, B, M, a0, taus_f)
    # f': shift s = 1+delta (band centre at lam=1)
    s = 1+delta
    rho_p = rho - s/lam
    band = np.where(np.abs(rho_p) < 1)[0]
    # order band resources by scale (coarse to fine)
    band = band[np.argsort(-lam[band])]
    taus = np.exp(np.linspace(np.log(r**8), np.log(r**-18), 70))
    J = len(band)
    def obj(z):
        xfr = np.append(z, 1.0 - np.sum(z))
        eta = np.zeros_like(lam); eta[band] = lam[band]*xfr
        return sup_profile(lam, rho_p, eta, 1.0, A, B, M, a0, taus)
    # initial: weights proportional to two-sided room * lam
    room = M*(1-np.abs(rho_p[band]))*lam[band]
    w0 = room/room.sum()
    v0 = obj(w0[:-1])
    zb, vb = nelder_mead(obj, w0[:-1], step=0.1, iters=250)
    print(f"delta={delta}: supP_f={supf:.4f}  band size J={J} lam={np.round(lam[band],3)} rho={np.round(rho_p[band],2)}")
    print(f"   room-weighted frozen: R={v0/supf:.4f};  optimized: R={vb/supf:.4f}  x_fr={np.round(np.append(zb,1-zb.sum()),3)}")
    sys.stdout.flush()
