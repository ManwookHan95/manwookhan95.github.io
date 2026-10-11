"""Near-certificate version: at the resonant configurations of check_resonant.py (bank mass th0 varied), take the left singular
vector y of the two-sided column matrix (smallest singular value = near-certificate size), orient it so that the one-sided (S_th raise)
actions are >= 0, and check: kappa_Psi < 0, sgn coef_k = -sgn(a_p v_k(p)) on thick-type carriers (J1.6(a)), y ~ eps*rho on K0,
one-sided mass identity, and that a pull at a far data-sign contact lowers y^T Ft (J1.7)."""
import numpy as np
exec(open('check_resonant.py').read().split("for seed in range(6):")[0])
def build_th(t, seed, th0):
    K, n, S, U, a, z, typ, Phi, mu, c, rho = build(t, seed)
    for k in (0, 1):
        for s in S[k]['hole']: a[s] = c[k]*th0
    return K, n, S, U, a, z, typ, Phi, mu, c, rho
for th0 in (1e-5, 1e-8):
    for seed in range(1, 5):
        def phi0(t):
            K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t, seed, th0)
            st = state(a, z, mu, U, Phi, np.zeros(K, bool)); q = qstar(a, mu)
            return sum(rho[k]/q*U[k] @ st['zh'] for k in (0, 1))
        t0 = brentq(phi0, 0.05, 20.0, xtol=1e-15)
        K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t0, seed, th0)
        st = state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']; Om = ~P
        st = state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
        eps = np.array([c.get(k, np.sign(st['val'][k]) or 1) for k in range(K)], float)
        rt = np.array([eps[l]*st['val'][l]/st['kappa'] for l in tuned])
        Ft = lambda s_: np.array([eps[l]*s_['val'][l] for l in tuned]) - rt*s_['kappa']
        zeta = Phi*st['val']; dk = dkappa(zeta, Phi, Om)
        gens, kinds = [], []; h = 1e-9
        for s in range(n):
            if typ[s] in ('TS', 'Sth'):
                a2 = a.copy(); a2[s] += h*np.sign(a[s]); gens.append((Ft(state(a2, z, mu, U, Phi, Om)) - Ft(st))/h); kinds.append(typ[s])
            elif typ[s] == 'FR':
                z2 = z.copy(); z2[s] += h; gens.append((Ft(state(a, z2, mu, U, Phi, Om)) - Ft(st))/h); kinds.append('FR')
        G = np.array(gens).T; two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
        Gn = G/np.abs(G).max(axis=0)
        Uu, sv, Vt = np.linalg.svd(Gn[:, two]); y = Uu[:, -1]
        if (y @ Gn[:, one]).sum() < 0: y = -y
        one_min = (y @ Gn[:, one]).min()
        zc = sum(y[i]*rt[i] for i in range(len(tuned))); coef = np.zeros(K)
        for i, l in enumerate(tuned): coef[l] += y[i]*eps[l]
        coef -= zc*dk*Phi
        Pc = coef @ U; kc = (mu*Pc) @ st['e']/st['nu']
        signs = [np.sign(coef[k]) == -np.sign(a[S[k]['thick'][0]]*U[k, S[k]['thick'][0]]) for k in (0, 1)]
        q = qstar(a, mu); ratio = [coef[k]/(kc*rho[k]/q) for k in (0, 1)]
        jumps = []
        for k in (0, 1):
            j = S[k]['other'][0]; p = S[k]['thick'][0]; tau = np.sign(a[p]*U[k, p]*U[k, j])
            z2 = z.copy(); z2[j] = tau; a2 = a.copy(); a2[j] = tau*1e-9
            dF = Ft(state(a2, z2, mu, U, Phi, Om)) - Ft(st); pred = coef[k]*U[k, j]*(tau - z[j])
            jumps.append((y @ dF, pred))
        print(f"th0={th0:.0e} seed={seed}: near-cert size(min sv)={sv[-1]:.1e}, min one-sided action={one_min:.1e}, kappa_Psi={kc:.3f}, "
              f"sign ok={signs}, coef_k/(kappa rho_k)={np.round(ratio, 4)}, jump y^T dFt vs pred: {[(f'{u:.2e}', f'{v:.2e}') for u, v in jumps]}")
