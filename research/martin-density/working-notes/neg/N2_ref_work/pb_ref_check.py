# Independent high-precision check of N2 Section 2 (T_PB, rows f, f_N, mates gamma h) with the TRUE parameters:
# staircase Sigma_+ = {k>=12, k=0 mod 3}, Sigma_- = {k>=13, k=1 mod 3}, Phi(k) = 2^{-1-k} c_k, c_k = 1 on staircase,
# c_k = 2^{-k^2} on generic carriers, mu_j = 2^{-j-10}, private signatures delta_k sigma_k, delta_k = 2^{-k} Phi(k)^2.
import mpmath as mp, random
mp.mp.dps = 60
random.seed(3)
KMAX = 96                      # carriers 1..KMAX (Phi(KMAX) ~ 2^{-97})
J = 1200                       # base coordinates 1..J
mu = {j: mp.mpf(2)**(-j-10) for j in range(1, J+1)}
abar = 1/(1+mu[1])
def qstar(b):                  # b: dict j->value
    return sum(abs(v) for v in b.values()) + mp.sqrt(sum((mu[j]*v)**2 for j, v in b.items()))
def ev(b, x):                  # pairing with x (dict or function)
    return sum(v*x(j) for j, v in b.items())
def add(*terms):               # linear combination of (coef, dict)
    out = {}
    for c, b in terms:
        for j, v in b.items(): out[j] = out.get(j, 0) + c*v
    return out
Splus = [k for k in range(12, KMAX+1) if k % 3 == 0]
Sminus = [k for k in range(13, KMAX+1) if k % 3 == 1]
stair = set(Splus) | set(Sminus)
c = {}; Phi = {}
for k in range(1, KMAX+1):
    c[k] = mp.mpf(1) if (k == 1 or k in stair) else mp.mpf(2)**(-k*k)
    Phi[k] = mp.mpf(2)**(-1-k)*c[k]
delta = {k: mp.mpf(2)**(-k)*Phi[k]**2 for k in Phi}
# signature sets: S_k = 6 coordinates in a private chunk (finite truncation of the infinite S_k)
S = {k: list(range(200 + 6*k, 206 + 6*k)) for k in range(1, KMAX+1)}
sig = {k: {s: mp.mpf(2)**(-s) for s in S[k]} for k in S}
h = {2: mp.mpf(1), 3: mp.mpf(-1)}; e0 = {2: mp.mpf(1), 3: mp.mpf(1)}; e1 = {1: mp.mpf(1)}
def zhat_fun(N=None):
    def z(j):
        if N is not None and j > N: return mp.mpf(0) if j != 1 else 1 + mu[1]
        return 1 + mu[1] if j == 1 else mp.mpf(1)/2
    return z
zh = zhat_fun()
v = {}
for k in range(1, KMAX+1):
    if k == 1:
        v[k] = add((1, e1), (delta[1], sig[1]))
    elif k in stair:
        beta = -8*Phi[k] if k in Splus else 8*Phi[k]
        v[k] = add((1, h), (beta, e0), (delta[k], sig[k]))
    else:   # generic: random sparse target on coordinates 1..60, normalised in q*
        sup = random.sample(range(1, 61), 3)
        y = {j: mp.mpf(random.gauss(0, 1)) for j in sup}
        ny = qstar(y); y = {j: val/ny for j, val in y.items()}
        val = ev(y, zh) + delta[k]*ev(sig[k], zh)
        s = mp.mpf(0) if abs(val) >= 4*Phi[k] else (8*Phi[k] if val >= 0 else -8*Phi[k])
        v[k] = add((1, y), (s*abar, e1), (delta[k], sig[k]))
n = {k: qstar(v[k]) for k in v}
u = {k: {j: val/n[k] for j, val in v[k].items()} for k in v}
a = {1: abar}
def forced(zf):
    zeta = {k: Phi[k]*ev(u[k], zf) for k in u}
    vv = {k: abs(zeta[k])/Phi[k]**2 for k in u}
    A = lambda x: sum(max(abs(zeta[k]) - x*Phi[k]**2, 0) for k in u)
    B = lambda x: sum(Phi[k]**2*min(x, vv[k])**2 for k in u)
    lo, hi = mp.mpf("1e-30"), mp.mpf(100)
    assert A(hi)**2 - B(hi) < 0
    for _ in range(400):
        mid = (lo+hi)/2
        if A(mid)**2 - B(mid) > 0: lo = mid
        else: hi = mid
    th = (lo+hi)/2; nz = A(th); M = th/(th+nz); C = nz/(th+nz)
    w = {k: mp.sign(zeta[k])*M*min(1, vv[k]/th) for k in u}
    return zeta, w, M, C, th, nz
def report(label, zf):
    zeta, w, M, C, th, nz = forced(zf)
    peaks = [k for k in u if abs(abs(w[k]) - M) < mp.mpf('1e-40')]
    rel = [ev(u[k], zf)/Phi[k] for k in stair]
    nonp = [k for k in u if k not in peaks]
    print(label, ' M=%s C=%s thr(zhat units)=%s |zeta|=%s' % (mp.nstr(M, 6), mp.nstr(C, 6), mp.nstr(th, 6), mp.nstr(nz, 6)))
    print('   staircase u_k(zhat)/Phi(k): Sigma+ in [%s,%s], Sigma- in [%s,%s]' % (
        mp.nstr(min(ev(u[k], zf)/Phi[k] for k in Splus), 6), mp.nstr(max(ev(u[k], zf)/Phi[k] for k in Splus), 6),
        mp.nstr(min(ev(u[k], zf)/Phi[k] for k in Sminus), 6), mp.nstr(max(ev(u[k], zf)/Phi[k] for k in Sminus), 6)))
    print('   all staircase are peaks:', all(k in peaks for k in stair), ' strict non-peaks:', nonp[:12], ' n_stair in [%s,%s]' % (
        mp.nstr(min(n[k] for k in stair), 8), mp.nstr(max(n[k] for k in stair), 8)))
    return zeta, w, M, C, th, nz
res = {'f': report('f   :', zh)}
for N in (3, 10, 60):
    res[N] = report('f_%d:' % N, zhat_fun(N))
import pickle
pickle.dump({'note': 'see pb_ref_check2.py'}, open('/dev/null', 'wb'))
