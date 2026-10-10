"""X1 check of the floor lemma (part 1, Lemma F): at FIXED active ratios r_l = u_l/kappa (l in Omega_a), removing inactive Omega mass
(pushing inactive Omega carriers to value 0) lowers every active relative position rho_l, and the result equals the floor
rho^0_l = m |r_l| K(sigma, R_a^2)/Phi_l (sigma = Phi_P^2 + s_f).  Block solver as in the referee's status_rigidity.py (40 digits).
Fixed point: given target ratios r_a, iterate  zeta_l := lambda_l r_l kappa(zeta)  (kappa recomputed) until convergence."""
import mpmath as mp, random
mp.mp.dps = 34
random.seed(23)
def solve_block(zeta, Phi):
    n = len(zeta); nu = [abs(zeta[k]) / Phi[k]**2 for k in range(n)]
    def parts(th):
        mins = [min(mp.mpf(1), nu[k] / th) for k in range(n)]
        s = mp.sqrt(mp.fsum(Phi[k]**2 * mins[k]**2 for k in range(n)))
        M = 1 / (1 + s); C = 1 - M
        A = M * mp.fsum(abs(zeta[k]) * mins[k] for k in range(n)); return A, M, C
    lo, hi = mp.mpf('1e-38'), max(nu) * 10 + 10
    for _ in range(300):
        mid = (lo + hi) / 2; A, M, C = parts(mid)
        if mid - A * M / C > 0: hi = mid
        else: lo = mid
    th = (lo + hi) / 2; A, M, C = parts(th); return A, th, M, C, nu
def K(sig, R2): return (sig + mp.sqrt(sig**2*R2 + sig*(1-R2)))/(1-R2)
def kappa_of(zeta, Phi, Omega):
    A, th, M, C, nu = solve_block(zeta, Phi)
    return (A*(A+th) - mp.fsum((nu[k]*Phi[k])**2 for k in Omega))/th, th, nu
ntest = 0; nok = 0; worst_floor = mp.mpf(0); min_drop = mp.mpf(1)
for trial in range(3000):
    m = random.randint(1, 3); n = random.randint(5, 8)
    Phi = [mp.mpf(2)**(-(m+k+1))*mp.mpf(random.uniform(0.3, 1)) for k in range(n)]
    lam = [m*Phi[k] for k in range(n)]
    zeta = [mp.mpf(random.choice([-1,1]))*Phi[k]**2*mp.mpf(random.uniform(0.0, 6.0)) for k in range(n)]
    A, th, M, C, nu = solve_block(zeta, Phi)
    P = [k for k in range(n) if nu[k] >= th]; Q = [k for k in range(n) if nu[k] < th]
    if len(P) < 1 or len(Q) < 3: continue
    random.shuffle(Q); Oa = Q[:2]; Oin = Q[2:]          # active and inactive Omega carriers (Omega = Q here, s_f = 0)
    if max(nu[k]/th for k in Oin) < 0.05: continue       # want robust inactive mass
    Omega = Oa + Oin
    kap, th0, nu0 = kappa_of(zeta, Phi, Omega)
    r = {l: (zeta[l]/lam[l])/kap for l in Oa}
    rho_before = {l: nu0[l]/th0 for l in Oa}
    # remove inactive mass, then restore the active ratios by the fixed point
    z2 = list(zeta)
    for l in Oin: z2[l] = mp.mpf(0)
    for it in range(120):
        k2, th2, nu2 = kappa_of(z2, Phi, Omega)
        for l in Oa: z2[l] = lam[l]*r[l]*k2
    k2, th2, nu2 = kappa_of(z2, Phi, Omega)
    P2 = [k for k in range(n) if nu2[k] >= th2]
    if sorted(P2) != sorted(P): continue
    ntest += 1
    rho_after = {l: nu2[l]/th2 for l in Oa}
    rat_err = max(abs((z2[l]/lam[l])/k2 - r[l]) for l in Oa)
    sig = mp.fsum(Phi[k]**2 for k in P); R2a = m**2*mp.fsum(r[l]**2 for l in Oa)
    floor = {l: m*abs(r[l])*K(sig, R2a)/Phi[l] for l in Oa}
    e = max(abs(rho_after[l] - floor[l])/floor[l] for l in Oa)
    worst_floor = max(worst_floor, e)
    drop = min(rho_before[l] - rho_after[l] for l in Oa)
    min_drop = min(min_drop, drop)
    if drop > 0 and rat_err < mp.mpf('1e-30'): nok += 1
print('tests', ntest, 'all active rho decreased at fixed ratios:', nok == ntest, ' min decrease', mp.nstr(min_drop, 4))
print('max rel. error |rho_after - floor|/floor =', mp.nstr(worst_floor, 3))
