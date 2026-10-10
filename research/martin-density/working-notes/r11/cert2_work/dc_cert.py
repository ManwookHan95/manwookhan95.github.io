"""cert2: independent finite model for Lemma DC (exact d-consistency by levers).
One block (m=1) or two blocks, diagonal base U^* e_s^* = mu_s k_s.  Row = (A unnormalized, z).  Forced data via lem:threshold
(E1) A = sum_P Phi^2 (nu - th), (E2) A^2 = th^2 Phi_P^2 + sum_Q nu^2 Phi^2, nu = |zeta|/Phi^2, M = th/(A+th), C = A/(A+th).
Levers: Z-con (inward z-move for P<=0, bank for P>0) and TU (fixed pull flip + pull mass 24 lam v, bank beta(P+2v)).
Checks: (1) Jacobian at P=0 vs I - p q^T; (2) zero P* exists with |P*| <= 2 K_J |F(0)| (Poincare-Miranda radius); (3) nv exact,
statuses kept; (4) gap identity gap' = (C'/C)gap + 1 - C'/C at P*.
"""
import numpy as np
from scipy.optimize import fsolve

rng = np.random.default_rng(7)

def block_norming(zeta, Phi):
    nu = np.abs(zeta)/Phi**2
    def G(th):
        P = nu >= th
        A = (Phi[P]**2*(nu[P] - th)).sum()
        return A*A - th*th*(Phi[P]**2).sum() - (nu[~P]**2*Phi[~P]**2).sum()
    lo, hi = 0.0, nu.max()
    for _ in range(300):
        mid = 0.5*(lo+hi)
        if G(mid) > 0: lo = mid
        else: hi = mid
    th = 0.5*(lo+hi)
    P = nu >= th
    A = (Phi[P]**2*(nu[P]-th)).sum()
    M = th/(A+th); C = A/(A+th)
    w = np.where(P, np.sign(zeta)*M, C*zeta/(Phi**2*A))
    return dict(w=w, A=A, M=M, C=C, th=th, P=P, nu=nu)

class Model:
    def __init__(s, mu, Ucar, blk, Phi):
        s.mu, s.U, s.blk, s.Phi = mu, Ucar, blk, Phi
        s.lam = blk*Phi
    def qstar(s, A): return np.abs(A).sum() + np.linalg.norm(s.mu*A)
    def forced(s, A_un, z):
        nu = np.linalg.norm(s.mu*A_un)
        e = s.mu*A_un/nu
        xh = z + s.mu*e
        val = s.U @ xh
        out = dict(val=val, nu=nu, xh=xh, blocks={})
        for m in np.unique(s.blk):
            idx = np.where(s.blk == m)[0]
            B = block_norming(s.lam[idx]*val[idx], s.Phi[idx]); B['idx'] = idx
            out['blocks'][m] = B
        return out

def build(seed, nfine=2, fineW=1e-6, two_blocks=False):
    r = np.random.default_rng(seed)
    S = 60
    mu = 0.5*0.985**np.arange(S)
    # carriers: block 1: peaks 0,1; Omega 2,3,4; fine 5..; (block 2 copy if two_blocks)
    nb = 2 if two_blocks else 1
    rows, blk, Phi = [], [], []
    sig = {}
    nxt = 12
    for b in range(1, nb+1):
        for k in range(5 + nfine):
            u = np.zeros(S)
            u[:10] = r.normal(size=10)*0.3
            if k < 2:   # peaks: big base overlap
                u[0] += 2.0*(1 if k == 0 else -1); u[1] += 1.0
                ph = 0.05 + 0.02*k
            elif k < 5: # Omega carriers: private signature set (6 coords with geometric v)
                ss = list(range(nxt, nxt+6)); nxt += 6
                u[ss] = 0.25*2.0**(-np.arange(6))
                sig[(b, k)] = ss
                ph = 0.03 + 0.01*k
            else:       # fine carriers: meet lever coordinates of Omega carriers
                ph = fineW*(1 + k)
                tgt = sig[(b, 2 + (k % 3))]
                u[tgt[1:4]] += r.normal(size=3)*0.5
            rows.append(u); blk.append(b); Phi.append(ph)
    U = np.array(rows); blk = np.array(blk); Phi = np.array(Phi)
    # normalize q*(u) = 1
    for i in range(len(U)):
        U[i] /= np.abs(U[i]).sum() + np.linalg.norm(mu*U[i])
    # row: support F = {0,1}, z: base-region contacts/free random, signature coords contacts z = +1 (eps = +1)
    A0 = np.zeros(S); A0[0] = 0.6; A0[1] = -0.3
    z0 = np.zeros(S); z0[0] = 1; z0[1] = -1
    z0[2:10] = np.clip(r.normal(size=8)*0.7, -1, 1); z0[3] = 1.0; z0[5] = -1.0   # 3,5 contacts
    z0[12:nxt] = 1.0
    return Model(mu, U, blk, Phi), A0, z0, sig, S

def run(seed, two_blocks=False, mass=2e-6, cut=59, verbose=True):
    md, A0, z0, sig, S = build(seed, two_blocks=two_blocks)
    D0 = md.forced(A0, z0)
    # Omega = strict non-peaks among coarse carriers 2,3,4 (check statuses)
    Om = []
    for (b, k), ss in sig.items():
        idx = b*0 + k + (b-1)*7
        B = D0['blocks'][b]; pos = list(B['idx']).index(idx)
        if not B['P'][pos]: Om.append((idx, b, ss))
    # pre-row: theta masses at contacts 3 (sign +), 5 (sign -), cut-off beyond `cut`
    A1 = A0.copy(); A1[3] += mass; A1[5] -= 0.5*mass
    z1 = z0.copy(); z1[cut:] = 0.0
    # levers: first Omega carrier gets TU (pull = 5th sig coord, bank = 2nd), others Z-con at 2nd sig coord (eps = +1)
    lev = []
    for n, (idx, b, ss) in enumerate(Om):
        v = md.U[idx]
        if n == 0: lev.append(('TU', idx, b, ss[1], ss[4], v))
        else:      lev.append(('Z', idx, b, ss[1], None, v))
    nu1 = np.linalg.norm(md.mu*A1)
    def row_of(P):
        A = A1.copy(); z = z1.copy()
        for (typ, idx, b, j, jp, v), p in zip(lev, P):
            if typ == 'Z':
                if p <= 0: z[j] = 1.0 - abs(p)/v[j]
                else: A[j] += nu1/(md.mu[j]**2*v[j])*p
            else:
                z[jp] = -1.0; A[jp] += -24*md.lam[idx]*v[jp]
                A[j] += nu1/(md.mu[j]**2*v[j])*(p + 2*v[jp])
        return A, z
    def F(P):
        A, z = row_of(P); D = md.forced(A, z)
        out = []
        for (typ, idx, b, j, jp, v) in lev:
            B, B0 = D['blocks'][b], D0['blocks'][b]
            out.append(D['val'][idx] - B['A']/B0['A']*D0['val'][idx])
        return np.array(out)
    P0 = np.zeros(len(lev)); F0 = F(P0)
    # Jacobian vs I - p q^T
    h = 1e-7; J = np.zeros((len(lev), len(lev)))
    for i in range(len(lev)):
        e = np.zeros(len(lev)); e[i] = h
        J[:, i] = (F(e) - F(-e))/(2*h)
    p = np.array([D0['val'][idx]/D0['blocks'][b]['A'] for (_, idx, b, *_ ) in lev])
    q = np.array([md.lam[idx]*D0['blocks'][b]['w'][list(D0['blocks'][b]['idx']).index(idx)] for (_, idx, b, *_ ) in lev])
    same = np.array([[1.0 if lev[i][2] == lev[k][2] else 0.0 for k in range(len(lev))] for i in range(len(lev))])
    Jth = np.eye(len(lev)) - np.outer(p, q)*same
    Amin = min(B['A'] for B in D0['blocks'].values())
    KJ = 1 + 2/Amin
    Pst = fsolve(F, P0, xtol=1e-15)
    res = F(Pst)
    A, z = row_of(Pst); D = md.forced(A, z)
    nv_err = max(abs(md.lam[idx]*D['val'][idx]/D['blocks'][b]['A'] - md.lam[idx]*D0['val'][idx]/D0['blocks'][b]['A']) for (_, idx, b, *_ ) in lev)
    status_ok = all((D['blocks'][b]['P'] == D0['blocks'][b]['P'])[:5].all() for b in D0['blocks'])
    # gap identity check at P*
    gap_err = 0.0
    for (_, idx, b, *_ ) in lev:
        B, B0 = D['blocks'][b], D0['blocks'][b]; pos = list(B0['idx']).index(idx)
        g0 = B0['M'] - abs(B0['w'][pos]); g1 = B['M'] - abs(B['w'][pos])
        gap_err = max(gap_err, abs(g1 - ((B['C']/B0['C'])*g0 + 1 - B['C']/B0['C'])))
    qTp = max(abs((p*q*same[i]).sum()) for i in range(len(lev)))
    if verbose:
        print(f"seed {seed} blocks {len(D0['blocks'])} |Omega| {len(lev)}  |F(0)| {abs(F0).max():.3e}  ||J - (I-pq^T)|| {abs(J-Jth).max():.2e}"
              f"  q^Tp {qTp:.3f} (C={max(B['C'] for B in D0['blocks'].values()):.3f})")
        print(f"   |P*| {abs(Pst).max():.3e}  2K_J|F(0)| {2*KJ*abs(F0).max():.3e}  ratio {abs(Pst).max()/(2*KJ*abs(F0).max()):.3f}"
              f"  res {abs(res).max():.1e}  nv_err {nv_err:.1e}  statuses kept {status_ok}  gap-identity err {gap_err:.1e}")
    return abs(Pst).max()/(2*KJ*abs(F0).max()), abs(J-Jth).max()

if __name__ == '__main__':
    worst = 0; jw = 0
    for sd in range(16):
        for tb in (False, True):
            try:
                rt, je = run(sd, two_blocks=tb)
                worst = max(worst, rt); jw = max(jw, je)
            except Exception as ex:
                print('seed', sd, tb, 'error', ex)
    print(f"WORST |P*|/(2 K_J |F(0)|) = {worst:.3f} (Poincare-Miranda radius respected iff <= 1);  worst Jacobian deviation {jw:.2e}")
