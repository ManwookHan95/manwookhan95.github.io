"""J1 check of Theorem J1.9 (one-out-of-many band) in the resonant model of check_resonant2.py.
Targets: current ratios displaced by d * (direction increasing the frozen functional, i.e. phi_y > 0 for the near-certificate y).
Linearized Step A: find t (t_j >= 0 on one-sided S_th columns, free on two-sided) with G t = -Ft; minimize ||t||_inf (LP).
Compare: (a) no band; (b) band |sigma| <= beta on the row of ONE thick-type carrier (k = 0); (c) band on the non-thick private carrier 3."""
import numpy as np
from scipy.optimize import linprog
exec(open('check_resonant2.py').read().split("for th0 in (1e-5, 1e-8):")[0])
def minmove(G, rhs, one, band_rows, beta):
    nr, nc = G.shape; nb = len(band_rows)
    # variables: t (nc), sigma (nb), s (bound) ; minimize s
    c = np.zeros(nc + nb + 1); c[-1] = 1
    A_eq = np.hstack([G, np.array([[1.0 if r == br else 0.0 for br in band_rows] for r in range(nr)]).reshape(nr, nb), np.zeros((nr, 1))])
    A_ub = []; b_ub = []
    for j in range(nc):
        e = np.zeros(nc + nb + 1); e[j] = 1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
        e = np.zeros(nc + nb + 1); e[j] = -1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
    bounds = [(0, None) if j in one else (None, None) for j in range(nc)] + [(-beta, beta)]*nb + [(0, None)]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=rhs, bounds=bounds, method='highs')
    return res.fun if res.status == 0 else np.inf
for seed in range(1, 5):
    th0 = 1e-8
    def phi0(t):
        K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t, seed, th0)
        st = state(a, z, mu, U, Phi, np.zeros(K, bool)); q = qstar(a, mu)
        return sum(rho[k]/q*U[k] @ st['zh'] for k in (0, 1))
    t0 = brentq(phi0, 0.05, 20.0, xtol=1e-15)
    K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t0, seed, th0)
    st = state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']; Om = ~P
    st = state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
    eps = np.array([c.get(k, np.sign(st['val'][k]) or 1) for k in range(K)], float)
    rc = np.array([eps[l]*st['val'][l]/st['kappa'] for l in tuned])
    gens, kinds = [], []; h = 1e-9
    def Ft_of(s_, rt): return np.array([eps[l]*s_['val'][l] for l in tuned]) - rt*s_['kappa']
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h*np.sign(a[s]); gens.append((Ft_of(state(a2, z, mu, U, Phi, Om), rc) - Ft_of(st, rc))/h); kinds.append(typ[s])
        elif typ[s] == 'FR':
            z2 = z.copy(); z2[s] += h; gens.append((Ft_of(state(a, z2, mu, U, Phi, Om), rc) - Ft_of(st, rc))/h); kinds.append('FR')
    G = np.array(gens).T; G = G/np.abs(G).max(axis=0)
    two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
    Uu, sv, Vt = np.linalg.svd(G[:, two]); y = Uu[:, -1]
    if (y @ G[:, one]).sum() < 0: y = -y
    i0 = tuned.index(0); i3 = tuned.index(3)
    for dsz in (1e-3,):
        # target displacement along -y (so that phi_y = y^T Ft = y^T (kappa (rc - rt)) > 0)
        rt = rc + dsz*y/st['kappa']*(-1)*(-1)   # rt - rc = +dsz*y/kappa  =>  Ft = -dsz*y  => phi_y = -dsz <0 ? fix sign below
        Ft0 = Ft_of(st, rt); phi = y @ Ft0
        if phi < 0: rt = rc - dsz*y/st['kappa']; Ft0 = Ft_of(st, rt); phi = y @ Ft0
        rhs = -Ft0
        m_none = minmove(G, rhs, one, [], 0.0)
        m_band0 = minmove(G, rhs, one, [i0], 4*abs(phi)/abs(y[i0]))
        m_band3 = minmove(G, rhs, one, [i3], 4*abs(phi)/max(abs(y[i3]), 1e-12))
        print(f"seed {seed}: near-cert size {sv[-1]:.1e}, phi_y={phi:.2e}, |y_0|={abs(y[i0]):.2f}, |y_3|={abs(y[i3]):.1e} | "
              f"min ||t||: no band {m_none:.2e}; band on thick-type row 0: {m_band0:.2e}; band (same width rule) on carrier 3: {m_band3:.2e}")
