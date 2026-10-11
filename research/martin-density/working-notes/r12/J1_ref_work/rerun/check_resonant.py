"""J1: exactly resonant one-block configuration carrying an exact Step-A certificate (targets = current ratios).
K0 = two anti-aligned thick-type carriers: 3 holes (S_th, data sign c_k, bank mass th0) + 3 thick coordinates of sign -c_k proportional
to v_k (a = rho_k v_k).  A robust peak with a private FR coordinate (two-sided peak resource) and no support; base support = K0 only.
A scalar t (hole profile scale) is tuned by brentq so that Phi0(zhat) = sum rho_k u_k(zhat) = 0 (one-sided hole mass = 1, J1.3(c)).
Checks: (1) exact certificate exists (LP); (2) every certificate: kappa_Psi < 0, coef_k sign = -sgn(a_p v_k(p)) (J1.6(a)), y ~ eps*rho on K0;
(3) far placement (pull) at a far data-sign contact of a K0 carrier lowers y^T Ft for every certificate (J1.7), predicted coef v (tau - z);
(4) away from resonance (t perturbed) the LP finds no exact certificate (near-certificates only)."""
import numpy as np
from scipy.optimize import linprog, brentq
from model import block, qstar
rng = np.random.default_rng(5)
def kappa_fn(zeta, Phi, Om):
    b = block(zeta, Phi); Q = ~b['P']; out = Q & ~Om
    S = (b['nu'][out]**2*Phi[out]**2).sum()
    return b['A'] + b['theta']*(Phi[b['P']]**2).sum() + S/b['theta'], b
def state(a_un, z, mu, U, Phi, Om):
    a = a_un/qstar(a_un, mu); nu = np.linalg.norm(mu*a); e = mu*a/nu; zh = z + mu*e; val = U @ zh
    kap, b = kappa_fn(Phi*val, Phi, Om); return dict(a=a, nu=nu, e=e, zh=zh, val=val, kappa=kap, blk=b)
def dkappa(zeta, Phi, Om, h=1e-7):
    g = np.zeros(len(zeta))
    for k in range(len(zeta)):
        zp = zeta.copy(); zm = zeta.copy(); zp[k] += h; zm[k] -= h
        g[k] = (kappa_fn(zp, Phi, Om)[0] - kappa_fn(zm, Phi, Om)[0])/(2*h)
    return g
def build(t, seed):
    r = np.random.default_rng(seed)
    K = 4   # 0,1: K0 ; 2: robust peak ; 3: strict non-peak with private FR (privately tunable)
    lay = {0: (3, 3, 2), 1: (3, 3, 2), 2: (0, 0, 3), 3: (0, 0, 3)}     # (holes, thick, FR-or-far)
    idx = 0; S = {}
    for k in range(K):
        h_, th_, f_ = lay[k]; S[k] = dict(hole=list(range(idx, idx+h_)), thick=list(range(idx+h_, idx+h_+th_)),
                                          other=list(range(idx+h_+th_, idx+h_+th_+f_))); idx += h_+th_+f_
    n = idx; U = np.zeros((K, n)); a = np.zeros(n); z = np.zeros(n); typ = ['']*n
    c = {0: 1, 1: -1}; rho = {0: -0.9, 1: 1.1}            # anti-aligned: sign(rho_k) = -c_k
    for k in (0, 1):
        U[k, S[k]['hole']] = t*r.uniform(0.6, 1, 3)
        U[k, S[k]['thick']] = r.uniform(0.3, 0.6, 3)
        U[k, S[k]['other']] = 1e-3*r.uniform(0.5, 1, 2)                    # far coordinates (v ~ 1e-3)
        for s in S[k]['hole']: a[s] = c[k]*1e-5; z[s] = c[k]; typ[s] = 'Sth'
        for s in S[k]['thick']: a[s] = rho[k]*U[k, s]; z[s] = np.sign(a[s]); typ[s] = 'TS'
        for s in S[k]['other']: z[s] = c[k]; typ[s] = 'far'                # far data-sign contacts (pullable)
    U[2, S[2]['other']] = [0.5, 0.3, 0.2]; z[S[2]['other']] = [1.0, 1.0, 0.3]; typ[S[2]['other'][2]] = 'FR'
    for s in S[2]['other'][:2]: typ[s] = 'none'
    U[3, S[3]['other']] = [0.2, 0.15, 0.1]; z[S[3]['other']] = [0.1, -0.2, 0.3]
    for s in S[3]['other']: typ[s] = 'FR'
    Phi = np.array([0.4, 0.38, 0.3, 0.42])
    mu = 0.3*0.9**np.arange(n)
    for k in (0, 1):
        for s in S[k]['other']: mu[s] = 1e-7
    return K, n, S, U, a, z, typ, Phi, mu, c, rho
def analyse(t, seed, do_jump=True):
    K, n, S, U, a, z, typ, Phi, mu, c, rho = build(t, seed)
    st = state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']
    if not P[2] or P[0] or P[1] or P[3]: return None
    Om = ~P; st = state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
    eps = np.array([c.get(k, np.sign(st['val'][k]) or 1) for k in range(K)], float)
    rt = np.array([eps[l]*st['val'][l]/st['kappa'] for l in tuned])
    Ft = lambda s_: np.array([eps[l]*s_['val'][l] for l in tuned]) - rt*s_['kappa']
    zeta = Phi*st['val']; dk = dkappa(zeta, Phi, Om)
    gens, kinds = [], []; h = 1e-8
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h*np.sign(a[s])
            gens.append((Ft(state(a2, z, mu, U, Phi, Om)) - Ft(st))/h); kinds.append(typ[s])
        elif typ[s] == 'FR':
            z2 = z.copy(); z2[s] += h; gens.append((Ft(state(a, z2, mu, U, Phi, Om)) - Ft(st))/h); kinds.append('FR')
    G = np.array(gens).T; two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
    sc = np.abs(G).max(axis=0); Gn = G/sc
    certs = []
    for rep in range(10):
        cobj = rng.normal(size=len(tuned))
        res = linprog(cobj, A_ub=-Gn[:, one].T, b_ub=np.zeros(len(one)) + 1e-10, A_eq=Gn[:, two].T, b_eq=np.zeros(len(two)),
                      bounds=[(-1, 1)]*len(tuned), method='highs')
        if res.status == 0 and np.linalg.norm(res.x) > 1e-6: certs.append(res.x/np.linalg.norm(res.x))
    out = dict(ncert=len(certs), kneg=0, signok=0, jumpok=0, jumps=0, minsv=np.linalg.svd(Gn[:, two], compute_uv=False).min())
    for yc in certs:
        zc = sum(yc[i]*rt[i] for i in range(len(tuned)))
        coef = np.zeros(K)
        for i, l in enumerate(tuned): coef[l] += yc[i]*eps[l]
        coef -= zc*dk*Phi
        Pc = coef @ U; kc = (mu*Pc) @ st['e']/st['nu']
        out['kneg'] += kc < 0
        ok = all(np.sign(coef[k]) == -np.sign(a[S[k]['thick'][0]]*U[k, S[k]['thick'][0]]) for k in (0, 1))
        out['signok'] += ok
        if do_jump:
            for k in (0, 1):
                j = S[k]['other'][0]; p = S[k]['thick'][0]; tau = np.sign(a[p]*U[k, p]*U[k, j])
                z2 = z.copy(); z2[j] = tau; a2 = a.copy(); a2[j] = tau*1e-6          # pull: tiny anti-sign support
                dF = Ft(state(a2, z2, mu, U, Phi, Om)) - Ft(st); pred = coef[k]*U[k, j]*(tau - z[j])
                out['jumps'] += 1; out['jumpok'] += (yc @ dF < 0) and abs(yc @ dF - pred) <= 2e-2*abs(pred)
    return out
for seed in range(6):
    def phi0(t):
        K, n, S, U, a, z, typ, Phi, mu, c, rho = build(t, seed)
        st = state(a, z, mu, U, Phi, np.zeros(K, bool))
        a_n = st['a']; q = qstar(a, mu)
        return sum(rho[k]/q*U[k] @ st['zh'] for k in (0, 1))
    try: t0 = brentq(phi0, 0.05, 20.0, xtol=1e-14)
    except ValueError: print(seed, 'no root'); continue
    res = analyse(t0, seed); res_off = analyse(t0*1.05, seed, do_jump=False)
    print(f"seed {seed}: t0={t0:.4f} Phi0(zhat)={phi0(t0):.1e} | resonant: {res} | off-resonance (t*1.05): certs={None if res_off is None else res_off['ncert']}")
