"""H1 numerics: (i) signed derivative d kappa/d zeta(c) = vs_c (1 - X) at a peak (Lemma NP's sign bookkeeping);
(ii) block-rescaling lever (Lemma TF with Delta = sigma rt^(m)): in variant B (no peak resource) rescale ALL targets of the block by
s = 1 + sgn(zeta) delta; prediction: this direction lowers phi_y by kappa delta |zeta| and relieves once that exceeds phi_y."""
import sys, os
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
    zeta_vec = Phi*st['val']; dk = dkappa(zeta_vec, Phi, Om)
    # (i) signed derivative at the peak c = 2 versus sign of zeta(c), and its modulus 1 - X
    cpk = 2; line = f"var {variant} seed {seed}: peak dkappa/dzeta = {dk[cpk]:+.4f}, sgn zeta(c) = {np.sign(zeta_vec[cpk]):+.0f}"
    # flip the sign of the peak's value (z -> -z on its private coords) and recompute: derivative should flip sign
    z2 = z.copy(); z2[S[cpk]['other']] *= -1
    st2 = state(a, z2, mu, U, Phi, Om); dk2 = dkappa(Phi*st2['val'], Phi, Om)
    line += f" | after flipping the peak's value: dkappa/dzeta = {dk2[cpk]:+.4f}, sgn zeta(c) = {np.sign(Phi[cpk]*st2['val'][cpk]):+.0f}"
    # (ii) block rescaling lever
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
    zt = y @ rt; ph = y @ F1; delta = 4*abs(ph)/(st['kappa']*abs(zt))
    out = []
    for lab, sgn in (('pred', np.sign(zt)), ('opp', -np.sign(zt))):
        rt2 = rt*(1 + sgn*delta); F2, G2, _ = system(rt2)
        out.append(f"{lab}(s={1+sgn*delta:.3f}): phi={y @ F2:+.1e} move={minmove(G2/sc, -F2, one):.2e}")
    print(line); print(f"   zeta={zt:+.2e} phi={ph:.1e} move0={minmove(G1/sc, -F1, one):.2e} | " + "; ".join(out))
