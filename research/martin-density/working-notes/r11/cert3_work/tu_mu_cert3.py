"""cert3: independent check of Part II lem:II-TU (explicit two-sided tuning: far pulls + private banks + scalar fixed point
y = M(y)) transplanted to T_fin's base mu_s = 2^{-s^2-1} (||U|| = 1/4).  Follows the PROOF of lem:II-TU literally:
  Step 1 pulls (mass 24 lam v(j), sign flip), Step 2 explicit n(y) = (Delta y + phi (y - nu_p))/(s'^2 v'), M(y) = sqrt(nu_p^2 + sum s'^2 n^2).
Checks: (i) val^# - val^(2) = x exactly (working precision); (ii) |M'| on I = [nu_p, nu_p + kappa_T] vs the proof's bound
B := sum (2 Delta + kappa)(Delta + ||U||)/((s' v')^2 nu); (iii) bank masses > 0; (iv) other carriers move <= C eps_x^2;
(v) T_fin design inequality mu_{j'}^2 v(j') >= (4/5) delta_min / B_mu(l) with B_mu = 2^sigma/mu_sigma^2, sigma = max first element
beyond s_max, and (mu v)^{-2} <= (25/16)(B_mu/delta_min)^2.
Usage: python3 -I tu_mu_cert3.py > tu_mu_cert3b.out"""
import mpmath as mp, random
mp.mp.prec = 2500
random.seed(20261010)
U_NORM = mp.mpf(1) / 4

def mu(s):
    return mp.mpf(2) ** (-(s * s) - 1)

def S(l, upto):
    out, i = [], 1
    while 2 ** l * (2 * i + 1) <= upto:
        out.append(2 ** l * (2 * i + 1)); i += 1
    return out

def ip_e(u, A):
    """<U^* u, U^* A>/||U^* A|| for the diagonal base (exact)."""
    nu = mp.sqrt(sum(mu(s) ** 2 * a ** 2 for s, a in A.items()))
    return sum(u.get(s, 0) * a * mu(s) ** 2 for s, a in A.items()) / nu, nu

def value(u, z, A, eps):
    pe, _ = ip_e(u, A)
    return eps * (sum(u[s] * z.get(s, 0) for s in u) + pe)

def run(smax, k, fac):
    F = [1, 3, 5]
    A2 = {s: mp.mpf(random.choice([-1, 1]) * random.uniform(0.3, 1.0)) for s in F}
    z = {s: (1 if A2[s] > 0 else -1) for s in F}
    d = [mp.mpf(random.uniform(0.1, 0.5)) * mp.mpf(2) ** (-l) for l in range(1, k + 1)]  # v_l(s) = d_l 2^{-s}
    lam = [mp.mpf(random.uniform(0.02, 0.2)) for _ in range(k)]
    eps = [random.choice([-1, 1]) for _ in range(k)]
    jp = [min(s for s in S(l, 10 ** 6) if s > smax) for l in range(1, k + 1)]   # bank coordinates s'_l(L)
    sigma = max(jp)
    reg = min(mu(jp[i]) ** 2 * (d[i] * mp.mpf(2) ** (-jp[i])) ** 2 for i in range(k))   # min (s' v')^2
    G0 = 2 ** (k + 1)
    epsx = mp.mpf(fac) * reg / (k * mp.mpf(4) ** G0)   # c_T ~ c_f Des^{-1}: Des >= l 4^G (s'v')^{-2}
    xs = [epsx * mp.mpf(random.uniform(-1, 1)) for _ in range(k)]
    xs[0] = epsx * random.choice([-1, 1])            # ||x||_inf = eps_x
    G = 2 ** (k + 1)
    pulls = []
    for i in range(k):
        l = i + 1
        # largest element j of S_l with v(j) >= eps_x: v(j) = d 2^{-j} >= epsx  <=> j <= log2(d/epsx)
        jmax = int(mp.floor(mp.log(d[i] / epsx, 2)))
        cand = [s for s in S(l, jmax) if s > jp[i]]
        if not cand:
            return ('nopull',)
        pulls.append(max(cand))
    cutoff = max(pulls) + 4 * G
    U = []
    for i in range(k):
        l = i + 1
        u = {s: mp.mpf(random.gauss(0, 0.3)) for s in F}
        for s in S(l, cutoff):
            if s > smax:
                u[s] = d[i] * mp.mpf(2) ** (-s)
                z[s] = eps[i]
        U.append(u)
    others = [{s: mp.mpf(random.gauss(0, 0.3)) for s in F} for _ in range(3)]
    val2 = [value(U[i], z, A2, eps[i]) for i in range(k)]
    oth2 = [value(o, z, A2, 1) for o in others]
    # Step 1: pulls
    Ap, zp = dict(A2), dict(z)
    for i in range(k):
        j = pulls[i]
        Ap[j] = -eps[i] * 24 * lam[i] * d[i] * mp.mpf(2) ** (-j)
        zp[j] = -eps[i]
    valp = [value(U[i], zp, Ap, eps[i]) for i in range(k)]
    _, nup = ip_e({}, Ap)
    Delta = [xs[i] + val2[i] - valp[i] for i in range(k)]
    phi = [eps[i] * ip_e(U[i], Ap)[0] for i in range(k)]
    s2v = [mu(jp[i]) ** 2 * d[i] * mp.mpf(2) ** (-jp[i]) for i in range(k)]
    sv2 = [(mu(jp[i]) * d[i] * mp.mpf(2) ** (-jp[i])) ** 2 for i in range(k)]

    def nvec(y):
        return [(Delta[i] * y + phi[i] * (y - nup)) / s2v[i] for i in range(k)]

    def M(y):
        n = nvec(y)
        return mp.sqrt(nup ** 2 + sum(mu(jp[i]) ** 2 * n[i] ** 2 for i in range(k)))
    kap = 2 * (M(nup) - nup)
    it = 0
    g = lambda yy: M(yy) - yy
    a, b = nup, nup + kap
    if kap <= 0 or g(a) < 0 or g(b) > 0:
        return ('nobracket/diverge', float(fac), mp.nstr(kap, 3))
    try:
        y = mp.findroot(g, (a, b), solver='illinois', tol=mp.mpf(2) ** (-2300), maxsteps=400)
    except Exception as ex:
        return ('rootfail', float(fac), str(ex)[:60])
    # derivative on I by finite differences
    h = kap / 1000 if kap > 0 else mp.mpf(2) ** (-2000)
    Mp = max(abs(M(nup + t * kap + h) - M(nup + t * kap)) / h for t in [0, 0.25, 0.5, 0.75, 1.0]) if kap > 0 else 0
    Bnd = sum((2 * abs(Delta[i]) + kap) * (abs(Delta[i]) + U_NORM) / (sv2[i] * nup) for i in range(k))
    n = nvec(y)
    if min(n) <= 0:
        return ('negbank', float(fac))
    As, zs = dict(Ap), dict(zp)
    for i in range(k):
        As[jp[i]] = As.get(jp[i], 0) + eps[i] * n[i]
    valS = [value(U[i], zs, As, eps[i]) for i in range(k)]
    exact = max(abs(valS[i] - val2[i] - xs[i]) for i in range(k)) / epsx
    othS = [value(o, zs, As, 1) for o in others]
    omove = max(abs(othS[t] - oth2[t]) for t in range(3)) / epsx ** 2 * reg
    # T_fin design inequality: sigma = max first elements; delta_min ~ min d_l (n_l = 1 here)
    dmin = min(d) * mp.mpf(2) ** 0
    Bmu = mp.mpf(2) ** sigma / mu(sigma) ** 2
    eff_ok = all(s2v[i] >= mp.mpf(4) / 5 * dmin / Bmu for i in range(k))
    con_ok = all(1 / sv2[i] <= mp.mpf(25) / 16 * (Bmu / dmin) ** 2 for i in range(k))
    return ('ok', smax, k, float(fac), int(sigma), float(mp.log(reg, 2)), mp.nstr(exact, 3), mp.nstr(Mp, 3), mp.nstr(Bnd, 3),
            mp.nstr(min(n) / (epsx / s2v[0]), 3), mp.nstr(omove, 3), eff_ok, con_ok, it)

print("# smax k fac sigma log2(reg) |val#-val2-x|/epsx |M'| proof-bound B minbank/(epsx/s'^2v') othermove*reg/epsx^2 effOK conOK iters")
for smax in [5, 7, 9, 11, 13]:
    for k in [1, 2, 3]:
        for fac in ['1e-4', '1e-3', '1e-2', '1e-1', '1', '10']:
            print(smax, k, fac, run(smax, k, fac), flush=True)
