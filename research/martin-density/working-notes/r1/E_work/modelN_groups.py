import numpy as np, sys
from modelN import solve, f_config, sup_profile
from modelM_opt import nelder_mead
# both types converted at several adjacent scales: group scalars S(lam) piecewise constant
r = 0.5; M = 0.5; A = 1.0; B = 0.5; a0 = 0.3
imin, imax = -20, 24
taus = np.exp(np.linspace(np.log(r**7), np.log(r**-15), 40))
delta = float(sys.argv[1]); ngroups = int(sys.argv[2])
lam, rho = f_config(r, imin, imax, delta)
n1 = len(lam)//2
taus_f = np.exp(np.linspace(0, np.log(1/r), 10, endpoint=False))
supf = sup_profile(lam, rho, np.zeros_like(lam), 1.0, A, B, M, a0, taus_f)
# group g (g=0..ngroups-1) converts scale r**g ; group boundaries between those scales
lam1 = lam[:n1]
S = np.empty_like(lam1)
for i, l in enumerate(lam1):
    g = int(np.clip(np.round(np.log(l)/np.log(r)), 0, ngroups-1)) if l <= 1.0 else 0
    if l < r**(ngroups-1): g = ngroups-1
    S[i] = (1+delta)*r**g
rho_p = rho.copy()
rho_p[:n1] = rho[:n1] - S/lam1
rho_p[n1:] = rho[n1:] + S/lam1
band = np.where(np.abs(rho_p) < 1)[0]
band = band[np.argsort(-lam[band])]
room = M*(1-np.abs(rho_p[band]))*lam[band]; w0 = room/room.sum()
def obj(z):
    xfr = np.append(z, 1.0 - np.sum(z))
    eta = np.zeros_like(lam); eta[band] = lam[band]*xfr
    return sup_profile(lam, rho_p, eta, 1.0, A, B, M, a0, taus)
v0 = obj(w0[:-1])
zb, vb = nelder_mead(obj, w0[:-1], step=0.1, iters=250)
print(f"delta={delta} groups={ngroups} band J={len(band)} lam={np.round(lam[band],3)} R(room)={v0/supf:.4f} R(opt)={vb/supf:.4f}")
