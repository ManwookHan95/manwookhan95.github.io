"""K2 referee: Theorem K2.16 structure on configurations that DO carry Step-A certificates.  Tuned carriers get private coordinate
patterns 'U' (all S_th: one-sided raises only), 'S' (all thick with a_s proportional to v_l(s): tiny spread, (P4)-type) or 'M' (thick
proportional + S_th).  For every exact certificate found by LP: gamma = <U*Psi,e> must be < 0 robustly; Psi(s) = kappa a_s at every thick s,
c_s(Psi) >= 0 at S_th coordinates, and the S_th sum of c_s equals |kappa|(1 - alpha) (identity with phi_y = 0)."""
import numpy as np
from scipy.optimize import linprog
exec(open('ref_sysA.py').read().split("worst_a = worst_b")[0])

def build2(Ko, Kp, Kf, ns, nT, pat):
    """Data-consistent toy: an Omega carrier with data sign c has near S_th coordinates of sign c (one-sided raises) and far THICK
    coordinates (two-sided) proportional to v; pattern 'U': far thick of sign -c (cancellation); 'D': far thick of sign +c
    (K2.17(d): no certificate); 'F': like 'U' plus one private FR coordinate (K2.17(c): no certificate)."""
    K = Ko + Kp + Kf
    sizes = [6] * Ko + [4] * (Kp + Kf)
    starts = np.cumsum([0] + sizes)
    n = starts[-1]
    S = [list(range(starts[k], starts[k + 1])) for k in range(K)]
    U = np.zeros((K, n)); a = np.zeros(n); z = np.zeros(n); typ = ['none'] * n
    for k in range(K):
        if k < Ko: U[k, S[k]] = rng.uniform(0.5, 1) * 0.93**np.arange(6)
        else: U[k, S[k]] = rng.uniform(0.3, 1) * 0.7**np.arange(4)
        U[k] /= np.abs(U[k]).sum()
    Phi = np.concatenate([rng.uniform(0.35, 0.45, Ko), rng.uniform(0.2, 0.3, Kp), rng.uniform(0.004, 0.008, Kf)])
    mu = 0.3 * 0.93**np.arange(n)
    for k in range(Ko):
        c = rng.choice([-1, 1]); amp = rng.uniform(0.15, 0.3)
        sfar = -c if pat[k] in ('U', 'F') else c
        for i, s in enumerate(S[k]):
            if i < 3:
                a[s] = c * 1e-4; z[s] = c; typ[s] = 'Sth'
            elif pat[k] == 'F' and i == 5:
                z[s] = 0.2; typ[s] = 'FR'
            else:
                a[s] = sfar * amp * U[k, s] / U[k, S[k][3]]; z[s] = np.sign(a[s]); typ[s] = 'TS'
    for k in range(Ko, Ko + Kp):
        for i, s in enumerate(S[k]):
            a[s] = 0.25 if i == 0 else 1e-4; z[s] = 1.0; typ[s] = 'TSpk_off' if i == 0 else 'Sth'
    for k in range(Ko + Kp, K):
        for s in S[k]: z[s] = 0.001 * rng.choice([-1, 1])
    return K, n, S, U, Phi, mu, a, z, typ

stats = []
for trial in range(400):
    Ko, Kp, Kf = 4, 2, 2
    pat = rng.choice(['U', 'U', 'U', 'D', 'F'], Ko)
    K, n, S, U, Phi, mu, a, z, typ = build2(Ko, Kp, Kf, 4, 0, pat)
    st = row_state(a, z, mu, U, Phi, np.zeros(K, bool))
    P = st['blk']['P']
    if any(P[k] for k in range(Ko + Kp, K)) or not P[Ko:Ko + Kp].any(): continue
    Om = np.array([not P[k] and k < Ko + Kp for k in range(K)])
    if Om.sum() < 2: continue
    st = row_state(a, z, mu, U, Phi, Om)
    tuned = [k for k in range(K) if Om[k]]
    eps = np.sign(st['val']); eps[eps == 0] = 1
    rt = np.array([eps[l] * st['val'][l] / st['kappa'] for l in tuned])
    Ft = lambda s_: np.array([eps[l] * s_['val'][l] for l in tuned]) - rt * s_['kappa']
    dk = dkappa(Phi * st['val'], Phi, Om); Kvec = (dk * Phi) @ U
    gens, kinds = [], []; h = 1e-7
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h * np.sign(a[s]) * qstar(a, mu)
            gens.append((Ft(row_state(a2, z, mu, U, Phi, Om)) - Ft(st)) / h); kinds.append((typ[s], s))
        elif typ[s] == 'FR':
            z2 = z.copy(); z2[s] += h
            gens.append((Ft(row_state(a, z2, mu, U, Phi, Om)) - Ft(st)) / h); kinds.append(('FR', s))
    G = np.array(gens).T
    two = [j for j, (kd, s) in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, (kd, s) in enumerate(kinds) if kd == 'Sth']
    found = None
    for i in range(len(tuned)):
        for sg in (+1, -1):
            c = np.zeros(len(tuned)); c[i] = -sg
            res = linprog(c, A_ub=-G[:, one].T if one else None, b_ub=np.zeros(len(one)) if one else None,
                          A_eq=G[:, two].T if two else None, b_eq=np.zeros(len(two)) if two else None, bounds=[(-1, 1)] * len(tuned), method='highs')
            if res.status == 0 and -res.fun > 1e-6: found = res.x / np.linalg.norm(res.x); break
        if found is not None: break
    if found is None: stats.append((''.join(pat), None)); continue
    yc = found
    zc = sum(yc[ii] * rt[ii] for ii in range(len(tuned)))
    Pc = sum(yc[ii] * eps[l] * U[l] for ii, l in enumerate(tuned)) - zc * Kvec
    gc = (mu * Pc) @ st['e']; kc = gc / st['nu']
    thick_err = max([abs(Pc[s] - kc * st['a'][s]) for s in range(n) if typ[s] == 'TS'] + [0])
    cs_one = [(Pc[s] - kc * st['a'][s]) * np.sign(a[s]) for s in range(n) if typ[s] == 'Sth']
    alpha = 0.0
    stats.append((''.join(pat), (gc, thick_err, min(cs_one + [0]), sum(cs_one), -kc * (st['a'] != 0).sum() * 0 + abs(kc) * 1.0)))
withc = [s for s in stats if s[1] is not None]
print(f"configurations: {len(stats)}; with exact certificates: {len(withc)}")
bad = [s for s in withc if not (s[1][0] < 0 and s[1][1] < 1e-5 and s[1][2] > -1e-6)]
print(f"certificates violating gamma<0 / Psi=kappa a at thick / c_s>=0 at S_th: {len(bad)}")
if withc:
    print("max gamma over certificates:", max(s[1][0] for s in withc), " min |gamma|:", min(abs(s[1][0]) for s in withc))
    print("patterns with certificates:", sorted(set(s[0] for s in withc)))
    print("patterns without certificates:", sorted(set(s[0] for s in stats if s[1] is None)))
    for s in withc[:8]:
        print("  pattern", s[0], " gamma = %.3e, max|Psi - kappa a| at thick = %.1e, min c_s at S_th = %.2e, sum c_s at S_th = %.3e" % s[1][:4])
