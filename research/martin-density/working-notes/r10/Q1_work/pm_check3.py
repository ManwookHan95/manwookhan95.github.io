"""Q1 sanity check of Lemma PM (ii)-(iii), block level (independent code, mpmath 50 digits).
A block: weights Phi_k, data zeta(k) = lambda_k u_k (values), norm |zeta| with dual N(W) = ||W||_inf + ||Phi W||_2.
Threshold equations: A = sum_P Phi^2 (nu - th), A^2 = th^2 Phi_P^2 + sum_Q nu^2 Phi^2, nu = |zeta|/Phi^2, rho = nu/th, M = th/(A+th), C = A/(A+th).
Carriers: robust peaks (rho >= 1.3), Omega = strict non-peaks incl. ONE near-threshold carrier d with rho_d = 1 - mu (mu tiny, Puiseux-type),
fine carriers with total weight W_fine ~ mu^2 (as c_{L+1} <= b^2 <= mu^2/64 in T_fin).
Perturbation: EVERY value moves by a relative amount up to r (r >> mu): this is what masses/levers/cut-off do at the engineered approximant.
d-consistency: the Omega values are then re-set to nv'_k = nv^0_k (nv = zeta/A), i.e. zeta'(k) = nv^0_k A' with A' = |zeta'| (fixed point).
Report: rho_d^0 = 1 - mu, rho_d after the untuned perturbation, rho_d after d-consistency, |C' - C|, and the Lemma PM bound."""
import mpmath as mp, random
mp.mp.dps = 80
random.seed(11)

def solve(zeta, Phi):
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def G(th):
        A = mp.fsum(p**2*(n - th) for n, p in zip(nu, Phi) if n >= th)
        return A*A - th*th*mp.fsum(p**2 for n, p in zip(nu, Phi) if n >= th) - mp.fsum(n**2*p**2 for n, p in zip(nu, Phi) if n < th)
    lo, hi = mp.mpf(0), max(nu)
    for _ in range(520):
        mid = (lo + hi)/2
        if G(mid) > 0: lo = mid
        else: hi = mid
    th = (lo + hi)/2
    A = mp.fsum(p**2*(n - th) for n, p in zip(nu, Phi) if n >= th)
    return dict(A=A, th=th, C=A/(A + th), M=th/(A + th), rho=[n/th for n in nu])

def instance(mu, r, nfine=8):
    nP, nO = 3, 4
    Phi = [mp.mpf(random.uniform(0.15, 0.3)) for _ in range(nP)] + [mp.mpf(random.uniform(0.05, 0.14)) for _ in range(nO)]
    Wf = mu**2
    Phi += [Wf*mp.mpf(2)**(-i - 1) for i in range(nfine)]
    kind = ['P']*nP + ['O']*nO + ['f']*nfine
    # values: choose zeta so that statuses are as wanted, relative to a provisional threshold th0 = 1
    zeta = []
    for k in range(len(Phi)):
        s = random.choice([-1, 1])
        if kind[k] == 'P': rho = random.uniform(1.6, 2.5)
        elif kind[k] == 'O': rho = random.uniform(0.2, 0.8)
        else:
            if k % 2 == 0:
                zeta.append(s*Phi[k]*mp.mpf(random.uniform(0.1, 1))); continue   # realistic fine value: zeta ~ lambda u, nu ~ 1/Phi (peak)
            rho = random.uniform(0.999, 1.001)                                      # fine carrier near ITS threshold: status flips
        zeta.append(s*rho*Phi[k]**2)          # nu = rho at th = 1 (the true th is then computed)
    # tune the near-threshold carrier d (= first Omega carrier) to rho_d = 1 - mu exactly (bisection on its value)
    d = nP
    lo, hi = mp.mpf(0), 4*Phi[d]**2
    for _ in range(190):
        mid = (lo + hi)/2
        z = list(zeta); z[d] = mid*(1 if zeta[d] > 0 else -1)
        if solve(z, Phi)['rho'][d] > 1 - mu: hi = mid
        else: lo = mid
    zeta[d] = (lo + hi)/2*(1 if zeta[d] > 0 else -1)
    S0 = solve(zeta, Phi)
    if not all((S0['rho'][k] >= 1.2) for k in range(nP)) or not all(S0['rho'][k] < 1 for k in range(nP, nP + nO)):
        return None
    # perturbation of every value by a relative amount <= r
    z1 = [z*(1 + mp.mpf(random.uniform(-1, 1))*r) for z in zeta]
    Su = solve(z1, Phi)
    # d-consistency on Omega: zeta'(k) = nv0_k A' (fixed point in A')
    nv0 = {k: zeta[k]/S0['A'] for k in range(nP, nP + nO)}
    A_ = Su['A']
    for it in range(200):
        z2 = list(z1)
        for k in nv0: z2[k] = nv0[k]*A_
        S2 = solve(z2, Phi)
        if abs(S2['A'] - A_) < mp.mpf(10)**(-72): break
        A_ = S2['A']
    res = max(abs(z2[k]/S2['A'] - nv0[k]) for k in nv0)
    # CONTROL: d-consistency on Omega minus its last carrier (a coarse strict non-peak left untuned)
    nv0c = {k: nv0[k] for k in list(nv0)[:-1]}
    A_ = Su['A']
    for it2 in range(200):
        z3 = list(z1)
        for k in nv0c: z3[k] = nv0c[k]*A_
        S3 = solve(z3, Phi)
        if abs(S3['A'] - A_) < mp.mpf(10)**(-72): break
        A_ = S3['A']
    # Lemma PM(ii) bound: |C'-C| <= (2(1-C)/C) sum_fine |d|nv|| / slope, slope = 2 Phi_*^2 (1-C)/C^3 (Phi_* = heaviest peak)
    C = S0['C']; Phis = max(Phi[:nP])
    fine = [k for k in range(len(Phi)) if kind[k] == 'f']
    dv = mp.fsum(abs(abs(z2[k])/S2['A'] - abs(zeta[k])/S0['A']) for k in fine)
    bound = (2*(1 - C)/C)*dv/(2*Phis**2*(1 - C)/C**3)
    return dict(mu=mu, r=r, rho0=S0['rho'][d], rhou=Su['rho'][d], rho2=S2['rho'][d], dC=abs(S2['C'] - C), dCu=abs(Su['C'] - C),
                bound=bound, res=res, Wf=mp.fsum(Phi[k] for k in fine), its=it, dCc=abs(S3['C'] - C), rhoc=S3['rho'][d],
                flips=sum(1 for k in fine if (S0['rho'][k] >= 1) != (S2['rho'][k] >= 1)))

print('mu  r | rho_d(f0) | rho_d untuned | rho_d d-consistent | |C1-C0| (untuned) | PM bound | nv resid | W_fine | fine flips | CONTROL (Omega minus one): |C1-C0|, 1-rho_d')
for mu, r in (('1e-8', '1e-3'), ('1e-12', '1e-4'), ('1e-16', '1e-2'), ('1e-20', '1e-5')):
    mu = mp.mpf(mu); r = mp.mpf(r); n = 0; tries = 0
    while n < 3 and tries < 60:
        tries += 1
        o = instance(mu, r)
        if o is None: continue
        n += 1
        print('%-6s %-6s | 1-%.3e | %s | 1-%.6e | %.2e (%.2e) | %.2e | %.1e | %.1e | %d | %.2e, %s' % (mp.nstr(mu, 2), mp.nstr(r, 2), 1 - o['rho0'],
              ('1-%.3e' % (1 - o['rhou'])) if o['rhou'] < 1 else ('1+%.3e PEAK' % (o['rhou'] - 1)), 1 - o['rho2'], o['dC'], o['dCu'],
              o['bound'], o['res'], o['Wf'], o['flips'], o['dCc'], ('%.3e' % (1 - o['rhoc'])) if o['rhoc'] < 1 else ('PEAK +%.2e' % (o['rhoc'] - 1))), flush=True)
