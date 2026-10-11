"""H1 numerics: Lemma AL (needed direction = inward iff aligned) and Theorem IN / OUT on J1-ref's CONSISTENT toy (ref_band_consistent).
For each seed and variant (A: peak with private FR resource; B: without), at the exact resonance (Phi0(zhat) = 0):
 - alignment of the thick-type carriers k = 0, 1: sign of rho_k u_k(zhat) (aligned > 0);
 - near-certificate y (near-null left vector of the two-sided columns, oriented positively on one-sided columns);
   predicted sign of y_k rt_k = -sign(rho_k u_k)  (Lemma AL);
 - obstruction: targets displaced along y (phi_y > 0, as in J1-ref N3); then a single-row displacement of row k by a factor (1 -+ s):
   inward/outward; min ||t||_inf of the consistent LP (generators recomputed at the new targets).  Prediction: only the needed
   direction (inward for aligned, outward for anti-aligned) removes the obstruction.
Also prints zeta_m(y; rt) (variant A: ~0 by R-PK) and Phi0 = sum rho_k u_k (mixed alignment forced when ~0)."""
import sys, os
import numpy as np
from scipy.optimize import linprog, brentq
base = '/tmp/claude-0/-home-user-manwookhan95-github-io/ec871029-cb65-5b86-9917-5095aaba7b7b/scratchpad/ctx/r12/J1_ref_work/rerun'
sys.path.insert(0, base); cwd = os.getcwd(); os.chdir(base)
exec(open('check_resonant.py').read().split("for seed in range(6):")[0])
os.chdir(cwd)

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
        al = {k: rho[k]*st['zh'] @ U[k] for k in (0, 1)}          # rho_k u_k(zhat): >0 aligned
        pos = {k: tuned.index(k) for k in (0, 1)}
        pred = {k: -np.sign(al[k]) for k in (0, 1)}                # predicted sign of y_k rt_k
        obs = {k: np.sign(y[pos[k]]*rc[pos[k]]) for k in (0, 1)}
        # obstruction: displace along y with phi_y > 0
        dsz = 1e-3
        d = -dsz*y/st['kappa']; rt = rc + d
        F1, G1, _ = system(rt)
        if y @ F1 < 0:
            rt = rc - d; F1, G1, _ = system(rt)
        base_move = minmove(G1/sc, -F1, one)
        line = (f"var {variant} seed {seed}: rho_k u_k(zhat) = ({al[0]:+.3f}, {al[1]:+.3f}) [aligned>0]; Phi0={al[0]+al[1]:+.1e}; "
                f"sign(y_k rt_k) obs/pred = ({obs[0]:+.0f}/{pred[0]:+.0f}, {obs[1]:+.0f}/{pred[1]:+.0f}); zeta={y @ rt:+.1e}; phi_y={y @ F1:.1e}; "
                f"move(no relief)={base_move:.2e}")
        res = []
        for k in (0, 1):
            i = pos[k]
            s = 4*abs(y @ F1)/(st['kappa']*abs(y[i]*rt[i])) + 1e-12
            for lab, fac in (('in', 1 - s), ('out', 1 + s)):
                rt2 = rt.copy(); rt2[i] = rt[i]*fac
                F2, G2, _ = system(rt2)
                mv = minmove(G2/sc, -F2, one)
                res.append(f"k{k}-{lab}: phi={y @ F2:+.1e} move={mv:.2e}")
        print(line + " | " + "; ".join(res))

for v in ('A', 'B'):
    run(v)
