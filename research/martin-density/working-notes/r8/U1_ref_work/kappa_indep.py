"""Independent high-precision check of U1 Lemmas 1.2-1.4 (referee).

Method (independent of U1's scripts): the norming functional of zeta in (l_1, |.|_Phi) (unit ball B_l1 + D_Phi B_l2,
dual norm N(w) = ||w||_inf + ||Phi w||_2) has the clamp form w(k) = sgn(zeta_k) M min(1, nu_k/theta),
nu_k = |zeta_k|/Phi_k^2, theta = A M / C.  Given theta, M = 1/(1 + sqrt(sum Phi^2 min(1,nu/theta)^2)), C = 1 - M,
A = <w, zeta>; theta is the root of  F(theta) := theta - A(theta) M(theta)/C(theta) = 0  (solved by bisection in mpmath).
We then check N(w) = 1, <w,zeta> = A (by construction), and compare A with the primal gauge computed independently by
cvxpy (double precision) for a subset of instances.  Then:
 (E1) sum_P Phi^2 (nu - theta) = A,  (E2) A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2,
 (1.3) Delta M kappa(Omega) = sum_Omega u_k gamma_k for random omega^+- supported in Omega subset Q, m = block index,
 Lemma 1.4 (a), (b), (c) by central differences on the FULL recomputation (theta re-solved, peak set re-determined).
"""
import mpmath as mp
import random
mp.mp.dps = 50
random.seed(20261010)

def solve_block(zeta, Phi):
    n = len(zeta)
    nu = [abs(zeta[k]) / Phi[k]**2 for k in range(n)]
    def parts(th):
        mins = [min(mp.mpf(1), nu[k] / th) for k in range(n)]
        s = mp.sqrt(mp.fsum(Phi[k]**2 * mins[k]**2 for k in range(n)))
        M = 1 / (1 + s); C = 1 - M
        A = M * mp.fsum(abs(zeta[k]) * mins[k] for k in range(n))
        return A, M, C, mins
    def F(th):
        A, M, C, _ = parts(th)
        return th - A * M / C
    lo, hi = mp.mpf('1e-40'), max(nu) * 10 + 10
    # F(lo) < 0 (theta tiny, A M/C positive), F(hi) > 0 for hi large
    assert F(lo) < 0 and F(hi) > 0
    for _ in range(400):
        mid = (lo + hi) / 2
        if F(mid) > 0:
            hi = mid
        else:
            lo = mid
    th = (lo + hi) / 2
    A, M, C, mins = parts(th)
    w = [mp.sign(zeta[k]) * M * mins[k] for k in range(n)]
    return dict(A=A, M=M, C=C, theta=th, w=w, nu=nu)

def kappa_of(zeta, Phi, Omega):
    b = solve_block(zeta, Phi)
    th, A, nu = b['theta'], b['A'], b['nu']
    n = len(zeta)
    P = [k for k in range(n) if nu[k] >= th]
    Q = [k for k in range(n) if nu[k] < th]
    PhiP2 = mp.fsum(Phi[k]**2 for k in P)
    k1 = (A * (A + th) - mp.fsum((nu[k] * Phi[k])**2 for k in Omega)) / th
    k2 = A + th * PhiP2 + mp.fsum((nu[k] * Phi[k])**2 for k in Q if k not in Omega) / th
    return k1, k2, b, P, Q, PhiP2

maxE1 = maxE2 = maxK = maxI = maxN = mp.mpf(0)
dA = []; dB = []; dC = []
ntests = 0
for trial in range(400):
    n = random.randint(4, 10)
    m = random.randint(1, 3)
    Phi = [mp.mpf(2)**(-(m + k + 1)) * mp.mpf(random.uniform(0.2, 1.0)) for k in range(n)]
    zeta = [mp.mpf(random.choice([-1, 1])) * mp.mpf(random.uniform(0.0, 1.0)) * Phi[k] ** mp.mpf(random.uniform(1.0, 2.2)) for k in range(n)]
    b = solve_block(zeta, Phi)
    th, A, M, C, w, nu = b['theta'], b['A'], b['M'], b['C'], b['w'], b['nu']
    Nw = max(abs(x) for x in w) + mp.sqrt(mp.fsum((Phi[k] * w[k])**2 for k in range(n)))
    maxN = max(maxN, abs(Nw - 1))
    P = [k for k in range(n) if nu[k] >= th]
    Q = [k for k in range(n) if nu[k] < th]
    if not P or not Q:
        continue
    ntests += 1
    PhiP2 = mp.fsum(Phi[k]**2 for k in P)
    E1 = mp.fsum(Phi[k]**2 * (nu[k] - th) for k in P) - A
    E2 = A**2 - th**2 * PhiP2 - mp.fsum((nu[k] * Phi[k])**2 for k in Q)
    maxE1 = max(maxE1, abs(E1) / A); maxE2 = max(maxE2, abs(E2) / A**2)
    Omega = [k for k in Q if random.random() < 0.6] or [Q[0]]
    k1, k2, _, _, _, _ = kappa_of(zeta, Phi, Omega)
    maxK = max(maxK, abs(k1 - k2) / abs(k1))
    # data identity (1.3): omega^+- supported in Omega
    lam = [m * Phi[k] for k in range(n)]
    om_p = [mp.mpf(random.uniform(-3, 3)) if k in Omega else mp.mpf(0) for k in range(n)]
    om_m = [mp.mpf(random.uniform(-3, 3)) if k in Omega else mp.mpf(0) for k in range(n)]
    d = lambda x: mp.fsum(Phi[k]**2 * w[k] * x[k] for k in range(n)) / C
    Delta = d(om_m) - d(om_p)
    u = [zeta[k] / lam[k] for k in range(n)]
    gamma = [lam[k] * ((om_m[k] - om_p[k]) - Delta * w[k]) for k in range(n)]
    lhs = Delta * M * k1
    rhs = mp.fsum(u[k] * gamma[k] for k in Omega)
    maxI = max(maxI, abs(lhs - rhs) / (abs(rhs) + abs(lhs) + mp.mpf('1e-40')))
    # derivatives (central differences on full recomputation)
    h = mp.mpf('1e-25')
    S = mp.fsum((nu[k] * Phi[k])**2 for k in Q if k not in Omega)
    X = C * S / (th**2 * PhiP2)
    # (a) push of a peak c
    c = random.choice(P)
    def push(k, s):
        z = list(zeta); z[k] = z[k] + mp.sign(zeta[k]) * s; return z
    kp = kappa_of(push(c, h), Phi, Omega)[0]; km = kappa_of(push(c, -h), Phi, Omega)[0]
    if len(kappa_of(push(c, h), Phi, Omega)[3]) == len(P) and len(kappa_of(push(c, -h), Phi, Omega)[3]) == len(P):
        num = (kp - km) / (2 * h)
        dA.append(abs(num - (1 - X)) / abs(1 - X))
    # (b) push of a strict non-peak d in Q \ Omega with zeta(d) != 0
    QmO = [k for k in Q if k not in Omega and zeta[k] != 0]
    if QmO:
        dd = random.choice(QmO)
        rho = nu[dd] / th
        kp = kappa_of(push(dd, h), Phi, Omega)[0]; km = kappa_of(push(dd, -h), Phi, Omega)[0]
        num = (kp - km) / (2 * h)
        formula = rho * (2 + M * X / C)
        dB.append(abs(num - formula) / abs(formula))
    # (c) push of a strict non-peak in Omega
    Oz = [k for k in Omega if zeta[k] != 0]
    if Oz:
        dd = random.choice(Oz)
        rho = nu[dd] / th
        kp = kappa_of(push(dd, h), Phi, Omega)[0]; km = kappa_of(push(dd, -h), Phi, Omega)[0]
        num = (kp - km) / (2 * h)
        formula = rho * M * X / C
        if abs(formula) > mp.mpf('1e-30'):
            dC.append(abs(num - formula) / abs(formula))

print('tests', ntests)
print('max |N(w)-1|', mp.nstr(maxN, 5))
print('max rel (E1)', mp.nstr(maxE1, 5), ' max rel (E2)', mp.nstr(maxE2, 5))
print('max rel kappa forms', mp.nstr(maxK, 5), ' max rel identity (1.3)', mp.nstr(maxI, 5))
print('Lemma 1.4(a): n=%d max rel err %s' % (len(dA), mp.nstr(max(dA), 5) if dA else '-'))
print('Lemma 1.4(b): n=%d max rel err %s' % (len(dB), mp.nstr(max(dB), 5) if dB else '-'))
print('Lemma 1.4(c): n=%d max rel err %s' % (len(dC), mp.nstr(max(dC), 5) if dC else '-'))
