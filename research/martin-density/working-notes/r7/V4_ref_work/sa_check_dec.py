"""High-precision re-check of Construction SA (V4 Theorem 2.2) and Proposition 3.2, N = 1.

V4's sa_check.py runs in double precision and tunes n_- val_- to -4.7e-16, i.e. ONE ulp: its sign checks for l_- are at
round-off level.  Here everything is done with mpmath at 120 digits, with (SF*)-type weights.
Model: coordinates Z0 = {0,1} = F, extra non-signature coordinates, truncated signature sets S_l (r coordinates each,
weights 2^{-i}).  Diagonal base s_j.  One block (m = 1), carriers l = 0..L-1 with k(l) = l+1.
"""
import decimalmp as mp
import random

mp.mp.dps = 120
random.seed(3)
L, r, n_extra = 9, 6, 30
Z0 = [0, 1]
extra = list(range(2, 2 + n_extra))
sig0 = 2 + n_extra
S = [list(range(sig0 + l * r, sig0 + (l + 1) * r)) for l in range(L)]
D = sig0 + L * r
s = [mp.mpf(1) / 2 ** (1 + (j % 7)) for j in range(D)]
s[0], s[1] = mp.mpf('0.8'), mp.mpf('0.6')
Unorm = max(s)

def qstar(v):
    return sum(abs(x) for x in v) + mp.sqrt(sum((s[j] * v[j]) ** 2 for j in range(D)))

l_minus = 5
h = [[mp.mpf(0)] * D for _ in range(L)]
for l in range(L):
    for i, j in enumerate(S[l]):
        h[l][j] = mp.mpf(1) / 2 ** (i + 1)
H = [sum(h[l]) for l in range(L)]
delta = [min(mp.mpf(1) / 2 ** (l + 1), 1 / (4 * (1 + Unorm) * H[l])) for l in range(L)]
Y = [[mp.mpf(0)] * D for _ in range(L)]
for l in range(L):
    if l == l_minus:
        Y[l][0], Y[l][1] = mp.mpf(1), mp.mpf(-1)
    else:
        pool = Z0 + extra + [j for ll in range(l) for j in S[ll][-2:]]
        supp = random.sample(pool, 4)
        for j in supp:
            g = random.gauss(0, 1)
            Y[l][j] = mp.mpf(g) + mp.mpf('0.3') * (1 if random.gauss(0, 1) > 0 else -1)
    qn = qstar(Y[l])
    Y[l] = [x / qn for x in Y[l]]
n = [qstar([Y[l][j] + delta[l] * h[l][j] for j in range(D)]) for l in range(L)]
Urow = [[(Y[l][j] + delta[l] * h[l][j]) / n[l] for j in range(D)] for l in range(L)]
eta_min = [min([mp.mpf(1)] + [abs(x) for x in Y[l] if x != 0]) for l in range(L)]
# (SF*)-type weights: c_l <= c_{l-1} delta_l 2^{-minS_l - l - 10}/(1+||U||) and sum_{l''>l} lambda <= 2^{-10} lambda_l delta_l 2^{-(1+k+minS)} eta/n
c = [mp.mpf(1)]
for l in range(1, L):
    lam_prev = mp.mpf(1) / 2 ** (1 + l) * c[l - 1]          # lambda_{l-1} = 2^{-m-k} c, m = 1, k = l
    b1 = c[l - 1] * delta[l] * mp.mpf(2) ** (-(S[l][0] - sig0 + 1) - l - 10) / (1 + Unorm)
    b2 = 3 * mp.mpf(2) ** (-10) * lam_prev * delta[l - 1] * mp.mpf(2) ** (-(1 + l + (S[l - 1][0] - sig0 + 1))) * eta_min[l - 1] / (n[l - 1] * (1 + Unorm))
    c.append(min(c[l - 1] / 4, b1, b2))
Phi = [mp.mpf(1) / 2 ** (1 + (l + 1)) * c[l] for l in range(L)]
lam = Phi[:]

def build(ratio):
    a = [mp.mpf(0)] * D
    a[0], a[1] = ratio, mp.mpf(1)
    nu = mp.sqrt(sum((s[j] * a[j]) ** 2 for j in range(D)))
    tot = sum(abs(x) for x in a) + nu
    a = [x / tot for x in a]
    nu = mp.sqrt(sum((s[j] * a[j]) ** 2 for j in range(D)))
    zh = {j: mp.sign(a[j]) + s[j] ** 2 * a[j] / nu for j in Z0}
    z = [mp.mpf(0)] * D
    assigned = set(Z0)
    for j in Z0:
        z[j] = mp.sign(a[j])
    eps = []
    for l in range(L):
        supp = [j for j in range(D) if Y[l][j] != 0]
        A = sum(Y[l][j] * (zh[j] if j in zh else z[j]) for j in supp if j in assigned)
        e = mp.mpf(1) if l == l_minus else (mp.sign(A) if A != 0 else mp.mpf(1))
        for j in supp:
            if j not in assigned:
                z[j] = e * mp.sign(Y[l][j]); assigned.add(j)
        for j in S[l]:
            z[j] = e; assigned.add(j)
        eps.append(e)
    zhat = z[:]
    for j in Z0:
        zhat[j] = zh[j]
    val = [sum(Urow[l][j] * zhat[j] for j in range(D)) for l in range(L)]
    return a, z, zhat, eps, val

def theta_of(zeta):
    nuk = [abs(zeta[k]) / Phi[k] ** 2 for k in range(L)]
    def Psi(th):
        A = sum(max(abs(zeta[k]) - th * Phi[k] ** 2, 0) for k in range(L))
        B = sum(Phi[k] ** 2 * min(th, nuk[k]) ** 2 for k in range(L))
        return A * A - B
    lo, hi = mp.mpf(0), 2 * max(nuk)
    for _ in range(800):
        mid = (lo + hi) / 2
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2, nuk

a, z, zhat, eps, val = build(mp.mpf(1))
th0, _ = theta_of([lam[k] * val[k] for k in range(L)])
eta = n[l_minus] * th0 * Phi[l_minus] / 4
target = -eta
lo, hi = mp.mpf('1e-8'), mp.mpf('1e8')
for _ in range(600):
    mid = mp.sqrt(lo * hi)
    v = build(mid)[4][l_minus] * n[l_minus]
    if v > target: hi = mid
    else: lo = mid
a, z, zhat, eps, val = build(mp.sqrt(lo * hi))
zeta = [lam[k] * val[k] for k in range(L)]
th, nuk = theta_of(zeta)
print("n_- val_- =", mp.nstr(n[l_minus] * val[l_minus], 12), " target", mp.nstr(target, 12))
for l in range(L):
    print(f"l={l} eps={int(eps[l]):+d} val={mp.nstr(val[l],6)} nu/theta={mp.nstr(nuk[l]/th,6)} "
          f"{'peak' if nuk[l] >= th else 'NON-PEAK'} sgn_ok={(mp.sign(val[l]) == eps[l]) or l == l_minus} "
          f"|val|>=dH/n: {abs(val[l]) >= delta[l]*H[l]/n[l] or l == l_minus}")
Aval = sum(max(abs(zeta[k]) - th * Phi[k] ** 2, 0) for k in range(L))
C_ = 1 / (1 + th / Aval); M_ = 1 - C_
w = [mp.sign(zeta[k]) * M_ if nuk[k] >= th else C_ * zeta[k] / (Phi[k] ** 2 * Aval) for k in range(L)]
print("N(w) - 1 =", mp.nstr(max(abs(x) for x in w) + mp.sqrt(sum((Phi[k] * w[k]) ** 2 for k in range(L))) - 1, 5),
      " <w,zeta> - |zeta| =", mp.nstr(sum(w[k] * zeta[k] for k in range(L)) - Aval, 5))
q_minus = eps[l_minus] * Phi[l_minus] * w[l_minus] / C_
print("q_- =", mp.nstr(q_minus, 6), "(< 0 expected)")
offF = [j for j in range(D) if j not in Z0]
W = [sum(lam[l] * eps[l] * Urow[l][j] for l in range(L)) for j in range(D)]
badW = [j for j in offF if W[j] != 0 and not (abs(z[j]) == 1 and z[j] * W[j] > 0)]
RW = [sum(lam[k] * w[k] * Urow[k][j] for k in range(L)) for j in range(D)]
V = [Urow[l_minus][j] - (val[l_minus] / Aval) * RW[j] for j in range(D)]
badV = [j for j in offF if abs(V[j]) > mp.mpf(10) ** (-100) and not (abs(z[j]) == 1 and z[j] * V[j] > 0)]
print("W z-signed off F:", not badW, " #W!=0:", sum(1 for j in offF if W[j] != 0))
print("V z-signed off F:", not badV, " #V!=0:", sum(1 for j in offF if abs(V[j]) > mp.mpf(10) ** (-100)))
print("V(zhat) =", mp.nstr(sum(V[j] * zhat[j] for j in range(D)), 5), "(0 expected)")
print("Delta d / Delta alpha =", mp.nstr(lam[l_minus] * val[l_minus] / Aval, 6), "(< 0 expected)")
print("min ratio later/owner on S_{l_-}:",
      mp.nstr(min((W[j] - lam[l_minus] * Urow[l_minus][j]) / (lam[l_minus] * Urow[l_minus][j]) for j in S[l_minus]), 4),
      mp.nstr(max((W[j] - lam[l_minus] * Urow[l_minus][j]) / (lam[l_minus] * Urow[l_minus][j]) for j in S[l_minus]), 4))
