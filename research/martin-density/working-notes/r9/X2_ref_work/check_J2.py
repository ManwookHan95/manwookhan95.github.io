"""X2-referee check 1b: Prop J inequality with |Q| >= 2 (non-trivial Cauchy-Schwarz), and the referee's observation:
exact nv-restoration on Omega = Q (all strict non-peaks) with unchanged peak set gives C' = C exactly; with Omega a proper subset of Q,
|C' - C| is of the order of the non-Omega strict non-peaks' value changes only."""
import numpy as np, sys
sys.path.insert(0, '.')
from rmodel import Row
rng = np.random.default_rng(5)

def make(N=2, Kb=5, nF=2, nsig=5):
    K = N*Kb; n = nF + K*nsig + 6
    mu = np.array([2.0**(-0.3*s - 1) for s in range(n)])
    U = np.zeros((K, n)); blk = np.repeat(np.arange(1, N + 1), Kb)
    Phi = np.concatenate([np.sort(rng.uniform(0.02, 0.25, Kb))[::-1]*2.0**(-m) for m in range(N)])
    z = np.zeros(n); z[:nF] = 1.0
    for k in range(K):
        y = np.zeros(n); y[:nF] = rng.normal(size=nF)*rng.uniform(0.05, 1)
        S = list(range(nF + k*nsig, nF + (k + 1)*nsig)); sg = rng.choice([-1.0, 1.0])
        y[S] = rng.uniform(0.02, 0.4)*2.0**(-np.arange(nsig))*sg; z[S] = sg
        U[k] = y
    R = Row(mu, U, blk, Phi, list(range(nF)))
    R.U = np.array([u/R.qstar(u) for u in U])
    z[nF + K*nsig:] = rng.uniform(-0.9, 0.9, 6)
    A = np.zeros(n); A[:nF] = rng.uniform(0.3, 1.0, nF)
    return R, A, z, n, nF, K, nsig

ratios = []; qs = []
for trial in range(400):
    R, A, z, n, nF, K, nsig = make()
    D0 = R.forced(A, z)
    for m in range(1, R.N + 1):
        B = D0['blocks'][m]; idx = B['idx']
        Q = [i for i in range(len(idx)) if not B['P'][i]]
        if len(Q) < 2: continue
        Dom = np.zeros(len(idx)); Dom[Q] = rng.normal(size=len(Q))*rng.uniform(0.1, 5)
        cont = [j for j in range(nF, n) if abs(z[j]) == 1.0]
        J = rng.choice(cont, size=5, replace=False)
        A1 = A.copy(); A1[J] += z[J]*rng.uniform(1e-4, 1e-2, 5)
        D1 = R.forced(A1, z); B1 = D1['blocks'][m]
        if not np.array_equal(B1['P'], B['P']): continue
        dd = R.d(D1, m, Dom) - R.d(D0, m, Dom); Delta = R.d(D0, m, Dom)
        du = np.abs(D1['val'][idx][Q] - D0['val'][idx][Q]).max()
        bound = m*np.linalg.norm(R.Phi[idx]*Dom)*np.sqrt(len(Q))*du/B1['A'] + abs(Delta)*abs(B1['A'] - B['A'])/B1['A']
        ratios.append(abs(dd)/bound); qs.append(len(Q))
ratios = np.array(ratios)
print('Prop J with |Q| >= 2: %d instances, max ratio - 1 = %.2e (<= 0 predicted), median ratio %.3f, |Q| in [%d, %d]' %
      (len(ratios), ratios.max() - 1, np.median(ratios), min(qs), max(qs)))

# referee's observation: Omega = Q vs Omega proper subset
def restore(R, A, z, A1, Om, lev):
    D0 = R.forced(A, z); nv0 = np.array([R.nv(D0, k) for k in Om])
    P = np.zeros(len(Om))
    def apply(P):
        zz = z.copy()
        for i, k in enumerate(Om): zz[lev[k]] += P[i]/R.U[k, lev[k]]
        return zz
    for it in range(30):
        zz = apply(P); D = R.forced(A1, zz)
        Fv = np.array([R.nv(D, k) for k in Om]) - nv0
        if np.abs(Fv).max() < 1e-15: break
        h = 1e-8; J = np.zeros((len(Om), len(Om)))
        for i in range(len(Om)):
            e = np.zeros(len(Om)); e[i] = h
            D2 = R.forced(A1, apply(P + e)); J[:, i] = (np.array([R.nv(D2, k) for k in Om]) - nv0 - Fv)/h
        P = P - np.linalg.solve(J, Fv)
    zz = apply(P)
    return D0, R.forced(A1, zz), np.abs(Fv).max(), np.abs(zz).max()

full = []; part = []
for trial in range(200):
    R, A, z, n, nF, K, nsig = make()
    D0 = R.forced(A, z)
    Q = [k for m in range(1, R.N + 1) for i, k in enumerate(D0['blocks'][m]['idx']) if not D0['blocks'][m]['P'][i]]
    if len(Q) < 2: continue
    lev = {}
    for k in Q:
        S = [j for j in np.where(np.abs(R.U[k]) > 0)[0] if nF <= j < n - 6]; lev[k] = S[-1]
    z1 = z.copy()
    for k in Q: z1[lev[k]] *= 0.5
    D0 = R.forced(A, z1)
    Q2 = [k for m in range(1, R.N + 1) for i, k in enumerate(D0['blocks'][m]['idx']) if not D0['blocks'][m]['P'][i]]
    if sorted(Q2) != sorted(Q): continue
    cont = [j for j in range(nF, n) if abs(z1[j]) == 1.0]
    J = rng.choice(cont, size=4, replace=False)
    A1 = A.copy(); A1[J] += z1[J]*rng.uniform(1e-4, 1e-3, 4)
    for Om, store in ((Q, full), (Q[:-1], part)):
        try:
            D0_, D1, res, zmax = restore(R, A, z1, A1, Om, lev)
        except np.linalg.LinAlgError:
            continue
        if res > 1e-13 or zmax > 1: continue
        same = all(np.array_equal(D0_['blocks'][m]['P'], D1['blocks'][m]['P']) for m in range(1, R.N + 1))
        if not same: continue
        store.append(max(abs(D1['blocks'][m]['C'] - D0_['blocks'][m]['C']) for m in range(1, R.N + 1)))
print('exact nv-restoration, Omega = Q: %d instances, max |C1 - C0| = %.1e ; Omega = Q minus one carrier: %d instances, median |C1 - C0| = %.1e'
      % (len(full), max(full), len(part), np.median(part)))
