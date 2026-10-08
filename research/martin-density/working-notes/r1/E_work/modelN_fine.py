import numpy as np, sys
from modelN import solve, f_config, sup_profile
r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.3
imin, imax = -20, 24
delta = float(sys.argv[1])
lam, rho = f_config(r, imin, imax, delta)
n1 = len(lam)//2
taus_f = np.exp(np.linspace(0, np.log(1/r), 24, endpoint=False))
supf = sup_profile(lam, rho, np.zeros_like(lam), 1.0, A, B, M, a0, taus_f)
# dense near band (lam ~ 1), coarse far away
taus = np.unique(np.concatenate([np.exp(np.linspace(np.log(r**6), np.log(r**-6), 61)),
                                 np.exp(np.linspace(np.log(r**-6), np.log(r**-16), 21))]))
def config(sp, sm):
    rho_p = rho.copy()
    rho_p[:n1] = rho[:n1] - (1+delta)*sp/lam[:n1]
    rho_p[n1:] = rho[n1:] + (1+delta)*sm/lam[n1:]
    band = np.where(np.abs(rho_p) < 1)[0]
    band = band[np.argsort(-lam[band])]
    return rho_p, band
def value(sp, sm, w):
    rho_p, band = config(sp, sm)
    if len(band) == 0: return np.inf
    w = np.asarray(w)[:len(band)]; w = w/np.sum(w)
    eta = np.zeros_like(lam); eta[band] = lam[band]*w
    return sup_profile(lam, rho_p, eta, 1.0, A, B, M, a0, taus)
print(f"delta={delta} supP_f={supf:.5f}"); sys.stdout.flush()
best = (np.inf,)
for sp in np.linspace(0.85, 1.2, 8):
    for sm in np.linspace(0.85, 1.2, 8):
        rho_p, band = config(sp, sm)
        J = len(band)
        if J == 0: continue
        if J == 1:
            v = value(sp, sm, [1.0]); wb = [1.0]
        else:
            # golden-section on first weight share if J==2, else equal weights + coordinate tweak
            if J == 2:
                lo, hi = 0.02, 0.98
                g = (np.sqrt(5)-1)/2
                a_, b_ = lo, hi
                c_ = b_ - g*(b_-a_); d_ = a_ + g*(b_-a_)
                fc = value(sp, sm, [c_, 1-c_]); fd = value(sp, sm, [d_, 1-d_])
                for _ in range(14):
                    if fc < fd: b_, d_, fd = d_, c_, fc; c_ = b_ - g*(b_-a_); fc = value(sp, sm, [c_, 1-c_])
                    else: a_, c_, fc = c_, d_, fd; d_ = a_ + g*(b_-a_); fd = value(sp, sm, [d_, 1-d_])
                v = min(fc, fd); wb = [c_, 1-c_]
            else:
                v = value(sp, sm, np.ones(J)); wb = list(np.ones(J)/J)
        if v < best[0]: best = (v, sp, sm, J, wb)
        print(f"  s+={sp:.3f} s-={sm:.3f} J={J} R={v/supf:.5f}"); sys.stdout.flush()
print(f"BEST delta={delta}: R={best[0]/supf:.5f} at s+={best[1]:.3f} s-={best[2]:.3f} J={best[3]} w={np.round(best[4],3)}")
