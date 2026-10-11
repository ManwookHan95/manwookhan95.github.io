"""Independent adversarial check of Lemma CH (G1 part 1).
Random instances, n in {3,4,5}, p up to 7 rows; strict rows (equalities E, strict inequalities Is) with exact
dependencies (all strict minors 0 or robust), cushioned rows Ic built as combinations of strict rows plus a tiny
defect of random sign (tiny minors mu) or generic.  Data x near the cone with violation V.  We implement the
constructive proof (slack pigeonhole, strict basis, robust maximal extension, projection) and check:
 (i) |x'-x| <= H V  (H = p^{p/2} Lam^p/u)  and also the sharper |x'-x| <= k^{k/2} rho/u with k = |B| <= n,
 (ii) strict rows exact, (iii) cushioned rows >= -eta|x'|, eta = 2^{n/2} mu/u, rows outside N_k strictly positive.
Also records |B| <= n and the ratio |x'-x|/V.
"""
import itertools, numpy as np
rng = np.random.default_rng(7)

def all_minors(A, rows):
    n = A.shape[1]
    out = []
    for k in range(1, min(len(rows), n) + 1):
        for R in itertools.combinations(rows, k):
            for K in itertools.combinations(range(n), k):
                out.append(abs(np.linalg.det(A[np.ix_(R, K)])))
    return out

def robust(A, R, u):
    if not R: return True
    M = A[list(R)]
    if len(R) > M.shape[1]: return False
    return any(abs(np.linalg.det(M[:, list(K)])) >= u for K in itertools.combinations(range(M.shape[1]), len(R)))

def construct(A, E, Is, Ic, x, u):
    p, n = A.shape
    I = Is + Ic
    s = A @ x
    V = max([abs(s[i]) for i in E] + [max(-s[i], 0) for i in I] + [0.0])
    if V == 0: return x.copy(), 0.0, None, None, 0
    Lam = p ** (p / 2) / u + 1
    rhos = [Lam ** k * V for k in range(p + 2)]
    k = next(k for k in range(p + 1) if not any(rhos[k] <= s[i] < rhos[k + 1] for i in I))
    rho = rhos[k]
    Nk = list(E) + [i for i in I if s[i] < rho]
    S = set(E) | set(Is)
    # strict basis: greedy independent strict rows of Nk
    Bs = []
    for i in [i for i in Nk if i in S]:
        if np.linalg.matrix_rank(A[Bs + [i]], tol=1e-12) > len(Bs): Bs.append(i)
    assert robust(A, Bs, u), "strict basis not robust: (SE) violated?"
    # maximal robust extension (exhaustive over subsets to get MAXIMAL CARDINALITY)
    rest = [i for i in Nk if i not in Bs]
    best = Bs
    for r in range(len(rest), 0, -1):
        found = False
        for add in itertools.combinations(rest, r):
            if len(Bs) + r <= n and robust(A, Bs + list(add), u):
                best = Bs + list(add); found = True; break
        if found: break
    B = best
    AB = A[B]
    xp = x - AB.T @ np.linalg.solve(AB @ AB.T, AB @ x) if B else x.copy()
    return xp, V, rho, Nk, len(B)

def unit(v): return v / np.linalg.norm(v)

def instance(n, u):
    nE = rng.integers(1, n); nIs = rng.integers(0, 2)
    base = [0.6 * unit(rng.normal(size=n)) for _ in range(nE + nIs)]
    strict = list(base)
    # an exactly dependent extra strict inequality row (combination with simple coefficients)
    if nE >= 2 and rng.random() < 0.5:
        strict.append(0.5 * (base[0] + base[1]) / 1.0)
    Ac = []
    mus = []
    for _ in range(rng.integers(1, 3)):
        if rng.random() < 0.7 and len(base) >= 1:
            k = rng.integers(1, len(base) + 1)
            coef = rng.normal(size=k) * 0.4
            c = sum(coef[i] * base[i] for i in range(k))
            Q, _ = np.linalg.qr(np.stack(base).T)
            q = rng.normal(size=n); q = unit(q - Q @ (Q.T @ q))
            mu = 10 ** rng.uniform(-11, -8); mus.append(mu)
            c = c + rng.choice([-1, 1]) * mu * q
            if np.linalg.norm(c) > 1: c = c / np.linalg.norm(c)
        else:
            c = 0.6 * unit(rng.normal(size=n))
        Ac.append(c)
    A = np.stack(strict + Ac)
    E = list(range(nE)); Is = list(range(nE, len(strict))); Ic = list(range(len(strict), len(strict) + len(Ac)))
    return A, E, Is, Ic

def main():
    u = 1e-3
    stats = dict(n=0, okS=0, okC=0, okH=0, okH2=0, Bn=0, ratio=[])
    tries = 0
    while stats['n'] < 600 and tries < 200000:
        tries += 1
        n = int(rng.integers(3, 6))
        A, E, Is, Ic = instance(n, u)
        p = A.shape[0]
        if p > 7 or np.isnan(A).any(): continue
        mins_all = all_minors(A, list(range(p)))
        tiny = [d for d in mins_all if d < u]
        mu = max(tiny) if tiny else 0.0
        if mu > 1e-6: continue                       # (MD) with a gap
        strictm = all_minors(A, E + Is)
        if any(1e-12 < d < u for d in strictm): continue   # (SE)
        mu = max(mu, 1e-300)
        # data: point of the exact face plus noise of size V0
        K = np.linalg.svd(A[E])[2][len(E):].T
        y = K @ rng.normal(size=K.shape[1])
        x = unit(y) + 10 ** rng.uniform(-9, -3) * unit(rng.normal(size=n))
        xp, V, rho, Nk, kB = construct(A, E, Is, Ic, x, u)
        if V == 0: continue
        stats['n'] += 1
        eta = 2 ** (n / 2) * mu / u
        okS = (np.max(np.abs(A[E] @ xp)) <= 1e-9) and (len(Is) == 0 or np.min(A[Is] @ xp) >= -1e-9)
        okC = np.min(A[Ic] @ xp + eta * np.linalg.norm(xp)) >= -1e-9
        Lam = p ** (p / 2) / u + 1
        H = p ** (p / 2) * Lam ** p / u
        okH = np.linalg.norm(xp - x) <= H * V * (1 + 1e-9)
        okH2 = np.linalg.norm(xp - x) <= (max(kB, 1) ** (max(kB, 1) / 2)) * rho / u * (1 + 1e-9)
        stats['okS'] += okS; stats['okC'] += okC; stats['okH'] += okH; stats['okH2'] += okH2; stats['Bn'] += (kB <= n)
        stats['ratio'].append(np.linalg.norm(xp - x) / V)
    r = np.array(stats['ratio'])
    print("instances:", stats['n'], " tries:", tries)
    print("strict exact:", stats['okS'], " cushioned >= -eta|x'|:", stats['okC'], " |x'-x|<=HV:", stats['okH'],
          " sharper k^{k/2} rho/u bound:", stats['okH2'], " |B|<=n:", stats['Bn'])
    print("|x'-x|/V: median %.3g  max %.3g" % (np.median(r), r.max()))

if __name__ == '__main__':
    main()
