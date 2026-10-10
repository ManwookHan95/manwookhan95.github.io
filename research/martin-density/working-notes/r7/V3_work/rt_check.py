"""Finite-model sanity check of Lemma 2.3 (raise transfer, RT) of V3.

Model: base coordinates j < n, diagonal base U (entries mu_j), blocks m = 1..M with K coordinates each,
carriers u_{k,m} in R^n with q*(u) = 1, Phi_m(k) <= 2^{-m-k}, lambda = m Phi.
q*(A) = ||A||_1 + ||mu * A||_2 ;  N_m(W) = ||W||_inf + ||Phi_m * W||_2 ;  p*(h) = min max(q*(A), max_m N_m(W_m)), A + sum R_m* W_m = h.
First row from forced data (a, z) as in Remark rem:lemmaZ(c).  Raise: Delta a on supp a with the signs of a.
Checks:  p*(f# + r h) <= 1 + (p*(f + lam r h) - 1 + 2||U* Da||)/lam + p*(L*(w# - w))   (RT)
and reports the transfer error eps' = 2||U* Da|| + p*(L*(w# - w)) versus p*(f# - f).
"""
import numpy as np, cvxpy as cp

rng = np.random.default_rng(1)
n, M, K = 14, 2, 6

def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)

def make_model(mu_scale):
    mu = mu_scale * 0.5 ** (np.arange(n) ** 1.3)       # fast-decaying diagonal base
    Phi = {m: np.array([2.0 ** (-m - k) * (0.5 + 0.5 * rng.random()) for k in range(K)]) for m in range(1, M + 1)}
    U = {}
    for m in range(1, M + 1):
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
    # |x|_m = min ||alpha||_1 + ||beta||_2,  x = alpha + Phi*beta
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
    zhat = z + mu * (mu * a) / nu              # z + U e,  e = U* a / nu
    zeta = {m: np.array([m * Phi[m][k] * U[(k, m)] @ zhat for k in range(K)]) for m in range(1, M + 1)}
    q0 = 1.0 / (1.0 + sum(block_norm(zeta[m], Phi[m]) for m in zeta))
    w = {m: norming(zeta[m], Phi[m]) for m in zeta}
    f = a + sum(Rstar(m, w[m], Phi, U) for m in w)
    return f, w, q0, zhat

def pstar(h, mu, Phi, U):
    A = cp.Variable(n); W = {m: cp.Variable(K) for m in range(1, M + 1)}; tau = cp.Variable()
    cons = [cp.norm1(A) + cp.norm2(cp.multiply(mu, A)) <= tau]
    expr = A
    for m in W:
        cons.append(cp.norm_inf(W[m]) + cp.norm2(cp.multiply(Phi[m], W[m])) <= tau)
        expr = expr + sum(m * Phi[m][k] * W[m][k] * U[(k, m)] for k in range(K))
    cons.append(expr == h)
    pr = cp.Problem(cp.Minimize(tau), cons)
    pr.solve(solver="CLARABEL")
    return pr.value

worst = -1e9
for trial in range(6):
    mu, Phi, U = make_model(0.5)
    supp = np.arange(8)                       # F = {0..7}; coordinates 8..13 off F
    a = np.zeros(n); a[supp] = rng.choice([-1, 1], len(supp)) * (0.5 ** supp) * (0.3 + rng.random(len(supp)))
    a /= qstar(a, mu)
    z = np.zeros(n); z[supp] = np.sign(a[supp]); z[8:] = rng.uniform(-1, 1, n - 8); z[8] = 1.0  # one contact
    f, w, q0, zhat = first_row(a, z, mu, Phi, U)
    pf = pstar(f, mu, Phi, U)
    # raise on the deep support coordinates 5..7 (tiny mu there)
    Da = np.zeros(n); Da[5:8] = np.sign(a[5:8]) * rng.uniform(0.02, 0.08, 3)
    lam = qstar(a + Da, mu)
    a_s = (a + Da) / lam
    f_s, w_s, q0_s, zhat_s = first_row(a_s, z, mu, Phi, U)
    UDa = np.linalg.norm(mu * Da)
    LW = sum(Rstar(m, w_s[m] - w[m], Phi, U) for m in w)
    pLW = pstar(LW, mu, Phi, U)
    eps_prime = 2 * UDa + pLW
    pdiff = pstar(f_s - f, mu, Phi, U)
    print(f"trial {trial}: p*(f)={pf:.6f} lam={lam:.4f} ||Da||_1={np.abs(Da).sum():.3e} ||U*Da||={UDa:.2e} "
          f"p*(L*(w#-w))={pLW:.2e} eps'={eps_prime:.2e}  vs p*(f#-f)={pdiff:.2e}")
    for r in [0.3, 0.1, 0.03, 0.01]:
        h = rng.standard_normal(n); h /= np.abs(h).sum()
        lhs = pstar(f_s + r * h, mu, Phi, U)
        rhs = 1 + (pstar(f + lam * r * h, mu, Phi, U) - 1 + 2 * UDa) / lam + pLW
        worst = max(worst, lhs - rhs)
        print(f"   r={r:5.2f}: LHS={lhs:.7f}  RHS={rhs:.7f}  RHS-LHS={rhs - lhs:.2e}")
print("max violation (LHS - RHS) over all tests:", worst)
