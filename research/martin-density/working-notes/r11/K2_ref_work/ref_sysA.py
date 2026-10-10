"""K2 referee: Sys-A in a finite one-block Martin-type model (route-V regime: Omega = all coarse strict non-peaks, Q minus Omega = 'fine'
carriers of tiny weight).
 (1) Lemma K2.8: Euler identity kappa = K(xhat) (a), generator actions y^T c_A(delta) = l_delta(Psi^A_y) (b), common mode (c);
     the non-peak Euler share Xt in this regime vs. a block where Q minus Omega contains a coarse carrier.
 (2) Theorem K2.16 / Corollary K2.17 consistency: generators = unit elementary moves (TS mass change and FR z-move two-sided, S_th raise
     one-sided), targets = current ratios (phi_y = 0).  Exact certificates y (G^T y >= 0 on one-sided, = 0 on two-sided) are searched by LP;
     for each certificate check gamma < 0, Psi(s) = kappa a_s at thick s, Psi = 0 at FR, c_s >= 0 at S_th, and the kind-based predictions;
     configurations satisfying K2.17 (c) or (d) must have no certificate.
"""
import numpy as np
from scipy.optimize import linprog
from model import block, qstar
rng = np.random.default_rng(7)

def kappa_fn(zeta, Phi, Om):
    b = block(zeta, Phi)
    Q = ~b['P']; out = Q & ~Om
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
        g[k] = (kappa_fn(zp, Phi, Om)[0] - kappa_fn(zm, Phi, Om)[0]) / (2 * h)
    return g

def build(Ko=4, Kp=2, Kf=2, ns=4, nT=2, types=None):
    K = Ko + Kp + Kf; n = nT + K * ns
    S = [list(range(nT + k * ns, nT + (k + 1) * ns)) for k in range(K)]
    U = np.zeros((K, n))
    for k in range(K):
        if k < Ko: U[k, :nT] = rng.uniform(-0.1, 0.1, nT); U[k, S[k]] = rng.uniform(0.5, 1) * 0.7**np.arange(ns)
        elif k < Ko + Kp: U[k, :nT] = rng.uniform(0.2, 0.5, nT); U[k, S[k]] = rng.uniform(0.3, 1) * 0.7**np.arange(ns)
        else: U[k, S[k]] = rng.uniform(0.3, 1) * 0.7**np.arange(ns)
        U[k] /= np.abs(U[k]).sum()
    Phi = np.concatenate([rng.uniform(0.35, 0.45, Ko), rng.uniform(0.15, 0.25, Kp), rng.uniform(0.004, 0.008, Kf)])
    mu = 0.3 * 0.9**np.arange(n)
    a = np.zeros(n); z = np.zeros(n); typ = ['' for _ in range(n)]
    for t in range(nT): a[t] = rng.choice([-1, 1]) * rng.uniform(0.1, 0.3); z[t] = np.sign(a[t]); typ[t] = 'TS'
    for k in range(K):
        for i, s in enumerate(S[k]):
            if k >= Ko + Kp: z[s] = 0.001 * rng.choice([-1, 1]); typ[s] = 'FR'; continue      # fine carriers: tiny values
            if k >= Ko: z[s] = 1.0; typ[s] = 'TSpk' if i == 0 else 'FRpk'
            if k >= Ko:
                if i == 0: a[s] = 0.2; z[s] = 1.0; typ[s] = 'TS'
                else: z[s] = 0.5; typ[s] = 'FR'
                continue
            t_ = types[k][i] if types is not None else rng.choice(['TS', 'Sth', 'FR'], p=[0.3, 0.5, 0.2])
            typ[s] = t_
            if t_ == 'TS': a[s] = rng.choice([-1, 1]) * rng.uniform(0.1, 0.3); z[s] = np.sign(a[s])
            elif t_ == 'Sth': sg = rng.choice([-1, 1]); a[s] = sg * 1e-4; z[s] = sg
            else: z[s] = rng.uniform(-0.5, 0.5)
    return K, n, S, U, Phi, mu, a, z, typ

worst_a = worst_b = worst_c = 0.0; Xt_route, Xt_general = [], []
ncert = 0; nconf = 0; struct_fail = 0; k217_viol = 0; nk217 = 0
for trial in range(250):
    Ko, Kp, Kf = 4, 2, 2
    K, n, S, U, Phi, mu, a, z, typ = build(Ko, Kp, Kf)
    st = row_state(a, z, mu, U, Phi, np.zeros(K, bool))
    P = st['blk']['P']
    Om = np.array([(k < Ko) and not P[k] for k in range(K)])
    if Om.sum() < 3 or any(P[k] for k in range(Ko + Kp, K)) or not P[Ko:Ko + Kp].any(): continue
    Om[[k for k in range(Ko, Ko + Kp) if not P[k]]] = True          # every coarse strict non-peak is tuned (route V)
    st = row_state(a, z, mu, U, Phi, Om)
    tuned = [k for k in range(K) if Om[k]]
    eps = np.sign(st['val']); eps[eps == 0] = 1
    rt = np.array([eps[l] * st['val'][l] / st['kappa'] for l in tuned])     # targets = current ratios
    Ft = lambda s_: np.array([eps[l] * s_['val'][l] for l in tuned]) - rt * s_['kappa']
    zeta = Phi * st['val']
    dk = dkappa(zeta, Phi, Om)
    Kvec = (dk * Phi) @ U
    worst_a = max(worst_a, abs(Kvec @ st['zhat'] - st['kappa']) / st['kappa'])
    Xt = sum(rt[i] * eps[l] * Phi[l] * dk[l] for i, l in enumerate(tuned)); Xt_route.append(abs(Xt))
    # general block: also leave one coarse strict non-peak out of Omega
    if len(tuned) >= 2:
        Om2 = Om.copy(); Om2[tuned[0]] = False
        dk2 = dkappa(zeta, Phi, Om2); kap2 = kappa_fn(zeta, Phi, Om2)[0]
        rt2 = [eps[l] * st['val'][l] / kap2 for l in tuned[1:]]
        Xt_general.append(abs(sum(rt2[i] * eps[l] * Phi[l] * dk2[l] for i, l in enumerate(tuned[1:]))))
    # generator columns (unit moves) and K2.8(b)
    gens, kinds = [], []
    h = 1e-7
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h * np.sign(a[s]) * qstar(a, mu)     # raise direction (normalized units, dm = h)
            col = (Ft(row_state(a2, z, mu, U, Phi, Om)) - Ft(st)) / h
            gens.append(col); kinds.append((typ[s], s))
        elif typ[s] == 'FR':
            z2 = z.copy(); z2[s] += h
            col = (Ft(row_state(a, z2, mu, U, Phi, Om)) - Ft(st)) / h
            gens.append(col); kinds.append(('FR', s))
    G = np.array(gens).T
    y = rng.normal(size=len(tuned)); y /= np.linalg.norm(y)
    zet = np.zeros(1); zet = sum(y[i] * rt[i] for i in range(len(tuned)))
    Psi = sum(y[i] * eps[l] * U[l] for i, l in enumerate(tuned)) - zet * Kvec
    gam = (mu * Psi) @ st['e']; kap = gam / st['nu']
    worst_c = max(worst_c, abs(Psi @ st['zhat'] - y @ Ft(st)))
    for j, (kd, s) in enumerate(kinds):
        pred = (mu[s]**2 / st['nu']) * (Psi[s] - kap * st['a'][s]) * np.sign(a[s]) if kd in ('TS', 'Sth') else Psi[s]
        worst_b = max(worst_b, abs(y @ G[:, j] - pred) / (abs(pred) + 1e-6))
    # exact certificates by LP: two-sided columns -> equality, one-sided (Sth raises) -> y^T g >= 0
    two = [j for j, (kd, s) in enumerate(kinds) if kd in ('TS', 'FR')]
    one = [j for j, (kd, s) in enumerate(kinds) if kd == 'Sth']
    nconf += 1
    has_cert = False
    for i in range(len(tuned)):
        for sg in (+1, -1):
            c = np.zeros(len(tuned)); c[i] = -sg
            res = linprog(c, A_ub=-G[:, one].T if one else None, b_ub=np.zeros(len(one)) if one else None,
                          A_eq=G[:, two].T if two else None, b_eq=np.zeros(len(two)) if two else None, bounds=[(-1, 1)] * len(tuned), method='highs')
            if res.status == 0 and -res.fun > 1e-7:
                has_cert = True; yc = res.x / np.linalg.norm(res.x)
                zc = sum(yc[ii] * rt[ii] for ii in range(len(tuned)))
                Pc = sum(yc[ii] * eps[l] * U[l] for ii, l in enumerate(tuned)) - zc * Kvec
                gc = (mu * Pc) @ st['e']; kc = gc / st['nu']
                thick_err = max([abs(Pc[s] - kc * st['a'][s]) for s in range(n) if typ[s] == 'TS'] + [0])
                fr_err = max([abs(Pc[s]) for s in range(n) if typ[s] == 'FR'] + [0])
                one_min = min([(Pc[s] - kc * st['a'][s]) * np.sign(a[s]) for s in range(n) if typ[s] == 'Sth'] + [0])
                ok = gc < -1e-6 and thick_err < 1e-5 and fr_err < 1e-5 and one_min > -1e-6
                if not ok:
                    struct_fail += 1
                    print("  structure check failed:", gc, thick_err, fr_err, one_min)
                break
        if has_cert: break
    ncert += has_cert
    # K2.17 (c)/(d): a tuned carrier with private TS and private FR, or private TS and private Sth of the same sign (v > 0 here)
    cond = False
    for l in tuned:
        if l >= Ko: continue
        tl = [typ[s] for s in S[l]]; sg_ts = [np.sign(a[s]) for s in S[l] if typ[s] == 'TS']; sg_st = [np.sign(a[s]) for s in S[l] if typ[s] == 'Sth']
        if 'TS' in tl and 'FR' in tl: cond = True
        if any(x in sg_st for x in sg_ts): cond = True
    if cond:
        nk217 += 1
        if has_cert: k217_viol += 1
print(f"K2.8(a) Euler: max |K(xhat) - kappa|/kappa = {worst_a:.1e};  (c) |Psi(xhat) - y^T Ft| = {worst_c:.1e};  (b) generator actions rel err = {worst_b:.1e}")
print(f"non-peak Euler share |Xt|: route-V regime (Q minus Omega fine) max = {max(Xt_route):.2e};  one coarse non-peak left out of Omega: max = {max(Xt_general):.2e}")
print(f"configurations: {nconf}; with an exact certificate: {ncert}; certificates violating K2.16 structure (gamma<0, Psi=kappa a at TS, Psi=0 at FR, c>=0 at S_th): {struct_fail}")
print(f"configurations satisfying K2.17(c) or (d): {nk217}; of these with a certificate (should be 0): {k217_viol}")
