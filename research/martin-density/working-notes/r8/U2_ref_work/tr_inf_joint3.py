# Independent check of Lemma TR-inf (cases (c) and (c')) and of the Sherman-Morrison residual (U2 3.2-3.3).
# Model: diagonal base mu_s (fast decay), every coordinate in the support F (infinite-F model, truncated),
# value map val_k = u_k(zhat), zhat_s = z_s + mu_s^2 a_s / nu, nu = ||(mu_s a_s)||, z = sgn a (moves keep signs).
# Carriers: coarse carriers k = 0..K-1 with targets on [0, smax) and private signature sets S_k beyond smax.
# (c): each tuned carrier uses a pair s < s' in S_k with Delta_s = -(alpha_{s'}/alpha_s) Delta_{s'} (ratio frozen at the base point).
# (c'): each tuned carrier uses one coordinate s' in S_k; a global anchor s0 <= smax (no tuned vector meets s0) cancels the common term.
# Exact tuning to prescribed increments x by Newton on the reduced unknowns; we report residuals, motion of untuned carriers.
import mpmath as mp
import random
mp.mp.dps = 600
random.seed(7)

def setup(n=40, K=6, smax=8, decay=1.6):
    mu = [mp.mpf(2) ** (-(s + 2) ** decay) for s in range(n)]
    S = {k: [s for s in range(smax, n) if (s - smax) % K == k] for k in range(K)}
    u = []
    for k in range(K):
        vec = [mp.mpf(0)] * n
        for s in random.sample(range(smax), 3):           # target part on [0, smax)
            vec[s] = mp.mpf(random.uniform(-1, 1)) / 3
        for s in S[k]:
            vec[s] = mp.mpf(2) ** (-s) * mp.mpf('0.7')     # signature v_k(s) = delta 2^{-s}/n
        u.append(vec)
    a = [mp.mpf(random.uniform(0.3, 1.0)) * (1 if random.random() < 0.6 else -1) for s in range(n)]
    return n, K, smax, mu, S, u, a

def vals(a, mu, u, z):
    nu = mp.sqrt(sum((m * x) ** 2 for m, x in zip(mu, a)))
    zh = [m * m * x / nu for m, x in zip(mu, a)]
    return nu, [sum(uk[s] * zh[s] for s in range(len(a))) for uk in u]

def run(case, eta):
    n, K, smax, mu, S, u, a = setup()
    z = [mp.sign(x) for x in a]
    nu, v0 = vals(a, mu, u, z)
    tuned = [0, 1, 2]                                    # L_0
    alpha = lambda s: mu[s] ** 2 * a[s] / nu ** 2
    plan = {}
    anchor = None
    if case == 'c':
        for k in tuned:
            s, sp = S[k][0], S[k][1]
            plan[k] = [(sp, mp.mpf(1)), (s, -alpha(sp) / alpha(s))]   # Delta at s = ratio * Delta'
    else:
        # anchor: a target-range coordinate not met by any tuned vector
        cand = [s for s in range(smax) if all(u[k][s] == 0 for k in tuned)]
        if not cand:
            for k in tuned:
                for s in range(smax):
                    u[k][s] = u[k][s] if s != 0 else mp.mpf(0)
            nu, v0 = vals(a, mu, u, z); cand = [0]
        anchor = cand[0]
        for k in tuned:
            plan[k] = [(S[k][1], mp.mpf(1))]
    scale = []
    for k in tuned:
        sp = plan[k][0][0]
        sc = mu[sp]**2 * u[k][sp] / nu
        if case == 'c':
            s = plan[k][1][0]
            sc = sc * (1 - (a[sp]/u[k][sp])/(a[s]/u[k][s]))
        scale.append(sc)
    effmin = min(abs(sc) for sc in scale)
    eta = eta * effmin
    x = [mp.mpf(random.uniform(-1, 1)) * eta for _ in tuned]
    def apply(dpn):
        dp = [dpn[i]/scale[i] for i in range(len(dpn))]
        b = list(a)
        tot0 = mp.mpf(0)
        for i, k in enumerate(tuned):
            for (s, r) in plan[k]:
                b[s] += r * dp[i]
                if case == "c'":
                    tot0 += alpha(s) * r * dp[i]
        if case == "c'":
            b[anchor] += -tot0 / alpha(anchor)
        return vals(b, mu, u, z)[1]
    # Newton on dp (finite-difference Jacobian, high precision)
    dp = [mp.mpf(0)] * len(tuned)
    for it in range(8):
        cur = apply(dp)
        F = [cur[k] - v0[k] - x[i] for i, k in enumerate(tuned)]
        h = eta * mp.mpf(10) ** (-30)
        J = mp.matrix(len(tuned), len(tuned))
        for j in range(len(tuned)):
            dq = list(dp); dq[j] += h
            cj = apply(dq)
            for i, k in enumerate(tuned):
                J[i, j] = (cj[k] - cur[k]) / h
        step = mp.lu_solve(J, mp.matrix(F))
        dp = [dp[i] - step[i] for i in range(len(tuned))]
    fin = apply(dp)
    res = max(abs(fin[k] - v0[k] - x[i]) for i, k in enumerate(tuned))
    others = [k for k in range(K) if k not in tuned]
    meets_anchor = [k for k in others if anchor is not None and u[k][anchor] != 0]
    clean = [k for k in others if k not in meets_anchor]
    mo_clean = max([abs(fin[k] - v0[k]) for k in clean] + [mp.mpf(0)])
    mo_anchor = max([abs(fin[k] - v0[k]) for k in meets_anchor] + [mp.mpf(0)])
    offdiag = max(abs(J[i, j]) for i in range(len(tuned)) for j in range(len(tuned)) if i != j)
    diag = min(abs(J[i, i]) for i in range(len(tuned)))
    return res/eta, mo_clean/eta**2, mo_anchor/eta, offdiag / diag, max(abs(dp[i]/scale[i]) for i in range(len(dp))), effmin

for case in ['c', "c'"]:
    for eta in [mp.mpf('1e-4'), mp.mpf('1e-8'), mp.mpf('1e-12')]:
        res, moc, moa, od, dmax, eff = run(case, eta)
        print(f"case {case:3s} eta/eff={mp.nstr(eta,2):6s} eff={mp.nstr(eff,3):9s} residual/eta={mp.nstr(res,3):10s} untuned move/eta^2={mp.nstr(moc,3):10s} "
              f"anchor-met move/eta={mp.nstr(moa,3):10s} offdiag/diag Jac={mp.nstr(od,3):9s} max|Delta'|={mp.nstr(dmax,3)}")
