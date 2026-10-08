import numpy as np, sys, warnings
warnings.filterwarnings("ignore")
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/refP1')
from model import *
ts = np.concatenate([-np.logspace(-4, 1, 16)[::-1], np.logspace(-4, 1, 16)])
for seed in range(3):
    M = build(seed)
    f, w, nrm = first_row(M, M['zhat'])
    u, a, zhat, nK = M['u'], M['a'], M['zhat'], M['nK']
    rng = np.random.default_rng(100+seed)
    K1 = np.zeros(M['n'], bool); K1[1:1+nK] = rng.random(nK) < 0.5
    for c in [0.05, 0.2]:
        v1 = np.where(K1, c*u, 0.0); beta = v1 @ zhat; g = v1 - beta*a
        worst = max(pstar(M, f + t*g) - np.sqrt(1+t*t) for t in ts)
        gauge2 = max((pstar(M, f + t*g)**2 - 1)/t**2 for t in ts)
        print(f"seed {seed} c={c}: two-piece g_K1: max_t [p*(f+tg) - s(t)] = {worst:.2e}, gauge^2 = {gauge2:.4f}")
    # free coordinate direction e_j*, j in J (zhat_j = 0): expect first-order growth
    j = 1 + nK + 2; g = np.zeros(M['n']); g[j] = 1.0
    vals = [(t, (pstar(M, f + t*g) - 1)/abs(t)) for t in [1e-2, 1e-3, 1e-4, -1e-3, -1e-4]]
    print("   free coord e_j*: (p*(f+tg)-1)/|t| =", [(t, round(r, 5)) for t, r in vals])
    # contact coordinate direction with g(zhat)=0: e_j* - zhat_j * alpha e_0* (j in K'); one-sided cheap
    j = 1 + 3; g = np.zeros(M['n']); g[j] = 1.0; g[0] = -zhat[j]*M['alpha']
    vals = [(t, (pstar(M, f + t*g) - 1)/abs(t)) for t in [1e-3, 1e-4, -1e-3, -1e-4]]
    print("   contact e_j* - zhat_j a/..: (p*(f+tg)-1)/|t| =", [(t, round(r, 5)) for t, r in vals])
