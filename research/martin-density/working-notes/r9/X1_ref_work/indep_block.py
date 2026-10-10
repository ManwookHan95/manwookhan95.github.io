"""X1-ref independent checks of Lemma K, Lemma F and the floor-form inward identity.

Block model (note, lem:threshold): |x|_Phi on l_1 with unit ball B_{l_1} + D(B_{l_2}), dual norm N(w) = ||w||_inf + ||D w||_2.
For a block vector zeta (= R_m^** zhat) the norming functional w satisfies zeta/A = alpha + D^2 w / C, M = ||w||_inf, C = ||Dw||_2,
M + C = 1, alpha >= 0-signed on the peak set P = {|w| = M}.

Independent solver 1 (double precision, cvxpy): maximise <w, zeta> subject to ||w||_inf + ||D w||_2 <= 1  (A = optimal value).
Independent solver 2 (mpmath, 60 digits): bisection on the threshold equation obtained from (E1),(E2):
    g(theta) := [sum_{nu > theta} Phi^2 (nu - theta)]^2 - theta^2 sum_{nu > theta} Phi^2 - sum_{nu <= theta} nu^2 Phi^2 = 0,
then A = sum_P Phi^2 (nu - theta), M = theta/(A + theta), C = A/(A + theta)  (U1 Lemma 1.2).  This differs from the fixed-point
solver used by X1/U1-ref (status_rigidity.py).
"""
import mpmath as mp, random, numpy as np
import cvxpy as cp

mp.mp.dps = 60
random.seed(2026)

def solve_E(zeta, Phi):
    n = len(zeta)
    nu = [abs(zeta[k]) / Phi[k]**2 for k in range(n)]
    def g(th):
        P = [k for k in range(n) if nu[k] > th]
        s1 = mp.fsum(Phi[k]**2 * (nu[k] - th) for k in P)
        return s1**2 - th**2 * mp.fsum(Phi[k]**2 for k in P) - mp.fsum(nu[k]**2 * Phi[k]**2 for k in range(n) if k not in P)
    lo, hi = mp.mpf(0), max(nu)
    for _ in range(600):
        mid = (lo + hi) / 2
        if g(mid) > 0: lo = mid
        else: hi = mid
    th = (lo + hi) / 2
    P = [k for k in range(n) if nu[k] >= th]
    A = mp.fsum(Phi[k]**2 * (nu[k] - th) for k in P)
    M = th / (A + th); C = A / (A + th)
    return A, th, M, C, nu, P

def K(sig, R2):
    return (sig + mp.sqrt(sig**2 * R2 + sig * (1 - R2))) / (1 - R2)

# ---------- (1) cross-check of the threshold structure against cvxpy (double precision) ----------
print("(1) cvxpy cross-check of the block threshold structure")
worst = 0.0
for trial in range(12):
    n = random.randint(4, 7); m = random.randint(1, 3)
    Phi = [2.0**(-(m + k + 1)) * random.uniform(0.3, 1) for k in range(n)]
    zeta = [random.choice([-1, 1]) * Phi[k]**2 * random.uniform(0, 4) for k in range(n)]
    w = cp.Variable(n)
    cons = [cp.norm(w, 'inf') + cp.norm(cp.multiply(np.array(Phi), w), 2) <= 1]
    prob = cp.Problem(cp.Maximize(np.array(zeta) @ w), cons)
    prob.solve(solver='CLARABEL', tol_gap_abs=1e-12, tol_gap_rel=1e-12, tol_feas=1e-12)
    A_cvx = prob.value
    wv = w.value; Mc = np.max(np.abs(wv)); Cc = np.linalg.norm(np.array(Phi) * wv)
    A, th, M, C, nu, P = solve_E([mp.mpf(z) for z in zeta], [mp.mpf(p) for p in Phi])
    # off-peak prediction w(k) = C zeta(k)/(Phi_k^2 A) and |w| = M on P
    pred = [float(C * zeta[k] / (Phi[k]**2 * A)) if k not in P else float(M) * np.sign(zeta[k]) for k in range(n)]
    e = max(abs(A_cvx - float(A)) / float(A), abs(Mc - float(M)), abs(Cc - float(C)), max(abs(wv[k] - pred[k]) for k in range(n)))
    worst = max(worst, e)
print("   12 random blocks: max discrepancy (A rel., M, C, w entries) =", "%.2e" % worst)

# ---------- (2) Lemma R-kt / Lemma K closed form, root choice, monotonicity ----------
print("(2) Lemma K: closed form, root selection, monotonicity, uniform form")
errK = errE = mp.mpf(0); minus_root_ok = True; mono_ok = True; cnt = 0
for trial in range(400):
    n = random.randint(4, 9); m = random.randint(1, 3)
    Phi = [mp.mpf(2)**(-(m + k + 1)) * mp.mpf(random.uniform(0.2, 1)) for k in range(n)]
    zeta = [mp.mpf(random.choice([-1, 1])) * Phi[k]**2 * mp.mpf(random.uniform(0, 3)) for k in range(n)]
    A, th, M, C, nu, P = solve_E(zeta, Phi)
    Q = [k for k in range(n) if k not in P]
    if not P or not Q: continue
    Om = [k for k in Q if random.random() < 0.6] or [Q[0]]
    Sf = mp.fsum((nu[k] * Phi[k])**2 for k in Q if k not in Om)
    kap = (A * (A + th) - mp.fsum((nu[k] * Phi[k])**2 for k in Om)) / th
    lam = [m * Phi[k] for k in range(n)]
    r = {k: (zeta[k] / lam[k]) / kap for k in Om}           # u_k(zhat)/kappa, since zeta(k) = lambda_k u_k(zhat)
    R2 = m**2 * mp.fsum(r[k]**2 for k in Om)
    sig = mp.fsum(Phi[k]**2 for k in P) + Sf / th**2
    k_true = kap / th
    errK = max(errK, abs(k_true - K(sig, R2)) / k_true)
    kminus = (sig - mp.sqrt(sig**2 * R2 + sig * (1 - R2))) / (1 - R2)
    if not (kminus <= sig): minus_root_ok = False
    E = mp.fsum(Phi[k]**2 * min(mp.mpf(1), nu[k] / th)**2 for k in range(n))
    errE = max(errE, abs((A / th)**2 - E) / E)
    # rho_l = m |r_l| k / Phi_l
    for k in Om:
        errK = max(errK, abs(nu[k] / th - m * abs(r[k]) * k_true / Phi[k]) / (nu[k] / th + mp.mpf('1e-300')))
    # monotonicity of K on a grid around (sig, R2)
    h = mp.mpf('1e-20')
    if not (K(sig + h, R2) > K(sig, R2) and K(sig, R2 + h) > K(sig, R2)): mono_ok = False
    cnt += 1
# global monotonicity scan
for s in [mp.mpf(10)**(-j) for j in range(1, 8)] + [mp.mpf(1), mp.mpf(5)]:
    xs = [mp.mpf(i) / 200 for i in range(0, 199)]
    vals = [K(s, x) for x in xs]
    if any(vals[i + 1] <= vals[i] for i in range(len(vals) - 1)): mono_ok = False
print("   blocks %d: max rel err (k = K(sigma,R^2), rho = m|r|k/Phi) = %s; a^2 = E rel err = %s" % (cnt, mp.nstr(errK, 3), mp.nstr(errE, 3)))
print("   minus root always <= sigma (so a <= 0 excluded):", minus_root_ok, "; K increasing in sigma and R^2:", mono_ok)

# ---------- (3) floor-form inward identity: lambda vs Domega = vs gamma + Delta' m^2 |r| k ----------
print("(3) inward identity lambda_l vs_l Domega(l) = vs_l gamma_l + Delta'_m m^2 |r_l| k  (w from the duality map)")
err3 = mp.mpf(0)
for trial in range(200):
    n = random.randint(4, 8); m = random.randint(1, 3)
    Phi = [mp.mpf(2)**(-(m + k + 1)) * mp.mpf(random.uniform(0.2, 1)) for k in range(n)]
    zeta = [mp.mpf(random.choice([-1, 1])) * Phi[k]**2 * mp.mpf(random.uniform(0, 3)) for k in range(n)]
    A, th, M, C, nu, P = solve_E(zeta, Phi)
    Q = [k for k in range(n) if k not in P]
    if not Q or not P: continue
    kap = (A * (A + th) - mp.fsum((nu[k] * Phi[k])**2 for k in Q)) / th     # Omega = Q
    lam = [m * Phi[k] for k in range(n)]
    Delta = mp.mpf(random.uniform(-2, 2)); Dp = Delta * M
    for l in Q:
        wl = C * zeta[l] / (Phi[l]**2 * A)                 # duality map off the peak set
        vs = mp.sign(zeta[l]); gam = mp.mpf(random.uniform(-1, 1))
        Dom = gam / lam[l] + Delta * wl                     # Domega(l) = gamma_l/lambda_l + Delta w(l)
        r = (zeta[l] / lam[l]) / kap
        lhs = lam[l] * vs * Dom; rhs = vs * gam + Dp * m**2 * abs(r) * (kap / th)
        err3 = max(err3, abs(lhs - rhs) / (abs(lhs) + abs(rhs)))
print("   max rel err:", mp.nstr(err3, 3))
