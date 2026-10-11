"""J1-ref check N2 (argv: VFAR [B = remove the peak's private FR resource]): Corollary J1.5's reading ("no companion that keeps the one-sided signs realizes the current Step-A targets")
versus Theorem J1.7 (a far placement keeps every one-sided (S_th) sign and makes Step A solvable).
Model: J1's resonant one-block toy (check_resonant2/check_band), with the far coordinate of thick-type carrier 0 given v = VFAR.
At R_1: near-certificate y, targets rt = rc - dsz*y/kappa (phi_y > 0), linearized min ||t||_inf (one-sided S_th columns t >= 0).
At R' = R_1 + pull at the helpful far coordinate j of carrier 0 (z_j: c_0 -> tau = -c_0, tiny anti-sign mass): SAME targets rt,
generators recomputed at R'; S_th coordinates untouched (signs kept).  Also report: the J1.4 quantities (frozen functional Phi = Psi/kappa
at R_1 and R', and the Deep term E(j)(z'_j - z_j)/kappa that J1.4's bound must absorb)."""
import sys, os
import numpy as np
from scipy.optimize import linprog, brentq
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rerun'))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rerun'))
src = open('check_resonant.py').read().split("for seed in range(6):")[0]
exec(src)
VFAR = float(sys.argv[1]) if len(sys.argv) > 1 else 1e-2
NOPEAKRES = len(sys.argv) > 2 and sys.argv[2] == "B"
def build_th(t, seed, th0):
    K, n, S, U, a, z, typ, Phi, mu, c, rho = build(t, seed)
    for k in (0, 1):
        for s in S[k]['hole']: a[s] = c[k]*th0
    U[0, S[0]['other'][0]] = VFAR
    if NOPEAKRES: typ[S[2]['other'][2]] = 'none'
    return K, n, S, U, a, z, typ, Phi, mu, c, rho
def minmove(G, rhs, one):
    nr, nc = G.shape
    cobj = np.zeros(nc + 1); cobj[-1] = 1
    A_ub = []; b_ub = []
    for j in range(nc):
        e = np.zeros(nc + 1); e[j] = 1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
        e = np.zeros(nc + 1); e[j] = -1; e[-1] = -1; A_ub.append(e); b_ub.append(0)
    bounds = [(0, None) if j in one else (None, None) for j in range(nc)] + [(0, None)]
    res = linprog(cobj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=np.hstack([G, np.zeros((nr, 1))]), b_eq=rhs,
                  bounds=bounds, method='highs')
    return (res.fun, res.x[:-1]) if res.status == 0 else (np.inf, None)
def gens_at(a, z, mu, U, Phi, Om, tuned, eps, rt, typ, n):
    def Ft_of(s_): return np.array([eps[l]*s_['val'][l] for l in tuned]) - rt*s_['kappa']
    st = state(a, z, mu, U, Phi, Om); F0 = Ft_of(st)
    gens, kinds = [], []; h = 1e-9
    for s in range(n):
        if typ[s] in ('TS', 'Sth'):
            a2 = a.copy(); a2[s] += h*np.sign(a[s]); gens.append((Ft_of(state(a2, z, mu, U, Phi, Om)) - F0)/h); kinds.append(typ[s])
        elif typ[s] == 'FR':
            z2 = z.copy(); z2[s] += h; gens.append((Ft_of(state(a, z2, mu, U, Phi, Om)) - F0)/h); kinds.append('FR')
    G = np.array(gens).T
    return F0, G, kinds, st
for seed in range(1, 5):
    th0 = 1e-8
    def phi0(t):
        K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t, seed, th0)
        st = state(a, z, mu, U, Phi, np.zeros(K, bool)); q = qstar(a, mu)
        return sum(rho[k]/q*U[k] @ st['zh'] for k in (0, 1))
    try:
        t0 = brentq(phi0, 0.05, 20.0, xtol=1e-15)
    except ValueError:
        print(f"seed {seed}: no resonance root"); continue
    K, n, S, U, a, z, typ, Phi, mu, c, rho = build_th(t0, seed, th0)
    st = state(a, z, mu, U, Phi, np.zeros(K, bool)); P = st['blk']['P']; Om = ~P
    if not P[2] or P[0] or P[1] or P[3]:
        print(f"seed {seed}: pattern changed"); continue
    st = state(a, z, mu, U, Phi, Om); tuned = [k for k in range(K) if Om[k]]
    eps = np.array([c.get(k, np.sign(st['val'][k]) or 1) for k in range(K)], float)
    rc = np.array([eps[l]*st['val'][l]/st['kappa'] for l in tuned])
    F0, G, kinds, _ = gens_at(a, z, mu, U, Phi, Om, tuned, eps, rc, typ, n)
    sc = np.abs(G).max(axis=0); Gn = G/sc
    two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
    Uu, sv, Vt = np.linalg.svd(Gn[:, two]); y = Uu[:, -1]
    if (y @ Gn[:, one]).sum() < 0: y = -y
    dsz = 1e-3
    rt = rc - dsz*y/st['kappa']
    F1, G1, _, st1 = gens_at(a, z, mu, U, Phi, Om, tuned, eps, rt, typ, n)
    phi = y @ F1
    if phi < 0:
        rt = rc + dsz*y/st['kappa']; F1, G1, _, st1 = gens_at(a, z, mu, U, Phi, Om, tuned, eps, rt, typ, n); phi = y @ F1
    m1, _ = minmove(G1/sc, -F1, one)
    # placement (pull) at the helpful far coordinate j of thick-type carrier 0
    k = 0; j = S[k]['other'][0]; p = S[k]['thick'][0]; tau = np.sign(a[p]*U[k, p]*U[k, j])
    assert z[j]*tau <= 0
    z2 = z.copy(); z2[j] = tau; a2 = a.copy(); a2[j] = tau*1e-9
    F2, G2, _, st2 = gens_at(a2, z2, mu, U, Phi, Om, tuned, eps, rt, typ, n)
    m2, t2 = minmove(G2/sc, -F2, one)
    sth = [s for s in range(n) if typ[s] == 'Sth']
    signs_kept = all(np.sign(a2[s]) == np.sign(a[s]) and z2[s] == z[s] for s in sth)
    # frozen functional bookkeeping (J1.4): Psi_y and its value at R_1 and R'
    zc = sum(y[i]*rt[i] for i in range(len(tuned)))
    dk = dkappa(Phi*st1['val'], Phi, Om)
    coef = np.zeros(K)
    for i, l in enumerate(tuned): coef[l] += y[i]*eps[l]
    coef -= zc*dk*Phi
    Psi = coef @ U; kap = (mu*Psi) @ st1['e']/st1['nu']
    deep_term = (Psi[j] - kap*st1['a'][j])*(z2[j] - z[j])
    print(f"seed {seed}: near-cert size {sv[-1]:.1e}, phi_y={phi:.2e}, kappa_Psi={kap:.3f} | min||t|| at R_1: {m1:.2e}; "
          f"after pull at far j (v={U[k, j]:.0e}, S_th signs kept={signs_kept}): min||t|| at R': {m2:.2e}, |Ft(R')|_inf={np.abs(F2).max():.2e}, "
          f"y^T Ft(R')={y @ F2:.2e} | Phi(zhat')-Phi(zhat_1)={(Psi @ st2['zh'] - Psi @ st1['zh'])/kap:.2e}, Deep term E(j)dz_j/kappa={deep_term/kap:.2e}")
