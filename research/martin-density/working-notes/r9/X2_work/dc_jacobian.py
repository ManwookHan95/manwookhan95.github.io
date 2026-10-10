"""X2 numerics: Lemma DC linearization.  Two strict non-peaks in Omega (one block), levers = z-moves at a free coordinate of each
carrier's signature set (exact first-order slope v), F_l(P) = eps_l[u_l(xhat(P)) - (A(P)/A0) u_l(zhat0)].  Compare the finite-difference
Jacobian with I - p q^T (p_l = eps_l u_l/A0, q_k = eps_k lambda_k w(k)) and check 1 - q^T p >= 1 - C."""
import numpy as np, sys
sys.path.insert(0, '.')
from xmodel import Model
rng = np.random.default_rng(3)
worst = 0; mindet = 1; cnt = 0
for trial in range(40):
    tg = [(1.0, rng.uniform(-1,1)), (1.0, rng.uniform(-0.9,-0.5)), (0.5, 1.0), (1.0, rng.uniform(-0.9,-0.4))]
    M = Model(nsig=10, tg=tg, sdiag=[0.6,0.5]+[0.3]*40, Phi=[0.2, 0.08, 0.05, 0.03])
    z = M.z0.copy()
    D0 = M.forced(M.a0, z)
    rho = D0['nuk']/D0['theta']
    Om = [k for k in range(M.K) if rho[k] < 0.9 and rho[k] > 0.05]
    if len(Om) < 2: continue
    lev = {k: M.S[k][1] for k in Om}
    for k in Om: z[lev[k]] = 0.3*np.sign(z[lev[k]])           # make the lever coordinate free (room 0.7)
    D0 = M.forced(M.a0, z)
    eps = {k: 1.0 for k in Om}
    def F(P):
        zz = z.copy()
        for i, k in enumerate(Om): zz[lev[k]] += eps[k]*P[i]/M.U[k, lev[k]]
        D = M.forced(M.a0, zz)
        return np.array([eps[k]*(D['val'][k] - D['A']/D0['A']*D0['val'][k]) for k in Om])
    h = 1e-7
    J = np.array([(F(h*e) - F(-h*e))/(2*h) for e in np.eye(len(Om))]).T
    p = np.array([eps[k]*D0['val'][k]/D0['A'] for k in Om]); q = np.array([eps[k]*M.lam[k]*D0['w'][k] for k in Om])
    Jth = np.eye(len(Om)) - np.outer(p, q)
    cnt += 1; worst = max(worst, np.abs(J - Jth).max()); mindet = min(mindet, (1 - q @ p) - (1 - D0['C']))
print(cnt, "trials with |Omega| >= 2; max |J_fd - (I - p q^T)| = %.2e ; min over trials of (1 - q.p) - (1 - C) = %.3e (>= 0 predicted)" % (worst, mindet))
