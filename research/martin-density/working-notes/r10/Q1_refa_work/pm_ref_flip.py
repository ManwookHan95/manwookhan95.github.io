"""Referee (a) independent check of Lemma PM (ii)-(iii) with a DIFFERENT block solver.
Block norm |zeta| = sup{<w,zeta> : ||w||_inf + ||D w||_2 <= 1}.  For fixed M = ||w||_inf the inner problem is solved in closed form
(w_k = sgn zeta_k min(M, t nu_k), nu_k = |zeta_k|/Phi_k^2, t from sum Phi_k^2 min(M, t nu_k)^2 = (1-M)^2, by sorting), and the outer
concave maximization over M is solved by bisection on the envelope derivative
    A'(M) = sum_{clamped} (|zeta_k| - Phi_k^2 M/t) - (1 - M)/t.
Statuses: peak iff t nu_k >= M; rho_k = t nu_k / M; C = 1 - M; nv_k = zeta_k/A.
Test (worst case for Lemma PM): Omega = coarse strict non-peaks incl. one near-threshold d (rho_d = 1 - mu); coarse peaks robust;
fine carriers (tiny weights, total ~ W).  Perturbation: coarse peaks relative r; FINE values ARBITRARY (absolute moves of size up to
2 lambda_k, statuses may flip); then d-consistency on Omega (fixed point zeta'_k = nv_k A').  Report |C'-C|/W_fine and the identity
rho'_k/rho_k = [C'/(1-C')]/[C/(1-C)] on Omega.  Control: one Omega carrier left untuned."""
import mpmath as mp, random
mp.mp.dps = 64
random.seed(23)

def tofM(M, nu, Phi):
    # solve sum Phi^2 min(M, t nu)^2 = (1-M)^2 for t
    idx = sorted(range(len(nu)), key=lambda k: -nu[k])
    S = mp.mpf(0)                      # sum Phi^2 over clamped
    Q = mp.fsum(nu[k]**2*Phi[k]**2 for k in idx)   # sum nu^2 Phi^2 over unclamped
    R = (1 - M)**2
    for j in range(len(idx) + 1):
        # j clamped (the top j)
        if j > 0:
            k = idx[j-1]; S += Phi[k]**2
        if j == len(idx):
            return None
        Q = mp.fsum(nu[kk]**2*Phi[kk]**2 for kk in idx[j:])
        num = R - M*M*S
        if num <= 0:
            return None
        if Q <= 0:
            continue
        t = mp.sqrt(num/Q)
        top_ok = (j == 0) or (t*nu[idx[j-1]] >= M*(1 - mp.mpf(10)**(-58)))
        nxt_ok = t*nu[idx[j]] <= M*(1 + mp.mpf(10)**(-58))
        if top_ok and nxt_ok:
            return t
    # fallback: direct bisection in t (F(t) increasing); used only near status changes / rounding ties
    tot = M*M*mp.fsum(p**2 for p in Phi)
    if tot <= R:
        return None
    lo_t, hi_t = mp.mpf(0), mp.mpf(1)
    while mp.fsum(p**2*min(M, hi_t*n)**2 for n, p in zip(nu, Phi)) < R:
        hi_t *= 2
    for _ in range(400):
        mid_t = (lo_t + hi_t)/2
        if mp.fsum(p**2*min(M, mid_t*n)**2 for n, p in zip(nu, Phi)) < R: lo_t = mid_t
        else: hi_t = mid_t
    return (lo_t + hi_t)/2

def solve(zeta, Phi):
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def g(M):
        t = tofM(M, nu, Phi)
        if t is None:
            return mp.mpf(1)           # M < 1/(1+||Phi||_2): l2 constraint slack, A(M) = M ||zeta||_1 increasing
        return mp.fsum(abs(z) - p**2*M/t for z, p, n in zip(zeta, Phi, nu) if t*n >= M) - (1 - M)/t
    lo, hi = mp.mpf(0), mp.mpf(1)
    for _ in range(230):
        mid = (lo + hi)/2
        if g(mid) > 0: lo = mid
        else: hi = mid
    M = (lo + hi)/2
    t = tofM(M, nu, Phi)
    if t is None:                      # corner solution: every carrier clamped (all peaks), t = +infinity
        t = mp.inf
    A = mp.fsum(abs(z)*min(M, t*n) for z, n in zip(zeta, nu))
    C = 1 - M
    rho = [t*n/M for n in nu]
    return dict(A=A, C=C, M=M, t=t, rho=rho)

def instance(mu, r, W):
    nP, nO, nF = 3, 4, 10
    Phi = [mp.mpf(random.uniform(0.12, 0.3)) for _ in range(nP)] + [mp.mpf(random.uniform(0.04, 0.11)) for _ in range(nO)]
    Phi += [W*mp.mpf(2)**(-i - 1) for i in range(nF)]
    m = 1  # block index (lambda = m Phi)
    kind = ['P']*nP + ['O']*nO + ['f']*nF
    zeta = []
    for k in range(len(Phi)):
        s = random.choice([-1, 1])
        if kind[k] == 'P': zeta.append(s*mp.mpf(random.uniform(1.6, 2.5))*Phi[k]**2)
        elif kind[k] == 'O': zeta.append(s*mp.mpf(random.uniform(0.2, 0.8))*Phi[k]**2)
        else: zeta.append(s*m*Phi[k]*mp.mpf(random.uniform(0, 1.5)) if k % 2 == 0 else s*mp.mpf(random.uniform(0.5, 1.5))*Phi[k]**2)
    target = [None]*len(Phi)
    for k in range(nP + nO):
        target[k] = abs(zeta[k])/Phi[k]**2          # intended rho at theta = 1
    for _ in range(4):                               # rescale coarse values so that rho = target at the actual threshold
        S = solve(zeta, Phi); th = S['M']/S['t']
        for k in range(nP + nO):
            zeta[k] = (1 if zeta[k] > 0 else -1)*target[k]*th*Phi[k]**2
    S = solve(zeta, Phi)
    if not all(S['rho'][k] >= 1.2 for k in range(nP)) or not all(S['rho'][k] < 1 for k in range(nP, nP + nO)):
        return None
    d = nP
    lo, hi = mp.mpf(0), 4*Phi[d]**2*S['M']/S['t']
    sgn = 1 if zeta[d] > 0 else -1
    for _ in range(150):
        mid = (lo + hi)/2
        z = list(zeta); z[d] = sgn*mid
        if solve(z, Phi)['rho'][d] > 1 - mu: hi = mid
        else: lo = mid
    zeta[d] = sgn*(lo + hi)/2
    S0 = solve(zeta, Phi)
    if not all(S0['rho'][k] >= 1.2 for k in range(nP)) or not all(S0['rho'][k] < 1 for k in range(nP, nP + nO)):
        return None
    # identity check of lem:threshold: t = C/A
    ident = abs(S0['t'] - S0['C']/S0['A'])
    Om = list(range(nP, nP + nO))
    nv0 = {k: zeta[k]/S0['A'] for k in Om}
    z1 = list(zeta)
    for k in range(nP): z1[k] = zeta[k]*(1 + mp.mpf(random.uniform(-1, 1))*r)
    th0 = S0['M']/S0['t']
    for k in range(nP + nO, len(Phi)):
        if k % 2 == 0: z1[k] = random.choice([-1, 1])*m*Phi[k]*mp.mpf(random.uniform(0, 2))          # arbitrary fine values
        else: z1[k] = random.choice([-1, 1])*mp.mpf(random.uniform(0.5, 1.5))*th0*Phi[k]**2          # near-threshold fine carriers (flips)
    for k in Om: z1[k] = zeta[k]*(1 + mp.mpf(random.uniform(-1, 1))*r)
    def dcons(Oset):
        A_ = solve(z1, Phi)['A']
        for it in range(300):
            z2 = list(z1)
            for k in Oset: z2[k] = nv0[k]*A_
            S2 = solve(z2, Phi)
            if abs(S2['A'] - A_) < mp.mpf(10)**(-55): break
            A_ = S2['A']
        return z2, S2
    z2, S2 = dcons(Om)
    z3, S3 = dcons(Om[:-1])
    C, C2 = S0['C'], S2['C']
    fac = (C2/(1 - C2))/(C/(1 - C))
    idres = max(abs(S2['rho'][k]/S0['rho'][k] - fac) for k in Om)
    Wf = mp.fsum(Phi[k] for k in range(nP + nO, len(Phi)))
    flips = sum(1 for k in range(nP + nO, len(Phi)) if (S0['rho'][k] >= 1) != (S2['rho'][k] >= 1))
    Phis = max(Phi[:nP])
    sumnv = mp.fsum(abs(z2[k])/S2['A'] + abs(zeta[k])/S0['A'] for k in range(nP + nO, len(Phi)))
    bound = (2*(1 - C)/C)*sumnv/(2*Phis**2*(1 - C)/C**3)
    return dict(ident=ident, dC=abs(C2 - C), Wf=Wf, bound=bound, idres=idres, rho_d=S2['rho'][d], flips=flips,
                dCc=abs(S3['C'] - C), rho_dc=S3['rho'][d])

print('mu, r, W | t-C/A | |C1-C0| | /W_fine | PM bound | identity resid | 1 - rho_d (tuned) | fine flips | CONTROL |C1-C0|, rho_d')
for mu, r, W in (('1e-6', '1e-2', '1e-14'), ('1e-9', '1e-3', '1e-20'), ('1e-12', '1e-2', '1e-26')):
    mu, r, W = mp.mpf(mu), mp.mpf(r), mp.mpf(W)
    n = tries = 0
    while n < 3 and tries < 40:
        tries += 1
        o = instance(mu, r, W)
        if o is None: continue
        n += 1
        print('%s %s %s | %.1e | %.2e | %.2f | %.2e | %.1e | %s | %d | %.2e, %s' % (mp.nstr(mu, 2), mp.nstr(r, 2), mp.nstr(W, 2), o['ident'], o['dC'],
              o['dC']/o['Wf'], o['bound'], o['idres'], mp.nstr(1 - o['rho_d'], 6), o['flips'], o['dCc'],
              ('1-%s' % mp.nstr(1 - o['rho_dc'], 3)) if o['rho_dc'] < 1 else ('PEAK +%s' % mp.nstr(o['rho_dc'] - 1, 3))), flush=True)
