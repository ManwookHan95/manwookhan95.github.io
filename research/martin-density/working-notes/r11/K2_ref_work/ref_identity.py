"""K2 referee: independent checks of Lemma K2.2 (identity + split form (2.1)), Lemma K2.3 in the SIGNED form
(kappa_u >= 0: sum_{s<=D} (c_s)_- >= <U*u,e> - u(zhat) - tail;  kappa_u <= 0: sum (c_s)_+ >= |<U*u,e>| + u(zhat) - tail),
and Lemma K2.4 (first-order actions of mass changes / banks / z-moves) in 50-digit arithmetic, with the corrected
composite-move sign (z-branch z_s -> z_s (1 + P), P <= 0).
Diagonal base U k_s = mu_s e_s.  Rows: a with q*(a) = ||a||_1 + ||mu a|| = 1, z = sgn a on F, |z| <= 1.
"""
import numpy as np
import mpmath as mp
rng = np.random.default_rng(11)
mp.mp.dps = 50

def row(n, pF, pC):
    A = np.zeros(n); z = np.zeros(n)
    for s in range(n):
        r = rng.random()
        if r < pF:
            A[s] = rng.uniform(-1, 1) * 2.0**(-0.3 * s); z[s] = np.sign(A[s])
        elif r < pF + pC:
            z[s] = rng.choice([-1.0, 1.0])
        else:
            z[s] = rng.uniform(-0.95, 0.95)
    if not A.any():
        A[0] = 0.5; z[0] = 1.0
    return A, z

def normalize(A, mu):
    q = np.abs(A).sum() + np.linalg.norm(mu * A)
    return A / q

worst_id, worst_split, viol_pos, viol_neg, ntest = 0.0, 0.0, 0, 0, 0
for trial in range(2000):
    n = int(rng.integers(5, 60))
    mu = 0.3 * 2.0**(-0.5 * np.arange(n)) * rng.uniform(0.5, 1, n)
    A, z = row(n, rng.uniform(0.1, 0.7), rng.uniform(0.1, 0.6))
    a = normalize(A, mu)
    nu = np.linalg.norm(mu * a); e = mu * a / nu
    zhat = z + mu * e
    u = rng.normal(size=n) * 2.0**(-0.2 * np.arange(n))
    gam = (mu * u) @ e
    kap = gam / nu
    F = a != 0
    lhs = u @ zhat
    rhs = kap + ((u - kap * a) * np.sign(a))[F].sum() + (u * z)[~F].sum()
    worst_id = max(worst_id, abs(lhs - rhs))
    c = np.where(F, (u - kap * a) * np.sign(a), u * z)
    for D in range(1, n + 1):
        alpha = np.abs(a[D:]).sum()
        split = kap * (1 - alpha) + c[:D].sum() + (u[D:] * z[D:]).sum()
        worst_split = max(worst_split, abs(split - lhs))
        tail = np.abs(u[D:]).sum()
        ntest += 1
        if gam >= 0:
            if np.clip(-c[:D], 0, None).sum() < gam - lhs - tail - 1e-12: viol_pos += 1
        else:
            if np.clip(c[:D], 0, None).sum() < -gam + lhs - tail - 1e-12: viol_neg += 1
print("K2.2 identity: max |u(zhat) - rhs| =", worst_id)
print("K2.2 split form (2.1): max error =", worst_split)
print("K2.3 signed form: tests", ntest, " violations (kappa>=0, negative parts):", viol_pos, " (kappa<=0, positive parts):", viol_neg)

# Lemma K2.4 in 50 digits
def val_mp(Amp, zmp, mump, ump):
    q = sum(abs(x) for x in Amp) + mp.sqrt(sum((m * x)**2 for m, x in zip(mump, Amp)))
    a = [x / q for x in Amp]
    nu = mp.sqrt(sum((m * x)**2 for m, x in zip(mump, a)))
    e = [m * x / nu for m, x in zip(mump, a)]
    return sum(uu * (zz + m * ee) for uu, zz, m, ee in zip(ump, zmp, mump, e)), a, nu, e

worst_rel = 0.0
for trial in range(150):
    n = int(rng.integers(5, 25))
    mu = 0.3 * 2.0**(-0.5 * np.arange(n)) * rng.uniform(0.5, 1, n)
    A, z = row(n, 0.4, 0.4)
    u = rng.normal(size=n)
    Amp = [mp.mpf(x) for x in A]; zmp = [mp.mpf(x) for x in z]; mump = [mp.mpf(x) for x in mu]; ump = [mp.mpf(x) for x in u]
    v0, a, nu, e = val_mp(Amp, zmp, mump, ump)
    q = sum(abs(x) for x in Amp) + mp.sqrt(sum((m * x)**2 for m, x in zip(mump, Amp)))
    kap = sum(m * uu * ee for m, uu, ee in zip(mump, ump, e)) / nu
    h = mp.mpf('1e-20')
    for s in range(n):
        if A[s] != 0:      # (i) mass change at a support coordinate (in normalized units: dm = h)
            A2 = list(Amp); A2[s] += h * q * mp.sign(Amp[s])
            pred = mump[s]**2 / nu * (ump[s] - kap * a[s]) * h * mp.sign(Amp[s])
            v2 = val_mp(A2, zmp, mump, ump)[0]
        elif abs(z[s]) == 1:   # (ii) bank at a contact, mass of sign z_s; and composite z-branch (inward)
            A2 = list(Amp); A2[s] = zmp[s] * h * q
            pred = mump[s]**2 / nu * ump[s] * zmp[s] * h
            v2 = val_mp(A2, zmp, mump, ump)[0]
            # composite: bank branch P > 0 with mass (nu/mu^2) P z_s ; z-branch P < 0: z_s -> z_s (1 + P)
            P = h
            A3 = list(Amp); A3[s] = zmp[s] * (nu / mump[s]**2) * P * q
            v3 = val_mp(A3, zmp, mump, ump)[0]
            z4 = list(zmp); z4[s] = zmp[s] * (1 - P)
            v4 = val_mp(Amp, z4, mump, ump)[0]
            slope_plus = (v3 - v0) / P; slope_minus = (v0 - v4) / P
            worst_rel = max(worst_rel, float(abs(slope_plus - ump[s] * zmp[s]) / (abs(ump[s]) + 1e-30)),
                            float(abs(slope_minus - ump[s] * zmp[s]) / (abs(ump[s]) + 1e-30)))
        else:                   # (iii) z-move at a free coordinate
            z2 = list(zmp); z2[s] += h
            pred = ump[s] * h
            v2 = val_mp(Amp, z2, mump, ump)[0]
        rel = abs((v2 - v0) - pred) / (abs(pred) + mp.mpf('1e-45'))
        worst_rel = max(worst_rel, float(rel))
print("K2.4 first-order actions (incl. composite with corrected sign), max relative error:", worst_rel)
