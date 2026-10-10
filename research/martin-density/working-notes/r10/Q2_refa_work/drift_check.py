"""Referee (a): independent check of Q2 Lemma 3.4 (exact drift identity) and of the necessity of its hypotheses.
Diagonal base U* e_s* = mu_s k_s.  u in l_1 with u|_F = kappa a|_F (finite combination is irrelevant: only u matters).
Identity: u(zhat^1) - u(zhat0) = -(kappa nu0/2) ||e^1 - e0||^2 whenever z^1 = z0 on supp u and (supp a^1 \ F) cap supp u = {}.
Also: (i) a mass at s in supp u \ F breaks it at first order; (ii) a z-change on supp u breaks it at first order; (iii) sweep of
de-proportionalizing moves: max of u(zhat^1) over random support moves never exceeds u(zhat0) for kappa > 0.
"""
import numpy as np
rng = np.random.default_rng(8)
n = 60
worst = 0.0; maxgain = -1.0
for trial in range(400):
    mu = 0.7 ** (np.arange(n) * rng.uniform(0.5, 1.0))
    F = np.sort(rng.choice(n, 20, replace=False))
    a0 = np.zeros(n); a0[F] = rng.choice([-1, 1], 20) * rng.uniform(0.01, 1, 20)
    a0 /= np.abs(a0).sum() + np.linalg.norm(mu * a0)
    z0 = rng.uniform(-1, 1, n); z0[F] = np.sign(a0[F])
    kappa = rng.choice([-1, 1]) * rng.uniform(0.2, 3)
    u = rng.standard_normal(n); u[F] = kappa * a0[F]
    offF = np.setdiff1d(np.arange(n), F)
    zero_off = rng.choice(offF, 15, replace=False); u[zero_off] = 0.0          # coordinates off supp u (allowed for masses/z-moves)
    nu0 = np.linalg.norm(mu * a0); e0 = mu * a0 / nu0
    val0 = u @ (z0 + mu * e0)
    # random admissible move: raise/lower/truncate on F (same sign), masses + z-moves off supp u
    a1 = a0.copy(); z1 = z0.copy()
    a1[F] *= rng.uniform(0, 3, 20)                                             # includes truncation-like small factors
    a1[F[rng.random(20) < 0.2]] = 0.0                                          # truncation to contacts of the same sign (z kept)
    if not np.any(a1[F]): a1[F[0]] = a0[F[0]]
    for s in rng.choice(zero_off, 5, replace=False):
        a1[s] = rng.uniform(-0.3, 0.3); z1[s] = np.sign(a1[s]) if a1[s] != 0 else z1[s]
    for s in rng.choice(zero_off, 5, replace=False):
        if a1[s] == 0: z1[s] = rng.uniform(-1, 1)
    nu1 = np.linalg.norm(mu * a1); e1 = mu * a1 / nu1
    val1 = u @ (z1 + mu * e1)
    pred = -(kappa * nu0 / 2) * np.linalg.norm(e1 - e0) ** 2
    worst = max(worst, abs((val1 - val0) - pred))
    if kappa > 0:
        maxgain = max(maxgain, val1 - val0)
print(f"max |identity error| over 400 random admissible moves: {worst:.2e};  max gain (kappa > 0): {maxgain:.2e} (<= 0 predicted)")
# necessity: mass on supp u \ F
s = [j for j in range(n) if j not in F and u[j] != 0][0]
for m in [1e-6, 1e-5, 1e-4]:
    a1 = a0.copy(); a1[s] = m * np.sign(u[s]); z1 = z0.copy(); z1[s] = np.sign(a1[s])
    e1 = mu * a1 / np.linalg.norm(mu * a1); dv = u @ (z1 + mu * e1) - val0
    print(f"mass {m:.0e} at s in supp u \\ F (z set to its sign): change = {dv:+.3e}; first-order Hilbert part = {m*mu[s]**2*u[s]*np.sign(u[s])/nu0:+.3e} (+ z-change {u[s]*(z1[s]-z0[s]):+.3e})")
