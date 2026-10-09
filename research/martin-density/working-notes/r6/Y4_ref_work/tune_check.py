"""Referee check of Prop. P4 (two-sided per-carrier exact tuning, diagonal base) in a finite model.
Targets: change v_A := u_A(zhat) by -x (LOWER) and v_B := u_B(zhat) by +x (RAISE) exactly, keep the others nearly fixed.
Moves: one pull in S_A (flip z_j: +1 -> -1, mass -mu_j at j), then one private bank in S_A and one in S_B (masses >= 0),
solved by Newton on the 2 bank masses.  Carriers have components on F = {0} so that normalization effects are nonzero."""
import sys, numpy as np
sys.path.insert(0, '../Y4_work')
from toy import Model

n = 75
s = 0.8 * 2.0 ** (-0.02 * np.arange(n)); U = np.diag(s); E = np.eye(n)
targets = [0.8*E[1]+0.1*E[0], -0.8*E[2]+0.05*E[0], 0.6*E[3]+0.2*E[4], -0.7*E[5]+0.1*E[0],
           0.25*E[7]-0.1*E[8]+0.05*E[0], 0.2*E[9]+0.15*E[10]-0.05*E[0]]
sig, nxt = [], 11
for k in range(len(targets)):
    sig.append(list(range(nxt, nxt + 10))); nxt += 10
us = []
for k, y in enumerate(targets):
    h = np.zeros(n); h[sig[k]] = 2.0 ** (-np.arange(1, 11)); us.append(y + 0.15 * h)
Phis = np.array([0.05, 0.025, 0.0125, 0.006, 2e-3, 2e-3])
blk = dict(u=np.array(us), Phi=Phis, m=1); M = Model(U, [blk])
a = np.zeros(n); a[0] = 1.0; a /= M.qstar(a); z = np.ones(n)
A_, B_ = 4, 5
def vals(aa, zz):
    D = M.first_row(aa / M.qstar(aa), zz)
    return np.array([blk['u'][k] @ D['zhat'] for k in range(len(us))]), D
v0, D0 = vals(a, z)
print("values at f:", np.round(v0, 6), " w(A),w(B),M:", np.round(D0['w'][0][[A_, B_]], 5), round(D0['M'][0], 5))
for x in [1e-3, 2.5e-4, 6e-5]:
    # pull: choose j in S_A with 2 v_A(j) in [2x, ~4x]
    cand = [j for j in sig[A_] if 2 * blk['u'][A_][j] >= 2 * x]
    j = cand[-1]; vj = blk['u'][A_][j]; mu = 0.2 * vj
    ap = a.copy(); ap[j] = -mu; zp = z.copy(); zp[j] = -1.0
    jA, jB = sig[A_][0], sig[B_][0]           # private bank positions
    target = v0.copy(); target[A_] -= x; target[B_] += x
    m = np.zeros(2)
    for it in range(30):
        aa = ap.copy(); aa[jA] += m[0]; aa[jB] += m[1]
        v, _ = vals(aa, zp)
        r = v[[A_, B_]] - target[[A_, B_]]
        if np.max(np.abs(r)) < 1e-13: break
        J = np.zeros((2, 2)); h = 1e-7
        for c in range(2):
            mm = m.copy(); mm[c] += h; ab = ap.copy(); ab[jA] += mm[0]; ab[jB] += mm[1]
            J[:, c] = (vals(ab, zp)[0][[A_, B_]] - v[[A_, B_]]) / h
        m = m - np.linalg.solve(J, r)
        assert m.min() >= 0, m
    aa = ap.copy(); aa[jA] += m[0]; aa[jB] += m[1]
    v, Ds = vals(aa, zp)
    others = [k for k in range(len(us)) if k not in (A_, B_)]
    cost = M.pstar(Ds['f'] - D0['f'])
    print(f"x={x:.1e}: pull j={j} (2v={2*vj:.2e}, mu={mu:.1e}); bank masses={m}; residual={np.max(np.abs(v[[A_,B_]]-target[[A_,B_]])):.1e}; "
          f"max|d v_other|={np.max(np.abs(v[others]-v0[others])):.2e}; cost p*={cost:.2e}; cost/x={cost/x:.2f}; "
          f"min bank mass>=0: {m.min() >= 0}")
