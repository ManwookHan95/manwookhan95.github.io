"""J1-ref check N3: J1's check_band.py builds the generator matrix with targets = current ratios (rc) but the right-hand side with
displaced targets rt = rc +- dsz*y/kappa.  The Sys-A columns depend on the targets (through zeta_m(y) = sum_l y_l rt_l, e.g. the column of
the peak's private FR resource is -(1-X) lambda_c v_c(s) rt^(m)).  Here everything is recomputed CONSISTENTLY at rt.
Variants: (A) J1's toy (peak has a private FR coordinate = private two-sided peak resource);
          (B) the same toy with the peak's FR coordinate removed (no private peak resource).
For each: smallest singular value of the two-sided columns at rc and at rt, zeta(y; rt), phi_y, LP min||t||_inf without band and with
a band (half-width rule of check_band) on the thick-type row 0.  Also (A'): targets displaced ORTHOGONALLY to y inside the block
(sum_l y_l delta_l = 0): then y stays a near-certificate but phi_y ~ 0 (marginal)."""
import sys, os
import numpy as np
from scipy.optimize import linprog, brentq
base = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(base, "rerun"))
os.chdir(os.path.join(base, 'rerun'))
exec(open('check_resonant.py').read().split("for seed in range(6):")[0])
def minmove(G, rhs, one, band_rows, beta):
    nr, nc = G.shape; nb = len(band_rows)
    cobj = np.zeros(nc + nb + 1); cobj[-1] = 1
    Bm = np.zeros((nr, nb))
    for i, br in enumerate(band_rows): Bm[br, i] = 1.0
    A_eq = np.hstack([G, Bm, np.zeros((nr, 1))])
    A_ub = []; b_ub = []
    for j in range(nc):
        e = np.zeros(nc + nb + 1); e[j] = 1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
        e = np.zeros(nc + nb + 1); e[j] = -1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
    bounds = [(0, None) if j in one else (None, None) for j in range(nc)] + [(-beta, beta)]*nb + [(0, None)]
    res = linprog(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=rhs, bounds=bounds, method='highs')
    return res.fun if res.status == 0 else np.inf
def run(variant):
    for seed in range(1, 5):
        th0 = 1e-8
        def build_th(t):
            K, n, S, U, a, z, typ, Phi, mu, c, rho = build(t, seed)
            for k in (0, 1):
                for s in S[k]['hole']: a[s] = c[k]*th0
            if variant == 'B':
                typ[S[2]['other'][2]] = 'none'
            return K, n, S, U, a, z, typ, Phi, mu, c, rho
        def phi0(t):
            K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t)
            st = state(a, z, mu, U, Phi, np.zeros(K, bool)); q = qstar(a, mu)
            return sum(rho[k]/q*U[k] @ st['zh'] for k in (0, 1))
        t0 = brentq(phi0, 0.05, 20.0, xtol=1e-15)
        K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t0)
        st = state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']; Om = ~P
        st = state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
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
        F0, G0, kinds = system(rc)
        sc = np.abs(G0).max(axis=0)
        two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
        Uu, sv, Vt = np.linalg.svd((G0/sc)[:, two]); y = Uu[:, -1]
        if (y @ (G0/sc)[:, one]).sum() < 0: y = -y
        i0 = tuned.index(0)
        dsz = 1e-3
        out = []
        for mode in ('along', 'orth'):
            if mode == 'along':
                d = -dsz*y/st['kappa']
            else:
                w = np.zeros(len(tuned)); w[i0] = 1.0; w -= (w @ y)*y; w /= np.linalg.norm(w); d = dsz*w/st['kappa']
            rt = rc + d
            F1, G1, _ = system(rt)
            if mode == 'along' and y @ F1 < 0:
                rt = rc - d; F1, G1, _ = system(rt)
            Gn1 = G1/sc
            sv1 = np.linalg.svd(Gn1[:, two], compute_uv=False)[-1]
            ytwo = np.abs(y @ Gn1[:, two]).max()
            phi = y @ F1; zeta = y @ rt
            m_none = minmove(Gn1, -F1, one, [], 0.0)
            m_band = minmove(Gn1, -F1, one, [i0], 4*max(abs(phi), dsz)/abs(y[i0]))
            m_stale = minmove(G0/sc, -F1, one, [], 0.0)
            out.append(f"[{mode}] sv_min(two)@rt={sv1:.1e} max|y^T g_two|@rt={ytwo:.1e} zeta(y;rt)={zeta:.1e} phi_y={phi:.1e} "
                       f"min||t||: consistent {m_none:.2e}, consistent+band {m_band:.2e}, STALE generators (J1 check_band) {m_stale:.2e}")
        print(f"variant {variant} seed {seed}: sv_min(two)@rc={sv[-1]:.1e} | " + " | ".join(out))
for v in ('A', 'B'):
    run(v)
