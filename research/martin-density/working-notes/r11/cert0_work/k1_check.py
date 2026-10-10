"""
cert0: independent check of K1 (formula-1 kappa with the pattern's Omega, Omega meeting P), Lemma K, Lemma F, and the KN-1
sensitivity (inactive Omega values enter the active statuses only through R^2).

Block solver (lem:threshold): |w(k)| = M min(1, nu_k/theta), nu_k = |zeta_k|/Phi_k^2, theta = A M/C, C = M sqrt(S_1), M + C = 1,
A = M S_2;  theta solves theta = S_2/(sqrt(S_1)(1 + sqrt(S_1))) with S_1 = sum Phi^2 min(1,nu/theta)^2, S_2 = sum |zeta| min(1,nu/theta).
(written from the statement of lem:threshold; independent of the earlier solvers)
"""
import mpmath as mp
import random
mp.mp.dps = 60
random.seed(11)

def solve_block(Phi, zeta):
    nu = [abs(z) / p ** 2 for z, p in zip(zeta, Phi)]
    def g(th):
        S1 = mp.fsum(p ** 2 * min(1, n / th) ** 2 for p, n in zip(Phi, nu))
        S2 = mp.fsum(abs(z) * min(1, n / th) for z, n in zip(zeta, nu))
        return th - S2 / (mp.sqrt(S1) * (1 + mp.sqrt(S1)))
    lo, hi = mp.mpf('1e-40'), max(nu) * 10
    # g(lo) < 0, g(hi) > 0 ; g is increasing (bisection)
    for _ in range(400):
        mid = (lo + hi) / 2
        if g(mid) > 0:
            hi = mid
        else:
            lo = mid
    th = (lo + hi) / 2
    S1 = mp.fsum(p ** 2 * min(1, n / th) ** 2 for p, n in zip(Phi, nu))
    S2 = mp.fsum(abs(z) * min(1, n / th) for z, n in zip(zeta, nu))
    M = 1 / (1 + mp.sqrt(S1)); C = 1 - M; A = M * S2
    return th, A, M, C, nu

def Kfun(s, x):
    return (s + mp.sqrt(s ** 2 * x + s * (1 - x))) / (1 - x)

def random_block(n=9):
    Phi = [mp.mpf(random.uniform(0.02, 0.25)) for _ in range(n)]
    zeta = [mp.mpf(random.uniform(-1, 1)) * Phi[i] ** 2 * random.choice([0.2, 1, 3, 10]) for i in range(n)]
    return Phi, zeta

def k1_test(Phi, zeta, Omega):
    th, A, M, C, nu = solve_block(Phi, zeta)
    rho = [n / th for n in nu]
    P = [k for k in range(len(Phi)) if rho[k] >= 1]
    kappa = (A * (A + th) - mp.fsum(nu[k] ** 2 * Phi[k] ** 2 for k in Omega)) / th
    k = kappa / th; a = A / th
    R2 = mp.fsum(nu[l] ** 2 * Phi[l] ** 2 for l in Omega) / kappa ** 2          # = m^2 sum r_l^2
    sf = mp.fsum(rho[q] ** 2 * Phi[q] ** 2 for q in range(len(Phi)) if q not in P and q not in Omega)
    sig = mp.fsum(Phi[p] ** 2 for p in P if p not in Omega) + mp.fsum((1 - rho[l] ** 2) * Phi[l] ** 2 for l in Omega if l in P) + sf
    e1 = abs(a ** 2 - (sig + k ** 2 * R2))
    e2 = abs(k - (a + sig))
    e3 = abs(k - Kfun(sig, R2)) / k
    # identity check theta = A M / C
    e0 = abs(th - A * M / C) / th
    return (e0, e1, e2, e3, sig), len([l for l in Omega if l in P])

if __name__ == "__main__":
    worst = 0; n_meet = 0; trials = 0
    for t in range(60):
        Phi, zeta = random_block()
        th, A, M, C, nu = solve_block(Phi, zeta)
        rho = [n / th for n in nu]
        P = [k for k in range(len(Phi)) if rho[k] >= 1]
        Q = [k for k in range(len(Phi)) if rho[k] < 1]
        # Omega: random subset of Q plus (to test K1) possibly one peak which is not the only peak
        Omega = [q for q in Q if random.random() < 0.6]
        if len(P) >= 2 and random.random() < 0.7:
            # K1 situation: make the weakest peak a WEAK peak (rho in [1, 1.05]) and put it into Omega
            pw = sorted(P, key=lambda p: rho[p])[0]
            target = 1 + random.uniform(0, 0.05)
            # rescale zeta_pw (iterate: theta moves slightly)
            for _ in range(60):
                th2, A2, M2, C2, nu2 = solve_block(Phi, zeta)
                zeta[pw] = zeta[pw] * target / (nu2[pw] / th2)
            th, A, M, C, nu = solve_block(Phi, zeta)
            rho = [n / th for n in nu]
            P = [k for k in range(len(Phi)) if rho[k] >= 1]
            Q = [k for k in range(len(Phi)) if rho[k] < 1]
            Omega = [q for q in Omega if q in Q]
            if pw in P:
                Omega.append(pw)
        if not Omega:
            continue
        errs, meet = k1_test(Phi, zeta, Omega)
        err = max(errs[:4])
        if err > 1e-40:
            print('  large error', [mp.nstr(e, 3) for e in errs], 'meet', meet)
        worst = max(worst, err); n_meet += (meet > 0); trials += 1
    print(f"K1/Lemma K identities: {trials} blocks ({n_meet} with Omega ∩ P nonempty): max error {mp.nstr(worst, 3)}")

    # Lemma F + KN-1 sensitivity: one block, active set Omega_a, one inactive Omega carrier i with value v_i.
    # Statuses at FIXED active ratios r (values rescaled to keep u_l/kappa fixed) as the inactive value varies.
    Phi = [mp.mpf(x) for x in ['0.20', '0.15', '0.12', '0.10', '0.08', '0.06']]
    # carrier 0: robust peak; 1, 2: active (2 near threshold); 3: inactive (held); 4, 5: small
    def statuses_at_fixed_ratio(v_inactive, r_target):
        # find zeta with zeta_0 robust, zeta_1, zeta_2 such that r_l = zeta_l/(Phi_l kappa) (m = 1) equals r_target, zeta_3 = v_inactive
        z = [mp.mpf('0.2'), mp.mpf('0.004'), mp.mpf('0.004'), v_inactive, mp.mpf('1e-6'), mp.mpf('-1e-6')]
        Omega = [1, 2, 3, 4, 5]
        for it in range(200):
            th, A, M, C, nu = solve_block(Phi, z)
            kappa = (A * (A + th) - mp.fsum(nu[k] ** 2 * Phi[k] ** 2 for k in Omega)) / th
            new = list(z)
            new[1] = r_target[0] * Phi[1] * kappa
            new[2] = r_target[1] * Phi[2] * kappa
            if max(abs(new[i] - z[i]) for i in (1, 2)) < mp.mpf(10) ** -50:
                break
            z = new
        th, A, M, C, nu = solve_block(Phi, z)
        rho = [n / th for n in nu]
        P = [k for k in range(len(Phi)) if rho[k] >= 1]
        sig_rob = Phi[0] ** 2
        Ra2 = (r_target[0] ** 2 + r_target[1] ** 2)
        floor2 = abs(r_target[1]) * Kfun(sig_rob, Ra2) / Phi[2]
        return rho, P, floor2
    # pick r so that carrier 2 sits near threshold
    rt = [mp.mpf('0.02'), mp.mpf('0.0')]
    # calibrate r_2 so that the floor status of carrier 2 is 1 - 1e-6 (a 'Puiseux margin' mu = 1e-6)
    sig_rob = Phi[0] ** 2
    lo, hi = mp.mpf('1e-6'), mp.sqrt(1 - rt[0]**2) * mp.mpf('0.999')
    for _ in range(200):
        mid = (lo + hi) / 2
        val = mid * Kfun(sig_rob, rt[0] ** 2 + mid ** 2) / Phi[2]
        if val > 1 - mp.mpf('1e-6'):
            hi = mid
        else:
            lo = mid
    rt[1] = (lo + hi) / 2
    print("\nKN-1 sensitivity (fixed active ratios; carrier 2 floor status = 1 - 1e-6):")
    for vin in [mp.mpf(0), mp.mpf('1e-9'), mp.mpf('1e-7'), mp.mpf('1e-5'), mp.mpf('1e-4')]:
        rho, P, floor2 = statuses_at_fixed_ratio(vin, rt)
        print(f"  inactive value {mp.nstr(vin,2):>6}: rho_2 = 1 - {mp.nstr(1 - rho[2], 6):>12}  (floor 1 - {mp.nstr(1 - floor2, 6)}),"
              f" rho_2 - floor = {mp.nstr(rho[2] - floor2, 4)}, peaks = {P}")
