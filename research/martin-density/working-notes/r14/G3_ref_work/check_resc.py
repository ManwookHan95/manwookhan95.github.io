"""Check Cor 2.11 (G3) and the referee's Lemma R-ESC (1)-(3) term by term on the decompositions of test_pin variants
and on random feasible decompositions (maximizing random combinations of the pair's switching amplitudes).

Lemma R-ESC: unshifted block, G = {l+, l-}, J_c = {j} (the shared coordinate), private coordinates of each carrier split
w.r.t. eps_k = sgn gamma_k into aligned A_k, anti-aligned R_k (|z| weights) and free (eta weights).  Then
 (1) |gamma_k| F_k <= 2 alpha(R_k)/t + t/(2 q0) + Psi_k
 (2) |gamma_k| Fr_k <= t/q0 + Psi_k
 (3) sum_k |gamma_k| (N_k - F_k - h_k) <= E(t) = S_1 + r_Q + t/(2 q0) + 2 alpha(J_c)/t + Psi_J
"""
import numpy as np, warnings, sys
warnings.filterwarnings('ignore')
import test_pin2 as tp
from refmodel import qstar

rng = np.random.default_rng(3)
worst = {}


def rec(name, lhs, rhs):
    v = (lhs - rhs) / (1 + abs(rhs))
    worst[name] = max(worst.get(name, -np.inf), v)


def analyse(row, t, d):
    D = row.derived(t, d)
    V, ep, em = D['V'], D['ep'], D['em']
    gam = D['gam'][0]
    U = row.Us[0]; z = row.z; a = row.a; h = row.h
    w = row.ws[0]; M = np.abs(w).max(); C = np.linalg.norm(row.Phis[0] * w)
    P = np.where(np.abs(w) >= M - 1e-6)[0]
    Q = np.setdiff1d(np.arange(len(w)), P)
    if 0 in P or 1 in P:
        return
    dTh = D['Thm'][0] - D['Thp'][0]
    etaP = np.abs(dTh[P]).max()
    PhiP2 = (row.Phis[0][P] ** 2).sum()
    sig = row.sigmas[0]
    S1 = t / row.q0 + (sig / row.q0) * etaP * (1 + M * PhiP2 / C)
    G = [0, 1]
    QmG = np.setdiff1d(Q, G)
    uz = U @ row.zhat
    rQ = abs(uz[QmG] @ gam[QmG])
    Jc = [tp.J]
    psi = V - gam[G] @ U[G]
    PsiJ = np.abs(psi[Jc]).sum()
    alphaJ = np.abs(a[Jc]).sum()
    E = S1 + rQ + t / (2 * row.q0) + 2 * alphaJ / t + PsiJ
    lhs3 = 0.0
    for k in G:
        eps = np.sign(gam[k]) if abs(gam[k]) > 1e-12 else 1.0
        supp = np.where(np.abs(U[k]) > 0)[0]
        priv = [s for s in supp if s not in Jc]
        Nk = Fk = Frk = alR = Psik = 0.0
        for s in priv:
            o = eps * z[s] * U[k, s]
            if o > 0:
                Nk += abs(z[s]) * abs(U[k, s])
            elif o < 0:
                Fk += abs(z[s]) * abs(U[k, s])
                if row.F[s]:
                    alR += abs(a[s])
            if (not row.F[s]) and abs(z[s]) < 1:
                Frk += (1 - abs(z[s])) * abs(U[k, s])
            Psik += abs(psi[s])
        hk = np.sum(np.abs(U[k] * h))
        rec('R-ESC (1)', abs(gam[k]) * Fk, 2 * alR / t + t / (2 * row.q0) + Psik)
        rec('R-ESC (2)', abs(gam[k]) * Frk, t / row.q0 + Psik)
        lhs3 += abs(gam[k]) * (Nk - Fk - hk)
    rec('R-ESC (3)', lhs3, E)


for var in ['ii', 'i', 'iii', 'iv', 'v', 'vi']:
    row = tp.build(var)
    for t in [0.1, 0.03, 0.01]:
        lam = row.lams[0]
        for rep in range(6):
            c = rng.normal(size=2)
            def obj(Vv, c=c, t=t):
                g0 = lam[0] * ((row.ws[0][0] - Vv['Wm'][0][0]) / t - (Vv['Wp'][0][0] - row.ws[0][0]) / t)
                g1 = lam[1] * ((row.ws[0][1] - Vv['Wm'][0][1]) / t - (Vv['Wp'][0][1] - row.ws[0][1]) / t)
                return c[0] * g0 + c[1] * g1
            try:
                d = row.decomp(t, obj)
            except Exception:
                continue
            if d['status'] != 'optimal':
                continue
            analyse(row, t, d)
    print(var, 'done', flush=True)

print('worst normalized slack (must be <= ~1e-6):')
for k, v in worst.items():
    print(f'  {k:12s} {v: .3e}  {"OK" if v <= 1e-5 else "VIOLATED"}')
