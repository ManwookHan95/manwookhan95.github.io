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

# ---- block: carriers 0,1 robust peaks; 2,3,4 Omega (2 near-threshold 'K4'-type, 3 and 4 robust active); 5,6 fine tiny
def make_block(with_d0):
    Phi = [mp.mpf('0.20'), mp.mpf('0.15'), mp.mpf('0.12'), mp.mpf('0.10'), mp.mpf('0.08'), mp.mpf('1e-6'), mp.mpf('5e-7')]
    zeta = [mp.mpf('0.5') * Phi[0]**2 * 40, mp.mpf('0.5') * Phi[1]**2 * 40, None, mp.mpf('0.3') * Phi[3]**2 * 10,
            -mp.mpf('0.5') * Phi[4]**2 * 10, mp.mpf('1e-14'), mp.mpf('3e-15')]
    if with_d0:
        Phi.append(mp.mpf('0.11')); zeta.append(mp.mpf('0.5') * Phi[-1]**2 * 10)
    zeta[2] = mp.mpf(1)  # placeholder, tuned to put carrier 2 at the threshold
    return Phi, zeta

def tune_threshold(Phi, zeta, k, target_rho):
    # choose |zeta_k| so that rho_k = target_rho (bisection on |zeta_k|)
    def f(x):
        z = list(zeta); z[k] = x
        A, th, M, C, nu = solve_block(z, Phi)
        return nu[k] / th - target_rho
    x = bisect(f, mp.mpf('1e-12'), mp.mpf(1))
    z = list(zeta); z[k] = x
    return z

for with_d0 in (False, True):
    Phi, zeta = make_block(with_d0)
    zeta = tune_threshold(Phi, zeta, 2, 1 - mp.mpf('1e-9'))   # carrier 2: near-threshold strict non-peak (rho = 1 - 1e-9)
    Omega = [2, 3, 4] + ([7] if with_d0 else [])
    active = [2, 3, 4]
    d0 = data(zeta, Phi, Omega)
    print('=== with inactive robust Omega carrier d0:', with_d0)
    print(' base: theta=%s kappa=%s rho=%s' % (mp.nstr(d0['th'], 12), mp.nstr(d0['kap'], 12), [mp.nstr(d0['rho'][k], 10) for k in Omega + [0, 1]]))
    Lam = mp.mpf('1e-6')
    z1 = push(zeta, 0, Lam)                      # V1 donor raise at peak 0
    d1 = data(z1, Phi, Omega)
    X = d1['C'] * mp.fsum((solve_block(z1, Phi)[4][k] * Phi[k])**2 for k in [5, 6]) / (d1['th']**2 * (Phi[0]**2 + Phi[1]**2))
    print(' (1) donor raise Lam=%s: dkappa/Lam=%s (1-X=%s), dtheta=%s, rho_2-1=%s' % (mp.nstr(Lam, 3), mp.nstr((d1['kap'] - d0['kap']) / Lam, 10),
          mp.nstr(1 - X, 10), mp.nstr(d1['th'] - d0['th'], 6), mp.nstr(d1['rho'][2] - 1, 6)))
    # (2) restore kappa by pushing peak 1 inward (U1's kappa push)
    s2 = bisect(lambda s: data(push(z1, 1, -s), Phi, Omega)['kap'] - d0['kap'], mp.mpf(0), 10 * Lam)
    z2 = push(z1, 1, -s2); d2 = data(z2, Phi, Omega)
    print(' (2) kappa restored by a peak push: theta-theta_base=%s (raise was %s), rho_2-1=%s' % (mp.nstr(d2['th'] - d0['th'], 6),
          mp.nstr(d1['th'] - d0['th'], 6), mp.nstr(d2['rho'][2] - 1, 6)))
    # (3) keep the raise, restore the ACTIVE ratios u_l/kappa by scaling active Omega values (iterate: kappa depends on them weakly)
    z3 = list(z1)
    for _ in range(60):
        d3 = data(z3, Phi, Omega)
        fac = d3['kap'] / d0['kap']
        z3 = list(z3)
        for k in active:
            z3[k] = zeta[k] * fac
    d3 = data(z3, Phi, Omega)
    ratio_err = max(abs(d3['u'][k] / d3['kap'] - d0['u'][k] / d0['kap']) for k in active)
    print(' (3) raise + active ratios restored (max ratio err %s): rho_2-1=%s, rho changes %s' % (mp.nstr(ratio_err, 3),
          mp.nstr(d3['rho'][2] - 1, 6), [mp.nstr(d3['rho'][k] - d0['rho'][k], 4) for k in active]))
    if with_d0:
        # (4) inward push of inactive d0 (index 7) by 10 Lam, then restore kappa by a small push of peak 0 (either sign)
        z4 = push(zeta, 7, -10 * Lam)
        f4 = lambda s: data(push(z4, 0, s), Phi, Omega)['kap'] - d0['kap']
        s4 = bisect(f4, -10 * Lam, 10 * Lam)
        z4 = push(z4, 0, s4); d4 = data(z4, Phi, Omega)
        print(' (4) kappa-neutral lever: |kappa-kappa_base|=%s, active values unchanged, theta change=%s, rho_2-1=%s, rho changes %s' % (
              mp.nstr(abs(d4['kap'] - d0['kap']), 3), mp.nstr(d4['th'] - d0['th'], 6), mp.nstr(d4['rho'][2] - 1, 6),
              [mp.nstr(d4['rho'][k] - d0['rho'][k], 4) for k in active]))
