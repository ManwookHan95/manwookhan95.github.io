"""U4 audit, conflict C1: V1 Lemma TU (pulls + private banks, explicit scalar fixed point) with a SUPER-EXPONENTIALLY
decaying diagonal base s_j = 2^{-beta j^2} (finite-model analogue of mu_s = 2^{-s^2-1}) instead of 2^{-alpha j}.
Checks: exactness val^# - val^(2) = x on L0, second-order change of other carriers, positivity of bank masses, contraction,
and that the admissible tuning size scales with min_l s_{j'_l}^2 v_l(j'_l) (the quantity that B_mu(l) controls in Design(l)).
Model as in V1-ref tu_check4.py: base support F = {0,1,2}; carriers in L0 have private signature sets with bounded gaps,
v_l(s) = d_l 2^{-alpha s}, exactly swallowed beyond a cutoff; 'other' carriers live on F and on coarse coordinates."""
import numpy as np, collections
rng = np.random.default_rng(11)

def zhat(A, z, s):
    nu = np.linalg.norm(s * A)
    return z + s**2 * A / nu

per = collections.defaultdict(float); worst_exact = 0.0; worst_other = 0.0; minmass = np.inf; maxlip = 0.0
fails = 0; tests = 0; skipped = 0; regime_ratio = []
for trial in range(300):
    beta = rng.uniform(0.002, 0.006)          # s_j = 2^{-beta j^2}: super-exponential decay
    alpha = rng.uniform(0.05, 0.12)           # signature weights v_l(s) ~ 2^{-alpha s}
    nL = int(rng.integers(1, 4)); G = 2
    cutoff = 10
    n = cutoff + nL * 120 + 5
    jj = np.arange(1, n + 1)
    s = 2.0 ** (-beta * jj**2)
    A2 = np.zeros(n); F = [0, 1, 2]
    A2[F] = rng.normal(size=3)
    z2 = rng.uniform(-1, 1, n); z2[F] = np.sign(A2[F])
    S = [cutoff + l + nL * G * np.arange(0, 120 // G) for l in range(nL)]
    eps = rng.choice([-1, 1], size=nL)
    U = []
    for l in range(nL):
        u = np.zeros(n)
        u[F] = rng.normal(size=3) * 0.2
        tg = rng.choice(np.arange(3, cutoff), size=3, replace=False); u[tg] = rng.normal(size=3) * 0.2
        dl = rng.uniform(0.2, 0.6)
        u[S[l]] = dl * 2.0 ** (-alpha * S[l])
        z2[S[l]] = eps[l]
        U.append(u)
    others = []
    for k in range(4):
        u = np.zeros(n); u[F] = rng.normal(size=3) * 0.2
        tg = rng.choice(np.arange(3, cutoff), size=4, replace=False); u[tg] = rng.normal(size=4) * 0.2
        others.append(u)
    lam = rng.uniform(0.05, 0.25, size=nL)
    zh2 = zhat(A2, z2, s)
    val2 = np.array([eps[l] * U[l] @ zh2 for l in range(nL)])
    oth2 = np.array([u @ zh2 for u in others])
    jb0 = [S[l][0] for l in range(nL)]
    key = np.min(s[jb0]**2 * np.array([U[l][jb0[l]] for l in range(nL)]))   # min s'^2 v' (B_mu-type quantity)
    nu2 = np.linalg.norm(s * A2)
    reg = 0.02 * key * np.min(np.array([U[l][jb0[l]] for l in range(nL)])) * nu2 / nL / 2**(alpha*nL*G)
    for fac in [1e-1, 1e-2, 1e-3, 1e-4]:
        eta = fac * reg
        x = rng.uniform(-1, 1, size=nL) * eta
        eta_ = np.max(np.abs(x))
        Ap = A2.copy(); zp = z2.copy(); jb = []
        ok = True
        for l in range(nL):
            jprime = S[l][0]; jb.append(jprime)
            vS = U[l][S[l]]
            cand = [j for j, v in zip(S[l][1:], vS[1:]) if eta_ <= v <= 2 ** (alpha * nL * G) * eta_ * 1.0000001]
            if not cand:
                ok = False; break
            j = cand[0]
            mu = 24 * lam[l] * U[l][j]
            Ap[j] += -eps[l] * mu; zp[j] = -eps[l]
        if not ok:
            skipped += 1; continue
        nup = np.linalg.norm(s * Ap)
        zhp = zhat(Ap, zp, s)
        valp = np.array([eps[l] * U[l] @ zhp for l in range(nL)])
        ep = s * Ap / nup
        bet = np.array([eps[l] * np.dot(s * U[l], ep) for l in range(nL)])
        Delta = x + val2 - valp
        sp = s[jb]; vp = np.array([U[l][jb[l]] for l in range(nL)])
        mfun = lambda y: (Delta * y + bet * (y - nup)) / (sp**2 * vp)
        Phi = lambda y: np.sqrt(nup**2 + np.sum(sp**2 * mfun(y) ** 2))
        y = nup
        for it in range(300):
            y = Phi(y)
        h = 1e-9 * nup
        lip = abs(Phi(y + h) - Phi(y)) / h
        if not (lip < 0.9):
            fails += 1; continue
        maxlip = max(maxlip, lip)
        m = mfun(y)
        A = Ap.copy()
        for l in range(nL):
            A[jb[l]] += m[l] * eps[l]
        zh = zhat(A, zp, s)
        valh = np.array([eps[l] * U[l] @ zh for l in range(nL)])
        othh = np.array([u @ zh for u in others])
        tests += 1
        worst_exact = max(worst_exact, np.max(np.abs(valh - val2 - x)) / eta_); worst_abs = max(globals().get("worst_abs", 0.0), np.max(np.abs(valh - val2 - x)))
        worst_other = max(worst_other, np.max(np.abs(othh - oth2)) / eta_**2)
        per[fac] = max(per[fac], np.max(np.abs(othh - oth2)) / eta_**2)
        minmass = min(minmass, np.min(m))
        regime_ratio.append(np.max(m) * key / eta_)
        if np.min(m) <= 0 or np.min(Delta) < eta_ / 2:
            fails += 1
print("tests", tests, "skipped(no pull coord in range)", skipped, "failures(diverge or mass<=0 or Delta<eta/2)", fails)
print("max |val^# - val^(2) - x|/eta =", worst_exact, " absolute:", worst_abs)
print("max other change/eta^2 overall =", worst_other, "  per factor:", {k: float('%.3g' % v) for k, v in per.items()})
print("min bank mass =", minmass, "  max |Phi'| at fixed point =", maxlip)
print("bank mass x min(s'^2 v')/eta: median %.3g, max %.3g (O(1): masses scale like eta/(s'^2 v'), i.e. like B_mu)" %
      (np.median(regime_ratio), np.max(regime_ratio)))
