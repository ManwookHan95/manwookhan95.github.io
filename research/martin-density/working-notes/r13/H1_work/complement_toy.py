"""H1 numerics: Theorem UC (UC1)/(UC2) on J1-ref's consistent toy.  Units = single rows {k} (all targets free in the toy).
(UC1) down-scale the ALIGNED carrier's row alone; (UC2) keep row k and down-scale the complement (all other rows of the block).
Prediction (variant A, peak resource => zeta_m(y; rc) = 0): (UC2) relieves for the ANTI-ALIGNED k and not for the aligned one;
(UC1) relieves for the aligned one.  The obstruction is created as in J1-ref N3 (targets displaced along y)."""
import numpy as np
from scipy.optimize import brentq
exec(open('align_toy.py').read().split("def run(variant):")[0])
for variant in ('A', 'B'):
  for seed in range(1, 5):
    th0 = 1e-8
    def build_th(t):
        K, n, S, U, a, z, typ, Phi, mu, c, rho = build(t, seed)
        for k in (0, 1):
            for s in S[k]['hole']: a[s] = c[k]*th0
        if variant == 'B': typ[S[2]['other'][2]] = 'none'
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
                z2_ = z.copy(); z2_[s] += h; gens.append((Ft_of(state(a, z2_, mu, U, Phi, Om)) - F0)/h); kinds.append('FR')
        return F0, np.array(gens).T, kinds
    F0, G0, kinds = system(rc); sc = np.abs(G0).max(axis=0)
    two = [j for j, kd in enumerate(kinds) if kd in ('TS', 'FR')]; one = [j for j, kd in enumerate(kinds) if kd == 'Sth']
    Uu, sv, Vt = np.linalg.svd((G0/sc)[:, two]); y = Uu[:, -1]
    if (y @ (G0/sc)[:, one]).sum() < 0: y = -y
    d = -1e-3*y/st['kappa']; rt = rc + d; F1, G1, _ = system(rt)
    if y @ F1 < 0: rt = rc - d; F1, G1, _ = system(rt)
    ph = y @ F1
    al = {k: rho[k]*st['zh'] @ U[k] for k in (0, 1)}
    out = [f"var {variant} seed {seed}: zeta(y;rc)={y @ rc:+.1e} phi={ph:.1e} move0={minmove(G1/sc, -F1, one):.2e}"]
    for k in (0, 1):
        i = tuned.index(k); lab = 'aligned' if al[k] > 0 else 'anti'
        # (UC2) complement scaling: keep row k, scale others by s = 1 - delta
        zE = y[i]*rt[i]; zm = y @ rt
        delta = 4*abs(ph)/(st['kappa']*max(abs(zE - zm), 1e-12))
        rt2 = rt*(1 - delta); rt2[i] = rt[i]
        F2, G2, _ = system(rt2)
        out.append(f"k{k}({lab}) UC2: zetaE={zE:+.1e} phi={y @ F2:+.1e} move={minmove(G2/sc, -F2, one):.2e}")
    print(" | ".join(out))
