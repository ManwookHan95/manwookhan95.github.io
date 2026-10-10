"""U4-ref: independent HIGH-PRECISION check of V1 Lemma TU (pulls + private banks + explicit scalar fixed point) with the
ACTUAL base mu_s = 2^{-s^2-1} and bank coordinates far enough out that mu_{j'}^2 is super-exponentially small
(j' in {8,...,14}: mu^2 between 2^{-130} and 2^{-394}).  U4's tu_mu_check.py used s_j = 2^{-beta j^2} with beta ~ 0.004 and
banks at j' ~ 11-13, i.e. s'^2 in [0.25, 0.7]: it did not exercise the super-exponential regime that conflict C1 is about.

Model (as in V1 3.4): base support F = {1,2,3}; carriers l in L0 with private signature sets S_l (bounded gaps), v_l(s) = d_l 2^{-s},
exactly swallowed (z = eps_l on S_l); coarse target coordinates T in [4, s0-1]; 'other' carriers supported on F u T.
Pull at j_l in S_l with v_l(j_l) in [eta, 2^{gap} eta] (mass 24 lambda_l v_l(j_l), z_j := -eps_l); bank at j'_l = min S_l.
Reported: exactness of val^# - val^(2) = x; second-order motion of other carriers; contraction |Phi'| at the fixed point;
all in units of reg := min_l mu_{j'_l}^2 v_l(j'_l)^2 (the quantity bounded below by (4/5)^2 delta_min^2 / (B_mu 2^sigma) ).
Expected (V1-ref (p4) with the mu-base): |Phi'| ~ eta/reg, other motion ~ eta^2/reg, failure once eta >> reg."""
import mpmath as mp, random, sys
mp.mp.prec = 3000
random.seed(7)

def mu(s):
    return mp.mpf(2) ** (-(s * s) - 1)

def run(s0, nL, fac, gapmul=2):
    G = nL * gapmul
    d = [mp.mpf(random.uniform(0.2, 0.6)) for _ in range(nL)]
    lam = [mp.mpf(random.uniform(0.05, 0.25)) for _ in range(nL)]
    eps = [random.choice([-1, 1]) for _ in range(nL)]
    jprime = [s0 + l for l in range(nL)]
    reg = min(mu(jprime[l]) ** 2 * (d[l] * mp.mpf(2) ** (-jprime[l])) ** 2 for l in range(nL))
    eta = mp.mpf(fac) * reg
    # pull coordinates: first s in S_l beyond j' with v in [eta, 2^G eta]
    pull = []
    for l in range(nL):
        s = jprime[l] + G
        while d[l] * mp.mpf(2) ** (-s) > (mp.mpf(2) ** G) * eta:
            s += G
        if d[l] * mp.mpf(2) ** (-s) < eta:
            return None
        pull.append(s)
    n = max(pull) + 2
    F = [1, 2, 3]
    T = random.sample(range(4, s0), min(3, s0 - 4))
    A2 = {s: mp.mpf(random.gauss(0, 1)) for s in F}
    z2 = {s: (1 if A2[s] > 0 else -1) for s in F}
    for j in T:
        z2[j] = mp.mpf(random.uniform(-0.9, 0.9))
    U = []
    for l in range(nL):
        u = {s: mp.mpf(random.gauss(0, 1)) * mp.mpf('0.2') for s in F}
        for j in T:
            u[j] = mp.mpf(random.gauss(0, 1)) * mp.mpf('0.2')
        s = jprime[l]
        while s <= n:
            u[s] = d[l] * mp.mpf(2) ** (-s)
            z2[s] = eps[l]
            s += G
        U.append(u)
    others = []
    for k in range(3):
        u = {s: mp.mpf(random.gauss(0, 1)) * mp.mpf('0.2') for s in F}
        for j in T:
            u[j] = mp.mpf(random.gauss(0, 1)) * mp.mpf('0.2')
        others.append(u)

    def nu_of(A):
        return mp.sqrt(mp.fsum((mu(s) * a) ** 2 for s, a in A.items()))

    def val(u, A, z, sign=1):
        nu = nu_of(A)
        tot = mp.mpf(0)
        for s, c in u.items():
            zh = mp.mpf(z.get(s, 0)) + (mu(s) ** 2 * A[s] / nu if s in A else 0)
            tot += c * zh
        return sign * tot

    x = [mp.mpf(random.uniform(-1, 1)) * eta for _ in range(nL)]
    val2 = [val(U[l], A2, z2, eps[l]) for l in range(nL)]
    oth2 = [val(u, A2, z2) for u in others]
    # pulls
    Ap = dict(A2); zp = dict(z2)
    for l in range(nL):
        Ap[pull[l]] = -eps[l] * 24 * lam[l] * U[l][pull[l]]
        zp[pull[l]] = -eps[l]
    nup = nu_of(Ap)
    valp = [val(U[l], Ap, zp, eps[l]) for l in range(nL)]
    beta = [eps[l] * mp.fsum(mu(s) ** 2 * U[l].get(s, 0) * a for s, a in Ap.items()) / nup for l in range(nL)]
    Delta = [x[l] + val2[l] - valp[l] for l in range(nL)]
    sp = [mu(jprime[l]) for l in range(nL)]
    vp = [U[l][jprime[l]] for l in range(nL)]
    def mfun(y):
        return [(Delta[l] * y + beta[l] * (y - nup)) / (sp[l] ** 2 * vp[l]) for l in range(nL)]
    def Phi(y):
        m = mfun(y)
        return mp.sqrt(nup ** 2 + mp.fsum((sp[l] * m[l]) ** 2 for l in range(nL)))
    def dPhi(y):
        m = mfun(y)
        return mp.fsum(sp[l] ** 2 * m[l] * (Delta[l] + beta[l]) / (sp[l] ** 2 * vp[l]) for l in range(nL)) / Phi(y)
    y = nup
    conv = False
    for it in range(4000):
        y1 = Phi(y)
        if abs(y1 - y) < nup * mp.mpf(10) ** (-850):
            y = y1; conv = True; break
        if y1 > 1e6 * nup:
            break
        y = y1
    lip = abs(dPhi(y))
    if not conv:
        return ('diverge', float(lip), float(eta / reg))
    m = mfun(y)
    A = dict(Ap)
    for l in range(nL):
        A[jprime[l]] = m[l] * eps[l]
    valh = [val(U[l], A, zp, eps[l]) for l in range(nL)]
    othh = [val(u, A, zp) for u in others]
    exact = max(abs(valh[l] - val2[l] - x[l]) for l in range(nL)) / eta
    other = max(abs(othh[k] - oth2[k]) for k in range(len(others)))
    massok = min(m) > 0
    return ('ok', float(lip), float(lip * reg / eta), float(exact), float(other / eta), float(other * reg / eta ** 2),
            bool(massok), float(max(m) * reg / eta), float(eta / reg))

if __name__ == '__main__':
    rows = []
    for s0 in [8, 10, 12, 14]:
        for nL in [1, 2, 3]:
            for fac in ['1e-3', '1e-2', '1e-1', '1', '10', '100']:
                r = run(s0, nL, fac)
                rows.append((s0, nL, fac, r))
                print(s0, nL, fac, r); sys.stdout.flush()
