"""X1-ref: an ACTIVE WEAK PEAK l (rho_l in [1, 1+b]) and the floor.  With kappa defined by U1 Lemma 1.3's first formula
kappa_Omega = [A(A + theta) - sum_{Omega} nu^2 Phi^2]/theta  (Omega containing l although l is a peak at f), Lemma K holds with
sigma' = Phi_{P minus l}^2 + (1 - rho_l^2) Phi_l^2 + s_f, so |rho - floor| = O(b) for all active carriers.  With the PEAK
convention (kappa computed with l in P, i.e. Omega without l) the ratios of the whole block differ by a relative O(Phi_l^2/k):
this is NOT small, so the convention matters."""
import mpmath as mp, random
src = open('indep_block.py').read().split('# ---------- (1)')[0]
ns = {}; exec(src, ns); solve_E = ns['solve_E']; K = ns['K']
mp.mp.dps = 40; random.seed(5)
res = []
for trial in range(300):
    m = random.randint(1, 2); n = 6
    Phi = [mp.mpf(2)**(-(m + k + 1)) * mp.mpf(random.uniform(0.5, 1)) for k in range(n)]
    lam = [m * Phi[k] for k in range(n)]
    z = [mp.mpf(0)] * n
    z[0] = Phi[0]**2 * mp.mpf(random.uniform(20, 40))                      # robust peak
    z[2] = -Phi[2]**2 * mp.mpf(random.uniform(0.1, 1)); z[3] = Phi[3]**2 * mp.mpf(random.uniform(0.1, 1))  # active non-peaks (scaled later)
    A, th, M, C, nu, P = solve_E(z, Phi)
    for b in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
        # put carrier 1 at rho = 1 + b/2 (fixed point in theta)
        for it in range(80):
            z[1] = th * Phi[1]**2 * (1 + b / 2)
            A, th_new, M, C, nu, P = solve_E(z, Phi)
            if abs(th_new - th) < mp.mpf(10)**(-35) * th: th = th_new; break
            th = th_new
        A, th, M, C, nu, P = solve_E(z, Phi)
        if sorted(P) != [0, 1]: continue
        Om = [1, 2, 3]                                                     # active: the weak peak 1 and carriers 2, 3
        kap1 = (A * (A + th) - mp.fsum((nu[k] * Phi[k])**2 for k in Om)) / th            # formula-1 convention
        kapP = (A * (A + th) - mp.fsum((nu[k] * Phi[k])**2 for k in [2, 3])) / th        # peak convention for carrier 1
        r1 = {k: (z[k] / lam[k]) / kap1 for k in Om}
        R2 = m**2 * mp.fsum(r1[k]**2 for k in Om)
        fl = {k: m * abs(r1[k]) * K(Phi[0]**2, R2) / Phi[k] for k in Om}
        dev = max(abs(nu[k] / th - fl[k]) / fl[k] for k in Om)
        conv = abs(kap1 - kapP) / kapP
        res.append((float(b), float(dev), float(conv)))
import collections
agg = collections.defaultdict(list)
for b, d, c in res: agg[b].append((d, c))
for b in sorted(agg):
    print("b = %.0e: max |rho - floor|/floor (formula-1 convention) = %.2e ; relative kappa change between conventions: min %.2e max %.2e"
          % (b, max(d for d, c in agg[b]), min(c for d, c in agg[b]), max(c for d, c in agg[b])))
