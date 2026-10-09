# Test Bregman identity, exact form, and smallness e(y;y') = o(A) under ADVERSARIAL perturbations
import numpy as np, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/P2ref_work')
from blocklib import *
rng = np.random.default_rng(7)
n = 40; m = 1
Phi = 2.0**(-np.arange(1, n+1))*rng.uniform(0.5, 1, n); lam = m*Phi
u = rng.uniform(-1, 1, n)
# make many off-peak coordinates at all depths: |u_k| ~ c Phi_k
off = np.arange(2, n, 2)
u[off] = rng.uniform(-1, 1, len(off))*Phi[off]*3
zeta = lam*u
w = J_clip(zeta, Phi); M = np.max(np.abs(w)); C = np.linalg.norm(Phi*w)
print("check N(w)=1:", N(w,Phi), " <w,zeta> vs primal:", w@zeta, primal(zeta,Phi))
peaks = np.abs(np.abs(w)-M) < 1e-9
print("M,C", M, C, "#off-peak", np.sum(~peaks))
theta = M*primal(zeta,Phi)/(m*C)
print("clip formula error:", np.max(np.abs(w - M*np.clip(u/(theta*Phi), -1, 1))))
for A in [1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5]:
    worst = 0; worst_disp = 0; worst_ratio_bound = 0
    for rep in range(6):
        if rep < 3:
            d = A*rng.uniform(-1, 1, n)
        else:
            # adversarial: push each off-peak coordinate toward threshold crossing in the sign that increases |u|
            d = A*np.sign(u)*(1.0)
        up = u + d; zp = lam*up
        wp = J_clip(zp, Phi); nzp = wp@zp; nz = w@zeta
        e = 1 - (w@zp)/nzp; ebar = 1 - (wp@zeta)/nz
        lhs = nzp*e + nz*ebar; rhs = (wp-w)@(zp-zeta)
        assert abs(lhs-rhs) < 1e-9*max(1,abs(rhs)), (lhs, rhs)
        worst = max(worst, e/A); worst_disp = max(worst_disp, np.sum(lam*np.abs(wp-w))/A)
    print(f"A={A:.0e}  max e/A={worst:.3e}   max sum lam|dw|/A={worst_disp:.3f}")
