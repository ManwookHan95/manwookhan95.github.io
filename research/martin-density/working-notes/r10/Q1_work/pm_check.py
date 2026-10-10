"""Q1 sanity check of Lemma PM (part 2.4): at a d-consistent approximant the statuses of the switching carriers are frozen up to the
fine carriers, so a near-threshold carrier with a TINY margin mu (Puiseux-type) keeps its margin although the perturbation (masses ->
Hilbert part -> all values) moves values by r >> mu.  Independent model written from scratch (mpmath, 60 digits), one or two blocks,
diagonal base.  Block norm: dual N(W) = ||W||_inf + ||Phi W||_2; norming functional via the threshold equations (E1), (E2):
   A = sum_P Phi^2 (nu - th),  A^2 = th^2 Phi_P^2 + sum_Q nu^2 Phi^2,  nu_k = |zeta_k|/Phi_k^2,  M = th/(A+th), C = A/(A+th).
Checks: (1) clamp equation sum_k min(Phi_k (1-C)/C, v_k)^2 = 1 (v_k = |nv_k|/Phi_k); (2) exact d-consistency by private levers (Newton);
(3) |C' - C| versus the fine-carrier bound of Lemma PM(ii); (4) rho_d before / after perturbation (untuned) / after tuning."""
import mpmath as mp
import random
mp.mp.dps = 60
random.seed(7)

def block(zeta, Phi):
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def G(th):
        P = [n >= th for n in nu]
        A = mp.fsum(p**2*(n - th) for n, p, b in zip(nu, Phi, P) if b)
        return A*A - th*th*mp.fsum(p**2 for p, b in zip(Phi, P) if b) - mp.fsum(n**2*p**2 for n, p, b in zip(nu, Phi, P) if not b)
    lo, hi = mp.mpf(0), max(nu)
    for _ in range(260):
        mid = (lo + hi)/2
        if G(mid) > 0: lo = mid
        else: hi = mid
    th = (lo + hi)/2
    P = [n >= th for n in nu]
    A = mp.fsum(p**2*(n - th) for n, p, b in zip(nu, Phi, P) if b)
    M = th/(A + th); C = A/(A + th)
    return dict(A=A, M=M, C=C, th=th, P=P, nu=nu, rho=[n/th for n in nu])

class Model:
    def __init__(s, nblk=1):
        s.mu = lambda j: mp.mpf(2)**(-mp.mpf(j)/3 - 1)
        s.F = [0, 1]; s.T = list(range(2, 8))
        s.car = []          # (block, Phi, vector dict coord -> entry, kind)
        nxt = 8
        def add(m, Phi, kind, tscale):
            nonlocal nxt
            vec = {j: mp.mpf(random.uniform(-1, 1))*tscale for j in s.F + s.T}
            priv = list(range(nxt, nxt + 3)); nxt += 3
            for i, j in enumerate(priv): vec[j] = mp.mpf(random.uniform(0.2, 0.4))*mp.mpf(2)**(-i)
            q = mp.fsum(abs(v) for v in vec.values()) + mp.sqrt(mp.fsum((s.mu(j)*v)**2 for j, v in vec.items()))
            vec = {j: v/q for j, v in vec.items()}
            s.car.append(dict(m=m, Phi=mp.mpf(Phi), vec=vec, kind=kind, priv=priv))
        for m in range(1, nblk + 1):
            sc = mp.mpf(2)**(-m)
            add(m, 0.30*sc, 'peak', 1); add(m, 0.22*sc, 'peak', 1)
            add(m, 0.15*sc, 'near', 0.3); add(m, 0.12*sc, 'omega', 0.3); add(m, 0.09*sc, 'omega', 0.3)
            for i in range(6): add(m, 1e-6*sc*(0.5**i), 'fine', 0.5)
        s.n = nxt; s.nblk = nblk
    def forced(s, A, z):
        q = mp.fsum(abs(A[j]) for j in A) + mp.sqrt(mp.fsum((s.mu(j)*A[j])**2 for j in A))
        a = {j: A[j]/q for j in A}
        nu = mp.sqrt(mp.fsum((s.mu(j)*a[j])**2 for j in a))
        zhat = dict(z)
        for j in a: zhat[j] = z[j] + s.mu(j)**2*a[j]/nu
        val = [mp.fsum(v*zhat[j] for j, v in c['vec'].items()) for c in s.car]
        out = dict(val=val, blocks={})
        for m in range(1, s.nblk + 1):
            idx = [k for k, c in enumerate(s.car) if c['m'] == m]
            zeta = [m*s.car[k]['Phi']*val[k] for k in idx]
            B = block(zeta, [s.car[k]['Phi'] for k in idx]); B['idx'] = idx
            B['nv'] = {k: m*s.car[k]['Phi']*val[k]/B['A'] for k in idx}
            out['blocks'][m] = B
        return out

def status(Mo, D, k):
    m = Mo.car[k]['m']; B = D['blocks'][m]; i = B['idx'].index(k)
    return B['rho'][i], B['P'][i]

def run(nblk, mu_target, pert):
    Mo = Model(nblk)
    z = {j: mp.mpf(0) for j in range(Mo.n)}
    A = {0: mp.mpf('0.7'), 1: mp.mpf('-0.4')}
    z[0], z[1] = mp.mpf(1), mp.mpf(-1)
    for j in Mo.T: z[j] = mp.mpf(random.choice([-1, 1]))
    for k, c in enumerate(Mo.car):
        sg = 1 if c['kind'] in ('peak',) else random.choice([-1, 1])
        for i, j in enumerate(c['priv']):
            z[j] = mp.mpf(sg) if c['kind'] == 'peak' else mp.mpf(sg)*mp.mpf('0.5')
    # make every 'near' carrier a strict non-peak with rho = 1 - mu_target (tune its last private coordinate by bisection)
    for k, c in enumerate(Mo.car):
        if c['kind'] != 'near': continue
        j = c['priv'][0]
        lo, hi = mp.mpf(-1), mp.mpf(1)
        sgn = 1 if status(Mo, Mo.forced(A, {**z, j: hi}), k)[0] > status(Mo, Mo.forced(A, {**z, j: lo}), k)[0] else -1
        target = 1 - mu_target
        for _ in range(220):
            mid = (lo + hi)/2
            r = status(Mo, Mo.forced(A, {**z, j: mid}), k)[0]
            if (r - target)*sgn > 0: hi = mid
            else: lo = mid
        z[j] = (lo + hi)/2
    D0 = Mo.forced(A, z)
    # sanity: peaks are peaks, omega/near strict non-peaks
    Om = [k for k, c in enumerate(Mo.car) if c['kind'] in ('near', 'omega')]
    for k in Om:
        if status(Mo, D0, k)[1]: return None
    for k, c in enumerate(Mo.car):
        if c['kind'] == 'peak' and not status(Mo, D0, k)[1]: return None
    # clamp-equation check
    clamp = []
    for m, B in D0['blocks'].items():
        Cc = B['C']
        clamp.append(abs(mp.fsum(min(Mo.car[k]['Phi']*(1 - Cc)/Cc, abs(B['nv'][k])/Mo.car[k]['Phi'])**2 for k in B['idx']) - 1))
    # perturbation: masses on two contact coordinates of T (sign of z) + changes of fine carriers' private z
    A1 = dict(A); z1 = dict(z)
    for j in Mo.T[:2]: A1[j] = z[j]*mp.mpf(pert)
    for k, c in enumerate(Mo.car):
        if c['kind'] == 'fine':
            for j in c['priv']: z1[j] = -z[j]
    D1u = Mo.forced(A1, z1)
    # levers: private coordinate priv[1] of every Omega carrier, z-move (free coordinates, |z| = 0.5)
    lev = {k: Mo.car[k]['priv'][1] for k in Om}
    nv0 = {k: D0['blocks'][Mo.car[k]['m']]['nv'][k] for k in Om}
    def Fv(P):
        zz = dict(z1)
        for i, k in enumerate(Om): zz[lev[k]] = z1[lev[k]] + P[i]/Mo.car[k]['vec'][lev[k]]
        D = Mo.forced(A1, zz)
        return [D['blocks'][Mo.car[k]['m']]['nv'][k] - nv0[k] for k in Om], D, zz
    P = [mp.mpf(0)]*len(Om)
    for it in range(12):
        F0, D, zz = Fv(P)
        if max(abs(x) for x in F0) < mp.mpf(10)**(-45): break
        h = mp.mpf(10)**(-25); J = mp.matrix(len(Om), len(Om))
        for i in range(len(Om)):
            Pe = list(P); Pe[i] += h
            Fe = Fv(Pe)[0]
            for r in range(len(Om)): J[r, i] = (Fe[r] - F0[r])/h
        dP = mp.lu_solve(J, mp.matrix(F0))
        P = [P[i] - dP[i] for i in range(len(Om))]
    F1, D1, zz = Fv(P)
    res = max(abs(x) for x in F1)
    if max(abs(zz[j]) for j in zz) > 1: return None
    out = []
    for m in range(1, nblk + 1):
        B0, B1, Bu = D0['blocks'][m], D1['blocks'][m], D1u['blocks'][m]
        kd = [k for k in B0['idx'] if Mo.car[k]['kind'] == 'near'][0]
        r0 = status(Mo, D0, kd)[0]; ru = status(Mo, D1u, kd)[0]; r1 = status(Mo, D1, kd)[0]
        fine = [k for k in B0['idx'] if Mo.car[k]['kind'] == 'fine']
        dv = mp.fsum(abs(abs(B1['nv'][k]) - abs(B0['nv'][k])) for k in fine)
        valmove = max(abs(D1u['val'][k] - D0['val'][k]) for k in B0['idx'])
        out.append(dict(m=m, res=res, dC=abs(B1['C'] - B0['C']), dCu=abs(Bu['C'] - B0['C']), finedv=dv,
                        mu=1 - r0, rho_untuned=ru, rho_tuned=r1, valmove=valmove, clamp=max(clamp)))
    return out

for nblk in (1, 2):
    for mu_target, pert in (('1e-8', '1e-4'), ('1e-12', '1e-3'), ('1e-10', '3e-3')):
        o = None; tries = 0
        while o is None and tries < 20:
            o = run(nblk, mp.mpf(mu_target), pert); tries += 1
        if o is None: print('nblk', nblk, 'no valid instance'); continue
        for d in o:
            print('blocks=%d m=%d mu=%s pert=%s | clamp eq err %.1e | max value move %.2e | nv residual %.1e | |C1-C0| %.2e (untuned %.2e)'
                  ' fine sum|d|nv|| %.2e | rho_d: f0 1-%.2e, untuned %s, tuned 1-%.6e' %
                  (nblk, d['m'], mu_target, pert, d['clamp'], d['valmove'], d['res'], d['dC'], d['dCu'], d['finedv'],
                   d['mu'], mp.nstr(d['rho_untuned'], 12), 1 - d['rho_tuned']))
