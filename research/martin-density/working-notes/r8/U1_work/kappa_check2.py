"""High-precision check of Lemma 1.4 (derivatives of kappa) with mpmath.
For a fixed peak set P, (A, theta) solve (E1) sum_P Phi^2 (nu - theta) = A and (E2) A^2 = theta^2 Phi_P^2 + sum_Q nu^2 Phi^2.
(E1) gives A linear in theta; substitute into (E2): quadratic in theta.  We take the root with nu_k >= theta on P, nu_k < theta on Q,
and verify self-consistency (it must coincide with the norming-functional data: checked in kappa_check.py).
Then central finite differences (h = 1e-30) of kappa against the formulas of Lemma 1.4."""
import mpmath as mp
import random
mp.mp.dps = 60
random.seed(7)

def solve(nu, Phi, P):
    Q = [k for k in range(len(nu)) if k not in P]
    SP = mp.fsum(Phi[k]**2 * nu[k] for k in P)
    PhiP2 = mp.fsum(Phi[k]**2 for k in P)
    SQ = mp.fsum((nu[k]*Phi[k])**2 for k in Q)
    # A = SP - theta PhiP2 ; (SP - th PhiP2)^2 = th^2 PhiP2 + SQ
    a = PhiP2**2 - PhiP2
    b = -2*SP*PhiP2
    c = SP**2 - SQ
    disc = b*b - 4*a*c
    if disc < 0:
        return [], PhiP2, Q
    roots = [(-b + mp.sqrt(disc))/(2*a), (-b - mp.sqrt(disc))/(2*a)]
    good = []
    for th in roots:
        A = SP - th*PhiP2
        if A > 0 and th > 0 and all(nu[k] >= th for k in P) and all(nu[k] < th for k in Q):
            good.append((A, th))
    return good, PhiP2, Q

def kappa(nu, Phi, P, Omega):
    good, PhiP2, Q = solve(nu, Phi, P)
    if len(good) != 1:
        return None
    A, th = good[0]
    S = mp.fsum((nu[k]*Phi[k])**2 for k in Q if k not in Omega)
    return A + th*PhiP2 + S/th, A, th, PhiP2, S

worst1 = mp.mpf(0); worst2 = mp.mpf(0); worst3 = mp.mpf(0); n1 = n2 = n3 = 0
for trial in range(3000):
    n = random.randint(4, 9)
    Phi = [mp.mpf(2)**(-(k+2)) * mp.mpf(random.uniform(0.3, 1.0)) for k in range(n)]
    nu = [mp.mpf(random.uniform(0.0, 3.0)) for k in range(n)]
    # choose P = set of nu >= some theta guess; then require consistency
    th0 = mp.mpf(random.uniform(0.5, 2.0))
    P = [k for k in range(n) if nu[k] >= th0]
    if len(P) == 0 or len(P) == n:
        continue
    Q = [k for k in range(n) if k not in P]
    Omega = [k for k in Q if random.random() < 0.5]
    r = kappa(nu, Phi, P, Omega)
    if r is None:
        continue
    K0, A, th, PhiP2, S = r
    M = th/(A + th); C = A/(A + th)
    X = C*S/(th**2*PhiP2)
    h = mp.mpf('1e-30')
    # (a) peak push: zeta(c) += s  <=> nu_c += s/Phi_c^2
    c = max(P, key=lambda k: nu[k])
    nup = list(nu); nup[c] += h/Phi[c]**2
    num = list(nu); num[c] -= h/Phi[c]**2
    rp = kappa(nup, Phi, P, Omega); rm = kappa(num, Phi, P, Omega)
    if rp and rm:
        fd = (rp[0] - rm[0])/(2*h)
        worst1 = max(worst1, abs(fd - (1 - X))/max(1, abs(1 - X))); n1 += 1
    # (b) dropped strict non-peak push
    drop = [k for k in Q if k not in Omega]
    if drop:
        d = drop[0]
        nup = list(nu); nup[d] += h/Phi[d]**2
        num = list(nu); num[d] -= h/Phi[d]**2
        rp = kappa(nup, Phi, P, Omega); rm = kappa(num, Phi, P, Omega)
        if rp and rm:
            fd = (rp[0] - rm[0])/(2*h)
            pred = (nu[d]/th)*(2 + M*X/C)
            worst2 = max(worst2, abs(fd - pred)/max(1, abs(pred))); n2 += 1
    # (c) kept strict non-peak push
    if Omega:
        d = Omega[0]
        nup = list(nu); nup[d] += h/Phi[d]**2
        num = list(nu); num[d] -= h/Phi[d]**2
        rp = kappa(nup, Phi, P, Omega); rm = kappa(num, Phi, P, Omega)
        if rp and rm:
            fd = (rp[0] - rm[0])/(2*h)
            pred = (nu[d]/th)*M*X/C
            worst3 = max(worst3, abs(fd - pred)/max(1, abs(pred))); n3 += 1
print('peak push tests', n1, 'max rel err', mp.nstr(worst1, 5))
print('dropped SNP push tests', n2, 'max rel err', mp.nstr(worst2, 5))
print('kept SNP push tests', n3, 'max rel err', mp.nstr(worst3, 5))
