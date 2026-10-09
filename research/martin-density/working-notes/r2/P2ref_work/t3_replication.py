# Pinning "Lipschitz step": if zeta' = c*zeta on [1,K] (exact replication of the window) and zeta' is ARBITRARILY perturbed beyond K,
# then |C'-C| <= sum_{k>K} Phi_k^2 / g_0 (replication identity) and sum_k lambda_k |w'(k)-w(k)| = O(sum_{k>K} Phi_k^2) + 2 sum_{k>K} lambda_k.
import numpy as np, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/P2ref_work')
from blocklib import *
rng = np.random.default_rng(11)
n = 36; m = 1
Phi = 2.0**(-np.arange(1, n+1))*rng.uniform(0.5, 1, n); lam = m*Phi
u = rng.uniform(-1, 1, n); u[[1, 4, 7]] = rng.uniform(-0.3, 0.3, 3)*Phi[[1, 4, 7]]   # strict non-peaks in the window
zeta = lam*u; w = J_clip(zeta, Phi); M = np.max(np.abs(w)); C = 1-M
for K in [8, 12, 16, 20]:
    worst = []
    for rep in range(4):
        up = u.copy(); up[K:] = rng.uniform(-1, 1, n-K)          # arbitrary deep perturbation (O(1) in sup norm)
        c = rng.uniform(0.8, 1.2)
        wp = J_clip(c*lam*up, Phi); Cp = 1-np.max(np.abs(wp))
        disp_win = np.sum(lam[:K]*np.abs(wp[:K]-w[:K]))
        worst.append((abs(Cp-C), disp_win, np.sum(lam*np.abs(wp-w))))
    w_ = np.max(np.array(worst), axis=0)
    print(f"K={K}: max|C'-C|={w_[0]:.2e} (sum_{{k>K}}Phi^2={np.sum(Phi[K:]**2):.2e});  window displacement={w_[1]:.2e};  total={w_[2]:.2e} (2 sum_{{k>K}} lam={2*np.sum(lam[K:]):.2e})")
