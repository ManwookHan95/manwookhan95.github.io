# NOTE (referee): no degenerate point was found in this toy (the (P4)-type degeneracy h^T g = 1 needs target cross terms, which the toy lacks: with private proportional thick coordinates only, h^T g = (Hilbert mass of a on them)/nu^2 < 1).  Kept as a record; output empty.
"""K2 referee: Step-A certificates at a TUNED degenerate point (Sherman-Morrison-type degeneracy of the two-sided system), data-consistent
toy of ref_sysA2.py (pattern 'U': near S_th of the data sign, far thick coordinates of the opposite sign proportional to v).  At the
degenerate point the left null vector y of the two-sided columns is computed; K2.16 predicts: of +-y only the one with gamma < 0 can be a
certificate (all one-sided c_s >= 0), and then Psi = kappa a on thick coordinates, one-sided sum = |kappa|(1 - alpha) > 0."""
import numpy as np
from scipy.optimize import brentq
exec(open('ref_sysA2.py').read().split("stats = []")[0])

def system(amp0, seed):
    global rng
    rng = np.random.default_rng(seed)
    Ko, Kp, Kf = 3, 2, 2
    K, n, S, U, Phi, mu, a, z, typ = build2(Ko, Kp, Kf, 6, 0, ['U'] * Ko)
    for s in S[0][3:]:                     # tune the far amplitude of carrier 0
        a[s] = np.sign(a[s]) * amp0 * U[0, s] / U[0, S[0][3]]
    st = row_state(a, z, mu, U, Phi, np.zeros(K, bool))
    P = st['blk']['P']
    if any(P[:Ko]) or not P[Ko:Ko + Kp].any() or any(P[Ko + Kp:]): return None
    Om = np.array([k < Ko for k in range(K)])
    st = row_state(a, z, mu, U, Phi, Om)
    tuned = list(range(Ko))
    eps = np.sign(st['val']); eps[eps == 0] = 1
    rt = np.array([eps[l] * st['val'][l] / st['kappa'] for l in tuned])
    Ft = lambda s_: np.array([eps[l] * s_['val'][l] for l in tuned]) - rt * s_['kappa']
    gens, kinds = [], []; h = 1e-7
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h * np.sign(a[s]) * qstar(a, mu)
            gens.append((Ft(row_state(a2, z, mu, U, Phi, Om)) - Ft(st)) / h); kinds.append((typ[s], s))
    G = np.array(gens).T
    two = [j for j, (kd, s) in enumerate(kinds) if kd == 'TS']
    rep = [two[3 * l] for l in range(Ko)]          # one thick column per carrier (the others are proportional)
    return np.linalg.det(G[:, rep]), (K, n, S, U, Phi, mu, a, z, typ, st, Om, tuned, eps, rt, G, kinds, two)

done = 0
for seed in range(1, 400):
    if done >= 6: break
    grid = np.linspace(0.02, 0.6, 30); vals = []
    for t in grid:
        r = system(t, seed); vals.append(None if r is None else r[0])
    root = None
    for i in range(len(grid) - 1):
        if vals[i] is not None and vals[i + 1] is not None and vals[i] * vals[i + 1] < 0:
            root = brentq(lambda t: system(t, seed)[0], grid[i], grid[i + 1], xtol=1e-13); break
    if root is None: continue
    det, (K, n, S, U, Phi, mu, a, z, typ, st, Om, tuned, eps, rt, G, kinds, two) = system(root, seed)
    y = np.linalg.svd(G[:, two].T)[2][-1]
    dk = dkappa(Phi * st['val'], Phi, Om); Kvec = (dk * Phi) @ U
    out = []
    for sg in (+1, -1):
        yy = sg * y
        zet = sum(yy[i] * rt[i] for i in range(len(tuned)))
        Ps = sum(yy[i] * eps[l] * U[l] for i, l in enumerate(tuned)) - zet * Kvec
        gam = (mu * Ps) @ st['e']; kap = gam / st['nu']
        one = [(Ps[s] - kap * st['a'][s]) * np.sign(a[s]) for s in range(n) if typ[s] == 'Sth']
        thick = max(abs(Ps[s] - kap * st['a'][s]) for s in range(n) if typ[s] == 'TS')
        alpha = 0.0
        is_cert = min(yy @ G[:, j] for j, (kd, s) in enumerate(kinds) if kd == 'Sth') >= -1e-9
        out.append((sg, gam, is_cert, min(one), sum(one), abs(kap) * (np.abs(st['a']).sum() + st['nu'] - np.abs(st['a']).sum()), thick))
    done += 1
    print(f"seed {seed}: degenerate amp0 = {root:.6f}, s_min(two-sided) = {np.linalg.svd(G[:, two], compute_uv=False)[-1]:.1e}")
    for sg, gam, is_cert, mn, sm, pred, thick in out:
        print(f"   {'+' if sg > 0 else '-'}y: gamma = {gam:+.4f}, certificate (all one-sided actions >= 0): {is_cert}, min one-sided c_s = {mn:+.2e}, "
              f"sum one-sided c_s = {sm:+.4f} vs |kappa| nu = {pred:.4f} (phi = 0, alpha = 0 => sum = -kappa(1-alpha) >= |kappa| nu), max|Psi - kappa a| at thick = {thick:.1e}")
