"""X1 check of Lemma K: k = K(sigma, R^2) = [sigma + sqrt(sigma^2 R^2 + sigma(1-R^2))]/(1-R^2), sigma = Phi_P^2 + s_f,
and the uniform form a^2 = sum_k Phi_k^2 min(rho_k,1)^2.  Block solver copied from the referee's status_rigidity.py."""
import mpmath as mp, random
mp.mp.dps = 50
random.seed(17)
def solve_block(zeta, Phi):
    n = len(zeta); nu = [abs(zeta[k]) / Phi[k]**2 for k in range(n)]
    def parts(th):
        mins = [min(mp.mpf(1), nu[k] / th) for k in range(n)]
        s = mp.sqrt(mp.fsum(Phi[k]**2 * mins[k]**2 for k in range(n)))
        M = 1 / (1 + s); C = 1 - M
        A = M * mp.fsum(abs(zeta[k]) * mins[k] for k in range(n))
        return A, M, C
    lo, hi = mp.mpf('1e-45'), max(nu) * 10 + 10
    for _ in range(400):
        mid = (lo + hi) / 2; A, M, C = parts(mid)
        if mid - A * M / C > 0: hi = mid
        else: lo = mid
    th = (lo + hi) / 2; A, M, C = parts(th)
    return A, th, M, C, nu
def K(sig, R2): return (sig + mp.sqrt(sig**2*R2 + sig*(1-R2)))/(1-R2)
worst = [0, 0]; n = 0
for trial in range(300):
    nn = random.randint(4, 9); m = random.randint(1, 3)
    Phi = [mp.mpf(2)**(-(m+k+1))*mp.mpf(random.uniform(0.2, 1)) for k in range(nn)]
    zeta = [mp.mpf(random.choice([-1,1]))*Phi[k]**2*mp.mpf(random.uniform(0.0, 3.0)) for k in range(nn)]
    A, th, M, C, nu = solve_block(zeta, Phi)
    P = [k for k in range(nn) if nu[k] >= th]; Q = [k for k in range(nn) if nu[k] < th]
    if not P or not Q: continue
    Omega = [k for k in Q if random.random() < 0.7] or [Q[0]]
    Sf = mp.fsum((nu[k]*Phi[k])**2 for k in Q if k not in Omega); PhiP2 = mp.fsum(Phi[k]**2 for k in P)
    kap = (A*(A+th) - mp.fsum((nu[k]*Phi[k])**2 for k in Omega))/th
    lam = [m*Phi[k] for k in range(nn)]
    R2 = m**2*mp.fsum(((zeta[k]/lam[k])/kap)**2 for k in Omega)
    sig = PhiP2 + Sf/th**2
    e1 = abs(kap/th - K(sig, R2))/(kap/th)
    E = mp.fsum(Phi[k]**2*min(mp.mpf(1), nu[k]/th)**2 for k in range(nn))
    e2 = abs((A/th)**2 - E)/E
    worst = [max(worst[0], e1), max(worst[1], e2)]; n += 1
print('blocks', n, 'max rel err K closed form', mp.nstr(worst[0], 3), ' uniform form a^2 = E', mp.nstr(worst[1], 3))
