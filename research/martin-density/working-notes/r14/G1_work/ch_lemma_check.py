"""Sanity check of Lemma CH (cushioned face-wise Hoffman lemma), G1 part 1.

Random instances in R^4: strict rows a1, a2 (equalities), a3 (strict inequality); cushioned rows
c1 = 0.3 a1 - 0.4 a2 + sgn*mu*q (q unit, orthogonal to span(a1,a2): a TINY minor mu), a4 generic.
Data x = x0 + noise, x0 in the exact face (ker a1,a2, a3>0, a4>0).  We run the constructive proof of Lemma CH,
check (MD)/(SE) on the instance, verify (i)-(iii), and compare |x'-x| with the distance of x to the EXACT cone
(c1 x >= 0 strictly enforced) -- large when the defect is wrong-signed and mu |x| >> V.
"""
import itertools, warnings, numpy as np, cvxpy as cp
warnings.filterwarnings('ignore')
rng = np.random.default_rng(1)

def minors(A, rows):
    n = A.shape[1]
    for k in range(1, min(len(rows), n) + 1):
        for R in itertools.combinations(rows, k):
            for K in itertools.combinations(range(n), k):
                yield R, abs(np.linalg.det(A[list(R)][:, list(K)]))

def check_MD_SE(A, mu, u, strict):
    md = all(not (2 * mu < d < u) for R, d in minors(A, range(A.shape[0])))
    se = all(not (1e-12 < d < u) for R, d in minors(A, strict))
    return md, se

def robust(A, R, u):
    if not R:
        return True
    M = A[list(R)]
    return any(abs(np.linalg.det(M[:, list(K)])) >= u for K in itertools.combinations(range(M.shape[1]), len(R)))

def construct(A, E, Is, Ic, x, u):
    p, n = A.shape
    I = Is + Ic
    s = A @ x
    V = max([abs(s[i]) for i in E] + [max(-s[i], 0) for i in I])
    if V == 0:
        return x.copy(), 0.0
    Lam = p ** (p / 2) / u + 1
    rhos = [Lam ** k * V for k in range(p + 2)]
    k = next(k for k in range(p + 1) if not any(rhos[k] <= s[i] < rhos[k + 1] for i in I))
    Nk = list(E) + [i for i in I if s[i] < rhos[k]]
    S = set(E) | set(Is)
    B = []
    for i in [i for i in Nk if i in S] + [i for i in Nk if i not in S]:   # strict rows first, then extension
        if robust(A, B + [i], u):
            B.append(i)
    if not B:
        return x.copy(), V
    AB = A[B]
    return x - AB.T @ np.linalg.solve(AB @ AB.T, AB @ x), V

def dist_exact_cone(A, E, Iall, x):
    y = cp.Variable(A.shape[1])
    prob = cp.Problem(cp.Minimize(cp.sum_squares(y - x)), [A[E] @ y == 0, A[Iall] @ y >= 0])
    for solver in (cp.CLARABEL, cp.OSQP, cp.SCS):
        try:
            prob.solve(solver=solver)
            if prob.value is not None:
                return float(np.sqrt(max(prob.value, 0.0)))
        except Exception:
            pass
    return float('nan')

def unit(v):
    return v / np.linalg.norm(v)

def main():
    u = 1e-4
    rows = []
    tries = 0
    while len(rows) < 200 and tries < 20000:
        tries += 1
        mu = 10 ** rng.uniform(-13, -8) if tries % 2 else 10 ** rng.uniform(-10, -8); sgn = rng.choice([-1, 1])
        a1, a2, a3, a4 = (0.5 * unit(rng.normal(size=4)) for _ in range(4))
        Q, _ = np.linalg.qr(np.stack([a1, a2]).T)
        q = rng.normal(size=4); q = unit(q - Q @ (Q.T @ q))
        c1 = 0.3 * a1 - 0.4 * a2 + sgn * mu * q
        A = np.stack([a1, a2, a3, c1, a4]); E, Is, Ic = [0, 1], [2], [3, 4]
        md, se = check_MD_SE(A, mu, u, E + Is)
        if not (md and se):
            continue
        K = np.linalg.svd(A[E])[2][2:].T
        y = K @ rng.normal(size=2)
        if not (a3 @ y > 0.05 * np.linalg.norm(y) and a4 @ y > 0.05 * np.linalg.norm(y)):
            continue
        x0 = unit(y); V0 = 10 ** rng.uniform(-8, -3) if tries % 2 else 10 ** rng.uniform(-15, -13)
        x = x0 + V0 * unit(rng.normal(size=4))
        xp, V = construct(A, E, Is, Ic, x, u)
        eta = 2 ** 2 * mu / u
        okS = max(abs(A[E] @ xp)) <= 1e-10 and A[2] @ xp >= -1e-10
        okC = min(A[Ic] @ xp + eta * np.linalg.norm(xp)) >= -1e-10
        dC = dist_exact_cone(A, E, Is + Ic, x)
        wrong = sgn * (q @ x0) < 0
        rows.append((okS, okC, np.linalg.norm(xp - x) / max(V, 1e-300), dC, wrong, mu, V))
    r = np.array(rows, dtype=float)
    print("instances satisfying (MD),(SE):", len(r))
    print("strict rows exact at x':", int(r[:, 0].sum()), "   cushioned rows >= -eta|x'|:", int(r[:, 1].sum()))
    print("max |x'-x|/V = %.3g   median = %.3g" % (r[:, 2].max(), np.median(r[:, 2])))
    w = r[:, 4] > 0; big = r[:, 5] > 100 * r[:, 6]
    print("right-signed defect: %d, max dist(x, EXACT cone)/V = %.3g" % ((~w).sum(), (r[~w, 3] / r[~w, 6]).max()))
    sel = w & big
    if sel.sum():
        print("wrong-signed defect with mu >= 100 V: %d, min dist(x, EXACT cone) = %.3g, max |x'-x| = %.3g"
              % (sel.sum(), r[sel, 3].min(), (r[sel, 2] * r[sel, 6]).max()))
    sel2 = (~w) & big
    if sel2.sum():
        print("right-signed defect with mu >= 100 V: %d, max dist(x, EXACT cone) = %.3g" % (sel2.sum(), r[sel2, 3].max()))

if __name__ == "__main__":
    main()
