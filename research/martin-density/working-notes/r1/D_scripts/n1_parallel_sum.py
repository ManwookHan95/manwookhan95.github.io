# N1: second-order behaviour of the gauge of a Minkowski sum B = K1 + K2 (dual balls add).
# Claim: if f = a + k on boundary of B with common normal xi (normalized f(xi)=1),
# q0 = h_{K1}(xi), then d^2/dt^2 gauge_B(f+tg) at 0 equals
#   Q(g) = inf_{b+c=g, b(xi)=c(xi)=0} [ q0*A(b) + (1-q0)*B(c) ],
# where A(b) = d^2/dt^2 gauge_{K1}(a+tb), B(c) = d^2/dt^2 gauge_{K2}(k+tc) at t=0.
import numpy as np
rng = np.random.default_rng(1)

def h_ell(M, x):            # support function of ellipsoid {M u : |u|<=1}
    return np.linalg.norm(M.T @ x)

def gauge_from_support(hfun, y, dirs):   # gauge_B(y) = max_x <x,y>/h_B(x)
    vals = (dirs @ y) / np.array([hfun(x) for x in dirs])
    return vals.max()

def refine_gauge(hfun, y, n):
    # maximize <x,y>/h(x) over unit sphere in R^n via random restarts + local ascent
    best = -np.inf; bx = None
    for _ in range(40):
        x = rng.normal(size=n); x /= np.linalg.norm(x)
        step = 0.3
        val = (x @ y) / hfun(x)
        for it in range(3000):
            cand = x + step * rng.normal(size=n); cand /= np.linalg.norm(cand)
            cv = (cand @ y) / hfun(cand)
            if cv > val: x, val = cand, cv
            else: step *= 0.995
            if step < 1e-12: break
        if val > best: best, bx = val, x
    return best

def run(n):
    M1 = rng.normal(size=(n, n)); M2 = 0.6 * rng.normal(size=(n, n))
    hB = lambda x: h_ell(M1, x) + h_ell(M2, x)
    x = rng.normal(size=n); xi = x / hB(x)          # normer, h_B(xi)=1
    a = M1 @ (M1.T @ xi) / np.linalg.norm(M1.T @ xi)  # grad h1 at xi
    k = M2 @ (M2.T @ xi) / np.linalg.norm(M2.T @ xi)  # grad h2 at xi
    f = a + k
    q0 = h_ell(M1, xi)
    print("n=%d  f(xi)=%.6f  q0=%.4f" % (n, f @ xi, q0))
    # exact gauges of ellipsoids: gauge_{E}(y) = |M^{-1} y|
    g1 = lambda y: np.linalg.norm(np.linalg.solve(M1, y))
    g2 = lambda y: np.linalg.norm(np.linalg.solve(M2, y))
    # Hessians of the ellipsoid gauges (as quadratic forms on tangent space ker xi)
    def hess(gf, p):
        hh = 1e-4; H = np.zeros((n, n)); I = np.eye(n)
        for i in range(n):
            for j in range(n):
                H[i, j] = (gf(p + hh*I[i] + hh*I[j]) - gf(p + hh*I[i] - hh*I[j])
                           - gf(p - hh*I[i] + hh*I[j]) + gf(p - hh*I[i] - hh*I[j])) / (4*hh*hh)
        return H
    HA = hess(g1, a); HB = hess(g2, k)
    # tangent basis of ker xi
    Q, _ = np.linalg.qr(np.column_stack([xi] + [rng.normal(size=n) for _ in range(n-1)]))
    T = Q[:, 1:]
    A_t = T.T @ HA @ T; B_t = T.T @ HB @ T
    # parallel sum: inf_{b+c=g}[q0 A(b) + (1-q0) B(c)] = g^T (inv(q0 A)+inv((1-q0)B))^{-1} g
    P = np.linalg.inv(np.linalg.inv(q0 * A_t) + np.linalg.inv((1 - q0) * B_t))
    for trial in range(3):
        coef = rng.normal(size=n-1); gv = T @ coef
        pred = coef @ P @ coef
        # numerical second derivative of gauge_B(f + t g)
        hh = 2e-3
        G = lambda t: refine_gauge(hB, f + t*gv, n)
        g0, gp, gm = G(0.0), G(hh), G(-hh)
        num = (gp + gm - 2*g0) / hh**2
        print("  trial %d: gauge(f)=%.8f  numeric d2=%.5f  parallel-sum pred=%.5f  max(A,B)-split pred=%.5f"
              % (trial, g0, num, pred,
                 min(max(coef@A_t@coef*s*s, coef@B_t@coef*(1-s)**2) for s in np.linspace(0,1,2001))))
run(2)
run(3)
