"""Referee (a) independent check of Q2 Lemma LT (full and partial lowering), adversarial directions.

Model: base coordinates 0..n-1, diagonal base mu_j, blocks with K carriers (random q*-normalized vectors), Phi_m(k) = 2^{-m-k} * rand.
p*(h) = min max(q*(A), max_m N_m(W_m)), h = A + sum_m R_m* W_m, R_m* W = sum_k m Phi_m(k) W(k) u_{k,m}.
First rows from forced data (a, z).  Directions h chosen ADVERSARIALLY: anti-sign on the truncated support (so that the optimal
decomposition at f + r h uses the far cushions), plus random parts.  Checks:
  (LT)        p*(f^M + r h) <= pi + 2 Lambda_M + 2||U* a_{>M}|| + p*(L*(w^M - w))
  (LT-part)   p*(f^low + r h) <= pi + 2 sum min(|Da|, (y - alpha')_+) + 2||U* Da|| + p*(L*(w^low - w))
  base-level sharpness of the factor 2 (q* only).
"""
import numpy as np, cvxpy as cp

rng = np.random.default_rng(2026)
n, Mb, K = 14, 2, 5

def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)

def make_model():
    mu = 0.3 * 0.45 ** (np.arange(n) ** 1.2)
    Phi = {m: np.array([2.0 ** (-m - k) * (0.5 + 0.5 * rng.random()) for k in range(K)]) for m in range(1, Mb + 1)}
    U = {}
    for m in range(1, Mb + 1):
        for k in range(K):
            u = rng.standard_normal(n)
            U[(k, m)] = u / qstar(u, mu)
    return mu, Phi, U

def Rstar(m, W, Phi, U):
    return sum(m * Phi[m][k] * W[k] * U[(k, m)] for k in range(K))

def block_norm(x, Phi_m):
    al, be = cp.Variable(K), cp.Variable(K)
    pr = cp.Problem(cp.Minimize(cp.norm1(al) + cp.norm2(be)), [al + cp.multiply(Phi_m, be) == x])
    pr.solve(solver="CLARABEL")
    return pr.value

def norming(x, Phi_m):
    w = cp.Variable(K)
    pr = cp.Problem(cp.Maximize(x @ w), [cp.norm_inf(w) + cp.norm2(cp.multiply(Phi_m, w)) <= 1])
    pr.solve(solver="CLARABEL")
    return w.value

def first_row(a, z, mu, Phi, U):
    nu = np.linalg.norm(mu * a)
    zhat = z + mu * (mu * a) / nu
    zeta = {m: np.array([m * Phi[m][k] * U[(k, m)] @ zhat for k in range(K)]) for m in range(1, Mb + 1)}
    w = {m: norming(zeta[m], Phi[m]) for m in zeta}
    f = a + sum(Rstar(m, w[m], Phi, U) for m in w)
    return f, w

def pstar_dec(h, mu, Phi, U):
    A = cp.Variable(n); W = {m: cp.Variable(K) for m in range(1, Mb + 1)}; tau = cp.Variable()
    cons = [cp.norm1(A) + cp.norm2(cp.multiply(mu, A)) <= tau]
    expr = A
    for m in W:
        cons.append(cp.norm_inf(W[m]) + cp.norm2(cp.multiply(Phi[m], W[m])) <= tau)
        expr = expr + sum(m * Phi[m][k] * W[m][k] * U[(k, m)] for k in range(K))
    cons.append(expr == h)
    pr = cp.Problem(cp.Minimize(tau), cons)
    pr.solve(solver="CLARABEL")
    return pr.value, A.value

worst_full, worst_part, n_tests = -1e9, -1e9, 0
for trial in range(5):
    mu, Phi, U = make_model()
    F = np.arange(11)
    a = np.zeros(n); a[F] = rng.choice([-1, 1], len(F)) * (0.7 ** F) * (0.3 + rng.random(len(F)))
    a /= qstar(a, mu)
    s = np.sign(a)
    z = np.zeros(n); z[F] = s[F]; z[11:] = rng.uniform(-0.9, 0.9, n - 11)
    f, w = first_row(a, z, mu, Phi, U)
    for Mt in [5, 8]:
        aM = a.copy(); aM[Mt:] = 0.0; aM /= qstar(aM, mu)
        fM, wM = first_row(aM, z, mu, Phi, U)
        UaM = np.linalg.norm(mu[Mt:] * a[Mt:])
        pLW, _ = pstar_dec(sum(Rstar(m, wM[m] - w[m], Phi, U) for m in w), mu, Phi, U)
        # partial lowering: halve the moduli on F cap [3, Mt) and zero beyond Mt-? (mixed)
        Da = np.zeros(n); Da[3:Mt] = -0.5 * a[3:Mt]; Da[Mt:11] = -a[Mt:11]
        al = (a + Da); al /= qstar(al, mu)
        flow, wlow = first_row(al, z, mu, Phi, U)
        pLWl, _ = pstar_dec(sum(Rstar(m, wlow[m] - w[m], Phi, U) for m in w), mu, Phi, U)
        for r in [0.2, 0.05, 0.01, 0.002, -0.01]:
            for kind in range(3):
                h = rng.standard_normal(n) * 0.2
                if kind >= 1:   # anti-sign usage of far support
                    h[Mt:11] -= s[Mt:11] * np.abs(a[Mt:11]) / max(abs(r), 1e-9) * (0.5 + rng.random(11 - Mt)) * (1 if kind == 1 else 3)
                if kind == 2:   # also anti-sign on lowered-but-kept coordinates
                    h[3:Mt] -= s[3:Mt] * np.abs(a[3:Mt]) / max(abs(r), 1e-9) * rng.random(Mt - 3)
                pi, A = pstar_dec(f + r * h, mu, Phi, U)
                B = (A - a) / r
                Lam = sum(min(abs(a[j]), max(-s[j] * r * B[j], 0.0)) for j in F if j >= Mt)
                lhs, _ = pstar_dec(fM + r * h, mu, Phi, U)
                rhs = pi + 2 * Lam + 2 * UaM + pLW
                worst_full = max(worst_full, lhs - rhs)
                y = np.maximum(-s * r * B, 0.0)
                alp = np.abs(a + Da)
                Lp = sum(min(abs(Da[j]), max(y[j] - alp[j], 0.0)) for j in F)
                lhs2, _ = pstar_dec(flow + r * h, mu, Phi, U)
                rhs2 = pi + 2 * Lp + 2 * np.linalg.norm(mu * Da) + pLWl
                worst_part = max(worst_part, lhs2 - rhs2)
                n_tests += 1
print("tests:", n_tests)
print("max (LHS - RHS) full LT   :", worst_full)
print("max (LHS - RHS) partial LT:", worst_part)
# base-level sharpness (q* only): h = -s_j e_j, j > M
mu, Phi, U = make_model()
a = np.zeros(n); a[:11] = (0.7 ** np.arange(11)); a /= qstar(a, mu); Mt = 6; j = 7
aM = a.copy(); aM[Mt:] = 0; aM /= qstar(aM, mu)
for r in [a[j] * 0.9, a[j] * 0.5, a[j] * 0.1]:
    h = np.zeros(n); h[j] = -1.0
    A = a + r * h; Ap = aM + r * h
    lam = min(a[j], r)
    print(f"r={r:.3e}: q*(A')-q*(A) = {qstar(Ap, mu) - qstar(A, mu):.6e}, 2 Lambda = {2*lam:.6e}, 2||U*a_>M|| = {2*np.linalg.norm(mu[Mt:]*a[Mt:]):.2e}")
