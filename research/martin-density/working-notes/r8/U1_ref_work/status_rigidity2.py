"""Referee check: status rigidity in ratio space (U1 Theorem 2.3 / gap C*-3).

Block model (one block m, finitely many carriers): zeta in R^n, weights Phi; norming data via the clamp parametrization
(as in kappa_indep.py).  Carriers: peaks P (robust), switching set Omega (coarse strict non-peaks), optionally an inactive
robust strict non-peak d0 in Omega, and a few tiny 'fine' carriers.  kappa(Omega) = [A(A+theta) - S_Omega]/theta.
The exact coarse shifted system depends on the Omega VALUES u_l = zeta_l/lambda_l and on kappa only through the ratios
r_l := u_l/kappa (U1 Lemma 1.3: Delta' kappa = sum u_l gamma_l).  Claims tested:
 (1) V1's donor raise (outward push of a robust peak by Lam in zeta units) moves kappa by ~(1-X) Lam (NOT by <= Design b).
 (2) Restoring kappa by a second peak push (U1's 'kappa push') undoes the raise of theta (theta returns to its old value
     up to second order): all peaks act identically on (theta, kappa).
 (3) Restoring instead the ACTIVE ratios r_l (scaling the active Omega values by kappa_new/kappa_old) restores every relative
     position rho_l = nu_l/theta of the active carriers (up to fine terms): status protection is impossible at fixed ratios
     when Omega has no inactive robust carrier.
 (4) With an inactive robust carrier d0 in Omega: an inward push of d0 (then kappa restored by a tiny peak push) lowers the
     relative positions of the active carriers while keeping their values AND kappa fixed (the kappa-neutral lever).
"""
import mpmath as mp
import random
mp.mp.dps = 40
random.seed(5)

def solve_block(zeta, Phi):
    n = len(zeta)
    nu = [abs(zeta[k]) / Phi[k]**2 for k in range(n)]
    def parts(th):
        mins = [min(mp.mpf(1), nu[k] / th) for k in range(n)]
        s = mp.sqrt(mp.fsum(Phi[k]**2 * mins[k]**2 for k in range(n)))
        M = 1 / (1 + s); C = 1 - M
        A = M * mp.fsum(abs(zeta[k]) * mins[k] for k in range(n))
        return A, M, C
    lo, hi = mp.mpf('1e-40'), max(nu) * 10 + 10
    for _ in range(300):
        mid = (lo + hi) / 2
        A, M, C = parts(mid)
        if mid - A * M / C > 0:
            hi = mid
        else:
            lo = mid
    th = (lo + hi) / 2
    A, M, C = parts(th)
    return A, th, M, C, nu

def data(zeta, Phi, Omega, m=1):
    A, th, M, C, nu = solve_block(zeta, Phi)
    S_Om = mp.fsum((nu[k] * Phi[k])**2 for k in Omega)
    kap = (A * (A + th) - S_Om) / th
    lam = [m * Phi[k] for k in range(len(zeta))]
    u = [zeta[k] / lam[k] for k in range(len(zeta))]
    rho = [nu[k] / th for k in range(len(zeta))]
    return dict(A=A, th=th, kap=kap, u=u, rho=rho, M=M, C=C)

def push(zeta, k, s):
    z = list(zeta); z[k] = z[k] + mp.sign(zeta[k]) * s; return z

def bisect(f, lo, hi, it=200):
    flo = f(lo)
    for _ in range(it):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def make_block(with_d0):
    Phi = [mp.mpf('0.20'), mp.mpf('0.15'), mp.mpf('0.12'), mp.mpf('0.10'), mp.mpf('0.08'), mp.mpf('1e-6'), mp.mpf('5e-7')]
    zeta = [Phi[0]**2*20, Phi[1]**2*20, Phi[2]**2*3, Phi[3]**2*3, -Phi[4]**2*2, mp.mpf('1e-14'), mp.mpf('3e-15')]
    if with_d0:
        Phi.append(mp.mpf('0.11')); zeta.append(Phi[7]**2*2)
    return Phi, zeta

def tune_threshold(Phi, zeta, k, target_rho):
    def f(x):
        z = list(zeta); z[k] = x
        A, th, M, C, nu = solve_block(z, Phi)
        return nu[k] / th - target_rho
    x = bisect(f, mp.mpf('1e-12'), mp.mpf(1))
    z = list(zeta); z[k] = x
    return z

for with_d0 in (False, True):
    Phi, zeta = make_block(with_d0)
    zeta = tune_threshold(Phi, zeta, 2, 1 - mp.mpf('1e-9'))
    Omega = [2, 3, 4] + ([7] if with_d0 else [])
    active = [2, 3, 4]
    b0 = data(zeta, Phi, Omega)
    print('=== inactive robust Omega carrier d0 present:', with_d0)
    print(' base rho (Omega, then peaks 0,1):', [mp.nstr(b0['rho'][k], 10) for k in Omega + [0, 1]])
    Lam = mp.mpf('1e-6')
    z1 = push(zeta, 0, Lam); b1 = data(z1, Phi, Omega)
    PhiP2 = Phi[0]**2 + Phi[1]**2
    print(' (1) donor raise (peak 0, Lam=1e-6): dkappa/Lam = %s ; dtheta/Lam = %s (C/Phi_P^2 = %s) ; rho_2 - 1 = %s' % (
        mp.nstr((b1['kap'] - b0['kap']) / Lam, 8), mp.nstr((b1['th'] - b0['th']) / Lam, 8), mp.nstr(b0['C'] / PhiP2, 8), mp.nstr(b1['rho'][2] - 1, 6)))
    s2 = bisect(lambda s: data(push(z1, 1, -s), Phi, Omega)['kap'] - b0['kap'], mp.mpf(0), 10 * Lam)
    z2 = push(z1, 1, -s2); b2 = data(z2, Phi, Omega)
    print(' (2) kappa restored by an inward push of peak 1: |kappa-kappa0| = %s ; theta-theta0 = %s ; rho_2 - 1 = %s' % (
        mp.nstr(abs(b2['kap'] - b0['kap']), 3), mp.nstr(b2['th'] - b0['th'], 4), mp.nstr(b2['rho'][2] - 1, 6)))
    z3 = list(z1)
    for _ in range(80):
        b3 = data(z3, Phi, Omega); fac = b3['kap'] / b0['kap']
        z3 = list(z1)
        for k in active:
            z3[k] = zeta[k] * fac
    b3 = data(z3, Phi, Omega)
    rerr = max(abs(b3['u'][k] / b3['kap'] - b0['u'][k] / b0['kap']) for k in active)
    print(' (3) raise kept, active ratios u/kappa restored (err %s): rho changes of active carriers %s ; rho_2 - 1 = %s' % (
        mp.nstr(rerr, 3), [mp.nstr(b3['rho'][k] - b0['rho'][k], 4) for k in active], mp.nstr(b3['rho'][2] - 1, 6)))
    if with_d0:
        z4 = push(zeta, 7, -100 * Lam)
        b4a = data(z4, Phi, Omega)
        f4 = lambda s: data(push(z4, 0, s), Phi, Omega)['kap'] - b0['kap']
        print('    lever: kappa change from d0 inward push alone = %s ; f4(-1e-4)=%s f4(1e-4)=%s' % (mp.nstr(b4a['kap'] - b0['kap'], 4), mp.nstr(f4(-mp.mpf('1e-4')),4), mp.nstr(f4(mp.mpf('1e-4')),4)))
        s4 = bisect(f4, -mp.mpf('1e-4'), mp.mpf('1e-4'))
        z4 = push(z4, 0, s4); b4 = data(z4, Phi, Omega)
        rerr4 = max(abs(b4['u'][k] / b4['kap'] - b0['u'][k] / b0['kap']) for k in active)
        print(' (4) kappa-neutral lever (d0 inward by 1e-4, kappa restored by peak push s=%s): |kappa-kappa0|=%s, active ratio err=%s,'
              ' theta-theta0=%s, rho changes of active carriers %s, rho_2 - 1 = %s' % (mp.nstr(s4, 4), mp.nstr(abs(b4['kap'] - b0['kap']), 3),
              mp.nstr(rerr4, 3), mp.nstr(b4['th'] - b0['th'], 4), [mp.nstr(b4['rho'][k] - b0['rho'][k], 4) for k in active], mp.nstr(b4['rho'][2] - 1, 6)))
