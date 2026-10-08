import numpy as np, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r2/refP1')
from model import *
for seed in range(4):
    M = build(seed)
    f, w, nrm = first_row(M, M['zhat'])
    pz = 1 + nrm                     # p(zhat) = q(zhat) + |R zhat|
    xi = M['zhat']/pz
    print(f"seed {seed}: f(xi) = {f@xi:.12f}, p*(f) = {pstar(M, f):.9f}, w = {np.round(w,4)}")
    # peak structure: all |w_k| = Mmax except k=1 (special) which should be 0
    Mx = np.abs(w).max(); print("   gaps:", np.round(Mx - np.abs(w), 6))
