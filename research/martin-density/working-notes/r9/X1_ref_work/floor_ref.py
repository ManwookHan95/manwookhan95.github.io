"""X1-ref check of Lemma F (floor lemma), the (T)-block deviation estimate and the (U)-block rescaling, with the independent
(E1)/(E2) solver of indep_block.py.

Construction of a block state with PRESCRIBED active ratios r_a (r = u(zhat)/kappa, kappa computed with Omega = Q): fixed point
zeta_l := lambda_l r_l kappa(zeta) for the active carriers; peaks and inactive carriers have prescribed values.
Tests:
 (a) rho_l >= floor m|r_l| K(sigma_rob, R_a^2)/Phi_l for every active l, for random inactive masses (robust, near-threshold,
     nearly neutral) and extra non-robust peaks; equality when inactive values are 0 and P = P_rob.
 (b) (T)-block deviation: with inactive carriers at rho <= b only, (rho - floor)/floor = O(b^2) (they enter R^2 through rho^2 Phi^2).
 (c) a weak peak (rho in [1, 1+b]) counted as a peak instead of as an Omega member changes the floor by O(b).
 (d) (U)-block rescaling r -> s r at fixed peaks: every active rho decreases by a factor <= s.
"""
import mpmath as mp, random
src = open('indep_block.py').read().split('# ---------- (1)')[0]
ns = {}; exec(src, ns); solve_E = ns['solve_E']; K = ns['K']
mp.mp.dps = 40
random.seed(99)

def state_with_ratios(Phi, m, fixed, act, r, iters=200):
    """fixed: dict k -> zeta value (peaks, inactive); act: active indices with target ratios r[l]."""
    n = len(Phi); lam = [m * Phi[k] for k in range(n)]
    z = [mp.mpf(0)] * n
    for k, v in fixed.items(): z[k] = v
    kap = mp.mpf(1)
    for it in range(iters):
        for l in act: z[l] = lam[l] * r[l] * kap
        A, th, M, C, nu, P = solve_E(z, Phi)
        Q = [k for k in range(n) if k not in P]
        kap_new = (A * (A + th) - mp.fsum((nu[k] * Phi[k])**2 for k in Q)) / th
        if abs(kap_new - kap) < mp.mpf(10)**(-36) * kap: kap = kap_new; break
        kap = kap_new
    for l in act: z[l] = lam[l] * r[l] * kap
    A, th, M, C, nu, P = solve_E(z, Phi)
    return z, A, th, M, C, nu, P, kap

okA = True; worst_eq = mp.mpf(0); ntests = 0
devs_b = []; devs_peak = []; okU = True
for trial in range(400):
    m = random.randint(1, 3); n = 8
    Phi = [mp.mpf(2)**(-(m + k + 1)) * mp.mpf(random.uniform(0.4, 1)) for k in range(n)]
    lam = [m * Phi[k] for k in range(n)]
    # carriers: 0,1 robust peaks; 2,3 active; 4,5,6 inactive; 7 spare
    peaks = {0: Phi[0]**2 * mp.mpf(random.uniform(30, 60)), 1: -Phi[1]**2 * mp.mpf(random.uniform(30, 60))}
    act = [2, 3]
    # choose ratios so that active carriers are moderately strong
    r = {2: mp.mpf(random.uniform(0.3, 0.9)) * Phi[2] / m, 3: -mp.mpf(random.uniform(0.3, 0.9)) * Phi[3] / m}
    base = dict(peaks)
    z0, A0, th0, M0, C0, nu0, P0, kap0 = state_with_ratios(Phi, m, base, act, r)
    if sorted(P0) != [0, 1]: continue
    sig_rob = Phi[0]**2 + Phi[1]**2
    R2a = m**2 * (r[2]**2 + r[3]**2)
    floor = {l: m * abs(r[l]) * K(sig_rob, R2a) / Phi[l] for l in act}
    rho0 = {l: nu0[l] / th0 for l in act}
    worst_eq = max(worst_eq, max(abs(rho0[l] - floor[l]) / floor[l] for l in act))
    # (a) random inactive masses (scaled relative to theta Phi^2)
    fx = dict(base)
    for k in (4, 5, 6):
        fx[k] = mp.mpf(random.choice([-1, 1])) * th0 * Phi[k]**2 * mp.mpf(random.choice([random.uniform(0, 0.01), random.uniform(0.2, 0.9), random.uniform(0.97, 1.05)]))
    z1, A1, th1, M1, C1, nu1, P1, kap1 = state_with_ratios(Phi, m, fx, act, r)
    if not all(l not in P1 for l in act) or not {0, 1} <= set(P1): continue
    for l in act:
        if nu1[l] / th1 < floor[l] * (1 - mp.mpf(10)**(-30)): okA = False
    ntests += 1
    # (b) inactive carriers nearly neutral at relative position b
    for b in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
        fb = dict(base)
        for k in (4, 5, 6): fb[k] = th0 * Phi[k]**2 * b      # rho ~ b (theta moves only slightly)
        zb, Ab, thb, Mb, Cb, nub, Pb, kapb = state_with_ratios(Phi, m, fb, act, r)
        dev = max((nub[l] / thb - floor[l]) / floor[l] for l in act)
        devs_b.append((float(b), float(dev)))
    # (c) a weak peak: carrier 7 at rho slightly above 1, counted as a peak at f; floor computed with sigma_rob
    for b in (mp.mpf('1e-2'), mp.mpf('1e-3')):
        fc = dict(base); fc[7] = th0 * Phi[7]**2 * (1 + b)
        zc, Ac, thc, Mc, Cc, nuc, Pc, kapc = state_with_ratios(Phi, m, fc, act, r)
        if 7 not in Pc: continue
        rho7 = nuc[7] / thc
        # floor treating 7 as an active Omega member with its ratio (u_7/kappa)
        r7 = (zc[7] / lam[7]) / kapc
        R2a7 = R2a + m**2 * r7**2
        fl = {l: m * abs(r[l]) * K(sig_rob, R2a7) / Phi[l] for l in act}
        dev = max(abs(nuc[l] / thc - fl[l]) / fl[l] for l in act)
        devs_peak.append((float(rho7 - 1), float(dev)))
    # (d) (U)-block rescaling of the active ratios by s
    s = mp.mpf('0.99')
    rs = {l: s * r[l] for l in act}
    zs, As, ths, Ms, Cs, nus, Ps, kaps = state_with_ratios(Phi, m, base, act, rs)
    for l in act:
        if not (nus[l] / ths <= s * rho0[l] * (1 + mp.mpf(10)**(-30))): okU = False
print("(a) tests %d: every active rho >= floor: %s; equality case (no inactive mass, P = P_rob) max rel err %s"
      % (ntests, okA, mp.nstr(worst_eq, 3)))
import collections
agg = collections.defaultdict(list)
for b, d in devs_b: agg[b].append(d)
print("(b) nearly neutral inactive carriers at rho ~ b: max (rho - floor)/floor:",
      {b: "%.2e" % max(v) for b, v in sorted(agg.items())}, "(ratio to b^2: %s)" % {b: "%.2f" % (max(v) / b**2) for b, v in sorted(agg.items())})
agg2 = collections.defaultdict(list)
for e, d in devs_peak: agg2[round(e, 3)].append(d)
print("(c) weak peak at rho = 1 + b counted as peak vs Omega member: max rel floor change by b:", {k: "%.2e" % max(v) for k, v in sorted(agg2.items())})
print("(d) (U)-rescaling r -> 0.99 r lowers every active rho by a factor <= 0.99:", okU)
