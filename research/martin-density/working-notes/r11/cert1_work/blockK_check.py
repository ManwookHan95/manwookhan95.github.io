# cert1 (Round 11): independent block solver (primal-dual via outer concave maximization over M)
# Checks: lem:threshold structure, (E2), alpha-mass identity sum_P (rho-1)Phi^2 = C/M, Lemma K closed form,
# K1 (Omega meeting P), E5 interiority 1 - R^2 >= sigma, monotonicity of K, Lemma F floor inequality.
import mpmath as mp, random
mp.mp.dps = 60

def inner(M, zeta, Phi):
    """max sum w_k zeta_k s.t. |w_k|<=M, sum Phi_k^2 w_k^2 <= (1-M)^2 ; returns value, w"""
    C = 1 - M
    n = len(zeta)
    box = mp.fsum(Phi[k]**2 * M**2 for k in range(n))
    if box <= C**2:
        w = [M * mp.sign(zeta[k]) for k in range(n)]
        return mp.fsum(abs(zeta[k]) * M for k in range(n)), w
    # w_k = sgn min(M, t |zeta_k|/Phi_k^2), find t with sum Phi^2 w^2 = C^2
    def g(t):
        return mp.fsum(Phi[k]**2 * min(M, t * abs(zeta[k]) / Phi[k]**2)**2 for k in range(n)) - C**2
    lo, hi = mp.mpf(0), mp.mpf(1)
    while g(hi) < 0:
        hi *= 2
    for _ in range(260):
        mid = (lo + hi) / 2
        if g(mid) < 0: lo = mid
        else: hi = mid
    t = (lo + hi) / 2
    w = [mp.sign(zeta[k]) * min(M, t * abs(zeta[k]) / Phi[k]**2) for k in range(n)]
    return mp.fsum(w[k] * zeta[k] for k in range(n)), w

def solve(zeta, Phi):
    gr = (mp.sqrt(5) - 1) / 2
    a, b = mp.mpf('1e-40'), 1 - mp.mpf('1e-40')
    c = b - gr * (b - a); d = a + gr * (b - a)
    fc = inner(c, zeta, Phi)[0]; fd = inner(d, zeta, Phi)[0]
    for _ in range(300):
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a); fc = inner(c, zeta, Phi)[0]
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a); fd = inner(d, zeta, Phi)[0]
    M = (a + b) / 2
    A, w = inner(M, zeta, Phi)
    return A, M, w

def K(s, x):
    return (s + mp.sqrt(s**2 * x + s * (1 - x))) / (1 - x)

random.seed(20261010)
maxerr = {'thr': 0, 'E2': 0, 'alpha': 0, 'K': 0, 'K1': 0, 'rho': 0}
minE5 = mp.inf; minE5b = mp.inf; mono_ok = True; floor_ok = True
nblocks = 0
for trial in range(40):
    m = random.randint(1, 4)
    n = random.randint(4, 8)
    Phi = [mp.mpf(2)**(-m - k - 1) * mp.mpf(random.uniform(0.3, 1.0)) for k in range(n)]
    x = [mp.mpf(random.uniform(-1, 1)) for k in range(n)]
    zeta = [m * Phi[k] * x[k] for k in range(n)]
    A, M, w = solve(zeta, Phi)
    C = 1 - M
    theta = A * M / C
    nu = [abs(zeta[k]) / Phi[k]**2 for k in range(n)]
    rho = [nu[k] / theta for k in range(n)]
    # threshold structure |w_k| = M min(1, rho_k)
    e = max(abs(abs(w[k]) - M * min(1, rho[k])) for k in range(n))
    maxerr['thr'] = max(maxerr['thr'], e)
    P = [k for k in range(n) if rho[k] >= 1]
    Q = [k for k in range(n) if rho[k] < 1]
    PhiP2 = mp.fsum(Phi[k]**2 for k in P)
    e2 = abs(A**2 - theta**2 * PhiP2 - mp.fsum(nu[k]**2 * Phi[k]**2 for k in Q))
    maxerr['E2'] = max(maxerr['E2'], e2 / A**2)
    alpha = mp.fsum((rho[k] - 1) * Phi[k]**2 for k in P)
    maxerr['alpha'] = max(maxerr['alpha'], abs(alpha - C / M) / (C / M))
    a = A / theta
    # Lemma K with random Omega subset of Q
    if len(Q) >= 1:
        Om = [k for k in Q if random.random() < 0.7] or [Q[0]]
        kappa = (A * (A + theta) - mp.fsum(nu[k]**2 * Phi[k]**2 for k in Om)) / theta
        u = [zeta[k] / (m * Phi[k]) for k in range(n)]
        r = {k: u[k] / kappa for k in Om}
        R2 = m**2 * mp.fsum(r[k]**2 for k in Om)
        sf = mp.fsum(nu[k]**2 * Phi[k]**2 for k in Q if k not in Om) / theta**2
        sigma = PhiP2 + sf
        kk = kappa / theta
        maxerr['K'] = max(maxerr['K'], abs(kk - K(sigma, R2)) / kk)
        for l in Om:
            maxerr['rho'] = max(maxerr['rho'], abs(rho[l] - m * abs(r[l]) * kk / Phi[l]) / rho[l])
        minE5 = min(minE5, (1 - R2) - sigma)
        # E5 formula 1 - R^2 = sigma(1+2a+sigma)/(a+sigma)^2
        minE5b = min(minE5b, abs((1 - R2) - sigma * (1 + 2 * a + sigma) / (a + sigma)**2))
        # monotonicity
        h = mp.mpf('1e-20')
        if not (K(sigma + h, R2) > K(sigma, R2) and K(sigma, min(R2 + h, 1 - h)) > K(sigma, R2)):
            mono_ok = False
        # Lemma F floor: drop part of Omega (inactive) and part of peaks -> floor <= actual
        Oa = [k for k in Om if random.random() < 0.6] or [Om[0]]
        Ra2 = m**2 * mp.fsum(r[k]**2 for k in Oa)
        Prob = [k for k in P if random.random() < 0.7] or P[:1]
        srob = mp.fsum(Phi[k]**2 for k in Prob)
        for l in Oa:
            if m * abs(r[l]) * K(srob, Ra2) / Phi[l] > rho[l] * (1 + mp.mpf('1e-25')):
                floor_ok = False
    # K1: Omega meets P (weak-peak convention): include one peak in Omega
    if len(P) >= 2:
        pk = min(P, key=lambda k: rho[k])
        Om1 = [pk] + [k for k in Q if random.random() < 0.5]
        kappa1 = (A * (A + theta) - mp.fsum(nu[k]**2 * Phi[k]**2 for k in Om1)) / theta
        u = [zeta[k] / (m * Phi[k]) for k in range(n)]
        R2 = m**2 * mp.fsum((u[k] / kappa1)**2 for k in Om1)
        sf = mp.fsum(nu[k]**2 * Phi[k]**2 for k in Q if k not in Om1) / theta**2
        sig1 = mp.fsum(Phi[k]**2 for k in P if k not in Om1) + mp.fsum((1 - rho[k]**2) * Phi[k]**2 for k in Om1 if k in P) + sf
        kk1 = kappa1 / theta
        if sig1 > 0:
            maxerr['K1'] = max(maxerr['K1'], abs(kk1 - K(sig1, R2)) / kk1)
    nblocks += 1

print('blocks', nblocks)
for kk_, v in maxerr.items():
    print(kk_, mp.nstr(v, 5))
print('min (1-R^2) - sigma  (E5, must be >= 0):', mp.nstr(minE5, 6))
print('E5 closed-form residual:', mp.nstr(minE5b, 5))
print('monotonicity ok:', mono_ok, ' Lemma F floor ok:', floor_ok)
