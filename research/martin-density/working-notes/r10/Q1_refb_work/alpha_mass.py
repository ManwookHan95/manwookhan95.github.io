"""Referee (b): alpha-mass identity  sum_{k in P} (rho_k - 1) Phi_k^2 = C/M  (P = peak set, rho = nu/theta), and the bound
R^2 <= 1 - sigma used for K_kappa (Lemma K: a^2 = sigma + k^2 R^2, k = a + sigma, sigma = Phi_P^2 + sum_{non-peaks outside Omega} rho^2 Phi^2;
here Omega := all strict non-peaks, so sigma = Phi_P^2).  Independent block solver as in clamp_check.py, 50 digits, random blocks."""
import mpmath as mp, random
mp.mp.dps = 50
random.seed(5)

def solve(Phi, zeta):
    nu = [abs(z)/p**2 for z, p in zip(zeta, Phi)]
    def parts(th):
        S1 = mp.fsum(p**2*min(1, n/th)**2 for p, n in zip(Phi, nu))
        S2 = mp.fsum(abs(z)*min(1, n/th) for z, n in zip(zeta, nu))
        return th - S2/(mp.sqrt(S1)*(1 + mp.sqrt(S1))), S1, S2
    lo, hi = mp.mpf(10)**-40, max(nu)*10
    for _ in range(400):
        mid = mp.sqrt(lo*hi) if hi/lo > 4 else (lo + hi)/2
        if parts(mid)[0] < 0: lo = mid
        else: hi = mid
    th = (lo + hi)/2
    _, S1, S2 = parts(th)
    M = 1/(1 + mp.sqrt(S1)); C = M*mp.sqrt(S1)
    return th, M, C, [n/th for n in nu]

worst_id = 0; worst_R = 1
for trial in range(300):
    m = random.randint(1, 4); K = random.randint(3, 25)
    Phi = [mp.mpf(2)**(-m-k-1)*mp.mpf(random.uniform(0.05, 1)) for k in range(K)]
    zeta = [m*p*mp.mpf(random.uniform(-1.25, 1.25)) for p in Phi]
    th, M, C, rho = solve(Phi, zeta)
    P = [k for k in range(K) if rho[k] >= 1]
    lhs = mp.fsum((rho[k] - 1)*Phi[k]**2 for k in P)
    worst_id = max(worst_id, abs(lhs - C/M)/(C/M))
    # Lemma K quantities with Omega = strict non-peaks: a = C/M, sigma = Phi_P^2, k^2 R^2 = sum_Omega rho^2 Phi^2
    a = C/M; sigma = mp.fsum(Phi[k]**2 for k in P)
    kR2 = mp.fsum(rho[k]**2*Phi[k]**2 for k in range(K) if rho[k] < 1)
    k_ = a + sigma; R2 = kR2/k_**2
    assert abs(a**2 - (sigma + kR2)) < mp.mpf(10)**-35*a**2, (a**2, sigma + kR2)
    worst_R = min(worst_R, (1 - R2) - sigma)
print("alpha-mass identity: max rel err", mp.nstr(worst_id, 3), "over 300 random blocks")
print("min over blocks of (1 - R^2) - sigma =", mp.nstr(worst_R, 5), "(claim >= 0)")
