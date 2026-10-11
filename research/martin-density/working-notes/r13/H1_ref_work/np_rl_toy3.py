"""H1-ref numerics: Lemma NP(b) and Theorem RL in a CONSISTENT one-block toy where the peak is THICK-TYPE and has NO private
two-sided peak resource (variant C of J1-ref's toy).
Carriers: 0, 1 thick-type tuned (3 S_th holes of data sign c_k, 3 TS thick coords a = rho_k v_k); 2 = robust PEAK c whose value is
dominated by 3 'deep' contacts (no generator) and which has 3 private TS coordinates with a = rho_c v_c (aligned: sgn rho_c = vs_c,
anti-aligned: opposite); 3 = privately tunable strict non-peak (3 FR coordinates).
Steps: (1) tune the hole scale t so that a (near-)certificate exists (min over t of the smallest singular value of the two-sided
columns, consistent generators at rc); (2) for the near-certificate y: zeta(y; rc), its predicted value -kappa_y rho_c vs_c/(Phi_c (1-X))
(Lemma NP(b): sign sgn(rho_c vs_c), robust); signed peak derivative; (3) obstruction: targets displaced along y (phi_y > 0);
(4) whole-block rescaling rt -> (1 + sig*delta) rt, delta = 4 phi_y/(kappa |zeta(y; rt)|): min ||t||_inf of the consistent LP for
sig = sigma_m (predicted relief) and sig = -sigma_m (predicted no relief)."""
import sys, os
import numpy as np
from scipy.optimize import linprog, minimize_scalar
base = '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r12/J1_ref_work/rerun'
sys.path.insert(0, base); cwd = os.getcwd(); os.chdir(base)
exec(open('check_resonant.py').read().split("def build(t, seed):")[0])
os.chdir(cwd)

def build_C(t, seed, align):
    r = np.random.default_rng(seed)
    K = 4
    lay = {0: (3, 3, 0), 1: (3, 3, 0), 2: (3, 3, 0), 3: (0, 0, 3)}   # carrier 2: (deep, TS, -) ; others (holes, thick, FR)
    idx = 0; S = {}
    for k in range(K):
        h_, th_, f_ = lay[k]
        S[k] = dict(hole=list(range(idx, idx+h_)), thick=list(range(idx+h_, idx+h_+th_)), other=list(range(idx+h_+th_, idx+h_+th_+f_)))
        idx += h_+th_+f_
    n = idx; U = np.zeros((K, n)); a = np.zeros(n); z = np.zeros(n); typ = ['']*n
    c = {0: 1, 1: -1}; rho = {0: -0.9, 1: 1.1}
    for k in (0, 1):
        U[k, S[k]['hole']] = t*r.uniform(0.6, 1, 3)
        U[k, S[k]['thick']] = r.uniform(0.3, 0.6, 3)
        for s in S[k]['hole']: a[s] = c[k]*1e-8; z[s] = c[k]; typ[s] = 'Sth'
        for s in S[k]['thick']: a[s] = rho[k]*U[k, s]; z[s] = np.sign(a[s]); typ[s] = 'TS'
    # peak: deep contacts (value sign +1), private TS coordinates
    U[2, S[2]['hole']] = 3.0*r.uniform(0.5, 0.8, 3); z[S[2]['hole']] = 1.0
    for s in S[2]['hole']: typ[s] = 'none'
    rc_ = 0.1 if align else -0.1
    U[2, S[2]['thick']] = r.uniform(0.1, 0.2, 3)
    for s in S[2]['thick']: a[s] = rc_*U[2, s]; z[s] = np.sign(a[s]); typ[s] = 'TS'
    rho[2] = rc_
    U[3, S[3]['other']] = [0.2, 0.15, 0.1]; z[S[3]['other']] = [0.1, -0.2, 0.3]
    for s in S[3]['other']: typ[s] = 'FR'
    Phi = np.array([1.0, 0.95, 0.8, 0.42])
    mu = 0.3*0.9**np.arange(n)
    return K, n, S, U, a, z, typ, Phi, mu, c, rho

def minmove(G, rhs, one):
    nr, nc = G.shape
    cobj = np.zeros(nc + 1); cobj[-1] = 1
    A_eq = np.hstack([G, np.zeros((nr, 1))])
    A_ub = []; b_ub = []
    for j in range(nc):
        e = np.zeros(nc + 1); e[j] = 1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
        e = np.zeros(nc + 1); e[j] = -1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
    bounds = [(0, None) if j in one else (None, None) for j in range(nc)] + [(0, None)]
    res = linprog(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=rhs, bounds=bounds, method='highs')
    return res.fun if res.status == 0 else np.inf

def setup(t, seed, align):
    K, n, S, U, a, z, typ, Phi, mu, c, rho = build_C(t, seed, align)
    st0 = state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st0['blk']['P']
    Om = ~P; st = state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
    eps = np.array([c.get(k, np.sign(st['val'][k]) or 1) for k in range(K)], float)
    rc = np.array([eps[l]*st['val'][l]/st['kappa'] for l in tuned])
    def system(rt):
        def Ft_of(s_): return np.array([eps[l]*s_['val'][l] for l in tuned]) - rt*s_['kappa']
        F0 = Ft_of(st); gens, kinds = [], []; h = 1e-9
        for s in range(n):
            if typ[s] in ('TS', 'Sth'):
                a2 = a.copy(); a2[s] += h*np.sign(a[s]); gens.append((Ft_of(state(a2, z, mu, U, Phi, Om)) - F0)/h); kinds.append(typ[s])
            elif typ[s] == 'FR':
                z2 = z.copy(); z2[s] += h; gens.append((Ft_of(state(a, z2, mu, U, Phi, Om)) - F0)/h); kinds.append('FR')
        return F0, np.array(gens).T, kinds
    return dict(K=K, n=n, S=S, U=U, a=a, z=z, typ=typ, Phi=Phi, mu=mu, c=c, rho=rho, P=P, Om=Om, st=st, tuned=tuned, eps=eps, rc=rc,
                system=system)

def svmin(t, seed, align):
    d = setup(t, seed, align)
    if list(np.where(d['P'])[0]) != [2]: return 10.0
    F0, G0, kinds = d['system'](d['rc'])
    sc = np.abs(G0).max(axis=0); two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]
    return np.linalg.svd((G0/sc)[:, two], compute_uv=False)[-1]

for align in (True, False):
    for seed in range(1, 6):
        def gres(t):
            d = setup(t, seed, align)
            st = d['st']; Phi = d['Phi']; Om = d['Om']; kap = st['kappa']; tuned = d['tuned']; eps = d['eps']; rc = d['rc']
            dk = dkappa(Phi*st['val'], Phi, Om)
            Phi0 = sum(d['rho'][k]*st['val'][k] for k in (0, 1))
            Xt = sum(rc[i]*eps[l]*dk[l]*Phi[l] for i, l in enumerate(tuned))
            return Phi0 + d['rho'][2]*kap*(1 - Xt)/(dk[2]*Phi[2])
        from scipy.optimize import brentq
        try:
            t0 = brentq(gres, 0.2, 1.0, xtol=1e-14)
        except ValueError:
            print('no root', align, seed); continue
        res = minimize_scalar(lambda t: svmin(t, seed, align), bounds=(t0 - 0.06, t0 + 0.06), method='bounded', options=dict(xatol=1e-14))
        t0 = res.x
        d = setup(t0, seed, align)
        F0, G0, kinds = d['system'](d['rc']); sc = np.abs(G0).max(axis=0)
        two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
        Uu, sv, Vt = np.linalg.svd((G0/sc)[:, two]); y = Uu[:, -1]
        if (y @ (G0/sc)[:, one]).sum() < 0: y = -y
        onemin = (y @ (G0/sc)[:, one]).min()
        st = d['st']; Phi = d['Phi']; Om = d['Om']; kap = st['kappa']; tuned = d['tuned']; eps = d['eps']; rc = d['rc']
        zeta_vec = Phi*st['val']; dk = dkappa(zeta_vec, Phi, Om)
        zc = y @ rc
        coef = np.zeros(d['K'])
        for ii, l in enumerate(tuned): coef[l] += y[ii]*eps[l]
        coef -= zc*dk*Phi
        Pc = coef @ d['U']; kpsi = (d['mu']*Pc) @ st['e']/st['nu']
        vs_c = np.sign(st['val'][2]); rho_c = d['rho'][2]
        sigma_m = np.sign(rho_c*vs_c)
        pred_zeta = -kpsi*rho_c/(Phi[2]*dk[2])        # = -kappa_y rho_c vs_c/(lambda_c (1 - X)) since dk[2] = vs_c (1 - X)
        # obstruction: displace targets along y
        dsz = 1e-3; dd = -dsz*y/kap; rt = rc + dd
        F1, G1, _ = d['system'](rt)
        if y @ F1 < 0: rt = rc - dd; F1, G1, _ = d['system'](rt)
        phi = y @ F1; zr = y @ rt
        m0 = minmove(G1/sc, -F1, one)
        out = []
        for sig in (sigma_m, -sigma_m):
            delta = 4*abs(phi)/(kap*abs(zr))
            rt2 = rt*(1 + sig*delta)
            F2, G2, _ = d['system'](rt2)
            out.append(f"sig={sig:+.0f}: phi={y @ F2:+.1e} move={minmove(G2/sc, -F2, one):.2e}")
        print(f"{'aligned' if align else 'anti   '} seed {seed}: t0={t0:.4f} sv_min={res.fun:.1e} min_one={onemin:+.1e} | "
              f"rho_c vs_c={rho_c*vs_c:+.2f} dkappa/dzeta(c)={dk[2]:+.4f} kappa_y={kpsi:+.3f} coef_c/(kappa_y rho_c)={coef[2]/(kpsi*rho_c):.4f} | "
              f"zeta(y;rc)={zc:+.4f} pred={pred_zeta:+.4f} sigma_m={sigma_m:+.0f} | obstruction phi_y={phi:.1e} move={m0:.2e} | " + "; ".join(out))
