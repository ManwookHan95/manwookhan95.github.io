# Step 5 of Thm 3.5 and P2x 4.1(a): block part W = w' + s(omega - d' w') + s*c*(w' - w), s<0.
# c = Delta d > 0: convex combination toward w -> second order.  c < 0: first-order excess ~ 2M|s c| if w, w' have a common opposite peak.
import numpy as np, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/P2ref_work')
from blocklib import *
rng = np.random.default_rng(3)
n = 30; m = 1
Phi = 2.0**(-np.arange(1, n+1))*rng.uniform(0.5, 1, n); lam = m*Phi
u = rng.uniform(-1, 1, n); u[[1, 3]] = 0.05*Phi[[1, 3]]          # two off-peak coordinates (k=1,3) at f
up = u + 1e-3*rng.uniform(-1, 1, n); up[n-3] = -u[n-3]           # f': small perturbation + a far common OPPOSITE peak
w = J_clip(lam*u, Phi); wp = J_clip(lam*up, Phi)
M = np.max(np.abs(w)); Mp = np.max(np.abs(wp)); Cp = np.linalg.norm(Phi*wp)
pk = np.abs(np.abs(w)-M) < 1e-9; pkp = np.abs(np.abs(wp)-Mp) < 1e-9
opp = np.where(pk & pkp & (w*wp < 0))[0]
print("off-peaks at f:", np.where(~pk)[0], " common opposite peaks:", opp)
omega = np.zeros(n); omega[1] = 3.0; omega[3] = -2.0
dp = (Phi*wp)@(Phi*omega)/Cp
for c in [0.5, -0.5]:
    print(f"c = Delta d = {c}")
    for s in [-1e-2, -3e-3, -1e-3, -3e-4]:
        W = wp + s*(omega - dp*wp) + s*c*(wp - w)
        exc = N(W, Phi) - 1
        print(f"   s={s:.0e}  excess={exc:.3e}  excess/s^2={exc/s**2:.3e}  excess/|s c|={exc/abs(s*c):.3e}  (2M={2*M:.3f})")
