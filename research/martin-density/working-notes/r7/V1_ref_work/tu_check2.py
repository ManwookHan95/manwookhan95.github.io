"""Independent check of V1 Lemma TU (pulls + banks, explicit scalar fixed point), diagonal base.
Model: coordinates 0..n-1, s_j = 2^{-alpha j}; base support F = {0,1,2}; carriers in L0 have private signature
sets S_l (bounded gaps) with v_l(s) = d_l 2^{-alpha s}, exactly swallowed (z = eps_l) beyond a cutoff;
'other' carriers have random supports on F and on coordinates below the cutoff.  val_l = eps_l u_l(zhat),
zhat_j = z_j + s_j^2 A_j/||U^*A||.  Checks: exactness of val^# - val^(2) = x on L0, second-order change of others,
positivity of bank masses, contraction of the scalar map, increments Delta in [eta/2, 4 2^G eta]."""
import numpy as np
rng = np.random.default_rng(7)

def zhat(A, z, s):
    nu = np.linalg.norm(s * A)
    return z + s**2 * A / nu

worst_exact = 0.0; worst_other = 0.0; minmass = np.inf; maxlip = 0.0; fails = 0; tests = 0
for trial in range(400):
    alpha = rng.uniform(0.05, 0.15)
    nL = int(rng.integers(1, 5)); G = 2
    cutoff = 12
    n = cutoff + nL * 40 + 5
    s = 2.0 ** (-alpha * np.arange(1, n + 1))
    A2 = np.zeros(n); F = [0, 1, 2]
    A2[F] = rng.normal(size=3)
    z2 = rng.uniform(-1, 1, n); z2[F] = np.sign(A2[F])
    # signature sets: S_l = cutoff + l + nL*G*i  (bounded gap nL*G), beyond cutoff
    S = [cutoff + l + nL * G * np.arange(0, 40 // G) for l in range(nL)]
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
    for eta in [1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 3e-6, 1e-6]:
        jb0 = [S[l][0] for l in range(nL)]
        reg = 0.02 * np.min(s[jb0]**2 * np.array([U[l][jb0[l]] for l in range(nL)])**2) * np.linalg.norm(s*A2) / nL / 2**(alpha*nL*G)
        if eta > reg:
            continue
        x = rng.uniform(-1, 1, size=nL) * eta
        eta_ = np.max(np.abs(x))
        Ap = A2.copy(); zp = z2.copy(); jb = []
        for l in range(nL):
            jprime = S[l][0]; jb.append(jprime)
            vS = U[l][S[l]]
            cand = [j for j, v in zip(S[l][1:], vS[1:]) if eta_ <= v <= 2 ** (alpha * nL * G) * eta_ * 1.0000001]
            if not cand:
                cand = [S[l][-1]]
            j = cand[0]
            mu = 24 * lam[l] * U[l][j]
            Ap[j] += -eps[l] * mu; zp[j] = -eps[l]
        nup = np.linalg.norm(s * Ap)
        zhp = zhat(Ap, zp, s)
        valp = np.array([eps[l] * U[l] @ zhp for l in range(nL)])
        ep = s * Ap / nup
        beta = np.array([eps[l] * np.dot(s * U[l], ep) for l in range(nL)])
        Delta = x + val2 - valp
        sp = s[jb]; vp = np.array([U[l][jb[l]] for l in range(nL)])
        def mfun(y):
            return (Delta * y + beta * (y - nup)) / (sp**2 * vp)
        def Phi(y):
            return np.sqrt(nup**2 + np.sum(sp**2 * mfun(y) ** 2))
        y = nup
        for it in range(200):
            y = Phi(y)
        # numerical Lipschitz constant of Phi near the fixed point
        h = 1e-9 * nup
        lip = abs(Phi(y + h) - Phi(y)) / h
        maxlip = max(maxlip, lip)
        m = mfun(y)
        A = Ap.copy()
        for l in range(nL):
            A[jb[l]] += m[l] * eps[l]
        zh = zhat(A, zp, s)
        valh = np.array([eps[l] * U[l] @ zh for l in range(nL)])
        othh = np.array([u @ zh for u in others])
        tests += 1
        worst_exact = max(worst_exact, np.max(np.abs(valh - val2 - x)))
        worst_other = max(worst_other, np.max(np.abs(othh - oth2)) / eta_**2)
        minmass = min(minmass, np.min(m))
        if np.min(m) <= 0 or np.min(Delta) < eta_ / 2:
            fails += 1
print("tests", tests, "failures(mass<=0 or Delta<eta/2)", fails)
print("max |val^# - val^(2) - x| =", worst_exact, " max other change/eta^2 =", worst_other)
print("min bank mass =", minmass, " max |Phi'| at fixed point =", maxlip)
