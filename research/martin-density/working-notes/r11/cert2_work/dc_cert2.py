"""cert2: Lemma DC in the small-perturbation regime (pull chosen adaptively with v(j_p) in [r, 2 r], as in X2 3.2(iii)).
Model as dc_cert.py; signature sets of 30 coordinates with v_l(s) = c 2^{-i}; bank at the 2nd element, pull at the element with v in [r,2r).
Checks: Jacobian at 0 vs I - p q^T (blockwise); zero P* with |P*| <= r where r := 2 K_J |F(0)| (and vs X2-ref radius
4 K_J (1+1/A_min) delta_1 + 8 K_J W_pull/A_min); exact nv; statuses; gap identity; and the C-factor in gap preservation.
"""
import numpy as np
from scipy.optimize import fsolve
from dc_cert import block_norming, Model

def build(seed, nb=1, fineW=1e-7):
    r = np.random.default_rng(seed)
    S = 12 + 30*3*nb + 4
    mu = 0.5*0.995**np.arange(S)
    rows, blk, Phi, role, sig = [], [], [], [], {}
    nxt = 12
    for b in range(1, nb+1):
        for k in range(7):
            u = np.zeros(S)
            if k < 2:
                u[:10] = r.normal(size=10)*0.05; u[k] += 1.5*(1 if k == 0 else -1); ph = 0.02 + 0.01*k; rl = 'peak'
            elif k < 5:
                u[:10] = r.normal(size=10)*0.05
                ss = list(range(nxt, nxt+30)); nxt += 30
                u[ss] = 0.3*2.0**(-np.arange(30)); sig[len(rows)] = ss; u[3] = -0.55 + 0.05*r.normal()
                ph = 0.08 + 0.02*k; rl = 'omega'
            else:
                ph = fineW*(k-3); rl = 'fine'
                tgt = sig[len(rows) - 3]           # meets the signature set of an Omega carrier (incl. deep coordinates)
                u[tgt[1]] += 0.3; u[tgt[10]] += 0.3; u[tgt[18]] += 0.3
            rows.append(u); blk.append(b); Phi.append(ph); role.append(rl)
    U = np.array(rows); blk = np.array(blk); Phi = np.array(Phi)
    for i in range(len(U)):
        U[i] /= np.abs(U[i]).sum() + np.linalg.norm(mu*U[i])
    A0 = np.zeros(S); A0[0] = 0.6; A0[1] = -0.3
    z0 = np.zeros(S); z0[0] = 1; z0[1] = -1
    z0[2:10] = np.clip(r.normal(size=8)*0.5, -0.9, 0.9); z0[3] = 1.0; z0[5] = -1.0
    z0[12:nxt] = 1.0
    return Model(mu, U, blk, Phi), A0, z0, sig, role, S

def run(seed, nb=1, mass=1e-6, verbose=True):
    md, A0, z0, sig, role, S = build(seed, nb)
    D0 = md.forced(A0, z0)
    def status(D, i):
        B = D['blocks'][md.blk[i]]; pos = list(B['idx']).index(i); return bool(B['P'][pos])
    Om = [i for i in sig if not status(D0, i)]
    if not Om: return None
    A1 = A0.copy(); A1[3] += mass; A1[5] -= 0.7*mass        # theta-masses at two contacts
    z1 = z0.copy()
    D1 = md.forced(A1, z1)
    delta1 = max(abs(D1['val'][i] - D0['val'][i]) for i in Om)
    Amin = min(B['A'] for B in D0['blocks'].values())
    KJ = 1 + 2/Amin
    rX2 = 4*KJ*(1 + 1/Amin)*delta1            # X2-ref (p-DC1) without the W_pull / T^4 s_1 terms
    nu1 = np.linalg.norm(md.mu*A1)
    lev = []
    for n, i in enumerate(Om):
        ss = sig[i]; v = md.U[i]
        if n % 2 == 0:
            # pull: element with v in [rX2, 2 rX2)
            cand = [s for s in ss[3:] if rX2 <= v[s] < 2*rX2]
            if not cand: return None
            lev.append(('TU', i, ss[1], cand[0], v))
        else:
            lev.append(('Z', i, ss[1], None, v))
    def row_of(P):
        A = A1.copy(); z = z1.copy()
        for (typ, i, j, jp, v), p in zip(lev, P):
            if typ == 'Z':
                if p <= 0: z[j] = 1.0 - abs(p)/v[j]
                else: A[j] += nu1/(md.mu[j]**2*v[j])*p
            else:
                z[jp] = -1.0; A[jp] += -24*md.lam[i]*v[jp]
                A[j] += nu1/(md.mu[j]**2*v[j])*(p + 2*v[jp])
        return A, z
    def F(P):
        A, z = row_of(P); D = md.forced(A, z)
        return np.array([D['val'][i] - D['blocks'][md.blk[i]]['A']/D0['blocks'][md.blk[i]]['A']*D0['val'][i] for (_, i, *_) in lev])
    n = len(lev); P0 = np.zeros(n); F0 = F(P0)
    h = 1e-9; J = np.zeros((n, n))
    for c in range(n):
        e = np.zeros(n); e[c] = h; J[:, c] = (F(e) - F(-e))/(2*h)
    p = np.array([D0['val'][i]/D0['blocks'][md.blk[i]]['A'] for (_, i, *_) in lev])
    q = np.array([md.lam[i]*D0['blocks'][md.blk[i]]['w'][list(D0['blocks'][md.blk[i]]['idx']).index(i)] for (_, i, *_) in lev])
    same = np.array([[1.0 if md.blk[lev[a][1]] == md.blk[lev[c][1]] else 0.0 for c in range(n)] for a in range(n)])
    Jth = np.eye(n) - np.outer(p, q)*same
    # W_pull: fine carriers meeting pull coordinates (weight-weighted |u_k(j_p)|)
    Wp = sum(md.lam[k]*2*abs(md.U[k][jp]) for (typ, i, j, jp, v) in lev if typ == 'TU' for k in range(len(md.U)) if role[k] == 'fine')
    Pst, info, ier, msg = fsolve(F, P0, xtol=1e-15, full_output=True)
    res = F(Pst)
    A, z = row_of(Pst); D = md.forced(A, z)
    nv_err = max(abs(md.lam[i]*D['val'][i]/D['blocks'][md.blk[i]]['A'] - md.lam[i]*D0['val'][i]/D0['blocks'][md.blk[i]]['A']) for (_, i, *_) in lev)
    st_ok = all(status(D, i) == status(D0, i) for i in range(len(md.U)) if role[i] != 'fine')
    gerr = 0.0; dC = 0.0; gratio = 1e9
    for (_, i, *_) in lev:
        B, B0 = D['blocks'][md.blk[i]], D0['blocks'][md.blk[i]]; pos = list(B0['idx']).index(i)
        g0 = B0['M'] - abs(B0['w'][pos]); g1 = B['M'] - abs(B['w'][pos])
        gerr = max(gerr, abs(g1 - ((B['C']/B0['C'])*g0 + 1 - B['C']/B0['C'])))
        dC = max(dC, abs(B['C'] - B0['C'])); gratio = min(gratio, g1/g0)
    rPM = 2*KJ*abs(F0).max()
    if verbose:
        print(f"seed {seed:2d} nb {nb} |Om| {n} delta1 {delta1:.2e} |F(0)| {abs(F0).max():.2e} rX2 {rX2:.2e} W_pull {Wp:.1e} "
              f"| J-(I-pq^T) | {abs(J-Jth).max():.1e} |P*| {abs(Pst).max():.2e} <= 2KJ|F0| {rPM:.2e}: {abs(Pst).max() <= rPM} "
              f"res {abs(res).max():.0e} nv {nv_err:.0e} st {st_ok} gapid {gerr:.0e} |dC| {dC:.1e} min gap'/gap {gratio:.4f}")
    return abs(Pst).max()/rPM, abs(J-Jth).max(), abs(res).max()

if __name__ == '__main__':
    out = []
    for sd in range(30):
        for nb in (1, 2):
            o = run(sd, nb)
            if o: out.append(o)
    out = np.array(out)
    print(f"instances {len(out)}; max |P*|/(2K_J|F(0)|) {out[:,0].max():.3f}; max Jacobian deviation {out[:,1].max():.2e}; max residual {out[:,2].max():.1e}")
