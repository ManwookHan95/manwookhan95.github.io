"""J2 numerics (sanity only): frozen block system with the TARGET pattern (P_f = robust peaks), Lemma J2.0 (first-order
action on relative positions), Lemma J2.1 (existence/uniqueness/consistency/frozen Lemma K), and the realization of a weak-peak
push either directly or by a threshold raise.  One Martin-type block: zeta_k = lambda_k u_k, lambda_k = m Phi_k.
High precision with mpmath (50 digits)."""
import mpmath as mp
import random
mp.mp.dps = 50
random.seed(12)

def true_block(zeta, Phi):
    """Threshold equation (Y2 Lemma T): theta = unique zero of Psi(th) = A(th)^2 - B(th)."""
    nu = [abs(z) / p**2 for z, p in zip(zeta, Phi)]
    def Psi(th):
        A = sum(max(abs(z) - th * p**2, 0) for z, p in zip(zeta, Phi))
        B = sum(p**2 * min(th, n)**2 for p, n in zip(Phi, nu))
        return A**2 - B
    lo, hi = mp.mpf('1e-30'), max(nu)
    for _ in range(400):
        mid = (lo + hi) / 2
        if Psi(mid) > 0: lo = mid
        else: hi = mid
    th = (lo + hi) / 2
    A = sum(max(abs(z) - th * p**2, 0) for z, p in zip(zeta, Phi))
    return th, A, nu

def frozen_block(zeta, Phi, Pf, fine):
    """Frozen system: coarse k in Pf counted as peaks, other coarse k as non-peaks, fine carriers truly."""
    nu = [abs(z) / p**2 for z, p in zip(zeta, Phi)]
    def Af(th):
        s = 0
        for k in range(len(zeta)):
            if k in fine: s += max(abs(zeta[k]) - th * Phi[k]**2, 0)
            elif k in Pf: s += abs(zeta[k]) - th * Phi[k]**2
        return s
    def Bf(th):
        s = 0
        for k in range(len(zeta)):
            if k in fine: s += Phi[k]**2 * min(th, nu[k])**2
            elif k in Pf: s += th**2 * Phi[k]**2
            else: s += nu[k]**2 * Phi[k]**2
        return s
    thmax = min(abs(zeta[k]) / Phi[k]**2 for k in Pf) * 4  # A_f > 0 region contains (0, thmax/4]
    # Psi_f strictly decreasing where A_f > 0; bisection on (0, th*) with A_f(th*) > 0
    lo, hi = mp.mpf('1e-30'), thmax
    while Af(hi) <= 0: hi = hi * 0.999
    assert Af(lo)**2 - Bf(lo) > 0, "no positive frozen root (Psi_f(0+) <= 0)"
    for _ in range(400):
        mid = (lo + hi) / 2
        if Af(mid)**2 - Bf(mid) > 0: lo = mid
        else: hi = mid
    th = (lo + hi) / 2
    return th, Af(th), nu

def Kfun(sig, R2):
    return (sig + mp.sqrt(sig**2 * R2 + sig * (1 - R2))) / (1 - R2)

def make_block(m, b, u):
    """coarse: 2 robust peaks (0,1), 2 weak peaks (2,3) with rho in (1,1+b), 4 strict non-peaks; 3 fine carriers. theta := 1."""
    Phi = [mp.mpf(random.uniform(0.05, 0.25)) for _ in range(8)] + [mp.mpf(random.uniform(1e-4, 1e-3)) for _ in range(3)]
    rho = [None, mp.mpf(random.uniform(1.5, 3.0)),
           1 + b * mp.mpf(random.uniform(0.05, 0.95)), 1 + b * mp.mpf(random.uniform(0.05, 0.95))] + \
          [mp.mpf(random.uniform(0.2, 0.9)) for _ in range(4)] + [mp.mpf(random.uniform(0.0, 0.5)) for _ in range(3)]
    # solve for rho_0 so that a = sum_P (rho-1)Phi^2 equals sqrt(Phi_P^2 + sum_Q rho^2 Phi^2)
    P = [0, 1, 2, 3]
    PhiP2 = sum(Phi[k]**2 for k in P)
    SQ = sum(rho[k]**2 * Phi[k]**2 for k in range(11) if k not in P)
    a = mp.sqrt(PhiP2 + SQ)
    rest = sum((rho[k] - 1) * Phi[k]**2 for k in P if k != 0)
    rho[0] = 1 + (a - rest) / Phi[0]**2
    assert rho[0] > 1 + u
    signs = [random.choice([-1, 1]) for _ in range(11)]
    zeta = [signs[k] * rho[k] * Phi[k]**2 for k in range(11)]   # theta = 1
    return zeta, Phi, rho

m = 2
b = mp.mpf('1e-3'); u = mp.mpf('0.1'); mu = mp.mpf('0.02')
fine = {8, 9, 10}; Pf = {0, 1}
worst = {}
def upd(key, v):
    worst[key] = max(worst.get(key, mp.mpf(0)), abs(v))

for trial in range(40):
    zeta, Phi, rho = make_block(m, b, u)
    th, A, nu = true_block(zeta, Phi)
    upd('true theta - 1 (construction)', th - 1)
    thf, Af, _ = frozen_block(zeta, Phi, Pf, fine)
    # (1) theta_f <= theta and size of the difference relative to b Phi_W^2/Phi_Pf^2
    PhiW2 = Phi[2]**2 + Phi[3]**2; PhiPf2 = Phi[0]**2 + Phi[1]**2
    assert thf <= th + mp.mpf('1e-40')
    upd('(theta - theta_f)/(theta b Phi_W^2/Phi_Pf^2)', (th - thf) / (th * b * PhiW2 / PhiPf2))
    # (2) frozen Lemma K: Omega := all coarse non-Pf carriers (incl. weak peaks)
    Om = [k for k in range(8) if k not in Pf]
    lam = [m * p for p in Phi]
    uval = [z / l for z, l in zip(zeta, lam)]
    SOm = sum(nu[k]**2 * Phi[k]**2 for k in Om)
    kap = Af + (Af**2 - SOm) / thf
    r = {k: uval[k] / kap for k in Om}
    R2 = m**2 * sum(r[k]**2 for k in Om)
    af, kf = Af / thf, kap / thf
    sig = (Af**2 - SOm) / thf**2
    upd('frozen Lemma K: a^2 - sigma - k^2 R^2', af**2 - sig - kf**2 * R2)
    upd('frozen Lemma K: k - a - sigma', kf - af - sig)
    upd('frozen Lemma K: k - K(sigma,R^2)', kf - Kfun(sig, R2))
    for k in Om:
        upd('frozen rho_l - m|r_l| K/Phi_l', nu[k] / thf - m * abs(r[k]) * kf / Phi[k])
    # sigma_f >= sigma_rob = Phi_Pf^2 (floor) and frozen statuses of weak peaks <= (1+b)(1 + C b)
    assert sig >= PhiPf2 - mp.mpf('1e-40')
    upd('max frozen rho of weak peaks - 1 (should be <= ~b(1+C))', max(nu[2], nu[3]) / thf - 1)
    # (3) realization A: push weak peaks DIRECTLY (lower |zeta|) until frozen rho = 1 - mu/2; then check consistency => frozen = true
    def zs(s):
        z = list(zeta)
        for k in (2, 3): z[k] = mp.sign(zeta[k]) * s * Phi[k]**2
        return z
    def gs(s):
        t, _, _ = frozen_block(zs(s), Phi, Pf, fine)
        return s / t - (1 - mu / 2)
    s_lo, s_hi = mp.mpf(0), mp.mpf(2)      # s/theta_f(s) increasing in s (Lemma J2.0: theta_f decreases when a frozen non-peak grows)
    for _ in range(200):
        mid = (s_lo + s_hi) / 2
        if gs(mid) > 0: s_hi = mid
        else: s_lo = mid
    z2 = zs((s_lo + s_hi) / 2)
    thf2, Af2, nu2 = frozen_block(z2, Phi, Pf, fine)
    th2, A2, _ = true_block(z2, Phi)
    cons = all(nu2[k] >= thf2 for k in Pf) and all(nu2[k] <= thf2 for k in range(8) if k not in Pf)
    assert cons
    upd('direct push: |theta_f - theta_true| (consistent frozen point)', thf2 - th2)
    upd('direct push: |A_f - A_true|', Af2 - A2)
    # (4) realization B: threshold raise -- raise robust peak 0 until both weak peaks have frozen rho <= 1 - mu/2
    z3 = list(zeta); s_lo, s_hi = mp.mpf(0), mp.mpf(10)
    def maxrho(s):
        z = list(zeta); z[0] = zeta[0] * (1 + s)
        t, _, n = frozen_block(z, Phi, Pf, fine)
        return max(n[2], n[3]) / t
    for _ in range(200):
        mid = (s_lo + s_hi) / 2
        if maxrho(mid) > 1 - mu / 2: s_lo = mid
        else: s_hi = mid
    s = s_hi; z3[0] = zeta[0] * (1 + s)
    thf3, Af3, nu3 = frozen_block(z3, Phi, Pf, fine)
    th3, A3, _ = true_block(z3, Phi)
    assert all(nu3[k] >= thf3 for k in Pf) and all(nu3[k] <= thf3 * (1 + mp.mpf('1e-40')) for k in range(8) if k not in Pf)
    upd('threshold raise: |theta_f - theta_true| at the end', thf3 - th3)
    # needed relative raise of |zeta_0| vs Lemma J2.0 prediction (first order): d log rho_k = -(a/(1+a)) dZ/(theta Phi'^2)
    a_true = A / th
    PhiP2true = sum(Phi[k]**2 for k in range(11) if nu[k] > th)
    dZ = abs(zeta[0]) * s
    pred = (mp.log(max(nu[2], nu[3]) / th) - mp.log(1 - mu / 2)) * th * PhiP2true * (1 + a_true) / a_true
    upd('threshold raise: dZ/predicted - 1 (first order, O(mu))', dZ / pred - 1)

# (5) Lemma J2.0: finite differences of theta (true) versus the formula, at generic points
for trial in range(20):
    zeta, Phi, rho = make_block(m, b, u)
    th, A, nu = true_block(zeta, Phi)
    P = [k for k in range(11) if nu[k] > th]; Q = [k for k in range(11) if k not in P]
    PhiP2 = sum(Phi[k]**2 for k in P)
    for j in range(11):
        h = mp.mpf('1e-25') * abs(zeta[j]) if zeta[j] != 0 else mp.mpf('1e-30')
        z = list(zeta); z[j] = zeta[j] + mp.sign(zeta[j]) * h
        th2, _, _ = true_block(z, Phi)
        fd = (th2 - th) / h
        formula = (A if j in P else -nu[j]) / (PhiP2 * (A + th))
        upd('Lemma J2.0: d theta/d|zeta_j| fd - formula (rel)', (fd - formula) / max(abs(formula), mp.mpf('1e-30')))
    upd('Lemma J2.0: Euler sum_j (d theta/d|zeta_j|)|zeta_j| - theta',
        sum(((A if j in P else -nu[j]) / (PhiP2 * (A + th))) * abs(zeta[j]) for j in range(11)) - th)

for key, v in worst.items():
    print(f"{key:70s} max = {mp.nstr(v, 5)}")
