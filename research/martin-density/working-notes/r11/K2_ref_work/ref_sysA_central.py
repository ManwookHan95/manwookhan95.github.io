"""K2.8(b) with central differences (step 1e-6): y^T c_A(delta) = l_delta(Psi^A_y)."""
import numpy as np
exec(open('ref_sysA.py').read().split("worst_a = worst_b")[0])
worst = 0.0; cnt = 0
for trial in range(120):
    Ko, Kp, Kf = 4, 2, 2
    K, n, S, U, Phi, mu, a, z, typ = build(Ko, Kp, Kf)
    st = row_state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']
    Om = np.array([(k < Ko + Kp) and not P[k] for k in range(K)])
    if Om.sum() < 2 or any(P[Ko + Kp:]) or not P[:Ko + Kp].any(): continue
    st = row_state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
    eps = np.sign(st['val']); eps[eps == 0] = 1
    rt = rng.normal(size=len(tuned)) * 0.5                       # arbitrary targets: (b) holds for every rt
    Ft = lambda s_: np.array([eps[l] * s_['val'][l] for l in tuned]) - rt * s_['kappa']
    dk = dkappa(Phi * st['val'], Phi, Om, h=1e-8); Kvec = (dk * Phi) @ U
    y = rng.normal(size=len(tuned)); y /= np.linalg.norm(y)
    Psi = sum(y[i] * eps[l] * U[l] for i, l in enumerate(tuned)) - (y @ rt) * Kvec
    gam = (mu * Psi) @ st['e']; kap = gam / st['nu']
    h = 1e-6
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            ap = a.copy(); am = a.copy(); d = h * np.sign(a[s]) * qstar(a, mu); ap[s] += d; am[s] -= d
            col = (Ft(row_state(ap, z, mu, U, Phi, Om)) - Ft(row_state(am, z, mu, U, Phi, Om))) / (2 * h)
            pred = (mu[s]**2 / st['nu']) * (Psi[s] - kap * st['a'][s]) * np.sign(a[s])
        elif typ[s] == 'FR':
            zp = z.copy(); zm = z.copy(); zp[s] += h; zm[s] -= h
            col = (Ft(row_state(a, zp, mu, U, Phi, Om)) - Ft(row_state(a, zm, mu, U, Phi, Om))) / (2 * h)
            pred = Psi[s]
        else: continue
        worst = max(worst, abs(y @ col - pred) / (abs(pred) + 1e-4 * mu[s]**2)); cnt += 1
print(f"K2.8(b) central differences: {cnt} moves, max rel err = {worst:.1e}")
