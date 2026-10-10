"""Numerical check of Lemma 3.4 of Q2 part 3 (one-sided structure behind (NDN)).

Diagonal base U k_s = mu_s e_s.  Row data (a, z): zhat = z + U e, e = U* a/||U* a||.  A combination u with u|_F = kappa a|_F.
For rows (a1, z1) with z1 = z on supp u and supp a1 minus F disjoint from supp u, the identity
      u(zhat1) - u(zhat) = -(kappa nu/2) ||e1 - e||^2
must hold exactly.  We test random support moves (raises, lowerings, truncations to contacts, sign changes outside supp u),
masses off supp u, z-moves off supp u.  We also show that a mass ON supp u \ F (a bank) breaks the one-sidedness (first order).
"""
import numpy as np
rng = np.random.default_rng(3)
n = 40
mu = 0.5 * 0.7 ** np.arange(n)            # any positive diagonal base

def e_of(a):
    v = mu * a
    return v / np.linalg.norm(v)

def zhat_of(a, z):
    return z + mu * e_of(a)                # U e as a vector of coordinates: (U e)_s = mu_s e_s

worst = 0.0
for trial in range(200):
    F = np.sort(rng.choice(n, size=25, replace=False))
    a = np.zeros(n); a[F] = rng.choice([-1, 1], 25) * rng.uniform(0.01, 1, 25) * 0.8 ** F
    z = rng.uniform(-1, 1, n); z[F] = np.sign(a[F])
    kappa = rng.uniform(0.2, 3.0) * rng.choice([-1, 1])
    offF = np.setdiff1d(np.arange(n), F)
    suppu_off = rng.choice(offF, size=6, replace=False)      # u lives on F (proportional to a) and on 6 off-F coordinates
    u = np.zeros(n); u[F] = kappa * a[F]; u[suppu_off] = rng.standard_normal(6)
    nu = np.linalg.norm(mu * a)
    base = u @ zhat_of(a, z)
    # random admissible move
    a1 = a.copy(); z1 = z.copy()
    # support moves on F: raises/lowerings, some truncations to contacts (same sign kept in z1)
    for j in F:
        r = rng.random()
        if r < 0.3:
            a1[j] *= rng.uniform(1.0, 3.0)            # raise
        elif r < 0.5:
            a1[j] *= rng.uniform(0.05, 1.0)           # lowering
        elif r < 0.6:
            a1[j] = 0.0                               # truncation: contact of sign s_j (z1 unchanged)
    # sign change on F outside supp u: impossible here since u is nonzero on all of F (kappa a); skip
    # masses and z-moves OFF supp u
    free_off = np.setdiff1d(offF, suppu_off)
    for j in rng.choice(free_off, size=4, replace=False):
        if rng.random() < 0.5:
            sgn = rng.choice([-1, 1]); z1[j] = sgn; a1[j] = sgn * rng.uniform(0.001, 0.2)   # new support (mass) off supp u
        else:
            z1[j] = rng.uniform(-1, 1)                                                     # z-move off supp u
    if np.allclose(a1, 0):
        continue
    lhs = u @ zhat_of(a1, z1) - base
    rhs = -(kappa * nu / 2) * np.linalg.norm(e_of(a1) - e_of(a)) ** 2
    worst = max(worst, abs(lhs - rhs))
print("max |LHS - RHS| over 200 random admissible moves:", worst)

# counter-check: a bank ON supp u \ F changes the combination at first order, in either direction
F = np.arange(20); a = np.zeros(n); a[F] = rng.choice([-1, 1], 20) * 0.8 ** F
z = np.zeros(n); z[F] = np.sign(a[F]); z[30] = 1.0
u = np.zeros(n); u[F] = 2.0 * a[F]; u[30] = 0.7
base = u @ zhat_of(a, z)
for m in [1e-4, 1e-3, 1e-2]:
    a1 = a.copy(); a1[30] = m      # bank at the contact 30 (sign z_30 = +1) which lies in supp u
    print(f"bank mass {m:.0e} on supp u: change of u(zhat) = {u @ zhat_of(a1, z) - base:+.3e}  (first order, sign of z_30 u(30))")
