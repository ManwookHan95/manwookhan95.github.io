"""Finite-model sanity check of Lemma LT (lowering transfer) of Q2 part 1.

Model as in r7/V3_work/rt_check.py: base coordinates j < n, diagonal base U (entries mu_j), blocks m = 1..M with K coordinates,
carriers u_{k,m} with q*(u) = 1, Phi_m(k) <= 2^{-m-k}, lambda = m Phi.
q*(A) = ||A||_1 + ||mu*A||_2 ; N_m(W) = ||W||_inf + ||Phi_m*W||_2 ; p*(h) = min max(q*(A), max_m N_m(W_m)), A + sum_m R_m* W_m = h.
First rows from forced data (a, z) (Remark rem:lemmaZ(c)).  Truncation at M: a^M = a 1_{[0,M)}/q*(a 1_{[0,M)}), same z
(support beyond M becomes contacts of sign s_j).
Check:  p*(f^M + r h) <= pi + 2 Lambda_M(r,B) + 2||U* a_{>M}|| + p*(L*(w^M - w)),  B := (A - a)/r from the optimal decomposition
f + r h = A + L* W (pi = p*(f + r h)),  Lambda_M = sum_{j in F, j >= M} min(|a_j|, (-s_j r B_j)_+).
Also reports the naive bound p*(f + r h) + p*(f^M - f) for comparison.
"""
import numpy as np, cvxpy as cp

rng = np.random.default_rng(7)
n, Mb, K = 16, 2, 6

def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)

def make_model():
    mu = 0.25 * 0.5 ** (np.arange(n) ** 1.3)
    Phi = {m: np.array([2.0 ** (-m - k) * (0.5 + 0.5 * rng.random()) for k in range(K)]) for m in range(1, Mb + 1)}
    U = {}
    for m in range(1, Mb + 1):
        for k in range(K):
            u = rng.standard_normal(n)
            U[(k, m)] = u / qstar(u, mu)
    return mu, Phi, U

def Rstar(m, W, Phi, U):
    out = np.zeros(n)
    for k in range(K):
        out += m * Phi[m][k] * W[k] * U[(k, m)]
    return out

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
    q0 = 1.0 / (1.0 + sum(block_norm(zeta[m], Phi[m]) for m in zeta))
    w = {m: norming(zeta[m], Phi[m]) for m in zeta}
    f = a + sum(Rstar(m, w[m], Phi, U) for m in w)
    return f, w, q0, zhat

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
    return pr.value, A.value, {m: W[m].value for m in W}

worst = -1e9
for trial in range(6):
    mu, Phi, U = make_model()
    F = np.arange(12)                                  # support 0..11; 12..15 off F
    a = np.zeros(n); a[F] = rng.choice([-1, 1], len(F)) * (0.6 ** F) * (0.3 + rng.random(len(F)))
    a /= qstar(a, mu)
    s = np.sign(a)
    z = np.zeros(n); z[F] = s[F]; z[12:] = rng.uniform(-0.9, 0.9, n - 12); z[12] = 1.0
    f, w, q0, zhat = first_row(a, z, mu, Phi, U)
    pf, _, _ = pstar_dec(f, mu, Phi, U)
    for Mt in [7, 9]:                                  # truncation point: keep 0..Mt-1
        aM = a.copy(); aM[Mt:] = 0.0; aM /= qstar(aM, mu)
        fM, wM, q0M, zhatM = first_row(aM, z, mu, Phi, U)
        UaM = np.linalg.norm(mu[Mt:] * a[Mt:])
        LW = sum(Rstar(m, wM[m] - w[m], Phi, U) for m in w)
        pLW, _, _ = pstar_dec(LW, mu, Phi, U)
        pdiff, _, _ = pstar_dec(fM - f, mu, Phi, U)
        print(f"trial {trial} M={Mt}: p*(f)={pf:.6f} alpha(M)={np.abs(a[Mt:]).sum():.2e} ||U*a_>M||={UaM:.2e} "
              f"p*(L*(w^M-w))={pLW:.2e} p*(f^M-f)={pdiff:.2e}")
        for r in [0.3, 0.1, 0.03, 0.01, -0.03]:
            h = rng.standard_normal(n); h /= np.abs(h).sum()
            pi, A, W = pstar_dec(f + r * h, mu, Phi, U)
            B = (A - a) / r
            Lam = sum(min(abs(a[j]), max(-s[j] * r * B[j], 0.0)) for j in F if j >= Mt)
            lhs, _, _ = pstar_dec(fM + r * h, mu, Phi, U)
            rhs = pi + 2 * Lam + 2 * UaM + pLW
            naive = pi + pdiff
            worst = max(worst, lhs - rhs)
            print(f"   r={r:6.3f}: LHS={lhs:.7f}  LT-RHS={rhs:.7f} (slack {rhs - lhs:.2e}, Lambda={Lam:.2e})  naive-RHS={naive:.7f}")
print("max violation (LHS - LT-RHS) over all tests:", worst)
