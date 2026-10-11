"""J1 check of Lemma J1.6(a) / Theorem J1.7 in the K2-referee finite one-block model (diagonal base, threshold equation):
exact certificates (y^T g = 0 on two-sided generators, y^T g >= 0 on one-sided ones) are sampled by LP with random objectives;
for every certificate: kappa_Psi < 0, and for every thick-type carrier k (a TS coordinate in S_k) coef_k has the sign -sgn(a_p v_k(p)).
Then a 'helpful far placement' (z_j -> tau at an extra far coordinate j of a thick-type carrier) changes y^T Ft by
coef_k v_k(j) (tau - z_j) < 0 for EVERY certificate (checked against finite differences of Ft)."""
import numpy as np
from scipy.optimize import linprog
from model import block, qstar
rng = np.random.default_rng(2026)
def kappa_fn(zeta, Phi, Om):
    b = block(zeta, Phi); Q = ~b['P']; out = Q & ~Om
    S = (b['nu'][out]**2 * Phi[out]**2).sum()
    return b['A'] + b['theta'] * (Phi[b['P']]**2).sum() + S / b['theta'], b
def row_state(a_un, z, mu, U, Phi, Om):
    a = a_un / qstar(a_un, mu); nu = np.linalg.norm(mu * a); e = mu * a / nu
    zhat = z + mu * e; val = U @ zhat
    kap, b = kappa_fn(Phi * val, Phi, Om)
    return dict(a=a, nu=nu, e=e, zhat=zhat, val=val, kappa=kap, blk=b)
def dkappa(zeta, Phi, Om, h=1e-7):
    g = np.zeros(len(zeta))
    for k in range(len(zeta)):
        zp = zeta.copy(); zm = zeta.copy(); zp[k] += h; zm[k] -= h
        g[k] = (kappa_fn(zp, Phi, Om)[0] - kappa_fn(zm, Phi, Om)[0]) / (2*h)
    return g
stats = dict(conf=0, cert=0, kappa_neg_fail=0, sign_fail=0, jump_fail=0, jump_tests=0)
for trial in range(400):
    Ko, Kp = 4, 2; K = Ko + Kp; ns = 5; nT = 2; nf = 2          # ns design-depth signature coords + nf far coords per carrier
    n = nT + K*(ns + nf)
    S = [list(range(nT + k*(ns+nf), nT + k*(ns+nf) + ns)) for k in range(K)]
    Sf = [list(range(nT + k*(ns+nf) + ns, nT + (k+1)*(ns+nf))) for k in range(K)]
    U = np.zeros((K, n))
    for k in range(K):
        U[k, :nT] = rng.uniform(-0.3, 0.3, nT) if k < Ko else rng.uniform(0.2, 0.5, nT)
        U[k, S[k]] = rng.uniform(0.4, 1)*0.7**np.arange(ns)*rng.choice([-1,1])
        U[k, Sf[k]] = 1e-3*rng.uniform(0.5, 1, nf)*np.sign(U[k, S[k][0]])
        U[k] /= np.abs(U[k]).sum()
    Phi = np.concatenate([rng.uniform(0.35, 0.45, Ko), rng.uniform(0.15, 0.25, Kp)])
    mu = 0.3*0.9**np.arange(n); mu[[j for k in range(K) for j in Sf[k]]] = 1e-6   # far coords: negligible base efficiency
    a = np.zeros(n); z = np.zeros(n); typ = ['']*n
    for t in range(nT): a[t] = rng.choice([-1,1])*rng.uniform(0.1, 0.3); z[t] = np.sign(a[t]); typ[t] = 'TS'
    for k in range(K):
        for i, s in enumerate(S[k]):
            if k >= Ko:
                if i == 0: a[s] = 0.2*np.sign(U[k, s]); z[s] = np.sign(a[s]); typ[s] = 'TS'
                else: z[s] = 0.5; typ[s] = 'FR'
                continue
            t_ = rng.choice(['TS', 'Sth', 'FR'], p=[0.45, 0.45, 0.10])
            typ[s] = t_
            if t_ == 'TS': a[s] = rng.choice([-1,1])*rng.uniform(0.1, 0.3); z[s] = np.sign(a[s])
            elif t_ == 'Sth': sg = rng.choice([-1,1]); a[s] = sg*1e-4; z[s] = sg
            else: z[s] = rng.uniform(-0.5, 0.5)
        for j in Sf[k]: z[j] = rng.choice([-1, 1]); typ[j] = 'far'
    st = row_state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']
    Om = np.array([(k < Ko) and not P[k] for k in range(K)])
    if Om.sum() < 2 or not P[Ko:].any(): continue
    Om[[k for k in range(Ko, K) if not P[k]]] = True
    st = row_state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
    eps = np.sign(st['val']); eps[eps == 0] = 1
    rt = np.array([eps[l]*st['val'][l]/st['kappa'] for l in tuned])
    Ft = lambda s_: np.array([eps[l]*s_['val'][l] for l in tuned]) - rt*s_['kappa']
    zeta = Phi*st['val']; dk = dkappa(zeta, Phi, Om); Kvec = (dk*Phi) @ U
    gens, kinds = [], []; h = 1e-7
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h*np.sign(a[s])*qstar(a, mu)
            gens.append((Ft(row_state(a2, z, mu, U, Phi, Om)) - Ft(st))/h); kinds.append((typ[s], s))
        elif typ[s] == 'FR':
            z2 = z.copy(); z2[s] += h
            gens.append((Ft(row_state(a, z2, mu, U, Phi, Om)) - Ft(st))/h); kinds.append(('FR', s))
    G = np.array(gens).T
    two = [j for j, (kd, s) in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, (kd, s) in enumerate(kinds) if kd == 'Sth']
    stats['conf'] += 1
    thick_type = [k for k in tuned if any(typ[s] == 'TS' for s in S[k])]
    certs = []
    for rep in range(12):
        c = rng.normal(size=len(tuned))
        res = linprog(c, A_ub=-G[:, one].T if one else None, b_ub=np.zeros(len(one)) if one else None,
                      A_eq=G[:, two].T if two else None, b_eq=np.zeros(len(two)) if two else None, bounds=[(-1, 1)]*len(tuned), method='highs')
        if res.status == 0 and np.linalg.norm(res.x) > 1e-6: certs.append(res.x/np.linalg.norm(res.x))
    if not certs: continue
    stats['cert'] += 1
    for yc in certs:
        zc = sum(yc[i]*rt[i] for i in range(len(tuned)))
        coef = np.zeros(K)
        for i, l in enumerate(tuned): coef[l] += yc[i]*eps[l]
        coef -= zc*dk*Phi
        Pc = coef @ U; kc = (mu*Pc) @ st['e']/st['nu']
        if kc >= -1e-8: stats['kappa_neg_fail'] += 1
        for k in thick_type:
            p = [s for s in S[k] if typ[s] == 'TS'][0]
            if abs(coef[k]) > 1e-6 and np.sign(coef[k]) != -np.sign(a[p]*U[k, p]): stats['sign_fail'] += 1
            # helpful far placement at j in Sf[k]
            for j in Sf[k]:
                tau = np.sign(a[p]*U[k, p]*U[k, j])
                if z[j] == tau: continue
                z2 = z.copy(); z2[j] = tau
                dF = Ft(row_state(a, z2, mu, U, Phi, Om)) - Ft(st)
                pred = coef[k]*U[k, j]*(tau - z[j])
                stats['jump_tests'] += 1
                if not (yc @ dF < 0 and abs(yc @ dF - pred) <= 1e-3*abs(pred) + 1e-9): stats['jump_fail'] += 1
print(stats)
