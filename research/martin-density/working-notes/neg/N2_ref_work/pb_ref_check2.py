# Check of N2 Prop. 2.3: explicit decompositions of f^# + t gamma h, both sides, at f and canonical truncations f_N.
exec(open('pbmodel.py').read())
theta = mp.mpf(1)/5; gamma0 = mp.mpf('5e-5')
tplus = Phi[12]/theta; tminus = Phi[13]/theta
def psi_of(w):
    out = {}
    for k in u:
        cf = Phi[k]*w[k]
        if cf == 0: continue
        for j, val in u[k].items(): out[j] = out.get(j, 0) + cf*val
    return out
def check_row(label, zf, gamma=None, nu_fixed=None):
    zeta, w, M, C, th, nz = forced(zf)
    psi = psi_of(w)
    worst = -mp.inf; info = None; worstN = -mp.inf; worstq = -mp.inf
    for side in (+1, -1):
        Sset = Splus if side == +1 else Sminus
        tmax = tplus if side == +1 else tminus
        for e in range(0, 60):
            t = tmax*mp.mpf(10)**(-mp.mpf(e)/4)       # t from tmax down to ~1e-15 tmax
            S_t = [k for k in Sset if Phi[k] <= theta*t]
            if not S_t: continue
            cont1 = (M/t)*sum(Phi[k]/n[k] for k in S_t)   # content per unit nu
            nu = nu_fixed if nu_fixed is not None else gamma/cont1
            if nu > mp.mpf(1)/2: print('nu > 1/2 !'); continue
            gam = nu*cont1
            om = {k: nu*M/t for k in S_t}
            S2 = sum(Phi[k]**2*om[k] for k in S_t)
            d = sum(Phi[k]**2*w[k]*om[k] for k in S_t)/C          # <Dw, D omega>/C
            # side +1: f + t gam h = (a + tB) + L*((1 - t d) w + t om);  side -1: f - t gam h = (a - tB) + L*((1 + t d) w - t om)
            if side == +1:
                W = {k: (1 - t*d)*w[k] + t*om.get(k, 0) for k in u}
            else:
                W = {k: (1 + t*d)*w[k] - t*om.get(k, 0) for k in u}
            NW = max(abs(x) for x in W.values()) + mp.sqrt(sum((Phi[k]*W[k])**2 for k in u))
            # B := gam h - L*(om - d w), computed directly (checks the content algebra B = -E + d psi)
            LTh = {}
            for k in u:
                cf = Phi[k]*(om.get(k, 0) - d*w[k])
                if cf == 0: continue
                for j, val in u[k].items(): LTh[j] = LTh.get(j, 0) + cf*val
            B = add((gam, h), (-1, LTh))
            A = add((1, a), (side*t, B))
            qA = qstar(A)
            # identity check: A + L*W == f + side*t*gam*h  (f = a + psi)
            LW = psi_of(W)
            lhs = add((1, A), (1, LW)); rhs = add((1, a), (1, psi), (side*t*gam, h))
            err = max(abs(lhs.get(j, 0) - rhs.get(j, 0)) for j in set(lhs) | set(rhs))
            exc = (max(qA, NW) - 1)/t**2
            worstN = max(worstN, (NW-1)/t**2); worstq = max(worstq, (qA-1)/t**2)
            if exc > worst: worst = exc; info = (side, mp.nstr(t, 4), mp.nstr(nu, 4), mp.nstr(err, 3), len(S_t))
    print(label, ' max (p*-bound - 1)/t^2 = %s  [N-part %s, q-part %s]  at (side, t, nu, identity err, |S(t)|) =' % (
        mp.nstr(worst, 6), mp.nstr(worstN, 6), mp.nstr(worstq, 6)), info)
for mode, kw in (('gamma = gamma_0', dict(gamma=gamma0)), ('nu = 1/2 (max content)', dict(nu_fixed=mp.mpf(1)/2))):
    print('==', mode)
    check_row('f   :', zh, **kw)
    for N in (3, 10, 60):
        check_row('f_%d:' % N, zhat_fun(N), **kw)
