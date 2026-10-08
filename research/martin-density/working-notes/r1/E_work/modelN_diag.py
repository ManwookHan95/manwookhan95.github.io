import numpy as np, sys
from modelN import solve, f_config, sup_profile
from modelM_opt import nelder_mead
r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.03; delta = 1.0
lam, rho = f_config(r, -20, 24, delta); n1 = len(lam)//2
taus_f = np.exp(np.linspace(0, np.log(1/r), 24, endpoint=False))
pf = [max(solve(t, s, lam, rho, np.zeros_like(lam), 1.0, A, B, M, a0)[0] for s in (1,-1)) for t in taus_f]
supf = max(pf); print("f-profile over one octave: min %.4f max %.4f" % (min(pf), supf))
lam1 = lam[:n1]
S = np.where(lam1 >= 1.0, (1+delta)*1.0, (1+delta)*0.5)
rho_p = rho.copy(); rho_p[:n1] = rho[:n1] - S/lam1; rho_p[n1:] = rho[n1:] + S/lam1
band = np.where(np.abs(rho_p) < 1)[0]; band = band[np.argsort(-lam[band])]
taus = np.unique(np.concatenate([np.exp(np.linspace(np.log(r**6), np.log(r**-6), 61)), np.exp(np.linspace(np.log(r**-6), np.log(r**-16), 21))]))
room = M*(1-np.abs(rho_p[band]))*lam[band]; w0 = room/room.sum()
def prof(z):
    xfr = np.append(z, 1.0 - np.sum(z)); eta = np.zeros_like(lam); eta[band] = lam[band]*xfr
    return [max(solve(t, s, lam, rho_p, eta, 1.0, A, B, M, a0)[0] for s in (1,-1)) for t in taus]
zb, vb = nelder_mead(lambda z: max(prof(z)), w0[:-1], step=0.1, iters=200)
p = prof(zb)
print("frozen weights", np.round(np.append(zb, 1-zb.sum()), 3), "band lam", lam[band], "rho", np.round(rho_p[band],2))
print("R =", max(p)/supf)
for t, v in zip(taus, p):
    if v > supf*0.995: print("  tau=%.4f  P_f'=%.4f  ratio=%.4f" % (t, v, v/supf))
print("tau->0 limit (Hilbert of frozen):", B*np.sum(np.append(zb,1-zb.sum())**2), " vs supf", supf)
