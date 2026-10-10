"""Independent referee check of V3 Lemma 2.3 (raise transfer), its VP-corrected variant, Corollary 2.4,
and the size of the transfer error eps' versus p*(f# - f).

Finite model: base coordinates j < n, diagonal U (entries mu_j), blocks m = 1..M with K coordinates each.
q*(A) = ||A||_1 + ||mu*A||_2 ; N_m(W) = ||W||_inf + ||Phi_m W||_2 ; R_m* W = sum_k m Phi_m(k) W(k) u_{k,m}.
p*(h) = min max(q*(A), max_m N_m(W_m)) over A + sum_m R_m* W_m = h  (lem:dualball).
Rows from forced data (a, z) (rem:lemmaZ(c)): e = U*a/nu, zhat = z + U e, zeta_m = R_m** zhat, w_m = J_m(zeta_m), f = a + L* w.
"""
import numpy as np, cvxpy as cp, sys

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 7)
n, M, K = 12, 2, 5

def qstar(A, mu):
    return np.abs(A).sum() + np.linalg.norm(mu * A)

def model():
    mu = 0.5 * 0.45 ** (np.arange(n) ** 1.25)
    Phi = {m: 2.0 ** (-m - np.arange(K)) * (0.4 + 0.6 * rng.random(K)) for m in range(1, M + 1)}
    U = {}
    for m in range(1, M + 1):
        for k in range(K):
            u = rng.standard_normal(n) * (rng.random(n) < 0.8)
            if not u.any():
                u[0] = 1.0
            U[(k, m)] = u / qstar(u, mu)
    return mu, Phi, U

def Rstar(m, W, Phi, U):
    return sum(m * Phi[m][k] * W[k] * U[(k, m)] for k in range(K))

def norming(x, Phim):
    w = cp.Variable(K)
    pr = cp.Problem(cp.Maximize(x @ w), [cp.norm_inf(w) + cp.norm2(cp.multiply(Phim, w)) <= 1])
    pr.solve(solver="CLARABEL")
    return w.value, pr.value

def row(a, z, mu, Phi, U):
    nu = np.linalg.norm(mu * a)
    e = mu * a / nu                      # U* a / nu  (H = R^n, U = diag(mu))
    zhat = z + mu * e
    w = {}
    for m in range(1, M + 1):
        zeta = np.array([m * Phi[m][k] * (U[(k, m)] @ zhat) for k in range(K)])
        w[m], _ = norming(zeta, Phi[m])
    f = a + sum(Rstar(m, w[m], Phi, U) for m in w)
    return f, w, e, zhat

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

def s(t):
    return np.sqrt(1 + t * t)

worst_rt, worst_vp, worst_cor = -1e9, -1e9, -1e9
for trial in range(5):
    mu, Phi, U = model()
    F = np.arange(7)
    a = np.zeros(n); a[F] = rng.choice([-1, 1], len(F)) * 0.6 ** F * (0.2 + rng.random(len(F)))
    a /= qstar(a, mu)
    z = np.zeros(n); z[F] = np.sign(a[F]); z[7:] = rng.uniform(-1, 1, n - 7); z[7] = np.sign(z[7]) or 1.0
    f, w, e, zhat = row(a, z, mu, Phi, U)
    assert abs(pstar(f, mu, Phi, U) - 1) < 1e-6
    for size in [0.03, 0.3, 1.0]:          # raise masses up to O(1): lambda up to ~2
        Da = np.zeros(n); Da[3:7] = np.sign(a[3:7]) * size * rng.random(4)
        # VP-type correction of arbitrary sign on F0 = {0,1}, |Da''| <= |a|/2 (here random, not value-preserving)
        Dpp = np.zeros(n); Dpp[:2] = rng.uniform(-0.5, 0.5, 2) * np.abs(a[:2]) * (size > 0.1)
        for corr in [False, True]:
            D = Da + (Dpp if corr else 0)
            lam = qstar(a + D, mu)
            if lam < 1:
                print("lam < 1, skip", lam); continue
            fs, ws, es, zs = row((a + D) / lam, z, mu, Phi, U)
            UD = np.linalg.norm(mu * D)
            pLW = pstar(sum(Rstar(m, ws[m] - w[m], Phi, U) for m in w), mu, Phi, U)
            extra = 2 * np.abs(Dpp).sum() if corr else 0.0
            for r in [1.0, 0.3, 0.05, 0.01]:
                for _ in range(3):
                    h = rng.standard_normal(n); h /= np.abs(h).sum()
                    lhs = pstar(fs + r * h, mu, Phi, U)
                    rhs = 1 + (pstar(f + lam * r * h, mu, Phi, U) - 1 + 2 * UD + extra) / lam + pLW
                    if corr:
                        worst_vp = max(worst_vp, lhs - rhs)
                    else:
                        worst_rt = max(worst_rt, lhs - rhs)
            if not corr:
                print(f"trial {trial} size {size}: lam={lam:.3f} ||Da||_1={np.abs(D).sum():.2e} ||U*Da||={UD:.2e} "
                      f"p*(L*(w#-w))={pLW:.2e} p*(f#-f)={pstar(fs - f, mu, Phi, U):.2e}")
    # Corollary 2.4 with an actual (numerical) mate g: h with h(xi)=0, scaled until p*(f+tg) <= s(t) on a grid
    xi_dir = zhat                          # xi is a positive multiple of zhat
    h = rng.standard_normal(n); h -= (h @ xi_dir) / (a @ xi_dir) * a   # h(zhat) = 0 (a(zhat) = 1)
    ts = np.concatenate([-np.logspace(-3, 1.5, 25), np.logspace(-3, 1.5, 25)])
    c = 1.0
    for _ in range(40):
        if all(pstar(f + t * c * h, mu, Phi, U) <= s(t) + 1e-9 for t in ts):
            break
        c *= 0.7
    g = c * h
    Da = np.zeros(n); Da[3:7] = np.sign(a[3:7]) * 0.5 * rng.random(4)
    lam = qstar(a + Da, mu)
    fs, ws, es, zs = row((a + Da) / lam, z, mu, Phi, U)
    UD = np.linalg.norm(mu * Da)
    pLW = pstar(sum(Rstar(m, ws[m] - w[m], Phi, U) for m in w), mu, Phi, U)
    for rho in [1.0, 0.8]:
        for r in [-3, -0.5, -0.05, 0.02, 0.4, 2.0]:
            lhs = pstar(fs + r * rho * g, mu, Phi, U)
            rhs = 1 + (s(lam * rho * r) - 1) / lam + 2 * UD + pLW
            worst_cor = max(worst_cor, lhs - rhs)
print("max violation RT:", worst_rt, " RT with VP-type correction:", worst_vp, " Cor 2.4 (numerical mate):", worst_cor)
