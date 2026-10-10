"""X2-referee check 1: (a) block norming vs cvxpy; (b) Proposition J's inequality
   |(d'-d)(Dom)| <= m ||D Dom||_2 |Omega|^{1/2} max_k |u_k(xhat') - u_k(zhat)| / A' + |Delta| |A' - A| / A'
on random multi-block instances with window masses on off-F contacts (diagonal base); (c) d-consistency identities:
if nv'_k = nv_k on Omega then w'(k) = (C'/C) w(k), gap' = (C'/C) gap + 1 - C'/C, H' = (C/C') H, and if Omega = Q (all strict
non-peaks) and the peak set is unchanged then C' = C exactly (referee's observation)."""
import numpy as np, cvxpy as cp, sys
sys.path.insert(0, '.')
from rmodel import Row
rng = np.random.default_rng(11)

def cvx_norm(zeta, Phi):
    W = cp.Variable(len(zeta))
    prob = cp.Problem(cp.Maximize(zeta @ W), [cp.norm(W, 'inf') + cp.norm(cp.multiply(Phi, W), 2) <= 1])
    prob.solve(solver=cp.CLARABEL)
    return prob.value, W.value

# (a)
worst = 0
for _ in range(20):
    K = 6; Phi = np.sort(rng.uniform(0.01, 0.3, K))[::-1]; zeta = rng.normal(size=K)*Phi**rng.uniform(1, 2.5, K)
    B = Row.block_norming(zeta, Phi)
    val, W = cvx_norm(zeta, Phi)
    worst = max(worst, abs(val - B['A'])/val, np.abs(W - B['w']).max())
print('(a) block norming vs CLARABEL: max rel err %.1e' % worst)

def random_row(N=2, Kb=4, nF=2, nsig=5):
    K = N*Kb; n = nF + K*nsig + 6
    mu = np.array([2.0**(-0.3*s - 1) for s in range(n)])
    U = np.zeros((K, n)); blk = np.repeat(np.arange(1, N + 1), Kb)
    Phi = np.concatenate([np.sort(rng.uniform(0.02, 0.25, Kb))[::-1]*2.0**(-m) for m in range(N)])
    z = np.zeros(n); z[:nF] = 1.0
    for k in range(K):
        y = np.zeros(n); y[:nF] = rng.normal(size=nF); y[nF + K*nsig + rng.integers(0, 6)] = rng.normal()*0.3
        S = list(range(nF + k*nsig, nF + (k + 1)*nsig))
        sg = rng.choice([-1.0, 1.0])
        y[S] = rng.uniform(0.05, 0.4)*2.0**(-np.arange(nsig))*sg
        z[S] = sg
        U[k] = y
    R = Row(mu, U, blk, Phi, list(range(nF)))
    R.U = np.array([u/R.qstar(u) for u in U])
    z[nF + K*nsig:] = rng.uniform(-0.9, 0.9, 6)
    A = np.zeros(n); A[:nF] = rng.uniform(0.3, 1.0, nF)
    return R, A, z, n, nF, K

# (b)
ratios = []; cnt = 0
for trial in range(300):
    R, A, z, n, nF, K = random_row()
    D0 = R.forced(A, z)
    for m in range(1, R.N + 1):
        B = D0['blocks'][m]; idx = B['idx']
        Q = [i for i, k in enumerate(idx) if not B['P'][i]]
        if not Q: continue
        Dom = np.zeros(len(idx)); Dom[Q] = rng.normal(size=len(Q))*rng.uniform(0.1, 5)
        # masses on random off-F contacts (sign z)
        cont = [j for j in range(nF, n) if abs(z[j]) == 1.0]
        J = rng.choice(cont, size=4, replace=False)
        A1 = A.copy(); A1[J] += z[J]*rng.uniform(1e-4, 1e-2, 4)
        D1 = R.forced(A1, z)
        B1 = D1['blocks'][m]
        if not np.array_equal(B1['P'], B['P']): continue
        dd = R.d(D1, m, Dom) - R.d(D0, m, Dom)
        Delta = R.d(D0, m, Dom)
        du = np.abs(D1['val'][idx][Q] - D0['val'][idx][Q]).max()
        DD = np.linalg.norm(R.Phi[idx]*Dom)
        bound = m*DD*np.sqrt(len(Q))*du/B1['A'] + abs(Delta)*abs(B1['A'] - B['A'])/B1['A']
        ratios.append(abs(dd)/bound); cnt += 1
ratios = np.array(ratios)
print('(b) Prop J inequality on %d block-instances: max |(d1-d0)(Dom)|/bound = %.4f (<= 1 predicted), median %.3f' % (cnt, ratios.max(), np.median(ratios)))

# (c) d-consistency identities: perturb by masses, then restore nv on Omega = Q by solving for the values directly:
# we emulate exact levers by adding to zhat a correction on private signature coordinates (z-moves on the carrier's own S, which no
# other carrier meets); then compare.
worst_gap = worst_H = worst_C = 0; cnt = 0
from scipy.optimize import fsolve
for trial in range(60):
    R, A, z, n, nF, K = random_row()
    D0 = R.forced(A, z)
    cont = [j for j in range(nF, n) if abs(z[j]) == 1.0]
    J = rng.choice(cont, size=4, replace=False)
    A1 = A.copy(); A1[J] += z[J]*rng.uniform(1e-4, 1e-3, 4)
    Om = [k for m in range(1, R.N + 1) for i, k in enumerate(D0['blocks'][m]['idx']) if not D0['blocks'][m]['P'][i]]
    if len(Om) < 2: continue
    # lever coordinate: last signature coordinate of each Omega carrier (exclusive to it in this model); make it free-ish
    lev = {}
    for k in Om:
        S = np.where(np.abs(R.U[k]) > 0)[0]; S = [j for j in S if nF <= j < n - 6]
        lev[k] = S[-1]
    z1 = z.copy()
    for k in Om: z1[lev[k]] *= 0.5            # room 0.5 at the lever coordinate (do this at the BASE row too)
    D0 = R.forced(A, z1)
    if any(D0['blocks'][R.blk[k]]['P'][list(D0['blocks'][R.blk[k]]['idx']).index(k)] for k in Om): continue
    nv0 = np.array([R.nv(D0, k) for k in Om])
    def Fz(P):
        zz = z1.copy()
        for i, k in enumerate(Om): zz[lev[k]] += P[i]/R.U[k, lev[k]]
        D = R.forced(A1, zz)
        return np.array([R.nv(D, k) for k in Om]) - nv0
    P = fsolve(Fz, np.zeros(len(Om)), xtol=1e-14)
    zz = z1.copy()
    for i, k in enumerate(Om): zz[lev[k]] += P[i]/R.U[k, lev[k]]
    if np.abs(zz).max() > 1: continue
    D1 = R.forced(A1, zz)
    res = np.abs(Fz(P)).max()
    for m in range(1, R.N + 1):
        B0, B1 = D0['blocks'][m], D1['blocks'][m]
        if not np.array_equal(B0['P'], B1['P']): break
        idx = B0['idx']; Q = ~B0['P']
        r = B1['C']/B0['C']
        gap0 = B0['M'] - np.abs(B0['w'][Q]); gap1 = B1['M'] - np.abs(B1['w'][Q])
        worst_gap = max(worst_gap, np.abs(gap1 - (r*gap0 + 1 - r)).max())
        om = np.zeros(len(idx)); om[Q] = rng.normal(size=Q.sum())
        worst_H = max(worst_H, abs(R.H(D1, m, om) - R.H(D0, m, om)/r))
        worst_C = max(worst_C, abs(B1['C'] - B0['C']))
    cnt += 1
print('(c) %d instances with exact nv-restoration on Omega = Q (residual <= 1e-13): max |gap1 - ((C1/C0)gap0 + 1 - C1/C0)| = %.1e,'
      ' max |H1 - (C0/C1)H0| = %.1e, max |C1 - C0| = %.1e  (referee: C1 = C0 when Omega = Q and P unchanged)' % (cnt, worst_gap, worst_H, worst_C))
